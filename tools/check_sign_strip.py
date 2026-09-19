#!/usr/bin/env python3
"""check_sign_strip.py — the DA-23 guard.

DA-23 is a defect in the **platform's** extraction layer: a filed negative is served as a
positive of identical magnitude. It is live — at RKLB Q2 2026 the served
`OperatingIncomeLoss` is `+57,514,000` against a filed `(57,514)` thousand, where the
served components give `84,576,000 − 142,090,000 = −57,514,000`. Any screen on the raw
field inverts: the worst loss-makers rank at the top.

Nothing upstream fixes this from here, and the kit does not address it. So this is a
**workspace-side guard**, and it follows the register's own remedy rather than inventing
one.

WHAT IT DOES — and it is deliberately narrow
--------------------------------------------
It enforces the **DA-29 circularity test on the strip's own arithmetic**. An artifact that
asserts the strip fingerprint — `diff = 2 × <term>`, or `2 × (<a> + <b>)` — is asserting a
number. **If that number appears nowhere else in the artifact, the assertion is a
back-solve: it closes exactly and tests nothing.** This tool locates the terms.

    for every `2 × N` claim: is `2N` present anywhere in the same artifact?

That is checkable, it can fail, and it maps exactly onto the register's rule.

WHAT IT REFUSES TO DO
---------------------
**It never corrects a sign, and it never re-grades an artifact.** A tool that silently
flips a value is a back-solve wearing a checker's clothes — the DA-29 failure living inside
the remedy for DA-23. This tool reports and exits non-zero. A human decides.

WHAT IT DOES NOT DO — stated so a clean exit is not over-read
-------------------------------------------------------------
- It does **not** detect an uncorrected strip in an artifact that does not assert the
  fingerprint. That requires reading the artifact against the filing, and no regex does it.
- It does **not** read XBRL facts. It reads markdown.
- **A zero exit means "every asserted fingerprint is grounded", NOT "no artifact is
  stripped."** The distinction is the whole point of this session's finding: a check that
  closes cleanly while testing nothing is the defect, not the remedy.

Usage
-----
  python3 tools/check_sign_strip.py theses/002-evidence-validation
  python3 tools/check_sign_strip.py --selftest      # proves the rule can fail
Exit code = number of ungrounded assertions (0 = every asserted term was located).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)

# `2 × 57,514`  |  `2 × (51,791 + 46,951)`  |  `2 x 1,510`
# The `(?<![\d.])` guard is load-bearing: without it, `0.0072 × 10` matches as `2 × 10`,
# and the tool fires on every decimal that happens to end in 2. A detector that fires on
# everything is the failure mode this tool exists to catch, not a conservative default.
CLAIM_RE = re.compile(r"(?<![\d.])2\s*[×xX*]\s*(\([^)]*\)|[\d][\d,_.]*)")
# A `2 ×` assertion is a STRIP fingerprint only in strip context. `2 × 12,536,053 −
# 12,574,261` is a derivation, not a fingerprint, and must not be graded as one.
STRIP_CONTEXT = re.compile(
    r"strip|sign|diff|invert|mirror|doubl|residual|served|loss", re.I)

# The strip signature itself: a served magnitude that equals a filed magnitude's absolute
# value with the sign inverted. Recorded, not acted on.
STRIP_HINT = re.compile(
    r"\b(stripped|sign.strip|STRIPPED|served\s+`?\+|served\s+\+|= exactly 2)\b", re.I)


def _numbers_in(text: str) -> set[str]:
    """Every numeric token, normalised to bare digits, for presence testing.

    A claim of `115,028` may be written as `115,028`, `115028000`, or `115.028` depending
    on the artifact's units. We accept any of those as grounding the term.
    """
    out = set()
    for tok in re.findall(r"[\d][\d,_.]*", text):
        bare = tok.replace(",", "").replace("_", "")
        out.add(bare)
        out.add(bare.lstrip("0"))
        if "." in bare:
            out.add(bare.replace(".", ""))
        # thousands→millions and thousands→billions variants
        if bare.isdigit():
            out.add(bare + "000")
            out.add(bare + "000000")
    return {x for x in out if x}


def _claim_value(expr: str) -> float | None:
    """Evaluate a claim's operand: a literal, or a sum of literals."""
    expr = expr.strip()
    if expr.startswith("(") and expr.endswith(")"):
        parts = re.split(r"[+\-]", expr[1:-1])
        total = 0.0
        for p in parts:
            p = p.strip().replace(",", "").replace("_", "")
            if not p:
                continue
            try:
                total += float(p)
            except ValueError:
                return None
        return abs(total)
    try:
        return abs(float(expr.replace(",", "").replace("_", "")))
    except ValueError:
        return None


