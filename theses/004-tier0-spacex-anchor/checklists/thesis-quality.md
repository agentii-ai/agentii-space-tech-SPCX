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
      <!-- N/A — approved 2026-09-19 at the implement soft gate (Q29). §2 fixes the universe
           at ONE member (SPCX), so there is no screening step that could return an empty set.
           The pillar-level degenerate case IS defined, in §1b P1: "a segment without a
           discrete filed revenue line or operating result — i.e. fewer than three separable
           businesses", resolving to "a single blended multiple". That is a pillar fallback,
           not a universe one — which is why this stayed open for five clarify rounds before
           being closed as inapplicable rather than satisfied. -->

## Requirement Consistency
- [x] CHK004 pillars 之间是否存在互相矛盾的隐含假设？[Conflict]
- [x] CHK005 各 pillar 的时间视角是否一致（同一 as_of 与同一持有期）？[Consistency]

---

## Re-evaluation log

### 2026-09-19 — after clarify round 2 · **4/5 passing · 0 regressions**

Written by `agentii.clarify` per the Q32 rule that the checklist is re-evaluated
**after every spec write**. Baseline before this round was **3/5**.

| ID | State | Basis |
|---|---|---|
| **CHK001** | ✅ **pass** | `tools/clarify_scan.py` returns **0 candidates** on all seven checks; the prose-`wrong_if` check specifically confirms every pillar P1–P6 carries `metric=` + `threshold=` + `source=`. **Caveat held against A-2:** P2 and P4 pass on **form** while failing on **substance** — their `source=` names an operating-margin reading that 002 proved basis-ambiguous to **46.47pp**. The box is checked because the *writing* requirement is met; A-2 is the substantive remedy. |
| **CHK002** | ✅ **pass** | §2 carries a rationale for the one universe member, a role **and** a why-not-a-member clause for each of the five read-through rows, and an explicit *"Excluded by design"* paragraph. Scanner's universe check returns no short rows and no row with an empty rationale. |
| **CHK003** | ❌ **open** | No disposition is written for the empty-result scenario. Partially mitigated rather than satisfied: the universe is fixed at one member, so no screen can return zero, and **P1 defines the degenerate case** (*"a segment without a discrete filed revenue line or operating result — i.e. fewer than three separable businesses"*, resolving to *"a single blended multiple"*). That is a pillar-level fallback, not a universe-level one, and does not discharge the item as written. |
| **CHK004** | ✅ **pass** | The one **known** contradiction is resolved. It was real and it was the reason this round ran: clarify round 1 re-ranked the pillars (*"P2 Connectivity → MAIN LINE; P3 → Contested; P4 → DEMOTED"*) while §1b still listed all six at their original priorities, and round 1 was never written into the body. Round 2 resolved it — *"§1b keeps six pillars. Round 1's re-ranking is rationale, not structure."* **Scope note: this records resolution of the known instance, not a systematic cross-pillar assumption audit**, which no round has performed. |
| **CHK005** | ✅ **pass** | All six pillars share one time horizon (2026-Q4) and one price reference (the dated print — `$135.00`, 2026-06; ~$1.62T per the constitution), and `as_of: 2026-09-18` is declared in `thesis.md`. Round 2's re-pin to `constitution_pin: 1.5.0` is a **version** change and moves no pillar's time perspective. |

**Regressions: none.** No box moved from checked to unchecked. CHK004 is the round's
gain (3/5 → 4/5) and CHK003 remains the single open item.

**Carried for the next round or `agentii.converge`:** CHK003, and the substance half of
CHK001 — tracked as **A-2** in `spec.md`'s Clarify round 2, alongside **A-1** and
**A-3 … A-7**, none of which are in this checklist's scope (they are body amendments,
not prose-quality failures).

### 2026-09-19 — after clarify round 3 · **4/5 passing · 0 regressions**

Scope against a **completed 003** and a **live price feed**. Boxes unchanged; the basis for
three of the four passes got materially stronger, and one new checking obligation appeared.

