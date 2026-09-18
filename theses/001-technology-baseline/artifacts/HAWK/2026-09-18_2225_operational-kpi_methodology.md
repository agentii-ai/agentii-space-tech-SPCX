---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: HAWK
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T22:25:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income UNVERIFIABLE — HAWK is a CANDIDATE; the extract is internally inconsistent post-IPO"
  - da_id: "DA-26"
    chosen_reading: "cannot be evaluated — only two periods present, both post-IPO"
  - da_id: "DA-28"
    chosen_reading: "NEW CANDIDATE — capital-structure discontinuity around an IPO invalidates share-count-based detectors"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# HAWK — Operating Baseline

Source: Form 10-Q, accession `0001750704-26-000022` (Q2 2026, quarter ended 2026-06-30).

**⚠️ This artifact reports a data-integrity finding, not an operating baseline.** HawkEye
360's extract cannot support a ratio analysis, and saying so precisely is more useful than
publishing a baseline built on unusable inputs.

---

## 1. The extract is internally inconsistent, in three independent ways

**(a) Share counts are discontinuous across the IPO boundary.**

```
Q1 2026 weighted average diluted shares    8,359,379
Q2 2026 weighted average diluted shares   61,924,756      <- 7.4x in one quarter
CommonStockSharesIssued (tagged)           4,168,374      <- dated 2025-12-31
common_shares_outstanding (extract field) 97,965,552
```

**Four different share counts, spanning 4.2M to 98.0M.** The financing cash flow of
**+$413.009M** and the jump in equity ($109.549M → $794.818M) date a listing to Q2 2026.
**No two of the four figures agree, and the extract does not mark which is pre- and which
is post-IPO.**

**(b) The EPS bridge fails catastrophically — and not because of a sign defect.**

```
EPS (diluted) $0.07 x 61.925M = $4.335M
reported net income           = $15.278M
gap: 72%          <- against sub-1% for every clean issuer in the universe
```

**(c) The balance-sheet block is stale relative to the metrics block.**

| Source | Assets | Period |
|---|---:|---|
| `balance_sheet` block | $489.940M | tagged **2025-12-31** |
| `metrics` array, Q2 2026 | **$904.222M** | 2026-06-30 |

**A 1.85× difference for the same quarter.** The balance-sheet block carries a pre-IPO
period while the metrics row carries the current one.

## 2. Why this is a NEW class, not another instance of DA-23

**DA-23 would predict a sign inversion at equal magnitude. Here the level itself does not
reconcile, and the cause is identifiable: an IPO between the two reported periods.**

**NEW CANDIDATE — DA-28: capital-structure discontinuity invalidates share-count-based
detectors.** Around a listing, weighted-average share counts are computed over a period
that straddles two capital structures, so **EPS × shares cannot reconcile to net income on
either side** — and unlike DA-23, no arithmetic test can recover the true figure, because
the correct denominator is a time-weighted blend the extract does not expose.

**This matters beyond HAWK.** The universe's coverage audit lists several recent listings
(KRMN, VOYG, and HAWK among them). **Any issuer whose first reported quarter straddles its
IPO will fail the EPS bridge for a legitimate reason, and a thesis screening for DA-23 by
EPS reconciliation will produce false positives.** KRMN and VOYG were both checked this pass
and both passed cleanly — **because both had already reported a full post-IPO quarter.**
HAWK has not.

## 3. What IS usable, and it is one real finding

| Metric | Q2 2026 | Q1 2026 | Change |
|---|---:|---:|---|
| Revenue | **$49.810M** | $49.798M | **+0.02%** |
| Operating income (reported) | $11.546M | $5.617M | +105.6% |
| **Operating margin (reported)** | **23.2%** | 11.3% | +11.9 pts |
| Net income | $15.278M | $8.989M | +70.0% |
| R&D | $8.244M | $9.171M | **−10.1%** |
| **R&D / revenue** | **16.5%** | 18.4% | — |

**Revenue is FLAT — $49.798M to $49.810M, a 0.02% sequential change — while reported
operating income doubled.** Revenue that does not move cannot produce a doubling of
operating income unless a cost fell, and **R&D fell only 10.1% ($0.927M), which explains
$0.9M of the $5.9M increase. $5.0M is unexplained by the extract.**

**Recorded as a DA-23 CANDIDATE** — a 23.2% operating margin at an RF-geolocation satellite
company is not credible on its face, and the movement is not explained by the disclosed cost
lines. **But it is NOT confirmed**, because the same IPO discontinuity that breaks the EPS
bridge also weakens every other reconciliation.

**The honest position: HAWK's operating line cannot be validated either way from this
extract.** The finding is the limitation.

## 4. What would resolve it

**The named disclosure**: HawkEye 360's **first post-IPO 10-Q with a full quarter of
post-listing capital structure** — which would give a stable denominator for the EPS bridge
and a comparable prior period. **Until then HAWK should be excluded from cross-issuer margin
rankings**, and the exclusion should be recorded as a coverage limitation (Q-category), not
as a data defect in the issuer.

---

## Carry-forwards

1. **HAWK's extract is internally inconsistent in three independent ways** — four
   non-agreeing share counts, a 72% EPS-bridge failure, and a balance sheet 1.85× stale
   against its own metrics row. **No operating baseline is publishable.**
2. **NEW DA-28 CANDIDATE — capital-structure discontinuity around an IPO invalidates
   share-count-based detectors**, and no arithmetic test recovers the true figure because
   the correct denominator is a blend the extract does not expose. **A thesis screening for
   DA-23 by EPS reconciliation will produce false positives on recent listings** — the
   detector needs a guard for issuers whose first reported quarter straddles a listing.
3. **One real finding: revenue flat to 0.02% while reported operating income doubled.**
   Disclosed cost lines explain $0.9M of $5.9M. **Recorded as a DA-23 candidate, NOT
   confirmed** — the same discontinuity that breaks the bridge weakens every other test.
4. **Recommendation: exclude HAWK from cross-issuer margin rankings** until a full
   post-IPO quarter exists. Record as a coverage limitation, not an issuer defect.
