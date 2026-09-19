# Research Plan: 004 — Tier 0: SpaceX Anchor, SOTP across Space / Connectivity / AI

**Spec**: `spec.md` (clarify rounds 1–4, 2026-09-18/19) · **Constitution pin**: 1.5.0
**Budget**: `max_tasks: 40` · **Market data**: per-row (`late` × 2, `none` × 5 executed)
**Layer**: 4 of 4 — the valuation layer · **Binding constraint**: `CAPITAL`

> **Provenance.** This plan is authored by hand. **`agentii_cmd.py plan` does not exist** — the
> installed plugin exposes `specify, clarify, tasks, constitution, singleskill, converge,
> challenge, implement, status`, and no `plan` subcommand. The skill's documented invocation
> cannot run, so the four side artifacts and the registers below are written directly, matching
> 003's plan as the house template.

---

## Constitution Check (first evaluation — Q35)

| Constraint | Status | Evidence |
|---|---|---|
| **Scalar constraints** (position cap, stop-loss) | **N/A — PASS** | SPCX §1: *"No trade ideas: sizing is 011's."* §5: *"This thesis produces the anchor and no positions."* No sizing exists to violate a cap. |
| **Research scope — market cap** | **PASS** | Universe is one mega-cap (SPCX, ~$1.62T dated print). No cap floor is set by the constitution; §2's single-member rationale is *decomposability*, not size. |
| **Research scope — regions** | **PASS** | US-listed only. Read-through names (MSFT, GOOG, NVDA, VRT, IRDM) are all US-listed. |
| **Research scope — excluded sectors** | **PASS** | No excluded sector touched. SPCX is `industrial.aerospace_defense`; read-throughs are `tech.platform_internet`, `tech.semiconductors`, `industrial.machinery`, `tech.telecom_services`. |
| **P11 deal-securities** | **PASS with tagging** | **Cursor is now INSIDE the headline** (round 4 — pro-forma). IRDM and GSAT are P11 securities and their *multiples are inadmissible* despite live pricing. Every figure drawn from a P11 name carries *pre-merger basis*; the `risk` row exists to carry the tagging. |
| **P10 (orbital-compute underwriting)** | **PASS** | §1b P3: the 1M-satellite / 100 kW-per-tonne filing is *"a filed aspiration with no revenue line, inadmissible as a valuation input."* **A4 bars valuing terrestrial and orbital compute as one**, and SPCX's AI segment is ground-based. |
| **A4 / A1b** | **PASS** | A4 ceiling applied at P3. **A1b is falsified** and the SOTP must *show* value migrating out of launch, not assert it — §5 carries it as a constitution interaction. |
| **P4 (evidence grading)** | **PASS** | Every §0 inherited row carries a grade; the V-1 … V-7 queue names the source class that would convert each `CLAIMED`/`MODELED` input. **A-1 (the basis column) is open** and is the known gap — see the Deviation Register. |
| **Q33 version** | **PASS at 1.5.0** | Re-pinned from 1.4.0 at round 2. Brings **DA-29** (back-solved checks) and **DA-30** (two bases on one concept collapsed) into scope; **DA-30 governs §1c's component-identity rule**. A queued 1.5.0 → 1.6.0 is registered as an expiry trigger. |

> **⚠️ Version finding, carried forward — and it may now have changed.** 003's plan recorded that
> `constitution.md` **line 206 self-reports `1.4.0` while the document is at `1.5.0`** — a stale
> field that missed the bump, with the frontmatter transition, the `### 1.5.0` amendment entry and
> the closing note all agreeing on 1.5.0. **This plan does not re-verify line 206.** It is
> recorded so that if 004's artifacts ever disagree with a reader's check, the known cause is
> named. **The queued 1.6.0 (30 amendments: 3 PATCH, 27 MINOR, 0 MAJOR) marks all 42 artifacts
> stale**, and 004's `constitution_bump` expiry trigger is registered for it.

### Scalar-clearance note (why the second check is still run)

The template requires the Constitution Check **twice** — plan start (scalar + scope) and after
sizing (aggregate). 004 produces no positions, so the second check's aggregates are **sector
concentration, theme concentration and macro exposure**, not portfolio limits. Running it anyway
is deliberate: the Risk Framework's **40% theme cap binds before the 25% sub-sector cap in a
single-theme book**, and §5 names SPCX as *"the largest single-theme exposure available."* That
finding lives in the second check and would be lost if the check were skipped for having nothing
to size.

---

## Phases

Nine phases, mirroring spec §7 exactly. **Phase 0 and Phase 2 are new at rounds 3–4.** The
skills column names the `ticker × skill` rows that populate each; **3b's nine consumed rows
generate no tasks at all.**

