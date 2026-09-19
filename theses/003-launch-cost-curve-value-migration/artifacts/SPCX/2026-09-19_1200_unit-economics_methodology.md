---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-1
ticker: SPCX
skill: unit-economics
mode: methodology
generated_at: 2026-09-19T12:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-01
    chosen_reading: >
      cost-per-kg basis. All four bases are reported together in every row — A (customer
      list price), A′ (realized revenue per customer launch, carried on TWO numerator
      readings: all-Space-segment revenue and Launch-Services-only, the latter labelled
      A″), B (marginal cost per launch), C (fully-loaded amortized). No basis is ever
      quoted alone. Basis B is the only basis that tests an F5 floor and it is MODELED
      here — this artifact's contribution to PIL-1 is a DEMONSTRATED price against a
      MODELED cost.
  - da_id: DA-02
    chosen_reading: >
      denominator orbit. SPCX's filed mass-to-orbit metric names NO orbit: it is "the
      total kilograms of payload that we deploy to orbit in a given period", summed "from
      all successful orbital and flight tests". Every $/kg in this artifact is therefore a
      $/kg-to-UNSPECIFIED-ORBIT, thesis-normalised to LEO and labelled as such. The
      payload kg is carried explicitly beside every $/kg, on one of five registered
      denominators (§1.1), and the denominator used is named per figure.
  - da_id: DA-03
    chosen_reading: >
      reusable architecture. Architecture is a CLAIM, not a demonstrated property, so it is
      labelled, never asserted. Falcon 9 = `partially_reusable` (booster and fairing
      recovered and depreciated per the filing; second stage expended). Starship is carried
      on TWO architecture rows — `fully_reusable` (the declared target, F5a applied) and
      `fully_expendable` (as flown: no ship catch has occurred; Flight 13 was a
      splashdown).
  - da_id: DA-06
    chosen_reading: >
      price vs cost. A′ and A″ are PRICE; B and C are COST. On this issuer the price is
      DEMONSTRATED and the cost is MODELED, so the two are never differenced into a margin
      without stating which basis each side is on. Every margin below names both.
  - da_id: DA-07
    chosen_reading: >
      mass to orbit. Customer payload tons as filed (87 t in Q2 2026). The metric sums
      "verified mass, including Starlink satellites, customer payloads, and development
      cargo, from all successful orbital and flight tests", excludes failed or scrubbed
      attempts, includes development cargo, and is NOT split by vehicle — so Falcon and
      Starship mass cannot be separated on this platform.
  - da_id: DA-08
    chosen_reading: >
      a "launch". The filed definition is "the sum of all successful orbital and flight
      tests across our rockets, including internal Starlink deployments, development tests,
      and launches for our third-party customers, and excluding any cancellations or
      scrubs". It is therefore not an orbital-launch count: the single Starship launch
      counted in Q2 2026 is Flight 12, described by the issuer as a suborbital mission.
  - da_id: DA-21
    chosen_reading: >
      segment boundaries. Space segment revenue is the CUSTOMER boundary and the issuer
      states it in those words. Internal launch costs are capitalised into satellites and
      generate no inter-segment revenue, so Space cost of revenue is the CUSTOMER-launch
      cost base, not the fleet's — which changes which denominator is comparable to it.
  - da_id: DA-23
    chosen_reading: >
      sign stripping. Checked in-line rather than assumed: the component identity closes at
      both levels — Space segment 962 − 1,504 = (542); consolidated 7,814 − 7,957 = (143) —
      so every negative read here is confirmed by arithmetic on filed cells, not by the
      server's sign.
  - da_id: DA-30
    chosen_reading: >
      two bases collapsed without a basis field. Applied twice. (1) To the floor: the F5b
      floor is expressible per kg on at least three denominators and the reading is named
      wherever a per-kg floor appears. (2) To the ISSUER'S OWN CLAIMS: the corpus carries a
      ratio ("10x") and a percentage ("99% or more") for the same quantity, with no basis,
      no denominator and no period on either, and they are more than an order of magnitude
      apart (§3.1).
evidence_grade: DEMONSTRATED
key_metrics:
  usd_per_kg_launch_services_revenue_a_prime_prime_d2_customer_payload: 7448
  usd_per_kg_space_segment_revenue_a_prime_d2_customer_payload: 11057
  launch_only_share_of_consolidated_revenue_pct: 8.29
  customer_launch_share_of_total_launches_pct: 26.3
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "SPCX ect1 p.3"
    ticker: SPCX
    citation_id: ect1
    page_no: 3
    url: https://agentii.ai/v/SPCX/ect1/3
    located_via: read_source_pages
  - figure: "SPCX sec7 p.7"
    ticker: SPCX
    citation_id: sec7
    page_no: 7
    url: https://agentii.ai/v/SPCX/sec7/7
    located_via: read_source_pages
  - figure: "SPCX sec8 p.35"
    ticker: SPCX
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "SPCX sec8 p.37"
    ticker: SPCX
    citation_id: sec8
    page_no: 37
    url: https://agentii.ai/v/SPCX/sec8/37
    located_via: read_source_pages
  - figure: "SPCX sec8 p.42"
    ticker: SPCX
    citation_id: sec8
    page_no: 42
    url: https://agentii.ai/v/SPCX/sec8/42
    located_via: read_source_pages
  - figure: "SPCX ect1 p.6"
    ticker: SPCX
    citation_id: ect1
    page_no: 6
    url: https://agentii.ai/v/SPCX/ect1/6
    located_via: read_source_pages
  - figure: "SPCX ect1 p.1"
    ticker: SPCX
    citation_id: ect1
    page_no: 1
    url: https://agentii.ai/v/SPCX/ect1/1
    located_via: read_source_pages
  - figure: "SPCX sec8 p.36"
    ticker: SPCX
    citation_id: sec8
    page_no: 36
    url: https://agentii.ai/v/SPCX/sec8/36
    located_via: read_source_pages
  - figure: "SPCX sec8 p.14"
    ticker: SPCX
    citation_id: sec8
    page_no: 14
    url: https://agentii.ai/v/SPCX/sec8/14
    located_via: read_source_pages
  - figure: "SPCX sec7 p.5"
    ticker: SPCX
    citation_id: sec7
    page_no: 5
    url: https://agentii.ai/v/SPCX/sec7/5
    located_via: read_source_pages
---

# SPCX — Unit Economics Methodology, Q2 2026

**Pillar:** PIL-1 (`003-launch-cost-curve-value-migration`) · **Skill pin:** `e87ee63269a2` ·
**Constitution pin:** 1.5.0 · **Corpus:** `agentii-2026-09-18` · **as_of** 2026-09-19

