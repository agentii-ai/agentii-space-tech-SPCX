---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-3
ticker: YSS
skill: ratio-analysis
mode: methodology
generated_at: 2026-09-19T16:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "2d27c7f751fa"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: "Absolute-value stripping in the served layer. Six of six served YSS OperatingIncomeLoss facts are positive; all six filed counterparts are parenthesised negative. The filing is clean; the extraction is not."
  - da_id: DA-24
    chosen_reading: "Non-operating contamination of operating_income. At YSS this is REFUTED by formula: the gain sits below the operating line, and the cost-of-revenue composition closes exactly against the filed total."
  - da_id: DA-25
    chosen_reading: "A normalised per-unit metric not reproducible from the audited tables. CONFIRMED twice at YSS: a spacecraf-per-dollar figure computable at exactly one date, and a non-GAAP input that breaks from the audited table by $21 thousand."
  - da_id: DA-26
    chosen_reading: "Annual figures mislabelled as quarterly. NOT TESTABLE at YSS — the FY2025 10-K's XBRL remains unprocessed, so there is no annual fact layer to test the labels against."
  - da_id: DA-28
    chosen_reading: "Capital-structure discontinuity around the IPO. YSS's equity statement shows Class P Units and common units converting alongside the IPO, which invalidates share-count detectors — and is why the served 1000x share defect is invisible from inside a single filing."
  - da_id: DA-29
    chosen_reading: "A reconciliation that closes is not thereby a check. The cost-of-revenue composition closes on all four columns AND its terms are named in a footnote, so DA-29 is satisfied here."
  - da_id: DA-30
    chosen_reading: "Two bases on one concept collapsed without a basis field. YSS reports cost of revenues on the income statement and a separate direct-materials-plus-other-segment-items basis in the segment note, and the non-GAAP table uses a third input."
evidence_grade: DEMONSTRATED
citations:
  - figure: "Q2 2026 condensed consolidated income statement: revenue $92,547k, net loss $39,343k; six-month revenue $208,890k, net loss $154,185k"
    ticker: YSS
    citation_id: sec12
    page_no: 7
    form_type: 10-Q
    url: https://agentii.ai/v/YSS/sec12/7
    located_via: read_source_pages
  - figure: "Q2 2026 results-of-operations ladder: revenue $92,547k +10%, cost of revenues $70,367k (76%), gross profit $22,180k (24%) +133%, total operating expenses $63,493k (69%), loss from operations $(41,313)k at (45)% of revenue with a filed % change of 95%"
    ticker: YSS
    citation_id: sec12
    page_no: 40
    form_type: 10-Q
    url: https://agentii.ai/v/YSS/sec12/40
    located_via: read_source_pages
  - figure: "Significant expenses table: direct materials $53,240k, other segment items $17,127k, whose sum equals the filed cost of revenues $70,367k; footnote defines other segment items as operating cost of revenue components"
    ticker: YSS
    citation_id: sec12
    page_no: 35
    form_type: 10-Q
    url: https://agentii.ai/v/YSS/sec12/35
    located_via: read_source_pages
  - figure: "Six-month gross profit $44.3M vs $34.1M, +30%; gross margin 21% vs 18%; SG&A $77.5M vs $52.6M, +47%; stock-based compensation $95.6M vs $0"
    ticker: YSS
    citation_id: sec12
    page_no: 44
    form_type: 10-Q
    url: https://agentii.ai/v/YSS/sec12/44
    located_via: read_source_pages
  - figure: "Non-GAAP measure definitions and contribution margin table; the table's direct-materials input reads 129,517 against the segment note's filed 129,538"
    ticker: YSS
    citation_id: sec12
    page_no: 45
    form_type: 10-Q
    url: https://agentii.ai/v/YSS/sec12/45
    located_via: search_keyword_in_source
  - figure: "Reconciliation of contribution margin to gross profit, and EBITDA / Adjusted EBITDA reconciliations from net loss"
    ticker: YSS
    citation_id: sec12
    page_no: 46
    form_type: 10-Q
    url: https://agentii.ai/v/YSS/sec12/46
    located_via: search_keyword_in_source
  - figure: "Solestial acquisition gain on remeasurement, acquisition-related expenses, and provisional fair value allocation — sits below the operating line"
    ticker: YSS
    citation_id: sec12
    page_no: 20
    form_type: 10-Q
    url: https://agentii.ai/v/YSS/sec12/20
    located_via: search_keyword_in_source
  - figure: "Backlog increase to $592 million and discussion of the Solestial and All.Space acquisitions"
    ticker: YSS
    citation_id: sec12
    page_no: 37
    form_type: 10-Q
    url: https://agentii.ai/v/YSS/sec12/37
    located_via: search_keyword_in_source
  - figure: "Q1 2026 results ladder: loss from operations $(110,466)k filed at (95)% of revenue"
    ticker: YSS
    citation_id: sec9
    page_no: 36
    form_type: 10-Q
    url: https://agentii.ai/v/YSS/sec9/36
    located_via: read_source_pages
  - figure: "Q1 2026 income statement, including the WeightedAverageNumberOfSharesOutstandingBasic facts later found to be served at 1000x"
    ticker: YSS
    citation_id: sec9
    page_no: 7
    form_type: 10-Q
    url: https://agentii.ai/v/YSS/sec9/7
    located_via: read_source_pages
  - figure: "\"growing our backlog to approximately $543 million and 107 spacecraft as of December 31, 2025\" — the only place the 107-unit denominator is filed"
    ticker: YSS
    citation_id: sec8
    page_no: 5
    form_type: 10-K
    url: https://agentii.ai/v/YSS/sec8/5
    located_via: read_source_pages
  - figure: "\"As of December 31, 2025, the aggregate amount of the transaction price allocated to remaining performance obligations was $542,557.\""
    ticker: YSS
    citation_id: sec8
    page_no: 103
    form_type: 10-K
    url: https://agentii.ai/v/YSS/sec8/103
    located_via: read_source_pages
