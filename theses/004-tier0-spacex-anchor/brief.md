---
thesis_id: "004-tier0-spacex-anchor"
constitution_pin: "1.5.0"
assumption_pin: "2"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
---

# Stage-0 context brief — 004

**Purpose.** What the corpus and the workshops already know that bears on this thesis, recorded
**before** the phases run so the retrieval is reproducible and its limits are explicit.

---

## 1. Retrieval result — the honest headline

> ### ⚠️ Sector-keyed retrieval returns ZERO, and this is by construction
>
> | Query | Result |
> |---|---|
> | `search_investment_cases("space satellite launch rocket")` | **0 rows** |
> | `search_investment_strategies(sectors="aerospace_defense")` | **0 rows** |
> | `list_domains()` → `applicable_sectors` | `["med","tech","fin"]` — **no industrial or aerospace domain exists in the registry at all** |
>
> **`PROGRAM.md` §4 records this and it holds.** A query shaped *"give me space strategies"* will
> always return nothing, **and zero is not evidence of absence — it is evidence the index is keyed
> by sector and this sector is not a key.**

> ### ⚠️ `search_by_analogue(company_situation=…)` is ALSO a dead end
>
> `company_situation=category_creation` returned **0 cases and 0 strategies**, and the
> `analogue_tags` on nearly every row are **empty arrays**. **Retrieval must use full-text
> `search`, `practitioner`, `investment_style`, or `domain`.**

**Correction to §4's understatement.** §4 listed analogues at roughly one per row. **The corpus is
far richer by situation than that implies** — the ARK and a16z clusters alone supply **six
strategies and twenty-plus cases**, several with fully-populated `body` blocks carrying selection
criteria, position sizing, exit rules and risk limits. **Retrieve by structural situation, and
expect to find a lot.**

---

## 2. The strategies that bear on this thesis

Round 1 selected three frameworks. **Round 2 moved ownership of all three to 011's P1** — 004 is
the valuation layer and *reads* them. Each is recorded with a `method_selection:` verdict.

| # | Strategy / framework | Corpus ID | `method_selection:` verdict |
|---|---|---|---|
| **F1** | **ARK Wright's Law & S-Curve Innovation Valuation** | `ark_invest__wrights_law_valuation_framework` (+ `ark_invest__innovation_disruption_investing`) | ⚠️ **PARTIAL — the METHOD is admitted, the SCREENS are not.** See the feasibility box below. **Consumed from 011**, which owns the criterion |
| **F2** | **a16z Platform-Shift & Network-Effect Moats** | `a16z__platform_shift_network_effects` (+ `a16z__core_venture_methodology`) | ✅ **ADMITTED as a qualitative lens.** Yields the ecosystem-keystone map. **Owned by 011** (`PROGRAM.md` line 427) — 004 uses it only to explain why P2's margin leads |
| **F3** | **Platform Technology Monetisation via Licensing** | `med_bio-red-dividend__platform-technology-monetization-via-licensing` | ⚠️ **ADMITTED with a migration grade of `MODELED`.** It is a **medicine-domain** strategy; the transfer to launch-vs-payload is **structural, not sector**. State what would make it inapplicable |

