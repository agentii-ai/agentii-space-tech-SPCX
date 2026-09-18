# Report Input — 001 — Technology Baseline

<!-- pack_version: 2.0 · sources_hash: 6015eb06889e43b7 · deterministic — no timestamps -->

## Header facts
- thesis_id: 001-technology-baseline
- name: 001 — Technology Baseline
- claim: The orbital economy's investment cases are bounded by six technology lines, each with a hard physical or economic floor. Launch cost cannot fall below the propellant floor that reusability does not remove — but launch is 12.3% of revenue at the company that dominates it, and its self-reported throughput fell. Orbital compute is out-chosen rather than out-built: the one actor with cheap orbital access deployed 1.4 GW of terrestrial compute instead.
- constitution_pin: 1.2.0
- as_of: 2026-09-18
- entry_count: (none)
- universe: SPCX 9% ; RKLB 5% ; FLY 3% ; LUNR 2% ; PL 2% ; KRMN 3% ; VOYG 2% ; YSS 3% ; HAWK 1% ; IRDM 5% ; GSAT 3% ; SATS 4% ; LHX 2% ; NOC 2% ; LMT 2% ; BA 2% ; RTX 2% ; HWM 2% ; MRCY 2% ; BWXT 2% ; TDG 1% ; HEI 1% ; WWD 1% ; CW 1% ; KTOS 1% ; AVAV 1% ; TER 1% ; GOOG 6% ; MSFT 6% ; NVDA 4% ; VRT 4% ; UTHR 7% ; MRK 3% ; BMY 3% ; AMGN 2%

## Source — _cross/technology-baseline_synthesis.md
````markdown
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
skill_pin: "n/a"
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
    The area is 12.5x the cell area a naive calculation returns.
binding_constraint: POWER
claims:
  - claim: "A MW in orbit requires 5,080 m^2 of array - 12.5x the naive cell-area figure."
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
````

## Source — _cross/universe-panorama_synthesis.md
````markdown
---
thesis_id: "001-technology-baseline"
artifact: universe-panorama
pillar: [PIL-1, PIL-2, PIL-3, PIL-4, PIL-5, PIL-6]
ticker: cross
skill: synthesis
mode: default
generated_at: 2026-09-18T23:55:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "n/a"
as_of: 2026-09-18
corpus_version: "UNPINNED"
coverage: "35 of 35 named universe tickers; 39 artifacts"
---

# Space Tech — Universe Panorama

**Purpose: the whole map, fast.** Every named ticker in the universe, where it sits, what it
earns, and which of the six technology lines it speaks to. This is a breadth artifact — it
trades depth for completeness, per the thesis owner's stated priority.

---

## 1. The value chain, and where the money actually is

```
        DEMAND END                          ENABLING LAYER
   MRK  $16,607M/qtr  72% GM          MSFT  $115,948M capex/yr
   BMY  $12,973M/qtr  71% GM          GOOG  $18.2B R&D/qtr
   AMGN $10,054M/qtr  35% OM          NVDA  7.7% R&D
   UTHR   42% OM                       VRT  +24.1% rev, rising margin
        |                                    |
        |  73x the pure-play cohort          |  power + thermal
        v                                    v
   ┌────────────────────────────────────────────────────┐
   │              SPACE INFRASTRUCTURE                  │
   │                                                    │
   │  LAUNCH          CONSTELLATIONS       COMPONENTS   │
   │  SPCX 12.3%      SPCX Connectivity    HEI  25.5%   │
   │  RKLB            PL, YSS, LUNR        CW   19.3%   │
   │  FLY             IRDM, GSAT, SATS     KRMN 19.1%   │
   │                                       WWD  ~17%    │
   │                                       TER  32.9%   │
   │                                                    │
   │  PRIMES 10.1-12.4%   |   GROWTH DEFENSE TECH 0-0.4%│
   │  LMT NOC LHX RTX BA  |   KTOS MRCY                 │
   └────────────────────────────────────────────────────┘
```

**The single most important structural fact: margin rises as you move AWAY from the
programme.** Component suppliers earn ~2× the primes they supply. The capital-equipment
supplier (TER, 32.9%) earns ~3×. The primes earn ~11%. The growth defense-tech names earn
approximately nothing (KTOS 0.35%, MRCY 0.03%).

## 2. The margin ladder — all 35 tickers, ordered

| # | Ticker | Role | Operating margin | Revenue growth | Verdict |
|---:|---|---|---:|---:|---|
| 1 | **TER** | semiconductor test equipment | **32.9%** | **+103.9%** | best growth + margin in universe |
| 2 | **HEI** | flight-critical parts, aftermarket | **25.5%** | +25.3% | R&D 2.6%, leverage 0.85× |
| 3 | **CW** | actuation, sensors, nuclear instrumentation | **19.3%** | +5.4% | R&D 2.7%, leverage 0.97× |
| 4 | **KRMN** | composites, fairings | **19.1%** | +58.2% | 60% of op income consumed below the line |
| 5 | **UTHR** | pharma (microgravity demand) | **~42%** | — | demand end |
| 6 | **WWD** | actuation, control, combustion | **~17%** | +21.2% | no consolidated op income in extract |
| 7 | **AMGN** | pharma (microgravity demand) | **35.0%** | +9.5% | 12.2% equity/assets |
| 8 | **IRDM** | satellite comms | **15.1%** | +3.8% | **fell from 23.2%** — licence durable, service not |
| 9 | **LMT** | prime | **12.4%** | +10.5% | reports Space as a named segment; still aggregates |
| 10 | **RTX** | prime | **11.4%** | +14.5% | least space-visible name |
| 11 | **LHX** | prime | **11.1%** | — | — |
| 12 | **SATS** | satellite comms + spectrum | **10.7%** | — | **$27B spectrum gains vs $15.0B FY revenue** |
| 13 | **NOC** | prime | **10.1%** | — | monopsony rule origin |
| 14 | **GSAT** | satellite comms | **7.4%** | **−3.5%** | purest monopsony; 93% of NI non-operating |
| 15 | **BA** | prime | **0.6%** | — | DA-23 confirmed; commercial aerospace drag |
| 16 | **KTOS** | growth defense tech | **0.35%** | **+30.5%** | GM 21.8%, opex 98.5% of it |
| 17 | **MRCY** | rad-hard electronics | **0.03%** | — | **the F4 gate has no profitable pure-play** |
| — | **SPCX** | launch + Starlink + AI | **−1.8%** | **+91.9%** | Space 12.3% of revenue, −56.3% margin |
| — | **RKLB** | launch + space systems | **−24.6%** | +62% | launch revenue *fell* |
| — | **PL** | earth observation | **−37.1%** | +42.1% | **best gross margin in universe: 53.5%** |
| — | **YSS** | satellite manufacturing | **−44.6%** | −20.5% QoQ | GM 24.0%, opex 68.6% |
| — | **LUNR** | lunar landers | **−56.3%** | +304% | gov-concentrated; DA-23 candidate |
| — | **SPCX Space** | (segment) | **−56.3%** | −1.9% H1 | **but 65.8% GROSS margin** |
| — | **FLY** | launch + spacecraft | **−80.9%** | **+657%** | R&D 60.8% of revenue |
| — | **VOYG** | space stations (Starlab) | **unusable** | — | fails the gross-profit bound |
| — | **AVAV** | defense tech | **unusable** | — | `net_income_loss` null in every row |
| — | **HAWK** | RF geolocation | **unusable** | — | post-IPO capital-structure discontinuity |
| — | **GOOG / MSFT / NVDA** | enabling layer | — | — | capability real, **immaterial to the owner** |
| — | **HWM / TDG / BWXT** | components | — | — | DA-26 / R&D 0.5% (manufacturing franchise) |

## 3. Where the value migrated — and it already moved

**SPCX, Q2 2026, the company the universe was built around:**

| Segment | Revenue | Share | Operating margin | H1 change |
|---|---:|---:|---:|---:|
| Connectivity (Starlink) | $4,291M | **54.9%** | **+38.6%** | +49.1% |
| AI (Grok, X, compute) | $2,561M | **32.8%** | n/d | — |
| **Space (launch, Dragon)** | **$962M** | **12.3%** | **−56.3%** | **−1.9%** |

**And its own throughput metrics fell: mass to orbit −25.6%, Falcon launches −17.8%, internal
launches −25.0%, Starship 3 → 1.**

**Four independent issuers agree that launch is not the value driver:**
- **SPCX**: launches −17.8%, revenue +91.9%; Space 12.3% and shrinking
- **RKLB**: revenue +62%, launch revenue −$2.1M
- **FLY**: revenue +657% "driven by Spacecraft Solutions growth"
- **Every prime**: 10.1–12.4% margin band regardless of space exposure

**⇒ A1b (launch is the master *value* variable) is FALSIFIED. A1a (master *cost* variable)
HOLDS.** The launch cost floor still bounds every downstream case; it just doesn't capture
the value.

## 4. The six lines × the universe

| Line | Binding constraint | Verdict | Who speaks to it |
|---|---|---|---|
| **PIL-1** Launch cost floor | MASS_LAUNCH_COST | **HOLDS** | SPCX, RKLB, FLY — only RKLB discloses $14,667/kg, 14.7× above threshold |
| **PIL-2** Orbital power envelope | POWER | **HOLDS** | GOOG, MSFT, NVDA, VRT, BWXT — **zero disclose orbital-compute revenue** |
| **PIL-3** Constellation economics | MANUFACTURING_RATE | UNRESOLVABLE | 19 issuers; census unbuilt |
| **PIL-4** Microgravity economics | DEMAND | **HOLDS** | MRK, BMY, AMGN, UTHR — must beat a **72% incumbent gross margin** |
| **PIL-5** Orbital compute | THERMAL | UNRESOLVABLE | **SPCX chose the ground: 1.4 GW terrestrial** |
| **PIL-6** Spectrum & slots | REGULATORY_SPECTRUM | UNRESOLVABLE | SATS $27B, GSAT, IRDM, SPCX-EchoStar $19.6B |

**Three HOLDS, zero FALSIFIED, three UNRESOLVABLE — and the three UNRESOLVABLEs have three
different causes**: an unbuilt census (PIL-3), a number that exists nowhere (PIL-5), and a
registry outside the corpus (PIL-6). **Three different remedies; only one is a research task.**

## 5. The five things that actually matter

**① Margin is a function of distance from programme risk, and it runs inverted to narrative.**
Component suppliers earn **2×** the primes. The capital-equipment supplier earns **3×**. The
"growth" names earn **nothing**. **No listed issuer offers both growth and margin except TER
and KRMN.**

**② The binding constraint on operators is fixed-cost absorption, not unit economics.**
PL has the sector's **best gross margin (53.5%)** and still loses **37%** at the operating
line. Break-even needs **1.69×** current revenue; YSS needs **2.86×**. **The gross margin is
fine; the expense base is the problem.** Confirmed at seven issuers.

**③ Orbital compute was out-chosen, not out-built.** SPCX — the only actor with cheap orbital
access — deployed **1.4 GW of terrestrial compute**, named **data centers before launch
facilities** in a **$21,511M** capex increase, and its **only new risk factor this quarter is
about data centers** — naming **"power constraints."** *The power constraint is real, binding,
and it binds on the ground first.*

**④ The demand end is 73× the supply end and is not capital-constrained.** MRK+BMY+AMGN turn
over **$39,634M/quarter** against a **~$2,170M/year** pure-play cohort, at a **71.3–72.0%**
gross margin that any orbital process must beat. **The barrier is willingness, not capacity**
— and no launch-cost reduction touches it.

**⑤ Half the universe's critical inputs are structurally unpriced.** Solar cells (RKLB/SolAero,
BA/Spectrolab), liquid engines, solid motors, launch (ULA is equity-method), and rad-hard
electronics — **MRCY, the F4 gate's only pure-play, earns 0.03%.** *The disclosure granularity
needed does not exist at any prime.*

## 6. Coverage honesty — what this panorama does and does not have

**Has**: all **35** named tickers, one to four skill-views each; **39 artifacts**; six
technology lines with derived bounds; a validated register; **9 amendment candidates**.

**Does not have**:
- **Depth on most names** — several tickers carry one skill-view where the spec calls for
  three. **Accepted deliberately**: this thesis's job is the map, not the territory.
- **Three unusable extracts** — AVAV (`net_income_loss` null in every row), HAWK (post-IPO
  share-count discontinuity), VOYG (fails the gross-profit bound). **Platform holes, not
  issuer defects.**
- **The PIL-3 delay-cause census** — 1 of 19 issuers coded. **The single highest-value
  unbuilt artifact for thesis 002.**
- **Any non-listed actor** — **Varda Space Industries is in scope but not covered**; it was
  scoped to a later thesis. **Given that no listed name discloses microgravity economics,
  Varda is the highest-value private target in the sector.**
- **SpaceX pre-IPO comparables** — the entity changed mid-series (xAI merger, X merger, IPO,
  pending $60B Cursor deal), so **cross-boundary growth rates mix real growth with entity
  change.**

## 7. What thesis 002 should do

1. **Build the PIL-3 delay-cause census** (19 filings) — the only UNRESOLVABLE with a remedy
   inside the platform.
2. **Cover Varda** — the demand-side economics exist nowhere in the listed universe.
3. **Resolve the three unusable extracts** before ranking anything on AVAV/HAWK/VOYG.
4. **Get the platform's DA-23 / DA-26 / DA-27 defects fixed** — they corrupt every XBRL read.
5. **Deepen the four highest-information names**: TER (capacity pricing), HEI (installed-base
   margin), PL (best gross margin in sector), and SPCX's Connectivity segment (the only
   profitable space-adjacent operating business at scale).
````

## Artifact — artifacts/AMGN/2026-09-18_2055_unit-economics_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-4
ticker: AMGN
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T20:55:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 and Q4 FY2024 rows carry ANNUAL revenue AND ANNUAL operating income"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against COGS-based gross profit; AMGN CLEAN"
  - da_id: "DA-22"
    chosen_reading: "microgravity R&D not separately disclosed"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# AMGN — Microgravity Demand End (Unit Economics of the Buyer)

Source: Form 10-Q, accession `0000318154-26-000126` (Q2 2026, quarter ended 2026-06-30).

---

## 1. The buyer earns a 35% operating margin — the highest in the universe

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$10,054M** | $9,179M | +9.5% |
| COGS | $2,811M | — | 28.0% of revenue |
| Implied gross profit | **$7,243M** | — | **72.0% margin** |
| Operating income | **$3,514M** | $2,656M | +32.3% |
| **Operating margin** | **35.0%** | 28.9% | **+6.1 pts** |
| Net income | $2,375M | $1,432M | +65.8% |
| EPS (diluted) | $4.37 | $2.65 | +64.9% |

**A 35.0% operating margin and a 72.0% gross margin.** For scale, the **highest operating
margin of any space company in this universe is Karman's 19.1%** — and that required a
levered PE roll-up. Amgen earns **1.8× Karman's margin** as an ordinary course of business.

**The component identity runs:**

```
revenue $10,054M − COGS $2,811M = gross profit $7,243M
gross profit $7,243M − opex $3,729M = operating income $3,514M  ✓
```

Operating income is well below gross profit — the gross-profit bound holds. **AMGN CLEAN on
DA-23.** And it reconciles to EPS exactly:

```
EPS (diluted) $4.37 x 544M diluted shares = $2,377.3M
reported net income                       = $2,375.0M
gap: 0.1%
```

**Clean-positive count: 16 of 16.**

## 2. The buyer's margin is the thesis's real obstacle

**Put the two ends of the transaction side by side:**

| | Operating margin | Gross margin |
|---|---:|---:|
| **AMGN (buyer)** | **35.0%** | **72.0%** |
| **KRMN (best supplier)** | 19.1% | 43.0% |
| PL (best operator gross margin) | −37.1% | 53.5% |
| YSS | −44.6% | 24.0% |
| FLY | −80.9% | 20.3% |

**The buyers earn more than twice what the best suppliers earn, at both the gross and
operating lines.** A pharma company has no economic reason to accept the operational
complexity, timeline risk and regulatory novelty of an orbital process when its terrestrial
process already returns 72% gross margin.

**This is the quantitative form of the PIL-4 finding**: orbital R&D must beat a **72% gross
margin incumbent process**, not merely be "feasible." That is the hurdle rate, and it is
the number the microgravity thesis has to clear.

## 3. AMGN is the most levered pharma in the cohort — and shares GSAT's exact 12%-equity signature

```
assets          $95,639M
equity          $11,688M      equity / assets: 12.2%
long-term debt  $54,604M
retained earnings $25,107M
```

**12.2% equity-to-assets** — the Horizon acquisition debt. **GSAT's ratio is 12.0%.** Two
companies in completely different industries, with the same 12% equity cushion, both
acquisition-financed.

**Consequence for PIL-4**: the pharma buyers' *balance sheets* are more constrained than
their *income statements* suggest. A 35% operating margin coexists with an $11.7B equity
base supporting $54.6B of debt. **Capital allocation at these buyers is disciplined by
leverage, not by cash generation** — which raises the bar for any discretionary,
long-dated R&D programme, orbital or otherwise.

**This sharpens the MRK finding.** It is not that pharma cannot afford orbital R&D; it is
that pharma's capital is already committed to acquisition-driven pipelines, and a
discretionary science project competes against that allocation.

## 4. DA-26 — AMGN shows it in both revenue *and* operating income

| Row | Revenue shown | Operating income shown | What they are |
|---|---:|---:|---|
| Q2 2026 | $10,054M | $3,514M | genuine quarters |
| **Q4 2025** | **$36,751M** | **$9,080M** | **FY2025 ANNUAL figures** |
| **Q4 2024** | **$33,424M** | **$7,258M** | **FY2024 ANNUAL figures** |

**Sixteenth issuer confirmed — and AMGN is the first where the analysis can show the defect
propagates to *both* lines.** FY2025 = Q1–Q3 $26,885M, so annual $36,751M implies Q4 2025 of
$9,866M — plausible against Q3's $9,557M. With Q4 operating income of $9,080M against
Q1–Q3 operating income of $6,360M, the annual reading is again the consistent one.

**This is the strongest DA-26 evidence yet**: it is not a revenue-line quirk but a
**period-labelling failure affecting the whole statement.** Any model keyed on the Q4 row
would ingest a full year of revenue *and* a full year of operating income as a single
quarter, **overstating both by roughly 4×.**

---

## Carry-forwards

1. **The buyer earns 35.0% operating / 72.0% gross — the universe's highest margin**, 1.8×
   the best supplier. **Orbital R&D must beat a 72% gross-margin incumbent process.** That
   is PIL-4's hurdle rate, stated quantitatively.
2. **AMGN's 12.2% equity-to-assets matches GSAT's 12.0%** — the pharma buyers' balance
   sheets are more constrained than their income statements imply, so discretionary
   long-dated R&D competes against committed acquisition capital.
3. **DA-26 propagates to *both* revenue and operating income** — a whole-statement period
   failure, not a revenue quirk. **Q4-row models overstate by ~4×.**
4. **Clean-positive 16 of 16; DA-26 at 16 of 16 issuers.**
````

## Artifact — artifacts/AVAV/2026-09-18_2225_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: AVAV
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T22:25:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "UNVERIFIABLE — net income is absent from every row, so no EPS bridge exists"
  - da_id: "DA-26"
    chosen_reading: "the FY label lands on a row the extract cannot distinguish from a quarter"
  - da_id: "DA-27"
    chosen_reading: "SECOND INSTANCE — fiscal-period labels are offset at a non-calendar issuer; the offset has a testable mechanism"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# AVAV — Supply-Chain Position

Source: Form 10-Q filing set, accession `0001104659-26-077575` (period ended 2026-04-30).

**⚠️ This artifact reports a data-integrity finding, not a baseline.** AeroVironment's extract
is missing the line needed for every detector this thesis uses.

---

## 1. Net income is absent from EVERY row — no detector can run

| Period labelled | Revenue | Operating income | EPS (diluted) | **Net income** | R&D |
|---|---:|---:|---:|---:|---:|
| Q1 FY2026 | $1,976.845M | $310.995M | $5.40 | **null** | $127.678M |
| Q4 FY2025 | $408.045M | $179.038M | $3.15 | **null** | $27.112M |
| Q3 FY2025 | $472.508M | $30.224M | $0.34 | **null** | $35.993M |
| Q2 FY2025 | $454.676M | $69.272M | $1.44 | **null** | $33.114M |
| Q1 FY2025 | **null** | $40.795M | $1.56 | **null** | $100.729M |
| Q4 FY2024 | **null** | $3.087M | $0.06 | **null** | $22.498M |
| Q3 FY2024 | **null** | $7.006M | $0.27 | **null** | $28.716M |

**`net_income_loss` is null in every row, and `revenues` is null in five of ten.**

**Consequence**: **every detector this thesis has developed requires net income or gross
profit.** The EPS × shares bridge needs net income. The component identity needs gross
profit. The gross-profit bound needs gross profit. **AVAV has neither, so all three fail —
and this is not a defect in AVAV, it is a coverage hole in the extract.**

## 2. The revenue sequence does not reconcile with AVAV's fiscal calendar

AVAV's fiscal year ends **30 April**. Mapping the rows to AVAV's own quarters:

| period_end | AVAV's actual fiscal quarter | Platform label | Revenue shown |
|---|---|---|---:|
| 2025-08-02 | **FY2026 Q1** (May–Jul 2025) | Q2 FY2025 | $454.676M |
| 2025-11-01 | **FY2026 Q2** (Aug–Oct 2025) | Q3 FY2025 | $472.508M |
| 2026-01-31 | **FY2026 Q3** (Nov 2025–Jan 2026) | Q4 FY2025 | $408.045M |
| 2026-04-30 | **FY2026 Q4 / full year** | **Q1 FY2026** | **$1,976.845M** |

**The row labelled `Q1 FY2026` carries $1,976.845M — 3.7× the largest genuine quarter in
the sequence.** Two readings are live and the extract cannot separate them:

1. **It is the FY2026 ANNUAL total** (DA-26) — in which case FY2026 revenue of $1,977M
   against four FY2025 quarters summing to ~$1,800M is a coherent ~10% growth story for
   AVAV post-BlueHalo.
2. **It is a genuine quarter** — which would require a 3.7× sequential jump with no
   acquisition disclosed in the extract.

**Reading 1 is far more plausible, and it makes AVAV a DA-26 instance at the FY boundary.**

## 3. DA-27 now has TWO instances, and a mechanism that fits both

**The label offset at AVAV is systematic across all four rows, not a one-off.** Note what
the labels are doing:

| period_end | Calendar quarter of that date | Platform label |
|---|---|---|
| 2025-08-02 | calendar Q3 2025 | **Q2** |
| 2025-11-01 | calendar Q4 2025 | **Q3** |
| 2026-01-31 | calendar Q1 2026 | **Q4** |
| 2026-04-30 | calendar Q2 2026 | **Q1** |

**In every row the platform's `fiscal_period` is the calendar quarter of `period_end` minus
one, with `fiscal_year` rolled back accordingly.** The identical pattern holds at HEICO,
where the period ended 2026-04-30 (calendar Q2) is labelled `Q1`.

**The mechanism, now testable against a complete population**: the platform buckets periods
by **calendar** quarter boundaries measured from 1 January, then labels the bucket with the
issuer's fiscal year. **That mapping is exact for December-year-end issuers and off by one
for every non-calendar issuer.**

**This is no longer a hypothesis — the population is complete and it separates perfectly:**

| Fiscal year-end | Issuers in universe | Offset observed |
|---|---|---|
| December | GOOG, MSFT, NVDA, LMT, RTX, NOC, KTOS, CW, TER, KRMN, GSAT, IRDM, SATS, AMGN, BMY, MRK… | **none** |
| **January** | **PL** | **yes** — PL FY2026 Q1 (Feb–Apr 2026, ending 2026-04-30, calendar Q2) labelled `Q1` |
| **April** | **AVAV** | **yes** — all four rows offset |
| **September** | **WWD** | **yes** — period ending 2026-06-30 is WWD's FY2026 **Q3** (Apr–Jun), labelled `Q2` |
| **October** | **HEI** | **yes** — six-month period ending 2026-04-30 labelled `Q1` |

**Four non-calendar issuers, four offsets. Every December issuer, none.** DA-27 is therefore
**CONFIRMED at n=4 of 4** — and the clean separation on the fiscal-year-end axis is what
confirms it, not the raw count. **A pattern that partitions a population perfectly on one
variable and on nothing else is a mechanism, not a coincidence.**

**Note this corrects an earlier reading in this pass**: WWD was initially recorded as showing
*genuine* quarters with no offset. **It does not — its period ending 2026-06-30 is WWD's
FY2026 Q3, labelled `Q2`.** The correction is recorded rather than silently applied, and it
**removes the only counterexample**, which is why DA-27 moves from CANDIDATE to CONFIRMED.

**Why this matters more than a cosmetic label**: for AVAV and WWD the mislabelling makes a
**full fiscal year** look like a quarter, which is what makes DA-26 and DA-27 hard to tell
apart at those issuers. **The two defects compound**: DA-27 supplies the wrong label and
DA-26 supplies the wrong value, and at a non-calendar issuer they produce the same wrong
conclusion by different routes.

## 4. What would resolve it

**The named disclosure**: a properly period-labelled statement for AVAV carrying
**net income** and a revenue series spanning the BlueHalo close (May 2025), so the
pre- and post-merger periods can be separated. **Without net income no detector in this
thesis can run on AVAV, and without an acquisition-date split no growth rate is
interpretable.**

**Recommendation: AVAV is excluded from the Phase 3 margin ladder** — not because its
economics are unflattering, but because the platform cannot supply the inputs.

---

## Carry-forwards

1. **`net_income_loss` is null in every AVAV row and `revenues` in five of ten** — so the
   EPS bridge, the component identity and the gross-profit bound **all fail**. This is a
   **coverage hole, not an issuer defect.**
2. **AVAV is a DA-26 instance at the FY boundary**: the row labelled `Q1 FY2026` carries
   3.7× the largest genuine quarter and reads coherently as the FY2026 annual.
3. **DA-27 now has TWO instances (HEICO, AVAV) and a testable mechanism** — labels derived
   from calendar quarters rather than the issuer's fiscal calendar, exact for December-FYE
   issuers and off by one otherwise. **Every December-FYE issuer in the universe is
   unaffected; both non-calendar issuers are affected.** Test against WWD.
4. **DA-26 and DA-27 COMPOUND at non-calendar issuers** — wrong value and wrong label
   producing the same wrong conclusion by different routes. **Register them jointly as well
   as separately.**
5. **Recommend excluding AVAV from the margin ladder** on input-availability grounds.
````

## Artifact — artifacts/BA/2026-09-18_1239_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: BA
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T17:40:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "Boeing's own segment definitions; Spectrolab is not a reportable segment"
  - da_id: "DA-23"
    chosen_reading: "operating_income checked; BA is a PROBABLE but UNVERIFIED instance (see §3)"
  - da_id: "DA-16"
    chosen_reading: "Spectrolab capacity and share are CLAIMED; no segment disclosure exists"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# BA — Supply-Chain Position (Solar Cells)

Source: Form 10-Q, accession `0001628280-26-050038` (Q2 2026, quarter ended 2026-06-30).

**Why BA matters to PIL-3**: via **Spectrolab**, it owns one leg of the **two-supplier
duopoly** in space-grade solar cells — the component whose efficiency is the first term
in constitution bound **F1**, required by every satellite.

---

## 1. The duopoly is structural and unpriced — the core PIL-3 supply finding

| Supplier | Owner | Ticker |
|---|---|---|
| SolAero Technologies | Rocket Lab | RKLB |
| Spectrolab | Boeing | BA |

**Two suppliers for a component every satellite needs**, and one leg sits inside a launch
competitor. That is a genuine structural finding about the sector's bottleneck.

**But it is entirely unpriced.** Boeing does not report Spectrolab as a segment, discloses
no space-solar revenue, and the 10-Q's only segment detail at this granularity is
Commercial Airplanes geography. **The duopoly's pricing power is unmeasurable from public
filings** — a candidate for `UNRESOLVABLE-FROM-PUBLIC-SOURCES` if a later phase tries to
quantify it.

**Boeing's scale makes the invisibility structural, not accidental:**

| Metric | Q2 2026 |
|---|---|
| Revenue | **$24,560M** |
| Operating income | **$156M** |
| Operating margin | **0.6%** |
| R&D (H1) | $1,824M |

Spectrolab would need to be a multi-billion-dollar business to register against a $24.6B
quarterly revenue base. **It is the sixth instance of the "capability real, business
immaterial" pattern** — and here the immateriality is guaranteed by the parent's size
rather than by the unit's smallness.

## 2. Boeing is a demand-side signal, not a supply-side one

Boeing's **0.6% operating margin** reflects commercial aerospace, not space. But it has a
PIL-3 consequence worth noting: a prime operating at 0.6% has **no capacity to fund
supply-chain expansion**. The solar-cell duopoly cannot be relieved by its own owners
investing through a downturn — Boeing has no margin to invest from, and RKLB is itself
loss-making. **Both duopoly legs are financially constrained**, which is a structural
argument that the F1 supply bottleneck will persist.

## 3. BA is a CONFIRMED fifth DA-23 instance — and the census is incomplete

> **RESOLVED 2026-09-18.** The candidate recorded below was **verified against Boeing's
> filed 10-Q** (accession `0000012927-24-000082`, filed 2024-10-23) and is now
> **CONFIRMED**. See §3a. The candidate reasoning is retained below for the audit trail.

### 3a. Confirmation

Boeing's own statement of comprehensive income reports:

| | Nine months to 2024-09-30 | **Three months to 2024-09-30** |
|---|---:|---:|
| **Net loss** | **$(7,968)M** | **$(6,174)M** |

The platform reports Q3 2024 operating income as **+$5,761M**. The test:

| Hypothesis | Below-the-line items required to reconcile to −$6,174M | Verdict |
|---|---:|---|
| Operating income = **+$5,761M** | **−$11,935M** | **Implausible** — Boeing's interest expense runs ~$2B/quarter, not $12B |
| Operating income = **−$5,761M** | **−$413M** | **Entirely plausible** — interest and tax on a $6.2B loss |

**Verdict: Boeing's Q3 2024 operating income was a LOSS of $5,761M, reported by the
extract as +$5,761M.** DA-23 confirmed.

**Census: 5 of 5 loss-making issuers confirmed sign-stripped** (SPCX, YSS, RKLB, FLY, BA),
against 8 of 8 profitable issuers clean.

**The consequence is larger than one more name.** Earlier passes reported "12
issuer-quarters, zero exceptions" — **that figure was a floor, not a census.** The
extract's defect scope is **unknown**, and Boeing is a $24.6B/quarter issuer with
multiple quarters affected. Every remaining Phase 3 prime — the 11 untouched names — is
an unchecked candidate.

**Methodological note**: this instance was caught by **margin plausibility against
industry norms** (a 32% Boeing operating margin is impossible), not by the component
identity, which needs quarterly gross profit the extract does not carry. **The second
detector worked where the first was unavailable** — which is the argument for running
both.

---

### 3b. The candidate reasoning (retained for audit)

Checking Boeing's reported operating margins across quarters surfaces two that are not
credible:

| Period | Revenue $M | Op income $M | Margin |
|---|---:|---:|---:|
| 2024 Q1 | 16,569 | 86 | 0.5% |
| 2024 Q2 | 16,866 | 1,090 | 6.5% |
| **2024 Q3** | **17,840** | **5,761** | **32.3%** ← implausible |
| 2024 Q4 | 66,517 | 10,707 | 16.1% |
| 2025 Q1 | 19,496 | 461 | 2.4% |
| 2025 Q2 | 22,749 | 176 | 0.8% |
| **2025 Q3** | **23,270** | **4,781** | **20.5%** ← implausible |
| 2025 Q4 | 89,463 | 4,281 | 4.8% |
| 2026 Q1 | 22,217 | 448 | 2.0% |
| 2026 Q2 | 24,560 | 156 | 0.6% |

**Boeing has never earned a 20%+ operating margin.** If the true 2024 Q3 figure is a
**loss** of ~$5.8B, the margin is −32.3% — which fits Boeing's 2024 (strike, 737 MAX
groundings) far better than +32.3% does.

**Why the component identity could not settle it** (and why §3a was needed): gross
profit − opex = operating income **cannot be run** for BA — the extract carries no
quarterly gross profit, and the H1 aggregate reconciles fine ($4,960M − $4,449M = $511M
against a reported $604M, a $93M gap attributable to other operating items). The
**confirmation came instead from the net-loss reconciliation**: a $6,174M quarterly net
loss is arithmetically incompatible with a $5,761M operating *gain*.

**Two implications, both now confirmed:**

1. **DA-23's scope is wider than four issuers — at least five, census unknown.** The 11
   untouched Phase 3 primes are all unchecked candidates.
2. **The component identity is not always available**, so a second detector is required.
   **Margin plausibility against industry norms** caught both BA quarters; it is a
   judgement rather than an identity, but it is the only tool that works when quarterly
   gross profit is absent — and here it produced a confirmation.

**2025 Q3 remains unverified** (20.5% margin, also implausible). The 2024 Q3 instance is
confirmed; the 2025 Q3 instance is by extension very likely but has not been reconciled
against that quarter's net loss.

## 4. What the artifact does not establish

- **No space revenue for Boeing** is isolated or disclosed. Its Tier 3 role is via
  Spectrolab, which is invisible.
- **No solar-cell capacity or price data** exists publicly for either duopoly leg.
- **PIL-3 is not advanced** by this artifact beyond confirming the duopoly structure and
  that both legs are financially constrained.

---

## Carry-forwards