| ID | State | Basis |
|---|---|---|
| **CHK001** | ✅ **pass** | Scanner still returns **0 candidates**. Round 3 added two matrix rows (`revenue-decomp`, `reverse-dcf`) but **no pillars**, so the `wrong_if` population is unchanged and every pillar still carries `metric=` + `threshold=` + `source=`. **A-2 remains the substance half and is still open** — P2 and P4 falsify on readings 002 proved basis-ambiguous to 46.47pp. |
| **CHK002** | ✅ **pass** | §2 unchanged. Round 3's rebuild of §3 initially **orphaned VRT** — it appeared only in the `comps` row, and narrowing that row would have left VRT scoped and then dropped, which is what invariant I1 exists to catch. `comps` was widened to carry the AI framing set, and **`plan_audit.py` now returns 4/4**. |
| **CHK003** | ❌ **open** | Unchanged. Still no universe-level empty-result disposition. **Round 3 sharpened why it may not matter**: the universe is fixed at one member, so no screen can return zero, and P1 defines the pillar-level degenerate case. That remains a mitigation, not a discharge. |
| **CHK004** | ✅ **pass** | **A third contradiction was found and resolved in this round, and it was between two owner answers**: *"consume 003's 9; run only the 5 new"* and *"go deeper inside the segments."* 003 worked at the **segment** level, so going inside was work on precisely the skills the first answer said to skip. **Resolved by `revenue-decomp`** — a registry skill used by neither thesis — which honours both literally. **The instance count is now three, all resolved; no systematic cross-pillar audit has yet run.** |
| **CHK005** | ✅ **pass** | **Round 3 made this the most load-bearing item and it now passes on a stricter reading.** Before, every figure shared one time reference. Now there are **two price bases at different dates** — the live quote (2026-09-18/19) and the constitution's print (2026-06, `$135.00`). They are not collapsed: **§5 requires every market-referenced figure to carry its basis, its stamp and its source**, and the spread between the bases is reported as a finding. All six pillars still share the 2026-Q4 horizon. |

**Regressions: none.** CHK003 remains the only open item, as after round 2.

**New checking obligation, recorded not yet discharged.** `plan_audit.py` verifies I1–I4 but
knows nothing about **market-data stage**. Round 3 found two rows (`sotp-valuation`,
`ratio-analysis`) where this spec declared `none` and the skill registry declares `late` —
a mismatch no existing check catches, and one that pinned the primary instrument where it
could not obtain a price. **A `market_data_stage` consistency check against the registry is
the obvious I5**, and is proposed rather than built.

### 2026-09-19 — after clarify round 4 · **4/5 passing · 0 regressions**

Scoping the depth row against what the filer actually reports. `plan_audit.py` **4/4**,
`clarify_scan.py` **0 candidates**. **The round's own output would have failed an I-invariant
that does not exist yet** — see below.

| ID | State | Basis |
|---|---|---|
| **CHK001** | ✅ **pass** | Scanner 0. Round 4 changed no falsifier population; it corrected a **matrix row's scope** and two `warn`/`blocking` classifications, not any pillar's `wrong_if`. **A-2 remains the substance half and is still open.** |
| **CHK002** | ✅ **pass** | §2 unchanged; `plan_audit` I1 passes. **But round 4 exposed that I1 is too weak** — it checks a universe ticker appears somewhere, and it passed while a **matrix row named cuts the filer does not report**. See the gap note. |
| **CHK003** | ❌ **open** | Unchanged — the fourth round in which it has been carried. It is now the **longest-open item in this checklist**. |
| **CHK004** | ✅ **pass** | No new pillar-level contradiction. **Round 4's own correction was not a contradiction between pillars but between a spec row and the source data** — a different class, and one no checklist item covers. |
| **CHK005** | ✅ **pass** | Round 4 **improved** this materially: V-7's resolution adds the customer-concentration series on **four periods across two years** (Customer A 17.89/18.30/19.89/16.70%), all on stated bases. It also added a **fifth** instance of the two-bases-opposite-signs pattern — H1 falls while Q2 rises — which §1c's DA-30 rule now covers. |

**Regressions: none.** CHK003 remains the sole open item.

**The gap this round found, and it is the sharper version of round 3's.** I3 asks whether a
skill resolves in the registry. I1 asks whether a universe ticker appears in the matrix.
**Neither asks whether a row's *claimed inputs* exist in the filer's disclosure.** Round 3
wrote *"aviation / maritime"* as fileable cuts; both appear twice in the whole SPCX corpus,
as prose, with no revenue line. `plan_audit` passed the entire time.

**That is a `formability` check, not a coverage check**, and it is the same class as round 3's
missing market-data-stage check — a value that *looks* like a specification and is actually an
assumption. **Both are now proposed as I5/I6 rather than built.** The lesson from three rounds
is consistent: **this spec's tables are read as data by tools that cannot tell a verified
figure from a plausible one, and every round so far has found at least one of the latter.**
