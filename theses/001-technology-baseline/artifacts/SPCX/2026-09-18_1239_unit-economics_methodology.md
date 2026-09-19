---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: SPCX
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T12:39:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"   # no corpus-version endpoint exposed by the platform; see brief.md
definitions_used:
  - da_id: "DA-01"
    chosen_reading: "ALL THREE REPORTED — A, A', B, C. No basis is adopted as 'the' answer."
  - da_id: "DA-02"
    chosen_reading: "LEO. Falcon 9 figures restated to LEO; GTO not used."
  - da_id: "DA-06"
    chosen_reading: "price and cost reported separately, never conflated"
evidence_grade: MODELED
deal_security_basis: not_applicable
unresolvable: false
---

# Phase 1 — Launch Cost Baseline (PIL-1)

**Purpose**: build the DA-01 definitional table for cost per kilogram to LEO, per the
§1c standing rule — enumerate every competing basis, report all, and treat the spread
as the finding.

**Headline result**: the three bases span **~$500/kg to ~$6,600/kg** — a spread of
roughly **7–13×** around a single Falcon 9 mission. Quoting any one of them as "the
cost per kilogram to orbit" is therefore not a simplification; it is a different claim.

---

## DA-01 — the four bases compared

All figures are SPCX Q2 2026 unless marked. Payload denominator: **22.8 t to LEO**
(Falcon 9 reusable, `CLAIMED` — published vehicle spec, not in any filing).

| Basis | What it measures | Q2 2026 figure | Per kg | Grade |
|---|---|---|---|---|
| **A** — customer list price | Published price an external customer pays | ~$67M per Falcon 9 launch | **~$2,939/kg** | `CLAIMED` |
| **A'** — realized revenue per customer launch | Space segment revenue ÷ customer launches | $962M ÷ 10 = **$96.2M** | ~$4,220/kg | `DEMONSTRATED` (figures) / `MODELED` (the division) |
| **B** — marginal cost per launch | Propellant + expended stage + range + refurbishment | **~$12–20M** | **~$525–875/kg** | `MODELED` |
| **C** — fully-loaded segment cost | Space segment total costs ÷ customer launches | $1,504M ÷ 10 = **$150.4M** | **~$6,596/kg** | `DEMONSTRATED` (figures) / `MODELED` (the division) |

### Source detail

**A' input** — `DEMONSTRATED`. Space segment revenue $962M, customer launches 10,
Q2 2026 (10-Q, accession `0001628280-26-052535`, p35 and p42).
**Important caveat**: Space segment revenue includes *Launch and Development*
government contracts with terms up to 14 years, not merely launch services. A' is
therefore an **upper bound** on a launch price, not a price. Restating it to launch
services alone is not possible from public disclosure — this is DA-21 in operation
(issuer-defined segment boundaries).

**C input** — `DEMONSTRATED`. Space segment costs Q2 2026: cost of revenue $329M +
R&D $1,076M + SG&A $99M = **$1,504M** (10-Q p42). Segment operating loss $(542)M.

**B inputs** — `MODELED`, from physics and public cost references:

| Component | Value | Basis |
|---|---|---|
| Propellant | ~$0.36M | Falcon 9 ~485 t (RP-1/LOX), blended ~$0.75/kg. Compare Starship: ~4,600 t at $1–2/kg = $4.6–9.2M |
| Expended second stage | ~$8–12M | **Not recovered.** The dominant term |
| Range and launch operations | ~$2–5M | Range fees, recovery vessel, ground ops |
| Booster refurbishment | ~$1–3M | Between-flight inspection and refurb |
| **Total** | **~$12–20M** | |

---

## Finding 1 — the spread is the finding (why DA-01 exists)

```
  B  ~$525–875/kg   ← marginal cost, the physics floor
  A  ~$2,939/kg     ← list price          (3.4–5.6× B)
  A' ~$4,220/kg     ← realized revenue    (4.8–8.0× B)
  C  ~$6,596/kg     ← fully-loaded        (7.5–12.6× B)
```

A reader told "SpaceX launches cost about $3,000/kg" and a reader told "$6,600/kg"
hold the same stock and disagree about its economics by a factor of two. A reader told
"marginal cost is $500/kg" believes Starship is already obsolete. **All three statements
are supportable from the same filing.** The §1c rule exists precisely because this
spread is load-bearing, not cosmetic.

---

## Finding 2 — F5 needs refinement: the floor's *composition* depends on reuse architecture

