# Thesis Program — Space & Orbital Economy

**Constitution pin**: 1.4.0 · **as of**: 2026-09-18 · **Status**: Active
**Scope**: full coverage of the 57-name listed universe across all six tiers, plus
the decision layer.

> This document answers one question: **what theses does the workspace need, in what
> order, and why each one exists.** It is a map, not a thesis. Every thesis it names
> gets its own `theses/{nnn}-{slug}/` directory with a frozen `spec.md`.

---

## 0. The governing design rule

001 was a *baseline*: it established what is physically and economically true, graded
every claim `DEMONSTRATED` / `CLAIMED` / `MODELED`, and produced no trade ideas by
design. **Its primary artifact — the technology-line register
(`_cross/technology-baseline_synthesis.md`) — is published.** 001 now holds **38
artifacts across all 35 tickers**, six technology lines, and verdicts on all six
falsifiers: **3 HOLDS, 0 FALSIFIED, 3 UNRESOLVABLE.**

**Everything from 002 forward inherits 001 rather than repeating it.** Two obligations
follow, and every spec in this program carries both as named sections:

| Obligation | Meaning |
|---|---|
| **Inherited baseline** | What 001 already `DEMONSTRATED` that this thesis takes as given and will **not** re-derive. Cited by artifact, so a reader can verify the inheritance rather than trust it. |
| **Validation queue** | Which of 001's `CLAIMED` and `MODELED` figures this thesis must convert to `DEMONSTRATED`, or record as unresolvable. Under P4, `MODELED` can never satisfy a falsifier — so an unvalidated number is a pillar that cannot fire. |

### 0.1 The five inherited results that most constrain this program

These are 001's load-bearing conclusions. **A downstream thesis that contradicts one is
not automatically wrong, but it must engage the artifact that produced it.**

1. **Value has already migrated out of launch — at the launch monopoly.** SPCX's own Q2
   2026 segment disclosure: **Connectivity 54.9% of revenue, AI 32.8% *(⚠️ boundary-contaminated — see §0b; do not quote as organic migration)*, Space 12.3%** and
   *falling 1.9%* across a half in which consolidated revenue rose **53.7%**. **Mass to
   orbit −25.6%, Falcon launches −17.8%, internal launches −25.0%.** A1b is falsified on
   the issuer's chosen metrics. **Qualification that must travel with it:** Space carries
   a **65.8% gross margin** — highest in the universe — with cost of revenue flat while
   revenue rose 29%. **Falcon launch economics are good; the segment loss is Starship
   R&D.** The reporting entity also changed mid-series (xAI merger, X merger, IPO,
   pending $60B Cursor) — **common-control accounting recasts prior periods, so growth
   rates spanning those boundaries mix real growth with entity change.** The Space
   series is the one that survives the boundary.
2. **The margin ladder is inverted relative to narrative.** One monotone ordering across
   eight issuers, **as a function of distance from programme risk**: HEI **25.5%**, KRMN
   19.1%, WWD ~17%, LMT 12.4%, RTX 11.4%, LHX 11.1%, NOC 10.1%, and **GSAT 7.4%** — a
   monopsony supplier. **Component suppliers earn ~2× the primes they supply.**
   Refined rule: *component concentration predicts margin when the supplier's revenue
   spreads across programmes* — the discriminator is **single-programme dependence**,
   not buyer concentration. **No listed issuer offers both growth and margin except TER
   and KRMN.**
3. **The binding constraint on space operators is fixed-cost absorption, not launch
   cost.** PL earns the universe's best gross margin (**53.5%**) and still loses 37% at
   the operating line; **break-even needs 1.69× current revenue.** YSS needs **2.86×**.
   **Neither multiple involves launch cost.** This is what PIL-3's falsifier was reaching
   for by reading risk-factor prose — and XBRL answered it directly.
4. **The demand side is 73× the supply side.** Three pharma buyers turn over
   **$39,634M/quarter** against a pure-play space cohort at **~$2,170M/year**. Merck's
   R&D alone is **7.3×** the cohort's combined revenue.
5. **Orbital compute is being out-*chosen*, not out-built.** SPCX — the one actor with
   cheap orbital access — deployed **1.4 GW on the ground**, named *data centers* before
   launch facilities in its own capex narrative, and is buying a $60B software company
   with stock. The line does not close because physics forbids it; it closes because the
   only party able to choose it revealed a terrestrial preference with $21.5B of capex.
   **A false-positive trap is registered:** SPCX's *"AI computational infrastructure"*
   segment is **terrestrial compute with satellite-delivered distribution** — it fails
   the DA-20 four-way test and must not be read as orbital compute.

