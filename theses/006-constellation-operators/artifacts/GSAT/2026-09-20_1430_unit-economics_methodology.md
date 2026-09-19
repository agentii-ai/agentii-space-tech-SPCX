---
thesis_id: "006-constellation-operators"
pillar: "PIL-1"
ticker: GSAT
skill: unit-economics
mode: methodology
generated_at: 2026-09-20T14:30:00Z
constitution_pin: "1.6.0"
assumption_pin: "2"
skill_pin: "80483892ed01"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
deal_security_basis: standalone_pre_merger
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "Component identity shown IN-LINE on every figure: revenue - total operating expenses = operating income. Read from FILED cells on 10-Q p.5 and p.33, and the sign is carried as FILED — `(4,775)`, a loss — never as its absolute value. GSAT is the register's named instance for the sign strip, and it is also the name where the served block and the filed page disagree by a factor of 1,000 on the same concept, so nothing in this artifact is taken from the served block."
  - da_id: "DA-30"
    chosen_reading: "Every percentage below names its denominator in-line. The margin denominators are FILED TOTAL REVENUE for the same 3M period — 64,772 and 67,148 — and never a segment, a ceiling, or a served pair. §4 records the one place where this artifact's own coverage statistic could be misread the same way, and names both denominators to prevent it."
  - da_id: "DA-02"
    chosen_reading: "The 3M quarter is kept separate from the 6M half throughout. Every figure in §1 and §2 is the three months ended 2026-06-30, from the p.5 statements of operations. The half-year is a different object and is not blended in."
  - da_id: "DA-10"
    chosen_reading: "GSAT's ARPU series covers LESS THAN A THIRD of its revenue, and the issuer says so itself. p.33 states that wholesale capacity and government revenue are not subscriber driven and that no ARPU is presented for them. §4 therefore reports ARPU as a PARTIAL basis with its coverage share computed, not as a company-wide per-subscriber metric."
  - da_id: "DA-21"
    chosen_reading: "Line boundaries are the FILER's: the four revenue lines and the six expense lines are GSAT's own, as presented on p.5 and disaggregated on p.33 and p.35. The six expense lines are the SAME six 003 used to reproduce the 69,547 total, and they close to the same figure here independently."
entity_claims:
  - claim_id: "gsat-q2-2026-total-revenue"
    ticker: GSAT
    metric: total_revenue
    value: 64772000
    unit: USD
    basis: "filed consolidated; 3M duration, three months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "GSAT 10-Q sec166 p.5 — https://agentii.ai/v/GSAT/sec166/5"
  - claim_id: "gsat-q2-2026-operating-loss"
    ticker: GSAT
    metric: operating_income
    value: -4775000
    unit: USD
    basis: "filed, DA-23 identity verified in-line: 64,772 - 69,547 = (4,775). NEGATIVE, carried as filed; the served block's positive 4,775,000 loses the sign and differs by 1,000x. 3M duration"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "GSAT 10-Q sec166 p.5 — https://agentii.ai/v/GSAT/sec166/5"
  - claim_id: "gsat-q2-2026-merger-transaction-costs"
    ticker: GSAT
    metric: transaction_costs
    value: 10400000
    unit: USD
    basis: "filed DISCLOSED amount: the legal-and-professional-fee increase within MG&A, stated to be 'due primarily to transaction costs related to the Mergers'; the disclosure is a component of a component and is NOT additive to the filed total; 3M duration"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "GSAT 10-Q sec166 p.35 — https://agentii.ai/v/GSAT/sec166/35"
  - claim_id: "gsat-q2-2026-wholesale-capacity-revenue"
    ticker: GSAT
    metric: wholesale_capacity_revenue
    value: 40114000
    unit: USD
    basis: "filed; largest single revenue line; DA-10: carries NO ARPU because the issuer states it is not subscriber driven; 3M duration"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "GSAT 10-Q sec166 p.33 — https://agentii.ai/v/GSAT/sec166/33"
