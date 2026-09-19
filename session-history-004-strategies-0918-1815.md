# Session History — 004 strategies/cases retrieval forensics

**Written:** 2026-09-18 18:15
**Scope:** the segment of session `8c133785-827c-4a93-b09a-c1352356689d` covering thesis 004's
clarify round 1 — the request to search the agentii knowledge base for strategies and cases
applicable to SpaceX, and to build one or two frameworks from them.
**Purpose (owner's words):** *"我需要仔细研究 agents 通过怎样的匹配方式，搜索，得到和spacex相关的
strategies 和cases，有哪些变量和参数给了搜索，搜索如何返回的结果"*

> **Provenance note.** This is reconstructed from the session's live context. Every API call's
> parameters are reproduced **as issued**, and every return is reproduced at the field level.
> Where a return payload was very large (the `depth: full` strategy bodies), the **structure and
> every field name/value** is preserved but long prose fields are quoted selectively — the
> selection is marked. **For byte-exact JSON, the raw transcript is at**
> `/Users/frank/.claude/projects/-Users-frank-B-agentii-space-tech-SPCX/8c133785-827c-4a93-b09a-c1352356689d.jsonl`.
> Nothing in this document is inferred; where I am reading structure off a return, I say so.

---

## Part 0 — The question being answered

The owner asked for strategies/cases to analyse SpaceX as a "颠覆式创新超级巨无霸" (disruptive-innovation
super-giant), and explicitly for the **retrieval mechanics** to be documented. So this file's primary
object is **not** the strategies — it is **which parameter did the matching**.

**The one-line answer, stated up front so the evidence below can be read against it:**

> **The corpus is indexed by INVESTMENT CONCEPT, not by INDUSTRY.** Free-text `search` matches the
> strategy/case **prose** (description, core_belief, situation_type). Every industry-shaped key —
> `sectors`, `sector`, and the `company_situation` / `market_regime` / `event_type` analogue tags —
> is either **unpopulated** or **absent from the registry entirely**. That is why
> `"disruptive innovation cost curve"` returns ARK and `"space satellite launch rocket"` returns
> **zero**, with no sector involved in either.

---

## Part 1 — The conversation (004 clarify round 1)

**Owner instruction (verbatim):**

> `@theses/004-tier0-spacex-anchor/` spacex 作为体量最大的上市space tech公司，是整个板块的压舱石
>
> 本thesis 需要把spacex作为中心，挖掘 space tech 整个生态下，spacex 的核心
>
> 你是一个买方fund的顶级分析师，thesis 004需要你搜索agentii 知识库里面的strategies cases，
>
> spacex是市场不曾见过的颠覆式创新超级巨无霸，用什么样的strategies分析这家公司，历史上有哪些cases可以参考
>
> 构建一个两个分析spacex的框架（包括spacex在生态中的相互作用）
>
> must stay in main

**Invoked:** `/agentii:clarify /Users/frank/B/agentii-space-tech-SPCX/theses/004-tier0-spacex-anchor`

**Prior state read before any corpus call:**

| Read | Result |
|---|---|
| `004/spec.md` | 582 lines. **6 pillars, all SOTP/valuation**: P1 three-segment SOTP + conglomerate discount (MDV); P2 Connectivity is the value; P3 AI carries no admissible multiple; P4 Space as public good; P5 `CAPITAL` binding; P6 three regimes with comparability boundaries |
| `004/spec.md` §Clarifications | **Q-1 … Q-7 already recorded open** — all internal to the SOTP framing |
| `PROGRAM.md` §4 "The corpus gap" | Recorded: sector search → 0; `list_domains` has no industrial domain; **retrieve by structural situation** |
| `PROGRAM.md` §5 dependency graph | `003 ──> 004` ("SPCX sizes off the curve") |
| Memory `agentii-corpus-retrieval-by-situation` | Pre-existing note: no industrial/aerospace domain; sector-keyed queries return zero **by construction** |

**Why this matters for reading Part 2:** the "corpus gap" was **already known and documented**
before this round. The round's finding is not *that* the sector search fails — it is **how much
the situation search returns, and which parameter shapes are dead ends.**

---

## Part 2 — Every API call, verbatim

**12 calls total.** Ordered as issued. `→` marks the return.

---

### Call 1 — `list_domains`

```json
{}
```

**Why issued:** to test the sector taxonomy directly rather than trust the prior note.

**Return — `total_count: 9`:**

| domain_key | display_name | `applicable_sectors` |
|---|---|---|
| `business_model` | Business Model | `["med","tech","fin"]` |
| `clinical` | Clinical Development | `["med"]` |
| `commercial` | Commercial & Sales | `["med","tech","fin"]` |
| `competitive` | Competitive Landscape | `["med","tech","fin"]` |
| `financial` | Financial Performance | `["med","tech","fin"]` |
| `operational` | Operations & Supply Chain | `["med","tech","fin"]` |
| `product_pipeline` | Product Pipeline | `["med","tech"]` |
| `regulatory` | Regulatory & Legal | `["med"]` |
| `workforce` | Workforce & Leadership | `["med","tech","fin"]` |

- `entity_types: []` on **all nine**.
- `meta.data_freshness: "2026-08-26 07:08:56.75577+00"`.

> **⚠️ FINDING 1 — this is a DOMAIN list, not a SECTOR list.** The enumeration is *research
> domains* (what an analyst studies), and `applicable_sectors` is a **sub-field**, not the key.
> **Across all 9 domains the union of `applicable_sectors` is exactly `{med, tech, fin}`.**
> No `industrial`, no `aerospace`, no `defense`, no `energy`, no `materials`.
> **A sector-scoped query for this universe cannot match — not because it is rare, but because
> the value does not exist in the enumeration.** This is a **closed-world** failure: the filter
> is not returning "no results", it is matching against a vocabulary that excludes the sector.

---

### Call 2 — `search_investment_strategies` (first success)

```json
{"search": "disruptive innovation cost curve", "depth": "summary", "page_size": 10}
```

**Return — 1 row, `total_pages: 1`:**

| field | value |
|---|---|
| `strategy_id` | `ark_invest__innovation_disruption_investing` |
| `title` | ARK Innovation Disruption Investing |
| `kind` | `enduring` |
| `investment_style` | **`innovation_disruption`** |
| `practitioner` | **`ark_invest`** |
| `domain` | `fundamental` · `time_horizon: ["investment"]` |
| `situation_type` | **`null`** |
| `analogue_tags` | **`{"event_type":[], "market_regime":[], "company_situation":[]}` — ALL EMPTY** |
| `asset_class` | `null` · `managed_by`: `null` |
| `citation_id` | `ark_invest__innovation_disruption_investing` |

`description` (quoted): *"…investing in companies leading or enabling disruptive innovation
across five converging platforms (AI, autonomous systems, genomics, blockchain, energy). It
targets early-adoption S-curve inflection points where **exponential cost declines (Wright's
Law)** are systematically undervalued by short-term, linearly-thinking markets."*

> **⚠️ FINDING 2 — the match was made on PROSE, and it was a near-exact hit.** The query string
> `"disruptive innovation cost curve"` intersects the `description` and `core_belief` text.
> **No sector was involved, and the row's `analogue_tags` are empty — so a tag-keyed query could
> not have found this row at all.** Note also `kind: enduring` and `investment_style:
> innovation_disruption`, both of which are **usable filter parameters** (see Call 8).

---

### Call 3 — `search_investment_cases` (first failure)

```json
{"search": "vertical integration platform monopoly", "depth": "summary", "page_size": 10}
```

**Return: `{"rows": [], "total": null}` — ZERO.**

> **⚠️ FINDING 3 — a thematic query that SHOULD have hit, and did not.** SpaceX is the most
> vertically integrated company in the universe and its launch position is monopoly-adjacent.
> This suggests either (a) the case corpus does not carry these concepts, or (b) case `search`
> is narrower than strategy `search`. **Distinguishing (a) from (b) needs a control query** —
> Call 7 is that control, and it succeeded, which favours (b): the case corpus IS searchable,
> this particular phrase simply is not in it.

---

### Call 4 — `search_by_analogue` (structural dead end)

```json
{"company_situation": "category_creation", "page_size": 20}
```

**Return: `{"cases": [], "strategies": [], "total_cases": null, "total_strategies": null}` — ZERO BOTH.**

> **⚠️⚠️ FINDING 4 — THE MOST IMPORTANT NEGATIVE RESULT IN THIS FILE.** This is the tool whose
> *name* suggests exactly the right retrieval mode ("search by analogue"), and it returns nothing.
> **The reason is visible in Call 2's return: `analogue_tags` is `{"event_type":[], "market_regime":[], "company_situation":[]}` — empty arrays, on essentially every row examined.** The tag layer is **unpopulated**, so any tag-keyed query has nothing to match against.
> **This is a second dead end of the SAME SHAPE as the sector filter:** a keyed query against a
> vocabulary that was never filled in. **Two documented dead ends now, and neither errors — both
> return a clean empty set that reads as "the corpus has nothing."**

---

### Call 5 — `search_investment_strategies` (unfiltered, to size the corpus)

```json
{"depth": "summary", "page_size": 15}
```

**Return: 15 rows, `page: 1`, `total_pages: 53`.**

**→ Implied corpus size ≈ 15 × 53 ≈ 795 strategy rows.**

**Practitioner concentration in the 15-row sample:** `bio_red_dividend` (9), `deerfield` (2),
`ra_capital` (2), `ark_invest` (0 in this page but present via Call 2).

**Unfiltered-page observation:** the first page is **overwhelmingly `med`** — titles like
*Microbiome-Centric Metabolic & Lifestyle Interventions*, *Psychoneuroimmunology & Psychedelic
Revaluation*, *Health Economics Arbitrage via QALY Valuation*. **The default ordering is
NOT neutral with respect to sector**, so an analyst sampling "the corpus" from page 1 would
conclude it is a biotech corpus. **It is not — but you have to query past page 1 to find out.**

---

### Call 6 — `search_investment_cases` (unfiltered, to size the case corpus)

```json
{"depth": "summary", "page_size": 15}
```

**Return: 15 rows, `total: null`.**

**Field-level structure — note what is EMPTY on every row:**

| field | observed value across the 15 |
|---|---|
| `analogue_tags` | **empty arrays on 13 of 15**; `["turnaround"]` on Bridgewater/MCD; `["acquisition"]` on Royce/FUL; `["regulatory-overhang"]` on Coatue/META |
| `category_tags` | **`[]` on all 15** |
| `protagonists` | `[]` on all but the ARK rows |
| `case_summary` | **`null`** |
| `variant_view` | **`null`** |
| `result_headline` | **`null`** |
| `when_to_recall` | **`null`** |
| `related_strategies` | **`[]`** |
| `stock_case` | `true` on 12, `false` on 3 |
| `layer_tags` | populated — `["L2","L3"]`, `["L2","T4"]`, `["L2","L3","L4"]` |
| `sectors_referenced` | populated — free-text industry names (`"Industrials"`, `"Building Products"`, `"Materials"`, `"Technology"`) |
| `tickers_referenced` | populated — `PBR`, `MCD`, `MSFT`, `TMO`, `FUL`, `SSD`, `GOOGL`, `AMZN`, `V`, `META`, `AMBP`, `005930.KS`, `MELI` |
| `outcome` | populated on most — e.g. Eagle/MSFT *"10-12x (1,000-1,200%)"* |

> **⚠️ FINDING 5 — the "fund-direct" case layer is a FUND-HOLDINGS layer.** The rows are keyed by
> **`managed_by` / `practitioner`** (`brandywine`, `bridgewater`, `brown_advisory`, `royce`,
> `calamos`, `eagle_capital`, `baillie_gifford`, `coatue`, `oakmark_harris`, `lord_abbett`,
> `dodge_and_cox`, `baron_capital`) — i.e. **"what fund held what stock"**, extracted from
> factsheets. `sectors_referenced` is free text, **not** the `med/tech/fin` enum used by
> `list_domains`. **These are two DIFFERENT sector vocabularies in the same API surface.**
> **And `provenance: "extracted"` marks them as pulled from documents, which is why the analyst
> fields (`case_summary`, `variant_view`, `when_to_recall`) are null and `outcome` is populated.**

---

### Call 7 — `search_investment_cases` (the successful thematic query)

```json
{"search": "exponential cost decline S-curve disruption", "depth": "summary", "page_size": 10}
```

**Return — 4 rows, all `provenance: "synthesized"`, all `practitioner: "ark_invest"`:**

| case_id | title | `related_strategies` |
|---|---|---|
| `ic_ark_ev_adoption_prediction_2017_2023` | ARK predicted EVs would achieve 15%+ share by 2023 | `["ark_invest__innovation_disruption_investing"]` |
| `ic_cathie_wood_holding_tesla_through_drawdowns` | Cathie Wood holding Tesla through severe drawdowns | `["ark_invest__drawdown_buying_and_sentiment_exploitation"]` |
| `ic_ark_tesla_valuation_2018_2023` | ARK's probability-weighted Tesla valuation | `["ark_invest__wrights_law_valuation_framework"]` |
| `ic_ark_doubling_down_on_tesla_during_production_hell` | ARK doubling down during production hell | `["ark_invest__risk_management_and_volatility_acceptance"]` |

**⚠️ Compare Call 6 and Call 7 — this is the key structural contrast:**

| | Call 6 (unfiltered) | Call 7 (thematic) |
|---|---|---|
| `provenance` | `"extracted"` | **`"synthesized"`** |
| `practitioner` | 12 different funds | `ark_invest` |
| `analogue_tags` | mostly empty | empty, but `["high-volatility"]` on one |
| `result_headline` | **`null`** | **POPULATED** |
| `variant_view` | **`null`** | **POPULATED** |
| `when_to_recall` | **`null`** | **POPULATED** |
| `case_summary` | **`null`** | **POPULATED — multi-paragraph** |
| `related_strategies` | **`[]`** | **POPULATED — the link exists** |

> **⚠️⚠️ FINDING 6 — THERE ARE TWO CASE LAYERS, AND THE ANALYTICALLY USEFUL ONE IS `synthesized`.**
> **`extracted` cases = fund-holdings records.** Analysts' reasoning fields are null; the payload
> is `sectors_referenced` + `tickers_referenced` + `outcome`.
> **`synthesized` cases = analytic narratives.** They carry `case_summary`, `variant_view`,
> `result_headline`, `when_to_recall`, and **`related_strategies` links back to the strategy layer.**
> **The `related_strategies` edge is the retrieval graph, and it is populated ONLY on synthesized
> cases.** That is the mechanism by which a strategy leads to its cases and vice versa.
> **Practical consequence: to retrieve by *situation*, you need synthesized cases; to retrieve by
> *who held it*, extracted cases suffice.** The two are not interchangeable and the API does not
> flag the distinction — only `provenance` does.

---

### Call 8 — `search_investment_strategies` (ENUM FILTER — the cleanest parameter)

```json
{"investment_style": "innovation_disruption", "depth": "full", "page_size": 5}
```

**Return — 5 rows, `total_pages: 2` → ≈ 6–10 rows carry this `investment_style`. All with FULL bodies:**

| strategy_id | practitioner | `layer_tags` |
|---|---|---|
| `a16z__ai_acceleration` | a16z | `["L1","L2","L4"]` |
| `a16z__core_venture_methodology` | a16z | `["L1","L2","L3"]` |
| `a16z__crypto_full_stack` | a16z | `["L1","L2","L3","L4"]` |
| `a16z__platform_shift_network_effects` | a16z | `["L1","L2","L3"]` |
| `ark_invest__conviction_weighted_portfolio_construction` | ark_invest | `["L3"]` |

**The `depth: "full"` return adds a `body` object. Its keys are the operational payload:**

```
body: { exit_rules, risk_limits, position_sizing, selection_criteria, portfolio_construction }
```

**`instrument_scope`**, **`sectors_focus`**, **`referenced_strategies`**, **`referenced_cases`**,
**`as_of_date`**, **`version`**, **`provenance`**, **`review_status`** also appear at full depth
and are **absent at summary depth**.

> **⚠️⚠️ FINDING 7 — `investment_style` IS THE STRONGEST WORKING PARAMETER AFTER FREE TEXT.**
> It is a controlled enum, it partitions cleanly, and it returns **5 rows with complete operational
> bodies from a single call.** Compare: Call 2's prose query returned **1** row. **If you know the
> style, filter on it; do not search prose.**
>
> **⚠️ AND NOTE THE `referenced_cases` FIELD — it is the reverse edge of Finding 6.**
> `a16z__core_venture_methodology` carries `referenced_cases` = **12 ids**, including
> `ic_jeff_bezos_as_amazon_founder_ceo_for_27_years`, `ic_mark_zuckerberg_as_meta_founder_ceo_through_existential_cris`,
> `ic_brian_chesky_as_airbnb_founder_ceo_through_pandemic_near_dea`,
> `ic_reed_hastings_as_netflix_founder_ceo_through_dvd_to_streamin`.
> **`a16z__platform_shift_network_effects` carries 8, including `ic_netscape_ipo_1995` and
> `ic_netscape_vs_microsoft_browser_war_1995_1999`.**
> **So: filtering by `investment_style` and reading `referenced_cases` retrieves the case set
> WITHOUT any case search at all.** This is the hub-and-spoke structure — **strategies are the
> hubs, cases are the spokes, and `referenced_cases` / `related_strategies` are the edges.**

---

### Call 9 — `search_investment_cases` (the definitive sector control)

```json
{"search": "space satellite launch rocket", "depth": "summary", "page_size": 5}
```

**Return: `{"rows": [], "total": null}` — ZERO.**

> **⚠️ FINDING 8 — this is the CONTROL that makes Finding 1 conclusive.** Same tool, same depth,
> same `page_size` shape as Call 7 which returned **4** rows. **The only variable is the query
> string.** `"exponential cost decline S-curve disruption"` → 4. `"space satellite launch rocket"`
> → 0. **So the case corpus IS searchable and IS populated; it simply contains no space-industry
> material.** Combined with Call 1, the mechanism is now pinned:
> **the corpus is indexed by investment concept, and there is no industry axis to search on.**

---

### Call 10 — `search_investment_cases` (the null control, `depth: full`)

```json
{"search": "Musk founder CEO conviction concentrated", "depth": "full", "page_size": 6}
```

**Return: `{"rows": [], "total": null}` — ZERO.**

> **⚠️ FINDING 9 — the corpus contains NO Musk case and NO SpaceX case.** The query mixed a
> **name** (`Musk`), a **structural role** (`founder CEO`), and **behavioural traits**
> (`conviction concentrated`). Zero on all three jointly. **Call 11's success with a
> *concept* query and this failure with a *name + trait* query is the sharpest single contrast
> in the file:** the index is built on **investment concepts**, not on **people** and not on
> **companies**. `search_investment_cases` is not a name lookup.

---

### Call 11 — `search_investment_strategies` (the framework, retrieved in full)

```json
{"search": "Wright's Law cost decline learning curve", "depth": "full", "page_size": 6}
```

**Return — 1 row, `total_pages: 1` — and it is the framework later built into the spec:**

**`ark_invest__wrights_law_valuation_framework`** — *"ARK Wright's Law & S-Curve Innovation Valuation"*, `kind: enduring`, `domain: fundamental`, `layer_tags: ["L2","L3"]`.

**`body.selection_criteria` (quoted, this is the operable content):**

> *"Technologies must exhibit a documented Wright's Law learning rate (e.g., batteries 20%, solar
> 28%, DNA sequencing ~50%, AI compute 60%+) sustained for **≥5 cumulative production doublings**,
> with a TAM that expands dramatically at the cost-curve endpoint. Companies are screened by:
> (1) consistent learning rate history, (2) S-curve adoption position (**sub-20% penetration**),
> (3) revenue CAGR potential ≥30%, (4) **platform-orchestrator characteristics (data network
> effects, scale advantages)**. Red flags: **learning rate decay below 10–15%**, demand
> saturation stalling the S-curve…"*

