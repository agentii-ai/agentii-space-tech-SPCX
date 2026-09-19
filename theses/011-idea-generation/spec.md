# Research Thesis: 011 — Idea Generation, Strategies & Cases

**Constitution Ref**: constitution.md **v1.6.0** (`constitution_pin: 1.6.0`) — **re-pinned at
the re-specification round, 2026-09-19. Was `1.4.0`**, which predated both the §Universe
Definition re-cut (one axis — *function in the value chain* — with an explicit membership
test that moved **PL, BKSY, HAWK, SPIR to Tier 2**) and the DA-26 census correction
(20 tested, 19 exhibiting; FLY the counterexample). **The ownership rule in §0 is v1.6.0's
cross-tier dependency rule, instantiated** — see §0.
**Created**: 2026-09-18 · **Specified**: 2026-09-18 (upgraded from stub by the clarify round on 002)
· **Re-specified**: 2026-09-19 (ownership arbitration; the corrected GSAT rung — §0, Q-9, Q-10)
**Status**: Active
**板块**: Decision layer · **Binding constraint**: *n/a — portfolio construction*
**Depends on**: `001-technology-baseline` (the register), `002-evidence-validation`
(**COMPLETE** — graded inputs *with their basis*, per its own headline finding),
`003-launch-cost-curve-value-migration` (**COMPLETE** — the corrected margin ladder and the
value-pool map), `004-tier0-spacex-anchor` (**landed** — the anchor valuation). **And only
those four for the work this thesis executes.**
**Cites (does not depend on, does not re-derive)**: `005` (runway, break-even),
`006` (deal gate chain, operator margins, the licensed asset), `008` (the ladder's
extension, solar-cell pricing) — **§0a is the ownership rule, §3b the mechanism, and an
owner that has not run is carried as `PENDING`, never filled in.**
See §1d for the **split dependency**: the main line and the strategy layer start now;
only position sizing waits — **now on 005–010, not 004–010.**
**Produces**: the program's **governing investment argument**, the strategy inventory
with honest actionability grading, and — once the segment theses land — a sized book.

---

## 0. Inherited baseline — what this thesis does NOT re-derive

011 inherits all of 001–010 by construction and re-derives none of it. But it is
**specified early, ahead of 004–010**, because the clarify round established that its
first five pillars do not depend on them. That is a deliberate change to this thesis's
sequencing, and §1d states its cost. **Since the re-specification round: 004 has landed
(so the block on P7 is 005–010), and the parts of P3–P6 that belonged to 005, 006 and 008
are cited rather than researched — §0a is the rule, §3b is the mechanism.**

### 0a. The ownership rule — added at the re-specification round, 2026-09-19

**011 was re-deriving questions five other theses own.** The constitution's §Universe
Definition, re-cut at **v1.6.0**, states the governing rule — *"A cross-tier question
belongs to the thesis that owns that tier, and the host thesis cites it"* — and the
programme's arbitration table is that rule **instantiated**. **Each contested question has
exactly one owner, and an overlap is resolved by lookup, not by negotiation:**

| Contested question | **Sole owner** | 011's role |
|---|---|---|
| IRDM/RKLB deal gate chain | **006** (`constellation-operators`) | **cite, don't re-derive** |
| Solar-cell duopoly & pricing power | **008** (`supply-chain-components`) | **cite** |
| The margin ladder's monotonicity | **008** | **cite** |
| Financing runway / fixed-cost absorption | **005** (`launch-spacecraft-services`) | **cite** |
| Operator margins by segment | **006** | **cite** |

**How 011 discharges the rule — three clauses, and they are binding:**

1. **No task.** Each of the five questions is cited in a `Consumes (00X)` line under the
   pillar that uses it, and **generates no 011 task** (§3b states the mechanism). 011's
   §0 already disclaimed re-research; §3a is where that disclaimer becomes arithmetic.
2. **Cite the owner, not the number.** Where 011 quotes an owner's figure it names the
   owner and the artifact, and carries the owner's grade. Where the owner **has not yet
   run** — 005 and 006 are specified but unrun, and 008's spec is not yet frozen — the
   question is carried
   as **`PENDING — owned by 00X`**, and **011 does not research it to fill the gap.**
   What 011 may still quote in that state is 001's or 003's *finding* on the same subject,
   with the owner's reframing named as outstanding.
3. **Cite the correction, not only the corrected number.** A figure 011 takes from an
   upstream thesis travels **with its correction history** (see the GSAT rung below), because
   the correction is the part a downstream reader cannot reconstruct.

**The rule's necessity is measured, not asserted.** The constitution records why it exists:
*"thesis 005 (Tier 1) had grown three pillars belonging to other tiers — a supply-chain
duopoly, a single-deal merger model, and a financing screen — until only one of its six
pillars was about its own cohort."* **At this round 011 was carrying the same three
questions** — 008's duopoly (strategy 6), 006's deal model (strategy 4), 005's financing
screen (strategy 2). The defect the v1.6.0 re-cut was written to stop had **recurred one tier
up**, in the thesis whose job is arbitration rather than research — which is why the fix is a
**table with one owner per row** and not a paragraph of intent.

> **The ownership rule is not a boundary of topic; it is a boundary of *work*.** 011 still
> grades every name it cites — actionability, dilution and trigger are 011's own questions
> and no one else's. What it no longer does is **compute another thesis's instrument on
> that thesis's names**, which is what P3, P5 and P6 did before this round (§1b).

### 0b. Inherited baseline — 001 to 004

**Path shorthand used throughout this thesis — declared, not implied.** Paths are real and
relative to *this spec's directory*; `001/` expands to `../001-technology-baseline/`,
`005/` to `../005-launch-spacecraft-services/`, and `theses/` to `../../`. Every row resolves
to a file on disk — e.g. row 1 reads
`../001-technology-baseline/_cross/technology-baseline_synthesis.md` §4.1, and row 15 reads
`../004-tier0-spacex-anchor/_cross/tier0-spacex-anchor_synthesis.md`.

