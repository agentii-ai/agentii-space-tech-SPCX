# Research Thesis: 005 — Tier 1: Launch, Spacecraft & In-Space Services

**Constitution Ref**: constitution.md v1.6.0 (`constitution_pin: 1.6.0`)
**Created**: 2026-09-18 · **Re-cut**: 2026-09-19 (v1.6.0 tier re-cut)
**Status**: Active
**板块**: Tier 1 · Wave 1
**Time Horizon**: 2026-Q4, terminating at the wave-2 hand-off to 006/008/009, or at the
RKLB/Iridium close (expected mid-2027), whichever comes first
**Depends on**: `001-technology-baseline` (pin 1.2.0 — inherited, §0), `002-evidence-validation`
(validated input set), `003-launch-cost-curve-value-migration` (the launch-cost curve and the
value-pool map this thesis ranks against), `004-tier0-spacex-anchor` (the only anchor row this
tier may price off)
**Binding constraint**: **`MULTI` — DECLARED.** The P3 compromise, stated in full in §1.
It is not an omission; it is a named position, and it carries a stated cost.
**Produces**: a ranked Tier 1 cross-section across **six researchable names**, a Tier 1
**constraint map** (exactly one binding constraint per name), a sub-sector mapping that makes
the Concentration Rule evaluable, and **at most three** capped position slots. Not a book.
**Hosts three pillars.** Every question this thesis depends on but does not own is named in
**§2b Cross-tier dependencies** and cited there rather than re-derived.

---

## 0. Inherited baseline — what this thesis does NOT re-derive

001–004 established the following. This thesis **takes them as given**; re-deriving any of
them is out of scope. Every row cites the artifact, so the inheritance is verifiable rather
than trusted. Paths are repo-relative. Grades are P4 grades (`DEMONSTRATED` / `CLAIMED` /
`MODELED`), with a disposition class named where the finding *is* an absence
(`UNRESOLVABLE-FROM-PUBLIC-SOURCES`, `NON-FORMABLE`, `UNMEASURED`).

**Correction policy.** Where a later thesis invalidates an earlier figure, the earlier
artifact is **not** rewritten. Its files are frozen; the correction is recorded here and
cited by location — matching 001's own annotate-don't-rewrite policy. §0 therefore carries
**four corrected rows**, and three of them correct positions this spec itself held.

### Inherited from 001 — the technology baseline

| Inherited result | 001 artifact | Grade |
|---|---|---|
| Launch is the master **cost** variable (A1a **holds**) and **not** the master **value** variable (A1b **falsified**), on three independent issuer confirmations | `theses/001-technology-baseline/artifacts/FLY/2026-09-18_1239_unit-economics_methodology.md`; `…/artifacts/RKLB/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` |
| **Electron basis A = $30,333/kg; basis B = $14,667/kg** — the only demonstrated per-launch cost in the universe, at a **`CLAIMED` 300 kg** payload | `…/artifacts/RKLB/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` on the cost; **denominator `CLAIMED`** |
| **Electron is 10.3× Falcon 9 per kg** on basis A — the small-lift penalty, quantified from filed data | same | `DEMONSTRATED` |
| RKLB **built 14 / launched 16** (2024), **24 / 21** (2025), **11 / 12** (H1 2026) → demand- or production-limited, **not launch-limited** | same | `DEMONSTRATED` |
| RKLB revenue **+62%** with **launch revenue −$2.1M** (declining); growth from space systems **+$91.6M** | same | `DEMONSTRATED` |
| **The fixed-cost-absorption bound**: **PL** earns the universe's best gross margin (**53.5%**) and still loses **37%** at the operating line because opex is **90.6%** of revenue — break-even needs **1.69×** current revenue; **YSS needs 2.86×**. **Neither multiple involves launch cost** | `theses/001-technology-baseline/_cross/technology-baseline_synthesis.md` §4.2 | `DEMONSTRATED` |
| **YSS gross margin 24.0% against an opex ratio of 68.6%**; fixed costs are **2.9× gross profit** | `…/artifacts/YSS/2026-09-18_1239_operational-kpi_methodology.md`; `…/_cross/phase-3-production-supply.md` | `DEMONSTRATED` — **see the 002 correction row below: 2.86× on the quarter, 1.94× on FY2025** |
| **YSS revenue −20.5% QoQ** ($92.547M vs $116.343M), carried forward **UNSMOOTHED** against the volume reading | `…/artifacts/YSS/2026-09-18_1239_operational-kpi_methodology.md` | `DEMONSTRATED` |
| FLY revenue **+657% to $117.7M** "driven by Spacecraft Solutions"; **GM 20.3%** (weakest of the three); **R&D 60.8% of revenue** (highest in the universe); operating loss **$(95.2)M**; **emerging growth company** | `…/artifacts/FLY/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` |
| **KRMN**: revenue **$182.063M** (+58.2%), gross profit **$78.234M (43.0%)**, operating income **$34.829M (19.1%)** — highest of any hardware supplier, **1.6× the primes**; net income $14.032M; **capital structure absorbs 60% of operating income** ($20.797M below the line); **2.4× debt-to-equity PE roll-up, mechanism NOT established** | `…/artifacts/KRMN/2026-09-18_2015_supply-chain_methodology.md` | `DEMONSTRATED` |
| **PIL-3's falsifier was never evaluated.** It is **PENDING**, not failed — the disclosure is public, it simply has not been read | `…/_cross/phase-3-production-supply.md` | **`UNMEASURED`** |
| **DA-25**: RKLB's disclosed `revenue per launch` implies a **51.6%** launch gross margin; the audited segment table implies **42.9%** | `…/artifacts/RKLB/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` |
| Backlog at 2026-06-30: **RKLB $2,355.9M**, **FLY $1,468.1M** (up **8.7%** from $1,351.1M) — a demand-side datum, not a launch-side one | `…/artifacts/FLY/2026-09-18_1239_unit-economics_methodology.md` | `DEMONSTRATED` |
| **DA-13** — production rate in units is disclosed by **exactly one issuer** in the universe (RKLB). Every cross-issuer manufacturing-rate comparison is blocked by this | `…/artifacts/YSS/2026-09-18_1239_operational-kpi_methodology.md` | `DEMONSTRATED` (the absence) |
| **The manufacturing constraint is queue position, not capability** — TER's single-year revenue increase (~$2,100M) approximately equals the combined annual revenue of every pure-play space company in the universe (~$2,170M) | `theses/001-technology-baseline/thesis.md` (status log, `TER × operational-kpi`) | `DEMONSTRATED` |

