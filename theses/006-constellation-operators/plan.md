# Research Plan: 006 — Tier 2 — Constellation Operators: Connectivity, Spectrum & Geospatial

**Status**: Active · **Generated**: 2026-09-20 · **Constitution pin**: `1.6.0`
**Author**: `agentii.plan` is **not a command** in `agentii_cmd.py` — the kit ships
`specify, clarify, tasks, constitution, singleskill, converge, challenge, implement, status`.
This plan is authored by hand against **003's and 004's** `plan.md`, which are the workspace's
two passing precedents. That is stated rather than implied, because a plan that claims a
generator it did not use is the same defect class as a figure that claims a basis it lacks.

---

## Constitution Check (first evaluation — Q35)

| Requirement | Where 006 stands | Verdict |
|---|---|---|
| **P4 — evidence discipline; a grade is not a basis** | §1c mandates the component identity in-line for every `operating_income` read, and §0.2 inherits the rule that a `DEMONSTRATED` grade is not sufficient for an input | ✅ satisfied by construction |
| **P11 — deal securities are not underwritten on fundamentals** | IRDM and GSAT are P11; §1b P4 forbids a fundamentals underwrite and **Q-16 extends the ban into the strategy layer** — they get gate cards, not ideas | ✅ satisfied, and **strengthened at Q-16** |
| **P9 / F6 — a dateable catalyst inside 180 days** | §1b P6 instruments it directly, and names the narrower skill bar (**20–60 days**) as the binding constraint (Q-20) | ✅ satisfied |
| **F6 — spectrum and orbital slots are gating assets, not paperwork** | §1c instrument 2 makes the checklist dated and sourced per name and per gate; §1b P4 lists the gates | ✅ satisfied |
| **Risk Framework — ≤2 positions per sub-sector; 2% binary cap** | §5 states it; §3's `position-sizing` row sizes inside it | ✅ satisfied |
| **The membership test — one axis: primary revenue from operating a constellation** | §2 states it and applies it to all 8 members, 5 `NOT_READY` names and 4 cited third parties | ✅ satisfied |
| **Q33 — a thesis must pin a constitution version, and a stale pin is a hard failure** | See **F3** — the pin resolves, but **two of the three places the version is recorded disagree** | ⚠️ **see F3** |

**Scalar-clearance note (why a second check is still run).** 003 and 004 each ran this check
twice, the second time after the plan's findings had changed the work. The same applies here and
for a sharper reason: **F1 below removes 16 of §3's analyses from the schedule**, and
**F2 adds a sequencing constraint the spec does not express**. Both change what the plan
schedules, so the second evaluation is not a formality.

---

## ⭐ The governing directive — consume, never re-run

**This is the owner's instruction for this thesis, and it is the plan's first constraint:**

> 001–004 已经跑了大量调研与分析。**不要重复做。** 006 只能在它们的基础上**更广、更深**。
> **不要重复跑相同的 skills。** 在前面的基础上只有 **Challenge and validation**，更深入分析。

Encoded as three rules that every phase below obeys:

1. **CONSUME, DO NOT RE-RUN.** A `(ticker, skill)` pair 001–004 already produced an artifact for
   is **cited, never re-executed**. §0 of the spec is the propagation mechanism; the plan adds
   §F1's ledger of exactly which pairs those are.
2. **RUN ONLY WHAT IS NEW** — the **79** pairs that no prior thesis touched, plus the five skills
   this thesis introduces (`trade-idea-generation`, `position-sizing`, `qualitative-filtering`,
   and — added at the evaluation, F12 — `sotp-valuation` and `residual-income`).
3. **CHALLENGE AND VALIDATE WHAT IS INHERITED.** Where 006 consumes an upstream figure, it
   **challenges it** — re-deriving on the inherited basis and recording disagreement — rather
   than accepting it. That is the layer 002 performed for 001, and it is now 006's obligation
   toward 001–004. **§The challenge layer** below specifies it.

**A note on what "do not repeat" does NOT mean.** It does not mean *do not read the same
filing*. 006 legitimately re-reads the same 10-Qs, because a component identity computed on a
filed cell is a **different object** from a margin read off a served metrics block — 002 proved
that they differ by **46.47 pp** at SPCX. The prohibition is on **re-running a skill to
reproduce a result that exists**, not on touching the same source.

---

## 🔴 F1 — 16 of §3's analyses already ran in 001–004, and three names are untouched. *(Phase 0 — changes the work)*

**Measured, not estimated.** Every artifact under `theses/00{1,2,3,4}/artifacts/` was parsed for
its `{date}_{skill}_{mode}` filename and intersected with §3's declared matrix.

| | at plan time | after F12 | **after the second pass** |
|---|---:|---:|---:|
| §3's declared `(ticker, skill)` pairs | **85** | 99 | **95** |
| Already produced by 001–004 → **CONSUME** | **16** | 16 | **16** |
| **Must be newly run** | **69** | 83 | **79** |
| Repeat rate removed by this finding | **19%** | 16% | **17%** |

*(F12 added the two valuation skills; **the second pass settled their depth and scope** — Deep
`sotp-valuation` on the scarce trio plus Standard on the granted four, and `residual-income` on
the scarce trio only. **None of the 10 valuation pairs is consumed.**)*

**The 16 consumed pairs, with their sources.** ⚠️ **The description column is the artifact's OWN
title, taken from the file — not a paraphrase.** The first version of this table paraphrased, and
**six of the sixteen paraphrases did not match the artifact they pointed at** (F16). Each row is
cited into §0, never re-run:

| Pair | Source theses | What the artifact actually contains |
|---|---|---|
| `IRDM × competitive` | 001, 002, 003 | **Competitive Position, Q2 2026** — P11 deal-security status and the pre-merger standalone basis |
| `IRDM × recent-quarter` | 002, 003 | **recent-quarter methodology** — the component identity closing **zero residual on 7 of 7 periods** |
| `IRDM × risk` | 003 | **P11 deal-security tagging and the falsifier-reachability census** |
| `IRDM × secular-trends` | 003 | ⚠️ **"the platform cannot represent this thesis's question"** — a **negative** result |
| `GSAT × competitive` | 001, 003 | **Competitive Position (Mobile Satellite Services)** — the revenue series ($64.772M / $67.148M, −3.5%) |
| `GSAT × recent-quarter` | 003 | **the corrected series, the sign layer, and a two-basis Q1 2026** |
| `GSAT × risk` | 003 | **the register has absorbed the platform's own defect** — the DA-23 + 1,000× census |
| `SATS × recent-quarter` | 002, 003 | **the register's own DA-24 origin instance, RE-TESTED** — and the independence claim **FAILS** |
| `SATS × risk` | 001, 002 | **Regulatory Risk, Q1 2026** — *"why SATS carries the P6 regulatory analysis"* |
| `PL × growth-strategy` | 003 | **"A Launch Share That Cannot Be Drawn, at the Customer the Curve Is Supposed to Reach"** |
| `PL × operational-kpi` | 001 | **Operating Baseline** — whose finding is *"exact magnitude match, opposite sign"*, i.e. a **defect**, not a baseline |
| `PL × ratio-analysis` | 003 | **the margin ladder, the served-sign defect, and the demand-side programme-cost shares** |
| `PL × recent-quarter` | 003 | **the best gross margin in the universe, and a fixed-cost wall** |
| `PL × sector-overview` | 003 | **the highest gross margin in the universe, at −37% operating** |
| `HAWK × operational-kpi` | 001 | ⚠️ **an Operating-Baseline artifact whose own `definitions_used` reads `operating_income UNVERIFIABLE`** — **there is no usable HAWK KPI series in the corpus** |
| `HAWK × recent-quarter` | 002 | **the DA-28 site** — and *"a DA-28 that MASKS a separate DA-23"* |