| Phase | Content | Skills (ticker × skill) | Depends on |
|:---:|------|------|---|
| **0 — Consume 003** (new) | Read `003/_cross/launch-cost-curve.md` (1,013 lines) and `003/_cross/value-pool-map.md` (1,408 lines); index the nine consumed SPCX artifacts in spec §3b **by path**. **⚠️ 003 is COMPLETE — do not re-derive the curve or the map (F1). ⚠️ NO PRICE IS FETCHED HERE — see F13.** | *(none — a reading task)* | 003 COMPLETE; constitution 1.5.0 loaded |
| **1 — Separability (P1)** | Read the segment note; **confirm V-1 as a given — it is RESOLVED, do not re-litigate**; run `segments_sum_to_total` in-line; build the segment-attribution ledger. **⚠️ V-2's residual must be shown in-line (F3).** | `business-model`, `operational-kpi`, `recent-quarter` × SPCX *(all consumed — cited, not re-run)* | Phase 0 |
| **2 — Granularity** (new — P2, P3, P4) | **`revenue-decomp`**: the cut *inside* each segment. **⚠️ DERIVE the cuts from the filings — do not pre-declare a taxonomy. The spec's own round-3 five-tier list was wrong: aviation and maritime are not formable (F7).** Enterprise/government grew **2.4× faster than consumer** (F8). | `revenue-decomp` × SPCX | Phase 1; **`get_segment_data` is unusable — read pages (F6)** |
| **3 — Connectivity (P2)** | ARPU/subscriber/margin series on the **cohort cut from Phase 2**; all **DA-10** readings side by side; the price-erosion vs mix-shift test. **⚠️ `subscribers × ARPU × 3` does NOT reproduce consumer revenue (F8).** | `unit-economics`, `what-if` × SPCX *(consumed)* | Phase 2 |
| **4 — AI admissibility (P3)** | Test framings (a) comparable, (b) **invested capital ← the confirmed headline**, (c) optionality incl. zero; the MSFT/GOOG/NVDA framing set; apply the A4/P10 ceiling; **consume** 002's DA-11 restatement; the **market-implied limb** from `reverse-dcf`. | `reverse-dcf` × SPCX; `comps`, `peer-bench`, `secular-trends` × the framing set | Phase 3 |
| **5 — Space standalone (P4)** | Ex-R&D margin; the Starship/Falcon split labelled `MODELED`; **DA-08** internal-transfer limitation; **DA-01** A/A′/B/C restatement; **carry DA-06 as a stated non-comparability limitation — Space has NO transaction price (F9).** | `competitive` × SPCX, RKLB, FLY | Phase 2 |
| **6 — Capital (P5)** | Coverage ratio; funding structure and **Cursor/P11 dilution — now BLOCKING (F5)**; control and float; index-inclusion catalyst datability; **beta / cost of equity from live data**. | `risk` × SPCX; `ratio-analysis` × SPCX *(consumed)* | Phase 3 |
| **7 — SOTP (P1, P6)** | Scenario weights with in-line justification; three regimes; **the PRO-FORMA basis stated on the headline**; the discount decomposition **against both price bases, with the spread named as its own component (F4)**; `reverse-dcf` as cross-check; event-window studies. | `sotp-valuation`, `reverse-dcf` × SPCX | Phases 1–6 **and V-5** |
| **8 — Hand-off (P6)** | Publish `_cross/anchor-sotp.md` with boundaries naming **005, 006 and 009**; record what could not be valued. | **Two hand-added synthesis tasks** (`agentii.tasks` emits none — 001's finding) | Phase 7 |

**Task arithmetic — MEASURED, not estimated.**

```
matrix pairs 19 | generated pairs 19 | tasks 37 | cross-cutting 2 hand-emitted
```

**19 `(ticker, skill)` pairs across 7 executed rows** (`comps` alone holds 11 tickers:
SPCX, RKLB, FLY, GSAT, IRDM, ASTS, VSAT, MSFT, GOOG, NVDA, VRT). **§3b's nine consumed rows
contribute zero.** Distribution: `comps` 11 · `competitive` 9 · `sotp-valuation` 5 ·
`revenue-decomp` 5 · `risk` 3 · `growth-strategy` 3 · `reverse-dcf` 1.

> ### ✅ 39 FILED / 24 EFFECTIVE, AGAINST A BUDGET OF 40 — and the first measurement was 63
>
> **This measurement was not the first one, and the difference is the whole finding.**
> The initial run read **33 matrix pairs → 63 tasks**, because `tasks_md.py` parses matrix rows
> **positionally** with `^\| ([a-z-]+) \| [a-z-]+ \| (\w+) \| ([^|]+) \|` and has no concept of a
> "consumed" row — so §3b, written in 3a's shape to satisfy `plan_audit` I2, was read as **work to
> dispatch**. `secular-trends` alone contributed 12 tasks; all nine consumed skills dispatched.
>
> **The fix was a column shape**, not a rule: §3b now puts the 003 artifact path in the second
> cell, which cannot match `[a-z-]+`, so `MATRIX_ROW` skips it. The `Subscribed` lines were then
> trimmed to executed skills only, with consumed pairs moved to a **`Consumes (003)`** field that
> neither tool parses.
>
> | | pairs | tasks | fits 40? |
> |---|---:|---:|---|
> | First run (3b in 3a's shape) | 33 | **63** | ❌ +58% |
> | After the shape fix | 19 | **37** | ✅ |
>
> **The consume decision was worth 26 tasks — and it was invisible in prose.** Until the generator
> ran, "consume 003's nine" was a sentence; the toolchain was dispatching all nine anyway.
> **This is a third missing check, alongside I5 and I6:** neither `plan_audit` nor `tasks_md` knows
> what a consumed row is, and **the two tools' contracts conflict** — I2 wants subscribed pairs in
> the matrix, `tasks_md` wants matrix rows to be work. There is no shape satisfying both;
> 004's resolution is two shapes and a new field.

**Two synthesis tasks are mandatory** (spec §6): `_cross/anchor-sotp.md` and
`_cross/segment-attribution-ledger.md`. The generator will emit neither.

---

## ⚠️ Phase crosswalk — the declared nine and the generated six are DIFFERENT, and that is fine

**`tasks_md.py` files by FIRST PILLAR, not by the spec's phase list.** With only six pillars and
nine analytical phases, the two numbering systems cannot coincide. The plan therefore publishes
**both**, and states which is authoritative for what.

| Analytical phase (above, and spec §7) | Generated phase | Tasks | Work actually filed there |
|---|:---:|---:|---|
| **0 — Consume 003** | — | **none** | ⚠️ **Hand-emitted — see below.** Not `ticker × skill`, so the generator cannot emit it |
| 1 — Separability (P1) | — | **none** | **All consumed from 003.** P1's own matrix row (`sotp-valuation`) is filed at 7 — see the violation below |
| 2 — Granularity | **Phase 3** | 5 | `revenue-decomp`. **No pillar's first phase is 2**, so no Phase 2 section is generated |
| 3 — Connectivity (P2) | Phase 3 | *(shared)* | the same 5 tasks serve P2, P3 and P4 |
| 4 — AI admissibility (P3) | **Phase 4** | **12** | `reverse-dcf` ×1 + `comps` ×11 |
| 5 — Space standalone (P4) | **Phase 5** | 9 | `competitive` × RKLB, FLY, SPCX |
| 6 — Capital (P5) | **Phase 6** | 6 | `risk` ×3 + `growth-strategy` ×3 |
| 7 — SOTP (P1, P6) | **Phase 7** | 5 | `sotp-valuation` × 5 modes |
| 8 — Hand-off (P6) | **Phase 8 — Cross-cutting** | 2 | T900, T901 — **never `[P]`** |

**Authoritative for what:** the **analytical phase** governs *sequence and dependency* — it is
what the spec's §7 table and this plan's critical path mean. The **generated phase** governs
*filing and dispatch order*. Where they disagree, the analytical phase wins on ordering and the
generated phase wins on where a task sits.

### 🔴 A DEPENDENCY VIOLATION WAS FOUND AND FIXED HERE (2026-09-19)

**The first generated plan filed `sotp-valuation` at Phase 1.** `sotp-valuation` is bracketed
`[PIL-1/PIL-6]`, and first-pillar filing takes PIL-1 — so **the anchor computation was scheduled
before Connectivity, AI, Space, Capital, and before V-5**, the blocking Cursor dilution on the
critical path. **That is not load imbalance; it is a phase that reads outputs which do not yet
exist.**

**The cause is specific and worth naming.** P1's *only* subscribed matrix row is
`sotp-valuation`, because round 3's consume decision moved every other skill P1 names into §3b
as consumed. **So the consume decision — a correct change — created the violation.** Before it,
P1 had five subscriptions and the SOTP was one of five; after it, the SOTP was the only thing
P1 filed.

**The fix is in `phases.yaml` (`PIL-1: 7`), and the phase map is the ONLY lever**: `parse_phases`
reads `phases` and `names` only — **`depends` is documentation that changes nothing.**

> **P1's MDV is still delivered FIRST; only its INSTRUMENT moves.** The separability test — does
> each segment file a discrete operating result? — is answered from 003's artifacts during
> Phase 0 and needs no task. **What runs at Phase 7 is the valuation those separable segments
> receive**, which genuinely depends on Phases 2–6.

### ⚠️ Phase 0 has no task, and is therefore tracked HERE

The consume edge is real work — read the curve matrix (1,013 lines) and the value-pool map
(1,408 lines), index the nine consumed artifacts, and **capture and stamp the live quote**. It is
not `ticker × skill` shaped, so `tasks_md.py` cannot emit it, and **the platform has no concept of
a cross-cutting task** — the same gap that forces T900/T901 to be hand-emitted (001 documented it).

**Hand-emitted, and it must be dispatched first:**

| id | task | blocks |
|---|---|---|
| **T000** | **Read `003/_cross/launch-cost-curve.md` and `003/_cross/value-pool-map.md`; index the nine consumed SPCX artifacts of §3b by path.** — **⚠️ THIS TASK DOES NOT FETCH A PRICE. See F13.** | **every other phase** — Phases 2–7 all cite 003 |
| **T700** *(moved from T000)* | **Capture the live SPCX quote via `get_quote` and stamp `observed_at` + `retrieved_at`** — runs at **Phase 7**, adjacent to `sotp-valuation` | Phase 7 only |

> ### 🔴 F13 — THE PRICE CAPTURE WAS IN THE WRONG PHASE, AND THE PLATFORM WOULD HAVE REFUSED IT
>
> **Found by checking deployability, after two plan passes had already signed off the schedule.**
>
> `data-tools/refusal.py`:
> ```python
> def require_price_access(stage: str, tool: str):
>     """Q41/Q42: `late`-stage skills never touch `get_price_history`
>        (price is the final check, not the raw material)."""
>     if stage == "late" and tool == "get_price_history":
>         return refuse("PRICE_ACCESS_PREMATURE", ...)
> ```
> **`contracts/taxonomy.yaml` calls `PRICE_ACCESS_PREMATURE` *"plan-declared (Q41 late-mode
> early-quote refusal)"* — it is a rule about PLANS, and 004's plan broke it.**
>
> | | |
> |---|---|
> | **What I wrote** | Phase 0: *"capture the live quote and stamp it"*, and a rationale stating **"Phase 0 is where the price basis is set for every downstream figure"** |
> | **What the rule says** | **Price is the FINAL CHECK for fundamental work, never the raw material.** A `late`-stage skill gets `get_realtime_quote` **at the end only** |
> | **Why it matters** | 004 is the **first `late` thesis in this workspace** — 001, 002 and 003 are all `none`, so nothing here has ever exercised the rule |
>
> **The tool split is exact, and my earlier verification used the right half by luck:**
> `market_data.get_quote` ✅ allowed at the end · `market_data.get_price_history` ❌ **forbidden
> for `late` at any time.** ⚠️ **`live_snapshot.py` calls BOTH** (lines 99 and 100), so **it must
> not be pointed at a `late` thesis's early phases** — it would trip the refusal on its second call.
>
> **Fix:** T000 no longer fetches. **The capture moves to Phase 7 (T700)**, where `sotp-valuation`
> and `reverse-dcf` actually consume it. `entities.md`'s `quote_observation` schema is unchanged
> and still correct — **only its timing was wrong.**
>
> **Why two plan passes missed it:** both evaluated the schedule's *internal* consistency —
> ordering, loads, resume keys — and neither asked **whether the platform's own rules permit the
> work being scheduled.** The rule lives in `refusal.py`, not in any gate. **This is the fourth
> missing check: nothing validates a plan against the refusal vocabulary.**

### 🔴 39 filed, 24 effective — and the 16-task gap was a RESUME DEFECT, not scope

**Every read-through ticker in a matrix row generates a task, but read-throughs produce no
per-ticker artifact (§2).** So the generator over-counts, and worse — **the over-counted tasks
could never resume.** `dispatch.resume_verdict()` computes
`root = thesis_dir / "artifacts" / ticker` and globs `*_{skill}_{mode}.md`. Called with
`ticker="RKLB"` it looks in `artifacts/RKLB/`, **a directory §2 forbids.** It finds nothing,
returns **`"run"`**, and **re-dispatches forever.**

**§6 is amended at plan time: read-through rows file ONE artifact under SPCX**, and
`resume_verdict` must be called with `ticker="SPCX"` for them.

| Row | tickers | generated | effective artifacts | saved |
|---|---:|---:|---:|---:|
| `comps` | 11 | 11 | **1** (`SPCX × comps × default`) | −10 |
| `competitive` | 3 | 9 | **3** (SPCX × its 3 modes; RKLB and FLY fold in) | −6 |
| `risk` | 1 | 3 | 3 | — |
| `growth-strategy` | 1 | 3 | 3 | — |
| `sotp-valuation` | 1 | 5 | 5 | — |
| `reverse-dcf` | 1 | 1 | 1 | — |
| `revenue-decomp` | 1 | 5 | 5 | — |
| cross-cutting | — | 2 | 2 | — |
| **total filed** | | **39** | **23** | **−16** |
| hand-emitted **T000** | — | *(0 — generator cannot)* | **1** | — |
| **effective dispatches** | | | **24** | |

> **Arithmetic note, recorded because this plan has already published one wrong total.** The
> generator prints *"tasks 37"* and then separately *"cross-cutting tasks hand-emitted: 2"*. **37
> is the matrix-only count.** The filed total is **39**, and the first draft of this table used 37
> as though it were the total. **Corrected above.**

> **⚠️ Do not read this as scope reduction.** The 16 collapsed tasks are the *same work* — a
> comparability table is one artifact however many comparators it names. **What changed is that
> the work can now finish.** Before the §6 amendment those 16 dispatches were unresumable, so the
> budget was being spent re-running them rather than on the thesis.

### Two load findings, restated on the effective count

1. **Phase 4's 12 generated tasks are 2 effective** — `reverse-dcf` ×1 + `comps` ×1. It is no
   longer the heaviest phase; **the filing made it look heavy because `comps` names 11 tickers.**
   The ticker count stays: each comparator needs its own exclusion reason for P6, and narrowing
   the row would orphan VRT and fail invariant I1. **Only the artifact shape changes.**
2. **Phases 3 and 7 are 5 generated / 5 effective and both SPCX-only**, while Phases 5–6 carry 15
   generated / 9 effective across read-through names. **No rebalancing is needed** — the phases
   are dependency-ordered, not load-balanced, and the critical path runs 3 → 4 → 6 → 7
   regardless.

---

## Dependency graph and critical path

```
001 ──> 002 (COMPLETE) ──┐
                          ├──> 004 ──> 005, 006, 007, 008, 009 ──> 011
003 (COMPLETE) ──────────┘        └──> 006 and 009 named as permitted to price off it
```

**Two hard facts about this graph, both established at rounds 2–4:**

1. **Both upstream edges are now satisfied.** 002 is COMPLETE and 003 is COMPLETE. 004 is the
   first thesis in the programme whose dependencies are **done rather than pending** — which
   means Phase 0 and Phase 1 can begin immediately and there is no upstream wait to schedule
   around.
2. **The `003 → 004` edge was declared in `PROGRAM.md` §5 and in 003's own header from the start,
   and 004's spec did not carry it until round 2.** The lesson is not that the edge was missing —
   it is that **a declared edge can go unread for two theses' worth of work.** Phase 0 exists so it
   is a task rather than an assumption.

**Critical path: V-5 → Phase 6 → Phase 7.** The pro-forma headline (round 4) made the Cursor
dilution a prerequisite rather than a sensitivity. **V-5 is the only `blocking` item on the
critical path that is not already resolved** — V-1 is resolved, V-2 is mechanical, V-7 is resolved.

---

## Gates per phase

004 inherits 003's gate set. **All five are `fail`-level except `clarify_scan`, and two of
`check_contract.py`'s rules are `warn` by design.**

| Gate | What it enforces | Level |
|---|---|---|
| `check_contract.py <thesis>` | the contract's mechanical rules — `skill_pin_wellformed`, `evidence_grade_present`, `da_id_registered`, `unresolvable_class_required`, `deal_security_tagging` | **fail** |
| `check_sign_strip.py <thesis>` | **the DA-23 guard.** For every `2 × N` claim: *is `2N` present anywhere else?* If not, **the assertion is a back-solve.** | **fail** |
| `check_citations.py <thesis>` | the citation contract | **fail** |
| `plan_audit.py <spec>` | coverage invariants I1–I4 | **fail** |
| `clarify_scan.py <thesis>` | unstated falsifiers / undecidable pillars | candidate list |

**Two `warn`-only rules, and they are where 004's exposure lives.** `check_contract.py`'s
`basis_named` (DA-30) and `reconciliation_terms_located` (DA-29) are **semantic** — a regex cannot
decide whether a figure's basis was named. The file says so itself: *"A blanket regex would produce
exactly the failure mode this thesis spent Phase 3 documenting: **a check that closes cleanly while
testing nothing**."*

> ### 🔴 FOUR CHECKS THAT DO NOT EXIST — and every one was found by a defect that passed 4/4
>
> | Proposed | Would have caught | In this thesis |
> |---|---|---|
> | **I5 — market-data-stage consistency** | a spec declaring `none` where the skill registry declares `late` | **004 declared `none` on all 14 rows**; the registry says `sotp-valuation`, `ratio-analysis` and `reverse-dcf` are `late`. The primary instrument was pinned where no price could reach it, and `plan_audit` returned **4/4** throughout |
> | **I6 — formability** | a matrix row naming inputs the filer does not report | **spec §3a named *"aviation / maritime"* as Starlink tiers.** They appear twice in all nine SPCX artifacts, as prose, with no revenue line. `plan_audit` returned **4/4** throughout |
> | **I7 — consume / read-through awareness** | a table whose column shape makes a parser treat a *consumed* row as *work* | **`tasks_md` dispatched all nine consumed skills** (63 tasks vs 39), and `resume_verdict` would have re-run **16 read-through tasks forever** because it keys on `artifacts/{ticker}/` — a directory §2 forbids. `plan_audit` returned **4/4** throughout |
> | **I8 — refusal-vocabulary / platform-permission** | a plan scheduling work the platform refuses to perform | **Phase 0 captured the price**, which `PRICE_ACCESS_PREMATURE` refuses for a `late` thesis — *"price is the final check, never the raw material."* **Two plan passes signed off the schedule before this was caught** (F13) |
>
> **The four share one shape: the gates verify ARTIFACTS, and every defect lived in the space
> before one exists** — a registry stage, a declared tier, a table's column shape, a phase's
> position. **`plan_audit` returned 4/4 through all four.**
>
> **Both were proposed at round 3/4 and neither is built.** They are named here because a plan that
> lists its gates and omits the two its own history proves necessary is not complete. **The
> consistent pattern across four rounds: `plan_audit` checks coverage, not *existence of inputs* —
> so a value that looks like a specification and is actually an assumption passes every check.**

---

### Wiring, phase by phase

**Which gate binds which phase, and why *that* phase.** A phase that "completes" without its
binding gates has not been checked — and **two of 004's phases produce no artifact at all, so
the gates that bind them are different in kind.**

| Phase | Gates that bind it | Why *this* phase |
|:---:|---|---|
| **0 — Consume 003** | **none of the four** — no artifact is produced | T000's output is a **read-set**, and nothing validates it. **⚠️ Narrowed by F13: the price no longer lives here** — it moved to Phase 7, so Phase 0's unvalidated surface is smaller than the first draft assumed. **The residual gap stands: a read-set is not an artifact, so no gate sees it** |
| **1 — Separability (P1)** | **none of the four** — all work consumed from 003 | The separability test reads 003's artifacts. **The only 004-produced output is the ledger (`_cross`), which Phase 8's gates cover** |
| **2/3 — Granularity** | `check_sign_strip.py` ⚠️ **critical** · `check_contract.py` · `check_citations.py` | `revenue-decomp` **reports revenue and operating results by cohort** — every `2 × N` claim must have `2N` present elsewhere or it is a back-solve. **This is where a cohort margin can close cleanly while testing nothing** (DA-29) |
| **4 — AI admissibility** | `check_contract.py` ⚠️ **`deal_security_tagging` critical** · `check_citations.py` | `comps` prices **IRDM and GSAT — both P11 deal securities.** Their prices are **spreads**, and a live multiple on a spread is inadmissible. **The tagging rule is the only mechanical guard on that** |
| **5 — Space standalone** | `check_contract.py` ⚠️ **`da_id_registered` critical** · `check_sign_strip.py` | **DA-06 and DA-08 both live here** — the captive-integrated flag and the internal/customer launch split. Space's operating loss is **the DA-23 case at this issuer** |
| **6 — Capital (P5)** | `check_contract.py` ⚠️ **P11 / Cursor** · `check_citations.py` | **V-5 is blocking**, and the Cursor consideration is Class A stock. **This phase cannot close without the dilution**, and the tagging rule is what forces it into the open |
| **7 — SOTP** | **all four** · ⚠️ `check_sign_strip.py` **most critical** | The primary artifact. **The component identity runs on every segment table**, and §1c makes it mandatory. `check_contract.py`'s **`basis_named` is `warn`-only here — and this is where the 46.47pp exposure lives** (P2/P4 name their basis in-line precisely because the gate does not force it) |
| **8 — Hand-off** | **all four**, **plus the four that DO NOT EXIST** | `_cross/anchor-sotp.md` is what 005–009 cite. **I5, I6, I7 and I8 would all bind here — and none is built.** See below |

> **⚠️ THE WIRING EXPOSES THE REAL GAP, stated at phase granularity.** Phases **0 and 1 have no
> binding gate because they produce no artifact** — and Phase 0 is where the price basis is
> established for every downstream figure. **The two phases with the least mechanical checking
> are the two that set the thesis's most-cited inputs.** That is the same shape as the three
> missing checks: the gates cover artifacts, and **an input that is never written to an artifact
> is never gated at all.**

### Findings absorbed that CORRECT this plan's OWN artifacts

**These are defects in files this plan produced, not in the spec.** All corrected in this pass,
and recorded here rather than left inline, because **each was found by the pass that wrote it:**

| Where | The claim | What was wrong | Fix |
|---|---|---|---|
| **`phases.yaml`** | `PIL-1: 1` | **Filed the SOTP at Phase 1** — before Connectivity, AI, Space, Capital, and before V-5. A dependency violation, not load imbalance. **Caused by round 3's consume decision**, which left `sotp-valuation` as P1's only filed row | **`PIL-1: 7`.** Phase 1 no longer exists; the SOTP files at 7 |
| **`spec.md` §6** | `artifacts/SPCX/{date}_{skill}_{mode}.md` | **Silent collision.** 11 `comps` tickers all key on `(skill, mode)`, so `resume_verdict` would treat one artifact as satisfying all 11 — and called with `ticker="RKLB"` it looks in **a directory §2 forbids**, returning `"run"` forever | **Read-through rows file under SPCX**; 16 tasks collapse to 4 artifacts |
| **`plan.md`'s own task table** | *"37 → 21 effective"* | **Both totals wrong.** 37 is the **matrix-only** count; the filed total is 39. Effective is 23, or 24 with T000 | Corrected, **with the arithmetic note left in place** |
| **`thesis.md`** | *"Q42 NOW BINDS"* | **Overstated.** Q42's trigger is `early`; 004 is `late` on two rows and `early` on none. What is needed is a **quote** schema, not a bars schema | Corrected (spec A-15); `entities.md` defines `quote_observation` |
| **`spec.md` §3a** | *"aviation / maritime"* as Starlink tiers | **Not formable** — they appear twice in nine SPCX artifacts, as prose, with no revenue line. `plan_audit` returned **4/4** throughout | Rescoped to **derive cuts from the filings** (round 4) |
| **`plan.md` Phase 0** | *"capture the live quote and stamp it"*; *"Phase 0 is where the price basis is set for every downstream figure"* | **The platform forbids it.** `PRICE_ACCESS_PREMATURE` is *"plan-declared (Q41 late-mode early-quote refusal)"* — price is **the final check, never the raw material**, so a `late` thesis captures it **last** | **Moved to Phase 7 (T700)** — plan finding **F13**. **Two plan passes had already signed off the schedule before this was caught, because both asked whether the plan was internally consistent and neither asked whether the platform permits the work** |

> **Five defects, and four of them passed every check the workspace has.** The pattern is
> consistent across four clarify rounds and this plan pass: **the gates verify artifacts, and
> every defect so far has lived in the space before one exists** — a phase map, a filename
> convention, a schema claim, a column shape, a declared tier.

---

## Phase-by-phase evaluation against upstream results

Findings absorbed from 001, 002, 003 and clarify rounds 2–4 that **change the phases above**. As
in 003's plan, the numbering is local to this thesis.

### F1 — 003 is COMPLETE and nine of §3's rows were already run. *(Phase 0 — changes the work)*

003 produced **nine SPCX artifacts** across nine of 004's fourteen §3 rows, plus both `_cross`
deliverables. **The matrix was rebuilt at round 3 into 3a (7 executed) and 3b (9 consumed).**
Phase 0 exists to consume, and **Phase 1's three skills are now cited rather than run.** This is
the largest single reduction in the thesis's task load — and it was invisible in the spec until
round 2.

### F2 — A keyless live price feed exists, and `market_data_stage: none` was WRONG. *(Phase 0, all phases)*

`data-tools/market_data.py`, source **nasdaq**, `auth: "none"`. **Verified live 2026-09-19:
SPCX $152.71, close 2026-09-18, 3,759 ms.** `live_snapshot.py` already names SPCX.
**This was a declaration, not a fact**, and it contradicted the registry on two rows.

### F3 — The constitution's ~$1.62T anchor is ~13.1% stale. *(Phase 7)*

Struck against `$135.00` in 2026-06; the live quote is **$152.71**. **Both bases publish and the
spread between them is a named component of the discount decomposition** — it is not a
conglomerate discount and must not be silently attributed to one.

### F4 — V-7 is RESOLVED from XBRL, not from Note 3 prose. *(Phase 7)*

**Customer A: 17.89% H1 2026 · 18.30% Q2 2026 · 19.89% H1 2025 · 16.70% Q2 2025. Customer B:
12.20% H1 2026 · 19.50% Q2 2026.** Combined H1 concentration **30.09%**. **The DCF's backlog limb
goes from *unquantified* to *bounded*.** Retrieval route: `search_xbrl_facts` with
`ConcentrationRiskPercentage1` under `srt:MajorCustomersAxis`.

### F5 — V-5 is now `blocking`, because the headline is PRO-FORMA. *(Phase 6 → Phase 7 — critical path)*

Round 4 overrode the pre-close provisional. **Cursor is inside the headline, so its $60B all-stock
consideration and dilution are inputs to P1, not sensitivities — and V-5 previously recorded
dilution as *not determinable*.** The pre-close provisional existed precisely to avoid this
dependency; the owner chose pro-forma, and **the cost is stated rather than hidden.**

### F6 — `get_segment_data` is unusable. *(Phase 2 — changes the method)*

**003 recorded this first** (`003/plan.md` § F4, from 002 §7): the tool *"hard-errors at SPCX
(`column "k" does not exist`) and elsewhere reports a `total_revenue` summing served facts across
two years and two durations with no de-duplication — `segment_coverage_pct 116.2` masking a
302.1% overlap. 002's verdict: **'Treat its output as unusable.'**"*
**The working route is `search_xbrl_facts(…, view=detailed)`.**

### F7 — `revenue-decomp` must DERIVE its cuts, not declare them. *(Phase 2 — changes the work)*

Round 3 wrote five Starlink tiers into §3a. **SPCX files two.** `aviation` and `maritime` appear
twice in all nine SPCX artifacts, as qualitative prose, with **no revenue figure attached**.
**This is the round-1 F1-screens failure — a screen whose inputs do not exist — committed inside
004's own method, one round after 004 recorded that failure as a lesson.**

### F8 — The mix-shift evidence P2 needs is filed, and it is decisive. *(Phase 3)*

**Consumer `1,721 → 2,485 (+44.4%)`; Enterprise & Government `867 → 1,806 (+108.3%)`** — the
managed channel grew **2.4× faster**. Both *"segment, filed"*. **But `subscribers × ARPU × 3` does
NOT reproduce consumer revenue**, and managed-channel subscribers/ARPU are
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — so **price erosion cannot be fully separated from mix shift**,
and the pillar's claim must be stated as a bound.

### F9 — Space has NO transaction price. *(Phase 5 — bounds P4)*

003's `captive_integrated` flag: *"Comparing −56.34% against RKLB's Launch Services gross margin
is comparing a price to a non-price."* **Round 4's answer: carry it as a stated limitation per
P6's partition rule** — Space's value comes from **segment contribution**, and no external
multiple is borrowed.

### F10 — Customer A repeats the two-bases-opposite-signs pattern. *(Phase 7)*

H1 falls **19.89% → 17.89%** while Q2 rises **16.70% → 18.30%**. **A single quoted customer share
is a basis choice, not a fact** — the same DA-30 structure 003 found for SPCX's customer-launch
share. **Customer B has no 2025 comparative**, consistent with an entity acquired inside the
period, and carries the **DA-19** common-control flag.

### F11 — Pro-forma moves the control/float discount. *(Phase 7)*

The Cursor consideration is **Class A stock**, so the control/float component is no longer a
discount *on* the anchor — it is partly a discount **created by** the transaction the anchor now
includes. **Where the two cannot be separated, that is the finding.**

### F12 — The spec's tables are a machine contract. *(all phases)*

Round 3's re-verification found three parser-level defects in this spec's own §3: a bespoke column
shape that silently zeroed every consumed subscription; **bolded skill names that do not match the
registry** (`**sotp-valuation**` ≠ `sotp-valuation`, because the parser strips backticks but not
asterisks); and two rows subscribed by no pillar, which would have taken the `[P1]` fallback
bracket and mislabelled them as Minimum-Defensible-View work. **A layout chosen for readability
can silently zero out a subscription.**

---

### F13 — The platform REFUSES a `late` thesis that takes its price early. *(Phase 0 → Phase 7 — changes the schedule)*

**Found by checking deployability, after two plan passes had signed off the schedule.**
`data-tools/refusal.py` implements **`PRICE_ACCESS_PREMATURE`**, which `contracts/taxonomy.yaml`
calls *"**plan-declared** (Q41 late-mode early-quote refusal)"*:

```python
if stage == "late" and tool == "get_price_history":
    return refuse("PRICE_ACCESS_PREMATURE",
        "price is the FINAL CHECK for fundamental work, never the raw material")
```

**004's first draft put the price capture in Phase 0 and stated the rationale as *"Phase 0 is
where the price basis is set for every downstream figure"* — which is the forbidden pattern,
written out in the plan's own words.** 004 is the **first `late` thesis in this workspace**
(001–003 are all `none`), so nothing here had ever exercised the rule.

**Tool split, exact:** `market_data.get_quote` ✅ allowed at the end · `get_price_history` ❌
refused. ⚠️ **`live_snapshot.py` calls both**, so it must not run against a `late` thesis's early
phases. **Fix: the capture moves to Phase 7 (T700); the schema is unchanged.**

**The generalisable lesson — and it is the sharpest one this plan produced:** *both* plan passes
evaluated the schedule's **internal consistency** — ordering, loads, resume keys, phase maps —
and **neither asked whether the platform's own rules permit the work being scheduled.** The rule
lives in `refusal.py`, **not in any gate.**

#### 004 checked against the FULL refusal vocabulary — because F13 proved nobody does this

`contracts/taxonomy.yaml` defines a **closed enum of 13 `error_code` values.** Checking 004
against all of them, rather than against the one that happened to bite:

| Code | Implemented? | 004's position |
|---|---|---|
| **`PRICE_ACCESS_PREMATURE`** | ✅ `refusal.py::require_price_access` | 🔴 **VIOLATED in draft, FIXED (F13)** — price moved to Phase 7 |
| **`DATA_STALE`** | ✅ `refusal.py::require_observed_at` — *"a quote lacking `observed_at` may not be used in any pinned artifact"* (Q71) | ✅ **satisfied** — `entities.md`'s `quote_observation` makes `observed_at` a required field, kept distinct from `retrieved_at` |
| **`INSUFFICIENT_HISTORY`** | ✅ `market_data.py` — *"tool-side refusal"* (Q42); fires when `< 20 bars` | ✅ **not reachable** — it gates `get_price_history`, which **004 never calls.** *Reinforces the F13 fix: the only price route open to a `late` thesis is also the only one that cannot trip this* |
| `ASSUMPTION_UNPINNED` | ⚠️ **in the enum; no implementation located** | ⚠️ **carries a known exposure** — §1c: *"`assumptions.yaml` carries no scenario-weight field, so a weight not justified in-line is silent drift."* **And beta is now a second such input** (spec A-9). If a check is ever built, **these two are where 004 fails it** |
| `LOOKAHEAD_VIOLATION` | ⚠️ **in the enum; no implementation located** | ⚠️ **a forward-looking SOTP is exactly what this code names.** Carried as an open exposure, not a clearance |
| `UNFRAMED_REFERENCE` · `CONSTITUTION_BREACH` · `PIN_MISMATCH` · `DEP_MISSING` · `CALC_UNVALIDATED` · `VALUE_IMPLAUSIBLE` · `SCHEMA_MISMATCH` | ⚠️ enum only | 004 addresses each in §5 / the five pins / the V-queue, **but no implemented check confirms it** |

> **The honest result: 13 codes, 3 with located implementations, 1 of those violated by this
> plan's first draft, and 10 that are vocabulary.** `PRICE_ACCESS_PREMATURE` was caught only
> because this pass went looking after reading `dispatch.py`'s retry table — **not because
> anything tests for it.** That is the argument for **I8** stated at its strongest: **the refusal
> vocabulary is plan-declared policing with no plan-level checker.**

---

## Side artifacts (Q36 — produced by `agentii.plan`)

| Artifact | Status | What it carries |
|---|---|---|
| `brief.md` | ✅ **written** | The retrieval record (**sector-keyed queries return zero by construction**; `search_by_analogue` is a dead end), two real `<ref:*>` blocks, **a `method_selection:` verdict per framework**, and **the F1 screens feasibility box** — its thresholds are `UNRESOLVABLE-FROM-PLATFORM` with a named resolver, its *method* survives |
| `entities.md` | ✅ **written** | `entity_claims` schema, the entity/metric map, the **DA register** (DA-06/08/10/11/19/21/23/29/30), the two disposition classes, and a **tool register**. **Emits the `quote_observation` schema — see the Q42 note below** |
| `reproduce.md` | ✅ **written** | **7 executed skills with real computed per-skill hashes** + the five pins + `as_of` + the reproduction recipe. **Two hashes reproduce 003's validated values exactly** (`competitive 826995c722a4`, `risk 953fc5d396e7`) |
| `contracts/artifact-frontmatter.yaml` | ✅ **present** | Output frontmatter schema |
| `contracts/anchor-sotp.yaml` | ✅ **written** | **Primary artifact contract** — three regimes, the **partition** boundary shape with its required clauses, scenario weights, the **pro-forma** headline basis, and the **four-component** discount decomposition |
| `contracts/segment-attribution-ledger.yaml` | ✅ **written** | **Secondary artifact contract** — the V-1 … V-7 queue with dispositions, the **blocking set**, and the disposition classes stated distinctly |
| `thesis.md` | ⚠️ **partial** | Pins, budget, expiry triggers, `depends_on`, `market_data_stage: per_row` all populated. **`claim` and `pillars` are still `[TBD]`/`[]`** — spec A-7, open, carried in the Deviation Register with an expiry |
| `phases.yaml` | ✅ **written** | The pillar → phase map `tasks_md.py` requires. ⚠️ **Its schema comment must NOT be written as a `phases:` key** — `parse_phases` uses a bare `re.search`, so the platform's own `PHASES_FILE` header, copied verbatim, is parsed *as the declaration* and the real one is never read |
| `tasks.md` | ✅ **generated** | 19 pairs → **37 tasks** + 2 hand-emitted cross-cutting |

> ### ⚠️ Q42 — `entities.md` and the bars schema, unresolved
>
> The skill's rule: **`market_data_stage: early` theses MUST define the bars schema (Q42) —
> without it, `implement` refuses.** **004 is `late` on two rows, not `early` on any.** The
> requirement is therefore **not literally triggered**, and round 3's note in `thesis.md` claiming
> *"Q42 NOW BINDS"* **overstates it.**
>
> **What is actually true:** 004 needs a **quote/observation schema** — ticker, price, basis,
> `observed_at`, `retrieved_at`, source, and the refusal envelope — for its two `late` rows. That
> is a *different* schema from `early`'s OHLCV bars (a `sotp-valuation` run needs a price at a
> timestamp, not a 250-day series). **The registry has no `late` example in this workspace to
> copy** — 001, 002 and 003 are all `none` — **so 004 is the first and must define it.**
> `entities.md` will carry it; **the `thesis.md` note is corrected separately (spec A-15).**

