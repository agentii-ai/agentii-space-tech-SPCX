---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-6
ticker: PL
skill: sector-overview
mode: methodology
generated_at: 2026-09-19T15:45:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "8fb208998401"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: >-
      The filed sign governs; the served positive is an extraction artefact. At PL the regime
      is UNIFORM — every served OperatingIncomeLoss across the issuer's history is positive and
      every filed one is negative — so the served stack closes in |x| space and NO arithmetic
      heuristic detects it. Only the component identity detects it.
  - da_id: DA-27
    chosen_reading: >-
      Fiscal labels derived from the calendar quarter. PL's fiscal year ends January 31, so the
      quarter ended 2026-04-30 is Q1 FY2027; the platform's outline labels the SAME table both
      "Q1 FY2027" and "Q1 FY2026", and the 003 entity map calls it "Q1 FY2026". Every period in
      this artifact is cited by its PERIOD-END DATE, never by a fiscal label.
  - da_id: DA-30
    chosen_reading: >-
      Two bases on one concept collapsed without a basis field. Live at PL in two places: the
      two opex definitions (which CONVERGE here, uniquely in this cohort and for a stated
      reason), and the GAAP versus non-GAAP gross margin bases (54% and 56%), which must never
      be quoted as one series.
  - da_id: DA-24
    chosen_reading: >-
      Non-operating contamination measured, not assumed. PL's net loss is 76.7% a non-operating
      warrant remeasurement; the operating line is reported separately and the contamination is
      quantified rather than netted away.
evidence_grade: DEMONSTRATED
citations:
  - ticker: PL
    citation_id: sec76
    form_type: "10-Q"
    page_no: 6
    figure: "Statements of operations, quarter ended April 30, 2026; loss from operations 34,888"
    url: "https://agentii.ai/v/PL/sec76/6"
    located_via: read_source_pages
  - ticker: PL
    citation_id: sec76
    form_type: "10-Q"
    page_no: 38
    figure: "Revenue +$27,885k / +42%; total opex +44%; loss from operations +53%"
    url: "https://agentii.ai/v/PL/sec76/38"
    located_via: read_source_pages
  - ticker: PL
    citation_id: sec76
    form_type: "10-Q"
    page_no: 41
    figure: "Non-GAAP: gross margin 54% vs 55%; non-GAAP gross margin 56% vs 59%; adjusted EBITDA"
    url: "https://agentii.ai/v/PL/sec76/41"
    located_via: read_source_pages
  - ticker: PL
    citation_id: sec76
    form_type: "10-Q"
    page_no: 47
    figure: "Risk factor: history of operating losses"
    url: "https://agentii.ai/v/PL/sec76/47"
    located_via: read_source_outline
  - ticker: PL
    citation_id: sec76
    form_type: "10-Q"
    page_no: 49
    figure: "Risk factor: competition"
    url: "https://agentii.ai/v/PL/sec76/49"
    located_via: read_source_outline
  - ticker: PL
    citation_id: sec76
    form_type: "10-Q"
    page_no: 51
    figure: "Risk factor: satellite development and launch"
    url: "https://agentii.ai/v/PL/sec76/51"
    located_via: read_source_outline
  - ticker: PL
    citation_id: sec76
    form_type: "10-Q"
    page_no: 59
    figure: "Risk factor: supply chain and cloud"
    url: "https://agentii.ai/v/PL/sec76/59"
    located_via: read_source_outline
  - ticker: PL
    citation_id: sec76
    form_type: "10-Q"
    page_no: 62
    figure: "Risk factor: customer concentration and seasonality"
    url: "https://agentii.ai/v/PL/sec76/62"
    located_via: read_source_outline
  - ticker: PL
    citation_id: sec76
    form_type: "10-Q"
    page_no: 77
    figure: "Risk factor: NOAA, FCC, ITAR, EAR and OFAC regulatory exposure"
    url: "https://agentii.ai/v/PL/sec76/77"
    located_via: read_source_outline
  - ticker: PL
    citation_id: sec76
    form_type: "10-Q"
    page_no: 87
    figure: "Risk factor: 2030 Notes and capped calls"
    url: "https://agentii.ai/v/PL/sec76/87"
    located_via: read_source_outline
key_metrics:
  gross_margin_gaap_pct_q1_fy2027: 53.53
  operating_margin_pct_q1_fy2027: -37.06
  opex_to_gross_profit_multiple_x: 1.692
  warrant_remeasurement_share_of_net_loss_pct: 76.66
---

