---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: VRT
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
# ^ Written at pin 1.4.0. The register moved to 1.5.0 during this phase — the contract's
#   mtime (16:21) and this artifact's (16:21) are the same minute — so the disposition is
#   recorded rather than inferred. Kept at 1.4.0 for three reasons: it matches thesis.md,
#   which the `pins_match_thesis` rule requires; the 1.5.0 changelog records that "the 23
#   artifacts written at pin 1.4.0 ... all remain valid at their recorded pin; none is
#   silently re-run (Q56)", and this artifact is one of the 23 (23 artifact files on disk,
#   all at 1.4.0, including three edited after the bump); and `check_citations.py` does not
#   gate on the value. The 1.5.0 DA-29/DA-30 obligations, which the changelog DEFERS to
#   Phase 7's validation ledger, are nevertheless discharged here rather than deferred —
#   both are listed in `definitions_used` and both are answered — DA-30 in §9, DA-29 in §12 —
#   because this artifact's central finding turned out to BE a DA-30 instance and its §2
#   findings turned out to be DA-29 instance-classes. Doing it early is strictly stronger
#   than deferring it. Separately, `skill_pin` was UNRESOLVED at first write and was
#   resolved to 07d26b9c738b mid-phase by the Q57 re-derivation; see §11.9.
assumption_pin: "2"
skill_pin: "07d26b9c738b"  # Q57 resolved 2026-09-18: re-derived from plugins/agent-plugins/agentii-equity-agent/skills/agentii/recent-quarter AND plugins/vertical-plugins/equity-research-core/skills/agentii/recent-quarter — two independent roots AGREE. Algorithm dispatch.skill_version_hash() (scripts/dispatch.py:132) validated 9/9 against the six pins tabled in theses/001-technology-baseline/reproduce.md, which resolve to four separate plugin roots. Supersedes the UNRESOLVED gap recorded at first write.
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "absolute-value sign strip on a negative stored fact — tested per-period AND per-fact by the component identity (gross profit − opex) on the operating line, and by the gross-profit bound at every level. On the operating line VRT is UNEXERCISED, not clean: all 61 OperatingIncomeLoss facts in the corpus are positive. On the cash-flow subtotals VRT EXHIBITS the strip: NetCashProvidedByUsedInInvestingActivities and NetCashProvidedByUsedInFinancingActivities are stored positive where the filing prints them in parentheses. EPS × shares was not used and is inadmissible."
  - da_id: "DA-24"
    chosen_reading: "a disposal or acquisition fair-value item inside the operating subtotal — REFUTED at VRT in both directions: no gain-on-disposal or bargain-purchase line exists above Operating profit in any of the thirteen periods examined (goodwill is positive on all three 2025-26 acquisitions, so no gain on bargain purchase exists), and the one acquisition fair-value item that does sit above the operating line — the PurgeRite contingent consideration — is a CHARGE of $62.0M, i.e. DA-24's structural shape with the opposite sign. VRT therefore supplies an independent second instance of BA's §10.3 magnitude/sign objection to DA-24."
  - da_id: "DA-25"
    chosen_reading: "issuer-defined per-unit metric not reproducible from the segment tables — NOT TESTABLE at VRT: there is no object. The Q2 2026 10-Q discloses no per-unit, order, backlog or book-to-bill metric (`book-to-bill` returns zero hits in the filing; the only `backlog` hits are an intangible-asset category and forward-looking-statements boilerplate). Recorded as absence-of-object, not as a clean pass."
  - da_id: "DA-26"
    chosen_reading: "annual value carried in a fiscal_period-labelled quarterly row — CONFIRMED at VRT, and the mislabelled period is Q4. The metrics rows for FY2025/Q4 and FY2024/Q4 each carry FOUR independent twelve-month figures (revenue, operating income, net income and basic EPS), every one of which matches the 10-K annual statement exactly. The true Q4 2025 revenue is $2,880.0M; the row says $10,229.9M."
  - da_id: "DA-27"
    chosen_reading: "fiscal labels synthesised from the calendar quarter rather than read from the filing — NOT TESTABLE at VRT, and this is the interesting part: VRT's fiscal year IS the calendar year, so a calendar-synthesised label and a filing-read label are indistinguishable on every period. `fiscal_year_end_month: 12` with `fiscal_year_end_month_source: gold_companies` (not `default` as at SPCX), and `cross_validation_hint: null`. The method finding survives — the calendar synthesises FY2027 periods for a company whose latest filing is 2026-07-29 — but no VRT period can falsify it."
  - da_id: "DA-28"
    chosen_reading: "capital-structure discontinuity at or after listing — REFUTED for every period this artifact quotes: preferred stock is authorised at 5,000,000 shares and NONE issued or outstanding in either balance-sheet column, the common stock is a single 700,000,000-share class, and no convertible or warrant line appears at 30 June 2026 or 31 December 2025. The BA-analogue discontinuity is present in VRT's HISTORY and is carried, not closed: change in fair value of warrant liabilities ran $157.9M (FY2023) → $449.2M (FY2024) → nil (FY2025), i.e. a vanishing instrument that makes FY2024 and FY2025 net income non-comparable. Pre-listing 10-Qs (2018–2019) were identified but not read."
  - da_id: "DA-29"
    chosen_reading: "back-solved and opaque checks — a reconciliation that closes is not thereby a check. APPLIED, and this artifact PASSES the mechanical circularity test: every term in all thirteen component identities is a filed line item located on a cited statement page, no term is derived to fit, and no `computed` value is cited as a derivation anywhere — the instrument's `computed` column is treated throughout as an opaque assertion and appears only as evidence of instrument behaviour. VRT supplies two fresh instances of the entry's own classes. (Instance 2, `computed` not reproducible from the instrument's own tree: NetIncomeLoss computed as −125.4M and −139.1M against filed positives of 1,332.8 and 488.7; LiabilitiesAndStockholdersEquity computed as 11,146.9M against a filed 15,900.9M.) (Instance 3, `reported` is not definitionally the filed value: the cash-flow sign strip — each of those `reported` values was reconciled to the statement face before use, and two of them failed.)"
  - da_id: "DA-30"
    chosen_reading: "two bases on one concept, collapsed without a basis field. INDEPENDENT SECOND INSTANCE, and this census's headline finding — reached independently, before the 1.5.0 text was read. VRT reports its product/services split on two bases within a single filing, differing by $134.9M–$183.6M annually and $40.3M at Q2 2026, exactly compensating so every total agrees. THE BASIS IS NAMED, as the entry requires: the income-statement basis is established on the face of the condensed consolidated statements of earnings (products 2,646.7 / services 627.6 at Q2 2026); the disaggregation basis is established in Note 4 (products 2,606.4 / services & spares 667.9). BWXT's instance is a platform collapse across filings; VRT's is a within-filing split that the platform serves under two line-item labels with no basis field and no reconciling footnote, and it is the first instance where the divergence is arithmetically INVISIBLE — compensating to the tenth of a million — rather than merely unlabelled."
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: "Q2 2026 statement of earnings: net sales 3,274.3 (products 2,646.7 / services 627.6); cost of sales 2,039.4; gross profit 1,234.9; SG&A 494.4; amortization 73.7; restructuring (3.9); FX 3.9; other operating expense 28.9; operating profit 637.9 [442.4 Q2 2025; 1,078.0 / 733.1 six-month]"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 5
    url: https://agentii.ai/v/VRT/sec136/5
    located_via: read_source_pages
  - figure: "Q2 2026 balance sheets: total assets 15,900.9 / 12,212.4; total liabilities 11,143.3 / 8,271.1; total equity 4,757.6 / 3,941.3; total liabilities and equity 15,900.9 / 12,212.4; preferred stock authorised 5,000,000 shares, none issued and outstanding; common stock one class, 700,000,000 authorised, 384,936,985 / 382,553,680 outstanding"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 7
    url: https://agentii.ai/v/VRT/sec136/7
    located_via: read_source_pages
  - figure: "Q2 2026 cash flow statement: net cash provided by operating activities 1,866.6; net cash provided by (used for) investing activities (780.7) / (182.8); net cash provided by (used for) financing activities (3.0) / (32.9); increase in cash 1,085.8"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 8
    url: https://agentii.ai/v/VRT/sec136/8
    located_via: read_source_pages
  - figure: "Note 3 PurgeRite purchase price allocation: consideration transferred 1,138.3 net of cash acquired 14.4; goodwill 588.4 → 589.3; premium purchase accounting; contingent-consideration LOSS of 28.8 (three months) and 62.0 (six months) recognised within Other operating expense (income)"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 11
    url: https://agentii.ai/v/VRT/sec136/11
    located_via: read_source_pages
  - figure: "Note 3 Great Lakes ($203.5 consideration, $65.2 goodwill) and three Q2 2026 acquisitions ($336.5 gross consideration, $260.1 goodwill, $278.1 cash) — positive goodwill on every acquisition, so no gain on bargain purchase exists"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 12
    url: https://agentii.ai/v/VRT/sec136/12
    located_via: read_source_pages
  - figure: "Note 4 disaggregation: products 2,606.4 / services & spares 667.9 = 3,274.3 [Q2 2026]; products 2,118.9 / services 519.2 [Q2 2025] — against the income statement's products 2,646.7 / services 627.6, a compensating $40.3M shift on both lines"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 13
    url: https://agentii.ai/v/VRT/sec136/13
    located_via: read_source_pages
  - figure: "Note 11 segment information: operating profit Americas 571.4 / Asia Pacific 95.6 / EMEA 124.2 = 791.2; less corporate and other (79.6) less amortization (73.7) = 637.9; segment cost of sales 2,024.4 is a different basis from the income statement's 2,039.4 by exactly $15.0M of segregated R&D"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 21
    url: https://agentii.ai/v/VRT/sec136/21
    located_via: read_source_pages
  - figure: "Note 12 earnings per share: net income 497.8 / 324.2 / 887.9 / 488.7; basic shares 384,555,346; diluted 392,746,991; basic EPS $1.29 / $0.85 / $2.31 / $1.28; diluted $1.27 / $0.83 / $2.26 / $1.25"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 24
    url: https://agentii.ai/v/VRT/sec136/24
    located_via: read_source_pages
  - figure: "MD&A results of operations, verbatim: 'Margin expansion in the second quarter of 2026 was primarily driven by the mix of product and service sales.' Gross profit 1,234.9 = 37.7% of sales vs 896.6 = 34.0% (33.99%). 'Product sales increased $487.5 ... Services & Spares sales increased $148.7' — which are the Note 4 basis movements (487.5 = 2,606.4 − 2,118.9; 148.7 = 667.9 − 519.2), not the income statement's own (480.7 / 155.5)"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 28
    url: https://agentii.ai/v/VRT/sec136/28
    located_via: read_source_pages
  - figure: "MD&A cash-flow summary, in prose: 'Net cash used for investing activities was $780.7 ... compared to net cash used for investing activities of $182.8'; 'Net cash used for financing activities was $3.0 ... compared to $32.9 used for financing activities'; 'Trade working capital provided $678.8'; non-cash items 292.4 = 223.5 + 62.0 + 30.8 + 2.2 − 26.1"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 35
    url: https://agentii.ai/v/VRT/sec136/35
    located_via: read_source_pages
  - figure: "Q1 2026 statement of earnings: net sales 2,649.5 (products 2,135.8 / services 513.7) [2,036.0 / 1,649.7 / 386.3 Q1 2025]; cost of sales 1,649.8; SG&A 456.7; amortization 77.6; restructuring (4.9); FX (1.6); other operating expense 31.8; operating profit 440.1 [290.7]"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec134
    page_no: 5
    url: https://agentii.ai/v/VRT/sec134/5
    located_via: read_source_pages
  - figure: "Q1 2026 cash flow statement: net cash provided by (used for) investing activities (376.7) / (38.8); net cash provided by (used for) financing activities 11.9 / (24.9); increase in cash 401.4 = 766.8 − 376.7 + 11.9 − 0.6"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec134
    page_no: 8
    url: https://agentii.ai/v/VRT/sec134/8
    located_via: read_source_pages
  - figure: "Q1 2025 disaggregation: products 1,611.1 / services & spares 424.9 = 2,036.0 — against the income statement's 1,649.7 / 386.3, a compensating $38.6M shift"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec134
    page_no: 13
    url: https://agentii.ai/v/VRT/sec134/13
    located_via: read_source_pages
  - figure: "Q3 2025 statement of earnings: net sales 2,675.8 [Q3 2024 2,073.5] and nine-month 7,349.9 [5,665.4]; operating profit 516.7 / 371.6 / 1,249.8 / 910.2; change in fair value of warrant liabilities nil in 2025 vs 67.2 / 269.2 in 2024"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec133
    page_no: 5
    url: https://agentii.ai/v/VRT/sec133/5
    located_via: read_source_pages
  - figure: "FY2025 MD&A results of operations: net sales 10,229.9 [8,011.8]; gross profit 3,715.2 [2,934.2]; operating profit 1,829.7 [1,367.4]; net income 1,332.8 [495.8]; change in fair value of warrant liabilities nil [449.2]; 'Product sales increased $1,961.8 ... Services & spares sales increased $256.3' — the disaggregation-basis movements"
    ticker: VRT
    form_type: 10-K
    citation_id: sec110
    page_no: 41
    url: https://agentii.ai/v/VRT/sec110/41
    located_via: read_source_pages
  - figure: "FY2025 consolidated statement of earnings: net sales 10,229.9 / 8,011.8 / 6,863.2 (products 8,390.6 / 6,393.5 / 5,406.1; services 1,839.3 / 1,618.3 / 1,457.1); cost of sales 6,514.7 / 5,077.6 / 4,462.7; operating profit 1,829.7 / 1,367.4 / 872.2; net income 1,332.8 / 495.8 / 460.2; basic EPS $3.49 / $1.32 / $1.21"
    ticker: VRT
    form_type: 10-K
    citation_id: sec110
    page_no: 62
    url: https://agentii.ai/v/VRT/sec110/62
    located_via: read_source_pages
  - figure: "Note 4 disaggregation of revenues, FY2025 / FY2024 / FY2023: products 8,207.0 / 6,245.2 / 5,271.2; services & spares 2,022.9 / 1,766.6 / 1,592.0 — against the income statement's 8,390.6 / 6,393.5 / 5,406.1 and 1,839.3 / 1,618.3 / 1,457.1, a compensating $183.6M / $148.3M / $134.9M shift on each line"
    ticker: VRT
    form_type: 10-K
    citation_id: sec110
    page_no: 76
    url: https://agentii.ai/v/VRT/sec110/76
    located_via: read_source_pages