**And the three names with ZERO upstream coverage — every one of their pairs is new:**

| Name | New pairs | Why untouched |
|---|---:|---|
| **BKSY** | **12** | never read by any prior thesis; `sector` unassigned |
| **ASTS** | **10** | 002 recorded it as a *spectrum counter-party*, never a competitor; **no ASTS financials exist anywhere in 002** |
| **VSAT** | **9** | `PARTIAL`; 002 measured the served defect (**19 of 30 rows fail, 11 with the `2×` fingerprint**) but never read the filings for a thesis |

**The full accounting, stated once and consistently — because the first draft of this plan got
it wrong and the error is instructive.** *That draft's phase table carried hand-written
per-phase numbers that did not reconcile to 16; they were recomputed from §1b's `Subscribed`
lines and the table above now matches this ledger.*

| Layer | at plan time | **now** |
|---|---:|---:|
| §3 declares | **85** | **95** |
| Subscribed by a pillar (**union**) | 69 | **95** |
| Subscribed by **no** pillar | **16** → **F11** | **0** ✅ |
| Already run by 001–004 → **CONSUME** | **16** | **16** |
| **Must be newly run** | **69** | **79** |

**⚠️ The unowned-pair column is now ZERO, and it changed for a reason worth recording.** At plan
time **16 rows had no pillar owner** (F11); the evaluation's fix extended P1, P2 and P3's
`Subscribed` lines to claim all 16, and E1's two valuation rows were **subscribed at the moment
they were written** — so the gap closed rather than recurring. **`plan_audit` I2 would have
caught E1's omission** (it did, in fact, on the first attempt — see F12), **but it cannot catch
F11's shape**, which is why F11 was found by hand.

**Why this is F1 and not a footnote.** The plan-time matrix declared **85** pairs (**95** after
F12); the pre-F1 schedule would have dispatched all of them, and **17%**
of them would have reproduced work that already exists**, and — worse — **would have produced a
second, parallel copy of a figure under a different thesis_id**, which is precisely the
divergence §0 exists to prevent. **The remedy is a spec-level one and is recorded as A-1 below:
§3's matrix should mark the 16 consumed pairs, so that `tasks_md` does not dispatch them.**

---

## Phases

**Seven phases, mapped one-to-one onto §1b's six pillars plus a hand-off.** §7 of the spec
declares this structure; the plan adds the wiring, the gates and the F-findings beneath it.

| # | Phase | Pillar | Pairs | Consumed | **New pairs** | **New mode-tasks** | Week |
|:--:|---|:--:|---:|---:|---:|---:|:--:|
| **0** | **Preconditions** — sector assignment, listing guards, the F1 ledger | — | — | — | — | — | 0 |
| **1** | Decomposition — IRDM's residual decline by line | P1 | 12 | 5 | **7** | **25** | 1 |
| **2** | Attribution — the three-basis SOTP via `sotp-valuation` + `residual-income` | P2 | 25 | 1 | **24** | **60** | 2 |
| **3** | D2D placement — all eight names on the axis | P3 | 17 | 4 | **13** | **62** | 3 |
| **4** | The gate chain — one dated checklist per name | P4 | 17 | 6 | **11** | **32** | 4–5 |
| **5** | Queue close-out — the §0b scorecard | P5 | 9 | 1 | **8** | **8** | 6 |
| **6** | **The sector book** — strategies, sizes, structural analogues | P6 | 18 | 0 | **18** | **18** | 7 |
| **7** | Hand-off — the register and the sector book for 007 / 009 / 011 | — | — | — | — | 0 (hand-emitted) | 8 |
| | **Total** | | **98** | **17** | **81** | **205** | |

> ⚠️ **The `New tasks` column is `tasks_md`'s OUTPUT, not a model of it** — see F17. It read
> **19 / 60 / 56 / 26 / 8 / 18 = 187** until the fifth evaluation ran the generator, which
> produces **205**. **The column was wrong by 18 and the total by 89**, because it was computed
> from the registry's `essentials_modes` rather than from the tool that generates the work.

> **⚠️ THE `New pairs` COLUMN WAS MISLEADING AND IS NOW PAIRED WITH `New mode-tasks`.** At plan
> time it read P6 = 18 as *"the largest single phase"* — **which was wrong.** P6's three skills are
> all `Standard` with an empty `essentials_modes`, so each pair costs **one** mode-task: 18 pairs
> = **18 tasks**. P2's ten pairs include `unit-economics` at **Deep**, so **P2 was always the
> heaviest phase and the pair count hid it.** **Pairs measure scope; mode-tasks measure load, and
> only the second schedules a week.** Both are shown now.
>
> **The pair columns sum to 98 / 17 / 81, while the pair union is 95 pairs / 16 consumed /
> 79 new. Both are correct on their own basis, and the gap is named
> rather than smoothed:** these columns are **per-pillar mentions** and **6 pairs are subscribed
> by two pillars**, so the union is smaller than the sum. **The matrix dispatches each pair ONCE**
> (`tasks_md` expands §3, not the `Subscribed` lines — the lines are a coverage invariant, I2), so
> **205 is the scheduling number** — and **tasks are NOT double-counted the way pairs are**,
> because the generator emits them from the matrix per `(ticker, skill, mode)`. Use
> **205 against the `max_tasks: 210` budget — headroom 5.**

> **These columns are computed from §1b's `Subscribed` lines against the F1 ledger, not assigned
> by hand** — an earlier draft carried five hand-written numbers that did not reconcile to the
> ledger's 16, and they were replaced rather than rounded.
>
> ⚠️ **The columns sum to 60 new and 12 consumed, while F1's ledger reports 58 and 11. Both are
> correct on their own basis**: these are **per-pillar mentions**, and **3 pairs are subscribed by
> two pillars** (2 new + 1 consumed), so the union is smaller than the sum. **Use the mentions
> column to plan a phase's load and the union column to count distinct work.** Stated because a
> reader who adds the column and compares it to F1 would otherwise find a 2-pair discrepancy with
> no explanation — which is the defect this programme spends its time removing.
>
> **P6's 18 is the largest single phase**, and it is the arithmetic behind the Q-17 budget.

### ⚠️ Phase 0 exists because three of §3's rows cannot evaluate without it

§2 records three **preconditions that are not assumptions**:

1. **ASTS, VSAT and BKSY carry `sector: null`.** *"No sector-aggregate constraint evaluates until
   it is assigned by hand, and the assignment is recorded in every artifact's frontmatter."*
   **Three of 006's eight names — 31 new pairs between them — are blocked on a manual field.**
2. **HAWK carries a `DA-28` candidate** — four non-agreeing share counts (4.2M–98.0M) and an EPS
   bridge failing by 72%. *"No DA-23 detector may be run on HAWK without a listing-date guard."*
3. **The F1 ledger** must exist before dispatch, or 19% of the matrix re-runs.

**Phase 0 has no pillar and therefore no `tasks.md` row** — the same structural position 004's
Phase 0 held, and tracked here for the same reason: *a phase that produces no artifact is
invisible to the dispatcher.*

---

## 🔴 F2 — `position-sizing` is `late`, and 006 is otherwise `none`. The price rule bites here. *(Phase 6 — changes the schedule)*

**Found by applying 004's F13 to the row this thesis added yesterday.** 004 discovered that
`data-tools/refusal.py` implements **`PRICE_ACCESS_PREMATURE`**:

