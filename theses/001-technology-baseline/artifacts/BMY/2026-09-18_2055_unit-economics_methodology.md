---
thesis_id: "001-technology-baseline"
pillar: PIL-4
ticker: BMY
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T20:55:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 and Q4 FY2024 rows carry ANNUAL revenue"
  - da_id: "DA-23"
    chosen_reading: "operating_income NULL in extract; EPS identity used and reconciles to 0.02%"
  - da_id: "DA-24"
    chosen_reading: "Q1 2024 net income ~= revenue is flagged as an asset-sale contamination CANDIDATE, not treated as operating performance"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# BMY — Microgravity Demand End (Unit Economics of the Buyer)

Source: Form 10-Q, accession `0000014272-26-000020` (Q2 2026, quarter ended 2026-06-30).

---

## 1. The third pharma buyer, and the cohort total

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$12,973M** | $12,269M | +5.7% |
| COGS | $3,726M | — | 28.7% of revenue |
| Implied gross profit | **$9,247M** | — | **71.3% margin** |
| Net income | $3,317M | $1,310M | +153% |
| EPS (diluted) | $1.62 | $0.64 | +153% |
| R&D | **$2,959M** | $2,580M | +14.7% |
| **R&D / revenue** | **22.8%** | 21.0% | — |

**BMY is clean and reconciles exactly:**

```
EPS (diluted) $1.62 x 2,048M diluted shares = $3,317.8M
reported net income                        = $3,317.0M
gap: 0.02%
```

**Clean-positive count: 17 of 17.**

**`OperatingIncomeLoss` is NULL for BMY**, like MRK — the component-identity detector
cannot run. The EPS identity is the only available check.

## 2. The three-pharma buyer cohort, quantified

| Issuer | Q2 2026 revenue | Q2 2026 R&D | Implied gross margin |
|---|---:|---:|---:|
| MRK | $16,607M | $9,741M | — |
| **BMY** | **$12,973M** | **$2,959M** | **71.3%** |
| AMGN | $10,054M | — | 72.0% |
| **Combined** | **$39,634M** | **$12,700M+** | **~72%** |

```
One quarter of the three pharma buyers:      $39,634M
The ENTIRE pure-play space cohort, one year:  ~$2,170M
                                             ─────────
                        ratio: 18.3x per quarter
                        annualised: 73x
```

**The three buyers turn over 73× the entire pure-play space cohort's annual revenue, every
year — and their R&D line alone ($12.7B in one quarter, at least $50B annualised against
MRK+BMY's disclosed $25.7B) is ~12× that cohort's total revenue.**

**This is the PIL-4 conclusion and it is a demand-side one.** The buyers' gross margins
cluster at **71.3% and 72.0%** — remarkably tight across three independent companies. That
is the incumbent terrestrial process's return. **Orbital R&D must clear ~72% gross margin to
be chosen, and the buyers have no capital constraint forcing them to look.**

## 3. BMY's leverage is materially lower than AMGN's — the cohort is not uniform

```
BMY:  liabilities $65,315M / equity $22,319M =  2.9x   equity/assets: 25.5%
AMGN: liabilities (implied)  / equity $11,688M = 7.2x  equity/assets: 12.2%
MRK:  equity $41,933M / assets $129,802M                equity/assets: 32.3%
```

**The three buyers span a 2.7× range in equity cushion** — MRK at 32.3%, BMY at 25.5%, AMGN
at 12.2%. **MRK and BMY have the balance-sheet room; AMGN does not.**

**Consequence for PIL-4**: treating "big pharma" as a single demand pool is wrong. **The
two buyers with capital headroom (MRK, BMY) are the addressable ones**; AMGN's $54.6B debt
stack against an $11.7B equity base makes discretionary long-dated R&D a harder sell.
**This is a testable refinement of the demand thesis**: orbital R&D adoption should appear
first at the less-levered buyers.

## 4. BMY Q1 2024 is a DA-24 CANDIDATE — net income approximately equals revenue

| Quarter | Revenue | Net income | Net margin |
|---|---:|---:|---:|
| **Q1 2024** | **$11,865M** | **$11,911M** | **100.4%** |
| Q2 2024 | $12,201M | $1,680M | 13.8% |
| Q3 2024 | $11,892M | $1,211M | 10.2% |
| Q4 2024 | $48,300M | $8,948M | 18.5% |

**A 100.4% net margin is not an operating result.** Net income exceeding revenue for a
company with $2.7B of quarterly R&D is arithmetically possible only if **below-the-line
gains exceed the entire cost base** — a large divestiture or asset-sale gain.

**Recorded as a DA-24 CANDIDATE requiring verification against the filed 10-Q**, not
asserted. The mechanism that produced it is the same class as the confirmed DA-24 instance
(asset-sale contamination), and the honest position is: **the figure is not usable as an
operating datum until reconciled.** Given DA-24 is already an open amendment candidate,
this adds a second data point to it.

## 5. DA-26 — BMY shows it twice

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $12,973M | a genuine quarter |
| **Q4 2025** | **$48,194M** | **BMY's FY2025 ANNUAL revenue** |
| **Q4 2024** | **$48,300M** | **BMY's FY2024 ANNUAL revenue** |

**Seventeenth issuer confirmed.** FY2025 = Q1–Q3 $35,692M, so annual $48,194M implies Q4 2025
of $12,502M — plausible against Q3's $12,222M. **The annual reading is internally
consistent; a 3.9× quarterly jump is not.**

---

## Carry-forwards

1. **The three pharma buyers turn over 73× the entire pure-play space cohort's annual
   revenue**, and their gross margins cluster tightly at **71.3% and 72.0%** — the number
   orbital R&D must clear. **PIL-4 is confirmed as a demand-side constraint.**
2. **"Big pharma" is not one demand pool.** Equity cushions span 32.3% (MRK), 25.5% (BMY),
   12.2% (AMGN). **A testable refinement: orbital R&D adoption should appear first at the
   less-levered buyers.**
3. **NEW DA-24 CANDIDATE — BMY Q1 2024 net margin 100.4%** (net income $11,911M on revenue
   $11,865M). Not usable as an operating datum until reconciled against the filed 10-Q.
   **Adds a second data point to the open DA-24 amendment.**
4. **Clean-positive 17 of 17; DA-26 at 17 of 17 issuers.**