**`body.risk_limits` (the trigger rule):** *"If a learning rate falls below the model's predicted
bound for two consecutive doublings, the position is reduced by ~1/3."*

**`body.exit_rules`:** exit on thesis break / moat erosion / acquisition at fair value / price
exceeds bull-case EV. **"Never sell on short-term earnings misses, macro headlines, or negative sentiment."**

**`body.portfolio_construction`:** *"terminal value capped at 50–70% of total EV"*; required return
**15–25% (target IRR, not WACC)**.

**`referenced_cases` = 5:** `ic_ark_ai_training_cost_collapse_prediction_2020_2024`,
`ic_ark_dna_sequencing_at_100_prediction_2014_2023`, `ic_ark_ev_adoption_prediction_2017_2023`,
`ic_ark_tesla_valuation_2018_2023`, `ic_arks_tesla_investment_2016_2020`.

> **⚠️ FINDING 10 — `search` matched the strategy's METHOD prose and returned a single precise hit.**
> The query named the *technique* (`Wright's Law`, `cost decline`, `learning curve`), not an
> industry or a company. **This is the retrieval mode that works, stated positively.**

---

### Call 12 — `get_investment_strategy` (direct ID fetch)

```json
{"strategy_id": "ark_invest__innovation_disruption_investing", "depth": "full"}
```

