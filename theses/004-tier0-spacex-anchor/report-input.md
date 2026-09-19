# Report Input — 004 — Tier 0: SpaceX Anchor, SOTP across Space / Connectivity / AI

<!-- pack_version: 2.0 · sources_hash: 79dafd812940578c · deterministic — no timestamps -->

## Header facts
- thesis_id: 004-tier0-spacex-anchor
- name: 004 — Tier 0: SpaceX Anchor, SOTP across Space / Connectivity / AI
- claim: SPCX's live $2.07 trillion capitalisation is 312.8× the annualised operating income of Connectivity — its only profitable segment. No conglomerate discount exists to measure, and no admissible comparator exists for any of the three regimes: the partition closes at zero of eleven.
- constitution_pin: 1.5.0
- as_of: 2026-09-18
- entry_count: (none)
- universe: SPCX 100%

## Source — _cross/tier0-spacex-anchor_synthesis.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: cross
ticker: cross
skill: synthesis
mode: methodology
generated_at: 2026-09-19T16:10:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "Every segment figure is read on the FILED sign. The segments sum to $(143)M and the served consolidated line returns +143,000,000 — 16 of 20 served SPCX OperatingIncomeLoss facts are sign-stripped."
pillar_verdicts:
  PIL-1: "HOLDS — 3 of 3 segments carry a discrete filed revenue line AND a discrete filed operating result. The Minimum Defensible View is delivered; the decomposition is real."
  PIL-2: "HOLDS, with the DA-10 bound carried — operating leverage is demonstrated (+79.4% income on +65.8% revenue) and the channel mix moves toward the higher-value channel. Price erosion cannot be fully separated from mix shift from public disclosure."
  PIL-3: "HOLDS AS A BOUND, not as a value — the AI segment has no admissible multiple from filed or peer data. Carried at INVESTED CAPITAL; advertising IS separable at 21.0% of the segment, Grok and compute are not."
  PIL-4: "HOLDS — the ex-R&D operating result is POSITIVE at +$534M, so launch carries standalone value. The numerator is MODELED (the filing does not split Starship from Falcon R&D) and the DA-06 non-comparability flag travels with the row."
  PIL-5: "HOLDS — coverage 0.1005x, an order of magnitude below the 1.0x falsifier. CAPITAL binds, and at this moment it binds through one unresolved disclosure (the Cursor dilution) now RESOLVED at 391,041,680 shares."
  PIL-6: "HOLDS — the comparability partition admits 0 of 11, and every published anchor row carries a boundary naming 005, 006 and 009 as its permitted consumers."
capability_timeline:
  - note: >
      Partial. This thesis is `market_data_stage: per_row` — `sotp-valuation` and `reverse-dcf`
      run at `late`, the other five executed rows at `none`. It is the FIRST thesis in the
      workspace with a live market-data dependency, and the first where `PRICE_ACCESS_PREMATURE`
      could fire. The nearest timeline equivalent is the seven-trigger register (T-1 … T-7),
      which is datability-driven rather than capability-adoption-driven.
key_metrics:
  separable_segments: 3
  live_market_cap_usd_t: 2.0718
  market_cap_to_connectivity_opinc: 312.8
  admissible_comparators: 0
  coverage_ratio: 0.1005
  cursor_shares_issued: 391041680
  challenge_findings_high: 4
  segment_capex_total_q2_2026_usd_m: 18369
  ai_capex_share_q2_2026: 0.8617
  connectivity_closure_residual_usd_m: 0
---

# Thesis 004 — Tier 0: SpaceX Anchor

**The synthesis.** What the anchor found, what it refused to claim, and what 005–009 may price off.

## The finding, in one line

> **SPCX's live market capitalisation — $2.0718T — is 312.8× the annualised operating income of
> Connectivity, and Connectivity is the ONLY profitable segment.**

Space runs **$(2.2)bn** annualised and AI **$(5.0)bn**. **So there is no conventional conglomerate
discount to measure.** The standard SOTP asks whether the parts exceed the whole; here the whole
already requires the one profitable segment to carry ~313×, and **the finding survives every
allocation** — even granting the two loss-making segments **$1.5T**, Connectivity carries **86×**.

## Where the value sits, and where it does not

**Four independent lines converge, and three were already in the workspace before this thesis:**

| Line | Source | What it says |
|---|---|---|
| **A1b falsified** | 001 | Value migrated **out of** launch |
| **27 of 37 internal** | 004's own §1 | Space is an **unpriced input** to the thing that earns — capitalised into satellites in PP&E |
| **The margin ladder** | 003 | Operating margin is **monotone in distance from programme risk** |
| **The extension is a mix shift** | 004 | Connectivity's growth is **channel mix toward Enterprise & Government (+108.3% vs +44.4%)**, not a rising tide |

**And the anchor's own addition: the AI segment cannot be valued from public disclosure at all.**
Its headline metric — **1.4 GW** — is **IT load** (DA-11), a capacity figure no disclosed $/kW
converts. **That is why P3's headline is invested capital, a COST basis.**

## What the anchor refused to claim

The refusals are the deliverable as much as the finding:

- **No blended multiple.** Valuing three businesses at one rate is a different claim, and the
  spread between the two is the finding.
- **No forward DCF.** Fails the ≥3-year positive-FCF limb. `reverse-dcf` is admissible **because
  it forecasts nothing**.
- **No borrowed comparator.** **The partition admits 0 of 11**, and the three segments fail for
  **three different reasons** — earnings, price formation, and disclosure. One screen would not
  have found them.
- **No external multiple for Space.** DA-06: a captive-integrated launcher has **no transaction
  price**. Comparing its margin to a peer is comparing a price to a non-price.
- **No point estimate.** Every regime is a `MODELED` range.

## The reverse-DCF, and the breach it exposes

At the constitution's **15–25% required return**, the live price implies **14.7–24.7% perpetual
growth** — `g ≈ r − 0.32%`. **Terminal value therefore approaches 100% of EV, breaching F1's own
50–70% cap.** Reported as three readings, not resolved: the price may be too high, the cap may be
wrong at this stage, or **the attribution may be the artefact** — the 313× sets Space and AI to
zero by construction.

## What this thesis could NOT value — recorded, never implied

| Item | Class |
|---|---|
| Aviation / maritime splits | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — inside `EnterpriseAndGovernmentMember` |
| Grok vs compute | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — advertising **is** separable |
| Subscribers / ARPU by channel | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — revenue decomposes, the denominator does not |
| The constitution's ~$1.62T basis | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — **it implies $122.95/share against an IPO at $135.00** |

> ### ⚠️ RETRACTED ROW — "segment-level capex" was NOT unresolvable, and the claim is withdrawn
>
> An earlier version of this table listed **segment-level capex** as
> `UNRESOLVABLE-FROM-PUBLIC-SOURCES`, *"company-level attribution only."* **That is false.** The
> 10-Q's Note 18 supplemental segment table files **capital expenditures by segment** — Space
> **$1,174M**, Connectivity **$1,367M**, AI **$15,828M**, total **$18,369M**, 3M ended 2026-06-30.
> Source: [SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30).
>
> **Why the retraction matters more than the row.** The claim was not a search failure — the figure
> is on **the same page as the segment income table this thesis is built on**. It was recorded as
> unresolvable because the artifact that produced it **did not open the page it was citing**. A
> bound asserted as `UNRESOLVABLE` is the most expensive kind of error here: it closes a question
> the filings answer, and no downstream thesis will re-open it.
>
> **What the figure adds — AI is 86.2% of capital expenditure and the largest loss.**
> `15,828 / 18,369 = 86.17%` of quarterly capex goes to the segment running a **$(1,257)M** quarterly
> operating loss on **$2,561M** of revenue. **Connectivity, the only profitable segment, receives
> 7.4%.** That is the capital-allocation finding stated as arithmetic, and it is available from the
> filings this thesis already reads.

## What 005, 006 and 009 may price off

**The Connectivity and AI rows are reusable references for 006 and 009** — SPCX appears in **neither
universe**. The boundaries are **partitions**: a name is in or out, with its excluded class named
(`P11` · `loss_making` · `PARTIAL` · `non_disclosure`). **A downstream thesis that prices off a name
this anchor excluded has re-opened a closed class without saying so** — the failure P6 is built to
prevent, and one that would be invisible because that thesis would look internally consistent.

**And per Q64, two challenge findings block knowledge-base entry**: the `entity_claims` schema names
`ticker` where every consumer reads `entity`, and carries no `retrieved_at`. See `challenge.md`.
````

## Artifact — artifacts/SPCX/2026-09-19_competitive_direct-competitor-identification-and-analysis.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-4/PIL-5"
ticker: SPCX
skill: competitive
mode: direct-competitor-identification-and-analysis
generated_at: 2026-09-19T12:10:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "826995c722a4"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-06"
    chosen_reading: "SPCX Space is captive_integrated — it flies its own payloads. A competitor is therefore identified on the CUSTOMER-LAUNCH book, not the full manifest: 27 of 37 Falcon launches were internal and generate no Space revenue. Comparing total-launch counts across launchers compares a market against a non-market."
  - da_id: "DA-08"
    chosen_reading: "Launch counting basis — the filed split is three-way and never collapsed: Falcon-only (37 / 77), all-vehicles (38 / 78, derived), customer-only (10 / 17). Every competitive share below names its basis. 003 established that two filed rates point in OPPOSITE directions on one quarter."
entity_claims:
  - claim_id: "comp-space-customer-launches-q2"
    ticker: SPCX
    metric: customer_launch_count
    value: 10
    unit: count
    basis: "customer-only launch count, Q2 2026; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "003/artifacts/SPCX/2026-09-19_2310_operational-kpi — consumed, not re-derived"
  - claim_id: "comp-space-total-launches-q2"
    ticker: SPCX
    metric: total_launch_count
    value: 38
    unit: count
    basis: "all-vehicles basis, Q2 2026; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "003/artifacts/SPCX — all-vehicles basis, derived; the filed basis set is three-way"
key_metrics:
  customer_launch_count_q2_2026: 10
  total_launch_count_q2_2026: 38
---

# SPCX × competitive × direct-competitor-identification-and-analysis

**Launch competitive position, behind P4's standalone-value test and P5's capital-intensity
comparison.** Filed under **SPCX** per spec §6: **RKLB and FLY are read-through comparators**, so
their data is read here and this single artifact is the output — they receive no artifact of their
own.

## 1. Who is actually a competitor — the boundary question

**The naive answer is a launch-count share. It is the wrong measurement, and the reason is DA-06.**

| Basis | SPCX Q2 2026 | What it measures |
|---|---:|---|
| **All vehicles** | **38** | SPCX's own cadence |
| **Customer launches only** | **10** | **The market SPCX competes in** |
| Internal | 28 | SPCX launching SPCX. **No transaction price exists** |

**~74% of SPCX launches produce no Space revenue by design** — the segment's revenue is a *residual
customer-book*, not a market. So:

> **A competitor is a company bidding for the same customer launch. RKLB and FLY are not competing
> with 38 launches; they are competing with 10.**

**This is the single most important competitive fact in the thesis, and it is counter-intuitive in
the direction that matters.** SPCX's apparent dominance on manifest count **overstates its
competitive exposure** — the internal launches are cost, not share.

## 2. The competitor set, classed

| Name | Class | Position |
|---|---|---|
| **RKLB** | **Direct** — the only other launcher with a **measured** marginal cost | Electron (small-lift, **the universe's only `DEMONSTRATED` cost point**) and Neutron (medium-lift, **UNFLOWN**). **Files NO segment operating income for Launch Services** (003's E-04) |
| **FLY** | **Direct**, structurally weaker | Alpha — fully expendable, and **the universe's worst verified margin at −80.90%**. An EGC with thin disclosure |
| **Amazon Leo** *(Kuiper)* | **Vertical threat, not a launch competitor** | ⚠️ **Named but not classed as a direct competitor**: it is a *demand owner* building its own constellation. It competes with **Connectivity**, not Space |
| **China state launch** | **Out of universe** | No listed comparator; a **state-priced** alternative. **Excluded as unpriceable, not as irrelevant** |
| **Starship itself** | ⚠️ **The competitor that is not in the set** | See §4 |

## 3. The asymmetry that defines the Space position

From 003's curve, consumed not re-derived:

| | SPCX Space | RKLB | FLY |
|---|---|---|---|
| **Segment gross margin** | **65.80%** *(highest in the company)* | — | — |
| **Segment operating margin** | **−56.34%** *(worst in the company)* | — | **−80.90%** |
| **Measured marginal cost** | ✗ none disclosed | ✅ **Electron — the universe's only one** | ✗ none disclosed |
| **Basis C $/kg** | **$6,596** — **71.5% Starship R&D, not a launch cost** | — | — |

**The swing inside SPCX Space is 122.14 pp**, decomposed exactly as **R&D 111.85 pp + SG&A 10.29 pp**
of segment revenue. **So SPCX's launch business is simultaneously the sector's best gross margin and
its second-worst operating margin**, and the two ladders order it at opposite ends.

**Consequence for P4:** the competitive position cannot be read off either ladder alone.
**The gross margin is the launch economics; the operating margin is Starship.** P4's ex-R&D test
exists precisely to separate them, and this artifact establishes that **the separation is also the
competitive question** — SPCX's launch position is strong *and* its reported segment position is
weak, and both are true on the same filing.

## 4. ⚠️ Starship is SPCX's own most dangerous competitor, and it is inside the segment

The sharpest competitive fact is structural:

- **Starship is fully reusable; Falcon is partially reusable.** The architecture change moves the
  cost floor from **F5b** (expended second stage dominant, ~$8–12M) to **F5a** (propellant only,
  ~$46–92/kg at 100 t) — **an order of magnitude**.
- **Starship therefore competes with Falcon**, on SPCX's own manifest.
- **The plan's binding constraint for P4 is `MANUFACTURING_RATE` in the medium term — F5b, the
  expended second-stage curve.** So the competitive pressure is not from RKLB or FLY; it is the
  transition **within** the segment.

**And it is not yet a competitor in the market sense:** Starship launched **3 → 1 across H1**, so it
is a **cost and capability programme, not a competitive position**. **P4's claim — that launch is
separable from Starship funding — is exactly the claim that this transition has not yet happened.**

## 5. What this establishes for the SOTP

| Feeds | What |
|---|---|
| **P4** | The competitor set behind the standalone-value test; **the DA-06 boundary that makes 10 the right denominator** |
| **P5** | Capital-intensity comparison — the plan assigns this here, and it is the **second half of the competitive question**: SPCX's position is bought with a capital scale RKLB and FLY cannot match. **Carried to P5, not concluded here** |
| **P6** | RKLB and FLY are **`loss_making`** in the comparability partition → **no multiple may be borrowed from either** |

**What this artifact does NOT do:** price anything. It establishes *who competes* and *on what
basis*. The multiple that attaches is P6's, and the partition there excludes both names.
````

## Artifact — artifacts/SPCX/2026-09-19_competitive_market-share-dynamics-analysis.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-4/PIL-5"
ticker: SPCX
skill: competitive
mode: market-share-dynamics-analysis
generated_at: 2026-09-19T12:15:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "826995c722a4"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-08"
    chosen_reading: "The customer-launch share is reported on BOTH durations because the two point in OPPOSITE directions. A single quoted share is a basis choice, not a fact — 003 established this and this artifact does not collapse it."
  - da_id: "DA-26"
    chosen_reading: "Q2 (3M) and H1 (6M) are filed under the same concept and axis. The two share readings below are not a trend and a level; they are two measurements of different windows, and neither is more correct."
entity_claims:
  - claim_id: "msd-customer-share-q2-2026"
    ticker: SPCX
    metric: customer_launch_share
    value: 0.263
    unit: ratio
    basis: "customer launches / all launches, Q2 2026, all-vehicles denominator; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "003/artifacts/SPCX/2026-09-19_2310_operational-kpi — consumed"
  - claim_id: "msd-customer-share-h1-2026"
    ticker: SPCX
    metric: customer_launch_share
    value: 0.218
    unit: ratio
    basis: "customer launches / all launches, H1 2026; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "003/artifacts/SPCX/2026-09-19_2310_operational-kpi — consumed"
  - claim_id: "msd-customer-share-q2-2025"
    ticker: SPCX
    metric: customer_launch_share
    value: 0.196
    unit: ratio
    basis: "customer launches / all launches, Q2 2025; 3M duration, quarter ended 2025-06-30"
    period: "2025Q2"
    evidence_grade: DEMONSTRATED
    source: "003/artifacts/SPCX — consumed"
  - claim_id: "msd-customer-share-h1-2025"
    ticker: SPCX
    metric: customer_launch_share
    value: 0.250
    unit: ratio
    basis: "customer launches / all launches, H1 2025; 6M duration, six months ended 2025-06-30"
    period: "2025Q2"
    evidence_grade: DEMONSTRATED
    source: "003/artifacts/SPCX — consumed"
key_metrics:
  customer_launch_share_q2_2026: 0.263
  customer_launch_share_h1_2026: 0.218
  customer_launch_share_q2_2025: 0.196
  customer_launch_share_h1_2025: 0.25
---

# SPCX × competitive × market-share-dynamics-analysis

**How the share moves, and why a single number cannot say.**

## 1. 🔴 The share has TWO bases with OPPOSITE signs

| Window | 2025 | 2026 | Change |
|---|---:|---:|---|
| **Q2 (3M)** | 19.6% | **26.3%** | **▲ +6.7 pp — RISING** |
| **H1 (6M)** | 25.0% | **21.8%** | **▼ −3.2 pp — FALLING** |

**Both are computed from the same filing, on the same metric, over overlapping windows — and they
disagree in sign.**

**This is not a rounding artefact or an error.** Q2 2026's customer share (26.3%) is high against a
low Q2 2025, while H1 2026 is dragged down by a weak Q1 that the quarter window does not see.
**The two windows measure different things and neither is wrong.**

> **Consequence, stated plainly: "SPCX's customer-launch share is rising" and "…is falling" are both
> defensible citations of the filing.** An artifact that quotes one without the other has made a
> **basis choice** and presented it as a fact. This artifact quotes **four** figures so that choice
> is visible.