| # | Inherited result | Source artifact | Grade |
|---|---|---|---|
| 1 | **The margin ladder** — operating margin ordered by distance from programme risk across **8 issuers**, descending and **bottom rung NEGATIVE** at the corrected value: HEI 25.5%, KRMN 19.1%, WWD ~17%, LMT 12.4%, RTX 11.4%, LHX 11.1%, NOC 10.1%, GSAT **−7.37%** ⚠️ **CORRECTED — see 0c** | `001/_cross/technology-baseline_synthesis.md` §4.1; rung corrected from `003/_cross/value-pool-map.md` §E-11 | `DEMONSTRATED` (the ordering) — **the *consecutive-decline* reading does not survive; see 0c** |
| 2 | Refined rule: **component concentration predicts margin when the supplier's revenue spreads across programmes** — the discriminator is single-programme dependence, not buyer concentration | `001/_cross/technology-baseline_synthesis.md` §4.1 | `DEMONSTRATED` |
| 3 | **The ladder is BIMODAL, not one smooth ladder** — component suppliers **22.76%** (TER 32.9 · HEI 25.5 · CW 19.3 · KRMN 19.1 · WWD ~17.0) against prime integrators **11.25%** (LMT 12.4 · RTX 11.4 · LHX 11.1 · NOC 10.1) = **2.02×**; the operator rungs sit **outside both bands** (SPCX Connectivity **+38.59%**, GSAT **−7.37%**) and the launcher/manufacturer rows are all negative. **Which ladder you pick decides whether launch looks like the best business in the sector or the worst** (SPCX Space: gross margin 65.80%, operating margin −56.34%) | `003/_cross/launch-cost-curve-value-migration_synthesis.md` §3 | `DEMONSTRATED` — **003's re-measurement is the reason row 1's ordering claim is restated rather than repeated** |
| 4 | **Value migrated out of launch at the launch monopoly** — Connectivity 54.9%, AI 32.8%, Space 12.3% of SPCX revenue; **Space −1.9%** across a half in which consolidated revenue rose **53.7%**; mass to orbit **−25.6%**, Falcon launches **−17.8%**; Space operating margin **−56.3%** at a **65.8% gross margin**. **⚠️ The AI 32.8% share is boundary-contaminated** (xAI common-control recast, 2026-02-02) and **may not be quoted as organic migration** — routed to 002 P6; Space (clean) and Connectivity (clean, organic) carry the claim | `001/_cross/technology-baseline_synthesis.md` §4.6; `001/artifacts/SPCX/2026-09-18_2310_operational-kpi_methodology.md` §1; `001/artifacts/SPCX/2026-09-18_2310_business-model_methodology.md` §2 | `DEMONSTRATED` (Space, Connectivity) / boundary-flagged (AI) |
| 5 | **Fixed-cost absorption is the binding constraint on operators** — PL break-even **1.69×** current revenue (53.5% GM, 90.6% opex ratio); YSS **2.86×**; **neither multiple involves launch cost**. **⚠️ RE-OWNED at this round: the instrument is 005's** (`005/spec.md` §1b P3, bound to its P1 funding-runway test) and 005's reframing is outstanding | `001/_cross/technology-baseline_synthesis.md` §4.2 | `DEMONSTRATED` — **owner 005; 011 cites (§3b)** |
| 6 | **Terrestrial compute is constrained but expanding** — MSFT FY2026 capex **$115,948M** implies **2.9–11.6 GW/yr** against SPCX's **1.4 GW cumulative**; VRT margin *expanding* **2.7 pts on +24% revenue** | `001/artifacts/MSFT/2026-09-18_1239_secular-trends_methodology.md` | `DEMONSTRATED` |
| 7 | **Orbital compute is out-*chosen*, not out-built** — the only actor with cheap orbital access deployed **1.4 GW on the ground**, named data centers before launch facilities in its own capex narrative, and is buying a software company with stock | `001/_cross/technology-baseline_synthesis.md` §Line 5, §7 | `DEMONSTRATED` |
| 8 | **The demand side is 73× the supply side** — three pharma buyers turn over **$39,634M/qtr** against a **~$2,170M/yr** space cohort | `001/_cross/technology-baseline_synthesis.md` §4.3 | `DEMONSTRATED` |
| 9 | **Four critical duopolies are structurally unpriced** — solar cells, liquid engines, solid motors, radiation-tolerant electronics; **MRCY earns 0.03%**, so rad-hard is not scarce the way F2's thermal area is | `001/_cross/technology-baseline_synthesis.md` §4.5 | `DEMONSTRATED` (structure) / `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (price) — **owner 008 for solar cells; 011 cites** |
| 10 | **"No listed issuer offers both growth and margin except TER and KRMN"** | `001/_cross/technology-baseline_synthesis.md` §7 | `DEMONSTRATED` |
| 11 | **Spectrum reference price $19.6B** (SPCX–EchoStar, AWS-4 / H-Block / AWS-3; FCC-approved, transfer closed) | `001/_cross/phase-4-regulatory-allocation.md` | `DEMONSTRATED` |
| 12 | IRDM and GSAT are **deal securities** — RKLB @$54/sh, AMZN @$90/sh; **P11 governs every figure quoted for them** | constitution §P11 | `CLAIMED` (terms from announcement) — **owner 006 for the gate chain** |
| 13 | The **corpus gap**: no industrial/aerospace domain exists, so sector-keyed strategy retrieval returns zero **by construction** — and reporting that emptiness as *"no analogues exist"* is a false negative | `theses/PROGRAM.md` §4 | `DEMONSTRATED` |
| 14 | **002's headline is a warning about grades, not about arithmetic:** *converting a figure to `DEMONSTRATED` does not convert its BASIS* — the two come apart by **46.47 pp on one ratio** (SPCX `operating_margin`: a filed **−16.68%** served as **+29.79%**). **Every 011 figure inherited from 001 therefore travels with its basis.** 002 also **falsified its own PIL-5** (four of nine readings fire) and confirmed DA-23 as **a census of a default, not a rare defect: 14 of 17 issuers** | `002/_cross/002-evidence-validation_synthesis.md` §1, §2, §3 | `DEMONSTRATED` — 002 is **COMPLETE** |
| 15 | **The anchor valuation** — SPCX's live market capitalisation **$2.0718T** is **312.8×** Connectivity's annualised operating income, and **Connectivity is the only profitable segment** (Space and AI run losses). **No conventional conglomerate discount exists to measure**; the finding survives every allocation (86× at the most generous). **Comparability partition admits 0 of 11**; coverage ratio **0.1005×**; Cursor **closed 2026-08-14**, 391,041,680 shares issued. Market data is **LIVE** — SPCX **$152.71** (close 2026-09-18) | `004/_cross/tier0-spacex-anchor_synthesis.md`; `004/_cross/anchor-sotp.md` | `DEMONSTRATED` (Connectivity, Space) / `MODELED` (AI, carried at invested capital) — 004's challenge found **4 HIGH findings, all in the `entity_claims` schema; the arithmetic survives every angle** |
| 16 | **003's deal finding, which 011's P5 now cites rather than rebuilds:** Amazon pays **≈41.4× TTM revenue for a loss-making operator** (GSAT) while RKLB pays **≈8.3× for a profitable one** (IRDM) — a **≈5.0× multiple ratio against a 22.5-point margin differential in the opposite direction.** **Neither acquirer priced the target's income statement** | `003/_cross/launch-cost-curve-value-migration_synthesis.md` §3 | `DEMONSTRATED` (41.4×) / `UNRESOLVED` (IRDM multiple, armed band 6.5×–8.5×) |

