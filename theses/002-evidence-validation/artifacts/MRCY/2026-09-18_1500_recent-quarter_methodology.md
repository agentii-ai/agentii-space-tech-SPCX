---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: MRCY
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07d26b9c738b"  # Pin of record: theses/002-evidence-validation/skill_pins.jsonl, TWO records (2026-09-18T16:23:35+08:00 and the cross_root_confirmation append), both `07d26b9c738b`. `recent-quarter` is absent from the six-row table in theses/001-technology-baseline/reproduce.md — that table's own note says remaining skills "hash on first use and are APPENDED to skill_pins.jsonl", which is what happened. HONEST LIMIT: the recorded derivation path (`skill_version_hash` at scripts/dispatch.py:132, hashing plugins/agent-plugins/agentii-equity-agent/skills/agentii/recent-quarter and plugins/vertical-plugins/equity-research-core/skills/agentii/recent-quarter) does NOT exist in this workspace — `scripts/dispatch.py` is absent and there is no `plugins/` root at all. I therefore verified the RECORD, not the hash. It is not UNRESOLVED (a hash does exist in-repo) and it is not independently recomputed.
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "CONFIRMED, and it REFUTES the clean verdict this thesis was pointed at. The component identity (`gross profit − opex = operating income`) was run IN-LINE on all 13 filed periods MRCY presents, with every component cell quoted from the statement face: 13 of 13 close to the dollar, and the five-line opex sub-stack closes 13 of 13 as well. The identity is not merely a convention here — it is the filer's OWN linkbase arc (`OperatingIncomeLoss` ← `GrossProfit` weight 1, `OperatingExpenses` weight −1). It proves the VALUES are internally consistent and proves nothing about the SIGNS: 11 of the 13 filed periods are LOSSES served as positive magnitudes, and the only 2 served values that are correct are the only 2 filed-POSITIVE periods (Q3 FY2026 +5,230 and FY2026 +280). 001 tested exactly one of those two periods and cleared the issuer on it. The mechanism is per-VALUE-SIGN, not per-issuer and not per-concept: within the single table on sec203 p.4, `Other (expense) income, net` is served stripped in three columns and correct in the fourth (the only positive, 2,304). Component level is also CONFIRMED, on three concepts, with the exact strip signature `diff = 2 × value` reproducing at 2 × 48,000 = 96,000. `EPS × shares` was not used and is inadmissible."
  - da_id: "DA-24"
    chosen_reading: "REFUTED as to a gain inflating the operating line — and the disposal at MRCY lands on the operating line with the OPPOSITE SIGN, which is a DA-24 variant worth registering. The filer's linkbase gives the operating line exactly seven inputs (GrossProfit, and the five opex lines rolling into OperatingExpenses); no disposal-gain concept is among them. All disposal PROCEEDS sit in investing (Cicor sale, $6,246, FY2025). The only disposal-related amount inside the operating line is a COST: sec205 p.33 states fiscal 2025 acquisition costs 'included $1.4 million related to the sale of our manufacturing operations in Switzerland and the associated supply agreement with Cicor Group'. So the disposal made fiscal 2025's operating loss LARGER by 7.13% — a disposal-neutral comparator would IMPROVE FY2025 and therefore make 001's supposed collapse smaller still. Max |operating income| / revenue across the 13 periods is 17.69% (FY2024), against 4.6x for the SATS instance."
  - da_id: "DA-25"
    chosen_reading: "REFUTED, with positive evidence rather than absence of search. The filer enumerates exactly four non-GAAP measures on sec203 p.35 (adjusted EBITDA, adjusted income, adjusted EPS, free cash flow) and NONE is a per-unit metric — there is no per-system, per-program or per-launch denominator anywhere in scope. Both non-GAAP reconciliations are fully reproducible from filed line items: the adjusted-EBITDA bridge (sec203 p.36) closes on 4 of 4 columns and the adjusted-income bridge (sec203 p.37) closes on 2 of 2 periods, every one of their 10 and 12 terms located on the pages cited. Adjacent hazard recorded, and it is a DA-23 interaction rather than a DA-25 instance: for the SAME nine months the GAAP basis is a loss of $(30,471) / $(0.51) per share while the non-GAAP basis is adjusted income of $41,416 / $0.68 per share — opposite signs — and the platform serves the GAAP figure sign-stripped, so the two now read as concordant positive measures."
  - da_id: "DA-26"
    chosen_reading: "CONFIRMED, and the magnitude is new. Three platform metrics rows carry ANNUAL revenue under a quarter label: fiscal_year 2026 / fiscal_period Q2 revenue 983,622,000; 2025 / Q2 912,020,000; 2024 / Q2 835,275,000. Each value equals the filed ANNUAL column to the dollar (sec205 p.47), so the defect is the LABEL, not the content. Ratio of the served value to the quarter the label names: 983,622 / 232,872 = 4.22x (FY2026) and 912,020 / 223,125 = 4.09x (FY2025). The generalisation, and it is testable: the contamination magnitude is set by whether the issuer files a Q4 10-Q. MRCY does NOT, so its year-end row carries the ANNUAL (4.1-4.2x); an issuer that does would carry the quarter and show a label-only defect at ~1x. MRCY is therefore the high-magnitude pole of this DA."
  - da_id: "DA-27"
    chosen_reading: "CONFIRMED, and the strongest instance recorded in this phase because the platform contradicts ITSELF rather than merely contradicting the issuer. Three independent served artefacts disagree: (a) get_company_fiscal_calendar gives `fiscal_year_end_month: 6` from `gold_companies` with `cross_validation_hint: null` and a grid in which 'FY2026 Q4' = 2026-04-01 to 2026-06-30; (b) MRCY's filed fiscal 2026 runs 2025-06-28 to 2026-07-03 (53 weeks) and its third quarter ended 2026-03-27; (c) get_calculation_tree returns `fiscal_period: \"Q1\"` for the 10-Q whose report_date is 2026-03-27 — while the platform's OWN grid places 2026-03-27 in FY2026 Q3. So the served quarter label is two quarters off the issuer AND two quarters off the platform's own calendar. Separately, `search_sec_filings` `year_q_no` tracks the CALENDAR year of the report date, so the Q1 and Q2 FY2026 10-Qs are both served under fiscal year 2025. The fiscal-year end date 2026-07-03 falls outside the platform's FY2026 grid entirely and into platform FY2027 Q1."
  - da_id: "DA-28"
    chosen_reading: "REFUTED — MRCY is a clean comparator on the capital-structure axis, and the test is worth stating because the denominator is unusable for a different reason entirely (DA-30). Filed weighted-average shares rise monotonically from 57,105 thousand (Q1 FY2024) to 59,460 thousand (FY2026): +4.13% across the whole window, largest consecutive step +0.75%, no discontinuity, no listing or recapitalisation event in scope. The per-share bridge reproduces the filed cent in 10 of 12 periods; the two exceptions are one truncation convention and one 2.3% gap that I could not explain from the served data. Because the antidilutive periods make basic = diluted on the face, the filed count CAN substitute for `EPS × shares` as a denominator — but the count itself is quoted on two bases, which is the DA-30 finding below."
  - da_id: "DA-29"
    chosen_reading: "RUN, and it found both a clean instance and the causal chain. CLEAN: the adjusted-income bridge on sec203 p.37 has every one of its ten terms on the page and closes exactly for both periods (−30,471 + 2,894 + 29,514 + 5,591 + 0 + 3,412 + 394 + 11,631 + 42,381 − 23,930 = 41,416; −54,274 − 3,097 + 32,574 + 7,231 + 0 + 4,512 + 486 + 8,948 + 34,108 − 20,515 = 9,973) — no back-solve, nothing to locate that is not located. DEFECTIVE: `reported` in the instrument is served from the same stripped fact store as the headline values and is therefore itself an absolute magnitude in at least five rows of a single 10-K run (28,889 vs filed (28,889); 29,673 vs (29,673); 21,941 vs (21,941); 44,399 vs (44,399); 94,793 vs (94,793)) — so 'reconcile `reported` to the statement face' is not a formality, it is the load-bearing check. And the chain is now reconstructible: the sec203 `OperatingExpenses` row's 96,000 residual is EXACTLY 2 x 48,000, caused by feeding the strip-stripped restructuring value into the arc, which makes DA-23 the upstream CAUSE of a DA-29 symptom."
  - da_id: "DA-30"
    chosen_reading: "CONFIRMED, second instance in this thesis, different mechanism from BWXT's. One concept, two bases, no basis field: `WeightedAverageNumberOfDilutedSharesOutstanding` is served ONLY as the GAAP count (59,386 for 9M FY2026 — which equals BASIC on the face because the period is a loss), while the same filing's adjusted-EPS table divides by 60,525, and footnote (2) on sec203 p.37 is the only place the second basis is established ('Adjusted earnings per share is calculated using diluted shares whereas Net loss per share is calculated using basic shares'). The platform serves 36 facts for the concept and NONE of them is 60,525. Basis difference +1.92%; a consumer recomputing adjusted EPS from served facts gets $0.70 against a filed $0.68. A second instance on the PERIOD axis: the sec203 `OperatingIncomeLoss` 3M slot is populated with the 9M value (14,185,000) while the computed column holds the correct 3M value (5,230,000)."
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: "sec203 p.4, Consolidated Statements of Operations and Comprehensive Loss, verbatim, four columns (third quarters and nine months ended March 27, 2026 and March 28, 2025): Net revenues 235,759 / 211,358 / 693,840 / 638,914; Cost of revenues 166,709 / 154,248 / 501,258 / 469,188; Gross margin 69,050 / 57,110 / 192,582 / 169,726; Selling, general and administrative 39,138 / 43,044 / 127,183 / 116,698; Research and development 15,014 / 15,983 / 43,579 / 55,734; Amortization of intangible assets 9,561 / 10,185 / 29,514 / 32,574; Restructuring and other charges (48) / 4,931 / 5,591 / 7,231; Acquisition costs and other related expenses 155 / 311 / 900 / 666; Total operating expenses 63,820 / 74,454 / 206,767 / 212,903; Income (loss) from operations 5,230 / (17,344) / (14,185) / (43,177); Other (expense) income, net (3,093) / 2,304 / (5,613) / (2,900); Income tax provision (benefit) 174 / (2,648) / (6,211) / (14,967); Net loss (2,861) / (19,170) / (30,471) / (54,274); Basic and diluted net loss per share (0.04) / (0.33) / (0.51) / (0.93); Basic and diluted weighted-average shares 59,422 / 58,749 / 59,386 / 58,614. Header reads 'Third Quarters Ended' — the issuer's own label"
    ticker: MRCY
    form_type: 10-Q
    citation_id: sec203
    page_no: 4
    url: https://agentii.ai/v/MRCY/sec203/4
    located_via: read_source_pages
  - figure: "sec201 p.4, Consolidated Statements of Operations and Comprehensive Loss, verbatim, two columns (first quarters ended September 26, 2025 and September 27, 2024): Net revenues 225,209 / 204,431; Cost of revenues 162,310 / 152,641; Gross margin 62,899 / 51,790; Selling, general and administrative 45,906 / 33,153; Research and development 13,184 / 18,383; Amortization of intangible assets 10,259 / 11,235; Restructuring and other charges 1,584 / 2,260; Acquisition costs and other related expenses 563 / 177; Total operating expenses 71,496 / 65,208; Loss from operations (8,597) / (13,418); Other expense, net (2,080) / (1,339); Income tax benefit (4,021) / (5,594); Net loss (12,515) / (17,525); Basic and diluted net loss per share (0.21) / (0.30); Basic and diluted weighted-average shares 59,191 / 58,260"
    ticker: MRCY
    form_type: 10-Q
    citation_id: sec201
    page_no: 4
    url: https://agentii.ai/v/MRCY/sec201/4
    located_via: read_source_pages
  - figure: "sec202 p.4, Consolidated Statements of Operations and Comprehensive Loss, verbatim, four columns (second quarters and six months ended December 26, 2025 and December 27, 2024): Net revenues 232,872 / 223,125 / 458,081 / 427,556; Cost of revenues 172,239 / 162,299 / 334,549 / 314,940; Gross margin 60,633 / 60,826 / 123,532 / 112,616; Selling, general and administrative 42,139 / 40,501 / 88,045 / 73,654; Research and development 15,381 / 21,368 / 28,565 / 39,751; Amortization of intangible assets 9,694 / 11,154 / 19,953 / 22,389; Restructuring and other charges 4,055 / 40 / 5,639 / 2,300; Acquisition costs and other related expenses 182 / 178 / 745 / 355; Total operating expenses 71,451 / 73,241 / 142,947 / 138,449; Loss from operations (10,818) / (12,415) / (19,415) / (25,833); Other expense, net (440) / (3,865) / (2,520) / (5,204); Income tax benefit (2,364) / (6,725) / (6,385) / (12,319); Net loss (15,095) / (17,579) / (27,610) / (35,104); Basic and diluted net loss per share (0.26) / (0.30) / (0.47) / (0.60); Basic and diluted weighted-average shares 59,415 / 58,561 / 59,324 / 58,454"
    ticker: MRCY
    form_type: 10-Q
    citation_id: sec202
    page_no: 4
    url: https://agentii.ai/v/MRCY/sec202/4
    located_via: read_source_pages
  - figure: "sec205 p.47, Consolidated Statements of Operations and Comprehensive Loss, verbatim, three columns (fiscal years ended July 3, 2026; June 27, 2025; June 28, 2024): Net revenues 983,622 / 912,020 / 835,275; Cost of revenues 702,457 / 657,526 / 639,374; Gross margin 281,165 / 254,494 / 195,901; Selling, general and administrative 175,031 / 154,412 / 166,786; Research and development 59,736 / 67,647 / 101,328; Amortization of intangible assets 38,904 / 42,849 / 47,661; Restructuring and other charges 5,939 / 7,216 / 26,170; Acquisition costs and other related expenses 1,275 / 1,997 / 1,710; Total operating expenses 280,885 / 274,121 / 343,655; Income (loss) from operations 280 / (19,627) / (147,754); Other expense, net (7,302) / (974) / (7,705); Income tax expense (benefit) 784 / (12,520) / (51,635); Net loss (29,673) / (37,904) / (137,640); Basic and diluted net loss per share (0.50) / (0.65) / (2.38); Basic and diluted weighted-average shares 59,460 / 58,746 / 57,738; Total comprehensive loss (21,941) / (44,399) / (139,476)"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 47
    url: https://agentii.ai/v/MRCY/sec205/47
    located_via: read_source_pages
  - figure: "sec205 p.32, MD&A Fiscal 2026 vs Fiscal 2025, verbatim: 'There were 53 weeks and 52 weeks included in the results of operations for fiscal 2026 and fiscal 2025, respectively.' and 'Total revenues increased $71.6 million, or 7.9%, to $983.6 million during fiscal 2026, as compared to $912.0 million during fiscal 2025.' Table: Net revenues 983,622 / 912,020; Gross margin 281,165 / 28.6% / 254,494 / 27.9%; Total operating expenses 280,885 / 28.6% / 274,121 / 30.0%; 'Income (loss) from operations 280 / — / (19,627) / (2.1)'. Also the disposal disclosures: 'On April 15, 2025, we entered into a strategic supply agreement under which Cicor Group acquired the Company's manufacturing operations in Plan-Les-Ouates, Switzerland' and 'On April 30, 2025, we completed an asset acquisition of Star Lab, a subsidiary of Wind River Systems, Inc.'"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 32
    url: https://agentii.ai/v/MRCY/sec205/32
    located_via: read_source_pages
  - figure: "sec205 p.33, MD&A cost lines, verbatim: 'Gross margin was 28.6% for fiscal 2026, an increase of 70 basis points from the 27.9% gross margin realized during fiscal 2025.' Research and development: 'decreased $7.9 million, or 11.7%, to $59.7 million during fiscal 2026, as compared to $67.6 million for fiscal 2025. The decrease was primarily driven by efficiency improvements and the savings from headcount reductions of approximately 270 employees'. Restructuring: 'During fiscal 2026, we incurred $5.9 million of restructuring and other charges ... All of the Restructuring and other charges are classified as Operating expenses in the Consolidated Statements of Operations and Comprehensive Loss'. Acquisition costs: 'Acquisition costs during fiscal 2025 included $1.4 million related to the sale of our manufacturing operations in Switzerland and the associated supply agreement with Cicor Group'. EAC table: Gross favorable 28,847 / 26,642; Gross unfavorable (47,589) / (47,712); Net impact of changes in estimates (18,742) / (21,070)"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 33
    url: https://agentii.ai/v/MRCY/sec205/33
    located_via: read_source_pages
  - figure: "sec205 p.49, Consolidated Statements of Cash Flows, verbatim, three columns (fiscal years ended July 3, 2026; June 27, 2025; June 28, 2024): Net loss (29,673) / (37,904) / (137,640); Net cash provided by operating activities 102,388 / 138,851 / 60,382; Purchases of property and equipment (34,301) / (19,803) / (34,291); Acquisition of assets and businesses, net of cash acquired (1,415) / (4,543) / —; 'Proceeds from sale of manufacturing operations to Cicor Group' — / 6,246 / —; Other investing activities — / 4,600 / —; Net cash used in investing activities (35,716) / (13,500) / (34,291); Proceeds from employee stock plans 5,418 / 3,661 / 4,642; Payments under credit facilities (150,000) / — / (25,000); 'Net cash (used in) provided by financing activities (162,739) / 1,412 / 82,680'; Net (decrease) increase in cash and cash equivalents (94,793) / 128,578 / 108,958"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 49
    url: https://agentii.ai/v/MRCY/sec205/49
    located_via: read_source_pages
  - figure: "sec203 p.36, adjusted EBITDA reconciliation, verbatim, four columns (third quarters and nine months ended March 27, 2026 and March 28, 2025): Net loss (2,861) / (19,170) / (30,471) / (54,274); Other non-operating adjustments, net 2,445 / (3,911) / 2,894 / (3,097); Interest expense, net 4,824 / 6,778 / 16,884 / 23,164; Income tax provision (benefit) 174 / (2,648) / (6,211) / (14,967); Depreciation 8,395 / 9,731 / 25,655 / 29,484; Amortization of intangible assets 9,561 / 10,185 / 29,514 / 32,574; 'Restructuring and other charges (48) / 4,931 / 5,591 / 7,231'; Impairment of long-lived asset — / — / — / —; Acquisition, financing and other third party costs 581 / 1,072 / 3,412 / 4,512; Fair value adjustments from purchase accounting 132 / 131 / 394 / 486; Litigation and settlement expense, net 2,120 / 5,467 / 11,631 / 8,948; Stock-based and other non-cash compensation expense 10,768 / 12,124 / 42,381 / 34,108; Adjusted EBITDA 36,091 / 24,690 / 101,674 / 68,169"
    ticker: MRCY
    form_type: 10-Q
    citation_id: sec203
    page_no: 36
    url: https://agentii.ai/v/MRCY/sec203/36
    located_via: read_source_pages
  - figure: "sec203 p.37, adjusted income and adjusted EPS reconciliation, verbatim, as filed: Net loss and loss per share (30,471) / (0.51) / (54,274) / (0.93); Other non-operating adjustments, net 2,894 / (3,097); Amortization of intangible assets 29,514 / 32,574; Restructuring and other charges 5,591 / 7,231; Impairment of long-lived assets — / —; Acquisition and financing costs 3,412 / 4,512; Fair value adjustments from purchase accounting 394 / 486; Litigation and settlement expense, net 11,631 / 8,948; Stock-based and other non-cash compensation expense 42,381 / 34,108; Impact to income taxes (23,930) / (20,515); 'Adjusted income and adjusted earnings per share $ 41,416 / $ 0.68 / $ 9,973 / $ 0.17'; 'Diluted weighted-average shares outstanding 60,525 / 59,024'. Footnote (2), verbatim: 'Adjusted earnings per share is calculated using diluted shares whereas Net loss per share is calculated using basic shares. There was no impact and a $0.01 impact to the calculation of adjusted earnings per share as a result of this for the nine months ended March 27, 2026 and March 28, 2025, respectively.'"
    ticker: MRCY
    form_type: 10-Q
    citation_id: sec203
    page_no: 37
    url: https://agentii.ai/v/MRCY/sec203/37
    located_via: read_source_pages
  - figure: "sec203 p.35, NON-GAAP FINANCIAL MEASURES, verbatim: 'In our periodic communications, we discuss certain important measures that are not calculated according to U.S. generally accepted accounting principles (GAAP), including adjusted EBITDA, adjusted income, adjusted EPS, and free cash flow.' — four measures, none a per-unit metric"
    ticker: MRCY
    form_type: 10-Q
    citation_id: sec203
    page_no: 35
    url: https://agentii.ai/v/MRCY/sec203/35
    located_via: read_source_pages
  - figure: "sec203 p.6, Consolidated Statements of Cash Flows, verbatim, two columns (nine months ended March 27, 2026 and March 28, 2025): Net loss (30,471) / (54,274); Net cash provided by operating activities 60,235 / 100,776; Acquisition of assets and businesses, net of cash acquired (1,415) / —; Net cash used in investing activities (22,128) / (11,105); Proceeds from employee stock plans 2,728 / 1,492; Purchase and retirement of common stock (15,001) / —; Payments of deferred financing and offering costs (3,156) / (2,249); 'Net cash used in financing activities (15,429) / (757)'; Net increase in cash and cash equivalents 22,701 / 89,301"
    ticker: MRCY
    form_type: 10-Q
    citation_id: sec203
    page_no: 6
    url: https://agentii.ai/v/MRCY/sec203/6
    located_via: read_source_pages