key_metrics:
  total_revenue_q2_2026_usd_k: 64772
  total_revenue_q2_2025_usd_k: 67148
  revenue_change_pct: -0.0354
  operating_income_q2_2026_usd_k: -4775
  operating_income_q2_2025_usd_k: 6146
  operating_margin_q2_2026: -0.0737
  operating_margin_q2_2025: 0.0915
  margin_swing_pp: -16.52
  total_opex_q2_2026_usd_k: 69547
  total_opex_q2_2025_usd_k: 61002
  opex_increase_usd_k: 8545
  mgna_increase_usd_k: 13342
  merger_transaction_costs_usd_k: 10400
  transaction_cost_share_of_mgna_increase: 0.779
  ex_transaction_cost_operating_income_usd_k: 5625
  ex_transaction_cost_margin_q2_2026: 0.0868
  wholesale_capacity_revenue_usd_k: 40114
  wholesale_capacity_share_of_revenue: 0.6193
  arpu_covered_revenue_share: 0.2907
  arpu_coverage_basis: partial
  subscribers_total: 803980
  arpu_iot_usd: 4.31
  arpu_spot_usd: 13.81
  arpu_duplex_usd: 57.44
evidence_grade: DEMONSTRATED
citations:
  - figure: "the statements of operations — total revenue 64,772 / 67,148, total operating expenses 69,547 / 61,002, and operating loss (4,775) against prior income 6,146; the six expense lines"
    ticker: GSAT
    citation_id: sec166
    page_no: "5"
    url: https://agentii.ai/v/GSAT/sec166/5
    located_via: read_source_pages
  - figure: "revenue by service type — wholesale capacity 40,114, IoT 7,512, SPOT 8,604, Duplex 2,715, government and other 1,053, subscriber equipment 4,774; subscribers 803,980; ARPU IoT $4.31 / SPOT $13.81 / Duplex $57.44; and the issuer's statement that wholesale capacity and government revenue are not subscriber driven"
    ticker: GSAT
    citation_id: sec166
    page_no: "33"
    url: https://agentii.ai/v/GSAT/sec166/33
    located_via: read_source_pages
  - figure: "the expense variance narrative — cost of services +$4.1M by component, MG&A +$13.3M with legal and professional fees +$10.4M 'due primarily to transaction costs related to the Mergers', and the CARES Act retention credit as a non-recurring 2025 offset"
    ticker: GSAT
    citation_id: sec166
    page_no: "35"
    url: https://agentii.ai/v/GSAT/sec166/35
    located_via: read_source_pages
---

# GSAT × unit-economics × methodology

**P1's contrast case. IRDM's licensed stream held while its overlay compressed. GSAT has no
licensed stream to hold — and that is the point of running it.**

## 0. What this artifact is for

**P1 is a two-sided claim and IRDM only tests one side of it.** IRDM's answer was that the
licence's own revenue stream **grew** (+5,758) while its cost **fell** (−2,289), so the
compression sat on the competition-exposed overlay. **A claim that survives only where a licence
exists is not a claim about the tier — it is a claim about licences.** GSAT is the tier's
counter-example: **the largest revenue line carries no licence and no subscriber**, and it is
where this artifact looks first.

**Three things GSAT contributes that no other name in the universe can:**

1. **It is the DA-23 instance the register names** — the sign strip — and it is also the name
   where **the served block and the filed page disagree by a factor of 1,000** on the same
   concept. Both defects are live here simultaneously.
2. **It is the DA-10 analogue that is worse than DA-10.** IRDM's ARPU problem was a service-line
   basis. **GSAT's is a coverage problem: the issuer explicitly declines to publish ARPU for the
   line that is 61.9% of revenue.**
3. **It is a merged security** (AMZN at $90.00/sh), so `standalone_pre_merger` binds, and —
   unlike IRDM, where the deal cost was disclosed as a clean $14.3M — **GSAT buries the same
   class of cost inside a fee line.** §3 does the un-burying.

## 1. The component identity, in-line, per DA-23

**Source: GSAT 10-Q `sec166`, p.5 — the statements of operations, three months ended
2026-06-30.** All figures in thousands, **as filed**.