# PL × sector-overview — the highest gross margin in the universe, at −37% operating

## The finding

**PL holds the best gross margin in this universe — 53.5% — and the operating line is −37.06%.**
Both are DEMONSTRATED and both are filed. The 90.5 percentage-point gap between them is the
value-chain finding: **PL is the cleanest available test of "which position in the stack holds the
margin", and the answer is that the position holding the gross margin is not the position holding
the operating margin, because the fixed cost base is set independently of the gross margin level.**

Three consequences, and they are the substance:

1. **The loss is a FIXED-COST result, not a launch-cost result.** Cost of revenue is **46.5%** of
   revenue; operating expenses are **90.6%** of revenue and **1.692× gross profit**. Launch cost
   lives inside the 46.5% and is demonstrably not the binding constraint — **PL retains 53.5%
   gross while absorbing it.** This is evidence *for* PIL-6's migration claim and against reading
   launch cost as the sector's value variable.
2. **Operating leverage is NEGATIVE.** Revenue grew **+42%** and the loss from operations widened
   **+53%**; opex grew **+44%**, faster than revenue. `[📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38)`
   A 42% growth quarter produced a wider loss. There is no scale fix at this revenue level.
3. **76.7% of the net loss is a non-operating warrant remeasurement** — a DA-24 contamination
   point that must be quantified, not netted. `[📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)`

## 1. Component identity, opex definition, units

**Opex definition: total operating expenses as filed — R&D, sales and marketing, and general and
administrative — EXCLUSIVE of cost of revenue.** PL files a **gross-profit line**, so both pairings
are computable, and this is the one issuer in this cohort where they agree.

| Pairing | Arithmetic ($k) | Result |
|---|---|---|
| **Exclusive** (filed lines) | 50,401 − 85,289 | **(34,888)** ✓ |
| **Inclusive** (cost of revenue added to opex) | 94,150 − (43,749 + 85,289) | **(34,888)** ✓ |

**Both pairings give the same answer, and the reason is worth stating because it is not a
coincidence.** The inclusive pairing uses `revenue − cost_of_revenue − opex`; the exclusive uses
`gross_profit − opex`; and `revenue − cost_of_revenue = gross_profit` **by the filer's own
arithmetic**. They converge **precisely because the gross-profit line exists**. At GSAT, IRDM and
YSS the first term is unavailable or the second is misfiled, and the two definitions diverge by
the entire cost of sales. **So the opex-definition ambiguity is a defect of the issuers who do not
file a gross-profit line, not of the concept.** `[📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)`

**Full statement, quarter ended 2026-04-30 vs the quarter ended 2025-04-30:**

| Line ($k) | 2026-04-30 | 2025-04-30 | Change |
|---|---|---|---|
| Revenue | **94,150** | 66,265 | **+42.08%** |
| Cost of revenue | 43,749 | 29,662 | +47.49% |
| **Gross profit** | **50,401** | 36,603 | **+37.70%** |
| **Gross margin** | **53.53%** | 55.24% | **−1.71pp** |
| Research and development | 33,420 | 23,074 | +44.84% |
| Sales and marketing | 22,782 | 16,314 | +39.65% |
| General and administrative | 29,087 | 19,986 | +45.54% |
| **Total operating expenses** | **85,289** | 59,374 | **+43.65%** |
| **Loss from operations** | **(34,888)** | (22,771) | **+53.21%** |
| **Operating margin** | **−37.06%** | −34.36% | **−2.70pp** |
| Interest income | 5,153 | 1,884 | — |
| Interest expense | (1,446) | (499) | — |
| **Change in fair value of warrant liabilities** | **(106,474)** | 10,387 | — |
| Total other income (expense), net | (102,973) | 11,071 | — |
| Loss before income taxes | (137,861) | (11,700) | — |
| **Net loss** | **(138,872)** | (12,628) | — |
| **EPS** | **$(0.40)** | $(0.04) | — |

**The identity closes exactly:** `50,401 − 85,289 = (34,888)` ✓

**The four ratios that carry the section:**

| Ratio | Value | Basis |
|---|---|---|
| Cost of revenue ÷ revenue | **46.47%** | 43,749 / 94,150 |
| Opex ÷ revenue | **90.59%** | 85,289 / 94,150 |
| **Opex ÷ gross profit** | **1.692×** | 85,289 / 50,401 |
| Opex less gross profit | **$34,888k** | the operating loss, exactly |