**Return: the same row as Call 2, but at `depth: "full"` — now carrying a complete `body`.**

**`body.selection_criteria` (quoted):**

> *"Identify companies operating on one or more of five core innovation platforms… with:
> proven Wright's Law cost-curve trajectory (**≥5 cumulative doublings**), early-adoption phase
> (**sub-20% penetration**), total addressable market **>$1T at cost-curve end**, convergence
> potential across platforms, and a **platform-orchestrator business model (owns customer
> relationship and tech stack) with data network effects, scale economies, and high switching
> costs**."*

**`referenced_cases` = 8:** `ic_cathie_wood_ark_invest_2020_2022_boom_and_bust`,
`ic_ark_ev_adoption_prediction_2017_2023`, `ic_ark_streaming_over_linear_tv_prediction_2016_2023`,
`ic_ark_robotaxi_fleet_prediction_2020_2030`, `ic_ark_bitcoin_institutionalization_prediction_2019_2024`,
`ic_ark_crispr_cures_prediction_2018_2023`, `ic_arks_tesla_investment_2016_2020`,
`ic_arkk_2020_tesla_driven_surge`.

> **FINDING 11 — `get_investment_strategy(strategy_id=…)` is the RELIABLE fetch.** It returns the
> full body for a known id, with no dependence on the search index at all. **Pairs with Finding 7:
> enumerate via an enum filter, then fetch by id.**