### 0.2 Three UNRESOLVABLE verdicts, three different causes — do not collapse them

001's most methodologically useful output is that its three unanswerable falsifiers fail
for **three different reasons**, each with a different remedy:

| Line | Cause | Remedy | Owned by |
|---|---|---|---|
| **PIL-3** | **An unbuilt census** — not an unavailable disclosure | **Build it.** Read Item 1A + MD&A delay causes across 19 filings. **Bounded work, inside the platform.** | **005**, **008** |
| **PIL-5** | **The number does not exist anywhere** | None available. Report as a finding about disclosure. | **009** |
| **PIL-6** | **A registry outside the corpus** (FCC IBFS, ITU Space Network List) | Requires direct registry access the platform does not provide | **006** |

**PIL-3 is the only one with a remedy inside the platform, and it is the cheapest
open item in the program.** A downstream thesis that reports all three as "insufficient
data" discards the distinction, which is itself the finding.

### 0.3 The validation queue, carried forward

001's headline conclusions rest on a narrower base of `DEMONSTRATED` inputs than their
precision implies. The open items 002 owns:

1. **RKLB's Electron payload is `CLAIMED` at 300 kg** — the denominator of *every*
   Electron $/kg figure, and basis B is the **only** demonstrated per-launch cost in the
   universe. ±15% moves every Electron number ±15%.
2. **SPCX's Falcon 9 denominator is `CLAIMED` at 22.8 t** — same structural problem,
   larger by revenue.
3. **F2's physics has two unsourced inputs** — the heat-pump COP at elevated rejection
   temperature (F2's table is rejection-side only) and radiator areal density (8 kg/m² is
   an admitted placeholder). F2 is the *named binding constraint for orbital compute*, so
   its placeholders propagate into the sector's largest narrative.
4. **Six data-integrity defects** (DA-23 … DA-28) are registered but applied to a census
   rather than the universe. *See below.*

A thesis that inherits a `CLAIMED` denominator and builds a falsifiable pillar on it has
validated nothing. That is the failure mode this program is designed to avoid.

### 0.4 001's carry-forwards, and where each lands

| 001 carry-forward | Owner |
|---|---|
| 0 — Escalate the launch-volume finding to the constitution | **DONE** — A1a/A1b split executed at v1.3.0 |
| 0b — Review every SPCX-dependent finding for entity-boundary contamination | **002** (new pillar) |
| 0c — Register the "AI infrastructure ≠ orbital compute" trap | **DONE** — registered in §0.1(5) here and in 009 |
| 1 — Build the PIL-3 delay-cause census (19 filings) | **005** and **008** |
| 2 — Add the gross-profit bound as a detector | **DONE** — registered at v1.3.0 as detector #2 |
| 3 — Register DA-26 at 19 of 19 with the WWD scope question | **DONE** — registered at v1.3.0 |
| 4 — Register DA-27 | **DONE** — registered at v1.3.0, **n = 4 of 4** in current thesis.md (the synthesis recorded 1 candidate; thesis.md is newer and records the correction) |
| 5 — Report the margin ladder and the 73× asymmetry as primary findings | **008** and **010** |
| 6 — Seven amendments queued for owner approval | **DONE** — executed at v1.3.0 |

---

## 0b. The investment main line — the program's governing argument

**Added 2026-09-18 after the `agentii.clarify` round on 002.** The main line is formable
**now, from 001 alone** — it does not depend on 004–010 existing. It is recorded here
because it is what the program is *for*: every segment thesis either supplies an input to
it or tests a part of it.

### The claim

> **Space is a cost curve, not a value pool.**

A1a holds — cheap launch *makes* orbital businesses possible. A1b is falsified — cheap
launch does **not** distribute the value to launchers. Value settles in the layers that
are **indifferent to which operator or programme wins**, and in the finite allocated
assets that are **priced rather than granted**. Everything else in the theme is a bet on
a specific programme winning — which is precisely the bet the sector punishes.

### The two findings it joins

001 reported these separately and never joined them. They are the same finding in two
registers:

| 001 finding | What it says | Where |
|---|---|---|
| **The margin ladder** | Operating margin is **monotone in distance from programme risk**, across eight issuers | synthesis §4.1 |
| **Value migrated out of launch** | Launch is **12.3% of revenue at the company that dominates launch**, and fell 1.9% across a half in which consolidated revenue rose 53.7% | synthesis §4.6 |

