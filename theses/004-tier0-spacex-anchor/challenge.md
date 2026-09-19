---
thesis_id: "004-tier0-spacex-anchor"
challenged_at: 2026-09-19T15:40:00Z
constitution_pin: "1.5.0"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
method: [cross_run_contradiction, pre_mortem, inversion, wrong_if_falsifiability]
findings_raised: 12
findings_high: 4
findings_medium: 6
findings_low: 2
scope: "thesis-complete — all 23 artifacts, incremental backstop: thesis complete is a lifecycle hook"
---

# Challenge — SPCX anchor (004)

**The buyer-side IC verb.** Not an audit: this assumes the thesis is **wrong** and tries to find
where. Four angles, per the skill's method bodies. **Finding IDs are content-derived**
(`sha256(entity|metric|period|gap_type)[:12]`), so an unchanged re-run reproduces them byte-identically.

**Headline: the anchor's ARITHMETIC survives every angle. Its `entity_claims` SCHEMA does not, and
the failure silently disarms the two checks that consume it.**

---

## 🔴 HIGH

### `cbafa3f26a56` — `entity_claims` names the entity `ticker`; every consumer reads `entity`

**Angle 1 (cross-run contradiction) — found by running it, not by reading the schema.**

```
build_entity_index(artifacts_root) →
  entity='None'  metric='customer_launch_share'  period='2026Q2'  vals=[0.218, 0.263]
  ...and 6 more, ALL with entity='None'
```

**Root cause, verified in both consumers:** `reduce_journals.build_entity_index` and
`g1_gate._check_claims` both read `claim.get("entity")`. **`entities.md` — which I authored —
specifies `ticker`.** Neither reads `ticker`, so **every claim in all 23 artifacts is attributed to
the literal string `"None"`.**

**Why HIGH:** the entity index's entire purpose is `(entity, metric, period)` grouping. With
`entity` uniformly `"None"`, **every claim in the thesis collapses into one namespace**, and a
contradiction can never be attributed to a company. **The anchor is the programme's most-cited
artifact; a knowledge-base entry built from it is unaddressable.**

**The aggravating detail:** `g1_gate`'s own LOOKAHEAD message prints `claim.get('entity')` — so
**the check I made live last round reports `claim None.metric`**. Fixing `period` made the check
*fire*; leaving `entity` makes its output *useless*.

### `49ae5b9fe05a` — no `retrieved_at`, so every conflict is a "true contradiction"

`build_entity_index` classifies by `times = {r["retrieved_at"] for r in rows}`:
**equal → true contradiction; different → suspected restatement.**

**My claims carry no `retrieved_at`.** So `times = {None}`, `len(times) == 1`, and:

```
contradictions: 7        suspected_restatements: 0
```

**⇒ Seven findings would reach the IC agenda as mechanical TRUE CONTRADICTIONS, when at most ONE
is real** (see `8f7be6a9f98b`). Six are artefacts of coarse metric names — the same `metric` string
covering different populations.

**Why HIGH:** the skill says *"The validator never auto-resolves — candidates go to the IC agenda."*
**Six spurious high-confidence contradictions is worse than none**, because the agenda's scarce
attention is spent on them and the real one is buried among them.

> **Both fields are in the same file, and I fixed a third there last round.** Round 4 of implement
> corrected `period_basis → period` after checking that one field against its consumer. **I did not
> check the other two.** The lesson is not "check fields" — it is **check EVERY field a consumer
> reads, or say you checked one.**

### `c35c87cdb516` — the 313× attributes the WHOLE market cap to ONE segment

**Angle 3 (inversion).** The headline divides the entire market capitalisation by Connectivity's
annualised operating income. **That arithmetic implicitly sets Space and AI to zero.**

**I tested the inversion, and it fails:** even granting the two loss-making segments **$1.5T**,
Connectivity still carries **86×**. **So the conclusion holds — but the framing must not be read as
"Connectivity is worth 313× income."** The artifact says this in §3 of `reverse-dcf`; **it should say
it in the anchor too, and the anchor's §3 does.** *Finding recorded as CLOSED-BY-EXISTING-TEXT with
the location named, per the skill's rule that a resolved candidate is not silently dropped.*