---

# VRT — Recent-Quarter Register Census, Q2 2026 (Phase 3, PIL-3)

**Headline.** The instrument is silent on VRT's operating income in every accession tested — the seven-arc concept returns no row — and where the instrument does speak, one of its true findings arrives as a `fail` indistinguishable from its thirty-seven false ones. VRT's operating line is nonetheless clean on all thirteen periods by the component identity. VRT's actual exhibited defect is a sign strip, but not where Phase 2 looked: it is on the **cash-flow subtotals**, proved per-fact by the sign of the underlying value — and it makes VRT the **second instance of the register's newest DA-23 row** (clean at every subtotal, stripped at a component), and the first where the stripped component lies on a different statement. Separately, the **within-filing two-basis revenue split is real, systematic, present in all seven periods tested including three annual ones, exactly compensating, and invisible to every detector in the register** — reached independently in this census, it is the **second instance of DA-30**, and the first where the divergence is arithmetically invisible rather than merely unlabelled. VRT also enters the DA-26 census as a new issuer (20 of 20, twice consecutively), and supplies two fresh instances of DA-29's classes.

**Register version note.** This artifact was written at `constitution_pin: 1.4.0`. The register moved to **1.5.0** in the same minute (contract and artifact mtimes both 16:21), adding **DA-29** and **DA-30** and correcting DA-23 twice. The 1.5.0 changelog *defers* the DA-29/DA-30 obligations on the 23 artifacts pinned at 1.4.0 to Phase 7's validation ledger. This artifact discharges both anyway, in §9 and §12 — they were answered from the filings before the 1.5.0 text was read, which is why DA-30's "state where the basis was established" requirement is met without having been copied from it.

Inheritance: Phase 2's VRT artifact (`artifacts/VRT/2026-09-18_1500_unit-economics_methodology.md`, PIL-2) is cited, not re-derived. Its in-line component derivation, its 37.71% gross margin, its 19.68% → 20.40% services-weight movement and its seven-arc inventory are all confirmed exactly at source by this census; **no correction to Phase 2 is owed.** What Phase 2 could not do — because PIL-2 asked about unit economics and this pillar asks about extraction — is the per-fact sweep, the detector-availability verdict, and the annual-level test of the two-basis split. Those are added here.

**⚠️ The governing rule for this artifact, applied literally: DA-23 runs on every period quoted, at fact level.** Thirteen periods are quoted below. The component identity is shown in-line for all thirteen. Section 1 is that table.

## Summary verdicts

| DA | Register test | VRT verdict |
|---|---|---|
| **DA-23** | `\|x\|` strip on a negative fact, any level failing the gross-profit bound | **EXHIBITED — but not on the operating line, and the register's census cannot see where it is.** Operating line: 13/13 periods close exactly by the component identity; 61/61 `OperatingIncomeLoss` facts positive → the strip channel is **unexercised there, not clean**, since the register's own census row lists VRT among the profitable issuers it calls unaffected (a profitable issuer cannot have its *sign* stripped, so the row is inapplicable rather than informative). Cash-flow subtotals: **stripped** — investing (780.7) stored +780.7 in two accessions, financing (3.0) stored +3.0. **VRT is the second instance of the 1.5.0 BWXT row — clean at every subtotal, stripped at a component — and the first where the stripped component sits on a different STATEMENT.** §3. |
| **DA-24** | disposal gain inside the operating line | **REFUTED, both signs.** No disposal or bargain-purchase line above `Operating profit` in any period; goodwill positive on all three acquisitions. The one acquisition fair-value item above the operating line is PurgeRite contingent consideration — a **$62.0M charge**. |
| **DA-25** | issuer-defined per-unit metric not reproducible from segment tables | **NOT TESTABLE — no object.** No per-unit, order, backlog or book-to-bill metric in the 10-Q. |
| **DA-26** | annual value mislabelled as a quarter | **CONFIRMED. Mislabelled period = Q4.** Two rows, four annual figures each, all matching the 10-K. |
| **DA-27** | fiscal labels synthesised from the calendar quarter | **NOT TESTABLE.** VRT's fiscal year is the calendar year, so synthesised and read labels are indistinguishable. Method finding survives. |
| **DA-28** | capital-structure discontinuity | **REFUTED for all quoted periods.** Preferred authorised, none issued; single common class; no convertible, no warrant line. Historical warrant discontinuity carried. |
| **DA-29** | a reconciliation that closes is not thereby a check; `computed` is opaque | **PASSES the circularity test** — every term in all thirteen identities is a filed line item on a cited page; no `computed` value is cited as a derivation anywhere. **And VRT supplies two fresh instances of its classes** — `computed` unreproducible from the instrument's own tree, and `reported` not definitionally the filed value. §12. |
| **DA-30** | two bases on one concept, collapsed without a basis field | **INDEPENDENT SECOND INSTANCE — and this census's headline finding.** VRT reports its product/services split on two bases within one filing, 7/7 periods, differing by $134.9M–$183.6M annually. Compensating, so invisible to every total-based check by construction. **Basis named and its establishment recorded in §9.** |
| **(not registered)** | instrument silence on a concept that has arcs | **REPRODUCED, and moved to a NEW class.** 3/3 VRT accessions; 5 accessions / 2 issuers / arc counts 7, 5, 4. The register's existing coverage hole is about a concept *absent or segment-only* in the data; VRT's concept is **present, fully filed, seven arcs deep, and the validator is still silent** — a validator-completeness gap, not a data-availability gap. §2.1. |

## 1. True operating income — the component identity, thirteen periods

Every figure below is the filing's own line item, read at source. `opex` is the sum of the operating-expense lines as the filing presents them, benefits included with their printed sign.

