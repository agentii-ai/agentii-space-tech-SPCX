# Research Thesis: 009 — Tier 4: Enabling Layer (Power, Thermal, Compute)

**Claim**: The enabling layer is a cohort of four listed compute-capacity sellers and one
silicon supplier, none of which reports a discrete orbital revenue line. The orbital case
requires all five of P10's conditions; zero are met at every named operator. The investable
question is therefore **positioning, not demand** — power is the binding constraint, the
cost *share* is unmodelled, and the terrestrial comparator is a scaling cost curve rather
than a scarcity rent.

**Constitution Ref**: constitution.md **v1.6.0** (`constitution_pin: 1.6.0`) — **re-pinned
at re-scope, 2026-09-19.** Was `1.4.0`, which predates the v1.6.0 **§Universe Definition
re-cut**. That re-cut is not cosmetic for this thesis: it **moved VRT out of Tier 4's
membership into a named comparator role**, stating that *"a thesis cannot hold its subject
and its control. Thesis 009's own §3 said so while listing it as a member."* This thesis's
entire §2 and §3.2 were structural evidence for that amendment, and are rewritten here to
comply with it.
**Created**: 2026-09-18 · **Re-scoped**: 2026-09-19 (constitution 1.4.0 → 1.6.0)
**Status**: **PLANNED — spec COMPLETE and self-consistent. Not frozen. No tasks may be
generated.**
**Wave**: 2 (activates when a slot opens under `max_theses_active: 6`)
**板块**: Tier 4 · **Binding constraint**: **`POWER`** — single, named. The `MULTI`
declaration is **retired**; see §1c.
**Depends on**: `001-technology-baseline` (artifacts below), `002-evidence-validation`
(**COMPLETE** — the three notifications in §0.1–§0.3 are its output and are consumed here,
not re-derived), `003-launch-cost-curve-value-migration` (**the framing authority — see
§1a**)
**Market data**: **LIVE — declared, `per_row`.** A keyless feed exists
(`data-tools/market_data.py`, source `nasdaq`; verified in 004 round 3 at SPCX `$152.71`,
close 2026-09-18). §1's second limb — *how much of that positioning is already priced* — is
**unanswerable without a quote**, and the stub declared no stage at all. See §5.
**Produces**: a **positioning grade per name** — contracted, narrated, or absent — with the
P10 gate audit attached. **No trade ideas**: sizing is 011's.

---

## 0. Inherited baseline — what this thesis does NOT re-derive

**This section was internally contradictory before the 2026-09-19 re-scope and is the
reason the re-scope was ordered.** It asserted VRT's *"scarcity pricing, which is what a
functioning market produces"* and *"the GPU is not the dominant cost term"*, while three
`UPSTREAM NOTIFICATION FROM THESIS 002` blocks — appended below §4 in the same file —
refuted exactly those two claims. **A spec may not carry the superseded version of its own
evidence.** The superseded claims are struck below and the three notifications are folded
into §0 as the register that governs, rather than left as corrections appended after a
contradicting §0.

**Path shorthand used throughout this section — declared, not implied.** Paths are relative
to *this spec's directory*; `001/` expands to `../001-technology-baseline/`, `002/` to
`../002-evidence-validation/`, `003/` to `../003-launch-cost-curve-value-migration/`, `004/`
to `../004-tier0-spacex-anchor/`. Every row resolves to a file on disk.

