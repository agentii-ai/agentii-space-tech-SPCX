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
