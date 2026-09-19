---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: SATS
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.5.0"
# ^ Written at 1.5.0, not grandfathered. This artifact is the A7 resolution vehicle, and A7
#   is a 1.5.0-queue amendment, so the DA-29 and DA-30 obligations are discharged here in
#   full rather than deferred to Phase 7 — §7 (DA-29) and §8 (DA-30) both carry live
#   findings, and §8's four instances are the densest DA-30 census in the phase.
assumption_pin: "2"
skill_pin: "07d26b9c738b"  # Q57 resolved 2026-09-18: re-derived from plugins/agent-plugins/agentii-equity-agent/skills/agentii/recent-quarter AND plugins/vertical-plugins/equity-research-core/skills/agentii/recent-quarter — two independent roots AGREE. Algorithm dispatch.skill_version_hash() (scripts/dispatch.py:132), validated 9/9 against the six pins tabled in theses/001-technology-baseline/reproduce.md. Recorded as a verified value, not as UNRESOLVED.
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "absolute-value sign strip on a negative stored fact — CONFIRMED and EXERCISED at SATS on four independent axes, which makes SATS the widest DA-23 census in this phase. (1) COMPONENT level: `sats:AssetImpairmentChargesAndOther` Q1 2026 is filed `(66,159)` and served `+66,159,000`. (2) OPERATING level: `OperatingIncomeLoss` is stripped in 9 of 10 read-verified periods — the only clean period is the only one whose filed value is positive. The filed calculation arc makes the identity `OperatingIncomeLoss = Revenue (+1) + CostsAndExpenses (−1)`, and it closes EXACTLY at filed signs in 10 of 10 periods. (3) PER-SHARE level: `EarningsPerShareBasic` is positive on 14 of 14 read-verified periods whose filed value is parenthesised negative — SATS inverts, the MRCY/YSS shape. (4) STATEMENT level: 12 of 12 read-verified filed-NEGATIVE cash-flow subtotals across all three sections are served positive; 8 of 8 filed-positive subtotals are untouched. `GrossProfit` returns zero facts — and here the absence is genuine (the filed statement has no gross-profit line), so the substitute detector is the filer's own filed arc. `EPS × shares` was not used and is inadmissible; §2.4 demonstrates WHY it is inadmissible on this issuer."
  - da_id: "DA-24"
    chosen_reading: "a disposal or acquisition fair-value item inside the operating subtotal — the register's ORIGIN instance, and it is INVERTED. The magnitude reproduces (operating income 16,641,875 / revenue 3,614,258 = 4.605×), but the item is not a spectrum-licence sale: it is a NON-CASH 5G-Network impairment CHARGE of $16,481,468 thousand (Wireless 16,199,344 + Broadband and Satellite Services 282,124), and the spectrum licences remain on the balance sheet at 2026-03-31 because no purchase agreement has closed. The same shape as VRT's PurgeRite contingent consideration — DA-24's structural shape with the opposite sign — now reproduces at DA-24's own founding instance. Separately, the register's 'quarterly operating-margin progression' has four of its five terms as the ABSOLUTE VALUES of losses and its fourth term as an ANNUAL figure mislabelled as Q4 (DA-26 contamination inside DA-24's own instance)."
  - da_id: "DA-25"
    chosen_reading: "issuer-defined normalised metric not reproducible from the audited segment table — REFUTED at SATS: there is no divergence. The one normalised metric in the neighbourhood, Segment Adjusted OIBDA, reconciles EXACTLY to the filed segment table at both Q1 2026 (392,847 + 166,601 + (66,159) = 493,289) and FY2025 ((17,723,146) + 1,585,549 + 17,632,011 = 1,494,414), every term a filed line item. The registered shape requires a divergence; none exists. The materiality caveat is nevertheless severe and is carried in §3: the FY2025 add-back is 91.75% impairment, so the metric is not quotable without the charge."
  - da_id: "DA-26"
    chosen_reading: "annual value carried in a fiscal_period-labelled quarterly row — CONFIRMED at SATS, and SATS is already named in the register's instance. FOUR independent twelve-month figures sit on the FY2025/Q4 metrics row (revenue 15,004,989; operating income 17,723,146; net income 14,497,180; basic EPS 50.41), every one matching the FY2025 10-K annual statement exactly. The true Q4 2025 revenue is 3,796,014; the row says 15,004,989. The same four-of-four pattern repeats at FY2024/Q4."
  - da_id: "DA-27"
    chosen_reading: "fiscal labels synthesised from the calendar quarter rather than read from the filing — NOT TESTABLE at SATS, kind = MECHANISM-POPULATION IDENTITY (A6's caution): the mechanism is 'exact for December-year-end issuers and off by one for every other fiscal year-end', and SATS IS a December-year-end issuer (`fiscal_year_end_month: 12`), so the testable population is defined by the same property that defines the mechanism and cannot falsify it. The method finding survives independently: the calendar synthesises FY2027 quarters for an issuer whose latest read filing period is 2026-03-31."
  - da_id: "DA-28"
    chosen_reading: "capital-structure discontinuity at or after listing — NOT TESTABLE at SATS, kind = GENUINE ABSENCE FROM THE SOURCE: no listing event occurs in any served period, and the registered mechanism is an IPO discontinuity. The A3 generalisation (basis discontinuity in the denominator) does have a live instance carried in §6: the per-share line runs on a COMBINED Class A and B denominator, with 58 million potentially-convertible shares excluded as anti-dilutive."
  - da_id: "DA-29"
    chosen_reading: "back-solved and opaque checks — a reconciliation that closes is not thereby a check. APPLIED, and this artifact PASSES the mechanical circularity test: every term in every identity below is a filed line item located on a cited statement page, no term is derived to fit, and no `computed` value is cited as a derivation. SATS supplies the strongest platform-side instance yet found, and it is a NEW KIND: `validate_calculation` RUNS here (33/26/41 rows across three accessions — VRT's zero-row gap does NOT reproduce) and its `reported` column carries SIGN-STRIPPED values out of the same fact store, so it returns `status: pass` on `ProfitLoss` Q3 2025 computed = reported = 12,781,348,000, `diff 0`, while the filing prints `(12,781,348)`. A validator PASS coexisting with a wrong-signed value on the very concept checked."
  - da_id: "DA-30"
    chosen_reading: "two bases on one concept, collapsed without a basis field — CONFIRMED, FOUR live instances, the densest in this phase. (1) CAPTION-vs-CONTENT on the statement face: the income statement groups its cost lines under 'Costs and Expenses (exclusive of depreciation and amortization)' and then includes a D&A line inside that group, so the tagged total 3,274,642 is D&A-INCLUSIVE while the caption asserts the opposite (exclusive basis = 3,108,041). (2) NET INCOME on two bases collapsed: consolidated (147,300) vs attributable (146,885), and the platform serves the ATTRIBUTABLE basis under the undimensioned concept `net_income_loss` while the validator's `ProfitLoss` row serves the CONSOLIDATED basis — two values for 'net income' from two platform surfaces for one period. (3) The spectrum asset on two bases in ONE table: 29,614,839 subtotal vs 34,550,802 total. (4) SEGMENT vs CONSOLIDATED: segment total 392,674 vs consolidated 392,847. The GOOG mechanism is REFUTED here: the served consolidated value is the consolidated member, not a segment member."
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger   # P11. Basis established on the face of the filings: both purchase agreements are PENDING (AT&T expected H1 2026; Spectrum Acquisition Closing expected on or about 2027-11-30), the licences remain on the balance sheet at 2026-03-31, and the 10-K states substantial doubt about going concern absent the closings. Every figure quoted in this artifact is a STANDALONE PRE-CLOSE figure. See §9 — the in-flight transaction changes what three of the quoted figures mean.
unresolvable: false
citations:
  - figure: "Q1 2026 condensed consolidated statements of operations, cells: Revenue — service 3,375,540 / 3,606,156; equipment sales and other 291,949 / 263,602; Total revenue 3,667,489 / 3,869,758. Costs and Expenses (exclusive of depreciation and amortization): cost of services 1,998,268 / 2,432,198; cost of sales - equipment and other 536,907 / 439,508; SG&A 639,025 / 597,851; depreciation and amortization 166,601 / 488,333; Impairments and other (66,159) / —. Total costs and expenses 3,274,642 / 3,957,890. Operating income (loss) 392,847 / (88,132). Total other income (expense) (561,067) / (179,136). Income (loss) before income taxes (168,220) / (267,268). Income tax (provision) benefit, net 20,920 / 63,987. Net income (loss) (147,300) / (203,281). Less: NCI (415) / (612). Net income (loss) attributable to EchoStar $ (146,885) / $ (202,669). Basic 289,014 / 286,513; diluted 289,014 / 286,513. Basic and diluted net income (loss) per share attributable to EchoStar $ (0.51) / $ (0.71)"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 11
    url: https://agentii.ai/v/SATS/sec121/11
    located_via: read_source_pages
  - figure: "Q1 2026 condensed consolidated statements of cash flows, cells: Net cash flows from operating activities 238,284 / 206,755; purchases of property and equipment (133,435) / (258,427); net cash flows from investing activities 849,095 / (1,656,719); redemption and repurchases of debt (1,787,082) / (289,383); net cash flows from financing activities (1,783,496) / (331,847); net increase (decrease) in cash (696,357) / (1,780,097); cash, end of period $ 1,485,798 / $ 2,813,707"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 13
    url: https://agentii.ai/v/SATS/sec121/13
    located_via: read_source_pages
  - figure: "Note 3 Basic and Diluted Net Income (Loss) Per Share, cells: Net income (loss) $ (147,300) / $ (203,281); Less: net income (loss) attributable to NCI, net of tax (415) / (612); Net income (loss) attributable to EchoStar - Basic (146,885) / (202,669); Net income (loss) attributable to EchoStar - Diluted $ (146,885) / $ (202,669). Weighted-average common shares outstanding - Class A and B common stock: basic 289,014 / 286,513; diluted 289,014 / 286,513. Earnings per share - Class A and B common stock: basic net income (loss) per share attributable to EchoStar $ (0.51) / $ (0.71); diluted $ (0.51) / $ (0.71). Footnote (1) verbatim: 'For the three months ended March 31, 2026 and 2025, the interest on dilutive Convertible Notes and the dilutive impact of weighted-average shares of Class A common stock were excluded from the computation of \"Diluted net income (loss) per share attributable to EchoStar\" because the effect would have been anti-dilutive as a result of the net loss attributable to EchoStar in the period. As of March 31, 2026 and 2025, our Convertible Notes may be converted into 58 million shares.'"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 25
    url: https://agentii.ai/v/SATS/sec121/25
    located_via: read_source_pages
  - figure: "Note 1 Recent Developments — AT&T License Purchase Agreement: dated August 25, 2025; agreed to sell all 3.45-3.55 GHz and 600 MHz spectrum licenses and a 99-year extension of existing Hawaii leases 'for an aggregate purchase price of $22.650 billion in cash, subject to certain potential adjustments (the \"Closing Purchase Price\")'; 'The AT&T License Purchase Agreement also extends to AT&T the right to lease certain 3.45 GHz licenses from us, which AT&T exercised, subject to a short-term spectrum manager lease, at the end of the third quarter of 2025'; 'We are not obligated to consummate the AT&T Transactions if the Closing Purchase Price, after giving effect to the aggregate amount of any such adjustments, is less than $18.6 billion (the \"Minimum Purchase Price\")'; DISH 2021 Intercompany Loan Payoff 'includes $2.844 billion due to DISH DBS as of March 31, 2026 for the DISH 2021 Intercompany Loan 2028 Tranche'"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 14
    url: https://agentii.ai/v/SATS/sec121/14
    located_via: read_source_pages
  - figure: "Note 1 — AT&T closing conditions verbatim: 'The completion of the AT&T Transactions are subject to the satisfaction or waiver of customary closing conditions, including, but not limited to, certain government approvals, including, among other things, receipt of certain consents and approvals from the FCC and the United States Department of Justice (the \"DOJ\")... The closing is expected to occur in the first half of 2026.' 11 3/4% Senior Secured Notes due November 15, 2027 'will be redeemed concurrently with the closing... As of March 31, 2026, the aggregate principal amount outstanding of our 11 3/4% Senior Secured Notes due November 15, 2027 was $3.5 billion and is secured by the 600 MHz Licenses.' SpaceX License Purchase Agreement dated September 7, 2025; 'The consideration for the Initial SpaceX Transactions payable at the Spectrum Acquisition Closing is $17 billion (the \"Total Consideration Amount\")'"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 15
    url: https://agentii.ai/v/SATS/sec121/15
    located_via: read_source_pages
  - figure: "Note 1 — SpaceX consideration structure: 'up to $8.5 billion will be paid in SpaceX's Class A Common Stock, valued at $212 per share (the \"Equity Amount\")'; 'As of March 31, 2026, the aggregate principal amount outstanding of the Seller Notes was $9.821 billion and is secured by the AWS-4 and AWS-3 Licenses'; 'The Spectrum Transfer Closing is expected to occur in the first half of 2026. The Spectrum Acquisition Closing is expected to occur on or about November 30, 2027'; Interim Debt Service 'will equal approximately $2 billion'; 'As of March 31, 2026, we have made approximately $414 million in cash interest payments on the Seller Notes, which is subject to reimbursement from SpaceX upon the Spectrum Transfer Closing'; Amended and Restated License Purchase Agreement dated November 5, 2025"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 16
    url: https://agentii.ai/v/SATS/sec121/16
    located_via: read_source_pages
  - figure: "Wireless Spectrum Licenses note, cells (in thousands, as of March 31, 2026): SpaceX Transactions AWS-4 1,928,688; H Block 1,671,506; AWS-3 2,035,433. AT&T Transactions 600 MHz 6,449,578; 3.45-3.55 GHz 7,199,380. DBS 677,409; 700 MHz 701,803; 3550-3650 MHz 912,200; AWS-3 7,793,854. Subtotal $29,614,839; Capitalized interest $10,270,436; Impairment of indefinite-lived intangible assets $(5,334,473); Total as of March 31, 2026 $34,550,802. Note (2): 'Subject to the terms of the AT&T License Purchase Agreement, at the end of the third quarter of 2025, AT&T, subject to a short-term spectrum manager lease, exercised its right to lease certain 3.45 GHz licenses from us.'"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 46
    url: https://agentii.ai/v/SATS/sec121/46
    located_via: read_source_pages
  - figure: "Q1 2026 segment table, cells: Total revenue Segment Total 3,677,394 / Eliminations (9,905) / Consolidated 3,667,489; total cost of services 1,998,253 / 15 / 1,998,268; cost of sales 537,270 / (363) / 536,907; total SG&A 648,746 / (9,721) / 639,025; Impairments and other (66,159) in Other; OIBDA 527,433 / 13,717 / 94,124 / (75,990) / Segment Total 559,284 / 164 / 559,448; total D&A 166,610 / (9) / 166,601; total costs and expenses 3,284,720 / (10,078) / 3,274,642; Operating income (loss) Pay-TV 471,567 / Wireless (35,782) / Broadband and Satellite Services 44,184 / Other (87,295) / Segment Total 392,674 / Eliminations 173 / 392,847"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 71
    url: https://agentii.ai/v/SATS/sec121/71
    located_via: read_source_pages
  - figure: "Segment Adjusted OIBDA reconciliation, cells: definition verbatim — 'Segment Adjusted OIBDA is calculated by adding back depreciation and amortization expense and impairments and other to business segments operating income (loss)'. Q1 2026: Segment operating income (loss) 471,567 / (35,782) / 44,184 / (87,295) / 173 / 392,847; D&A 166,601; OIBDA 559,448; Impairments and other (66,159); Adjusted OIBDA $527,433 / $13,717 / $94,124 / $(142,149) / $164 / $493,289. Q1 2025: segment operating income (loss) 653,430 / (93,894) / (19,195) / (628,410) / (63) / (88,132); OIBDA = Adjusted OIBDA = 729,873 / (73,707) / 85,703 / (324,481) / (17,187) / 400,201"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 108
    url: https://agentii.ai/v/SATS/sec121/108
    located_via: read_source_pages
  - figure: "Q3 2025 condensed consolidated statements of operations, cells (three months ended September 30, 2025 / 2024; nine months ended September 30, 2025 / 2024): Total revenue 3,614,258 / 3,890,984 / 11,208,975 / 11,858,578; Total costs and expenses 20,256,133 / 4,051,751 / 28,152,390 / 12,099,958; Operating income (loss) (16,641,875) / (160,767) / (16,943,415) / (241,380); Net income (loss) attributable to EchoStar $ (12,781,196) / $ (141,812) / $ (13,289,997) / $ (454,779); Basic and diluted net income (loss) per share attributable to EchoStar $ (44.37) / $ (0.52) / $ (46.25) / $ (1.67); weighted-average shares 288,051 / 271,736 / 287,362 / 271,616"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec120
    page_no: 10
    url: https://agentii.ai/v/SATS/sec120/10
    located_via: read_source_pages
  - figure: "Nine-month 2025 condensed consolidated statements of cash flows, cells: Net income (loss) (13,291,473) / (459,634); Net cash flows from operating activities 325,948 / 1,207,144; Net cash flows from investing activities (1,650,042) / (1,177,398); Net cash flows from financing activities (562,872) / 869,589; Net increase (decrease) in cash (1,883,975) / 895,877; Cash, end of period $ 2,709,829 / $ 2,807,478"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec120
    page_no: 12
    url: https://agentii.ai/v/SATS/sec120/12
    located_via: read_source_pages
  - figure: "Note 1 impairment table, cells (in thousands): Prepaids and other 391,972; Regulatory authorizations 5,409,517; Property and equipment, net 5,682,226; Operating lease assets 4,191,133; Exit and disposal costs 806,620; Impairments and other $16,481,468 — i.e. Wireless 16,199,344 + Broadband and Satellite Services 282,124"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec120
    page_no: 19
    url: https://agentii.ai/v/SATS/sec120/19
    located_via: read_source_pages
  - figure: "Q3 2025 segment table, cells: Wireless 'Impairments and other 16,199,344'; Operating income (loss) Pay-TV $549,388 / Wireless $(16,883,499) / Broadband and Satellite Services $(308,327) / Eliminations $563 / total (16,641,875)"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec120
    page_no: 75
    url: https://agentii.ai/v/SATS/sec120/75
    located_via: read_source_pages
  - figure: "MD&A segment results, cells and prose: Total operating income (loss) $ (16,641,875) / $ (160,767) / $ (16,481,108); 'Our consolidated operating loss totaled $16.642 billion for the three months ended September 30, 2025'; 'adversely impacted by \"Impairments and other\" of: (1) $16.199 billion from our Wireless segment and (2) $282 million from our Broadband and Satellite Services segment'"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec120
    page_no: 95
    url: https://agentii.ai/v/SATS/sec120/95
    located_via: read_source_pages
  - figure: "MD&A other consolidated results, cells: Operating income (loss) $ (16,641,875); Net income (loss) attributable to EchoStar $ (12,781,196); effective tax rate 24.5%"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec120
    page_no: 120
    url: https://agentii.ai/v/SATS/sec120/120
    located_via: read_source_pages
  - figure: "FY2025 consolidated statements of operations, cells (2025 / 2024 / 2023): Total revenue 15,004,989 / 15,825,516 / 17,015,598; Cost of services 9,445,223 / 10,135,622 / 9,510,427; Cost of sales - equipment and other 1,685,099 / 1,636,955 / 2,434,904; SG&A 2,380,253 / 2,426,816 / 2,989,154; Depreciation and amortization 1,585,549 / 1,930,193 / 1,597,923; Impairments and other (Note 1) 17,632,011 / — / 761,099; Total costs and expenses 32,728,135 / 16,129,586 / 17,293,507; Operating income (loss) (17,723,146) / (304,070) / (277,909); Interest income 228,733 / 116,625 / 207,374; Interest expense, net (1,521,713) / (481,622) / (90,357); Other, net 122,812 / 593,497 / (1,770,792); Total other income (expense) (1,170,168) / 228,500 / (1,653,775); Income (loss) before income taxes (18,893,314) / (75,570) / (1,931,684); Income tax (provision) benefit, net 4,386,375 / (48,945) / 296,860; Net income (loss) (14,506,939) / (124,515) / (1,634,824); Less: NCI (9,759) / (4,969) / 67,233; Net income (loss) attributable to EchoStar $ (14,497,180) / $ (119,546) / $ (1,702,057); Basic 287,589 / 274,079 / 270,842; Basic and diluted net income (loss) per share attributable to EchoStar $ (50.41) / $ (0.44) / $ (6.28)"
    ticker: SATS
    form_type: 10-K
    citation_id: sec85
    page_no: 150
    url: https://agentii.ai/v/SATS/sec85/150
    located_via: read_source_pages
  - figure: "FY2025 consolidated statements of cash flows, cells (2025 / 2024 / 2023): Net cash flows from operating activities (99,374) / 1,252,697 / 2,432,647; Net cash flows from investing activities (1,404,606) / (3,048,350) / (2,808,732); Net cash flows from financing activities (910,313) / 4,483,577 / (277,121); Effect of exchange rates 2,644 / (5,721) / 3,004; Net increase (decrease) (2,411,649) / 2,682,203 / (650,202); Cash, end of period $ 2,182,155 / $ 4,593,804 / $ 1,911,601. Investing detail: Sale of Fiber business 47,207; Purchases of property and equipment (965,730); Capitalized interest related to regulatory authorizations (676,311). Operating adjustments include 'Asset sales and other losses (gains) (100,028)' and 'Impairments and other 17,632,011'"
    ticker: SATS
    form_type: 10-K
    citation_id: sec85
    page_no: 152
    url: https://agentii.ai/v/SATS/sec85/152
    located_via: read_source_pages
  - figure: "MD&A liquidity and capital resources: 'upon the closing of the AT&T Transactions, subject to certain conditions and adjustments, we will receive $22.650 billion in cash and upon the closing of the SpaceX Transactions, subject to certain conditions, we will receive approximately $22 billion in consideration which includes $20 billion upon the Spectrum Acquisition Closing in a combination of cash and the Amended Equity Amount... and payments for the Interim Debt Service of approximately $2 billion effective with the Spectrum Transfer Closing'; 'During the year ended December 31, 2025, we recorded a total charge of $17.632 billion, $16.481 billion and $1.151 billion during the third and fourth quarters of 2025, respectively'; triggering events caused by the AT&T and SpaceX Transactions leading to abandonment and decommissioning of 5G Network portions not used in the Hybrid MNO model, recorded in the Other and Broadband and Satellite Services Segments; going-concern substantial doubt — 'funding is not deemed committed'"
    ticker: SATS
    form_type: 10-K
    citation_id: sec85
    page_no: 76
    url: https://agentii.ai/v/SATS/sec85/76
    located_via: read_source_pages
  - figure: "Amended and Restated SpaceX License Purchase Agreement: 'the transfer of up to an aggregate of 15 MHz of AWS spectrum in the frequency range of 1695-1710 MHz... in exchange for additional consideration of $2.6 billion, all of which will be paid in SpaceX's Class A Common Stock, valued at $212 per share. As a result of this change, the total consideration for the SpaceX Transactions has increased from $17 billion to approximately $20 billion, with up to $11 billion to be paid in SpaceX's Class A Common Stock, valued at $212 per share (the \"Amended Equity Amount\")'; Cash on Hand (cash and marketable securities) $2.984 billion as of December 31, 2025; $2.0 billion debt maturing July 2026, $1.377 billion August 2026, $2.750 billion December 2026; FCC required to initiate Auction 113 by June 23, 2026; maximum payment up to approximately $2.921 billion for the Northstar and SNR Re-Auction Payments"
    ticker: SATS
    form_type: 10-K
    citation_id: sec85
    page_no: 157
    url: https://agentii.ai/v/SATS/sec85/157
    located_via: read_source_pages