```python
if stage == "late" and tool == "get_price_history":
    return refuse("PRICE_ACCESS_PREMATURE",
        "price is the FINAL CHECK for fundamental work, never the raw material")
```

**004's plan recorded the generalisable lesson, and it transfers verbatim:** *both plan passes
evaluated the schedule's internal consistency and **neither asked whether the platform's own
rules permit the work being scheduled**. The rule lives in `refusal.py`, not in any gate.*

**006 is now the second thesis in the workspace with a `late` row** — and the first with exactly
one, sitting inside an otherwise-`none` tier. Three consequences the plan must enforce:

1. **Tool split, exact:** `market_data.get_quote` ✅ admissible at the end of a `late` row's
   phase · `get_price_history` ❌ **refused**. ⚠️ `live_snapshot.py` calls **both**, so it must
   not run against 006 at all.

   > ⚠️ **SCOPE CORRECTED at the plan evaluation (F12): F2 originally said 006 had exactly ONE
   > `late` row. It now has THREE** — `position-sizing`, plus the two valuation skills F12 added.
   > **The finding was understated rather than wrong** — it was computed before those rows
   > existed and then asserted *"the only `late` row"* in a document whose job is to stay true
   > when read. **The rule does not change; its scope does**, and that scope is now three rows
   > across Phases 2 and 6 rather than one in Phase 6.
2. **And the row cannot obtain its inputs anyway.** §0.4 records that **no price series exists
   for any Tier 2 name**, so this is a `late` skill in a tier with no prices. **Every published
   size states in-line that its instrument had no price series behind it** (Q-19) — which is a
   disclosure obligation on Phase 6's output, not a reason to lower the stage.
3. **`as_of` discipline.** The `as_of` is **2026-09-18** for every artifact. A size published in
   Phase 6 carries that stamp, not the date it was computed.

---

## 🔴 F3 — The constitution's 1.6.0 amendment has no Sync Impact Report, and its YAML mirror is stale. *(Constitution Check — a provenance defect)*

**Found by checking the pin rather than trusting it** — 006's own header says *"a stale pin is a
hard failure under P4, not a footnote."*

| Where the version is recorded | Says |
|---|---|
| `constitution.md` body (`**CONSTITUTION_VERSION**`) | **1.6.0** ✅ |
| `constitution.md` — the Sync Impact Report block | **last entry is `1.4.0 → 1.5.0`** ❌ no 1.6.0 entry |
| `constitution.yaml` — the ratified-against attestation | **v1.5.0** ❌ |
| 006's spec / thesis.md / contract `const` | **1.6.0** ✅ (all three agree) |

**So the pin RESOLVES — 006 is not pinning a version that does not exist — but the amendment
that created 1.6.0 was applied to the body without its record.** The 1.6.0 content **is**
present: the one-axis re-cut, the `PARTIAL` redefinition, the DA-26 census correction, the GSAT
addition to the DA-23 census, VRT's removal from membership, BKSY's reclassification.

**What is missing is the record of why, and its classification.** Every prior bump carries a
Sync Impact Report naming the amendment, its MINOR/PATCH rationale, and what it touched. **1.6.0
has none — which means a downstream reader cannot reconstruct what changed or why**, and the
`constitution.yaml` mirror that the executable constraints are ratified against **attests a
version four theses have already moved past.**

> **Recorded as a workspace finding, not a 006 blocker.** 006 proceeds at `1.6.0` because its own
> three declarations agree and the body supports them. **The remedy belongs to the constitution's
> owner, not to this thesis** — and it is the same class as 004's unbuilt `I5`: *a version is
> recorded in three places and nothing checks that they agree.*

---

## 🔴 F4 — §6's "second contract gap" does not exist. *(spec correction)*

§6 records **two** contract gaps. The first (PIL-6 unused) **was already withdrawn** at my
2026-09-20 round. **The second is false and this plan records it:**

> §6 states the `da_id_registered` rule validates against **`DA-23…DA-28`**, so *"DA-29 and DA-30 …
> cannot yet be declared in `definitions_used` without failing the rule."*

**006's own contract already reads `DA-23..DA-30`.** The rule was widened before this thesis was
chartered. **The stale range is in 004's contract, not 006's** — so the spec is describing a
constraint it does not have, and **P2's obligation to declare `DA-30` in `definitions_used` is
discharged, not blocked.** Recorded as **A-2** below.

---

## Dependency graph and critical path

```
001 ──┐
002 ──┼──► 006 ──► 007   (primes as incumbent satcom competition)
003 ──┤      │  ──► 009   (D2D as compute-adjacent demand)
004 ──┤      │  ──► 011   (the sector book as INPUTS to its allocation)
005 ──┘      └──► 005   (the gate chain, BY CITATION — 005 consumes it)
```

| Edge | Direction | Nature |
|---|---|---|
| 001 → 006 | inbound | the panorama — consumed, §0.1 |
| 002 → 006 | inbound | the validated input set **with its verdicts**, §0.2 |
| 003 → 006 | inbound | the value-pool map + the corrected operator ladder, §0.3 |
| 004 → 006 | inbound | the Connectivity reference + the **permitted-consumer boundary** |
| **005 → 006** | **inbound, citation-only** | RKLB's financing facts — the $3.6B bridge, the consideration mix |
| **006 → 005** | **outbound** | **the IRDM/RKLB gate chain.** 005 carries its RKLB row `known-open` until 006's P4 lands |
| 006 → 007/009/011 | outbound | the attribution register + the sector book |

