---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-5
ticker: GSAT
skill: recent-quarter
mode: methodology
generated_at: 2026-09-19T14:15:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07d26b9c738b"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: "the platform serves a filed negative as a positive of identical magnitude (|x|, not inversion). At GSAT the strip is PER-FACT, not per-period: 12 of 12 filed-negative served values came back as |x| and 8 of 8 filed-positive served values came back correct, across the same rows and the same quarters, so the served sign is uninformative in BOTH directions unless the identity closes. The retained-deficit series is a SECOND, independent exhibit: 20 of 20 served positive against a line that is a deficit at every date, with NO filed-positive control anywhere in the series — so that series cannot be read without the income-statement series, which carries both signs. DA-23 IS A LAYER PROPERTY, NOT A DATA PROPERTY: the earnings-calendar layer carries the correct sign for the same metric and period where the row/XBRL layer strips it, and NEITHER LAYER CAN REPAIR THE OTHER — a clean reading from one surface is not evidence about the other."
  - da_id: DA-24
    chosen_reading: "non-operating items sitting inside the filed operating line. At GSAT the instance is INVERTED relative to SATS: not an impairment charge but a government-sourced credit — CARES Act employee retention credits of $2.0M and $1.9M were recognised as REDUCTIONS to operating expenses in Q1 2025 and Q2 2025, so filed operating income in those two quarters is flattered by a non-recurring, non-operating benefit. A second instance runs the other way, as an EXPENSE inside MG&A in 2026, and it is QUANTIFIED for Q1 2026: the Q1 2026 10-Q states legal and professional fees rose $1.4 million 'due primarily to transaction costs related to the Mergers, totaling $3.2 million' against a filed MG&A rise of $3,239 thousand — the quarter's entire MG&A increase. The Q2 2026 10-Q names the same driver for a +$10.4 million legal-and-professional-fee rise but does not split its +$13,342 thousand MG&A increase between transaction costs and other drivers."
  - da_id: DA-26
    chosen_reading: "annual figures mislabelled as quarterly. TWO instances at GSAT, both in the served row layer: the row served as FY2025 Q4 carries the FY2025 ANNUAL (revenue 3.794x the quarter, net income sign-stripped and 1.34x the quarter's loss) and the row served as FY2024 Q4 carries the FY2024 ANNUAL (revenue 4.092x the quarter). The true Q4 values are recoverable as FY minus 9M from filed columns, and the earnings-calendar layer corroborates the derived Q4 2025 revenue to the dollar."
  - da_id: DA-27
    chosen_reading: "fiscal labels synthesised from the calendar quarter of the period end. GSAT's fiscal year IS the calendar year, so the label synthesis is benign in itself and cannot be used to detect the defect — which is exactly why it does not rescue the two annual-as-quarterly rows: the label is right and the values are wrong."
  - da_id: DA-28
    chosen_reading: "capital-structure discontinuity invalidating share-count detectors. GSAT effectuated a 1:15 reverse stock split on 2025-02-10 and both 2026 10-Qs state in footnote (1) that all prior-period share and per-share amounts have been adjusted for it. Consequence carried: the served EPS values for 2024 are NOT on the filed basis in magnitude (they are plausible on a PRE-split share count: Q1 2024 $0.01 and Q3 2024 $0.00 against filed-order $(0.15) and $0.06), and the served FY2024 annual EPS 0.58 is the filed (0.59) TRUNCATED, not rounded. Every EPS used in this artifact is taken from a filed per-share table, never from the served row."
  - da_id: DA-29
    chosen_reading: "a reconciliation that closes is not thereby a check. At GSAT the validator `pass` on `IncomeLossFromContinuingOperationsBeforeIncomeTaxes...` reports computed = reported = 22,630,000, diff 0, pass — against a filed (22,630). The pass is on a STRIPPED value, so the instrument's zero-difference row is evidence of nothing; and the `OperatingIncomeLoss` row fails with a `computed` of (9,549,000) that reproduces from no filed cell. A fail is as uninformative as a pass."
  - da_id: DA-30
    chosen_reading: "two bases on one concept collapsed without a basis field. At GSAT the largest instance is at the FILING level, not the platform level: net loss for Q1 2026 is filed as $(17,420) thousand in the Q1 2026 10-Q and is $(14,818) thousand implied by the Q2 2026 10-Q's six-month column — a $2,602 thousand gap, disclosed in the later filing as the cumulative retained-earnings adjustment on adoption of ASU 2025-07. Both bases are reported below, always, and the operating series is unaffected (revenue, opex and operating income are identical on both)."
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
citations:
  - figure: "Q2 2026 10-Q Note 2 — two-step merger structure (First/Second Merger); the Written Consent (Thermo ≈57.6% at execution; 'all required approvals ... no further approval ... is required or will be sought'); Merger Consideration ($90.00 per share cash or Amazon stock at an exchange ratio, cash elections prorated to a 40% cap, downward adjustment capped at $110 million); Note 1's ASU 2025-07 modified-retrospective adoption"
    ticker: GSAT
    citation_id: sec166
    page_no: 11
    url: https://agentii.ai/v/GSAT/sec166/11
    located_via: read_source_pages
  - figure: "Q1 2026 10-Q MD&A — 'The Mergers are expected to close in 2027 ... no assurance can be given as to when, or if, the Mergers will occur'; Apple Inc. named as the Customer; Customer = 66% and 61% of total revenue for 3M 2026/2025, no other customer above 10%; 15% of network capacity retained"
    ticker: GSAT
    citation_id: sec164
    page_no: 26
    url: https://agentii.ai/v/GSAT/sec164/26
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q income statement, 3M and 6M 2026 vs 2025 — revenue 64,772 / 67,148 / 134,836 / 127,180; the six opex lines summing to 69,547 / 61,002 / 131,441 / 129,535; (loss) income from operations (4,775) / 6,146 / 3,395 / (2,355); net (26,539) / 19,208 / (41,357) / 1,877; reverse-split footnote (1)"
    ticker: GSAT
    citation_id: sec166
    page_no: 5
    url: https://agentii.ai/v/GSAT/sec166/5
    located_via: read_source_pages
  - figure: "Q1 2026 10-Q income statement with Q1 2025 comparative — revenue 70,064 / 60,032; opex 61,894 / 68,533; income (loss) from operations 8,170 / (8,501); net loss (17,420) / (17,331); attributable to common (20,035) / (19,946); EPS (0.16) / (0.16); WACS 128,417 / 126,476; reverse-split footnote (1)"
    ticker: GSAT
    citation_id: sec164
    page_no: 4
    url: https://agentii.ai/v/GSAT/sec164/4
    located_via: read_source_pages
  - figure: "Q3 2025 10-Q income statement, 3M and 9M 2025 vs 2024 — revenue 73,845 / 201,025 (9M 2024 189,172); opex 63,689 / 193,224; income from operations 10,156 / 7,801 (9M 2024 3,300); net 1,090 / 2,967 (9M 2024 (12,945)); attributable (1,583) / (4,965); EPS (0.01) / (0.04); WACS 126,688 / 126,593; reverse-split footnote (1)"
    ticker: GSAT
    citation_id: sec163
    page_no: 4
    url: https://agentii.ai/v/GSAT/sec163/4
    located_via: read_source_pages
  - figure: "FY2025 10-K income statement, FY2025 / FY2024 / FY2023 — revenue 272,986 / 250,349 / 223,808; opex 265,556 / 251,298 / 223,973; income (loss) from operations 7,430 / (949) / (165); net loss (8,651) / (63,164) / (24,718); attributable (19,256) / (73,798) / (35,323); EPS (0.15) / (0.59) / (0.29); WACS 126,757 / 125,877 / 122,334; reverse-split footnote (1)"
    ticker: GSAT
    citation_id: sec128
    page_no: 48
    url: https://agentii.ai/v/GSAT/sec128/48
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q MD&A — revenue-line drivers verbatim (wholesale capacity −5% / +9%; Commercial IoT +7% / +10%; SPOT −7% / −7%; Duplex −26% / −26%; government and other +20% / +53%; equipment +$0.8M / +$1.2M) and Operating Expenses (totals 69.5 / 61.0 and 131.4 / 129.5; the CARES Act credits: $2.0M and $1.9M, $1.4M / $1.3M allocated to cost of services and $0.6M each to MG&A)"
    ticker: GSAT
    citation_id: sec166
    page_no: 34
    url: https://agentii.ai/v/GSAT/sec166/34
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q Note 12 'Net (Loss) Income Per Share' — net (26,539) / (41,357); preferred dividends (2,644) / (5,259); attributable to common shareholders (29,183) / (46,616); basic and diluted WACS 129,122 / 128,771; EPS (0.23) / (0.36)"
    ticker: GSAT
    citation_id: sec166
    page_no: 27
    url: https://agentii.ai/v/GSAT/sec166/27
    located_via: read_source_pages
  - figure: "Q1 2026 10-Q Note 11 'Loss Per Share' — net loss (17,420) / (17,331); preferred dividends (2,615); attributable (20,035) / (19,946); basic and diluted WACS 128,417 / 126,476; EPS (0.16) / (0.16). The same page carries the related-party section (XCOM/Virewirx; the Strategic Review Committee's 45% Thermo threshold)"
    ticker: GSAT
    citation_id: sec164
    page_no: 22
    url: https://agentii.ai/v/GSAT/sec164/22
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q Note 1 'Basis of Presentation' — the MSS business as the only reportable segment; Thermo as principal owner and largest stockholder; the Merger Agreement paragraph (two-step structure); the 'Recently Adopted Accounting Pronouncement' heading"
    ticker: GSAT
    citation_id: sec166
    page_no: 10
    url: https://agentii.ai/v/GSAT/sec166/10
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q Part II Item 1A and Item 5 — the cash/stock election and proration risk verbatim; the downward adjustment 'up to $110 million' and 'approximately $97 million reduced from $110 million'; Items 2-4 'None'; the Rule 10b5-1 plan statement"
    ticker: GSAT
    citation_id: sec166
    page_no: 44
    url: https://agentii.ai/v/GSAT/sec166/44
    located_via: read_source_pages
  - figure: "Q1 2026 10-Q MD&A — MG&A 'increased $3.2 million' (personnel +$1.2 million; legal and professional fees +$1.4 million 'due primarily to transaction costs related to the Mergers, totaling $3.2 million', partly offset by non-recurring Q1 2025 Globalstar SPE costs and a $0.6 million CARES Act credit); stock-based compensation −$4.3 million; the $7.0 million satellite disposal loss in Q1 2025; D&A −$3.9 million; interest +$11.9 million"
    ticker: GSAT
    citation_id: sec164
    page_no: 32
    url: https://agentii.ai/v/GSAT/sec164/32
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q MD&A — MG&A 'increased $13.3 million and $16.6 million' (3M / 6M) with legal and professional fees up $10.4 million and $11.7 million 'due primarily to transaction costs related to the Mergers'; cost of services +$4.1 million / +$8.9 million"
    ticker: GSAT
    citation_id: sec166
    page_no: 35
    url: https://agentii.ai/v/GSAT/sec166/35
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q consolidated balance sheets, 2026-06-30 / 2025-12-31 — cash 409,771 / 447,471; derivative asset — / 114,461; retained deficit (2,206,570) / (2,136,797); total stockholders' equity 292,613 / 355,729; 129,562,435 common shares issued and outstanding"
    ticker: GSAT
    citation_id: sec166
    page_no: 6
    url: https://agentii.ai/v/GSAT/sec166/6
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q MD&A — foreign currency (1.4) / (3.0) against 12.0 / 16.1; the $4.2 million contingent-interest gain; the ASU 2025-07 verbatim ('The $2.6 million loss recorded during the first quarter of 2026 was reclassified back to the derivative asset'); income tax expense +$5.7 million / +$2.7 million"
    ticker: GSAT
    citation_id: sec166
    page_no: 37
    url: https://agentii.ai/v/GSAT/sec166/37
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q MD&A overview and Performance Indicators — the two revenue bases verbatim: 'total revenue decreased 3% to $64.8 million from $67.1 million' (3M) and 'increased 6% to $134.8 million from $127.2 million' (6M)"
    ticker: GSAT
    citation_id: sec166
    page_no: 32
    url: https://agentii.ai/v/GSAT/sec166/32
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q MD&A — the Customer at 64% and 62% of total revenue for 6M 2026/2025, no other customer above 10%, 15% of capacity retained, approximately 811,000 MSS subscribers at 2026-06-30, and the Band 53/n53 spectrum description"
    ticker: GSAT
    citation_id: sec166
    page_no: 30
    url: https://agentii.ai/v/GSAT/sec166/30
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q condensed statements of cash flows, 6M 2026 / 2025 — operating 159,767 / 209,741; investing (208,326) / (271,788); financing 10,570 / (22,024); cash at end 409,771 / 308,226; supplemental non-cash: the $114,461 embedded derivative derecognised on ASU 2025-07 adoption"
    ticker: GSAT
    citation_id: sec166
    page_no: 9
    url: https://agentii.ai/v/GSAT/sec166/9
    located_via: read_source_pages
