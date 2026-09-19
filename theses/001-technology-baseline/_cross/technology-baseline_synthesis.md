---
thesis_id: "001-technology-baseline"
artifact: technology-line-register
pillar: [PIL-1, PIL-2, PIL-3, PIL-4, PIL-5, PIL-6]
ticker: cross
skill: synthesis
mode: default
task: T126
generated_at: 2026-09-18T21:45:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-18
corpus_version: "UNPINNED"
schema: technology_line_register
schema_version: 1
evidence_grades_present: [DEMONSTRATED, CLAIMED, MODELED]
verdicts: {HOLDS: 3, FALSIFIED: 0, UNRESOLVABLE-FROM-PUBLIC-SOURCES: 3}
---

# Technology Baseline — Register of Six Lines

**This is the artifact thesis 001 exists to produce.** Six technology lines, each with the
physical or economic bound that governs it, the single constraint that binds, every claim
graded, and the falsifier verdict.

**Headline finding: three of six falsifiers cannot fire from any public source.**
PIL-3, PIL-5 and PIL-6 each depend on a disclosure that does not exist — not in the corpus,
not in a filing, not anywhere the platform can reach. **The thesis's falsifiers are not
weak; half of them are structurally unarmed.** This is a finding about disclosure, not
about the technology, and it is stated in §7.

---

## Summary table

| # | Line | Pillar | Governing bound | Value | Unit | Binding constraint | Verdict |
|---:|---|---|---|---:|---|---|---|
| 1 | Launch cost floor | PIL-1 | Propellant mass × propellant price ÷ payload | **46.0** | USD per kg to LEO | MASS_LAUNCH_COST | **HOLDS** |
| 2 | Orbital power envelope | PIL-2 | Array area per MW delivered BOL | **5,080** | m² per MW | POWER | **HOLDS** |
| 3 | Constellation economics | PIL-3 | Break-even revenue at observed gross margin | **1.69** | × current revenue | MANUFACTURING_RATE | UNRESOLVABLE |
| 4 | Microgravity economics | PIL-4 | Incumbent terrestrial gross margin | **72.0** | percent | DEMAND | **HOLDS** |
| 5 | Orbital compute closure | PIL-5 | Rejection area per MW at 300 K | **2,419** | m² per MW | THERMAL | UNRESOLVABLE |
| 6 | Spectrum and slots | PIL-6 | Reference transaction for three spectrum blocks | **19.6** | USD billions | REGULATORY_SPECTRUM | UNRESOLVABLE |

---

## Line 1 — Launch cost has a hard floor

```yaml
line_no: 1
pillar: PIL-1
line_name: "Launch cost has a hard floor, and no one has crossed it"
governing_bound:
  statement: >
    The propellant mass a reusable vehicle must lift sets a price floor that
    reusability does not remove: it removes the hardware, not the propellant.
  value: 46.0
  unit: "USD per kg of payload delivered to LEO"
  source: "constitution F5; Starship propellant load ~4,600 t; LNG and LOX commodity prices"
  derivation: >
    4,600,000 kg propellant x $1.00/kg = $4.60M per flight.
    4,600,000 kg x $2.00/kg        = $9.20M per flight.
    At 100,000 kg payload to LEO: $4.60M / 100 t = $46/kg;  $9.20M / 100 t = $92/kg.
    The bound is the COMMODITY price of methane and oxygen, not a contract price.
binding_constraint: MASS_LAUNCH_COST
claims:
  - claim: "The propellant floor is $46-92/kg to LEO and is unreachable downward by reuse."
    evidence_grade: MODELED
    source: "constitution F5 derivation; propellant load is an engineering estimate, not a filed figure"
  - claim: "The only issuer disclosing a per-launch figure discloses $14,667/kg."
    evidence_grade: DEMONSTRATED
    source: "RKLB 10-Q unit-economics artifact; the sole per-launch disclosure in the universe"
    definitions: ["DA-01", "DA-06"]
  - claim: "No launch company in the universe has launch as its growth driver."
    evidence_grade: DEMONSTRATED
    source: "SPCX, RKLB and FLY unit-economics artifacts, three independent filings"
  - claim: "LAUNCH VOLUME FELL AT THE LAUNCH MONOPOLY: SPCX mass to orbit -25.6%, Falcon launches -17.8%, internal launches -25.0%, Starship launches 3 to 1."
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q Q2 2026, Key Business Metrics table - the issuer's own chosen throughput measures"
  - claim: "SPCX Space segment is 12.3% of revenue and fell 1.9% across H1 2026 while consolidated revenue rose 53.7%."
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q Q2 2026, segment results"
  - claim: "Price and cost are not the same number, and no issuer discloses price at cadence."
    evidence_grade: CLAIMED
    source: "no issuer filing; inference from contract values and payload mass"
    definitions: ["DA-02", "DA-06"]
wrong_if_verdict:
  metric: demonstrated_price_per_kg_to_LEO_P50
  threshold: 1000
  observed: 14667.0
  basis: >
    basis B (marginal cost per launch) - the ONLY basis any issuer discloses. The
    falsifier is evaluated on basis B because bases A (customer list price) and C
    (fully loaded amortized) are not disclosed by any issuer in the universe.
  verdict: HOLDS
```

**Reading.** The falsifier fires if a demonstrated price falls below $1,000/kg. The only
demonstrated figure anywhere in the universe is **$14,667/kg on basis B — 14.7× above the
threshold.** The bound is not close to being tested.

