# Research Thesis: 004 — Tier 0: SpaceX Anchor, SOTP across Space / Connectivity / AI

**Constitution Ref**: constitution.md v1.4.0 (`constitution_pin: 1.4.0`)
**Created**: 2026-09-18
**Status**: Active
**Time Horizon**: 2026-Q4, terminating at the wave-1 hand-off to 005–006
**Depends on**: `001-technology-baseline` (pin 1.2.0 — the artifacts this thesis values), `002-evidence-validation` (the validated input set; where 002 has not landed, 004 inherits 001's grades unchanged and says so)
**Binding constraint**: `CAPITAL` (PROGRAM §2). See Clarification Q-4 — named against the `POWER` reading, deliberately.
**Produces**: the **anchor valuation** — three segment multiple regimes with stated comparability boundaries and grades. **No trade ideas**: sizing is 011's.

---

## 0. Inherited baseline — what this thesis does NOT re-derive

001 established the following and this thesis **takes them as given**. 001 ran `operational-kpi`
and `unit-economics` on SPCX and produced **throughput** (mass to orbit, launches, subscribers,
ARPU, nameplate draw) and **cost** ($/kg). **It produced no valuation.** That gap is this thesis.

**Path shorthand used throughout this table — declared, not implied.** Paths are real and
relative to *this spec's directory*; `001/` expands to `../001-technology-baseline/`, and the
mid-path `…` expands to `artifacts/SPCX/`. Every row therefore resolves to a file on disk —
e.g. row 2 reads `../001-technology-baseline/artifacts/SPCX/2026-09-18_1239_operational-kpi_methodology.md`.
Except for row 1, which names both artifacts because the three-segment frame is a claim about the
whole SPCX corpus. The two `2310` artifacts are post-10-Q reads and **supersede the `1239` pair**
where they overlap — 001 recorded that supersession in its own status log and did not rewrite
the earlier files.

| Inherited result | 001 artifact | Grade |
|---|---|---|
| SPCX reports **THREE** segments as of Q2 2026 — Space, Connectivity, AI — and the frame **supersedes every prior two-segment SPCX artifact** | `001/artifacts/SPCX/2026-09-18_2310_business-model_methodology.md` §2, §4 | `DEMONSTRATED` |
| **Space**: revenue **$962M** (+29.0%), cost of revenue **$329M** (−0.3%), R&D **$1,076M** (+55.3%) = **3.3× cost of revenue**, SG&A $99M, total costs **$1,504M**, operating loss **$(542)M widening +46.9%** | `001/…/2026-09-18_1239_operational-kpi_methodology.md`; refined in `…_2310_operational-kpi_methodology.md` §2 | `DEMONSTRATED` |
| Space earns a **65.8% gross margin** (gross profit $633M) and the loss is **Starship development R&D**, not launch economics — cost of revenue was *flat* while revenue rose 29% | `001/…/2026-09-18_2310_operational-kpi_methodology.md` §2 | `DEMONSTRATED` |
| **Connectivity**: revenue **$4,291M** (+65.8%), operating income **$1,656M** (+79.4%), subscribers **12.0M** (+101.2%), ARPU **$66/mo vs $85/mo (−22.4%)** | `001/…/2026-09-18_1239_operational-kpi_methodology.md`; `…_2310_operational-kpi_methodology.md` §4 | `DEMONSTRATED` |
| Connectivity is the **only segment with demonstrated operating leverage in the 35-name universe**; segment gross margin **52.0%**; **enterprise/government outgrew consumer** (+$939M vs +$764M) | `001/…/2026-09-18_1239_operational-kpi_methodology.md`; `…_2310_operational-kpi_methodology.md` §4 | `DEMONSTRATED` |
| **AI**: revenue **$2,561M** (+247.5%), operating loss **$(1,257)M** narrowing −17.5%, **nameplate compute draw 1.4 GW vs 0.4 GW (+250%)** | `001/…/2026-09-18_2310_operational-kpi_methodology.md` §2 (revised) | **`DERIVED`, not disclosed** — see V-1 resolution below. |
| **DA-23 at consolidation**: Space −542 + AI −1,257 + Connectivity +1,656 = **−143 operating LOSS**, while `get_company_financials` returns `OperatingIncomeLoss: +143,000,000` | `001/…/2026-09-18_1239_operational-kpi_methodology.md` §segment reconciliation; `…_1239_unit-economics_methodology.md` data-quality note | `DEMONSTRATED` |
| **DA-11**: the 1.4 GW is **IT load only** — explicitly excluding cooling, power distribution losses, lighting, security, facility overhead. True facility draw typically **1.2–1.5×**. Called *"the most dangerous figure in this thesis"* | `001/…/2026-09-18_1239_operational-kpi_methodology.md` §AI | `DEMONSTRATED` (the definition). **The restatement is 002's — not re-derived here.** |
| **A4 boundary**: the AI segment is **ground-based**. SPCX's separate filing for up to **1 million satellites at 100 kW of compute per tonne** is a **filed aspiration with no revenue line**, inadmissible as a valuation input | `001/…/2026-09-18_1239_operational-kpi_methodology.md`; constitution §0 A4 and §P10 | `CLAIMED` |
| **Mass to orbit 485 t vs 652 t (−25.6%)** while revenue rose +91.9%; customer payload **flat at 87 t vs 88 t**; Falcon launches 37 vs 45 (−17.8%); only **10 of 37** count as customer launches; internal 27 (−25.0%); Starship 3 → 1 across H1 | `001/…/2026-09-18_2310_operational-kpi_methodology.md` §1 | `DEMONSTRATED` |
| **A1b falsified on SPCX's own metrics** — revenue +91.9% with Falcon launches −18% and Space up only +29.0% | `001/…/2026-09-18_2310_operational-kpi_methodology.md` §1; constitution §0 A1b | `DEMONSTRATED` |
| **Capital**: H1 2026 operating CF **+$3,466M**, investing **$(34,487)M**, financing **+$100,291M**; IPO net proceeds **$85,675M** (638.9M shares at $135.00); **$40,869M** notes at a 6.03% effective rate; **$856M** EchoStar spectrum instalments | `001/…/2026-09-18_2310_operational-kpi_methodology.md` §5 | `DEMONSTRATED` |
| **Entity discontinuity**: X merger 2025-03-28, xAI merger **2026-02-02 (common control)**, IPO 2026-06, five-for-one split 2026-05, **Cursor $60B all-stock pending Q3 2026** — *"the single largest statement-level discontinuity in the universe"* | `001/…/2026-09-18_2310_business-model_methodology.md` §1 | `DEMONSTRATED` |
| **Segment revenue shares**: Connectivity **54.9%**, AI **32.8%**, Space **12.3%**; consolidated **$7,814M**; H1 Space **$1,581M vs $1,611M (−1.9%)** while H1 total rose +53.7% | `001/…/2026-09-18_2310_business-model_methodology.md` §2 | `DEMONSTRATED` |
| **DA-01 bases** — A ~$2,939/kg, A′ ~$4,220/kg, B ~$525–875/kg, C ~$6,596/kg: a **7–13× spread** round one Falcon mission; the **22.8 t denominator is `CLAIMED`** | `001/…/2026-09-18_1239_unit-economics_methodology.md`; `…_1239_operational-kpi_methodology.md` | `DEMONSTRATED` (A′, C figures) / `MODELED` (B) / `CLAIMED` (denominator) |
| **Market-cap anchor ~$1.62T** (SPCX anchors the top of the market-cap screen) | `constitution.md` §Research Scope Constraints | `CLAIMED` — a dated print, not a live one. **Market Data Stage is `none`.** |

**What 001 did not do:** convert throughput and cost into **value**. Every figure above is a
quantity, a price or a cost. None is a multiple, a segment value, or a discount. That is this
thesis's entire scope — and it is why 004 is the anchor rather than another segment thesis.

### Validation queue — segment attribution and valuation inputs

**Scope boundary, stated first.** `002-evidence-validation` owns **denominator and physics**
validation: the three `CLAIMED` payload masses (002 P1), F2's two unsourced constants (002 P2),
the universe-wide DA-23 census (002 P3) and the DA-11 PUE restatement (002 P4). **004 does not
re-derive any of them.** 004's queue is the one 002 does not carry: **whether the segment
attribution is real, and whether the valuation inputs are admissible.** Where 002 has not yet
landed, 004 inherits 001's grade unchanged and labels it.

| # | Item | Why it gates a pillar | Resolving source |
|---|---|---|---|
| **V-1** ✅ **RESOLVED at specification review** | **Does the AI segment file an operating result at all?** **It does not — the line is `DERIVED`, not disclosed.** The two 001 artifacts do not contradict; they describe different things. `2310_operational-kpi` §2 (newer, superseding) records the AI operating line as *"not disclosed"*; `1239` §AI's **$(1,257)M** is recoverable **by subtraction** — consolidated **$(143)M** − Connectivity **$1,656M** − Space **$(542)M** = **$(1,257)M**. | **The MDV survives, but its basis changes and must be stated.** P1's separability test remains **3 of 3 segments have determinable operating results — but only 2 of 3 are *disclosed*.** The DA-23 segment sum is an **identity, not an independent check**: it cannot corroborate itself, so the consolidated `OperatingIncomeLoss: +143,000,000` sign flip is what DA-23 tests, and the segment arithmetic inherits that sign rather than confirming it. **Consequence for P3:** the AI segment's value must be carried on revenue and capex, never on a derived operating margin presented as filed. | Resolved — recorded here; 10-Q note `0001628280-26-052535` remains the confirming source |
| **V-2** | **Segment-to-consolidated reconciliation residual.** `value-checks.yaml` carries `segments_sum_to_total` at **`fail`** level | A non-zero residual means the SOTP denominator is broken before the first multiple is applied | 10-Q segment note; show the residual in-line |
| **V-3** | **Is the AI segment homogeneous enough to carry one multiple?** It aggregates **Grok, X (advertising) and compute** — DA-21 (issuer-defined segment boundaries) in operation | A multiple applied to a segment mixing advertising with compute infrastructure is not a multiple | Note 1 and Note 3, segment definitions |
| **V-4** | **Does the Space series survive the entity boundary?** Common-control recast (DA-19) means growth rates across 2025-03-28 / 2026-02-02 mix real growth with entity change. 001 found **Space is the one series that survives** | The SOTP's growth inputs for Connectivity and AI are contaminated; Space's are not | 10-Q MD&A, `2310_business-model` §1 |
| **V-5** | **Cursor treatment under P11.** A **$60B all-stock** acquisition by a loss-making issuer, closing Q3 2026, dilution not determinable | The SOTP cannot be both pre-close and pro-forma. One must be named as the headline basis | Clarification Q-6; 10-Q subsequent-events note |
| **V-6** | **Price-input datability.** Market Data Stage `none` → no live price | The discount measure is **as-of a named print**, never live; the print and its date travel with every quoted figure | `$135.00` IPO price (2026-06); constitution's **~$1.62T** anchor |
| **V-7** | **Backlog quantification for the DCF admissibility test.** Note 3 discloses `concentration of risk` naming **Customer A and Customer B**; the extract does not carry the percentages | The DCF's *backlog limb* cannot be evaluated without it, and the Space segment is the only place the limb could pass | Note 3; bounded read, as 001 recorded |

> **Under P4, an unvalidated number is a pillar that cannot fire.** V-1 and V-2 are
> `blocking` — P1 cannot be delivered without them. V-3 … V-7 are `warn` and are reported
> as bounds rather than resolved to a point, per the §1c standing rule.

---

## 1. Research Question

**What is SPCX worth as three separate businesses — Space, Connectivity, AI — and does the
market price it as one?**

The constitution makes **scenario-weighted sum-of-the-parts primary for multi-segment issuers
precisely because SPCX's three segments are three different businesses with three different
multiples.** SPCX is the cleanest case the rule was written for: a 65.8%-gross-margin launch
business that loses money on development R&D, a 38.6%-operating-margin broadband operator that
is 54.9% of revenue, and a 247%-growth terrestrial compute business that is the largest single
contributor to consolidated growth. Valuing those three at one blended multiple is not a
simplification. It is a different claim, and the spread between the two is the finding.

This thesis therefore answers the question the constitution already told us to ask, and it
answers it in the register the constitution requires: **three multiple regimes, each with a
stated comparability boundary and a grade, scenario-weighted, and reconciled against a dated
market print.**

### Why this thesis exists at all

001 could have been extended with a valuation. It was not, and the reason is structural rather
than stylistic. Three specific facts make the SOTP the only admissible method — and each is a
finding in its own right:

1. **A consolidated earnings multiple is not available.** SPCX's DA-23-corrected operating
   result is **$(143)M** — a loss. Its H1 2026 free cash flow is deeply negative ($3,466M
   operating against $34,487M investing). Comps on consolidated earnings or on FCF are
   **inadmissible, not merely unattractive** — the constitution bars treating comps as primary
   for a pre-profit issuer, and at the consolidated line SPCX is one.
2. **A consolidated DCF is not admissible either.** SPCX fails the constitution's **≥3 years of
   positive FCF** limb outright, and the backlog limb reaches **only the Space segment** (1–14
   year Launch and Development contracts, themselves unquantified — V-7). Full gate at §1c.
3. **The segments are not arm's-length, and the SOTP must say so.** **27 of 37 Falcon launches
   were internal** (DA-08) and generate **no inter-segment revenue** — the cost is capitalised
   into satellites in PP&E. Space is therefore simultaneously a revenue business, a 12.3% segment
   *and* an unpriced capex input to Connectivity. A sum-of-the-parts on a company with material
   unpriced inter-segment transfers is not wrong, but it is only honest if the transfer is
   stated as a limitation rather than netted away.

---

## 1b. Pillars

### Pillar 1 — The three-segment SOTP is buildable, and the implied conglomerate discount is measurable (Priority: P1) 🎯 Minimum Defensible View

The constitution asserts that SPCX's three segments are three different businesses with three
different multiples. **That assertion is untested.** It requires each segment to carry a
discrete filed revenue line *and* a discrete filed operating result — and it requires the three
to reconcile to the consolidated total, which `value-checks.yaml` already enforces at `fail`
level via `segments_sum_to_total`.

**V-1 makes this pillar live rather than formal.** Two 001 artifacts disagree on whether the AI
segment files an operating result: `1239_operational-kpi` reports **$(1,257)M** and the
DA-23 reconciliation depends on it; `2310_operational-kpi` §2 records *"not disclosed."* If the
latter is right, the SOTP is **two segments plus an unattributable residual**, P1's threshold
cannot be met, and the Minimum Defensible View fails on its first test. This is not a
bookkeeping question — it decides whether SPCX can be decomposed at all.

**The claim:** all **three** segments carry a discrete filed revenue line **and** a discrete
filed operating result, the three reconcile to consolidated within 2%, and a
**scenario-weighted SOTP** built on those three regimes yields a value range that can be
compared against the dated market print to quantify a **conglomerate discount or premium** —
stated as such, with the price date travelling with the number.

**Why this priority**: it is the Minimum Defensible View because it is the only deliverable that
makes 004 an anchor. 005, 006 and 007 all benchmark against it; if the decomposition does not
hold, the anchor degrades to a single blended multiple and **every downstream comparability
statement inherits that coarseness silently**.

**Independently falsifiable**: a segment without a discrete filed revenue line or operating
result — i.e. fewer than three separable businesses.

**wrong_if**: `metric=count_of_spcx_segments_with_a_discrete_filed_revenue_line_and_operating_result threshold=3 source=10-Q_segment_note op=<`

**Subscribed**: `SPCX × sotp-valuation`, `SPCX × business-model`, `SPCX × recent-quarter`, `SPCX × ratio-analysis`, `SPCX × operational-kpi`

**Binding constraint**: *comparability* — not `CAPITAL`. P1 is bounded by whether each segment's
inputs exist and reconcile, which no capital injection repairs.

---

### Pillar 2 — Connectivity is the value, and its operating leverage survives ARPU decay (Priority: P2)

Connectivity is the only segment in the 35-name universe with **demonstrated operating
leverage**: income from operations **+79.4%** on revenue **+65.8%**, at a **38.6% operating
margin** and a 52.0% gross margin. The constitution rates Satellite Connectivity
**OVERWEIGHT / High** on exactly this evidence.

**Against it stands a single number: ARPU fell −22.4% ($85 → $66) while subscribers rose
+101.2%.** Under **DA-10** the decline is genuinely ambiguous — subscriber service revenue only,
excluding enterprise, government, aviation and maritime, with SPCX attributing the fall to
*"international expansion and the addition of lower priced service plans."* **At least part of
the 22.4% is therefore a mix-shift artefact rather than price erosion, and the two readings are
not distinguishable from public disclosure.** That ambiguity is the whole pillar: a mix shift
means volume strategy and durable margin; price erosion means the cheap cohort compresses margin
as it scales.

**The claim:** the operating-leverage case **survives** the ARPU restatement on a
revenue-per-subscriber and margin basis, with **all four DA-10 readings reported side by side**
per the §1c standing rule — so the segment enters the SOTP on a margin that is **stable or
expanding**, not on a margin that is being bought.

**Why this priority**: P2 rather than P1 because it is the SOTP's largest input by value
(54.9% of revenue, and the only segment with positive operating income) but not the
decomposition's precondition. If P1 fails, P2 has nothing to sit inside; if P2 fails, P1 still
delivers a decomposition with a *declining* anchor segment — a worse but valid answer.

**Independently falsifiable**: a Connectivity operating margin that declines year over year on
the component identity, or a subscriber/revenue series in which revenue per subscriber falls
faster than ARPU, which would identify price erosion rather than mix shift.

**wrong_if**: `metric=connectivity_segment_operating_margin_yoy_change_pp threshold=0 source=10-Q_segment_note_component_identity op=<`

**Subscribed**: `SPCX × unit-economics`, `SPCX × operational-kpi`, `SPCX × recent-quarter`, `SPCX × what-if`

**Binding constraint**: `DEMAND` — the segment is bounded by whether the price-volume trade
continues to add contribution, not by any physical or capital limit.

---

### Pillar 3 — The AI segment has no admissible multiple from filed or peer data, and must be carried at cost or as optionality (Priority: P3)

The AI segment is **32.8% of revenue**, the **largest single contributor to consolidated
growth** (+$1,824M), and the **largest recipient of capital allocation**. It is also the segment
with the **weakest valuation basis in the SOTP**, and the reason is constitutional rather than
analytical.

**A4 is explicit:** terrestrial and orbital compute are different businesses and must never be
valued as one; SPCX's AI segment is **ground-based**; the 1-million-satellite /
**100 kW-per-tonne** filing is a *filed aspiration with no revenue line*, **inadmissible as a
valuation input**. **P10 gates orbital compute** on five conditions, none of which SPCX's AI
segment meets — because it is not an orbital-compute business. **DA-11 then removes the
segment's own headline metric from the SOTP entirely**: the 1.4 GW is **IT load**, explicitly
excluding cooling, power distribution, lighting, security and facility overhead, so it is a
**capacity** figure, not a revenue or earnings figure, and it cannot be converted without a
$/kW-revenue assumption that no issuer discloses.

The usual escape — price it off peers — fails on inspection. **MSFT, GOOG and NVDA do not report
a discrete compute-infrastructure segment carrying a comparable multiple**: MSFT's compute sits
inside Intelligent Cloud as a cost centre, GOOG's inside Google Cloud, and NVDA is the silicon
supplier rather than the operator. Each is a read-through, not a comparable.

**The claim:** exactly three framings are evaluated side by side per §1c — **(a)** a terrestrial
compute comparable multiple where one can be bounded, **(b)** **invested capital**, using the
H1 2026 capex attributed *"first to the build out of DATA CENTERS and related infrastructure,"*
and **(c)** **optionality at a stated value, including zero** — and the SOTP headline names
**which one it uses**. At least one framing must be admissible from filed data; a segment carried
at zero is a legitimate output, but it must be *stated*, never implied.

**Why this priority**: P3 because it changes the SOTP's answer by tens of percent while P1 and P2
change it by more — but its falsifier is genuinely reachable, and an anchor that publishes an
invented AI multiple **contaminates every downstream thesis that prices off it**.

**Independently falsifiable**: no admissible framing produced by any of the three — i.e. the AI
segment is carried `UNRESOLVABLE-FROM-PUBLIC-SOURCES` at zero, and P1's separability test then
governs whether the SOTP survives at all.

**wrong_if**: `metric=count_of_admissible_ai_segment_valuation_framings_derivable_from_filed_or_peer_data threshold=1 source=10-Q_segment_note_capex_disclosure_and_peer_bench_tables op=<`

**Subscribed**: `SPCX × business-model`, `SPCX × peer-bench`, `SPCX × secular-trends`, `SPCX × what-if`

**Binding constraint**: `POWER` is the constraint on the *business*, but the constraint on
*valuing* it here is `A4` — a constitution-level boundary, not an operational one. **Not
`CAPITAL`**: capital is being spent and is disclosed; what is missing is an admissible
capitalisation of it.

---

### Pillar 4 — Space is a public good with a private balance sheet: standalone value separable from Starship funding (Priority: P4)

Two facts about Space that point in opposite directions, and both are `DEMONSTRATED`:

- It carries **the highest gross margin in the universe — 65.8%** — with **cost of revenue flat
  (−0.3%) while revenue rose 29.0%**, so **the marginal Falcon launch is highly profitable**.
- It reports an **operating loss of $(542)M, widening +46.9%**, because **R&D is $1,076M — 3.3×
  cost of revenue and 111.9% of segment revenue** — driven by Starship production, engineering
  and test.

**The difference is the entire question.** Basis C's **$6,596/kg** fully-loaded figure is
**Starship-subsidised**: it divides a segment cost base inflated by a future vehicle by a
current-vehicle customer-tally. An analyst arguing *"SpaceX loses money on every launch"* and
one arguing *"SpaceX is profitable per launch"* can both cite the same filing; the difference is
whether Starship R&D is assigned to Falcon missions.

**The claim:** the standalone launch business is **separable** from Starship development funding —
the segment's **ex-Starship-development operating result is positive** — and therefore carries
standalone value in the SOTP rather than being carried as an input-cost centre. The
**inter-segment transfer limitation** (DA-08: 27 of 37 launches internal, no inter-segment
revenue) is **stated in the SOTP as a limitation**, not netted silently.

**Why this priority**: P4 because the segment is 12.3% of revenue and falling (−1.9% H1) — too
small to move the anchor, and large enough that mis-assigning Starship R&D changes whether the
SOTP has two or three positive-value segments. It is also where **A1b's falsification is priced**:
value migrated from launch to constellations and services, and the SOTP must show that migration
rather than assert it.

**Independently falsifiable**: an ex-R&D Space segment result that is **negative**, i.e. gross
profit less SG&A below zero — at which point launch has no standalone value even before any
Starship allocation, and Space enters the SOTP as an input cost with its revenue treated as
strategic rather than economic.

**wrong_if**: `metric=space_segment_operating_margin_ex_RD_pct threshold=0 source=10-Q_segment_note_component_identity op=<`

**Subscribed**: `SPCX × operational-kpi`, `SPCX × unit-economics`, `SPCX × competitive`, `SPCX × business-model`

**Binding constraint**: `MANUFACTURING_RATE` in the medium term — F5b, the expended second-stage
manufacturing curve is the binding floor for a partially reusable vehicle, not propellant.
**The ex-R&D test itself is bounded by disclosure granularity**, since the filing does not split
Starship from Falcon R&D; the split is therefore `MODELED` and must be labelled so.

---

### Pillar 5 — `CAPITAL` is the binding constraint, and the SOTP's swing factor is the funding requirement (Priority: P5)

The constitution requires **exactly one** binding constraint per thesis, and PROGRAM §2 names
**`CAPITAL`** for 004. The operational reading is direct: SPCX is deploying capital at a scale no
internal cash flow approaches, and it is deploying it **on the ground**.

```
H1 2026 operating cash flow   +$3,466M
H1 2026 investing            $(34,487)M     ← coverage ≈ 0.10×
H1 2026 financing           +$100,291M      ← IPO $85,675M + notes $40,869M
```

**A company with a $(143)M quarterly operating loss raised $85.7B in equity and $40.9B in notes,
and named data centers before launch facilities when describing the capex.** The constraint that
binds is the **cost and availability of external capital** — because it is the only input whose
withdrawal stops the build, whereas a delay in any physical constraint merely moves it.

**The claim:** within the SOTP's forecast horizon, **internal cash flow does not cover the
compute build** (coverage ratio **below 1.0×**), so the anchor's downside scenario is governed by
the funding structure rather than by any physical or demand constraint — and the anchor **states
its financing assumption explicitly**, including the **Cursor** $60B all-stock dilution under
P11 and the single-class control structure that determines who can price that dilution.

**Why this priority**: it is P5, not P1, because it is a *context* claim rather than a *value*
claim — but it is the one that decides which scenario the SOTP's probability weights belong on,
and it is the **only pillar whose falsifier would re-rate every other pillar at once**.

**Independently falsifiable**: an internal coverage ratio at or above **1.0×** over the SOTP's
horizon, which would mean the build is self-funding and the capital constraint is not binding.

**wrong_if**: `metric=spcx_ttm_operating_cash_flow_coverage_of_investing_outflow_ratio threshold=1.0 source=10-Q_cash_flow_statement op=>=`

**Subscribed**: `SPCX × ratio-analysis`, `SPCX × risk`, `SPCX × growth-strategy`, `SPCX × competitive`, `SPCX × recent-quarter`

**Binding constraint**: `CAPITAL` — the thesis-level constraint, carried here. **Index inclusion
and float structure ride on the same pillar**: the constitution records **no index inclusion at
ratification**, so the marginal buyer of the equity that funds the build is a **dated catalyst**,
not a standing assumption, and it must be recorded as such or dropped.

---

### Pillar 6 — The anchor publishes three regimes *with comparability boundaries*, not three numbers (Priority: P6)

004's value to the programme is not its number — it is that **005–009 benchmark against it**
(PROGRAM §5). An anchor published as a point estimate, or as a multiple without a stated
comparability set, propagates a **false comparability** into every downstream thesis, and the
error is invisible because the downstream theses will each look internally consistent.

**The failure is structural and each segment fails for a different constitutional reason:**
Space's pure-play comparables (RKLB, FLY) are **loss-making**, so no earnings multiple exists;
Connectivity's *profitable* comparables (IRDM, GSAT) are **P11 deal securities** whose prices
track spreads rather than fundamentals, so their multiples are inadmissible; and AI's comparables
**do not report a discrete compute segment** at all. **Three regimes, three different reasons no
natural comp set exists.** The SOTP must therefore source its multiples from SPCX's own segment
data and from bounded read-throughs, and say which comparators are **admissible** and which are
**excluded, and why.**

**The claim:** the anchor table publishes **one multiple regime per segment**, each with a
**source, a grade, and an explicit comparability boundary** naming which downstream names may
and may not price off it — and **zero** published anchors lack a boundary.

**Why this priority**: last because it is the hand-off, and it can only be written after P1–P5
land. Its payoff is that it is the mechanism by which the anchor **fails loudly instead of
silently** in someone else's thesis.

**Independently falsifiable**: any published segment anchor without a stated comparability
boundary — including an anchor whose boundary is "all peers," which is the same failure stated
politely.

**wrong_if**: `metric=count_of_published_segment_anchors_without_a_stated_comparability_boundary threshold=0 source=004_anchor_table op=>`

**Subscribed**: `SPCX × peer-bench`, `SPCX × comps`, `SPCX × sector-overview`, `SPCX × ratio-analysis`

**Binding constraint**: *disclosure granularity* — the anchor can only publish a boundary as
narrow as the comparables' own segment disclosure permits. **Not** `DEMAND`: the constraint on
the hand-off is what the peers disclose, not how much demand exists.

---

> **Delivering P1 alone yields a defensible partial conclusion** — SPCX either decomposes into
> three separable businesses or it does not, and 005–009 will know which before they size
> anything. That is the single most valuable output of this thesis and it is delivered first.

## 1c. Method — the valuation instruments

Four capabilities are specific to this thesis and are the reason an anchor valuation is a
distinct workstream rather than a pass over 001's artifacts.

1. **Scenario-weighted SOTP — the constitution-mandated primary instrument.** Three segments,
   three multiple regimes, probability-weighted scenarios. **The multiple-sourcing problem is the
   method's real content**, and it is worse than it looks: each segment fails to find a natural
   comp set for a different reason.

   | Segment | Natural comparables | Why no admissible comparable multiple exists | SOTP treatment |
   |---|---|---|---|
   | **Space** | RKLB, FLY (005); BA, LMT, NOC (007) as primes | Pure-plays are **loss-making** — there is no earnings multiple to borrow | Revenue or capacity multiple, `MODELED`, stated as a range |
   | **Connectivity** | IRDM, GSAT (006); ASTS, VSAT (006) | The profitable comparables are **P11 deal securities** — their price is a **spread**, not a fundamental. ASTS/VSAT are `PARTIAL` | Margin-anchored, `MODELED`, cross-checked against terrestrial broadband rather than satellite peers |
   | **AI** | MSFT, GOOG, NVDA (009) | **None reports a discrete compute-infrastructure segment carrying a comparable multiple** | One of three framings; see **P3** |

   **The only `DEMONSTRATED` inputs to the SOTP are the segment financials themselves.** Every
   multiple is `MODELED`, and P4 requires each to be labelled as such. Scenario weights are
   likewise `MODELED` — no vendor source exists for them, and `assumptions.yaml` carries no
   scenario-weight field, so a weight that is not justified in-line is **silent drift**.
2. **Comparability-boundary construction.** Every published anchor names (a) the peer set it was
   drawn from, (b) the comparators **excluded** and the reason — `P11`, loss-making, `PARTIAL`
   coverage, or non-disclosure — and (c) the downstream names permitted to price off it. This is
   where `peer-bench` and `comps` deploy, and comps are used **only here**: the constitution makes
   them a **cross-check**, never primary, and at the consolidated line SPCX is a pre-profit issuer.
3. **The DCF admissibility gate — run, and expected to fail at the consolidated level.**
   The constitution admits DCF only with **≥3 years of positive FCF** *or* **a contracted backlog
   covering the forecast period**. SPCX fails the FCF limb: H1 2026 operating cash flow
   **+$3,466M** against investing **$(34,487)M**. The backlog limb is available **at the Space
   segment only**, where Launch and Development contracts run **1–14 years**, and it is
   unquantified (V-7). **`dcf` is therefore deliberately absent from §3.** A segment-level DCF on
   Space may be commissioned *after* V-7 resolves; commissioning one before the gate passes would
   violate the constitution's own sequencing, and a consolidated DCF is barred outright.
4. **Component identity, in-line, always.** Per **DA-23**, an artifact reading `operating_income`
   shows `gross profit − opex` in-line. The SOTP reads the operating line for all three segments,
   so this applies to every segment table. **`EPS × shares` is not a valid sign test** — it passes
   spuriously on flipped issuers. The **gross-profit bound** (operating income can never exceed
   gross profit, at any sign) is the second detector and is cheap to run here.

**Standing rule — definitional ambiguity.** Per the §1c rule inherited from 001, where a term
admits multiple readings, artifacts report **all** of them, label which is quoted, and treat the
spread as a finding. Four classes bind this thesis directly: **DA-01** (cost bases — A, A′, B, C
are enumerated, never collapsed), **DA-08** (customer vs internal launches), **DA-10**
(Stubscriber/ARPU service-line definition), **DA-11** (IT load vs facility draw), **DA-19**
(common-control recast), **DA-21** (issuer-defined segment boundaries), and **DA-23** (sign).

**Correction policy.** 001's files are **frozen**. Where this thesis invalidates a 001 figure the
correction is recorded in 004 and cross-cited by location — matching 001's own
annotate-don't-rewrite policy. **One exception is inherited rather than created**: 001 itself
recorded that the two `2310` SPCX artifacts **supersede** the `1239` pair, and 004 follows that
ordering wherever they conflict (V-1).

## 2. Universe Definition

**Universe members: one.** A thesis is included as a member only if it receives its own
`artifacts/{ticker}/` output. This thesis sizes no trades, so weights are **analytical effort**,
not positions.

| Ticker | Company | Sector | Weight | Why it is in this thesis |
|---|---|:---:|---|
| SPCX | SpaceX | industrial.aerospace_defense | 100% | **The whole thesis.** Three reportable segments, three multiple regimes, one consolidated loss — the case the constitution's SOTP rule was written for |

**Read-through comparators — NOT universe members.** They receive no `artifacts/{ticker}/`
output of their own; they appear in §3 because read-through effort is spent on them, and they
supply benchmarking inputs consumed **inside** SPCX artifacts. Listed here so the effort is
visible and its limits are explicit.

| Ticker | Company | Sector | Weight | Role — and why it cannot be a universe member |
|---|---|:---:|---|---|
| MSFT | Microsoft | tech.platform_internet | read-through | **AI-segment framing (P3)**. The capex-derived capacity comparator. Compute is a **cost centre inside Intelligent Cloud**, not a segment — so no comparable multiple exists |
| GOOG | Alphabet | tech.platform_internet | read-through | **AI-segment framing (P3)** and the sector's most detailed orbital-compute disclosure (Project Suncatcher). Query as **`GOOG`**, never `GOOGL` |
| NVDA | NVIDIA | tech.semiconductors | read-through | The **silicon** leg of the AI stack. Supplies the capability, reports no compute segment — the read-through is to *feasibility*, never to a multiple |
| VRT | Vertiv | industrial.machinery | read-through | Thermal comparator. Supplies the **DA-11 restatement context that 002 owns** — consumed here, not re-derived |
| IRDM | Iridium Communications | tech.telecom_services | read-through | The **profitable-constellation benchmark** — 66 satellites, licensed L-band, 15.1% operating margin. **A P11 deal security**: its price is a spread, so its **multiple is inadmissible** as a comp (P6) |

**Excluded by design.** The remaining 52 names in the 57-name universe carry no SOTP input. They
enter when a *specific* segment of theirs supplies a comparator — GSAT, RKLB, FLY, ASTS and VSAT
appear in §3 for that reason and for no other — not because they are in the universe. Broadening
§2 would turn this into a second general baseline and repeat 001, which is the failure mode the
program exists to avoid.

## 3. Skill Deployment Matrix

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|:---:|---|:---:|---|
| sotp-valuation | valuation | Deep | SPCX | none | **The constitution-mandated primary instrument.** Three regimes, scenario weights, the discount/premium measure against the dated print (**P1**, **P6**) |
| business-model | equity-research-core | Deep | SPCX | none | Segment-boundary and homogeneity tests — DA-21, the AI segment's Grok/X/compute aggregation, and the P11 Cursor treatment (**P1**, **P3**) |
| unit-economics | business-intelligence | Deep | SPCX | none | Connectivity's ARPU/mix decomposition under **DA-10** (**P2**); the Space ex-R&D margin and the **DA-01** basis restatement (**P4**) |
| operational-kpi | business-intelligence | Deep | SPCX | none | Segment revenue, operating result and the DA-08 internal/customer split; the in-line **DA-23** derivation on every segment table (**P1**, **P2**, **P4**) |
| recent-quarter | equity-research-core | Standard | SPCX | none | Segment series with `validate_calculation` on each issuer-quarter; the **entity-boundary** tagging (**V-4**) (**P1**, **P2**, **P5**) |
| ratio-analysis | quantitative-analysis | Standard | SPCX | none | Coverage ratio for the capital claim (**P5**); every derived ratio re-checked against the component identity (**P1**, **P6**) |
| peer-bench | equity-research-core | Standard | SPCX, MSFT, GOOG, NVDA, IRDM, VRT | none | The AI framing set — including **VRT** for the terrestrial thermal context consumed by DA-11, and the **IRDM** profitable-constellation benchmark (**P3**) — plus the comparability boundaries and their exclusions (**P6**) |
| comps | equity-research-core | Light | SPCX, RKLB, FLY, GSAT, IRDM, ASTS, VSAT | none | **Cross-check only**, per the constitution. Demonstrates *why* each natural peer set is inadmissible — loss-making, `P11`, or `PARTIAL` (**P6**) |
| competitive | equity-research-core | Light | SPCX, RKLB, FLY | none | Launch competitive position behind the Space standalone-value test (**P4**); the capital-intensity comparison behind **P5** |
| risk | equity-research-core | Standard | SPCX | none | The funding-structure and dilution analysis (**P5**); **P11** treatment of Cursor (**V-5**) |
| sector-overview | equity-research-core | Light | SPCX | none | Places the anchor in the Sector Preferences table so the boundaries are sector-relative, not SPCX-relative (**P6**) |
| secular-trends | equity-research-core | Light | SPCX, MSFT, GOOG, NVDA | none | The terrestrial-compute capacity trend the AI framing is bounded against (**P3**) |
| what-if | quantitative-analysis | Standard | SPCX | none | Scenario construction and the DA-10 mix-shift sensitivity — the two places the answer is a range rather than a point (**P2**, **P3**) |
| growth-strategy | equity-research-core | Light | SPCX | none | Capital-allocation narrative against the capex disclosure — data centers named before launch facilities (**P5**) |

> **Coverage invariant.** Every universe member in §2 appears at least once above; every
> `Subscribed` pair in §1b resolves to a matrix row; every matrix skill is named in at least one
> `Subscribed` line. Read-through rows generate **no** per-ticker artifacts. Verified by
> `tools/plan_audit.py` (I1–I4).

## 4. Depth Tiers

| Tier | Skills | mode-set | Tickers | Output |
|:---:|------|---|--------|------|
| Deep | sotp-valuation, business-model, unit-economics, operational-kpi | all modes | SPCX | Full-mode valuation work on the four skills carrying P1–P4 |
| Standard | recent-quarter, ratio-analysis, peer-bench, risk, what-if | essentials_modes | As listed | The segment series, capital ratios, framing set and scenario bounds |
| Light | comps, competitive, sector-overview, secular-trends, growth-strategy | essentials_modes | As listed | The boundary-setting checks that make P6 publishable |

**Budget note.** `thesis.md` sets `max_tasks: 40`. This matrix yields roughly **34 tasks** across
one member and five read-through names — the narrowest universe in the program and the densest
per name. If the budget must come down, **drop the Light rows first** — never the Deep rows,
which carry P1 through P4, and **never the `recent-quarter` or `ratio-analysis` rows**, which are
the entire delivery mechanism for V-2 and the capital claim.

## 5. Cross-Cutting Analysis

- **The anchor table** is the cross-cutting output: one row per segment, each with its multiple
  regime, grade, source, and comparability boundary. This is what 005–009 cite.
- **The discount decomposition.** The gap between SOTP value and the dated market print is
  reported as **three named components** — conglomerate discount, control/float discount, and
  unallocated corporate cost — and where a component cannot be separated from another, that is
  **reported as a finding**, not allocated arbitrarily. A single blended "discount" figure is a
  P6 violation.
- **Price-input discipline.** Market Data Stage is `none`. **Every market-referenced figure
  carries its print date in-line** (`$135.00`, 2026-06; ~$1.62T per the constitution), and no
  correlation, beta or relative-multiple regression against live prices is run. The discount is
  **as of the print**, not live, and says so.
- **Macro sensitivity: high.** SPCX is the longest-duration asset in the universe and the regime
  is hostile to duration — 10Y at 4.80%, 30Y at 5.26%, both at three-year highs, with hike risk
  priced. The constitution's **NEUTRAL** bias and its re-rate triggers (10Y > 5.25%, or a Fed
  pivot to cuts) are the **scenario-weight inputs** for P5's capital claim, not background.
