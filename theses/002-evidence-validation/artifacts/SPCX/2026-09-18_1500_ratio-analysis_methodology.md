---
thesis_id: "002-evidence-validation"
pillar: PIL-5
ticker: SPCX
skill: ratio-analysis
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "2d27c7f751fa"  # Q57 resolved 2026-09-18: COMPUTED, not guessed. dispatch.skill_version_hash() (scripts/dispatch.py:132) validated FIRST by re-deriving six of six published pins — operational-kpi 0730fd170124, unit-economics e87ee63269a2, secular-trends e6b41dbb2426, supply-chain 8cb3ac1de486, competitive 826995c722a4, risk 953fc5d396e7 — all six MATCH in every non-decoy root: plugins/vertical-plugins/*, plugins/agentii-plugin/*, plugins/agent-plugins/*, the packaged skills dir .claude/skills/agentii, and the second checkout A/agenzym/agentii-investment-intelligence/plugins/*. The base directory is therefore correct. ratio-analysis is 2d27c7f751fa in ALL of those roots (5 keeper locations, 3 distinct roots) and differs in EVERY decoy copy: packaging/targets/claude-code 3f69103fbf71, packaging/targets/generic-cli 3f69103fbf71, packaging/targets/codex 271f4893b4d9, packaging/targets/cowork 42c1dd5f52f1, models-and-pitches 9b1d7a504789, cache.bak/2.2.1 296490e6f094. The four packaging/targets decoys DO exist — under the second checkout, not under the .claude/plugins copy; §11 records the correction to my own first pass.
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "sign strip applied downstream of the filing, not by it — CONFIRMED and ATTRIBUTED: 4 of 4 consolidated operating lines served with the loss sign inverted; the detector gap equals 2 x the filed magnitude in all four periods; the segment table's own mixed-sign arithmetic foots exactly, which localises the defect to the platform"
  - da_id: "DA-24"
    chosen_reading: "non-operating item inside the operating line — NOT EVIDENT: the component census of 'total costs and expenses' (five named operating components, four periods) closes to the dollar with zero residual at every period, so no third-party amount is embedded; the two non-operating items found (debt-extinguishment loss 1,545; digital-asset unrealized loss 539) sit in the cash-flow reconciliation, not in the operating line"
  - da_id: "DA-25"
    chosen_reading: "issuer-normalised per-unit metric with an undisclosed denominator — NOT TESTABLE BY THIS SKILL: no slot in the ratio block is a per-unit metric; the live SPCX instance (Starlink ARPU) is owned by the recent-quarter artifact and is not re-derived here"
  - da_id: "DA-26"
    chosen_reading: "duration collision — CONFIRMED at SPCX in the collision mechanism (six-month values served under the same key that carries three-month values; validator rows show 4,146 and 541 on one key for the same per-share concept pair), while the specific annual-misread-as-quarterly instance is UNEXERCISED (no annual period exists in this corpus)"
  - da_id: "DA-27"
    chosen_reading: "fiscal label synthesised from the calendar quarter — UNEXERCISED at SPCX (Dec-31 filer): the channel exists in the label space and cannot shift any SPCX period label, so it is recorded inert, not clean"
  - da_id: "DA-28"
    chosen_reading: "capital-structure discontinuity — CONFIRMED and mechanised: preferred converted at IPO (38,752 to nil), APIC 37,706 to 167,344 on 85,675 of IPO proceeds, shareholders' equity 2,573 to 127,224, 5-for-1 stock split; every balance-sheet denominator in the ratio block is a post-IPO instant while the numerators are six-month durations spanning the boundary"
  - da_id: "DA-29"
    chosen_reading: "defective checks / back-solved derivations — CENTRAL. CONFIRMED: validate_calculation returns pass on a 541 magnitude that is a 541 LOSS, and pass on a cost total bound to the wrong duration; the platform's own `computed` column is unreproducible from the filing in 3 of the rows I tested and is itself a mixed-instant back-solve in a 4th. Corollaries applied: `computed` is cited here only as evidence of platform behaviour, never as a derivation; `reported` is reconciled to the statement face in every row I use"
  - da_id: "DA-30"
    chosen_reading: "two bases on one concept collapsed with no basis field — CENTRAL and CONFIRMED at LINE level: 6 concepts in the ratio block carry 14 distinct filed bases and the served values select bases they never name (cash 93,522 vs 94,352; debt 21,968 / 36,839 / 39,364 / 38,433 plus a fifth served 21,659; equity 127,224 vs APIC 167,344; operating income consolidated vs segment vs year-ago segment; net income 541 vs 4,817 vs 5,488; EBITDA filed Adjusted 3,538 / 4,665 vs an implied 3,831 or 6,379 that is not filed)"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: "Balance sheet cells, June 30, 2026 / December 31, 2025: cash and cash equivalents 93,522 / 24,747; marketable securities 6,487 / 0; accounts receivable 3,596 / 1,579; inventory 2,718 / 2,416; prepaid and other current assets 1,724 / 2,210; Total current assets 108,047 / 30,952; Total assets 192,770 / 92,079; accounts payable 8,243 / 11,792; deferred revenue current 7,977 / 6,111; debt and finance leases current 2,525 / 928; accrued expenses 2,377 / 2,569; Total current liabilities 21,122 / 21,400; debt and finance leases non-current 36,839 / 21,968; Total liabilities 65,546 / 50,754; additional paid-in capital 167,344 / 37,706; accumulated deficit (41,852) / (37,035); Total shareholders' equity 127,224 / 2,573"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 4
    url: https://agentii.ai/v/SPCX/sec8/4
    located_via: read_source_pages
  - figure: "Statements of operations cells: revenue 7,814 / 4,071 / 12,508 / 8,138; cost of revenue 3,495 / 2,282 / 5,883 / 4,244; research and development 3,548 / 1,958 / 7,062 / 3,515; selling, general and administrative 912 / 606 / 1,658 / 1,099; restructuring 2 / 190 / (9) / 194; impairment 0 / 5 / 0 / 29; Total costs and expenses 7,957 / 5,041 / 14,594 / 9,081; Loss from operations (143) / (970) / (2,086) / (943); interest expense (629) / (411) / (1,293) / (858); interest income 340 / 98 / 553 / 215; other income (expense), net (86) / 413 / (1,962) / 202; loss before income taxes (518) / (870) / (4,788) / (1,384); provision for income taxes 23 / 138 / 29 / 152; Net loss (541) / (1,008) / (4,817) / (1,536); basic and diluted loss per share (0.09) / (0.34) / (1.12) / (0.53); weighted-average shares 5,864 / 2,929 / 4,879 / 2,902"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 5
    url: https://agentii.ai/v/SPCX/sec8/5
    located_via: read_source_pages
  - figure: "Statements of cash flows cells: Net cash provided by operating activities 3,466 / 351; depreciation and amortization 5,290 / 2,970; share-based compensation 1,470 / 694; unrealized (gain) loss on digital assets 539 / (252); loss on debt extinguishment 1,545 / 0; purchases of property, plant and equipment (28,476) / (6,965); Net cash used in investing activities (34,487) / (6,032); Net cash provided by financing activities 100,291 / 9,199; effect of exchange rate changes on cash and cash equivalents (42) / 75; Net increase in cash, cash equivalents and restricted cash 69,228 / 3,593; cash, cash equivalents and restricted cash, beginning of period 25,124 / 11,501; end of period 94,352 / 15,094"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 9
    url: https://agentii.ai/v/SPCX/sec8/9
    located_via: read_source_pages
  - figure: "Cash and Cash Equivalents and Restricted Cash table: cash and cash equivalents $93,522 / $24,747; restricted cash in prepaid expenses and other current assets 210 / 182; restricted cash in other assets 620 / 195; Total as presented in the consolidated statements of cash flows $94,352 / $25,124"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 12
    url: https://agentii.ai/v/SPCX/sec8/12
    located_via: read_source_pages
  - figure: "Note 11 components: prepaid expenses and other current assets — tax related assets 561 / 618, unbilled receivables 192 / 223, rebates and credits 178 / 597, restricted cash and deposits 210 / 182, other current assets 583 / 590, total $1,724 / $2,210. Accrued expenses and other current liabilities — tax related liabilities 529 / 563, payroll and employee benefit accruals 452 / 322, operating lease liabilities current 344 / 422, restructuring liabilities 177 / 339, accrued interest 20 / 416, other current liabilities 855 / 507, total $2,377 / $2,569"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 22
    url: https://agentii.ai/v/SPCX/sec8/22
    located_via: read_source_pages
  - figure: "EPS reconciliation: Net loss (541) / (1,008) / (4,817) / (1,536); less deemed dividend 671 (six months 2026); Net loss attributable to common shareholders (541) / (1,008) / (5,488) / (1,536); weighted-average shares 5,864 / 2,929 / 4,879 / 2,902; basic and diluted EPS (0.09) / (0.34) / (1.12) / (0.53); anti-dilutive instruments: xAI redeemable convertible preferred 0 / 1,220; SpaceX redeemable convertible preferred 0 / 6,760; share-based compensation awards 564 / 669"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 26
    url: https://agentii.ai/v/SPCX/sec8/26
    located_via: read_source_pages
  - figure: "Note 18 segment table, three months 2026: revenue Space 962, Connectivity 4,291, AI 2,561, Total 7,814; total costs and expenses 1,504 / 2,635 / 3,818 / 7,957; Income (loss) from operations (542) / 1,656 / (1,257) / (143); interest expense (629); interest income 340; other expense (86); loss before income taxes (518); depreciation and amortization 158 / 805 / 1,885 / 2,848; share-based compensation 179 / 136 / 516 / 831; capital expenditures 1,174 / 1,367 / 15,828 / 18,369"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 30
    url: https://agentii.ai/v/SPCX/sec8/30
    located_via: read_source_pages
  - figure: "Segment tables, six months 2026 and three months 2025: six months 2026 revenue 1,581 / 7,548 / 3,379 / 12,508 and loss from operations (1,204) / 2,844 / (3,726) / (2,086); three months 2025 revenue 746 / 2,588 / 737 / 4,071 and loss from operations (369) / 923 / (1,524) / (970); six months 2026 depreciation 324 / 1,588 / 3,378 / 5,290; share-based compensation 324 / 252 / 894 / 1,470; capital expenditures 2,226 / 2,699 / 23,551 / 28,476; three months 2025 depreciation 146 / 569 / 811 / 1,526"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 31
    url: https://agentii.ai/v/SPCX/sec8/31
    located_via: read_source_pages
  - figure: "AI segment MD&A table: revenue 2,561 / 737 / 3,379 / 1,465; total costs and expenses 3,818 / 2,261 / 7,105 / 3,925; Loss from operations $(1,257) / $(1,524) / $(3,726) / $(2,460), with year-over-year change 267 and 1,266 (17.5% and 51.5%)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 44
    url: https://agentii.ai/v/SPCX/sec8/44
    located_via: read_source_pages
  - figure: "MD&A prose (not a table page): 'AI loss from operations for the three months ended June 30, 2026 decreased by $267 million, or 17.5%' and the six-month movement 'increased by $1,266 million, or 51.5%'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 45
    url: https://agentii.ai/v/SPCX/sec8/45
    located_via: read_source_pages
  - figure: "Non-GAAP reconciliation: Adjusted EBITDA 3,538 / 1,214 / 4,665 / 2,944; Segment Adjusted EBITDA Space (205), Connectivity 2,597, AI 1,146, Total 3,538; the stated definition names depreciation and amortization, share-based compensation, restructuring, impairments, interest expense, interest income, other income (expense) and taxes"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 46
    url: https://agentii.ai/v/SPCX/sec8/46
    located_via: read_source_pages
  - figure: "Debt footnote (prose plus table): 'outstanding $38,433 million in aggregate principal amount of indebtedness'; SpaceX Notes $25,000 aggregate principal, weighted-average coupon 5.855%, coupons 5.350%-6.650%, maturities 2031-2056; SpaceX Credit Facility $1,500 with no amount outstanding; Consolidated Leverage Ratio covenant 3.75:1.0"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 48
    url: https://agentii.ai/v/SPCX/sec8/48
    located_via: read_source_pages