This artifact supplies the **SPCX rows** of the thesis's vehicle × architecture × basis matrix
(the cross file `_cross/launch-cost-curve.md` is assembled from the per-issuer artifacts; the
entries below are written in that schema's shape, `contracts/launch-cost-curve.yaml`).

It covers tasks **T001–T005** as five sections of one file: **triggers** (§4.1), **defaults**
(§4.2), **methodology** (§4.3), **retrieval-scope** (§4.4), **retrieval-strategy** (§4.5).

---

## The finding

**SPCX gives the thesis exactly one demonstrated price per kilogram to orbit, and it is a
Falcon 9 price. The vehicle the cost curve is actually about has none — and the issuer's two
published cost targets for it disagree by more than an order of magnitude, one of them
landing below that vehicle's own physical propellant floor.**

Four parts, in order of load:

1. **Falcon 9's demonstrated price is `$5,567–7,448/kg` to (unspecified) orbit on the
   matched-pair basis A″ — a 1.34× band across five filed periods.** Both numerator and
   denominator are filed cells from the same population: Launch Services revenue ÷ customer
   payload mass. `DEMONSTRATED` inputs, `MODELED` division. This is the only SPCX figure in
   this artifact that is not either absent or modelled.

2. **That price clears Falcon 9's F5b floor by 2.4×–5.4×, so PIL-1's `wrong_if` does not
   fire at SPCX — but only Falcon 9 was testable.** The F5b recurring-cost floor is
   `$1,379–2,299/kg` on the same denominator. The most adverse pairing (lowest demonstrated
   price `$5,567/kg` against highest floor `$2,299/kg`) still leaves a **2.42× margin**, so
   the negative is not marginal. **Starship's row is `UNEXERCISED`, not `CLEAN`**: it has no
   demonstrated price, so it cannot be counted as passing a test it never faced (§2.4).

3. **The issuer publishes two Starship cost claims that are not the same claim, on the same
   day, with no basis on either.** *"reduce launch costs by 10x compared to our Falcon 9
   rocket"* ([📄 SPCX Q2 2026 call p.3](https://agentii.ai/v/SPCX/ect1/3), `CLAIMED`) versus
   *"reduce the cost to orbit by 99% or more relative to the historical average"*
   ([📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7), `CLAIMED`). One order of magnitude
   versus two, from the same issuer, in the same quarter, in the same corpus. On the
   constitution's own Falcon 9 reference point (`$2,700–2,900/kg` on customer list price,
   §F5b) a 99% reduction lands at **`$27–29/kg` — wholly below F5a's `$46–92/kg` propellant
   floor at the 100 t reference payload**, and clearing it would require **159–317 t of
   payload per flight**. The constitution states the credible Starship band is *"a
   one-order-of-magnitude improvement, not two"* — i.e. **the constitution's own bound
   classifies the issuer's filed 99%+ claim as beyond the credible band**, and the 10× claim
   as inside it. Neither is a curve point.

