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
