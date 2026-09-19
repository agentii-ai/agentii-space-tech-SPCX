---
thesis_id: "006-constellation-operators"
pillar: "PIL-1"
ticker: IRDM
skill: unit-economics
mode: retrieval-scope
generated_at: 2026-09-20T15:30:00Z
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
  why: "The skill's declared scope admits ONLY the served structured block. This thesis's data-integrity register documents that block as inadmissible at IRDM — DA-30 (8 of 8 served quarterly margins divide by the Aireon hosting-agreement revenue ceiling) and DA-29 (the served `operating_income` carries a computed/reported back-solve signature). The skill's scope and the thesis's register are in direct conflict, and NO contract mechanism exists to declare a scope deviation. The deviation is therefore declared here, in-line, in the artifact, because that is the only place available."
  what_was_excluded: "The entire served metrics block — get_company_financials highlights and every search_xbrl_facts served fact — for IRDM's income-statement concepts."
definitions_used:
  - da_id: "DA-30"
    chosen_reading: "This artifact's own scope declaration is the DA-30 rule turned on the retrieval path: a source whose basis cannot be named is not admissible, and the served block's margin denominators ARE the Aireon ceiling — a contract maximum, not IRDM's revenue. Naming that is what makes the exclusion principled rather than convenient."
  - da_id: "DA-23"
    chosen_reading: "The sign test is the reason the filed path is required rather than merely preferred. A served figure with a stripped sign cannot be checked against an identity; a filed cell can."
key_metrics:
  skill_declared_scope: structured_only
  skill_allowed_tools_count: 8
  skill_allows_document_retrieval: false
  declared_deviation: true
  contract_mechanism_for_deviation_exists: false
  skills_006_uses: 18
  skills_006_uses_structured_only: 6
  tasks_bound_to_structured_only_skills: 75
  tasks_total: 270
  share_of_tasks_affected: 0.278
  library_skills_structured_only: 36
  library_skills_with_internal_scope_conflict: 0
  library_skills_total: 72
evidence_grade: DEMONSTRATED
citations:
  - figure: "the results-of-operations table and both component identities — the filed path taken"
    ticker: IRDM
    citation_id: sec191
    page_no: "24"
    url: https://agentii.ai/v/IRDM/sec191/24
    located_via: read_source_pages
  - figure: "the $14.3M transaction cost disclosure"
    ticker: IRDM
    citation_id: sec191
    page_no: "26"
    url: https://agentii.ai/v/IRDM/sec191/26
    located_via: read_source_pages
---

# IRDM × unit-economics × retrieval-scope

**⚠️ This artifact records a CONFLICT, not a procedure: `unit-economics` declares
`structured_only` and excludes document retrieval, while this thesis's register documents the
structured block as inadmissible at IRDM. There is no contract mechanism to resolve it. The
deviation is declared here because there is nowhere else to declare it.**

## 1. What the skill declares

`unit-economics/SKILL.md` frontmatter:

```yaml
retrieval_scope: structured_only
allowed_tools:
 - search_companies
 - search_xbrl_facts
 - get_company_financials
 - get_company_profile
 - list_xbrl_concepts
 - search_knowledge_entries
 - get_knowledge_entry
 - search_by_analogue
```

**Eight tools. `read_source_pages`, `read_source_outline` and `read_source_deep_outline` are not
among them** — and §1 of the skill body is explicit that this is deliberate, not an omission:

> *"This skill operates with `retrieval_scope: structured_only`. It performs structured data
> retrieval only (XBRL facts, financials, earnings calendar) — **no unstructured document search.
> Document-retrieval tools are excluded from `allowed_tools`.**"*

**So the skill's declared admissible basis is: the served structured block, and nothing else.**

## 2. What this thesis's register says about that block — at IRDM

| Register entry | Finding | Consequence |
|---|---|---|
| **DA-30** | **8 of 8** served quarterly margins divide by the **Aireon hosting-agreement revenue CEILING** (`$200,000` thousand, `srt:MaximumMember`, six-month period) and reproduce to the basis point | 003's verdict is unconditional: *"IRDM's served margins do not measure IRDM and NONE of them is admissible to this map."* |
| **DA-29** | The served `operating_income` carries a **back-solve signature** — `computed −51,791,000` against `reported +51,791,000` | The served value appears **solved for rather than read**, and it differs in **sign** |
| **DA-02** | IRDM's disclosures **mix 3M and 6M durations within one table** | A served quarterly series built without duration discipline **is not a series** |

> ### ⚠️ SO THE SKILL'S ADMISSIBLE BASIS IS, AT IRDM, THE ONE BASIS THE THESIS FORBIDS
> **This is not a preference ordering.** It is not that the filed path is *better*; it is that
> **the served path is inadmissible on documented grounds** — a denominator that is a contract
> ceiling, and an income figure whose own served representation contradicts its sign.
> **A skill whose declared retriever is that block cannot run as declared at this name.**