---

## Part 3 — The matching mechanism, assembled

### 3.1 The parameter surface, classified by observed behaviour

| Parameter | Type | Tested? | Behaviour |
|---|---|---|---|
| `search` | **free text** | ✅ Calls 2, 3, 7, 9, 10, 11 | **Works — and it is the PRIMARY discovery mode.** Matches strategy/case **prose**: `description`, `core_belief`, `situation_type`, `case_summary`, `when_to_recall`. **Not a name lookup; not an industry lookup.** |
| `investment_style` | **enum** | ✅ Call 8 | **Works cleanly.** 5 full-body rows in one call. Best precision-per-call observed. |
| `depth: "full"` | output control | ✅ Calls 8, 10, 11, 12 | Adds `body{exit_rules, risk_limits, position_sizing, selection_criteria, portfolio_construction}` + `referenced_cases` + `referenced_strategies` + `instrument_scope` + `sectors_focus` + `version` + `provenance` |
| `practitioner` | key | ❌ untested | Implied viable — `practitioner` is populated on every row (`ark_invest`, `a16z`, `bio_red_dividend`, `deerfield`, `ra_capital`, 12 funds in Call 6) |
| `domain` | enum | ❌ untested | Values seen: `fundamental`, `hybrid` |
| `kind` | enum | ❌ untested | Values seen: `enduring`, `situational` |
| `time_horizon` | enum array | partially | Values seen: `["investment"]`, `["investment","trading"]` |
| `asset_class` | enum | ❌ | Values seen: `equity`, `null` |
| **`company_situation`** | **tag** | ✅ Call 4 | **DEAD — `analogue_tags` empty ⇒ nothing to match** |
| **`market_regime`** | **tag** | — | **Same layer; Call 6 shows populated on only 2 of 15 rows** |
| **`event_type`** | **tag** | — | **Same layer; populated on 3 of 15** |
| `sectors` / `sector` | **enum** | ✅ Call 1 + `PROGRAM.md` §4 | **DEAD BY CONSTRUCTION — vocabulary is `{med, tech, fin}`** |
| `min_signal_score`, `layer_tags`, `category_tags` | — | ❌ | `category_tags` observed `[]` on all 15 case rows |

