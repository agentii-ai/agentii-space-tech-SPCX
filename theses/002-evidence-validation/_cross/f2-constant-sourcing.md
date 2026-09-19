---
thesis_id: "002-evidence-validation"
artifact: f2-constant-sourcing
pillar: [PIL-2]
ticker: cross
skill: synthesis
mode: default
task: T901
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
schema: f2_constant_sourcing
evidence_grade: MODELED
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM
definitions_used:
  - da_id: DA-25
    chosen_reading: >
      The radiator areal-density constants are PER-UNIT figures that are NORMALISATIONS,
      not derivations: none is reproducible from any issuer's audited tables, and the
      derivation path for each class is unstated. This is DA-25's exact shape applied to a
      generic engineering constant rather than an issuer-defined one. The consequence is
      the finding this artifact rests on: 001's 8 kg/m² placeholder is never declared as a
      class choice, and it is a CREWED/ISS-class value (the 5.3-11 band) applied to a
      mass-optimized uncrewed platform whose alternatives run 1.0-3.5 kg/m² — a 2.7-5x
      mismatch IN F2's OWN FAVOUR. The two grounds for downgrading F2 are independent:
      the band is wide (±35% to ±83% depending on scope, breaching ±50% in two of three
      scopes), and the COP penalty needs no source at all (+42.9% to +150.0%).
  - da_id: DA-23
    chosen_reading: >
      NOT APPLICABLE — no issuer operating-income line is read by this artifact. Recorded
      explicitly rather than omitted, per the standing rule that an absent detector must
      be declared, never left to read as a passed check. The gross-profit bound (DA-23
      detector 2) cannot act here for the same reason: there is no gross profit to bound
      against.
citations:
  - figure: "SPCX facility-side power vs compute basis (the PIL-4 input)"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 4
    url: "https://agentii.ai/v/SPCX/ect1/4"
    located_via: read_source_pages
  - figure: "GOOG: no Suncatcher/satellite/orbit disclosure across 216 filing + 17 transcript pages"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 15
    url: "https://agentii.ai/v/GOOG/sec156/15"
    located_via: read_source_pages
---

# F2 Constant Sourcing — the phase deliverable (T901)

> **Spec §6 required this artifact and it did not exist** until Phase 2's BWXT task flagged the
> gap. It synthesises the four Phase 2 artifacts that bear on F2:
> `GOOG/…_secular-trends_methodology.md`, `BWXT/…_secular-trends_methodology.md`,
> `BWXT/…_supply-chain_methodology.md`, `VRT/…_unit-economics_methodology.md`.

## Outcome: F2 is a QUALITATIVE bound, and the falsifier is not evaluable as written

**Two independent acceptance-test breaches**, either of which alone would force the downgrade:

| Ground | Finding |
|---|---|
| **1 — The band is WIDE, not undefined — corrected at T901 review** | An earlier draft of this artifact said *"the band is undefined, not wide."* **That was wrong, and the correction strengthens the finding.** The constants **are** reachable by direct search — just not by any registry skill. **Radiator areal density spans 1.0–11 kg/m²: ±83% un-scoped, ±56% advanced-class, ±35% crewed-class. TWO OF THREE SCOPES BREACH ±50%**, so **the downgrade survives even with the constants in hand.** That is a stronger verdict than "no data": the data exists, and it is too wide to support a point value. |
| **2 — The derivable axis alone spans +43% to +150%** | The COP penalty needs **no source** — it follows from thermodynamics given a stated cold-side temperature. `f = 1/(1−1/COP)`, `COP_Carnot = T_r/(T_r−T_c)`: **313 m²/MW** (001, no pump) → **447** (+42.9%, Carnot) → **783** (+150.0%, realistic 50%-Carnot). |

**⚠️ And 001's 8 kg/m² placeholder was never declared as a class choice.** It is a **crewed/ISS-class** value (the 5.3–11 band) applied to a **mass-optimized uncrewed platform**, whose alternatives run **1.0–3.5 kg/m²**. That is a **2.7–5× mismatch in F2's own favour** — the placeholder made orbital compute look *better* than the relevant hardware class supports. F2's published area figures inherit that.

**⚠️ A CONTRACT GAP THAT MAKES PIL-2 UNEVALUABLE BY CONSTRUCTION.** PIL-2's falsifier names `source=peer_reviewed_literature_or_flown_hardware_disclosure`. The artifact contract's `citation_url_wellformed` rule is level **`fail`** and its pattern admits **only `agentii.ai` URLs**. **So the source class PIL-2 tests against cannot be recorded in any artifact.** The falsifier is not merely hard to evaluate — **a passing evaluation would be unrecordable.** Escalated as first-class input to P7's disposition census and to the amendment queue.