**Ordering (Q-18): 005 and 006 run in TRUE PARALLEL.** The edge to 005 is a citation rather than
a data dependency, and the two are now **parallel sector books on different tiers** (005's six
names, 006's eight) with no resource contention. **The gate chain is a mid-flight delivery.**

**Critical path**: `Phase 0 → 1 → 2 → 3 → 4 → 5 → 6`. **Phase 1 is the true gate** — see F6.

⚠️ **The wave defect is still open.** PROGRAM.md §3 places **006 and 008 in wave 1**, 006
self-declares Wave 1, and **005's header calls 006 wave-2** and mislabels 008 and 009 in the same
sentence. Two sources to one; 005's header is the outlier and needs its own PATCH. Recorded at
Q-11 and Q-18, **not resolved here because it is not 006's file to change.**

---

## Gates per phase — the tools that exist, and the ones that do not

| Gate | Tool | Status |
|---|---|---|
| Plan invariants **I1–I4** | `tools/plan_audit.py` | ✅ exists — **4/4** today (**95 pairs, 98 subscriptions, 0 unowned**) |
| Citation well-formedness + resolution | `tools/check_citations.py` | ✅ exists |
| Frontmatter / contract conformance | `tools/check_contract.py` | ✅ exists |
| **DA-23 sign strip** | `tools/check_sign_strip.py` | ✅ exists |
| Artifact frontmatter (**G1**) | `plugin/scripts/g1_gate.py` | ✅ exists — **but latent**: `data_class` is required by the gate and absent from 001–003's contracts |
| Clarify candidates | `tools/clarify_scan.py` | ✅ exists — **2 candidates, both false positives** (F9) |
| Task generation | `tools/tasks_md.py`, `tools/gen_tasks_md.py` | ✅ exist |
| **Market-data-stage vs registry** | — | ❌ **proposed as `I5`, never built** — see F8 |
| **Formability of a declared input** | — | ❌ **proposed as `I6`, never built** |
| **Version-record agreement** | — | ❌ **F3's shape; nothing checks it** |

### Wiring, phase by phase

| Phase | Gate that must pass before it closes |
|---|---|
| **0** | `plan_audit` 4/4 · sector assigned for ASTS/VSAT/BKSY in frontmatter · HAWK listing guard in place · **F1 ledger written** |
| **1** | `check_sign_strip` on every IRDM figure · **component identity in-line** (DA-23) · **002-F8's re-run landed** or the pillar is recorded `UNEXERCISED`, not carried |
| **2** | `check_contract` · **every margin carries a named denominator** (DA-30) · all three bases printed per name · `g1_gate` on each artifact |
| **3** | all 8 names placed, **including the granted-licence trio without D2D** · ASTS placeable or the axis is restated |
| **4** | every gate either **dated with a filed source** or recorded as a disclosure-quality finding · `deal_security_basis` set on all IRDM/GSAT artifacts (P11, **fail-level**) |
| **5** | every §0b row converted or **classed with a named resolving source** · verdicts preserved as verdicts |
| **6** | **`get_price_history` never called** (F2) · every size states its missing price series · **`as_of` 2026-09-18** on all · the all-zero case reported if it obtains |
| **7** | `check_citations` clean · the register and the sector book published · 005's gate-chain citation named |

---

## ⭐ The challenge layer — what 006 owes 001–004

**This is the second half of the owner's directive, and it had no home in the spec.** Where 006
consumes an upstream result, it **challenges** it. Not a re-run — a **validation on the inherited
basis**, in the shape 002 performed for 001.

| What is inherited | The challenge 006 runs | Where |
|---|---|---|
| 001's IRDM margin direction (*"the licence is durable, the service business is not"*) | **re-derive on the FY basis** — 003 already showed the margin RISES (**24.12% → 27.07%**) and that the Q2 decline is **63.8% non-recurring deal cost**. 006 tests whether the corrected framing survives | Phase 1 |
| 002's `validate_calculation` failure modes | **re-verify the four modes at a Tier 2 name** — 002 demonstrated them at SATS; 006 asks whether they reproduce at IRDM and GSAT | Phase 1 |
| 003's operator margin ladder | **re-derive the Tier 2 rows on the filed component identity**, and report any row that moves — the ladder's own anchors are FY and its operator rows 3M, **and the two ends are not on the same basis** | Phase 2 |
| 003's GSAT **−7.37%** | **confirm the sign strip and the 1,000× unit offset directly**, by calling both endpoints on one accession | Phase 2 |
| 004's Connectivity reference | **verify it is consumed inside its boundary** — 004 permits a *benchmark*, never a borrowed multiple, and admits **0 of 11** comparators | Phase 2 |
| 004's **312.8×** | **test whether it is reusable at all here** — 004's own finding is that a `P11` price is inadmissible as a fundamental, **and IRDM and GSAT are both `P11`** | Phase 2 |
| Every inherited `DEMONSTRATED` | **carry the basis as well as the grade** — 002's programme result is that a grade does not carry one (SPCX `operating_margin` reproduced on two bases **46.47 pp apart**) | all phases |
| Every inherited correction | **verify it reached a pin** — 002 measured that **only 3 of 32 corrections did**, and *"a correction that is recorded and never propagated is indistinguishable, in effect, from one never made"* | Phase 5 |

**The rule that governs it**: a challenge that **agrees** is recorded as a confirmation with its
basis; a challenge that **disagrees** is recorded as a correction and **propagated** — never
silently resolved in favour of the newer thesis.

---

## Side artifacts (Q36 — produced by `agentii.plan`)

| Artifact | Purpose |
|---|---|
| `theses/006-constellation-operators/plan.md` | **this file** |
| `_cross/tier2-attribution-register.md` | the primary — what 007, 009 and 011 cite **for value** |
| `_cross/tier2-gate-chain.md` | the one dated checklist per name — **005 consumes it by citation** |
| `_cross/tier2-d2d-placement.md` | the placement map |
| `_cross/tier2-sector-book.md` | 🆕 **Q-21** — the strategy set, the gate cards, the structural analogues, the two-count headline |

---

## Phase-by-phase evaluation against upstream results — the F-findings

`F1`–`F4` are recorded above at their phases. The remainder, in the order they change the work:

### F5 — IRDM's SERVED margins are inadmissible, so P1 cannot read them. *(Phase 1 — changes the method)*

003 measured the defect exactly: **every served quarterly IRDM margin divides by a single
`$200,000` thousand denominator** — the Aireon hosting-agreement revenue **ceiling**
(`srt:MaximumMember`, six-month period) — and **8 of 8 reproduce to the basis point**. 003's
verdict is unambiguous: *"IRDM's served margins do not measure IRDM and NONE of them is
admissible to this map."*

**P1's entire object is a margin decomposition.** So Phase 1 **must** recompute from filed
components, and **the served metrics block may not be opened for a margin**. This is the same
discipline 004 applied to SPCX's sign strip, at a different defect.

### F6 — P1 is gated on `002-F8`, and until it lands IRDM's ladder admission is `UNEXERCISED`. *(Phase 1 — a genuine blocker)*

003 records: *"IRDM's ladder admission is `UNEXERCISED`, pending the component re-run **002-F8**
requires. The served `operating_income` carries a **DA-29 signature**: `computed −51,791,000`
against `reported +51,791,000`."*

**A `DA-29` signature is the back-solve flag** — *"if any term in a reconciliation appears NOWHERE
in the source, the check is a BACK-SOLVE — and a back-solve closes exactly, so it cannot be
caught on the closure."* **So Phase 1 inherits a reconciliation that closes and may be a
back-solve.** The plan's position: **run the component re-run first, and if it does not land, P1
is recorded `UNEXERCISED` rather than reported as a pass.** P1 is the Minimum Defensible View;
**a MDV that rests on an unexercised check is not defensible.**

### F7 — Three names are blocked on a manual field, and one needs a guard before any detector runs. *(Phase 0)*

Already stated in Phase 0 above. Recorded here for the F-ledger's completeness: **the
`PARTIAL` precondition is not an assumption but a task**, and it blocks **31 pairs across ASTS,
VSAT and BKSY**.

### F8 — No tool checks a declared stage against the registry, and that is now demonstrated twice. *(all phases)*

004's checklist proposed an **`I5` market-data-stage consistency check** and it was **never
built**. **006 is the second supporting case and the cleaner one**: my 2026-09-20 re-scope
declared `position-sizing` as `none` **in good faith**, `plan_audit` returned **4/4**, and
**nothing anywhere objected** — the mismatch (registry: `late`) was found only because a human
read the registry entry. **Recorded as a proposal with two supporting cases, not as a fix.**

### F9 — Two scanner candidates are false positives, and the tool should not be "fixed" by changing the spec. *(Phase 0)*

`clarify_scan.py` returns `rationale-SPIR` and `rationale-TSAT`. **Both are false positives.** The
regex `^\|\s*([A-Z0-9]{1,5})\s*\|[^|]*\|[^|]*\|[^|]*\|\s*\|` uses `[^|]*`, which **spans
newlines** — so it reads a row's *closing* pipe plus the next row's *opening* pipe as an empty
cell. **SPIR and TSAT both carry full rationale, and neither is a universe member.** The fix
belongs in the regex, not in the spec.

### F10 — Q-5 and Q-8 remain flagged for human confirmation, and the plan carries them as bounds. *(Phases 4 and 6)*

**Q-5** — spread width is unmeasurable (Market Data Stage `none` for all eight names). Carried
qualitatively. **Q-8** — the **6.0×** pro-forma net-debt-to-gross-profit bar is a **spec-set
threshold, not a measurement**, and RKLB's loss-making status makes any leverage denominator
sign-sensitive. **P4's falsifier does not rest on it**; it rests on the consent-date test, which
is mechanical. **Neither is silently resolved.**

---

### F11 — **16 matrix pairs are subscribed by no pillar, and `plan_audit` I4 passes anyway.** *(Phase 0 — an invariant defect)*

**Found by reconciling this plan's own phase table**, which is the only reason it was found at
all — **no tool reports it.**

§3 states I4's purpose in its own words: *"**I4** (every matrix skill is subscribed somewhere, **so
no row gets the `[P1]` fallback bracket**)."* **Its stated purpose is about ROWS. Its
implementation is about SKILLS.** So it passes — and it *should* pass, because every one of the
15 skills appears in some `Subscribed` line — while **16 of the 85 rows carry no pillar owner
and will each receive the `[P1]` fallback bracket the invariant exists to prevent.**