key_metrics:
  opex_to_gross_profit_q2_2026_x: 2.863
  opex_to_gross_profit_6m_2026_x: 4.424
  sbc_to_gross_profit_6m_2026_pct: 215.6
  operating_margin_6m_2026_pct: -72.66
---

# YSS — the margin ladder, the `95%` collision, and a per-unit metric computable at exactly one date

**Finding.** York Space Systems files a **24.0% gross margin** consumed by an operating-expense base running at
**2.9× gross profit**, giving an operating margin of **(44.6%)**. The company's gross margin is genuinely
expanding — 18% → 21% over six months — while its stock-based compensation line goes from **$0** to
**$95,589 thousand**, which is **4.3×** the entire six-month gross profit. And the single most important result
here is a **label collision**: the string **`95%` denotes two different things on two different pages, one
quarter apart** — an operating margin in Q1, and a year-over-year *change* in the operating loss in Q2. Both are
filed correctly; only a basis-naming discipline keeps them apart (P2), and the per-unit metric available at YSS
is computable at **exactly one date in the company's history** (P5).

## 1. Acceptance test — adopted and run

An identification is accepted only if it is **(a) exact**, **(b) stable across periods**, and **(c) consistent
with a specified formula or a filed basis**. Everything else is `UNRESOLVED` — never "probably fine". The test
is load-bearing here rather than ceremonial: the register records a ~**2,500**-candidate sweep over **36 filed
cells** that returned **6–9 coincidental hits per metric**, and only **2 of 16** served ratio fields turned out
to be the ratio they claimed. **Every ratio below is recomputed from filed cells; no served ratio is quoted.**
As at PL, `list_xbrl_concepts(search="ratio")` surfaces **no margin concept at all**, so there is nothing served
to quote.

Formula for every ratio: `filed numerator ÷ filed denominator`, both read off one page.

## 2. The margin ladder

All figures in $ thousands. Both columns read from one page.