| # | Inherited result | Artifact | Grade |
|---|---|---|---|
| 1 | **Terrestrial compute is constrained but expanding.** MSFT FY2026 capex **$115,948M** — at the reported **$10–40M/MW** that is **2.9–11.6 GW of new capacity annually**, against SPCX's **1.4 GW cumulative** nameplate draw. *"Microsoft alone adds ~8× SPCX's entire installed base every year."* 001 called this *"the strongest single datum against the orbital-compute case produced anywhere in this thesis."* | `001/artifacts/MSFT/2026-09-18_1239_secular-trends_methodology.md` | `DEMONSTRATED` (capex) / `MODELED` (the GW conversion — the $10–40M/MW band is a stated range, not a disclosure) |
| 2 | **F2 precedes F4 empirically.** Starcloud-1's H100 failed on **thermal**, not radiation — the first gate stopped it before the second was tested. | `001/_cross/phase-2-constraint-envelope.md` | `DEMONSTRATED` |
| 3 | **NVDA has no space product line**, and is R&D-intensive at **7.7%** — so its absent rad-hard SKU is a **revealed preference about market size**, not a capability gap. | `001/artifacts/NVDA/2026-09-18_1239_secular-trends_methodology.md` | `DEMONSTRATED` (the absence) / `MODELED` (the inference) |
| 4 | **GOOG Project Suncatcher**: 81-satellite reference configuration, two prototypes targeted early 2027. Graded **`CLAIMED` throughout — no flight, no prototype, no filing.** | `001/artifacts/GOOG/2026-09-18_1239_secular-trends_methodology.md` §2, §3 | `CLAIMED` |
| 5 | **The scale asymmetry runs both ways.** Alphabet's quarterly R&D base makes Suncatcher **affordable at a scale no space company can match** — and **financially irrelevant to Alphabet.** *"Alphabet has no financial need to make Suncatcher work."* | `001/artifacts/GOOG/2026-09-18_1239_secular-trends_methodology.md` §1 | `DEMONSTRATED` |
| 6 | **P5's terrestrial denominator is `UNRESOLVABLE-FROM-PLATFORM`.** Colocation and greenfield costs are **commercially licensed** — a *stronger* condition than merely unreachable. VRT bounds the **cooling equipment share only.** | `001/_cross/phase-2-constraint-envelope.md` | `DEMONSTRATED` |
| 7 | **The "capability real, business immaterial" pattern** — 4–5 instances in this tier and across the universe. It suppresses the very disclosure P10's falsifiers need. **This pattern is this thesis's central methodological obstacle, not a footnote.** | `001/_cross/technology-baseline_synthesis.md`; `001/_cross/universe-panorama_synthesis.md` | `DEMONSTRATED` |
| 8 | **P10 gate status: UNMET on all five conditions.** No listed issuer reports orbital-compute revenue. | `constitution.md` §P10; `001/_cross/phase-2-constraint-envelope.md` | `DEMONSTRATED` |
| 9 | ~~VRT's operating margin *expanded 2.7 pts on +24.1% revenue* — **scarcity pricing, which is what a functioning market produces.**~~ **STRUCK — SUPERSEDED by §0.2.** The `+2.7 pts / +24.1%` figures are retained as a *quantity*; **the causal attribution is withdrawn.** | ~~`001/artifacts/VRT/2026-09-18_1239_unit-economics_methodology.md`~~ superseded by `002/artifacts/VRT/2026-09-18_1500_unit-economics_methodology.md` | **`UNRESOLVABLE` — the mechanism is undisclosed rate.** See §0.2 |
| 10 | ~~**The GPU is not the dominant cost term.** NVDA's 65.6% margin sits against $2.3–4.6M/MW of power+thermal at the F5a floor.~~ **STRUCK — SUPERSEDED by §0.3, and the claim is INVERTED.** | ~~`001/_cross/phase-2-constraint-envelope.md`~~ superseded by `002/artifacts/NVDA/2026-09-18_1500_secular-trends_methodology.md` | **`MODELED` presented as a fact.** See §0.3 |
| 11 | **A standing discipline carried into every figure in this thesis (DA-23).** The platform's `search_xbrl_facts` **strips the sign** from `OperatingIncomeLoss`; `get_statement` on the same accession preserves it. 001 declared GSAT *"clean on DA-23"* — *"clean-positive count: 15 of 15"* — and built a section on the stripped figure. **GSAT's filed operating margin is −7.37%, not +7.4%.** GSAT is **not** in this thesis's universe; **the instrument is.** | `001/artifacts/GSAT/2026-09-18_2040_competitive_methodology.md` (**superseded**), checked against GSAT 10-Q `0001366868-26-000039` §income statement via `get_statement` | `DEMONSTRATED` — **every margin in §0 and every pillar falsifier must pass the component identity (`gross profit − opex`) before it is quoted.** |

### §0.1 Correction A — F2 has downgraded (source: 002)

**Constitution's named binding constraint for orbital compute is now a QUALITATIVE bound,
not a quotable figure.** The radiator band is **undefined rather than wide**: the 8 kg/m²
areal density is an admitted placeholder with no sourced value anywhere on the platform,
and F2's own admissible source class (peer-reviewed literature / flown-hardware disclosure)
**does not exist in the corpus**.

**What survives, and it is robust:** order **10³ m²** and order **10¹ t per MW** — stable
across a 7.72× area range, a 3× density range and a 2× COP penalty. **The constraint still
binds; it cannot be quoted to four significant figures. Do not cite F2 to a point value.**

Two corrections that travel with it:

1. **001's 24× nuclear reduction is ~16×.** With a COP = 2 heat pump folded in — the loop
   001 left open — it is **470 m²/MW, not 313**. The 24× assumed a free pump.
2. **The eclipse multiplier is 1.587×, not 8×.** Dawn-dusk SSO has no eclipse; array falls
   **5,080 → 3,201 m²/MW**. The "8× more productive" claim implies an unstated reference
   terrestrial capacity factor of **18.6%** — at an assumed CF it is trivially satisfied, at
   an unstated CF it has no truth value.

Source: `002/artifacts/GOOG/2026-09-18_1500_secular-trends_methodology.md`

### §0.2 Correction B — the terrestrial comparator is NOT tradeable (source: 002)

**This is the correction that strikes §0 row 9.** VRT's artifact reports that the quantity
P5 needs from this layer is **non-formable, not merely wide**. It passes the ±50% acceptance
test on a technicality (±7.1% on the share bound), and the artifact explicitly calls that
**a false clearance**.

**What VRT supplies:** a **bound and a direction, never a level.** Basis A (hyperscaler
marginal) and Basis B (colocation market) stay out of reach **structurally** — VRT sells
equipment *to* colocation operators, so its revenue is a **supplier price, never a rental
price**. No further work on VRT changes this. **`PUE` returns zero hits in its 10-Q.**