**The 16 unowned pairs:**

| Name | Unowned pairs |
|---|---|
| **PL** (6) | `business-model`, `operational-kpi`, `ratio-analysis`, `recent-quarter`, `sector-overview`, `secular-trends` |
| **BKSY** (5) | `ratio-analysis`, `recent-quarter`, `sector-overview`, `unit-economics` |
| **HAWK** (4) | `competitive`, `recent-quarter`, `sector-overview`, `unit-economics` |
| **ASTS** (1) | `recent-quarter` |
| **VSAT** (1) | `recent-quarter` |

**The pattern is not random, and it is the finding.** **PL, BKSY and HAWK account for 15 of the
16** — the three names added to this tier at the v1.6.0 re-cut. **Their matrix rows were written
when the names joined the universe, and no pillar's `Subscribed` line was extended to claim
them.** That is the same defect shape as everything else this programme keeps finding: **a change
applied in one place and never propagated to the places that depend on it.**

**Consequences, stated rather than assumed.** Those 16 rows are **11 new pairs plus 5 consumed
ones**. The consumed five need no work. **The 11 new ones would still dispatch** — the fallback
bracket does not *skip* a row, it *mis-files* it — so the cost is not lost work but **work filed
against a pillar that did not ask for it**, which corrupts the phase-level accounting this plan
is built on.

> ### ✅ FIXED AT THE EVALUATION — applied, not merely recorded.
> **P1, P2 and P3's `Subscribed` lines were extended to claim all 16**, and `plan_audit` now
> reports **0 unowned pairs** (95 subscribed of 95 declared). The assignment follows each skill's
> existing home: **P1** takes the freshness rows (`PL × operational-kpi` and `recent-quarter` on
> PL, BKSY, HAWK, ASTS, VSAT) because P1 is the decomposition pillar and **IRDM × recent-quarter
> was already there**; **P2** takes the value rows (`unit-economics`, `ratio-analysis`,
> `business-model`); **P3** takes the placement rows (`competitive`, `secular-trends`,
> `sector-overview`). **A-6 is CLOSED.** This is the **second** I4-class defect: 004's round 4 recorded
that *"I1 is too weak — it checks a universe ticker appears somewhere, and it passed while a
matrix row named cuts the filer does not report."* **Both invariants are under-strict relative to
their stated purpose, and both passed.**

### 🆕 F12 — **006 declared NO valuation skill at all, while its P2 deliverable IS a valuation.** *(Phase 2 — found by the evaluation, not by any gate)*

**The largest gap the plan-time pass missed, and it was hiding in plain sight.**

§1b P2's claim is *"running a **two-basis SOTP** per name"*; §7 Phase 2's task is *"build the
three-basis SOTP"*. **§3's matrix declared fifteen skills and not one was a valuation skill.**
The instrument was **hand-rolled**, while the registry ships `sotp-valuation` — **stage `late`,
and the exact skill 004 ran for the exact same deliverable.**

| Available | Stage | Declared by 006? | Verdict |
|---|---|---|---|
| **`sotp-valuation`** | `late` | ❌ no | ✅ **adopted** — 004's precedent, same deliverable |
| **`residual-income`** | `late` | ❌ no | ✅ **adopted** — *"Spectrum and licenses"* is an **indefinite-life intangible**, and residual income is the model built for an asset with **no finite life**. **It is the correct instrument for basis B** |
| `dcf` | `none` | ❌ no | ⚠️ **not adopted** — 004 found a forward DCF inadmissible **at SPCX** (negative consolidated FCF); **IRDM is profitable, so that verdict does not transfer** — but basis B is already covered, and a third valuation model would spend budget F13 shows is tight |
| `valuation-methods` | `none` | ❌ no | ⚠️ generic; the specific skills are better instruments |

**Adopted, and then CORRECTED on depth and scope at the second pass** — the first form put both
skills at **Standard on all seven names**, and that was wrong on one of them. **004 runs
`sotp-valuation` at Deep**, and its own purpose text calls it the *"constitution-mandated primary
instrument"*; 006 had given **P2's only deliverable** a single mode. **Deep on all seven would
cost 42 and put the total at 204 — twenty-four over budget.** The resolution is neither:
**Deep on `sotp-valuation` for the scarce-licence trio (IRDM/GSAT/SATS), Standard for the
granted-licence four, and `residual-income` on the scarce trio only** — because **basis C exists
only where the licence is separable**, and Q-3 records that as RESOLVED for IRDM and OPEN for the
other four. **Net +8 mode-tasks, 10 pairs, and the headroom falls 11 → 3.** Two consequences,
both recorded rather than absorbed:

1. **F2's scope changed** — three `late` rows, not one. See F2.
2. **`plan_audit` I2 caught the first attempt to add them**, because the new rows' skill and
   ticker cells were **bolded** and the parser reads a bare slug: `**sotp-valuation**` ≠
   `sotp-valuation`, and a bolded list **drops its first and last tickers** (`**SATS` /
   `HAWK**`). **Both were fixed by un-bolding, not by weakening the invariant** — the matrix's
   first column is a machine field, the same lesson 004 recorded when it bolded a skill name.
   **I2 failing there is the invariant working correctly.**

### 🆕 F13 — **The budget had never been reconciled, and the consume rule is what pays for the depth.** *(all phases)*

**The plan-time pass set `max_tasks: 180` and never showed the arithmetic.** Worse, the spec's §4
note recorded the matrix as **"79 distinct analyses"** — **a number that was never computed and
was wrong from the moment it was written**; `plan_audit` has always reported **85**.

| | mode-tasks |
|---|---:|
| **Full matrix, as `tools/tasks_md.py` actually generates it** | **266** |
| **Released by the consume rule** (the 16 pairs 001–004 already ran) | **−61** |
| **Required** | **205** |
| Budget (raised to 210 at this evaluation) | **210** |
| **Headroom** | **5** |

> ⚠️ **This table read 216 / −47 / 169 until the third pass, and the spec's §4 had already been
> corrected to 224 / −47 / 177 — so the two documents disagreed on the same computation.** That is
> the identical defect to everything else this thesis has found: **a correction applied where it
> was noticed and not propagated to the other place that quotes it.** Both now read the same
> numbers, and both were emitted by script rather than typed.

**And the consume rule is what keeps this NEAR the budget, not what puts it under.** Without
F1's 16 consumed pairs the generator produces **266** against a budget of **210** — **over by 56,
and the only levers left would be pruning rows this spec has twice refused to prune.** *The owner's directive not to repeat work is what makes room
for the two valuation skills the spec was missing.* **That is the opposite of the usual
direction: a budget constraint normally forces work out; here, removing duplicated work is what
lets the missing work in.**

### 🆕 F14 — **The v1.6.0 re-cut's three names were never absorbed into §0 either.** *(Phase 0 — the second pass's largest finding)*