**This is DA-30 in operation** — two bases on one concept, collapsed without a basis field — and it
is the third instance of the pattern found at SPCX this thesis has recorded.

## 2. What the share actually measures, and what it cannot

**Denominator:** **all vehicles** (38 in Q2 2026), per the filed three-way basis set.
**Numerator:** **customer launches only** (10).

**Three things the ratio is NOT:**

1. **Not a revenue share.** The internal 28 launches carry **no transaction price** (DA-06). A
   *count* share and a *revenue* share are different quantities, and the segment's revenue is a
   residual customer-book.
2. **Not a market share.** There is no filed total-market denominator. The ratio is **SPCX customer
   launches over SPCX launches** — a *mix* metric, not a share of a market.
3. **Not comparable to RKLB's or FLY's launch counts** without re-basing: RKLB's cumulative figure
   *"includes suborbital launches"*, a mixed basis 003 flagged.

## 3. The dynamic that matters for P4

**The share is moving because the denominator is moving, not the numerator.**

| | Q2 2026 | Direction |
|---|---:|---|
| Customer launches | **10** | **flat** across the universe's peers (003: customer payload *"flat at 87 t vs 88 t"*) |
| All launches | **38** | internal-heavy |
| **⇒ Customer share** | 26.3% / 21.8% | **moves with the internal manifest** |

**SPCX's customer book is not growing as fast as its own internal manifest.** That is the
competitive dynamic: **the launch business is increasingly SPCX launching SPCX.**

**And it cuts against a naive reading of P4.** If more of the manifest is internal, the *launch*
segment looks less like a market business and more like a **captive cost centre** — which is
**DA-06's structural point arriving through the share series.**

**It does NOT falsify P4's claim**, which is that the ex-R&D launch result is **positive** and the
segment carries standalone value. **A captive-heavy manifest can still be profitable per customer
launch** — SPCX's 65.80% segment gross margin says it is. **What it falsifies is any claim that
SPCX's competitive position is widening in the market.** It is not; its *customer* book is flat
while its *internal* book grows.

## 4. Benchmarks — and why they are weak by construction

| Comparator | Its share series | Usable? |
|---|---|---|
| **RKLB** | Electron cadence, and a build-vs-launch inventory series (003: 2024 14 built/16 launched; 2025 24/21; H1 2026 11/12) — **inventory drawn down in 2 of 3 periods** | ⚠️ **Different denominator** — a small-lift pure-play. The **build-vs-launch** series is the *usable* comparison, not a share |
| **FLY** | No comparable series; single reportable segment, thin EGC disclosure | ❌ |
| **Amazon Leo** | None — it is a **demand owner**, and its launches are its own | ❌ **Not a launch-market participant on this metric** |

**No comparator produces a share series on SPCX's basis.** Per P6's partition, RKLB and FLY are
`loss_making` and **no multiple may be borrowed**; this artifact adds that **no share may be
borrowed either**, for the separate reason that the bases differ.

## 5. What P4 and P5 take from this

- **P4:** the competitive position is **flat in the customer market and growing internally** —
  which strengthens the case for reading Space's value from **segment contribution** (round 4's
  DA-06 answer) rather than from a market-share narrative.
- **P5:** the growing internal manifest is a **capital story**: internal launches are **capitalised
  into satellites in PP&E**, so the share shift and the capex are the same fact seen twice.
  **Carried to P5.**
````

## Artifact — artifacts/SPCX/2026-09-19_competitive_market-share-evolution-and-competitive-benchmarking.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-4/PIL-5"
ticker: SPCX
skill: competitive
mode: market-share-evolution-and-competitive-benchmarking
generated_at: 2026-09-19T12:20:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "826995c722a4"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-08"
    chosen_reading: "Every benchmarking comparison below names the launch-count basis it uses and the vehicle it concerns. 003's curve is consumed for cost, never re-derived, and its per-vehicle grades travel with each row."
  - da_id: "DA-01"
    chosen_reading: "Cost bases A / A' / B / C are enumerated, never collapsed — the four span a 7-13x spread around ONE Falcon mission. A benchmarking table that quotes a single $/kg has silently chosen a basis."
entity_claims:
  - claim_id: "mse-rklb-inventory-drawdown-periods"
    ticker: RKLB
    metric: periods_with_inventory_drawdown
    value: 2
    unit: count
    basis: "of 3 comparable periods (2024, 2025, H1 2026); build 14/24/11 vs launch 16/21/12"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "003/artifacts/RKLB — consumed, not re-derived"
  - claim_id: "mse-fly-margin"
    ticker: FLY
    metric: operating_margin
    value: -0.809
    unit: ratio
    basis: "filed, FLY consolidated — the universe's worst verified margin; 3M duration"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "003/_cross/value-pool-map.md §4.4 — consumed"
key_metrics:
  rklb_periods_with_inventory_drawdown: 2
  fly_operating_margin: -0.809
---

# SPCX × competitive × market-share-evolution-and-competitive-benchmarking

**How the position evolved, and what it can legitimately be benchmarked against.**

## 1. The evolution, in one line

> **SPCX's competitive position did not widen or narrow — it CHANGED KIND.** The customer book is
> flat; the internal manifest grew. **The launch segment has moved from a market business toward a
> captive supply function**, and that is the evolution, not a share number.

**The evidence is §3 of `market-share-dynamics-analysis`**: customer share Q2 ▲26.3% vs H1 ▼21.8%,
with the customer count **flat** while the all-vehicle denominator moved. **A share that moves only
with its denominator is a mix change, not a competitive gain.**

## 2. The benchmarking table — and its three exclusions

**Consuming 003's curve** (never re-derived). **Every row names its basis.**

| Benchmark | SPCX | RKLB | FLY | Usable for a multiple? |
|---|---|---|---|---|
| **Segment operating margin** | **−56.34%** (Space) | *no segment operating income filed* | **−80.90%** | ❌ all negative |
| **Segment gross margin** | **65.80%** (Space) | — | — | ⚠️ **basis-mismatched** — see §3 |
| **`DEMONSTRATED` marginal cost** | ✗ none | ✅ **Electron — the universe's only one** | ✗ none | ⚠️ **not comparable to SPCX** (different architecture tier) |
| **Basis C $/kg** | **$6,596** — **71.5% Starship R&D, not a launch cost** | — | — | ❌ **not a launch cost at all** |
| **Vehicle architecture** | F9 partially reusable (**F5b**); Starship declared fully reusable (**F5a**, flown expendable) | Electron **F5c**; Neutron F5b **unflown** | Alpha **F5c** | ✅ the one **cleanly comparable** attribute |
| **Capital intensity** | **investing $(34,487)M** H1 vs operating **+$3,466M** | — | — | ✅ but carried to **P5**, not concluded here |

**Excluded from the table, with reason:**

- **BA / LMT / NOC** — primes, 007's universe. **Named as a load-bearing absence, not proxied.**
- **Amazon Leo** — a demand owner, not a launch-market participant.
- **Any whole-company multiple for RKLB or FLY** — both `loss_making` (P6 partition).

## 3. ⚠️ Why the gross-margin comparison is a basis trap

SPCX Space's **65.80%** is the universe's highest segment gross margin. **It is not comparable to a
peer launcher's gross margin**, and the reason is **DA-06 + DA-30 together**:

1. **SPCX files NO segment gross-profit subtotal.** The 65.80% is **`DERIVED`** — `(962 − 329) / 962`
   — from the segment's own revenue and cost of revenue. **003 constructed it; the filer did not file it.**
2. **The served ratio at SPCX pairs a segment numerator with a consolidated denominator** — the
   DA-30 instance 003 recorded (segment **65.80%** vs consolidated **55.27%**). **Both bases are
   live in the platform's served layer.**
3. **`captive_integrated` means the cost base is not a market cost.** SPCX's launch cost of revenue
   excludes everything it flies for itself.

**⇒ A peer's gross margin is a ratio over a priced cost base. SPCX's is a ratio over a residual
customer-book cost base, derived by us rather than filed.** Comparing them compares a price to a
non-price — 003's own phrasing, and it applies to the margin line exactly as it does to the multiple.

## 4. What is genuinely comparable — the architecture axis

**One attribute survives every exclusion: vehicle architecture, because it is a physical fact
rather than an accounting one.**

From 003's curve, consumed:

| Vehicle | Architecture | F5 tier | Forward indicator |
|---|---|---|---|
| Falcon 9 | partially reusable | **F5b** | Expended second stage ~**$8–12M** dominates; propellant only ~2–3% |
| Starship | declared fully reusable | **F5a** *(flown expendable → F5c)* | Propellant ~**$4.6–9.2M**, floor ~**$46–92/kg** at 100 t |
| Electron | fully expendable | **F5c** | **The universe's only `DEMONSTRATED` price** |
| Neutron | partially reusable | **F5b** | **Unflown** |
| Alpha | fully expendable | **F5c** | Payload is a **CLASS LABEL**, not a denominator |

**The evolution this table shows:** SPCX is the only name in the set holding **two architectures at
once** — and **P4's binding constraint is that the transition between them is the medium-term cost
question, not the competitive one.** RKLB is attempting the same jump (Electron F5c → Neutron F5b)
**with an unflown vehicle**.

## 5. Benchmarking conclusion, stated as a bound

**No competitor in this universe can benchmark SPCX's launch segment on a financial metric.**
Three independent reasons, and they must not be collapsed:

| Barrier | Applies to |
|---|---|
| `loss_making` — no earnings multiple exists | RKLB, FLY |
| **basis mismatch** — derived vs filed, captive vs market cost base | all peers on the gross-margin line |
| **architecture tier differs** — F5a/b/c are different cost structures | every vehicle comparison except within-tier |

**The only clean comparisons are physical (architecture) and capital (P5).** That is the finding,
and it is the same shape as P6's partition: **the reasons to exclude differ per row, so one
screen would not have found them.**

## 6. Hand-offs

| To | What |
|---|---|
| **P4** | Launch position is **flat in the market, growing internally** → read value from **segment contribution**, per round 4's DA-06 answer |
| **P5** | **Capital intensity is where SPCX is genuinely incomparable** — and that is the plan's assignment for this row. `$(34,487)M` investing against `+$3,466M` operating, ratio **≈0.10×**. **The competitive position is bought with capital no peer can match**, which makes the funding structure the binding constraint rather than any competitive dynamic |
| **P6** | RKLB and FLY are `loss_making`; **no multiple borrowable** |
| **007** | BA / LMT / NOC — the prime layer, **excluded here by scope, not by class** |
````

## Artifact — artifacts/SPCX/2026-09-19_comps_retrieval-scope.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-3/PIL-6"
ticker: SPCX
skill: comps
mode: retrieval-scope
generated_at: 2026-09-19T11:50:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "264697c3872a"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "A comparator is judged on whether it files a DISCRETE segment matching the SPCX segment being priced. A whole-company multiple is not a substitute for a segment multiple — it prices a different collection of businesses against the same numerator."
  - da_id: "DA-06"
    chosen_reading: "SPCX Space is captive_integrated: no transaction price exists for the launches it does not sell. A comparator's launch margin is a PRICE against cost; Space's is a residual customer-book. They are not two measurements of one quantity."
entity_claims:
  - claim_id: "comps-admissible-count"
    ticker: SPCX
    metric: count_of_admissible_segment_comparators
    value: 0
    unit: count
    basis: "comparators admitted to carry a P6 boundary; all eleven named names excluded with a class. 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "this artifact §2 — the partition, with each exclusion classed"
key_metrics:
  admissible_segment_comparators: 0
---

# SPCX × comps × retrieval-scope

**Which sources are admitted and which are excluded — the P6 comparability boundary.**

The partition is the deliverable. Per round 4's confirmed answer, **a boundary is a
PARTITION, not a graded score**: a name is **in or out**, and the excluded class is named with its
reason. **A graded score would let each downstream thesis pick its own threshold**, which is the
failure P6 exists to stop.

## 1. The partition, stated once

| Class | Meaning |
|---|---|
| **ADMITTED** | May carry a P6 boundary; downstream theses may price off it |
| **EXCLUDED — `loss_making`** | No earnings multiple exists to borrow |
| **EXCLUDED — `P11`** | A deal security: the price is a **spread**, not a fundamental |
| **EXCLUDED — `PARTIAL`** | Coverage insufficient to construct a multiple |
| **EXCLUDED — `non_disclosure`** | Files no discrete segment matching the SPCX segment |

> ### 🔴 ADMITTED: ZERO of eleven.
>
> **Not one named comparator can carry a P6 boundary.** The anchor's three regimes must therefore
> be sourced from **SPCX's own segment data and bounded read-throughs**, and that is the finding —
> not a shortfall in the search. **Three regimes, three different reasons no natural comp set
> exists**, and the *reasons* differ, which is why one exclusion rule would not have found them.

## 2. The partition applied — eleven names

### Space comparators

| Ticker | Class | Why |
|---|---|---|
| **RKLB** | ❌ `loss_making` | A pure-play launcher with no positive earnings. **No earnings multiple exists to borrow.** Also **P11** (acquirer of IRDM) — **two independent exclusions**, which matters because it would otherwise be the closest comparator |
| **FLY** | ❌ `loss_making` | Second fully-expendable vehicle; the universe's *worst* verified margin at **−80.90%** (003's map). A negative denominator prices nothing |
| BA · LMT · NOC | ⚠️ **out of scope here** | Primes, owned by 007. **Named as a load-bearing absence, not proxied** — and 003's margin ladder puts the prime layer at **11.25%**, which is a *different* business from a launch segment |

### Connectivity comparators

| Ticker | Class | Why |
|---|---|---|
| **IRDM** | ❌ **`P11`** | Acquired by RKLB at **$54.00/share (agreed 2026-06-28)**. **Its price is a spread.** ⚠️ **This is the exclusion that survives live data** — a *live* multiple on a spread is **no more admissible than a stale one**. Round 3's live feed makes the boundary **verifiable**; it does not remove it |
| **GSAT** | ❌ **`P11`** | Acquired by Amazon at **$90.00/share (agreed 2026-04-13)**. **64% of six-month revenue is one customer** who is also financier and acquirer. Spread, not fundamental |
| **ASTS** | ❌ **`PARTIAL`** | Coverage insufficient to construct a comparable multiple |
| **VSAT** | ❌ **`PARTIAL`** | Same |
| **SATS** | ⚠️ **`DA-24` contaminated** | The Q3 2025 event was a **non-cash $16,481,468k impairment charge**, not the *"$27B spectrum gain"* an earlier draft recorded. **The licences remain on the balance sheet.** Used as inherited context only |

### AI comparators

| Ticker | Class | Why |
|---|---|---|
| **MSFT** | ❌ `non_disclosure` | **Compute is a cost centre inside Intelligent Cloud**, not a reportable segment. **A cost centre carries no segment multiple to borrow** |
| **GOOG** | ❌ `non_disclosure` | Compute sits **inside Google Cloud**. Same structural bar. *(Query as **`GOOG`**, never `GOOGL`.)* |
| **NVDA** | ❌ `non_disclosure` — **and a category error** | **The silicon supplier, not the operator.** The read-through is to *feasibility*, never to a multiple |
| **VRT** | ❌ `non_disclosure` | Thermal comparator. Supplies the **DA-11 PUE restatement context that 002 owns** — **consumed, never re-derived** |

## 3. What the partition produces — the three regimes

| Segment | Natural comparables | The reason no comp exists | SOTP treatment |
|---|---|---|---|
| **Space** | RKLB, FLY | `loss_making` — no earnings multiple | Revenue or capacity multiple, `MODELED`, stated as a range; **plus the DA-06 non-comparability flag** |
| **Connectivity** | IRDM, GSAT | **`P11`** — the price is a spread | **Margin-anchored**, `MODELED`, cross-checked against **terrestrial broadband** rather than satellite peers |
| **AI** | MSFT, GOOG, NVDA | `non_disclosure` — no discrete compute segment | One of P3's three framings; **headline = invested capital** (round 4) |

**The three reasons are different, and the table is the argument for why a single comp screen would
not have found them.** `loss_making` is an earnings problem; `P11` is a *price-formation* problem;
`non_disclosure` is a *segment-boundary* problem.

## 4. ⚠️ Live data does NOT promote any excluded name

Round 3 established a **keyless live price feed** and round 4 confirmed the boundary shape. Two
things follow, and the second is the one that is easy to get wrong:

1. **The boundary is now VERIFIABLE rather than asserted.** Each exclusion can be checked against a
   live price.
2. **Verifiable ≠ admissible.** **`IRDM` and `GSAT` remain excluded as `P11` even though they are
   now priceable.** A live multiple computed on a merger spread measures **deal terms**, not the
   business. **This is the trap the partition exists to catch**, and the live feed makes it *more*
   tempting, not less.

## 5. Downstream permissions

Per round 2's coverage answer, the anchor's rows are reusable references for **005, 006 and 009** —
**not 005 alone.** SPCX appears in **neither 006's universe** (IRDM, GSAT, SATS, ASTS, VSAT) **nor
009's** (VRT, NVDA, GOOG, MSFT, AMZN, AAPL), so **004 is the programme's only valuation of SPCX's
Connectivity and AI segments**, and those two rows are built to be cited.

**What a downstream thesis may NOT do with this artifact:** treat any of the eleven names as an
admitted comparator. **The partition says zero.** A downstream thesis that prices off a name this
artifact excluded has **re-opened a closed class without stating it** — the failure mode P6 is
built to prevent, and one that would be invisible because that thesis would look internally
consistent.
````

## Artifact — artifacts/SPCX/2026-09-19_growth-strategy_growth-strategy-assessment.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-5"
ticker: SPCX
skill: growth-strategy
mode: growth-strategy-assessment
generated_at: 2026-09-19T12:55:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "ab94b90ee0ff"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "The capital-allocation narrative is read against the CAPEX DISCLOSURE's own ordering, not against management commentary. Where the filing lists an allocation sequence, the sequence is the evidence."
entity_claims:
  - claim_id: "gs-investing-h1-2026"
    ticker: SPCX
    metric: investing_cash_outflow
    value: -34487000000
    unit: USD
    basis: "H1 2026 investing; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "001/artifacts/SPCX/2026-09-18_2310_operational-kpi §5 — consumed"
  - claim_id: "gs-financing-h1-2026"
    ticker: SPCX
    metric: financing_cash_inflow
    value: 100291000000
    unit: USD
    basis: "H1 2026 financing = IPO 85,675 + notes 40,869 + other; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "001/artifacts/SPCX/2026-09-18_2310_operational-kpi §5 — consumed"