4. **Starship's contribution to the curve is zero on every basis, by construction.** One
   launch in Q2 2026 — and that one is Flight 12, which the issuer itself describes as
   *suborbital*. Zero customer launches (*"To date, all Starship launches have been
   classified as internal"*, [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35)), therefore
   zero Space revenue, therefore no numerator for A, A′, B or C. **The curve has one plateau
   and no descent.**

> **One sentence for the pillar.** SPCX is a `DEMONSTRATED` **price** on a `MODELED` **cost**
> for a partially reusable vehicle whose floor is proven to be non-binding — and an absence of
> both for the fully reusable vehicle whose floor is the thesis's whole subject.

---

## 1. The DA-01 basis table

### 1.1 The denominator register (DA-02) — SPCX's unspecified orbit

The 10-Q defines its mass metric without naming an orbit: *"Mass to orbit is the total
kilograms of payload that we deploy to orbit in a given period"*, calculated *"by summing
verified mass, including Starlink satellites, customer payloads, and development cargo, from
all successful orbital and flight tests"* ([📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35)).
**"To orbit" is not "to LEO."** The metric pools every destination the fleet flies — LEO,
SSO, GTO, GEO, MEO, lunar and escape — across Falcon 9, Falcon Heavy and Starship together, and
it is not split by vehicle.

**Consequence, stated plainly:** every `$/kg` in this artifact is a `$/kg` **to unspecified
orbit**, thesis-normalised to LEO. Because GTO/GEO missions carry far less mass per launch than
LEO missions, pooling destinations **understates** the LEO-specific price per kg — the error
runs in a known direction, and it is not corrected here because the filing does not permit it.
This is a DA-02 exposure the issuer creates, not one the artifact chooses.

Five denominators are registered, and every `$/kg` below names which one it uses:

| # | Denominator | kg | Derivation | Grade |
|---|---|---|---|---|
| **D1** | Falcon 9 nameplate capacity | 22,800 | **Off-corpus.** `"22.8"` returns **zero pages** in the 10-Q. | `CLAIMED` — **DENOMINATOR-FAILED** |
| **D2** | Realized customer payload per customer launch, Q2 2026 | 8,700 | 87 t ÷ 10 customer launches | `DEMONSTRATED` — the matched pair |
| **D3** | Realized payload per launch, all launches, Q2 2026 | 12,763 | 485 t ÷ 38 launches | `DEMONSTRATED` |
| **D4** | Realized payload per internal launch, Q2 2026 | 14,179 | 397 t ÷ 28 internal launches | `DEMONSTRATED` |
| **D5** | F5a reference payload | 100,000 | constitution §F5a — `MODELED`, no filed source | `CLAIMED` |

D2/D3/D4 reproduce the inherited denominators to the filed tonne (8.70 / 12.76 / 14.18 t) and
are consumed, not re-derived. **D1 is the one 001 used, and it is the one that fails.**

**The pairing rule, applied to the denominator as well as the basis.** A′ and A″ divide
*customer-launch* revenue; B is a *per-launch* cost; C divides *customer-launch* cost. The
numerator and the denominator must be drawn from the same population. This is the
`no_single_basis_collapse` rule turned on the divisor — the defect 002 diagnosed in 001, where
the numerator varied across four bases while the denominator stayed fixed at a single
`CLAIMED` value.

### 1.2 Falcon 9 — `partially_reusable`, floor **F5b**, Q2 2026

All four bases, side by side. Numerator, per-launch, per-kg and grade on every row.

| Basis | Numerator (filed, Q2 2026) | Per customer launch | Per kg @ **D2** (8,700 kg) | Grade |
|---|---|---|---|---|
| **A** — customer list price | **none filed** | **ABSENT** | **ABSENT** | — (§1.4) |
| **A″** — Launch Services revenue ÷ customer launches | $648M ÷ 10 | **$64.8M** | **$7,448/kg** | `DEMONSTRATED` inputs `MODELED` division |
| **A′** — Space segment revenue ÷ customer launches | $962M ÷ 10 | **$96.2M** | **$11,057/kg** | `DEMONSTRATED` inputs `MODELED` division |
| **B** — marginal cost per launch | **none filed** | `MODELED` **$12–20M** | `MODELED` **$1,379–2,299/kg** | `MODELED` |
| **C**(i) — fully-loaded segment cost ÷ customer launches | $1,504M ÷ 10 | **$150.4M** | **$17,287/kg** | `DEMONSTRATED` inputs `MODELED` division |
| **C**(ii) — Space cost of revenue ÷ customer launches | $329M ÷ 10 | **$32.9M** | **$3,782/kg** | `DEMONSTRATED` inputs `MODELED` division |

**The A″ / A′ gap is not noise — it is the non-launch business, quantified.** A″ is 67.4% of
A′ by construction ([📄 SPCX 10-Q p.37](https://agentii.ai/v/SPCX/sec8/37), Launch Services
67.4% of Space revenue), and the difference is **$3,609/kg** of Launch & Development —
spacecraft development and mission services sold to government programmes, recognised
*over time* on a cost-to-cost basis, **not a launch price**. Quoting A′ as "the price of a
Falcon 9 launch" is a DA-21/DA-30 collapse; A″ is the narrower and better-matched basis and is
the one the thesis should carry as **the** demonstrated price.

**Basis A, and why it stays absent.** No filed page states a Falcon 9 list price — `list price`
returns zero pages in the 10-Q. The widely-quoted `~$67M` figure is **off-corpus and
uncitable**, and the `$2,939/kg` built from it divides a `CLAIMED` price by D1, which returns
zero pages in the filing. **It is recordable only as `DENOMINATOR-FAILED`.** On D2 it
recomputes to `~$7,701/kg` — a `MODELED` figure with a `CLAIMED` numerator and a filed
denominator, and **not** an improvement on A″. The matched pair supersedes it.

**Cross-period band, basis A″ (the value this artifact carries forward):**

| | Q2 2026 | Q1 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---|---|---|---|---|
| Launch Services revenue ($M) | 648 | 330 | 490 | 978 | 1,056 |
| Customer launches (#) | 10 | 7 | 9 | 17 | 21 |
| Customer payload (t) | 87 | 45 | 88 | 132 | 163 |
| **A″ per customer launch** | **$64.8M** | $47.1M | $54.4M | $57.5M | $50.3M |
| **A″ per kg @ D2** | **$7,448/kg** | $7,333/kg | **$5,567/kg** | $7,409/kg | $6,479/kg |

**Band: `$5,567–7,448/kg` — 1.34×.** Recomputed here from the filed cells; 002's published
points agree to ≤`$5/kg` (Q1 2026 `$7,332`, H1 2026 `$7,414`, H1 2025 `$6,481`), the
difference being rounding of metric-ton figures the issuer files to the nearest tonne. **Test a
band, not a point.**

Also: the realized price moves **$47.1M–64.8M per customer launch across five quarters**, so
`"$67M per launch"` is not a stable descriptor of a Falcon 9 mission — the Q2 figure is the
high end, and the issuer attributes it to *"a favorable customer mix shift"*
([📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42)). §3.2 uses that phrase against a
different claim.

### 1.3 Starship — `fully_reusable` (declared) and `fully_expendable` (as flown)

Carried on two architecture rows, because the declared and the demonstrated architecture
differ and DA-03 forbids collapsing them. `floor_architecture_consistency` maps F5a to
`fully_reusable` and F5c to `fully_expendable`; both apply, to different rows.

| Basis | Numerator (filed, Q2 2026) | Per launch | Per kg | Grade |
|---|---|---|---|---|
| **A** — list price | none exists | **ABSENT** | **ABSENT** | — |
| **A′** / **A″** — revenue per customer launch | $0 revenue; 0 customer launches | **ABSENT** | **ABSENT** | — |
| **B** — marginal cost | none filed | **ABSENT** | **ABSENT** | — |
| **C** — fully-loaded | none filed | **ABSENT** | **ABSENT** | — |

**Every basis is absent, and the reason is structural, not a retrieval failure.** Starship
produced one launch in Q2 2026, zero customer launches, and therefore zero revenue. The
absence is a *design property of the CUSTOMER boundary* (§2.5), not a gap the search failed to
close. **A vehicle with no customer launch has no price; a vehicle in development has no
marginal cost; the two absences are not evidence about each other.**

The only filed Starship payload datapoint is a **count**: Flight 13 deployed *"20 production V3
satellites"* ([📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7)). No satellite mass is
disclosed, so the count **cannot be converted to tonnes on this platform** — inherited from
002 as a blocked conversion, not re-attempted, and not a failed search.

Nor are the F5a inputs sourced: **4,600 t of propellant and $1–2/kg appear in no SPCX filing.**
`propellant` returns **zero pages** in the 10-Q and in the 8-K; its only appearance in the whole
corpus is qualitative — *"propellant transfer in orbit is critical"*
([📄 SPCX Q2 2026 call p.6](https://agentii.ai/v/SPCX/ect1/6)). The constitution's F5a
parameters are **exogenous `MODELED` values**, and the artifact says so rather than citing a
filing that does not contain them.

### 1.4 Absent cells, each with its resolving source

An absent cell is named with what would fill it. An unnameable gap is indistinguishable from
an unsearched one.

| Vehicle | Basis | Reason | Resolving source | Class |
|---|---|---|---|---|
| Falcon 9 | **A** | No filed list price; `list price` → 0 pages in the 10-Q. The `~$67M` figure is off-corpus and the `$2,939/kg` built on it divides by D1, which returns 0 pages. | SpaceX's published price schedule, or a customer contract with a disclosed value filed with the SEC | `UNRESOLVABLE-FROM-PLATFORM` |
| Falcon 9 | **B** | No marginal cost disclosed; `marginal cost` → 0 pages in the 10-Q. | **NASA CRS / Commercial Crew contract values as a revealed-price floor** (named per 002 §5.1) — see §1.5 | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Falcon 9 | **payload_kg** (rated) | No rated capacity in any filed page; `payload capacity` → 0 pages in the 8-K. | SpaceX Falcon 9 payload user guide (off-platform) | `UNRESOLVABLE-FROM-PLATFORM` |
| Falcon 9 | **D3/D4 split by vehicle** | The mass metric is not split by vehicle, so Falcon and Starship mass cannot be separated. | A vehicle-level mass-to-orbit disclosure | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Falcon Heavy | **all bases, launch count** | Falcon Heavy launches are pooled inside "Falcon launches"; no separate count, price or payload. | A separate Heavy disclosure | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Falcon 9 / Starship | **C, depreciation component** | Cost of revenue includes *"depreciation (inclusive of booster, Merlin engine, and fairing depreciation)"* with **no amount**; segment D&A is $158M undifferentiated. | A segment D&A breakdown, or a property-class depreciation schedule by segment | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Starship | **A, A′, B, C** | Zero revenue and zero customer launches by construction (all Starship launches are internal). | The first Starship contract with a disclosed value — i.e. the first Starship **customer launch**. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Starship | **payload_kg** | No Starship capacity in any filing; the call gives only a relative *"quadruple payload capacity"*. | A Starship payload user guide, or a filing stating capacity | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Starship | **F5a inputs** | 4,600 t and $1–2/kg appear in no SPCX filing. | None filed. The constitution's F5a parameters are exogenous `MODELED` values and are inherited as such. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |

*One absence is recorded but not named as a cell above, because the answer is recoverable:* the
**first-stage share of the $329M cost of revenue**. Not filed. See §3.3 for why it matters and
what it changes.

### 1.5 Basis B and the 002 §5.1 disposition — inherited, not re-litigated

002's validation ledger registers **"SPCX unit-economics"** among nine items classified
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` (`_cross/validation-ledger.md` §5.1), and the brief carries
that disposition forward. **This artifact records it rather than overrides it, and names the
resolving source as instructed: NASA CRS and Commercial Crew contract values as a
revealed-price floor.**

Two precisions on that naming, because the class does real work here:

1. **What NASA contract values actually resolve is a PRICE, not a COST.** A contract value is
   what a sophisticated, repeat, price-insensitive customer paid. It adds a second price point
   under basis A — government versus commercial — and it is the only route to splitting the
   `$64.8M` blended A″ into its components. It bounds a marginal cost only weakly and
   indirectly: if a customer pays `$X` and the seller accepts, cost is below `$X`, which is not
   a disclosure and does not satisfy `basis_b_grade`.
2. **On this corpus it is also unreachable, and that is a separate finding.** `NASA` returns
   **zero pages** in both the 10-Q and the earnings call; the SPCX corpus on this platform is
   ten documents (8-Ks, one 10-Q, one transcript) carrying **no contract-value source at all**;
   and the one tool call attempted against the class —
   `search_unified(SPCX, "NASA contract")` — returned
   **`INTERNAL_ERROR: invalid input syntax for type json`**. So the class is
   `UNRESOLVABLE-FROM-PUBLIC-SOURCES` **as to the datum** (it exists publicly and is not
   disclosed by the issuer) and independently `UNRESOLVABLE-FROM-PLATFORM` **as to reach**
   (the corpus does not carry it and the composition tool errors). **The two readings are
   reported together and not collapsed; the frontmatter carries the primary class, which is
   002's.**

**Basis B as carried: `MODELED`, `$12–20M` per launch.** Components, all from constitution
§F5b (an authority at the pin, not a platform source, and therefore not URL-citable — the
citation contract admits only `agentii.ai` URLs):

| Component | Value | Share of the component sum ($11–20M) |
|---|---|---|
| Expended second stage (manufacturing) | $8–12M | **60–73%** — dominant |
| Range and launch operations | $2–5M | 18–25% |
| Booster refurbishment | $1–3M | 9–15% |
| Propellant — 485 t RP-1/LOX at ~$0.75/kg | **~$0.36M** | **1.8–3.3%** |
| **Sum** | **~$11.4–20.4M** | registered band `$12–20M` |

**Basis B is `MODELED` and under P4 a `MODELED` input can never satisfy a falsifier.** That is
the single most important sentence in this section: it is why §2.4's negative verdict on
PIL-1's `wrong_if` is a statement about the *price* row only.

---

## 2. The F5 floor, applied per architecture

### 2.1 The mapping, stated before the values

`floor_architecture_consistency` maps one-to-one: **F5a → `fully_reusable`**, **F5b →
`partially_reusable`**, **F5c → `fully_expendable`**. The tiers are **exhaustive**. `tier: none`
is admissible only where the architecture is itself undetermined, and no SPCX vehicle's
architecture is undetermined — so no SPCX row carries `none`.

| Vehicle | Architecture (DA-03 label) | Applied tier | Floor value | Grade |
|---|---|---|---|---|
| Falcon 9 | `partially_reusable` | **F5b** | `$1,379–2,299/kg` @ D2 (`$12–20M`/launch) | `MODELED` |
| Starship — as flown | `fully_expendable` | **F5c** | no numeric value registered | `MODELED` |
| Starship — declared target | `fully_reusable` | **F5a** | **`$46.00/kg`** (band `$46–92/kg` @ D5; `$31–61/kg` @ 150 t) | `MODELED` |

**The registered inversion is not re-raised here.** F5 as originally written bounded only the
two reusable architectures; the sector's only `DEMONSTRATED` price belongs to an expendable
vehicle. That inversion — demonstrated data on the unbounded architecture, modelled bounds on
the undemonstrated one — is registered in the constitution's own §F5c and the coverage gap is
**closed**. This artifact consumes it. (The inversion bears on the *universe* row — Electron,
`001:PIL-1` / `003:PIL-4` — not on SPCX, whose only demonstrated price sits on a
**partially** reusable vehicle.)

### 2.2 F5b, applied to Falcon 9 — and the category error it prevents

F5b's derivation, shown rather than asserted (P4 rule 3), at D2:

```
propellant   = 485 t × $0.75/kg              = ~$0.36M   =  1.8–3.3% of marginal cost
floor(low)   = $12M  ÷ 8,700 kg  (D2)        = $1,379/kg
floor(high)  = $20M  ÷ 8,700 kg  (D2)        = $2,299/kg
```

**Propellant is ~2–3% of a Falcon-class marginal cost, because 98% of the vehicle comes back.**
The dominant unrecoverable term is the expended second stage ($8–12M, 60–73% of the component
sum). The floor is therefore a **manufacturing** cost curve — **soft**, because it yields to
production learning, where F5a is **hard** because it yields only to physics.

> ⚠️ **Applying F5a's `$46–92/kg` to a Falcon-class vehicle is a category error** and would
> understate the vehicle's achievable price by an order of magnitude. F5a's floor is
> `$4.6–9.2M` per flight of *propellant alone* — **12×–26× Falcon 9's entire propellant bill**
> (`$0.36M`), on a vehicle whose propellant is 2–3% of cost rather than ~100%. **Measure which
> floor applies by asking what is *expended* on each flight.** On Falcon 9: the second stage.
> On Starship, if the catch succeeds: the propellant.

The constitution's F5b reference point — *"Falcon 9 reusable is roughly `$2,700–2,900/kg` to
LEO on customer list price"* — is **denominator-exposed on D1** and is not used as a value
here. The matched-pair band `$5,567–7,448/kg` is the filed replacement; the constitution
figure is retained only because §3.1 needs it as a *reference point for the issuer's own
claims*, which the issuer evidently also uses.

### 2.3 F5a, applied to Starship — a floor nothing is demonstrated against

```
floor = 4,600 t × $1–2/kg  =  $4.6–9.2M per flight
      ÷ 100 t (D5)         =  $46–92/kg
      ÷ 150 t              =  $31–61/kg
```

`$46.00/kg` is the registered value; the band is `$46–92/kg`. Two properties of this row are
load-bearing and are stated rather than implied:

- **The floor is a quotient of two `MODELED`/`CLAIMED` inputs.** 002 §5 already withdrew the
  row's confidence on this ground: the numerator is a constitution estimate and the
  denominator (100 t) is an unfiled company figure on a vehicle with **zero demonstrated
  orbital payload**. A curve built on `$46–92/kg` is a model divided by a claim. **`MODELED`
  never satisfies a falsifier**, so the F5a row cannot falsify anything and cannot be falsified
  by anything in this corpus.
- **Nothing is demonstrated on the other side of it.** Zero revenue, zero customer launches,
  no filed cost. **The F5a row is `UNEXERCISED`** — see §2.4.

### 2.4 F5c, and PIL-1's `wrong_if` run to a verdict

**F5c, Starship as flown.** No ship catch has occurred; Flight 13's terminal event was the
*"softest ever splashdown of Starship"* ([📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7)),
and Musk targets a catch of *"the first and the second stage"* this year with *"the ship as soon
as the next flight"* ([📄 SPCX Q2 2026 call p.1](https://agentii.ai/v/SPCX/ect1/1), `CLAIMED`).
As of the corpus date, **both stages are expended on every Starship flight**, so the as-flown
architecture is `fully_expendable` and **F5c** applies. The constitution registers **no numeric
value** for F5c — it is the tier of the universe's only `DEMONSTRATED` price, not a numeric
floor — so `applied_floor.value` is legitimately absent for this row. There is likewise no
per-unit Starship vehicle cost: the vehicle's manufacturing cost sits undivided inside Space
R&D, which is **$1,076M in the quarter** ([📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42)).

**PIL-1's `wrong_if`, evaluated:**

```
metric   = count_of_universe_vehicles_with_a_demonstrated_price_per_kg_to_LEO
           _below_their_architecture_applied_launch_cost_floor
threshold= 0
op       = >
```

| Vehicle | Demonstrated price/kg to orbit | Applied floor | Position | Testable? |
|---|---|---|---|---|
| Falcon 9 | **$5,567–7,448/kg** (A″ @ D2) | F5b `$1,379–2,299/kg` | price **2.42×–5.40×** the floor | **Yes — does not fire** |
| Starship | none — no customer launch | F5a `$46–92/kg` | **no price exists to compare** | **No — `UNEXERCISED`** |

**Verdict: the count is 0, and for two different reasons that must not be merged.** For Falcon 9
the count is 0 because the price clears the floor, on a **2.42× margin at the most adverse
pairing** — a robust negative, not a marginal one. For Starship the count is 0 because **no
numerator exists at all**. `003:PIL-1`'s `wrong_if` therefore **does not fire at SPCX**, and the
honest scope of that result is *one of the thesis's vehicles was testable and passed; the
other was not tested.*

> **PRESENCE ≠ ABSENCE.** A vehicle with no demonstrated price is not a vehicle that cleared
> its floor. **Starship is `UNEXERCISED`, not `CLEAN`** — an unengaged check is not a passed
> check, and this is the single easiest place in the thesis to make that error.

**Note the contrast with `002:PIL-1`, namespaced because the identifiers collide.** 002's
`wrong_if` was the *denominator* falsifier (`abs_pct_change_..._after_denominator_validation`,
`threshold=0.15`) and it **FIRED**: the realized denominator moved every demonstrated $/kg by
+79% to +162%, 5.3–10.8× the tolerance. 003's is the *floor* falsifier and it does not fire.
**One thesis falsified the divisor; this one finds the level, once the divisor is fixed,
comfortably above the floor.** Both are true; neither is evidence about the other.

### 2.5 The CUSTOMER boundary (DA-21) — verbatim, and what it does to every per-launch figure

The issuer states its own segment boundary in one sentence, and it is the single most
consequential definition in this artifact:

> **"Our Space segment revenue only reflects our customer launches and customer activities."**
> — [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35)

And the mechanism, filed verbatim, which makes the boundary a *cost* boundary and not only a
revenue one:

> **"For launches of our Starlink satellites, the Company does not recognize any inter-segment
> revenue, rather those launch costs are capitalized in satellites in Property, plant, and
> equipment, net."** — [📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36)

**Consequences, each of which changes a number:**

1. **~74% of launches produce no Space revenue by design.** Q2 2026: **10 customer launches of
   38 total = 26.3%**, so **73.7%** of launches are internal. H1 2026: 17 of 78 = 21.8%.
   *"We allocate a significant amount of launch capacity to our Connectivity segment, and
   expect to allocate a significant amount to our AI segment in the future"* (p.36).
2. **The 10-Q's own Key Business Metrics section says why the metrics outrun the revenue**:
   *"Mass to orbit and launches generally grow more rapidly than Space segment revenue because
   these metrics include our internal constellation deployments from which we do not recognize
   inter-segment revenue"* (p.35). The divergence is **definitional, not operational** — the
   filed explanation for the whole A1b fact pattern, in the issuer's own words.
3. **It is the fix for the denominator problem.** Space cost of revenue is the *customer-launch*
   cost base, because the Starlink launches' costs leave the segment at capitalisation. So the
   comparable denominator for cost of revenue is the **customer launch count**, not the total —
   which is why C(ii) above pairs $329M with 10 and not with 38 (§3.3).
4. **Space ≠ launch.** Space revenue is 12.3% of consolidated revenue ($962M ÷ $7,814M) and
   **launch-only is 8.29%** ($648M ÷ $7,814M). Those are two different claims sharing one
   number, and neither is a "launch share" of the company on any other reading. Within Space,
   **32.6% is Launch & Development** — a development-services business, not a launch business.
   *"12.3%" is not one thing.*
5. **It is why Starship's row is empty.** All Starship launches are internal
   ([📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35)), therefore no Starship revenue,
   therefore no Starship price — structurally, permanently, until a Starship customer exists.

---

## 3. Findings not in the inherited baseline

Reported because each changes a figure or a verdict that a downstream thesis would otherwise
inherit wrong.

### 3.1 The issuer's two Starship cost claims are not the same claim — and one is below the floor

Both are `CLAIMED`, both are filed in the same corpus, both published **2026-08-04**:

| Claim | Wording | Where | Grade |
|---|---|---|---|
| **~10×** | *"Starship aims to quadruple payload capacity and **reduce launch costs by 10x** compared to our Falcon 9 rocket"* | [📄 SPCX Q2 2026 call p.3](https://agentii.ai/v/SPCX/ect1/3) | `CLAIMED` |
| **~99%+** | *"reduce the cost to orbit by **99% or more** relative to the historical average"* | [📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7) | `CLAIMED` |

**These differ by more than an order of magnitude, and each carries a DA-30 collapse inside its
own definition.** The 10× claim gives **a ratio with no basis** — 10× against what? cost or
price? per launch or per kg? The 99% claim gives **a percentage with no reference value** — the
"historical average" of what, and over what window? Neither names a denominator; neither names
a period. They cannot both describe the same quantity, and the issuer does not say which
quantity it means.

**Tested against the constitution's own reference point**, and this is the part that matters:
F5b records *"Falcon 9 reusable is roughly `$2,700–2,900/kg` to LEO on customer list price"* and
states the credible Starship band is **"a one-order-of-magnitude improvement, not two."**

| Reading | Applied to | Result | vs F5a floor `$46–92/kg` @ D5 |
|---|---|---|---|
| **10×** (one order) | $2,700–2,900/kg | **$270–290/kg** | clears it 2.9×–6.3× ✓ |
| **99%+** (two orders) | $2,700–2,900/kg | **$27–29/kg** | **wholly below it** ✗ |
| 99%+ | matched pair $5,567–7,448/kg | $55.67–74.48/kg | straddles (002 §6a) |

**So the constitution's own bound classifies one of the issuer's filed claims as inside the
credible band and the other as outside it** — and the outside one, taken at face value, requires
**159–317 t of payload per flight** to clear the propellant floor (at $1–2/kg propellant),
i.e. **1.6×–3.2× the F5a reference payload**. Against the matched-pair realized basis it
requires **83–165 t**. Either way it clears the floor **only on a payload the issuer has never
filed**.

**Verdict: neither claim is admissible as a curve point, and the pair is not a range — it is a
contradiction.** Recorded `CLAIMED`. The correct downstream use is as PIL-3's raw material: this
is what the sector's cost conversation looks like when nothing is measured, and it is why the
thesis's curve is `CLAIMED` rather than `DEMONSTRATED`.

*Two renderings of the 99% sentence appear on the same page* — *"which is expected to reduce"*
in one block and *"which we believe will reduce"* in the other. Both are forward-looking; the
modality difference does not change the grade, and is recorded so a downstream reader who sees
the other wording knows it is the same claim.

### 3.2 The CEO's uniform-price claim contradicts the issuer's filed mix-shift language

**`CLAIMED`, and it conflicts with a `DEMONSTRATED` statement in the same corpus.** Musk:
*"we launched competing satellite constellations at fair prices, **the same price we charge
everyone**"* ([📄 SPCX Q2 2026 call p.1](https://agentii.ai/v/SPCX/ect1/1)).

Against it, the 10-Q: Q2 2026 Launch Services revenue rose **$158M** on a customer-launch count
that rose from 9 to 10. Per customer launch that is **$54.4M → $64.8M, +19.0%**, against a
**+11.1%** increase in launch count — and the issuer's attribution is *"**a favorable customer
mix shift**"* ([📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42); the 8-K says *"a favorable
customer shift"*, [p.7](https://agentii.ai/v/SPCX/sec7/7)).

**A mix shift cannot move revenue per launch if the price is uniform.** The filed sentence is
only coherent if price varies by customer or mission — which is also what the five-quarter
A″ range (`$47.1M–64.8M`, a **1.37×** spread on a *price*) shows directly. **The CEO's claim is
false as stated, or "price" means something narrower than a mission price.** This matters
because a uniform-price assumption is exactly what makes a single-point `$/kg` defensible, and
this issuer's own filings do not support one. *(The phrase does not appear in any 001 or 002
artifact — verified by search — so it is raised here for the first time.)*

### 3.3 The Space cost-of-revenue paradox, and its resolution

Read Space cost of revenue the obvious way and it contradicts the F5b floor:

| Reading | Value | Tension |
|---|---|---|
| $329M ÷ **38** total launches | **$8.66M** /launch | **below** F5b's `$12–20M` marginal band — impossible if CoR is fully loaded and includes depreciation |
| $329M ÷ **37** Falcon launches | **$8.89M** /launch | same |
| $329M ÷ **10** customer launches | **$32.9M** /launch | **above** it — and consistent |

**The resolution is the §2.5 capitalisation sentence.** Space cost of revenue is described as
*"second stages flown related to the Company's Falcon 9 and Falcon Heavy launches, launch
operations and overhead, depreciation (inclusive of booster, Merlin engine, and fairing
depreciation), employee compensation..., launch testing and overhead, engineering costs,
inventory excess and obsolescence, shared costs incurred in the production of launch hardware,
and ongoing product support"* ([📄 SPCX 10-Q p.37](https://agentii.ai/v/SPCX/sec8/37)). With
Starlink launch costs capitalised to satellites and Starship test flights expensed to R&D
(*"Space segment's R&D expenses mainly relate to the development, build, and testing of
Starship"*, p.37), **the cost of revenue is predominantly the cost of the customer-launch
business**, so the customer-launch denominator is the population-matched one and the
`$32.9M` reading is the comparable figure. The reading is graded honestly: the **mechanism** is
`DEMONSTRATED` (all three legs — capitalisation, R&D attribution, point-in-time recognition —
are filed verbatim), the **allocation of "launch operations and overhead" across 38 launches**
is `MODELED`.

**This also discharges an open question 002 left standing.** 002 §8 item 6 recorded the
internal-launch capitalisation mechanism as *"widel[y] believed true of Starlink and **not
asserted here**: it appears in no filed text this artifact could locate"*, and handed it
forward as *"an open question for P3, not as a finding."* **It is filed verbatim**, at
[📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36): *"those launch costs are capitalized in
satellites in Property, plant, and equipment, net."* 002's `capitaliz*` sweep did not surface
it; a direct page read did. **002 §8 item 6 is corrected, the open question is closed, and the
finding is upgraded from "widely believed" to `DEMONSTRATED`** — and it is load-bearing, because
it is what makes §3.3's resolution work. *(The retrieval difference is recorded in §4.5: the
sweep and the read disagree, and on this instrument the read is authoritative.)*

### 3.4 The Q2 2026 Starship "launch" is suborbital (DA-08)

The 8-K reports **one Starship launch** in Q2 2026 and describes Flight 12 as *"Starship V3's
**first suborbital mission**"*, completed in May; Flight 13 followed *"subsequent to the second
quarter"* in July ([📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7)). The filing's own
definition includes *"all successful orbital **and flight tests**"*
([📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35)). **Therefore the Starship launch count
for the quarter contains zero orbital launches**, and the mass metric pools them. Musk confirms
the state of play: Flight 13 demonstrated capabilities *"necessary to achieve an orbital
mission"* and Flight 14 *"will be our first flight to fly our Version 3 Starlink satellites...
**to operational orbit**"* ([📄 SPCX Q2 2026 call p.1](https://agentii.ai/v/SPCX/ect1/1)).

**Why it matters here:** a "launch count" that includes suborbital flight tests cannot be a
denominator for an orbital cost, and Starship's payload-to-orbit contribution is not
established by its launch count. Whether Flight 12's deployed satellites sit inside the 485 t
is **not disclosed** — inherited from 002 as a `DA-07` ambiguity, not resolved here.

### 3.5 The component identity closes, so the signs are confirmed (DA-23)

Run rather than assumed, at both levels, before any negative was read:

| Level | Revenue | − Costs | = Computed | Filed "Loss from operations" |
|---|---|---|---|---|
| Space segment (Q2 2026) | $962M | $1,504M | **$(542)M** | **$(542)M** ✓ |
| Consolidated (Q2 2026) | $7,814M | $7,957M | **$(143)M** | **$(143)M** ✓ |

The Space segment's `Costs and expenses` block is the opex definition used (cost of revenue
$329M + R&D $1,076M + SG&A $99M + impairment $0 = $1,504M); the consolidated block is cost of
revenue $3,495M + R&D $3,548M + SG&A $912M + restructuring $2M = $7,957M. **Both close.** DA-23
`|x|` stripping would leave a component identity that fails to close, and neither does. The
signs carried in this artifact are therefore **confirmed by arithmetic on filed cells**, not
taken from the served value. *(The same identity is the reason the `-0.3%` cost-of-revenue
movement at p.42 is read as a genuine decrease: $330M → $329M.)*

---

## 4. The five modes

### 4.1 Triggers — what would overturn this

Ranked by what they would change, with the falsifier each engages.

| # | Trigger | Effect | Falsifier engaged |
|---|---|---|---|
| **T-1** | **A Starship customer launch**, at a disclosed price | Converts every Starship basis from `ABSENT` to populated — the first real test of F5a | `003:PIL-1`'s `wrong_if` becomes **exercisable** for the first time |
| **T-2** | **A filed Starship payload mass ≥ 159 t** | Rescues the "99% or more" claim from below the F5a floor at the list-price anchor; below that the claim stands falsified against F5a | F5a row |
| **T-3** | **A demonstrated Falcon 9 price below `$1,379/kg`** (A″ @ D2) | Flips the `wrong_if` count to 1 — the price row would sit below its own architecture's floor | `003:PIL-1` |
| **T-4** | **Space cost of revenue rising with total launches rather than customer launches** | Breaks §3.3's resolution; means CoR is not the customer-launch cost base and the `$32.9M` reading is wrong | §3.3 |
| **T-5** | **A disclosed Falcon 9 list price** | Populates basis A and permits the A/A″ discount test directly | `basis_named` |
| **T-6** | **`propellant` or `second stage` cost appearing in a filing** | Converts basis B from `MODELED` toward `DEMONSTRATED` — the universe's second demonstrated cost, after Electron | `basis_b_grade` |
| **T-7** | **A ship catch demonstrated on a flight with disclosed payload** | Moves Starship from the `fully_expendable` row to the `fully_reusable` row *on evidence*, not on declaration | DA-03 |
| **T-8** | **A disclosed vehicle-level mass split** | Separates Falcon from Starship mass and makes D3/D4 vehicle-specific | DA-07 |
| **T-9** | **The realized price band (A″) leaving `$5,567–7,448/kg`** | The demonstrated price is period-sensitive (1.34× across five quarters); a sixth period outside the band re-opens the band, not the level | §1.2 |

**What would NOT overturn it, and is recorded so it is not mistaken for a trigger:** the
**F5 coverage gap**. That was closed at constitution v1.3.0 by the three-way split and the
thesis pins 1.5.0. **Do not re-raise it.** Likewise, the *inversion* — demonstrated price on
the expendable architecture, modelled bounds on the reusable one — is a registered finding, not
a gap.

### 4.2 Defaults — assumptions used where no filed figure exists

Each default is named, graded, and given the direction of its likely error.

| # | Default | Value | Grade | Why, and which way it leans |
|---|---|---|---|---|
| **D-1** | Denominator for A′/A″/C | **D2, 8,700 kg** (realized customer payload per customer launch) | `DEMONSTRATED` | Chosen because numerator and denominator come from the same population. The alternative readings raise `$/kg` by 1.47× (D3) to 1.63× (D4) — so **D2 is the conservative end** |
| **D-2** | Basis B marginal cost | **$12–20M/launch** | `MODELED` | Inherited from constitution §F5b; components sum to $11.4–20.4M. A `MODELED` input **cannot satisfy a falsifier**; its use here is to bound, not to test |
| **D-3** | Falcon 9 propellant price | **~$0.75/kg** | `MODELED` | F5b's own parameter, absent from every SPCX filing. At $1.50/kg propellant is still only ~4–7% of marginal cost — **the category error is robust to a 2× error in this default** |
| **D-4** | Starship propellant | **4,600 t at $1–2/kg** | `MODELED` | Exogenous. The floor's denominator (100 t) is `CLAIMED` and unfiled (002 §5) |
| **D-5** | Orbit for every `$/kg` | **LEO, thesis-normalised** | `MODELED` | The issuer **names no orbit**. Because non-LEO missions carry less mass, pooling **understates** LEO `$/kg` — the default is conservative in the same direction as D-1 |
| **D-6** | Attaching Space cost of revenue to customer launches | **10, not 38** | `MODELED` on allocation, `DEMONSTRATED` on mechanism | §3.3. If wrong, cost per launch is $8.66M rather than $32.9M — and then F5b's `$12–20M` is overstated, not understated |
| **D-7** | Starship's architecture as flown | **`fully_expendable`** | `DEMONSTRATED` | No catch has occurred; Flight 13 splashed down. Not a default at all — recorded here so the reader can see which rows carry one and which do not |

**Defaults that are explicitly refused**, because the thesis's own rule forbids them:

- **No proxy for basis A.** The `~$67M` figure is off-corpus; the artifact does not import it as
  a price. An imported number with a failed denominator is worse than a named absence.
- **No sub-`$10/kg` input.** Constitution §F5a: *"any claim of sub-$10/kg to LEO is below the
  propellant floor... Treat sub-$10/kg as a marketing figure, not an input."* §3.1's `$27–29/kg`
  reading is reported as a **claim under test**, never as a value.
- **No single-basis `$/kg`.** Every figure above names its basis *and* its denominator.
- **No `tier: none`.** Every SPCX vehicle's architecture is determinable, so every row carries a
  tier.

### 4.3 Methodology — the derivation path, stated so it reproduces

```
STEP 1  Locate the denominator before the numerator.
        10-Q p.35 → Mass to Orbit and Launches definitions, both tables.
        Note the orbit is NOT named .......................... DA-02 exposure, recorded
        Read BOTH number sets (8-K p.7 gives 5 periods; 10-Q p.35 gives 4).

STEP 2  Establish the boundary before dividing anything.
        10-Q p.35 → "Our Space segment revenue only reflects our customer launches
                     and customer activities."
        10-Q p.36 → internal launch costs capitalised to satellites.
        ⇒ numerator population = CUSTOMER. Denominator population = CUSTOMER.
        ⇒ 26.3% of launches (10/38) carry the revenue; 73.7% carry none.

STEP 3  Numerator, three readings, all filed:
        A″ = Launch Services revenue   (8-K p.7)  ÷ customer launches   = $64.8M
        A′ = Space segment revenue     (8-K p.7)  ÷ customer launches   = $96.2M
        C  = Space total costs         (8-K p.7)  ÷ customer launches   = $150.4M
             Space cost of revenue    (8-K p.7)  ÷ customer launches   = $32.9M
        A  = NOT SOURCED. Stop. Record absent + resolving source.

STEP 4  Divide, and STATE THE DENOMINATOR ON EVERY LINE.
        A″ ÷ 8,700 kg = $7,448/kg      A′ ÷ 8,700 kg = $11,057/kg
        C  ÷ 8,700 kg = $17,287/kg     C(ii) ÷ 8,700 kg = $3,782/kg
        Recompute all five periods and report the BAND, not the point.
        Reconcile to 002's published points; explain any residual (rounding, ≤$5/kg).

STEP 5  Apply the floor BY ARCHITECTURE.
        Falcon 9 partially_reusable → F5b → $12–20M/launch → $1,379–2,299/kg @ D2
        Starship fully_reusable    → F5a → $46–92/kg @ 100 t
        Starship fully_expendable  → F5c → no registered value
        NEVER apply F5a to Falcon 9 (category error, §2.2).

STEP 6  Run the falsifier, and report the COUNT and its SCOPE.
        Compare like-for-like: demonstrated price vs the floor of ITS OWN architecture.
        Report per-vehicle whether the test was testable.
        Starship = UNEXERCISED. Do not report it as passing.

STEP 7  Check the sign by component identity before reading any negative. (§3.5)
```

**Reproducibility check.** Every figure in §1.2 is a quotient of two integers on a filed page,
and every page is cited. A reader with the URLs can reproduce the entire table without the
platform: 648/10, 962/10, 1,504/10, 329/10, then each ÷ 8.7, and 87/10 for the denominator.
**Nothing in the DA-01 table depends on a `MODELED` input except basis B.**

### 4.4 Retrieval scope — what is admitted, what is excluded

**Admitted:**

| Source | Why |
|---|---|
| 10-Q Q2 2026 (`sec8`, accession `0001628280-26-052535`, filed 2026-08-04) | The audited-period primary source. Segment note, Key Business Metrics, MD&A |
| 8-K Ex. 99.1 earnings release (`sec7`, accession `0001628280-26-052515`, filed 2026-08-04) | The **five-period** Space segment table — the only place the Q1 2026 and H1 2025 splits exist |
| Q2 2026 earnings call transcript (`ect1`, 2026-08-04) | Preparatory only. Every figure drawn from it is graded `CLAIMED` and is never a curve input |
| constitution.md §F5a/§F5b/§F5c at pin 1.5.0 | The floor parameters. A pin-level authority, **not URL-citable** — the citation contract admits only `agentii.ai` URLs |
| 001 and 002 SPCX unit-economics artifacts | Inherited denominators and the §5.1 disposition. Consumed, not re-derived |

**Excluded, with reason:**

| Source | Why excluded |
|---|---|
| `sec9` — 8-K filed 2026-08-14 (Cursor/Anysphere merger, 96 pages) | **Launch-irrelevant.** A capital-markets and AI-segment event; carries no vehicle, cost or launch disclosure |
| SpaceX corporate channels, published price schedules, user guides | **Off-platform.** Real and free, but inadmissible — the citation contract admits only `agentii.ai` URLs. Named as *resolving sources* for absent cells, never cited as evidence |
| NASA contract awards, NASA OIG cost reports, CRS/Commercial Crew values | **Not carried by this corpus** (`NASA` → 0 pages in the 10-Q and in the call) and the one composition query against the class errored. Named as the resolving source for basis B (§1.5) |
| The metrics block / `get_segment_data` / `data_freshness` | **Unusable.** `get_segment_data` errors (`column "k" does not exist`) and double-counts; `data_freshness` reports **2027-04-12**. DA-23/26/27 live in the extracted layer. **Pages were read directly** |
| Linkbase `LABEL` values | **Stale and figure-bearing** (hard rule 6). No figure here is sourced from a label |
| Third-party market-research $/kg figures | Not `agentii.ai`, and mostly unauditable. The thesis's correction to RKLB (published `$/kg` **1.79×–2.62× too low, four of four periods**) is the standing reason not to inherit a `$/kg` from anywhere |

**In scope and found absent** — these are results, not omissions: no list price, no marginal
cost, no per-launch price, no propellant mass or price, no rated payload capacity, no Falcon
Heavy count, no vehicle-level mass split, no depreciation amount inside cost of revenue, no
Starship revenue of any kind. Each is carried as a named absence with a resolving source in
§1.4.

### 4.5 Retrieval strategy — how the sources were located, so the search repeats

**Layer order, and why it was not the obvious one.**

1. `search_documents(SPCX)` → 10 corpus documents, each with a resolved `citation_id`. Recorded
   up front because it bounds every negative below: **five are 8-Ks and only one is a 10-Q.**
   A negative finding at SPCX is a statement about *this* ten-document corpus.
2. `read_source_outline` on `sec8` (55 pages) → the segment note, Key Business Metrics and MD&A
   page ranges. `read_source_outline` on `sec7` → located **p.7**, the five-period Space table —
   the single highest-value page in the corpus, and one the 10-Q does not contain.
3. `search_keyword_in_source` for **`propellant`, `22.8`, `expendable`, `marginal cost`,
   `list price`, `second stage`, `NASA`, `Falcon 9`, `Dragon`, `payload capacity`** across
   `sec8`, `sec7` and `ect1`. **Zero-hit results are the load-bearing half** — they are what
   converts "I did not see a marginal cost" into "the token does not occur in the filing".
4. `read_source_pages` on every page promoted out of steps 2–3, **before** any figure was
   written down. Direct page reads, not the metrics block.

**Three instrument hazards, each of which changed how a result was read.**

- **`search_keyword_in_source` is not a phrase matcher.** It matches at token level with fuzzy
  behaviour, so **a non-zero hit is not evidence the phrase occurs.** Calibration: a search for
  `payload capacity` returned pages 35 and 36, **neither of which contains the phrase**;
  `Falcon 9` correctly hit p.35/36/37. **Every hit was therefore confirmed by reading the page
  before citation** — the same hazard 002 recorded at BWXT p.27.
- **A zero hit *is* meaningful, and this was calibrated too.** `propellant` correctly returned
  **ect1 p.6** — a page that does contain it — while returning **0** on `sec7` and `sec8`. A
  tool that finds the token where it exists and not where it does not is usable for negatives.
  That is why §1.3 can say the F5a parameters appear in no SPCX filing, and §1.4 can say
  `list price` and `marginal cost` occur nowhere in the 10-Q.
- **The sweep and the direct read disagree, and the read wins.** 002's `capitaliz*` sweep found
  nothing about capitalising internal launch costs; **p.36 states the mechanism verbatim**
  (§3.3). Locating a **definitional sentence** is not the same retrieval task as locating a
  **figure**, and a keyword sweep is calibrated for the latter. **Read the note's prose, not
  just its tables.**

**Two tool failures, recorded rather than worked around:**

- `read_source_outline(SPCX, sec10)` → **`NO_DOCUMENT`**. Resolved by taking the filing's
  `source_id` (`80fa17b3-0e51-4c1b-9965-2c908108c9fd`) from `search_documents`, which returned
  `citation_id: sec9`. **`citation_id`s are assigned by artefact, not enumerated** — a missing
  identifier is not a missing document.
- `search_unified(SPCX, "NASA contract")` → **`INTERNAL_ERROR: invalid input syntax for type
  json`**. Not retried. Consequence: the basis-B resolving source (§1.5) is reported as
  **unreached**, and the failure is named rather than reported as an absence of evidence. **A
  tool that errored is `UNEXERCISED`, not evidence of nothing.**

**Searches that were run and returned nothing, listed so the search is not repeated:**
`22.8` (0 pages, `sec8`) — the fact that made basis A's denominator fail; `expendable` (0,
`sec8`); `marginal cost` (0, `sec8`); `list price` (0, `sec8`); `propellant` (0, `sec8`; 0,
`sec7`); `NASA` (0, `sec8`; 0, `ect1`); `payload capacity` (0, `sec7` — no Starship or Falcon
capacity anywhere).

---

## 5. Dispositions — what this artifact could not resolve

**Primary, `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (carried in the frontmatter):** basis B, the
marginal cost per launch, for every SPCX vehicle. **Named resolving source: NASA CRS and
Commercial Crew contract values as a revealed-price floor** — inherited from 002 §5.1, which
registers "SPCX unit-economics" in this class. The disclosure that would resolve it is a
**filed contract value or unit-cost disclosure**; a contract value is a price and bounds cost
only indirectly (§1.5).

**Secondary, `UNRESOLVABLE-FROM-PLATFORM`, reported separately and not collapsed into the
above:** the basis B resolving source is *additionally* unreachable — `NASA` → 0 pages in the
10-Q and in the call; the corpus carries no contract-value document; `search_unified` errored.
The two classes have **different remedies** (monitor for a disclosure vs widen platform reach),
which is why they are not merged.

**Per-cell classes are in §1.4.** Cells absent for `UNRESOLVABLE-FROM-PLATFORM` reasons —
Falcon 9 basis A, the rated payload capacity — are absences of *reach*, **not** evidence that
the figures do not exist. Cells absent for `UNRESOLVABLE-FROM-PUBLIC-SOURCES` reasons —
Starship's entire row, the vehicle-level mass split, the depreciation amount — are absences of
*the world*, and each names the disclosure that would fill it.

**`UNEXERCISED` items, named as such and never as `CLEAN`:**

| Item | Why unexercised |
|---|---|
| Starship's F5a floor against a demonstrated price | No Starship price exists (§2.4) |
| Starship's F5c floor against a demonstrated cost | No per-unit Starship vehicle cost is filed |
| The A-vs-A″ discount test | Basis A is absent, so the corroboration 002 ran (to 3.4%) cannot be re-run on a second period |
| `basis_b_grade`'s DEMONSTRATED branch | No SPCX basis B exists; only Electron has one |
| DA-30 on the floor, for Starship | There is no per-kg Starship figure to hold to a basis |

**One corrected item, recorded rather than silently fixed:** 002 §8 item 6's conclusion that the
internal-launch capitalisation mechanism *"appears in no filed text this artifact could
locate"* is **falsified by 10-Q p.36**, quoted verbatim in §3.3. The mechanism is
`DEMONSTRATED`, the open question 002 handed to P3 is discharged, and the finding is
load-bearing rather than incidental — it is what makes §3.3's cost-of-revenue reading work and
what makes the customer-launch denominator the correct one.

**What would move the headline.** A Starship customer launch at a disclosed price (T-1). Until
then, the honest statement of the SPCX contribution to PIL-1 is: **a demonstrated price and a
modelled cost for a partially reusable vehicle, comfortably above its own floor; and no price,
no cost and no customer for the fully reusable one whose floor is the subject.**

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| SPCX ect1 p.3 | [📄 SPCX  p.3](https://agentii.ai/v/SPCX/ect1/3) |
| SPCX sec7 p.7 | [📄 SPCX  p.7](https://agentii.ai/v/SPCX/sec7/7) |
| SPCX sec8 p.35 | [📄 SPCX  p.35](https://agentii.ai/v/SPCX/sec8/35) |
| SPCX sec8 p.37 | [📄 SPCX  p.37](https://agentii.ai/v/SPCX/sec8/37) |
| SPCX sec8 p.42 | [📄 SPCX  p.42](https://agentii.ai/v/SPCX/sec8/42) |
| SPCX ect1 p.6 | [📄 SPCX  p.6](https://agentii.ai/v/SPCX/ect1/6) |
| SPCX ect1 p.1 | [📄 SPCX  p.1](https://agentii.ai/v/SPCX/ect1/1) |
| SPCX sec8 p.36 | [📄 SPCX  p.36](https://agentii.ai/v/SPCX/sec8/36) |
| SPCX sec8 p.14 | [📄 SPCX  p.14](https://agentii.ai/v/SPCX/sec8/14) **(newly surfaced)** |
| SPCX sec7 p.5 | [📄 SPCX  p.5](https://agentii.ai/v/SPCX/sec7/5) **(newly surfaced)** |
