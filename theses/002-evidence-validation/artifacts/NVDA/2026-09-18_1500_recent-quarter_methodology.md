---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: NVDA
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
# Written at 1.4.0. The 1.5.0 bump (DA-29 defective CHECKS, DA-30 collapsed basis) post-dates
# this artifact's pin; per contracts/artifact-frontmatter.yaml `pins_match_thesis`
# (accepted_constitution_pins: ["1.4.0", "1.5.0"]) an artifact is valid at the pin it RECORDS.
# This artifact nevertheless FINDS a DA-30-class instance (see §12) and applies the DA-29
# rule to every reconciliation below; those obligations are discharged in the Phase 7
# validation ledger, per the 1.3.0 precedent.
constitution_pin: "1.4.0"
assumption_pin: "2"
# Not resolvable at this layer. The platform carries no skill-hash field for this skill on any
# surface reachable with the permitted tools, and 001's `e6b41dbb2426` is a 001-era pin that
# must not be copied forward into 002 (copying it would assert a pin the platform never served
# to this skill). Left explicitly UNRESOLVED rather than guessed or borrowed.
skill_pin: "07d26b9c738b"  # Q57 resolved 2026-09-18: re-derived from plugins/agent-plugins/agentii-equity-agent/skills/agentii/recent-quarter AND plugins/vertical-plugins/equity-research-core/skills/agentii/recent-quarter — two independent roots AGREE. Algorithm dispatch.skill_version_hash() (scripts/dispatch.py:132) validated 9/9 against the six pins tabled in theses/001-technology-baseline/reproduce.md. Four packaging/targets trees FAIL 0/6 and are decoys. Supersedes the UNRESOLVED gap recorded at first write.
as_of: 2026-09-18
# No corpus version is exposed by any permitted tool. The four freshness stamps reachable
# DISAGREE with each other (list_sources/search_documents 2026-08-21; get_company_financials
# 2026-08-25; get_company_fiscal_calendar 2026-08-26; search_xbrl_facts and
# get_calculation_tree 2027-04-12 — the last of which is seven months in the FUTURE of
# `as_of`). A corpus version cannot be honestly asserted from these.
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "|x| absolute-value stripping; per-FACT not per-period; concept-agnostic on *CashProvidedByUsedIn*. NVDA: income-statement series has zero negatives (test has no power); cash-flow series IS stripped. 001's 'clean' holds only vacuously for the sign question."
  - da_id: "DA-24"
    chosen_reading: "disposal gain entering above the operating subtotal — tested by arc count into OperatingIncomeLoss; NVDA has exactly two arcs and is refuted"
  - da_id: "DA-25"
    chosen_reading: "issuer-defined per-unit metric not reproducible from segment tables; no such metric on the pages read"
  - da_id: "DA-26"
    chosen_reading: "annual mislabelled as quarterly; NVDA exhibits it in 3 of 3 Q4 rows, quantified against the filing's own Q4 cells"
  - da_id: "DA-27"
    chosen_reading: "calendar-derived fiscal labels; NVDA exhibits it with a 100% hit rate (11 of 11 rows) plus a platform self-contradiction, and the register's source=='default' detector mis-fires for a third issuer"
  - da_id: "DA-28"
    chosen_reading: "capital-structure discontinuity. Not applicable as an IPO (NVDA IPO'd 1999, not a deal security). A THIRD sub-mechanism is exhibited in the served series (10-for-1 split, un-restated per-share base) and is recorded as an adjacent candidate, not as DA-28."
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: "Operating income 53,536 / 21,638 (consolidated); Revenue 81,615 / 44,062; Cost of revenue 20,458; Gross profit 61,157; R&D 6,321; SG&A 1,300; Total operating expenses 7,621; Net income 58,321"
    ticker: NVDA
    form_type: 10-Q
    citation_id: sec173
    page_no: 3
    url: https://agentii.ai/v/NVDA/sec173/3
    located_via: read_source_pages
  - figure: "AFS net change in unrealized gain (loss) (78) / 139; Other comprehensive income (loss), net of tax (41) / 158; Total comprehensive income 58,280"
    ticker: NVDA
    form_type: 10-Q
    citation_id: sec173
    page_no: 4
    url: https://agentii.ai/v/NVDA/sec173/4
    located_via: read_source_pages
  - figure: "Total current assets 150,995; Total assets 259,474; Short-term debt 1,000; Long-term debt 7,470; Total liabilities 64,000; Common stock 24; APIC 10,275; Retained earnings 185,038; Total shareholders' equity 195,474"
    ticker: NVDA
    form_type: 10-Q
    citation_id: sec173
    page_no: 5
    url: https://agentii.ai/v/NVDA/sec173/5
    located_via: read_source_pages
  - figure: "Balances Apr 26, 2026 (24,221 sh / $24 / 10,275 / 137 / 185,038 / 195,474); Other comprehensive loss (41); SBC 1,928; Shares repurchased (108) sh / (20,013)"
    ticker: NVDA
    form_type: 10-Q
    citation_id: sec173
    page_no: 6
    url: https://agentii.ai/v/NVDA/sec173/6
    located_via: read_source_pages
  - figure: "Net cash provided by operating activities 50,344 / 27,414; (Gains) losses from equity securities, net (15,936); SBC 1,928; D&A 997; Deferred income taxes 1,584; Purchases related to PP&E (1,757); Net cash used in investing activities (26,429); Net cash used in financing activities (21,283); Change in cash 2,632"
    ticker: NVDA
    form_type: 10-Q
    citation_id: sec173
    page_no: 7
    url: https://agentii.ai/v/NVDA/sec173/7
    located_via: read_source_pages
  - figure: "Segment operating income: C&N 53,335, Graphics 2,941, Total 56,276 (comparative 22,054 / 1,640 / 23,694); segment D&A C&N 526, Graphics 194; Other segment items footnote (1)"
    ticker: NVDA
    form_type: 10-Q
    citation_id: sec173
    page_no: 19
    url: https://agentii.ai/v/NVDA/sec173/19
    located_via: read_source_pages
  - figure: "Reconciliation: Segment operating income 56,276 − SBC (1,928) − Unallocated operating expenses (565) − Acquisition-related and other costs (247) = 53,536; comparative 23,694 − (1,474) − (419) − (163) = 21,638"
    ticker: NVDA
    form_type: 10-Q
    citation_id: sec173
    page_no: 20
    url: https://agentii.ai/v/NVDA/sec173/20
    located_via: read_source_pages
  - figure: "First Quarter FY2027 Summary: Revenue 81,615 / 68,127 / 44,062; Gross margin 74.9% / 75.0% / 60.5%; Operating income 53,536 / 44,299 / 21,638; Net income per diluted share 2.39 / 1.76 / 0.76"
    ticker: NVDA
    form_type: 10-Q
    citation_id: sec173
    page_no: 24
    url: https://agentii.ai/v/NVDA/sec173/24
    located_via: read_source_pages
  - figure: "Results of Operations % of revenue: Gross profit 74.9 / 60.5; Total operating expenses 9.3 / 11.5; Operating income 65.6 / 49.0; Net income 71.5% / 42.6%. Operating Income by Reportable Segments: C&N 53,335, Graphics 2,941, Total 56,276"
    ticker: NVDA
    form_type: 10-Q
    citation_id: sec173
    page_no: 26
    url: https://agentii.ai/v/NVDA/sec173/26
    located_via: read_source_pages
  - figure: "Item 1 Business — 'In 2024, we launched the NVIDIA Blackwell architecture – connecting 36 Grace CPUs and 72 Blackwell GPUs in a data center scale, liquid-cooled design'; no space product line, no rad-hard variant, no orbital SKU on the page"
    ticker: NVDA
    form_type: 10-K
    citation_id: sec169
    page_no: 4
    url: https://agentii.ai/v/NVDA/sec169/4
    located_via: read_source_pages
  - figure: "Q&A, Antoine Chkaiban (New Street Research) — 'space data centers'; Jensen Huang — 'the economics are poor today'; 'Liquid cooling is obviously out of the question because it's kind of — it's heavy and freezes'; 'NVIDIA is already the world's first GPU in space, Hopper is in space'; orbital use case stated as imaging/inference and edge data reduction"
    ticker: NVDA
    form_type: earnings_call_transcript
    citation_id: ect80
    page_no: 4
    url: https://agentii.ai/v/NVDA/ect80/4
    located_via: read_source_pages
