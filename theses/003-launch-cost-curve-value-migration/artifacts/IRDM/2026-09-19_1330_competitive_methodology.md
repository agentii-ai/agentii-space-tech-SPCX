---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-2
ticker: IRDM
skill: competitive
mode: methodology
generated_at: 2026-09-19T13:30:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "826995c722a4"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: >-
      Absolute-value sign stripping. CONFIRMED at IRDM on four concept-series. Every figure
      in this artifact is read from the FILED page cell; no figure is taken from a served
      fact. `EPS x shares` was not used as a sign test anywhere.
  - da_id: DA-24
    chosen_reading: >-
      Non-operating contamination of operating_income. Tested at IRDM and CLEAN (EXERCISED):
      the served value equals the filed value in 4 of 4 periods and all four below-the-line
      items are filed below the operating line, so contamination above it would have broken
      the component identity.
  - da_id: DA-25
    chosen_reading: >-
      Normalised per-unit metrics not reproducible from audited tables. Read here as a
      kind-5 ingestion absence of a DATUM CLASS, not a metric defect: the ARPU definition IS
      filed (p.25 fn 2) and the table is internally consistent, but subscriber counts are
      never XBRL-tagged. ARPU and subscriber figures are taken from the filed MD&A table.
  - da_id: DA-26
    chosen_reading: >-
      Annual figures mislabelled as quarterly. Locus is the `metrics` array of
      `get_company_financials`. CONFIRMED twice at IRDM. No figure in this artifact is read
      from that array.
  - da_id: DA-28
    chosen_reading: >-
      Capital-structure discontinuity. NOT TESTABLE at IRDM (kind 6, coverage window): the
      FY2009 IPO predates corpus coverage. No share-count or per-share detector in this
      artifact spans it.
  - da_id: DA-29
    chosen_reading: >-
      A reconciliation that closes is not thereby a check. Both reconciliations used here
      (component identity, equity fingerprint) name every term, and every term is located on
      a filed page.
  - da_id: DA-30
    chosen_reading: >-
      Two bases on one concept collapsed. Q2 2026 operating margin is reported on BOTH bases
      (filed 15.10%; ex-transaction-costs 21.45%), leverage on two bases, and the Aireon
      stake on both a carrying-value and a transaction-implied basis.
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "Q2 2026 income statement: revenue 225,237; operating income 34,008; net income 9,679; equity-method loss (1,510)"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 5
    url: https://agentii.ai/v/IRDM/sec191/5
    located_via: read_source_pages
  - figure: "Statements of changes in stockholders' equity: APIC 864,367; accumulated deficit (387,281); AOCI (4,681); total equity 472,511; repurchases 4,927k shares / 136,073"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 6
    url: https://agentii.ai/v/IRDM/sec191/6
    located_via: read_source_pages
  - figure: "Balance sheet: total assets 2,565,093; total stockholders' equity 472,511"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 4
    url: https://agentii.ai/v/IRDM/sec191/4
    located_via: read_source_outline
  - figure: "MD&A overview: 2,627,000 billable subscribers (+144,000 / 6%); Aireon acquisition; 120 service providers, 320 VARs"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 21
    url: https://agentii.ai/v/IRDM/sec191/21
    located_via: read_source_pages
  - figure: "Three-month results table: all five operating-expense lines; total opex 191,229; operating income 34,008; SG&A +22,417 / +50%"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 24
    url: https://agentii.ai/v/IRDM/sec191/24
    located_via: read_source_pages
  - figure: "Commercial services and government services revenue/subscriber/ARPU tables; ARPU definition (fn 2); EMSS fixed at 110.5 million per year"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 25
    url: https://agentii.ai/v/IRDM/sec191/25
    located_via: read_source_pages
  - figure: "Subsequent events: completed acquisition of remaining 60.5% of Aireon Holdings for approximately 366.7 million on July 2, 2026"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 20
    url: https://agentii.ai/v/IRDM/sec191/20
    located_via: read_source_outline
  - figure: "Note 14: Merger Agreement with Rocket Lab, Exchange Ratio, 223.6 million termination fee; Aireon bridge-loan commitment"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 19
    url: https://agentii.ai/v/IRDM/sec191/19
    located_via: read_source_outline
  - figure: "MD&A merger discussion: Exchange Ratio mechanics, closing conditions, interim covenants, board recommendation"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 22
    url: https://agentii.ai/v/IRDM/sec191/22
    located_via: read_source_outline
  - figure: "Operating-expense variances including 14.3 million of transaction costs from the Rocket Lab merger and Aireon acquisition"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 26
    url: https://agentii.ai/v/IRDM/sec191/26
    located_via: read_source_outline
  - figure: "Cover: 105,960,383 common shares outstanding as of July 15, 2026; common stock 0.001 par value"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 2
    url: https://agentii.ai/v/IRDM/sec191/2
    located_via: read_source_outline
  - figure: "Equity transactions: dividends 0.15 per share per quarter; share repurchase program terminated June 28, 2026"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 14
    url: https://agentii.ai/v/IRDM/sec191/14
    located_via: read_source_outline
  - figure: "FY2025 10-K Competition: principal MSS competitors are Viasat, Globalstar, ORBCOMM and Thuraya; maritime mix migration"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 27
    url: https://agentii.ai/v/IRDM/sec151/27
    located_via: read_source_pages
  - figure: "FY2025 10-K industry structure: VSAT providers Eutelsat and SES; Starlink D2D; spectrum purchased from EchoStar in 2025"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 9
    url: https://agentii.ai/v/IRDM/sec151/9
    located_via: read_source_pages
  - figure: "FY2025 10-K spectrum inventory (8.725 MHz L-band) and Aireon ownership: 39.5% fully diluted, 120 million redemption right"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 26
    url: https://agentii.ai/v/IRDM/sec151/26
    located_via: read_source_pages
