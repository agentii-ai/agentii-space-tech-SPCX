#!/usr/bin/env python3
"""fetch_filing_figures.py — pull filer-embedded images out of an SEC exhibit.

WHY THIS IS THESIS-SIDE AND NOT IN THE KIT
    `synthesize_report.py assemble` must stay deterministic and offline: it pins
    `sources_hash` over file bytes and refuses to produce a report whose sources
    moved underneath it. A network fetch inside that path would make the pin
    meaningless. So the bytes are fetched HERE, written to disk, and hashed like
    any other source — the assembler only ever reads a local file.

WHAT IT GETS, AND WHY THERE IS NO IMAGE URL
    agentii.ai does not host filing images as separate assets. The filer's own
    JPEGs are carried inside the `combined.htm` artifact and served INLINE as
    base64 `data:` URIs, so the only way to obtain one is to fetch the document
    and lift the payload out of its `<img src>`. `COMBINED_HTML_METADATA` in the
    same response publishes `images_embedded`, which is the authoritative count:
    we check it and REFUSE on a disagreement rather than guessing an index.

    Verified 2026-09-19 against SPCX/sec7 (8-K EX-99.1): 10 images, one per page,
    pages 4–13, each 1055x1365. SPCX/sec8 (the 10-Q) has ZERO — a document with
    no images is the common case, not an error, but it is not a silent one.

PLATFORM POLICY — READ BEFORE USING
    agentii.ai and its R2 backing are RATE-LIMITED, and there is no per-image
    endpoint: every figure costs a full-document GET. This tool is for QUOTING a
    few figures with attribution into a report, NOT for collecting filings. The
    position is that a reader may read documents on the platform; a report may
    quote a handful. Accordingly:

      * a report embeds AT MOST FIVE filing figures. Enforced in the assembler
        (`MAX_FILING_FIGURES`), so it holds whichever route the bytes arrived by;
      * a document offering more than `--max-images` (default 5) is REFUSED here;
      * a second run costs NOTHING — if every recorded figure is already on disk
        and complete, no request is made at all (`--refresh` to override).

    If you find yourself raising these limits, the thing being built is a mirror
    of the corpus, and it should not be built from this endpoint.

USAGE
    python3 tools/fetch_filing_figures.py --ticker SPCX --citation-id sec7

    Writes report/assets/<ticker>-<cid>-p<NN>.jpg + manifest.json beside them.
    Idempotent twice over: no GET when the manifest is complete on disk, and no
    write when a file's sha256 already matches.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.agentii.ai/v1/view_document/{ticker}/{cid}"
UA = "agentii-space-tech-SPCX figure fetch (research; contact repo owner)"

# JPEG SOI/EOI. A payload that does not both open and close as JPEG is corrupt
# or is not a JPEG at all — either way it must not reach the report.
JPEG_SOI = b"\xff\xd8\xff"
JPEG_EOI = b"\xff\xd9"

# PLATFORM-PROTECTION CAP. agentii.ai serves documents from a rate-limited R2
# origin, and there is no per-image endpoint — a figure costs a FULL-DOCUMENT GET.
# The product position is that people may read filings on the platform; a report
# may quote a handful. Five is that budget, and it is enforced in the assembler
# (`MAX_FILING_FIGURES` in synthesize_report.py) as well as here, because the
# report is what gets distributed. This tool refuses a document that offers more
# than the caller asked for, rather than quietly pulling a hundred pages.
MAX_IMAGES_PER_REPORT = 5


class FigureFetchError(Exception):
    pass


def fetch_document(ticker: str, cid: str) -> str:
    url = API.format(ticker=ticker, cid=cid)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        if r.status != 200:
            raise FigureFetchError(f"{url} -> HTTP {r.status}")
        return r.read().decode("utf-8", errors="replace")


def parse_metadata(html: str) -> dict:
    m = re.search(r"COMBINED_HTML_METADATA:\s*(\{.*?\})\s*-->", html, re.S)
    if not m:
        raise FigureFetchError("no COMBINED_HTML_METADATA in response")
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as e:
        raise FigureFetchError(f"COMBINED_HTML_METADATA is not JSON: {e}") from e


def declared_image_count(meta: dict) -> int:
    """Sum of `images_embedded` across exhibits. Absent field == 0, not unknown:
    the publisher omits it when there is nothing to count."""
    return sum(int(e.get("images_embedded") or 0) for e in meta.get("exhibits", []))


def extract_images(html: str) -> list[dict]:
    """Every `<img>` carrying a base64 data URI, IN DOCUMENT ORDER, each tagged
    with the nearest preceding `apm-page{N}` anchor — that anchor is the only
    page attribution the artifact itself carries, so it is what we record."""
    out: list[dict] = []
    page = None
    for m in re.finditer(r'<img\b[^>]*>|apm-page(\d+)', html, re.I):
        if m.group(1) is not None:
            page = int(m.group(1))
            continue
        tag = m.group(0)
        src = re.search(r'src\s*=\s*["\'](data:image/(\w+);base64,([A-Za-z0-9+/=]+))["\']',
                        tag, re.I)
        if not src:
            continue
        raw = base64.b64decode(src.group(3))
        out.append({
            "page_no": page,
            "mime": f"image/{src.group(2).lower()}",
            "bytes": raw,
            "declared_height": (re.search(r'height\s*=\s*["\']?(\d+)', tag, re.I) or [None, None])[1],
        })
    return out


def verify(raw: bytes, where: str) -> None:
    if not raw.startswith(JPEG_SOI):
        raise FigureFetchError(f"{where}: payload does not begin with a JPEG SOI")
    if not raw.endswith(JPEG_EOI):
        raise FigureFetchError(f"{where}: payload does not end with a JPEG EOI "
                               "(truncated or re-encoded)")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--citation-id", required=True, dest="cid")
    ap.add_argument("--out", default="report/assets",
                    help="output dir relative to cwd (default: report/assets)")
    ap.add_argument("--list", action="store_true",
                    help="report what is available; write nothing")
    ap.add_argument("--refresh", action="store_true",
                    help="re-GET even when every recorded figure is already on disk")
    ap.add_argument("--max-images", type=int, default=MAX_IMAGES_PER_REPORT,
                    help=f"refuse if this document offers more than N images "
                         f"(default {MAX_IMAGES_PER_REPORT}; the per-report cap)")
    args = ap.parse_args(argv)

    # NO RE-DOWNLOAD OF WHAT WE ALREADY HOLD. The GET is the whole cost — there is
    # no per-image endpoint, so pulling bytes we already have is pure origin load
    # for zero new information. This is the guard that matters for a rate-limited
    # R2 origin: a second run is free, and only a genuinely new document costs.
    outdir = Path(args.out)
    manifest_path = outdir / "manifest.json"
    key = f"{args.ticker}/{args.cid}"
    if not args.refresh and manifest_path.exists():
        try:
            prior = json.loads(manifest_path.read_text()).get(key)
        except (OSError, ValueError):
            prior = None
        figs = (prior or {}).get("figures") or []
        if figs and all((outdir / f["file"]).is_file() for f in figs):
            print(f"{key}: {len(figs)} figure(s) already on disk and complete — "
                  "no request made. Use --refresh to re-GET.")
            for f in figs:
                print(f"    {f['file']}  p.{f['page_no']}  {f['bytes']:,} B")
            return 0

    html = fetch_document(args.ticker, args.cid)
    meta = parse_metadata(html)
    declared = declared_image_count(meta)
    images = extract_images(html)

    print(f"{args.ticker}/{args.cid}: declared={declared} extracted={len(images)}")
    if declared != len(images):
        raise FigureFetchError(
            f"declared {declared} embedded images but extracted {len(images)} — "
            "refusing to write, because the index a caller would pick may not be "
            "the index this parser found")
    if not images:
        print(f"  {args.ticker}/{args.cid} carries no filer-embedded images "
              "(the common case — most exhibits have none). Nothing to do.")
        return 0

    if args.list:
        for i, im in enumerate(images, 1):
            print(f"  {i:2d}. page {im['page_no']}  {im['mime']}  "
                  f"{len(im['bytes']):,} B  h={im['declared_height']}")
        return 0

    if len(images) > args.max_images:
        raise FigureFetchError(
            f"this document offers {len(images)} images but the cap is "
            f"{args.max_images}. A report quotes a few filings with attribution; "
            f"it does not mirror an exhibit. Raise --max-images deliberately if "
            f"this is a one-off, and keep the ASSEMBLED report at or under "
            f"{MAX_IMAGES_PER_REPORT} figures.")

    outdir.mkdir(parents=True, exist_ok=True)
    stem = meta.get("exhibits", [{}])[0].get("filename") or "doc"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    entry = manifest.setdefault(key, {
        "accession_number": meta.get("accession_number"),
        "form_type": meta.get("form_type"),
        "exhibit_filename": stem,
        "source_url": API.format(ticker=args.ticker, cid=args.cid),
        "figures": [],
    })

    written = skipped = 0
    seen: dict[str, int] = {}
    for i, im in enumerate(images, 1):
        page = im["page_no"] or 0
        base = f"{args.ticker}-{args.cid}-p{page:02d}"
        # Two images CAN share one page anchor — a logo repeated across a spread,
        # or an inline mark beside body text. Naming only by page made the second
        # SILENTLY OVERWRITE the first: measured 2026-09-19 on FLY/sec5, where 4
        # extracted images produced 3 files, `wrote 4` was printed, and the
        # manifest lost an entry. The declared-vs-extracted check could not catch
        # it because both said 4. An ordinal keeps every payload addressable.
        seen[base] = seen.get(base, 0) + 1
        name = f"{base}.jpg" if seen[base] == 1 else f"{base}-{seen[base]}.jpg"
        dest = outdir / name
        verify(im["bytes"], f"{key} image {i} ({name})")
        sha = hashlib.sha256(im["bytes"]).hexdigest()
        if dest.exists() and hashlib.sha256(dest.read_bytes()).hexdigest() == sha:
            skipped += 1
        else:
            dest.write_bytes(im["bytes"])
            written += 1
        entry["figures"] = [f for f in entry["figures"] if f["file"] != name] + [
            {"file": name, "page_no": page, "image_ordinal": i,
             "bytes": len(im["bytes"]), "sha256": sha,
             "declared_height": im["declared_height"]}]

    entry["figures"].sort(key=lambda f: f["page_no"])
    entry["fetched_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    print(f"  wrote {written}, unchanged {skipped} -> {outdir}/")
    for f in entry["figures"]:
        print(f"    {f['file']}  p.{f['page_no']}  {f['bytes']:,} B  {f['sha256'][:12]}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except FigureFetchError as e:
        print(f"REFUSED: {e}", file=sys.stderr)
        sys.exit(2)