The four bounds, **none a level**: share α **12.3–14.2%** (one-sided upper bound); margin
structure β $0.62/$0.38/$0.15/$0.19; **capex intensity γ 4.9% of sales against 24–37%
revenue growth — a bottleneck shows up as capital intensity, and VRT's does not**; backlog
δ $15.0B vs $7.2B.

**And the adversarial conclusion now has a better mechanism.** 001 argued terrestrial
cooling is *"a competitive, mass-produced, 24%-growing solution"* and that the orbital case
must beat it. **That survives — but its pricing-power evidence does not.** VRT's margin
expansion is attributed by its own 10-Q to *"the mix of product and service sales"*, and
**Note 4 shows the mix moved only +0.72 pts** — which cannot produce +372 bps unless
services carried a ~520-point gross-margin differential. **~365 bps is undisclosed rate.**
The prior year inverted: **+27.7% revenue with gross margin FALLING 30 bps**, in a year the
filing calls *"improved price realization."*

**Consequence for sizing:** with scarcity rents removed, terrestrial cooling is a **scaling
cost curve**, not a rent — and **a scaling cost curve is a harder competitor than a rent.**
**Do not build a position on the assumption that the terrestrial side is protected by
scarcity.**

Source: `002/artifacts/VRT/2026-09-18_1500_unit-economics_methodology.md`

### §0.3 Correction C — the cost-stack claim is INVERTED (source: 002)

**This is the correction that strikes §0 row 10.** 001 carried a claim into this thesis:
*"the GPU is not the dominant cost term."* **Its own cited source says the opposite**, and
001's carry-forward propagated the inversion.

`001/_cross/phase-2-constraint-envelope.md` §Corrections 3 states: *"**The dominant term is
the compute hardware and its replacement rate, which this phase did not model.**"*

Three compounding problems with the claim as inherited:

1. **The GPU term was never in the table.** No issuer discloses a GPU ASP — this is
   unmodellable at every row in the universe, not just NVDA.
2. **A 75% gross margin measures the *seller's* rent, not the *buyer's* cost share.**
   Reading NVDA's gross margin as evidence the part is cheap **inverts the sign**.
3. **"Meaningful but not dominant" is corner-dependent presented as corner-independent.**
   At the $10M/MW corner, launching power+thermal *alone* is **46%** of all-in — excluding
   array, radiator, reactor hardware, and the GPU.

**What survives, and it is a different claim:** **power is the binding *constraint*** —
confirmed by NVDA unprompted twice, and by an installed base denominated in MW rather than
GPU counts. **Cost *share* is unmodelled. Do not size against a cost stack you cannot
build.** This is why §1c names `POWER` and not `CAPITAL`.

Two further findings that bear on this tier:

- **NVDA's terrestrial roadmap and the orbital requirement are DIVERGING.** Its flagship is
  a **liquid-cooled** design; the company's CEO states *"Liquid cooling is obviously out of
  the question"* in orbit.
- **NVDA's stated orbital thesis is imaging/inference** — edge data reduction, *"ignore all
  of the data… until you see something interesting"* — **not megawatt compute.** That is a
  different product category from the one this thesis's compute narrative assumed.

Source: `002/artifacts/NVDA/2026-09-18_1500_secular-trends_methodology.md`

### What 001 did not do

001 produced **quantities and prices** for this layer — capex, capacity, margins, drawn
bounds. It produced **no positioning grade and no price-in**. Every row above is a fact about
a company's terrestrial business. **None of them is a fact about an orbital one.** That gap
is this thesis's entire scope.

---

## 1. Research Question

**Which listed issuers sell power, thermal management or compute capacity as primary
revenue — and of those, which has a *signed or contracted* path to orbital revenue rather
than a capability narrative, and how much of that positioning is already priced?**

Three things this question deliberately is **not**:

- **Not "is orbital compute viable."** That is **003's disposition, and 003 has already
  closed it** (§1a). 009 takes the disposition as given.
- **Not a demand forecast.** Demand is not observable; positioning is.
- **Not a multi-constraint question.** The `MULTI` compromise is retired (§1c).

### 1a. The framing dispute — resolved: **003 governs**

The stub said *"That is 003's framing problem and P10's gate."* **003's spec says the
opposite**, in its Pillar 2 *Reachability caveat (P10)*:

> *"It does **not** value any constellation, and it does not treat orbital compute as a
> destination: no listed issuer reports orbital-compute revenue, so it is not a pool, it is
> a watch item."* — `../003-launch-cost-curve-value-migration/spec.md` §1b P2

**003 governs. Three reasons, in order of weight:**

1. **003 is the charter.** 003's own header states it is chartered to answer *"where does
   value accrue"*, and `PROGRAM.md` §5 declares 003 → 004/005 as *"the curve that 004 and
   005 price off."* 009 is not chartered to build a value pool and cannot re-open one.
2. **009's line delegated a question that was already answered.** *"That is 003's framing
   problem"* reads as an open hand-off. It is not open: 003 recorded the disposition — a
   **watch item, not a pool** — and that is a *negative* finding, not an absence.
3. **P10 already governs both**, and 003's sentence is a direct restatement of it. Under
   P10: *"Absent all five [conditions], orbital compute is a **watch item, not a thesis**."*
   003 said the same thing in its own words.

