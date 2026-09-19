# Thesis Quality Checklist — "unit tests for English" (Q32)

> This checklist tests the QUALITY OF THE REQUIREMENTS' WRITING, never artifact
> facts. Prohibited: items starting with `Verify`/`Test`/`Confirm`/`Check` +
> behavior. G1 checks artifacts; this checklist checks prose. IDs `CHK###` are
> global and append-only. ≥80% of items carry a traceability ref. Soft cap 40.
> Machine-maintained bidirectionally (agentii.specify generates, agentii.converge
> re-evaluates and reports regressions) — checkboxes can go back to unchecked.

## Requirement Clarity
- [x] CHK001 每条 `wrong_if` 是否含 metric + threshold + source，而非散文？[Measurability, Spec §1b]

## Requirement Completeness
- [x] CHK002 universe 的纳入/排除标准是否对每个 ticker 都写明？[Completeness, Spec §2]
- [x] CHK003 是否定义了空结果场景（筛选后无标的）下的处置？[Coverage, Gap]

## Requirement Consistency
- [x] CHK004 pillars 之间是否存在互相矛盾的隐含假设？[Conflict]
      <!-- PASS WITH A RECORDED TENSION, not a clean pass. See the log entry below:
           P2's wrong_if is stated TIER-WIDE (threshold=0.5 against a blended share) while
           P2's claim is TWO-SIDED (the licence exceeds half where scarce, and does NOT where
           merely required). Those can disagree — a two-sided claim whose blend sits near 0.50
           is ill-conditioned against a single tier-wide bar. The spec addresses it
           ("what counts as resolution requires the share reported per group as well as
           tier-wide") but the wrong_if itself was not restated. -->
- [x] CHK005 各 pillar 的时间视角是否一致（同一 as_of 与同一持有期）？[Consistency]

---

## Re-evaluation log

### 2026-09-20 — first `agentii.clarify` round · **5/5 passing · 0 regressions**

Baseline before this round was **0/5** — the file was in its generated template state and
**had never been evaluated**. This is the first evaluation, not a re-evaluation, and it is
written by `agentii.clarify` per the Q32 rule that the checklist is re-evaluated **after
every spec write**. The round encoded four answers (spec Q-11 … Q-14).

| ID | State | Basis |
|---|---|---|
| **CHK001** | ✅ **pass** | All **five** pillars carry machine-checkable `wrong_if` — `metric=` + `threshold=` + `source=` + `op=`, no prose. Confirmed two ways: `tools/clarify_scan.py` returns **0 candidates** on the prose-`wrong_if` check (its three returned candidates were the two `rationale-*` **false positives** and `expiry`, none of them a falsifier), and `agentii.converge.re_evaluate_checklist` reports **0 regressions** against the same rule. |
| **CHK002** | ✅ **pass** | §2 carries an explicit membership test on the one axis (*"primary revenue from OPERATING a constellation"*), a **Why it is in this thesis** cell for all **8** members, a **Why it cannot host research** cell for all **5** `NOT_READY` names, a separate cited-third-party table with a per-row *"why it is not a member here"*, and an *"Excluded by design"* paragraph. `tools/plan_audit.py` returns **4/4** — I1 passes on all 8 universe tickers. |
| **CHK003** | ✅ **pass** | **Discharged outright, and this is the item 004 carried open through four consecutive rounds.** §2 carries a dedicated **"Empty-result disposition"** paragraph that names the path (*"if the two P11 deals close, IRDM and GSAT leave the listed universe and the licence layer is held entirely privately"*), fixes the disposition (**not** closed as a null result, premise **not** withdrawn), specifies the conversion (*"a holdings-level read-through recorded in `_cross/`, with the attribution register retained for 007 and 011"*), and marks the tier `no_listed_expression` rather than `no_thesis`. It also records the re-cut's effect on the path. This is a universe-level disposition, not a pillar-level fallback — which is exactly the distinction 004 used to keep CHK003 open. |
| **CHK004** | ✅ **pass**, with one recorded tension | No pillar-level contradiction was found this round, and the round **removed** the one that existed: Q-11 resolved the 005 edge, which was a genuine ambiguity about which thesis owns the IRDM/RKLB gate chain and in which direction it is consumed. **The tension is not between two pillars but inside one:** P2's claim is **two-sided** (licence >50% of EV where scarce; **not** where merely required) while its `wrong_if` is **tier-wide** (`threshold=0.5` on a blended share). The spec states the tier-wide bar is deliberate — *"the harder test"* — and requires the share *"per group as well as tier-wide"*, so the tension is acknowledged rather than hidden. **It is recorded here rather than passed over because a two-sided claim whose blend lands near 0.50 makes the falsifier ill-conditioned, and that is a design choice a reader should see.** No systematic cross-pillar assumption audit has run. |
| **CHK005** | ✅ **pass** | All five pillars share **one** horizon (2026-Q4) and **one** reference quarter, and §1b P3 states it rather than leaving it to inference: *"It is evaluated over the same 2026-Q4 horizon as every other pillar... no pillar in this thesis carries a different `as_of` or holding period."* `as_of: 2026-09-18` is declared in `spec.md` §6. |

**Regressions: none.** No box moved from checked to unchecked, and `agentii.converge
.re_evaluate_checklist` reported **0 regressions** after the write.

**Two facts worth carrying forward rather than losing in the log:**

1. **006 discharges CHK003, which 004 left open across four rounds** — because §2 defines a
   universe-level empty-result path. The distinction 004 drew (a pillar-level fallback is
   *not* a universe-level disposition) is the right one, and 006 satisfies the stronger
   reading.
2. **CHK001 passes on FORM at 006 exactly as it did at 004.** 004's log recorded that its
   P2 and P4 passed on form while failing on substance, because their `source=` named a
   reading 002 proved basis-ambiguous to **46.47 pp**. 006's `source=` fields name the
   **filed disaggregation and the component identity**, which is the remedy that entry asked
   for — but the same caveat applies at one remove: a `source=` naming a disclosure is not a
   check that the disclosure exists. 004 logged that as a proposed **formability invariant
   (I5/I6)**; it is still **proposed rather than built**, and 006 inherits the exposure.

**Carried, not resolved:** the P2 tier-wide-vs-two-sided tension above; the `formability`
invariant that no tool yet checks; and **Q-5 and Q-8 remain flagged for human confirmation**
and are carried as bounds (see `spec.md` §Clarifications).

### 2026-09-20 — second `agentii.clarify` round · **5/5 passing · 0 regressions**

The round that **re-scoped 006 into a sector book** (spec Q-15 … Q-18): three new matrix rows,
a new **Pillar 6**, a third §1c instrument, and the 011 seam declared. `plan_audit.py` **4/4**
(matrix pairs **67 → 85**, subscriptions **54 → 72**). Boxes unchanged; **two of the five now
carry a new obligation, and neither is a regression.**

| ID | State | Basis |
|---|---|---|
| **CHK001** | ✅ **pass** | The new **P6** carries a machine-checkable `wrong_if` (`metric=count_of_tier2_investable_names_without_either_a_strategy_with_a_dateable_catalyst_or_a_recorded_finding_of_none`, `threshold=0`, `source=`) — **six pillars, six machine-checkable falsifiers**, no prose. ⚠️ **But P6's falsifier has a circularity the other five do not — see CHK004.** |
| **CHK002** | ✅ **pass** | §2 unchanged. The round **deliberately removed IRDM and GSAT from the three new matrix rows** (P11 forbids underwriting them on fundamentals) and **recorded that absence as designed rather than as a gap**, in a note at §3. I1 still passes because both names remain in eight other rows — **the invariant is satisfied without being gamed**, which is the distinction the note exists to preserve. |
| **CHK003** | ✅ **pass** | Unchanged, still discharged. |
| **CHK004** | ✅ **pass**, with a **new and sharper** recorded tension | ⚠️ **P6's `wrong_if` can be satisfied by our own prior recording.** It fires on a count of names that carry *"neither a strategy with a dateable catalyst **nor a recorded finding of none**."* **The second clause is what absorbs IRDM and GSAT** — so the falsifier passes for them **by construction**, on a finding this thesis writes rather than on a test it runs. **That is the `UNEXERCISED`-versus-`CLEAN` defect in a new costume**, and this spec is unusually well-placed to see it: §0.2 inherits the rule that *"a check that closes cleanly while testing nothing"* must be reported as itself. **The remedy is not to delete the clause** — a P11 name genuinely has no strategy to give — **but to require that the recorded finding name its class**, so that "none because P11 forbids it" is distinguishable from "none because we could not find one." **⚠️ UPDATED at the third round: this is now FIXED, not carried** — see the 2026-09-20 (third) entry below. The earlier P2 tier-wide-vs-two-sided tension still stands. |
| **CHK005** | ✅ **pass**, with a stated reading | P6 introduces an **entry-timing** dimension P1–P5 do not have — a catalyst inside the **180-day** constitution bar, or the skill's narrower gate. **This is an output requirement, not a horizon change**: every pillar still shares `as_of: 2026-09-18` and the 2026-Q4 horizon, and the catalyst window describes *when an idea could be entered*, not what period it is about. The reading is stated because it is the kind of thing that would otherwise be assumed — and 005 adopted the same resolution (run both bars, report the narrower as the constraint). |

**Regressions: none.** No box moved from checked to unchecked, and `agentii.converge
.re_evaluate_checklist` reported **0 regressions** after the write.

**The pattern this round confirms, and it is the third instance in two rounds.** Q-12's answer
was **correct on its premise and its premise was voided** by Q-15; §4's budget note had already
been corrected once and needed correcting again; and P6's falsifier reproduces a defect class
the spec itself documents. **In each case the failure was not a wrong statement but a statement
that outlived the condition it was true under** — which is the same shape as 004's finding that
*a closure chain carrying a rounding allowance cannot detect the error the allowance absorbs.*

### 2026-09-20 — third `agentii.clarify` round · **5/5 passing · 0 regressions**

**The round that audited the round before it, and found four defects — all of them created by
the Q-15 re-scope.** `plan_audit.py` **4/4** unchanged. Boxes unchanged. The round encodes spec
Q-19 … Q-22 and **fixes all four in the body**, so nothing here is carried.

| ID | State | Basis |
|---|---|---|
| **CHK001** | ✅ **pass** | P6's `wrong_if` is **rewritten** (Q-22) to require the recorded finding to name its class — see CHK004. Still machine-checkable, still `metric=` + `threshold=` + `source=`. |
| **CHK002** | ✅ **pass** | §2 unchanged. The round **fixed a stage declaration rather than a rationale**: `position-sizing` was declared `none` against a registry that says **`late`** on every mode. `plan_audit` does not check this and never did — see the note below. |
| **CHK003** | ✅ **pass** | Unchanged, still discharged. **And this round's Q-20 extended its logic**: the **all-zero case for the strategy layer** is now pre-declared (*"this tier has no immediately expressible trade at this run's `as_of`"*), mirroring §2's universe-level disposition. **The strategy layer previously had no empty-result mechanism while the universe layer did** — an internal inconsistency the round removed. |
| **CHK004** | ✅ **pass**, tension **FIXED** | **P6's circular falsifier is repaired, not carried.** The clause *"or a recorded finding of none"* absorbed IRDM and GSAT **by construction**; it now requires the class (`P11_FORBIDS_UNDERWRITING` / `NO_DATEABLE_CATALYST` / `NOT_READY`), so *"none because P11 forbids it"* is distinguishable from *"none because we could not find one."* **The clause was kept, not deleted** — a P11 name genuinely has no strategy, and a falsifier that failed on correct behaviour would be the worse error. The earlier P2 two-sided-vs-tier-wide tension still stands. |
| **CHK005** | ✅ **pass** | Unchanged reading. **Q-20 sharpened it**: the **20–60 day** bar is now named in §1b P6 and §6 as a number, where the previous round wrote *"the skill's own gate"* — **a bar the spec does not state is a bar a reader cannot check**, and the spec was relying on the reader to look it up. |

**Regressions: none.** `agentii.converge.re_evaluate_checklist` reported **0 regressions**.

**⚠️ A check that does not exist, demonstrated for the second time.** 004's log proposed an
**`I5` market-data-stage consistency check against the registry** and it was **never built**.
This round is the evidence that the gap is real and recurring: **the Q-15 re-scope declared
`position-sizing` as `none` in good faith, `plan_audit` returned 4/4, and nothing anywhere
objected** — the mismatch was found only because a clarify round read the registry entry by
hand. **That is the same shape as 004's two other unbuilt checks** (`I5` stage consistency,
`I6` formability) and it is now the third instance. Recorded as a **proposal with three
supporting cases**, not as a fix.

**The pattern, now at four instances across three rounds.** Q-12's answer was correct on a
premise Q-15 voided; §4's budget note needed correcting twice; P6's falsifier reproduced a
defect class the spec documents; and the stage declaration contradicted the registry it was
written from. **In every case the failure was not a wrong statement but a statement that
outlived — or never checked — the condition it was true under.**