---

# SATS — recent-quarter methodology: the register's own DA-24 origin instance, re-tested

## Headline

**DA-24's founding instance is inverted, and its independence claim FAILS.**

The register records that at SATS *"2025 Q3 operating income was 4.6× revenue ($16.6B on $3.6B) — a spectrum-licence sale"* and that SATS exhibits *"DA-24 without DA-23 (its EPS × shares reconciles to 0.3%)"*, calling this *"the cleanest proof the two diagnoses are distinct."* Re-tested against the filings, all three parts of that record change:

1. **The magnitude reproduces; the identification does not.** Operating income of $(16,641,875) thousand on total revenue of $3,614,258 thousand is 4.605× — arithmetically exact. But the item is **not** a spectrum-licence sale. It is a **non-cash 5G-Network impairment charge of $16,481,468 thousand** ($16,199,344 Wireless + $282,124 Broadband and Satellite Services), triggered by the AT&T and SpaceX transactions. The spectrum licences **remain on the balance sheet** at 2026-03-31, at $34,550,802 thousand, because **no purchase agreement has closed**. This is DA-24's structural shape with the **opposite sign** — the same inversion this phase found at VRT, now reproducing at DA-24's own origin.
2. **The independence proof is inadmissible AND closes for the wrong reason.** The register's proof is `EPS × shares`. §2.4 shows the served product closes to 0.35% at Q1 2026 — reproducing the register's 0.3% — *because both operands carry the same sign strip*, so the residual is invariant under a global flip. The test carries zero information about the sign.
3. **The independence claim FAILS on A7's own test.** The component identity closes exactly at filed signs in 10 of 10 read-verified periods (A7's first conjunct holds), but **no spectrum-sale gain sits inside the operating stack** (the second conjunct is false — the item is an impairment charge), **and** SATS exhibits DA-23 in the same periods. "DA-24 without DA-23" is false at SATS.