### 0c. ⚠️ The corrected GSAT rung, and which reading changes

**`001` printed the ladder's bottom rung as `GSAT 7.4%`, graded `DEMONSTRATED`. That value is
the DA-23 sign strip — the platform serving a filed negative as a positive of identical
magnitude. GSAT's filed Q2 2026 operating margin is `−7.37%` (operating loss $(4,775)k on
$64,772k revenue, the filed margin printed `(7.37)%`).** Traced end to end: **001 originated
it** (`001/artifacts/GSAT/2026-09-18_2040_competitive_methodology.md` — the row
`| Operating margin | 7.4% | 9.2% | −1.8 pts |`), **002 missed it**, **003 corrected it**
(`003/_cross/value-pool-map.md` §E-11 carries the correction, with the 1,000× offset systematic
across **7 served facts**), and **011 still carried it at this round.** The correcting source
is **003**, and every citation of this rung in this thesis names it.

**What changes:**

| Reading | At `+7.4%` — 001's text | At `−7.37%` — corrected |
|---|---|---|
| The **ordering** | 8 rungs descending | 8 rungs descending — **unchanged** |
| The **character of the bottom rung** | the thinnest *positive* margin in the set | **the only NEGATIVE margin in the set** — a categorically different fact, not a small number |
| 001's derived comparison (`9.2% → 7.4%, −1.8 pts`) | a modest **−1.8 pt** erosion | **`+9.15% → −7.37%`, a −16.5 point swing to a loss**, and the line turned negative **inside** the year (Q1 2026 +$8,170k → Q2 2026 −$(4,775)k) |
| "*Monotone*" as a **consecutive decline** down a ladder | a smooth 25.5 → 7.4 staircase | **does not survive** — the measured shape is **BIMODAL** (row 3): two bands, 22.76% and 11.25%, with GSAT not on the staircase at all |
| The **mechanism** ("distance from programme risk") | a thin positive margin at maximum concentration | **strengthened** — at the maximum-concentration end (one customer = **64% of six-month revenue**, and that customer is also the financier and the acquirer) the operating margin is **negative**, not thin |

**The restated claim, and it is the only form 011 asserts:** *operating margin is **ordered** by
distance from programme risk across the eight names — and the maximum-concentration end is
**negative**, while the diversified end is the sector's best margin.* **011 asserts the ordering
and the sign change; it does not assert a smooth monotone decline, and it does not assert the
ladder's shape** — the bimodality in row 3 is 003's measurement, and **the extension to all 21
Tier 3 names is 008's question, not 011's** (§3b).

**What 001 did not do:** turn any of it into a position. 001 sized no trades and named no
strategy. Its synthesis ends at findings. 011 begins there. **And what 002–004 added to the
starting point is not more findings but a discipline and an anchor: 002's *grade ≠ basis*,
003's re-measurement and its corrected rungs, and 004's valuation of the one profitable
segment in the anchor.**

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

### 1a. The main line (P1 — formable now; 001–004 all landed)

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

**⚠️ The bottom rung is NEGATIVE, not thin — corrected at this round (§0c).** The ladder's
bottom rung is GSAT at **−7.37%**, the DA-23 sign strip corrected by **003**, not the `+7.4%`
001 printed. **The ordering survives; the reading "a thin positive margin" does not.** The
correction *strengthens* the axis: at maximum programme concentration — one customer at
**64%** of six-month revenue, and that customer is also the financier and the acquirer — the
operating margin is **negative**, not merely small.

**And the axis is not a smooth staircase.** 003 re-measured the same eight names and found
the shape **bimodal** — component suppliers at **22.76%** against primes at **11.25%**
(2.02×) — with the operator rungs outside both bands. **011 therefore asserts the *ordering*
and the *sign*, not a smooth monotone decline**, and it does not own the ladder's shape:
**extending it to all 21 Tier 3 names is 008's** (§0a, §3b).

**The core finding, and this thesis's headline: you cannot buy this theme cleanly.**

### 1d. Split dependency (the sequencing change introduced at the clarify round)

| Pillars | Depends on | Can start |
|---|---|---|
| **P1–P2, P4** — the main line, the dilution quantification, the terrestrial expression — **executed here** | 001, 002, 003, 004 | **Now** |
| **P3, P5, P6** — strategies 2, 4 and the watch items — **citation only** (§0a, §3b) | the owners: **005** (P3), **006** (P5, and strategy 5), **008** (strategy 6) — **specs now, artifacts when those theses run** | **Now, as citations** — every not-yet-run owner is carried as `PENDING — owned by 00X` and **never filled by 011** |
| **P7** — sizing, catalyst calendar, theme-cap arithmetic | **005–010** (⚠️ re-scoped: **004 has landed**, so the anchor is an input now, not a dependency) | After wave 1–2 |

**The cost of this split, stated rather than hidden:** P7 cannot start, so this thesis
will produce an **unpositioned** main line first. A reader of the P1–P6 output gets the
argument and the strategy inventory but **no sizes and no entries**. That is deliberate —
the alternative was to defer the whole thesis to wave 3, which would have left the
program's governing argument unwritten while nine segment theses were researched against
it.

**And the citation conversion has a second cost, which is also the point.** 011 now delivers
**fewer computed numbers than it was specified to**: three quantities the earlier draft
would have derived — the break-even multiple per pre-profit name, the two deals' gate chains,
and the ladder's extension — are **005's, 006's and 008's**, and 011 reports them as
`PENDING` until those theses run. A reader may find the strategy inventory thinner than
before. **The alternative was two theses computing one number on one set of names, which is
invisible from inside either thesis and visible only from here** — which is why §0a is
written down rather than agreed.

---

## 1b. Pillars

### Pillar 1 — The main line is real: one argument explains four independent findings (Priority: P1) 🎯 Minimum Defensible View

Four of 001's results were produced independently and reported separately. **The claim is
that they are one finding:**

| # | 001's finding | Its register |
|---|---|---|
| 1 | Margin **ordered** by distance from programme risk (8 issuers) — **bottom rung NEGATIVE at −7.37%** (§0c, corrected by 003) | *who earns* |
| 2 | Value migrated out of launch at the launch monopoly | *where value went* |
| 3 | Fixed-cost absorption binds, not launch cost (PL 1.69×, YSS 2.86×) | *why operators lose* |
| 4 | Orbital compute out-*chosen* by the only actor who could choose it | *why the narrative didn't convert* |