Read together: **the sector pays for indifference to outcome, and it punishes
concentration — including concentration on the launch programme the theme is named after.**

**⚠️ The mechanism names TWO joint axes — narrowed at clarify round 2.** The strongest
counter-argument is that the ladder is an **aftermarket-vs-OEM artifact**, not a
programme-structure fact. It is not: **the ladder holds within OEM too** — KRMN (OEM
components) **19.1%** vs LMT (OEM prime) **12.4%**. So **programme concentration *and*
revenue recurrence operate jointly**, and a thesis attributing the ladder to either alone
is `UNFRAMED_REFERENCE`.

**⚠️ One supporting figure is boundary-contaminated and must not be quoted.** The
workspace has been citing **"AI is 32.8% of SPCX revenue"** as evidence of migration. The
AI segment contains **xAI, merged 2026-02-02 under common control**, which recasts prior
periods — so its growth mixes organic expansion with an entity that was not previously
inside the reporting entity. **The migration claim rests instead on Space (clean, and the
series that *fell* 1.9% H1) and Connectivity (clean, wholly organic, 54.9%).** That is a
stronger footing, and the flag is **002 P6's** to enforce.

**⚠️ The ladder's measured scope is 8 issuers**, selected by which artifacts 001 happened
to write — a real selection concern. **Extension to all 21 Tier 3 names is assigned to
008.** Until it runs, the mechanism is `DEMONSTRATED` on 8 names and `MODELED` beyond them,
and every citation must say so.

### The organizing axis, and where every name sits

| Position on the axis | Names | Op. margin | Space purity | Character |
|---|---|---|---|---|
| Installed-base component — **maximum indifference** | HEI, KRMN | **25.5%, 19.1%** | Low | Revenue spread across programmes; does not care which wins |
| Subsystem | WWD | ~17% | Low | |
| Primes | LMT 12.4% · RTX 11.4% · LHX 11.1% · NOC 10.1% | mid | Low | DoD buyer across many programmes |
| **Monopsony operator — the worst of both** | **GSAT** | **7.4%** | **High** | A licence *and* one customer |
| Pure-play operators | PL, YSS, RKLB, FLY | **negative** | **Highest** | Fixed-cost absorption, not unit economics |
| **The only "both" names** | **KRMN, TER** | 19.1%, 32.9% | KRMN genuine · TER thin | 001's §7: *"no listed issuer offers both growth and margin except TER and KRMN"* |

The two extremes are the two traps: **diluted space exposure** at the top, **concentrated
outcome risk** at the bottom. GSAT is the diagnostic case — 001's line: *"a licence is an
asset; being a licence holder with one customer is not the same as owning the asset."*

### The core finding — stated plainly, per the 2026-09-18 clarify decision

> **You cannot buy this theme cleanly. The space-pure names have the sector's worst
> economics, and the names with the best margins are mostly not space companies.**

This is not a defect in the analysis; it is the analysis. 001 reached it independently:
*"The thesis's claim survives contact with the filings, and its falsifiers mostly could
not have fired."* **Consequence for method: screen on margin quality and programme
indifference, not on space purity.** A screen that filters for space exposure selects
for exactly the property the ladder penalizes.

### The strategy inventory — and the honest actionability count