### `ca6db022e97e` — the constitution's ~$1.62T anchor does not reconcile

`$1.62T ÷ 13,176,000,000 = $122.95/share`. **The IPO priced at $135.00.** So the anchor and the IPO
do not reconcile on the filed share count, and **the anchor's own basis is not in this workspace.**

**Why HIGH:** 004 is the **anchor**. Every downstream thesis comparing itself to a market reference
inherits this. **And round 4's *"+13.1%"* measured the live price against the IPO price — not
against the anchor.** The published figure was wrong by ~15 pp.

---

## 🟠 MEDIUM

### `8f7be6a9f98b` · `ace81611628f` — the `period` field cannot express DA-26 durations

**The real contradiction the index found.** `customer_launch_share` at `2026Q2` = **0.218 and
0.263**; `segment_revenue` at `2026Q2` = **4,291 and 7,548**. **These are 3M and 6M figures sharing
one label.**

**Cause, and it is a two-gate conflict I created:** `g1_gate._PERIOD_RE` is `^(\d{4})Q([1-4])$`, so
`period` **must** be a bare `YYYYQN`. **A bare `YYYYQN` cannot say which duration.** I moved the
duration into `basis` — **free text the index does not read.**

> **DA-26 exists precisely to forbid this collapse, and my fix for one gate reintroduced it in the
> form the other gate cannot see.**

**Recommended remedy:** add a `duration` field to `entity_claims` and key the index on
`(entity, metric, period, duration)`. **Not applied** — it is a schema change affecting every
thesis, and it belongs in a workspace amendment rather than a silent local edit.

### `2083bfe7adee` — the annualisation takes the STRONGEST quarter × 4

**Angle 2 (pre-mortem).** `D-1` annualises `3M × 4`. Checked against the filed half-year:
Connectivity **H1 7,548 − Q2 4,291 = Q1 3,257**, so **Q2 is 31.7% above Q1**. `Q2 × 4 = 17,164`
against an H1-average `3,774 × 4 = 15,096` — **13.7% higher.**

**Direction of the error:** a smaller denominator makes the **313× larger** (≈355× on an H1-average
basis). **So the annualisation is CONSERVATIVE, and the finding strengthens rather than weakens.**

**Recorded because it was not stated.** `D-1` justified `×4` against the 6M alternative but **never
checked whether Q2 was representative of the half.** An artifact that chose the strongest quarter
without saying so, in a thesis whose whole method is basis discipline, is the exact defect it
polices.

### `29a34dbb9025` — Connectivity is a SINGLE POINT OF FAILURE for the anchor

**Angle 2.** The 313× rests entirely on one segment being the only profitable one. **Pre-mortem:
which pillar failed first? P2** — and if Connectivity's margin is a mix-shift artefact rather than
operating leverage, **the anchor has no positive-value segment at all.**

**Mitigation already in place:** P2's falsifier is live and checkable, and the **T-1** trigger names
the exact datum. **But the concentration is not stated as a risk in the anchor.** It should be.

### `1a3fbe01279d` — P3's falsifier is not mechanically checkable

**Angle 4.** `count_of_admissible_ai_segment_valuation_framings_derivable_from_filed_or_peer_data
< 1`. **"Admissible framing" is a judgement, not a metric.** Two analysts can disagree on the count
while agreeing on every fact. **Per Q8-4, a prose falsifier is not a falsifier — and this is prose
wearing a metric's clothes.**

### `df5f41952e14` — P4's ex-R&D numerator is a CONSTRUCTION

**Angle 4.** `space_segment_operating_margin_ex_RD_pct` — the filing does **not** separate Starship
from Falcon R&D, so the ex-R&D numerator is **`MODELED`**. The falsifier can therefore fire on the
**construction**, not on the business. **P4's own text says this; the `wrong_if` does not.**

