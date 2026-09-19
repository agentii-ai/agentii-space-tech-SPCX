# Reproduce — 004 Tier 0: SpaceX Anchor

> Q8 contract 5 / Q36: the thesis-level reproduction recipe — the ONE file an external reviewer
> (compliance, LP, a new analyst) needs. Every artifact's frontmatter carries its own pins; this
> file aggregates them.

## Skills used — 7 executed across 7 tickers

**Nine further skills are CONSUMED from 003 and listed separately below. They generate no tasks.**

| skill | mode | vertical | depth / tickers | market data |
|---|---|---|---|---|
| `sotp-valuation` | all modes | models-and-pitches | **Deep** — SPCX | **`late`** |
| `revenue-decomp` | all modes | business-intelligence | **Deep** — SPCX | none |
| `reverse-dcf` | `essentials_modes` | quantitative-analysis | Standard — SPCX | **`late`** |
| `risk` | `essentials_modes` | equity-research-core | Standard — SPCX | none |
| `comps` | `essentials_modes` | models-and-pitches | Light — SPCX, RKLB, FLY, GSAT, IRDM, ASTS, VSAT, MSFT, GOOG, NVDA, VRT | none |
| `competitive` | `essentials_modes` | equity-research-core | Light — SPCX, RKLB, FLY | none |
| `growth-strategy` | `essentials_modes` | equity-research-core | Light — SPCX | none |

**19 distinct `(ticker, skill)` analyses → 37 mode-tasks** against a budget of `max_tasks: 40`.
**Measured, not estimated** (`tools/tasks_md.py`, 2026-09-19). Distribution: `comps` 11 ·
`competitive` 9 · `sotp-valuation` 5 · `revenue-decomp` 5 · `risk` 3 · `growth-strategy` 3 ·
`reverse-dcf` 1.

> **⚠️ The first measurement was 63, and the 26-task gap was a PARSER artifact, not scope.**
> `tasks_md.py` reads matrix rows **positionally** and has no concept of a consumed row, so §3b —
> written in the executed rows' shape to satisfy `plan_audit` I2 — was dispatched as work.
> **Fixing it was a column shape, and it is worth more than any single phase in this plan.**

### Consumed from 003 — cited, never re-run

`business-model` · `unit-economics` · `operational-kpi` · `recent-quarter` · `ratio-analysis` ·
`peer-bench` · `sector-overview` · `secular-trends` · `what-if`

Paths and purposes are in `spec.md` §3b. **These are excluded from the hash table below** —
their reproducibility is 003's, and citing 004 hashes for them would misattribute the work.

### `skill_pin` — real per-skill content hashes

`dispatch.skill_version_hash()` computes the **sha256 of the skill directory** (`SKILL.md` +
`references/`), truncated to 12 hex. Marketplace version labels are human-readable only; **the hash
is the machine truth (Q57).**

| skill | sha256 (12 hex) |
|---|---|
| `sotp-valuation` | `07305f5d5391` |
| `reverse-dcf` | `b42ad3a44570` |
| `revenue-decomp` | `037b396ab004` |
| `comps` | `264697c3872a` |
| `competitive` | `826995c722a4` |
| `risk` | `953fc5d396e7` |
| `growth-strategy` | `ab94b90ee0ff` |

> **✅ Method cross-checked against 003's validated set.** 003 published six hashes it had
> reproduced exactly from 001's. **Two of 004's computed values — `competitive
> 826995c722a4` and `risk 953fc5d396e7` — match 003's exactly.** Same validated function, same
> skills, same values. **The other five are computed, not inferred.**

> ### ⚠️ `skill_pin: none` is the declared sentinel — and it is deliberate
>
> A thesis spans many skills, **so there is no single hash to pin at the thesis level.** 003
> recorded the trap: its `skill_pin` read `registry-1.0.0`, a **whole-registry version**, which
> `tools/check_contract.py`'s `skill_pin_wellformed` rule names as the worst case — *"it reads as a
> pin, passes every check, and **pins NOTHING**."* **004 declares `none` and carries the real
> hashes above, where they can be checked.**

## The five pins

| pin | value |
|---|---|
| `constitution_pin` | **`1.5.0`** — re-pinned at clarify round 2 (was `1.4.0`, one MINOR stale). Brings **DA-29** and **DA-30** into scope; DA-30 governs §1c's component-identity rule |
| `assumption_pin` | `"2"` |
| `skill_pin` | **`none`** — sentinel; per-skill hashes above |
| `as_of` | **`2026-09-18`** (spec + `thesis.md`) — with a **second, later** time reference: the live quote's `observed_at` **2026-09-18** / `retrieved_at` **2026-09-19** |
| `corpus_version` | `agentii-2026-09-18` |

> **⚠️ `as_of` is the subtle one on this thesis.** Every figure 001–003 quote is on a **dated,
> historical** basis. 004 additionally carries a **live observation**, and the two are **not the
> same time reference** — which is why `entities.md`'s `quote_observation` schema separates
> `observed_at` from `retrieved_at`. **The price basis ($152.71 live vs ~$1.62T / $135.00 dated)
> travels with every market-referenced figure, and the ~13.1% spread between them is itself a
> published finding.**

## Reproduction recipe

1. **Load the pins.** `constitution_pin 1.5.0` — and note the queued **1.5.0 → 1.6.0** (30
   amendments: 3 PATCH, 27 MINOR, 0 MAJOR) which **marks all 42 artifacts stale**. 004 registers
   `constitution_bump` as an expiry trigger for exactly this.
2. **Consume 003 first.** `_cross/launch-cost-curve.md` and `_cross/value-pool-map.md`, plus the
   nine SPCX artifacts in `spec.md` §3b. **Do not re-derive the curve or the map.**
   ⚠️ **`value-pool-map.md` E-03 was corrected on 2026-09-19** (two errors: a 49.08% revenue share
   that should read 32.77%, and an unsourced "1,438 total loss" where the consolidated result is
   143). **A reader holding a pre-correction copy will reproduce two wrong figures.**
3. **Capture the price — ⚠️ AT THE END, NOT HERE.** `data-tools/market_data.py --ticker SPCX
   --json` (keyless, source `nasdaq`) uses **`get_quote`**, which is permitted. **But the
   sequence matters:** `data-tools/refusal.py` refuses `get_price_history` for any `late`-stage
   skill — *"price is the FINAL CHECK for fundamental work, never the raw material"* — so **004
   fetches its price at Phase 7, not up front** (plan finding **F13**). ⚠️ **`live_snapshot.py`
   calls both entry points, so it must not be run against a `late` thesis's early phases.**
   Stamp `observed_at` **and** `retrieved_at`. **Where the feed refuses, record the refusal** —
   the absence is the finding.
4. **Read segment facts via `search_xbrl_facts(…, view=detailed)`.** ⚠️ **NOT
   `get_segment_data` — it is broken** (`column "k" does not exist`), a finding **003's plan
   recorded first** (F4, from 002 §7).
5. **Run the gates** — `plan_audit.py` (I1–I4) and `clarify_scan.py`, and where they **cannot**
   reach: **I5 (market-data-stage) and I6 (formability) do not exist**, and both of 004's central
   round-3/4 defects passed every check that does.

## `corpus_version` caveat — stated plainly

`agentii-2026-09-18`. **The corpus carries no space sector tag**, so retrieval by sector returns
zero by construction; and **`search_by_analogue` is a dead end** because `analogue_tags` are
empty arrays on nearly every row. **Retrieve by full-text `search`, `practitioner`,
`investment_style` or `domain`.** See `brief.md` §1.
