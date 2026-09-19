---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-2/PIL-3/PIL-4"
ticker: SPCX
skill: revenue-decomp
mode: defaults
generated_at: 2026-09-19T11:30:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "037b396ab004"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-26"
    chosen_reading: "Where a duration is not stated in the fact itself, the default is to READ IT FROM the period_start/period_end pair rather than infer it from row position — 002 registered that the mislabelled period varies by issuer and cannot be screened positionally."
entity_claims:
  - claim_id: "rdf-closure-residual-zero"
    ticker: SPCX
    metric: segment_closure_residual
    value: 0
    unit: USD
    basis: "Connectivity child-sum 4,633 + 2,915 = 7,548 vs filed parent 7,548; 6M duration, six months ended 2026-06-30. CLOSES EXACTLY"
    period: "2026Q2"
    evidence_grade: DERIVED
    source: "SPCX 10-Q spcx-20260630.htm p.13 (Note 3) — arithmetic on filed cells"
key_metrics:
  connectivity_closure_residual_usd_m: 0
  conn_entgov_h1_2026_usd_m: 2915
---

# SPCX × revenue-decomp × defaults

**The default assumptions used where no filed figure exists.** Every default below is one the
filer does not settle, and each is stated so a reader can disagree with it explicitly rather than
inherit it silently.

## D-1 — There is NO closure residual. The earlier ±$1M was a transcription error, not rounding

**Where it appeared:** Connectivity, 6M. An earlier draft read the Enterprise & Government child as
`2,914`, giving `4,633 + 2,914 = 7,547` against a filed parent of `7,548` — a **$1M residual**.

**The filed child is `2,915`.** Read from the source rather than re-read from the draft:

> `Consumer 4,633 + Enterprise & Government 2,915 = Connectivity 7,548` — **exact**.
> Source: [SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13) (Note 3, revenue disaggregated by type
> and segment, six months ended 2026-06-30).

| | |
|---|---|
| **What was defaulted** | Nothing. A **phantom** `$1M` cell was described as *"rounding within $M-denominated filing"* |
| **Why the correction matters** | The artifact had already **constructed a default (D-1) to absorb a number that does not exist** — and a default is the one construct a reader cannot falsify, because it is a reading rather than a filed claim |
| **How it was caught** | By reading p.13 directly. The residual **could not have been caught by closure testing**, because closure was tested against the same wrong child it was derived from |
| **What would overturn the correction** | A filed E&G figure of `2,914` for 6M 2026 anywhere in the filing. It does not appear |
| **Class** | `DERIVED` — arithmetic on filed cells |

> ### ⚠️ This is the same defect class the report is about, one level up.
>
> **A fabricated residual is worse than a fabricated figure.** A figure can be checked against the
> filing; a *default* is a stated reading of an ambiguity, so **it can only be checked against the
> ambiguity** — and there was none. The artifact spent a page explaining how to treat a gap that
> the filing closes exactly.
>
> **Recorded rather than deleted**, because the correction is the finding: **a thesis that reads its
> own prior drafts instead of the source will manufacture residuals, and then build defaults to
> absorb them.** Every closure test in this skill now reads p.13.

## D-2 — The product axis is assumed EXHAUSTIVE, and the assumption is tested

**Where:** every closure test.

**Default:** the assumption that `srt:ProductOrServiceAxis` members are a **partition** of each
segment — that no revenue is unfiled.

**Why it is a default and not a fact:** XBRL does not declare a dimension exhaustive. The filer
could in principle file less than the whole.

**How it is tested:** the **closure test is the test of the assumption.** If the children summed to
less than the parent, the axis would be non-exhaustive and the gap would be unfiled revenue.
**They sum to the parent in all three segments and at consolidation.** So the assumption is
**confirmed by arithmetic**, not merely asserted.

**What would overturn it:** any period where `Σ(children) < parent` by more than rounding. **That
would be a finding — unfiled revenue — not a bookkeeping error.**

## D-3 — Which of the two served forms to take

**Where:** every segment fact.

**Default:** take the fact carrying `srt:ConsolidationItemsAxis = us-gaap:OperatingSegmentsMember`;
**never sum across the pair.**

**Why a default is needed at all:** the platform serves each segment figure **twice**, once with
that dimension and once without, at the same value. **Nothing in the response marks one as
canonical.**

**Why the dimensioned form:** it states *which consolidation item the figure belongs to* — the
information needed to know the fact is a segment subtotal and not a consolidated total that
happens to equal it.

**Cost of getting it wrong:** summing both forms gives **exactly double**. Recorded in
`retrieval-scope` §"the de-duplication trap".

## D-4 — Duration is read from the fact, never inferred from position

**Where:** choosing 3M vs 6M throughout.

**Default:** read `period_start`/`period_end` off the fact itself.

**Why:** 001 and 002 both registered period traps — **DA-26** (an annual-basis fact served where a
quarterly label is asserted, universal across 19 of 19 issuers, with the mislabelled period
**varying by issuer**) and **DA-27** (calendar-derived fiscal labels). **Row position is not a
usable proxy.** SPCX files 3M and 6M under the same concept and the same axes, so a positional
reading would silently mix them.

**Application:** every figure in this skill's artifacts names its duration in `basis`, and the
machine-readable `period` field carries `2026Q2` for both durations — which is why the duration
label is **not optional** in `basis`.

## D-5 — No default is taken where a filed figure exists

Stated as a negative, because it is the discipline that makes the other four meaningful:

| Question | Default taken? |
|---|---|
| How much did Connectivity Consumer earn in H1? | **No** — filed, `4,633` |
| Did that split exist? | **No** — filed as a dimension, not inferred |
| Which segment does `ConsumerMember` belong to? | **No** — the fact carries `spcx:ConnectivityMember` |
| What is aviation revenue? | **No default is available.** Recorded `UNRESOLVABLE-FROM-PUBLIC-SOURCES`. **Inventing one would be the failure this section exists to prevent** |

## Summary

| # | Default | Grade | Overturned by |
|---|---|---|---|
| D-1 | **No residual exists** — the earlier ±$1M was a transcription error | `DERIVED` | A filed E&G of `2,914`; it does not appear |
| D-2 | The product axis is exhaustive | `MODELED`, **arithmetically confirmed** | `Σ(children) < parent` beyond rounding |
| D-3 | Take the dimensioned served form | `DERIVED` | A response marking a canonical form |
| D-4 | Duration read from the fact | `DERIVED` | — (this is the safe reading, not a guess) |
| D-5 | No default where a figure is filed | — | — |

**Four defaults survive and one is retracted.** The retraction is the substantive result: **three
segments and the consolidated total now close on filed cells alone, with no reading of ours
anywhere in the closure chain.**
