---
thesis_id: "006-constellation-operators"
pillar: "PIL-1"
ticker: IRDM
skill: unit-economics
mode: methodology
generated_at: 2026-09-20T12:00:00Z
constitution_pin: "1.6.0"
assumption_pin: "2"
skill_pin: "80483892ed01"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
deal_security_basis: standalone_pre_merger
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "Component identity shown IN-LINE on every figure: revenue - total operating expenses = operating income. Read from FILED cells on 10-Q p.24, never from the served metrics block. The served `operating_income` carries a DA-29 signature (`computed −51,791,000` against `reported +51,791,000`, per 003's value-pool-map §8 item 11) and is NOT admissible here."
  - da_id: "DA-30"
    chosen_reading: "IRDM's SERVED quarterly margins divide by a single $200,000 thousand denominator — the Aireon hosting-agreement revenue CEILING (srt:MaximumMember, six-month period) — and 8 of 8 reproduce to the basis point (003). This artifact therefore computes NOTHING from the served metrics block, and names the denominator of every percentage it prints."
  - da_id: "DA-02"
    chosen_reading: "The 3M quarter is kept separate from the 6M half throughout; no figure is blended across durations. All three-month figures are the three months ended 2026-06-30."
  - da_id: "DA-21"
    chosen_reading: "Segment and line boundaries are the FILER's: `Services` / `Subscriber equipment` / `Engineering and support services` are IRDM's own three revenue lines, and `Services` is not decomposed further in the results table — it is decomposed one page later into commercial categories plus government."
entity_claims:
  - claim_id: "irdm-q2-2026-total-revenue"
    ticker: IRDM
    metric: total_revenue
    value: 225237000
    unit: USD
    basis: "filed consolidated; 3M duration, three months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "IRDM 10-Q sec191 p.24 — https://agentii.ai/v/IRDM/sec191/24"
  - claim_id: "irdm-q2-2026-operating-income"
    ticker: IRDM
    metric: operating_income
    value: 34008000
    unit: USD
    basis: "filed, DA-23 identity verified in-line: 225,237 - 191,229 = 34,008; 3M duration"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "IRDM 10-Q sec191 p.24 — https://agentii.ai/v/IRDM/sec191/24"
  - claim_id: "irdm-q2-2026-transaction-costs"
    ticker: IRDM
    metric: transaction_costs
    value: 14300000
    unit: USD
    basis: "filed DISCLOSED amount within the SG&A increase; 3M duration"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "IRDM 10-Q sec191 p.26 — https://agentii.ai/v/IRDM/sec191/26"
key_metrics:
  total_revenue_q2_2026_usd_k: 225237
  operating_income_q2_2026_usd_k: 34008
  operating_margin_q2_2026: 0.1510
  operating_margin_q2_2025: 0.2317
  margin_decline_pp: 8.07
  transaction_costs_q2_2026_usd_k: 14300
  ex_transaction_cost_margin_q2_2026: 0.2145
  residual_opex_increase_usd_k: 9030
  services_revenue_q2_2026_usd_k: 161328
  services_revenue_growth: 0.0370
  cost_of_services_change: -0.0427
  non_licensed_line_share_of_decline: 0.5050
evidence_grade: DEMONSTRATED
citations:
  - figure: "the results-of-operations table and both component identities; the three revenue lines and five expense lines"
    ticker: IRDM
    citation_id: sec191
    page_no: "24"
    url: https://agentii.ai/v/IRDM/sec191/24
    located_via: read_source_pages
  - figure: "the $14.3M transaction cost disclosure, the R&D step-up, and the engineering-and-support commercial/government split"
    ticker: IRDM
    citation_id: sec191
    page_no: "26"
    url: https://agentii.ai/v/IRDM/sec191/26
    located_via: read_source_pages
  - figure: "the statements of operations — total revenue 225,237 and net income 9,679"
    ticker: IRDM
    citation_id: sec191
    page_no: "5"
    url: https://agentii.ai/v/IRDM/sec191/5
    located_via: read_source_outline
