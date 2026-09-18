# Research Thesis: 008 — Tier 3b: Space Supply Chain & Components

**Constitution Ref**: constitution.md v1.4.0 (`constitution_pin: 1.4.0`)
**Created**: 2026-09-18
**Status**: **PLANNED — stub spec. Not frozen. No tasks may be generated.**
**Wave**: **1 — promoted at clarify round 2, 2026-09-18.** Swapped in for 003, because the
margin ladder says the component layer is where the returns are. Activates under
`max_theses_active: 6`; 001's slot frees on close.
**板块**: Tier 3b · **Binding constraint**: `MANUFACTURING_RATE`

> This file reserves the thesis ID and records the design intent. It is **not** a
> specification. Replace wholesale on activation.

## 0. Inherited baseline (to be completed on activation)

001 mapped the supply chain in `_cross/phase-3-production-supply.md` and its
`supply-chain` matrix rows, and produced two findings this thesis inherits:

- **A two-supplier duopoly in space-grade solar cells** — RKLB (SolAero) and BA
  (Spectrolab). Structurally concentrated, but **unpriced**: neither discloses the unit
  separately. 001's judgement: *"structural, but unpriced."*
- **MRCY earns a 0.03% operating margin** ($0.280M on $983.6M) — the billed "direct P2
  evidence" for radiation tolerance captures **no rent**. 001's reading: either the
  demand has not arrived, or radiation tolerance is *not a scarce input* the way F2's
  thermal area is.
- **BWXT's R&D is 0.5% of revenue** (versus FLY 60.8%, RKLB 35.2%) — the profile of a
  manufacturing franchise, not a space-reactor development programme. 001's line:
  *"physics claim stands; investment claim does not."*
- The **"capability real, business immaterial"** pattern, with 4–5 instances across the
  universe (GOOG, UTHR, MRCY, BWXT, NVDA), suppressing both disclosure and effort.

**Do not re-derive any of the above.** 008's question is different: whether the *tier as
a whole* converts a manufacturing-rate constraint into pricing power.

## 1. Research Question

**Across the component and subsystem layer, does anyone convert a genuine bottleneck
into pricing power — or does every node in this chain compete away its own scarcity?**

## 2. Universe Definition

| Ticker | Company | Role | Coverage |
|---|---|---|---|
| HWM | Howmet Aerospace | Engine and structural castings, fasteners | READY — 84 filings |
| TDG | TransDigm | Aerospace and defense components | READY — 112 filings |
| HEI | Heico | Replacement parts, electronic components | READY — 60 filings |
| WWD | Woodward | Control systems for propulsion | READY — 75 filings |
| CW | Curtiss-Wright | Actuation and defense electronics | READY — 60 filings |
| KTOS | Kratos Defense | Space/satellite C2, ground systems | READY — 56 filings |
| MRCY | Mercury Systems | Radiation-tolerant processing electronics | READY — 56 filings |
| AVAV | AeroVironment | Defense autonomy, stratospheric systems | READY — 87 filings |
| TER | Teradyne | Robotics and semiconductor test | READY — 62 filings |
| BWXT | BWX Technologies | Nuclear power and thermal propulsion **for space** | READY — 57 filings (sector: `nuclear_energy`) |
| KRMN | Karman Holdings | Missile/space and defense components | READY — 30 filings |
| MOG-A | Moog | Space/defense motion control, satellite components | **NOT_READY** — no data |
| TDY | Teledyne | Space imaging and IR detectors | **NOT_READY** — no data |
| ATRO | Astronics | Power distribution and lighting | **NOT_READY** — no data |

**Two coverage gaps are load-bearing and must be recorded, not proxied:** MOG-A
(motion control) and TDY (imaging/IR detectors) are the two most-cited gaps in this
tier. **MOG-A additionally carries a fund-sourced case in the knowledge corpus —
Brown Advisory, ~2.1–2.5× on cost, ~28–38% IRR — while carrying no issuer coverage.**
A case that cannot be validated against filings is a research liability, not an asset;
record the asymmetry.

**Sector-taxonomy hazard:** `BWXT` files under `industrial.nuclear_energy` and `TER`
under `tech.semiconductors`. **A sector screen on `aerospace_defense` will not surface
them.** This is a screening trap 001 documented and 008 must not fall into.

## 3. Skill Deployment Matrix (outline — not frozen)

1. **Pricing power test across the tier**: margin *direction* under revenue growth. A
   node with a real bottleneck shows expanding margin; a node competing away its
   scarcity shows flat-to-declining margin. **MRCY is the negative control** at 0.03%.
   **TDG is the positive control** — its pricing-power reputation is the tier's
   benchmark and the test of whether the defence-component model transfers to space.
2. **R&D intensity as a diagnostic.** 001 adopted R&D/revenue as a cross-issuer
   instrument distinguishing a *development programme* from a *manufacturing franchise*.
   008 applies it across the tier and asks what the distribution implies about who is
   actually building space capability.
3. **The radiation-tolerance question inverts**: F4's supplier earns nothing. Is
   radiation tolerance a scarce input, or is it a solved problem that was never a moat?
4. **BWXT's nuclear escape hatch** — 001 established a **24× deployed-area reduction**
   (7,499 → 313 m²/MW) is arithmetically available and *economically unattached*. Does
   any filing or programme move it from arithmetic to attributable revenue?
5. **⚠️ EXTEND THE MARGIN LADDER TO THE FULL TIER 3 LIST — assigned by 011 at clarify
   round 2, 2026-09-18.** 001's ladder covers **8 issuers, selected by which artifacts
   happened to get written** — a real selection concern that 011's pressure test could
   not resolve. **This is the test of whether the ladder is monotone or was monotone on
   the sample.** Method: compute operating margin for all **21 Tier 3 names** from
   component-identity-clean figures (per the Data-Integrity Register) and report the
   ordering with its rank correlation against distance-from-programme-risk and against
   revenue recurrence (aftermarket share). **If a fuller ladder is not monotone, 011's P1
   mechanism claim narrows or fails** — and reporting that is worth more than defending
   the claim. **This is bounded work: a margin is one income statement.**
   **Why it belongs in 008 and not 011**: 011 grades positions against 001's conclusions
   and does not re-research businesses; the ladder is a Tier 3 fact, and 008 owns Tier 3.

**Candidate binding constraint — `MANUFACTURING_RATE`.** The tier's constraint is
production throughput and unit cost, not demand. To be tested on activation.

## 4. Dependencies

- **002** — DA-23 discipline is mandatory; several names here are small-cap with
  irregular quarters.
- **005** (Tier 1) — the supply chain sells into the pure-plays' programmes.
- **009** (Tier 4) — the enabling layer is the adjacent rung; some names sit in both.
