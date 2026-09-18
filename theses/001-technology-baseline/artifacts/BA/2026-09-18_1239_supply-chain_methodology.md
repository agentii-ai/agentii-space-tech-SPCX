---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: BA
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T17:40:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "Boeing's own segment definitions; Spectrolab is not a reportable segment"
  - da_id: "DA-23"
    chosen_reading: "operating_income checked; BA is a PROBABLE but UNVERIFIED instance (see §3)"
  - da_id: "DA-16"
    chosen_reading: "Spectrolab capacity and share are CLAIMED; no segment disclosure exists"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# BA — Supply-Chain Position (Solar Cells)

Source: Form 10-Q, accession `0001628280-26-050038` (Q2 2026, quarter ended 2026-06-30).

**Why BA matters to PIL-3**: via **Spectrolab**, it owns one leg of the **two-supplier
duopoly** in space-grade solar cells — the component whose efficiency is the first term
in constitution bound **F1**, required by every satellite.

---

## 1. The duopoly is structural and unpriced — the core PIL-3 supply finding

| Supplier | Owner | Ticker |
|---|---|---|
| SolAero Technologies | Rocket Lab | RKLB |
| Spectrolab | Boeing | BA |

**Two suppliers for a component every satellite needs**, and one leg sits inside a launch
competitor. That is a genuine structural finding about the sector's bottleneck.

**But it is entirely unpriced.** Boeing does not report Spectrolab as a segment, discloses
no space-solar revenue, and the 10-Q's only segment detail at this granularity is
Commercial Airplanes geography. **The duopoly's pricing power is unmeasurable from public
filings** — a candidate for `UNRESOLVABLE-FROM-PUBLIC-SOURCES` if a later phase tries to
quantify it.

**Boeing's scale makes the invisibility structural, not accidental:**

| Metric | Q2 2026 |
|---|---|
| Revenue | **$24,560M** |
| Operating income | **$156M** |
| Operating margin | **0.6%** |
| R&D (H1) | $1,824M |

Spectrolab would need to be a multi-billion-dollar business to register against a $24.6B
quarterly revenue base. **It is the sixth instance of the "capability real, business
immaterial" pattern** — and here the immateriality is guaranteed by the parent's size
rather than by the unit's smallness.

## 2. Boeing is a demand-side signal, not a supply-side one

Boeing's **0.6% operating margin** reflects commercial aerospace, not space. But it has a
PIL-3 consequence worth noting: a prime operating at 0.6% has **no capacity to fund
supply-chain expansion**. The solar-cell duopoly cannot be relieved by its own owners
investing through a downturn — Boeing has no margin to invest from, and RKLB is itself
loss-making. **Both duopoly legs are financially constrained**, which is a structural
argument that the F1 supply bottleneck will persist.

## 3. BA is a CONFIRMED fifth DA-23 instance — and the census is incomplete

> **RESOLVED 2026-09-18.** The candidate recorded below was **verified against Boeing's
> filed 10-Q** (accession `0000012927-24-000082`, filed 2024-10-23) and is now
> **CONFIRMED**. See §3a. The candidate reasoning is retained below for the audit trail.

### 3a. Confirmation

Boeing's own statement of comprehensive income reports:

| | Nine months to 2024-09-30 | **Three months to 2024-09-30** |
|---|---:|---:|
| **Net loss** | **$(7,968)M** | **$(6,174)M** |

The platform reports Q3 2024 operating income as **+$5,761M**. The test:

| Hypothesis | Below-the-line items required to reconcile to −$6,174M | Verdict |
|---|---:|---|
| Operating income = **+$5,761M** | **−$11,935M** | **Implausible** — Boeing's interest expense runs ~$2B/quarter, not $12B |
| Operating income = **−$5,761M** | **−$413M** | **Entirely plausible** — interest and tax on a $6.2B loss |

**Verdict: Boeing's Q3 2024 operating income was a LOSS of $5,761M, reported by the
extract as +$5,761M.** DA-23 confirmed.

