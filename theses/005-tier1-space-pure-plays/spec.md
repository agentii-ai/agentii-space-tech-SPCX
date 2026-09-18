# Research Thesis: 005 — Tier 1: Listed Space Pure-Plays

**Constitution Ref**: constitution.md v1.4.0 (`constitution_pin: 1.4.0`)
**Created**: 2026-09-18
**Status**: Active
**板块**: Tier 1 · Wave 1
**Time Horizon**: 2026-Q4, terminating at the RKLB/Iridium close (expected mid-2027) or
at the wave-2 hand-off to 008/009, whichever comes first
**Depends on**: `001-technology-baseline` (pin 1.2.0 — inherited, below), `002-evidence-validation`
(validated input set), `003-launch-cost-curve-value-migration` (the value-pool map this
thesis ranks against), `004-tier0-spacex-anchor` (the benchmark every Tier 1 name prices off)
**Binding constraint**: **`MULTI` — DECLARED.** The P3 compromise, stated in full in §1.
It is not an omission; it is a named position, and it carries a stated cost.
**Produces**: a ranked Tier 1 cross-section, a Tier 1 **constraint map** (exactly one
binding constraint per *decision* — one per name, except RKLB, which contains two), a
sub-sector mapping that makes the Concentration Rule evaluable, and **at most three**
capped position slots. Not a book.

---

## 0. Inherited baseline — what this thesis does NOT re-derive

001 established the following. This thesis **takes them as given**; re-deriving any of
them is out of scope. Every row cites the artifact, so the inheritance is verifiable
rather than trusted. Paths are repo-relative.

| Inherited result | 001 artifact | Grade |
|---|---|---|
| Launch is the master **cost** variable (A1a **holds**) and **not** the master **value** variable (A1b **falsified**), on three independent issuer confirmations | `theses/001-technology-baseline/artifacts/FLY/2026-09-18_1239_unit-economics_methodology.md`; `theses/001-technology-baseline/artifacts/RKLB/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` |
| **Electron basis A = $30,333/kg; basis B = $14,667/kg** — the only demonstrated per-launch cost in the universe, at a **`CLAIMED` 300 kg** payload | `theses/001-technology-baseline/artifacts/RKLB/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` on the cost; **denominator `CLAIMED`** |
| **Electron is 10.3× Falcon 9 per kg** on basis A — the small-lift penalty, quantified from filed data | same | `DEMONSTRATED` |
| RKLB **built 14 / launched 16** (2024), **24 / 21** (2025), **11 / 12** (H1 2026) → demand- or production-limited, **not launch-limited** | same | `DEMONSTRATED` |
| RKLB revenue **+62%** with **launch revenue −$2.1M** (declining); growth from space systems **+$91.6M** | same | `DEMONSTRATED` |
| **YSS gross margin 24.0% against an opex ratio of 68.6%**; fixed costs are **2.9× gross profit** → a **volume** problem, not a unit-economics problem | `theses/001-technology-baseline/artifacts/YSS/2026-09-18_1239_operational-kpi_methodology.md`; `theses/001-technology-baseline/_cross/phase-3-production-supply.md` | `DEMONSTRATED` |
| **YSS revenue −20.5% QoQ** ($92.547M vs $116.343M), carried forward **UNSMOOTHED** against the volume reading | `theses/001-technology-baseline/artifacts/YSS/2026-09-18_1239_operational-kpi_methodology.md` | `DEMONSTRATED` |
| FLY revenue **+657% to $117.7M** "driven by Spacecraft Solutions"; **GM 20.3%** (weakest of the three); **R&D 60.8% of revenue** (highest in the universe); operating loss **$(95.2)M**; **emerging growth company** | `theses/001-technology-baseline/artifacts/FLY/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` |
| Space-grade solar cells are a **two-supplier duopoly** (RKLB/SolAero · BA/Spectrolab) — **structural, but unpriced**: neither parent discloses the unit | `theses/001-technology-baseline/_cross/phase-3-production-supply.md` | `DEMONSTRATED` (structure) / **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** (price) |
| **PIL-3's falsifier was never evaluated.** It is **PENDING**, not failed — the disclosure is public, it simply has not been read | `theses/001-technology-baseline/_cross/phase-3-production-supply.md` | **`UNMEASURED`** |
| **DA-25**: RKLB's disclosed `revenue per launch` implies a **51.6%** launch gross margin; the audited segment table implies **42.9%** | `theses/001-technology-baseline/artifacts/RKLB/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` |
| Backlog at 2026-06-30: **RKLB $2,355.9M**, **FLY $1,468.1M** (up **8.7%** from $1,351.1M) — a demand-side datum, not a launch-side one | `theses/001-technology-baseline/artifacts/FLY/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` |
| **DA-13** — production rate in units is disclosed by **exactly one issuer** in the universe (RKLB). Every cross-issuer manufacturing-rate comparison is blocked by this | `theses/001-technology-baseline/artifacts/YSS/2026-09-18_1239_operational-kpi_methodology.md` | `DEMONSTRATED` (the absence) |
| **The margin ladder inverts the narrative**: space operators sit at the bottom at **−24.6% to −44.6%** operating margin, below every component supplier | `theses/001-technology-baseline/thesis.md` (status log, Phase 7 synthesis) | `DEMONSTRATED` |
| **The manufacturing constraint is queue position, not capability** — TER's single-year revenue increase (~$2,100M) approximately equals the combined annual revenue of every pure-play space company in the universe (~$2,170M) | `theses/001-technology-baseline/thesis.md` (status log, `TER × operational-kpi`) | `DEMONSTRATED` |

**What 001 did not do.** 001 covered Tier 1 only through the lens of specific pillars —
YSS for manufacturing rate, RKLB and FLY for launch unit economics, LUNR/PL/HAWK at
Light depth only. **It never asked the cross-sectional question**: given A1b is
falsified — value does *not* accrue to launch — **which pure-plays are positioned where
value actually went?** That cross-section is this thesis's entire scope.

### Validation queue — the Tier 1 figures this thesis owns

