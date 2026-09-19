# Thesis Quality Checklist — "unit tests for English" (Q32)

> This checklist tests the QUALITY OF THE REQUIREMENTS' WRITING, never artifact
> facts. Prohibited: items starting with `Verify`/`Test`/`Confirm`/`Check` +
> behavior. G1 checks artifacts; this checklist checks prose. IDs `CHK###` are
> global and append-only. ≥80% of items carry a traceability ref. Soft cap 40.
> Machine-maintained bidirectionally (`agentii.specify` generates, `agentii.converge`
> re-evaluates and reports regressions) — checkboxes can go back to unchecked.

## Requirement Clarity
- [x] CHK001 每条 `wrong_if` 是否含 metric + threshold + source，而非散文？[Measurability, Spec §1b]
  → **PASS.** 7 `wrong_if` blocks, all three keys present on every one, **0 malformed**.
  Note: Pillar 3 carries **two** `wrong_if` lines (the register claim and the Tier 1
  gross-margin control) and Pillar 5's carries a `wrong_if_companion` — both intentional,
  both well-formed.

## Requirement Completeness
- [x] CHK002 universe 的纳入/排除标准是否对每个 ticker 都写明？[Completeness, Spec §2]
  → **PASS.** 17 rows, **every one** with a rationale ≥12 chars. Four names (VOYG, LUNR,
  HAWK, BA) are marked as **defect sites rather than research subjects** — present for a
  single reason each, and the spec says so rather than implying they are businesses.
- [x] CHK003 是否定义了空结果场景（筛选后无标的）下的处置？[Coverage, Gap]
  → **PASS — and the disposition is stronger than the item asks for.** This thesis has no
  screen, so the literal "no names survive" case does not arise. The *analogous* case does,
  and it is defined: **a denominator that cannot be resolved is recorded
  `UNRESOLVABLE-FROM-PUBLIC-SOURCES` and the ±15% test is reported `not met` — never
  passed by default**, with the two v1.3.0 disposition classes supplying the remedy.
  001 closed this item the same way (spec §1c, closing paragraph).

## Requirement Consistency
- [x] CHK004 pillars 之间是否存在互相矛盾的隐含假设？[Conflict]
  → **PASS, with one interaction recorded.** No pillar contradicts another, but **P6 can
  depress P5's denominator in a way the spec does not currently surface:**
  | | |
  |---|---|
  | **The interaction** | P1 converts a figure to `DEMONSTRATED` by citing it at source. **P6 may then classify that same figure boundary-contaminated** (e.g. anything inside SPCX's AI segment). A contaminated figure should not count as a clean `DEMONSTRATED`. |
  | **Consequence** | **P6 succeeding can push P5's conversion share *down*.** A pillar doing its job well makes another pillar's threshold harder. |
  | **Why it is not a contradiction** | Both are correct. The conversion share is *supposed* to fall when figures turn out to be contaminated — that is the ledger working. |
  | **What was missing** | P5's `wrong_if` did not say whether contaminated figures count. **Resolved: a contaminated figure converts to `DERIVED` or stays `CLAIMED`, never `DEMONSTRATED`** — so the share is honest by construction. |
  | **Similarly** | P2's failure (band >50%) does not invalidate P5; it **removes figures from the convertible set**, again lowering the share. The share is a *measure of the evidence base*, not of effort. |

## Requirement Consistency
- [x] CHK005 各 pillar 的时间视角是否一致（同一 as_of 与同一持有期）？[Consistency]
  → **PASS.** `as_of: 2026-09-18` in both `spec.md` and `thesis.md`. **No holding period
  exists** because no positions are taken — the item's second clause is N/A by design, and
  stated rather than left blank. Filing periods differ per figure (Q2 2026, Q1 2026,
  FY2025) but that is *source* period, not *as_of* period; every artifact dates its source.

---

**Evaluation recorded 2026-09-18** at the `agentii.implement` preflight. The soft gate
(Q29) was **not** waived — all five items were evaluated, and CHK004 produced a
finding that changed P5's semantics rather than a rubber stamp.