key_metrics:
  operating_margin_basis_swing_pp: 46.47
  da30_instances: 7
  internal_launches_of_total: "27/37"
  filed_operating_margin_pct: -16.68
  served_operating_margin_pct: 29.79

---

# SPCX — ratio-analysis: every ratio cross-checked against its component identity

**Source instrument:** SPCX 10-Q for the quarterly period ended June 30, 2026, accession `0001628280-26-052535`, filed 2026-08-04, citation_id `sec8` (12 citations below; every page cell-quoted from a direct read, not from an outline description).

**Scope.** This artifact does one thing: it takes the platform's derived ratio block for SPCX and cross-checks *every* served value against the component identity of the ratio it claims to be. A residual is attributed to a named defect or declared unresolved. It does **not** re-ask 001's questions — 001 is frozen at 1.2.0 (`upstream_stale: "001@1.2.0"`) and one of its facts is corrected in §9, not rewritten.

**Result in one line.** 12 numeric ratio slots are served. **10 of 12 reproduce to the served precision from filed cells. Of those 10, only 3 survive their own component identity on a single consistent basis.** 2 slots cannot be reproduced from any filed pair and are declared UNATTRIBUTED. 1 slot is served null while both its components are filed. The two portable detectors fire in all four periods. Themselves at issue are not the ratios but the bases: DA-29 and DA-30 are both CONFIRMED and both are the reason this method exists.