**Consequence, and it is the load-bearing change to this thesis.** 009 **must not depend on
the orbital-compute framing at all.** The positioning question survives without it: an
enabling layer that sells power, thermal management and compute capacity sells into *any*
orbital build-out — constellations, stations, hosted payloads — regardless of whether
orbital compute ever becomes a pool. **The stub's §3.3 (*"009 owns the investable
consequence"*) is withdrawn**: there is no investable consequence to own while P10 is
unmet. What 009 owns is the **positioning grade** and the **P10 gate audit as a gate**.

### 1b. Why this thesis exists at all

Because it is the tier where **A2's constraints actually bind**, and because the
constitution's Tier 4 membership test — *primary revenue from selling power, thermal
management or compute capacity, where the orbital case is a stated demand path* — has never
been applied to the universe 001 assembled. The v1.6.0 re-cut says the pre-amendment tier
*"spanned at least five unrelated industries (data-centre thermal, GPU silicon, hyperscale
cloud, batteries, telecom) and was in fact a **theme**."* **§2 is that test, applied.**

### 1c. The `MULTI` declaration is RETIRED — split into three sub-questions, two delegated

The stub declared `MULTI` — *"Thermal (F2) binds the compute narrative; `CAPITAL` binds the
terrestrial comparator; regulatory (F6) binds the D2D demand side. **These do not reduce to
one constraint**"* — invoking the same P3 compromise as 005.

**That declaration was a symptom, not a justification.** The three constraints did not
reduce to one because **they belonged to three different questions, none of which is this
thesis's.** Splitting them shows this:

| Sub-question | Constraint it carries | Owner — and why not 009 |
|---|---|---|
| **Q-A. Does the *orbital compute* narrative close physically?** — radiator rejection, array area, eclipse duty cycle, the F2/F4 ordering | `THERMAL` (F2) | **002.** Physics validation is 002's charter and Q-A is **already discharged** — §0.1. 009 may not re-derive F2 and must not cite it to a point value. |
| **Q-B. Is the *terrestrial comparator* protected, and at what cost floor?** | `CAPITAL` | **002 owns the VRT unit-economics work** (§0.2), and **004 owns the AI-segment framing**. VRT is now a **comparator, not a member** (§2b) — and under the membership test a comparator's capital constraint is not a Tier 4 constraint. |
| **Q-C. Does the *D2D demand side* clear spectrum and regulatory gates?** | `REGULATORY_SPECTRUM` (F6) | **006** (Tier 2 — connectivity and spectrum). AAPL and TMUS are **006's names**, not this thesis's (§2c). |
| **Q-D. Which listed issuers are positioned to sell into an orbital build-out, and how much is priced?** | **`POWER`** | **009 — this thesis, and only this.** |

**Q-D is the thesis.** It survives the split because it is the only one that asks about the
*seller's revenue composition* rather than about physics, the terrestrial incumbent's
protection, or a demand-side regulatory gate.

**Why `POWER` and not `DEMAND`.** `DEMAND` would re-import exactly the framing 003 closed in
§1a — it presumes an orbital-compute demand pool to be measured. `POWER` is the constraint
the evidence actually names: the tier is *defined* by selling power and its rejection, A2
binds through it, and 001 records NVDA confirming it **unprompted twice**, with an installed
base **denominated in MW rather than GPU counts** (§0.3). **One thesis, one constraint** —
P3 is satisfied by naming one, not by declaring three.

---

## 1b. Pillars

### Pillar 1 — No Tier 4 member reports a discrete orbital revenue line; the tier's orbital exposure is undisclosed and therefore unpriced (Priority: P1) 🎯 Minimum Defensible View

**Claim.** Across the admitted universe, the count of members disclosing a discrete orbital
or space revenue line — in the segment note or in the revenue disaggregation table — is
**zero**. This is not an assertion of absence; it is a **measured** zero, established by
direct inspection of each member's most recent 10-Q/10-K revenue disclosures. It is P10
condition (1) — *revenue or offtake* — restated at the cohort level, and it is why the
thesis is a positioning study rather than a demand study.

**Consumes**: `GOOG × business-model`, `MSFT × business-model`, `AMZN × business-model`,
`NVDA × business-model`, `GOOG × recent-quarter`, `MSFT × recent-quarter`

**Why P1**: it is the MDV because it is **decidable at zero cost to the thesis's other
claims**. If any member discloses the line, P2–P5 must be re-framed around it; if none does,
every downstream pillar is bounded by that fact.

**Independently falsifiable**: a member reporting orbital, in-orbit, space-based or
space-qualified revenue as a named line, in a segment note or a `RevenueFromContractWithCustomer`
disaggregation, at any period.

**wrong_if**: `metric=count_of_tier4_members_reporting_a_discrete_orbital_or_space_revenue_line threshold=0 source=10-Q_or_10-K_segment_note_and_revenue_disaggregation_table op=>`

**Subscribed**: `GOOG × business-model`, `MSFT × business-model`, `AMZN × business-model`, `NVDA × business-model`, `GOOG × recent-quarter`, `MSFT × recent-quarter`, `AMZN × recent-quarter`, `GOOG × secular-trends`, `MSFT × secular-trends`, `GOOG × peer-bench`

