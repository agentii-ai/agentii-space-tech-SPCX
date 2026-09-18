# Research Thesis: 006 — Tier 2 — Satellite Connectivity, Spectrum & Services

**Constitution Ref**: constitution.md v1.4.0 (`constitution_pin: 1.4.0`)
**Created**: 2026-09-18
**Status**: Active
**板块**: Tier 2 · Wave 1 · **Binding constraint**: `REGULATORY_SPECTRUM`
**Time Horizon**: 2026-Q4, terminating at the wave-1 hand-off to 007, 009 and 011
**Depends on**: `001-technology-baseline` (pin 1.2.0) · `002-evidence-validation` (the validated input set) · `004-tier0-spacex-anchor` (the operating-leverage benchmark)
**Produces**: the **segment thesis for Tier 2** — a licence-versus-business value attribution per name, a direct-to-cell (D2D) placement map, and a dated regulatory gate chain per deal security. Sizes no position above P11's 2% binary cap.

---

## 0. Inherited baseline — what this thesis does NOT re-derive

001 established the following through PIL-6 and this thesis **takes them as given**.
Re-deriving any of them is out of scope; the artifact cites 001's file rather than
repeating its work. Paths are relative to the workspace root.

| Inherited result | 001 artifact | Grade |
|---|---|---|
| **IRDM is profitable on licensed L-band** — the buy-side test PIL-6 needed. Q2 2026 revenue **$225.237M (+3.8%)**, operating income **$34.008M (−32.3%)**, operating margin **15.1% vs 23.2% (−8.1 pts)**, net income **$9.679M (−55.9%)**, R&D **$5.53M (+29.2%)** | `theses/001-technology-baseline/artifacts/IRDM/2026-09-18_1239_competitive_methodology.md` | `DEMONSTRATED` |
| **The direction of that margin is itself the finding** — *"the licence is durable, the service business on top of it is not automatically so"* — and 001 left the cause open, nominating it for Phase 6: *"test whether that decay is competitive (Starlink/D2D pressure) or cyclical"* | same | `DEMONSTRATED` |
| **"The spectrum, not the constellation, is the scarce input."** Satellites can be rebuilt; L-band licences cannot be created | same | `DEMONSTRATED` |
| **SATS realised ~$27B of gains across 2025 H2 from selling spectrum licences**, against **$15.0B of full-year 2025 revenue** — the regulatory asset was worth **~1.8×** the entire operating business that held it, while generating no revenue of its own | `theses/001-technology-baseline/_cross/phase-4-regulatory-allocation.md` | `MODELED` — the direction is certain; the $27B quantum is inferred from a GAAP operating line the filing does not break out at that granularity |
| **The SPCX–EchoStar mark prices spectrum: ~$19.6B** for AWS-4 / H-Block / AWS-3, **FCC-approved with the transfer closed**. It is a transaction value, **not** a $/MHz-pop (DA-17) | `_cross/phase-4-regulatory-allocation.md`; constitution F6 | `DEMONSTRATED` |
| **DA-24 registered — asset-sale contamination.** SATS 2025 Q3 operating income was **4.6× revenue** ($16.6B on $3.6B); margin progression **2.3% → 5.7% → 460.5% → 118.1% → 10.7%** | constitution §Data-Integrity Register; `artifacts/SATS/2026-09-18_1239_risk_methodology.md` | `DEMONSTRATED` |
| **DA-24 is independent of DA-23** — SATS is contaminated but **not** sign-stripped (EPS × shares reconciles to 0.3%). Exactly one defect, not both | `artifacts/SATS/2026-09-18_1239_risk_methodology.md` | `DEMONSTRATED` |
| **SATS's clean quarter** — revenue **$3,667.5M**, operating income **$392.8M**, operating margin **10.7%**, net income **$146.9M (4.0%)** | same | `DEMONSTRATED` |
| **The regulatory gates are SEQUENTIAL, not parallel** — FCC licence transfer (**passed**) → ITU international coordination (**named** in RKLB's Iridium risk factors) → DCSA / CFIUS-adjacent review (**also named**) → national market access (**not evidenced**). DA-18 upgraded from ambiguity to checklist | `artifacts/SATS/…_risk_methodology.md`; `_cross/phase-4-regulatory-allocation.md` | `DEMONSTRATED` for gate identity and naming; the *ordering* is `MODELED` |
| **PIL-6's disposition splits**: the *premise* is `DEMONSTRATED` from filings; only the *falsifier* is `UNRESOLVABLE-FROM-PLATFORM` (FCC IBFS / ITU Space Network List) | same; `_cross/technology-baseline_synthesis.md` line 6 | `DEMONSTRATED` |
| **GSAT is the purest monopsony in the universe** — revenue **$64.772M (−3.5%)**, operating margin **7.4%**, **93% of net income non-operating**, **7.4×** leverage, **12.0%** equity/assets, **$2,136.8M** accumulated deficit | `artifacts/GSAT/2026-09-18_2040_competitive_methodology.md` | `DEMONSTRATED` |
| **SPCX Connectivity is the tier's operating-leverage benchmark** — operating income **$1,656M** on **$4,291M** revenue (Q2 2026, **+79.4% YoY**), ARPU **$66 (−22.4%)** against subscribers **+101.2%** | constitution §Sector Preferences; `artifacts/SPCX/2026-09-18_2310_operational-kpi_methodology.md` | `DEMONSTRATED` |
| **DA-17 / DA-18 / DA-19 are registered ambiguity classes** — spectrum quantity (MHz vs MHz-pop vs licensed footprint); "regulatory approval" (ITU coordination vs national licence vs market access); orbital slot priority (ITU filing date vs bring-into-use milestone vs operation — **priority can lapse for non-use**, so a filing is not a durable asset) | `theses/001-technology-baseline/spec.md` §1c (DA-01 … DA-22) | `DEMONSTRATED` as *registrations*; **none is resolved** |
| **P11 binds IRDM and GSAT** — do not underwrite standalone fundamentals; the price tracks a spread; binding constraint `REGULATORY_SPECTRUM`; size at the 2% binary cap; **on a break, re-underwrite from scratch** | constitution §In-Flight M&A Treatment | `DEMONSTRATED` as policy |

**What 001 did not do — and why this thesis exists.** 001 covered Tier 2 through PIL-6
and closed the *premise* two-sidedly: the sell side (EchoStar realised the price) and
the buy side (IRDM holds it profitably). It never asked the **investment** question.
Three things were left on the table, and they are this thesis's entire scope:

1. **What are these businesses worth?** The licence has an observed price and the
   operating businesses have filed margins, and nobody has put the two side by side.
2. **What does the D2D transition do to them?** Direct-to-cell could commoditise the
   service layer while *raising* the value of the licensed layer — a claim never tested.
3. **What do the two deal spreads price?** Two of the five names are P11 securities, so
   half the tier is not an operating business at all.

**006 is the segment thesis. It inherits the premise and owns the valuation, the
transition and the deal mechanics.** The Tier 2-specific contested figures it must
convert are enumerated below.

---

## 0b. Validation queue — the Tier 2 figures this thesis owns

**002 owns the cross-cutting denominators and physics inputs** (Electron's 300 kg,
Falcon 9's 22.8 t, F2's unsourced constants, the DA-23 universe census). **006 owns the
Tier 2-specific contested figures** and must not re-open 002's. Under P4, `MODELED` can
never satisfy a falsifier — so an unconverted figure here is a pillar that cannot fire.

| Contested figure | Grade now | Why it is contested | Owner | The source that resolves it |
|---|---|---|---|---|
| **the ~$27B SATS licence gain and the 1.8× ratio** | `MODELED` | inferred from a GAAP operating line; the filing does not break the gain out at that granularity | P2 | SATS 10-K / 10-Q spectrum-disposal disclosure, or the transaction documents behind the $19.6B mark |
| **the $19.6B mark used as a *unit* price** | `DEMONSTRATED` as a transaction value, **not** usable as $/MHz-pop | DA-17: the coverage denominator for each block is undisclosed, so the mark prices one specific combination and cannot be transferred to another licence without a denominator | P2 | FCC licence files and the coverage footprint per block — **platform-unreachable** |
| **IRDM's and GSAT's licence carrying value** | unverified | if the licence sits on the balance sheet as an indefinite-lived intangible, it is an independent valuation basis; if it is aggregated, it is not | P2 | 10-K intangible-asset notes and purchase accounting |
| **the two deal prices and their conditions** — IRDM $54/sh (RKLB), GSAT $90/sh (AMZN) | `CLAIMED` from announcement and constitution | the consideration, conditions, outside dates and break fees sit in the filed merger agreements | P4 | the 8-K / merger agreement exhibits and the proxy |
| **ASTS's D2D capacity, coverage and commercial-service claims** | `CLAIMED` (issuer) | no filed revenue line; `PARTIAL` coverage with `sec_filings` counter at 0 despite 18,536 XBRL facts and 142 source documents | P3, P5 | ASTS 10-K / 10-Q, and a first filed service-revenue disclosure |
| **VSAT's GEO/LEO mix and government-satcom backlog** | unverified | `PARTIAL`; the sector must be assigned manually before any sector-aggregate constraint evaluates (PROGRAM.md §7) | P2, P3 | VSAT 10-K segment tables |
| **"connectivity has demonstrated operating leverage" as a Tier 2 property** | `DEMONSTRATED` **only at the anchor** | the entire evidence base is one segment of one issuer (SPCX Connectivity); no Tier 2 name has been shown to exhibit it | P1, P6 | IRDM and GSAT segment-level margin series |
| **PIL-6's falsifier** (`new_entrant_primary_spectrum_or_slot_grant_without_incumbent_acquisition`) | `UNRESOLVABLE-FROM-PLATFORM` | the registers are public and outside the reachable corpus. 001 recommended splitting the disposition rather than dropping the pillar | P5 | **not re-attempted** — 006 builds a reachable proxy instead (§1b P5) |

---

## 1. Research Question

**Connectivity is the only space sub-sector with demonstrated operating leverage. Is
that leverage durable — or is it a temporary consequence of a licensed asset that
cannot be replicated and will be repriced?**

The question is uncomfortable, and the inherited numbers state it better than any
framing: **IRDM's operating margin fell from 23.2% to 15.1% year over year while
revenue grew 3.8%** — an 8.1-point compression on a licence that cannot be duplicated.
Meanwhile **EchoStar realised ~$27B from selling licences against $15.0B of annual
revenue from the business that held them**, and its clean quarter runs at a **10.7%**
operating margin. The asset appreciated; the businesses operating on top of it did not.

So the tier poses two opposed readings, and this thesis exists to decide between them:

- **Reading A — the licence is the asset and the business is a thin margin on it.**
  Then the correct valuation is an SOTP that splits a durable, priced licence from a
  competitive service business, and the market's single blended multiple for these names
  is wrong. D2D *raises* the licence's value even as it compresses service pricing.
- **Reading B — the licence is the asset and the business is now being priced by D2D.**
  Then the licence is not a moat but a **toll that is being routed around**: ASTS and
  Starlink direct-to-cell attack the service layer from orbit, and the incumbent licence
  is what the attacker *rents or buys* (Apple holds ~20% of GSAT and rights to **85%** of
  its network capacity; AMZN pays **$90/sh** for the rest of it).

Both readings agree the licence is real — 001 settled that. They disagree about **who
captures the rent**, which is the only question a valuation can answer.

### Why this thesis exists at all

The alternative was to leave Tier 2 covered by PIL-6's premise and move on. Three
concrete costs follow from that:

1. **Half the tier would be underwritten as a business.** IRDM and GSAT are P11 deal
   securities. Under P11 their price tracks a spread, their binding constraint is
   `REGULATORY_SPECTRUM`, and on a break the standalone case is **not** the
   pre-announcement case. A thesis that values them on fundamentals is valuing something
   that is contractually ceasing to exist.
2. **The tier's best-evidenced fact would go unexploited.** The ~$19.6B mark is the only
   observed price of spectrum in the universe. Without an attribution that applies it,
   the mark is an anecdote rather than a valuation input.
3. **A live falsifier would stay un-evaluated.** PIL-6's falsifier needs FCC IBFS / ITU
   sources the platform does not carry. 001 split the disposition and recommended
   carrying the pillar rather than dropping it. 006 is where that split becomes a
   *method* — a reachable proxy test — instead of a note.

---

## 1b. Pillars

### Pillar 1 — The licence is durable and the business on top of it is not, and the IRDM margin decay is decomposable by line (Priority: P1) 🎯 Minimum Defensible View

The inherited fact is a **contradiction against the tier's own thesis**: the
constitution rates Satellite Connectivity **Overweight / High** because it is *"the only
space sub-sector with demonstrated operating leverage."* Yet the tier's only profitable
constellation operator lost **8.1 points of operating margin on +3.8% revenue growth**.
001 flagged the cause as open and nominated it for Phase 6.

The arithmetic is already informative before any new disclosure arrives:

```
Q2 2026 operating income     $34.008M      on revenue $225.237M  →  15.1%
Q2 2025 operating income     $50.258M      on revenue $216.906M  →  23.2%
decline                      $16.250M                            →  −8.1 pts
R&D step-up                   $1.251M ($5.530M − $4.279M)        →  ≈0.6 pts
```

**The disclosed R&D step-up explains roughly 0.6 of the 8.1 points — about 7% of the
decline.** The residual ~7.5 points sits on the revenue side: price, mix or volume. On
the component arithmetic alone the decay is **not** a reinvestment story.

**The claim:** the decline is attributable **by revenue line**, and **less than half of
it falls on the licensed-spectrum service line** — i.e. the licence's own revenue stream
holds while the competition-exposed overlay (equipment, wholesale, adjacent services)
absorbs the compression. If instead the decline is concentrated *in* the licensed-service
line, then the licence itself is being repriced, the "durable asset / weak business"
separation fails at IRDM, and P2's attribution premise must be rebuilt before it is used
anywhere else in the tier.

**Why this priority**: it is the Minimum Defensible View because it decides whether the
inherited Tier 2 premise is *actionable* or merely *true*. Everything else in this
thesis — the SOTP, the D2D placement, the peer comparison — rests on the licence and the
service business being separable in the financials. It is also the only Tier 2 figure
currently **moving against** the constitution's conviction ranking, which makes it the
highest-information number in the tier.

**What counts as resolution.** A line-level attribution must come from IRDM's own
reported revenue and cost disaggregation (service vs subscriber equipment vs other, and
the operating-expense lines beneath them) — **not** from a company narrative about
"investment in growth." Where the filing does not disaggregate finely enough to attribute
the decline, the pillar defaults to the coarser gross-profit − opex test and the
limitation is recorded, not glossed.

**Independently falsifiable**: a line-level decomposition in which half or more of the
margin decline lands on the licensed-spectrum service line.

**wrong_if**: `metric=share_of_irdm_operating_margin_decline_attributable_to_lines_other_than_licensed_spectrum_services threshold=0.5 source=IRDM_10-Q_revenue_and_cost_disaggregation op=<`

**Subscribed**: `IRDM × unit-economics`, `IRDM × operational-kpi`, `IRDM × recent-quarter`, `IRDM × ratio-analysis`, `IRDM × competitive`, `GSAT × unit-economics`

---

### Pillar 2 — The licensed asset and the operating business price separately, and the licence is the majority of the value (Priority: P2)

If the licence is an asset with an observed price and the business on top is a
single-digit-to-low-teens operating margin, the two must be valued apart. The reference
mark is **~$19.6B** for AWS-4 / H-Block / AWS-3 — **a transaction value, not a unit
price** (DA-17). Applied to SATS, it was **~1.8× the annual revenue** of the business
that held it. Applied to the rest of the tier, it has never been tried.

**The claim:** running a two-basis SOTP per name — **(A) transaction-mark transfer** and
**(B) capitalised licence-attributable cash flow** — the licensed asset accounts for
**more than half** of the tier's attributable enterprise value, and the operating
businesses account for the rest at margins in the observed 7.4–15.1% band. If the
licence is instead a minority of value, then the tier is a service business with a
permit attached, the mark is an outlier rather than a comparable, and P1's separation
matters far less than the tier's narrative implies.

**Both bases must be reported side by side** under the §1c standing rule. Basis A is the
only observed print and prices **one** combination of blocks for **one** footprint;
carrying it forward to a different licence requires a coverage denominator the
disclosures do not provide, and a bare $/MHz-pop ratio would be a DA-17 violation.
Basis B is derived and therefore `MODELED` until the cash-flow split is filed.

**Why this priority**: it is the valuation the inherited premise implies, and it is the
instrument the rest of the tier consumes — P3's placement rule and 007's competitive
read-through both need a per-name answer to "how much of this is the licence?". It is P2
rather than P1 because P1 decides whether the separation exists at all; P2 prices it.

**What counts as resolution.** A per-name attribution survives only if the licence's
revenue and cost can be identified from filed disaggregation or from a disclosed
transaction of *that* issuer's own assets. An attribution that depends on a management
assertion of licence value is `CLAIMED` and cannot satisfy a falsifier.

**Independently falsifiable**: an SOTP in which the operating businesses alone account
for half or more of attributable enterprise value.

**wrong_if**: `metric=share_of_tier2_attributable_enterprise_value_attributable_to_licensed_spectrum_per_sotp threshold=0.5 source=SPCX_EchoStar_transaction_mark_and_issuer_filed_operating_financials op=<`

**Subscribed**: `SATS × unit-economics`, `SATS × business-model`, `SATS × ratio-analysis`, `GSAT × unit-economics`, `GSAT × ratio-analysis`, `IRDM × unit-economics`, `VSAT × business-model`

---

### Pillar 3 — The D2D transition compresses the service layer while raising the value of the licensed layer, and every Tier 2 name is placeable on one side (Priority: P3)

Direct-to-cell is the first technology in the sector's history that can serve a handset
without an incumbent's distribution — and it needs exactly what the incumbents hold.
The two halves move in opposite directions:

| Layer | What D2D does to it | Evidence in hand |
|---|---|---|
| **Service** (voice/data/SOS delivered) | **Compresses price** — the number of routes to a handset rises while the handset population is fixed | GSAT revenue **−3.5% y/y**, the only negative-growth operator in the universe; SPCX consumer ARPU **$66, −22.4%** against subscribers **+101.2%** (borrowed from the anchor as a comparator, never as Tier 2 evidence) |
| **Licence** (globally harmonised L-band / MSS) | **Raises value** — a D2D entrant must rent, partner for, or buy it | Apple holds **~20%** of GSAT and rights to **85%** of its network capacity; AMZN bids **$90/sh** for GSAT; RKLB bids **$54/sh** for IRDM's L-band |

**The claim:** the placement is **total and mechanical**. A name sits on the **licence
side** if P2's attribution assigns the majority of its value to the licensed asset, and
on the **service side** if it does not — and the split cuts across the tier rather than
along it. ASTS is the adversarial case that makes the axis real: it is a **service-layer
attacker that owns a spectrum position**, which means it can be on both sides at once —
and if it cannot be placed, the axis is not discriminating and this pillar is a
framework, not a finding.

**Why this priority**: it is the mechanism that links the tier's valuation (P2) to its
competitive future, and it is what 009 consumes as a compute-adjacent demand signal. It
is P3 rather than P1/P2 because it *interprets* the attribution rather than producing it
— and because its central claim (which side appreciates) is a **direction, not a level**.
It is evaluated over the **same 2026-Q4 horizon** as every other pillar, against the next
disclosed quarter; no pillar in this thesis carries a different `as_of` or holding period.

**Independently falsifiable**: a Tier 2 name that cannot be placed on the licence/service
axis by P2's attribution rule.

**wrong_if**: `metric=count_of_tier2_names_not_placeable_on_the_licence_service_axis_by_the_P2_attribution_rule threshold=0 source=SOTP_attribution_per_P2 op=>`

**Subscribed**: `ASTS × competitive`, `ASTS × secular-trends`, `ASTS × operational-kpi`, `VSAT × competitive`, `VSAT × sector-overview`, `GSAT × competitive`, `GSAT × business-model`, `GSAT × operational-kpi`, `IRDM × secular-trends`

---

### Pillar 4 — The two deal spreads price the gate chain, not the businesses — and a break is re-underwritten from scratch (Priority: P4)

**IRDM ($54/sh, RKLB) and GSAT ($90/sh, AMZN) are P11 securities.** Under P11 the
binding constraint for both is `REGULATORY_SPECTRUM` — antitrust, CFIUS and
national-security review — and neither clears trivially: **IRDM carries safety-of-life
and defense communications; GSAT carries globally harmonised L-band and an Apple
capacity agreement.** This pillar's job is **not** to underwrite them on fundamentals,
which P11 forbids, nor to trade the spread, which the platform cannot price at Market
Data Stage `none`. It is to establish **what the spread is a price of**, from filings.

**The claim:** each deal security's next unpassed gate can be **dated from filings** —
the merger agreement's conditions and outside date, the risk factors naming the required
consents, and the disclosed financing. If it can, the P11 position is
catalyst-instrumented and the constitution's Catalyst Requirement (a dateable catalyst
within 180 days) is satisfiable. If it cannot, the position is **un-sizeable even at the
2% binary cap** and must be carried as `known-open`, not as a position.

