---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-5"
ticker: SPCX
skill: risk
mode: regulatory-compliance-risk-assessment
generated_at: 2026-09-19T12:50:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "953fc5d396e7"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-24"
    chosen_reading: "Where a regulatory event is described in prose differently from its accounting treatment, the FILED accounting wins and the prose is reported as a separate claim. The SATS Q3 2025 event is the registered instance: a non-cash impairment charge, not a gain."
entity_claims:
  - claim_id: "rr-echostar-instalments"
    ticker: SPCX
    metric: spectrum_instalment_obligation
    value: 856000000
    unit: USD
    basis: "EchoStar spectrum instalments; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "001/artifacts/SPCX/2026-09-18_2310_operational-kpi §5 — consumed"
key_metrics:
  echostar_spectrum_instalments_usd_m: 856
---

# SPCX × risk × regulatory-compliance-risk-assessment

**One significant regulatory exposure, one bound, and one thing that is not a regulatory risk.**

## 1. R-1 — The EchoStar spectrum obligation, and the licence-holder's terminal condition

**$856M of EchoStar spectrum instalments** on SPCX's balance-sheet obligations.

**The exposure is not the instalment — it is the counterparty's trajectory.** SATS is buying AWS-4
and H-Block to SpaceX for **~$20bn, up to $11bn of it in SpaceX Class A at $212/share**. So:

- **SPCX is paying instalments on spectrum it is simultaneously acquiring the licence-holder for.**
- **SATS' own operating satellite business is ~$0.3bn** against **≈$42.65bn** of regulatory-asset
  realisation — the **≈142×** figure 003's map derived. **Launch cost is not a variable in the
  transaction that realises the value.**
- **The disposal gain or loss is `UNRESOLVABLE-FROM-PUBLIC-SOURCES` until closing**, because it is
  determined at closing on a basis different from the current statements.

**⇒ The regulatory risk is a CONSOLIDATION risk, not a compliance risk.** If the transaction closes,
SPCX's instalment obligation and its consideration are the same transaction viewed twice — and the
**$856M must not be treated as an arm's-length payable to a third party.**

## 2. R-2 — The 1M-satellite filing: regulatory status is not a valuation input

**Two separate questions, and only one of them is P5's:**

| Question | Answer |
|---|---|
| Is the orbital filing **regulatorily** live? | **Not assessed here.** It is a filed aspiration, and its ITU/FCC status is **not a valuation input** under A4/P10 |
| May the anchor price it? | **No.** A4 bars valuing terrestrial and orbital compute as one; **P10's five conditions are not met** |

**⇒ Recorded so the two are not conflated.** "The filing exists" is not "the revenue is coming", and
it is also not "the filing is a regulatory risk". **It is inadmissible — which is a statement about
the anchor, not about the regulator.**

## 3. R-3 — Index inclusion: a dated catalyst, never a standing assumption

**The constitution records NO index inclusion at ratification.** Therefore:

- **The marginal buyer of the equity that funds the build is a DATED CATALYST.** P5 must record it
  as such **or drop it** — there is no third option
- **Float structure rides on the same pillar.** Post-IPO equity moved **2,573 → 127,224 (49.5×)**,
  so the float that would enter an index is a post-IPO artefact, not a historical one

**Why this is a risk and not an opportunity:** an anchor that assumes index inclusion **prices a
buyer who has not arrived.** The `market_data_stage_regresses` expiry trigger covers the adjacent
case (the live feed stopping); **there is no trigger for an inclusion that never happens**, which is
why the item is carried as a *dated catalyst with no date* rather than as an assumption.

## 4. What is NOT a regulatory risk — stated for exhaustiveness

| Candidate | Why not |
|---|---|
| **Launch licensing** | SPCX's cadence is filed and current; a licensing constraint would appear as a cadence break, **which the DA-08 series would show** |
| **Spectrum at SPCX's own Connectivity segment** | The segment is filed and operating. **The regulatory exposure in this thesis is EchoStar's, not SPCX's** |
| **CFIUS / P11 gates** | **P11 deal securities are IRDM, GSAT and RKLB — not SPCX.** SPCX is an acquirer here, and its own gate exposure is not registered |

## 5. Register

| # | Item | Class | Binds? |
|---|---|---|---|
| **R-1** | EchoStar instalments **$856M** | **Consolidation, not compliance** | ⚠️ Must not be treated as an arm's-length payable |
| **R-2** | 1M-satellite filing | **Admissibility bound (A4/P10)** | ✅ Not a regulatory risk — an anchor limit |
| **R-3** | Index inclusion / float | **Dated catalyst** | ⚠️ Must be dated or dropped; post-IPO float is 49.5× |
