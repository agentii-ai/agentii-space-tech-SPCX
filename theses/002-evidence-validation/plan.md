# Research Plan: 002 — Evidence Validation & Model Hardening

**Thesis**: `theses/002-evidence-validation/` · **Constitution pin**: 1.4.0 · **as_of**: 2026-09-18
**Status**: Active · **Duration**: 7 phases, ~7 weeks
**Task budget**: **112 emitted / 87 dispatched / 120 budgeted**

> **Ordering-rule adaptation (Q35/Q36).** The template prescribes *fundamentals first,
> trade ideas last*. This thesis has **no trade-ideas phase**, by design: `spec.md`
> states it produces no trade ideas and sizes no positions. Phases terminate at hand-off.
> The same adaptation 001 registered, for the same reason.

---

## §Evaluation — what the first draft of this plan got wrong

**This section exists because the first draft was measured and found defective in four
ways.** It is retained rather than quietly corrected, because two of the four defects are
*structural properties of the tooling* that every future thesis in this workspace will hit.

| # | Defect in the first draft | Measured | Fix |
|---|---|---|---|
| **E1** | **The phase table was wrong by up to 8×.** It reported Phase 4 as **3 tasks**. True load is **23**. | Phase 4: 3 → **23**. And **PIL-6 showed *zero* tasks in every phase** | Recompute load **per pillar*, not per generator bucket (below) |
| **E2** | **25 tasks (22% of 132) were mis-scoped modes** serving no pillar of this thesis | `earnings-vs-consensus` ×17; two `secular-trends` trend modes ×8 | **Declared N/A** with reasons — see §Declared-N/A Register |
| **E3** | **`secular-trends` at Deep was the wrong instrument.** Deep expands to **8 modes**; five of them (EV-trend, quantum/renewable, strategic-position, capacity-and-readiness, market-perception) **cannot source a physics constant**, which is exactly what P2 asks for | secular-trends: 32 → **12** tasks | Depth reduced Deep → Standard in `spec.md` §3 |
| **E4** | **My own fix introduced a regression.** Splitting the secular-trends row into one Deep row + one Standard row caused the generator to **silently drop one** — leaving **BWXT, the name carrying P2's nuclear case, with zero secular-trends tasks** | 0 tasks for BWXT × secular-trends | Collapsed to a single row; caught by counting, not by reading |

> **E4 is the important one.** It is the same failure class as 001's I2 finding: *a matrix
> and a subscription list can disagree without producing an error — the work simply never
> happens.* It was caught only because the task count was **verified per `(ticker, skill)`
> pair** rather than accepted in aggregate. **Any edit to the Skill Deployment Matrix must
> re-verify per-pair counts.** Recorded as a standing rule for this workspace.

### The root cause of E1

The generator assigns a multi-pillar task to its **first** pillar's phase. Three pillars —
**P4, P6 and P7** — are carried entirely by pairs whose first pillar is something else:

| Pillar | Generator bucket | **True load** | Why it was hidden |
|---|---:|---:|---|
| **PIL-6** entity-boundary | **0** | **11** | Its three subscribed pairs all resolve `[PIL-1, …]` first |
| **PIL-4** nameplate (DA-11) | 3 | **12** | Same — `SPCX × operational-kpi` is `[PIL-1/PIL-4/PIL-6]` |
| **PIL-7** reachability | 13 | **18** | Partly hidden |
| PIL-1 / PIL-2 / PIL-3 / PIL-5 | 21 / 15 / 56 / 4 | same | Unaffected — they are first in their brackets |

**The consequence is not cosmetic.** PIL-6 carries the **entity-boundary classification**
— the finding that *"AI is 32.8% of SPCX revenue"* is contaminated by the xAI merger and
may not be quoted as organic migration. That finding is **load-bearing for 011's main
line**. A plan that shows PIL-6 with zero tasks would let a dispatcher skip it.

---

## Constitution Check — first evaluation (plan start: scalar + scope)

| Constraint | Status | Evidence |
|---|---|---|
| `POS_SINGLE` — single position ≤ 6% | **N/A** | No positions are sized or recommended. Output is a validated input set. |
| `POS_BINARY` — binary catalyst ≤ 2% | **N/A** | Same. |
| `STOP_THESIS` — stop ≤ 30% | **N/A** | Same. No entries, no stops. |
| Research scope — market cap ≥ $250M | **PASS** | All 17 universe issuers listed and audited `READY`. |
| Research scope — regions (US-listed primary or ADR) | **PASS** | All 17 US-listed. No ADRs. |
| Research scope — excluded sectors | **PASS** | No China/Russia-domiciled entity, no digital-asset vehicle, no SPAC shell. |
| Research scope — liquidity floor (ADV ≥ $5M) | **N/A at this stage** | Applies to positions, not research. Flagged for 011. |
| `Max Concurrent Positions` = 12 | **N/A** | No positions. |

