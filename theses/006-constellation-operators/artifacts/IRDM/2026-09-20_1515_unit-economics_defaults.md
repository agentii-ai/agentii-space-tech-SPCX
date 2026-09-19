---
thesis_id: "006-constellation-operators"
pillar: "PIL-1"
ticker: IRDM
skill: unit-economics
mode: defaults
generated_at: 2026-09-20T15:15:00Z
constitution_pin: "1.6.0"
assumption_pin: "2"
skill_pin: "80483892ed01"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
deal_security_basis: standalone_pre_merger
definitions_used:
  - da_id: "DA-02"
    chosen_reading: "The skill's `lookback_quarters: 4` default is INADMISSIBLE as written at this tier — see D-2. The default silently blends 3M and 6M durations across a fiscal year, which is the exact trap DA-02 names. A replacement default is stated rather than the default being used unnoticed."
  - da_id: "DA-30"
    chosen_reading: "Every default below names what it divides by. A default that would produce an unnamed-denominator percentage is recorded as ABSENT rather than estimated."
  - da_id: "DA-10"
    chosen_reading: "Where the skill's headline outputs require a basis the filer does not publish, the default is ABSENCE, not a constructed value. Constructing a CAC from a total sales-and-marketing line is the error this register exists to prevent."
key_metrics:
  skill_default_lookback_quarters: 4
  skill_default_admissible_at_this_tier: false
  replacement_lookback_quarters: 6
  defaults_declared: 7
  defaults_resolving_to_absence: 5
  defaults_carrying_a_numeric_value: 3
  irdm_cac_available: false
  irdm_ltv_available: false
  irdm_churn_available: false
  irdm_payback_available: false
evidence_grade: DEMONSTRATED
citations:
  - figure: "the results-of-operations table — the expense lines from which no subscriber-acquisition cost can be isolated"
    ticker: IRDM
    citation_id: sec191
    page_no: "24"
    url: https://agentii.ai/v/IRDM/sec191/24
    located_via: read_source_pages
  - figure: "the R&D step-up and the transaction cost disclosure"
    ticker: IRDM
    citation_id: sec191
    page_no: "26"
    url: https://agentii.ai/v/IRDM/sec191/26
    located_via: read_source_pages
---

# IRDM × unit-economics × defaults

**The assumptions this analysis runs on where no filed figure exists. Seven declared, and five of
them resolve wholly or partly to ABSENCE rather than to a number — which is the finding.**

## 0. The rule this artifact is written under

**A default is a value used in the absence of a filed figure.** Its danger is not that it is
wrong; it is that **it is invisible once used** — a computed result does not carry a mark saying
which of its inputs were assumed. **So each default below is stated with three things: what it
stands in for, what it is set to, and what would replace it if the filer published it.**

**And the register adds a fourth requirement at this tier:** *a default may not manufacture a
basis the filer declined to publish.* Where that is the only way to produce the skill's named
output, **the correct default is ABSENCE.**

## 1. D-1 · Subscriber-acquisition cost (CAC) — **ABSENT, and it cannot be anything else**

**What it stands in for:** `unit-economics`'s first named output is **CAC** — cost to acquire a
subscriber. It requires subscriber-acquisition spend isolated from general selling expense.

**What IRDM files:** a single **`Selling, general and administrative`** line — **`67,044`**, up
**`+22,417`** or **+50%**. It is **not decomposed** on p.24, and p.26 attributes the increase to
**transaction costs (`14,300`)** rather than to acquisition.

**Set to:** **ABSENT.**

**What would replace it:** a filing that splits SG&A into acquisition and non-acquisition
components. **IRDM has never published one and there is no reason to expect it to.**

> ### ⚠️ AND THE TEMPTATION IS EXACTLY WHAT DA-30 FORBIDS
> **A careless analysis would take `67,044` as the acquisition denominator** and produce a
> "CAC" of roughly `$67M / (subscriber adds)`. **That number would be wrong by construction** —
> **`14,300` of it is deal cost, and the rest is corporate overhead, engineering, and the
> professional fees of a merger, none of which acquires a subscriber.** **The register's rule is
> that a percentage whose denominator has not been named is inadmissible; this is the case where
> the denominator cannot be named at all.** Recorded as absence.

## 2. D-2 · `lookback_quarters` — **the skill's own default is inadmissible here**

**The skill's default:** `lookback_quarters: 4` (`SKILL.md` Defaults table, rationale *"Standard
lookback for this skill type"*).

