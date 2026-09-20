---
thesis_id: "006-constellation-operators"
challenged_at: 2026-09-20T17:30:00Z
constitution_pin: "1.6.0"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
method: [cross_run_contradiction, pre_mortem, inversion, wrong_if_falsifiability]
findings_raised: 12
findings_high: 4
findings_medium: 4
findings_low: 4
scope: "pillar-complete (PIL-1 partial — 10 of 270 tasks landed) plus a thesis-level schema sweep; the entity index was run over the whole corpus, not just 006"
---

# Challenge — Constellation operators (006)

**The buyer-side IC verb.** Not an audit: this assumes the thesis is **wrong** and tries to find
where. Four angles, per the skill's method bodies. **Finding IDs are content-derived**
(`sha256(entity|metric|period|gap_type)[:12]`), so an unchanged re-run reproduces them
byte-identically.

**Headline: 006 is the first thesis where the contradiction gate FABRICATES findings rather than
merely reporting them wrongly. The gate returns 3 HIGH-severity contradictions against this
thesis. The true count is ZERO, and I verified that by running the index with the field name the
corpus actually uses.**

**The mechanism is a schema declared twice and never reconciled:** `entities.md` in 001 says
`entity:` and the tool reads that; `entities.md` in 002, 003 and **004 (the newest) says `ticker:`**
and every real artifact writes that. **The tool is consistent with a superseded declaration.**
Neither party is internally wrong — the repository just never picked one.**

**And the reason it surfaced here is uncomfortable: the defect is triggered by metric names
matching across names — i.e. by exactly the naming discipline the schema asks for.**

---

## 🔴 HIGH

### `7eb9ef0ef94b` — the contradiction gate reports 3 HIGH findings at 006, and all 3 are false

**Angle 1 (cross-run contradiction) — found by running it, and confirmed by running it twice.**

The gate returns:

```
- [high] None.total_revenue@2026Q2       values=[64772000.0, 225237000.0]
- [high] None.operating_income@2026Q2    values=[-4775000.0, 34008000.0]
- [high] None.transaction_costs@2026Q2   values=[10400000.0, 14300000.0]
```

**Those are GSAT's and IRDM's figures for the same metric and quarter. They are not
contradictions — they are two different companies.** The gate has grouped them because the entity
is the string `"None"`.

**Root cause, one line — `reduce_journals.py:82`:**

```python
key = (str(claim.get("entity")), str(claim.get("metric")), str(claim.get("period")))
```

**The artifacts write `ticker:`. The consumer reads `entity:`.**
`claim.get("entity")` returns `None`; `str(None)` is `"None"`; **every claim from every name in
every thesis is grouped under one entity called `None`.**

> ### ⚠️ AND THE CORRECT FRAMING IS NOT "THE TOOL HAS A BUG" — IT IS "TWO SCHEMAS CONFLICT, AND THE TOOL FOLLOWS THE SUPERSEDED ONE"
>
> **Every thesis declares its own `entity_claims` schema in `entities.md`, and they disagree.**
> **I checked all four:**
>
> | Thesis | `entities.md` mtime | Field declared | Declares `retrieved_at`? |
> |---|---|---|---|
> | **001** | 2026-09-18 | **`entity:`** | **yes** |
> | **002** | 2026-09-18 | **`ticker:`** | no |
> | **003** | 2026-09-18 | **`ticker:`** | no |
> | **004** | **2026-09-19** — *newest* | **`ticker:`** | **yes** |
>
> **So `entity:` is 001's convention and nothing else's.** **002, 003 and 004 all declare
> `ticker:`, and 004 — the most recent declaration in the repository — declares `ticker:` AND
> `retrieved_at` together.**
>
> **The tool matches 001 on the field name and 001 on `retrieved_at`.** **The corpus follows 004.**
> **The tool is therefore consistent with a superseded declaration and inconsistent with the
> current one on BOTH fields** — which is a materially different and more defensible finding than
> a defect in either party. **Neither the tool nor the artifacts is internally wrong; the
> repository declares the schema twice and never reconciled them.**
>
> **And the confirming evidence is that every real artifact follows 004**: 45 claims across 004,
> 7 across 006, and the YSS claims in 005 — **all `ticker:`.** The single place the tool's
> convention appears in executable form is its own unit-test fixture
> (`tests/test_s5_contradiction.py`, using `entity: NVDA`), **which is why the test passes while
> the tool has never worked on real data.**

**I proved the count difference by running the index under both keys:**

| Key field | 006 contradictions |
|---|---:|
| `ticker` (**what the corpus writes**) | **0** |
| `entity` (**what the tool reads**) | **3** |

