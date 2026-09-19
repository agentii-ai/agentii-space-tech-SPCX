---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: FLY
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "07d26b9c738b"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income sign-stripped — tested on every period this artifact quotes, all four, plus the full served series"
  - da_id: "DA-24"
    chosen_reading: "disposal/transaction gain contaminating the operating line — tested against the calculation-linkbase arcs into OperatingIncomeLoss"
  - da_id: "DA-25"
    chosen_reading: "issuer-defined per-unit metric not reproducible from the segment tables — FLY is single-segment; tested against the CODM table and the non-GAAP reconciliations"
  - da_id: "DA-26"
    chosen_reading: "annual value served under a quarterly label — tested on fiscal_period duration and on the earnings calendar"
  - da_id: "DA-27"
    chosen_reading: "fiscal label derived from the calendar quarter rather than the filing — tested on label basis and on the synthesized fiscal calendar"
  - da_id: "DA-28"
    chosen_reading: "IPO capital-structure discontinuity — tested as share-count step, EPS bridge, and post-IPO history availability"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: "Loss from operations, four periods: (95,197) / (54,350) / (190,865) / (112,894) — all four served positive by the platform"
    ticker: FLY
    form_type: 10-Q
    citation_id: sec21
    page_no: 6
    url: https://agentii.ai/v/FLY/sec21/6
    located_via: read_source_pages
  - figure: "Revenue up 657% to $117.7M; Spacecraft Solutions revenue 'driven by the inclusion of SciTec, which was acquired in the fourth quarter of 2025'"
    ticker: FLY
    form_type: 10-Q
    citation_id: sec21
    page_no: 40
    url: https://agentii.ai/v/FLY/sec21/40
    located_via: read_source_pages
  - figure: "CODM segment expense table, single reportable segment; 2025 comparative labelled '(Recast)'; warrant FV change 6M 2025 = (1,118)"
    ticker: FLY
    form_type: 10-Q
    citation_id: sec21
    page_no: 33
    url: https://agentii.ai/v/FLY/sec21/33
    located_via: read_source_pages
  - figure: "Adjusted EBITDA reconciliation closing to $(61,214) / $(47,903) / $(125,923) / $(95,036); Free Cash Flow $(185,199) / $(96,456); warrant FV add-back 6M 2025 = 5,107"
    ticker: FLY
    form_type: 10-Q
    citation_id: sec21
    page_no: 44
    url: https://agentii.ai/v/FLY/sec21/44
    located_via: read_source_pages
  - figure: "SciTec purchase price allocation: total consideration $550,294 = net assets acquired $550,294; goodwill $436,343; no gain on bargain purchase"
    ticker: FLY
    form_type: 10-Q
    citation_id: sec21
    page_no: 14
    url: https://agentii.ai/v/FLY/sec21/14
    located_via: read_source_pages
  - figure: "SciTec acquired 2025-10-31 for $550.3M ($277.4M cash + $269.6M stock + $3.3M working capital adjustment); $24.4M acquisition costs expensed"
    ticker: FLY
    form_type: 10-Q
    citation_id: sec21
    page_no: 13
    url: https://agentii.ai/v/FLY/sec21/13
    located_via: read_source_pages
  - figure: "IPO 2025-08-08: 22.2M shares at $45.00; 105.8M shares issued on preferred conversion; 1.0M on warrant exercise; 1-for-3.2544 reverse split; Registered Equity Offering 2026-06-01 of 12.0M shares at $48.00"
    ticker: FLY
    form_type: 10-Q
    citation_id: sec21
    page_no: 27
    url: https://agentii.ai/v/FLY/sec21/27
    located_via: read_source_pages
  - figure: "515,767 shares issued 2026-06-23 as partial consideration for the Space-ng acquisition"
    ticker: FLY
    form_type: 10-Q
    citation_id: sec21
    page_no: 52
    url: https://agentii.ai/v/FLY/sec21/52
    located_via: read_source_pages
  - figure: "Revenue disaggregation: Launch $9,400K / Spacecraft Solutions $108,283K (Q2 2026); SciTec pro forma revenue for the 2025 periods"
    ticker: FLY
    form_type: 10-Q
    citation_id: sec21
    page_no: 15
    url: https://agentii.ai/v/FLY/sec21/15
    located_via: read_source_pages
  - figure: "RKLB page 6 is the condensed consolidated statements of operations table; the sentence 001 attributed to it appears verbatim in the platform's page description instead"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 6
    url: https://agentii.ai/v/RKLB/sec109/6
    located_via: read_source_pages
---

# FLY — Recent Quarter, Defect Census (Phase 3, PIL-3)

Source: Form 10-Q, accession `0001860160-26-000023`, filed 2026-08-11. Calculated from the
filing's own calculation linkbase (`get_calculation_tree`) and its filed statement tables.

Phase 1's FLY unit-economics artifact
(`theses/002-evidence-validation/artifacts/FLY/2026-09-18_1500_unit-economics_methodology.md`)
is the upstream work on this ticker; its DA-23 component identity, its DA-28 lead, and its
citation-accuracy finding are **cited here, not re-derived**. What is new here is the
four-period census the governing rule demands, the DA-24/25/26/27 tests it never reached,
and the class-defect answer.

## Summary of verdicts