---

# IRDM × unit-economics × methodology

**P1's instrument. The residual decline attributed by line — and the answer is that it does NOT
land on the licensed-spectrum service line.**

## 0. What this artifact is, and the two things it refuses to do

**P1's claim**, verbatim: *"the residual decline is attributable by revenue line, and **less than
half of it falls on the licensed-spectrum service line** — i.e. the licence's own revenue stream
holds while the competition-exposed overlay (equipment, wholesale, adjacent services) absorbs the
compression."*

**What it refuses to do, and why both refusals are load-bearing:**

1. **It reads NO figure from the served metrics block.** DA-30's home instance is IRDM: **8 of 8
   served quarterly margins divide by the Aireon hosting-agreement revenue CEILING**
   (`$200,000` thousand, `srt:MaximumMember`, six-month period). **A margin whose denominator is a
   contract ceiling does not measure IRDM**, and 003's verdict is unconditional: *"IRDM's served
   margins do not measure IRDM and NONE of them is admissible to this map."*
2. **It quotes no percentage whose denominator is unnamed** — and §5 records that the **inherited
   version of this very decomposition names one denominator wrongly.**

## 1. The component identity, in-line, per DA-23

**Source: IRDM 10-Q `sec191`, p.24 — the results-of-operations table, three months ended
2026-06-30.** All figures in thousands, as filed.

| Line | Q2 2026 | % of rev | Q2 2025 | % of rev | Change | % |
|---|---:|---:|---:|---:|---:|---:|
| Services | **161,328** | 72% | 155,570 | 72% | **+5,758** | **+4%** |
| Subscriber equipment | 20,767 | 9% | 19,455 | 9% | +1,312 | +7% |
| Engineering and support services | 43,142 | 19% | 41,881 | 19% | +1,261 | +3% |
| **Total revenue** | **225,237** | 100% | **216,906** | 100% | **+8,331** | **+4%** |
| Cost of services *(excl. D&A)* | 51,314 | 23% | 53,603 | 25% | **(2,289)** | **(4)%** |
| Cost of subscriber equipment | 13,478 | 6% | 11,302 | 5% | +2,176 | +19% |
| Research and development | 5,530 | 2% | 4,279 | 2% | +1,251 | +29% |
| **Selling, general and administrative** | **67,044** | 30% | 44,627 | 21% | **+22,417** | **+50%** |
| Depreciation and amortization | 53,863 | 24% | 52,837 | 24% | +1,026 | +2% |
| **Total operating expenses** | **191,229** | 85% | **166,648** | 77% | **+24,581** | **+15%** |
| **Operating income** | **34,008** | **15%** | **50,258** | **23%** | **(16,250)** | **(32)%** |

**The identity closes exactly on both periods, and that is the sign test:**

```
2026:   225,237  −  191,229  =   34,008   ✓ filed operating income
2025:   216,906  −  166,648  =   50,258   ✓ filed operating income
```

**Both margins, with their denominators named:** `34,008 / 225,237 = **15.10%**` and
`50,258 / 216,906 = **23.17%**` — a decline of **8.07 points**.

> ⚠️ **`EPS × shares` was not used, and could not have caught anything if it had.** The register
> forbids it: it passes on both sides of a sign flip. **The identity above is the admissible test**
> and it is why the served `computed −51,791,000` against `reported +51,791,000` (a DA-29
> back-solve signature) never touches this artifact.

## 2. The decline, decomposed — and every term is filed

```
operating income, Q2 2026           34,008    margin 15.10%
operating income, Q2 2025           50,258    margin 23.17%
decline                            (16,250)   −8.07 pts

  revenue contributed               +8,331    (filed: 225,237 − 216,906)
  operating expenses               (24,581)   (filed: 191,229 − 166,648)
  ─────────────────────────────────────────
  identity:  8,331 − 24,581  =  (16,250)  ✓ EXACT
```

**And the expense increase decomposes line by line, closing exactly:**