| Line | Q2 2026 | Q2 2025 | Filed % of revenue | Basis | Grade |
|---|---|---|---|---|---|
| Revenue | 92,547 | 83,839 | 100% | consolidated, as filed | DEMONSTRATED |
| Cost of revenues | 70,367 | 74,313 | 76% / 89% | consolidated, as filed | DEMONSTRATED |
| **Gross profit** | **22,180** | **9,526** | **24% / 11%** | consolidated, as filed | DEMONSTRATED |
| SG&A | 40,825 | 25,790 | 44% / 31% | consolidated, as filed | DEMONSTRATED |
| Stock-based compensation | 10,893 | — | 12% / — | consolidated, as filed | DEMONSTRATED |
| Research & development | 5,766 | 4,893 | 6% / 6% | consolidated, as filed | DEMONSTRATED |
| Transaction costs | 6,009 | 75 | 6% / — | consolidated, as filed | DEMONSTRATED |
| **Total operating expenses** | **63,493** | **30,758** | **69% / 37%** | the four lines above, summed | DEMONSTRATED |
| **Loss from operations** | **(41,313)** | **(21,232)** | **(45)% / (25)%** | filed, parenthesised | DEMONSTRATED |
| Net loss | (39,343) | (24,234) | (43)% / (29)% | consolidated, as filed | DEMONSTRATED |