> ### ⚠️ FEASIBILITY CHECK ON F1's SCREENS — **NOT evaluable on this workspace's data**
>
> **Wright's Law requires a learning rate fitted to `cost per unit` vs `CUMULATIVE PRODUCTION`.
> Neither axis exists here, and the one that does is contaminated.**
>
> | Input the screen needs | What the workspace holds | Verdict |
> |---|---|---|
> | A `$/kg` **time series** | 2026 (×50) and 2025 (×11) and nothing earlier — **a point estimate across four DA-01 bases, not a series** | **ABSENT** |
> | A **cumulative-production series** | The only cumulative figure in reach is RKLB's *"87 successful missions … **including suborbital launches**"* — **DA-08 already flagged as a mixed orbital+suborbital basis** | **PRESENT BUT BASIS-CONTAMINATED** |
>
> **A learning-rate fit needs ≥5 doublings of cumulative production against cost — a 32× volume
> range. The workspace holds a 2025→2026 window.** So *"learning rate sustained for ≥5 cumulative
> production doublings"* **cannot be computed.**
>
> **Disposition: `UNRESOLVABLE-FROM-PLATFORM`, with a named resolver** — an external source for
> historical launch prices and cumulative counts. **This is 002's F2 finding repeating**, and it
> takes the same treatment.
>
> **What SURVIVES, and it is the more useful half:** the **valuation METHOD** —
> probability-weighted bear/base/bull replacing point-estimate DCF, **terminal value capped at
> 50–70% of total EV**, and a stated **15–25% required return (target IRR, not WACC)**. **This is
> the piece 004 most needs**, because §1 establishes that both a consolidated DCF and comps are
> *inadmissible* — F1 supplies a third path.
>
> **What DOES NOT survive:** the numeric triggers. **A numeric trigger that cannot be computed is
> not a risk control; recording it as one would be the DA-29 failure inside this thesis's own
> method.**

---

## 3. The cases

### `<ref:ic_ark_tesla_valuation_2018_2023>` — the closest analogue, and a strong one

A traditional DCF valued Tesla at **$150** while ARK's probability-weighted framework said
**~$800**; Tesla reached a **$745.44** pre-split equivalent by end-2023. **The case's own lesson,
verbatim:** *"point-estimate DCF structurally undervalues disruptive innovation when growth,
margins, and TAM follow non-linear S-curves."*

**Why it bears on 004.** SPCX is the programme's clearest case of a company whose segments follow
different curves: a 65.8%-gross-margin launch business losing money on Starship R&D, a
38.6%-operating-margin broadband operator at 54.9% of revenue, and a 247%-growth compute business
that is the largest contributor to consolidated growth. **A single blended multiple is the
point-estimate error in SPCX's clothing.**

### `<ref:ic_jeff_bezos_as_amazon_founder_ceo_for_27_years>` — and the founder-CEO set

With `ic_mark_zuckerberg_as_meta_founder_ceo_through_existential_cris`,
`ic_brian_chesky_as_airbnb_founder_ceo_through_pandemic_near_dea`,
`ic_reed_hastings_as_netflix_founder_ceo_through_dvd_to_streamin`, plus `ic_netscape_ipo_1995` and
`ic_netscape_vs_microsoft_browser_war_1995_1999`.

> **⚠️ `search_investment_cases("Musk")` returns ZERO.** These are **structural analogues with a
> different operator.** **Disposition: use them as the METHOD, and record Musk-specific claims as
> `CLAIMED` — no artifact in this thesis may grade a Musk-behaviour claim `DEMONSTRATED` from the
> corpus.** The People leg is **self-built**, and that limit is the finding.

---

## 4. The workshop's own material

**001** built the technology baseline — throughput, cost, the six verdicts. **Its primary artifact
is published and six of six verdicts are recorded.** 004 consumes it and does not re-derive it.

**002** validated 001's figures and produced the programme's sharpest result: **a grade does not
carry a basis.** SPCX `operating_margin` reproduces exactly on two bases **46.47pp apart**. **This
is why P2 and P4's falsifiers name their basis in-line.**

**003** is **COMPLETE** — the curve matrix, the value-pool map, and nine SPCX artifacts that 004
**consumes rather than re-runs.** Its E-01/E-02/E-03 already carry all three SPCX segments with
exact component identities.

---

## 5. The two structural facts this brief was written to carry

1. **The retrieval problem is a KEYING problem, not a coverage problem.** The corpus has no space
   sector tag; it has strategies and cases that transfer **by situation**. **A zero result is a
   query-shape finding.**
2. **The one framework whose screens are quantitative has uncomputable screens.** Its *method*
   survives and is what 004 uses; its *thresholds* are recorded `UNRESOLVABLE-FROM-PLATFORM` with
   a named resolver — **not silently deleted, and not asserted.**