| DA | Verdict at FLY | Basis |
|---|---|---|
| **DA-23** | **CONFIRMED — 4 of 4 quoted periods, 15 of 15 served facts** | Component identity closes to zero residual on all four periods; every `OperatingIncomeLoss` fact the platform serves for FLY is positive |
| **DA-24** | **REFUTED — not a site** | The operating line has exactly two arcs; the SciTec acquisition produced no bargain-purchase gain; the only gain sits below the line |
| **DA-25** | **REFUTED as registered** (one residual reproducibility defect, §5) | No per-unit metric exists; the disclosed non-GAAP measures reproduce exactly, though one closes on a contradicted input |
| **DA-26** | **NOT CONFIRMED at FLY** | Every served `fiscal_period` label matches its fact's duration; the earnings calendar does not mislabel |
| **DA-27** | **NOT CONFIRMED at FLY** | Label basis is `gold_companies`, not `default`; outcomes correct. The residual invariant is forward-synthesis, not mislabelling |
| **DA-28** | **CONFIRMED — a site, with a different sub-mechanism than HAWK** | 11.659× share step; the registered EPS-bridge detector does not fire |

The register's assumption that this universe's defects are uniform is wrong in both
directions: **two of the six DAs (24, 25) do not fire at FLY at all**, and two more (26, 27)
do not fire on the surfaces the register names.

## 1. DA-23: the four-period census — 4 of 4 flipped, zero clean

The governing rule from MRCY's Phase 2 finding is that **DA-23 must run on every period an
artifact quotes**. FLY's filed table states the loss four times with four negative signs.
Each is tested below against the filed components on the same page.

The component identity is `gross profit − total operating expenses = loss from operations`.
All four periods, in-line, from
[📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6):

| Period | Gross profit | − Total opex | = Arithmetic result | Served as | Residual |
|---|---|---|---|---|---|
| 3M 2026 | 23,875 | 119,072 | **−95,197** | **+95,197** | 0 |
| 3M 2025 | 3,995 | 58,345 | **−54,350** | **+54,350** | 0 |
| 6M 2026 | 41,336 | 232,201 | **−190,865** | **+190,865** | 0 |
| 6M 2025 | 6,215 | 119,109 | **−112,894** | **+112,894** | 0 |