Read together: **the sector pays for indifference to outcome and punishes concentration —
including concentration on the launch programme the theme is named after.** (2) is (1)
measured at the anchor; (3) is the mechanism by which (1) is enforced on operators; (4) is
(1) applied to the sector's largest narrative, where the most-indifferent actor available
— a monopolist launcher — chose the layer with diversified demand.

**The corrected rung, stated inside (1) rather than beside it — §0c.** Finding (1) is the
ladder, and its bottom rung was carried at `+7.4%` through four theses. **It is `−7.37%`** —
003's correction of a DA-23 sign strip, not a small positive number. **The ordering is
unaffected, and the claim is stronger for it:** *margin is ordered by distance from programme
risk, and the maximum-concentration end is negative.* What does **not** survive is the older
reading — *a thin positive margin*, and a smooth `25.5% → 7.4%` staircase. 003 measured the
shape as **bimodal** (22.76% vs 11.25%), and the rung's own series is a **−16.5 point swing
to a loss inside the year** (`+9.15% → −7.37%`). **011 asserts the ordering and the sign; it
asserts neither smooth monotonicity nor the ladder's shape** — the shape is 003's measurement,
and the extension to the 21 Tier 3 names is **008's** (§0a, §3b). **The rung is cited
wherever it appears in this thesis, and named as corrected.**

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
a genuine selection concern. **Extending it to the full 21-name Tier 3 list is 008's**
(§0a — an ownership, not an assignment to be re-negotiated); until that runs, the claim is
`DEMONSTRATED` on 8 names and `MODELED` beyond them.

**Subscribed**: `HEI × business-model`, `KRMN × business-model`, `SPCX × business-model`, `SPCX × recent-quarter`

**Consumes (§0a — cited, generating no task by design):** the ladder's shape and its bottom
rung from **003** (`003/_cross/value-pool-map.md` §E-11;
`003/_cross/launch-cost-curve-value-migration_synthesis.md` §3), and the ladder's extension
from **008** — `PENDING — owned by 008` (its spec not yet frozen). **`GSAT × competitive` and
`PL × unit-economics` were removed from this pillar at the re-specification round: the
monopsony case is 006's and the break-even multiple is 005's.** See §3b.

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

### Pillar 3 — Strategy 2 (fixed-cost absorption) is **005's instrument**; 011 cites it and grades what it is not (Priority: P3)

**⚠️ Converted from re-derivation to citation at the re-specification round (§0a).** This
pillar previously computed a break-even revenue multiple per pre-profit name. **The
financing-runway question is 005's** — 005 P1 is its Minimum Defensible View and **005 P3
owns this exact instrument on these exact names**, having been specified with them. 011
computing it as well would have meant **two theses, one number, one set of names.** **No
task is generated here.**

**The instrument, cited and not rebuilt** — `opex ratio ÷ gross margin`: PL needs **1.69×**
current revenue, YSS **2.86×**, and **neither multiple involves launch cost**. The measured
values are **001's** (`001/_cross/technology-baseline_synthesis.md` §4.2, `DEMONSTRATED`);
the reframing of them against a runway test is **005's** (`005/spec.md` §1b P1 and P3) —
**`PENDING — owned by 005`**, specified but not yet run, and **011 does not fill the gap by
computing it itself.**

**What 011 still owns, and it is a judgement rather than a computation.** 001 established
that this screen answers the question PIL-3's falsifier spent 19 documents failing to
reach, and that it is the **only mechanically reproducible screen the sector supports**.
Both are true, and neither is the whole reading: **it is a *pre-profit industrial* screen —
it would work unchanged on any capital-intensive manufacturer** — so it must be reported as
a **timing instrument, not a space-exposure instrument.** That grading is 011's
contribution here, and it is a statement about the label, not about the arithmetic.

**The 011-owned claim**: the screen's *interpretation* — a name inside the lower band is
investable on volume, a name above the upper band is waiting on a financing event — sorts
the cohort by **when**, not by **what**, and the strategy inventory must say so wherever a
reader would otherwise read it as a space view.

**Independently falsifiable**: a name that closes a >2× break-even multiple without
dilution, debt, or a revenue inflection. *The test is 005's to run; 011 reports its outcome
and grades the label.*

**wrong_if**: `metric=count_of_preprofit_names_closing_a_break_even_multiple_above_2x_without_external_financing threshold=0 source=005_artifact_10-Q_cash_flow_statement_and_liquidity_note op=>`

**Consumes (005)**: the break-even instrument and its worked multiples — `005/spec.md` §1b
P1 (funding runway) and P3 — **cited from §3b, generating no tasks by design.** *(This field
is not parsed by `plan_audit` or `tasks_md`; §3b states why.)*

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

### Pillar 5 — Strategy 4 (the deal spread) is **006's gate chain**; 011 cites it and grades the position (Priority: P5)

**⚠️ Converted from re-derivation to citation at the re-specification round (§0a).** This
pillar previously enumerated each deal's gate chain itself. **The IRDM/RKLB deal gate chain
is 006's** — 006 P4 prices the two deal spreads against the gate chain and 006 P5 carries
the checklist — and **operator margins by segment, the other half of what this pillar would
have computed, is also 006's.** **No task is generated here.**