| Period | Gross profit | Operating-expense lines | Σ opex | GP − opex | Filed operating profit | Δ |
|---|---|---|---|---|---|---|
| Q1 2026 | 2,649.5 − 1,649.8 = **999.7** | 456.7 + 77.6 − 4.9 − 1.6 + 31.8 | 559.6 | **440.1** | 440.1 | 0 |
| Q2 2026 | 3,274.3 − 2,039.4 = **1,234.9** | 494.4 + 73.7 − 3.9 + 3.9 + 28.9 | 597.0 | **637.9** | 637.9 | 0 |
| H1 2026 | 5,923.8 − 3,689.2 = **2,234.6** | 951.1 + 151.3 − 8.8 + 2.3 + 60.7 | 1,156.6 | **1,078.0** | 1,078.0 | 0 |
| Q1 2025 | 2,036.0 − 1,349.5 = **686.5** | 346.3 + 46.0 + 1.1 + 2.6 − 0.2 | 395.8 | **290.7** | 290.7 | 0 |
| Q2 2025 | 2,638.1 − 1,741.5 = **896.6** | 395.6 + 46.9 + 1.9 + 2.3 + 7.5 | 454.2 | **442.4** | 442.4 | 0 |
| H1 2025 | 4,674.1 − 3,091.0 = **1,583.1** | 741.9 + 92.9 + 3.0 + 4.9 + 7.3 | 850.0 | **733.1** | 733.1 | 0 |
| Q3 2025 | 2,675.8 − 1,665.1 = **1,010.7** | 414.3 + 48.2 + 30.7 + 0.9 − 0.1 | 494.0 | **516.7** | 516.7 | 0 |
| 9M 2025 | 7,349.9 − 4,756.1 = **2,593.8** | 1,156.2 + 141.1 + 33.7 + 5.8 + 7.2 | 1,344.0 | **1,249.8** | 1,249.8 | 0 |
| Q3 2024 | 2,073.5 − 1,317.1 = **756.4** | 334.6 + 45.3 + 6.3 + 5.3 − 6.7 | 384.8 | **371.6** | 371.6 | 0 |
| 9M 2024 | 5,665.4 − 3,601.4 = **2,064.0** | 1,012.4 + 137.1 + 4.1 + 8.7 − 8.5 | 1,153.8 | **910.2** | 910.2 | 0 |
| FY2023 | 6,863.2 − 4,462.7 = **2,400.5** | 1,312.3 + 181.3 + 28.6 + 16.0 − 9.9 | 1,528.3 | **872.2** | 872.2 | 0 |
| FY2024 | 8,011.8 − 5,077.6 = **2,934.2** | 1,374.0 + 184.2 + 5.3 + 9.3 − 6.0 | 1,566.8 | **1,367.4** | 1,367.4 | 0 |
| FY2025 | 10,229.9 − 6,514.7 = **3,715.2** | 1,617.8 + 200.4 + 54.5 + 12.0 + 0.8 | 1,885.5 | **1,829.7** | 1,829.7 | 0 |

Thirteen periods, thirteen exact closes, zero residue. Q2 2026 is Phase 2's derivation, reproduced: gross profit 1,234.9 ([📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec136/5)) minus opex 597.0 = 637.9 exactly. Phase 2's 37.71% is 1,234.9 ÷ 3,274.3.

