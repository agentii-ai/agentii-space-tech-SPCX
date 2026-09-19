---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-2/PIL-3/PIL-4"
ticker: SPCX
skill: revenue-decomp
mode: retrieval-scope
generated_at: 2026-09-19T11:20:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "037b396ab004"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "Source admission is judged by whether a datum sits on the FILER's own dimensional axes. A cut we construct ourselves is not admitted, however arithmetically sound — it is a taxonomy, not a decomposition."
entity_claims:
  - claim_id: "rs-segment-axes-admitted-count"
    ticker: SPCX
    metric: admitted_dimensional_axes
    value: 3
    unit: count
    basis: "axes carrying segment-scoped revenue facts admitted for the deep cut; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q spcx-20260630.htm — dimensional enumeration via search_xbrl_facts(view=detailed)"
key_metrics:
  admitted_dimensional_axes: 3
---

# SPCX × revenue-decomp × retrieval-scope

**Which sources are admitted, and which are excluded.** Spec §3a requires the deep cut to be
*derived from the filings*; this artifact states the admission rule that makes "derived" mean
something, and names what it excludes.

## The admission rule — one test

> **A cut is ADMITTED if and only if the filer files a dimension for it. A cut we construct by
> arithmetic on other cuts is NOT admitted, however sound the arithmetic.**

**Why the rule is strict:** the whole point of `revenue-decomp` is to see the business the way the
issuer reports it, so that later multiples attach to *filed* segments rather than to our model of
them. A constructed cut would let us decompose SPCX into whatever shape suited the valuation —
which is precisely the freedom the constitution removes by fixing segment boundaries at DA-21.

## Admitted

| Source | Status | What it supplies | Why admitted |
|---|---|---|---|
| **`spcx-20260630.htm`** (10-Q, filing `34ca500a-…`) | ✅ **PRIMARY** | All six segment-scoped revenue cuts and both nature cuts | It is the filing. **Every figure in the methodology artifact traces to this single document** |
| `srt:ProductOrServiceAxis` | ✅ admitted | The filer's own product/service dimension | **This is the decomposition.** Not a proxy for it |
| `us-gaap:StatementBusinessSegmentsAxis` | ✅ admitted | Segment scope for each cut | Establishes which segment a product-cut belongs to |
| `srt:ConsolidationItemsAxis` | ✅ admitted, **with a de-duplication rule** | Names which consolidation item a fact belongs to | Admitted **only in its dimensioned form.** The same value is served with and without `OperatingSegmentsMember`; **taking both double-counts.** See the trap below |
| **`003/artifacts/SPCX/…`** (nine artifacts) | ✅ admitted as **cross-check only** | Independent derivations of the same figures | Admitted to *confirm*, never to *supply*. Used once: 003's Consumer 2,485 / Enterprise&Gov 1,806 matched this artifact's figures exactly, which validates both |

## Excluded

| Source | Why excluded |
|---|---|
| **`get_segment_data`** | ❌ **Unusable at the platform level.** Hard-errors at SPCX (`column "k" does not exist`) and elsewhere sums served facts across two years and two durations with no de-duplication. **003's plan recorded this first** (F4, from 002 §7). Its `segment_coverage_pct 116.2` masks a **302.1% overlap** |
| **MD&A narrative prose** | ❌ **Not excluded as a source — excluded as a DENOMINATOR.** It is read for *naming* (it is where "aviation, maritime" appear) but a figure quoted only in prose is not a filed cut. **This distinction is why the plan's F7 went wrong**: it correctly found the prose and incorrectly concluded no decomposition existed |
| **A constructed aviation/maritime split** | ❌ **Constructed, not filed.** Both sit inside `EnterpriseAndGovernmentMember`. Splitting them out would require an allocation assumption with no filed basis |
| **Analyst / third-party segment estimates** | ❌ Outside the filing. A segment shape imposed by a sell-side model is not the filer's |
| **Non-XBRL-derived segment tables** | ❌ Any figure not traceable to a dimensioned fact in `spcx-20260630.htm` |
| **The 1-million-satellite / 100 kW-per-tonne filing** | ❌ **A4: a filed aspiration with no revenue line.** Inadmissible as a valuation input, and it carries no segment revenue to decompose |

## ⚠️ The de-duplication trap — admitted source, double-counted result

Facts are served **twice**: once with `srt:ConsolidationItemsAxis = us-gaap:OperatingSegmentsMember`
and once without it, **carrying the same value.** Measured in this artifact's own queries:

- Connectivity segment revenue `7,548` (6M) and `4,291` (3M) — **each appears twice**
- AI segment revenue `3,379` (6M) and `2,561` (3M) — **each appears twice**
- Space segment revenue `1,581` (6M) and `962` (3M) — **each appears twice**

**Admitting both forms and summing gives exactly double the segment total.** The rule: **take the
dimensioned form**, which states which consolidation item the figure belongs to, and never sum
across the pair. This is the arithmetic cousins of the defect that made `get_segment_data`
unusable — the same data, the same double-service, caught here by hand instead.

## What is NOT decided here

Whether the *excluded* cuts would be material if obtainable. That is a **bound recorded with its
class**, not a gap: aviation and maritime sit inside a filed line; a further split is
`UNRESOLVABLE-FROM-PUBLIC-SOURCES`, not "unknown".