**The break case is a distinct re-underwrite, not a discount to the deal.** On a break,
**the standalone case is not the pre-announcement case**: a failed deal leaves the target
*and* the acquirer re-rated, with the acquirer carrying deal costs. For IRDM that means
the pre-merger artifacts (`artifacts/IRDM/…_competitive_methodology.md`, tagged
`standalone_pre_merger`) are **inputs to the re-underwrite, not its answer**. The
scenario pair — close versus break — is run as a `what-if`, and the break leg re-derives
value from P2's basis B rather than from the announced price.

**Why this priority**: it is P4 because it is a *boundary condition* on the tier rather
than a finding about it — and because its output is a discipline (what may and may not be
sized) rather than a number. Note that under the Risk Framework the tier also caps at
**≤ 2 positions in any single sub-sector**, so the Tier 2 expression is at most two names
across five, two of which are in-flight deals.

**Independently falsifiable**: a deal security whose next regulatory gate cannot be dated
from any filed disclosure.

**wrong_if**: `metric=count_of_tier2_deal_securities_whose_next_regulatory_gate_lacks_a_recorded_expected_date_and_source threshold=0 source=merger_agreement_and_risk_factor_disclosures op=>`

**Subscribed**: `IRDM × risk`, `GSAT × risk`, `IRDM × recent-quarter`, `GSAT × recent-quarter`, `IRDM × what-if`, `GSAT × what-if`

