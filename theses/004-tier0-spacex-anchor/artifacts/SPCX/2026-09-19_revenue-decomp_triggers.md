---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-2/PIL-3/PIL-4"
ticker: SPCX
skill: revenue-decomp
mode: triggers
generated_at: 2026-09-19T11:35:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "037b396ab004"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "A trigger is a specific, checkable event — not a risk category. Each row names the datum to read and the threshold, so the check runs without interpretation. Modelled on the plan's own convention and 003's F16 rule that NON-FORMABLE is not PASS."
entity_claims:
  - claim_id: "rdt-trigger-count"
    ticker: SPCX
    metric: falsifier_count
    value: 6
    unit: count
    basis: "checkable triggers over the decomposition finding; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: MODELED
    source: "this artifact — the trigger set itself"
key_metrics:
  falsifier_count: 6
---

# SPCX × revenue-decomp × triggers

**What would overturn the decomposition finding.** The finding under test is:

> **SPCX files a three-level revenue decomposition — segment, then product-or-service within each
> segment, then a consolidated service/product nature split — and every level closes.**

Six triggers. Each names **the datum to read** and **the threshold**, so it fires mechanically
rather than on judgement.

## T-1 — A product member disappears or is renamed

**Read:** the `srt:ProductOrServiceAxis` member list in the next 10-Q or 10-K.
**Threshold:** the list is **not** {LaunchServices, LaunchAndDevelopment, Consumer,
EnterpriseAndGovernment, AISolutionsAndInfrastructure, Advertising} — or the segment pairing of
any member changes.

**Why it matters:** the decomposition is the filer's, so its *stability* is the claim. A renamed
or dropped member means the taxonomy is being managed — and a managed taxonomy is a weaker
foundation for a multiple than a stable one. **A member moving between segments would be the
strongest version of this trigger**, because it would show the boundary is discretionary.

## T-2 — Closure fails

**Read:** `Σ(children)` vs the filed segment parent, per segment, per duration.
**Threshold:** a residual **larger than $1M**, or one that **persists across two consecutive
quarters**.

**Why the $1M and the persistence test:** one $1M cell is rounding (default **D-1**). A residual
that survives a quarter is a cut we have not found. **Firing means the decomposition is
incomplete**, and every multiple built on it inherits the gap.

## T-3 — The two served forms diverge

**Read:** the dimensioned and undimensioned values of the same segment fact.
**Threshold:** the two differ.

**Why:** default **D-3** takes the dimensioned form on the reasoning that the pair carries one
value. **If they ever differ, that reasoning is void** and the choice of form becomes a real
decision — on data that currently presents itself as a non-choice.

## T-4 — A new axis appears

**Read:** the full dimensional enumeration for the revenue concept.
**Threshold:** an axis not previously seen — **`srt:StatementGeographicalAxis` above all**.

**Why:** §3 of `retrieval-strategy` records geography as **UNQUERIED, not ABSENT** — 30 of 30
returned facts carried no such axis, but absence was never established. **A geographic split would
materially change P2** (international expansion is SPCX's stated ARPU driver) and **P3**
(where compute is deployed).

## T-5 — The AI segment splits further

**Read:** whether `spcx:AISolutionsAndInfrastructureMember` (2,669 · 6M) gains sub-dimensions.
**Threshold:** Grok and compute become separately filed.

**Why:** plan finding **V-3** asks *"is the AI segment homogeneous enough to carry one multiple?"*
and this artifact's answer is **partial**: **advertising is separable (710 of 3,379 = 21.0%)**, but
**Grok and compute are not**. **T-5 firing converts P3's partial answer into a full one** — and
would let the two limbs carry different treatments rather than one blended framing.

## T-6 — A common-control recast moves the prior periods

**Read:** whether SPCX restates earlier-period revenue cuts.
**Threshold:** any restatement of a period used in this skill's artifacts.

**Why:** **DA-19.** The xAI merger (2026-02-02) recast prior periods under common control, and the
plan's **V-4** found **Space is the one series that survives the entity boundary**. **A further
recast would not necessarily invalidate the decomposition — but it would invalidate every
growth rate computed across it**, which is why the trigger is on restatement and not on level.

## Trigger summary

| # | Datum | Threshold | Fires ⇒ |
|---|---|---|---|
| **T-1** | product-member list | changed set or pairing | taxonomy is managed; multiples weaken |
| **T-2** | closure residual | >$1M or persisting | decomposition incomplete |
| **T-3** | dimensioned vs undimensioned | any divergence | D-3's reasoning void |
| **T-4** | axis enumeration | a new axis, esp. geography | the cut can be extended |
| **T-5** | AI sub-dimensions | Grok/compute split | V-3 fully answered |
| **T-6** | prior-period restatement | any | growth rates across the boundary void |

## What this set does NOT trigger on

Stated so the boundary is explicit:

- **A change in the LEVEL of any cut.** Revenue can halve inside `AdvertisingMember` without
  touching this finding — the decomposition question is *what is filed*, not *how much*.
- **A change in the segment structure itself** (three segments becoming two). That is a **different
  claim** — plan finding **V-1** and **P1**'s separability test — and it fires *those*, not this.
- **Anything in the prose.** §4 of `retrieval-strategy` records why prose is the wrong place to
  look: it is where aviation and maritime appear, and where the plan wrongly concluded absence.