---

## What upstream supplies — consume, do not re-derive

### From 003 (added at round 2 — the edge PROGRAM always declared)

| Input | Artifact | Consumed as | 004 may **not** |
|---|---|---|---|
| **The curve matrix** — vehicle × architecture × DA-01 basis, per-architecture F5 floor | `003/_cross/launch-cost-curve.md` | P4's **Cost** limb and the A/A′/B/C restatement | Re-derive any $/kg base, or apply a floor named for another architecture |
| **The value-pool map** — revenue growth and operating margin by segment, 9 names | `003/_cross/value-pool-map.md` | The **prior** the three regimes must be consistent with | Re-map the pool, or re-run the cross-issuer margin test |
| **The demonstrated-versus-claimed split** | curve matrix, P3 | The admissibility test for every $/kg entering the SOTP | Treat a `CLAIMED` curve as factual |
| **The nine SPCX artifacts** (§3b) | `003/artifacts/SPCX/*` | Business model, unit economics, operational KPI, recent quarter, ratio analysis, peer bench, sector overview, secular trends, what-if | Re-run any of them |

### From 001

The `spec.md` §0 table — throughput, cost, segment structure, the entity discontinuity, the DA-01
bases, the capital structure. **All `DEMONSTRATED` at 001's grade; A-1's basis column is open.**