## §1 The served set, and where each value comes from

| # | ratio | served | reproduction from filed cells | reproduction error | basis actually used |
|---|---|---|---|---|---|
| 1 | net_margin | 0.3851 | 4,817 / 12,508 = 0.385113 | 0.0% | six-month net loss / six-month revenue |
| 2 | roa | 0.0250 | 4,817 / 192,770 = 0.024988 | 0.0% | six-month net loss / period-end assets |
| 3 | asset_turnover | 0.0649 | 12,508 / 192,770 = 0.064886 | 0.0% | six-month revenue / period-end assets (unannualised) |
| 4 | current_ratio | 5.0489 | 108,047 / 21,400 = 5.048925 | 0.0% | **6/30 current assets / 12/31 current liabilities** |
| 5 | quick_ratio | 4.3702 | 93,522 / 21,400 = 4.370187 | 0.0% | **cash only** (no receivables, no marketable securities) |
| 6 | cash_ratio | 4.3702 | 93,522 / 21,400 = 4.370187 | 0.0% | identical to slot 5, to all four decimals |
| 7 | operating_cf_ratio | 0.1620 | 3,466 / 21,400 = 0.161963 | 0.0% | six-month operating cash flow / **12/31** current liabilities |
| 8 | roe | 0.0288 | 4,817 / 167,344 = 0.028785 | 0.0% | net loss / **additional paid-in capital** (not equity) |
| 9 | debt_to_equity | 0.3917 | 65,546 / 167,344 = 0.391684 | 0.004% | **total liabilities / additional paid-in capital** |
| 10 | operating_margin | 0.2979 | 3,726 / 12,508 = 0.297889 | 0.0% | **AI segment six-month operating loss / consolidated six-month revenue** |
| 11 | roic | 0.0181 | none | — | **UNATTRIBUTED** (§3.2) |
| 12 | debt_to_ebitda | 10.2751 | none | — | **UNATTRIBUTED** (§3.2) |
| 13 | gross_margin | `null` | 0.5527 (3M26), 0.5297 (6M26), 0.4395 (3M25), 0.4785 (6M25) | — | served null; both components filed (§2.5) |