| # | Strategy | Evidence base | Actionable? |
|---|---|---|---|
| 1 | **Own the indifference layer** — component revenue spread across programmes | Margin ladder, 8 issuers, monotone | ✅ **but it is not a space investment.** HEI runs 2.6% R&D; space exposure is incidental |
| 2 | **Screen on fixed-cost absorption, not TAM** — break-even multiple = opex ratio ÷ gross margin. PL **1.69×**, YSS **2.86×** | synthesis §4.2, XBRL-derived | ✅ mechanical and reproducible — but it is a *pre-profit industrial* screen, not a space screen |
| 3 | **Express the compute narrative terrestrially** — own VRT/NVDA/MSFT, not orbital aspirants | SPCX deployed **1.4 GW on the ground**; MSFT adds ~8× SPCX's nameplate **per year** | ✅ strongest evidence in the workspace |
| 4 | **Deal-security spread** — IRDM (RKLB @$54), GSAT (AMZN @$90) as FCC/ITU/CFIUS gate trades | P11; sequential gate chain | ✅ low correlation; 2% binary cap |
| 5 | **Licensed-asset play** — own the licence with *diversified* demand | $19.6B EchoStar mark | ⚠️ premise holds; **falsifier `UNRESOLVABLE-FROM-PLATFORM`** |
| 6 | **Unpriced duopolies** — solar cells, liquid engines, solid motors | synthesis §4.5 | ❌ **unsizable** — `UNRESOLVABLE-FROM-PUBLIC-SOURCES`; the price cannot be verified |
| 7 | **Demand asymmetry** — pharma demand **73×** the space cohort | synthesis §4.3 | ❌ economics `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |

**Four of seven are actionable. Not one of the four is a bet on space technology
succeeding.** They are an aerospace-component margin trade, a generic pre-profit screen,
a terrestrial-compute trade, and a merger-arb spread.

### Falsifiers for the main line itself

Recorded because a governing argument that cannot be falsified is a narrative, not a thesis:

| `wrong_if` | Fires when |
|---|---|
| `metric=operating_margin_spread_between_installed_base_component_layer_and_primes threshold=0 source=10-K_10-Q_operating_margins op=<` | The component layer stops out-earning the primes — the ladder flattens or inverts |
| `metric=spcx_space_segment_share_of_consolidated_revenue threshold=0.123 source=SPCX_10-Q_segment_disclosure op=<` | Launch re-emerges as a growth driver at the anchor |
| `metric=listed_issuer_orbital_compute_revenue_disclosed threshold=0 source=10-K_or_10-Q_segment_disclosure op=>` | An orbital-compute revenue line appears — falsifying "adjacent, not in space" |

**Ownership:** strategies 1–4 and the falsifiers above are **011's P1**. The main line is
011's organizing claim; segment theses 004–010 supply its inputs and test its parts.

---

## 1. Why these theses and not others

### What 001 closed

| 001 result | Status |
|---|---|
| Launch cost sits **15–30× above the $1,000/kg threshold** on every demonstrated basis | **Closed.** PIL-1 holds on basis B without a model, because RKLB discloses `cost per launch` and `revenue per launch`. |
| The F5 propellant floor applies to **fully reusable vehicles only** | **Closed at v1.3.0** — split into F5a/F5b. Falcon 9's binding term is the expended second stage, not propellant. |
| Launch is the master **cost** variable but not the master **value** variable | **Closed at v1.3.0** — split into A1a/A1b, with three independent issuer confirmations. |
| `operating_income` **sign-stripping** is a systematic extraction defect | **Closed at v1.3.0** — DA-23 registered, 12 issuer-quarters, zero exceptions. |
| F1's array ceiling is **~5,000–5,600 m²/MW**, not the naive 2,449 | **Closed.** Eclipse duty, packing factor and EOL degradation multipliers applied. |
| Terrestrial compute is **constrained but expanding** — MSFT alone adds ~8× SPCX's entire installed nameplate every year | **Closed.** "Bottleneck" is superseded as a framing. |
| The knowledge corpus carries **no space-tagged strategies or cases** | **Closed, with a correction** — see §4. |

### What 001 left open, and which thesis now owns it

| Open item | Owner |
|---|---|
| Two unsourced F2 physics inputs; three `CLAIMED` denominators | **002** |
| Where value is captured once launch is not the value variable (A1b) | **003** |
| PIL-3's falsifier is expensive and its evidence is thin (1 issuer with unit data) | **005**, **008** |
| P5's terrestrial denominator is commercially licensed → `UNRESOLVABLE-FROM-PLATFORM` | **009** |
| PIL-6's falsifier needs FCC IBFS / ITU sources the platform does not carry | **006** |
| PIL-4 is the clearest `UNRESOLVABLE-FROM-PUBLIC-SOURCES` in the workspace | **010** |
| No sector analogue could be retrieved — method had to be built from first principles | **011** |

### What no thesis covers, deliberately

- **Advanced air mobility** (JOBY, ACHR) — atmospheric, not orbital. Read-through only.
- **China and Europe/Japan listed space** (LandSpace, Eutelsat, Avio, SKY Perfect JSAT,
  Astroscale) — no platform coverage and no US listing; excluded by the Research Scope
  Constraints. Tracked as competitive inputs, never as theses.
- **The 13 `NOT_READY` names** — cannot host a thesis until coverage is acquired. Three
  of them (MOG-A, ENS, TDY) are load-bearing supply-chain read-throughs and their
  absence is recorded as a coverage gap in the theses that would use them.

---

## 2. The program

**10 new theses, 002–011**, in three parts.

### Part A — Foundation (002–003)

Both are cross-cutting: they produce inputs every segment thesis consumes, and neither
is owned by a single tier.

| # | Thesis | The question | Binding constraint | Output |
|---|---|---|---|---|
| **002** | **Evidence Validation & Model Hardening** | Which of 001's headline numbers survive primary-source validation, and which are artefacts of a `CLAIMED` denominator or an unsourced constant? | *n/a — methodology* | A validated input set. Every downstream thesis cites it instead of re-deriving. |
| **003** | **Launch Cost Curve & Value Migration** | With F5a/F5b now separated and A1b falsified, **where does value accrue** as $/kg falls — and what does the cost curve look like across every vehicle and architecture? | `MASS_LAUNCH_COST` | The sector cost curve + the value-pool map. Tier 0 and Tier 1 both price off this. |

### Part B — Segments (004–010)

One thesis per 板块, per the tier division. **Tier 3 splits in two** (primes and
supply-chain have different binding constraints and different economics). Tiers 1 and 4
remain multi-pillar by construction — they are the two places where a single binding
constraint genuinely cannot be named — and each declares that compromise explicitly
rather than hiding it.

| # | 板块 | Thesis | Universe | Binding constraint |
|---|---|---|---|---|
| **004** | **Tier 0** | **SpaceX Anchor — SOTP across Space / Connectivity / AI** | SPCX | `CAPITAL` |
| **005** | **Tier 1** | **Listed Space Pure-Plays** | RKLB, FLY, LUNR, PL, KRMN, VOYG, YSS, HAWK (+ BKSY, RDW, SPIR, SPCE where coverage permits) | **multi — declared** |
| **006** | **Tier 2** | **Satellite Connectivity, Spectrum & Services** | IRDM, GSAT, SATS, ASTS, VSAT (+ MDA, TSAT, GILT, SGBAF) | `REGULATORY_SPECTRUM` |
| **007** | **Tier 3a** | **Diversified Primes & Defense-Space** | BA, LMT, NOC, LHX, RTX | `DEMAND` |
| **008** | **Tier 3b** | **Space Supply Chain & Components** | HWM, TDG, HEI, WWD, CW, KTOS, MRCY, AVAV, TER, BWXT, KRMN + (MOG-A, TDY, ATRO) | `MANUFACTURING_RATE` |
| **009** | **Tier 4** | **Enabling Layer — Power, Thermal, Compute** | VRT, NVDA, GOOG, MSFT, AMZN, AAPL (+ AMPX, ENS, TMUS) | **multi — declared** |
| **010** | **Tier 5** | **Microgravity Demand Side** | UTHR, MRK, BMY, AMGN, LLY | `DEMAND` |

### Part C — Decision layer (011)

| # | Thesis | The question |
|---|---|---|
| **011** | **Idea Generation, Strategies & Cases** | Given validated facts and positioned segments, **what is actually investable**, at what size, against which catalyst — and which historical analogue applies? |

Tier 0 sits in Part B rather than as a foundation thesis because SPCX is a *segment*
(three reportable segments with three different multiples), not a cross-cutting input.
It is nonetheless built first among the segments — everything else prices off it.

---

## 3. Wave sequencing

`constitution.yaml` sets **`max_theses_active: 6`** and `max_tasks_per_day: 40`. 001 is
still pinned `active` but **its primary artifact is published** — the register exists and
six of six verdicts are recorded. Its only remaining research item is the PIL-3 census,
which is **delegated to 005 and 008** in this program. 001 can therefore be closed to
free a slot as soon as that delegation is accepted.

| Wave | Theses | Slots | Rationale |
|:---:|---|:---:|---|
| **1** | 002, 004, 005, 006, **008** | 5 + 001 = 6 | Foundation plus the anchor and the three sub-sectors the evidence actually supports. **Reordered at clarify round 2**: **008 (component layer) promoted in**, because the margin ladder says that is where the returns are; **003 (launch cost curve) moved to wave 2**, because 001 already settled the curve's *level* and that value left launch. **006 stays** — Connectivity is the one OW/High rating 001's evidence supports unamended (SPCX Connectivity, 38.6% operating margin). |
| **1b** | **011 (P1–P6 only)** | runs *inside* wave 1 | **Added at clarify round 1.** The main line and the strategy layer depend on **001 alone** — not on any segment thesis — so they run immediately rather than waiting for wave 3. No new slot is used: 011's P1–P6 are a synthesis over 001, not a new research cohort. |
| **2** | 003, 007, 009, 010 | 5 | Opens as 001 closes. Launch-curve refinement, primes, enabling layer, microgravity. |
| **3** | 011 (P7 only) | — | Sizing, catalyst calendar and theme-cap arithmetic. **This is the only part of 011 that was ever blocked** — see `011/spec.md` §1d. |

> **Why the reordering is evidence-driven and not a preference.** The constitution's
> Sector Preferences ranked launch first, but at v1.4.0 that row's rationale was corrected:
> launch is OW/High as a **cost-curve and unit-economics** position, not as the sector's
> value pool. Wave 1 follows where the evidence says returns are — the component layer —
> rather than the tier numbering or the pre-v1.4.0 conviction ranking.

**Wave 1 is the Minimum Defensible View of the program.** If all research stopped after
it, the workspace would hold: a validated input set, a sector cost curve, the anchor
thesis, and the two highest-conviction pure-play segments. That is a usable book, not a
fragment.

> **Sequencing note, revised after reading 001's synthesis.** The margin ladder (§0.1(2))
> is 001's most investable single finding, and it points at **Tier 3b — the component
> layer** — which is a **wave 2** thesis. Wave 1 was ordered by the constitution's
> sub-sector conviction ranking, and that ranking places launch and connectivity first.
> **Both orderings are defensible and they disagree.** If the wave-2 slot opens late,
> moving 008 into wave 1 in place of 006 is the highest-value reordering available —
> because 008 is where the baseline says the returns actually are.

---

## 4. The corpus gap, and how Part C handles it

001's brief recorded that the knowledge corpus has **no space content**, and this was
re-verified during program design. The finding holds for sector tags — and carries a
material correction that changes what Part C can do.

**Verified absent.** `search_investment_strategies` on space keywords → 0 rows.
`search_investment_cases` on space keywords → 0 rows. `search_investment_strategies`
filtered `sectors=aerospace_defense` → 0 rows. `list_domains` returns 9 domains whose
`applicable_sectors` are `["med","tech","fin"]` only — **there is no industrial or
aerospace domain in the registry at all.**

**Verified present, and previously missed.** The corpus *does* carry cases on two names
already in this universe, filed under the `Industrials` tag rather than a space tag:

| Universe name | Case | Outcome |
|---|---|---|
| **Moog (MOG-A, Tier 3)** | Brown Advisory — Small Cap Fundamental Value | **~2.1–2.5× on cost, ~110–150% total return over ~3 years, IRR ~28–38%.** Still held. |
| **EnerSys (ENS, Tier 4)** | Brown Advisory — Sustainable Small Cap Core | No disclosed outcome. |

This is a real asymmetry worth recording: **both names are `NOT_READY` on issuer
coverage while carrying fund-sourced cases.** A case without coverage cannot be
validated against filings, and coverage without the case would not have surfaced the
manager's reasoning. Neither alone is sufficient.

**Structurally transferable analogues also exist**, retrievable by *situation shape*
rather than sector tag:

| Analogue | Situation shape | Transfers to |
|---|---|---|
| GATX (railcar leasing) | Capital-intensive asset leasing; utilisation-driven returns | Launch and constellation ownership economics |
| KBR | Government/defense engineering services | Primes with programme concentration (007) |
| Linde | Oligopoly pricing power in an industrial gas | The space-solar-cell duopoly (RKLB/SolAero vs BA/Spectrolab) |
| CNR | Toll-road infrastructure network | The launch-as-toll-road framing under A1a |
| Bio-Red-Dividend **Disruptive Food-Tech Cost Curve Arbitrage** | Exponential cost decline vs incumbent parity — *explicitly modelled on solar PV and semiconductors* | The launch $/kg cost curve (003) |
| Bio-Red-Dividend **Cross-Listed Biotech Arbitrage ("US Premium")** | Non-US-listed assets at a structural discount to US peers, realising via cross-listing or acquisition | Eutelsat, Avio, SKY Perfect JSAT, Astroscale — the exclusion tier |
| Bio-Red-Dividend **Platform Technology Monetisation via Licensing** | The platform owner captures more than the end-product developer | A1b — who captures value in the stack (003) |

**Consequence for 011.** Retrieval must be by **structural situation**, not sector tag.
The sector filter is a dead end by construction: the registry has no industrial domain,
so any sector-keyed query is guaranteed to fail. Part C therefore builds its
strategies-and-cases layer from situation-shape retrieval against the analogue set
above, with primary sources filling the space-specific gaps, and states plainly which
conclusions rest on a borrowed analogue rather than on sector evidence.

---

## 5. Dependency graph

```
001 technology-baseline
 │
 ├──> 002 Evidence Validation ──────┬──> ALL downstream theses cite its validated inputs
 │                                  │
 ├──> 003 Launch Cost Curve ────────┼──> 004 (Tier 0)   SPCX sizes off the curve
 │      & Value Migration           └──> 005 (Tier 1)   launch pure-plays ARE the curve
 │
 ├──> 004 Tier 0  SpaceX Anchor ───────> 005, 006, 007, 008, 009 — every segment
 │      (SOTP)                            benchmarks against the anchor
 │
 ├──> 005 Tier 1  Pure-Plays ──────┬──> 008  supply chain sells into these programs
 │                                  └──> 009  enabling layer sells into these too
 │
 ├──> 006 Tier 2  Connectivity ────┬──> 007  primes are the incumbent satcom competition
 │                                  └──> 009  D2D is a compute-adjacent demand signal
 │
 ├──> 007 Tier 3a Primes ──────────┐
 ├──> 008 Tier 3b Supply Chain ────┼──> 011 Idea Generation  (needs all segments)
 ├──> 009 Tier 4  Enabling ────────┤
 └──> 010 Tier 5  Microgravity ────┘
