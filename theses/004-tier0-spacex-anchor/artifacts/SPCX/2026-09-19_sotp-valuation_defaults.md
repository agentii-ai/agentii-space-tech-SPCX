---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-1/PIL-6"
ticker: SPCX
skill: sotp-valuation
mode: defaults
generated_at: 2026-09-19T14:15:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07305f5d5391"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-02"
    chosen_reading: "Duration — the annualisation below is the 3M rate x4, stated as an ANNUALISATION, never as a forecast. It is not a 6M figure doubled and it is not a projection."
  - da_id: "DA-11"
    chosen_reading: "The 1.4 GW is IT load only, excluding cooling, distribution losses, lighting, security and facility overhead — true facility draw typically 1.2-1.5x. No $/kW-revenue assumption is disclosed, so it cannot be converted into the invested-capital framing without a stated default."
entity_claims:
  - claim_id: "sotpf-annualised-connectivity-opinc"
    ticker: SPCX
    metric: annualised_operating_income
    value: 6624000000
    unit: USD
    basis: "1,656 x 4 — annualisation of the 3M rate, NOT a forecast; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: MODELED
    source: "arithmetic on filed cells; the annualisation multiplier is the default"
  - claim_id: "sotpf-live-market-cap"
    ticker: SPCX
    metric: market_capitalisation
    value: 2071800000000
    unit: USD
    basis: "13,567,041,680 shares x $152.71; price observed 2026-09-18, retrieved 2026-09-19"
    period: "2026Q3"
    evidence_grade: DERIVED
    source: "10-Q share count + 8-K Cursor shares + live nasdaq quote"
key_metrics:
  annualised_connectivity_opinc_usd_m: 6624
  live_market_cap_usd_t: 2.0718
---

# SPCX × sotp-valuation × defaults

**Every assumption the SOTP takes where no filed figure settles the question.** Each is stated so a
reader can disagree with it explicitly rather than inherit it silently.

## D-1 — Annualisation is `3M × 4`, and it is NOT a forecast

| Segment | 3M (filed) | Annualised *(×4)* |
|---|---:|---:|
| Connectivity | 1,656 | **6,624** |
| Space | (542) | **(2,168)** |
| AI | (1,257) | **(5,028)** |
| Consolidated | (143) | **(572)** |

**Why a default is needed:** the filing gives a quarter, and multiples need a year.
**Why `×4` and not `6M × 2`:** the 10-Q files both under one concept (**DA-26**), and mixing the
durations would compound two bases. **The 3M rate is the most recent and the least contaminated by
the pre-xAI comparison window.**

**What would overturn it:** a filed annual figure. **None exists for a company that IPO'd in
June 2026.** The `×4` is therefore a **stated artefact of the disclosure's window**, not a modelled
growth assumption — **and the artifact says so rather than presenting 6,624 as a number SPCX
earned.**

## D-2 — The market cap uses the PRO-FORMA share count

**Shares: 13,176,000,000 (2026-06-30) + 391,041,680 (Cursor, 2026-08-14) = 13,567,041,680.**

**Why pro-forma:** round 4 made the headline pro-forma, and the deal has now **closed** — so
**pre-close is the counterfactual, not the base case.** Using 13.176bn would price a company that no
longer exists.

**What is excluded and why:** the **73,493,373** assumed RSUs and options are **contingent**, so
they enter as a **dilution note**, not in the denominator. **Including them would be a default the
filings do not support.**

## D-3 — The AI segment's invested-capital basis needs a default the filing does not give

**Round 4's confirmed headline is INVESTED CAPITAL**, using the H1 2026 capex attributed *"first to
the build out of DATA CENTERS and related infrastructure."*

**The default that follows, and its limit:** **the filing does not disaggregate that capex by
segment.** So the invested-capital figure is **an allocation of a company-wide number**, not a filed
AI-segment number. **Default taken: report it as a company-level attribution with the allocation
stated, never as a filed segment figure.**

**What would overturn it:** a segment-level capex disclosure. **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`
on the pages read.**

## D-4 — Risk-free and duration inputs come from the constitution, not from a model

**Required return: a stated target IRR, not WACC** — per F1's surviving method, **15–25%**. And the
constitution's macro triggers (**10Y > 5.25%**, or a Fed pivot) are the **scenario-weight inputs**,
not background.

**Default:** the 10Y is taken at the constitution's recorded **4.80%**, with **30Y at 5.26%**, both
at three-year highs. **No live rate was fetched** — the live feed is an equity quote source, and
**a rate fetched from a different source would be a second basis, not an update.**

## D-5 — What this artifact deliberately does NOT default

| Question | Default? |
|---|---|
| Space's multiple | **No** — DA-06: **no external multiple is borrowed**. Value from contribution |
| Connectivity's multiple | **No** — all satellite comparables are `P11` or `PARTIAL` |
| AI's multiple | **No** — headline is invested capital, and the other two framings are reported alongside |
| A single blended multiple | **No — barred.** "Valuing the three at one rate is not a simplification. It is a different claim" |
| A point estimate | **No** — every regime is a range |

## Summary

| # | Default | Grade | Overturned by |
|---|---|---|---|
| **D-1** | Annualise `3M × 4` | `MODELED` | A filed annual figure — none exists |
| **D-2** | Pro-forma share count; contingent awards excluded | `DERIVED` | The contingent awards vesting |
| **D-3** | Invested capital is a **company-level attribution** | `MODELED` | Segment-level capex disclosure |
| **D-4** | 15–25% target IRR; 10Y at the constitution's 4.80% | `MODELED` | A live rate from a stated source |
| **D-5** | No default where a multiple would be invented | — | — |
