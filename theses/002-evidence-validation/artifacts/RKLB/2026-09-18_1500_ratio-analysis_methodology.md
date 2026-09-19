---
thesis_id: "002-evidence-validation"
pillar: PIL-5
ticker: RKLB
skill: ratio-analysis
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "2d27c7f751fa"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-16"
    chosen_reading: "DEMONSTRATED is claimed only for figures read as cells from the issuer's own filing pages; every served-store value in this artifact is labelled SERVED and is never the basis of a DEMONSTRATED ratio. Ratios computed from served values alone are stamped DERIVED-at-best in section 4"
  - da_id: "DA-23"
    chosen_reading: "the sign-strip is treated as PRESENT and MEASURED, not suspected: operating income and net income are served as positive magnitudes of identical absolute value in 7 of 7 periods. Every ratio in section 3 is classified sign-EXPOSED, flip-INVARIANT or unexposed, and the classification is derived from the arc weights and the filed cell signs, never from EPS x shares"
  - da_id: "DA-24"
    chosen_reading: "the reported 'Research and development, net' line is read as a line that CONTAINS a contra. R&D + SG&A = total operating expenses closes exactly in 7 of 7 periods, so no non-operating item sits BETWEEN the selling line and the total - but the magnitude of the contra inside R&D is undisclosed and is declared UNEVIDENT rather than clean. Non-operating items (disposals, helicopter gains) are verified below the operating line"
  - da_id: "DA-25"
    chosen_reading: "both bases reported side by side for launch economics: the issuer's normalised revenue/cost per launch and the audited segment table. The segment table governs every margin claim. The divergence is measured in 4 of 4 periods here, not only in the registered Q2 2026 instance"
  - da_id: "DA-26"
    chosen_reading: "served annual facts reachable at a quarterly label are detected twice at RKLB (fiscal_period=Q4 returns the FY2025 and FY2024 annual revenue figures 601,799 and 436,214). No ratio in this artifact is built on a Q4-labelled served fact"
  - da_id: "DA-27"
    chosen_reading: "NOT-TESTABLE at RKLB and excluded from the denominator, not reported clean: RKLB has a December fiscal year-end, which is the precondition DA-27's population excludes. The adjacent defect that IS present - a period label that does not disambiguate three-month from six-month duration, and one row that mixes them - is reported separately under its own name"
  - da_id: "DA-28"
    chosen_reading: "the registered failure mode (false POSITIVES from an EPS reconciliation on a recent listing) does not reproduce at RKLB: RKLB has reported many full post-IPO quarters and the measured failure is the opposite, a false NEGATIVE in 7 of 7 periods. The capital-structure discontinuity itself is live, so the discontinuity is carried as a DA-30 basis problem (four share-count bases, three anti-dilutive tranches) per A3's generalisation"
  - da_id: "DA-29"
    chosen_reading: "every term in every reconciliation below is a cell read from a named filing page; no `computed` column is used as a derivation and no term is back-solved. Two platform rows that CLOSE EXACTLY while being wrong are decomposed term by term rather than passed - the FY2025 NetIncomeLoss pass and the Q2 2026 NetIncomeLoss triple - and a sub-class (coincident closure / identical mirror) is named because neither is a back-solve and neither can be caught by the terms test alone"
  - da_id: "DA-30"
    chosen_reading: "the basis is named for every multi-basis concept in the ratio set: gross profit on four filed bases, operating income consolidated-only by the issuer's own statement that segment operating expenses are not reviewed, share count on four bases, deferred tax on two filed bases, liquidity on three bases, and every forward ratio on a pre-/post-Iridium-close basis. Deal-security tagging of the basis is explicit in section 8"
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM
citations:
  - figure: "Q2 2026 filed cells, three months ended June 30 2026: product revenues 181,347; service revenues 52,719; total revenues 234,066; total cost of revenues 149,490; gross profit 84,576; Research and development, net 82,429; Selling, general and administrative 59,661; total operating expenses 142,090; operating loss (57,514); total other income 13,583; loss before income taxes (43,931); provision for income taxes (5,327); net loss (49,258); comprehensive loss (54,863); basic and diluted EPS (0.08); WASO 629,681,803"
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec109"
    page_no: 6
    url: "https://agentii.ai/v/RKLB/sec109/6"
    located_via: "read_source_pages"
  - figure: "balance sheet cells at June 30 2026 / December 31 2025: cash 2,129,485/828,660; marketable securities current 172,700/187,917; inventories 266,931/158,407; total current assets 2,895,759/1,365,544; total assets 4,187,374/2,324,478; total current liabilities 528,196/334,476; total liabilities 695,221/602,624; common stock issued 639,131,688/589,525,802 and outstanding 598,180,438/543,574,552; preferred issued and outstanding 40,951,250/45,951,250; accumulated deficit (1,106,190)/(1,011,910); total stockholders' equity 3,492,153/1,721,854"
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec109"
    page_no: 5
    url: "https://agentii.ai/v/RKLB/sec109/5"
    located_via: "read_source_pages"
  - figure: "cash flow cells, six months ended June 30 2026/2025: net loss (94,280)/(127,030); D&A 35,933/17,465; SBC 47,677/37,167; net cash used in operating activities (134,407)/(77,467); purchases of PP&E and software (53,112)/(60,719); net cash used in investing activities (84,608)/(36,022); net cash provided by financing activities 1,523,403/406,048; FX effect (35)/1,127; net increase 1,304,353/293,686; beginning 833,545/275,302; end 2,137,898/568,988"
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec109"
    page_no: 8
    url: "https://agentii.ai/v/RKLB/sec109/8"
    located_via: "read_source_pages"
  - figure: "MD&A results-of-operations percentage column, Q2 2026/Q2 2025: cost of revenues 63.9%/67.9%; gross profit 36.1%/32.1%; R&D 35.2%/45.8%; SG&A 25.5%/27.6%; total operating expenses 60.7%/73.4%; operating loss (24.6)%/(41.3)%; total other income (expense) 5.8%/(2.6)%; loss before income taxes (18.8)%/(43.9)%; provision for income taxes (2.3)%/(2.0)%; net loss (21.1)%/(45.9)%"
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec109"
    page_no: 39
    url: "https://agentii.ai/v/RKLB/sec109/39"
    located_via: "read_source_pages"
  - figure: "segment cells: Launch Services Q2 2026 revenue 44,586 / cost 25,476 / gross profit 19,110 and Q2 2025 46,646/32,426/14,220; Space Systems Q2 2026 189,480/124,014/65,466 and Q2 2025 97,852/65,684/32,168; six-month Launch 108,249/60,916/47,333 and Space Systems 326,165/212,429/113,736. Also net loss attributable to common stockholders and WASO 629,681,803 / 515,086,631 with anti-dilutive options+RSUs 13,095,520 / 23,616,300 and convertible-note shares 2,607,745 / 69,261,530"
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec109"
    page_no: 32
    url: "https://agentii.ai/v/RKLB/sec109/32"
    located_via: "read_source_pages"
  - figure: "revenue disaggregation cells: Products - Space Systems Q2 2026 181,347/117,439/63,908 and Q2 2025 92,725/61,692/31,033; Services - Launch Q2 2026 44,586/25,476/19,110; Services - Space Systems Q2 2026 8,133/6,575/1,558 and Q2 2025 5,127/3,992/1,135; and the statement 'Management does not regularly review either reporting segment's total assets or operating expenses'"
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec109"
    page_no: 33
    url: "https://agentii.ai/v/RKLB/sec109/33"
    located_via: "read_source_pages"
  - figure: "revenue per launch and cost per launch: Q2 2026 $9.1M and $4.4M; Q2 2025 $7.9M and $5.0M; H1 2026 $9.2M and $4.9M; H1 2025 $7.5M and $5.3M; and the filed metric definitions (revenue per launch is the average transaction price attributable to launch contract performance obligations, independent of the recognition method)"
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec109"
    page_no: 37
    url: "https://agentii.ai/v/RKLB/sec109/37"
    located_via: "read_source_pages"
  - figure: "liquidity and the Iridium transaction: 'expects $2.1B cash and $258.1M marketable securities to fund operations for 12 months'; definitive agreement to acquire Iridium for $54 per share, approximately $8.0B enterprise value, with $3.6B committed bridge financing"
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec109"
    page_no: 44
    url: "https://agentii.ai/v/RKLB/sec109/44"
    located_via: "search_keyword_in_source"
  - figure: "FY2025 balance sheet cells at December 31 2025/2024: total current assets 1,365,544/692,621; total assets 2,324,478/1,184,342; total current liabilities 334,476/339,525; total liabilities 602,624/801,889; convertible notes net 152,395/345,392; current installments of borrowings -/12,045; accumulated deficit (1,011,910)/(813,701); total stockholders' equity 1,721,854/382,453"
    ticker: "RKLB"
    form_type: "10-K"
    citation_id: "sec87"
    page_no: 68
    url: "https://agentii.ai/v/RKLB/sec87/68"
    located_via: "read_source_pages"
  - figure: "FY2025/2024/2023 income statement cells: total revenues 601,799/436,214/244,592; gross profit 207,181/116,149/51,409; R&D net 270,716/174,394/119,054; SG&A 165,303/131,556/110,273; total operating expenses 436,019/305,950/229,327; operating loss (228,838)/(189,801)/(177,918); total other income net 2,941/390/(1,003); loss before income taxes (225,897)/(189,411)/(178,921); Benefit (provision) for income taxes 27,688/(764)/(3,650); net loss (198,209)/(190,175)/(182,571); EPS (0.37)/(0.38)/(0.38); WASO 530,664,781/495,929,861/481,768,060"
    ticker: "RKLB"
    form_type: "10-K"
    citation_id: "sec87"
    page_no: 69
    url: "https://agentii.ai/v/RKLB/sec87/69"
    located_via: "read_source_pages"
  - figure: "FY2025/2024/2023 cash flow cells: net loss (198,209)/(190,175)/(182,571); D&A 43,935/33,655/29,744; net cash used in operating activities (165,521)/(48,890)/(98,867); purchases of PP&E and software (156,285)/(67,093)/(54,707); net cash (used in) provided by investing activities (347,397)/(98,327)/12,018; net cash provided by financing activities 1,071,271/256,682/7,369; FX effect (110)/(597)/43; net increase (decrease) 558,243/108,868/(79,437); beginning 275,302/166,434/245,871; end 833,545/275,302/166,434"
    ticker: "RKLB"
    form_type: "10-K"
    citation_id: "sec87"
    page_no: 71
    url: "https://agentii.ai/v/RKLB/sec87/71"
    located_via: "read_source_pages"
  - figure: "inventory and PP&E note cells: raw materials 76,739/50,650; work in process 68,712/60,462; finished goods 12,956/7,962; total inventories 158,407/119,074; property, plant and equipment gross 410,338/260,423; accumulated depreciation (90,865)/(65,585); net 319,473/194,838"
    ticker: "RKLB"
    form_type: "10-K"
    citation_id: "sec87"
    page_no: 90
    url: "https://agentii.ai/v/RKLB/sec87/90"
    located_via: "search_keyword_in_source"
  - figure: "segment cells FY2025/2024/2023: Launch Services revenue 199,042/125,376/71,894, cost 117,772/90,786/63,827, gross profit 81,270/34,590/8,067; Space Systems revenue 402,757/310,838/172,698, cost 276,846/229,279/129,356, gross profit 125,911/81,559/43,342; by product/service Products-Space Systems 118,769/76,016/41,218, Services-Launch 81,270/34,590/8,067, Services-Space Systems 7,142/5,543/2,124"
    ticker: "RKLB"
    form_type: "10-K"
    citation_id: "sec87"
    page_no: 107
    url: "https://agentii.ai/v/RKLB/sec87/107"
    located_via: "search_keyword_in_source"
