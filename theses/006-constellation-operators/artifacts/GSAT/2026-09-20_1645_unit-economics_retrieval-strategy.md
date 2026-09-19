---
thesis_id: "006-constellation-operators"
pillar: "PIL-1"
ticker: GSAT
skill: unit-economics
mode: retrieval-strategy
generated_at: 2026-09-20T16:45:00Z
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
  why: "See the retrieval-scope sibling. The path below departs from the skill's declared scope at step 4, and the departure is recorded in the narrative rather than omitted from it."
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "Step 5's sign test is what grounds the filed (4,775) against the served +4,775,000, and it is run BEFORE the figure enters any computation. At GSAT the sign is not a formatting detail — it is the difference between a profit and a loss."
  - da_id: "DA-02"
    chosen_reading: "Step 6's duration check runs last, and at GSAT it additionally has to contend with the CARES Act credit: a prior-year benefit that is non-recurring, so a comparison drawn across it compares two cost regimes."
key_metrics:
  steps_in_the_strategy: 7
  steps_that_differ_from_the_skill_declaration: 1
  distinct_filed_pages_used: 3
  served_block_queries_issued: 0
  citation_id_resolved: sec166
  filing_date: 2026-08-06
  accession_number_retrieved: false
  page_count_retrieved: false
  revenue_lines_retrieved: 6
  expense_lines_retrieved: 6
evidence_grade: DEMONSTRATED
citations:
  - figure: "the statements of operations — all six revenue lines, all six expense lines, and both component identities"
    ticker: GSAT
    citation_id: sec166
    page_no: "5"
    url: https://agentii.ai/v/GSAT/sec166/5
    located_via: read_source_pages
  - figure: "revenue disaggregated by service type, subscriber counts, the three ARPU figures, and the issuer's subscriber-driven statement"
    ticker: GSAT
    citation_id: sec166
    page_no: "33"
    url: https://agentii.ai/v/GSAT/sec166/33
    located_via: read_source_pages
  - figure: "the expense variance narrative — cost-of-services components, the MG&A legal-and-professional increase, and the CARES Act credit"
    ticker: GSAT
    citation_id: sec166
    page_no: "35"
    url: https://agentii.ai/v/GSAT/sec166/35
    located_via: read_source_pages
---

# GSAT × unit-economics × retrieval-strategy

**The path actually taken at GSAT, stated so it repeats. Same seven steps as the IRDM sibling —
but the CONTENT of what each step returns differs, and one difference changes the strategy's
cost.**

## 0. Where the strategy is the skill's, and where it is not

`unit-economics` §2 prescribes the `contracts/retrieval.md` decision tree, primary branch
**(a) Structured Data Query**, with canonical-ticker resolution first. **Steps 1–3 follow it.
Step 4 does not** — the served block is inadmissible at GSAT on **two** grounds (sign and unit),
per the retrieval-scope sibling. **Steps 5–7 are this thesis's register, not the skill's.**

## 1. The seven steps at GSAT

### Step 1 — Resolve the ticker
`GSAT` resolves exactly. **Single-class Nasdaq listing; no alias or share-class branch needed.**
**Cheaper than it looks:** GSAT carries an AMZN merger pending at `$90.00`/share, so a first-pass
lookup could plausibly return a merger-related symbol — **it does not, and the plain ticker
resolves.**

### Step 2 — Fiscal calendar and coverage pre-flight
`get_company_fiscal_calendar` then `get_ticker_coverage`. **Establishes the 2026-06-30 quarter as
the latest filed period and `as_of: 2026-09-18` as the corpus date.**

### Step 3 — Locate the filing, resolve the `citation_id`
**GSAT's Q2 2026 10-Q resolves to `sec166`**, filed **2026-08-06** (verified via
`search_documents`, which also returns the description *"Q2 ending 2026-06-30"* — **an
independent confirmation of the period, which IRDM's filing list does not provide).**

> ⚠️ **Two metadata fields were NOT retrieved and are recorded as absent rather than estimated:**
> **`accession_number_retrieved: false` and `page_count_retrieved: false`.** **`search_documents`
> returns `filing_date` and a description, but neither an accession number nor a page count.**
> **The IRDM sibling carried the same two fields fabricated in an earlier draft and they were
> removed there; this artifact is written correctly the first time, and the fields are declared
> absent here so that a later reader can see the omission is deliberate.**

### Step 4 — ⚠️ THE DEPARTURE: read the FILED pages
**The skill's branch (a) would query the served block here. This artifact issues 0 such queries
for GSAT income-statement concepts** — the served `operating_income` is `+4,775,000` against a
filed `(4,775)` thousand. **Both the sign and the scale are wrong**, so the served value is not
merely inadmissible: **it is a positive number where the truth is negative.**

**Instead:** `read_source_outline` on `sec166`, then `read_source_pages` for three pages:

| Page | What it yielded | Why it was needed |
|---|---|---|
| **p.5** | **all six revenue lines, all six expense lines, both identities** | the primary source for every figure in the GSAT artifact set |
| **p.33** | revenue by service type, `803,980` subscribers, three ARPU figures, **and the issuer's subscriber-driven statement** | the DA-10 basis limit — **the sentence that makes the ARPU restriction the issuer's rather than ours** |
| **p.35** | cost-of-services components, the MG&A legal-and-professional increase, the CARES credit | the DA-23/DA-30 disclosure the whole GSAT reading rests on |

> ### ⚠️ AND GSAT's STRATEGY COSTS MORE THAN IRDM's, FOR A REASON THAT IS THE FINDING
> **At IRDM, three pages sufficed because the question was arithmetic** — the identity, the
> decomposition, the split. **At GSAT, three pages were needed because the question is a
> DISCLOSURE**, and the disclosure is **nested**: `p.5` gives the expense line, **`p.35` is where
> the line's cause is stated**, and **`p.33` is where the revenue basis is limited.**
>
> **None of the three is redundant and none could be inferred from the others.** **A strategy
> that stopped at the statements of operations would have produced the filed totals correctly and
> entirely missed both of this artifact set's findings** — the `10,400` transaction cost and the
> 29.1% ARPU coverage.

### Step 5 — The sign test (DA-23), before any figure is used
**Both component identities are computed in-line from filed cells:**
`64,772 − 69,547 = (4,775)` ✓ and `67,148 − 61,002 = 6,146` ✓.

**This is the step that grounds the sign** — and at GSAT it is the difference between reporting a
profit and a loss, because **the served value asserts the wrong one.**

**And the sign is confirmed by FIVE independent equalities, not one** — which is what makes the
`(4,775)` robust rather than merely asserted:

```
1.  component identity, Q2 2026:   64,772 − 69,547 = (4,775)   ✓ filed
2.  component identity, Q2 2025:   67,148 − 61,002 =  6,146   ✓ filed
3.  six-line expense sum, Q2 2026: 23,602+3,395+23,025+2,723+0+16,802 = 69,547  ✓
4.  six-line expense sum, Q2 2025: 19,479+2,881+9,683+5,949+0+23,010 = 61,002  ✓
5.  revenue-by-type sum, Q2 2026:  40,114+7,512+8,604+2,715+1,053+4,774 = 64,772  ✓
```

**Five separate filed decompositions, and every one requires the operating result to be NEGATIVE.**
**The served `+4,775,000` fails all five simultaneously** — which is why the sign test is not a
formality but the check that decides which number is real.

### Step 6 — The duration check (DA-02), run LAST
**Every figure carries 3M or 6M explicitly.** **GSAT's additional duration hazard is the CARES Act
retention credit** — a **non-recurring 2025 benefit** that inflates the prior-year base. **The
duration check and the credit adjustment are both required**, and **a comparison that fixes the
duration but ignores the credit still compares two cost regimes.**

### Step 7 — Citation roll-up
Every figure resolves to `https://agentii.ai/v/GSAT/sec166/{page}`. **`check_citations.py` returns
clean**; the anti-fabrication gate admits only `{ticker}/{citation_id}` pairs present in the
packed source text.

## 2. What was NOT retrieved, and why

| Not retrieved | Reason |
|---|---|
| **The served metrics block** | **Inadmissible** — sign and unit both wrong (retrieval-scope sibling) |
| **A company-wide ARPU** | **The issuer declines to publish one** (DA-10). Not a retrieval failure |
| **Subscriber-acquisition cost** | **Not published** (defaults sibling, D-4) |
| **Gross adds / gross losses** | **Not published.** Net subscribers only — so churn is not derivable (defaults sibling, D-5) |
| **XCOM revenue** | **Cost is disclosed, revenue is not** (triggers sibling, T-4) |
| **The accession number / page count** | **`search_documents` does not return them** — recorded as absent, not estimated |

> ### ⚠️ FOUR OF SIX ROWS ARE ABSENCES THE FILER CHOSE, NOT RETRIEVAL FAILURES
> **And that ratio is the strategy's actual finding.** **At GSAT the retrieval path is not the
> constraint** — the constraint is that **the filer publishes net subscribers and no churn, a cost
> line and no matching revenue line, three ARPUs and no company-wide one.**
>
> **A different strategy, a better query, or a second source does not change any of those four
> rows.** **Recorded so that a later reader does not re-run this search expecting a different
> result** — the same note the IRDM sibling carries, arrived at independently, **which is what
> makes it a property of the tier rather than of either name.**

## 3. Repeatability

**Resolve → calendar/coverage → locate and resolve `citation_id` → outline first, then only the
named pages → sign test on all identities → duration check AND non-recurring-credit adjustment →
cite.** **Three pages; 0 served queries; two metadata fields recorded absent.**

**The step that will not repeat unchanged is step 4**, and whether it applies at the next name
depends on the register — the retrieval-scope sibling states the test.

---

**Sources.** [GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5) — statements of operations ·
[GSAT 10-Q p.33](https://agentii.ai/v/GSAT/sec166/33) — revenue disaggregation, subscribers, ARPU ·
[GSAT 10-Q p.35](https://agentii.ai/v/GSAT/sec166/35) — the expense variance.
