---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-1/PIL-6"
ticker: SPCX
skill: sotp-valuation
mode: triggers
generated_at: 2026-09-19T14:20:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07305f5d5391"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "A trigger that reads a served figure must name the FILED basis, because the served layer inverts the sign in 16 of 20 SPCX OperatingIncomeLoss facts. Every trigger below names the datum and the filed reading."
entity_claims:
  - claim_id: "sotpt-trigger-count"
    ticker: SPCX
    metric: falsifier_count
    value: 7
    unit: count
    basis: "checkable triggers over the SOTP; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: MODELED
    source: "this artifact"
key_metrics:
  falsifier_count: 7
---

# SPCX × sotp-valuation × triggers

**What would overturn the anchor.** Each trigger names **the datum to read** and **the threshold**,
so it fires mechanically.

## T-1 — Connectivity's operating margin stops rising

**Read:** Connectivity income from operations ÷ segment revenue, filed, on the **filed segment
basis**. **Threshold:** the margin **falls year over year**, or **flatlines while ARPU continues to
fall**.

**Why:** the **~313×** headline rests entirely on Connectivity being the one profitable segment with
demonstrated operating leverage. **A flat margin with falling ARPU is the price-erosion reading
winning over the mix-shift reading** — which is **P2's falsifier** and would remove the anchor's only
positive-value segment.

## T-2 — The DA-23 sign defect reaches the segment tables

**Read:** the component identity (`gross profit − opex`) per segment, on the **filed** signs.
**Threshold:** any segment where the served value differs from the filed value.

**Why:** the defect is **already live on the consolidated line** (`+143` served vs `(143)` filed).
**If it reaches a segment line, the SOTP's inputs are wrong at the source.** 002's census found it in
**16 of 20** served facts — so this is a **probability, not a hypothesis.**

## T-3 — Coverage moves toward 1.0×

**Read:** operating cash flow ÷ investing outflow, from the cash flow statement.
**Threshold:** **≥ 1.0×** over a trailing period.

**Why:** that is **P5's falsifier, stated verbatim** — *"an internal coverage ratio at or above 1.0×
over the SOTP's horizon, which would mean the build is self-funding and the capital constraint is not
binding."* **Current: 0.1005×.** Firing it would **dissolve the thesis-level binding constraint**.

## T-4 — Starship cadence resumes

**Read:** Starship launches per period, filed.
**Threshold:** **≥ 3 in a period** — returning to the H1 2025 rate from which it fell to 1.

**Why:** P4's binding constraint is **`MANUFACTURING_RATE`** — the F5b expended second-stage curve —
and the anchor does not price a transition the filings show has not started. **A resuming cadence
means the F5a floor is becoming real**, which changes the Space regime from
revenue-multiple-with-a-non-comparability-flag toward an architecture-based cost position.

## T-5 — A comparability partition entry changes class

**Read:** the P11 register and the coverage tiers.
**Threshold:** **any of IRDM, GSAT, RKLB ceasing to be a deal security** — a terminated merger, or a
closed one.

**Why:** the partition currently **admits 0 of 11**. A **closed** deal removes the spread and makes
the security's price a fundamental — **which would admit the first comparator this anchor has ever
had.** `IRDM`'s merger has a **$223.6M termination fee** and needs **> $3.0bn cash**; `GSAT`'s close
is expected **2027**.

## T-6 — The live price feed stops

**Read:** `market_data.py --ticker SPCX` status.
**Threshold:** **refusal, or a regression to `market_data_stage: none`.**

**Why:** this is the registered **`market_data_stage_regresses`** trigger. The discount measure is
**print-bound**; if the feed stops, the anchor reverts to the constitution's dated anchor — **which
does not reconcile on the filed share count** (it implies **$122.95/share** against an IPO at
`$135.00`).

## T-7 — A constitution bump to 1.6.0

**Read:** `constitution.md` version.
**Threshold:** **1.6.0 lands** — the queued batch of **30 amendments (3 PATCH, 27 MINOR, 0 MAJOR)**.

**Why:** it **marks all 42 artifacts `stale`**. Registered as the `constitution_bump` expiry trigger;
named here because **it is the one trigger that fires on a schedule rather than on a disclosure.**

## Trigger summary

| # | Datum | Threshold | Fires ⇒ |
|---|---|---|---|
| **T-1** | Connectivity segment margin | falls YoY, or flat with falling ARPU | **the anchor loses its only positive segment** |
| **T-2** | Segment component identity | served ≠ filed | inputs wrong at source |
| **T-3** | Coverage ratio | **≥ 1.0×** | **`CAPITAL` stops binding — thesis-level** |
| **T-4** | Starship cadence | ≥ 3/period | the F5a floor becomes real |
| **T-5** | P11 register | any deal security normalises | **the first admissible comparator** |
| **T-6** | Live feed | refusal / regression | the discount reverts to the unreconciled anchor |
| **T-7** | Constitution version | 1.6.0 | all 42 artifacts stale |

## What does NOT trigger

- **A price move.** The anchor publishes a **range** and two price bases. **A price change moves the
  comparison, not the valuation.**
- **A quarter of revenue growth in any segment.** The regimes are **multiple regimes**; the finding
  is the *shape*, not the level.
- **Cursor's contingent awards vesting.** **73,493,373** shares — a **dilution note**, per default
  **D-2**, not a trigger. Recorded so it is not mistaken for one.