**And the register's Clean row is wrong about this issuer.** The DA-23 Clean row lists SATS. SATS exhibits the sign strip on **four independent axes** — component, operating, per-share and statement level — and is the widest DA-23 census in this phase:

- **Operating level: 9 of 10** read-verified `OperatingIncomeLoss` periods are served positive where the filing prints a negative. The **one** clean period is the **only** one whose filed value is positive.
- **Statement level: 12 of 12** read-verified filed-negative cash-flow subtotals — across operating, investing **and financing** — are served positive; **8 of 8** filed-positive subtotals are untouched. Zero exceptions in either direction.
- **Per-share level: 14 of 14** read-verified `EarningsPerShareBasic` periods are served positive where the filing prints a parenthesised negative. The per-share line inverts — the MRCY/YSS shape.
- **Component level:** `sats:AssetImpairmentChargesAndOther` Q1 2026 is filed `(66,159)` and served `+66,159,000`.

**A fifth finding, platform-side and new to this phase:** `validate_calculation` **runs** at SATS (33/26/41 rows across three accessions — VRT's zero-row gap does **not** reproduce) and returns `status: pass` on a value whose sign is wrong. Its `reported` column draws from the same stripped fact store, so the validator **cannot** detect the strip by construction.

## Register version note

Written at `constitution_pin: "1.5.0"`, not grandfathered. This artifact is the vehicle for **A7** — the queued amendment recording that *"the register's own independence proof uses a tool the register itself forbids"*, dispatched to this artifact with the instruction *"do not pre-judge."* §2.5 resolves it: **the independence claim FAILS.** DA-29 (§7) and DA-30 (§8) are discharged here in full rather than deferred to Phase 7, and both yield live findings — DA-29 supplies a new failure kind, and DA-30 supplies the densest instance census in the phase (four).

`skill_pin: 07d26b9c738b` is a **verified** value, not a guess: re-derived from two independent plugin roots that agree, using `dispatch.skill_version_hash()` (`scripts/dispatch.py:132`), validated 9/9 against the six pins tabled in `001/reproduce.md`. The four `packaging/targets/*` trees were tested and fail 0/6; they are decoys and are not used.

## Inheritance from 001

**001 is frozen and is not rewritten.** 001 carries exactly **one** SATS metric row — `SATS | Spectrum gains vs operating business | ~$27B vs $15.0B FY revenue | fact` — and no SATS quarterly income statement. Its spec cites the SPCX–EchoStar transaction as the P6 reference mark at `$19.6B`. §10 tests all three figures. Result: **`$15.0B` reproduces exactly; `$19.6B` reproduces arithmetically but is DERIVED and mis-described; `~$27B` does not reproduce**, and the phrase *"spectrum gains"* is refuted — no gain has been recognised, and the operating line carries an impairment **charge**.

001's questions are not repeated here; its facts are validated, and the two corrections are recorded in §10 without touching the frozen artifact.

## Summary verdicts

| Detector | Verdict | Basis in one line |
|---|---|---|
| **DA-23** component level | **CONFIRMED — EXERCISED** | `sats:AssetImpairmentChargesAndOther` Q1 2026: filed `(66,159)`, served `+66,159,000` |
| **DA-23** operating level | **CONFIRMED — EXERCISED** | 9 of 10 periods stripped; the 1 clean period is the only filed-positive one; identity closes exactly, 10 of 10 |
| **DA-23** per-share level | **CONFIRMED — EXERCISED** | 14 of 14 inverts (MRCY/YSS shape) |
| **DA-23** statement level | **CONFIRMED — EXERCISED** | 12 of 12 filed-negative subtotals (all 3 sections) stripped; 8 of 8 filed-positive clean |
| **DA-23** primary detector (`gross-profit` bound) | **NOT TESTABLE — GENUINE ABSENCE** | no gross-profit line is filed; confirmed by reading the statement face, **not** inferred from the zero-fact return |
| **DA-24** instance | **REFUTED as recorded / CONFIRMED INVERTED** | $16.6B is a non-cash impairment **charge**, not a licence sale; magnitude 4.605× reproduces |
| **DA-24** independence ("without DA-23") | **FAILS** | A7's test: identity closes, but no sale gain is in the stack **and** DA-23 is present in the same periods |
| **DA-25** | **REFUTED** | the one normalised metric reconciles **exactly** to the filed segment table; no divergence exists |
| **DA-26** | **CONFIRMED** | 4 of 4 twelve-month figures on the FY2025/Q4 row; true Q4 revenue 3,796,014 vs row's 15,004,989 |
| **DA-27** | **NOT TESTABLE — MECHANISM-POPULATION IDENTITY** | December-year-end issuer; the sample is defined by the mechanism's own property (A6) |
| **DA-28** | **NOT TESTABLE — GENUINE ABSENCE** | no listing event in any served period |
| **DA-29** | **APPLIED — self-clean; validator supplies a new failure kind** | `pass` returned on a stripped value |
| **DA-30** | **CONFIRMED — four live instances** | caption-vs-content; net income; the spectrum asset; segment-vs-consolidated |
| **GOOG mechanism** (segment member served as consolidated) | **REFUTED** | served value is the consolidated member (392,847), not Pay Segment (471,567) |
| **DA-32 / A2** (1000× scale) | **NOT CONFIRMED** | four share counts match the statement faces |

---

## 1. DA-23 — the sign strip, four independent axes

### 1.1 Detector availability: name which axis is open, and why

Detector availability is **two axes**, and at SATS they resolve in opposite directions:

- **Axis (a) — is a gross-profit line filed? NO.** `search_xbrl_facts(ticker=SATS, concept=GrossProfit)` returns `{"data":[],"total_count":0}`. **A zero-fact return is evidence about the CONCEPT NAME, not about the ISSUER** — so the zero return alone would not settle it. It is settled by reading the statement face: the Q1 2026 statement of operations runs *Total revenue → Costs and Expenses → Total costs and expenses → Operating income (loss)*, with `Cost of services` and `Cost of sales - equipment and other` as the first two cost lines and **no gross-profit line anywhere** ([SATS 10-Q p.11](https://agentii.ai/v/SATS/sec121/11)); the FY2025 statement is the same shape ([SATS 10-K p.150](https://agentii.ai/v/SATS/sec85/150)). So this is **GENUINE ABSENCE FROM THE SOURCE**, established by reading, not by the zero return. The primary DA-23 detector (gross-profit bound) cannot run.
- **Axis (b) — is `OperatingIncomeLoss` a filed first-class consolidated subtotal? YES.** 35 served facts, and the filed calculation linkbase carries the arc explicitly: `OperatingIncomeLoss ← RevenueFromContractWithCustomerExcludingAssessedTax (+1)` and `OperatingIncomeLoss ← CostsAndExpenses (−1)` (role `...StatementCondensedConsolidatedStatementsOfOperationsAndComprehensiveIncomeLoss`, `get_calculation_tree(sec121)` and `(sec120)`).

So the admissible substitute for the gross-profit bound is **the filer's own filed arc** — not an invented identity. Where the finer decomposition is available it is shown in full, at line-item granularity.

### 1.2 The component identity, in-line, at filed signs — 10 of 10 close exactly

**Q1 2026** ([p.11](https://agentii.ai/v/SATS/sec121/11)), via the gross-profit surrogate at line-item granularity:

- gross-profit surrogate = Total revenue 3,667,489 − Cost of services 1,998,268 − Cost of sales - equipment and other 536,907 = **1,132,314**
- opex = SG&A 639,025 + D&A 166,601 + Impairments and other **(66,159)** = **739,467**
- 1,132,314 − 739,467 = **392,847** = filed Operating income (loss) **392,847** → **exact**

**FY2025** ([p.150](https://agentii.ai/v/SATS/sec85/150)):

- gross-profit surrogate = 15,004,989 − 9,445,223 − 1,685,099 = **3,874,667**
- opex = 2,380,253 + 1,585,549 + 17,632,011 = **21,597,813**
- 3,874,667 − 21,597,813 = **(17,723,146)** = filed Operating income (loss) **(17,723,146)** → **exact**

**Via the two-term filed arc** (`Total revenue − Total costs and expenses`), all remaining read-verified periods:

| Period | Total revenue | Total costs and expenses | Identity | Filed OI | |
|---|---|---|---|---|---|
| Q1 2026 | 3,667,489 | 3,274,642 | **392,847** | 392,847 | exact |
| Q1 2025 | 3,869,758 | 3,957,890 | **(88,132)** | (88,132) | exact |
| Q3 2025 | 3,614,258 | 20,256,133 | **(16,641,875)** | (16,641,875) | exact |
| 9M 2025 | 11,208,975 | 28,152,390 | **(16,943,415)** | (16,943,415) | exact |
| FY2025 | 15,004,989 | 32,728,135 | **(17,723,146)** | (17,723,146) | exact |
| Q3 2024 | 3,890,984 | 4,051,751 | **(160,767)** | (160,767) | exact |
| 9M 2024 | 11,858,578 | 12,099,958 | **(241,380)** | (241,380) | exact |
| FY2024 | 15,825,516 | 16,129,586 | **(304,070)** | (304,070) | exact |
| FY2023 | 17,015,598 | 17,293,507 | **(277,909)** | (277,909) | exact |

Cells from [p.11](https://agentii.ai/v/SATS/sec121/11), [p.10](https://agentii.ai/v/SATS/sec120/10) and [p.150](https://agentii.ai/v/SATS/sec85/150). **10 of 10 exact. The identity is not the problem. The store is.**

Q2 2025 is available by difference from two read-verified filed figures: filed 9M 2025 (16,943,415) − filed Q3 2025 (16,641,875) = filed 6M 2025 **(301,540)**; less filed Q1 2025 (88,132) = filed Q2 2025 **(213,408)**. Both derived terms are filed figures on cited pages.

### 1.3 The strip, and the `diff = 2 × value` signature

Comparing the served store against the filed pages, using the filed arc as the sign-forcing identity:

| Period | Identity at filed signs | Served `OperatingIncomeLoss` | Disposition |
|---|---|---|---|
| Q1 2026 | +392,847 | +392,847,000 | **CLEAN** |
| Q1 2025 | −88,132 | +88,132,000 | **STRIPPED** |
| Q2 2025 | −213,408 | +213,408,000 | **STRIPPED** |
| Q3 2025 | −16,641,875 | +16,641,875,000 | **STRIPPED** |
| 9M 2025 | −16,943,415 | +16,943,415,000 | **STRIPPED** |
| FY2025 | −17,723,146 | +17,723,146,000 | **STRIPPED** |
| Q3 2024 | −160,767 | +160,767,000 | **STRIPPED** |
| 9M 2024 | −241,380 | +241,380,000 | **STRIPPED** |
| FY2024 | −304,070 | +304,070,000 | **STRIPPED** |
| FY2023 | −277,909 | +277,909,000 | **STRIPPED** |

**9 of 10 stripped. The single clean period is the single filed-positive one.** Every served fact is positive — all 35 `OperatingIncomeLoss` facts in the SATS series are non-negative, which is itself the tell.

**The `diff = 2 × value` signature is exact**, and the residual identifies *which term* was stripped rather than merely *that* something was. At FY2025, the served pair (revenue 15,004,989, costs 32,728,135) has residual `served_OI − (revenue − costs)` = 17,723,146 − (15,004,989 − 32,728,135) = **35,446,292 = 2 × 17,723,146**. Had `Revenue` been the stripped term the residual would be −30,009,978; had `CostsAndExpenses` been stripped, −65,456,270. Only stripping **`OperatingIncomeLoss` itself** produces 2 × 17,723,146. The same signature holds on the cash-flow subtotals (FY2025 financing: filed (910,313), served +910,313, `diff` 1,820,626 = 2 × 910,313).

### 1.4 Statement level: the discriminator is the SIGN, and it is not confined to the income statement

The task's requirement is a census at **statement** level, not income-statement level. Twenty read-verified cells across all three cash-flow subtotals, every one compared to the printed statement:

| Subtotals | Filed negative → **STRIPPED** | Filed positive → **CLEAN** |
|---|---|---|
| **Operating** | FY2025 (99,374) → +99,374 | Q1 2026 +238,284 · Q1 2025 +206,755 · 9M 2024 +1,207,144 · 9M 2025 +325,948 · FY2024 +1,252,697 |
| **Investing** | Q1 2025 (1,656,719) · 9M 2024 (1,177,398) · 9M 2025 (1,650,042) · FY2024 (3,048,350) · FY2025 (1,404,606) · FY2023 (2,808,732) | Q1 2026 +849,095 |
| **Financing** | Q1 2026 (1,783,496) · Q1 2025 (331,847) · 9M 2025 (562,872) · FY2025 (910,313) · FY2023 (277,121) | 9M 2024 +869,589 · FY2024 +4,483,577 |

Cells from [p.13](https://agentii.ai/v/SATS/sec121/13), [p.12](https://agentii.ai/v/SATS/sec120/12) and [p.152](https://agentii.ai/v/SATS/sec85/152).

**12 of 12 filed-negative subtotals stripped. 8 of 8 filed-positive subtotals untouched. Zero exceptions in either direction.** The `|x|` stripping reaches **every statement**, not just the income statement — the same shape A6 recorded at BWXT and this phase found at VRT, here read-verified at cell level on all three subtotals. Unlike VRT, this is **EXERCISED, not UNEXERCISED**: the filed-negative cases exist and the detector caught them.

### 1.5 Per-share level: the line inverts — MRCY/YSS shape, CONFIRMED

`EarningsPerShareBasic` is served **positive on 14 of 14** read-verified periods whose filed value is a parenthesised negative:

| Period | Filed | Served |
|---|---|---|
| Q1 2026 | $ (0.51) | +0.51 |
| Q1 2025 | $ (0.71) | +0.71 |
| Q2 2025 | $ (1.06) | +1.06 |
| Q3 2025 | $ (44.37) | +44.37 |
| 9M 2025 | $ (46.25) | +46.25 |
| FY2025 | $ (50.41) | +50.41 |
| Q3 2024 | $ (0.52) | +0.52 |
| 9M 2024 | $ (1.67) | +1.67 |
| FY2024 | $ (0.44) | +0.44 |
| FY2023 | $ (6.28) | +6.28 |

Filed cells on [p.25](https://agentii.ai/v/SATS/sec121/25), [p.10](https://agentii.ai/v/SATS/sec120/10) and [p.150](https://agentii.ai/v/SATS/sec85/150) (plus the corresponding interim statements). The same strip takes `NetIncomeLoss`: Q1 2026 net loss attributable to EchoStar of $(146,885) thousand is served as `net_income_loss` **+146,885,000**; FY2025 $(14,497,180) → +14,497,180,000.

**A locating detail worth recording:** the non-numeric table-text fact `ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock` **retains the correct parenthesised negatives** (e.g. `$(0.51)$(0.71)`; `$(50.41)$(0.44)$(6.28)`). The strip is therefore in the **numeric fact extraction**, not in the document text — a precise localisation of the defect.

### 1.6 Component level — the BWXT analogue, and the concept-name trap

`us-gaap:AssetImpairmentCharges` returns only **6 facts** at SATS (FY2023 761,099,000; 9M/6M/Q1 2023 all 3,142,000; FY2022 711,000; FY2021 null) — **none of which is the $16.481B or $17.632B impairment.** The 2025 charge is tagged with a **filer extension concept**, `sats:AssetImpairmentChargesAndOther`, and that tag returns 5 facts, all read-reconciled to the statement faces:

| Period | Filed | Served | Disposition |
|---|---|---|---|
| Q1 2026 | **(66,159)** — a credit, printed in parentheses | +66,159,000 | **STRIPPED** |
| Q3 2025 | 16,481,468 | +16,481,468,000 | CLEAN |
| 9M 2025 | 16,481,468 | +16,481,468,000 | CLEAN |
| FY2025 | 17,632,011 | +17,632,011,000 | CLEAN |
| FY2023 | 761,099 | +761,099,000 | CLEAN |

**5 of 5 consistent with the sign rule: the one filed-negative member is stripped; the four filed-positive members are not.** Two conclusions:

1. **The component-level DA-23 detector is EXERCISED at SATS — CONFIRMED** — where at VRT's operating line it was UNEXERCISED.
2. **The Q1 2026 strip is forced by the issuer's own arithmetic, not merely by reading the parentheses.** The Segment Adjusted OIBDA reconciliation ([p.108](https://agentii.ai/v/SATS/sec121/108)) bridges OIBDA 559,448 to Adjusted OIBDA 493,289 by exactly one term, "Impairments and other", printed as **(66,159)**. 559,448 − 66,159 = 493,289; with +66,159 the bridge would give 625,607, which appears nowhere. **The reconciliation only closes if the term is negative** — so the served `+66,159,000` is demonstrably wrong independently of how the parentheses are read.
3. **The `us-gaap:AssetImpairmentCharges` zero-relevance is an INGESTION-ABSENCE kind, not genuine absence.** The line exists in the filing; it is tagged as an extension. A concept-keyed query therefore cannot see it. This is the same family as the `GrossProfit` / plain-`Revenues` name traps, and it is distinct from §1.1's genuine absence: **there the line does not exist; here it exists and is tagged under a name the query does not know.**

---

## 2. DA-24 — the register's origin instance, re-tested

### 2.1 What the register records

> *"EchoStar (SATS) 2025 Q3 operating income was **4.6× revenue** ($16.6B on $3.6B) — a spectrum-licence sale. Quarterly operating-margin progression 2.3% → 5.7% → 460.5% → 118.1% → 10.7% makes the event unmistakable."*

### 2.2 The magnitude reproduces; the identification is inverted

The ratio is exact: 16,641,875 / 3,614,258 = **4.605×**. But the item is the opposite of a sale:

- **It is a charge.** "Impairments and other" of **$16,481,468 thousand** ([p.19](https://agentii.ai/v/SATS/sec120/19)), disaggregated as Wireless **16,199,344** + Broadband and Satellite Services **282,124** ([p.75](https://agentii.ai/v/SATS/sec120/75)), and stated in the MD&A in prose: *"Our consolidated operating loss totaled $16.642 billion for the three months ended September 30, 2025"*, *"adversely impacted by 'Impairments and other' of: (1) $16.199 billion from our Wireless segment and (2) $282 million from our Broadband and Satellite Services segment"* ([p.95](https://agentii.ai/v/SATS/sec120/95)). It sits **inside** the operating stack — it is a component of `Total costs and expenses`, and §1.2's identity only closes when it is inside.
- **It is non-cash and transaction-triggered.** The 10-K states verbatim that the AT&T and SpaceX Transactions were **triggering events**: *"we began the abandonment and decommission process for certain portions of our 5G Network that will not be utilized in our Hybrid MNO business"*, and *"During the year ended December 31, 2025, we recorded a total charge of $17.632 billion, $16.481 billion and $1.151 billion during the third and fourth quarters of 2025, respectively, for non-cash asset impairments and other expenses in 'Impairments and other'"* ([p.76](https://agentii.ai/v/SATS/sec85/76)).
- **No sale has been recognised, because no sale has closed.** The spectrum licences remain on the balance sheet at 2026-03-31: **$29,614,839** thousand at cost, **$34,550,802** thousand after capitalised interest and accumulated impairment, and the AT&T-Transaction licences are still listed as the company's own (600 MHz $6,449,578; 3.45–3.55 GHz $7,199,380) ([p.46](https://agentii.ai/v/SATS/sec121/46)). All AT&T took at the end of Q3 2025 was a **short-term spectrum manager lease** ([p.14](https://agentii.ai/v/SATS/sec121/14), note (2) on [p.46](https://agentii.ai/v/SATS/sec121/46)) — which is why the licences stay on the balance sheet at all. Both agreements remained pending FCC and DOJ approval ([p.15](https://agentii.ai/v/SATS/sec121/15)).
- **The FY2025 cash-flow statement records no disposal gain.** The only reconciling item in that neighbourhood is `Asset sales and other losses (gains) (100,028)` — against `Impairments and other 17,632,011` ([p.152](https://agentii.ai/v/SATS/sec85/152)).

**Verdict: DA-24's registered SATS instance is REFUTED as recorded.** DA-24's *shape* — an item of non-operating magnitude sitting inside the operating subtotal — is present and confirmed; the *identification* as a spectrum-licence sale is inverted in sign. This is the second occurrence in this phase of DA-24's shape with the opposite sign (VRT's PurgeRite contingent consideration, a $62.0M charge, was the first), and here it occurs **at DA-24's own founding instance**.

### 2.3 The register's margin progression: 4 of 5 terms are absolute values of losses, and one is an annual figure

The progression reproduces arithmetically from the served store — but decomposed, it is not a progression of margins:

| Register term | Quotient | Filed value of the period | Correct figure |
|---|---|---|---|
| 2.3% | 88,132 / 3,869,758 = 2.28% | OI **(88,132)** | **(2.28)%** |
| 5.7% | 213,408 / 3,724,959 = 5.73% | OI **(213,408)** (by difference, §1.2) | **(5.73)%** |
| 460.5% | 16,641,875 / 3,614,258 = 460.46% | OI **(16,641,875)** | **(460.46)%** |
| 118.1% | 17,723,146 / 15,004,989 = 118.11% | **both terms are ANNUAL figures** (FY2025) | **(20.54)% for the true Q4 2025** |
| 10.7% | 392,847 / 3,667,489 = 10.71% | OI **+392,847** | **+10.71%** ✓ |

Two independent defects:

- **Signs.** Four of the five terms are the absolute values of **losses**. Only the last term is a true positive margin — and it is the only term whose filed value is positive.
- **DA-26 contamination inside DA-24's own instance.** The 118.1% term is `FY2025 annual operating income ÷ FY2025 annual revenue` — four twelve-month figures sitting on a row labelled Q4 (see §4). **Q4 2025 is therefore absent from the register's progression entirely.** The true Q4 2025 figures, by difference from read-verified filed cells: OI (17,723,146) − (16,943,415) = **(779,731)**; revenue 15,004,989 − 11,208,975 = **3,796,014**; margin **−20.54%**.

**The correct filed progression for the five quarters is: (2.28)% → (5.73)% → (460.46)% → (20.54)% → +10.71%.** The register's version reads as a rise (2.3 → 5.7 → 460.5). The filed version is a collapse into a catastrophic loss, a partial recovery to a still-large loss, then a return to modest positive margin. The register's own framing — *"makes the event unmistakable"* — is right for the wrong reason: the event is unmistakable, but what it shows is a **charge**, not a sale.

### 2.4 Why `EPS × shares` is inadmissible — demonstrated, not asserted

The register's independence proof is that SATS's "EPS × shares reconciles to 0.3%". The products do reconcile — and the mechanism is now visible:

| Period | Served EPS | × served shares | Served net income | Deviation |
|---|---|---|---|---|
| Q1 2026 | 0.51 | 289,014 | 147,397 | 146,885 | **0.35%** |
| FY2025 | 50.41 | 287,589 | 14,497,361 | 14,497,180 | 0.0012% |
| Q3 2025 | 44.37 | 288,051 | 12,780,822 | 12,781,196 | 0.0029% |
| 9M 2025 | 46.25 | 287,362 | 13,290,492 | 13,289,997 | 0.0037% |
| Q3 2024 | 0.52 | 271,736 | 141,303 | 141,812 | 0.36% |

The first row **reproduces the register's 0.3% exactly**. And every one of those five rows is a period on which **both operands carry the same sign strip** — the EPS is served positive where the filing prints `(0.51)`, and the net income is served positive where the filing prints `(146,885)`.

**This is why the test cannot work, in one line: the residual is `|EPS| × shares − |NI|`, which is invariant under a global sign flip.** The test is not merely weak here; it is **arithmetically blind to the exact defect it was used to rule out**. Filed: (0.51) × 289,014 = (147,397) against filed (146,885) — the same 0.35% gap, unchanged. The reconciliation closes **because** both sides are corrupted identically, and it would close identically whether the strip were present or absent. There is no admissible reading on which it carries information about the sign.

This is a stronger refutation than RKLB/FLY/VOYG supplied (where the test "passes on both sides of a flip"), because SATS shows the mechanism: **the instrument's two operands are drawn from the same stripped store, so their product is a sign-invariant.** DA-23's own justification gains its missing mechanism. And it is precisely why the contract lists `EPS × shares` as inadmissible for the `data_integrity_register_applied` rule.

### 2.5 A7 resolution — the independence claim FAILS

A7 specified the admissible test and both branches. Applied literally:

| A7's condition | Result at SATS |
|---|---|
| "If SATS's component identity **closes to its filed operating income**" | **HOLDS — 10 of 10 exact** (§1.2) |
| "while **a spectrum-sale gain sits inside the operating stack**" | **FALSE — the item inside the stack is an impairment CHARGE of $16,481,468 thousand; no sale gain exists because nothing has closed** |
| "**the independence claim is restored**" | **not reached — the conjunction fails** |
| "If it does not close, **the claim fails**" | the identity closes, so this branch is not the operative one — but the second conjunct fails independently, and DA-23 is present in the same periods |

**Resolution: the independence claim FAILS.** SATS does **not** exhibit DA-24 without DA-23. It exhibits **both, in the same periods**: the strip is present on 9 of 10 operating periods, on the Q1 2026 impairment component, on 14 of 14 per-share periods and on 12 of 12 filed-negative cash-flow subtotals, while the DA-24-shaped item sits in the operating stack of Q3 2025 and FY2025 as a charge.

The register's sentence *"This is the cleanest proof the two diagnoses are distinct"* is therefore **false as written for SATS**, on two independent grounds: the proof uses a forbidden test, and the test's target — DA-24-without-DA-23 — does not hold at the instance chosen to demonstrate it. **Carry-forward C1.** The remedy is not to delete DA-24's independence claim but to re-designate a different instance as its proof, or to restate DA-24's independence as unproven. That re-designation is a register edit and is not made here.

---

## 3. DA-25 — REFUTED (no divergence), with a severe materiality caveat

DA-25's registered shape is an issuer-defined normalised per-unit metric that **diverges** from the audited segment table (RKLB: `revenue per launch` implying 51.6% launch gross margin against a 42.9% audited figure). At SATS the metric exists and **does not diverge**:

- The definition is filed verbatim: *"Segment Adjusted OIBDA is calculated by adding back depreciation and amortization expense **and impairments and other** to business segments operating income (loss)"* ([p.108](https://agentii.ai/v/SATS/sec121/108)).
- **Q1 2026 closes exactly:** segment operating income 392,847 + D&A 166,601 + impairments and other (66,159) = **493,289** = the filed consolidated Adjusted OIBDA. Per segment: Pay-TV 471,567 + 55,866 = 527,433 ✓; Other (87,295) + 11,305 + (66,159) = (142,149) ✓.
- **FY2025 closes exactly:** (17,723,146) + 1,585,549 + 17,632,011 = **1,494,414** — the 10-K's "$1.49 billion". Every term filed ([p.150](https://agentii.ai/v/SATS/sec85/150)).

**Verdict: REFUTED — the registered shape requires a divergence and none exists.** This is a REFUTED, not an UNEXERCISED: the detector ran, found the normalised metric, and reconciled it term by term.

**The caveat, which is material and is why the row is not closed as a clean pass:** the metric is dominated by the very charge at issue. At FY2025 the impairment add-back is **17,632,011 / 19,217,560 = 91.75%** of total add-backs. At Q1 2026 the impairment is the **only** adjustment between OIBDA (559,448) and Adjusted OIBDA (493,289) — 100% of that bridge — and it is a **credit**, not a charge, so in that quarter the normalisation moves profit **down**, not up. Adjusted OIBDA at SATS is therefore not a measure of operating performance; it is a measure of operating performance **with the transaction-triggered impairment removed**. Any artifact quoting it must quote the impairment alongside it, per `no_single_basis_collapse`.

---

## 4. DA-26 — CONFIRMED (SATS is already named in the register)

The metrics block's **FY2025/Q4** row carries four independent twelve-month figures, each matching the FY2025 10-K annual statement **exactly**:

| Metrics row FY2025/Q4 | Value | FY2025 annual, filed | Match |
|---|---|---|---|
| revenues | 15,004,989,000 | Total revenue **15,004,989** ([p.150](https://agentii.ai/v/SATS/sec85/150)) | exact |
| operating_income | 17,723,146,000 | Operating income (loss) **(17,723,146)** | exact |
| net_income_loss | 14,497,180,000 | attributable to EchoStar **$(14,497,180)** | exact |
| eps | 50.41 | basic EPS **$ (50.41)** | exact |

**4 of 4 are annual figures on a quarterly-labelled row.** The same 4-of-4 pattern repeats on the FY2024/Q4 row (revenue 15,825,516; OI 304,070; EPS 0.44 — all FY2024 annuals). The true Q4 2025 revenue is **3,796,014**, not 15,004,989; the true Q4 2025 operating income is **(779,731)**, not 17,723,146.

SATS is already named in the register's DA-26 instance, so this is a **reproduction, not a new finding** — but it has a consequence the register does not draw: **DA-26 contaminates DA-24's own founding instance** (§2.3). The register's progression uses the mislabelled annual row as its fourth quarterly term, so the register's DA-24 exhibit is *itself* a DA-26 exhibit. Two diagnoses are not merely coexisting at SATS; one is the medium through which the other was recorded.

---

## 5. DA-27 — NOT TESTABLE, and the kind is MECHANISM-POPULATION IDENTITY

DA-27's mechanism is calendar-quarter bucketing, *"exact for December-year-end issuers and off by one for every other fiscal year-end."* SATS is a **December-year-end issuer** — `fiscal_year_end_month: 12`, sourced from `gold_companies` (not defaulted). The testable population for "off by one" is therefore the complement of SATS's own class, and **SATS cannot falsify the mechanism on any period**: a calendar-synthesised label and a filing-read label are identical for every period by construction.

**Kind named: MECHANISM-POPULATION IDENTITY** — A6's caution (*"a defect whose mechanism is defined by the property that also defines the sample cannot be censused by that sample"*), applied to the issuer rather than to the sample. This is a distinct third kind, not one of the three the task enumerates (ingestion absence / genuine absence / validator-completeness), and it is recorded as such.

The independent method finding survives and is not weakened by the untestability: the platform's calendar synthesises **FY2027** periods for an issuer whose latest read filing period is **2026-03-31** (10-Q filed 2026-05-11). SATS therefore contributes to the method finding while contributing nothing to the mechanism census. **Carry-forward C4.**

---

## 6. DA-28 — NOT TESTABLE (genuine absence), plus a live A3 instance

DA-28's registered mechanism is a **capital-structure discontinuity at or after listing** (HAWK's four share counts; the EPS bridge failing 72%). At SATS:

- **No listing event occurs in any served period.** The served series runs FY2019–Q1 2026; the registered mechanism is an IPO discontinuity. **Kind: GENUINE ABSENCE FROM THE SOURCE** — the event is not in the corpus because it is not in the periods, not because ingestion dropped it (contrast §9's ingestion-absence finding, which is a different kind with a different remedy).
- **Control on the unit:** four share counts read against the statement faces match exactly — Q1 2026 289,014 ([p.11](https://agentii.ai/v/SATS/sec121/11), [p.25](https://agentii.ai/v/SATS/sec121/25)); Q1 2025 286,513; FY2025 287,589 ([p.150](https://agentii.ai/v/SATS/sec85/150)); Q3 2025 288,051 ([p.10](https://agentii.ai/v/SATS/sec120/10)). **DA-32 (A2's 1000× scale error) is NOT CONFIRMED** — there is no scale defect in the share counts.

**A3's generalisation does have a live instance here**, carried rather than closed: SATS's per-share line runs on a **combined denominator** — "Weighted-average common shares outstanding - **Class A and B common stock**" ([p.25](https://agentii.ai/v/SATS/sec121/25); [p.11](https://agentii.ai/v/SATS/sec121/11)) — so a Class-A-only reading of the denominator is available and wrong, and the filing's own labels do not distinguish the two classes' separate share counts on the face. Additionally **58 million potentially-convertible shares** were excluded as anti-dilutive at both Q1 2026 and Q1 2025 (*"our Convertible Notes may be converted into 58 million shares"*, note (1) on [p.25](https://agentii.ai/v/SATS/sec121/25)) — a denominator basis that is period-dependent in a way the label does not show. **Carry-forward C5.**

---

## 7. DA-29 — applied; self-clean, and the platform supplies a new failure kind

### 7.1 The mechanical circularity test on this artifact: PASSES

Every term in every reconciliation in §1–§4 is a filed line item on a cited page, and none is fitted:

`Total revenue`, `Cost of services`, `Cost of sales - equipment and other`, `Selling, general and administrative expenses`, `Depreciation and amortization`, `Impairments and other`, `Total costs and expenses`, `Operating income (loss)` ([p.11](https://agentii.ai/v/SATS/sec121/11), [p.150](https://agentii.ai/v/SATS/sec85/150)); `Net cash flows from operating / investing / financing activities` ([p.13](https://agentii.ai/v/SATS/sec121/13), [p.12](https://agentii.ai/v/SATS/sec120/12), [p.152](https://agentii.ai/v/SATS/sec85/152)); `Segment Adjusted OIBDA` bridge terms ([p.108](https://agentii.ai/v/SATS/sec121/108)); the Q4 2025 and Q2 2025 terms by difference from filed figures (§1.2, §2.3). **No term is absent from the source. No back-solve.** No `computed` value is cited as a derivation anywhere in this artifact.

### 7.2 The VRT zero-rows gap does NOT reproduce — and the truth is worse

`validate_calculation` **runs** at all three SATS accessions:

| Accession | Filing | Rows | pass / warn / fail |
|---|---|---|---|
| `0001104659-25-107277` | Q3 2025 10-Q (sec120) | **33** | 21 / 1 / 11 |
| `0001104659-26-058150` | Q1 2026 10-Q (sec121) | **26** | 15 / 2 / 9 |
| `0001104659-26-021817` | FY2025 10-K (sec85) | **41** | 15 / 7 / 19 |

So the disposition proposed in A5 (`UNVALIDATED-BY-PLATFORM`) does **not** apply to SATS in VRT's sense — the validator is not silent here. But it is **not thereby reliable**, and the way it fails is new:

**A `status: pass` is returned on a value whose sign is wrong.** `ProfitLoss` Q3 2025: computed **12,781,348,000**, reported **12,781,348,000**, `diff 0`, **status pass** — while the filing prints **$ (12,781,348)** ([p.10](https://agentii.ai/v/SATS/sec120/10)). The same occurs at FY2025: computed = reported = **14,506,939,000**, pass, against a filed **(14,506,939)** ([p.150](https://agentii.ai/v/SATS/sec85/150)).

**The structural reason, and it is the finding:** the validator's `reported` column is drawn from **the same stripped fact store** that serves the metrics block, so the validator compares the store against the store. It is **constitutively incapable** of detecting the strip. This is not the A5 failure mode ("the validator never ran", VRT) nor a simple miss — it is **a validator that runs, passes, and affirms a wrong-signed value**, the most dangerous of the three because it produces positive evidence of correctness. **Carry-forward C2** — propose a distinct disposition for it rather than folding it into A5.

### 7.3 Both DA-29 corollaries confirmed, with fresh instances

- **"`computed` may not be cited as a derivation."** Confirmed and severe. `OperatingIncomeLoss` Q1 2026: instrument `computed` **3,657,411,000** against a filed **392,847** thousand ([p.11](https://agentii.ai/v/SATS/sec121/11)) — wrong by ~9.3×. Q3 2025: `computed` **224,000** / `reported` **563,000**, while the served fact for the same concept and period is **16,641,875,000** — three mutually inconsistent values, none matching the filed (16,641,875). The `computed` column is unusable at SATS.
- **"The `reported` column is therefore not definitionally the filed value."** Confirmed: `IncomeLossFromContinuingOperationsBeforeIncomeTaxes...` Q3 2025 `reported` **16,936,807,000** against a filed **(16,936,807)** ([p.10](https://agentii.ai/v/SATS/sec120/10)); FY2025 `reported` **18,893,314,000** against a filed **(18,893,314)** ([p.150](https://agentii.ai/v/SATS/sec85/150)). Also `PropertyPlantAndEquipmentNet` computed **−6,726,426,000** against a reported **3,084,793,000**.

**Every `reported` value in this artifact was reconciled to the statement face before use. Two of them failed and are recorded above.**

---

## 8. DA-30 — four live instances, the densest in this phase

The rule: *"any artifact quoting a multi-basis concept must name the basis, and must state where the basis was established."* Four multi-basis concepts are live at SATS, each named below with the basis this artifact quotes and where that basis is established.

### 8.1 Caption-vs-content on the statement face — `CostsAndExpenses`

The income statement groups its cost lines under the caption **"Costs and Expenses (exclusive of depreciation and amortization)"** and then includes a `Depreciation and amortization` line **inside that group** ([p.11](https://agentii.ai/v/SATS/sec121/11)). The tagged total therefore depends on the reading:

- **D&A-inclusive basis: 3,274,642** — the tagged `CostsAndExpenses` total, and the basis §1.2 uses, and the only basis that closes the filed arc `OperatingIncomeLoss ← Revenue (+1) + CostsAndExpenses (−1)`.
- **D&A-exclusive basis: 3,108,041** = 3,274,642 − 166,601 — the basis the caption asserts.

**The caption and the content disagree about the same number, on the face of the same statement.** Basis quoted by this artifact: **inclusive (3,274,642)**, established by the filed calculation arc and by the identity closing. That the caption points the other way is recorded because a reader reconciling from the caption would compute 3,108,041 and fail to close — the basis must be named, and it is not named anywhere in the filing.

### 8.2 Net income on two bases, collapsed — and served differently by two platform surfaces

| Basis | Q1 2026 | FY2025 | Where established |
|---|---|---|---|
| Consolidated `Net income (loss)` | **(147,300)** | **(14,506,939)** | [p.11](https://agentii.ai/v/SATS/sec121/11) face; [p.25](https://agentii.ai/v/SATS/sec121/25); [p.150](https://agentii.ai/v/SATS/sec85/150) |
| Attributable to EchoStar | **(146,885)** | **(14,497,180)** | same, and the 10-Q MD&A ([p.120](https://agentii.ai/v/SATS/sec120/120)) |

Difference: NCI of 415 (Q1 2026) / 9,759 (FY2025). **The platform serves the two bases from two different surfaces under the same undimensioned idea:** `get_company_financials` serves `net_income_loss` on the **attributable** basis (146,885,000 at Q1 2026; 14,497,180,000 at FY2025), while `validate_calculation`'s `ProfitLoss` row serves the **consolidated** basis (12,781,348,000 at Q3 2025). Two values for "net income", one period, no basis field. Basis quoted by this artifact: **attributable**, wherever a per-share or MD&A figure is meant; **consolidated**, wherever `ProfitLoss` or the validator is meant. Both are named at every use.

### 8.3 The spectrum asset on two bases in one table

[p.46](https://agentii.ai/v/SATS/sec121/46): **Subtotal $29,614,839** (sum of the licence tranches) versus **Total as of March 31, 2026 $34,550,802**, after **Capitalized interest $10,270,436** and **Impairment of indefinite-lived intangible assets $(5,334,473)**. The two bases differ by **16.7%**. Any comparison of SATS's spectrum to a transaction price must name which basis it uses. Basis quoted by this artifact: **the fully loaded total, $34,550,802**, wherever the balance-sheet carrying amount is meant; **the tranche subtotal, $29,614,839**, where the licence-level detail is meant.

### 8.4 Segment versus consolidated

[p.71](https://agentii.ai/v/SATS/sec121/71): `Segment Total` operating income **392,674** vs `Consolidated` **392,847**, differing by Eliminations **173**; revenue `Segment Total` **3,677,394** vs `Consolidated` **3,667,489**, differing by Eliminations **(9,905)**. Basis quoted: **consolidated**, at every use.

### 8.5 GOOG-mechanism test — REFUTED

The GOOG mechanism is a **segment member served as the consolidated value**. Tested here: the served `OperatingIncomeLoss` Q1 2026 is **392,847,000**, which is the **consolidated** member. The segment members are Pay-TV 471,567, Wireless (35,782), Broadband and Satellite Services 44,184, Other (87,295) — none of them 392,847. Same at Q3 2025: served 16,641,875,000 = consolidated (16,641,875), not any segment member ([p.75](https://agentii.ai/v/SATS/sec120/75)). **The GOOG mechanism does NOT reproduce at SATS.**

---

## 9. P11 — deal-security basis, and why the in-flight transaction changes the figures

**`deal_security_basis: standalone_pre_merger`.**

**What basis is quoted.** Every figure in this artifact is a **standalone pre-close** figure: EchoStar's consolidated results for periods in which neither the AT&T Transactions nor the SpaceX Transactions had closed.

**Where the basis was established.** On the face of the filings, three ways:

1. **Both agreements are pending.** AT&T: *"The completion of the AT&T Transactions are subject to the satisfaction or waiver of customary closing conditions, including, but not limited to, certain government approvals, including, among other things, receipt of certain consents and approvals from the FCC and the United States Department of Justice"*; *"The closing is expected to occur in the first half of 2026"* ([p.15](https://agentii.ai/v/SATS/sec121/15)). SpaceX: *"The Spectrum Transfer Closing is expected to occur in the first half of 2026. The Spectrum Acquisition Closing is expected to occur on or about November 30, 2027"* ([p.16](https://agentii.ai/v/SATS/sec121/16)).
2. **Nothing has been derecognised.** The licences remain on the balance sheet at 2026-03-31 ([p.46](https://agentii.ai/v/SATS/sec121/46)); AT&T holds only a short-term spectrum manager lease ([p.14](https://agentii.ai/v/SATS/sec121/14)). No gain or loss on disposal is recognised anywhere.
3. **The 10-K states the basis depends on the closings.** *"until the closing of these transactions ... funding is not deemed committed"* — with **substantial doubt about going concern** absent them ([p.76](https://agentii.ai/v/SATS/sec85/76)).

**Does the in-flight transaction change what any figure means? Yes — three figures, and the first is the largest in the series.**

1. **The Q3 2025 operating loss is transaction-caused.** The $16,481,468 thousand impairment exists *because* the AT&T and SpaceX Transactions were **triggering events** ([p.76](https://agentii.ai/v/SATS/sec85/76)). The register quotes this figure as evidence of a **sale**; it is in fact an artefact **of the pending sale**. The same figure is simultaneously the register's DA-24 exhibit and a disclosure about an unclosed transaction — so any DA-24-shaped reading of SATS must be taken on the `standalone_pre_merger` basis, where the item is a charge, not on a `post_close` basis, where it would not exist in this form.
2. **The spectrum carrying values are pre-close values.** $34,550,802 thousand ([p.46](https://agentii.ai/v/SATS/sec121/46)) is a **pre-disposal** carrying amount, not a realisable amount. The consideration is $22.650 billion cash from AT&T (minimum $18.6 billion) and $17 billion → approximately $20 billion from SpaceX ([p.14](https://agentii.ai/v/SATS/sec121/14), [p.15](https://agentii.ai/v/SATS/sec121/15), [p.157](https://agentii.ai/v/SATS/sec85/157)); the combined anticipated proceeds are *"$22.650 billion in cash"* plus *"approximately $22 billion in consideration which includes $20 billion upon the Spectrum Acquisition Closing ... and payments for the Interim Debt Service of approximately $2 billion"* ([p.76](https://agentii.ai/v/SATS/sec85/76)). The gain or loss on disposal will be determined **at closing**, on a different basis from anything in the current statements.
3. **The standalone figures are not a going-concern-basis series in the ordinary sense.** Scheduled maturities are $2.0 billion (July 2026), $1.377 billion (August 2026) and $2.750 billion (December 2026) ([p.157](https://agentii.ai/v/SATS/sec85/157)); the AT&T closing must concurrently redeem $3.5 billion of 11¾% notes ([p.15](https://agentii.ai/v/SATS/sec121/15)); and $414 million of cash interest on the Seller Notes has already been paid and is reimbursable only on the Spectrum Transfer Closing ([p.16](https://agentii.ai/v/SATS/sec121/16)). Continuation as reported depends on closings the company does not control.

**One further basis point, since P11's enum was drafted for acquirers:** SATS is on the **disposing** side of both transactions. `standalone_pre_merger` is still the correct label — the statements are the standalone pre-close statements — but "pre-merger" here means *pre-disposal*, and the artifact records that reading explicitly rather than relying on the enum's label.

---

## 10. Corrections to 001 (001 is frozen; nothing in it is rewritten)

001's only SATS metric row is `SATS | Spectrum gains vs operating business | ~$27B vs $15.0B FY revenue | fact`; its spec cites the SPCX–EchoStar transaction at `$19.6B`.

| 001 figure | Verdict | Filed basis |
|---|---|---|
| **`$15.0B` FY revenue** | **REPRODUCES EXACTLY** | Total revenue **15,004,989** thousand ([p.150](https://agentii.ai/v/SATS/sec85/150)) |
| **`$19.6B` SPCX–EchoStar transaction** | **REPRODUCES ARITHMETICALLY — but re-grade DERIVED and correct the description** | $17 billion Total Consideration Amount ([p.15](https://agentii.ai/v/SATS/sec121/15)) + $2.6 billion for 15 MHz of additional AWS-3 spectrum ([p.157](https://agentii.ai/v/SATS/sec85/157)) = $19.6B. The filing's own rounded statement is **"approximately $20 billion"**, with up to $11 billion in SpaceX Class A at $212/share |
| **`~$27B`** | **DOES NOT REPRODUCE** | No filed figure equals $27B. See the substitution list below |
| **`Spectrum gains`** | **REFUTED as a characterisation** | No spectrum-sale gain has been recognised. Nothing has closed; the Q3 2025 event was a **charge** of $16.481 billion; the FY2025 cash-flow statement's only disposal item is `Asset sales and other losses (gains) (100,028)` ([p.152](https://agentii.ai/v/SATS/sec85/152)) |

**Two corrections, recorded rather than applied:**

**CORRECTION 001-S1 — grade and description of `$19.6B`.** The figure is reproducible but is the **sum of two filed terms**, not a filed figure, so under P4 it is `DERIVED`, not `fact`. And 001's description attributes the $19.6B to *"AWS-4, H-Block and ..."* — but **AWS-4 and H-Block alone are the $17 billion Total Consideration Amount** ([p.15](https://agentii.ai/v/SATS/sec121/15)); the additional $2.6 billion is for **15 MHz of AWS-3 spectrum in 1695–1710 MHz**, added by the Amended and Restated License Purchase Agreement dated November 5, 2025 ([p.157](https://agentii.ai/v/SATS/sec85/157)). The licence description and the grade both need correcting; the magnitude does not.

**CORRECTION 001-S2 — `~$27B` does not reproduce; substitute the filed bases.** No figure in the SATS filings equals ~$27B — a keyword search over the corpus returns no page described as containing it. The filed bases are:

| Filed basis | Value | Source |
|---|---|---|
| AT&T Closing Purchase Price (cash) | **$22.650 billion** (Minimum Purchase Price $18.6 billion) | [p.14](https://agentii.ai/v/SATS/sec121/14) |
| SpaceX Total Consideration Amount, initial | **$17 billion** | [p.15](https://agentii.ai/v/SATS/sec121/15) |
| SpaceX, as amended | **"approximately $20 billion"**, up to $11 billion in SpaceX Class A | [p.157](https://agentii.ai/v/SATS/sec85/157) |
| Combined anticipated proceeds | **$22.650B cash + approximately $22B** (incl. $20B at the Acquisition Closing and ~$2B Interim Debt Service) | [p.76](https://agentii.ai/v/SATS/sec85/76) |
| Spectrum carrying value, tranche subtotal | **$29,614,839 thousand** | [p.46](https://agentii.ai/v/SATS/sec121/46) |
| Spectrum carrying value, fully loaded | **$34,550,802 thousand** | [p.46](https://agentii.ai/v/SATS/sec121/46) |

Note that the register's own DA-24 text and 001's row are consistent with each other and both wrong in the same direction: **$16.6B is the impairment charge, not a $27B gain.** The nearest filed single figure to $27B is $29,614,839 thousand — the spectrum **carrying value**, which is a balance-sheet amount and not a transaction value at all. If $27B was intended as a transaction value, it has no filed basis.

**Direction of travel for 001's SATS headline figure.**

- **Toward DEMONSTRATED in part.** `$15.0B` FY revenue reproduces exactly. `$19.6B` reproduces arithmetically from two filed terms.
- **Away from DEMONSTRATED in part.** `~$27B` does not reproduce on any filed basis, and the row's framing — *"Spectrum gains"* — presupposes a realised gain that does not exist. The largest figure in the neighbourhood is a **$16.6 billion non-cash impairment charge** arising from transactions that have not closed.
- **Net:** the SATS row is **partly validated and partly corrected**. The revenue mark survives; the transaction mark survives with a grade change; the magnitude mark does not survive; the characterisation does not survive.

---

## Carry-forwards

**C1 — DA-24 independence:** the register's SATS independence claim **FAILS** (§2.5). Requires a register edit: either re-designate a different instance as DA-24's independence proof, or restate DA-24's independence as unproven. **A7 is resolved by this artifact; the register edit is not made here.**

**C2 — validator-affirms-stripped-value:** propose a disposition distinct from A5's `UNVALIDATED-BY-PLATFORM` for the case where `validate_calculation` **runs and returns `status: pass`** on a value whose sign is wrong, because its `reported` column shares the stripped store. VRT's gap (zero rows) and SATS's (pass on a wrong-signed value) are different failures with different remedies and must not be merged.

**C3 — register Clean row:** remove **SATS** from the DA-23 Clean row and add it to the DA-23 instance set on four axes (§1). This is the second register-row correction this phase has produced on a founding instance.

**C4 — DA-27 kind:** the untestability at SATS is a **third kind** — MECHANISM-POPULATION IDENTITY, the issuer-side form of A6's caution — distinct from ingestion absence, genuine absence, and validator-completeness. The three-kind taxonomy needs a fourth entry, or the A6 caution needs generalising from samples to issuers.

**C5 — A3 basis discontinuity:** the combined Class A-and-B per-share denominator plus 58 million anti-dilutive convertible shares ([p.25](https://agentii.ai/v/SATS/sec121/25)) is a live instance of the denominator-basis discontinuity.

**C6 — component-tag ingestion absence:** the 2025 impairment charge is tagged `sats:AssetImpairmentChargesAndOther`, so the `us-gaap:AssetImpairmentCharges` route returns six facts, none of them the $16.481B or $17.632B charge. Any register census keyed on us-gaap concepts will silently miss filer-extension tags. Same family as `GrossProfit` / plain `Revenues`.

**C7 — `NetIncomeLoss` / `EarningsPerShareBasic` strip scope:** SATS extends the strip beyond the operating line to nine-and-fourteen-period series, and the non-numeric table-text facts retain the correct signs — localising the defect to numeric fact extraction.

## Could not be verified

- **All SATS filings carry `processing_status: "pending"`**; `get_company_financials` reports `gold_filings_count: 0`, `processed_pct: 0.0000`, and `statements_available: false` ("Rendered markdown financial statements not yet available — `pipeline.xbrl_rendered_statements` pending creation"). This is the **INGESTION-ABSENCE** kind of untestability and must not be merged with the other two: the remedy is pipeline completion, not an artifact correction. **It does not block this artifact** — every figure here is read from a filing page, not from a rendered statement — but it does mean the platform's own statement view is unavailable as a cross-check.
- **`get_calculation_tree(sec85)` was not read.** The call returned 72.8 KB and was persisted unread. The `sec121` and `sec120` trees were read and supplied the filed arc used in §1.1; the FY2025 tree would add confirmation, not a new term. Recorded as an unread input, not as a failed check.
- **A share count of 83,850 thousand appears on 2023 periods served from `sats-20230930.htm`,** against ~270,842 thousand on the FY2023 statement face ([p.150](https://agentii.ai/v/SATS/sec85/150)). This is an unexplained anomaly consistent with entity-scope contamination in the served series. **It is recorded as an anomaly, not asserted as a finding**, because I did not read the corresponding 2023 filing page. **Open item for the ledger.**
- **The four `packaging/targets/*` skill trees were not used** (0/6 validation); `skill_pin` is the independently re-derived `07d26b9c738b`.

---

## Sources

> Every figure asserted above resolves to the page cited. The links are inline at the point of use; this table is the index to them.

| Figure (as filed) | Source |
|---|---|
| Q1 2026 condensed consolidated statements of operations — the component-identity cells, the two cost-groupings basis, and the net-income two-basis pair | [📄 SATS 10-Q p.11](https://agentii.ai/v/SATS/sec121/11) |
| Q1 2026 condensed consolidated statements of cash flows — operating / investing / financing subtotals | [📄 SATS 10-Q p.13](https://agentii.ai/v/SATS/sec121/13) |
| Note 3 Basic and Diluted Net Income (Loss) Per Share — consolidated vs attributable basis, combined Class A and B denominator, 58 million anti-dilutive convertible shares | [📄 SATS 10-Q p.25](https://agentii.ai/v/SATS/sec121/25) |
| Note 1 — AT&T License Purchase Agreement: $22.650 billion, Minimum Purchase Price $18.6 billion, short-term spectrum manager lease | [📄 SATS 10-Q p.14](https://agentii.ai/v/SATS/sec121/14) |
| Note 1 — AT&T closing conditions (FCC, DOJ, H1 2026); 11 3/4% notes $3.5 billion; SpaceX License Purchase Agreement; $17 billion Total Consideration Amount | [📄 SATS 10-Q p.15](https://agentii.ai/v/SATS/sec121/15) |
| Note 1 — SpaceX Equity Amount $8.5 billion at $212/share; Seller Notes $9.821 billion; Spectrum Acquisition Closing on or about November 30, 2027; Interim Debt Service ~$2 billion; $414 million cash interest | [📄 SATS 10-Q p.16](https://agentii.ai/v/SATS/sec121/16) |
| Wireless Spectrum Licenses note — the spectrum asset on two bases: $29,614,839 subtotal vs $34,550,802 total | [📄 SATS 10-Q p.46](https://agentii.ai/v/SATS/sec121/46) |
| Q1 2026 segment table — segment total vs consolidated; the segment members | [📄 SATS 10-Q p.71](https://agentii.ai/v/SATS/sec121/71) |
| Segment Adjusted OIBDA reconciliation — the definition verbatim, and the bridge that forces the impairment credit to be negative | [📄 SATS 10-Q p.108](https://agentii.ai/v/SATS/sec121/108) |
| Q3 2025 condensed consolidated statements of operations — Total revenue 3,614,258; Total costs and expenses 20,256,133; Operating income (loss) (16,641,875) | [📄 SATS 10-Q p.10](https://agentii.ai/v/SATS/sec120/10) |
| Nine-month 2025 condensed consolidated statements of cash flows — all three subtotals, 2025 and 2024 | [📄 SATS 10-Q p.12](https://agentii.ai/v/SATS/sec120/12) |
| Note 1 impairment table — Impairments and other $16,481,468; Wireless 16,199,344; Broadband and Satellite Services 282,124 | [📄 SATS 10-Q p.19](https://agentii.ai/v/SATS/sec120/19) |
| Q3 2025 segment table — Wireless impairments and other 16,199,344; operating income (loss) by segment | [📄 SATS 10-Q p.75](https://agentii.ai/v/SATS/sec120/75) |
| MD&A segment results — consolidated operating loss $16.642 billion; the $16.199 billion / $282 million disaggregation | [📄 SATS 10-Q p.95](https://agentii.ai/v/SATS/sec120/95) |
| MD&A other consolidated results — operating income (loss) (16,641,875); net income (loss) attributable to EchoStar (12,781,196); effective tax rate 24.5% | [📄 SATS 10-Q p.120](https://agentii.ai/v/SATS/sec120/120) |
| FY2025 consolidated statements of operations, three annual columns — the component-identity cells and the FY2025/FY2024/FY2023 figures | [📄 SATS 10-K p.150](https://agentii.ai/v/SATS/sec85/150) |
| FY2025 consolidated statements of cash flows, three annual columns — the FY2025 operating / investing / financing subtotals; `Asset sales and other losses (gains) (100,028)`; `Impairments and other 17,632,011` | [📄 SATS 10-K p.152](https://agentii.ai/v/SATS/sec85/152) |
| MD&A liquidity — combined anticipated proceeds $22.650 billion + approximately $22 billion; the $17.632bn / $16.481bn / $1.151bn quarterly charges; triggering events; going-concern substantial doubt | [📄 SATS 10-K p.76](https://agentii.ai/v/SATS/sec85/76) |
| Amended and Restated SpaceX License Purchase Agreement — the $2.6 billion AWS-3 addition; $17 billion → approximately $20 billion; $11 billion Amended Equity Amount at $212/share; debt maturities; Auction 113 | [📄 SATS 10-K p.157](https://agentii.ai/v/SATS/sec85/157) |