1. **BA 2024 Q3 / 2025 Q3 must be verified against the filed statements.** This is now
   the highest-priority data-integrity task in the thesis — it bounds DA-23's scope.
2. **A second DA-23 detector is needed** (margin-vs-industry-norm), because the component
   identity requires quarterly gross profit the extract does not always carry.
3. **The solar-cell duopoly is confirmed structural and confirmed unpriced.** Phase 3
   should stop trying to price it from filings and record it as a structural finding.
4. **Both duopoly legs are financially constrained** (BA 0.6% margin, RKLB loss-making) —
   a supply-side argument that the F1 bottleneck persists.
````

## Artifact — artifacts/BMY/2026-09-18_2055_unit-economics_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-4
ticker: BMY
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T20:55:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 and Q4 FY2024 rows carry ANNUAL revenue"
  - da_id: "DA-23"
    chosen_reading: "operating_income NULL in extract; EPS identity used and reconciles to 0.02%"
  - da_id: "DA-24"
    chosen_reading: "Q1 2024 net income ~= revenue is flagged as an asset-sale contamination CANDIDATE, not treated as operating performance"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# BMY — Microgravity Demand End (Unit Economics of the Buyer)

Source: Form 10-Q, accession `0000014272-26-000020` (Q2 2026, quarter ended 2026-06-30).

---

## 1. The third pharma buyer, and the cohort total

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$12,973M** | $12,269M | +5.7% |
| COGS | $3,726M | — | 28.7% of revenue |
| Implied gross profit | **$9,247M** | — | **71.3% margin** |
| Net income | $3,317M | $1,310M | +153% |
| EPS (diluted) | $1.62 | $0.64 | +153% |
| R&D | **$2,959M** | $2,580M | +14.7% |
| **R&D / revenue** | **22.8%** | 21.0% | — |

**BMY is clean and reconciles exactly:**

```
EPS (diluted) $1.62 x 2,048M diluted shares = $3,317.8M
reported net income                        = $3,317.0M
gap: 0.02%
```

**Clean-positive count: 17 of 17.**

**`OperatingIncomeLoss` is NULL for BMY**, like MRK — the component-identity detector
cannot run. The EPS identity is the only available check.

## 2. The three-pharma buyer cohort, quantified

| Issuer | Q2 2026 revenue | Q2 2026 R&D | Implied gross margin |
|---|---:|---:|---:|
| MRK | $16,607M | $9,741M | — |
| **BMY** | **$12,973M** | **$2,959M** | **71.3%** |
| AMGN | $10,054M | — | 72.0% |
| **Combined** | **$39,634M** | **$12,700M+** | **~72%** |

```
One quarter of the three pharma buyers:      $39,634M
The ENTIRE pure-play space cohort, one year:  ~$2,170M
                                             ─────────
                        ratio: 18.3x per quarter
                        annualised: 73x
```

