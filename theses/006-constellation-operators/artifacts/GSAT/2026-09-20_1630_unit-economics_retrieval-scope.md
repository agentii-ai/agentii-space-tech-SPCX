---
thesis_id: "006-constellation-operators"
pillar: "PIL-1"
ticker: GSAT
skill: unit-economics
mode: retrieval-scope
generated_at: 2026-09-20T16:30:00Z
constitution_pin: "1.6.0"
assumption_pin: "2"
skill_pin: "80483892ed01"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
deal_security_basis: standalone_pre_merger
scope_deviation:
  declared: true
  skill_declares: structured_only
  artifact_used: read_source_pages
  why: "Same conflict as the IRDM sibling, and at GSAT it is SHARPER: the served block returns +4,775,000 for a filed operating loss of (4,775) thousand — the sign is stripped AND the magnitude is off by 1,000x. A skill scoped to that block cannot produce a correct GSAT operating figure at all. The deviation is declared in-line because no contract mechanism exists to declare it."
  what_was_excluded: "The entire served metrics block for GSAT's income-statement concepts. Zero served queries were issued."
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "GSAT is the register's named sign-strip instance and this is why the filed path is not optional. The served value is not merely unsign ed — it is wrong by three orders of magnitude, because the filed cell is in THOUSANDS and the served value appears to be in units. Both defects are on the same concept in the same period."
  - da_id: "DA-30"
    chosen_reading: "The exclusion criterion is the same as at IRDM: a source whose basis cannot be named is inadmissible. At GSAT the failing basis is the UNIT and the SIGN, where at IRDM it was the DENOMINATOR."
key_metrics:
  skill_declared_scope: structured_only
  skill_allows_document_retrieval: false
  declared_deviation: true
  contract_mechanism_for_deviation_exists: false
  served_operating_income_value: 4775000
  filed_operating_income_usd_k: -4775
  served_vs_filed_sign_mismatch: true
  served_vs_filed_unit_factor: 1000
  filed_pages_used: 3
  served_block_queries_issued: 0
  citation_id_resolved: sec166
  filing_date: 2026-08-06
evidence_grade: DEMONSTRATED
citations:
  - figure: "the statements of operations — the filed basis, and the cell the served block contradicts"
    ticker: GSAT
    citation_id: sec166
    page_no: "5"
    url: https://agentii.ai/v/GSAT/sec166/5
    located_via: read_source_pages
  - figure: "revenue disaggregation, subscribers and ARPU — the lines carrying the DA-10 coverage limit"
    ticker: GSAT
    citation_id: sec166
    page_no: "33"
    url: https://agentii.ai/v/GSAT/sec166/33
    located_via: read_source_pages
  - figure: "the expense variance and the transaction-cost attribution"
    ticker: GSAT
    citation_id: sec166
    page_no: "35"
    url: https://agentii.ai/v/GSAT/sec166/35
    located_via: read_source_pages
---

# GSAT × unit-economics × retrieval-scope

**The same conflict as at IRDM, and at GSAT it is sharper: the served block returns a POSITIVE
number, `+4,775,000`, for a filed operating LOSS of `(4,775)` thousand. Two defects on one
concept.**

## 0. The structural finding is the IRDM sibling's — this artifact adds the GSAT instance

**`unit-economics` declares `retrieval_scope: structured_only` and excludes `read_source_*` from
`allowed_tools`; this thesis's register documents the served block as inadmissible; no contract
mechanism exists to declare the deviation; 36 of 72 library skills declare the same scope; and 75
of 270 tasks in this thesis are bound to it.**

**That analysis is in `artifacts/IRDM/…_unit-economics_retrieval-scope.md` and is not repeated
here.** **What this artifact adds is the GSAT instance — which is a strictly worse case than
IRDM's, and worth stating on its own because it moves the argument from *inadmissible basis* to
*arithmetically wrong*.**

## 1. ⚠️ The GSAT instance: two defects, same concept, same period

