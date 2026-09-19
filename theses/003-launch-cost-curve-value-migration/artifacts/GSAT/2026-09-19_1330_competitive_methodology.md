---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-2
ticker: GSAT
skill: competitive
mode: methodology
generated_at: 2026-09-19T13:30:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "826995c722a4"
as_of: 2026-09-19
corpus_version: "agentii-2026-09-18"
definitions_used:
  - da_id: DA-23
    chosen_reading: >-
      Absolute-value sign stripping. CONFIRMED at GSAT on 14 concept-periods across four
      concept-series, with bidirectional controls on the same concepts in both directions.
      Every figure here is read from the FILED page cell, never from a served fact. The
      equity fingerprint is the detector: on served signs it overstates total equity by
      exactly 2x the filed deficit.
  - da_id: DA-24
    chosen_reading: >-
      Non-operating contamination of operating_income. EXERCISED and CLEAN: the FY2022
      candidate (+221,029,000) is a DA-23 strip of a filed operating loss, not an
      extraction of a non-operating item; the filed impairment charge that explains its
      magnitude sits INSIDE opex as filed. The below-the-line chain is separately located
      in full for both Q2 periods.
  - da_id: DA-25
    chosen_reading: >-
      Normalised per-unit metrics not reproducible from audited tables. EXERCISED and CLEAN
      on the subscriber-services block, and NOT ASKABLE over the rest: the ARPU table
      reproduces from filed revenue to within $3k, and the other 63.6% of total revenue
      carries no per-unit metric by construction. The detector was run on the comparator
      side as well (A12).
  - da_id: DA-26
    chosen_reading: >-
      Annual figures mislabelled as quarterly. Locus is the `metrics` array of
      `get_company_financials`. CONFIRMED twice at GSAT. No figure in this artifact is read
      from that array.
  - da_id: DA-27
    chosen_reading: >-
      Fiscal-period labels from the calendar quarter. UNEXERCISED at GSAT: GSAT has a
      December fiscal year-end, so the calendar-quarter label and the fiscal label coincide
      and there is no independent test available in the periods read.
  - da_id: DA-28
    chosen_reading: >-
      Capital-structure discontinuity. EXERCISED and APPLICABLE at GSAT, and NOT via an IPO:
      a 1:15 reverse stock split completed February 10, 2025. Every share-count and per-share
      detector in this artifact is scoped to post-restatement comparisons, which is the
      control the filer itself supplies.
  - da_id: DA-29
    chosen_reading: >-
      A reconciliation that closes is not thereby a check. The retained-deficit walk closes
      exactly AND names every term on one page, including the 2,602 basis adjustment that
      would otherwise be an unexplained residual.
  - da_id: DA-30
    chosen_reading: >-
      Two bases on one concept collapsed. Reported on both bases, never one: revenue is
      quoted against total revenue or service revenue with the base named; debt is quoted on
      the balance-sheet basis (358,789) AND the filing's principal basis (423.7 million);
      Q1 2026 net loss is quoted as-filed and as-adjusted; leverage on the total-liability
      basis and the interest-bearing basis.
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "GSAT sec166 p.5"
    ticker: GSAT
    citation_id: sec166
    page_no: 5
    url: https://agentii.ai/v/GSAT/sec166/5
    located_via: read_source_pages
  - figure: "GSAT sec126 p.45"
    ticker: GSAT
    citation_id: sec126
    page_no: 45
    url: https://agentii.ai/v/GSAT/sec126/45
    located_via: read_source_pages
  - figure: "GSAT sec166 p.38"
    ticker: GSAT
    citation_id: sec166
    page_no: 38
    url: https://agentii.ai/v/GSAT/sec166/38
    located_via: read_source_pages
  - figure: "GSAT sec166 p.11"
    ticker: GSAT
    citation_id: sec166
    page_no: 11
    url: https://agentii.ai/v/GSAT/sec166/11
    located_via: read_source_pages
  - figure: "GSAT sec128 p.10"
    ticker: GSAT
    citation_id: sec128
    page_no: 10
    url: https://agentii.ai/v/GSAT/sec128/10
    located_via: read_source_pages
  - figure: "IRDM sec151 p.27"
    ticker: IRDM
    citation_id: sec151
    page_no: 27
    url: https://agentii.ai/v/IRDM/sec151/27
    located_via: read_source_pages
  - figure: "GSAT sec128 p.11"
    ticker: GSAT
    citation_id: sec128
    page_no: 11
    url: https://agentii.ai/v/GSAT/sec128/11
    located_via: read_source_pages
  - figure: "GSAT sec166 p.39"
    ticker: GSAT
    citation_id: sec166
    page_no: 39
    url: https://agentii.ai/v/GSAT/sec166/39
    located_via: read_source_pages
  - figure: "GSAT sec166 p.33"
    ticker: GSAT
    citation_id: sec166
    page_no: 33
    url: https://agentii.ai/v/GSAT/sec166/33
    located_via: read_source_pages
  - figure: "GSAT sec166 p.29"
    ticker: GSAT
    citation_id: sec166
    page_no: 29
    url: https://agentii.ai/v/GSAT/sec166/29
    located_via: read_source_pages
  - figure: "GSAT sec166 p.44"
    ticker: GSAT
    citation_id: sec166
    page_no: 44
    url: https://agentii.ai/v/GSAT/sec166/44
    located_via: read_source_pages
  - figure: "GSAT sec166 p.42"
    ticker: GSAT
    citation_id: sec166
    page_no: 42
    url: https://agentii.ai/v/GSAT/sec166/42
    located_via: read_source_pages
  - figure: "GSAT sec166 p.1"
    ticker: GSAT
    citation_id: sec166
    page_no: 1
    url: https://agentii.ai/v/GSAT/sec166/1
    located_via: read_source_pages
  - figure: "GSAT sec166 p.6"
    ticker: GSAT
    citation_id: sec166
    page_no: 6
    url: https://agentii.ai/v/GSAT/sec166/6
    located_via: read_source_pages
  - figure: "GSAT sec166 p.7"
    ticker: GSAT
    citation_id: sec166
    page_no: 7
    url: https://agentii.ai/v/GSAT/sec166/7
    located_via: read_source_pages
  - figure: "GSAT sec164 p.4"
    ticker: GSAT
    citation_id: sec164
    page_no: 4
    url: https://agentii.ai/v/GSAT/sec164/4
    located_via: read_source_pages
  - figure: "GSAT sec166 p.34"
    ticker: GSAT
    citation_id: sec166
    page_no: 34
    url: https://agentii.ai/v/GSAT/sec166/34
    located_via: read_source_pages
  - figure: "GSAT sec166 p.30"
    ticker: GSAT
    citation_id: sec166
    page_no: 30
    url: https://agentii.ai/v/GSAT/sec166/30
    located_via: read_source_pages
  - figure: "GSAT sec166 p.32"
    ticker: GSAT
    citation_id: sec166
    page_no: 32
    url: https://agentii.ai/v/GSAT/sec166/32
    located_via: read_source_pages