---

### Pillar 5 — The gate chain is a dated checklist per name, and PIL-6's falsifier is bridged by a reachable proxy rather than re-attempted (Priority: P5)

F6 names orbital slots, spectrum rights and FCC/ITU coordination as **gating assets, not
paperwork**, and requires any thesis whose value depends on them to carry an explicit,
dated regulatory catalyst. 001 converted DA-18 from an ambiguity into a **checklist** by
naming the gates in sequence — **FCC → ITU → DCSA/CFIUS → national market access** — with
gate 1 **passed** for EchoStar and gate 4 **not evidenced** at all.

**The claim:** the checklist is completed **per name and per gate**, each gate carrying
an expected date and a source, and each gate classified as **filing-evidenced**
(reachable) or **registry-blocked** (FCC IBFS / ITU Space Network List —
`UNRESOLVABLE-FROM-PLATFORM`, inherited and not re-attempted). A gate with no dateable
expectation is recorded as a finding about disclosure quality, not quietly omitted.

**The falsifier is bridged, not retired.** PIL-6's falsifier —
`new_entrant_primary_spectrum_or_slot_grant_without_incumbent_acquisition` — needs
registries the platform does not carry, and 001's split disposition (premise
`DEMONSTRATED`, falsifier unreachable) is inherited as settled. What 006 adds is a
**reachable proxy**: whether a D2D entrant reaches commercial service on **primary**
grants it applied for rather than on an acquired incumbent licence, documented in its
own SEC filings. ASTS is the live candidate and is the reason this proxy is Tier 2
-specific. **The proxy triggers external verification; it does not fire the falsifier** —
issuer statements are `CLAIMED` under P4 and a `CLAIMED` figure can never satisfy a
falsifier. The proxy's job is to tell 011 when the FCC/ITU query is worth paying for.