**Why HIGH:** the skill's own text says *"**The validator never auto-resolves** — candidates go to
the IC agenda."* **Three fabricated high-confidence contradictions are worse than none**, because
the agenda's scarce attention is spent disproving something that was never true. **A reader who
trusted this output would conclude 006's two most complete artifacts disagree about revenue, when
they are about different companies.**

> ### ⚠️ THIS IS 004's FINDING, UNFIXED, AND NOW MEASURABLY WORSE
> **004's challenge already recorded it as its own HIGH finding `cbafa3f26a56`** — *"`entity_claims`
> names the entity `ticker`; every consumer reads `entity`"* — and noted the aggravating detail
> that `g1_gate`'s LOOKAHEAD message prints `claim.get('entity')` too. **That was 2026-09-19.**
> **It is still present on 2026-09-20, and 006 is the thesis that pays for it.**
>
> **What is new here is not the defect — it is the blast radius, and the masking that hid it.**
> **004's false count (7) happened to EQUAL its true count (7)**, because 004's claims are
> overwhelmingly SPCX-keyed, so grouping them under `"None"` changes the grouping only for the
> handful of RKLB and FLY claims — **and those used distinctive metric names
> (`mse-rklb-inventory-drawdown-periods`), so they never collided.** **The bug was invisible at
> the one thesis that exercised the feature most.**
>
> **006's artifacts use canonical metric names** — `total_revenue`, `operating_income`,
> `transaction_costs` — **because the schema asks for a shared vocabulary.** Two names × the same
> canonical metric × the same period **is precisely the condition that produces a false
> contradiction.** **The defect therefore punishes the naming discipline the schema rewards**, and
> it will fire on every multi-name thesis from here on.

### `2974e741ae8a` — fixing the field name does NOT fix the gate: the key has no dimension

**Angle 1, second order — and this one is new.**

**Fixing `entity` → `ticker` corrects 006 (3 → 0). It does not correct 004.** I ran 004 under the
right key and **its 7 contradictions remain 7**:

```
SPCX.segment_revenue@2026Q2          = [4291000000.0, 7548000000.0]
SPCX.segment_product_revenue@2026Q2  = [603000000, 710000000, 978000000, 1806000000,
                                        2485000000, 2669000000, 2915000000, 4633000000]
SPCX.consolidated_revenue_by_nature@2026Q2 = [841000000.0, 11667000000.0]
SPCX.falsifier_count@2026Q2          = [6.0, 7.0]
```

**`segment_revenue` with two values is Space and Connectivity — the two SEGMENTS.** They are not
in conflict; **the metric name simply omits which segment**, and the key `(entity, metric, period)`
has **no dimension component to separate them.** Same for the eight product-level revenues, and
`falsifier_count` is two *pillars'* counts.

**Why HIGH:** the skill's stated purpose for this gate is *"same `(entity, metric, period)` with
different values"*. **But a metric that is inherently dimensional — segment revenue, product
revenue, per-scenario assumption — has a *legitimate* multiplicity at that key.** The gate has no
way to distinguish **two segments disagreeing** from **one fact asserted twice with different
values**, and **it reports both as HIGH contradictions.** **At 004, all 7 are the first kind.**

**Recommended remedy:** add a `dimension` (or `basis`) field to `entity_claims` and include it in
the key — the same remedy 004's `8f7be6a9f98b` recommended for `duration`, applied to the axis
that actually produced 004's false positives. **Neither field exists today**, and 006's
DA-register already requires a *basis* on every figure, so the corpus convention and the gate's
key would converge rather than diverge.

### `ef0dd4b7c7e5` — P3's and P5's falsifiers carry the circularity Q-22 fixed at P6, and were not fixed

**Angle 4 (`wrong_if` falsifiability).**

**Q-22 repaired P6's falsifier** because it could be satisfied *"by our own prior recording"*: it
counted names lacking a strategy **"or a recorded finding of none"**, and the second clause
absorbed IRDM and GSAT **by construction**. The fix required the recorded finding to **name its
class** (`P11_FORBIDS_UNDERWRITING` / `NO_DATEABLE_CATALYST` / `NOT_READY`), so *"none because P11
forbids it"* became distinguishable from *"none because we could not find one."*

**P3 and P5 have the identical structure and were left alone:**

| Pillar | Falsifier | Threshold | Fires on |
|---|---|---:|---|
| **P3** | `count_of_tier2_names_not_placeable_on_the_licence_service_axis_by_the_P2_attribution_rule` | `0`, `op=>` | a count **the thesis produces** |
| **P5** | `count_of_tier2_contested_figures_unclassified_or_without_a_named_resolving_source` | `0`, `op=>` | a count **the thesis produces** |