**Result: no failures.**

### 🔒 Hard precondition — do not dispatch Phase 1 until this is resolved

**001 is pinned at 1.2.0 and is marked `stale` by the 1.4.0 bump. Its re-examination is
bounded but UNDISCHARGED.** This thesis validates 001's figures; if 001's artifacts move
under it, 002's own baseline moves mid-flight.

| State | Action |
|---|---|
| Re-examination **discharged** (001 re-pinned to 1.4.0) | Proceed. Validate against the re-pinned artifacts. |
| Re-examination **explicitly deferred** by the owner | Proceed, but **stamp every 002 artifact with `upstream_stale: 001@1.2.0`** so the provenance is unambiguous. |
| **Neither** | **Do not dispatch.** |

The first draft recorded this as *risk 5* — a soft concern. **It is a gate**, and the
difference matters: a risk is something to watch, a gate is something that blocks.

---

## §Phase evaluation — phase by phase, and what changed

**Each phase was assessed against four questions:** is the work *correctly scoped*, is the
instrument *adequate*, is the *deliverable named*, and does the *acceptance test exist*?
Six of seven phases failed at least one on the first pass. The optimizations are below
each finding.

### Phase 1 — Denominators (P1) · 21 filed · 21 true

| Finding | Disposition |
|---|---|
| **The skill list was over-broad.** It named "unit-economics; operational-kpi" without tickers, which imported **VRT** (P2's terrestrial comparator) and **UTHR** (P7's) into a phase they do not belong to | **Trimmed** to `unit-economics` on RKLB/SPCX/FLY and `operational-kpi` on SPCX/RKLB/YSS |
| **A spec/plan mismatch on the denominator set.** The plan said *"Electron, Falcon 9, Starship, Alpha"*; the spec's P1 `wrong_if` tests **three** — Electron, Falcon 9, Starship. **Alpha is not in the falsifier** | **Resolved toward the spec**: Alpha's payload is collected as a *supporting* datum for FLY's economics, **not** as a P1 denominator. The plan now says so rather than silently widening the test |
| **21 tasks ≈ 5 distinct analyses.** The 5 `unit-economics` modes are *sections of one analysis* — 001's own finding — so the count overstates the work ~4× | **Recorded**, not trimmed: the modes are a decomposition, and `dispatch` runs them as one artifact |

### Phase 2 — Physics inputs (P2) · 15 filed · 15 true

| Finding | Disposition |
|---|---|
| **⚠️ THE INSTRUMENT IS INADEQUATE, AND THIS IS THE PHASE THAT MATTERS MOST.** P2 asks to *source a radiator areal density and a heat-pump COP*. **No skill in the registry is a literature or hardware review** — the nearest is `secular-trends`, which reads **securities filings**. After the 8 declared-N/A trend modes, **Phase 2 has ~7 real tasks for the constitution's *named binding constraint for orbital compute*** | **Recorded as the plan's principal open risk.** The phase must be prepared to conclude `UNRESOLVABLE-FROM-PUBLIC-SOURCES` for one or both constants — which is a legitimate output and a *stronger* finding than a modelled number |
| **No deliverable was named** | **Named**: `_cross/f2-constant-sourcing.md`, carrying each constant with its citation, its uncertainty interval, and the **re-derived radiator mass per MW both with and without the COP penalty** |
| **No acceptance test for the COP loop** | **Added**: if the sourced band exceeds **±50%**, F2 **downgrades to a qualitative bound**, and **003 and 009 must be notified** — 003 frames the compute narrative on F2 and 009 sells into it |

### Phase 3 — Defect census (P3) · 56 filed · 56 true

