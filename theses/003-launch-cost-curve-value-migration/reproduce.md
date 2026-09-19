# Reproduce — 003 Launch Cost Curve & Value Migration

> Q8 contract 5 / Q36: the thesis-level reproduction recipe — the ONE file an external
> reviewer (compliance, LP, a new analyst) needs. Every artifact's frontmatter carries its
> own pins; this file aggregates them.

## Skills used — 13 across 9 tickers

| skill | mode | vertical | depth / tickers |
|---|---|---|---|
| unit-economics | all modes | business-intelligence | **Deep** — SPCX, RKLB |
| operational-kpi | all modes | business-intelligence | **Deep** — RKLB, SPCX |
| business-model | `essentials_modes` | equity-research-core | Standard — SPCX, RKLB |
| what-if | `essentials_modes` | business-intelligence | Standard — RKLB, SPCX, FLY |
| recent-quarter | `essentials_modes` | equity-research-core | Standard — SPCX, RKLB, FLY, SATS, IRDM, GSAT, LUNR, PL, YSS |
| ratio-analysis | `essentials_modes` | quantitative-analysis | Standard — RKLB, SPCX, FLY, PL, YSS |
| peer-bench | `essentials_modes` | industry-analysis | Standard — RKLB, FLY, SPCX |
| competitive | `essentials_modes` | equity-research-core | Standard — FLY, IRDM, GSAT |
| secular-trends | `essentials_modes` | equity-research-core | Standard — SPCX, IRDM, GSAT |
| sector-overview | `essentials_modes` | industry-analysis | Standard — SPCX, RKLB, PL, YSS |
| growth-strategy | `essentials_modes` | equity-research-core | Light — LUNR, PL, YSS, SATS |
| supply-chain | `essentials_modes` | industry-analysis | Light — RKLB, PL |
| risk | `essentials_modes` | equity-research-core | Light — IRDM, GSAT, RKLB |

**45 distinct `(ticker, skill)` analyses.** At 001's measured **2.07×** mode expansion these
resolve to **~90 mode-tasks** against a budget of 80 — registered in `plan.md`'s Deviation
Register, pending owner sign-off, expiring 2026-10-02 at first `agentii.tasks` run.

### `skill_pin` — real per-skill content hashes

`dispatch.skill_version_hash()` computes the **sha256 of the skill directory** (`SKILL.md` +
`references/`), truncated to 12 hex. Marketplace version labels are human-readable only; the
hash is the machine truth (Q57).

**Method validated before use.** The implementation was checked against the six hashes 001
published and **reproduced all six exactly** (`operational-kpi 0730fd170124`, `unit-economics
e87ee63269a2`, `secular-trends e6b41dbb2426`, `supply-chain 8cb3ac1de486`, `competitive
826995c722a4`, `risk 953fc5d396e7`). The seven new hashes below are computed by the same
validated function, **not inferred**.

> **⚠️ AND THE VALIDATION STILL MISSED ONE — corrected 2026-09-19.** A 6/6 reproduction
> validated the **algorithm**; it could not validate a hash the algorithm was never asked to
> check. **`ratio-analysis` was published as `9b1d7a504789`, which is the
> `models-and-pitches` root — a directory that contains NO `SKILL.md` and has since been
> DELETED (`ca0c8b3`, "Fix the upgrade path: 5 orphan dirs…").** The correct value is
> **`2d27c7f751fa`**, confirmed three independent ways: the `quantitative-analysis` vertical
> root (the one the installer actually copies), the `agentii-plugin` symlink, and **the
> installed copy itself** in `~/.claude/skills/agentii/ratio-analysis`.
>
> **Why it happened, and why it is the interesting kind of error.** The pin was computed with
> `setdefault` over a glob, so where a name exists in **two** roots the winner is decided by
> **glob order, not by which root is valid** — `models-and-pitches` sorts before
> `quantitative-analysis`, so the skill-less directory won. **002 warned about exactly this**
> and named both values; the warning was recorded in a *different thesis* and did not travel.
> The lesson is not "hash more carefully" — it is that **a validation set drawn from known-good
> values cannot detect the error mode of the values it excludes.** The check that works is
> cross-root agreement plus a `SKILL.md` existence test, which is what this table now rests on.

| skill | version_hash | skill | version_hash |
|---|---|---|---|
| unit-economics | `e87ee63269a2` | competitive | `826995c722a4` |
| operational-kpi | `0730fd170124` | secular-trends | `e6b41dbb2426` |
| business-model | `9479220eef91` | sector-overview | `8fb208998401` |
| what-if | `87af28d574e9` | growth-strategy | `ab94b90ee0ff` |
| recent-quarter | `07d26b9c738b` | supply-chain | `8cb3ac1de486` |
| ratio-analysis | `2d27c7f751fa` | risk | `953fc5d396e7` |
| peer-bench | `8c91d57a0d74` | | |

A version change mid-thesis uses the new hash and **appends** to `skill_pins.jsonl` — never
overwritten (Q57).

## Five pins

All five are mandatory. An artifact missing any one is classified `resume` (partial-write
class) by `dispatch.resume_verdict()` and **silently re-run** — the filesystem is the
checkpoint (Q56).