- **Constitution interaction**: **A1b** (falsified — the SOTP must show value migrating out of
  launch, not assert it); **A4 / P10** (the AI segment's admissibility ceiling); **P3** (one
  binding constraint, `CAPITAL` — see Q-4); **P4** and the Data-Integrity Register (DA-23
  in-line, `EPS × shares` barred); **P11** (Cursor); **Risk Framework** (the 40% theme cap binds
  before the 25% sub-sector cap in a single-theme book, and SPCX is the largest single-theme
  exposure available).
- **Pair-trade candidates**: none produced here. This thesis produces the anchor and no positions.

## 6. Output Contract

- **Per-ticker (dispatcher-resumable)**: `artifacts/SPCX/{YYYY-MM-DD}_{skill}_{mode}.md` — the
  suffix **must** be `_{skill}_{mode}.md` with the real mode slug, so `dispatch.resume_verdict()`
  can find it.
- **Cross-cutting (not resume-tracked)**: `_cross/{name}.md`.
- **Primary artifact**: `_cross/anchor-sotp.md` — the three-regime anchor table with grades,
  sources and comparability boundaries, plus the scenario weights and the discount decomposition.
  This is what 005–009 cite.
- **Secondary artifact**: `_cross/segment-attribution-ledger.md` — the V-1 … V-7 validation queue
  with each item's disposition. Read-through tickers contribute **inputs only** and receive no
  per-ticker artifact of their own.