> ### 🔴 INSTRUMENT RULE — measured before dispatch, and it prevents ~250 false defects
>
> Phase 1's `RKLB × operational-kpi` task reported a `validate_calculation` anomaly. Running
> the tool directly on RKLB's Q2 2026 10-Q (`0001819994-26-000062`) shows the problem is
> **much broader than that task could see**:
>
> | | |
> |---|---|
> | Raw output | **8 pass · 1 warn · 15 fail** on an ordinary 10-Q |
> | Of the 15 FAILs | **1** is sign-only (`|computed| == |reported|`, sign opposite) → a genuine DA-23 hit |
> | | **14** are **magnitude** mismatches → incomplete calculation arcs, or 3-month/6-month period mixing |
> | **Consequence** | **the `status` column is 14/15 = 93% false-positive as a defect detector** |
>
> **A Phase 3 run that treated `fail` as "defect found" would have manufactured ~15 false
> defects per issuer across 17 names — roughly 250 spurious findings**, and then registered
> them in the constitution's Data-Integrity Register.
>
> **THE RULE — do not read the `status` column:**
> 1. Compare the **`computed`** value against the **`reported`** value for the concept of interest.
> 2. **A DA-23 hit is `|computed| == |reported|` AND `sign(computed) != sign(reported)`** — magnitude identical, sign opposite. That is the sign strip, and nothing else is.
> 3. **A magnitude difference is NOT a DA-23 hit.** It is an incomplete arc or a period-mixing artefact, and is recorded as an **instrument limitation** — never as an issuer defect.
>
> **AND THE INVERSE — `pass` is not evidence of a correct sign either.** FLY's task found
> `validate_calculation` returning **`pass`** on the sign-stripped cash parent
> (`CashCashEquivalents…PeriodIncreaseDecrease…`: computed **333,149,000** = reported
> **333,149,000**) — because the children share the inversion, so the parent *computes* the
> flipped value and matches it. **A `pass` where every child is flipped is a passed check
> that the sign is wrong.**
>
> So the `status` column fails in **both** directions: **93% false-positive on `fail`, and
> `pass` does not certify a sign.** The only admissible use is the raw
> `computed`-vs-`reported` **pair**, read through the component identity.
>
> The instrument is still usable for P3 — but as a **source of the `computed` column**, not
> as a verdict. The component identity remains the discriminator (P4 / the register).
>
> **Second instrument limitation — `pass` propagates an inverted subtree.** Where an
> inversion is shared between parent and children, the check is self-consistent and
> therefore silent. **A third detector is needed: compare the sign against the *prose* or
> against an independently-derived component, never against the extract's own arithmetic.**

| Finding | Disposition |
|---|---|
| **56 tasks ≈ 17 mechanical calls.** The register application is `validate_calculation` per issuer; `recent-quarter`'s three modes are sections of one artifact | **Recorded**: the real unit is **17 calls + 3 candidate resolutions**, and at `max_concurrent_subagents: 5` that is **~4 rounds, not 12** |
| **The instrument over-reports by 93%** (above) | **Rule added to every Phase 3 brief** |
| **The rail period-alignment guard.** RKLB's 2025 `OperatingIncomeLoss` row returns computed **−186,242,000** against reported **+59,639,000** — a figure matching no filed period, because the arc mixes the 3-month and 6-month columns | **Recorded as an instrument limitation.** Phase 3 must name the period it is testing and confirm the columns align before reading any row |
| **The coverage hole was missing.** `OperatingIncomeLoss` is **absent or segment-only at MRK, BMY and WWD** — no detector can run. The spec requires these be recorded `UNRESOLVABLE-FROM-PLATFORM`, but **the plan's Phase 3 did not list it** | **Added as an explicit Phase 3 deliverable** — the failure mode is an artifact treating absence as a *clean read* |
| **The three open candidates had no per-candidate checklist.** "BA 2025 Q3, LUNR, VOYG — either explained or registered as a further defect" is prose, not a test | **Added**: each candidate resolves to exactly one of `{explained with citation}` / `{promoted to a registered defect}`. **VOYG is flagged as the tricky one** — it fails the *gross-profit bound*, not the sign test, so a sign-only check passes it and is wrong |

### Phase 4 — SPCX validation (P4 + P6) · **3 filed · 23 true**

| Finding | Disposition |
|---|---|
| **This is the 8× phase.** It files 3 tasks and carries 23, because the entity-boundary pillar is fed entirely by SPCX pairs whose first pillar is PIL-1 | **`tasks.md` now shows both columns** and instructs scheduling off **True load**. A dispatcher reading "3" would have under-resourced the phase that produces 011's load-bearing finding |
| **No deliverable was named** | **Named**: `_cross/spcx-nameplate-and-boundary.md` — the PUE restatement **and** a per-series classification table (Space: clean · Connectivity: clean · AI: **contaminated**) |
| **The boundary table is an 011 dependency and was not marked as one** | **Added**: 011's P1 cannot finalise its migration evidence until this lands. It is a **soft gate on 011**, not just a 002 output |