**What would change the verdict**: an issuer disclosing a customer list price (basis A) or a
fully-loaded cost (basis C) at commercial cadence. **None does.** The gap between the
propellant floor ($46/kg, MODELED) and the only disclosed figure ($14,667/kg, DEMONSTRATED)
is **319×** — and that gap, not the floor, is where the investment question lives.

### ⚠️ The line's content changed in the final pass, and it changed the wrong way for the thesis

**SPCX's Q2 2026 10-Q reports its own throughput metrics falling:**

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---:|---:|---:|
| **Mass to orbit (t)** | **485** | 652 | **−25.6%** |
| **Falcon launches** | **37** | 45 | **−17.8%** |
| — internal (Starlink) launches | 27 | 36 | **−25.0%** |
| Starship launches | 1 | 1 | H1: 3 → **1** |

**SPCX describes mass to orbit as "a key indicator of SpaceX's capacity and scalability."
It fell 25.6%.** The contraction is concentrated in **internal** launches — Starlink
deployment, the demand that was supposed to justify the cadence.

**And the Space segment is 12.3% of revenue, falling 1.9% across H1 while consolidated
revenue rose 53.7%.** The company the universe was built around is **a satellite broadband
operator (54.9%) with a terrestrial AI business (32.8%) that also launches rockets.**

**A1b — "launch is the master *value* variable" — is falsified on the issuer's own chosen
metrics.** A1a — "launch cost is the master *cost* variable" — survives, because the cost
floor still bounds every downstream case. **The constitution's proposed A1a/A1b split should
be reviewed with this evidence in hand: the split is not merely defensible, it is confirmed,
and the falsified half is the one the sector's narratives rest on.**

**One distinction must be preserved, and it is favourable to the launch business.** SPCX's
Space segment carries a **65.8% gross margin** — the highest in the universe — and its cost
of revenue was **flat (−0.3%)** while revenue rose 29.0%. **The marginal Falcon launch is
highly profitable.** The $(542)M quarterly segment loss is **Starship development R&D
($1,076M per quarter, 111.9% of segment revenue)**, not launch economics. **Falcon launch
economics are good; the segment loss is a development-funding decision.** That distinction
is the difference between "launch is unprofitable" and "one rocket is being funded," and
only the second is what the filings say.

---

## Line 2 — Orbital power and thermal rejection set a hard envelope

```yaml
line_no: 2
pillar: PIL-2
line_name: "Orbital power and thermal rejection set a hard envelope on every orbital business"
governing_bound:
  statement: >
    Solar array area required per MW delivered at beginning of life, after eclipse,
    packing and degradation multipliers.
  value: 5080.0
  unit: "square metres of solar array per MW delivered in orbit"
  source: "constitution F1; AM0 solar constant and published space-cell efficiency"
  derivation: >
    AM0 irradiance 1,361 W/m^2 x 30% cell efficiency = 408 W/m^2.
    1,000,000 W / 408 W/m^2 = 2,449 m^2 of cell area per MW.
    Multipliers, applied as a chain:
      x 1.587  eclipse and duty cycle (battery recharge share)
      / 0.85   array packing and structural fill factor
      / 0.90   end-of-life degradation
    = 2,449 x 1.587 / 0.85 / 0.90 = 5,080 m^2 per MW.
    The area is 2.1x the cell area a naive calculation returns (5,080 / 2,449 = 2.07),
    which reconciles against the independently published estimate of ~5,640 m^2/MW.
    NOTE: this line previously read "12.5x" - a unit confusion, being 5,080 / 408, i.e.
    area divided by a power density. Corrected 2026-09-18.
binding_constraint: POWER
claims:
  - claim: "A MW in orbit requires 5,080 m^2 of array - 2.1x the naive cell-area figure."
    evidence_grade: MODELED
    source: "constitution F1 derivation; chain multipliers are engineering estimates"
  - claim: "No listed issuer discloses orbital-compute revenue on any reading."
    evidence_grade: DEMONSTRATED
    source: "GOOG, NVDA, VRT, MSFT secular-trends and unit-economics artifacts"
    definitions: ["DA-20"]
  - claim: "The capability is real and immaterial to its listed owner."
    evidence_grade: DEMONSTRATED
    source: "GOOG R&D $18.2B/quarter is ~20x SPCX entire Space segment revenue"
  - claim: "Hyperscaler capex implies terrestrial capacity far exceeding any orbital plan."
    evidence_grade: DEMONSTRATED
    source: "MSFT FY2026 capex $115,948M implies 2.9-11.6 GW/yr; SPCX cumulative is ~1.4 GW"
wrong_if_verdict:
  metric: listed_issuer_orbital_compute_revenue_disclosed
  threshold: 0
  observed: 0.0
  basis: "any of the four readings in DA-20: recognized revenue, material revenue, signed commitment, backlog"
  verdict: HOLDS
```

**Reading.** The falsifier fires on **any** disclosure of orbital-compute revenue on **any**
of four readings. **Zero of five subscribing issuers disclose any.** The verdict is HOLDS
and it is the strongest of the three: the observation is binary, the sources are quarterly
filings, and all five are covered.

### ⚠️ The verdict now rests on a definitional test, not on absence — register the trap

