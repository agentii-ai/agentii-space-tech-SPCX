---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: BWXT
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "07d26b9c738b"  # Q57 resolved 2026-09-18: re-derived from plugins/agent-plugins/agentii-equity-agent/skills/agentii/recent-quarter AND plugins/vertical-plugins/equity-research-core/skills/agentii/recent-quarter — two independent roots AGREE. Algorithm dispatch.skill_version_hash() (scripts/dispatch.py:132) validated 9/9 against the six pins tabled in theses/001-technology-baseline/reproduce.md, which resolve to four separate plugin roots. Supersedes the UNRESOLVED gap recorded at first write.
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "RUNS at BWXT on a SUBSTITUTE DETECTOR, and the substitute is VALID. BWXT files no gross-profit line at any level, so the registered component identity (`gross profit − opex = operating income`) cannot run in its stated form; the cost stack is unfolded instead and every term is a filed subtotal: `Revenues − Total Costs and Expenses + Equity in Income of Investees = Operating Income`. It closes TO THE DOLLAR on 8 of 8 periods, and the second level (the cost-stack close) closes to the dollar on 8 of 8. BWXT is CLEAN at every subtotal. SEPARATELY, and for the first time in this thesis, DA-23 is PRESENT at a COMPONENT element while being absent at every subtotal: all 29 served `GainLossOnSalesOfAssetsAndAssetImpairmentCharges` facts are non-negative across six fiscal years, while at least four page-verified filed columns are losses. A headline-only census cannot see this. `EPS × shares` was NOT used and is recorded as inadmissible, with the arithmetic of its failure shown."
  - da_id: "DA-24"
    chosen_reading: "PRESENT, DISCLOSED, and (mostly) immaterial — but MATERIAL to the exact year-over-year figure 001 quotes. Asset disposal is not a below-the-line item at BWXT: `Losses (gains) on asset disposals and impairments, net` is a line INSIDE `Costs and Expenses`, tagged with the GainLoss element, and carried by a calculation arc into `CostsAndExpenses` at weight −1. A gain therefore RAISES operating income. Magnitudes: 4.59% of Q1 2025 operating income, 2.22% of H1 2025, 1.23% of FY2025, ≤1.2% elsewhere. On a disposal-neutral basis 001's quoted Q1 operating-income growth of +10.4% becomes +15.9%. SEPARATELY, the LARGER contamination inside BWXT's operating line is not an asset sale at all — a disclosed $29.4M favourable contract adjustment sits in Q2 2025 operating income (28.7% of it), which falls outside DA-24's literal definition and is recorded as a candidate for the register's open list rather than as a DA-24 instance."
  - da_id: "DA-25"
    chosen_reading: "NOT PRESENT, with positive evidence rather than absence of search. No normalised per-unit metric (per-MW, per-kg, per-launch) is quoted in any period or figure in scope. Every ratio in scope is reproducible from the consolidated statement itself (operating margin 12.40% / 14.16%, R&D 0.48% of revenue), not merely from segment tables. The DA-25 positive control holds and is unusually strong at BWXT: the segment table reproduces the consolidated totals exactly at both levels — segment revenues + eliminations = consolidated revenue (601,291 + 302,512 − 2,178 = 901,625) and segment operating income + unallocated corporate = consolidated operating income (105,678 + 24,332 − 15,874 = 114,136)."
  - da_id: "DA-26"
    chosen_reading: "CONFIRMED at BWXT, in the HWM class — the mislabel lands on `Q4`. The platform metrics block carries rows `fiscal_year: 2025, fiscal_period: Q4` and `fiscal_year: 2024, fiscal_period: Q4` whose values are the ANNUAL columns: revenue 3,198,425 and 2,703,654. The issuer separately files the genuine fourth quarters in Note 16 (885,842 and 746,267), and the four filed quarters sum to the annual exactly. The defect is a LABEL defect with numerically sound content: the mislabelled row's own component identity still closes to the dollar. A consumer reading `fiscal_period: Q4` and annualising is wrong by 3.6×."
  - da_id: "DA-27"
    chosen_reading: "CANNOT MANIFEST at BWXT, by construction — a clean negative and a partition control rather than a test. BWXT's fiscal year ends in December and the platform stores `fiscal_year_end_month: 12`; all twelve enumerated quarters are exactly calendar-aligned, and the issuer's own column headers read `Three Months Ended March 31` and `Three Months Ended June 30` for periods ending 2026-03-31 and 2026-06-30. BWXT must be excluded from DA-27's denominator. METHOD NOTE, and it does not reproduce: the platform field's source is `gold_companies` here, not the `default` value recorded at SPCX — so the DA-27 method finding is issuer-specific, not universal."
  - da_id: "DA-28"
    chosen_reading: "NOT PRESENT — BWXT is a CLEAN comparator. No IPO, reverse split or SPAC in the quoted window (the 2010 spin-off from Babcock & Wilcox predates it by fifteen years), and the EPS bridge is clean in all four statement columns: misses of 0.086%, 0.166%, 0.262% and 0.562% against the sub-1% clean class, versus HAWK's 72% failure. The share count is stable (91.6M → 92.0M diluted). 001's use of `EPS × shares` was nevertheless inadmissible under the standing rule, and it was also LESS precise than the bridge 001 already had: 0.99 × 91.7M = 90.783M misses net income by 0.313%, while the exact bridge 0.99 × 91,908,600 = 90,989,514 misses by 0.086%."
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: "Q2 2026 10-Q Condensed Consolidated Statements of Income, verbatim, four columns (three and six months ended June 30, 2026 and 2025): Revenues 901,625 / 764,039 / 1,761,842 / 1,446,297; Cost of operations 699,320 / 572,642 / 1,362,169 / 1,089,707; Research and development costs 4,167 / 4,565 / 8,266 / 6,578; '(Gain) loss on asset disposals and impairments, net' (2) / 13 / 123 / (4,418); Selling, general and administrative expenses 108,432 / 102,940 / 216,448 / 190,509; Total Costs and Expenses 811,917 / 680,160 / 1,587,006 / 1,282,376; Equity in Income of Investees 24,428 / 18,545 / 45,993 / 35,133; Operating Income 114,136 / 102,424 / 220,829 / 199,054; Total Other Income (Expense) (542) / (4,665) / 82 / (9,478); Income before Provision for Income Taxes 113,594 / 97,759 / 220,911 / 189,576; Net Income 89,098 / 78,462 / 180,289 / 153,988; Net Income Attributable to BWX Technologies, Inc. 89,014 / 78,388 / 180,084 / 153,850; diluted EPS 0.97 / 0.85 / 1.96 / 1.68; diluted shares 92,007,253 / 91,702,703 / 91,957,928 / 91,788,204. NO gross-profit subtotal is presented anywhere on the face — the statement runs Revenues → Costs and Expenses → Total Costs and Expenses → Equity in Income of Investees → Operating Income."
    ticker: BWXT
    form_type: 10-Q
    citation_id: sec164
    page_no: 3
    url: https://agentii.ai/v/BWXT/sec164/3
    located_via: read_source_outline
  - figure: "Q2 2026 10-Q segment table, verbatim. REVENUES: Government Operations 601,291 / 588,959; Commercial Operations 302,512 / 176,139; Eliminations (2,178) / (1,059); total 901,625 / 764,039. OPERATING INCOME: Government Operations 105,678 / 109,417; Commercial Operations 24,332 / 6,877; subtotal 130,010 / 116,294; Unallocated Corporate (15,874) / (13,870); Total Operating Income 114,136 / 102,424. Both levels reconcile to the consolidated statement to the dollar — the DA-25 positive control."
    ticker: BWXT
    form_type: 10-Q
    citation_id: sec164
    page_no: 26
    url: https://agentii.ai/v/BWXT/sec164/26
    located_via: read_source_outline
  - figure: "Q1 2026 10-Q Condensed Consolidated Statements of Income, verbatim, two columns (three months ended March 31, 2026 and 2025): Revenues 860,217 / 682,258; Cost of operations 662,849 / 517,065; Research and development costs 4,100 / 2,013; 'Gain (loss) on asset disposals and impairments, net' 125 / (4,431); Selling, general and administrative expenses 108,017 / 87,569; Total Costs and Expenses 775,091 / 602,216; Equity in Income of Investees 21,565 / 16,588; Operating Income 106,691 / 96,630; Total Other Income (Expense) 625 / (4,813); Income before Provision for Income Taxes 107,316 / 91,817; Provision for Income Taxes 16,127 / 16,291; Net Income 91,189 / 75,526; Net Income Attributable to Noncontrolling Interest (121) / (64); Net Income Attributable to BWX Technologies, Inc. 91,068 / 75,462; basic and diluted EPS 0.99 / 0.82; basic shares 91,663,975 / 91,594,084; diluted shares 91,908,600 / 91,873,702. NO gross-profit subtotal. This is the period 001 quotes, and the page 001 did not cite."
    ticker: BWXT
    form_type: 10-Q
    citation_id: sec162
    page_no: 3
    url: https://agentii.ai/v/BWXT/sec162/3
    located_via: search_keyword_in_source
  - figure: "FY2025 10-K Consolidated Statements of Income, verbatim, three columns (years ended December 31, 2025, 2024, 2023): Revenues 3,198,425 / 2,703,654 / 2,496,309; Cost of operations 2,465,566 / 2,048,447 / 1,875,716; Research and development costs 13,867 / 7,478 / 7,613; 'Losses (gains) on asset disposals and impairments, net' (4,972) / 4,390 / 1,034; Selling, general and administrative expenses 394,416 / 318,663 / 279,694; Total Costs and Expenses 2,868,877 / 2,378,978 / 2,164,057; Equity in Income of Investees 74,911 / 55,931 / 50,807; Operating Income 404,459 / 380,607 / 383,059; Total Other Income (Expense) (6,339) / (31,887) / (61,659); Income before Provision for Income Taxes 398,120 / 348,720 / 321,400; Net Income 329,861 / 282,298 / 246,321; Net Income Attributable to BWX Technologies, Inc. 328,945 / 281,941 / 245,849; diluted EPS 3.58 / 3.07 / 2.68; diluted shares 91,856,013 / 91,859,732 / 91,874,537. The line LABEL is decisive: the filer's own heading is 'Losses (gains) …', so FY2025's parenthesised (4,972) is a GAIN while FY2024's 4,390 and FY2023's 1,034 are unparenthesised LOSSES. No gross-profit subtotal."
    ticker: BWXT
    form_type: 10-K
    citation_id: sec126
    page_no: 50
    url: https://agentii.ai/v/BWXT/sec126/50
    located_via: search_keyword_in_source
  - figure: "FY2025 10-K Note 16 – Quarterly Financial Data (Unaudited), verbatim. FY2025 quarters (Mar 31 / Jun 30 / Sep 30 / Dec 31): Revenues 682,258 / 764,039 / 866,286 / 885,842; Operating income (1) 96,630 / 102,424 / 113,349 / 92,056; Equity in income of investees 16,588 / 18,545 / 21,216 / 18,562; Net Income Attributable to BWX Technologies, Inc. 75,462 / 78,388 / 82,106 / 92,989; diluted EPS 0.82 / 0.85 / 0.89 / 1.01. FY2024 quarters: Revenues 603,966 / 681,465 / 671,956 / 746,267; Operating income (1) 92,961 / 98,806 / 96,578 / 92,262; Equity in income of investees 13,203 / 11,584 / 15,532 / 15,612; Net Income Attributable to BWX Technologies, Inc. 68,468 / 72,972 / 69,483 / 71,018; diluted EPS 0.75 / 0.79 / 0.76 / 0.77. Footnote verbatim: '(1) Includes equity in income of investees.' This page is the DA-26 comparator (the genuine fourth quarters are 885,842 and 746,267, not the annual 3,198,425 and 2,703,654) and the DA-24 adjacent finding: 'In the quarter ended June 30, 2025, we recognized favorable contract adjustments totaling $29.4 million related to a nuclear operations contract.'"
    ticker: BWXT
    form_type: 10-K
    citation_id: sec126
    page_no: 95
    url: https://agentii.ai/v/BWXT/sec126/95
    located_via: read_source_outline