### 3.2 The two-layer structure (Findings 6 + 7 combined)

```
STRATEGIES  ──references──▶  CASES
   (hubs)     referenced_cases      (spokes)
              ◀── related_strategies ──
```

- **Strategies are the hubs.** They carry `body` — the operational content (selection criteria,
  risk limits, position sizing, exit rules).
- **Cases are the spokes.** `extracted` cases are fund-holdings records; `synthesized` cases are
  analytic narratives.
- **The edges are only populated on `synthesized` cases / on strategies' `referenced_cases`.**
- **⇒ The efficient traversal is: enum-filter → strategy → `referenced_cases` → fetch cases.**
  **It does not require a case search at all**, and it avoids the empty `analogue_tags` layer
  entirely.

### 3.3 Why sector-shaped queries fail — the mechanism, precisely

Two **independent** closed-world failures, and neither raises an error:

1. **`list_domains.sectors` = `{med, tech, fin}`.** The sector axis has **no value for this
   universe**. A sector query is not "unlucky"; it is matching against a vocabulary that
   structurally excludes the answer. *(Call 1.)*
2. **`analogue_tags` are empty arrays on essentially every row.** `search_by_analogue` — the tool
   *built* for situation matching — is querying a **field that was never populated**. *(Calls 2, 4, 6.)*