**F1 said the 16 CONSUME pairs are *"cited into §0, never re-run."* That was an assertion the
plan-time pass never checked, and it is 6/16 true.**

Measured against §0's own artifact paths: **only 6 of the 16 consumed pairs could be located in
§0.** Ten could not. And the shape is not random — **`HAWK` appeared ZERO times in the whole of §0
despite having two upstream artifacts, and `PL` appeared twice despite having six.**

**This is F11's twin, and the same root cause.** The v1.6.0 re-cut moved **PL, BKSY and HAWK**
into Tier 2 and completed **neither** place that had to absorb them: their matrix rows carried
**no pillar owner** (F11, open for six days) and **§0 carried no inheritance rows** (F14).
**`plan_audit` passed 4/4 through the entire period** — because I1 asks whether a universe ticker
appears *somewhere* in the matrix, and it did.

**And one of the missing rows changes what a pillar must do.** 006's §2 inherits HAWK as **one**
defect — a `DA-28` share-count candidate with a listing-date guard as the remedy. **002's artifact
says HAWK is *"a DA-28 that MASKS a separate DA-23."*** **Two defects, stacked** — and a guard
against the outer one leaves the inner one untested. **The guard stays; a DA-23 test is added
behind it.**

> ### ✅ FIXED — a new spec §0.6 was written.
> **§0.6 "The v1.6.0 re-cut's three names — and the two places that never absorbed them"** now
> carries **six PL rows and two HAWK rows with their real filed figures** (53.53% gross / −37.06%
> operating; opex at **1.692×** gross profit; **33 of 33** PL operating facts stripped; the
> two-basis cost-of-revenue gap at **32.3%** of the line; hosting-to-launch at **12.5×**; adjusted
> EBITDA **positive** against a GAAP operating loss; the exact-magnitude-opposite-sign signature),
> **plus the explicit note that BKSY's absence is CORRECT and must not be filled** — it has no
> upstream artifacts, so a row would be an invention. **A-9.** The HAWK consequence is carried as
> **A-10** and lands on **P4's checklist.**

### 🆕 F15 — **A malformed cell in a machine-read table is dropped SILENTLY, and I made the same mistake three times in one session.** *(Phase 0 — a tooling gap)*

**The matrix's first column and its ticker list are machine fields.** `parse_matrix` reads a bare
skill slug and comma-separated bare tickers, and **anything it cannot parse it silently omits** —
no warning, no count, no failure. **A bolded list loses its first and last entries:**
`**IRDM, GSAT, SATS**` parses as **`GSAT` alone**; `VSAT, PL, BKSY, HAWK` in bold parses as
`PL, BKSY`.

**Three instances, all mine, all in this session:**

| # | Where | What was silently lost |
|---|---|---|
| 1 | F12's first attempt to add the valuation rows | `**sotp-valuation**` did not resolve as a skill, and both bolded ticker lists lost 2 entries each — **`plan_audit` I2 caught this one** |
| 2 | F12's own fix — I un-bolded those **two** rows and wrote the replacement rows **bolded again** | the same 2-per-list loss, **and nothing caught it**: the matrix simply counted **89 instead of 95** |
| 3 | the new `Deep` row's depth cell, `**Deep**` | harmless to `plan_audit` (it does not filter on depth) but **my own analysis filter skipped the row entirely** |

**The generalisable defect is not the bolding — it is that the parser cannot report what it
dropped.** I4 exists precisely so that *"no row gets the `[P1]` fallback bracket"*; **but a row
whose tickers failed to parse is not a bracket — it is a row that does not exist**, and no
invariant sees it. **Recorded as A-11**, with three supporting cases and **the second one being
the cleanest**: the fix was applied, and the defect reproduced anyway, because **nothing verifies
that a written count equals a parsed count.**

**What the plan does about it now:** the phase table's totals are **computed by script against
§3's parsed matrix**, never carried by hand — and the two numbers it shows (mentions and union)
are both emitted rather than one derived from the other.

### 🆕 F16 — **F1's "the inherited result is" column was written from §0's prose, and six of sixteen did not match the artifact.** *(Phase 0 — the fourth pass, and the deepest of the F1 findings)*

**Every pass has found a different layer of the same defect, and this is the layer underneath the
first three.** F1 built a CONSUME ledger so that 006 would not re-run 16 existing analyses. **The
ledger's premise is a claim about what each artifact contains** — and until this pass, **that
claim had never been checked against a single artifact.**

**Six of the sixteen descriptions do not describe the artifact they point at:**

| Pair | F1 said | The artifact's own title says |
|---|---|---|
| `PL × growth-strategy` | *"the EO test that left this tier"* | **"A Launch Share That Cannot Be Drawn"** — nothing to do with the EO test |
| `IRDM × secular-trends` | *"the D2D read-through"* | **"the platform cannot represent this thesis's question"** — a **negative** result |
| `IRDM × risk` | *"the RKLB gate chain as filed"* | **"P11 deal-security tagging and the falsifier-reachability census"** |
| `IRDM × competitive` | *"the Aireon unconstructibility finding + the licence inventory"* | **"Competitive Position, Q2 2026"** — P11 status and the pre-merger basis |
| `SATS × risk` | *"the deal terms as filed"* | **"Regulatory Risk, Q1 2026"** — why SATS carries the P6 analysis |
| `HAWK × operational-kpi` | *"the KPI series"* | **an Operating-Baseline artifact whose `definitions_used` reads `operating_income UNVERIFIABLE`** |

**Why this is the most consequential F1 finding and not a wording quibble.** A CONSUME ledger's
whole function is to tell a future author **"cite this, do not re-run it."** **Six of its sixteen
rows would have sent that author to an artifact for a figure the artifact does not carry** — and
the failure is silent, because the file exists and the citation resolves. **That is the same shape
as a citation whose page number is plausible but wrong**, which this programme's citation rule was
written about: *"a guessed page number resolves to the wrong page — which is worse than no link,
because it looks correct."*

**And the root cause is that I wrote the column from §0.** Pass 2 found §0 was **incomplete**
(missing PL and HAWK rows entirely); this pass finds that **the descriptions §0 does carry are not
reliable either**. **§0 is a propagation mechanism, and a propagation mechanism built on
paraphrase propagates the paraphrase.**

> ### ✅ FIXED — the column now carries each artifact's OWN TITLE, taken from the file.
> **Not a better paraphrase — the artifact's own heading.** A title cannot drift from the document
> it belongs to, which is the property a CONSUME ledger needs and a paraphrase does not have.
> **A-13.** Note the two rows that are now **more** informative than before: `PL × operational-kpi`
> and `HAWK × operational-kpi` are both *Operating Baseline* artifacts **whose own finding is that
> no trustworthy baseline exists** — which is exactly the kind of thing a consumer must know
> **before** citing them.

### 🆕 F17 — **The budget was MODELLED, not RUN — and three passes "corrected" it on the same wrong model.** *(all phases — the fifth evaluation, and the largest number in this plan)*

**A phase map was missing, and finding that led to the real finding.**

`tools/tasks_md.py` **refuses to run without `phases.yaml`**: `ERROR: no phase map. Pass
--phases or add phases.yaml.` **006 had none — so the thesis could not generate a single task.**
plan.md described a phase table, a dispatch model and a mode-task budget, and **the machine that
turns a plan into work could not read any of it.** (Only 002, 003 and 004 carried a map; 001 and
005–009 did not. `phases.yaml` is now written for 006 — **A-14**.)

**Then the generator was run, and it disagreed with the plan by 89 tasks.**

