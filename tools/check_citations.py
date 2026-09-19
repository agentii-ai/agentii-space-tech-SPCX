#!/usr/bin/env python3
"""check_citations.py — enforce thesis 002's citation contract (spec §1d) across artifacts.

Three contract rules are level `fail` and this tool is their executable form:

  citations_present       a DEMONSTRATED figure must carry a citations block
  citation_url_wellformed the canonical URL, WITH the ticker
  citations_pages_located every page number must name the tool that found it

Why the third rule exists: **a page number that was not located by a tool is a guess, and
a guessed page number resolves to the wrong page — which is worse than no link, because it
looks correct.** The ticker-less short form `agentii.ai/v/{citation_id}/{page}` does not
resolve at all: the portal redirects to
`api.agentii.ai/v1/view_document/{ticker}/{citation_id}?page_no=page{N}` and joins
`src_documents` to `sec_filings`, a join that cannot be performed without it.

Usage
-----
  python3 tools/check_citations.py theses/002-evidence-validation
Exit code is the number of failing artifacts (0 = clean).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

URL_RE = re.compile(r"^https://agentii\.ai/v/[A-Z][A-Z0-9.\-]{0,6}/[a-z]+[0-9]+/[0-9]+$")
CID_RE = re.compile(r"^[a-z]+[0-9]+$")
TK_RE = re.compile(r"^[A-Z][A-Z0-9.\-]{0,6}$")
LOCATED = {"search_keyword_in_source", "read_source_outline", "read_source_pages",
           "citation_retrieved_at_specification"}
FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)
INLINE = re.compile(r"\((https://agentii\.ai/v/[^)]+)\)")


def check(path: Path, require_upstream_stale: bool = False) -> list[str]:
    """`require_upstream_stale` gates the 002-only stamp.

    `upstream_stale: "001@1.2.0"` records that **thesis 002** inherits an undischarged 001
    gate. It is not a workspace-wide rule, and applying it to every thesis reported all 49
    of thesis 001's artifacts as red — for carrying a stamp that would be wrong for them to
    carry, since 001 IS the upstream. Scope comes from the thesis, never from the tool.
    """
    errs: list[str] = []
    text = path.read_text(encoding="utf-8")
    m = FM.match(text)
    if not m:
        return ["no frontmatter block"]
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return [f"frontmatter does not parse: {str(e)[:80]}"]

    for pin in ("constitution_pin", "assumption_pin", "skill_pin", "as_of", "corpus_version"):
        if not fm.get(pin):
            errs.append(f"missing pin `{pin}`")

    grade = fm.get("evidence_grade")
    cites = fm.get("citations") or []

    # rule: citations_present
    if grade == "DEMONSTRATED" and not cites:
        errs.append("evidence_grade=DEMONSTRATED but no `citations` block")
    # rule: upstream_stale stamp — applies ONLY to the thesis that inherits the gate
    if require_upstream_stale and fm.get("upstream_stale") != "001@1.2.0":
        errs.append("missing or wrong `upstream_stale` — must be \"001@1.2.0\"")

    body = text[m.end():]
    for i, c in enumerate(cites):
        if not isinstance(c, dict):
            errs.append(f"citations[{i}] is not a mapping")
            continue
        tag = f"citations[{i}]"
        u = str(c.get("url", ""))
        # rule: citation_url_wellformed
        if not URL_RE.match(u):
            if "/v/" in u and not re.match(r"^https://agentii\.ai/v/[A-Z]", u):
                errs.append(f"{tag} url lacks a ticker (does NOT resolve): {u}")
            else:
                errs.append(f"{tag} url malformed: {u}")
        elif c.get("ticker") and f"/v/{c['ticker']}/" not in u:
            errs.append(f"{tag} url ticker != field ticker ({c['ticker']})")
        if c.get("citation_id") and not CID_RE.match(str(c["citation_id"])):
            errs.append(f"{tag} citation_id malformed: {c.get('citation_id')}")
        if c.get("ticker") and not TK_RE.match(str(c["ticker"])):
            errs.append(f"{tag} ticker malformed: {c.get('ticker')}")
        # rule: citations_pages_located
        lv = c.get("located_via")
        if lv not in LOCATED:
            errs.append(f"{tag} located_via={lv!r} — page number was not located by a tool")
        # body link must match the frontmatter url
        fig = str(c.get("figure", ""))[:40]
        if fig and u and u not in body:
            errs.append(f"{tag} url never appears as a link in the body ({fig}…)")

    # any inline /v/ link that is ticker-less
    for u in INLINE.findall(body):
        if not URL_RE.match(u):
            errs.append(f"body contains a non-resolving link: {u}")
    return errs


def repair(path: Path) -> bool:
    """Append/regenerate a body `## Sources` table from the frontmatter citations block.

    Spec §1d requires the links **in the body**; a frontmatter block alone fails. Six of the
    first eighteen artifacts needed this by hand, so it is now a flag. Regenerating rather
    than skipping matters: an artifact can gain a citation *after* its Sources section was
    written, and a skip-if-present repair would silently miss it. That happened at VOYG.
    """
    t = path.read_text(encoding="utf-8")
    m = FM.match(t)
    if not m:
        return False
    fm = yaml.safe_load(m.group(1)) or {}
    cites = [c for c in (fm.get("citations") or []) if isinstance(c, dict) and c.get("url")]
    if not cites:
        return False
    body = re.split(r"\n---\n\n## Sources\n", t[m.end():])[0]
    if not any(str(c["url"]) not in body for c in cites):
        return False
    rows = []
    for c in cites:
        pg = f" p.{c.get('page_no')}" if c.get("page_no") else ""
        chip = (f"[📄 {c.get('ticker')} {str(c.get('form_type','')).replace('_',' ')}"
                f"{pg}]({c['url']})")
        rows.append(f"| {re.sub(chr(92)+'s+',' ',str(c.get('figure',''))).strip()[:150]} | {chip}"
                    f"{'' if str(c['url']) in body else ' **(newly surfaced)**'} |")
    sec = ("\n\n---\n\n## Sources\n\n"
           "> Every figure asserted above resolves to the page cited. Regenerated from the\n"
           "> artifact's `citations` block — the frontmatter block alone does not satisfy\n"
           "> spec §1d, which requires the links **in the body**.\n\n"
           "| Figure | Source |\n|---|---|\n" + "\n".join(rows) + "\n")
    path.write_text(t[:m.end()] + body.rstrip() + sec, encoding="utf-8")
    return True


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    do_fix = "--fix" in sys.argv
    d = Path(args[0]) if args else Path(".")
    if do_fix:
        n = 0
        for f in list((d / "artifacts").rglob("*.md")) + list((d / "_cross").glob("*.md")):
            if repair(f):
                print(f"repaired: {f.relative_to(d)}")
                n += 1
        print(f"repaired {n} artifact(s)\n")
    arts = sorted((d / "artifacts").rglob("*.md")) if (d / "artifacts").is_dir() else []
    xcut = sorted((d / "_cross").glob("*.md")) if (d / "_cross").is_dir() else []
    files = arts + xcut
    if not files:
        print("no artifacts yet")
        return 0
    bad = 0
    urls = set()
    # The upstream-stale stamp is a property of thesis 002 (it inherits 001's gate). Derived
    # from the thesis directory, not applied globally.
    require_stale = "002" in d.name
    for f in files:
        rel = f.relative_to(d)
        errs = check(f, require_stale)
        fm = FM.match(f.read_text(encoding="utf-8"))
        if fm:
            for c in (yaml.safe_load(fm.group(1)) or {}).get("citations") or []:
                if isinstance(c, dict) and c.get("url"):
                    urls.add(str(c["url"]))
        if errs:
            bad += 1
            print(f"\n✗ {rel}")
            for e in errs:
                print(f"    {e}")
        else:
            print(f"✓ {rel}")
    print(f"\n{len(files) - bad}/{len(files)} artifacts clean · {len(urls)} distinct citations")
    return bad


if __name__ == "__main__":
    sys.exit(main())
