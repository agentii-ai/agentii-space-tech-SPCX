---
thesis_id: "002-evidence-validation"
pillar: PIL-2
ticker: VRT
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "VERIFIED CLEAN at VRT, from components, in-line. The identity is run in BOTH admissible forms — (i) `gross profit − opex` and (ii) the calculation-linkbase arc set — and both close on 637.9 exactly. `EPS × shares` was NOT used, and is recorded as inadmissible. Separately: the platform's calculation-arc INSTRUMENT reports four sign-inverted pairs on this accession while never testing `OperatingIncomeLoss` at all, whose arcs demonstrably exist — a detector-coverage gap, not a pass."
  - da_id: "DA-04"
    chosen_reading: "terrestrial basis reported as a SUPPLIER economics structure (equipment margin, capex intensity, order book), never as a cost-per-kW. VRT does not disclose $/kW of cooling; that scope limit is inherited from 001 and re-confirmed here (zero hits for `megawatt` and for `PUE` in the Q2 2026 10-Q)."
  - da_id: "DA-05"
    chosen_reading: "ALL THREE BASES REPORTED, none collapsed — Basis A (hyperscaler marginal cost/kW): OUT OF REACH. Basis B (colocation market price/kW): OUT OF REACH, and structurally so, because VRT *sells equipment to* colocation operators, making its revenue per unit a supplier price rather than a market rental price. Basis C (new-build fully-loaded cost/kW): PARTLY BOUNDED, and the bound is one-sided — VRT bounds the cooling/power EQUIPMENT share of a greenfield build, not land, shell, power interconnect or IT load."
  - da_id: "DA-25"
    chosen_reading: "normalised per-unit metrics. The single per-unit figure produced here ($3.25–3.75M of VRT content per MW) is reported as a BOUNDED OBSERVATION with its basis mismatch stated: the numerator is a whole-powertrain-plus-thermal content figure and the denominator is SPCX's nameplate MW, so the ratio is one-sided and is not substituted into any filed series."
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "Q2 2026 income statement — products 2,646.7 / services 627.6 / net sales 3,274.3; cost of sales 2,039.4; SG&A 494.4; amortization 73.7; restructuring (3.9); foreign currency loss 3.9; other operating expense 28.9; operating profit 637.9; interest 17.4; pre-tax 620.0; tax 122.2; net income 497.8"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 5
    url: https://agentii.ai/v/VRT/sec136/5
    located_via: read_source_pages
  - figure: "Results of operations — net sales 3,274.3 vs 2,638.1 (+24.1%); cost of sales 2,039.4; gross profit 1,234.9 vs 896.6 (37.7% vs 34.0%); SG&A 494.4 (+25.0%); amortization 73.7 (+57.1%); other operating expense 28.9 (+285.3%); operating profit 637.9 (+44.2%); VERBATIM 'Margin expansion in the second quarter of 2026 was primarily driven by the mix of product and service sales'"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 28
    url: https://agentii.ai/v/VRT/sec136/28
    located_via: read_source_pages
  - figure: "SG&A 15.1% vs 15.0% of sales; Americas net sales 2,070.8 (+29.2%), operating profit 571.4 (+48.6%), margin 27.6% vs 24.0% — VERBATIM 'margin increased primarily due to the mix of product and service sales in addition to operational leverage'"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 29
    url: https://agentii.ai/v/VRT/sec136/29
    located_via: read_source_pages
  - figure: "APAC net sales 719.9 (+28.5%), operating profit 95.6 (+61.5%), margin 13.3% vs 10.6%; EMEA net sales 483.6 (+1.7%), operating profit 124.2 (+19.2%), margin 25.7% vs 21.9%; Corporate and other $79.6 vs $58.7 including a $28.8 loss on change in fair value of contingent consideration (PurgeRite)"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 30
    url: https://agentii.ai/v/VRT/sec136/30
    located_via: read_source_pages
  - figure: "Note 11 segment reconciliation — segment cost of sales 2,024.4, marketing/sales/service 191.2, ER&D 139.9, IT 57.8, other segment items 69.8; segment operating profit Americas 571.4 + APAC 95.6 + EMEA 124.2 = 791.2; less FX (3.9), Corporate (75.7) and amortization (73.7) = total operating profit 637.9"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 21
    url: https://agentii.ai/v/VRT/sec136/21
    located_via: read_source_pages
  - figure: "Note 4 revenue disaggregation — products 2,606.4 / services & spares 667.9 = 3,274.3 (Q2 2026); products 2,118.9 / services & spares 519.2 = 2,638.1 (Q2 2025). This is a DIFFERENT product/service split from the income statement's 2,646.7 / 627.6 — a $40.3M reclassification between the two lines"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 13
    url: https://agentii.ai/v/VRT/sec136/13
    located_via: read_source_pages
  - figure: "Capital expenditure — $288.5M in H1 2026; FY2026 capex guidance $550.0–$570.0M 'to support capacity expansion across the business'; cash $2,810.6M and revolver availability $2,483.6M"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 34
    url: https://agentii.ai/v/VRT/sec136/34
    located_via: read_source_pages
  - figure: "NEGATIVE RESULT, located — the phrase 'gross margin' appears in the Q2 2026 10-Q only on pages 28 and 31 (consolidated results of operations). There is NO gross margin disclosed by product/service line and NO gross margin disclosed by segment; segment reporting terminates at operating profit. The filing therefore attributes the gross-margin expansion to product/service mix while never disclosing gross margin by product or service."
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 28
    url: https://agentii.ai/v/VRT/sec136/28
    located_via: search_keyword_in_source
  - figure: "Order backlog — VERBATIM 'Vertiv's estimated combined order backlog was $15.0 billion and $7.2 billion as of December 31, 2025 and 2024, respectively, as continued strong demand has contributed to an increase in customer orders being placed in advance of our ability to fulfill them'; 'the majority ... is considered firm and is expected to be shipped within the next 12 to 18 months'; 'Orders may be subject to cancellation or rescheduling by the customer'"
    ticker: VRT
    form_type: 10-K
    citation_id: sec110
    page_no: 9
    url: https://agentii.ai/v/VRT/sec110/9
    located_via: read_source_pages
  - figure: "Competition — 'niche players (e.g., Delta Electronics, Inc., Stulz GmbH, Johnson Controls International PLC, and Socomec Holding SA) and large-scale global competitors (e.g., Schneider Electric, S.E., Eaton Corporation Plc, Legrand SA, and Huawei Investment & Holding Co., Ltd.)'; competition 'primarily on the basis of reliability, quality, price, service and customer relationships'"
    ticker: VRT
    form_type: 10-K
    citation_id: sec110
    page_no: 10
    url: https://agentii.ai/v/VRT/sec110/10
    located_via: read_source_pages
  - figure: "FY2025 — net sales $10,229.9M (+27.7%); gross profit 3,715.2 (36.3%) vs 2,934.2 (36.6%) in 2024; operating profit 1,829.7 vs 1,367.4 (+33.8%). VERBATIM on the flat gross margin: 'Margin was relatively flat as benefits from higher sales volume and improved price realization were offset by cost inflation, particularly related to tariffs'"
    ticker: VRT
    form_type: 10-K
    citation_id: sec110
    page_no: 41
    url: https://agentii.ai/v/VRT/sec110/41
    located_via: read_source_pages
  - figure: "Capacity expansion — 'Since late 2021, Vertiv has more than doubled its manufacturing capacity for switchgear, busbar and integrated power solutions'; new Pune, India thermal management facility opened 2024, producing in-row and wall-mount units through to large direct expansion and free-cooling systems"
    ticker: VRT
    form_type: 10-K
    citation_id: sec110
    page_no: 39
    url: https://agentii.ai/v/VRT/sec110/39
    located_via: read_source_pages
  - figure: "Q1 2026 income statement — net sales 2,649.5 vs 2,036.0; products 2,135.8 vs 1,649.7; services 513.7 vs 386.3; cost of sales 1,649.8; SG&A 456.7; amortization 77.6; operating profit 440.1 vs 290.7; net income 390.1"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec134
    page_no: 5
    url: https://agentii.ai/v/VRT/sec134/5
    located_via: read_source_pages
  - figure: "Q1 2026 gross profit 999.7 = 37.7% vs 686.5 = 33.7%; SG&A 17.2% vs 17.0% of sales; VERBATIM 'Margin increased in the first quarter of 2026 due primarily to the mix of product and service sales in addition to operational leverage'"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec134
    page_no: 26
    url: https://agentii.ai/v/VRT/sec134/26
    located_via: read_source_pages
  - figure: "Q2 2026 earnings call — THE PER-MW FIND: analyst restates 'Vertiv's 800-volt DC offering could be toward the higher end of that 3.25 million to 3.75 million per megawatt range you gave us at the Analyst Day'; management does not dispute it and replies 'we are pretty convinced about that ... we see value there for Vertiv and an expansion of revenue per TAM per megawatt ... think about the entire powertrain, all the elements ... with that density, with that complexity, our content is impacted favorably'"
    ticker: VRT
    form_type: earnings_call_transcript
    citation_id: ect27
    page_no: 4
    url: https://agentii.ai/v/VRT/ect27/4
    located_via: read_source_pages
  - figure: "Q2 2026 earnings call — adjusted operating margin 22.6%, +410 bps; adjusted operating profit $738M (+51%); VERBATIM 'Pricing continues to be favorable. We expect positive price cost in 2026, including the current impact of tariffs and countermeasures'; capacity online (Johor Malaysia, five large Americas plant expansions, EMEA chiller capacity); FY guide net sales $14B, adj EPS $6.70, capex at high end of 4% of 2026 sales; net cash position"
    ticker: VRT
    form_type: earnings_call_transcript
    citation_id: ect27
    page_no: 1
    url: https://agentii.ai/v/VRT/ect27/1
    located_via: read_source_pages
  - figure: "Q2 2026 earnings call — organic +18% / acquisitions +5% / FX +1%; Americas +21% organic, APAC +26% organic, EMEA −2% organic; margin expansion attributed to 'strong operational execution, continued productivity gains, and favorable price cost execution, partially offset by tariff impacts'; Q3 2026 guide adjusted operating margin 24.5%, +220 bps; FY2026 guide adjusted operating margin 23.8%, +340 bps"
    ticker: VRT
    form_type: earnings_call_transcript
    citation_id: ect27
    page_no: 2
    url: https://agentii.ai/v/VRT/ect27/2
    located_via: read_source_pages
  - figure: "Q2 2026 earnings call — EMEA margin durability concession, VERBATIM: 'the gain that you saw in margin, was a favorable comp too, as you had mentioned, the Ireland portion did come through Q2 last year, which was in EMEA'; separately 800V adoption described as 'gradual' with 400V DC also in play"
    ticker: VRT
    form_type: earnings_call_transcript
    citation_id: ect27
    page_no: 6
    url: https://agentii.ai/v/VRT/ect27/6
    located_via: read_source_pages
  - figure: "Q1 2026 earnings call — adjusted operating margin 20.8%, +430 bps; Americas +53% (+44% organic); APAC +15% (+12% organic); EMEA −29% organic; FY2026 guide originally 23.3% adjusted operating margin, +290 bps; capex described as investing in capacity and ER&D"
    ticker: VRT
    form_type: earnings_call_transcript
    citation_id: ect26
    page_no: 2
    url: https://agentii.ai/v/VRT/ect26/2
    located_via: read_source_pages
  - figure: "Calculation linkbase — the role UNAUDITEDCONDENSEDCONSOLIDATEDSTATEMENTSOFEARNINGSLOSS carries SEVEN arcs into us-gaap:OperatingIncomeLoss (Revenue +1; RestructuringCharges −1; vrt_AmortizationOfIntangibleAssetsExcludingCostsOfSales −1; SellingGeneralAndAdministrativeExpense −1; ForeignCurrencyTransactionGainLossBeforeTax +1; CostOfGoodsAndServicesSold −1; OtherOperatingIncomeExpenseNet +1), and that arc set closes on 637.9 with signed values. Yet validate_calculation returns NO result for OperatingIncomeLoss on this accession"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 5
    url: https://agentii.ai/v/VRT/sec136/5
    located_via: read_source_pages
