---
thesis_id: "006-constellation-operators"
pillar: "PIL-1"
ticker: GSAT
skill: unit-economics
mode: triggers
generated_at: 2026-09-20T16:00:00Z
constitution_pin: "1.6.0"
assumption_pin: "2"
skill_pin: "80483892ed01"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
deal_security_basis: standalone_pre_merger
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "Each trigger names the filed line it would move and the sign it would move it in. GSAT is the register's sign-strip instance, so a trigger stated without a sign is not evaluable here."
  - da_id: "DA-30"
    chosen_reading: "Every threshold names its denominator. The falsifier's denominator is FILED TOTAL REVENUE for the 3M period — 64,772 — and never a served pair."
  - da_id: "DA-10"
    chosen_reading: "The single highest-value trigger at GSAT is the ARPU coverage share, because it is the one series a reader is most likely to treat as company-wide when it covers 29.1% of revenue."
key_metrics:
  trigger_count: 6
  triggers_that_change_the_verdict: 3
  triggers_that_are_clocks_not_tests: 1
  wholesale_capacity_share_of_revenue: 0.6193
  arpu_coverage_share: 0.2907
  ex_transaction_cost_margin: 0.0868
  ex_transaction_cost_margin_is_a: lower_bound
  deal_cost_share_breakeven: 0.459
  ex_deal_cost_margin_interval_low: -0.0737
  ex_deal_cost_margin_interval_high: 0.0868
  reported_margin: -0.0737
  subscribers_total: 803980
  subscribers_growth: 0.0288
evidence_grade: DEMONSTRATED
citations:
  - figure: "the statements of operations — total revenue 64,772 / 67,148, total operating expenses 69,547 / 61,002, operating loss (4,775) against prior income 6,146"
    ticker: GSAT
    citation_id: sec166
    page_no: "5"
    url: https://agentii.ai/v/GSAT/sec166/5
    located_via: read_source_pages
  - figure: "revenue by service type and the issuer's statement that wholesale capacity and government revenue are not subscriber driven"
    ticker: GSAT
    citation_id: sec166
    page_no: "33"
    url: https://agentii.ai/v/GSAT/sec166/33
    located_via: read_source_pages
  - figure: "the MG&A variance and the legal-and-professional increase attributed to merger transaction costs"
    ticker: GSAT
    citation_id: sec166
    page_no: "35"
    url: https://agentii.ai/v/GSAT/sec166/35
    located_via: read_source_pages
---

# GSAT × unit-economics × triggers

**What would overturn the GSAT reading. Six triggers — and unlike IRDM's set, three of these can
actually move the verdict, because GSAT's conclusion rests on a DISCLOSURE rather than on an
arithmetic bound.**

## 0. What is being tested at GSAT

**The reading:** GSAT's reported operating swing of **−16.52 points** (`9.15%` → `−7.37%`) is
**substantially deal cost**, not operating deterioration. On the issuer's own disclosure —
legal and professional fees **`+10,400`**, *"due primarily to transaction costs related to the
Mergers"* — the ex-deal-cost margin is **`5,625 / 64,772 = 8.68%`**, a swing of **−0.47 points**.

**⚠️ And `8.68%` is a LOWER BOUND, not a result**, because *"primarily"* means the deal-cost share
of the fee increase is **at most** the whole of it — so **the interval the filing supports is
`[−7.37%, +8.68%]`, and it straddles zero.** The filing does **not** settle whether GSAT's quarter
was operating-profitable before deal costs, **and every trigger below is about narrowing that
interval.** See T-1 for the break-even.

## 1. The triggers

### T-1 · GSAT quantifies "primarily" — **the highest-value trigger, and it is a disclosure**

**Datum:** `10,400` is the **increase in legal and professional fees**, with causation attached to
the fee line — **not a transaction-cost total.** IRDM gives a clean *"transaction costs totaling
$14.3 million"*; **GSAT gives a fee increase that is *primarily* deal cost.**

**Threshold — and it is a single computable number.** Let `s` be the deal-cost share of the
`10,400` fee increase. Ex-deal-cost operating income is `(4,775) + s × 10,400`, which **crosses
zero at `s = 4,775 / 10,400 = ` **45.9%**:**

| `s` | Ex-deal-cost operating income | Margin |
|---:|---:|---:|
| 0% (filed) | **(4,775)** | **−7.37%** |
| 40% | (615) | −0.95% |
| **45.9%** | **0** | **0.00%** ← **the break-even** |
| 50% | +425 | **+0.66%** |
| 77.9% (whole legal/professional increase) | +3,327 | +5.14% |
| 100% (the literal upper bound) | +5,625 | **+8.68%** |

> ### ⚠️ THE BREAK-EVEN IS 45.9% — AND *"PRIMARILY"* ORDINARILY MEANS MORE THAN HALF
> **So on the ordinary meaning of the word GSAT used, the company's ex-deal-cost operating margin
> is POSITIVE — and the entire reported loss is deal cost.** `+0.66%` at exactly 50%, `+8.68%` at
> the literal bound.
>
> **The verdict therefore flips on a question of English, not of accounting** — and **that is
> exactly why this trigger is at the top of the list.** **Any quantification by GSAT settles it**;
> **the word alone already leans the reading one way, and leans it by more than the `0.47`-point
> swing the methodology sibling reports as the optimistic case.**
>
> **Restated honestly: `8.68%` is the LOWER bound on the margin and `100%` is the UPPER bound on
> `s` — these are the same statement.** The interval `[−7.37%, +8.68%]` is what the filing
> supports, **and it straddles zero, which means the filing does not settle whether GSAT's quarter
> was profitable before deal costs.**