key_metrics:
  operating_income_facts_nonnegative: 69
  segment_substitution_error_pct: 5.12
  computed_column_error_x: 37

---

# NVDA — Recent-Quarter Defect Census, Q1 FY2027

Source: Forms 10-Q / 10-K / 8-K, and the 2026-02-25 earnings-call transcript. Most recent
filed quarter: **period ended 2026-04-26 = Q1 FY2027** (10-Q accession `0001045810-26-000052`,
filed 2026-05-20, retrieval `sec173`). Prior-year-end 10-K: accession `0001045810-26-000021`,
filed 2026-02-25, retrieval `sec169`.

**Every figure in this artifact is a cell read off a page with `read_source_pages`.** No
platform `description` field is quoted anywhere, and no sentence *about* a table is offered as
evidence. Where a value is a served XBRL fact rather than a printed cell, it is named as such
and its `dimensions` are given.

---

## Summary of verdicts

| DA | Test | NVDA verdict | Where |
|---|---|---|---|
| **DA-23** | `\|x\|` stripping, per-FACT | **PRESENT** — on the cash-flow class. Income-statement class is clean but **vacuously** so | §1 |
| **DA-24** | disposal gain above the operating subtotal | **REFUTED** — exactly two arcs into `OperatingIncomeLoss` | §4 |
| **DA-25** | issuer-defined per-unit metric not reproducible from segments | **NOT EXHIBITED** (scope-limited to pages read) | §5 |
| **DA-26** | annual mislabelled as quarterly | **PRESENT** — 3 of 3 Q4 rows, verified against the filing's own Q4 cells | §6 |
| **DA-27** | calendar-derived fiscal labels | **PRESENT** — 11 of 11 rows off by one, plus a platform self-contradiction | §7 |
| **DA-28** | capital-structure discontinuity | **NOT APPLICABLE as IPO**; adjacent split sub-mechanism recorded | §8 |
| *DA-30-class* | one concept, two bases, no basis field | **PRESENT** — segment total vs consolidated under one concept | §12 |

**001's "NVDA clean" verdict on DA-23 stands only for the sign question, and only because the
question is empty.** The register as a whole is **incomplete** for NVDA. A DA-23-only detector
passes NVDA and is wrong. See §10.

---

## 1. DA-23 — per period, per fact

### 1a. The income-statement class has zero negatives, so the sign test has no power

Served fact counts for the concepts DA-23 is specified against, NVDA, 2014–2026:
`OperatingIncomeLoss` 69, `NetIncomeLoss` 89, `EarningsPerShareDiluted` 78, `GrossProfit` 78,
`OperatingExpenses` 69 — **every served value is non-negative**, and every one of the ~25
issuer-periods I checked by hand satisfies the component identity exactly (residual 0):