key_metrics:
  operating_income_filed_thousands: -57514
  operating_income_served_thousands: 57514
  component_identity_residuals: 50
  fcf_filed_fy2025_thousands: -321806
  fcf_served_fy2025_thousands: 9236

---

# RKLB — ratio analysis: the component identity as the only admissible numerator

**Thesis 002, pillar PIL-5, skill `ratio-analysis`, mode `methodology`.** Ticker RKLB, a deal
security under P11 (Rocket Lab's agreement to acquire Iridium, $54/share, approximately
$8.0B enterprise value, $3.6B committed bridge — [RKLB 10-Q p.44](https://agentii.ai/v/RKLB/sec109/44)),
tagged `standalone_pre_merger` throughout. **No ratio in this artifact is computed on a
post-close basis**, and every forward-looking ratio is flagged in section 8 as carrying a
pre-/post-close basis risk that this artifact cannot close.

**What this artifact is.** T090's literal instruction is to cross-check *every derived ratio
against the component identity* and to trace *every residual to a named defect or declare it
unresolved*. It is carried out as four objects:

1. the component identity, stated in-line for every period (section 1);
2. the ratio set, each ratio classified by whether the platform's sign defect can reach it
   (section 3), with the served-store value and the filed value both shown;
3. the six-defect census DA-23…DA-28, each with a verdict and, where not testable, the KIND
   of not-testability named (section 5);
4. what this does to PIL-5's falsifier (section 9).

**What it is not.** No valuation ratio is computed: the `ratio-analysis` skill matrix row for
RKLB carries Market Data Stage `none`, so price-dependent ratios (P/E, EV/EBITDA, P/B, PEG)
are **UNEXERCISED**, and section 5 records that word rather than a clean verdict. A test that
cannot fail is not a passing test; the same discipline applies to a test that was never run.

---

## 0. Method: the filer's own linkbase supplies the identity

Every identity used below is the **filer's own calculation arc**, read from
`get_calculation_tree(0001819994-26-000062)` (role
`CONDENSEDCONSOLIDATEDSTATEMENTSOFOPERATIONSANDCOMPREHENSIVELOSS`), not an analyst
convention:

| parent | child | weight |
|---|---|---|
| `OperatingIncomeLoss` | `GrossProfit` | **+1** |
| `OperatingIncomeLoss` | `OperatingExpenses` | **−1** |
| `OperatingExpenses` | `SellingGeneralAndAdministrativeExpense` | **+1** |
| `OperatingExpenses` | `ResearchAndDevelopmentExpense` | **+1** |
| `GrossProfit` | `RevenueFromContractWithCustomerExcludingAssessedTax` | **+1** |
| `GrossProfit` | `CostOfRevenue` | **−1** |
| `NetIncomeLoss` | `IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` | **+1** |
| `NetIncomeLoss` | `IncomeTaxExpenseBenefit` | **−1** |
| `NonoperatingIncomeExpense` | `InterestExpenseNonoperating` | **−1** |
| `NonoperatingIncomeExpense` | `InvestmentIncomeNonoperating` | **+1** |
| `NonoperatingIncomeExpense` | `ForeignCurrencyTransactionGainLossBeforeTax` | **+1** |
| `NonoperatingIncomeExpense` | `OtherNonoperatingIncomeExpense` | **+1** |
| `CashCashEquivalents…PeriodIncreaseDecrease…` | operating / investing / financing / FX effect, all four | **+1** |
| `Assets` | ten children: `AssetsCurrent`, PP&E net, intangibles net, goodwill, both ROU assets, MS non-current, restricted cash, DTA, other non-current — **all ten** | **+1 each** |

The identity `gross profit − opex = operating income` is therefore not a heuristic. It is the
linkbase. That matters for the contract rule `data_integrity_register_applied`, which requires
the component derivation in-line: the derivation below is the filer's arithmetic, and where it
disagrees with the platform the discrepancy is attributable to a named column.

**The four detectors applied, and one refinement.** (i) DA-23's strip signature; (ii) A16's
overshoot detector; (iii) the calculation-weight discriminator; (iv) a **third exact
signature identified in this artifact — self-reference**, where `diff` equals the `reported`
value and `computed = 2 × reported` exactly (FY2025 `FinanceLeaseLiabilityPaymentsDue`
computed 49,220,000 / reported 24,610,000; `LesseeOperatingLeaseLiabilityPaymentsDue`
computed 252,818,000 / reported 126,409,000 — both, `diff` = reported exactly). Self-reference
is not a strip: a strip moves a value across zero, self-reference doubles it. All three are
exact, and all three are present at RKLB in one filing each.

**A8's weight rule, sharpened.** *A concept enters its parent at a weight fixed in the
linkbase; the store holds the magnitude as displayed.* The consequences are:

- at weight **+1**, a filed-parenthesised child served positive is a **strip** (measured);
- at weight **−1**, a positive magnitude is **licensed** — which removes the false positive
  on `InterestExpenseNonoperating` (filed `(581)`, served `+581`, `w = −1`, **correct**) but
  **cannot certify**. RKLB falsifies sufficiency: FY2025 `IncomeTaxExpenseBenefit` is a
  **benefit** (filed "Benefit (provision) for income taxes 27,688", unparenthesised), so its
  contribution to `NetIncomeLoss` is **positive**, while the arc is `−1` and the store serves
  `+27,688` → the tool subtracts a benefit. Same concept, same weight, same issuer, adjacent
  periods: Q2 2026 "Provision for income taxes (5,327)" is served `+5,327` and that is
  **correct**. **The weight discriminator therefore resolves *unidirectional* concepts and is
  powerless on *bidirectional* ones — a concept tagged once for both a gain and a loss, or
  both an expense and a benefit.** At RKLB the bidirectional set is exactly
  `ForeignCurrencyTransactionGainLossBeforeTax`, `OtherNonoperatingIncomeExpense`,
  `IncomeTaxExpenseBenefit` and `ProfitLoss`; this is the A17 directionality boundary extended
  from "does the convention flip across issuers" to "does it flip across periods for one
  issuer and one concept."

---

## 1. The component identity, in-line, every period — 50 checks, 50 zero residuals

All values in thousands of USD, as filed. Identities: **(A)** `GP − opex = OI`;
**(B)** `R&D + SG&A = opex`; **(C)** `OI + total other = pretax`; **(D)** `pretax − tax = NI`,
where the tax enters as an expense (negative when the filing shows a benefit).
Cells from [RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6) and
[RKLB 10-K p.69](https://agentii.ai/v/RKLB/sec87/69).

| period | A: GP − opex | B: R&D + SG&A | C: OI + other | D: pretax − tax | residual |
|---|---|---|---|---|---|
| Q2 2026 | 84,576 − 142,090 = **(57,514)** | 82,429 + 59,661 = **142,090** | (57,514) + 13,583 = **(43,931)** | (43,931) − 5,327 = **(49,258)** | 0 |
| Q2 2025 | 46,388 − 106,027 = **(59,639)** | 66,134 + 39,893 = **106,027** | (59,639) + (3,837) = **(63,476)** | (63,476) − 2,938 = **(66,414)** | 0 |
| H1 2026 | 161,069 − 274,552 = **(113,483)** | 162,942 + 111,610 = **274,552** | (113,483) + 22,738 = **(90,745)** | (90,745) − 3,535 = **(94,280)** | 0 |
| H1 2025 | 81,635 − 200,462 = **(118,827)** | 121,243 + 79,219 = **200,462** | (118,827) + (6,078) = **(124,905)** | (124,905) − 2,125 = **(127,030)** | 0 |
| FY2025 | 207,181 − 436,019 = **(228,838)** | 270,716 + 165,303 = **436,019** | (228,838) + 2,941 = **(225,897)** | (225,897) − (−27,688) = **(198,209)** | 0 |
| FY2024 | 116,149 − 305,950 = **(189,801)** | 174,394 + 131,556 = **305,950** | (189,801) + 390 = **(189,411)** | (189,411) − 764 = **(190,175)** | 0 |
| FY2023 | 51,409 − 229,327 = **(177,918)** | 119,054 + 110,273 = **229,327** | (177,918) + (1,003) = **(178,921)** | (178,921) − 3,650 = **(182,571)** | 0 |

The FY2025 row of identity (D) is the one that matters: the filed tax line is a **benefit** of
27,688 shown without parentheses ("Benefit (provision) for income taxes 27,688",
[RKLB 10-K p.69](https://agentii.ai/v/RKLB/sec87/69)), so the tax expense is −27,688 and
subtracting it **increases** the loss. This is the single cell that the platform's store gets
backwards, and it is the cell that makes the platform's FY2025 `NetIncomeLoss` row `pass`
(section 5.3).

**Balance sheet identities, both dates** — cells from
[RKLB 10-Q p.5](https://agentii.ai/v/RKLB/sec109/5) and
[RKLB 10-K p.68](https://agentii.ai/v/RKLB/sec87/68):

| identity | 2026-06-30 | 2025-12-31 |
|---|---|---|
| current assets = sum of six lines | 2,129,485 + 172,700 + 112,889 + 94,245 + 266,931 + 119,509 = **2,895,759** | 828,660 + 187,917 + 39,001 + 61,606 + 158,407 + 89,953 = **1,365,544** |
| total assets = current + ten non-current | (ten children) = **4,187,374** | (ten children) = **2,324,478** |
| current liabilities = sum of five lines | 74,512 + 44,206 + 29,118 + 351,193 + 29,167 = **528,196** | 72,699 + 19,299 + 25,803 + 195,438 + 21,237 = **334,476** |
| total liabilities = current + six non-current | **695,221** | **602,624** |
| equity = preferred + common − treasury + APIC − deficit − AOCI | 4 + 60 − 0 + 4,606,854 − 1,106,190 − 8,575 = **3,492,153** | 5 + 54 − 0 + 2,735,669 − 1,011,910 − 1,964 = **1,721,854** |
| liabilities + equity = total assets | 695,221 + 3,492,153 = **4,187,374** | 602,624 + 1,721,854 = **2,324,478** |

Twelve checks, twelve zeros. Note the equity identity **requires the negative accumulated
deficit** — the filed arithmetic is only correct with the sign, and the platform's own
`RetainedEarningsAccumulatedDeficit` fact is **not retrievable at all** for RKLB (a
concept-keyed `search_xbrl_facts` returns **zero rows** while the balance sheet line reads
`Accumulated deficit (1,106,190)`). A zero from a concept-keyed query is evidence about the
tag, not about the filing; the equity denominator used in section 3 is therefore established
from the filed cells, not from the store.

**Cash-flow identities** — cells from [RKLB 10-Q p.8](https://agentii.ai/v/RKLB/sec109/8) and
[RKLB 10-K p.71](https://agentii.ai/v/RKLB/sec87/71):

| period | operating + investing + financing + FX = net change | beginning + net change = end | residual |
|---|---|---|---|
| H1 2026 | (134,407) + (84,608) + 1,523,403 + (35) = **1,304,353** | 833,545 + 1,304,353 = **2,137,898** = cash 2,129,485 + restricted 8,413 | 0 |
| FY2025 | (165,521) + (347,397) + 1,071,271 + (110) = **558,243** | 275,302 + 558,243 = **833,545** | 0 |
| FY2024 | (48,890) + (98,327) + 256,682 + (597) = **108,868** | 166,434 + 108,868 = **275,302** | 0 |
| FY2023 | (98,867) + 12,018 + 7,369 + 43 = **(79,437)** | 245,871 − 79,437 = **166,434** | 0 |

**Result: 50 component-identity checks across 7 income-statement periods, 2 balance-sheet
dates and 4 cash-flow periods, all closing with residual exactly zero.** The filed record is
arithmetically exact everywhere this artifact checks it. **The residual to be explained is
therefore not an arithmetic gap; it is a sign gap, and every residual below is a sign gap or
a selection error.**

---

## 2. What the served store does to that identity

For Q2 2026 (the accession's own period), the served facts are, on the store's own metadata
(`is_primary: true`, `dimensions: {}`, `source_authority: 2`, `source_file: rklb-20260630.htm`):

| concept | served | filed cell (p.6) | verdict |
|---|---|---|---|
| `us-gaap:GrossProfit` | **84,576,000** | 84,576 | CORRECT |
| `us-gaap:OperatingExpenses` | **142,090,000** | 142,090 | CORRECT |
| `us-gaap:OperatingIncomeLoss` | **57,514,000** | **(57,514)** | **STRIPPED** |
| `us-gaap:NetIncomeLoss` | **49,258,000** | **(49,258)** | **STRIPPED** |

So the served components are **sound** and the served subtotal is **corrupt**:

> served GP 84,576,000 − served opex 142,090,000 = **−57,514,000**
> served `OperatingIncomeLoss` = **+57,514,000**
> difference = **115,028,000 = exactly 2 × 57,514,000**

and the same relation holds in **7 of 7 periods** (the served-store margin is the positive
mirror of the true margin):

| period | true operating margin | served-store operating margin | true net margin | served-store net margin |
|---|---|---|---|---|
| Q2 2026 | −24.57% | **+24.57%** | −21.04% | **+21.04%** |
| Q2 2025 | −41.27% | **+41.27%** | −45.96% | **+45.96%** |
| H1 2026 | −26.12% | **+26.12%** | −21.70% | **+21.70%** |
| H1 2025 | −44.49% | **+44.49%** | −47.56% | **+47.56%** |
| FY2025 | −38.03% | **+38.03%** | −32.94% | **+32.94%** |
| FY2024 | −43.51% | **+43.51%** | −43.60% | **+43.60%** |
| FY2023 | −72.74% | **+72.74%** | −74.64% | **+74.64%** |

**Consequence for this skill, stated as the artifact's operational rule:** at RKLB the
component identity is not merely a check that a served ratio can be *tested* against — it is
**the only admissible source for the numerator**. Every DEMONSTRATED ratio in section 3 is
computed from filed cells with the identity shown in-line; where a served-store value is also
given it is labelled SERVED and is never the basis of a grade.

---

## 3. The ratio census: every derived ratio, and whether the sign defect can reach it

Classification rule used throughout, derived in section 3.4: a DA-23 strip moves a stored
value across zero. It is therefore **visible** in a ratio only when the strip does not cancel
between numerator and denominator.

### 3.1 Not sign-exposed (no negative appears in the filed numerator or denominator)

| ratio | period | component identity, in-line | value |
|---|---|---|---|
| gross margin | Q2 2026 | (234,066 − 149,490) / 234,066 = 84,576 / 234,066 | **36.13%** |
| | Q2 2025 | (144,498 − 98,110) / 144,498 = 46,388 / 144,498 | **32.10%** |
| | H1 2026 | 161,069 / 434,414 | **37.08%** |
| | H1 2025 | 81,635 / 267,067 | **30.57%** |
| | FY2025 | 207,181 / 601,799 | **34.43%** |
| | FY2024 | 116,149 / 436,214 | **26.63%** |
| | FY2023 | 51,409 / 244,592 | **21.02%** |
| segment gross margin — Launch Services | Q2 2026 / Q2 2025 / H1 2026 / H1 2025 / FY2025 / FY2024 / FY2023 | 19,110/44,586 · 14,220/46,646 · 47,333/108,249 · 21,437/82,238 · 81,270/199,042 · 34,590/125,376 · 8,067/71,894 | **42.86 / 30.48 / 43.73 / 26.07 / 40.83 / 27.59 / 11.22%** |
| segment gross margin — Space Systems | same seven | 65,466/189,480 · 32,168/97,852 · 113,736/326,165 · 60,198/184,829 · 125,911/402,757 · 81,559/310,838 · 43,342/172,698 | **34.55 / 32.87 / 34.87 / 32.57 / 31.26 / 26.24 / 25.10%** |
| current ratio | 2026-06-30 / 2025-12-31 / 2024-12-31 | 2,895,759/528,196 · 1,365,544/334,476 · 692,621/339,525 | **5.482 / 4.083 / 2.040** |
| quick ratio | same three | (CA − inventory)/CL = 2,628,828/528,196 · 1,207,137/334,476 · 573,547/339,525 | **4.977 / 3.609 / 1.689** |
| cash ratio | same three | (cash + MS current)/CL = 2,302,185/528,196 · 1,016,577/334,476 · 418,990/339,525 | **4.359 / 3.039 / 1.234** |
| working capital | same three | 2,895,759 − 528,196 · 1,365,544 − 334,476 · 692,621 − 339,525 | **2,367,563 / 1,031,068 / 353,096** |
| debt / equity | same three | 695,221/3,492,153 · 602,624/1,721,854 · 801,889/382,453 | **0.199 / 0.350 / 2.097** |
| net cash | same three | cash + current MS + non-current MS − (convertible notes net + long-term borrowings net) = 2,387,590 − 14,845 · 1,098,824 − 154,111 · 479,676 − 401,486 | **2,372,745 / 944,713 / 78,190** |
| book value per share | 2026-06-30 | 3,492,153 / 598,180,438 (outstanding) · 3,492,153 / 639,131,688 (issued) | **$5.838 / $5.464** |
| | 2025-12-31 | 1,721,854 / 543,574,552 · 1,721,854 / 589,525,802 | **$3.168 / $2.921** |
| cash per share | 2026-06-30 | 2,129,485 / 598,180,438 (cash only) · 2,387,590 / 598,180,438 (cash + securities) | **$3.560 / $3.991** |
| asset turnover | FY2025 | 601,799 / avg(1,184,342 , 2,324,478) = 601,799/1,754,410 · end-of-period 601,799/2,324,478 | **0.343 / 0.259** |
| inventory turnover and DIO | FY2025 | 394,618 / avg(119,074 , 158,407) = 394,618/138,740.5; DIO = 365/2.844 | **2.844× / 128.3 d** |
| DSO | FY2025 | avg(36,440 , 39,001) / 601,799 × 365 | **22.9 d** |
| DPO | FY2025 | avg(53,059 , 72,699) / 394,618 × 365 | **58.2 d** |
| revenue per launch, cost per launch (issuer basis) | Q2 2026 / Q2 2025 / H1 2026 / H1 2025 | filed cells, [p.37](https://agentii.ai/v/RKLB/sec109/37) | $9.1M / $4.4M · $7.9M / $5.0M · $9.2M / $4.9M · $7.5M / $5.3M |

**None of these is exposed to DA-23**, because no filed cell in any of them is negative: a
strip requires a filed-parenthesised cell, and these ratios are built from revenue, cost,
asset, liability, equity and share-count cells that the filing shows positive. **They are
exposed to a different defect, and it is larger — see 3.3.**

### 3.2 Visibly sign-exposed (numerator negative, denominator positive: the served ratio is the positive mirror)

| ratio | period | filed identity | true | served |
|---|---|---|---|---|
| operating margin | 7 periods | OI / revenue, section 2 | −24.57% … −72.74% | **mirror, +24.57% … +72.74%** |
| net margin | 7 periods | NI / revenue | −21.04% … −74.64% | **mirror** |
| EBITDA (OI + D&A) and margin | FY2025 | (228,838) + 43,935 = (184,903) / 601,799 | **−184,903 (30.73%)** | **+184,903** |
| EBITDA, SBC-inclusive basis | FY2025 | −184,903 + 71,099 | **−113,804 (18.91%)** | **+113,804** |
| EBITDA | H1 2026 | (113,483) + 35,933 = (77,550) / 434,414 | **−77,550 (17.85%)** | **+77,550** |
| EBITDA | FY2024 / FY2023 | (189,801) + 33,655 ; (177,918) + 29,744 | **−156,146 · −148,174** | mirrors |
| ROE | FY2025 | 198,209 / avg(382,453 , 1,721,854) = 198,209/1,052,153.5 | **−18.84%** | **+18.84%** |
| ROE, end-of-period basis | FY2025 | 198,209 / 1,721,854 | **−11.51%** | **+11.51%** |
| ROE, annualised | H1 2026 | 94,280 / avg(1,721,854 , 3,492,153) × 2 | **−7.23%** | **+7.23%** |
| ROA | FY2025 | 198,209 / 1,754,410 | **−11.30%** | **+11.30%** |
| ROIC (pre-tax, debt + equity) | FY2025 | 228,838 / (154,111 + 1,721,854) | **−12.20%** | **+12.20%** |
| ROIC, annualised | H1 2026 | (57,514 × 4) / (14,845 + 3,492,153) | **−6.56%** | **+6.56%** |
| **free cash flow** | FY2025 | (165,521) − 156,285 = **(321,806)** / 601,799 | **−321,806 (−53.47%)** | **+9,236 (+1.53%)** |
| | H1 2026 | (134,407) − 53,112 = **(187,519)** / 434,414 | **−187,519 (−43.17%)** | **+81,295 (+18.71%)** |
| | FY2024 | (48,890) − 67,093 = **(115,983)** / 436,214 | **−115,983 (−26.59%)** | **−18,203 (−4.17%)** |
| | FY2023 | (98,867) − 54,707 = **(153,574)** / 244,592 | **−153,574 (−62.79%)** | **+44,160 (+18.06%)** |

**FCF is the sharpest case in the artifact and it is not a cancellation.** The two components
sit at **opposite weights in different parents**: operating cash flow enters the net-change
parent at **+1** (and is therefore stripped), while capex enters the investing parent at **−1**
(and is therefore *licensed* as a positive magnitude and is served correctly). At a user
level the two are combined by subtraction, so the error does not cancel:

> served FCF, FY2025 = +165,521 − 156,285 = **+9,236**
> filed FCF, FY2025 = −165,521 − 156,285 = **−321,806**
> error = 331,042 = **exactly 2 × 165,521**

so the platform reports RKLB as **free-cash-flow positive at a +1.53% margin in FY2025, in H1
2026 and in FY2023**, where the filed record is negative in all four periods tested. **The
served OCF values themselves are DERIVED here from the platform's own exact overshoot
residuals, both of which are measured:** FY2025 net-change row raw sum 1,584,299,000 against
reported 558,243,000, residual 1,026,056,000 = exactly 2 × (165,521 + 347,397 + 110); H1 2026
residual 438,100,000 = exactly 2 × (134,407 + 84,608 + 35). Since every child of the net-change
parent enters at **+1**, the overshoot is exactly `2 × Σ|filed-negative child|` — which is
itself a derivation of A16's detector from A8's weight rule and explains why the detector is
exact rather than approximate. **Its power is zero for any subtree whose children all enter at
−1** (a pure-outflow section), which is a limit on A16 worth recording.

### 3.3 Flip-INVARIANT: the defect is present and invisible

Three ratios built from **two negative filed cells** are unchanged by the strip, because both
numerator and denominator move across zero together. They are **not sign-exposed** — and the
invariance is accidental, so a reader who assumes a negative ratio will be wrong in the
opposite direction.

| ratio | period | filed identity | filed | served | note |
|---|---|---|---|---|---|
| effective tax rate (tax expense / pre-tax income) | Q2 2026 | 5,327 / 43,931 | **+12.13%** | +12.13% | both cells negative → invariant |
| | H1 2026 / FY2024 / FY2023 | 3,535/90,745 · 764/189,411 · 3,650/178,921 | **3.90% / 0.40% / 2.04%** | same | |
| | FY2025 | (−27,688) / (−225,897) | **+12.26%** | +12.26% | a benefit on a loss → **NOT MEANINGFUL as a rate** |
| interest coverage (OI / interest expense) | Q2 2026 | (57,514) / (581) | **+98.99×** | +98.99× | both negative → invariant; **NOT MEANINGFUL** |
| | FY2025 | (228,838) / (26,489) | **+8.64×** | +8.64× | **NOT MEANINGFUL** |
| operating cash flow / net loss | H1 2026 / H1 2025 / FY2025 / FY2024 / FY2023 | 134,407/94,280 · 77,467/127,030 · 165,521/198,209 · 48,890/190,175 · 98,867/182,571 | **1.426 / 0.610 / 0.835 / 0.257 / 0.542** | same | both negative → invariant |

**Rule extracted: a DA-23 strip is invisible in any ratio whose numerator and denominator are
both negative in the filed record, and visible only where the filed denominator is positive.**
Interest coverage at RKLB is the instructive case: the platform's `+98.99×` and the filed
record's `+98.99×` are the same number and both are meaningless — a coverage ratio computed
from two negative numbers says nothing about the ability to cover interest. **A ratio that
survives the defect by arithmetic accident is not a validated ratio**, and the verdict
recorded here is NOT-MEANINGFUL, not CLEAN.

### 3.4 The one non-sign ratio error that is larger than the sign error

FY2025's served balance-sheet rows read the **prior-year comparative column**. The platform's
`Liabilities` row reports 801,889,000 where the current-year filed value is 602,624 (801,889 is
the December 31 2024 column); `AssetsCurrent` reports 692,621,000 where the filed current-year
value is 1,365,544 (692,621 is the 2024 column); and `InventoryNet` is reported at 119,074,000
against a current-year 158,407 — the third of the three, and the only one the platform flags,
at `status: warn`.

| ratio | from filed current-year cells | from the served (prior-year) column | relative error |
|---|---|---|---|
| current ratio, FY2025 | 1,365,544 / 334,476 = **4.083** | 692,621 / 334,476 = **2.071** | **−49.3%** |
| quick ratio, FY2025 | 1,207,137 / 334,476 = **3.609** | 573,547 / 334,476 = **1.689** | **−53.2%** |
| working capital, FY2025 | **1,031,068** | **353,096** | **−65.8%** |

**A ratio can be wrong by 49–66% at RKLB with no sign involved, and the platform's severity
tier for it is `warn`.** Any DA-23 clearance that reports RKLB "clean on signs" while quoting
a served balance-sheet ratio is reporting the smaller of the two errors.

### 3.5 `EPS × shares` as a sign test: measured inadmissible at n = 7

Served `NetIncomeLoss` divided by the served weighted-average shares outstanding, against the
served (and filed) EPS magnitude — cells from [RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32)
and [RKLB 10-K p.69](https://agentii.ai/v/RKLB/sec87/69):

| period | served NI / WASO | EPS magnitude | ratio | sign test result |
|---|---|---|---|---|
| Q2 2026 | 49,258,000 / 629,681,803 = 0.07823 | 0.08 | 0.978 | PASSES |
| Q2 2025 | 66,414,000 / 515,086,631 = 0.12893 | 0.13 | 0.992 | PASSES |
| H1 2026 | 94,280,000 / 617,625,210 = 0.15264 | 0.15 | 1.018 | PASSES |
| H1 2025 | 127,030,000 / 510,376,584 = 0.24890 | 0.25 | 0.996 | PASSES |
| FY2025 | 198,209,000 / 530,664,781 = 0.37353 | 0.37 | 1.010 | PASSES |
| FY2024 | 190,175,000 / 495,929,861 = 0.38346 | 0.38 | 1.009 | PASSES |
| FY2023 | 182,571,000 / 481,768,060 = 0.37896 | 0.38 | 0.997 | PASSES |

**7 of 7 periods reconcile inside ±2.2%, on a value that is stripped in 7 of 7.** The test's
detection power at RKLB is **zero**, measured, not argued. Per the contract rule
`data_integrity_register_applied`, `EPS × shares` is not used anywhere in this artifact; the
sign of every numerator above comes from the component identity of section 1. RKLB is the
issuer that supplies the evidence for the test's inadmissibility, and this is that evidence.

### 3.6 The MD&A percentage column is a second basis, and it does not fully reproduce

The filing prints its own margin column, so every ratio in 3.1–3.2 has **two filed bases**:
the printed percentage and the ratio of the printed dollars. Cells from
[RKLB 10-Q p.39](https://agentii.ai/v/RKLB/sec109/39). Cross-checking all 30 three-month lines,
the convention is **rounding to one decimal**; three lines violate it:

| line | printed | dollars recomputed | discrepancy |
|---|---|---|---|
| Q2 2026 net loss | **(21.1)%** | 49,258 / 234,066 = 21.044% | fails under **both** rounding (21.0) and truncation (21.0) — **0.06 pp, unattributable** |
| Q2 2025 total other income (expense) | **(2.6)%** | 3,837 / 144,498 = 2.655% | fails rounding (2.7), passes truncation |
| Q2 2025 net loss | **(45.9)%** | 66,414 / 144,498 = 45.961% | fails rounding (46.0), passes truncation |

**Residual disposition:** three of 30 presented ratios fail to reproduce from their own
component cells at the disclosed precision; maximum discrepancy 0.10 pp; direction mixed (two
toward zero, one away). **Attribution: none available — no registered defect covers a
presentation-layer rounding violation, and the magnitude is immaterial to every conclusion in
this artifact. Declared as a residual, not rounded away.** Per DA-29's terms test, all six
terms *are* filed (49,258 / 234,066 on p.6 and the percentages on p.39), so this is not a
back-solve; it is a reproducibility failure between two filed cells, which is the smallest
kind of failure this artifact recognises and still reports.

---

## 4. How `computed` and `reported` each fail — four rows, four resolutions, one filing

This is the mechanism section, and it is the reason the contract says `computed` may not be
cited as a derivation. All rows are `validate_calculation(0001819994-26-000062)`, Q2 2026, with
the filed comparand from [p.6](https://agentii.ai/v/RKLB/sec109/6).

| row | computed | reported | filed cell | which column is right |
|---|---|---|---|---|
| `OperatingIncomeLoss` | **−57,514,000** | +57,514,000 | **(57,514)** | **computed** — the children are sound, the parent is stripped |
| `NonoperatingIncomeExpense` | 18,227,000 | **13,583,000** | 13,583 | **reported** — two children stripped, parent sound |
| `GrossProfit` | 20,668,000 | **84,576,000** | 84,576 | **reported** — `computed` used two service members (19,110 + 1,558) instead of one consolidated concept → **−75.6%** |
| `NetIncomeLoss` | 38,604,000 | 49,258,000 | **(49,258)** | **NEITHER** |

**`OperatingIncomeLoss`** — exact strip: `diff` 115,028,000 = 2 × 57,514,000, and `computed` is
the value obtainable from the same linkbase the tool is reading.
**`NonoperatingIncomeExpense`** — `computed` = −581 + 16,486 + 1,954 + 368 = 18,227, where
`InterestExpenseNonoperating` served **+581** is *correct* at weight −1
(`InterestExpenseNonoperating` filed `(581)`, `w = −1`, contribution −581 ✓), while
`ForeignCurrencyTransactionGainLossBeforeTax` served **+1,954** (filed `(1,954)`) and
`OtherNonoperatingIncomeExpense` served **+368** (filed `(368)`) are **stripped** at weight
**+1**. Filed total: −581 + 16,486 − 1,954 − 368 = **13,583** ✓. `diff` 4,644,000 = exactly
2 × (1,954 + 368) — and the row's `status` is **`warn`**, not fail. This single row contains
the MSFT control case and two true positives in one subtree: a naive sign test would call
`InterestExpenseNonoperating` a false positive, and the weight rule separates it exactly.
**`GrossProfit`** — `reported` is the filed value; `computed` is a **member substitution**, with
a measured magnitude of −75.6%.
**`NetIncomeLoss`** — `computed` = 43,931 − 5,327 = 38,604, a number that is neither the filed
magnitude (49,258) nor the filed signed value (−49,258). **Correction to the natural reading of
this row, recorded because the natural reading is wrong:** `diff` = 10,654,000 = 2 × 5,327,
which invites "the tax term was stripped." It was not. The served
`IncomeTaxExpenseBenefit` **+5,327 is correct** — the filing shows "Provision for income taxes
(5,327)", an expense, whose contribution to the loss is −5,327, and the arc is −1. The failure
is the pretax child (served +43,931 where the arc needs −43,931 → error 2 × 43,931 = 87,862,
and −49,258 + 87,862 = 38,604 ✓), and the `diff` equalling 2 × tax is an algebraic consequence
of `reported` being the *mirror* of the true value: with `reported` = −T and `computed` =
T + 2|C|, `diff` = 2(|T| − |C|) = 2 × the sum of the correctly-signed children. **Generalised:
`diff` is exact in both regimes but means opposite things — when the parent is sound,
`diff` = 2 × Σ|stripped child|; when the parent is mirrored, `diff` = 2 × Σ|correctly-signed
child|. The register's "2 × the stripped term" is the first regime only.** RKLB supplies both,
in one filing, in adjacent rows.

**The balance-sheet control.** Every arc into `Assets` is **+1** (section 0), so **no
sign-strip is possible in that subtree**, and the residual there cannot be DA-23. It is
nonetheless non-zero: Q2 2026 `Assets` computed 3,875,532,000 against a filed 4,187,374,000 —
**short by 311,842**, with `PropertyPlantAndEquipmentNet` computed 110,255,000 (filed 393,946),
`IntangibleAssetsNetExcludingGoodwill` computed 401,719,000 (filed 320,415, and *over*, not
under), and the remainder **109,455 unattributed**. The filed children sum to the total exactly
(2,895,759 + 393,946 + 320,415 + 299,072 + 113,690 + 12,349 + 85,405 + 8,413 + 1,057 + 57,268 =
4,187,374 ✓), so the tool's child set is wrong and it discloses no selection field. **Disposition:
UNRESOLVABLE-FROM-PLATFORM, recorded as the artifact's `unresolvable_class`.** The same shape
recurs at FY2025 (`Assets` 1,616,464 against 2,324,478; `PropertyPlantAndEquipmentNet`
110,255 with a negative `−40,255`-class computed net carrying accumulations through a −1 arc
whose magnitude the tool does not expose).

---

## 5. The six-defect census

### 5.1 DA-23 — sign inversion. **Verdict: PRESENT AND MEASURED, 7 of 7 periods.**

Served `OperatingIncomeLoss` and `NetIncomeLoss` are positive magnitudes of identical absolute
value to the filed negatives in every period tested. **RKLB is confirmed as one of the six
loss-making issuers in the register's 6-of-6 census.** Ratios reaching it: 3.2 (all of them).
Ratios immune: 3.1. Ratios surviving by accident: 3.3. Detectors exercised: strip (exact, 4
rows), overshoot (exact, 2 rows), self-reference (exact, 2 rows, **new**), member substitution
(exact, 2 rows), comparative-column mis-selection (exact, 3 rows), duration mixture (1 row).
**Refinements recorded: (i) the strip is invisible in any ratio whose numerator and denominator
are both negative; (ii) the weight discriminator is powerless at weight −1 for a bidirectional
concept; (iii) `diff` has two exact regimes with opposite meanings.**

### 5.2 DA-24 — non-operating contamination of an operating subtotal. **Verdict: UNEVIDENT as to magnitude; the one testable sub-claim is CLEAN.**

Testable and tested: `R&D + SG&A = total operating expenses` closes **exactly in 7 of 7
periods** (section 1, identity B), so no unallocated non-operating item sits between the
selling line and the total. Disposals are verified **below** the operating line: the
helicopter gains sit in other income ($2,825 in 2024, $1,094 in 2023,
[RKLB 10-K p.90](https://agentii.ai/v/RKLB/sec87/90)), and H1 2026 shows "(Gain) loss on
disposal of assets (403)" inside operating cash flow only
([RKLB 10-Q p.8](https://agentii.ai/v/RKLB/sec109/8)).

Unevident and declared: the line is labelled **"Research and development, net"** — a contra sits
inside it and its magnitude is disclosed nowhere in the filing's face. DA-24's registration is
about contamination of the operating subtotal, and a *net* R&D line is exactly the
compositional lead DA-24 predicts, but **this artifact can test only existence, not
magnitude.** Verdict **UNEVIDENT (magnitude)**, not CLEAN. This is a
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` residual, distinct from the platform-side class in the
frontmatter; both classes are live in this artifact and the frontmatter records the dominant
remedy.

### 5.3 DA-25 — normalised per-launch metric versus audited segment basis. **Verdict: REPRODUCED, and it is 4 of 4 periods, not 1.**

The registered instance is Q2 2026. Both bases, cells from
[p.37](https://agentii.ai/v/RKLB/sec109/37) and [p.32](https://agentii.ai/v/RKLB/sec109/32):

| period | issuer normalised margin, (rev/launch − cost/launch) / rev/launch | audited segment margin, Launch Services GP / revenue | gap |
|---|---|---|---|
| Q2 2026 | (9.1 − 4.4) / 9.1 = **51.65%** | 19,110 / 44,586 = **42.86%** | **8.79 pp** |
| Q2 2025 | (7.9 − 5.0) / 7.9 = **36.71%** | 14,220 / 46,646 = **30.48%** | **6.23 pp** |
| H1 2026 | (9.2 − 4.9) / 9.2 = **46.74%** | 47,333 / 108,249 = **43.73%** | **3.01 pp** |
| H1 2025 | (7.5 − 5.3) / 7.5 = **29.33%** | 21,437 / 82,238 = **26.07%** | **3.26 pp** |

**Extension of the registered finding: DA-25 is not a single-instance artefact at RKLB; it
reproduces in 4 of 4 periods, always in the same direction (the normalised metric flatters),
with gaps of 3.0–8.8 points.** The mechanism is in the issuer's own definition — revenue per
launch is "the average transaction price attributable to launch contract performance
obligations during the period in which the launch occurs, **regardless of whether the revenue is
recognized using the point-in-time or over-time method**" — so the metric is a transaction-price
basis and the segment table is a recognised-revenue basis. The component identity that fails,
with the residual named: 9.1 × 6 missions = **54,600** against filed Launch Services revenue
**44,586**, residual **10,014 (22.5%)**, cause disclosed by the filing (two of the six Q2 2026
missions were HASTE, recognised over time, partially in prior quarters); H1 2026: 9.2 × 12 =
110,400 against 108,249, residual 2,151 (2.0%). **The segment table governs every margin claim
in this artifact**, per the register's remedy; the issuer metric is reported only here, beside
it.

### 5.4 DA-26 — annual figure served at a quarterly label. **Verdict: CONFIRMED twice.**

The served store returns **601,799** as a `Q4` fiscal-period fact for FY2025 revenue and
**436,214** for FY2024 — both of which are the **annual** totals ([RKLB 10-K p.69](https://agentii.ai/v/RKLB/sec87/69)),
not fourth-quarter figures. Two instances, both annual-as-quarterly. No ratio in section 3
rests on a Q4-labelled served fact.

### 5.5 DA-27 — fiscal-period label offset. **Verdict: NOT-TESTABLE — kind 4, mechanism-population identity. EXCLUDED FROM THE DENOMINATOR.**

DA-27's population is issuers whose fiscal-year label diverges from the calendar; its own
registration records n = 4 of 4 partitioning that population, and every December-year-end
issuer in the universe shows **no** offset. RKLB has a **December 31 year-end** —
the balance sheet dates, the 10-K cover period, and the cash-flow beginnings and ends
(275,302 → 833,545 → 2,137,898) are all calendar-aligned. **The precondition is absent, so the
mechanism cannot occur, and the verdict is NOT-TESTABLE of the mechanism-population kind, which
is NOT the same as CLEAN and is not counted as a pass.** Reporting RKLB "clean on DA-27" would
be exactly the error the register's margin-conditioned-power rule forbids.

**A DA-27-adjacent defect is nonetheless present and is reported under its own name.** The
platform's period label `Mon Jun 30 2025` does not disambiguate the three-month from the
six-month window, and one row **mixes them**: `NetIncomeLoss` `reported` 127,030 (the H1 2025
figure) against `computed` 60,538 (= 63,476 − 2,938, the Q2 2025 quarter), `diff` 66,492 — a
**duration artefact, not a strip**, and identified as such because 66,492 is not 2 × any filed
negative term. The same class of error appears at `OperatingExpenses` in the FY2025 comparative:
`computed` 145,353 = 66,134 (Q2 2025 R&D, three months) + 79,219 (H1 2025 SG&A, six months)
against a filed three-month 106,027 ([p.6](https://agentii.ai/v/RKLB/sec109/6)). **Both are
duration mixtures inside the row's child set.** The served store *does* hold a correct
three-month `OperatingExpenses` = 106,027,000 from `rklb-20250630.htm`, so this is a selection
failure in the current accession's row, not a corruption of the prior-year fact — recorded as a
self-correction to the naive reading that the prior-year quarter is missing.

### 5.6 DA-28 — IPO capital-structure discontinuity. **Verdict: the registered failure mode is UNEXERCISED; the discontinuity itself is PRESENT and carried as a basis problem.**

DA-28 warns that "a thesis screening for DA-23 by EPS reconciliation will produce false
positives on recent listings", and records that KRMN and VOYG passed cleanly only because both
had already reported a full post-IPO quarter while HAWK had not. **At RKLB the registered
failure mode does not reproduce, and the measured failure is the opposite: a false NEGATIVE in
7 of 7 periods** (section 3.5). RKLB had reported many full post-IPO quarters before the tested
periods — SEC coverage is 83 filings and the served corpus reaches the SPAC/pre-IPO filings —
so **DA-28 as registered is UNEXERCISED for these periods; it has no power here in either
direction, and it is not credited as a pass.**

The discontinuity it warns about is nonetheless live, and it produces the artifact's largest
multi-basis set: shares **issued** 639,131,688 against **outstanding** 598,180,438 (the
40,951,250 difference is the preferred stock held as treasury — and it reconciles exactly:
639,131,688 − 598,180,438 = 40,951,250 = the preferred balance, and 589,525,802 − 543,574,552 =
45,951,250 at the prior date ✓); an ATM that raised 1,529,639 in six months
([p.8](https://agentii.ai/v/RKLB/sec109/8)); a 5,000,000-share preferred conversion completed
May 26 2026 ([p.33](https://agentii.ai/v/RKLB/sec109/33)); and **23,154,465 anti-dilutive shares**
(options+RSUs 13,095,520 + convertible-note shares 2,607,745 + collared forward 7,451,200,
[p.32](https://agentii.ai/v/RKLB/sec109/32)). Per A3's generalisation this is a **DA-30 basis
problem here, not a detector-validity problem**, and it is handled in section 8.

### 5.7 Cross-holding (queued DA-31). **Verdict: UNEVIDENT — kind 4, mechanism-population identity. NOT CLEAN.**

The June 30 2026 balance sheet carries **no equity-method or unconsolidated-investment line** —
all ten non-current asset children are PP&E, intangibles, goodwill, two ROU assets, marketable
securities, restricted cash, a deferred tax asset and other
([p.5](https://agentii.ai/v/RKLB/sec109/5)). [p.33](https://agentii.ai/v/RKLB/sec109/33) states
in terms that "as of June 30, 2026 and December 31, 2025, there are no amounts due to or from
related parties", and no business-combination note records a retained minority interest. Keyword
searches for an equity-method holding return zero hits — **and a zero from
`search_keyword_in_source` is not evidence that the filing lacks the concept; it is evidence
about the search.** The method used to establish the absence is the filed cell set: the balance
sheet's assets are fully accounted for by the ten children above, which close to the total
exactly (section 1), so **there is no room in the filed balance sheet for an unconsolidated
investment of material size.** That is a stronger statement than the keyword zero and it is the
one this artifact makes.

**The MSFT precedent is recorded as the reason a nil result must not be read as clean:** at MSFT
the cross-holding mechanism was **not appreciation** but a **dilution gain recognised as the
stake FELL** (HLBV), 3.71% of net income — a mechanism that leaves no equity-method line at all
in the periods where the stake is being diluted. **RKLB's Iridium transaction is exactly the
shape in which such a mechanism could appear later** (a $3.6B bridge, an all-stock component
evidenced by "common stock in acquisition 160,802" in the H1 2026 non-cash disclosures), so the
verdict is UNEVIDENT with the mechanism named, not CLEAN.

---

## 6. DA-29 — the terms of every reconciliation in this artifact

Every term used above is a numerical cell read from a named page of a named filing: sec109
pp. 5, 6, 8, 32, 33, 37, 39; sec87 pp. 68, 69, 71, 90, 107. **No `computed` column is used as a
derivation anywhere**, and no term is back-solved. Two platform rows that **close exactly while
being wrong** are decomposed rather than passed:

- **FY2025 `NetIncomeLoss`: `status: pass`, `diff: 0`, computed = reported = 198,209,000, filed
  (198,209).** Both columns hold the same sign-inverted value. The mechanism is not two strips
  cancelling: applying the arc weights (+1 pretax, −1 tax) to two children that are independently
  sign-inverted reproduces **the mirror of the true value** exactly: 225,897 − 27,688 = 198,209 =
  −(−198,209). **Sub-class named: IDENTICAL-MIRROR PASS.** It is not a back-solve (every term is
  filed) and cannot be caught by the terms test; it can only be caught by the component identity
  (section 1, identity D) or by the weight rule with the filed presentation of the tax line. This
  is a **second, mechanically distinct route to the SATS outcome** (`pass` on a wrong-signed
  value), and it strengthens the register's claim that `validate_calculation`'s `reported` column
  "is constitutively incapable of detecting a strip": here it does not merely share a stripped
  store, it agrees with a corrupted `computed`.
- **Q2 2026 `ComprehensiveIncomeNetOfTax`: computed = reported = 54,863,000, `status: pass`,
  while the filed cell is (54,863)** — the A14 instance, reproduced exactly. Its three children
  (`NetIncomeLoss` +1, FX OCI +1, unrealized OCI +1, all at weight +1) are all sign-inverted, so
  the pass is again an identical mirror: 49,258 + 5,358 + 247 = 54,863 = −(−54,863) ✓.
- **Q2 2026 `NetIncomeLoss`: three distinct numbers** (computed 38,604 / reported 49,258 / filed
  −49,258) with a `diff` of 10,654 that is exact but attributes to the *wrong* term (section 4).
- **`validate_calculation` returning ZERO ROWS** for a filed concept: the register's VRT case
  (`UNVALIDATED-BY-PLATFORM`) has its analogue here at the fact level —
  `RetainedEarningsAccumulatedDeficit` returns **zero rows** for RKLB while the balance sheet
  line reads (1,106,190). Recorded `UNVALIDATED-BY-PLATFORM`; never recorded as a pass.

---

## 7. Residual dispositions, exhaustively

| residual | class | discharged by |
|---|---|---|
| served `OperatingIncomeLoss` and `NetIncomeLoss` positive in 7/7 periods | **STRIP**, DA-23 | section 2; exact 2 × signature |
| `NonoperatingIncomeExpense` 4,644 = 2 × (1,954 + 368) | **STRIP** (two children) | weight rule at +1 vs the licensed −1 child |
| net-change rows 1,026,056 and 438,100 | **OVERSHOOT** = 2 × Σ\|filed-negative child at +1\| | derived from the arc weights |
| lease-payment rows 49,220 / 24,610 and 252,818 / 126,409 | **SELF-REFERENCE** (computed = 2 × reported, diff = reported) | new signature, stated |
| `GrossProfit` FY2024 reported 81,559 = the Space Systems **segment** value; Q2 2026 computed 20,668 = two service **members** | **MEMBER SUBSTITUTION** | −75.6% at Q2 2026, measured |
| `Liabilities` 801,889 vs 602,624; `AssetsCurrent` 692,621 vs 1,365,544; `InventoryNet` 119,074 vs 158,407 | **COMPARATIVE-COLUMN MIS-SELECTION** (FY2025) | ratio error 49–66%, section 3.4 |
| `NetIncomeLoss` 127,030 vs computed 60,538; `OperatingExpenses` 145,353 | **DURATION MIXTURE** | quarter + half-year children in one row |
| `Assets` short 311,842; PP&E computed 110,255; intangibles net 401,719; 109,455 unattributed | **SELECTION, not sign** (all arcs +1) | **UNRESOLVABLE-FROM-PLATFORM** |
| `IncomeTaxExpenseBenefit` FY2025 served +27,688 against a filed benefit | **STRIP at weight −1, bidirectional concept** | presentation test; extends A17 |
| `DeferredTaxAssetsNet` residual 120,122 = 2 × 60,061 | **PARTIALLY ATTRIBUTED** | 60,061 is valuation-allowance magnitude; identity unconfirmed without the tax note → **declared UNRESOLVED**, not rounded |
| `IncomeLossFromContinuingOperations` diff 27,166 = 2 × 13,583 | **ATTRIBUTED** | the other-income child |
| MD&A percentage column, 3 of 30 lines | **PRESENTATION LAYER** | **UNATTRIBUTED**; max 0.10 pp |
| FY2025 `GrossProfit` computed 80,776 (nearest filed cell: Launch segment GP 81,270, residual 494); `IncomeTaxExpenseBenefit` FY2025 deferred components 33,826 / 30,406 with a 3,420 warn-level `diff` | **UNATTRIBUTED** | declared; not rounded |
| R&D "net" contra magnitude | **DA-24, UNEVIDENT** | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| valuation ratios (P/E, EV/EBITDA, P/B, PEG) | **UNEXERCISED** | Market Data Stage `none` — no verdict issued |

---

## 8. DA-30 — the basis is named for every multi-basis concept

| concept | bases found at RKLB (all filed) | basis used here |
|---|---|---|
| gross profit | consolidated **84,576** · segment total 19,110 + 65,466 = 84,576 · product 63,908 · service 1,558 + 19,110 = 20,668 | **consolidated**, and the product/service split is shown where used |
| operating income | consolidated **only** — "Management does not regularly review either reporting segment's total assets or operating expenses" ([p.33](https://agentii.ai/v/RKLB/sec109/33)) closes the segment basis by the issuer's own statement | consolidated |
| share count | issued 639,131,688 · outstanding 598,180,438 · basic WASO 629,681,803 · diluted = basic (23,154,465 excluded as anti-dilutive) | named at every use; BVPS shown on both issued and outstanding |
| deferred tax | tax note 30,406/30,667 vs cash-flow 30,406 | tax-note basis, cash-flow basis shown |
| liquidity | cash 2,129,485 · cash + restricted 2,137,898 · cash + all marketable securities 2,387,590 · the issuer's own "$2.1B cash and $258.1M marketable securities" ([p.44](https://agentii.ai/v/RKLB/sec109/44)) | all four; the issuer's $258.1M reconciles **exactly** to 172,700 + 85,405 = 258,105 ✓ |
| EBITDA | OI + D&A (cash-flow D&A) · the same with SBC added | both, labelled |
| runway | 8.88 years at the H1 2026 burn (134,407 × 2 against 2,387,590) · 14.42 years at the FY2025 burn (165,521) | both, and **pre-Iridium basis only** |
| every forward ratio | pre-close · post-close ($3.6B bridge, $54/share, ~$8.0B EV) | `standalone_pre_merger`; the post-close basis is **not computable from this filing** and is flagged, not modelled |

**A basis difference can be exactly compensating and invisible to `validate_calculation`** (the
VRT case: $134.9M–$183.6M annually across 7 of 7 periods). The detector is **line-level**. Two
line-level instances at RKLB: the `GrossProfit` member substitution (a different line, not a
different total, and the total still closes because the segment sum equals the consolidated
figure) and the two deferred-tax figures in one filing (30,406 vs 30,667 — 261 apart, below any
total-level tolerance). Both were found by reading cells, not by any closure test.

---

## 9. What this artifact does to PIL-5's falsifier

PIL-5's `wrong_if` is `metric = share_of_001_headline_figures_converted_to_DEMONSTRATED`,
`op = <`, `threshold = 0.5`, `source = validation_ledger`. **The denominator is UNSTATED**, and
this artifact supplies evidence bearing on it:

1. **The ceiling.** thesis.md's Phase 7 pre-finding enumerates 001's **six** headline figures,
   three of which (the two $/kg-class and the two m²/MW-class values plus the dollars figure)
   are marked UNRESOLVABLE and one of which is UNRESOLVABLE at 1.69×. If the denominator is all
   six, **at most three can convert, so the share's ceiling is exactly 0.50 and the falsifier is
   met with zero margin** — a single further unresolvable figure falsifies the pillar. If the
   denominator is the four *value* figures, the ceiling is 0.75. **The artifact therefore reports
   that the pillar's verdict is determined by a denominator that is not written down anywhere**,
   and that this is itself a P5 finding.
2. **A possible second denominator.** PIL-7's table row reads
   `PIL-5 | PENDING — terrestrial denominator is commercially licensed`, which attaches a
   *different* denominator to PIL-5. If that is the operative denominator, the falsifier's metric
   is not the one defined at PIL-5 and the two must be reconciled before Phase 7 can score it.
   Recorded as an observation on the unstated denominator, not as a resolution.
3. **What this artifact contributes to the metric.** The metric asks how many 001 figures convert
   to `DEMONSTRATED`. This artifact supplies the **method** by which any ratio input can qualify:
   recomputable from filed components with the identity shown in-line. It also demonstrates the
   one figure class whose conversion **cannot** be achieved by a platform read — the operating
   income of a loss-making issuer — because the served subtotal is sign-inverted while the served
   components are sound. **So for the loss-making issuers, `DEMONSTRATED` requires component
   recomputation, and a ledger that counts platform reads as conversions will over-count by
   construction.**

---

## 10. Corrections and extensions to the register and to 001

**001 is frozen and is not rewritten.** The following are recorded as corrections to be carried
in Phase 7's ledger, per the rule to validate 001's facts rather than repeat its questions:

1. **001's DA-23 census stands at RKLB and is extended**: RKLB is confirmed (7 of 7 periods), and
   three further exact signatures are added (self-reference; identical-mirror pass; duration
   mixture). The register's claim that `validate_calculation`'s `reported` column "is
   constitutively incapable of detecting a strip" is **strengthened**, with a second mechanism
   (the FY2025 `pass` where computed and reported are the *same* corrupted value).
2. **A9's dichotomous statement of the segment-substitution condition is falsified as a complete
   statement.** A9 predicts silence where nothing is unallocated and overstatement where
   something is. RKLB Q2 2025 shows a third case: **single-member substitution**, where the
   validator picks one dimensional member and **understates by 69.4%** (reported 14,220 against a
   consolidated 46,388; the members reconcile exactly, 14,220 + 32,168 = 46,388 and
   31,033 + 1,135 = 32,168 ✓, so nothing is unallocated). **The served store also holds no
   undimensioned `GrossProfit` fact at all for the Q2 2025 comparative quarter** — the
   consolidated value exists only on the statement face — and it holds one member fact with
   `value_numeric: null`. A total-based screen cannot see any of this; the line-level detector
   can.
3. **A8/A17 directionality, completed.** The weight discriminator licenses a positive magnitude
   at weight −1 and therefore cannot certify; and it is powerless on **bidirectional** concepts,
   whose direction flips across periods under a fixed weight. RKLB supplies the counterexample
   pair for a single concept (`IncomeTaxExpenseBenefit`: correct in Q2 2026, stripped in FY2025)
   and the identity of the bidirectional set in this issuer.
4. **A16's overshoot detector is a corollary of A8**, derived here: the residual is exactly
   `2 × Σ|filed-negative child entering at weight +1|`, which is why it is exact and why it has
   **zero power** in a subtree of pure weight-−1 children.
5. **A11's freshness contradiction, reproduced**: `data_freshness: 2027-04-12` appears on the
   XBRL surfaces, `read_source_pages` and `get_ticker_coverage` alike, while every RKLB coverage
   tier reads `missing` although seven of seven sources are populated (83 SEC filings, 22,293
   XBRL facts, 26 earnings-calendar records, 19 transcripts, 27 institutional-holdings records,
   53 insider trades, 106 documents). Recorded as a platform-metadata contradiction; no ratio in
   this artifact depends on a freshness field.
6. **The description-field contamination vector, reproduced.** A `search_keyword_in_source`
   hit for "Iridium" on sec109 returned **page 53** — an RKLB exhibit index whose merger
   counterparty is Iridium — with the description-field keywords "Mercury Systems", "MRCY" and
   "merger agreement" attached to it, re-confirmed this session. (The field is the same
   LLM-generated description `read_source_outline` serves, and the contract records that
   `search_keyword_in_source` matches on it: "confirm via `read_source_pages`" is necessary but
   not sufficient.) Every table page in this artifact is therefore cited by **cells**, never by a
   sentence about the table, which is also why the MD&A percentage column in 3.6 is quoted as
   cells.
7. **The linkbase label field is a second fabrication vector, twelve years stale.** The
   `StockholdersEquity` role's labels carry "Preferred Stock; 5,000 shares authorized; no shares
   issued and outstanding at December 31, 2014 or 2013" and "Common Stock … 14,824 shares issued
   and outstanding at December 31, 2014 … 12,644 shares … at December 31, 2013", and the PP&E
   label reads "net of $32,412 and $28,145" against a filed accumulated depreciation of
   (90,865)/(65,585) at the dates tested — figures that match no period in this artifact.
   **A figure recovered from a label is as fabricated as one recovered from an LLM description**,
   and it differs from the filed cell by four orders of magnitude on the authorized-share count
   (5,000 vs 100,000,000). Recorded as extending the rationale of
   `table_pages_quote_cells_not_prose` beyond the description field.

---

## 11. What could not be verified, and why

- **Post-close ratios.** The Iridium transaction's completion and its purchase accounting are
  not determinable from the June 30 2026 filing; every forward ratio here is
  `standalone_pre_merger` and the post-close basis is declared uncomputable, not modelled.
- **The R&D contra magnitude.** The "net" label establishes that a contra exists; the filing
  discloses no amount. `UNRESOLVABLE-FROM-PUBLIC-SOURCES`.
- **The balance-sheet selection residuals** (Assets short 311,842; PP&E computed 110,255;
  intangibles net 401,719; 109,455 unattributed). Their arcs are all +1, so they are not sign
  errors; the platform exposes no selection field, so what the tool chose cannot be recovered.
  `UNRESOLVABLE-FROM-PLATFORM` — the artifact's recorded class.
- **`RetainedEarningsAccumulatedDeficit`** returns zero rows from a concept-keyed query, so the
  sign of the served accumulated deficit could not be established from the store. The equity
  denominator was established from filed cells instead; the store's own 2024-12-31 equity total
  (382,453) is **CORRECT** — 50 + 1,198,909 − 813,701 − 2,805 = 382,453 ✓ — so **no
  mis-tagging claim is made anywhere in this artifact.**
- **The deferred-tax residual 120,122** (= 2 × 60,061). Of valuation-allowance magnitude;
  the tax note's identity could not be confirmed from the pages read, so it is **declared
  UNRESOLVED**, not attributed.
- **Valuation ratios.** Market Data Stage `none`. `UNEXERCISED`.
- **DA-27 and DA-28 as registered.** Precondition absent and precondition over-satisfied
  respectively; both **NOT-TESTABLE / UNEXERCISED** and neither counted as a pass.

---

## Sources

| figure | page |
|---|---|
| Q2 2026 statement of operations, comprehensive loss, EPS, WASO | [RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6) |
| Balance sheet cells, both dates, share counts | [RKLB 10-Q p.5](https://agentii.ai/v/RKLB/sec109/5) |
| Six-month cash-flow cells and non-cash disclosures | [RKLB 10-Q p.8](https://agentii.ai/v/RKLB/sec109/8) |
| MD&A results of operations, dollar and percentage columns | [RKLB 10-Q p.39](https://agentii.ai/v/RKLB/sec109/39) |
| Segment tables, net loss attributable, WASO, anti-dilutive shares | [RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32) |
| Revenue disaggregation; no segment opex or assets reviewed; related-party nil | [RKLB 10-Q p.33](https://agentii.ai/v/RKLB/sec109/33) |
| Revenue and cost per launch, metric definitions, cadence | [RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37) |
| Liquidity ($2.1B cash, $258.1M securities); Iridium $54/share, ~$8.0B EV, $3.6B bridge | [RKLB 10-Q p.44](https://agentii.ai/v/RKLB/sec109/44) |
| FY2025 balance sheet cells, both years | [RKLB 10-K p.68](https://agentii.ai/v/RKLB/sec87/68) |
| FY2025/2024/2023 income statement cells, tax benefit, EPS, WASO | [RKLB 10-K p.69](https://agentii.ai/v/RKLB/sec87/69) |
| FY2025/2024/2023 cash-flow cells | [RKLB 10-K p.71](https://agentii.ai/v/RKLB/sec87/71) |
| Inventories, PP&E gross and accumulated depreciation, helicopter gains | [RKLB 10-K p.90](https://agentii.ai/v/RKLB/sec87/90) |
| Segment revenue, cost, gross profit by segment and by product/service | [RKLB 10-K p.107](https://agentii.ai/v/RKLB/sec87/107) |

**Machine-readable supplements** (tool outputs, not page-citable, and never used as a
derivation): `get_calculation_tree(0001819994-26-000062)` for the arc weights in section 0;
`validate_calculation` on accessions `0001819994-26-000062` (24 rows: 8 pass / 1 warn / 15 fail)
and `0001819994-26-000013` (29 rows: 5 pass / 5 warn / 19 fail) for the row-level signatures in
sections 4 and 7; `search_xbrl_facts` for the served values in section 2. **The skill pin is
computed, not guessed:** `2d27c7f751fa`, from `skill_version_hash` at `scripts/dispatch.py:132`
(sha256 over `sorted(skill_dir.rglob("*"))`, files only, update `p.name` then `p.read_bytes()`,
first 12 hex), on `plugins/vertical-plugins/quantitative-analysis/skills/agentii/ratio-analysis`.
**The base was validated against all six pins in `theses/001-technology-baseline/reproduce.md`
before any hash was taken — 6 of 6 reproduce** (operational-kpi `0730fd170124`, unit-economics
`e87ee63269a2`, secular-trends `e6b41dbb2426`, supply-chain `8cb3ac1de486`, competitive
`826995c722a4`, risk `953fc5d396e7`). The four `packaging/targets/` trees
(`claude-code`, `codex`, `generic-cli`, `cowork`) hold decoy copies of every skill and **all four
fail all six known hashes**; a second `ratio-analysis` copy under `models-and-pitches` hashes
`9b1d7a504789` and is not the canonical skill.
