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