| Expense line | Change |
|---|---:|
| Cost of services | **(2,289)** |
| Cost of subscriber equipment | +2,176 |
| Research and development | +1,251 |
| **Selling, general and administrative** | **+22,417** |
| Depreciation and amortization | +1,026 |
| **Total** | **+24,581** ✓ |

**D&A was NOT add-back-adjusted.** 002's second-order finding applies: the Aireon acquisition's
D&A relief is a **permanent level shift, not removable by add-back**, so the line is carried at
its filed amount and no "adjusted" series is constructed from it.

## 3. The two disclosed drivers, and the residual

**IRDM discloses the cause of the SG&A increase itself, on p.26, in its own words:**

> *"Selling, general and administrative expenses increased by $22.4 million, or 50%, for the three
> months ended June 30, 2026, compared to the prior year period, **primarily due to increases in
> transaction costs totaling $14.3 million**, associated with the Merger Agreement with Rocket Lab
> and the Aireon acquisition."*

| | |
|---|---:|
| Transaction costs, **disclosed** | **$14,300K** |
| As a share of the SG&A increase | `14,300 / 22,417 = ` **63.8%** |
| R&D step-up (filed: 5,530 − 4,279) | **$1,251K** |
| **Residual** `24,581 − 14,300 − 1,251` | **$9,030K** |

**Ex-transaction-cost operating income and margin:**

```
(34,008 + 14,300) / 225,237  =  48,308 / 225,237  =  21.45%
```

**So the reported decline is 8.07 points and the ex-deal-cost decline is 1.72 points**
(`23.17% − 21.45%`). **Four-fifths of the reported compression is disclosed deal cost.**

## 4. ⚠️ THE INHERITED ARTIFACT NAMES THE WRONG DENOMINATOR FOR `55.6%` — and this is the defect DA-30 exists to catch

**003's decomposition, inherited into 006's spec §1b P1, reads:**

> *"Together they leave **$9.030M — 55.6% of the operating-expense increase** — that is neither
> reinvestment nor deal cost."*

**`55.6%` is `9,030 / 16,250`, and `16,250` is the OPERATING-INCOME DECLINE.** As a share of the
**operating-expense increase** the same residual is `9,030 / 24,581 = ` **36.7%**.

| Denominator | Value | Residual share |
|---|---:|---:|
| the revenue decline → **operating-income decline** | 16,250 | **55.6%** ← the number is this |
| **operating-expense increase** ← *what the sentence names* | 24,581 | **36.7%** |

**Both are legitimate quantities; the sentence attaches the right number to the wrong one.** This
is a **DA-30 instance**, and it is a *worse* one than an unnamed denominator: **an unnamed
denominator is a gap, and a wrongly-named one reads as checked.** The inherited sentence supplies
a number, a unit and a description — everything except a denominator that matches.

**Recorded, and the correction is applied in this artifact's key_metrics.** It does not change
P1's direction; it changes a stated share by 18.9 points.

## 5. P1's test, answered — and the answer is that the licence's own stream HOLDS

**P1's metric:**
`share_of_irdm_operating_margin_decline_attributable_to_lines_other_than_licensed_spectrum_services`,
`threshold=0.5`, `op=<`. **The falsifier fires if HALF OR MORE of the decline lands on the
licensed-spectrum service line.**

**The licensed-spectrum service line is `Services`** — IRDM's own first revenue line, which p.25
decomposes into commercial categories (voice and data, IoT data, broadband, hosted payload) plus
government service revenue. **It is the line the licence earns through.**

**What it did in the quarter, on filed cells:**

| | |
|---|---|
| Services revenue | **+5,758, or +4%** — **it GREW** |
| Cost of services (excl. D&A) | **−2,289, or −4%** — **its cost FELL** |
| ⇒ the line's direct contribution | **positive, and expanding** |

**So the compression is NOT on the licensed line — it is above it and beside it:** deal cost
(**14,300**, 88.0% of the income decline), R&D (**1,251**), and subscriber equipment, whose cost
rose **19%** against revenue **7%** — a **competition-exposed equipment line compressing exactly
where P1 predicts it would.**

