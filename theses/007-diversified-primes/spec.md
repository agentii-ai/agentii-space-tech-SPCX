# Research Thesis: 007 — Tier 3a: Diversified Primes & Defense-Space

**Constitution Ref**: constitution.md v1.6.0 (`constitution_pin: 1.6.0`)
**Created**: 2026-09-18 · **Spec written**: 2026-09-19 (placeholder replaced)
**Status**: **PLANNED — NARROWED. One surviving research question.** Not frozen.
**Wave**: 2 (activates when a slot opens under `max_theses_active: 6`)
**板块**: Tier 3a · **Binding constraint**: `DEMAND`

> **This thesis is narrower than its ID suggests, and the narrowness is the finding.**
> Its original question — *do the primes offer a better risk-adjusted route to the same
> secular driver than the pure-plays?* — is **already answered negatively by 001**, and
> §0 states that answer before anything else. What survives is a single question about
> **segment disclosure and multiple dilution**, and it survives only because 001 made a
> claim this pass found to be **false**: that LMT is the only prime with a named space
> segment. Three of four do. §8 states the condition under which this thesis closes.

---

## 0. Inherited baseline

**Paths are relative to the workspace root.** Nothing in this table is re-derived.

### 0a. The negative prior — this thesis's question is pre-answered

**001 executed the natural version of this thesis's question and returned a negative.**
The result is stated first, at full strength, because a thesis whose question has already
been answered must say so or it is not a research question:

> *"Four of five primes cluster between 10.1% and 12.4%. That is a tight band for
> companies with very different space exposure — evidence that **consolidated prime margins
> are set by defence programme economics, not by space participation.** … **prime operating
> margin carries no information about space exposure in this universe. Any thesis
> attempting to rank primes by space leverage using margin would be measuring something
> else.**"*
>
> *"**RTX's role in the thesis is therefore as a scale datum, not a space exposure.** Its
> inclusion tests whether adding primes adds information; on this evidence, **it does
> not.**"*
> — `theses/001-technology-baseline/artifacts/RTX/2026-09-18_1239_supply-chain_methodology.md` §1–2

**Carried to Phase 6 as a recommendation, not a caveat**: *"Tier 3 should be described as
**context, not evidence** — it demonstrates the sector's industrial base and its financial
capacity, but contributes no pricing signal on any critical component."*

**Consequence.** The framed question — *is the primes' space exposure diluted below the
threshold where it moves the consolidated multiple?* — is **not open at the margin axis**.
001 closed it. `DEMAND` as a candidate binding constraint is likewise unsupported: 001
found the space-segment margin set by programme economics, and no evidence was produced
that budget or award flow binds these names.

### 0b. Inherited results this thesis consumes