> **Two 001 rows this thesis inherited are NOT carried here, and the reason is ownership
> rather than quality.** The **space-grade solar-cell duopoly** (RKLB/SolAero · BA/Spectrolab)
> is a supply-chain-pricing question owned by **008**; **the margin ladder's monotonicity**
> (001's *"operators sit at the bottom"*) is owned by **008** as well, and 003 has since
> measured it **bimodal rather than monotone**. Both are cited in §2b, neither is a pillar
> here. **The ladder is consumed as a ranking input; it is not re-tested.**

### Inherited from 002 — the validated input set

| Inherited result | 002 artifact | Grade |
|---|---|---|
| **DA-23/24/25/26/27/28/29/30 per-issuer census**: FLY `C 4/4, 15/15`; LUNR `C`; RKLB `C (two regimes)`; VOYG `C`; YSS `C (FLIPPED)`; HAWK `C 5/6` | `theses/002-evidence-validation/_cross/002-evidence-validation_synthesis.md` | `DEMONSTRATED` |
| **⚠ Correction to this spec — VOYG is a plain DA-23 SIGN STRIP, and the register's *"unreconcilable LEVEL"* classification is WITHDRAWN.** `−51.408 < +4.457` violates nothing; the bound fires on **16 of 17 periods, continuously since FY2024**, not three. **The claim that VOYG "fails the gross-profit bound by $46,951M across three consecutive quarters" was carried in this spec's validation queue and is false.** The component identity closes on **17 of 17 periods** | `…/artifacts/VOYG/2026-09-18_1500_recent-quarter_methodology.md`; `…/_cross/validation-ledger.md` (correction row 28) | `DEMONSTRATED` |
| **⚠ Correction — LUNR's DA-23 is CONFIRMED and promoted from CANDIDATE**, and **the component identity RUNS**: `Revenues − CostsAndExpenses`. The recorded unavailability was a **CONCEPT-NAME artefact** — `GrossProfit` returns zero facts at LUNR while `CostsAndExpenses` carries the data. **The 42.1% is the \|FY2025 annual\| operating margin mislabelled as a quarter** (DA-23 + DA-26), and **001's DA-26 exception is OVERTURNED** | `…/artifacts/LUNR/2026-09-18_1500_recent-quarter_methodology.md` | `DEMONSTRATED` |
| **⚠ Correction — YSS's `$110.466M` Q1 2026 figure is RESOLVED**: it is a sign-stripped `$(110,466)K` operating **LOSS**, and the *"95% margin"* is the filed `(95)%` with the minus dropped — **the same defect as the Q2 2026 flip, not a second one.** DA-26 **NOT TESTABLE** (10-K ingestion pending, kind 1); **DA-28 confirmed** (1000× share-count scale error); **91% single-customer concentration**; backlog **$592,049K at 2026-06-30** | `…/artifacts/YSS/2026-09-18_1500_recent-quarter_methodology.md`; `…/artifacts/YSS/2026-09-18_1500_operational-kpi_methodology.md` | `DEMONSTRATED` |
| **RKLB's FY2025 balance-sheet rows read the PRIOR-YEAR COMPARATIVE COLUMN** — current ratio served **2.071** against a filed **4.083** (−49.3%); working capital −65.8%. **`EPS × shares` is INADMISSIBLE as a sign test** | `…/_cross/validation-ledger.md`; `…/artifacts/RKLB/2026-09-18_1500_ratio-analysis_methodology.md` | `DEMONSTRATED` |
| **The only runway-adjacent RKLB disclosure located**: *"expects $2.1B cash and $258.1M marketable securities to fund operations for 12 months"*; a **$3.6B committed bridge**; filed balance-sheet cells; current ratio 5.482 / 4.083 / 2.040; **FCF FY2025 `(321,806)` served as `+9,236`** | `…/artifacts/RKLB/2026-09-18_1500_ratio-analysis_methodology.md` | `DEMONSTRATED` (the disclosure); the served FCF is a **DA-23 artefact** |
| **The fixed-cost multiple, restated from the filed quarter**: YSS opex is **2.86×** gross profit on the quarter (**1.94×** on FY2025) — 001's *"2.9×"* is the rounded reading and is superseded by this one | `…/artifacts/YSS/2026-09-18_1500_operational-kpi_methodology.md` | `DEMONSTRATED` |

### Inherited from 003 — the launch-cost curve and the value-pool map

**Consumed, never re-derived.** 005 ranks *against* the map; it does not rebuild it.

| Inherited result | 003 artifact | Grade |
|---|---|---|
| **Electron is the only `DEMONSTRATED` marginal cost in the universe**; and **Q2 2025 → Q2 2026 cost/launch −12.0% while cost/kg +32.0%** — two of six Q2 2026 missions were **HASTE suborbital, zero kg**. The unit-economics direction depends on which denominator is used | `…/_cross/launch-cost-curve-value-migration_synthesis.md` | `DEMONSTRATED` |
| The **SPCX 4-basis 12.8× spread** — $939 / $1,519 / $7,409 / $11,977 per kg. **A single "launch cost" figure is a modelling choice, not a datum** | same | `DEMONSTRATED` |
| **PIL-6 is `NON-FORMABLE` at YSS** — a **PRESENCE** finding: YSS's cost of revenue decomposes exhaustively, so the falsifier's inputs do not exist. **`NON-FORMABLE` is not `PASS`** | same | **`NON-FORMABLE`** |
| **LUNR 14.19% FY2025** is the only value above the bar, and it **collapses to 3.64% / 4.37% in 2026 as a DENOMINATOR EVENT** (Lanteris) — not an efficiency change | `…/_cross/value-pool-map.md` **E-07** | `DEMONSTRATED` |
| **DA-23 confirmed at 9 of 9 tickers.** The GSAT artifact that *documented* DA-23 was itself reproducing it on eight figures **while all three automated gates passed** | `…/_cross/launch-cost-curve-value-migration_synthesis.md` | `DEMONSTRATED` |
| The cohort's value-pool rows — **E-04 RKLB Launch Services** (revenue **44,586**, **−4.42% YoY**, GM **42.86%**, **files NO segment operating income**, `operator_class: independent_launch`, **100% services revenue**, 81.0% of RKLB revenue is Space Systems) · **E-05 RKLB Space Systems** (189,480, **+93.64%**, GM 34.55%, *"the closest thing in this universe to a market price for launch"*) · **E-06 FLY** (117,683, **+656.86%**, operating income **−95,197**, **−80.90%**, **92.0% spacecraft solutions vs 8.0% launch**, the **DA-26 counterexample**) · **E-07 LUNR** (206,168, +309.77%, −47,136, **−22.86%**, files **no gross-profit subtotal** so the **INCLUSIVE** pairing is admissible) · **E-09 YSS** (92,547, −41,313, **−44.64%**, gross margin **23.97% FILED not derived**, opex **2.86×** gross profit, exhaustive four-component cost decomposition, **the positive pass-through counterexample** — contribution margin rose 33→34, 24→42, 29→38 and direct material per revenue dollar fell **$0.758 → $0.575**) | `…/_cross/value-pool-map.md` **E-04…E-09** | `DEMONSTRATED` / `DERIVED` per row |
| **⚠ Correction carried forward from 003**: the figures **22,150 / 22,180 / 44,330 / 24,602 / 9,526 / 34,128** circulating in this workspace as *"YSS revenue"* are **YSS's GROSS PROFIT**. Any artifact quoting them as revenue is quoting the wrong line | `…/_cross/value-pool-map.md` | `DEMONSTRATED` |

### Inherited from 004 — the anchor, and its boundaries

| Inherited result | 004 artifact | Grade |
|---|---|---|
| **The Space segment row**: revenue **$962M**, operating income **$(542)M**, **−56.34%**, regime *revenue multiple, range*, `MODELED`, boundary **❌ NON-COMPARABLE (DA-06)** — *no transaction price exists; no external multiple borrowed*; **RKLB/FLY are `loss_making`**. **Permitted consumers: 005, 007** | `theses/004-tier0-spacex-anchor/_cross/anchor-sotp.md` | `MODELED` |
| **The headline**: live market cap **$2.0718T** ÷ Connectivity operating income = **312.8×**, and Connectivity is the **only** profitable segment. The finding **survives every allocation** — even granting Space + AI **$1.5T**, Connectivity carries **86×** | `…/_cross/tier0-spacex-anchor_synthesis.md` | `DERIVED` |
| **AI capex is 86.2% of quarterly capex** while Connectivity — the only profitable segment — receives **7.4%**. The capital-allocation finding, stated as arithmetic | same | `DEMONSTRATED` |
| **The comparator partition admits 0 of 11**, and the three segments fail for **three different reasons** — earnings, price formation, disclosure. **No borrowed comparator exists for the Space row either** | `…/_cross/anchor-sotp.md` §7 | `DEMONSTRATED` (the absence) |

**The transfer conditions are part of the inheritance, not commentary on it.** A consumer of
004's Space row **must carry**: (1) the **DA-23 filed sign** — the segments sum to **$(143)M**
while the served layer returns `+143,000,000`; (2) **the basis and date of every market
figure** — the live/dated spread is a **~28% component**, not noise; (3) **DA-06** — a
captive-integrated segment has **no transaction price**, so comparing its margin to a peer
launcher is comparing **a price to a non-price**; (4) **A4/P10** — the 1M-satellite filing is
**inadmissible as a valuation input**; (5) **the A1b showing** — value migrating out of launch
must be **shown**, not asserted. **005 is a permitted consumer of the Space row only.** The
Connectivity and AI rows belong to 006 and 009, and pricing off them here would re-open a
closed class (§2b).

**What 001–004 did not do.** 001 covered Tier 1 only through the lens of specific pillars —
YSS for manufacturing rate, RKLB and FLY for launch unit economics, LUNR at Light depth.
002 validated the *figures* and never asked a business question. 003 built the curve and the
value-pool map and stopped at the map's edge. 004 valued **the anchor's own segments** and
excluded this cohort by construction (SPCX appears in **neither** 005's universe nor 006's).
**None of the four asked the cross-sectional question**: given A1b is falsified — value does
*not* accrue to launch — **which of these pure-plays are positioned where value actually
went, and which can still fund themselves while they wait?** That cross-section is this
thesis's entire scope.

### Validation queue — the Tier 1 figures this thesis owns

**Denominator and physics validation is 002's, not this thesis's.** 002 owns the three
`CLAIMED` denominators (Electron 300 kg, Falcon 9 22.8 t, Starship 100 t), F2's unsourced
constants, and the DA-23 census universe-wide. **005 owns the Tier 1-specific contested
figures below** — the ones no other thesis can resolve, because no other thesis reads this
cohort. Where a 005 conclusion depends on a 002-owned number, the dependency is named
in-line and the conclusion carries 002's band.

**Four rows of the previous queue are closed and three of them closed *against this spec*.**
They are retained below, struck through in substance, because a queue whose resolutions
disappear is a queue that cannot be audited.

| Tier 1 contested figure | Current state | Disposition required here |
|---|---|---|
| ~~**VOYG operating income $51.408M against gross profit $4.457M** — *"fails the gross-profit bound by $46,951M across three quarters"*~~ | ✅ **CLOSED — and this spec's claim was FALSE.** VOYG is a **plain DA-23 sign strip**; `−51.408 < +4.457` violates nothing; the component identity closes **17 of 17**. The register's *"unreconcilable LEVEL"* sub-mechanism is **withdrawn** | **P1 now runs on the ordinary component identity at VOYG.** No substitute detector, no barred line |
| ~~**LUNR Q4 2025 operating margin 42.1%** — *"no quarterly gross-profit line exists, so the component identity cannot run"*~~ | ✅ **CLOSED — and this spec's premise was WRONG.** The unavailability was a **concept-name artefact**: `GrossProfit` returns zero facts at LUNR while **`CostsAndExpenses` carries the data**. The 42.1% is the **\|FY2025 annual\| margin mislabelled as a quarter** (DA-23 + DA-26); 001's DA-26 exception is **overturned** | **The component identity runs** via `Revenues − CostsAndExpenses`. Recorded as a **concept-availability** finding, not an issuer defect |
| ~~**YSS Q1 2026 operating figure $110.466M on $116.343M revenue — a 95% "margin"**~~ | ✅ **CLOSED.** A sign-stripped **`$(110,466)K` operating LOSS**; the 95% is the filed **`(95)%`** with the minus dropped — the **same defect as the Q2 2026 flip, not a second one**. DA-26 **NOT TESTABLE** (10-K ingestion pending, kind 1) | **No fourth defect class.** The YSS series is read on the filed sign throughout |
| **KRMN: capital structure absorbs 60% of operating income** ($34.829M operating vs $14.032M net) | Demoted by 001 from defect to **structure** | Operating-margin rankings **overstate levered suppliers**; the below-the-line bridge must be shown in-line. **Open here** |
| **RKLB FY2025 balance-sheet cells read the prior-year comparative column** (current ratio served 2.071 vs filed 4.083) | ✅ Confirmed by 002's ledger | Any balance-sheet ratio read from the served layer is **presumed contaminated** until the comparative column is identified. **Open here as a reading rule** |
| **RKLB runway**: *"$2.1B cash and $258.1M marketable securities to fund operations for 12 months"*, and a **$3.6B committed bridge** carrying the Iridium consideration | `CLAIMED` disclosure; the bridge is a **committed facility with a named counterparty**, which is the only kind §1b's runway test admits | **Counts toward the runway computation.** The *deal's* gate chain and combined-entity model are **006's** (§2b) |
| **Deal values**: Iridium **~$8B** (announced 2026-06-29), All.Space **~$355M** (agreed 2026-04-29), Astrobotic **~$300M** | All press-sourced and unaudited — `CLAIMED` under P4; pointers: constitution §A5 and §Tier 1 | Admissible as context and for **structure**; **never as a valuation input** |
| **YSS's 68.6% opex ratio may be All.Space deal-cost inflated** | Open carry-forward from 001 Phase 3 | Segment confirmation required before the fixed-cost multiple is quoted as a run-rate. **Open here — and it is now P1's own input** |

**Disposition classes are kept distinct**, per P4: `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (the
disclosure does not exist anywhere — remedy is a named external source);
`UNRESOLVABLE-FROM-PLATFORM` (it exists, the platform cannot reach it — remedy is a read
route); **`NON-FORMABLE`** (the falsifier's inputs do not exist — **is NOT `PASS`**);
`UNMEASURED` (the work has not been done — a task, not a finding).

---

## 1. Research Question

**Within the listed pure-play layer, which business models actually convert launch-cost
decline into shareholder value — and which are simply levered to a narrative?**

A1b is falsified: value did not accrue to the launcher. SPCX grew **+91.9%** with Falcon
launches **−18%**; RKLB grew **+62%** with launch revenue **−$2.1M**; FLY grew **+657%**
from Spacecraft Solutions. If value migrated away from launch, then a cohort of
companies *defined by* manufacturing-and-launch should not all be priced as though the
migration had not happened. Some of them are positioned where value went. Some are not.
**Telling those two groups apart is the question, and the cohort is small enough to answer
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

**Sub-questions 1 and 3 are one pillar, not two.** Question 3's own 001 provenance already
reframed it as *"which names can close the gap before funding runs out"* — which is
question 1's question. They are hosted together as **P1**; question 2 is **P2**.

### The P3 compromise — declared, not hidden

**P3 requires exactly one binding constraint per thesis.** This thesis cannot honestly
name one, and says so rather than choosing the modal answer and presenting it as
binding. The reasons are specific:

1. **Tier 1 is not one business model.** It contains a launch provider that owns a
   solar-cell supplier and is buying a constellation (RKLB), a launch provider integrating
   an acquisition (FLY), a lunar lander and services firm (LUNR), a component supplier
   (KRMN), a space-station and defense firm (VOYG), and a satellite manufacturer (YSS).
   Naming `CAPITAL` for the cohort would be a statement about the balance sheets; naming
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
   **exactly one** permitted constraint value, evidenced — **one per name, with no
   exception**. **The thesis-level constraint is multi; the decision-level constraint is
   single**, and every sizing decision in this thesis is taken at the decision level.
   That is the honest form of P3 compliance here, and it is the first deliverable, not a
   closing note.

> **The re-cut simplified this compromise and did not dissolve it.** At v1.6.0 the
> deal-leg value `REGULATORY_SPECTRUM` left this thesis with the debt-and-merger leg it
> belonged to, so **RKLB now carries one constraint value, not two.** The remaining map is
> six names, six values, no name carrying two.

---

## 1b. Pillars

### Pillar 1 — Funding runway and fixed-cost absorption are one question, and no Tier 1 name has a break-even multiple it cannot fund (Priority: P1) 🎯 Minimum Defensible View

This is the Minimum Defensible View because **it is the only pillar that can make the
others irrelevant.** The cohort is pre-profit, the regime is NEUTRAL, and the long end
is at **4.80%** — three-year highs, with the market pricing hike risk rather than cuts.
A pure-play that has to return to the capital markets before it reaches breakeven is
making a financing bet, not a value-capture bet, and no amount of positioning changes
that. **Survival is the precondition; positioning is the question.**

**The claim:** for each of the **six researchable** Tier 1 names, disclosed cash, disclosed
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

#### The fold: runway and absorption are one arithmetic, not two

**The second limb of this pillar is not a second question.** A break-even revenue multiple
is a *quantity of funding required*; a runway is a *quantity of funding available*. Neither
is decision-relevant alone. **A Tier 1 name whose break-even multiple exceeds its funding
runway is a financing event, not a growth story** — and that sentence is the whole pillar.

The absorption measure is already established for the universe and is inherited, not
re-derived. From `technology-baseline_synthesis.md` §4.2 — *"the binding constraint on
space operators is fixed-cost absorption"* — with a Tier 1 name as the canonical case:

| Issuer | Gross margin | Opex ratio | Break-even revenue multiple | Cohort status at v1.6.0 |
|---|---:|---:|---:|---|
| **PL** | **53.5% — best in the universe** | **90.6%** | **1.69× current revenue** | **Moved to Tier 2 (006).** Its row is consumed as the bound's sharpest instance, **not as a cohort member** |
| **YSS** | 24.0% (**23.97% filed**) | 68.6% | **2.86× current revenue** | **In cohort — the returned case** |
| **KRMN** | 43.0% | **23.8%** *(DERIVED: (78.234 − 34.829) ÷ 182.063)* | **0.55×** *(DERIVED: 43.405 ÷ 78.234)* | **In cohort — the counterexample: the only name whose fixed costs are a fraction of gross profit, which is why it earns 19.1% at the operating line** |

**PL earns the universe's best gross margin and still loses 37% at the operating line**
because opex is 90.6% of revenue. **No multiple in that table involves launch cost.** The
synthesis's own verdict: *"This is the finding PIL-3's falsifier was trying to reach by
reading risk-factor prose, and XBRL answers it directly."*

**Consequence — the scope of the question changed.** It is no longer *"is the cohort
launch-limited or demand-limited?"* (answered: neither — **it is fixed-cost absorption, and
the arithmetic is in the income statement**). The open question is **which Tier 1 names can
close a 1.69×–2.86× revenue gap before their funding runs out**, and **KRMN's 0.55× is the
proof that the gap is not a cohort-wide condition** — it is a per-name condition and the
cohort spans a wide range of it.

**Two behavioural instruments, neither of which reads prose:**

1. **The build-vs-launch test.** A launch-limited company accumulates unlaunched inventory;
   a demand-limited company draws it down. RKLB's filings show **14 built / 16 launched**
   (2024), **24 / 21** (2025), **11 / 12** (H1 2026) — drawdown in two of three periods,
   which is not the behaviour of a launch-constrained firm.
2. **The margin-multiple test.** Fixed costs ÷ gross profit, from the income statement.
   Above 1.0×, the issuer is volume-constrained by arithmetic, whatever its filings say
   about delays. KRMN at **0.55×** and YSS at **2.86×** are the two ends of the cohort's
   range.

**Why this is P1 and not P2**: the answer gates the other two pillars. A name that fails
P1 cannot be sized at any priority level, so running P2–P3 first would produce a ranking
that cannot be acted on.

**Two honest limits, carried in-line.** (a) **DA-13 blocks the ideal test**: production
rate in units is disclosed by **exactly one issuer in the universe** (RKLB). Where units
are absent, the margin-multiple test substitutes and the substitution is recorded per
name. (b) **TER's queue-position finding complicates the inference**: TER's single-year
revenue increase (~$2,100M) approximately equals the combined annual revenue of every
pure-play space company (~$2,170M), and its capacity is allocated by a larger market
that pays more. **A capable supplier does not relieve a constraint if the queue is
longer than the cohort's order book.** Where a Tier 1 manufacturer is queue-limited
rather than demand-limited, that distinction is reported rather than averaged away.

**Independently falsifiable** — four conditions, all mechanical:

**wrong_if** (runway): `metric=count_of_tier1_pure_plays_with_less_than_24_months_disclosed_funding_runway_and_no_committed_facility threshold=0 source=10-Q_cash_flow_statement_and_liquidity_note op=>`

**wrong_if** (the fold — a break-even multiple it cannot fund): `metric=count_of_tier1_issuers_whose_break_even_revenue_multiple_exceeds_their_disclosed_funding_runway threshold=0 source=10-Q_income_statement_and_liquidity_note op=>`

**wrong_if** (behavioural — the build-vs-launch test): `metric=share_of_tier1_issuers_accumulating_unlaunched_inventory_across_consecutive_reporting_periods threshold=0.5 source=issuer_disclosed_build_versus_launch_counts_or_inventory_balances op=>`

**wrong_if** (data-integrity — a hardware manufacturer that cannot cover its own cost of revenue): `metric=count_of_tier1_hardware_manufacturers_reporting_negative_gross_margin threshold=0 source=10-Q_income_statement_after_component_recomputation op=>`

**Subscribed**: `RKLB × recent-quarter`, `FLY × recent-quarter`, `YSS × recent-quarter`, `LUNR × recent-quarter`, `KRMN × recent-quarter`, `VOYG × recent-quarter`, `RKLB × ratio-analysis`, `FLY × ratio-analysis`, `YSS × ratio-analysis`, `VOYG × ratio-analysis`, `LUNR × ratio-analysis`, `KRMN × ratio-analysis`, `RKLB × risk`, `FLY × risk`, `LUNR × risk`, `VOYG × risk`, `RKLB × operational-kpi`, `YSS × operational-kpi`, `FLY × operational-kpi`, `RKLB × unit-economics`, `YSS × unit-economics`, `FLY × unit-economics`, `KRMN × unit-economics`, `RKLB × supply-chain`, `YSS × supply-chain`, `KRMN × supply-chain`, `FLY × supply-chain`

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
enough to order the cohort.

**The re-cut made this a cleaner test and moved its prior — both are stated.** With the
four constellation operators removed to Tier 2 at v1.6.0, the cohort is now
**manufacturing-and-launch by membership**, and the composition question stops being a
mixed-cohort question with an obvious answer at one end. **Five of the six names sell
hardware; LUNR is the only services model left standing.** The measured share, taken from
the value-pool rows 003 already built, is not close to the 0.5 threshold:

- FLY is **92.0% spacecraft solutions** against 8.0% launch;
- RKLB's **Space Systems is 81.0% of company revenue** (189,480 of ~234,066 across the two
  mapped segments) and Launch Services is **100% services revenue** at 44,586;
- YSS manufactures satellites, KRMN supplies components, VOYG builds stations;
- **LUNR is the only name whose revenue is a service performed with hardware it also builds.**

**A >0.5 reading is therefore the expected outcome, and the pillar says so rather than
implying otherwise.** That does not retire the falsifier — a falsifier whose prior is known
is still a falsifier, and it is evaluated on the cohort as it exists. What it changes is
the **interpretation route**: if it fires, the correct output is not a re-worded claim but
the recorded finding that **the pure-play layer is still a hardware layer** — value migrated
*out of launch* without the listed pure-plays migrating *out of hardware* — and that the
ranking **carries no information the sector-membership ordering did not.** 011 then sizes
the theme on the sector ordering, not on this ranking. **That outcome is a finding, not a
null**, and it is the more interesting of the two because it is the one the cohort's
membership test predicts.

**Two things the measured share still buys, whichever way it lands:** the **level**, which
is what 011 needs to size a theme in which the listed expression is the hardware layer; and
the **trend**, period by period, from the segment tables — a cohort drifting toward services
and a cohort parked in hardware price very differently at the same level.

**Why this priority**: it is the thesis's actual research question, and it is P2 rather
than P1 only because it is unactionable until P1 says who can wait. It is ranked above
the remaining pillar because that pillar is a characterisation of discrete events and this
one is a property of the cohort.

**Classification discipline.** Every issuer's revenue is classified by **its own
segment definitions** (DA-21), and the classification is stated per issuer, never
aggregated across issuers on the assumption that the segments mean the same thing. The
value pool is defined precisely: revenue from **services, operations, or constellation
capacity** — as distinct from hardware delivered to a customer.

> **⚠ Correction carried.** The previous version of this pillar quoted the constitution's
> Earth Observation & Geospatial rationale as *"commoditized imagery, government-concentrated
> demand, persistent negative unit economics"* and proposed testing it here. **Both halves
> are now wrong.** The rationale was **restated at v1.4.0** — *"persistent negative unit
> economics"* is **refuted**, because PL earns the **best gross margin in the universe
> (53.5%)** and loses money to fixed-cost absorption, which is a volume problem and not a
> cost problem; the Underweight now rests on demand concentration and is a **timing**
> judgment. And **PL and BKSY left this tier at v1.6.0**, so the EO test is **006's**. Both
> are recorded in §2b; neither is hosted here.

**Independently falsifiable**: hardware sales and manufacturing remain more than half of
Tier 1 aggregate revenue, meaning the cohort's centre of gravity has not moved and the
value-capture ordering carries no information the sector-membership ordering did not.

**wrong_if**: `metric=share_of_tier1_aggregate_revenue_from_hardware_sales_and_manufacturing threshold=0.5 source=10-Q_segment_and_revenue_disaggregation_tables op=>`

**Subscribed**: `RKLB × business-model`, `YSS × business-model`, `VOYG × business-model`, `RKLB × unit-economics`, `YSS × unit-economics`, `FLY × unit-economics`, `KRMN × unit-economics`, `RKLB × competitive`, `LUNR × competitive`, `VOYG × competitive`, `RKLB × secular-trends`, `LUNR × secular-trends`, `VOYG × secular-trends`, `RKLB × sector-overview`, `YSS × sector-overview`, `KRMN × sector-overview`, `VOYG × sector-overview`, `RKLB × peer-bench`, `FLY × peer-bench`, `YSS × peer-bench`, `KRMN × peer-bench`, `LUNR × peer-bench`

---

### Pillar 3 — Tier 1's acquisitions are value-pool migration, not empire-building (Priority: P3)

**Four of the six cohort names are acquirers, and that is what makes this a cohort question
rather than a set of anecdotes.** RKLB is acquiring Iridium (~$8B), VOYG acquired Astrobotic
(~$300M), YSS acquired All.Space (~$355M, agreed 2026-04-29), and **KRMN carries a 2.4×
debt-to-equity PE roll-up** whose mechanism 001 recorded as **not established** and demoted
from defect to **structure**. Three of the four are priced under P4 as `CLAIMED`; all four
are large relative to the acquirer. **The question is not whether they are large — it is
whether they are the same strategic move, and whether that move is the one A1b predicts.**

**The claim:** the three integration targets are **downstream acquisitions into the value
pool** — constellation operations, lunar services, and ground/terminal connectivity
respectively — rather than unrelated diversification. The test is structural, not
rhetorical: an integration is value-pool migration when the target's business lies in
**services, operations or constellation capacity**, which A1b identifies as where value
went. It is empire-building when the acquirer funds it from a deteriorating operating
position with cash or debt rather than equity — buying growth it cannot yet afford with
money it does not yet generate. **KRMN is the pillar's control case**: a serial acquirer
funding acquisitions from a **positive** operating position ($34.829M operating income,
19.1% margin) — the mirror image of the falsifier below, carried with its mechanism
recorded as open rather than assumed.

**Why this priority**: last because it is a *characterisation* of four discrete capital-
allocation events, and it becomes decisive only if one of them breaks. Its usefulness is
concentrated in a single scenario, which is why it ranks below the two cohort-wide
pillars. The value-pool definition used to test the targets is fixed once in §1c and not
restated.

**Ownership boundary, declared in advance.** 005 owns the **cohort-level** test: is this
pattern value-pool migration or empire-building, across all four acquirers, read from the
consideration mix and the acquirer's operating cash flow. 005 does **not** own any
individual deal's regulatory gate chain or any combined-entity forecast — those are
**006's** (§2b), and this thesis neither models a combined entity nor dates a consent.
**The one acquirer-side fact 005 does keep is the consideration mix**, because a
majority-debt acquisition funded by a pre-profit buyer is exactly the falsifier below, and
because the committed bridge is a *financing* fact, which is P1's own subject.

**Independently falsifiable**: any Tier 1 acquirer with negative operating cash flow
funding a majority cash-or-debt acquisition. That is the empire-building signature — a
pre-profit buyer levering a narrative rather than acquiring a cash-generative pool.

**wrong_if**: `metric=count_of_tier1_acquirers_with_negative_operating_cash_flow_funding_a_majority_cash_or_debt_acquisition threshold=0 source=10-Q_cash_flow_statement_and_8-K_merger_consideration_disclosure op=>`

**Subscribed**: `RKLB × business-model`, `VOYG × business-model`, `YSS × business-model`, `RKLB × what-if`, `VOYG × what-if`, `YSS × what-if`, `KRMN × what-if`, `RKLB × competitive`, `FLY × competitive`, `LUNR × competitive`, `VOYG × competitive`

---

> **Delivering P1 alone yields a defensible partial conclusion** — the Tier 1 cohort
> splits into names that can fund themselves to profitability and names that cannot, on
> disclosed cash and disclosed burn. That is the single most valuable output of this
> thesis, it is delivered first, and it is the only pillar whose answer does not depend
> on another pillar's answer.

## 1c. Method — the cross-sectional instruments

This is a **cross-sectional comparison, not six per-name deep dives.** Depth is
allocated to the names that carry the pillars (RKLB, YSS, FLY, VOYG) and the other two are
read at the depth needed to place them in the ranking. Three instruments are specific to
this thesis:

1. **The build-vs-launch behavioural test.** For every issuer disclosing both counts,
   accumulated inventory is computed period by period. Drawdown means demand- or
   production-limited; accumulation means launch-limited. **This is a behavioural
   measure and requires no prose coding** — it is the replacement 001 proposed for
   PIL-3's 19-document risk-factor read, and it is why P1 is affordable.
2. **The margin-multiple test.** Fixed costs ÷ gross profit, from the income statement.
   Above 1.0×, the issuer is volume-constrained by arithmetic — and the ratio's second use
   is as the **break-even revenue multiple** (opex ÷ gross profit), which is the quantity
   P1's second falsifier compares against the runway. KRMN at **0.55×** and YSS at
   **2.86×** are the cohort's worked ends. Where a name reports negative gross
   margin, the multiple is undefined and the name reports under the fourth P1 falsifier
   instead.
3. **The value-pool classification.** Every issuer's revenue is allocated to hardware
   versus services/operations/constellation capacity, using **each issuer's own segment
   definitions** (DA-21), with the allocation stated per name. The cohort is then ranked
   by distance from the hardware end. **This instrument produces P2's answer and P3's
   target test from the same classification**, which is why the definitions are fixed in
   §1b.

**Evidence discipline.** Per P4 and the v1.6.0 Data-Integrity Register, no artifact in
this thesis reads `operating_income` without showing `gross profit − opex` in-line.
**`EPS × shares` is not a sign test** — it passes spuriously on flipped issuers at RKLB,
FLY and VOYG — and its use is a defect, not a shortcut. Where the component identity
cannot run, the artifact says so and uses the weaker margin-plausibility detector, named
as such; **at v1.6.0 no cohort name is in that class** — the two names the previous spec
barred on component-availability grounds (LUNR, VOYG) were both cleared by 002, LUNR on a
concept-name artefact and VOYG on a withdrawn sub-mechanism. **DA-26 (annual figures
mislabelled as quarterly) and DA-27 (fiscal-period labels derived from the calendar
quarter) both apply to this cohort** — PL has left the tier, but KRMN, VOYG and YSS each
straddle a fiscal boundary, so every quarterly series built here is reconciled against
the annual before use. **DA-23 is presumed present until disproved**: 002's census found
all six cohort names exhibiting, and the served layer's balance-sheet rows may be reading
the prior-year comparative column (RKLB), so **every balance-sheet ratio is re-derived
from the filed cells, never taken from the served aggregate.**

**Correction policy.** Where this thesis contradicts a 001–004 figure, their files are
**frozen**. The correction is recorded here and cited by location — matching 001's own
annotate-don't-rewrite policy.

## 2. Universe Definition

**Eight names, of which six are researchable.** The tier's membership test is single —
*does the issuer's primary revenue come from building or flying launch vehicles, spacecraft,
landers or in-space infrastructure?* — and the cohort that results is
**manufacturing-and-launch**, with no constellation operator, no Earth-observation data
product and no suborbital tourism in it. Weights are **analytical effort, not positions** —
the position cap is fixed by the Concentration Rule and the multi-constraint declaration in
§1, not by this table. **Market Data Stage is `none` across the cohort**: every conclusion
here is drawn from filings, not prices. Deal values are `CLAIMED` under P4.

| Ticker | Company | Sector | Sub-sector (Sector Preferences) | Weight | Role in this thesis |
|---|---|---|:---:|---|
| RKLB | Rocket Lab | industrial.aerospace_defense | Launch Services & Reusable Transport | 25% | **Largest surface.** The only demonstrated launch unit economics in the universe (basis B $14,667/kg); the only issuer disclosing build-vs-launch counts; **P11 acquirer** of Iridium (~$8B) carrying the $3.6B bridge. **P1, P2 and P3 all land here** |
| YSS | York Space Systems | industrial.aerospace_defense | Space Infrastructure & Components | 20% | **The cleanest manufacturing read and the cohort's diagnostic case**: 24.0% gross margin against a 68.6% opex ratio and a **2.86×** break-even multiple — **P1**. Also carries revenue **−20.5% QoQ** that cuts against the volume reading, and **91% single-customer concentration** |
| FLY | Firefly Aerospace | industrial.aerospace_defense | Launch Services & Reusable Transport | 17% | Weakest gross margin of the manufacturers (**20.3%**) with the highest R&D intensity (**60.8%**) and the largest operating loss (**$(95.2)M**) — **P1**. **92.0% spacecraft solutions against 8.0% launch** — **P2**. An **emerging growth company**, a structural disclosure-quality variable |
| VOYG | Voyager Technologies | industrial.aerospace_defense | **unmapped** — provisional Space Infrastructure & Components | 15% | Starlab space station plus defense; acquired Astrobotic (~$300M) — **P3**. **The operating line is clean**: VOYG's DA-23 is a plain sign strip, the component identity closes **17 of 17 periods**, and **P1 runs on the ordinary component identity here** |
| LUNR | Intuitive Machines | industrial.aerospace_defense | **unmapped** — no lunar-services line exists | 12% | Lunar landers and services; **the cohort's only services model** and the one name that keeps **P2**'s hardware-share test live. DA-23 **confirmed**; the component identity runs via `Revenues − CostsAndExpenses` |
| KRMN | Karman Holdings | industrial.aerospace_defense | Space Infrastructure & Components | 11% | Missile/space/defense components — a **hardware model with supplier economics**, and **the cohort's only name whose fixed costs are a fraction of gross profit (0.55×)**. Capital structure absorbs **60%** of operating income — **P1, P3**. The supply-chain question belongs to **008**; 005 reads it as the cohort's hardware pole and its control case for acquisition behaviour |
| **Sum** | | | | **100%** | |

**Named but not researchable — recorded as coverage gaps, not proxied.**

| Ticker | Company | Class | Why it cannot host research |
|---|---|---|---|
| RDW | Redwire | `NOT_READY` | Deployable structures and in-space manufacturing — a **Tier 1 member by the membership test**, and the one that would have tested P2's hardware pole from the *in-space infrastructure* end. `xbrl_facts` = 0, `src_documents` = 0 |
| SPCE | Virgin Galactic | `NOT_READY` | Suborbital human spaceflight — a Tier 1 member by function (flying spacecraft) whose economics share nothing with the rest of the cohort. Unavailable |

**Both are `NOT_READY` under the constitution's own coverage audit and cannot host a thesis.**
Their absence is recorded as a **coverage gap**, and it is a real one on both sides: RDW
would have widened P2's hardware share, and SPCE would have widened its *range*. **No proxy
is substituted for either name** — where a datapoint would have rested on RDW or SPCE, the
gap is recorded and the conclusion is stated without it. Re-check before wave 2.

**Sub-sector mapping is itself a deliverable.** Two of the six names (**VOYG, LUNR**) **do
not map onto a Sector Preferences sub-sector without inventing one** — the table has no
space-station and no lunar-services line. The mapping above is **provisional**, and it is
required work rather than bookkeeping, because the **Concentration Rule is defined by
sub-sector** and cannot be evaluated without it. Under the provisional map:

- **Launch Services & Reusable Transport holds exactly two names (RKLB, FLY) — at its
  2-position cap**, so both can be held, and doing so consumes two of the three Tier 1
  slots.
- **Space Infrastructure & Components holds three names (YSS, KRMN, and VOYG
  provisionally) against the same 2-position cap**, and four if LUNR is also forced onto
  the nearest available line. **It is oversubscribed whichever way VOYG is mapped**, so
  at least one of the three can never be held alongside the others.

So the **3-position Tier 1 cap binds the cohort's size, and the 2-position sub-sector cap
binds *within* Space Infrastructure & Components** — which is the sub-sector where the
cohort's manufacturing economics actually live. That is a structural feature of the tier,
not a bookkeeping annoyance, and it is flagged in Clarifications **Q-3**.

**Cohort-erosion and empty-result disposition.** Both are live rather than hypothetical,
and the re-cut makes them sharper:

1. **RKLB leaves this tier by its own membership test if the Iridium acquisition closes.**
   The constitution's Tier 1 table already marks it `DEAL (as acquirer)`, and the
   combined entity's primary revenue would come from *operating* a constellation — which
   is Tier 2's function, not this one. **The closure therefore removes the cohort's
   largest name, its only demonstrated launch unit economics, and its only build-vs-launch
   discloser.** Five names remain, and P1's build-vs-launch instrument loses its only
   direct reading; it falls back to the margin-multiple test with the substitution
   recorded per name.
2. **If screening then returns no researchable expression, the tier is not closed as a null
   result and the premise is not withdrawn.** It converts to a **holdings-level read-through
   recorded in `_cross/`**, with the ranked cross-section and constraint map retained for
   006/008/009/011 and the tier marked **`no_listed_expression`** rather than `no_thesis`.
   The inherited premise survives; only its expressibility is lost — which is itself a
   finding 011 must size against.
3. **The partial-erosion case is the likely one and is handled in-line**: the ranked
   cross-section is published **with the cohort it was measured on and the date**, and any
   name that leaves the tier after measurement is marked as a **member at measurement,
   not at delivery** — never quietly dropped from a ranked table.

**Excluded by adjacency:** **JOBY** and **ACHR** are READY and appear in space thematic
funds, but they operate in the atmosphere. Excluded by the constitution's Research Scope
Constraints; read-through only, and not into this thesis. **Astroscale** (TYO: 186A) is a
listed pure-play by function but is not platform-covered and trades in Tokyo — out of scope
until an ADR exists.

## 2b. Cross-tier dependencies — declared, not absorbed

**The rule this section discharges** (constitution §Universe Definition): where a name spans
functions, the tier is set by primary revenue and every other function is carried as a
**DECLARED CROSS-TIER DEPENDENCY — never absorbed as a pillar of the host thesis.** A
cross-tier question belongs to the thesis that owns that tier, and the host thesis cites it.
**005 hosts three pillars and cites everything else.** This table is the complete list, so
that an unhosted question is a declared dependency rather than a silent gap.

| Question 005 depends on | Sole owner | What 005 cites, and what it must not do |
|---|:---:|---|
| **The IRDM/RKLB deal gate chain** — FCC → ITU → DCSA, the dated milestones, the combined-entity model, and the break-and-re-underwrite rule | **006** | 005 cites **whether and when the deal closes**, and nothing finer. 005 **models no combined entity, dates no consent, and prices no spread.** RKLB is read **standalone** here; the only acquirer-side facts 005 keeps are the **consideration mix** and the **committed bridge**, which are financing facts and therefore P1's |
| **Operator margins by segment** — the downstream margin reference for the value pool | **006** | Consumed as a reference in P2's value-pool ranking. Never re-derived; never used to price a Tier 1 name |
| **The Earth Observation & Geospatial sub-sector test** — the constitution's only Underweight / Low space rating | **006** | The test was hosted here only because PL and BKSY sat in this cohort. **Both moved to Tier 2 at v1.6.0**, so the test moved with them. 005 cites the outcome; it does not re-open it |
| **The space-grade solar-cell duopoly and its pricing power** — RKLB/SolAero · BA/Spectrolab | **008** | A structural finding that is **real, load-bearing for every constellation plan in the sector, and priced zero times**. 005 cites 008's finding when it lands and **hosts no work on it**: no disclosure search, no artifact, no falsifier |
| **BA / Spectrolab** | **008** | The Spectrolab leg is not 005's, and **no proxy is substituted** for it |
| **The margin ladder's monotonicity** | **008** | 005 **consumes** the ladder as a ranking input. It does **not** re-test monotonicity — and the two framings in the workspace (**001's** *"operators sit at the bottom"* vs **003's** measurement that it is **BIMODAL, not monotone**: component suppliers **22.76%** vs primes **11.25%** = **2.02×**, which holds) are **008's to resolve**, not 005's |
| **The component-pricing and queue-position question for KRMN and the supply layer** | **008** | 005 hosts KRMN's **cohort** read (runway, break-even multiple, value-pool classification, acquirer behaviour). The **supplier-economics** question is 008's |
| **The SPCX anchor rows** | **004** | 005 is a **permitted consumer of the Space row only** (`$962M / $(542)M / −56.34%`, `MODELED`, **❌ NON-COMPARABLE (DA-06)**, RKLB/FLY `loss_making`), and it must carry **all five transfer conditions** listed in §0. **The Connectivity and AI rows are 006's and 009's**: pricing off a name this anchor excluded re-opens a closed class without saying so |
| **The launch-cost curve and the value-pool map** | **003** | Consumed, never re-derived. 005's §0 carries the results; no artifact here rebuilds a curve or re-ranks a value pool from source |

**A dependency is not a hedge.** Citing 006 for the deal gate chain does not license 005 to
form a view on the close; it obliges 005 to **state the standalone case and name the event
that would invalidate it**. The same applies in the other direction: 006 holds the licence
layer and the geospatial operators, and if 006's findings contradict 005's, the resolution
is a recorded reconciliation between two theses, not an amendment to either.

## 3. Skill Deployment Matrix

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|:---:|---|:---:|---|
| operational-kpi | business-intelligence | Deep | RKLB, YSS, FLY | none | Build-vs-launch counts, inventory balances, and the margin-multiple inputs — **P1**'s two behavioural instruments. RKLB is the universe's only unit-rate discloser |
| unit-economics | business-intelligence | Deep | RKLB, YSS, FLY, KRMN | none | Gross margin, R&D intensity, fixed-cost-to-gross-profit multiple per name; DA-25's two readings side by side — **P1, P2** |
| business-model | equity-research-core | Deep | RKLB, VOYG, YSS | none | The value-pool classification (hardware vs services/operations/constellation) and each acquirer's stated integration rationale — **P2, P3** |
| recent-quarter | equity-research-core | Standard | RKLB, FLY, LUNR, KRMN, VOYG, YSS | none | The DA-23/DA-24/DA-26/DA-27 read on every Tier 1 issuer-quarter; the **validation queue** is built here — **P1** |
| ratio-analysis | quantitative-analysis | Standard | RKLB, FLY, YSS, VOYG, LUNR, KRMN | none | Runway, leverage and margin ratios on component-verified inputs; the below-the-line bridge shown in-line; balance-sheet cells re-derived from the filed column — **P1** |
| risk | equity-research-core | Standard | RKLB, FLY, LUNR, VOYG | none | Cash runway, going-concern language, committed facilities, and the terms of the committed bridge — **P1** |
| peer-bench | quantitative-analysis | Standard | RKLB, FLY, YSS, KRMN, LUNR | none | The cross-sectional rank itself — the instrument that makes a cohort claim more than six anecdotes — **P2** |
| competitive | equity-research-core | Standard | RKLB, FLY, LUNR, VOYG, KRMN | none | Competitive structure **inside the tier**, and the lunar-services field now consolidating into VOYG — **P2, P3** |
| supply-chain | industry-analysis | Light | YSS, KRMN, RKLB, FLY | none | What these manufacturers buy — and where the queue is longer than the order book. **The component-pricing question itself is 008's** — **P1** |
| sector-overview | equity-research-core | Light | RKLB, YSS, KRMN, VOYG | none | Sub-sector mapping for the Concentration Rule, including the two names that have no sub-sector line — **P2** |
| secular-trends | equity-research-core | Light | LUNR, VOYG | none | Demand-pool direction for lunar services and commercial stations — **P2** |
| what-if | quantitative-analysis | Light | RKLB, VOYG, YSS, KRMN | none | The integration counterfactuals and the acquirer consideration mix — **P3** |

> **Coverage invariant.** Every ticker in §2 appears at least once above; every
> `Subscribed` pair in §1b generates at least one task; every matrix skill is named in at
> least one `Subscribed` line. Verified by `tools/plan_audit.py` (I1–I4).
>
> **One depth is corrected here.** `business-model` was listed Standard in this matrix and
> Deep in §4. It is **Deep**, because it is P2's only classification instrument and P2 is
> the thesis's own research question — the matrix row was the outlier, not the tier list.

## 4. Depth Tiers

| Tier | Skills | mode-set | Tickers | Output |
|:---:|------|---|--------|------|
| Deep | operational-kpi, unit-economics, business-model | all modes | RKLB, YSS, FLY, **and VOYG on `business-model` only** | Full-mode work on the names carrying P1 and P2 — RKLB, YSS and FLY are the three names that appear in both pillars' `Subscribed` sets, and VOYG's integration rationale is P3's largest single input |
| Standard | recent-quarter, ratio-analysis, risk, peer-bench, competitive | essentials_modes | As listed | The cohort read, the rank, the runway computation, the competitive placement |
| Light | sector-overview, secular-trends, supply-chain, what-if | essentials_modes | As listed | Scoping checks that bound the above |

**Budget note.** **Six names; the matrix yields 49 distinct `(ticker, skill)`
analyses**, expanding to roughly **58 mode-tasks**. The re-cut reduced the pair count from
55, so the per-name load went **up** — this is Deep work
on a small cohort, not a broad shallow pass, and the concentration is deliberate: RKLB
alone carries 11 of the 49 pairs. **`thesis.md` currently carries a placeholder budget of
40; this spec requires it raised to 60 at plan time** — recorded as a precondition, not
assumed. If the budget must come down, drop the Light rows first; never the Deep rows,
which carry P1 and P2, and never the `recent-quarter` row, which is the entire delivery
mechanism for the validation queue.

## 5. Cross-Cutting Analysis

- **The ranked cross-section** is the primary output: every researchable Tier 1 name,
  its value-pool distance, its runway in months, its fixed-cost multiple, and its
  provisional single binding constraint — one table, **six rows**, every cell traceable to
  a filing.
- **The constraint map** is the second output, and it is how the P3 compromise is
  discharged: **one permitted constraint value per name**, evidenced, no exceptions.
  Provisional: **`MANUFACTURING_RATE`** for **YSS** and **KRMN** — 001's register already
  codes the constellation-economics line this way on the measured break-even multiple
  (**KRMN 0.55×, YSS 2.86×**), and it is the value P1's title asserts. **The remedy
  direction is `DEMAND`** (a volume problem yields only to order flow), which is why the
  two readings sit adjacent rather than in conflict: `MANUFACTURING_RATE` is the
  **evidenced constraint**, `DEMAND` is the **remedy**. **`DEMAND`** for **LUNR**, whose
  revenue is a services contract against a government and commercial order book.
  **`CAPITAL`** for **FLY**, **VOYG** and **RKLB**. **Six names, six values** — the
  re-cut removed the second value RKLB used to carry, because the deal leg's
  `REGULATORY_SPECTRUM` left with the deal model, and `REGULATORY_SPECTRUM` now belongs to
  006's cohort (§2b).
- **Macro sensitivity: high, and it is concentrated in P1.** These are pre-profit,
  long-duration issuers in a NEUTRAL-bias regime with the 10Y at **4.80%** and a market
  pricing hike risk. The constitution's own re-rate trigger — a 10Y break above **5.25%**
  — deepens caution on exactly this cohort, because it moves the financing cost of every
  externally dependent name in the runway table. The sector preference is **Overweight /
  High** on Launch Services, which is a *sector* call this thesis tests at the
  *cohort* level rather than assumes — and **the constitution's own restatement makes the
  boundary explicit**: *"a thesis citing this row as evidence that value accrues to
  launchers is `UNFRAMED_REFERENCE`."* **005 cites it as a cost-curve and picks-and-shovels
  position, never as an A1b claim.**
- **Constitution interaction**: **P3** — declared multi, discharged per name (§1).
  **P11** — RKLB is a deal security (`DEAL — as acquirer`), so its artifacts carry
  `deal_security_basis` and its position sizes at the **2% binary cap**; **the gate chain
  that governs the close is 006's** (§2b), and no artifact here models the combined
  entity. **Risk Framework** — the **Concentration Rule** binds hard here: the cohort
  cannot be traded as a basket, and its 6% ceiling is set in §1, not chosen here.
  **A1a/A1b** — A1a is settled and inherited; **A1b is the organising fact**, not a pillar
  to re-prove. **P4 / Data-Integrity Register** — DA-23, DA-25, DA-26, DA-27 and DA-28 all
  bind this cohort directly; `EPS × shares` is inadmissible as a sign test.
- **Pair-trade candidates: none admissible.** The cohort shares one factor — the theme —
  and the Concentration Rule caps Tier 1 at three positions with **two per sub-sector**.
  With Launch Services holding exactly two names and Space Infrastructure & Components
  oversubscribed at three, the sub-sector cap already forces a choice *inside* the cohort;
  a relative-value pair would consume the whole allowance to express a single spread. The
  relative call belongs in 011, where the theme cap (40% of NAV) binds before the
  sub-sector cap (25%).
- **Deliberate non-outputs**: no DCF. Per the Methodology Foundation, DCF is admissible
  only where an issuer has three years of positive free cash flow or a contracted backlog
  covering the forecast period — most of this cohort fails the first condition, and
  comps are a cross-check only for a pre-profit issuer. **This thesis ranks; it does not
  value.** No combined-entity model, no consent dating, and no solar-cell or
  margin-ladder work: all three are hosted elsewhere (§2b).

## 6. Output Contract

- **Per-ticker (dispatcher-resumable)**: `artifacts/{ticker}/{YYYY-MM-DD}_{skill}_{mode}.md`
  — the suffix **must** be `_{skill}_{mode}.md` with the real mode slug, so
  `dispatch.resume_verdict()` can find it.
- **Cross-cutting (not resume-tracked)**: `_cross/{name}.md`.
- **Primary artifact**: `_cross/tier1-value-capture-ranking.md` — the ranked cross-section
  with the value-pool classification, runway months, fixed-cost multiple and provisional
  constraint per name, **published with the cohort it was measured on and the date**.
  **This is what 006, 008, 009 and 011 cite.**
- **Second artifact**: `_cross/tier1-constraint-map.md` — the per-name single-constraint
  assignment with evidence, which is what discharges the P3 compromise.
- Snapshot: `snapshots/005-launch-spacecraft-services/{YYYY-MM-DD}_thesis.md`
- **Frontmatter**: per `contracts/artifact-frontmatter.yaml`, with `thesis_id:
  "005-launch-spacecraft-services"`. All five pins are mandatory: `constitution_pin: 1.6.0`,
  `assumption_pin: "2"`, `skill_pin`, `as_of`, `corpus_version`. **Any artifact on RKLB
  must set `deal_security_basis` (P11).**

## 7. Thesis Phases

| Phase | Tasks | Duration | Dependencies |
|:---:|------|---|------|
| 1 — Cohort validation and component hygiene (**the queue**) | The DA-23/DA-26/DA-27/DA-28 read on all six names; every operating line shown as `gross profit − opex` in-line; balance-sheet cells re-derived from the filed column; the four closed rows recorded as closed | Week 1 | Constitution v1.6.0 loaded; 002's census and per-ticker artifacts at `constitution_pin: 1.6.0` |
| 2 — Runway and fixed-cost absorption (**P1**) | Cash, disclosed burn and committed facilities for all six names; runway in months; the break-even multiple per name; the self-funding / externally-dependent split; the build-vs-launch series for every discloser; the TER queue-position carve-out | Week 2 | Phase 1 |
| 3 — Value capture (**P2**) | Value-pool classification per issuer (DA-21, own segment definitions); the hardware share of Tier 1 aggregate revenue; the level and the trend | Week 3 | Phase 2 |
| 4 — Integrations (**P3**) | The three targets plus the KRMN roll-up classified against the value pool; consideration mix and acquirer operating cash flow; the financing test | Week 4 | Phase 3 |
| 5 — Rank and hand-off | Publish the ranking and the constraint map; record what could not be resolved and what left the tier; hand the cohort to 011 and the cross-tier dependencies to 006/008/009 | Week 5 | Phase 4 |

## Clarifications

Recorded by `agentii.specify` at creation, 2026-09-18; re-opened at the v1.6.0 re-cut,
2026-09-19. No `agentii.clarify` round has run; the following are recorded as open for
that pass.

- **Q-1 (P3, the declared compromise)** — Is the per-name constraint map an acceptable
  discharge of P3, or does a multi-constraint thesis require an explicit exemption
  recorded against the constitution? **Provisional:** the map discharges it, because P3's
  purpose is to prevent sizing against several constraints relaxing at once, and every
  sizing decision here is taken on a single named constraint. **The re-cut strengthened
  this answer**: the map is now six names to six values with no name carrying two, so
  there is no longer a name where the discharge has to be argued. **If answered
  differently this is a PATCH to spec, not a MAJOR event.**
- **Q-2 (P1, the 24-month bar)** — 24 months of runway was chosen as the point at which a
  pre-profit issuer can plausibly reach a financing window rather than be forced into
  one. It is a **spec-set bar**, not a measured quantity, and it is now **load-bearing for
  two falsifiers**, since the break-even multiple is compared against it. **Flagged for
  human confirmation.**
- **Q-3 (all pillars, the sub-sector mapping)** — Two names (**VOYG, LUNR**) have no
  Sector Preferences line, and the **Concentration Rule cannot evaluate without a
  sub-sector**. Should the mapping be provisional-per-thesis as written here, or does it
  require a constitution amendment to add the missing lines? **Provisional:** provisional
  per thesis, with the gap recorded — because the amendment route would block this
  thesis on a SemVer event. **Note the mapping is now doing more work than it used to:**
  with three names provisionally inside Space Infrastructure & Components against a
  2-position cap, the sub-sector line the constitution does not have is the one that
  decides which Tier 1 names can be held together.
- **Q-4 (P2, the 0.5 hardware-share threshold)** — The majority test was chosen as the
  point at which the cohort stops being described by hardware. It is **stated, not
  measured**, and the re-cut has moved the expected outcome to the far side of it. **Two
  readings are put to the human**: (a) retain `threshold=0.5` and report the firing as the
  finding, or (b) re-base the threshold on the cohort as re-cut, which would require a
  *stated* new bar rather than a measured one. **The spec takes (a)**, because a falsifier
  moved to accommodate its own prior is no longer a falsifier. **Flagged for human
  confirmation.**