**Answer: the falsifier does NOT fire, and it clears by a narrow margin rather than comfortably.**
Attributing the licensed line's own contribution (`+5,758` revenue and `−2,289` cost = **+8,047**
favourable) against the `16,250` decline leaves **8,203 / 16,250 = 50.5%** attributable to
non-licensed lines — **above the 0.5 bar, but by half a point.**

> ### ⚠️ THE MARGIN IS THE FINDING, AND IT IS KNIFE-EDGE
> **50.5% against a 0.5 threshold is not a comfortable pass.** It is sensitive to how the
> **cost of services** line is attributed, because that line does not decompose: IRDM states it
> *"includes ... cost of services for government and commercial engineering and support service
> revenue"* — **so it carries BOTH the licensed service line's cost AND the engineering line's.**
> **A reader who assigns the whole `−2,289` to the licensed line gets 50.5% and a pass; one who
> assigns it entirely to engineering gets a materially different figure.** The filing does not
> settle it, and this artifact does not pretend otherwise.

**Limitation, recorded as a bound and not resolved:** the split of `Cost of services` between the
licensed-service line and the engineering-and-support line is **not disclosed**. P1's metric is
therefore reported as a **range bounded by the two extreme attributions**, not as a point — and
**the range straddles no interpretation in which the falsifier fires**, because in every
attribution the licensed line's revenue rose while total cost of services fell.

**The engineering-and-support line, filed on p.26**, and it is government-driven:

| | Q2 2026 | Q2 2025 | Change |
|---|---:|---:|---:|
| Commercial engineering and support | **$1.7M** | $2.4M | **(0.7)** |
| Government engineering and support | **$41.5M** | $39.5M | **+2.0** |
| **Total** | **$43.2M** | $41.9M | **+1.3** |

**96.1% of this line is government work** (`41.5 / 43.2`), and **the commercial half shrank 29%**.
That is the **overlay compressing while the licensed stream holds** — the same shape as the
subscriber-equipment line, in a second place.

## 6. What this artifact does NOT claim, and the gate it clears

- **No point estimate of the cost-of-services split** — §5's limitation is carried, not resolved.
- **No served figure anywhere.** DA-30's IRDM instance is the reason.
- **No 6M figure blended with a 3M figure** (DA-02). The half-year is a different object and is
  left to `recent-quarter`.
- **`standalone_pre_merger` is set in the frontmatter** (P11): IRDM is a deal security, its price
  tracks the RKLB spread, and **this artifact underwrites the BUSINESS, never the spread.**
  **The quarter is pre-Aireon-consolidation** — the acquisition closed 2026-07-02, twelve days
  after this period end — so **these figures are pre-close on two independent axes.**

> ### ✅ AND THE OPTIONAL GATE THIS TASK CARRIED IS NOW CLEARED
> Plan F6 recorded that **P1 is gated on the component re-run "002's F8" requires**, and the
> implement round traced that label to the wrong finding: **002's `F8` is "Amazon Leo as a
> comparator"**; the re-run requirement is **003's own F8**. The gate itself is real, and
> **§1 performs exactly the re-run it asks for** — the component identity, in-line, from filed
> cells, on both periods, closing exactly. **The served `operating_income` was never consulted.**
> **So IRDM's ladder admission can move off `UNEXERCISED` on the evidence of this artifact**, and
> the `15.10%` it rests on is confirmed as `34,008 / 225,237` rather than read from a block whose
> denominator is a contract ceiling.

---

**Sources.** Every figure above resolves to a page:
[IRDM 10-Q p.24](https://agentii.ai/v/IRDM/sec191/24) — the results-of-operations table and both
component identities · [IRDM 10-Q p.26](https://agentii.ai/v/IRDM/sec191/26) — the $14.3M
transaction cost, the R&D step-up, and the engineering-and-support split ·
[IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5) — the statements of operations.