key_metrics:
  investing_outflow_h1_2026_usd_m: -34487
  financing_inflow_h1_2026_usd_m: 100291
---

# SPCX × growth-strategy × growth-strategy-assessment

**The capital-allocation story the filings tell, versus the one the segments show.**

## 1. The allocation, read from the disclosure's own ordering

**SPCX named data centers before launch facilities when describing the capex.** That ordering is the
finding, and it is checkable against the numbers:

| | H1 2026 |
|---|---:|
| Operating cash flow | **+$3,466M** |
| **Investing** | **$(34,487)M** |
| **Financing** | **+$100,291M** — IPO **$85,675M** + notes **$40,869M** |

**Coverage ≈ 0.10×.** The build is funded **almost entirely externally**, and the disclosure says
where it goes first.

**⇒ The growth strategy is a CAPITAL strategy.** Every segment's growth is downstream of a funding
decision, not of a demand or technology constraint. That is why `CAPITAL` is the thesis's binding
constraint, and this artifact is where the allocation narrative meets it.

## 2. The strategy per segment, stated as what the filings support

| Segment | Growth driver | Filed evidence | Constraint |
|---|---|---|---|
| **Connectivity** | **Enterprise & Government**, 2.4× faster than consumer | `+108.3%` vs `+44.4%` (from `revenue-decomp`) | **`DEMAND`** — P2's constraint |
| **AI** | Compute buildout | **1.4 GW IT load** (DA-11 — unconvertible) | **`POWER`** operationally, **A4** for valuation |
| **Space** | **Not growth** — customer book flat, 8.29% of consolidated | 003's two-bases-opposite-signs share series | **`MANUFACTURING_RATE`** (F5b) |

**⇒ Two segments grow, one does not, and the one that does not is the segment the theme is named
after.** That is A1b's falsification, priced: **the allocation follows the growth rather than
creating it.**

## 3. ⚠️ The Cursor acquisition is a strategy statement, and it is unresolved