### Phase 5 — Reachability (P7) · 13 filed · 18 true

| Finding | Disposition |
|---|---|
| **The work was OVERSTATED.** The plan said *"classify all six 001 falsifiers"* — but **001 already classified them** (3 HOLDS, 0 FALSIFIED, 3 UNRESOLVABLE, with causes named) | **Corrected**: Phase 5 does not classify from scratch. It (a) assigns each of the three UNRESOLVABLE verdicts to a **v1.3.0 disposition class** — the split that did not exist when 001 ran — and (b) proposes **evaluable proxy tests** |
| **The plan implied Phase 5 invents the proxies** | **Corrected**: **006 already supplies PIL-6's proxy** (an issuer-disclosure bridge, since FCC IBFS is platform-unreachable). Phase 5 **adopts** it and records it, rather than generating a competing one |

### Phase 6 — Ledger (P5) · 4 filed · 4 true

| Finding | Disposition |
|---|---|
| **This is the thesis's PRIMARY artifact and it had no schema.** "Assemble the validation ledger" does not say what a row is | **Schema named**: `{figure, source_artifact, original_grade, validated_grade, band, citation, pillar, disposition}` — **the `citation` column is mandatory per §1d** |
| **The conversion share had no stated denominator** | **Stated**: the share is `rows whose grade moved to DEMONSTRATED ÷ total ledger rows`. **The 50% threshold is itself unconfirmed** (spec Q-5) — the plan now says the ledger is published **with the count**, so the threshold can be judged against a real denominator rather than pre-committed |

### Phase 7 — Hand-off · no tasks (cross-cutting)

Unchanged. It carries the Output Contract's `_cross/validation-ledger.md` forward to
003–006 and records what could not be validated.

**Net effect of the evaluation:** no task count changed — the work was already emitted.
What changed is that **six phases now name a deliverable, four have an acceptance test
where none existed, one over-count and one under-count were corrected, and the phase that
matters most (P2) is flagged as instrument-inadequate rather than assumed adequate.**

**Phase 3 is 50% of emitted tasks (56 of 112) but ~4 dispatch rounds at width 5, not 12.**
**Phase 4 files 3 and carries 23** — the largest gap in the plan. **Phase 2 is the smallest
real phase and the highest-stakes.**

## Task inventory

**112 tasks emitted** from 40 `(ticker, skill)` pairs (expansion **2.80×**), of which
**25 are declared N/A** — leaving **87 to dispatch**. Coverage: **17 / 17 universe tickers.**

**`tasks.md` is written** — 170 lines, 6 phase sections, every bracket re-attributed, every
declared-N/A marked in-line. Generate it with:

```bash
python3 tools/tasks_md.py --thesis theses/002-evidence-validation \
  --declared-na "recent-quarter:earnings-vs-consensus,\
secular-trends:deep-dive-ai-trend,secular-trends:deep-dive-data-value-trend"
```

**Use `tools/tasks_md.py`, not `agentii_cmd.py tasks` directly.** The platform generator
emits ~60% wrong brackets, no phases, and no coverage check. The local tool re-attributes
from the `(ticker, skill)` map, applies `phases.yaml`, marks declared-N/A tasks, and
**fails loudly if any matrix pair produces zero tasks** — the silent-work-loss class that
caught a real regression during this plan's evaluation.

`tasks.md` reports **both** `Filed here` and `True load` per phase, because the first-pillar
filing heuristic makes them diverge — **Phase 4 files 3 and carries 23.** Schedule off
**True load**.

### ⚠️ Two generator defects that survive this plan

| # | Defect | Measured | Disposition |
|---|---|---|---|
| **1** | **Pillar brackets keyed by SKILL, not `(ticker, skill)`** — every task for a skill inherits the *union* of all pillars subscribing it anywhere. `RKLB × unit-economics` gets `[PIL-1/PIL-2/PIL-4/PIL-7]` instead of `[PIL-1]` | **~60% of tasks mis-bracketed** | **Re-attribute before dispatch.** `tools/gen_tasks_md.py` carries the fix but is **hard-coded to 001** — parameterizing it is a **prerequisite**, since `dispatch` reads the bracket |
| **2** | **Multi-pillar tasks bucket to their first pillar's phase** — the root cause of E1 | PIL-6: **0 shown vs 11 real** | The phase table above uses true load. **`tasks.md` must be phased the same way, not by the generator's bucket** |

