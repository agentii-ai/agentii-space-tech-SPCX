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