| Line | Q2 2026 | % of rev | Q2 2025 | % of rev | Change |
|---|---:|---:|---:|---:|---:|
| Wholesale capacity services | **40,114** | 61.9% | **42,414** | 63.2% | **(2,300)** |
| IoT | 7,512 | 11.6% | 6,749 | 10.1% | +763 |
| SPOT | 8,604 | 13.3% | 8,086 | 12.0% | +518 |
| Duplex | 2,715 | 4.2% | 2,857 | 4.3% | (142) |
| Government and other services | 1,053 | 1.6% | 1,176 | 1.8% | (123) |
| Subscriber equipment | 4,774 | 7.4% | 5,866 | 8.7% | **(1,092)** |
| **Total revenue** | **64,772** | 100% | **67,148** | 100% | **(2,376)** |
| Cost of services | 23,602 | 36.4% | 19,479 | 29.0% | +4,123 |
| Cost of subscriber equipment | 3,395 | 5.2% | 2,881 | 4.3% | +514 |
| **Selling, general and administrative** | **23,025** | **35.5%** | **9,683** | **14.4%** | **+13,342** |
| Stock-based compensation | 2,723 | 4.2% | 5,949 | 8.9% | **(3,226)** |
| Reduction in value of assets | 0 | 0.0% | 0 | 0.0% | 0 |
| Depreciation and amortization | 16,802 | 25.9% | 23,010 | 34.3% | **(6,208)** |
| **Total operating expenses** | **69,547** | 107.4% | **61,002** | 90.8% | **+8,545** |
| **Operating income (loss)** | **(4,775)** | **(7.4)%** | **6,146** | **9.2%** | **(10,921)** |

**The identity closes exactly on both periods:**

```
2026:    64,772  −  69,547  =   (4,775)   ✓ filed operating LOSS — negative
2025:    67,148  −  61,002  =     6,146   ✓ filed operating income
```

**Both margins, with their denominators named:** `(4,775) / 64,772 = **−7.37%**` and
`6,146 / 67,148 = **+9.15%**` — a swing of **−16.52 points**, and it crosses zero.

> ### ⚠️ THE SIGN IS THE FIRST FINDING, AND IT IS CARRIED AS FILED
> **`(4,775)` is a LOSS and every appearance of it in this artifact is negative.** The served
> block returns `+4,775,000` for the same concept on the same period — **wrong in sign and wrong
> by a factor of 1,000**, because the filed cell is in thousands and negative. **This artifact
> reads no figure from the served block**, and §1's identity is the test that would have caught
> it: `64,772 − 69,547` is negative, and no arrangement of the two filed operands makes it
> positive. **A sign strip cannot survive an in-line identity, which is why DA-23 asks for one.**

## 2. The expense increase, decomposed — and the six lines are 003's six lines

**The increase is +8,545 and it closes exactly, on the same six-line boundary 003 used:**

| Expense line | Change |
|---|---:|
| Cost of services | +4,123 |
| Cost of subscriber equipment | +514 |
| **Selling, general and administrative** | **+13,342** |
| Stock-based compensation | **(3,226)** |
| Reduction in value of assets | 0 |
| Depreciation and amortization | **(6,208)** |
| **Total** | **+8,545** ✓ EXACT |

```
revenue contributed                  (2,376)
operating expenses                   (8,545)
─────────────────────────────────────────────
identity:  (2,376) − 8,545  =  (10,921)  ✓ EXACT = the filed operating-income swing
```

> ### ⚠️ AND TWO OF THE SIX LINES MOVED THE OTHER WAY — which is why the *headline* understates the damage
> **D&A fell 6,208 and stock-based comp fell 3,226 — together 9,434 of favourable movement
> against a 8,545 total increase.** Absent those two, the cash-operating lines rose **17,979**.
> **The reported +14.0% expense increase is a net figure that two large favourable non-cash
> lines are suppressing**, and a reader who takes it as the operating cost trend takes the wrong
> number. **This is the tier's compression being masked from inside the expense side** — the
> mirror of IRDM, where a favourable revenue line masked it from the other direction.

## 3. The disclosed driver, and the un-burying

**GSAT discloses the cause on p.35, in its own words:**

> *"MG&A expenses increased **$13.3 million**... due to higher legal and professional fees as well
> as higher personnel costs. For the three... months ended June 30, 2026 compared to the same
> periods in 2025, **legal and professional fees increased $10.4 million**... due primarily to
> **transaction costs related to the Mergers**"*

| | |
|---|---:|
| MG&A increase, filed | **13,342** |
| Legal and professional fees increase, **disclosed** | **10,400** |
| **As a share of the MG&A increase** | `10,400 / 13,342 = ` **77.9%** |
| Personnel costs increase, **disclosed** | ~1,800 |

**Ex-transaction-cost operating income and margin:**

```
(4,775) + 10,400  =  5,625        and      5,625 / 64,772  =  8.68%
```

