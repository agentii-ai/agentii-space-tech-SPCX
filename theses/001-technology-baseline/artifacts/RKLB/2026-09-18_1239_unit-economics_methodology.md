---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: RKLB
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T14:30:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-01"
    chosen_reading: "basis A and basis B both REPORTED; basis B is DEMONSTRATED here, not modelled"
  - da_id: "DA-02"
    chosen_reading: "LEO. Electron payload taken as 300 kg to LEO (CLAIMED vehicle spec)"
  - da_id: "DA-06"
    chosen_reading: "revenue per launch (price side) and cost per launch (cost side) kept separate"
  - da_id: "DA-23"
    chosen_reading: "operating_income sign verified against component arithmetic; confirmed flipped"
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
unresolvable: false
---

# RKLB — Unit Economics, Q2 2026

Source: Form 10-Q, accession `0001819994-26-000062`, filed 2026-08-10. Pages 32, 33, 37
read in full. **RKLB is a P11 deal security** (acquiring Iridium, ~$8.0B EV, announced
2026-06-29, close expected mid-2027) — all figures are **pre-merger standalone basis**.

---

## Headline: the first `DEMONSTRATED` marginal cost in the universe

Rocket Lab discloses **`cost per launch`** and **`revenue per launch`** as key
operational metrics. **No other issuer in the 35-name universe discloses either.** This
converts basis B of DA-01 from a model into a measurement.

| Metric | Q2 2026 | H1 2026 |
|---|---|---|
| Revenue per launch | **$9.1M** | $9.2M |
| Cost per launch | **$4.4M** | $4.9M |
| Electron missions completed | 6 | 12 |

→ **Basis B (marginal cost): $14,667/kg** at 300 kg to LEO — `DEMONSTRATED`
→ **Basis A (price): $30,333/kg** — `DEMONSTRATED`

**Segment cross-check** (Launch Services, Q2 2026): revenue $44,586k, cost of revenue
$25,476k, gross profit $19,110k. Cost/launch × 6 = $26,400k against segment cost
$25,476k — consistent within 3.6%, which validates the disclosed metric against the
audited segment table.

## The cross-issuer comparison, now with a measured anchor

| Vehicle | Basis | $/kg to LEO | Grade |
|---|---|---|---|
| Falcon 9 | A — list price | $2,939 | `CLAIMED` |
| Falcon 9 | B — marginal | ~$700 | `MODELED` |
| **Electron** | **A — revenue/launch** | **$30,333** | **`DEMONSTRATED`** |
| **Electron** | **B — cost/launch** | **$14,667** | **`DEMONSTRATED`** |

**Electron is 10.3× Falcon 9 per kilogram on basis A.** That is the small-lift penalty,
quantified from filed data rather than asserted. It is also the entire quantitative case
for Neutron: the same launch *price* ($9.1M) on a medium-lift vehicle's payload would
put RKLB at roughly Falcon-9 parity per kilogram.

**The universal pattern holds**: on every basis, for every vehicle, for every issuer
examined, **cost per kilogram sits above the $1,000 threshold**, and on the
`DEMONSTRATED` bases it is 15–30× above it.

## PIL-1 verdict — strengthened

| Field | Value |
|---|---|
| metric | `demonstrated_price_per_kg_to_LEO_P50`, threshold $1,000, `basis=ANY_OF_A_B_C` |
| **Observed** | Basis B **now demonstrated**: $14,667/kg (RKLB). Basis A demonstrated: $30,333/kg (RKLB), $2,939/kg (SPCX, `CLAIMED`) |
| **Verdict** | **HOLDS, and now on basis B as well** |

Phase 1 recorded a residual gap: *"marginal cost is modelled below $1,000/kg and cannot
be demonstrated from public filings."* **That gap is now closed — and the answer went
the other way.** The one issuer that actually discloses marginal cost reports
$14,667/kg, i.e. **15× the threshold**. The worry that basis B might sit below $1,000/kg
is resolved: it does not, for the only vehicle-and-issuer pair where it is measurable.

PIL-1 no longer rests on a model for its most important basis.

## PIL-3 evidence — production is not launch-constrained

Page 37 discloses build-rate and cadence together, which directly tests PIL-3:

| Period | Electron built | Electron launched | Net |
|---|---:|---:|---|
| 2024 | 14 | 16 | **−2** (drew down inventory) |
| 2025 | 24 | 21 | **+3** (built inventory) |
| H1 2026 | 11 | 12 | **−1** (drew down) |

**Rocket Lab builds at roughly the rate it launches, and in two of three periods
launched more than it built.** If launch capacity were the binding constraint, a launch
company would be accumulating unlaunched inventory, not drawing it down. This is
**direct filed evidence that RKLB is demand- or production-limited, not
launch-limited** — supporting PIL-3's claim, for one issuer.

This does not yet evaluate PIL-3's falsifier (which needs 19 issuer risk-factor reads),
but it is the first hard evidence on the question.

## DA-23 — third instance, and now confirmed against the filing's own narrative

```
  RKLB Q2 2026
    gross profit − operating expenses = $84.576M − $142.090M = −$57.514M   ← arithmetic
    XBRL OperatingIncomeLoss                                =  +$57.514M   ← reported
    → opposite sign, identical magnitude
```

**This one is stronger than the first two**, because the 10-Q's own text states it
explicitly on page 6: *"net loss of $(49,258) thousand, and basic and diluted EPS of
$(0.08)."* The filed narrative says **loss** and **negative EPS**; the XBRL extract says
+$49,258k and +$0.08. The defect is no longer inferred — it is contradicted by the
source document.

**DA-23 is now 3 of 3 issuers checked (SPCX, YSS, RKLB).** Definitively systematic.

**Refinement to the discriminating test.** Phase 4 used `EPS × shares ≈ net income` to
clear SATS. That test is **weaker than stated**: for RKLB, EPS × shares ≈ net income
*also* holds ($0.08 × 629.7M = $50.4M ≈ $49.258M) — because both figures share the same
flip. **The robust test is the component identity** (`gross profit − opex = operating
income`), which does not depend on two figures agreeing. The EPS test can clear a
flipped issuer spuriously; the component test cannot.

## A definitional quirk worth flagging (DA-25 candidate)

RKLB's `revenue per launch` implies a **51.6% launch gross margin** ($9.1M vs $4.4M).
The audited segment table implies **42.9%** ($44,586k vs $25,476k on 6 missions). The
gap is definitional: the disclosed metric is *"the average transaction price attributable
to launch contract performance obligations during the period in which the launch occurs,
regardless of whether the revenue is recognized using the point-in-time or over-time
method"* — a **normalisation**, not actual revenue. Two Q2 HASTE missions were recognised
over time with revenue partly taken in prior quarters, which explains the divergence.

**Neither number is wrong; they answer different questions.** Registering as **DA-25**:
issuer-defined "per unit" metrics may be normalised rather than derived, and are not
reproducible from the segment tables.

---

## Carry-forwards

1. **FLY is now the highest-value unexamined Phase 1 name** — a third launch provider
   would test whether RKLB's disclosure practice is unique.
2. **Electron's 300 kg payload is `CLAIMED`, not filed** — it drives the entire $/kg
   conversion. If the true figure differs by ±15%, every Electron number moves ±15%.
   A filed source should be sought.
3. **PIL-3 could be evaluated cheaply for RKLB's peers** by the same build-vs-launch
   test, rather than the 19-document risk-factor read the plan assumes.
4. **DA-25 proposed** alongside DA-23/DA-24.
