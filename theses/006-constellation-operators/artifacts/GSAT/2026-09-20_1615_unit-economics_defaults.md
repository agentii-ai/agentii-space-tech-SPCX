---
thesis_id: "006-constellation-operators"
pillar: "PIL-1"
ticker: GSAT
skill: unit-economics
mode: defaults
generated_at: 2026-09-20T16:15:00Z
constitution_pin: "1.6.0"
assumption_pin: "2"
skill_pin: "80483892ed01"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
deal_security_basis: standalone_pre_merger
definitions_used:
  - da_id: "DA-10"
    chosen_reading: "GSAT publishes subscriber counts but NOT a company-wide ARPU, because the issuer states 61.9% of revenue is not subscriber driven. The default is therefore a BOUNDED-BASIS ARPU — computed only over the lines the issuer publishes it for — and never a company-wide figure."
  - da_id: "DA-02"
    chosen_reading: "The skill's `lookback_quarters: 4` default is inadmissible here for the same reason as at IRDM, and additionally because GSAT's CARES Act credit makes the 2025 comparison base non-recurring — a window spanning the credit's introduction would be comparing different regimes."
  - da_id: "DA-30"
    chosen_reading: "Every default names its denominator. The ARPU default at GSAT is the register's clearest case: 29.1% or 31.4% depending on the denominator, and quoting either without naming it is the defect."
key_metrics:
  defaults_declared: 7
  defaults_resolving_to_absence: 3
  defaults_carrying_a_numeric_value: 4
  skill_default_lookback_quarters: 4
  skill_default_admissible_at_this_tier: false
  replacement_lookback_quarters: 6
  gsat_cac_available: false
  gsat_ltv_available: false
  gsat_churn_available: false
  gsat_payback_available: false
  gsat_subscriber_count_available: true
  gsat_company_wide_arpu_available: false
  gsat_per_unit_possible_on_share_of_revenue: 0.2907
  arpu_covered_revenue_usd_k: 18831
  subscribers_total: 803980
  deal_cost_share_lower_bound: 0.50
  deal_cost_share_upper_bound: 1.0
evidence_grade: DEMONSTRATED
citations:
  - figure: "the statements of operations and the six expense lines"
    ticker: GSAT
    citation_id: sec166
    page_no: "5"
    url: https://agentii.ai/v/GSAT/sec166/5
    located_via: read_source_pages
  - figure: "revenue by service type, subscribers 803,980, the three ARPU figures, and the statement that wholesale capacity and government revenue are not subscriber driven"
    ticker: GSAT
    citation_id: sec166
    page_no: "33"
    url: https://agentii.ai/v/GSAT/sec166/33
    located_via: read_source_pages
  - figure: "the expense variance, the legal-and-professional increase attributed to merger transaction costs, and the CARES Act retention credit"
    ticker: GSAT
    citation_id: sec166
    page_no: "35"
    url: https://agentii.ai/v/GSAT/sec166/35
    located_via: read_source_pages
---

# GSAT × unit-economics × defaults

**The assumptions this analysis runs on where no filed figure exists — and GSAT's set is
substantially BETTER than IRDM's, in a way that is itself a finding.**

## 0. The contrast that structures this artifact

**IRDM publishes no subscriber count, so per-unit economics are unavailable at IRDM on
principle** (IRDM defaults sibling, D-5). **GSAT publishes `803,980` subscribers, `781,470` a year
earlier — `+2.9%`.** **So at GSAT, a per-subscriber metric IS computable.**

**⚠️ But only over the lines the issuer publishes ARPU for — and those carry `18,831` of
`64,772` revenue, `29.1%`.** **So GSAT's defaults are not divided into "available" and
"unavailable" as IRDM's are; they are divided into *available on a partial basis* and
*unavailable*.** **A partial-basis metric is more dangerous than an absent one**, because it can be
quoted without its restriction and look complete.

## 1. D-1 · ARPU — **available, BOUNDED, and the bound must travel with the number**

**What it stands in for:** revenue per subscriber.

**What GSAT files — the three published figures, p.33:**

| Line | ARPU | Revenue | Share of total |
|---|---:|---:|---:|
| IoT | **$4.31** | 7,512 | 11.6% |
| SPOT | **$13.81** | 8,604 | 13.3% |
| Duplex | **$57.44** | 2,715 | 4.2% |
| **ARPU-covered** | | **18,831** | **29.1%** |

**What the issuer says, verbatim:** *"**None of these service revenue items are subscriber
driven.** Accordingly, we do not present ARPU for wholesale capacity services revenue or
government and other services revenue."*

**Set to:** **a BOUNDED-BASIS ARPU over the three published lines only.**

> ### ⚠️ AND THE BOUND IS THE DEFAULT'S MOST IMPORTANT PROPERTY
> **A "GSAT ARPU" computed over all subscribers would divide `64,772` by `803,980` and produce
> `$80.56` a quarter** — **a number the issuer explicitly declines to construct, over a
> denominator that includes a capacity line that is not subscriber-driven.** **That figure is
> WRONG, it is easy to compute, and nothing in the filing stops a reader from computing it.**
>
> **The correct usage carries its restriction every time it appears** — `$4.31` (IoT), `$13.81`
> (SPOT), `$57.44` (Duplex) — **and never a blended figure.** **The register's DA-30 rule is that
> a percentage must name its denominator; this is the case where a RATIO must name its
> population**, which is the same rule applied one step further out.