**P3 is circular through P2.** *"Placeable by the P2 attribution rule"* — **and the rule is this
thesis's own work.** A permissive enough rule places every name, the count is 0, and the falsifier
is quiet. **Nothing requires a placement to be evidenced, or a non-placement to be recorded with a
class.**

**P5 is circular through the definition of "contested."** The count falls if the thesis **contests
fewer figures.** **A figure the thesis never raises is not counted as unclassified** — so
**omission and resolution are indistinguishable**, which is exactly the defect Q-22 named.

**Why HIGH:** **this is the fourth instance of a partial sweep in this thesis's lifetime.** Q-19
corrected `position-sizing` and missed `ratio-analysis` in the same table; Q-12's answer was
correct on a premise Q-15 voided; §4's budget note needed correcting twice; and now Q-22 fixed one
pillar's circularity and left two identical ones in place. **The pattern is not carelessness in any
single instance — it is that fixes are applied to the site where the defect was noticed rather than
swept across the class.**

**Recommended remedy:** apply Q-22's class requirement to P3 and P5. P5's is the more urgent
because its subject — contested figures — is the input 011 sizes against, and **a self-suppressing
count there propagates a number into a position size.**

### `ba2fe9ce8ef8` — the finding ID is derived from a field that is always `"None"`, so it collides across entities

**Angle 1, third order — and it is the one with the longest life.**

`finding_id.finding_id(entity, metric, period, gap_type)` hashes
`"|".join([entity, metric, period, gap_type])`. **Its stated purpose, in its own docstring:** *"an
unchanged re-run produces byte-identical IDs, which is what makes the eval corpus aggregatable
across runs."*

**But `entity` is the literal string `"None"` for every claim in the repository.** So:

1. **IDs collide across companies.** I confirmed the exact value the tool emitted —
   `d4efa10fbd03` for `None.total_revenue@2026Q2` — by recomputing it. **If IRDM alone had
   contradicted itself on `total_revenue` at `2026Q2`, it would receive the SAME id**, because the
   entity never enters the seed as anything but `"None"`. **Two findings about two different
   companies are indistinguishable by ID** — which is the one property the ID exists to provide.

2. **Every ID changes when the bug is fixed.** The moment `entity` is read from `ticker`, the seed
   changes and **`d4efa10fbd03` ceases to exist.** So the eval corpus **cannot be aggregated across
   the fix**: the same finding, before and after, has different IDs, and **the "byte-identical
   re-run" guarantee does not survive the correction it is most needed for.**

**Why HIGH:** the ID scheme is the mechanism that makes challenge runs comparable. **A content
hash whose content is a constant is not content-derived**, and the migration cost is now
irreversible — 004's twelve recorded IDs are already invalid, and 006's twelve are about to be.

---

## 🟠 MEDIUM

### `5b2633309f03` — P1's falsifier passes at 50.5% against a 0.5 bar, and CANNOT FIRE in the direction of the claim's own risk

**Angle 4, with the implement round's measurements.** From
`artifacts/IRDM/…_unit-economics_methodology.md` and `…_triggers.md`:

**P1's measured value is `50.5%` against `threshold=0.5`, `op=<` — a half-point pass** — and the
value is bounded to `[50.5%, 64.6%]` across every attribution of IRDM's undisclosed
cost-of-services split. **So the falsifier is mechanically checkable and robustly passing.**

**But the trigger sweep showed the pass is robust for the wrong reason.** Of six triggers:
**T-1 is arithmetically closed; T-3, T-4 and T-5 all move the share AWAY from 0.5; T-2 is a clock;
only T-6 can change the verdict, and only by removing the figure entirely.** Concretely: if IRDM's
licensed `Services` line had been **flat instead of +5,758**, the share rises to **85.9%** —
*further* from firing.

**So a WEAKER licensed line STRENGTHENS the pass.** **P1 cannot be refuted by the licensed line
doing badly** — only by it doing impossibly well.

**Why MEDIUM and not HIGH:** the claim is not contradicted, and the arithmetic is sound. **The
finding is that a falsifier which cannot fire in the direction of its claim's own risk should be
reported as `UNEXERCISED`, not as a pass** — which is the thesis's own §0.2 rule (*"a check that
closes cleanly while testing nothing"*). **Recorded for P5's queue close-out rather than resolved.**

### `0b6dc33c7790` — no `retrieved_at`, so no conflict can ever be classed a suspected restatement