```

**Hard dependency:** 011 cannot start before 004–010 reach a defensible partial
conclusion. Every other edge is a soft input — a segment thesis can complete without
its upstream neighbour, but its benchmark will be weaker.

---

## 6. Constitution interaction

| Principle / register | How it binds this program |
|---|---|
| **A1a** | Settled. No thesis needs a pillar to prove launch cost is the master cost variable. |
| **A1b** | Falsified on current disclosure. **003 exists to explain where value goes instead.** Any thesis assuming value accrues to the launcher is `UNFRAMED_REFERENCE` if it does not test it. |
| **F5a / F5b** | Every $/kg figure must state which vehicle architecture the floor is applied to. They differ by an order of magnitude. |
| **P2** | Every segment thesis must clear the feasibility gate with a stated physical bound, units and source — including 007 and 009, which are the least physics-bound and most likely to argue from narrative. |
| **P3** | Exactly one binding constraint per thesis. **005 and 009 declare a multi-constraint compromise explicitly** rather than naming one falsely. |
| **P4 / Data-Integrity Register** | Any artifact reading `operating_income` must show `gross profit − opex` in-line. `EPS × shares` is **not** a valid sign test — it passes spuriously on flipped issuers. |
| **P6** | Varda enters 010 as a value-chain node with UTHR as its named listed proxy. No private company receives its own thesis. |
| **P10** | Orbital compute is gated on all five conditions. 009 must not underwrite it; 003 maps the value pool without valuing the constellation. |
| **P11** | IRDM, GSAT and RKLB are deal securities in 005 and 006. Model the acquirer's combined entity, size at the 2% binary cap, and re-underwrite from scratch on a break. |
| **Risk Framework** | The theme cap (40% of NAV) binds before the sub-sector cap (25%) in a single-theme book. 011 is where this becomes a constraint rather than a note. |

---

## 7. Coverage ledger

Tracking which of the 57 listed names each thesis must reach. A ticker appearing in no
thesis is a coverage gap, and identifying those gaps is one purpose of this document.

| Tier | Names | Covered by | Gaps |
|---|---|---|---|
| 0 | SPCX | 002, 003, 004 | — |
| 1 | RKLB, FLY, LUNR, PL, KRMN, VOYG, YSS, HAWK | 003, 005, 008 | — |
| 1 | BKSY, RDW, SPIR, SPCE | 005 | **`PARTIAL` / `NOT_READY`** — named, not researchable |
| 2 | IRDM, GSAT, SATS, ASTS, VSAT | 006 | — |
| 2 | MDA, TSAT, GILT, SGBAF | 006 | **`NOT_READY`** — claimed as read-through only |
| 3 | BA, LMT, NOC, LHX, RTX | 007 | — |
| 3 | HWM, TDG, HEI, WWD, CW, KTOS, MRCY, AVAV, TER, BWXT | 008 | — |
| 3 | MOG-A, TDY, ATRO | 008 | **`NOT_READY`** — MOG-A carries a corpus case with no coverage (**§4**) |
| 3 | TRMB, GRMN, PLTR | 008 | **`PARTIAL`** — sector must be assigned manually |
| 3 | JOBY, ACHR | — | **Excluded** — atmospheric, not orbital |
| 4 | VRT, NVDA, GOOG, MSFT | 003, 009 | — |
| 4 | AMZN, AAPL | 009 | **`PARTIAL`** — manual sector assignment required |
| 4 | AMPX, ENS, TMUS | 009 | **`NOT_READY`** — ENS carries a corpus case with no coverage (**§4**) |
| 5 | UTHR, MRK, BMY, AMGN | 010 | — |
| 5 | LLY | 010 | **`PARTIAL`** — manual sector assignment required |

**Nine `PARTIAL` names** are researchable once their sector is assigned by hand; that
assignment is a precondition recorded in each owning spec, not an assumption.
**Thirteen `NOT_READY` names** cannot host a thesis. Where one is load-bearing for a
segment — MOG-A and TDY for supply chain, MDA and TSAT for connectivity — the owning
thesis records the gap and proceeds without it rather than substituting a proxy.

---

## 8. Thesis registry

| # | Slug | 板块 | Wave | Status |
|:--:|---|:---:|:---:|---|
| 001 | `technology-baseline` | — | — | **active, primary artifact published** — 38 artifacts, 35/35 tickers, register at `_cross/technology-baseline_synthesis.md` (3 HOLDS / 0 FALSIFIED / 3 UNRESOLVABLE). Marked `stale` by the 1.3.0 bump; re-examination **bounded and not dispatched**. One open research item — the PIL-3 census — delegated to 005 and 008. |
| 002 | `evidence-validation` | Foundation | 1 | **specified** — 7 pillars, 17 names, budget 70, audit 4/4 |
| 003 | `launch-cost-curve-value-migration` | Foundation | **2** | **specified** — 6 pillars, audit 4/4. **Moved to wave 2 at clarify round 2** — 001 already settled the cost curve's level. |
| 004 | `tier0-spacex-anchor` | Tier 0 | 1 | **specified** — 6 pillars, audit 4/4; V-1 resolved (AI operating line is `DERIVED`, not disclosed) |
| 005 | `tier1-space-pure-plays` | Tier 1 | 1 | **specified** — 6 pillars, audit 4/4 |
| 006 | `tier2-connectivity-spectrum` | Tier 2 | 1 | **specified** — 6 pillars, audit 4/4 |
| 007 | `tier3a-diversified-primes` | Tier 3a | 2 | planned |
| 008 | `tier3b-supply-chain` | Tier 3b | **1** | stub — **promoted into wave 1 at clarify round 2.** Owns the margin-ladder extension to all 21 Tier 3 names. |
| 009 | `tier4-enabling-layer` | Tier 4 | 2 | planned |
| 010 | `tier5-microgravity` | Tier 5 | 2 | planned |
| 011 | `idea-generation` | Decision | **1b + 3** | **specified** — 7 pillars, audit 4/4. **P1–P6 active now** (depend on 001 alone); **P7 blocked on 004–010**. Home of the main line (§0b). |

**Status vocabulary.** `specified` = directory created, frozen `spec.md` written, ready
to generate tasks. `planned` = reserved in this registry with proposed pillars; the
directory may exist as a stub, but the spec is not frozen and no tasks may be
generated. `active` = tasks dispatched.

---

## 9. Open risks to this program

- **Denominator fragility.** Three `CLAIMED` denominators underpin the sector's headline
  $/kg and $/kW figures. If 002 cannot convert them, every downstream cost conclusion
  carries an unquantified error bar — and the honest response is to widen the stated
  ranges rather than to keep the precision.
- **Compounding waves.** Wave 2 opens only as 001 closes. 001 is 11% complete after the
  first day, and its remaining 112 tasks are the pacing item for the entire program. If
  001 stalls, the program stalls — wave 2 has no legal slot.
- **Analogue contamination.** Part C borrows reasoning from biotech and railcar-leasing
  analogues. A cost-curve strategy derived from cultivated meat is a *shape* match, not
  sector evidence. 011 must label every borrowed conclusion as borrowed.
- **Short-history tickers.** YSS (10 filings), HAWK (4), VOYG (18), FLY (19) have too
  little history for trend work. Claims about them will be cross-sectional, not
  longitudinal, and must say so.
- **`NOT_READY` supply-chain names.** MOG-A and TDY are the two most-cited coverage
  gaps. If they stay uncovered, 008's supply-chain map has a hole at precisely the
  motion-control and imaging nodes.