**Four periods, four filed losses, four positive values served, four residuals of exactly
zero.** The filing states the loss again in the MD&A table on
[📄 FLY 10-Q p.40](https://agentii.ai/v/FLY/sec21/40) — `Loss from operations (95,197)
(54,350)` with a `% Change` of `(75%)`, a correctly signed and correctly negated comparative —
and a third time in the CODM table on
[📄 FLY 10-Q p.33](https://agentii.ai/v/FLY/sec21/33). **The issuer states this figure four
times in one document, always negative. The platform serves it positive every time.**

Widening to the served series, `search_xbrl_facts` returns **15 `OperatingIncomeLoss` facts
for FLY spanning FY2023 through Q2 2026, and all 15 are positive.** Zero negatives. The series
is internally additive — 58,544 + 54,350 + 62,193 = 175,087 (matches the served 9M 2025
fact), 98,041 + 34,194 = 132,235 (matches 9M 2024), 95,668 + 95,197 = 190,865 (matches
6M 2026) — so **a consumer who sums quarters derives the right magnitude with the wrong sign
at every level.** The strip is consistent, which makes it invisible to any consistency check
and makes every derived figure wrong in the same direction.

**DA-23 is confirmed at FLY and its scope is wider than the register states.** The register
frames DA-23 as an income-statement defect. It is not confined to one: at FLY it also strips
`NetCashProvidedByUsedInInvestingActivities`, served as **+119,780,000** against a filed net
cash *used* of $(119,780)K, and
`CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect`,
served as **+333,149,000** against a filed net *decrease* of $(333,149)K (cash fell from
$792.9M at 2025-12-31 to $459.8M at 2026-06-30). **Any screen over this universe that reads a
`*CashProvidedByUsedIn*` concept is reading a sign-stripped magnitude.**

### 1.1 The three detectors, measured at FLY

| Detector | Result | Detail |
|---|---|---|
| **1 — component identity** | **4 of 4 fire** | §1 above. The only detector that is complete and that names the correct sign. |
| **2 — sign reconciliation, `\|computed\| == \|reported\|`** | **1 of 4 fire** | Fires at the 3M 2026 headline. **Silent at the 3M 2025 comparator** — and the reason is §3. |
| **3 — gross-profit bound** | **4 of 4 fire** | 95,197/23,875 = **3.99×** GP; 54,350/3,995 = **13.61×**; 190,865/41,336 = **4.62×**; 112,894/6,215 = **18.16×**. All four violate the bound (operating income cannot exceed gross profit). |

**Detector 3 is the exact mirror image of its performance at SPCX.** The SPCX artifact
recorded detector 3 as a false negative at every level — *"a bound test that passes on the
worst case in the document carries no information"* — because SPCX's gross margin is 55.3%
and the stripped magnitudes sat inside it. FLY's gross margin is 20.3%, so the same stripped
values sit 4× to 18× outside the bound and all four fire. **Detector 3's power scales
inversely with gross margin**, which is now measured at both ends of the range: useless at
55%, decisive at 20%. A register that reports detector 3 without its margin dependence is
reporting a number that will not transfer.

This also supplies a mechanism for the VOYG case the spec flags — `OperatingIncomeLoss`
$51.408M against gross profit $4.457M, an 11.5× ratio that "fails the gross-profit bound
outright." **That ratio is the same shape as FLY's 13.61× and 18.16×.** The spec treats VOYG
as a possible distinct sub-mechanism ("an artifact testing only for sign will pass VOYG and
be wrong"); the FLY evidence suggests the simpler reading — VOYG is an ordinary DA-23 strip
of a low-margin issuer, and the reason a sign-only test passes it is that the *magnitude* is
also wrong once the sign is wrong, which is what DA-23 does. **This should be settled by
running the component identity at VOYG rather than by adding a seventh register entry.**

## 2. The instrument, measured at FLY

Phase 1 recorded the `validate_calculation` output for this accession. Read again here for
the `computed` vs `reported` **pair only** — the `status` column is not reported, per the
instrument rule, and the FLY run is a second independent measurement of why.

The run returns **9 pass, 3 warn, 9 fail**. Of the nine `fail` rows:

| Row | computed | reported | What the row actually is |
|---|---|---|---|
| `OperatingIncomeLoss` 2026-06-30 | **−95,197,000** | 95,197,000 | **True positive.** The real DA-23 flip. |
| `OperatingIncomeLoss` 2025-06-30 | **−115,114,000** | 54,350,000 | **True positive by accident** — the `computed` is itself corrupted (§3) |
| `StockholdersEquity…` | 3,641,473,000 | **17,000** | `reported` is the **par value** of common stock ($0.0001 × 170M shares). A **214,000× understatement** |
| `DebtInstrumentCarryingAmount` | 27,221,000 | **93,000** | `reported` is a different element entirely |
| `PropertyPlantAndEquipmentNet` | **−45,145,000** | 186,057,000 | `computed` is **negative** — the arcs were applied to sign-stripped inputs, so DA-23 propagated *into* the instrument's arithmetic |
| `CommodityContractAssetCurrent` | 24,500,000 | 40,940,000 | Unresolved element mismatch |
| `OperatingExpenses` 2025-06-30 | 52,831,000 | **119,109,000** | `reported` is the **six-month** value on a three-month row (§3) |
| `NetCashProvidedByUsedInInvestingActivities` | −119,780,000 | 119,780,000 | **True positive** — DA-23 outside the income statement (§1) |
| `NetIncomeLossAvailableToCommonStockholdersDiluted` 2025-06-30 | 63,512,000 | 80,263,000 | Element mismatch — `computed` used net loss, not net loss available to common |

**Two of nine `fail` rows are true DA-23 detections. Seven are instrument artefacts — a 78%
false-positive rate on `fail`,** against the 93% measured at SPCX. Two independent
measurements, same conclusion: the `fail` tier does not carry information about the defect it
appears to name.

The `pass` tier is worse, because a `pass` is read as certification:

- `NetIncomeLoss` 2026-06-30: **computed = reported = 92,319,000**, `status: pass` — the
  sign-stripped magnitude of a **$(92,319)K net loss**.
- `CashCashEquivalents…IncreaseDecrease` 2026-06-30: **computed = reported = 333,149,000**,
  `status: pass` — the stripped magnitude of a **$(333,149)K cash decrease**.

**This is the SPCX proof replicating exactly at a second issuer.** At SPCX the equivalent row
was `NetIncomeLossAvailableToCommonStockholdersDiluted` marked `pass` at computed = reported =
541, the stripped magnitude of a $541M net loss. At FLY there are two such rows. **A `pass` on
a sign-stripped fact is not a near-miss; it is the defect wearing the instrument's highest
confidence label.**

And the `warn` tier is where a sign flip can hide quietly:
`IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` 2026-06-30 reports **reported
92,354,000** — a **positive** $(92,354)K loss — at `status: warn`, on a 3,643,000 diff that
has nothing to do with the sign.

**One further limitation, new at FLY: the instrument collapses the four periods.** The filing
quotes a 3-month and a 6-month figure for each of two year-ends. `validate_calculation`
returns **two** `OperatingIncomeLoss` rows — one per period-end date. The 6-month facts are
not separately testable through this instrument at all, because the period key is the end
date and the two durations collide. **The instrument cannot run the governing rule.**

## 3. The mechanism, read directly off the instrument's own output

Detector 2 is silent at the 3M 2025 comparator: computed **−115,114,000** against reported
**+54,350,000**. The magnitude test fails, so a reader applying detector 2 as specified would
record the comparator as clean or as unrecognised noise.

It is neither. **−115,114 is not noise, and it is not in the filing.** It decomposes exactly:

```
  Gross profit, 3M 2025 (p.6)              3,995
− Total operating expenses, 6M 2025 (p.6)  119,109
=                                        −115,114   ← the instrument's computed value
```

**The run paired a three-month numerator with a six-month denominator.** The confirmation is
in the instrument's own rows: `OperatingExpenses` at the 2025-06-30 label reports
**119,109,000** — the six-month figure — while the filed three-month value on the same page is
58,345. The platform elects the six-month fact `is_primary: true` at that label and serves the
three-month fact `is_primary: false`.

**This is the period-duration collision the SPCX artifact identified in §10.2 — "the period
key is the period end date only and does not encode duration" — now shown to corrupt a parent
`computed`, not merely to make two facts indistinguishable.** It is a stronger result than
SPCX had. At SPCX the collision was an ambiguity; at FLY it produces a number that exists
nowhere in the source document, inside the tool an analyst would use to check the source
document.

The consequence for the register is direct: **DA-23's second-most-reliable detector is
defeated by a platform mechanism, not by the issuer.** Detector 2 fires at 1 of 4 periods at
FLY. Detector 3 fires at 4 of 4. Detector 1 fires at 4 of 4 and is the only one that reports
the *correct* signed answer. **The component identity is not merely the best detector; at FLY
it is the only one whose output is admissible.**

A third comparator corruption appears in the same run: `GrossProfit` at the 2025-06-30 label
has computed **−35,000** against reported 3,995,000. The filed 3-month gross profit is 3,995;
the values on the page are 15,549 / 11,554 / 71,404 / 65,189. **−35,000 matches nothing in the
filing.** Mechanism unidentified — recorded as a third instance of comparator corruption
rather than explained.

## 4. DA-24: REFUTED — FLY is not a site

The register names FLY as a DA-24 candidate on the SciTec acquisition ($550.3M, closed
2025-10-31), asking where the accounting lands. The calculation linkbase answers it
definitively.

**The income-statement role has exactly two arcs into the operating line:**

```
us-gaap:OperatingIncomeLoss
  ├── us-gaap:GrossProfit          weight  +1
  └── us-gaap:OperatingExpenses    weight  −1
```

Nothing else. `OperatingIncomeLoss` is arithmetically `gross profit − total operating
expenses` and there is no third arc through which any gain, loss, or disposal could enter. The
operating line is closed by construction. Every candidate item hangs off
`us-gaap:NonoperatingIncomeExpense` instead — `GainLossRelatedToLitigationSettlement`,
`fly_ChangeInFairValueOfWarrantLiability`, `InterestExpenseNonoperating`,
`InterestIncomeOperating`, `OtherNonoperatingIncomeExpense` — which is below the line and
feeds `IncomeLossFromContinuingOperationsBeforeIncomeTaxes…`.

The transaction accounting confirms it. The purchase price allocation on
[📄 FLY 10-Q p.14](https://agentii.ai/v/FLY/sec21/14) shows **total consideration $550,294K
against net assets acquired of $550,294K** — the two are equal by construction, with goodwill
$436,343K as the residual. **There is no gain on bargain purchase**, which is the only way an
acquisition of this kind could put income into the operating line. The associated
[📄 FLY 10-Q p.13](https://agentii.ai/v/FLY/sec21/13) confirms the $550.3M consideration split
as $277.4M cash + $269.6M stock + $3.3M working-capital adjustment, with $24.4M of
acquisition-related costs **expensed as incurred** — an expense, not a gain.

The only gain-like item in the filing is `Gain on settlement of contingent liabilities`,
**926 / — / 1,307 / —**, which sits in `Other income (expense), net` on
[📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6) and is separately deducted in the Adjusted
EBITDA reconciliation on [📄 FLY 10-Q p.44](https://agentii.ai/v/FLY/sec21/44). It never
touches the operating line. `PaymentsToAcquireBusinessesNetOfCashAcquired` is an **investing**
arc with weight −1.

**DA-24 REFUTED at FLY, and the refutation is structural rather than evidential:** the
linkbase shows the operating line has no room for the defect. **A two-arc operating line is
the cleanest possible DA-24 test, and it should replace the acquisition-scanning approach the
register currently implies.** The register should drop FLY from its DA-24 candidate list.

## 5. DA-25: REFUTED as registered — with one residual reproducibility defect

The register defines DA-25 as an issuer-defined per-unit metric not reproducible from the
segment tables. At FLY the test resolves in the issuer's favour on the first clause and needs
restating on the second.

**No per-unit metric exists.** Phase 1's FLY artifact established that FLY discloses neither
`cost per launch` nor `revenue per launch` — *"FLY's 10-Q contains no cost per launch and no
revenue per launch metric"* — and 001's artifact reached the same conclusion independently.
The registered DA-25 shape therefore has **no site at FLY**. The register's coverage claim
needs FLY marked absent rather than untested.

**FLY is single-reportable-segment, and the segment note is a CODM expense table.** The
[📄 FLY 10-Q p.33](https://agentii.ai/v/FLY/sec21/33) table reports revenue and the significant
expense categories provided to the CODM — there is no second segment against which a per-unit
metric could be checked. The 2025 comparative is labelled **"(Recast)"**, which matters below.

**The issuer-defined metrics that do exist are fully reproducible.** FLY discloses two non-GAAP
measures, both on [📄 FLY 10-Q p.44](https://agentii.ai/v/FLY/sec21/44), each with a complete
reconciliation. Recomputing from the filed figures:

| Adjusted EBITDA | Filed | Recomputed | Residual |
|---|---|---|---|
| 3M 2026 | $(61,214) | $(61,214) | 0 |
| 3M 2025 | $(47,903) | $(47,903) | 0 |
| 6M 2026 | $(125,923) | $(125,923) | 0 |
| 6M 2025 | $(95,036) | $(95,036) — **on the +5,107 warrant basis only** | 0 |

Free Cash Flow also closes exactly: $(144,110) − $41,089 = **$(185,199)** and
$(84,619) − $11,837 = **$(96,456)**.

**But one column closes only on an input that contradicts the filing's own primary
statement.** The Adjusted EBITDA reconciliation uses a warrant fair-value add-back of
**+5,107** for the six months ended 2025-06-30. The statement of net loss on
[📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6) reports `Change in fair value of warrant
liability` of **(1,118)** for that same six-month period, and the CODM table on
[📄 FLY 10-Q p.33](https://agentii.ai/v/FLY/sec21/33) independently reports **(1,118)**. Two
tables in the current filing agree on $(1,118)K; the reconciliation on p.44 uses +5,107.

The discrepancy is 3,989 and it is load-bearing: on the income statement's own figure the
6M 2025 reconciliation lands on **$(99,025)**, not the filed $(95,036). **The reconciliation
reproduces — but only on a basis that the same filing's statement of net loss contradicts.**
The platform's `FairValueAdjustmentOfWarrants` fact for 6M 2025 is **+5,107,000**, sourced
`is_primary: true` to the Q2 2025 10-Q (`fly-20250630.htm`) rather than to the current filing's
comparative. **The platform elects the superseded value as primary,** and the "(Recast)" label
on p.33 is the issuer's own signal that a recast occurred. See §11, candidate N-3.

**DA-25 verdict: refuted as registered at FLY** — there is no per-unit metric and the
disclosed measures reproduce. The residual is not a DA-25 defect; it is a basis-election
defect, and it is worth more than the DA-25 test it displaced.

## 6. DA-26: NOT CONFIRMED at FLY

The register claims DA-26 is universal — *"19 of 19"*. FLY does not show it on either surface
tested.

**Duration labels are internally correct.** Inspecting the period bounds of the served facts:
`OperatingIncomeLoss` FY2025 = `2025-01-01 → 2025-12-31` (12 months), Q1 2026 =
`2026-01-01 → 2026-03-31` (3 months), 6M 2026 = `2026-01-01 → 2026-06-30` (6 months). Every
served label matches its fact's actual duration. The FY-labelled facts are sourced to the
10-K (`fly-20251231.htm`); the quarterly ones to the 10-Qs. **No annual value is served under
a quarterly label, and no quarterly value under an annual label.**

**The earnings calendar does not mislabel either.** `search_earnings_calendar` returns six FLY
rows. The row labelled `2025 (Q4)` carries `revenue_actual: 57673000` — $57,673K, which is the
**fourth-quarter** figure, not FY2025 revenue (FY2025 revenue reconstructs to $159,855K from
the filed quarters). Correct label, correct value.

**What does replicate is the Q4 hole.** `search_xbrl_facts` with `fiscal_period="Q4"` returns
**0 facts** — the same result SPCX returned. The cause appears structural rather than
defective: FLY files no Q4 10-Q, so a standalone fourth quarter is never filed and is only
derivable as FY − 9M. Combined with the earnings calendar's having **no FY row at all** —
FLY's annual release (2026-03-19) is labelled `2025 (Q4)` and carries Q4 revenue — **the FY2025
annual total is not reachable from either platform surface except by summing quarters or
reading the 10-K's FY-labelled facts.** That is a coverage gap with the same consequence as a
mislabelling (a screen keyed on the annual figure silently returns nothing) but it is not the
registered defect, and reporting it as DA-26 would be a false positive.

**DA-26 is NOT CONFIRMED at FLY.** Since the register asserts universality, one counterexample
is sufficient to falsify the coverage claim: **the "19 of 19" figure should be withdrawn or
re-scoped to the surface on which it was measured**, which is not the surface this artifact
tested.

## 7. DA-27: NOT CONFIRMED at FLY — and the detector as registered would be wrong

DA-27 is "fiscal labels derived from the calendar quarter rather than the filing." SPCX's
signature was `fiscal_year_end_month_source: "default"` alongside a false cross-validation
hint. **FLY presents a different source-field signature for the same correct outcome.**
`get_company_fiscal_calendar` returns `fiscal_year_end_month_source: "gold_companies"` with
`cross_validation_hint: null` — where SPCX returned `"default"` and a populated but false
hint.

The outcomes are correct at both issuers (both are 31-December filers). **So a DA-27 detector
keyed on `source == "default"` would pass FLY and fail SPCX while both are correct, and would
be measuring the derivation path rather than the label.** The register should say so.

The earnings-calendar labels are also correct and, usefully, are correct in a way that
demonstrates the point: the row labelled `2025 (Q2)` carries `report_date: 2025-09-22` — an
event occurring in **calendar Q3 2025** for a quarter that ended **2025-06-30**. The date is
calendar-drifted; the label is fiscal. `fiscal_source: "ect_exact"`. **This is exactly the
case DA-27 is meant to catch, and the platform gets it right.**

**The residual DA-27-shaped invariant is forward-synthesis, not mislabelling.**
`get_company_fiscal_calendar` synthesises FY2027 Q1–Q4 through 2027-12-31 for a filer whose
latest filing is dated 2026-08. The invariant is that **the fiscal calendar manufactures
quarters beyond the corpus rather than reporting their absence.** That generalises across both
issuers and is the part worth encoding; the `source` field is not.

## 8. DA-28: CONFIRMED — a site, with a different sub-mechanism than HAWK

**The share step is real and large.** Weighted-average shares, from
[📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6): 161,784K (3M 2026) against 13,877K
(3M 2025) — **11.659×**. The six-month pair is 160,711K against 13,659K (11.767×). FLY is a
DA-28 site.

**The mechanism is a preferred-stock conversion, not a public raise.** From
[📄 FLY 10-Q p.27](https://agentii.ai/v/FLY/sec21/27): the IPO closed 2025-08-08 with **22.2M
shares** at $45.00, and **in connection with the closing, all outstanding redeemable
convertible preferred stock converted into 105.8M shares of common stock**. A further 1.0M
shares came from automatic exercise of the Common Warrants, and a **1-for-3.2544 reverse stock
split** was effected and retroactively applied. The follow-on Registered Equity Offering
(2026-06-01, 12.0M shares at $48.00) and the 515,767 shares issued for Space-ng on 2026-06-23
([📄 FLY 10-Q p.52](https://agentii.ai/v/FLY/sec21/52)) are second-order.

**The 11.659× step is therefore not an 11.659× capital raise.** Roughly 105.8M of the ~148M
added shares were **claims that already existed all along as preferred stock** and were
reclassified into the common denominator on a single day. The pre-IPO denominator of 13,877K
describes a capital structure that omits the very claims the preferred holders were holding.
**This is a different sub-mechanism from HAWK's**, which the register records as a
de-SPAC/merger equity issuance.

**The registered detector does not fire.** HAWK's registered signature is that the
`EPS × shares` bridge fails 72% of the time. At FLY the bridge **passes at all four periods** —
0.11% / 0.08% / 0.34% / 0.02% residual — because both inputs carry the same sign strip.
`0.57 × 161,784 = 92,217` against a filed net loss available to common of 92,319. **A detector
keyed on the bridge would return "clean" at FLY.** This is the same structural weakness the
contract's `data_integrity_register_applied` rule names: a bridge that agrees on a flipped
pair is not evidence of anything.

**FLY also has post-IPO quarterly history, unlike HAWK** — Q3 2025, FY2025, Q1 2026, Q2 2026
are all served. So the "no post-IPO history" condition the register attaches to DA-28 is
absent here, and the site is confirmed on the share step alone.

### 8.1 The harm, stated in one line

| | Q2 2025 | Q2 2026 | Direction |
|---|---|---|---|
| Net loss | $(63,778)K | $(92,319)K | **deteriorated 44.8%** |
| Basic and diluted EPS | $(5.78) | $(0.57) | **"improved" 90.1%** |
| Weighted-average shares | 13,877K | 161,784K | 11.659× |

**The per-share series moves opposite to the loss it is supposed to describe.** And the
platform propagates the artefact: `search_earnings_calendar` returns
`eps_yoy_change_pct: 0.920754716981132` — a **+92.1% improvement** — for a period in which the
net loss grew 44.8%. That row also carries `eps_actual: -0.42` against the filed $(0.57), and
`eps_prior_year: -5.3` against the filed $(5.78). **See §11, candidate N-4: the calendar's EPS
basis reconciles to the filed statement at neither comparative.**

## 9. The class-defect answer: 001's page-attribution error is a class defect — and it is worse than 001 or Phase 1 described

The question was whether 001's page-attribution error at FLY recurs at other issuers. The
answer required checking at least two others. **The census is exhaustive, not sampled, and the
defect is confirmed at 3 of 3.**

A grep across all 34 ticker directories of 001's artifacts for every page-attributed
quotation pattern returns **exactly three instances in the entire thesis** — plus two
page-numbered factual references and one page-less quotation that fall outside the class:

| # | Location | 001's text | Verdict |
|---|---|---|---|
| 1 | `FLY/…_1239_unit-economics_methodology.md:54` | *"Page 6 states it in the filing's own words: …"* | **DEFECT** — the quoted sentence is the platform's page-6 description |
| 2 | `FLY/…_1239_unit-economics_methodology.md:68` | *"FLY page 40 states revenue rose 657% to $117.7M 'driven by Spacecraft Solutions growth.'"* | **DEFECT** — the quoted phrase is the platform's page-40 description |
| 3 | `RKLB/…_1239_unit-economics_methodology.md:117–118` | *"the 10-Q's own text states it explicitly on page 6: …"* | **DEFECT** — the quoted sentence is the platform's page-6 description |
| — | `FLY/…_1239:110` | *"FLY is an emerging growth company (page 1)"* | clean — a page reference, not a quotation; p.1 does state EGC status |
| — | `SPCX/…_2310_operational-kpi_methodology.md:105` | *"And SPCX states its own allocation intent explicitly: …"* | outside the class — no page number attached; first-person issuer prose, not a description |
| — | `RKLB/…_1239` | *"RKLB's 10-Q Iridium risk factors name the ITU…"* (in `SATS`) | clean — no page attribution |

**The unifying mechanism is more specific than "prose attributed to a page that holds a
table," which is how Phase 1 recorded it.** At all three sites, the quoted sentence is
**verbatim the platform's own LLM-generated page description** — the text `read_source_outline`
returns in its `description` field.

The proof is a string match, not an inference. 001's FLY quotation reads *"gross profit of
$23.9M, operating loss of $95.2M, net loss of $92.3M, and basic/diluted EPS of −$0.57."* The
`sec21` outline's page-6 description reads: *"Statements of net loss showing revenue of $117.7M
for Q2 2026 (vs $15.5M in Q2 2025) with gross profit of $23.9M, operating loss of $95.2M, net
loss of $92.3M, and basic/diluted EPS of -$0.57 for the three-month period."* Same figures, same
order, same four-part construction. And the page itself,
[📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6), is the *Condensed Consolidated Statements
of Net Loss and Comprehensive Loss* — a table, in which the string `gross profit of $23.9M`
does not and cannot appear.

The same match holds at RKLB. 001 quotes *"net loss of $(49,258) thousand, and basic and
diluted EPS of $(0.08)."* The `sec109` outline's page-6 description reads: *"Condensed
consolidated statements of operations and comprehensive loss … reporting total revenues of
$234,066 thousand for Q2 2026, net loss of $(49,258) thousand, and basic and diluted EPS of
$(0.08)."* And [📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6) is the statements of
operations — a table showing `Net loss $ (49,258)` and `Basic and diluted $ (0.08)` as table
cells.

And at FLY page 40, 001 quotes *"driven by Spacecraft Solutions growth."* The `sec21` outline's
page-40 description reads: *"…showing revenue up 657% to $117.7M driven by Spacecraft Solutions
growth…"* The page itself,
[📄 FLY 10-Q p.40](https://agentii.ai/v/FLY/sec21/40), says something materially different —
see §10.

**What this means for 002.** The defect is not an issuer-property and not an analyst-property.
It is a **platform-property**: the outline description is a fluent, figure-dense summary of the
page, written in the register of the filing, and it is served by the same tool an analyst uses
to locate the page. **Quoting it as the filing's own words is the single most likely failure
mode of the three-layer protocol, and 001 fell into it three times out of three attempts.** The
description is not marked as a summary in any way that survives being copied into prose, and
where it paraphrases a loss table it inherits the filing's negative signs — so the resulting
quotation is *substantively correct and evidentially fabricated* at the same time. That
combination is why the defect survived 001's own review and why it is more dangerous than a
wrong number.

**Two consequences for PIL-3's instrument rule.** First, *"confirm by `read_source_pages`
before citing"* is necessary but not sufficient: 001 quoted a page it had good reason to
believe contained the sentence, and `search_keyword_in_source` **returns matches on the
description text**, which is the second of its two false-positive modes and the one that
produces exactly this error. Second, **a citation to a page that holds a table should be
required to quote the table's cells, not a sentence about the table.** That is a checkable
rule, and it would have caught all three instances.

## 10. Correction to 001: FLY's revenue growth is acquired, not a mix shift

001's FLY artifact used page 40 for a constitution-level argument — that *"revenue rose 657% to
$117.7M 'driven by Spacecraft Solutions growth'"* — and concluded that *"in all three cases,
revenue growth comes from non-launch business."* The figures are right. The causal reading is
not, and the page says so.

[📄 FLY 10-Q p.40](https://agentii.ai/v/FLY/sec21/40), verbatim: *"Total revenue increased by
$102.1 million, or 657%, to $117.7 million … primarily driven by the factors discussed below."*
And the actual driver sentence: *"Spacecraft Solutions revenue increased by $99.1 million, or
1,077%, to $108.3 million … **driven by the inclusion of SciTec, which was acquired in the
fourth quarter of 2025**, and continued progress on our Blue Ghost and Elytra spacecraft
missions."*

**The filing attributes the non-launch growth to an acquisition that closed 2025-10-31 — after
the entire Q2 2025 comparative period.** Q2 2025 therefore contained **zero** SciTec revenue.
The disaggregation on [📄 FLY 10-Q p.15](https://agentii.ai/v/FLY/sec21/15) makes the split
explicit: Launch $9,400K / Spacecraft Solutions $108,283K in Q2 2026, against $6,349K / $9,200K
in Q2 2025. **Spacecraft Solutions grew from $9.2M to $108.3M, and 100% of that $99.1M
increase is the acquired business plus Blue Ghost/Elytra progress.**

This does not overturn 001's A1a/A1b proposal — launch revenue grew only 48% and remains the
smaller segment by 11×. But it **removes FLY as organic evidence for the mix-shift claim.**
001's table reads *"FLY Q2 — +657% — Spacecraft Solutions — Not the driver"* alongside RKLB's
organic space-systems growth of +$91.6M. **FLY's number is inorganic and should be excluded
from that comparison, or marked as such.** The A1b argument retains two organic
confirmations rather than three.

## 11. New register candidates

**N-1 — instrument-induced period collision corrupting a parent `computed`.** §3. Distinct
from DA-23 and from SPCX §10.2's ambiguity: the collision fabricates a value (−115,114) that
exists nowhere in the source. Higher severity than either, because it defeats a *detector*
rather than merely confusing a fact. Detect by testing whether any `computed` value
decomposes from components drawn from two different durations at the same period-end label.

**N-2 — weak-tier certification of a sign-stripped fact.** §2. Both `pass` (FLY: two rows;
SPCX: one row) and `warn` (FLY: `IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` served
positive at `warn`) certify stripped values. At FLY the `pass` tier is 22% false and the
`fail` tier is 78% false, measured on the same run. **No tier of the `status` column carries
information about DA-23.**

**N-3 — stale-primary basis election across filer revisions.** §5. The platform serves
`FairValueAdjustmentOfWarrants` for 6M 2025 as +5,107,000 at `is_primary: true` from the Q2
2025 10-Q, while the current Q2 2026 10-Q's income statement and CODM table both state
$(1,118)K for the same period — a 3,989 divergence, and the issuer labels the comparative
"(Recast)". The platform elects the superseded filing's value as primary. **Detect by
cross-checking each `is_primary` fact against the most recent filing that reports the same
concept and period.** This is the value-level counterpart of DA-26/27 and is likely to fire
widely.

**N-4 — earnings-calendar EPS on an unreconciled basis.** §8.1. `search_earnings_calendar`
serves `eps_actual: -0.42` against the filed $(0.57) for Q2 2026, and `-5.3` against the filed
$(5.78) for Q2 2025. **It matches the filed statement at neither period.** It is not a DA-23
strip (magnitudes differ) — it is a different basis, undisclosed. Detect by reconciling the
calendar's EPS to the filed basic/diluted EPS; flag any row that reproduces on neither the
net-loss nor the net-loss-available-to-common basis.

**N-5 — DA-23 extends to the cash-flow statement.** §1.
`NetCashProvidedByUsedInInvestingActivities` (+119,780,000 for a filed net cash *used* of
$(119,780)K) and
`CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect`
(+333,149,000 for a filed net *decrease* of $(333,149)K). **The register scopes DA-23 to
operating income; the defect is concept-agnostic on `*NetCashProvidedByUsedIn*`.**
`view=detailed`/`include_all_sources` variants were not tested — see "Could not be verified".

**N-6 — detector validity is regime-dependent and must be reported with its conditioning
variable.** §1.1. Detector 3 (gross-profit bound) fires 4 of 4 at FLY's 20.3% gross margin and
0 of many at SPCX's 55.3%. **A detector's registration should carry the margin range over
which it has been shown to work.**

## Carry-forwards

1. **The four-period rule is vindicated at FLY and the register's detector ranking must change
   with it.** Detector 3 fired 4 of 4 here and 0 of many at SPCX; detector 2 fired 1 of 4 here
   and is defeated by a platform mechanism, not by the issuer. **Only detector 1 (the component
   identity) was correct and complete at both issuers.** The register's ordering should be
   inverted to put the component identity first unconditionally, and detectors 2 and 3 should
   be demoted to confirmatory with their conditioning variables stated.

2. **`validate_calculation` cannot run the governing rule.** §2. It returns one row per
   period-end date, so the filing's four quoted periods collapse to two and the 6-month facts
   are untestable through it. **The instrument that the register implicitly relies on is
   structurally incapable of the check the register mandates.** Any DA-23 census must be run
   off `search_xbrl_facts` period bounds, as §1 does.

3. **The class defect is a platform property, not an analyst error, and the remedy is a
   documentation change.** §9. The outline `description` field is a fluent filing-register
   summary that `search_keyword_in_source` matches on. **002 should require that any citation
   to a table page quote the table's cells**, and should mark the `description` field as
   non-quotable in the retrieval protocol. This is the highest-value single change in this
   artifact.

4. **Two of six DAs do not fire at FLY and the register's coverage claims must be narrowed.**
   DA-24 (§4) and DA-25 (§5) are refuted, not merely untested. DA-26's "19 of 19" universality
   claim (§6) is falsified by one counterexample. DA-27's proposed `source == "default"`
   detector (§7) would be wrong at both issuers.

5. **The two-arc operating line is the cleanest available DA-24 test** and should replace
   acquisition-scanning, which produced a false candidate at FLY.

6. **The SciTec acquisition date makes FLY's YoY comparison partly non-comparable**, and the
   same will be true of every acquirer in this universe — RKLB/Iridium, SPCX/xAI notably.
   **PIL-3 should register an acquisition-comparability test alongside the six DAs**, because
   an unadjusted YoY figure at an acquiring issuer is a mixed-organic figure presented as
   organic.

7. **VOYG should be tested with the component identity before it is registered as a distinct
   sub-mechanism.** §1.1. The FLY ratios (13.61×, 18.16×) bracket VOYG's 11.5× and the same
   detector fires on all of them.

8. **FLY's EGC status and its effect on DA-26/27 coverage should be recorded as a confound.**
   Phase 1 noted FLY is an emerging growth company (p.1) with relaxed disclosure obligations.
   EGC status reduces the *filing's* content, which reduces what a defect census can conclude
   from absence — **"no site found" at an EGC issuer is weaker evidence than at a full filer.**

## Could not be verified

- **The mechanism behind `GrossProfit` computed = −35,000** at the 2025-06-30 label (§3). The
  filed 3-month value is 3,995 and no combination of values on the page produces −35. Recorded
  as a third comparator corruption, unexplained.
- **Whether the 6M 2025 warrant divergence (§5) is a disclosed restatement or an error.** The
  "(Recast)" label on p.33 is the only signal either way, and no restatement note was located.
  The observable — two bases in one filing, with the platform electing the older one — is
  verified.
- **The derivation of the earnings calendar's EPS basis (§8.1, N-4).** The served values
  reproduce on neither the net-loss nor the net-loss-available-to-common basis and on no share
  count I could reconstruct. Recorded as unreconciled rather than explained.
- **DA-26 on surfaces other than the two tested** (§6). `search_xbrl_facts` `fiscal_period`
  labels and `search_earnings_calendar` are clean at FLY. The register's "19 of 19" was
  measured somewhere; if that surface is a metrics API not reachable with the authorized tools,
  the counterexample stands but the *mechanism* of the claimed universality remains unknown.
- **N-5's scope.** DA-23 on cash-flow concepts was confirmed at 6M 2026 only, on the default
  `is_primary: true` view. `include_all_sources: true` and `view: detailed` were not run, so
  the full extent of the strip across the cash-flow statement and across segments is
  unmeasured.
- **DA-28 at FLY for periods after 2026-06-30.** Q3 2026 is a calendar estimate
  (`fiscal_source: "ect_forward"`, no actuals). The share step is measured on filed periods
  only.
- **The substantive accuracy of 001's SPCX quotation** (§9, `…_2310:105`). It carries no page
  number, so it falls outside the defect class; whether the sentence is genuine filing prose
  was not checked.