def check(path: Path) -> list[str]:
    """Return ungrounded fingerprint assertions in one artifact."""
    text = path.read_text(encoding="utf-8", errors="replace")
    m = FM.match(text)
    body = text[m.end():] if m else text
    present = _numbers_in(text)
    lines = body.splitlines()
    bad: list[str] = []
    for i, line in enumerate(lines):
        ctx = " ".join(lines[max(0, i - 1): i + 2])   # the line and its neighbours
        if not STRIP_CONTEXT.search(ctx):
            continue                                   # a derivation, not a fingerprint
        for cm in CLAIM_RE.finditer(line):
            val = _claim_value(cm.group(1))
            if val is None:
                continue
            doubled = val * 2
            # Preserve the decimal: `2 × 6.8` grounds on `13.6`, and a `:,.0f` rendering
            # would ask for `14` and report a false positive on a correct artifact.
            plain = f"{doubled:.10f}".rstrip("0").rstrip(".")
            cands = {plain, plain.replace(".", "")}
            if doubled == int(doubled):
                n = str(int(doubled))
                cands |= {n, n + "000", n + "000000"}
            if not ({c for c in cands if c} & present):
                bad.append(f"`{cm.group(0).strip()}` → {plain} appears nowhere in the "
                           f"artifact — the assertion is a back-solve (DA-29)")
    return bad


def _selftest() -> int:
    """Prove the rule can fail. A guard that cannot fail is the defect it exists to catch."""
    import tempfile
    cases = [
        # grounded: the fingerprint's own product is present
        ("grounded.md",   "served is sign-stripped: diff = 2 × 57,514\n\nThe difference "
                          "is 115,028.\n",                                          0),
        # ungrounded: same assertion, product absent -> a back-solve
        ("ungrounded.md", "served is sign-stripped: diff = 2 × 57,514\n\nNo other "
                          "number here.\n",                                         1),
        ("grounded_sum.md", "residual = 2 × (51,791 + 46,951); the gap is 197,484\n", 0),
        ("ungrounded_sum.md", "residual = 2 × (51,791 + 46,951); nothing else\n",     1),
        # decimal grounding: 2 × 6.8 must ground on 13.6, not on a rounded 14
        ("grounded_dec.md", "served sign-stripped: 13.6 = 2 × 6.8 ✓\n",             0),
        # NOT a fingerprint: a decimal tail `0.0072 × 10` must not match `2 × 10`
        ("decimal_tail.md", "note: 0.0072 × 10 = 7 bps, sign-neutral\n",             0),
        # NOT a fingerprint: a derivation with no strip context
        ("derivation.md",   "12,497,845 — derived: 2 × 12,536,053 − 12,574,261\n",   0),
    ]
    ok = True
    with tempfile.TemporaryDirectory() as td:
        for name, body, want in cases:
            p = Path(td)/name
            p.write_text(f"---\nthesis_id: x\n---\n{body}")
            got = len(check(p))
            flag = "ok " if got == want else "FAIL"
            if got != want:
                ok = False
            print(f"  {flag} {name:20} expected {want} ungrounded, got {got}")
    print(f"\nselftest {'PASSED' if ok else 'FAILED'}")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("path", nargs="?", default=".")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return _selftest()

    d = Path(a.path)
    files = sorted((d/"artifacts").rglob("*.md")) if (d/"artifacts").is_dir() else []
    if (d/"_cross").is_dir():
        files += sorted((d/"_cross").glob("*.md"))
    if not files:
        print("no artifacts found")
        return 0
    bad = 0
    for f in files:
        errs = check(f)
        if errs:
            bad += len(errs)
            print(f"\n✗ {f.relative_to(d)}")
            for e in errs:
                print(f"    {e}")
    print(f"\n{len(files) - len({f for f in files if check(f)})}/{len(files)} artifacts have "
          f"every asserted fingerprint grounded · {bad} ungrounded")
    print("NOTE: this checks ASSERTED arithmetic only. A zero here does not mean no "
          "artifact is stripped — it means no artifact asserts a fingerprint it cannot ground.")
    return bad


if __name__ == "__main__":
    sys.exit(main())
