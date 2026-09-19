# Report Outline — Thesis 002, Evidence Validation & Model Hardening

> **Q94 gate.** The outline is written and **finalised before any page is authored** —
> without it the structure of the argument is never chosen, only emerges. Sections below
> are the gate's four required elements, in its own vocabulary.

## Key arguments

Each argument is a claim pointing at an investment conclusion — what this means for
expectations or returns, not a restatement of what the data says.

**A1 — The thesis falsified its own MVP pillar, and that is the report's news.**
PIL-5 — *"at least half of 001's headline figures convert to `DEMONSTRATED`"* — is
**partially falsified**: four of nine readings fire and three more land exactly on the
threshold with zero margin. **This argues for** reading every downstream thesis's inputs as
conditional, because the programme's own falsification test is not a formality.

**A2 — `DEMONSTRATED` is not a sufficient grade, because a grade does not carry a basis.**
SPCX `operating_margin` reproduces exactly from filed cells and is off by **46.47 pp**
against what its label names — an AI-segment loss over consolidated revenue. **Therefore**
003–011 must carry *basis* alongside *grade*, or inherit figures that reproduce and mean
something else. This is the report's single most consequential finding.

**A3 — The evidentiary base is thinner than 001's precision implied, but the arithmetic held.**
Per-ticker sums reproduced at IRDM, MRCY, UTHR and SPCX. **This implies** the correction
target is *labelling and clearance*, not the numbers — a narrower and more fixable defect
than "the model is wrong".

**A4 — Sign stripping is a default, not an exception: 14 of 17 issuers.**
DA-23 inverts any screen on raw `operating_income`; at RKLB the served value is `+57,514`
thousand against a filed `(57,514)`. **This points to** a required remediation — recompute
from components — and to the fact that no validator in the workspace currently reads a
sign.

**A5 — Corrections do not propagate: 3 of 32.**
`upstream_stale` is mandatory in all 41 artifacts, correct in all 41, **consumed by none**.
**This warrants** a named resumption queue, because a recorded-but-unpropagated correction
is indistinguishable in effect from one never made.

## Evidence

| Argument | Primary source | Grade |
|---|---|---|
| A1 | `_cross/validation-ledger.md` — the nine-reading ladder | `DERIVED` |
| A2 | `artifacts/SPCX/…_ratio-analysis_methodology.md` (§ operating_margin, 4 bases) | `DEMONSTRATED` |
| A3 | `thesis.md` corrections; per-ticker reproduction in IRDM/MRCY/UTHR/SPCX artifacts | `DEMONSTRATED` |
| A4 | `artifacts/RKLB/…_ratio-analysis_methodology.md`; constitution §Data-Integrity Register | `DEMONSTRATED` |
| A5 | `_cross/validation-ledger.md` corrections census; `theses/002-evidence-validation/skill_pins.jsonl` | `DERIVED` |

Supporting: the falsifier reachability census (PIL-7 metric **0**, 11 blocks classified,
seven not-testable kinds) and the instrument-defect catalogue (`validate_calculation`'s
three failure modes; `computed` is not a derivation; extension tags are silently missed).

## Page plan

| Page(s) | Section | Argument |
|---|---|---|
| 1 | Cover — **template-owned, not authored** | — |
| 2 | The answer up front | A1 |
| 3–4 | The nine-reading ladder | A1 |
| 5 | Why it matters: the 46.47 pp example | A2 |
| 6–7 | What survived | A3 |
| 8–9 | The defect register (DA-23…DA-30) | A4 |
| 10–11 | Corrections do not propagate | A5 |
| 12–13 | Falsifier reachability + instrument defects | supporting |
| 14–15 | What this means for 003–011 | A1–A5 |
| 16 | Limitations — the three irreducible gaps | supporting |
| 17 | Disclaimer — **template-owned, not authored** | — |

**Budget:** ~15 authored pages, ≤40 prose lines and ≤18 table rows per page.

## Story line

002 is an **evidence audit**, not a sector thesis, so it must not borrow 001's structure.
The narrative is a **narrowing**: 001 asserted a sector-level model; 002 asked which parts
of it can be reproduced from primary sources, and found that **the numbers survive but the
labels do not**.

The report opens on the falsification — not buried at the end, because it *is* the news —
establishes that the failure is one of **basis rather than arithmetic**, catalogues the
platform defects that make the distinction hard to see, and closes on the one instruction a
downstream reader needs: **carry the basis, not just the grade.**

The tone is a validation report clearing a model, not a takedown. 001's arithmetic largely
held; what 002 removes is the licence to quote it at four significant figures.
