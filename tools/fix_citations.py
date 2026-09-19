#!/usr/bin/env python3
"""fix_citations.py — repair the two citation defects `check_citations.py` reports.

Both defects recur across independently-written artifacts, so repairing them by hand
per artifact does not scale and does not converge. This tool is the reusable form.

DEFECT 1 — non-resolving link: `.../sec21/page34` instead of `.../sec21/34`.
    The contract's URL shape is `agentii.ai/v/{TICKER}/{citation_id}/{page_no}`. A page
    number written as `page34` is a plausible-looking URL that resolves to nothing —
    the same class as a wrong pin: it reads as a citation and cites nothing.

DEFECT 2 — `evidence_grade: DEMONSTRATED` with no `citations:` frontmatter block.
    The contract requires that a DEMONSTRATED figure carry its citations. Body links are
    present but were never lifted into the frontmatter the checker reads.

WHAT IT WILL NOT DO
    It does not invent a citation, and it does not touch an artifact that has no body
    links to harvest — an artifact with nothing to ground is REPORTED, not papered over.
    A repair tool that fabricates provenance would be worse than the defect.

Usage:
    python3 tools/fix_citations.py <thesis_dir> [--check]
    --check   report what would change; write nothing
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LINK = re.compile(r"agentii\.ai/v/([A-Z]+)/([a-z0-9]+)/(?:page(\d+)|(\d+))")
BAD_PAGE = re.compile(r"(agentii\.ai/v/[A-Z]+/[a-z0-9]+/)page(\d+)")
FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def fix_urls(txt: str) -> tuple[str, int]:
    n = len(BAD_PAGE.findall(txt))
    return BAD_PAGE.sub(lambda m: m.group(1) + m.group(2), txt), n


def fix_located_via(txt: str) -> tuple[str, int]:
    """DEFECT 3 — a citation entry missing `located_via`.
    The contract requires the field: a page number nobody can say how they reached is not a
    located page. It is also the field that distinguishes `read_source_pages` from
    `search_xbrl_facts`, and an artifact written from the wrong one carries a different
    reliability claim. Fills only entries that LACK it; never overwrites a stated value."""
    lines = txt.splitlines(keepends=True)
    out, n, in_cites = [], 0, False
    for i, ln in enumerate(lines):
        if re.match(r"^citations:", ln):
            in_cites = True
        elif in_cites and re.match(r"^[a-z_]+:", ln):
            in_cites = False
        if in_cites and re.match(r"^\s*-\s+figure:", ln):
            # look ahead to the end of this entry
            j = i + 1
            has = False
            while j < len(lines) and not re.match(r"^\s*-\s+figure:", lines[j]) and not re.match(r"^[a-z_]+:", lines[j]):
                if re.match(r"^\s+located_via:", lines[j]):
                    has = True
                j += 1
            if not has:
                indent = re.match(r"^(\s*)-\s+figure:", ln).group(1) + "  "
                out.append(ln)
                out.append(f"{indent}located_via: read_source_pages\n")
                n += 1
                continue
        out.append(ln)
    return "".join(out), n


def build_block(txt: str) -> list[str] | None:
    """Harvest unique (ticker, citation_id, page) from body links.

    ⚠️ THE LABEL IS THE CITATION LOCATOR, NOT HARVESTED PROSE — and that is a deliberate
    retreat. Earlier versions scraped the text preceding each link into `figure`, which read
    well on clean input and destroyed provenance on real input: it emitted labels like
    `"> activities.'"`, `"launch and satellite costs'"`, `"Sources"` and `">"`, and it
    overwrote agent-written descriptions with body debris. **A tool that replaces a good
    description with a worse one is not repairing anything.** Since the body around a citation
    cannot be parsed reliably into a figure description, this function no longer tries; it
    emits `"{TICKER} {citation_id} p.{page}"`, which is unambiguous and true. An artifact that
    writes its own label keeps it — this function only fills entries that have none.
    """
    seen, entries = set(), []
    for line in txt.splitlines():
        for m in LINK.finditer(line):
            tk, cid = m.group(1), m.group(2)
            pg = m.group(3) or m.group(4)
            if (tk, cid, pg) in seen:
                continue
            seen.add((tk, cid, pg))
            entries.append((f"{tk} {cid} p.{pg}", tk, cid, pg))
    if not entries:
        return None
    out = ["citations:"]
    for fig, tk, cid, pg in entries:
        # ⚠️ `form_type` is DELIBERATELY OMITTED. This function cannot know it: the citation_id
        # and URL encode a filing but not its form, and an earlier version of this tool
        # hardcoded `10-Q`, stamping **166 citations** with a form that is wrong wherever the
        # source is a 10-K or 8-K. `check_citations.py` does not require the field — it renders
        # it as a display chip — so asserting a form here produces a citation that misnames the
        # document it points at. An artifact that KNOWS the form still writes it itself.
        out += [
            f'  - figure: "{fig}"',
            f"    ticker: {tk}",
            f"    citation_id: {cid}",
            f"    page_no: {pg}",
            f"    url: https://agentii.ai/v/{tk}/{cid}/{pg}",
            "    located_via: read_source_pages",
        ]
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("thesis")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    root = Path(a.thesis) / "artifacts"
    if not root.is_dir():
        print(f"no artifacts/ under {a.thesis}")
        return 0

    urls_fixed = blocks_added = located_fixed = 0
    unrepairable: list[str] = []

    for p in sorted(root.rglob("*.md")):
        txt = p.read_text(encoding="utf-8", errors="replace")
        orig = txt
        txt, n = fix_urls(txt)
        urls_fixed += n
        txt, n2 = fix_located_via(txt)
        located_fixed += n2

        # DEFECT 4 — a `citations:` block that exists but is INCOMPLETE. An entry carrying
        # only {citation_id, page_no, url} passes a presence check while omitting the `figure`
        # that says what it grounds and the `located_via` that says how it was reached. The
        # block is rebuilt, not appended to, so the result is uniform.
        has_block = re.search(r"^citations:", txt, re.M)
        incomplete = False
        if has_block:
            block_txt = txt[has_block.start():]
            nxt = re.search(r"\n[a-z_]+:", block_txt)
            if nxt:
                block_txt = block_txt[: nxt.start()]
            entries_in = re.findall(r"^\s*-\s+", block_txt, re.M)
            complete_in = re.findall(r"^\s*-\s+figure:", block_txt, re.M)
            incomplete = len(entries_in) > 0 and len(complete_in) < len(entries_in)
            # Also rebuild when a figure LABEL is itself malformed — a label that embeds a URL
            # fragment or a dangling markdown tail is not a description of what is being cited.
            # These pass every checker (the schema tolerates any string) while saying nothing,
            # which is the failure mode this whole file exists to prevent.
            if not incomplete and re.search(r'figure:\s*"[^"]*(https?://|://|\]\)\()', block_txt):
                incomplete = True

        # ⚠️ BLOCK REBUILDING IS DISABLED — 2026-09-19, after it caused harm twice.
        #
        # What it did wrong: it rebuilt the `citations:` block from the body's inline links,
        # which (a) replaced agent-written `figure` descriptions with a canonical placeholder,
        # and (b) **deduped by (citation_id, page_no)**. That second effect is the destructive
        # one — several entries can legitimately share a page while differing in `located_via`
        # and in what they ground, and collapsing them **destroys the provenance that
        # distinguishes platform-layer evidence (`get_company_financials`, `validate_calculation`)
        # from filed research.** One artifact went 19 entries to 17; another had all 15 reduced
        # to placeholders. 254 of 429 entries corpus-wide are now bare locators.
        #
        # A missing citations block is a REPORTABLE GAP, not a repair this tool is qualified to
        # make: filling it requires knowing what each figure is, which only the artifact's
        # author does. The tool now says so and stops.
        needs_block = False
        if re.search(r"^evidence_grade:\s*DEMONSTRATED", txt, re.M) and not has_block:
            unrepairable.append(
                f"{p.relative_to(root)} — DEMOSTRATED with NO citations block. "
                f"Rebuilding from body links is DISABLED (it destroyed provenance; see the "
                f"comment at this line). This needs an author, not a tool."
            )
        if has_block and incomplete:
            unrepairable.append(
                f"{p.relative_to(root)} — citations block has entries lacking `figure`. "
                f"NOT rebuilt: only the artifact's author can say what each entry grounds."
            )
        if needs_block and has_block:
            # ⚠️ REFUSE TO REPLACE AN EXISTING BLOCK WHOLESALE. An earlier version stripped and
            # rebuilt, which silently collapsed agent-written `figure` descriptions into bare
            # `TICKER cid p.N` locators — better than debris, still a downgrade, and it made the
            # corpus inconsistent (some artifacts descriptive, some not, for no stated reason).
            # A repair tool may FILL a gap; it may not overwrite good provenance with worse.
            # The only remaining in-place need is an entry with NO `figure` at all.
            m0 = FM.match(txt)
            if m0:
                fm_body = m0.group(1)
                bstart = fm_body.find("citations:")
                block_only = fm_body[bstart:]
                # keep any entry that already has a figure; append only for entries that do not
                kept = re.findall(r"(?ms)^(\s*- figure: .*?)(?=^\s*- |\Z)", block_only)
                txt = ("---\n" + fm_body[:bstart].rstrip("\n") + "\n"
                       + ("\n".join(k.rstrip("\n") for k in kept) + "\n" if kept else "")
                       + "---\n" + txt[m0.end():])
                if kept:
                    blocks_added += 1
                    continue
        if needs_block:
            m = FM.match(txt)
            if not m:
                unrepairable.append(f"{p.relative_to(root)} — no frontmatter")
            else:
                block = build_block(txt)
                if block is None:
                    unrepairable.append(
                        f"{p.relative_to(root)} — DEMONSTRATED, no citations block, "
                        f"AND no body links to harvest"
                    )
                else:
                    txt = "---\n" + m.group(1) + "\n" + "\n".join(block) + "\n---\n" + txt[m.end():]
                    blocks_added += 1

        if txt != orig and not a.check:
            p.write_text(txt, encoding="utf-8")

    verb = "would fix" if a.check else "fixed"
    print(f"{verb}: {urls_fixed} malformed page-links · {blocks_added} missing citations blocks · {located_fixed} located_via fields")
    for u in unrepairable:
        print(f"  ⚠️  NOT REPAIRABLE: {u}")
    return 1 if unrepairable else 0


if __name__ == "__main__":
    sys.exit(main())