**In the final pass SPCX disclosed AI-segment revenue of $2,561M in Q2 2026 — the largest
single contributor to its consolidated growth — and named the segment *"AI computational
infrastructure"* with a key metric of nameplate compute draw (1.4 GW).**

**A reader could fire PIL-2's falsifier on this.** The DA-20 four-way reading — required by
§1c precisely for this situation — says not to:

| Axis | SPCX's AI segment |
|---|---|
| compute **in** orbit | **No** — nameplate compute draw counts GPUs installed **in data centers**, and explicitly excludes cooling, power distribution and facility overhead: the vocabulary of a terrestrial build |
| compute **for** orbit | No |
| communications **from** orbit | No — that is the Connectivity segment, reported separately |
| **terrestrial compute with satellite-delivered distribution** | **Yes** |

**Verdict unchanged: HOLDS.** But the basis of the verdict has changed in a way that matters:
**it is no longer "no issuer discloses anything adjacent," it is "the closest adjacent
disclosure fails the definitional test."** **Registered as a false-positive trap for any
future analyst on this pillar** — "AI infrastructure" is adjacent to, and not the same as,
"orbital compute," and the §1c side-by-side reading is the only thing standing between them.

**The finding is asymmetric in a way worth stating.** The envelope is not being tested
because **nobody is near it** — not because the physics blocks them. MSFT's single-year
capex implies terrestrial capacity **2–8× SPCX's entire cumulative launch history** in one
year. **The orbital-compute question is settled by terrestrial economics before the orbital
envelope is reached.** Line 5 makes this precise.

---

## Line 3 — Manufacturing rate, not launch capacity, binds constellation economics

```yaml
line_no: 3
pillar: PIL-3
line_name: "Manufacturing rate, not launch capacity, is the binding constraint on constellation economics"
governing_bound:
  statement: >
    Revenue multiple required to absorb a fixed operating base at the issuer's own
    observed gross margin. This is the line's real bound: not a cost, but a ratio
    between a fixed cost base and a gross margin that must cover it.
  value: 1.69
  unit: "multiple of current quarterly revenue required to reach operating break-even"
  source: "PL 10-Q Q1 FY2026; YSS 10-Q; cross-checked against RKLB and FLY"
  derivation: >
    PL Q1 FY2026: revenue $94.150M, gross profit $50.401M (53.5%), operating
    expenses $85.289M. Break-even revenue = $85.289M / 0.535 = $159.392M.
    $159.392M / $94.150M = 1.69x current revenue.
    YSS: gross margin 24.0%, opex 68.6% of revenue.
    Break-even = 0.686 / 0.240 = 2.86x current revenue.
    The higher the gross margin, the LOWER the required multiple - but neither
    issuer is within 1.69x of break-even today.
binding_constraint: MANUFACTURING_RATE
claims:
  - claim: "The sector's problem is fixed-cost absorption, not unit economics."
    evidence_grade: DEMONSTRATED
    source: "PL: best gross margin in the universe (53.5%) and still -37.1% operating"
  - claim: "Component suppliers earn roughly 2x the primes they supply."
    evidence_grade: DEMONSTRATED
    source: "HEI 25.5%, KRMN 19.1%, WWD ~17% vs LMT 12.4%, RTX 11.4%, LHX 11.1%, NOC 10.1%"
  - claim: "Prime operating margin carries no information about space exposure."
    evidence_grade: DEMONSTRATED
    source: "four primes in a 10.1-12.4% band with very different space exposure"
  - claim: "Launch is not the growth driver for any of the three launch companies."
    evidence_grade: DEMONSTRATED
    source: "SPCX, RKLB, FLY artifacts, three independent filings"
wrong_if_verdict:
  metric: share_of_named_issuers_citing_launch_availability_as_primary_delay_cause
  threshold: 0.5
  basis: >
    Item 1A risk factors and MD&A delay language across all 19 named issuers, with the
    PRIMARY delay cause identified by the issuer.
  verdict: UNRESOLVABLE-FROM-PUBLIC-SOURCES
```

**Why UNRESOLVABLE, stated precisely — and this is a distinction the entry owes the
reader.** The risk-factor language **is** filed and **is** public. What does not exist is
**any structured field for delay cause**: the platform exposes no such column, no issuer
codes its delays, and the census would require reading and coding 19 filings. **So the
honest description is: the census is UNBUILT, not the disclosure UNAVAILABLE.**

**The disclosure that would resolve it**: a per-issuer coding of Item 1A and MD&A delay
language across all 19 named issuers, recording the primary cause the issuer itself names.
Building it is bounded work — 19 filings — and it is the single highest-value unbuilt
artifact in the thesis.

**The adjacent finding is stronger than the falsifier, and is why the pillar still stands.**
The measured constraint is **fixed-cost absorption**, which is DEMONSTRATED on filed
numbers: PL needs **1.69×** its current revenue to break even with the sector's best gross
margin, YSS needs **2.86×**. **Neither number involves launch at all.** The falsifier asks
about launch because the thesis expected launch to bind; the filings say something else
does, and the something else is measurable from XBRL without reading a word of risk-factor
prose.

**Recommendation carried to the amendment queue: re-scope PIL-3's wrong_if** from a prose
census to the break-even multiple, which is computable, comparable across issuers, and
already computed here.

---

## Line 4 — Microgravity processing is demonstrated physics with unproven economics