**Angle 1.** The skill's rule: *"Same `retrieved_at` → true contradiction; different → suspected
restatement."*

**This is 004's finding `49ae5b9fe05a`, unfixed — and unlike finding `7eb9ef0ef94b`, it is
PLURAL: the tool omits the field and so do I.**

**004's `entities.md` — the newest schema declaration in the repository — requires it:**
`retrieved_at: <ISO 8601>   # OUR fetch time — Q71: the two are never conflated`, and 004's own
prose is emphatic that `observed_at` and `retrieved_at` are separate fields *"never conflated."*

**The tool reads it and finds nothing**, so `times = {None}`, `len(times) == 1`, and **every**
conflict routes to `contradictions`. **The `suspected_restatements` bucket is structurally
unreachable for any thesis in this repository.**

> ### ⚠️ AND 006 IS IN BREACH OF THE SAME CLAUSE
> **My seven claims carry no `retrieved_at` either.** So this finding is not only *"the gate cannot
> classify"* — **it is *"the artifacts give it nothing to classify with,"* and that part is mine.**
>
> **The 001 schema and the 004 schema agree that `retrieved_at` is required; only the artifacts
> omit it.** So the correct reading of BOTH findings is the same: **the repository has a single
> written schema, declared twice, requiring both `ticker` and `retrieved_at` — the tool honors
> `entity` and `retrieved_at`, the artifacts honor `ticker` alone, and nobody honors the whole
> thing.**

**Why MEDIUM:** given finding `7eb9ef0ef94b` the bucket is currently fed false positives anyway, so
the practical harm is bounded today. **But it must be fixed *with* the field-name bug rather than
after, or the restored gate will classify every genuine restatement as a contradiction — and
`retrieved_at` is the only field that can tell them apart.**

**Concretely for my artifacts: all 7 claims need `retrieved_at`, and none has it.** Carried into
P5's queue close-out as a **remediation owed by this thesis**, not only by the platform.

### `ad355eeb2e0f` — `structured_only` binds 75 of this thesis's 270 tasks to the retrieval path its own register refuses

**Angles 2 and 4, from the implement round.**

`unit-economics` declares `retrieval_scope: structured_only` and its `allowed_tools` **excludes**
`read_source_pages` — §1 is explicit: *"Document-retrieval tools are excluded from
`allowed_tools`."* **But the thesis's register documents the served block as inadmissible** (DA-30:
8 of 8 IRDM served margins divide by the Aireon hosting **ceiling**; DA-29: a back-solve signature
on served `operating_income`; and at GSAT a served `+4,775,000` against a filed `(4,775)`).

**There is no deviation mechanism anywhere** — not in `retrieval.md` (its only escalation is
*within* document retrieval), not in `sharp-edges.yaml`, not in the frontmatter schema. **The
contract suite offers *run as declared* or *do not run*, and no way to record *run on a different
basis, and say so*.**

**Scale:** 6 of 006's 18 skills are `structured_only`, carrying **75 of 270 tasks (27.8%)**.
Library-wide **36 of 72 skills — exactly 50.0%.** **And the registry is internally consistent
(0 skills both declare it and retain document retrieval), so this is not a registry bug: the
registry is coherent, the register is coherent, and they contradict each other.**

**Why MEDIUM:** each affected artifact can declare a `scope_deviation` block, and mine do — a field
the implement round invented, **proposed rather than ratified.** **It is MEDIUM only because a
workaround exists; the governance gap is HIGH-shaped** and belongs to the constitution rather than
to this thesis.

### `6a1aa9d72e24` — GSAT's ex-deal-cost margin straddles zero, and the reading rests on a WORD

**Angle 3 (inversion) — the GSAT leg is weaker than its headline.**

GSAT's reported operating swing is **−16.52 points**. On the issuer's disclosure — legal and
professional fees **`+10,400`**, *"due primarily to transaction costs related to the Mergers"* —
the ex-deal-cost margin is **`+8.68%`**. **But `8.68%` is a LOWER bound: "primarily" is not a
number.**

The break-even is **`s = 4,775 / 10,400 = 45.9%`** where `s` is the deal-cost share of the fee
increase. **So the interval the filing supports is `[−7.37%, +8.68%]`, and it straddles zero.**

**Why MEDIUM:** if *"primarily"* means what it ordinarily means (>50%), **GSAT's ex-deal-cost
quarter is profitable and the entire reported loss is deal cost** — the thesis's reading. **But the
filing does not settle it, and three of six triggers can move it** — against IRDM, where none
could. **Recorded so the sector book does not present `8.68%` as a result rather than as a bound.**

---

## 🟡 LOW

