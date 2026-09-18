# Research Thesis: 003 — Launch Cost Curve & Value Migration

**Constitution Ref**: constitution.md v1.4.0 (`constitution_pin: 1.4.0`)
**Created**: 2026-09-18
**Status**: Active · **Wave 2** (moved from wave 1 at clarify round 2, 2026-09-18 —
001 already settled the cost curve's *level* and that value left launch; 003 is refinement)
**板块**: Foundation · **Wave**: 1
**Binding constraint (P3)**: `MASS_LAUNCH_COST`
**Time Horizon**: 2026-Q4, terminating at the wave-1 hand-off to 004–006
**Depends on**: `001-technology-baseline` (pin 1.2.0 — the baseline this thesis inherits);
`002-evidence-validation` (payload denominators and F2 physics — **consumed, never
re-derived here**)
**Produces**: no trade ideas. Produces the **sector cost curve** (vehicle × architecture ×
DA-01 basis, with the correct F5 floor per architecture) and the **value-pool map**. Tier 0
and Tier 1 both price off these.

---

## 0. Inherited baseline — what this thesis does NOT re-derive

001 built unit economics for **exactly three issuers**. It established the *level* of
cost, the *existence* of the floor, and that PIL-1 holds. This thesis takes all of it as
given and cites the artifact rather than repeating the work.

| Inherited result | 001 artifact | Grade |
|---|---|---|
| RKLB basis B = **$14,667/kg**; basis A = **$30,333/kg** (Electron, 300 kg to LEO) | `RKLB/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` |
| RKLB is the **only** issuer disclosing `cost per launch` / `revenue per launch`; SPCX and FLY disclose neither | `RKLB/…_unit-economics_methodology.md`; `FLY/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` |
| Electron is **10.3× Falcon 9 per kg on basis A** — the small-lift penalty, quantified from filed data | `RKLB/…_unit-economics_methodology.md` | `DEMONSTRATED` |
| The four DA-01 bases span **~$500/kg to ~$6,600/kg** — a **7–13× spread around one Falcon 9 mission** | `SPCX/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` (A′/C figures) · `MODELED` (B) |
| F5a (fully reusable, propellant ~**$4.6–9.2M/flight**, floor ~**$46–92/kg** at 100 t) vs F5b (partially reusable, propellant only **~2–3%** of a **$12–20M** marginal cost; the expended second stage at **~$8–12M** dominates) | `SPCX/…_unit-economics_methodology.md`; constitution §F5a/§F5b | `MODELED` |
| A1b **falsified**: SPCX revenue **+91.9%** with Falcon launches **−18%** and Space only **+29%**; RKLB **+62%** with launch revenue **−$2.1M**; FLY **+657%** *"driven by Spacecraft Solutions growth"* | `SPCX/2026-09-18_1239_operational-kpi_methodology.md`; `RKLB/…`; `FLY/…` | `DEMONSTRATED` |
| DA-25: disclosed `revenue per launch` implies **51.6%** launch gross margin; the audited segment table implies **42.9%** | `RKLB/…_unit-economics_methodology.md` | `DEMONSTRATED` (figures) |
| RKLB build-vs-launch: 2024 **14 built/16 launched**; 2025 **24/21**; H1 2026 **11/12** — inventory drawn down in 2 of 3 periods | `RKLB/…_unit-economics_methodology.md` | `DEMONSTRATED` |
| SPCX Space carries a **65.8% gross margin** with cost of revenue **flat (−0.3%)** while revenue rose 29.0%; the segment loss is **Starship R&D $1,076M** (111.9% of segment revenue) | `SPCX/…_operational-kpi_methodology.md` | `DEMONSTRATED` |
| Space-grade solar cells are a **two-supplier duopoly** (RKLB/SolAero · BA/Spectrolab), structurally unpriced | `_cross/technology-baseline_synthesis.md` | `DEMONSTRATED` |
| DA-23/DA-24/DA-25 registered; the **component identity** (`gross profit − opex = operating_income`) is the only robust sign discriminator; `EPS × shares` is **not** admissible | constitution §Data-Integrity Register | `DEMONSTRATED` |

**What 001 did not do:** 001 never built the *curve*. It measured one point (Electron), one
mission (Falcon 9), and three issuers. It did not place those points on a
vehicle-by-architecture axis, did not explain *where the value went* once A1b fell, and
never asked whether RKLB's per-launch disclosure is comparable to anything else. That is
this thesis's entire scope.

> **Path correction on inheritance.** `001/thesis.md` cites the Phase 1 cross artifact as
> `_cross/phase-1-launch-cost-baseline.md`. **No such file exists** — the Phase 1 baseline
> lives at `SPCX/2026-09-18_1239_unit-economics_methodology.md`. The real path governs;
> the synthesised path is recorded here rather than silently followed.

### Validation queue — the `CLAIMED`/`MODELED` figures this thesis must convert

Per PROGRAM.md §0, under **P4** a `MODELED` input can never satisfy a falsifier, so an
unconverted figure is a pillar that cannot fire. **002 owns the physics and the payload
denominators; 003 owns the curve.** The split is explicit below so neither thesis
duplicates the other.

| Figure inherited from 001 | Grade at inheritance | Owner | What converts it |
|---|---|---|---|
| Electron payload **300 kg** to LEO — the divisor of *every* Electron $/kg | `CLAIMED` | **002** | Government manifest, filed document or customer contract. 003 consumes 002's result and states its band; it does **not** re-derive it |
| Falcon 9 payload **22.8 t**; Starship **100 t** | `CLAIMED` | **002** | Same admissibility rule |
| Falcon 9 basis B components (propellant ~$0.36M, expended stage ~$8–12M, range $2–5M, refurb $1–3M) | `MODELED` | **003** | A filed or contract-sourced anchor. 001 itself names the candidate: NASA CRS/Commercial Crew contract values as a revealed-price floor |
| Falcon 9 basis A **$2,939/kg** (published list price) | `CLAIMED` | **003** | A filed contract value or a customer filing. **Load-bearing**: it is P4's threshold |
| F5a/F5b inputs — propellant **mass** (Starship ~4,600 t; Falcon 9 ~485 t) and **price** ($1–2/kg; ~$0.75/kg) | `CLAIMED` (mass) / market price (price) | **003** | An operator disclosure, a range-safety or environmental filing, or a published propellant market series |
| Falcon 9 basis C **$6,596/kg** — Space segment cost ÷ customer launches | `DEMONSTRATED` (figures) / `MODELED` (the division) | **003** | A DA-21 restatement isolating launch services from 14-year development contracts |
| Electron basis B **$14,667/kg** — the universe's only demonstrated marginal cost | `DEMONSTRATED` | **003** | Extend it: is it durable quarter-over-quarter, and does it *decline*? (P3, P5) |
| DA-25's **51.6% vs 42.9%** gross-margin gap | `DEMONSTRATED` (figures) | **003** | Repeat the reconciliation each quarter; test whether the gap is definitional or a recognition-timing artefact (P5) |
| Neutron's payload to LEO | **absent from 001 entirely** | **003** | A filed source or published vehicle spec; the arithmetic in P4 turns on it |
| F2's unsourced constants; SPCX's 1.4 GW nameplate | `MODELED` / `CLAIMED` | **002** | Out of scope here. 003 maps the value pool **without** valuing any constellation (P10) |

**Residue policy.** A figure 003 cannot convert is recorded with the specific source class
that would settle it — `UNRESOLVABLE-FROM-PUBLIC-SOURCES` or `UNRESOLVABLE-FROM-PLATFORM`
— and the curve is reported with a **widened band** rather than retained precision.

---

## 1. Research Question

**With F5a/F5b now separated and A1b falsified, where does value accrue as $/kg falls — and
what does the cost curve actually look like across every vehicle and architecture?**

The premise is uncomfortable in a specific way. The sector's cost narrative is a *curve* —
a monotone decline from $/kg today toward $/kg someday — and the workspace has a *point*.
Exactly **one** vehicle-and-issuer pair in the universe has a `DEMONSTRATED` marginal cost
per launch, and it is the *worst* one on the curve: Electron at $14,667/kg on basis B,
**10.3×** Falcon 9 per kg. Everything else that is called a cost curve is an issuer
assertion about a vehicle that has not flown at cadence, priced against a payload mass
nobody filed. **The gap between the claimed curve and the demonstrated point is itself the
finding**, and no thesis in this program has yet measured it.

The second half of the question is the constructive reading of A1b's falsification. Three
independent issuers grew revenue from non-launch business, and in two of three launch
revenue *declined*. A1b's fall is therefore not "value went nowhere" — it is a relocation,
and the destination has never been mapped. **The value-pool map is the deliverable that
makes A1b's falsification usable rather than merely recorded.**

This thesis produces no position and no valuation. Its output is the curve plus the map.

### Why this thesis exists at all

The alternative was to let 004–006 each build their own comparator. That would propagate
three specific errors downstream:

1. **A misapplied floor becomes a valuation input.** F5a's $46–92/kg propellant floor and
   F5b's upper-stage manufacturing floor differ by an order of magnitude, and the
   constitution names floors for only **two** of the three reuse architectures actually
   present in this universe. A thesis that applies F5a to a Falcon-class vehicle
   understates achievable price by an order of magnitude; a thesis that applies F5b to
   Starship overstates it. **This is the named failure mode and P1 exists to prevent it.**
2. **A claimed curve becomes a factual curve.** Every "$/kg by 2030" figure in the sector
   is `CLAIMED`. Without a register separating demonstrated from claimed, a downstream
   model cannot tell a measurement from a roadmap — and the two differ by roughly an order
   of magnitude today.
3. **A falsified axiom becomes an unframed assumption.** A1b is dead, but "value accrues to
   the launcher" is the default framing of every launch thesis. Under the constitution, any
   thesis assuming it without testing is `UNFRAMED_REFERENCE`. **003 is where the test
   lives**, so 005 does not have to repeat it five times.

---

## 1b. Pillars

### Pillar 1 — The complete cost curve: every vehicle × every reuse architecture × all three DA-01 bases, each with the floor its architecture actually implies (Priority: P1) 🎯 Minimum Defensible View

001 produced a four-row cost comparison centred on one Falcon 9 mission. This pillar
produces the **matrix**: vehicle × architecture × basis, populated or explicitly recorded as
absent, with the correct binding floor named for each architecture.

The architecture axis is **three-valued**, and the constitution currently names floors for
only two of them — which is the first substantive finding this pillar expects to produce:

| Architecture | Vehicles in this universe | Binding marginal-cost term | Constitution floor |
|---|---|---|---|
| **Fully reusable** | Starship (SPCX) | Propellant — nothing else consumed | **F5a** — hard, ~$46–92/kg at 100 t |
| **Partially reusable** | Falcon 9 (SPCX); Neutron (RKLB, forward) | The **expended upper stage** (~$8–12M) | **F5b** — soft, a manufacturing curve |
| **Fully expendable** | **Electron (RKLB), Alpha (FLY)** | The **entire vehicle** — no stage is recovered | **none named.** The two vehicles for which the universe has *any* demonstrated data sit on the architecture F5 does not cover |

**The claim:** all three DA-01 bases can be stated for every vehicle in the universe, the
floor applied to each is the one its architecture implies, and **no vehicle shows a
demonstrated $/kg below its own architecture-applied floor**. Where a basis or a
denominator does not exist, the cell is recorded as absent with the named source that would
fill it — not estimated. The spread across bases for a single vehicle is reported as the
finding, per the §1c standing rule.

**Why this priority**: it is the Minimum Defensible View because every other pillar and
every downstream thesis reads its numbers off this matrix. It is also the only pillar whose
failure mode — a floor applied to the wrong architecture — silently corrupts a valuation
rather than merely being wrong.

**Independently falsifiable**: any vehicle in the universe whose demonstrated $/kg to LEO
falls below the floor its own disclosed cost stack implies, or any architecture cell for
which no basis can be stated and no resolving source named.

**wrong_if**: `metric=count_of_universe_vehicles_with_a_demonstrated_price_per_kg_to_LEO_below_their_architecture_applied_launch_cost_floor threshold=0 source=issuer_filing_or_audited_segment_table op=>`

**Subscribed**: `SPCX × unit-economics`, `RKLB × unit-economics`, `SPCX × operational-kpi`, `RKLB × operational-kpi`, `RKLB × peer-bench`, `FLY × competitive`, `RKLB × what-if`

---

### Pillar 2 — The value pool migrated to the integrator that owns the demand, not to the launcher and not to the independent operator (Priority: P2)

A1b's falsification is recorded but unexplained. This pillar maps where the growth actually
went, across the nine-name universe, on the issuer's own segment boundaries (**DA-21**) —
and reports the spread between those boundaries and a normative restatement.

The three available destinations are distinguishable by margin, and the ordering is not the
one the narrative implies:

| Position | Evidence in this universe | Operating result |
|---|---|---|
| **Launch** | SPCX Space 12.3% of revenue, **−1.9% across H1**; RKLB launch revenue **−$2.1M**; FLY launch *"not the driver"* | SPCX Space **$(542)M** on $962M |
| **Captive services, inside the launcher** | SPCX Connectivity **$4,291M** at a **+38.6%** operating margin, income from operations **+79.4%** | The only segment in the universe with demonstrated operating leverage |
| **Independent operators** | IRDM **15.1%** operating margin (down from 23.2%), GSAT **7.4%** with revenue **−3.5%**, SATS **10.7%** | The thinnest operator cohort in the universe |

**The claim:** value migrated to the segment **adjacent to a launcher's own internal
demand** — the captive service built on the launcher's own launched capacity — and **not**
to independent constellation operators, whose margins are thinner than the launchers' and
in two cases deteriorating. Stated as a mechanism: SPCX Connectivity exists because SPCX
owns Starlink, and the sector's merger wave (RKLB→IRDM, AMZN→GSAT) is the attempt by
non-SPCX actors to *acquire* the demand they cannot generate internally. **That is A5's
mechanism, and this pillar is where it gets a number.**

**Why this priority**: P2 rather than P1 because it is the thesis's reason for existing —
003 is chartered to answer "where does value accrue", and this is that answer. It is P2
rather than P1 only because P1's matrix is the input it reads.

**Reachability caveat (P10).** This pillar maps the value pool. It does **not** value any
constellation, and it does not treat orbital compute as a destination: no listed issuer
reports orbital-compute revenue, so it is not a pool, it is a watch item.

**Independently falsifiable**: any issuer in the universe where a *launch* segment's
operating margin exceeds its non-launch segment's, or where an independent operator's
margin exceeds the launcher's captive-services margin.

**wrong_if**: `metric=count_of_universe_issuers_where_launch_segment_operating_margin_exceeds_non_launch_segment_operating_margin threshold=0 source=issuer_segment_disclosure op=>`

**Subscribed**: `SPCX × business-model`, `RKLB × business-model`, `SPCX × sector-overview`, `RKLB × sector-overview`, `SPCX × secular-trends`, `IRDM × competitive`, `GSAT × competitive`, `RKLB × supply-chain`

---

### Pillar 3 — The curve is `CLAIMED`, not `DEMONSTRATED`: exactly one vehicle has a measurable cost series, and its single observed step may be a definitional artefact (Priority: P3)

The sector describes a monotone decline in $/kg. This pillar separates every cost-reduction
claim in the universe into `DEMONSTRATED` (filed, flown, or audited) and `CLAIMED`
(roadmap, press, or target), and reports the ratio. The expected shape of the register:

| Claim class | Vehicles | Evidence |
|---|---|---|
| **Demonstrated cost series** | Electron only | `cost per launch`: **$4.4M** (Q2 2026) against **$4.9M** (H1 2026) — which, if H1 is the two-mission-quarter mean, implies **~$5.4M** in Q1 2026 |
| **Demonstrated price series** | Electron only | `revenue per launch`: **$9.1M** (Q2) against **$9.2M** (H1) — implying **~$9.3M** in Q1 2026 |
| **Claimed reductions** | Starship, Neutron, Alpha Block II, Falcon 9 refurbishment curve | Roadmaps and published targets. `CLAIMED` under P4 until flown at cadence with a disclosed cost |

**The claim:** the demonstrated share of the sector's cost-curve claims is **under half** —
the curve as commonly drawn is a projection, and the single measured step (Electron, one
quarter, ~18% cost decline against a ~2% price decline) is (a) two periods, not a curve,
and (b) **not yet separable from a mission-mix effect or from DA-25's normalisation**. The
gap between the claimed curve and the demonstrated point is reported as the finding.

**Why this priority**: it is what stops a downstream model from discounting a roadmap as
though it were a measurement. It is P3 rather than P2 because P2's map is the more
valuable output; it is above P4/P5 because those two pillars consume its register.

**Independently falsifiable**: a majority of the universe's announced $/kg improvements
carrying a filed or flown basis rather than a roadmap basis.

**wrong_if**: `metric=share_of_universe_cost_reduction_claims_with_a_filed_flown_or_audited_basis threshold=0.5 source=issuer_filing_or_audited_segment_table op=<`

**Subscribed**: `RKLB × operational-kpi`, `SPCX × operational-kpi`, `RKLB × unit-economics`, `SPCX × peer-bench`, `FLY × competitive`, `YSS × ratio-analysis`

---

### Pillar 4 — Neutron's medium-lift case closes arithmetically only above a stated payload bar, and it rests on F5b, not F5a (Priority: P4)

The 10.3× small-lift penalty is the entire quantitative case for medium lift, and 001
stated it cleanly: *the same launch price ($9.1M) on a medium-lift vehicle's payload would
put RKLB at roughly Falcon-9 parity per kilogram.* This pillar tests whether that sentence
survives contact with arithmetic and with the architecture axis.

The test is derivable today, because the threshold is already in evidence: parity against
Falcon 9 **basis A** (`CLAIMED` at $2,939/kg) at RKLB's disclosed price per launch of
$9.1M requires a payload of **≥ ~3.1 t to LEO**. Below that bar the case does not close at
the current price; above it, it does — and only then does the medium-lift argument become
an economic claim rather than a capacity claim. **Neutron's actual payload figure is not in
any 001 artifact** and must be sourced; until it is, the P4 conclusion is conditional on a
`CLAIMED` input and that conditionality must be stated, not smoothed.

**The architecture check is the second half.** Neutron is designed as a partially reusable
vehicle — a recovered booster with an expended upper stage — so **F5b applies and F5a does
not**. Any Neutron $/kg figure compared against the F5a propellant floor is a category
error, and the correct comparator is a *manufacturing* cost curve on the upper stage,
which yields to production learning.

**Why this priority**: P4 because it is forward-looking and rests on a `CLAIMED`
denominator; under P4 an unvalidated input cannot carry a falsifier, so this pillar is
sized as conditional from the start rather than promoted on optimism. It is above P5
because 004 and 005 both need it.

**Independently falsifiable**: an implied Neutron $/kg at the disclosed price that exceeds
Falcon 9's basis-A figure — the case simply does not close — or a sourced payload that puts
Neutron on the F5a architecture rather than F5b.

**wrong_if**: `metric=implied_neutron_price_per_kg_to_LEO_at_disclosed_revenue_per_launch threshold=2939 source=RKLB_filing_and_published_vehicle_spec op=>`

**Subscribed**: `RKLB × what-if`, `RKLB × unit-economics`, `FLY × competitive`, `RKLB × peer-bench`, `SPCX × unit-economics`

---

### Pillar 5 — RKLB's per-launch disclosure is a durable *cost-side measurement* and an unreconciled *revenue-side normalisation*; the asymmetry is the finding (Priority: P5)

RKLB's disclosure is the universe's only per-launch figure of either kind, which makes its
integrity load-bearing for every $/kg conclusion in the workspace. 001 checked it once
against the audited Launch Services segment table and found the **cost** side consistent
within **3.6%**. The **revenue** side does not reconcile at all.

The arithmetic is derivable from the figures already in the 001 artifact:

```
  Q2 2026, 6 Electron missions
    cost side     $4.4M × 6 = $26,400k   vs segment cost of revenue  $25,476k   →  3.6% gap
    revenue side  $9.1M × 6 = $54,600k   vs segment revenue          $44,586k   → 22.5% gap
```

**The claim:** the disclosure is a **measurement on the cost side and a normalisation on the
revenue side** — exactly the DA-25 mechanism, now quantified at 22.5% rather than described
as an 8.7-point margin difference. Whether that gap is **structural** (the issuer's stated
"regardless of recognition method" definition, which would persist) or **transient** (the two
Q2 HASTE missions recognised over time, with revenue partly taken in prior quarters, which
would reverse) is decidable: the derived Q1 2026 implied launch gross margin of **~41.9%**
sits almost exactly on the segment table's **42.9%**, while the disclosed Q2 figure of
**51.6%** is the outlier — which fits the timing explanation. **Timing is the better
hypothesis; this pillar requires it be tested rather than assumed.**

**Why this priority**: P5 because it is meta-evidence about the curve's best data point
rather than a curve conclusion itself — but it is load-bearing, because P6 reads the same
two numbers and P1's only `DEMONSTRATED` marginal cost comes from this metric.

**Note the discarded test.** `EPS × shares` is **not** admissible as a sign or
consistency test anywhere in this thesis (constitution §Data-Integrity Register); it passes
spuriously on flipped issuers at RKLB, FLY and VOYG. Per-launch reconciliation uses the
**component identity** against the audited segment table.

**Independently falsifiable**: a cost-side reconciliation gap above 5% in any quarter, a
discontinuation of the metric, or a revenue-side gap that fails to close as the
over-time-recognised missions roll off — each of which would demote the disclosure from
measurement to convention.

**wrong_if**: `metric=abs_pct_gap_between_disclosed_cost_per_launch_times_missions_and_audited_launch_segment_cost_of_revenue threshold=0.05 source=RKLB_10-Q_launch_services_segment_table op=>`

**Subscribed**: `RKLB × operational-kpi`, `RKLB × recent-quarter`, `RKLB × ratio-analysis`, `FLY × competitive`, `SPCX × recent-quarter`, `IRDM × recent-quarter`, `GSAT × recent-quarter`, `PL × recent-quarter`, `YSS × recent-quarter`, `LUNR × recent-quarter`, `SATS × recent-quarter`

---

### Pillar 6 — The released value was captured at the launcher, not passed through to the customer, and the demand side does not price off the curve (Priority: P6)

A1a holds: launch cost sets the floor under every downstream case. This pillar asks the
question A1a does not answer — **how much of that floor actually transmits to the customer,
and how much of the customer's cost stack it is.**

The first half is answerable from the same two filed numbers as P5. Over the one observed
interval, RKLB's cost per launch fell **~18%** (Q2 against the derived Q1) while its
revenue per launch fell **~2%**. **The released value was retained as margin, not passed
through as price.** That is a demonstrated finding about who captures a falling cost curve,
and it is the launcher-level counterpart to P2's segment-level map.

The second half is the demand-side test: for SATS, IRDM, GSAT, LUNR, PL and YSS, what
share of the relevant programme cost is launch, and is it material enough for the curve to
move their economics? If launch is a single-digit share of a constellation's cost stack,
then a 2× fall in $/kg moves the customer by a few percent — which is **why** value
migrated away from launch even though A1a holds. That reconciliation, if it survives, is
this thesis's unifying statement.

**Why this priority**: last because it is the only pillar whose demand-side half must be
`MODELED` from disclosed capex and disclosed launch prices rather than read directly, and
under P4 a modelled input cannot carry the falsifier alone. The cost/price half is
demonstrated and is delivered regardless.

**Independently falsifiable**: a demonstrated fall in `revenue per launch` at least as large
as the fall in `cost per launch` (pass-through occurred), or a launch share of programme
cost above 10% at the demand-side names (the curve does bind them).

**wrong_if**: `metric=launch_cost_share_of_total_program_cost_at_universe_demand_side_names threshold=0.10 source=issuer_filing_capex_and_launch_price_disclosure op=>`

**Subscribed**: `RKLB × operational-kpi`, `RKLB × unit-economics`, `PL × growth-strategy`, `YSS × growth-strategy`, `LUNR × growth-strategy`, `SATS × growth-strategy`, `PL × ratio-analysis`, `YSS × ratio-analysis`, `PL × sector-overview`, `YSS × sector-overview`, `IRDM × secular-trends`, `GSAT × secular-trends`, `IRDM × risk`, `GSAT × risk`, `RKLB × risk`

---

> **Delivering P1 alone yields a defensible partial conclusion** — a complete cost curve on
> all three bases with the correct floor named per architecture, and every gap recorded with
> its resolving source. That is the single most valuable output of this thesis, because 004
> and 005 cannot benchmark without it, and it is delivered first.

## 1c. Method — the curve instruments

Three capabilities are specific to this thesis and are not used elsewhere in the program.
They are why a curve thesis is a distinct workstream rather than a comparison pass.

1. **DA-01 A/B/C basis discipline.** Every $/kg figure is stated on **all three** bases —
   (A) customer list price, (B) marginal cost per launch, (C) fully-loaded amortized cost —
   labelled with the basis quoted, with the spread reported as the finding. Per the §1c
   standing rule inherited from 001 and restated in the constitution's Data-Integrity
   Register, **no basis is ever adopted as "the" answer**, and no pillar may be marked
   unresolved for being multi-definitional. A figure whose basis is unstated is treated as
   **unvalidated**, not as validated at face value. `DA-02` (which orbit) and `DA-06`
   (price vs cost) are applied on every line, and `DA-21` (issuer-defined segment
   boundaries) on every segment comparison.
2. **The F5a/F5b architecture test.** Before any floor is cited, the vehicle's architecture
   is named and the question "what is *expended* on each flight?" is answered. Fully
   reusable → F5a's propellant floor. Partially reusable → F5b's upper-stage manufacturing
   curve. **Fully expendable → neither, and the absence of a named floor is recorded as a
   finding**, not filled with the nearest available number. This is the instrument that
   prevents P1's named failure mode, and it is the reason P4 tests Neutron on F5b.
3. **`CLAIMED` / `DEMONSTRATED` curve separation.** Every cost-reduction claim is graded and
   the register reports the ratio. A target, a roadmap and a press figure are all `CLAIMED`
   under P4 and cannot satisfy a falsifier; a filed per-launch metric or an audited segment
   table is `DEMONSTRATED`. Where a value is arithmetic on demonstrated inputs but the
   division or the averaging assumption is ours, it is graded `DEMONSTRATED` (figures) /
   `MODELED` (the derivation) — 001's convention, carried forward unchanged.

**Evidence discipline.** Per P4 and the v1.3.0 register, any artifact reading
`operating_income` shows the component derivation in-line, and the **component identity** —
not `EPS × shares` — is the sign discriminator. DA-23's census is a **floor, not a census**:
001 confirmed 6 issuers and left the true scope unknown, so every issuer touched here is a
candidate.

**Correction policy.** Where this thesis invalidates a 001 figure, 001's files are **not**
rewritten. 001 is frozen; the correction is recorded here and cited by location, matching
001's own annotate-don't-rewrite policy.

## 2. Universe Definition

Deliberately narrow. Three core issuers supply the curve; six demand-side names price off
it. Weights are **analytical effort, not positions** — this thesis sizes no trades. The
57-name universe is not re-listed: a name enters 003 only if it contributes a point to the
curve or a position to the value-pool map.

| Ticker | Company | Sector | Weight | Why it is in this thesis (the point it contributes) |
|---|---|:---:|---|
| SPCX | SpaceX | industrial.aerospace_defense | 20% | **The curve's reference vehicle.** Falcon 9 (partially reusable), Starship (fully reusable) — two of the three architectures — plus mass to orbit, the three-segment structure that P2 reads, and the basis A/A′/B/C inputs |
| RKLB | Rocket Lab | industrial.aerospace_defense | 20% | **The curve's only measured point.** Electron basis A and B, the `cost per launch` / `revenue per launch` series (P3, P5, P6), the build-vs-launch cadence, the SolAero solar-cell leg, and Neutron (P4). A P11 deal security as acquirer |
| FLY | Firefly Aerospace | industrial.aerospace_defense | 10% | **The disclosure-uniqueness control.** Alpha is a second fully expendable vehicle; FLY discloses neither per-launch metric, which makes RKLB's disclosure a finding rather than a convention. Also an EGC — a structural explanation for thin disclosure |
| SATS | EchoStar | tech.telecom_services | 8% | **The counter-case to launcher capture**: value realised by selling the regulatory asset (~$27B of spectrum gains in 2025 H2 against $15.0B of revenue) rather than by operating. DA-24 contaminated — the asset-sale gain runs through `operating_income` |
| IRDM | Iridium Communications | tech.telecom_services | 8% | **The best-performing independent operator**, and the P2 test: 15.1% operating margin *falling* from 23.2% while revenue grew 3.8%. P11 deal security (RKLB) |
| GSAT | Globalstar | tech.telecom_services | 7% | **The purest monopsony in the universe** and its thinnest operator margin — 7.4%, on revenue that *declined* 3.5%. If value migrated to operators, it did not arrive here. P11 deal security (AMZN) |
| LUNR | Intuitive Machines | industrial.aerospace_defense | 7% | **Payload customer**: lunar services, launch as a cost input. DA-23 candidate — a 42.1% operating margin at Q4 2025 is not credible |
| PL | Planet Labs | industrial.aerospace_defense | 10% | **Payload customer with the universe's best gross margin (53.5%) that still loses 37% at the operating line** — the cleanest test of whether the curve's pass-through can reach a customer whose problem is fixed cost, not launch cost (P6) |
| YSS | York Space Systems | industrial.aerospace_defense | 10% | **Payload customer and manufacturer**: 24.0% gross margin against a 68.6% opex ratio, revenue **−20.5% QoQ** — a volume problem, not a unit-economics problem. The far end of the pass-through chain |

**Excluded by design.** The remaining names in the 57-name universe contribute no curve
point. Two exclusions are worth naming because they are *load-bearing absences* rather than
omissions: **BA** (Spectrolab) is the second leg of the space-solar-cell duopoly and is
**outside this universe** — 007/008 own it, and the map records the gap rather than
substituting a proxy; **BWXT** is F2's nuclear escape hatch and belongs to 002. Both are
cited as inherited context only.

**Coverage caveats carried in.** Per the constitution's audit: `IRDM`, `GSAT` and `RKLB` are
**P11 deal securities** — their operational metrics describe a standalone business
contractually ceasing to exist, and every figure drawn from them is tagged *pre-merger
basis*. `SATS` is DA-24 contaminated. `LUNR` is a DA-23 candidate. Sector values for `IRDM`
and `GSAT` follow the platform's assignment for `SATS` and are confirmed in-line at first
use, not assumed.

## 3. Skill Deployment Matrix

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|:---:|---|:---:|---|
| unit-economics | business-intelligence | Deep | SPCX, RKLB | none | Build DA-01 A/B/C for every vehicle; apply the F5 floor per architecture; source the basis-B cost stack (**P1**, **P4**) |
| operational-kpi | business-intelligence | Deep | RKLB, SPCX | none | The `cost per launch` / `revenue per launch` series and its reconciliation to the audited segment table (**P3**, **P5**, **P6**) |
| business-model | equity-research-core | Standard | SPCX, RKLB | none | Segment boundaries and the **DA-21** restatement before any segment comparison (**P2**) |
| what-if | business-intelligence | Standard | RKLB, SPCX, FLY | none | Neutron price/payload arithmetic and architecture substitution; the basis-mix sensitivity of P1's matrix (**P4**, **P1**) |
| recent-quarter | equity-research-core | Standard | SPCX, RKLB, FLY, SATS, IRDM, GSAT, LUNR, PL, YSS | none | The quarterly series every pillar reads; the **component identity** applied in-line on every issuer touched (**P5**, all) |
| ratio-analysis | quantitative-analysis | Standard | RKLB, SPCX, FLY, PL, YSS | none | The margin ladder, the per-launch margin reconciliation, and the demand-side programme-cost shares; catches DA-23/DA-24 residuals (**P2**, **P5**, **P6**) |
| peer-bench | industry-analysis | Standard | RKLB, FLY, SPCX | none | The cross-vehicle $/kg comparison table and the basis-spread report; the demonstrated-versus-claimed split across the vehicle set (**P1**, **P3**, **P4**) |
| competitive | equity-research-core | Standard | FLY, IRDM, GSAT | none | Whether RKLB's disclosure is unique; operator-versus-launcher margin positioning (**P3**, **P5**, **P2**) |
| secular-trends | equity-research-core | Standard | SPCX, IRDM, GSAT | none | Demand-side trajectory — is constellation cadence responding to the curve at all? (**P2**, **P6**) |
| sector-overview | industry-analysis | Standard | SPCX, RKLB, PL, YSS | none | The value-chain position map: which position in the stack holds the margin (**P2**, **P6**) |
| growth-strategy | equity-research-core | Light | LUNR, PL, YSS, SATS | none | Payload-customer demand response, and the programme-cost base the pass-through share divides by (**P6**) |
| supply-chain | industry-analysis | Light | RKLB, PL | none | The space-solar-cell duopoly leg inside the universe (RKLB/SolAero); records the BA/Spectrolab coverage gap rather than proxying it (**P2**) |
| risk | equity-research-core | Light | IRDM, GSAT, RKLB | none | P11 deal-security tagging for the operator cohort, and falsifier reachability (**P6**) |

> **Coverage invariant.** Every ticker in §2 appears at least once above; every
> `Subscribed` pair in §1b generates at least one task; every matrix skill is named in at
> least one `Subscribed` line. Verified by `tools/plan_audit.py` (I1–I4).

## 4. Depth Tiers

| Tier | Skills | mode-set | Tickers | Output |
|:---:|------|---|--------|------|
| Deep | unit-economics, operational-kpi | all modes | SPCX, RKLB | Full-mode curve construction on the two names that carry P1, and the only per-launch series in the universe |
| Standard | business-model, what-if, recent-quarter, ratio-analysis, peer-bench, competitive, secular-trends, sector-overview | essentials_modes | As listed | Segment restatement, Neutron arithmetic, the quarterly series, the margin ladder and the value-pool map |
| Light | growth-strategy, supply-chain, risk | essentials_modes | As listed | Demand-side scoping, the duopoly leg inside the universe, and P11 tagging |

**Budget note.** This is a targeted synthesis, not a second baseline: roughly **40 tasks
across 9 names**, against 001's 126 across 35 and 002's ~34 across 12. The budget is set to
**40** in `thesis.md`. If it must come down, drop the Light rows first — **never** the two
Deep rows, which carry P1 and the only demonstrated curve data — and never the
`recent-quarter` row, which is the entire delivery mechanism for P5.

## 5. Cross-Cutting Analysis

- **The curve matrix** (P1) is the cross-cutting output — vehicle × architecture × basis,
  with the applied floor and its grade in every cell.
- **The value-pool map** (P2) is the second: revenue growth and operating margin by segment
  across the universe, on the issuer's boundaries and on a normative restatement, with the
  spread reported rather than collapsed.
- **Basis discipline is quoted, not implied.** Downstream theses receive `B = $X/kg` and
  `C = $Y/kg` as separate facts with the architecture named. A single "$/kg to orbit" without
  a basis and an architecture is not a valid citation of this thesis's output.
- **Macro sensitivity: medium.** The curve itself is a cost series and is largely
  price-independent, but the *value-pool map* is not: the demand side funds cadence from
  capital markets, and the long end is at three-year highs with hike risk priced. In a
  NEUTRAL-bias, long-end-hostile regime the honest reading is that the demand side's
  ability to absorb the curve is constrained — which is itself a P6 input, not an opinion.
- **Constitution interaction.** A1a settled and not re-tested; **A1b tested explicitly** in
  P2 (a thesis assuming it without a test is `UNFRAMED_REFERENCE`); **F5a/F5b applied per
  architecture** in P1 and P4, with the fully-expendable gap surfaced; **DA-01/DA-02/DA-03/
  DA-06/DA-21/DA-25** applied on every line; **P4** governs every grade; **P10** bounds P2 —
  the value pool is mapped without valuing any constellation; **P11** tags IRDM, GSAT and
  RKLB.
- **A constitution gap this thesis expects to surface.** F5a/F5b cover fully and partially
  reusable vehicles. **Fully expendable vehicles — Electron and Alpha, the two vehicles for
  which the universe has demonstrated cost data at all — sit outside both.** Recorded as an
  amendment candidate for human approval, not executed here.
- **Pair-trade candidates: none.** This thesis produces no positions by design. The relative
  axis it does produce — launcher margin versus operator margin — is handed to 005, 006 and
  011 to convert.

## 6. Output Contract

- **Per-ticker (dispatcher-resumable)**: `artifacts/{ticker}/{YYYY-MM-DD}_{skill}_{mode}.md`
  — the suffix **must** be `_{skill}_{mode}.md` with the real mode slug, so
  `dispatch.resume_verdict()` can find it.
- **Cross-cutting (not resume-tracked)**: `_cross/{name}.md`.
- **Primary artifacts**: `_cross/launch-cost-curve.md` — the vehicle × architecture × basis
  matrix with its applied floors, its grades and its absent cells (**P1**); and
  `_cross/value-pool-map.md` — the segment-level value map (**P2**). These two are what 004
  and 005 cite.
- Snapshot: `snapshots/003-launch-cost-curve-value-migration/{YYYY-MM-DD}_thesis.md`
- **Frontmatter**: per `contracts/artifact-frontmatter.yaml`, with `thesis_id:
  "003-launch-cost-curve-value-migration"`. All five pins are mandatory:
  `constitution_pin: 1.4.0`, `assumption_pin: "2"`, `skill_pin`, `as_of`,
  `corpus_version`.
- **Synthesis task.** 001 found that `agentii.tasks` emits **no** synthesis task, so a
  thesis whose Output Contract requires a `_cross/` artifact must hand-add one. **Two are
  required here**, one per primary artifact.

## 7. Thesis Phases

| Phase | Tasks | Duration | Dependencies |
|:---:|------|:---:|------|
| 1 — Curve matrix (P1) | DA-01 A/B/C for every vehicle; architecture labels; the three-way floor table; absent cells named with their resolving source | Week 1 | Constitution v1.3.0 loaded; 002's denominators consumed |
| 2 — Floor inputs (P1, P4) | Source propellant mass and price; the expended-stage cost band; convert basis B for Falcon 9; record what 003 owns of the validation queue | Week 2 | Phase 1 |
| 3 — Value-pool map (P2) | Segment revenue growth and margin across all nine names; DA-21 restatement; the captive-versus-independent operator test | Week 3 | Phase 2 |
| 4 — Curve direction (P3, P5) | The `CLAIMED`/`DEMONSTRATED` register; the per-launch series and its averaging assumption; the 22.5% revenue-side reconciliation and its timing hypothesis | Week 4 | Phase 3 |
| 5 — Neutron arithmetic (P4) | Source the payload; test the ~3.1 t break-even; confirm the F5b architecture; state the conclusion conditionally | Week 5 | Phase 4 |
| 6 — Pass-through (P6) | Cost-versus-price at the only issuer disclosing both; demand-side programme-cost shares; the A1a-reconciliation statement | Week 6 | Phase 5 |
| 7 — Hand-off | Publish the citable curve and map for 004–006; record every unconverted figure with its disposition class | Week 7 | Phase 6 |

## Clarifications

Recorded by `agentii.specify` at creation, 2026-09-18. No `agentii.clarify` round has run;
the following are recorded as open for that pass.

- **Q-1 (P1, basis adoption)** — Does the curve's headline become a single basis, or is the
  *spread* the deliverable? **Provisional, pending clarify:** the spread. Per the §1c
  standing rule, all three bases are reported and the spread is a finding; the *rank
  ordering of vehicles* is reported per basis, and any rank inversion between bases is
  itself a result.
- **Q-2 (P3/P5, the averaging assumption)** — Is RKLB's `revenue per launch` an arithmetic
  mean over the period's missions, which is what makes the Q1 figures derivable by
  subtraction from Q2 and H1? **Unverified.** **Provisional:** derive them, grade them
  `DEMONSTRATED` (figures) / `MODELED` (the derivation), and put the averaging assumption
  itself in the validation queue as P5's first task.
- **Q-3 (P4, payload admissibility)** — Is a published vehicle spec admissible as the
  Neutron denominator, given 002 is chartered to **reject** company-published specs for
  Electron? **Provisional:** reject it on the same grounds. Use a filed or manifest source,
  or carry the ± band explicitly and mark P4 conditional. A rule applied to one issuer and
  waived for another is not a rule.
- **Q-4 (P2, pool boundary)** — Does "the launch segment" mean the issuer's own segment
  definition (**DA-21**) or a normative restatement? **Provisional:** both, side by side,
  with the spread reported — the standing rule again. Note that SPCX's Space segment
  contains 14-year development contracts and SPCX's internal Starlink launches generate no
  inter-segment revenue (**DA-08**), so the issuer definition understates launch on both
  sides.
- **Q-5 (P3/P6, thresholds)** — P3's 50% demonstrated-share bar and P6's 10% programme-cost
  bar are judgements set to be falsifiable, not measurements. **Flagged for human
  confirmation; if answered differently this is a PATCH to spec, not a MAJOR event.**
