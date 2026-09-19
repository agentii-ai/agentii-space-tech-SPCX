---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: GOOG
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
    chosen_reading: "sign strip on negative income facts — tested on EVERY period this artifact quotes (six consolidated periods, seven segment periods) by the component identity (revenues − cost of revenue − R&D − S&M − G&A = operating income) and the segment-sum identity, never by EPS × shares. TWO-TRACK verdict: CLEAN on Alphabet's own reported facts (20 of 20 identities close); CONTAMINATED on the instrument's `reported` column, where one exact |computed| == |reported| opposite-sign pair exists (§3.3)."
  - da_id: "DA-24"
    chosen_reading: "disposal gain inside the operating line — REFUTED at GOOG: the only divestiture is pending (GFiber, closing late 2026, results still in Other Bets, no impairment recognised), so no disposal gain exists in any period. A MIRROR-IMAGE hazard is present and disclosed: two non-operating items sit INSIDE the operating line (§4.3)."
  - da_id: "DA-25"
    chosen_reading: "issuer-defined per-unit metric not reproducible from the segment tables — CONFIRMED at GOOG in two instances and two sub-modes: (a) monetization metrics disclosed ONLY as rates of change, so no level exists to reproduce (§5.1); (b) revenue backlog, an issuer-defined stock metric absent from the segment tables whose DEFINITION CHANGED in Q1 2026 with no comparative restated (§5.2)."
  - da_id: "DA-26"
    chosen_reading: "annual value mislabelled as quarterly — CONFIRMED at GOOG with two instances. The platform's 'Q4 2025' revenue $402,836M is read-verified as the FY2025 ANNUAL total; the defect is row-wide and duration-specific. GOOG is the first site where the mislabelled row is independently identified rather than inferred by subtraction (§6)."
  - da_id: "DA-27"
    chosen_reading: "fiscal labels generated from the calendar quarter — CONFIRMED at GOOG on method AND on outcome. Unlike SPCX (correct by accident, source `default`), GOOG's offset is served from a database (`fiscal_year_end_month_source: gold_companies`) and is actively wrong for a Dec-31 filer: labels are displaced ~2 months AND ~1 year, and quarters are synthesised into FY2027 (§7)."
  - da_id: "DA-28"
    chosen_reading: "IPO capital-structure discontinuity — NOT APPLICABLE for IPO (2004, 22 years outside any window). Three adjacent findings recorded: (a) the only split ratios on record at GOOG are 20 (2022) and 2 (2014) — there is NO 5-for-1, and neither falls in the comparison window; (b) a capital-structure event DOES fall inside the window — the June 2026 issuance of 6.25% mandatory convertible preferred stock, which for the first time makes net income ≠ net income available to common stockholders and makes diluted EPS class-dependent (Class A $9.12, Class C $9.11), plus a 2.213× share-count basis collapse; (c) a scheduled, price-dependent conversion on or about 15 May 2029 — a forward discontinuity DA-28's IPO framing cannot reach (§8)."
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM
platform_residual: "UNRESOLVABLE-FROM-PLATFORM — the rule by which the calculation engine selects WHICH dimensional member to serve as `computed` and as `reported` for a parent concept is a property of the engine's role-resolution internals. It is not derivable from any public source: the same parent resolves to a different member in different periods of the same filing, and the member set is not disclosed. Recorded as a residual rather than diagnosed. §3.4"
cross_holding_register: "RECOMMENDED — a new register entry, distinct from DA-23 and from the unregistered DA-29 common-control candidate. GOOG's own disclosure establishes the circularity: 68.7% of Q2 2026 net income and 68.7% of diluted EPS come from a non-cash revaluation of equity Alphabet holds. §10"
citations:
  - figure: "Consolidated statements of income, four periods — Q2 2026: revenues 119,796; cost of revenues 45,943; R&D 18,219; S&M 8,403; G&A 6,461; total costs and expenses 79,026; income from operations 40,770; other income (expense) net 97,983; income before income taxes 138,753; provision for income taxes 26,560; net income 112,193; preferred stock dividends 86; net income available to common stockholders 112,107; basic EPS 9.23; diluted EPS 9.11. Q2 2025 comparatives 96,428 / 39,039 / 13,808 / 7,101 / 5,209 / 65,157 / 31,271 / 2,662 / 33,933 / 5,737 / 28,196 / basic 2.33 / diluted 2.31. Six-month columns 186,662 / 229,692 / 124,785 / 149,226 / 61,877 / 80,466 / 174,771"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 5
    url: https://agentii.ai/v/GOOG/sec156/5
    located_via: read_source_pages
  - figure: "Segment table — revenues Google Services 82,543 -> 94,540; Google Cloud 13,624 -> 24,768; Other Bets 373 -> 382; hedging (112) -> 106; total 96,428 -> 119,796. Operating income (loss): Google Services 33,063 -> 39,544; Google Cloud 2,826 -> 8,814; Other Bets (1,246) -> (1,799); Alphabet-level activities (3,372) -> (5,789); total income from operations 31,271 -> 40,770. Six-month columns 159,807 / 25,884 / 823 / 148 / 186,662 and 65,745 / 5,003 / (2,472) / (6,399) / 61,877"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 40
    url: https://agentii.ai/v/GOOG/sec156/40
    located_via: read_source_pages
  - figure: "Segment profitability and OI&E component table — segment operating income (loss) repeated for both three- and six-month periods; gain (loss) on equity securities, net 1,286 -> 99,031; income (loss) and impairment from equity method investments, net 419 -> (35); other 72 -> (973); other income (expense), net 2,662 -> 97,983"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 50
    url: https://agentii.ai/v/GOOG/sec156/50
    located_via: read_source_pages
  - figure: "Executive overview — consolidated revenues 96,428 -> 119,796 (+24%); cost of revenues 39,039 -> 45,943; operating expenses 26,118 -> 33,083; operating income 31,271 -> 40,770; operating margin 32% -> 34%; OI&E 2,662 -> 97,983 (+3,581%); net income available to common stockholders +298%; diluted EPS 2.31 -> 9.11"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 45
    url: https://agentii.ai/v/GOOG/sec156/45
    located_via: read_source_pages
  - figure: "Key highlights — 'OI&E of $98.0 billion for the three months ended June 30, 2026 included net gains on equity securities of $99.0 billion, primarily related to unrealized gains in our equity securities portfolio from SpaceX and a private company'; the $2.1B PriceRunner accrual of which 'principal damages of $1.5 billion were accrued in general and administrative expenses in our Google Services segment, and accrued interest and costs of $581 million was recognized in other income (expense), net'; $49.6B equity raise; $20.3B senior notes; capex $44.9B; operating cash flow $39.1B; 198,933 employees"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 46
    url: https://agentii.ai/v/GOOG/sec156/46
    located_via: read_source_pages
  - figure: "Fair value hierarchy — marketable equity securities 86,049 (Level 1) + 1,014 (Level 2) = 87,063 as of June 30, 2026, footnote (1) 'Includes $80.0 billion of Space Exploration Technologies Corp. (SpaceX) shares subject to short-term restrictions on the ability to sell'; other non-current assets footnote (2) 'Includes $14.1 billion of SpaceX shares subject to long-term restrictions on the ability to sell through the third quarter of 2027'. Total $94.1B of SpaceX stock, classified Level 1"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 15
    url: https://agentii.ai/v/GOOG/sec156/15
    located_via: read_source_pages
  - figure: "Non-marketable securities roll-forward — carrying value under the measurement alternative 64,094 -> 124,259; cumulative upward adjustments 44,485 -> 85,732; total non-marketable securities 68,687 -> 131,461; footnote (1) 'our investments in non-marketable securities accounted for under the measurement alternative primarily consist of our investment in a private company'. Equity-securities gain table: gross unrealized gain on the measurement-alternative portfolio 670 -> 77,544; unrealized net gain on marketable and other equity securities 853 -> 21,399; total gain on equity securities 1,286 -> 99,031"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 18
    url: https://agentii.ai/v/GOOG/sec156/18
    located_via: read_source_pages
  - figure: "Consolidated balance sheets — total assets 595,281 -> 921,983; non-marketable securities 68,687 -> 131,461; long-term debt 46,547 -> 98,165; total liabilities 180,016 -> 281,503; total stockholders' equity 415,265 -> 640,480; 'Class A, Class B, and Class C stock and additional paid-in capital, $0.001 par value per share: 300,000 shares authorized (Class A 180,000, Class B 60,000, Class C 60,000); 12,088 (Class A 5,822, Class B 837, Class C 5,429) and 12,230 (Class A 5,868, Class B 835, Class C 5,527) shares issued and outstanding'"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 4
    url: https://agentii.ai/v/GOOG/sec156/4
    located_via: read_source_pages
  - figure: "Cover page — three listed classes: Class A Common Stock (GOOGL), Class C Capital Stock (GOOG), depositary shares GOOGM and GOOGN for the 6.25% Series A/B mandatory convertible preferred; 'As of July 15, 2026, there were 5,868 million shares of Alphabet's Class A stock outstanding, 835 million shares of Alphabet's Class B stock outstanding, and 5,527 million shares of Alphabet's Class C stock outstanding'"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 1
    url: https://agentii.ai/v/GOOG/sec156/1
    located_via: read_source_pages
  - figure: "Revenue backlog — 'As of June 30, 2026, we had $519.5 billion of remaining performance obligations (\"revenue backlog\"), of which $513.9 billion related to Google Cloud'; and the definition change: 'In the first quarter of 2026, we elected to change our reporting of revenue backlog to also include contracts with an original expected term of one year or less'"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 14
    url: https://agentii.ai/v/GOOG/sec156/14
    located_via: read_source_pages
  - figure: "Monetization metrics — 'The following table presents changes in monetization metrics ... expressed as a percentage': Google Search & other paid clicks change 13% (three months) and 13% (six months); cost-per-click change 3% and 4%; Google Network impressions change (12)% and (10)%; cost-per-impression change 13% and 10%. Revenues by type: Google Search & other 54,190 -> 63,271; YouTube ads 9,796 -> 11,055; Google Network 7,354 -> 7,303; Google advertising 71,340 -> 81,629; Google subscriptions, platforms, and devices 11,203 -> 12,911; Google Services total 82,543 -> 94,540; Cloud 13,624 -> 24,768; Other Bets 373 -> 382; hedging (112) -> 106; total 96,428 -> 119,796"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 47
    url: https://agentii.ai/v/GOOG/sec156/47
    located_via: read_source_pages
  - figure: "Pending divestiture — 'In March 2026, we entered into a definitive agreement to contribute our ownership interest in GFiber, a wholly owned subsidiary, into a newly formed entity. Upon closing, we expect to receive $1.5 billion in cash, a $2.0 billion note receivable, and a 49.99% equity interest ... The transaction is expected to close in late 2026. GFiber meets the criteria for held for sale classification. No impairment loss was recognized upon initial classification as held for sale ... The operating results of GFiber remain included within the Other Bets segment through the close of the transaction.' Also Wiz ($29,467M purchase price, goodwill 22,705) and Intersect ($5,868M, goodwill 2,174, PP&E 5,129)"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 29
    url: https://agentii.ai/v/GOOG/sec156/29
    located_via: read_source_pages
  - figure: "Legal matters — Android: EC fine reduced to EUR 4.1B, appeal denied July 2026, 'the EC decision is now final. In July 2026, we made a cash payment of $5.2 billion for the fine plus accrued interest'; AdSense for Search: EUR 1.5B fine annulled by the General Court in September 2024, EC appeal pending"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 31
    url: https://agentii.ai/v/GOOG/sec156/31
    located_via: read_source_pages
  - figure: "Advertising technology — 'in September 2025, the EC announced its decision ... The EC decision imposed a EUR 3.0 billion fine ... We recognized a charge of $3.5 billion in the third quarter of 2025, and we placed bank guarantees in the fourth quarter of 2025 in lieu of cash payment'"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 32
    url: https://agentii.ai/v/GOOG/sec156/32
    located_via: read_source_pages
  - figure: "Q2 2026 results 8-K, Exhibit 99.1 — OI&E table (interest income 1,050 -> 1,430; interest expense (261) -> (1,278); gain on equity securities 1,286 -> 99,031; other income (expense) net 2,662 -> 97,983) with footnote (1): 'For Q2 2026, the net effect of the gain on equity securities of $99.0 billion increased the provision for income tax, net income, and diluted net income per common share by $21.9 billion, $77.1 billion, and $6.26, respectively.' Free-cash-flow table by quarter: operating cash flow Q3 2025 48,414 / Q4 2025 52,402 / Q1 2026 45,790 / Q2 2026 39,069"
    ticker: GOOG
    form_type: 8-K
    citation_id: sec155
    page_no: 12
    url: https://agentii.ai/v/GOOG/sec155/12
    located_via: read_source_pages
  - figure: "FY2025 10-K, revenues by type — Google Search & other 198,084 -> 224,532; YouTube ads 36,147 -> 40,367; Google Network 30,359 -> 29,792; Google advertising 264,590 -> 294,691; subscriptions, platforms, devices 40,340 -> 48,030; Google Services total 304,930 -> 342,721; Google Cloud 43,229 -> 58,705; Other Bets 1,648 -> 1,537; hedging 211 -> (127); TOTAL REVENUES 350,018 -> 402,836. Also 'Other Bets operating loss of $7.5 billion for the year ended December 31, 2025 included a $2.1 billion employee compensation charge recognized in the fourth quarter for Waymo, primarily reflected in research and development expenses'; OI&E $29.8B including $24.1B of equity-securities gains; operating cash flow $164.7B; capex $91.4B"
    ticker: GOOG
    form_type: 10-K
    citation_id: sec144
    page_no: 34
    url: https://agentii.ai/v/GOOG/sec144/34
    located_via: read_source_pages
  - figure: "FY2025 10-K segment table, three annual columns — operating income (loss): Google Services 95,858 / 121,263 / 139,404; Google Cloud 1,716 / 6,112 / 13,910; Other Bets (4,095) / (4,444) / (7,515); Alphabet-level activities (9,186) / (10,541) / (16,760); total income from operations 84,293 / 112,390 / 129,039. Revenues: 272,543 / 304,930 / 342,721; 33,088 / 43,229 / 58,705; 1,527 / 1,648 / 1,537; hedging 236 / 211 / (127); total 307,394 / 350,018 / 402,836"
    ticker: GOOG
    form_type: 10-K
    citation_id: sec144
    page_no: 88
    url: https://agentii.ai/v/GOOG/sec144/88
    located_via: read_source_pages
  - figure: "Q1 2026 consolidated statements of income — three months ended March 31: revenues 90,234 -> 109,896; cost of revenues 36,361 -> 41,271; R&D 13,556 -> 17,032; S&M 6,172 -> 7,606; G&A 3,539 -> 4,291; total costs and expenses 59,628 -> 70,200; income from operations 30,606 -> 39,696; OI&E 11,183 -> 37,716; income before income taxes 41,789 -> 77,412; provision for income taxes 7,249 -> 14,834; net income 34,540 -> 62,578; basic EPS 2.84 -> 5.17; diluted EPS 2.81 -> 5.11"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec149
    page_no: 5
    url: https://agentii.ai/v/GOOG/sec149/5
    located_via: read_source_pages
  - figure: "Note 11 Stockholders' Equity — 'On June 4, 2026, the company completed an underwritten public offering of 29 million Class A shares at a price of $355.1982 per share and 29 million Class C shares at a price of $351.8018 per share'; 'a private placement of 14 million Class A and 14 million Class C shares to an affiliate of Berkshire Hathaway Inc.'; net proceeds '$20.5 billion from the public offering and $10.0 billion from the private placement'. Mandatory convertible preferred — 'On June 5, 2026, the company issued an aggregate amount of 385 million Series A and Series B depositary shares, representing 19 million shares of 6.25% Mandatory Convertible Preferred Stock, split evenly into Series A (indexed to Class A stock) and Series B (indexed to Class C stock). Each depositary share represents a 1/20th fractional interest'; 'liquidation preference of $1,000 per share ($50 per depositary share)'; 'Aggregate net proceeds were $19.0 billion'; 'each outstanding share will automatically convert on the mandatory conversion date, which is on or about May 15, 2029. The conversion rate for each share of our Series A mandatory convertible preferred stock will be between 2.2520 and 2.8160 shares of Class A stock, and Series B ... between 2.2740 and 2.8420 shares of Class C stock, depending on the applicable market value'. Capped call transactions entered into in connection with the issuance"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 34
    url: https://agentii.ai/v/GOOG/sec156/34
    located_via: read_source_pages
  - figure: "Note 12 Net Income Per Common Share — 'We compute net income per common share of Class A, Class B, and Class C stock using the two-class method'; 'The dilutive effect of mandatory convertible preferred shares is reflected in diluted earnings per common share pursuant to the if-converted method'; 'The computation of the diluted net income per common share of Class A stock assumes the conversion of Class B stock, while the diluted net income per common share of Class B stock does not assume the conversion of those shares'; 'Net income available to common stockholders is calculated by adjusting net income to deduct accumulated and declared dividends on the mandatory convertible preferred stock'"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 36
    url: https://agentii.ai/v/GOOG/sec156/36
    located_via: read_source_pages
  - figure: "Note 12 EPS computation tables, three months ended June 30, 2025 and 2026. Net income available to common stockholders, consolidated: 28,196 -> 112,107 (Class A 13,536 -> 53,843; Class B 1,981 -> 7,703; Class C 12,679 -> 50,561). Diluted numerator: preferred stock dividends declared and accumulated 0 -> 86 (Class A 47, Class C 39); reallocation of undistributed earnings (88)/(11)/88 -> (700)/(91)/700; net income 28,196 -> 112,193 (Class A 15,429 -> 60,893; Class B 1,970 -> 7,612; Class C 12,767 -> 51,300). Diluted denominator: shares used in basic computation 12,122 -> 12,151 (Class A 5,819 -> 5,836; Class B 852 -> 835; Class C 5,451 -> 5,480); conversion of Class B to Class A 852 -> 835; RSUs and other contingently issuable shares 76 -> 142; conversion of preferred stock 0 -> 16 (Class A 8, Class C 8); number of shares used in per share computation 12,198 -> 12,309 (Class A 6,671 -> 6,679; Class B 852 -> 835; Class C 5,527 -> 5,630). Diluted net income per common share: CLASS A $2.31 -> $9.12; CLASS B $2.31 -> $9.12; CLASS C $2.31 -> $9.11; consolidated $2.31 -> $9.11. Basic net income per common share $2.33 -> $9.23 all classes"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 37
    url: https://agentii.ai/v/GOOG/sec156/37
    located_via: read_source_pages