---

# VRT — Terrestrial Cooling Comparator, Phase 2 (F2 physics inputs)

Source: Form 10-Q for the quarter ended 2026-06-30, accession `0001628280-26-050609`,
filed 2026-07-29 (platform `citation_id` `sec136`, 41 pages); Form 10-K for FY2025,
accession `0001674101-26-000008`, filed 2026-02-13 (`sec110`, 99 pages); Form 10-Q for
the quarter ended 2026-03-31 (`sec134`); Q2 2026 earnings call of 2026-07-29 (`ect27`);
Q1 2026 earnings call of 2026-04-22 (`ect26`).

**Pillar**: PIL-2 (F2's unsourced constants). VRT enters F2 not as a source for F2's own
constant — the orbital radiator mass per MW is set by physics, not by a terrestrial
vendor — but as the **comparator that sets the penalty**. F2 asks what orbital cooling
costs in mass per MW; the question of whether that penalty is *worth paying* is a
question about the terrestrial alternative. This artifact bounds that alternative.

**Inherited, not re-derived.** 001's `VRT/2026-09-18_1239_unit-economics_methodology.md`
already established the headline figures (revenue $3,274.3M +24.1%; gross profit
$1,234.9M at 37.7%; operating income $637.9M +44.2% at 19.5% vs 16.8%; net income
$497.8M +53.5%) and the scope limit that **VRT does not disclose $/kW of cooling**. Both
are re-confirmed at source here and neither is recomputed. What is *new* is the
bounding, the durability test, and one correction to 001's DA-23 evidence.

---

## 1. Instrument compliance — DA-23 at VRT, from components, in-line

### 1.1 The component identity

The register requires `operating_income` to be shown as `gross profit − opex` in-line.
VRT's Q2 2026 income statement, read at
[📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec136/5):

```
Net sales                                                  3,274.3
Cost of sales                                             (2,039.4)
                                                        ----------
Gross profit                                               1,234.9   = 37.71% of sales

  Selling, general and administrative                       (494.4)
  Amortization of intangibles                                (73.7)
  Restructuring                                                3.9   (a benefit, shown parenthesised as (3.9))
  Foreign currency loss                                       (3.9)
  Other operating expense                                    (28.9)
                                                        ----------
  opex subtotal                                              597.0
                                                        ----------
Operating profit                                             637.9
```

**1,234.9 − 597.0 = 637.9, exactly.** No rounding residue. VRT is **DA-23-clean**, and 001's
conclusion stands — but by a different route: 001's stated confirmation was the
`EPS × shares` test, which the 002 register declares **inadmissible**. The admissible test
is the one above, and it is the first time it has been run on VRT. 001's *verdict* was
right; its *evidence* was not admissible, and is here replaced.

### 1.2 Arc-level corroboration — and a detector-coverage gap for PIL-3

The calculation linkbase for this accession was retrieved. The role
`UNAUDITEDCONDENSEDCONSOLIDATEDSTATEMENTSOFEARNINGSLOSS` carries **seven arcs** into
`us-gaap:OperatingIncomeLoss`:

| Child | Weight |
|---|---|
| `RevenueFromContractWithCustomerExcludingAssessedTax` | +1 |
| `CostOfGoodsAndServicesSold` | −1 |
| `SellingGeneralAndAdministrativeExpense` | −1 |
| `vrt_AmortizationOfIntangibleAssetsExcludingCostsOfSales` | −1 |
| `RestructuringCharges` | −1 |
| `ForeignCurrencyTransactionGainLossBeforeTax` | +1 |
| `OtherOperatingIncomeExpenseNet` | +1 |

Summing with **signed** values (restructuring carries −3.9 in XBRL because it is a credit,
so the −1 weight yields +3.9; FX and other-operating likewise carry their negative signs)
reproduces **637.9 exactly**. The arc set and the component identity agree, which is the
strongest available corroboration.

**The instrument finding.** `validate_calculation` returns results for `NetIncomeLoss`,
`AssetsCurrent`, `LiabilitiesAndStockholdersEquity`,
`NetCashProvidedByUsedInInvestingActivities` and others — but returns **no result at all
for `OperatingIncomeLoss`**, despite its arc set demonstrably existing. Per the instrument
rule the `status` column was not read; the `computed` vs `reported` pairs were read
instead, and they are self-evidently unusable on this accession:

| Concept | `computed` | `reported` |
|---|---|---|
| `NetIncomeLoss` (H1 2025) | −139.1M | 488.7M |
| `NetCashProvidedByUsedInInvestingActivities` | −780.7M | **+780.7M** |
| `PropertyPlantAndEquipmentNet` | −403.1M | 921.8M |
| `LiabilitiesAndStockholdersEquity` | 11,146.9M | 15,909.0M |

The investing-activities pair is a **pure sign inversion on the computed side** — the
DA-23 failure mode reappearing in the arc layer rather than the fact layer. Consistent
with the sibling SPCX artifact, these are **arc-selection artefacts**: a single period's
arc set is applied across all comparative periods in the filing.

**Two findings hand to PIL-3.** (i) The arc instrument does not test a concept whose arcs
exist — the same *absence rather than wrong value* hazard class the spec registers for the
pharma issuers, but here appearing as an instrument coverage gap rather than a source gap.
(ii) The arc instrument's failures on this accession are **100% false-positive by
construction** (9 fail / 6 pass / 2 warn, none usable), which independently corroborates
the 93%-false-positive rate the constitution registers.

---

## 2. Job 1 — Bounding the cooling equipment share of a terrestrial build

VRT's three reportable segments are **geographic** (Americas, Asia Pacific, EMEA) — read at
[📄 VRT 10-Q p.21](https://agentii.ai/v/VRT/sec136/21) and
[📄 VRT 10-K p.8](https://agentii.ai/v/VRT/sec110/8). There is **no thermal-versus-power
revenue split anywhere in the filing**, and segment reporting terminates at operating
profit — there is no segment gross margin either. So no bound can be constructed from a
disclosed cooling revenue line. Four indirect bounds are available instead, and they are
mutually reinforcing.

### 2.1 Bound α — VRT content per MW (transcript-only, and it is a whole-chain figure)

On the Q2 2026 call, an analyst restates a figure management does not dispute:

> *"…would you surmise that Vertiv's 800-volt DC offering could be toward the higher end of
> that **3.25 million to 3.75 million per megawatt range** you gave us at the Analyst Day."*
> — [📄 VRT earnings_call_transcript p.4](https://agentii.ai/v/VRT/ect27/4)

Management's reply confirms the direction and — critically — the **scope**: *"think about
the entire powertrain, all the elements … with that density, with that complexity, our
content is impacted favorably."* This is VRT content across **power train plus thermal plus
services**, not cooling alone.

Set against the denominator established in the sibling SPCX artifact — AI-segment capex of
**$15,828M** in Q2 2026 across **0.4 GW** of nameplate added, i.e. **$39.6M per MW of
nameplate** and **$26.4M per MW of facility-side power** at the 1.5× restatement
(`artifacts/SPCX/2026-09-18_1500_operational-kpi_methodology.md` §3.2):

| Comparison | Range | Midpoint | Half-width |
|---|---|---|---|
| VRT content ÷ SPCX facility-side capex ($26.4M/MW) | **12.3% – 14.2%** | 13.3% | **±7.1%** |
| VRT content ÷ SPCX nameplate capex ($39.6M/MW) | **8.2% – 9.5%** | 8.8% | ±7.1% |

**This is a one-sided bound on cooling, and the direction matters.** The full powertrain
plus thermal plus services chain — VRT's *entire* content opportunity per MW — is
12–14% of what SPCX spends per MW of facility-side power. Cooling alone is **strictly less
than that**. So terrestrial cooling equipment is bounded **above** at ~12–14% of facility
capex per MW. The bound does not give a cooling-only number, but it does establish that
the cooling equipment line is a **minority component** of a terrestrial build, and it is
an *upper* bound in the direction that matters for the orbital case.

**Caveat that must travel with this figure.** The $3.25–3.75M/MW originates from VRT's
Investor Day deck, a non-filed document not on the platform; it reaches this artifact
through an analyst's restatement on a filed-adjacent transcript, undisputed by management.
It is therefore **CLAIMED, not DEMONSTRATED**, and under the same admissibility logic the
spec applies at Q-1, a company's own figure is not adjudication. It is used here to
*bound*, never to populate.

### 2.2 Bound β — the supplier's cost/price structure

For every $1.00 of VRT revenue in Q2 2026
([📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec136/5)): cost of sales $0.62, gross profit
$0.38, SG&A $0.15, all other operating items $0.03, operating profit $0.19. This bounds
**the margin available in terrestrial cooling and power supply** — it says nothing about
the share of a build, which is why 001 graded Basis C "partly" rather than "yes."

### 2.3 Bound γ — capex intensity: the supply response is cheap

This is the bound 001 did not have, and it is the most directly adversarial to the
"bottleneck" framing. H1 2026 capital expenditure was **$288.5M on H1 revenue of
$5,923.8M — 4.9% of sales** — and FY2026 capex is guided to **$550.0–$570.0M** against
guided FY revenue of $14B, i.e. **3.9%–4.1% of sales**, described by the CFO as the
"high end of 4% of 2026 sales"
([📄 VRT 10-Q p.34](https://agentii.ai/v/VRT/sec136/34);
[📄 VRT earnings_call_transcript p.1](https://agentii.ai/v/VRT/ect27/1)).

**A capacity bottleneck shows up as capital intensity. VRT's is 4–5% of sales while revenue
grows 24–37%.** Terrestrial cooling and power capacity is being added at roughly four cents
of capital per dollar of revenue. That is the signature of a **scaling** industry, not a
capital-constrained one, and it is corroborated on the ground: *"Since late 2021, Vertiv has
more than doubled its manufacturing capacity for switchgear, busbar and integrated power
solutions,"* plus a new Pune, India thermal management facility in 2024 producing in-row
units through to large free-cooling systems
([📄 VRT 10-K p.39](https://agentii.ai/v/VRT/sec110/39)).

### 2.4 Bound δ — order-book depth, which is the *only* genuine scarcity signal

> *"Vertiv's estimated combined order backlog was **$15.0 billion** and $7.2 billion as of
> December 31, 2025 and 2024, respectively, as continued strong demand has contributed to an
> increase in customer orders being placed in advance of our ability to fulfill them."*
> — [📄 VRT 10-K p.9](https://agentii.ai/v/VRT/sec110/9)

Against FY2025 revenue of $10,229.9M that is **≈1.47× coverage**, with the majority
"considered firm" and expected to ship "within the next 12 to 18 months," subject to
cancellation or rescheduling. This is real: demand is running ahead of shipment capacity.

**But note what it does and does not establish.** A deep backlog is evidence of a **tight**
market; it is not evidence of a **repricing** market. The filing says orders are placed
"in advance of our ability to fulfill them" — a quantity statement. It does not say the
backlog is being repriced upward. Bound δ therefore supports *demand outrunning supply*,
and **not** the pricing-power inference 001 drew from the margin. Section 3 shows the
margin data does not support it either.

**Book-to-bill is not disclosed.** `book-to-bill` returns **zero hits** in the FY2025 10-K;
VRT discloses backlog *levels*, never a ratio, and the Q2 2026 8-K (`sec135`) carries no
backlog number at all. A book-to-bill can be *derived* (backlog Δ $7.8B against FY2025
revenue $10,229.9M implies ≈1.76×, though the Δ is contaminated by acquisitions) — but a
derived ratio is MODELED and is not substituted into any filed series here.

### 2.5 What the four bounds jointly establish

Terrestrial cooling equipment is (α) a **minority share** of facility capex per MW,
strictly under ~12–14%; (β) supplied at a **~38% gross / ~19% operating margin**; (γ) added
at **4–5% of sales of capital intensity** while growing 24–37%; and (δ) backed by an
**~18-month firm order book** built by a supplier base VRT itself describes as crowded —
niche players Delta Electronics, Stulz, Johnson Controls and Socomec alongside large-scale
global competitors Schneider Electric, Eaton, Legrand and Huawei, competing *"primarily on
the basis of reliability, quality, price, service and customer relationships"*
([📄 VRT 10-K p.10](https://agentii.ai/v/VRT/sec110/10)).

**The industrial reading is unambiguous: cheap to scale, crowded, growing fast, and
competing on price.** An expensive competitive scaling supply chain is a *harder*
competitor than a bottleneck, because the orbital alternative must beat a supply base that
is getting cheaper and larger every quarter — not one that is stuck.

---

## 3. Job 2 — Is the margin expansion durable?

**Verdict up front: the margin LEVEL is real and not a one-quarter artefact. The margin
EXPANSION is not demonstrably a pricing regime, and the filing's own attributed driver
explains about 2% of the effect. 001's scarcity-pricing inference is not supported by the
primary source.**

### 3.1 The level is real

Two consecutive quarters, both at the same gross margin. Operating profit and net sales are
taken from the face of each income statement — Q2 2026 at
[📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec136/5) and Q1 2026 at
[📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec134/5) (different filings, so different
citation IDs at the same page) — with the percentages as compared in MD&A
([📄 VRT 10-Q p.28](https://agentii.ai/v/VRT/sec136/28);
[📄 VRT 10-Q p.26](https://agentii.ai/v/VRT/sec134/26)):

| | Q1 2025 | Q1 2026 | Δ | Q2 2025 | Q2 2026 | Δ |
|---|---|---|---|---|---|---|
| Gross margin | 33.72% | **37.73%** | +401 bps | 33.99% | **37.71%** | +372 bps |
| GAAP operating margin | 14.28% | **16.61%** | +233 bps | 16.77% | **19.48%** | +271 bps |

(Margins computed from the disclosed dollars; the filing's own rounded comparison reads
37.7% vs 33.7% and 37.7% vs 34.0%.)

H1 2026 GAAP operating margin 18.20% vs 15.68% (+252 bps). **Gross margin sits at 37.7% in
both quarters** — that flatness is what makes the level credible rather than a timing spike.
Adjusted figures are higher and are reported as CLAIMED: Q1 adjusted operating margin 20.8%
(+430 bps, [📄 VRT earnings_call_transcript p.2](https://agentii.ai/v/VRT/ect26/2)); Q2
22.6% (+410 bps, [📄 VRT earnings_call_transcript p.1](https://agentii.ai/v/VRT/ect27/1)).

### 3.2 The mechanism INVERTED relative to FY2025 — this is the durability problem

001 read the margin expansion as pricing power. The prior fiscal year's pattern says
otherwise. In FY2025 VRT grew revenue **+27.7%** and its gross margin **FELL 30 bps**
(36.62% → 36.32%), while the operating margin **ROSE 82 bps** (17.07% → 17.89%)
([📄 VRT 10-K p.41](https://agentii.ai/v/VRT/sec110/41)). The entire operating expansion
came from **opex leverage**: SG&A fell from 17.15% to 15.81% of sales, **134 bps**, against
flat gross margin. The filing's own words: *"Margin was relatively flat as benefits from
higher sales volume and **improved price realization** were offset by cost inflation,
particularly related to tariffs."*

**FY2025 had improved price realization AND a falling gross margin.** That single sentence
is decisive against the scarcity-pricing reading: price was already favorable, and it did
not move gross margin.

In H1 2026 the mechanism flipped. Gross margin **rose 372 bps** while SG&A as a share of
sales **rose slightly** (15.0% → 15.1% in Q2; 17.0% → 17.2% in Q1;
[📄 VRT 10-Q p.29](https://agentii.ai/v/VRT/sec136/29);
[📄 VRT 10-Q p.26](https://agentii.ai/v/VRT/sec134/26)). The opex-leverage engine that
drove FY2025's expansion is **not** contributing. The entire operating gain now comes from
gross margin **rate** — and gross margin rate is the line the filing attributes to "mix."

### 3.3 The decomposition — the filing's attributed driver cannot be the driver

The 10-Q attributes the expansion to *"the mix of product and service sales"*
([📄 VRT 10-Q p.28](https://agentii.ai/v/VRT/sec136/28)) and repeats it at segment level
([📄 VRT 10-Q p.29](https://agentii.ai/v/VRT/sec136/29)). Note 4 discloses that mix
([📄 VRT 10-Q p.13](https://agentii.ai/v/VRT/sec136/13)):

- Services & spares weight, Q2 2025: 519.2 / 2,638.1 = **19.68%**
- Services & spares weight, Q2 2026: 667.9 / 3,274.3 = **20.40%**
- **Shift: +0.72 percentage points** toward the higher-margin line.

A two-line mix effect is `Δw × (m_services − m_products)`. For a **+0.72 pt** weight shift to
produce **+372 bps** of blended gross margin, the gross margin differential between services
and products would have to be **≈520 percentage points** — services earning roughly six
times products. That is arithmetically impossible for two positive-margin lines blending to
37.7%. Run the other way: even a generous **10-point** margin differential yields
`0.0072 × 10 = 7 bps` — **about 2% of the observed 372 bps**.

**So the filing's stated cause explains ≈2% of the effect.** The remaining ≈365 bps is
*rate* — price, cost, or within-line volume leverage — which the filing does not name.
Section 5 records why it cannot be recovered: **VRT discloses no gross margin by product
line and none by segment.**

### 3.4 The two-basis problem sits on exactly the line being blamed

The income statement reports Q2 2026 products 2,646.7 / services 627.6
([📄 VRT 10-Q p.5](https://agentii.ai/v/VRT/sec136/5)). Note 4 reports products 2,606.4 /
services & spares 667.9 ([📄 VRT 10-Q p.13](https://agentii.ai/v/VRT/sec136/13)). Both sum
to 3,274.3 — the difference is a **$40.3M reclassification between products and services**,
0.7 points of revenue, on **precisely the two lines whose mix the filing credits for the
margin expansion**. Per §1c's standing rule both bases are reported here and neither is
collapsed; the consequence is that the attributed driver is not merely undecomposable but
**measured two ways**.

### 3.5 Duration risks — three, and the company names them

1. **Management's own guidance decelerates.** Q3 2026 adjusted operating margin is guided
   to **24.5%, +220 bps** — against Q2's **+410 bps**
   ([📄 VRT earnings_call_transcript p.2](https://agentii.ai/v/VRT/ect27/2)). The expansion
   is guided to roughly **halve** next quarter. FY2026 adjusted operating margin of 23.8%
   (+340 bps) then requires a Q4 step-up, i.e. the company is back-loading the year.
2. **EMEA's margin gain is partly a comp.** EMEA margin rose 25.7% vs 21.9% (+380 bps) on
   net sales up just **+1.7%** — and **−2% organic**. The CFO concedes it directly: *"the
   gain that you saw in margin, was a favorable comp too … the Ireland portion did come
   through Q2 last year, which was in EMEA"*
   ([📄 VRT earnings_call_transcript p.6](https://agentii.ai/v/VRT/ect27/6);
   [📄 VRT 10-Q p.30](https://agentii.ai/v/VRT/sec136/30)). One of three segments' margin
   gains is a comp artefact on a shrinking organic base.
3. **Acquisition accounting widens the GAAP/adjusted gap.** GAAP expansion is +271 bps;
   adjusted is +410 bps — a **139 bps gap** driven by amortization of intangibles
   (+57.1% to $73.7M) and other operating expense (+285.3% to $28.9M, including a **$28.8M
   loss on PurgeRite contingent consideration**,
   [📄 VRT 10-Q p.30](https://agentii.ai/v/VRT/sec136/30)). Acquisitions contributed **+5
   pts of the 24% growth** ([📄 VRT earnings_call_transcript p.2](https://agentii.ai/v/VRT/ect27/2))
   and $129.7M of revenue. Part of the growth is bought, and it arrives GAAP-margin-dilutive.

Tariffs are a fourth, unquantified drag the company acknowledges in both documents.

### 3.6 Verdict on durability

- **Level: DEMONSTRATED** — two quarters, flat 37.7% gross margin, cited above.
- **Driver: NOT ESTABLISHED.** The filing says "mix"; the mix arithmetic says ≈2%. The call
  says "price cost execution" ([📄 VRT earnings_call_transcript p.2](https://agentii.ai/v/VRT/ect27/2))
  while the filed document says "mix" — **two different causal stories for the same number,
  both dated 2026-07-29.** Under the same admissibility logic applied at Q-1, the filed
  document governs, and the filed document's stated cause does not survive arithmetic.
- **Durability: NOT ESTABLISHED.** Guided expansion halves in Q3; EMEA's gain is comp-driven;
  FY2025 is a same-company precedent of positive pricing coexisting with a *falling* gross
  margin; the opex-leverage engine that drove FY2025 is currently contributing nothing.

**The load-bearing correction for the orbital case.** 001 wrote that *"an expanding margin
alongside rapid growth indicates a supplier market where demand is outrunning capacity —
pricing power, not a commodity race to the bottom."* The demand-outrunning-capacity half is
supported (Bound δ, $15.0B firm backlog). The **pricing-power half is not**. And the
correction runs in an awkward direction: with scarcity rents removed, terrestrial cooling
looks *more* like the "competitive, mass-produced, 24%-growing solution" 001 described, not
less — because its economics now rest on volume, mix and cheap capacity addition rather
than on price. **001's adversarial conclusion survives; its stated mechanism does not.**
That matters for F2 because a comparator whose advantage is a scaling cost curve is harder
to displace than one whose advantage is a scarcity rent that a new entrant could undercut.

---

## 4. Job 3 — The earnings call, and what only lives there

Phase 1's lesson held: a physical parameter reached the transcript that never reached the
10-Q. Three findings are transcript-only.

1. **The per-MW content figure** ($3.25–3.75M/MW, §2.1). The word `megawatt` returns
   **zero hits** in the Q2 2026 10-Q. The single most useful physical parameter in this
   artifact exists on the platform only because someone asked a question on a call.
2. **The 800V DC schedule and its density coupling.** 800V DC under customer validation in
   2026 with deployment 2027; data-hall-level validation 2027 / deployment 2028; adoption
   described as *"gradual"* with 400V DC also in play
   ([📄 VRT earnings_call_transcript p.1](https://agentii.ai/v/VRT/ect27/1);
   [📄 VRT earnings_call_transcript p.6](https://agentii.ai/v/VRT/ect27/6)). Management ties
   content growth to density explicitly — *"with that density, with that complexity, our
   content is impacted favorably"* — and to liquid cooling spreading beyond the chip:
   *"not just liquid cooling for the chip, but for a much bigger array of electronics across
   the entire IT stack"* ([📄 VRT earnings_call_transcript p.4](https://agentii.ai/v/VRT/ect27/4)).
   **This is the terrestrial cooling roadmap the orbital case must beat**, and it points to
   rising, not falling, terrestrial content per MW.
3. **The EMEA comp concession** (§3.5), which is a durability admission that appears
   nowhere in the 10-Q.

**Negative result, located:** `PUE` returns **zero hits** in the Q2 2026 10-Q — independently
re-confirming Phase 1's check. A sourced PUE does not exist in VRT's filings, so
`pue_proper_residual` remains `UNRESOLVABLE-FROM-PUBLIC-SOURCES`, as the sibling SPCX
artifact also found.

---

## 5. What VRT cannot bound — Basis A and Basis B remain out of reach

Per §1c, every competing basis is reported and none collapsed.

| P5's ratio needs (DA-05) | Can VRT supply it? | Why |
|---|---|---|
| **Basis A** — hyperscaler marginal cost/kW | **No** | Not disclosed by any hyperscaler, and VRT is a supplier to them, not one of them |
| **Basis B** — colocation market price/kW | **No, structurally** | VRT *sells equipment to* colocation operators. Its revenue per unit is a **supplier price**, not a market rental price. No transaction in VRT's financials is a rental |
| **Basis C** — new-build fully-loaded cost/kW | **Partly, one-sided** | Bound α puts VRT's whole power+thermal+services content at 12–14% of facility capex per MW, so **cooling equipment ⊂ that** is bounded *above*. Land, shell, power interconnect and IT load remain outside VRT's disclosure entirely |

**Explicitly: Basis A and Basis B remain out of reach, and VRT's data cannot close them.**
No amount of further work on VRT changes this — the blocker is the entity's position in the
value chain, not the depth of its disclosure. This is a structural
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` disposition, and it is a *stronger* case than PIL-6's
FCC/ITU gap: colocation pricing is not merely unreachable, it is commercially licensed data.

Three further gaps, all verified:

- **No cooling-only revenue.** Segments are geographic
  ([📄 VRT 10-K p.8](https://agentii.ai/v/VRT/sec110/8)); the only offering split is
  products vs services & spares, which cuts across thermal and power. So the cooling share
  of VRT's *own* revenue is undisclosed.
- **No gross margin by line or segment** — the phrase "gross margin" appears only on pages
  28 and 31 of the 10-Q, both consolidated
  ([📄 VRT 10-Q p.28](https://agentii.ai/v/VRT/sec136/28), via `search_keyword_in_source`).
  This is why §3.3's driver is unrecoverable.
- **No book-to-bill.** Backlog levels only; zero hits for `book-to-bill` in the 10-K.

---

## 6. Acceptance test verdict

The task's test: *if the sourced band exceeds ±50%, F2 downgrades to a qualitative bound
and 003 and 009 must be notified.*

**On the figure this artifact actually sources, the test does not fire.** The bound on VRT
content per MW is $3.25M–$3.75M — a half-width of **±7.1%** about the $3.5M midpoint. That
is well inside ±50%. The Bound α comparison inherits the same ±7.1%.

**But the test is the wrong shape for this blocker, and saying only "it passes" would be
misleading.** P5 needs a *cooling-only $/kW on Basis A or B*. VRT's contribution is a
*whole-chain content share on neither basis*. That quantity is not **wide** — it is
**non-formable**. A band that cannot be drawn is not a band within ±50%; it is a different
failure, and the practical consequence for the downstream thesis is the same. **Recording
it as a pass on a technicality would be exactly the kind of false clearance 002 exists to
prevent.**

**Notification status:**

- **003** — no notification on the ±50% rule. Notify instead on the finding that the
  terrestrial cooling driver is **unrecoverable from the filing** (§3.3, §5): any 003 model
  that carries a terrestrial-cooling cost escalator or deflator should record its driver as
  **MODELED**, not sourced.
- **009** — **the comparator is NOT strong enough to trade against, and 009 must be told
  so.** 009 would trade VRT as the terrestrial comparator to the orbital case. What VRT
  supplies is (i) a *supplier's* margin structure, (ii) an upper bound on equipment share,
  and (iii) a capacity-growth rate. What it cannot supply is any of the three bases P5's
  ratio needs. A trade requires a **level**; VRT provides only a **bound** and a
  **direction**. 009 may use VRT to argue *direction* — terrestrial cooling is cheap to
  scale, crowded, and getting more content per MW — but it cannot price the orbital penalty
  off VRT, and should not represent that it can.

**On F2's own falsifier** (`f2_radiator_mass_per_MW_uncertainty_band_pct threshold=0.50`):
this artifact does not set F2's radiator constant and cannot bound it — that is physics, and
belongs to whichever Phase 2 artifact does the radiator derivation. What this artifact
establishes is the *counterfactual* against which that band will be judged. **No F2
downgrade is triggered by anything in this artifact.**

---

## 7. Data-integrity register

| Register | Application to VRT | Disposition |
|---|---|---|
| **DA-23** sign stripping | Component identity closes at 637.9 in both admissible forms (§1.1, §1.2). Platform field `OperatingIncomeLoss` returns **+637,900,000** (Q2 2026), +1,078,000,000 (H1 2026), +440,100,000 (Q1 2026) — matching the filed positives. `EPS × shares` NOT used | **Not stripped. CLEAN.** 001's verdict upheld on admissible evidence |
| **DA-04** terrestrial basis | Reported as supplier margin/capex/order structure, never as $/kW. Scope limit re-confirmed: `megawatt` and `PUE` both zero hits in `sec136` | Applied; both bases stated, not collapsed |
| **DA-05** competing bases | A, B and C all reported; A and B OUT OF REACH, C partly bounded. No collapse | Applied (§5) |
| **DA-25** normalised per-unit | One per-unit figure produced ($3.25–3.75M/MW) and reported as a bounded observation with its basis mismatch stated; not substituted into any filed series | Applied |
| **DA-24** asset-sale contamination | No asset-sale gain identified in Q2 2026 operating income. Acquisitions contribute revenue (+5 pts) and GAAP-margin dilution, not a one-time gain | Not present |
| **DA-26 / DA-27** period labelling | Q2 2026 10-Q, three and six months, both presented; no annual-as-quarterly mislabel found | Not present |
| **DA-28** IPO discontinuity | Not applicable — VRT is not a recent IPO and per-share items are not used in any growth claim here | Not applicable |

**New register gap for PIL-3 — no DA covers two-basis revenue disaggregation.** The income
statement and Note 4 report the same product/service split $40.3M apart (§3.4). This is a
*within-filing* basis inconsistency, distinct from DA-05 (competing definitions of a metric
across sources) and from DA-26/27 (period labelling). It is not registered. Recorded here
for the register, not silently normalised.

---

## 8. What could NOT be verified

1. **Cooling-only $/kW on any basis.** Non-formable. Basis A and B structurally out of
   reach (§5). This is the artifact's principal `UNRESOLVABLE-FROM-PUBLIC-SOURCES`
   disposition.
2. **The $3.25–3.75M/MW figure's primary source.** It originates from VRT's Investor Day
   deck — non-filed, not on the platform. It reaches this artifact via an analyst's
   restatement, undisputed by management, on `ect27` p.4. **CLAIMED, not DEMONSTRATED.**
3. **The margin-expansion driver.** The filing attributes it to mix; the mix arithmetic
   refutes that (≈2%); the call attributes it to price/cost; line-level gross margins that
   would settle it are not disclosed (§3.3, §5). **Unresolved, and unresolvable from VRT's
   filings.**
4. **Book-to-bill.** Not disclosed. The ≈1.76× derivation is MODELED and contaminated by
   acquisitions; not used.
5. **Which product/service split is authoritative** (income statement vs Note 4, $40.3M
   apart). Both reported; no basis to prefer one.
6. **Tariff magnitude.** Acknowledged in both the 10-Q and the call as a drag, quantified in
   neither. So the "+410 bps adjusted" cannot be decomposed into price, productivity and
   tariff components.
7. **FY2026's implied Q4 step-up.** FY guidance of 23.8% adjusted operating margin against a
   Q3 guide of 24.5% requires a Q4 acceleration that management does not itemise. Not
   verifiable from the disclosure.
8. **`validate_calculation` on `OperatingIncomeLoss`.** Unavailable — no result returned
   despite the arc set existing. Verified by component identity and calculation tree
   instead (§1). Flagged to PIL-3 as a detector-coverage gap.

**Instrument caveat, recorded per the standing rule:** the 9 `fail` rows on this accession
were **not** read as failures. Their `computed` vs `reported` pairs are internally
impossible and include a pure sign inversion on the computed side (§1.2). They are
arc-selection artefacts, consistent with the sibling SPCX artifact's finding, and they
corroborate rather than contradict the 93%-false-positive rate.

---

## 9. Carry-forwards

1. **PIL-2:** the terrestrial counterfactual is bounded in **share** (cooling equipment
   ⊂ 12–14% of facility capex per MW) and in **trajectory** (4–5% of sales capex, 24–37%
   revenue growth, ~18-month firm backlog), but **not in level**. F2's penalty is therefore
   assessable as a *direction* question, not yet as a *magnitude* question.
2. **PIL-3:** two register entries — the `OperatingIncomeLoss` arc-coverage gap (§1.2) and
   the unregistered two-basis revenue disaggregation (§7).
3. **PIL-5:** 001 recorded VRT DA-23-clean via an inadmissible test. The verdict is upheld
   here on admissible evidence, so VRT's `DEMONSTRATED` grade stands; but the **method**
   001 used should not be counted toward PIL-5's ≥50% conversion, and this artifact
   supersedes it.
4. **§1c:** `no_single_basis_collapse` observed — three P5 bases reported, basis A/B failures
   stated explicitly rather than elided.
5. **003 and 009:** notified per §6 — 003 on the unrecoverable driver; 009 that the
   comparator supports a direction but **not a trade**.