| Inherited result | 001 artifact | Grade |
|---|---|---|
| **Primes cluster at 10.1–12.4% operating margin regardless of space exposure** — LMT 12.4%, RTX 11.4%, LHX 11.1%, NOC 10.1%; BA 0.6% (now 008's name, out of scope here) | `artifacts/RTX/2026-09-18_1239_supply-chain_methodology.md` §2 | `DEMONSTRATED` |
| **LMT files a Space segment that aggregates satellites, missiles and government space — and therefore does not expose component pricing.** *"Space-as-a-segment does not equal space-supply-chain visibility."* **This closes the hope that adding primes surfaces the solar-cell, engine, motor or launch duopolies** | `artifacts/LMT/2026-09-18_1239_supply-chain_methodology.md` §1 | `DEMONSTRATED` |
| **ULA is equity-method and invisible at both parents** — the launch duopoly is unpriceable from any prime's filings | `artifacts/LMT/…` §2 | `DEMONSTRATED` |
| **Four critical duopolies are structurally unpriced** (solar cells, liquid engines, solid motors, launch) | `_cross/technology-baseline_synthesis.md` §4.5 | `DEMONSTRATED` |
| **The margin ladder places the primes mid-table** — suppliers above (HEI 25.5%, KRMN 19.1%, WWD ~17%), the monopsony supplier below. **The ladder is 008's instrument and 008 owns its monotonicity**; 007 consumes the prime rungs only | `_cross/technology-baseline_synthesis.md` §4.1 | `DEMONSTRATED` for the eight printed rungs; **one rung is now known to be sign-corrupted — see §0c(3)** |
| **The refined rule: component concentration predicts margin when the supplier's revenue spreads across programmes** — the discriminator is whether the supplier depends on a single programme winning | `_cross/technology-baseline_synthesis.md` §4.1; `artifacts/HEI/2026-09-18_2120_…` | `DEMONSTRATED` |
| **LMT, RTX, LHX, NOC are clean at the parent/subtotal level** — with the register's own qualifier that a subtotal-level census cannot support an unqualified `Clean` | constitution §Data-Integrity Register, DA-23 census row | `DEMONSTRATED` at subtotal level only |
| **GSAT's 7.4% rung is a DA-23 sign strip; the filed figure is −7.37%.** Every inherited margin in this spec was checked against this trap; the prime rungs are unaffected (all four are genuinely positive), but the ladder's ordering is not | `theses/003-launch-cost-curve-value-migration/thesis-report.html`; §0c(3) below | `DEMONSTRATED` (003); the ladder's ordering is **contested** |

### 0c. What this spec-writing pass established — three corrections to 001

These were found while checking 001's claims against the platform, not inherited from it.
They are the reason a narrowed thesis survives.

1. **001's claim that *"LMT is the only prime in the universe that reports Space as a named
   segment"* is FALSE — and it is falsified twice.** Dimensional XBRL facts carry a
   **`noc:SpaceSystemsMember`** segment (Q2 2026 operating income **$236M** of **$1,158M**
   total segment operating income; H1 **$471M**) and an **`hrs:SpaceMissionSystemsSegmentMember`**
   segment (Q2 2026 operating income **$290M** of **$942M** — **30.8% of segment operating
   income**). **Three of this universe's four primes file a named space segment with both
   revenue and operating income.** The component-level claim in 0b stands; the
   segment-level claim does not, and it is the one the dilution question needs.
2. **The SOTP surface is real and computable at LMT**: `lmt:SpaceMember` Q2 2026 revenue
   **$3,496M** and operating income **$371M** (**10.6%**), against consolidated operating
   income of **$2,479M on $20,063M** (**12.4%**). **First look: the space segment earns
   BELOW the consolidated margin.** The contract mix explains the mechanism — Space revenue
   is **$2,603M cost-reimbursable against $893M fixed-price** (74.5% / 25.5%), i.e. a
   low-risk, low-return profile by design. This is a first look from filed facts, not a
   pillar result, but it points the thesis at its own falsifier before activation.
3. **Two DA-30/DA-23 basis traps sit directly under any prime SOTP**, and both are new:
   **(a) DA-30, two bases on one concept** — at LMT the segment-sum operating income
   (**$2,162M**) and the consolidated operating income (**$2,479M**) are the **same concept
   on two bases**, differing by an unallocated **$317M** (**12.8%** of the consolidated
   line) with no basis field in the extract. **(b) DA-23 at a corporate line** — at LHX the
   `CorporateNonSegmentMember` line is served as **+$288M**, while segment sum (**$942M**)
   minus consolidated (**$654M**, consistent with 001's 11.1% margin) requires a **$288M
   cost**. Opposite sign, identical magnitude: the strip signature. **Both require 002-grade
   confirmation before being cited as findings.**

### 0d. What 001 did not do — and why a narrowed thesis still exists

001 never asked the **valuation** question. It established that prime margin carries no
information about *space exposure*, and that segment disclosure does not expose *component*
pricing. It did not ask whether a disclosed space segment is **worth a different multiple**
from the entity that contains it, and it did not decompose the segment basis against the
consolidated basis. Those two things are open, they are answerable from filed data at three
names, and they are the whole of this thesis.

### 0e. Validation queue — open before any pillar can fire

| # | Item | State |
|---|---|---|
| 1 | **Confirm `noc:SpaceSystemsMember` and `hrs:SpaceMissionSystemsSegmentMember` against the filed segment notes** (not the dimensional extract alone), and pull NOC's segment revenue to complete the pair | `blocking` |
| 2 | **Separate the segment basis from the consolidated basis** at all four primes; report the unallocated residual as a percentage of consolidated operating income. Do not compute a segment margin from a collapsed denominator (DA-30) | `blocking` |
| 3 | **Re-derive the LHX corporate non-segment line's sign** under the DA-23 component identity before using LHX's segment sum | `blocking` |
| 4 | **Confirm RTX discloses no space segment** (001 asserts it; a negative claim needs a positive search) | `warn` |
| 5 | **Confirm the prime rungs** — LMT 12.4%, RTX 11.4%, LHX 11.1%, NOC 10.1% — came from component-identity-clean figures. 001's LMT artifact showed only an EPS bridge, which the register rules inadmissible as a sign test | `warn` |
| 6 | **Take the ladder correction** — do not consume GSAT's `+7.4%` rung from `PROGRAM.md` or the synthesis; 003 records **−7.37%** | `warn` |

---

## 1. Research Question

**At the three primes that disclose a named space segment, is the space business's
disclosed margin and growth different enough from the consolidated blend that a
sum-of-the-parts exposes value the consolidated multiple cannot — or does the segment
disclosure show the space arm earning at or below the consolidated rate, in which case the
diversified-prime route to space exposure offers nothing and this thesis closes?**

**Stated plainly: the original question does not survive.** *"Do the primes offer a better
risk-adjusted route to the same secular driver?"* was answered by 001 in the negative at the
margin axis, and this spec does not re-ask it. What survives is the **dilution** half,
narrowed to a computable test, and it is 007's because the ownership table assigns
*diversified-prime multiple dilution* here and nowhere else.

---

## 1b. Pillars

**Two pillars, deliberately.** P1 carries the question; P2 carries its precondition. No
third pillar exists that is not already owned by another thesis — see §5.

### Pillar 1 — The space segment is disclosed, and it does not out-earn the entity that holds it (Priority: P1)

**Claim.** Three of the four primes file a space segment with revenue and operating income.
If any one of them shows the segment out-earning the consolidated blend, the consolidated
multiple is mispricing a decomposable business and an SOTP has content. If none does, the
segment disclosure is *confirmatory of dilution rather than corrective to it*, the
diversified-prime route carries no hidden value, and **007's surviving question resolves
negative and the thesis closes (§8).**

**Why this priority.** It is the only open question 001 left, it is answerable per issuer
from one XBRL axis, and it fails fast — the first look (§0c(2)) already points at the
falsifier, which is exactly what a thesis worth running should do.

**Independently falsifiable.** Yes. Segment operating margin and segment revenue are
computable per issuer-quarter from `us-gaap:StatementBusinessSegmentsAxis`, on figures whose
signs are all positive (so DA-23 does not bite) once the basis is separated (P2).

**wrong_if**: `metric=count_of_universe_primes_whose_named_space_segment_operating_margin_exceeds_that_issuer_s_consolidated_operating_margin threshold=0 source=10-Q_segment_note_us-gaap_StatementBusinessSegmentsAxis op=<=`

**Subscribed**: `LMT × sotp-valuation`, `NOC × sotp-valuation`, `LHX × sotp-valuation`,
`LMT × business-model`, `NOC × business-model`, `LHX × business-model`,
`LMT × recent-quarter`, `NOC × recent-quarter`, `LHX × recent-quarter`.

**Boundary conditions that must be reported with any result.** (a) The contract-mix profile
— cost-reimbursable versus fixed-price segment revenue — because it is the mechanism that
predicts the answer: a cost-reimbursable segment *should* earn a stable, low margin, and
finding that is a mechanism, not an anomaly. (b) `DA-21`: each prime's segment boundaries
are its own; LMT's Space is not NOC's Space is not LHX's Space, and no cross-prime
aggregation is admissible. (c) The segment margin is computed on the segment basis, never on
a consolidated denominator.

### Pillar 2 — The SOTP's precondition: the segment basis and the consolidated basis must be separated before any decomposition is arithmetic (Priority: P2)

**Claim.** Every prime's segment-sum operating income differs from its consolidated
operating income by an unallocated residual, and at this universe's primes the residual is
**material** — LMT **$317M** on a **$2,479M** consolidated line (**12.8%**), LHX a
**$288M** corporate non-segment line served with a **stripped sign** (§0c(3)). Until the
basis is named, any segment margin, any SOTP and any "dilution" figure is arithmetic on a
collapsed number.

**Why this priority.** It is not a second question, it is the *precondition* of the first,
and it is the specific thing that makes a segment SOTP fail silently. A thesis that computes
P1 without P2 would produce a number and call it a result.

**Independently falsifiable.** Yes, and cheaply: if the residual is immaterial everywhere,
this pillar fails and P1 can be computed directly.

**wrong_if**: `metric=max_abs_unallocated_residual_pct_of_consolidated_operating_income_across_universe_primes threshold=5 source=10-Q_segment_note_segment_sum_vs_consolidated_operating_income op=<`

**Subscribed**: `LMT × ratio-analysis`, `NOC × ratio-analysis`, `LHX × ratio-analysis`,
`RTX × ratio-analysis`, `LMT × competitive`, `NOC × competitive`, `LHX × competitive`,
`RTX × competitive`, `RTX × recent-quarter`.

**Note on RTX.** RTX has no space segment (001; `warn`-queued at §0e(4)), so it cannot enter
P1. It stays in the universe as P2's **null arm** and as the scale datum 001 designated —
which is a use, not a role.

---

## 1c. Method

Four steps, in order, each gated on the previous.

1. **Basis separation** (P2). For each prime, reconstruct the segment note: segment revenue
   and segment operating income per `us-gaap:StatementBusinessSegmentsAxis`, plus
   `CorporateNonSegmentMember` and `IntersegmentEliminationMember`, and reconcile the sum to
   the consolidated line. Report the residual and its basis explicitly. **No segment margin
   is computed in this step.**
2. **Segment profile** (P1). For each named space segment: revenue, operating income, margin,
   and the contract-mix split (cost-reimbursable / fixed-price) where the segment note
   carries it. Report on the segment basis.
3. **The comparison.** Segment margin against the issuer's consolidated margin, on the
   reconciled bases. Count how many primes clear the threshold in P1's `wrong_if`.
4. **The valuation step.** Only if step 3's count is non-zero: apply a comparable multiple to
   the segment and compare the implied attribution against the consolidated market multiple.
   This step runs at the `late` market-data stage (§3) and is the only step that requires a
   price.

---

## 2. Universe Definition

**Four names.** Weights are **analytical effort, not positions** — position sizing is fixed
by the Concentration Rule and the Risk Framework, not by this table. Market Data Stage is
`none` for every row except the valuation step, which is `late` (see §3).

| Ticker | Company | Sector | Sub-sector (Sector Preferences) | Weight | Role in this thesis |
|---|---|---|:---:|---|
| LMT | Lockheed Martin | industrial.aerospace_defense | Diversified Primes & Defense-Space | 30% | **The reference disclosure.** `lmt:SpaceMember` carries revenue and operating income; the largest and most stable consolidated base; ULA sits equity-method inside it and is **not** decomposable — **P1, P2** |
| LHX | L3Harris | industrial.aerospace_defense | Diversified Primes & Defense-Space | 25% | **The highest space-segment share of the four** (`hrs:SpaceMissionSystemsSegmentMember` = 30.8% of segment operating income) and the **worst basis contamination** — a corporate non-segment line with a stripped sign. Aerojet is **not** in scope here (see §5) — **P1, P2** |
| NOC | Northrop Grumman | industrial.aerospace_defense | Diversified Primes & Defense-Space | 25% | **Second named space segment** (`noc:SpaceSystemsMember`); also carries programme-level dimensional facts inside Space Systems, which is more granularity than 001 credited — **P1, P2** |
| RTX | RTX | industrial.aerospace_defense | Diversified Primes & Defense-Space | 20% | **Null arm and scale datum.** No space segment; space sensors sit inside Collins and Raytheon. In the universe to prove the negative claim is a search result, not an assumption — **P2 only** |

**BA is not in this universe.** Boeing's Spectrolab leg is a **Tier 3 supply-chain**
question and belongs to **008**, which holds both legs of the solar-cell duopoly. 007 does
not cite BA's 0.6% operating margin, does not carry BA in any pillar, and does not re-open
the 0.6% finding.

**Names deliberately absent.** Every other Tier 3 member (HWM, TDG, HEI, WWD, CW, KTOS,
MRCY, BWXT, AVAV, TER, MOG-A, TDY, ATRO, TRMB, GRMN, PLTR) sits in 008's universe, not this
one. **The margin ladder is 008's instrument** and 007 does not extend it; the four prime
rungs enter 008's ladder as a **declared cross-thesis input**, per the constitution's rule
that a name spanning functions is set by primary revenue and never absorbed as a pillar of
the host thesis.

---

## 3. Skill Deployment Matrix

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|---|---|---|---|
| `sotp-valuation` | quantitative-analysis | Deep | LMT, NOC, LHX | `late` | The decomposition itself — segment value against consolidated value (P1, step 4) |
| `business-model` | equity-research-core | Standard | LMT, NOC, LHX | `none` | Contract mix: cost-reimbursable vs fixed-price segment revenue, i.e. where programme risk sits (P1) |
| `ratio-analysis` | quantitative-analysis | Deep | LMT, NOC, LHX, RTX | `none` | The basis reconciliation — segment sum vs consolidated line, residual as a % of the consolidated line (P2) |
| `recent-quarter` | equity-research-core | Standard | LMT, NOC, LHX, RTX | `none` | The segment note per quarter; DA-26 (Q4 row carries ANNUAL) and DA-27 (label offset) apply at every issuer |
| `competitive` | equity-research-core | Standard | LMT, NOC, LHX, RTX | `none` | Prime-vs-prime on the segment definition, and the pure-play alternative the question is really about (P1, P2) |
| `peer-bench` | equity-research-core | Standard | LMT, NOC, LHX, RTX | `late` | The consolidated multiple against the component-layer multiples — the comparison that decides whether a re-rating is even available |
| `comps` | quantitative-analysis | Light | LMT, NOC, LHX | `late` | The standalone multiple a space arm would attract; the denominator of the dilution test |
| `reverse-dcf` | quantitative-analysis | Light | LMT | `late` | What growth the consolidated price already implies — and whether it can be met without the space segment |
| `risk` | equity-research-core | Light | LMT, NOC, LHX, RTX | `none` | Fixed-price development charges, the primes' characteristic failure mode, read per segment rather than per company |

**Market Data Stage.** Filings-based work is `none`. The valuation step needs prices, and a
keyless NASDAQ feed is available to the platform — **do not assume `none` for
`sotp-valuation`, `comps`, `peer-bench` or `reverse-dcf`; check the skill registry's true
stage per skill before scheduling.** 004 established the same for its SOTP and reverse-DCF
work.

---

## 4. Depth Tiers

| Tier | Skills | Names | Note |
|---|---|---|---|
| **Deep** | `sotp-valuation`, `ratio-analysis` | LMT, NOC, LHX | The three names that can carry P1 |
| **Standard** | `business-model`, `recent-quarter`, `competitive`, `peer-bench` | LMT, NOC, LHX, RTX | RTX is Standard on P2 only |
| **Light** | `comps`, `reverse-dcf`, `risk` | as marked | Valuation step, conditional on P1 clearing step 3 |

---

## 5. Cross-Cutting — ownership boundaries, and what 007 may not absorb

Each question has exactly one owner. This thesis is the smallest in the programme and the
boundaries are most of what keeps it from growing into another thesis's work.

| Question | Sole owner | 007's relationship to it |
|---|---|---|
| IRDM/RKLB deal gate chain | **006** | Not in universe |
| Operator margins by segment | **006** | **006's**; 007 computes segment margins at primes only, never at operators |
| Financing runway / fixed-cost absorption | **005** | **005's**; 007 does not compute break-even revenue multiples |
| Solar-cell duopoly & pricing power | **008** | **008's**, both legs; BA is out of 007's universe for this reason |
| BA / Spectrolab | **008** | Not in universe |
| The margin ladder's monotonicity | **008** | 007 **supplies** the four prime rungs as a declared input and does not extend, rank or reconcile the ladder |
| Liquid-engine and solid-motor duopolies (Aerojet/LHX, NOC) | **008** | In universe as companies, **out of scope** as duopoly questions; 007 does not price propulsion |
| The F2 nuclear escape hatch (BWXT) | **009** / 001 PIL-2 | Not in universe |
| **Diversified-prime multiple dilution** | **007** | **This thesis's only owned question** |

**Declared cross-thesis inputs.** 008 consumes LMT/NOC/LHX/RTX segment-independent operating
margins for its ladder; that input is a datum, not a claim, and it does not make 007 a
contributor to 008's pillar. 002 owns the DA-23 census and every block in §0e.

---

## 6. Output Contract

The thesis produces, at minimum:

1. **A basis-reconciliation table** — per prime: segment sum, corporate non-segment,
   intersegment elimination, consolidated operating income, and the unallocated residual as
   a percentage of the consolidated line, with the basis named on every column.
2. **A segment profile per prime** — space-segment revenue, operating income, margin and
   contract mix, on the segment basis, with the segment's own definition quoted (`DA-21`).
3. **A named count** against P1's `wrong_if`, reported whichever way it falls.
4. **A disposition.** If the count is zero, the SOTP has no content and §8 compels a close
   rather than an extension.
5. **A negative-disclosure register** for RTX — what was searched, and what was not found.

---

## 7. Thesis Phases

| Phase | Content | Gate |
|---|---|---|
| 1 | §0e validation queue cleared — especially (1), (2), (3) | Blocks everything |
| 2 | Basis separation at all four primes (P2) | P2's `wrong_if` is evaluated here |
| 3 | Segment profiles at LMT, NOC, LHX (P1) | Inputs P1 |
| 4 | The comparison and the count (P1) | **The decision point** |
| 5 | The valuation step — **only if the count is non-zero** | Conditional |
| 6 | Output contract, and either a finding or a close | — |

---

## 8. Close Condition — stated before activation, not after

**If P1's count is zero — no prime's named space segment out-earns its consolidated margin —
then the diversified-prime route carries no decomposable value, 001's *"context, not
evidence"* is confirmed at the valuation axis as well as the margin axis, and 007 must
**close** rather than acquire new pillars.** On that outcome the thesis's surviving content
is a single paragraph for 008's ladder (the four prime rungs, on a reconciled basis) and no
further work is authorised. **The only permitted extension is a third pillar that is
*found* in Phase 3 and falsifiable on filed data — not one written to fill the space left by
a question 001 already answered.**

**Clarifications**

- **2026-09-19** — Placeholder replaced. Original scope (five primes, four prose
  workstreams, an unpopulated matrix) removed: BA deleted from the universe per the
  ownership table; the pre-answered question stated at the top of §0 rather than hidden
  behind *"to be completed on activation"*; pillars cut to two; a close condition added.
  Constitution reference moved v1.4.0 → v1.6.0, under which the 007/008 split is
  constitutional and deliberate.
- **2026-09-19** — §0c records three corrections to 001 found during this pass (a false
  exclusivity claim about segment disclosure; the first SOTP-computable segment figures; two
  basis traps). All three are `blocking`/`warn` in §0e before use.