```yaml
line_no: 4
pillar: PIL-4
line_name: "Microgravity processing is demonstrated physics with unproven economics"
governing_bound:
  statement: >
    The gross margin of the incumbent terrestrial process that an orbital process
    must beat to be chosen. This is the hurdle rate, and it is the line's real bound.
  value: 72.0
  unit: "percent gross margin of the incumbent terrestrial process"
  source: "AMGN 10-Q Q2 2026; BMY 10-Q Q2 2026"
  derivation: >
    AMGN Q2 2026: revenue $10,054M - COGS $2,811M = gross profit $7,243M
      -> $7,243M / $10,054M = 72.0%.
    BMY Q2 2026: revenue $12,973M - COGS $3,726M = gross profit $9,247M
      -> $9,247M / $12,973M = 71.3%.
    Two independent buyers cluster within 0.7 points of each other. That
    convergence is the finding: ~72% is the incumbent's return, and an orbital
    process must clear it.
binding_constraint: DEMAND
claims:
  - claim: "The demand side turns over 73x the entire pure-play space cohort, annually."
    evidence_grade: DEMONSTRATED
    source: "MRK $16,607M + BMY $12,973M + AMGN $10,054M = $39,634M/quarter vs ~$2,170M/yr cohort"
  - claim: "Merck's R&D alone is 7.3x the combined annual revenue of the pure-play cohort."
    evidence_grade: DEMONSTRATED
    source: "MRK FY2025 R&D $15,789M vs cohort ~$2,170M"
  - claim: "The constraint is demand-side willingness, not supply-side capacity."
    evidence_grade: DEMONSTRATED
    source: "MRK, BMY, AMGN artifacts; no capital constraint at the buyers"
  - claim: "Buyers are not one pool: equity cushions span 32.3% (MRK), 25.5% (BMY), 12.2% (AMGN)."
    evidence_grade: DEMONSTRATED
    source: "three 10-Qs; adoption should appear first at the less-levered buyers"
  - claim: "Value-per-kg and cost-per-kg for any microgravity product do not exist publicly."
    evidence_grade: CLAIMED
    source: "Varda is private; UTHR discloses no microgravity economics"
    definitions: ["DA-22"]
wrong_if_verdict:
  metric: listed_pharma_microgravity_commercial_manufacturing_disclosure
  threshold: 0
  observed: 0.0
  basis: "UTHR, MRK, BMY, AMGN 10-K or 10-Q - any disclosure of commercial microgravity manufacturing"
  verdict: HOLDS
```

**Reading.** The falsifier fires on any listed pharma disclosing commercial microgravity
manufacturing. **Zero of four do.** HOLDS.

**But the falsifier is the weaker half of this line, and the register should say so.** The
disclosure test passes trivially because the disclosure does not exist — the same
"immaterial-to-the-counterparty" suppression named in §4 as a cross-pillar pattern. **The
economic test is the real one, and it is the clearest UNRESOLVABLE in the thesis:**

**The disclosure that would resolve it**: a value-per-kg or cost-per-kg figure for a
microgravity-manufactured product, from either a listed pharma's segment disclosure or a
private operator's (Varda's) financials. **Neither exists.** Varda is private and discloses
nothing; UTHR's partnership is too small to force a segment. **This is a stronger
UNRESOLVABLE than PIL-3's** — there the data is unbuilt, here it is absent.

**The finding that does stand is quantitative and sufficient to carry the pillar**: an
orbital process must beat a **72% gross margin**. That is what the buyers already earn
terrestrially, on filed numbers, at two independent companies that agree to within 0.7
points. **The microgravity question is not "is it feasible" — it is "is it better than 72%",
and no one has published a number either way.**

---

## Line 5 — Does orbital compute close before terrestrial compute wins?

```yaml
line_no: 5
pillar: PIL-5
line_name: "Does orbital compute close before terrestrial compute wins?"
governing_bound:
  statement: >
    Radiative heat rejection area required per MW of compute power, at the
    temperature the radiator must run.
  value: 2419.0
  unit: "square metres of radiator per MW rejected at 300 K"
  source: "constitution F2; Stefan-Boltzmann"
  derivation: >
    P/A = epsilon x sigma x (T^4 - T_sink^4), sigma = 5.6704e-8 W/m^2K^4.
    T = 300 K, epsilon = 0.9, T_sink negligible:
      P/A = 0.9 x 5.6704e-8 x 300^4
          = 0.9 x 5.6704e-8 x 8.1e9
          = 413.4 W/m^2.
    1 MW = 1e6 W -> 1e6 / 413.4 = 2,419 m^2 per MW.
    T^4 scaling is the whole story: at 400 K -> 765 m^2/MW; at 500 K -> 313 m^2/MW.
    Returning the waste heat is 7.7x harder than collecting the power (F1: 5,080 m^2/MW).
binding_constraint: THERMAL
claims:
  - claim: "Rejecting a MW costs 2,419 m^2 at 300 K; collecting one costs 5,080 m^2."
    evidence_grade: MODELED
    source: "constitution F1 and F2 derivations; epsilon and T are engineering assumptions"
  - claim: "Terrestrial capacity is expanding faster than any orbital plan."
    evidence_grade: DEMONSTRATED
    source: "MSFT FY2026 capex $115,948M implies 2.9-11.6 GW/yr vs SPCX cumulative ~1.4 GW"
  - claim: "Vertiv is constrained but still expanding - 'bottleneck' overstates its position."
    evidence_grade: DEMONSTRATED
    source: "VRT 10-Q unit-economics artifact"
  - claim: "No operator discloses orbital compute capacity in kW, revenue, or cost per kW."
    evidence_grade: DEMONSTRATED
    source: "GOOG, NVDA, VRT, MSFT, SPCX filings"
wrong_if_verdict:
  metric: orbital_to_terrestrial_cost_per_kW_ratio
  threshold: 3
  basis: >
    REPORTED ON ALL THREE BASES, per the contract's no_bare_ratio rule.
    The DENOMINATOR is public on all three; the NUMERATOR is undisclosed on all three.
      A - hyperscaler marginal: MSFT FY2026 capex $115,948M over 2.9-11.6 GW
          implied capacity = $10,000-40,000 per kW. (DEMONSTRATED capex;
          MODELED capacity conversion.)
      B - colocation market rate: ~$2,000 per kW per year annualised.
          (MODELED - no issuer in the universe discloses a colo rate.)
      C - new-build fully loaded: basis A capex annualised over ~15 yr at 8%
          = ~$1,170-4,670 per kW per year. (MODELED.)
    Orbital numerator: no issuer discloses cost per kW, capacity in kW, or rate.
    A ratio cannot be formed. Reporting one basis alone would fail validation;
    reporting three with a missing numerator is the honest state.
  verdict: UNRESOLVABLE-FROM-PUBLIC-SOURCES
```

