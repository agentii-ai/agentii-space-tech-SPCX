---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: IRDM
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
# Written at the pin whose rules it obeys: this artifact APPLIES DA-29 (§7 — every
# reconciliation term named and located) and DA-30 (§6 — the basis named before use), both
# added by the 1.4.0 → 1.5.0 bump at 002 Phase 3. `pins_match_thesis` accepts {1.4.0, 1.5.0};
# 1.4.0 is the grandfathered set for the 23 artifacts written before the bump. 1.5.0 is a
# RECORDED, not an assumed, pin.
constitution_pin: "1.5.0"
assumption_pin: "2"
# Q57 resolved 2026-09-18: re-derived from plugins/agent-plugins/agentii-equity-agent/skills/agentii/recent-quarter
# AND plugins/vertical-plugins/equity-research-core/skills/agentii/recent-quarter — two independent
# roots AGREE. Algorithm dispatch.skill_version_hash() (scripts/dispatch.py:132) validated 9/9 against
# the six pins tabled in theses/001-technology-baseline/reproduce.md. Four packaging/targets trees
# contain decoy recent-quarter/ dirs and ALL FAIL the validation 0/6 — they are not used here, and
# UNRESOLVED is not recorded.
skill_pin: "07d26b9c738b"
as_of: 2026-09-18
# Every fact and page in this artifact was retrieved this session. The platform reported
# `data_freshness: 2027-04-12` on every call — a forward-dated marker, which cannot be used as a
# corpus version. Nothing to pin. (Same disposition as the MSFT artifact of this date.)
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "|x| absolute-value stripping of a fact's sign — concept-agnostic, and PER-FACT, not per-period. Inversion (negation) is a DIFFERENT defect, and this artifact reports one live inversion (a filed $(0.01) served as +0.01) separately from its strips."
  - da_id: "DA-24"
    chosen_reading: "a disposal gain sitting ABOVE the operating subtotal, tested on the calculation linkbase as an arc whose child is OperatingIncomeLoss"
  - da_id: "DA-25"
    chosen_reading: "an issuer-defined per-unit metric that cannot be reproduced from the filed reconciliation terms (the DA-29 corridor test applied to per-unit metrics)"
  - da_id: "DA-26"
    chosen_reading: "a twelve-month value served under a quarterly label; mechanism = fiscal_period derived as calendar_quarter(period_end)"
  - da_id: "DA-27"
    chosen_reading: "fiscal labels derived from the calendar rather than from the issuer's fiscal calendar; tested on fiscal_year_end_month AND on the field the value was read from"
  - da_id: "DA-28"
    chosen_reading: "IPO capital-structure discontinuity — new-issue step or preferred-stock conversion; tested on the equity rollforward's linkbase children. Read together with the queued generalisation to BASIS discontinuity (A3), which fires where the capital structure is discontinuous across a transaction rather than across an IPO."
  - da_id: "DA-29"
    chosen_reading: "defective checks — every reconciliation term must be NAMED and located in the source; a back-solve closes exactly and so cannot be caught on the closure, only on the terms. `computed` is not a derivation and `reported` is not definitionally the filed value."
  - da_id: "DA-30"
    chosen_reading: "a basis the platform collapses before an artifact sees it; the artifact must NAME the basis and state where the basis was established, PRIOR to any use"
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM
citations:
  - figure: "Income statement: Total revenue 225,237 / 216,906 / 444,294 / 431,784; Total operating expenses 191,229 / 166,648 / 359,573 / 321,138; Operating income 34,008 / 50,258 / 84,721 / 110,646; Interest expense, net (19,246) / (22,752) / (38,612) / (44,576); Other expense, net (448) / (871) / (642) / (2,556); Total other expense, net (19,694) / (23,623) / (39,254) / (47,132); Loss on equity method investments (1,510) / (860) / (2,242) / (1,508); Income tax expense (3,125) / (3,807) / (11,952) / (9,626); Net income 9,679 / 21,968 / 31,273 / 52,380"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 5
    url: https://agentii.ai/v/IRDM/sec191/5
    located_via: read_source_pages
  - figure: "Balance sheet: Cash and cash equivalents 184,214 / 96,501; Additional paid-in capital 864,367 / 880,643; Common stock, $0.001 par value 106 / 105; Accumulated deficit (387,281) / (418,554); Accumulated other comprehensive income (loss), net of tax (4,681) / 406; Total stockholders' equity 472,511 / 462,600; Total liabilities and stockholders' equity 2,565,093 / 2,531,009"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 4
    url: https://agentii.ai/v/IRDM/sec191/4
    located_via: read_source_pages
  - figure: "Cash-flow statement: Net cash used in investing activities (51,791) / (45,256); Net cash used in financing activities (46,951) / (162,608); Payments to acquire property and equipment (51,791); net change in cash and cash equivalents 87,713 for the six months ended June 30, 2026"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 7
    url: https://agentii.ai/v/IRDM/sec191/7
    located_via: read_source_pages
  - figure: "MD&A cash-flow table, first two columns: Cash used in investing activities $ (51,791) $ (45,256); Cash used in financing activities $ (46,951) $ (162,608)"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 34
    url: https://agentii.ai/v/IRDM/sec191/34
    located_via: read_source_pages
  - figure: "Note 12 Related Party: Aireon Holdings equity-method carrying value $36.3M at June 30, 2026 and $38.5M at December 31, 2025; fully diluted ownership approximately 39.5%; purchase agreement May 13, 2026; transaction consummated July 2, 2026"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 18
    url: https://agentii.ai/v/IRDM/sec191/18
    located_via: read_source_pages
  - figure: "Subsequent event: agreement to acquire the remaining 60.5% of Aireon Holdings for approximately $366.7M, 50% cash and 50% deferred as a seller loan payable one year following closing; consolidation of Aireon's $154.7M term loans; $183.4M one-year non-interest-bearing seller loan; $100.0M drawn on the Revolving Facility on July 1, 2026"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 20
    url: https://agentii.ai/v/IRDM/sec191/20
    located_via: read_source_pages
  - figure: "MD&A overview: 2,627,000 billable subscribers at June 30, 2026, an increase of 144,000 or 6% from 2,483,000 at June 30, 2025; 66 operational satellites (MD&A prose, not a table row)"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 21
    url: https://agentii.ai/v/IRDM/sec191/21
    located_via: read_source_pages
  - figure: "Results-of-operations table: Total other expense, net (19,694) and (23,623); Total revenue 225,237 and 216,906 for the three months ended June 30, 2026 and 2025"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 24
    url: https://agentii.ai/v/IRDM/sec191/24
    located_via: read_source_pages
  - figure: "ARPU definition footnote — average revenue per subscriber is computed as revenue divided by the average of the beginning and end of period billable subscribers, divided by the number of months in the period. Prose footnote; the numeric ARPU table on the page is not relied on in this artifact."
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 25
    url: https://agentii.ai/v/IRDM/sec191/25
    located_via: read_source_pages
  - figure: "Annual income statement face: Total revenue 871,659 / 830,682 / 790,723; Total operating expenses 635,679 / 630,298 / 709,095; Operating income 235,980 / 200,384 / 81,628; Interest expense, net (88,252) / (91,134) / (90,387); Other income (expense), net (2,915) / 534 / 4,012; Total other expense (91,167) / (90,600) / (86,375); Income (loss) before income taxes and equity in net earnings of affiliates 144,813 / 109,784 / (4,747); Income tax (expense) benefit (27,618) / (12,259) / 26,251; Gain (loss) on equity method investments (2,823) / 15,251 / (6,089); Net income 114,372 / 112,776 / 15,415; Net income per share basic $1.07 / $0.95 / $0.12; diluted $1.06 / $0.94 / $0.12"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 64
    url: https://agentii.ai/v/IRDM/sec151/64
    located_via: read_source_pages
  - figure: "Income tax components table: Total current tax expense 5,451 / 5,699 / 5,577; Total deferred tax expense (benefit) 22,167 / 6,560 / (31,828); Total income tax expense (benefit) $ 27,618 / $ 12,259 / $ (26,251); Total income (loss) before income taxes 144,813 / 109,784 / (4,747)"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 85
    url: https://agentii.ai/v/IRDM/sec151/85
    located_via: read_source_pages
  - figure: "MD&A: 'For the year ended December 31, 2025, our loss on equity method investments was $2.8 million, compared to a gain of $15.3 million in the prior year. The change is primarily the result of the acquisition of Satelles in 2024, upon which we recorded a $19.8 million gain on our pre-acquisition equity method investment in Satelles'"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 55
    url: https://agentii.ai/v/IRDM/sec151/55
    located_via: read_source_pages
  - figure: "Q2 2022 10-Q earnings-per-share note: Net income (loss) 4,557 / 3,833 / 7,381 / (1,350); Weighted average common shares basic 128,351 / 133,367 / 129,355 / 134,215; diluted 129,611 / 134,981 / 130,811 / 134,215; Net income (loss) per share basic and diluted $ 0.04 / $ 0.03 / $ 0.06 / $ (0.01)"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec176
    page_no: 17
    url: https://agentii.ai/v/IRDM/sec176/17
    located_via: read_source_pages
