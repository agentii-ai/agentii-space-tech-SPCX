---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: YSS
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T16:05:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-12"
    chosen_reading: "constellation size — YSS is a manufacturer, not an operator; N/A"
  - da_id: "DA-13"
    chosen_reading: "production rate — searched for; YSS discloses revenue, not unit counts"
  - da_id: "DA-21"
    chosen_reading: "single reportable segment; no split available"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; YSS IS flipped (loss-maker)"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# YSS — Operational Baseline, Q2 2026

Source: Form 10-Q, accession `0001628280-26-056874`. Consolidated with the Phase 3
cross artifact, which introduced this company.

**Why YSS is the cleanest PIL-3 test case**: it **builds spacecraft and does not launch
them**. Launch availability is therefore an input it buys, not a capability it holds —
which isolates the manufacturing question from the launch question.

---

## 1. The finding that reframes PIL-3: a volume problem, not a unit-economics problem

| Metric | Q2 2026 | Q1 2026 | QoQ |
|---|---|---|---|
| Revenue | **$92.547M** | $116.343M | **−20.5%** |
| Cost of revenue | $70.367M | — | — |
| **Gross profit** | **$22.180M** | — | **24.0% margin** |
| Operating expenses | **$63.493M** | — | **68.6% of revenue** |
| R&D | $5.766M | $5.289M | +9.0% |
| Operating result | **$(41.313)M** | — | see DA-23 note |

**Gross margin 24.0% against an operating-expense ratio of 68.6%.** YSS does not lose
money because satellite manufacturing is unprofitable — **24% gross margin is a real,
positive manufacturing spread.** It loses money because its fixed cost base is **2.9×**
its gross profit.

**That distinction is the whole of PIL-3.** If satellites carry 24% gross margin at
sub-scale, then manufacturing *cost* is not the binding constraint on constellation
economics — manufacturing *volume* is. Those are different claims with different
remedies: a cost problem yields to engineering, a volume problem yields only to order
flow.

**And the quarter-over-quarter revenue decline (−20.5%) cuts against volume.** Revenue
fell sequentially while the cost base did not. One quarter is not a trend, but the
direction is unhelpful to the thesis and should be monitored rather than smoothed over.

## 2. DA-13 — production rate is not disclosed, in units, by anyone

Phase 3's plan called for the DA-13 distinction (manufactured vs launched vs
operational). This analysis searched for it and **YSS does not disclose unit counts** —
revenue only.

Combined with the earlier finding that RKLB discloses **build-rate and cadence
together** (14 built / 16 launched in 2024; 24 / 21 in 2025; 11 / 12 in H1 2026), the
position is:

| Issuer | Unit production disclosure |
|---|---|
| RKLB | **Yes** — vehicles built and launched, by period |
| YSS | **No** — revenue only |
| All 15 primes | Not examined; unlikely at segment granularity |

**So DA-13 is applicable to exactly one issuer.** Any cross-issuer manufacturing-rate
comparison is currently impossible, and PIL-3's evidence base is correspondingly thin —
it rests on RKLB's build-vs-launch series plus YSS's margin structure.

## 3. PIL-3 falsifier — still not evaluated, but now better scoped

| Field | Value |
|---|---|
| metric | `share_of_named_issuers_citing_launch_availability_as_primary_delay_cause` |
| threshold | 0.5, op `>` |
| **Observed** | **not measured** |
| **Verdict** | **PENDING** |

**Two cheaper paths have emerged than the 19-document risk-factor read the plan assumes:**

1. **The build-vs-launch test** (used successfully on RKLB) works on any issuer that
   discloses both. It is a *behavioural* measure and does not require reading prose.
2. **YSS's margin structure** is a second indirect test: a manufacturer at 24% gross
   margin with a 2.9× fixed-cost multiple is volume-constrained by arithmetic, whatever
   its filings say about delays.

Both are cheaper and less subjective than coding risk-factor language. The falsifier
should be re-scoped in `plan.md` to use them.

## 4. DA-23 — YSS is one of the four flipped issuers

```
gross profit − operating expenses = $22.180M − $63.493M = −$41.313M
XBRL OperatingIncomeLoss                                =  +$41.313M
```

**YSS is flipped**, consistent with the rule that the extract strips signs on negative
values. Its **positive** Q1 figure ($110.466M against $116.343M revenue — a 95%
"margin", which is itself implausible) is worth a separate check; if Q1's true operating
result is also a loss, the Q1 magnitude differs from the pattern and should be verified
against that filing's components directly.

**Flagged, not asserted**: Q1 was not examined at component level in this pass. The
recorded rule stands on 12 issuer-quarters with no exceptions, but Q1/YSS is a
plausible weak point and is listed here so it is not assumed clean.

---

## Carry-forwards

1. **PIL-3's evidence is thin and should be declared so**: one issuer with unit data
   (RKLB), one with margin structure (YSS), and a falsifier not yet measured.
2. **YSS Q1's $110.5M operating figure needs a component check** — it sits outside the
   pattern's magnitude and may be a different defect class.
3. **PIL-3's falsifier should be re-scoped** in `plan.md` toward the build-vs-launch and
   margin-multiple tests rather than risk-factor prose coding.
4. **YSS revenue fell 20.5% QoQ** — carry into Phase 6 as a demand-side signal against
   the volume-constraint reading.