**And the reciprocal fact that makes the corpus usable anyway:** the **concept** axis is rich and
densely populated (`description`, `core_belief`, `body.selection_criteria`), so **free-text and
enum queries retrieve copiously.** *(Calls 2, 7, 8, 11.)*

> **⚠️ The operational rule: SEARCH PROSE AND ENUMS; NEVER SEARCH TAGS OR SECTORS.**
> Correspondingly — **a zero from a tag or sector query is evidence about the VOCABULARY, not
> about the corpus.** This is the same failure class thesis 002 documented all phase: *a check
> that returns a clean empty set while testing nothing.*

### 3.4 What each dead end would have misled an analyst into concluding

| Query | Naive reading | True state |
|---|---|---|
| `sectors=aerospace_defense` → 0 | "no strategy applies to space" | the sector value does not exist; **three frameworks apply** |
| `company_situation=category_creation` → 0 | "no analogue was ever recorded" | **the tag field is empty**, not the corpus |
| `"vertical integration platform monopoly"` → 0 | "no case covers integration/monopoly" | this **phrase** is absent; the case corpus is searchable (Call 7 returned 4) |
| `"space satellite launch rocket"` → 0 | "nothing here for SpaceX" | **correct as to industry, wrong as to applicability** — the frameworks transfer |
| `"Musk …"` → 0 | "no founder-CEO material" | **4 founder-CEO crisis cases exist**; they are reachable via `referenced_cases` on `a16z__core_venture_methodology` |