**Why this priority**: last of the substantive pillars because it is a discipline over the
others — it dates the catalysts P4 sizes against and it is the only part of the
inherited Tier 2 premise that 001 could not evaluate at all.

**Independently falsifiable**: a Tier 2 spectrum asset whose granting gate chain is
named in no filed disclosure.

**wrong_if**: `metric=count_of_tier2_spectrum_assets_with_the_granting_gate_chain_named_in_a_filed_disclosure threshold=0 source=10-K_10-Q_risk_factors_and_8-K_transaction_filings op=<`

**Subscribed**: `SATS × risk`, `ASTS × risk`, `VSAT × risk`, `ASTS × recent-quarter`, `VSAT × recent-quarter`, `ASTS × growth-strategy`, `GSAT × growth-strategy`, `SATS × sector-overview`

---

### Pillar 6 — Every Tier 2 contested figure converts to `DEMONSTRATED` or is recorded as unresolvable (Priority: P6)

The meta-pillar and the scorecard for §0b. The queue is not decoration: under P4,
`MODELED` can never satisfy a falsifier, so **an unvalidated Tier 2 figure is a pillar
that cannot fire** — and the tier's headline ratio (**1.8×**) is precisely such a figure
today.

**The claim:** every row of §0b ends the thesis either **converted to `DEMONSTRATED`**
with the source that moved it, or **classified** into one of the two v1.3.0 disposition
classes with the specific resolving disclosure named. At least half the queue converts.
The residue is not a failure — it is a finding about disclosure or platform reach, and it
is reported as one.

