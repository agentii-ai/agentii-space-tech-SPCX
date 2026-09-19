---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: YSS
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T13:40:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-18
definitions_used:
  - da_id: "DA-08"
    chosen_reading: "launch counts restated — YSS is not a launch provider, so no restatement applies"
  - da_id: "DA-13"
    chosen_reading: "production rate — manufactured vs launched vs operational reported separately where disclosed"
  - da_id: "DA-21"
    chosen_reading: "each prime's own segment definition; no cross-prime aggregation attempted"
  - da_id: "DA-23"
    chosen_reading: "operating_income sign verified against component arithmetic, never taken from XBRL alone"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# Phase 3 — Production and Supply (PIL-3)

**Purpose**: test whether the binding constraint on constellation economics is
manufacturing rate or launch availability; map the supply chain for critical
sub-components.

**Status: partially executed.** The YSS operating baseline and the DA-23 finding are
complete. The PIL-3 falsifier itself — the share of issuers citing launch availability
as the primary delay cause — is **not evaluated**, because it requires reading risk
factors and MD&A across 15 primes. Flagged below rather than faked.

---

## YSS — the satellite-manufacturing benchmark

York Space Systems is the cleanest listed read on satellite manufacturing unit
economics: it builds spacecraft and does not launch them. Q2 2026 (10-Q, accession
`0001628280-26-056874`):

| Metric | Q2 2026 | Note |
|---|---|---|
| Revenue | $92.547M | |
| Cost of revenue | $70.367M | |
| **Gross profit** | $22.180M | **gross margin 24.0%** |
| Operating expenses | $63.493M | **68.6% of revenue** |
| Operating result | **$(41.313)M** loss | see DA-23 note |
| R&D | $5.766M | 6.2% of revenue |

**The structural fact**: gross margin of 24.0% against an operating-expense ratio of
68.6%. YSS loses money not because manufacturing is unprofitable — 24% gross margin is a
real, positive manufacturing spread — but because the fixed cost base is 2.9× the gross
profit. This is a **scale problem, not a unit-economics problem**, and it is the
signature of a manufacturer below minimum efficient scale.

That distinction matters for PIL-3. If satellites carry a 24% gross margin at sub-scale,
then manufacturing *cost* is not the binding constraint — manufacturing *volume* is.
Those are different claims with different remedies.

**Caveat**: Q2 2026 includes the All.Space acquisition (agreed 2026-04-29), so the
operating-expense ratio may be inflated by deal costs. Segment-level confirmation was
not available from the XBRL extract — carried forward.

## The critical sub-component: a two-supplier market

PIL-3's specific claim was that critical sub-components, not launch, gate deployment.
The clearest case is **space-grade solar cells**:

| Supplier | Owner | Ticker |
|---|---|---|
| SolAero Technologies | Rocket Lab | RKLB |
| Spectrolab | Boeing | BA |

**Two suppliers, both inside the 35-name universe, for a component every satellite
requires** — and whose efficiency is the first term in constitution bound **F1**. An
industry planning constellations in the thousands is buying its solar cells from a
duopoly where one leg is a subsidiary of a launch competitor.

That is a genuine structural finding, but note the honest limitation: **this is a
structural observation, not a priced one.** Neither RKLB nor BA discloses SolAero or
Spectrolab revenue separately, so the duopoly's pricing power is unmeasurable from
public filings. It is a candidate for `UNRESOLVABLE-FROM-PUBLIC-SOURCES` if a later
phase tries to quantify it.

## DA-23 — the XBRL sign trap is systematic, not incidental (upgraded finding)

Phase 1 found `OperatingIncomeLoss` sign-flipped for SPCX. This phase found the **same
defect in YSS**, verified by independent arithmetic rather than narrative:

```
  YSS Q2 2026
    gross profit − operating expenses  =  $22.180M − $63.493M  =  −$41.313M   ← arithmetic
    XBRL OperatingIncomeLoss                                  =   +$41.313M   ← reported
    → opposite sign, identical magnitude

  SPCX Q2 2026
    segment sum: −542 + −1,257 + 1,656                        =  −$143M       ← arithmetic
    XBRL OperatingIncomeLoss                                  =   +$143M      ← reported
    → opposite sign, identical magnitude
```

**2 of 2 issuers checked.** The magnitude matches exactly in both cases, which rules
out a transcription error and points to a systematic sign convention in the extraction
pipeline.

**Consequence**: any screen of the form `operating_income > 0` over this universe will
classify loss-making issuers as profitable. Both SPCX and YSS would be misclassified.
**Every artifact in this thesis must verify `operating_income` against component
arithmetic and never take the XBRL value alone.** This is now a hard rule, not a note.

This substantially strengthens the **DA-23** amendment candidate: it is no longer
"one issuer looked odd" but a reproducible, twice-confirmed platform defect.

## PIL-3 falsifier — NOT evaluated

| Field | Value |
|---|---|
| metric | `share_of_named_issuers_citing_launch_availability_as_primary_delay_cause` |
| threshold | 0.5, op `>` |
| source | `10-Q_risk_factors_and_MD&A` |
| **Observed** | **not measured** |
| **Verdict** | **PENDING** — carried to Phase 3 continuation, not `UNRESOLVABLE` (the disclosure exists; it simply has not been read) |

**What it needs**: risk-factor and MD&A text for the 15 primes plus YSS, PL, LUNR,
KRMN, VOYG — searching for delay-cause language, then coding each issuer as
launch-gated or production-gated. That is a bounded, mechanical task requiring document
reads this phase did not perform.

**Do not read this as the pillar holding or failing.** PIL-3 is currently untested.

---

## Corrections and carry-forwards

1. **PIL-3 is untested** — the falsifier needs ~19 issuer document reads. This is the
   single largest remaining Phase 3 task.
2. **YSS's 68.6% opex ratio may be acquisition-distorted** — needs segment confirmation.
3. **The solar-cell duopoly is structural, not priced** — no separate revenue disclosure
   exists for SolAero or Spectrolab.
4. **DA-23 upgraded** from a Phase 1 curiosity to a twice-confirmed systematic defect
   affecting any `operating_income` screen. Recommend promoting it in the next
   constitution amendment round alongside F5a/F5b.
5. **DA-13 remains open**: YSS reports revenue, not unit counts. No listed
   satellite manufacturer in the universe discloses production rate in units, so the
   "manufactured vs launched vs operational" distinction cannot yet be applied.
