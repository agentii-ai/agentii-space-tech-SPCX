---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: YSS
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-12"
    chosen_reading: "constellation size — YSS is a manufacturer, not an operator; it flies spacecraft it does not operate as a service. N/A, and unchanged from 001."
  - da_id: "DA-13"
    chosen_reading: "production rate — 001's reading ('YSS discloses revenue, not unit counts') is REFUTED. YSS discloses 107 spacecraft in backlog, 74 missions flown, 17 products with flight heritage, more than 45 ground antennas, and a stated capacity target of over 1,000 satellites annually. What it does NOT disclose is a per-period manufactured-versus-launched rate — that narrower gap is what remains."
  - da_id: "DA-21"
    chosen_reading: "one operating segment and one reportable segment, space infrastructure (sec12 p.34). CONFIRMED, and note the consequence: the 'segment table' is a consolidated net-loss cost decomposition with no segment columns, so any DA-25 screen that requires segment splits cannot find its components."
  - da_id: "DA-23"
    chosen_reading: "sign strip on negative OperatingIncomeLoss — tested by the component identity (gross profit − opex) on all six periods quoted here, never by EPS × shares; CONFIRMED. The $110.466M Q1 figure 001 flagged as a 95% 'margin' is a sign-stripped $(110,466)K operating LOSS, and the 95% is the filed (95)% with the minus dropped."
  - da_id: "DA-25"
    chosen_reading: "issuer-defined metric not reproducible from the segment tables — CONFIRMED on the per-unit limb: backlog is disclosed in dollars at three dates but with a spacecraft denominator at exactly one date, so the per-spacecraft basis is unreproducible for both quarters the 10-Qs quote. Also CONFIRMED in weak form on the non-GAAP contribution margin, whose 6M 2026 direct-material input is $21K below the only figure in the filing that reconciles."
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: "Q1 2026 income statement: Revenue 116,343; cost of revenues 94,193; gross profit 22,150; SG&A 36,706 + SBC 84,696 + R&D 5,289 + transaction costs 5,925 = total operating expenses 132,616; loss from operations (110,466); net loss (114,842) / (175,756) available to common; EPS (1.51); weighted-average shares 116,022,676"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 7
    url: https://agentii.ai/v/YSS/sec9/7
    located_via: read_source_pages
  - figure: "MD&A for Q1 2026: loss from operations (110,466) at (95)% of revenue — the source of 001's '95% margin'"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 36
    url: https://agentii.ai/v/YSS/sec9/36
    located_via: read_source_pages
  - figure: "Q2 2026 and six-month income statement: Revenue 92,547 / 208,890; cost of revenue 70,367 / 164,560; gross profit 22,180 / 44,330; SG&A 40,825 / 77,531; SBC 10,893 / 95,589; R&D 5,766 / 11,055; transaction costs 6,009 / 11,934; total operating expenses 63,493 / 196,109; loss from operations (41,313) / (151,779)"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 7
    url: https://agentii.ai/v/YSS/sec12/7
    located_via: read_source_pages
  - figure: "Segment significant-expenses table: Revenue 92,547 / 83,839 / 208,890 / 190,091; Direct materials 53,240 / 63,555 / 129,538 / 134,505; other segment items 17,127 / 10,758 / 35,022 / 21,458 — note direct materials + other segment items = cost of revenue exactly on all four columns; Net loss (39,343) / (24,234) / (154,185) / (35,963)"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 35
    url: https://agentii.ai/v/YSS/sec12/35
    located_via: read_source_pages
  - figure: "Backlog $642,298 at 2026-03-31 and $542,557 at 2025-12-31, with the issuer definition (aggregate expected revenue of awarded contracts at execution of a legally binding agreement; excludes unexercised contract options; includes contract liabilities); expects to recognize over 55% within the next 12 months; stated capacity to 'manufacture and test over 1,000 satellites annually'; expected replacement cycle five to six years"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 33
    url: https://agentii.ai/v/YSS/sec9/33
    located_via: read_source_pages
  - figure: "Backlog $592,049 at 2026-06-30 and $542,557 at 2025-12-31; over 55% expected within 12 months; 1,000-satellite annual capacity target repeated"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 37
    url: https://agentii.ai/v/YSS/sec12/37
    located_via: read_source_pages
  - figure: "The only disclosed spacecraft denominator: 'growing our backlog to approximately $543 million and 107 spacecraft as of December 31, 2025'; also 74 missions flown, 17 products with flight heritage, over four million on-orbit hours, more than 45 ground antennas, and the claimed comparative 'price per satellite has been approximately half the price of our competitors'"
    ticker: YSS
    form_type: 10-K
    citation_id: sec8
    page_no: 5
    url: https://agentii.ai/v/YSS/sec8/5
    located_via: read_source_pages
  - figure: "Remaining performance obligations $642.3 million at 2026-03-31 (Q1 10-Q) and $592.0 million at 2026-06-30 (Q2 10-Q)"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 19
    url: https://agentii.ai/v/YSS/sec12/19
    located_via: read_source_pages
  - figure: "Contract balances: contract assets 96,573 / 76,809 and contract liabilities 28,565 / 110,275 at 2026-03-31 and 2025-12-31; net EAC adjustments before income taxes (754) for Q1 2026 and 565 for Q1 2025; per-share impact $(0.01) and $0.01"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 17
    url: https://agentii.ai/v/YSS/sec9/17
    located_via: read_source_pages
  - figure: "One operating segment and one reportable segment, space infrastructure; CODM is the CEO; the measure of segment assets is total assets"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 34
    url: https://agentii.ai/v/YSS/sec12/34
    located_via: read_source_pages
  - figure: "Contribution margin (non-GAAP) = revenue less direct material costs: 3M 2026 39,307 (42%); 3M 2025 20,284 (24%); 6M 2026 79,373 (38%); 6M 2025 55,586 (29%) — the 6M 2026 direct-material input of 129,517 does not tie to the 129,538 on page 35"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 45
    url: https://agentii.ai/v/YSS/sec12/45
    located_via: read_source_pages
  - figure: "Adjusted EBITDA reconciliation, Q1 2026: EBITDA (100,570) vs 5,519 for Q1 2025; Adjusted EBITDA (3,638) vs 5,454"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 40
    url: https://agentii.ai/v/YSS/sec9/40
    located_via: read_source_pages
  - figure: "Loss contracts recognised within cost of revenues: none for 3M 2026; $2.1 million for 3M 2025; $5.5 million and $2.1 million for 6M 2026 and 2025"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 19
    url: https://agentii.ai/v/YSS/sec12/19
    located_via: read_source_pages
  - figure: "Material weakness in internal control over financial reporting disclosed in Part I Item 4"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 46
    url: https://agentii.ai/v/YSS/sec9/46
    located_via: read_source_pages
  - figure: "Condensed consolidated balance sheet at 2026-03-31 and 2025-12-31: common units 0 / 50,000,000; Class P Units 0 / 240,956,348; common stock 1,000,000,000 and 0 authorized, 127,609,213 and 0 issued and outstanding; accumulated deficit (383,864) / (269,022); total stockholders' equity or member's capital 1,722,351 / 867,824"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec9
    page_no: 6
    url: https://agentii.ai/v/YSS/sec9/6
    located_via: read_source_pages
  - figure: "Revenue disaggregation by customer type, Government 85,138 / 81,179 / 199,446 / 182,068 and Commercial and other 7,409 / 2,660 / 9,444 / 8,023 for 3M 2026 / 3M 2025 / 6M 2026 / 6M 2025 — 92% / 97% / 95% / 96% government; and the one-customer concentration: approximately 91% and 96% of revenues for the three months ended June 30, 2026 and 2025 came from a single customer, and 96% and 95% for the six months"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 17
    url: https://agentii.ai/v/YSS/sec12/17
    located_via: read_source_pages
  - figure: "Contract balances at June 30, 2026 and December 31, 2025: contract assets 114,967 / 76,809; contract liabilities 18,157 / 110,275; revenue recognized in 6M 2026 from the opening contract liability balance $108.1 million; net EAC adjustments, before income taxes, $(439) and $(13,812) for 3M 2026 and 2025, $(1,193) and $(13,247) for 6M 2026 and 2025"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 18
    url: https://agentii.ai/v/YSS/sec12/18
    located_via: read_source_pages
