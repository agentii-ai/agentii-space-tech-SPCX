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
