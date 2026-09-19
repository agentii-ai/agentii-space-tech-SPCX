---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: YSS
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
    chosen_reading: "sign strip on negative OperatingIncomeLoss — tested by the component identity (gross profit − opex) on all six periods the 10-Qs present, never by EPS × shares; CONFIRMED six of six, zero exceptions. The Q1 2026 figure 001 flagged ($110.466M) is the SAME defect as the Q2 2026 flip, not a second one."
  - da_id: "DA-24"
    chosen_reading: "disposal gain inside the operating line — REFUTED at YSS: the Solestial remeasurement gain is $0.4M and is stated to sit in other (expense) income, net; the segment reconciliation (sec12 p.35) closes to net loss with no gain line in the operating build"
  - da_id: "DA-25"
    chosen_reading: "issuer-defined metric not reproducible from the segment tables — CONFIRMED on two counts: (a) backlog's per-spacecraft basis is disclosed at exactly one date and never in a 10-Q, so it is unreproducible for both quarters the 10-Qs quote; (b) the non-GAAP contribution-margin table's 6M 2026 direct-material input (129,517) does not tie to the segment table's direct-materials line (129,538), a $21K single-cell break"
  - da_id: "DA-26"
    chosen_reading: "annual value mislabelled as quarterly — NOT TESTABLE at YSS, and the non-testability is an ingestion absence, not a clean screen: the FY2025 10-K is readable as page content (sec8) but carries `processing_status: pending`, no annual fact exists in pipeline.xbrl_facts, and fiscal_period=Q4 and Q3 both return 0 facts. Register as unresolved, not clean."
  - da_id: "DA-27"
    chosen_reading: "fiscal labels generated from the calendar quarter — method CONFIRMED (fiscal_year_end_month_source: gold_companies, a table, with cross_validation_hint null and periods synthesised into FY2027); outcome benign (YSS is a verified Dec-31 filer, so calendar == fiscal)"
  - da_id: "DA-28"
    chosen_reading: "IPO capital-structure discontinuity — CONFIRMED as the per-share failure that is NOT DA-23: the Corporate Conversion forced a retrospective restatement of all pre-IPO share counts to a constructed 95,141,928, and one quarter (Q1 2026) now carries three different per-share values on two live bases plus a sign strip"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: "Q1 2026 consolidated statement of operations: Revenue 116,343; cost of revenues 94,193; gross profit 22,150; SG&A 36,706 + SBC 84,696 + R&D 5,289 + transaction costs 5,925 = total operating expenses 132,616; Loss from operations (110,466); total other expense (4,486); loss before income taxes (114,952); income tax benefit 110; net loss (114,842); accretion 192 + deemed dividend 60,722; net loss available to common (175,756); EPS (1.51); weighted-average shares 116,022,676"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 7
    url: https://agentii.ai/v/YSS/sec9/7
    located_via: read_source_pages
  - figure: "MD&A Results of Operations for Q1 2026: Loss from operations (110,466) stated at (95)% of revenue; the origin of 001's '95% margin'"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 36
    url: https://agentii.ai/v/YSS/sec9/36
    located_via: read_source_pages
  - figure: "Q2 2026 and six-month consolidated statement of operations: Revenue 92,547 / 208,890; cost of revenue 70,367 / 164,560; gross profit 22,180 / 44,330; SG&A 40,825 / 77,531; SBC 10,893 / 95,589; R&D 5,766 / 11,055; transaction costs 6,009 / 11,934; total operating expenses 63,493 / 196,109; loss from operations (41,313) / (151,779); net loss (39,343) / (154,185)"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 7
    url: https://agentii.ai/v/YSS/sec12/7
    located_via: read_source_pages
  - figure: "Segment reporting, significant expenses included within consolidated net loss. Revenue 92,547 / 83,839 / 208,890 / 190,091; Direct materials 53,240 / 63,555 / 129,538 / 134,505; SG&A 40,825 / 25,790 / 77,531 / 52,591; SBC 10,893 / — / 95,589 / —; R&D 5,766 / 4,893 / 11,055 / 9,294; transaction costs 6,009 / 75 / 11,934 / 106; interest expense 2,884 / 7,118 / 5,783 / 14,177; interest income (4,208) / (218) / (8,828) / (759); other expense (income), net (928) / (1,201) / 5,279 / (1,315); income tax expense (benefit) 282 / (2,697) / 172 / (4,003); other segment items 17,127 / 10,758 / 35,022 / 21,458; Net loss (39,343) / (24,234) / (154,185) / (35,963)"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 35
    url: https://agentii.ai/v/YSS/sec12/35
    located_via: read_source_pages
  - figure: "Basic and diluted net loss per share computation. Net loss as reported (39,343) / (24,234) / (154,185) / (35,963); less accretion of Class P Units — / — / 192 / —; less deemed dividend on Class P Unit conversion — / — / 60,722 / —; net loss attributable to common shareholders (39,343) / (24,234) / (215,099) / (35,963); weighted average shares 128,095,949 / 95,141,928 / 122,092,664 / 95,141,928; net loss per share (0.31) / (0.25) / (1.76) / (0.38). Anti-dilutive: RSUs 862,973, RSAs 2,026,896"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 32
    url: https://agentii.ai/v/YSS/sec12/32
    located_via: read_source_pages
  - figure: "Net Loss per Share policy: pre-IPO shares retrospectively adjusted to 95,141,928 as akin to a split-like situation; the Corporate Conversion issued 99,558,713 shares, including 2,269,473 unrestricted shares for vested Incentive Units and 2,147,313 restricted shares for unvested Incentive Units, both excluded from the 2025 denominator"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 31
    url: https://agentii.ai/v/YSS/sec12/31
    located_via: read_source_pages
  - figure: "IPO and Corporate Conversion: common stock began trading on NYSE 2026-01-29; 18.5 million shares at $34.00 for aggregate offering price $629 million; net proceeds $583.4 million after $36.2 million underwriting discounts and commissions and $9.4 million offering costs; Midco II converted to a Delaware corporation on 2026-01-28 and Holdings distributed and liquidated"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 33
    url: https://agentii.ai/v/YSS/sec9/33
    located_via: read_source_pages
  - figure: "Cover pages: 129,694,458 shares of common stock outstanding as of May 12, 2026 (Q1 10-Q); 137,357,605 shares outstanding as of August 12, 2026 (Q2 10-Q)"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 1
    url: https://agentii.ai/v/YSS/sec9/1
    located_via: read_source_pages
  - figure: "Condensed consolidated balance sheet: common units 0 / 50,000,000 and Class P Units 0 / 240,956,348 at 2026-03-31 and 2025-12-31; common stock 0.0001 par, 1,000,000,000 and 0 authorized, 127,609,213 and 0 issued and outstanding; accumulated deficit (383,864) / (269,022); total stockholders' equity/member's capital 1,722,351 / 867,824; total assets 2,049,054 / 1,475,385; total liabilities 326,703 / 464,446"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 6
    url: https://agentii.ai/v/YSS/sec9/6
    located_via: read_source_pages
  - figure: "Backlog table $642,298 at 2026-03-31 and $542,557 at 2025-12-31, with the issuer's definition (aggregate expected revenue of awarded contracts at execution of a legally binding agreement, excludes unexercised options, includes contract liabilities)"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 33
    url: https://agentii.ai/v/YSS/sec9/33
    located_via: read_source_pages
  - figure: "Backlog table $592,049 at 2026-06-30 and $542,557 at 2025-12-31"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 37
    url: https://agentii.ai/v/YSS/sec12/37
    located_via: read_source_pages
  - figure: "Remaining performance obligations $592.0 million as of 2026-06-30 (Q2 10-Q) and $642.3 million as of 2026-03-31 (Q1 10-Q) — identical to the backlog figures at the same dates to the rounding"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 19
    url: https://agentii.ai/v/YSS/sec12/19
    located_via: read_source_pages
  - figure: "Contribution margin (non-GAAP), revenue less direct material costs: 3M 2026 92,547 − 53,240 = 39,307 (42%); 3M 2025 83,839 − 63,555 = 20,284 (24%); 6M 2026 208,890 − 129,517 = 79,373 (38%); 6M 2025 190,091 − 134,505 = 55,586 (29%). The 6M 2026 direct-material figure 129,517 conflicts with 129,538 at page 35"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 45
    url: https://agentii.ai/v/YSS/sec12/45
    located_via: read_source_pages
  - figure: "Solestial remeasurement gain of $0.4 million 'included in other (expense) income, net' — the DA-24 exclusion; consideration $71.7 million ($15.5 million cash and approximately $51.8 million in shares), prior minority investment fair-valued at $4.4 million"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 20
    url: https://agentii.ai/v/YSS/sec12/20
    located_via: read_source_pages
  - figure: "One operating segment and one reportable segment, space infrastructure; measure of segment assets is total assets; CODM is the CEO"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 34
    url: https://agentii.ai/v/YSS/sec12/34
    located_via: read_source_pages
  - figure: "Backlog approximately $543 million and 107 spacecraft as of December 31, 2025; 74 missions flown; 17 products with flight heritage; over four million on-orbit hours; more than 45 ground antennas; 'our price per satellite has been approximately half the price of our competitors'"
    ticker: YSS
    form_type: 10-K
    citation_id: sec8
    page_no: 5
    url: https://agentii.ai/v/YSS/sec8/5
    located_via: read_source_pages
  - figure: "Q1 2026 Adjusted EBITDA reconciliation: EBITDA (100,570) vs 5,519 for Q1 2025; Adjusted EBITDA (3,638) vs 5,454"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 40
    url: https://agentii.ai/v/YSS/sec9/40
    located_via: read_source_pages
  - figure: "Material weakness in internal control over financial reporting disclosed in Part I Item 4"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 46
    url: https://agentii.ai/v/YSS/sec9/46
    located_via: read_source_pages
  - figure: "Q1 2026 contract balances and remaining performance obligations: contract assets 96,573 / 76,809 and contract liabilities 28,565 / 110,275 at 2026-03-31 and 2025-12-31; $95.6 million of Q1 2026 revenue recognized from the opening contract liability balance; net EAC adjustments, before income taxes, $(754) for 3M 2026 against a favourable $565 for 3M 2025, per basic and diluted share $(0.01) against $0.01; RPO $642.3 million at 2026-03-31 with over 55% expected within 12 months"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 17
    url: https://agentii.ai/v/YSS/sec9/17
    located_via: read_source_pages
  - figure: "Q2 2026 cover page: 137,357,605 shares of common stock outstanding as of August 12, 2026 — the count against which the served weighted-average share figures can be bounded"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 1
    url: https://agentii.ai/v/YSS/sec12/1
    located_via: read_source_pages
