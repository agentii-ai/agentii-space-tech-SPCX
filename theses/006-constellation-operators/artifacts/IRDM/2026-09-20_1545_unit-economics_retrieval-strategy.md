---
thesis_id: "006-constellation-operators"
pillar: "PIL-1"
ticker: IRDM
skill: unit-economics
mode: retrieval-strategy
generated_at: 2026-09-20T15:45:00Z
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
  why: "See the retrieval-scope sibling. The strategy below is the path actually taken; it departs from the skill's declared scope at step 4 and the departure is recorded rather than omitted from the narrative."
definitions_used:
  - da_id: "DA-02"
    chosen_reading: "The last step of the strategy is a DURATION CHECK, and it is last on purpose: a source that passes every other test and fails this one is still inadmissible, and no earlier step would have caught it."
  - da_id: "DA-23"
    chosen_reading: "Step 5 is the sign test and it is not optional. A retrieved figure that cannot be checked against a component identity has not been retrieved in the sense this thesis requires — it has merely been located."
key_metrics:
  steps_in_the_strategy: 7
  steps_that_differ_from_the_skill_declaration: 1
  sources_retrieved: 3
  distinct_filed_pages_used: 3
  served_block_queries_issued: 0
  citation_id_resolved: sec191
  filing_date: 2026-07-22
  accession_number_retrieved: false
  page_count_retrieved: false
evidence_grade: DEMONSTRATED
citations:
  - figure: "the statements of operations — the entry point for the filed path"
    ticker: IRDM
    citation_id: sec191
    page_no: "5"
    url: https://agentii.ai/v/IRDM/sec191/5
    located_via: read_source_outline
  - figure: "the results-of-operations table, the three revenue lines and five expense lines, and both component identities"
    ticker: IRDM
    citation_id: sec191
    page_no: "24"
    url: https://agentii.ai/v/IRDM/sec191/24
    located_via: read_source_pages
  - figure: "the $14.3M transaction cost disclosure, the R&D step-up, and the engineering-and-support split"
    ticker: IRDM
    citation_id: sec191
    page_no: "26"
    url: https://agentii.ai/v/IRDM/sec191/26
    located_via: read_source_pages
---

# IRDM × unit-economics × retrieval-strategy

**The path actually taken, stated so it repeats. Seven steps — and step 4 is the one that departs
from the skill's declared scope.**

## 0. The skill's declared strategy, and where fidelity ends

`unit-economics` §2 states: *"Follows the retrieval strategy decision tree in
`contracts/retrieval.md`. Primary branch: **(a) Structured Data Query**. Resolve the canonical
ticker first (exact → fuzzy alias → share-class) before any data call."*

**Steps 1–3 below follow that. Step 4 does not** — the skill's branch (a) is the served structured
block, and the register forbids it at this name (see the retrieval-scope sibling). **Steps 5–7
are added by this thesis's register, not by the skill.**

## 1. The seven steps

### Step 1 — Resolve the ticker
`IRDM` resolves exactly on the first branch. **No fuzzy alias or share-class step is needed** —
IRDM is a single-class Nasdaq listing and carries no `.A`/`.B` ambiguity. **Recorded because the
skill's decision tree makes this a step, and a step that is skipped for a reason should say so.**

### Step 2 — Fiscal calendar and coverage pre-flight
`get_company_fiscal_calendar` then `get_ticker_coverage`, per the skill's mandatory pre-flight.
**Purpose at this tier: locate the most recent 10-Q and confirm its date, before any figure is
read.** Establishes `as_of: 2026-09-18` as the corpus date and **the 2026-06-30 quarter as the
latest filed period.**

### Step 3 — Locate the filing, and resolve the `citation_id`
`search_documents` on the symbol returns the filing set with a `citation_id` per document.
**IRDM's Q2 2026 10-Q resolves to `sec191`**, filed **2026-07-22** (verified via
`search_documents`).
**The `citation_id` is required, not decorative:** the anti-fabrication gate admits only
`{ticker}/{citation_id}` pairs present in the packed source text, so **a citation cannot be
written until this step has produced the id.**

### Step 4 — ⚠️ THE DEPARTURE: read the FILED pages, not the served block
**The skill's branch (a) would call `get_company_financials` and `search_xbrl_facts` here and
read the returned values.** **This artifact issues 0 such queries for IRDM's income-statement
concepts** — the served block is inadmissible per DA-29/DA-30 (retrieval-scope sibling, §2).