**Why this priority**: it cannot be pursued directly, only accumulated — and its output
is what stops 011 from sizing against a number that was never real.

**Independently falsifiable**: any Tier 2 contested figure left unclassified or without a
named resolving source.

**wrong_if**: `metric=count_of_tier2_contested_figures_unclassified_or_without_a_named_resolving_source threshold=0 source=validation_queue_scorecard op=>`

**Subscribed**: `IRDM × peer-bench`, `GSAT × peer-bench`, `SATS × peer-bench`, `ASTS × peer-bench`, `VSAT × peer-bench`, `SATS × recent-quarter`

---

> **Delivering P1 alone yields a defensible partial conclusion** — the tier's one
> profitable constellation operator either holds its licence revenue while the service
> overlay absorbs the compression, or it does not. That single decomposition decides
> whether the rest of this thesis's instrument is usable, and it is delivered first.

## 1c. Method — the attribution and gate instruments

Two capabilities are specific to this thesis and are not used elsewhere in the program.

1. **The split of the regulatory asset from the operating business.** Every Tier 2 name
   is decomposed into (a) the licensed position and (b) the operating business, valued on
   **two bases each** — transaction-mark transfer and capitalised licence-attributable
   cash flow for the licence; filed operating margin at the `satellite_connectivity`
   WACC band (**8.5–11.5%**, `assumptions.yaml`) for the business. This is the instrument
   P1 delivers, P2 prices and P3 places on an axis. It is also the reason the tier cannot
   be read with a single blended multiple.
2. **The sequential-gate discipline.** DA-18 was upgraded from ambiguity to checklist by
   001; this thesis makes the checklist **dated and sourced per name** and instruments
   the Catalyst Requirement directly. The instrument's value is negative evidence as much
   as positive: a gate that cannot be dated is a disclosure-quality finding, and the
   inherited `UNRESOLVABLE-FROM-PLATFORM` boundary is respected rather than re-attempted.

**Evidence discipline.** Per P4 and the v1.3.0 register, any artifact reading
`operating_income` shows the component derivation in-line — which is mandatory here for a
specific reason: **SATS is DA-24-contaminated** (a licence sale flowed through the
operating line) and **DA-24 is independent of DA-23** (SATS is contaminated but *not*
sign-stripped). Exactly one defect applies. Reading SATS's 2025 quarters as operating
performance is a `DATA_STALE` error, and the clean read is the latest-quarter margin.

**Definitional discipline (inherited by reference).** DA-17 (spectrum quantity), DA-18
("regulatory approval"), DA-19 (orbital slot priority) and DA-21 (segment definitions)
are live in every artifact here. **DA-21 matters most at the deal names**: Apple's "85% of
network capacity" and IRDM's "2.5M subscribers" are not commensurable quantities, and
aggregating them across issuers is the error the no-single-basis-collapse rule exists to
prevent. Per the §1c standing rule, artifacts report all competing bases and label which
one is quoted.

