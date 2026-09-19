---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-3/PIL-6"
ticker: SPCX
skill: reverse-dcf
mode: methodology
generated_at: 2026-09-19T14:35:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "b42ad3a44570"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-02"
    chosen_reading: "The base is Connectivity's 3M operating income annualised x4, stated as an annualisation of a filed quarter, not a forecast. The reverse-DCF solves for the growth implied by a price; it does not project one."
  - da_id: "DA-23"
    chosen_reading: "The earnings base is taken on the FILED sign. The served consolidated line returns +143,000,000 against a filed (143,000,000), so a reverse-DCF run on served figures would solve for growth in a quantity that does not exist."
entity_claims:
  - claim_id: "rdcf-live-market-cap"
    ticker: SPCX
    metric: market_capitalisation
    value: 2071800000000
    unit: USD
    basis: "13,567,041,680 shares x $152.71; price observed 2026-09-18"
    period: "2026Q3"
    evidence_grade: DERIVED
    source: "10-Q share count + 8-K Cursor shares + live nasdaq quote"
  - claim_id: "rdcf-connectivity-annualised-opinc"
    ticker: SPCX
    metric: annualised_operating_income
    value: 6624000000
    unit: USD
    basis: "1,656 x 4 — annualisation of the filed 3M rate"
    period: "2026Q2"
    evidence_grade: MODELED
    source: "SPCX 10-Q Note 18, filed segment operating income"
  - claim_id: "rdcf-implied-perpetual-growth-lo"
    ticker: SPCX
    metric: implied_perpetual_growth_rate
    value: 0.1468
    unit: ratio
    basis: "Gordon: r - 1/multiple = 0.15 - 1/312.8; at the constitution's 15% required return"
    period: "2026Q3"
    evidence_grade: MODELED
    source: "arithmetic on live price and filed segment income"
  - claim_id: "rdcf-implied-perpetual-growth-hi"
    ticker: SPCX
    metric: implied_perpetual_growth_rate
    value: 0.2468
    unit: ratio
    basis: "Gordon: 0.25 - 1/312.8; at the constitution's 25% required return"
    period: "2026Q3"
    evidence_grade: MODELED
    source: "arithmetic on live price and filed segment income"
key_metrics:
  live_market_cap_usd_t: 2.0718
  connectivity_annualised_opinc_usd_m: 6624
  implied_perpetual_growth_lo: 0.1468
  implied_perpetual_growth_hi: 0.2468
---

# SPCX × reverse-dcf × methodology

**What the live price implies — the price question asked backwards.** Admitted because a reverse DCF
**forecasts nothing**; it takes an observed price as given. **It never faced the FCF-history limb**
that bars a forward DCF at SPCX.

## 1. The instrument

```
Live market cap             $2.0718T     (13,567,041,680 × $152.71)
Connectivity op income      $6,624M      (filed 3M × 4 — the only positive segment)
⇒ Market-cap-to-Connectivity-income      312.8×
```

**Gordon: `P/E = 1 / (r − g)`**, so **`r − g = 1/312.8 = 0.32%`**.

| Required return `r` *(constitution: 15–25% target IRR)* | **Implied perpetual growth `g`** |
|---:|---:|
| **15%** | **14.68%** |
| **20%** | **19.68%** |
| **25%** | **24.68%** |

> ### 🔴 THE FINDING: THE IMPLIED PERPETUAL GROWTH ESSENTIALLY EQUALS THE REQUIRED RETURN
>
> **`g ≈ r − 0.32%`.** At every point in the constitution's stated range, **the growth the price
> implies is within a third of a percentage point of the return demanded.**
>
> **What that means mechanically:** when `g → r`, the Gordon denominator collapses and **the
> terminal value approaches 100% of the present value.** Virtually none of the $2.07T is paying for
> cash flows anyone can see. **It is all terminal.**

## 2. ⚠️ And that breaches F1's own terminal-value cap

**F1's surviving method carries a hard rule: *"terminal value capped at 50–70% of total EV."***
**The implied terminal share here is ~100%.** So:

| | |
|---|---|
| **F1's cap** | **50–70% of total EV** |
| **This reverse-DCF implies** | **≈100%** |
| **⇒ The price is outside F1's own admitted framework** | |

**Three readings, and the artifact reports all three rather than choosing:**

1. **The price is too high** — the market has not applied the cap the framework demands.
2. **The cap is wrong for a business at this stage** — a company whose only profitable segment has a
   **+108.3%**-growth channel may legitimately be valued as near-pure terminal.
3. **The attribution is the problem** — the 313× divides the **whole** market cap by **one**
   segment's income, which implicitly sets **Space and AI to zero**.
   **Framing (3) is the most likely and the most important: the arithmetic is not "Connectivity is
   worth 313× income" — it is "the whole company costs 313× the income of its only profitable
   segment."**

## 3. What the price implies about Space and AI

**Restated as the question it actually answers:**

> **After paying 313× for Connectivity, what is left for Space and AI?**
>
> **Nothing — by construction.** The framing sets them to **zero** and still needs a ~100% terminal
> value. **So the market is either (a) attributing the whole price to Connectivity and treating Space
> and AI as free, or (b) applying a Connectivity multiple far lower than 313× and crediting Space and
> AI with substantial value.**

**This artifact cannot distinguish (a) from (b)** — that requires the regimes, which are `MODELED`
ranges in `sotp-valuation`. **What it can state is the bound:**

| If Space + AI are worth | Then Connectivity's implied multiple is |
|---|---:|
| **$0** | **312.8×** |
| **$0.5T** | **237.3×** |
| **$1.0T** | **161.8×** |
| **$1.5T** | **86.3×** |

**Even at a generous $1.5T for the two loss-making segments, Connectivity carries 86×.** **The
finding survives every allocation** — which is what makes it a finding rather than an artefact of
framing (3).

## 4. Status — a constraint, not a licence

**Per §1c: `reverse-dcf` is a cross-check on the three regimes, in the same class as `comps` —
never primary.** Its output is *"what the live price implies"*, **not** *"what SPCX is worth."*

**Where the implied growth is absurd on its face, that is a finding about the PRICE, reported as
such.**

## 5. Hand-off

| To | What |
|---|---|
| **P3** | The **market-implied limb**: the price requires **~15–25% perpetual growth in the only profitable segment**, with the AI segment contributing **no separable value** under framing (3) |
| **P6** | The terminal-value breach of F1's 50–70% cap is a **comparability fact for the anchor** — the price sits outside the framework the anchor would use |
| **011** | **The 313× is a valuation fact, not a position.** This thesis produces no trade ideas; 011 sizes |
| **T-5 (triggers)** | If a P11 deal security normalises and the **first admissible comparator** appears, this reverse-DCF can be re-run against a **borrowed** multiple instead of a segment-derived one |