**DA-29 compliance — the source of every term, stated rather than assumed.** A reconciliation that closes is not thereby a check: if any term appears nowhere in the source, the closure is a back-solve, and a back-solve closes exactly. So the test runs on the terms, not the closure. Every term above is a filed line item on the face of a statement cited in this artifact — net sales, cost of sales, gross profit, SG&A, amortization, restructuring, foreign currency, other operating expense and operating profit are all printed lines on the condensed consolidated statements of earnings ([📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec136/5), [📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec134/5), [📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec133/5), [📄 VRT 10-K p.62](https://agentii.ai/v/VRT/sec110/62)); the nine-month figures used for the cross-foot are printed in the comparatives on the same pages. **No term is derived to fit, nothing is carried from an earlier period to make a later one close, and no value in this artifact is back-solved.** Explicitly: **no `computed` value from the instrument is cited as a derivation anywhere in this artifact** — the `computed` column is an opaque assertion that the instrument does not make reproducible from its own returned tree, so it appears in §2 only as *evidence about instrument behaviour*, never as a source. That is what qualifies the table: it is thirteen independent reconciliations, not one reconciliation shown thirteen times.

**Cross-foot, independent of any single statement.** Q1 2025 + Q2 2025 + Q3 2025 = 2,036.0 + 2,638.1 + 2,675.8 = **7,349.9** = the nine-month figure printed on the Q3 2025 statement ([📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec133/5)). And the nine-month column itself closes: 2,593.8 − 1,344.0 = 1,249.8. So the quarterly and year-to-date presentations agree with each other, and each agrees with its own components.

**The segment level closes too, in every column.** For Q2 2026 ([📄 VRT 10-Q p.21](https://agentii.ai/v/VRT/sec136/21)): Americas 2,070.8 − 1,208.1 − 126.7 − 86.4 − 30.7 − 47.5 = 571.4; Asia Pacific 719.9 − 539.0 − 33.7 − 29.1 − 17.0 − 5.5 = 95.6; EMEA 483.6 − 277.3 − 30.8 − 24.4 − 10.1 − 16.8 = 124.2. Total 791.2, less corporate and other (79.6), less amortization (73.7) = **637.9**. Both segment columns and the reconciliation are exact.

**A second basis for cost of sales, which reconciles — and is therefore not a defect.** The segment table's cost of sales totals 2,024.4 against the income statement's 2,039.4, and the footnote explains it: segment cost of sales is "exclusive of engineering, research and development costs," shown separately as 139.9. The two taxonomies sum to the same total cost: 2,024.4 + 191.2 + 139.9 + 57.8 + 69.8 + 79.6 + 73.7 = **2,636.4**, and 2,039.4 + 494.4 + 73.7 − 3.9 + 3.9 + 28.9 = **2,636.4**. The $15.0M difference on the cost-of-sales line is fully explained and fully disclosed. §1c wants both bases reported; both are, above. This is the control case for §9 below: a competing basis that reconciles and is footnoted is not a register gap. A competing basis that reconciles and is **not** explained is.

**The inadmissible test, recorded as not used.** `EPS × shares` would reproduce here — 497.8 ÷ 384.555 = $1.294 → $1.29 basic, 497.8 ÷ 392.747 = $1.267 → $1.27 diluted ([📄 VRT 10-Q p.24](https://agentii.ai/v/VRT/sec136/24)) — and that is precisely why it is inadmissible: it reproduces only because VRT's earnings are positive in all four columns, and it inverts wherever a metrics block has no negative values to draw on. It was not used as a sign test anywhere in this artifact.

## 2. Instrument values — the `computed`/`reported` pair, read as a pair

`validate_calculation` was run on all three VRT accessions. **57 result rows: 15 `pass`, 3 `warn`, 39 `fail`.**

### 2.1 The silent concept — the detector-coverage gap, reproduced at VRT

**Not one of the 57 rows is `us-gaap:OperatingIncomeLoss`.** The Q2 2026 filing: 17 rows, none. Q1 2026: 13 rows, none. FY2025 10-K: 27 rows, none. Meanwhile `get_calculation_tree` on the Q2 2026 accession shows the role `UNAUDITEDCONDENSEDCONSOLIDATEDSTATEMENTSOFEARNINGS**LOSS**` carrying **exactly seven arcs into `us-gaap:OperatingIncomeLoss`**:

| child concept | weight |
|---|---|
| `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` | +1 |
| `us-gaap:CostOfGoodsAndServicesSold` | −1 |
| `us-gaap:SellingGeneralAndAdministrativeExpense` | −1 |
| `vrt_AmortizationOfIntangibleAssetsExcludingCostsOfSales` | −1 |
| `us-gaap:RestructuringCharges` | −1 |
| `us-gaap:ForeignCurrencyTransactionGainLossBeforeTax` | +1 |
| `us-gaap:OtherOperatingIncomeExpenseNet` | +1 |

Seven arcs, a fully determined parent, and no row. **Silence is the instrument's output here, and silence is indistinguishable from a clean pass.** With VRT added, the pattern stands at **five accessions across two issuers at arc counts 7, 5 and 4 — zero rows, every time.** VRT is not the idiosyncrasy; VRT is the instance, and it is now the strongest one, because seven arcs is the most determinate case tested and it is still silent.

**This is a new class of the register's coverage hole, and the register's existing remedy does not reach it.** The hole as registered is about *data availability*: `OperatingIncomeLoss` is absent or segment-only at MRK, BMY and WWD, and the register's disposition is that "absence must be recorded as `UNRESOLVABLE-FROM-PLATFORM`, never as a passed check" — correct, and it also records that the absence is *presentational*, resolved by reading the statement face. **VRT's concept is not absent.** It is filed at every level, it is a first-class consolidated subtotal among the profitable-issuer census row, it sits under a fully populated seven-arc calculation linkbase that the instrument itself returns, and the validator produces **no row at all**. So:

| Coverage-hole cell | Register's current disposition | VRT |
|---|---|---|
| Concept absent from the data (MRK, BMY, WWD) | `UNRESOLVABLE-FROM-PLATFORM`; a zero-fact return is evidence about the *concept name*, not the issuer | not VRT's case |
| Concept present but no identity available (LUNR) | Detector 1 unavailable; fall back to detector 2 with its gross-margin caveat | not VRT's case |
| **Concept present, tree complete, validator silent** | **no disposition exists** | **VRT — 3 of 3 accessions, 7 arcs** |

The third cell is not a data problem at all; it is a **validator-completeness** problem, and the disposition it needs is different in kind. `UNRESOLVABLE-FROM-PLATFORM` says *the data is public but unreachable* — but VRT's data is reachable: the arcs, the components and the values are all present, and the component identity closes thirteen times out of thirteen. Nothing is unresolvable. What is missing is the *check*. **The disposition for this cell is not "unresolvable" but "the artifact must run Detector 1 itself, and must never read the validator's silence as a result."** The register already mandates the component derivation in-line; what VRT adds is *why* the mandate is load-bearing rather than belt-and-braces — for this class of issuer the instrument cannot be the backstop, because on the one concept the thesis most depends on, **it produces no output to be wrong about.** For the universe-wide census the consequence is a denominator correction: VRT is counted in the DA-23 profitable-issuer census row as unaffected, and counted nowhere in the coverage-hole census, so **a validator that never ran on VRT and a validator that ran and passed on VRT are the same row in every tally the programme currently keeps.**

### 2.2 A true `reported` corruption — the sign strip, on the cash-flow subtotals

| Concept | `computed` | `reported` | Filed value | Verdict |
|---|---|---|---|---|
| `NetCashProvidedByUsedInInvestingActivities`, H1 2026 | −780,700,000 | **+780,700,000** | **(780.7)** | `fail` — `reported` stripped |
| `NetCashProvidedByUsedInFinancingActivities`, H1 2026 | −3,000,000 | **+3,000,000** | **(3.0)** | `warn` — `reported` stripped |
| `NetCashProvidedByUsedInInvestingActivities`, Q1 2026 | −376,700,000 | **+376,700,000** | **(376.7)** | `fail` — `reported` stripped |
| `NetCashProvidedByUsedInFinancingActivities`, Q1 2026 | +11,900,000 | +11,900,000 | **+11.9** | `pass` — **correct, and genuinely positive** |

The filed signs are unambiguous three ways over: the statement prints parentheses ([📄 VRT 10-Q p.8](https://agentii.ai/v/VRT/sec136/8)), the MD&A says in prose "net cash **used for** investing activities was $780.7" and "net cash **used for** financing activities was $3.0" ([📄 VRT 10-Q p.35](https://agentii.ai/v/VRT/sec136/35)), and the statements cross-foot only with the negative sign: 1,866.6 − 780.7 − 3.0 + 2.9 = **1,085.8** ✓ at H1, and 766.8 − 376.7 + 11.9 − 0.6 = **401.4** ✓ at Q1 ([📄 VRT 10-Q p.8](https://agentii.ai/v/VRT/sec134/8)). Take the stored positive and the H1 statement balances to 2,647.2 — no such figure appears anywhere.

**This is the per-fact rule, proved on a new axis.** The register's HAWK evidence showed the strip varying within one column (net income clean, EPS stripped). VRT shows it varying within one concept across adjacent periods: `NetCashProvidedByUsedInFinancingActivities` is **correct at +11.9 in Q1 2026 and stripped at −3.0 in H1 2026** — the same tag, the same company, the same fiscal year, six months apart. No period-level, concept-level or issuer-level rule explains that. **Only the sign of the value does.**

### 2.3 The `computed` column is independently broken — in the same run

The same three runs contain the inverse: rows where `reported` matches the filing and `computed` is garbage.

| Concept | `computed` | `reported` | Filed | Note |
|---|---|---|---|---|
| `NetIncomeLoss`, FY2025 10-K | **−125,400,000** | 1,332,800,000 | 1,332.8 ([📄 VRT 10-K p.62](https://agentii.ai/v/VRT/sec110/62)) | computed negative for a positive year |
| `PropertyPlantAndEquipmentNet`, 10-K | −391,900,000 | 625,100,000 | — | computed negative |
| `LiabilitiesAndStockholdersEquity`, Q2 2026 | 11,146,900,000 | **15,900,900,000** | 15,900.9 ([📄 VRT 10-Q p.7](https://agentii.ai/v/VRT/sec136/7)) | `reported` correct, computed short |
| `NetCashProvidedByUsedInOperatingActivities`, Q2 2026 | 171,100,000 | 1,866,600,000 | 1,866.6 ([📄 VRT 10-Q p.8](https://agentii.ai/v/VRT/sec136/8)) | `reported` correct |
| `IncreaseDecreaseInOperatingCapital`, Q2 2026 | −706,600,000 | 678,800,000 | 678.8, "provided" ([📄 VRT 10-Q p.35](https://agentii.ai/v/VRT/sec136/35)) | `reported` correct, computed negative |
| `NetIncomeLoss`, H1 2025 comparative | **−139,100,000** | 488,700,000 | 488.7 ([📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec136/5)) | computed negative on a comparative |

So the two columns are unreliable in opposite directions inside a single call: **`computed` correct where `reported` is stripped (§2.2), and `reported` correct where `computed` is collapsed (§2.3).** Reading "only the `computed` vs `reported` pair" is necessary but not sufficient — the pair is not a controlled comparison, and neither column can be trusted as the reference. The filing is the reference.

### 2.4 `pass` does not certify — the vacuous pass

The FY2025 10-K's three passes include `EffectiveIncomeTaxRateContinuingOperations` with **`computed`: 0 and `reported`: 0** — both sides empty, status `pass`. A row that asserts agreement between two absences is the purest form of the rule that `pass` certifies nothing. The Q2 2026 run also contains three passes that are **genuine** (`AssetsCurrent` 9,984.9 = 9,984.9, `InventoryNet` 2,522.7 = 2,522.7, `NetIncomeLoss` 497.8 = 497.8), so `pass` is neither reliably vacuous nor reliably meaningful. It carries no evidential weight either way.

### 2.5 The same defect, graded differently by size

The investing strip (diff 1,561.4M) is graded `fail`; the financing strip (diff 6.0M) is graded `warn`. **Identical defect class, identical mechanism, different status — decided by magnitude alone.** A register entry keyed on `fail` status would silently drop the financing strip.

### 2.6 The false-positive rate, measured at VRT

Of the 39 `fail` rows, **two** correspond to a genuinely corrupted stored fact (the investing strip in two accessions); the remaining **37** are `computed`-column artifacts. That is 94.9% false positives on `fail`. Adding the two `warn`-tier rows, three true defects sit among 42 non-pass rows — **92.9%, independently reproducing the register's 93% figure from a new issuer.** The operational consequence is sharper than the statistic: **at VRT the instrument's one true finding arrives wearing the uniform of its thirty-seven false ones.** There is no feature of the investing-strip row — not its status, not its magnitude, not its concept class — that distinguishes it from the computed-column collapses beside it. A reviewer calibrated to discount 93% of `fail`s will discount the true one too. This is the mechanism by which the instrument's silence at `OperatingIncomeLoss` (§2.1) and its noise everywhere else combine into a single failure mode: **the instrument produces no signal that can be acted on without going back to the filing.**

### 2.7 A segment-dimensioned fact presented as consolidated

The Q2 2026 filing's own `income_statement` highlights carry `ResearchAndDevelopmentExpense` = **86,400,000** with `dimensions` set to `ConsolidatedItemsAxis: OperatingSegmentsMember` **and** `StatementBusinessSegmentsAxis: AmericasSegmentMember`. 86.4 is exactly the Americas segment's engineering/R&D line ([📄 VRT 10-Q p.21](https://agentii.ai/v/VRT/sec136/21)); the segment total is 139.9. A single-segment fact is served as the company's R&D, and nothing in the payload flags it beyond a `dimensions` field a consumer may not read. This is the register's defect 3 — "`reported` can be a SEGMENT TOTAL" — reproduced at VRT in the metadata layer rather than the validator layer.

### 2.8 The highlights block mixes two prior year-ends

The balance-sheet highlights for the Q2 2026 accession serve `Assets` = 12,212,400,000 at `period_instant` **2025-12-31** and `StockholdersEquity` = 2,434,300,000 at `period_instant` **2024-12-31**, alongside `LongTermDebt` at 2025-12-31. Neither date is the filing's own. Both values are correct *for the dates attached* — 12,212.4 is the FY2025 year-end and 2,434.3 the FY2024 year-end — so this is not a wrong number but a wrong period, served in the same block as correctly-dated debt. The metrics table for the same filing is correct (assets 15,900.9, liabilities 11,143.3, equity 4,757.6; and 11,143.3 + 4,757.6 = 15,900.9 ✓). **One accession, two balance-sheet surfaces, one right and one serving two earlier year-ends without a label.**

### 2.9 Platform page numbers do not match printed footers

VRT's offsets, measured: sec136 constant **+3** (platform 5 → footer 2; 7 → 4; 8 → 5; 11 → 8; 12 → 9; 13 → 10; 21 → 18; 24 → 21; 28 → 25; 35 → 32); sec134 constant **+3** (5 → 2; 8 → 5; 13 → 10); sec133 constant **+3** (5 → 2); sec110 constant **+2** (41 → 39; 62 → 60; 76 → 74). The offset is constant within an accession and differs between accessions of the same issuer and the same form type — extending BA's (2, 2, 6) observation. The rule holds: **cite the platform's page number, and never "correct" a right citation into a wrong one.** Every citation in this artifact is a platform page number.

## 3. DA-23 verdict — per period, per fact

**Operating line: clean by the component identity in 13 of 13 periods, and satisfying the gross-profit bound in 13 of 13.** The bound test — does operating profit exceed gross profit at any level? — holds everywhere: at Q2 2026, 637.9 < 1,234.9 consolidated, and 571.4 / 95.6 / 124.2 all positive and below their segments' gross profit. At the 10-K, 1,829.7 < 3,715.2. No level fails the bound, so the register's second DA-23 trigger never fires.

**But the bound is doing almost no work here, and the artifact should say so rather than bank the 13-of-13.** The register's own corrected note on detector 2 is that its power scales **inversely with gross margin** — it is "near-useless at high-margin issuers" (a false negative at every level at SPCX, ~65% gross margin) and only bites at low-margin issuers (4 of 4 at FLY, ~20%). **VRT's gross margin is 37.7%** — mid-range, and a threshold that a genuinely corrupted operating figure could sit under while remaining plausible. 637.9 comfortably below 1,234.9 confirms nothing about the *sign* of either; a strip that turned 637.9 into a plausible-looking number would not trip it. **The 13-of-13 that carries weight is Detector 1, the component identity, not the bound.** The correct reading of this section is therefore narrow and should not be paraphrased upward: VRT's operating line is exact by construction against filed components, and the bound adds a weak screen that happens not to fire.

**But "clean" is the wrong word for the operating line, and the distinction matters.** Every one of the **61 `us-gaap:OperatingIncomeLoss` facts in the corpus** — FY2019 through H1 2026, quarterly, six-month and annual durations, both primary and secondary sources — is **positive**. The smallest is $19.0M (H1 2022); the largest $1,829.7M (FY2025). **There is no negative operating-income fact in VRT's history for the `|x|` channel to act on.** The correct disposition is therefore *unexercised*, not *clean*: the operating line passes DA-23 because there is nothing for DA-23 to do there. Phase 2's clearance — "operating_income verified against components; VRT is NOT flipped" — is right, and its basis is now extended: it is right for the strong reason (no negative exists by construction of a consistently profitable operating line), not merely the weak one (no failure observed).

**And the register already lists VRT in its "Clean" row — which is exactly why the label is inapplicable rather than reassuring.** The DA-23 census reads "**19 of 19 profitable issuers are unaffected**," and VRT is named among them. But an absolute-value operation **cannot** strip the sign of a positive number, so for every issuer in that row the sign channel is inert by arithmetic, not by merit. The row measures *"is this issuer's sign corrupted?"* and answers a question that the issuer's profitability has already pre-answered. **The 1.5.0 correction to the same entry makes this concrete from the other direction: BWXT is "clean at every subtotal, stripped at a component" — and the register's own conclusion is that "a census that tests only the parent concepts reports a clean issuer while a component of that same statement is sign-corrupted."** VRT's operating line is unexercised; the only way to find where VRT *is* exercised is to look outside the parent concepts and outside the income statement.

**And VRT does exhibit the strip — elsewhere, and provably.** On the cash-flow subtotals (§2.2), two accessions, three facts, the stored value is the absolute value of the filed negative. This is new relative to Phase 2, which examined the operating line only. The finding separates two questions that "VRT is DA-23-clean" had conflated: *is the strip live in VRT's extraction pipeline?* — **yes, demonstrated** — and *does it touch the operating line?* — **no, because no negative exists there.**

**VRT is the second instance of the register's newest DA-23 row, and it extends that row's scope by one statement.** BWXT is "clean at every subtotal, stripped at a component," registered at the same phase as the 1.5.0 bump; the component it strips is `GainLossOnSalesOfAssetsAndAssetImpairmentCharges` — an **income-statement** component one level below the subtotals. VRT's stripped component is a cash-flow subtotal, `NetCashProvidedByUsedInInvestingActivities` / `…FinancingActivities`, i.e. **the second and third sections of the statement of cash flows rather than the top of the income statement.** The register's consequence line — "component-level census is a distinct requirement from subtotal-level census" — is therefore correct but not yet wide enough: the requirement VRT supplies is **statement-level** census. An issuer can be clean at every subtotal on every statement the census reads and still be sign-corrupted on a statement the census never opens, and the two cases now on the register (BWXT below the subtotals, VRT on another statement) are failures of two different omissions. Note also that BWXT's strip was marked `pass` by the instrument; VRT's was marked `fail` among 37 other false ones — **the same defect, arriving under both status labels, which is the §2.6 point restated at the level of the register's own newest entry.**

**The per-fact table.** For each fact quoted in this artifact that carries a sign, the DA-23 status:

| Fact class | Periods | Status | Basis |
|---|---|---|---|
| `OperatingIncomeLoss` (consolidated) | all 13 | **clean / unexercised** | component identity exact; 61/61 facts positive |
| `OperatingIncomeLoss` (segment) | Q2 2026, all 3 segments | **clean** | segment columns close exactly |
| `GrossProfit` | all 13 | **clean — never stripped** | all positive, and each equals sales − cost of sales |
| `NetIncomeLoss` | all 13 | **clean in the filing; computed column corrupt in 2** | filed values positive throughout; validator `computed` returned −139.1M and −125.4M (§2.3) — a **`computed`**-side sign inversion, distinct from the `reported`-side strip |
| `NetCashProvidedByUsedInInvestingActivities` | Q1 2026, H1 2026 | **STRIPPED** | filed (376.7) / (780.7); stored +376.7 / +780.7 |
| `NetCashProvidedByUsedInFinancingActivities` | H1 2026 | **STRIPPED** | filed (3.0); stored +3.0 |
| `NetCashProvidedByUsedInFinancingActivities` | Q1 2026 | **clean** | filed +11.9; stored +11.9; the sign discriminates |
| `EarningsPerShareBasic` / `Diluted` | all 4 columns of Q2 2026 | **clean** | all positive; and the inadmissible test was not used |
| `CostOfGoodsAndServicesSold` | all 13 | **clean** | all positive; feeds the identity |

**Disposition: DA-23 CONFIRMED as an exhibited defect at VRT, on the cash-flow subtotals, 3 facts across 2 accessions; NOT exhibited on the operating line, where it is unexercised rather than passed.** For the register: **VRT joins the BWXT row as a second instance, on a different statement**, and its existing placement in the "19 of 19 profitable issuers are unaffected" row should be annotated as *sign-inapplicable* rather than *clean*, or the census row will keep counting a channel that cannot run.

## 4. DA-24 — refuted in both directions

The register's DA-24 test is a disposal gain flowing through the operating line. VRT's income statement has no disposal or gain-on-sale line, in any of the four statements read. The lines between gross profit and operating profit are the same set in every period — SG&A, amortization of intangibles, restructuring, foreign currency, other operating expense — and **every non-operating item the company does carry sits below the operating subtotal**: loss on extinguishment of debt 6.2 ([📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec134/5)), interest, other non-operating expense, and change in fair value of warrant liabilities (157.9 / 449.2 / nil; [📄 VRT 10-K p.62](https://agentii.ai/v/VRT/sec110/62)). VRT's operating-line discipline is clean in all thirteen periods.

**Acquisition accounting does not put a gain above the operating line.** Note 3 shows goodwill — which is consideration *in excess of* fair value of net assets — on all three acquisitions: PurgeRite 588.4 → 589.3, Great Lakes 65.2, three Q2 2026 acquisitions 260.1 ([📄 VRT 10-Q p.11](https://agentii.ai/v/VRT/sec136/11), [p.12](https://agentii.ai/v/VRT/sec136/12)). Positive goodwill everywhere means **no gain on bargain purchase exists anywhere in the period**, and by construction goodwill is the residual that would go negative if one did.

**What VRT does put above the operating line is DA-24's structural shape with the opposite sign.** The PurgeRite contingent-consideration remeasurement is recognised in "Other operating expense (income)" — **a loss of $28.8M for the quarter and $62.0M for the six months** ([📄 VRT 10-Q p.11](https://agentii.ai/v/VRT/sec136/11)); Q1 2026 carries $33.2M ([📄 VRT 10-Q p.8](https://agentii.ai/v/VRT/sec134/8)). It is a non-cash, non-operating, acquisition-fair-value item inside the operating subtotal — exactly the exposure DA-24 exists to catch, arriving as a **charge**. BA's §10.3 objection ("the register's DA-24 test is satisfied by $(1)M and by $9,566M alike") is a magnitude complaint; VRT supplies the **sign** companion to it. A test phrased as "disposal *gain*" is blind to this item, and the item is the same structural hazard. **Carry-forward: DA-24 should be restated as any non-operating or acquisition fair-value item inside the operating subtotal, either sign, with a magnitude clause** — VRT is the second independent instance of the objection, from the opposite direction.

## 5. DA-25 — no object

DA-25 tests an issuer-defined per-unit metric that cannot be reproduced from the segment tables. VRT's Q2 2026 10-Q discloses no such metric. `book-to-bill` returns **zero** hits in the filing; `backlog` returns two pages, one of which is "order backlog" as a finite-lived intangible asset category and the other is forward-looking-statements boilerplate — neither a metric block. There is no orders, backlog, book-to-bill, per-unit or per-installation figure anywhere in the document.

**Disposition: NOT TESTABLE at VRT — absence of object, recorded as such.** This is not a clean pass and must not be counted as one: a DA that has nothing to test has not been tested. For the universe census it is a coverage fact — DA-25's denominator is issuers that disclose a per-unit metric, and VRT is not one of them. VRT's only issuer-defined measures are non-GAAP margin and organic-sales reconciliations, which are reconcilable by construction and outside DA-25's definition. The Q2 2026 earnings call was not read (scope: this task's sources are the filing set); if VRT discloses an orders or book-to-bill metric verbally it would sit in the transcript, and that is recorded as unverified rather than as absence.

## 6. DA-26 — CONFIRMED, mislabelled period **Q4**

The metrics table serves a row labelled `fiscal_period: "Q4"`, `period_end_date: 2025-12-31`, carrying **four** figures. Every one is the twelve-month value.

| Field in the "Q4 2025" row | Row value | Twelve-month value, from the 10-K | Verdict |
|---|---|---|---|
| `revenues` | 10,229,900,000 | 10,229.9 ([📄 VRT 10-K p.62](https://agentii.ai/v/VRT/sec110/62)) | annual |
| `operating_income` | 1,829,700,000 | 1,829.7 (same page) | annual |
| `net_income_loss` | 1,332,800,000 | 1,332.8 (same page) | annual |
| `eps_basic` | 3.49 | $3.49 (same page) | annual |

**Arithmetic proof that the row is not a quarter.** The true Q4 2025 revenue is the annual figure less the nine-month figure: 10,229.9 − **7,349.9** = **2,880.0**, where 7,349.9 is printed on the Q3 2025 statement ([📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec133/5)) and independently confirmed as 2,036.0 + 2,638.1 + 2,675.8. The row says 10,229.9 — **3.55× the actual quarter.** EPS shows the same: the four rows Q1–Q3 read 0.43, 0.85, 1.04, and the "Q4" row reads 3.49; summing the quarters as served gives 5.81 against a true annual 3.49, an overstatement of 66%. An analyst building a trailing-four-quarter series from this table overstates both revenue and earnings in the quarter and in the year.

**A second instance, one fiscal year earlier.** The same shape at FY2024: the "Q4 2024" row carries revenues 8,011,800,000, operating_income 1,367,400,000, net_income_loss 495,800,000 and eps_basic 1.32 — all four the FY2024 annual figures ([📄 VRT 10-K p.62](https://agentii.ai/v/VRT/sec110/62)) — against a true Q4 2024 revenue of 8,011.8 − 5,665.4 = **2,346.4**, where 5,665.4 is the nine-month 2024 figure printed beside the nine-month 2025 one ([📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec133/5)). Again 3.41× the quarter.

**VRT is a NEW census entry.** The register's DA-26 row enumerates nineteen issuers — HWM, TDG, BA, GOOG, MSFT, NVDA, SATS, NOC, LMT, RTX, PL, KRMN, VOYG, GSAT, MRK, AMGN, BMY, WWD, HEI — and **VRT is not among them.** With this artifact the census reads **20 of 20**, and VRT matches the register's own secondary observation that "most exhibit it twice, in consecutive years": the mislabel is present at both FY2025 and FY2024, verified against the annual statement at both.

The register records that the mislabelled **label varies by issuer** — "HWM's annual figure appears as `Q4`/`Q1`; TDG's as `Q3`" — and the consequence drawn is that it "cannot be screened by position." **VRT's label is `Q4`, the same as BA's**, on two consecutive years. That stability is itself a datum: where HWM's and TDG's labels move around the table, VRT's attaches to the year-end row both times, which suggests the mechanism is a fiscal-period resolver that renames the annual row rather than a per-fact extraction fault. **Carry-forward: test whether the mislabelled period is stable within each issuer across years, not only which period it is** — VRT is the second issuer (with BA) for which Q4 is stable across two years, and the pair is what would distinguish a positional mechanism from a random one.

**One structural point VRT adds to the register's own account.** The register records that at non-calendar issuers the mislabel "lands on the year-end quarter" — PL (January), HEI (October), WWD (September) — and calls this "the subtlest form, because a year-end quarter is *legitimately* the largest." **VRT is the December-year-end case of the same landing**: for a calendar filer the year-end quarter *is* Q4, so the annual figure lands on the row it would sit on anyway, and the only tell is the 3.55× magnitude. That makes VRT a distinct sub-case — not a *wrong* period, but a *wrong duration in the right period*. The register's current framing (label varies, cannot be screened by position) is about the label moving; VRT shows the harder version, where **the label is where a reader would expect it and the value is four times too large** — so a positional screen ("ignore the Q4 row") would have discarded VRT's most informative row, and a magnitude screen is the only one that fires. **The register's screening consequence should be widened from "cannot be screened by position" to "cannot be screened by position, and at December-year-end issuers position is actively misleading."**

**Note the contrast with §2.8.** The metrics *table*'s Q4 rows carry correct numbers under a wrong period label; the highlights *block*'s balance-sheet items carry correct numbers under wrong dates (§2.8). Both are period-attribution faults, both in the same product surface, neither flagged. They are the same defect class as DA-26 arriving through two other doors.

## 7. DA-27 — not testable, because the coincidence holds

`get_company_fiscal_calendar(VRT)` returns `fiscal_year_end_month: 12`, `fiscal_year_end_month_source: **gold_companies**`, `cross_validation_hint: null`. The source is not `default` (as it is at SPCX), so the month is not a hard-coded fallback — but for a December-year-end filer, a registry-read month and a calendar default produce identical labels, so the distinction cannot be tested from the output. VRT's own interim period is stated on the face of the filing as the three and six months ended 30 June 2026 with report date 2026-06-30, and every fiscal label in the corpus matches the calendar quarter it names.

**Disposition: NOT TESTABLE at VRT — and the register's own statement of the mechanism is what makes it untestable, which is the finding.** DA-27's registered mechanism is: "The platform buckets a period by **calendar quarter measured from 1 January**, then labels the bucket with the issuer's *fiscal* year. That is **exact for December-year-end issuers and off by one for every other fiscal year-end**." The register's census is **n = 4 of 4** — PL (January), AVAV (April), WWD (September), HEI (October) — and it closes with "**Every December-year-end issuer in the universe shows no offset.**"

**VRT is a December-year-end issuer.** So the mechanism predicts, correctly and by its own terms, that VRT shows no offset — and a prediction that is satisfied identically whether the platform synthesises the label or reads it from the filing **cannot be tested on this issuer at all.** The offset is not absent; it is *unobservable*, because the two candidate methods agree. That is a stronger form of untestability than "no failure observed," and it is not a clearance: **the artifact records that DA-27 was not run, and cannot be.**

**The register's own census makes the coverage limit structural, and this is the larger half of the problem.** DA-27's *testable* population is the four non-calendar filers above — a small minority of the universe. Every December-year-end issuer — VRT, and the majority — sits in the *untestable* population, and per the register's mechanism there is no offset to find there. So the n = 4 of 4 census is **not a sample of the universe; it is the entire testable population**, and the register's success rate is 4 of 4 measured on 4 of 4 available cases. **DA-27's census denominator should be restated to name the untestable majority explicitly**, or a reader will take "n = 4 of 4" as evidence about the universe when it is evidence about a partition of it. There is also a live consequence for the artifact contract: the rule that an artifact must not treat absence as a passed check applies here — VRT's DA-27 status is **not tested**, and it must not be tallied as clean.

**The method finding survives and is confirmed at VRT.** The calendar synthesises **FY2027 quarters, including 2027-10-01 → 2027-12-31**, for a company whose latest filing is dated 2026-07-29. Future periods are generated regardless of whether any filing exists to support them. Any consumer joining on a fiscal label without filtering to filed periods will match rows that no filing backs.

## 8. DA-28 — refuted for every quoted period; the historical discontinuity carried

**Preferred stock: authorised, none issued.** "Preferred stock, $0.0001 par value, 5,000,000 shares authorized, none issued and outstanding" — $— in both columns ([📄 VRT 10-Q p.7](https://agentii.ai/v/VRT/sec136/7)). **Common stock: a single class** — 700,000,000 shares authorised, 384,936,985 and 382,553,680 outstanding. **No convertible, no warrant line** at either 30 June 2026 or 31 December 2025. The BA-analogue test the brief specified — a preferred-stock or convertible discontinuity — returns nothing. The balance sheet itself foots exactly at both dates (11,143.3 + 4,757.6 = 15,900.9; 8,271.1 + 3,941.3 = 12,212.4).

**DA-28 as written — an IPO capital-structure discontinuity — is not applicable, and the pre-listing exposure is real but unexamined.** VRT's 10-Q series under CIK 0001674101 runs back to 2018, pre-dating the February 2020 SPAC listing, so filings exist on the other side of the discontinuity. They were identified and **not read** (scope). The 2019 operating-income fact ($206.1M) does sit in the XBRL corpus, so the pre-listing era is partly represented in the fact layer even though the transition itself was not examined.

**The discontinuity VRT does have is a vanishing warrant liability, and it is material to comparability.** `Change in fair value of warrant liabilities` runs **$157.9M (FY2023) → $449.2M (FY2024) → nil (FY2025)** ([📄 VRT 10-K p.62](https://agentii.ai/v/VRT/sec110/62)), and the Q3 2025 statement shows it at nil for both the quarter and the nine months against $67.2M and $269.2M in 2024 ([📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec133/5)). The instrument existed, then did not. Two consequences: **the FY2024 → FY2025 net income comparison is not like-for-like** — FY2024's $495.8M is struck after a $449.2M non-cash warrant charge that FY2025 does not bear, so the MD&A's "+168.8%" net income growth is substantially a non-recurring-effect artefact, and §1c requires both bases to be stated; and **a universe-wide capital-structure screen keyed on preferred or convertible instruments would have missed VRT's discontinuity entirely**, because it was a warrant. **Carry-forward: DA-28's instrument list should include warrants and earnout/redemption features, not only preferred and convertible.**

**Disposition: DA-28 REFUTED for all quoted periods; the warrant discontinuity carried as an open exposure for the pre-2025 record and as a comparability qualification on FY2024→FY2025.** Note also that VRT is outside DA-28's *scope* as registered — the entry binds issuers whose first reported quarter straddles a listing, and VRT listed in early 2020, five years before the periods quoted here. The register's consequence for detector design ("the DA-23 detector requires a listing-date guard") does not bind VRT, and the pre-listing 10-Qs are relevant only if a later artifact reaches back past FY2019.

## 9. The within-filing two-basis revenue split — **DA-30, second instance**

This is the register gap Phase 2 flagged (its §7: "New register gap for PIL-3 — no DA covers two-basis revenue disaggregation"). **Reached independently in this census and then matched to the register, the finding is not a new defect class: it is DA-30 — "two bases on one concept, collapsed without a basis field" — and VRT is its second instance, from a different mechanism.** Phase 2 identified the phenomenon and correctly declined to write a definition; the register supplied the definition at 1.5.0; the evidence below is what VRT contributes to it.

**DA-30's requirement, discharged first: the basis, named, with where it was established.** Any artifact quoting a multi-basis concept must name the basis and state where it was established. VRT's two bases for the same product/services split are:

| Basis | Where established | Q2 2026 products / services |
|---|---|---|
| **Income-statement basis** | On the face of the condensed consolidated statements of earnings ([📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec136/5)) | **2,646.7 / 627.6** |
| **Disaggregation basis** | Note 4, "Revenue disaggregation" ([📄 VRT 10-Q p.13](https://agentii.ai/v/VRT/sec136/13)) | **2,606.4 / 667.9** |

Both are VRT's own; both are filed in the same document on the same date; neither is labelled as a competing basis; **and no footnote anywhere in the filing reconciles them.** Every revenue figure quoted in this artifact is tagged to one of these two bases, and where the two differ the difference is stated rather than averaged — §1c requires both and this section is where both are shown.

**How VRT's instance differs from BWXT's.** BWXT's DA-30 instance is a **platform collapse across filings**: the issuer files operating income equity-inclusive and equity-exclusive, and the platform serves both under one concept with no basis field, so the artifact cannot comply by diligence alone — it must first discover a second basis exists. VRT's is a **within-filing split, served under two different labels, with no basis field and no reconciling footnote**, and it adds the property that makes DA-30's class sharper: **the two bases are arithmetically indistinguishable at the total.** BWXT's two bases differ in the level of the number the artifact quotes (equity is 20.2% of it), so an artifact that quotes the wrong basis quotes a wrong number. **VRT's two bases differ only in the *split*, and both sum to the same revenue** — so an artifact that quotes the wrong basis quotes a number that is *right at the level anyone checks* and wrong at the level it is used. That is a second, distinct route into DA-30, and it is the reason the entry's detector requirement is line-level rather than total-level.

**The inconsistency, at source, in all seven periods tested:**

| Period | Income statement — products / services | Note disaggregation — products / services & spares | Compensating shift | % of revenue |
|---|---|---|---|---|
| FY2023 | 5,406.1 / 1,457.1 | 5,271.2 / 1,592.0 | **134.9** | 1.97% |
| FY2024 | 6,393.5 / 1,618.3 | 6,245.2 / 1,766.6 | **148.3** | 1.85% |
| FY2025 | 8,390.6 / 1,839.3 | 8,207.0 / 2,022.9 | **183.6** | 1.79% |
| Q1 2025 | 1,649.7 / 386.3 | 1,611.1 / 424.9 | **38.6** | 1.90% |
| Q2 2025 | 2,166.0 / 472.1 | 2,118.9 / 519.2 | **47.1** | 1.79% |
| Q2 2026 | 2,646.7 / 627.6 | 2,606.4 / 667.9 | **40.3** | 1.23% |
| H1 2026 | 4,782.5 / 1,141.3 | 4,697.6 / 1,226.2 | **84.9** | 1.43% |

Sources: income statement ([📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec136/5), [📄 VRT 10-K p.62](https://agentii.ai/v/VRT/sec110/62), [📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec134/5), [📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec133/5)); disaggregation ([📄 VRT 10-Q p.13](https://agentii.ai/v/VRT/sec136/13), [📄 VRT 10-K p.76](https://agentii.ai/v/VRT/sec110/76), [📄 VRT 10-Q p.13](https://agentii.ai/v/VRT/sec134/13)).

Five properties, each independently disqualifying for the existing register:

1. **Universal.** Seven of seven periods, spanning two fiscal years, three quarters, two six-month columns and three annual columns, in two form types. Not an error; a property of the reporting.
2. **Compensating — and therefore invisible to the instrument.** The products shift and the services shift are equal and opposite to the tenth of a million in every period, so **both bases total the same revenue** (3,274.3, 10,229.9, 8,011.8, 6,863.2). Every calculation arc closes. Every total ties. `validate_calculation` returned no row on either revenue concept in any of the three accessions — not because it is silent by coverage gap, as at `OperatingIncomeLoss`, but because **there is nothing for a calculation check to find: a compensating reclassification is arithmetically invisible by construction.**
3. **Systematic in sign.** Products is **always** higher on the income statement; services & spares **always** higher in the note. Something consistently classified as a service in the disaggregation is classified as a product on the face of the earnings statement, every period, forever, with no disclosure of the rule.
4. **Stable in magnitude** — 1.2% to 2.0% of revenue — which is what distinguishes a definitional difference from a misstatement, and is precisely why it has survived: it is too small to trip a materiality screen and too systematic to be a typo.
5. **It breaks the causal chain the filing uses.** The MD&A's own offering-level growth figures are the **note** basis, not the income-statement basis: at Q2 2026 the filing says "Product sales increased $487.5 ... Services & Spares sales increased $148.7," which are 2,606.4 − 2,118.9 and 667.9 − 519.2 exactly — the note basis — whereas the income statement's own lines give 480.7 and 155.5. The same holds annually: FY2025's "Product sales increased $1,961.8 ... Services & spares sales increased $256.3" are 8,207.0 − 6,245.2 and 2,022.9 − 1,766.6 exactly, against income-statement-basis movements of 1,997.1 and 221.0 ([📄 VRT 10-K p.41](https://agentii.ai/v/VRT/sec110/41)). **The narrative is computed off one basis while the table directly above it in the same section presents the other**, and the margin attribution in §10 is expressed in the narrative's basis.

**Why none of DA-23…DA-28 covers it.** DA-23 tests sign; this has no sign problem. DA-24 tests a gain in the operating line; this is revenue, above it, and no gain. DA-25 tests a metric not reproducible from the segment tables; this *is* reproducible, from the wrong table. DA-26 tests a mislabelled period; both periods are labelled correctly. DA-27 tests a synthesised fiscal label; nothing is mislabelled. DA-28 tests a capital-structure discontinuity; this is revenue. §1c `no_single_basis_collapse` is the nearest relative, and the register's own DA-30 entry states the relation precisely: that rule "governs an **artifact** that quotes one competing basis and not the others" while DA-30 is "**the platform collapsing two bases before any artifact sees them**." §1c made this artifact show both bases (§9's table); it cannot make the platform detect the divergence.

**The detector requirement, stated for the register.** DA-30's entry establishes the requirement — *name the basis, and state where it was established* — and records that "**No artifact in thesis 002 names it** — recorded as a live §1c gap." This artifact names it, and VRT's case supplies the argument for what a DA-30 detector must look like, because the entry's current instance (a level difference: equity at 20.2% of the quoted figure) is detectable by comparing levels while VRT's is not:

> **A DA-30 detector must compare LINE-LEVEL, not total-to-total.** For every disaggregation axis a filing presents (product/service, geography, timing, segment), recompute each line from every surface that presents it and compare line by line. **A detector keyed on totals cannot fire on a compensating difference by construction** — and the compensating case is the one an artifact is most likely to quote without noticing, because the total it cross-checks against agrees.
>
> **Trigger:** any line-level difference exceeding rounding, **with no footnote reconciling the two bases.**
>
> **Negative control, from §1 of this artifact:** the segment/consolidated cost-of-sales difference of $15.0M is **not** a DA-30 instance. It is footnoted ("exclusive of engineering, research and development costs") and both taxonomies sum to the same total cost of 2,636.4. **The rule must require the absence of an explanatory footnote, or it will fire on every legitimate taxonomy difference in the universe.**

**Why this is the most valuable finding in the census.** The thesis's governing danger is that silence is indistinguishable from a clean pass. At `OperatingIncomeLoss` VRT shows the silence (§2.1). At the two-basis split VRT shows a second and worse form of the same danger: **a defect the instrument cannot see even in principle, because it is arithmetically compensating.** A reviewer who runs every calculation check in the register, on every period, and finds every total tying, has performed a complete check that is structurally incapable of finding this — and the numbers he validated are the same numbers the filing's own margin explanation is built on (§10).

**Where this sits against DA-29.** The two-basis split also survives for a DA-29 reason: the check that would catch it *closes*. Every total agrees, so any reconciliation built on totals is a check that tests nothing about the split — not a back-solve, but the same failure mode from the other side, and the register's remedy (run the test on the terms, not the closure) applies unchanged: **the terms are the line items, and the closure is the total, so a total-based check is precisely the check DA-29 says not to trust.**

## 10. The margin attribution fails arithmetic on both bases

The filing's causal claim, verbatim: "**Margin expansion in the second quarter of 2026 was primarily driven by the mix of product and service sales**" ([📄 VRT 10-Q p.28](https://agentii.ai/v/VRT/sec136/28)). Two documents, two causal stories, same date: the MD&A attributes the expansion to mix, and the note-based arithmetic does not support it at the magnitude claimed.

Gross margin moved from 34.0% (33.99%; 896.6 ÷ 2,638.1) to 37.7% (37.71%; 1,234.9 ÷ 3,274.3) — **+372 basis points**. §1c requires both bases, so both are computed:

| Basis | Services weight, Q2 2025 | Services weight, Q2 2026 | Δ weight | Gross-margin differential required to produce 372 bps | Share of the move explained at a plausible 10-pt differential |
|---|---|---|---|---|---|
| **Note 4** (the basis the MD&A's own growth figures use) | 519.2 / 2,638.1 = **19.68%** | 667.9 / 3,274.3 = **20.40%** | **+0.72 pts** | **517 pts** | ~7 bps ≈ **2%** |
| **Income statement** | 472.1 / 2,638.1 = **17.89%** | 627.6 / 3,274.3 = **19.17%** | **+1.28 pts** | **291 pts** | ~13 bps ≈ **3%** |

On the note basis, mix must carry a **517-point** gross-margin differential to produce the move; on the income-statement basis, **291 points**. A services-versus-products gross-margin differential of 291 points is not credible when the company's *total* gross margin is 37.7% — it would require the services business to run at a gross margin so far below products as to be loss-making on a fully-loaded basis, and services revenue is 19% of the total while contributing a declining share of gross profit. **Phase 2's ~520-point figure is confirmed on its basis and, as §1c requires, the other basis is now stated: it demands 291 points, which is also not credible.** The conclusion is robust to the basis choice: **mix explains on the order of 2–3% of the 372-basis-point expansion; roughly 365 basis points is undisclosed rate, volume, or cost movement.**

The filing does disclose other, larger movements that it does not name in the causal sentence: acquisition-related sales of **$129.7M** and a positive foreign-currency impact of **$35.9M** on the top line ([📄 VRT 10-Q p.28](https://agentii.ai/v/VRT/sec136/28)) — acquisitions carry acquired cost structures and acquired margins, which is a rate story, not a mix story. The attribution names mix; the disclosure names acquisitions and FX. This is a **CLAIMED** item in P4 terms — the filing asserts a cause this census does not verify, and cannot verify from the filing, which is why it is recorded as an unexplained residual rather than as a defect of the numbers. The numbers tie; the explanation does not.

## 11. Instrument observations outside the six DAs

1. **The coverage gap is total for the concept VRT was chosen to test** (§2.1): seven arcs, no row, three accessions.
2. **Both columns of the `computed`/`reported` pair are independently unreliable in one run** (§2.2–2.3): `computed` right and `reported` stripped for the cash-flow subtotals; `reported` right and `computed` collapsed for PP&E, current assets and liabilities, working capital, operating cash flow and net income. The pair is not a controlled comparison.
3. **`pass` can be `0 = 0`** (§2.4), and can also be genuine — so it carries no weight in either direction.
4. **Status is decided by magnitude, not by defect class** (§2.5): the same strip is `fail` at 1,561.4M and `warn` at 6.0M.
5. **The false-positive rate on `fail` is 94.9% at VRT** (§2.6), independently reproducing the register's 93%. The one true positive is not distinguishable from the false ones on any surface feature.
6. **A segment-dimensioned fact is served as a consolidated one** (§2.7): Americas R&D 86.4 as the company's R&D, flagged only in `dimensions`.
7. **One accession, two balance-sheet surfaces, one correct and one serving two prior year-ends** (§2.8).
8. **A `computed`-side sign inversion is a distinct defect from the `reported`-side strip** (§3): `NetIncomeLoss` computed as −139.1M and −125.4M against reported +488.7M and +1,332.8M. Registering only the `reported` channel would miss it.
9. **The `recent-quarter` skill pin resolved mid-phase — recorded rather than silently absorbed.** At first write this artifact carried `skill_pin: UNRESOLVED` with the reason that `recent-quarter` is absent from the six-hash table in 001's `reproduce.md` and that the Q57 ledger it should append to (`skill_pins.jsonl`) does not exist in the repo. That gap was closed on 2026-09-18: the pin is now `07d26b9c738b`, re-derived from **two independent plugin roots** (`agentii-equity-agent/skills/agentii/recent-quarter` and `equity-research-core/skills/agentii/recent-quarter`) which **agree**, using the `dispatch.skill_version_hash()` algorithm validated 9/9 against the six pins tabled in `reproduce.md`. **The method point survives the resolution and is the reason this item is kept:** an unresolved pin recorded with its reason is recoverable, and this one was recovered without touching the artifact's findings — whereas a fabricated or borrowed hash (BA §8.10's cross-artifact inconsistency) would have been indistinguishable from a correct one at every later stage. The ledger gap that made the UNRESOLVED state necessary is still open; the pin is now sourced, but nothing in the repo yet *appends* a pin automatically, so the next skill to be pinned will hit the same wall.
10. **The outline layer can misattribute the document.** `read_source_outline` on the Q2 2026 accession described page 1 as belonging to "Veralto Corporation's Q2 2026 Form 10-Q" while the accession number, the page-2 description and every page read are Vertiv's. An LLM-label contamination in the outline layer, not the data layer — but it is a wrong-company label on a first page, and it would be invisible to anyone who did not read the page.

## 12. Register version, and the DA-29 discharge

**The pin.** This artifact was written at `constitution_pin: 1.4.0`. The register moved to **1.5.0** in the same minute (contract mtime 16:21, artifact mtime 16:21), adding DA-29 and DA-30 and correcting DA-23 twice. It is kept at 1.4.0 because it matches `thesis.md` (rule `pins_match_thesis`), because the 1.5.0 changelog records that the 23 artifacts written at 1.4.0 "all remain valid at their recorded pin; none is silently re-run (Q56)" and this artifact is one of the 23, and because `check_citations.py` does not gate on the value. The changelog *defers* the DA-29/DA-30 obligations on those artifacts to Phase 7's validation ledger. **Both are discharged here instead**, because both turned out to bear directly on what this census found: the central finding is a DA-30 instance (§9), and the §2 instrument findings are DA-29 instances.

**DA-29 discharge — the mechanical circularity test, run on this artifact.** *If any term in a reconciliation appears nowhere in the source, the check is a back-solve; the test must be run on the terms, not the closure.* Applied to all thirteen component identities in §1: **every term is a filed line item on a cited statement page** — no term is derived to fit, nothing is carried from one period to make another close, and no reconciliation here is a back-solve. Stated affirmatively for the record: **no `computed` value from the instrument is cited as a derivation anywhere in this artifact.** The `computed` column appears only as evidence *about instrument behaviour* in §2, never as a source for a figure that appears in §1 or §10, because — per the register's DA-29 Instance 2 — the instrument never discloses which role produced each `computed` row, so a `computed` value cannot be reproduced from the material the instrument itself returns.

**VRT supplies two fresh instances of DA-29's registered classes, and a third thing that is not a defect.**

| DA-29 class | VRT's instance |
|---|---|
| **Instance 2 — `computed` not reproducible from the instrument's own tree** | `NetIncomeLoss` computed as **−125.4M** (FY2025 10-K) and **−139.1M** (H1 2025 comparative) against filed positives of **1,332.8** and **488.7** ([📄 VRT 10-K p.62](https://agentii.ai/v/VRT/sec110/62), [📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec136/5)). `LiabilitiesAndStockholdersEquity` computed as **11,146.9M** against a filed **15,900.9** ([📄 VRT 10-Q p.7](https://agentii.ai/v/VRT/sec136/7)). In each case the instrument's own returned material contains the filed value, so the `computed` row is not derivable from what the instrument gives back. |
| **Instance 3 — `reported` is not definitionally the filed value** | The cash-flow sign strip (§2.2): three `reported` values that are the absolute value of the filed negative, with `computed` correct beside them. Also `PropertyPlantAndEquipmentNet` computed as −391.9M against reported 625.1M at the 10-K. |
| **Not a defect — the `pass` that is `0 = 0`** | `EffectiveIncomeTaxRateContinuingOperations` with computed 0 and reported 0, status `pass` (§2.4). This is the class's *precondition* rather than a back-solve — but it is the reason the entry's warning is worth keeping: "**a passing check is the artifact most likely to be accepted without examination.**" A row asserting agreement between two absences is that warning in its purest form. |

**What VRT adds to DA-29's remedy.** The register's remedy is procedural — "name the source of every term" — and VRT's evidence is that the remedy is *necessary and, on its own, not sufficient for a reader of the instrument*: because `computed` is opaque and `reported` is not definitional, **the instrument's output cannot be the place a term's source is established.** The source has to be the filing. Every figure in §1 and §10 was taken from the statement face and reconciled there, which is the only procedure that satisfies the entry.

## Carry-forwards

1. **Register DA-30, second instance — VRT, and the line-level detector requirement (§9).** The direct answer to the brief's question: **yes, the $40.3M needs its own DA — and it turns out to have one already.** VRT should be recorded as the second instance, with the mechanism named as a within-filing split rather than a cross-filing collapse, and with the compensating property recorded as a distinct route into the class.
2. **Register DA-23 — annotate VRT's census row, and widen the consequence from component-level to statement-level (§3).** VRT is currently listed among "19 of 19 profitable issuers are unaffected," where the sign channel is inert by arithmetic; annotate it as *sign-inapplicable*, not *clean*. And VRT is the second instance of the BWXT row ("clean at every subtotal, stripped at a component") with the component on a **different statement** — so the census requirement is statement-level, not just component-level.
3. **Register DA-29 — the coverage-hole remedy needs a third cell (§2.1).** The registered hole is data-availability ("concept absent or segment-only" → `UNRESOLVABLE-FROM-PLATFORM`). VRT's concept is present, fully filed, seven arcs deep, and the validator is silent. Disposition for that cell is not "unresolvable" but "**the artifact must run Detector 1 itself; the validator's silence is not a result.**" Without it, a validator that never ran and one that ran and passed are the same row in every tally.
4. **Restate DA-24 to cover both signs** — VRT's PurgeRite contingent consideration ($62.0M charge) is the same structural hazard with the opposite sign from a disposal gain; combine with BA's §10.3 magnitude clause.
5. **Extend DA-28's instrument list to warrants and earnouts** — VRT's discontinuity was a warrant liability ($157.9M → $449.2M → nil), invisible to a preferred-or-convertible screen.
6. **Restate DA-27's denominator** — the register's n = 4 of 4 is not a sample, it is the entire testable population; every December-year-end issuer is untestable by the register's own mechanism statement, and that majority must be named (§7).
7. **DA-26 — add VRT (20 of 20), and widen the screening consequence.** The register's rule is "cannot be screened by position"; VRT is the December-year-end sub-case where **position is actively misleading** — the annual lands on the Q4 row, which is where it belongs for a calendar filer, so only a magnitude screen fires (§6).
8. **Test whether DA-26's mislabelled period is stable within an issuer across years** — VRT is Q4 in both FY2024 and FY2025, matching BA; the pair is what would distinguish a positional mechanism from a random fault.
9. **Record the per-fact rule on the sign axis** — the strip varies within one concept across adjacent periods (sign-driven), as HAWK showed it varying within one column. No period-level rule explains either.
10. **Instrument coverage manifest** (BA §10.1) — VRT adds three more accessions and a seventh-arc case to the silence column: 5 accessions, 2 issuers, 0 rows.
11. **Severity grading is magnitude-driven** (§2.5) — any register entry keyed on `fail` will miss defects graded `warn` for being small; and VRT's one true `fail` is indistinguishable from its 37 false ones.
12. **Pre-listing VRT filings (2018–2019) unread** — the SPAC-listing capital-structure transition is the DA-28 exposure that remains open at this issuer, though it is outside DA-28's scope for the periods quoted here.
13. **VRT Q2 2026 earnings call unread** — if an orders or book-to-bill metric is disclosed verbally, DA-25 acquires an object at VRT through the transcript and the "no object" verdict must be revisited; the filing itself discloses none.

## Could not be verified

- **Whether the $40.3M-class reclassification rule is disclosed anywhere.** Nothing in the two 10-Qs or the 10-K read here explains which revenue the income statement calls a product and the note calls a service. The published filings do not say. If the rule is disclosed it is in a document not read here (a registration statement, a comment-letter response, or an earnings-call explanation).
- **VRT's Q2 2026 earnings call transcript** — not read; DA-25's verdict is scoped to the filing set.
- **The pre-2020 capital structure** — the 2018–2019 10-Qs exist under CIK 0001674101 and were not read; the SPAC-listing transition is therefore identified but not examined.
- **Whether the sign strip originates in extraction or in a downstream transform.** The stored value is wrong and the validator's `reported` echoes it, so the corruption is upstream of validation — but the pipeline stage that applies `|x|` was not inspected, because that artifact is not in the source set.
- **Whether any `OperatingIncomeLoss` fact has ever been negative for a peer issuer** — VRT's 61 facts are all positive, so the operating-line strip is unexercised here; the population in which it *is* exercised cannot be estimated from this issuer.
- **The `recent-quarter` skill's reproducibility across roots — resolved for this skill, not for the others.** The pin is now `07d26b9c738b`, agreeing across two independent plugin roots (§11.9). What could not be verified is that the same two-root agreement holds for the other skills in the six-hash table, and the Q57 ledger that should record the next pin still does not exist — nothing in the repo appends one automatically.