**Denominator and physics validation is 002's, not this thesis's.** 002 owns the three
`CLAIMED` denominators (Electron 300 kg, Falcon 9 22.8 t, Starship 100 t), F2's
unsourced constants, and the DA-23 census universe-wide. **005 owns the Tier 1-specific
contested figures below** — the ones no other thesis can resolve, because no other
thesis reads this cohort. Where a 005 conclusion depends on a 002-owned number, the
dependency is named in-line and the conclusion carries 002's band.

| Tier 1 contested figure | Current state | Disposition required here |
|---|---|---|
| **YSS Q1 2026 operating figure $110.466M on $116.343M revenue — a 95% "margin"** | Flagged by 001 as *"a plausible weak point in the DA-23 record"*; never checked at component level | Resolve from components, or register as a **fourth defect class**. **002 owns the census; 005 owns the Tier 1 read.** |
| **VOYG reported operating income $51.408M against gross profit $4.457M** — fails the gross-profit bound by **$46,951M** across three consecutive quarters | DA-23 **candidate**, new sub-mechanism: not a sign inversion but an **unreconcilable level** | The operating line is **unusable** until reconciled. VOYG's capital-structure and margin work proceeds on other lines. |
| **LUNR Q4 2025 operating margin 42.1%** (2024 quarters ran ~7.4%) | DA-23 candidate; **no quarterly gross-profit line exists**, so the component identity **cannot run** | Margin-plausibility detector only; recorded as a **detector-availability** finding, not an issuer defect. |
| **HAWK: four non-agreeing share counts (4.2M – 98.0M), EPS bridge fails by 72%**, Q2 2026 listing | DA-28 candidate; extract inconsistent three independent ways | Any EPS- or share-count-based screen **false-positives on recent listings**. A listing-date guard is mandatory. |
| **KRMN: capital structure absorbs 60% of operating income** ($34.829M operating vs $14.032M net) | Demoted from defect to **structure** | Operating-margin rankings **overstate levered suppliers**; the below-the-line bridge must be shown in-line. |
| **PL Q2 loss $(34.888)M** — gross profit $50.401M − opex $85.289M, the cleanest DA-23 instance | Resolved by 001 | Inherited. Not re-derived. |
| **RKLB/Iridium combined entity**: $3.6B bridge facility plus stock consideration; pro-forma combined financials are **not disclosed** | `CLAIMED` (constitution P11) | `MODELED` only. A model may not satisfy a falsifier under P4. |
| **Deal values**: Iridium **~$8B** (announced 2026-06-29, close expected mid-2027), All.Space **~$355M** (agreed 2026-04-29), Astrobotic **~$300M** | All press-sourced and unaudited — `CLAIMED` under P4; pointers: constitution §A5 and §Tier 1 | Admissible as context and for **structure**; **never as a valuation input**. |
| **SolAero and Spectrolab unit revenue** | Does not exist publicly. RKLB discloses SolAero at no granularity; Spectrolab is immaterial inside a $24.6B/quarter parent | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`.** The BA leg belongs to **007**; 005 records the gap and **does not substitute a proxy**. |
| **YSS's 68.6% opex ratio may be All.Space deal-cost inflated** | Open carry-forward from 001 Phase 3 | Segment confirmation required before the fixed-cost multiple is quoted as a run-rate. |

---

## 1. Research Question

**Within the listed pure-play layer, which business models actually convert launch-cost
decline into shareholder value — and which are simply levered to a narrative?**

A1b is falsified: value did not accrue to the launcher. SPCX grew **+91.9%** with Falcon
launches **−18%**; RKLB grew **+62%** with launch revenue **−$2.1M**; FLY grew **+657%**
from Spacecraft Solutions. If value migrated away from launch, then a cohort of
companies *defined by* launch-adjacency should not all be priced as though the migration
had not happened. Some of them are positioned where value went. Some are not. **Telling
those two groups apart is the question, and the cohort is small enough to answer
cross-sectionally rather than one name at a time.**

Three sub-questions follow and are not separable from it:

1. **Survival before positioning.** These are pre-profit, rate-sensitive issuers in a
   NEUTRAL-bias regime with the 10Y at **4.80%**, the highest long end since 2023. A
   pure-play that cannot fund itself to profitability is not a value-capture question at
   all — it is a financing question wearing one.
2. **Distance from the value pool.** Per A1b, services, constellations and operations
   capture what launch no longer does. Where does each pure-play sit relative to that
   pool — and is the position *revenue-evidenced* or *narrated*?
3. **Whether the constraint is real.** 001 left PIL-3's falsifier **unmeasured** and
   proposed replacing a 19-document risk-factor read with two cheaper behavioural tests.
   Those tests have never been run across the cohort.

### The P3 compromise — declared, not hidden

**P3 requires exactly one binding constraint per thesis.** This thesis cannot honestly
name one, and says so rather than choosing the modal answer and presenting it as
binding. The reasons are specific:

1. **Tier 1 is not one business model.** It contains a launch provider that owns a
   solar-cell supplier (RKLB), a launch provider integrating an acquisition (FLY), a
   lunar lander and services firm (LUNR), an Earth-observation operator (PL), a
   component supplier (KRMN), a space-station and defense firm (VOYG), a satellite
   manufacturer (YSS), and an RF-geolocation / SIGINT data business (HAWK). Naming
   `CAPITAL` for the cohort would be a statement about the balance sheets; naming
   `DEMAND` would be a statement about the order books; naming `MANUFACTURING_RATE`
   would be a statement about the production lines. **All three are true of different
   names, and the disagreement is the finding.**
2. **`CAPITAL`, `DEMAND` and `MANUFACTURING_RATE`** — three of the eight permitted
   values — are each the binding constraint for a different subset of the cohort. Naming
   one would assert in the header what the cross-section exists to establish. Tier 1 and
   Tier 4 are the program's two declared multis; this is what the Tier 1 one means.
3. **P3's own second sentence supplies the remedy.** *"A thesis whose narrative depends
   on two or more constraints relaxing simultaneously is a compound bet and must be
   sized as a binary catalyst."* The declaration therefore **forces a sizing
   consequence**: at most **3 positions** in Tier 1 (Concentration Rule), each under the
   **2% binary cap** — a **maximum Tier 1 footprint of 6% of NAV**. A thesis that could
   name one constraint would size larger. This one cannot, and its size reflects that.
4. **The compromise is discharged at the level where it matters.** The thesis produces
   a per-name **constraint map** in which every researchable Tier 1 name carries
   **exactly one** permitted constraint value, evidenced — one per name, except RKLB,
   which carries two because it contains two decisions (standalone business, deal leg).
   **The thesis-level constraint is multi; the decision-level constraint is single**,
   and every sizing decision in this thesis is taken at the decision level. That is the
   honest form of P3 compliance here, and it is the first deliverable, not a closing note.

---

## 1b. Pillars

### Pillar 1 — Every Tier 1 pure-play's funding runway to profitability is computable, and none is inside 24 months of involuntary recapitalisation (Priority: P1) 🎯 Minimum Defensible View

This is the Minimum Defensible View because **it is the only pillar that can make the
others irrelevant.** The cohort is pre-profit, the regime is NEUTRAL, and the long end
is at **4.80%** — three-year highs, with the market pricing hike risk rather than cuts.
A pure-play that has to return to the capital markets before it reaches breakeven is
making a financing bet, not a value-capture bet, and no amount of positioning changes
that. **Survival is the precondition; positioning is the question.**

**The claim:** for each of the eight researchable Tier 1 names, disclosed cash, disclosed
operating cash burn, and committed facilities support a **runway in months**; and the
cohort separates cleanly into **self-funding** and **externally dependent** — with **no
name inside 24 months of involuntary recapitalisation** without committed financing. The
split, not a single verdict, is the output: it tells 011 which names can wait for the
value migration and which are on a clock.

**What counts as computable.** Runway is computed from the **cash-flow statement**, not
from a press release or a shelf registration. A committed facility counts only if it is
drawn or undrawn-and-available under a disclosed agreement with a named counterparty. An
ATM programme is **not** committed financing — it is access to a market that may be shut.
Where runway cannot be computed from disclosure, the name is recorded with its blocking
disclosure named, and the pillar reports **how many names were computable** rather than
asserting a cohort conclusion over a partial set.

**Why this is P1 and not P2**: the answer gates the other five pillars. A name that fails
P1 cannot be sized at any priority level, so running P2–P6 first would produce a ranking
that cannot be acted on.

**Independently falsifiable**: any Tier 1 name with under 24 months of disclosed runway
and no committed facility.

**wrong_if**: `metric=count_of_tier1_pure_plays_with_less_than_24_months_disclosed_funding_runway_and_no_committed_facility threshold=0 source=10-Q_cash_flow_statement_and_liquidity_note op=>`

**Subscribed**: `RKLB × recent-quarter`, `FLY × recent-quarter`, `YSS × recent-quarter`, `LUNR × recent-quarter`, `PL × recent-quarter`, `KRMN × recent-quarter`, `VOYG × recent-quarter`, `HAWK × recent-quarter`, `BKSY × recent-quarter`, `RKLB × ratio-analysis`, `FLY × ratio-analysis`, `YSS × ratio-analysis`, `VOYG × ratio-analysis`, `LUNR × ratio-analysis`, `KRMN × ratio-analysis`, `RKLB × risk`, `FLY × risk`, `LUNR × risk`, `VOYG × risk`

---

### Pillar 2 — Value capture ranks the cohort, and the ranking is measured rather than narrated (Priority: P2)

A1b says value migrated to services, constellations and operations. If that migration is
real *at the pure-play layer*, then the cohort's revenue composition should show it — and
the names closest to the value pool should carry the better growth-and-margin pairing.
**If instead hardware sales remain the majority of Tier 1 revenue, then "value capture"
is an overlay on a cohort that is still what it always was, and the ranking is a
narrative, not a measurement.**

**The claim:** Tier 1 aggregate revenue can be classified into **hardware sales and
manufacturing** versus **services, operations and constellation capacity**, from the
segment and disaggregation tables, per issuer; and the resulting ranking is stable
enough to order the cohort. The KRMN/HAWK data-services models and the YSS/VOYG
hardware models should land in different halves. **The constitution already takes a
position here** — Earth Observation & Geospatial is the one sub-sector marked
**Underweight / Low**, on *"commoditized imagery, government-concentrated demand,
persistent negative unit economics"* — and PL and BKSY sit in it. This pillar tests
whether the platform's own sector bias survives contact with the cohort.

**Why this priority**: it is the thesis's actual research question, and it is P2 rather
than P1 only because it is unactionable until P1 says who can wait. It is ranked above
the manufacturing question because the manufacturing question is inherited and this one
is new.

**Classification discipline.** Every issuer's revenue is classified by **its own
segment definitions** (DA-21), and the classification is stated per issuer, never
aggregated across issuers on the assumption that the segments mean the same thing. The
value pool is defined precisely: revenue from **services, operations, or constellation
capacity** — as distinct from hardware delivered to a customer.

**Independently falsifiable**: hardware sales and manufacturing remain more than half of
Tier 1 aggregate revenue, meaning the cohort's centre of gravity has not moved and the
value-capture ordering carries no information the sector-membership ordering did not.

**wrong_if**: `metric=share_of_tier1_aggregate_revenue_from_hardware_sales_and_manufacturing threshold=0.5 source=10-Q_segment_and_revenue_disaggregation_tables op=>`

**Subscribed**: `RKLB × business-model`, `YSS × business-model`, `VOYG × business-model`, `KRMN × business-model`, `HAWK × business-model`, `RKLB × unit-economics`, `YSS × unit-economics`, `FLY × unit-economics`, `PL × competitive`, `BKSY × competitive`, `HAWK × competitive`, `LUNR × competitive`, `PL × secular-trends`, `LUNR × secular-trends`, `VOYG × secular-trends`, `RKLB × sector-overview`, `YSS × sector-overview`, `PL × sector-overview`, `KRMN × sector-overview`, `RKLB × peer-bench`, `FLY × peer-bench`, `YSS × peer-bench`, `KRMN × peer-bench`, `LUNR × peer-bench`

---

### Pillar 3 — Manufacturing rate, not launch availability, is the binding constraint at the pure-play layer — tested behaviourally, not by prose (Priority: P3)

**This pillar inherits PIL-3 and re-scopes its falsifier, exactly as 001 proposed.**
PIL-3's original test — the share of named issuers citing launch availability as the
primary delay cause — requires reading risk factors and MD&A across ~19 documents, was
**never executed**, and remains `PENDING`. 001's carry-forward named two cheaper
instruments that do not read prose at all:

1. **The build-vs-launch behavioural test.** A launch-limited company accumulates
   unlaunched inventory; a demand-limited company draws it down. RKLB's filings show
   **14 built / 16 launched** (2024), **24 / 21** (2025), **11 / 12** (H1 2026) — drawdown
   in two of three periods, which is not the behaviour of a launch-constrained firm.
2. **The margin-multiple test.** A manufacturer whose fixed costs are a **multiple** of
   its gross profit is **volume-constrained by arithmetic**, whatever its filings say
   about delays. YSS at **24.0% gross margin against a 2.9× fixed-cost-to-gross-profit
   multiple** is the worked example.

**⚠️ 001's published synthesis has already answered this pillar's question, and the
answer is stronger than the pillar was scoped to find.** `_cross/technology-baseline_synthesis.md`
§4.2 established the bound directly from XBRL — *"the binding constraint on space
operators is fixed-cost absorption"* — and it did so with a **Tier 1 name as the
canonical case**:

| Issuer | Gross margin | Opex ratio | Break-even revenue multiple |
|---|---:|---:|---:|
| **PL** | **53.5% — best in the universe** | **90.6%** | **1.69× current revenue** |
| YSS | 24.0% | 68.6% | **2.86× current revenue** |

**PL earns the universe's best gross margin and still loses 37% at the operating line**
because opex is 90.6% of revenue. **Neither multiple involves launch cost.** The
synthesis's own verdict: *"This is the finding PIL-3's falsifier was trying to reach by
reading risk-factor prose, and XBRL answers it directly."*

**Consequence for this pillar — its scope changes.** The question is no longer *"is the
cohort launch-limited or demand-limited?"* (answered: neither — **it is fixed-cost
absorption, and the arithmetic is in the income statement**). The open question is
**which Tier 1 names can close a 1.69×–2.86× revenue gap before their funding runs out**
— which is why this pillar is now bound to Pillar 1's runway test rather than standing
alone. **A Tier 1 name whose break-even multiple exceeds its funding runway is a
financing event, not a growth story.**

**The claim:** run across the cohort, the build-vs-launch and margin-multiple tests agree;
every Tier 1 name's break-even multiple is computed from its own income statement; and
**no Tier 1 name has a break-even multiple it cannot fund**. The tests are cheaper, less
subjective and reproducible — they read tables, not adjectives.

**Why this priority**: P3 rather than P2 because 001 already furnished the shape of the
answer for one issuer. This pillar's job is to widen a single-issuer finding to a cohort
— valuable, but not the thesis's question.

**Two honest limits, carried in-line.** (a) **DA-13 blocks the ideal test**: production
rate in units is disclosed by **exactly one issuer in the universe** (RKLB). Where units
are absent, the margin-multiple test substitutes and the substitution is recorded per
name. (b) **TER's queue-position finding complicates the inference**: TER's single-year
revenue increase (~$2,100M) approximately equals the combined annual revenue of every
pure-play space company (~$2,170M), and its capacity is allocated by a larger market
that pays more. **A capable supplier does not relieve a constraint if the queue is
longer than the cohort's order book.** Where a Tier 1 manufacturer is queue-limited
rather than demand-limited, that distinction is reported rather than averaged away.

**Independently falsifiable** — two conditions, both mechanical:

**wrong_if**: `metric=share_of_tier1_issuers_accumulating_unlaunched_inventory_across_consecutive_reporting_periods threshold=0.5 source=issuer_disclosed_build_versus_launch_counts_or_inventory_balances op=>`

**wrong_if**: `metric=count_of_tier1_hardware_manufacturers_reporting_negative_gross_margin threshold=0 source=10-Q_income_statement_after_component_recomputation op=>`

**wrong_if** (added at specification review, for the reframed claim): `metric=count_of_tier1_issuers_whose_break_even_revenue_multiple_exceeds_their_disclosed_funding_runway threshold=0 source=10-Q_income_statement_and_liquidity_note op=>`

**Subscribed**: `RKLB × operational-kpi`, `YSS × operational-kpi`, `FLY × operational-kpi`, `VOYG × operational-kpi`, `PL × operational-kpi`, `RKLB × supply-chain`, `YSS × supply-chain`, `KRMN × supply-chain`, `FLY × supply-chain`

---

### Pillar 4 — The three Tier 1 integrations are value-pool migration, not empire-building (Priority: P4)

Three Tier 1 issuers have bought something in the last eighteen months: **RKLB is
acquiring Iridium (~$8B)**, **VOYG acquired Astrobotic (~$300M)**, **YSS acquired
All.Space (~$355M, agreed 2026-04-29)**. All three deals are `CLAIMED`-priced under P4.
The question is not whether they are large — it is whether they are **the same strategic
move**, and whether that move is the one A1b predicts.

**The claim:** all three are **downstream acquisitions into the value pool** —
constellation operations, lunar services, and ground/terminal connectivity respectively
— rather than unrelated diversification. The test is structural, not rhetorical: an
integration is value-pool migration when the target's business lies in **services,
operations or constellation capacity**, which A1b identifies as where value went. It is
empire-building when the acquirer funds it from a deteriorating operating position with
cash or debt rather than equity — buying growth it cannot yet afford with money it does
not yet generate.

**Why this priority**: P4 because it is a *characterisation* of three discrete events,
not a property of the cohort. It becomes decisive only if one of the three deals breaks
— at which point P11 requires a from-scratch re-underwrite of the acquirer. The
value-pool definition used to test the targets is fixed once in §1c and not restated.

**Independently falsifiable**: any Tier 1 acquirer with negative operating cash flow
funding a majority cash-or-debt acquisition. That is the empire-building signature — a
pre-profit buyer levering a narrative rather than acquiring a cash-generative pool.

**wrong_if**: `metric=count_of_tier1_acquirers_with_negative_operating_cash_flow_funding_a_majority_cash_or_debt_acquisition threshold=0 source=10-Q_cash_flow_statement_and_8-K_merger_consideration_disclosure op=>`

**Subscribed**: `RKLB × business-model`, `VOYG × business-model`, `YSS × business-model`, `RKLB × what-if`, `VOYG × what-if`, `YSS × what-if`

---

### Pillar 5 — The space-grade solar-cell duopoly is structural, unpriced, and carries no *demonstrated* pricing power (Priority: P5)

Two suppliers — **SolAero (RKLB)** and **Spectrolab (BA)** — serve a component every
satellite requires, and cell efficiency is the **first term in constitution bound F1's**
array-area chain. One leg of the duopoly is owned by a launch competitor of the other
leg's customers. **This is a genuine structural finding, and it is priced zero times**:
neither parent discloses the unit, and both parents' financials are dominated by other
business — BA at a **0.6%** operating margin and RKLB loss-making.

**The claim:** the duopoly's pricing power is **unquantifiable from public filings**, and
that is the finding — a constraint that is real, load-bearing for every constellation
plan in the sector, and **structurally invisible** to the disclosure granularity the
platform carries. Neither leg shows elevated consolidated margin, which is either
evidence the scarcity is small relative to the parents, or evidence the demand that
would make it bite has not arrived.

**Why this priority**: P5 because its most likely correct output is a *disposition* —
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — not a valuation. It is retained rather than dropped
because P4 forbids dropping it silently, and because its negative result is informative
for F1 and for 008's supply-chain map.

**Ownership boundary.** The BA/Spectrolab leg belongs to **007**. 005 owns the **RKLB**
leg, where the question is live because RKLB is the acquirer and would carry the
duopoly rent inside its own Space Systems segment. **No proxy is substituted** for the
Spectrolab leg; the gap is recorded.

**Independently falsifiable**: any universe filing or transcript that discloses a
space-grade solar-cell unit revenue, price, capacity or backlog figure — which would
convert the pillar from an unpriced structural finding into a priced one.

**wrong_if**: `metric=count_of_disclosed_space_grade_solar_cell_unit_revenue_price_capacity_or_backlog_figures_in_universe_filings threshold=0 source=10-K_10-Q_or_earnings_call_transcript op=>`

**Subscribed**: `RKLB × supply-chain`, `YSS × supply-chain`, `KRMN × supply-chain`, `RKLB × operational-kpi`

---

### Pillar 6 — RKLB/Iridium is modellable as a combined entity, carries a dated consent catalyst inside 180 days, and is sized at the 2% binary cap (Priority: P6)

**P11 is explicit that the acquirer is the harder case.** RKLB is a deal security *as
acquirer*, so this thesis must **model the combined entity including deal financing and
dilution — the $3.6B bridge facility and the stock consideration — and treat the close
date as the dated catalyst.** Pro-forma combined financials are **not disclosed**, so the
combined-entity model is `MODELED` by construction and can never satisfy a falsifier
under P4. That is stated, not hidden.

**The claim:** the combined entity can be modelled from disclosed inputs; the
transaction's binding constraint is `REGULATORY_SPECTRUM` per P11, not financing; and at
least one **required consent carries a dated milestone inside the 180-day catalyst
window**, so the position has a datable catalyst even though the close itself (expected
mid-2027) does not. 001 already established that RKLB's Iridium risk factors name
**FCC, ITU and DCSA** as required consents — the consent set exists and is named; what
P6 adds is the date.

**Why this priority**: last because it is the most conditional output in the thesis — a
single-name, single-deal model whose usefulness depends on P1 clearing RKLB's runway
first. It is present at all because **P11 makes it mandatory**, not optional.

**Sizing, stated plainly.** The RKLB deal position is a **binary catalyst** and sizes at
the **2% cap**, not the 4% default. Under the multi-constraint declaration in §1, Tier 1
carries **at most 3 positions** and at most **2 in any sub-sector**; RKLB and FLY both
map to Launch Services & Reusable Transport, so **at most one of them can be held**
alongside a third Tier 1 name. On a break, P11 requires a from-scratch re-underwrite:
the standalone case is not the pre-announcement case.

**A model caveat that must travel with the output.** RKLB is loss-making, so any
pro-forma leverage ratio has a sign-sensitive denominator. The pro-forma net-debt test
is reported as a **stated bar of 6.0×** (see Clarifications Q-2) — it is a spec-set bar,
not a measurement — and the model must show the component arithmetic in-line per P4.

**Independently falsifiable**: any required consent for the RKLB/Iridium close that
carries neither a clearance nor a dated milestone inside 180 days — which would leave
the position with no datable catalyst and no P9-compliant entry.

**wrong_if**: `metric=count_of_required_regulatory_consents_for_rklb_iridium_without_a_clearance_or_dated_milestone_within_180_days threshold=0 source=8-K_10-Q_risk_factors_and_HSR_CFIUS_FCC_ITU_DCSA_filings op=>`

**Subscribed**: `RKLB × recent-quarter`, `RKLB × risk`, `RKLB × what-if`, `RKLB × ratio-analysis`, `RKLB × unit-economics`

---

> **Delivering P1 alone yields a defensible partial conclusion** — the Tier 1 cohort
> splits into names that can fund themselves to profitability and names that cannot, on
> disclosed cash and disclosed burn. That is the single most valuable output of this
> thesis, it is delivered first, and it is the only pillar whose answer does not depend
> on another pillar's answer.

## 1c. Method — the cross-sectional instruments

This is a **cross-sectional comparison, not eight per-name deep dives.** Depth is
allocated to the four names that carry the pillars (RKLB, YSS, FLY, VOYG) and the other
five are read at the depth needed to place them in the ranking. Three instruments are
specific to this thesis:

1. **The build-vs-launch behavioural test.** For every issuer disclosing both counts,
   accumulated inventory is computed period by period. Drawdown means demand- or
   production-limited; accumulation means launch-limited. **This is a behavioural
   measure and requires no prose coding** — it is the replacement 001 proposed for
   PIL-3's 19-document risk-factor read, and it is the reason P3 is affordable.
2. **The margin-multiple test.** Fixed costs ÷ gross profit, from the income statement.
   Above 1.0×, the issuer is volume-constrained by arithmetic. YSS at **2.9×** is the
   worked example; the cohort is ranked on it. Where a name reports negative gross
   margin, the multiple is undefined and the name reports under the **second** P3
   falsifier instead.
3. **The value-pool classification.** Every issuer's revenue is allocated to hardware
   versus services/operations/constellation capacity, using **each issuer's own segment
   definitions** (DA-21), with the allocation stated per name. The cohort is then ranked
   by distance from the hardware end. **This instrument produces P2's answer and P4's
   target test from the same classification**, which is why the definitions are fixed in
   §1b.

**Evidence discipline.** Per P4 and the v1.3.0 Data-Integrity Register, no artifact in
this thesis reads `operating_income` without showing `gross profit − opex` in-line.
**`EPS × shares` is not a sign test** — it passes spuriously on flipped issuers at RKLB,
FLY and VOYG — and its use is a defect, not a shortcut. Where the component identity
cannot run (LUNR has no quarterly gross-profit line; HAWK's share counts do not
reconcile), the artifact says so and uses the weaker margin-plausibility detector, named
as such. **DA-26 (annual figures mislabelled as quarterly) and DA-27 (fiscal-period
labels derived from the calendar quarter) both apply to this cohort** — PL (January
year-end), KRMN, VOYG and YSS each straddle a fiscal boundary, so every quarterly series
built here is reconciled against the annual before use.

**Correction policy.** Where this thesis contradicts a 001 figure, 001's files are
**frozen**. The correction is recorded here and cited by location — matching 001's own
annotate-don't-rewrite policy.

## 2. Universe Definition

The eight researchable Tier 1 pure-plays, plus one conditional name. Weights are
**analytical effort, not positions** — the position cap is fixed by the Concentration
Rule and the multi-constraint declaration in §1, not by this table. **Market Data Stage
is `none` across the cohort**: every conclusion here is drawn from filings, not prices.
Deal values are `CLAIMED` under P4.

| Ticker | Company | Sector | Sub-sector (Sector Preferences) | Weight | Role in this thesis |
|---|---|---|:---:|---|
| RKLB | Rocket Lab | industrial.aerospace_defense | Launch Services & Reusable Transport | 20% | **Largest surface.** The only demonstrated launch unit economics in the universe (basis B $14,667/kg); the only issuer disclosing build-vs-launch counts; **P11 acquirer** of Iridium (~$8B) carrying the $3.6B bridge — **P3, P4, P5, P6** all land here |
| YSS | York Space Systems | industrial.aerospace_defense | Space Infrastructure & Components | 16% | **The cleanest manufacturing read and the cohort's diagnostic case**: 24.0% gross margin against a 68.6% opex ratio and a **2.9×** fixed-cost multiple — **P3**. Also carries the unresolved **$110.466M** Q1 operating figure, and revenue **−20.5% QoQ** that cuts against the volume reading |
| FLY | Firefly Aerospace | industrial.aerospace_defense | Launch Services & Reusable Transport | 13% | Weakest gross margin of the three manufacturers (**20.3%**) with the highest R&D intensity (**60.8%**) and the largest operating loss (**$(95.2)M**) — **P1, P3**. An **emerging growth company**, a structural disclosure-quality variable |
| VOYG | Voyager Technologies | industrial.aerospace_defense | **unmapped** — provisional Space Infrastructure & Components | 12% | Starlab space station plus defense; acquired Astrobotic (~$300M) — **P4**. Its reported operating line fails the gross-profit bound by **$46,951M** across three quarters, so **P1** runs on non-operating lines here |
| LUNR | Intuitive Machines | industrial.aerospace_defense | **unmapped** — no lunar-services line exists | 10% | Lunar landers and services; **the purest services model in the cohort** and the second-largest payer to the value pool — **P2**. DA-23 candidate at a **42.1%** Q4 2025 operating margin with the component identity unavailable |
| PL | Planet Labs | industrial.aerospace_defense | Earth Observation & Geospatial | 10% | The constitution's **only Underweight / Low** space sub-sector; best gross margin in the universe at **53.5%** and still **−37%** at the operating line — **P2**'s hardest test case |
| KRMN | Karman Holdings | industrial.aerospace_defense | Space Infrastructure & Components | 9% | Missile/space/defense components — a **hardware model with supplier economics**. Capital structure absorbs **60%** of operating income — **P1, P4**. Primary depth belongs to **008**; 005 reads it as the cohort's hardware pole |
| HAWK | HawkEye 360 | industrial.aerospace_defense | **unmapped** — space-based SIGINT has no line | 6% | RF geolocation and signals intelligence — a **data-services** model, the clearest contrast to the hardware pole — **P2**. Extract inconsistent three independent ways (DA-28 candidate) |
| BKSY | BlackSky | **unassigned — `PARTIAL`** | Earth Observation & Geospatial | 4% | **Conditional.** Enters only on manual sector assignment per PROGRAM §7. If the assignment is not made, this row is **dropped, not proxied** |
| **Sum** | | | | **100%** | |

**Named but not researchable — recorded, not proxied.** **RDW** (Redwire), **SPIR**
(Spire Global) and **SPCE** (Virgin Galactic) are `NOT_READY`: zero XBRL facts, zero
source documents, nothing but an institutional-holdings stub dated 2025-12-31. They
**cannot host a thesis** under the Evidence and Anti-Drift Rules. Their absence is
recorded as a **coverage gap**, and it is a real one: RDW is a deployable-structures and
in-space-manufacturing supplier whose economics would inform P2's hardware pole, and SPIR
is a second space-data-services model that would strengthen P2's comparison. **No proxy
is substituted for any of the three.** Re-check before wave 2.

**Sub-sector mapping is itself a deliverable.** Three of nine names (VOYG, LUNR, HAWK)
**do not map onto a Sector Preferences sub-sector without inventing one** — the table has
no space-station, lunar-services or space-SIGINT line. The mapping above is
**provisional**, and it is required work rather than bookkeeping, because the
**Concentration Rule is defined by sub-sector** and cannot be evaluated without it. Under
the provisional map, **Space Infrastructure & Components would hold three names
(YSS, KRMN, VOYG) against a 2-position sub-sector cap** — and **five (adding LUNR and
HAWK) if the unmapped names are forced onto the nearest available line**. Either way that
cap, not the 3-position Tier 1 cap, is the binding constraint on the cohort. Flagged in
Clarifications Q-4.

**Excluded by adjacency:** **JOBY** and **ACHR** are READY and appear in space thematic
funds, but they operate in the atmosphere. Excluded by the constitution's Research Scope
Constraints; read-through only, and not into this thesis.

## 3. Skill Deployment Matrix

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|:---:|---|:---:|---|
| operational-kpi | business-intelligence | Deep | RKLB, YSS, FLY, VOYG, PL | none | Build-vs-launch counts, inventory balances, and the margin-multiple inputs — **P3**'s two instruments. PL is here because its **1.69×** break-even multiple is the universe's sharpest instance of the reframed claim |
| unit-economics | business-intelligence | Deep | RKLB, YSS, FLY | none | Gross margin, R&D intensity, fixed-cost-to-gross-profit multiple per name; DA-25's two readings side by side — **P2, P3** |
| business-model | equity-research-core | Standard | RKLB, VOYG, YSS, KRMN, HAWK | none | The value-pool classification (hardware vs services/operations/constellation) and each acquirer's stated integration rationale — **P2, P4** |
| competitive | equity-research-core | Standard | PL, BKSY, HAWK, LUNR | none | EO and SIGINT competitive structure, and the lunar-services field now consolidating into VOYG — does the constitution's Underweight/Low EO call survive contact with the cohort? — **P2, P4** |
| risk | equity-research-core | Standard | RKLB, VOYG, LUNR, FLY | none | Cash runway, going-concern language, committed facilities, and the Iridium consent set — **P1, P6** |
| recent-quarter | equity-research-core | Standard | RKLB, FLY, LUNR, PL, KRMN, VOYG, YSS, HAWK, BKSY | none | The DA-23/DA-24/DA-26/DA-27 read on every Tier 1 issuer-quarter; the **validation queue** is built here — **P1, P6** |
| peer-bench | quantitative-analysis | Standard | RKLB, FLY, YSS, KRMN, LUNR | none | The cross-sectional rank itself — the instrument that makes a cohort claim more than eight anecdotes — **P2** |
| ratio-analysis | quantitative-analysis | Standard | RKLB, FLY, YSS, VOYG, LUNR, KRMN | none | Runway, leverage and margin ratios on component-verified inputs; the below-the-line bridge shown in-line — **P1** |
| sector-overview | equity-research-core | Light | RKLB, YSS, PL, KRMN | none | Sub-sector mapping for the Concentration Rule, and the EO sub-sector's structural case — **P2** |
| secular-trends | equity-research-core | Light | PL, LUNR, VOYG | none | Demand-pool direction for EO, lunar services and commercial stations — **P2** |
| supply-chain | industry-analysis | Light | YSS, KRMN, RKLB, FLY | none | What these manufacturers buy — solar cells, engines, components — and where the queue is longer than the order book — **P3, P5** |
| what-if | quantitative-analysis | Light | RKLB, VOYG, YSS | none | Combined-entity and pro-forma scenarios; the integration counterfactuals — **P4, P6** |

> **Coverage invariant.** Every ticker in §2 appears at least once above; every
> `Subscribed` pair in §1b generates at least one task; every matrix skill is named in at
> least one `Subscribed` line. Verified by `tools/plan_audit.py` (I1–I4).

## 4. Depth Tiers

| Tier | Skills | mode-set | Tickers | Output |
|:---:|------|---|--------|------|
| Deep | operational-kpi, unit-economics, business-model | all modes | RKLB, YSS, FLY, VOYG, **and PL on `operational-kpi` only** | Full-mode work on the four names carrying P3, P4, P5 and P6, plus PL's break-even inputs (the reframed P3 claim) |
| Standard | recent-quarter, ratio-analysis, risk, peer-bench, competitive | essentials_modes | As listed | The cohort read, the rank, the runway computation, the competitive placement |
| Light | sector-overview, secular-trends, supply-chain, what-if | essentials_modes | As listed | Scoping checks that bound the above |

**Budget note.** **Nine names; the matrix yields 55 distinct `(ticker, skill)`
analyses**, expanding to roughly **65 mode-tasks**. That
is materially more per name than 002's ~34 across twelve, because 002 was a validation
pass and this is segment research. **`thesis.md` currently carries a placeholder budget
of 40; this spec requires it raised to 70 at plan time** — recorded as a precondition,
not assumed. If the budget must come down, drop the Light rows first; never the Deep
rows, which carry P3, P4 and P6, and never the `recent-quarter` row, which is the entire
delivery mechanism for the validation queue.

## 5. Cross-Cutting Analysis

- **The ranked cross-section** is the primary output: every researchable Tier 1 name,
  its value-pool distance, its runway in months, its fixed-cost multiple, and its
  provisional single binding constraint — one table, eight rows, every cell traceable to
  a filing.
- **The constraint map** is the second output, and it is how the P3 compromise is
  discharged: **one permitted constraint value per name**, evidenced. Provisional:
  **`MANUFACTURING_RATE`** for YSS, PL and KRMN — 001's register already codes the
  constellation-economics line this way on the measured break-even multiple (**PL 1.69×,
  YSS 2.86×**), and it is the value P3's own title asserts. **The remedy direction is
  `DEMAND`** (a volume problem yields only to order order flow), which is why the two
  readings sit adjacent rather than in conflict: `MANUFACTURING_RATE` is the **evidenced
  constraint**, `DEMAND` is the **remedy**. **`DEMAND`** for LUNR, where no break-even
  multiple has been computed yet; **`CAPITAL`** for FLY, VOYG, HAWK and RKLB's standalone
  business. **RKLB carries two constraint values because it contains two decisions** —
  `CAPITAL` for the standalone business and `REGULATORY_SPECTRUM` for the deal leg, which
  is the value P11 assigns to deal securities. That split is the resolution of the
  multi-constraint problem: **one constraint per decision, not per ticker.**
- **Macro sensitivity: high, and it is concentrated in P1.** These are pre-profit,
  long-duration issuers in a NEUTRAL-bias regime with the 10Y at **4.80%** and a market
  pricing hike risk. The constitution's own re-rate trigger — a 10Y break above **5.25%**
  — deepens caution on exactly this cohort, because it moves the financing cost of every
  externally dependent name in the runway table. The sector preference is **Overweight /
  High** on Launch Services, which is a *sector* call this thesis tests at the
  *cohort* level rather than assumes.
- **Constitution interaction**: **P3** — declared multi, discharged per name (§1).
  **P11** — RKLB is a deal security; model the combined entity, size at 2%, re-underwrite
  on a break. **Risk Framework** — the **Concentration Rule** binds hard here: the cohort
  cannot be traded as a basket, and its 6% ceiling is set in §1, not chosen here.
  **A1a/A1b** — A1a is settled and inherited; **A1b is the organising fact**, not a pillar
  to re-prove. **P4 / Data-Integrity Register** — DA-23, DA-25, DA-26 and DA-27 all bind
  this cohort directly; `EPS × shares` is inadmissible as a sign test.
- **Pair-trade candidates: none admissible.** The cohort shares one factor — the theme —
  and the Concentration Rule caps Tier 1 at three positions with two per sub-sector, so a
  relative-value pair would consume the entire allowance to express a single spread. The
  relative call belongs in 011, where the theme cap (40% of NAV) binds before the
  sub-sector cap (25%).
- **Deliberate non-outputs**: no DCF. Per the Methodology Foundation, DCF is admissible
  only where an issuer has three years of positive free cash flow or a contracted backlog
  covering the forecast period — most of this cohort fails the first condition, and
  comps are a cross-check only for a pre-profit issuer. **This thesis ranks; it does not
  value.**

## 6. Output Contract

- **Per-ticker (dispatcher-resumable)**: `artifacts/{ticker}/{YYYY-MM-DD}_{skill}_{mode}.md`
  — the suffix **must** be `_{skill}_{mode}.md` with the real mode slug, so
  `dispatch.resume_verdict()` can find it.
- **Cross-cutting (not resume-tracked)**: `_cross/{name}.md`.
- **Primary artifact**: `_cross/tier1-value-capture-ranking.md` — the ranked cross-section
  with the value-pool classification, runway months, fixed-cost multiple and provisional
  constraint per name. **This is what 008, 009 and 011 cite.**
- **Second artifact**: `_cross/tier1-constraint-map.md` — the per-name single-constraint
  assignment with evidence, which is what discharges the P3 compromise.
- Snapshot: `snapshots/005-tier1-space-pure-plays/{YYYY-MM-DD}_thesis.md`
- **Frontmatter**: per `contracts/artifact-frontmatter.yaml`, with `thesis_id:
  "005-tier1-space-pure-plays"`. All five pins are mandatory: `constitution_pin: 1.4.0`,
  `assumption_pin: "2"`, `skill_pin`, `as_of`, `corpus_version`.

## 7. Thesis Phases

| Phase | Tasks | Duration | Dependencies |
|:---:|------|---|------|
| 1 — Runway and capital structure (**P1**) | Cash, disclosed burn and committed facilities for all nine names; runway in months; the self-funding / externally-dependent split | Week 1 | Constitution v1.3.0 loaded; 002's DA-23 census at least partial |
| 2 — Value capture (**P2**) | Value-pool classification per issuer (DA-21, own segment definitions); the hardware share of Tier 1 aggregate revenue; the EO sub-sector test | Week 2 | Phase 1 |
| 3 — Manufacturing rate (**P3**) | Build-vs-launch series for every discloser; margin-multiple ranking; the queue-position carve-out | Week 3 | Phase 2 |
| 4 — Integrations (**P4**) | The three targets classified against the value pool; consideration mix and acquirer operating cash flow; the financing test | Week 4 | Phase 3 |
| 5 — Solar-cell duopoly (**P5**) | The disclosure search across all universe filings and transcripts; record the gap or convert the pillar | Week 4 | Phase 3 |
| 6 — RKLB/Iridium (**P6**) | Combined-entity model including the $3.6B bridge and stock consideration; the consent set and its dated milestones; the 2% sizing | Week 5 | Phase 4 |
| 7 — Rank and hand-off | Publish the ranking and the constraint map; record what could not be resolved; hand the cohort to 011 | Week 6 | Phase 6 |

## Clarifications

Recorded by `agentii.specify` at creation, 2026-09-18. No `agentii.clarify` round has
run; the following are recorded as open for that pass.

- **Q-1 (P3, the declared compromise)** — Is the per-name constraint map an acceptable
  discharge of P3, or does a multi-constraint thesis require an explicit exemption
  recorded against the constitution? **Provisional:** the map discharges it, because P3's
  purpose is to prevent sizing against several constraints relaxing at once, and every
  sizing decision here is taken on a single named constraint. **If answered differently
  this is a PATCH to spec, not a MAJOR event.**
- **Q-2 (P6, the 6.0× pro-forma bar)** — The pro-forma net-debt-to-gross-profit bar is
  **set at 6.0× as a specification threshold, not derived from any measurement**, and
  RKLB's loss-making status makes any leverage denominator sign-sensitive. **Flagged for
  human confirmation.** The pillar's falsifier does **not** rest on this bar — it rests on
  the consent-date test, which is mechanical.
- **Q-3 (P1, the 24-month bar)** — 24 months of runway was chosen as the point at which a
  pre-profit issuer can plausibly reach a financing window rather than be forced into
  one. It is a **spec-set bar**, not a measured quantity. **Flagged for human
  confirmation.**
- **Q-4 (all pillars, the sub-sector mapping)** — Three names (VOYG, LUNR, HAWK) have no
  Sector Preferences line, and the **Concentration Rule cannot evaluate without a
  sub-sector**. Should the mapping be provisional-per-thesis as written here, or does it
  require a constitution amendment to add the missing lines? **Provisional:** provisional
  per thesis, with the gap recorded — because the amendment route would block this
  thesis on a SemVer event.
- **Q-5 (P2, the 0.5 hardware-share threshold)** — The majority test was chosen as the
  point at which the cohort stops being described by hardware. It is **stated, not
  measured.** **Flagged for human confirmation.**
- **Q-6 (P6, the entity boundary)** — Should the combined RKLB/Iridium entity be carried
  as **one name** in this cohort, or should RKLB be read pre-merger and IRDM read
  separately in 006? **Provisional:** one name, modelled combined per P11, with all
  operational metrics tagged **pre-merger basis** — because the analyst cannot hold the
  two halves of the same entity as separate positions, and pricing them separately would
  double-count the same cash flows.