key_metrics:
  periods_stripped: 11
  periods_verified: 13
  periods_correct: 2
  served_series_negative_values: 0

---

# MRCY × recent-quarter — Phase 3 defect census (PIL-3)

## 0. What this artifact is, and the one rule it obeys

The constitution pins MRCY as the edge case this register was built to catch: *"MRCY is DA-23-clean with an operating income of $0.280M on $983.6M of revenue (0.03% margin). A sign error there would be invisible by inspection — the magnitude is plausible either way. This is why the component identity is mandatory rather than a spot-check."*

The assignment was therefore not to re-inspect MRCY but to **run the identity in-line, every period, and either confirm or refute the clean verdict** — accepting no conclusion drawn from plausibility, because at a 0.03% margin plausibility carries zero information.

**The verdict is REFUTED.** The component identity closes to the dollar on 13 of 13 filed periods, and it is the filer's own arc — but `OperatingIncomeLoss` is served sign-stripped in **11 of those 13 periods**, and the 2 that are correct are precisely the 2 that were filed POSITIVE. The 0.03% margin is real, the break-even reading of FY2026 is real, and the clean verdict is an artefact of having tested the one period that could not expose the defect. 001 tested that period. So did the platform's own validator, which returns `status: pass` for the FY2026 annual `OperatingIncomeLoss` row ([sec205 p.47](https://agentii.ai/v/MRCY/sec205/47)).

The one rule this artifact obeys throughout: **the component identity is run on every period it quotes, not only the period it reports.** Every figure below is a cell read off a page, and every period in the comparison is verified on its own face. The failure this artifact records is exactly the failure of running the identity on one side of a comparison.

**Pin note, recorded honestly.** `constitution_pin` is `1.5.0`; this artifact is on the post-amendment side and therefore carries the DA-29 and DA-30 obligations in full, both of which are discharged in §5 and §7. `skill_pin` is `07d26b9c738b`, present as two agreeing records in `theses/002-evidence-validation/skill_pins.jsonl` — but the derivation path those records cite (`scripts/dispatch.py`, `plugins/…`) does not exist in this workspace, so the pin is recorded, not independently recomputed. `corpus_version` remains `UNPINNED`, which is the honest value: no corpus-version endpoint exists.

---

## 1. The test that can actually run at MRCY

### 1.1 The arc set, read from the filer's own linkbase

MRCY is the **fully-resolvable cell** of the detector-availability 2×2 (§8): both axes are present, so the registered detector runs in its stated form with no substitution. Two consequences, and the second is the one that matters.

First, the component identity is not an analyst's convention imported onto the data. The filer's own calculation linkbase, returned for accession `0001049521-26-000024`, asserts it:

```
parent: us-gaap:OperatingIncomeLoss  "Income (loss) from operations"
  child: us-gaap:GrossProfit          "Gross profit"             weight  1
  child: us-gaap:OperatingExpenses    "Total operating expenses" weight -1
```

and `OperatingExpenses` branches to exactly five children — `SellingGeneralAndAdministrativeExpense`, `ResearchAndDevelopmentExpense`, `AmortizationOfIntangibleAssets`, `RestructuringCharges`, `BusinessCombinationAcquisitionRelatedCosts` — all weight `1`. Seven inputs to the operating line, no more. This is the DA-24 refutation in §6 and it is what makes "every component cell quoted from the face" a complete check rather than a sample.

Second, and less comfortable: because the identity is the platform's own declared arithmetic, **a component-identity failure at MRCY is a self-inconsistency of the instrument, not a cross-check that happens to agree.** The identity holds at MRCY, so it cannot be the instrument's defence — the instrument is internally consistent about the VALUES and wrong about the SIGNS.

### 1.2 Why the identity cannot deliver a clean verdict on its own

The identity is a statement about arithmetic consistency. A sign strip applied uniformly to both sides of a comparison preserves every additive relation. Concretely: if `served = |filed|`, then `GrossProfit_served − Opex_served = OperatingIncome_served` **if and only if** the filed computation also involved those magnitudes with the same relative signs — which it does for a positive gross margin and a positive opex total. The MRCY case is the degenerate instance: gross margin and opex are both large positives, so their difference is small and its sign is the only thing the identity could have caught. The identity catches it — 13 of 13 exact against the FILED cells. What it cannot catch is a strip applied to the SERVED cells downstream of that computation, which is precisely what happened, and which is why §2.3 exists.

---

## 2. The census: DA-23 on every quoted period

### 2.1 The component identity, in-line, 13 of 13 exact

All values in $ thousands, every cell quoted from the statement face cited. The opex column shows the five filed lines summing to the filed total; `GM − Opex` is the identity; the last two columns are the filed operating result and the served value.

| # | Period | Face | Gross margin | Opex components (SG&A + R&D + Amort + Restructuring + Acq) | `GM − Opex` | Filed op. inc./(loss) | Served value | Sign verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | Q1 FY2026 3M (to 2025-09-26) | [sec201 p.4](https://agentii.ai/v/MRCY/sec201/4) | 62,899 | 45,906 + 13,184 + 10,259 + 1,584 + 563 = **71,496** | **−8,597** | (8,597) | +8,597,000 | **STRIPPED** |
| 2 | Q1 FY2025 3M (to 2024-09-27) | [sec201 p.4](https://agentii.ai/v/MRCY/sec201/4) | 51,790 | 33,153 + 18,383 + 11,235 + 2,260 + 177 = **65,208** | **−13,418** | (13,418) | +13,418,000 | **STRIPPED** |
| 3 | Q2 FY2026 3M (to 2025-12-26) | [sec202 p.4](https://agentii.ai/v/MRCY/sec202/4) | 60,633 | 42,139 + 15,381 + 9,694 + 4,055 + 182 = **71,451** | **−10,818** | (10,818) | +10,818,000 | **STRIPPED** |
| 4 | Q2 FY2025 3M (to 2024-12-27) | [sec202 p.4](https://agentii.ai/v/MRCY/sec202/4) | 60,826 | 40,501 + 21,368 + 11,154 + 40 + 178 = **73,241** | **−12,415** | (12,415) | +12,415,000 | **STRIPPED** |
| 5 | Q3 FY2026 3M (to 2026-03-27) | [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4) | 69,050 | 39,138 + 15,014 + 9,561 + (48) + 155 = **63,820** | **+5,230** | 5,230 | +5,230,000 | **CLEAN** |
| 6 | Q3 FY2025 3M (to 2025-03-28) | [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4) | 57,110 | 43,044 + 15,983 + 10,185 + 4,931 + 311 = **74,454** | **−17,344** | (17,344) | +17,344,000 | **STRIPPED** |
| 7 | 6M FY2026 (to 2025-12-26) | [sec202 p.4](https://agentii.ai/v/MRCY/sec202/4) | 123,532 | 88,045 + 28,565 + 19,953 + 5,639 + 745 = **142,947** | **−19,415** | (19,415) | +19,415,000 | **STRIPPED** |
| 8 | 6M FY2025 (to 2024-12-27) | [sec202 p.4](https://agentii.ai/v/MRCY/sec202/4) | 112,616 | 73,654 + 39,751 + 22,389 + 2,300 + 355 = **138,449** | **−25,833** | (25,833) | +25,833,000 | **STRIPPED** |
| 9 | 9M FY2026 (to 2026-03-27) | [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4) | 192,582 | 127,183 + 43,579 + 29,514 + 5,591 + 900 = **206,767** | **−14,185** | (14,185) | +14,185,000 | **STRIPPED** |
| 10 | 9M FY2025 (to 2025-03-28) | [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4) | 169,726 | 116,698 + 55,734 + 32,574 + 7,231 + 666 = **212,903** | **−43,177** | (43,177) | +43,177,000 | **STRIPPED** |
| 11 | FY2026 (to 2026-07-03) | [sec205 p.47](https://agentii.ai/v/MRCY/sec205/47) | 281,165 | 175,031 + 59,736 + 38,904 + 5,939 + 1,275 = **280,885** | **+280** | 280 | +280,000 | **CLEAN** |
| 12 | FY2025 (to 2025-06-27) | [sec205 p.47](https://agentii.ai/v/MRCY/sec205/47) | 254,494 | 154,412 + 67,647 + 42,849 + 7,216 + 1,997 = **274,121** | **−19,627** | (19,627) | +19,627,000 | **STRIPPED** |
| 13 | FY2024 (to 2024-06-28) | [sec205 p.47](https://agentii.ai/v/MRCY/sec205/47) | 195,901 | 166,786 + 101,328 + 47,661 + 26,170 + 1,710 = **343,655** | **−147,754** | (147,754) | +147,754,000 | **STRIPPED** |

**The identity closes 13 of 13 to the dollar, and the opex sub-stack closes 13 of 13 as well.** The additive articulation checks independently: 62,899 + 60,633 = 123,532 (6M FY2026); 123,532 + 69,050 = 192,582 (9M FY2026); 51,790 + 60,826 = 112,616 (6M FY2025); 112,616 + 57,110 = 169,726 (9M FY2025). Every quarter sums into its year-to-date, and every year-to-date into its year.

**The strip is 11 of 13 against the filed cells: 11 filed losses, all 11 served positive of identical magnitude; 2 filed incomes, both served unchanged.** The rule has no exceptions and no residual. Both directions of the comparison are now verified against verbatim statement faces — including, this pass, both columns of the statement 001 relied on.

### 2.2 The single sharpest demonstration in this artifact, and it is one table

It is not the 11-of-13 count. It is a single line, `Other (expense) income, net`, on [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4), whose four columns are filed as **(3,093) | 2,304 | (5,613) | (2,900)**.

Three negatives and one positive, in one table, in one filing, under one concept. The served series for `OtherNonoperatingIncomeExpense` contains **twelve values equal to the absolute value of the filed negative and exactly one value equal to the filed positive (2,304)** — thirteen filed cells, twelve stripped, one clean, and the clean one is the only filed-positive one. Across the whole concept's filed history on the four faces cited there is exactly one non-negative cell and it is the only non-stripped one.

This is the finding that closes the question. A concept-level or issuer-level sign transformation cannot produce it: the concept is demonstrably served with BOTH signs. The transformation is applied **per VALUE SIGN** — filed-positive values pass through untouched; filed-negative values are replaced by their magnitudes. Any detector that tests for "this concept is being absolutised" is testing the wrong hypothesis.

### 2.3 The served series does not articulate — and the size of the failure identifies the stripped term

A consequence worth recording because it is a *portable* detector, independent of the component identity:

```
served 6M FY2026  +19,415,000
served Q3 FY2026   +5,230,000
                          sum = +24,645,000
served 9M FY2026             = +14,185,000      ✗ does not articulate
```

The served quarters do not sum to the served year-to-date. The gap is 24,645 − 14,185 = **10,460**, and 10,460 = **2 × 5,230** exactly — 2× the served value of the very term whose served sign differs from its filed sign. The identity that does hold is `19,415 − 5,230 = 14,185`, i.e. the served magnitudes combined with the FILED signs.

**Stated as a detector: for any adjacent period pair with a sign discontinuity, the served series fails articulation by exactly 2× the stripped term's magnitude.** That is checkable without any external source, and no back-solve can produce it by accident, because a back-solved series articulates by construction.

### 2.4 Verdict on the 0.03% clean read

**REFUTED — and the refutation is exact, not probabilistic.**

001's `definitions_used` records `da_id: DA-23` with the reading *"operating_income verified against components; MRCY clean (components reconcile exactly)"* (001 artifact, lines 18–19). Both clauses are separately evaluable:

- **"components reconcile exactly" — TRUE, and I reproduce it.** 001's own figure, gross profit $281,165 less operating expenses $280,885 = $0.280M, is exact against [sec205 p.47](https://agentii.ai/v/MRCY/sec205/47), and it is row 11 of the table above.
- **"MRCY clean" — FALSE.** MRCY is the opposite of clean: 11 of the 13 filed periods on the four faces are served sign-stripped, and every served `OperatingIncomeLoss` fact in the platform's series — 36 facts spanning fiscal 2020 through fiscal 2026 — is non-negative, while at least 11 of them are filed losses.

**The mechanism of the error is the single most useful output of this artifact**, because it is a method error rather than a data error, and it will reproduce anywhere:

> 001 ran the component identity on the period it was REPORTING and not on the period it was COMPARING AGAINST. FY2026 is one of the two filed-positive periods. It was therefore guaranteed to pass, and the comparator — the value carrying the sign that produced 001's headline — was never tested. A detector run only on the subject of a comparison cannot detect a comparison error.

MRCY's 0.03% margin genuinely is "close enough to zero that a sign error would be invisible by inspection" — 001 said so itself (line 94). That is exactly why leaving the comparator unverified was the decisive omission: the identity resolved the one number that could not be wrong in a way that mattered, and cleared the issuer on it.

---

## 3. The DA-23 component finding: three concepts, per-value-sign

The register's component-level clause was added at 1.5.0 after BWXT produced the first instance. **MRCY is the second, at three component concepts**, and it produces the exact signature.

### 3.1 `RestructuringCharges` — the exact strip signature, confirmed on two independent pages

Fiscal 2026 third quarter, filed as **(48)** on the statement face ([sec203 p.4](https://agentii.ai/v/MRCY/sec203/4), `Restructuring and other charges | (48) | 4,931 | 5,591 | 7,231`) and again as **(48)** in the adjusted-EBITDA reconciliation ([sec203 p.36](https://agentii.ai/v/MRCY/sec203/36), `Restructuring and other charges (48) / 4,931 / 5,591 / 7,231`). Two pages, same parenthesised negative, both inside the same filing.

Served value: **+48,000.**

```
diff = served − filed = 48,000 − (−48) = 48048 = 2 × 48,000  →  signature 2 × |value|  ✓ EXACT
```

The remaining filed-face cells of this concept are all unparenthesised positives — 1,584 / 2,260 / 4,055 / 40 / 5,639 / 2,300 / 5,591 / 7,231 / 4,931 / 5,939 / 7,216 / 26,170 — and are served unchanged. One negative cell in the entire series, and it is the one that moves. The clause is satisfied literally: *"check whether any individual component concept is served as an absolute magnitude"* — yes, and the exact strip signature is present.

### 3.2 `OtherNonoperatingIncomeExpense` — 13 cells, 12 stripped, 1 clean

Covered in §2.2. The filed cells, in full, from the four faces: sec203 p.4 `(3,093) / 2,304 / (5,613) / (2,900)`; sec201 p.4 `(2,080) / (1,339)`; sec202 p.4 `(440) / (3,865) / (2,520) / (5,204)`; sec205 p.47 `(7,302) / (974) / (7,705)`. Twelve negatives, served as magnitudes. One positive — 2,304 — served as filed. Same concept, same filing, adjacent columns, opposite treatment.

### 3.3 `IncomeTaxExpenseBenefit` — 16 cells, 14 negative, 2 positive

Filed cells: sec203 p.4 `174 / (2,648) / (6,211) / (14,967)`; sec201 p.4 `(4,021) / (5,594)`; sec202 p.4 `(2,364) / (6,725) / (6,385) / (12,319)`; sec205 p.47 `784 / (12,520) / (51,635)`. Fourteen negatives, two positives (174 and 784). On the seven served facts I compared individually, the two filed-positives are served unchanged and all five of the filed-negatives checked are served as their absolute values.

### 3.4 The discriminator: a doubling is not a stripping

Found this pass, and it is a live trap for anyone implementing the component test. The 10-K instrument run returns `LesseeOperatingLeaseLiabilityPaymentsDue` with `computed: 136,742,000` against `reported: 68,371,000` — a diff of exactly one times the value, i.e. the computed figure is **2 ×** the reported figure. That is the same *numeric* signature family as the strip (`diff = 2 × value`) and it is **not DA-23**: a stripped fact is served as **1 × |filed|**, so its diff against the filed value is **2 × |filed|** because the sign flip doubles the gap. A double-counted arc produces **2 × reported** in the computed column and a diff of 1 × reported.

**The discriminator is `served / filed`, not `diff / value`:** ratio 1 with a sign flip = DA-23; ratio 2 with no sign question = an arc defect. Recording this because the register states the signature as `diff = 2 × value`, and both defects satisfy it while requiring opposite remedies.

---

## 4. The per-share line: inverted in every period, and still not a sign test

MRCY's per-share line inverts in every period observed, in the same class as the live YSS inversion. Filed against served, side by side, both bases (MRCY prints basic and diluted identically because every period in scope is a loss and the instruments are antidilutive):

| Period | Face | Filed basic | Filed diluted | Served | Verdict |
|---|---|---|---|---|---|
| Q3 FY2026 3M | [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4) | $(0.04) | $(0.04) | 0.04 | **INVERTED** |
| Q3 FY2025 3M | [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4) | $(0.33) | $(0.33) | 0.33 | **INVERTED** |
| 9M FY2026 | [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4) | $(0.51) | $(0.51) | 0.51 | **INVERTED** |
| 9M FY2025 | [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4) | $(0.93) | $(0.93) | 0.93 | **INVERTED** |
| Q1 FY2026 3M | [sec201 p.4](https://agentii.ai/v/MRCY/sec201/4) | $(0.21) | $(0.21) | 0.21 | **INVERTED** |
| Q1 FY2025 3M | [sec201 p.4](https://agentii.ai/v/MRCY/sec201/4) | $(0.30) | $(0.30) | 0.30 | **INVERTED** |
| Q2 FY2026 3M | [sec202 p.4](https://agentii.ai/v/MRCY/sec202/4) | $(0.26) | $(0.26) | 0.26 | **INVERTED** |
| Q2 FY2025 3M | [sec202 p.4](https://agentii.ai/v/MRCY/sec202/4) | $(0.30) | $(0.30) | 0.30 | **INVERTED** |
| 6M FY2026 | [sec202 p.4](https://agentii.ai/v/MRCY/sec202/4) | $(0.47) | $(0.47) | 0.47 | **INVERTED** |
| 6M FY2025 | [sec202 p.4](https://agentii.ai/v/MRCY/sec202/4) | $(0.60) | $(0.60) | 0.60 | **INVERTED** |
| FY2026 | [sec205 p.47](https://agentii.ai/v/MRCY/sec205/47) | $(0.50) | $(0.50) | 0.50 | **INVERTED** |
| FY2025 | [sec205 p.47](https://agentii.ai/v/MRCY/sec205/47) | $(0.65) | $(0.65) | 0.65 | **INVERTED** |
| FY2024 | [sec205 p.47](https://agentii.ai/v/MRCY/sec205/47) | $(2.38) | $(2.38) | 2.38 | **INVERTED** |

Thirteen of thirteen inverted; **every served per-share value is non-negative** because MRCY had no profitable period in the window. This is the YSS failure mode reproduced at a second issuer, which upgrades it from an incident to a class.

**`EPS × shares` remains INADMISSIBLE, and MRCY shows why the rule is not merely conservative.** The per-share line inverts *in both directions simultaneously*: the numerator (net loss) is served stripped, and the denominator is quoted on two bases (DA-30, §7.2). Using it as a sign test corrupts sign and magnitude at once — and it is strictly less precise than the identity already in hand. The filed weighted-average count is the admissible denominator; it is available on every face (59,422 / 58,749 / 59,386 / 58,614 on [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4)) and, because basic equals diluted in these loss periods, it needs no antidilution adjustment for the GAAP basis.

---

## 5. The instrument, re-measured (computed vs reported pairs only)

`status` is discarded throughout as a summary statistic; the pairs are read directly. Two runs are in scope: the FY2026 10-K (`0001049521-26-000045`), counts `pass 10 / warn 7 / fail 7`, and the Q3 FY2026 10-Q (`0001049521-26-000024`).

### 5.1 `reported` is itself sign-stripped — five instances in one run

The DA-29 corollary says `reported` must be reconciled to the statement face. At MRCY that is not a formality, because **`reported` is served from the same stripped fact store as the headline values.** Five rows of the single 10-K run, each `reported` checked against a cell I read on [sec205 p.47](https://agentii.ai/v/MRCY/sec205/47):

| Row (10-K, `0001049521-26-000045`) | Instrument `reported` | Filed cell | Verdict |
|---|---|---|---|
| `IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` | 28,889,000 | **Loss before income taxes (28,889)** | `reported` = absolute magnitude |
| `NetIncomeLoss` | 29,673,000 | **Net loss $(29,673)** | `reported` = absolute magnitude |
| `ComprehensiveIncomeNetOfTax` (FY2026) | 21,941,000 | **Total comprehensive loss $(21,941)** | `reported` = absolute magnitude |
| `ComprehensiveIncomeNetOfTax` (FY2025) | 44,399,000 | **Total comprehensive loss $(44,399)** | `reported` = absolute magnitude; **`status: pass`** |
| `CashCashEquivalents…PeriodIncreaseDecrease…` | 94,793,000 | **Net (decrease) in cash (94,793)**, [sec205 p.49](https://agentii.ai/v/MRCY/sec205/49) | `reported` = absolute magnitude |

The fourth row is the one to hold onto: `computed 44,399,000 = reported 44,399,000, diff 0, status: pass`. Both sides were stripped, the strips cancelled, and the check reported clean. **`status: pass` does not mean the values are signed correctly; two sign errors in one row produce a pass.** That is the general form of the warning BWXT's §4.1 recorded, and it is why this artifact reports pairs and never statuses.

### 5.2 The causal chain: DA-23 produces the DA-29 symptom, reconstruitibly

The Q3 10-Q run returns `OperatingExpenses` with `computed: 63,916,000` against `reported: 63,820,000` — a residual of **96,000**. Reconstructed exactly from the filed cells on [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4):

```
filed cells, filed signs:   39,138 + 15,014 + 9,561 + (48) + 155 =  63,820   ← matches `reported`, and the face
served values, stripped:    39,138 + 15,014 + 9,561 +  48  + 155 =  63,916   ← matches `computed`
                                                              residual = 96 = 2 × 48
```

**The instrument's opex mis-computation is caused by the DA-23 strip, propagated through the filer's own arc.** The same run then derives `OperatingIncomeLoss` from the CORRECT opex (69,050 − 63,820 = 5,230, appearing in that row's `computed` column), so the run's own rows do not cohere: the same calculation used 63,916 in one row and 63,820 in another. Both cannot be right, and the strip is why.

This is the artifact's most consequential structural finding. DA-23 is treated in the register as a presentation defect on headline values. At MRCY it is **upstream of the instrument's derived subtotals**, so it corrupts values that were never directly stripped — and the corruption is invisible to a screen that checks closure, because 63,916 is a perfectly well-formed number.

### 5.3 `computed` is not reproducible from the instrument's own tree

Two instances, and the distinction between them matters:

- **`GrossProfit`, Q3 FY2026 3M:** `computed −238,570,000` against `reported 69,050,000`. The arc is `GrossProfit = Revenues (1) − CostOfRevenue (−1)`; run on the filed cells it gives 235,759 − 166,709 = 69,050 — exact against the face. **The arc is sound; the fact injection is not.** The 10-K run shows the same shape on the annual (`computed −513,638,000` vs `reported 281,165,000`), which would require a cost of revenues of 1,497,260 where the filed value is 702,457 ([sec205 p.47](https://agentii.ai/v/MRCY/sec205/47)). That figure appears nowhere in the filing.
- **`PropertyPlantAndEquipmentNet`, `LesseeOperatingLeaseLiabilityPaymentsDue`, `ComprehensiveIncomeNetOfTax`:** each fails on the same pattern — a correct arc fed a wrong-context fact. None of the `computed` values is used in this artifact, per the corollary.

Under DA-29's mechanical test, a term appearing nowhere in the source is a back-solve. **`−238,570,000` and `−513,638,000` appear nowhere in MRCY's filings.** They are recorded and discarded, not reconciled.

### 5.4 The residual-locator

Two rows of the 10-K run share a residual of **exactly 6,909,000**: `Liabilities` (`computed 832,227,000` vs `reported 825,318,000`) and `OperatingLeaseLiability` (`computed 66,324,000` vs `reported 59,415,000`). Identical residuals across rows of different magnitude identify a single mis-scoped child arc propagating upward. Cheap, and it works without reading the tree.

### 5.5 The Q3 10-Q, `OperatingIncomeLoss` — the DA-30 period-axis collapse

The row that matters most for §7.2: for the parent whose period key is the three-month date, `reported: 14,185,000` and `computed: 5,230,000`.

The filed three-month value is **+5,230** and the filed nine-month value is **(14,185)** ([sec203 p.4](https://agentii.ai/v/MRCY/sec203/4)). So the row conflates two defects at once: a **period-basis mis-attribution** (the 9M value placed in the 3M slot) and a **strip** (that 9M value served as +14,185 rather than (14,185)). Here `computed` holds the correct figure and `reported` holds the wrong one — the mirror image of the usual case, and a fourth variant of the DA-29 corollary, which assumes `reported` is the anchor. It is not; it is served from the same store as everything else. Error in `reported`: **8,955,000.**

---

## 6. The six DAs, one by one

### DA-23 — sign stripping; any level failing the gross-profit bound: **CONFIRMED**

Parent concept: **11 of 13 filed periods stripped**, zero exceptions to the per-value-sign rule; the 2 clean values are the only 2 filed-positive periods. Full series: 36 served facts across fiscal 2020–2026, **all non-negative**, against a filer with at least 11 filed losses in that window. Component level: **CONFIRMED at three concepts** — `OtherNonoperatingIncomeExpense` (13 cells: 12 stripped, 1 clean), `RestructuringCharges` (1 negative of 13 cells, stripped, exact signature `diff = 2 × 48,000 = 96,000`), `IncomeTaxExpenseBenefit` (16 cells, 14 negative). Per-share line: 13 of 13 inverted. Cash-flow line: `NetCashProvidedByUsedInFinancingActivities` served **+162,739,000** against filed **"(162,739)"** ([sec205 p.49](https://agentii.ai/v/MRCY/sec205/49)), while the two filed-positive years (1,412 and 82,680) are served unchanged — the same rule on a second statement, one stripped cell and two clean. Gross-profit bound: N/A here, the component identity is available and was used.

### DA-24 — asset-sale contamination of the operating line: **REFUTED, with a variant worth registering**

Three independent checks, all negative:

1. **The arc set forecloses it.** The operating line has exactly seven inputs (§1.1) — `GrossProfit` plus five named opex lines. No gain-on-disposal concept is among them, so no disposal gain can reach the operating line. This is a structural refutation, not a magnitude argument.
2. **Proceeds are outside the operating line.** The Cicor sale of the Plan-Les-Ouates manufacturing operations (strategic supply agreement disclosed on [sec205 p.32](https://agentii.ai/v/MRCY/sec205/32)) appears in investing: `Proceeds from sale of manufacturing operations to Cicor Group — / 6,246 / —` ([sec205 p.49](https://agentii.ai/v/MRCY/sec205/49)).
3. **Magnitude is bounded far below the threshold.** Max |operating income| / revenue across the 13 periods is 147,754 / 835,275 = **17.69%** (FY2024). The SATS instance this DA was registered for was **4.6× revenue**. No period's operating line is within an order of magnitude of disposal domination.

**The variant: the disposal DOES touch the operating line, with the opposite sign.** [sec205 p.33](https://agentii.ai/v/MRCY/sec205/33) states verbatim: *"Acquisition costs during fiscal 2025 included $1.4 million related to the sale of our manufacturing operations in Switzerland and the associated supply agreement with Cicor Group"* — and that line, `Acquisition costs and other related expenses`, is inside `Total operating expenses`. So the disposal's only operating-line incidence is a **cost**, which made fiscal 2025's operating loss **larger** by 1.4 / 19.627 = **7.13%**. A disposal-neutral comparator would IMPROVE FY2025 — which, applied to 001's claim, makes the supposed collapse smaller still. DA-24's registered concern is a gain *inflating* an operating result; MRCY is the mirror case, and the register should say which direction it cares about.

### DA-25 — normalised per-unit metrics not reproducible from segment tables: **REFUTED, on positive evidence**

The filer enumerates its non-GAAP measures on [sec203 p.35](https://agentii.ai/v/MRCY/sec203/35): *"including adjusted EBITDA, adjusted income, adjusted EPS, and free cash flow."* Four measures; **none carries a per-unit denominator.** No per-system, per-program, per-spacecraft or per-launch metric is published in scope.

Both non-GAAP reconciliations are then fully reproducible from filed line items — every term located on the page cited, nothing back-solved:

**Adjusted EBITDA ([sec203 p.36](https://agentii.ai/v/MRCY/sec203/36)) — closes on 4 of 4 columns:**

```
9M FY2026: −30,471 + 2,894 + 16,884 − 6,211 + 25,655 + 29,514 + 5,591 + 0 + 3,412 + 394 + 11,631 + 42,381 = 101,674  ✓ filed
9M FY2025: −54,274 − 3,097 + 23,164 − 14,967 + 29,484 + 32,574 + 7,231 + 0 + 4,512 + 486 + 8,948 + 34,108 =  68,169  ✓ filed
 3M FY2026:  −2,861 + 2,445 +  4,824 +    174 +  8,395 +  9,561 −    48 + 0 +   581 + 132 +  2,120 + 10,768 =  36,091  ✓ filed
 3M FY2025: −19,170 − 3,911 +  6,778 −  2,648 +  9,731 + 10,185 + 4,931 + 0 + 1,072 + 131 +  5,467 + 12,124 =  24,690  ✓ filed
```

**Adjusted income ([sec203 p.37](https://agentii.ai/v/MRCY/sec203/37)) — closes on 2 of 2 periods:**

```
9M FY2026: −30,471 + 2,894 + 29,514 + 5,591 + 0 + 3,412 + 394 + 11,631 + 42,381 − 23,930 = 41,416  ✓ filed
9M FY2025: −54,274 − 3,097 + 32,574 + 7,231 + 0 + 4,512 + 486 +  8,948 + 34,108 − 20,515 =  9,973  ✓ filed
```

**Adjacent hazard, recorded as a cross-DA interaction rather than a DA-25 instance.** For the same nine months, the GAAP basis is a loss of $(30,471) / $(0.51) per share while the non-GAAP basis is adjusted income of $41,416 / $0.68 per share — **opposite signs from the same reconciliation**. The platform serves the GAAP figure sign-stripped, so the served GAAP loss and the filed non-GAAP income now read as two concordant positive measures. Nothing normalises a loss away here; the strip does it instead. That is DA-25's *effect* arriving through DA-23's *mechanism*, and it is the reason a DA-25 screen that looks only for per-unit denominators will miss it.

### DA-26 — annual figures mislabelled as quarterly: **CONFIRMED**

Three platform metrics rows carry annual revenue under a quarter label:

| Served label | Served revenue | Filed annual | Quarter the label names | Ratio |
|---|---|---|---|---|
| `fiscal_year: 2026, fiscal_period: Q2` | 983,622,000 | **983,622** ✓ ([sec205 p.47](https://agentii.ai/v/MRCY/sec205/47)) | 3M ended 2025-12-26 = **232,872** ([sec202 p.4](https://agentii.ai/v/MRCY/sec202/4)) | **4.22×** |
| `fiscal_year: 2025, fiscal_period: Q2` | 912,020,000 | **912,020** ✓ ([sec205 p.47](https://agentii.ai/v/MRCY/sec205/47)) | 3M ended 2024-12-27 = **223,125** ([sec202 p.4](https://agentii.ai/v/MRCY/sec202/4)) | **4.09×** |
| `fiscal_year: 2024, fiscal_period: Q2` | 835,275,000 | **835,275** ✓ ([sec205 p.47](https://agentii.ai/v/MRCY/sec205/47)) | not in scope | — |

Each value equals the filed ANNUAL column to the dollar, so the defect is the LABEL, not the content: **a consumer reading `fiscal_period: Q2` and annualising is wrong by 4.1–4.2×.** The Q1- and Q3-labelled rows carry quarterly values, which I verified (235,759 and 211,358 against the 3M cells on [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4)).

**The generalisation, and it is testable.** The contamination magnitude is set by whether the issuer files a Q4 10-Q. MRCY does not — no 10-Q covers a fourth quarter, and the 10-K presents annual columns only — so the platform's year-end row carries the ANNUAL. An issuer that *does* file a Q4 10-Q would carry the quarter in that row and show a label-only defect of roughly 1×. MRCY is therefore the high-magnitude pole of this DA, and the ratio is the discriminator.

### DA-27 — fiscal labels derived from the calendar quarter: **CONFIRMED, and the platform contradicts itself**

The strongest instance recorded in this phase, because it does not depend on trusting the issuer's own labelling. Three served artefacts disagree with each other:

**(a) The calendar.** `get_company_fiscal_calendar` returns `fiscal_year_end_month: 6` with source `gold_companies` and `cross_validation_hint: null`, and a grid in which `FY2026 Q1` = 2025-07-01 → 2025-09-30 and `FY2026 Q4` = **2026-04-01 → 2026-06-30**. Coverage runs FY2025 Q1 → FY2027 Q4 only, so MRCY's earlier filings in the corpus (sec184–sec200, fiscal 2019–2025) sit outside the grid entirely.

**(b) The filings.** MRCY's fiscal 2026 ran **2025-06-28 → 2026-07-03** — a 53-week year ([sec205 p.32](https://agentii.ai/v/MRCY/sec205/32)), in which the third quarter ended 2026-03-27 and the second ended 2025-12-26. So the fiscal year ends in **July**, not June, and the issuer's own quarter headers read `Third Quarters Ended March 27, 2026` ([sec203 p.4](https://agentii.ai/v/MRCY/sec203/4)).

**(c) The label the platform attaches to the filing.** `get_calculation_tree` for accession `0001049521-26-000024` — report date **2026-03-27**, the issuer's third quarter — returns `"fiscal_year": 2026, "fiscal_period": "Q1"`.

The consequence is sharper than "the platform disagrees with the issuer": **the served quarter label is two quarters off the issuer AND two quarters off the platform's own grid**, which places 2026-03-27 in FY2026 Q3. And the fiscal-year end date itself, 2026-07-03, falls **outside the platform's FY2026 grid entirely** — it lands in platform FY2027 Q1 (2026-07-01 → 2026-09-30). The 53rd week belongs to no platform quarter.

One further instance on a different field: `search_sec_filings` returns `year_q_no` equal to the **calendar year of the report date** — 2026 for the 2026-03-27 filing, but 2025 for the 2025-12-26 and 2025-09-26 filings. So the Q1 FY2026 and Q2 FY2026 10-Qs are both served under fiscal year **2025**, off by one fiscal year.

**What I could not determine, and it is the honest gap:** the actual derivation rule. The pure-calendar hypothesis fails on the 10-K (period end 2026-07-03 is calendar Q3, and a calendar rule would label it Q3), and the fiscal-quarter hypothesis fails on the Q3 10-Q (period end 2026-03-27 → labelled Q1, where both the calendar and the platform's grid say Q3). The label is inconsistent with the grid; the rule that generates it is unresolved. Recorded as a carry-forward rather than guessed.

### DA-28 — IPO capital-structure discontinuity: **REFUTED**

MRCY is a clean comparator on this axis, and the test is worth stating because its denominator is unusable for a different reason entirely. Filed weighted-average shares (basic, which equals diluted in every loss period): 57,105 / 57,314 / 57,424 / 57,536 / 57,698 (FY2024); 58,260 / 58,454 / 58,561 / 58,749 (FY2025); 59,191 / 59,324 / 59,386 / 59,415 / 59,422 (FY2026); annuals 57,738 / 58,746 / 59,460.

- **Monotonic, no discontinuity.** Range 57,105 → 59,460 = **+4.13%** across the entire window. Largest consecutive step **+0.75%**; largest year-over-year step +1.75%. No recapitalisation or listing event appears in scope.
- **The per-share bridge holds.** Net loss ÷ filed weighted-average shares reproduces the filed cent in 10 of 12 periods: FY2026 29,673/59,460 = 0.4991 → $(0.50)$ ✓; FY2025 37,904/58,746 = 0.6452 → $(0.65)$ ✓; FY2024 137,640/57,738 = 2.3839 → $(2.38)$ ✓; 9M FY2026 30,471/59,386 = 0.5131 → $(0.51)$ ✓; and so on.
- **Two exceptions, both recorded.** Q3 FY2026: 2,861/59,422 = 0.0481 against a filed $(0.04)$ — the filer truncates rather than rounds (rounding gives 0.05). Q2 FY2026: 15,095/59,415 = **0.2541** against a filed **$(0.26)$** — a **2.3% gap** that is neither rounding nor truncation, and that I could not explain from the served data (basic and diluted are identical in that period, there is no preferred stock, and no attribution line intervenes). Recorded as an open item, not as a DA-28 instance: a bridge miss is not a capital-structure discontinuity.

Against HAWK's 72% failure and 23× share-count span, MRCY's 4.13% and sub-1% bridge are in the clean class. `EPS × shares` remains inadmissible regardless — see §4.

---

## 7. DA-29 and DA-30, the two 1.5.0 additions

### 7.1 DA-29 — the term-location test, run on every reconciliation in this artifact

Every reconciliation presented here was checked term by term against the page cited. **The adjusted-income bridge on [sec203 p.37](https://agentii.ai/v/MRCY/sec203/37) is the clean instance and it is clean completely:** ten terms per period, every one printed on that page, closing exactly on both periods (§6, DA-25). Nothing to locate that is not located, so no back-solve is possible. The 12-term adjusted-EBITDA bridge on [sec203 p.36](https://agentii.ai/v/MRCY/sec203/36) passes identically.

The defect instances are in §5, and their taxonomy is the useful part:

| Class | Instance | Evidence |
|---|---|---|
| `reported` is sign-stripped, not the filed value | 5 rows of the 10-K run | each `reported` equals \|filed cell\| (§5.1) |
| `reported` carries the wrong period basis | sec203 `OperatingIncomeLoss` 3M row, 14,185,000 for a 3M slot | filed 3M = +5,230, filed 9M = (14,185) (§5.5) |
| `computed` not reproducible from the arc | `GrossProfit` −238,570,000 / −513,638,000 | term appears nowhere; the arc run on filed cells gives 69,050 / 281,165 (§5.3) |
| `computed` wrong *because* of a strip | `OperatingExpenses` 63,916,000 vs 63,820,000 | residual 96,000 = 2 × 48,000, reconstructed exactly (§5.2) |
| `status: pass` on two cancelled strips | `ComprehensiveIncomeNetOfTax` FY2025 | computed = reported = 44,399,000, filed (44,399) (§5.1) |
| residual-locator | `Liabilities` and `OperatingLeaseLiability` share 6,909,000 | single mis-scoped arc (§5.4) |

The corollaries are discharged in this artifact by construction: **`computed` is cited nowhere as a derivation** — every value used was read off a page, and the two `computed` values with no page presence are recorded and discarded; and **`reported` is reconciled to the statement face for every figure quoted**, which is how §5.1 was found at all.

### 7.2 DA-30 — the share-count basis collapse, named

**MRCY reports `WeightedAverageNumberOfDilutedSharesOutstanding` on two bases, and the platform serves one.**

| | Basis | Value, 9M FY2026 | Where established |
|---|---|---|---|
| A | GAAP diluted — equal to basic, instruments antidilutive in a loss period | **59,386** | statement face, [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4) |
| B | non-GAAP adjusted-EPS diluted | **60,525** | footnote (2), [sec203 p.37](https://agentii.ai/v/MRCY/sec203/37) — nowhere else |

Footnote (2) verbatim: *"Adjusted earnings per share is calculated using diluted shares whereas Net loss per share is calculated using basic shares."* The same pair for 9M FY2025 is 58,614 (A) against 59,024 (B).

The platform serves **only basis A**: 36 facts for the concept, none of which equals 60,525 or 59,024. There is no basis field, so the collapse is silent. **This is DA-30's second instance in this thesis and its mechanism differs from BWXT's** — BWXT collapses two operating-income scopes (equity-inclusive vs equity-exclusive, 20.2% of the figure); MRCY collapses two share-count bases within one concept. Same structure (one concept, two bases, second basis discoverable only in a footnote), different axis.

**Cost of the collapse, quantified.** Basis B exceeds basis A by 60,525/59,386 = **+1.92%**, and the EPS effect is directional: a consumer recomputing adjusted EPS from served facts computes 41,416 / 59,386 = **$0.70** against the filed **$0.68** — a **+2.6%** overstatement, systematically in the direction of overstating non-GAAP profitability.

**A sub-finding, and it is a defect in the disclosure that establishes the basis.** Footnote (2) quantifies its own effect: *"There was no impact and a $0.01 impact to the calculation of adjusted earnings per share as a result of this for the nine months ended March 27, 2026 and March 28, 2025, respectively."* The arithmetic on the two bases the footnote names contradicts both halves:

```
9M FY2026: 41,416 / 60,525 = 0.6843 → $0.68 filed ✓ ;  41,416 / 59,386 = 0.6974 → $0.70   → impact $0.02  (footnote says "no impact")
9M FY2025:  9,973 / 59,024 = 0.1690 → $0.17 filed ✓ ;   9,973 / 58,614 = 0.1702 → $0.17   → impact $0.00  (footnote says "$0.01")
```

The stated impacts are inverted. The DA-30 finding stands unchanged — the two bases exist and both are filed — but an artifact that names the basis by quoting this footnote would inherit a quantification error, so the footnote is quoted here and separately checked.

**A second DA-30 instance, on the period axis.** §5.5: the sec203 `OperatingIncomeLoss` three-month slot is populated with the nine-month value. One concept, two period bases, no basis field, and this time the platform's own computed column holds the right answer. Structurally identical to the BWXT collapse; the collapsing axis is period length rather than equity scope.

---

## 8. Detector availability — the census-relevant finding

### 8.1 What can run at MRCY: both axes, present

| Axis | Status | Evidence |
|---|---|---|
| (a) gross-profit line FILED | **PRESENT** | `Gross margin $ 69,050` is a first-class subtotal on the face of every statement read — [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4), [sec202 p.4](https://agentii.ai/v/MRCY/sec202/4), [sec201 p.4](https://agentii.ai/v/MRCY/sec201/4), [sec205 p.47](https://agentii.ai/v/MRCY/sec205/47) — sitting between cost of revenues and operating expenses. `GrossProfit` also returns served facts, so MRCY is not a zero-fact concept-name trap. |
| (b) `OperatingIncomeLoss` a filed first-class consolidated subtotal | **PRESENT** | `Income (loss) from operations` on [sec205 p.47](https://agentii.ai/v/MRCY/sec205/47) and [sec203 p.4](https://agentii.ai/v/MRCY/sec203/4); `Loss from operations` on [sec202 p.4](https://agentii.ai/v/MRCY/sec202/4) and [sec201 p.4](https://agentii.ai/v/MRCY/sec201/4). The linkbase carries it as a parent with its own arc. |

**MRCY occupies the fully-resolvable cell** — the first issuer in this phase with both axes present. Two consequences:

1. The component identity runs in its registered form with **no substitute detector**, so the census is fully testable and no inference rests on a proxy.
2. Because the identity is the platform's own arc, the instrument's opex residual of 96,000 (§5.2) is a **self-inconsistency**, not a cross-check disagreement. When both detectors are available, a failure cannot be attributed to a missing line.

The register's framing is therefore vindicated in an unexpected direction. The constitution's reason for choosing MRCY was that a small margin makes a sign error invisible by inspection — and the sign error was there. But the detectors made it *visible anyway*, because the margin being small is irrelevant to a component identity: the identity compares cells, and the cells are unambiguous at any margin. The margin's smallness only defeated the plausibility screen, which 001 correctly refused to rely on and then, correctly refusing, relied on the identity for one of the two sides of its comparison.

### 8.2 The 2×2, fourth cell populated

| | `OperatingIncomeLoss` filed as a subtotal | no filed subtotal |
|---|---|---|
| **gross-profit line filed** | **MRCY** — both detectors, identity runs as registered | resolvable via linkbase (BWXT, LUNR) |
| **no gross-profit line** | — | unresolvable (MRK, BMY, WWD) |

### 8.3 Two name traps on the same detector, both live at MRCY

Carried forward from the PIL-2 MRCY artifact and confirmed here: the platform's `read_source_outline` description field is LLM-generated, fluent, figure-dense, **inherits the negative signs of the text it describes**, and is what `search_keyword_in_source` matches on. A quotation taken from it is simultaneously substantively correct and evidentially fabricated. Every figure in this artifact was read as cells off a page for that reason, and the pages are cited so the cells can be checked. The `radiator` / `radiation` STEM false positive on MRCY's p.8 remains the second trap — a keyword match that is not a match.

---

## 9. 001's clearance: restated, and repaired

001's MRCY artifact is frozen and is not rewritten here; corrections are recorded with line numbers. The file is `theses/001-technology-baseline/artifacts/MRCY/2026-09-18_1239_secular-trends_methodology.md`.

**Reproduced exactly, no correction:** 001's revenue row (`$983.6M` / `$912.0M` / `+7.9%`, line 41) and its R&D row (`$59.7M` / `$67.6M` / `−11.7%`, line 46). Both are the filed figures — the 10-K prints `Total revenues increased $71.6 million, or 7.9%` and `Research and development expenses decreased $7.9 million, or 11.7%` ([sec205 p.32](https://agentii.ai/v/MRCY/sec205/32), [sec205 p.33](https://agentii.ai/v/MRCY/sec205/33)). 001's component arithmetic (lines 48–50: gross profit $281.165M less operating expenses $280.885M = $0.280M) reproduces to the dollar against [sec205 p.47](https://agentii.ai/v/MRCY/sec205/47).

| # | 001's claim (line) | Verified against the filing | Correction |
|---|---|---|---|
| C1 | `Operating income $0.280M vs $19.6M` (44) | filed FY2025 is **Loss** from operations **(19,627)**, printed `(19,627)` on [sec205 p.47](https://agentii.ai/v/MRCY/sec205/47) and `(19,627)` / `(2.1)` in MD&A ([sec205 p.32](https://agentii.ai/v/MRCY/sec205/32)) | The comparator is a **LOSS**. 001's `$19.6M` is the stripped absolute value. **RECORDED, not rewritten.** |
| C2 | `−98.6%` (44) | `(280 − 19,627) / 19,627 = −98.57%` — reproducible **only** from the stripped comparator. On filed signs `280 − (−19,627) = +19,907` **favourable**; the percent change is undefined (the comparison crosses zero) | **Direction inverted.** The correct statement is a **+$19.9M favourable** swing, not a 98.6% collapse. |
| C3 | `Operating margin 0.03% vs 2.2%, −2.1 pts` (45) | 0.03% reproduces (280 / 983,622); filed FY2025 margin is **(2.1)%** ([sec205 p.32](https://agentii.ai/v/MRCY/sec205/32)) | Magnitude right, **sign wrong**: the movement is **+2.1 pts of improvement**, not −2.1 of deterioration. This is 001's most compact reproduction of the DA-23 signature — the filed parenthesised figure with its sign removed. |
| C4 | `Gross profit $281.2M \| — \| 28.6% margin` (42) | filed FY2025 gross margin **254,494 = 27.9%**; MD&A states the increase verbatim: *"an increase of 70 basis points from the 27.9% gross margin"* ([sec205 p.33](https://agentii.ai/v/MRCY/sec205/33)) | The prior-year comparator **exists and is filed**. 001's `—` hides a 70 bp **improvement** on the line that is the identity's first term. |
| C5 | `Operating expenses $280.9M \| — \| 28.6% of revenue` (43) | filed FY2025 opex **274,121 = 30.0%** of revenue ([sec205 p.32](https://agentii.ai/v/MRCY/sec205/32)) | Completion: opex intensity **fell** 30.0% → 28.6%. |
| C6 | `Revenue … +7.9%` (41) | reproduced exactly, and it is the filed figure ([sec205 p.32](https://agentii.ai/v/MRCY/sec205/32)) | Completion: FY2026 was a **53-week** year against 52 (*"There were 53 weeks and 52 weeks included in the results of operations for fiscal 2026 and fiscal 2025, respectively"*). ~1.9 pts of the 7.9% is calendar, not organic. |
| C7 | `R&D … −11.7%` (46) | reproduced exactly ([sec205 p.33](https://agentii.ai/v/MRCY/sec205/33)) | No correction. Driver added: ~270 headcount reductions worth $13.1M, partially offset by engineering utilisation. A cost reduction, not a demand signal. |
| C8 | Header: `accession 0001049521-26-000045 (FY2026 Q2, period ended …)` (27) | the accession is the **FY2026 ANNUAL report**, fiscal year ended **2026-07-03**, filed 2026-08-18 | A fiscal year is not a `Q2`. The mislabel is the DA-26/DA-27 class (§6). |
| C9 | DA-23 reading: *"operating_income verified against components; MRCY clean (components reconcile exactly)"* (18–19) | first clause reproduces 13/13; second clause **fails** — 11 of 13 filed periods are served stripped | **First clause TRUE, second clause FALSE.** MRCY is the register's **most** contaminated issuer in this phase, not a clean one. |
| C10 | §3: *"MRCY is clean, and is a useful edge case"*; *"$0.280M is close enough to zero that a sign error [would be invisible]"*; *"component test resolves it cleanly"* (88–96) | 001's own reasoning is correct and is the reason its clearance should have been withheld | **Method correction:** the identity must be run on **every period quoted**, not only the period reported. 001 ran it on FY2026 — one of the two filed-positive periods — and left the comparator that produced its headline unverified. |

**Does 001's profitability claim hold?** Partly, and the part that holds is immaterial to 001's argument. 001's §3 conclusion (line 107, *"MRCY's 0.03% operating margin is a negative signal for the orbital-compute"*) survives as a statement about **FY2026 alone**: the margin is 0.03%, filed, and reproducible. It does not survive as a statement about MRCY's trajectory, because 001's trajectory evidence was the inverted comparator: on filed figures the operating result moved from a **(19,627) loss** to a **+280 profit**, i.e. **improved**, and gross margin improved 70 bp on the same filing. The observable remains "MRCY earns approximately nothing on operating", which is true; it is not "MRCY is collapsing", which is what 001's −98.6% and −2.1 pts assert and which is the opposite of the filed direction.

---

## 10. What could not be verified

Each item names **which kind** of not-testable it is; ingestion absences and genuine source absences have different remedies and are not merged.

1. **FY2023's `OperatingIncomeLoss` (+21,685,000 served).** The FY2023 10-K (sec165, `0001049521-23-000031`) was not read, so whether this is a filed income or a stripped loss is unestablished. **Kind: not tested (scope limit of this pass)** — not an absence. Remedy: read sec165's statement face. One further historical served value is likewise unreconciled.
2. **A standalone filed fourth quarter.** MRCY files no Q4 10-Q, and the 10-K presents annual columns only, so no filed Q4 income-statement period exists in the corpus. **Kind: genuine absence from the source.** Consequence and it is definitional for this skill: *"every period"* means **13 filed periods, not 16**. Q4 FY2026 = 280 − (−14,185) = **+14,465** and Q4 FY2025 = −19,627 − (−43,177) = **+23,550** are **DERIVED, not filed**, and are therefore inadmissible to a component identity run on filed cells. They are recorded here and used nowhere.
3. **The rendered-statement layer.** `get_company_financials` reports `statements_available: false`, noting that `pipeline.xbrl_rendered_statements` is pending creation. **Kind: ingestion absence at the PLATFORM level** — a table that does not exist — as distinct from a filing-level ingestion absence and from a source absence. Remedy: backfill; nothing about MRCY's disclosures is missing, and every value in this artifact came from page text.
4. **`processing_status: pending` — and it is a NEGATIVE CONTROL.** All 36 MRCY filings returned by `search_sec_filings` carry `processing_status: pending`, while **10 of 10 pages requested served full cell-level text with tables**. So for MRCY, `pending` is a metadata lag and **not** an ingestion absence. The inference recorded at YSS — `pending` ⇒ periods return 0 facts ⇒ not testable — **does not generalise**, and should not be applied without checking whether pages serve.
5. **The Q2 FY2026 per-share bridge gap.** Filed $(0.26)$ against 15,095 / 59,415 = **0.2541**, a 2.3% miss, neither rounding nor truncation. **Kind: tested and unexplained** — not an absence. Basic and diluted are identical in that period, there is no preferred stock, and no attribution line intervenes. At 10 of 12 periods clean and this the one material exception, it is recorded rather than resolved.
6. **The DA-27 label-derivation rule.** The served `fiscal_period` is inconsistent with both the issuer's labels and the platform's own calendar grid (§6, DA-27), and neither a pure-calendar nor a fiscal-quarter rule reproduces it (the pure-calendar rule fails on the 10-K, the fiscal-quarter rule on the Q3 10-Q). **Kind: tested and unresolved.** Recorded as a carry-forward rather than guessed, because a guessed rule would look correct.
7. **The `skill_pin` recomputation.** The pin of record exists in-repo — `theses/002-evidence-validation/skill_pins.jsonl`, two agreeing records — but its stated derivation path (`scripts/dispatch.py:132`, two `plugins/…` skill roots) is **absent from this workspace**: there is no `scripts/` directory and no `plugins/` root. **Kind: not reproducible from this workspace.** The value is recorded, not fabricated and not independently confirmed. It is not `UNRESOLVED`, because a content hash does exist in-repo.
8. **The register-wide reach of §5.2.** That a DA-23 strip corrupts the instrument's derived subtotals is established here for one filing and one concept. Whether it is general is untested. **Kind: tested at n=1.**

---

## 11. Carry-forwards to the register

1. **DA-23's mechanism is per-VALUE-SIGN.** Stated as a rule: filed-positive values pass through untouched; filed-negative values are replaced by their magnitudes, within one concept, one filing, one table. `OtherNonoperatingIncomeExpense` demonstrates it in a single line (§2.2). Detectors framed as "is this concept absolutised" test the wrong hypothesis. **Register wording should say per-value, not per-concept.**
2. **The `diff = 2 × value` signature is necessary but not sufficient.** A doubled arc satisfies it too (`LesseeOperatingLeaseLiabilityPaymentsDue`: computed = 2 × reported). The discriminator is the ratio `served / filed`: 1 with a sign flip is DA-23; 2 is an arc defect. **Publish the ratio, not the diff.**
3. **DA-23 propagates into derived subtotals.** §5.2: the opex residual is reconstructed exactly as 2 × the stripped term. The register treats the strip as a presentation defect; at MRCY it corrupts values that were never directly stripped, undetectably by any closure test. **Severity upgrade recommended.**
4. **Served-series non-articulation is a portable detector.** When adjacent served periods carry opposite filed signs, the served series fails to articulate by exactly **2 × the smaller term** (24,645 vs 14,185; gap 10,460 = 2 × 5,230). Needs no external source and cannot arise from a back-solve.
5. **DA-26's magnitude is set by whether the issuer files a Q4 10-Q.** MRCY does not, so its year-end metrics row carries the ANNUAL and the ratio is **4.1–4.2×**. An issuer that does file a Q4 10-Q would show a label-only defect at ~1×. **Testable prediction; MRCY is the high-magnitude pole.**
6. **DA-24 needs a direction.** The registered concern is a gain inflating the operating line. MRCY's disposal lands on the operating line as a **cost** — $1.4M of Cicor-sale transaction costs inside `Acquisition costs and other related expenses`, 7.13% of the FY2025 operating loss ([sec205 p.33](https://agentii.ai/v/MRCY/sec205/33)) — while proceeds sit in investing. Register both directions, or say why one is immaterial.
7. **DA-30's second mechanism: two bases on one concept, second basis in a footnote only.** BWXT collapses equity scopes; MRCY collapses share-count bases (59,386 GAAP vs 60,525 non-GAAP, +1.92%, established only in footnote (2)). Two of two issuers tested have a DA-30 instance with different mechanisms, so **DA-30 is not an issuer idiosyncrasy.**
8. **A basis-disclosure footnote can itself be wrong.** Footnote (2) of [sec203 p.37](https://agentii.ai/v/MRCY/sec203/37) states its basic-vs-diluted impacts as "no impact" / "$0.01"; the arithmetic on the two bases it names gives $0.02 / $0.00 — **inverted**. An artifact complying with `basis_named` by quoting the footnote inherits the error. **The basis must be named AND checked.**
9. **`reported` in the instrument is served from the stripped store.** Five instances in one 10-K run, each equal to |filed| (§5.1), one of them carrying `status: pass` because both sides were stripped. **Two cancelled sign errors produce a pass** — so `status: pass` is not evidence of correct signs, and the DA-29 corollary is the load-bearing check rather than a formality.
10. **A candidate register entry, not DA-26.** The sec203 calculation linkbase carries **decade-stale labels on live concepts**: `CommonStockValue` labelled *"Common Stock; 45,000 shares authorized; 14,824 shares issued and outstanding at December 31, 2014 … 12,644 shares … at December 31, 2013"* and `PreferredStockValue` labelled *"no shares issued and outstanding at December 31, 2014 or 2013"* — inside a 2026 filing. Related to DA-26 (period label versus period content) but not the same rule: the period is on a **label**, and it is twelve years off rather than one quarter.
11. **Detector availability, fourth cell.** MRCY has **both** axes present (§8.1), so the census is fully testable and the identity runs in its registered form with no substitute. The instrument's opex residual is therefore a self-inconsistency rather than a cross-check disagreement — a strictly stronger finding than the resolvable-via-linkbase class (BWXT, LUNR) can support.
12. **DA-27 is strongest when the platform contradicts itself.** MRCY's served `fiscal_period` (Q1) disagrees with the platform's own calendar grid (which places the same period in FY2026 Q3) *and* with the issuer (third quarter) — and the fiscal-year end 2026-07-03 falls outside the platform's FY2026 grid entirely, into FY2027 Q1. **Recommend the self-contradiction test: compare the served label to the served grid before comparing it to the issuer.** It requires no filing and no issuer label.

---

## Sources

> Every figure asserted above resolves to the page cited. The cells were read off the pages; no
> quotation is taken from the platform's generated description field (spec §1d and the §8.3 traps).
> Page numbers were established with `read_source_pages` in every case.

| Figure | Source |
|---|---|
| Q3 FY2026 10-Q statement of operations, 3M and 9M, four columns — gross margin 69,050; restructuring (48); income (loss) from operations 5,230 / (17,344) / (14,185) / (43,177); other (expense) income, net (3,093) / 2,304 / (5,613) / (2,900); EPS (0.04) / (0.33) / (0.51) / (0.93); shares 59,422 / 58,749 / 59,386 / 58,614 | [MRCY 10-Q sec203 p.4](https://agentii.ai/v/MRCY/sec203/4) |
| Q1 FY2026 10-Q statement of operations, two columns — gross margin 62,899 / 51,790; loss from operations (8,597) / (13,418); EPS (0.21) / (0.30); shares 59,191 / 58,260 | [MRCY 10-Q sec201 p.4](https://agentii.ai/v/MRCY/sec201/4) |
| Q2 FY2026 10-Q statement of operations, 3M and 6M, four columns — revenues 232,872 / 223,125; loss from operations (10,818) / (12,415) / (19,415) / (25,833); EPS (0.26) / (0.30) / (0.47) / (0.60) | [MRCY 10-Q sec202 p.4](https://agentii.ai/v/MRCY/sec202/4) |
| FY2026 10-K statement of operations, three annual columns — revenue 983,622 / 912,020 / 835,275; gross margin 281,165 / 254,494 / 195,901; opex 280,885 / 274,121 / 343,655; income (loss) from operations 280 / (19,627) / (147,754); net loss (29,673) / (37,904) / (137,640); EPS (0.50) / (0.65) / (2.38); shares 59,460 / 58,746 / 57,738 | [MRCY 10-K sec205 p.47](https://agentii.ai/v/MRCY/sec205/47) |
| FY2026 MD&A — 53 weeks vs 52; revenue +$71.6M or 7.9%; FY2025 operating margin (2.1)%; Cicor and Star Lab disclosures | [MRCY 10-K sec205 p.32](https://agentii.ai/v/MRCY/sec205/32) |
| FY2026 MD&A cost lines — gross margin +70 bp; R&D −11.7% on ~270 headcount reductions; restructuring inside operating expenses; $1.4M of Cicor-sale acquisition costs; EAC net (18,742) / (21,070) | [MRCY 10-K sec205 p.33](https://agentii.ai/v/MRCY/sec205/33) |
| FY2026 10-K cash flows — Cicor proceeds 6,246 (investing); net cash (used in) provided by financing activities (162,739) / 1,412 / 82,680; net decrease in cash (94,793) | [MRCY 10-K sec205 p.49](https://agentii.ai/v/MRCY/sec205/49) |
| Adjusted EBITDA reconciliation, four columns — restructuring (48) / 4,931 / 5,591 / 7,231; adjusted EBITDA 36,091 / 24,690 / 101,674 / 68,169; closes 4 of 4 exactly | [MRCY 10-Q sec203 p.36](https://agentii.ai/v/MRCY/sec203/36) |
| Adjusted income and adjusted EPS — adjusted income 41,416 / 9,973; adjusted EPS $0.68 / $0.17; diluted weighted-average shares 60,525 / 59,024; footnote (2) establishing the basis | [MRCY 10-Q sec203 p.37](https://agentii.ai/v/MRCY/sec203/37) |
| Non-GAAP measures enumerated — adjusted EBITDA, adjusted income, adjusted EPS, free cash flow (no per-unit metric) | [MRCY 10-Q sec203 p.35](https://agentii.ai/v/MRCY/sec203/35) |
| Q3 FY2026 10-Q cash flows, nine months — net cash used in financing activities (15,429) / (757) | [MRCY 10-Q sec203 p.6](https://agentii.ai/v/MRCY/sec203/6) |