| | tasks |
|---|---:|
| **`tasks_md` full matrix — RUN** | **266** |
| Released by the consume rule (61 tasks belong to the 16 consumed pairs) | **−61** |
| **Required** | **205** |
| Budget | **180 → 210** |

**The plan said 177. It was wrong by 28 on the requirement and 89 on the full matrix, and the
error has one cause: I computed the mode expansion from the registry instead of running the
tool.**

`agentii_cmd.depth_to_modes` returns **one** mode for an empty `essentials_modes`.
**`tasks_md` gives three** to the four Standard skills that do not declare `methodology` —
`recent-quarter` (`consolidated-p-and-l`, `earnings-vs-consensus`, `margin-analysis`),
`business-model`, `growth-strategy`, `secular-trends` — and **`8×2 + 6×2 + 4×2 + 3×2 = 42`**, which
is exactly the gap between the modelled 224 and the generated 266.

> ### 🔴 THREE ROUNDS "CORRECTED" THIS ARITHMETIC AND EVERY CORRECTION WAS BUILT ON THE SAME WRONG MODEL.
> F13 opened by saying **the budget *"had never been reconciled"***. **It had never been RUN.**
> Round 2 rebuilt the reconciliation, round 3 fixed its stale numbers, and both were arithmetic
> **over a model of the generator rather than over its output.** The corrections were real —
> 79→87→95 was a genuine sequence of fixes — and **all of them were scored against the wrong
> denominator.**
>
> **And the conclusion INVERTS.** The plan said **headroom 3**. The truth is **25 over budget**
> at 180. **A budget that reads "just fits" while being 25 short is worse than one that reads
> "over"**, because the plan's own §4 rule — inherited from 005 — is that *a budget which
> silently truncates an owner-directed scope is the failure mode the budget exists to prevent.*
> **A silent 25-task truncation is exactly that failure, and the plan's arithmetic would have
> concealed it.**

