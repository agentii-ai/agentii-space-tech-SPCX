# Research Thesis: 001 — Technology Baseline

**Constitution Ref**: constitution.md v1.2.0 (`constitution_pin: 1.2.0`)
**Created**: 2026-09-18
**Status**: Active
**Time Horizon**: 2026-Q4 (baseline refresh at each issuer's Q3 2026 reporting)

**Claim**: Six technology lines bound the orbital economy's investment cases, each with a hard physical or economic floor. Launch cannot fall below the propellant floor — yet launch is 12.3% of revenue at the company that dominates it. Orbital compute was out-chosen, not out-built.

## 1. Research Question

Across the orbital economy, **what is the *demonstrated* technology baseline — as
distinct from what is claimed — and which single technology line binds first for each
business model that depends on it?**

This is the foundation thesis. It produces no trade ideas. Its output is the
feasibility substrate that every later thesis (valuation, catalyst, position) must
clear under constitution principle **P2**. Its governing discipline is the evidence
grading rule **P4**: every material claim is tagged `DEMONSTRATED` (flown, filed, or
reported), `CLAIMED` (company or press assertion), or `MODELED` (our own derivation).
Roadmaps and target cost curves are `CLAIMED` until flown.

The scope is deliberately *not* "is space a good investment". It is "what is
physically and economically true today, what has a hard floor under it, and where the
binding constraint sits". Six technology lines are in scope, one per pillar:

| # | Technology line | Binding-boundary in constitution terms |
|---|---|---|
| 1 | Launch cost and reusability | A1, F5 (propellant floor) |
| 2 | Orbital power and thermal rejection | A2, F1, F2 |
| 3 | Satellite manufacturing rate and unit cost | A2 |
| 4 | Microgravity processing and reentry return | F3 |
| 5 | Orbital vs terrestrial compute parity | A4, P10 |
| 6 | Orbital, spectral and launch-licence access as finite allocated resources | A2, F6 |

**A note on definitional work.** Two pillars (1 and 5) turn on terms that the industry
uses loosely and inconsistently — "cost per kilogram to orbit" and "cost per kW of
compute". Rather than pick one definition and silently fix it, both pillars require the
**full set of competing definitions to be enumerated, quantified where possible, and
compared side by side**, because the *spread between definitions* is itself a finding.
See Clarifications Q-1 and Q-3 below.

## 1b. Pillars

### Pillar 1 — Launch cost has a hard floor, and no one has crossed it (Priority: P1) 🎯 Minimum Defensible View

Launch cost per kilogram to LEO is the master variable for the entire sector (A1), and
it is bounded below by propellant mass — a floor reusability does **not** remove (F5).
A Starship-class vehicle consumes roughly 4,600 t of propellant per flight; at $1–2/kg
delivered to the pad that is $4.6–9.2M per flight, or **$46–92/kg at 100 t of
payload**. Falcon 9 reusably operates at roughly **$2,700–2,900/kg**. The claim is
that no operator has *demonstrated* commercial-cadence pricing below **$1,000/kg**,
and that any sub-$10/kg figure is arithmetically below the floor and therefore false
as stated.

**Why this priority**: it is the Minimum Defensible View because every application-layer
business case is a derivative of this number. If the curve does not move, nothing above
it becomes viable; if it moves further than the floor permits, the claim is falsified
by arithmetic rather than by argument. Delivering P1 alone yields a defensible partial
conclusion: an inventory of what launch actually costs today, with the floor identified.

**Definitional requirement (Clarification Q-1).** This pillar must first enumerate and
quantify every competing basis for "$/kg to LEO", because they differ by 3–5× and the
sector quotes whichever basis suits the argument. The comparison table *is* a primary
deliverable, not preamble:

| Basis | What it includes | Why it is used | Where it is sourced |
|---|---|---|---|
| **A — Customer list price** | Price paid by an external customer ÷ payload mass delivered | The industry's standard marketing number; how Falcon 9's ~$2,700–2,900/kg is derived | Issuer filings, customer contract disclosures, NASA/DoD award values |
| **B — Marginal cost per launch** | Propellant, refurbishment, range and ops — excludes R&D, factory, overhead | The only basis that actually tests the F5 propellant floor, since A carries margin | Not disclosed by any issuer; `MODELED` from propellant mass and reuse assumptions |
| **C — Fully-loaded amortized cost** | All-in: R&D, manufacturing capacity, overhead, depreciation | The economically complete basis — what an investor should actually pay for | Not disclosed at this granularity; `MODELED` from segment R&D and capex |

The spread between A, B and C is itself the finding: it measures how much of the
sector's claimed cost progress is engineering and how much is accounting.

**Independently falsifiable**: a single documented commercial contract or disclosed
per-launch price that clears the threshold on **any** basis, or a filed
payload-per-flight figure that raises the denominator enough to move the propellant
floor below it.

**wrong_if**: `metric=demonstrated_price_per_kg_to_LEO_P50 threshold=1000 source=issuer_filing_or_customer_contract_disclosure op=< basis=ANY_OF_A_B_C`

**Subscribed**: `SPCX × unit-economics`, `SPCX × operational-kpi`, `SPCX × business-model`, `SPCX × recent-quarter`, `SPCX × sector-overview`, `SPCX × peer-bench`, `SPCX × ratio-analysis`, `RKLB × unit-economics`, `RKLB × operational-kpi`, `FLY × unit-economics`, `FLY × operational-kpi`, `LUNR × operational-kpi`, `PL × operational-kpi`

---

### Pillar 2 — Orbital power and thermal rejection set a hard envelope on every orbital business (Priority: P2)

In vacuum there is no convection and no conduction sink: all waste heat must be
radiated, `P = ε·σ·A·(T⁴ − T_sink⁴)`. At 300 K with ε = 0.9 that is **~413 W/m²**, so
1 MW of continuous electrical load requires **~2,420 m² of radiator** — comparable to
the solar array that powers it, which after the eclipse duty cycle, packing factor and
end-of-life degradation multipliers is **~5,000–5,600 m² per MW** (F1). The claim is
that this envelope, not compute silicon, is what binds orbital compute; that battery
mass through the ~37% eclipse fraction is a first-order driver; and that **no listed
issuer reports orbital compute revenue today** — SPCX's AI segment is ground-based.

**Why this priority**: it is the highest-leverage physics claim in the workspace. It
governs the sector's largest narrative (orbital compute, `太空算力`) and it is the
one where the market's implicit assumptions are furthest from the engineering reality.
It is also already confirmed in flight: **Starcloud-1 carried an NVIDIA H100 that
cannot run at full power because its cooling capacity is insufficient.**

**Independently falsifiable**: any listed issuer disclosing an actual orbital compute
revenue line, or a flown system whose radiator mass per kW reaches terrestrial cooling
parity.

**wrong_if**: `metric=listed_issuer_orbital_compute_revenue_disclosed threshold=0 source=10-K_or_10-Q_segment_disclosure op=>`

**Subscribed**: `GOOG × secular-trends`, `GOOG × recent-quarter`, `NVDA × secular-trends`, `MSFT × secular-trends`, `MRCY × secular-trends`, `BWXT × secular-trends`, `VRT × competitive`, `MSFT × business-model`, `LHX × business-model`

---

### Pillar 3 — Manufacturing rate, not launch capacity, is the binding constraint on constellation economics (Priority: P3)

With launch capacity commercially available, the limit on constellation deployment
shifts to **how fast and how cheaply satellites can be built**. This pillar tests
whether named operators' deployment slippage is caused by launch availability or by
production rate and unit cost, and it maps who controls the critical sub-components —
notably space-grade solar cells, where Rocket Lab owns SolAero and Boeing owns
Spectrolab. Two suppliers is a thin base for an industry planning constellations in
the thousands.

**Why this priority**: it decides whether the sector's revenue timelines are gated by
something SpaceX can sell more of (launch) or by something nobody can buy (production
capacity and supply chain). It also identifies where pricing power sits upstream.

**Independently falsifiable**: if launch availability, not production, is the
documented primary delay cause across the majority of named issuers, the pillar is
wrong.

**wrong_if**: `metric=share_of_named_issuers_citing_launch_availability_as_primary_delay_cause threshold=0.5 source=10-Q_risk_factors_and_MD&A op=>`

**Subscribed**: `YSS × operational-kpi`, `TER × operational-kpi`, `PL × operational-kpi`, `RKLB × supply-chain`, `RKLB × peer-bench`, `BA × supply-chain`, `KRMN × supply-chain`, `LHX × supply-chain`, `HWM × supply-chain`, `TDG × supply-chain`, `HEI × supply-chain`, `WWD × supply-chain`, `CW × supply-chain`, `NOC × supply-chain`, `LMT × supply-chain`, `RTX × supply-chain`, `AVAV × supply-chain`, `KTOS × supply-chain`, `VOYG × supply-chain`, `LHX × business-model`

---

### Pillar 4 — Microgravity processing is demonstrated physics with unproven economics (Priority: P4)

Microgravity genuinely improves specific processes: protein crystal growth without
sedimentation, ZBLAN fluoride fiber without crystallization, polymorph control (Varda's
ritonavir Form III result, published in *Nature*). The physics is `DEMONSTRATED`. The
economics are not. The correct test is **value per kilogram returned versus
fully-loaded cost per kilogram returned** — launch, on-orbit processing, reentry
capsule, and recovery combined — not total addressable market. Varda returns roughly
**50 kg of active pharmaceutical ingredient per mission**, has raised ~$329M, holds an
FAA Part 450 reentry licence, and its first pharma partnership (with UTHR, announced
May 2026) targets first samples as early as 2027. **No microgravity-manufactured drug
has reached market.**

**Why this priority**: it is the sector's most plausible non-communication revenue
line, and the one most often argued from TAM rather than from unit economics. It is
P4 rather than P1 because the near-term investment consequence is limited — there is
no listed pure-play.

**Independently falsifiable**: a listed pharmaceutical partner disclosing a
commercial-scale microgravity manufacturing commitment (as distinct from research or
pilot volumes).

**wrong_if**: `metric=listed_pharma_microgravity_commercial_manufacturing_disclosure threshold=0 source=UTHR_MRK_BMY_AMGN_10-K_or_10-Q op=>`

**Subscribed**: `UTHR × unit-economics`, `UTHR × business-model`, `MRK × growth-strategy`, `BMY × growth-strategy`, `AMGN × growth-strategy`

---

### Pillar 5 — The decisive open question: does orbital compute close before terrestrial compute wins? (Priority: P5)

The orbital-compute thesis rests on a gap: reported orbital infrastructure cost of
**$10,000–40,000 per kW** against a terrestrial build far below it, with large-scale
viability requiring launch at **$100–200/kg** versus today's $2,600–3,400/kg. Both
sides of the ratio are moving — terrestrial AI data centres are themselves constrained
by power availability and cooling, which is the same constraint wearing different
clothes. This pillar does not assert an answer; it frames the comparison term by term
(radiator mass, array mass, launch $/kg, radiation tolerance, terrestrial power price,
terrestrial cooling COP) so that a later thesis can be decided on arithmetic.

**Why this priority**: it is the largest narrative in the sector and the one with the
weakest evidence base, which makes it fragile in both directions. It is P5 because it
cannot be *settled* with today's disclosures — only framed, and monitored against P10's
five gates.

**Definitional requirement (Clarification Q-3).** The denominator decides the answer.
Three defensible terrestrial bases differ by roughly 5–10×, so this pillar must report
**all three** and treat the spread as the finding:

| Basis | What it includes | Why it is used | What it does to the ratio |
|---|---|---|---|
| **A — Hyperscaler marginal cost** | Incremental kW inside an already-built facility: server plus cooling increment and electricity; land, shell and interconnect are sunk | The cost a Google or Microsoft actually incurs for one more kW | Lowest denominator, so the **highest** ratio. Orbital looks worst. Not directly observable — must be `MODELED` |
| **B — Colocation market price** | What a customer pays to rent a kW in a commercial data centre, including the operator's margin and full facility cost | A market-clearing price, therefore observable and comparable | Mid denominator. Reported all-in orbital infrastructure cost of $10,000–40,000/kW lands roughly 5–20× above this basis |
| **C — New-build fully-loaded cost** | Greenfield: land, shell, power interconnect (now itself a binding constraint with multi-year queues), cooling plant, generation, plus IT load | The only true like-for-like against an orbital system, which is also built from scratch | Highest denominator. Reported AI-grade greenfield capex near $10–14M/MW puts orbital at roughly 1–4× — **the only basis on which the threshold of 3 is reachable at all** |

**The crux, stated plainly:** the P5 falsifier is **only reachable against basis C**.
Against colocation price or hyperscaler marginal cost, no foreseeable launch-price
improvement brings the ratio to 3. Per the standing rule in §1c, this is **not resolved
by choosing basis C** — it is reported as a property of each basis:

| Basis | Ratio | Threshold 3 reachable? |
|---|---|---|
| A — hyperscaler marginal | highest | No — not at any foreseeable launch price |
| B — colocation market price | mid | No — orbital sits ~5–20× above |
| C — new-build fully-loaded | lowest | **Yes — orbital sits ~1–4× above** |

That table *is* the finding: it says the orbital-compute thesis is arithmetically
reachable only if you accept the greenfield-construction comparator, and unreachable on
any other. Quoting a single ratio without its basis would be meaningless.

**Independently falsifiable**: a credible techno-economic analysis or operator
disclosure putting the orbital-to-terrestrial cost ratio below the threshold on a
stated basis.

**wrong_if**: `metric=orbital_to_terrestrial_cost_per_kW_ratio threshold=3 source=operator_disclosure_or_peer_reviewed_techno_economic_analysis op=< basis=ANY_OF_A_B_C`

**Subscribed**: `GOOG × secular-trends`, `NVDA × secular-trends`, `VRT × unit-economics`, `MSFT × business-model`, `SPCX × business-model`, `SPCX × what-if`, `GOOG × what-if`

---

### Pillar 6 — Orbital, spectral and launch-licence access are finite allocated resources, allocated before capital can be deployed (Priority: P6)

**Added at Clarification Q-2 on the human's instruction.** Spectrum and orbital slots
are not freely available inputs. They are coordinated globally through the **ITU**
under a first-come priority regime and licensed nationally — the **FCC** in the United
States — while launch and reentry require national licences (**FAA Part 450** in the
US). Each is finite: there are only so many usable orbital shells, only so much usable
L-, S-, Ku- and Ka-band spectrum, and only so much launch-range capacity at the handful
of ranges that can support high cadence. Because allocation *precedes* deployment, a
licensed position is an asset with a real market price rather than a permit.

The reference mark is the **SPCX–EchoStar transaction: $19.6B for AWS-4, H-Block and
AWS-3 spectrum**, FCC-approved with the spectrum transfer closed. That single
transaction prices the resource better than any model can.

**Evidence base.** ITU Space Network List and coordination priority; FCC IBFS filings
and licence grants; FAA Part 450 launch and reentry licences (Varda holds one permitting
unlimited landings at Koonibba over five years — a private-company fact admissible only
as `CLAIMED`, per Clarification Q-4); and range capacity at Cape Canaveral, Vandenberg,
Starbase and Kourou.

**Why this priority.** It is the only constraint in this thesis that is *institutional*
rather than physical, which makes it simultaneously a moat and a dated catalyst. Under
constitution **F6**, any thesis whose value depends on un-granted spectrum or an
un-issued licence must carry that as an explicit, dated regulatory catalyst. This pillar
supplies the evidence base those catalyses draw on — and it is the one place where a
regulatory decision, not an engineering breakthrough, changes the answer.

**Independently falsifiable**: if a new entrant secures primary coordination or a grant
in a contested band or shell *without* acquiring it from an incumbent, the scarcity
premise weakens.

**wrong_if**: `metric=new_entrant_primary_spectrum_or_slot_grant_without_incumbent_acquisition threshold=0 source=FCC_IBFS_or_ITU_Space_Network_List op=>`

**Subscribed**: `SATS × risk`, `IRDM × competitive`, `GSAT × competitive`, `SPCX × risk`

---

> Delivering P1 alone yields a defensible partial conclusion — a documented launch-cost
> baseline with its floor identified. P1+P2 yields the full feasibility envelope for
> every orbital business model in the universe. Research halting at any pillar boundary
> leaves a usable artifact rather than a fragment.

## 1c. Definitional Ambiguity Register (standing rule)

**Standing rule, established by Clarification Q-6.** This sector's vocabulary is not
standardised, and most of its headline numbers are self-defined by the issuer reporting
them. The following is therefore a **binding methodological stance for this thesis and
every thesis that inherits from it**:

> **Clarify the *existence* of a definitional ambiguity; do not resolve it to a single
> choice.** Where a term admits multiple defensible definitions, every artifact must
> report **all** of them, label which one is being quoted, and treat the *spread between
> definitions* as a finding in its own right.

This is not indecision. It is the correct treatment of a domain where the ambiguity is
**load-bearing**: in most cases the choice of definition determines the answer, so
collapsing to one would manufacture false precision. It also supplies the disposition
that CHK003 previously failed on — see the last row of the register.

**Execution consequence.** No pillar may be marked unresolved for being multi-definitional.
A pillar whose `wrong_if` cannot be evaluated on a single number is evaluated on **all**
bases and reported per basis, with the reachability of each basis stated.

### A. Cost metrics

| ID | Term | Competing definitions | Why the spread matters | Pillar |
|---|---|---|---|---|
| DA-01 | Cost per kg to LEO | (A) customer list price; (B) marginal cost per launch; (C) fully-loaded amortized | Differ 3–5×. Only (B) tests the F5 propellant floor, since (A) carries margin and (C) carries R&D | P1 |
| DA-02 | The denominator orbit | LEO vs SSO vs GTO vs "delivered to final orbit" | GTO is roughly 3× harder than LEO per kg; mixing them silently inflates or deflates every comparison | P1 |
| DA-03 | "Reusable" | booster-only reuse (Falcon 9) vs full-stack reuse (Starship) vs fairing/component reuse | Full reuse changes the denominator in DA-01 far more than booster reuse; the word alone conveys neither | P1 |
| DA-04 | Cost per kW, orbital | on-orbit hardware only vs including launch and deployment; nameplate vs actual draw | Including launch roughly doubles the figure; nameplate vs actual is a further large multiplier | P5 |
| DA-05 | Cost per kW, terrestrial | (A) hyperscaler marginal; (B) colocation market price; (C) new-build fully-loaded | Differ 5–10×. **Threshold 3 is reachable only against (C).** Choosing the comparator decides the answer | P5 |
| DA-06 | Launch price vs launch cost | price charged to a customer vs internal cost of delivery | Only meaningful for a vertically integrated operator with internal payloads, where no transaction price exists at all | P1, P3 |

### B. Operational metrics — all self-defined by the reporting issuer

| ID | Term | Competing definitions | Why the spread matters | Pillar |
|---|---|---|---|---|
| DA-07 | Mass to orbit | SpaceX: verified mass from successful launches only, excluding failures and scrubs, counting internal and customer payloads together | Excludes failed attempts, so it overstates delivered mass relative to a launched-mass basis; not comparable to a competitor counting attempts | P1, P3 |
| DA-08 | A "launch" | SpaceX: "customer launch" only if an external payload is the *primary* payload and mission parameters are designed around it | Internal Starlink launches are excluded from customer counts. Cross-issuer launch-count comparisons are therefore invalid without restatement | P1, P3 |
| DA-09 | "Subscriber" | SpaceX: a *service line*, not a person, household or device; excludes managed enterprise and government | 12.0M subscribers ≠ 12M users. A household with residential + roam counts twice | P2, P3 |
| DA-10 | ARPU | SpaceX: subscribers-only service revenue ÷ average subscribers ÷ months — excludes enterprise, government, aviation, maritime | ARPU decline may be a mix-shift artifact of adding lower-priced plans rather than price erosion | P3 |
| DA-11 | Nameplate compute draw | SpaceX: GPUs installed × all-in power draw, **explicitly excluding** cooling, power distribution losses, lighting, security and facility overhead | The stated 1.4 GW is IT load only. True facility draw is materially higher — the exclusion is disclosed but easy to miss | P2, P5 |
| DA-12 | Constellation size | licensed vs launched vs operational vs revenue-generating satellites | Four different numbers used interchangeably in industry commentary; licensing runs years ahead of operation | P3, P6 |
| DA-13 | Production rate | satellites manufactured vs launched vs operational | Manufactured-but-unlaunched inventory looks like progress on a production basis and stalls on an operational one | P3 |

### C. Technical terms

| ID | Term | Competing definitions | Why the spread matters | Pillar |
|---|---|---|---|---|
| DA-14 | Radiation tolerance | rad-hard by process vs by design (TMR/redundancy) vs COTS with mitigation | Different cost curves by an order of magnitude; a COTS claim and a rad-hard claim are not comparable | P2 |
| DA-15 | Thermal rejection temperature | peak vs average; with or without an assumed heat pump | Radiated power scales as T⁴, so a 50 K assumption change moves radiator area by ~1.9× | P2, P5 |
| DA-16 | "Demonstrated" | flown once vs flown at cadence vs flown with disclosed economics vs audited | The single most consequential ambiguity in this thesis — it decides whether a claim is `DEMONSTRATED` or `CLAIMED` under P4 | all |

### D. Market and regulatory terms

| ID | Term | Competing definitions | Why the spread matters | Pillar |
|---|---|---|---|---|
| DA-17 | Spectrum quantity | MHz of bandwidth vs MHz-pop (coverage-weighted) vs licensed geographic footprint | Un-normalised spectrum comparisons are meaningless; the $19.6B EchoStar mark only prices a specific combination | P6 |
| DA-18 | "Regulatory approval" | ITU coordination priority vs national licence grant vs market access | Sequential gates, not synonyms. Passing one says nothing about the next | P6 |
| DA-19 | Orbital slot priority | ITU filing date vs bringing-into-use milestone vs actual operation | Priority can lapse for non-use, so a filing is not a durable asset | P6 |

### E. Financial terms

| ID | Term | Competing definitions | Why the spread matters | Pillar |
|---|---|---|---|---|
| DA-20 | Revenue recognition vs commitment | ASC 606 recognized revenue vs signed contract value vs backlog | The sector prices commitments (EchoStar at $19.6B on signing), so a recognition-only basis understates what the market actually counts | P2 |
| DA-21 | "Space revenue" at primes | each issuer's own segment definition; LMT's Space ≠ NOC's Space ≠ LHX's Space | Segment boundaries are drawn by management and change over time; naive aggregation across primes double-counts and omits | P3 |
| DA-22 | Private-company valuation | post-money vs pre-money; press-reported vs audited | Governed by P4 — admissible as `CLAIMED` only, and can never satisfy a falsifier (Clarification Q-4) | P4 |

### Disposition for unresolvable items (closes CHK003)

If a `wrong_if` cannot be evaluated because the required disclosure does not exist, the
pillar is **not** dropped and **not** failed. It is recorded as
`UNRESOLVABLE-FROM-PUBLIC-SOURCES`, carried forward in `thesis.md → known-open`, and
reported at every synthesis with the specific disclosure that would resolve it named
explicitly. A pillar in this state is a **finding about disclosure quality**, which is
itself relevant to a technology baseline — not a gap in the research.

## 2. Universe Definition

Thirty-five listed issuers, all audited `READY` (constitution §Agent-Coverage Audit:
sector, industry and cohort assigned; filings, XBRL facts and source documents
populated), plus one private company admitted only as a value-chain node under **P6**.
Weights are *analytical effort*, not portfolio positions — this thesis sizes no trades.

| Ticker | Company | Sector | Weight in Thesis | Rationale for Inclusion |
|--------|---------|--------|:---:|------|
| SPCX | SpaceX | industrial.aerospace_defense | 9% | Core anchor (P1). Sets the $/kg curve, operates the largest constellation, and discloses the sector's only real operating metrics (mass to orbit, launches, ARPU, nameplate compute draw) |
| RKLB | Rocket Lab | industrial.aerospace_defense | 5% | Second launch provider; owns SolAero — a critical space-solar-cell supplier; acquiring Iridium (P11 deal security) |
| FLY | Firefly Aerospace | industrial.aerospace_defense | 3% | Third launch data point; small enough that unit economics are legible |
| LUNR | Intuitive Machines | industrial.aerospace_defense | 2% | Lunar delivery — tests the F3/F4 envelope outside LEO |
| PL | Planet Labs | industrial.aerospace_defense | 2% | Constellation operator; evidence on manufacturing rate vs launch capacity |
| KRMN | Karman Holdings | industrial.aerospace_defense | 3% | Component supplier; upstream pricing power |
| VOYG | Voyager Technologies | industrial.aerospace_defense | 2% | Starlab — the ISS-replacement demand signal for habitation and power |
| YSS | York Space Systems | industrial.aerospace_defense | 3% | Satellite manufacturing rate — the direct P3 test case |
| HAWK | HawkEye 360 | industrial.aerospace_defense | 1% | RF geolocation; small-constellation baseline |
| IRDM | Iridium Communications | tech.telecom_services | 5% | Only LEO operator with sustained GAAP profitability; the sector's one profitable-constellation benchmark (P11 deal security) |
| GSAT | Globalstar | tech.tech_hardware | 3% | D2D spectrum economics; Apple capacity agreement (P11 deal security) |
| SATS | EchoStar | tech.telecom_services | 4% | Spectrum as a priced asset — the $19.6B SPCX transaction is the reference mark |
| LHX | L3Harris | industrial.aerospace_defense | 2% | Aerojet Rocketdyne propulsion; space payloads |
| NOC | Northrop Grumman | industrial.aerospace_defense | 2% | Solid rocket motors; Cygnus |
| LMT | Lockheed Martin | industrial.aerospace_defense | 2% | ULA joint venture; space segment |
| BA | Boeing | industrial.aerospace_defense | 2% | Spectrolab space solar cells — one of only two credible space-cell suppliers (P3) |
| RTX | RTX | industrial.aerospace_defense | 2% | Space sensors and electronics |
| HWM | Howmet Aerospace | industrial.aerospace_defense | 2% | Engine and structural castings; launch-rate read-through |
| MRCY | Mercury Systems | industrial.aerospace_defense | 2% | Radiation-tolerant processing — direct P2 evidence |
| BWXT | BWX Technologies | industrial.nuclear_energy | 2% | **Space nuclear power and thermal propulsion** — the only credible path to raising radiator temperature and shrinking F2's penalty |
| TDG | TransDigm | industrial.aerospace_defense | 1% | Component pricing power benchmark |
| HEI | Heico | industrial.aerospace_defense | 1% | Replacement parts; aftermarket economics |
| WWD | Woodward | industrial.aerospace_defense | 1% | Propulsion control systems |
| CW | Curtiss-Wright | industrial.aerospace_defense | 1% | Actuation and defense electronics |
| KTOS | Kratos Defense | industrial.aerospace_defense | 1% | Ground segment and satellite C2 |
| AVAV | AeroVironment | industrial.aerospace_defense | 1% | Autonomy and stratospheric systems |
| TER | Teradyne | tech.semiconductors | 1% | Test and automation; production-rate read-through |
| GOOG | Alphabet | tech.platform_internet | 6% | **Project Suncatcher** — the most detailed public orbital-compute engineering disclosure in the sector. Query as `GOOG`, never `GOOGL` |
| MSFT | Microsoft | tech.platform_internet | 6% | Azure Space; the terrestrial-compute comparator at hyperscale |
| NVDA | NVIDIA | tech.semiconductors | 4% | Compute silicon; an H100 already flew on Starcloud-1 with the F2 cooling failure |
| VRT | Vertiv | industrial.machinery | 4% | Thermal management at scale — the terrestrial comparator that defines the orbital cooling penalty |
| UTHR | United Therapeutics | med.medicines_biotech | 7% | Varda's named pharma partner; the listed proxy for microgravity processing economics (P6) |
| MRK | Merck | med.medicines_biotech | 3% | ISS protein-crystallization research history |
| BMY | Bristol Myers Squibb | med.medicines_biotech | 3% | Microgravity biologics research |
| AMGN | Amgen | med.medicines_biotech | 2% | Microgravity protein research |
| — | **Varda Space Industries** (private) | — | node | **P6 value-chain node only.** No weight, no thesis, no valuation. Enters as the microgravity processing evidence base and as UTHR's counterparty |

**Excluded**: JOBY and ACHR (advanced air mobility) — atmospheric, not orbital, and
admissible only as a certification-timeline read-through. 13 audited `NOT_READY` names
(RDW, SPIR, SPCE, MDA, TSAT, GILT, SGBAF, MOG-A, TDY, ATRO, AMPX, ENS, TMUS) cannot
host work until coverage is acquired. The 9 `PARTIAL` names (BKSY, ASTS, VSAT, AMZN,
AAPL, TRMB, GRMN, PLTR, LLY) are deferred to a follow-on thesis pending manual sector
assignment.

## 3. Skill Deployment Matrix

Depth is assigned surgically, not by importance: `Deep` expands to **all** modes of a
skill (5 modes for most), while `Standard` expands to the skill's `essentials_modes`
and `Light` to the same set at minimum viable scope. Deep is reserved for the two names
that actually carry the baseline — SPCX (the sector's only hard-metric disclosure) and
GOOG (the only detailed orbital-compute engineering disclosure). Everything else runs
Standard or Light.

> **Coverage invariant (added after audit, 2026-09-18).** Every ticker in §2 must appear
> at least once below. The first version of this matrix covered only 13 of 35 universe
> names — 22 were scoped and then never researched — and 11 subscribed pairs generated
> zero tasks. Verified by `tools/plan_audit.py`; expect **3/3 invariants**.

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|----------|:---:|---|:---:|---|
| operational-kpi | business-intelligence | Deep | SPCX | none | Full-mode extraction of the sector's only hard throughput metrics — mass to orbit, launches, ARPU, nameplate compute draw — for the P1 and P3 baselines |
| unit-economics | business-intelligence | Deep | SPCX | none | Full-mode derivation of $/kg-to-orbit against the F5 propellant floor, at segment level |
| secular-trends | equity-research-core | Deep | GOOG | none | Full-mode assessment of Project Suncatcher as the orbital-compute reference design; grade every claim `DEMONSTRATED` vs `CLAIMED` (P4) |
| business-model | equity-research-core | Standard | SPCX, RKLB, GOOG, UTHR, LHX, MSFT | none | Classify each model and separate space revenue from non-space revenue before any comparison (DA-21) |
| competitive | equity-research-core | Standard | SPCX, RKLB, IRDM, SATS, GSAT, VRT | none | Competitive structure per technology line; where two-supplier markets and spectrum holdings concentrate pricing power (P6) |
| risk | equity-research-core | Standard | SPCX, BWXT, SATS, IRDM | none | Technology-disruption and regulatory risk; F4 radiation and the F6 spectrum/licence dimension that underpins P6 |
| recent-quarter | equity-research-core | Standard | SPCX, GOOG | none | Latest reported quarter as the freshness anchor for every DEMONSTRATED metric |
| sector-overview | industry-analysis | Standard | SPCX | none | Sector-level TAM, concentration and regulatory framing |
| peer-bench | industry-analysis | Standard | SPCX, RKLB | none | Cross-company comparison within the launch technology line |
| operational-kpi | business-intelligence | Standard | RKLB, FLY, YSS, TER | none | Launch cadence and satellite production rate as the P3 test cases |
| unit-economics | business-intelligence | Standard | RKLB, FLY, UTHR, VRT | none | Value-per-kg-returned (UTHR/Varda) and the terrestrial cooling-cost comparator (VRT) against the F3 test; FLY's legible unit economics |
| supply-chain | industry-analysis | Standard | RKLB, BA, KRMN, LHX, HWM, TDG, HEI, WWD, CW, NOC, LMT, RTX, AVAV, KTOS, VOYG | none | The space-grade solar-cell duopoly (SolAero vs Spectrolab) plus the full prime and component chain — the P3 bottleneck map |
| what-if | business-intelligence | Standard | SPCX, GOOG | none | Scenario the $/kg and $/kW cost curves to frame the P5 parity question |
| secular-trends | equity-research-core | Light | NVDA, MSFT, MRCY, BWXT | none | Orbital-compute exposure and radiation-tolerant processing — MRCY is direct P2 evidence (DA-14) |
| operational-kpi | business-intelligence | Light | LUNR, PL, HAWK | none | Lunar, constellation and small-constellation operational baselines; PL is the P3 manufacturing-rate test |
| growth-strategy | equity-research-core | Light | MRK, BMY, AMGN | none | Microgravity demand side — whether listed pharma is moving beyond research volumes (P4) |
| ratio-analysis | quantitative-analysis | Light | SPCX | none | Capital-intensity screening cross-check |

## 4. Depth Tiers

| Tier | Skills | mode-set | Tickers | Output |
|:---:|------|---|--------|------|
| Deep | operational-kpi, unit-economics, secular-trends | all modes | SPCX, GOOG | Full-mode per-ticker analysis on the two names that carry the baseline |
| Standard | operational-kpi, unit-economics, supply-chain, what-if, business-model, competitive, risk, recent-quarter, sector-overview, peer-bench | essentials_modes | As listed in the matrix | Essentials-mode coverage |
| Light | ratio-analysis | essentials_modes | SPCX | Screening-level cross-check |

**Budget note.** The matrix now yields roughly 78 tasks. The `specify` scaffold seeds
`thesis.md` with `budget: {max_tasks: 40}`, which is far too tight for a 35-issuer
six-technology-line baseline; the budget is set to **85** in `thesis.md`. The matrix was
first cut from an initial ~230-task draft, then grew by 12 tasks when Pillar 6 (P6
regulatory) added SATS and GSAT to the `competitive` and `risk` rows. If the budget must
come down, drop Standard-tier rows first — never the Deep rows, which carry P1, P2 and P5.

## 5. Cross-Cutting Analysis

- **Sector thesis**: the technology baseline itself is the cross-cutting output — five
  technology lines, five binding constraints, one evidence-graded fact base.
- **The master comparison** (P5): a single term-by-term table placing orbital compute
  and terrestrial compute side by side on radiator mass, array mass, launch $/kg,
  radiation tolerance, power price and cooling COP. This is the artifact later theses
  cite.
- **Macro sensitivity**: **high**. The whole universe is long-duration; the constitution
  records the 10Y at 4.80% with hike risk priced, and bias NEUTRAL for that reason.
  This thesis produces no positions, but its output constrains any later one.
- **Pair-trade candidates**: deferred to a later thesis. Flagged here for continuity —
  the two-supplier structure in space-grade solar cells (RKLB/SolAero vs BA/Spectrolab)
  is the most concrete relative-value setup the baseline identifies.
- **Constitution interaction**: P2 gates every later thesis; P4 governs evidence
  grading here; P6 constrains how Varda may appear; P10 governs when orbital compute
  becomes underwritable; P11 applies to IRDM, GSAT and RKLB as deal securities.

## 6. Output Contract

**Corrected 2026-09-18 to match the dispatcher's resume convention.** The original
contract wrote per-ticker artifacts to `{ticker}/…`, but `dispatch.resume_verdict()`
looks in `artifacts/{ticker}/` and matches on a filename **suffix** of exactly
`_{skill}_{mode}.md`. Under the original path every completed artifact read as
`run` (absent) and would have been silently redone — the filesystem is the checkpoint
(Q56), so a path mismatch is a correctness bug, not a cosmetic one.

- **Per-ticker (dispatcher-resumable)**: `artifacts/{ticker}/{YYYY-MM-DD}_{skill}_{mode}.md`
  — the suffix **must** be `_{skill}_{mode}.md` with the mode being the real mode slug,
  so the resume matrix can find it.
- **Cross-cutting (not resume-tracked)**: `_cross/{name}.md` — a cross artifact spans
  several tickers and therefore satisfies **no** per-ticker mode-task. Its supporting
  tasks will correctly read as `run`. Do not mark them `[x]` on the strength of a
  `_cross/` artifact.
- Snapshot: `snapshots/001-technology-baseline/{YYYY-MM-DD}_thesis.md`
- **Primary artifact**: a technology-line register — six lines, each with its binding
  constraint, its governing physical bound with units and source, and every claim
  tagged `DEMONSTRATED` / `CLAIMED` / `MODELED`.

## 7. Thesis Phases

| Phase | Tasks | Duration | Dependencies |
|:---:|------|:---:|------|
| 1 — Foundation (P1) | Launch-cost baseline: build the A/B/C definition table for $/kg with figures; SPCX/RKLB/FLY unit economics and operational metrics; the F5 propellant floor | Week 1 | Constitution v1.2.0 loaded |
| 2 — Constraint envelope (P2) | Orbital power and thermal: F1/F2 derivations, radiator and array mass per kW, radiation tolerance (F4), BWXT nuclear path | Week 2 | Phase 1 |
| 3 — Production and supply (P3) | Manufacturing rate and supply-chain mapping; the space-solar-cell duopoly (SolAero vs Spectrolab); deployment-slippage cause analysis | Week 3 | Phase 2 |
| 4 — Regulatory allocation (P6) | ITU/FCC coordination priority, FAA Part 450 licences, launch-range capacity; price the resource off the SPCX–EchoStar $19.6B mark | Week 4 | Phase 3 |
| 5 — Microgravity and reentry (P4) | Varda as P6 node; UTHR partnership terms; value-per-kg-returned vs cost-per-kg-returned (CLAIMED evidence only) | Week 5 | Phase 4 |
| 6 — Parity framing (P5) | Orbital vs terrestrial compute on all three terrestrial comparators; P10 gate check; publish the technology-line register | Week 6 | Phase 5 |
| 7 — Synthesis | Cross-cutting synthesis; verdict on each pillar's `wrong_if`; hand-off notes for thesis 002 | Week 7 | Phase 6 |

## Clarifications

Recorded by `agentii.clarify` (round 1, 2026-09-18). Scanner output: 1 mechanical
candidate (`as_of` missing); 4 further intent ambiguities raised manually, since the
deterministic scan cannot see definitional ambiguity.

- [2026-09-18] Q-1 (P1, `demonstrated_price_per_kg_to_LEO_P50`): **Which basis for
  "price per kg" should the falsifier measure — customer list price, marginal cost, or
  fully-loaded amortized cost?** → A: **Do not choose one. Enumerate every competing
  definition of price per kg, compare them in the documents, and clarify all definitions
  and numbers.** P1 now carries a mandatory A/B/C basis table (customer list price /
  marginal cost per launch / fully-loaded amortized) as a primary deliverable, and the
  falsifier is evaluated `basis=ANY_OF_A_B_C`. The spread between bases is itself the
  finding.

- [2026-09-18] Q-2 (P2, `listed_issuer_orbital_compute_revenue_disclosed`): **How strict
  should "revenue" be — any recognized revenue, a material/reportable segment, or a
  signed offtake?** → A: **Explain this question and its options in detail. Separately:
  orbital slots and launch licences require international and domestic regulatory
  approval and are finite, special resources — make this a pillar.** The threshold
  strictness is **governed by the Q-6 standing rule, not resolved by a choice** — see
  below. A new **Pillar 6** was added covering orbital, spectral and launch-licence
  access as finite allocated resources, with falsifier
  `new_entrant_primary_spectrum_or_slot_grant_without_incumbent_acquisition > 0`
  sourced to FCC IBFS / ITU Space Network List.

- [2026-09-18] Q-3 (P5, `orbital_to_terrestrial_cost_per_kW_ratio`): **Which terrestrial
  basis should the ratio use?** → A: **Describe this question in detail and contrast the
  different definitions.** P5 now carries a mandatory A/B/C comparator table (hyperscaler
  marginal cost / colocation market price / new-build fully-loaded) and must report all
  three. The falsifier is evaluated on `basis=C_new_build_fully_loaded`, since that is
  the only basis on which the threshold of 3 is reachable at all.

- [2026-09-18] Q-4 (P4, private-company evidence): **How should press-reported private
  figures such as Varda's ~50 kg per mission be treated under P4?** → A: **Admissible as
  `CLAIMED` only.** Private-company figures may inform the analysis but can never satisfy
  a falsifier. Consequence: Pillar 4's economic test can be *framed* but never *settled*
  from public sources, and this must be stated in every P4 artifact rather than papered
  over.

- [2026-09-18] Q-5 (spec header, scanner finding `missing_as_of`): **What is the
  market-data reference date for this thesis?** → A: **2026-09-18, provisionally** — the
  date of the constitution's agent-coverage audit. Recorded as the `as_of` for all
  temporal consistency checks (CHK005). Flagged for human confirmation; if market data
  is sourced later than this date, `as_of` must move with it.

- [2026-09-18] Q-6 (methodology, all pillars): **Should the definitional ambiguities be
  resolved to a single choice, or recorded as ambiguities?** → A: **Write all the
  multi-definition and ambiguity issues into `spec.md`. Clarify the *existence* of the
  problems but do not give a choice for now — in the research that follows, wherever
  these different definitions and ambiguities arise, give the definition from multiple
  angles rather than one.** Encoded as the standing rule in **§1c Definitional Ambiguity
  Register**, which enumerates 22 ambiguity classes (DA-01 … DA-22) across cost metrics,
  issuer-defined operational metrics, technical terms, market/regulatory terms and
  financial terms. Consequence: the P2 threshold question below is **no longer blocking**
  — it is one of the DA-20 ambiguities and is reported on all bases. This also supplies
  the CHK003 disposition (see §1c, closing paragraph).

### P2 threshold — disposition under the standing rule

Previously recorded as an open, blocking question. Under Q-6 it is **resolved as an
ambiguity to report, not a choice to make** (registered as DA-20). All four competing
readings are carried and reported side by side:

| Reading | Fires when | Character of the risk |
|---|---|---|
| Any recognized revenue | A single disclosed dollar of recognized orbital-compute revenue | Fires on a trivial pilot booking that proves nothing about the business case |
| Material / reportable segment | A reportable segment or stated materiality is crossed | May be unfalsifiable in practice — materiality lags the phenomenon |
| Signed offtake or contract | A contracted but unrecognized commitment exists | Fires earliest; matches how the sector prices commitments (EchoStar at $19.6B on signing) |

Compounding fourth axis — **what counts as "orbital" compute**: compute *in* orbit
(Suncatcher), compute *for* orbit (ground processing of satellite data), and
communications *from* orbit (Starlink) are three different things, and only the first is
clearly in scope. Reported as three separate measurements rather than collapsed.
