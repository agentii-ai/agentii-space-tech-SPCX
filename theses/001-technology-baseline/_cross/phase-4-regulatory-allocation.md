---
thesis_id: "001-technology-baseline"
pillar: PIL-6
ticker: SATS
skill: risk
mode: regulatory-compliance-risk-assessment
generated_at: 2026-09-18T14:05:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-18
definitions_used:
  - da_id: "DA-17"
    chosen_reading: "spectrum quantified as transaction value ($), not MHz or MHz-pop — the only basis disclosed"
  - da_id: "DA-18"
    chosen_reading: "regulatory approval = FCC licence transfer completed; ITU coordination not separately confirmed"
  - da_id: "DA-22"
    chosen_reading: "the $19.6B EchoStar mark is a signed-transaction value, CLAIMED-source but contract-confirmed"
  - da_id: "DA-23"
    chosen_reading: "sign convention verified per issuer; SATS checked and cleared"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# Phase 4 — Regulatory Allocation (PIL-6)

**Purpose**: test whether orbital, spectral and launch-licence access are genuinely
finite allocated resources with a real market price — the premise the human added as
Pillar 6 at Clarification Q-2.

**Headline result**: the premise holds, and it is quantifiable. EchoStar recognised
roughly **$27B of gains across 2025 H2 from selling spectrum licences** — against
**$15.0B of full-year 2025 revenue**. A regulatory asset that produced no operating
revenue was worth more than the entire operating business that held it.

---

## The reference transaction, quantified

The SPCX–EchoStar deal (~$19.6B for AWS-4, H-Block and AWS-3 licences, FCC-approved,
transfer closed) was already recorded as the sector's pricing mark. EchoStar's own
financials now size the *gain*:

| Period | Revenue | Operating income | op/rev | Net income |
|---|---|---|---|---|
| 2025 Q1 | $3,869.8M | $88.1M | 2.3% | n/a |
| 2025 Q2 | $3,725.0M | $213.4M | 5.7% | n/a |
| **2025 Q3** | **$3,614.3M** | **$16,641.9M** | **460.5%** | $12,781.2M |
| **2025 Q4** | **$15,005.0M** | **$17,723.1M** | **118.1%** | $14,497.2M |
| 2026 Q1 | $3,667.5M | $392.8M | 10.7% | $146.9M |

**Q3 2025 operating income was 4.6× revenue.** No telecom operator earns that. The
quarterly progression is unmistakable: 2.3% → 5.7% → 460.5% → 118.1% → 10.7%. Two
quarters carry the spectrum gain; the rest are the actual operating business at
**2–11% operating margin**.

**The comparison that matters**: ~$27B of combined 2025 H2 gain, against $15.0B of
full-year 2025 revenue. **The licences were worth roughly 1.8× the annual revenue of
the business that held them** — and they generated no revenue of their own.

This is the empirical answer to PIL-6's premise. The resource is finite, allocated by
regulators before capital can be deployed, and it has a market price that can be
realised independently of any operating business.

## PIL-6 chain of reasoning, and where it stops

The pillar claims: allocation precedes deployment → a licensed position is an asset →
the asset has a price → therefore it is a moat *and* a dated catalyst.

EchoStar confirms the middle links. Two caveats must travel with it:

1. **This is a sell-side observation, not a buy-side one.** EchoStar realised value by
   *exiting* spectrum. The pillar's investment claim is that holding a licensed
   position is a durable asset — that is supported by the price, but not by this
   company, which demonstrates the exit.
2. **The gain is a `CLAIMED`-grade inference.** The $27B is derived from GAAP operating
   income whose classification the filing does not break out at this granularity. The
   direction is certain; the exact figure is `MODELED`.

## DA-24 (new) — "operating income" contaminated by asset-sale gains

EchoStar's 2025 Q3/Q4 operating income is **not operating**. A spectrum-licence sale
was classified such that it flows through the operating line, producing margins of 460%
and 118%. Any screen, ranking or comparison using SATS's operating income compares a
licence sale against operating businesses.

**Candidate registration as DA-24** — distinct from DA-23 (sign convention) because the
defect is *classification*, not sign. Both have the same consequence: `operating_income`
must be verified against components before use. **This now covers three issuers via two
mechanisms**, and the operational rule is the same for both.

## A near-miss worth recording

I initially suspected SATS was a **third DA-23 instance** — the 460% margin looks like
exactly the sort of nonsense a sign flip produces. It is not. The discriminating test:

| Issuer | Test | Result |
|---|---|---|
| SPCX | segment sum vs XBRL operating income | **disagree in sign** → DA-23 |
| YSS | gross profit − opex vs XBRL operating income | **disagree in sign** → DA-23 |
| SATS | EPS × shares vs reported net income | **agree to 0.3–0.5%** → **not** DA-23 |

**The rule this yields**: an implausible-looking financial figure must be tested against
a *different* internal relationship before being labelled a data defect. SATS passed
that test, so it is evidence for PIL-6 rather than a data-quality finding. Recording the
near-miss because the same impulse will recur across this universe.

## PIL-6 falsifier — NOT evaluated

| Field | Value |
|---|---|
| metric | `new_entrant_primary_spectrum_or_slot_grant_without_incumbent_acquisition` |
| threshold | 0, op `>` |
| source | `FCC_IBFS_or_ITU_Space_Network_List` |
| **Observed** | **not measured** |
| **Verdict** | **PENDING** — requires FCC IBFS and ITU Space Network List queries, neither of which the platform provides |

**Note a real limitation**: this falsifier's sources are **outside the platform**. The
agentii toolset covers SEC filings, XBRL, transcripts and market data — it has no FCC or
ITU access. PIL-6's falsifier may therefore be permanently `UNRESOLVABLE-FROM-PLATFORM`
and require an external data source. That is a stronger statement than
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` (the data is public; we simply cannot reach it) and
should be registered as such if it persists.

---

## Corrections and carry-forwards

1. **PIL-6's premise is supported** by the strongest single datapoint in the thesis so
   far — but by a *seller*, not a holder. A buy-side confirmation would need a licensee
   that has kept and monetised spectrum — IRDM is the candidate.
2. **DA-24 proposed** (asset-sale contamination) alongside DA-23 (sign convention). Both
   resolved by the same operational rule.
3. **PIL-6 falsifier is likely platform-unreachable** — flag for the next amendment
   round as a new disposition class.
4. **IRDM has not been examined.** It is the universe's only profitable LEO operator
   *and* it holds licensed L-band spectrum — the correct buy-side test of PIL-6, and now
   the highest-value unexamined name in the thesis.