**Sourcing basis for the two claims this artifact rests on.** The **PIL-4 facility-draw input
is a transcript, not a filing** — SPCX's earnings call discloses facility-side power against the
same compute basis: [📄 SPCX transcript p.4](https://agentii.ai/v/SPCX/ect1/4). And the **GOOG
absence is quantified, not asserted**: Alphabet's entire SpaceX-related SEC disclosure in Q2 2026
is a **$94.1B equity stake** and **$99.0B of earnings** across **216 filing pages and 17
transcript pages** in which `Suncatcher`, `satellite`, `orbit` and `orbital` return **zero**
hits — [📄 GOOG 10-Q p.15](https://agentii.ai/v/GOOG/sec156/15). **Not an oversight: correct
application of a materiality threshold.** The number PIL-2 needs will not be disclosed until it
is financially material — which is exactly when it stops mattering to the falsifier.

**And the falsifier as specified cannot be run by this platform at all.** PIL-2 tests against
`source=peer_reviewed_literature_or_flown_hardware_disclosure`. **No skill in this registry
can read peer-reviewed literature or flown-hardware documentation.** That is a **distinct
disposition from "no data exists"**: the test is specified against a source class the
platform cannot reach.

| Disposition | Applies to | Remedy |
|---|---|---|
| `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | The **issuer value** — no company discloses these constants | Name the disclosure that would resolve it; monitor |
| `UNRESOLVABLE-FROM-PLATFORM` | The **generic constants** — they exist in NASA/peer-reviewed sources the platform does not carry | Platform reach, not a research task |

## What survives — and it is robust

**Order 10³ m² and order 10¹ t per MW.** Stable across a **7.72× area range**, a **3× density
range** and a **2× COP penalty**. **The constraint still binds; it cannot be quoted to four
significant figures.** Any downstream thesis citing F2 must cite it as an order of magnitude.

## Two corrections to 001 that travel with this

**1. The 24× nuclear reduction is 9.6×–16.8×.** 001's figure varies **two things at once** —
it is `3.10× (array removal) × 7.72× (300→500 K)`. Unpriced, they compound; priced, they do not.

**2. The eclipse multiplier is 1.587×, not 8×.** A **dawn-dusk SSO has no eclipse**, so that
multiplier drops out entirely: array falls **5,080 → 3,201 m²/MW** (−34.8%). That is the *whole*
of what F1 can adjudicate for a Suncatcher-class orbit. The "8× more productive" claim implies
an **unstated reference terrestrial capacity factor of 18.6%** — at an assumed CF it is
trivially satisfied; at an unstated CF it has no truth value.

## The finding that CUTS THE OTHER WAY — nuclear's case is stronger than 001 argued

**Pricing the heat pump creates a 16× asymmetry between the two architectures.** The pump's
power penalty has to be rejected as *heat*, which costs:

| Architecture | Extra rejection area for the same pump penalty |
|---|---|
| **Solar** | **~5,080 m²/MW** of additional array |
| **Nuclear** | **~313 m²/MW** of radiator |

**Solar + 500 K with a realistic pump is 1.80× WORSE than solar + 300 K.** Raising rejection
temperature is **self-defeating without nuclear**, because the solar architecture pays the pump
penalty in array area ~16× over. 001 left this loop open and therefore understated *why* nuclear
matters — it is not merely a 24× area saving, it is **what makes the temperature effect
available at all.**

## The funded-programme gap is worse than 001 knew

BWXT does have named programmes (NASA/DoW/DOE; NTP development with NASA; Antares Mark-0
criticality on TRISO/HALEU; Golden Dome; a $21M DOE award). **But the funded, named NASA
programme is NTP — nuclear *thermal* propulsion, which throws its heat out the nozzle — not
F2's closed-cycle nuclear-electric architecture.**

**The named programme is the wrong physics for the constraint F2 describes.** A closed-cycle
NEP system must reject all its waste heat through radiators; NTP rejects most of it as exhaust.
The gap is not that the business is small — **it is that the funded work does not address the
constraint.**

## Notification — DELIVERED

Per the plan's Phase 2 acceptance test, **003 and 009 both carry written notifications** that
F2 has downgraded, with the two corrections attached. Both files were appended on 2026-09-18.

**What this means downstream:** any thesis citing F2 must cite an **order of magnitude**, must
**not** quote 313 m²/MW or 24× as point values, and must record any terrestrial-cooling
escalator as `MODELED` rather than sourced.