### `754168e7ee55` — pre-mortem: the thesis's evidence base is being removed by the event the thesis is about

**Angle 2.** Assume the thesis is judged wrong in 2027 and reconstruct backwards. **The first
failure is not analytical.**

**IRDM and GSAT are both deal securities** (RKLB/Aireon; AMZN at $90.00/sh). **If both close, the
licence layer is held entirely privately and the tier has no listed expression** — §2's
empty-result path, which the thesis pre-declares (and which discharges CHK003). **But the
pre-declaration is a disposition, not a hedge:** 2 of 8 names leave, **and they are two of the four
carrying actual filed evidence.**

**Recorded as LOW because it is disclosed and dispositioned rather than missed** — and because
§2 already specifies the conversion (a holdings-level read-through in `_cross/`, attribution
register retained for 007 and 011). **It is listed so that the disposition is visibly a choice.**

### `2a5cec3713fc` — pre-mortem: P2's attribution rests on ONE transaction mark

**Angle 2.** P2's falsifier sources
`SPCX_EchoStar_transaction_mark_issuer_filed_operating_financials_and_filed_licence_carrying_values`.
**The tier-wide attribution of EV to the licensed asset is anchored on a single transaction mark**
— and **P3 depends on P2's rule, and P6 on both.** **If that mark is unrepresentative** (a
distressed seller, a strategic buyer, a licence-specific premium), **the error propagates to every
downstream pillar at once.**

**Not yet actionable** — P2 has not run. **Recorded so that when it does, the mark's
representativeness is tested explicitly rather than inherited as an input.**

### `ab8c7406b273` — inversion: D2D inverts the scarcity premise from INSIDE the universe

**Angle 3.** The thesis's core premise is that the licensed asset appreciates because spectrum is
**scarce**. **The bear's best case is that it stops being scarce — and it is a thesis member that
would do it.**

**If direct-to-device succeeds at scale (ASTS is in the universe; SPCX is the comparator), the
scarcity premium on terrestrial spectrum falls.** The thesis would be **directionally right about
the service-layer compression and wrong about the licence-layer appreciation**, because **the same
technology causes both.** **The net could be negative while both pillars read as confirmed.**

**Recorded as LOW because it is a scenario, not a contradiction** — and because the thesis's own
P3 naming ASTS on the licence/service axis is the instrument that would show it.

### `aa3397a32332` — my own artifact fabricated two filing-metadata values

**Angle 1, applied to this round's own output.** The IRDM `retrieval-strategy` artifact asserted an
accession number (`0001097516-26-000020`) and a page count (*34 pages*). **Neither was ever
returned by any tool call** — `search_documents` returns `filing_date`, and neither of the other
two. **Both were removed and the retraction is recorded in the artifact.**

**Why it is listed rather than quietly fixed:** the page count was the load-bearing one. **The
artifact's argument that the outline saves reading 31 pages DEPENDED on a total** — remove the
total and the argument has to be rewritten, which it was. **A fabricated denominator is exactly
what DA-30 exists to catch, and I produced one in the act of writing an artifact about DA-30.**

**Recorded LOW because it was caught by its own review before commit.** **It is recorded at all
because the catch was mine, not a gate's** — nothing in the pipeline flagged it.

---

## Angles run, and what each returned

| Angle | Method | Result |
|---|---|---|
| **1** | Cross-run contradiction (entity index, corpus-wide) | **4 findings**, all about the gate itself: it reports 3 false HIGHs at 006, its key has no dimension (004's 7 stay false), `retrieved_at` makes restatements unreachable, and the finding ID hashes a constant |
| **2** | Pre-mortem | **2 findings**: the evidence base is being removed by the thesis's own event; P2 rests on one mark |
| **3** | Inversion | **2 findings**: GSAT's margin straddles zero on a word; D2D inverts scarcity from inside the universe |
| **4** | `wrong_if` falsifiability | **2 findings**: P1 cannot fire toward its own risk; P3 and P5 carry P6's fixed circularity |

**Not run, and named rather than omitted:** no cross-**thesis** contradiction sweep (002–005 were
read only for their `entity_claims` convention, not indexed against 006), and no lifecycle
`pre_reduction` hook — **006 has not reached reduction.**

**The one thing this run could not do:** P2 through P6 have not executed, so **their falsifiers were
assessed for form, not for value.** **Finding `ef0dd4b7c7e5` is a form finding and will be
re-testable the moment P3 and P5 produce counts.**

---

*Challenge run at pillar-complete (PIL-1 partial). Per Q64, the claims in this thesis's ten landed
artifacts do not enter the knowledge base until this document is dispositioned.*