**This is the trigger that matters.** It is also the one **this thesis cannot resolve** — it
requires a future filing.

### T-2 · The AMZN merger closes — **a clock, not a test**

**Datum:** GSAT is acquired by **AMZN at $90.00 per share.**
**Threshold:** on close, **the security ceases to exist** and `standalone_pre_merger` becomes
historical rather than current. **No further quarterly comparison is possible.**

**Recorded as a clock rather than a test:** it does not move a number, it **ends the series.**
**This artifact expires at close**, and the correct handling then is a **holdings-level
read-through**, not a re-run.

### T-3 · A wholesale-capacity contract turns

**Datum:** wholesale capacity is **`40,114` — 61.9% of revenue — and it FELL 5.4%** (`42,414` to
`40,114`). **It is the largest single line and the entire tier's most concentrated exposure.**
**Threshold:** **the line is not subscriber-driven** (issuer, p.33), so it does not move with the
803,980 subscriber base — **it moves with individual capacity contracts.** A single contract
renewal or loss **moves more revenue than every other line combined moved this quarter.**

**This trigger can fire in either direction and would dominate everything else in the filing.**

### T-4 · XCOM technology development commercializes — **or does not**

**Datum:** cost of services rose **`4,123`**, of which **XCOM technology development `+0.6`** —
**an increase in spend on a product whose revenue is not separately disclosed.**
**Threshold:** GSAT reports the cost line but **not a corresponding XCOM revenue line.** If XCOM
reaches disclosure, the `4,123` increase reclassifies from *cost pressure* to *investment*; if it
does not appear within a few quarters, **it is cost pressure.**

**Recorded as a trigger with a soft threshold**, and flagged as such: **the filing gives no way
to date it.**

### T-5 · The CARES Act retention credit's comparison base rolls off

**Datum:** p.35 records CARES Act retention credits in **2025** that are **non-recurring** —
**a 2025 benefit that inflates the prior-year base and makes the 2026 increase look larger.**
**Threshold:** **2025's benefit expires from the comparison in Q3 2026** (when the prior-year
quarter is Q3 2025 — *which also carried the credit*), so **the effect persists through the
current fiscal year and ends at Q1 2027.**

**So T-5 predicts the opex increase will look SMALLER in Q1 2027 for a reason that has nothing to
do with operations** — a base effect, stated in advance so a later reader does not mistake it for
improvement.

### T-6 · ARPU coverage changes

**Datum:** ARPU is published for lines carrying **`18,831` of `64,772` = 29.1% of revenue**; the
issuer **declines to publish it** for wholesale capacity (61.9%) and government (1.6%).
**Threshold:** if GSAT begins publishing a per-subscriber metric for wholesale capacity, **the
29.1% coverage changes and any series built across the break is inadmissible.** **Conversely, if
the ARPU lines' share of revenue keeps falling**, the published ARPU becomes progressively less
representative of the company **without any change in the disclosure** — **a silent
representativeness decay**, which is worse than a disclosed break.

## 2. Aggregate

| # | Trigger | Type | Can move the verdict? |
|---|---|---|---|
| T-1 | "primarily" is quantified — **break-even at `s = 45.9%`** | **disclosure** | **YES — the interval straddles zero** |
| T-2 | AMZN closes | clock | no — ends the series |
| T-3 | Wholesale contract turns | event | **YES — dominates** |
| T-4 | XCOM commercializes | soft | partly — reclassifies |
| T-5 | CARES base rolls off | base effect | no — affects the *appearance* |
| T-6 | ARPU coverage changes | basis | **YES — invalidates the series** |

> ### ✅ AND THIS IS THE STRUCTURAL CONTRAST WITH IRDM'S TRIGGER SET
> **At IRDM, five of six triggers could not move the falsifier across its bar** — the metric was
> bounded and the triggers sat outside the bound. **At GSAT, three of six can.**
>
> **The difference is what each conclusion rests on.** **IRDM's rests on an arithmetic bound** —
> `[50.5%, 64.6%]` computed from filed cells, robust to any reattribution. **GSAT's rests on a
> WORD** — *"primarily"* — and **a word can be replaced by a number in the next filing.**
>
> **So the two names in this pair have opposite exposure profiles:** IRDM's conclusion is
> **arithmetically robust and evidentially thin** (it survives because the metric is
> ill-conditioned, not because it was tested); GSAT's is **evidentially sharp and
> disclosure-dependent** (one sentence in a future 10-Q can move it several points).
> **Recorded as the pair's joint finding, because neither name's trigger set shows it alone.**

**Carried, not resolved:** whether T-4's soft threshold should be recorded as a trigger at all,
given that **no filing can date it.** The register's rule is that a check which cannot be
evaluated is reported as itself — **so T-4 is recorded as `UNDATEABLE` rather than as pending.**

---

**Sources.** [GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5) — the statements of operations ·
[GSAT 10-Q p.33](https://agentii.ai/v/GSAT/sec166/33) — revenue by service type and the
subscriber-driven statement · [GSAT 10-Q p.35](https://agentii.ai/v/GSAT/sec166/35) — the MG&A
variance and the transaction-cost attribution.