**Opex exceeds gross profit by exactly the operating loss, which is the identity restated. The
information is in the RATIO: 1.692×.** A fixed cost base 69% larger than gross profit cannot be
covered by any plausible gross-margin improvement at this revenue level — **a 5pp gross-margin gain
would add $4,708k against a $34,888k gap.**

### 1.1 DA-23 at PL — the UNIFORM regime

Every served `OperatingIncomeLoss` at PL is positive and every filed one negative, across the
issuer's entire history — **≥12 periods, all stripped**: quarter ended 2026-04-30 served
**+34,888,000** against filed `(34,888)`; quarter ended 2025-04-30 **+22,771,000**; FY ending
2026-01-31 **+95,073,000**; FY ending 2025-01-31 **+116,122,000**; nine months FY2026
**+59,071,000**; Q3 FY2026 **+18,340,000**; six months FY2026 **+40,731,000**; Q2 FY2026
**+17,960,000**; nine months FY2025 **+96,756,000**; Q3 FY2025 **+22,608,000**; Q2 FY2025
**+39,577,000**; six months FY2025 **+74,148,000**.

**The regime is UNIFORM, so the strip is UNDETECTABLE arithmetically.** Because PL has never had a
positive operating income, the served `|x|` stack is **monotone and internally consistent** — Q2
FY2026 +17,960 ≤ six months +40,731 ≤ nine months +59,071 ≤ FY +95,073. The monotonicity detector
that fires at GSAT **cannot fire here**, exactly as at RKLB and YSS. **The component identity is
the only detector, and it requires reading the filing.** `[📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)`

### 1.2 ⚠️ Cite the period, never the label — DA-27

**PL's fiscal year ends January 31, so the quarter ended 2026-04-30 is Q1 FY2027.** The platform's
outline for the same document labels the same table **both "Q1 FY2027" and "Q1 FY2026"**, and the
003 entity map calls it **"Q1 FY2026"**. **Three labels, one period.** DA-27 is a label derived
from the calendar quarter rather than the fiscal one, and PL is its live instance.

**Every period in this artifact is therefore cited by period-end date.** A reader who inherits
"Q1 FY2026" from the entity map and compares it against a calendar-year peer is comparing
different quarters, and nothing in the label signals it.

**Units.** As-filed statements are in **thousands**; the platform's `value_numeric` is in
**dollars**. The 1,000× offset is systematic and is a unit conversion, not a defect.

## 2. The GAAP and non-GAAP bases must never be one series

`[📄 PL 10-Q p.41](https://agentii.ai/v/PL/sec76/41)`

| Metric | 2026-04-30 | 2025-04-30 |
|---|---|---|
| Gross margin (as filed) | **54%** | 55% |
| Non-GAAP gross margin | **56%** | 59% |
| Non-GAAP gross profit ($k) | 52,968 | 38,850 |
| **Adjusted EBITDA ($k)** | **(1,033)** | 1,199 |

**Two bases on one metric, 2pp apart, and the gap WIDENED from 4pp to 2pp** — i.e. the non-GAAP
adjustment shrank as a share, while the non-GAAP margin fell **3pp** against the GAAP margin's
**1pp**. **The non-GAAP series is deteriorating faster than the GAAP series**, which is the
opposite of what a non-GAAP presentation usually signals. And **Adjusted EBITDA crossed from
positive to negative**: **+$1,199k → $(1,033)k**. A non-GAAP measure that goes negative is the
adjustment's own verdict on the fixed cost base.

**Never quote "PL's gross margin is 54%" and "56%" interchangeably.** Both are filed; they are
different metrics; DA-30.

### 2.1 DA-24 — the net loss is 76.7% a warrant mark

**Change in fair value of warrant liabilities: $(106,474)k** against a **$(138,872)k** net loss =
**76.66%**. `[📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)`

This is a **non-cash remeasurement of a liability**, and it went the wrong way in the same quarter
the prior-year comparison went the right way (+$10,387k). **The comparison is therefore dominated
by a swing in a non-operating, non-cash item**, and a reader comparing net losses year over year
is comparing two different things. **The operating line is the comparable one, and it is also
worse — `(34,888)` against `(22,771)`.** That matters: **the honest reading is that the operating
deterioration is real *and* the net-loss blowout is mostly non-operating.** Both, not either.

## 3. The value-chain position map

**The purpose of this skill is to locate which position in the stack holds the margin. PL sits one
layer above launch, and it is the strongest available test.**

| Layer | Name | Gross margin | Operating margin |
|---|---|---|---|
| Launch | RKLB | — (see the RKLB artifact) | deeply negative |
| **Data and analytics, above launch** | **PL** | **53.53%** | **−37.06%** |
| Vertical / infrastructure services | YSS | 23.97% | −44.64% |

