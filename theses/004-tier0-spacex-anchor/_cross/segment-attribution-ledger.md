---
thesis_id: "004-tier0-spacex-anchor"
pillar: cross
ticker: SPCX
skill: synthesis
mode: methodology
generated_at: 2026-09-19T15:00:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "Every disposition below states the FILED reading where the served layer differs. The consolidated operating line is served as +143,000,000 against a filed (143,000,000)."
  - da_id: "DA-21"
    chosen_reading: "Whether the segment attribution is real is a question about the issuer's own filed boundaries, answered from Note 18 — never from a synthesis of it."
entity_claims:
  - claim_id: "ledger-blocking-resolved"
    ticker: SPCX
    metric: count_of_blocking_items_resolved
    value: 3
    unit: count
    basis: "V-1, V-5, V-7 resolved of the blocking set {V-1, V-2, V-5, V-7}; V-2 resolves in-line"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "this ledger, with each resolution's page reference"
---

# Segment Attribution Ledger — the V-1 … V-7 queue, with dispositions

> **Why this file exists.** Under P4 an unvalidated number is a pillar that cannot fire. **Its
> purpose is that an item CANNOT quietly disappear**: every row names the pillar it gates, the
> source class that would resolve it, and its disposition — **including the ones that resolved
> against this thesis's own earlier positions.**

## The queue

| # | Question | Gates | Status | Disposition |
|---|---|---|---|---|
| **V-1** | Does the AI segment file an operating result at all? | **P1** | ✅ **RESOLVED** | **YES — FILED, disclosed four times.** `$(1,257)M` at **p.30 (Note 18), p.44, p.45 (narrative), p.46 (reconciliation)**; identity closes exactly. **P1's separability test is 3 of 3 DISCLOSED, not 2 of 3** |
| **V-2** | Segment-to-consolidated reconciliation residual | **P1** | ✅ **RESOLVED in-line** | **Residual = 0 on the FILED signs.** `7,814 − 7,957 = (143)` ✓. ⚠️ **The served layer returns `+143,000,000`** — a **DA-23 artefact, not a residual** |
| **V-3** | Is the AI segment homogeneous enough for one multiple? | **P3** | ⚠️ **PARTIALLY RESOLVED** | **Advertising IS separable (710 of 3,379 = 21.0%).** Grok and compute are **not** — `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| **V-4** | Does the Space series survive the entity boundary? | **P1, P2, P5** | ✅ **RESOLVED** | **Space is the series that SURVIVES** — and it **fell 1.9%** across H1 while consolidated revenue rose 53.7%. Connectivity also clean |
| **V-5** | Cursor treatment; is the dilution determinable? | **P1** | ✅ **RESOLVED — and the premise was WRONG** | **The deal CLOSED 2026-08-14.** **391,041,680** shares issued; **464,535,053** total potential dilution. **It was never "not determinable"** |
| **V-6** | Price-input datability | **P6** | ✅ **SUPERSEDED by the live feed** | A **keyless NASDAQ** quote exists (verified **$152.71**). Both bases publish; the spread is a component |
| **V-7** | Backlog quantification for the DCF admissibility test | **P7** | ✅ **RESOLVED from XBRL** | Customer concentration is a **dimensional fact**, not Note 3 prose. **Customer A 17.89% H1 / 18.30% Q2; Customer B 12.20% H1 / 19.50% Q2**; combined **30.09%** |

## The blocking set, as it moved across the run

| Item | Round 0 | Round 4 | **Implement (final)** |
|---|---|---|---|
| **V-1** | `blocking` | ✅ resolved | ✅ **resolved** |
| **V-2** | `blocking` | `blocking` | ✅ **resolved in-line** |
| **V-5** | `warn` | 🔴 **raised to `blocking`** | ✅ **resolved** |
| **V-7** | `warn` | ✅ resolved | ✅ **resolved** |

**⇒ The blocking set is EMPTY at delivery.** Two of the three resolutions came from **querying the
filings' XBRL dimensions** rather than from the prose the plan expected them in.

## Three lessons this ledger records against itself

**1. V-1 was wrong once, and the error propagated.** An earlier draft concluded the AI operating
line was *"`DERIVED`, not disclosed"* on the strength of a **nominal supersession** — and pushed it
into 002's brief. **Phase 1 of 002 disproved it from the source.** *A supersession claim is itself
an evidence claim and needs the same page-level verification as any other. "Newer artifact wins" is
not a validation.*

**2. V-5's `blocking` status rested on a premise nobody checked.** Round 4 raised it to `blocking`
because the dilution was *"not determinable"* — a claim inherited from round 0. **It was
determinable, and had been since 2026-08-14.** *An inherited "unknown" is a claim, not a fact.*

**3. V-7's resolution was in the platform the whole time.** It was recorded as *"the extract does
not carry the percentages."* **They are a dimensional XBRL fact.** *"Not in the extract we read" is
not "not filed" — the same failure shape as plan finding F7, which wrongly concluded SPCX's
sub-segment cuts were unformable.*

## Items that are NOT in this queue and why

| Item | Where it lives |
|---|---|
| Payload denominators (Falcon 22.8 t, Electron 300 kg, Starship 100 t) | **002 P1** — consumed, never re-derived |
| F2's unsourced constants | **002 P2** |
| The universe-wide DA-23 census | **002 P3** |
| The DA-11 PUE restatement | **002 P4** — consumed by P3, never re-derived |
| The launch cost curve and the value-pool map | **003** — consumed, never re-derived |

## Disposition classes, kept distinct

| Class | Meaning | Remedy |
|---|---|---|
| `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | The disclosure does not exist anywhere | A **named external source** |
| `UNRESOLVABLE-FROM-PLATFORM` | The disclosure exists; the platform cannot reach it | A **read route or a tool fix** |
| **`NON-FORMABLE`** | The falsifier's inputs do not exist | **IS NOT `PASS`** (003's F16) — recorded, never marked passing |

## What is left unresolvable at delivery

| Item | Class | Named resolver |
|---|---|---|
| Aviation / maritime revenue splits | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | A product-or-service dimension finer than `EnterpriseAndGovernmentMember` |
| Grok vs compute within AI | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | A dimension inside `AISolutionsAndInfrastructureMember` |
| Subscribers / ARPU by channel | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | Subscriber disclosure for the managed channel |
| Segment-level capex | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | A segment capex aggregation |
| The constitution's ~$1.62T basis | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | The basis the anchor was struck on |
| **A forward DCF** | **Barred, not unresolved** | ≥3 years of positive FCF |

**Every one names the disclosure that would resolve it.** An item without a named resolver would be
a gap, not a bound.