| pin | value |
|---|---|
| `constitution_pin` | **1.5.0** — `constitution.md` sha256 `3d379aa4ef798839` |
| `assumption_pin` | **`"2"`** — `assumptions.yaml` v2, sha256 `0d0264e58a736568` |
| `skill_pin` | registry **1.0.0**; per-skill hashes above |
| `as_of` | **2026-09-18** |
| `corpus_version` | **`agentii-2026-09-18`** — see the caveat below |

**`assumption_pin` is unchanged from 001** — `assumptions.yaml` hashes identically
(`0d0264e58a736568`), so the two theses share one assumption set. Worth stating because a pin
that *looks* copied is here genuinely identical.

**⚠️ `corpus_version` caveat — a dated convention, not a retrieved corpus id.** No
corpus-version endpoint is exposed, so `agentii-2026-09-18` is a **date-stamped label** that
satisfies `g1_gate.FIVE_PINS`' *presence* requirement. It is **not** a machine-derived
corpus identifier, and it is not evidence that the corpus is frozen.

**⚠️ CORRECTED 2026-09-18 — do NOT use `data_freshness` as the freshness signal.** An earlier
version of this file called the `data_freshness` field *"the real freshness signal."* **That
is wrong.** Thesis 002 §7 established it as **UNUSABLE**: on the XBRL tools it reports
**`2027-04-12` — seven months in the FUTURE of `as_of = 2026-09-18`**, so it cannot be a
retrieval timestamp at all. **And the freshness stamps that ARE reachable disagree with each
other** — `2026-08-21`, `2026-08-25` and `2026-08-26` were all observed on this universe. A
reproduction should therefore treat **every** freshness field on this platform as
`UNVALIDATED-BY-PLATFORM` and confirm currency by **reading the filing's own period-end**,
not by trusting a stamp. `corpus_version: "UNPINNED"` is what 002 records, and it is the
honest value.

## Cited prices (evidence)

**None — by design.** This thesis cites no prices. `market_data_stage: none` on every §3 row,
and `spec.md §5` states: *"Pair-trade candidates: none. This thesis produces no positions by
design."* The Q71 `observed_at` / `evidence/quotes/` mechanism is unused.

The ordering rule (Q35/Q36) expects a plan to end at dateable catalysts and sizing. This
thesis ends at **hand-off** instead — it publishes the citable curve and value-pool map that
004, 005, 006 and 011 convert. That deviation is registered in `plan.md`, not skipped.

## Reproducing this thesis from scratch

1. Restore `constitution.md` at sha256 `3d379aa4ef798839` (**v1.5.0** — includes DA-29/DA-30;
   DA-23…DA-30 is the full register) and confirm `constitution_ratified()` returns `True`.
2. Confirm `assumptions.yaml` version 2 (sha256 `0d0264e58a736568`).
3. Recompute the 13 skill hashes with `dispatch.skill_version_hash()` and compare against the
   table above. **Any mismatch means a skill changed under the thesis** — check whether the
   affected phase's findings still hold before reusing them.
4. Regenerate the task set:
   `python3 scripts/agentii_cmd.py tasks --thesis theses/003-launch-cost-curve-value-migration/thesis.md --spec theses/003-launch-cost-curve-value-migration/spec.md`
   → expect **45 distinct analyses**, expanding to ~90 mode-tasks. **Two synthesis tasks must
   be hand-added** (`agentii.tasks` emits none — 001's finding), one per primary artifact.
5. Re-run the plan audit — the authoritative check on the coverage invariant:
   `python3 tools/plan_audit.py theses/003-launch-cost-curve-value-migration/spec.md`
   → expect **4/4 invariants hold**, reporting `universe: 9 | matrix pairs: 45 | matrix
   tickers: 9 | subscriptions: 52`.

**Pair-level note (not an invariant failure — a finer cut).** I4 as specified is
**skill-level** ("every matrix *skill* is named in at least one `Subscribed` line"), and it
passes. At **pair** level, **7 of the 45 matrix pairs appear in no `Subscribed` line**:
`FLY × {peer-bench, ratio-analysis, recent-quarter, what-if}`, `PL × supply-chain`,
`SPCX × {ratio-analysis, what-if}`. Because `_pillars_of_skills` keys pillars by **skill
only** (001's documented mechanism), these seven inherit their pillar attribution from the
same skill's other assignments rather than having it assigned — so they are **not
unattributed**, but the attribution is inherited. The skills involved (`peer-bench`,
`ratio-analysis`, `recent-quarter`, `what-if`, `supply-chain`) are each named in at least one
`Subscribed` line, which is why I4 passes. Recorded so the distinction is not lost:
**the audit is a skill-level gate, so a pair-level gap can pass it silently.**

**What cannot be reproduced by retrieval.** The registry has **no industrial, aerospace or
defence domain** — every `applicable_sectors` value is a subset of `{med, tech, fin}` — so
**every sector-keyed query for this thesis fails by construction**. The store is not empty;
the index is. The reproducible unit is therefore the two keyword-reached references in
`brief.md` (the Baillie Gifford SpaceX case, ARK's Wright's Law framework) plus the
constitution's F1/F2/F5 physics and the cited SEC accessions — **not** a sector strategy id,
which does not exist for this domain.