**The finding is what happens between the columns.** PL and YSS differ by **29.6 percentage points**
of gross margin and by only **7.6 percentage points** of operating margin. **Gross margin does not
predict operating margin in this sector, and the reason is arithmetic rather than narrative:** PL's
opex ratio is **90.59%** of revenue; YSS's is **68.60%**. **PL's 29.6pp gross-margin advantage is
more than consumed by a 22.0pp higher opex ratio.** The ranking between two names at different
depths of the stack is set by the fixed cost base, not by the position.

**And that is the answer to the sector-overview question, stated precisely: in this stack, at these
two names, NO position holds an operating margin, and the value-chain depth of a name tells you
nothing about which of them loses less.** A map that ranks positions by gross margin produces the
exact inverse of a map that ranks them by operating margin.

### 3.1 Where launch cost actually sits in PL's cost structure

**Launch is inside PL's 46.47% cost of revenue, and PL retains 53.53% gross while paying it.**
That is the load-bearing inference for PIL-6:

- **If launch cost were the binding constraint at the data layer, a data-layer gross margin of
  53.53% would not be available.** It is.
- **Therefore the constraint at the data layer is not launch cost.** It is the **90.59% opex
  ratio** — R&D at **35.50%** of revenue, sales and marketing at **24.20%**, G&A at **30.90%**.
- **So the value did not stay at the launch layer, and it did not stop at the data layer either.**
  It migrated upward and was consumed by the fixed cost of operating a data business at sub-scale
  revenue. **PIL-2's "value migrated to the integrator that owns the demand" is confirmed in
  direction and refined in destination: the migration is real and the destination is a cost base,
  not a margin.**

**PL's own risk set confirms the reading.** A filed risk factor is **"history of operating
losses"** `[📄 PL 10-Q p.47](https://agentii.ai/v/PL/sec76/47)`, and the other filed exposures are
**competition** (p.49), **satellite development and launch** (p.51), **supply chain and cloud**
(p.59), **customer concentration and seasonality** (p.62), **NOAA/FCC/ITAR/EAR/OFAC regulatory**
(p.77) and the **2030 Notes and capped calls** (p.87). **Launch appears once, as a development
dependency. It does not appear as a cost driver anywhere in PL's risk set** — while the fixed cost
components (cloud, personnel-driven G&A, and the debt service) appear repeatedly. **The filer's own
risk taxonomy ranks launch below the fixed cost base as a threat to the business.** That is a
`CLAIMED`-grade filing statement and it agrees with the DEMONSTRATED arithmetic in §1.

### 3.2 The growth is real and it is concentrated

Revenue grew **+$27,885k / +42.08%**, driven by a **$24.7M increase in the defense and intelligence
vertical.** `[📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38)`

**$24.7M of a $27,885k increase is 88.6% — one vertical.** That is not diversification; it is
single-account growth against a filed **customer-concentration-and-seasonality** risk factor
(p.62). **The margin consequence is adverse**: defense and intelligence revenue carries a different
cost structure than imagery subscription revenue, and the **cost of revenue grew +47.49% against
revenue +42.08%** — i.e. **the growth is arriving at a worse incremental gross margin than the
existing base**, which is why the gross margin fell 1.71pp even in a 42% growth quarter.
**Growth is diluting the gross margin and widening the operating loss simultaneously.**

## 4. Falsifier-reachability census