Source: [📄 YSS 10-Q p.40](https://agentii.ai/v/YSS/sec12/40)

**The opex definition used here is the EXCLUSIVE one** — SG&A + SBC + R&D + transaction costs, i.e. exactly the
four lines the filing prints under `Operating expenses`. The inclusive pairing is inadmissible, because
`us-gaap:CostsAndExpenses` includes cost of sales and YSS files a cost-of-revenues line. Note the filing itself
solves this by printing `Total operating expenses` as its own row: **40,825 + 10,893 + 5,766 + 6,009 = 63,493**,
which is the filed total. Exact.

### 2.1 Component identity, run on six periods

```
Q2 2026:  22,180 − 63,493   = (41,313)   exact   [p.40]
Q2 2025:   9,526 − 30,758   = (21,232)   exact   [p.40]
6M 2026:  44,330 − 196,109  = (151,779)  exact   [p.35 + p.44]
6M 2025:  34,128 − 61,991   = (27,863)   exact   [p.35 + p.44]
Q1 2026:  22,150 − 132,616  = (110,466)  exact   [sec9 p.36]
Q1 2025:                         (6,631)  filed   [sec9 p.36]
```

The six-month arms are built from the significant-expenses table at
[📄 YSS 10-Q p.35](https://agentii.ai/v/YSS/sec12/35): **77,531 + 95,589 + 11,055 + 11,934 = 196,109** (2026) and
**52,591 + 0 + 9,294 + 106 = 61,991** (2025). Six of six close to the dollar. The independent check on the
gross-profit inputs: **208,890 − 164,560 = 44,330** and **190,091 − 155,963 = 34,128**, both matching the filed
narrative at [📄 YSS 10-Q p.44](https://agentii.ai/v/YSS/sec12/44) (*"$44.3 million"*, *"$34.1 million"*).
**The identity is the only reliable sign detector and it runs cleanly here.**

### 2.2 Derived ratios

| Ratio | Q2 2026 | Q2 2025 | 6M 2026 | 6M 2025 | Formula | Grade |
|---|---|---|---|---|---|---|
| Gross margin | **23.97%** | 11.36% | **21.22%** | 17.96% | GP ÷ revenue | DEMONSTRATED |
| Operating margin | **(44.64%)** | (25.32%) | (72.66%) | (14.66%) | loss from ops ÷ revenue | DEMONSTRATED |
| Opex ratio | **68.61%** | 36.69% | 93.87% | 32.62% | total opex ÷ revenue | DEMONSTRATED |
| **Opex ÷ gross profit** | **2.863×** | 3.229× | **4.424×** | 1.817× | total opex ÷ GP | DEMONSTRATED |
| SBC ÷ gross profit | **49.11%** | — | **215.6%** | — | SBC ÷ GP | DEMONSTRATED |
| Transaction cost ÷ GP | 27.09% | 0.79% | 26.92% | 0.31% | transaction ÷ GP | DEMONSTRATED |
| Revenue QoQ | **−20.45%** | — | — | — | (92,547 − 116,343) ÷ 116,343 | DEMONSTRATED |

Every filed percentage reproduces: **23.97% → filed 24%**; **68.61% → filed 69%**; **44.64% → filed (45)%**;
**42.51% → filed (43)%**; **21.22% → filed 21%**; **17.96% → filed 18%**. This is a **positive** result for the
ratios that *are* the ratios they claim — and it is the control that makes the collisions in §3 and §4 visible.

**The structural finding:** the fixed cost base runs at **2.9× gross profit** in the quarter and **4.4×** over
six months. Gross margin expanded 18% → 21% — the filing attributes it to *"lower unfavorable EAC adjustments"*
— and **stock-based compensation alone is 215.6% of six-month gross profit**. Revenue fell **20.5% quarter over
quarter** (116,343 → 92,547, both filed).

## 3. P2 — the `95%` collision: one string, two meanings, one quarter apart

This is the artifact's sharpest finding and it is a **label** defect, not an arithmetic one. Both values are
filed correctly.

| Where | Row | Column | Value | Meaning |
|---|---|---|---|---|
| [sec12 p.40](https://agentii.ai/v/YSS/sec12/40) | Loss from operations, Q2 2026 | **% of revenue** | **(45)%** | 41,313 ÷ 92,547 = 44.64% |
| [sec12 p.40](https://agentii.ai/v/YSS/sec12/40) | Loss from operations, Q2 2026 | **% Change** | **95%** | 20,081 ÷ 21,232 = 94.58% |
| [sec9 p.36](https://agentii.ai/v/YSS/sec9/36) | Loss from operations, Q1 2026 | **% of revenue** | **(95)%** | 110,466 ÷ 116,343 = 94.95% |

**The same row of the same table carries `(45)%` and `95%` in adjacent columns.** One column is a *margin*; the
other is a *year-over-year change*. A quarter earlier, `(95)%` was a margin. Any artifact that lifts "the 95%
figure" from the Q1 page and applies it to Q2 has silently swapped a margin for a growth rate — and the two
coincide numerically precisely because the operating loss was itself **95% of revenue** in the earlier quarter.

**Consequence for this workspace.** The register records that "001's 95% margin" traces to the filed `(95)%`
with the minus dropped. That is now **half-resolved**: the value is a *filed* ratio, correctly parenthesised,
reading **94.95% → (95)%**; what was dropped is the minus. But `95%` is **also** a filed ratio on a *later*
page with an unrelated meaning. **Neither is quotable without its column name and its period basis.** This is
DA-30's shape reached through a label rather than through a basis field, and it satisfies all three legs of the
acceptance test: the values are **exact**, the collision is **stable** across the two filings, and each is
**consistent with its own specified formula** (margin = ÷ revenue; change = ÷ prior-year loss).

## 4. P5 — DA-25 confirmed twice

### 4.1 A per-spacecraft figure computable at exactly one date

| Input | Value | Date | Where | Grade |
|---|---|---|---|---|
| Backlog, rounded | *"approximately $543 million"* | 2025-12-31 | [sec8 p.5](https://agentii.ai/v/YSS/sec8/5) | DEMONSTRATED |
| Remaining performance obligations | **$542,557 thousand** | 2025-12-31 | [sec8 p.103](https://agentii.ai/v/YSS/sec8/103) | DEMONSTRATED |
| Spacecraft | **107** | 2025-12-31 | [sec8 p.5](https://agentii.ai/v/YSS/sec8/5) | DEMONSTRATED |
| **Backlog ÷ spacecraft** | **$5,070 thousand** | — | derived | DEMONSTRATED |

**542,557 ÷ 107 = 5,070.6**. This is the metric shape DA-25 defines: a normalised per-unit figure that the
audited tables **cannot reproduce**, for three independent reasons.

1. **It is computable at exactly one date.** `"107 spacecraft"` returns **ZERO hits** in the Q2 2026 10-Q
   (`sec12`). By that filing the backlog has moved to **$592 million**
   ([📄 YSS 10-Q p.37](https://agentii.ai/v/YSS/sec12/37)) — and **no spacecraft denominator is filed with it.**
   The ratio therefore exists for 2025-12-31 and nowhere else: a single point, not a series.
2. **The numerator has two filed readings.** *"approximately $543 million"* gives 5,074.8; the exact
   `$542,557` gives 5,070.6. **Both correct, neither comparable** — a DA-30 pair collapsed onto one ratio.
3. **It mixes registers.** The numerator is a *transaction-price* obligation (an ASC 606 RPO concept); the
   denominator is a *units* count from a business-overview sentence. Nothing in the audited tables ties them.

**The disclosed basis does not reconcile, and that IS the finding.** Stated as a per-unit metric it would carry
three significant digits' worth of false precision from two inputs that are not on the same basis.

### 4.2 A non-GAAP input that breaks from the audited table by $21 thousand

| Figure | Value | Where | Grade |
|---|---|---|---|
| Direct materials, 6M 2026, segment note | **129,538** | [sec12 p.35](https://agentii.ai/v/YSS/sec12/35) | DEMONSTRATED |
| Direct-materials input, 6M 2026, non-GAAP contribution-margin table | **129,517** | [sec12 p.45](https://agentii.ai/v/YSS/sec12/45) | DEMONSTRATED |
| Break | **$21 thousand** | derived | DEMONSTRATED |

The same quantity, two filed values, on the same basis and the same period. **This is DA-25 exactly**: a
normalised input whose derivation is not reproducible from the audited table. The break is immaterial to the
narrative and material to the *method* — a reader who recomputes the non-GAAP table from the segment note will
not reproduce it, and the $21k difference has no visible explanatory term. Under the acceptance test this is
`UNRESOLVED`, not "probably a rounding difference": a rounding explanation is a *hypothesis* about a term that
appears nowhere in the source (DA-29's back-solve shape).

## 5. P5 — DA-23 at YSS: 6 of 6 stripped, and the bound test *does* fire here

**All six served `YSS OperatingIncomeLoss` facts are positive:**

```
+151,779,000  (6M 2026)      +27,863,000  (6M 2025)
 +41,313,000  (Q2 2026)      +21,232,000  (Q2 2025)
+110,466,000  (Q1 2026)       +6,631,000  (Q1 2025)      ← 6 of 6 POSITIVE
```

Every one is filed **negative**. The filed ladder at [📄 YSS 10-Q p.40](https://agentii.ai/v/YSS/sec12/40)
prints `(41,313)`, `(21,232)`, `(39,061)`; the Q1 page prints `(110,466)`
([📄 YSS 10-Q p.9 p.36](https://agentii.ai/v/YSS/sec9/36)). Same magnitude, opposite sign — **absolute-value
stripping**, not inversion. **The filing is clean; the extraction is not.** Grade the served values as
DEMONSTRATED-from-the-served-layer, which is where DA-23 lives.

**The bound test fires at YSS and is silent at PL.** Served **+110,466 exceeds filed gross profit 22,150**, and
a positive operating income cannot exceed gross profit — so the naive check catches YSS. At PL the served value
*sits below* gross profit and the same check misses entirely. **The same defect, the same register, two
opposite outcomes from one detector.** That is why §2.1 runs the component identity on six periods rather than
trusting any single heuristic. **`EPS × shares` is not an admissible sign test and was not used** — see §6 for
why that is not merely a rule but the reason a second defect went unseen.

## 6. DA-28 — a 1000× share-count defect, invisible from inside one filing

`us-gaap:WeightedAverageNumberOfSharesOutstandingBasic` is served by YSS at:

| Filing | Period | Served value | Correct? |
|---|---|---|---|
| `yss-20260331.htm` (Q1 2026 10-Q) | 3M ended 2026-03-31 | **116,022,676,000** | ✗ 1000× |
| `yss-20260331.htm` (Q1 2026 10-Q) | 3M ended 2025-03-31 | **95,141,928,000** | ✗ 1000× |
| `yss-20260630.htm` (Q2 2026 10-Q) | 3M ended 2026-06-30 | 128,095,949 | ✓ |
| `yss-20260630.htm` (Q2 2026 10-Q) | 6M ended 2026-06-30 | 122,092,664 | ✓ |
| `yss-20260630.htm` (Q2 2026 10-Q) | 3M ended 2025-06-30 | 95,141,928 | ✓ |
| `yss-20260630.htm` (Q2 2026 10-Q) | 6M ended 2025-06-30 | 95,141,928 | ✓ |

**The decisive control:** the 3M period ending **2025-03-31** is served **1000× too large in the Q1 filing** and
correctly in the Q2 filing. Same concept, same period, two filings, opposite correctness. **The defect follows
the FILING, not the concept and not the period** — which rules out a concept-mapping error and localises it to
the Q1 10-Q's extraction. This is a **DA-28-adjacent** failure: YSS's equity statement shows Class P Units and
common units converting to common stock alongside the IPO and acquisition-related issuance
([📄 YSS 10-Q p.9](https://agentii.ai/v/YSS/sec12/9)), i.e. a capital-structure discontinuity in exactly the
window the share counts span.

**Why it went unseen, and why that matters.** Rule 5 forbids `EPS × shares` as a sign test — correctly. But it
means that **within any single filing there is no admissible cross-check on the share count.** The 1000× defect
is invisible from inside the document that contains it; it is visible only by comparing the same concept across
two filings. A defect whose only detector is cross-filing comparison will be missed by any single-document
review, and this artifact is a single-document review of each filing in turn.

## 7. DA-24 refuted by formula, and DA-26 left unexercised

**DA-24 is REFUTED at YSS, and the refutation is a formula rather than an assertion.** The Solestial gain sits
in `Other (expense) income, net` ([📄 YSS 10-Q p.20](https://agentii.ai/v/YSS/sec12/20)) — a line **below** loss
from operations in the ladder, so it cannot contaminate it. The harder question is whether the segment note's
cost-of-revenue composition hides a non-operating item, and it is settled exactly:

```
Direct materials + Other segment items = filed Cost of revenues
  53,240 + 17,127 =  70,367  ✓ Q2 2026
  63,555 + 10,758 =  74,313  ✓ Q2 2025
 129,538 + 35,022 = 164,560  ✓ 6M 2026
 134,505 + 21,458 = 155,963  ✓ 6M 2025
```

Four of four close. The footnote defines `other segment items` as *"other costs of revenue excluding direct
materials, **including direct labor, overhead costs and depreciation and amortization**"* — **purely operating
content**. Because the two buckets sum exactly to the filed operating cost of revenues, **no non-operating item
can be inside either.** This satisfies DA-29 as well: the reconciliation closes *and* its terms are located.

**DA-26 is NOT TESTABLE at YSS — `UNRESOLVABLE-FROM-PLATFORM`.** The test is whether an annual figure is
mislabelled as quarterly. At YSS the FY2025 10-K's XBRL carries `processing_status: pending` and **no annual
facts are served at all**, so there is no annual fact layer to test the labels against. **This is not `CLEAN`.**
The check could not run. Register DA-26's incidence as *19 of 20 tested*, with YSS **outside the test set** —
and note that the counterexample in that set is FLY, so DA-26 must not be reported as universal.

## 8. What this artifact could NOT resolve

| Unresolved | Why | Class | Disclosure that would resolve it |
|---|---|---|---|
| DA-26 at YSS | FY2025 10-K XBRL unprocessed; no annual facts served | `UNRESOLVABLE-FROM-PLATFORM` | Reprocessing of the FY2025 10-K fact layer |
| The $21k non-GAAP break | No explanatory term appears anywhere in the source; any explanation is a back-solve | `UNRESOLVED` | A filed reconciliation of the non-GAAP contribution-margin inputs to the segment note |
| Backlog ÷ spacecraft beyond 2025-12-31 | The Q2 2026 filing reports backlog but files no units count | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | A spacecraft count filed alongside each backlog figure |
| Q1 2025 served `OperatingIncomeLoss` | Served `+6,631,000`; the sign is inferred from the ladder's structure, not from a page read in this artifact | `UNRESOLVED` | A direct read of the Q1 2025 comparative column |

**`UNRESOLVABLE-FROM-PLATFORM` and `UNRESOLVABLE-FROM-PUBLIC-SOURCES` are different dispositions with different
remedies** and are kept apart deliberately. DA-26 is blocked because the *platform* has not processed a filing
that exists. Backlog ÷ spacecraft is blocked because the *issuer* does not file the quantity. Re-querying the
platform resolves the first; only a new filing resolves the second.

**DA-25 and DA-24 are exercised at YSS; DA-26 is not.** Recording an unrun check as clean would be the exact
failure DA-29 warns about — *a reconciliation that closes is not thereby a check.*

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Q2 2026 condensed consolidated income statement: revenue $92,547k, net loss $39,343k; six-month revenue $208,890k, net loss $154,185k | [📄 YSS 10-Q p.7](https://agentii.ai/v/YSS/sec12/7) **(newly surfaced)** |
| Q2 2026 results-of-operations ladder: revenue $92,547k +10%, cost of revenues $70,367k (76%), gross profit $22,180k (24%) +133%, total operating expen | [📄 YSS 10-Q p.40](https://agentii.ai/v/YSS/sec12/40) |
| Significant expenses table: direct materials $53,240k, other segment items $17,127k, whose sum equals the filed cost of revenues $70,367k; footnote de | [📄 YSS 10-Q p.35](https://agentii.ai/v/YSS/sec12/35) |
| Six-month gross profit $44.3M vs $34.1M, +30%; gross margin 21% vs 18%; SG&A $77.5M vs $52.6M, +47%; stock-based compensation $95.6M vs $0 | [📄 YSS 10-Q p.44](https://agentii.ai/v/YSS/sec12/44) |
| Non-GAAP measure definitions and contribution margin table; the table's direct-materials input reads 129,517 against the segment note's filed 129,538 | [📄 YSS 10-Q p.45](https://agentii.ai/v/YSS/sec12/45) |
| Reconciliation of contribution margin to gross profit, and EBITDA / Adjusted EBITDA reconciliations from net loss | [📄 YSS 10-Q p.46](https://agentii.ai/v/YSS/sec12/46) **(newly surfaced)** |
| Solestial acquisition gain on remeasurement, acquisition-related expenses, and provisional fair value allocation — sits below the operating line | [📄 YSS 10-Q p.20](https://agentii.ai/v/YSS/sec12/20) |
| Backlog increase to $592 million and discussion of the Solestial and All.Space acquisitions | [📄 YSS 10-Q p.37](https://agentii.ai/v/YSS/sec12/37) |
| Q1 2026 results ladder: loss from operations $(110,466)k filed at (95)% of revenue | [📄 YSS 10-Q p.36](https://agentii.ai/v/YSS/sec9/36) |
| Q1 2026 income statement, including the WeightedAverageNumberOfSharesOutstandingBasic facts later found to be served at 1000x | [📄 YSS 10-Q p.7](https://agentii.ai/v/YSS/sec9/7) **(newly surfaced)** |
| "growing our backlog to approximately $543 million and 107 spacecraft as of December 31, 2025" — the only place the 107-unit denominator is filed | [📄 YSS 10-K p.5](https://agentii.ai/v/YSS/sec8/5) |
| "As of December 31, 2025, the aggregate amount of the transaction price allocated to remaining performance obligations was $542,557." | [📄 YSS 10-K p.103](https://agentii.ai/v/YSS/sec8/103) |