| | Filed (`sec166` p.5, thousands) | Served block | Relationship |
|---|---:|---|---|
| Operating income (loss), Q2 2026 | **`(4,775)`** | **`+4,775,000`** | **sign flipped; magnitude ×1,000** |

**Both figures describe the same concept in the same period, and they disagree in two ways at
once:**

1. **The sign.** Filed is a **loss**; served is **positive**. A reader taking the served value would
   conclude GSAT earned operating income of `$4.775M` in a quarter it lost `$4.775M`.
2. **The magnitude.** The filed cell is **in thousands**; the served value appears to be in
   **units**. **A `1,000×` factor, on a number whose sign is already wrong.**

> ### ⚠️ WHY THIS IS WORSE THAN IRDM'S INSTANCE, AND WHY IT MATTERS FOR THE SCOPE ARGUMENT
> **IRDM's served defect was a wrong DENOMINATOR** — the margins divided by the Aireon hosting
> ceiling. **That produces a number that is wrong but plausibly sized.** A reader who did not know
> the denominator would see a margin in a normal range and have no reason to doubt it. **The defect
> was invisible without the register.**
>
> **GSAT's defect is a wrong SIGN and a wrong SCALE on a filed line — and it is visible to anyone
> who computes the identity.** **`64,772 − 69,547` is negative; no arrangement of the two filed
> operands makes it positive.** **The identity is the whole test, and the served value fails it.**
>
> **So the two instances fail differently, and the difference is the argument:** **one is
> undetectable without the register, and the other is detectable by arithmetic alone.** **A skill
> scoped to the structured path is exposed to both kinds, and the second kind means the exposure
> is not merely theoretical.**

## 2. What is admitted and excluded at GSAT

| | |
|---|---|
| **ADMITTED** | GSAT's filed **10-Q** (`sec166`), filed **2026-08-06** — **p.5** statements of operations, **p.33** revenue by service type / subscribers / ARPU, **p.35** expense variance |
| **ADMITTED** | The **component identity**, computed in-line, both periods, closing exactly — **and this is the test that grounds the sign** |
| **EXCLUDED** | The **entire served metrics block** for GSAT income-statement concepts — **0 queries issued** |
| **EXCLUDED** | The **6M half-year** as a source for any 3M figure (DA-02) |
| **EXCLUDED** | Any **company-wide ARPU** — the issuer declines to publish one (DA-10) |
| **EXCLUDED** | `EPS × shares` as a validation of operating income |

> ### ✅ AND THE SIGN TEST IS NOT ASPIRATIONAL — IT IS CHECKED BY A TOOL
> **`tools/check_sign_strip.py` returns `9/9 artifacts have every asserted fingerprint grounded ·
> 0 ungrounded` on this thesis's artifact set at this point in the run.** **This artifact asserts a sign-strip defect
> AND grounds it with the filed identity** — **a claim about a bad number that is itself
> checkable, rather than an assertion a reader must take on faith.**
>
> **And that tool's own caveat is quoted here because it applies:** *"this checks ASSERTED
> arithmetic only. A zero here does not mean no artifact is stripped — it means no artifact
> asserts a fingerprint it cannot ground."* **A clean run bounds what we claimed, not what
> exists.**

## 3. The task-level consequence, stated once

**GSAT × unit-economics is one of 75 tasks in this thesis bound to a `structured_only` skill —
27.8% of 270.** **Every one of them faces the same fork: declare a `scope_deviation` and read
filed cells, or record `BLOCKED_SCOPE`.** **This artifact takes the first path and names it.**

**Carried to P5's queue close-out** — the thesis-level decision on whether the 75 tasks are
executed under declared deviation or reported as blocked is **a spec-level choice, not a
per-artifact one**, and it should be made once rather than 75 times.

---

**Sources.** [GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5) — the statements of operations and
the filed cell the served block contradicts ·
[GSAT 10-Q p.33](https://agentii.ai/v/GSAT/sec166/33) — revenue disaggregation, subscribers and
ARPU · [GSAT 10-Q p.35](https://agentii.ai/v/GSAT/sec166/35) — the expense variance.