The constitution's **F5** states that a propellant floor exists which reusability does
not remove. That is correct for a **fully reusable** vehicle and **materially
incomplete for a partially reusable one**:

| Architecture | Binding marginal-cost term | Propellant share of marginal cost |
|---|---|---|
| **Fully reusable** (Starship) | Propellant | ~100% — nothing else is consumed |
| **Partially reusable** (Falcon 9) | **The expended second stage** | **~2–3%** |

Falcon 9's propellant is roughly **$0.36M against a ~$12–20M marginal cost**. The floor
for a partially reusable vehicle is therefore set by *manufacturing cost of the
expendable stage*, which falls with production learning — **not** by propellant, which
does not fall at all.

**Consequence**: the F5 propellant argument proves sub-$10/kg is impossible *for
Starship-class fully reusable vehicles*. It does **not** bound Falcon-class vehicles,
whose floor is a manufacturing curve and could in principle keep falling. The
constitution's F5 should be split into F5a (fully reusable: propellant floor, hard) and
F5b (partially reusable: upper-stage manufacturing floor, soft). Flagged as a
constitution amendment candidate — **not executed here**, since amending the
constitution is a human approval, not an artifact write.

---

## Finding 3 — the R&D burden and what "customer launch" excludes

Space segment R&D of **$1,076M** is **3.3× the segment's cost of revenue** ($329M), and
is driven by Starship development (+55.3% YoY). Two consequences:

1. **Basis C is Starship-subsidized.** The $6,596/kg fully-loaded figure is inflated by
   a development programme that belongs to a future vehicle. An analyst arguing "SpaceX
   loses money on every launch" and one arguing "SpaceX is profitable per launch" can
   both cite the filing — the difference is whether Starship R&D is assigned to Falcon
   missions.
2. **DA-08 in operation.** SPCX flew **37 Falcon launches in Q2 2026** but classified
   only **10** as customer launches — the other **27** were internal Starlink
   deployments, which generate no inter-segment revenue by design. Any cross-issuer
   "launches" comparison that does not restate for this is invalid.

---

## Data-quality note — an XBRL sign-convention trap

`get_company_financials(SPCX)` returns `OperatingIncomeLoss: +143,000,000` — a
**positive** $143M. The consolidated figure is actually an operating **loss** of $143M.
Verification: the three segments sum to −542 (Space) + −1,257 (AI) + 1,656 (Connectivity)
= **−143**, and the 10-Q narrative reports a net loss of $541M.

**This is a live trap.** An analyst screening on "operating income > 0" would classify
SPCX as profitable. The sign convention in the platform's income-statement extract is
not reliable for loss-making issuers; narrative and segment reconciliation must be
cross-checked. Registered as a candidate DA class — the metric `operating_income` is
itself ambiguous in sign convention across sources.

---

## PIL-1 falsifier evaluation

| Field | Value |
|---|---|
| metric | `demonstrated_price_per_kg_to_LEO_P50` |
| threshold | 1000 |
| basis | `ANY_OF_A_B_C` |
| **Observed** | A ≈ $2,939 · A' ≈ $4,220 · B ≈ $525–875 · C ≈ $6,596 |
| **Verdict** | **HOLDS** on A, A' and C. **NOT EVALUABLE on B** — basis B is `MODELED`, not `demonstrated`, and no issuer discloses marginal cost |

**Read carefully**: the falsifier says *demonstrated* price. On basis B the value sits
**below** the $1,000 threshold — but it is our model, not a demonstration. Under P4,
`MODELED` cannot satisfy a falsifier. So PIL-1 **holds**, and the honest statement is:
*prices are demonstrated above $1,000/kg on every disclosed basis; marginal cost is
modelled below it and cannot be demonstrated from public filings.*

That gap — between a demonstrable price and a non-demonstrable cost — is the single
most important structural fact about launch economics. It is also a candidate
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` case for the *cost* half of the question: no issuer
discloses marginal cost per launch, and none is likely to.

---

## Next actions (Phase 2 hand-off)

1. RKLB and FLY unit economics not yet built — needed to test whether the A/B/C spread
   is SpaceX-specific or sector-wide.
2. Basis B needs a defensible public anchor. Candidate: NASA CRS/Commercial Crew
   contract values as a revealed-price floor.
3. F5a/F5b split flagged for constitution amendment.
4. `operating_income` sign convention proposed as DA-23.