### From 002

The **validated** input set, and its programme-level result: **a grade does not carry a basis.**
SPCX `operating_margin` reproduces exactly on two bases differing by **46.47pp** (filed
**−16.68%** vs platform-served **+29.79%**). **This is why P2 and P4's falsifiers now name their
basis in-line.** 002 also supplies the **DA-11 PUE restatement** (consumed by P3, never re-derived).

---

## Constitution Check (second evaluation — after sizing, Q35)

Sizing does not occur here, so the aggregates evaluated are the three §5 names.

| Constraint | Status | Evidence |
|---|---|---|
| **Sector concentration** | **PASS with a stated bound** | Single-member universe; **SPCX is the largest single-theme exposure available.** The binding mitigation is not a cap but the **three-segment decomposition** — three businesses, three regimes, one issuer. |
| **Theme concentration** | **PASS — and this is where the Risk Framework actually binds** | The **40% theme cap binds before the 25% sub-sector cap** in a single-theme book. **This thesis takes no position**, so the cap binds 011, not 004 — recorded here because §5 names it and the second check is where it belongs. |
| **Macro exposure** | **PASS, with §5's finding carried** | §5 rates macro sensitivity **high**: SPCX is *"the longest-duration asset in the universe and the regime is hostile to duration"* — 10Y 4.80%, 30Y 5.26%, both three-year highs, hike risk priced. **The constitution's re-rate triggers (10Y > 5.25%, or a Fed pivot) are the scenario-weight inputs for P5's capital claim**, and beta now joins them as a measured input rather than an assumed one. |
| **Aggregate position cap** | **N/A** | No positions. |
| **A1b** | **TESTED, not assumed** | A1b is falsified; §5 requires the SOTP to *show* the migration rather than assert it. |

