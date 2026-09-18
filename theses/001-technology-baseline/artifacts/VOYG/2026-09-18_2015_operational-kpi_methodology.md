---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: VOYG
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T20:15:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income FAILS the gross-profit bound in 3 consecutive quarters; recorded as CANDIDATE with a NEW sub-mechanism"
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 row carries the ANNUAL revenue"
  - da_id: "DA-16"
    chosen_reading: "Starlab milestone claims graded CLAIMED where not filed"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# VOYG — Operating Baseline

Source: Form 10-Q, accession `0001628280-26-052292` (Q2 2026, quarter ended 2026-06-30).

---

## 1. A NEW DETECTOR: operating income cannot exceed gross profit

```
Q2 2026 gross profit       $4.457M
Q2 2026 operating income  $51.408M
                          ─────────
operating income EXCEEDS gross profit by $46.951M
```

**This is arithmetically impossible for a normal income statement.** Operating income is
gross profit *minus* operating expenses. Voyager discloses R&D of $7.336M, so operating
expenses are strictly positive. There is no set of operating expenses — including zero —
under which operating income exceeds gross profit.

**The gross-profit bound is a detector the sign rule does not cover.** DA-23's rule
("a negative operating income is stripped of its sign") predicts a *sign inversion at equal
magnitude*. Here the level itself is unreconcilable, at any sign.

**Look at how far outside the bound it is:** GP $4.457M vs OI $51.408M. If the true figure
were the sign-flipped loss −$51.408M, operating expenses would need to be $55.865M on
revenue of $52.746M — i.e. **SG&A alone at 92% of revenue** after $7.3M of R&D. That is
not a credible reading either.

**Neither mechanism reconciles.** Voyager is recorded as a **DA-23 CANDIDATE with a new
sub-mechanism**, and the honest statement is that **the operating income line is
unusable** — not that it is sign-flipped.

## 2. The pattern is persistent across three consecutive quarters

| Quarter | Revenue | Reported operating income | OI / revenue | OI − GP |
|---|---:|---:|---:|---:|
| Q2 2025 | $45.674M | $24.137M | **52.8%** | n/a (no GP line) |
| Q3 2025 | $39.587M | $24.043M | **60.7%** | n/a |
| Q1 2026 | $35.246M | $44.647M | **126.7%** | n/a |
| **Q2 2026** | **$52.746M** | **$51.408M** | **97.5%** | **+$46.951M** |

**An operating margin above 100% (Q1 2026) is not a margin at all.** A persistent,
multi-quarter pattern rules out the benign explanation that a single one-off gain sat
between gross profit and operating income in one period — **a one-off would not recur
four times.**

**This is a more serious defect class than the six sign-strip confirmations**, because a
sign strip is detectable by magnitude-preserving reconciliation while a level error of
this size is detectable only by the gross-profit bound. **Any thesis using VOYG's operating
line is using a broken number.**

## 3. What is still usable

**Net income is close to operating income and reconciles to EPS:**

```
EPS (diluted) $0.79 x 58.522M weighted diluted shares = $46.233M
reported net income                                   = $46.490M
gap: 0.6%
```

**So the EPS identity holds even though the operating line does not.** This is the same
divergence seen at RKLB and FLY, where EPS × shares passes on both sides of a flip because
both numbers share the same error. **It confirms the earlier finding**: EPS reconciliation
is not a reliable detector; **component identity is.**

**Revenue appears sound**: Q1 2026 $35.246M, Q2 2026 $52.746M (+49.6% sequentially), against
FY2025 annual of $166.419M. Voyager's balance sheet is genuinely strong — cash $373.436M,
current assets $581.300M, total assets $1,009.273M — and Q2 2026 operating cash flow was
**+$84.027M** with **$86.652M of capex**. That combination (positive operating cash flow
plus heavy capex) is the profile of a company building toward Starlab, and it is the most
credible thing in the filing.

## 4. DA-26 — VOYG's Q4 row is the annual, and the check is arithmetic

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $52.746M | a genuine quarter |
| **Q4 2025** | **$166.419M** | **VOYG's FY2025 ANNUAL revenue** |

**Thirteenth issuer confirmed.** FY2025 = Q2 $45.674M + Q3 $39.587M + Q1 + Q4, against a
reported annual of $166.419M — leaving $81.158M across Q1 and Q4, consistent with the
observed quarterly range. **The annual reading is internally consistent; the quarterly
reading (a 4.2× sequential jump from Q3's $39.587M) is not.**

---

## Carry-forwards

1. **NEW DETECTOR — the gross-profit bound.** Operating income exceeding gross profit is
   arithmetically impossible and confirms a corrupted line **at any sign**. This detector
   is strictly stronger than sign-reconciliation and would have caught instances the sign
   rule misses.
2. **VOYG is a DA-23 CANDIDATE with a NEW sub-mechanism** — not sign inversion but an
   unreconcilable *level*, persistent across three consecutive quarters. **The operating
   income line is unusable.** Register as a distinct amendment item from the six
   sign-strip confirmations.
3. **EPS reconciliation is confirmed unreliable** (again) — VOYG's EPS identity holds at a
   0.6% gap while the operating line fails by $46.951M.
4. **DA-26 at 13 of 13 issuers.**