**Cited, not rebuilt**: IRDM (RKLB @$54/sh) and GSAT (AMZN @$90/sh) are **spread trades on
regulatory gates**, and the chain is **sequential, not parallel** (001's DA-18): FCC licence
transfer → ITU coordination → DCSA/CFIUS-adjacent review → national market access. **A
thesis treating "regulatory approval" as a single event understates the process by three
gates** — that sentence is 001's finding and **006's checklist to maintain**
(`006/spec.md` §1b P4, P5 — `PENDING — owned by 006`). **011 does not enumerate the gates.**

**And what 011 cites from 003 is the pricing fact that makes the strategy worth stating at
all**: Amazon pays **≈41.4× TTM revenue for a loss-making operator** (GSAT) while RKLB pays
**≈8.3× for a profitable one** (IRDM) — **a ≈5.0× multiple ratio against a 22.5-point margin
differential in the opposite direction, and neither acquirer priced the target's income
statement** (`003/_cross/launch-cost-curve-value-migration_synthesis.md` §3).

**What 011 owns here, and it is a portfolio judgement, not a gate count.** P11 governs: do
**not** underwrite standalone fundamentals; the price tracks a spread; **size at the 2%
binary cap**; on a break, re-underwrite from scratch — a failed deal leaves both target and
acquirer re-rated and the acquirer carrying deal costs. **The two positions' actual value to
this book is that they are low-correlation to everything else in it** — which matters
precisely because the book is single-theme, and it is the one diversification 011 can state
without sizing (P7).

**The 011-owned claim**: the deal securities are **actionable and are not a space view at
all** — their P&L is a function of regulatory timing, not of the sector's economics. The
strategy inventory must say so, and §2 carries them as **cited names, not effort.**

**Independently falsifiable**: a deal closing without clearing a named gate, or a gate
resolving from a source other than 001's DA-18 sequence. *The gates are 006's to date; 011
reports the outcome and grades the position.*

**wrong_if**: `metric=count_of_deal_securities_closing_without_clearing_a_named_gate threshold=0 source=006_artifact_FCC_8-K_and_merger_proxy_disclosures op=>`

**Consumes (006)**: the gate chain, its expected dates, and the two deal spreads —
`006/spec.md` §1b P4 and P5 — **cited from §3b, generating no tasks by design.** *(This field
is not parsed by `plan_audit` or `tasks_md`; §3b states why.)*

---

### Pillar 6 — Strategies 5–7 are watch items with named triggers, not positions (Priority: P6)

Three strategy candidates **cannot be sized**, and the honest output is a watch list with
the specific event that would change that — not a papered-over position. **Strategies 5 and
6 were converted from 011's work to citations at the re-specification round (§0a);
strategy 7 remains 011's own.**

| # | Strategy | Why it cannot be sized | **The trigger that would change it** |
|---|---|---|---|
| 5 | **Licensed-asset play** — own the licence with diversified demand | Premise `DEMONSTRATED` ($19.6B EchoStar mark; IRDM profitable) but the falsifier — a new entrant granted primary spectrum without acquiring it — is **`UNRESOLVABLE-FROM-PLATFORM`** (FCC IBFS / ITU not in the corpus). **⚠️ Owned by 006** — its P2 prices the licensed asset separately — so 011 **cites the disposition and does not re-open the question** | A transferable **$/MHz-pop** basis, or registry access — **006's to detect** |
| 6 | **Unpriced duopolies** — solar cells, liquid engines, solid motors | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — the structure is `DEMONSTRATED`, the *price* is not disclosed by either parent. **⚠️ The solar-cell leg is owned by 008** (solar-cell duopoly and pricing power, §0a), and the ladder's extension is 008's with it | A unit disclosure from RKLB/SolAero, BA/Spectrolab, or a comparable transaction — **008's to detect** |
| 7 | **Demand asymmetry** — pharma demand 73× the space cohort | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — value-per-kg and cost-per-kg returned **do not exist publicly at all** (Varda private; UTHR immaterial to a $783M/quarter issuer). **011's own — no other thesis owns the demand side** | Any value/kg or cost/kg figure; a Varda listing or disclosure |

**Why this pillar exists**: 001's most useful methodological output was that its three
unanswerable falsifiers failed for **three different reasons**, each with a different
remedy. The same discipline applies here: a watch item with a named trigger is a
different object from a position, and conflating them is how a research program acquires
positions it cannot defend.

**What 011 still executes here**: **strategy 7's disposition** — a `risk`-skill call, not
an arithmetic one. Which of the constitution's two unresolvable classes applies to the
surviving watch item, and **what event would reclassify it into a sized candidate**, is
011's judgement to make and to date. Rows 5 and 6 are cited dispositions: **011 reports
006's and 008's classes, and generating a task on either would be re-opening work §0a
assigned elsewhere.**

**Independently falsifiable**: any of the three triggers occurring, converting a watch
item into a sized candidate. *The first two are 006's and 008's to report; 011 owns the
third.*

**wrong_if**: `metric=count_of_watch_items_with_a_named_resolving_trigger threshold=3 source=this_thesis_artifact op=<`

**Subscribed**: `UTHR × unit-economics`, `UTHR × risk`

**Consumes (006 / 008)**: strategy 5's licensed-asset disposition is **006's**
(`006/spec.md` §1b P2 — `PENDING — owned by 006`); strategy 6's solar-cell leg is
**008's** (`008/spec.md` §3 item 5 — `PENDING — owned by 008`; its spec not yet frozen) — **both cited from
§3b, generating no tasks by design.** *(This field is not parsed by `plan_audit` or
`tasks_md`; §3b states why.)*

---

### Pillar 7 — The book is sized, and the theme cap binds before the sub-sector cap (Priority: P7 — **BLOCKED on 005–010**)

**⚠️ The block was re-scoped at the re-specification round: it is 005–010, not 004–010.**
**004 has landed** — 21 artifacts, a `_cross` SOTP and synthesis, and a `challenge.md` whose
four HIGH findings are all `entity_claims` schema defects with **the anchor's arithmetic
intact** — so the anchor is a usable sizing input now, not a pending one. Its published rows
carry explicit boundaries naming **005, 006 and 009** as their permitted consumers, and
**011 is not among them**: 011 sizes against the 005–009 rankings, and quotes the anchor only
through §0b row 15.

**The strategy**: construct and size the book under the Risk Framework: ≤12 positions,
4% default / **2% binary** / 6% max single, ≤25% per sub-sector, **≤40% theme**, ≤15%
macro-driven, 30% thesis-driven stop.

**Why it is last and why it is blocked**: it is the only pillar that needs the segment
theses. In a **single-theme book the 40% theme cap binds before the 25% sub-sector cap** —
and the arithmetic of that, not the idea generation, is what forces cuts. Which names
must be cut cannot be known before the segment theses rank them. **And three of the names
011 would previously have sized on its own arithmetic — PL, YSS, RKLB — are now sized on
005's and 006's rankings instead (§0a, §3b), which makes the block stricter than it was: 011
cannot substitute its own break-even screen for 005's ranking.**

**The claim**: the book's binding constraint is the theme cap, the arithmetic is shown
rather than asserted, and every position carries a dateable catalyst within 180 days
with its expected date and source — **where a catalyst cannot be dated, the position
cannot be sized against it.**

**Independently falsifiable**: a book satisfying the Risk Framework whose positions lack
dated catalysts, or whose theme-cap arithmetic is violated.

**wrong_if**: `metric=count_of_positions_without_a_dateable_catalyst_within_180_days threshold=0 source=constitution_Methodology_Foundation_catalyst_requirement op=>`

**Subscribed**: `SPCX × ratio-analysis`, `KRMN × ratio-analysis`, `VRT × ratio-analysis`

**Consumes (005–010)**: the segment rankings this pillar sizes against — **005** (space
pure-plays: runway and the break-even ranking), **006** (connectivity and spectrum: the
operator margins and the gate chain), **007** (diversified primes), **008** (supply chain),
**009** (enabling layer), **010** (microgravity) — **cited from §3b, generating no tasks by
design.** *(This field is not parsed by `plan_audit` or `tasks_md`; §3b states why.)*
`RKLB × ratio-analysis` was removed with them: RKLB is a cited name under §0a, not an 011
name.

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
001–004's findings and grades positions rather than analysing businesses afresh. Weights are
analytical effort, not positions; **P7 sizes, and it is blocked.**

**⚠️ Re-cut at the re-specification round (§0a): two tables, because 011 does two different
things now.** The **executed** names are the ones 011 still researches; the **cited** names
are the ones **005, 006 and 008 own**, carried here so the strategy inventory stays complete
and so a reader can see **who owns each question**. The cited table is **deliberately four
columns** — see §3b for why that shape is load-bearing rather than cosmetic.

**§2a — Executed names (011 researches these; they carry the matrix and the task budget)**

| Ticker | Company | Sector | Role in this thesis | Weight |
|---|---|---|---|:---:|
| HEI | Heico | industrial.aerospace_defense | **Strategy 1** — the ladder's top rung; the dilution case | 14% |
| KRMN | Karman Holdings | industrial.aerospace_defense | **Strategy 1 + the only genuine "both" name** | 14% |
| WWD | Woodward | industrial.aerospace_defense | Strategy 1 — the middle rung | 7% |
| TDG | TransDigm | industrial.aerospace_defense | Strategy 1 — the pricing-power control | 7% |
| VRT | Vertiv | industrial.machinery | **Strategy 3** — the terrestrial thermal enabler | 13% |
| NVDA | NVIDIA | tech.semiconductors | Strategy 3 — compute silicon | 9% |
| MSFT | Microsoft | tech.platform_internet | Strategy 3 — the capex datum | 11% |
| GOOG | Alphabet | tech.platform_internet | Strategy 3 — Suncatcher, the orbital aspirant. **Query as `GOOG`, never `GOOGL`** | 7% |
| UTHR | United Therapeutics | med.medicines_biotech | **Strategy 7** — the demand-asymmetry watch item, and the only watch item 011 still dispositions | 9% |
| SPCX | SpaceX | industrial.aerospace_defense | **The anchor the whole main line is measured at** — cited from 004, never re-valued | 9% |

Weights sum to **100%** and measure **analytical effort**. The cited names carry **no
weight**, because 011 assigns them no effort — that is the difference between the two
tables, stated as arithmetic.

**§2b — Cited names (owned by 005 / 006 / 008; 011 hosts no work on their questions)**

| Ticker | Company | Owned by | 011 uses it for |
|---|---|---|---|
| PL | Planet Labs | 005 | Strategy 2's canonical case — break-even **1.69×**, cited from 001 §4.2 via 005 P3 |
| YSS | York Space Systems | 005 | Strategy 2's **2.86×** case — same citation |
| RKLB | Rocket Lab | 005 / 006 | Strategy 2's runway ranking (005); the IRDM acquisition's gate chain (006) |
| FLY | Firefly Aerospace | 005 | Strategy 2 — highest R&D intensity in the universe; **the DA-26 census counterexample** |
| LUNR | Intuitive Machines | 005 | Strategy 2 — pre-profit, capital-hungry |
| IRDM | Iridium | 006 | Strategy 4's deal security; strategy 5's diversified-demand licence |
| GSAT | Globalstar | 006 | Strategy 4's deal security; **the monopsony case — `−7.37%`, corrected by 003** (§0c) |
| SATS | EchoStar | 006 | Strategy 5 — the $19.6B spectrum mark (§0b row 11); 006 P2 prices the licensed asset |

**Every row above carries four cells, and that is the mechanism** (§3b): `plan_audit.py`
parses a universe row only when it has **five or more cells**, and `tasks_md.py` reads a task
only from the five-plus-cell matrix shape. A four-column row is therefore **legible to a
reader and inert to both tools** — which is what *"cite, don't re-derive"* has to mean inside
a workspace whose audit tooling **has no exclusion mechanism at all** (Q-10).

**Two operational traps carried forward, because they are 011's own and cost nothing to
keep**: **GSAT files under `tech.tech_hardware`, not telecom — a telecom-keyed screen
silently drops it**; and **GOOG must be queried as `GOOG`, never `GOOGL`**. Neither is a
research question and neither is an owner's to maintain.

**Recorded for whoever runs `clarify_scan.py` next — this re-cut changes the scanner's
noise, not its findings.** The scanner's §2 heuristic is *"five or more columns, and the
fifth must be a substantive rationale"*; it fires **10 `universe_no_rationale`** candidates
on §2a (it reads the **weight** cell as the rationale — a pre-existing misfire, unchanged by
this round) and will fire **8 `universe_short_row`** candidates on §2b, one per cited name.
**Both sets are answered by Q-10 and are not work to be reopened**: the short rows are the
**exclusion mechanism**, and a scanner that flags the mechanism as a defect is the tooling
confirming §3b's premise that it has no way to express *"cited"* except by shape.

**Excluded by design:** the `NOT_READY` names (including **MOG-A** and **ENS**, which
carry corpus cases but no coverage) and the `PARTIAL` names (ASTS, VSAT, AMZN, AAPL,
TRMB, GRMN, PLTR, LLY), which require manual sector assignment. The foreign-listed tier
(Eutelsat, Avio, SKY Perfect JSAT, Astroscale) is **excluded by the Research Scope
Constraints** and admissible only as read-through — which makes the Cross-Listed Biotech
analogue in §1c a *shape* match with no purchasable instrument, and that must be said.

## 3. Skill Deployment Matrix

### 3a. Executed — the parsed matrix (`plan_audit` I1–I4 and `tasks_md` read **this** table)

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|:---:|---|:---:|---|
| business-model | equity-research-core | Standard | HEI, KRMN, WWD, TDG, SPCX | none | **Strategy 1's dilution quantification** — space revenue share beside margin (**P2**); the main line's anchor reading (**P1**) |
| unit-economics | business-intelligence | Standard | VRT, UTHR | none | **Strategy 3's** terrestrial economics (**P4**); the 73× demand test and strategy 7's disposition (**P6**) |
| secular-trends | equity-research-core | Standard | NVDA, GOOG | none | **Strategy 3's** orbital-vs-terrestrial evidence (**P4**) |
| competitive | equity-research-core | Standard | KRMN, VRT | none | The within-OEM counter-argument (**P1**, **P2**); the terrestrial layer's competitive read (**P4**) |
| risk | equity-research-core | Standard | UTHR | none | Disposition class for the one surviving watch item (**P6**) — **not** the deal gate chain, which is 006's |
| recent-quarter | equity-research-core | Standard | MSFT, SPCX | none | Freshness anchor for every figure this thesis quotes (**P1**, **P4**) |
| ratio-analysis | quantitative-analysis | Light | HEI, KRMN, SPCX, VRT | none | **P2's** dilution arithmetic; **P7's** theme-cap arithmetic, when unblocked |

> **Coverage invariant.** Every executed ticker in §2a appears at least once above; every
> `Subscribed` pair in §1b generates at least one task; and **no §2b name appears in a
> five-cell row anywhere** — the cited names generate no tasks at all. Verified by
> `tools/plan_audit.py` (I1–I4).

**Budget**: this matrix yields **18 `ticker × skill` rows**, down from **30** before the
re-specification round. `max_tasks: 30` in `thesis.md` still holds, and the headroom is now
deliberate: **the removed rows are the work 005, 006 and 008 own** (§3b). P7's block reserves
**4** rows for when 005–010 land.

### 3b. Consumed — cited, not executed (read by **neither** tool, by design)

| Consumed from | Artifact consumed | 011 uses it as | Owner's grade |
|---|---|---|---|
| **005** P1, P3 | `005/spec.md` §1b — the runway MVV and the break-even instrument | The fixed-cost-absorption screen and its multiples (**P3**) | `PENDING` — 005 specified, not yet run |
| **006** P1, P4, P5 | `006/spec.md` §1b — operator margins by segment; the deal spreads and the gate checklist | The gate chain and the operator rungs (**P5**, **P1**) | `PENDING` — 006 specified, not yet run |
| **006** P2 | `006/spec.md` §1b — the licensed asset priced separately | Strategy 5's disposition (**P6**) | `PENDING` — 006 specified, not yet run |
| **008** §3 item 5 | `008/spec.md` §3 — the ladder extended to the full Tier 3 list | The ladder's shape beyond the 8 measured names; the solar-cell leg (**P1**, **P6**) | `PENDING` — 008's spec **not yet frozen**; no tasks may be generated from it |
| **003** §E-11, §3, §6 | `003/_cross/value-pool-map.md`; `003/_cross/launch-cost-curve-value-migration_synthesis.md` | The corrected GSAT rung; the bimodality measurement; the deal multiples (**P1**) | `DEMONSTRATED` (corrected) |
| **001** §4.2 | `001/_cross/technology-baseline_synthesis.md` | The measured break-even values 005 reframes per name (**P3**) | `DEMONSTRATED` |

**Why this table has four columns, and it is not a style choice.** `plan_audit.py`'s
`parse_matrix` reads a row only when it has **five or more cells**; `tasks_md.py`'s
`matrix_pairs` applies the same five-cell test. **A four-column table is therefore invisible
to both** — which is exactly what *consumed* has to mean here, because **neither tool has an
exclusion mechanism**: `plan_audit` I1 asserts `universe ⊆ matrix` with no way to mark a name
excluded, and any five-cell row naming a ticker becomes a task. **A different column shape is
the mechanism that makes "cited" mean cited** — the same device 004 uses for its own consumed
table, and the reason §2b is four columns as well.

**And the horizon on the `PENDING` rows, stated rather than implied:** where an owner has not
run, 011 cites **the owner's spec** and the **upstream measurement** — never a placeholder
artifact path, and never its own computation standing in for the owner's. **When 005, 006 or
008 runs, the citation is updated to its artifact; until then the strategy inventory carries
the row as open, with the owner named.** A reader is never shown 011's number in the owner's
place.

## 4. Depth Tiers

| Tier | Skills | mode-set | Tickers | Output |
|:---:|------|---|--------|------|
| Standard | business-model, unit-economics, secular-trends, competitive, risk, recent-quarter | essentials_modes | As listed in §3a | The main line, four actionable strategies, three watch items — **P3, P5 and the first two rows of P6 reported as citation (§3b), not computed here** |
| Light | ratio-analysis | essentials_modes | HEI, KRMN, SPCX, VRT | Dilution arithmetic (**P2**); theme-cap arithmetic (deferred with P7) |

**§3b's consumed rows are in no tier**, by design: a tier is a *mode-set for work this thesis
executes*, and a consumed artifact has no mode-set because **011 runs no mode on it.**

## 5. Cross-Cutting Analysis

- **The main line** is the cross-cutting output and the program's governing argument.
- **The strategy inventory** — 7 candidates, 4 actionable, each with its dilution or its
  blocking condition stated. **Three of the seven arrive as citations** (strategies 2 and 4,
  and 5–6's dispositions); **the inventory is 011's, the instruments are not** (§0a, §3b).
- **The ownership rule (§0a) is itself cross-cutting**: it is the programme's arbitration
  table, and 011 is where it is instantiated and auditable — the place a future overlap is
  resolved by lookup.
- **Macro sensitivity: high, and immediately binding.** This is the only thesis that
  turns findings into positions. The constitution's bias is **NEUTRAL** precisely because
  the universe is long-duration and the 10Y sits at **4.80%** with hike risk priced. **A
  NET_LONG expression of the main line is a bet on duration, not on space.** P7 must size
  through that lens or say why not.
- **Constitution interaction**: P4 governs every grade; P11 governs P5; the Data-Integrity
  Register governs every figure inherited from XBRL — **and DA-23 has already bitten this
  thesis once, through the GSAT rung (§0c)**; P10 forbids underwriting orbital compute; the
  Risk Framework's theme cap is P7's binding arithmetic; **§Universe Definition's cross-tier
  dependency rule is §0a's ownership table, instantiated.**

## 6. Output Contract

- **Per-ticker (dispatcher-resumable)**: `artifacts/{ticker}/{YYYY-MM-DD}_{skill}_{mode}.md`
  — suffix **must** be `_{skill}_{mode}.md`.
- **Cross-cutting (not resume-tracked)**: `_cross/{name}.md`.
- **Primary artifact**: `_cross/main-line-and-strategy-inventory.md` — the governing
  argument, its falsifiers, and the 7-strategy table with honest actionability grading.
  **This is the artifact the program is organized around.**
- **Deferred artifact**: `_cross/position-sizing.md` — written only when P7 unblocks.
- Snapshot: `snapshots/011-idea-generation/{YYYY-MM-DD}_thesis.md`
- **P11**: every artifact on **IRDM or GSAT** must set `deal_security_basis` — **including
  the cited ones**: §0a removed 011's *work* on those names, not the P11 tagging duty.
- **Citation duty (§0a)**: the primary artifact reproduces **§3b's consumed table** with each
  owner's grade, and **every `PENDING` row names its owner**. A cited figure that arrives
  with a correction history carries it — **the GSAT rung is written `−7.37%`, named as
  corrected by 003, in every artifact that quotes it** (§0c).

## 7. Thesis Phases

| Phase | Tasks | Duration | Dependencies |
|:---:|------|:---:|------|
| 1 — The main line (P1) | Test the four findings for a common mechanism; state the governing claim; register its falsifiers — **at the corrected GSAT rung (§0c)** | Week 1 | **001–004** (all landed) |
| 2 — Dilution (P2) | Space revenue share beside margin for the component layer; grade the label | Week 2 | Phase 1 |
| 3 — The screen (P3) — **citation** | Take 005's instrument and its multiples as cited; grade the label (*timing, not space*); carry the owner as `PENDING` | Week 3 | Phase 2 · **005's spec** |
| 4 — The terrestrial expression (P4) | Grade the strongest-evidence/weakest-purity trade honestly | Week 4 | Phase 3 |
| 5 — Deals and watch items (P5, P6) — **citation** | Cite 006's gate chain and 008's duopoly disposition; **disposition strategy 7 — 011's own**; name triggers for all three | Week 5 | Phase 4 · **006's, 008's specs** |
| 6 — Publish | `_cross/main-line-and-strategy-inventory.md` — with §3b's consumed table, and every `PENDING` row owner-named | Week 6 | Phase 5 |
| 7 — Sizing (P7) — **BLOCKED** | Theme-cap arithmetic; catalyst calendar; position sizes | on unblock | **005–010** (004 landed) |

## Clarifications

Recorded by `agentii.clarify` — **three rounds**. Rounds 1 and 2 were on **2026-09-18, both
invoked on 002** and resolved by moving the main line here; round 3 is the
**re-specification round of 2026-09-19**, invoked on this thesis. On **all three** rounds the
scanner reported **0 mechanical candidates**; every question below was raised manually, since
the deterministic scan cannot see intent, and neither could it see a claim that needed
narrowing, a constitution table that contradicted itself, or **a figure that four theses
carried and none had re-read against the filing.**

**Round 1** established *where* the main line lives. **Round 2** pressure-tested *whether
it is true* and found a constitution defect the first round missed. **Round 3** found **a
sign error and five ownership collisions** — §0a and §0c are its two dispositions.

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
  there is nothing to size. ***(Round 3, Q-10, sharpens this: strategy 6's solar-cell leg
  is 008's question, so "don't attempt it here" is now an ownership boundary rather than a
  self-denying ordinance — 011 cites 008's disposition instead of declining the work.)***

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

- [2026-09-19] **Q-9 (round 3, re-specification — the corrected rung)**: *"011 carries
  `GSAT 7.4%` as the ladder's bottom rung, graded `DEMONSTRATED`, in §1 and again in §2.
  Is that figure right?"* → **A: no — it is the DA-23 sign strip, and the filed value is
  `−7.37%`.** GSAT's Q2 2026 operating result is a loss of **$(4,775)k on $64,772k**
  revenue, and the filed margin prints **`(7.37)%`**; the served figure is the same
  magnitude with the sign stripped. **Traced end to end before changing anything**: 001
  originated it (`001/artifacts/GSAT/2026-09-18_2040_competitive_methodology.md` — the row
  `| Operating margin | 7.4% | 9.2% | −1.8 pts |`, and the synthesis ladder at
  `001/_cross/technology-baseline_synthesis.md` §4.1), **002 missed it**, **003 corrected
  it** (`003/_cross/value-pool-map.md` §E-11, with the offset systematic across seven
  served facts), and **011 still carried it, graded `DEMONSTRATED`.** **Disposition:**
  corrected in **both** places, **cited as corrected with 003 named as the correcting
  source** — not silently swapped — and the monotonicity claim **restated so it is true at
  the corrected value** (§0c). **Which reading changes:** the *ordering* survives and the
  axis is **strengthened** (maximum concentration produces a **negative** margin, not a
  thin one); what dies is the *"thin positive margin"* reading and the derived comparison
  `9.2% → 7.4%, −1.8 pts`, which at the filed values is **`+9.15% → −7.37%` — a −16.5 point
  swing to a loss inside the year**; and *"monotone"* as a smooth staircase does not
  survive 003's re-measurement of the shape as **bimodal** (22.76% vs 11.25%). **011 now
  asserts the ordering and the sign, and neither the smooth decline nor the shape.**
  **⚠️ Recorded, not fixed — out of this thesis's scope:** the constitution's DA-23 register
  row still lists **GSAT among the issuers it calls "Clean — subtotal-level only"**, which
  conflicts with 003's finding that GSAT's *served* operating income is the stripped sign.
  **The constitution is not this thesis's to edit**; the conflict is reported to the
  programme. *(And the correcting source is the artefact of record: a future reader should
  not re-derive it from 001.)*

- [2026-09-19] **Q-10 (round 3, re-specification — ownership, and how a citation is made
  real)**: *"P3, P5 and P6 re-derive questions five other theses own — same instrument, same
  worked numbers, same names — and §2's matrix lists tickers 005 and 006 own. How does this
  thesis cite another thesis's work inside tooling that has **no exclusion mechanism**?"* →
  **A: three dispositions, all in §0a and §3b.**
  **(i) The arbitration rule is written down.** §0a carries the programme's ownership table —
  each contested question with exactly one owner — as **v1.6.0's cross-tier dependency rule
  instantiated**, so a future overlap is resolved **by lookup rather than negotiation**.
  **(ii) The work moves to the owner, and the owner is named, including when it has not run.**
  P3's break-even computation is **005's**, P5's gate chain is **006's**, P6's solar-cell and
  licensed-asset dispositions are **008's and 006's**; none generates a 011 task. **Where the
  owner has not run, 011 cites the owner's spec and the upstream measurement and carries the
  row as `PENDING — owned by 00X`** — it does **not** fill the gap by computing the number
  itself. **Checked against 005's spec rather than assumed:** the shared instrument and the
  worked multiples (`PL 1.69×`, `YSS 2.86×`) live in **005's break-even pillar** — 005 P3 as
  its spec currently numbers it, bound to its P1 funding-runway pillar; **005 P2 is its
  value-capture ranking and carries neither the instrument nor the numbers.** The citation
  therefore names **005 P1 and P3**, by question as well as by number so it survives 005's
  own re-specification.
  **(iii) The citation is made *mechanical*, not rhetorical.** §2 splits into **§2a executed**
  (five-cell rows — `plan_audit` I1–I4 and `tasks_md` parse these) and **§2b cited**
  (**four-column** rows — below both tools' five-cell threshold, so they generate no task);
  §3 splits into **§3a executed** and **§3b consumed**, the latter in the same four-column
  shape. **The column count is the exclusion mechanism the tooling does not have**: I1 has no
  way to mark a name excluded, and any five-cell row naming a ticker becomes work. Net effect:
  **18 matrix rows, down from 30**; the twelve removed rows are exactly the ones 005, 006 and
  008 own. **A reader sees every name and every question; only 011's own work is scheduled.**
