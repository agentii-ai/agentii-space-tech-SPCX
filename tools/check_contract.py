#!/usr/bin/env python3
"""check_contract.py — the executable form of the rules `check_citations.py` does not cover.

`check_citations.py` enforces the four CITATION rules. The artifact contract
(`contracts/artifact-frontmatter.yaml`) declares several more at level `fail`, and until
this file existed they were enforced by nothing but discipline. Phase 7's ledger needs
them mechanical, because its job is a census across every artifact.

Rules implemented
-----------------
  pins_present              all five pins, and constitution_pin in the ACCEPTED set
  skill_pin_wellformed      12 lowercase hex, or the declared sentinel `none`/`n/a`.
                            ADDED 2026-09-19: the value was previously unchecked, so
                            `registry-1.0.0` — a registry version, not a skill hash —
                            passed every check in the repo while pinning nothing.
  evidence_grade_present    required; enum-checked. Absence is a fail, never a default
  da_id_registered          definitions_used[].da_id within DA-01..DA-22 or DA-23..DA-30
  unresolvable_class_required  unresolvable:true requires a class
  deal_security_tagging     IRDM / GSAT / RKLB must set deal_security_basis (P11)
  basis_named               DA-30: a multi-basis concept must name its basis
  reconciliation_terms_located  DA-29: a reconciliation must name every term

Why the last two are only HEURISTIC, and are reported as `warn` not `fail`
----------------------------------------------------------------------------
DA-29 and DA-30 are semantic. A regex cannot decide whether a reconciliation's terms are
all filed, nor whether the basis a figure needs has been named. **A blanket regex would
produce exactly the failure mode this thesis spent Phase 3 documenting: a check that
closes cleanly while testing nothing.** So these two report *candidates for a human read*
and never gate the exit code. The mechanical rules gate.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)

# 1.4.0 -> 1.5.0 at 002 Phase 3. Both are legitimately live in thesis 002: it was
# specified at 1.4.0 and the register gained DA-29/DA-30 at 1.5.0. An artifact is valid
# at the pin it RECORDS. See contract rule `pins_match_thesis`.
#
# ⚠️ This was a GLOBAL constant until 2026-09-19, and a global constant cannot be right for
# a workspace holding theses specified at different versions — 001 is pinned 1.2.0, 011 at
# 1.4.0, 002/003 at 1.5.0. Hardcoding {1.4.0, 1.5.0} reported **all 49 of thesis 001's
# artifacts as red** for a reason that is not a defect. The set is now derived per-thesis
# from that thesis's own declarations; this fallback applies only when none are found.
ACCEPTED_PINS_FALLBACK = {"1.4.0", "1.5.0"}


def accepted_pins(d: Path) -> set[str]:
    """The constitution pins THIS thesis legitimately passed through, from its own files.

    Two sources, both authored by the thesis rather than by this tool:
      1. `thesis.md` frontmatter — `constitution_pin` and, where a bump occurred,
         `constitution_pin_at_specification`. Thesis 002 carries both because it spans the
         1.4.0 -> 1.5.0 amendment.
      2. `contracts/artifact-frontmatter.yaml` — a rule's `accepted_constitution_pins`
         list, where the thesis declares the set explicitly.

    Reading it rather than hardcoding it is the same discipline the contract's own comment
    states: *"An artifact is valid at the pin it RECORDS."* A tool that disagrees with the
    thesis about which pins are legitimate is not checking the thesis — it is checking
    itself.
    """
    pins: set[str] = set()
    t = d / "thesis.md"
    if t.is_file():
        m = FM.match(t.read_text(encoding="utf-8", errors="replace"))
        if m:
            try:
                fm = yaml.safe_load(m.group(1)) or {}
                for k in ("constitution_pin", "constitution_pin_at_specification"):
                    if isinstance(fm, dict) and fm.get(k):
                        pins.add(str(fm[k]))
            except yaml.YAMLError:
                pass
    c = d / "contracts" / "artifact-frontmatter.yaml"
    if c.is_file():
        try:
            data = yaml.safe_load(c.read_text(encoding="utf-8")) or {}
            for r in (data.get("validation_rules") or []):
                for p in ((r or {}).get("accepted_constitution_pins") or []):
                    pins.add(str(p))
            # The FIELD-DECLARED pin. Thesis 001 states its accepted version here —
            # `constitution_pin: {type: str, required: true, const: "1.2.0"}` — and nowhere
            # else. Reading only the rules list missed it and fell back to the global
            # constant, which reintroduced the exact false-red this function removes.
            fields = (data.get("fields") or {})
            if isinstance(fields, dict):
                fld = fields.get("constitution_pin")
                if isinstance(fld, dict) and fld.get("const"):
                    pins.add(str(fld["const"]))
        except yaml.YAMLError:
            pass
    return pins or ACCEPTED_PINS_FALLBACK
PINS = ("constitution_pin", "assumption_pin", "skill_pin", "as_of", "corpus_version")
GRADES = {"DEMONSTRATED", "CLAIMED", "MODELED", "DERIVED"}
UCLASSES = {"UNRESOLVABLE-FROM-PUBLIC-SOURCES", "UNRESOLVABLE-FROM-PLATFORM"}
DSB = {"standalone_pre_merger", "post_close", "not_applicable"}
# DA-01..DA-22 are definitional ambiguities defined in 001 spec §1c and inherited by
# reference; DA-23..DA-30 are defects/platform-collapses defined in the constitution.
REGISTERED = {f"DA-{n:02d}" for n in range(1, 31)}
DEAL_SECURITIES = {"IRDM", "GSAT", "RKLB"}

# skill_pin canonical form. Until 2026-09-19 the value was never checked — `check_citations`
# and this file both tested PRESENCE only — so four incompatible VALUES validated identically:
# 12-hex hashes, `"n/a"`, `"registry-1.0.0"` (a whole-registry version, not a per-skill hash),
# and one unquoted scalar. `registry-1.0.0` was the worst: it reads as a pin, passes every
# check, and pins nothing. `none` is the declared sentinel for a synthesis artifact that has
# no single skill; `n/a` is retained as a tolerated legacy synonym.
SKILL_PIN_RE = re.compile(r"(?:[0-9a-f]{12}|none|n/a)\Z")
SKILL_PIN_SENTINELS = ("none", "n/a")

# Concepts the register has established are reported on more than one basis somewhere in
# the universe. Quoting one of these without naming a basis is a DA-30 candidate.
MULTI_BASIS = re.compile(
    r"\b(operating income|operating_income|OperatingIncomeLoss|gross margin|gross profit|"
    r"diluted EPS|net income|EBITDA)\b", re.I)
BASIS_WORD = re.compile(
    r"\b(basis|as[- ]filed|equity[- ]inclusive|equity[- ]exclusive|segment|consolidated|"
    r"Class [A-C]|attributable to|before|excluding|including|standalone_pre_merger|"
    r"post_close|recast|as[- ]reported|pro[- ]forma)\b", re.I)
# A reconciliation is asserted when these appear near a number.
RECON = re.compile(r"\breconcil\w+|\bcloses?\b|\bfoot(s|ed)?\b|\btie[sd]?\b|\bbridge\b", re.I)


def check(path: Path, accepted: set[str] | None = None) -> tuple[list[str], list[str]]:
    """Return (errors, warnings). Errors gate; warnings do not.

    `accepted` is the pin set for the thesis this artifact belongs to — pass the result of
    `accepted_pins(thesis_dir)`. Falling back to the global constant silently reinstates the
    false-red this parameter exists to remove.
    """
    accepted = accepted or ACCEPTED_PINS_FALLBACK
    errs: list[str] = []
    warns: list[str] = []
    text = path.read_text(encoding="utf-8")
    m = FM.match(text)
    if not m:
        return ["no frontmatter block"], warns
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return [f"frontmatter does not parse: {str(e)[:80]}"], warns
    if not isinstance(fm, dict):
        return ["frontmatter is not a mapping"], warns
    body = text[m.end():]

    # pins_present
    for p in PINS:
        if not fm.get(p):
            errs.append(f"missing pin `{p}`")
    cp = str(fm.get("constitution_pin", ""))
    if cp and cp not in accepted:
        errs.append(f"constitution_pin={cp!r} is not in this thesis's accepted set "
                    f"{sorted(accepted)}")

    # skill_pin_wellformed — the value, not just its presence.
    sp = fm.get("skill_pin")
    if sp is not None and not SKILL_PIN_RE.match(str(sp)):
        errs.append(f"skill_pin={str(sp)!r} is not canonical — expected 12 lowercase "
                    f"hex chars, or one of {SKILL_PIN_SENTINELS}")

    # evidence_grade_present
    g = fm.get("evidence_grade")
    if not g:
        errs.append("evidence_grade absent — absence is a fail, not a default")
    elif str(g) not in GRADES:
        errs.append(f"evidence_grade={g!r} not in {sorted(GRADES)}")

    # da_id_registered
    dus = fm.get("definitions_used") or []
    if not dus:
        errs.append("definitions_used is empty (min_items: 1)")
    for i, d in enumerate(dus):
        if not isinstance(d, dict):
            errs.append(f"definitions_used[{i}] is not a mapping")
            continue
        da = str(d.get("da_id", ""))
        if not re.fullmatch(r"DA-\d{2}", da):
            errs.append(f"definitions_used[{i}].da_id malformed: {da!r}")
        elif da not in REGISTERED:
            errs.append(f"definitions_used[{i}].da_id {da} is unregistered")
        if not d.get("chosen_reading"):
            errs.append(f"definitions_used[{i}] has no chosen_reading")

    # unresolvable_class_required
    if fm.get("unresolvable"):
        uc = fm.get("unresolvable_class")
        if not uc:
            errs.append("unresolvable: true but no unresolvable_class "
                        "(the two dispositions have different remedies)")
        elif str(uc) not in UCLASSES:
            errs.append(f"unresolvable_class={uc!r} not in {sorted(UCLASSES)}")

    # deal_security_tagging
    tk = str(fm.get("ticker", ""))
    if tk in DEAL_SECURITIES and not fm.get("deal_security_basis"):
        errs.append(f"{tk} is a deal security — deal_security_basis is required (P11)")
    dsb = fm.get("deal_security_basis")
    if dsb and str(dsb) not in DSB:
        errs.append(f"deal_security_basis={dsb!r} not in {sorted(DSB)}")

    # basis_named (DA-30) — HEURISTIC, warn only
    hits = {h.group(0).lower() for h in MULTI_BASIS.finditer(body)}
    if hits and not BASIS_WORD.search(body):
        warns.append(f"DA-30 candidate: quotes {sorted(hits)} but names no basis")

    # reconciliation_terms_located (DA-29) — HEURISTIC, warn only
    if RECON.search(body) and not re.search(r"filed|per the|as reported|per sec", body, re.I):
        warns.append("DA-29 candidate: asserts a reconciliation without naming a source"

                     " term")
    return errs, warns


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    d = Path(args[0]) if args else Path(".")
    files = sorted((d / "artifacts").rglob("*.md")) if (d / "artifacts").is_dir() else []
    if (d / "_cross").is_dir():
        files += sorted((d / "_cross").glob("*.md"))
    if not files:
        print("no artifacts yet")
        return 0
    bad = nwarn = 0
    acc = accepted_pins(d)
    print(f"accepted constitution pins for this thesis: {sorted(acc)}")
    for f in files:
        rel = f.relative_to(d)
        errs, warns = check(f, acc)
        if warns:
            nwarn += 1
            print(f"\n⚠ {rel}")
            for w in warns:
                print(f"    {w}")
        if errs:
            bad += 1
            print(f"\n✗ {rel}")
            for e in errs:
                print(f"    {e}")
    print(f"\n{len(files) - bad}/{len(files)} artifacts contract-clean · "
          f"{nwarn} with DA-29/DA-30 candidates for read")
    return bad


if __name__ == "__main__":
    sys.exit(main())