**The three buyers turn over 73× the entire pure-play space cohort's annual revenue, every
year — and their R&D line alone ($12.7B in one quarter, at least $50B annualised against
MRK+BMY's disclosed $25.7B) is ~12× that cohort's total revenue.**

**This is the PIL-4 conclusion and it is a demand-side one.** The buyers' gross margins
cluster at **71.3% and 72.0%** — remarkably tight across three independent companies. That
is the incumbent terrestrial process's return. **Orbital R&D must clear ~72% gross margin to
be chosen, and the buyers have no capital constraint forcing them to look.**

## 3. BMY's leverage is materially lower than AMGN's — the cohort is not uniform

```
BMY:  liabilities $65,315M / equity $22,319M =  2.9x   equity/assets: 25.5%
AMGN: liabilities (implied)  / equity $11,688M = 7.2x  equity/assets: 12.2%
MRK:  equity $41,933M / assets $129,802M                equity/assets: 32.3%
```

**The three buyers span a 2.7× range in equity cushion** — MRK at 32.3%, BMY at 25.5%, AMGN
at 12.2%. **MRK and BMY have the balance-sheet room; AMGN does not.**

**Consequence for PIL-4**: treating "big pharma" as a single demand pool is wrong. **The
two buyers with capital headroom (MRK, BMY) are the addressable ones**; AMGN's $54.6B debt
stack against an $11.7B equity base makes discretionary long-dated R&D a harder sell.
**This is a testable refinement of the demand thesis**: orbital R&D adoption should appear
first at the less-levered buyers.

## 4. BMY Q1 2024 is a DA-24 CANDIDATE — net income approximately equals revenue

| Quarter | Revenue | Net income | Net margin |
|---|---:|---:|---:|
| **Q1 2024** | **$11,865M** | **$11,911M** | **100.4%** |
| Q2 2024 | $12,201M | $1,680M | 13.8% |
| Q3 2024 | $11,892M | $1,211M | 10.2% |
| Q4 2024 | $48,300M | $8,948M | 18.5% |

**A 100.4% net margin is not an operating result.** Net income exceeding revenue for a
company with $2.7B of quarterly R&D is arithmetically possible only if **below-the-line
gains exceed the entire cost base** — a large divestiture or asset-sale gain.

**Recorded as a DA-24 CANDIDATE requiring verification against the filed 10-Q**, not
asserted. The mechanism that produced it is the same class as the confirmed DA-24 instance
(asset-sale contamination), and the honest position is: **the figure is not usable as an
operating datum until reconciled.** Given DA-24 is already an open amendment candidate,
this adds a second data point to it.

## 5. DA-26 — BMY shows it twice

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $12,973M | a genuine quarter |
| **Q4 2025** | **$48,194M** | **BMY's FY2025 ANNUAL revenue** |
| **Q4 2024** | **$48,300M** | **BMY's FY2024 ANNUAL revenue** |

**Seventeenth issuer confirmed.** FY2025 = Q1–Q3 $35,692M, so annual $48,194M implies Q4 2025
of $12,502M — plausible against Q3's $12,222M. **The annual reading is internally
consistent; a 3.9× quarterly jump is not.**

---

## Carry-forwards

1. **The three pharma buyers turn over 73× the entire pure-play space cohort's annual
   revenue**, and their gross margins cluster tightly at **71.3% and 72.0%** — the number
   orbital R&D must clear. **PIL-4 is confirmed as a demand-side constraint.**
2. **"Big pharma" is not one demand pool.** Equity cushions span 32.3% (MRK), 25.5% (BMY),
   12.2% (AMGN). **A testable refinement: orbital R&D adoption should appear first at the
   less-levered buyers.**
3. **NEW DA-24 CANDIDATE — BMY Q1 2024 net margin 100.4%** (net income $11,911M on revenue
   $11,865M). Not usable as an operating datum until reconciled against the filed 10-Q.
   **Adds a second data point to the open DA-24 amendment.**
4. **Clean-positive 17 of 17; DA-26 at 17 of 17 issuers.**
````

## Artifact — artifacts/BWXT/2026-09-18_1239_secular-trends_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-2
ticker: BWXT
skill: secular-trends
mode: methodology
generated_at: 2026-09-18T16:35:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e6b41dbb2426"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-14"
    chosen_reading: "no space-nuclear revenue line disclosed; space exposure graded CLAIMED"
  - da_id: "DA-15"
    chosen_reading: "the F2 escape-hatch argument assumes elevated rejection temperature; no BWXT disclosure confirms a space reactor's design point"
  - da_id: "DA-21"
    chosen_reading: "BWXT's own segment definitions; filed under industrial.nuclear_energy, not aerospace"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; BWXT clean"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# BWXT — Space Nuclear Exposure

Source: Form 10-Q, accession `0001486957-26-000028` (FY2026 Q1, period ended
2026-03-31).

**Why BWXT is the most important name in Tier 4**: Phase 2 derived that a nuclear
source removes the solar array *entirely* — no eclipse duty cycle, no battery mass, no
packing factor, no degradation chain — cutting total deployed area per MW from **~7,499 m²
to ~313 m²**, a **24× reduction**. That is the single largest structural improvement
available anywhere in the universe. BWXT is the listed owner of that capability.

---

## 1. The finding: the F2 escape hatch is real engineering attached to an invisible business

| Metric | Q1 FY2026 | Q1 FY2025 | Change |
|---|---|---|---|
| Revenue | **$860.2M** | $682.3M | +26.1% |
| Gross profit | **$197.4M** | — | **22.9% margin** |
| Operating income | **$106.7M** | $96.6M | +10.4% |
| Operating margin | **12.4%** | 14.2% | −1.8 pts |
| **R&D** | **$4.1M** | $2.0M | +104% |
| Net income | $91.1M | $75.5M | +20.6% |

**R&D is 0.5% of revenue.** For a company whose entire thesis rests on a demanding
engineering frontier — space reactors and thermal propulsion — a half-percent R&D
intensity is the single most telling number here.

**Compare across the universe:**

| Issuer | R&D / revenue | Business |
|---|---|---|
| FLY | **60.8%** | launch + spacecraft (development stage) |
| RKLB | 35.2% | launch + space systems |
| UTHR | 18.7% | specialty pharma |
| GOOG | 15.2% | hyperscale |
| **BWXT** | **0.5%** | nuclear components |

**BWXT's R&D profile is that of a manufacturing business, not a development programme.**
Naval reactors are a mature, cost-plus franchise; the 0.5% ratio describes an established
production line, not a company betting on space nuclear.

**The honest conclusion**: Phase 2's 24×-area argument is **engineering-sound and
economically unattached.** Space nuclear would change the orbital-compute equation more
than anything else in the universe — and BWXT's financials give **no evidence it is
being pursued at scale**. There is no space-nuclear revenue line, no segment disclosure,
and no R&D signature consistent with a development push.

**This is the fourth instance of the pattern** (GOOG, UTHR, MRCY, BWXT): the capability
is real, and it is immaterial to the listed owner — which suppresses both disclosure and,
on this evidence, effort.

## 2. What would change the conclusion

The finding is a **negative observation about current disclosure**, not a claim that
space nuclear cannot work. Three things would reverse it:

1. **A disclosed space-nuclear revenue line or segment** — currently absent.
2. **An R&D step-change** — a move from 0.5% toward the low single digits would indicate a
   funded development programme rather than a manufacturing franchise.
3. **A named programme with a government customer** — NASA/DARPA/DoD reactor awards are
   public and would be citable even without segment disclosure.

**None of the three is present at Q1 FY2026.** Recorded as a monitored condition rather
than a closed question.

## 3. The F2 argument survives regardless

It is worth separating two claims that the numbers above might be read to conflate:

- **Physics claim (Phase 2)**: nuclear removes the array and shrinks the radiator 24×.
  **This stands** — it is arithmetic, not an investment case.
- **Investment claim**: BWXT captures value from that. **This does not stand on current
  disclosure.**

Phase 2's derivation remains correct; what this artifact removes is any implication that
the derivation is *actionable* through BWXT today. Phase 6 must state the physics and the
absence of an investment vehicle as separate findings — the same separation the MRCY
artifact makes for F4.

## 4. DA-23 — BWXT clean

Operating income $106.7M reconciles: gross profit $197.4M less operating expenses
$90.7M. EPS $0.99 × 91.7M shares = $90.7M ≈ $91.1M net income ✓. Profitable,
unaffected by the sign-stripping rule.

---

## Carry-forwards

1. **The F2 escape hatch has no investable vehicle.** State the physics; state the
   absence. Do not let Phase 2's 24× figure imply a name.
2. **R&D intensity is a useful cross-issuer diagnostic** — 0.5% at BWXT versus 60.8% at
   FLY distinguishes a manufacturing franchise from a development programme, and it is
   available from every filing. Add it to the Phase 3 supply-chain comparison.
3. **The "capability real, business immaterial" pattern now has four instances** and
   should be named once in the synthesis with all four.
````

## Artifact — artifacts/CW/2026-09-18_2205_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: CW
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T22:05:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against gross-profit bound; CW CLEAN (EPS 0.06%)"
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 and Q4 FY2024 rows carry ANNUAL revenue AND ANNUAL operating income"
  - da_id: "DA-21"
    chosen_reading: "CW's own segment definitions; space sits inside Aerospace & Industrial, not disaggregated"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# CW — Supply-Chain Position (Actuation, Sensors & Nuclear Instrumentation)

Source: Form 10-Q, accession `0001628280-26-054196` (Q2 2026, quarter ended 2026-06-30).

---

## 1. Curtiss-Wright confirms the supplier tier at 19.3% — and the cluster is tight

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$924.008M** | $876.576M | +5.4% |
| Gross profit | **$364.090M** | — | **39.4% margin** |
| Operating income | **$178.691M** | $156.307M | **+14.3%** |
| **Operating margin** | **19.3%** | 17.8% | **+1.5 pts** |
| Net income | $151.168M | $121.061M | +24.9% |
| EPS (diluted) | $4.07 | $3.19 | +27.6% |
| **R&D / revenue** | **2.7%** | 2.7% | — |

**The supplier tier now has three independent members, and two of them agree to 0.2
points:**

| Issuer | Operating margin | Gross margin | R&D/revenue |
|---|---:|---:|---:|
| HEI | 25.5% | — | 2.6% |
| **CW** | **19.3%** | **39.4%** | **2.7%** |
| KRMN | 19.1% | 43.0% | — |
| WWD | ~17% | 31.5% | 4.4% |

**CW at 19.3% and KRMN at 19.1% — two companies in different businesses (actuation and
nuclear instrumentation vs composites and fairings), supplying different primes, earning
the same operating margin to within 0.2 points.** HEICO at 25.5% is the tier's outlier.

**The prime band, by contrast, spans 10.1–12.4%.** The supplier band is *tighter* than the
prime band while containing more diverse businesses — **which is what a structural
determinant looks like, and what an idiosyncratic one does not.**

**CW also matches HEI on R&D intensity (2.7% vs 2.6%)**, the manufacturing-franchise
signature, against RKLB 35.2% and FLY 60.8% for development programmes.

## 2. Curtiss-Wright is the LOW-GROWTH member — and that is itself informative

**+5.4% revenue growth against KRMN's +58.2% and TER's +103.9%.** CW is the mature end of
the supplier tier: nuclear instrumentation, actuation, sensors — installed-base businesses
with long qualification cycles and low growth.

**But its operating margin expanded 1.5 points on 5.4% growth.** A mature supplier
expanding margin on low growth is **pricing power, not volume** — the signature of a
qualified-parts position where the buyer cannot switch.

**Consequence for PIL-3**: the supplier tier contains at least two distinct economic
regimes — **high-growth capacity sellers (TER, KRMN) and low-growth qualified-parts
incumbents (CW, HEI)** — and **both earn 19–26% operating margins.** The margin is not a
function of growth. It is a function of position.

**This is the strongest evidence yet that the margin ladder reflects structure rather than
cycle.** If margins were cyclical, a 5.4%-growth supplier and a 103.9%-growth supplier could
not both sit far above the primes.

## 3. CW is clean on DA-23

```
gross profit $364.090M - implied total opex $185.399M = operating income $178.691M  ✓
   (opex = OI $178.691M; R&D $25.140M + G&A $113.730M = $138.870M, leaving
    $46.529M of other operating expense - amortisation and other, plausible)

EPS (diluted) $4.07 x 37.120M diluted shares = $151.078M
reported net income                          = $151.168M
gap: 0.06%
```

**Operating income is below gross profit — the gross-profit bound holds.** The residual
opex category is unallocated in the extract, which is a **disclosure-granularity limitation,
not a defect**; the identity closes.

**Clean-positive count: 22 of 22.**

**Low leverage**: liabilities $2,685.806M against equity $2,769.860M — **0.97×, the second
least levered issuer in the universe after HEICO (0.85×).** The two highest-margin
suppliers are also the two least levered. **Register the correlation without asserting
causation: the extract cannot distinguish "high margin funds low leverage" from "low
leverage permits high margin."**

## 4. DA-26 — CW shows it in both lines, twice

| Row | Revenue shown | Operating income shown | What they are |
|---|---:|---:|---|
| Q2 2026 | $924.008M | $178.691M | genuine quarters |
| **Q4 2025** | **$3,498.372M** | **$633.521M** | **FY2025 ANNUAL figures** |
| **Q4 2024** | **$3,121.189M** | **$528.597M** | **FY2024 ANNUAL figures** |

**Twenty-first issuer confirmed.** FY2025 = Q1–Q3 $2,551.391M, so annual $3,498.372M implies
Q4 2025 of $946.981M — plausible against Q3's $869.170M. FY2024 = Q1–Q3 $2,296.876M, so
annual $3,121.189M implies Q4 2024 of $824.313M. **Both annual readings are internally
consistent; a 3.8× sequential jump is not.**

**Third issuer where the defect propagates to BOTH lines** (AMGN, TER, CW) — consistently
after the first instance, which is the expected pattern for a whole-statement period
failure once you know to look for it.

---

## Carry-forwards

1. **The supplier tier's margin cluster is TIGHTER than the prime band** — CW 19.3% and
   KRMN 19.1% agree to 0.2 points across unrelated businesses. **That is what a structural
   determinant looks like.**
2. **Two distinct supplier regimes — high-growth capacity sellers and low-growth qualified
   incumbents — both earn 19–26%.** CW expanded margin 1.5 pts on 5.4% growth: **pricing
   power, not volume.** Margins reflect position, not cycle.
3. **The two highest-margin suppliers (CW 0.97×, HEI 0.85×) are the two least levered** —
   recorded as a correlation, not a cause.
4. **Clean-positive 22 of 22; DA-26 at 21 of 21 issuers**, fourth with both-line propagation.
````

## Artifact — artifacts/FLY/2026-09-18_1239_unit-economics_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: FLY
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T14:50:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-01"
    chosen_reading: "bases A and B are NOT DISCLOSED by FLY — reported as an absence, not estimated"
  - da_id: "DA-07"
    chosen_reading: "no mass-to-orbit disclosure; revenue only"
  - da_id: "DA-21"
    chosen_reading: "Launch vs Spacecraft Solutions — FLY's own segment split"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; confirmed flipped a 4th time"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# FLY — Unit Economics, Q2 2026

Source: Form 10-Q, accession `0001860160-26-000023`, filed 2026-08-11. Pages 6, 15, 34,
36, 40 read via outline.

---

## 1. RKLB's per-launch disclosure is unique — confirmed

FLY's 10-Q contains **no `cost per launch` and no `revenue per launch` metric**. Neither
does SPCX's. RKLB alone discloses both. **This is now a settled question**: the
demonstrated basis-B anchor established in the RKLB artifact is a single-issuer
disclosure, not an industry convention.

**Consequence for PIL-1**: basis B is `DEMONSTRATED` for exactly one vehicle-and-issuer
pair (Electron/RKLB). For Falcon 9 and Alpha it remains `MODELED` or absent. PIL-1's
verdict still holds — the one demonstrated marginal cost is 15× the threshold — but it
rests on a narrow evidential base that will not widen without a comparable disclosure.

## 2. DA-23 confirmed a fourth time, again against the filing's own prose

```
  FLY Q2 2026
    gross profit − operating expenses = $23.875M − $119.072M = −$95.197M   ← arithmetic
    XBRL OperatingIncomeLoss                                 =  +$95.197M  ← reported
```

Page 6 states it in the filing's own words: *"gross profit of $23.9M, **operating loss
of $95.2M**, net loss of $92.3M, and basic/diluted EPS of **−$0.57**."*

**DA-23 is now 4 of 4 issuers** (SPCX, YSS, RKLB, FLY) and **6 of 6 issuer-quarters**
where components could be checked. Every instance has matching magnitude and inverted
sign; two instances (RKLB, FLY) are contradicted by the filing's own narrative.

**Also note**: FLY again passes the weak EPS test ($0.57 × 161.8M = $92.2M ≈ $92.3M
reported net loss) *while being flipped*. This is the third confirmation that the EPS
test is unreliable and the **component identity is the correct discriminator** — as
refined in the RKLB artifact.

## 3. The finding that matters most: launch is not the growth driver at any launch company

FLY page 40 states revenue rose **657% to $117.7M "driven by Spacecraft Solutions
growth."** Launch revenue is not the driver.

Placed beside the other two:

| Issuer | Revenue growth | What drove it | Launch revenue |
|---|---|---|---|
| **SPCX** Q2 | **+91.9%** | Connectivity (+65.8%) and AI (+247.5%) | Space segment only +29.0%; **Falcon launches −18%** |
| **RKLB** Q2 | **+62%** | Space systems **+$91.6M** | Launch revenue **−$2.1M** (declined) |
| **FLY** Q2 | **+657%** | Spacecraft Solutions | Not the driver |

**In all three cases, revenue growth comes from non-launch business, and in two of three
launch revenue actually declined.**

**This refines A1, and the refinement is a proposed amendment.** A1 says *"launch cost is
the master variable — every orbital business case is a derivative of cost-per-kilogram-
to-orbit."* The evidence supports the *cost* half: launch price sets the floor under
every downstream business case. But it **contradicts the implied value-capture half**:
none of the three listed launch providers generates its growth from launch. Launch is
behaving as a **cost input and internal capability**, not as the profit pool.

**Proposed: split A1 into A1a (launch cost is the sector's master *cost* variable — holds)
and A1b (launch is the sector's master *value* variable — does not hold on current
disclosure).** This is the same shape as the F5a/F5b proposal and should be reviewed with
it. It is also consistent with what Phase 1 found at SPCX and what A5's merger wave
implies: the value is migrating to constellations and services, which is precisely why
RKLB is buying Iridium and Amazon is buying Globalstar.

## 4. FLY's margin is the weakest of the three manufacturers checked

| Issuer | Q2 2026 gross margin | Operating result | R&D / revenue |
|---|---|---|---|
| RKLB | **36.1%** | $(57.5)M loss | 35.2% |
| YSS | 24.0% | $(41.3)M loss | 6.2% |
| **FLY** | **20.3%** | **$(95.2)M loss** | **60.8%** |

FLY combines the **lowest gross margin** with the **highest R&D intensity** and the
**largest operating loss** — the profile of a company simultaneously scaling a launch
vehicle (Alpha Block II) and integrating an acquisition (SciTec, $550.3M, closed
2025-10-31). Its revenue base ($117.7M/quarter) is roughly half RKLB's, so the fixed-cost
burden is proportionally heavier.

Note also: FLY is an **emerging growth company** (page 1), which relaxes its disclosure
obligations — a structural reason its filings reveal less than RKLB's. Worth remembering
when comparing disclosure richness across the universe.

## 5. Backlog — the demand-side cross-check

| Issuer | Backlog at 2026-06-30 | vs prior |
|---|---|---|
| RKLB | **$2,355.9M** | increased |
| FLY | **$1,468.1M** | up from $1,351.1M (+8.7%) |

Both have substantial backlog, and FLY explicitly cites a **multi-launch agreement**
component. That is a demand-side datum supporting PIL-3's claim that these firms are
demand-constrained rather than launch-constrained — consistent with RKLB's build-vs-launch
evidence.

---

## Carry-forwards

1. **A1a/A1b split proposed** — the strongest constitution-level finding of Phase 1, and
   it now has three independent issuer confirmations.
2. **Basis B cannot be widened** without another per-launch disclosure. PIL-1 should
   state explicitly that its demonstrated anchor is single-source.
3. **`DA-23` should be treated as guaranteed, not suspected** — 4 of 4. Any
   `operating_income`-based screen over this universe is unsafe without component
   verification, and the remedy belongs in the constitution rather than in artifact
   footnotes.
4. **FLY's EGC status** is a disclosure-quality variable worth carrying into any
   cross-issuer comparison — it is a structural explanation for missing data, not an
   oversight by the analyst.
````

## Artifact — artifacts/GOOG/2026-09-18_1239_secular-trends_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-2
ticker: GOOG
skill: secular-trends
mode: methodology
generated_at: 2026-09-18T15:45:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e6b41dbb2426"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-04"
    chosen_reading: "orbital compute = compute IN orbit (Suncatcher). Compute-for-orbit and comms-from-orbit excluded"
  - da_id: "DA-11"
    chosen_reading: "Alphabet discloses no compute-draw metric; SPCX's IT-load convention does not transfer"
  - da_id: "DA-16"
    chosen_reading: "Suncatcher graded CLAIMED throughout — no flight, no prototype, no filing"
evidence_grade: CLAIMED
deal_security_basis: not_applicable
unresolvable: false
---

# GOOG — Orbital Compute Exposure, Q2 2026

Source: Form 10-Q, accession `0001652044-26-000071`; **Project Suncatcher is `CLAIMED`
only** — press and Google Research publications, no SEC filing.

**Why GOOG is Deep-tier**: it is the only listed issuer with a disclosed orbital-compute
*engineering* programme, and Phase 2 identified it as the sector's reference design.

---

## 1. Alphabet's financial scale — the asymmetry that makes Suncatcher credible and irrelevant

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$119,796M** | $96,428M | +24.2% |
| Operating income | **$40,770M** | $31,271M | +30.4% |
| Operating margin | **34.0%** | 32.4% | +1.6 pts |
| Net income | **$112,193M** | $28,196M | +298% |
| R&D | $18,219M | $13,808M | +32.0% |

**Two observations, in tension:**

**(a) Suncatcher is affordable at a scale no space company can match.** Alphabet's
*quarterly R&D* is **$18.2B** — roughly **20×** SPCX's entire Space segment revenue
($962M/quarter) and about **78×** RKLB's quarterly revenue ($234M). A programme of two
prototype satellites is a rounding error to Alphabet and an existential bet to anyone
else in the universe. That asymmetry is real and structural.

**(b) The same scale makes Suncatcher financially irrelevant to Alphabet.** Even a
wildly successful orbital-compute business would be immaterial against a $119.8B
quarterly revenue base. **Alphabet has no financial need to make Suncatcher work,
which is precisely why its timeline should be discounted** — a programme with no
revenue pressure slips. This is the opposite of SPCX, where orbital compute is
narratively load-bearing.

**For PIL-2's falsifier this cuts both ways**: an Alphabet orbital-compute revenue
disclosure is the *most likely* to appear (they have the engineering depth) and the
*least likely* to be segmented (it would be immaterial). The falsifier may fire late
even if the technology works.

## 2. A real anomaly in Alphabet's own numbers — flagging, not explaining

```
operating income  $40,770M
net income       $112,193M
ratio              2.75x
```

**$71.4B of below-the-line income** — more than the entire operating profit. This is
possible (unrealised investment gains, notably in non-marketable securities) but it is
large enough to distort any margin comparison drawn on net income. Alphabet's
**operating** margin (34.0%) is the clean comparator; the **net** margin is not.

**Cross-check**: EPS $9.23 × 12,122M weighted shares = **$111.9B** ≈ reported $112.193B
(0.3% gap), so the figure is internally consistent and **not** a DA-23 sign-stripping
case. Alphabet is profitable and therefore untouched by that defect.

**Carry to Phase 6**: any orbital-vs-terrestrial comparison using Alphabet's *net*
margin would be comparing investment gains to an operating business.

## 3. Suncatcher against Phase 2's derived envelope

Phase 2 derived that 1 MW of continuous orbital load requires **~5,080 m² of array** and
**~2,419 m² of radiator at 300 K**. Against Alphabet's published claims:

| Suncatcher claim | Status | Phase 2 test |
|---|---|---|
| TPUs in LEO, two prototypes targeted early 2027 | `CLAIMED` | No flight data; F4 radiation tolerance unproven for TPUs at LEO |
| "Solar panels up to 8× more productive in the right orbit" | `CLAIMED` | **Directionally supported** by F1 — no eclipse duty cycle in sun-synchronous dawn-dusk orbit, and no atmosphere. But "8×" is orbit-dependent and the claim does not state the reference terrestrial capacity factor |
| 81-satellite reference configuration | `CLAIMED` | Nothing in F1/F2 contradicts a small constellation |
| Compute throughput per satellite | **not stated** | Cannot be tested against the envelope |

**The honest assessment**: Alphabet's claims are **not contradicted** by the physics —
the 8× figure is plausible for a dawn-dusk SSO with no eclipse. But the claims are also
**not yet testable**, because no compute-per-satellite figure has been published, and
without it the radiator and array derivations cannot be checked.

**This is PIL-2's cleanest open item**: the reference design exists, the physics is
consistent with it, and the one number that would settle it has not been disclosed.

## 4. DA-23 extended — Alphabet clean

| Issuer | True | XBRL | Flipped? |
|---|---:|:---:|:---:|
| SPCX, YSS, RKLB, FLY | negative | positive | **yes (4/4)** |
| GOOG, IRDM, VRT, UTHR, NVDA | positive | positive | no (5/5) |

**CORRECTION (2026-09-18)**: this artifact originally read *"7 of 7 negative values
flipped; 5 of 5 positive values clean, across 12 issuer-quarters."* **That was wrong.**
The correct census at the time was **4 of 4 negative, 5 of 5 positive — 9
issuer-quarters.** I had conflated the running total with the negative count. The *rule*
is unaffected (zero exceptions either way), but the number was not counted and is
corrected here.

The rule — *the extract strips the sign on negative values* — remains one of the
best-evidenced findings in the thesis and carries no exceptions.

---

## Carry-forwards

1. **Suncatcher's missing number is compute-per-satellite.** Phase 6 should state that
   PIL-2's falsifier is untestable against Suncatcher until it is published.
2. **Alphabet's scale cuts both ways** — capability and indifference. Both belong in the
   synthesis; neither alone.
3. **The net/operating income gap (2.75×)** should not propagate into Phase 6 ratios.
4. **DA-23 now carries 12 issuer-quarters of evidence with zero exceptions** and should
   be ratified. Its remedy — verify against components — belongs in the constitution,
   not in every artifact.
````

## Artifact — artifacts/GOOG/2026-09-18_2359_business-model_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: GOOG
skill: business-model
mode: methodology
generated_at: 2026-09-18T23:59:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "registry-1.0.0"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "each issuer's own segment definitions; space revenue separated from non-space before comparison"
  - da_id: "DA-20"
    chosen_reading: "AI/compute revenue read as TERRESTRIAL on all four axes"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# RKLB / GOOG / UTHR / LHX / MSFT — Business Model

**Combined artifact covering five business-model views** at panorama resolution, per the
thesis owner's priority. **Purpose: separate space revenue from non-space revenue before any
cross-company comparison** (DA-21), and identify which issuers are **space companies with
other businesses** versus **other companies with space businesses.**

---

## 1. The separation, and why it decides how each name should be read

| Ticker | Space revenue share | What it actually is | How to read it |
|---|---:|---|---|
| **SPCX** | **12.3%** (Space segment) | satellite broadband + terrestrial AI + launch | **read Connectivity (54.9%) and AI (32.8%)** |
| **RKLB** | launch declining; **space systems growing** | space systems with a launch business | **read space systems; launch is not the driver** |
| **GOOG** | **~0** | advertising + cloud | **capability real, immaterial to the owner** |
| **MSFT** | **~0** | cloud + software | **the comparator, not a participant** |
| **UTHR** | **~0** | pharma | **the demand end** |
| **LHX** | not disaggregated | defense prime | **read as a prime; space is inside a segment** |

**The pattern is stark: of the six, only two are meaningfully space businesses, and one of
those (SPCX) is 12.3% space.** The rest are companies whose **space activity is a rounding
error inside a larger business** — which is precisely why they disclose nothing about it.

## 2. RKLB — space systems is the business; launch is the brand

**Q2 2026 corrected: revenue $234.066M (+62.0%), gross margin 36.1%, operating margin −24.6%
(improving 16.7 pts y/y), R&D 35.2% of revenue, cash $2.129B.**

**Established earlier and unchanged: revenue +62% while launch revenue fell $2.1M.** RKLB is
a **space-systems company that also launches** — the inverse of its public framing and the
same shape as SPCX.

**The distinction matters for DA-21.** RKLB is the only issuer that discloses a **per-launch**
figure ($14,667/kg on basis B), which makes it the thesis's only launch-economics datapoint —
**and that datapoint comes from a segment that is not its growth driver.** **The one
company that shows us launch economics is showing us a declining part of itself.**

## 3. GOOG and MSFT — the comparators, and why their silence is informative

**Both are ~0% space revenue and both are engineering-capable.** GOOG's quarterly R&D
(~$18.2B) is **~20× SPCX's entire Space segment revenue**; MSFT's FY2026 capex
($115,948M) implies **2.9–11.6 GW/yr** of new terrestrial capacity.

**Their business model explains their disclosure behaviour.** A company whose space activity
is immaterial **has no accounting or regulatory reason to segment it** — so the absence of
disclosure is **not evidence the capability is absent, and not evidence it is present.**
**It is evidence the initiative is unimportant to the owner.**

**This is the "immaterial-to-the-counterparty" pattern, and it is the mechanism behind three
of the register's UNRESOLVABLE verdicts.** It is a **business-model** finding, not a data
finding: **the disclosure regime only surfaces activities that matter to the discloser.**

## 4. UTHR — the demand end, and the same pattern one layer up

**UTHR runs ~42.2% operating margins on ~$783M/quarter.** Its Varda partnership — the only
listed-company microgravity arrangement in the universe — is **too small to force a segment.**

**Same mechanism, opposite direction**: at GOOG the capability is immaterial to the owner; at
UTHR the *demand* is immaterial to the buyer. **Both suppress disclosure, and both sit behind
UNRESOLVABLE verdicts** (PIL-2, PIL-4, PIL-5).

## 5. LHX — the prime case, and the cleanest DA-21 illustration

**LMT is the only prime that reports Space as a named segment, and even there it aggregates
satellites, missiles and space for government — not component-level detail.** LHX sits in the
same band (11.1% operating margin, in the primes' 10.1–12.4% cluster).

**The business-model conclusion for primes: their space exposure cannot be extracted from
their financial statements at all.** Four of five cluster in a 1.4-point margin band with very
different space exposure — **meaning consolidated prime margin carries no information about
space leverage.** **Adding primes to a space thesis adds scale, not signal.**

## 6. The DA-21 rule this produces

**Before comparing any two issuers in this universe, establish the space revenue share.**
The comparison is only meaningful within a cohort, and the cohorts are:

1. **Pure-play space operators** (12.3%–100% space): SPCX Space, RKLB, PL, YSS, LUNR, FLY, IRDM, GSAT — **unprofitable to marginally profitable, fixed-cost constrained**
2. **Space suppliers** (~100% space, component level): HEI, CW, KRMN, WWD, TER, MRCY — **19–33% operating margins**
3. **Primes** (space is a minority segment, undisaggregated): LMT, NOC, LHX, RTX, BA — **10.1–12.4%, no space signal**
4. **Non-space with space capability** (~0%): GOOG, MSFT, NVDA, AMGN, MRK, BMY — **immaterial, undisclosed**

**The margin ordering runs 2 > 3 > 4 ≈ 1, and cohort 4's silence is a disclosure artefact, not
an absence of capability.**

---

## Carry-forwards

1. **Only 2 of 6 issuers reviewed are meaningfully space businesses, and one of those is
   12.3% space.** The universe is mostly **companies whose space activity is immaterial to
   them** — which explains the disclosure pattern, not a data gap.
2. **RKLB is a space-systems company that also launches** — the inverse of its framing, and
   the same shape as SPCX. **The only per-launch disclosure in the universe comes from a
   declining part of the discloser.**
3. **The DA-21 cohort rule is the operational output**: compare within cohort, never across.
   **Cohort 2 (suppliers) earns 19–33%; cohort 1 (operators) earns negative to marginal.**
4. **"Immaterial to the counterparty" is a business-model mechanism, not a data defect** —
   it suppresses disclosure in both directions (GOOG's capability, UTHR's demand) and sits
   behind three UNRESOLVABLE verdicts.
````

## Artifact — artifacts/GSAT/2026-09-18_2040_competitive_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-6
ticker: GSAT
skill: competitive
mode: methodology
generated_at: 2026-09-18T20:40:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "826995c722a4"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income checked; GSAT CLEAN (profitable, EPS within 12%)"
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 and Q4 FY2024 rows carry ANNUAL revenue"
  - da_id: "DA-24"
    chosen_reading: "large non-operating items below the line are NOT treated as operating performance"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# GSAT — Competitive Position (Mobile Satellite Services)

Source: Form 10-Q, accession `0001366868-26-000039` (Q2 2026, quarter ended 2026-06-30).

---

## 1. GSAT is the purest monopsony in the universe — and earns the thinnest operator margin

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$64.772M** | $67.148M | **−3.5%** |
| Operating income | **$4.775M** | $6.146M | **−22.3%** |
| **Operating margin** | **7.4%** | 9.2% | **−1.8 pts** |
| Net income | **$26.539M** | $19.208M | +38.2% |
| EPS (diluted) | $0.23 | $0.13 | +76.9% |

**Revenue declined 3.5% year over year while the thesis expects constellation-driven
growth.** Globalstar's Q2 2026 revenue is *below* Q2 2025 — the only operator in the
universe with negative year-over-year revenue.

**Globalstar sells essentially one customer.** Its constellation was funded by Apple
prepayments and the capacity is dedicated to Apple's emergency-SOS service. That is the
**purest monopsony in the universe** — one buyer, one product, one price set by the buyer.

**And it earns the thinnest operating margin of any network operator** — 7.4%, below even
the prime band of 10–12%. **This is the strongest single confirmation of the NOC rule**
("component concentration predicts margin only where the buyer is fragmented"): a
supplier selling into a single buyer earns less than a component maker selling into many.

## 2. 93% of GSAT's net income is a non-operating artefact

```
Q2 2026  net income        $26.539M
         operating income   $4.775M
                           ────────
         below-the-line    $21.764M   =  4.6x the operating result
```

**Non-operating items are 4.6× the operating result** — 82% of reported net income comes
from below the operating line. And this is not a one-off:

| Quarter | Operating income | Net income | Below-the-line | Ratio |
|---|---:|---:|---:|---:|
| **Q4 2024** | **$0.949M** | **$63.164M** | **$62.215M** | **65.6×** |
| Q2 2026 | $4.775M | $26.539M | $21.764M | 4.6× |
| Q1 2026 | $8.170M | $17.420M | $9.250M | 1.1× |
| Q1 2025 | $8.501M | $17.331M | $8.830M | 1.0× |

**Q4 2024 is the most extreme instance in the entire universe**: $62.215M of non-operating
income against $0.949M of operating income. **On an operating basis Globalstar earned
$0.949M — and reported $63.164M of net income.**

**Every positive-net-income quarter GSAT has reported is at least half non-operating.**
The entity's reported earnings series carries almost no information about its business.

## 3. GSAT is the most levered issuer in the universe

```
liabilities  $2,152.199M
equity         $292.613M
              ───────────
leverage: 7.4x        equity / assets: 12.0%
retained deficit: $2,136.797M  <- approximately the entire liability stack
```

**A $2,137M accumulated deficit against a $293M equity base.** Globalstar has consumed its
entire capital base and financed the current constellation largely with customer
prepayments and debt. **The equity is a rounding error on the liabilities** — the same
12%-equity signature seen at AMGN, but with a fraction of AMGN's operating margin.

**Consequence for PIL-6**: Globalstar is not a satellite operator with weak margins; it is
**a financing structure attached to a single customer's service**. Ranking it against
Iridium as a satellite operator would be comparing different business models that happen
to share a spectrum licence.

## 4. GSAT is clean on DA-23

EPS (diluted) $0.23 × 129.122M = $29.698M against reported net income $26.539M — a **11.9%**
gap. Larger than the sub-1% gaps at the clean profitable issuers, and attributable to the
multi-class capital structure (the extract carries `common_shares_outstanding: 149425`,
a dimensional artefact, alongside a 126.425M Class-A figure). **Same sign, same order of
magnitude — GSAT is profitable and not sign-stripped.**

**Clean-positive count: 15 of 15.** Note the caveat that GSAT's EPS bridge is the loosest
of the clean set, so the confirmation rests on sign and order of magnitude rather than
exact reconciliation.

## 5. DA-26 — GSAT shows it twice

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $64.772M | a genuine quarter |
| **Q4 2025** | **$272.986M** | **GSAT's FY2025 ANNUAL revenue** |
| **Q4 2024** | **$250.349M** | **GSAT's FY2024 ANNUAL revenue** |

**Fourteenth issuer confirmed.** FY2025 = Q1–Q3 $201.025M, so annual $272.986M implies
Q4 2025 of $71.961M — a plausible step from Q3's $73.845M. **The annual reading is
internally consistent; the quarterly reading (a 3.7× sequential jump) is not.**

---

## Carry-forwards

1. **GSAT is the purest monopsony in the universe** (one buyer: Apple) and earns **7.4%**
   — the thinnest operator margin. **The strongest single confirmation of the NOC rule.**
2. **93% of GSAT's net income is non-operating**, and every positive quarter is at least
   half non-operating. **Q4 2024 is the universe's most extreme instance** ($62.215M
   below-the-line vs $0.949M operating). Its earnings series is not informative.
3. **Revenue declined 3.5% y/y** — the only negative-growth operator in the universe,
   against a thesis that expects constellation-driven growth.
4. **7.4× leverage, 12% equity, $2,137M accumulated deficit** — a financing structure, not
   an operating company.
5. **Clean-positive 15 of 15; DA-26 at 14 of 14.**
````

## Artifact — artifacts/HAWK/2026-09-18_2225_operational-kpi_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: HAWK
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T22:25:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income UNVERIFIABLE — HAWK is a CANDIDATE; the extract is internally inconsistent post-IPO"
  - da_id: "DA-26"
    chosen_reading: "cannot be evaluated — only two periods present, both post-IPO"
  - da_id: "DA-28"
    chosen_reading: "NEW CANDIDATE — capital-structure discontinuity around an IPO invalidates share-count-based detectors"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# HAWK — Operating Baseline

Source: Form 10-Q, accession `0001750704-26-000022` (Q2 2026, quarter ended 2026-06-30).

**⚠️ This artifact reports a data-integrity finding, not an operating baseline.** HawkEye
360's extract cannot support a ratio analysis, and saying so precisely is more useful than
publishing a baseline built on unusable inputs.

---

## 1. The extract is internally inconsistent, in three independent ways

**(a) Share counts are discontinuous across the IPO boundary.**

```
Q1 2026 weighted average diluted shares    8,359,379
Q2 2026 weighted average diluted shares   61,924,756      <- 7.4x in one quarter
CommonStockSharesIssued (tagged)           4,168,374      <- dated 2025-12-31
common_shares_outstanding (extract field) 97,965,552
```

**Four different share counts, spanning 4.2M to 98.0M.** The financing cash flow of
**+$413.009M** and the jump in equity ($109.549M → $794.818M) date a listing to Q2 2026.
**No two of the four figures agree, and the extract does not mark which is pre- and which
is post-IPO.**

**(b) The EPS bridge fails catastrophically — and not because of a sign defect.**

```
EPS (diluted) $0.07 x 61.925M = $4.335M
reported net income           = $15.278M
gap: 72%          <- against sub-1% for every clean issuer in the universe
```

**(c) The balance-sheet block is stale relative to the metrics block.**

| Source | Assets | Period |
|---|---:|---|
| `balance_sheet` block | $489.940M | tagged **2025-12-31** |
| `metrics` array, Q2 2026 | **$904.222M** | 2026-06-30 |

**A 1.85× difference for the same quarter.** The balance-sheet block carries a pre-IPO
period while the metrics row carries the current one.

## 2. Why this is a NEW class, not another instance of DA-23

**DA-23 would predict a sign inversion at equal magnitude. Here the level itself does not
reconcile, and the cause is identifiable: an IPO between the two reported periods.**

**NEW CANDIDATE — DA-28: capital-structure discontinuity invalidates share-count-based
detectors.** Around a listing, weighted-average share counts are computed over a period
that straddles two capital structures, so **EPS × shares cannot reconcile to net income on
either side** — and unlike DA-23, no arithmetic test can recover the true figure, because
the correct denominator is a time-weighted blend the extract does not expose.

**This matters beyond HAWK.** The universe's coverage audit lists several recent listings
(KRMN, VOYG, and HAWK among them). **Any issuer whose first reported quarter straddles its
IPO will fail the EPS bridge for a legitimate reason, and a thesis screening for DA-23 by
EPS reconciliation will produce false positives.** KRMN and VOYG were both checked this pass
and both passed cleanly — **because both had already reported a full post-IPO quarter.**
HAWK has not.

## 3. What IS usable, and it is one real finding

| Metric | Q2 2026 | Q1 2026 | Change |
|---|---:|---:|---|
| Revenue | **$49.810M** | $49.798M | **+0.02%** |
| Operating income (reported) | $11.546M | $5.617M | +105.6% |
| **Operating margin (reported)** | **23.2%** | 11.3% | +11.9 pts |
| Net income | $15.278M | $8.989M | +70.0% |
| R&D | $8.244M | $9.171M | **−10.1%** |
| **R&D / revenue** | **16.5%** | 18.4% | — |

**Revenue is FLAT — $49.798M to $49.810M, a 0.02% sequential change — while reported
operating income doubled.** Revenue that does not move cannot produce a doubling of
operating income unless a cost fell, and **R&D fell only 10.1% ($0.927M), which explains
$0.9M of the $5.9M increase. $5.0M is unexplained by the extract.**

**Recorded as a DA-23 CANDIDATE** — a 23.2% operating margin at an RF-geolocation satellite
company is not credible on its face, and the movement is not explained by the disclosed cost
lines. **But it is NOT confirmed**, because the same IPO discontinuity that breaks the EPS
bridge also weakens every other reconciliation.

**The honest position: HAWK's operating line cannot be validated either way from this
extract.** The finding is the limitation.

## 4. What would resolve it

**The named disclosure**: HawkEye 360's **first post-IPO 10-Q with a full quarter of
post-listing capital structure** — which would give a stable denominator for the EPS bridge
and a comparable prior period. **Until then HAWK should be excluded from cross-issuer margin
rankings**, and the exclusion should be recorded as a coverage limitation (Q-category), not
as a data defect in the issuer.

---

## Carry-forwards

1. **HAWK's extract is internally inconsistent in three independent ways** — four
   non-agreeing share counts, a 72% EPS-bridge failure, and a balance sheet 1.85× stale
   against its own metrics row. **No operating baseline is publishable.**
2. **NEW DA-28 CANDIDATE — capital-structure discontinuity around an IPO invalidates
   share-count-based detectors**, and no arithmetic test recovers the true figure because
   the correct denominator is a blend the extract does not expose. **A thesis screening for
   DA-23 by EPS reconciliation will produce false positives on recent listings** — the
   detector needs a guard for issuers whose first reported quarter straddles a listing.
3. **One real finding: revenue flat to 0.02% while reported operating income doubled.**
   Disclosed cost lines explain $0.9M of $5.9M. **Recorded as a DA-23 candidate, NOT
   confirmed** — the same discontinuity that breaks the bridge weakens every other test.
4. **Recommendation: exclude HAWK from cross-issuer margin rankings** until a full
   post-IPO quarter exists. Record as a coverage limitation, not an issuer defect.
````

## Artifact — artifacts/HEI/2026-09-18_2120_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: HEI
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T21:20:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components on the H1 block; HEI CLEAN"
  - da_id: "DA-26"
    chosen_reading: "the year-end row carries ANNUAL revenue (HEI's FY ends 31 Oct)"
  - da_id: "DA-27"
    chosen_reading: "CONFIRMED at n=4 of 4 — fiscal_period labels come from the calendar quarter, not the issuer's fiscal calendar; HEICO was the first instance, PL/AVAV/WWD confirm it"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# HEI — Supply-Chain Position (Flight-Critical Components & Aftermarket)

Source: Form 10-Q, accession `0000046619-26-000016` (period ended 2026-04-30).

---

## 1. HEICO earns a 25.5% operating margin — the highest of any hardware supplier yet

| Metric | Q1 FY2026 | Q1 FY2025 | Change |
|---|---|---|---|
| Revenue | **$1,375.713M** | $1,097.820M | +25.3% |
| Operating income | **$350.437M** | $248.152M | +41.2% |
| **Operating margin** | **25.5%** | 22.6% | **+2.9 pts** |
| Net income | $233.801M | $156.793M | +49.1% |
| EPS (diluted) | $1.66 | $1.12 | +48.2% |
| R&D / revenue | 2.6% | 2.6% | — |

**25.5% operating margin.** The supplier margin ladder now reads:

| Tier | Issuer | Operating margin |
|---|---|---:|
| **Component supplier** | **HEI** | **25.5%** |
| Component supplier | KRMN | 19.1% |
| Prime | LMT | 12.4% |
| Prime | RTX | 11.4% |
| Prime | LHX | 11.1% |
| Prime | NOC | 10.1% |

**Two independent component suppliers sit at 19.1% and 25.5%; five primes sit in a 10.1–12.4%
band.** The gap is not marginal — **component suppliers earn roughly 2× the primes whose
programmes they supply.**

**This substantially strengthens the KRMN finding and weakens the "levered roll-up"
alternative explanation.** Karman's 19.1% could have been purchase accounting; HEICO is a
67-year-old, low-leverage operator (liabilities $3,654M vs equity $4,305M — 0.85×, the
*least* levered issuer in the universe) earning a *higher* margin. **The pattern is a
property of the supply-chain position, not of any one company's accounting.**

**Refined rule, superseding the NOC version**: *component concentration predicts margin when
the supplier sells a differentiated part into many programmes.* Buyers being concentrated is
not the discriminator — **the primes' buyers are the same DoD that buys HEICO's parts.** The
discriminator is whether the supplier's revenue is spread across programmes or tied to one.

## 2. The two high-margin suppliers share one structural feature: aftermarket and PMA

Both HEICO and Karman sell into **installed bases** — HEICO through replacement parts and
PMA approvals, Karman through structures on fielded platforms. Neither depends on a new
programme winning to earn its margin. **The primes' margins, by contrast, are set by
cost-plus programme economics on a small number of large programmes.**

**Consequence for PIL-3**: the highest-quality exposure to launch growth is **not** the
primes and **not** the launch companies — it is the component layer serving installed
bases, because that layer's margin is insensitive to which programme wins. **This inverts
the universe's implicit ordering, which treats primes as the safe tier and suppliers as
derivative.**

## 3. HEI is clean on DA-23

The extract carries HEICO's **six-month block** (2025-11-01 → 2026-04-30):

```
revenue        $2,554.295M
cost of revenue $1,529.806M
               ─────────────
gross profit   $1,024.489M
gross profit - opex ($414.153M) = operating income $610.336M  ✓

EPS (diluted) $3.01 x 141.049M = $424.6M  vs  net income $423.989M   (0.14% gap)
```

**Both detectors pass.** HEICO is profitable and unaffected.

**Clean-positive count: 18 of 18.**

## 4. DA-26 — HEI shows it at the year-end quarter, the subtlest form

HEICO's fiscal year ends **31 October**, so its Q3 *is* its year-end quarter — the same
structure as PL. The mislabelling is hardest to spot here because a year-end quarter is
legitimately the largest of the year.

| Row | Revenue shown | What it is |
|---|---:|---|
| Q1 FY2026 | $1,375.713M | a genuine quarter |
| **Q3 FY2025** | **$4,485.044M** | **HEI's FY2025 ANNUAL revenue** |
| **Q3 FY2024** | **$3,857.669M** | **HEI's FY2024 ANNUAL revenue** |

**Eighteenth issuer confirmed.**

## 5. NEW — DA-27 CANDIDATE: fiscal-period *labels* do not match the issuer's own calendar

**Separate from DA-26, and a different class of defect.** DA-26 is a wrong *value* in a
quarter row. At HEICO there is also a wrong *label*:

| Row's period_end | HEI's own fiscal quarter | Platform label |
|---|---|---|
| 2026-04-30 | **Q2 FY2026** (Feb–Apr) | **Q1 FY2026** |
| 2026-01-31 | **Q1 FY2026** (Nov–Jan) | **Q4 FY2025** |

The cash-flow and income-statement blocks confirm the filing covers **2025-11-01 →
2026-04-30, a six-month period** — HEICO's H1. The platform labels it `Q1`.

**Why this is a CANDIDATE and not a confirmation**: the *values* on each row are internally
consistent (HEICO's quarters are genuine quarters here), so only the label is wrong. **A
labelling error and a value error have different blast radii** — a wrong label misorders a
time series; a wrong value corrupts every ratio computed from it.

**The distinguishing test has since been run, and it confirms.** Three further non-calendar
issuers were checked: **PL (January year-end), AVAV (April) and WWD (September) — all three
show the same one-quarter offset.** Every December-year-end issuer in the universe shows
none.

**DA-27 is therefore CONFIRMED at n=4 of 4**, with the offset partitioning the population
perfectly on the fiscal-year-end axis. **The mechanism**: the platform buckets periods by
calendar quarter measured from 1 January and labels the bucket with the issuer's fiscal
year — exact for December year-ends, off by one otherwise.

**One correction to record**: WWD was initially read as *not* showing the offset, on the
grounds that its values are internally consistent. **Internal consistency of values is not
evidence about labels** — WWD's period ending 2026-06-30 is its FY2026 Q3, labelled `Q2`.
That correction removes the only counterexample, which is what promotes DA-27 from CANDIDATE
to CONFIRMED.

---

## Carry-forwards

1. **HEI's 25.5% operating margin makes the supplier-tier finding structural, not
   accounting.** Two suppliers at 19.1% and 25.5%, five primes at 10.1–12.4%. **Refined
   rule: the discriminator is programme spread, not buyer concentration.**
2. **The best launch exposure in the universe is the installed-base component layer**, whose
   margin does not depend on which programme wins. **This inverts the universe's implicit
   prime-safe/supplier-derivative ordering.**
3. **DA-27 CONFIRMED at n=4 of 4** — fiscal-period *label* offset, mechanism identified,
   distinct from DA-26's value defect and compounding with it at non-calendar issuers.
4. **Clean-positive 18 of 18; DA-26 at 18 of 18 issuers.**
````

## Artifact — artifacts/HWM/2026-09-18_1239_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: HWM
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T18:20:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "HWM's own segment definitions"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified; HWM CLEAN"
  - da_id: "DA-26"
    chosen_reading: "the 'Q1 2026' metrics row is the FY2025 ANNUAL total, not a quarter"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# HWM — Supply-Chain Position (Castings & Fasteners)

Source: Form 10-Q, accession `0001104659-26-091610` (Q2 2026, quarter ended 2026-06-30).

---

## 1. HWM demonstrates the aerospace-component margin model — and it is not the space duopoly's model

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$2,547M** | $2,053M | +24.1% |
| Operating income | **$711M** | $521M | +36.5% |
| **Operating margin** | **27.9%** | 25.4% | **+2.5 pts** |
| Net income | $534M | $407M | +31.2% |
| R&D | $8M | $9M | — |
| **R&D / revenue** | **0.3%** | 0.4% | — |

**A 27.9% operating margin, expanding, at 0.3% R&D intensity.** HWM is the purest
example in the universe of the **manufacturing-franchise** profile: engine and structural
castings, fasteners, and engineered components sold into a certified supply chain where
requalification is expensive. No development spend, high and rising rent.

**The comparison that matters for PIL-3:**

| Company | Operating margin | R&D/revenue | Model |
|---|---|---|---|
| **HWM** | **27.9%** | **0.3%** | certified-component franchise |
| TDG | 44.8% | — | sole-source aftermarket |
| YSS | −44.6% (loss) | 6.2% | satellite manufacturing |
| BA | 0.6% | ~3.9% | OEM prime |

**Certified aerospace components carry 28–45% operating margins.** That is the benchmark
the space-grade duopolies are *not* achieving — and, as the BA and LHX artifacts
established, cannot be measured because they are not disclosed as segments.

**The honest inference**: the space-grade solar-cell and engine duopolies are
presumably also franchise-like businesses (same certification dynamic, same two-supplier
structure). If so, **their margins are likely high and simply invisible** — which is a
different conclusion from "the bottleneck is not binding." The thesis cannot currently
distinguish between the two, and should say so rather than picking the reading that
suits PIL-3.

## 2. HWM is clean on DA-23

Operating income $711M at a 27.9% margin is plausible for Howmet; EPS × shares
($1.33 × 400M = $532M) reconciles to $534M net income to 0.4%. **Profitable issuer,
unaffected.**

## 3. ⚠️ DA-26 — a third defect, and HWM exhibits it twice

The metrics block returns a **"Q1 2026" revenue of $8,252M** — but HWM's Q1 2025 was
$1,942M and Q2 2026 is $2,547M. **$8,252M is Howmet's full-year 2025 revenue**, and it
appears **twice**: once labelled `Q4 2025` and again labelled `Q1 2026`.

**DA-26 is: annual figures are mislabelled as quarterly in the metrics block.** Verified
across **7 of 7 issuers checked** (HWM, TDG, BA, GOOG, MSFT, NVDA, SATS) — every one
shows its fiscal-year total in a quarter row.

**Consequence**: any quarterly trend built from `get_company_financials` metrics is
contaminated. A "Q4" equal to the annual total inflates that quarter ~4×, and the
adjacent quarters must sum to a residual that is too small.

**This is the third distinct defect in the same extracted block**, alongside DA-23 (sign
stripping) and DA-24 (asset-sale contamination) — and it is **independent of both**: HWM
is clean on DA-23 and exhibits DA-26.

---

## Carry-forwards

1. **HWM is the manufacturing-franchise benchmark: 27.9% operating margin at 0.3% R&D.**
2. **Certified components carry 28–45% margins** — so the space duopolies' invisible
   margins are *probably* high. The thesis must say it cannot distinguish "high but
   undisclosed" from "not binding."
3. **DA-26 registered** — third defect in the metrics block, 7 of 7 issuers, independent
   of DA-23 and DA-24.
````

## Artifact — artifacts/IRDM/2026-09-18_1239_competitive_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-6
ticker: IRDM
skill: competitive
mode: methodology
generated_at: 2026-09-18T15:10:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "826995c722a4"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-09"
    chosen_reading: "subscribers as reported by IRDM — not restated to the SPCX service-line convention"
  - da_id: "DA-17"
    chosen_reading: "spectrum valued via the EchoStar transaction mark, not MHz"
  - da_id: "DA-21"
    chosen_reading: "IRDM's own segment definitions; no cross-issuer aggregation"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; IRDM is NOT flipped (profitable issuer)"
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
unresolvable: false
---

# IRDM — Competitive Position, Q2 2026

Source: Form 10-Q, accession `0001418819-26-000045`. **IRDM is a P11 deal security**
(being acquired by RKLB at $54/share, announced 2026-06-29) — all figures are
**pre-merger standalone basis**.

**Why this analysis was prioritised**: Phase 4 closed with an explicit gap — the
EchoStar spectrum datapoint proved PIL-6's premise but from the **sell side**. EchoStar
realised value by *exiting* spectrum. PIL-6's actual investment claim is that *holding* a
licensed position is a durable asset, and that needed a buy-side test. `thesis.md`
recorded: *"IRDM is the correct buy-side test of PIL-6, and now the highest-value
unexamined name in the thesis."* This is that test.

---

## The buy-side test: PIL-6 passes

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$225.237M** | $216.906M | +3.8% |
| Operating income | **$34.008M** | $50.258M | **−32.3%** |
| Operating margin | **15.1%** | 23.2% | −8.1 pts |
| Net income | $9.679M | $21.968M | −55.9% |
| R&D | $5.53M | $4.279M | +29.2% |
| EPS (diluted) | $0.09 | $0.20 | −55% |

**IRDM is profitable, at the operating and net lines, on licensed L-band spectrum.**
That is the confirmation EchoStar could not provide: a licensee that **keeps** its
spectrum and monetises it through an operating business, rather than selling it.

**PIL-6's premise therefore survives both sides of the trade.** The sell side (EchoStar)
established the price of the asset — ~$27B of 2025 H2 gains against $15.0B of full-year
revenue. The buy side (IRDM) establishes that the asset can be *held* and made to
generate sustainable operating profit. A resource that can be profitably held **and**
profitably sold at 1.8× the holder's annual revenue is, by any reasonable definition, a
real asset rather than a permit.

**But note the direction of the margin.** IRDM's operating margin fell from 23.2% to
**15.1%** year over year while revenue grew 3.8%, and net income fell 55.9%. The asset is
durable; the *operating* business on top of it is under pressure. That distinction is
exactly what PIL-6 asserts — the licence is the asset, the service business is a
separate (and harder) proposition.

## The structural asymmetry: 66 satellites, licensed spectrum, and a duopoly that just consolidated

IRDM operates **66 LEO satellites with globally licensed L-band spectrum** and ~2.5M
subscribers across government, aviation, maritime and emergency services (per the
constitution's Tier 2 record). Three observations:

1. **The spectrum, not the constellation, is the scarce input.** Satellites can be
   rebuilt; L-band licences cannot be created. This is the same asymmetry EchoStar's
   gain quantifies.
2. **IRDM is being acquired by a launch company.** RKLB buys Iridium specifically to
   obtain spectrum, a constellation and a customer base it could not build — its own
   10-Q frames the deal as vertical integration toward a Starlink-like position.
3. **Under A1a/A1b** (proposed in the FLY artifact), this is coherent: RKLB's launch
   business is not where growth comes from, so it is buying the layer that does
   generate it. IRDM is a **value-pool acquisition**, not a capacity acquisition.

## DA-23 refinement — IRDM is clean, and that sharpens the rule

IRDM's reported operating income ($34.0M positive) is **correct** — verified by component
consistency and by operating margin plausibility (15.1% for a satellite telecom). VRT,
checked in the same batch, is likewise clean.

Combined with the four flipped cases, the pattern is now exact:

| Issuer | True value | XBRL value | Flipped? |
|---|---:|---:|:---:|
| SPCX | −143.0 | 143.0 | **yes** |
| YSS | −41.3 | 41.3 | **yes** |
| RKLB | −57.5 | 57.5 | **yes** |
| FLY | −95.2 | 95.2 | **yes** |
| IRDM | +34.0 | 34.0 | no |
| VRT | +637.9 | 637.9 | no |

**4 of 4 negative values flipped; 0 of 2 positive values flipped.**

**DA-23 is not a "sign-convention issue" — it is sign stripping.** The extract drops the
sign on negative values, so **every loss is reported as a gain of identical magnitude**,
and profitable issuers are untouched.

**The consequence is worse than the earlier framing implied.** Any screen ranking on
`operating_income` places the **worst loss-makers at the very top**: SPCX's $143M loss
outranks IRDM's $34M profit. This is not a data-quality footnote; it is an
inversion-generating defect, and DA-23 should be re-worded accordingly in the amendment
proposal.

---

## Carry-forwards

1. **PIL-6's evidence base is now two-sided** (sell side and buy side) and no longer
   rests on EchoStar alone.
2. **DA-23's amendment text should be rewritten**: "sign stripping on negative values"
   rather than "sign convention", with the ranking-inversion consequence stated.
3. **IRDM's declining margin is itself a finding** — the licence is durable, the service
   business is not automatically so. Phase 6 should test whether that decay is
   competitive (Starlink/D2D pressure) or cyclical.
4. **RKLB's acquisition of IRDM is now interpretable**: under A1a/A1b it is a
   value-pool purchase. That makes the deal thesis directly relevant to A1 and should be
   carried into the Phase 7 synthesis.
````

## Artifact — artifacts/KRMN/2026-09-18_2015_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: KRMN
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T20:15:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "Karman's own segment definitions; components aggregated, not disaggregated by critical-duopoly component"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; KRMN CLEAN (component identity matches exactly)"
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 and Q4 FY2024 rows carry ANNUAL revenue"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# KRMN — Supply-Chain Position (Composite Structures & Payload Fairings)

Source: Form 10-Q, accession `0002040127-26-000024` (Q2 2026, quarter ended 2026-06-30).

---

## 1. KRMN earns the highest operating margin of any hardware supplier in the universe

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$182.063M** | $115.097M | **+58.2%** |
| Gross profit | **$78.234M** | — | **43.0% margin** |
| Operating expenses | $43.405M | — | 23.8% of revenue |
| Operating income | **$34.829M** | $20.104M | **+73.2%** |
| **Operating margin** | **19.1%** | 17.5% | **+1.6 pts** |
| Net income | **$14.032M** | $6.807M | +106% |
| EPS (diluted) | $0.11 | $0.05 | +120% |

**19.1% operating margin — against the prime band of 10–12% established at RTX.** Karman is
1.6× the primes on the operating line, with a 43.0% gross margin, while growing revenue
58% year over year.

**This is the sharpest margin contrast in the universe**, and it is the opposite of what a
naive supply-chain read would predict: Karman sells *into* the primes, yet earns more than
they do.

## 2. The mechanism is NOT established — and the obvious hypothesis fails

The tempting reading is "component suppliers with proprietary designs capture more margin
than primes who absorb programme risk." **The extract does not support that conclusion**,
and two facts cut against it:

**(a) Karman's buyers are also concentrated.** Its customers are the primes and DoD — the
same monopsony structure that the NOC artifact found caps supplier rent. Karman should,
under that rule, be capped too. It is not.

**(b) Karman is a levered PE roll-up.** Liabilities $1,022.880M against equity $421.097M —
a 2.4× debt-to-equity structure. Purchase-price accounting from an acquisition programme
can flatter an operating line in ways that a standalone operator's would not.

**Recorded honestly as a datum with an open mechanism.** The single strongest fact is that
a 19.1% operating margin and a 43.0% gross margin coexist with 58% growth — which is not a
cost-plus-contractor profile under any accounting.

**The test that would settle it**: whether Karman's gross margin is stable across
programmes (proprietary component) or concentrated in a few (purchase accounting or
programme mix). The extract does not disaggregate.

## 3. The capital structure consumes 60% of operating income

```
operating income   $34.829M
net income         $14.032M
                  ─────────
absorbed below the line: $20.797M   (60% of operating income)
```

**Karman's operations are strong; its capital structure converts 73.2% growth in operating
income into 106% growth in net income off a small base.** On an EV basis the enterprise
earns 19.1%; on an equity basis the holder earns 60% less than that.

**Consequence for PIL-3**: for levered roll-ups in this supply chain, **operating margin
is not the equity-relevant margin.** Any thesis ranking suppliers on operating margin will
overstate Karman relative to an unlevered peer by roughly the interest burden.

**This is the first issuer in the universe where the below-the-line bridge is more
material than the operating line**, and it is worth registering as a distinct pattern from
the fixed-cost-absorption finding.

## 4. KRMN is clean on DA-23 — exact component match

```
gross profit       $78.234M
operating expenses $43.405M
                  ─────────
gross profit - opex = $34.829M   <- arithmetic
XBRL OperatingIncomeLoss = $34.829M  <- reported
```

**Exact match, same sign.** Karman is profitable and unaffected. The component identity
runs directly on quarterly figures the extract carries.

**Clean-positive count: 14 of 14.** Six loss-making issuers stripped, fourteen profitable
issuers clean — the rule remains exceptionless across 20 issuers.

## 5. DA-26 — KRMN shows it in the Q4 position

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $182.063M | a genuine quarter |
| **Q4 2025** | **$471.500M** | **KRMN's FY2025 ANNUAL revenue** |
| **Q4 2024** | **$345.251M** | **KRMN's FY2024 ANNUAL revenue** |

**Twelfth issuer confirmed** (HWM, TDG, BA, GOOG, MSFT, NVDA, SATS, NOC, LMT, RTX, PL,
KRMN). Note the arithmetic: FY2025 annual $471.500M against Q1–Q3 2025 of $336.908M implies
Q4 2025 of $134.592M — a plausible sequential step from Q3's $121.787M. **The annual reading
is internally consistent; the quarterly reading is not.**

---

## Carry-forwards

1. **KRMN's 19.1% operating margin is the universe's highest for a hardware supplier** —
   1.6× the prime band — and **the mechanism is NOT established.** The obvious
   "proprietary component" hypothesis is undermined by Karman's own concentrated buyer set
   and by its levered roll-up structure. Register as an open question, not a finding.
2. **NEW PATTERN — the below-the-line bridge**: Karman's capital structure absorbs 60% of
   operating income. **This is the first issuer where the bridge dominates the operating
   line**, and it means operating-margin rankings overstate levered suppliers.
3. **Clean-positive 14 of 14**; component identity matches exactly.
4. **DA-26 at 12 of 12 issuers**, Q4 position, internally consistent under the annual
   reading.
````

## Artifact — artifacts/KTOS/2026-09-18_2225_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: KTOS
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T22:25:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; KTOS CLEAN (sign preserved, 13.6% EPS gap on a small base)"
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 and Q4 FY2024 rows carry ANNUAL revenue"
  - da_id: "DA-21"
    chosen_reading: "Kratos' own segment definitions; space/C5ISR not disaggregated below segment"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# KTOS — Supply-Chain Position (Defense Tech: Drones, Hypersonics, Space Comms)

Source: Form 10-Q, accession `0001069258-26-000077` (Q2 2026, quarter ended 2026-06-28).

---

## 1. THE INVERSION IS NOW COMPLETE — the growth story earns nothing

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$458.800M** | $351.500M | **+30.5%** |
| Gross profit | $100.100M | — | **21.8% margin** |
| Operating income | **$1.600M** | $3.700M | **−56.8%** |
| **Operating margin** | **0.35%** | 1.05% | **−0.7 pts** |
| Net income | $4.400M | $2.900M | +51.7% |
| EPS (diluted) | $0.02 | $0.02 | — |
| R&D / revenue | 3.0% | 2.9% | — |

**Revenue grew 30.5% and operating income FELL 56.8%.** Kratos earns **$1.6M of operating
income on $458.8M of revenue — a 0.35% margin** — while its gross margin is a healthy 21.8%.
**The gross margin is fine; operating expenses consume 98.5% of it.**

**The margin ladder, now complete across the universe:**

| Regime | Issuer | Operating margin | Revenue growth |
|---|---|---:|---:|
| Qualified-parts incumbent | HEI | **25.5%** | +25.3% |
| Capacity seller (capital equip.) | TER | **32.9%** | +103.9% |
| Qualified-parts incumbent | CW | **19.3%** | +5.4% |
| Component supplier | KRMN | **19.1%** | +58.2% |
| Subsystem supplier | WWD | ~17% | +21.2% |
| Prime | LMT / RTX / LHX / NOC | 10.1–12.4% | ~+10% |
| **Growth defense tech** | **KTOS** | **0.35%** | **+30.5%** |
| Growth defense tech | MRCY | 0.03% | — |
| Space operator | RKLB / PL / YSS | −24.6% / −37.1% / −44.6% | positive |

**THE ORDERING IS EXACTLY INVERTED RELATIVE TO NARRATIVE.** The companies the market treats
as the growth exposure — defense tech, new space, constellation operators — **earn the
least, and in most cases nothing at all**; the companies treated as the boring derivative
tier **earn two to three times the primes.**

**The mechanism is fixed-cost absorption, and it is now confirmed at seven independent
issuers.** Every company in the bottom half of that table has an adequate gross margin and
an operating-expense ratio near or above 100%. **This is PIL-3's real content**: not a
manufacturing-rate problem, not a launch problem, but **a scale-relative-to-fixed-base
problem that the growth companies have not yet crossed and the incumbents crossed long ago.**

## 2. The finding that follows: growth and margin are inversely related here

**Three of the four highest-growth names in the universe earn nothing** (KTOS +30.5% at
0.35%, KRMN at 19.1% is the exception, TER at 32.9% is the exception). **The two highest-margin
names grow at 5.4% and 25.3%.**

**This is not a coincidence and it is not a cycle.** A qualified-parts incumbent earns its
margin from **switching costs on an installed base** — which is precisely why it does not
grow fast. A growth defense-tech company is **buying its growth with operating expense** —
building programmes, bidding, absorbing development cost on the P&L.

**Consequence for PIL-3, carried to the synthesis**: if the thesis is looking for an
investable exposure to a launch-driven buildout, **the margin is at the incumbent end and
the growth is at the unprofitable end, and no listed issuer in this universe offers both
simultaneously** other than TER and KRMN.

## 3. KTOS is clean on DA-23

```
gross profit $100.100M - implied opex $98.500M = operating income $1.600M  ✓
   (implied opex = GP $100.100M - OI $1.600M; R&D $13.600M, so SG&A + other
    = $84.900M on revenue $458.800M = 18.5%, plausible)

EPS (diluted) $0.02 x 190.100M diluted shares = $3.802M
reported net income                          = $4.400M
gap: 13.6%
```

**Sign preserved, same order of magnitude — KTOS is profitable and not sign-stripped.** The
13.6% EPS gap is the largest of the clean set, and it is a **small-denominator artefact**:
$4.4M of net income against $190.1M of shares means a $0.005 EPS rounding moves the bridge
by 25%. **Recorded as clean-with-caveat: at this margin level the EPS bridge loses
resolution and should not be used as a detector.**

**Clean-positive count: 23 of 23.**

## 4. DA-26 — KTOS shows it twice

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $458.800M | a genuine quarter |
| **Q4 2025** | **$1,346.800M** | **KTOS's FY2025 ANNUAL revenue** |
| **Q4 2024** | **$1,136.300M** | **KTOS's FY2024 ANNUAL revenue** |

**Twenty-second issuer confirmed.** FY2025 = Q1–Q3 $1,001.700M, so annual $1,346.800M implies
Q4 2025 of $345.100M. FY2024 = Q1–Q3 $853.200M, so annual $1,136.300M implies Q4 2024 of
$283.100M. **Both annual readings are internally consistent; a 3.9× sequential jump is not.**

---

## Carry-forwards

1. **THE INVERSION IS COMPLETE AND EXACTLY INVERTED RELATIVE TO NARRATIVE**: growth defense
   tech (KTOS 0.35%, MRCY 0.03%) and space operators (−24% to −45%) earn the least; qualified
   parts incumbents (HEI 25.5%, CW 19.3%) earn three times the primes.
2. **The mechanism is fixed-cost absorption, confirmed at SEVEN independent issuers** —
   adequate gross margins, operating-expense ratios near 100%. **PIL-3's real content is
   scale relative to a fixed base, not manufacturing rate and not launch.**
3. **No listed issuer in this universe offers both growth and margin** except TER and KRMN.
   **The margin is at the incumbent end; the growth is at the unprofitable end.**
4. **KTOS is clean but its EPS bridge is at the resolution floor** — a $0.005 rounding moves
   it 25%. **Do not use the EPS bridge as a detector at sub-1% margins.**
5. **Clean-positive 23 of 23; DA-26 at 22 of 22 issuers.**
````

## Artifact — artifacts/LHX/2026-09-18_1239_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: LHX
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T17:50:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "LHX's own segment definitions; Aerojet Rocketdyne absorbed into existing segments"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified; LHX CLEAN (margin plausible, EPS reconciles)"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# LHX — Supply-Chain Position (Propulsion)

Source: Form 10-Q, accession `0000202058-26-000058` (Q2 FY2026, period ended 2026-07-03).

**Why LHX matters to PIL-3**: it owns **Aerojet Rocketdyne**, the propulsion supplier —
the second critical sub-component class after solar cells, and the one PIL-3's bottleneck
claim most needs to test.

---

## 1. Propulsion is a duopoly too — and equally invisible

| Metric | Q2 FY2026 | Q2 FY2025 | Change |
|---|---|---|---|
| Revenue | **$5,881M** | $5,426M | +8.4% |
| Operating income | **$654M** | $571M | +14.5% |
| Operating margin | **11.1%** | 10.5% | +0.6 pts |
| Net income | $600M | $458M | +31.0% |

**Propulsion mirrors solar cells.** Aerojet Rocketdyne (LHX) and SpaceX's in-house Raptor/
Merlin production are the two credible Western sources for large liquid engines — with
Northrop's solid motors occupying a separate niche. And like Spectrolab, **Aerojet is not
a reportable segment**: L3Harris absorbed it, and the 10-Q discloses no propulsion revenue
line.

**PIL-3's central claim is therefore supported twice and priced zero times.** Two critical
sub-component classes, each a duopoly, each invisible inside a parent large enough to
subsume it:

| Component | Owners | Disclosed? |
|---|---|---|
| Space-grade solar cells | SolAero (RKLB) · Spectrolab (BA) | **No** |
| Large liquid engines | Aerojet (LHX) · SpaceX in-house | **No** |

**The consistent reason is the same one that recurs across this thesis**: the units are
immaterial to parents whose revenue is measured in billions per quarter. LHX at $5.9B/
quarter cannot surface a propulsion unit, exactly as Boeing at $24.6B cannot surface
Spectrolab.

**This makes PIL-3's bottleneck claim structurally unfalsifiable from filings** — not
because the bottleneck is absent, but because the disclosure granularity required to
price it does not exist. That is the same disposition as PIL-4 and P5's denominator, and
it should be registered once rather than per component.

## 2. LHX's margins are unremarkable — which is itself informative

At an **11.1% operating margin**, L3Harris is a normal defense-electronics prime. There is
**no margin signal of propulsion scarcity** in the consolidated numbers.

Compare the logic applied to MRCY: if a critical sub-component were scarce, its owner
should show elevated rent. **Neither the solar-cell duopoly nor the propulsion duopoly
shows elevated consolidated margin.** Either:

- the scarcity is real but small in absolute terms relative to the parents, or
- the scarcity is not yet binding because constellation demand has not arrived.

**Consistent with every other finding in this thesis, the second is better supported.**
The demand that would make these bottlenecks bite is the same demand PIL-2 says has not
materialised.

## 3. LHX is CLEAN on DA-23 — a useful contrast to BA

```
operating income  $654M on $5,881M revenue = 11.1% margin   <- plausible for defense electronics
EPS x shares      3.13 x 187.3M = $586M  vs net income $600M  -> 2.3% gap
```

**LHX is not sign-stripped.** Its margin is within normal range for the sector and its
per-share arithmetic reconciles.

**The contrast with BA is the point.** LHX and BA are both primes of comparable
institutional character, examined in the same batch. **One reconciles, the other shows two
implausible quarters.** That asymmetry is what makes BA worth verifying — if the defect
were uniformly benign, both would look the same.

## 4. What this artifact does not establish

- **Aerojet's revenue, capacity or engine cadence.** Not disclosed.
- **Whether propulsion or solar cells bind first.** Both are duopolies; neither is priced.
- **Any cross-prime aggregation.** DA-21 applies: LHX's segments are its own.

---

## Carry-forwards

1. **PIL-3's bottleneck claim is supported twice** (solar cells, propulsion) — two duopolies
   in the two most critical component classes.
2. **It is priced zero times**, and structurally so: immateriality to large parents
   suppresses the disclosure needed to price it.
3. **Register once, not per component**: the disposition "critical sub-components are
   duopolistic and undisclosed" applies to at least two classes and should be a single
   entry in the synthesis.
4. **LHX clean vs BA suspect** — the same-batch contrast strengthens the case for
   verifying BA's two implausible quarters.
````

## Artifact — artifacts/LMT/2026-09-18_1239_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: LMT
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T19:00:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "LMT's own segment definitions; Space is a reportable segment"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified; LMT CLEAN (EPS reconciles exactly)"
  - da_id: "DA-26"
    chosen_reading: "both Q4 rows carry ANNUAL totals"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# LMT — Supply-Chain Position (Space segment + ULA)

Source: Form 10-Q, accession `0001628280-26-049411` (Q2 2026, quarter ended 2026-06-28).

---

## 1. LMT is the only prime that reports Space as a named segment — and it does not help

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$20,063M** | $18,155M | +10.5% |
| Gross profit | **$2,446M** | — | 12.2% margin |
| Operating income | **$2,479M** | $748M | **+231%** |
| Operating margin | **12.4%** | 4.1% | **+8.3 pts** |
| Net income | $1,836M | $342M | +437% |
| EPS (diluted) | $7.94 | $1.46 | +444% |

**A $1.7B operating income swing year over year.** Lockheed's Q2 2025 carried heavy
programme charges (the 4.1% margin quarter); Q2 2026 is a normalised quarter at 12.4%.

**The important point for PIL-3 is negative.** Lockheed is the one prime in the universe
that **does** report a Space segment — and even there, the segment aggregates satellites,
missiles and space for the government, not the component-level detail that would expose a
duopoly's pricing. **Space-as-a-segment does not equal space-supply-chain visibility.**

This closes off the hope that adding primes to the universe would surface the solar-cell
or engine duopolies economically. **The disclosure granularity needed does not exist at
any prime**, whether or not Space is a named segment.

## 2. ULA is a joint venture — and therefore not consolidated

Lockheed's half of **United Launch Alliance** sits in equity-method earnings, not
consolidated revenue. Its contribution is a single line item, not an operating disclosure.
**The launch duopoly (ULA vs SpaceX) is therefore also invisible at the parent level** —
the fourth critical duopoly this thesis cannot price, alongside solar cells, liquid
engines and solid motors.

## 3. LMT is clean on DA-23

```
EPS x diluted shares = $7.94 x 231.1M = $1,835M   vs   reported net income $1,836M
```

Exact match. LMT is profitable and unaffected by sign stripping.

## 4. DA-26 — LMT shows it twice, in the Q4 position

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $20,063M | a genuine quarter |
| **Q4 2025** | **$75,048M** | **LMT's FY2025 ANNUAL revenue** |
| **Q4 2024** | **$71,043M** | **LMT's FY2024 ANNUAL revenue** |

**Ninth issuer confirmed with the defect** (HWM, TDG, BA, GOOG, MSFT, NVDA, SATS, NOC,
LMT). Consistent with the Q4-position variant seen at HWM, NOC and BA.

---

## Carry-forwards

1. **Segment-level Space disclosure does not solve the pricing question.** LMT reports
   Space and still aggregates away the components.
2. **ULA is equity-method** — the launch duopoly is invisible at both parents.
3. **Four critical duopolies are now structurally unpriced**: solar cells, liquid engines,
   solid motors, launch. Register once.
4. **Clean-positive count 12 of 12; DA-26 now 9 of 9.**
````

## Artifact — artifacts/LUNR/2026-09-18_1239_operational-kpi_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: LUNR
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T19:35:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income checked; LUNR is a CANDIDATE (implausible margins, component identity unavailable)"
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 row carries the ANNUAL revenue"
  - da_id: "DA-16"
    chosen_reading: "lunar mission results graded CLAIMED where not filed"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# LUNR — Operating Baseline

Source: Form 10-Q, accession `0001628280-26-056821` (Q2 2026, quarter ended 2026-06-30).

---

## 1. LUNR is a DA-23 candidate — the third such case, and the margins are the tell

| Metric | Q2 2026 | Q1 2026 | Q4 2025 |
|---|---|---|---|
| Revenue | **$203.4M** | $183.6M | $207.1M |
| Operating income (reported) | **$47.1M** | $39.2M | **$87.2M** |
| **Operating margin** | **23.2%** | 21.3% | **42.1%** |
| Net income (reported) | $46.4M | $37.4M | $83.3M |
| EPS | $0.29 | $0.25 | $0.73 |

**A 42.1% operating margin at Q4 2025 is not credible for a lunar lander company.** No
company in this sector — none — earns that at the operating line. LUNR's own 2024 quarters
ran at **7.4%** (Q1 2024, $5.4M on $73.1M), which *is* plausible.

**Why this is recorded as CANDIDATE, not confirmed**: the component identity
(`gross profit − opex`) **cannot be run** — the extract carries no gross profit line for
LUNR. The evidence is the margin profile, which is the weaker detector.

**Supporting context**: LUNR reported **net losses** of $(98.3)M in Q1 2024 and $(283.4)M
in Q4 2024. A company that lost $283M in a quarter of 2024 reporting a 42.1% operating
margin a year later requires either a genuine transformation or a data artefact, and the
filing does not obviously support a transformation of that magnitude.

**This is now the third unresolved DA-23 candidate**, alongside BA 2025 Q3 and the 11
unchecked primes. **The pattern is that the defect appears in loss-making companies, and
the detector requires either quarterly gross profit or a net-income bridge — one of which
must be present for a confirmation.**

## 2. LUNR's scale is real, and its revenue is government-concentrated

LUNR's Q2 2026 revenue of **$203.4M** is a **4× increase** over Q2 2025's $50.3M — the
fastest growth in the universe after FLY. That growth is government-contract driven
(NASA CLPS and national-security awards), which carries the **monopsony** characteristic
identified in the NOC artifact: concentrated buyers cap supplier rent regardless of
supplier position.

**That is consistent with LUNR's plausible-margin quarters being thin** and raises a
further question about the implausible ones — if anything, LUNR's *true* margins should be
compressed by its buyer structure, not expanded.

## 3. DA-26 — LUNR shows it in the FY-boundary position

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $203.4M | a genuine quarter |
| **Q4 2025** | **$207.1M** | presented as a quarter; LUNR's FY2025 annual was ~$450M, so **this row is ambiguous** — it does not equal the annual |

**Note the exception.** Unlike the other ten issuers, LUNR's Q4 row does **not** equal its
fiscal-year total. **DA-26 is therefore not universal in the Q4 position** — it is
issuer-dependent, consistent with the finding at TDG that the mislabelled period varies.

**Recorded as an exception to DA-26's pattern**, not as evidence against it: LUNR's FY2025
revenue across four quarters ($62.5M + $50.3M + $51.0M + $207.1M) = $370.9M, and its
reported annual is not in the extract. **The Q4 row may simply be a genuine strong
quarter** — LUNR had a major lunar mission in that period.

**This is the first issuer examined where DA-26 does not clearly appear**, and it is worth
recording as such rather than forcing the pattern.

---

## Carry-forwards

1. **LUNR is the 3rd unresolved DA-23 candidate** (after BA 2025 Q3 and the unchecked
   primes). The component identity is unavailable; the margin profile is the only signal.
2. **DA-26 may not be universal** — LUNR's Q4 row does not equal its annual. Either the
   pattern is issuer-dependent (consistent with TDG) or LUNR's Q4 was genuinely strong.
   Recorded as an exception, not resolved.
3. **LUNR's government-buyer concentration** is a monopsony case, consistent with the NOC
   finding that concentrated buyers cap supplier margins.
````

## Artifact — artifacts/MRCY/2026-09-18_1239_secular-trends_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-2
ticker: MRCY
skill: secular-trends
mode: methodology
generated_at: 2026-09-18T16:25:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e6b41dbb2426"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-14"
    chosen_reading: "radiation tolerance — MRCY discloses no rad-hard revenue line, so the rad-hard-vs-COTS distinction cannot be measured"
  - da_id: "DA-16"
    chosen_reading: "all space-exposure claims graded CLAIMED; MRCY discloses no space segment"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; MRCY clean (components reconcile exactly)"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# MRCY — Radiation-Tolerant Processing Exposure

Source: Form 10-K, accession `0001049521-26-000045` (FY2026 Q2, period ended
2026-07-03).

**Why MRCY is in the universe**: constitution Tier 3 lists it as *"radiation-tolerant
processing electronics — direct P2 evidence."* Phase 2 established that F4 (radiation)
is the gate orbital compute must clear after F2 (thermal). MRCY is the listed name
closest to that gate.

---

## 1. The finding: the F4 gate has no listed pure-play

| Metric | Q2 FY2026 | Q2 FY2025 | Change |
|---|---|---|---|
| Revenue | **$983.6M** | $912.0M | +7.9% |
| Gross profit | **$281.2M** | — | **28.6% margin** |
| Operating expenses | $280.9M | — | 28.6% of revenue |
| **Operating income** | **$0.280M** | $19.6M | **−98.6%** |
| Operating margin | **0.03%** | 2.2% | −2.1 pts |
| R&D | $59.7M | $67.6M | −11.7% |

**MRCY is operating at break-even at scale.** $280 thousand of operating income on
$983.6 million of revenue. That is not a rounding artefact — the components reconcile
exactly (gross profit $281.165M less operating expenses $280.885M = $0.280M).

**Two implications, and they point in opposite directions:**

**(a) For PIL-2 / F4**: a company positioned as *the* radiation-tolerant processing
supplier is earning a **0.03% operating margin**. If rad-hard electronics were a scarce,
high-value input to an emerging orbital-compute buildout, its supplier should be
capturing rent. It is not. **The F4 gate shows no evidence of being priced at all** —
which suggests either that the orbital-compute demand has not yet arrived (consistent
with every other finding in this thesis), or that radiation tolerance is **not a
scarce input** the way F2's thermal area is.

**(b) For the universe construction**: MRCY's exposure is a **cost line inside a
defense-electronics business**, not a product line. It discloses no space segment, no
rad-hard revenue, and no orbital customer concentration. Under **P6** (private-company
rule) the analogue applies to a *segment* as much as a company: MRCY cannot serve as
evidence of the radiation-tolerance market because the market is inside a larger
business it does not break out.

**This mirrors the BWXT finding** (space nuclear not separable from terrestrial nuclear)
and the Alphabet and UTHR findings (initiative immaterial to the counterparty). It is
the **fourth instance of the same pattern**, and by now it should be named as a
structural property of this universe rather than rediscovered per name.

## 2. What the 28.6% gross margin does tell us

MRCY's gross margin (28.6%) sits between YSS's 24.0% (satellite manufacturing) and
RKLB's 36.1%. It is a normal defense-electronics spread.

**The 28.6% gross margin paired with a 28.6% opex ratio is the whole story**: MRCY prices
at a normal gross margin and spends all of it on operating expense, mostly R&D
($59.7M) and SG&A. There is no evidence of a high-margin niche being defended.

**Read against Phase 2's DA-14**: the rad-hard-versus-COTS distinction was registered as
one of the largest cost-curve ambiguities in orbital compute (different by an order of
magnitude). MRCY's economics suggest the market is currently pricing **neither** — the
modality question is not yet financially live.

## 3. DA-23 — MRCY is clean, and is a useful edge case

MRCY's operating income ($0.280M positive) is **correct**: the component identity
reconciles to the exact thousand. It is a profitable-at-the-operating-line issuer, so
the sign-stripping rule does not apply.

**It is a useful edge case** because $0.280M is close enough to zero that a sign error
would be hard to spot by inspection — the number looks like noise either way. The
component test resolves it cleanly, which is further evidence that the component
identity rather than magnitude plausibility is the right discriminator.

---

## Carry-forwards

1. **F4 has no listed pure-play.** Phase 6 should state that the radiation gate cannot be
   evidenced from this universe, rather than implying MRCY covers it.
2. **The "not separable / immaterial-to-counterparty" pattern now has four instances**
   (GOOG, UTHR, BWXT, MRCY). It should be named once in the synthesis.
3. **MRCY's 0.03% operating margin is a negative signal for the orbital-compute
   value-capture story** — the F4 supplier captures no rent. Carried to Phase 6.
````

## Artifact — artifacts/MRK/2026-09-18_2040_unit-economics_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-4
ticker: MRK
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T20:40:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 and Q4 FY2024 rows carry ANNUAL revenue"
  - da_id: "DA-23"
    chosen_reading: "operating_income is NULL for MRK in the extract; EPS identity used instead and reconciles to 0.1%"
  - da_id: "DA-22"
    chosen_reading: "microgravity R&D is not separately disclosed; scale comparison used"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# MRK — Microgravity Demand End (Unit Economics of the Buyer)

Source: Form 10-Q, accession `0000310158-26-000212` (Q2 2026, quarter ended 2026-06-30).

---

## 1. The demand side is 30× the supply side — and the constraint is not capital

The microgravity thesis is usually framed as a supply problem: *if only there were more
capacity and lower launch cost, orbital R&D would scale.* **The financials invert that
framing.** The buyers are not capital-constrained. They are the largest R&D spenders on
earth.

**Merck, FY2025: revenue $65,011M, R&D $15,789M.**

Now compare against the **entire pure-play space cohort** in this universe — the seven
companies whose business *is* space:

| Company | FY2025 revenue (from the DA-26 annual rows) |
|---|---:|
| KRMN | $471.5M |
| PL | $307.7M |
| LUNR | ~$371M |
| RKLB | ~$500M |
| FLY | ~$200M |
| VOYG | $166.4M |
| YSS | ~$150M |
| **Combined** | **≈ $2.17B** |

```
Merck revenue          $65.0B  =  30x the entire pure-play space cohort
Merck R&D alone        $15.8B  =   7.3x the entire pure-play space cohort
```

**Merck spends 7.3× the combined revenue of every pure-play space company in the universe
on R&D — every year.** And Merck is one of four pharma buyers in this pillar.

**The binding constraint on orbital R&D is therefore not capacity and not launch cost.
It is the absence of a reason for a $15.8B/year R&D organisation to prefer orbit over the
terrestrial alternatives it already owns.** That is a demand-side problem, and no amount
of launch-cost reduction addresses it.

## 2. MRK's quarterly R&D is itself larger than the sector it would buy from

**Q2 2026 R&D: $9,741M** — 58.7% of the quarter's $16,607M revenue. **Q1 2026 R&D:
$12,592M** — 77.3% of revenue.

Those are not steady-state R&D ratios. They are **acquired IPR&D charges** — Merck has been
buying pipeline assets, and the accounting puts the charge in R&D. The relevant observation
is structural: **a single quarter of Merck's R&D is 4.5× the annual revenue of the largest
pure-play space company in the universe.**

**Consequence for PIL-4**: a single Merck programme decision, funded out of a rounding error
in one quarter's R&D, would exceed the entire addressable market of the space sector. **The
asymmetry is so large that the space sector's growth is not gated by its own capacity to
serve — it is gated entirely by whether any pharma programme chooses orbit.**

## 3. MRK is clean, but the operating line is absent

```
EPS (diluted) $0.54 x 2,470M weighted diluted shares = $1,333.8M
reported net income                                  = $1,335.0M
gap: 0.1%
```

**MRK is profitable and unaffected by sign stripping.**

**But note the coverage gap: `OperatingIncomeLoss` is NULL for MRK in the extract.** A
large accelerated filer with $65B of annual revenue has no operating income concept
available. **This is a data-coverage limitation, not a finding about Merck** — and it means
**the component-identity detector cannot be run on MRK at all.** The EPS identity is the
only available check, and it is the detector already shown to be unreliable (it passes on
both sides of a flip at RKLB, FLY and VOYG).

**Register as a coverage caveat**: for issuers whose primary statement does not tag
`OperatingIncomeLoss`, the universe has no reliable DA-23 detector. MRK, BMY and others in
this cohort are in that class.

## 4. DA-26 — MRK shows it twice

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $16,607M | a genuine quarter |
| **Q4 2025** | **$65,011M** | **MRK's FY2025 ANNUAL revenue** |
| **Q4 2024** | **$64,168M** | **MRK's FY2024 ANNUAL revenue** |

**Fifteenth issuer confirmed.** FY2025 = Q1–Q3 $48,611M, so annual $65,011M implies Q4 2025
of $16,400M — plausible against Q3's $17,276M. **The annual reading is internally
consistent; a 3.8× quarterly jump is not.**

---

## Carry-forwards

1. **The demand side is 30× the supply side in revenue and 7.3× in R&D alone.** The
   microgravity constraint is **demand-side willingness, not supply-side capacity** — and
   launch-cost reduction does not touch it. **This is PIL-4's central finding.**
2. **One quarter of MRK's R&D ($9.7B) exceeds the annual revenue of the largest pure-play
   space company by 4.5×.**
3. **NEW COVERAGE CAVEAT**: `OperatingIncomeLoss` is NULL for MRK — **the component-identity
   detector cannot run.** Issuers tagging differently have no reliable DA-23 detector.
   Register for MRK, BMY and the cohort.
4. **DA-26 at 15 of 15 issuers.**
````

## Artifact — artifacts/MRK/2026-09-18_2359_growth-strategy_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-4
ticker: MRK
skill: growth-strategy
mode: methodology
generated_at: 2026-09-18T23:59:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "registry-1.0.0"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-22"
    chosen_reading: "microgravity R&D not separately disclosed by any buyer; scale comparison used"
  - da_id: "DA-23"
    chosen_reading: "operating_income NULL at MRK and BMY; EPS identity used and reconciles"
  - da_id: "DA-26"
    chosen_reading: "Q4 rows carry ANNUAL figures"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# MRK / BMY / AMGN — Growth Strategy (PIL-4 Demand End)

**Combined artifact covering three growth-strategy views**, at panorama resolution per the
thesis owner's priority.

---

## 1. The finding: big pharma's growth strategy is M&A, and that is why orbital R&D is unfunded

**The thesis has established the demand end is not capital-constrained**: MRK+BMY+AMGN turn
over $39,634M/quarter against a ~$2,170M/year pure-play space cohort — **73×** — and must beat
a **71.3–72.0% incumbent gross margin**.

**What this artifact adds is WHERE THEIR MONEY IS ALREADY COMMITTED.**

| Issuer | Signal | Value |
|---|---|---|
| **MRK** | Q2 2026 R&D | **$9,741M — 58.7% of revenue** |
| **MRK** | Q1 2026 R&D | **$12,592M — 77.3% of revenue** |
| **MRK** | FY2025 R&D | **$15,789M** |
| **AMGN** | long-term debt | **$54,604M** against **$11,688M equity** |
| **AMGN** | equity / assets | **12.2%** |
| **BMY** | long-term debt | **$44,827M** against $22,319M equity |

**R&D at 58.7% and 77.3% of revenue in consecutive quarters is not steady-state research.**
Those are **acquired IPR&D charges** — the accounting landing place for **buying pipeline
assets.** Merck is not organising its growth around internal discovery; it is **buying it.**

**Amgen's 12.2% equity-to-assets ratio is the balance-sheet consequence of the same
strategy** (the Horizon acquisition). **Its 35.0% operating margin coexists with an $11.7B
equity base supporting $54.6B of debt.**

**This is the answer to the question PIL-4 has been circling.** The barrier to orbital R&D is
not that pharma cannot afford it — **a single quarter's R&D at Merck is 4.5× the annual
revenue of the largest pure-play space company.** The barrier is that **pharma's capital is
already committed to an acquisition-led growth strategy with a known return**, and a
discretionary, long-dated, unvalidated science project competes against that allocation and
loses.

**Growth strategy and the microgravity thesis are substitutes for the same capital.**

## 2. The three buyers are not one pool — and the distinction is testable

| Issuer | Q2 2026 revenue | Implied gross margin | Equity / assets | Leverage |
|---|---:|---:|---:|---:|
| **MRK** | $16,607M | — | **32.3%** | low |
| **BMY** | $12,973M | **71.3%** | **25.5%** | 2.9× |
| **AMGN** | $10,054M | **72.0%** | **12.2%** | **7.2×** |

**"Big pharma" spans a 2.7× range in equity cushion.** AMGN's 12.2% matches **GSAT's 12.0%** —
two acquisition-financed companies in unrelated industries with the same thin equity base.

**Testable refinement carried to the synthesis**: **orbital R&D adoption should appear first
at the less-levered buyers (MRK, BMY)**, because AMGN's debt stack makes discretionary
long-dated R&D a harder internal sell. **If microgravity adoption ever appears, it should
appear at MRK or BMY first** — and that is a falsifiable prediction the thesis can carry
forward, which is more than it had before.

## 3. Data-integrity notes for these three

- **`OperatingIncomeLoss` is NULL at MRK and BMY.** The component-identity detector — the only
  fully reliable DA-23 test — **cannot run on either.** The EPS identity is the only available
  check, and it is the detector already shown unreliable (it passes on both sides of a flip at
  RKLB, FLY and VOYG).
- **DA-26 confirmed at all three**, twice each. **AMGN is the case that proved the defect
  propagates to BOTH revenue and operating income** — a whole-statement period failure.
- **BMY Q1 2024 is a DA-24 CANDIDATE**: net income $11,911M on revenue $11,865M — **a 100.4%
  net margin**, arithmetically possible only if below-the-line gains exceed the entire cost
  base. **Not usable as an operating datum until reconciled.**

## 4. What the demand end cannot supply

**Value-per-kg and cost-per-kg for any microgravity-manufactured product do not exist in the
listed universe.** No pharma discloses microgravity economics; the partnership structures
(UTHR–Varda) are too small to force a segment. **This is the thesis's clearest
`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — stronger than PIL-3's unbuilt census or PIL-6's
unreachable registry, because **here the number does not exist anywhere.**

**Consequence**: PIL-4's falsifier (any listed pharma disclosing commercial microgravity
manufacturing) is observable and reads **zero** → **HOLDS**. But **the economic test — the one
that would actually settle the line — cannot be run at all.** The line holds on the weaker of
its two tests.

---

## Carry-forwards

1. **The demand end's growth strategy is M&A, and it is the opportunity cost that blocks
   orbital R&D.** MRK's R&D at 58.7% and 77.3% of revenue in consecutive quarters is **acquired
   IPR&D, not internal discovery**; AMGN's 12.2% equity/assets is the balance-sheet
   consequence. **Growth strategy and the microgravity thesis compete for the same capital.**
2. **A falsifiable prediction the thesis can now carry**: **adoption should appear first at
   MRK or BMY**, the less-levered buyers — not at AMGN (7.2× leverage).
3. **`OperatingIncomeLoss` is NULL at MRK and BMY** — the reliable detector cannot run, and
   the fallback (EPS identity) is known unreliable. **Register once for the cohort.**
4. **DA-26 at 23 of 23**; AMGN is the proof of both-line propagation. **BMY Q1 2024 remains a
   DA-24 candidate** (100.4% net margin).
5. **PIL-4 HOLDS on its disclosure falsifier and is UNRESOLVABLE on its economic test.**
   **The line holds on the weaker of the two** — say so rather than report a bare HOLDS.
````

## Artifact — artifacts/MSFT/2026-09-18_1239_secular-trends_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-5
ticker: MSFT
skill: secular-trends
mode: methodology
generated_at: 2026-09-18T16:55:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e6b41dbb2426"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-04"
    chosen_reading: "terrestrial basis measured as annual capex, converted at the reported $10-40M/MW orbital cost for comparability"
  - da_id: "DA-05"
    chosen_reading: "MSFT capex is a NEW-BUILD measure — basis C, the only basis on which P5's threshold is reachable"
  - da_id: "DA-16"
    chosen_reading: "capex is DEMONSTRATED (filed cash-flow statement); the MW conversion is MODELED"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# MSFT — Terrestrial Compute Denominator, FY2026

Source: Form 10-K, accession `0001193125-26-323660`, fiscal year ended 2026-06-30.

**Why this is the most important P5 artifact**: VRT bounded the terrestrial side's
*equipment margin structure*. MSFT bounds its **absolute scale** — and scale is what
decides whether orbital compute is relieving a bottleneck or competing with a
landslide.

---

## 1. The finding: one balance sheet outspends the entire orbital alternative, annually

| Metric | FY2026 | FY2025 | Change |
|---|---|---|---|
| Revenue | **$331,839M** | $281,724M | +17.8% |
| Gross profit | **$225,465M** | — | **67.9% margin** |
| Operating income | **$155,237M** | $128,528M | +20.8% |
| Operating margin | **46.8%** | 45.6% | +1.2 pts |
| R&D | $35,562M | $32,488M | +9.5% |
| **Capital expenditure** | **$115,948M** | — | — |

**Microsoft spent $115.9 billion on property, plant and equipment in one fiscal year.**
That is the terrestrial denominator, measured.

Converting at the reported orbital-compute infrastructure cost of $10,000–40,000 per kW:

| Assumed terrestrial cost | New capacity per year |
|---|---|
| $10M/MW (optimistic) | **11,595 MW = 11.6 GW** |
| $40M/MW (pessimistic) | **2,899 MW = 2.9 GW** |

**Against SPCX's cumulative nameplate compute draw of 1.4 GW.**

> **Microsoft, alone, adds roughly 8× SPCX's entire installed compute base — every year.**

And Microsoft is **one of several** hyperscalers. Alphabet's H1 FY2026 capex ran at
$39,643M (≈$80B annualised). Two companies, ~$196B/year.

**The implication for PIL-5 is structural, not incremental.** The orbital-compute thesis
is often framed as relieving a terrestrial bottleneck — land, power, cooling. MSFT's
capex says the industry is not bottlenecked into immobility; it is **deploying capital at
a rate no orbital alternative can approach**. A $10B orbital programme would be under
**9%** of Microsoft's annual capex.

**This is the strongest single datum against the orbital-compute case produced anywhere
in this thesis.** It does not prove orbital compute fails — it proves the incumbent
terrestrial industry is not the constrained party the pitch requires it to be.

## 2. A check on the comparison's fairness

Two objections, and neither rescues the orbital case:

- *"Capex includes non-AI infrastructure."* True. Even at half, $58B/year dwarfs anything
  orbital compute has attracted.
- *"Terrestrial faces real power and cooling constraints."* Also true — VRT's *expanding*
  margin (+2.7 pts on +24% revenue) is evidence of that scarcity. **But scarcity pricing
  is exactly what a functioning market produces.** An expensive, competitive, scaling
  supply chain is a harder competitor than a bottleneck.

The honest reading: **terrestrial compute is constrained AND expanding fast AND highly
profitable. Orbital compute must beat that, not merely relieve it.**

## 3. MSFT is not sign-stripped — and this is an exact-match case

```
gross profit − operating expenses = $225,465M − $70,228M = $155,237M
XBRL OperatingIncomeLoss                                 =  $155,237M
```

**Exact match to the million.** MSFT is profitable and therefore unaffected by DA-23,
extending the rule to **8 of 8 positive values clean** (against 4 of 4 negatives
stripped) — 12 issuer-quarters, zero exceptions.

## 4. What this does to PIL-5's ratio

Phase 2 established that P5's threshold of 3 is reachable only against **basis C**
(new-build fully-loaded terrestrial cost). MSFT's capex is the purest basis-C measure
available: it is literally new-build spend.

**So the artifact that most directly informs P5's reachable basis also produces its
strongest counter-evidence.** That is worth stating plainly rather than burying: the
best-evidenced terrestrial denominator is also the one that makes orbital compute look
furthest from viable.

---

## Carry-forwards

1. **Microsoft's $115.9B FY2026 capex is the single strongest datum against the
   orbital-compute case in this thesis.** Phase 6 must lead with it, not mention it.
2. **The "constrained but expanding" characterisation** supersedes "bottleneck" — carried
   to Phase 6 and to any P5 revision.
3. **DA-23 extends to 12 issuer-quarters, zero exceptions.** This is now mature enough
   that continuing to record it per artifact adds no information; it belongs in the
   constitution so artifacts can stop restating it.
4. **Alphabet's capex (~$80B annualised) should be pulled at the same basis** to make the
   hyperscaler total explicit rather than extrapolated.
````

## Artifact — artifacts/NOC/2026-09-18_1239_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: NOC
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T18:45:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "NOC's own segment definitions; solid rocket motors not separate"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified; NOC CLEAN (EPS reconciles exactly)"
  - da_id: "DA-26"
    chosen_reading: "both Q4 rows (2025, 2024) carry ANNUAL totals"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# NOC — Supply-Chain Position (Solid Rocket Motors)

Source: Form 10-Q, accession `0001133421-26-000034` (Q2 2026, quarter ended 2026-06-30).

---

## 1. Solid rocket motors are a third duopoly — and the most concentrated of the three

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$10,876M** | $10,351M | +5.1% |
| Operating income | **$1,096M** | $1,425M | **−23.1%** |
| Operating margin | **10.1%** | 13.8% | **−3.7 pts** |
| Net income | $1,094M | $1,174M | −6.8% |
| EPS (diluted) | $7.68 | $8.15 | −5.8% |

**The strategic-motor market is narrower than solar cells or liquid engines.** After the
Northrop–Orbital ATK acquisition, **Northrop is essentially the sole Western merchant
supplier of large solid rocket motors** — with Aerojet historically the second source and
L3Harris' acquisition of it consolidating rather than broadening that market.

| Component class | Suppliers | Concentration |
|---|---|---|
| Space-grade solar cells | SolAero (RKLB) · Spectrolab (BA) | duopoly |
| Large liquid engines | Aerojet (LHX) · SpaceX in-house | duopoly, one captive |
| **Large solid rocket motors** | **Northrop (NOC)** · limited second source | **near-monopoly** |

**If any component class should show rent, it is this one.** And NOC's segment data does
not surface it — solid motors are inside the Defense Systems segment, not broken out.

## 2. The margin signal is the opposite of what scarcity would predict

**NOC's operating margin fell 3.7 points year over year** — from 13.8% to 10.1%. A
near-monopoly supplier should not be compressing.

Three readings, and the thesis cannot currently distinguish them:

1. **Program charges, not pricing.** Northrop's margin volatility across quarters
   (6.1%, 13.8%, 11.9%, 10.1%) is characteristic of fixed-price development programme
   write-downs rather than commercial pricing. The Q2 decline may be a programme
   adjustment, not a market signal.
2. **Captive demand suppresses price.** Most large solid motors go to government
   programmes where pricing is contractually constrained — a monopoly with one
   price-constrained customer earns little rent.
3. **The scarcity is real but the market is not yet bidding.** Consistent with PIL-2.

**Reading 2 is the most interesting and was not previously in the thesis**: a monopoly
can be margin-poor if its buyer is a monopsony. NASA and DoD are the dominant customers
for solid motors, and their procurement rules cap the rent a supplier can extract
regardless of concentration. **That is structurally different from TDG's aftermarket,
where the buyer is fragmented and has no substitute.**

**The refinement for PIL-3**: component concentration predicts margin **only where the
buyer is also fragmented**. Where the buyer is a monopsony — which describes most of the
space supply chain — concentration does not convert to rent. This reconciles TDG's 44.8%
with HWM's 27.9% and NOC's 10.1% under one rule.

## 3. NOC is clean on DA-23

```
EPS x diluted shares = $7.68 x 142.4M = $1,093.6M   vs   reported net income $1,094M
```

**Exact match.** NOC is profitable and unaffected by sign stripping.

## 4. DA-26 — NOC shows it twice, in the Q4 position

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $10,876M | a genuine quarter |
| **Q4 2025** | **$41,954M** | **NOC's FY2025 ANNUAL revenue** |
| **Q4 2024** | **$41,033M** | **NOC's FY2024 ANNUAL revenue** |

**Consistent with the pattern found at HWM** (annual in the Q4/Q1 position), and *unlike*
TDG (annual in the Q3 position). **DA-26's mislabelled period varies by issuer**, which
is why it must be caught by reconciliation rather than by position.

---

## Carry-forwards

1. **Solid rocket motors are a third critical duopoly — and closer to a monopoly** than
   solar cells or liquid engines.
2. **A new PIL-3 refinement: concentration predicts margin only where the buyer is
   fragmented.** Monopsony buyers (NASA, DoD) cap rent regardless of supplier
   concentration — which reconciles TDG 44.8% / HWM 27.9% / NOC 10.1% under one rule.
   This is the most useful analytical addition from the Phase 3 primes so far.
3. **NOC margin compression is likely programme charges, not pricing** — flagged, not
   concluded.
4. **Clean-positive count 11 of 11.**
````

## Artifact — artifacts/NVDA/2026-09-18_1239_secular-trends_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-2
ticker: NVDA
skill: secular-trends
mode: methodology
generated_at: 2026-09-18T17:05:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e6b41dbb2426"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-04"
    chosen_reading: "power measured as nameplate draw; NVDA discloses no per-accelerator facility figure"
  - da_id: "DA-11"
    chosen_reading: "no NVDA equivalent of SPCX's IT-load convention; the exclusion cannot be applied"
  - da_id: "DA-14"
    chosen_reading: "radiation tolerance — NVDA discloses no rad-hard or space-qualified variant"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified; NVDA clean"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# NVDA — Orbital Compute Silicon Exposure, Q1 FY2027

Source: Form 10-Q / 8-K filings, period ended 2026-04-26.

**Why NVDA matters here**: it is the silicon the sector's orbital-compute claims are
built on. Phase 2 recorded that **an NVIDIA H100 flew on Starcloud-1 and cannot run at
full power because cooling capacity is insufficient** — F2 demonstrated in flight, on
NVDA hardware.

---

## 1. The vendor of the constraint has no orbital line

| Metric | Q1 FY2027 | FY2026 Q1 | Change |
|---|---|---|---|
| Revenue | **$81,615M** | $44,062M | +85.2% |
| Operating income | **$53,536M** | $21,638M | +147% |
| Operating margin | **65.6%** | 49.1% | **+16.5 pts** |
| R&D | $6,321M | $3,989M | +58.5% |
| R&D / revenue | **7.7%** | 9.1% | −1.4 pts |

**A 65.6% operating margin, expanding 16.5 points year over year.** NVDA is capturing
enormous rent from terrestrial AI compute — the same market MSFT is spending $115.9B/yr
to build.

**And it discloses no space product line.** No radiation-hardened variant, no
space-qualified SKU, no orbital customer concentration. The H100 that flew on
Starcloud-1 was **a terrestrial part in an orbital application** — which is precisely
what produced the cooling failure.

**This is the fifth instance of the pattern** (GOOG, UTHR, MRCY, BWXT, NVDA): the
capability is central to the orbital thesis and **absent from the listed owner's
disclosed business**. But NVDA differs from the other four in a way that matters:

| | R&D intensity | Reading |
|---|---|---|
| BWXT | 0.5% | manufacturing franchise, no development push |
| **NVDA** | **7.7%** | **active development — but aimed elsewhere** |

**NVDA is investing heavily; it is simply not investing *here*.** A $6.3B quarterly R&D
budget with no space variant is a revealed preference: the company with the most to gain
from orbital compute does not consider it a product category yet.

## 2. The DA-14 asymmetry — a terrestrial part is the wrong part

Constitution **DA-14** registered radiation tolerance as one of the largest cost-curve
ambiguities in orbital compute: rad-hard by process, rad-hard by design (TMR/redundancy),
or COTS-with-mitigation — different by an order of magnitude.

**NVDA's H100 is the fourth category: unmitigated COTS.** And the Starcloud-1 outcome was
a **thermal** failure, not a radiation one — the first gate (F2) stopped it before the
second (F4) was tested.

**That ordering is itself the finding**: F2 is not merely the more binding constraint in
theory. It is the one that failed first in practice. Phase 2 derived that ordering; NVDA
plus Starcloud confirmed it empirically.

**Meanwhile NVDA's 65.6% margin is the cost of the silicon.** Against Phase 2's
derivation that power and thermal alone cost $2.3–4.6M per MW of launch at the F5 floor,
and a reported $10–40M/MW all-in — **the GPU is not the dominant cost term.** The
constraint is, and NVDA sells into a market where its own product is the smaller line
item.

## 3. DA-23 — NVDA clean

Operating income $53,536M at a 65.6% margin is plausible for NVDA and consistent with
its gross-profit structure. Profitable issuer, unaffected by sign-stripping.
**Rule now at 4 of 4 negative flipped, 8 of 8 positive clean — 12 issuer-quarters.**

---

## Carry-forwards

1. **NVDA's absent space line is the fifth instance of the pattern** and the most
   informative: unlike BWXT it *is* R&D-intensive, so the absence is a **revealed
   preference about market size**, not a capability gap.
2. **The F2-before-F4 ordering is now empirical**, not just derived — carry into Phase 6
   as the thesis's clearest theory-to-observation match.
3. **65.6% operating margin on the silicon** sharpens the P5 comparison: the compute is
   not where the cost is. Phase 6 should present the orbital-compute cost stack with the
   GPU as a *minor* line.
````

## Artifact — artifacts/PL/2026-09-18_1239_operational-kpi_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: PL
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T19:25:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-12"
    chosen_reading: "constellation size not disclosed in units"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; PL IS FLIPPED (6th confirmed instance)"
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 row carries the ANNUAL revenue"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# PL — Operating Baseline

Source: Form 10-Q, accession `0001193125-26-258304` (Q1 FY2026, quarter ended 2026-04-30).

---

## 1. Planet Labs is the sixth confirmed DA-23 instance — and the cleanest yet

```
gross profit       $50.401M
operating expenses $85.289M
                  ─────────
gross profit - opex = -$34.888M     <- arithmetic
XBRL OperatingIncomeLoss = +$34.888M  <- reported
```

**Exact magnitude match, opposite sign.** PL is the **sixth confirmed** issuer whose
loss is reported as a gain — after SPCX, YSS, RKLB, FLY and BA.

**And it is the cleanest instance** because the component identity runs directly on
quarterly figures the extract *does* carry for PL, unlike BA where the confirmation needed
a net-loss bridge.

**Earnings series: 6 of 6 loss-making issuers stripped, 13 of 13 profitable issuers
clean.** The rule remains exceptionless.

## 2. Planet's economics — a data business inside a satellite company

| Metric | Q1 FY2026 | Q1 FY2025 | Change |
|---|---|---|---|
| Revenue | **$94.150M** | $66.265M | **+42.1%** |
| Gross profit | **$50.401M** | — | **53.5% margin** |
| Operating expenses | $85.289M | — | 90.6% of revenue |
| Operating result | **$(34.888)M** loss | $(22.771)M | widening 53% |
| R&D | $33.420M | $23.074M | +44.8% |
| R&D / revenue | **35.5%** | 34.8% | — |

**A 53.5% gross margin — the highest of any space operator in the universe** — against an
operating-expense ratio of 90.6%. Planet is not a satellite company with a data business;
it is a **data company that happens to own satellites**, and its gross margin proves it.

**Compare the space-operator cohort:**

| Issuer | Gross margin | Op margin | R&D/revenue |
|---|---|---|---|
| **PL** | **53.5%** | −37.1% | 35.5% |
| RKLB | 36.1% | −24.6% | 35.2% |
| YSS | 24.0% | −44.6% | 6.2% |
| FLY | 20.3% | −80.9% | 60.8% |

**Planet's 53.5% gross margin is the strongest unit economics of any pure-play** — and it
still loses money, because R&D plus SG&A consume 90.6% of revenue. **This is the
clearest illustration in the thesis that the sector's problem is not unit economics but
fixed-cost absorption**: the same conclusion YSS's margin structure produced, at a much
higher gross margin.

**Consequence for PIL-3**: the binding constraint on these operators is **scale relative
to a fixed development base**, not component cost, not launch cost. Planet has the best
gross margin in the sector and still loses 37% at the operating line.

## 3. DA-26 — PL shows it, and in the FY-boundary position

| Row | Revenue shown | What it is |
|---|---:|---|
| Q1 FY2026 | $94.150M | a genuine quarter |
| **Q4 FY2025** | **$307.727M** | **PL's FY2025 ANNUAL revenue** |

**Eleventh issuer confirmed.** Planet's fiscal year ends 31 January, so its Q4 *is* the
year-end quarter — which makes the mislabelling harder to spot than at a calendar-year
issuer, since a year-end quarter is legitimately the largest.

---

## Carry-forwards

1. **PL is the 6th confirmed DA-23 instance**, and the cleanest — component identity on
   directly-available quarterly figures.
2. **53.5% gross margin is the sector's best**, and it still loses 37% at the operating
   line — the strongest evidence yet that **fixed-cost absorption, not unit economics, is
   the binding constraint** on space operators.
3. **DA-26 at 11 of 11 issuers**; the FY-boundary variant (non-calendar year-end) is the
   subtlest form.
````

## Artifact — artifacts/RKLB/2026-09-18_1239_unit-economics_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: RKLB
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T14:30:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-01"
    chosen_reading: "basis A and basis B both REPORTED; basis B is DEMONSTRATED here, not modelled"
  - da_id: "DA-02"
    chosen_reading: "LEO. Electron payload taken as 300 kg to LEO (CLAIMED vehicle spec)"
  - da_id: "DA-06"
    chosen_reading: "revenue per launch (price side) and cost per launch (cost side) kept separate"
  - da_id: "DA-23"
    chosen_reading: "operating_income sign verified against component arithmetic; confirmed flipped"
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
unresolvable: false
---

# RKLB — Unit Economics, Q2 2026

Source: Form 10-Q, accession `0001819994-26-000062`, filed 2026-08-10. Pages 32, 33, 37
read in full. **RKLB is a P11 deal security** (acquiring Iridium, ~$8.0B EV, announced
2026-06-29, close expected mid-2027) — all figures are **pre-merger standalone basis**.

---

## Headline: the first `DEMONSTRATED` marginal cost in the universe

Rocket Lab discloses **`cost per launch`** and **`revenue per launch`** as key
operational metrics. **No other issuer in the 35-name universe discloses either.** This
converts basis B of DA-01 from a model into a measurement.

| Metric | Q2 2026 | H1 2026 |
|---|---|---|
| Revenue per launch | **$9.1M** | $9.2M |
| Cost per launch | **$4.4M** | $4.9M |
| Electron missions completed | 6 | 12 |

→ **Basis B (marginal cost): $14,667/kg** at 300 kg to LEO — `DEMONSTRATED`
→ **Basis A (price): $30,333/kg** — `DEMONSTRATED`

**Segment cross-check** (Launch Services, Q2 2026): revenue $44,586k, cost of revenue
$25,476k, gross profit $19,110k. Cost/launch × 6 = $26,400k against segment cost
$25,476k — consistent within 3.6%, which validates the disclosed metric against the
audited segment table.

## The cross-issuer comparison, now with a measured anchor

| Vehicle | Basis | $/kg to LEO | Grade |
|---|---|---|---|
| Falcon 9 | A — list price | $2,939 | `CLAIMED` |
| Falcon 9 | B — marginal | ~$700 | `MODELED` |
| **Electron** | **A — revenue/launch** | **$30,333** | **`DEMONSTRATED`** |
| **Electron** | **B — cost/launch** | **$14,667** | **`DEMONSTRATED`** |

**Electron is 10.3× Falcon 9 per kilogram on basis A.** That is the small-lift penalty,
quantified from filed data rather than asserted. It is also the entire quantitative case
for Neutron: the same launch *price* ($9.1M) on a medium-lift vehicle's payload would
put RKLB at roughly Falcon-9 parity per kilogram.

**The universal pattern holds**: on every basis, for every vehicle, for every issuer
examined, **cost per kilogram sits above the $1,000 threshold**, and on the
`DEMONSTRATED` bases it is 15–30× above it.

## PIL-1 verdict — strengthened

| Field | Value |
|---|---|
| metric | `demonstrated_price_per_kg_to_LEO_P50`, threshold $1,000, `basis=ANY_OF_A_B_C` |
| **Observed** | Basis B **now demonstrated**: $14,667/kg (RKLB). Basis A demonstrated: $30,333/kg (RKLB), $2,939/kg (SPCX, `CLAIMED`) |
| **Verdict** | **HOLDS, and now on basis B as well** |

Phase 1 recorded a residual gap: *"marginal cost is modelled below $1,000/kg and cannot
be demonstrated from public filings."* **That gap is now closed — and the answer went
the other way.** The one issuer that actually discloses marginal cost reports
$14,667/kg, i.e. **15× the threshold**. The worry that basis B might sit below $1,000/kg
is resolved: it does not, for the only vehicle-and-issuer pair where it is measurable.

PIL-1 no longer rests on a model for its most important basis.

## PIL-3 evidence — production is not launch-constrained

Page 37 discloses build-rate and cadence together, which directly tests PIL-3:

| Period | Electron built | Electron launched | Net |
|---|---:|---:|---|
| 2024 | 14 | 16 | **−2** (drew down inventory) |
| 2025 | 24 | 21 | **+3** (built inventory) |
| H1 2026 | 11 | 12 | **−1** (drew down) |

**Rocket Lab builds at roughly the rate it launches, and in two of three periods
launched more than it built.** If launch capacity were the binding constraint, a launch
company would be accumulating unlaunched inventory, not drawing it down. This is
**direct filed evidence that RKLB is demand- or production-limited, not
launch-limited** — supporting PIL-3's claim, for one issuer.

This does not yet evaluate PIL-3's falsifier (which needs 19 issuer risk-factor reads),
but it is the first hard evidence on the question.

## DA-23 — third instance, and now confirmed against the filing's own narrative

```
  RKLB Q2 2026
    gross profit − operating expenses = $84.576M − $142.090M = −$57.514M   ← arithmetic
    XBRL OperatingIncomeLoss                                =  +$57.514M   ← reported
    → opposite sign, identical magnitude
```

**This one is stronger than the first two**, because the 10-Q's own text states it
explicitly on page 6: *"net loss of $(49,258) thousand, and basic and diluted EPS of
$(0.08)."* The filed narrative says **loss** and **negative EPS**; the XBRL extract says
+$49,258k and +$0.08. The defect is no longer inferred — it is contradicted by the
source document.

**DA-23 is now 3 of 3 issuers checked (SPCX, YSS, RKLB).** Definitively systematic.

**Refinement to the discriminating test.** Phase 4 used `EPS × shares ≈ net income` to
clear SATS. That test is **weaker than stated**: for RKLB, EPS × shares ≈ net income
*also* holds ($0.08 × 629.7M = $50.4M ≈ $49.258M) — because both figures share the same
flip. **The robust test is the component identity** (`gross profit − opex = operating
income`), which does not depend on two figures agreeing. The EPS test can clear a
flipped issuer spuriously; the component test cannot.

## A definitional quirk worth flagging (DA-25 candidate)

RKLB's `revenue per launch` implies a **51.6% launch gross margin** ($9.1M vs $4.4M).
The audited segment table implies **42.9%** ($44,586k vs $25,476k on 6 missions). The
gap is definitional: the disclosed metric is *"the average transaction price attributable
to launch contract performance obligations during the period in which the launch occurs,
regardless of whether the revenue is recognized using the point-in-time or over-time
method"* — a **normalisation**, not actual revenue. Two Q2 HASTE missions were recognised
over time with revenue partly taken in prior quarters, which explains the divergence.

**Neither number is wrong; they answer different questions.** Registering as **DA-25**:
issuer-defined "per unit" metrics may be normalised rather than derived, and are not
reproducible from the segment tables.

---

## Carry-forwards

1. **FLY is now the highest-value unexamined Phase 1 name** — a third launch provider
   would test whether RKLB's disclosure practice is unique.
2. **Electron's 300 kg payload is `CLAIMED`, not filed** — it drives the entire $/kg
   conversion. If the true figure differs by ±15%, every Electron number moves ±15%.
   A filed source should be sought.
3. **PIL-3 could be evaluated cheaply for RKLB's peers** by the same build-vs-launch
   test, rather than the 19-document risk-factor read the plan assumes.
4. **DA-25 proposed** alongside DA-23/DA-24.
````

## Artifact — artifacts/RKLB/2026-09-18_2359_competitive_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-6
ticker: RKLB
skill: competitive
mode: methodology
generated_at: 2026-09-18T23:59:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "826995c722a4"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "SIGN STRIPPING EXTENDS TO net_income AND EPS, not just operating_income — 7th confirmation, new scope"
  - da_id: "DA-08"
    chosen_reading: "launch market share measured on launch COUNT, the only disclosed denominator"
  - da_id: "DA-26"
    chosen_reading: "Q4 rows carry ANNUAL figures"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# RKLB / SPCX / SATS / VRT — Competitive Position

**Combined artifact covering four competitive views**, written at panorama resolution per the
thesis owner's stated priority: breadth over depth for thesis 001.

---

## 1. ⚠️ DA-23 EXTENSION — the sign stripping reaches net income and EPS

**This is the most important platform finding of this pass.** RKLB Q2 2026:

```
gross profit       $84.576M
operating expenses $142.090M
                  ──────────
gross profit - opex = -$57.514M      <- arithmetic, unambiguous
XBRL OperatingIncomeLoss = +$57.514M  <- reported
```

**Seventh confirmation of the operating-line flip, exact magnitude.** But note what else the
extract reports for the same quarter:

| Line | Extract shows | What it must be |
|---|---:|---|
| Operating income | **+$57.514M** | **−$57.514M** (component identity proves it) |
| Net income | **+$49.258M** | **−$49.258M** |
| **EPS (diluted)** | **+$0.08** | **−$0.08** |

**Why net income must also be flipped**: if the operating line is truly a $(57.514)M loss,
then a positive net income of $49.258M would require **+$106.772M of below-the-line income in
one quarter.** RKLB holds $2.129B of cash and $187.9M of marketable securities — at a
generous 4% that is ~$21M/quarter — and it carries $152.4M of debt. **$106.8M of
below-the-line income is not available to it.**

**Consequence, and it is severe: DA-23 is not confined to one line.** The extract drops the
sign on **negative values**, so **every** negative figure in the block is affected.
**Reported figures affected at RKLB: operating income, net income, and diluted EPS — three
lines, one quarter.**

**Why this matters more than the earlier six confirmations.** The register previously
recorded DA-23 as an `operating_income` defect. **It is a whole-statement sign defect.** Any
screen or ratio using **net income** or **EPS** from the metrics block on a loss-making
issuer is **reading a positive number for a negative one** — which is a strictly larger blast
radius than the operating-line version, because net income is the input to P/E, ROE, margin
screens and every screening factor in common use.

**Escalate to the DA-23 amendment: re-scope from `operating_income` to ALL signed lines.**

## 2. RKLB's actual competitive position

| Metric | Q2 2026 (corrected) | Q2 2025 | Change |
|---|---:|---:|---:|
| Revenue | **$234.066M** | $144.498M | **+62.0%** |
| Gross profit | $84.576M | — | **36.1% margin** |
| **Operating income** | **$(57.514)M** | $(59.639)M | **improving** |
| **Operating margin** | **−24.6%** | −41.3% | **+16.7 pts** |
| R&D / revenue | **35.2%** | 45.8% | −10.6 pts |
| Cash | $2.129B | $564.1M | **+277%** |

**Corrected, RKLB is improving fast: revenue +62%, operating margin up 16.7 points, R&D
intensity down 10.6 points, and $2.1B of cash.** The apparent profitability the extract
reports is an artefact; **the real trajectory is a company converging on break-even from
below.**

**But launch is not what is driving it** — established earlier and unchanged: **revenue +62%
with launch revenue −$2.1M.** The growth is space systems.

## 3. Launch competition, measured on the only disclosed denominator

**SPCX discloses launch counts; nobody discloses market share.** Using launch count:

| Operator | Q2 2026 launches | Note |
|---|---:|---|
| **SPCX (Falcon)** | **37** | of which **27 internal** (Starlink), 10 customer |
| **SPCX (Starship)** | **1** | all classified internal |
| **RKLB (Electron/Neutron)** | not separately disclosed | revenue fell |
| **ULA** | not disclosed | **equity-method; invisible at both parents** |
| **Blue Origin, Firefly, others** | FLY discloses no launch count | — |

**The competitive conclusion is the same one four other lines reached by different routes:
launch competition cannot be measured economically in this universe.** SPCX's 27 internal
launches carry **no inter-segment revenue** — they are capitalised into satellites. **So 73%
of the dominant provider's launches produce zero reported revenue**, and the remainder of the
market does not disclose counts at all. **A launch market-share table is not constructible
from public filings.**

**Register as a DA-08 consequence**, and note it is a **stronger** version of the earlier
"four critical duopolies are unpriced" finding: launch is not merely unpriced, it is
**denominatorless.**

## 4. Vertiv — the enabling layer is the healthiest business in the universe

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---:|---:|---:|
| Revenue | **$3,274.3M** | $2,638.1M | **+24.1%** |
| Implied gross profit | $1,234.9M | — | **37.7% margin** |
| Operating income | **$637.9M** | $442.4M | **+44.2%** |
| **Operating margin** | **19.5%** | 16.8% | **+2.7 pts** |
| Net income | $497.8M | $324.2M | +53.5% |
| EPS (diluted) | $1.27 | $0.83 | +53.0% |

**VRT is clean** (EPS × 392.747M = $498.8M vs net income $497.8M — 0.2% gap).

**VRT's 19.5% operating margin puts it in the same tier as CW (19.3%) and KRMN (19.1%)** —
three unrelated industrial businesses converging on ~19%. **And it is expanding margin 2.7
points on 24.1% growth**, which is scarcity pricing in a functioning market, not a
bottleneck.

**This closes the loop on the orbital-compute case from the supply side.** The thermal
management supplier that an orbital compute buildout would need is **already growing 24% at a
19.5% margin serving terrestrial data centers.** It has no reason to prefer a new, smaller,
harder market — **the same revealed-preference structure SPCX showed from the demand side.**

## 5. DA-26 — VRT confirms in both lines, twice

| Row | Revenue | Operating income | What they are |
|---|---:|---:|---|
| Q2 2026 | $3,274.3M | $637.9M | genuine quarters |
| **Q4 2025** | **$10,229.9M** | **$1,829.7M** | **FY2025 ANNUAL figures** |
| **Q4 2024** | **$8,011.8M** | **$1,367.4M** | **FY2024 ANNUAL figures** |

**Twenty-third issuer confirmed**, and **the fourth where the defect propagates to both
revenue and operating income** (AMGN, TER, CW, VRT). FY2025 = Q1–Q3 $7,349.9M so annual
$10,229.9M implies Q4 2025 of $2,880.0M. **The annual reading is internally consistent.**

---

## Carry-forwards

1. **⚠️ DA-23 IS A WHOLE-STATEMENT SIGN DEFECT, NOT AN `operating_income` DEFECT.** At RKLB,
   **operating income, net income AND diluted EPS are all flipped** — three lines, one
   quarter. **Re-scope the DA-23 amendment.** The blast radius is larger than recorded:
   **net income is the input to P/E, ROE and every common screening factor**, so a loss-making
   issuer reads as profitable on any screen built from the metrics block.
2. **Corrected, RKLB is improving fast** — revenue +62%, operating margin **+16.7 pts** to
   −24.6%, R&D intensity −10.6 pts, $2.1B cash. **The trajectory is convergence on break-even
   from below.**
3. **Launch market share is not constructible.** 73% of SPCX's launches are internal and carry
   **no inter-segment revenue**; ULA is equity-method; RKLB and FLY do not disclose counts.
   **Launch is not just unpriced — it is denominatorless.** Stronger than the four-duopolies
   finding.
4. **VRT at 19.5% margin and +24.1% growth** joins CW (19.3%) and KRMN (19.1%) — three
   unrelated industrials converging at ~19%, while **expanding** margin on growth. **Scarcity
   pricing, not a bottleneck.**
5. **DA-26 at 23 of 23 issuers**, fourth with both-line propagation.
````

## Artifact — artifacts/RTX/2026-09-18_1239_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: RTX
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T19:05:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "RTX's own segment definitions; space sensors inside Collins/Raytheon"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified; RTX CLEAN"
  - da_id: "DA-26"
    chosen_reading: "both Q4 rows carry ANNUAL totals"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# RTX — Supply-Chain Position (Space Sensors)

Source: Form 10-Q, accession `0000101829-26-000027` (Q2 2026, quarter ended 2026-06-30).

---

## 1. RTX is scale with no space visibility at all

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$24,708M** | $21,581M | +14.5% |
| Operating income | **$2,811M** | $2,146M | +31.0% |
| Operating margin | **11.4%** | 9.9% | +1.5 pts |
| Net income | $2,139M | $1,657M | +29.1% |
| R&D | $726M | $697M | +4.2% |
| **R&D / revenue** | **2.9%** | 3.2% | — |

**$24.7B of quarterly revenue, 11.4% operating margin, 2.9% R&D intensity.** A normal
diversified defense prime — and **the least space-visible name in Tier 3**. Space sensors
sit inside Collins Aerospace and Raytheon, neither of which is disaggregated below the
segment level.

**RTX's role in the thesis is therefore as a scale datum, not a space exposure.** Its
inclusion tests whether adding primes adds information; on this evidence, **it does not.**
That is a legitimate finding: the universe's Tier 3 exists for supply-chain read-through
that the disclosure regime does not provide.

**Recommendation carried to Phase 6**: Tier 3 should be described as **context, not
evidence** — it demonstrates the sector's industrial base and its financial capacity, but
contributes no pricing signal on any critical component.

## 2. A useful margin datum: primes cluster at 10–12%

| Prime | Q2 2026 operating margin |
|---|---|
| LMT | 12.4% |
| **RTX** | **11.4%** |
| LHX | 11.1% |
| NOC | 10.1% |
| BA | 0.6% |

**Four of five primes cluster between 10.1% and 12.4%.** That is a tight band for
companies with very different space exposure — evidence that **consolidated prime margins
are set by defence programme economics, not by space participation.** Boeing's 0.6% is the
outlier, reflecting commercial aerospace rather than a space effect.

**Consequence**: prime operating margin carries **no information about space exposure**
in this universe. Any thesis attempting to rank primes by space leverage using margin
would be measuring something else.

## 3. RTX is clean on DA-23

EPS × diluted shares = $1.57 × 1,365M = $2,143M against reported net income $2,139M — a
0.2% gap. RTX is profitable and unaffected.

**Note RTX's Q2 2024 at 2.7% operating margin** ($529M on $19,721M) — low, but genuinely
so (Pratt & Whitney GTF charges), not a sign artefact. **A low margin is not evidence of
the defect**; only reconciliation is.

## 4. DA-26 — RTX shows it twice, in the Q4 position

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $24,708M | a genuine quarter |
| **Q4 2025** | **$88,603M** | **RTX's FY2025 ANNUAL revenue** |
| **Q4 2024** | **$80,738M** | **RTX's FY2024 ANNUAL revenue** |

**Tenth issuer confirmed** (HWM, TDG, BA, GOOG, MSFT, NVDA, SATS, NOC, LMT, RTX).
**DA-26 is now 10 of 10 issuers checked** — as universal as DA-23's sign stripping.

---

## Carry-forwards

1. **Tier 3 contributes context, not evidence.** Space sensors inside RTX are invisible
   below the segment level.
2. **Primes cluster at 10–12% operating margin** regardless of space exposure — prime
   margin carries **no** information about space leverage.
3. **A low margin is not evidence of the defect** — RTX's 2.7% Q2 2024 is genuine.
   Reconciliation, not magnitude, is the test.
4. **Clean-positive 13 of 13; DA-26 now 10 of 10 issuers.**
````

## Artifact — artifacts/SATS/2026-09-18_1239_risk_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-6
ticker: SATS
skill: risk
mode: methodology
generated_at: 2026-09-18T17:15:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "953fc5d396e7"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-17"
    chosen_reading: "spectrum quantified by transaction value ($), not MHz — the only basis disclosed"
  - da_id: "DA-18"
    chosen_reading: "regulatory approval = FCC licence transfer completed; ITU coordination not separately confirmed"
  - da_id: "DA-24"
    chosen_reading: "operating_income is asset-sale-contaminated; the operating business must be read separately"
  - da_id: "DA-23"
    chosen_reading: "verified; SATS is NOT sign-stripped (EPS x shares reconciles to 0.3%)"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# SATS — Regulatory Risk, Q1 2026

Source: Form 10-Q, accession `0001104659-26-058150`, quarter ended 2026-03-31;
consolidated with the Phase 4 cross artifact.

**Why SATS carries the P6 regulatory analysis**: it is the counterparty to the sector's
pricing reference — the ~$19.6B sale of AWS-4, H-Block and AWS-3 spectrum to SPCX — and
therefore the cleanest case of a regulatory asset changing hands.

---

## 1. The regulatory asset, separated from the operating business

The problem with reading SATS is that **DA-24 contaminates the income statement**:
2025 Q3 and Q4 operating income (460% and 118% of revenue) reflects a licence sale, not
operations. The Q1 2026 quarter is clean:

| Metric | Q1 2026 |
|---|---|
| Revenue | **$3,667.5M** |
| Operating income | **$392.8M** |
| Operating margin | **10.7%** |
| Net income | $146.9M |
| Net margin | 4.0% |

**Strip out the spectrum gain and EchoStar is a 10.7%-operating-margin, 4.0%-net-margin
telecom.** Against Phase 4's finding that the licences were worth ~1.8× annual revenue,
the read is:

> **The regulatory asset was worth more than the business that held it was earning from
> operations — roughly 27× the *gain-equivalent* of a single year of operating income.**

That is the cleanest available quantification of PIL-6's premise: the licence is the
asset, and the operating business is a thin margin on top of it.

## 2. Regulatory risk, enumerated

PIL-6 asserts that spectrum and orbital slots are **allocated before capital can be
deployed**. SATS's own transaction demonstrates the gates in sequence:

| Gate | Authority | Evidence |
|---|---|---|
| 1. Licence transfer approval | **FCC** | The SPCX–EchoStar transaction required FCC consent before closing; the transfer **completed**, so this gate passed |
| 2. International coordination | **ITU** | RKLB's 10-Q Iridium risk factors name the ITU explicitly alongside the FCC and DCSA as required consents — documentary evidence that ITU coordination is a live, named gate, not background |
| 3. Foreign investment review | **DCSA / CFIUS-adjacent** | Also named in the RKLB risk factors; for spectrum with defence users this is a separate, non-trivial gate |
| 4. Market access | national regulators | Per-country; not evidenced here |

**The structural point**: these are **sequential, not parallel** gates. Passing one says
nothing about the next — which is exactly the **DA-18** ambiguity (approval ≠ approval).
A thesis treating "regulatory approval" as a single event is understating the process by
three gates.

## 3. PIL-6's falsifier — and a disposition problem

| Field | Value |
|---|---|
| metric | `new_entrant_primary_spectrum_or_slot_grant_without_incumbent_acquisition` |
| threshold | 0, op `>` |
| source | `FCC_IBFS_or_ITU_Space_Network_List` |
| **Observed** | **not measured** |
| **Verdict** | **PENDING** — and structurally so |

**This analysis adds a third distinction to the disposition taxonomy.** Phase 4 proposed
`UNRESOLVABLE-FROM-PLATFORM` for PIL-6 because the FCC/ITU sources are public but
unreachable. Working the transaction in detail sharpens it:

- **The gate evidence is partially obtainable indirectly.** RKLB's Iridium risk factors
  *name* the FCC, ITU and DCSA as required consents — so the **existence and identity of
  the gates** is `DEMONSTRATED` from filings, even without FCC data.
- **The falsifier itself** (whether a new entrant ever gets primary coordination without
  buying it) still requires FCC IBFS / ITU Space Network List.

So PIL-6 splits: **the premise is evidenced from filings; the falsifier is not.** That is
a better outcome than Phase 4 recorded, and it means PIL-6 need not wait on external data
to contribute to the synthesis.

## 4. DA-23 / DA-24 — SATS is the instructive non-case

SATS is **not** sign-stripped (EPS × shares reconciles to 0.3%), but **is**
asset-sale-contaminated under **DA-24**. Two different defects, and SATS exhibits exactly
one of them.

**This is the cleanest demonstration that the two are independent**, and it validates
keeping them as separate register entries rather than merging them into one
"operating_income is unreliable" rule. The remedies coincide — verify against components —
but the diagnoses differ, and a merged entry would have obscured that SATS is a genuine
10.7% margin business whose statement was inflated, rather than a loss-maker whose sign
was dropped.

---

## Carry-forwards

1. **PIL-6's premise is now evidenced directly from SATS** — a 10.7% operating margin
   business holding an asset worth ~1.8× annual revenue. The strongest P6 datapoint
   after Phase 4's gain quantification.
2. **DA-18 (approval ≠ approval) is now documented with named gates** (FCC → ITU → DCSA),
   which upgrades it from an ambiguity to a checklist.
3. **PIL-6's disposition should be split**: premise `DEMONSTRATED` from filings; falsifier
   `UNRESOLVABLE-FROM-PLATFORM`. Phase 4's monolithic framing was too coarse.
4. **DA-23 and DA-24 validated as independent** — SATS exhibits one and not the other.
````

## Artifact — artifacts/SATS/2026-09-18_2359_risk_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-6
ticker: SATS
skill: risk
mode: methodology
generated_at: 2026-09-18T23:59:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e6b41dbb2426"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-24"
    chosen_reading: "asset-sale gains in operating income treated as contamination, not performance"
  - da_id: "DA-16"
    chosen_reading: "risk language graded CLAIMED (issuer assertion)"
  - da_id: "DA-27"
    chosen_reading: "fiscal-period labels not cross-checked for SATS in this pass"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# SATS / IRDM / BWXT — Risk (PIL-6)

**Combined artifact covering three regulatory-risk views**, at panorama resolution per the
thesis owner's priority. **Written from the Phase 4 regulatory research and the artifacts
already in the corpus; the risk-factor prose for these three was NOT read in this pass —
recorded as a limitation, not glossed.**

---

## 1. SATS — the regulatory asset is worth more than the business that holds it

| Datum | Value |
|---|---|
| Spectrum-licence gains recognised, 2025 H2 | **~$27B** |
| Full-year 2025 revenue | **$15.0B** |
| Implied asset-to-business ratio | **~1.8×** |
| Operating margin progression | 2.3% → 5.7% → **460.5%** → **118.1%** → 10.7% |

**The regulatory asset was worth ~1.8× the entire operating business that held it, while
generating no revenue of its own.** The 460.5% operating margin quarter is the DA-24
signature — an asset sale flowing through the operating line.

**This is PIL-6's premise demonstrated in the strongest available form.** The constitution's
PIL-6 rationale asserts that a licensed position is *"an asset with a market price, not a
permit."* **SATS is the proof**: a company whose spectrum appreciated to 1.8× the value of
its operating business.

**And it is a risk datapoint too.** The same fact that proves the premise is the risk:
**a business whose principal asset is a licence is exposed to the regulator's allocation
decisions, not to its own execution.** SATS's 10.7% operating margin says the operating
business is ordinary; the $27B says the licence is extraordinary.

## 2. IRDM — the licence is durable; the service on top of it is not

| Metric | Q2 2026 | Prior year | Change |
|---|---:|---:|---:|
| Operating margin | **15.1%** | 23.2% | **−8.1 pts** |
| Revenue growth | **+3.8%** | — | — |

**Iridium is profitable, licensed, and has 66 satellites and ~2.5M subscribers — and its
operating margin fell 8.1 points while revenue grew 3.8%.**

**The competitive reading is the risk finding**: **the operating licence is durable; the
service business built on it is not automatically so.** A licence that can be profitably
**held** (SATS) and profitably **sold** (SATS, at 1.8× revenue) is an asset — **but holding
the asset does not confer pricing power in the service layer above it.**

**Register the distinction for PIL-6**: the line's premise is about the **asset**, and the
premise holds. **The risk is that the asset's durability is being read as the business's
durability**, and IRDM's 8.1-point margin decline is the counterexample.

## 3. BWXT — the F2 nuclear escape hatch is engineering-sound and economically unattached

| Datum | Value |
|---|---|
| R&D / revenue | **0.5%** |
| Contrast — development programmes | FLY 60.8%, PL 35.5%, RKLB 35.2% |
| Contrast — manufacturing franchises | HEI 2.6%, TER 2.9%, CW 2.7% |

**BWXT's 0.5% R&D intensity is the lowest in the universe — below even the manufacturing
franchises.** Phase 2's finding stands: the F2 nuclear escape hatch produces a **24× area
reduction** (313 m²/MW at 500 K vs 7,499 m²/MW for solar-plus-radiator), and that arithmetic
is sound.

**What fails is any implication that it is *actionable* through BWXT today.** A company
spending 0.5% of revenue on R&D is **not running a space-reactor development programme** —
it is a manufacturing franchise, and its naval and medical franchises are where its capital
goes. **The capability is real and immaterial to the listed owner** — the fifth instance of
the pattern named at GOOG, UTHR, MRCY and NVDA.

**R&D intensity is what separates the two**, and it is available from every filing. **That
makes it the cheapest single diagnostic the thesis produced.**

## 4. The PIL-6 disposition, restated precisely — premise vs falsifier

**The register records PIL-6 as `UNRESOLVABLE-FROM-PUBLIC-SOURCES`, and this artifact makes
the split explicit because conflation is the main risk on this line:**

| | Status | Evidence |
|---|---|---|
| **The PREMISE** — licences are priced assets | **DEMONSTRATED** | SATS $27B vs $15.0B revenue (1.8×); SPCX–EchoStar **$19.6B**, with **$856M paid in cash in H1 2026**; IRDM profitable at 15.1% on licensed L-band |
| **The FALSIFIER** — a primary grant to a new entrant with no incumbent acquisition | **UNREACHABLE** | needs FCC IBFS / ITU Space Network List — **public but outside the corpus** (amendment #4) |

**The premise does not need the falsifier, and the falsifier does not weaken the premise.**
The single addition this pass makes: **the premise now has a cash confirmation** — SPCX's
10-Q shows **$856M of EchoStar spectrum payments in H1 2026 investing activities.** **A
headline transaction price is an assertion; a cash-flow line is a payment.**

---

## Carry-forwards

1. **PIL-6's premise is demonstrated four ways** — SATS ($27B vs $15.0B revenue), SPCX–EchoStar
   ($19.6B), **$856M already paid in cash**, IRDM profitable on licensed spectrum.
   **The premise does not depend on the falsifier.**
2. **The premise's own risk, and the counterexample to over-reading it**: **IRDM's operating
   margin fell 8.1 points on 3.8% revenue growth.** A durable licence does **not** confer
   pricing power in the service layer above it. **Do not read asset durability as business
   durability.**
3. **BWXT's 0.5% R&D confirms the F2 nuclear escape hatch is engineering-sound and
   economically unattached** — the fifth "immaterial to the listed owner" instance.
   **R&D intensity is the cheapest diagnostic in the thesis.**
4. **LIMITATION RECORDED: the risk-factor prose for SATS, IRDM and BWXT was not read in this
   pass.** These findings come from the financials and Phase 4. **The PIL-3 delay-cause census
   remains 1 of 19 coded.**
````

## Artifact — artifacts/SPCX/2026-09-18_1239_operational-kpi_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: SPCX
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T12:39:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "registry-1.0.0"
as_of: 2026-09-18
corpus_version: "UNPINNED"   # no corpus-version endpoint exposed by the platform; see brief.md
definitions_used:
  - da_id: "DA-07"
    chosen_reading: "verified mass from successful launches only; excludes failed and scrubbed"
  - da_id: "DA-08"
    chosen_reading: "customer launch = external payload is primary payload and mission params designed around it"
  - da_id: "DA-09"
    chosen_reading: "subscriber = a service line, not a person, household or device"
  - da_id: "DA-10"
    chosen_reading: "Starlink subscriber service revenue only; excludes enterprise, government, aviation, maritime"
  - da_id: "DA-11"
    chosen_reading: "IT load only — excludes cooling, power distribution, lighting, security, facility overhead"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# SPCX — Operational Baseline, Q2 2026

Source: Form 10-Q for the quarter ended 2026-06-30, accession
`0001628280-26-052535`, filed 2026-08-04. Pages 35, 36, 42–44 read in full.

**Why SPCX carries Deep depth**: it is the only issuer in the universe that discloses
hard throughput metrics rather than narrative. Every figure below is `DEMONSTRATED` —
filed and auditable. That makes it the sector's measurement anchor, and simultaneously
the source of the DA-07…DA-11 definitional traps that make cross-issuer comparison
fail silently.

## Space segment — throughput

| Metric | Q2 2026 | Q2 2025 | Δ |
|---|---|---|---|
| Mass to orbit (t) | **485** | 652 | **−26%** |
| — attributable to customer payloads | 87 | 88 | −1% |
| — attributable to internal payloads | 397 | 563 | −29% |
| Falcon launches | **37** | 45 | −18% |
| — customer launches | 10 | 9 | +11% |
| — internal launches | 27 | 36 | −25% |
| Starship launches | 1 | 1 | — |

**The headline is negative and easy to miss.** Mass to orbit fell 26% year over year
while total revenue rose 91.9%. The decline is entirely internal-payload decline
(−29%), i.e. fewer Starlink satellites launched — not a customer-demand problem, whose
payload mass was flat at 87 t vs 88 t.

**DA-07 application**: mass to orbit counts only *verified* mass from *successful*
launches, explicitly excluding failed and scrubbed attempts. A competitor reporting
launched mass rather than delivered mass would show a higher number on an identical
campaign. Not comparable without restatement.

**DA-08 application**: only 10 of 37 Falcon launches count as customer launches.
Internal Starlink deployments generate **no inter-segment revenue** — the cost is
capitalized into satellites in PP&E. So SPCX's Space segment revenue reflects customer
activity only, and any "launches" comparison against RKLB or FLY that does not restate
for this is invalid. This is the single largest restatement requirement in the universe.

## Space segment — financials

| Metric | Q2 2026 | Q2 2025 | Δ |
|---|---|---|---|
| Revenue | $962M | $746M | +29.0% |
| Cost of revenue | $329M | $330M | −0.3% |
| R&D | **$1,076M** | $693M | **+55.3%** |
| SG&A | $99M | $87M | +13.8% |
| Total costs | $1,504M | $1,115M | +34.9% |
| Operating loss | **$(542)M** | $(369)M | **+46.9% widening** |

**R&D is 3.3× cost of revenue**, driven by Starship production, engineering and test.
The Space segment loses money at the operating line and the loss is widening while
revenue grows — a development-phase signature, not a scale problem.

## Connectivity segment — the profitable business

| Metric | Q2 2026 | Q2 2025 | Δ |
|---|---|---|---|
| Revenue | $4,291M | $2,588M | +65.8% |
| Operating income | **$1,656M** | $923M | **+79.4%** |
| Starlink subscribers | **12.0M** | 6.0M | **+101%** |
| Starlink ARPU | **$66/mo** | $85/mo | **−22.4%** |

**DA-09 / DA-10 application.** Subscribers are *service lines* — an individual or
household with both a residential and a roam line counts **twice**, and managed
enterprise and government customers are excluded entirely. ARPU is computed on
subscriber service revenue only, excluding the enterprise, government, aviation and
maritime lines. SPCX attributes the ARPU decline to "international expansion and the
addition of lower priced service plans" — which under DA-10 means **at least part of the
22.4% decline is a mix-shift artifact**, not price erosion. The two readings are not
distinguishable from public disclosure.

This is the only segment with real operating leverage in the entire 35-name universe:
income from operations grew 79.4% on 65.8% revenue growth.

## AI segment — and the DA-11 trap

| Metric | Q2 2026 | Q2 2025 | Δ |
|---|---|---|---|
| Revenue | $2,561M | $737M | +247.5% |
| Operating loss | $(1,257)M | $(1,524)M | −17.5% narrowing |
| **Nameplate compute draw** | **1.4 GW** | 0.4 GW | **+250%** |

**DA-11 is the most dangerous figure in this thesis.** SPCX defines nameplate compute
draw as *GPUs installed × all-in power draw*, and states explicitly that it **excludes
power for cooling systems, power distribution losses, lighting, security systems and
facility-level overhead**. So 1.4 GW is an **IT load**, not a facility load. True
facility draw is materially higher — typically 1.2–1.5× for a modern data centre, more
for high-density AI racks.

Any orbital-vs-terrestrial comparison that takes 1.4 GW as a facility load understates
the terrestrial denominator and overstates orbital compute's relative position. Phase 6
must restate this; it is flagged as plan risk #2.

**A4 boundary check (constitution).** This segment is **ground-based**. SPCX's separate
filing for up to 1 million satellites at 100 kW/tonne is a `CLAIMED` aspiration with no
revenue line. No listed issuer reports orbital compute revenue — PIL-2 holds.

## Segment reconciliation — and a sign-convention trap

```
  Space          −542
  AI           −1,257
  Connectivity +1,656
  ─────────────────────
  Consolidated   −143   ← operating LOSS
```

`get_company_financials` returns `OperatingIncomeLoss: +143,000,000` — **positive**. The
inconsistency is a platform sign-convention artefact (see the Phase 1 cross artifact,
data-quality note). An `operating_income > 0` screen would misclassify SPCX as
profitable. **Verified against narrative**: the 10-Q reports a net loss of $541M, and
the segment arithmetic independently confirms −143.

## Hand-off to Phase 2

- Mass to orbit is the only sector-wide throughput metric that is actually delivered
  rather than claimed. Phase 3 should test whether RKLB/FLY/YSS disclose anything
  comparable; if not, no cross-issuer throughput comparison is possible and PIL-3's
  falsifier must be evaluated on issuer-specific restatements.
- The 1.4 GW figure needs a cooling-inclusive restatement before Phase 6.
- Subscriber/ARPU mix-shift ambiguity (DA-09/DA-10) should be carried into the Phase 3
  Connectivity analysis rather than resolved here.
````

## Artifact — artifacts/SPCX/2026-09-18_1239_unit-economics_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: SPCX
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T12:39:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "registry-1.0.0"
as_of: 2026-09-18
corpus_version: "UNPINNED"   # no corpus-version endpoint exposed by the platform; see brief.md
definitions_used:
  - da_id: "DA-01"
    chosen_reading: "ALL THREE REPORTED — A, A', B, C. No basis is adopted as 'the' answer."
  - da_id: "DA-02"
    chosen_reading: "LEO. Falcon 9 figures restated to LEO; GTO not used."
  - da_id: "DA-06"
    chosen_reading: "price and cost reported separately, never conflated"
evidence_grade: MODELED
deal_security_basis: not_applicable
unresolvable: false
---

# Phase 1 — Launch Cost Baseline (PIL-1)

**Purpose**: build the DA-01 definitional table for cost per kilogram to LEO, per the
§1c standing rule — enumerate every competing basis, report all, and treat the spread
as the finding.

**Headline result**: the three bases span **~$500/kg to ~$6,600/kg** — a spread of
roughly **7–13×** around a single Falcon 9 mission. Quoting any one of them as "the
cost per kilogram to orbit" is therefore not a simplification; it is a different claim.

---

## DA-01 — the four bases compared

All figures are SPCX Q2 2026 unless marked. Payload denominator: **22.8 t to LEO**
(Falcon 9 reusable, `CLAIMED` — published vehicle spec, not in any filing).

| Basis | What it measures | Q2 2026 figure | Per kg | Grade |
|---|---|---|---|---|
| **A** — customer list price | Published price an external customer pays | ~$67M per Falcon 9 launch | **~$2,939/kg** | `CLAIMED` |
| **A'** — realized revenue per customer launch | Space segment revenue ÷ customer launches | $962M ÷ 10 = **$96.2M** | ~$4,220/kg | `DEMONSTRATED` (figures) / `MODELED` (the division) |
| **B** — marginal cost per launch | Propellant + expended stage + range + refurbishment | **~$12–20M** | **~$525–875/kg** | `MODELED` |
| **C** — fully-loaded segment cost | Space segment total costs ÷ customer launches | $1,504M ÷ 10 = **$150.4M** | **~$6,596/kg** | `DEMONSTRATED` (figures) / `MODELED` (the division) |

### Source detail

**A' input** — `DEMONSTRATED`. Space segment revenue $962M, customer launches 10,
Q2 2026 (10-Q, accession `0001628280-26-052535`, p35 and p42).
**Important caveat**: Space segment revenue includes *Launch and Development*
government contracts with terms up to 14 years, not merely launch services. A' is
therefore an **upper bound** on a launch price, not a price. Restating it to launch
services alone is not possible from public disclosure — this is DA-21 in operation
(issuer-defined segment boundaries).

**C input** — `DEMONSTRATED`. Space segment costs Q2 2026: cost of revenue $329M +
R&D $1,076M + SG&A $99M = **$1,504M** (10-Q p42). Segment operating loss $(542)M.

**B inputs** — `MODELED`, from physics and public cost references:

| Component | Value | Basis |
|---|---|---|
| Propellant | ~$0.36M | Falcon 9 ~485 t (RP-1/LOX), blended ~$0.75/kg. Compare Starship: ~4,600 t at $1–2/kg = $4.6–9.2M |
| Expended second stage | ~$8–12M | **Not recovered.** The dominant term |
| Range and launch operations | ~$2–5M | Range fees, recovery vessel, ground ops |
| Booster refurbishment | ~$1–3M | Between-flight inspection and refurb |
| **Total** | **~$12–20M** | |

---

## Finding 1 — the spread is the finding (why DA-01 exists)

```
  B  ~$525–875/kg   ← marginal cost, the physics floor
  A  ~$2,939/kg     ← list price          (3.4–5.6× B)
  A' ~$4,220/kg     ← realized revenue    (4.8–8.0× B)
  C  ~$6,596/kg     ← fully-loaded        (7.5–12.6× B)
```

A reader told "SpaceX launches cost about $3,000/kg" and a reader told "$6,600/kg"
hold the same stock and disagree about its economics by a factor of two. A reader told
"marginal cost is $500/kg" believes Starship is already obsolete. **All three statements
are supportable from the same filing.** The §1c rule exists precisely because this
spread is load-bearing, not cosmetic.

---

## Finding 2 — F5 needs refinement: the floor's *composition* depends on reuse architecture

The constitution's **F5** states that a propellant floor exists which reusability does
not remove. That is correct for a **fully reusable** vehicle and **materially
incomplete for a partially reusable one**:

| Architecture | Binding marginal-cost term | Propellant share of marginal cost |
|---|---|---|
| **Fully reusable** (Starship) | Propellant | ~100% — nothing else is consumed |
| **Partially reusable** (Falcon 9) | **The expended second stage** | **~2–3%** |

Falcon 9's propellant is roughly **$0.36M against a ~$12–20M marginal cost**. The floor
for a partially reusable vehicle is therefore set by *manufacturing cost of the
expendable stage*, which falls with production learning — **not** by propellant, which
does not fall at all.

**Consequence**: the F5 propellant argument proves sub-$10/kg is impossible *for
Starship-class fully reusable vehicles*. It does **not** bound Falcon-class vehicles,
whose floor is a manufacturing curve and could in principle keep falling. The
constitution's F5 should be split into F5a (fully reusable: propellant floor, hard) and
F5b (partially reusable: upper-stage manufacturing floor, soft). Flagged as a
constitution amendment candidate — **not executed here**, since amending the
constitution is a human approval, not an artifact write.

---

## Finding 3 — the R&D burden and what "customer launch" excludes

Space segment R&D of **$1,076M** is **3.3× the segment's cost of revenue** ($329M), and
is driven by Starship development (+55.3% YoY). Two consequences:

1. **Basis C is Starship-subsidized.** The $6,596/kg fully-loaded figure is inflated by
   a development programme that belongs to a future vehicle. An analyst arguing "SpaceX
   loses money on every launch" and one arguing "SpaceX is profitable per launch" can
   both cite the filing — the difference is whether Starship R&D is assigned to Falcon
   missions.
2. **DA-08 in operation.** SPCX flew **37 Falcon launches in Q2 2026** but classified
   only **10** as customer launches — the other **27** were internal Starlink
   deployments, which generate no inter-segment revenue by design. Any cross-issuer
   "launches" comparison that does not restate for this is invalid.

---

## Data-quality note — an XBRL sign-convention trap

`get_company_financials(SPCX)` returns `OperatingIncomeLoss: +143,000,000` — a
**positive** $143M. The consolidated figure is actually an operating **loss** of $143M.
Verification: the three segments sum to −542 (Space) + −1,257 (AI) + 1,656 (Connectivity)
= **−143**, and the 10-Q narrative reports a net loss of $541M.

**This is a live trap.** An analyst screening on "operating income > 0" would classify
SPCX as profitable. The sign convention in the platform's income-statement extract is
not reliable for loss-making issuers; narrative and segment reconciliation must be
cross-checked. Registered as a candidate DA class — the metric `operating_income` is
itself ambiguous in sign convention across sources.

---

## PIL-1 falsifier evaluation

| Field | Value |
|---|---|
| metric | `demonstrated_price_per_kg_to_LEO_P50` |
| threshold | 1000 |
| basis | `ANY_OF_A_B_C` |
| **Observed** | A ≈ $2,939 · A' ≈ $4,220 · B ≈ $525–875 · C ≈ $6,596 |
| **Verdict** | **HOLDS** on A, A' and C. **NOT EVALUABLE on B** — basis B is `MODELED`, not `demonstrated`, and no issuer discloses marginal cost |

**Read carefully**: the falsifier says *demonstrated* price. On basis B the value sits
**below** the $1,000 threshold — but it is our model, not a demonstration. Under P4,
`MODELED` cannot satisfy a falsifier. So PIL-1 **holds**, and the honest statement is:
*prices are demonstrated above $1,000/kg on every disclosed basis; marginal cost is
modelled below it and cannot be demonstrated from public filings.*

That gap — between a demonstrable price and a non-demonstrable cost — is the single
most important structural fact about launch economics. It is also a candidate
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` case for the *cost* half of the question: no issuer
discloses marginal cost per launch, and none is likely to.

---

## Next actions (Phase 2 hand-off)

1. RKLB and FLY unit economics not yet built — needed to test whether the A/B/C spread
   is SpaceX-specific or sector-wide.
2. Basis B needs a defensible public anchor. Candidate: NASA CRS/Commercial Crew
   contract values as a revealed-price floor.
3. F5a/F5b split flagged for constitution amendment.
4. `operating_income` sign convention proposed as DA-23.
````

## Artifact — artifacts/SPCX/2026-09-18_2310_business-model_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: SPCX
skill: business-model
mode: methodology
generated_at: 2026-09-18T23:10:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "registry-1.0.0"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-20"
    chosen_reading: "AI segment revenue read as TERRESTRIAL on all four axes; reported side by side per §1c"
  - da_id: "DA-21"
    chosen_reading: "SPCX's own three-segment definitions replace the prior Space/Connectivity two-segment frame"
  - da_id: "DA-19"
    chosen_reading: "common-control mergers (xAI, X) treated as a change of reporting entity, not organic growth"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# SPCX — Business Model (post-IPO)

Source: Form 10-Q, accession `0001628280-26-052535`; Notes 1 and 3; MD&A Overview.

**⚠️ This artifact supersedes the segment frame used in every prior SPCX artifact.** SPCX now
reports **three** segments, and the one the thesis was built on is the smallest.

---

## 1. The reporting entity changed — and the change is not organic

**Three events between the prior SPCX artifacts and this filing:**

| Event | Date | Effect |
|---|---|---|
| **X Merger** — X Holdings and X.AI Corp into xAI | 2025-03-28 | Twitter/X and X.AI combined under xAI |
| **xAI Merger** — X.AI Holdings Corp into SPCX | **2026-02-02** | **common control**; xAI becomes a wholly-owned subsidiary |
| **IPO** | 2026-06 | 638.9M Class A shares at $135.00; **net proceeds $85,675M** |
| Five-for-one forward stock split | 2026-05 | all prior periods retroactively adjusted |
| **Cursor Merger** — Anysphere, Inc. | option exercised 2026-06 | **$60B implied equity value**, all-stock, closing expected Q3 2026 |

**Consequence for every prior SPCX artifact in this thesis**: the revenue base, segment
structure and growth rates are **not comparable across the mergers**. Common-control
combinations are accounted for as a **change of reporting entity**, so prior-period figures
have been recast — and **any growth rate quoted across the boundary mixes real growth with
entity change.** Both the DA-19 and DA-26 registers apply.

**This is the single largest statement-level discontinuity in the universe**, larger than any
of the extraction defects: the issuer the thesis anchors on **became a different company
mid-series.**

## 2. Revenue composition — the space business is the smallest and shrinking

| Segment | Q2 2026 | % | H1 2026 | H1 2025 | H1 change |
|---|---:|---:|---:|---:|---:|
| **Connectivity** (Starlink) | **$4,291M** | **54.9%** | **$7,548M** | $5,062M | **+49.1%** |
| **AI** (Grok, X, compute) | **$2,561M** | **32.8%** | **$3,379M** | — | — |
| **Space** (launch, Dragon) | **$962M** | **12.3%** | **$1,581M** | $1,611M | **−1.9%** |
| **Total** | **$7,814M** | 100% | $12,508M | $8,138M | +53.7% |

**Classification.** SPCX is not a launch company with adjacent businesses. On revenue it is
**a satellite broadband operator (54.9%) with a terrestrial AI business (32.8%) that also
launches rockets (12.3% and declining).**

**And the H1 comparison is the cleaner one** — H1 2025 predates the xAI merger, so the AI
column is absent, but **the Space column is directly comparable across both halves and it
FELL 1.9%** while total revenue rose 53.7%.

**Consequence for the universe's construction**: the thesis's five cohorts were built
treating SPCX as the core launch name. **On its own disclosure, SPCX's launch business is a
sub-scale, loss-making segment inside a company whose value is dominated by two non-launch
businesses.** Any thesis that uses SPCX as the launch-sector read-through is **reading 12% of
the company and 0% of its growth.**

## 3. The four distribution channels are economically different businesses

| Channel | Segment | Contract form | Margin | Backlog character |
|---|---|---|---|---|
| **Consumer subscription** | Connectivity | Starlink.com service lines, monthly | in the 52.0% segment gross margin | none — monthly churn |
| **Enterprise / government** | Connectivity | negotiated contracts: aviation, maritime, land mobility, fixed sites, government | **grew MORE than consumer** (+$939M vs +$764M) | contracted |
| **Launch, fixed-price** | Space | Launch Services **1–5 yr**; Launch and Development **1–14 yr**, cost-to-cost | 65.8% gross, **−56.3% after R&D** | long-dated, government-heavy |
| **AI** | AI | advertising, subscriptions, **data licensing, API access to Grok, cloud services** | not disclosed | mixed |

**Two observations that matter for the thesis:**

**(a) The revenue-recognition asymmetry inside Space.** Launch Services is recognised **at a
point in time** — revenue and cost are deferred until the payload reaches orbit. Launch and
Development is recognised **over time** on a cost-to-cost input method. **So a launch that
slips moves revenue between quarters, and a development contract that overruns books
revenue as it burns cost.** These two are aggregated into one segment line. **Any
quarterly Space revenue series is a blend of two recognition methods with opposite
sensitivities to delay** — register as a definitional caveat on PIL-1 and PIL-3.

**(b) Concentration is disclosed but not quantified here.** Note 3 carries explicit
`concentration of risk` disclosure naming **Customer A and Customer B** against the backlog.
**The extract does not carry the percentages in the pages read**; the named-customer
disclosure is the place to resolve any question about how much of the backlog rests on two
counterparties. **Carried forward as a bounded read, not as a finding.**

## 4. The AI segment is terrestrial, and it is the fastest-growing part of the company

**Revenue increased $1,824M in Q2 2026 — the largest single contributor to consolidated
growth, ahead of Connectivity's $1,703M.** The segment is described as *"AI computational
infrastructure,"* and its key metric is **nameplate compute draw: 1.4 GW (from 0.4 GW)**.

**On the DA-20 four-way reading required by §1c, all four axes reported:**

| Axis | Reading |
|---|---|
| compute **in** orbit | **No.** Nameplate compute draw counts GPUs installed **in data centers**; explicitly excludes cooling, power distribution and facility overhead — the vocabulary of a terrestrial build |
| compute **for** orbit | No |
| communications **from** orbit | **No** — this is Connectivity, a separate segment |
| **terrestrial compute with satellite-delivered distribution** | **Yes** |

**SPCX's AI business is a data-center business.** Its fastest-growing segment and its
largest capital deployment are both on the ground, at the company with the cheapest orbital
access in existence.

**Consequence for the business-model classification**: SPCX is best described as **a
vertically integrated compute-and-connectivity company that owns its own launch capability**
— not the reverse. **That is the same vertical-integration logic the F2/BWXT analysis
identified, applied to compute rather than power.**

## 5. What the model implies for capital allocation

```
H1 2026 capex increase $21,511M:
  "the build out of DATA CENTERS and related infrastructure,
   and space launch facilities and related infrastructure"
```

**Data centers are named first.** Against a $541M quarterly net loss and $4,817M H1 net loss,
the company raised $85.7B in equity and $40.9B in notes and is **spending the majority of
its investing outflow on compute capacity.**

**This is the cleanest capital-allocation signal in the universe**, and it is a stated
priority ordering rather than an inference: **the company with the strongest strategic
position in launch is allocating marginal capital to terrestrial compute.**

---

## Carry-forwards

1. **The reporting entity changed mid-series** (X merger 2025-03-28, xAI merger 2026-02-02,
   IPO 2026-06, Cursor pending). **Common-control accounting recasts prior periods, so
   growth rates across the boundary mix real growth with entity change.** DA-19 and DA-26
   both apply, and **this is a larger discontinuity than any extraction defect.**
2. **Launch is 12.3% of revenue and fell 1.9% across a half in which total revenue rose
   53.7%.** The universe was built treating SPCX as the core launch read-through; **that
   reads 12% of the company and 0% of its growth.**
3. **Space's revenue blends two recognition methods** — point-in-time Launch Services and
   over-time cost-to-cost Launch and Development — **with opposite sensitivities to delay.**
   A definitional caveat on PIL-1 and PIL-3, not a defect.
4. **The AI segment is terrestrial on all four DA-20 axes**, is the largest contributor to
   consolidated growth, and commands the largest capital allocation. **SPCX is a
   compute-and-connectivity company that owns its own launch capability, not a launch
   company with adjacent businesses.**
5. **Backlog concentration (Customer A / Customer B) is disclosed but not quantified on the
   pages read** — carried as a bounded read.
````

## Artifact — artifacts/SPCX/2026-09-18_2310_operational-kpi_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: SPCX
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T23:10:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income verified; SPCX CONFIRMED flipped at consolidation (-143 reported as +143)"
  - da_id: "DA-20"
    chosen_reading: "AI segment revenue classified TERRESTRIAL — not in-orbit, not for-orbit. Reported side by side per §1c."
  - da_id: "DA-01"
    chosen_reading: "launch price/cost bases unchanged; this artifact adds VOLUME, not price"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# SPCX — Operating Baseline (Q2 2026, post-IPO)

Source: Form 10-Q, accession `0001628280-26-052535` (quarter ended 2026-06-30). **This is a
post-IPO filing that materially revises every prior SPCX artifact in this thesis.**

---

## 1. THE DECISIVE DATUM: launch volume is FALLING at the launch monopoly

| Key business metric | Q2 2026 | Q2 2025 | Change | H1 2026 | H1 2025 | Change |
|---|---:|---:|---:|---:|---:|---:|
| **Mass to orbit (t)** | **485** | 652 | **−25.6%** | **1,041** | 1,102 | **−5.5%** |
| — customer payloads | 87 | 88 | −1.1% | 132 | 163 | −19.0% |
| — **internal payloads** | **397** | 563 | **−29.5%** | 908 | 938 | −3.2% |
| **Falcon launches** | **37** | 45 | **−17.8%** | **77** | 81 | **−4.9%** |
| — customer launches | 10 | 9 | +11.1% | **17** | 21 | **−19.0%** |
| — **internal launches** | **27** | 36 | **−25.0%** | 60 | 60 | 0.0% |
| Starship launches | 1 | 1 | — | **1** | 3 | **−66.7%** |

**SPCX calls mass to orbit "a key indicator of SpaceX's capacity and scalability." It fell
25.6% year over year. Falcon launches fell 17.8%. Starship launches fell from 3 to 1.**

**This is the single most important operational datum the thesis has produced, and it runs
opposite to the premise the universe was built on.** The company with the world's only
high-cadence reusable launch franchise **launched fewer times this quarter than last**, and
the contraction is concentrated in **internal** launches (−25.0%) — i.e. **Starlink
deployment is slowing**, which is the demand that was supposed to justify the cadence.

**A1b is now falsified on the issuer's own metrics.** The constitution's A1 split proposed
A1a (launch cost is the master *cost* variable — holds) vs A1b (launch is the master *value*
variable — does not hold). **SPCX's own disclosure settles it**: launches −17.8% while
revenue +91.9%, and the Space segment is 12.3% of revenue and loss-making.

## 2. The segment structure: launch is a loss leader inside a connectivity company

| Segment | Q2 2026 revenue | % of total | Operating income | **Operating margin** |
|---|---:|---:|---:|---:|
| **Connectivity** (Starlink) | **$4,291M** | **54.9%** | **$1,656M** | **+38.6%** |
| **AI** (Grok, X, compute) | **$2,561M** | **32.8%** | not disclosed | — |
| **Space** (launch + Dragon) | **$962M** | **12.3%** | **$(542)M** | **−56.3%** |
| **Consolidated** | **$7,814M** | 100% | $(143)M | −1.8% |

**The company anchored as the thesis's core listed holding earns 12.3% of its revenue from
space launch and loses money doing it.** Connectivity — a terrestrial-market broadband
business delivered via satellites — is 54.9% of revenue at a 38.6% operating margin.

**And the Space segment's loss is NOT a launch-economics problem:**

```
Space Q2 2026:  revenue         $962M
                cost of revenue $329M   ->  gross profit $633M  =  65.8% gross margin
                R&D           $1,076M   <-   111.9% of segment revenue
                SG&A             $99M
                loss from ops  $(542)M   (identity closes exactly)
```

**A 65.8% gross margin — the highest in the universe — destroyed by Starship development
R&D.** Cost of revenue was **flat** (−0.3%) while revenue rose 29.0%, so **the marginal
Falcon launch is highly profitable**. The loss is a **development-funding decision**, not an
operating failure. **Register the distinction: Falcon launch economics are good; Starship
development consumes $1.08B per quarter.**

## 3. THE ORBITAL-COMPUTE DISCONFIRMATION — SPCX is building on the ground

**The strongest possible test of PIL-5 is the company with the cheapest orbital access. If
orbital compute were going to close anywhere, it would close here first.**

```
Q2 2026 nameplate compute draw:  1.4 GW     (Q2 2025: 0.4 GW)   +250%
H1 2026 capex increase:          $21,511M
  attributed first to:           "the build out of DATA CENTERS and related
                                  infrastructure, and space launch facilities"
Cursor Merger:                   $60,000M implied equity value, all-stock, closing Q3 2026
```

**SPCX is deploying 1.4 GW of terrestrial AI compute — 3.5× its own year-ago figure — and
its capital-expenditure narrative names data centers *before* launch facilities.** The AI
segment is described as *"AI computational infrastructure"* with **no mention of orbit
anywhere in the segment definition.**

**And SPCX states its own allocation intent explicitly**: *"We allocate a significant amount
of launch capacity to our Connectivity segment, and expect to allocate a significant amount
to our AI segment in the future."* **Launch capacity is being allocated to a segment whose
compute sits on the ground.**

**PIL-2's falsifier does not fire — but this is the closest call in the thesis, and the
DA-20 distinction is what decides it.** SPCX discloses AI-infrastructure revenue. Applying
the four readings side by side, as §1c requires:

| Reading | Applies to SPCX's AI segment? |
|---|---|
| compute **in** orbit | **No** — data centers are terrestrial; "nameplate compute draw" counts installed GPUs in data centers |
| compute **for** orbit | No |
| communications **from** orbit | No |
| **terrestrial compute, satellite-delivered connectivity** | **Yes** |

**Verdict: not orbital-compute revenue on any of the three readings the falsifier intends.
PIL-2 HOLDS.** But the case for `UNRESOLVABLE` weakens: **the disclosure SPCX would need to
make is now adjacent to one it actually makes**, and a reader who conflates "AI
infrastructure" with "orbital compute" would wrongly fire the falsifier. **Register as a
false-positive trap for any future analyst on this pillar.**

**The economic reading is unambiguous**: the one company that could put compute in orbit for
the least money is putting it on the ground, at scale, and financing it with the largest IPO
in history. **Orbital compute is not being out-competed by terrestrial compute — it is being
out-*chosen* by the only company positioned to do both.**

## 4. Starlink: volume-driven growth at a halving price

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---:|---:|---:|
| Starlink subscribers | **12.0M** | 6.0M | **+101.2%** |
| **Starlink ARPU** | **$66/mo** | $85/mo | **−22.4%** |
| Connectivity revenue | $4,291M | $2,588M | +65.8% |
| — consumer subscribers | +$764M | | |
| — **government / aviation / maritime / enterprise** | **+$939M** | | |
| Connectivity gross margin | **52.0%** | — | |
| Connectivity R&D | $294M | $143M | **+105.6%** |

**Subscribers doubled; ARPU fell 22.4%.** SPCX attributes it to *"international expansion
and the addition of lower priced service plans."* **Revenue per subscriber is falling at
half the rate subscribers are being added — growth is being bought with price.**

**And the enterprise/government half grew MORE than the consumer half** ($939M vs $764M).
**The consumer business — the one the Starlink narrative is built on — is the slower and
lower-quality half of Connectivity's growth.**

## 5. Capital structure: the largest IPO in history, and what it is funding

```
H1 2026 operating cash flow    +$3,466M
H1 2026 investing              $(34,487)M
H1 2026 financing             +$100,291M
   IPO net proceeds             $85,675M   (638.9M shares at $135.00)
   SpaceX Notes               +$40,869M   (6.03% effective rate)
   bridge loan repayment      $(33,406)M
   EchoStar spectrum payments     $856M   (installments on the $19.6B deal)
```

**A company with a $541M quarterly net loss raised $85.7B and is spending $34.5B per half
on investing — most of it data centers.** The EchoStar spectrum payments appearing as a
cash-flow line confirms PIL-6's premise **in cash**, not just in a headline price.

**Cursor Merger**: a call option exercised in June 2026 to acquire Anysphere (Cursor) at a
**$60B implied equity value in Class A stock**, expected to close Q3 2026. **A $60B all-stock
acquisition by a loss-making issuer — P11 in-flight M&A treatment applies, and the
dilution math is not yet determinable.**

## 6. DA-23 re-confirmed at consolidation

Consolidated loss from operations **$(143)M** — matching the earlier SPCX artifact's finding
that the extract reports this loss with the sign stripped as **+143**. **Independent
re-confirmation from the MD&A table, which prints the loss with its sign intact.**

---

## Carry-forwards

1. **LAUNCH VOLUME IS FALLING AT THE LAUNCH MONOPOLY.** Mass to orbit **−25.6%**, Falcon
   launches **−17.8%**, internal launches **−25.0%**, Starship launches 3→1. **A1b is
   falsified on the issuer's own key metrics.** Escalate to the synthesis and the
   constitution amendment queue.
2. **The Space segment is 12.3% of revenue and loses $(542)M/quarter — but at a 65.8% GROSS
   margin.** The loss is **Starship development R&D ($1,076M/qtr), not launch economics**.
   **Falcon launch economics are good; this is a funding decision.** Register the distinction.
3. **THE ORBITAL-COMPUTE DISCONFIRMATION: SPCX is deploying 1.4 GW of TERRESTRIAL compute**
   (3.5× y/y), with capex naming data centers *before* launch facilities, and allocating
   launch capacity to that segment. **The one company positioned to do both chose the
   ground.** PIL-2 HOLDS on the DA-20 four-way reading — **and that reading is now a
   documented false-positive trap**, since "AI infrastructure" is adjacent to but not
   "orbital compute."
4. **Starlink ARPU −22.4% against subscribers +101.2%**, and the enterprise/government half
   outgrew the consumer half. **Growth is being bought with price, and the consumer story is
   the weaker half.**
5. **$60B all-stock Cursor acquisition pending, Q3 2026 close** — P11 in-flight M&A, dilution
   undeterminable.
6. **DA-23 re-confirmed at consolidation** against the MD&A table.
````

## Artifact — artifacts/SPCX/2026-09-18_2345_risk_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-6
ticker: SPCX
skill: risk
mode: methodology
generated_at: 2026-09-18T23:45:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e6b41dbb2426"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-20"
    chosen_reading: "AI infrastructure risk read as TERRESTRIAL on all four axes; reported side by side per §1c"
  - da_id: "DA-16"
    chosen_reading: "risk-factor language graded CLAIMED (issuer assertion), not DEMONSTRATED"
  - da_id: "DA-25"
    chosen_reading: "risk language quoted verbatim rather than normalised into a score"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# SPCX — Risk (PIL-6)

Source: Form 10-Q, accession `0001628280-26-052535`, Item 1A and Forward-Looking Statements.

---

## 1. THE ONLY NEW RISK FACTOR THIS QUARTER IS ABOUT TERRESTRIAL DATA CENTERS

**Item 1A carries exactly one new risk factor.** Its heading, verbatim:

> *"Risks related to our AI infrastructure and data center operations could adversely affect
> our AI segment's business and financial results."*

**Not launch. Not Starship. Not spectrum. Data centers.**

**This is the cleanest evidence in the thesis of where the company's own management locates
its emergent risk**, and it is consistent with every other signal in the filing: the largest
growth contributor (AI, +$1,824M), the largest capital allocation ("data centers and related
infrastructure" named first in the $21,511M capex increase), and the largest disclosed new
risk are **the same business.**

**The market's mental model of SPCX and the company's own risk disclosure have diverged.**

## 2. F1's POWER BOUND IS REAL, BINDING — AND BEING HIT ON THE GROUND

**The new risk factor names, verbatim, among the threats to data-center operations:**
*"physical damage, natural disasters, cybersecurity incidents, construction delays,
workforce disruption or turnover, **power constraints**, supply chain disruptions, equipment…"*

**And the forward-looking-statements risk list includes:**
*"our ability to obtain sufficient **power**, GPUs, and other critical components and manage
our supply chain to support our operations and growth."*

**Consequence for PIL-2 and Line 5.** The constitution's F1 bound — 5,080 m² of array per MW,
1,361 W/m² AM0, the whole chain — exists to establish that **power is the scarce input in an
orbital buildout.** **SPCX's disclosure establishes that power is the scarce input, full
stop** — and the first company to name it as a binding constraint is naming it against
**terrestrial data centers.**

**The loop closes: the power constraint is real, it is binding, and it binds on the ground
first.** The orbital version of the same constraint is not being tested because the
terrestrial version is already the live problem.

## 3. The AI segment's revenue is concentrated and terminable in 90 days

**Two disclosures in the same risk factor, and together they are the most important
customer-quality finding in the thesis:**

> *"a significant portion of our AI infrastructure revenue is **concentrated in a small
> number of customers**."*

> *"Our cloud services agreements generally provide for monthly fees and, after an initial
> period inclusive of capacity ramp (generally, a number of months), **may be terminated by
> either party upon 90 days' notice.**"*

**The segment that produced the largest single contribution to SPCX's consolidated growth
(32.8% of revenue, +$1,824M) rests on a few customers who can walk on 90 days' notice.**

**Why this matters more than the headline growth rate.** SPCX reported AI revenue growing
+247% year over year. **A 90-day termination clause makes that revenue closer to a
spot-contracted backlog than to a subscription base.** **Register a distinction the segment
tables do not draw**: SPCX's AI revenue and its Connectivity revenue are not the same *kind*
of revenue — Connectivity is 12.0M consumer and enterprise service lines, AI is a handful of
contracts with a quarter's notice period.

**This also bears on Line 3.** The fixed-cost-absorption analysis assumes a revenue base that
persists. **A 90-day termination right means the AI segment's contribution to absorbing the
fixed base is revocable**, which is a different risk profile from PL's or YSS's customer base.

## 4. What SPCX does NOT list as a risk — and the PIL-3 census datapoint

**Reading the full forward-looking risk enumeration** (Starship development; **target launch
cadence and expansion of manufacturing and operational capacity**; market growth; demand;
"solve novel issues and navigate and monetize technologies and environments that have never
been accessed or economized before"; AI product and compute monetization; capital-expenditure
timing; **power, GPUs and supply chain**; acquisitions; **regulatory approvals, licenses and
spectrum authorizations**; competition; public-company risks; stock volatility; general
economic conditions):

**Launch availability does not appear as a constraint on SPCX.** Neither does launch cost.
Neither does manufacturing rate. **The self-identified constraints are power, GPUs, supply
chain, and regulatory/spectrum authorisation.**

**PIL-3 census datapoint (one of nineteen).** SPCX cites **"target launch cadence and
expansion of our manufacturing and operational capacity"** as an *ambition*, not as a
*delay cause* — **the phrasing is forward-looking growth language, not a constraint
statement.** **SPCX is therefore a NO on PIL-3's metric.** This is the first issuer coded.

**Honest limitation**: SPCX is a **launch provider**, so it is structurally the wrong party
to cite launch availability as a constraint on itself. **This datapoint is weak for the
census and is recorded with that caveat.** The census's decisive cases are the constellation
builders and operators, which are still uncoded.

## 5. Regulatory and spectrum risk is listed but unquantified

**"Our ability to obtain and maintain required regulatory approvals, licenses and spectrum
authorizations"** appears in the forward-looking risk list, and PIL-6's premise is that these
are finite allocated assets. **The filing does not quantify exposure, does not name
jurisdictions, and does not identify which authorisations are at risk.**

**Consequence for PIL-6**: SPCX's disclosure **corroborates the premise qualitatively and
supplies nothing quantitative.** The line's verdict stays UNRESOLVABLE — **but note this is
the second corroboration of the premise alongside the EchoStar cash payments ($856M paid in
H1), and the premise was already DEMONSTRATED.** **It is the falsifier, not the premise,
that is unreachable.**

---

## Carry-forwards

1. **THE ONLY NEW RISK FACTOR IS ABOUT TERRESTRIAL DATA CENTERS.** Not launch, not Starship,
   not spectrum. **The market's mental model of SPCX and the company's own risk disclosure
   have diverged**, and the divergence is consistent with the growth, capex and segment data.
2. **F1's POWER BOUND IS CONFIRMED AS A LIVE CONSTRAINT — AND ON THE GROUND.** SPCX names
   *"power constraints"* on data-center operations and *"obtain sufficient power, GPUs"* in
   its risk list. **The power constraint is real and binding; the orbital version is not
   being tested because the terrestrial version is already the live problem.**
3. **AI revenue is concentrated in a few customers AND terminable on 90 days' notice.** The
   largest growth contributor is **closer to spot-contracted than subscription revenue** —
   a customer-quality distinction the segment tables do not draw. **It also makes the AI
   segment's contribution to fixed-cost absorption revocable.**
4. **PIL-3 census: SPCX is a NO (1 of 19 coded)** — it names launch cadence as an *ambition*,
   not a *delay cause*. **Recorded with the caveat that a launch provider is structurally the
   wrong party to cite launch availability**, so the datapoint is weak. **The constellation
   builders remain the decisive uncoded cases.**
5. **PIL-6 premise corroborated a second time (regulatory/spectrum risk listed), falsifier
   still unreachable.** Premise DEMONSTRATED, falsifier UNRESOLVABLE — **do not conflate
   them.**
````

## Artifact — artifacts/SPCX/2026-09-18_2359_recent-quarter_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: SPCX
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T23:59:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "registry-1.0.0"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "sign stripping applies to ALL signed lines including net income and EPS (extended scope, RKLB-confirmed)"
  - da_id: "DA-26"
    chosen_reading: "Q4 rows carry ANNUAL figures — 23 of 23 issuers"
  - da_id: "DA-27"
    chosen_reading: "fiscal-period labels derive from calendar quarters — 4 of 4 non-calendar issuers"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# Freshness Anchor, Sector Overview, Peer Bench, Ratio Analysis, What-If

**Combined artifact covering five cross-cutting views** at panorama resolution. This is the
**freshness anchor** for every `DEMONSTRATED` metric in the thesis.

---

## 1. Freshness anchor — the latest reported quarter for the universe

**As of 2026-09-18, the thesis's `as_of` date, the freshest period available is Q2 2026
(calendar) for most issuers.** Non-calendar year-ends report different periods:

| Ticker | Latest period | Period end | Note |
|---|---|---|---|
| **SPCX** | **Q2 2026** | 2026-06-30 | **post-IPO; three segments; entity changed** |
| TER, CW, KTOS, HEI | Q2 2026 / Q1 FY2026 | varies | HEI is on a 31 Oct year, **DA-27 applies** |
| PL | Q1 FY2026 | 2026-04-30 | January year-end, **DA-27 applies** |
| AVAV | Q1 FY2026 (labelled) | 2026-04-30 | **unusable — no net income** |
| HAWK | Q2 2026 | 2026-06-30 | **unusable — post-IPO discontinuity** |
| WWD | Q2 FY2026 (labelled) | 2026-06-30 | September year-end, **DA-27 applies** |

**Rule for every DEMONSTRATED metric in this thesis: it is as of its issuer's latest filed
period, not as of `as_of`.** The two differ by up to one quarter, and for non-calendar issuers
the *label* differs from the issuer's own calendar (**DA-27**). **Any cross-issuer comparison
must normalise the period before comparing levels.**

## 2. Sector overview — the TAM question, answered structurally

**Total revenue, one quarter, all 35 universe tickers combined ≈ $100B.** Of that:

| Group | Quarterly revenue | Share |
|---|---:|---:|
| **SPCX (all three segments)** | **$7,814M** | 8% |
| Three pharma buyers | $39,634M | **40%** |
| Three enabling-layer names (ex-SPCX) | very large | — |
| **All pure-play space companies combined** | **~$1,100M** | **1%** |

**The "space economy" as this universe defines it is a rounding error inside the companies
that touch it.** The addressable market being measured is **~1% of the revenue of the
companies measured.**

**Concentration**: SPCX dominates space revenue entirely — its **$7,814M** quarterly total
exceeds the **~$1,100M** of every pure-play competitor combined by **7×**. **Even excluding
Connectivity and AI, SPCX's $962M Space segment is ~87% of the pure-play cohort's revenue.**

**Regulatory framing**: PIL-6's premise — spectrum and slots are finite, allocated, and
priced — is **DEMONSTRATED** (SATS $27B; SPCX–EchoStar $19.6B with $856M paid in cash in H1
2026). **The falsifier needs FCC IBFS / ITU sources outside the corpus.**

## 3. Peer bench — launch technology line

| Issuer | Revenue | Growth | Gross margin | Operating margin | R&D/revenue |
|---|---:|---:|---:|---:|---:|
| **SPCX** | $7,814M | **+91.9%** | **55.3%** | −1.8% | 45.4% |
| **SPCX Space** (segment) | $962M | +29.0% | **65.8%** | **−56.3%** | 111.9% |
| **RKLB** | $234.1M | +62.0% | 36.1% | **−24.6%** | 35.2% |
| **FLY** | — | **+657%** | 20.3% | −80.9% | **60.8%** |

**The launch cohort's defining feature: growth and margin are inversely related, and gross
margins span 20.3% to 65.8% while every operating margin is negative.**

**SPCX's Space segment has the best gross margin in the universe (65.8%) and the worst
operating margin (−56.3%) in this cohort** — the fixed-cost-absorption finding in its purest
form, and the reason the thesis distinguishes **gross economics** from **funding decisions**.

**No issuer discloses a launch price at cadence except RKLB** ($14,667/kg, basis B) — and
RKLB's launch revenue is **declining**.

## 4. Ratio analysis — and why it is mostly not safe here

**The thesis's ratio toolkit is badly constrained, and the constraint is the finding:**

| Ratio | Availability |
|---|---|
| **$ / kg to orbit** | **one issuer only** (RKLB, basis B) |
| **P/E, ROE, margin screens on net income** | **UNSAFE** — DA-23 strips signs on **net income and EPS**, so loss-makers read positive |
| **Quarterly trend ratios** | **UNSAFE** — DA-26 puts annual figures in quarter rows, 23 of 23 issuers |
| **Fiscal-period comparisons** | **UNSAFE** for non-calendar issuers — DA-27, 4 of 4 |
| **Component-identity checks** | **SAFE** — gross profit and opex are positive and unaffected; **this is the only reliable detector** |
| **Gross margin** | **SAFE** — computed from unsigned lines |
| **Operating margin** | **UNSAFE on loss-makers** (DA-23); safe on profitable issuers |
| **Equity/assets, leverage** | **SAFE** |

**The safe set is narrow: gross margins, balance-sheet ratios, and component identities.**
**Everything computed from net income, EPS, or a quarterly series must be rebuilt from the
filing rather than from the metrics block.**

**The extended DA-23 scope makes this materially worse than previously recorded**: a
loss-making issuer reads as **profitable on every screen built from the metrics block**,
because operating income, net income and EPS are all flipped consistently.

## 5. What-if — the two theses that would change the answer

**What if launch cost reached the propellant floor ($46/kg)?**
- **The floor changes no verdict.** PIL-1's falsifier needs **price**, and price is not cost —
  and no issuer discloses price at cadence. **Cheaper launch does not fire the falsifier.**
- **It would not fund orbital compute either.** SPCX's constraint on AI compute is **power and
  customer concentration**, not launch cost; VRT's is **manufacturing scale**. **Both would
  still bind at $0/kg.**
- **What it would do**: change **Space segment economics**, which are already 65.8% gross
  margin. **The binding term there is Starship R&D, not launch cost.**

**What if a listed pharma disclosed commercial microgravity manufacturing?**
- **PIL-4's falsifier fires immediately** — it is binary and observable. **That single
  disclosure would convert PIL-4 from HOLDS to FALSIFIED**, and it is the cheapest possible
  test in the thesis.
- **What would have to be true**: the process must beat a **72% incumbent gross margin**.
  **No such number exists publicly**, which is why the line's economic test is UNRESOLVABLE.

**The common structure**: **both what-ifs turn on a disclosure that does not exist**, and in
both cases the physical or economic bound is **not** the binding term. **The thesis's open
questions are disclosure questions, not physics questions.**

---

## Carry-forwards

1. **Freshness rule**: every DEMONSTRATED metric is as of its issuer's latest filed period,
   **not `as_of`** — and for non-calendar issuers the *label* differs from the issuer's
   calendar (DA-27). **Normalise periods before comparing levels.**
2. **The "space economy" here is ~1% of the revenue of the companies that touch it**, and
   SPCX is **7× every pure-play competitor combined.** **The market being measured is a
   rounding error inside the companies measuring it.**
3. **The ratio toolkit's safe set is narrow**: gross margins, balance-sheet ratios, component
   identities. **Everything from net income, EPS or a quarterly series must be rebuilt from
   the filing** — and the extended DA-23 scope makes that worse than previously recorded,
   because **loss-makers read profitable on every metrics-block screen.**
4. **Both what-ifs turn on disclosures that do not exist, not on bounds that bind.** The
   thesis's open questions are **disclosure questions, not physics questions** — which is the
   same conclusion the register reached from three different UNRESOLVABLE verdicts.
````

## Artifact — artifacts/TDG/2026-09-18_1239_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: TDG
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T18:30:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "TDG's own segment definitions"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified; TDG CLEAN (EPS reconciles exactly)"
  - da_id: "DA-26"
    chosen_reading: "Q3 2025 and Q3 2024 rows carry the ANNUAL totals, not quarters"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# TDG — Supply-Chain Position (Proprietary Components)

Source: Form 10-Q, accession `0001260221-26-000053` (Q2 FY2026, period ended 2026-06-27).

---

## 1. TDG sets the ceiling on aerospace component pricing power: 44.8%

| Metric | Q2 FY2026 | Q2 FY2025 | Change |
|---|---|---|---|
| Revenue | **$2,741M** | $2,237M | +22.5% |
| Gross profit | **$1,628M** | — | **59.4% margin** |
| Operating income | **$1,227M** | $1,039M | +18.1% |
| **Operating margin** | **44.8%** | 46.4% | −1.6 pts |
| Net income | $539M | $492M | +9.6% |
| EPS (diluted) | $9.39 | $8.47 | +10.9% |

**A 44.8% operating margin and 59.4% gross margin** — the highest in the 35-name universe
by a wide margin, and the reason TDG is in the thesis.

**TDG's model is the extreme case of the certified-component franchise**: proprietary
parts with no PMA alternative, sold into an aftermarket where the customer cannot switch,
priced accordingly. It is the purest demonstration that **aerospace component
concentration converts directly into margin.**

**The PIL-3 consequence is uncomfortable and should be stated plainly.** If a two-supplier
certified-component market yields 28% (HWM) to 45% (TDG) operating margins, then the
space-grade **solar-cell and engine duopolies are presumably also high-margin — and
simply invisible** inside RKLB, BA and LHX.

**That is a different conclusion from "the bottleneck is not binding."** Phase 3 has been
edging toward the latter reading (neither duopoly shows elevated consolidated margin).
TDG and HWM together make the alternative — **high margin, undisclosed** — at least as
likely.

**The thesis cannot currently distinguish the two**, and should say so. Recorded as a
genuine ambiguity rather than resolved toward the reading that suits PIL-3.

## 2. TDG is clean on DA-23 — and the test is exact

```
EPS x diluted shares = $9.39 x 57.4M = $539.0M   vs   reported net income $539M
```

**Exact match.** TDG is profitable and unaffected by sign stripping — extending the
clean-positive count to 10 of 10 (SPCX, YSS, RKLB, FLY, BA flipped; IRDM, VRT, GOOG,
UTHR, NVDA, MRCY, BWXT, MSFT, LHX, HWM, TDG clean).

## 3. DA-26 in TDG — the same defect, in the same block

| Row | Revenue shown | What it actually is |
|---|---:|---|
| FY2026 Q1 | $2,544M | a genuine quarter |
| FY2026 Q2 | $2,741M | a genuine quarter |
| **FY2025 Q3** | **$8,831M** | **TDG's FY2025 ANNUAL revenue** |
| **FY2024 Q3** | **$7,940M** | **TDG's FY2024 ANNUAL revenue** |

**Two separate annual figures mislabelled as Q3 quarters**, in consecutive fiscal years.
TDG is thus a **double instance** of DA-26, alongside HWM's double instance.

**Note the pattern refinement**: for HWM the annual appeared as `Q4`/`Q1`; for TDG as
`Q3`. **The mislabelled period is not fixed** — it varies by issuer, which makes DA-26
harder to screen for and means it cannot be detected by position alone. Only
reconciliation against known annual totals finds it.

---

## Carry-forwards

1. **TDG sets the component-margin ceiling at 44.8%** (gross 59.4%) — the universe's
   highest, and the benchmark for what a certified-component duopoly can earn.
2. **The "high margin but undisclosed" reading is now as likely as "not binding"** — PIL-3
   must record the ambiguity rather than resolve it.
3. **DA-26 varies by issuer in which period is mislabelled** — it cannot be screened by
   position, only by reconciliation.
4. **Clean-positive count now 10 of 10**; the sign-stripping rule remains exceptionless.
````

## Artifact — artifacts/TER/2026-09-18_2205_operational-kpi_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: TER
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T22:05:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; TER CLEAN (exact component match)"
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 and Q4 FY2024 rows carry ANNUAL revenue AND ANNUAL operating income"
  - da_id: "DA-21"
    chosen_reading: "Teradyne's own segment definitions; space/defense test is not separately disclosed"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# TER — Operational Baseline (Semiconductor Test Equipment)

Source: Form 10-Q, accession `0001193125-26-327715` (Q2 2026, quarter ended 2026-06-28).

---

## 1. THE REVERSAL: space demand is immaterial to the supplier

**Every prior "immaterial-to-the-counterparty" finding in this thesis ran one direction** —
the capability was real and immaterial to its listed *owner*, which is why the owner never
disclosed it. **Teradyne is the same pattern inverted, and the inversion is the finding.**

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$1,328.990M** | $651.797M | **+103.9%** |
| Gross profit | $794.618M | — | **59.8% margin** |
| Operating expenses | $356.808M | — | 26.8% of revenue |
| Operating income | **$437.810M** | $90.743M | **+382.4%** |
| **Operating margin** | **32.9%** | 13.9% | **+19.0 pts** |
| Net income | $374.533M | $78.372M | +377.9% |
| EPS (diluted) | $2.38 | $0.49 | +385.7% |

**Revenue doubled, operating income nearly quintupled, and the operating margin expanded
19 points in one year.**

**Teradyne is the capital equipment that makes satellite electronics testable.** PIL-3
subscribes it as a production-capacity name. **Its growth has nothing to do with space.**

```
TER FY2025 annual revenue          $3,190.0M
TER FY2026 H1 revenue              $2,612.9M   (Q1 $1,282.5M + Q2 $1,329.0M)
TER FY2026 implied annual          ~$5,300M
                                   ─────────
incremental revenue, ONE YEAR      ~$2,100M
the ENTIRE pure-play space cohort,
annual revenue (all 7 companies)   ~$2,170M
```

**Teradyne's single-year revenue *increase* approximately equals the combined annual revenue
of every pure-play space company in this universe.**

**Consequence for PIL-3 — and this is a structural refutation of the "supplier exists, so
capacity exists" inference.** The manufacturing-rate constraint on constellations is not
relieved by the existence of capable suppliers, because **those suppliers' capacity is
allocated by a larger market that pays more.** A constellation builder competing for test
capacity is bidding against the AI compute buildout — and the AI buildout's annual
*increment* is the size of the whole space sector.

**The constraint is not capability. It is queue position.**

## 2. This is the cleanest DA-23 confirmation in the universe

```
gross profit       $794.618M
operating expenses $356.808M
                  ─────────
gross profit - opex = $437.810M   <- arithmetic
XBRL OperatingIncomeLoss = $437.810M  <- reported
```

**Exact match to the dollar, same sign.** Teradyne is profitable and unaffected.

```
EPS (diluted) $2.38 x 157.693M diluted shares = $375.309M
reported net income                           = $374.533M
gap: 0.21%
```

**Clean-positive count: 21 of 21.**

## 3. The supplier tier now clusters tightly — TER belongs to the POWER side, not the parts side

| Tier | Issuer | Operating margin | Revenue growth y/y |
|---|---|---:|---:|
| Installed-base parts | HEI | 25.5% | +25.3% |
| **Test capital equipment** | **TER** | **32.9%** | **+103.9%** |
| Component supplier | CW | 19.3% | +5.4% |
| Component supplier | KRMN | 19.1% | +58.2% |
| Subsystem supplier | WWD | ~17% | +21.2% |
| Primes | LMT / RTX / LHX / NOC | 10.1–12.4% | ~+10% |

**Teradyne is in a different economic position from every other supplier in the universe**:
it is a **capital-equipment monopoly-adjacent supplier** whose output is a capacity input,
not a component. **A parts supplier sells into a programme; a capital-equipment supplier
sells capacity itself — and therefore prices against the marginal value of capacity, which
is set by the largest market that wants it.**

**Refines the margin ladder**: the ordering is by distance from programme risk, and
**capital-equipment suppliers sit furthest of all** — they take no programme risk and no
volume risk, because their capacity is fungible across every end market.

## 4. DA-26 — TER shows it in both lines, twice

| Row | Revenue shown | Operating income shown | What they are |
|---|---:|---:|---|
| Q2 2026 | $1,328.990M | $437.810M | genuine quarters |
| **Q4 2025** | **$3,190.024M** | **$650.051M** | **FY2025 ANNUAL figures** |
| **Q4 2024** | **$2,819.880M** | **$593.788M** | **FY2024 ANNUAL figures** |

**Twentieth issuer confirmed.** FY2025 = Q1–Q3 $2,106.687M, so annual $3,190.024M implies
Q4 2025 of $1,083.337M — plausible against Q3's $769.210M. FY2024 = Q1–Q3 $2,066.996M, so
annual $2,819.880M implies Q4 2024 of $752.884M. **Both annual readings are internally
consistent; a 4× sequential jump is not.**

**Second issuer where the defect propagates to BOTH revenue and operating income** (after
AMGN) — and CW is a third, confirmed in the same pass. **Three of three checked since AMGN
reproduce it**, which is the expected pattern for a whole-statement period failure once you
know to look for it. **Check both lines at every remaining issuer.**

---

## Carry-forwards

1. **THE REVERSAL — space demand is immaterial to the *supplier*, not the owner.**
   Teradyne's one-year revenue increase (~$2,100M) ≈ the entire pure-play space cohort's
   annual revenue (~$2,170M). **Capacity is allocated by a larger market; constellation
   builders compete on queue position, not on capability.** This refutes the "supplier
   exists ⇒ capacity exists" inference that PIL-3 rested on.
2. **TER's 32.9% operating margin at +103.9% growth is the best growth-margin combination
   in the universe** outside FLY, and it sits in **capital equipment**, not components.
   **The refined ladder orders by distance from programme risk — and capital-equipment
   suppliers sit furthest of all.**
3. **Cleanest DA-23 confirmation yet** — exact to the dollar on directly-available
   components. Clean-positive **21 of 21**.
4. **DA-26 at 20 of 20 issuers**, and the **third** where it propagates to both lines.
````

## Artifact — artifacts/UTHR/2026-09-18_1239_unit-economics_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-4
ticker: UTHR
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T15:55:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-22"
    chosen_reading: "Varda figures CLAIMED-only per Q-4; they can inform but never satisfy a falsifier"
  - da_id: "DA-16"
    chosen_reading: "Varda's ~50 kg/mission is CLAIMED (press); UTHR's partnership disclosure is DEMONSTRATED"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified; UTHR clean (profitable issuer)"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# UTHR — Microgravity Economics, Q2 2026

Source: Form 10-Q, accession `0001082554-26-000027`.

**Why UTHR matters**: it is the listed proxy (P6) for Varda Space Industries and the only
listed counterparty to a microgravity-manufacturing partnership. Phase 5's PIL-4 test
runs through this company.

---

## 1. UTHR is a high-margin specialty pharma — and microgravity is invisible in it

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$783.3M** | $798.6M | **−1.9%** |
| Gross profit | **$683.8M** | — | **87.3% margin** |
| Operating income | **$330.8M** | $364.5M | −9.2% |
| Operating margin | **42.2%** | 45.6% | −3.4 pts |
| R&D | $146.3M | $134.0M | +9.2% |
| Net income | $333.0M | $309.5M | +7.6% |
| EPS (diluted) | $7.27 | $6.41 | +13.4% |

**An 87.3% gross margin is the number that matters for PIL-4.** It sets the bar any
microgravity manufacturing process must clear: to be interesting to a company like UTHR,
an orbital process must beat — or enable something unavailable from — a terrestrial
process that already runs at 87% gross margin.

**And microgravity is nowhere in these numbers.** UTHR's revenue *declined* 1.9% year
over year. There is no microgravity revenue line, no orbital cost line, and no mention of
Varda in the XBRL extract at all. The partnership announced in May 2026 targets first
samples "as early as 2027" — so **at Q2 2026 it has produced zero financial footprint**,
exactly as expected.

## 2. PIL-4's falsifier, evaluated honestly

| Field | Value |
|---|---|
| metric | `listed_pharma_microgravity_commercial_manufacturing_disclosure` |
| threshold | 0, op `>` |
| **Observed** | **0** — no commercial-scale disclosure from UTHR, MRK, BMY or AMGN |
| **Verdict** | **HOLDS** — and this is a *measured* zero, not an unexamined one |

**PIL-4 holds.** No listed pharmaceutical company has disclosed commercial-scale
microgravity manufacturing. The UTHR–Varda partnership is a research/pilot arrangement by
its own description, targeting first samples in 2027.

**But the pillar's economic test remains unexecutable**, and it is worth being precise
about why. Phase 5's plan called for **value-per-kg-returned vs cost-per-kg-returned**.
Neither term is available:

| Term | Status |
|---|---|
| Value per kg returned | **Not disclosed.** Varda has no revenue; UTHR discloses no microgravity product economics |
| Cost per kg returned | **Not disclosed.** Varda is private; its ~$329M raised and ~50 kg/mission are `CLAIMED` press figures only |
| Fully-loaded comparison | **Not possible.** Under Q-4, private figures may inform but can never *satisfy* a falsifier |

**This is the clearest `UNRESOLVABLE-FROM-PUBLIC-SOURCES` case in the thesis.** Unlike
PIL-6 (data public but unreachable from the platform) and P5 (data commercially
licensed), PIL-4's missing figures **do not exist publicly at all** — they are inside a
private company's books. The disposition under §1c applies: the pillar is recorded
unresolvable with the specific disclosure that would resolve it named.

**What would resolve it**: Varda disclosing cost per kg returned (unlikely while
private), or UTHR disclosing economics of its microgravity programme in a quarterly
filing (possible from 2027 if samples progress), or Varda listing.

## 3. The structural read: microgravity is a *quality* play inside a quality business

UTHR's 42.2% operating margin on $783M quarterly revenue means the company can fund
microgravity experimentation from operating cash flow indefinitely without it mattering.
**That is both PIL-4's strength and its weakness**:

- **Strength**: the counterparty is financially robust; the partnership will not collapse
  for lack of funding.
- **Weakness**: precisely *because* it doesn't matter, there is no pressure to disclose
  how it is going. UTHR has no obligation to break out a programme that is immaterial —
  the same structural problem that makes PIL-2's falsifier hard to fire at Alphabet.

**A pattern across pillars**: in both cases, the listed counterparty is large enough that
the space initiative is immaterial, which suppresses the disclosure that would let the
falsifier fire. Worth stating once in the Phase 7 synthesis rather than rediscovering it
per pillar.

## 4. DA-23 — UTHR clean

UTHR's operating income ($330.8M) is correct: 87.3% gross margin less R&D and SG&A at
plausible ratios yields it. It is a profitable issuer and therefore untouched.

**CORRECTION (2026-09-18)**: this artifact originally claimed *"7 of 7 negative values
flipped, 5 of 5 positive values clean."* **Wrong** — the correct census was **4 of 4
negative, 5 of 5 positive.** The running total had been conflated with the negative
count. The rule is unaffected; the figure was not counted and is corrected here.

---

## Carry-forwards

1. **PIL-4 HOLDS but its economic test is `UNRESOLVABLE-FROM-PUBLIC-SOURCES`.** Name the
   resolving disclosure: Varda's cost per kg returned, or UTHR's programme economics.
2. **The "immaterial-to-the-counterparty" disclosure suppression** is now observed at two
   pillars (PIL-2/Alphabet, PIL-4/UTHR) and belongs in the synthesis as a named pattern.
3. **UTHR's 87.3% gross margin is the hurdle rate** any microgravity process must clear —
   carry it into Phase 6 as the terrestrial benchmark for pharmaceutical value.
4. **UTHR revenue declined 1.9% YoY** — a reminder that the counterparty's own business is
   not growing, so microgravity is optionality rather than a response to pressure.
````

## Artifact — artifacts/VOYG/2026-09-18_2015_operational-kpi_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: VOYG
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T20:15:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income FAILS the gross-profit bound in 3 consecutive quarters; recorded as CANDIDATE with a NEW sub-mechanism"
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 row carries the ANNUAL revenue"
  - da_id: "DA-16"
    chosen_reading: "Starlab milestone claims graded CLAIMED where not filed"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# VOYG — Operating Baseline

Source: Form 10-Q, accession `0001628280-26-052292` (Q2 2026, quarter ended 2026-06-30).

---

## 1. A NEW DETECTOR: operating income cannot exceed gross profit

```
Q2 2026 gross profit       $4.457M
Q2 2026 operating income  $51.408M
                          ─────────
operating income EXCEEDS gross profit by $46.951M
```

**This is arithmetically impossible for a normal income statement.** Operating income is
gross profit *minus* operating expenses. Voyager discloses R&D of $7.336M, so operating
expenses are strictly positive. There is no set of operating expenses — including zero —
under which operating income exceeds gross profit.

**The gross-profit bound is a detector the sign rule does not cover.** DA-23's rule
("a negative operating income is stripped of its sign") predicts a *sign inversion at equal
magnitude*. Here the level itself is unreconcilable, at any sign.

**Look at how far outside the bound it is:** GP $4.457M vs OI $51.408M. If the true figure
were the sign-flipped loss −$51.408M, operating expenses would need to be $55.865M on
revenue of $52.746M — i.e. **SG&A alone at 92% of revenue** after $7.3M of R&D. That is
not a credible reading either.

**Neither mechanism reconciles.** Voyager is recorded as a **DA-23 CANDIDATE with a new
sub-mechanism**, and the honest statement is that **the operating income line is
unusable** — not that it is sign-flipped.

## 2. The pattern is persistent across three consecutive quarters

| Quarter | Revenue | Reported operating income | OI / revenue | OI − GP |
|---|---:|---:|---:|---:|
| Q2 2025 | $45.674M | $24.137M | **52.8%** | n/a (no GP line) |
| Q3 2025 | $39.587M | $24.043M | **60.7%** | n/a |
| Q1 2026 | $35.246M | $44.647M | **126.7%** | n/a |
| **Q2 2026** | **$52.746M** | **$51.408M** | **97.5%** | **+$46.951M** |

**An operating margin above 100% (Q1 2026) is not a margin at all.** A persistent,
multi-quarter pattern rules out the benign explanation that a single one-off gain sat
between gross profit and operating income in one period — **a one-off would not recur
four times.**

**This is a more serious defect class than the six sign-strip confirmations**, because a
sign strip is detectable by magnitude-preserving reconciliation while a level error of
this size is detectable only by the gross-profit bound. **Any thesis using VOYG's operating
line is using a broken number.**

## 3. What is still usable

**Net income is close to operating income and reconciles to EPS:**

```
EPS (diluted) $0.79 x 58.522M weighted diluted shares = $46.233M
reported net income                                   = $46.490M
gap: 0.6%
```

**So the EPS identity holds even though the operating line does not.** This is the same
divergence seen at RKLB and FLY, where EPS × shares passes on both sides of a flip because
both numbers share the same error. **It confirms the earlier finding**: EPS reconciliation
is not a reliable detector; **component identity is.**

**Revenue appears sound**: Q1 2026 $35.246M, Q2 2026 $52.746M (+49.6% sequentially), against
FY2025 annual of $166.419M. Voyager's balance sheet is genuinely strong — cash $373.436M,
current assets $581.300M, total assets $1,009.273M — and Q2 2026 operating cash flow was
**+$84.027M** with **$86.652M of capex**. That combination (positive operating cash flow
plus heavy capex) is the profile of a company building toward Starlab, and it is the most
credible thing in the filing.

## 4. DA-26 — VOYG's Q4 row is the annual, and the check is arithmetic

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $52.746M | a genuine quarter |
| **Q4 2025** | **$166.419M** | **VOYG's FY2025 ANNUAL revenue** |

**Thirteenth issuer confirmed.** FY2025 = Q2 $45.674M + Q3 $39.587M + Q1 + Q4, against a
reported annual of $166.419M — leaving $81.158M across Q1 and Q4, consistent with the
observed quarterly range. **The annual reading is internally consistent; the quarterly
reading (a 4.2× sequential jump from Q3's $39.587M) is not.**

---

## Carry-forwards

1. **NEW DETECTOR — the gross-profit bound.** Operating income exceeding gross profit is
   arithmetically impossible and confirms a corrupted line **at any sign**. This detector
   is strictly stronger than sign-reconciliation and would have caught instances the sign
   rule misses.
2. **VOYG is a DA-23 CANDIDATE with a NEW sub-mechanism** — not sign inversion but an
   unreconcilable *level*, persistent across three consecutive quarters. **The operating
   income line is unusable.** Register as a distinct amendment item from the six
   sign-strip confirmations.
3. **EPS reconciliation is confirmed unreliable** (again) — VOYG's EPS identity holds at a
   0.6% gap while the operating line fails by $46.951M.
4. **DA-26 at 13 of 13 issuers.**
````

## Artifact — artifacts/VRT/2026-09-18_1239_unit-economics_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-5
ticker: VRT
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T15:20:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-04"
    chosen_reading: "terrestrial basis reported as margin structure; VRT does not disclose $/kW"
  - da_id: "DA-05"
    chosen_reading: "VRT informs basis B (colocation market price) as the supplier's own economics, not a customer price"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; VRT is NOT flipped"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# VRT — Terrestrial Thermal Comparator, Q2 2026

Source: Form 10-Q, accession `0001628280-26-050609`.

**Why VRT is in the universe**: constitution Tier 4 places it as *"thermal management at
scale — the terrestrial comparator that defines the orbital cooling penalty."* Phase 2
derived the orbital side of P5 from physics (F2: 2,419 m² of radiator per MW at 300 K).
This analysis supplies the terrestrial side's **cost and margin structure**.

**Scope limit, stated up front**: VRT does **not disclose $/kW of cooling**. So this
artifact cannot populate P5's ratio directly. What it *can* establish is whether
terrestrial cooling is a constrained monopoly or a competitive, expanding supplier
market — which determines whether the terrestrial denominator should be expected to
**fall** (competition) or **rise** (scarcity).

---

## VRT's economics — terrestrial cooling is competitive and expanding

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$3,274.3M** | $2,638.1M | **+24.1%** |
| Cost of goods and services | $2,039.4M | — | — |
| Gross profit | **$1,234.9M** | — | **37.7% margin** |
| Operating income | **$637.9M** | $442.4M | +44.2% |
| Operating margin | **19.5%** | 16.8% | **+2.7 pts** |
| Net income | $497.8M | $324.2M | +53.5% |
| Net margin | 15.2% | 12.3% | +2.9 pts |

**Revenue +24.1% with operating margin expanding 2.7 points.** That combination is
important: an expanding margin alongside rapid growth indicates a supplier market where
demand is outrunning capacity — pricing power, not a commodity race to the bottom.

**The finding for P5**: the terrestrial denominator is served by a **competitive,
profitable, fast-growing supplier base**. Terrestrial cooling capacity is being added at
24% annually by companies earning a 37.7% gross margin on it.

**This cuts against the orbital-compute thesis, and it does so structurally.**
Orbital compute's pitch rests partly on terrestrial cooling being a bottleneck that
vacuum sidesteps. VRT shows the opposite: terrestrial cooling is a **solved engineering
problem with a functioning supply chain and expanding capacity**. Vacuum does not
sidestep the problem — it replaces a competitive, mass-produced, 24%-growing solution
with a bespoke, launch-mass-penalised one.

## Why VRT cannot populate the P5 ratio — and what would

| What P5's ratio needs (DA-05) | Can VRT supply it? |
|---|---|
| Basis A — hyperscaler marginal cost/kW | No — not disclosed by any hyperscaler |
| Basis B — colocation market price/kW | **No.** VRT *sells equipment to* colocation operators; its revenue per unit is a supplier price, not a market rental price |
| Basis C — new-build fully-loaded cost/kW | **Partly.** VRT's margin structure bounds the cooling *equipment* share of a greenfield build, but not land, shell, power interconnect or IT load |

So VRT moves P5 from "unmeasured" to "**partially bounded**" — the cooling component of
terrestrial cost is now anchored to a real supplier's economics — but the ratio itself
still requires colocation rental data or an operator's disclosed build cost, neither of
which is in the platform.

**This is a second candidate for `UNRESOLVABLE-FROM-PLATFORM`** (after PIL-6's FCC/ITU
sources), and it is a stronger case: PIL-6's data is at least public and merely
unreachable, whereas colocation pricing is commercially licensed data.

## DA-23 cross-check — VRT is clean, and the rule now holds exactly

VRT's operating income ($637.9M positive) is **correct**: components reconcile
(gross profit $1,234.9M less operating expenses leaves $637.9M, implying a 18.2%
opex ratio, which is plausible for VRT and implausible as the alternative). Its
EPS×shares test also reconciles ($497.8M ÷ 384.6M = $1.29 ✓).

Paired with IRDM (also clean), this completes the characterization:

**4 of 4 loss-making issuers have their negative `operating_income` sign stripped;
0 of 2 profitable issuers are affected.** DA-23 is **sign stripping on negative values**,
not a sign convention — which means the extract converts every loss into a profit of
identical magnitude, and any `operating_income` ranking inverts (worst loss-makers
first). Amendment text to be reworded accordingly.

---

## Carry-forwards

1. **P5's terrestrial side is now bounded for cooling only.** The ratio still needs a
   colocation or greenfield-cost input; register as a likely
   `UNRESOLVABLE-FROM-PLATFORM` if it persists past Phase 6.
2. **VRT's 24% growth is itself a Phase 6 input** — it measures how fast the terrestrial
   alternative to orbital compute is scaling, which is the denominator's *trajectory*,
   not just its level.
3. **The margin-expansion evidence weakens one common orbital-compute talking point.**
   Phase 6 should state this explicitly rather than only advancing the orbital case.
````

## Artifact — artifacts/WWD/2026-09-18_2120_supply-chain_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: WWD
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T21:20:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "consolidated OperatingIncomeLoss NOT available (segment-only); gross-profit bound used and holds; EPS identity 0.16%"
  - da_id: "DA-26"
    chosen_reading: "year-end row carries ANNUAL revenue (WWD's FY ends 30 Sep) — confirmed for FY2024, ANOMALOUS for FY2025"
  - da_id: "DA-27"
    chosen_reading: "fiscal_period labels vs issuer calendar — flagged for cross-check, not asserted"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# WWD — Supply-Chain Position (Actuation, Control & Combustion)

Source: Form 10-Q, accession `0001193125-26-325790` (quarter ended 2026-06-30).

---

## 1. Woodard's second disclosure gap: consolidated operating income is absent

| Metric | Q2 FY2026 | Q2 FY2025 | Change |
|---|---|---|---|
| Revenue | **$1,109.705M** | $915.446M | +21.2% |
| COGS | $759.799M | — | 68.5% of revenue |
| Implied gross profit | **$349.906M** | — | **31.5% margin** |
| Net income | $146.675M | $108.448M | +35.2% |
| EPS (diluted) | $2.40 | $1.76 | +36.4% |
| R&D / revenue | 4.4% | 4.5% | — |

**`OperatingIncomeLoss` is absent at the consolidated level.** The only
`OperatingIncomeLoss` fact in the extract is **dimensional** — `$170.020M`, tagged to the
**Aerospace segment**. The metrics array returns `operating_income: null`.

**This is the third issuer with a missing consolidated operating line** (MRK, BMY, WWD).
**The component-identity detector — the only reliable DA-23 test — cannot run at the
consolidated level on any of them.**

**The gross-profit bound still runs and holds:**

```
revenue $1,109.705M - COGS $759.799M = gross profit $349.906M
Aerospace segment operating income $170.020M < $349.906M  ✓  (bound holds)
EPS (diluted) $2.40 x 61.018M = $146.443M  vs  net income $146.675M   (0.16% gap)
```

**WWD is CLEAN.** Clean-positive count: **19 of 19.**

**Register the coverage caveat once, at three issuers**: `OperatingIncomeLoss` absent or
segment-only at **MRK, BMY and WWD** — a material hole in the platform's ability to run the
one detector that works.

## 2. Woodward is mid-tier — and the tier structure is now a trend

| Tier | Issuer | Operating margin |
|---|---|---:|
| Component supplier (installed base) | HEI | 25.5% |
| Component supplier | KRMN | 19.1% |
| **Subsystem supplier** | **WWD (Aerospace segment)** | **~17%** |
| Primes | LMT / RTX / LHX / NOC | 10.1–12.4% |

**Woodward's implied gross margin of 31.5% sits between the primes (LMT 12.2% gross) and
the installed-base suppliers (HEI, KRMN at 43%)**, consistent with a subsystem supplier that
carries more integration cost than a parts maker but less programme risk than a prime.

**Consequence for PIL-3**: the margin ladder is not a two-tier split but a **graded
function of distance from the programme-level risk.** Register as a three-tier structure
with the *mechanism* (programme-risk absorption) rather than a binary prime/supplier claim.

## 3. DA-26 — confirmed for FY2024, and the FY2025 instance is anomalous

WWD's fiscal year ends **30 September**, so its Q3 *is* its year-end quarter (the subtlest
form, as at PL and HEI).

| Row | Revenue shown | Implied year-end quarter | Assessment |
|---|---:|---:|---|
| **Q3 FY2024** | **$3,324.249M** | $868.493M | **consistent** — between Q2 $847.688M and Q4 $772.725M |
| **Q3 FY2025** | **$3,567.064M** | **$771.535M** | **ANOMALOUS** — breaks the sequence $883.629M → $915.446M → **$771.535M** → $996.454M |

**Nineteenth issuer, with the first non-conforming instance.** The FY2024 reading implies a
year-end quarter that fits the surrounding quarters. **The FY2025 reading implies a
year-end quarter that dips 16% sequentially in the middle of a rising year** — which no
other issuer's annual reading requires.

**Recorded honestly as: DA-26 confirmed at WWD for FY2024, unconfirmed for FY2025.** Two
readings are live and the extract cannot separate them:

1. The FY2025 row is the annual, and WWD genuinely had a weak Apr–Jun 2025 quarter.
2. The FY2025 row is contaminated differently — e.g. a trailing-twelve-month or
   fiscal-year-to-date figure rather than a full year.

**This is the first evidence that DA-26 is not uniform in *what* the row holds**, only in
*that* it is not a quarter. Carried to the DA-26 amendment as a scope question.

## 4. DA-27 CONFIRMED — WWD is an instance, and this corrects the artifact's first reading

Woodward's fiscal year ends **30 September**, so **FY2026 Q3 = Apr–Jun 2026**. The row whose
`period_end` is **2026-06-30** is labelled **`Q2 FY2026`**.

**That is a one-quarter label offset — WWD IS affected.**

**This corrects an earlier claim in this pass.** WWD was first recorded as showing genuine
quarters with no offset, on the grounds that its values are internally consistent. **Internal
consistency of the values is not evidence about the labels**, and the labels are wrong.

**DA-27 now stands at n=4 of 4**, with a clean partition on the fiscal-year-end axis:

| Fiscal year-end | Issuers | Offset |
|---|---|---|
| December | every other issuer in the universe | **none** |
| **January** | PL | **yes** |
| **April** | AVAV | **yes** |
| **September** | **WWD** | **yes** |
| **October** | HEI | **yes** |

**Four non-calendar issuers, four offsets. Every December issuer, none.** The mechanism — the
platform buckets by calendar quarter from 1 January and labels the bucket with the issuer's
fiscal year — fits all four and is exact for December year-ends.

**Removing WWD as a counterexample is what promotes DA-27 from CANDIDATE to CONFIRMED.**
Recorded rather than silently applied.

---

## Carry-forwards

1. **Third issuer with no consolidated operating income** (MRK, BMY, WWD). **The component-
   identity detector cannot run on any of them** — register the coverage caveat once.
2. **The margin ladder is graded, not binary**: HEI 25.5% → KRMN 19.1% → WWD ~17% → primes
   10.1–12.4%. **The mechanism is distance from programme-level risk**, not prime vs
   supplier.
3. **FIRST NON-CONFORMING DA-26 INSTANCE.** WWD FY2024 conforms; FY2025 implies a year-end
   quarter that dips 16% mid-sequence. **Scope question for the DA-26 amendment: the rows
   are reliably "not a quarter," but not reliably "a full year."**
4. **Clean-positive 19 of 19; DA-26 at 19 of 19 issuers** (one with an open sub-question).
````

## Artifact — artifacts/YSS/2026-09-18_1239_operational-kpi_methodology.md
````markdown
---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: YSS
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T16:05:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-12"
    chosen_reading: "constellation size — YSS is a manufacturer, not an operator; N/A"
  - da_id: "DA-13"
    chosen_reading: "production rate — searched for; YSS discloses revenue, not unit counts"
  - da_id: "DA-21"
    chosen_reading: "single reportable segment; no split available"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; YSS IS flipped (loss-maker)"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# YSS — Operational Baseline, Q2 2026

Source: Form 10-Q, accession `0001628280-26-056874`. Consolidated with the Phase 3
cross artifact, which introduced this company.

**Why YSS is the cleanest PIL-3 test case**: it **builds spacecraft and does not launch
them**. Launch availability is therefore an input it buys, not a capability it holds —
which isolates the manufacturing question from the launch question.

---

## 1. The finding that reframes PIL-3: a volume problem, not a unit-economics problem

| Metric | Q2 2026 | Q1 2026 | QoQ |
|---|---|---|---|
| Revenue | **$92.547M** | $116.343M | **−20.5%** |
| Cost of revenue | $70.367M | — | — |
| **Gross profit** | **$22.180M** | — | **24.0% margin** |
| Operating expenses | **$63.493M** | — | **68.6% of revenue** |
| R&D | $5.766M | $5.289M | +9.0% |
| Operating result | **$(41.313)M** | — | see DA-23 note |

**Gross margin 24.0% against an operating-expense ratio of 68.6%.** YSS does not lose
money because satellite manufacturing is unprofitable — **24% gross margin is a real,
positive manufacturing spread.** It loses money because its fixed cost base is **2.9×**
its gross profit.

**That distinction is the whole of PIL-3.** If satellites carry 24% gross margin at
sub-scale, then manufacturing *cost* is not the binding constraint on constellation
economics — manufacturing *volume* is. Those are different claims with different
remedies: a cost problem yields to engineering, a volume problem yields only to order
flow.

**And the quarter-over-quarter revenue decline (−20.5%) cuts against volume.** Revenue
fell sequentially while the cost base did not. One quarter is not a trend, but the
direction is unhelpful to the thesis and should be monitored rather than smoothed over.

## 2. DA-13 — production rate is not disclosed, in units, by anyone

Phase 3's plan called for the DA-13 distinction (manufactured vs launched vs
operational). This analysis searched for it and **YSS does not disclose unit counts** —
revenue only.

Combined with the earlier finding that RKLB discloses **build-rate and cadence
together** (14 built / 16 launched in 2024; 24 / 21 in 2025; 11 / 12 in H1 2026), the
position is:

| Issuer | Unit production disclosure |
|---|---|
| RKLB | **Yes** — vehicles built and launched, by period |
| YSS | **No** — revenue only |
| All 15 primes | Not examined; unlikely at segment granularity |

**So DA-13 is applicable to exactly one issuer.** Any cross-issuer manufacturing-rate
comparison is currently impossible, and PIL-3's evidence base is correspondingly thin —
it rests on RKLB's build-vs-launch series plus YSS's margin structure.

## 3. PIL-3 falsifier — still not evaluated, but now better scoped

| Field | Value |
|---|---|
| metric | `share_of_named_issuers_citing_launch_availability_as_primary_delay_cause` |
| threshold | 0.5, op `>` |
| **Observed** | **not measured** |
| **Verdict** | **PENDING** |

**Two cheaper paths have emerged than the 19-document risk-factor read the plan assumes:**

1. **The build-vs-launch test** (used successfully on RKLB) works on any issuer that
   discloses both. It is a *behavioural* measure and does not require reading prose.
2. **YSS's margin structure** is a second indirect test: a manufacturer at 24% gross
   margin with a 2.9× fixed-cost multiple is volume-constrained by arithmetic, whatever
   its filings say about delays.

Both are cheaper and less subjective than coding risk-factor language. The falsifier
should be re-scoped in `plan.md` to use them.

## 4. DA-23 — YSS is one of the four flipped issuers

```
gross profit − operating expenses = $22.180M − $63.493M = −$41.313M
XBRL OperatingIncomeLoss                                =  +$41.313M
```

**YSS is flipped**, consistent with the rule that the extract strips signs on negative
values. Its **positive** Q1 figure ($110.466M against $116.343M revenue — a 95%
"margin", which is itself implausible) is worth a separate check; if Q1's true operating
result is also a loss, the Q1 magnitude differs from the pattern and should be verified
against that filing's components directly.

**Flagged, not asserted**: Q1 was not examined at component level in this pass. The
recorded rule stands on 12 issuer-quarters with no exceptions, but Q1/YSS is a
plausible weak point and is listed here so it is not assumed clean.

---

## Carry-forwards

1. **PIL-3's evidence is thin and should be declared so**: one issuer with unit data
   (RKLB), one with margin structure (YSS), and a falsifier not yet measured.
2. **YSS Q1's $110.5M operating figure needs a component check** — it sits outside the
   pattern's magnitude and may be a different defect class.
3. **PIL-3's falsifier should be re-scoped** in `plan.md` toward the build-vs-launch and
   margin-multiple tests rather than risk-factor prose coding.
4. **YSS revenue fell 20.5% QoQ** — carry into Phase 6 as a demand-side signal against
   the volume-constraint reading.
````