---

# BWXT × recent-quarter — Phase 3 defect census (PIL-3)

## 0. What this artifact is, and the one rule it obeys

This is the Phase 3 defect census for BWX Technologies at the `recent-quarter` skill. Its subject is
not BWXT's business. Its subject is whether the numbers this thesis has already published about BWXT
survive the Data-Integrity Register, and whether the instruments that are supposed to test them
actually do.

The rule that governs the whole artifact is the one MRCY's Phase 2 finding established:

> **DA-23 must run on every period an artifact quotes.** MRCY's headline year was clean while both
> comparators were flipped, and 001's one-period check reported "−98.6%" when the true movement was
> **+2.18 margin points, the opposite sign.**

That rule has a corollary that this artifact had to resolve before it could run anything: **the
registered DA-23 test does not exist at BWXT.** BWXT files no gross-profit line. Section 1 states what
runs instead and why it is admissible. Section 2 runs it on every period in scope. Section 3 records a
DA-23 instance that no headline test could have found. Section 4 re-measures the instrument. Section 5
takes the six DAs one at a time. Section 6 is the detector-availability finding this pillar was asked
to record.

Read in one sentence: **BWXT is clean, the substitute detector is valid and stronger than the test it
replaces, and the single most interesting result is that DA-23 is present at BWXT at a line item while
being absent at every subtotal — which means the census as currently constituted cannot see it.**

---

## 1. The test that can actually run at BWXT

### 1.1 The arc set, read from the filer's own linkbase