**Why UNRESOLVABLE — and note the asymmetry, which is the point.** The **denominator is
fully public.** MSFT's FY2026 capex of $115,948M and its capacity guidance give a
terrestrial cost per kW on all three bases. **The numerator does not exist.** No listed
issuer discloses orbital compute revenue, deployed capacity in kW, or cost per kW.

**Why UNRESOLVABLE — the numerator and denominator fail for DIFFERENT reasons, and the
register reports both rather than collapsing them.**

- **The denominator is reachable in principle but commercially licensed.** Basis B
  (colocation market rate) is not published; it is sold by data providers. That is the
  `UNRESOLVABLE-FROM-PLATFORM` condition amendment #4 proposes to name.
- **The numerator does not exist anywhere.** No listed issuer discloses orbital compute
  revenue, deployed capacity in kW, or cost per kW. That is the stricter
  `UNRESOLVABLE-FROM-PUBLIC-SOURCES` condition.

**The contract enum carries only `UNRESOLVABLE-FROM-PUBLIC-SOURCES`, so that is the value
recorded** — but the precise disposition differs by side, and **this entry is the second
piece of evidence for amendment #4**: the enum is missing a class that two pillars already
need.

**The disclosure that would resolve it**: an operator-disclosed cost per kW for a deployed
orbital compute payload, or a signed customer rate in $/kW, from any of GOOG, NVDA, VRT,
MSFT or SPCX; or a peer-reviewed techno-economic analysis with its basis stated. **None
exists**, and per §4.4 the reason is structural — the initiative is immaterial to every
listed owner, so no accounting or regulatory force compels the number into a filing.

**The falsifier cannot fire, and that is itself the line's finding.** A threshold of 3 is
unreachable when the numerator is undisclosed: **the ratio is not large, it is undefined.**
The previously-recorded reachability finding (threshold 3 reachable only against basis C)
**rests on MODELED terrestrial comparators and is carried here as MODELED, not
DEMONSTRATED.** What is DEMONSTRATED is more decisive: **MSFT's one-year capex implies
2–8× SPCX's entire cumulative launch history, in a single year.** Terrestrial compute is
not waiting for orbital compute to close — **it is closing the question from below.**

### ⚠️ THE DECISIVE DISCONFIRMATION — the one company that could do both chose the ground

**The strongest available test of this line was never the ratio. It was SPCX.** The company
with the world's only high-cadence reusable launch franchise is the one actor for whom
orbital compute has the lowest delivered mass cost. **If orbital compute were going to
close anywhere, it would close there first.**

**SPCX's Q2 2026 10-Q answers it:**

| Datum | Value |
|---|---|
| **Nameplate compute draw** | **1.4 GW** (Q2 2025: 0.4 GW) — **+250%** |
| H1 2026 capex increase | **$21,511M** |
| Attributed first to | *"the build out of **DATA CENTERS** and related infrastructure, and space launch facilities"* |
| AI segment definition | *"AI computational infrastructure"* — **no mention of orbit** |
| Stated launch-allocation intent | *"we expect to allocate a significant amount [of launch capacity] to our **AI segment** in the future"* |
| Pending acquisition | **Cursor, $60B implied equity value, all-stock, closing Q3 2026** |

**The one company positioned to do both is deploying 1.4 GW of compute on the ground, naming
data centers before launch facilities in its own capex narrative, and allocating launch
capacity to a segment whose compute never leaves the atmosphere.**

**This is not orbital compute being out-competed by terrestrial compute. It is orbital
compute being out-*chosen* by the only actor able to choose it.** The line does not close
because the physics forbids it — it closes because **the party with the best orbital access
revealed its preference with $21.5B of capital expenditure, and the preference is
terrestrial.**

**The residual honest caveat**: SPCX's disclosed orbital capability is not idle — mass to
orbit was 485 t in the quarter, and 397 t of it was internal payloads. **What the company
sends to orbit is satellites, not compute.** That is a fact about revealed preference, and
it is the strongest evidence on this line in either direction.