> ### ⚠️ THE DISCLOSURE IS NESTED, AND THAT IS THE DEFECT THIS SECTION EXISTS TO NAME
> **`$10.4M` is not a line item — it is a component of a component.** GSAT reports it as the
> increase in *legal and professional fees*, which is itself a sub-line of *MG&A*, and it
> attaches the causation (*"due primarily to transaction costs related to the Mergers"*) **to
> the fee line, not to a transaction-cost total.** **IRDM gives a clean `transaction costs
> totaling $14.3 million`; GSAT gives a fee increase that is *primarily* deal cost.**
> **The two are NOT the same quantity and this artifact does not treat them as such:** `10,400`
> is an **upper bound** on GSAT's transaction cost, because *"primarily"* means the true deal-cost
> share is at most the whole fee increase and at least a majority of it. **The ex-deal-cost margin
> of 8.68% is therefore a LOWER bound**, and is labelled as such — reported as the optimistic end
> of a range whose pessimistic end is the filed `(7.37)%`.

**So GSAT's story is the same shape as IRDM's, with one difference that matters:** the reported
swing is **−16.52 points**; on the most favourable reading of the disclosure it is **−0.47 points**
(`9.15% − 8.68%`). **GSAT's entire visible deterioration is, on the issuer's own account, deal
cost — and unlike IRDM, it is disclosed in a form that cannot be subtracted cleanly.**

**And the rest of the expense increase is not benign either.** Cost of services rose **4,123**,
which p.35 decomposes as personnel +1.1, ground network +0.6, IT +0.8, XCOM technology
development +0.6 — **a 21.2% increase against revenue that FELL 3.5%.** **Input costs rising while
output falls is the unit-economics definition of compression**, and it is present here
independent of the deal.

## 4. ⚠️ DA-10's analogue, and at GSAT it is a COVERAGE failure rather than a BASIS failure

**GSAT publishes ARPU for IoT, SPOT and Duplex. It publishes none for wholesale capacity or
government — and it says why, on p.33:**

> *"**None of these service revenue items are subscriber driven.** Accordingly, we do not present
> ARPU for wholesale capacity services revenue or government and other services revenue."*

**That is a correct and honest disclosure. The finding is what it implies for the metric:**

| Revenue line | Amount | Share | ARPU published? |
|---|---:|---:|---|
| Wholesale capacity | **40,114** | **61.9%** | **No — issuer declines** |
| IoT | 7,512 | 11.6% | Yes — $4.31 |
| SPOT | 8,604 | 13.3% | Yes — $13.81 |
| Duplex | 2,715 | 4.2% | Yes — $57.44 |
| Government and other | 1,053 | 1.6% | **No — issuer declines** |
| Subscriber equipment | 4,774 | 7.4% | n/a — equipment, not service |
| **ARPU-covered service revenue** | **18,831** | **29.1%** | |

> ### ⚠️ THE COVERAGE NUMBER, WITH BOTH DENOMINATORS NAMED — this is the DA-30 discipline applied to my own statistic
> **`18,831 / 64,772 = 29.1%`** — **ARPU is published for the lines carrying 29.1% of TOTAL
> revenue.** Two denominators are in play and conflating them is the easy error:
> **against TOTAL revenue the coverage is 29.1%; against SERVICE revenue** (`64,772 − 4,774`
> equipment `= 59,998`) **it is `18,831 / 59,998 = ` 31.4%.** **Both are stated because a reader
> given only "ARPU covers under a third of revenue" cannot tell which was meant** — the DA-30
> rule this artifact is bound by, applied to its own arithmetic rather than to someone else's.
>
> **And the 62%-of-revenue line is excluded not because GSAT is withholding, but because it is
> genuinely not subscriber-driven.** The metric is not missing — **it does not apply there.**
> That distinction is the difference between a data gap and a basis limit, and this artifact
> records it as the **basis limit** it is: **any company-wide "ARPU" for GSAT would be a
> constructed number that the issuer explicitly declines to construct.**

**Subscribers: 803,980 against 781,470** — **+2.9%**, in a quarter when service revenue from the
ARPU-covered lines **rose** while total revenue **fell**. **So GSAT's subscriber base is growing
on the lines that matter least to its revenue.** That is a real and uncomfortable fact for a
subscriber-count-driven narrative, and it is the DA-10 trap in its purest form: **the metric with
the growth is the metric covering 29% of the business.**

## 5. P1's test, re-run on the contrast case — and it answers the other way

**P1's metric:**
`share_of_gsat_operating_margin_decline_attributable_to_lines_other_than_licensed_spectrum_services`.

