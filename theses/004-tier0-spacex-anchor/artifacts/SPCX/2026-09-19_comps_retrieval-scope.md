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