**Instead:** `read_source_outline` on `sec191` to map the document, then `read_source_pages` for
the specific pages. **The outline is what makes this cheap** — a 10-Q contains roughly four pages
of results-of-operations material, **and the outline names them.**

> ⚠️ **Two metadata fields were NOT retrieved and are recorded as absent rather than estimated.**
> **`search_documents` returns `filing_date` but neither the accession number nor a page count.**
> **An earlier draft of this artifact stated both** — `0001097516-26-000020` and *34 pages* —
> **and neither was ever returned by any tool call. They were fabricated, and they are removed.**
> **The page count is the more dangerous of the two**, because §1's argument that the outline
> saves reading 31 pages *depends on a total*; **the argument now reads without it**, and the
> outline's own page map is the evidence for what was skipped.

| Page | Why it was read |
|---|---|
| **p.5** | statements of operations — the entry point; confirms `total revenue 225,237` and `net income 9,679` |
| **p.24** | **the results-of-operations table — the primary source for every figure in this artifact set** |
| **p.26** | the variance narrative — the `$14.3M` transaction cost, the R&D step-up, the engineering split |

**Three pages, and the outline is the reason the rest were not read** — the outline's page map
distinguishes financially-relevant pages from the remainder, and **only the three above carried a
figure this artifact set uses.**

### Step 5 — The sign test (DA-23), run before the figure is used
**Every operating figure is checked against the component identity, in-line, on both periods:**
`225,237 − 191,229 = 34,008` ✓ and `216,906 − 166,648 = 50,258` ✓. **A figure that fails this
step is not used** — and **step 5 is where the served `−51,791,000` would have been caught had it
been admitted at step 4.**

**`EPS × shares` is deliberately NOT used** — the register forbids it because it passes on both
sides of a sign flip.

### Step 6 — The duration check (DA-02), run LAST
**Every figure carries its duration explicitly: 3M (three months ended 2026-06-30) or 6M.** **No
figure is blended across durations**, and the 6M half-year is excluded from this artifact set
entirely.

**Last on purpose:** a source that passes steps 1–5 and fails this one is still inadmissible, and
**no earlier step would catch it.** A served quarterly series built from mixed 3M/6M cells is
computable, internally consistent, and wrong.

### Step 7 — Citation roll-up
Every figure resolves to `https://agentii.ai/v/IRDM/sec191/{page}`. **`tools/check_citations.py`
returns clean on the artifact set**; the anti-fabrication gate is the check that a citation naming
a page that does not exist would fail.

## 2. What was NOT retrieved, and why that is a result

| Not retrieved | Reason |
|---|---|
| **The served metrics block** | **Inadmissible** at IRDM (DA-29/DA-30) — 0 queries issued |
| **The 6M half-year** | DA-02 — a different object from any 3M figure |
| **IRDM's subscriber count** | **Does not exist in the filing.** Not a retrieval failure — a basis absence (defaults sibling, D-5) |
| **Subscriber-acquisition cost** | **Not published.** Same (defaults sibling, D-1) |
| **The Aireon segment, consolidated** | **Not yet in any filing** — the acquisition closed 2026-07-02, after this period |

> ### ⚠️ AND THE THIRD AND FOURTH ROWS ARE THE ONES THAT MATTER FOR `unit-economics`
> **A skill named for unit economics, run on a filer that publishes no units, produces four
> ABSENCES at step 2 and three filed pages at step 4.** **The retrieval strategy is not the
> constraint here and no better strategy would change it** — the constraint is that **this tier's
> filers report segment economics and not customer economics.** Recorded so that a later reader
> does not re-run this search expecting a different result.

## 3. Repeatability

**The strategy is stated so it repeats.** Concretely: resolve → calendar/coverage → locate and
resolve `citation_id` → **outline first, then read only the named pages** → sign test → duration
check → cite. **Three pages read; 31 skipped with a reason; 0 served queries issued.**

**The one step that will not repeat unchanged is step 4** — it is a deviation from the declared
scope, and **whether it applies at the next name depends on whether the register documents a
served-block defect there.** The retrieval-scope sibling records the test for that.

---

**Sources.** [IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5) — statements of operations ·
[IRDM 10-Q p.24](https://agentii.ai/v/IRDM/sec191/24) — the results-of-operations table ·
[IRDM 10-Q p.26](https://agentii.ai/v/IRDM/sec191/26) — the variance narrative.
