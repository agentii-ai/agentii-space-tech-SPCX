---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: HWM
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T18:20:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "HWM's own segment definitions"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified; HWM CLEAN"
  - da_id: "DA-26"
    chosen_reading: "the 'Q1 2026' metrics row is the FY2025 ANNUAL total, not a quarter"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# HWM — Supply-Chain Position (Castings & Fasteners)

Source: Form 10-Q, accession `0001104659-26-091610` (Q2 2026, quarter ended 2026-06-30).

---

## 1. HWM demonstrates the aerospace-component margin model — and it is not the space duopoly's model

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$2,547M** | $2,053M | +24.1% |
| Operating income | **$711M** | $521M | +36.5% |
| **Operating margin** | **27.9%** | 25.4% | **+2.5 pts** |
| Net income | $534M | $407M | +31.2% |
| R&D | $8M | $9M | — |
| **R&D / revenue** | **0.3%** | 0.4% | — |

**A 27.9% operating margin, expanding, at 0.3% R&D intensity.** HWM is the purest
example in the universe of the **manufacturing-franchise** profile: engine and structural
castings, fasteners, and engineered components sold into a certified supply chain where
requalification is expensive. No development spend, high and rising rent.

**The comparison that matters for PIL-3:**

| Company | Operating margin | R&D/revenue | Model |
|---|---|---|---|
| **HWM** | **27.9%** | **0.3%** | certified-component franchise |
| TDG | 44.8% | — | sole-source aftermarket |
| YSS | −44.6% (loss) | 6.2% | satellite manufacturing |
| BA | 0.6% | ~3.9% | OEM prime |

**Certified aerospace components carry 28–45% operating margins.** That is the benchmark
the space-grade duopolies are *not* achieving — and, as the BA and LHX artifacts
established, cannot be measured because they are not disclosed as segments.

**The honest inference**: the space-grade solar-cell and engine duopolies are
presumably also franchise-like businesses (same certification dynamic, same two-supplier
structure). If so, **their margins are likely high and simply invisible** — which is a
different conclusion from "the bottleneck is not binding." The thesis cannot currently
distinguish between the two, and should say so rather than picking the reading that
suits PIL-3.

## 2. HWM is clean on DA-23

Operating income $711M at a 27.9% margin is plausible for Howmet; EPS × shares
($1.33 × 400M = $532M) reconciles to $534M net income to 0.4%. **Profitable issuer,
unaffected.**

## 3. ⚠️ DA-26 — a third defect, and HWM exhibits it twice

The metrics block returns a **"Q1 2026" revenue of $8,252M** — but HWM's Q1 2025 was
$1,942M and Q2 2026 is $2,547M. **$8,252M is Howmet's full-year 2025 revenue**, and it
appears **twice**: once labelled `Q4 2025` and again labelled `Q1 2026`.

**DA-26 is: annual figures are mislabelled as quarterly in the metrics block.** Verified
across **7 of 7 issuers checked** (HWM, TDG, BA, GOOG, MSFT, NVDA, SATS) — every one
shows its fiscal-year total in a quarter row.

**Consequence**: any quarterly trend built from `get_company_financials` metrics is
contaminated. A "Q4" equal to the annual total inflates that quarter ~4×, and the
adjacent quarters must sum to a residual that is too small.

**This is the third distinct defect in the same extracted block**, alongside DA-23 (sign
stripping) and DA-24 (asset-sale contamination) — and it is **independent of both**: HWM
is clean on DA-23 and exhibits DA-26.

---

## Carry-forwards

1. **HWM is the manufacturing-franchise benchmark: 27.9% operating margin at 0.3% R&D.**
2. **Certified components carry 28–45% margins** — so the space duopolies' invisible
   margins are *probably* high. The thesis must say it cannot distinguish "high but
   undisclosed" from "not binding."
3. **DA-26 registered** — third defect in the metrics block, 7 of 7 issuers, independent
   of DA-23 and DA-24.
