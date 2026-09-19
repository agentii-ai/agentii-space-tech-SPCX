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