---

### Pillar 2 — The orbital initiative is immaterial to every member's P&L, which is *why* the disclosure P1 needs does not exist (Priority: P2)

**Claim.** The count of members disclosing an orbital programme's **cost, headcount or
contract value** in a filing or on an earnings call is **zero**. This is the
**"immaterial-to-the-counterparty" pattern** (§0 row 7) with a mechanism attached: Alphabet's
quarterly R&D base is roughly **20× SPCX's entire Space segment revenue** (§0 row 5), so
Suncatcher is simultaneously *affordable beyond any space company's reach* and *invisible in
the financial statements*. **The absence of disclosure is a consequence of size, not of
secrecy** — which means no amount of further work on these filings will produce it.

**Consumes**: `GOOG × secular-trends`, `MSFT × secular-trends`, `AMZN × secular-trends`, `NVDA × secular-trends`, `NVDA × risk`

**Why P2**: it converts P1's zero from an observation into an **explanation**, and it is the
pillar that would falsify the thesis's method if it broke — a member that *does* break out
programme economics proves the pattern is not structural.

**Independently falsifiable**: any member quantifying an orbital programme — capex, opex,
headcount, a signed contract value, or a named counterparty — in a 10-Q, 10-K or transcript.

**wrong_if**: `metric=count_of_tier4_members_disclosing_orbital_programme_cost_headcount_or_contract_value_in_a_filing_or_transcript threshold=0 source=10-Q_10-K_MD&A_and_earnings_call_transcript op=>`

**Subscribed**: `GOOG × secular-trends`, `MSFT × secular-trends`, `AMZN × secular-trends`, `NVDA × secular-trends`, `GOOG × peer-bench`, `MSFT × peer-bench`, `AMZN × peer-bench`, `NVDA × peer-bench`, `NVDA × risk`

---

### Pillar 3 — The competitor the orbital case must beat is a scaling cost curve, not a scarcity rent (Priority: P3)

**Claim.** VRT's margin expansion is **not explained by the mechanism its own 10-Q
attributes it to**. The filing says *"the mix of product and service sales"*; Note 4 shows
the mix moved **+0.72 pts**, which cannot produce **+372 bps** unless services carried a
~520-point gross-margin differential. **~365 bps is undisclosed rate.** The prior year
inverted — **+27.7% revenue with gross margin FALLING 30 bps**, in a year the filing calls
*"improved price realization."* The count of comparator margin-expansion periods in which
the disclosed mix change **fully explains** the expansion is therefore **zero**.

**The consequence is adversarial to this thesis's own narrative and is carried anyway:**
terrestrial cooling is a **scaling cost curve, and a scaling cost curve is a harder
competitor than a rent** (§0.2). Capex intensity γ is **4.9% of sales against 24–37% revenue
growth** — a bottleneck shows up as capital intensity, and VRT's does not.

**Consumes**: `VRT × unit-economics`, `VRT × business-model`, `VRT × ratio-analysis`

**Why P3**: it is the pillar that makes the thesis **falsifiable in the direction that
hurts**. 001's version (*"scarcity pricing"*) was unfalsifiable — any margin expansion
confirmed it. This version has a stated mechanism and a stated counter-mechanism.

**Independently falsifiable**: a comparator margin-expansion period where the disclosed mix
change, applied to the disclosed segment gross margins, closes the expansion to within the
disclosed rounding — i.e. a period where the mechanism *is* disclosed rate.

**wrong_if**: `metric=count_of_terrestrial_comparator_margin_expansion_periods_where_disclosed_mix_change_fully_explains_the_expansion threshold=0 source=VRT_10-Q_gross_margin_mix_note_Note_4 op=>`

**Subscribed**: `VRT × unit-economics`, `NVDA × unit-economics`, `VRT × business-model`, `VRT × ratio-analysis`, `GOOG × ratio-analysis`, `MSFT × ratio-analysis`

---

### Pillar 4 — Power is the binding constraint; the cost *share* is unmodellable at every member (Priority: P4)

**Claim.** The count of members disclosing a **GPU ASP or a compute-hardware cost share** is
**zero** — the GPU term cannot be built from any issuer's disclosure (§0.3). What *is*
established is directional and survives: **power is the binding constraint**, confirmed by
NVDA unprompted twice and by an installed base denominated in MW rather than GPU counts.
**Cost *share* is unmodelled**, and at the $10M/MW corner, launching power and thermal
*alone* is **46%** of all-in — before array, radiator, reactor hardware or the GPU. A pillar
that cannot be sized must say so rather than be sized anyway.

**Consumes**: `NVDA × supply-chain`, `NVDA × unit-economics`, `NVDA × secular-trends`, `GOOG × supply-chain`, `NVDA × what-if`

**Why P4**: it is where 001's inversion (§0.3) would have propagated into a sizing error,
and it is the direct justification for the `POWER` constraint named in §1c.

**Independently falsifiable**: any member disclosing a GPU ASP, a compute-hardware cost
share of a data-centre build, or an orbital power budget denominated in MW **with a
cost attached**.