---

## Deviation Register (Q35)

> ✅ **APPROVED 2026-09-19 — all three rows below, at the `agentii.implement` soft gate.**
> Recorded as one approval because the three were reviewed together immediately before the
> first dispatch, and one of them (row 2) had its own expiry set to exactly that moment.
> **With an Approver recorded, the plan is formally complete** — per the rule at the foot of
> the template, an accepted violation without one does not count.

| Constraint | Why Accepted | Safer Alternative Rejected Because | Approver | Expiry |
|---|---|---|---|---|
| **§0 carries no `Basis` column (spec A-1)** | Round 2's answer was to add one; **the values are research and a guessed basis reproduces the exact defect the answer removes.** So the column is specified and unpopulated. | **Populating it from 001's grades alone** would name a basis without checking it — the 46.47pp failure at SPCX `operating_margin`. **Waiting for 002's six SPCX artifacts to be read** is what Phase 1 does anyway. | ✅ **APPROVED — owner, 2026-09-19, at the `implement` soft gate** | **Phase 1 completion.** Populating §0's basis column is an explicit Phase 1 output; the register row expires when it lands. |
| **`thesis.md` `claim` and `pillars` are `[TBD]`/`[]` (spec A-7)** | The claim must be populated **from §1b**, and §1b changed materially at rounds 2–4 (the layering, the pro-forma headline, the confirmed framings). **Writing it earlier would have produced a claim the spec no longer supports.** | **Filling it at round 1** would have recorded the ecosystem-keystone claim that round 2 then moved to 011. **Deferring to `implement`** would let artifacts be written against a stub `thesis.md`, which is exactly the defect 003's plan repaired at its own gate. | ✅ **APPROVED — owner, 2026-09-19, at the `implement` soft gate** | **Before the first `implement` dispatch.** A stub `thesis.md` fails `pins_match_thesis` in `artifact-frontmatter.yaml` — the same failure 003 recorded. |
| ~~Budget `max_tasks: 40` against an unmeasured task count~~ ✅ **DOES NOT ARISE — measured at 37, inside budget** | The row was raised at plan time because the count was unmeasured and 003's ~90 estimate measured **109** (a 36% overrun). **Measured: 19 pairs → 37 tasks against a budget of 40.** **No deviation, no sign-off, no budget change.** | *(moot)* — the three rejected alternatives are recorded for the next thesis that plans a consume-from-upstream row: **estimating early** would have repeated 003's error; **inflating pre-emptively** is what 001 did four times (40 → 70 → 85 → 130 → 170); and **"drop the Light rows first"** — the spec's own rule — would have cut `comps`, a Light row that now carries the **AI framing set** (MSFT, GOOG, NVDA, VRT) and whose removal orphans four read-through names and fails `plan_audit` I1. | **N/A — closed by measurement 2026-09-19** | **Fired and resolved.** ⚠️ **But note the first measurement was 63, not 37** — the 26-task gap was a *parser* artifact, not scope. **A budget deviation can be manufactured by a table's column shape.** Had this row been granted without checking, 004 would have raised `max_tasks` to accommodate work that should never have been dispatched. |
| **`get_segment_data` is unusable but remains the documented route in the platform** (F6) | 003 recorded the verdict; **004 routes around it to `search_xbrl_facts(view=detailed)`**, which round 4 verified live. | **Fixing the tool** is a platform change outside this thesis. **Reading around it silently** would have hidden that the obvious route is broken. | ✅ **APPROVED — owner, 2026-09-19, at the `implement` soft gate** | **Does not expire** — a platform-tooling limitation, not a temporary accommodation. Carried so 008 and 009, the likely next callers, find it. |

> **All four rows are pending human sign-off.** Per the rule at the foot of the template, an
> accepted violation without an **Approver** means **the plan is not complete**. These are
> recorded, not granted.

---

## Spec corrections applied in this pass

| # | Location | Correction |
|---|---|---|
| 1 | §1b P2, §1b P4 | `wrong_if` `source=` restated as `…_at_filed_segment_basis`, each with an in-line definition (spec **A-2**, PATCH) |
| 2 | §1c instrument 1, §5, §7 Phase 7 | **Pro-forma basis propagated** — it had reached only §1b P1 and V-5 (spec **A-11**, PATCH) |
| 3 | §3a box | **`get_segment_data` breakage re-credited to 003's F4** — round 4 found it independently and presented it as new (spec **A-12**, PATCH) |

**Spec corrections *not* applied, recorded as debt:** A-1 (basis column), A-4 (§5's 006/009
boundary sentence), A-7 (`thesis.md` claim/pillars), A-9 (beta has no `assumptions.yaml` field),
A-13, A-14, **A-15 (the Q42 overstatement in `thesis.md`)**, FC-1, FC-2.

**Verification at plan time:** `plan_audit.py` **4/4** · `clarify_scan.py` **0 candidates**.