The substitute detector is not invented here. It is read off BWXT's own calculation linkbase for the
Q1 2026 10-Q, accession `0001486957-26-000028`
(`get_calculation_tree`, role `CondensedConsolidatedStatementsofIncome`). The arcs into
`OperatingIncomeLoss` are:

| order | child | weight |
|---|---|---|
| 1 | `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` | +1 |
| 2 | `us-gaap:CostsAndExpenses` | −1 |
| 3 | `us-gaap:IncomeLossFromEquityMethodInvestments` | +1 |

and the arcs into `CostsAndExpenses` are:

| order | child | weight |
|---|---|---|
| 1 | `us-gaap:GainLossOnSalesOfAssetsAndAssetImpairmentCharges` | **−1** |
| 2 | `us-gaap:ResearchAndDevelopmentExpense` | +1 |
| 3 | `us-gaap:SellingGeneralAndAdministrativeExpense` | +1 |
| 4 | `us-gaap:CostOfGoodsAndServicesSold` | +1 |

Three facts about this arc set matter downstream.

First, **the equity-method term is a first-class child of the operating line.** BWXT's operating income
is *defined* by its own linkbase to include equity in income of investees. That is not a rounding
detail — it is 20.2% of the Q1 2026 figure (21,565 of 106,691). See §2.5.

Second, **there is no `GrossProfit` parent anywhere in the linkbase.** The income role's parent
concepts are `CostsAndExpenses`, `NetIncomeLoss`, `ProfitLoss`, `NonoperatingIncomeExpense`,
`IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest` and
`OperatingIncomeLoss`. Gross profit is not among them. The registered detector has nothing to attach
to, and that is a property of the filer's linkbase, not of the extraction.

Third, **the disposal line is inside the cost stack, at weight −1.** This is DA-24's exact
contamination vector and it is present at BWXT by construction. See §5.

### 1.2 The substitute detector, stated

```
LEVEL 1 (discharges DA-23):
    Revenues  −  Total Costs and Expenses  +  Equity in Income of Investees  =  Operating Income

LEVEL 2 (independently closes the same statement):
    Cost of operations + R&D + disposal line (signed)  +  SG&A  =  Total Costs and Expenses
```

Every term in Level 1 is a **filed subtotal** on the face of the statement, not a derived figure. Every
term in Level 2 is a filed line item. The equality is the same equality the registered detector tests
— `gross profit − opex = operating income`, rearranged with the gross-profit subtotal left unfolded:

```
gross profit      ≡  Revenues − Cost of operations
opex              ≡  R&D + disposal + SG&A
gross profit − opex + equity  ≡  Revenues − (Cost of operations + R&D + disposal + SG&A) + equity
                              ≡  Revenues − Total Costs and Expenses + equity
```

So the substitute is not an analogy to the registered test. It **is** the registered test, with the one
subtotal BWXT does not file left un-computed.

### 1.3 Why it is valid — and what it does not cover