**wrong_if**: `metric=count_of_tier4_members_disclosing_a_gpu_asp_or_compute_hardware_cost_share threshold=0 source=10-Q_or_10-K_segment_note_and_supply_chain_disclosure op=>`

**Subscribed**: `NVDA × supply-chain`, `NVDA × unit-economics`, `NVDA × secular-trends`, `GOOG × supply-chain`, `NVDA × what-if`

---

### Pillar 5 — Orbital compute is a P10 watch item, not a thesis: zero named operators meet all five conditions (Priority: P5)

**Claim.** The count of named orbital-compute operators meeting **all five** P10 conditions
is **zero**. P10's five, verbatim — (1) revenue or offtake; (2) **radiator derivation**, with
explicit mass and area against F2 at a stated rejection temperature; (3) **array derivation**,
~5,000–5,600 m² per MW; (4) **launch cost** tested against the F5a propellant floor
(**~$46/kg**) and F5b if partially reusable; (5) **radiation**, TID + SEU — are assessed per
operator, and the verdict is the constitution's own: *"Absent all five, orbital compute is a
**watch item, not a thesis**."* **009 does not underwrite it and does not own its framing**
(§1a).

**Note on condition (2) after §0.1**: with F2 downgraded to a qualitative bound, condition
(2) **cannot be satisfied by any operator** — an operator cannot state mass and area "against
F2" when F2 has no point value. **The gate is now unclosable in principle, not merely
unmet.** That is a finding, and it is recorded as one.

**Consumes**: `GOOG × risk`, `SPCX × business-model`, `GOOG × secular-trends`, `NVDA × risk`

**Why P5**: it is the pillar that keeps the thesis honest about its own boundary. Without it,
P1–P4 could be read as building toward an orbital-compute position.

**Independently falsifiable**: a named operator satisfying all five — most likely entry
point is condition (1), a signed offtake with a disclosed price.

**wrong_if**: `metric=count_of_named_orbital_compute_operators_meeting_all_five_p10_conditions threshold=0 source=operator_disclosure_of_revenue_radiator_derivation_array_derivation_launch_cost_and_radiation_assumptions op=>`

**Subscribed**: `GOOG × risk`, `NVDA × risk`, `GOOG × secular-trends`, `GOOG × comps`, `NVDA × comps`, `GOOG × reverse-dcf`, `NVDA × reverse-dcf`

---

## 2. Universe Definition

**Membership test, applied as written** (constitution v1.6.0 §Universe Definition):

> *does the issuer's **primary revenue** come from this function? Membership is settled by
> **revenue composition**, not by market cap, index membership, or thematic resemblance.*

Tier 4's function: **selling power, thermal management or compute capacity, where the orbital
case is a stated demand path.**

### 2a. Universe members — 4 names

| Ticker | Company | Sector | Weight | Function that admits it — and its stated orbital path |
|---|---|---|---|---|
| NVDA | NVIDIA | tech.semiconductors | equal | **Compute silicon.** Primary revenue is the compute-capacity-enabling part. Stated orbital path: H100 flew on Starcloud-1 (and failed on thermal — §0 row 2). ⚠️ **Its *stated* orbital thesis is imaging/inference edge data reduction, NOT megawatt compute** (§0.3) — a narrower path than this tier's narrative assumes. **READY** — 169 filings |
| GOOG | Alphabet | tech.platform_internet | equal | **Sells compute capacity** (Google Cloud). Stated orbital path: **Project Suncatcher**, 81-satellite reference config — `CLAIMED` throughout, no flight, no prototype, no filing. **READY** — 146 filings. ⚠️ **Query as `GOOG`, never `GOOGL`** |
| MSFT | Microsoft | tech.platform_internet | equal | **Sells compute capacity** (Azure). Stated orbital path: Azure Space. **READY** — 52 filings |
| AMZN | Amazon | *(PARTIAL — unassigned)* | equal | **Sells compute capacity** (AWS). Stated orbital path: **Amazon Leo** (~180–200 sats, 3,200 by 2029, ~$17B committed); acquiring Globalstar. **PARTIAL** — `sector` null. ⚠️ **Manual assignment is a precondition, not an assumption.** No 001 artifact exists for AMZN (§6 K-2) |

*Weights are `equal` and carry no sizing meaning — 011 sizes. Every name here is a
**candidate for a positioning grade**, and a grade is not a weight.*

### 2b. Comparator / reference — **NOT a universe member**

**This section exists because the constitution put VRT here at v1.6.0.** The re-cut states:
*"**VRT MOVED OUT OF MEMBERSHIP.** … a thesis cannot hold its subject and its control.
Thesis 009's own §3 said so while listing it as a member."* VRT is cited below **for two
quantities only**, and receives **no `artifacts/{ticker}/` directory** in this thesis.

| Ticker | Company | What it is cited for — and why it cannot be a member |
|---|---|---|
| VRT | Vertiv | **The orbital cooling penalty's terrestrial reference, and the terrestrial cost floor.** It fails the membership test twice over: it sells **equipment to** colocation operators — a *supplier price, never a rental price* — so its revenue is not power or compute capacity sold; and its orbital case is **not stated** by the issuer. ⚠️ **It supplies a bound and a direction, never a level** (§0.2). `PUE` returns zero hits in its 10-Q. **Do not trade it, do not size it, do not let it enter a universe aggregate.** |