**Corpus discipline — a documented dead end.** PROGRAM.md §4 records that the knowledge
registry has **no industrial or aerospace domain** (`list_domains` returns 9 domains
whose `applicable_sectors` are `["med","tech","fin"]` only), so **any sector-keyed
strategy or case retrieval returns zero rows by construction**. 006 must **not** attempt
it. Where an analogue is wanted — an asset sale of a licence, an in-flight merger spread,
a monopoly asset with a commoditising service layer — it is retrieved by **structural
situation shape** and labelled borrowed, never presented as sector evidence.

**Correction policy.** Where this thesis invalidates a 001 figure, 001's artifact is
**not** rewritten. 001's files are frozen; the correction is recorded here and cited by
location.

## 2. Universe Definition

Five researchable names. The tier is small by construction, and **half of it is not an
operating business** — two of the five are P11 deal securities. Weights are analytical
effort, not positions; this thesis sizes nothing above the 2% binary cap.

| Ticker | Company | Sector | Weight | Coverage / Deal | Why it is in this thesis |
|---|---|:---:|---|---|---|
| IRDM | Iridium Communications | tech.telecom_services | 26% | READY — 77 filings, cohort `tier2_2026q3` | **P1's subject and the universe's only profitable constellation operator.** 66 satellites, licensed L-band, ~2.5M subscribers, $871.7M revenue and $114.4M net income (2025). **DEAL — acquired by RKLB at $54/sh (P11)** |
| GSAT | Globalstar | tech.tech_hardware | 22% | READY — 65 filings, cohort `tier2_2026q3` | **The monopsony case**: 7.4% operating margin, 93% of net income non-operating, the only negative-growth operator. Apple holds ~20% equity and rights to 85% of capacity. **DEAL — acquired by AMZN at $90/sh (P11)** |
| SATS | EchoStar | tech.telecom_services | 26% | READY — 62 filings, cohort `tier2_2026q3` | **The sell-side case and the tier's only observed spectrum price**: ~$19.6B AWS-4/H-Block/AWS-3 sale to SPCX, FCC-approved with transfer closed; ~$27B of 2025 H2 licence gains. DA-24-contaminated on the operating line |
| ASTS | AST SpaceMobile | **`PARTIAL` — sector unassigned** | 16% | `PARTIAL` — `sector` null, `sec_filings` counter 0, but 18,536 XBRL facts and 142 source documents | **The D2D attacker and P5's proxy test** — a new entrant pursuing primary grants rather than buying a licensee. Sector must be assigned by hand before any aggregate constraint evaluates |
| VSAT | Viasat | **`PARTIAL` — sector unassigned** | 10% | `PARTIAL` — `sector` null, `sec_filings` counter 0, but 21,898 XBRL facts and 98 source documents | **The pure service-layer comparator**: GEO/LEO broadband and government satcom with no licensed MSS position at stake. The control that makes P3's axis falsifiable |

> **Sector-assignment precondition (not an assumption).** ASTS and VSAT are `PARTIAL`
> under the constitution's coverage audit: researchable, but the sector must be supplied
> by hand before any sector-aggregate constraint can evaluate (PROGRAM.md §7). The
> assignment is recorded explicitly in each artifact's frontmatter. Note also that the
> platform files **GSAT under `tech.tech_hardware`**, not telecom services — a sector
> screen on telecom would silently omit the tier's second-largest name.

**Named but not researchable — recorded as coverage gaps, not proxied.**

| Ticker | Company | Class | Why it cannot host research |
|---|---|---|---|
| MDA | MDA Space | `NOT_READY` | Canadian space robotics and satellite subsystems — a load-bearing read-through for the tier's supply side. `xbrl_facts` = 0, `src_documents` = 0 |
| TSAT | Telesat | `NOT_READY` | Lightspeed LEO constellation — the closest listed analogue to a *primary* constellation entrant, and therefore the name P5's proxy would most want. Unavailable |
| GILT | Gilat Satellite Networks | `NOT_READY` | Ground segment and satellite networking — the service-layer cost base this thesis cannot size |
| SGBAF | SES S.A. | `NOT_READY` | Luxembourg GEO/MEO fleet operator (OTC ADR) — the European licence-comparator absent from the tier |

**Excluded by design**: JOBY and ACHR are atmospheric and out of scope; Eutelsat, Avio
and SKY Perfect JSAT are listed elsewhere and platform-uncovered — tracked as competitive
inputs, never as theses. **No proxy is substituted for a `NOT_READY` name**: where MDA or
TSAT would have carried a datapoint, the gap is recorded and the conclusion is stated
without it.

**Empty-result disposition.** This tier can genuinely empty out, and the path is live
rather than hypothetical: SATS's spectrum has already transferred to SPCX, and if the two
P11 deals close, **IRDM and GSAT leave the listed universe** and the licence layer is held
entirely privately. If screening then returns no researchable expression, the tier is
**not** closed as a null result and the premise is **not** withdrawn. It converts to a
**holdings-level read-through** recorded in `_cross/`, with the attribution register
retained for 007 and 011 and the tier marked `no_listed_expression` rather than
`no_thesis`. The inherited premise survives; only its expressibility is lost — which is
itself a finding 011 must size against.