**A $60B all-stock purchase by a loss-making issuer** ([8-K 2026-08-14, Item 2.01](https://agentii.ai/v/SPCX/sec9/2)) is a capital-allocation decision of the first
order — **and it is the one allocation whose terms the anchor cannot yet read.**

- **Round 4 made the headline PRO-FORMA**, so Cursor is **inside** the anchor
- **V-5 is `blocking`** because the dilution is not determinable
- **What it says strategically:** SPCX is buying a **software/AI developer-tools business** — not a
  launch asset, not a constellation. **The allocation is moving toward the AI segment's adjacency.**

**⇒ Recorded as a strategy fact with an unresolved term, not as a pending item.** The direction is
legible even though the magnitude is not, and **the direction is what the SOTP's AI-segment framing
must be consistent with.**

## 4. The assessment, in one paragraph

**SPCX's growth strategy is to convert external capital into compute and connectivity faster than
any competitor can, while its original business — launch — becomes an internal supply function.**
The filings support every clause: **coverage 0.10×** (external capital), **data centers named first**
(the destination), **customer share flat while the internal manifest grows** (launch's demotion), and
**a $60B software acquisition** (the direction of the next dollar). **None of it is a demand story.**
That is the finding, and it is why P5 is a *value* pillar rather than context: **the growth is
purchased, and the price of the purchase is the anchor's swing factor.**
````

## Artifact — artifacts/SPCX/2026-09-19_growth-strategy_organic-growth-driver-execution-assessment.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-5"
ticker: SPCX
skill: growth-strategy
mode: organic-growth-driver-execution-assessment
generated_at: 2026-09-19T13:05:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "ab94b90ee0ff"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-26"
    chosen_reading: "Execution is assessed on the FISCAL perio d the filing itself supports. The 10-Q carries 3M and 6M under one concept and axis, so a quarterly execution rate and a half-year rate are different measurements and are never blended into a trend line without naming both."
entity_claims:
  - claim_id: "oge-conn-revenue-q2-2026"
    ticker: SPCX
    metric: segment_revenue
    value: 4291000000
    unit: USD
    basis: "Connectivity segment, Q2 2026; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q spcx-20260630.htm — consumed via 003 and re-read here"
  - claim_id: "oge-conn-revenue-h1-2026"
    ticker: SPCX
    metric: segment_revenue
    value: 7548000000
    unit: USD
    basis: "Connectivity segment, H1 2026; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q spcx-20260630.htm"
key_metrics:
  conn_revenue_q2_2026_usd_m: 4291
  conn_revenue_h1_2026_usd_m: 7548
---

# SPCX × growth-strategy × organic-growth-driver-execution-assessment

**Is the organic driver being executed, or is it a strategy on paper?**

## 1. Three execution tests, each with a threshold

| # | Test | Evidence | Verdict |
|---|---|---|---|
| **E-1** | **Is the faster channel getting bigger as a share?** | Enterprise&Gov **867 → 1,806 (+108.3%)** vs Consumer **1,721 → 2,485 (+44.4%)** | ✅ **PASS** — the faster channel is growing faster *absolutely*, not just in rate |
| **E-2** | **Does the driver convert to operating income?** | Connectivity income from operations **+79.4%** on revenue **+65.8%** — **operating leverage, +13.6 pp of rate spread** | ✅ **PASS** — the only segment in the universe with **demonstrated operating leverage** |
| **E-3** | **Is the driver funded organically, or bought?** | Coverage **0.10×** — investing $(34,487)M vs operating +$3,466M | ❌ **FAIL as a capital test** — but it is the *wrong test for this driver*; see §3 |

**Two of three pass, and the failure is on a test the driver does not have to pass.**

## 2. The execution evidence, and its one soft spot

**Connectivity at 54.9% of revenue with a 38.6% operating margin is the strongest executed position
in the thesis.** The margin moved the right way **while the price fell** — ARPU −22.4% and margin
**up**. That is the definition of a mix shift being executed rather than suffered.

**⚠️ The soft spot, stated rather than smoothed:** the mix shift is partly a **price** decision.
**SPCX attributes the ARPU fall to *"international expansion and the addition of lower priced service
plans."*** So the execution is **buying volume with price** — and the test that would distinguish
*volume-bought-cheaply* from *volume-bought-at-a-loss* is the **margin**, which is **rising**. **On
the current filing the execution is working.** It would stop working if the margin flattened while
the cheaper cohort scaled, and **that is P2's falsifier**, not this artifact's.

## 3. ⚠️ Why E-3's failure is not an execution failure

**The capital test fails for the whole company, and it fails because of a different segment.**

| Segment | Its share of the investing outflow |
|---|---|
| **AI (compute buildout)** | **Named first** in the capex description; **the destination of the build** |
| Connectivity | An operator, largely built |
| Space | A supply function, capitalised into satellites in PP&E |

**⇒ The enterprise/government driver is not the thing consuming capital.** It is being executed from
an operating business that funds itself and more. **The 0.10× coverage is a statement about the AI
segment's build, not about Connectivity's execution.**

**This is the distinction that stops a correct figure being used to draw a wrong conclusion** — and
it is why the plan assigns the capital-intensity finding to **P5** and the operating-leverage finding
to **P2**. One number, two pillars, and **it means different things in each**.

## 4. Execution scorecard

| Driver | Executed? | Evidence | Bound |
|---|---|---|---|
| **Connectivity Enterprise&Gov** | ✅ **Yes** | 2.4× the consumer rate; margin **rising** while ARPU falls | `DEMAND` — P2's constraint |
| **Connectivity Consumer** | ✅ **Yes, as mix** | +44.4%, and the segment margin holds | ⚠️ Partly **bought with price** |
| **AI compute buildout** | ⚠️ **Capital-executed, value-unproven** | **1.4 GW IT load** (DA-11, unconvertible); capex named first | A4 / P3's admissibility ceiling |
| **Space** | ❌ **Not a growth driver** | Customer book **flat**; −1.9% H1; 8.29% of consolidated | `MANUFACTURING_RATE` |

## 5. Hand-off

| To | What |
|---|---|
| **P2** | ✅ **Execution confirmed on the operating test.** The pillar's remaining work is the **mix-shift vs price-erosion** separation, and the margin direction is the evidence it survives |
| **P5** | The capital test's failure belongs to **the AI build**, not to Connectivity. **State it that way or the finding is misattributed** |
| **P6** | Connectivity's row may carry a **margin-anchored** regime — its execution is the reason |
| **P3** | The AI buildout is **executed in capital and unproven in value**; the three framings (headline = invested capital) are the response |
````

## Artifact — artifacts/SPCX/2026-09-19_growth-strategy_organic-growth-drivers-analysis.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-5"
ticker: SPCX
skill: growth-strategy
mode: organic-growth-drivers-analysis
generated_at: 2026-09-19T13:00:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "ab94b90ee0ff"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-19"
    chosen_reading: "Organic growth is separated from entity change. The xAI merger (2026-02-02, common control) recasts prior periods, so any growth rate spanning it mixes organic expansion with an entity that was not previously inside the reporting entity. 001's finding is carried: '+$1,824M of new Space revenue is 48.7% of the quarter's growth and exists because an entity was acquired' — it is NOT organic."
  - da_id: "DA-10"
    chosen_reading: "ARPU is subscriber service revenue only, excluding enterprise, government, aviation and maritime. So a subscriber-count growth rate and an ARPU growth rate are computed over DIFFERENT populations and must never be combined without saying so."
entity_claims:
  - claim_id: "ogd-conn-entgov-q2"
    ticker: SPCX
    metric: segment_product_revenue
    value: 1806000000
    unit: USD
    basis: "Connectivity Enterprise & Government, Q2 2026, filed dimension; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "artifacts/SPCX/2026-09-19_revenue-decomp_methodology.md — this thesis's own, from spcx-20260630.htm"
  - claim_id: "ogd-conn-consumer-q2"
    ticker: SPCX
    metric: segment_product_revenue
    value: 2485000000
    unit: USD
    basis: "Connectivity Consumer, Q2 2026, filed dimension; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "artifacts/SPCX/2026-09-19_revenue-decomp_methodology.md"
key_metrics:
  conn_entgov_q2_2026_usd_m: 1806
  conn_consumer_q2_2026_usd_m: 2485
---

# SPCX × growth-strategy × organic-growth-drivers-analysis

**Which growth is organic, which is acquired, and which is a mix shift wearing growth's clothes.**

## 1. The organic driver — Enterprise & Government, and it is decisive

From `revenue-decomp`, this thesis's own work from the filing:

| Connectivity channel | H1 2025 | H1 2026 | Growth |
|---|---:|---:|---:|
| **Consumer** | 1,721 | **2,485** *(Q2)* | **+44.4%** |
| **Enterprise & Government** | 867 | **1,806** *(Q2)* | **+108.3%** |

**The managed channel grew 2.4× faster than consumer.** Both are **filed dimensions**, not
derivations.

**Why this is the cleanest organic signal at SPCX:**

1. **Both sides are filed** — the growth rate is not constructed over a mixed population
2. **Connectivity is wholly organic.** It has never been merged into; **003 recorded it as one of
   the two clean series** (with Space) that survive the entity boundary
3. **It is large** — Connectivity is 54.9% of revenue

## 2. ⚠️ The `DA-10` trap: the two growth rates are over DIFFERENT populations

**ARPU fell −22.4% ($85 → $66) while subscribers rose +101.2%.** Read together, that looks like
price erosion. **It is not that simple, and DA-10 is why:**

| Series | Population |
|---|---|
| **Subscriber count** | Consumer service lines |
| **ARPU** | **Subscriber service revenue only** — **excludes enterprise, government, aviation and maritime** |

**⇒ The subscriber series and the ARPU series do not cover the same customers.** The 12.0M
subscribers are consumer; the enterprise/government channel is *"disclosed as revenue but **not** as
subscribers"* (003's finding, confirmed). **So the ARPU decline cannot be attributed across the whole
business** — it is a statement about the consumer line only.

**And `subscribers × ARPU × 3` does NOT reproduce consumer revenue.** The identity does not close.
**Any growth decomposition that multiplies them is arithmetically wrong**, not merely approximate.

## 3. Non-organic growth, isolated

| Item | Amount | Organic? |
|---|---|---|
| **`+$1,824M` of new Space revenue** | 48.7% of the quarter's Space growth | ❌ **NOT organic** — 001's finding, carried: *"it exists because an entity was acquired"*. **This is the figure that must never be quoted as migration evidence** |
| **AI segment `+247.5%`** | — | ❌ **Contaminated** — xAI merged 2026-02-02 under common control; prior periods recast |
| **Connectivity +65.8% (Q2)** | — | ✅ **Organic** — never merged |
| **Space −1.9% (H1)** | — | ✅ **Organic, and falling** — the series that *survives* the boundary |

**⇒ Three of the four headline growth rates have an entity-boundary problem.** The two that do not
are **Connectivity (organic, growing)** and **Space (organic, falling)** — which is exactly why the
plan's **V-4** rests the migration claim on those two.

## 4. What "organic growth" means at SPCX, stated plainly

**The organic growth is a MIX SHIFT inside Connectivity, not a volume expansion of the whole
business.**

- Consumer grew **+44.4%** — real, but slower
- Enterprise & Government grew **+108.3%** — real, and faster
- The **blend** is the +65.8% segment rate

**⇒ The driver is channel mix, and it is favourable** — the higher-value channel is the faster-growing
one. **But it is not a rising tide**, and P2's operating-leverage claim must rest on **the mix
moving toward the better channel**, not on scale alone.

## 5. Hand-off

| To | What |
|---|---|
| **P2** | The organic driver is **channel mix toward Enterprise & Government**; the DA-10 readings must be reported side by side, and the identity that fails must be named as failing |
| **P5** | Organic growth does not fund the build — **coverage 0.10×**. The organic story is real and **irrelevant to the capital question**, which is the point |
| **P3** | The AI growth rate is **contaminated**; the market-implied limb (`reverse-dcf`, Phase 7) is the admissible read |
````

## Artifact — artifacts/SPCX/2026-09-19_revenue-decomp_defaults.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-2/PIL-3/PIL-4"
ticker: SPCX
skill: revenue-decomp
mode: defaults
generated_at: 2026-09-19T11:30:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "037b396ab004"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-26"
    chosen_reading: "Where a duration is not stated in the fact itself, the default is to READ IT FROM the period_start/period_end pair rather than infer it from row position — 002 registered that the mislabelled period varies by issuer and cannot be screened positionally."
entity_claims:
  - claim_id: "rdf-closure-residual-zero"
    ticker: SPCX
    metric: segment_closure_residual
    value: 0
    unit: USD
    basis: "Connectivity child-sum 4,633 + 2,915 = 7,548 vs filed parent 7,548; 6M duration, six months ended 2026-06-30. CLOSES EXACTLY"
    period: "2026Q2"
    evidence_grade: DERIVED
    source: "SPCX 10-Q spcx-20260630.htm p.13 (Note 3) — arithmetic on filed cells"
key_metrics:
  connectivity_closure_residual_usd_m: 0
  conn_entgov_h1_2026_usd_m: 2915
---

# SPCX × revenue-decomp × defaults

**The default assumptions used where no filed figure exists.** Every default below is one the
filer does not settle, and each is stated so a reader can disagree with it explicitly rather than
inherit it silently.

## D-1 — There is NO closure residual. The earlier ±$1M was a transcription error, not rounding

**Where it appeared:** Connectivity, 6M. An earlier draft read the Enterprise & Government child as
`2,914`, giving `4,633 + 2,914 = 7,547` against a filed parent of `7,548` — a **$1M residual**.

**The filed child is `2,915`.** Read from the source rather than re-read from the draft:

> `Consumer 4,633 + Enterprise & Government 2,915 = Connectivity 7,548` — **exact**.
> Source: [SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13) (Note 3, revenue disaggregated by type
> and segment, six months ended 2026-06-30).

| | |
|---|---|
| **What was defaulted** | Nothing. A **phantom** `$1M` cell was described as *"rounding within $M-denominated filing"* |
| **Why the correction matters** | The artifact had already **constructed a default (D-1) to absorb a number that does not exist** — and a default is the one construct a reader cannot falsify, because it is a reading rather than a filed claim |
| **How it was caught** | By reading p.13 directly. The residual **could not have been caught by closure testing**, because closure was tested against the same wrong child it was derived from |
| **What would overturn the correction** | A filed E&G figure of `2,914` for 6M 2026 anywhere in the filing. It does not appear |
| **Class** | `DERIVED` — arithmetic on filed cells |

> ### ⚠️ This is the same defect class the report is about, one level up.
>
> **A fabricated residual is worse than a fabricated figure.** A figure can be checked against the
> filing; a *default* is a stated reading of an ambiguity, so **it can only be checked against the
> ambiguity** — and there was none. The artifact spent a page explaining how to treat a gap that
> the filing closes exactly.
>
> **Recorded rather than deleted**, because the correction is the finding: **a thesis that reads its
> own prior drafts instead of the source will manufacture residuals, and then build defaults to
> absorb them.** Every closure test in this skill now reads p.13.

## D-2 — The product axis is assumed EXHAUSTIVE, and the assumption is tested

**Where:** every closure test.

**Default:** the assumption that `srt:ProductOrServiceAxis` members are a **partition** of each
segment — that no revenue is unfiled.

**Why it is a default and not a fact:** XBRL does not declare a dimension exhaustive. The filer
could in principle file less than the whole.

**How it is tested:** the **closure test is the test of the assumption.** If the children summed to
less than the parent, the axis would be non-exhaustive and the gap would be unfiled revenue.
**They sum to the parent in all three segments and at consolidation.** So the assumption is
**confirmed by arithmetic**, not merely asserted.

**What would overturn it:** any period where `Σ(children) < parent` by more than rounding. **That
would be a finding — unfiled revenue — not a bookkeeping error.**

## D-3 — Which of the two served forms to take

**Where:** every segment fact.

**Default:** take the fact carrying `srt:ConsolidationItemsAxis = us-gaap:OperatingSegmentsMember`;
**never sum across the pair.**

**Why a default is needed at all:** the platform serves each segment figure **twice**, once with
that dimension and once without, at the same value. **Nothing in the response marks one as
canonical.**

**Why the dimensioned form:** it states *which consolidation item the figure belongs to* — the
information needed to know the fact is a segment subtotal and not a consolidated total that
happens to equal it.

**Cost of getting it wrong:** summing both forms gives **exactly double**. Recorded in
`retrieval-scope` §"the de-duplication trap".

## D-4 — Duration is read from the fact, never inferred from position

**Where:** choosing 3M vs 6M throughout.

**Default:** read `period_start`/`period_end` off the fact itself.

**Why:** 001 and 002 both registered period traps — **DA-26** (an annual-basis fact served where a
quarterly label is asserted, universal across 19 of 19 issuers, with the mislabelled period
**varying by issuer**) and **DA-27** (calendar-derived fiscal labels). **Row position is not a
usable proxy.** SPCX files 3M and 6M under the same concept and the same axes, so a positional
reading would silently mix them.

**Application:** every figure in this skill's artifacts names its duration in `basis`, and the
machine-readable `period` field carries `2026Q2` for both durations — which is why the duration
label is **not optional** in `basis`.

## D-5 — No default is taken where a filed figure exists

Stated as a negative, because it is the discipline that makes the other four meaningful:

| Question | Default taken? |
|---|---|
| How much did Connectivity Consumer earn in H1? | **No** — filed, `4,633` |
| Did that split exist? | **No** — filed as a dimension, not inferred |
| Which segment does `ConsumerMember` belong to? | **No** — the fact carries `spcx:ConnectivityMember` |
| What is aviation revenue? | **No default is available.** Recorded `UNRESOLVABLE-FROM-PUBLIC-SOURCES`. **Inventing one would be the failure this section exists to prevent** |

## Summary

| # | Default | Grade | Overturned by |
|---|---|---|---|
| D-1 | **No residual exists** — the earlier ±$1M was a transcription error | `DERIVED` | A filed E&G of `2,914`; it does not appear |
| D-2 | The product axis is exhaustive | `MODELED`, **arithmetically confirmed** | `Σ(children) < parent` beyond rounding |
| D-3 | Take the dimensioned served form | `DERIVED` | A response marking a canonical form |
| D-4 | Duration read from the fact | `DERIVED` | — (this is the safe reading, not a guess) |
| D-5 | No default where a figure is filed | — | — |

**Four defaults survive and one is retracted.** The retraction is the substantive result: **three
segments and the consolidated total now close on filed cells alone, with no reading of ours
anywhere in the closure chain.**
````

## Artifact — artifacts/SPCX/2026-09-19_revenue-decomp_methodology.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-2/PIL-3/PIL-4"
ticker: SPCX
skill: revenue-decomp
mode: methodology
generated_at: 2026-09-19T11:05:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "037b396ab004"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "Issuer-defined segment boundaries taken as filed, then decomposed ONE level deeper on the filer's OWN axis (srt:ProductOrServiceAxis). The deep cut is not our taxonomy — it is the filer's, read from XBRL dimensions. This is what spec §3a requires: 'derive the cuts from the filings, do not pre-declare a taxonomy.'"
  - da_id: "DA-26"
    chosen_reading: "Period labels — the 10-Q carries both 3M (quarter ended 2026-06-30) and 6M (six months ended 2026-06-30) durations under the SAME concept and axis. Every figure below names its duration. A 3M figure is never compared to a 6M figure."
  - da_id: "DA-23"
    chosen_reading: "Not engaged. This artifact reads REVENUE only, which carries no sign-strip exposure at SPCX (the DA-23 census found the defect in OperatingIncomeLoss, 16 of 20 served facts). Stated so its absence is a decision, not an oversight."
entity_claims:
  - claim_id: "rd-space-launchservices-h1-2026"
    ticker: SPCX
    metric: segment_product_revenue
    value: 978000000
    unit: USD
    basis: "filed, segment x product-or-service; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax x srt:ProductOrServiceAxis=spcx:LaunchServicesMember x us-gaap:StatementBusinessSegmentsAxis=spcx:SpaceMember"
  - claim_id: "rd-space-launchanddev-h1-2026"
    ticker: SPCX
    metric: segment_product_revenue
    value: 603000000
    unit: USD
    basis: "filed, segment x product-or-service; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=spcx:LaunchAndDevelopmentMember x spcx:SpaceMember"
  - claim_id: "rd-conn-consumer-h1-2026"
    ticker: SPCX
    metric: segment_product_revenue
    value: 4633000000
    unit: USD
    basis: "filed, segment x product-or-service; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=spcx:ConsumerMember x spcx:ConnectivityMember"
  - claim_id: "rd-conn-entgov-h1-2026"
    ticker: SPCX
    metric: segment_product_revenue
    value: 2915000000
    unit: USD
    basis: "filed, segment x product-or-service; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=spcx:EnterpriseAndGovernmentMember x spcx:ConnectivityMember"
  - claim_id: "rd-ai-solutions-h1-2026"
    ticker: SPCX
    metric: segment_product_revenue
    value: 2669000000
    unit: USD
    basis: "filed, segment x product-or-service; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=spcx:AISolutionsAndInfrastructureMember x spcx:AIMember"
  - claim_id: "rd-ai-advertising-h1-2026"
    ticker: SPCX
    metric: segment_product_revenue
    value: 710000000
    unit: USD
    basis: "filed, segment x product-or-service; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=us-gaap:AdvertisingMember x spcx:AIMember"
  - claim_id: "rd-nature-service-h1-2026"
    ticker: SPCX
    metric: consolidated_revenue_by_nature
    value: 11667000000
    unit: USD
    basis: "filed, consolidated x product-or-service NATURE; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=us-gaap:ServiceMember"
  - claim_id: "rd-nature-product-h1-2026"
    ticker: SPCX
    metric: consolidated_revenue_by_nature
    value: 841000000
    unit: USD
    basis: "filed, consolidated x product-or-service NATURE; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=us-gaap:ProductMember"
key_metrics:
  space_launch_services_h1_2026_usd_m: 978
  space_launch_and_dev_h1_2026_usd_m: 603
  conn_consumer_h1_2026_usd_m: 4633
  conn_entgov_h1_2026_usd_m: 2915
  ai_solutions_h1_2026_usd_m: 2669
  ai_advertising_h1_2026_usd_m: 710
---

# SPCX × revenue-decomp × methodology

**The derivation path, stated so the numbers are reproducible.** Spec §3a requires the cut *inside*
each segment to be **derived from the filings, not declared by us.** This artifact establishes
which cuts the filer actually reports, proves each closes, and records the cuts that do **not**
exist — with their disposition class rather than silence.

> **⚠️ ROUND 4 OF THE PLAN SAID THESE CUTS WERE "NOT FORMABLE". THAT WAS WRONG, AND THIS ARTIFACT
> IS THE CORRECTION.** Plan finding **F7** concluded: *"`aviation` and `maritime` appear twice in
> all nine SPCX artifacts, as prose, with no revenue figure attached"* — **true, and it stopped
> there.** The filer's actual decomposition was in the **XBRL dimensional axes**, which none of
> 003's nine SPCX artifacts queried. **The correct conclusion is the opposite of "not formable":
> SPCX files a THREE-LEVEL revenue decomposition** — segment, then product-or-service within each
> segment, then a consolidated product/service nature split. **This is the single most consequential
> input to P2, P3 and P4 after the segment note itself.**

## 1. The axis, and why it settles the question

`srt:ProductOrServiceAxis` is filed at SPCX with these members:

| Member | Segment it sits in |
|---|---|
| `spcx:LaunchServicesMember` | Space |
| `spcx:LaunchAndDevelopmentMember` | Space |
| `spcx:ConsumerMember` | Connectivity |
| `spcx:EnterpriseAndGovernmentMember` | Connectivity |
| `spcx:AISolutionsAndInfrastructureMember` | AI |
| `us-gaap:AdvertisingMember` | AI |
| `us-gaap:ServiceMember` | *(consolidated — cross-segment nature)* |
| `us-gaap:ProductMember` | *(consolidated — cross-segment nature)* |

**Eight members across two axes uses.** The six segment-scoped members are the deep cut; the two
nature members are a separate, consolidated reading of the same axis. **They are not alternatives
and neither is a substitute for the other.**

## 2. The matrix, H1 2026 — every level closes

Duration basis: **6M, six months ended 2026-06-30.** Units USD millions, as filed.

| Segment | Segment total | Product-or-service cut | Sum | Closes |
|---|---:|---|---:|---|
| **Space** | **1,581** | Launch Services **978** + Launch & Development **603** | 1,581 | ✅ **exact** |
| **Connectivity** | **7,548** | Consumer **4,633** + Enterprise & Government **2,915** | 7,548 | ✅ **exact** |
| **AI** | **3,379** | AI Solutions & Infrastructure **2,669** + Advertising **710** | 3,379 | ✅ **exact** |
| **Σ segments** | **12,508** | | 12,508 | ✅ **exact** |
| **Consolidated by nature** | **12,508** | Service **11,667** + Product **841** | 12,508 | ✅ **exact** |

> ### ⚠️ CORRECTION — `2,914` → `2,915`, AND THERE IS NO RESIDUAL
>
> The first draft read Enterprise & Government as **2,914**, which produced `7,547` against a filed
> parent of `7,548` — a **$1M residual** — and the artifact then reported closure as *"✅ ±1
> (rounding)"* **at three levels**. The filed child is **2,915**:
> **every row closes exactly, and the ±1 is gone.**
> Source: [SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13).
>
> **Caught by re-reading the filing rather than re-reading this table.** The error propagated into
> `defaults` D-1, which had constructed a default to absorb it, and into `metrics.json` as
> `connectivity_closure_residual_usd_m: 1`. **A closure chain with a rounding allowance anywhere in
> it cannot detect an error, because the allowance absorbs exactly the error it would surface.**

**Three independent closures, and the same 12,508 reached by two different routes** — the segment
sum and the nature split. **That is the derivation's own check**: if the deep cut were a taxonomy
we had imposed, it would not close to the filer's own totals. **With the ±1 removed, the check is
now exact rather than near-exact, which is the only form in which it can fail loudly.**

## 3. The same matrix, Q2 2026 — for period discipline (DA-26)

Duration basis: **3M, quarter ended 2026-06-30.** **Never compared against §2.**

| Segment | Segment total | Product-or-service cut | Sum | Closes |
|---|---:|---|---:|---|
| **Space** | **962** | Launch Services **648** + Launch & Development **314** | 962 | ✅ **exact** |
| **Connectivity** | **4,291** | Consumer **2,485** + Enterprise & Government **1,806** | 4,291 | ✅ **exact** |
| **AI** | **2,561** | AI Solutions & Infrastructure **2,194** + Advertising **367** | 2,561 | ✅ **exact** |
| **Σ segments** | **7,814** | | 7,814 | ✅ **exact** |
| **Consolidated by nature** | **7,814** | Service **7,353** + Product **461** | 7,814 | ✅ **exact** |

**The two durations are filed under the same concept and the same axes.** Without the duration
label in-line, `978` and `648` are the same number presented twice. **DA-26 is live here, and this
artifact names its duration on every row.**

## 4. What this changes for P2, P3 and P4

**P2 — Connectivity.** 003's map had Consumer and Enterprise&Government from the MD&A. **This is
the XBRL source beneath it, and it confirms 003's figures** (Consumer Q2 **2,485** and
Enterprise&Government Q2 **1,806** match 003's `secular-trends` artifact exactly). The mix-shift
question — *is the −22.4% ARPU decline price erosion or mix shift?* — now has a **filed revenue
basis on both sides of the channel line**, which is stronger than the ARPU series alone.

**P4 — Space standalone.** This is the find that matters most. The plan treated Space as a single
revenue line. **The filer splits it: `LaunchServices` vs `LaunchAndDevelopment`.** For H1 2026 that
is **978 vs 603** — **launch services is 61.9% of the segment and 7.82% of consolidated revenue**;
on the Q2 basis, **648 of 962, or 8.29% of consolidated** — *which is the figure 003's map derived
independently.* **P4's "separable from Starship funding" test now has a filed numerator**, and the
"launch-only" reading is no longer a derived share but a **filed line item.**

**P3 — AI.** The plan's V-3 asked *"is the AI segment homogeneous enough to carry one multiple?"*
and named Grok, X-advertising and compute as the aggregation risk. **The filer splits it two ways,
not three: `AISolutionsAndInfrastructure` 2,669 and `Advertising` 710.** So **the homogeneity
question is sharper than the plan assumed** — advertising is **21.0% of the segment** and is a
genuinely different business from compute, while **Grok and compute are NOT separately filed.**
V-3 is partly answered and partly bounded: *the advertising limb is separable and should be carried
separately; the Grok/compute limb is not separable from public disclosure.*

## 5. Cuts that do NOT exist — named, with their class

| Intended cut | Status | Evidence |
|---|---|---|
| **aviation, maritime** | ❌ **NOT FORMABLE** | Both appear **twice in all nine SPCX artifacts**, as qualitative prose only — *"domains including aviation, maritime, land mobility, fixed sites, and government entities."* **No revenue figure is attached to either.** They sit inside the `EnterpriseAndGovernmentMember` line, which is the finest granularity the filer reports |
| **Grok vs compute** | ❌ **NOT separately filed** | The AI segment splits two ways. Both Grok and compute sit inside `AISolutionsAndInfrastructureMember` (2,669). `UNRESOLVABLE-FROM-PUBLIC-SOURCES` for a further split |
| **Subscribers / ARPU by channel** | ❌ `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | 003 recorded it: managed enterprise/government is *"disclosed as revenue but **not** as subscribers."* **Revenue decomposes; the subscriber denominator does not** — so a per-channel ARPU cannot be computed |
| **Falcon vs Starship** | ❌ `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | `LaunchServicesMember` mixes vehicles. No vehicle-level revenue line is filed |
| **Geographic split** | ⚠️ **not yet queried** | No `srt:StatementGeographicalAxis` fact appeared in the queries run for this artifact. **Recorded as unqueried, not as absent** — absence needs its own negative search |

> **`NON-FORMABLE` is not `PASS`** (003's F16). Each row above is recorded with the class and, where
> one exists, the disclosure that would resolve it.

## 6. Method — reproducible in four steps

```bash
# 1. Which product-or-service members does the filer use? Read the DIMENSIONS, not the values.
search_xbrl_facts(ticker="SPCX",
                  concept="RevenueFromContractWithCustomerExcludingAssessedTax",
                  view="detailed", fiscal_year=2026)
# → returns srt:ProductOrServiceAxis members, each paired with a segment where scoped

# 2. Cross each member against its segment total (StatementBusinessSegmentsAxis).
# 3. Prove closure: Σ(children) == parent, per segment AND at consolidation.
# 4. Name the duration (DA-26) on every figure — 3M and 6M share concept and axis.
```

**⚠️ DO NOT route this through `get_segment_data`.** It hard-errors at SPCX
(`column "k" does not exist`). **003's plan recorded this first** (F4, from 002 §7), with a fuller
diagnosis: it *"reports a `total_revenue` summing served facts across two years and two durations
with no de-duplication — `segment_coverage_pct 116.2` masking a 302.1% overlap."*
**`search_xbrl_facts(view=detailed)` is the working route**, and it is the route this artifact used.

**A note on the `srt:ConsolidationItemsAxis`.** Most segment facts carry
`us-gaap:OperatingSegmentsMember` as well. **Facts appear twice — with and without it — carrying
the same value.** Both were observed above (`7,548` and `4,291` each appear twice). **Take the
dimensioned one**, which names which consolidation item the figure belongs to, and do not sum
across the pair.

## 7. Sources

| Source | What it supplied |
|---|---|
| `SPCX 10-Q, spcx-20260630.htm` (filing `34ca500a-5978-4820-ad0f-fce2f39dfab6`) | Every figure in §2 and §3, as `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` under `srt:ProductOrServiceAxis` × `us-gaap:StatementBusinessSegmentsAxis` |
| `003/_cross/value-pool-map.md` § E-01/E-02/E-03, § 0 sub-finding 4 | The segment totals this decomposition reconciles to, and the independently-derived `8.29%` launch-only share |
| `003/artifacts/SPCX/2026-09-19_1345_secular-trends_methodology.md` | Consumer 2,485 / Enterprise&Government 1,806 (Q2) — **matched exactly** |
| `003/plan.md` § F4, from 002 §7 | The `get_segment_data` verdict and the routing instruction |
````

## Artifact — artifacts/SPCX/2026-09-19_revenue-decomp_retrieval-scope.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-2/PIL-3/PIL-4"
ticker: SPCX
skill: revenue-decomp
mode: retrieval-scope
generated_at: 2026-09-19T11:20:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "037b396ab004"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "Source admission is judged by whether a datum sits on the FILER's own dimensional axes. A cut we construct ourselves is not admitted, however arithmetically sound — it is a taxonomy, not a decomposition."
entity_claims:
  - claim_id: "rs-segment-axes-admitted-count"
    ticker: SPCX
    metric: admitted_dimensional_axes
    value: 3
    unit: count
    basis: "axes carrying segment-scoped revenue facts admitted for the deep cut; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q spcx-20260630.htm — dimensional enumeration via search_xbrl_facts(view=detailed)"
key_metrics:
  admitted_dimensional_axes: 3
---

# SPCX × revenue-decomp × retrieval-scope

**Which sources are admitted, and which are excluded.** Spec §3a requires the deep cut to be
*derived from the filings*; this artifact states the admission rule that makes "derived" mean
something, and names what it excludes.

## The admission rule — one test

> **A cut is ADMITTED if and only if the filer files a dimension for it. A cut we construct by
> arithmetic on other cuts is NOT admitted, however sound the arithmetic.**

**Why the rule is strict:** the whole point of `revenue-decomp` is to see the business the way the
issuer reports it, so that later multiples attach to *filed* segments rather than to our model of
them. A constructed cut would let us decompose SPCX into whatever shape suited the valuation —
which is precisely the freedom the constitution removes by fixing segment boundaries at DA-21.

## Admitted

| Source | Status | What it supplies | Why admitted |
|---|---|---|---|
| **`spcx-20260630.htm`** (10-Q, filing `34ca500a-…`) | ✅ **PRIMARY** | All six segment-scoped revenue cuts and both nature cuts | It is the filing. **Every figure in the methodology artifact traces to this single document** |
| `srt:ProductOrServiceAxis` | ✅ admitted | The filer's own product/service dimension | **This is the decomposition.** Not a proxy for it |
| `us-gaap:StatementBusinessSegmentsAxis` | ✅ admitted | Segment scope for each cut | Establishes which segment a product-cut belongs to |
| `srt:ConsolidationItemsAxis` | ✅ admitted, **with a de-duplication rule** | Names which consolidation item a fact belongs to | Admitted **only in its dimensioned form.** The same value is served with and without `OperatingSegmentsMember`; **taking both double-counts.** See the trap below |
| **`003/artifacts/SPCX/…`** (nine artifacts) | ✅ admitted as **cross-check only** | Independent derivations of the same figures | Admitted to *confirm*, never to *supply*. Used once: 003's Consumer 2,485 / Enterprise&Gov 1,806 matched this artifact's figures exactly, which validates both |

## Excluded

| Source | Why excluded |
|---|---|
| **`get_segment_data`** | ❌ **Unusable at the platform level.** Hard-errors at SPCX (`column "k" does not exist`) and elsewhere sums served facts across two years and two durations with no de-duplication. **003's plan recorded this first** (F4, from 002 §7). Its `segment_coverage_pct 116.2` masks a **302.1% overlap** |
| **MD&A narrative prose** | ❌ **Not excluded as a source — excluded as a DENOMINATOR.** It is read for *naming* (it is where "aviation, maritime" appear) but a figure quoted only in prose is not a filed cut. **This distinction is why the plan's F7 went wrong**: it correctly found the prose and incorrectly concluded no decomposition existed |
| **A constructed aviation/maritime split** | ❌ **Constructed, not filed.** Both sit inside `EnterpriseAndGovernmentMember`. Splitting them out would require an allocation assumption with no filed basis |
| **Analyst / third-party segment estimates** | ❌ Outside the filing. A segment shape imposed by a sell-side model is not the filer's |
| **Non-XBRL-derived segment tables** | ❌ Any figure not traceable to a dimensioned fact in `spcx-20260630.htm` |
| **The 1-million-satellite / 100 kW-per-tonne filing** | ❌ **A4: a filed aspiration with no revenue line.** Inadmissible as a valuation input, and it carries no segment revenue to decompose |

## ⚠️ The de-duplication trap — admitted source, double-counted result

Facts are served **twice**: once with `srt:ConsolidationItemsAxis = us-gaap:OperatingSegmentsMember`
and once without it, **carrying the same value.** Measured in this artifact's own queries:

- Connectivity segment revenue `7,548` (6M) and `4,291` (3M) — **each appears twice**
- AI segment revenue `3,379` (6M) and `2,561` (3M) — **each appears twice**
- Space segment revenue `1,581` (6M) and `962` (3M) — **each appears twice**

**Admitting both forms and summing gives exactly double the segment total.** The rule: **take the
dimensioned form**, which states which consolidation item the figure belongs to, and never sum
across the pair. This is the arithmetic cousins of the defect that made `get_segment_data`
unusable — the same data, the same double-service, caught here by hand instead.

## What is NOT decided here

Whether the *excluded* cuts would be material if obtainable. That is a **bound recorded with its
class**, not a gap: aviation and maritime sit inside a filed line; a further split is
`UNRESOLVABLE-FROM-PUBLIC-SOURCES`, not "unknown".
````

## Artifact — artifacts/SPCX/2026-09-19_revenue-decomp_retrieval-strategy.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-2/PIL-3/PIL-4"
ticker: SPCX
skill: revenue-decomp
mode: retrieval-strategy
generated_at: 2026-09-19T11:25:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "037b396ab004"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "The decomposition was located by reading the filer's DIMENSIONS, not its values. The search is stated as a query so it repeats, and the negative result (which axes are absent) is recorded with the same fidelity as the positive one."
entity_claims:
  - claim_id: "rst-deep-cut-found-at-query-1"
    ticker: SPCX
    metric: retrieval_queries_to_find_deep_cut
    value: 1
    unit: count
    basis: "queries required to surface srt:ProductOrServiceAxis; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "self-reported search trace; reproducible via the query in §1"
key_metrics:
  retrieval_queries_to_find_deep_cut: 1
---

# SPCX × revenue-decomp × retrieval-strategy

**How the sources were located, so the search repeats.** This artifact exists because the plan's
own retrieval **failed and did not know it** — see §4.

## 1. The query that found the decomposition, in full

```python
search_xbrl_facts(
    ticker="SPCX",
    concept="RevenueFromContractWithCustomerExcludingAssessedTax",
    view="detailed",        # ← THE LOAD-BEARING PARAMETER
    fiscal_year=2026,
    page_size=40)
```

**The whole find turns on `view="detailed"`.** The default is `view="standard"`, which
**collapses dimensionality** and returns one consolidated number per period. Under the default,
SPCX's revenue is `12,508` (6M) and `7,814` (3M) and the six segment-scoped cuts are **invisible**.

**One query was sufficient.** No iteration, no widening, no fallback. That is worth stating: the
decomposition was not hard to find, it was **hard to know to look for** — and the plan looked in
the wrong place (§4).

## 2. The read order, and why it is this order

1. **Read the DIMENSIONS before the VALUES.** The first pass reads only which axes and members are
   present, ignoring every number. This is what surfaced `srt:ProductOrServiceAxis` and its eight
   members.
2. **Pair each product member to its segment** via `us-gaap:StatementBusinessSegmentsAxis`, which
   most product facts also carry.
3. **Then** read values, and immediately test closure (§3 of the methodology artifact).
4. **Only then** compare against 003.

> **Why dimensions first:** if you read values first, the two served forms of the same fact
> (`7,548` twice — with and without `ConsolidationItemsMember`) look like **two different segment
> totals**, and the natural move is to reconcile them. **There is nothing to reconcile.** Reading
> structure first makes the duplication visible as structure rather than as a numerical puzzle.

## 3. The negative searches — recorded, not omitted

A search that returns nothing is a finding **only if it was actually run.** These were:

| Search | Result | Consequences |
|---|---|---|
| `srt:StatementGeographicalAxis` in the 30 facts returned | **0 occurrences** | ⚠️ **Recorded as UNQUERIED, not as ABSENT.** 30 facts is one page of a 30-row result; a geography axis could exist unexamined. **Stated as a bound, because "we did not see it" and "it is not filed" are different claims** |
| Any axis splitting `AISolutionsAndInfrastructureMember` further | **0 occurrences** | Grok and compute are not separately filed |
| Any axis splitting `EnterpriseAndGovernmentMember` into aviation / maritime | **0 occurrences** | Consistent with 003's finding that both appear only as prose |
| Vehicle-level splits (Falcon vs Starship) inside `LaunchServicesMember` | **0 occurrences** | Not filed |
| `get_segment_data(ticker="SPCX", segment_type="product")` | ❌ **HARD ERROR** — `column "k" does not exist` | The obvious route is broken. **003 recorded this first** |

## 4. ⚠️ Why the plan's own retrieval failed — the reusable lesson

**The plan searched 003's artifacts for the cut, and correctly concluded it was not there.**

> F7: *"`aviation` and `maritime` appear twice in all nine SPCX artifacts, as prose, with no revenue
> figure attached."*

**Every word of that is true.** The error was **inferring absence from a search of the wrong
corpus.** 003 built a *margin* map across nine issuers — it read the segment note and the MD&A,
and it had no reason to enumerate `srt:ProductOrServiceAxis`. **So a cut absent from 003's nine
artifacts is not a cut absent from the filing.**

| | |
|---|---|
| **The failing shape** | Treating a **downstream synthesis** as the primary source for a **disclosure question** |
| **The correct shape** | Disclosure questions are answered from **the filing's own XBRL**; syntheses are read to **cross-check**, never to bound |
| **The generalisable rule** | **"Not in the consumed artifacts" ≠ "not filed."** A consumed artifact is a *reading* of the filing, taken for someone else's purpose |

**This cost one plan round and produced a wrong finding (F7) that stood in the spec until the first
artifact contradicted it.** It is recorded here rather than in the artifact's prose because it is a
**method** defect, and the method is what this mode carries.

## 5. Reproducing this artifact

```bash
# 1. surface the axes (the query in §1)
# 2. read members, ignore values
# 3. read values, test closure per segment AND at consolidation
# 4. cross-check against 003 — confirm only, never bound
```

**Expected output:** six segment-scoped cuts, two nature cuts, three closures (§2 of the
methodology artifact), and the five negative results in §3.
````

## Artifact — artifacts/SPCX/2026-09-19_revenue-decomp_triggers.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-2/PIL-3/PIL-4"
ticker: SPCX
skill: revenue-decomp
mode: triggers
generated_at: 2026-09-19T11:35:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "037b396ab004"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "A trigger is a specific, checkable event — not a risk category. Each row names the datum to read and the threshold, so the check runs without interpretation. Modelled on the plan's own convention and 003's F16 rule that NON-FORMABLE is not PASS."
entity_claims:
  - claim_id: "rdt-trigger-count"
    ticker: SPCX
    metric: falsifier_count
    value: 6
    unit: count
    basis: "checkable triggers over the decomposition finding; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: MODELED
    source: "this artifact — the trigger set itself"
key_metrics:
  falsifier_count: 6
---

# SPCX × revenue-decomp × triggers

**What would overturn the decomposition finding.** The finding under test is:

> **SPCX files a three-level revenue decomposition — segment, then product-or-service within each
> segment, then a consolidated service/product nature split — and every level closes.**

Six triggers. Each names **the datum to read** and **the threshold**, so it fires mechanically
rather than on judgement.

## T-1 — A product member disappears or is renamed

**Read:** the `srt:ProductOrServiceAxis` member list in the next 10-Q or 10-K.
**Threshold:** the list is **not** {LaunchServices, LaunchAndDevelopment, Consumer,
EnterpriseAndGovernment, AISolutionsAndInfrastructure, Advertising} — or the segment pairing of
any member changes.

**Why it matters:** the decomposition is the filer's, so its *stability* is the claim. A renamed
or dropped member means the taxonomy is being managed — and a managed taxonomy is a weaker
foundation for a multiple than a stable one. **A member moving between segments would be the
strongest version of this trigger**, because it would show the boundary is discretionary.

## T-2 — Closure fails

**Read:** `Σ(children)` vs the filed segment parent, per segment, per duration.
**Threshold:** a residual **larger than $1M**, or one that **persists across two consecutive
quarters**.

**Why the $1M and the persistence test:** one $1M cell is rounding (default **D-1**). A residual
that survives a quarter is a cut we have not found. **Firing means the decomposition is
incomplete**, and every multiple built on it inherits the gap.

## T-3 — The two served forms diverge

**Read:** the dimensioned and undimensioned values of the same segment fact.
**Threshold:** the two differ.

**Why:** default **D-3** takes the dimensioned form on the reasoning that the pair carries one
value. **If they ever differ, that reasoning is void** and the choice of form becomes a real
decision — on data that currently presents itself as a non-choice.

## T-4 — A new axis appears

**Read:** the full dimensional enumeration for the revenue concept.
**Threshold:** an axis not previously seen — **`srt:StatementGeographicalAxis` above all**.

**Why:** §3 of `retrieval-strategy` records geography as **UNQUERIED, not ABSENT** — 30 of 30
returned facts carried no such axis, but absence was never established. **A geographic split would
materially change P2** (international expansion is SPCX's stated ARPU driver) and **P3**
(where compute is deployed).

## T-5 — The AI segment splits further

**Read:** whether `spcx:AISolutionsAndInfrastructureMember` (2,669 · 6M) gains sub-dimensions.
**Threshold:** Grok and compute become separately filed.

**Why:** plan finding **V-3** asks *"is the AI segment homogeneous enough to carry one multiple?"*
and this artifact's answer is **partial**: **advertising is separable (710 of 3,379 = 21.0%)**, but
**Grok and compute are not**. **T-5 firing converts P3's partial answer into a full one** — and
would let the two limbs carry different treatments rather than one blended framing.

## T-6 — A common-control recast moves the prior periods

**Read:** whether SPCX restates earlier-period revenue cuts.
**Threshold:** any restatement of a period used in this skill's artifacts.

**Why:** **DA-19.** The xAI merger (2026-02-02) recast prior periods under common control, and the
plan's **V-4** found **Space is the one series that survives the entity boundary**. **A further
recast would not necessarily invalidate the decomposition — but it would invalidate every
growth rate computed across it**, which is why the trigger is on restatement and not on level.

## Trigger summary

| # | Datum | Threshold | Fires ⇒ |
|---|---|---|---|
| **T-1** | product-member list | changed set or pairing | taxonomy is managed; multiples weaken |
| **T-2** | closure residual | >$1M or persisting | decomposition incomplete |
| **T-3** | dimensioned vs undimensioned | any divergence | D-3's reasoning void |
| **T-4** | axis enumeration | a new axis, esp. geography | the cut can be extended |
| **T-5** | AI sub-dimensions | Grok/compute split | V-3 fully answered |
| **T-6** | prior-period restatement | any | growth rates across the boundary void |

## What this set does NOT trigger on

Stated so the boundary is explicit:

- **A change in the LEVEL of any cut.** Revenue can halve inside `AdvertisingMember` without
  touching this finding — the decomposition question is *what is filed*, not *how much*.
- **A change in the segment structure itself** (three segments becoming two). That is a **different
  claim** — plan finding **V-1** and **P1**'s separability test — and it fires *those*, not this.
- **Anything in the prose.** §4 of `retrieval-strategy` records why prose is the wrong place to
  look: it is where aviation and maritime appear, and where the plan wrongly concluded absence.
````

## Artifact — artifacts/SPCX/2026-09-19_reverse-dcf_methodology.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-3/PIL-6"
ticker: SPCX
skill: reverse-dcf
mode: methodology
generated_at: 2026-09-19T14:35:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "b42ad3a44570"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-02"
    chosen_reading: "The base is Connectivity's 3M operating income annualised x4, stated as an annualisation of a filed quarter, not a forecast. The reverse-DCF solves for the growth implied by a price; it does not project one."
  - da_id: "DA-23"
    chosen_reading: "The earnings base is taken on the FILED sign. The served consolidated line returns +143,000,000 against a filed (143,000,000), so a reverse-DCF run on served figures would solve for growth in a quantity that does not exist."
entity_claims:
  - claim_id: "rdcf-live-market-cap"
    ticker: SPCX
    metric: market_capitalisation
    value: 2071800000000
    unit: USD
    basis: "13,567,041,680 shares x $152.71; price observed 2026-09-18"
    period: "2026Q3"
    evidence_grade: DERIVED
    source: "10-Q share count + 8-K Cursor shares + live nasdaq quote"
  - claim_id: "rdcf-connectivity-annualised-opinc"
    ticker: SPCX
    metric: annualised_operating_income
    value: 6624000000
    unit: USD
    basis: "1,656 x 4 — annualisation of the filed 3M rate"
    period: "2026Q2"
    evidence_grade: MODELED
    source: "SPCX 10-Q Note 18, filed segment operating income"
  - claim_id: "rdcf-implied-perpetual-growth-lo"
    ticker: SPCX
    metric: implied_perpetual_growth_rate
    value: 0.1468
    unit: ratio
    basis: "Gordon: r - 1/multiple = 0.15 - 1/312.8; at the constitution's 15% required return"
    period: "2026Q3"
    evidence_grade: MODELED
    source: "arithmetic on live price and filed segment income"
  - claim_id: "rdcf-implied-perpetual-growth-hi"
    ticker: SPCX
    metric: implied_perpetual_growth_rate
    value: 0.2468
    unit: ratio
    basis: "Gordon: 0.25 - 1/312.8; at the constitution's 25% required return"
    period: "2026Q3"
    evidence_grade: MODELED
    source: "arithmetic on live price and filed segment income"
key_metrics:
  live_market_cap_usd_t: 2.0718
  connectivity_annualised_opinc_usd_m: 6624
  implied_perpetual_growth_lo: 0.1468
  implied_perpetual_growth_hi: 0.2468
---

# SPCX × reverse-dcf × methodology

**What the live price implies — the price question asked backwards.** Admitted because a reverse DCF
**forecasts nothing**; it takes an observed price as given. **It never faced the FCF-history limb**
that bars a forward DCF at SPCX.

## 1. The instrument

```
Live market cap             $2.0718T     (13,567,041,680 × $152.71)
Connectivity op income      $6,624M      (filed 3M × 4 — the only positive segment)
⇒ Market-cap-to-Connectivity-income      312.8×
```

**Gordon: `P/E = 1 / (r − g)`**, so **`r − g = 1/312.8 = 0.32%`**.

| Required return `r` *(constitution: 15–25% target IRR)* | **Implied perpetual growth `g`** |
|---:|---:|
| **15%** | **14.68%** |
| **20%** | **19.68%** |
| **25%** | **24.68%** |

> ### 🔴 THE FINDING: THE IMPLIED PERPETUAL GROWTH ESSENTIALLY EQUALS THE REQUIRED RETURN
>
> **`g ≈ r − 0.32%`.** At every point in the constitution's stated range, **the growth the price
> implies is within a third of a percentage point of the return demanded.**
>
> **What that means mechanically:** when `g → r`, the Gordon denominator collapses and **the
> terminal value approaches 100% of the present value.** Virtually none of the $2.07T is paying for
> cash flows anyone can see. **It is all terminal.**

## 2. ⚠️ And that breaches F1's own terminal-value cap

**F1's surviving method carries a hard rule: *"terminal value capped at 50–70% of total EV."***
**The implied terminal share here is ~100%.** So:

| | |
|---|---|
| **F1's cap** | **50–70% of total EV** |
| **This reverse-DCF implies** | **≈100%** |
| **⇒ The price is outside F1's own admitted framework** | |

**Three readings, and the artifact reports all three rather than choosing:**

1. **The price is too high** — the market has not applied the cap the framework demands.
2. **The cap is wrong for a business at this stage** — a company whose only profitable segment has a
   **+108.3%**-growth channel may legitimately be valued as near-pure terminal.
3. **The attribution is the problem** — the 313× divides the **whole** market cap by **one**
   segment's income, which implicitly sets **Space and AI to zero**.
   **Framing (3) is the most likely and the most important: the arithmetic is not "Connectivity is
   worth 313× income" — it is "the whole company costs 313× the income of its only profitable
   segment."**

## 3. What the price implies about Space and AI

**Restated as the question it actually answers:**

> **After paying 313× for Connectivity, what is left for Space and AI?**
>
> **Nothing — by construction.** The framing sets them to **zero** and still needs a ~100% terminal
> value. **So the market is either (a) attributing the whole price to Connectivity and treating Space
> and AI as free, or (b) applying a Connectivity multiple far lower than 313× and crediting Space and
> AI with substantial value.**

**This artifact cannot distinguish (a) from (b)** — that requires the regimes, which are `MODELED`
ranges in `sotp-valuation`. **What it can state is the bound:**

| If Space + AI are worth | Then Connectivity's implied multiple is |
|---|---:|
| **$0** | **312.8×** |
| **$0.5T** | **237.3×** |
| **$1.0T** | **161.8×** |
| **$1.5T** | **86.3×** |

**Even at a generous $1.5T for the two loss-making segments, Connectivity carries 86×.** **The
finding survives every allocation** — which is what makes it a finding rather than an artefact of
framing (3).

## 4. Status — a constraint, not a licence

**Per §1c: `reverse-dcf` is a cross-check on the three regimes, in the same class as `comps` —
never primary.** Its output is *"what the live price implies"*, **not** *"what SPCX is worth."*

**Where the implied growth is absurd on its face, that is a finding about the PRICE, reported as
such.**

## 5. Hand-off

| To | What |
|---|---|
| **P3** | The **market-implied limb**: the price requires **~15–25% perpetual growth in the only profitable segment**, with the AI segment contributing **no separable value** under framing (3) |
| **P6** | The terminal-value breach of F1's 50–70% cap is a **comparability fact for the anchor** — the price sits outside the framework the anchor would use |
| **011** | **The 313× is a valuation fact, not a position.** This thesis produces no trade ideas; 011 sizes |
| **T-5 (triggers)** | If a P11 deal security normalises and the **first admissible comparator** appears, this reverse-DCF can be re-run against a **borrowed** multiple instead of a segment-derived one |
````

## Artifact — artifacts/SPCX/2026-09-19_risk_general-risk-factors-identification-assessment.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-5"
ticker: SPCX
skill: risk
mode: general-risk-factors-identification-assessment
generated_at: 2026-09-19T12:40:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "953fc5d396e7"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-19"
    chosen_reading: "Entity discontinuity — X merger 2025-03-28, xAI merger 2026-02-02 under common control, IPO 2026-06, five-for-one split 2026-05, Cursor pending. Growth rates across these boundaries mix real growth with entity change, so no risk figure below is quoted across a boundary without saying so."
entity_claims:
  - claim_id: "risk-coverage-ratio-h1-2026"
    ticker: SPCX
    metric: operating_cash_flow_coverage_of_investing
    value: 0.1005
    unit: ratio
    basis: "operating 3,466 / investing 34,487, H1 2026; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q — cash flow statement, via 001's capital row; consumed"
  - claim_id: "risk-notes-coupon"
    ticker: SPCX
    metric: effective_interest_rate
    value: 0.0603
    unit: ratio
    basis: "40,869 notes at a 6.03% effective rate; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "001/artifacts/SPCX — consumed"
key_metrics:
  coverage_ratio_h1_2026: 0.1005
  notes_effective_interest_rate: 0.0603
---

# SPCX × risk × general-risk-factors-identification-assessment

**The funding structure, ranked by what would actually stop the build.** P5's claim is that
`CAPITAL` is the binding constraint; this artifact tests whether the risks that bind are capital
risks or something else.

## 1. 🔴 R-1 — The Cursor dilution is BLOCKING, and it is the only risk on the critical path

| | |
|---|---|
| **What** | **$60B all-stock** acquisition of Cursor (Anysphere, Inc.). Merger agreement entered **2026-06-16**; re-affirmed in an **8-K of 2026-08-14** |
| **Status** | **Pending — closing Q3 2026** |
| **Why it is `blocking`** | Round 4 made the headline SOTP **PRO-FORMA**. Cursor is now **inside** the anchor, so its consideration and **dilution are inputs to P1**, not sensitivities |
| **The exposure** | **V-5 previously recorded the dilution as *not determinable*.** The pre-close provisional existed precisely to avoid this dependency; the owner overrode it, and **the cost is stated rather than hidden** |
| **Severity** | **Blocking for P1.** Not "a risk" — a **prerequisite** |

**What must be found:** the share consideration. The 8-K of **2026-08-14** is the most recent
filing; `search_documents` located it, and `read_source_pages` is the route to its terms.
**A pro-forma headline cannot be computed without it.**

## 2. R-2 — The coverage ratio, and why it is the claim rather than a risk

```
H1 2026 operating cash flow   +$3,466M
H1 2026 investing            $(34,487)M     ← coverage ≈ 0.10×
H1 2026 financing           +$100,291M      ← IPO $85,675M + notes $40,869M
```

**A company with a $(143)M quarterly operating loss raised $85.7B in equity and $40.9B in notes,
and named data centers before launch facilities when describing the capex.**

**P5's falsifier** is `coverage >= 1.0×`. At **0.1005×** it is **an order of magnitude away** — so
this is not a near-threshold risk; it is the structural condition. **Internal cash flow covers
about a tenth of the build.**

## 3. R-3 — The notes are priced at a level that is itself a risk signal

**$40,869M at a 6.03% effective rate.** For a company of SPCX's scale and narrative, **6.03% is not
an investment-grade cost of debt.** It is a rate that embeds the funding-structure risk this pillar
names.

**And a further tranche followed:** an 8-K of **2026-06-26** records **$7.0B of 5.350% Senior Notes
due 2031** — **priced 68 bp inside** the earlier effective rate. **The direction matters:** the
second raise priced tighter, which is evidence the market's read of the structure **improved**
between the two. **Recorded because it cuts against the risk narrative**, and a risk register that
only accumulates confirming evidence is not a register.

## 4. R-4 — Control, float, and who can price the dilution

**P5's claim names the single-class control structure as determining who can price the Cursor
dilution.** Two facts:

1. **The constitution records NO index inclusion at ratification.** So the marginal buyer of the
   equity that funds the build is a **dated catalyst, not a standing assumption** — it must be
   recorded as such or dropped.
2. **Post-IPO equity moved 2,573 → 127,224 (49.5×).** A structural change of that magnitude means
   **the shareholder base that will vote on any further dilution is not the one that existed at
   IPO.**

**Unresolved here:** whether the Cursor consideration is Class A and whether the control structure
gives any holder a veto. **That is the same 8-K R-1 needs**, and it is why the two risks are one
investigation.

## 5. Risk register, ranked

| # | Risk | Class | Binds? |
|---|---|---|---|
| **R-1** | **Cursor dilution** | **Execution / event** | 🔴 **BLOCKING — P1 cannot be delivered without it** |
| **R-2** | Coverage **0.1005×** | **Structural** | ✅ **This IS P5's claim**, not a risk against it |
| **R-3** | Cost of debt **6.03% → 5.350%** | Market | ⚠️ **Improving**, and recorded as such |
| **R-4** | Control / float / index inclusion | Governance | ⚠️ **Open — same 8-K as R-1** |
| R-5 | **A4's ceiling on orbital compute** | **Constitutional** | ✅ Not a risk but a **bound** — the 1M-satellite filing is inadmissible as a valuation input. **Not a threat to the anchor; a limit on what the anchor may claim** |

## 6. What this establishes

**P5's claim is that internal cash flow does not cover the compute build, so the anchor's downside
is governed by the funding structure rather than any physical or demand constraint.**

**This artifact confirms it — with one qualification the plan did not anticipate:** the *binding*
item is not the funding structure in general but **one specific unbounded liability (R-1)**.
`CAPITAL` binds; but at this moment **`CAPITAL` binds through a single, dated, unresolved
disclosure.** That is a sharper statement of the constraint than "capital is scarce", and it is
what P5 should carry.
````

## Artifact — artifacts/SPCX/2026-09-19_risk_regulatory-compliance-risk-assessment.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-5"
ticker: SPCX
skill: risk
mode: regulatory-compliance-risk-assessment
generated_at: 2026-09-19T12:50:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "953fc5d396e7"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-24"
    chosen_reading: "Where a regulatory event is described in prose differently from its accounting treatment, the FILED accounting wins and the prose is reported as a separate claim. The SATS Q3 2025 event is the registered instance: a non-cash impairment charge, not a gain."
entity_claims:
  - claim_id: "rr-echostar-instalments"
    ticker: SPCX
    metric: spectrum_instalment_obligation
    value: 856000000
    unit: USD
    basis: "EchoStar spectrum instalments; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "001/artifacts/SPCX/2026-09-18_2310_operational-kpi §5 — consumed"
key_metrics:
  echostar_spectrum_instalments_usd_m: 856
---

# SPCX × risk × regulatory-compliance-risk-assessment

**One significant regulatory exposure, one bound, and one thing that is not a regulatory risk.**

## 1. R-1 — The EchoStar spectrum obligation, and the licence-holder's terminal condition

**$856M of EchoStar spectrum instalments** on SPCX's balance-sheet obligations.

**The exposure is not the instalment — it is the counterparty's trajectory.** SATS is buying AWS-4
and H-Block to SpaceX for **~$20bn, up to $11bn of it in SpaceX Class A at $212/share**. So:

- **SPCX is paying instalments on spectrum it is simultaneously acquiring the licence-holder for.**
- **SATS' own operating satellite business is ~$0.3bn** against **≈$42.65bn** of regulatory-asset
  realisation — the **≈142×** figure 003's map derived. **Launch cost is not a variable in the
  transaction that realises the value.**
- **The disposal gain or loss is `UNRESOLVABLE-FROM-PUBLIC-SOURCES` until closing**, because it is
  determined at closing on a basis different from the current statements.

**⇒ The regulatory risk is a CONSOLIDATION risk, not a compliance risk.** If the transaction closes,
SPCX's instalment obligation and its consideration are the same transaction viewed twice — and the
**$856M must not be treated as an arm's-length payable to a third party.**

## 2. R-2 — The 1M-satellite filing: regulatory status is not a valuation input

**Two separate questions, and only one of them is P5's:**

| Question | Answer |
|---|---|
| Is the orbital filing **regulatorily** live? | **Not assessed here.** It is a filed aspiration, and its ITU/FCC status is **not a valuation input** under A4/P10 |
| May the anchor price it? | **No.** A4 bars valuing terrestrial and orbital compute as one; **P10's five conditions are not met** |

**⇒ Recorded so the two are not conflated.** "The filing exists" is not "the revenue is coming", and
it is also not "the filing is a regulatory risk". **It is inadmissible — which is a statement about
the anchor, not about the regulator.**

## 3. R-3 — Index inclusion: a dated catalyst, never a standing assumption

**The constitution records NO index inclusion at ratification.** Therefore:

- **The marginal buyer of the equity that funds the build is a DATED CATALYST.** P5 must record it
  as such **or drop it** — there is no third option
- **Float structure rides on the same pillar.** Post-IPO equity moved **2,573 → 127,224 (49.5×)**,
  so the float that would enter an index is a post-IPO artefact, not a historical one

**Why this is a risk and not an opportunity:** an anchor that assumes index inclusion **prices a
buyer who has not arrived.** The `market_data_stage_regresses` expiry trigger covers the adjacent
case (the live feed stopping); **there is no trigger for an inclusion that never happens**, which is
why the item is carried as a *dated catalyst with no date* rather than as an assumption.

## 4. What is NOT a regulatory risk — stated for exhaustiveness

| Candidate | Why not |
|---|---|
| **Launch licensing** | SPCX's cadence is filed and current; a licensing constraint would appear as a cadence break, **which the DA-08 series would show** |
| **Spectrum at SPCX's own Connectivity segment** | The segment is filed and operating. **The regulatory exposure in this thesis is EchoStar's, not SPCX's** |
| **CFIUS / P11 gates** | **P11 deal securities are IRDM, GSAT and RKLB — not SPCX.** SPCX is an acquirer here, and its own gate exposure is not registered |

## 5. Register

| # | Item | Class | Binds? |
|---|---|---|---|
| **R-1** | EchoStar instalments **$856M** | **Consolidation, not compliance** | ⚠️ Must not be treated as an arm's-length payable |
| **R-2** | 1M-satellite filing | **Admissibility bound (A4/P10)** | ✅ Not a regulatory risk — an anchor limit |
| **R-3** | Index inclusion / float | **Dated catalyst** | ⚠️ Must be dated or dropped; post-IPO float is 49.5× |
````

## Artifact — artifacts/SPCX/2026-09-19_risk_technology-disruption-risk-analysis.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-5"
ticker: SPCX
skill: risk
mode: technology-disruption-risk-analysis
generated_at: 2026-09-19T12:45:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "953fc5d396e7"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-11"
    chosen_reading: "The 1.4 GW is IT load only — excluding cooling, power distribution losses, lighting, security and facility overhead. True facility draw typically 1.2-1.5x. It is a CAPACITY figure, not a revenue or earnings figure, and no $/kW-revenue assumption the issuer discloses converts it. 002 owns the PUE restatement; consumed here, never re-derived."
entity_claims:
  - claim_id: "risk-nameplate-draw"
    ticker: SPCX
    metric: nameplate_compute_draw_it_load
    value: 1.4
    unit: GW
    basis: "IT load only, excluding cooling and distribution (DA-11); nameplate, not measured; 3M duration"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "001/artifacts/SPCX/2026-09-18_1239_operational-kpi §AI — consumed; 002 owns the restatement"
key_metrics:
  nameplate_compute_draw_it_load_gw: 1.4
---

# SPCX × risk × technology-disruption-risk-analysis

**The technology risks that actually bear on the anchor — and the two that do not.**

## 1. 🔴 T-1 — The architecture transition inside SPCX, not competition outside it

**F5a vs F5b is an order of magnitude.** Starship (F5a, fully reusable) has a propellant-dominant
floor of **~$46–92/kg at 100 t**; Falcon (F5b, partially reusable) has an **expended second stage
at ~$8–12M** dominating. **The transition between them is the sector's biggest cost event.**

**Why it is a risk to the anchor and not just an opportunity:**

| | |
|---|---|
| **P4's binding constraint** | **`MANUFACTURING_RATE`** in the medium term — **F5b, the expended second-stage manufacturing curve**, not propellant |
| **Starship cadence** | **3 → 1 across H1.** It is a **cost and capability programme, not a competitive position** |
| **Disclosure inversion** | 003 recorded that SPCX **publishes two contradicting cost claims on the same day**, and that Starship's **architecture diverges from its declaration** (declared F5a, flown expendable → F5c) |
| **The 71.5% problem** | Basis C's **$6,596/kg** is **71.5% Starship R&D — it is not a launch cost** |

**⇒ The risk is not that Starship fails. It is that the anchor prices a transition that the filings
show has not started.** P4's ex-R&D test separates launch economics from Starship funding precisely
so the SOTP does not pay for the transition twice.

## 2. 🔴 T-2 — The AI segment's own metric cannot be converted, by construction (DA-11)

**The 1.4 GW is IT load.** It excludes cooling, power distribution losses, lighting, security and
facility overhead — true facility draw is typically **1.2–1.5×**. 001 called it *"the most dangerous
figure in this thesis."*

**Two consequences, and the second is the one that bites:**

1. **It is a capacity figure, not a revenue or earnings figure.** No issuer discloses a
   `$/kW-revenue` assumption that would convert it.
2. **Therefore P3 cannot price the AI segment off its own headline metric** — and must fall back to
   **invested capital** (round 4's confirmed headline), which is a *cost* basis, not a *value* basis.

**⇒ This is a risk to the anchor's answer, not to the business.** The AI segment may be excellent;
**the disclosure does not let the anchor say so**, and pricing it off 1.4 GW would be the invented
multiple P3 exists to prevent.

## 3. T-3 — A4's ceiling: the orbital filing is inadmissible, and that is a bound not a threat

**SPCX's separate filing for up to 1 million satellites at 100 kW of compute per tonne** is a
**filed aspiration with no revenue line.** Under **A4** and **P10**, it is **inadmissible as a
valuation input**.

**Two things must not be confused:**

| | |
|---|---|
| **A4 is explicit** | Terrestrial and orbital compute are **different businesses** and must never be valued as one. SPCX's AI segment is **ground-based** |
| **P10 gates orbital compute** on five conditions, **none of which SPCX's AI segment meets** — because **it is not an orbital-compute business** | |

**⇒ The risk runs the other way from what a reader might expect.** The orbital filing does **not**
add optionality the anchor may price. **It adds a disclosure the anchor must refuse to price.** An
anchor that capitalised the 1M-satellite filing would violate A4 — and the failure would be
invisible, because the number would look conservative next to the segment's actual capex.

## 4. T-4 — The risk that is *not* here: competitive technology displacement

**Stated as a negative, because the register should be exhaustive in both directions.** The
following are **not** material to the anchor:

| Candidate | Why not |
|---|---|
| **RKLB Neutron** | **Unflown.** A vehicle that has not flown cannot displace a cadence |
| **Amazon Leo** | Competes with **Connectivity**, not with the launch or AI segments. Carried at 006 |
| **Terrestrial compute displacement** (a better chip, a cheaper operator) | **This is the demand-side risk inside the AI segment's own framing**, and it is **P3's admissibility problem**, not a separate register entry |
| **Propellant price** | **F5b's floor is the expended second stage, not propellant.** Propellant is **~2–3%** of a Falcon marginal cost — a 2× propellant move is ~1–1.5% of the floor. **The named risk is the wrong variable**, and 003 recorded the same inversion |

## 5. Register

| # | Risk | Bears on | Materiality to the anchor |
|---|---|---|---|
| **T-1** | Architecture transition not started (3→1) | **P4, P6** | 🔴 **High** — the anchor must not price a transition the filings do not show |
| **T-2** | 1.4 GW unconvertible (DA-11) | **P3** | 🔴 **High** — forces the cost-basis headline |
| **T-3** | Orbital filing inadmissible (A4/P10) | **P3** | ⚠️ **A bound, not a threat** |
| **T-4** | Competitive displacement | — | ✅ **Not material, with reasons stated** |
````

## Artifact — artifacts/SPCX/2026-09-19_sotp-valuation_defaults.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-1/PIL-6"
ticker: SPCX
skill: sotp-valuation
mode: defaults
generated_at: 2026-09-19T14:15:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07305f5d5391"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-02"
    chosen_reading: "Duration — the annualisation below is the 3M rate x4, stated as an ANNUALISATION, never as a forecast. It is not a 6M figure doubled and it is not a projection."
  - da_id: "DA-11"
    chosen_reading: "The 1.4 GW is IT load only, excluding cooling, distribution losses, lighting, security and facility overhead — true facility draw typically 1.2-1.5x. No $/kW-revenue assumption is disclosed, so it cannot be converted into the invested-capital framing without a stated default."
entity_claims:
  - claim_id: "sotpf-annualised-connectivity-opinc"
    ticker: SPCX
    metric: annualised_operating_income
    value: 6624000000
    unit: USD
    basis: "1,656 x 4 — annualisation of the 3M rate, NOT a forecast; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: MODELED
    source: "arithmetic on filed cells; the annualisation multiplier is the default"
  - claim_id: "sotpf-live-market-cap"
    ticker: SPCX
    metric: market_capitalisation
    value: 2071800000000
    unit: USD
    basis: "13,567,041,680 shares x $152.71; price observed 2026-09-18, retrieved 2026-09-19"
    period: "2026Q3"
    evidence_grade: DERIVED
    source: "10-Q share count + 8-K Cursor shares + live nasdaq quote"
key_metrics:
  annualised_connectivity_opinc_usd_m: 6624
  live_market_cap_usd_t: 2.0718
---

# SPCX × sotp-valuation × defaults

**Every assumption the SOTP takes where no filed figure settles the question.** Each is stated so a
reader can disagree with it explicitly rather than inherit it silently.

## D-1 — Annualisation is `3M × 4`, and it is NOT a forecast

| Segment | 3M (filed) | Annualised *(×4)* |
|---|---:|---:|
| Connectivity | 1,656 | **6,624** |
| Space | (542) | **(2,168)** |
| AI | (1,257) | **(5,028)** |
| Consolidated | (143) | **(572)** |

**Why a default is needed:** the filing gives a quarter, and multiples need a year.
**Why `×4` and not `6M × 2`:** the 10-Q files both under one concept (**DA-26**), and mixing the
durations would compound two bases. **The 3M rate is the most recent and the least contaminated by
the pre-xAI comparison window.**

**What would overturn it:** a filed annual figure. **None exists for a company that IPO'd in
June 2026.** The `×4` is therefore a **stated artefact of the disclosure's window**, not a modelled
growth assumption — **and the artifact says so rather than presenting 6,624 as a number SPCX
earned.**

## D-2 — The market cap uses the PRO-FORMA share count

**Shares: 13,176,000,000 (2026-06-30) + 391,041,680 (Cursor, 2026-08-14) = 13,567,041,680.**

**Why pro-forma:** round 4 made the headline pro-forma, and the deal has now **closed** — so
**pre-close is the counterfactual, not the base case.** Using 13.176bn would price a company that no
longer exists.

**What is excluded and why:** the **73,493,373** assumed RSUs and options are **contingent**, so
they enter as a **dilution note**, not in the denominator. **Including them would be a default the
filings do not support.**

## D-3 — The AI segment's invested-capital basis needs a default the filing does not give

**Round 4's confirmed headline is INVESTED CAPITAL**, using the H1 2026 capex attributed *"first to
the build out of DATA CENTERS and related infrastructure."*

**The default that follows, and its limit:** **the filing does not disaggregate that capex by
segment.** So the invested-capital figure is **an allocation of a company-wide number**, not a filed
AI-segment number. **Default taken: report it as a company-level attribution with the allocation
stated, never as a filed segment figure.**

**What would overturn it:** a segment-level capex disclosure. **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`
on the pages read.**

## D-4 — Risk-free and duration inputs come from the constitution, not from a model

**Required return: a stated target IRR, not WACC** — per F1's surviving method, **15–25%**. And the
constitution's macro triggers (**10Y > 5.25%**, or a Fed pivot) are the **scenario-weight inputs**,
not background.

**Default:** the 10Y is taken at the constitution's recorded **4.80%**, with **30Y at 5.26%**, both
at three-year highs. **No live rate was fetched** — the live feed is an equity quote source, and
**a rate fetched from a different source would be a second basis, not an update.**

## D-5 — What this artifact deliberately does NOT default

| Question | Default? |
|---|---|
| Space's multiple | **No** — DA-06: **no external multiple is borrowed**. Value from contribution |
| Connectivity's multiple | **No** — all satellite comparables are `P11` or `PARTIAL` |
| AI's multiple | **No** — headline is invested capital, and the other two framings are reported alongside |
| A single blended multiple | **No — barred.** "Valuing the three at one rate is not a simplification. It is a different claim" |
| A point estimate | **No** — every regime is a range |

## Summary

| # | Default | Grade | Overturned by |
|---|---|---|---|
| **D-1** | Annualise `3M × 4` | `MODELED` | A filed annual figure — none exists |
| **D-2** | Pro-forma share count; contingent awards excluded | `DERIVED` | The contingent awards vesting |
| **D-3** | Invested capital is a **company-level attribution** | `MODELED` | Segment-level capex disclosure |
| **D-4** | 15–25% target IRR; 10Y at the constitution's 4.80% | `MODELED` | A live rate from a stated source |
| **D-5** | No default where a multiple would be invented | — | — |
````

## Artifact — artifacts/SPCX/2026-09-19_sotp-valuation_methodology.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-1/PIL-6"
ticker: SPCX
skill: sotp-valuation
mode: methodology
generated_at: 2026-09-19T13:40:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07305f5d5391"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "Component identity shown in-line on every segment table: gross profit - opex = operating_income. SPCX files NO segment gross-profit subtotal, so gross profit is DERIVED. EPS x shares is inadmissible as a sign test; the gross-profit bound is the fallback."
  - da_id: "DA-06"
    chosen_reading: "Space is captive_integrated — no transaction price exists. Its value comes from segment CONTRIBUTION and no external multiple is borrowed. The flag travels with the row."
  - da_id: "DA-02"
    chosen_reading: "Segment operating income is filed on a 3M and a 6M basis under one concept. This artifact annualises the 3M rate x4 for the multiple's denominator and SAYS SO — it does not blend 3M and 6M figures."
entity_claims:
  - claim_id: "sotp-q2-consolidated-revenue"
    ticker: SPCX
    metric: consolidated_revenue
    value: 7814000000
    unit: USD
    basis: "filed consolidated; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q spcx-20260630.htm p.30 (Note 18) — consumed via 003, re-read here; https://agentii.ai/v/SPCX/sec8/30"
  - claim_id: "sotp-q2-consolidated-operating-loss"
    ticker: SPCX
    metric: operating_income_loss
    value: -143000000
    unit: USD
    basis: "filed consolidated, DA-23-corrected; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q — segments sum exactly to (143); the served layer returns +143,000,000 (DA-23)"
  - claim_id: "sotp-shares-outstanding-2026-06-30"
    ticker: SPCX
    metric: common_shares_outstanding
    value: 13176000000
    unit: shares
    basis: "Class A 7,607,000,000 + Class B 5,569,000,000, instant 2026-06-30; closes exactly"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q spcx-20260630.htm — us-gaap:CommonStockSharesOutstanding x StatementClassOfStockAxis"
  - claim_id: "sotp-cursor-shares-issued"
    ticker: SPCX
    metric: shares_issued_acquisition
    value: 391041680
    unit: shares
    basis: "389,289,254 at close + 1,752,426 vested RSUs; instant 2026-08-14"
    period: "2026Q3"
    evidence_grade: DEMONSTRATED
    source: "8-K 0001628280-26-056945 (2026-08-14) Item 2.01 — https://agentii.ai/v/SPCX/sec9/2"
  - claim_id: "sotp-live-quote"
    ticker: SPCX
    metric: share_price
    value: 152.71
    unit: USD
    basis: "close, source nasdaq, data_class fast; observed 2026-09-18, retrieved 2026-09-19"
    period: "2026Q3"
    evidence_grade: DEMONSTRATED
    source: "data-tools/market_data.py get_quote — keyless NASDAQ"
key_metrics:
  consolidated_revenue_q2_2026_usd_m: 7814
  consolidated_operating_loss_q2_2026_usd_m: -143
  shares_outstanding_2026_06_30: 13176000000
  cursor_shares_issued: 391041680
  live_price_usd: 152.71
  segment_capex_total_q2_2026_usd_m: 18369
  ai_capex_q2_2026_usd_m: 15828
  connectivity_capex_q2_2026_usd_m: 1367
  space_capex_q2_2026_usd_m: 1174
  ai_capex_share_q2_2026: 0.8617
---

# SPCX × sotp-valuation × methodology

**The anchor. Three segments, three regimes, one dated market print — and a convergence the plan
did not expect.**

## 0. ⚠️ Three premises changed during this run, and each is stated before the valuation

| # | What the plan assumed | What the filings show |
|---|---|---|
| **1** | Cursor **pending**, closing Q3 2026; dilution **not determinable** — V-5 `blocking` | **Cursor CLOSED 2026-08-14** ([8-K Item 2.01](https://agentii.ai/v/SPCX/sec9/2)). Dilution is **391,041,680 shares issued**, **464,535,053** including assumed awards. **V-5 RESOLVED** |
| **2** | Market Data Stage `none`; price is a dated print (`$135.00`, 2026-06) | **A keyless live feed exists.** **$152.71**, close **2026-09-18**, source `nasdaq` |
| **3** | The constitution's ~$1.62T anchor is ~13.1% behind the live price | **It is further behind than that, and on a basis we can now check** — §2 |

**The valuation below is built on the filings, not on the plan's assumptions about them.**

## 1. The segment table — component identity in-line, per DA-23

**Duration basis: 3M, quarter ended 2026-06-30. SPCX files NO segment gross-profit subtotal**, so
gross profit is **`DERIVED`** and shown as such.

| Segment | Revenue | Cost of rev. | **Gross profit** *(DERIVED)* | R&D | SG&A | Restr. | **Op. income** *(filed)* | Margin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Space** | 962 | 329 | **633** | 1,076 | 99 | — | **(542)** | **−56.34%** |
| **Connectivity** | 4,291 | 2,060 | **2,231** | 294 | 281 | — | **1,656** | **+38.59%** |
| **AI** | 2,561 | 1,106 | **1,455** | 2,178 | 532 | **2** | **(1,257)** | **−49.08%** |
| **Σ segments** | **7,814** | 3,495 | **4,319** | 3,548 | 912 | 2 | **(143)** | **−1.83%** |

**Identity closes exactly on every row and at consolidation:**
`962 − 1,504 = (542)` · `4,291 − 2,635 = 1,656` · **`2,561 − 3,818 = (1,257)`** · **`7,814 − 7,957 = (143)`** ✓

> ### ⚠️ CORRECTION, MADE IN THIS ARTIFACT'S FIRST DRAFT — A $2M "OTHER" TERM
>
> The first draft's AI row showed only **R&D 2,178 + SG&A 532 = 2,710**, giving
> `1,455 − 2,710 = (1,255)` — **$2M short of the filed `(1,257)`** — while the surrounding text
> asserted *"the identity closes exactly on every row."* **It did not.**
>
> **The missing term is the filed `Restructuring charges` line of $2M** — and a later pass found the draft had **also mislabelled the column "Other"**. The 10-Q names it. 003's `value-pool-map` E-03 has it right:
> `2,178 + 532 + 2 = 2,712 opex … 1,455 − 2,712 = (1,257) ✓ EXACT`. **This artifact dropped it**
> in transcription and then claimed exactness it had not verified.
>
> **Caught by running the arithmetic rather than trusting the assertion** — which is the only way
> this class of error is ever caught. **It is recorded rather than silently fixed because the
> claim "closes exactly" is precisely the kind of sentence that travels downstream unchecked**, and
> a reader who re-derived the row would have found a $2M hole with no note explaining it.
>
> **Reconciled total opex: `3,548 + 912 + 2 = 4,462`**, and `7,814 − (3,495 + 4,462) = (143)` ✓

> **⚠️ DA-23 IS LIVE ON THE CONSOLIDATED LINE.** The segments sum to **$(143)M**; the platform's
> served layer returns **`+143,000,000`**. 002's census found **16 of 20** served
> `OperatingIncomeLoss` facts at SPCX carry a positive value against a filed negative. **The
> artifact reads the filed sign.** `EPS × shares` would not have caught this.

### The supplemental block, which this artifact's first draft did not read

**Note 18 files three more segment lines below the income table. They are the capital-allocation
finding. An earlier version of `_cross/tier0-spacex-anchor_synthesis.md` recorded segment-level
capex as `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — it is filed, on this page.**

| Segment | D&A | Share-based comp. | **Capital expenditures** | Share of capex |
|---|---:|---:|---:|---:|
| Space | 158 | 179 | **1,174** | **6.4%** |
| Connectivity | 805 | 136 | **1,367** | **7.4%** |
| **AI** | 1,885 | 516 | **15,828** | **86.2%** |
| **Σ** | **2,848** | **831** | **18,369** | **100%** |

> **The AI segment absorbs `15,828 / 18,369 = 86.17%` of quarterly capital expenditure** while
> running the **largest operating loss** in the company — and **Connectivity, the only profitable
> segment, receives 7.4%.** Source: [SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30).

## 2. The market print — two bases, and a discrepancy that is a finding

| Basis | Value | Source |
|---|---:|---|
| **Shares outstanding**, 2026-06-30 | **13,176,000,000** | 10-Q, `CommonStockSharesOutstanding`; Class A 7,607M + Class B 5,569M — **closes exactly** |
| **+ Cursor**, issued 2026-08-14 | **391,041,680** | 8-K `0001628280-26-056945` |
| **Pro-forma shares** | **13,567,041,680** | |
| **Live price**, close 2026-09-18 | **$152.71** | `nasdaq`, keyless |
| **⇒ LIVE MARKET CAP** | **≈ $2.072T** | 13.567bn × $152.71 |
| Constitution anchor | **~$1.62T** | struck at `$135.00`, 2026-06 |

> ### 🔴 THE CONSTITUTION'S ANCHOR IMPLIES ~$122.95/SHARE ON THIS SHARE COUNT — NOT $135.00
>
> `$1.62T ÷ 13,176,000,000 = $122.95`. **The IPO priced at `$135.00`.** So the constitution's
> anchor and the IPO price **do not reconcile on the filed share count**, and the gap is **~9%
> at the anchor** before any price move.
>
> **⇒ The anchor is NOT "13.1% behind". Against the live price it is further behind, and the basis
> is unstated.** Round 4's provisional measured the gap as `152.71/135.00 − 1 = +13.1%` — **that
> compares the live price to the IPO price, not to the anchor's own implied price.**
>
> **This artifact therefore publishes BOTH and resolves neither**, per round 4's answer (*"both —
> live and dated, with the spread reported"*). **The reconciliation of the ~$1.62T anchor is
> `UNRESOLVABLE-FROM-PUBLIC-SOURCES` on the pages read**: it requires the basis the constitution
> struck it on, which is not in this workspace.

## 3. The regimes — one per segment, each with its boundary

### Space — `DA-06` non-comparability; value from contribution

| | |
|---|---|
| **Revenue** | **$962M** (3M) — **customer launches only.** ~74% of launches produce no Space revenue |
| **Gross margin** | **65.80%** — **the highest in the company** |
| **Operating margin** | **−56.34%** — **the worst in the company** |
| **The 122.14 pp swing** | **R&D 111.85 pp** + **SG&A 10.29 pp** — decomposed exactly |
| **Comparability** | ❌ **NONE.** `captive_integrated`; **no transaction price exists**. RKLB and FLY are `loss_making` |
| **Regime** | **Revenue multiple, `MODELED`, stated as a range** — and **no external multiple is borrowed** |

**P4's test — ex-R&D operating result is positive:** `633 gross profit − 99 SG&A = +$534M`. ✅
**The launch business is profitable before Starship development**, which is P4's claim. **The R&D
split is `MODELED`** (the filing does not separate Starship from Falcon), and that limit travels.

### Connectivity — margin-anchored; the only profitable segment

| | |
|---|---|
| **Revenue** | **$4,291M** (3M), **+65.8%**; **54.9% of consolidated** |
| **Operating margin** | **+38.59%** — **the only positive segment, and the highest-margin operator in the universe** |
| **Operating leverage** | Income **+79.4%** on revenue **+65.8%** — **+13.6 pp of rate spread** |
| **Channel mix** | **Enterprise&Gov +108.3%** vs **Consumer +44.4%** — the managed channel grew **2.4× faster** |
| **Comparability** | ❌ IRDM and GSAT are **`P11` deal securities — the price is a spread**. ASTS/VSAT `PARTIAL` |
| **Regime** | **Margin-anchored, `MODELED`** — cross-checked against **terrestrial broadband**, not satellite peers |

### AI — invested capital, under the A4 ceiling

| | |
|---|---|
| **Revenue** | **$2,561M** (3M), **+247.5%** — **contaminated** (xAI merged 2026-02-02, prior periods recast) |
| **Operating margin** | **−49.08%** — the largest single drag on the consolidated line |
| **Headline metric** | **1.4 GW IT load** — **DA-11: unconvertible.** It is a **capacity** figure |
| **Comparability** | ❌ MSFT/GOOG compute are **cost centres**; **NVDA is the supplier** |
| **Regime** | **INVESTED CAPITAL** (round 4's confirmed headline) |

## 4. 🔴 The finding: there is no conventional discount to measure

**Annualising the 3M rate ×4** — stated as an annualisation, not a forecast:

| | Annualised |
|---|---:|
| **Connectivity operating income** | **$6,624M** |
| Space operating loss | $(2,168)M |
| AI operating loss | $(5,028)M |
| **Consolidated** | **$(572)M — a LOSS** |

**Now the arithmetic that is the thesis:**

> **Live market cap ≈ $2.072T ÷ Connectivity's annualised operating income $6.624bn = 312.8×**
>
> **And Connectivity is the ONLY profitable segment.**

**So the "conglomerate discount" question inverts.** The standard SOTP asks: *does the sum of parts
exceed the whole?* **Here the whole already requires the one profitable segment to carry a ~313×
operating multiple while two segments run losses of $(2.2)bn and $(5.0)bn annualised.** A
conglomerate DISCOUNT is not the live question. **The live question is whether the market is
crediting the loss-making segments with value at all — or whether it is paying 313× for
Connectivity and treating Space and AI as options with a large embedded premium.**

**Stating it as the three components §5 requires:**

| Component | Status |
|---|---|
| **Conglomerate discount** | ⚠️ **Cannot be measured as a discount** — the parts do not sum to less than the whole under any admissible multiple. **Reported as the inverse** |
| **Control / float discount** | ⚠️ **Made harder by pro-forma.** The Cursor consideration is **Class A**, so the control/float component is partly a discount **created by** the transaction the anchor now includes. **Where the two cannot be separated, that is the finding** |
| **Unallocated corporate cost** | ❌ **Not separable from the segment table** — SPCX files no corporate/unallocated line. **Reported as a bound, not allocated arbitrarily** |
| **Price-basis spread** | **~$122.95 → $152.71 implied**, plus the anchor's own unreconciled basis (§2) |

## 5. What this artifact does NOT claim

- **No point estimate.** Every multiple above is `MODELED`, and the regimes are ranges.
- **No `dcf`.** Consolidated FCF is negative; the ≥3-year limb fails. **`reverse-dcf` is the
  admissible DCF-shaped instrument** and runs separately.
- **No borrowed multiple.** The comparability partition admits **zero of eleven** comparators.
- **No blended multiple.** Valuing three businesses at one rate is *a different claim*, and the
  spread between the two is the finding.

## 6. Hand-off

`_cross/anchor-sotp.md` publishes the three regimes with boundaries naming **005, 006 and 009** —
not 005 alone, because SPCX is in neither 006's nor 009's universe. **The 313× figure is the
anchor's headline and 011's problem to act on**: it is a *valuation* fact, and this thesis produces
no positions.
````

## Artifact — artifacts/SPCX/2026-09-19_sotp-valuation_preflight.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-1/PIL-6"
ticker: SPCX
skill: sotp-valuation
mode: preflight
generated_at: 2026-09-19T14:10:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07305f5d5391"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "The three-way decomposition is the issuer's own filed segment boundary. The preflight checks that the decomposition the SOTP depends on actually exists before any multiple is applied."
entity_claims:
  - claim_id: "sotp-preflight-separable-segments"
    ticker: SPCX
    metric: count_of_spcx_segments_with_a_discrete_filed_revenue_line_and_operating_result
    value: 3
    unit: count
    basis: "Space, Connectivity, AI — each with a filed revenue line AND a filed operating result; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q spcx-20260630.htm p.30 (Note 18) — three segments, each with Income (loss) from operations"
key_metrics:
  separable_segments: 3
---

# SPCX × sotp-valuation × preflight

**Does the SOTP have a subject?** P1's falsifier is
`count_of_spcx_segments_with_a_discrete_filed_revenue_line_and_operating_result < 3`. This artifact
runs it **before** the valuation, because a decomposition that failed here would make every
multiple below meaningless.

## 1. The separability test — 3 of 3, DISCLOSED

| Segment | Discrete filed revenue line | Discrete filed operating result | Passes? |
|---|---|---|---|
| **Space** | ✅ **962** (3M) | ✅ **(542)** | ✅ |
| **Connectivity** | ✅ **4,291** | ✅ **1,656** | ✅ |
| **AI** | ✅ **2,561** | ✅ **(1,257)** | ✅ |

**All three carry BOTH a revenue line and an operating result, filed.** `threshold=3`, `op=<` → the
count is **3**, so **the falsifier does not fire.**

> ### ⚠️ THIS PILLAR'S ANSWER WAS ALMOST LOST TO A SUPERSESSION CLAIM
>
> Two 001 artifacts disagreed on whether the AI segment files an operating result:
> `1239_operational-kpi` reported **$(1,257)M**; `2310_operational-kpi` §2 recorded *"not
> disclosed."* An intermediate draft concluded the line was **`DERIVED`** on the strength of the
> nominal supersession — and **propagated that error into 002's brief.**
>
> **Phase 1 of 002 disproved it from the source.** `$(1,257)M` appears at **p.30 (Note 18),
> p.44, p.45 (narrative) and p.46 (reconciliation)**, and the identity closes exactly.
> **The earlier `1239` artifact was right.**
>
> **⇒ The separability test is 3 of 3 DISCLOSED, not 2 of 3** — the stronger reading. **And the
> lesson travels: a *supersession* claim is itself an evidence claim and needs the same page-level
> verification as any other. "Newer artifact wins" is not a validation.**

## 2. The reconciliation residual — V-2

`value-checks.yaml` carries `segments_sum_to_total` at **`fail`** level. Run in-line:

```
-542 (Space) + 1,656 (Connectivity) + (-1,257) (AI) = 143 ... signed
```

⚠️ **The residual is ZERO on the filed signs, and the CLOSURE is the trap.** The segments sum to
**$(143)M** and the consolidated line is **$(143)M** — **`7,814 − 7,957 = (143)` closes exactly.**
But the **platform's served layer returns `OperatingIncomeLoss: +143,000,000`** — the **DA-23
sign strip**, quantified by 002 as **16 of 20** served SPCX facts.

**⇒ V-2 resolves as: residual = 0 on the filed signs, and the apparent `+143` is a DA-23 artefact,
not a residual.** **A SOTP built on the served layer would reconcile to the wrong number with no
error raised.**

## 3. Preflight checklist

| Check | Result |
|---|---|
| Three segments with discrete filed revenue lines | ✅ **3 of 3** |
| Three segments with discrete filed operating results | ✅ **3 of 3** — the AI line is **FILED** |
| Segments sum to consolidated | ✅ **exact on filed signs** (`7,814 − 7,957 = (143)`) |
| Component identity available per segment | ✅ derived gross profit − opex closes on all three |
| Market print available | ✅ live quote **$152.71**, plus the dated constitution anchor |
| Share count available | ✅ **13,176,000,000** at 2026-06-30, closes exactly |
| Comparability set | ⚠️ **partition admits 0 of 11** — the regimes are sourced from SPCX's own data |
| **Cursor dilution** | ✅ **RESOLVED** — 391,041,680 shares, closed 2026-08-14 |

**⇒ Preflight PASSES. The SOTP proceeds.**
````

## Artifact — artifacts/SPCX/2026-09-19_sotp-valuation_retrieval-scope.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-1/PIL-6"
ticker: SPCX
skill: sotp-valuation
mode: retrieval-scope
generated_at: 2026-09-19T14:25:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07305f5d5391"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-06"
    chosen_reading: "Sources are admitted by whether they can price the SPECIFIC segment. A source that prices SPCX as one company cannot price a segment of it, and a captive-integrated segment has no transaction price to be sourced at all."
entity_claims:
  - claim_id: "sotprs-admitted-comparators"
    ticker: SPCX
    metric: count_of_admissible_comparators
    value: 0
    unit: count
    basis: "of eleven named comparators across P6's partition; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "this thesis's comps artifact — the partition, with each exclusion classed"
key_metrics:
  admissible_comparators: 0
---

# SPCX × sotp-valuation × retrieval-scope

**Which sources the anchor admits, and which it excludes.**

## 1. The admission rule

> **A source is ADMITTED if it can price the segment being valued. A source that prices SPCX as one
> company cannot price a segment of it. And a source that requires a transaction price is
> inadmissible for a segment that has none.**

## 2. ADMITTED

| Source | Status | What it supplies |
|---|---|---|
| **SPCX 10-Q, Note 18** (`spcx-20260630.htm`) | ✅ **PRIMARY** | All three segments' revenue and operating results, with the component identity |
| **The `ProductOrServiceAxis` decomposition** | ✅ admitted | The sub-segment cuts P2/P3/P4 read (this thesis's `revenue-decomp`) |
| **The live NASDAQ quote** | ✅ admitted — **at the END only** | The market print. `get_quote`, **never** `get_price_history` (**PRICE_ACCESS_PREMATURE**) |
| **The constitution's dated anchor** | ✅ admitted as the **second** price basis | A governance reference with its own date and basis |
| **8-K `0001628280-26-056945`** (2026-08-14) | ✅ admitted | The Cursor consideration: **389,289,254 + 1,752,426** shares |
| **`003/_cross/` curve and map** | ✅ **cross-check only** | Confirms; never supplies |
| **002's validated set** | ✅ admitted — **with its basis**, per 002's rule | Grades plus bases |
| **Constitution F5a/F5b/F5c, A4, P10, DA register** | ✅ admitted as **bounds** | They define what may not be claimed |

## 3. EXCLUDED

| Source | Class | Why |
|---|---|---|
| **All eleven named comparators** | ❌ **partition admits 0 of 11** | `loss_making` (RKLB, FLY) · `P11` (IRDM, GSAT) · `PARTIAL` (ASTS, VSAT) · `non_disclosure` (MSFT, GOOG, NVDA, VRT) |
| **`get_segment_data`** | ❌ **BROKEN** | Hard-errors at SPCX (`column "k" does not exist`); elsewhere sums across two years and two durations. **003 recorded it first** |
| **`get_price_history` for the `late` rows** | ❌ **REFUSED** | `PRICE_ACCESS_PREMATURE` — *"price is the final check, not the raw material."* **004 is the first `late` thesis here** |
| **A consolidated earnings multiple** | ❌ **INADMISSIBLE, not merely unattractive** | SPCX's DA-23-corrected result is **$(143)M** — a loss. The constitution bars comps as primary for a pre-profit issuer |
| **A consolidated forward DCF** | ❌ **barred outright** | Fails the ≥3-year positive-FCF limb. **`reverse-dcf` is admissible because it forecasts nothing** |
| **Analyst segment estimates** | ❌ | Not the filer's taxonomy |
| **The 1M-satellite / 100 kW-per-tonne filing** | ❌ **A4 / P10** | A filed aspiration with no revenue line |
| **Any single blended multiple** | ❌ **barred** | *"A different claim"* — the constitution makes SOTP primary for multi-segment issuers precisely so this is not done |
| **`~$1.62T` as a *current* price** | ❌ as a live figure | ✅ admitted as a **dated print**. It **does not reconcile** on the filed share count (implies **$122.95** vs an IPO at `$135.00`) |

## 4. The three exclusions that matter most, and why each is different

| Exclusion | Its nature | Consequence |
|---|---|---|
| **DA-06 for Space** | **A missing TRANSACTION PRICE** | No external multiple is borrowed; Space's value comes from **contribution**. Not a data gap — a structural absence |
| **P11 for Connectivity** | **A PRICE-FORMATION problem** | IRDM and GSAT are **priceable and still inadmissible**. **Live data makes the boundary verifiable, not removable** |
| **`non_disclosure` for AI** | **A SEGMENT-BOUNDARY problem** | MSFT's and GOOG's compute are **cost centres**, not segments. **No segment multiple exists to borrow** |

**⇒ The three fail for three different reasons — earnings, price formation, and disclosure. A single
comp screen would not have found them.**

## 5. What the anchor publishes

| Per segment | Source it is built from |
|---|---|
| **Space** | **SPCX's own filed segment data**, with a `MODELED` revenue-multiple range and the **DA-06 non-comparability flag** |
| **Connectivity** | **SPCX's own filed segment margin**, cross-checked against **terrestrial broadband** — not satellite peers |
| **AI** | **INVESTED CAPITAL** (company-level capex attribution, per default **D-3**), with the other two framings reported alongside |

**And the market side publishes two bases** — the live quote and the dated constitution anchor —
**with the spread between them reported as its own component**, per round 4.
````

## Artifact — artifacts/SPCX/2026-09-19_sotp-valuation_triggers.md
````markdown
---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-1/PIL-6"
ticker: SPCX
skill: sotp-valuation
mode: triggers
generated_at: 2026-09-19T14:20:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07305f5d5391"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "A trigger that reads a served figure must name the FILED basis, because the served layer inverts the sign in 16 of 20 SPCX OperatingIncomeLoss facts. Every trigger below names the datum and the filed reading."
entity_claims:
  - claim_id: "sotpt-trigger-count"
    ticker: SPCX
    metric: falsifier_count
    value: 7
    unit: count
    basis: "checkable triggers over the SOTP; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: MODELED
    source: "this artifact"
key_metrics:
  falsifier_count: 7
---

# SPCX × sotp-valuation × triggers

**What would overturn the anchor.** Each trigger names **the datum to read** and **the threshold**,
so it fires mechanically.

## T-1 — Connectivity's operating margin stops rising

**Read:** Connectivity income from operations ÷ segment revenue, filed, on the **filed segment
basis**. **Threshold:** the margin **falls year over year**, or **flatlines while ARPU continues to
fall**.

**Why:** the **~313×** headline rests entirely on Connectivity being the one profitable segment with
demonstrated operating leverage. **A flat margin with falling ARPU is the price-erosion reading
winning over the mix-shift reading** — which is **P2's falsifier** and would remove the anchor's only
positive-value segment.

## T-2 — The DA-23 sign defect reaches the segment tables

**Read:** the component identity (`gross profit − opex`) per segment, on the **filed** signs.
**Threshold:** any segment where the served value differs from the filed value.

**Why:** the defect is **already live on the consolidated line** (`+143` served vs `(143)` filed).
**If it reaches a segment line, the SOTP's inputs are wrong at the source.** 002's census found it in
**16 of 20** served facts — so this is a **probability, not a hypothesis.**

## T-3 — Coverage moves toward 1.0×

**Read:** operating cash flow ÷ investing outflow, from the cash flow statement.
**Threshold:** **≥ 1.0×** over a trailing period.

**Why:** that is **P5's falsifier, stated verbatim** — *"an internal coverage ratio at or above 1.0×
over the SOTP's horizon, which would mean the build is self-funding and the capital constraint is not
binding."* **Current: 0.1005×.** Firing it would **dissolve the thesis-level binding constraint**.

## T-4 — Starship cadence resumes

**Read:** Starship launches per period, filed.
**Threshold:** **≥ 3 in a period** — returning to the H1 2025 rate from which it fell to 1.

**Why:** P4's binding constraint is **`MANUFACTURING_RATE`** — the F5b expended second-stage curve —
and the anchor does not price a transition the filings show has not started. **A resuming cadence
means the F5a floor is becoming real**, which changes the Space regime from
revenue-multiple-with-a-non-comparability-flag toward an architecture-based cost position.

## T-5 — A comparability partition entry changes class

**Read:** the P11 register and the coverage tiers.
**Threshold:** **any of IRDM, GSAT, RKLB ceasing to be a deal security** — a terminated merger, or a
closed one.

**Why:** the partition currently **admits 0 of 11**. A **closed** deal removes the spread and makes
the security's price a fundamental — **which would admit the first comparator this anchor has ever
had.** `IRDM`'s merger has a **$223.6M termination fee** and needs **> $3.0bn cash**; `GSAT`'s close
is expected **2027**.

## T-6 — The live price feed stops

**Read:** `market_data.py --ticker SPCX` status.
**Threshold:** **refusal, or a regression to `market_data_stage: none`.**

**Why:** this is the registered **`market_data_stage_regresses`** trigger. The discount measure is
**print-bound**; if the feed stops, the anchor reverts to the constitution's dated anchor — **which
does not reconcile on the filed share count** (it implies **$122.95/share** against an IPO at
`$135.00`).

## T-7 — A constitution bump to 1.6.0

**Read:** `constitution.md` version.
**Threshold:** **1.6.0 lands** — the queued batch of **30 amendments (3 PATCH, 27 MINOR, 0 MAJOR)**.

**Why:** it **marks all 42 artifacts `stale`**. Registered as the `constitution_bump` expiry trigger;
named here because **it is the one trigger that fires on a schedule rather than on a disclosure.**

## Trigger summary

| # | Datum | Threshold | Fires ⇒ |
|---|---|---|---|
| **T-1** | Connectivity segment margin | falls YoY, or flat with falling ARPU | **the anchor loses its only positive segment** |
| **T-2** | Segment component identity | served ≠ filed | inputs wrong at source |
| **T-3** | Coverage ratio | **≥ 1.0×** | **`CAPITAL` stops binding — thesis-level** |
| **T-4** | Starship cadence | ≥ 3/period | the F5a floor becomes real |
| **T-5** | P11 register | any deal security normalises | **the first admissible comparator** |
| **T-6** | Live feed | refusal / regression | the discount reverts to the unreconciled anchor |
| **T-7** | Constitution version | 1.6.0 | all 42 artifacts stale |

## What does NOT trigger

- **A price move.** The anchor publishes a **range** and two price bases. **A price change moves the
  comparison, not the valuation.**
- **A quarter of revenue growth in any segment.** The regimes are **multiple regimes**; the finding
  is the *shape*, not the level.
- **Cursor's contingent awards vesting.** **73,493,373** shares — a **dilution note**, per default
  **D-2**, not a trigger. Recorded so it is not mistaken for one.
````