---

# YSS — Operational KPI Baseline, Q1–Q2 2026

Source filings: Q1 2026 10-Q `0001628280-26-035244` (`sec9`, filed 2026-05-15); Q2 2026
10-Q `0001628280-26-056874` (`sec12`, filed 2026-08-14); FY2025 10-K
`0001628280-26-019923` (`sec8`, filed 2026-03-20). Upstream: 001's
`artifacts/YSS/2026-09-18_1239_operational-kpi_methodology.md`, whose figures are tested
here and whose two DA readings are corrected.

---

## 0. The correction that reframes this artifact

001's YSS artifact states: *"Phase 3's plan called for the DA-13 distinction … this analysis
searched for it and **YSS does not disclose unit counts** — revenue only"*, and concludes
*"DA-13 is applicable to exactly one issuer"* (RKLB).

**That reading is refuted by the 10-K.** At [📄 YSS 10-K p.5](https://agentii.ai/v/YSS/sec8/5):

> *"growing our backlog to approximately **$543 million and 107 spacecraft** as of December 31,
> 2025"*

alongside *"having flown **74 missions**, created **17 products** with flight heritage, and
logged over **four million on-orbit hours**"*, and *"more than **45 ground antennas**"* in
connection with the ATLAS acquisition.

**YSS is a unit-counting issuer.** It discloses backlog in spacecraft, cumulative missions
flown, flight-heritage product count, on-orbit hours, and ground-station count. What it does
*not* disclose is a **per-period** manufactured-versus-launched rate — the specific
production-rate distinction DA-13 was built to test. That narrower gap is real and remains;
the blanket claim "no unit counts" is wrong, and any downstream artifact resting on it
should be restated.

The likely cause of the miss is a scope boundary, not carelessness: 001 read the Q2 2026
10-Q, and **no 10-Q discloses a spacecraft count.** The one denominator in the record sits in
the 10-K, seven weeks before the quarter 001 analysed. That is itself the operational
finding — see §2.

---

## 1. The cost structure, with the component identity in-line

001's operational claim is that YSS is **volume-constrained, not cost-constrained**: a real
positive manufacturing spread against a fixed cost base that is too large for its volume.
That claim survives, and the components are given below for every period quoted.

```text
3M 2026   revenue 116,343 − cost of revenues 94,193 = gross profit 22,150
          opex 36,706 + 84,696 + 5,289 + 5,925 = 132,616
          gross profit − opex = 22,150 − 132,616 = (110,466)      filed, sec9 p.7
          gross margin 19.0%   opex/revenue 114.0%   opex multiple 5.99×

3M 2025   revenue 106,252 − cost of revenues 81,650 = gross profit 24,602
          opex 26,801 + 0 + 4,401 + 31 = 31,233
          gross profit − opex = 24,602 − 31,233 = (6,631)          filed, sec9 p.7
          gross margin 23.2%   opex/revenue 29.4%   opex multiple 1.27×

3M 2026   revenue 92,547 − cost of revenue 70,367 = gross profit 22,180
  (Q2)    opex 40,825 + 10,893 + 5,766 + 6,009 = 63,493
          gross profit − opex = 22,180 − 63,493 = (41,313)         filed, sec12 p.7
          gross margin 24.0%   opex/revenue 68.6%   opex multiple 2.86×

3M 2025   revenue 83,839 − cost of revenue 74,313 = gross profit 9,526
  (Q2)    opex 25,790 + 0 + 4,893 + 75 = 30,758
          gross profit − opex = 9,526 − 30,758 = (21,232)          filed, sec12 p.7
          gross margin 11.4%   opex/revenue 36.7%   opex multiple 3.23×

6M 2026   revenue 208,890 − cost of revenue 164,560 = gross profit 44,330
          opex 77,531 + 95,589 + 11,055 + 11,934 = 196,109
          gross profit − opex = 44,330 − 196,109 = (151,779)       filed, sec12 p.7
          gross margin 21.2%   opex/revenue 93.9%   opex multiple 4.42×

6M 2025   revenue 190,091 − cost of revenue 155,963 = gross profit 34,128
          opex 52,591 + 0 + 9,294 + 106 = 61,991
          gross profit − opex = 34,128 − 61,991 = (27,863)         filed, sec12 p.7
          gross margin 18.0%   opex/revenue 32.6%   opex multiple 1.82×
```

**The spread is real and it is widening.** Q2 2026 gross margin 24.0% against Q2 2025's
11.4% — a 12.6-point year-over-year improvement. Q2 revenue fell 20.5% sequentially
(116,343 → 92,547) while gross margin *rose* 5.0 points (19.0% → 24.0%). Revenue down,
margin up, on the same fixed base: **that is the volume-constraint signature**, and it is
the opposite of a cost problem. A cost problem would compress margin as volume fell.

The fixed-cost multiple, however, is the problem and it is deteriorating at the half-year
level: **1.82× (6M 2025) → 4.42× (6M 2026)**.

### The Q1 "anomaly" is entirely one non-cash line

The $110,466 loss at [📄 sec9 p.7](https://agentii.ai/v/YSS/sec9/7) contains a **$84,696K
stock-based compensation charge** — 73% of Q1 revenue, and $84,696K of the $95,589K
half-year total. Strip it and Q1 is not anomalous at all:

```text
DERIVED (arithmetic on filed components; not an issuer-disclosed figure)
Q1 2026  opex ex-SBC = 132,616 − 84,696 = 47,920
         gross profit − opex ex-SBC = 22,150 − 47,920 = (25,770)
Q2 2026  opex ex-SBC = 63,493 − 10,893 = 52,600
         gross profit − opex ex-SBC = 22,180 − 52,600 = (30,420)
6M 2026  opex ex-SBC = 196,109 − 95,589 = 100,520
         gross profit − opex ex-SBC = 44,330 − 100,520 = (56,190)
6M 2025  opex ex-SBC = 61,991 − 0 = 61,991  (no SBC in the 2025 comparative)
         gross profit − opex ex-SBC = 34,128 − 61,991 = (27,863)
```

**Ex-SBC, the loss widened sequentially: $(25,770)K → $(30,420)K.** And the half-year
ex-SBC loss doubled, $(27,863)K → $(56,190)K. 001's carry-forward 2 asked whether the Q1
magnitude was *"a different defect class."* It is not a defect at all — it is the IPO's
one-time compensation charge — **and stripping it reveals that the underlying trend is worse
than the reported Q1 number suggests, not better.** The issuer's own non-GAAP agrees:
Adjusted EBITDA was $(3,638)K in Q1 2026 against $5,454K in Q1 2025, a $9.1M swing
([📄 sec9 p.40](https://agentii.ai/v/YSS/sec9/40)).

**The 95% is a minus sign.** 001 recorded Q1 2026 as *"an operating figure of $110.466M
against $116.343M of revenue — a 95% 'margin'"*. The filed MD&A table reports the same
number as **(110,466)** at **(95%)** of revenue
([📄 sec9 p.36](https://agentii.ai/v/YSS/sec9/36)). The minus in the parenthetical was
dropped in transit; the `us-gaap:OperatingIncomeLoss` fact is served as **+110,466**. The
component identity on p.7 settles it: `22,150 − 132,616 = (110,466)`.

---

## 2. DA-25 — the per-unit denominator exists at exactly one date

This is the operational-KPI finding with the widest consequences.

```text
2025-12-31   backlog $542,557K ÷ 107 spacecraft = $5,070K per spacecraft
             sec9 p.33 / sec12 p.37 for the dollars; sec8 p.5 for the count

2026-03-31   backlog $642,298K ÷ (not disclosed) = NOT REPRODUCIBLE
             sec9 p.33

2026-06-30   backlog $592,049K ÷ (not disclosed) = NOT REPRODUCIBLE
             sec12 p.37
```

**A backlog per unit is computable for one date in the issuer's entire public record and for
neither of the two quarters the 10-Qs report.** DA-25 is confirmed on its per-unit limb. The
detector is a reproducibility check that needs no judgement: for each disclosed dollar
figure in an issuer-defined metric, require a disclosed denominator, and flag dates where
none exists.

Two further points on the same metric:

- **Backlog is the RPO under another name.** The backlog table gives $642,298K at 2026-03-31
  ([📄 sec9 p.33](https://agentii.ai/v/YSS/sec9/33)) and $592,049K at 2026-06-30
  ([📄 sec12 p.37](https://agentii.ai/v/YSS/sec12/37)); the RPO note gives **$642.3 million**
  and **$592.0 million** at the same two dates
  ([📄 sec9 p.17](https://agentii.ai/v/YSS/sec9/17), [📄 sec12 p.19](https://agentii.ai/v/YSS/sec12/19)).
  Identical to the rounding, at both dates, under two differently-worded definitions — the
  backlog definition adds contract liabilities and excludes unexercised options; the RPO
  definition is the ASC 606 transaction price allocated to remaining obligations. No
  reconciliation between them is disclosed. **Practically, "backlog" is the filed RPO**, which
  means it is reproducible from the notes even where the per-unit basis is not.
- **The 10-K makes a comparative price claim with no denominator.**
  *"our price per satellite has been approximately half the price of our competitors"*
  ([📄 p.5](https://agentii.ai/v/YSS/sec8/5)) — no comparator set, no period, no price. Grade
  it **CLAIMED**, never DEMONSTRATED, and keep it out of any cost-per-unit or price-per-unit
  series feeding PIL-1 or PIL-3.

### The non-GAAP input that does not tie

Contribution margin, defined as revenue less direct material costs
([📄 sec12 p.45](https://agentii.ai/v/YSS/sec12/45)): 3M 2026 42%, 3M 2025 24%, 6M 2026 38%,
6M 2025 29%. The 6M 2026 computation uses a direct-material figure of **129,517**, while the
segment disclosure's direct-materials line is **129,538**
([📄 sec12 p.35](https://agentii.ai/v/YSS/sec12/35)) — a **$21K** break on one cell; the
other three cells agree exactly. The segment table's value is the one that reconciles:

```text
6M 2026  direct materials 129,538 +
         other segment items 35,022 = 164,560 = filed cost of revenue       ✓
         eleven-line segment sum closes to (154,185)                          ✓
         with 129,517 in place, the cost-of-revenue identity fails by 21
```

At the disclosed precision the percentage is unaffected (79,373/208,890 = 38.0%;
79,352/208,890 = 38.0% — both round to 38%), so this changes no headline. **It is recorded
because the metric's input does not reproduce from the table it names, which is DA-25's
shape, and because a $21K break in a hand-built reconciliation is a signal about the process
behind it** — the same filing process whose internal control over financial reporting carries
a **material weakness** ([📄 sec9 p.46](https://agentii.ai/v/YSS/sec9/46)).

---

## 3. The capacity claim, and what it implies arithmetically

The issuer states at [📄 sec9 p.33](https://agentii.ai/v/YSS/sec9/33) and
[📄 sec12 p.37](https://agentii.ai/v/YSS/sec12/37):

> *"We have significant production capability and believe we will be able to meet demand to
> manufacture and test **over 1,000 satellites annually**."*

That is the single largest operational claim YSS makes. It is testable against its own
numbers, and the arithmetic is stark:

```text
DERIVED (issued from filed figures; the 1,000/yr figure is an issuer CLAIM)
one spacecraft of backlog implies   $542,557K ÷ 107          = $5.07M
capacity at the claimed rate        1,000 × $5.07M            = $5,070M of revenue/yr
actual 6M 2026 revenue              208,890   → annualised     ≈ $418M
implied capacity multiple           5,070 ÷ 418               ≈ 12.1×

backlog coverage of the run-rate    592,049 ÷ 417,780         ≈ 1.42 years
claimed capacity as a share of
   one year of booked backlog        592,049 ÷ 5,070,000       ≈ 11.7%
```

**The claimed capacity is roughly 12× the current revenue run-rate, and the entire booked
backlog would fill about 12% of one year at that capacity.** Set against a stated replacement
cycle of *"approximately five to six years"* and the expectation that *"over 55%"* of
backlog converts within twelve months (both at [📄 sec12 p.37](https://agentii.ai/v/YSS/sec12/37)),
the picture is internally coherent as a *capability* claim and wholly unproven as a *demand*
claim.

**For PIL-3 this is the cleanest available statement of the volume-constraint reading**: the
constraint is not that YSS cannot build satellites — it says it can build an order of
magnitude more than it is building — but that it has orders for 107 of them. And the
$5.07M-per-spacecraft figure is a *backlog* average, not a price list; treat it as an
order-of-magnitude anchor only, and note the issuer's competing per-unit claim (price at
"approximately half" of competitors') is CLAIMED and unquantified.

**Both per-unit figures are labeled:** $5.07M is DERIVED from two DEMONSTRATED inputs
($542,557K and 107), while "half the price of our competitors" is CLAIMED. The
`no_single_basis_collapse` rule is satisfied by reporting both rather than either alone.

---

## 4. DA-12 and DA-21

**DA-12 (constellation size) — N/A, unchanged from 001.** YSS manufactures spacecraft; it
does not operate a constellation as a service. The on-orbit figures it quotes — 74 missions,
four million on-orbit hours — describe *customer* spacecraft it built, not a fleet it flies.
A constellation-size metric applied to YSS would be a category error, and 001's N/A stands.

**DA-21 (segment split) — one operating and one reportable segment, space infrastructure**
([📄 sec12 p.34](https://agentii.ai/v/YSS/sec12/34)); "The Company has no intra-segment sales
or transfers." The CODM is the CEO; the measure of segment assets is total assets.

**But the consequence matters more than the reading.** In a single-segment issuer, the
"segment table" is not a segment table — it is a consolidated net-loss cost decomposition
with no segment columns at all. It nevertheless closes on all four columns:

```text
3M 2026  92,547 − 53,240 − 40,825 − 10,893 − 5,766 − 6,009 − 2,884 + 4,208 + 928 − 282 − 17,127 = (39,343) ✓
3M 2025  83,839 − 63,555 − 25,790 − 0 − 4,893 − 75 − 7,118 + 218 + 1,201 + 2,697 − 10,758        = (24,234) ✓
6M 2026 208,890 − 129,538 − 77,531 − 95,589 − 11,055 − 11,934 − 5,783 + 8,828 − 5,279 − 172 − 35,022 = (154,185) ✓
6M 2025 190,091 − 134,505 − 52,591 − 0 − 9,294 − 106 − 14,177 + 759 + 1,315 + 4,003 − 21,458     = (35,963) ✓
```

**This table is the operational goldmine it is easy to walk past.** It is the only place YSS
discloses direct materials as a standalone line — the input to contribution margin — and it
is the only place the residual cost-of-revenue bucket ("other segment items": direct labor,
overhead, D&A) is quantified. Direct-material intensity improved from **70.8%** of revenue
(6M 2025: 134,505/190,091) to **62.0%** (6M 2026: 129,538/208,890), an 8.8-point gain. A
DA-25 screen that requires segment splits will miss this table entirely, because there are
no segments.

---

## 5. DA-23 on every period quoted here

The governing rule — DA-23 runs on every period an artifact quotes, not just the headline.
Six issuer-periods are quoted in this artifact; all six are tested by the component identity
above and all six are stripped:

| Period | Component identity (gross profit − opex) | Served `OperatingIncomeLoss` | Verdict |
|---|---|---|---|
| 3M 2026 (sec9 p.7) | 22,150 − 132,616 = **(110,466)** | +110,466 | STRIPPED |
| 3M 2025 (sec9 p.7) | 24,602 − 31,233 = **(6,631)** | +6,631 | STRIPPED |
| 3M 2026 (sec12 p.7) | 22,180 − 63,493 = **(41,313)** | +41,313 | STRIPPED |
| 3M 2025 (sec12 p.7) | 9,526 − 30,758 = **(21,232)** | +21,232 | STRIPPED |
| 6M 2026 (sec12 p.7) | 44,330 − 196,109 = **(151,779)** | +151,779 | STRIPPED |
| 6M 2025 (sec12 p.7) | 34,128 − 61,991 = **(27,863)** | +27,863 | STRIPPED |

`EPS × shares` is not used and would be wrong twice over here: it is not an admissible sign
test, and at YSS both inputs are independently stripped, so the product returns a **profit**
for every period — see the recent-quarter census, which carries the DA-28 evidence
(`1.51 × 116,022,676 = +175.2M` against a filed $(175.8)M loss to common; and the served
weighted-average share count in the Q1 filing is inflated 1000×).

---

## 6. Operational KPIs on the record, and their reproducibility

| KPI | Value | Date | Reproducible from the filings? |
|---|---|---|---|
| Backlog ($) | 642,298 / 592,049 / 542,557 | 03-31 / 06-30 / 12-31 | Yes — ties to the RPO note |
| Backlog (spacecraft) | 107 | 2025-12-31 only | **No denominator after that date** |
| Backlog per spacecraft | $5,070K | 2025-12-31 only | Only at that date |
| Missions flown (cumulative) | 74 | 10-K date | No series; single point |
| Flight-heritage products | 17 | 10-K date | No series; single point |
| On-orbit hours (cumulative) | >4 million | 10-K date | No series; single point |
| Ground antennas | >45 | 10-K date | No series; single point |
| Annual capacity | >1,000 satellites | Claimed, both 10-Qs | **CLAIMED** — no denominator |
| Replacement cycle | 5–6 years | Claimed, both 10-Qs | **CLAIMED** — no basis disclosed |
| Backlog conversion | >55% within 12 months | Both 10-Qs | Management estimate |
| Contract assets / liabilities | 96,573 / 28,565 → [📄 sec9 p.17](https://agentii.ai/v/YSS/sec9/17); 114,967 / 18,157 → [📄 sec12 p.18](https://agentii.ai/v/YSS/sec12/18) | 03-31 / 06-30 | Yes |
| Net EAC adjustments (pre-tax) | (754) Q1'26; 565 Q1'25 → [📄 sec9 p.17](https://agentii.ai/v/YSS/sec9/17); (439) Q2'26; (13,812) Q2'25; (1,193) vs (13,247) 6M → [📄 sec12 p.18](https://agentii.ai/v/YSS/sec12/18) | 2026 / 2025 | Yes — and see §6 signal 1 and carry-forward 9 |
| Loss-contract charges | none Q1 2026; 5,500 6M 2026 | 2026 | Yes |
| Revenue mix, government | 92% / 97% / 95% / 96% → [📄 sec12 p.17](https://agentii.ai/v/YSS/sec12/17) | Q1'26/Q1'25/6M'26/6M'25 | Yes |
| **Single-customer concentration** | **91% / 96% / 96% / 95%** | Q1'26/Q1'25/6M'26/6M'25 | Yes, and it is the sharper figure |
| Adjusted EBITDA | (3,638) Q1 2026; 5,454 Q1 2025 | Q1 2026 | Issuer non-GAAP |

**The unit series has length one.** A single 107-spacecraft datapoint cannot support a
production-rate, backlog-conversion or per-unit-trend claim, and any PIL-3 artifact using it
as a series would be manufacturing a trend from a point. That is the honest limit of YSS's
operational disclosure — **not** "no unit counts" (001's reading), but "no unit *series*."

**Three operational signals worth carrying:**

1. **EAC adjustments: the Q1 sign flipped, the half-year magnitude collapsed — both are
   true and they are not in tension.** Before income taxes: **$(754)K** unfavourable in Q1
   2026 against a favourable **$565K** in Q1 2025 (per-share impact printed **$(0.01)** against
   **$0.01**) ([📄 sec9 p.17](https://agentii.ai/v/YSS/sec9/17)); and **$(439)K** vs
   **$(13,812)K** for Q2, **$(1,193)K** vs **$(13,247)K** for the half
   ([📄 sec12 p.18](https://agentii.ai/v/YSS/sec12/18)). The half-year improvement comes from
   the disappearance of a $(13.8)M Q2 2025 charge (reductions in contract value and forecast
   cost increases), not from Q1 2026 being clean — Q1 2026 *drove* unfavourable revisions via
   contract loss reserves. Report both, and note the per-share side: the document prints a
   negative per-share value in parentheses in the very same filing whose
   `OperatingIncomeLoss` is served positive — **the sign convention is not ambiguous in the
   source.**
2. **Contract liabilities fell 74% in Q1 and 84% over the half** — $110,275K → $28,565K at
   2026-03-31 ([📄 sec9 p.17](https://agentii.ai/v/YSS/sec9/17)) → $18,157K at 2026-06-30
   ([📄 sec12 p.18](https://agentii.ai/v/YSS/sec12/18)) — because $95.6M of prior-period
   contract liability was recognised as Q1 revenue and a further $108.1M over the half. The
   liability is nearly exhausted. Backlog *includes* contract liabilities by the issuer's own
   definition, so the Q1→Q2 backlog decline of $50.2M (642,298 → 592,049) is partly this
   mechanical unwinding rather than a pure demand signal. **001's carry-forward 4 ("YSS
   revenue fell 20.5% QoQ — carry into Phase 6 as a demand-side signal") should be qualified
   accordingly** — and the same mechanism will *flatter* future reported revenue less and less,
   since there is now little deferred billings left to convert.
3. **Concentration is the operational fact that frames every other one.** Approximately
   **91%** of Q2 2026 revenue came from a **single customer** (96% in Q2 2025; 96% and 95% for
   the two half-year periods) ([📄 sec12 p.17](https://agentii.ai/v/YSS/sec12/17)). This is
   materially sharper than the government/commercial split and it is the binding constraint on
   the capacity story in §3: YSS claims capacity for 1,000 satellites a year while **one
   customer** supplies 91% of its revenue and its entire backlog is 107 spacecraft. A
   volume-constrained issuer whose volume comes from one procurement office is a different risk
   object from a volume-constrained issuer with diversified demand, and PIL-3 should not
   collapse the two.

---

## Carry-forwards

1. **001's DA-13 reading is corrected: YSS discloses unit counts.** 107 spacecraft, 74
   missions, 17 flight-heritage products, 45+ antennas, 1,000/yr capacity. The real gap is
   the absence of a per-period production rate and of any unit **series**. Restate the DA-13
   conclusion from "one issuer with unit data" to two, and re-scope what RKLB alone provides
   (a genuine build-versus-launch rate series).
2. **The per-unit KPI has length one.** $5,070K per spacecraft, 2025-12-31 only. Any trend
   claim built on it is unsupported. Record as DA-25 CONFIRMED / unresolved at the two 2026
   quarter-ends.
3. **YSS is ONE DA-23 entry, not two.** The Q1 2026 $110.466M and the Q2 2026 flip are the
   same sign-strip on two periods. 001's carry-forward 2 is discharged. The different defect
   class 001 was reaching for is **DA-28** (the IPO capital-structure discontinuity), which
   is a separate register entry on the per-share line, not the operating line.
4. **The underlying operating trend is worse than the reported Q1 suggests.** Ex-SBC the
   operating loss widened $(25,770)K → $(30,420)K sequentially and doubled half-over-half.
   That is the finding 001 could not reach without the component check.
5. **Backlog's equality with RPO is undisclosed.** Two definitions, one number, two dates.
   Add to the register as an observation; the remedy is a §1c disclosure requirement, not a
   detector.
6. **Qualify the demand signal in 001's carry-forward 4** — the Q1→Q2 backlog decline
   includes the mechanical unwinding of $95.6M of contract liability.
7. **Grade the comparative-price claim CLAIMED.** *"Price per satellite approximately half
   the price of our competitors"* has no comparator set, period, or figure.
8. **Single-customer concentration (91% of Q2 2026 revenue) is the sharpest operational fact
   in the record and 001 did not carry it.** It belongs alongside the volume-constraint
   reading, not folded into a government/commercial split — the buyer is one customer, and
   the backlog is 107 spacecraft. Carry into Phase 6 as the demand-side framing.
9. **Add the H1 EAC turnaround: $(13,247)K unfavourable in 6M 2025 → $(1,193)K in 6M 2026**,
   and $(13,812)K → $(439)K at the quarter ([📄 sec12 p.18](https://agentii.ai/v/YSS/sec12/18)).
   The magnitude of unfavourable estimate revisions fell by roughly an order of magnitude;
   combined with the direct-material intensity gain (70.8% → 62.0% of revenue), this is the
   strongest evidence in the record that the *cost* side is genuinely improving even as the
   volume side stalls. It is the operational counterweight to §5's ex-SBC deterioration and
   both should be reported together.

---

## Could not be verified

- **Any 2026 spacecraft count.** No 10-Q discloses one, so backlog per spacecraft, per-unit
  pricing and backlog conversion per unit are all uncomputable for Q1 and Q2 2026.
- **FY2025 annual operational figures.** The 10-K's XBRL facts are absent from the platform
  (`processing_status: pending` on accession `0001628280-26-019923`); only its page text is
  readable. FY2025 revenue, production counts and any annual unit series were not retrieved.
- **The 1,000 satellites/yr capacity claim's basis.** No facility count, floor space,
  headcount, cycle time or capital figure supports it; the same sentence repeats verbatim in
  both 10-Qs and the 10-K. Unverifiable as stated, and recorded as CLAIMED.
- **Whether the 107-spacecraft backlog count and the $542,557K backlog figure are
  contemporaneous and consistently defined.** Both are dated 2025-12-31, but they appear in
  different filings (10-K p.5 and the 10-Qs' backlog notes) and the 10-K's $543 million is a
  rounded restatement of $542,557K. Treated here as the same datapoint; not proven to be.
- **The Class P Units' path to zero and its effect on any per-unit or share-based KPI.**
  $93,411K derivative liability and $143,115K temporary equity at 2025-12-31, both nil at
  2026-03-31 ([📄 sec9 p.6](https://agentii.ai/v/YSS/sec9/6)). The extinguishing entries were
  not read.
- **Sec9 pages 38, 39, 41 and the FY2026 earnings-call transcripts** were not read; no
  management commentary on production rate or capacity utilisation was captured, which is
  where a forward production-rate KPI would most plausibly appear.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Q1 2026 income statement: Revenue 116,343; cost of revenues 94,193; gross profit 22,150; SG&A 36,706 + SBC 84,696 + R&D 5,289 + transaction costs 5,92 | [📄 YSS 10-Q p.7](https://agentii.ai/v/YSS/sec9/7) |
| MD&A for Q1 2026: loss from operations (110,466) at (95)% of revenue — the source of 001's '95% margin' | [📄 YSS 10-Q p.36](https://agentii.ai/v/YSS/sec9/36) |
| Q2 2026 and six-month income statement: Revenue 92,547 / 208,890; cost of revenue 70,367 / 164,560; gross profit 22,180 / 44,330; SG&A 40,825 / 77,531 | [📄 YSS 10-Q p.7](https://agentii.ai/v/YSS/sec12/7) **(newly surfaced)** |
| Segment significant-expenses table: Revenue 92,547 / 83,839 / 208,890 / 190,091; Direct materials 53,240 / 63,555 / 129,538 / 134,505; other segment i | [📄 YSS 10-Q p.35](https://agentii.ai/v/YSS/sec12/35) |
| Backlog $642,298 at 2026-03-31 and $542,557 at 2025-12-31, with the issuer definition (aggregate expected revenue of awarded contracts at execution of | [📄 YSS 10-Q p.33](https://agentii.ai/v/YSS/sec9/33) |
| Backlog $592,049 at 2026-06-30 and $542,557 at 2025-12-31; over 55% expected within 12 months; 1,000-satellite annual capacity target repeated | [📄 YSS 10-Q p.37](https://agentii.ai/v/YSS/sec12/37) |
| The only disclosed spacecraft denominator: 'growing our backlog to approximately $543 million and 107 spacecraft as of December 31, 2025'; also 74 mis | [📄 YSS 10-K p.5](https://agentii.ai/v/YSS/sec8/5) |
| Remaining performance obligations $642.3 million at 2026-03-31 (Q1 10-Q) and $592.0 million at 2026-06-30 (Q2 10-Q) | [📄 YSS 10-Q p.19](https://agentii.ai/v/YSS/sec12/19) |
| Contract balances: contract assets 96,573 / 76,809 and contract liabilities 28,565 / 110,275 at 2026-03-31 and 2025-12-31; net EAC adjustments before  | [📄 YSS 10-Q p.17](https://agentii.ai/v/YSS/sec9/17) |
| One operating segment and one reportable segment, space infrastructure; CODM is the CEO; the measure of segment assets is total assets | [📄 YSS 10-Q p.34](https://agentii.ai/v/YSS/sec12/34) |
| Contribution margin (non-GAAP) = revenue less direct material costs: 3M 2026 39,307 (42%); 3M 2025 20,284 (24%); 6M 2026 79,373 (38%); 6M 2025 55,586  | [📄 YSS 10-Q p.45](https://agentii.ai/v/YSS/sec12/45) |
| Adjusted EBITDA reconciliation, Q1 2026: EBITDA (100,570) vs 5,519 for Q1 2025; Adjusted EBITDA (3,638) vs 5,454 | [📄 YSS 10-Q p.40](https://agentii.ai/v/YSS/sec9/40) |
| Loss contracts recognised within cost of revenues: none for 3M 2026; $2.1 million for 3M 2025; $5.5 million and $2.1 million for 6M 2026 and 2025 | [📄 YSS 10-Q p.19](https://agentii.ai/v/YSS/sec12/19) |
| Material weakness in internal control over financial reporting disclosed in Part I Item 4 | [📄 YSS 10-Q p.46](https://agentii.ai/v/YSS/sec9/46) |
| Revenue disaggregation, Government 85,138 / 81,179 / 199,446 / 182,068 and Commercial and other 7,409 / 2,660 / 9,444 / 8,023 for 3M 2026 / 3M 2025 /  | [📄 YSS 10-Q p.17](https://agentii.ai/v/YSS/sec12/17) **(newly surfaced)** |