| Period | Gross profit | − Operating expenses | = Operating income | Filing cell |
|---|---|---|---|---|
| Q1 FY2027 (2026-04-26) | 61,157 | 7,621 | **53,536** | [📄 sec173 p.3](https://agentii.ai/v/NVDA/sec173/3) |
| Q1 FY2026 (2025-04-27) | 26,668 | 5,030 | **21,638** | [📄 sec173 p.3](https://agentii.ai/v/NVDA/sec173/3) |
| Q4 FY2026 (2026-01-25) | 51,093 | 6,794 | **44,299** | [📄 sec173 p.24](https://agentii.ai/v/NVDA/sec173/24) |

The Q4 FY2026 row is DA-29-compliant: every term is located. Gross profit 51,093 is derived as
FY2026 GP 153,463 minus 9-month FY2026 GP 102,370 (both served 12-month/9-month durations);
operating expenses 6,794 and operating income 44,299 are printed cells on
[📄 sec173 p.24](https://agentii.ai/v/NVDA/sec173/24); and 51,093 − 6,794 = 44,299 closes.

**Consequence: a sign test on these concepts cannot detect anything at NVDA.** There are no
negative values to strip. This is the DA-23 analogue of the margin-conditioned detector power in
Rule 3, and it is the mechanical reason a DA-23-only detector passes NVDA: not because NVDA is
clean, but because the test is empty there.

### 1b. The cash-flow class is where the negatives are — and they are stripped

Reading only the `computed` vs `reported` pair through the component identity, for the quarter
ended 2026-04-26:

| Concept | Instrument `computed` | Instrument `reported` | Filing cell (sec173 p.7) | Verdict |
|---|---|---|---|---|
| `NetCashProvidedByUsedInInvestingActivities` | — | **+26,429,000,000** | **(26,429)** | **STRIPPED** |
| `NetCashProvidedByUsedInFinancingActivities` | — | **+21,283,000,000** | **(21,283)** | **STRIPPED** |
| `NetCashProvidedByUsedInInvestingActivities` (comparative, 2025-04-27) | — | **+5,216,000,000** | **(5,216)** | **STRIPPED** |

Every one of these is a served fact whose sign is the **absolute value** of the printed cell.
[📄 sec173 p.7](https://agentii.ai/v/NVDA/sec173/7) prints `Net cash used in investing
activities (26,429)` and `Net cash used in financing activities (21,283)`.

**Negatives survive elsewhere in the same filing and the same series** — the operating section's
`(15,936)` gain on equity securities is served correctly signed, and p.4's `(78)` and `(41)` are
served negative. **So the strip is per-FACT, not per-period and not per-concept**: the HAWK rule
demonstrated positively on a third issuer.

### 1c. Four arithmetic proofs that the strip corrupted the instrument's own arithmetic

The strip is not cosmetic. It changes the instrument's answers, and in two of the four cases
below it corrupts the **`computed`** column rather than the `reported` column — i.e. **both
columns can be wrong at once**, per the instrument rule.

| # | Concept | `computed` | `reported` | True value | Proof |
|---|---|---|---|---|---|
| 1 | `CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect` | **98,056** | 2,632 | **2,632** | 98,056 = 50,344 + **26,429** + **21,283**; diff 95,424 = 2 × 47,712 where 47,712 = 26,429 + 21,283 |
| 2 | `NonoperatingIncomeExpense` (comparative 2025-04-27) | **632** | 272 | **272** | 632 = 515 − 63 + \|−180\|; diff 360 = 2 × 180. Here `reported` is right and **`computed` is wrong** |
| 3 | `OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent` | **115** | 41 | **−41** | 115 = \|−78\| + 37; the true value is −41 per [📄 p.4](https://agentii.ai/v/NVDA/sec173/4) and [📄 p.6](https://agentii.ai/v/NVDA/sec173/6), and `reported` 41 is its magnitude |
| 4 | `ComprehensiveIncomeNetOfTax` | **58,362** | 58,280 | **58,280** | 58,362 = 58,321 + 41; diff 82 = 2 × 41. The instrument used **two mutually inconsistent OCI values in one period** |

Proof 1 is the decisive one: the instrument summed **98,056** for the change in cash where the
filing prints **2,632** ([📄 sec173 p.7](https://agentii.ai/v/NVDA/sec173/7)). An artifact that
trusted `computed` here would overstate NVDA's cash build by **95,424M** — a 37× error.

### 1d. Verdict

**DA-23 is PRESENT at NVDA.** It is invisible to the income-statement concepts (no negatives),
visible and severe in the cash-flow concepts, and per-fact in both directions.

---

## 2. The instrument measured

Seven failure modes are registered. NVDA instantiates five of them:

| Mode | NVDA instance |
|---|---|
| (1) 93% false-positive on `fail` | Not separately re-measured here; no `fail` row was load-bearing for any verdict above |
| (2) `pass` does not certify a sign | `AvailableForSaleDebtSecuritiesAmortizedCostBasis` = 2,009 is `pass` while the sibling `AvailableForSaleSecuritiesDebtSecurities` row is unreconciled (§11.8) |
| (3) `reported` corrupted — **and can be a SEGMENT TOTAL** | **NVDA is the instance** (§3). Both periods. Also corrupted on the comparative |
| (4) NO ROW for a concept with seven arcs into it | The unit/split discontinuity (§11.6) is a silent absence of restatement, not a row |
| (5) `reported` sign-stripped | §1b — three investing/financing facts |
| (6) `computed` wrong | §1c proofs 2, 3, 4; plus `GrossProfit` computed −19,168 (§11.5) |
| (7) period collapse | `validate_calculation` returns **one row per period-end date** and cannot run the every-period rule at all; the DA-26 Q4 collapse (§6) is the data-layer form |

**Component identity is the only detector that names the correct sign here**, and it is the only
reason the segment-total substitution is visible: without `gross profit − total operating
expenses`, the `reported` 56,276 is a plausible-looking number with no internal contradiction.
`EPS × shares` was not used anywhere in this artifact and is inadmissible.

---

## 3. The mechanism — segment total substituted for consolidated, in three roles

### 3a. The flagship: `OperatingIncomeLoss`

`validate_calculation` for the Q1 FY2027 10-Q returns:

```
us-gaap:OperatingIncomeLoss | Apr 26 2026 | computed 53,536,000,000 | reported 56,276,000,000 | diff +2,740,000,000
```

Both facts exist in the store for **the same concept, the same period (2026-01-26 →
2026-04-26), the same unit, and at `is_primary: true`** — they differ **only** in the
`srt:ConsolidationItemsAxis` dimension:

| Served fact | Value | `dimensions` |
|---|---|---|
| Consolidated | **53,536,000,000** | `{}` |
| Segment total | **56,276,000,000** | `{srt:ConsolidationItemsAxis: us-gaap:OperatingSegmentsMember}` |
| Segment total (second copy) | **56,276,000,000** | `{srt:ConsolidationItemsAxis: us-gaap:CorporateNonSegmentMember}` |

The instrument's `reported` selected the dimensioned fact. **The consolidated fact exists, is
un-dimensioned, is `is_primary: true`, and is 53,536 — which is the cell printed on
[📄 sec173 p.3](https://agentii.ai/v/NVDA/sec173/3) and again on
[📄 sec173 p.24](https://agentii.ai/v/NVDA/sec173/24).**

The same selection error occurs on the **comparative** period:

| Period | Consolidated (served, `dimensions: {}`) | Segment total (served, dimensioned) | `reported` | Error |
|---|---|---|---|---|
| Q1 FY2027 | **53,536,000,000** | 56,276,000,000 | 56,276,000,000 | **+2,740M (+5.12%)** |
| Q1 FY2026 | **21,638,000,000** | 23,694,000,000 | 23,694,000,000 | **+2,056M (+9.50%)** |
| FY2026 (annual) | **130,387,000,000** | 139,297,000,000 | — | **+8,910M (+6.83%)** |

The annual row is included because the same two-basis pair exists there, but I did **not**
observe the annual error in a `reported` column: `get_company_financials` served the
**consolidated** 130,387 for period_end 2026-01-25. **The defect is therefore not uniform across
endpoints** — the quarterly path in `validate_calculation` took the segment total; the annual
path in `get_company_financials` did not. I state the pair's existence and the observed error,
not a general rule about which endpoint fails.

### 3b. Why this concept and not revenue

`Revenues` is served on **four bases** for Q1 FY2027, and all of them reconcile to the
consolidated figure:

| Basis | Cells | Sum |
|---|---|---|
| Consolidated | 81,615,000,000 (`dimensions: {}`) | — |
| Geography | US 63,769 / Taiwan 12,006 / China 4,550 / Other 1,290 | **81,615** ✓ |
| Market platform | Data Center 75,246 / Edge Computing 6,369 | **81,615** ✓ |
| Segment | C&N 74,550 / Graphics 7,065 / Total 81,615 | **81,615** ✓ |

**All revenue is allocated to segments, so the segment total equals the consolidated total and
the substitution is harmless. Unallocated items — SBC, unallocated opex, acquisition costs — are
NOT allocated, so for `OperatingIncomeLoss` the segment total is larger than the consolidated
figure and the substitution is wrong.** That is the general rule this instance establishes:

> The segment-total-for-consolidated substitution is **silent for any concept with no
> unallocated reconciling items, and produces an overstatement for any concept that has them.**

[📄 sec173 p.20](https://agentii.ai/v/NVDA/sec173/20) supplies the wedge to the dollar, and every
term is a printed cell:

```
Q1 FY2027:  56,276 − 1,928 − 565 − 247 = 53,536   ✓
Q1 FY2026:  23,694 − 1,474 − 419 − 163 = 21,638   ✓
```

`56,276 − 53,536 = 2,740 = 1,928 (SBC) + 565 (unallocated operating expenses) + 247
(acquisition-related and other costs)`. **The instrument's `reported` for `OperatingIncomeLoss`
is the p.19/p.26 segment Total row** ([📄 sec173 p.19](https://agentii.ai/v/NVDA/sec173/19),
[📄 sec173 p.26](https://agentii.ai/v/NVDA/sec173/26)).

### 3c. Two further instances of the same wrapper

**Instance 2 — `GrossProfit`, `computed` = −19,168.** `CostOfRevenue` is served correctly and
positively (20,458,000,000, matching the p.3 cell). A `Revenues` fact **exists** as
1,290,000,000 for exactly this period with `dimensions: {srt:StatementGeographicalAxis:
nvda:OtherCountriesMember}` — the "Other" cell of the geographic table. And:

```
1,290 − 20,458 = −19,168   ✓ exactly the instrument's computed value
```

A **dimensional child fact won over the consolidated child fact** inside the `GrossProfit` role.
Note the structural point: `GrossProfit` itself has **zero dimensional facts** — the corruption
entered through a child, so it cannot be found by inspecting the parent's dimensions.

**Instance 3 — `NetCashProvidedByUsedInOperatingActivities`, `computed` = 49,873.** The role's 12
children sum exactly to the filing's `reported` 50,344 using the p.7 cells
(58,321 + 1,928 + 1,584 + 997 − 15,936 − 94 − 2,243 − 4,420 − 983 + 2,210 + 7,763 + 1,217 =
**50,344** ✓). The instrument's `computed` is short by exactly **471**, and:

```
997 (consolidated D&A, p.7) − 526 (C&N segment D&A, p.19) = 471   ✓
50,344 − 471 = 49,873   ✓ exactly the instrument's computed value
```

The term **526,000,000 is a served, `is_primary: true` fact** for this period with
`dimensions: {us-gaap:StatementBusinessSegmentsAxis: nvda:ComputeAndNetworkingSegmentMember}`,
and it is printed on [📄 sec173 p.19](https://agentii.ai/v/NVDA/sec173/19). I verified four of
the twelve children individually against the filing's cells (net income 58,321; SBC 1,928;
deferred income taxes 1,584; D&A 997; accrued liabilities 7,763; prepaid and other assets 983 —
all correct), which eliminates them as the source.

**Declared status of instances 2 and 3:** the *substitution* is inferred from an exact residual
against a term that **is present in the source** — so these are not DA-29 back-solves (a
back-solve's fatal property is a term that appears nowhere in the source and closes anyway). But
I did not directly observe the instrument select 526 or 1,290. They are recorded as
**mechanism-identified, selection-inferred**, with the exact arithmetic, for the Phase 7 ledger.

---

## 4. DA-24 — REFUTED

`us-gaap:OperatingIncomeLoss` has exactly **two** arcs in the consolidated role
(`CondensedConsolidatedStatementsofIncome`): `GrossProfit` weight **+1** and `OperatingExpenses`
weight **−1**. Nothing else enters above the operating subtotal, so no disposal gain can be
sitting in it — the cleanest possible form of this test. A second role
(`SegmentInformationScheduleofReconcilingItemsDetails`) binds the same concept as the **+1 first
addend** before three −1 children, which is the DA-30 structure discussed in §12 and is **not** a
DA-24 finding.

**Caveat carried:** `get_calculation_tree` returned a **stitched multi-era role set** — labels
reading "Common Stock; 45,000 shares authorized; 14,824 shares issued and outstanding at December
31, 2014", lease years 2021–2024, intangible years 2015–2018 — while its metadata asserts
`fiscal_year: 2026, fiscal_period: Q1`. The two-arc result above comes from the role named for
the condensed consolidated statements of income in the returned set, but the vintage mixing means
the arc **count** should be re-confirmed against a single-era tree before it is treated as
settled. Recorded as a tool limitation (§Could not be verified).

---

## 5. DA-25 — NOT EXHIBITED

Scope-limited to the pages read. The segment note on
[📄 sec173 p.19](https://agentii.ai/v/NVDA/sec173/19) reports only Revenue, Other segment items
and Operating income per segment; the tables on
[📄 sec173 p.24](https://agentii.ai/v/NVDA/sec173/24) and
[📄 sec173 p.26](https://agentii.ai/v/NVDA/sec173/26) report revenue, dollar change and percent
change. **No issuer-defined per-unit metric appears on any page read** — no cost-per-token,
per-watt or per-rack figure, which is notable given the call's heavy use of "performance per
watt" and "tokens per watt" as *rhetorical* comparatives (those are qualitative claims in
[📄 ect80 p.4](https://agentii.ai/v/NVDA/ect80/4), not issuer-defined metrics with a stated
denominator). **Absence here is absence-from-the-pages-read, not a clean bill**: I did not read
the full 10-Q.

---

## 6. DA-26 — PRESENT, quantified against the filing's own quarter

Every `Q4` row served by `get_company_financials` carries the issuer's **full-year** figures:

| Platform row | `revenues` | `operating_income` | `net_income` | `eps_diluted` | Filed quarter (sec173 p.24) |
|---|---|---|---|---|---|
| fy 2025 Q4, period_end 2026-01-25 | **215,938** | **130,387** | **120,067** | **4.90** | 68,127 / 44,299 / 42,960 / 1.76 |
| fy 2024 Q4, period_end 2025-01-26 | **130,497** | **81,453** | **72,880** | **2.94** | (FY2025 annual) |
| fy 2023 Q4, period_end 2024-01-28 | **60,922** | **32,972** | **29,760** | **11.93** | (FY2024 annual) |

Each is confirmed as a 12-month duration by the served annual facts (e.g. `Revenues`
215,938,000,000 and `OperatingIncomeLoss` 130,387,000,000 for 2025-01-27 → 2026-01-25; the p.26
geographic block prints "Total revenue $215,938 $130,497 $60,922"). I checked the year-end
quarter's true values against the cells on [📄 sec173 p.24](https://agentii.ai/v/NVDA/sec173/24),
which prints the Q4 FY2026 column: revenue **68,127**, operating expenses **6,794**, operating
income **44,299**, diluted EPS **1.76**.

**The platform's "Q4 FY2026" revenue is 3.17× the true quarter** (215,938 / 68,127) and **its
operating income 2.94×** (130,387 / 44,299). 3 of 3 rows. **The actual Q4 is absent from the
platform entirely for all three years** — not merely mislabelled, but not served.

**The universal claim is falsified; the census stands at 19 of 20 issuers.** FLY shows zero
instances. NVDA is one of the 19.

---

## 7. DA-27 — PRESENT, 100% hit rate, plus a platform self-contradiction

`get_company_fiscal_calendar` returns `fiscal_year_end_month: 2` with
`fiscal_year_end_month_source: "gold_companies"` and `cross_validation_hint: null`.

**The register's detector — keyed on `source == "default"` — mis-fires here.** NVDA's source
field is `gold_companies`. That is now a **third** issuer where the detector is wrong (MRCY and
FLY were the first two). The detector needs to key on the *synthesized-vs-filed* distinction, not
on the literal string `default`.

**Synthesized quarters are month-end-aligned approximations of a 52/53-week calendar.** FY2027 Q1
is synthesized as 2026-03-01 → 2026-05-31; the filed Q1 FY2027 is **2026-01-26 → 2026-04-26**.
The synthesized window **starts 34 days late**, ends 35 days late, and **overlaps the true Q2**.
The calendar also forward-synthesizes FY2027 Q3 and Q4 (2026-09-01 onward) beyond the corpus.

**Every `get_company_financials` row's `fiscal_year` is one less than the filing's own label —
11 of 11.** The platform calls period_end 2026-04-26 "fiscal_year 2026 Q1" while
[📄 sec173 p.24](https://agentii.ai/v/NVDA/sec173/24) heads it **"First Quarter of Fiscal Year
2027"**; it calls 2026-01-25 "fiscal_year 2025 Q4" while that is the FY**2026** year end.

**And the two endpoints contradict each other.** `get_company_fiscal_calendar` labels
2026-04-26 as FY2027 Q1 (correct) while `get_company_financials` calls the same period FY2026 Q1.
Separately, `get_company_financials` places "FY2025 Q4" at period_end 2026-01-25, whereas the
calendar's own FY2025 Q4 is 2024-12-01 → 2025-02-28. **The two surfaces disagree by a full fiscal
year on the same date.** A consumer cannot reconcile them, because neither exposes the basis.

---

## 8. DA-28 — NOT APPLICABLE as an IPO; an adjacent sub-mechanism is present

NVDA IPO'd in 1999, is not a deal security, and shows no IPO capital-structure discontinuity in
the served window. `deal_security_basis: not_applicable`. **Confirmed as instructed.**

**However, a third sub-mechanism of the same *class* (capital-structure discontinuity) is
present and is not in the register.** The served `eps_diluted` / `eps_basic` series mixes two
per-share bases with no restatement marker, across NVDA's **10-for-1 split (effective
2024-06-10)**:

| period_end | `eps_basic` | `eps_diluted` | Base |
|---|---|---|---|
| 2024-01-28 (FY2024 annual) | 12.05 | **11.93** | **PRE-split** |
| 2024-04-28 (Q1 FY2025) | 6.04 | **5.98** | **PRE-split** (filed May 2024, before the split) |
| 2024-07-28 (Q2 FY2025) | 0.68 | **0.67** | post-split |
| 2024-10-27 (Q3 FY2025) | 0.79 | **0.78** | post-split |
| 2025-04-27 onward | — | 0.76 … 4.90 | post-split |

The adjacent rows 2024-04-28 and 2024-07-28 carry **5.98 and 0.67**: a −89% EPS "collapse" that
never happened, produced by a unit change the platform does not mark. This is **DA-28-adjacent**:
the register's DA-28 covers capital-structure discontinuity but registers only two sub-mechanisms
(HAWK new-issue, FLY preferred conversion). Recorded as candidate **N-4**, not as DA-28.

---

## 9. The settled consolidated operating margin

**Settled: 65.60%.** Operating income **$53,536M** ÷ revenue **$81,615M** = **65.595%**.

The filing prints it three independent ways:

1. `Operating income 53,536` — [📄 sec173 p.3](https://agentii.ai/v/NVDA/sec173/3) consolidated
   statement of income, current-quarter column.
2. `Operating income 53,536` — [📄 sec173 p.24](https://agentii.ai/v/NVDA/sec173/24) First
   Quarter FY2027 Summary.
3. **`Operating income 65.6`** — [📄 sec173 p.26](https://agentii.ai/v/NVDA/sec173/26)
   Results of Operations, percentage-of-revenue column. That page also confirms the identity in
   percentage space: gross profit 74.9% − total operating expenses 9.3% = **65.6%** ✓.

**The instrument value that is wrong:** `validate_calculation`'s **`reported`** for
`us-gaap:OperatingIncomeLoss` = **$56,276,000,000**, which is the segment Total row of
[📄 sec173 p.19](https://agentii.ai/v/NVDA/sec173/19) and p.26 — not a filed consolidated figure.

| | Operating income | Margin | Error |
|---|---|---|---|
| **Filed consolidated** | **$53,536M** | **65.60%** | — |
| Instrument `reported` | $56,276M | **68.95%** | **+3.36 points** |
| Error on the figure | **+$2,740M** | | **+5.12%** |

(68.953% − 65.595% = **3.358 pts**. The task brief's "68.96% / 3.4 points" rounds the same facts;
the computed values are 68.95% and 3.36 pts, and the unrounded inflation is 3.358 points.)

**An artifact trusting `reported` prints a 68.95% operating margin for NVDA instead of 65.60% —
a 3.36-point inflation on the largest name in the sector**, with the margin overstated by $2,740M
on a $53,536M base, and the wedge exactly the three unallocated reconciling items.

---

## 10. Corrections to 001

**(a) "DA-23 — NVDA clean" is vacuous, and the register is incomplete for NVDA.** 001's §3
concludes cleanliness from plausibility ("plausible for NVDA and consistent with its gross-profit
structure... Profitable issuer, unaffected by sign-stripping") — a **margin-and-plausibility
argument, not a sign test**, and then extends the rule count to 12 issuer-quarters on the
strength of it. Two corrections:

1. **The verdict is right only for the sign question, and the sign question is empty here.**
   NVDA's income-statement concepts have **zero negative served values** across 2014–2026, so any
   sign test is unevident at NVDA — it can neither pass nor fail. "Clean" should read
   **"not testable on this concept class."**
2. **The register as a whole is incomplete for NVDA.** DA-23 shows the failure is real
   (three stripped cash-flow facts, four corrupted identities, one 37× error on the change in
   cash); DA-26 and DA-27 are both present; and NVDA carries a DA-30-class two-basis collapse
   that 001's structure had no slot for. **001's four DA-23/DA-24/DA-25/DA-26/DA-27/DA-28 slots
   are not a complete defect census of this issuer.**

**(b) "No space product line" is true; "no space exposure" would be FALSE.**

001's exact sentence — *"And it discloses no space product line. No radiation-hardened variant,
no space-qualified SKU, no orbital customer concentration. The H100 that flew on Starcloud-1 was
a terrestrial part in an orbital application"* — is **supported as written** by
[📄 sec169 p.4](https://agentii.ai/v/NVDA/sec169/4), which I read: it names Blackwell, Blackwell
Ultra, CUDA, Tensor Core, Grace, DRIVE/Clara/Omniverse, Nemotron and Cosmos, and contains **no
space product, no rad-hard variant, and no orbital customer**.

**But the narrow claim must not be widened, because NVDA claims the exposure itself, in its own
words, on its own earnings call.** Q&A, 2026-02-25, [📄 ect80 p.4](https://agentii.ai/v/NVDA/ect80/4):

> **Antoine Chkaiban (New Street Research):** "I'd like to ask about **space data centers**, which
> some of your customers are considering. How feasible do you think that is and what kind of
> horizon? And what do the economics look like today?"
>
> **Jen-Hsun Huang:** "Well, **the economics are poor today**, but it's going to improve over
> time. … There's an abundance of energy, but solar panels are large, but there's plenty of space
> in space. The heat dissipation, it's cold in space. However, **there's no airflow**. And so the
> only way to dissipate [heat] is through conduction and the radiators that you need to create are
> fairly large. **Liquid cooling is obviously out of the question because it's kind of — it's
> heavy and freezes.** … **NVIDIA is already the world's first GPU in space, Hopper is in
> space.** And one of the best use cases of GPUs in space is **imaging**, to be able to image at
> extremely high resolutions using, of course, optics and artificial intelligence. … It's hard to
> do that by sending petabytes and petabytes of imaging data back here on earth and doing that
> work. **It's easier just to do it out in space. And then ignore all of the data collected and
> processed until you see something interesting.** And so artificial intelligence in space will
> have very good, very interesting applications."

**Correct form: NVDA flies a terrestrial part into an orbital application and sells no orbital
product.** Its stated orbital thesis is **imaging/inference — edge data reduction, not megawatt
compute** — which is exactly the workload that does *not* need the cooling it says is unavailable.

**Two consequences 001's framing missed:**

1. **The vendor of the constraint states the constraint against itself.** Compare
   [📄 sec169 p.4](https://agentii.ai/v/NVDA/sec169/4) — *"connecting 36 Grace CPUs and 72
   Blackwell GPUs in a data center scale, **liquid-cooled** design"* — with the same CEO on
   [📄 ect80 p.4](https://agentii.ai/v/NVDA/ect80/4): *"**Liquid cooling is obviously out of the
   question** because it's kind of — it's heavy and freezes."* **NVDA's terrestrial flagship
   architecture is defined by the cooling method its CEO says cannot be used in orbit.** That is
   a stronger, self-sourced statement of 001's F2-before-F4 finding than 001 obtained.
2. **"The economics are poor today"** is NVDA's own characterization of orbital compute — an
   independent, adversarial-source confirmation of the thesis's cost-curve premise, from the
   supplier rather than the operator.

**Grade corrected:** the "world's first GPU in space" claim, carried from the brief as
**CLAIMED**, is now **DEMONSTRATED** — located verbatim at
[📄 ect80 p.4](https://agentii.ai/v/NVDA/ect80/4). 001's absent-space-line claim is
**DEMONSTRATED** at [📄 sec169 p.4](https://agentii.ai/v/NVDA/sec169/4). 001's *inference* from
that absence — that NVDA "does not consider it a product category yet" — remains **MODELED**: the
call shows a stated position on the application, and a stated absence of any product SKU, which is
not the same as disinterest.

---

## 11. New register candidates

**N-1. Segment-total-for-consolidated substitution on a two-role concept.** One concept bound in
both a consolidated role and a segment-reconciliation role, with the dimensioned fact taking
precedence. **Three instances at NVDA, all terms located: `OperatingIncomeLoss` (both periods and
the annual), `GrossProfit` computed (via a geographic `Revenues` child), and operating cash flow
computed (via a segment `D&A` child).** Sub-rule established in §3b: silent where nothing is
unallocated, an overstatement where something is. This is the most important candidate here — it
generalizes beyond NVDA to every issuer that discloses unallocated reconciling items.

**N-2. `is_primary: true` is not a basis guard.** For Q1 FY2027, `OperatingIncomeLoss` carries
**two** `is_primary: true` facts for one concept/period/unit that differ only in dimension
(53,536 and 56,276), plus a third copy at 56,276 under `CorporateNonSegmentMember`. A consumer
filtering on `is_primary` gets both and must choose, with no basis field to choose on.

**N-3. Two-column strip.** §1c proofs 2, 3, 4: the sign strip corrupts the **`computed`** column
while `reported` is right, and in proof 4 the instrument uses **two mutually inconsistent OCI
values in one period**. Detection on either column alone is insufficient — which is the
instrument rule, now with NVDA instances.

**N-4. Split-unadjusted per-share series** (§8): pre- and post-split EPS in one unmarked series,
−89% artifact at the boundary.

**N-5. `fiscal_period=FY` is not a duration filter.** `search_xbrl_facts(fiscal_year=2025,
fiscal_period=FY)` returns a **9-month YTD** fact (86,088,000,000 for 2025-01-27 → 2025-10-26),
a 6-month fact (50,078,000,000), two quarterly facts (36,010,000,000; 28,440,000,000), and the
12-month annual (81,453,000,000) — **six durations in one bucket, none labelled by duration.** A
consumer taking "FY" at face value reads a 9-month figure as an annual one. Plausibly an upstream
cause of DA-26 and DA-27.

**N-6. `data_freshness` is not a date of the data.** Four surfaces returned four values at one
instant: 2026-08-21, 2026-08-25, 2026-08-26, and **2027-04-12** — the last **seven months in the
future** of `as_of`. The field a consumer would use to judge whether a quarter is current is
unusable, and a "recent-quarter" artifact cannot establish corpus currency from it.

**N-7. `LongTermDebt` scope collapse.** `reported` = 8,470 = short-term 1,000 + long-term 7,470
([📄 sec173 p.5](https://agentii.ai/v/NVDA/sec173/5) cells) — the **total debt** served under a
long-term concept. `computed` 9,940 is not reproducible from any p.5 cell; diff is exactly 1,470;
**the filing's own long-term cell (7,470) appears in neither column.** The tree's
`DebtScheduleofLongtermDebtDetails` role defines `LongTermDebt` = `LongTermDebtCurrent` +1 /
`LongTermDebtNoncurrent` +1, consistent with `reported` being the role total. Both columns wrong,
right cell in neither.

**N-8. `AvailableForSaleSecuritiesDebtSecurities` basis collapse.** `computed` 39,233 vs
`reported` 2,010, diff 37,223 — while the sibling `AvailableForSaleDebtSecuritiesAmortizedCostBasis`
= 2,009 is a `pass`. Two bases collapsed into one row, with a `pass` on the row that hides it.

**N-9. `eps_basic` / `eps_diluted` served as unrounded IEEE doubles** (e.g.
2.399999999999999911182158029987476766109466552734375). String equality and display both break.

**N-10. Concept-filter leak.** `search_xbrl_facts(concept=NetIncomeLoss)` returned three
`BusinessAcquisitionsProFormaNetIncomeLoss` rows.

**N-11. Fact-series pagination inconsistent.** `NetIncomeLoss` `total_count: 89` with
`page_size: 50` / `total_pages: 2` returned 50 rows on page 1 and 39+3 on page 2.

---

## 12. DA-29 / DA-30-class findings, referred to the Phase 7 ledger

This artifact records `constitution_pin: "1.4.0"`, which predates DA-29 and DA-30. Per
`contracts/artifact-frontmatter.yaml` these obligations are discharged in Phase 7's validation
ledger. Two are nevertheless load-bearing here and are flagged rather than silently omitted.

**DA-30-class — one concept, two bases, no basis field (PRESENT).**
`us-gaap:OperatingIncomeLoss` is reported by the issuer on two bases in one filing — consolidated
(53,536, p.3) and segment-total (56,276, p.19) — under **one concept with no basis field**, and
the platform serves both at `is_primary: true`. This is precisely the DA-30 shape (BWXT's
equity-inclusive vs equity-exclusive operating income), with the additional property that here
the two bases **differ by 2,740M rather than by an allocation convention**, and the platform
picks one silently. **NVDA is a second DA-30 instance, not the BWXT mechanism.** The two bases are
reconciled explicitly at [📄 sec173 p.20](https://agentii.ai/v/NVDA/sec173/20), so the basis IS
establishable — the failure is entirely in the platform, which is why it is `UNRESOLVABLE-FROM-PLATFORM`
in character even though the artifact's own figures are fully resolvable from public sources.

**DA-29 — applied, and clean.** Every reconciliation in this artifact names the source of every
term. The operating-cash-flow reconciliation (§3c) uses only p.7 cells plus, for the residual,
the p.19 segment D&A that is a served fact and a printed cell. The margin reconciliation (§9) uses
only p.3, p.24 and p.26 cells. The `reported` values in §3a are reconciled to the statement face
(p.3) and identified as the p.19 segment row. **No `computed` value is cited as a derivation
anywhere in this artifact** — §1c and §3c quote `computed` only as the *object* of the defect, and
§1c proof 1 reproduces the identity (50,344 + 26,429 + 21,283) that exposes it.

---

## Carry-forwards

1. **N-1 (segment-total substitution) is the highest-value finding in this artifact** and should
   be tested universe-wide. The discriminator is mechanical and cheap: for each issuer, find
   concepts bound in **both** a consolidated role and a segment-reconciliation role, then check
   whether the served consolidated fact (un-dimensioned, `is_primary`) equals the served
   dimensioned fact. Where they differ, the platform has two candidates for one cell.
2. **The DA-30 census should be re-run with "unallocated reconciling items" as the detector**, not
   with an equity-allocation test. NVDA's instance was found by the wedge, not by a basis search.
3. **The DA-23 rule count in 001 must be re-scored.** "12 issuer-quarters" includes at least one
   issuer-quarter (NVDA) where the test is unevident rather than passed. The count of
   *issuer-quarters where DA-23 was actually testable* should replace the raw count.
4. **The DA-27 detector keyed on `source == "default"` is wrong at three issuers** (MRCY, FLY,
   NVDA-`gold_companies`). It must key on synthesized-vs-filed.
5. **Orbital-thesis content for Phase 6:** NVDA's own cost-curve statement ("the economics are
   poor today") and its own cooling statement ("liquid cooling is obviously out of the question")
   are the strongest self-sourced supports for the F2/F5 premise in the corpus. Phase 6 should
   quote them rather than paraphrase.
6. **The imaging/edge-reduction application is the one orbital workload NVDA endorses**, which
   partitions the thesis's orbital-compute market: edge data reduction is inside the vendor's
   stated scope; megawatt training compute is not.

## Could not be verified

1. **The full 10-Q was not read.** Nine pages (3, 4, 5, 6, 7, 19, 20, 24, 26) plus sec169 p.4 and
   ect80 pp.3–4. DA-25's "not exhibited" is scope-limited on that basis.
2. **`get_calculation_tree` returned a stitched multi-era role set** (2014-era share labels,
   2021–2024 lease years, 2015–2018 intangible years) under a `fiscal_year: 2026, fiscal_period:
   Q1` header. The DA-24 two-arc result comes from a role in that mixed set. Re-confirmation
   against a single-era tree was not possible with the permitted tools.
3. **The `CorporateNonSegmentMember` = 56,276 fact is unexplained at the issuer level.** Whether
   NVDA's own XBRL tags the reconciliation's starting row with both members, or the platform's
   dimensional extraction assigned it, could not be determined. It does not affect §3a (the
   `OperatingSegmentsMember` fact alone suffices), but it means there are **three** served
   candidates for one cell, not two.
4. **Instances 2 and 3 of the substitution (§3c) are selection-inferred.** The terms (1,290;
   526; 997) are all located in the source, and the residuals are exact — but I did not observe
   the instrument making the selection.
5. **The security-detection-limit question (Rule 1: every period, every fact) is answered for the
   concepts I could enumerate, not for the register.** `OperatingIncomeLoss` 69, `NetIncomeLoss`
   89, `EarningsPerShareDiluted` 78, `GrossProfit` 78, `OperatingExpenses` 69 facts surveyed;
   the full per-fact sweep of the cash-flow class across all periods was not run — the strip is
   demonstrated per-fact on three facts for one quarter, and the per-fact claim is established by
   those three sitting in a series that retains negatives elsewhere, not by exhaustive census.
6. **`search_keyword_in_source` is uninformative on table-heavy filings and unusable on
   transcripts by `source_id`.** On `sec173`, keyword "space" returned `total_count: 0` while
   keyword "Revenue" returned 23 rich descriptions — the tool matches the LLM description index,
   so a zero is **not** evidence the filing never says the word. On a transcript by `source_id` it
   returned `PROXY_ERROR / Upstream non-JSON (HTTP 404)`; the `source_id` worked only after being
   resolved to a `citation_id` via `read_source_outline`.
7. **`read_source_pages` returns `description: null` for sec173 pp.3/19/20/24/26 while
   `search_keyword_in_source` returns rich descriptions for those same page ids.** "I read the
   page and it had no description" is therefore **not** evidence the description does not exist —
   and this asymmetry is precisely the vector by which 001's three quotations were produced.
   **This artifact quotes no description field, and every quoted figure above is a cell or a
   served fact.**
8. **The 8-K accession `0001045810-26-000060`** (`fiscal_year 2026, fiscal_period Q2, period_end
   2026-06-28`, extraction 2026-08-20) was not examined and may carry Q2 FY2027 results. The
   newest 10-Q remains `sec173`. If it does, this artifact's "most recent quarter" is Q1 FY2027
   only as of the 10-Q corpus, and the DA-26/DA-27 counts would need re-running against the 8-K
   path. Note the apparent tension: the fiscal calendar forward-synthesizes FY2027 Q3/Q4 while a
   served 8-K points at a Q2 period_end.
9. **`statements_available: false`** with the note "pipeline.xbrl_rendered_statements pending
   creation" — the rendered-statement surface was unavailable, so the component identity was
   verified from served facts and filing cells rather than from rendered statements.
10. **Which instrument value a downstream consumer actually reads was not measured.** This
    artifact establishes that two contradictory published values exist and which is right; it does
    not establish whether any given report consumed 53,536 or 56,276.