### `522b9d0fc803` — P6's falsifier tests the thesis's OWN output

**Angle 4.** `count_of_published_segment_anchors_without_a_stated_comparability_boundary = 0`,
`source=004_anchor_table`. **It can only be evaluated after publication, and it tests the artifact
by the standard the artifact sets.** That is a consistency check, not a falsifier.

### `df5f41952e14` *(second instance)* — the falsifier count is inconsistent across artifacts

`revenue-decomp/triggers` reports **6**; `sotp-valuation/triggers` reports **7**. **Both are
correct** — they count different sets — but the shared metric name `falsifier_count` makes them read
as a contradiction. **Same coarse-metric failure as `49ae5b9fe05a`.**

---

## 🟡 LOW

### `6cc8ca365f95` — the `get_segment_data` workaround is a local fix to a platform defect

004 routes around it to `search_xbrl_facts(view=detailed)`, and records the routing in **its own**
artifacts. **003 recorded the breakage first.** But **the fix is per-thesis, and the next caller —
008 or 009 — will rediscover it.** *A workaround repeated per-thesis is not a fix.*

### The `\$` escape and the dropped `$2M` term

Both were caught by G1 and by running the arithmetic, and both are **already recorded in the
artifacts they occurred in**. **Not re-raised here** — the skill's scope is the thesis's claims, not
its authoring incidents. **Named once so the pattern is on the record: three of this thesis's four
self-caught errors were in the FRONTMATTER, not the analysis.**

---

## What the challenge did NOT find

**Angle 3 (inversion), run against the thesis's own conclusion:**

| Inversion | Tested | Result |
|---|---|---|
| *"The 313× is an attribution artefact"* | Recompute with Space+AI at $0.5T / $1.0T / $1.5T | **86× at the most generous — holds** |
| *"Connectivity's margin is a mix-shift artefact"* | Operating leverage **+79.4% income on +65.8% revenue**; margin **rising** while ARPU falls | **Holds; the falsifier is live (T-1)** |
| *"The annualisation flatters the multiple"* | Q2 is the **strongest** quarter | **Error is conservative** (`2083bfe7adee`) |
| *"DA-23 corrupts the segment table"* | Component identity closes on all three rows and at consolidation | **Holds** |
| *"The comparability partition is a search failure"* | Three segments fail for **three different reasons** | **Holds** |

**The arithmetic and the reachability of the falsifiers survive.** **What does not survive is the
claim schema — and it fails in the one way this programme keeps finding: a plausible field name that
means nothing to the consumer.**

---

## Disposition

| ID | Severity | Status |
|---|---|---|
| `cbafa3f26a56` | 🔴 HIGH | **OPEN — blocks knowledge-base entry (Q64)** |
| `49ae5b9fe05a` | 🔴 HIGH | **OPEN — blocks knowledge-base entry (Q64)** |
| `c35c87cdb516` | 🔴 HIGH | **CLOSED BY EXISTING TEXT** — `anchor-sotp.md` §3, `reverse-dcf` §3 |
| `ca6db022e97e` | 🔴 HIGH | **OPEN** — named for every downstream consumer |
| `8f7be6a9f98b` · `ace81611628f` | 🟠 MED | **OPEN** — needs a schema field, not a local edit |
| `2083bfe7adee` | 🟠 MED | **RECORDED** — direction stated; strengthens |
| `29a34dbb9025` | 🟠 MED | **OPEN** — anchor should state the concentration |
| `1a3fbe01279d` · `df5f41952e14` · `522b9d0fc803` | 🟠 MED | **OPEN** — spec-level falsifier defects |
| `6cc8ca365f95` · falsifier-count | 🟡 LOW | **RECORDED** |

> **Per Q64, `cbafa3f26a56` and `49ae5b9fe05a` mean the anchor's claims CANNOT ENTER THE KNOWLEDGE
> BASE as they stand.** They are two field names, both in a file I wrote, both with a consumer that
> reads something else — **and the second one silently converts every ambiguity into certainty.**