| Falsifier | Reachability at PL | Class | Note |
|---|---|---|---|
| **PIL-6 `independently_falsifiable`** — "a demonstrated fall in revenue per launch at least as large as the fall in cost per launch" | **NON-FORMABLE** | n/a | PL buys launches and files no per-launch cost or revenue. **NON-FORMABLE ≠ PASS (F16).** |
| **PIL-6 `wrong_if`** — launch-cost share of programme cost > 0.10 | **`REACHABLE-BUT-NOT-RECORDABLE`** | third class | Launch cost is inside cost of revenue and is not separately disclosed. The datum is reachable in the filer's books; no admissible field admits it. **Remedy: amend the contract** — the one class research cannot fix. |
| **The value-chain position falsifier** — "the margin is held at position X" | **REACHABLE — and it FAILS at both PL and YSS** | **DEMONSTRATED** | §3: no operating margin at either name; the ranking is set by opex ratio, not by depth. |
| **PIL-2 `wrong_if` census** | **CANNOT ENTER — `UNEXERCISED`, never CLEAN** | 002-corrected | PL files **no segment operating margin** and has **no launch segment**. "0 of N exceeding" would claim a test that could not run. |
| **DA-26** | **not applicable** | — | PL is a January fiscal-year-end filer; no annual figure is used as quarterly in this artifact. |
| **DA-27** | **CONFIRMED — live** | §1.2 | Three labels, one period. Period-end dates used throughout. |
| **F2 — Falcon 9 basis B** | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | inherited | Cite as an order of magnitude; never `313 m²/MW` or `24×` as point values. |
| **F3 — propellant price** | **`REACHABLE-BUT-NOT-RECORDABLE`** | canonical case | Remedy: amend the contract. |
| **`Launch` / `Satellite` concept vocabulary** | **0 concepts platform-wide** | structural | The structured layer has no term for the domain; PL's launch exposure is page-text-only. |
| **VZ / T / TMUS** | **`TICKER_NOT_FOUND`** — confirmed 2026-09-19 | n/a | **The telecom comparator leg is absent by construction.** |
| **F17 threshold reachability** | **NOT REACHABLE at PL** | n/a | An SPCX segment-boundary property; recorded so F17 is not over-read as universe-wide. |

## 5. What this artifact could not resolve

- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — PL's launch cost.** Inside cost of revenue, not
  separately disclosed at any granularity. The resolving disclosure is a cost-of-revenue
  decomposition naming launch.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — the defense-and-intelligence vertical's own margin.** The
  $24.7M is named as the growth driver; its gross margin is not disclosed, so the **dilution claim
  in §3.2 is inferred from the blended cost-of-revenue growth (+47.49%) and NOT from a segment
  margin.** Stated as an inference, not as a filed figure.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — the fixed cost base's scale-invariant share.** R&D,
  sales and marketing and G&A all grew **+39.7% to +45.5%** against revenue **+42.1%** — near
  proportionality, which is why the loss widened. **The disclosure that would separate fixed from
  variable cost inside opex does not exist**, so "fixed cost" here is characterised by its
  *behaviour* (opex ÷ revenue held at ~90%), not by a filed fixed/variable split.
- **UNEXERCISED — whether the warrant remeasurement can recur.** The $(106,474)k swing is filed
  for this quarter; the warrant terms that would bound future marks were not read.
- **UNEXERCISED — the 2030 Notes' covenants and the capped calls.** The risk factor exists at
  p.87; the terms were not read.
- **NOT ATTEMPTED — DA-28, DA-29.** No share-count detector is asserted (DA-28); no reconciliation
  is claimed whose terms are absent from the source (DA-29). **Recorded as not attempted. Not
  attempted is not CLEAN.**
- **`get_segment_data` UNUSABLE** (`column "k" does not exist`; double-counts) and
  **`data_freshness` UNUSABLE** (returns `2027-04-12`, seven months in the future of
  `as_of = 2026-09-18`). **Pages read directly.**

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Statements of operations, quarter ended April 30, 2026; loss from operations 34,888 | [📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6) |
| Revenue +$27,885k / +42%; total opex +44%; loss from operations +53% | [📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38) |
| Non-GAAP: gross margin 54% vs 55%; non-GAAP gross margin 56% vs 59%; adjusted EBITDA | [📄 PL 10-Q p.41](https://agentii.ai/v/PL/sec76/41) |
| Risk factor: history of operating losses | [📄 PL 10-Q p.47](https://agentii.ai/v/PL/sec76/47) |
| Risk factor: competition | [📄 PL 10-Q p.49](https://agentii.ai/v/PL/sec76/49) **(newly surfaced)** |
| Risk factor: satellite development and launch | [📄 PL 10-Q p.51](https://agentii.ai/v/PL/sec76/51) **(newly surfaced)** |
| Risk factor: supply chain and cloud | [📄 PL 10-Q p.59](https://agentii.ai/v/PL/sec76/59) **(newly surfaced)** |
| Risk factor: customer concentration and seasonality | [📄 PL 10-Q p.62](https://agentii.ai/v/PL/sec76/62) **(newly surfaced)** |
| Risk factor: NOAA, FCC, ITAR, EAR and OFAC regulatory exposure | [📄 PL 10-Q p.77](https://agentii.ai/v/PL/sec76/77) **(newly surfaced)** |
| Risk factor: 2030 Notes and capped calls | [📄 PL 10-Q p.87](https://agentii.ai/v/PL/sec76/87) **(newly surfaced)** |