**Retained for exactly two uses:** (i) the **cooling penalty** — the terrestrial cost the
orbital case must undercut, carried as the four bounds α/β/γ/δ with no level; (ii) the
**terrestrial cost floor's direction** — a scaling cost curve, not a rent (§0.2), which is
the adversarial input this thesis is required to carry.

### 2c. Removed from the stub's universe — stated, not silently dropped

The stub listed **9 names**. Five are removed. Each removal is a membership-test failure, and
each is stated with where the name belongs instead.

| Ticker | Removed because | Where it belongs |
|---|---|---|
| **VRT** | **Comparator, by constitution v1.6.0** — see §2b | §2b of this spec. Also 002 (unit-economics) and 004 (read-through) |
| **AAPL** | **Fails the function test.** Primary revenue is consumer devices. It does not *sell* power, thermal or compute capacity. Its Globalstar position (~20% of the company, rights to **85% of network capacity**) is a **capacity purchase** — it is a *buyer* of space services, and space is not its business. Under the universe definition that is the **demand side**, not Tier 4 | **006** (Tier 2 — connectivity and spectrum): the D2D anchor-demand read. Cited by 009 only as a demand read-through, never weighted |
| **TMUS** | **Fails the function test.** Primary revenue is mobile service; it buys D2D capacity from Starlink. Space is not its business. **`NOT_READY` in any case** — no data | **006**, alongside AAPL. The "telecom" industry the v1.6.0 re-cut names as one of the five that made Tier 4 a theme |
| **AMPX** | **Fails the function test.** High-specific-energy cells are **battery storage** — not power *sold*, not thermal management, not compute capacity. The re-cut names **"batteries"** among the industries that made Tier 4 a theme. **`NOT_READY` — no data** | Not in any wave-1/2 thesis. Recorded as a **coverage gap**: silicon-anode cells have space/HAPS heritage but no issuer disclosure to research. The "power beneath the power" question is **Tier 3's** (BWXT is the constitution's named path to raising F2's rejection temperature) |
| **ENS** | Same as AMPX — battery **systems**, including space-qualified cells. **`NOT_READY` — no data.** ⚠️ **ENS carries a fund-sourced case in the corpus** (Brown Advisory, Sustainable Small Cap Core) **with no issuer coverage** — the same asymmetry the programme recorded for MOG-A | Same as AMPX. **The corpus case is recorded here so it is not lost**; it is not a membership claim |

**What this leaves, and why it is coherent.** Four names, one function: selling compute
capacity, plus the silicon that capacity is built from. **The tier stops spanning five
industries and starts spanning one.** The two `NOT_READY` removals (AMPX, ENS) remove the
batteries leg entirely — and that leg was unresearched, so nothing is lost from the evidence
base; what is lost is a *claim of coverage* that did not exist. **The removals are recorded
in the status log, not deleted.**

⚠️ **Residual divergence, flagged not hidden.** The constitution's Tier 4 *table* still
carries rows for AAPL, AMPX, ENS and TMUS. This spec applies the membership *test*, which
v1.6.0 declares authoritative — *"Membership is settled by revenue composition"* — and the
test does not admit them. **The divergence is registered as a known-open for the next
amendment (see §6, K-1).** It is not resolved unilaterally here, and it does not block
activation: the four admitted members are unaffected either way.

---

## 3. Skill Deployment Matrix