---

## Line 6 — Orbital, spectral and launch-licence access are finite allocated resources

```yaml
line_no: 6
pillar: PIL-6
line_name: "Orbital, spectral and launch-licence access are finite allocated resources"
governing_bound:
  statement: >
    The reference market price of allocated spectrum, set by the only recent
    transaction in the universe that prices it.
  value: 19.6
  unit: "USD billions - transaction value for AWS-4, H-Block and AWS-3 spectrum"
  source: "SPCX-EchoStar transaction, per constitution F6"
  derivation: >
    $19.6B for three named blocks. Per-MHz-POP requires the population-coverage
    denominator for each block, which is not in the transaction disclosure; the
    headline is carried with its unit explicitly as a TRANSACTION VALUE, not a
    unit price, because the denominator is unavailable. Stated this way rather
    than as $/MHz-POP precisely because a bare ratio would fail the contract.
binding_constraint: REGULATORY_SPECTRUM
claims:
  - claim: "Spectrum is priced as an asset, not granted as a permit."
    evidence_grade: DEMONSTRATED
    source: "SPCX-EchoStar, $19.6B for AWS-4, H-Block, AWS-3"
  - claim: "Allocation precedes deployment, so a licensed position is a dated asset."
    evidence_grade: CLAIMED
    source: "ITU first-come priority and FCC licensing structure; not issuer-disclosed"
  - claim: "This is the only non-physical constraint among the six lines."
    evidence_grade: DEMONSTRATED
    source: "constitution F6; contrast with F1, F2, F5"
  - claim: "GSAT is the purest monopsony in the universe: one buyer, 7.4% operating margin."
    evidence_grade: DEMONSTRATED
    source: "GSAT 10-Q Q2 2026; constellation capacity dedicated to a single customer"
wrong_if_verdict:
  metric: new_entrant_primary_spectrum_or_slot_grant_without_incumbent_acquisition
  threshold: 0
  basis: "FCC IBFS filings and the ITU Space Network List, filtered for primary grants to entities with no prior US holdings"
  verdict: UNRESOLVABLE-FROM-PUBLIC-SOURCES
```

**Why UNRESOLVABLE — and this is the CASE THAT MOTIVATED AMENDMENT #4.** The registries are
public. **They are not in the platform.** `FCC_IBFS` and the `ITU_Space_Network_List` are
neither SEC filings nor XBRL, so no tool in this workspace can query them.

**This is a third, distinct failure mode**: the data exists, is public, and is outside the
reachable corpus. PIL-3's is an unbuilt census; PIL-5's numerator does not exist anywhere;
PIL-6's exists and cannot be reached. **Three UNRESOLVABLE verdicts, three different
causes, three different remedies — and the contract enum can express only one of them.**
The value recorded is `UNRESOLVABLE-FROM-PUBLIC-SOURCES` for contract validity; **the
accurate disposition is `UNRESOLVABLE-FROM-PLATFORM`, which amendment #4 exists to add.**

**The disclosure that would resolve it**: a query of FCC IBFS and the ITU Space Network
List for primary spectrum or orbital-slot grants to entities with no prior US holdings —
which requires direct registry access the platform does not provide.

**What the line does establish, DEMONSTRATED and from filings**: spectrum carries a
**$19.6B reference price** at the only transaction that prices it, and **GSAT demonstrates
what a licensed position is worth when the buyer is single** — a 7.4% operating margin,
7.4× leverage, and a $2,137M accumulated deficit. **A licence is an asset; being a licence
holder with one customer is not the same as owning the asset.**

---

## §4 — Cross-cutting findings

**These are the results that are not attributable to any single line.** Each is
DEMONSTRATED on filed numbers and each changes how the universe should be read.

### 4.1 The margin ladder is a function of distance from programme risk

| Tier | Issuer | Operating margin |
|---|---|---:|
| Component supplier, installed base | **HEI** | **25.5%** |
| Component supplier | KRMN | 19.1% |
| Subsystem supplier | WWD (Aerospace segment) | ~17% |
| Prime | LMT | 12.4% |
| Prime | RTX | 11.4% |
| Prime | LHX | 11.1% |
| Prime | NOC | 10.1% |
| **Monopsony supplier** | **GSAT** | **7.4%** |

**One monotone ordering across eight issuers.** The naive reading — primes are the safe
tier, suppliers derivative — **is inverted.** The two best margins in the universe belong to
component suppliers, and the worst belongs to a network operator with a single customer.

**Refined rule, superseding the NOC version**: *component concentration predicts margin when
the supplier's revenue spreads across programmes.* **Buyer concentration alone is not the
discriminator** — the primes' buyers are the same DoD that buys HEICO's parts. **The
discriminator is whether the supplier depends on a single programme winning.**

### 4.2 The binding constraint on space operators is fixed-cost absorption

PL earns the **best gross margin in the universe (53.5%)** and still loses **37% at the
operating line**, because opex is 90.6% of revenue. **Break-even needs 1.69× current
revenue.** YSS needs **2.86×**. **Neither multiple involves launch cost.** This is the
finding PIL-3's falsifier was trying to reach by reading risk-factor prose, and XBRL
answers it directly.

### 4.3 The demand side is 73× the supply side

