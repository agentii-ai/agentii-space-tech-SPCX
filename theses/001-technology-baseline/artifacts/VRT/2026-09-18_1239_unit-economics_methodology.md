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