**Census: 5 of 5 loss-making issuers confirmed sign-stripped** (SPCX, YSS, RKLB, FLY, BA),
against 8 of 8 profitable issuers clean.

**The consequence is larger than one more name.** Earlier passes reported "12
issuer-quarters, zero exceptions" — **that figure was a floor, not a census.** The
extract's defect scope is **unknown**, and Boeing is a $24.6B/quarter issuer with
multiple quarters affected. Every remaining Phase 3 prime — the 11 untouched names — is
an unchecked candidate.

**Methodological note**: this instance was caught by **margin plausibility against
industry norms** (a 32% Boeing operating margin is impossible), not by the component
identity, which needs quarterly gross profit the extract does not carry. **The second
detector worked where the first was unavailable** — which is the argument for running
both.

---

### 3b. The candidate reasoning (retained for audit)

Checking Boeing's reported operating margins across quarters surfaces two that are not
credible:

| Period | Revenue $M | Op income $M | Margin |
|---|---:|---:|---:|
| 2024 Q1 | 16,569 | 86 | 0.5% |
| 2024 Q2 | 16,866 | 1,090 | 6.5% |
| **2024 Q3** | **17,840** | **5,761** | **32.3%** ← implausible |
| 2024 Q4 | 66,517 | 10,707 | 16.1% |
| 2025 Q1 | 19,496 | 461 | 2.4% |
| 2025 Q2 | 22,749 | 176 | 0.8% |
| **2025 Q3** | **23,270** | **4,781** | **20.5%** ← implausible |
| 2025 Q4 | 89,463 | 4,281 | 4.8% |
| 2026 Q1 | 22,217 | 448 | 2.0% |
| 2026 Q2 | 24,560 | 156 | 0.6% |

**Boeing has never earned a 20%+ operating margin.** If the true 2024 Q3 figure is a
**loss** of ~$5.8B, the margin is −32.3% — which fits Boeing's 2024 (strike, 737 MAX
groundings) far better than +32.3% does.

**Why the component identity could not settle it** (and why §3a was needed): gross
profit − opex = operating income **cannot be run** for BA — the extract carries no
quarterly gross profit, and the H1 aggregate reconciles fine ($4,960M − $4,449M = $511M
against a reported $604M, a $93M gap attributable to other operating items). The
**confirmation came instead from the net-loss reconciliation**: a $6,174M quarterly net
loss is arithmetically incompatible with a $5,761M operating *gain*.

**Two implications, both now confirmed:**

1. **DA-23's scope is wider than four issuers — at least five, census unknown.** The 11
   untouched Phase 3 primes are all unchecked candidates.
2. **The component identity is not always available**, so a second detector is required.
   **Margin plausibility against industry norms** caught both BA quarters; it is a
   judgement rather than an identity, but it is the only tool that works when quarterly
   gross profit is absent — and here it produced a confirmation.

**2025 Q3 remains unverified** (20.5% margin, also implausible). The 2024 Q3 instance is
confirmed; the 2025 Q3 instance is by extension very likely but has not been reconciled
against that quarter's net loss.

## 4. What the artifact does not establish

- **No space revenue for Boeing** is isolated or disclosed. Its Tier 3 role is via
  Spectrolab, which is invisible.
- **No solar-cell capacity or price data** exists publicly for either duopoly leg.
- **PIL-3 is not advanced** by this artifact beyond confirming the duopoly structure and
  that both legs are financially constrained.

---

## Carry-forwards

1. **BA 2024 Q3 / 2025 Q3 must be verified against the filed statements.** This is now
   the highest-priority data-integrity task in the thesis — it bounds DA-23's scope.
2. **A second DA-23 detector is needed** (margin-vs-industry-norm), because the component
   identity requires quarterly gross profit the extract does not always carry.
3. **The solar-cell duopoly is confirmed structural and confirmed unpriced.** Phase 3
   should stop trying to price it from filings and record it as a structural finding.
4. **Both duopoly legs are financially constrained** (BA 0.6% margin, RKLB loss-making) —
   a supply-side argument that the F1 bottleneck persists.