key_metrics:
  operating_margin_pct_3m: -7.37
  revenue_growth_pct_3m: -3.54
  revenue_growth_pct_6m: 6.02
  q1_2026_net_loss_basis_gap_thousands: 2602
---

# GSAT — recent-quarter: the corrected series, the sign layer, and a two-basis Q1 2026

**The finding.** GSAT's quarter is a **contract-mechanics series, not a demand series**, and the
platform's served figures are wrong in three separable ways at once — sign, period base, and basis.
The corrected series is below. Two items are structural rather than arithmetic and matter beyond
the platform:

1. **GSAT's acquirer has already signed.** GSAT entered a Merger Agreement with Amazon.com, Inc. on
   **2026-04-13**, expected to close in **2027**, and at execution Thermo (≈57.6%) delivered a
   written consent that the filing states is *all* stockholder approval required
   ([📄 GSAT 10-Q p.11](https://agentii.ai/v/GSAT/sec166/11);
   [📄 GSAT 10-Q p.26](https://agentii.ai/v/GSAT/sec164/26)). Every figure here therefore describes
   a business whose acquirer has signed — see §0.2.
2. **Q1 2026's reported net loss has two filed bases**, $(17,420) thousand in the Q1 2026 10-Q and
   $(14,818) thousand implied by the Q2 2026 10-Q's six-month column. The $2,602 thousand is
   disclosed and named in the later filing. §4.2.

**The corrected series** — filed cells, all $ thousands (filed signs as printed), with the opex
definition of §1.1 stated once and applied throughout:

| Quarter | Total revenue | Total opex | Operating income | Op margin | Net income | Net margin | EPS |
|---|---|---|---|---|---|---|---|
| Q1 2025 | **60,032** | 68,533 | **(8,501)** | **(14.16)%** | (17,331) | (28.87)% | $(0.16) |
| Q2 2025 | **67,148** | 61,002 | **6,146** | **9.15%** | 19,208 | 28.61% | $0.13 |
| Q3 2025 | **73,845** | 63,689 | **10,156** | **13.75%** | 1,090 | 1.48% | $(0.01) |
| Q4 2025 | **71,961** ᴰ | 72,332 ᴰ | **(371)** ᴰ | **(0.52)%** | (11,618) ᴰ | (16.14)% | $(0.11) ᴰ |
| Q1 2026 | **70,064** | 61,894 | **8,170** | **11.66%** | (17,420) ᴬ / (14,818) ᴮ | (24.86)% ᴬ / (21.15)% ᴮ | $(0.16) |
| Q2 2026 | **64,772** | 69,547 | **(4,775)** | **(7.37)%** | (26,539) | (40.97)% | $(0.23) |

Grade: **DEMONSTRATED** for every bold figure (filed cells, or arithmetic directly on filed cells);
ᴰ = derived as FY minus 9M from two filed columns (Q4 2025: 272,986 − 201,025 = 71,961 revenue;
265,556 − 193,224 = 72,332 opex; 7,430 − 7,801 = (371) operating; (8,651) − 2,967 = (11,618) net;
attributable (19,256) − (4,965) = (14,291); at a derived Q4 basic share count of 127,249 thousand from
the FY2025 WACS of 126,757 and the 9M2025 WACS of 126,593, EPS = $(0.11)). ᴬ / ᴮ = the two filed
bases of Q1 2026 (§4.2). Sources: [📄 GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5),
[📄 GSAT 10-Q p.4](https://agentii.ai/v/GSAT/sec164/4),
[📄 GSAT 10-Q p.4 (Q3 2025)](https://agentii.ai/v/GSAT/sec163/4),
[📄 GSAT 10-K p.48](https://agentii.ai/v/GSAT/sec128/48).

**The two findings that come out of the corrected series:**

- **The operating line turned negative in Q2 2026** — from **+8,170** in Q1 2026 to **(4,775)**, a
  **12,945 thousand adverse swing in one quarter — a 158.4% decline measured against Q1's operating
  profit** (12,945 ÷ 8,170 = 158.45%) — on revenue down 7.6% sequentially (70,064 → 64,772; −3.5%
  YoY, 67,148 → 64,772) and opex up 12.4% sequentially (61,894 → 69,547). Both directions moved
  against the company in the same quarter. **Correction to carry:** an earlier draft put this swing at
  **1,570.9%**; that number reproduces from no filed cell — its implied denominator is 824 thousand,
  which appears on none of the pages read — so it is withdrawn under the DA-29 discipline that a
  `computed` reproducing from nothing is a back-solve.
- **The Q2 2025 comparison quarter was itself flattered by a government credit**: $1.9M of CARES Act
  employee retention credits were recognised as a *reduction of operating expenses* in Q2 2025
  ([📄 GSAT 10-Q p.34](https://agentii.ai/v/GSAT/sec166/34)) — §4.1. So the YoY decline is
  overstated by that amount and the underlying deterioration still holds: ex-credit Q2 2025 opex
  would be 62,902 thousand against a filed 61,002 thousand.

## 0.1 The component identity and the opex definition — stated once, applied throughout

**GSAT files no gross-profit subtotal on the income-statement face.** The statement runs *Total
revenue* → *Operating expenses:* (six lines) → *Total operating expenses* → *(Loss) income from
operations*
([📄 GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5)). The operable identity is therefore

> **Total revenue − Total operating expenses = (Loss) income from operations**

on the **D&A-INCLUSIVE `us-gaap:CostsAndExpenses` basis** — that is, an opex definition that
contains cost of services, cost of subscriber equipment sales, MG&A, stock-based compensation,
reduction in the value and disposal of long-lived assets, **and depreciation, amortization and
accretion**. The basis must be carried with every reading: an exclusive (cost-of-sales-only) pairing
gives a different number and is not the filed subtotal. It closes exactly in **all four filed
columns** of the Q2 2026 10-Q and in both columns of the Q1 2026 10-Q:

| Period | Components (filed) | Sum | Total operating expenses (filed) | Revenue − opex | Operating income (filed) |
|---|---|---|---|---|---|
| 3M 2026 | 23,602 + 3,395 + 23,025 + 2,723 + 0 + 16,802 | 69,547 | **69,547** ✓ | 64,772 − 69,547 | **(4,775)** ✓ |
| 3M 2025 | 19,479 + 2,881 + 9,683 + 5,949 + 0 + 23,010 | 61,002 | **61,002** ✓ | 67,148 − 61,002 | **6,146** ✓ |
| 6M 2026 | 47,035 + 5,862 + 37,853 + 5,428 + 64 + 35,199 | 131,441 | **131,441** ✓ | 134,836 − 131,441 | **3,395** ✓ |
| 6M 2025 | 38,104 + 4,928 + 21,272 + 12,906 + 7,038 + 45,287 | 129,535 | **129,535** ✓ | 127,180 − 129,535 | **(2,355)** ✓ |
| Q1 2026 | 23,433 + 2,467 + 14,828 + 2,705 + 64 + 18,397 | 61,894 | **61,894** ✓ | 70,064 − 61,894 | **8,170** ✓ |
| Q1 2025 | 18,625 + 2,047 + 11,589 + 6,957 + 7,038 + 22,277 | 68,533 | **68,533** ✓ | 60,032 − 68,533 | **(8,501)** ✓ |

Six of six close to the dollar. **`EPS × shares` is inadmissible as a sign test** and is not used
anywhere in this artifact; the per-share figures appear only where a filed per-share table supplies
them ([📄 GSAT 10-Q p.27](https://agentii.ai/v/GSAT/sec166/27),
[📄 GSAT 10-Q p.22](https://agentii.ai/v/GSAT/sec164/22)).

## 0.2 Standing of the issuer — `standalone_pre_merger` means more here than "a deal security"

**GSAT and Amazon are the same counterparty seen from two sides of one pending transaction, and the
transaction is signed.** On **2026-04-13** GSAT entered an Agreement and Plan of Merger with
Amazon.com, Inc., Grapefruit Acquisition Sub I, Inc. and Grapefruit Acquisition Sub II, LLC,
structured as a **two-step merger** — Acquisition Sub I merges into Globalstar (the First Merger),
then the surviving corporation merges into Acquisition Sub II, which survives as a direct wholly
owned subsidiary of Amazon ([📄 GSAT 10-Q p.10](https://agentii.ai/v/GSAT/sec166/10);
[📄 GSAT 10-Q p.11](https://agentii.ai/v/GSAT/sec166/11)). The Q1 2026 10-Q states the timing:
*"The Mergers are expected to close in 2027, subject to satisfaction of certain closing conditions in
the Merger Agreement, including required regulatory approvals; however, no assurance can be given as
to when, or if, the Mergers will occur."* ([📄 GSAT 10-Q p.26](https://agentii.ai/v/GSAT/sec164/26)).

Consideration, DEMONSTRATED (verbatim): **$90 per share in cash** — subject to a potential downward
adjustment — **or** Amazon common stock at an exchange ratio, at the holder's election, with
non-electing holders receiving stock and cash elections subject to automatic proration to a maximum
of **40%** of shares outstanding. The aggregate consideration is subject to a downward adjustment
**capped at $110 million**, and as of the Q2 2026 10-Q the Customer payment potentially payable under
the letter agreement is *"approximately $97 million reduced from $110 million as a result of the
Company's achievement of certain operational milestones since the signing"*
([📄 GSAT 10-Q p.44](https://agentii.ai/v/GSAT/sec166/44)).

Three consequences, stated rather than left to the tag:

1. **Stockholder approval is already in hand.** Thermo held ≈**57.6%** at execution and delivered a
   written consent that *"constitutes all required approvals of the Company's stockholders ...
   and no further approval of the Company's stockholders is required or will be sought"*
   ([📄 GSAT 10-Q p.11](https://agentii.ai/v/GSAT/sec166/11)). What remains is regulatory approval
   and the other closing conditions, not a vote.
2. **Q2 2026 is a straddling quarter** — it contains the 2026-04-13 signing. The quarter's operating
   deterioration and its below-the-line swing are therefore *pre-close* figures that management was
   reporting into a signed deal, and the MG&A line is where the transaction's own costs land. MG&A is
   DEMONSTRATED to have risen **+$3,239 thousand (+28.0%)** in Q1 2026 and **+$13,342 thousand
   (+137.8%)** in Q2 2026, on filed cells — and for Q1 2026 the transaction costs are **quantified**:
   *"Legal and professional fees increased $1.4 million ... due primarily to transaction costs
   related to the Mergers, totaling $3.2 million"*
   ([📄 GSAT 10-Q p.32](https://agentii.ai/v/GSAT/sec164/32)) — that is the entirety of the
   quarter's MG&A increase. The Q2 2026 10-Q names the same driver — legal and professional fees up
   $10.4 million and $11.7 million (3M / 6M) *"due primarily to transaction costs related to the
   Mergers"* ([📄 GSAT 10-Q p.35](https://agentii.ai/v/GSAT/sec166/35)) — but does not split the
   +$13,342 thousand MG&A rise between transaction costs and other drivers. **Correction to carry:**
   an earlier draft graded this instance "CLAIMED, not quantified" and said the split was "not
   quantified in the pages read"; that is wrong for Q1 2026, where the filing quantifies it at
   $3.2 million.
3. **The series ends here.** No merged basis exists to compare against, and none is disclosed —
   the `standalone_pre_merger` basis is the only basis on which these figures are meaningful. Under
   the merger agreement the cash/stock mix is at holders' election subject to proration, so the
   consideration's value is not fixed as of `as_of` either.

# 1. `consolidated-p-and-l` — the DA-23 sign test runs here

## 1.1 The served row layer against the filed cells

Ten quarterly rows are served by `get_company_financials`. Every one was tested against the filed
cells — twelve of them verbatim from the four filings cited above.

| Served row | Served operating income | Filed operating income | Verdict | Served net income | Filed net income | Verdict |
|---|---|---|---|---|---|---|
| FY2026 Q2 | +4,775,000 | (4,775) | **STRIPPED** | +26,539,000 | (26,539) | **STRIPPED** |
| FY2026 Q1 | +8,170,000 | 8,170 | clean | +17,420,000 | (17,420) | **STRIPPED** |
| FY2025 Q4 | +7,430,000 | 7,430 *(annual)* | clean value, **wrong period** | +8,651,000 | (8,651) *(annual)* | **STRIPPED** + wrong period |
| FY2025 Q3 | +10,156,000 | 10,156 | clean | +1,090,000 | 1,090 | clean |
| FY2025 Q2 | +6,146,000 | 6,146 | clean | +19,208,000 | 19,208 | clean |
| FY2025 Q1 | +8,501,000 | (8,501) | **STRIPPED** | +17,331,000 | (17,331) | **STRIPPED** |
| FY2024 Q4 | +949,000 | **(949)** *(annual)* | **STRIPPED** + wrong period | +63,164,000 | (63,164) *(annual)* | **STRIPPED** + wrong period |
| FY2024 Q3 | +9,434,000 | 9,434 | clean | +9,934,000 | 9,934 | clean |
| FY2024 Q2 | +1,422,000 | (1,422) | **STRIPPED** | +9,683,000 | (9,683) | **STRIPPED** |
| FY2024 Q1 | +4,712,000 | (4,712) | **STRIPPED** | +13,196,000 | (13,196) | **STRIPPED** |

**Counts, exact:** on the operating line, **5 of 5 filed-negative values served as |x|** and **5 of 5
filed-positive values served correctly**; on the net line, **7 of 7 filed-negative values served as
|x|** and **3 of 3 filed-positive values served correctly**. Pooled: **12 of 12 stripped, 8 of 8
clean, 0 false positives and 0 misses.** The fifth operating-line negative is the FY2024 annual row —
filed **(949)**, served **+949,000** — so that row carries the sign defect and the period defect
independently. The strip is **per-fact, not per-period** — Q1 2026's operating income was filed
*positive* and served correctly in the same row in which net income was filed *negative* and stripped,
so the platform resolved the sign of two facts in one period in opposite directions. **That is why the
served sign carries no information in either direction, and why the component identity of §0.1 is the
only detector.**

**Correction to carry:** an earlier draft read the FY2024 annual row as "clean value, wrong period"
and counted 11/11 stripped and 9/9 clean. The FY2025 10-K files FY2024 income (loss) from operations
as **(949)** — a loss ([📄 GSAT 10-K p.48](https://agentii.ai/v/GSAT/sec128/48)) — so the served
+949,000 is the strip, and that row was the artifact reproducing DA-23 inside its own test.

## 1.2 Five exact fingerprints

The derived quarters are not assertions of consistency; each closes against a filed subtotal:

1. **Q1 2025 operating income (8,501)**: filed 6M 2025 (2,355) − filed Q2 2025 6,146 = **(8,501)** ✓.
   Corroborated independently by the Q1 2026 10-Q's own comparative column, which prints
   *"(8,501)"* with parentheses ([📄 GSAT 10-Q p.4](https://agentii.ai/v/GSAT/sec164/4)) — two filed
   documents, one number.
2. **Q1+Q2 2024 operating income (6,134)**: filed 9M 2024 3,300 − filed Q3 2024 9,434 = **(6,134)**,
   which equals −(4,712 + 1,422), the served magnitudes of the two quarters ✓.
3. **6M 2025 operating income (2,355)**: filed directly ✓, and equal to (8,501) + 6,146 from the
   derived and filed quarters.
4. **Q1 2025 net loss (17,331)**: filed 9M 2025 2,967 − filed Q2 2025 19,208 − filed Q3 2025 1,090 =
   **(17,331)** ✓, corroborated by the Q1 2026 10-Q comparative *"(17,331)"*.
5. **Q1+Q2 2024 net loss (22,879)**: filed 9M 2024 (12,945) − filed Q3 2024 9,934 = **(22,879)** =
   −(13,196 + 9,683) ✓.

## 1.3 The ensemble signature — the served rows do not sum to the filed columns

This is the detector that works without reading a single page, and it is decisive at GSAT:

| Sum of served quarterly rows | Filed 9M column | Difference |
|---|---|---|
| Q1 2024 + Q2 2024 + Q3 2024 operating income = **+15,568** | 9M 2024 = **+3,300** | 12,268 |
| Q1 2025 + Q2 2025 + Q3 2025 operating income = **+24,803** | 9M 2025 = **+7,801** | 17,002 |

The served quarters sum to a *larger positive* number than the filed nine-month subtotal in both
years, and the excess is exactly twice the stripped loss (2 × 6,134 = 12,268 ✓; 2 × 8,501 = 17,002 ✓).
**A served series that overshoots the filed total by twice the hidden loss is the ensemble signature
of |x| stripping** — and the multiplier 2 is the tell that the defect is per-fact rather than
per-period. Grade: DEMONSTRATED (all six cells filed).

## 1.4 The retained-deficit series — a second, independent exhibit (and its missing control)

`us-gaap:RetainedEarningsAccumulatedDeficit` is served **positive in 20 of 20 periods** from
2020-12-31 through 2026-06-30 (`search_xbrl_facts`), against a balance-sheet line printed in
**parentheses** at both dates the balance sheet is in hand: **$(2,206,570)** at 2026-06-30 and
**$(2,136,797)** at 2025-12-31 ([📄 GSAT 10-Q p.6](https://agentii.ai/v/GSAT/sec166/6)). Grade:
**DEMONSTRATED** for those two dates; the remaining eighteen are DEMONSTRATED as served values with
the filed sign DERIVED from the line's definition plus the absence of any cumulative-profit period in
the issuer's history.

**The control is ABSENT, and that matters.** GSAT's retained earnings are negative at *every* date in
the series, so there is no filed-positive period against which to test whether the platform serves
*negatives as |x|* or *everything as positive*. The series alone cannot distinguish the two. **What
makes it readable is the income-statement series of §1.1, which carries both signs and therefore
establishes the strip's direction.** Cross-series reasoning is what licenses the conclusion here —
and it is the same point as the layer property below: a reading from one surface is evidence about
that surface.

Two roll-forward checks on the same series, both DEMONSTRATED:

- 2025-12-31 → 2026-03-31: the deficit rises by **17,420** = the Q1 2026 net loss *as originally
  reported* ✓ **exact**. The filed equity statement therefore carried basis A, not basis B (§4.2).
- 2026-03-31 → 2026-06-30: the deficit rises by **52,353**, which exceeds the filed Q2 2026 net loss
  of 26,539 by **25,814**. The gap is **UNRESOLVED** on the pages read; the named candidate is the
  ASU 2025-07 cumulative retained-earnings adjustment that the Q2 2026 10-Q discloses
  ([📄 GSAT 10-Q p.37](https://agentii.ai/v/GSAT/sec166/37)), and the visible balance-sheet
  corroboration is the **derivative asset going from $114,461 thousand at 2025-12-31 to nil at
  2026-06-30** ([📄 GSAT 10-Q p.6](https://agentii.ai/v/GSAT/sec166/6)). Resolving disclosure: the
  Q2 2026 10-Q statement of stockholders' equity (p.8) and Note 8 (Derivatives) — the adjustment's
  composition. Class: **UNRESOLVABLE-FROM-PUBLIC-SOURCES at `as_of` for the split** (the disclosure
  exists in the filing; it was not read in this pass), NOT a platform defect.

## 1.5 DA-23 is a LAYER property, not a data property

The sign defect does not live in the data and does not live in the issuer. It lives in **a layer of
the platform**, and the layers disagree with each other on the same metric and the same period:

| Layer | Same metric, same period | Sign served | Filed |
|---|---|---|---|
| **Earnings-calendar** | GSAT Q2 2026 EPS actual **−0.23** | **correct** | $(0.23)$ ✓ |
| **Earnings-calendar** | GSAT Q1 2026 EPS actual **−0.16** | **correct** | $(0.16)$ ✓ |
| **Earnings-calendar** | GSAT Q4 2025 EPS actual **−0.07** | correct **sign** | order $(0.09)$–$(0.11)$ |
| **Earnings-calendar** | GSAT Q1 2025 EPS actual **−0.13419** | correct **sign** | $(0.16)$ |
| **Row / XBRL fact** | Q2 2026 EPS served **+0.23** | **stripped** | $(0.23)$ |
| **Row / XBRL fact** | Q1 2026 EPS served **+0.16** | **stripped** | $(0.16)$ |
| **Row / XBRL fact** | Q1 2025 EPS served **+0.16** | **stripped** | $(0.16)$ |
| **Validator** | pre-tax loss "computed = reported = 22,630,000, diff 0, **pass**" | **stripped** | $(22,630)$ |

**Three operational consequences, and they are why this is a property rather than a quirk:**

- **Neither layer can repair the other.** A user who checked GSAT's signs against the consensus feed
  would find every negative served with the correct sign and conclude the store is sound. A user who
  checked the income-statement rows would find eleven stripped values. Both are reading the same
  platform on the same day. **A clean reading from one surface is not evidence about the other.**
- **The layers are demonstrably independent**, which is exactly what makes cross-layer disagreement
  admissible evidence — and why the SATS cross-layer contradiction and the GSAT
  calendar-versus-row split here are results rather than curiosities.
- **The word "layer" is load-bearing.** The validator's `reported` column is the row layer
  re-served: that is why one validator row reproduces a filed figure and the rest do not (§4.3), and
  why the instrument's agreement with itself is not corroboration.

**A refinement established at GSAT, and it cuts the other way too:** the calendar layer gives you the
correct **sign**, not necessarily the correct **value**. Of the seven rows where a filed per-share
figure exists to test against, **five reproduce to the cent** (Q2 2025 $0.13; Q3 2025 $(0.01);
Q4 2024 $(0.42); Q1 2026 $(0.16); Q2 2026 $(0.23)) and **two do not** — Q1 2025, served −0.13419
against a filed-order $(0.16)$, and Q4 2025, served −0.07 against a filed-order $(0.11)$ on the
attributable basis / $(0.09)$ on net. The Q1 2025 magnitude implies a denominator of ≈129.1M shares
(17,331 ÷ 0.13419 ≈ 129,153) against that quarter's own filed basic WACS of **126,476 thousand**
([📄 GSAT 10-Q p.22](https://agentii.ai/v/GSAT/sec164/22)) — a 2.1% gap, so the magnitude is not on
the period's own basis. Class: **UNRESOLVED-FROM-PLATFORM** (a served ratio not reproducible from
filed cells). Use the calendar layer for the sign; never for the magnitude.

## 1.6 The EPS line: truncated, and off the filed share-count basis (DA-28)

- **The served FY2024 annual EPS is 0.58 against a filed $(0.59)$.** Both values are in hand. The
  filed figure is the rounding of (73,798) ÷ 125,877 = **0.58627**; 0.58 is that value **truncated**.
  Grade: DEMONSTRATED for both cell values and the arithmetic; the truncation *mechanism* is
  **MODELED** and is offered as the parsimonious reading, not as a finding.
- **The served 2024 quarterly EPS values are not on the filed basis at all.** Served Q1 2024 $0.01
  and Q3 2024 $0.00 against filed-order $(0.15)$ and $0.06$ — 15× apart in magnitude, which is the
  reverse-split factor. On a pre-split count of ≈1,888 million shares, (13,196) ÷ 1,888,155 = 0.00699
  → $0.01 and 7,261 ÷ 1,888,155 = 0.00385 → $0.00, i.e. **both served values are plausible only on a
  PRE-split denominator.** Grade: DEMONSTRATED (four values + arithmetic); mechanism MODELED. The
  filed filings are explicit that this must not happen — footnote (1) of both 2026 10-Qs and of the
  10-K states that all prior-period per-share amounts have been adjusted for the **1:15 reverse stock
  split on 2025-02-10** ([📄 GSAT 10-K p.48](https://agentii.ai/v/GSAT/sec128/48),
  [📄 GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5)). **Consequence carried: no EPS in this
  artifact comes from the served row.**
- **A DA-30 collision inside one served row:** the row also serves
  `NetIncomeLossAvailableToCommonStockholdersBasic` for Q2 2026 as **+29,183,000** against a filed
  $(29,183)$ — two bases of the same concept (net income and net income attributable to common
  shareholders) in one row, both sign-defective, with **no basis field**. The filed table keeps them
  apart ([📄 GSAT 10-Q p.27](https://agentii.ai/v/GSAT/sec166/27)); the served row does not.

**The EPS basis is proven, and this refutes a two-class artefact claim.** Q2 2026: 29,183 ÷ 129,122 =
**0.226011 → $0.23** ✓ exactly as filed, whereas 26,539 ÷ 129,122 = 0.205537 → $0.21 ✗. Q1 2026:
20,035 ÷ 128,417 = **0.156010 → $(0.16)** ✓, whereas 17,420 ÷ 128,417 = 0.135655 → $(0.14)$ ✗. The
filed per-share figures are on the **attributable-to-common** basis, consistently, in both quarters
and both filings. A claimed ~11.9% "two-class artefact" in the EPS bridge is therefore **not
reproducible**: the bridge closes to the cent on the attributable basis. Grade: DEMONSTRATED.

# 2. `margin-analysis` — the DA-26 / DA-27 period traps bite here

## 2.1 Two annual figures served as quarters (DA-26, two instances)

| Served row | Served revenue | True quarter | Multiplier | Served net income | True quarter |
|---|---|---|---|---|---|
| **FY2025 Q4** | 272,986,000 | 71,961 | **3.794×** | +8,651,000 | (11,618) |
| **FY2024 Q4** | 250,349,000 | 61,177 | **4.092×** | +63,164,000 | (50,219) |

Both served rows are the **annual** income statement — revenue, total opex, operating income, net
income, EPS, R&D — carrying a `fiscal_period = Q4` label synthesised from the calendar quarter of the
2025-12-31 and 2024-12-31 period ends (DA-27). **The label is right and the values are wrong**, which
is why DA-27 cannot detect this and why the two defects must not be merged: GSAT's fiscal year *is*
the calendar year, so nothing about the label would ever look suspicious. Grade: DEMONSTRATED (both
served values and both filed annual values are in hand;
[📄 GSAT 10-K p.48](https://agentii.ai/v/GSAT/sec128/48)). Independent corroboration of the derived
quarters: the earnings-calendar layer serves Q4 2025 revenue as **71,961,000** and Q4 2024 as
**61,176,000** — the first matching the derivation to the dollar, the second within $1 thousand
(the provider's own rounding).

**Consequence:** any quarterly margin history built from the served rows is not a margin history. The
FY2025 "Q4" row's implied margin of 7,430 ÷ 272,986 = **2.72%** is the *annual* margin, and the
FY2024 "Q4" row's 949 ÷ 250,349 = **0.38%** is likewise annual — read with the filed sign, that
annual margin is **(0.38)%, not +0.38%**: the FY2024 annual operating line was a **loss of (949)**
(§1.1), and the served magnitude carries the strip. The corrected Q4 2025 margin is **(0.52)%** and
the corrected Q4 2024 margin is **(6.95)%** ((4,249) ÷ 61,177).

## 2.2 The corrected margin series, and the non-operating share

| Quarter | Op margin | Net margin | Below-the-line gap (net − operating) | Non-operating share |
|---|---|---|---|---|
| Q1 2025 | (14.16)% | (28.87)% | (8,830) | **50.95%** |
| Q2 2025 | 9.15% | 28.61% | 13,062 | **68.00%** |
| Q3 2025 | 13.75% | 1.48% | (9,066) | **831.74%** |
| Q4 2025 | (0.52)% | (16.14)% | (11,247) | **96.81%** |
| Q1 2026 | 11.66% | (24.86)% | (25,590) | **146.90%** |
| Q2 2026 | (7.37)% | (40.97)% | (21,764) | **82.00%** |

**Construction stated, because the metric has more than one.** Non-operating share here =
**|net income − operating income| ÷ |net income|**. A second construction exists — total other
expense plus income tax, over |net income| — which is the one quoted elsewhere in this workspace. The
two **coincide in every filed period at GSAT**, because the filed subtotals between the operating and
net lines leave nothing unaccounted between them (FY2025: 10,203 + 5,878 = 16,081 = |(8,651) −
7,430| ✓; FY2024: 60,080 + 2,135 = 62,215 = |(63,164) − (949)| ✓ = **98.49%** both ways).
**Correction to carry:** an earlier draft of this paragraph reported FY2024 **diverging** at
**101.50%** versus 98.49%, *"because that year's operating line was +949 and added to the loss"*. The
FY2024 operating line was **(949)** — a loss ([📄 GSAT 10-K p.48](https://agentii.ai/v/GSAT/sec128/48))
— so the +949 was the DA-23 strip, and that paragraph was the artifact reproducing the very defect it
documents; on filed signs the constructions agree. **Any citation of this metric must name its
construction** — this is DA-30 applied to a derived metric, and it is the second most common way a
correct number becomes an incorrect claim.

**What the corrected series says:**

- **The true non-operating extreme is Q3 2025 at 831.74%**, not any 2024 quarter: the operating line
  earned **+10,156** and the quarter delivered **+1,090** of net income, because **$(9,066) thousand
  of below-the-line net expense** consumed 89% of a profitable quarter. Grade: DEMONSTRATED.
- **A widely-quoted "93% non-operating share" is not reproducible from any filed period.** The six
  filed-order values are 50.95%, 68.00%, 831.74%, 96.81%, 146.90% and 82.00%. The cited figure's own
  worked example resolves to **82.00%** (Q2 2026) and its own FY2024 table value resolves to **98.49%**
  on either construction (the FY2024 operating line was a loss, so the constructions coincide there) —
  so the claim is internally inconsistent as well as externally unreproducible. **Withdrawn.** Grade:
  DEMONSTRATED (refutation).
- **A widely-quoted "7.4% operating margin" is the absolute value of an operating loss.** Q2 2026's
  operating margin is **(7.37)%** — the served +4,775 on 64,772 would give 7.37%, and 4,775 ÷ 64,772 =
  7.3720% exactly. The published figure is therefore a **DA-23 strip propagated into a derived
  margin**: the sign was dropped in the row layer and the derived metric never had a chance.
  Grade: DEMONSTRATED (refutation).
- **The "$2,137M accumulated deficit" is the wrong balance-sheet date.** The accumulated deficit is
  filed as **$(2,206,570) thousand at 2026-06-30** and **$(2,136,797) thousand at 2025-12-31**
  ([📄 GSAT 10-Q p.6](https://agentii.ai/v/GSAT/sec166/6)). The quoted $2,137M is the **December 31,
  2025** column, presented as current; the deficit has since grown by **$69,773 thousand (+3.3%)**.
  Grade: DEMONSTRATED (refutation).

Two further DA-30 notes on the balance sheet, for the pilot's benefit: the deficit and equity figures
are **6-month and instant-date** measures while the income series is quarterly, and the served
`RetainedEarningsAccumulatedDeficit` facts are all positive (§1.4) — so a reader taking the balance
sheet from the served layer would read solvency backwards **and** at the wrong date.

## 2.3 Period bases must be stated with any share or growth metric

**Revenue, two bases, opposite signs** — verbatim: *"For the three months ended June 30, 2026, total
revenue decreased 3% to $64.8 million ... For the six months ended June 30, 2026, total revenue
increased 6% to $134.8 million"*
([📄 GSAT 10-Q p.32](https://agentii.ai/v/GSAT/sec166/32)). Recomputed on filed cells: **3M −3.54%**
(64,772 vs 67,148) and **6M +6.02%** (134,836 vs 127,180). **Any GSAT revenue growth figure quoted
without its period basis is ambiguous to the point of being wrong in one of its two readings.**

**The same trap at a revenue line.** The Customer's own line — wholesale capacity services — is
**−5% on 3M and +9% on 6M**; Commercial IoT +7% / +10%; SPOT −7% / −7%; Duplex −26% / −26%;
Government and other +20% / +53%; subscriber equipment +$0.8M / +$1.2M
([📄 GSAT 10-Q p.34](https://agentii.ai/v/GSAT/sec166/34)). The company attributes the swing to
*"the timing and amount of service fees associated with the reimbursement of network-related costs"* —
i.e. **contract mechanics, not demand.** That is the correct reading of this series and it is why the
quarterly revenue line should not be treated as a demand indicator at GSAT.

**Customer-share metric, two bases, and the directions agree here — the levels do not.**
- **SIX months** ended 2026-06-30 and 2025: **64% and 62%** — verbatim
  ([📄 GSAT 10-Q p.30](https://agentii.ai/v/GSAT/sec166/30)).
- **THREE months** ended 2026-03-31 and 2025: **66% and 61%** — verbatim
  ([📄 GSAT 10-Q p.26](https://agentii.ai/v/GSAT/sec164/26)).
- The counterparty is named in the Q1 2026 10-Q: *"We provide certain services to Apple Inc. (the
  'Customer')"*, and no other customer exceeds 10% of revenue. Also from the same disclosure: GSAT
  retains **15%** of current and future network capacity, and had approximately **811,000** MSS
  subscribers at 2026-06-30.

**Both bases rise, so unlike SPCX's opposite-signed pair there is no sign trap here — but the LEVELS
differ (66% on 3M, 64% on 6M), so quoting "the customer is 66% of revenue" as a standing figure
over-reads one quarter by 2 percentage points.** State the basis.

# 3. `earnings-vs-consensus`

## 3.1 Revenue: five of five serve-filed matches, and a beat-to-miss reversal

| Quarter | Filed revenue | Calendar revenue | Match | vs estimate | Surprise |
|---|---|---|---|---|---|
| Q2 2025 | 67,148 | 67,148,000 | **exact** | 63,132,500 | **+6.36%** beat |
| Q3 2025 | 73,845 | 73,845,000 | **exact** | 68,924,430 | **+7.14%** beat |
| Q4 2025 | 71,961 ᴰ | 71,961,000 | **exact** | 71,231,650 | **+1.02%** beat |
| Q1 2026 | 70,064 | 70,064,000 | **exact** | 70,923,020 | **−1.21%** miss |
| Q2 2026 | 64,772 | 64,772,000 | **exact** | 71,981,000 | **−10.02%** miss |

The calendar layer's revenue column is the **only** surface in this artifact that is correct on both
sign and magnitude at every row tested, and it **independently corroborates the derived Q4 2025
revenue of 71,961 to the dollar**. Grade: DEMONSTRATED.

**The pattern that matters:** three consecutive beats (+6.36%, +7.14%, +1.02%) followed by two
consecutive misses (−1.21%, −10.02%), with the miss widening **8.3×** in one quarter. The consensus
line was estimating **growth**: the Q2 2026 estimate of 71,981 implies **+7.2%** YoY against a
delivered **−3.5%**. And the revenue miss is concentrated in the Customer's line (wholesale capacity),
consistent with the timing mechanics of §2.3 — the street appears to have modelled the line as a
growth series.

## 3.2 Earnings: the street never modelled a profit, and the misses are absolute

| Quarter | EPS actual | EPS estimate | Absolute miss | Provider surprise % |
|---|---|---|---|---|
| Q2 2025 | $0.13 | $(0.09)$ | **+0.22** beat | +244.44% |
| Q3 2025 | $(0.01)$ | $(0.01)$ | 0.00 | 0.00% |
| Q4 2025 | $(0.07)$ | **$0.01** | **−0.08** | −800.00% |
| Q1 2026 | $(0.16)$ | $(0.04941)$ | **−0.11059** | −223.82% |
| Q2 2026 | $(0.23)$ | $(0.08667)$ | **−0.14333** | −165.37% |

**The estimate was negative in four of the five quarters and the one positive estimate (Q4 2025,
$0.01) was the quarter that missed by the widest absolute margin relative to a near-zero base.**
Grade: DEMONSTRATED (both columns served).

**The percentage column is a DA-25 trap and is not used for any claim in this artifact.** A
percentage surprise computed against a *negative* estimate is a ratio to a denominator whose sign is
itself the story: the +244.44% "beat" in Q2 2025 is 0.22 ÷ 0.09, i.e. it says nothing about a company
that earned $0.13, and the −800% Q4 2025 figure is 0.08 ÷ 0.01, a ratio to a one-cent estimate. These
are normalised metrics that are **not reproducible from any audited table** — the filed tables publish
per-share amounts, not estimate-relative ratios — so the **absolute miss** is the only admissible
statistic. Note also the estimates' precision (−0.08667; −0.04941), which implies a **thin mean of a
few analysts**: at a loss-making issuer with one customer at 64% of revenue, the consensus base is
fragile in a way the surprise percentage hides rather than reveals.

**Two of the five EPS magnitudes are not reproducible** on the calendar layer (Q1 2025 −0.13419,
Q4 2025 −0.07; §1.5). Do not quote them as filed EPS.

## 3.3 Forward row (as of `as_of`, an expectation only)

**Q3 2026, report date 2026-11-05: EPS estimate $(0.12)$; revenue estimate $74,452,000.** For scale,
the filed Q3 2025 quarter was 73,845 revenue and $(0.01)$ EPS. The estimate therefore implies a
return to modest YoY growth after the Q2 2026 miss, on a quarter that will be the first full quarter
inside a signed merger agreement. GSAT files **no guidance** — there is no issuer forecast to compare
the consensus against, so "earnings versus consensus" at GSAT is consensus-only. Grade: CLAIMED (a
third-party expectation, which can never satisfy a falsifier).

# 4. DA-24, DA-28, DA-29, DA-30 at GSAT

## 4.1 DA-24 — the CARES Act credits sit inside filed operating expenses (quantified)

**The defining GSAT instance is inverted relative to SATS' impairment charge: it is a credit, not a
charge, and it is government-sourced.** Verbatim: *"In February and May 2025, we received employee
retention credits of $2.0 million and $1.9 million, respectively, under the provisions of the
Coronavirus Aid, Relief and Economic Security Act (the 'CARES Act'). These credits were recognized as
reductions to operating expenses during the first and second quarters of 2025, respectively, with
$1.4 million and $1.3 million allocated to cost of services and $0.6 million for each period
allocated to marketing, general and administrative expense"*
([📄 GSAT 10-Q p.34](https://agentii.ai/v/GSAT/sec166/34)).

| Quarter | Filed opex | Credit embedded | Opex ex-credit (derived) | Filed operating income | OI ex-credit (derived) | Reduction |
|---|---|---|---|---|---|---|
| Q1 2025 | 68,533 | 2,000 | 70,533 | (8,501) | (10,501) | 23.5% deeper loss |
| Q2 2025 | 61,002 | 1,900 | 62,902 | 6,146 | 4,246 | **30.9% lower profit** |

Grade: DEMONSTRATED (the credit amounts, the allocations and the filed cells); the ex-credit columns
are DERIVED arithmetic on those cells. **Consequence for reading the series:** the Q2 2025
comparison quarter — the base of the YoY decline that makes Q2 2026 look catastrophic — was itself
flattered by a non-recurring credit. The deterioration is real; the *rate* of deterioration quoted
against Q2 2025 is overstated. A second instance sits on the other side of the ledger — an **expense**
rather than a credit, and **quantified for Q1 2026**: merger transaction costs inside MG&A, *"totaling
$3.2 million"* ([📄 GSAT 10-Q p.32](https://agentii.ai/v/GSAT/sec164/32)), against a filed Q1 2026
MG&A rise of $3,239 thousand, so the quarter's entire MG&A increase is the transaction's own cost.
The Q2 2026 counterpart is attributed to the same driver but not split
([📄 GSAT 10-Q p.35](https://agentii.ai/v/GSAT/sec166/35)) — §0.2, which carries the correction to
the earlier "CLAIMED, not quantified" grading.

## 4.2 DA-30 — Q1 2026's net loss has two filed bases, and the difference is disclosed

| Basis | Net loss | Where it is filed | Operating income | Revenue | Opex |
|---|---|---|---|---|---|
| **A — as originally reported** | **$(17,420)** | Q1 2026 10-Q income statement, Note 11, and the equity roll-forward to 2026-03-31 | 8,170 | 70,064 | 61,894 |
| **B — conformed in the Q2 2026 10-Q** | **$(14,818)** | implied: 6M 2026 $(41,357) − Q2 2026 $(26,539)$ | 8,170 | 70,064 | 61,894 |

**The $2,602 thousand gap is entirely below the operating line and entirely in one line.** The Q1
2026 10-Q files *"Derivative loss and other (expense) income $(2,558)$"*; the Q2 2026 10-Q's
six-month column carries *"Derivative gain and other income 44"*, and since Q2 2026's own derivative
line is nil, the implied Q1 2026 figure is a **+$44 thousand gain** — a $2,602 thousand difference ✓
exact. Every other line reconciles to the dollar (interest (19,814) both ways; FX (1,621) both ways).

**And the cause is on the filed page**, verbatim: *"Upon adoption of ASU 2025-07 on January 1, 2026,
the embedded derivative within the 2024 Debt Repayment no longer required mark-to-market adjustments.
The $2.6 million loss recorded during the first quarter of 2026 was reclassified back to the
derivative asset and was included in the cumulative retained earnings adjustment in connection with
the adoption of this standard."* ([📄 GSAT 10-Q p.37](https://agentii.ai/v/GSAT/sec166/37)). The
modified-retrospective adoption is disclosed in Note 1's Recently Adopted Accounting Pronouncement
section ([📄 GSAT 10-Q p.11](https://agentii.ai/v/GSAT/sec166/11))
and the derivative asset's disappearance from the balance sheet is visible
([📄 GSAT 10-Q p.6](https://agentii.ai/v/GSAT/sec166/6)).

**Consequences, stated rather than resolved:**

1. **A six-month column that does not equal the sum of its two filed quarters, with the non-closure
   disclosed.** 6M 2026 $(41,357) ≠ Q1 $(17,420) + Q2 $(26,539) = $(43,959)$; the gap is the adoption.
   This is the mirror image of DA-29: here a reconciliation that *fails* is informative precisely
   because the failure is named. Grade: DEMONSTRATED.
2. **The operating series is unaffected.** Revenue, opex and operating income are **identical on both
   bases**, so the §0 headline operating columns and every margin in §2.2 hold without qualification.
   Only the Q1 2026 net-margin and below-the-line figures carry the dual basis, and both are given.
3. **Both bases are reported wherever that quarter appears.** The equity roll-forward of §1.4 shows
   the filed statement of stockholders' equity carried **basis A**, which is why the served row layer
   serves **basis A** — the row layer is not wrong here; it is one of two filed bases, with no basis
   field.

## 4.3 DA-29 — a pass on a stripped value, and a fail whose `computed` reproduces from nothing

`validate_calculation` on accession `0001366868-26-000039` returns **5 pass / 5 warn / 6 fail**.
Two rows are citable, and they fail in opposite directions:

- **A `pass` that is evidence of nothing:** `IncomeLossFromContinuingOperationsBeforeIncomeTaxes...`
  computed = reported = **22,630,000**, diff 0, **pass** — against a filed **$(22,630)$**
  ([📄 GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5)). The zero difference is between two copies
  of the same stripped value. Grade: DEMONSTRATED.
- **A `fail` that is equally uninformative:** `OperatingIncomeLoss` Q2 2026 computed
  **(9,549,000)** vs reported 4,775,000, diff 14,324,000, **fail**. The `reported` is the stripped
  |4,775|, and **the `computed` (9,549,000) reproduces from no filed cell** — a back-solve. A fail is
  as uninformative as a pass.

**The instrument's `reported` column is the row layer re-served and its `computed` column is opaque;
neither column is corroboration.** Nothing in this artifact rests on a validator row except as an
exhibit.

## 4.4 DA-28 — the reverse split, carried

The **1:15 reverse stock split effectuated 2025-02-10** is disclosed in footnote (1) of both 2026
10-Qs and in the FY2025 10-K, in each case stating that prior-period share and per-share amounts have
been adjusted ([📄 GSAT 10-K p.48](https://agentii.ai/v/GSAT/sec128/48)). **Two consequences carried:**
(i) the served 2024 per-share values are not on the filed basis (§1.6), so no share-count detector may
be run on them; (ii) share counts are **not** comparable across the 2024/2025 boundary in the served
layer without an explicit adjustment, and the FY2024/FY2023 WACS of 125,877 / 122,334 thousand are
already restated.

# 5. What is UNEXERCISED

**An unengaged check is not a passed check.** These were not run, and no clean reading is claimed:

- **The balance-sheet sign test beyond the retained deficit.** Only
  `RetainedEarningsAccumulatedDeficit` was pulled as a served series. GSAT's balance sheet also files
  negative or bracketed items elsewhere; the served treatment of those concepts was **not** tested.
  Resolving action: pull the served balance-sheet concept series.
- **The cash-flow statement as a served series.** The statement page has been read and is cited
  ([📄 GSAT 10-Q p.9](https://agentii.ai/v/GSAT/sec166/9) — six months: operating 159,767 against
  209,741 in 2025; investing (208,326) against (271,788); financing 10,570 against (22,024)), but
  **the served concept series was not pulled and no sign test was run on it**, so the DA-23 exposure
  of the cash-flow layer is UNEXERCISED. Resolving action: pull the served cash-flow concept series
  and run §1.1's test.
- **The segment note.** GSAT reports **one** reportable segment (MSS), so a segment-versus-consolidated
  reconciliation test — the most productive DA-24 detector at SATS — **cannot engage here**. It is
  UNEXERCISED by construction, not CLEAN. (MSS-only reporting is stated in Note 1,
  [📄 GSAT 10-Q p.10](https://agentii.ai/v/GSAT/sec166/10).)
- **DA-25 proper.** The DA-25 instance cited in §3.2 is a third-party normalised metric, not an
  issuer-filed per-unit metric; GSAT files no per-unit production metric in the pages read, so the
  issuer-side DA-25 test is UNEXERCISED.
- **The 2023 and earlier quarters.** Not tested; the ten-row test window opens at FY2024 Q1.
- **The ASU 2025-07 cumulative adjustment's composition.** The ~25,814 thousand gap in the deficit
  roll-forward (§1.4) is unresolved on the pages read.

# 6. Sources

All figures are cited in-line and enumerated in the `citations:` block. Filing set:
**sec166** = GSAT Q2 2026 10-Q, accession `0001366868-26-000039`, filed 2026-08-06;
**sec164** = GSAT Q1 2026 10-Q, accession `0001366868-26-000029`, filed 2026-05-07;
**sec163** = GSAT Q3 2025 10-Q, accession `0001366868-25-000113`, filed 2025-11-06;
**sec128** = GSAT FY2025 10-K, accession `0001366868-26-000012`, filed 2026-02-27.

**Exposure index — this artifact's figures against the DA register:**

| DA | Exposure at GSAT | Where |
|---|---|---|
| DA-23 | **HIGH — the defining defect at this issuer** | §1.1–§1.5; 12/12 stripped, 20/20 deficit series, 3-layer split |
| DA-24 | **PRESENT — both directions (a credit in 2025, an expense in 2026)** | §4.1; credits quantified at 2,000 / 1,900 thousand, merger transaction costs at $3.2 million (Q1 2026, p.32) |
| DA-25 | PRESENT only in a third-party normalised metric | §3.2, excluded from claims |
| DA-26 | **PRESENT — two instances, 3.794× and 4.092×** | §2.1 |
| DA-27 | PRESENT but benign in itself (calendar-year filer) | §2.1 |
| DA-28 | **PRESENT — 1:15 reverse split, 2025-02-10** | §1.6, §4.4 |
| DA-29 | PRESENT — one pass on a stripped value, one opaque fail | §4.3 |
| DA-30 | **PRESENT at the FILING level — the largest instance in the artifact** | §4.2, and §2.2 for the derived metric |
