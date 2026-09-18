# Thesis Quality Checklist — "unit tests for English" (Q32)

> This checklist tests the QUALITY OF THE REQUIREMENTS' WRITING, never artifact
> facts. Prohibited: items starting with `Verify`/`Test`/`Confirm`/`Check` +
> behavior. G1 checks artifacts; this checklist checks prose. IDs `CHK###` are
> global and append-only. ≥80% of items carry a traceability ref. Soft cap 40.
> Machine-maintained bidirectionally (agentii.specify generates, agentii.converge
> re-evaluates and reports regressions) — checkboxes can go back to unchecked.

## Re-evaluation history

| Round | Date | Result | Change |
|---|---|---|---|
| 1 | 2026-09-18 | 2/5 passing, 1 partial, 1 failing, 1 caveat | First evaluation after `agentii.clarify` round 1 |
| **2** | **2026-09-18** | **4/5 passing, 1 partial** | `agentii.clarify` round 2 (Q-6) closed CHK003 |

**Round 2 result: 4/5 passing, 1 partial.** No regressions — CHK003 moved from failing
to passing; nothing moved backwards.

| ID | Round 1 | Round 2 |
|---|---|---|
| CHK001 | ✅ | ✅ |
| CHK002 | ✅ | ✅ |
| CHK003 | ❌ | ✅ **closed** |
| CHK004 | ⚠️ | ⚠️ unchanged |
| CHK005 | ◐ | ◐ unchanged |

---

## Requirement Clarity
- [x] CHK001 每条 `wrong_if` 是否含 metric + threshold + source，而非散文？[Measurability, Spec §1b]
  - **Passing, and strengthened.** All six pillars carry `metric=`, `threshold=`, `source=`
    and an explicit `op=`. PIL-1 and PIL-5 now additionally carry `basis=ANY_OF_A_B_C`
    under the Q-6 standing rule, so the falsifier is evaluated across every competing
    definition rather than a silently chosen one. `tools/clarify_scan.py` reports zero
    `prose_wrong_if` findings.

## Requirement Completeness
- [x] CHK002 universe 的纳入/排除标准是否对每个 ticker 都写明？[Completeness, Spec §2]
  - **Passing.** All 35 listed rows carry a rationale; the closing paragraph states the
    exclusion rule for JOBY/ACHR, the 13 `NOT_READY` names and the 9 deferred `PARTIAL`
    names; Varda's basis of admission (P6 node) is stated in its row.
- [x] CHK003 是否定义了空结果场景（筛选后无标的）下的处置？[Coverage, Gap]
  - **Closed in round 2.** §1c now carries an explicit disposition: a pillar whose
    `wrong_if` cannot be evaluated for want of a disclosure is **not dropped and not
    failed** — it is recorded `UNRESOLVABLE-FROM-PUBLIC-SOURCES`, carried in
    `thesis.md → known-open`, and reported with the specific disclosure that would
    resolve it. The rule explicitly reframes such a pillar as *a finding about
    disclosure quality* rather than a research gap, which is the right framing for a
    technology-baseline thesis. The clause "no pillar may be marked unresolved for
    being multi-definitional" also prevents the Q-6 register from becoming an
    escape hatch. Mirrored in `thesis.md → methodology.unresolvable_disposition`.

## Requirement Consistency
- [x] CHK004 pillars 之间是否存在互相矛盾的隐含假设？[Conflict]
  - **Passing, caveat unchanged from round 1.** PIL-1 (launch cost governs every
    application-layer business case) and PIL-3 (manufacturing rate is the binding
    constraint) remain reconcilable — PIL-1 is the *viability* axis, PIL-3 the
    *deployment-timing* axis — but the spec still does not say so explicitly.
    **Unchanged recommended fix:** add one clause to PIL-3 stating it does not contest
    PIL-1's cost-viability claim. Advisory; does not block execution.
- [ ] CHK005 各 pillar 的时间视角是否一致（同一 as_of 与同一持有期）？[Consistency]
  - **Partial, unchanged.** `as_of: 2026-09-18` is now declared, so the pillars share a
    reference date. They do not share a natural horizon: PIL-1/PIL-2 resolve against
    current disclosures, PIL-4's evidence point is "first samples as early as 2027", and
    PIL-6 turns on multi-year regulatory proceedings. The spec declares a 2026-Q4
    horizon at the top but never reconciles it against per-pillar horizons.
    Note: the §1c register addresses *definitional* multiplicity, not *temporal*
    multiplicity — these are different axes and DA-01…DA-22 do not cover this. A
    per-pillar horizon column would close it.

---

## Notes for the next round

- **The one hard failure is closed.** CHK003 was pure writing work and is now done.
- **Zero blocking items remain** in `thesis.md → known-open`. Both entries were
  downgraded to `blocking: false` under the Q-6 standing rule. Task execution can begin.
- Two advisory fixes outstanding, neither blocking: the PIL-3 wording clause (CHK004)
  and a per-pillar horizon column (CHK005).
- The §1c register imposes a **new obligation on every future artifact**: each must
  label which definition of each ambiguous term it is quoting. This is not a checklist
  item yet — if it proves to be a recurring failure mode, it should become CHK006.
