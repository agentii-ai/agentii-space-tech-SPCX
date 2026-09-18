# Research Thesis: 011 — Idea Generation, Strategies & Cases

**Constitution Ref**: constitution.md v1.4.0 (`constitution_pin: 1.4.0`)
**Created**: 2026-09-18 · **Specified**: 2026-09-18 (upgraded from stub by the clarify round on 002)
**Status**: Active
**板块**: Decision layer · **Binding constraint**: *n/a — portfolio construction*
**Depends on**: `001-technology-baseline` (the register) — **and only 001 for P1–P5.**
See §1d for the **split dependency**: the main line and the strategy layer start now;
only position sizing waits for 004–010.
**Produces**: the program's **governing investment argument**, the strategy inventory
with honest actionability grading, and — once the segment theses land — a sized book.

---

## 0. Inherited baseline — what this thesis does NOT re-derive

011 inherits all of 001–010 by construction and re-derives none of it. But it is
**specified early, ahead of 004–010**, because the clarify round established that its
first five pillars do not depend on them. That is a deliberate change to this thesis's
sequencing, and §1d states its cost.

| Inherited result | Source | Grade |
|---|---|---|
| **The margin ladder**: operating margin monotone in distance from programme risk across 8 issuers — HEI 25.5%, KRMN 19.1%, WWD ~17%, LMT 12.4%, RTX 11.4%, LHX 11.1%, NOC 10.1%, GSAT 7.4% | `001/_cross/technology-baseline_synthesis.md` §4.1 | `DEMONSTRATED` |
| Refined rule: **component concentration predicts margin when the supplier's revenue spreads across programmes** — the discriminator is single-programme dependence, not buyer concentration | same | `DEMONSTRATED` |
| **Value migrated out of launch at the launch monopoly** — Connectivity 54.9%, AI 32.8%, Space 12.3% of SPCX revenue; Space −1.9% across a half in which consolidated revenue rose 53.7%; mass to orbit −25.6%, Falcon launches −17.8% | `001/_cross/…_synthesis.md` §4.6; `artifacts/SPCX/…_2310_operational-kpi_methodology.md` | `DEMONSTRATED` |
| **Fixed-cost absorption is the binding constraint** — PL break-even **1.69×** current revenue (53.5% GM, 90.6% opex ratio); YSS **2.86×** | `001/_cross/…_synthesis.md` §4.2 | `DEMONSTRATED` |
| **Terrestrial compute is constrained but expanding** — MSFT FY2026 capex $115,948M implies 2.9–11.6 GW/yr against SPCX's 1.4 GW cumulative; VRT margin *expanding* 2.7 pts on +24.1% revenue | `artifacts/MSFT/…_secular-trends_methodology.md` | `DEMONSTRATED` |
| **Orbital compute is out-*chosen*, not out-built** — SPCX deployed 1.4 GW on the ground, named data centers before launch facilities, buying Cursor at $60B | `001/_cross/…_synthesis.md` §Line 5 | `DEMONSTRATED` |
| **The demand side is 73× the supply side** — three pharma buyers turn over $39,634M/qtr vs a ~$2,170M/yr space cohort | `001/_cross/…_synthesis.md` §4.3 | `DEMONSTRATED` |
| **Four critical duopolies structurally unpriced** — solar cells, liquid engines, solid motors, radiation-tolerant electronics | `001/_cross/…_synthesis.md` §4.5 | `DEMONSTRATED` (structure) / `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (price) |
| **"No listed issuer offers both growth and margin except TER and KRMN"** | `001/_cross/…_synthesis.md` §7 | `DEMONSTRATED` |
| **Spectrum reference price $19.6B** (SPCX–EchoStar, AWS-4/H-Block/AWS-3) | `_cross/phase-4-regulatory-allocation.md` | `DEMONSTRATED` |
| IRDM and GSAT are **deal securities** — RKLB @$54/sh, AMZN @$90/sh | constitution §P11 | `CLAIMED` (terms from announcement) |
| The **corpus gap**: no industrial/aerospace domain exists, so sector-keyed strategy retrieval returns zero **by construction** | `theses/PROGRAM.md` §4 | `DEMONSTRATED` |

**What 001 did not do:** turn any of it into a position. 001 sized no trades and named no
strategy. Its synthesis ends at findings. 011 begins there.

---

## 1. Research Question

**Given that the sector's best margins belong to companies that are not space companies,
and its most space-pure names have the worst economics — is there an investment logic
that runs through every segment, and what does it tell us to own?**

Two sub-questions, in dependency order:
1. **Is the main line real?** — does one organizing argument explain the margin ladder,
   the launch-value migration, the fixed-cost-absorption finding and the orbital-compute
   disconfirmation simultaneously, or are these four unrelated facts?
2. **What does it imply?** — which strategies are *actionable*, which are watch items,
   and which are traps.

### 1a. The main line (P1 — formable now, from 001 alone)

> **Space is a cost curve, not a value pool.**

A1a holds — cheap launch *makes* orbital businesses possible. A1b is falsified — cheap
launch does **not** distribute the value to launchers. Value settles in the layers that
are **indifferent to which operator or programme wins**, and in the finite allocated
assets that are **priced rather than granted**. Everything else in the theme is a bet on
a specific programme winning — precisely the bet the sector punishes.

The organizing axis is therefore **distance from programme risk**, and it explains every
name in the universe without exception. The two extremes are the two traps: **diluted
space exposure** at the top of the margin ladder, **concentrated outcome risk** at the
bottom.

**The core finding, and this thesis's headline: you cannot buy this theme cleanly.**

### 1d. Split dependency (the sequencing change introduced at the clarify round)

| Pillars | Depends on | Can start |
|---|---|---|
| **P1–P5** — main line, strategies 1–4, the licensed-asset strategy | **001 alone** | **Now** |
| **P6** — watch items and their named triggers | 001, plus 002's disposition classes | Now |
| **P7** — sizing, catalyst calendar, theme-cap arithmetic | **004–010** | After wave 1–2 |

**The cost of this split, stated rather than hidden:** P7 cannot start, so this thesis
will produce an **unpositioned** main line first. A reader of the P1–P6 output gets the
argument and the strategy inventory but **no sizes and no entries**. That is deliberate —
the alternative was to defer the whole thesis to wave 3, which would have left the
program's governing argument unwritten while nine segment theses were researched against
it.

---

## 1b. Pillars

### Pillar 1 — The main line is real: one argument explains four independent findings (Priority: P1) 🎯 Minimum Defensible View

Four of 001's results were produced independently and reported separately. **The claim is
that they are one finding:**

| # | 001's finding | Its register |
|---|---|---|
| 1 | Margin monotone in distance from programme risk (8 issuers) | *who earns* |
| 2 | Value migrated out of launch at the launch monopoly | *where value went* |
| 3 | Fixed-cost absorption binds, not launch cost (PL 1.69×, YSS 2.86×) | *why operators lose* |
| 4 | Orbital compute out-*chosen* by the only actor who could choose it | *why the narrative didn't convert* |

Read together: **the sector pays for indifference to outcome and punishes concentration —
including concentration on the launch programme the theme is named after.** (2) is (1)
measured at the anchor; (3) is the mechanism by which (1) is enforced on operators; (4) is
(1) applied to the sector's largest narrative, where the most-indifferent actor available
— a monopolist launcher — chose the layer with diversified demand.

**Why this is the Minimum Defensible View**: it is the program's organizing claim. If the
four findings are *not* one argument, then the segment theses are unrelated and the
program has no spine — and that is a finding worth having before nine theses are built on
the assumption that it does.

**⚠️ The mechanism narrows to TWO axes — added at clarify round 2, 2026-09-18.** The
claim as first written was *"the sector pays for indifference to programme risk."* A
pressure test established that a second axis operates simultaneously and was not
distinguished:

| Axis | What it measures | The evidence |
|---|---|---|
| **1 — Programme concentration** | Whether the supplier depends on a single programme winning | HEI/KRMN (top of ladder) vs GSAT (monopsony, bottom) |
| **2 — Revenue recurrence** | Aftermarket/installed-base vs programme-contingent revenue | HEI is an **aftermarket** franchise at 25.5%; the primes are programme-contingent OEM at 10–12% |

**The strongest counter-argument to the main line is that axis 2 alone explains the
ladder as a business-model fact, not a programme-structure fact.** It does not — **the
ladder holds within OEM too**: KRMN (OEM components) 19.1% vs LMT (OEM prime) 12.4%. So
**both axes operate jointly, and the claim must be stated as both.** A thesis attributing
the ladder to either axis alone is `UNFRAMED_REFERENCE`.

**Independently falsifiable**: the four findings are shown to have independent causes —
e.g. the margin ladder is driven by accounting classification rather than programme
structure, or the launch migration is an entity-boundary artefact (see 002 P6 / 004 V-4).

**wrong_if**: `metric=count_of_the_four_findings_attributable_to_a_single_common_mechanism threshold=4 source=cross_issuer_filing_analysis op=<`

**Companion condition — added at clarify round 2 to prevent a false fire.** Margins
mean-revert for cyclical reasons unrelated to the structural claim, so the spread
inverting in a downturn would fire the falsifier without the claim being wrong. **The
falsifier therefore requires the spread to invert *while both layers' revenue is growing*,
and to persist across a full cycle — not merely to print negative once.** A single
negative print with falling component-layer revenue is a cycle, not a falsification.

**And the ladder must be extended before the mechanism is treated as established.** The
measured ladder covers **8 issuers, selected by which artifacts 001 happened to write** —
a genuine selection concern. **Extending it to the full 21-name Tier 3 list is assigned to
008**; until that runs, the claim is `DEMONSTRATED` on 8 names and `MODELED` beyond them.

**Subscribed**: `HEI × business-model`, `KRMN × business-model`, `GSAT × competitive`, `SPCX × business-model`, `PL × unit-economics`

---

### Pillar 2 — Strategy 1 is actionable but is not a space investment, and the report must say so (Priority: P2)

**The strategy**: own the indifference layer — component revenue spread across programmes
(HEI, KRMN, WWD, TDG). The margin ladder says these out-earn the primes they supply by
roughly 2×.

**The honest caveat, and the reason this pillar exists**: **HEI runs 2.6% R&D — it is an
aerospace aftermarket franchise, not a space company.** Its space exposure is incidental.
A reader who buys the margin ladder believing they have bought the space theme has bought
an aerospace trade and mislabelled it.

**The claim**: the strategy survives; **the label does not.** Each candidate's *space
revenue share* is quantified and reported next to its margin, so the dilution is visible
rather than implied. Where a name's space exposure cannot be isolated from filings —
which 001 found is the norm, since only LMT reports Space as a named segment and ULA is
equity-method invisible at both parents — that is recorded as a **disclosure limitation**,
not estimated.

**Why P2**: it is the highest-margin actionable idea in the workspace and the most likely
to be mis-sold. Grading it honestly is worth more than discovering it.

**Independently falsifiable**: a Tier 3b candidate whose filings disclose a space revenue
share large enough to make it a genuine space exposure at component-layer margins.

**wrong_if**: `metric=count_of_component_layer_candidates_with_a_disclosed_space_revenue_share_above_0.25 threshold=0 source=10-K_segment_and_revenue_disaggregation_tables op=>`

**Subscribed**: `HEI × business-model`, `HEI × ratio-analysis`, `KRMN × business-model`, `KRMN × competitive`, `WWD × business-model`, `TDG × business-model`

---

### Pillar 3 — Strategy 2 (fixed-cost absorption) is a valid screen and a statement about timing, not about space (Priority: P3)

**The strategy**: screen on break-even revenue multiple — `opex ratio ÷ gross margin` —
rather than on TAM. PL needs **1.69×** current revenue, YSS **2.86×**. Names inside a
lower band are investable on volume; names above an upper band are waiting on a financing
event.

**Why it is a pillar rather than a tool**: it is the **only mechanically reproducible
screen the sector supports**, and 001 established it answers the question PIL-3's
falsifier spent 19 documents failing to reach. But it is a *pre-profit industrial* screen
— it would work unchanged on any capital-intensive manufacturer — so it must be reported
as a timing instrument, not as a space-exposure instrument.

**The claim**: the screen is computable for every pre-profit name in the universe from
the income statement alone, its inputs are DA-23-clean by construction (component
identity), and it sorts the cohort into *fundable-through-break-even* and *needs-a-
financing-event*.

**Independently falsifiable**: a name that closes a >2× break-even multiple without
dilution, debt, or a revenue inflection.

**wrong_if**: `metric=count_of_preprofit_names_closing_a_break_even_multiple_above_2x_without_external_financing threshold=0 source=10-Q_cash_flow_statement_and_liquidity_note op=>`

**Subscribed**: `PL × unit-economics`, `YSS × unit-economics`, `RKLB × unit-economics`, `FLY × unit-economics`, `LUNR × unit-economics`

---

### Pillar 4 — Strategy 3 (the terrestrial expression) has the strongest evidence and the weakest space content (Priority: P4)

**The strategy**: if the compute narrative is the reason to own the theme, own it where
the compute actually is — VRT, NVDA, MSFT — not in the orbital aspirants.

**Why it is a pillar**: this is the workspace's **highest-confidence** finding (001 called
MSFT's capex datum *"the strongest single datum against the orbital-compute case produced
anywhere in this thesis"*), and simultaneously the **lowest-purity** expression of the
theme. It is the sharpest instance of the main line's core finding, and it is where a
reader is most likely to object that this is no longer a space investment at all.

**The claim**: the terrestrial layer's evidence is stronger than the orbital layer's on
every comparable axis (revenue: disclosed vs zero; capex: filed vs aspirational; margin:
expanding vs absent), and **the trade is only a space trade if the orbital case is the
thing being shorted** — which is a legitimate but different position from owning compute.

**Independently falsifiable**: an orbital-compute revenue disclosure, or a terrestrial
capacity build that fails to keep pace with the orbital alternative.

**wrong_if**: `metric=listed_issuer_orbital_compute_revenue_disclosed threshold=0 source=10-K_or_10-Q_segment_disclosure op=>`

**Subscribed**: `VRT × unit-economics`, `NVDA × secular-trends`, `MSFT × recent-quarter`, `GOOG × secular-trends`, `VRT × competitive`

---

### Pillar 5 — Strategy 4 (the deal spread) is actionable and is not a space view at all (Priority: P5)

**The strategy**: IRDM (RKLB @$54/sh) and GSAT (AMZN @$90/sh) are spread trades on
regulatory gates. P11 governs: do **not** underwrite standalone fundamentals; the price
tracks a spread; size at the **2% binary cap**; on a break, re-underwrite from scratch —
a failed deal leaves both target and acquirer re-rated and the acquirer carrying deal
costs.

**The chain is sequential, not parallel** (001's DA-18, upgraded from ambiguity to
checklist): FCC licence transfer → ITU coordination → DCSA/CFIUS-adjacent review →
national market access. **A thesis treating "regulatory approval" as a single event
understates the process by three gates.**

**The claim**: each deal's remaining gate chain is enumerated with expected dates and
named sources per the Catalyst Requirement, and the two positions are **low-correlation
to the rest of the book** — which is their actual portfolio value, since the book is
single-theme.

**Independently falsifiable**: a deal closing without clearing a named gate, or a gate
resolving from a source other than the one named.

**wrong_if**: `metric=count_of_deal_securities_closing_without_clearing_a_named_gate threshold=0 source=FCC_8-K_and_merger_proxy_disclosures op=>`

**Subscribed**: `IRDM × competitive`, `GSAT × competitive`, `SATS × risk`, `IRDM × recent-quarter`

---

### Pillar 6 — Strategies 5–7 are watch items with named triggers, not positions (Priority: P6)

Three strategy candidates **cannot be sized**, and the honest output is a watch list with
the specific event that would change that — not a papered-over position.

| # | Strategy | Why it cannot be sized | **The trigger that would change it** |
|---|---|---|---|
| 5 | **Licensed-asset play** — own the licence with diversified demand | Premise `DEMONSTRATED` ($19.6B EchoStar mark; IRDM profitable) but the falsifier — a new entrant granted primary spectrum without acquiring it — is **`UNRESOLVABLE-FROM-PLATFORM`** (FCC IBFS / ITU not in the corpus) | A transferable **$/MHz-pop** basis, or registry access |
| 6 | **Unpriced duopolies** — solar cells, liquid engines, solid motors | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — the structure is `DEMONSTRATED`, the *price* is not disclosed by either parent, so the positions cannot be sized | A unit disclosure from RKLB/SolAero, BA/Spectrolab, or a comparable transaction |
| 7 | **Demand asymmetry** — pharma demand 73× the space cohort | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — value-per-kg and cost-per-kg returned **do not exist publicly at all** (Varda private; UTHR immaterial to a $783M/quarter issuer) | Any value/kg or cost/kg figure; a Varda listing or disclosure |

**Why this pillar exists**: 001's most useful methodological output was that its three
unanswerable falsifiers failed for **three different reasons**, each with a different
remedy. The same discipline applies here: a watch item with a named trigger is a
different object from a position, and conflating them is how a research program acquires
positions it cannot defend.

**Independently falsifiable**: any of the three triggers occurring, converting a watch
item into a sized candidate.

**wrong_if**: `metric=count_of_watch_items_with_a_named_resolving_trigger threshold=3 source=this_thesis_artifact op=<`

**Subscribed**: `SATS × competitive`, `IRDM × competitive`, `UTHR × unit-economics`

---

### Pillar 7 — The book is sized, and the theme cap binds before the sub-sector cap (Priority: P7 — **BLOCKED on 004–010**)

**The strategy**: construct and size the book under the Risk Framework: ≤12 positions,
4% default / **2% binary** / 6% max single, ≤25% per sub-sector, **≤40% theme**, ≤15%
macro-driven, 30% thesis-driven stop.

**Why it is last and why it is blocked**: it is the only pillar that needs the segment
theses. In a **single-theme book the 40% theme cap binds before the 25% sub-sector cap** —
and the arithmetic of that, not the idea generation, is what forces cuts. Which names
must be cut cannot be known before the segment theses rank them.

**The claim**: the book's binding constraint is the theme cap, the arithmetic is shown
rather than asserted, and every position carries a dateable catalyst within 180 days
with its expected date and source — **where a catalyst cannot be dated, the position
cannot be sized against it.**

**Independently falsifiable**: a book satisfying the Risk Framework whose positions lack
dated catalysts, or whose theme-cap arithmetic is violated.

**wrong_if**: `metric=count_of_positions_without_a_dateable_catalyst_within_180_days threshold=0 source=constitution_Methodology_Foundation_catalyst_requirement op=>`

**Subscribed**: `SPCX × ratio-analysis`, `RKLB × ratio-analysis`, `KRMN × ratio-analysis`, `VRT × ratio-analysis`

---

> **Delivering P1 alone yields a defensible partial conclusion** — the program's governing
> argument is stated and falsifiable, or it is not. That is the single most valuable output
> of this thesis, and it is delivered first, without waiting for any segment thesis.

---

## 1c. Method — the corpus gap and how this thesis retrieves

**001's brief recorded that the knowledge corpus has no space content. This was
re-verified and it holds — with a material correction.** The finding is that
`list_domains` returns 9 domains whose `applicable_sectors` are `["med","tech","fin"]`
**only** — there is no industrial or aerospace domain in the registry at all.

**Consequence: the sector filter is a dead end *by construction*.** Any sector-keyed
query returns zero rows, and **reporting that emptiness as "no analogues exist" is a
false negative** — it is a fact about the registry, not about the world.

**Method, therefore — retrieve by STRUCTURAL SITUATION, not sector tag:**

| Analogue | Situation shape | Transfers to |
|---|---|---|
| **Disruptive Food-Tech Cost Curve Arbitrage** | Exponential cost decline vs incumbent parity — *explicitly modelled on solar PV and semiconductors* | **The main line itself** — a cost curve is not a value pool |
| **Platform Technology Monetisation via Licensing** | Platform owner captures more than the end-product developer | **A1b** — who captures value in the stack |
| **Cross-Listed Biotech Arbitrage ("US Premium")** | Non-US assets at a structural discount, realising via cross-listing or acquisition | Eutelsat, Avio, SKY Perfect JSAT, Astroscale — the excluded tier |
| GATX (railcar leasing) | Capital-intensive asset leasing; utilisation-driven returns | Fixed-cost absorption (P3) |
| CNR (rail) | Toll-road infrastructure network | The launch-as-toll-road framing under A1a |
| Linde | Oligopoly pricing power in an industrial gas | The unpriced solar-cell duopoly (P6) |
| KBR | Government engineering services; programme concentration | The primes' space-segment dilution (P2) |
| Coatue — Meta | Regulatory overhang + drawdown + rebuild | The deal securities (P5) |

**Labelling rule, and it is binding.** Every borrowed analogue is labelled **borrowed**.
A cost-curve strategy derived from cultivated meat is a *shape* match, not sector evidence.
Presenting it as sector evidence is a P4 violation.

**Verified present, and previously missed — the correction.** The corpus carries cases on
**two names already in this universe**, filed under `Industrials` rather than a space tag:
**Moog (`MOG-A`)** — Brown Advisory, **~2.1–2.5× on cost, ~110–150% total return over ~3
years, IRR ~28–38%** — and **EnerSys (`ENS`)**. **Both are `NOT_READY` on issuer coverage.**
A case that cannot be validated against filings, and coverage that would not surface the
manager's reasoning: **neither alone is sufficient**, and the asymmetry is an actionable
coverage-acquisition priority.

## 2. Universe Definition

Universe names are the **strategy candidates**, not a research cohort — this thesis reads
001's findings and grades positions rather than analysing businesses afresh. Weights are
analytical effort, not positions; **P7 sizes, and it is blocked.**

| Ticker | Company | Sector | Role in this thesis | Weight |
|---|---|---|---|:---:|
| HEI | Heico | industrial.aerospace_defense | **Strategy 1** — the ladder's top rung; the dilution case | 8% |
| KRMN | Karman Holdings | industrial.aerospace_defense | **Strategy 1 + the only genuine "both" name** | 8% |
| WWD | Woodward | industrial.aerospace_defense | Strategy 1 — the middle rung | 4% |
| TDG | TransDigm | industrial.aerospace_defense | Strategy 1 — the pricing-power control | 4% |
| PL | Planet Labs | industrial.aerospace_defense | **Strategy 2** — the 1.69× canonical case | 6% |
| YSS | York Space Systems | industrial.aerospace_defense | Strategy 2 — the 2.86× case | 5% |
| RKLB | Rocket Lab | industrial.aerospace_defense | Strategy 2 + **P11 deal** (acquiring IRDM) | 8% |
| FLY | Firefly Aerospace | industrial.aerospace_defense | Strategy 2 — highest R&D intensity in the universe | 4% |
| LUNR | Intuitive Machines | industrial.aerospace_defense | Strategy 2 — pre-profit, capital-hungry | 3% |
| VRT | Vertiv | industrial.machinery | **Strategy 3** — the terrestrial thermal enabler | 7% |
| NVDA | NVIDIA | tech.semiconductors | Strategy 3 — compute silicon | 5% |
| MSFT | Microsoft | tech.platform_internet | Strategy 3 — the capex datum | 6% |
| GOOG | Alphabet | tech.platform_internet | Strategy 3 — Suncatcher, the orbital aspirant. **Query as `GOOG`, never `GOOGL`** | 4% |
| IRDM | Iridium | tech.telecom_services | **Strategy 4 + 5** — deal security; the diversified-demand licence | 7% |
| GSAT | Globalstar | tech.tech_hardware | **Strategy 4** — deal security; the monopsony case (7.4%). **Files under `tech_hardware`, not telecom — a telecom-keyed screen silently drops it** | 6% |
| SATS | EchoStar | tech.telecom_services | **Strategy 5** — the $19.6B spectrum mark | 5% |
| UTHR | United Therapeutics | med.medicines_biotech | **Strategy 7** — the demand-asymmetry watch item | 5% |
| SPCX | SpaceX | industrial.aerospace_defense | **The anchor the whole main line is measured at** | 5% |

**Excluded by design:** the `NOT_READY` names (including **MOG-A** and **ENS**, which
carry corpus cases but no coverage) and the `PARTIAL` names (ASTS, VSAT, AMZN, AAPL,
TRMB, GRMN, PLTR, LLY), which require manual sector assignment. The foreign-listed tier
(Eutelsat, Avio, SKY Perfect JSAT, Astroscale) is **excluded by the Research Scope
Constraints** and admissible only as read-through — which makes the Cross-Listed Biotech
analogue above a *shape* match with no purchasable instrument, and that must be said.

## 3. Skill Deployment Matrix

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|:---:|---|:---:|---|
| business-model | equity-research-core | Standard | HEI, KRMN, WWD, TDG, SPCX | none | **Strategy 1's dilution quantification** — space revenue share beside margin (**P2**); the main line's anchor reading (**P1**) |
| unit-economics | business-intelligence | Standard | PL, YSS, RKLB, FLY, LUNR, VRT, UTHR | none | **Strategy 2's break-even multiple** computed per name (**P3**); the 73× demand test (**P6**) |
| secular-trends | equity-research-core | Standard | NVDA, GOOG | none | **Strategy 3's** orbital-vs-terrestrial evidence (**P4**) |
| competitive | equity-research-core | Standard | GSAT, IRDM, SATS, VRT, KRMN | none | The monopsony case (**P1**, **P2**); the licensed-asset and duopoly watch items (**P6**) |
| risk | equity-research-core | Standard | SATS, SPCX, IRDM | none | **Strategy 4's** sequential gate chain (**P5**); disposition classes (**P6**) |
| recent-quarter | equity-research-core | Standard | MSFT, IRDM, SPCX | none | Freshness anchor for every quoted figure; the capex datum (**P4**) |
| ratio-analysis | quantitative-analysis | Light | HEI, KRMN, SPCX, RKLB, VRT | none | **P7's** theme-cap arithmetic, when unblocked |

> **Coverage invariant.** Every ticker in §2 appears at least once above; every
> `Subscribed` pair in §1b generates at least one task. Verified by `tools/plan_audit.py`.

**Budget**: this matrix yields roughly **26 tasks**, deliberately small — this thesis
consumes 001's conclusions and does not re-research businesses. `max_tasks: 30` in
`thesis.md`. **Pillars P1–P6 use approximately 20; P7's block reserves 10 for when
004–010 land.**

## 4. Depth Tiers

| Tier | Skills | mode-set | Tickers | Output |
|:---:|------|---|--------|------|
| Standard | business-model, unit-economics, secular-trends, competitive, risk, recent-quarter | essentials_modes | As listed | The main line, four actionable strategies, three watch items |
| Light | ratio-analysis | essentials_modes | HEI, KRMN, SPCX, RKLB, VRT | Theme-cap arithmetic (deferred with P7) |

## 5. Cross-Cutting Analysis

- **The main line** is the cross-cutting output and the program's governing argument.
- **The strategy inventory** — 7 candidates, 4 actionable, each with its dilution or its
  blocking condition stated.
- **Macro sensitivity: high, and immediately binding.** This is the only thesis that
  turns findings into positions. The constitution's bias is **NEUTRAL** precisely because
  the universe is long-duration and the 10Y sits at **4.80%** with hike risk priced. **A
  NET_LONG expression of the main line is a bet on duration, not on space.** P7 must size
  through that lens or say why not.
- **Constitution interaction**: P4 governs every grade; P11 governs P5; the Data-Integrity
  Register governs every figure inherited from XBRL; P10 forbids underwriting orbital
  compute; the Risk Framework's theme cap is P7's binding arithmetic.

## 6. Output Contract

- **Per-ticker (dispatcher-resumable)**: `artifacts/{ticker}/{YYYY-MM-DD}_{skill}_{mode}.md`
  — suffix **must** be `_{skill}_{mode}.md`.
- **Cross-cutting (not resume-tracked)**: `_cross/{name}.md`.
- **Primary artifact**: `_cross/main-line-and-strategy-inventory.md` — the governing
  argument, its falsifiers, and the 7-strategy table with honest actionability grading.
  **This is the artifact the program is organized around.**
- **Deferred artifact**: `_cross/position-sizing.md` — written only when P7 unblocks.
- Snapshot: `snapshots/011-idea-generation/{YYYY-MM-DD}_thesis.md`
- **P11**: every artifact on IRDM or GSAT must set `deal_security_basis`.

## 7. Thesis Phases

| Phase | Tasks | Duration | Dependencies |
|:---:|------|:---:|------|
| 1 — The main line (P1) | Test the four findings for a common mechanism; state the governing claim; register its falsifiers | Week 1 | **001 alone** |
| 2 — Dilution (P2) | Space revenue share beside margin for the component layer; grade the label | Week 2 | Phase 1 |
| 3 — The screen (P3) | Break-even multiple per pre-profit name; sort into fundable / needs-financing | Week 3 | Phase 2 |
| 4 — The terrestrial expression (P4) | Grade the strongest-evidence/weakest-purity trade honestly | Week 4 | Phase 3 |
| 5 — Deals and watch items (P5, P6) | Gate chains per deal; named triggers for strategies 5–7 | Week 5 | Phase 4 |
| 6 — Publish | `_cross/main-line-and-strategy-inventory.md` | Week 6 | Phase 5 |
| 7 — Sizing (P7) — **BLOCKED** | Theme-cap arithmetic; catalyst calendar; position sizes | on unblock | **004–010** |

## Clarifications

Recorded by `agentii.clarify` — **two rounds, both on 2026-09-18, both invoked on 002**
and resolved by moving the main line here. On **both** rounds the scanner reported **0
mechanical candidates** on 002; every question below was raised manually, since the
deterministic scan cannot see intent, and neither could it see a claim that needed
narrowing or a constitution table that contradicted itself.

**Round 1** established *where* the main line lives. **Round 2** pressure-tested *whether
it is true* and found a constitution defect the first round missed.

- [2026-09-18] **Q-1 (scope, raised on 002)**: *"Can we form a main-line investment logic
  for space tech in thesis 002 — a big logic running through all the segments, or several
  strategies?"* → **A: yes, the main line is formable — but it does not belong in 002.**
  002 is chartered validation-only (*"produces no trade ideas, sizes no positions"*), and
  the main line is a synthesis output. Disposition: the main line is written into
  **`theses/PROGRAM.md` §0b** as the program's governing argument and becomes **011's P1**.
  002 gains no pillar. **Recorded here rather than in 002 because this thesis is its home.**

- [2026-09-18] **Q-2 (sequencing, raised with Q-1)**: should 011 stay in wave 3, gated on
  004–010? → **A: no — split the dependency.** The main line and the strategy layer depend
  only on 001 and **start now** (P1–P6); sizing (P7) keeps the segment dependency. The cost
  — an unpositioned main line first — is stated in §1d rather than hidden.

- [2026-09-18] **Q-3 (the purity/margin tension)**: the evidence says the theme's
  investable content is mostly *adjacent* to space. How should the program handle it? →
  **A: state it as the main line's core finding** — *"you cannot buy this theme cleanly"* —
  and screen on **margin quality and programme indifference, not on space purity**. A
  screen that filters for space exposure selects for exactly the property the margin
  ladder penalizes.

- [2026-09-18] **Q-4 (RESOLVED, round 2)**: strategies 5–7 cannot be sized — is a watch
  item with a named trigger an acceptable *output*, or should the program attempt the
  unpriced-duopoly work (strategy 6) despite 001 judging it
  `UNRESOLVABLE-FROM-PUBLIC-SOURCES`? → **A: accept the watch item; do not attempt
  strategy 6.** A watch item with a named trigger is *falsifiable*; a position on
  unresolvable data is not. The constitution already provides two disposition classes
  for exactly this. 001 established neither parent discloses the solar-cell unit, so
  there is nothing to size.

- [2026-09-18] **Q-5 (RESOLVED, round 2)**: P7 is blocked — does the wave-1 hand-off
  accept an unpositioned main line, or should P7 be unblocked early by promoting 008 into
  wave 1? → **A: swap 003 out of wave 1 for 008.** 001 already settled the cost curve's
  *level* and that value left launch, so 003 is refinement; **008 is where the ladder says
  the returns are.** **006 stays** — Connectivity is the one OW/High rating 001's evidence
  actually supports (SPCX Connectivity at a 38.6% operating margin). Wave 1 becomes
  **002, 004, 005, 006, 008**; 003 moves to wave 2.

- [2026-09-18] **Q-6 (round 2 — a constitution defect this round found)**: *"Sector
  Preferences rates Launch Services Overweight/High on the rationale 'The toll road' —
  which IS the A1b claim that §0 declares falsified."* The v1.3.0 A1a/A1b split was
  **not propagated** to the sub-sector table, leaving the constitution internally
  contradictory in three rows. → **A: fix the rationales, keep the biases.**
  Executed as **constitution v1.4.0** (MINOR): Launch stays OW/High restated on an
  A1a-consistent basis (unit economics + the cost curve, not value accrual); Space
  Infrastructure stays Neutral/Medium because the layer is **not space-pure** (HEI 2.6%
  R&D); Earth Observation stays UW/Low as a **timing** judgment, not a structural one.
  **No bias changed, no cap moved, no wave ordering altered.**

- [2026-09-18] **Q-7 (round 2 — tightening three claims)**: pressure-testing the main
  line found three items needing narrowing rather than restatement. → **A: fold into 011
  as it runs.** (i) **P1's mechanism now names TWO axes** — programme concentration *and*
  revenue recurrence — because the strongest counter-argument is that the ladder is an
  aftermarket-vs-OEM artifact; it is not, since the ladder holds within OEM (KRMN 19.1%
  vs LMT 12.4%), so both axes operate jointly. (ii) **The falsifier gains a companion
  condition** — the spread must invert *while both layers' revenue grows*, across a full
  cycle, or a cyclical mean-reversion fires it falsely. (iii) **The "AI 32.8%" figure is
  boundary-contaminated** (xAI merged 2026-02-02 under common control, recasting prior
  periods) and may not be quoted as organic migration — **routed to 002 P6**, which owns
  entity-boundary classification, with Space (clean, and the series that fell) and
  Connectivity (clean, organic) carrying the migration claim instead. **The main line
  survives all four pressure tests; three required tightening.**

- [2026-09-18] **Q-8 (round 2 — assigned, not resolved)**: the margin ladder covers
  **8 issuers selected by which artifacts 001 happened to write** — a selection concern
  the pressure test could not settle. → **A: extend it to all 21 Tier 3 names, assigned to
  008** (which owns Tier 3). Until it runs, the mechanism claim is `DEMONSTRATED` on 8
  names and `MODELED` beyond them. **This is bounded work — a margin is one income
  statement.**