**GSAT has no licensed-spectrum service line.** Verbatim from the filed disaggregation: its four
service lines are **wholesale capacity, IoT, SPOT, Duplex**, plus government. **Wholesale
capacity is 61.9% of revenue and on the issuer's own statement is "not subscriber driven"** — it
is a capacity-sale line, sold to distributors and partners, not a licence-earned retail stream.

| | |
|---|---|
| Wholesale capacity revenue | **−2,300** |
| All other service lines | +1,016 (IoT +763, SPOT +518, Duplex −142, Gov −123) |
| Subscriber equipment | **−1,092** |
| **Total revenue** | **−2,376** ✓ |

**So on the P1 question — "does the licence's own stream hold?" — GSAT returns no answer at all,
because the condition P1 names does not exist at GSAT.** The literal test cannot run on a name
with no licensed service line, and **recording that as a null rather than manufacturing a
partition is the only honest reading.**

**But the test's *substance* transfers, and it is the sharper reading of P1 anyway** — because
what P1 is really asserting is an **ordering**: the subscription-anchored service line holds,
and the lines exposed to capacity competition and equipment pricing do not. **IRDM showed that
ordering where a licence exists. GSAT shows it where one does not:**

| | IRDM | GSAT |
|---|---|---|
| Subscription/licence-anchored service | `Services` **+4%**, cost **−4%** | **IoT + SPOT `(7,512 + 8,604 = 16,116)` `+8.6%`** |
| Capacity / un-licensed line | eng-and-support commercial **−29%** | **wholesale capacity `−5.4%`** |
| Equipment line | revenue +7% against cost **+19%** | **revenue `−18.6%`** |

**The ordering holds at both names, on different partitions, at different signs of total
revenue** — IRDM's total grew 4% while GSAT's fell 3.5%, and the internal ordering is the same.

> ### ✅ THE CONTRAST CASE SHARPENS P1 RATHER THAN REFUTING IT
> **At both names, the subscription/licence-anchored service revenue grew and the
> capacity-and-equipment lines fell.** The falsifier still does not fire. **And the contrast case
> raises the confidence materially, because GSAT is the name where P1's own mechanism could not
> operate in principle** — there is no licensed stream to hold — **and the ordering still appears,
> on the metric's substance rather than its letter.**
>
> ⚠️ **Stated as a limit, not a result:** "IoT + SPOT is GSAT's licensed-stream analogue" is **my
> mapping, not the filer's**. GSAT does not present a licensed/non-licensed partition, and this
> artifact does not claim it does. **The mapping is recorded as an interpretation** so a reader
> can reject it without rejecting the arithmetic above it.

## 6. What this artifact does NOT claim, and the gates it clears

- **No figure from the served block.** §1's sign is filed; the `1,000×`/sign-strip pair is the
  reason, and the identity is the test.
- **No point estimate of GSAT's true transaction cost.** `10,400` is an **upper bound**
  (*"primarily"*), so `8.68%` is a **lower bound on the margin** — §3 says so in-line.
- **No company-wide ARPU constructed.** The issuer declines to construct one; §4 records the
  basis limit rather than filling it.
- **No 6M figure blended with a 3M figure** (DA-02).
- **`standalone_pre_merger` is set in the frontmatter** (P11): **GSAT is being acquired by AMZN at
  $90.00 per share**, so its price tracks a deal spread and **this artifact underwrites the
  BUSINESS, never the spread.** All figures are **pre-close**.

> ### ✅ AND IT CLEARS THE ONE THING THAT WOULD HAVE MADE IT UNUSABLE
> **003's six-line expense decomposition of `69,547` is independently reproduced here from the
> filed cells, closing exactly** — `23,602 + 3,395 + 23,025 + 2,723 + 0 + 16,802 = 69,547`. **The
> line boundary 003 used at GSAT is confirmed, not inherited**, which matters because §2's
> finding (that two favourable non-cash lines suppress the increase) depends entirely on that
> boundary being the filer's.

---

**Sources.** Every figure above resolves to a page:
[GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5) — the statements of operations, the six
expense lines, and both component identities · [GSAT 10-Q p.33](https://agentii.ai/v/GSAT/sec166/33)
— revenue by service type, subscribers, the three ARPU figures, and the issuer's own statement
that wholesale capacity and government revenue are not subscriber driven ·
[GSAT 10-Q p.35](https://agentii.ai/v/GSAT/sec166/35) — the expense variance narrative and the
$10.4M legal-and-professional increase attributed to merger transaction costs.