**Why it cannot be used:** **four quarters spans a fiscal year, and IRDM's disclosures mix 3M and
6M durations within one table** (DA-02). A four-quarter window will **pick up 3M figures from some
quarters and 6M figures from others**, and the resulting series is not a series — it is a
concatenation of two different objects. **The default is not merely suboptimal at this tier; it
is the specific trap DA-02 was written about.**

**Set to:** **6 quarters**, read **as six discrete 3M periods**, never as three 6M periods and
never as a trailing-twelve-month sum.

**What would replace it:** nothing. **This is a permanent replacement, not a placeholder** — the
duration discipline is a property of the filings, not of this analysis.

## 3. D-3 · The cost-of-services split — **the one default with a real value, and it is a RANGE**

**What it stands in for:** the split of `Cost of services` (`51,314`) between the licensed
service line and the engineering-and-support line, **which IRDM does not publish**.

**Set to:** **not a point — a bounded range**, `[50.5%, 64.6%]` on P1's falsifier, computed by
**attributing the whole `(2,289)` decline to each line in turn.** The falsifier passes at both
endpoints.

**Why a range rather than a midpoint:** **a midpoint would be a fabricated figure with no filed
support.** A range whose endpoints are *computable from filed cells under stated extreme
assumptions* is a different kind of object: **every value in it is defensible, the extremes are
exactly stated, and the conclusion is invariant across it.** The register permits this; it does
not permit the midpoint.

## 4. D-4 through D-7 · The remaining four, all of which lose either their basis or their unit

| ID | Default | Set to | Basis |
|---|---|---|---|
| **D-4** | **LTV** | **ABSENT** | Requires CAC (D-1) and a churn rate. **Neither exists.** LTV is not estimable here at any confidence. |
| **D-5** | **Churn rate** | **ABSENT** | IRDM files **no subscriber count** on p.24 or p.26. **A churn rate requires a denominator this filer does not publish** — the same shape as the ARPU problem at GSAT, in the acquisition direction. |
| **D-6** | **Payback period** | **ABSENT** | Requires both D-1 and D-4. |
| **D-7** | **Gross margin per unit** | **the "per unit" is ABSENT; the company margin is computable** | **`15.10%`** operating. ⚠️ **Gross margin carries TWO different denominators and they differ by 9.0 points** — `(225,237 − 51,314) / 225,237 = ` **77.22%** against **total revenue**; `(161,328 − 51,314) / 161,328 = ` **68.19%** against **Services revenue**. **Neither may be quoted without its denominator.** And **"per unit" is not computable at all**: IRDM publishes **no subscriber count**, so there is no unit — see D-5. |
| — | **Contribution margin** | **`34,008 / 225,237 = 15.10%`** | Computable and filed. §1 of the methodology sibling. |

> ### ⚠️ FIVE OF SEVEN DEFAULTS RESOLVE TO ABSENCE, AND THAT IS THE RESULT
> **`unit-economics` names eleven things — unit economics, CAC, LTV, churn, gross margin per unit,
> customer economics, subscription economics, per-unit profitability, contribution margin,
> payback period, cohort economics.** **At IRDM, everything that requires a UNIT COUNT is
> unavailable**, because **the filer publishes segment and line economics, not customer
> economics** — and **D-1, D-4, D-5, D-6 and D-7's per-unit half all fail on that same missing
> denominator.**
>
> **This is not a data gap that better retrieval would close.** It is a **basis mismatch between
> the skill's named outputs and what satellite operators disclose** — and it will repeat at every
> name in the tier, because **no constellation operator files subscriber-acquisition cost or
> cohort retention.** **Recorded here as the defaults artifact's finding rather than as a
> per-name limitation**, because it is a property of the tier and not of IRDM.

## 5. What this artifact does NOT do

- **No midpoint substituted for D-3's range.**
- **No CAC proxy built from SG&A.** `67,044` is not an acquisition denominator.
- **No served figure.** Same DA-30/DA-29 exposure as the methodology sibling.
- **No 4-quarter default window** (D-2), and the replacement is stated rather than assumed.

---

**Sources.** [IRDM 10-Q p.24](https://agentii.ai/v/IRDM/sec191/24) — the expense lines from which
no subscriber-acquisition cost can be isolated ·
[IRDM 10-Q p.26](https://agentii.ai/v/IRDM/sec191/26) — the R&D step-up and the transaction cost
disclosure.