key_metrics:
  concept_series_stripped: 12
  statements_affected: 4
  weight_discriminator_facts_checked: 38

---

# IRDM — recent-quarter methodology

**Scope.** Iridium Communications Inc. (CIK 0001418819, NASDAQ). Verdict on the six Data-Integrity
Register defects DA-23…DA-28, a fact-level census of DA-23, the standing component identity, an
explicit DA-29 term-location audit, DA-30 basis naming, and the queued cross-holding check.

**Why this issuer.** IRDM is in 001's universe at 5% and 001 cleared its DA-23 row — `GOOG, IRDM, VRT,
UTHR, NVDA | positive | positive | no (5/5)`. That verdict is **REFUTED** below, and not vacuously:
**twelve concept-series in this issuer's filings carry confirmed `|x|` strips**, spread across all four
statements, while **two concepts in the same filings are demonstrably served correctly**, so the
positives that 001 counted as evidence of health are the product of a test that cannot fail.

**Verdict up front.** **AWAY from DEMONSTRATED.** 001's IRDM *arithmetic* is correct — every figure it
quotes reproduces exactly against the filed cells (§12). Its *data-integrity clearance* is not: the
5/5-positive test is the exact shape MSFT falsified, and at IRDM it is not merely vacuous but
contradicted by twelve concept-series in the same accessions (§3).

---

## 1. Component identity, in-line, for every period read

The contract's `data_integrity_register_applied` rule admits either the `gross profit − opex`
derivation **or** the gross-profit bound where the component identity is unavailable. **IRDM files no
gross-profit line at all** — the face runs `Total revenue` straight to `Total operating expenses`, and
the only two arcs into `OperatingIncomeLoss` are revenue at **+1** and `CostsAndExpenses` at **−1**
(§2). So the bound is invoked, and the issuer's own two-line face identity is shown with actual filed
values:

| Period | Total revenue | − Total operating expenses | = Operating income | Residual |
|---|---:|---:|---:|---:|
| Q2 2026 (3M) | 225,237 | 191,229 | 34,008 | 0 |
| Q2 2025 (3M) | 216,906 | 166,648 | 50,258 | 0 |
| H1 2026 (6M) | 444,294 | 359,573 | 84,721 | 0 |
| H1 2025 (6M) | 431,784 | 321,138 | 110,646 | 0 |
| FY2025 | 871,659 | 635,679 | 235,980 | 0 |
| FY2024 | 830,682 | 630,298 | 200,384 | 0 |
| FY2023 | 790,723 | 709,095 | 81,628 | 0 |

All fourteen values are filed cells, read from [IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5) and
[IRDM 10-K p.64](https://agentii.ai/v/IRDM/sec151/64). **Zero residual in all seven periods.**

**Second level, all seven periods** (also zero residual, the same two pages):

```
Q2 2026  51,314 + 13,478 + 5,530 + 67,044 + 53,863 = 191,229  ✓
FY2025  197,577 + 50,426 + 19,758 + 157,711 + 210,207 = 635,679  ✓
FY2024  178,140 + 52,427 + 28,422 + 168,182 + 203,127 = 630,298  ✓
FY2023  158,710 + 66,410 + 20,269 + 143,706 + 320,000 = 709,095  ✓
```

**Third level, Q2 2026 revenue:** `161,328 + 20,767 + 43,142 = 225,237` ✓ — three filed service lines.
**Cash bridge, H1 2026** ([IRDM 10-Q p.7](https://agentii.ai/v/IRDM/sec191/7)):
`185,762 − 51,791 − 46,951 + 693 = 87,713` ✓, and 87,713 is the filed cash-change row.

The operating figure is therefore **filed, not derived**, and it is a **first-class consolidated
subtotal**, not a segment or a component (35 `OperatingIncomeLoss` facts). §3's strips do **not** touch
it. This is why the honest disposition for IRDM is neither "clean" nor "the headline is wrong": the
income statement is intact and the cash-flow and balance-sheet facts are not.

---

## 2. The calculation linkbase — every arc, and the two arcs that are missing

Read from the XBRL calculation linkbase for accession `0001418819-26-000045` (Q2 2026 10-Q). The weight
below is the arc weight of the concept **into its parent**, and it is recorded for **all 22 concepts
judged** in this artifact — the discriminant in §4 is meaningless without it.

**Income-statement role (14 arcs):**

| Concept | Parent | Weight |
|---|---|---:|
| `RevenueFromContractWithCustomerExcludingAssessedTax` | `OperatingIncomeLoss` | **+1** |
| `CostsAndExpenses` | `OperatingIncomeLoss` | **−1** |
| `CostOfGoodsAndServicesSold` | `CostsAndExpenses` | +1 |
| `ResearchAndDevelopmentExpense` | `CostsAndExpenses` | +1 |
| `SellingGeneralAndAdministrativeExpense` | `CostsAndExpenses` | +1 |
| `DepreciationDepletionAndAmortization` | `CostsAndExpenses` | +1 |
| `InterestIncomeExpenseNet` | `NonoperatingIncomeExpense` | **+1** |
| `OtherNonoperatingIncomeExpense` | `NonoperatingIncomeExpense` | **+1** |
| `IncomeLossFromEquityMethodInvestments` | `NetIncomeLoss` | **+1** |
| `IncomeLossFromContinuingOperationsBeforeIncomeTaxes…EquityMethodInvestments` | `NetIncomeLoss` | **+1** |
| `IncomeTaxExpenseBenefit` | `NetIncomeLoss` | **−1** |
| `NetIncomeLoss` | `ComprehensiveIncomeNetOfTax` | +1 |
| FX translation | `ComprehensiveIncomeNetOfTax` | +1 |
| `irdm_UnrealizedGainLossOnCashFlowHedgesNetOfTax` | `ComprehensiveIncomeNetOfTax` | +1 |

**Cash-flow role:** the period-change row
(`CashCashEquivalents…PeriodIncreaseDecreaseIncludingExchangeRateEffect`) ← operating **+1**, investing
**+1**, financing **+1**, FX **+1**. Investing ← `PaymentsToAcquirePropertyPlantAndEquipment` **−1**.
Financing ← short-term-debt proceeds **+1**, `ProceedsFromLinesOfCredit` **+1**,
`PaymentsForRepurchaseOfCommonStock` **−1**, `ProceedsFromStockOptionsExercised` **+1**,
`PaymentsRelatedToTaxWithholdingForShareBasedCompensation` **−1**, `PaymentsOfDividendsCommonStock`
**−1**. Operating ← 15 arcs including `ShareBasedCompensation` **+1**, `NetIncomeLoss` **+1**,
`DepreciationDepletionAndAmortization` **+1** (its **second** parent), and
**`IncomeLossFromEquityMethodInvestments` −1** — the same concept that enters `NetIncomeLoss` at +1.

**Balance-sheet role:** `StockholdersEquity` ← `CommonStockValue` **+1**,
`AdditionalPaidInCapitalCommonStock` **+1**, `RetainedEarningsAccumulatedDeficit` **+1**,
`AccumulatedOtherComprehensiveIncomeLossNetOfTax` **+1**.

### ★ Linkbase arc omission — a validator-completeness finding

**`OperatingIncomeLoss` and `NonoperatingIncomeExpense` never appear as a `child` anywhere in the
linkbase.** The pretax chain is disconnected: the platform cannot derive
`IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` from the operating chain, and **the one arc
that would have exposed the `NonoperatingIncomeExpense` strip is exactly the arc that is absent.**

`validate_calculation("0001418819-26-000045")` returned **16 rows — 6 pass / 2 warn / 8 fail — so the
validator DID run.** IRDM is therefore **not** a wholesale `UNVALIDATED-BY-PLATFORM` case (contrast
VRT, where the same call returned zero rows for a concept that *is* filed). The correct disposition is
a narrowly-scoped, **named** sub-kind — **PARTIALLY-VALIDATED-BY-PLATFORM (linkbase arc omission)** —
which belongs to the queued `UNVALIDATED-BY-PLATFORM` class (A5) rather than fragmenting the register
into a new one.

**Recorded as `UNVALIDATED-BY-PLATFORM`, not as a pass:** the two concepts whose arcs are missing are
precisely the two the validator structurally cannot check.

---

## 3. DA-23 census — fact level, with the weight recorded for each concept

`|x|` stripping is per-fact. The census below is scoped by **statement**, because the defect is not
confined to one (§3.3 is the reason).

### 3.1 Income statement

| Concept | Period | Filed cell | Served | Weight | Verdict |
|---|---|---|---:|---:|---|
| `NonoperatingIncomeExpense` | Q2 2026 | **(19,694)** | +19,694,000 | **+1** | **STRIPPED** |
| `NonoperatingIncomeExpense` | H1 2026 | **(39,254)** | +39,254,000 | +1 | **STRIPPED** |
| `OtherNonoperatingIncomeExpense` | Q2 2026 | **(448)** | +448,000 | **+1** | **STRIPPED** |
| `OtherNonoperatingIncomeExpense` | H1 2026 | **(642)** | +642,000 | +1 | **STRIPPED** |
| `OtherNonoperatingIncomeExpense` | FY2025 | **(2,915)** | +2,915,000 | +1 | **STRIPPED** |
| `OtherNonoperatingIncomeExpense` | FY2024 | **534** | +534,000 | +1 | **CORRECT** |
| `OtherNonoperatingIncomeExpense` | FY2023 | **4,012** | +4,012,000 | +1 | **CORRECT** |
| `InterestIncomeExpenseNet` | Q2 2026 | **(19,246)** | +19,246,000 | **+1** | **STRIPPED** |
| `InterestIncomeExpenseNet` | H1 2026 | **(38,612)** | +38,612,000 | +1 | **STRIPPED** |
| `InterestIncomeExpenseNet` | FY2025 | **(88,252)** | +88,252,000 | +1 | **STRIPPED** |
| `InterestIncomeExpenseNet` | FY2024 | **(91,134)** | +91,134,000 | +1 | **STRIPPED** |
| `InterestIncomeExpenseNet` | FY2023 | **(90,387)** | +90,387,000 | +1 | **STRIPPED** |
| `IncomeLossFromEquityMethodInvestments` | Q2 2026 | **(1,510)** | +1,510,000 | **+1** | **STRIPPED** |
| `IncomeLossFromEquityMethodInvestments` | H1 2026 | **(2,242)** | +2,242,000 | +1 | **STRIPPED** |
| `IncomeLossFromEquityMethodInvestments` | FY2025 | **(2,823)** | +2,823,000 | +1 | **STRIPPED** |
| `IncomeLossFromEquityMethodInvestments` | FY2023 | **(6,089)** | +6,089,000 | +1 | **STRIPPED** |
| `IncomeLossFromEquityMethodInvestments` | FY2024 | **15,251** | +15,251,000 | +1 | **CORRECT** |
| `IncomeLossFromContinuingOperationsBefore…EquityMethodInvestments` | FY2023 | **(4,747)** | +4,747,000 | **+1** | **STRIPPED** |
| `IncomeTaxExpenseBenefit` | FY2023 | **−26,251** (element value — see §6) | +26,251,000 | **−1** | **STRIPPED** |
| `OperatingIncomeLoss` | 35 facts, all periods | all positive | all positive | never a child | **UNEXERCISED** |
| `RevenueFromContractWithCustomerExcludingAssessedTax` | periods read | no filed negative | positive | **+1** | **UNEXERCISED** |
| `CostsAndExpenses` | periods read | no filed negative | positive | **−1** | **UNEXERCISED** |

`InterestIncomeExpenseNet` is the extreme case: **35 of 35 served facts are positive and not one is
negative.** The subtree closes exactly on the platform's own terms — `19,246 + 448 = 19,694` — so
**the platform's consistency test certifies a uniformly sign-inverted subtree.**

### 3.2 Cash-flow statement — the `diff = 2 × value` fingerprint

| Concept | Period | Filed cell | Served | Weight | Verdict |
|---|---|---|---:|---:|---|
| `NetCashProvidedByUsedInInvestingActivities` | H1 2026 | **(51,791)** | +51,791,000 | **+1** | **STRIPPED** |
| `NetCashProvidedByUsedInInvestingActivities` | H1 2025 | **(45,256)** | +45,256,000 | +1 | **STRIPPED** |
| `NetCashProvidedByUsedInFinancingActivities` | H1 2026 | **(46,951)** | +46,951,000 | **+1** | **STRIPPED** |
| `NetCashProvidedByUsedInFinancingActivities` | H1 2025 | **(162,608)** | +162,608,000 | +1 | **STRIPPED** |
| `CashCashEquivalents…PeriodIncreaseDecreaseIncludingExchangeRateEffect` | Q2 2026 | 87,713 | served 87,713; **computed** 285,197 | **+1** | **STRIPPED (children)** |
| `PaymentsToAcquirePropertyPlantAndEquipment` | 24 facts, all periods | all parenthesised outflows | all **positive** | **−1** | **CORRECT 24/24** |

The `NetCashProvidedByUsedInFinancingActivities` series is **24 facts with zero negatives served.**
The period-change row closes the arithmetic: `285,197 − 87,713 = 197,484 = 2 × 98,742 = 2 × (51,791 +
46,951)` — **the strip fingerprint is exactly twice the sum of the two stripped subtotals.**

### 3.3 ★ Balance sheet — the both-directions control, in two cells of one row

| Concept | Period | Filed cell | Served | Weight | Verdict |
|---|---|---|---:|---:|---|
| `RetainedEarningsAccumulatedDeficit` | 2026-06-30 | **(387,281)** | +387,281,000 | **+1** | **STRIPPED** |
| `RetainedEarningsAccumulatedDeficit` | 2025-12-31 | **(418,554)** | +418,554,000 | **+1** | **STRIPPED** |
| `RetainedEarningsAccumulatedDeficit` | 2026-03-31 | (deficit, label-proven) | +396,960,000 | +1 | **STRIPPED** |
| `AccumulatedOtherComprehensiveIncomeLossNetOfTax` | 2026-06-30 | **(4,681)** | +4,681,000 | **+1** | **STRIPPED** |
| `AccumulatedOtherComprehensiveIncomeLossNetOfTax` | 2025-12-31 | **406** | +406,000 | **+1** | **CORRECT** |

**This is the strongest single piece of DA-23 evidence in the thesis series.** On one row of one filed
table — `Accumulated other comprehensive income (loss), net of tax | (4,681) | 406`
([IRDM 10-Q p.4](https://agentii.ai/v/IRDM/sec191/4)) — two adjacent columns carry one negative and one
positive filed value. The platform serves **+4,681,000** and **+406,000**. It strips the negative and
preserves the positive. **The control that 001's test lacked is a single row of a filing.**

**Balance-sheet strips proven by exact roll-forward** (each closes to the cent against the served
`NetIncomeLoss`, which is itself correct — see §5):

```
2025-12-31 (418,554)  + FY2025 net income 114,372  →  (304,182)  … and 2025-09-30 (443,419) + Q4 24,865 = (418,554) ✓
2026-03-31 (418,554)  + Q1 2026 net income  21,594 →  (396,960)  ✓
2026-06-30 (396,960)  + Q2 2026 net income   9,679 →  (387,281)  ✓
```

All three close exactly. **Two of the three are additionally proven by the filed cell itself.**
`RetainedEarningsAccumulatedDeficit` is served positive in **20 of 20 facts** spanning 2020-12-31 to
2026-06-30 — the monotone draw-down-then-rebuild curve (275,915 → 21,011 → 443,419 → 387,281) is the
signature of a *deficit* magnitude, and the label on the filed face is literally **"Accumulated
deficit"**. The remaining seventeen are graded **DERIVED** (label + curve + roll-forward), not
cell-proven.

**Equity fingerprint:** `StockholdersEquity` children are all **+1**, so `computed = 106 + 864,367 +
387,281 + 4,681 = 1,256,435` while `as filed = 106 + 864,367 − 387,281 − 4,681 = 472,511`.
`1,256,435 − 472,511 = 783,924 = 2 × 391,962 = 2 × (387,281 + 4,681)` — **EXACT.**

### 3.4 Per-share block — a live INVERSION, reported separately from the strips

Per-share is the most-stripped class at this issuer: **19 confirmed strips across 3 concepts and 7
accessions, with zero negative per-share facts served across ~90 records** (33 diluted + 57 basic).
Positive controls — Q2 2021 `$0.03` and Q2 2022 `$0.04` — are served correctly.

**One of these is an inversion, not a strip,** and it has a verbatim cell citation. From the Q2 2022
10-Q per-share note ([IRDM 10-Q p.17](https://agentii.ai/v/IRDM/sec176/17)), for 3M 2022 / 3M 2021 /
6M 2022 / 6M 2021:

```
| Net income (loss)                     | $ 4,557 | $ 3,833 | 7,381 | (1,350) |
| Weighted average common shares - basic| 128,351 | 133,367 | 129,355 | 134,215 |
| Weighted average common shares - dil. | 129,611 | 134,981 | 130,811 | 134,215 |
| Net income (loss) per share - b. & d. | $ 0.04  | $ 0.03  | $ 0.06 | $ (0.01) |
```

The served `EarningsPerShareBasic` for the six months ended 2021-06-30 is **+0.01**; the filed cell is
**$ (0.01)**. Two independent rows of the same table corroborate the sign: the numerator is
**(1,350)**, and the same page states *"Due to the Company's net loss position for the six months
ended June 30, 2021, all potential common stock equivalents were anti-dilutive."*

This is the **MRCY shape** — filed `$(x)` served `+x` — reproduced live at a third issuer, and unlike
MRCY's +0.25/+0.38 it is a *negative-to-positive* flip on a loss-making period, which is the more
dangerous direction because the served value reads as a profitable quarter.

### 3.5 Census summary

**12 concept-series carry confirmed strips, spanning four statements** — income statement
(`NonoperatingIncomeExpense`, `OtherNonoperatingIncomeExpense`, `InterestIncomeExpenseNet`,
`IncomeLossFromEquityMethodInvestments`, `IncomeTaxExpenseBenefit`,
`IncomeLossFromContinuingOperationsBefore…`), cash flow (investing and financing subtotals), balance
sheet (`RetainedEarningsAccumulatedDeficit`, `AccumulatedOtherComprehensiveIncomeLossNetOfTax`), and
the per-share block. **The strip is not confined to the income statement; and per §4, neither is the
test that finds it.**

**`UNEXERCISED` is reported distinctly from `CLEAN`.** `OperatingIncomeLoss` (35 facts, all positive),
`RevenueFromContractWithCustomerExcludingAssessedTax` and `CostsAndExpenses` had **no negative filed
value in any period read**. The sign channel was never exercised on them, which is **untested, not
passed**. This is precisely why 001's `positive | positive | no (5/5)` row is inadmissible: **the test
is restricted to the population on which the defect cannot be observed.**

---

## 4. ★ The weight discriminator — replicated, and bounded

**The MSFT rule:** a concept entering its parent at **weight −1** carries a positive magnitude
legitimately; at **weight +1** with a parenthesised filed cell it is **STRIPPED**.

**Replication at IRDM, two periods, same statement, same filed number:**

| Concept | Period | Filed | Served | Weight | Verdict |
|---|---|---:|---:|---:|---|
| `PaymentsToAcquirePropertyPlantAndEquipment` | H1 2026 | (51,791) | +51,791,000 | **−1** | **CORRECT** |
| `NetCashProvidedByUsedInInvestingActivities` | H1 2026 | (51,791) | +51,791,000 | **+1** | **STRIPPED** |
| `PaymentsToAcquirePropertyPlantAndEquipment` | H1 2025 | (45,256) | +45,256,000 | **−1** | **CORRECT** |
| `NetCashProvidedByUsedInInvestingActivities` | H1 2025 | (45,256) | +45,256,000 | **+1** | **STRIPPED** |

**Same number, same period, same statement, same parentheses on the page. The verdict differs and the
weight is the only difference.** Without the weight, a detector would report 24 stripped capex facts
that are all correct. The rule earns its place.

### ★ The bound — the same weight yields opposite verdicts

| Concept | Weight | Filed | Served | Verdict |
|---|---:|---:|---:|---|
| `PaymentsToAcquirePropertyPlantAndEquipment` | **−1** | (51,791) | +51,791,000 | **CORRECT** |
| `IncomeTaxExpenseBenefit` (FY2023) | **−1** | −26,251 | +26,251,000 | **STRIPPED** |
| `IncomeLossFromEquityMethodInvestments` | **+1** *and* **−1** | (2,242) / +2,242 | +2,242,000 | **correct for one parent, wrong for the other** |

**Weight −1 carries three concepts and three different verdicts.** The MSFT rule is therefore
**necessary but not sufficient**, and IRDM bounds it:

> **The completing test is unidirectionality.** A concept that is a *gross flow of a single direction
> by definition* — capex is always an outflow, and the element's sign is fixed — has its sign absorbed
> by the arc weight, so a positive served magnitude is the platform's normal encoding and **correct**.
> A concept that is *bidirectional by definition* — net income/loss, gain/loss, expense/benefit,
> earnings/deficit, comprehensive income/loss, increase/decrease — **carries its sign as substance, and
> no weight in the filing can restore it.**

Arithmetically: for a unidirectional element the served magnitude equals `|filed|` and the weight
supplies the sign, so a sign test on it is **vacuous by construction**; for a bidirectional element the
served magnitude equals `|filed|` **only if stripped**.

**Corollary — the admissible form of a DA-23 clearance.** Detection is possible **only** on
bidirectional concepts, so any clearance must (i) be scoped to bidirectional concepts, (ii) exhibit at
least one *negative-filed* instance, and (iii) record the arc weight so that a unidirectional positive
is `CORRECT` rather than an unexamined pass. **A clearance that cannot state a single negative-filed
instance is `UNEXERCISED`.** 001's IRDM row fails all three.

`IncomeLossFromEquityMethodInvestments` is the bidirectional case in its purest form and is a **DA-30**
instance as well as a DA-23 one: **one concept, two parents, opposite weights, one served number.** The
filed income-statement value is `(2,242)`; the filed cash-flow add-back value is `+2,242`; the platform
serves `+2,242,000` for both. There is no weight it could have chosen that makes the served value right
for both parents.

---

## 5. Validator behaviour — three shapes, and one that certifies a corrupted value

**(a) The inverse row shape.** For `NetCashProvidedByUsedInInvestingActivities` the validator's
**`computed` = −51,791,000 (the FILED sign)** while **`reported` = +51,791,000 (the STRIPPED value)**.
This is the **inverse** of MSFT §2.5, where `computed` was the garbage column and `reported` held the
filed sign. **"Trust `computed`" does not generalise** — the two columns swap roles within one corpus.

**(b) A PASS certified on a sign-inverted fact — the most dangerous shape.**
`NonoperatingIncomeExpense` Q2 2026: `computed` **19,694,000** against `reported` **19,694,000** —
**PASS**, on a subtree that is inverted twice over: `NonoperatingIncomeExpense` is itself stripped, and
so are both of its children (`InterestIncomeExpenseNet` −19,246 and `OtherNonoperatingIncomeExpense`
−448, which sum to the stripped 19,694). **The instrument is silent on a corrupted value**, and because
the value *is* the subtotal, no downstream check can recover the sign.

**(c) A subtotal served correctly while its children are stripped.**
`NetIncomeLoss` Q2 2026 is served **+9,679,000 = the filed 9,679**, even though three of its children
are stripped. The platform's own `computed` for the same cell is **12,699,000** = `14,314 + 1,510 −
3,125`, against the filed `14,314 − 1,510 − 3,125 = 9,679`. **Fingerprint: `12,699 − 9,679 = 3,020 =
2 × 1,510`** — exact. Same at Q2 2025: `2 × 860 = 1,720` exact. Same at FY2023: the served
`NetIncomeLoss` is **+15,415,000 = the filed 15,415**, while the platform's children imply
`4,747 + 6,089 − 26,251 = −15,415` — **the negative of the filed value.**

**Therefore the propagation rule is not uniform**: `NetIncomeLoss` (70+ facts, appears on every
statement) is served from the filed subtotal and survives its stripped children; `NonoperatingIncomeExpense`
is served stripped although it is itself a subtotal. **A census scoped to subtotals cannot predict the
sign any better than a census scoped to one statement.** This is the second axis of the MSFT
statement-level finding and it is why §3 is scoped by statement *and* by concept directionality.

**DA-29 discipline applied to this section.** `computed` is **not** cited anywhere in this artifact as
a derivation of any figure; it is cited only as *evidence about the platform*, and every figure asserted
is reconciled to the **statement face** — the filed cells of p.4, p.5, p.7, p.64 and p.85. That
distinction is load-bearing here: on the balance sheet, `reported` for `StockholdersEquity` is not
definitionally the filed value, and I did not establish which of 472,511 or 1,256,435 the platform
serves. **The strip is proven at the level of the individual child facts, where both children carry
filed parentheses and both arcs are +1; whether a given served *subtotal* is contaminated must be
tested per concept, because §5(c) shows it can go either way.**

---

## 6. DA-30 — every competing basis, NAMED, and where it was established

**Basis 1 — the FY2023 income-tax figure is filed on two sign conventions inside one document.**
The income statement face ([IRDM 10-K p.64](https://agentii.ai/v/IRDM/sec151/64)) prints
`Income tax (expense) benefit | (27,618) | (12,259) | 26251` — FY2023 **unparenthesised, positive** —
under a **negated label** ("(expense) benefit"). The tax note
([IRDM 10-K p.85](https://agentii.ai/v/IRDM/sec151/85)) prints
`Total income tax expense (benefit) | $ 27,618 | $ 12,259 | $ (26,251)` — the **same fact, opposite
visual sign**. Neither is an error: one is a negated-label presentation of the credit.

**The closure settles it, and only the closure settles it.** FY2023 as filed:
`−4,747 + (−6,089) − (−26,251) = 15,415` = the filed FY2023 net income ✓. The alternative
(`−4,747 + 26,251 − 6,089` treating the tax as an expense) gives −37,087 ✗. So the **element value is
−26,251** and the served **+26,251,000 is STRIPPED**. **A reader who checked `reported` against the
statement face would conclude the platform is correct; a reader who checked it against the note would
conclude it is wrong; both would be discharging DA-29 on an ambiguous term.** This is the case the
register's `reported is not definitionally the filed value` corollary exists for.

**Basis 2 — `IncomeLossFromEquityMethodInvestments` is filed on two bases.** Income-statement basis:
`(2,242)` (H1 2026), `(2,823)` (FY2025). Cash-flow add-back basis: `+2,242`, entering operating cash
flow at **−1**, corroborated by MD&A prose — *"our loss on equity method investments was $2.8 million"*
([IRDM 10-K p.55](https://agentii.ai/v/IRDM/sec151/55)). **Established in the calculation linkbase**: the
concept has two parents with **opposite weights**.

**Basis 3 — capex, three bases.** Cash paid `51,791` (cash-flow statement); property and equipment
received but not yet paid `7,921` ⇒ `59,712` accrual basis; plus capitalised stock-based compensation
`2,073`. Three defensible bases; the platform serves the cash-paid basis. **Named here before use in
§3.2.**

**Basis 4 — P11 basis discontinuity (the queued A3 generalisation, and it fires without an IPO).**
The Q2 2026 balance sheet is **`standalone_pre_merger`** *and* **pre-Aireon-consolidation**: the RKLB
merger was signed 2026-06-28 with completion expected mid-2027, and the Aireon closing
(2026-07-02) falls **four days after** the balance-sheet date, adding the `$183.4M` seller loan,
`$154.7M` of consolidated Aireon term loans and a `$100.0M` revolver draw
([IRDM 10-Q p.20](https://agentii.ai/v/IRDM/sec191/20)). **Any IRDM figure read from the Q2 2026 10-Q
is pre-close on both transactions**, and no single basis-flag exists for it.

---

## 7. DA-29 — term location for every reconciliation presented

The mechanical circularity test is applied to each: **if any term appears nowhere in the source, the
check is a back-solve.**

| Reconciliation | Terms | Location |
|---|---|---|
| Q2 2026 opex, second level | 51,314 / 13,478 / 5,530 / 67,044 / 53,863 | filed, p.5 — all five present |
| Q2 2026 revenue, third level | 161,328 / 20,767 / 43,142 | filed, p.5 — all three present |
| H1 2026 cash bridge | 185,762 / 51,791 / 46,951 / 693 → 87,713 | filed, p.7 — all four present |
| FY2023 net income, three terms | −4,747 / −6,089 / −26,251 → 15,415 | filed, p.64 **and** p.85 — all three present |
| FY2024 / FY2025 net income | 109,784 / 12,259 / 15,251 / 112,776 · 144,813 / 27,618 / 2,823 / 114,372 | filed, p.64 — all present |
| Equity fingerprint | 106 / 864,367 / 387,281 / 4,681 → 472,511 | filed, p.4 — all four present |

**No term in any reconciliation in this artifact appears nowhere in the source, and no term was taken
from `computed`.** No back-solve is present. The one figure in this artifact that is **DERIVED** rather
than DEMONSTRATED (§10, the Aireon remeasurement order-of-magnitude) is labelled as such **at the point
of use**, and every one of its terms is located — see §10.

---

## 8. Six-DA census

| DA | Verdict | Evidence |
|---|---|---|
| **DA-23** | **CONFIRMED** | 12 concept-series; 4 statements; weights recorded for all 22 concepts judged. Two both-directions controls in one filed row (§3.3) and one filed table (§3.1). `UNEXERCISED` on `OperatingIncomeLoss`, revenue and `CostsAndExpenses`. |
| **DA-24** | **REFUTED** | Discharged from the full arc set, both directions. The arcs into `OperatingIncomeLoss` are **exactly two** — revenue **+1**, `CostsAndExpenses` **−1** — and into `NetIncomeLoss` **exactly three** — equity-method **+1**, pretax **+1**, tax **−1**. **No disposal/sale-gain arc exists.** Corroborated by exact closure at three levels in all seven periods read. |
| **DA-25** | **NOT TESTABLE — ingestion absence of a DATUM CLASS** | The definition **is** filed ([IRDM 10-Q p.25](https://agentii.ai/v/IRDM/sec191/25): revenue ÷ average of beginning- and end-of-period billable subscribers ÷ months), so the register's issuer-level defect does **not** apply. The metric is nonetheless **not reproducible from the served fact set** because subscriber counts appear only as MD&A prose ([IRDM 10-Q p.21](https://agentii.ai/v/IRDM/sec191/21): *2,627,000 at June 30, 2026 vs 2,483,000*, +144,000 or 6%) and are **never XBRL-tagged** — so no period returns zero facts; the query returns zero **by construction**. This is a **third kind**, distinct from a period returning 0 facts. |
| **DA-26** | **CONFIRMED — twice** | The metrics block's Q4-2025 row carries revenue **871,659** and operating income **235,980**, which are **exactly the filed FY2025 annual cells** ([IRDM 10-K p.64](https://agentii.ai/v/IRDM/sec151/64)); the Q4-2024 row carries **830,682 / 200,384**, exactly the filed FY2024 annuals. The filed quarterly figures derived from the served series are 212,940 and 55,249 for Q4 2025 ⇒ **ratios 4.094× and 4.271×**; 212,991 and 52,115 for Q4 2024 ⇒ **3.900× and 3.845×**. (Ratios DERIVED from served facts; the annual and the row values are cell-DEMONSTRATED.) |
| **DA-27** | **does not fire** | `fiscal_year_end_month: 12`, source `gold_companies` — **populated AND correct**; labels exact. Per the queued A6 caution: this confirms the mechanism on a member of the population it predicts and carries **no** information about the remainder. The source discriminator (populated-but-incorrect registry field) is the material case and it is **not** present here. |
| **DA-28** | **NOT TESTABLE — coverage-window kind** | IRDM's SEC coverage window **opens 2022-02-17** (FY2021 10-K, `sec147`); the IPO is outside it. **Not** an absence of facts and **not** a validator gap — a boundary of the corpus, stated with a date. |
| **DA-32** (queued) | **does not fire** | WASO: 35 facts, all between 105M and 135M, declining from ~135M (2021) to 106,648 (H1 2026). No 1000× anomaly. |

**Not-testable kinds, named and never merged.** This artifact exhibits **two** of the three kinds and is
explicit that the third is absent by *finding*, not by oversight. (i) **Ingestion absence** — **cannot be
exhibited at IRDM at all**: FY2023 facts sourced from `irdm-20231231.htm` are served, so that accession
is demonstrably ingested; see §9. (ii) **Genuine absence from the source** — DA-28's IPO, an event
outside the corpus window. (iii) **Validator completeness** — the **linkbase arc omission** of §2, the
one kind present here.

---

## 9. What could NOT be verified — and why

**★ `processing_status` is NON-DISCRIMINATING, and this corrects the task brief's own parenthetical.**
All **9** accessions inspected return **`"pending"`** — *including* `sec191`, whose 40 pages are served,
whose facts are queryable, and whose `validate_calculation` returned 16 rows. It is therefore **not an
ingestion-absence marker** and must not be used as one. `sec149` (FY2023 10-K) is also `pending` while
`NetIncomeLoss` FY2023 **is served from `irdm-20231231.htm`** — that accession's own file. The correct
test remains "does the query return rows," which is itself subject to the compound-filter trap
(`RevenueFromContractWithCustomerExcludingAssessedTax` with `fiscal_year=2026` returns **3** facts;
unfiltered it returns **35** — *silence is not absence*).

**Recorded as `unresolvable: true`, class `UNRESOLVABLE-FROM-PLATFORM`,** on two items:
1. **Ingestion completeness is unreportable at this issuer.** No accession at IRDM returns a status
   distinguishing ingested from un-ingested, so no platform-internal test can establish whether a
   datum's absence is a corpus boundary or a pipeline failure.
2. **The FY2021 10-K annual per-share table page is not locatable.** `search_keyword_in_source` on
   `sec147` for *net loss per share* returned 5 candidate pages (87, 70, 61, 60, 55) **all with
   `description: null` and empty `keywords`** — the tool cannot discriminate among them, and naming one
   would be a guess. **A guessed page number is worse than no link because it looks correct**, so no
   citation is offered for that instance; the live inversion in §3.4 rests on a page that *was* located.

**Also not established, and stated as a limit rather than a finding:** whether the platform *serves*
`StockholdersEquity` at the filed 472,511 or at the double-counted 1,256,435. The concept query returned
text-block and `LiabilitiesAndStockholdersEquity` concepts rather than the numeric fact, and §5(c)
establishes that served subtotals can go either way, so I will not infer it. **The strip is proven where
the evidence is: at the two child facts, both with filed parentheses and both at weight +1.**

---

## 10. Cross-holding check (queued as DA-31) — IRDM carries a material stake, and has already run this play

**It carries one.** Aireon Holdings: equity-method carrying value **$36.3M** at 2026-06-30, fully diluted
ownership **approximately 39.5%**, from a $50.0M investment in June 2022 for ~6% preferred with prior
investments written down to zero ([IRDM 10-Q p.18](https://agentii.ai/v/IRDM/sec191/18)). The mark is
currently **NEGATIVE** — a $2,242 thousand loss in H1 2026, a $2,823 thousand loss in FY2025.

**And the mechanism is not hypothetical at this issuer — it is in its own filing history.** On acquiring
Satelles in 2024, IRDM **recorded a $19.8 million gain on its pre-acquisition equity method investment
in Satelles** ([IRDM 10-K p.55](https://agentii.ai/v/IRDM/sec151/55)) — which is why FY2024's
equity-method line is a **$15.3M gain** against FY2025's $2.8M loss. That is:
- **the MSFT mechanism** (a remeasurement on a stake, recognised through earnings), **not appreciation** —
  the MSFT correction was that a stake's mark need not move with its market value;
- **larger than MSFT's instance**: $19.8M on FY2024 net income of $112,776 = **17.6%**, against MSFT's
  3.71%;
- **and on the BUY side**: the gain arises as the stake is *consumed* by control purchase, the mirror of
  MSFT's dilution gain as the stake *fell*.

**The queued instance.** The Aireon step acquisition — remaining **60.5%** for approximately
**$366.7M**, 50% cash and 50% deferred, **closed 2026-07-02**, four days after the balance-sheet date
([IRDM 10-Q p.20](https://agentii.ai/v/IRDM/sec191/20)) — queues the identical mechanism for Q3 2026,
on the 39.5% stake carried at $36.3M.

**Graded DERIVED, explicitly, at the point of use — order-of-magnitude only.** A pro-rata illustration
`366.7 ÷ 0.605 × 0.395 ≈ $239.4M` implies a remeasurement gain on the order of `239.4 − 36.3 ≈ $203M`,
which would be **~2.1× H1 2026 net income ($31.3M)** and **~5.6× H1 2026 operating income ($84.7M)**.
**Every term is located** (366.7 and 60.5% at p.20; 36.3 at p.18; 39.5% at p.18 and p.20), so this is
**not** a back-solve — but **the fair value of the retained stake is not filed**, a control-stake price
may overstate the per-point value of a non-controlling interest, and the gain is therefore
**DERIVED, not DEMONSTRATED**. It is stated as an order of magnitude and used for no other purpose.

---

## 11. Correction to 001

**001's IRDM arithmetic is CORRECT.** Every figure it quotes reproduces exactly against the filed
cells: "reported operating income ($34.0M positive) is correct — verified by component" ⇒ Q2 2026
`225,237 − 191,229 = 34,008` ✓; "operating margin fell from 23.2% to 15.1%" ⇒ `50,258 ÷ 216,906 =
23.17%` and `34,008 ÷ 225,237 = 15.10%` ✓; "down 8.1 pts YoY" ✓; "revenue grew 3.8%" ⇒
`225,237 ÷ 216,906 − 1 = +3.84%` ✓. **Nothing in 001 is rewritten — 001 is frozen, and its IRDM
figures stand.**

**001's DA-23 clearance is REFUTED, and not vacuously.** Its row `GOOG, IRDM, VRT, UTHR, NVDA |
positive | positive | no (5/5)` clears IRDM because the served values are positive. But (i) the test is
restricted to the population on which `|x|` stripping is unobservable — MSFT's falsification, reproduced
here; (ii) at IRDM it is **contradicted in the same accessions**: 12 concept-series carry confirmed
strips, including four concepts in the Q2 2026 10-Q that 001's own quarter reads; (iii) the two
positives-in-both-columns that 001 counted are the exact shape of `NonoperatingIncomeExpense`, where
**the validator also passes**; and (iv) §4 supplies the control 001 lacked — two adjacent cells of one
row, one stripped and one preserved.

**Does this move 001's headline toward or away from DEMONSTRATED? AWAY.** 001's IRDM *conclusion* — a
15.1% operating margin, down 8.1 points on 3.8% revenue growth — is **correct as filed and now
independently re-derived from the cells**; the operating subtotal is a filed first-class consolidated
subtotal and is not among the stripped concepts. But the artifact that supported it **certified the
issuer's data integrity with a test that cannot fail**, so the *evidence grade* of 001's clearance claim
falls: IRDM moves from "validated, positive, 5/5" to **"headline correct; sign channel demonstrably
corrupted in 12 concept-series; validator passes at least one inverted subtree."** A reader who took
001's DA-23 row as assurance about IRDM's served facts has been misled in the direction of confidence,
and the correct grade for that row is **WITHHELD, not CLEAN**.

---

## Sources

> Every figure asserted above resolves to the page cited. Each page was read with
> `read_source_pages`; no page number in this artifact is a guess, and no table page is quoted
> through the platform's LLM-generated `read_source_outline` description field.

| Figure | Source |
|---|---|
| Income statement: revenue 225,237 / 216,906 / 444,294 / 431,784; opex 191,229 / 166,648 / 359,573 / 321,138; operating income 34,008 / 50,258 / 84,721 / 110,646; interest (19,246) / (22,752) / (38,612) / (44,576); other expense (448) / (871) / (642) / (2,556); total other expense (19,694) / (23,623) / (39,254) / (47,132); equity method (1,510) / (860) / (2,242) / (1,508); tax (3,125) / (3,807) / (11,952) / (9,626); net income 9,679 / 21,968 / 31,273 / 52,380 | [📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5) |
| Balance sheet: cash 184,214 / 96,501; APIC 864,367 / 880,643; common stock 106 / 105; **accumulated deficit (387,281) / (418,554)**; **AOCI (4,681) / 406**; total stockholders' equity 472,511 / 462,600; total liabilities and equity 2,565,093 / 2,531,009 | [📄 IRDM 10-Q p.4](https://agentii.ai/v/IRDM/sec191/4) |
| Cash-flow: investing (51,791) / (45,256); financing (46,951) / (162,608); capex (51,791); cash change 87,713 | [📄 IRDM 10-Q p.7](https://agentii.ai/v/IRDM/sec191/7) |
| MD&A cash-flow table: Cash used in investing $ (51,791) $ (45,256); Cash used in financing $ (46,951) $ (162,608) | [📄 IRDM 10-Q p.34](https://agentii.ai/v/IRDM/sec191/34) |
| Note 12: Aireon carrying value $36.3M / $38.5M; ~39.5% fully diluted; agreement May 13, 2026; consummated July 2, 2026 | [📄 IRDM 10-Q p.18](https://agentii.ai/v/IRDM/sec191/18) |
| Subsequent event: remaining 60.5% of Aireon for ~$366.7M, 50% cash / 50% deferred; $154.7M term loans; $183.4M seller loan; $100.0M revolver drawn | [📄 IRDM 10-Q p.20](https://agentii.ai/v/IRDM/sec191/20) |
| MD&A overview: 2,627,000 billable subscribers at June 30, 2026 vs 2,483,000, +144,000 or 6%; 66 operational satellites | [📄 IRDM 10-Q p.21](https://agentii.ai/v/IRDM/sec191/21) |
| Results-of-operations table: Total other expense, net (19,694) / (23,623); Total revenue 225,237 / 216,906 | [📄 IRDM 10-Q p.24](https://agentii.ai/v/IRDM/sec191/24) |
| ARPU definition footnote — revenue ÷ average of beginning and end of period billable subscribers ÷ months (prose; the numeric ARPU table is not relied on) | [📄 IRDM 10-Q p.25](https://agentii.ai/v/IRDM/sec191/25) |
| Annual income statement face: revenue 871,659 / 830,682 / 790,723; opex 635,679 / 630,298 / 709,095; operating income 235,980 / 200,384 / 81,628; interest (88,252) / (91,134) / (90,387); other income (expense) (2,915) / 534 / 4,012; total other expense (91,167) / (90,600) / (86,375); pretax 144,813 / 109,784 / (4,747); tax (27,618) / (12,259) / 26,251; equity method (2,823) / 15,251 / (6,089); net income 114,372 / 112,776 / 15,415; EPS basic $1.07 / $0.95 / $0.12, diluted $1.06 / $0.94 / $0.12 | [📄 IRDM 10-K p.64](https://agentii.ai/v/IRDM/sec151/64) |
| Income tax components: current 5,451 / 5,699 / 5,577; deferred 22,167 / 6,560 / (31,828); **Total income tax expense (benefit) $ 27,618 / $ 12,259 / $ (26,251)**; pretax income 144,813 / 109,784 / (4,747) | [📄 IRDM 10-K p.85](https://agentii.ai/v/IRDM/sec151/85) |
| MD&A: "$2.8 million, compared to a gain of $15.3 million … the acquisition of Satelles in 2024, upon which we recorded a $19.8 million gain on our pre-acquisition equity method investment in Satelles" | [📄 IRDM 10-K p.55](https://agentii.ai/v/IRDM/sec151/55) |
| Q2 2022 EPS note: net income (loss) 4,557 / 3,833 / 7,381 / **(1,350)**; WASO basic 128,351 / 133,367 / 129,355 / 134,215; diluted 129,611 / 134,981 / 130,811 / 134,215; **per share $ 0.04 / $ 0.03 / $ 0.06 / $ (0.01)** | [📄 IRDM 10-Q p.17](https://agentii.ai/v/IRDM/sec176/17) |