Reproduced cells: revenue 7,814 / 4,071 / 12,508 / 8,138; cost of revenue 3,495 / 2,282 / 5,883 / 4,244; total costs and expenses 7,957 / 5,041 / 14,594 / 9,081; loss from operations (143) / (970) / (2,086) / (943); net loss (541) / (1,008) / (4,817) / (1,536); weighted-average shares 5,864 / 2,929 / 4,879 / 2,902 (https://agentii.ai/v/SPCX/sec8/5). Balance-sheet cells: total current assets 108,047 / 30,952; total assets 192,770 / 92,079; total current liabilities 21,122 / 21,400; total liabilities 65,546 / 50,754; additional paid-in capital 167,344 / 37,706; accumulated deficit (41,852) / (37,035); total shareholders' equity 127,224 / 2,573 (https://agentii.ai/v/SPCX/sec8/4).

Every one of the ten reproductions closes on a term that appears on the statement face. That is the *terms* test, not the closure test: a back-solve closes exactly too (§6).

## §2 Component identity, in-line, per period

The identity is stated with actual values in every period, in the order debt → cash → net income, so that a sign error anywhere in the chain shows up as a residual rather than as a plausible number.

### 2.1 The operating line (the DA-23 test, in-line)

Consolidated, four periods:

- 3M26: 7,814 − 7,957 = **(143)** — served **+143**
- 6M26: 12,508 − 14,594 = **(2,086)** — served **+2,086**
- 3M25: 4,071 − 5,041 = **(970)** — served **+970**
- 6M25: 8,138 − 9,081 = **(943)** — served **+943**

All four filed operating lines are negative (https://agentii.ai/v/SPCX/sec8/5). The platform's positive ratio-adjacent values and its validator row `OperatingIncomeLoss` (reported **+143**, computed **−4,578**) both carry the wrong sign, and the computed number is not the filing's either (the filing's own six-month subtraction is (2,086)) — a second, independent defect on the same row (§6).

### 2.2 The `total costs and expenses` census (the DA-24 test)

Five named operating components, four periods, closed in-line:

- 3M26: 3,495 + 3,548 + 912 + 2 + 0 = **7,957** (filed 7,957)
- 6M26: 5,883 + 7,062 + 1,658 + (9) + 0 = **14,594** (filed 14,594)
- 3M25: 2,282 + 1,958 + 606 + 190 + 5 = **5,041** (filed 5,041)
- 6M25: 4,244 + 3,515 + 1,099 + 194 + 29 = **9,081** (filed 9,081)

Zero residual at every period, and every component is an operating line by the issuer's own presentation. The two non-operating items in the filing — the 1,545 loss on debt extinguishment and the 539 unrealized loss on digital assets — appear in the cash-flow reconciliation only, never inside `total costs and expenses` (https://agentii.ai/v/SPCX/sec8/9). **DA-24 is NOT EVIDENT** here, on a test that could have fired: a contaminant folded into `total costs` would have appeared as a sixth component, and there is none.

Note the limit: the identity `revenue − total costs = operating income` **cannot** detect DA-24, because a contaminant inside the filed subtotal is absorbed by the subtotal. The test with power is the component census above, not the subtraction. I report the census as the test and the subtraction only as the articulation check.

### 2.3 Liquidity (the weakest block)

- `current_ratio` 5.0489 = 108,047 (6/30) / 21,400 (12/31). The two terms are one period apart. On one instant the value is 108,047 / 21,122 = **5.1154**; the served figure is 1.32% low. Cell evidence for both instants: total current assets 108,047 / 30,952 and total current liabilities 21,122 / 21,400 (https://agentii.ai/v/SPCX/sec8/4).
- `quick_ratio` = `cash_ratio` = 4.3702 exactly. Quick assets are conventionally cash + short-term investments + receivables = 93,522 + 6,487 + 3,596 = **103,605**, which gives 103,605 / 21,122 = **4.9050**. The served pair omits 6,487 of marketable securities and 3,596 of receivables and lands on the cash ratio. **Two slots, one value: the quick ratio is arithmetically inert — it carries no discriminant power at all.** Named as a defect, not as agreement.
- `operating_cf_ratio` 0.1620 uses six-month operating cash flow 3,466 over the **prior** period-end liability total 21,400 (https://agentii.ai/v/SPCX/sec8/9).

### 2.4 Leverage and return: the basis substitutions

- `debt_to_equity` 0.3917 = **65,546 / 167,344**. The numerator is *total liabilities* (includes 21,122 of non-debt current liabilities and 6,309 of non-current deferred revenue), the denominator is *additional paid-in capital*, not equity. Filed-consistent: debt and finance leases 2,525 + 36,839 = **39,364**; equity **127,224**; ratio **0.3094**. The served value is **26.6% high**. On the serving basis the arithmetic is exact to 4 dp, so the defect is not arithmetic — it is a component substitution, and it is invisible to any check that validates the division rather than the terms.
- `roe` 0.0288 = 4,817 / 167,344, i.e. **net loss over paid-in capital**. Against filed equity: 4,817 / 127,224 = **0.0379**, so the served value is **31.5% low**. APIC (167,344) exceeds total equity (127,224) because the accumulated deficit (41,852) is deducted; the platform has picked the gross contributed-capital line over the net residual claim. The components of the equity section: 167,344 + 1,719 + common stock par + (41,852) = 127,224, residual **13** — the par line (par value $0.001) is the single line I did not capture cell-wise; recorded as an incomplete capture, not as a gap in the filing (https://agentii.ai/v/SPCX/sec8/4).
- `roa` 0.0250 and `asset_turnover` 0.0649 both divide by period-end assets 192,770 rather than the average of 192,770 and 92,079 (**142,425**), which would give 0.0338 and 0.0878. Period-end is a defensible convention; **it is not labelled**, and on a balance sheet that moved 192,770 / 92,079 = 2.09x in six months the choice moves the value by 35%.

### 2.5 The segment-substituted ratio, and the null slot

- `operating_margin` 0.2979 = **3,726 / 12,508**: the AI segment's six-month operating **loss** over the *consolidated* six-month revenue. Segment cells: six months 2026 loss from operations (1,204) / 2,844 / **(3,726)** / (2,086) (https://agentii.ai/v/SPCX/sec8/31); AI MD&A table loss from operations (1,257) / (1,524) / (3,726) / (2,460) with revenue 3,379 for the six months (https://agentii.ai/v/SPCX/sec8/44). Against its own revenue the AI margin is (3,726) / 3,379 = **−110.3%**; against consolidated revenue the filed consolidated margin is (2,086) / 12,508 = **−16.68%**. The served **+29.79%** therefore inverts a −16.68% margin: a **46.47 percentage-point swing**. The segment substitution is established by cell, not by prose: the AI table's own identity closes exactly at all four periods (2,561 − 3,818 = (1,257); 737 − 2,261 = (1,524); 3,379 − 7,105 = (3,726); 1,465 − 3,925 = (2,460)).
- `gross_margin` is served `null` while **both components are filed** at four periods: (7,814 − 3,495) / 7,814 = **0.5527**; (12,508 − 5,883) / 12,508 = **0.5297**; (4,071 − 2,282) / 4,071 = **0.4395**; (8,138 − 4,244) / 8,138 = **0.4785** (https://agentii.ai/v/SPCX/sec8/5). The reason is a tag absence, not a data absence: `GrossProfit` returns zero facts for this filer from `search_xbrl_facts`, so the slot is left null. **A null slot is a platform-completeness gap, and I record it as `UNVALIDATED-BY-PLATFORM`, never as a pass and never as an absence of the underlying figure.** The four values above are my computation from read cells, not the platform's.
- The register row for DA-23 records "~65% GM" at SPCX. That figure reproduces on **exactly one basis I can find**: the Space segment, three months 2026 — (962 − 329) / 962 = **65.80%** (https://agentii.ai/v/SPCX/sec8/30). It does **not** reproduce on the consolidated basis in any period (43.95% – 55.27%), nor on Connectivity 3M26 (2,231 / 4,291 = 51.99%), nor on AI 3M26 (1,455 / 2,561 = 56.81%). The register row names no basis; the only reading on which it is true is segment-level. Recorded as a DA-30 basis collapse **inside the register row itself** — not asserted as an error in 001's text, which does not specify a basis.

## §3 Residual register

### 3.1 Attributed residuals (each traced to a named defect)

| residual | magnitude | attributed to |
|---|---|---|
| current_ratio 5.0489 vs 5.1154 | 1.32% low | denominator instant taken at 12/31 while the numerator is 6/30 — the same mis-binding appears in the validator row `LiabilitiesCurrent` (reported 21,400 under a 6/30 key) |
| roe 0.0288 vs 0.0379 | 31.5% low | denominator substituted: APIC 167,344 for equity 127,224 |
| debt_to_equity 0.3917 vs 0.3094 | 26.6% high | both terms substituted: total liabilities for debt, APIC for equity |
| operating_margin 0.2979 vs −0.1668 | 46.47 pp swing | segment substitution: AI segment loss over consolidated revenue |
| quick_ratio 4.3702 | equals cash_ratio exactly | quick-asset set computed as cash only (6,487 + 3,596 omitted) |
| roa 0.0250, asset_turnover 0.0649 | 35% vs the average-balance convention | closing rather than average balance; unlabelled convention |
| gross_margin `null` | both components filed | `GrossProfit` tag absent for this filer |
| equity section residual 13 | — | common stock par line not captured (`$0.001` par) |
| DA-23 sign inversion, 4 periods | gap = 2 x magnitude each period | sign stripped downstream of the filing (§4) |

### 3.2 Unattributed residuals — declared unresolved, not rounded away

- **`roic` = 0.0181.** Implied denominator for the six-month operating loss of 2,086: **114,931 – 115,568** (the band that rounds to 0.0181). Nearest construction on the platform's own APIC basis: 2,086 / (39,364 + 167,344 − 93,522) = 2,086 / 113,186 = **0.018430**, which is **1.82% above** the served value and falls outside the band. The filed-consistent construction — 2,086 / (39,364 + 127,224 − 93,522) = 2,086 / 73,066 = **0.028550** — is **57.7% away**. No filed cell, no filed subtotal, and no two-term combination of them lands in the implied band.
- **`debt_to_ebitda` = 10.2751.** Implied EBITDA, per candidate debt basis: 39,364 / 10.2751 = **3,831**; 65,546 / 10.2751 = **6,379**; 36,839 / 10.2751 = **3,585**; 21,659 / 10.2751 = **2,108**. None of these is filed or derivable: the filing's own Adjusted EBITDA is **3,538** (3M26) and **4,665** (6M26), reconciled exactly below (https://agentii.ai/v/SPCX/sec8/46). The nearest filed-metric pair is 36,839 / 3,538 = **10.4121**, **1.33% above** the served value; 38,433 / 3,538 = 10.8633. A brute-force sweep of 37.9M expression candidates built from the filing's own cells returned **zero** matches at a 5.5e-5 tolerance.

Both are declared **UNRESOLVED — UNATTRIBUTED**, with the intervals above. A residual I cannot attribute is a finding; the finding is that the platform can serve a ratio whose terms appear nowhere in the instrument, and whose closure therefore cannot be checked at all.

The Adjusted EBITDA reconciliation I *can* close, in-line, on one sign convention and only from cells I read:

- 3M26: OIL (143) + D&A 2,848 + SBC 831 + restructuring 2 = **3,538** (filed 3,538). D&A = 158 + 805 + 1,885; SBC = 179 + 136 + 516 (https://agentii.ai/v/SPCX/sec8/30); OIL and restructuring (https://agentii.ai/v/SPCX/sec8/5).
- 6M26: OIL (2,086) + D&A 5,290 + SBC 1,470 + restructuring (9) = **4,665** (filed 4,665) (https://agentii.ai/v/SPCX/sec8/46) (https://agentii.ai/v/SPCX/sec8/9).
- The 2025 columns require the three-month 2025 share-based compensation cell, which I did **not** read. Recorded **NOT READ** — not fitted, not approximated, not reported as a pass.

## §4 The two portable detectors, the weight discriminator, and their positive controls

**Articulation (gap = 2 x stripped term).** All four periods, exact:

| period | revenue − total costs | served | gap | 2 x magnitude |
|---|---|---|---|---|
| 3M26 | (143) | +143 | 286 | 2 x 143 = 286 |
| 6M26 | (2,086) | +2,086 | 4,172 | 2 x 2,086 = 4,172 |
| 3M25 | (970) | +970 | 1,940 | 2 x 970 = 1,940 |
| 6M25 | (943) | +943 | 1,886 | 2 x 943 = 1,886 |

**Overshoot (excess = 2 x |every negative component|).** The platform's own roll-forward for the change in cash, from the validator's returned row: computed **138,286** against reported **69,228**. Excess **69,058 = 2 x (34,487 + 42)** — the investing outflow 34,487 and the exchange-rate outflow 42, both filed parenthesised and both at arc weight **+1** in the platform's tree. Exact to the dollar. Same detector, prior year: computed 15,657 against reported 3,593, excess **12,064 = 2 x 6,032** — and the 2025 exchange effect was **+75**, positive, so the rule correctly excludes it. Cell evidence: net cash used in investing (34,487) / (6,032); exchange effect (42) / 75; net increase 69,228 / 3,593 (https://agentii.ai/v/SPCX/sec8/9).

**Weight discriminator, both arms exercised at SPCX.**
- Negative control: `PaymentsToAcquirePropertyPlantAndEquipment` sits at arc weight **−1**, so the served positive 28,476 is **LEGITIMATE** even though the filed cell is parenthesised (28,476). *A parenthesised filed cell is not sufficient evidence of a strip; the weight decides.*
- Positive control: `NetCashProvidedByUsedInInvestingActivities` and the exchange-rate line are at weight **+1** with parenthesised filed cells, and the overshoot detector confirms they were stripped.
- The filing's own signs are internally consistent: the segment table's mixed-sign arithmetic foots exactly (revenue 962 + 4,291 + 2,561 = 7,814; operations (542) + 1,656 + (1,257) = (143); https://agentii.ai/v/SPCX/sec8/30) and the six-month table foots too ((1,204) + 2,844 + (3,726) = (2,086); https://agentii.ai/v/SPCX/sec8/31). **The inversion is introduced downstream of the filing.** The Connectivity segment's +1,656 / +2,844 / +923 carries the profitable arm as the positive control on the same pages.

**Gross-profit bound: UNEXERCISED.** With computed gross margins of 43.95% – 55.27%, a bound that can only fire above 100% has no power at SPCX. I do not report it as a passed test. **A test that cannot fail is not a passing test.**

## §5 The six-DA census (DA-23 … DA-28)

| DA | verdict | test that ran, or the KINDS of test that could not |
|---|---|---|
| DA-23 sign strip | **CONFIRMED / ATTRIBUTED** | articulation detector, 4/4 periods exact; weight discriminator both arms; 4 of 4 consolidated operating lines inverted. Profitable arm UNEXERCISED at consolidated level (all four lines are losses) and exercised at segment level (Connectivity +1,656 / +2,844 / +923) |
| DA-24 non-operating contamination | **NOT EVIDENT** | `total costs and expenses` component census: 5 components, 4 periods, zero residual. The identity subtraction has no power here (a contaminant is absorbed by the filed subtotal) — named so the NOT EVIDENT verdict is not read as CLEAN by a weaker test |
| DA-25 per-unit metrics | **NOT TESTABLE BY THIS SKILL** | KINDS: (i) issuer-normalised per-unit metrics — none in the ratio block; (ii) the block's 13 slots are all X/Y with both terms platform-supplied. SPCX's live instance (Starlink ARPU, definition without a disclosed denominator) belongs to the recent-quarter artifact and is not re-derived here |
| DA-26 duration mislabel | **CONFIRMED (collision) / UNEXERCISED (annual instance)** | collision exercised: the six-month net loss 4,817 drives `net_margin`/`roa` while `net_income_loss` 541 is served elsewhere, both filed under one June-30-2026 column (https://agentii.ai/v/SPCX/sec8/5); validator rows serve 4,146 and 541 on one key for the same per-share concept pair, and pass a 5,041 total bound to the six-month date. Annual-as-quarterly: UNEXERCISED — no annual period exists in this corpus |
| DA-27 fiscal-label synthesis | **UNEXERCISED (inert)** | SPCX is a Dec-31 filer with a Dec-31 quarter; synthesised labels cannot shift any SPCX period. Recorded inert, **not clean** |
| DA-28 capital-structure discontinuity | **CONFIRMED, mechanism named** | preferred 38,752 to nil, APIC 37,706 to 167,344 on 85,675 of IPO proceeds, equity 2,573 to 127,224 (49.5x), 5-for-1 split (https://agentii.ai/v/SPCX/sec8/4) (https://agentii.ai/v/SPCX/sec8/9). Consequence for the ratio block: every balance-sheet denominator is a post-IPO instant while the numerators are six-month durations that straddle the boundary |

## §6 DA-29 — the checks (central)

**Finding 1 — a pass carries no sign information.** `NetIncomeLossAvailableToCommonStockholdersDiluted` returns **pass** with computed = reported = **541**, difference 0 — on a period whose filed net loss is **(541)** (https://agentii.ai/v/SPCX/sec8/5) (https://agentii.ai/v/SPCX/sec8/26). Same shape at 1,008. The check closes on a sign-stripped value and reports it as validated. This is the SATS shape reproduced on a second ticker.

**Finding 2 — a pass on a period-mismatched value.** `CostsAndExpenses` returns **pass** with computed = reported = **5,041**, which is the *three-month* 2025 total bound to the six-month 2025 date (the six-month total is 9,081).

**Finding 3 — the `computed` column is not reproducible in 3 of the rows I tested, and is itself a mixed-instant back-solve in a 4th.**
- `AssetsCurrent` computed **37,439** **is** reproducible — and only as 24,747 (12/31 cash) + **6,487 (6/30 marketable securities, substituted for a 12/31 zero)** + 1,579 (12/31) + 2,416 (12/31) + 2,210 (12/31). A fallback rule across instants that no reader could reconstruct from the instrument.
- `Assets` computed **78,871** matches neither the 6/30 children sum (**192,770**) nor the 12/31 children sum (**92,079**).
- `LiabilitiesCurrent` computed **18,962** matches neither filed total (21,122 / 21,400).
- `OperatingIncomeLoss` computed **−4,578** is not the filing's own subtraction for any period (6M26 gives (2,086)). A four-term fit drawn from four different period-lines — 2,086 + 1,008 + 943 + 541 = 4,578 — closes exactly and is recorded as **coincidence, not mechanism**: a fit that closes exactly is not evidence of a derivation, which is the whole point of DA-29. On the cash-flow row the excess 6,010 − 3,466 = 2,544 equals 1,536 + 1,008, the two prior-year net losses, which is **suggestive of a cross-period collision and is not established**; I record it as suggestive and leave it unresolved.

**Finding 4 — `reported` is not definitionally the filed value (the corollary runs both ways).** The `Assets` row's reported **25,124** *is* a filed figure — it is the **12/31/2025 total of cash, cash equivalents and restricted cash** from the cash-flow reconciliation: 24,747 + 182 + 195 = **25,124**, and the 6/30 counterpart 93,522 + 210 + 620 = **94,352** (https://agentii.ai/v/SPCX/sec8/12). A cash subtotal is served as Total Assets (the filed total is 92,079). The defect is a mis-binding, not an omission — and it is only visible because the *line-level* cells were read.

**Finding 5 — the terms test, applied to my own work.** Every ratio I report as reproduced closes on terms that appear on the statement face with the arithmetic shown in-line. The two that do not (§3.2) are **back-solves by construction**: they close on terms that appear nowhere, which is precisely the class the closure check cannot catch and the terms check can. `computed` is cited in this artifact **only** as evidence of platform behaviour, never as a derivation of a filing value; `reported` is reconciled to the statement face in every row used.

**Finding 6 — validator completeness.** `validate_calculation` on accession `0001628280-26-052535`: **29 rows, 9 pass / 2 warn / 18 fail.** `GrossProfit` returns **zero rows** while both components are filed — recorded `UNVALIDATED-BY-PLATFORM`, never a pass. The two warns are `OtherComprehensiveIncomeLoss...` at a difference of exactly **4** in both periods (40 vs 36; 540 vs 536); four is unattributed and recorded as such. The validator also returns **zero rows** for `us-gaap:GrossProfit`, and `list_xbrl_concepts(namespace="spcx")` returns no extension concepts, so the extension check for this filing is `UNEXERCISED`: a `us-gaap:` zero here is evidence about the **tag**, not about the filing.

## §7 DA-30 — the bases (central)

The served block consumes six concepts that this issuer reports on more than one basis, and names **none** of them. The bases, with cells:

| concept | filed bases found | which one the platform used |
|---|---|---|
| cash | 93,522 (balance sheet) / 94,352 (cash + restricted, cash-flow face) — difference 830, composed of 210 + 620 (https://agentii.ai/v/SPCX/sec8/12) | 93,522 in the ratios, and 25,124/94,352 mis-bound as `Assets` |
| debt | 21,968 (non-current, 12/31); 36,839 (non-current, 6/30); 39,364 (including current 2,525); 38,433 (aggregate principal, MD&A) (https://agentii.ai/v/SPCX/sec8/48) | `long_term_debt` **21,659** is served and matches none of the four; `debt_to_equity` used total liabilities 65,546 |
| equity | 127,224 (total shareholders' equity); 167,344 (APIC) | APIC — in `roe` and in the `debt_to_equity` denominator |
| operating income | consolidated (143) / (2,086) / (970) / (943); AI segment (1,257) / (3,726) / (1,524) / (2,460); Space (542) / (1,204) / (369); Connectivity +1,656 / +2,844 / +923 | the AI segment's, in `operating_margin` |
| net income | (541) / (1,008) / (4,817) / (1,536) net loss; (5,488) attributable to common shareholders after a 671 deemed dividend (https://agentii.ai/v/SPCX/sec8/26) | the 4,817 base in the ratios; 541 in metrics |
| EBITDA | no filed GAAP EBITDA; Adjusted EBITDA **3,538** (3M26) / **4,665** (6M26), issuer-defined (https://agentii.ai/v/SPCX/sec8/46) | an implied **3,831** or **6,379** — neither filed nor derivable |

**The detector is LINE-LEVEL, not total-to-total.** Total assets over total liabilities (192,770 / 65,546) shows no anomaly at all; the mixed-instant defect in `current_ratio` only appears when 108,047, 30,952, 21,122 and 21,400 are read as four separate cells. A total-to-total comparison cannot see it, and neither can a closure check — the division is arithmetically correct.

**A second collapse, of a different kind:** `quick_ratio` and `cash_ratio` are the same value (4.3702). Two slots, one basis, no label.

## §8 Queued register items

- **DA-31 cross-holding / valuation circularity — CONFIRMED as a mechanical transfer, mechanism not appreciation.** The transfer channel is present and quantified: a **671** deemed dividend on preferred conversion for the six months, subtracted between net loss (4,817) and net loss attributable to common shareholders (5,488) (https://agentii.ai/v/SPCX/sec8/26). That is **13.93%** of the six-month net loss redirected from common shareholders by conversion mechanics with **no appreciation event** anywhere in the chain. Separately, the anti-dilutive table reports instruments excluded from the diluted count — xAI redeemable convertible preferred 1,220 and SpaceX redeemable convertible preferred **6,760** against a weighted-average diluted count of 5,864 (3M26). The 6,760 cell sits in the prior-year column of the table I read, so the excluded-instruments-exceed-the-diluted-count comparison is **cross-period and is flagged as such, not asserted as same-period**.
- **DA-32 scale error in one accession — NOT EVIDENT in this accession.** The 18 failing validator rows are not 10^n-consistent with their reported counterparts (489 vs 4,817; −60 vs 518; 78,871 vs 25,124). The queued item's scope is cross-accession; this artifact covers one accession and does not report a scale finding.

## §9 The 001 correction (recorded; 001 stays frozen)

A prior resolution asserted that SPCX's **$(1,257)M AI operating line was DERIVED, never filed. That is false.** The figure is filed on **pp. 30, 31, 44, 45 and 46** of `sec8`:

- p.30, Note 18 segment table, cell: `Income (loss) from operations | (542) | 1,656 | (1,257) | (143)` (https://agentii.ai/v/SPCX/sec8/30).
- p.31, six-month 2026 segment table, cell: (1,204) / 2,844 / **(3,726)** / (2,086) (https://agentii.ai/v/SPCX/sec8/31).
- p.44, AI segment MD&A table, cells: revenue 3,379, total costs 7,105, **loss from operations (3,726)** for the six months and **(1,257)** for the three (https://agentii.ai/v/SPCX/sec8/44).
- p.45, prose: "AI loss from operations for the three months ended June 30, 2026 decreased by $267 million, or 17.5%" (https://agentii.ai/v/SPCX/sec8/45).
- p.46, Segment Adjusted EBITDA reconciliation, which carries the AI segment line (https://agentii.ai/v/SPCX/sec8/46).

The strongest form of the correction is that the MD&A movements are arithmetic on the filed cells and close exactly: **1,524 − 1,257 = 267** (267 / 1,524 = 17.52%, the filed 17.5%) and **3,726 − 2,460 = 1,266** (1,266 / 2,460 = 51.46%, the filed 51.5%). A figure that a filed derivation consumes four times is filed, not derived. The claim is not propagated here, and 001 is not rewritten.

## §10 What this does to PIL-5's falsifier

PIL-5's falsifier is `share_of_001_headline_figures_converted_to_DEMONSTRATED < 0.5`. **001 does not state the denominator.** The ledger must therefore choose a reading, and this artifact reports the fraction under each:

| reading of the denominator | numerator | fraction | falsifier |
|---|---|---|---|
| 001's own headline figures (the set of numeric claims 001 makes) | not enumerable from the corpus I read — 001's headline inventory is not enumerated anywhere | **UNCOMPUTED** | undecidable until the ledger enumerates it |
| the 12 numeric ratio slots served for SPCX, "converted" = served value reproduced exactly from a filed cell | 10 | **0.8333** | not triggered |
| the same 12 slots, "converted" = reproduced **and** both terms are the ratio's own named components (excludes quick_ratio, roe, debt_to_equity, operating_margin) | 6 | **0.5000** | not triggered — at the boundary, saved only by the strict inequality |
| the same 12 slots, "converted" = reproduced **and** own components **and** one consistent basis, instant and duration labelled (further excludes current_ratio, cash_ratio, operating_cf_ratio) | 3 | **0.2500** | **TRIGGERED** |
| all **13** slots including the served null (gross_margin) | as above | **0.7692 / 0.4615 / 0.2308** | the second reading **flips to TRIGGERED** at denominator 13 |
| the single 001 headline figure I actually validated (the $(1,257)M AI operating line) | 1 | **1.0000** | not triggered — but the *content* of the claim inverted: it is filed, not derived |

**The finding the ledger needs:** whether PIL-5 fires depends on whether a null slot counts in the denominator and on whether "converted to DEMONSTRATED" requires a named basis. Under the value-only reading the programme is at 0.769–0.833 and comfortably clear. Under the basis-consistent reading it is at 0.231–0.250 and fires. I report both rather than choose, because the choice is the ledger's and the gap between them is the finding: **the platform's ratios are mostly correct arithmetic on unnamed bases.** Converting a *figure* to DEMONSTRATED does not convert the *basis* to DEMONSTRATED, and this artifact demonstrates that the two come apart by 46.47 percentage points on a single ratio.

## §11 What I could NOT verify, and why

> **⚠️ CORRECTION, appended 2026-09-18 after direct re-verification. THE FIRST SENTENCE BELOW IS UNQUALIFIED, NOT FALSE — and the distinction is the finding.**
> **There are TWO `agentii-investment-intelligence` trees, and their `packaging/` directories differ.**
> The **working tree** (`/Users/frank/A/agenzym/agentii-investment-intelligence/packaging/`) contains
> `.gitkeep`, `README.md`, `export.py`, `export.sh`, `skillseekers.config.yaml` **AND `targets/`** —
> four subdirs, each with a real `SKILL.md`, **all four failing the six known hashes (0/6).**
> The **marketplace tree** (`~/.claude/plugins/marketplaces/agentii-investment-intelligence/packaging/`)
> contains **those same five files and NO `targets/`.**
> **So the listing below is a VERBATIM-ACCURATE DESCRIPTION OF THE MARKETPLACE COPY. It is not a
> fabrication and not a bad search — it is an accurate observation of a tree that was not named.**
> This artifact works in the marketplace tree (the tree Claude Code loads skills from); the
> workspace's `skill_pins.jsonl` was built against the working tree. **Both are right about
> different objects.**
> **⚠️ The failure class is therefore DA-30's, not DA-29's: one quantity on two bases, quoted
> without a basis field** — the same shape as the collapsed Class A/B/C diluted EPS and the
> register's own basis-collapsed "~65% GM" row. **Not a fabricated negative; an unnamed comparison.**
> **⚠️ And the operational consequence is asymmetric:** the decoys exist **only in the working tree**,
> so a pin computed from the marketplace root would never meet one — while this workspace's own pins
> all rest on the tree where all four exist. Everything else in the bullet (the `models-and-pitches`
> and `cache.bak` hashes, the six-skill mismatch sweep) was verified and STANDS.

- **The four `packaging/targets/{claude-code,codex,generic-cli,cowork}` decoys exist, and all four fail the pin.** They are not under the installed marketplace copy — `/Users/frank/.claude/plugins/marketplaces/agentii-investment-intelligence/packaging/` contains only `.gitkeep`, `README.md`, `export.py`, `export.sh` and `skillseekers.config.yaml` — they are under the **second checkout** `/Users/frank/A/agenzym/agentii-investment-intelligence/packaging/targets/`, as bare skill directories (`packaging/targets/<target>/ratio-analysis`, without the `skills/agentii/` wrapper that every keeper copy has). Hashes against the authoritative `2d27c7f751fa`: claude-code **3f69103fbf71**, generic-cli **3f69103fbf71**, codex **271f4893b4d9**, cowork **42c1dd5f52f1** — **4 of 4 differ**, and claude-code and generic-cli are byte-identical to each other, so the decoy set is three distinct contents and none of them is the keeper. The warning is confirmed in full. Two further decoys: `plugins/vertical-plugins/models-and-pitches/skills/agentii/ratio-analysis` **9b1d7a504789** (identical content in both checkouts) and `cache.bak/agentii-investment-intelligence/quantitative-analysis/2.2.1/skills/agentii/ratio-analysis` **296490e6f094**. Every one of the six known skills also mismatches under `cache.bak` (operational-kpi a2c3d34b1acd, unit-economics 887f82f355ae, secular-trends fa341dfc985c in two roots, supply-chain 216afc3763a9, competitive 7ab86ffee9c1 in two roots, risk 69cdfb5886fb in two roots). The keepers match in three distinct roots, one of them a packaged flat skills directory (`.claude/skills/agentii/<skill>`) rather than a `plugins/*/*/skills/agentii/<skill>` path, which is a fifth keeper location and the one that survives if the marketplace tree is moved. **Correction to my own first pass:** I initially searched only the installed marketplace and reported these four decoys as absent from the machine. They are present, and the pin is now falsified against all four. The pin is unaffected — this is the failure mode the register warns about, ruling a thing out from a scoped search.

> **⚠️ SECOND CORRECTION, appended 2026-09-18 — and this one changes a METHOD, not a fact.**
> The `skill_pin` reasoning in the frontmatter cites corroboration "in two independent roots
> (`plugins/vertical-plugins/*` and `plugins/agentii-plugin/*`)". **`plugins/agentii-plugin/skills/agentii`
> IS A PURE SYMLINK FARM — 70 of 70 entries are symlinks**, e.g.
> `ratio-analysis -> ../../../vertical-plugins/quantitative-analysis/skills/agentii/ratio-analysis`.
> **A symlinked root agrees with its target by construction, so it cannot corroborate it.**
> **The genuine disagreement is 1 real copy vs 1 real copy, not 2-to-1:** the real candidates are
> `vertical-plugins/quantitative-analysis` (inode 200960032) = `2d27c7f751fa` and
> `vertical-plugins/models-and-pitches` (inode 232779211) = `9b1d7a504789`. **The pin still stands,
> but on the THESIS-MEMBERSHIP ground (`spec.md` §3 and `reproduce.md` line 25 both place the skill
> in `quantitative-analysis`) and on `models-and-pitches` lacking a `SKILL.md` — NOT on a majority
> vote, which was inflated by the symlink farm.** *Method rule: an agreement count must exclude
> symlinked roots, or it counts one root twice.*
- **`GrossProfit`**: zero facts and zero validator rows. I record `UNVALIDATED-BY-PLATFORM`; the four gross margins in §2.5 are my arithmetic from read cells, not a platform value.
- **The three-month 2025 share-based compensation cell** was not read, so the 3M25/6M25 Adjusted EBITDA identities are `NOT READ`, not fitted.
- **The equity section's common-stock par line** was not captured cell-wise (inferred as 13 from the closing residual).
- **The platform's tree weights** for the income-statement and balance-sheet concepts were not returned for every arc; the weight discriminator is stated only for the cash-flow arcs where I verified it, and the DA-23 result rests on the articulation detector, not on assumed weights.
- **`GrossProfit` extension tags**: `list_xbrl_concepts(namespace="spcx")` returns none, so no extension-based reading is available; absence was established by reading pages, not by a zero-row filter — and a compound filter returning zero is not absence.
- **Two validator rows remain unreproducible** (`OperatingIncomeLoss` computed −4,578; `NetCashProvidedByUsedInOperatingActivities` computed 6,010) and one is a mixed-instant back-solve (`AssetsCurrent` 37,439). Recorded as platform defects with the exact arithmetic, not resolved.
- **Period semantics of the 12/31 instants** are taken from the comparative column of the filed balance sheet; I did not read the prior 10-K or prospectus, so the 12/31 figures are as the Q2 filing presents them.

## §12 Verification and sources

`python3 tools/check_citations.py theses/002-evidence-validation` and `python3 tools/check_contract.py theses/002-evidence-validation` — both run against this file; see the run log in the phase ledger. All 12 citations below are `located_via: read_source_pages`, i.e. every page number was established by opening the page and reading its cells; no page number and no quotation is inherited from an outline description.

- p.4 balance sheet cells (https://agentii.ai/v/SPCX/sec8/4)
- p.5 statements of operations cells (https://agentii.ai/v/SPCX/sec8/5)
- p.9 statements of cash flows cells (https://agentii.ai/v/SPCX/sec8/9)
- p.12 cash and restricted cash reconciliation table (https://agentii.ai/v/SPCX/sec8/12)
- p.22 Note 11 balance-sheet component tables (https://agentii.ai/v/SPCX/sec8/22)
- p.26 EPS reconciliation and anti-dilutive table (https://agentii.ai/v/SPCX/sec8/26)
- p.30 Note 18 segment table, three months 2026 (https://agentii.ai/v/SPCX/sec8/30)
- p.31 segment tables, six months 2026 and three months 2025 (https://agentii.ai/v/SPCX/sec8/31)
- p.44 AI segment MD&A table (https://agentii.ai/v/SPCX/sec8/44)
- p.45 MD&A prose on the AI operating loss (https://agentii.ai/v/SPCX/sec8/45)
- p.46 Adjusted EBITDA and Segment Adjusted EBITDA reconciliation (https://agentii.ai/v/SPCX/sec8/46)
- p.48 debt footnote (https://agentii.ai/v/SPCX/sec8/48)
