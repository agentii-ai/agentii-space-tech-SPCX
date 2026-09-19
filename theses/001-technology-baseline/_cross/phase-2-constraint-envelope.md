---
thesis_id: "001-technology-baseline"
pillar: PIL-2
ticker: GOOG
skill: secular-trends
mode: methodology
generated_at: 2026-09-18T13:10:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-18
definitions_used:
  - da_id: "DA-04"
    chosen_reading: "1 MW = continuous delivered electrical load at the payload, not nameplate and not including conversion losses"
  - da_id: "DA-11"
    chosen_reading: "excluded entirely — this artifact uses facility-load reasoning, not SPCX's IT-load convention"
  - da_id: "DA-15"
    chosen_reading: "rejection temperature reported as an explicit variable across 300–500 K, never a single assumed value"
  - da_id: "DA-16"
    chosen_reading: "all derivations here are MODELED; no flown radiator has been demonstrated by any listed issuer"
evidence_grade: MODELED
deal_security_basis: not_applicable
unresolvable: false
---

# Phase 2 — Orbital Power and Thermal Envelope (PIL-2)

**Purpose**: derive the F1 and F2 bounds from first principles, per constitution P2 — with
units, shown arithmetic, and every competing definition (DA-15) reported rather than fixed.

**Headline result**: 1 MW of continuous orbital electrical load needs **~7,500 m² of
deployed surface** at a 300 K rejection temperature — of which **~2,420 m² is radiator**
and ~5,080 m² is solar array. Raising the rejection temperature to 500 K cuts radiator
area by **7.7×** but leaves the array untouched. The array, not the radiator, is the
dominant area term — and both scale linearly with compute power.

---

## F2 — Radiative rejection, across the DA-15 temperature range

In vacuum there is no convection and no conduction sink. All waste heat is radiated:

**P = ε · σ · A · (T_rad⁴ − T_sink⁴)**, σ = 5.6704 × 10⁻⁸ W·m⁻²·K⁻⁴, ε = 0.9,
T_sink ≈ 3 K (deep space, negligible at these temperatures).

| T_rad | εσT⁴ (W/m²) | Radiator area per MW | vs 300 K |
|---|---|---|---|
| **300 K** | 413 | **2,419 m²** | 1.00× |
| 350 K | 766 | 1,305 m² | 1.85× less |
| **400 K** | 1,307 | **765 m²** | **3.16× less** |
| 450 K | 2,092 | 478 m² | 5.06× less |
| **500 K** | 3,190 | **313 m²** | **7.72× less** |

**DA-15 in operation.** T⁴ dominates everything. A 50 K change at 300→350 K cuts radiator
area by 46%; the same 50 K at 450→500 K cuts it by another 34%. **Any orbital-compute
analysis that quotes a single radiator figure without its rejection temperature is
uninterpretable** — and the sector's published estimates do exactly that. This is the
single most load-bearing ambiguity in the orbital-compute debate.

**A physical caveat the derivation implies but does not solve**: a hotter radiator
requires a heat pump to lift heat from chip-junction temperatures (~350–400 K) to the
radiator, and the pump consumes power — becoming waste heat itself. The table above is
the *rejection* side only. Real systems at 400 K+ need a pump whose COP reduces the net
benefit. **Raising rejection temperature is not free, and the sector's claims that quote
high temperatures without a COP penalty are incomplete.**

## F1 — Solar array, with the full multiplier chain

1 MW of *continuous delivered* load, at cell-level beginning-of-life efficiency 30%
(triple-junction IMM, Spectrolab/SolAero class — `CLAIMED` spec, not filed):

| Step | Factor | Area |
|---|---|---|
| Cell level, BOL, continuous | 1,000,000 ÷ (1,361 × 0.30) | 2,449 m² |
| ÷ eclipse duty (0.63 sunlight fraction at ~500 km) | × 1.587 | 3,886 m² |
| ÷ array packing factor (0.85 — cells do not tile the panel) | ÷ 0.85 | 4,572 m² |
| ÷ end-of-life degradation (0.90 retention over mission life) | ÷ 0.90 | **5,080 m²** |

The naive figure (2,449 m²) **understates the real requirement by 2.1×**. Reconciled
against the independently published estimate of ~5,640 m²/MW — the residual gap is
consistent with a lower assumed efficiency or a longer mission life.

**Note the asymmetry**: array area is **independent** of radiator temperature. Raising
T_rad shrinks the radiator only.

## The combined envelope — and why BWXT matters