**`tasks_md.py` parses §3a only.** §3b is deliberately a different column shape so it parses
as prose — **the mechanism that makes "consumed" mean consumed** (004's convention).

### 3a. Executed

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|---|---|---|---|
| secular-trends | business-intelligence | Deep | GOOG, MSFT, AMZN, NVDA | none | **The orbital demand path per member** — is it stated, by whom, with what specificity. The primary instrument for **P1**, **P2**, **P5** |
| business-model | business-intelligence | Deep | GOOG, MSFT, AMZN, NVDA, VRT | none | **Segment boundaries (DA-21)** and the revenue disaggregation table — where an orbital line would appear if one existed. Gates **P1**; the VRT run serves **P3** (comparator only) |
| recent-quarter | business-intelligence | Standard | GOOG, MSFT, AMZN | none | The quarterly series behind P1's zero, and the entity boundaries that make it a *measured* zero rather than a settled one |
| unit-economics | business-intelligence | Deep | VRT, NVDA | none | **Comparator only.** The four bounds (no level) and the margin-mix decomposition that breaks the scarcity reading (**P3**) |
| supply-chain | business-intelligence | Standard | NVDA, GOOG | none | The power/thermal content per MW, and the **GPU-cost-term** question that P4 records as unmodellable |
| ratio-analysis | quantitative-analysis | Standard | GOOG, MSFT, AMZN, NVDA, VRT | **`late`** | Capex intensity γ, margin structure β, and the **price-stamped** ratios. Registry-`late`; feeds **P3**, **P4** |
| peer-bench | quantitative-analysis | Standard | GOOG, MSFT, AMZN, NVDA | none | The cross-member rank and the comparator's position in it — the DA-21 boundaries made explicit (**P1**, **P3**) |
| comps | models-and-pitches | Light | GOOG, MSFT, AMZN, NVDA | **`late`** | **The pricing limb of §1**: how much of the positioning is already in the multiple. **P6's cross-check only** — no implied value |
| reverse-dcf | quantitative-analysis | Standard | GOOG, MSFT, AMZN, NVDA | **`late`** | **The price question asked backwards** — what growth the live quote implies, and whether *any* orbital contribution is required to justify it. The strongest available form of "already priced" (**P1**, **P2**) |
| what-if | decision-analysis | Light | NVDA, GOOG | none | **The cost-stack counterfactual**: at which corner, if any, does power+thermal *stop* being decisive? The instrument that keeps §0.3's "46% at $10M/MW" from being read as corner-independent (**P4**) |
| risk | risk-management | Light | NVDA, GOOG | none | **Per-operator P10 audit** (the five conditions, §0.1's unclosability note) and the disclosure-suppression risk in P2 (**P5**) |

### 3b. Consumed — not executed here

| Consumed from | What | Why this thesis does not run it |
|---|---|---|
| **002** F2 validation (`GOOG × secular-trends`, `f2-constant-sourcing`) | The qualitative bound: order 10³ m² and 10¹ t per MW; the ~16× and 1.587× corrections | Q-A is 002's (§1c). **009 may not cite F2 to a point value** (§0.1) |
| **002** VRT unit-economics | The four bounds and the mix-decomposition finding | Q-B is 002's. 009 consumes the conclusion and re-runs only the *period-over-period* test in P3 |
| **003** value-pool map and curve matrix | The disposition that orbital compute is a watch item, not a pool | §1a. **003 governs the framing** |
| **004** anchor SOTP and segment attribution ledger | The AI-segment framing and the terrestrial comparator's role | Q-B's second half. 009 does not value SPCX |
| **006** D2D demand work | AAPL/TMUS demand-side reads | §2c. Those names are 006's |
| **010** | The "immaterial-to-the-counterparty" pattern's second instance | Shared methodology, not shared universe |

---

## 4. Dependencies

- **002** — owns F2's physics validation and the VRT unit-economics; **the three §0.1–§0.3
  notifications are its output and are consumed, not re-derived.** 002 is COMPLETE.
- **003** — **owns the framing (§1a).** 009 consumes the watch-item disposition and builds
  the positioning question underneath it.
- **004** — owns the AI-segment framing and the terrestrial comparator's valuation role.
  Consumed via the read-through set; **MSFT/GOOG/NVDA carry no weight in 004's universe and
  carry full weight in 009's.**
- **006** — Tier 2. **Receives AAPL and TMUS from this re-scope (§2c)** along with the
  D2D demand-side question (Q-C).
- **010** — the microgravity demand side shares the "immaterial-to-counterparty" pattern
  (**P2** here, its P1 there). Cross-reference, not shared universe.
- **011** — sizing. 009 produces grades, not positions.

---

## 5. Market data

**Stage: `per_row` — declared, where the stub declared nothing.**

The stub's research question has two limbs: *which issuers are positioned*, and *how much of
that is already priced*. **The second limb is unanswerable without a quote**, and a stage
must be declared for the thesis that asks it. 005's parallel spec declares `none` across its
cohort; **009 is not 005 and must not inherit that declaration by adjacency.**

- **`late`** — `ratio-analysis`, `comps`, `reverse-dcf` (the three registry-`late` skills),
  applied to the four members and the comparator.
- **`none`** — every other executed row.

**The feed is live and keyless.** `data-tools/market_data.py`, source `nasdaq`; verified in
004 round 3 (SPCX `$152.71`, close 2026-09-18). **Every price entering this thesis is
datable and must be quoted with its date** — the same discipline 004's V-6 imposed.

⚠️ **DA-30 applies.** Where a price figure is carried from a dated print rather than the live
quote, **the basis travels with it**: a print and a live quote are two bases on one concept
and are never collapsed into one unnamed number.

---

## 6. Known-open at re-scope

| # | Item | Disposition |
|---|---|---|
| **K-1** | **Constitution Tier 4 table still lists AAPL, AMPX, ENS, TMUS**, which §2c removes on the membership test | **Flagged, not resolved.** Register for the next amendment. Does not block activation — the four admitted members are unaffected |
| **K-2** | **No 001 artifact exists for AMZN, AAPL or LLY-class names.** 001's artifact set covers GOOG, MSFT, NVDA, VRT — **not AMZN** | AMZN is a member with **no inherited evidence**. `business-model` and `secular-trends` run on it fresh; its `PARTIAL` sector assignment precedes any aggregate |
| **K-3** | **NVDA's stated orbital thesis is imaging/inference, not megawatt compute** (§0.3) | Carried as a scope limit on **P1/P5**, not a defect. If the tier's compute narrative is read as megawatt-scale, NVDA's *stated* path does not support it |
| **K-4** | **P10 condition (2) is unclosable while F2 has no point value** (P5) | Registered as a finding. `risk` records it per operator |
| **K-5** | **ENS's fund-sourced corpus case with no issuer coverage** | Recorded in §2c so it is not lost. Not a membership claim |