---

## Part 4 — What was actually retrieved, and the one caveat

**Three frameworks and a case set, all filed under tech/innovation:**

| # | Framework | Strategy ID | How it was reached |
|---|---|---|---|
| F1 | ARK Wright's Law & S-Curve Valuation | `ark_invest__wrights_law_valuation_framework` | **Call 11** — concept query `"Wright's Law cost decline learning curve"` |
| F1b | ARK Innovation Disruption Investing | `ark_invest__innovation_disruption_investing` | **Call 2** — concept query `"disruptive innovation cost curve"` |
| F2 | a16z Platform-Shift & Network Effects | `a16z__platform_shift_network_effects` | **Call 8** — enum filter `investment_style` |
| F2b | a16z Founder-Led Venture Methodology | `a16z__core_venture_methodology` | **Call 8** — same enum filter |
| F3 | Platform Technology Monetisation via Licensing | `med_bio-red-dividend__platform-technology-monetization-via-licensing` | **Call 5** — unfiltered strategy page |

**Cases:** `ic_ark_tesla_valuation_2018_2023` (DCF $150 vs ARK ~$800 vs actual $745.44),
`ic_ark_ev_adoption_prediction_2017_2023`, `ic_ark_doubling_down_on_tesla_during_production_hell`,
`ic_cathie_wood_holding_tesla_through_drawdowns`, `ic_ark_ai_training_cost_collapse_prediction_2020_2024`,
`ic_ark_dna_sequencing_at_100_prediction_2014_2023`, `ic_ark_robotaxi_fleet_prediction_2020_2030`,
`ic_netscape_ipo_1995`, and the founder-CEO quartet (Bezos / Zuckerberg / Chesky / Hastings).