| Configuration | Array | Radiator | **Total deployed area/MW** |
|---|---|---|---|
| Solar + 300 K rejection | 5,080 m² | 2,419 m² | **7,499 m²** |
| Solar + 400 K rejection | 5,080 m² | 765 m² | 5,845 m² |
| Solar + 500 K rejection | 5,080 m² | 313 m² | 5,393 m² |
| **Nuclear + 500 K rejection** | **0 m²** | 313 m² | **313 m²** |

**The nuclear row is the finding.** A reactor removes the array *entirely* — no eclipse
duty, no battery mass, no packing factor, no degradation chain. Total deployed area falls
from ~7,500 m² to ~313 m² per MW, a **24× reduction**, and it eliminates the eclipse
battery, which F1 identifies as a first-order mass driver.

This is the concrete, quantitative reason **BWXT (space nuclear power and thermal
propulsion)** sits in the enabling layer: it is the only asset in the universe that acts
directly on F1 *and* F2 simultaneously. It is also why a thesis that ignores nuclear
power is modelling a strictly worse system than the one that may actually get built.

## Terrestrial comparison — the number that decides P5

| | Orbital (solar, 300 K) | Terrestrial |
|---|---|---|
| Surface area per MW | ~7,499 m² deployed | ~200–400 m² building footprint |
| Heat rejection mechanism | radiation only, T⁴-limited | chillers + evaporative towers, COP 2–3 |
| Rejection area per MW | 2,419 m² | ~0 m² of *deployed* surface — towers are compact |

**Orbital systems need roughly 20–35× the surface area per MW.** That comparison is the
P5 crux and it is structural, not a cost curve that learning could bend: a cooling tower
rejects heat to the atmosphere by evaporating water, and vacuum offers no such shortcut.

**But there is a counter-argument the table also exposes**: terrestrial data centres are
themselves constrained by *power availability and interconnect queues*, not by cooling
area. On a land-and-power-constrained basis the comparison is less lopsided than the
area column suggests — which is exactly why DA-05's three terrestrial comparators produce
a 5–10× spread and why P5 reports all three.

## Mass and launch-cost coupling

Using rough areal densities (radiator ~8 kg/m² incl. fluid loops; array ~6 kg/m² incl.
structure — both `MODELED`, neither disclosed by any issuer):

| Configuration | Mass per MW | Launch cost at F5 floor ($46–92/kg) |
|---|---|---|
| Solar + 300 K | ~50 t | **$2.3M–4.6M per MW** |
| Nuclear + 500 K | ~2.5 t + reactor mass | reactor-dominated; not comparable |

**This connects F1/F2 to F5.** Power and thermal alone cost the F5 propellant floor
**$2.3–4.6M per MW of compute** before a single GPU is launched. At the reported
orbital-compute infrastructure figure of $10,000–40,000 per kW (= $10–40M per MW), power
and thermal are therefore a **meaningful but not dominant** share — which is an
uncomfortable result for the "it's all thermal" framing and worth stating plainly.

## PIL-2 falsifier evaluation

| Field | Value |
|---|---|
| metric | `listed_issuer_orbital_compute_revenue_disclosed` |
| threshold | 0, op `>` |
| **Observed** | **0** — verified against SPCX (AI segment is ground-based, 1.4 GW nameplate IT load), GOOG (Suncatcher is pre-prototype, `CLAIMED` only), NVDA (no orbital revenue line), MSFT |
| **Verdict** | **HOLDS** — no listed issuer discloses orbital-compute revenue on any of the three readings in DA-20 |

**Field confirmation that the constraint is live**: Starcloud-1 carried an NVIDIA H100
and **cannot run it at full power because cooling capacity is insufficient**
(`CLAIMED` — press, private company, admissible under Q-4 as CLAIMED only). This is F2
observed in flight rather than derived — the first empirical data point in the thesis.

---

## Corrections and open gaps

1. **The heat-pump COP gap.** The F2 table is the rejection side only. A defensible
   orbital-compute model needs a net-power figure including pump work at elevated
   rejection temperatures. **Not yet modelled** — carried to Phase 6.
2. **Radiator areal density is modelled, not sourced.** 8 kg/m² is a placeholder. Phase 3
   should attempt to source it from VRT (terrestrial comparator) or MDA (NOC/BA adjacent).
3. **The "it's all thermal" framing is overstated.** Power+thermal is ~$2.3–4.6M/MW of
   launch cost against a reported $10–40M/MW all-in — meaningful, not dominant. The
   dominant term is the compute hardware and its replacement rate, which this phase did
   not model.
4. **BWXT's space-nuclear component is not separable** from its terrestrial nuclear
   revenue in current disclosures (already logged in `thesis.md → known-open`). The
   nuclear row above is therefore an engineering bound, not an investable claim.