## 3. Skill Deployment Matrix

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|:---:|---|:---:|---|
| unit-economics | business-intelligence | Deep | IRDM, GSAT, SATS | none | **P1's decomposition instrument** and P2's per-name split of licence revenue from service revenue |
| operational-kpi | business-intelligence | Deep | IRDM, GSAT, ASTS | none | Subscribers, ARPU, capacity and constellation KPIs — the tier's operating-leverage series (**P1**, **P3**) |
| competitive | equity-research-core | Deep | IRDM, GSAT, ASTS, VSAT | none | **P3's D2D placement**: who attacks the service layer and who holds the licence layer |
| risk | equity-research-core | Deep | IRDM, GSAT, SATS, ASTS, VSAT | none | **P4 and P5**: the gate chain, per-name gate dating, and the deal conditions in the agreements |
| business-model | equity-research-core | Standard | SATS, GSAT, VSAT | none | Classify each model and separate licence revenue from service revenue before any comparison (**DA-21**; **P2**, **P3**) |
| recent-quarter | equity-research-core | Standard | IRDM, GSAT, SATS, ASTS, VSAT | none | Latest reported quarters on the component identity — **and DA-24 hygiene at SATS** (**P1**, **P4**, **P5**) |
| ratio-analysis | quantitative-analysis | Standard | IRDM, SATS, GSAT | none | Margin and return ratios recomputed from components; catches DA-23/DA-24 residuals (**P1**, **P2**) |
| peer-bench | industry-analysis | Standard | IRDM, GSAT, SATS, ASTS, VSAT | none | The five names against each other: margin ladder, leverage, and the licence/service mix (**P6**) |
| sector-overview | industry-analysis | Standard | VSAT, SATS | none | D2D and GEO/LEO segment structure; where the tier's capacity is actually sold (**P3**, **P5**) |
| secular-trends | equity-research-core | Standard | ASTS, IRDM | none | The D2D transition as a secular force, and the licence-value read-through (**P3**) |
| what-if | business-intelligence | Light | IRDM, GSAT | none | The close-versus-break scenario pair; on a break, re-underwrite from scratch (**P4**) |
| growth-strategy | equity-research-core | Light | ASTS, GSAT | none | Primary-grant path versus acquisition path — the reachable proxy for PIL-6's falsifier (**P5**) |

> **Coverage invariant.** Every ticker in §2 appears at least once above; every
> `Subscribed` pair in §1b generates at least one task. Verified mechanically by
> `tools/plan_audit.py` — invariants **I1** (universe ⊆ matrix), **I2** (subscribed ⊆
> matrix), **I3** (skills resolve against the registry) and **I4** (every matrix skill is
> subscribed somewhere, so no row gets the `[P1]` fallback bracket). The `NOT_READY` table
> in §2 is deliberately outside the matrix: those four names cannot host research.

## 4. Depth Tiers

| Tier | Skills | mode-set | Tickers | Output |
|:---:|------|---|--------|------|
| Deep | unit-economics, operational-kpi, competitive, risk | all modes | IRDM, GSAT, SATS, ASTS | Full-mode work on the names carrying P1–P5 |
| Standard | business-model, recent-quarter, ratio-analysis, peer-bench, sector-overview, secular-trends | essentials_modes | As listed | Cross-sectional comparison, the margin ladder, the placement map |
| Light | what-if, growth-strategy | essentials_modes | As listed | The break scenario and the falsifier proxy |

**Budget note.** The matrix yields **39 distinct (ticker, skill) analyses across 5 names**
— a smaller universe than 001's 35 and a larger analytical load per name. Mode expansion
applies multiplicatively, as it did at 001 (2.07×). The `max_tasks: 40` currently recorded
in `thesis.md` **counts mode-tasks and is too low for the matrix as drawn**; either the
budget rises to roughly 65 or the Standard and Light rows are pruned to essentials-only
before dispatch. Recorded as an open item rather than silently reconciled. If it must
come down, drop the Light rows first — never the `risk` row, which is the entire delivery
mechanism for P4 and P5, and never `recent-quarter` at SATS, which carries the DA-24
hygiene the tier's only clean operating read depends on.

## 5. Cross-Cutting Analysis

- **The attribution register** is the cross-cutting output: per name, licence value on
  both bases, operating-business value, the resulting placement, and the deal status —
  the Tier 2 analogue of 001's technology-line register, and the artifact 007, 009 and
  011 cite instead of re-deriving.
- **The gate chain** is a dated checklist per name, with each gate marked
  filing-evidenced or registry-blocked. The blocked entries are reported as a finding
  about platform reach, per the v1.3.0 disposition classes — not as absence of evidence.
- **Macro sensitivity: high but bifurcating.** Three names are long-duration operating
  equities in a NEUTRAL-bias, long-end-hostile regime (10Y at 4.80%). Two names are
  spread-driven and therefore almost rate-insensitive at the margin. **The tier's macro
  sensitivity falls as the deal securities become a larger share of it** — an unusual and
  worth-stating property in a single-theme book.
- **Constitution interaction.** P11 governs IRDM and GSAT at every step — no standalone
  underwriting, 2% binary cap, re-underwrite on a break. **DA-24 governs any SATS read**
  (a licence sale flowed through the operating line; the clean read is the latest
  quarter). DA-17/18/19/21 govern every cross-name quantity. **F6 supplies the Catalyst
  Requirement** that P4 and P5 instrument. The Sector Preferences ranking (**Overweight /
  High**) is the prior this thesis tests, not a finding it inherits.
- **Corpus note.** Per PROGRAM.md §4 the registry has no industrial or aerospace domain,
  so sector-keyed strategy retrieval returns zero rows by construction. Any analogue used
  here is retrieved by **structural situation shape** — a licence sale, an in-flight
  merger spread, a monopoly asset with a commoditising service layer — and labelled
  borrowed. 006 does not attempt a sector-tagged lookup.
- **Pair candidates are constrained, not absent.** The licence-layer-versus-service-layer
  pair is the natural expression of P3, but the Risk Framework caps the tier at **≤ 2
  positions in any single sub-sector** and the theme cap (40% NAV) binds first in a
  single-theme book. With two of five names being P11 securities, at most two Tier 2
  expressions exist at any time, and the pair is one of them. Size is 011's decision; this
  thesis supplies the attribution and the gates.

## 6. Output Contract

- **Per-ticker (dispatcher-resumable)**: `artifacts/{ticker}/{YYYY-MM-DD}_{skill}_{mode}.md`
  — the suffix **must** be `_{skill}_{mode}.md` with the real mode slug, so
  `dispatch.resume_verdict()` can find it.
- **Cross-cutting (not resume-tracked)**: `_cross/{name}.md` — `_cross/tier2-attribution-register.md`
  (primary), `_cross/tier2-gate-chain.md`, `_cross/tier2-d2d-placement.md`.