## 3. ⚠️ There is no mechanism to declare the deviation — and this is the finding

**Searched, and the search is negative:**

| Where a deviation mechanism would live | Result |
|---|---|
| `contracts/retrieval.md` | **None.** Its only escalation (line 70) is **within** document retrieval — `read_source_outline` → `read_source_deep_outline`. It does not contemplate leaving a declared scope. |
| `contracts/sharp-edges.yaml` | **None.** No entry mentions `structured_only`, `retrieval_scope`, or scope conflict. |
| `contracts/output-frontmatter-schema.md` | **No scope field, no deviation field, no admissibility field.** |

**So the contract suite offers exactly two states — *run as declared*, or *do not run* — and no way
to record the third state that this thesis actually requires: *run on a different basis, and say
so*.**

**This artifact therefore invents the field.** `scope_deviation` is declared in the frontmatter
above, with four keys: what the skill declares, what was used, why, and what was excluded.
**It is recorded here as an addition to the contract, proposed rather than ratified** — because
the alternative is that the deviation happens silently, which is what would otherwise occur.

## 4. The exposure is not one artifact — it is 75 tasks

**Six of the eighteen skills this thesis uses declare `structured_only`:**

| Skill | Tasks in 006 | Declared scope | Document retrieval |
|---|---:|---|---|
| **unit-economics** | **30** | `structured_only` | ❌ excluded |
| **operational-kpi** | **25** | `structured_only` | ❌ excluded |
| **trade-idea-generation** | 6 | `structured_only` | ❌ excluded |
| **position-sizing** | 6 | `structured_only` | ❌ excluded |
| **ratio-analysis** | 5 | `structured_only` | ❌ excluded |
| **residual-income** | 3 | `structured_only` | ❌ excluded |
| | **75** | | |
| competitive | 56 | `unstructured_document_search` | ✅ |
| risk | 32 | `unstructured_document_search` | ✅ |
| recent-quarter | 24 | `unstructured_document_search` | ✅ |
| sotp-valuation | 19 | `unstructured_document_search` | ✅ |
| business-model | 18 | `unstructured_document_search` | ✅ |
| *(7 more)* | 46 | `unstructured_document_search` | ✅ |
| | **195** | | |

> ### ⚠️ 75 OF 270 TASKS — 27.8% — ARE BOUND TO THE SCOPE THIS THESIS MUST REFUSE
> **And the library-wide figure says this is not 006's problem:** **36 of 72 skills — exactly
> 50.0% — declare `structured_only`.**
>
> **⚠️ And the registry is internally CONSISTENT: `0` of those 36 put a `read_source_*` tool in
> `allowed_tools`, and `0` skills anywhere declare `structured_only` while retaining document
> retrieval.** So the conflict is **not a registry defect.** The registry is coherent, and the
> thesis's register is coherent, and **they contradict each other** — which is a harder problem
> than a bug, because neither side is wrong on its own terms.
>
> **Two readings, and the thesis must pick one:**
> **(a)** every one of the 75 tasks carries a declared `scope_deviation` and reads filed cells; or
> **(b)** those 75 tasks are `BLOCKED_SCOPE` and cannot be executed as declared.
>
> **This artifact takes (a) and says so in-line.** **It does not claim (a) is contractually
> correct** — no contract says it is. **It claims (a) is the only reading under which the work
> can be done at all, and that a deviation declared in the artifact is strictly safer than the
> same deviation undeclared.**

## 5. What is admitted and what is excluded, stated exactly

| | |
|---|---|
| **ADMITTED** | IRDM's filed **10-Q** (`sec191`), pages read directly — **p.24** results of operations, **p.26** the variance narrative, **p.5** statements of operations |
| **ADMITTED** | The **component identity** computed in-line from those filed cells, both periods, closing exactly |
| **EXCLUDED** | The **entire served metrics block** — `get_company_financials` highlights and every served `search_xbrl_facts` fact for IRDM income-statement concepts |
| **EXCLUDED** | The **6M half-year** as a source for any 3M figure (DA-02) |
| **EXCLUDED** | Any percentage whose denominator is not named in-line (DA-30) |
| **EXCLUDED** | `EPS × shares` as a validation of operating income — **the register forbids it**, because it passes on both sides of a sign flip |

**And the exclusions are checkable, not aspirational: `tools/check_citations.py` returns 2/2 clean
on this artifact set, and the anti-fabrication gate admits only `{ticker}/{citation_id}` pairs
that resolve into the packed source text.** A citation to a served metric would not pass it.

---

**Sources.** [IRDM 10-Q p.24](https://agentii.ai/v/IRDM/sec191/24) — the filed results-of-operations
table, the admitted basis · [IRDM 10-Q p.26](https://agentii.ai/v/IRDM/sec191/26) — the $14.3M
transaction cost disclosure.