**Fixed at the source:** `max_tasks: 180 → 210`, set from the generator's 266, with 5 tasks of
margin (005's own margin was ~2).

> **✅ AND THE 266 IS CORROBORATED BY A SECOND, INDEPENDENT IMPLEMENTATION.** The sixth pass ran
> **both** generators: the platform's `agentii_cmd.py tasks` and the local `tools/tasks_md.py`
> each emit **exactly 266**. They are separate code paths and neither reads the other. **They
> also disagree on one thing and it is the thing that mattered:** the platform generator emits
> **no phase at all** (0 `## Phase` sections — the same limitation 004's plan recorded), **which
> is precisely why `phases.yaml` was required and why its absence blocked the run.** So the two
> tools agreeing on the count is strong evidence the count is right, **and their differing phase
> handling is why finding it required running them rather than modelling them.** **The spec's §4 and this plan now both carry 266 / −61 / 205.**
**A-14.**

**And running the generator exposed a second defect, in the same family.** The first run emitted
**T904 — a task instructing 006 to publish `_cross/tier1-value-capture-ranking.md`**, which is
**005's artifact.** `tasks_md` reads any backticked `_cross/*.md` token inside §6 as a
*deliverable of this thesis*, and **my §6 cross-reference to 005's artifact** — *"Isomorphic to
005's `_cross/tier1-value-capture-ranking.md`"* — was parsed as one. **The tool already guards
this** (its docstring: *"emitting a task for another thesis's artifact is worse than emitting
none"*) by scoping the scan to §6 — **but a citation inside §6 is still a citation, and the scope
guard cannot tell one from a declaration.** Reworded; the thesis now emits **4** cross-cutting
tasks, all its own. **A-15.**

**The generalisable rule, which the spec now states once:** *where a model and the generator
disagree, the generator's output is the number.* This is the fifth instance of the session's one
defect — **a value computed by hand where the system owning it could have been asked** — and the
first where the hand-computed value **changed a conclusion** rather than a description.

### 🆕 F18 — **⚠️ `tools/gen_tasks_md.py` DESTROYS completion evidence, has no argument parsing, and I ran it by accident.** *(Phase 0 — a workspace hazard, and a disclosure)*

**I ran `python3 tools/gen_tasks_md.py --help` intending to read its interface. It has no
argument parsing at all — zero `argparse` lines — so it did not print help. IT RAN, with a
default target, and OVERWROTE `theses/001-technology-baseline/tasks.md`.**

**What was lost, briefly.** 001 is a **completed** thesis whose `tasks.md` recorded which tasks
were satisfied and by which artifacts. The regeneration converted

```
- [x] T001 [P] [PIL-1] SPCX × operational-kpi × triggers — …  ✅ satisfied by: `2026-09-18_1239_…`
```

into

```
- [ ] T001 [P] [PIL-1] SPCX × operational-kpi × triggers — …
```

**`[x]` became `[ ]` and the `✅ satisfied by:` evidence was stripped — 124 insertions against
157 deletions, and 77 satisfied tasks erased.** That is not a formatting change: it is the
**audit trail** of a finished thesis, and it is the only record that those tasks were verified.

> ### ✅ RESTORED FROM HEAD (`git checkout --`), and 001 verifies clean with all 77 satisfied tasks back.
> **Disclosed because I caused it and because the hazard outlives my mistake.**

**Three properties make this a workspace hazard rather than my slip:**

1. **No argument parsing.** `--help`, `--dry-run`, `--thesis` — none exist. **Any invocation
   executes the write.** A reader cannot ask what the tool does without causing it to do.
2. **Not idempotent.** Running it on a thesis whose tasks are already satisfied **does not
   no-op** — it produces a fresh `[ ]` file and discards the satisfaction state.
3. **It defaults to a thesis rather than requiring one.** Nothing in the invocation named 001.

**⚠️ AND IT IS LIVE FOR THE CONCURRENT SESSION.** Another session is actively running tooling
across **005, 007, 008, 009, 010 and 011** — thirteen files are modified in the working tree
right now, and `tools/clarify_scan.py` and `tools/plan_audit.py` are among them. **Any of those
theses that is complete, and whose `tasks.md` records satisfaction, is one accidental
`gen_tasks_md.py` away from the same loss** — and **005 has now reached the sector-book stage
where tasks begin to be satisfied.** **Recorded as A-16.**

## Constitution Check (second evaluation — the scalar-clearance pass, as promised)

**The first check's note said a second evaluation would run because F1 and F2 *"change what the
plan schedules"*. It has now run, and the evaluation changed more than the plan-time pass did.**

| Requirement | After the evaluation | Verdict |
|---|---|---|
| **P4 — a grade is not a basis** | unchanged | ✅ |
| **P11 — no fundamentals underwrite on a deal security** | unchanged; **and Q-16's extension into the strategy layer is untouched by F12** (the valuation skills run on the seven names P2 values, and IRDM/GSAT are among them **as deal securities valued as spread securities** — see the note below) | ⚠️ **see note** |
| **P9 / F6 — a dateable catalyst inside 180 days** | unchanged | ✅ |
| **F6 — gating assets are not paperwork** | unchanged | ✅ |
| **Risk Framework — caps** | unchanged | ✅ |
| **The membership test** | unchanged | ✅ |
| **Q33 — the pin** | **unchanged, and F3 still stands**: the pin resolves against the constitution's *body*, while its Sync Impact Report and yaml mirror disagree | ⚠️ **F3 open** |
| **Q41 — `PRICE_ACCESS_PREMATURE`** | **SCOPE WIDENED**: three `late` rows now, not one (F2/F12). `get_price_history` is refused in all three | ⚠️ **see F2** |

> **The P11 note, stated precisely because F12 brushes against it.** §1b P2 **does** value IRDM
> and GSAT — it always did, and P2's two-sided claim depends on the scarce-licence group. **What
> P11 forbids is not valuing them; it is underwriting them on fundamentals.** P2 values them **on
> their filed financials and their own disclosed transactions**, and §1b P4 states the deal price
> is a **spread** that 006 does not trade. **What Q-16 forbids — and what F12 does not touch — is
> a buy-side *strategy*** for them. **`sotp-valuation` on IRDM produces an attribution, not an
> idea; `trade-idea-generation` on IRDM would produce an idea and is not declared.** The line is
> between *valuing* and *recommending*, and the matrix now draws it in two places rather than one.

**Second-pass verdict: the plan schedules no work the platform's rules forbid, and the one
constraint that moved (Q41's scope) moved because the evaluation added rows rather than because
the rule was misread.** The plan-time pass's own lesson — from 004's F13, that *both plan passes
evaluated internal consistency and neither asked whether the platform permits the work* — **was
applied here and caught the change.**

---

## Amendments this plan proposes (A-2 applied; A-1, A-3 … A-6 recorded and NOT applied)

| # | Amendment | Why |
|---|---|---|
| **A-1** | **Mark the 16 consumed pairs in §3**, so `tasks_md` does not dispatch them | Otherwise **19% of the matrix re-runs** and produces a second, parallel copy of an existing figure under a different `thesis_id` |
| **A-2** | ✅ **APPLIED** — §6's second "contract gap" is withdrawn in the spec | The contract already validates `DA-23..DA-30`; the stale range is **004's**, not this thesis's (F4). **Left unapplied it would have suppressed a `definitions_used` declaration P2 is entitled to make** |
| **A-3** | **Correct `constitution.yaml`'s attestation and add the 1.6.0 Sync Impact Report** | Three places record the version; two disagree (F3). **Owner: the constitution, not this thesis** |
| **A-4** | **PATCH 005's header** — it calls 006 wave-2 and mislabels 008 and 009 | Contradicts PROGRAM.md §3 and 006's own declaration (Q-11, Q-18) |
| **A-5** | **Build `I5`** (stage vs registry) and **`I6`** (formability) | Two demonstrated cases each, and no tool catches either (F8) |
| **A-6** | ✅ **APPLIED** — P1, P2 and P3's `Subscribed` lines extended to claim all 16 unowned pairs | **15 of the 16 belonged to PL, BKSY and HAWK** — the three names added at the v1.6.0 re-cut, whose rows were written without any pillar claiming them. **I4 passed while 16 rows got the `[P1]` fallback bracket its own text says it prevents** (F11). `plan_audit` now reports **0 unowned** |
| **A-7** | ✅ **APPLIED** — §3 gains **`sotp-valuation`** and **`residual-income`**, both `late`, on the seven names P2 values; §4's budget note is corrected from the never-computed **"79"** — and then from a **"87"** whose own components summed to 99 — to **95**, emitted by `plan_audit` rather than typed, with the full mode reconciliation | **006 declared no valuation skill while its P2 deliverable was a valuation** (F12), and its budget had never been reconciled (F13) |
| **A-8** | **Extend I4 to check PAIRS, not skills** | A-6 fixed this instance by adding rows; **the invariant is still under-strict**, so the next re-cut reproduces it. 004 recorded the same shape for **I1** — *"it checks a universe ticker appears somewhere"* — **so two of the four invariants pass while their own stated purpose fails** (F11) |
| **A-9** | ✅ **APPLIED** — spec **§0.6** written, with six PL rows and two HAWK rows at their real filed figures, plus the explicit note that **BKSY's absence is correct** | **10 of the 16 CONSUME pairs had no §0 home**, and §0 is the propagation mechanism 002 says a downstream thesis must not bypass. `HAWK` appeared **zero times** in §0 despite two upstream artifacts (F14) |
| **A-10** | **P4's HAWK checklist carries BOTH defects** — the listing-date guard **and** a DA-23 test behind it | 002: *"HAWK is a DA-28 that **masks a separate DA-23**."* §2 inherits only the DA-28, so the guard would suppress the false-positive **and leave the sign strip untested** (F14) |
| **A-12** | ✅ **APPLIED** — §4's reconciliation is **emitted by script**, and a stated total must equal the sum printed beside it | **§4's total was wrong three times** — *"79"* (never computed), then *"87"* whose **own components summed to 99**, while the real matrix was 95 — **and the plan's F13 table quoted a different set again (216/169 vs the spec's 224/177)**. A total that disagrees with the sum beneath it is worse than no total: a reader who adds the parts cannot tell which side to trust (third-pass finding) |
| **A-13** | ✅ **APPLIED** — F1's description column carries each artifact's **own title**, not a paraphrase | **Six of sixteen paraphrases did not match the artifact** (F16), and a CONSUME ledger that misdescribes what it consumes is worse than none: the citation resolves, so the failure is silent. **The root cause is that the column was written from §0's prose — and §0's own descriptions are not reliable** |
| **A-14** | ✅ **APPLIED — `phases.yaml` written, and the budget set from the generator** | **`tasks_md` refuses to run without a phase map, and 006 had none** — the thesis could not generate a single task. Running it produced **266**, not the modelled 224, **without a phase map. Writing it was not a formality; it was what exposed F17.** `max_tasks` 180 → 210 |
| **A-15** | ✅ **APPLIED** — §6's cross-reference to 005's artifact is reworded so it is not a backticked `_cross/*.md` token | **It emitted T904, instructing 006 to publish 005's artifact.** The tool scopes its scan to §6 to prevent exactly this, **but a citation inside §6 is indistinguishable from a declaration to a regex.** `cross_tasks` should exclude an artifact whose name is attributed to another thesis — or the scope should be a bullet list, not a section |
| **A-16** | **`gen_tasks_md.py` needs `argparse` and an idempotence guard** — and a completion-state check before it writes | **It has zero argument handling, so `--help` executes a write**; it overwrites `tasks.md` without preserving `[x]` / `✅ satisfied by:` state; and it defaults to a thesis nobody named. **It erased 77 satisfied tasks from completed 001 in one invocation** (F18, restored). **005 is at the stage where its own tasks begin to be satisfied** |
| **A-11** | **`parse_matrix` should REPORT what it dropped** — an unparseable skill or ticker cell must fail loudly, not vanish | **Three instances in one session, all mine**, and **the second reproduced inside the very fix for the first**: a bolded cell undercounts the matrix (89 vs 95) with no warning, and no invariant sees a row that failed to parse (F15) |

---

## What upstream supplies — consume, do not re-derive

**The full inventory is spec §0, and it is already a propagation mechanism rather than a
courtesy.** The plan adds only the routing rule:

| From | Consumed as | Never |
|---|---|---|
| **001** | the panorama — quantities, the L-band scarcity finding, the sequential-gate identity | re-derived |
| **002** | the validated input set **with its verdicts and their kinds** (`UNEXERCISED` ≠ `CLEAN`) | re-opened, or its denominators and physics recomputed |
| **003** | the value-pool map and the **corrected** operator margin ladder | re-mapped, or the cross-issuer margin test re-run |
| **004** | the Connectivity figures and the **`MODELED` regime — as a benchmark, inside its boundary** | used to import a satellite peer multiple (partition admits **0 of 11**) |
| **005** | RKLB's financing facts — the bridge and the consideration mix | used to underwrite RKLB's runway or model a combined entity |

**And the one-way rule from §5b, restated because it is the failure this plan most needs to
prevent:** *a cross-tier question answered here without a citation back to its owner* is the
failure mode that section exists to stop — and it is the same failure the constitution records
as the reason **005 was itself re-cut.**