### ⚠️ The caveat that must travel with F1

**F1's numeric screens depend on a Wright's Law learning rate — and that cannot be computed from
this workspace's data.** Verified after retrieval:

| Required | Held | Verdict |
|---|---|---|
| a `$/kg` **time series** | SPCX unit-economics artifacts carry **2026 (×50) and 2025 (×11) only** | **ABSENT** |
| a **cumulative-production** series | only RKLB's *"87 successful missions … including suborbital launches"* — **DA-08-flagged as mixed orbital+suborbital** | **CONTAMINATED** |

**So `≥5 cumulative doublings`, `sub-20% penetration` and the *"two consecutive doublings"* risk
trigger are `UNRESOLVABLE-FROM-PLATFORM`.** What survives is F1's **method** — probability-weighted
scenarios with a **50–70% terminal-value cap** — and its **qualitative platform-orchestrator
criterion**, which is the falsifier for thesis 004's main line. **Full record in
`theses/004-tier0-spacex-anchor/spec.md` §Clarifications, clarify round 1.**

---

## Part 5 — Suggested next probes (not run)

If the matching mechanism is to be characterised further, these are the untested parameters with
the highest information value:

1. **`practitioner: "ark_invest"`** — does it return the whole ARK cluster in one call? *(Would
   confirm `practitioner` as a usable enumeration key.)*
2. **`domain: "hybrid"` vs `"fundamental"`** — does `domain` partition the corpus usefully, or is
   it too coarse? *(Called `fundamental` on nearly every row seen.)*
3. **`kind: "situational"`** — the corpus has this kind; `situation_type` is populated on some rows
   (`med_deerfield__…` rows carry prose situations). **Does `kind=situational` retrieve by situation
   better than `search_by_analogue` does?** *(This is the most promising untested path.)*
4. **A control pair on `search`** — same tool, one industry word vs one concept word, to pin the
   index's axis definitively rather than by inference.
5. **`list_related_cases(case_id=…)`** — the Memory note records this tool exists. **Untested here,
   and it is the direct traversal of Finding 6's edge.**