---

# YSS — Recent-Quarter Defect Census

Accessions: Q1 2026 10-Q `0001628280-26-035244` (`sec9`, filed 2026-05-15, period
2026-03-31, 50 pages); Q2 2026 10-Q `0001628280-26-056874` (`sec12`, filed 2026-08-14,
period 2026-06-30, 56 pages); FY2025 10-K `0001628280-26-019923` (`sec8`, filed
2026-03-20). This artifact tests 001's YSS figures and answers spec Q-3.

---

## 0. The headline, resolved

**The $110.466M is not a margin. It is a sign-stripped operating LOSS of $(110,466)K.**

The Q1 2026 10-Q prints, for the three months ended March 31, 2026
([📄 YSS 10-Q p.7](https://agentii.ai/v/YSS/sec9/7)):

| Line | Filed |
|---|---|
| Revenue, net | $116,343 |
| Cost of revenues | 94,193 |
| **Gross profit** | **22,150** |
| Selling, general and administrative | 36,706 |
| Stock-based compensation expense | 84,696 |
| Research and development | 5,289 |
| Transaction costs | 5,925 |
| **Total operating expenses** | **132,616** |
| **Loss from operations** | **(110,466)** |
| Total other expense | (4,486) |
| Loss before income taxes | (114,952) |
| Income tax benefit | 110 |
| **Net loss** | **(114,842)** |
| Less: accretion of Class P Units | 192 |
| Less: deemed dividend on Class P Unit conversion | 60,722 |
| **Net loss available to common shareholders** | **(175,756)** |
| Net loss per share | **$(1.51)** |
| Weighted-average shares, basic and diluted | 116,022,676 |

**Component identity, in-line: 22,150 − 132,616 = (110,466).** Exact.

The MD&A table at [📄 YSS 10-Q p.36](https://agentii.ai/v/YSS/sec9/36) prints the same
figure as **(110,466)** at **(95%)** of revenue. 001's "95% margin" is that filed
**(95)%** with the minus dropped. There is no 95% margin; there is a **−95% operating
margin**, and it is the largest in the issuer's history because of a one-time charge
(§3 below), not because of a change in the manufacturing spread.

### One defect or two? **One.**

Both statements are **DA-23**. The Q2 2026 "flip" and the Q1 2026 "95% margin" are the
same mechanism — `us-gaap:OperatingIncomeLoss` serves the sign-stripped magnitude of a
negative value — observed on two periods of the same issuer. **YSS is one DA-23 register
entry, not two.** The Q1 magnitude that 001 thought "sits outside the pattern's magnitude"
is fully explained by a real $84,696K stock-based compensation charge plus $5,925K of
transaction costs, both genuine, both disclosed, both on the face of the statement.

YSS *does* carry a second register entry, but it is not on the operating line: it is
**DA-28** (§8), and 001 did not look for it.

---

## 1. The governing rule, applied: DA-23 on every quoted period

MRCY's Phase 2 finding is that DA-23 must run on every period an artifact quotes, not
just the headline. The two 10-Qs present **six distinct issuer-periods**. All six are
tested below by the component identity read from the documents.

```text
3M 2026 (sec9 p.7)    gross profit     22,150
                      opex  36,706 + 84,696 + 5,289 + 5,925 = 132,616
                      22,150 − 132,616                     = (110,466)  filed
                      XBRL OperatingIncomeLoss             = +110,466   STRIPPED

3M 2025 (sec9)        revenue 106,252 − COGS 81,650        = 24,602  gross profit
                      opex  26,801 + 0 + 4,401 + 31        = 31,233
                      24,602 − 31,233                      = (6,631)    filed
                      XBRL OperatingIncomeLoss             = +6,631     STRIPPED

3M 2026 (sec12 p.7)   gross profit     22,180
                      opex  40,825 + 10,893 + 5,766 + 6,009 = 63,493
                      22,180 − 63,493                      = (41,313)   filed
                      XBRL OperatingIncomeLoss             = +41,313    STRIPPED

3M 2025 (sec12)       revenue 83,839 − COGS 74,313         = 9,526  gross profit
                      opex  25,790 + 0 + 4,893 + 75        = 30,758
                      9,526 − 30,758                       = (21,232)   filed
                      XBRL OperatingIncomeLoss             = +21,232    STRIPPED

6M 2026 (sec12 p.7)   gross profit     44,330
                      opex  77,531 + 95,589 + 11,055 + 11,934 = 196,109
                      44,330 − 196,109                     = (151,779)  filed
                      XBRL OperatingIncomeLoss             = +151,779   STRIPPED

6M 2025 (sec12)       revenue 190,091 − COGS 155,963       = 34,128  gross profit
                      opex  52,591 + 0 + 9,294 + 106       = 61,991
                      34,128 − 61,991                      = (27,863)   filed
                      XBRL OperatingIncomeLoss             = +27,863    STRIPPED
```

**Six periods, six strips, zero exceptions.** The served `OperatingIncomeLoss` is
positive in every case; the filed value is negative in every case; `|computed| ==
|reported|` holds exactly and the signs are opposite in all six.

Each of the six also closes forward to net loss independently — a second, orthogonal
identity that a magnitude-only test cannot satisfy by accident:

```text
Q1 2026  (110,466) + (4,486) + 110     = (114,842)   sec9 p.7
Q2 2026  (41,313) + 2,252 − 282        = (39,343)    sec12 p.7
Q1 2025  (6,631) + (6,404) + 1,306     = (11,729)    sec9 p.7
Q2 2025  (21,232) + (5,699) + 2,697    = (24,234)    sec12 p.7
6M 2026  (151,779) + (2,234) − 172     = (154,185)   sec12 p.7
6M 2025  (27,863) + (12,103) + 4,003   = (35,963)    sec12 p.7
```

### The Q1 anomaly is confirmed by an independent filing

The strongest available check on the Q1 figure does not come from the Q1 filing. The Q2
10-Q presents a six-month column and a three-month column over the same
[📄 p.7](https://agentii.ai/v/YSS/sec12/7). Subtracting gives Q1 2026 on every line:

```text
revenue   208,890 − 92,547 = 116,343   = sec9 p.7 revenue    ✓
COGS      164,560 − 70,367 =  94,193   = sec9 p.7 COGS       ✓
GP         44,330 − 22,180 =  22,150   = sec9 p.7 gross profit ✓
opex      196,109 − 63,493 = 132,616   = sec9 opex components ✓
operating (151,779) − (41,313) = (110,466) = sec9 filed loss   ✓
```

**Five lines, exact, from a filing published three months later.** The $110,466 loss is
not a transcription artifact of one document; it is corroborated by a second.

### The segment table is an independent third

The segment note's "significant expenses included within consolidated net loss" table
([📄 YSS 10-Q p.35](https://agentii.ai/v/YSS/sec12/35)) is a complete net-loss
reconciliation, and it closes on all four columns:

```text
3M 2026  92,547 − 53,240 − 40,825 − 10,893 − 5,766 − 6,009 − 2,884 + 4,208 + 928 − 282 − 17,127 = (39,343) ✓
3M 2025  83,839 − 63,555 − 25,790 − 0 − 4,893 − 75 − 7,118 + 218 + 1,201 + 2,697 − 10,758        = (24,234) ✓
6M 2026 208,890 − 129,538 − 77,531 − 95,589 − 11,055 − 11,934 − 5,783 + 8,828 − 5,279 − 172 − 35,022 = (154,185) ✓
6M 2025 190,091 − 134,505 − 52,591 − 0 − 9,294 − 106 − 14,177 + 759 + 1,315 + 4,003 − 21,458     = (35,963) ✓
```

and the residual line ties to cost of revenue on all four columns:
`direct materials + other segment items = cost of revenue`
(53,240+17,127 = 70,367; 63,555+10,758 = 74,313; 129,538+35,022 = 164,560;
134,505+21,458 = 155,963 — all exact).

---

## 2. What the instrument served, against what was filed

| Period | Filed (parenthetical = negative) | Served `OperatingIncomeLoss` | Δ |
|---|---|---|---|
| 3M 2026 (Q1 filing) | **(110,466)** | +110,466 | sign only |
| 3M 2025 (Q1 filing) | **(6,631)** | +6,631 | sign only |
| 3M 2026 (Q2 filing) | **(41,313)** | +41,313 | sign only |
| 3M 2025 (Q2 filing) | **(21,232)** | +21,232 | sign only |
| 6M 2026 | **(151,779)** | +151,779 | sign only |
| 6M 2025 | **(27,863)** | +27,863 | sign only |

The negative does not exist at any access level: `include_all_sources=true` returns the
same six positive values and nothing else. **The sign is only in the document.** And the
document's convention is unambiguous on the pages quoted: `Net loss | $ (39,343)`,
`Accumulated deficit | (383,864)`,
`Interest income | (4,208)`
([📄 p.35](https://agentii.ai/v/YSS/sec12/35), [📄 sec9 p.6](https://agentii.ai/v/YSS/sec9/6)).

### The strip does not stop at the operating line

Four further served facts, each checked against a page:

| Fact | Filed | Served | Citation |
|---|---|---|---|
| Net loss, 3M 2025 | **(24,234)** | +24,234 | [sec12 p.35](https://agentii.ai/v/YSS/sec12/35) |
| Net loss, 6M 2026 | **(154,185)** | +154,185 | [sec12 p.35](https://agentii.ai/v/YSS/sec12/35) |
| EPS, 3M 2025 | **$(0.25)** | +0.25 | [sec12 p.32](https://agentii.ai/v/YSS/sec12/32) |
| EPS, 6M 2025 | **$(0.38)** | +0.38 | [sec12 p.32](https://agentii.ai/v/YSS/sec12/32) |
| EPS, 6M 2026 | **$(1.76)** | (not returned; 3M figure +1.51 is) | [sec12 p.32](https://agentii.ai/v/YSS/sec12/32) |
| Accumulated deficit, 2025-12-31 | **(269,022)** | +269,022 | [sec9 p.6](https://agentii.ai/v/YSS/sec9/6) |

**This is the MRCY inversion, live.** The two 2025 comparatives are *loss* periods — net
losses of $(24,234)K and $(35,963)K — and the served EPS for them is **positive**. An
analyst reading the served pair would conclude YSS was *profitable* in H1 2025 and turned
loss-making in 2026. The truth is the opposite direction of travel entirely: H1 2026's net
loss is $(154,185)K against $(35,963)K, a **4.3× widening**.

### The instrument columns on the same filings

`validate_calculation` was run on both 10-Qs. Three rows are load-bearing here.

**Row 1 — a true positive with a correct `computed` side.** sec9,
`OperatingIncomeLoss` 3M 2026: computed **−110,466**, reported **110,466**. The `computed`
column is right; the `reported` column is the stripped one. The platform's own calculation
tree confirms which side to trust: `get_calculation_tree(0001628280-26-035244)` returns
`OperatingIncomeLoss ← GrossProfit (weight 1) + OperatingExpenses (weight −1)`, and
`GrossProfit ← RevenueFromContractWithCustomerExcludingAssessedTax (1) + CostOfRevenue (−1)`,
and `OperatingExpenses ← SG&A (1) + AllocatedShareBasedCompensationExpense (1) + R&D (1) +
yss_TransactionCosts (1)` — **the issuer's linkbase encodes exactly the four-component
identity read off p.7.** The tree and the document agree; `reported` does not.

**Row 2 — the `computed` column inherits the strip.** sec9,
`NetIncomeLossAvailableToCommonStockholdersBasic`: computed **53,928** vs reported
**175,756**. The tree gives
`NetIncomeLossAvailableToCommonStockholdersBasic ← NetIncomeLoss (1) +
TemporaryEquityAccretionToRedemptionValueAdjustment (−1) + TemporaryEquityDividendsAdjustment (−1)`.
The computed side evaluated `114,842 − 60,722 − 192 = 53,928` — **it took the child
`NetIncomeLoss` as +114,842, i.e. it inherited the strip, and so returned a $53.9M profit
for a quarter the filing reports as a $(175.8)M loss to common.** Two independently corrupt
numbers, exactly as the instrument rule predicts. Here they differ in magnitude so `fail`
fires; where the corruption is consistent end to end it does not fire at all (SPCX:
computed = reported = 541, status `pass`, a $541M net loss).

**Row 3 — `pass` beside a corrupted parent.** sec12, `GrossProfit` 3M 2026: computed =
reported = **22,180**, status **`pass`** — in the same run whose parent
`OperatingIncomeLoss` is flipped to +41,313. A passing row certifies the sign of nothing.

**Row 4 — magnitude noise dominates the `fail` bucket.** sec9: pass 12 / warn 3 / fail 11;
sec12: pass 10 / warn 2 / fail 14. In that set,
`BusinessCombinationRecognizedIdentifiableAssetsAcquiredGoodwillAndLiabilitiesAssumedNet`
computes 696,840 against a reported 74,858 (the computed side sums across acquisitions and
measurement dates; `reported` is one column), and sec9's `GrossProfit` 3M 2025 computes
−76,287 against a reported 24,602. These are the incomplete-arc / column-mixing class —
the 93% false-positive class — and they carry no information about YSS.

**Conclusion on the instrument.** `status` is not the detector at YSS and is not
informative here in either direction. The detector that works is the component identity
read from the document, corroborated by the platform's own calculation tree.

---

## 3. DA-23 verdict table, every level

| Level | Periods | Test | Verdict |
|---|---|---|---|
| Consolidated operating line | 6 | `gross profit − opex` vs served | **STRIPPED 6 / 6** |
| Net loss forward-close | 6 | operating + other + tax | **CLOSES 6 / 6** |
| Segment significant-expenses table | 4 | sum of eleven lines to net loss | **CLOSES 4 / 4** |
| Cost-of-revenue decomposition | 4 | direct materials + other segment items | **CLOSES 4 / 4** |
| EPS | 4 | filed `$ (…)` vs served `+` | **STRIPPED 4 / 4** |
| Net loss | 2 checked | filed `(…)` vs served `+` | **STRIPPED 2 / 2** |
| Accumulated deficit | 1 checked | filed `(…)` vs served `+` | **STRIPPED 1 / 1** |
| Balance-sheet identity | 2 | assets − liabilities = equity | **CLOSES 2 / 2** (2,049,054 − 326,703 = 1,722,351; 2,070,219 − 324,412 = 1,745,807) |

**Why the gross-profit bound is not a detector here.** The bound (operating income must
not exceed gross profit) would have caught the SPCX-class inflation. At YSS it is worse
than useless: the served Q1 figure of +110,466 exceeds filed gross profit of 22,150 by
**5.0×**, and the served Q2 figure of +41,313 exceeds filed gross profit of 22,180 by
1.9×. A bound test does fire at YSS. But it fires on the *served* side, and 001's own
artifact read the served side, saw the number, and correctly called it implausible without
being able to resolve it. The bound flags; only the component identity resolves.

---

## 4. DA-24 — disposal gain inside the operating line: **REFUTED**

The Solestial acquisition closed 2026-06-04 with the prior minority investment
fair-valued at $4.4M at close, producing a gain of **$0.4 million** which the filing states
is *"included in other (expense) income, net on the unaudited condensed consolidated
statement of operations and comprehensive loss"*
([📄 YSS 10-Q p.20](https://agentii.ai/v/YSS/sec12/20)). The six-month other-expense move
is explained at [📄 p.45](https://agentii.ai/v/YSS/sec12/45) as *"a loss on derivative
liability associated with the Class P Units fair value adjustment as well as a loss from our
initial investment in Orbion, offset by a gain from our initial investment in Solestial."*

The segment table at [📄 p.35](https://agentii.ai/v/YSS/sec12/35) closes to net loss with no
gain line anywhere in the operating build: every one of the eleven lines is a revenue, a
cost, or an interest/tax item, and the residual "other segment items" is defined as *"other
costs of revenue excluding direct materials, including direct labor, overhead costs and
depreciation and amortization"* — and it equals `cost of revenue − direct materials`
exactly on all four columns. **There is no room in the operating line for a gain.**
DA-24 REFUTED, with an arithmetic proof rather than a prose one.

Note also that the loss-contract charges run the other way: $5.5M and $2.1M for 6M 2026 and
2025, and no charge for 3M 2026 ([📄 p.19](https://agentii.ai/v/YSS/sec12/19)) — these
*reduce* the operating line and are disclosed inside cost of revenues.

---

## 5. DA-25 — issuer-defined metric not reproducible: **CONFIRMED, twice**

### (a) The per-spacecraft basis exists at exactly one date

YSS's backlog is issuer-defined and stated as a dollar figure in both 10-Qs:
**$642,298K at 2026-03-31** and $542,557K at 2025-12-31
([📄 sec9 p.33](https://agentii.ai/v/YSS/sec9/33)); **$592,049K at 2026-06-30** and
$542,557K at 2025-12-31 ([📄 sec12 p.37](https://agentii.ai/v/YSS/sec12/37)). The
definition is explicit — aggregate expected revenue of awarded contracts at execution of a
legally binding agreement, unexercised options excluded, contract liabilities included.

**A unit denominator is disclosed exactly once, in the 10-K, for one date:**
*"growing our backlog to approximately $543 million and **107 spacecraft** as of December
31, 2025"* ([📄 YSS 10-K p.5](https://agentii.ai/v/YSS/sec8/5)). Neither 10-Q discloses a
spacecraft count in its backlog section. So:

```text
2025-12-31   $542,557K / 107 spacecraft = $5,070K per spacecraft   REPRODUCIBLE
2026-03-31   $642,298K / ?              = not computable           UNREPRODUCIBLE
2026-06-30   $592,049K / ?              = not computable           UNREPRODUCIBLE
```

**The per-unit metric is unreproducible by construction for both periods the 10-Qs quote**,
because the denominator is not disclosed. **DA-25 CONFIRMED** on the per-unit limb. The
detector that settles it is a per-unit reproducibility check: divide each disclosed backlog
dollar figure by its disclosed unit count and report which dates lack a denominator. It
needs no segment split and no judgement.

Two further observations inside the same limbs:

- **Backlog equals RPO to the rounding.** RPO is $642.3M at 2026-03-31
  ([📄 sec9 p.17](https://agentii.ai/v/YSS/sec9/17)) and $592.0M at 2026-06-30
  ([📄 sec12 p.19](https://agentii.ai/v/YSS/sec12/19)) — the same figures as backlog at the
  same dates. Two differently-worded definitions, two dates, identical numbers, no
  reconciliation disclosed. This makes the metric *reproducible* (it ties to the ASC 606
  RPO note) while concealing that the issuer's "backlog" is its RPO under another name.
- **The 10-K discloses a comparative price claim with no table behind it**: *"our price per
  satellite has been approximately half the price of our competitors"*
  ([📄 p.5](https://agentii.ai/v/YSS/sec8/5)). That is a per-unit claim with no disclosed
  denominator, no comparator set, and no period. **Grade it CLAIMED, not DEMONSTRATED**, and
  do not let it enter any cost-per-unit series.

### (b) A non-GAAP metric whose input does not tie to the segment table

The contribution-margin table at [📄 sec12 p.45](https://agentii.ai/v/YSS/sec12/45) defines
the metric as revenue less direct material costs, and computes 6M 2026 as
`208,890 − 129,517 = 79,373`. **The segment table's direct-materials line for 6M 2026 is
129,538** ([📄 p.35](https://agentii.ai/v/YSS/sec12/35)) — a **$21K** discrepancy on one
cell. Every other cell agrees exactly (53,240 / 63,555 / 134,505 appear identically in both
tables).

The segment table's figure is the one that reconciles: with 129,538 the eleven-line sum
closes to $(154,185) exactly, and `129,538 + 35,022 = 164,560` equals filed cost of revenue
exactly. Both identities fail on 129,517. So the non-GAAP metric's stated input is $21K
below the only figure in the filing that ties, and the disclosed contribution margin for
6M 2026 should be $79,352K, not $79,373K. **Immaterial in magnitude (0.016%) but exact in
kind** — DA-25's shape is a metric whose inputs do not reproduce from the tables.

**Detector:** a cross-table same-name identity check within a single filing — require the
input named in a non-GAAP reconciliation to equal the identically-named line in the notes,
to the dollar.

---

## 6. DA-26 — annual mislabelled as quarterly: **NOT TESTABLE, and the gap is ingestion**

YSS is one of the few issuers in the universe with a 10-K, so the screen should be
runnable. It is not.

- `search_xbrl_facts(YSS, fiscal_period="Q4")` returns **0 facts**. `Q3` also returns **0**.
- `search_xbrl_facts(YSS, fiscal_period="FY")` returns **469 facts** spanning twelve pages —
  and the facts returned carry **three-month and six-month durations**
  (`period_start 2025-04-01 → period_end 2025-06-30`), i.e. the filter does not
  discriminate. Same behaviour as SPCX.
- `get_company_financials(YSS, fiscal_year=2025)` returns **no 10-K at all** — five FY2026
  filings only.
- The 10-K record itself carries **`"processing_status": "pending"`**
  (`search_sec_filings`, accession `0001628280-26-019923`, citation `sec8`), even though its
  **page content is fully readable** — p.5 returns normal text, and the figures on it are
  quotable.

**So the absence of a Q4 fact is an ingestion absence, not a clean screen.** No annual
YSS fact exists in `pipeline.xbrl_facts` for the DA-26 test to mislabel. This is the
instrument-rule failure mode #4 (a NO RESULT that is an absence, not a value), occurring one
layer below the calculation check: **the corpus indexes the document but never extracted
its facts.** Recording DA-26 as "clean at YSS" would be exactly the error the register
exists to prevent. **Outcome: promoted to a registered open candidate, class
UNRESOLVABLE-FROM-PLATFORM for this ticker** — the remedy is ingestion of the FY2025 10-K
(`sec8`), after which the annual-versus-quarterly label screen can run.

The annual values themselves are readable from the document and were not needed to resolve
this artifact; FY2025 revenue was not extracted.

---

## 7. DA-27 — fiscal labels from the calendar quarter: **method CONFIRMED, outcome benign**

`get_company_fiscal_calendar(YSS)` returns `fiscal_year_end_month: 12`,
`fiscal_year_end_month_source: "gold_companies"`, `cross_validation_hint: null`, and
synthesises FY2027 Q1–Q4 out to 2027-12-31. The label therefore originates in a registry
table, not in a filing — **DA-27's method is present at YSS**, and note that the source is
`gold_companies` whereas SPCX's was `default`: two different table-derived paths reaching
the same non-filing origin.

**Outcome benign**: YSS is a verified December-31 filer — the 10-Qs are for the three months
ended March 31 and June 30 ([📄 sec9 p.7](https://agentii.ai/v/YSS/sec9/7),
[📄 sec12 p.7](https://agentii.ai/v/YSS/sec12/7)), and the Q1 10-Q cites *"the Company's 2025
Annual Report on Form 10-K, filed with the SEC on March 19, 2026."* For a calendar-year
filer, calendar quarter == fiscal quarter and the wrong method produces the right label.

**Method and outcome recorded separately**, as at SPCX. Method defect live; outcome correct
by coincidence.

---

## 8. DA-28 — IPO capital-structure discontinuity: **CONFIRMED. This is the per-share failure that is not DA-23.**

YSS's listing is the cleanest DA-28 test case in the universe because the discontinuity is
**inside the financial statements**, not merely above them.

### The mechanism, in the filing's own words

*"Prior to January 28, 2026, we operated as a Delaware limited liability company under the
name Yellowstone Midco Holdings II, LLC … On January 28, 2026 … Midco II converted into a
Delaware corporation pursuant to a statutory conversion … all units of Midco II were
converted into shares of the Company's common stock, and immediately following the
Corporate Conversion, Holdings distributed all shares … to its limited partners and
liquidated."* ([📄 YSS 10-Q p.33](https://agentii.ai/v/YSS/sec9/33))

The IPO followed on 2026-01-29: common stock began trading on the NYSE, 18.5 million shares
at $34.00, aggregate offering price $629 million, net proceeds $583.4 million after
$36.2 million of underwriting discounts and commissions and $9.4 million of offering costs
([📄 p.33](https://agentii.ai/v/YSS/sec9/33)).

### The denominator is constructed, and the filing says so

*"The conversion of common units into common stock which occurred as part of the Corporate
Conversion is considered akin to a split-like situation. For calculation of net loss per
share, shares outstanding for all historical periods before our IPO have been retrospectively
adjusted to 95,141,928 … the Corporate Conversion resulted in the issuance of 99,558,713
shares … However, this amount includes 2,269,473 shares of unrestricted common stock
distributed in respect of vested Incentive Units and 2,147,313 shares of restricted stock
distributed in respect of unvested Incentive Units. As the distribution … is not considered
akin to a split-like situation, these shares were excluded from shares outstanding in the
calculation of net loss per share for the three and six months ended June 30, 2025 and are
only included as outstanding shares prospectively from the vesting date."*
([📄 YSS 10-Q p.31](https://agentii.ai/v/YSS/sec12/31))

**A judgement call determines the historical denominator.** Every pre-IPO per-share figure
in this issuer's record rests on a constructed 95,141,928 whose construction required the
issuer to decide which Incentive-Unit shares were "akin to a split" and which were not.
This is the DA-28 capital-structure discontinuity stated as a disclosure, and it is the
mechanism the register's DA-28 records.

### Every disagreeing share count on the record

| Date | Count | Basis | Citation |
|---|---|---|---|
| 2025-12-31 | 50,000,000 | common **units** outstanding (LLC) | [sec9 p.6](https://agentii.ai/v/YSS/sec9/6) |
| 2025-12-31 | 240,956,348 | Class P **units** outstanding | [sec9 p.6](https://agentii.ai/v/YSS/sec9/6) |
| 2025-12-31 | 95,141,928 | retrospective as-if share count for EPS | [sec12 p.31](https://agentii.ai/v/YSS/sec12/31) |
| 2026-03-31 | 127,609,213 | common shares issued and outstanding | [sec9 p.6](https://agentii.ai/v/YSS/sec9/6) |
| 2026-03-31 | 116,022,676 | weighted average, basic = diluted | [sec9 p.7](https://agentii.ai/v/YSS/sec9/7) |
| 2026-05-12 | 129,694,458 | cover page count | [sec9 p.1](https://agentii.ai/v/YSS/sec9/1) |
| 2026-06-30 | 128,095,949 | weighted average, basic = diluted | [sec12 p.32](https://agentii.ai/v/YSS/sec12/32) |
| 2026-06-30 | 122,092,664 | weighted average, six months | [sec12 p.32](https://agentii.ai/v/YSS/sec12/32) |
| 2026-08-12 | 137,357,605 | cover page count | [sec12 p.1](https://agentii.ai/v/YSS/sec12/1) |

**Seven counts inside the 2026 calendar year alone, on four bases: units, shares
outstanding, weighted-average, and retrospective as-if.** Plus the served
`CommonStockSharesIssued`/`CommonStockSharesOutstanding` of **0** at 2025-12-31 — which is
**not a defect**: the pre-conversion entity had units, not shares. A share-count-based test
that treats the served zero as a data error will "correct" a correct value.

### One quarter, three published per-share values

Q1 2026 net loss is $(114,842)K as reported
([📄 sec12 p.35](https://agentii.ai/v/YSS/sec12/35)) and $(175,756)K attributable to common
shareholders after $192K of Class P accretion and a $60,722K deemed dividend on conversion
([📄 sec9 p.7](https://agentii.ai/v/YSS/sec9/7)). Q2 2026 carries no accretion and no
deemed dividend ([📄 sec12 p.32](https://agentii.ai/v/YSS/sec12/32)) — **the discontinuity
is period-specific, DA-28's signature.**

From that, three values circulate for one quarter:

| Value | Numerator | Basis | Source |
|---|---|---|---|
| **$(1.51)** | (175,756) | net loss attributable to common ÷ 116,022,676 | [sec9 p.7](https://agentii.ai/v/YSS/sec9/7) |
| **$(1.76)** | (215,099) | six-month basis ÷ 122,092,664 | [sec12 p.32](https://agentii.ai/v/YSS/sec12/32) |
| **+1.51** | — | sign-stripped | XBRL served |
| **−0.99** | (114,842) | net loss *as reported* ÷ 116,022,676 | earnings calendar, report_date 2026-05-14 |

The calendar's −0.99 is **not a defect**: it is the "net loss as reported" basis, correctly
signed, and it reconciles to $114,842/116,022,676 = 0.9898. It is a **competing basis**, and
under the §1c `no_single_basis_collapse` rule an artifact quoting Q1 2026 EPS must report
both — the calendar basis (−0.99, as reported) and the filing basis ($(1.51), attributable
to common). The difference between them is entirely the $60,722K deemed dividend, which is
an artifact of the listing, not of operations.

### `EPS × shares` is not merely inadmissible — it is inverted, and here it is provable twice

The instruction is to read only the `computed` vs `reported` pair through the component
identity. YSS shows why in arithmetic:

```text
served EPS 1.51 × served shares 116,022,676   = +175.2M   PROFIT
filed net loss attributable to common         = (175.8M)  LOSS
                                  sign inverted; magnitude nearly exact

served EPS 1.51 × served shares 116,022,676,000 = +175,194M  (1000× on top)
served EPS 0.25 × filed shares  95,141,928      = +23.8M    PROFIT
filed net loss, 3M 2025                         = (24.2M)   LOSS
```

**Both inputs are independently sign-stripped, so the product is a profit for every period
in the record.** An analyst using `EPS × shares` would report YSS as profitable in H1 2026.

### A new defect class, not in the register: 1000× scale on weighted-average share facts

`WeightedAverageNumberOfSharesOutstandingBasic` is served **three orders of magnitude too
large in the Q1 10-Q only**:

| Period | Filed | Served (sec9) | Served (sec12) |
|---|---|---|---|
| 3M 2026 | 116,022,676 | **116,022,676,000** | 128,095,949 (Q2) — correct |
| 3M 2025 | 95,141,928 | **95,141,928,000** | 95,141,928 — correct |
| 6M 2025 | 95,141,928 | (not in Q1 filing) | 95,141,928 — correct |

**The decisive control: the same concept for the same period (3M 2025 = 95,141,928) is
served correctly in the Q2 filing and 1000× in the Q1 filing.** The defect follows the
**filing**, not the concept or the period. EPS in the same Q1 filing is *not* scaled
(1.51, not 1,510), so it is not a blanket scale on the document. And `search_xbrl_facts`
returns 116022676**000** as the stored `value_numeric`, so this is a fact-level defect, not
a rendering one.

**Promote as a registered candidate with the detector named: a per-fact units-and-scale
assertion** — for every `xbrli:shares` fact, require the served magnitude to fall inside a
plausible band for the concept (weighted-average shares within, say, 1×–10× the cover-page
count), and flag any fact whose served value differs from the same concept in a *later*
filing of the same issuer for an overlapping period. That second check is the one that
catches this, and it caught it here.

---

## 9. Instrument observations outside the six DAs

1. **The platform's calculation tree is correct where the `reported` column is not.**
   `get_calculation_tree` returns the issuer's own four-component opex arc set and the
   `GrossProfit − OperatingExpenses` arc with the right weights. The tree is trustworthy at
   YSS; the `reported` column is not. This inverts the usual assumption.
2. **A concept with two home roles.** `AllocatedShareBasedCompensationExpense` is a child of
   `OperatingExpenses` in the income-statement role *and* a child of `NetIncomeLoss` in
   `SegmentReportingScheduleofSegmentSignificantExpensesDetails`. The segment role puts
   **eleven arcs into `NetIncomeLoss`** — the VRT-class hazard ("NO RESULT for a concept with
   seven arcs into it") is present at YSS at a higher arity. Any check that resolves a concept
   by its role must not assume the income-statement role wins.
3. **The segment table is a net-loss reconciliation, not a segment table.** In a
   single-segment issuer it has no segment columns at all — it is a cost decomposition of
   consolidated net loss. Any DA-25 screen that assumes "segment tables" means revenue and
   profit by segment will not find this table's components at all.
4. **`fiscal_period` filters do not discriminate.** `FY` returns 3M and 6M durations; `Q4`
   and `Q3` return nothing; `Q1` returns 199 facts, all from the Q1 filing. The filter is
   filing-scoped in practice and period-labelled only incidentally.
5. **A readable document with `processing_status: pending`.** `sec8` serves full page text
   and no facts. "No facts" and "not readable" are different states and must not be conflated
   — the DA-26 test above turns on exactly this distinction.

---

## Carry-forwards

1. **YSS is ONE DA-23 register entry, not two.** The Q1 2026 $110.466M and the Q2 2026 flip
   are the same mechanism on two periods. Record one entry covering six periods.
2. **YSS adds a DA-28 register entry.** The IPO discontinuity is real, is disclosed as a
   constructed retrospective denominator, and produces three per-share values for one
   quarter on two live bases. This is a *second* register entry for the same issuer, on a
   different line — 001's carry-forward 2 asked whether Q1 was a different defect class; it
   is not, and the different defect class is DA-28.
3. **DA-26 is unresolved at YSS and the cause is ingestion.** The FY2025 10-K (`sec8`) is
   readable but `processing_status: pending`, so no annual fact exists to mislabel. Do not
   record YSS as clean on DA-26. Adds one issuer-quarter to PIL-3's unresolved count.
4. **New register candidate: 1000× scale on `xbrli:shares` facts, filing-specific.** Detector:
   cross-filing same-concept-overlapping-period comparison, plus a plausibility band against
   the cover-page count.
5. **New register candidate: non-GAAP input that does not tie to the notes.** Detector:
   cross-table same-name identity within one filing, to the dollar. The YSS instance is $21K;
   the SPCX/NVDA instances are not.
6. **The `reported` column inherits sign strips from its children.** A `computed` value is
   only as signed as its inputs. Do not treat `computed` as authoritative without the tree.
7. **001's DA-28 exposure is unaddressed.** 001's YSS artifact records revenue, gross margin
   and opex but no share count, no EPS basis, and no mention of the listing that occurred
   seven weeks before the quarter it analyses.

---

## Could not be verified

- **FY2025 annual figures.** The 10-K's facts are not in the platform
  (`processing_status: pending`); only its page text is. FY2025 revenue and EPS were not
  extracted, so DA-26 could not be run even from the document within this pass.
- **`validate_calculation`'s `reported` basis for the `NetIncomeLossAvailableToCommon…` row.**
  The computed side was reproduced exactly (114,842 − 60,722 − 192 = 53,928) but why
  `reported` shows 175,756 rather than 53,928 or 175,756-with-sign was not established;
  the row is recorded, not diagnosed.
- **The Class P derivative liability's journey to zero.** $93,411K at 2025-12-31
  ([📄 sec9 p.6](https://agentii.ai/v/YSS/sec9/6)) against a $4.7M remeasurement loss and a
  $98.1M Level 3 fair value in the Q2 filing's note (sec12 p.33 per the page index). The
  extinguishing entries were not read and the DA-28 bridge through temporary equity is
  therefore recorded but not closed.
- **Whether the platform's `fiscal_period="Q1"` label set is generated or filed.** 199 facts
  came back from the Q1 filing, but whether the label is read from the filing or assigned
  from the report date was not established — the DA-27 test at issuer level passes either
  way for a calendar-year filer.
- **The 107-spacecraft count for any 2026 date.** No 10-Q discloses a backlog unit count, so
  the per-unit metric could not be computed for Q1 or Q2 2026 at all.
- **Sec9 pages 38, 39, 41 and the FY2026 Q1 earnings-call transcript** were not read; the
  EBITDA/Adjusted EBITDA figures cited come from p.40 and are unaudited non-GAAP by the
  issuer's own label.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Q1 2026 consolidated statement of operations: Revenue 116,343; cost of revenues 94,193; gross profit 22,150; SG&A 36,706 + SBC 84,696 + R&D 5,289 + tr | [📄 YSS 10-Q p.7](https://agentii.ai/v/YSS/sec9/7) |
| MD&A Results of Operations for Q1 2026: Loss from operations (110,466) stated at (95)% of revenue; the origin of 001's '95% margin' | [📄 YSS 10-Q p.36](https://agentii.ai/v/YSS/sec9/36) |
| Q2 2026 and six-month consolidated statement of operations: Revenue 92,547 / 208,890; cost of revenue 70,367 / 164,560; gross profit 22,180 / 44,330;  | [📄 YSS 10-Q p.7](https://agentii.ai/v/YSS/sec12/7) |
| Segment reporting, significant expenses included within consolidated net loss. Revenue 92,547 / 83,839 / 208,890 / 190,091; Direct materials 53,240 /  | [📄 YSS 10-Q p.35](https://agentii.ai/v/YSS/sec12/35) |
| Basic and diluted net loss per share computation. Net loss as reported (39,343) / (24,234) / (154,185) / (35,963); less accretion of Class P Units — / | [📄 YSS 10-Q p.32](https://agentii.ai/v/YSS/sec12/32) |
| Net Loss per Share policy: pre-IPO shares retrospectively adjusted to 95,141,928 as akin to a split-like situation; the Corporate Conversion issued 99 | [📄 YSS 10-Q p.31](https://agentii.ai/v/YSS/sec12/31) |
| IPO and Corporate Conversion: common stock began trading on NYSE 2026-01-29; 18.5 million shares at $34.00 for aggregate offering price $629 million;  | [📄 YSS 10-Q p.33](https://agentii.ai/v/YSS/sec9/33) |
| Cover pages: 129,694,458 shares of common stock outstanding as of May 12, 2026 (Q1 10-Q); 137,357,605 shares outstanding as of August 12, 2026 (Q2 10- | [📄 YSS 10-Q p.1](https://agentii.ai/v/YSS/sec9/1) |
| Condensed consolidated balance sheet: common units 0 / 50,000,000 and Class P Units 0 / 240,956,348 at 2026-03-31 and 2025-12-31; common stock 0.0001  | [📄 YSS 10-Q p.6](https://agentii.ai/v/YSS/sec9/6) |
| Backlog table $642,298 at 2026-03-31 and $542,557 at 2025-12-31, with the issuer's definition (aggregate expected revenue of awarded contracts at exec | [📄 YSS 10-Q p.33](https://agentii.ai/v/YSS/sec9/33) |
| Backlog table $592,049 at 2026-06-30 and $542,557 at 2025-12-31 | [📄 YSS 10-Q p.37](https://agentii.ai/v/YSS/sec12/37) |
| Remaining performance obligations $592.0 million as of 2026-06-30 (Q2 10-Q) and $642.3 million as of 2026-03-31 (Q1 10-Q) — identical to the backlog f | [📄 YSS 10-Q p.19](https://agentii.ai/v/YSS/sec12/19) |
| Contribution margin (non-GAAP), revenue less direct material costs: 3M 2026 92,547 − 53,240 = 39,307 (42%); 3M 2025 83,839 − 63,555 = 20,284 (24%); 6M | [📄 YSS 10-Q p.45](https://agentii.ai/v/YSS/sec12/45) |
| Solestial remeasurement gain of $0.4 million 'included in other (expense) income, net' — the DA-24 exclusion; consideration $71.7 million ($15.5 milli | [📄 YSS 10-Q p.20](https://agentii.ai/v/YSS/sec12/20) |
| One operating segment and one reportable segment, space infrastructure; measure of segment assets is total assets; CODM is the CEO | [📄 YSS 10-Q p.34](https://agentii.ai/v/YSS/sec12/34) **(newly surfaced)** |
| Backlog approximately $543 million and 107 spacecraft as of December 31, 2025; 74 missions flown; 17 products with flight heritage; over four million  | [📄 YSS 10-K p.5](https://agentii.ai/v/YSS/sec8/5) |
| Q1 2026 Adjusted EBITDA reconciliation: EBITDA (100,570) vs 5,519 for Q1 2025; Adjusted EBITDA (3,638) vs 5,454 | [📄 YSS 10-Q p.40](https://agentii.ai/v/YSS/sec9/40) **(newly surfaced)** |
| Material weakness in internal control over financial reporting disclosed in Part I Item 4 | [📄 YSS 10-Q p.46](https://agentii.ai/v/YSS/sec9/46) **(newly surfaced)** |