**This is the same defect 001 documented** — measured at 57 of 103 (55%) there, ~60% here.
**It is a property of the shared plugin, not of any thesis**, and 001 fixed it locally
rather than upstream. Every new thesis inherits it.

## §Declared-N/A Register

**25 tasks are declared not-applicable**, with the reason. This is not budget-trimming —
each is a mode that **cannot serve any pillar of this thesis**, and running it would
produce an artifact that looks like evidence and isn't.

| Mode | Ticker set | Tasks | Why N/A |
|---|---|:---:|---|
| `earnings-vs-consensus` | all 17 | **17** | Measures **analyst surprise**. No pillar of this thesis uses analyst estimates — **Market Data Stage is `none` for every matrix row**, and the register application needs the *income statement*, not consensus. `consolidated-p-and-l` and `margin-analysis` carry the work |
| `deep-dive-ai-trend-assessment-…` | BWXT, GOOG, NVDA, MRCY | **4** | AI trend exposure is 011's question, not a validation question |
| `deep-dive-data-value-trend-assessment-…` | BWXT, GOOG, NVDA, MRCY | **4** | Same |

> **A declared-N/A is a scope decision, and it is auditable.** Each is recorded here rather
> than dropped silently, so a reviewer can disagree with the call and restore it. **The
> alternative — running 25 tasks that produce irrelevant artifacts — is worse than
> declaring them**, because it inflates the ledger with material that looks like evidence.

## Citation requirement — a cross-cutting obligation on all 87 dispatched tasks

**Spec §1d, added at clarify round 3.** Every material figure and fact carries a
source-page citation:

```
[📄 {ticker} {form_type} p.{N}](https://agentii.ai/v/{ticker}/{citation_id}/{N})
```

**The ticker is mandatory** — the short form `agentii.ai/v/{citation_id}/{page}` does not
resolve; the portal joins `src_documents` to `sec_filings`, which needs it.

**This is a phase-crossing obligation, not a phase.** Three contract rules enforce it at
level `fail`. `citations_pages_located` requires every page number to name the tool that
established it — **a guessed page number resolves to the wrong page, which is worse than
no link.** Executed once at specification: four anchor figures verified at source, and
**DA-10 resolved as a side effect** (the filing attributes the 22.4% ARPU decline to
international expansion and lower-priced plans → **mix-shift, not price erosion**).
Budget **+0 tasks** — the work is inside each task, not alongside it.

## Concurrency and budget

| Limit | Value | Plan's use |
|---|---|---|
| `max_concurrent_subagents` | 5 | Planned parallel width **5**. At the cap. |
| **Real unit of work** | **40 distinct `(ticker, skill)` analyses** | **Not 112 and not 87.** The mode expansion is a *decomposition*, not a multiplier — 5 `unit-economics` modes are sections of one artifact. **40 analyses ÷ width 5 = 8 dispatch rounds**, and that is the schedule. |
| `max_tasks_per_day` | 40 | Well inside. **Pacing is not the constraint; Phase 2's instrument adequacy is.** |
| `max_theses_active` | 6 | 6 (001 + wave-1 five). **At the cap** — wave 2 cannot open until a slot frees, so 002 cannot be replaced if it stalls. |
| `budget.max_tasks` | **120** | 112 emitted. **Raised 40 → 70 → 140 → 120.** The 140 figure was set before E2/E3 removed 25 mis-scoped and 20 over-depth tasks; **the budget was cut, not grown, once the work was measured.** |

**Dispatch schedule, corrected.** An earlier draft of this plan computed "87 dispatched ≈
12/phase ≈ 2.2 working days" — treating mode-tasks as work units. The phase evaluation
found that **overstates the schedule by ~2.8×**: 112 mode-tasks decompose from **40 distinct
analyses**, and at width 5 that is **8 rounds**. Phase 3's 56 tasks are **17 mechanical
`validate_calculation` calls**, not 56 units — **~4 rounds, not 12.**

### 🔴 Dispatch rule — group by ISSUER, not by pair (added during Phase 1)

**The unit of dispatch is the issuer-within-a-phase, not the `(ticker, skill)` pair.**
Three phases contain two pairs on the same issuer:

| Phase | Issuer | Pairs | Risk if dispatched separately |
|---|---|---|---|
| **1** | RKLB | `unit-economics` + `operational-kpi` | Two agents read the same 10-Q and could quote different payload or launch figures |
| **1** | SPCX | `unit-economics` + `operational-kpi` | Same — and both touch the DA-11 nameplate |
| **2** | BWXT | `secular-trends` + `supply-chain` | Same |
| **2** | MRCY | `secular-trends` + `supply-chain` | Same |
| **5** | SATS | `risk` + `competitive` | Same — and both touch the DA-24 asset-sale contamination |

**Two agents on one issuer produce two artifacts that can disagree, and nothing in the
pipeline detects the disagreement.** One agent per issuer per phase writes both artifacts
from a single filing read — cheaper, and consistent by construction.

**Phase 1 was dispatched at pair granularity, so RKLB and SPCX each had two agents in
flight.** The `RKLB × operational-kpi` artifact independently flagged a cross-check for its
parallel partner, which is the right instinct — but the reconciliation is manual and is
**recorded as a Phase 1 verification step** rather than assumed to have happened.

## Deviation Register (Q35)

**No deviation requested.** 001 accepted one (a P10 deviation, because its Pillars 2 and 5
concerned orbital compute without meeting P10's five gates). **002 does not need one:**

| Constraint | Why it does not bite |
|---|---|
| **P10** | 002 *validates F2's constants*; it does not underwrite orbital compute, value it, or propose a position. P10 gates underwriting. |
| **P11** | The universe contains **RKLB** (deal security as acquirer). 002 reads its *per-launch cost disclosure*, not its equity value. The artifact contract requires `deal_security_basis: standalone_pre_merger`. **Handled by contract.** |
| **P6** | No private company enters this thesis. Varda appears only via 001's disposition classification (Pillar 7). |

> A deviation register with no rows **is** a complete plan — the Q35 rule requires all five
> columns only for an *accepted* violation. There is none to accept.

## Side artifacts (Q36)

| Artifact | Status | Note |
|---|---|---|
| `brief.md` | ✅ | Q7 `method_selection` recorded **not-applicable-by-scope**: the corpus has **no industrial/aerospace domain**, so sector-keyed retrieval returns zero **by construction** — and this thesis **does not want it**, since a borrowed strategy analogue would be a category error in an evidence audit. |
| `entities.md` | ✅ | `entity_claims` schema + entity/metric map. Q42 bars schema **not required** (`market_data_stage: none` throughout) — stated so the absence is a decision. |
| `reproduce.md` | ✅ | skills + five pins + `as_of`, plus a reproduction recipe and the cited reproducibility limits. |
| `contracts/` | ✅ | `artifact-frontmatter.yaml` — `citations` block, three citation rules, and `data_integrity_register_applied`. |

## Constitution Check — second evaluation (post-sizing: aggregate)

**Cannot be evaluated, because no sizing occurs.** `CONC_SECTOR`, `CONC_THEME` and
`EXPO_MACRO` are aggregate constraints over `position_pct`, and this thesis sizes nothing.
**Recording a PASS would be false assurance**, as in 001.

| Substitute check | Status | Evidence |
|---|---|---|
| No position sized, implied or recommended | **PASS** | Verified against all 7 pillars. |
| Sub-sector spread within the research set | **PASS (informational)** | 5 sub-sectors; max **36%** of analytical effort (`aerospace_defense`). Research weights, not positions. |
| Aggregate check deferred to | **011** | Carried forward from 001. |

## Risks to the plan

1. **The denominators may not resolve — and that is the point.** PIL-1 fires on a >15%
   move, but `UNRESOLVABLE-FROM-PUBLIC-SOURCES` is the likelier outcome for one or more.
   **A non-resolution is a finding**, and the honest output is a **wider band** on every
   downstream $/kg figure, not a preserved point estimate.
2. **Defect 1 will silently corrupt the task list.** `dispatch` reads the pillar bracket,
   and ~60% are wrong. **Parameterizing `tools/gen_tasks_md.py` is a hard prerequisite.**
3. **Phase 3 pacing.** 56 tasks at width 5 is ~12 rounds. Schedule, not difficulty.
4. **The citation requirement can be satisfied decoratively** — a link to the right
   document and the wrong page looks correct. `citations_pages_located` is `fail` for
   this reason.
5. **001's pin is 1.2.0 and `stale`** — now a hard gate, above.
6. **SPCX has exactly one 10-Q on the platform** (`sec8`). The anchor's entire evidence
   base — including the A1b falsification the constitution rests on — traces to a single
   filing with no second source to corroborate against. **Phases 3 and 4 both depend on
   it**, so a re-ingest of `sec8` would move two phases at once.