- **Primary artifact**: `_cross/tier2-attribution-register.md` — per name: licence value
  on basis A and basis B, operating-business value, the licence/service placement, the
  dated next gate, and the deal status. This is what 007, 009 and 011 cite.
- **⚠️ P11 — `deal_security_basis` is mandatory on IRDM and GSAT artifacts.** Every
  artifact written for IRDM or GSAT **must set `deal_security_basis`** in its frontmatter
  (`standalone_pre_merger` while the transaction is unclosed; `post_close` after), and
  every operational metric drawn from those names is tagged pre-merger basis. This is the
  `deal_security_tagging` validation rule in `contracts/artifact-frontmatter.yaml` and it
  is a **fail-level** rule: an artifact on either name that omits the field is rejected,
  not re-run. `not_applicable` is admissible only on SATS, ASTS and VSAT.
- **Frontmatter**: per `contracts/artifact-frontmatter.yaml`, with `thesis_id:
  "006-tier2-connectivity-spectrum"`. All five pins are mandatory: `constitution_pin:
  1.4.0`, `assumption_pin: "2"`, `skill_pin`, `as_of`, `corpus_version`. `definitions_used`
  is required with at least one `DA-NN` — **DA-17, DA-18, DA-19, DA-21 and DA-24 are live
  for every artifact in this thesis.**
- **`PARTIAL` precondition**: ASTS and VSAT artifacts record the manual sector assignment
  in the frontmatter before any sector-aggregate constraint evaluates.
- Snapshot: `snapshots/006-tier2-connectivity-spectrum/{YYYY-MM-DD}_thesis.md`

## 7. Thesis Phases

| Phase | Tasks | Duration | Dependencies |
|:---:|------|:---:|------|
| 1 — Decomposition (P1) | Line-level attribution of IRDM's 8.1-pt margin decline on the component identity; isolate R&D's ≈0.6 pts; test the licensed-service line | Week 1 | Constitution v1.3.0 loaded; 002's validated inputs where they apply |
| 2 — Attribution (P2) | Build the two-basis SOTP; assemble the $19.6B mark with its DA-17 limits; run the split for SATS, IRDM, GSAT, ASTS, VSAT | Week 2 | Phase 1 |
| 3 — D2D placement (P3) | Service-layer compression evidence; place all five names on the axis by the P2 rule; test whether ASTS is placeable at all | Week 3 | Phase 2 |
| 4 — Deal mechanics (P4) | Read the IRDM–RKLB and GSAT–AMZN agreements for consideration, conditions, outside dates and break fees; run close-versus-break | Week 4 | Phase 3 |
| 5 — Gate chain (P5) | The dated checklist per name and gate; classify filing-evidenced vs registry-blocked; build the primary-grant proxy test | Week 5 | Phase 4 |
| 6 — Queue close-out (P6) | Scorecard for §0b: convert or classify every Tier 2 contested figure | Week 6 | Phase 5 |
| 7 — Hand-off | The attribution register for 007 (primes as incumbent satcom competition), 009 (D2D as compute-adjacent demand), 011 (positions, sizing, analogues) | Week 7 | Phase 6 |

## Clarifications

Recorded by `agentii.specify` at creation, 2026-09-18. No `agentii.clarify` round has
run; the following are recorded as open for that pass.

- **Q-1 (P1, attribution granularity)** — Does IRDM's filed disaggregation separate
  licensed-spectrum service revenue from the equipment and other lines finely enough to
  attribute the margin decline by line, or does it stop at the operating-expense level?
  **Provisional answer, pending clarify:** if the filing stops short, P1 defaults to the
  coarser gross-profit − opex test, the limitation is recorded in-line, and the pillar is
  carried as partially evaluated rather than dropped.
- **Q-2 (P2, one mark, different assets)** — The $19.6B mark prices one combination of
  blocks for one footprint (DA-17). Is a **mark-based** transfer admissible as a primary
  SOTP basis for a different licence, or must basis B (capitalised licence cash flow) be
  primary with the mark shown only as the single observed print? **Provisional:** both
  bases reported side by side; the mark labelled as a transaction value and never as a
  unit price.
- **Q-3 (P2, licence carrying value)** — Is the in-place licence separable on the balance
  sheet, or is it an indefinite-lived intangible inside a line that also carries other
  assets? **Open** — it decides whether a third, accounting-derived basis exists.
- **Q-4 (P3, borrowed comparator)** — SPCX's ARPU series is the universe's only
  demonstrated service-layer price series, but SPCX is Tier 0 and belongs to 004. Is it
  admissible inside 006 as a **cited comparator**, or must every Tier 2 price claim rest
  on Tier 2 names alone? **Provisional:** admissible as a comparator, labelled as such,
  and never counted as Tier 2 evidence.
- **Q-5 (P4, Market Data Stage `none`)** — The spread is the central object of P4 and the
  platform carries no price series at this stage, so spread *width* is not measurable
  here. Does 006 carry the spreads qualitatively (a spread exists, its width unmeasured)
  or does it request a market-data stage for these two names? **Flagged for human
  confirmation; if answered differently this is a PATCH to spec, not a MAJOR event.**
- **Q-6 (P5, proxy admissibility)** — Is the primary-grant proxy (a D2D entrant reaching
  commercial service on its own filings rather than an acquired licence) admissible as the
  evaluable substitute for PIL-6's falsifier? **Provisional:** yes as a **trigger for
  external verification**, explicitly not as the falsifier firing — issuer statements are
  `CLAIMED` under P4 and cannot satisfy a falsifier. The real falsifier stays
  `UNRESOLVABLE-FROM-PLATFORM` and is not retired.
- **Q-7 (P4/P6, budget)** — `thesis.md` records `max_tasks: 40`, which is below the 39
  analyses after mode expansion. Raise the budget or prune the Light rows? **Provisional:**
  raise to ~65; pruning `what-if` would remove the break-case re-underwrite that P11
  requires.