key_metrics:
  operating_margin_pct_3m: -7.37
  revenue_growth_pct_3m: -3.54
  wholesale_capacity_share_of_revenue_pct_3m: 62.0
  merger_consideration_per_share_usd: 90.00
---

# GSAT — competitive methodology (PIL-2, the operator leg)

## The finding

**If value migrated to operators, it did not arrive here.**

Globalstar reports Q2 2026 operating income of **$(4,775) thousand** on **$64,772 thousand** of
revenue — **−7.37%**, down from **+9.15%**, a **−16.5 point swing** — on revenue that **fell
3.54%** [📄 GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5). It carries the thinnest operator
margin in the universe, and it is the only operator in the universe whose revenue **declined**.
**This is the leg of PIL-2 that the operator hypothesis needs to work, and it does not work.**

Three structural facts, each filed, decide the leg:

1. **93% of net income is non-operating — and the correct filed figure is 98.5%.** FY2024
   operating income was **$949 thousand** against net income of **$63,164 thousand**: **98.5% of
   net income arose below the operating line**
   [📄 GSAT 10-K p.45](https://agentii.ai/v/GSAT/sec126/45). In Q2 2026 the arithmetic is more
   acute: **interest expense of $(20,660)k alone is 4.33x the operating loss of $(4,775)k**, and
   the company recorded an income tax **expense** of $3,909k in a loss quarter — so the net loss
   of $(26,539)k is **82.0% non-operating by origin**
   [📄 GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5).
2. **It is a financing structure attached to one customer's service, not an operating company.**
   Operating cash flow of **+$159,767k** over H1 2026 was supported by a **+$216,595k increase in
   deferred revenue** — *larger than the whole figure* — plus **+$80,734k** of payables and
   accrued network construction costs, against a **net loss of $(41,357)k**. The receipts are
   the customer's prepayments, filed as *"recorded as deferred revenue and used to fund capital
   expenditures for the Extended MSS Network"*
   [📄 GSAT 10-Q p.38](https://agentii.ai/v/GSAT/sec166/38).
   **Strip the customer's prepayments and the operating cash flow is negative $56,828k**
   (grade DERIVED — arithmetic on filed cells; see the basis note below).
3. **And it is being acquired by its own demand owner.** On April 13, 2026 GSAT signed a Merger
   Agreement with Amazon affiliates at **$90.00 per share**
   [📄 GSAT 10-Q p.11](https://agentii.ai/v/GSAT/sec166/11) — **≈41.4x–41.6x TTM revenue,
   against the ≈8.3x the launcher pays for the profitable operator.**

**The counter-case to launcher capture is refuted at this leg — and refuted in a way that
strengthens PIL-2 rather than weakening it.** The operator leg fails on margin, fails on
independence, and fails in the direction of the demand owner rather than the launcher. **The
value pool did not rest with the independent operator here; it was already contracted to one
customer, and that customer is now buying the shell.**

---

## Mode 1 — direct-competitor-identification-and-analysis

### The filed competitor set, and it is bilateral

GSAT's FY2025 10-K states it verbatim: *"**Our largest global competitors are Viasat, Iridium and
ORBCOMM**"* [📄 GSAT 10-K p.10](https://agentii.ai/v/GSAT/sec128/10), and of IRDM specifically:
*"**Iridium markets products and services that are similar to those marketed by us.**"*

IRDM's FY2025 10-K states the reciprocal: *"our principal mobile satellite services competitors
are **Viasat, Globalstar, ORBCOMM, and Thuraya**"*
[📄 IRDM 10-K p.27](https://agentii.ai/v/IRDM/sec151/27).

**Both legs of PIL-2's operator test name each other as direct competitors, in filed documents,
in the same fiscal year.** GSAT's disclosure goes a step further and reveals that its own SPOT
product competes *on Iridium's network*: SPOT's competitors are *"Garmin inReach, Honeywell
Global Tracking … and Somewear … **all of which work on Iridium's satellite network**"*
[📄 GSAT 10-K p.11](https://agentii.ai/v/GSAT/sec128/11). **GSAT is, for a material slice of its
subscriber base, a reseller competing against resellers of its named competitor's network.**

### ⚠️ The taxonomy omission — silent, and it looks like a clean result

- **GSAT files under `tech.tech_hardware`.**
- **IRDM files under `tech.telecom_services`.**

A comparator set assembled by taxonomy node **includes IRDM and omits GSAT** — while both
issuers' own filings name each other as principal competitors and IRDM lists Globalstar first in
its set of four. **The omission is invisible and looks like a clean result.** This is a
platform/corpus property, not an issuer property; the remedy is a curated sector map. Until one
exists, **no taxonomy-node comparator set at these two tickers is admissible**, and this
artifact reports the set on both bases — the taxonomy node *and* the filed competitor list —
rather than on either alone.

### The demand owner is in the competitor list of the company it is buying

GSAT's own filing names *"SpaceX's Starlink and Amazon Leo and AST SpaceMobile"* as emerging
competitors [📄 GSAT 10-K p.10](https://agentii.ai/v/GSAT/sec128/10) — **"Amazon Leo" is Amazon,
which on April 13, 2026 agreed to acquire GSAT.** The same filing lists *"recent terrestrial
spectrum sales, such as between **EchoStar and SpaceX** and between **EchoStar and AT&T**."*

**Neither GSAT nor IRDM names Rocket Lab as a competitor in any period.** *The two acquisitions
that end the independent-operator leg of PIL-2 are made by a party that was already a named
competitor (Amazon at GSAT) and by a party from a different layer entirely (Rocket Lab at
IRDM).* That asymmetry is the substantive answer to PIL-2: **the launcher is not buying a
competitor, it is buying a position in someone else's competitive set.**

A second axis: **SpaceX is simultaneously a named competitor and a supplier.** GSAT's H1 2026
investing cash flow was driven by *"the timing of milestone payments made to **MDA Space and
SpaceX**"* for network upgrades [📄 GSAT 10-Q p.39](https://agentii.ai/v/GSAT/sec166/39). GSAT is
buying its competitive response, in part, from a competitor.

### Head-to-head, on the one basis that is filed at both

| | GSAT Q2 2026 | IRDM Q2 2026 | GSAT as % of IRDM |
|---|---|---|---|
| Total revenue | $64,772k | $225,237k | 28.8% |
| Operating income | $(4,775)k | $34,008k | — |
| Operating margin | **−7.37%** | **15.10%** | — |
| Service revenue | $59,998k | $161,328k | 37.2% |
| Total subscribers | 803,980 | 2,627,000 | 30.6% |
| Revenue per subscriber, quarterly | **$74.6** | ~$61.4 (total-revenue basis) | 121.5% |

**This comparison rests on two incompatible subscriber bases and must not be quoted as a share
(DA-30).** GSAT counts *"the number of devices that are subject to agreements"* and files the
caveat verbatim: *"Other providers of comparable services may count their subscribers
differently"* [📄 GSAT 10-Q p.33](https://agentii.ai/v/GSAT/sec166/33). GSAT also counts
**devices**, IRDM counts **billable subscribers**, and GSAT's base includes several thousand
*"Other"* units (192) with no revenue line at all. **There is no filed reconciliation between the
two bases and no platform-derived basis field. Any universe-level subscriber-share figure
computed by ratio across these two issuers is a basis collapse and should be refused.**

---

## Mode 2 — market-share-dynamics-analysis

### The denominator does not exist

**Neither issuer files a market-share statistic, and no such statistic exists anywhere in the
corpus.** `list_xbrl_concepts` returns **0** for `MarketShare`, **0** for `Spectrum`, **0** for
`Subscriber` — a **zero by construction**, because no filer tags the concept, so no structured
query can ever return one. **A quantified market-share analysis at GSAT is UNEXERCISED, and the
disposition is `UNRESOLVABLE-FROM-PUBLIC-SOURCES`**: the resolving input is a filed share
statistic or a third-party market census, neither of which any platform can extract from these
documents. **This leg of the artifact therefore rests on page text, not on facts, throughout.**

### What the filings do support: the base grew while the revenue shrank

| Subscriber line | Avg subs Q2 26 | ARPU Q2 26 | Rev Q2 26 | Avg subs Q2 25 | ARPU Q2 25 | Rev Q2 25 |
|---|---|---|---|---|---|---|
| Commercial IoT | 580,427 | $4.31 | $7,512k | 534,505 | $4.40 | $7,051k |
| SPOT service | 207,606 | $13.81 | $8,604k | 224,885 | $13.67 | $9,224k |
| Duplex | 15,755 | $57.44 | $2,715k | 21,841 | $56.12 | $3,677k |
| Other | 192 | — | — | 239 | — | — |
| **Subscriber services, derived** | **803,980** | — | **$18,831k** | **781,470** | — | **$19,952k** |
| Wholesale capacity services | *(not subscriber driven)* | — | **$40,114k** | — | — | **$42,385k** |
| Government and other services | *(not subscriber driven)* | — | **$1,053k** | — | — | **$879k** |
| **Total service revenue (filed subtotal)** | | | **$59,998k** | | | **$63,216k** |

[📄 GSAT 10-Q p.33](https://agentii.ai/v/GSAT/sec166/33). **Basis note (DA-30): subscriber
services is a DERIVED subtotal** — the statement presents the three subscriber lines and the filed
subtotal is *total service revenue*; $18,831k = 7,512 + 8,604 + 2,715 ✓ EXACT, and $19,952k =
7,051 + 9,224 + 3,677 ✓ EXACT. **The filed percentages are on the wholesale line: 62% of total
revenue in Q2 2026, 64% for the six months.**

**Subscribers grew 2.88% while subscriber-services revenue fell 5.62%.** The composition is
adverse on every line that matters: **SPOT lost 17,279 subscribers (−7.7%)** and **Duplex lost
6,086 (−27.9%)** — the two highest-ARPU lines — while the growth is entirely in IoT, the lowest
ARPU line at $4.31. **ARPU is flat-to-up on every line and revenue falls anyway: this is a
volume-mix problem, not a pricing problem.** The losses are in the lines that carry the price.
The subscriber bridge ties exactly: `+45,922 (IoT) − 17,279 (SPOT) − 6,086 (Duplex) − 47 (Other)
= +22,510` ✓ **EXACT** against the filed 803,980 vs 781,470.

### The DA-25 reproduction test — run on BOTH sides (A12), and it passes

A positive `DA-25` finding requires the per-unit metric to be non-reproducible. Run against GSAT's
own filed revenue, the table **reproduces**:

| Line | ARPU × subscribers × 3 months | Filed | Variance |
|---|---|---|---|
| Duplex | $57.44 × 15,755 × 3 = **$2,714,902** | $2,715k | **exact** |
| IoT | $4.31 × 580,427 × 3 = $7,504,921 | $7,512k | $7k (0.09%) |
| SPOT | $13.81 × 207,606 × 3 = **$8,601,117** | $8,604k | $3k (0.03%) |
| IoT, *prior year* | $4.40 × 534,505 × 3 = $7,055,466 | $7,051k | $4k (0.06%) |
| SPOT, *prior year* | $13.67 × 224,885 × 3 = $9,222,533 | $9,224k | $1k (0.02%) |
| Duplex, *prior year* | $56.12 × 21,841 × 3 = $3,677,591 | $3,677k | $1k (0.02%) |

**And the block ties to the income statement exactly:** subscriber services $18,831k + wholesale
capacity $40,114k + government/other $1,053k = **$59,998k** ✓ EXACT service revenue
[📄 GSAT 10-Q p.33](https://agentii.ai/v/GSAT/sec166/33)
[📄 GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5). **The table reproduces on BOTH years, six
of six cells to within $7k** — which is a stronger clearance than a single-period fit.

**So `DA-25` is CLEAN here, scoped and exhibited** — not because the metrics are vague but
because they reproduce to rounding. **The control was run on the comparator side too (A12): at
IRDM the identical table *cannot* be reproduced, because IRDM's subscriber counts are never
XBRL-tagged. Two issuers, two opposite verdicts, same detector.** The scope of the GSAT
clearance is limited and must be stated with it:

- **63.6% of Q2 2026 total revenue carries no per-unit metric by construction** — wholesale
  capacity $40,114k (62.0%) plus government/other $1,053k (1.6%) = $41,167k.
  **On the service-revenue base that share is 68.6%.** Both bases are given because they differ
  (DA-30) and the metric is meaningless without naming one. **The issuer states the reason
  verbatim: *"None of these service revenue items are subscriber driven. Accordingly, we do not
  present ARPU for wholesale capacity services revenue or government and other services
  revenue."***
- **Wholesale capacity is 62.0% of GSAT's total revenue and it has no subscriber concept at all.**
  This is the customer's contract. **The one line that is largest is the one line that is not a
  market.**
- **⚠️ Period-basis trap, and GSAT has one too.** Wholesale capacity revenue **fell 5.36%** in
  Q2 2026 ($40,114k vs $42,385k) but **rose 9.21%** for the six months ($86,381k vs $79,094k) —
  **a sign reversal on the same line from the same page.** The H1 direction is the customer
  ramping the Extended MSS Network; the Q2 direction is the customer's payments stepping down.
  **Never quote GSAT's wholesale trend without its period basis.** Government and other services
  runs the other way (Q2 +$174k, H1 +$972k) and includes *"revenue generated primarily from
  terrestrial spectrum and network solutions"* — which is the line exposed to the Anterix /
  Nextwave / TerraStar terrestrial competition GSAT names in its 10-K and, on its own filing, to
  the *"recent terrestrial spectrum sales, such as between EchoStar and SpaceX and between
  EchoStar and AT&T"* [📄 GSAT 10-K p.10](https://agentii.ai/v/GSAT/sec128/10).

### ~64% of revenue is one customer, and the customer is also the financier and the acquirer

GSAT discloses that a single customer accounted for **64% of revenue** in the six months ended
June 30, 2026 [📄 GSAT 10-Q p.29](https://agentii.ai/v/GSAT/sec166/29). The filing calls that
party only **"the Customer"**; **the identity is established by a competitor's filing** — IRDM's
10-K names *"Globalstar's partnership with Apple"*
[📄 IRDM 10-K p.27](https://agentii.ai/v/IRDM/sec151/27). **GSAT itself never names the customer
in the periods read.** That is a disclosure asymmetry worth recording: the identity of the
counterparty holding 64% of an issuer's revenue is sourced from the issuer's named competitor.

**The same customer is the financing source.** Deferred revenue, net, is **$1,085,545k**
($56,179k current + $1,029,366k non-current) — **44.4% of total assets and 50.4% of total
liabilities** — of which *"the majority is expected to be earned over a period in excess of five
years"*, and H1 2026 included *"the receipt of **$104.8 million** pursuant to the Infrastructure
Prepayment and **$19.9 million** pursuant to the 2023 Funding Agreement"*, receipts which are
*"recorded as deferred revenue and used to fund capital expenditures for the Extended MSS
Network, typically in the quarter following the receipt of funds"*
[📄 GSAT 10-Q p.38](https://agentii.ai/v/GSAT/sec166/38)
[📄 GSAT 10-Q p.39](https://agentii.ai/v/GSAT/sec166/39).

**And the same customer is now the acquirer.** See Mode 3. **The correct description of this
entity is not "an operator with a large customer." It is a customer's infrastructure, financed by
the customer, held at 12% equity, and now being purchased by the customer.**

---

## Mode 3 — market-share-evolution-and-competitive-benchmarking

### The operator-versus-launcher margin benchmark

| Issuer | Layer | Q2 2026 operating margin | Prior-year | Revenue y/y | Basis |
|---|---|---|---|---|---|
| **IRDM** | independent operator | **+15.10%** | +23.17% | **+3.84%** | filed, 4 of 4 periods exact |
| **GSAT** | independent operator | **−7.37%** | +9.15% | **−3.54%** | filed, 9 of 9 periods exact |
| **RKLB** | launcher | **−24.57%** | −41.3% | +62.0% | inherited correction, not recomputed |
| **SPCX** | integrator | 8.29% launch-only | — | — | inherited; `12.3%` is three things at once |

**The universe contains exactly two independent operators. One earns 15.10% and is bought by the
launcher; the other earns −7.37% and is bought by its own customer. Neither survives as the
independent operator PIL-2 posits as an alternative recipient of the value pool.**

**The five-year trend is real and must be stated with the reversal.** GSAT's operating margin ran
**−52.70% (FY2021) → −148.84% (FY2022) → −0.07% (FY2023) → +0.38% (FY2024) → +2.72% (FY2025) →
+11.66% (Q1 2026) → −7.37% (Q2 2026)**. Four years of operating improvement — the FY2022 trough is
almost entirely a filed `Reduction in the value of long-lived assets` of **$166,526k** sitting
inside opex — and then a single quarter gives back 19 points of it. **One quarter is not a trend,
and four years is not a business: the improvement ran from a −148.8% trough to a +2.7% level, and
then reversed.**

### The Amazon transaction is priced off milestones, and the cash is capped

*"each share … will be converted into the right to receive $90.00 in cash or … a number of shares
of Amazon common stock"* at an exchange ratio, with **stock consideration as the default** and
**cash elections capped at 40% of shares outstanding with automatic proration**; aggregate
consideration is *"subject to a downward adjustment … capped at $110 million"* for failure to
meet operational milestones with the Customer, and *"as of the date of this Report, the maximum
amount … is **approximately $97 million reduced from $110 million**"*; the termination fee payable
by GSAT is **approximately $420 million**; and **the HSR waiting period expired July 17, 2026**
[📄 GSAT 10-Q p.11](https://agentii.ai/v/GSAT/sec166/11)
[📄 GSAT 10-Q p.44](https://agentii.ai/v/GSAT/sec166/44)
[📄 GSAT 10-Q p.42](https://agentii.ai/v/GSAT/sec166/42).

**There is no shareholder vote and there will not be one.** Thermo, holding **approximately
57.6%**, delivered a **written consent**: *"no further approval of the Company's stockholders is
required or will be sought"* [📄 GSAT 10-Q p.11](https://agentii.ai/v/GSAT/sec166/11).

- **Implied equity value: $90.00 × 129,563,390 common shares = $11,660.7M**
  [📄 GSAT 10-Q p.1](https://agentii.ai/v/GSAT/sec166/1). Grade DEMONSTRATED as arithmetic;
  **a floor, because it excludes the 149,425 Series A Preferred shares and the customer and
  Thermo warrants** — and the filing states the preferred is to be *"cancel[led] … in exchange
  for the liquidation preference upon consummation of the Mergers"*
  [📄 GSAT 10-Q p.38](https://agentii.ai/v/GSAT/sec166/38).
- TTM revenue = $272,986k − $127,180k + $134,836k = **$280,642k**.
- **≈41.4x–41.6x TTM revenue** (the band is the debt basis, below — DA-30).

### ⚠️ The platform serves the wrong share count for GSAT, by 867x

`get_company_financials` returns **`common_shares_outstanding: "149425"`**. The filing states:
*"As of July 31, 2026, **129,563,390 shares of common stock** were outstanding and **149,425
shares of preferred stock** were outstanding"* [📄 GSAT 10-Q p.1](https://agentii.ai/v/GSAT/sec166/1),
and the balance sheet independently reports *"Voting Common Stock … **129,562,435** and
128,050,400 shares issued and outstanding at June 30, 2026 and December 31, 2025"*
[📄 GSAT 10-Q p.6](https://agentii.ai/v/GSAT/sec166/6).

**The served figure is the PREFERRED share count, presented as the common count — an error of
867x.** Any per-share valuation, market capitalisation or share-count detector built on this
field at GSAT is wrong by three orders of magnitude, and it is wrong in the *conservative*
direction (it understates equity value), so it will not announce itself. **This is a
platform-extraction defect of the same family as the DA-23 strips below: it is invisible to any
plausibility heuristic, and only a page read catches it.**

### The structural contrast: the demand owner prices execution; the launcher prices its own currency

| | Amazon buys GSAT | Rocket Lab buys IRDM |
|---|---|---|
| Announced | April 13, 2026 | June 28, 2026 |
| Price per share | **$90.00** | **$54.00** in-band |
| Form | Cash **capped at 40%**, default stock | **$27.00 unconditional cash** + stock half |
| Price protection | **$110M → $97M milestone reduction** | **±25% value-preserving collar** ($67.50–$112.50) |
| Shareholder approval | **none — 57.6% written consent** | required (Form S-4) |
| Termination fee | **~$420M** | **$223.6M** |
| Operating margin of target | **−7.37%** | **+15.10%** |
| Implied EV / TTM revenue | **≈41.4x–41.6x** | **≈8.3x** |

**The demand owner pays 5.0x the revenue multiple for the *unprofitable* operator; the launcher
pays one fifth of that for the *profitable* one.** The demand owner's consideration is
**conditional on execution** (milestones) and its cash is **rationed** (40% cap). The launcher's
consideration is **fixed in real terms inside a wide band** and its cash half is
**unconditional**.

**That is the PIL-2 finding in its most testable form.** Amazon is not paying 41x revenue for
GSAT's margin — it is paying for the position. Rocket Lab is not paying 8.3x revenue for IRDM's
margin either — it is paying for the licence, the government and aviation demand, and Aireon.
**Neither acquirer prices the operator's income statement. Both price the customer relationship
the operator sits on.** The value pool was never in the operating margin; it was in the demand,
and both layers above the operator are now paying to own it directly.

---

## Data-integrity register — GSAT self-run DA census

**GSAT carries no DA census from thesis 002. The checks below were run here. Anything not
attempted is marked `UNEXERCISED` and is never reported as CLEAN.**

### DA-23 — CONFIRMED. 14 stripped, four concept-series, with bidirectional controls

**Detector: the component identity only. `EPS × shares` was not used as a sign test anywhere.**

**The equity fingerprint closes on the filed signs and fails by exactly 2x on the served signs.**
Filed: `13 + 2,492,511 + 6,659 − 2,206,570 = 292,613` ✓ **EXACT** against the filed total
stockholders' equity of $292,613k [📄 GSAT 10-Q p.6](https://agentii.ai/v/GSAT/sec166/6). Served
with the deficit stripped: `13 + 2,492,511 + 6,659 + 2,206,570 = 4,705,753` — an excess over
served total equity (292,613,000) of **4,413,140 = 2 × 2,206,570** ✓ **EXACT**. **The same 2x
signature as IRDM: one stripped component produces exactly twice its magnitude of error.**

| Concept | Period | Filed | Served | Verdict |
|---|---|---|---|---|
| `OperatingIncomeLoss` | Q2 2026 | **(4,775)** | +4,775,000 | **STRIPPED** |
| `OperatingIncomeLoss` | H1 2025 | **(2,355)** | +2,355,000 | **STRIPPED** |
| `OperatingIncomeLoss` | Q1 2025 | **(8,501)** | +8,501,000 | **STRIPPED** |
| `OperatingIncomeLoss` | FY2022 | **(221,029)** | +221,029,000 | **STRIPPED** |
| `OperatingIncomeLoss` | Q2 2025 | **+6,146** | +6,146,000 | **preserved** |
| `OperatingIncomeLoss` | H1 2026 | **+3,395** | +3,395,000 | **preserved** |
| `OperatingIncomeLoss` | Q1 2026 | **+8,170** | +8,170,000 | **preserved** |
| `OperatingIncomeLoss` | FY2025 / Q3 2025 / 9M 2025 | **+7,430 / +10,156 / +7,801** | as filed | **preserved** |
| `NetIncomeLoss` | Q1 2026 / Q2 2026 / H1 2026 / Q1 2025 | **(17,420) / (26,539) / (41,357) / (17,331)** | all **positive** | **STRIPPED (4)** |
| `NetIncomeLoss` | Q2 2025 / H1 2025 / FY2024 | **+19,208 / +1,877 / +63,164** | as filed | **preserved** |
| `NetIncomeLossAvailableToCommonStockholdersBasic` | Q1 2026 / Q2 2026 / H1 2026 / Q1 2025 / H1 2025 | **(20,035) / (29,183) / (46,616) / (19,946) / (3,382)** | all **positive** | **STRIPPED (5)** |
| `RetainedEarningsAccumulatedDeficit` | 2025-12-31 | **(2,136,797)** | +2,136,797,000 | **STRIPPED** |
| `AccumulatedOtherComprehensiveIncomeLoss` | 2026-06-30 / 2025-12-31 / 2026-03-31 | **+6,659 / +3,286 / +5,325** | as filed | **preserved (3)** |

[📄 GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5)
[📄 GSAT 10-Q p.7](https://agentii.ai/v/GSAT/sec166/7)
[📄 GSAT 10-K p.45](https://agentii.ai/v/GSAT/sec126/45).

**The bidirectional control is unusually strong and it is internal to one concept.**
`OperatingIncomeLoss` is genuinely bidirectional — both signs are filed — and the *same concept*
is preserved at **Q2 2025 (+6,146)** and stripped at **Q2 2026 (−4,775)**, one year apart in the
same fiscal quarter. `AccumulatedOtherComprehensiveIncomeLoss` completes the control on the
adjacent equity line: it is filed **positive** at all three dates observed and **served
correctly**, while the deficit immediately beneath it is filed negative and stripped. **Same
statement, adjacent lines, opposite outcomes, and the sign of the filed value predicts which.**

**State the scoping precisely, because it is the difference between a result and a claim:**
**every filed GSAT operating loss examined (4 of 4) is served positive, and every filed positive
(6 of 6) is preserved.** That is a clearance *scoped to bidirectional concepts and exhibited with
negative-filed instances* — the A17 requirement. **It does NOT extend to FY2021 and FY2023, whose
served values were not read: those are `UNEXERCISED`, not CLEAN.** *(FY2021 and FY2023 operating
losses of $(65,503)k and $(165)k are filed at sec126 p.45; the served facts were not compared.)*

### DA-26 — CONFIRMED twice

Locus: the `metrics` array of `get_company_financials`. The **Q4-2025 row carries FY2025 annuals**
(revenue 272,986; operating income 7,430; net income 8,651 — each matching the FY2025 10-K facts)
and the **Q4-2024 row carries FY2024 annuals** (250,349; 949; 63,164; EPS 0.59, post-split
restated). Inflation ratios `272,986 / 71,961 = 3.794x` and `250,349 / 61,176 = 4.092x` —
**both are FY figures against a Q4 denominator; neither row is a Q4-vs-Q4 comparison.** The defect
is **per-concept, not per-row**. Note the companion silent zero: **`search_xbrl_facts` with
`fiscal_period: "Q4"` returns zero at GSAT in every period — also by construction, since a 10-K
files no Q4-only duration fact.**

### DA-28 — EXERCISED AND APPLICABLE, and not via an IPO

**The brief's DA-28 exemplar is an IPO. At GSAT the discontinuity is a reverse split, and it is
dated and disclosed:** *"All historical share and per share amounts for the periods prior to the
completion of the **1:15 reverse stock split on February 10, 2025** reflected in this Report have
been adjusted to reflect the reverse stock split"*
[📄 GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5). The balance sheet corroborates the
post-split capital structure — 143,333,334 voting common shares authorised, $0.0001 par
[📄 GSAT 10-Q p.6](https://agentii.ai/v/GSAT/sec166/6).

**Verdict: any share-count or per-share detector spanning 2025-02-10 is inadmissible unless both
sides are post-split restated.** The control is supplied by the filer itself: the Q2 2026 vs
Q2 2025 weighted-average share counts (129,122 vs 126,614) **are** comparable, and only because
the filing restated the prior period. **The detector was run and passes *within* the scope; it
would have failed silently across the split, where a 15x step would have appeared as a 93%
share-count collapse.**

### DA-29 — the retained-deficit walk closes exactly AND names every term

```
Balances – January 1, 2026                    (2,136,797)
Cumulative effect of adoption of ASU 2025-07     (28,416)
Balances as adjusted – January 1, 2026        (2,165,213)  ✓  (2,136,797) − 28,416
Net loss (as reported)  Q1 2026                  (17,420)
Impact of adoption of ASU 2025-07 on net loss      +2,602
Balances – March 31, 2026                     (2,180,031)  ✓  (2,165,213) − 17,420 + 2,602
Net loss  Q2 2026                                (26,539)
Balances – June 30, 2026                      (2,206,570)  ✓  (2,180,031) − 26,539
```

[📄 GSAT 10-Q p.7](https://agentii.ai/v/GSAT/sec166/7). **Every term is filed on that page —
including the `+2,602` that would otherwise be an unexplained residual. This is not a back-solve:
the reconciliation closes *and* each input is located.** (DA-29's failure mode is a reconciliation
that closes against a term appearing nowhere in the source. This one does not.)

**It also resolves the apparent 2,602 residual in the cumulative chain:** Q1 2026 as-filed
$(17,420)k + Q2 2026 $(26,539)k = $(43,959)k against H1 2026 as-filed $(41,357)k — a $2,602k
residual **which is exactly the filed basis adjustment.** The chain does not close across the
adoption date, and the reason is filed rather than inferred.

**DA-30 corollary — Q1 2026 net loss has two bases and both are reported: $(17,420)k as filed in
the Q1 10-Q, and $(14,818)k as adjusted** (derivable from the walk above and from
$(41,357) − $(26,539)). **A Q1 2026 net loss quoted without its basis is a DA-30 collapse.**

### DA-24 — EXERCISED and CLEAN, and the candidate is discharged the other way

The served `OperatingIncomeLoss` of **+221,029,000** for FY2022 looked like a non-operating item
contaminating the operating line. **It is not.** It is a **DA-23 strip** of a filed operating loss
of **$(221,029)k** [📄 GSAT 10-K p.45](https://agentii.ai/v/GSAT/sec126/45), and its magnitude is
explained by a genuine filed **`Reduction in the value of long-lived assets` of $166,526k sitting
inside opex.** The component identity closes exactly on all three FY2021–FY2023 periods against
the filed `Total operating expenses` subtotal, leaving no room for a non-operating item above the
line.

**And the below-the-line chain is located in full for both Q2 periods — every term filed, not
inferred:**

- **Q2 2026:** `(4,775) − 20,660 − 1,376 + 4,181 = (22,630)` ✓ **EXACT** pre-tax; `(22,630) − 3,909
  = (26,539)` ✓ **EXACT** net. (Interest income and expense, net $(20,660)k; foreign currency
  loss $(1,376)k; gain on the contingent interest feature within the 2024 Debt Repayment
  $4,181k; income tax **expense** $3,909k.)
- **Q2 2025:** `6,146 − 7,428 + 11,966 + 6,697 = 17,381` ✓ **EXACT**; `17,381 − (1,827) = 19,208` ✓
  **EXACT**.
- **H1 2026:** `(35,851) − 5,506 = (41,357)` ✓ **EXACT** net, but the total-other term of
  $(39,246)k is a **back-solve** from the filed subtotals — it is not located on any page read —
  **so the H1 below-the-line reconciliation is reported as closing on the filed sub/supertotals
  and NOT as a term-located check.**

[📄 GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5). **Conclusion: no non-operating item sits
inside GSAT's operating line. The contamination the register warns of is absent here, and the
one candidate is fully explained by the register's other defect.** *Note for the census: the
served `IncomeTaxExpenseBenefit` of +3,125,000 at IRDM is **not** a DA-23 strip — a
sign-convention element presented as a deduction is not a stripped sign, and it must not be
counted as one.*

### DA-25 — CLEAN on the subscriber block, NOT ASKABLE outside it

Reported in full in Mode 2 above: reproduction exact for Duplex, 0.09% for IoT, 0.03% for SPOT,
and the block ties to filed service revenue exactly. **Scope stated with the clearance: it covers
the $18,831k subscriber-services block, 29.1% of total revenue. The other 70.9% of total Q2 2026
revenue — wholesale capacity $40,114k (62.0%) plus equipment sales $4,774k (7.4%) plus
government/other $1,053k (1.6%) — has no per-unit metric to test, which is a genuine absence from
the source, not an ingestion failure.** The detector was run on the comparator side (A12): at
IRDM the identical table is **not** reproducible, because IRDM never tags a subscriber count.
**Two issuers, one detector, opposite verdicts.**

### DA-27 — UNEXERCISED

GSAT has a December fiscal year-end, so the calendar quarter and the fiscal quarter coincide and
no independent test is available in the periods read. **`UNEXERCISED` — not CLEAN.**

### The component identity, stated with its opex definition, 9 of 9 periods exact

**Opex definition: the six filed operating-expense lines — Cost of services; Cost of subscriber
equipment sales; Marketing, general and administrative; Stock-based compensation; Reduction in
the value and disposal of long-lived assets; Depreciation, amortization and accretion — checked
against the filed `Total operating expenses` subtotal, which the statement carries as a filed
subtotal rather than a derived figure.** Because GSAT files **no gross-profit subtotal**, the
inclusive and exclusive constructions are the same statement and converge by definition; the
identity is invariant to which group each line sits in provided each is counted once.

| Period | Revenue − opex (filed subtotal) | = Operating income (filed) |
|---|---|---|
| Q2 2026 | 64,772 − 69,547 | **(4,775)** ✓ |
| Q2 2025 | 67,148 − 61,002 | **6,146** ✓ |
| H1 2026 | 134,836 − 131,441 | **3,395** ✓ |
| H1 2025 | 127,180 − 129,535 | **(2,355)** ✓ |
| Q1 2026 | 70,064 − 61,894 | **8,170** ✓ |
| Q1 2025 | 60,032 − 68,533 | **(8,501)** ✓ |
| FY2021 | 124,297 − 189,800 | **(65,503)** ✓ |
| FY2022 | 148,504 − 369,533 | **(221,029)** ✓ |
| FY2023 | 223,808 − 223,973 | **(165)** ✓ |

[📄 GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5)
[📄 GSAT 10-Q p.4](https://agentii.ai/v/GSAT/sec164/4)
[📄 GSAT 10-K p.45](https://agentii.ai/v/GSAT/sec126/45). **`EPS × shares` was not used as a sign
test anywhere in this artifact.**

### DA-30 — leverage and debt on two bases each; both reported

**The brief's 7.4x leverage reading has a basis, and it is the misleading one.** Total liabilities
$2,152,199k ÷ total equity $292,613k = **7.36x** ✓ (the brief's 7.4x reproduces on this basis).
**But 50.4% of those liabilities are deferred revenue — the customer's prepayments — not
borrowings.** On the interest-bearing basis: $(51,400 + 307,389)k = **$358,789k ÷ $292,613k =
1.23x**. **And the filing uses a *third*, larger basis for the same concept:** *"The principal
amount of our debt outstanding was **$423.7 million** at June 30, 2026, compared to $410.0 million
at December 31, 2025"*, *"which accrues fees at a weighted average stated rate up to 9%"*
[📄 GSAT 10-Q p.38](https://agentii.ai/v/GSAT/sec166/38)
[📄 GSAT 10-Q p.39](https://agentii.ai/v/GSAT/sec166/39). **The balance-sheet carrying basis is
$358,789k; the filing's stated principal basis is $423,700k; the gap is $64,911k and its
decomposition was NOT attempted in this artifact → `UNEXERCISED`.** A reader who takes leverage
from MD&A and equity from the balance sheet is mixing bases (DA-30).

**The headline is not the debt basis at all — it is the equity, and it is thinner than it
looks.** Equity is **11.97%** of assets ($292,613k ÷ $2,444,812k), and the retained deficit is
**$(2,206,570)k** — **7.5x the entire equity base.** *(The brief's $2,137M is the prior-year
figure: the deficit was $(2,136,797)k at 2025-12-31 and is $(2,206,570)k at 2026-06-30
[📄 GSAT 10-Q p.6](https://agentii.ai/v/GSAT/sec166/6).)* **Of that movement, $(28,416)k is the
ASU 2025-07 cumulative-effect catch-up and $+2,602k its in-period reversal — net $(25,814)k of
the $(69,773)k change is an accounting-basis adoption, not operating losses.**

**With deferred revenue at $1,085,545k against equity of $292,613k, GSAT's balance sheet is
financed 3.71x more by its customer's prepayments than by its own shareholders.**

### DA-23-adjacent, platform-level: the wrong share count

Recorded here rather than as a DA number because the register has **no DA-31**: the served
`common_shares_outstanding` of 149,425 is the **preferred** count, against a filed common count of
129,563,390 [📄 GSAT 10-Q p.1](https://agentii.ai/v/GSAT/sec166/1)
[📄 GSAT 10-Q p.6](https://agentii.ai/v/GSAT/sec166/6). **An 867x error that understates value and
therefore never announces itself. Same family as DA-23: a served value that is exactly wrong and
entirely plausible.**

---

## What this artifact could not resolve

| Item | Disposition | Resolving input |
|---|---|---|
| Quantified market share, any line | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a filed share statistic or third-party market census |
| Identity of the 64% customer, from GSAT's own filings | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | GSAT naming the counterparty, or a filed exhibit |
| Comparability of GSAT vs IRDM subscriber bases | `UNEXERCISED` | a filed reconciliation between the two counting bases |
| Debt-basis gap of $64,911k | `UNEXERCISED` | Note 7: Long-Term Debt and Other Financing Arrangements |
| H1 2026 below-the-line total-other term $(39,246)k | back-solve, not term-located | the H1 other-income detail, unread |
| FY2021 / FY2023 served vs filed operating signs | `UNEXERCISED` | a served-fact read for those two annual periods |
| DA-27 fiscal-label test | `UNEXERCISED` | a fiscal year-end not aligned to the calendar |
| Whether the $97M milestone reduction recurs | not yet determinable | the closing conditions as finally satisfied |

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| GSAT sec166 p.5 | [📄 GSAT  p.5](https://agentii.ai/v/GSAT/sec166/5) |
| GSAT sec126 p.45 | [📄 GSAT  p.45](https://agentii.ai/v/GSAT/sec126/45) |
| GSAT sec166 p.38 | [📄 GSAT  p.38](https://agentii.ai/v/GSAT/sec166/38) |
| GSAT sec166 p.11 | [📄 GSAT  p.11](https://agentii.ai/v/GSAT/sec166/11) |
| GSAT sec128 p.10 | [📄 GSAT  p.10](https://agentii.ai/v/GSAT/sec128/10) |
| IRDM sec151 p.27 | [📄 IRDM  p.27](https://agentii.ai/v/IRDM/sec151/27) |
| GSAT sec128 p.11 | [📄 GSAT  p.11](https://agentii.ai/v/GSAT/sec128/11) |
| GSAT sec166 p.39 | [📄 GSAT  p.39](https://agentii.ai/v/GSAT/sec166/39) |
| GSAT sec166 p.33 | [📄 GSAT  p.33](https://agentii.ai/v/GSAT/sec166/33) |
| GSAT sec166 p.29 | [📄 GSAT  p.29](https://agentii.ai/v/GSAT/sec166/29) |
| GSAT sec166 p.44 | [📄 GSAT  p.44](https://agentii.ai/v/GSAT/sec166/44) |
| GSAT sec166 p.42 | [📄 GSAT  p.42](https://agentii.ai/v/GSAT/sec166/42) |
| GSAT sec166 p.1 | [📄 GSAT  p.1](https://agentii.ai/v/GSAT/sec166/1) |
| GSAT sec166 p.6 | [📄 GSAT  p.6](https://agentii.ai/v/GSAT/sec166/6) |
| GSAT sec166 p.7 | [📄 GSAT  p.7](https://agentii.ai/v/GSAT/sec166/7) |
| GSAT sec164 p.4 | [📄 GSAT  p.4](https://agentii.ai/v/GSAT/sec164/4) |
| GSAT sec166 p.34 | [📄 GSAT  p.34](https://agentii.ai/v/GSAT/sec166/34) **(newly surfaced)** |
| GSAT sec166 p.30 | [📄 GSAT  p.30](https://agentii.ai/v/GSAT/sec166/30) **(newly surfaced)** |
| GSAT sec166 p.32 | [📄 GSAT  p.32](https://agentii.ai/v/GSAT/sec166/32) **(newly surfaced)** |
