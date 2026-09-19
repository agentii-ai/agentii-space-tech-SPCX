---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-2/PIL-3/PIL-4"
ticker: SPCX
skill: revenue-decomp
mode: retrieval-strategy
generated_at: 2026-09-19T11:25:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "037b396ab004"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "The decomposition was located by reading the filer's DIMENSIONS, not its values. The search is stated as a query so it repeats, and the negative result (which axes are absent) is recorded with the same fidelity as the positive one."
entity_claims:
  - claim_id: "rst-deep-cut-found-at-query-1"
    ticker: SPCX
    metric: retrieval_queries_to_find_deep_cut
    value: 1
    unit: count
    basis: "queries required to surface srt:ProductOrServiceAxis; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "self-reported search trace; reproducible via the query in §1"
key_metrics:
  retrieval_queries_to_find_deep_cut: 1
---

# SPCX × revenue-decomp × retrieval-strategy

**How the sources were located, so the search repeats.** This artifact exists because the plan's
own retrieval **failed and did not know it** — see §4.

## 1. The query that found the decomposition, in full

```python
search_xbrl_facts(
    ticker="SPCX",
    concept="RevenueFromContractWithCustomerExcludingAssessedTax",
    view="detailed",        # ← THE LOAD-BEARING PARAMETER
    fiscal_year=2026,
    page_size=40)
```

**The whole find turns on `view="detailed"`.** The default is `view="standard"`, which
**collapses dimensionality** and returns one consolidated number per period. Under the default,
SPCX's revenue is `12,508` (6M) and `7,814` (3M) and the six segment-scoped cuts are **invisible**.

**One query was sufficient.** No iteration, no widening, no fallback. That is worth stating: the
decomposition was not hard to find, it was **hard to know to look for** — and the plan looked in
the wrong place (§4).

## 2. The read order, and why it is this order

1. **Read the DIMENSIONS before the VALUES.** The first pass reads only which axes and members are
   present, ignoring every number. This is what surfaced `srt:ProductOrServiceAxis` and its eight
   members.
2. **Pair each product member to its segment** via `us-gaap:StatementBusinessSegmentsAxis`, which
   most product facts also carry.
3. **Then** read values, and immediately test closure (§3 of the methodology artifact).
4. **Only then** compare against 003.

> **Why dimensions first:** if you read values first, the two served forms of the same fact
> (`7,548` twice — with and without `ConsolidationItemsMember`) look like **two different segment
> totals**, and the natural move is to reconcile them. **There is nothing to reconcile.** Reading
> structure first makes the duplication visible as structure rather than as a numerical puzzle.

## 3. The negative searches — recorded, not omitted

A search that returns nothing is a finding **only if it was actually run.** These were:

| Search | Result | Consequences |
|---|---|---|
| `srt:StatementGeographicalAxis` in the 30 facts returned | **0 occurrences** | ⚠️ **Recorded as UNQUERIED, not as ABSENT.** 30 facts is one page of a 30-row result; a geography axis could exist unexamined. **Stated as a bound, because "we did not see it" and "it is not filed" are different claims** |
| Any axis splitting `AISolutionsAndInfrastructureMember` further | **0 occurrences** | Grok and compute are not separately filed |
| Any axis splitting `EnterpriseAndGovernmentMember` into aviation / maritime | **0 occurrences** | Consistent with 003's finding that both appear only as prose |
| Vehicle-level splits (Falcon vs Starship) inside `LaunchServicesMember` | **0 occurrences** | Not filed |
| `get_segment_data(ticker="SPCX", segment_type="product")` | ❌ **HARD ERROR** — `column "k" does not exist` | The obvious route is broken. **003 recorded this first** |

## 4. ⚠️ Why the plan's own retrieval failed — the reusable lesson

**The plan searched 003's artifacts for the cut, and correctly concluded it was not there.**

> F7: *"`aviation` and `maritime` appear twice in all nine SPCX artifacts, as prose, with no revenue
> figure attached."*

**Every word of that is true.** The error was **inferring absence from a search of the wrong
corpus.** 003 built a *margin* map across nine issuers — it read the segment note and the MD&A,
and it had no reason to enumerate `srt:ProductOrServiceAxis`. **So a cut absent from 003's nine
artifacts is not a cut absent from the filing.**

| | |
|---|---|
| **The failing shape** | Treating a **downstream synthesis** as the primary source for a **disclosure question** |
| **The correct shape** | Disclosure questions are answered from **the filing's own XBRL**; syntheses are read to **cross-check**, never to bound |
| **The generalisable rule** | **"Not in the consumed artifacts" ≠ "not filed."** A consumed artifact is a *reading* of the filing, taken for someone else's purpose |

**This cost one plan round and produced a wrong finding (F7) that stood in the spec until the first
artifact contradicted it.** It is recorded here rather than in the artifact's prose because it is a
**method** defect, and the method is what this mode carries.

## 5. Reproducing this artifact

```bash
# 1. surface the axes (the query in §1)
# 2. read members, ignore values
# 3. read values, test closure per segment AND at consolidation
# 4. cross-check against 003 — confirm only, never bound
```

**Expected output:** six segment-scoped cuts, two nature cuts, three closures (§2 of the
methodology artifact), and the five negative results in §3.