**It is valid because it is the only DA-23 form that uses a filed parent.** The gross-profit bound (the
register's detector 2) needs a gross profit to bound against; there is none. The component identity
needs a gross profit to subtract from; there is none. What remains is the cost basket, and it is filed.

**It is stronger than the test it replaces, on one specific axis.** The register's detector 1 confirms
one value by decomposing it into two derived quantities (gross profit and opex) whose derivation is
itself unverified. The substitute decomposes it into three *filed* quantities and closes exactly. A
filament of error cannot survive in the residual, because there is no residual to hide in.

**What it does not cover — stated plainly, because this is the point of requirement 3.** The substitute
is an *identity* test, not a *bound* test. It can prove that an operating-income figure is internally
consistent with the statement it came from. It cannot detect a defect that is applied consistently to
every term of that statement, because such a defect cancels. Concretely: **if a sign were stripped
uniformly across a whole column, Level 1 would still close.** §3 shows exactly that happening one
level down, and §3.4 shows the instrument catching it while the arc set does not.

---

## 2. The census: DA-23 on every quoted period

### 2.1 Level 1 — the operating-income identity, 8 of 8 exact

All twelve values in each row below are filed figures, read off the pages cited. `Equity` is
`Equity in Income of Investees`. All figures are thousands of dollars.

| period | Revenues | Total Costs & Expenses | Equity | Sum | Filed Operating Income | verdict |
|---|---|---|---|---|---|---|
| Q1 2026 | 860,217 | 775,091 | +21,565 | **106,691** | 106,691 | **exact** |
| Q2 2026 | 901,625 | 811,917 | +24,428 | **114,136** | 114,136 | **exact** |
| H1 2026 | 1,761,842 | 1,587,006 | +45,993 | **220,829** | 220,829 | **exact** |
| Q1 2025 | 682,258 | 602,216 | +16,588 | **96,630** | 96,630 | **exact** |
| Q2 2025 | 764,039 | 680,160 | +18,545 | **102,424** | 102,424 | **exact** |
| H1 2025 | 1,446,297 | 1,282,376 | +35,133 | **199,054** | 199,054 | **exact** |
| FY2025 | 3,198,425 | 2,868,877 | +74,911 | **404,459** | 404,459 | **exact** |
| FY2024 | 2,703,654 | 2,378,978 | +55,931 | **380,607** | 380,607 | **exact** |

Q1 2026 and Q1 2025 are cited from
[📄 BWXT 10-Q p.3](https://agentii.ai/v/BWXT/sec162/3); Q2 2026, Q2 2025, H1 2026 and H1 2025 from
[📄 BWXT 10-Q p.3](https://agentii.ai/v/BWXT/sec164/3); FY2025 and FY2024 from
[📄 BWXT 10-K p.50](https://agentii.ai/v/BWXT/sec126/50).

**All eight close to the dollar.** No period is short, no period is over, no period required a plug.
The MRCY rule is discharged for every period any artifact quotes: 001's BWXT artifact quotes Q1 FY2026
and Q1 FY2025, and both are in the table.

### 2.2 Level 2 — the cost-stack close, 8 of 8 exact

The second level is run because Level 1 would close even if two offsetting errors sat inside the cost
basket. It does not depend on Level 1 and it does not reuse any of its terms except the total.

| period | Cost of operations | R&D | disposal line (signed) | SG&A | Sum | Filed Total Costs & Expenses | verdict |
|---|---|---|---|---|---|---|---|
| Q1 2026 | 662,849 | 4,100 | +125 | 108,017 | **775,091** | 775,091 | **exact** |
| Q2 2026 | 699,320 | 4,167 | −2 | 108,432 | **811,917** | 811,917 | **exact** |
| H1 2026 | 1,362,169 | 8,266 | +123 | 216,448 | **1,587,006** | 1,587,006 | **exact** |
| Q1 2025 | 517,065 | 2,013 | −4,431 | 87,569 | **602,216** | 602,216 | **exact** |
| Q2 2025 | 572,642 | 4,565 | +13 | 102,940 | **680,160** | 680,160 | **exact** |
| H1 2025 | 1,089,707 | 6,578 | −4,418 | 190,509 | **1,282,376** | 1,282,376 | **exact** |
| FY2025 | 2,465,566 | 13,867 | −4,972 | 394,416 | **2,868,877** | 2,868,877 | **exact** |
| FY2024 | 2,048,447 | 7,478 | +4,390 | 318,663 | **2,378,978** | 2,378,978 | **exact** |

The disposal column is the filed column read with the filer's own parenthesisation. Q2 2026 is `(2)`, a
gain, so the signed contribution is −2; Q2 2025 is `13`, a loss, so it is +13. Both pages label the row
`(Gain) loss on asset disposals and impairments, net` in the 10-Qs and `Losses (gains) on asset
disposals and impairments, net` in the 10-K, which fixes the convention in the filer's own words.

> **Correction recorded against Phase 2.** Phase 2's BWXT secular-trends artifact states the Q2 2026
> close as `699,320 + 4,167 + (2) + 108,432 = 811,917`. Read as written — with `(2)` carrying a `+` —
> that sums to 811,921, not 811,917. Read as the filed parenthesised gain it is exact. The identity is
> unaffected; the string is ambiguous. Recorded here per the correction policy (001's files are frozen;
> corrections are recorded in 002 and cross-cited by location). Location:
> `artifacts/BWXT/2026-09-18_1500_secular-trends_methodology.md` §6.

### 2.3 Level 3 — quarterly-to-annual articulation

The two DA-26-mislabelled rows are audited here rather than assumed, using the issuer's own Note 16
([📄 BWXT 10-K p.95](https://agentii.ai/v/BWXT/sec126/95)) as the quarterly series:

| FY2025 line | Q1 + Q2 + Q3 + Q4 (filed Note 16) | Annual (filed p.50) | verdict |
|---|---|---|---|
| Revenues | 682,258 + 764,039 + 866,286 + 885,842 = **3,198,425** | 3,198,425 | **exact** |
| Operating income | 96,630 + 102,424 + 113,349 + 92,056 = **404,459** | 404,459 | **exact** |
| Equity in income of investees | 16,588 + 18,545 + 21,216 + 18,562 = **74,911** | 74,911 | **exact** |

Three lines out of three articulate exactly. This matters twice: it means the annual DA-23 run in §2.1
is redundant with the quarterly runs rather than independent of them, and it means **the row DA-26
flags as mislabelled carries the correct annual values.** DA-26 at BWXT is a label defect with sound
content — see §5.

### 2.4 The gross-profit substitute at work: 001's $197.4M, reproduced and double-derived

001's BWXT artifact quotes *"Gross profit $197.4M — 22.9% margin"*. Requirement 3 asks what substitutes
for the missing detector; this is where the substitute earns its keep, because it can adjudicate that
figure.

- Basis A (revenues less the filed cost-of-operations subtotal): **860,217 − 662,849 = 197,368**
  → $197.4M. Margin 197,368 / 860,217 = **22.94%** → 001's 22.9%.
- Basis B (operating income plus the non-COGS cost stack, less equity):
  **106,691 + 108,017 + 4,100 + 125 − 21,565 = 197,368** — the same number by a disjoint route.

So 001's gross profit is **reproducible exactly and is robust to two independent derivations.** That is
the good news and it should be recorded as such. The bad news is that it is **not a filed figure.**
BWXT files no gross-profit subtotal in any of the three statements read, and the concept returns zero
facts on the platform. 001 quoted it as though it were filed, and then — see §7 — used it as the anchor
of the reconciliation that was supposed to clear DA-23. A §1c `no_single_basis_collapse` reading
applies: a derived gross profit must be labelled as derived and its basis named. 001 named none.

### 2.5 The basis collapse: BWXT files its operating income on two bases

This is a new finding and it is a §1c violation risk for every artifact that quotes BWXT operating
income, including 001's and including this one.

The filed statement's `Operating Income` **includes** equity in income of investees. BWXT says so in
its own words, in the footnote to its own quarterly note:
*"(1) Includes equity in income of investees."* ([📄 BWXT 10-K p.95](https://agentii.ai/v/BWXT/sec126/95)).
The linkbase agrees: the equity term is a weight-+1 child of `OperatingIncomeLoss` (§1.1).

Two competing bases therefore exist for the same label:

| period | equity-INCLUSIVE (filed face) | equity-EXCLUSIVE (`Revenues − Total Costs`) | difference as % of the quoted figure |
|---|---|---|---|
| Q1 2026 | 106,691 | 85,126 | **20.2%** |
| Q2 2026 | 114,136 | 89,708 | **21.4%** |
| FY2025 | 404,459 | 329,548 | **18.5%** |

No artifact in this thesis names the basis. Under `no_single_basis_collapse` (level: fail) that is a
§1c violation for any artifact quoting an operating-income level or a year-over-year comparison of one.
001's BWXT artifact quotes *"Operating income $106.7M vs $96.6M (+10.4%)"* with no basis named. The
growth rate happens to be nearly basis-invariant (+10.4% inclusive, +10.6% exclusive) — but that is a
coincidence of this pair, not a property of the metric, and it is not a defence.

The platform inherits the collapse: the metrics block returns `operating_income: 106691000` for Q1 2026
with no basis field.

---

## 3. The DA-23 finding at BWXT: present at a component, absent at every subtotal

This is the substantive result of the artifact.

### 3.1 The served series: zero negatives in 29 facts

`us-gaap:GainLossOnSalesOfAssetsAndAssetImpairmentCharges` for BWXT returns 29 facts spanning FY2021 Q1
to FY2026 Q1. **Every non-null value served by the platform is non-negative.** Not one negative value
appears in six fiscal years on an element whose entire purpose is to carry a sign.

By contrast, the filed pages show the element taking a negative value in at least four of those
columns.

### 3.2 The four page-verified losses, stripped — and the two gains, untouched

Every pair below is `filed page` vs `platform-served value`. The filed column gives the line exactly as
printed, with the filer's own parenthesisation, which fixes the sign.

| period | filed line (verbatim) | true signed value | served `value_numeric` | outcome |
|---|---|---|---|---|
| Q1 2026 | `125` (unparenthesised → loss) | −125 | **+125,000** | **stripped** |
| Q2 2026 | `(2)` (gain) | +2 | (not queried) | — |
| Q1 2025 | `(4,431)` (gain) | +4,431 | +4,431,000 | correct |
| Q2 2025 | `13` (loss) | −13 | **+13,000** | **stripped** |
| H1 2025 | `(4,418)` (gain) | +4,418 | +4,418,000 | correct |
| FY2025 | `(4,972)` (gain) | +4,972 | +4,972,000 | correct |
| FY2024 | `4,390` (loss) | −4,390 | **+4,390,000** | **stripped** |
| FY2023 | `1,034` (loss) | −1,034 | **+1,034,000** | **stripped** |

**Four losses stripped, three gains untouched — 4 of 4 and 3 of 3.** That is precisely the signature
the register already carries from the inherited baseline: *"4 of 4 negative flipped / 8 of 8 positive
clean."* BWXT reproduces that ratio at the element level.

### 3.3 Why the arc weight cannot be the cause

There is a competing explanation that has to be eliminated, because it has a different remedy: perhaps
the value is served correctly and the **arc weight of −1 is wrong**.

It cannot be. An arc weight is a property of the linkbase role, defined once and applied to every
period in that role. The sign discrepancy is **period-dependent**: at Q1 2025 the served `+4,431`
reconciles to the filed total under weight −1 (because the line genuinely is a gain there), while at
Q1 2026 the served `+125` does not (because the line is a loss there). A single constant weight cannot
be right in one column and wrong in the next for the same element. **Therefore the served value is the
term carrying the defect, and the defect is a sign strip.**

### 3.4 The calc-tree corroboration: the 250

The instrument confirms the strip independently and arithmetically. `validate_calculation` on the Q1
2026 10-Q reports, for `us-gaap:CostsAndExpenses`:

```
computed  774,841,000
reported  775,091,000
diff          250,000
```

The filed total is 775,091. The cost stack with the disposal term entered at **+125** is 775,091. The
cost stack with the served value **+125** pushed through the linkbase's **−1** weight is
774,966 − 125 = **774,841** — the instrument's own `computed`, to the dollar. **The discrepancy is
2 × 125 = 250, and 250 is the width of a sign strip.**

The standing instrument rule says to read the `computed` vs `reported` pair and ignore `status`. It
proves its worth here in the strongest available form: this is a **real defect**, correctly surfaced
in the pair, and `status` called the row **`pass`**.

### 3.5 What this costs a detector — and what it costs this artifact: nothing

A detector that neutralises disposals from platform facts gets the adjustment **backwards in every loss
period.** For Q1 2026 the correct disposal-neutral operating income is 106,691 + 125 = **106,816**;
a detector trusting the served sign computes 106,691 − 125 = **106,566**. The error is 250 — the same
250, in the opposite direction. Two independent instruments, same number.

**It costs this artifact nothing, and that is the point worth recording.** §2's identity closes exactly
in all 16 checks *despite* the strip, because the strip is confined to a component that Level 1 never
reads and Level 2 reads only through the filed parent. **A DA-23 census assembled from subtotals cannot
detect a component-level strip, and BWXT is the first instance in this thesis where DA-23 is present
and every subtotal is clean.** The inherited census statistic measures the headline; it does not
measure this.

---

## 4. The instrument, re-measured on BWXT (computed vs reported pairs only)

Five defects of `validate_calculation` were already measured before this artifact. BWXT exercises all
five and adds two. Per the standing rule, **no `status` value is reported here as a verdict**; where
`status` appears it appears only as evidence that the column is non-certifying.

### 4.1 `status` discarded a real defect

Measured on `0001486957-26-000028`:

| parent concept | computed | reported | diff | status | what it actually is |
|---|---|---|---|---|---|
| `CostsAndExpenses` | 774,841,000 | 775,091,000 | 250,000 | `pass` | **the signature of a real sign strip** (§3.4) |
| `DefinedBenefitPlanNetPeriodicBenefitCost` | 749,000 | 154,000 | 595,000 | `pass` | a 4.87× discrepancy |
| `OperatingIncomeLoss` (Q1 2026) | 71,139,000 | 106,691,000 | 35,552,000 | `fail` | see §4.3 |
| `NetIncomeLoss` | 91,068,000 | 91,068,000 | 0 | `pass` | correct |

Two rows carrying material discrepancies are marked `pass`, one of which is the only place in the run
where a real defect is visible. This is the third independent filing — after SPCX — where the `status`
column carries no information about correctness. The SPCX case showed `pass` on a sign-stripped value;
**BWXT shows `pass` on a value whose discrepancy is *caused by* a sign strip and equals twice its
magnitude.** The column is not merely non-certifying. On this filing it is anti-informative.

### 4.2 `reported` was wrong on a comparative — and is derivable from other rows in the same run

`us-gaap:OperatingIncomeLoss`, period 2025-03-31: **`reported` = 97,746,000.** The filed Q1 2025
operating income is **96,630,000**
([📄 BWXT 10-Q p.3](https://agentii.ai/v/BWXT/sec162/3)). The `reported` column is over by 1,116,000 —
a 1.16% error on the comparative, and the comparative is exactly the column MRCY's finding says must be
tested.

The error is not random. In the same run, `IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` for
Q1 2025 has `computed` 102,559,000 and `NonoperatingIncomeExpense` has `computed` −4,813,000. And
102,559 − 4,813 = **97,746** — the value in `reported`. So `reported` was not read from the filing at
all; it is reproducible only as an arithmetic consequence of two other rows in the same output, both of
which are themselves wrong (the filed pre-tax figure is 91,817, and the filed total other income is
+4,813, sign-inverted here).

This is defect 3 (corrupted `reported` on comparatives, the GOOG 11× understatement) sharpened into a
mechanism: **on a comparative column, `reported` can be a value derived from the run rather than a
value read from the source, and the standing rule's anchor is therefore itself unreliable on exactly
the column the MRCY rule prioritises.**

### 4.3 `computed` was not reproducible from the instrument's own tree

`us-gaap:OperatingIncomeLoss`, Q1 2026: **`computed` = 71,139,000** against a filed 106,691,000 — a
35,552,000 shortfall, 33.3% of the figure.

It is not reproducible. The instrument *returns* the arc set (§1.1) and it *serves* the facts (860,217;
775,091; 21,565; all confirmed above). Applying them: 860,217 − 775,091 + 21,565 = 106,691 — exact. No
combination of the instrument's own tree and the instrument's own served facts yields 71,139,000. Nor
is 71,139,000 any filed value in the statement.

Two things make this more than a curiosity.

**It is internally inconsistent within a single run.** The same output reports
`IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` with `computed` = 107,316,000 and `reported` =
107,316,000. The filed 107,316 = 106,691 + 625, and the filed pre-tax figure is 107,316
([📄 BWXT 10-Q p.3](https://agentii.ai/v/BWXT/sec162/3)). So the instrument **simultaneously asserts
that its parent row's `computed` is exact — which presupposes an operating income of 106,691 — and
that the operating income computes to 71,139.** Both cannot be true under one arc set applied one way.

**It is a distinct defect from the one already registered.** The VRT case was *NO RESULT* for a concept
with seven arcs — an absence. This is a *wrong value* returned for a concept with three arcs, alongside
a *correct* value for its parent. The closest existing defect is NVDA's segment-total contamination;
here the plausible mechanism is that the operating-income row drew on a **dimensioned or duplicate arc
set** — note that the segment role carries a custom parent `bwxt_CostsAndExpensesAdjusted`, so BWXT's
linkbase does contain a second cost decomposition. **The fixable part of the defect is that the
instrument reports `calculation_roles` in full and never says which role each `computed` row came
from** — so a reader cannot check which decomposition produced the number they are being shown.

### 4.4 `reported` carried the wrong quantity, twice more

| concept | computed | reported | what `reported` actually is |
|---|---|---|---|
| `StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest` | 1,280,614,000 | **1,286,000** | off by 1,279,328,000 — a column/scale mis-selection, not the total |
| `PropertyPlantAndEquipmentNet` | 324,285,000 | **879,581,000** | `reported` is **gross** PP&E (879,581), not net; the concept is net, and 879,581 − 555,296 = 324,285 confirms which is which |

Both are the NVDA-class line-item mis-selection, and both occur in a filing where the *correct* values
were available. Combined with §4.2, that is **three separate `reported` mis-selections in one filing** —
a materially denser instance set than the GOOG case that established the defect.

### 4.5 The five standing defects: reproduction on BWXT

| # | defect (as measured) | reproduced at BWXT? |
|---|---|---|
| 1 | 93% false-positive rate on `fail` | **not re-measured** — `fail` count here is 7 of 19, and two of those (`OperatingIncomeLoss` rows) are artefacts of §4.2/§4.3, so the denominator is not clean. Recorded as not re-measured rather than as a rate. |
| 2 | `pass` does not certify a sign | **yes, and amplified** (§4.1): `pass` on a row whose discrepancy *is* a sign strip |
| 3 | `reported` corrupted on comparatives | **yes, three times in one filing** (§4.2, §4.4) |
| 4 | NO RESULT for a concept with seven arcs (VRT) | **not observed** — every queried parent returned a row |
| 5 | `reported` can be a segment total (NVDA) | **yes, in kind** (§4.4): `reported` can be a *sibling quantity* (gross for net, a component for a total) |

**New this artifact:**
**6. `computed` is not reproducible from the instrument's own returned calculation tree plus its own
served facts, and can contradict its own parent row in the same run** (§4.3).

---

## 5. The six DAs, one by one

### DA-23 — sign stripping; any level failing the gross-profit bound

**VERDICT: CLEAN at every subtotal; PRESENT at one component element.**

- Subtotal level: 8 of 8 periods close exactly at Level 1 and 8 of 8 at Level 2 (§2.1, §2.2). No
  negative-value anomaly at any headline: all 42 primary `OperatingIncomeLoss` facts (FY2019 → Q1 2026)
  are positive, as are all 50 audit-view facts examined. BWXT joins the "profitable, clean" positive
  control in the inherited baseline.
- Component level: 29 of 29 served `GainLossOnSalesOfAssetsAndAssetImpairmentCharges` facts non-negative
  across six fiscal years, against four page-verified filed losses (§3.1–3.3).
- The registered detector **could not run in its stated form** and the substitute that ran is stated and
  defended in §1.
- 001's DA-23 clearance for BWXT is circular and did not discharge the rule. Repaired in §7.

### DA-24 — asset-sale contamination of the operating line

**VERDICT: PRESENT, DISCLOSED, SMALL — but MATERIAL to the exact figure 001 quotes.**

The contamination vector is structural: the disposal line is a weight-−1 child of `CostsAndExpenses`,
so a gain **raises** operating income. Measured magnitudes against the operating income of the same
column:

| period | disposal line | signed | % of that period's operating income |
|---|---|---|---|
| Q1 2025 | (4,431) gain | +4,431 | **4.59%** |
| H1 2025 | (4,418) gain | +4,418 | 2.22% |
| FY2025 | (4,972) gain | +4,972 | 1.23% |
| FY2024 | 4,390 loss | −4,390 | 1.15% |
| Q1 2026 | 125 loss | −125 | 0.12% |
| Q2 2026 | (2) gain | +2 | 0.002% |

**The material consequence is on 001's own quoted comparison.** 001 reports Q1 operating income
*"$106.7M vs $96.6M (+10.4%)"*. On a disposal-neutral basis —
(106,691 + 125) / (96,630 − 4,431) = 106,816 / 92,199 — the growth is **+15.9%**. The contamination
deprives the comparison of **5.4 percentage points** and it is not disclosed in 001.

**A larger contamination exists in the same line and is NOT DA-24.** BWXT's Note 16 discloses:
*"In the quarter ended June 30, 2025, we recognized favorable contract adjustments totaling $29.4
million related to a nuclear operations contract."*
([📄 BWXT 10-K p.95](https://agentii.ai/v/BWXT/sec126/95)). That is **28.7% of Q2 2025 operating
income** (29,400 / 102,424) and it is a one-off inside the operating line — the same *class* of problem
DA-24 exists to catch, but not an asset sale, so it falls outside DA-24's literal definition. It
matters to this artifact's own skill: the `recent-quarter` comparison of Q2 2026 against Q2 2025 is
**+11.4% as reported and +56.3% on the disclosed-adjustment-excluded basis**. The disposal adjustment
alone moves it by 0.02pt; the contract catch-up moves it by 44.8pt. Recorded as a candidate for the
register's open list, with the ranking made explicit so it is not mistaken for a DA-24 instance.

### DA-25 — normalised per-unit metrics not reproducible from segment tables

**VERDICT: NOT PRESENT.** No per-unit metric is quoted anywhere in scope. Every ratio in scope is
reproducible from the consolidated statement alone: operating margin 106,691 / 860,217 = **12.40%**
(001 quotes 12.4%), 96,630 / 682,258 = **14.16%** (001 quotes 14.2%), R&D 4,100 / 860,217 = **0.48%**
(001 quotes 0.5%). The DA-25 positive control is unusually strong at BWXT: the segment table
reproduces the consolidated statement exactly at both levels —
601,291 + 302,512 − 2,178 = 901,625 and 105,678 + 24,332 − 15,874 = 114,136
([📄 BWXT 10-Q p.26](https://agentii.ai/v/BWXT/sec164/26)).

### DA-26 — annual mislabelled as quarterly

**VERDICT: CONFIRMED, in the `Q4` class (HWM class).**

| platform row | platform value | genuine filed quarter | annual filed | verdict |
|---|---|---|---|---|
| `fiscal_year: 2025, fiscal_period: Q4`, revenues | **3,198,425** | Q4 2025 = **885,842** | FY2025 = 3,198,425 | **mislabelled** |
| `fiscal_year: 2024, fiscal_period: Q4`, revenues | **2,703,654** | Q4 2024 = **746,267** | FY2024 = 2,703,654 | **mislabelled** |
| `fiscal_year: 2023, fiscal_period: Q4`, revenues | **2,496,309** | — | FY2023 = 2,496,309 | **mislabelled** |

The genuine fourth quarters are filed in Note 16
([📄 BWXT 10-K p.95](https://agentii.ai/v/BWXT/sec126/95)) and the annual figures are filed on the face
of the statement ([📄 BWXT 10-K p.50](https://agentii.ai/v/BWXT/sec126/50)). The ratio 3,198,425 /
885,842 = 3.61× is arithmetically impossible for a quarter, so the defect is provable without appeal to
any external source. The genuine Q1/Q2/Q3 rows carry correct three-month figures and correct period end
dates.

**The mislabelled rows are numerically sound.** The FY2025 row's own operating income, 404,459, is
exactly what the §2.1 identity produces from the annual column. DA-26 at BWXT is a **label** defect, not
a value defect — the benign end of the register — but a consumer reading `fiscal_period: Q4` and
annualising an operating income of 404,459 is wrong by 3.6×.

BWXT lands in the **`Q4`/`Q1` class with HWM**, not the `Q3` class with TDG, consistent with the
register's observation that the mislabelled period varies by issuer.

### DA-27 — fiscal labels derived from the calendar quarter

**VERDICT: CANNOT MANIFEST — and the method finding does NOT reproduce.**

BWXT's fiscal year ends in December (`fiscal_year_end_month: 12`), every enumerated quarter is exactly
calendar-aligned, and the filed column headers confirm the periods: `Three Months Ended March 31` for
the period ending 2026-03-31 and `Three Months Ended June 30` for the period ending 2026-06-30
([📄 BWXT 10-Q p.3](https://agentii.ai/v/BWXT/sec162/3),
[📄 BWXT 10-Q p.3](https://agentii.ai/v/BWXT/sec164/3)). The label "Q1 FY2026" for the period ending
2026-03-31 is correct. **Zero offset. BWXT must be excluded from DA-27's denominator.**

> **Method finding, and it is a negative.** The platform field is
> `fiscal_year_end_month_source: "gold_companies"` at BWXT — **not** the `"default"` value recorded at
> SPCX, which is what the existing DA-27 method finding rests on. The method finding is therefore
> **issuer-specific, not universal**, and DA-27's enumeration path needs re-checking per issuer before
> the method finding is generalised. `cross_validation_hint` is `null` at BWXT, so nothing in the
> platform cross-checks the month.

Two structural notes. BWXT is a calendar-year filer that exhibits **DA-26 and not DA-27** — the labels
are not *offset*, they are *collapsed*, which is consistent with the register's statement that the two
defects partition the population by fiscal year-end. And the two defects break labelling from opposite
ends: DA-27 moves every label by a quarter, DA-26 merges the fourth quarter into the annual. A
calendar-year filer can only suffer the second.

### DA-28 — IPO capital-structure discontinuity

**VERDICT: NOT PRESENT. BWXT is a clean comparator.**

No IPO, no reverse split and no SPAC in the quoted window; the 2010 spin-off from Babcock & Wilcox
predates every period in scope by fifteen years, and the diluted share count is stable across the
window (91,873,702 → 92,007,253).

The registered symptom is EPS-bridge failure. All four statement columns bridge to the sub-1% clean
class:

| period | EPS(dil) × diluted shares | Net income attributable to BWXT | miss | class |
|---|---|---|---|---|
| Q1 2026 | 0.99 × 91,908,600 = 90,989,514 | 91,068,000 | **0.086%** | clean |
| Q1 2025 | 0.82 × 91,873,702 = 75,336,436 | 75,462,000 | **0.166%** | clean |
| Q2 2026 | 0.97 × 92,007,253 = 89,247,035 | 89,014,000 | **0.262%** | clean |
| Q2 2025 | 0.85 × 91,702,703 = 77,947,298 | 78,388,000 | **0.562%** | clean |

Maximum miss 0.562% — versus HAWK's 72% failure. **However, the bridge is inadmissible as a sign test
under the standing rule**, and 001 used it anyway (§7).

---

## 6. Detector availability — the census-relevant finding

### 6.1 What can and cannot run at BWXT

| detector | runs? | why |
|---|---|---|
| **D1** component identity, registered form: `gross profit − opex = operating income` | **NO — CANNOT RUN as stated** | no gross-profit subtotal is filed and no `GrossProfit` parent exists in the linkbase (§1.1). `GrossProfit` returns **0** facts |
| **D1′** substitute: `Revenues − Total Costs and Expenses + Equity in Income of Investees = Operating Income` | **YES — 8 of 8 exact** | every term is a filed subtotal (§1.2, §2.1) |
| **D2** gross-profit bound: `operating income ≤ gross profit` | **NO — cannot run as a bound** | presupposes a filed gross profit. Runs only in *derived* form and passes there (106,691 ≤ 197,368; 96,630 ≤ 165,193), but a derived bound is not a filed bound and cannot be used to discharge the register |
| **D3** margin plausibility | **YES — runs, does not discriminate** | 12.40% and 14.16% operating margins are unremarkable for a nuclear/defence supplier; the detector has no discriminating power here |
| **`EPS × shares`** | **INADMISSIBLE** | standing rule. At BWXT it also round-trips — EPS is derived from the same net income — and it is *less* precise than the bridge (0.313% vs 0.086%) |
| **subject-absence test** (`OperatingIncomeLoss` absent or segment-only — the MRK/BMY/WWD hole) | **NOT IN THE HOLE** | BWXT files a first-class `OperatingIncomeLoss`: 42 primary facts span FY2019 → Q1 2026, all positive, carried by three linkbase arcs, with a filed subtotal on the face of every statement |

### 6.2 The 2×2, and what it does to the universe-wide census

The finding, stated in the form the census can consume:

> **"Gross profit is absent" is not a single condition. It is one axis of two, and the other axis
> decides whether the issuer is resolvable.**

| | `OperatingIncomeLoss` filed as a consolidated subtotal | `OperatingIncomeLoss` absent or segment-only |
|---|---|---|
| **No gross-profit line** | **BWXT, LUNR** — D1′ runs; DA-23 discharged at every period | **MRK, BMY, WWD** — `UNRESOLVABLE-FROM-PLATFORM`; never a passed check |
| **Gross-profit line present** | the ordinary case — D1 runs | malformed statements; out of scope |

BWXT sits in the resolvable cell with a substitute that is **stronger** than the test it replaces
(§1.3). MRK/BMY/WWD sit in the unresolvable cell. The census must therefore record **two** attributes
per issuer-quarter — `gross_profit_line_present` and `operating_income_filed` — because recording only
the first would put BWXT and MRK in the same bucket when their dispositions are opposite.

### 6.3 Two independent name traps on the same detector

The LUNR lesson was that "detector unavailable" must be **tested** by attempting the detector, never
inferred from the absence of a concept name. BWXT doubles the hazard, because **two** names are absent
while the data are present:

1. **`GrossProfit` returns 0 facts** — the registered detector's subject. Absent as a *name*. The
   *subject*, operating income, is fully present.
2. **`Revenues` returns 0 facts** — revenue is tagged
   `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` (42 facts). A substitute written
   against plain `Revenues` would *also* return nothing and could be mistaken for a second
   unavailability.

The decisive test, applied here rather than inferred: **the face of the statement was read**
([📄 BWXT 10-Q p.3](https://agentii.ai/v/BWXT/sec162/3),
[📄 BWXT 10-Q p.3](https://agentii.ai/v/BWXT/sec164/3),
[📄 BWXT 10-K p.50](https://agentii.ai/v/BWXT/sec126/50)) and confirmed to contain no gross-profit
subtotal between `Revenues` and `Total Costs and Expenses`. Note that `CostOfGoodsAndServicesSold`
**is** present (662,849) — the data that *could* support a gross-profit subtotal are filed; the filer
simply does not present one. **The absence is presentational, not conceptual**, and that is the
distinction that makes the substitute the right answer rather than a coverage gap.

**Universe consequence.** The gross-profit detector's availability is a function of **statement
format**, not of the data platform. BWXT is the fifth name in this class (LUNR, MRK, BMY, WWD, BWXT).
The class does not collapse to a single disposition: two of the five are resolvable with a substitute
and three are not.

---

## 7. 001's clearance: restated, and repaired

001's BWXT artifact, §4, states verbatim:

> *"Operating income $106.7M reconciles: gross profit $197.4M less operating expenses $90.7M. EPS $0.99
> × 91.7M shares = $90.7M ≈ $91.1M net income ✓."*

Four things are wrong with it, and they are worth separating because only one of them is the DA-23
problem.

**(a) The label is wrong by a factor of 8.5.** "Operating expenses $90.7M" — BWXT's filed
`Total Costs and Expenses` is **775,091** = $775.1M. The two figures differ by 684,391.

**(b) The number is not filed at all.** $90.7M appears nowhere in any BWXT statement. It is the
residual 197,368 − 106,691 = 90,677. It is *defined* as the quantity that makes the reconciliation
close, and the reconciliation is then presented as evidence that the reconciliation holds. **That is
the circularity.** Mechanically it equals SG&A 108,017 + R&D 4,100 + disposal loss 125 − equity 21,565
= 90,677 — a derived quantity, correctly derivable, presented as though filed.

**(c) The EPS clause cannot corroborate anything, and is inadmissible.** 0.99 × 91.7 = 90.783 against
net income 91.068 — a 0.313% coincidence between two quantities linked by definition, since EPS is
computed from net income over those same shares. The standing rule bars `EPS × shares` as a sign test
outright. It was also strictly worse than the bridge 001 already had: the exact bridge misses by 0.086%.

**(d) The verdict was nevertheless right.** BWXT is clean on DA-23, and §2 now shows it at 16 exact
checks across 8 periods with the correct basis and the correct test.

**The repair, stated as the general rule this artifact contributes:**

> A clearance is discharged by showing the *components* of a filed subtotal, each of them a filed
> figure, and showing that they sum. A clearance is **not** discharged by showing that the subtotal
> equals two quantities one of which was chosen so that it would. The test for whether a check is
> circular is mechanical: **if any term in the reconciliation appears nowhere in the source, the check
> is a back-solve.** 001's $90.7M appears nowhere. 002's 775,091 and 21,565 are both filed.

---

## 8. What could not be verified

1. **Whether the sign strip is a platform-ingest effect or is present in the raw iXBRL.** §3.3 proves
   that the *served value* carries the defect, and excludes the arc weight as the cause. It cannot
   distinguish "the platform stripped it at ingest" from "the filer tagged it stripped and the platform
   passed it through", because the raw XBRL sign attribute is not exposed on any tool available to this
   artifact. The two have different remedies — platform fix versus filer fix — and this is the one
   genuinely unresolvable sub-item in the artifact. It is recorded as local to §3 and **does not make
   the pillar unresolved**: PIL-3's falsifier asks for a count of issuer-quarters with unresolved
   defect status, and BWXT's status is resolved.
2. **Which calculation role produced `computed` = 71,139,000 for `OperatingIncomeLoss`** (§4.3). The
   instrument returns its roles but not the row-to-role mapping. The dimensioned-role hypothesis (the
   segment role carries a custom `bwxt_CostsAndExpensesAdjusted` parent) is a hypothesis, not a finding.
3. **The FY2024 quarterly disposal signs beyond Q4 and FY2023's quarters.** Four page-verified loss
   columns establish the pattern (§3.2); the remaining served facts are consistent with it but were not
   each paired against a filed page.
4. **The FY2025 `CostsAndExpenses` 9M value**, which would allow a fourth quarterly articulation check
   independently of the annual. Not queried; the annual and the quarterly series already articulate
   exactly at three lines, so the check is redundant rather than missing.
5. **The platform's `q4`-row basis label.** §2.5 shows the platform collapses the equity-inclusive and
   equity-exclusive bases with no basis field. How many other issuers in the universe are collapsed the
   same way was not measured and is a carry-forward.

---

## 9. Carry-forwards to the register

1. **DA-23 needs a component-level clause.** The census as currently constituted counts headline
   subtotals. BWXT is the first issuer where DA-23 is present at a component element (4 of 4 filed
   losses stripped, 3 of 3 gains clean, 0 negatives in 29 served facts across six years) while every
   subtotal is clean. An issuer like BWXT would be recorded as a clean positive control by the current
   statistic. Proposed: report DA-23 at **two levels** — subtotal and component — or the positive
   control is measuring the wrong thing.
2. **DA-26's mislabelled period needs to be a recorded attribute, not just a confirmation.** BWXT is
   `Q4` class (with HWM), not `Q3` class (with TDG). The register already notes the period varies; the
   census should record which.
3. **DA-27's method finding is issuer-specific and must be re-derived per issuer.** The
   `fiscal_year_end_month_source` field is `gold_companies` at BWXT and was `default` at SPCX. The
   method finding as recorded over-generalises from one issuer.
4. **DA-24's definition is narrower than the contamination it is meant to catch.** BWXT's largest
   operating-line one-off is a disclosed $29.4M contract catch-up in Q2 2025 (28.7% of that quarter's
   operating income). It is not an asset sale and so is outside DA-24 — but it does exactly what DA-24
   exists to catch, and it moves this skill's own headline comparison by 44.8 points. Candidate for the
   register's open list.
5. **A new §1c basis requirement for equity-method filers.** BWXT files its operating income on two
   bases and labels the basis only in a footnote to the quarterly note. Every artifact quoting a BWXT
   operating income level or comparison currently violates `no_single_basis_collapse`. The rule needs a
   mechanical trigger: **where a parent's linkbase arcs include an equity-method child, the basis must
   be named.**
6. **Instrument defect 6, and a fixable instrument gap.** `computed` is not reproducible from the
   instrument's own returned calculation tree plus its own served facts, and can contradict its own
   parent row within one run (§4.3); and the instrument does not disclose which role produced each
   `computed` row. The second is the smaller and the more tractable.