- Snapshot: `snapshots/004-tier0-spacex-anchor/{YYYY-MM-DD}_thesis.md`
- **Frontmatter**: per `contracts/artifact-frontmatter.yaml`, with `thesis_id:
  "004-tier0-spacex-anchor"`. All five pins are mandatory: `constitution_pin: 1.4.0`,
  `assumption_pin: "2"`, `skill_pin`, `as_of`, `corpus_version`.

## 7. Thesis Phases

| Phase | Tasks | Duration | Dependencies |
|:---:|------|:---:|------|
| 1 — Separability (P1) | Read the segment note; resolve **V-1** (does the AI segment file an operating result?); run `segments_sum_to_total` in-line; build the segment-attribution ledger | Week 1 | Constitution v1.3.0 loaded |
| 2 — Connectivity (P2) | ARPU/subscriber/margin series on the component identity; all **DA-10** readings reported side by side; the price-erosion vs mix-shift test | Week 2 | Phase 1 |
| 3 — AI admissibility (P3) | Test framings (a) comparable, (b) invested capital, (c) optionality incl. zero; build the MSFT/GOOG/NVDA framing set; apply the A4/P10 ceiling; **consume** 002's DA-11 restatement | Week 3 | Phase 2 |
| 4 — Space standalone (P4) | Ex-R&D margin; the Starship/Falcon R&D split labelled `MODELED`; **DA-08** internal-transfer limitation; **DA-01** A/A′/B/C restatement | Week 3 | Phase 2 |
| 5 — Capital (P5) | Coverage ratio; funding structure and **Cursor/P11** dilution; control and float; index-inclusion catalyst datability | Week 4 | Phase 3 |
| 6 — SOTP (P1, P6) | Scenario weights with in-line justification; three regimes; the discount decomposition against the dated print | Weeks 5–6 | Phases 1–5 |
| 7 — Hand-off (P6) | Publish `_cross/anchor-sotp.md` with boundaries for 005–006; record what could not be valued | Week 6 | Phase 6 |