Three pharma buyers turn over **$39,634M per quarter** against a pure-play space cohort
turning over **~$2,170M per year** — **73× annualised.** Merck's R&D alone is **7.3×** the
cohort's combined revenue. **The microgravity constraint is demand-side willingness against
a 72% incumbent gross margin, not supply-side capacity.**

### 4.4 Immaterial-to-the-counterparty disclosure suppression

**Four instances** (GOOG, UTHR, MRCY, BWXT): the capability is real, and it is **financially
irrelevant to the listed owner**, so no accounting or regulatory force compels disclosure.
**This suppresses the evidence the falsifiers at PIL-2, PIL-4 and PIL-5 need to fire.**
It is the mechanism behind three of this register's UNRESOLVABLE verdicts, and it is why
"no disclosure" must be read as **"immaterial to the counterparty"** rather than
"does not exist."

### 4.5 Four critical duopolies are structurally unpriced

**Solar cells, liquid engines, solid motors, launch** — plus **radiation-tolerant
electronics**, the F4 gate with no listed pure-play (MRCY earns a 0.03% operating margin,
so rad-hard is not a scarce input the way F2's area is). **LMT reports Space as a named
segment and still aggregates the components away; ULA is equity-method and invisible at
both parents.** The disclosure granularity needed does not exist at any prime.

### 4.6 Value has already migrated out of launch — at the launch monopoly

**The final-pass SPCX 10-Q settles a question the thesis had been treating as open.**

| Segment | Q2 2026 revenue | Share | Operating margin | H1 revenue change |
|---|---:|---:|---:|---:|
| **Connectivity** (Starlink) | **$4,291M** | **54.9%** | **+38.6%** | **+49.1%** |
| **AI** (Grok, X, compute) | **$2,561M** | **32.8%** | not disclosed | — |
| **Space** (launch, Dragon) | **$962M** | **12.3%** | **−56.3%** | **−1.9%** |
| Consolidated | $7,814M | 100% | −1.8% | +53.7% |

**Launch is 12.3% of revenue at the company that dominates launch, and it shrank across a
half in which consolidated revenue rose 53.7%.** Meanwhile **mass to orbit fell 25.6%** and
**Falcon launches fell 17.8%.**

**This is the thesis's most important single result, and it is a statement about the sector
rather than about one company.** Every cohort in the universe was assembled on the premise
that launch is the sector's centre of gravity — the primes sell to it, the component
suppliers supply it, the operators depend on it. **The dominant launch provider's own
segment disclosure says its future is connectivity and compute, and that it is reducing,
not increasing, what it lifts.**

**Two qualifications must travel with it, and both cut against over-reading:**

1. **The Space segment's 65.8% gross margin is the highest in the universe**, and its cost
   of revenue was flat while revenue rose 29%. **The marginal Falcon launch is highly
   profitable.** The segment loss is **Starship development R&D** — a reinvestment choice,
   not an operating failure.
2. **The reporting entity changed mid-series** (xAI merger 2026-02-02, X merger 2025-03-28,
   IPO 2026-06, Cursor pending). **Common-control accounting recasts prior periods, so
   cross-boundary growth rates mix real growth with entity change.** The Space-segment
   comparison is the one series that survives the boundary, and it is the one that fell.

### 4.7 R&D intensity distinguishes a development programme from a manufacturing franchise

Adopted as a cross-issuer diagnostic, available from every filing. **FLY 60.8%, PL 35.5%,
RKLB 35.2%** (development programmes) vs **HEI 2.6%, RTX 2.9%, BWXT 0.5%** (manufacturing
franchises). **BWXT's 0.5% is why the F2 nuclear escape hatch is engineering-sound and
economically unattached.**

---

## §5 — Platform defects found by this thesis

**Six defects, all reproducible, none previously documented.** They are reported because
every one of them would silently corrupt a thesis built on this platform.

| # | Defect | Blast radius | Status |
|---|---|---|---|
| 1 | **DA-23 sign stripping** — negative `operating_income` reported with sign removed | **6 confirmed** (SPCX, YSS, RKLB, FLY, BA, PL) + 3 candidates | amendment queued |
| 2 | **DA-26 period mislabelling** — Q4 row carries ANNUAL figures | **19 of 19 issuers**; propagates to revenue AND operating income (AMGN) | amendment queued |
| 3 | **DA-27 fiscal-period label offset** — labels do not match the issuer's own calendar | 1 candidate (HEI, 31 Oct year-end) | needs 2nd instance |
| 4 | **`_pillars_of_skills` keys by skill, not (ticker, skill)** | **55% of tasks mis-bracketed** (57 of 103) | fixed in generator |
| 5 | **Template separator row parses as a task** | ghost T001 in every template-derived spec | fixed in spec |
| 6 | **No synthesis task emitted** | Phase 7 empty for any thesis needing `_cross/` | hand-added each time |

**Plus two coverage caveats**: `OperatingIncomeLoss` is absent or segment-only at **MRK, BMY
and WWD** (the one reliable detector cannot run), and **EPS × shares is not a reliable
detector** — it passes on both sides of a flip at RKLB, FLY and VOYG.

**The strongest new detector this thesis produced is the gross-profit bound**: operating
income **cannot exceed gross profit**, at any sign. VOYG fails it by **$46,951M** across
three consecutive quarters. **This detector is strictly stronger than sign
reconciliation** and would catch every instance the sign rule misses. Add it to the
amendment queue.

---

## §6 — What would change each verdict

| Line | Verdict | The single disclosure that would move it |
|---|---|---|
| PIL-1 | HOLDS | any issuer disclosing a customer list price (basis A) or fully-loaded cost (basis C) at cadence |
| PIL-2 | HOLDS | any listed issuer disclosing orbital-compute revenue on any of the four DA-20 readings |
| PIL-3 | UNRESOLVABLE | **an unbuilt census, not an unavailable disclosure** — code Item 1A + MD&A delay causes across 19 issuers |
| PIL-4 | HOLDS (falsifier) | a value-per-kg or cost-per-kg figure for any microgravity product, from a listed pharma segment or Varda's financials |
| PIL-5 | UNRESOLVABLE | an operator-disclosed orbital cost per kW, or a peer-reviewed techno-economic analysis with its basis stated |
| PIL-6 | UNRESOLVABLE | **a corpus gap** — FCC IBFS and ITU Space Network List access |

---

## §7 — Conclusion

**The thesis's claim survives contact with the filings, and its falsifiers mostly could not
have fired. But the claim that mattered most did not survive, and it was not one of the
six.**

Three lines hold on binary, well-sourced observations — no issuer discloses orbital-compute
revenue, no listed pharma discloses commercial microgravity manufacturing, and the only
disclosed launch price is **14.7× above** the falsification threshold. Three lines are
unresolvable, **and the three failures have three different causes**: an unbuilt census
(PIL-3), a number that does not exist anywhere (PIL-5), and a registry outside the corpus
(PIL-6). **Distinguishing those three is more useful than a single "insufficient data"
label, because each has a different remedy — and only one of them is a research task.**

**The result the thesis was not looking for, and the one that matters most: launch is
12.3% of revenue at the company that dominates launch, and it is shrinking.** Mass to orbit
fell **25.6%**, Falcon launches **17.8%**, internal launches **25.0%**. The dominant launch
provider's own segment disclosure says its future is connectivity (54.9%) and compute
(32.8%), and that it is **reducing**, not increasing, what it lifts. **Every cohort in this
universe was assembled on the premise that launch is the sector's centre of gravity. The
dominant launch provider's own filings say otherwise.** A1b — launch as the master *value*
variable — is falsified on the issuer's chosen metrics. A1a — launch cost as the master
*cost* variable — survives.

**The most important positive finding is not about any of the six lines.** Across eight
issuers, the operating margin ordering is monotone in **distance from programme risk**, and
it runs **opposite** to the universe's implicit ordering: the component suppliers earn
**2×** the primes they supply, and the worst margin in the universe belongs to a network
operator with one customer. **The best exposure to a launch-driven buildout is the
installed-base component layer, whose margin does not depend on which programme wins** —
and **no listed issuer offers both growth and margin** except TER and KRMN.

**The most important negative finding is that the orbital envelope is not being tested, and
now we know why.** It is not physics and it is not cost. **The one actor with cheap orbital
access — the only actor for whom the delivered-mass penalty is smallest — deployed 1.4 GW
of compute on the ground, named data centers before launch facilities in its own capex
narrative, and is buying a $60B software company with stock.** Orbital compute is not being
out-built. **It is being out-*chosen* by the only party that could have chosen it.**

---

## Carry-forwards

0. **ESCALATE THE LAUNCH-VOLUME FINDING TO THE CONSTITUTION.** SPCX's mass to orbit
   (**−25.6%**), Falcon launches (**−17.8%**) and internal launches (**−25.0%**) fell, and
   the Space segment is **12.3% of revenue, down 1.9%** across a half in which the company
   grew 53.7%. **A1b is falsified on the issuer's own metrics; A1a survives.** The proposed
   A1a/A1b split is not merely defensible — **it is confirmed, and the falsified half is the
   one the sector's narratives rest on.** This is the highest-priority amendment in the
   queue.
0b. **REVIEW EVERY SPCX-DEPENDENT FINDING FOR ENTITY-BOUNDARY CONTAMINATION.** The xAI
   merger (2026-02-02) and X merger (2025-03-28) recast prior periods, and the June 2026
   IPO plus the pending $60B Cursor deal compound it. **Any growth rate quoted across those
   boundaries mixes real growth with entity change.** The Space-segment series is the one
   that survives; it is the one that fell.
0c. **REGISTER THE "AI INFRASTRUCTURE ≠ ORBITAL COMPUTE" TRAP** on PIL-2. SPCX now discloses
   adjacent revenue of $2,561M/quarter. The verdict holds **only** because the §1c four-way
   reading separates them. **Any analyst who reads "AI computational infrastructure" as
   orbital compute will wrongly fire the falsifier.**
1. **Build the PIL-3 delay-cause census** (19 filings). It is the only one of the three
   UNRESOLVABLEs with a remedy inside the platform, and it is bounded work.
2. **Add the gross-profit bound to the DA-23 amendment** as a detector strictly stronger
   than sign reconciliation.
3. **Register DA-26 at 19 of 19 with the WWD scope question** — the rows are reliably "not
   a quarter," not reliably "a full year."
4. **Register DA-27** pending a second non-calendar-fiscal-year instance.
5. **Report the margin ladder and the 73× demand asymmetry as the thesis's two primary
   findings**, ahead of any single line's verdict.
6. **Seven amendments remain queued for owner approval** and are unchanged by this
   synthesis.