## 2. D-2 · `lookback_quarters` — **inadmissible, for IRDM's reason AND a second one**

**The skill's default:** `lookback_quarters: 4`.

**Reason one (shared with IRDM):** four quarters spans a fiscal year and **GSAT's disclosures mix
3M and 6M durations** (DA-02).

**Reason two (GSAT's own):** p.35 records **CARES Act retention credits in 2025 that are
non-recurring** — **a 2025 benefit that inflates the prior-year comparison base.** **A four-quarter
window spanning the credit's presence and absence compares two different cost regimes** and would
attribute the difference to operations.

**Set to:** **6 quarters, read as six discrete 3M periods** — and, additionally, **the CARES credit
is carried as a named adjustment in any YoY comparison until it has rolled out of the window
entirely.**

## 3. D-3 · The deal-cost share — **a bounded parameter, and the bound is the point**

**What it stands in for:** the fraction `s` of the `10,400` legal-and-professional increase that is
transaction cost. **GSAT says *"primarily"* and gives no number.**

**Set to:** a **range**, `s ∈ [0.50, 1.00]` — the lower bound being the ordinary meaning of
*"primarily"* (`>50%`), the upper being the literal bound (the whole fee increase).

**What that implies, computed in the triggers sibling:** ex-deal-cost operating margin lies in
**`[+0.66%, +8.68%]`** — **and the break-even `s = 45.9%` sits BELOW the lower bound, so every value
in the adopted range produces a POSITIVE ex-deal-cost margin.**

> ⚠️ **This is the one place in the pair where a default is doing real analytical work, and it is
> stated as a range precisely so that it cannot be mistaken for a point.** **The comparison:
> IRDM's D-3 is a range because the filer did not disclose; GSAT's D-3 is a range because the filer
> used a word instead of a number.** **Same shape, different cause** — and **GSAT's is the more
> fragile**, because **a word can be replaced in the next filing and IRDM's silence cannot.**

## 4. D-4 through D-7

| ID | Default | Set to | Basis |
|---|---|---|---|
| **D-4** | **CAC** | **ABSENT** | **GSAT DOES decompose MG&A** — unlike IRDM — into legal/professional `+10,400` and personnel `~+1,800`. **But neither is subscriber acquisition**, and there is no acquisition sub-line. |
| **D-5** | **Churn rate** | **ABSENT** | **The subscriber COUNT exists; the churn rate does not.** A churn rate requires a cohort or a gross-adds/gross-losses split, **and GSAT publishes net subscribers only.** ⚠️ **`+2.9%` net is compatible with almost any churn rate** — a company with 30% annual churn and heavy acquisition shows the same net figure as one with 3% churn. **The published number cannot distinguish them.** |
| **D-6** | **Payback period** | **ABSENT** | Requires D-4. |
| **D-7** | **Per-unit revenue contribution** | **computable, bounded** | `18,831 / 803,980 = ` **$23.42 per subscriber per quarter**, **over the ARPU-covered lines only.** ⚠️ **Against total revenue the same division gives `$80.56` — a 3.4× difference that is entirely a population choice.** |

> ### ⚠️ D-5 IS THE SUBTLEST ABSENCE IN EITHER ARTIFACT SET
> **GSAT publishes `803,980` subscribers and it is tempting to treat a subscriber series as a unit
> economics series.** **It is not one.** **Net subscribers is a stock; unit economics needs
> flows** — gross adds, gross losses, cost to acquire. **A net figure of `+2.9%` is consistent
> with a stable base and with a churning one, and the filing does not separate them.**
>
> **Recorded because the number EXISTS and looks like it answers the question.** IRDM's absence is
> safe — nothing there invites the error. **GSAT's is not.**

## 5. Summary

| | IRDM | GSAT |
|---|---|---|
| Subscriber count | **absent** | **present** (`803,980`) |
| Company-wide ARPU | **absent** (and inadmissible) | **absent — issuer declines** |
| Bounded ARPU | absent | **present on 29.1% of revenue** |
| Churn | absent | **absent, despite a count existing** |
| CAC / LTV / payback | absent | absent |
| Cost decomposition | **single SG&A line** | **partially decomposed** |
| Deal cost | **disclosed as a total** (`14,300`) | **disclosed as a word** (*"primarily"*) |
| Net defaults usable as-is | **1 of 7** | **4 of 7** |

**Both names remain unable to support the skill's core outputs — CAC, LTV, churn, payback — and
that is a property of the tier, not of either filer.** **GSAT's advantage is real but narrow: it
can compute per-subscriber revenue on less than a third of its business, and it cannot compute
per-subscriber cost or retention at all.**

---

**Sources.** [GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5) — the statements of operations ·
[GSAT 10-Q p.33](https://agentii.ai/v/GSAT/sec166/33) — revenue by type, subscribers, ARPU, and the
subscriber-driven statement · [GSAT 10-Q p.35](https://agentii.ai/v/GSAT/sec166/35) — the expense
variance, the transaction-cost attribution, and the CARES Act credit.