## Clarifications

Recorded by `agentii.specify` at creation, 2026-09-18. No `agentii.clarify` round has run; the
following are recorded as open for that pass.

- **Q-1 (P1, price admissibility under Market Data Stage `none`)** — Is the constitution's
  **~$1.62T** anchor admissible as the market comparator when it cannot be refreshed?
  **Provisional answer, pending clarify:** admissible, but **only as a dated print with its date
  printed in-line**, and never described as a current price. A discount quoted against an
  undated market cap is not a finding.
- **Q-2 (P3, the AI framing)** — When no comparable exists, is the honest headline **(a)** zero,
  **(b)** invested capital, or **(c)** an interval from a terrestrial compute comp set admitted
  to be non-comparable? **Provisional:** evaluate all three, report all three per the §1c
  standing rule, and name which one the SOTP headline uses. A segment carried at zero is a
  legitimate output; an unstated choice is not.
- **Q-3 (P4, revenue basis vs capacity basis)** — Should the Space multiple sit on **revenue** or
  on **capacity** (mass to orbit / launches)? They are different businesses: revenue reflects
  customer activity only (**10 of 37** launches), while capacity includes the **27 internal
  launches that generate no inter-segment revenue**. **Provisional:** revenue for the multiple,
  capacity reported as a separate disclosure, and the internal-transfer limitation carried as a
  finding rather than netted.