key_metrics:
  operating_margin_3m_2026_pct: 15.10
  operating_margin_ex_transaction_costs_3m_2026_pct: 21.45
  operating_income_decline_transaction_cost_share_pct: 88.0
  merger_consideration_usd_per_share: 54.00
---

# IRDM — competitive methodology (PIL-2, the operator leg)

## The finding

**The operator leg of PIL-2 tests positive on margin and is extinguished on ownership.**

IRDM reports Q2 2026 operating income of **$34,008 thousand** on **$225,237 thousand** of revenue
— **15.10%**, down from **23.17%** — while revenue grew **3.84%**
[📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5)
[📄 IRDM 10-Q p.24](https://agentii.ai/v/IRDM/sec191/24). That divergence is the finding, and it
divides cleanly:

1. **The licence is durable.** Services revenue — the L-band licence plus the constellation —
   rose 4% to $161,328 thousand, 72% of total revenue, at a *lower* cost of services
   ($51,314 thousand, −4%). The 66-satellite mesh and the 8.725 MHz L-band position are not
   eroding [📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26).
2. **The service business on top of it is not automatically durable.** Of the
   **$16,250 thousand** decline in operating income, **$14,300 thousand — 88.0% — is
   transaction costs**, filed inside SG&A as attributable to *"the Merger Agreement with
   Rocket Lab and the Aireon acquisition"*
   [📄 IRDM 10-Q p.26](https://agentii.ai/v/IRDM/sec191/26). Stripping them leaves an operating
   margin of **21.45%** against 23.17% — a residual decline of **1.72 points, not 8.07**
   (basis: filed, ex-transaction-costs; grade DERIVED, arithmetic on filed cells).
3. **And the entity is not going to be an independent operator.** On June 28, 2026 IRDM signed
   a Merger Agreement with Rocket Lab Corporation
   [📄 IRDM 10-Q p.19](https://agentii.ai/v/IRDM/sec191/19).

**So the PIL-2 operator test does not resolve to a margin verdict. It resolves to an ownership
verdict: the universe's best operator and the universe's worst operator are both being
acquired, and neither survives to be compared with the launcher it competes against.**

**The counter-case to launcher capture is real in the margin and absent in the outcome.** IRDM's
15.10% operating margin is ~39.7 points *better* than Rocket Lab's −24.57% (inherited
correction, thesis 003 workstream). A launcher earning −24.57% does not need to buy an operator
earning +15.10% in order to capture value — unless the value it is buying is not the margin. What
it is buying is disclosed: the demand-side position (government and aviation), the licence, and
Aireon. **Value at the operator was realised by the operator's shareholders through a sale to
the layer above them, at a fixed price.**

---

## Mode 1 — direct-competitor-identification-and-analysis

### The filed competitor set, and it is bilateral

IRDM's FY2025 10-K states its competitor set verbatim: *"our principal mobile satellite services
competitors are **Viasat, Globalstar, ORBCOMM, and Thuraya Telecommunications Co. (Thuraya)**"*
[📄 IRDM 10-K p.27](https://agentii.ai/v/IRDM/sec151/27).

GSAT's FY2025 10-K states the reciprocal: *"Our largest global competitors are **Viasat, Iridium
and ORBCOMM**"*, and of IRDM specifically: *"**Iridium markets products and services that are
similar to those marketed by us.**"*
[📄 GSAT 10-K p.10](https://agentii.ai/v/GSAT/sec128/10).

**Both legs of PIL-2's operator test name each other as direct competitors, in filed documents,
in the same fiscal year.** GSAT goes further and discloses that its SPOT competitor set runs *on
Iridium's network* — *"Garmin's inReach devices … Honeywell Global Tracking … and Somewear … all
of which work on **Iridium's satellite network**"*
[📄 GSAT 10-K p.11](https://agentii.ai/v/GSAT/sec128/11).

### ⚠️ The taxonomy omission is confirmed, and it is invisible

- **IRDM files under `tech.telecom_services`.**
- **GSAT files under `tech.tech_hardware`.**

A comparator set assembled by taxonomy node therefore **includes IRDM and silently omits GSAT**,
while both issuers' own filings place them in the same competitive set and IRDM names Globalstar
first among four. **The two nearest comparable operators in the universe — the only two, on the
filed evidence — are not in the same node, and the resulting set still looks clean.** This is a
platform/corpus property, not an issuer property: the remedy is a curated sector map, and until
one exists **no taxonomy-node comparator set at these two tickers is admissible.** Both bases are
reported here (taxonomy node *and* filed competitor list); neither is quoted alone.

### The structural features of the competitor set (filed, not inferred)

- **Architecture is the filed differentiator.** IRDM's mesh crosslinks vs the *"bent pipe"*
  architecture *"from operators like Globalstar and ORBCOMM"* which *"can only provide real-time
  service when they are within view of a ground station"*
  [📄 IRDM 10-K p.9](https://agentii.ai/v/IRDM/sec151/9).
- **The operators' own filings name the launcher's affiliate as the emerging competitor.** IRDM
  cites *"Starlink's D2D offerings … with plans for a global service in the future utilizing
  spectrum purchased from EchoStar in 2025"*; GSAT cites *"SpaceX's Starlink and Amazon Leo and
  AST SpaceMobile"* and *"recent terrestrial spectrum sales, such as between EchoStar and SpaceX
  and EchoStar and AT&T"* [📄 GSAT 10-K p.10](https://agentii.ai/v/GSAT/sec128/10).
- **Asymmetry worth recording: Amazon is a *listed competitor* of the company it is
  acquiring** (GSAT). **Rocket Lab appears in neither IRDM's nor GSAT's filed competitor set.**
  The launcher's move into IRDM is not a move within a market it already contested; the demand
  owner's move into GSAT is.

### Head-to-head, on the one basis that is filed at both

| | IRDM Q2 2026 | GSAT Q2 2026 | Ratio |
|---|---|---|---|
| Total revenue | $225,237k | $64,772k | 3.48x |
| Operating income | $34,008k | $(4,775)k | — |
| Operating margin | **15.10%** | **−7.37%** | 22.5 pts |
| Subscriber services | $133,700k commercial | $18,831k subscriber-driven | — |
| Total billable subscribers | 2,627,000 | 803,980 | 3.27x |

**This comparison is reported on two different subscriber bases and must not be collapsed
(DA-30).** IRDM counts *"billable subscribers"* at period end; GSAT counts *"the number of
devices that are subject to agreements"* and files the caveat that *"Other providers of
comparable services may count their subscribers differently"*
[📄 GSAT 10-Q p.33](https://agentii.ai/v/GSAT/sec166/33). **There is no universe-level
comparable subscriber metric at these two operators, and no filed reconciliation between the two
bases.** The 3.27x is an order of magnitude, not a share.

The same caveat governs ARPU: IRDM divides revenue by *"the average of the number of billable
subscribers at the beginning of the period and the number … at the end of the period and then
dividing … by the number of months"*
[📄 IRDM 10-Q p.25](https://agentii.ai/v/IRDM/sec191/25); GSAT divides by a directly filed
*"average number of subscribers for the period"*. IoT ARPU of $7.64 vs $4.31 is therefore a
1.77x gap between two different denominators, not a price comparison.

---

## Mode 2 — market-share-dynamics-analysis

### The denominator does not exist, so the mode is a negative finding

**Neither issuer files a market-share statistic, and no such statistic exists in the corpus.**
`list_xbrl_concepts` returns **0** for `MarketShare`, **0** for `Spectrum`, and **0** for
`Subscriber`. This is a **zero by construction** — but not in the sense that warns of a hidden
value: the search returns nothing because no filer ever tags the concept, so a structured query
*can never* return one. **A quantified market-share analysis at IRDM is UNEXERCISED, and the
disposition is `UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — the resolving input is a third-party market
census or a filed share statistic, neither of which any platform can extract from these filings.
**A zero from a structured query is a zero by construction; this leg of the artifact therefore
rests on page text, not on facts, throughout.**

### What the filings do support: the dynamics of the filed base

The observable analogue of share is the migration of the revenue base, and at IRDM the migration
is **dilutive** — it is adding subscribers at the bottom of its own price ladder.

| Commercial line | Revenue Q2 26 | Subs Q2 26 | ARPU | Subs y/y | ARPU y/y |
|---|---|---|---|---|---|
| IoT data | $47.1M | 2,091k | $7.64 | **+167k** | **−$0.19** |
| Voice and data | $58.4M | 402k | $49 | −13k | +$3 |
| Broadband | $11.7M | 16.0k | $243 | −0.3k | **−$17** |
| Hosted payload | $16.5M | n/a | n/a | n/a | n/a |
| **Total commercial** | **$133.7M** | **2,509k** | — | **+154k** | — |

[📄 IRDM 10-Q p.25](https://agentii.ai/v/IRDM/sec191/25)

**Commercial subscribers grew 6.54% while commercial revenue grew 3.80% — revenue per subscriber
fell ~2.6%.** The growth is 100%+ concentrated in the lowest-ARPU line: IoT added 167 thousand
subscribers while voice/data lost 13 thousand and broadband lost 0.3 thousand; the headline
*"2,627,000 billable subscribers … an increase of 144,000, or 6%"*
[📄 IRDM 10-Q p.21](https://agentii.ai/v/IRDM/sec191/21) decomposes **exactly** as
167 − 13 − 0.3 − 10 (government) = 143.7 thousand ✓ (grade DEMONSTRATED; and the two published
subtotals tie: 2,509 + 118 = 2,627 ✓, and 2,355 + 128 = 2,483 ✓).

Broadband's ARPU fell to $243 from $260 *"reflecting the increased prevalence of use of
lower-priced companion plans"* — the same adverse mix migration IRDM files directly in maritime:
*"our business shifted from providing higher value primary connections to mariners, to **lower
value backup and safety connections** on large vessels"*
[📄 IRDM 10-K p.27](https://agentii.ai/v/IRDM/sec151/27).

### ~12% of IRDM's revenue is a contract, not a competitive position

The government services line is **$27,600 thousand** on **118 thousand** subscribers, down from
128 thousand — revenue *flat* while the subscriber count fell 10 thousand, because the EMSS
service fee *"is fixed at $110.5 million per year for the remainder of the term and is **not
based on subscribers or usage**, allowing an unlimited number of users access"*
[📄 IRDM 10-Q p.25](https://agentii.ai/v/IRDM/sec191/25). Cross-check: $27.6M × 4 = $110.4M ✓.

**EMSS is 12.25% of Q2 2026 revenue and it carries its own expiration risk: the contract expires
September 2026, the government may unilaterally extend six months at the same rate, and IRDM
*"expect[s] to enter into [a new EMSS contract] by March 2027"* — a date that only closes against
the September 2026 expiry if the six-month extension is exercised.** There is no filed margin of
safety in that window.

---

## Mode 3 — market-share-evolution-and-competitive-benchmarking

### The operator-versus-launcher margin benchmark

| Issuer | Layer | Q2 2026 operating margin | Prior-year | Revenue y/y | Basis |
|---|---|---|---|---|---|
| **IRDM** | independent operator | **+15.10%** | +23.17% | **+3.84%** | filed, 4 of 4 periods exact |
| **GSAT** | independent operator | **−7.37%** | +9.15% | −3.54% | filed, see GSAT artifact |
| **RKLB** | launcher | **−24.57%** | −41.3% | +62.0% | inherited correction, not recomputed here |
| **SPCX** | integrator | 8.29% launch-only | — | — | inherited; `12.3%` is three things at once |

**The operator is the best-earning layer in the universe and the only layer being acquired at a
price its own filings let us compute.** That is the counter-case. It is answered not by the
margin but by the transaction structure, below.

### The evolution is negative on margin and, on the filed evidence, mostly self-inflicted

Q2 2026 vs Q2 2025, six-month figures on the same basis: revenue $444,294k vs $431,784k
(**+2.90%**), operating income $84,721k vs $110,646k (**−23.4%**), net income $31,273k vs
$52,380k (**−40.3%**). Margin 19.07% from 25.62% [📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5).

The attributable causes are filed and separable: SG&A +$22,417 thousand (**+50%**) of which
$14,300 thousand is deal costs; R&D +$1,251k (+29%); D&A +$1,026k (+2%); cost of services
**−$2,289k (−4%)**; subscriber equipment cost +$2,176k (+19%) on revenue +$1,312k (+7%) — **the
only line whose cost grew faster than its revenue**
[📄 IRDM 10-Q p.24](https://agentii.ai/v/IRDM/sec191/24).

**Two cross-period facts complete the evolution picture.** First, IRDM **bought back 4,927
thousand of its own shares for $136,073 thousand in H1 2025** ($27.62 average) and 2,553 thousand
for $65,595 thousand in Q2 2025 ($25.69 average) — a **zero repurchase in H1 2026**, with the
program **terminated on June 28, 2026, the same date as the Rocket Lab Merger Agreement**
[📄 IRDM 10-Q p.6](https://agentii.ai/v/IRDM/sec191/6)
[📄 IRDM 10-Q p.14](https://agentii.ai/v/IRDM/sec191/14). Against the $54.00 in-band merger
consideration that is **2.10x and 1.96x** on two filed figures. **The board demonstrably
believed the value was at the operator, and acted on it with the company's cash.** Second, IRDM
still paid $32,865 thousand of dividends in H1 2026 ($0.15/share/quarter) *while* its operating
income fell 23.4%.

### Rocket Lab's acquisition of IRDM is priced, and the price is fixed

*"Each share … will be converted into the right to receive (i) $27.00 in cash and (ii) a number of
shares of Rocket Lab common stock equal to the Exchange Ratio"* — **0.4000 if RKLB ≤ $67.50,
$27.00 ÷ price between $67.50 and $112.50, and 0.2400 if RKLB ≥ $112.50** — with a **$223.6
million termination fee**
[📄 IRDM 10-Q p.19](https://agentii.ai/v/IRDM/sec191/19)
[📄 IRDM 10-Q p.22](https://agentii.ai/v/IRDM/sec191/22).

**Arithmetic on those filed terms: the stock half is worth exactly $27.00 at both collar
boundaries and throughout the band, so total consideration is $54.00 per share whenever RKLB
trades between $67.50 and $112.50 (±25% about $90.00) — and the cash half is unconditional at
every price.** Below the band IRDM shareholders bear RKLB's downside at a fixed 0.4000 ratio;
above it they keep the upside at 0.2400.

- Implied equity value: **$54.00 × 105,960,383 shares = $5,721.9M** (shares filed as of
  July 15, 2026 [📄 IRDM 10-Q p.2](https://agentii.ai/v/IRDM/sec191/2)); grade DEMONSTRATED as
  arithmetic, **but conditional on the collar band**, which is why it is stated with its basis
  rather than as a market capitalisation.
- Total interest-bearing debt at June 30, 2026: $12,532k + $1,749,342k = **$1,761,874k**
  [📄 IRDM 10-Q p.4](https://agentii.ai/v/IRDM/sec191/4).

**The operator's price is fixed and the launcher's currency floats.** That is the structurally
important asymmetry for PIL-2: RKLB has committed roughly $27.00 of cash out and about $27.00 of
its own equity per share, and can only make the equity half cheaper by falling below $67.50 — a
fall at which its own shareholders, not IRDM's, absorb the loss. **A launcher paying a fixed price
in a floating currency for an operator earning 15.10% is a launcher admitting that the earnings
are not where its own value is.**

---

## The Aireon transaction — and why any Q3 2026 margin printed from this platform will be wrong

On May 13, 2026 IRDM agreed, and **on July 2, 2026 it closed**, the purchase of *"the remaining
60.5% of equity interests in Aireon Holdings … for approximately $366.7 million, **50% in cash and
50% deferred and in the form of a loan by the Sellers, payable one year following the Aireon
Closing**"* [📄 IRDM 10-Q p.21](https://agentii.ai/v/IRDM/sec191/21)
[📄 IRDM 10-Q p.20](https://agentii.ai/v/IRDM/sec191/20). IRDM already held **39.5%** fully
diluted and accounted for it as an equity-method investment
[📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26); the filed Q2 2026 balance sheet still
carries it unconsolidated, and Q2 2026's **$(1,510)k** *"Loss on equity method investments"* sits
**below the operating line** [📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5).

**Implied remeasurement gain (grade MODELED — it is our derivation, not a filed amount, and so it
can satisfy no falsifier):** 100% implied at $366.7M ÷ 0.605 = $606.1M; the retained 39.5% is
therefore implied at ~**$239.4M**; against the filed carrying value of **$37,511k** the gain is
**~$202M** — **1.25x H1 2026 operating income**… on the *six-month* base of $84,721k, that is
**2.38x H1 2026 operating income** and **6.46x H1 2026 net income** ($31,273k). *(The
implementation brief records these as ~2.1x net income and ~5.6x operating income; **those do not
reproduce on the H1 2026 bases** — the labels appear transposed and neither magnitude matches.
Reported as a correction.)*

Three consequences this artifact will not let a later reader miss:

1. **The gain is created by an acquisition, not by operating performance.** It is the same
   artefact this thesis already carries at SPCX: `+$1,824M` is not evidence of migration because
   it exists because an entity was acquired. **If the PIL-2 map spans Q3 2026, a one-time
   remeasurement of this size distorts it.**
2. **The Q3 2026 distortion may land ABOVE the operating line**, because DA-24 has already been
   demonstrated in this workspace to move non-operating items into `operating_income`. The
   component identity of the Q3 2026 statement — `gross_profit − opex` against the filed
   total-operating-expenses subtotal — must be run before any Q3 2026 IRDM margin is quoted.
3. **Half the cash is a one-year seller loan**, so the transaction adds disclosed leverage
   without an equivalent cash outflow; the $100M Revolving Facility draw for the acquisition is
   separately filed. Two bases on the same leverage concept (DA-30) — report both.

---

## The PIL-2 operator verdict

**PIL-2's wrong_if** is `count_of_universe_issuers_where_launch_segment_operating_margin_exceeds_non_launch_segment_operating_margin`, threshold 0, source `issuer_segment_disclosure`. **A1b is TESTED here, not assumed — and the result at this issuer is a structural exclusion, which is itself the finding.**

**IRDM cannot enter that census, and not because of a missing figure.** It has **no launch
segment**, so the predicate is inapplicable; and it files **no segment operating margin at all**
— its revenue is disaggregated by *service type* (voice/data, IoT, broadband, hosted payload,
government) on a single consolidated operating line. **The two independent operators in this
universe therefore contribute nothing to PIL-2's falsifier — not a negative result, but an
inability to be represented in it.** The falsifier can only be fired by issuers that disclose both
a launch segment and a non-launch segment, i.e. by the launchers themselves. **This is the
artifact's most important methodological result: PIL-2's wrong_if is structurally underexercised
at exactly the leg that is supposed to test it, and a census that reported "0 of N operators
exceeding" would be claiming a test that could not run.** A test that could not run is
`UNEXERCISED`, not `CLEAN`.

**What the operator leg does show, on filed evidence:**

- **Value at the operator layer was real** — 15.10%, the highest operating margin in the
  universe, with the 88% of its decline attributable to deal costs.
- **And it was captured by whoever owned the adjacent layer.** IRDM is bought by the **launcher**
  (Rocket Lab, June 28 2026, $27.00 cash + a value-collared stock half, $223.6M termination fee).
  GSAT is bought by its **demand owner** (Amazon, April 13 2026, $90.00/share). **Both independent
  operators in the universe exit to the layer above them, in the same twelve months.** Neither
  survives as the independent operator PIL-2 posits as the alternative recipient of the pool.
- **The pool did not rest at the operator.** The operator's shareholders received it, at a fixed
  price, from a buyer standing one layer up. **PIL-2 is not refuted by the operator leg — it is
  confirmed in its strongest form: the integrator layer is where the demand sits, and the
  launcher is paying equity to acquire its way into it rather than capturing it organically.**

---

## Data-integrity register — IRDM census

### DA-23 — CONFIRMED. Four concept-series, and thesis 001's clearance is REFUTED

**The component identity is the only reliable detector, and it strips the sign off a filed
negative by serving it as a positive of identical magnitude.** At IRDM:

**(1) The equity fingerprint closes exactly — and only on the filed signs.**
`106 + 864,367 − 387,281 − 4,681 = 472,511` ✓ **EXACT**, against the filed total stockholders'
equity of $472,511 thousand [📄 IRDM 10-Q p.6](https://agentii.ai/v/IRDM/sec191/6)
[📄 IRDM 10-Q p.4](https://agentii.ai/v/IRDM/sec191/4). Served with the two negative components
stripped, the same cells give **1,256,435** — an excess of **783,924 = 2 × (387,281 + 4,681)**
✓, which is the arithmetic signature of two simultaneous strips.

**(2) The bidirectional control that A17 requires, at three positive instances.** The same
fingerprint closes exactly on the *positive* side of the same concept:

| Date | AOCI as filed | Served | Verdict |
|---|---|---|---|
| 2025-12-31 | **+406** | +406,000 | **correctly preserved** |
| 2025-06-30 | **+9,303** | +9,303,000 | **correctly preserved** |
| 2024-12-31 | **+18,271** | +18,271,000 | **correctly preserved** |
| 2026-06-30 | **(4,681)** | +4,681,000 | **STRIPPED** |
| 2026-03-31 | (1,712) | +1,712,000 | **STRIPPED** |

[📄 IRDM 10-Q p.6](https://agentii.ai/v/IRDM/sec191/6). **This is the strongest admissible form of
the proof: the concept is genuinely bidirectional — both signs are filed — and it exhibits
negative-filed instances.** The clearance is therefore scoped to a bidirectional concept *and*
evidenced, which is what makes it a clearance rather than an absence.

**(3) `IncomeLossFromEquityMethodInvestments`** — served **+1,510,000 / +2,242,000** against filed
**$(1,510)k / $(2,242)k** [📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5). The line sits
*after* tax, so the sign is forced by the statement's own arithmetic:
`14,314 − 3,125 − 1,510 = 9,679` ✓ and `45,467 − 11,952 − 2,242 = 31,273` ✓.

**(4) `OtherNonoperatingIncomeExpense`** — served **+448,000 / +642,000** against filed
**$(448)k / $(642)k**; `14,314 = 34,008 − 19,246 − 448` ✓ forces the negative.
`RetainedEarningsAccumulatedDeficit` is served as **+387,281,000** and **+446,674,000** against
filed **$(387,281)k** and **$(446,674)k**.

**⚠️ Thesis 001's "5/5 clean" clearance of IRDM is REFUTED, and the grade is WITHHELD.** Four
concept-series strip. **Additionally, the operating-line clearance is `UNEXERCISED`, not CLEAN:**
`OperatingIncomeLoss` served as **+34,008,000** is *correct*, but **every IRDM operating figure in
every period examined is positive**, so the concept has no negative-filed instance and the
detector cannot be exercised on it. **A clearance is admissible only if scoped to bidirectional
concepts and exhibited with a negative-filed instance; otherwise it is `UNEXERCISED`.** IRDM's
operating line is the second case.

### DA-26 — CONFIRMED twice

Locus: the `metrics` array of `get_company_financials`. The **Q4-2025 row carries FY2025
annuals** (revenue 871,659; operating income 235,980; EPS 1.06) and the **Q4-2024 row carries
FY2024 annuals** (830,682; 200,384; 0.94). Inflation ratios `871,659 / 212,940 = 4.094x` and
`235,980 / 55,249 = 4.271x` — **both are FY2025 figures against a Q4-2025 denominator; neither
row is a Q4-2025 vs Q4-2024 comparison.** True Q4 2025 quarterly revenue is 212,940, confirmed
two ways (earnings calendar; FY 871,659 − 9M 658,719). **The defect is per-concept, not
per-row.** Note the contrast: **`search_xbrl_facts` with `fiscal_period: "Q4"` returns zero at
IRDM in every period — also a zero by construction, because a 10-K files no Q4-only duration
fact.** Two different surfaces, two different silent zeros.

### DA-25 — NOT TESTABLE (kind 5: ingestion absence of a datum class)

The ARPU **definition is filed** in full [📄 IRDM 10-Q p.25](https://agentii.ai/v/IRDM/sec191/25),
and the table is internally consistent. **Subscriber counts exist only as MD&A prose — 2,627,000
at 2026-06-30 against 2,483,000 — and are never XBRL-tagged.** `list_xbrl_concepts` returns 0 for
`Subscriber`. **The absence is of the datum class, not of the metric: the issuer never files a
structured subscriber fact, so no platform can serve one.** Class:
`UNRESOLVABLE-FROM-PUBLIC-SOURCES`; the resolving disclosure is an XBRL-tagged subscriber-count
fact. **Control run on the comparator side (A12):** at GSAT the same table **reproduces** from
filed revenue — `57.44 × 15,755 × 3 = $2,714,902` against filed Duplex revenue of $2,715k ✓
EXACT, IoT within 0.09%, SPOT within 0.03%. **The detector was run on both sides, and the IRDM
result is a genuine ingestion absence rather than a defect in the per-unit metric.**

### DA-28 — NOT TESTABLE (kind 6: coverage window), with a correction to the brief

**The IPO falls outside coverage.** The implementation brief dates the coverage window's opening
at 2022-02-17; **that is wrong** — the corpus serves IRDM 10-Ks back to FY2014/FY2015
(`sec140`/`sec141`). **The conclusion is unchanged: the FY2009 IPO is outside it either way.**
Disposition class differs from DA-25's and the remedy is different: the 2009 capital structure
exists on EDGAR and is missing from the *corpus*, so this is
`UNRESOLVABLE-FROM-PLATFORM` (extend coverage), whereas DA-25 is
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` (the disclosure does not exist anywhere in structured form).
**The frontmatter records the dominant class; both are named here so neither is hidden.**

### DA-24 — CLEAN (EXERCISED)

The served `OperatingIncomeLoss` equals the filed value in **4 of 4** periods, and all four
below-the-line items — interest, other, tax, equity-method loss — are filed **below** the
operating line, so any of them leaking above it would have broken the identity. The one
candidate is not a mis-extraction: the **$14,300 thousand** of Rocket Lab/Aireon transaction
costs sits inside SG&A **as a filed classification choice**, and it is disclosed as such. It is
correctly graded as an operating expense; it is *not* correctly comparable to a prior period, and
this artifact reports the margin on both bases rather than choosing one.

### DA-29 — satisfied, not merely closed

Both reconciliations used here — the component identity and the equity fingerprint — **name every
term, and every term is located on a filed page.** The component identity, stated with its opex
definition: **opex = the filed `Total operating expenses` subtotal, which INCLUDES the two
cost-of-revenue lines**; equivalently, with gross profit taken as revenue − cost of services −
cost of subscriber equipment, opex = R&D + SG&A + D&A. **Both constructions converge, because the
filed statement carries no gross-profit subtotal at all** (revenue → operating expenses →
operating income), which is why the definition must be stated rather than assumed:

| Period | Revenue − opex (filed subtotal) | = Operating income (filed) | Inclusive construction | Exclusive construction |
|---|---|---|---|---|
| Q2 2026 | 225,237 − 191,229 | **34,008** ✓ | 160,445 − 126,437 = 34,008 ✓ | ✓ converges |
| Q2 2025 | 216,906 − 166,648 | **50,258** ✓ | 152,001 − 101,743 = 50,258 ✓ | ✓ converges |
| H1 2026 | 444,294 − 359,573 | **84,721** ✓ | 317,352 − 232,631 = 84,721 ✓ | ✓ converges |
| H1 2025 | 431,784 − 321,138 | **110,646** ✓ | 308,933 − 198,287 = 110,646 ✓ | ✓ converges |

[📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5)
[📄 IRDM 10-Q p.24](https://agentii.ai/v/IRDM/sec191/24). **`EPS × shares` was not used as a sign
test anywhere in this artifact.**

### DA-30 — four concepts on two bases each, all reported

Operating margin (filed 15.10% / ex-deal-costs 21.45%); leverage (total liabilities ÷ equity
4.43x *vs* interest-bearing debt ÷ equity 3.73x, with deferred revenue $79,181k = **3.8%** of
liabilities — so IRDM's leverage is borrowings, unlike GSAT's); the Aireon stake (carrying value
$37,511k *vs* transaction-implied ~$239.4M); and the merger consideration ($54.00 in-band, with
its two tail regimes stated). Equity/assets = **18.42%**.

---

## What this artifact could not resolve

| Item | Disposition | Resolving input |
|---|---|---|
| Quantified market share, any line | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a filed share statistic or third-party market census |
| Subscriber counts as structured data | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | an XBRL-tagged subscriber-count fact |
| FY2009 IPO capital structure (DA-28) | `UNRESOLVABLE-FROM-PLATFORM` | corpus coverage extended to pre-2014 filings |
| Comparability of IRDM vs GSAT subscribers | `UNEXERCISED` | a filed reconciliation between the two subscriber bases |
| Operating-line DA-23 detection | `UNEXERCISED` | a period with a negative-filed operating income |
| IRDM's realised D2D/EMSS re-contract outcome | not yet determinable | the post-March-2027 EMSS contract |

**The two operators' subscriber bases are not reconcilable from public sources, and this is not a
platform defect.** IRDM counts billable subscribers; GSAT counts devices under agreement and
states that comparable providers may count differently. **Any universe-level subscriber-share
figure computed by ratio across these two issuers is a basis collapse (DA-30) and should be
refused.**

---

## Sources

> Every figure asserted above resolves to the page cited. Inline citations appear at the point of
> use; this table is the complete list.

| Figure | Source |
|---|---|
| Q2 2026 income statement: revenue 225,237; five opex lines; operating income 34,008; net income 9,679 | [📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5) |
| Statements of changes in equity: APIC 864,367; deficit (387,281); AOCI (4,681); equity 472,511; repurchases 4,927k/$136,073k | [📄 IRDM 10-Q p.6](https://agentii.ai/v/IRDM/sec191/6) |
| Balance sheet: total assets 2,565,093; total equity 472,511; debt 12,532 + 1,749,342 | [📄 IRDM 10-Q p.4](https://agentii.ai/v/IRDM/sec191/4) |
| MD&A: 2,627,000 subscribers; Aireon acquisition; distribution network | [📄 IRDM 10-Q p.21](https://agentii.ai/v/IRDM/sec191/21) |
| Three-month results table and operating-expense variances | [📄 IRDM 10-Q p.24](https://agentii.ai/v/IRDM/sec191/24) |
| Commercial/government revenue, subscriber and ARPU tables; ARPU definition; EMSS $110.5M | [📄 IRDM 10-Q p.25](https://agentii.ai/v/IRDM/sec191/25) |
| Subsequent events: Aireon 60.5% closed July 2, 2026 for ~$366.7M | [📄 IRDM 10-Q p.20](https://agentii.ai/v/IRDM/sec191/20) |
| Note 14: Rocket Lab Merger Agreement, Exchange Ratio, $223.6M termination fee | [📄 IRDM 10-Q p.19](https://agentii.ai/v/IRDM/sec191/19) |
| MD&A merger discussion: closing conditions, covenants, board recommendation | [📄 IRDM 10-Q p.22](https://agentii.ai/v/IRDM/sec191/22) |
| $14.3M transaction costs attributable to the Rocket Lab merger and Aireon acquisition | [📄 IRDM 10-Q p.26](https://agentii.ai/v/IRDM/sec191/26) |
| 105,960,383 common shares outstanding at July 15, 2026 | [📄 IRDM 10-Q p.2](https://agentii.ai/v/IRDM/sec191/2) |
| Dividends $0.15/share/quarter; repurchase program terminated June 28, 2026 | [📄 IRDM 10-Q p.14](https://agentii.ai/v/IRDM/sec191/14) |
| FY2025 competitor set: Viasat, Globalstar, ORBCOMM, Thuraya; maritime mix migration | [📄 IRDM 10-K p.27](https://agentii.ai/v/IRDM/sec151/27) |
| Industry structure: Eutelsat, SES, Starlink D2D, EchoStar spectrum sale | [📄 IRDM 10-K p.9](https://agentii.ai/v/IRDM/sec151/9) |
| Spectrum 8.725 MHz L-band; Aireon 39.5% fully diluted; $120M redemption right | [📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26) |
| Reciprocal competitor naming, GSAT side | [📄 GSAT 10-K p.10](https://agentii.ai/v/GSAT/sec128/10) |
| GSAT SPOT competitors running on Iridium's network | [📄 GSAT 10-K p.11](https://agentii.ai/v/GSAT/sec128/11) |
| GSAT subscriber basis caveat and ARPU reproduction control | [📄 GSAT 10-Q p.33](https://agentii.ai/v/GSAT/sec166/33) |