---
# GOOG — the Six-DA Register at the Calibration Site (PIL-3)

**Phase 3 · `GOOG × recent-quarter` · defect census, pillar PIL-3.**

GOOG is the calibration case for PIL-3 for two reasons. It is the site of **two instrument
defects** found in Phase 2 (`validate_calculation`'s `reported` column, and DA-26), and it is a
**new hazard class** — Alphabet carries a large equity stake in another universe member, so its
own reported earnings are partly a mark on that member's valuation.

This artifact runs the **full six-DA register**, every period, on read-verified pages. It is the
only GOOG artifact in 002 that does so.

**Sources.** Form 10-Q accession `0001652044-26-000071` (**`sec156`**, 64 pages); Q2 2026 results
8-K accession `0001652044-26-000066` (**`sec155`**, 13 pages); FY2025 10-K accession
`0001652044-26-000018` (**`sec144`**, 99 pages); Q1 2026 10-Q accession `0001652044-26-000048`
(**`sec149`**, 53 pages). Phase 2's GOOG artifact is cited, never re-derived.

---

## 0. Summary of verdicts

| DA | Verdict at GOOG | Basis |
|---|---|---|
| DA-23 | **CLEAN on the issuer, CONTAMINATED on the instrument** | 20 of 20 component and segment-sum identities close; but one exact `\|computed\| == \|reported\|` opposite-sign pair exists in the `reported` column (§3.3) |
| DA-24 | **REFUTED** | the only divestiture is pending and unclosed; no disposal gain exists. A **mirror-image** hazard is present and disclosed (§4.3) |
| DA-25 | **CONFIRMED** (two instances, two new sub-modes) | rate-only monetization metrics; a backlog definition changed mid-window with no comparative restated (§5) |
| DA-26 | **CONFIRMED** (two instances) | "Q4 2025" revenue = $402,836M = the **FY2025 annual** total; row-wide and duration-specific (§6) |
| DA-27 | **CONFIRMED, and NOT benign** | offset served from a database (`gold_companies`) for a Dec-31 filer; labels displaced ~2 months and ~1 year; FY2027 synthesised (§7) |
| DA-28 | **NOT APPLICABLE** (IPO) + three in-window capital-structure findings | no 5-for-1 exists and neither recorded split falls inside the window; but a 2.213× share-count basis collapse, a new preferred class, and a scheduled 2029 conversion all do (§8) |

**Register candidates produced by this census: three** — the `reported`-column/segment-member defect
(now mechanistically established, §3.4), cross-holding contamination (§10), and the scheduled
capital-structure discontinuity that DA-28's IPO framing cannot see (§8.3(b)(iii)).

---

## 1. The component identity, run in-line on every quoted period

Per the binding instrument rule, the **`computed` vs `reported` pair is read through the component
identity**. `EPS × shares` is inadmissible and is not used anywhere in this artifact.

### 1.1 Consolidated (`revenues − cost of revenue − R&D − S&M − G&A = operating income`)

| Period | Revenues | CoR | R&D | S&M | G&A | Total costs | Operating income | Identity |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Q2 2026 | 119,796 | 45,943 | 18,219 | 8,403 | 6,461 | 79,026 | 40,770 | 119,796 − 79,026 = **40,770** ✓ |
| Q2 2025 | 96,428 | 39,039 | 13,808 | 7,101 | 5,209 | 65,157 | 31,271 | 96,428 − 65,157 = **31,271** ✓ |
| 6M 2026 | 229,692 | 87,214 | 35,251 | 16,009 | 10,752 | 149,226 | 80,466 | 229,692 − 149,226 = **80,466** ✓ |
| 6M 2025 | 186,662 | 75,400 | 27,364 | 13,273 | 8,748 | 124,785 | 61,877 | 186,662 − 124,785 = **61,877** ✓ |
| Q1 2026 | 109,896 | 41,271 | 17,032 | 7,606 | 4,291 | 70,200 | 39,696 | 109,896 − 70,200 = **39,696** ✓ |
| Q1 2025 | 90,234 | 36,361 | 13,556 | 6,172 | 3,539 | 59,628 | 30,606 | 90,234 − 59,628 = **30,606** ✓ |

All six periods from the face of the filings — Q2 columns at
[📄 GOOG 10-Q p.5](https://agentii.ai/v/GOOG/sec156/5), Q1 columns at
[📄 GOOG 10-Q p.5](https://agentii.ai/v/GOOG/sec149/5). **6 of 6 close exactly.**

### 1.2 Segment sum (`Σ segment operating income = total income from operations`)

| Period | Google Services | Google Cloud | Other Bets | Alphabet-level | Sum | Total OI |
|---|---:|---:|---:|---:|---:|---:|
| Q2 2026 | 39,544 | 8,814 | (1,799) | (5,789) | **40,770** | 40,770 ✓ |
| Q2 2025 | 33,063 | 2,826 | (1,246) | (3,372) | **31,271** | 31,271 ✓ |
| 6M 2026 | 80,133 | 15,412 | (3,899) | (11,180) | **80,466** | 80,466 ✓ |
| 6M 2025 | 65,745 | 5,003 | (2,472) | (6,399) | **61,877** | 61,877 ✓ |
| FY2025 | 139,404 | 13,910 | (7,515) | (16,760) | **129,039** | 129,039 ✓ |
| FY2024 | 121,263 | 6,112 | (4,444) | (10,541) | **112,390** | 112,390 ✓ |
| FY2023 | 95,858 | 1,716 | (4,095) | (9,186) | **84,293** | 84,293 ✓ |

Quarterly columns at [📄 GOOG 10-Q p.40](https://agentii.ai/v/GOOG/sec156/40) and
[📄 GOOG 10-Q p.50](https://agentii.ai/v/GOOG/sec156/50); annual columns at
[📄 GOOG 10-K p.88](https://agentii.ai/v/GOOG/sec144/88). **7 of 7 close exactly.**

Segment *revenues* sum to consolidated revenue on the same seven periods (e.g. Q2 2026:
94,540 + 24,768 + 382 + 106 = **119,796**; FY2025: 342,721 + 58,705 + 1,537 − 127 = **402,836**).

### 1.3 The gross-profit bound (detector 3 — the weak one)

`operating income ≤ revenues − cost of revenue`:

| Period | Gross profit | Operating income | Bound |
|---|---:|---:|---|
| Q2 2026 | 73,853 | 40,770 | pass |
| Q2 2025 | 57,389 | 31,271 | pass |
| 6M 2026 | 142,478 | 80,466 | pass |
| 6M 2025 | 111,262 | 61,877 | pass |
| Q1 2026 | 68,625 | 39,696 | pass |
| Q1 2025 | 53,873 | 30,606 | pass |

**6 of 6 pass — and this detector is why the `reported` defect is dangerous.** `us-gaap:GrossProfit`
returns **zero facts at GOOG**; gross profit has to be derived as revenues − cost of revenue, a
coverage gap worth recording. More importantly, the corrupted FY2024 `reported` value of **4,444**
(§3.3) passes this bound *silently* — a value that is far below the true 112,390 still satisfies
`OI ≤ gross profit`. **The bound can only catch an overstatement, never an understatement.**

---

## 2. Sample size and the MRCY rule

**The MRCY rule — DA-23 must run on every period an artifact quotes — is satisfied above by
construction.** GOOG makes the rule bite in a specific way, and it is worth stating precisely
because it is the opposite of the SPCX case:

> **At GOOG the current period is clean and the comparator is corrupt.**

Within the *same* `validate_calculation` payload for the Q2 2026 10-Q:

- `us-gaap:OperatingIncomeLoss` **Q2 2026**: computed 40,770 / reported 40,770 → **`pass`**
- `us-gaap:OperatingIncomeLoss` **Q2 2025**: computed −10,660 / reported **2,826** → `fail`

An artifact that quoted only the current quarter and moved on would see a `pass` and conclude the
period was clean, while the comparative it must display beside it is wrong. That is MRCY's failure
mode reproduced on a different axis — MRCY's headline year was clean and both comparators flipped;
GOOG's headline quarter is clean and its comparator is corrupt.

---

## 3. DA-23 — sign stripping

### 3.1 Track A: Alphabet's own facts are clean, per period

001 placed GOOG on the clean side of the census (positive/positive, "no (5/5)"). **Verified
per-period, not inherited.** Every `OperatingIncomeLoss` and `NetIncomeLoss` fact served by the
platform for GOOG is positive and, where it is correct at all, correct with the right sign. The 20
identities in §1 are the evidence: a sign-stripped fact cannot satisfy an arithmetic identity that
requires its sign. **Alphabet is profitable at the consolidated level and is untouched by the
issuer-side defect.**

### 3.2 Track B: the `reported` column is contaminated, and it is not only comparatives

Phase 2 registered the `reported`-column corruption on **comparatives** at GOOG. **That
characterisation is correct but incomplete.** Running the same instrument on three filings shows
the corruption on **current** periods too:

| Filing | Period | Concept | `reported` | Filed | Factor |
|---|---|---|---:|---:|---:|
| Q2 2026 10-Q | Q2 2025 | OperatingIncomeLoss | 2,826 | **31,271** | 11.1× |
| Q2 2026 10-Q | Q2 2025 | Revenues | 138 | **96,428** | 699× |
| Q2 2026 10-Q | Q2 2025 | NetIncomeLoss | 78 | **28,196** | 361× |
| Q1 2026 10-Q | **Q1 2026** | OperatingIncomeLoss | 2,100 | **39,696** | 18.9× |
| Q1 2026 10-Q | **Q1 2026** | Revenues | 211 | **109,896** | 521× |
| FY2025 10-K | FY2024 | OperatingIncomeLoss | 4,444 | **112,390** | 25.3× |
| FY2025 10-K | FY2024 | Revenues | 174 | **350,018** | 2,012× |
| FY2025 10-K | FY2023 | Revenues | 213 | **307,394** | 1,443× |

Filed values are read-verified: Q2 2026/Q2 2025 at [📄 GOOG 10-Q p.5](https://agentii.ai/v/GOOG/sec156/5),
Q1 2026 at [📄 GOOG 10-Q p.5](https://agentii.ai/v/GOOG/sec149/5), FY2024/FY2023 totals at
[📄 GOOG 10-K p.34](https://agentii.ai/v/GOOG/sec144/34) and
[📄 GOOG 10-K p.88](https://agentii.ai/v/GOOG/sec144/88).

**A silence asymmetry governs which of these are dangerous.** Corruption that *understates* an
income result passes the gross-profit bound silently — the 25.3× FY2024 case is the exhibit.
Corruption that understates **revenue** would fail loudly, because the segment revenues would not
sum to it. This is why the operating-income cases, not the revenue cases, are the ones that reach an
artifact unremarked.

### 3.3 The DA-23 signature is present — on the instrument, not the issuer

DA-23's formal test is `|computed| == |reported|` with **opposite signs**. At GOOG there is exactly
one clean instance, and it is on a comparative:

```
FY2025 10-K · OtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentNetOfTax · FY2024
computed  −666,000,000
reported  +666,000,000
diff      +1,332,000,000
status    fail
```

**Exact magnitude, opposite sign.** This is DA-23's signature reproduced inside the platform's own
`reported` column, on a $666M item, on a comparative — the same locus as every other instance in
this census.

And the two operating-income cases are sign strips of a different kind:

- FY2024 `OperatingIncomeLoss` reported **4,444** = **|Other Bets FY2024 operating loss|**, which the
  filing gives as **(4,444)** at [📄 GOOG 10-K p.88](https://agentii.ai/v/GOOG/sec144/88).
- Q1 2026 `OperatingIncomeLoss` reported **2,100** = **|Other Bets Q1 2026 operating loss|**,
  obtained as 6M 2026 (3,899) − Q2 2026 (1,799) = (2,100) from
  [📄 GOOG 10-Q p.50](https://agentii.ai/v/GOOG/sec156/50).

**DA-23 at GOOG, per period: the issuer is clean on every period; the instrument strips signs on
some.** The two tracks must not be collapsed — 001's "GOOG clean" remains true of Alphabet and is
false of the extraction path.

### 3.4 The mechanism, now established — and one unification

Phase 2 proposed that the corruption comes from **duplicate parents**: `Revenues` and
`CostsAndExpenses` are each defined in more than one calculation role, and the instrument resolves a
parent through the *segment-detail* role rather than the consolidated one. **This census confirms
that proposal arithmetically, on both columns:**

```
Q2 2026  Revenues computed 24,874  =  24,768 (Google Cloud revenue)      + 106 (hedging)
Q2 2025  Revenues computed 82,655  =  82,543 (Google Services revenue)  + 112 (hedging)
```

Both terms are read-verified at [📄 GOOG 10-Q p.40](https://agentii.ai/v/GOOG/sec156/40). The
instrument serves **one segment member's revenue plus hedging** as the consolidated parent's
`computed` — and the member *differs between the two periods in the same filing*.

This unifies two of the five measured instrument defects. The register has carried them separately:
"(3) `reported` is corrupted on comparatives" and "(5) `reported` can be a SEGMENT TOTAL (NVDA)". At
GOOG they are **one event**: the `reported` value for a consolidated parent is a single segment
member of that same parent, sign-stripped when the member is loss-making. Phase 2's finding is not
an unexplained corruption — **it is defect (5), at scale, compounded by DA-23.**

**What remains undetermined** and is recorded as `UNRESOLVABLE-FROM-PLATFORM`: the rule that selects
*which* member. Q2 2025 resolves to Google Cloud (2,826) while Q1 2026 and FY2024 resolve to Other
Bets (2,100 / 4,444); it is neither the smallest nor the largest member; and the FY2025 10-K's
`Revenues` computed values (24,029 / 36,358 / 34,924 for FY2025/FY2024/FY2023) are **not**
reproducible from the segment table. No client-side rule can anticipate the selection, so a GOOG
quarter carries a residual that no filings-based check closes.

### 3.5 The `status` column — not read, and the reason holds at GOOG

Per the binding instrument rule the `status` column is **not read** as evidence. GOOG confirms the
rule is precaution *and* that its consequences are visible here: the Q2 2026 10-Q returns
**11 pass / 1 warn / 25 fail**, and most of the 25 `fail`s are **false positives** in which the
`reported` value is correct and `computed` is the contaminated one. Worked examples:

| Concept | `computed` | `reported` | Filed | Verdict on `reported` |
|---|---:|---:|---:|---|
| Revenues Q2 2026 | 24,874 | **119,796** | 119,796 | **correct** — false positive |
| CostsAndExpenses Q2 2026 | 94,980 | **79,026** | 79,026 | **correct** — false positive |
| Assets | 886,860 | **921,983** | 921,983 | **correct** — false positive |
| Liabilities | 259,603 | **281,503** | 281,503 | **correct** — false positive |
| NetCashProvidedByUsedInOperatingActivities 6M 2026 | 15,959 | **84,859** | 84,859 | **correct** — false positive |

Filed comparators at [📄 GOOG 10-Q p.4](https://agentii.ai/v/GOOG/sec156/4) and
[📄 GOOG 10-Q p.5](https://agentii.ai/v/GOOG/sec156/5); the 6M operating cash flow of 84,859 also
equals Q1 2026 45,790 + Q2 2026 39,069 from
[📄 GOOG 8-K p.12](https://agentii.ai/v/GOOG/sec155/12), an exact independent tie-out.

**The FY2025 10-K is worse on this measure: 13 pass / 1 warn / 30 fail**, with `reported` wrong on
`Liabilities` (2,000 against 180,016), `StockholdersEquity` (325,084 against 415,265), `Assets`
(450,256 against 595,281) and `IncomeTaxExpenseBenefit` (44 against ~26,656). Note the two
directions of the same failure: at the 10-K it is the *balance sheet* that is badly corrupted and
the *income statement* that is mostly right; at the Q2 10-Q it is the reverse.
**A `fail` therefore carries no information about which column is wrong — the false-positive rate at
GOOG is 15 of 25 fails (60%) — and a `pass` certifies no sign.**

---

## 4. DA-24 — disposal gain inside the operating line

### 4.1 Verdict: REFUTED

**No disposal gain exists at GOOG in any period this census covers**, and the reason is structural
rather than arithmetical: the only divestiture is **unclosed**.

> "In March 2026, we entered into a definitive agreement to contribute our ownership interest in
> GFiber, a wholly owned subsidiary, into a newly formed entity. Upon closing, we expect to receive
> $1.5 billion in cash, a $2.0 billion note receivable, and a 49.99% equity interest … The
> transaction is expected to close in late 2026. GFiber meets the criteria for held for sale
> classification. **No impairment loss was recognized** upon initial classification as held for sale
> and we ceased depreciation of the related long-lived assets. The operating results of GFiber
> **remain included within the Other Bets segment** through the close of the transaction."
> — [📄 GOOG 10-Q p.29](https://agentii.ai/v/GOOG/sec156/29)

A transaction that has not closed cannot have produced a gain. Held-for-sale accounting has, if
anything, *suppressed* a loss rather than created a gain: no impairment was taken and depreciation
has stopped, so **Other Bets operating loss is understated** relative to a no-transaction
counterfactual. That is a DA-24-adjacent distortion pointing the opposite way from the register's
hypothesis.

### 4.2 Acquisitions are not disposals

Wiz (completed 11 March 2026, $29,467M, goodwill 22,705) and Intersect (completed 10 March 2026,
$5,868M, goodwill 2,174, PP&E 5,129) both went through purchase accounting with **net liabilities
assumed** of (1,538) and (221) respectively, and **no bargain-purchase gain is disclosed** on either
— [📄 GOOG 10-Q p.29](https://agentii.ai/v/GOOG/sec156/29). The $2.1B Waymo investment round noted
in the 10-K is a financing event at a portfolio company, not a disposal by Alphabet.

Realised gains on securities **do** exist, but they sit below the line where the register expects
them: "Realized net gain (loss) on marketable and non-marketable equity securities sold during the
period" is $278M for Q2 2026, inside OI&E — [📄 GOOG 10-Q p.18](https://agentii.ai/v/GOOG/sec156/18).

### 4.3 The mirror-image hazard IS present, and it is disclosed

The register asks whether a non-operating item has contaminated the operating line. At GOOG the
answer is **yes, twice — with the sign reversed** (charges, not gains):

| Item | Amount | Period | Where it lands |
|---|---:|---|---|
| PriceRunner private action | 1,500 | Q2 2026 | **G&A inside the Google Services segment** — i.e. inside operating income |
| PriceRunner interest and costs | 581 | Q2 2026 | OI&E — below the line |
| Waymo employee compensation charge | 2,100 | Q4 2025 | **R&D** — inside Other Bets operating loss |
| EC advertising-technology fine | 3,500 | Q3 2025 | charge recognised in Q3 2025 |

Sources: PriceRunner detail at [📄 GOOG 10-Q p.46](https://agentii.ai/v/GOOG/sec156/46); Waymo
charge at [📄 GOOG 10-K p.34](https://agentii.ai/v/GOOG/sec144/34); EC adtech charge at
[📄 GOOG 10-Q p.32](https://agentii.ai/v/GOOG/sec156/32).

Two consequences for the register's utility, both demonstrated:

1. **A GOOG operating-margin comparison is not like-for-like unless these are stripped.** Growth in
   the Other Bets operating loss (Q2 2026 (1,799) against Q2 2025 (1,246), a $553M widening at
   [📄 GOOG 10-Q p.50](https://agentii.ai/v/GOOG/sec156/50)) is partly the Q4 2025 Waymo charge's
   absence rather than a change in run-rate.
2. **Timing creates cliffs.** The $5.2B Android payment was made in **July 2026** against a
   previously accrued liability — [📄 GOOG 10-Q p.31](https://agentii.ai/v/GOOG/sec156/31) — so it
   does **not** touch Q2 2026 operating income but will sit in Q3 2026's cash flow. An analyst
   comparing Q2 to Q3 sees a $5.2B swing that is neither an earnings event nor a defect.

**DA-24's remedy at GOOG is therefore not "look for a disposal gain" but "look for a disclosed
non-operating charge inside the segment operating lines"** — and unlike the `reported`-column
defect, every instance here is disclosed, which makes it a lesser hazard.

---

## 5. DA-25 — issuer-defined per-unit metric not reproducible from the segment tables

### 5.1 CONFIRMED, sub-mode A: rate-only disclosure

> "The following table presents **changes in** monetization metrics for Google Search & other
> revenues (paid clicks and cost-per-click) and Google Network revenues (impressions and
> cost-per-impression), **expressed as a percentage** …"
> — [📄 GOOG 10-Q p.47](https://agentii.ai/v/GOOG/sec156/47)

| Metric | Three months | Six months |
|---|---:|---:|
| Google Search & other — paid clicks change | 13% | 13% |
| Google Search & other — cost-per-click change | 3% | 4% |
| Google Network — impressions change | (12)% | (10)% |
| Google Network — cost-per-impression change | 13% | 10% |

**No level exists anywhere.** Alphabet discloses neither a paid-clicks count nor a cost-per-click
amount, in this filing or in the 10-K. This is DA-25 in its literal form — a per-unit metric not
reproducible from the segment tables — **extended by a sub-mode the register does not yet name: the
level is not merely unallocated, it is undisclosed.** A rate-only metric cannot be contradicted by
any table, so it cannot be falsified from the corpus.

It is, however, **partially testable against the revenue line**, and this artifact runs that test:

```
Search & other:  paid clicks +13% × cost-per-click +3%  ->  implied +16.4%
                 actual  63,271 / 54,190 = +16.75%      ->  agrees to ~0.4 pt
Google Network:  impressions (12)% × cost-per-impression +13%  ->  implied −0.56%
                 actual  7,303 / 7,354 = −0.69%          ->  agrees to ~0.1 pt
```

Revenue levels at [📄 GOOG 10-Q p.47](https://agentii.ai/v/GOOG/sec156/47). The decomposition is
*consistent* to within rounding and mix — which is exactly the problem: it is consistent and
unverifiable. **Marked MODELED, not DEMONSTRATED.**

### 5.2 CONFIRMED, sub-mode B: a definition changed mid-window with no comparative restated

> "As of June 30, 2026, we had **$519.5 billion** of remaining performance obligations ("revenue
> backlog"), of which **$513.9 billion** related to Google Cloud … **In the first quarter of 2026, we
> elected to change our reporting of revenue backlog to also include contracts with an original
> expected term of one year or less.**"
> — [📄 GOOG 10-Q p.14](https://agentii.ai/v/GOOG/sec156/14)

This is a stronger DA-25 instance than the monetization metrics, on three counts:

1. **The metric is a headline number** — $519.5B, quoted in the earnings call and in the 10-K.
2. **It is not in the segment table, and its concentration is invisible there.** 98.9% of it is
   Google Cloud ($513.9B of $519.5B), a fact that appears only in this note. A reader working from
   the segment table alone cannot see either the magnitude or the concentration.
3. **Its definition changed inside the comparison window — Q1 2026 — and the prior-period figure is
   not restated.** Only the June 2026 value is given. Any "backlog growth" statement spanning Q1
   2026 is therefore a comparison across two definitions, and the size of the discontinuity is not
   disclosed.

Per the `no_single_basis_collapse` rule, both bases are reported here and the pre-change basis is
**not available in this corpus** — a `UNRESOLVABLE-FROM-PUBLIC-SOURCES` gap for any metric computed
on backlog across the boundary.

---

## 6. DA-26 — annual value mislabelled as quarterly

### 6.1 CONFIRMED, with a second instance and a read-verified identification

Phase 2 recorded that the platform's **"Q4 2025" revenue is $402,836M against a true Q4 2025 of
$113,828M — 3.54× overstated, established by subtraction**, making GOOG the third named instance
after HWM and TDG.

**This census now identifies the figure directly rather than by subtraction.** $402,836M is the
**FY2025 annual revenue**, read-verified on the face of the 10-K:

> Total revenues, year ended December 31: 2024 **$350,018** · 2025 **$402,836**
> — [📄 GOOG 10-K p.34](https://agentii.ai/v/GOOG/sec144/34)

It is corroborated by the segment table's FY2025 column summing to the same total
(342,721 + 58,705 + 1,537 − 127 = **402,836**,
[📄 GOOG 10-K p.88](https://agentii.ai/v/GOOG/sec144/88)), and by `validate_calculation` serving
402,836 as the **correct** `Revenues` for the FY2025 annual period of that same 10-K. A second
instance follows immediately: the platform's **"Q4 2024" revenue is $350,018M**, likewise the
FY2024 annual total, against a Phase-2-derived true Q4 2024 of $96,469M — **3.63× overstated**.

**The load-bearing point is that the platform's `reported` value is correct and its period label is
wrong.** DA-26 does not live in the same layer as the §3 defect: `validate_calculation` gets FY2025
revenue right; the **period-attribution layer** then files the annual value under a Q4 label.

### 6.2 The mechanism is row-wide and duration-specific

Phase 2 noted the mislabelling extends beyond revenue. The sharpening this census adds is *which*
facts in the row are affected:

| Fact type in the "Q4 2025" row | Correct? | Why |
|---|---|---|
| Duration facts — revenues, operating income, net income, R&D, EPS | **Wrong, annual** | a 12-month value in a 3-month slot |
| Instant facts — balances at period end | **Correct** | for a Dec-31 filer, the Q4-end instant **is** the FY-end instant |

So a mixed row is served in which instant facts are right and duration facts are wrong. **Ratios are
not constant across the two instances (3.54× and 3.63×), so no fixed divisor repairs it** — only a
row-level guard that tests each duration fact against its labelled period length does.

### 6.3 Corollary: the Q4 quarter is unavailable, not merely mislabelled

A query for `fiscal_period="Q4"` at GOOG returns **four facts, none of them a Q4 income-statement
fact** (a 2022 split ratio and three 2015 goodwill items). The practical consequence is that
**GOOG's Q4 periods exist in the platform only as mislabelled annual rows** — the true quarterly Q4
is not retrievable by the Q4 label at all, and must be derived by subtraction. This mirrors SPCX
§10.3. `fiscal_period="FY"`, by contrast, returns 8,243 facts: the filter is not discriminating at
either end.

---

## 7. DA-27 — fiscal labels generated from the calendar quarter

### 7.1 Method and outcome are both CONFIRMED, and this one is NOT benign

SPCX's DA-27 was confirmed on method and *benign* on outcome: its offset came from
`fiscal_year_end_month_source: default` and SPCX happens to be a Dec-31 filer, so the fabricated
calendar was accidentally right. **GOOG is the opposite case and is the first non-benign instance in
the census.**

```
get_company_fiscal_calendar(GOOG) ->
  fiscal_year_end_month          : 2
  fiscal_year_end_month_source   : "gold_companies"
  "FY2026 Q2"  ->  2025-06-01 .. 2025-08-31
  "FY2026 Q4"  ->  2025-12-01 .. 2026-02-28
  ... continuing into FY2027 Q4 -> 2026-12-01 .. 2027-02-28
```

Alphabet is a **December-31 filer** — stated on the cover of the 10-Q ("quarterly period ended
June 30, 2026", [📄 GOOG 10-Q p.1](https://agentii.ai/v/GOOG/sec156/1)) and on the face of the
10-K ("year ended December 31", [📄 GOOG 10-K p.34](https://agentii.ai/v/GOOG/sec144/34)). The
platform's quarter boundaries are therefore displaced by **two months** (Jun–Aug in place of
Apr–Jun) **and its year labels by one year** (the period containing June 2025 is labelled FY2026
Q2). It also **synthesises quarters into FY2027** from data that ends in FY2025.

Three distinct failures, in ascending order of severity:

1. **The offset is served from a database, not defaulted.** `gold_companies` is an assertion about
   Alphabet, and it is wrong. Unlike SPCX, this is not an accident that happens to be harmless — it
   is a stored incorrect value that any label-consuming query will pick up.
2. **Boundaries and labels are both wrong, in different directions.** A consumer that trusts the
   boundaries gets a two-month shift; one that trusts the label gets a one-year shift.
3. **Future quarters are fabricated.** FY2027 quarters are generated that no filing supports. This
   is the DA-27 failure mode with the greatest capacity to reach an artifact unremarked, because a
   synthesised FY2027 quarter looks exactly like a real one.

**This extends DA-27's census past n = 4 of 4 and adds its first non-benign outcome.**

---

## 8. DA-28 — IPO capital-structure discontinuity

### 8.1 Verdict: NOT APPLICABLE for the IPO test

Alphabet's IPO was August 2004 — 22 years before this artifact's `as_of`, far outside any window the
corpus covers. **No IPO-discontinuity test is possible or meaningful at GOOG.**

### 8.2 The five-for-one check: no such split exists

The task asked to verify the absence of a five-for-one and the absence of a recent split. **Both
confirmed.** The only share-conversion ratios the platform holds for GOOG are:

| Ratio | Date | Source filing |
|---:|---|---|
| **20** | 2022-02-01 and 2022-07-15 | `goog-20221231.htm` |
| 2 | 2014-04-02 | `goog-20151231.xml` |

So the last split is a **20-for-1 in 2022** (announced 1 February 2022, effective 15 July 2022),
**4.5 years before the window**, and there is **no 5-for-1 at GOOG on any date**. The 2014 event is
the creation of the Class C line — the event that produced the GOOG/GOOGL distinction in the first
place — and it is 12 years outside the window. **No share-count discontinuity from a split falls
inside the comparison window.** DA-28's *specific* hypothesis is clean at GOOG.

The cover page corroborates a stable three-class structure: Class A (GOOGL), Class C (GOOG), and the
Series A/B depositary lines GOOGM/GOOGN —
[📄 GOOG 10-Q p.1](https://agentii.ai/v/GOOG/sec156/1).

### 8.3 But a capital-structure event DOES fall inside the window — and the register misses it

Two in-window findings, neither covered by DA-28 as written:

**(a) A 2.21× share-count basis collapse inside a single payload.** The platform's highlights block
reports `common_shares_outstanding: 5,527,000,000`. The balance sheet reports 12,230 million shares
at 30 June 2026, of which **5,527 million is the Class C count alone**:

> "12,088 (Class A 5,822, Class B 837, Class C 5,429) and 12,230 (Class A 5,868, Class B 835,
> **Class C 5,527**) shares issued and outstanding"
> — [📄 GOOG 10-Q p.4](https://agentii.ai/v/GOOG/sec156/4)

The cover page independently confirms the same three-class split as of 15 July 2026 — "5,868 million
shares of Class A, 835 million of Class B, and **5,527 million of Class C**" —
[📄 GOOG 10-Q p.1](https://agentii.ai/v/GOOG/sec156/1), a second date agreeing with the balance
sheet because no issuance intervened. **Both figures are correct on their own basis.** The defect is
that one payload serves a class-scoped count under a label implying all common shares, with **no
basis label** — 12,230 / 5,527 = **2.213×**. This is precisely the `no_single_basis_collapse` hazard,
and it is a per-ticker artefact: because the ticker here is **GOOG (Class C)**, a naive "GOOG shares
outstanding" is off by 2.21× against the company's total equity, and any per-share metric built on
it is off by the inverse.

A collision makes the field more treacherous than the arithmetic alone suggests: **5,527 also
appears in the EPS table as the Q2 2025 diluted Class C share count** (5,451 basic + 76 RSUs =
5,527, [📄 GOOG 10-Q p.37](https://agentii.ai/v/GOOG/sec156/37)), a different quantity in a
different period that happens to be numerically equal to the 30 June 2026 Class C balance. A value
of 5,527 recovered from GOOG can therefore mean either of two unrelated things.

**(b) A new class of stock issued in June 2026, inside the window.** Read-verified cells from Note
11, [📄 GOOG 10-Q p.34](https://agentii.ai/v/GOOG/sec156/34):

| Event | Cells as filed |
|---|---|
| Public offering, 4 June 2026 | 29 million Class A at **$355.1982**; 29 million Class C at **$351.8018**; net proceeds **$20.5 billion** |
| Private placement, 4 June 2026 | 14 million Class A + 14 million Class C to a **Berkshire Hathaway** affiliate; net proceeds **$10.0 billion** |
| Preferred, 5 June 2026 | **385 million** Series A and B depositary shares representing **19 million** shares of **6.25%** Mandatory Convertible Preferred Stock; par $0.001; **liquidation preference $1,000 per share ($50 per depositary share)**; aggregate net proceeds **$19.0 billion** |
| Split | Series A indexed to **Class A** stock; Series B indexed to **Class C** stock |
| Conversion | automatic, on or about **15 May 2029**; Series A converts into **2.2520–2.8160** Class A shares; Series B into **2.2740–2.8420** Class C shares, **depending on the applicable market value** |

The balance sheet independently carries 19 million preferred shares at a $1,000 liquidation
preference, $18,023M — [📄 GOOG 10-Q p.4](https://agentii.ai/v/GOOG/sec156/4).

The consequence that matters for this register is on the income statement and in the EPS table.
Net income per common share moved to a **two-class method** with the preferred under the
**if-converted method** — [📄 GOOG 10-Q p.36](https://agentii.ai/v/GOOG/sec156/36) — and the actual
cells, from [📄 GOOG 10-Q p.37](https://agentii.ai/v/GOOG/sec156/37):

| Three months ended 30 June | Q2 2025 | Q2 2026 |
|---|---:|---:|
| Net income available to common stockholders (consolidated) | 28,196 | **112,107** |
| Preferred stock dividends declared and accumulated — add-back | **0** | **86** |
| Conversion of preferred stock — shares added to denominator | **0** | **16** |
| Net income (consolidated, diluted numerator) | 28,196 | **112,193** |
| Diluted EPS — Class A | $2.31 | **$9.12** |
| Diluted EPS — Class B | $2.31 | **$9.12** |
| Diluted EPS — Class C | $2.31 | **$9.11** |
| Diluted EPS — consolidated | $2.31 | **$9.11** |

**Three findings follow, none of which DA-28 as written reaches:**

**(b)(i) `NetIncomeLoss` and `NetIncomeLossAvailableToCommonStockholders` now diverge** — 112,193
against 112,107, a **$86M** preferred dividend. This is the exact concept pair whose sign-stripping
is the SPCX exhibit proving `pass` does not certify a sign. GOOG's basis surface for a DA-23 test
widened from one net-income concept to several in this quarter.

**(b)(ii) The diluted EPS basis is now class-dependent, and the platform collapses it.** Class A
diluted EPS is **$9.12**; Class C is **$9.11**. In Q2 2025 both were $2.31 — **the divergence is new
this quarter**, and it is the Series A/Series B split landing (Series B, indexed to Class C, carries
the $39M attributed to Class C). The platform serves a single undimensioned fact:

```
search_xbrl_facts(GOOG, EarningsPerShareDiluted, FY2026 Q2)
  -> 9.109999999...   dimensions: {}   source_file: goog-20260630.htm
```

One value, no class dimension, for a metric that is **$9.11 for Class C and $9.12 for Class A**.
Because the query is scoped to **GOOG (Class C)** the served value is the right one for this ticker
— but it is a **collapsed basis with no label**, which is what `no_single_basis_collapse` prohibits.
The same query returns `NetIncomeLossAvailableToCommonStockholdersBasic` = **112,107,000,000**,
which ties exactly to p.5 and p.37. **Any per-share figure built from this platform without naming
the class is off by $0.01 for Class A holders from this quarter forward.**

**(b)(iii) There is a forward capital-structure discontinuity inside a three-year horizon, and the
register has no entry for it.** The preferred converts automatically on or about **15 May 2029**
into a **price-dependent** number of shares (2.2520–2.8160× for Class A, 2.2740–2.8420× for
Class C), offset by capped call transactions entered into in connection with the issuance —
[📄 GOOG 10-Q p.34](https://agentii.ai/v/GOOG/sec156/34).
A share-count discontinuity that is *scheduled*, *quantified as a range*, and *inside the window* is
a DA-28-shaped hazard that DA-28's IPO test cannot see. This is recorded as a **third register
candidate** alongside §3.4 and §10, and it is the strongest argument that DA-28 should be
generalised from "IPO discontinuity" to "capital-structure basis discontinuity".

**Recommendation:** record (a) and (b) as DA-28 *adjacent* rather than as DA-28 instances — DA-28 as
written tests IPO discontinuity, and none of the three is a discontinuity of that kind. (b)(ii) is a
**live, measured basis collapse** and (b)(iii) is a **scheduled future one**; PIL-3 should carry
both forward.

---

## 9. Instrument observations outside the six DAs

1. **`validate_calculation` changed in scale, not in kind.** Q2 2026 10-Q: 11 pass / 1 warn / 25
   fail. FY2025 10-K: 13 pass / 1 warn / 30 fail. Q1 2026 10-Q: comparable. The defect is not
   getting better or worse across GOOG's filings — it is structural.
2. **The false-positive rate at GOOG is 15 of 25 fails (60%)**, measured by checking each failing
   `reported` value against the read-verified filing. This is lower than the 93% measured elsewhere
   in the census, so **the rate is site-dependent and must not be transferred** between issuers —
   only the existence of the defect transfers.
3. **Both columns can be contaminated simultaneously and in opposite directions.** `Revenues` Q2
   2026: `computed` 24,874 (wrong, segment member) while `reported` 119,796 (right). `Revenues` Q2
   2025: `computed` 82,655 (wrong, a different segment member) while `reported` 138 (wrong
   differently). An artifact that reads both and takes the agreement as confirmation learns nothing.
4. **`us-gaap:GrossProfit` returns zero facts at GOOG.** Gross profit must be derived. This is a
   coverage gap distinct from the `OperatingIncomeLoss` hole at MRK/BMY/WWD recorded in 001, and it
   means detector 3 is unavailable as a *served* concept at GOOG and must be reconstructed.
5. **`fiscal_period` is non-discriminating in both directions** — `Q4` returns 4 irrelevant facts,
   `FY` returns 8,243 (§6.3).
6. **No transcript figure is used in this artifact.** The Phase 2 unit error (the Q2 2026 call
   rendering consolidated revenue as "$119.8 million") was therefore not a live risk here; every
   figure above is from a filing page, and the filing column confirms the call's *billions* reading
   — so the defect is isolated to the transcript's rendering, not to the underlying data.

---

## 10. Does cross-holding contamination need its own register entry?

**YES — a new entry, distinct from DA-23 and from the unregistered DA-29 common-control candidate.
Recommendation: register it; leave the DA number to the constitution owner.**

### 10.1 The disclosure establishes the circularity beyond argument

Three pages across two filings, read-verified:

> "OI&E of $98.0 billion for the three months ended June 30, 2026 included **net gains on equity
> securities of $99.0 billion, primarily related to unrealized gains in our equity securities
> portfolio from SpaceX and a private company**."
> — [📄 GOOG 10-Q p.46](https://agentii.ai/v/GOOG/sec156/46)

> "For Q2 2026, the net effect of the gain on equity securities of $99.0 billion increased the
> provision for income tax, net income, and diluted net income per common share by **$21.9 billion,
> $77.1 billion, and $6.26**, respectively."
> — [📄 GOOG 8-K p.12](https://agentii.ai/v/GOOG/sec155/12)

Decomposed at [📄 GOOG 10-Q p.18](https://agentii.ai/v/GOOG/sec156/18): gross unrealized gain on the
measurement-alternative portfolio **$77,544M**; unrealized net gain on marketable and other equity
securities **$21,399M**; realised **$278M**; total **$99,031M** — tying to the OI&E table's
"gain (loss) on equity securities, net" at
[📄 GOOG 10-Q p.50](https://agentii.ai/v/GOOG/sec156/50). The non-marketable leg is disclosed as
"primarily … our investment in a private company" (p.18 fn 1); the marketable leg is SpaceX —
**$80.0B short-term-restricted plus $14.1B long-term-restricted = $94.1B**, classified **Level 1**
([📄 GOOG 10-Q p.15](https://agentii.ai/v/GOOG/sec156/15)).

```
$77.1B / $112,193M net income  = 68.7%   of net income from one non-cash mark
$6.26  / $9.11 diluted EPS     = 68.7%   of diluted EPS from the same mark
net margin 112,193/119,796     = 93.6%   against operating margin 40,770/119,796 = 34.0%
```

**Confirmed at 68.7%, from two independent denominators.** Any GOOG↔SPCX comparison drawn on GOOG
*net* income is circular: it is a mark on the anchor entity's own equity being used as evidence about
the anchor entity. Use **operating** income (34.0%) or revenue; never net margin.

### 10.2 Why it is a distinct entry and not an extension of anything existing

| | DA-23 | DA-29 (proposed) | Cross-holding |
|---|---|---|---|
| What is wrong | a sign was stripped | the entity boundary moved | **nothing is wrong with the number** |
| Detectable by an extraction test | yes | partly | **no — no test can see it** |
| Remedy | verify against components | re-state on one boundary | **exclude the mark from the comparison base** |
| Scope | one fact | one issuer's history | **two universe members, mutually** |

The decisive argument is the second row: **`validate_calculation` certifies the contaminated figure
with a `pass`.** `NetIncomeLoss` Q2 2026 is computed 112,193 = reported 112,193, `status: pass` —
and 68.7% of that number is a non-cash revaluation. Every remedy in the existing register is a
*verification* remedy, and verification passes here. Cross-holding contamination is therefore not a
defect in the register's sense at all: it is a **non-independence between two members of the
universe**, and it belongs on a second axis — extraction fidelity (DA-23…DA-28) versus cross-entity
contamination. Filing it as a DA without that distinction would silently imply a verification
remedy that does not exist.

### 10.3 And it is falsifier-bearing, which makes registration mandatory rather than tidy

PIL-3's `wrong_if` is `count_of_universe_issuer_quarters_with_unresolved_defect_status == 0`. If
cross-holding contamination is **not** registered, GOOG's Q2 2026 quarter cannot be marked
unresolved, and the census will report **zero** while a 68.7%-of-net-income circularity is live in
the anchor comparison. **The register's own falsifier is defeated by the omission** — which is the
strongest available argument for the entry, and the reason it is a *registration* question rather
than a *presentation* one.

### 10.4 Scope and a note against overclaiming

The entry should be written as **directional and reciprocal**: the contaminated member is the
*holder* whose earnings move with the *held* entity's valuation, and the practical rule is that any
cross-member comparison must name which side carries a mark in the other and exclude it. Whether the
register treats it as one entry or a per-pair rule is a question for the constitution owner.

**One caveat, recorded rather than resolved.** The $99.0B is not one number with one evidentiary
quality — it decomposes into two legs with different observability:

| Leg | Amount | Accounting | What backs it |
|---|---:|---|---|
| Non-marketable, measurement alternative | **77,354** | cost less impairment, adjusted for observable price changes | a **private company** (p.18 fn 1) — no quoted price |
| Marketable and other equity securities, unrealized | **21,399** | fair value, quoted prices | includes the SpaceX stake |
| Realised, sold during the period | **278** | realised | — |
| **Total** | **99,031** | | ties to the OI&E table (p.50) |

**68.7% of the effect ($77,544M of gross unrealized gain) sits in the leg with no quoted price at
all**, so the stronger half of the circularity argument does not depend on any fair-value debate.
The smaller leg is where a question exists: Alphabet classifies the restricted SpaceX shares as
**Level 1** — "quoted prices in active markets for identical assets" — while also disclosing they are
subject to sale restrictions through the third quarter of 2027
([📄 GOOG 10-Q p.15](https://agentii.ai/v/GOOG/sec156/15)). A Level 1 classification implies an
active market for identical assets; a sale-restricted holding is the case where that implication is
worth stating rather than assuming. **This artifact does not second-guess the filer's hierarchy
classification** — it is an audited disclosure and the reasoning behind it is not on the pages read
— but the tension is flagged so that a downstream artifact does not read "Level 1" as
"independently verifiable" without checking. The recommendation to register the hazard (§10.3) does
not rest on this leg.

---

## Carry-forwards

1. **Three register candidates, not one.** (a) The `reported`-column / segment-member defect — now
   mechanistically established, unified with instrument defect (5), demonstrable on both columns
   with exact arithmetic (§3.4). (b) Cross-holding contamination (§10). (c) A scheduled,
   price-dependent capital-structure discontinuity (May 2029 preferred conversion, §8.3(b)(iii))
   that DA-28's IPO framing cannot reach. Phase 2 registered (a) without a number; 002 has now
   hardened it. All three await a constitution-level numbering decision, and (c) additionally
   argues for **generalising DA-28** from "IPO discontinuity" to "capital-structure basis
   discontinuity".
2. **The `reported` defect is a *current-period* defect, not a comparative one.** Q1 2026's own
   quarter is corrupt (18.9×). Any artifact whose method assumes "the current column is safe" is
   wrong at GOOG.
3. **DA-27 is non-benign for the first time.** The offset is stored (`gold_companies`), the
   boundaries and labels are wrong in different directions, and FY2027 quarters are fabricated.
   Every other artifact in this census that consumes a platform fiscal label should be re-checked
   against this.
4. **DA-25 gained two sub-modes** — rate-only disclosure, and mid-window definition change with no
   comparative restated. The backlog case is the more serious and affects the anchor narrative
   ($513.9B of $519.5B is Cloud).
5. **The GOOG ticker is Class C only.** A 2.213× basis collapse (§8.3(a)). Any per-share or
   market-cap figure built from a "GOOG shares outstanding" field must state which class it means.
   Note the 5,527 collision: the same number is both the 30 June 2026 Class C balance and the
   Q2 2025 diluted Class C share count.
6. **`NetIncomeLoss` ≠ `NetIncomeLossAvailableToCommonStockholders` from Q2 2026** — 112,193
   against 112,107, a **$86M** preferred dividend (§8.3(b)(i)). The basis surface for a DA-23 test
   at GOOG has widened, on the exact concept pair whose sign-stripping is the SPCX exhibit.
7. **Diluted EPS is now class-dependent and the platform collapses it** — Class A $9.12, Class C
   $9.11, single undimensioned fact served (§8.3(b)(ii)). New this quarter; both classes were $2.31
   in Q2 2025. Any GOOG per-share figure must name its class from Q2 2026 forward.
8. **Phase 2's `EPS × shares` cross-check (001's §2, $9.23 × 12,122M) is inadmissible** under the
   binding instrument rule and is superseded by §1's component identity. Two independent reasons,
   neither of which is the MRCY inversion: **(i)** $9.23 is the **basic** figure while the comparable
   diluted figure is $9.11; **(ii)** the read-verified p.37 table shows **12,122M is the Q2 2025
   consolidated basic share count**, not a Q2 2026 count — Q2 2026's own basic count is **12,151M**.
   The cross-check therefore multiplied a 2026 numerator by a 2025 denominator and landed within
   0.2% of the right answer by coincidence of scale. This is exactly the failure mode the binding
   rule exists to prevent.
9. **GFiber closes late 2026** — a real disposal gain or loss will then enter the operating line for
   the first time. DA-24 must be re-run at GOOG after that close.

## Could not be verified

1. **The member-selection rule** that produces the corrupted `computed` and `reported` values. Three
   exact matches establish *that* a segment member is served; *which* member, and why it changes
   between periods of the same filing, is not derivable from any public source. Registered as
   `UNRESOLVABLE-FROM-PLATFORM`. The FY2025 10-K's `Revenues` computed values (24,029 / 36,358 /
   34,924) are **not** reproducible from the segment table at all.
2. **The FY2025 10-K's `OperatingIncomeLoss` FY2024 `computed` of −36,943** is not reproducible from
   the segment table. The `reported` value (4,444) *is* identified; the `computed` value is not.
3. **The `reported` value of 138 / 174 / 213 for `Revenues`** across three filings has no
   identified basis — it is not a segment revenue, not a revenue type, and not on the same scale as
   any line in the filings. Recorded as an unexplained residue.
4. **The pre-change basis of revenue backlog.** The Q1 2026 definition change is disclosed but the
   prior basis is not restated, so no cross-boundary backlog comparison is possible from this
   corpus. `UNRESOLVABLE-FROM-PUBLIC-SOURCES` for that specific comparison.
5. **The true Q4 2025 and Q4 2024 revenue levels are not independently re-derived here.** This
   artifact read-verifies the *identification* ($402,836M = FY2025 annual; $350,018M = FY2024
   annual) and cites Phase 2 for the subtraction-derived true Q4 figures (113,828 / 96,469) and the
   ratios (3.54× / 3.63×). Independently re-deriving them requires Q3 2025 and Q3 2024 revenue,
   which no page read for this artifact supplies.
6. **The per-class EPS figures for the six-month period are not verified.** The Q2 columns are
   read-verified at [📄 GOOG 10-Q p.37](https://agentii.ai/v/GOOG/sec156/37); the 6M 2026 columns sit
   on sec156 p.38, which was **located but not read** for this artifact. No link is given for it and
   it does not appear in `citations[]` — a page number that was not established by reading the page
   is not citable, and the platform's 6M EPS facts are consequently unverified here.
7. **The forward conversion dilution is not quantified.** §8.3(b)(iii) records that the May 2029
   conversion rate is a price-dependent range (2.2520–2.8160 Class A / 2.2740–2.8420 Class C) but
   this artifact does not compute the share count at any price. The capped call transactions are
   confirmed to exist, but their notional size and strike terms are not disclosed on the pages read
   ([📄 GOOG 10-Q p.34](https://agentii.ai/v/GOOG/sec156/34)), so their offsetting effect is not
   quantified here and the $1.0 billion cost recorded elsewhere in the filing is **not cited** —
   that page was not read.
8. **`search_unified` remains non-functional** (`INTERNAL_ERROR: invalid input syntax for type json`)
   and was not used. `search_keyword_in_source` was used and its output confirmed by
   `read_source_pages` in every case, per the two-false-positive-mode rule — and the
   `table_pages_quote_cells_not_prose` discipline was applied throughout: every page attributed
   above was opened, and where the page carries a table its **cells** are quoted rather than a
   sentence describing them. Where a page's content could not be read, the citation was **removed**
   rather than retained on a description match (two such removals were made during review).

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**; the in-body links are
> inline at the point of use, and this table is the index to them.

| Figure (as filed) | Source |
|---|---|
| Consolidated statements of income, four periods — Q2 2026: revenues 119,796; cost of revenues 45,943; R&D 18,219; S&M 8,403; G&A 6,461; total costs and expenses 79,026; income from operations 40,770; other income (expense) net 97,983; income before income taxes 138,753; provision for income taxes 26,560; net income 112,193; preferred stock dividends 86; net income available to common stockholders 112,107; basic EPS 9.23; diluted EPS 9.11. Q2 2025 comparatives 96,428 / 39,039 / 13,808 / 7,101 / 5,209 / 65,157 / 31,271 / 2,662 / 33,933 / 5,737 / 28,196 / basic 2.33 / diluted 2.31. Six-month columns 186,662 / 229,692 / 124,785 / 149,226 / 61,877 / 80,466 / 174,771 | [📄 GOOG 10-Q p.5](https://agentii.ai/v/GOOG/sec156/5) |
| Segment table — revenues Google Services 82,543 -> 94,540; Google Cloud 13,624 -> 24,768; Other Bets 373 -> 382; hedging (112) -> 106; total 96,428 -> 119,796. Operating income (loss): Google Services 33,063 -> 39,544; Google Cloud 2,826 -> 8,814; Other Bets (1,246) -> (1,799); Alphabet-level activities (3,372) -> (5,789); total income from operations 31,271 -> 40,770. Six-month columns 159,807 / 25,884 / 823 / 148 / 186,662 and 65,745 / 5,003 / (2,472) / (6,399) / 61,877 | [📄 GOOG 10-Q p.40](https://agentii.ai/v/GOOG/sec156/40) |
| Segment profitability and OI&E component table — segment operating income (loss) repeated for both three- and six-month periods; gain (loss) on equity securities, net 1,286 -> 99,031; income (loss) and impairment from equity method investments, net 419 -> (35); other 72 -> (973); other income (expense), net 2,662 -> 97,983 | [📄 GOOG 10-Q p.50](https://agentii.ai/v/GOOG/sec156/50) |
| Executive overview — consolidated revenues 96,428 -> 119,796 (+24%); cost of revenues 39,039 -> 45,943; operating expenses 26,118 -> 33,083; operating income 31,271 -> 40,770; operating margin 32% -> 34%; OI&E 2,662 -> 97,983 (+3,581%); net income available to common stockholders +298%; diluted EPS 2.31 -> 9.11 | [📄 GOOG 10-Q p.45](https://agentii.ai/v/GOOG/sec156/45) |
| Key highlights — 'OI&E of $98.0 billion for the three months ended June 30, 2026 included net gains on equity securities of $99.0 billion, primarily related to unrealized gains in our equity securities portfolio from SpaceX and a private company'; the $2.1B PriceRunner accrual of which 'principal damages of $1.5 billion were accrued in general and administrative expenses in our Google Services segment, and accrued interest and costs of $581 million was recognized in other income (expense), net'; $49.6B equity raise; $20.3B senior notes; capex $44.9B; operating cash flow $39.1B; 198,933 employees | [📄 GOOG 10-Q p.46](https://agentii.ai/v/GOOG/sec156/46) |
| Fair value hierarchy — marketable equity securities 86,049 (Level 1) + 1,014 (Level 2) = 87,063 as of June 30, 2026, footnote (1) 'Includes $80.0 billion of Space Exploration Technologies Corp. (SpaceX) shares subject to short-term restrictions on the ability to sell'; other non-current assets footnote (2) 'Includes $14.1 billion of SpaceX shares subject to long-term restrictions on the ability to sell through the third quarter of 2027'. Total $94.1B of SpaceX stock, classified Level 1 | [📄 GOOG 10-Q p.15](https://agentii.ai/v/GOOG/sec156/15) |
| Non-marketable securities roll-forward — carrying value under the measurement alternative 64,094 -> 124,259; cumulative upward adjustments 44,485 -> 85,732; total non-marketable securities 68,687 -> 131,461; footnote (1) 'our investments in non-marketable securities accounted for under the measurement alternative primarily consist of our investment in a private company'. Equity-securities gain table: gross unrealized gain on the measurement-alternative portfolio 670 -> 77,544; unrealized net gain on marketable and other equity securities 853 -> 21,399; total gain on equity securities 1,286 -> 99,031 | [📄 GOOG 10-Q p.18](https://agentii.ai/v/GOOG/sec156/18) |
| Consolidated balance sheets — total assets 595,281 -> 921,983; non-marketable securities 68,687 -> 131,461; long-term debt 46,547 -> 98,165; total liabilities 180,016 -> 281,503; total stockholders' equity 415,265 -> 640,480; 'Class A, Class B, and Class C stock and additional paid-in capital, $0.001 par value per share: 300,000 shares authorized (Class A 180,000, Class B 60,000, Class C 60,000); 12,088 (Class A 5,822, Class B 837, Class C 5,429) and 12,230 (Class A 5,868, Class B 835, Class C 5,527) shares issued and outstanding' | [📄 GOOG 10-Q p.4](https://agentii.ai/v/GOOG/sec156/4) |
| Cover page — three listed classes: Class A Common Stock (GOOGL), Class C Capital Stock (GOOG), depositary shares GOOGM and GOOGN for the 6.25% Series A/B mandatory convertible preferred; 'As of July 15, 2026, there were 5,868 million shares of Alphabet's Class A stock outstanding, 835 million shares of Alphabet's Class B stock outstanding, and 5,527 million shares of Alphabet's Class C stock outstanding' | [📄 GOOG 10-Q p.1](https://agentii.ai/v/GOOG/sec156/1) |
| Revenue backlog — 'As of June 30, 2026, we had $519.5 billion of remaining performance obligations ("revenue backlog"), of which $513.9 billion related to Google Cloud'; and the definition change: 'In the first quarter of 2026, we elected to change our reporting of revenue backlog to also include contracts with an original expected term of one year or less' | [📄 GOOG 10-Q p.14](https://agentii.ai/v/GOOG/sec156/14) |
| Monetization metrics — 'The following table presents changes in monetization metrics ... expressed as a percentage': Google Search & other paid clicks change 13% (three months) and 13% (six months); cost-per-click change 3% and 4%; Google Network impressions change (12)% and (10)%; cost-per-impression change 13% and 10%. Revenues by type: Google Search & other 54,190 -> 63,271; YouTube ads 9,796 -> 11,055; Google Network 7,354 -> 7,303; Google advertising 71,340 -> 81,629; Google subscriptions, platforms, and devices 11,203 -> 12,911; Google Services total 82,543 -> 94,540; Cloud 13,624 -> 24,768; Other Bets 373 -> 382; hedging (112) -> 106; total 96,428 -> 119,796 | [📄 GOOG 10-Q p.47](https://agentii.ai/v/GOOG/sec156/47) |
| Pending divestiture — 'In March 2026, we entered into a definitive agreement to contribute our ownership interest in GFiber, a wholly owned subsidiary, into a newly formed entity. Upon closing, we expect to receive $1.5 billion in cash, a $2.0 billion note receivable, and a 49.99% equity interest ... The transaction is expected to close in late 2026. GFiber meets the criteria for held for sale classification. No impairment loss was recognized upon initial classification as held for sale ... The operating results of GFiber remain included within the Other Bets segment through the close of the transaction.' Also Wiz ($29,467M purchase price, goodwill 22,705) and Intersect ($5,868M, goodwill 2,174, PP&E 5,129) | [📄 GOOG 10-Q p.29](https://agentii.ai/v/GOOG/sec156/29) |
| Legal matters — Android: EC fine reduced to EUR 4.1B, appeal denied July 2026, 'the EC decision is now final. In July 2026, we made a cash payment of $5.2 billion for the fine plus accrued interest'; AdSense for Search: EUR 1.5B fine annulled by the General Court in September 2024, EC appeal pending | [📄 GOOG 10-Q p.31](https://agentii.ai/v/GOOG/sec156/31) |
| Advertising technology — 'in September 2025, the EC announced its decision ... The EC decision imposed a EUR 3.0 billion fine ... We recognized a charge of $3.5 billion in the third quarter of 2025, and we placed bank guarantees in the fourth quarter of 2025 in lieu of cash payment' | [📄 GOOG 10-Q p.32](https://agentii.ai/v/GOOG/sec156/32) |
| Q2 2026 results 8-K, Exhibit 99.1 — OI&E table (interest income 1,050 -> 1,430; interest expense (261) -> (1,278); gain on equity securities 1,286 -> 99,031; other income (expense) net 2,662 -> 97,983) with footnote (1): 'For Q2 2026, the net effect of the gain on equity securities of $99.0 billion increased the provision for income tax, net income, and diluted net income per common share by $21.9 billion, $77.1 billion, and $6.26, respectively.' Free-cash-flow table by quarter: operating cash flow Q3 2025 48,414 / Q4 2025 52,402 / Q1 2026 45,790 / Q2 2026 39,069 | [📄 GOOG 8-K p.12](https://agentii.ai/v/GOOG/sec155/12) |
| FY2025 10-K, revenues by type — Google Search & other 198,084 -> 224,532; YouTube ads 36,147 -> 40,367; Google Network 30,359 -> 29,792; Google advertising 264,590 -> 294,691; subscriptions, platforms, devices 40,340 -> 48,030; Google Services total 304,930 -> 342,721; Google Cloud 43,229 -> 58,705; Other Bets 1,648 -> 1,537; hedging 211 -> (127); TOTAL REVENUES 350,018 -> 402,836. Also 'Other Bets operating loss of $7.5 billion for the year ended December 31, 2025 included a $2.1 billion employee compensation charge recognized in the fourth quarter for Waymo, primarily reflected in research and development expenses'; OI&E $29.8B including $24.1B of equity-securities gains; operating cash flow $164.7B; capex $91.4B | [📄 GOOG 10-K p.34](https://agentii.ai/v/GOOG/sec144/34) |
| FY2025 10-K segment table, three annual columns — operating income (loss): Google Services 95,858 / 121,263 / 139,404; Google Cloud 1,716 / 6,112 / 13,910; Other Bets (4,095) / (4,444) / (7,515); Alphabet-level activities (9,186) / (10,541) / (16,760); total income from operations 84,293 / 112,390 / 129,039. Revenues: 272,543 / 304,930 / 342,721; 33,088 / 43,229 / 58,705; 1,527 / 1,648 / 1,537; hedging 236 / 211 / (127); total 307,394 / 350,018 / 402,836 | [📄 GOOG 10-K p.88](https://agentii.ai/v/GOOG/sec144/88) |
| Q1 2026 consolidated statements of income — three months ended March 31: revenues 90,234 -> 109,896; cost of revenues 36,361 -> 41,271; R&D 13,556 -> 17,032; S&M 6,172 -> 7,606; G&A 3,539 -> 4,291; total costs and expenses 59,628 -> 70,200; income from operations 30,606 -> 39,696; OI&E 11,183 -> 37,716; income before income taxes 41,789 -> 77,412; provision for income taxes 7,249 -> 14,834; net income 34,540 -> 62,578; basic EPS 2.84 -> 5.17; diluted EPS 2.81 -> 5.11 | [📄 GOOG 10-Q p.5](https://agentii.ai/v/GOOG/sec149/5) |
| Note 11 Stockholders' Equity — 'On June 4, 2026, the company completed an underwritten public offering of 29 million Class A shares at a price of $355.1982 per share and 29 million Class C shares at a price of $351.8018 per share'; 'a private placement of 14 million Class A and 14 million Class C shares to an affiliate of Berkshire Hathaway Inc.'; net proceeds '$20.5 billion from the public offering and $10.0 billion from the private placement'. Mandatory convertible preferred — 'On June 5, 2026, the company issued an aggregate amount of 385 million Series A and Series B depositary shares, representing 19 million shares of 6.25% Mandatory Convertible Preferred Stock, split evenly into Series A (indexed to Class A stock) and Series B (indexed to Class C stock). Each depositary share represents a 1/20th fractional interest'; 'liquidation preference of $1,000 per share ($50 per depositary share)'; 'Aggregate net proceeds were $19.0 billion'; 'each outstanding share will automatically convert on the mandatory conversion date, which is on or about May 15, 2029. The conversion rate for each share of our Series A mandatory convertible preferred stock will be between 2.2520 and 2.8160 shares of Class A stock, and Series B ... between 2.2740 and 2.8420 shares of Class C stock, depending on the applicable market value'. Capped call transactions entered into in connection with the issuance | [📄 GOOG 10-Q p.34](https://agentii.ai/v/GOOG/sec156/34) |
| Note 12 Net Income Per Common Share — 'We compute net income per common share of Class A, Class B, and Class C stock using the two-class method'; 'The dilutive effect of mandatory convertible preferred shares is reflected in diluted earnings per common share pursuant to the if-converted method'; 'The computation of the diluted net income per common share of Class A stock assumes the conversion of Class B stock, while the diluted net income per common share of Class B stock does not assume the conversion of those shares'; 'Net income available to common stockholders is calculated by adjusting net income to deduct accumulated and declared dividends on the mandatory convertible preferred stock' | [📄 GOOG 10-Q p.36](https://agentii.ai/v/GOOG/sec156/36) |
| Note 12 EPS computation tables, three months ended June 30, 2025 and 2026. Net income available to common stockholders, consolidated: 28,196 -> 112,107 (Class A 13,536 -> 53,843; Class B 1,981 -> 7,703; Class C 12,679 -> 50,561). Diluted numerator: preferred stock dividends declared and accumulated 0 -> 86 (Class A 47, Class C 39); reallocation of undistributed earnings (88)/(11)/88 -> (700)/(91)/700; net income 28,196 -> 112,193 (Class A 15,429 -> 60,893; Class B 1,970 -> 7,612; Class C 12,767 -> 51,300). Diluted denominator: shares used in basic computation 12,122 -> 12,151 (Class A 5,819 -> 5,836; Class B 852 -> 835; Class C 5,451 -> 5,480); conversion of Class B to Class A 852 -> 835; RSUs and other contingently issuable shares 76 -> 142; conversion of preferred stock 0 -> 16 (Class A 8, Class C 8); number of shares used in per share computation 12,198 -> 12,309 (Class A 6,671 -> 6,679; Class B 852 -> 835; Class C 5,527 -> 5,630). Diluted net income per common share: CLASS A $2.31 -> $9.12; CLASS B $2.31 -> $9.12; CLASS C $2.31 -> $9.11; consolidated $2.31 -> $9.11. Basic net income per common share $2.33 -> $9.23 all classes | [📄 GOOG 10-Q p.37](https://agentii.ai/v/GOOG/sec156/37) |