- **Q-4 (P5, `CAPITAL` vs `POWER`)** — PROGRAM names `CAPITAL` as 004's binding constraint, but
  the AI segment's *business* is bounded by `POWER` (F1/F2). Is `CAPITAL` correctly named?
  **Provisional:** `CAPITAL` holds, because SPCX's AI segment is **terrestrial** and F1/F2 bound
  *orbital* compute — the physical constraints bind a business SPCX is not in. Flagged for human
  confirmation; **if answered differently this is a PATCH to spec, not a MAJOR event.**
- **Q-5 (P6, boundary shape)** — Is a comparability boundary a **partition** (a name is in or
  out) or a **graded score**? **Provisional:** partition, with the excluded class named and the
  reason recorded — `P11`, loss-making, `PARTIAL` coverage, or non-disclosure. A graded score
  invites the downstream thesis to pick its own threshold, which is the failure P6 exists to stop.
- **Q-6 (P1/P5, Cursor)** — Under **P11**, is the headline SOTP **pre-close** (excluding Cursor)
  or **pro-forma** (including the $60B all-stock consideration and its dilution)?
  **Provisional:** pre-close headline, with a pro-forma sensitivity reported separately, because
  the consideration is Class A stock whose dilution is not determinable from the pages read
  (**V-5**).
- **Q-7 (all pillars, 002 dependency)** — Where 002 has not landed, does 004 inherit 001's grades
  unchanged, or wait? **Provisional:** inherit and **label**, per the §1c standing rule. Waiting
  would idle the anchor behind a foundation thesis; inheriting silently is the drift P4 bars. The
  label is the whole remedy.
