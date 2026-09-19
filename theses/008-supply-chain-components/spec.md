# Research Thesis: 008 — Tier 3b: Space Supply Chain & Components

**Constitution Ref**: constitution.md v1.6.0 (`constitution_pin: 1.6.0`)
**Created**: 2026-09-18 · **Spec written**: 2026-09-19 (placeholder replaced)
**Status**: **PLANNED — Wave 1. Not frozen. Tasks may be generated on activation.**
**Wave**: **1 — promoted at clarify round 2, 2026-09-18 on its own finding** (the margin
ladder says the component layer is where the returns are). Activates under
`max_theses_active: 6`.
**板块**: Tier 3b · **Binding constraint**: `MANUFACTURING_RATE` (candidate — tested in P2)

> **Wave-header correction.** This header previously read *"Swapped in for 003."* That is
> stale and is withdrawn: `PROGRAM.md` records **003 as RESTORED to wave 1** at the
> post-002 sequencing review (reversing the clarify-round-2 demotion), and 002's completion
> vacated the slot 003 occupies — so 003 took a slot *without displacing anyone*.
> **008's promotion never depended on 003's removal and stands on its own finding.** The
> two events are independent and the header now says so.

---

## 0. Inherited baseline

**Paths are relative to the workspace root.** Nothing in this table is re-derived.

### 0a. Inherited results

| Inherited result | 001 artifact | Grade |
|---|---|---|
| **Space-grade solar cells are a two-supplier duopoly**: SolAero (**RKLB**) and Spectrolab (**BA**) — a component every satellite requires, whose efficiency is the **first term in constitution bound F1** | `001-technology-baseline/_cross/phase-3-production-supply.md` §"The critical sub-component" | `DEMONSTRATED` (structure) / **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** (price) |
| **The duopoly's pricing power is unmeasurable from public filings** — neither parent discloses the unit's revenue separately. 001's judgement: *"structural, not priced"*, and a named candidate for `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | `_cross/phase-3-production-supply.md`, carry-forward 3 | `DEMONSTRATED` as a non-disclosure finding |
| **MRCY earns a 0.03% operating margin** — $0.280M on $983.6M revenue, gross $281.2M (28.6%), opex $280.9M, R&D $59.7M. The **component identity reconciles exactly** ($281.165M − $280.885M = $0.280M) | `artifacts/MRCY/2026-09-18_1239_secular-trends_methodology.md` | `DEMONSTRATED` **for that quarter**; the *series* is `CONTESTED` — see §0c(2) |
| **The F4 gate shows no evidence of being priced at all** — radiation tolerance is a billed pure-play requirement whose supplier captures no rent | `artifacts/MRCY/2026-09-18_1239_secular-trends_methodology.md` | `DEMONSTRATED` (one quarter) |
| **R&D intensity separates a development programme from a manufacturing franchise** — FLY 60.8%, PL 35.5%, RKLB 35.2% vs HEI 2.6%, RTX 2.9%, **BWXT 0.5%** | `_cross/technology-baseline_synthesis.md` §4.7 | `DEMONSTRATED` |
| **BWXT's 24× deployed-area reduction (7,499 → 313 m²/MW) is arithmetically available and economically unattached** — *"engineering-sound… physics claim stands; investment claim does not"* | `artifacts/BWXT/2026-09-18_1239_secular-trends_methodology.md` | `MODELED` (area arithmetic) — **a `MODELED` grade can never satisfy a falsifier (P4)** |
| **The margin ladder** — one monotone ordering across eight issuers: HEI 25.5% / KRMN 19.1% / WWD (Aerospace segment) ~17% / LMT 12.4% / RTX 11.4% / LHX 11.1% / NOC 10.1% / GSAT **7.4%** | `_cross/technology-baseline_synthesis.md` §4.1 | `DEMONSTRATED` for seven rungs; **the GSAT rung is SIGN-CORRUPTED** — see §0c(1) |
| **The refined rule** — *component concentration predicts margin when the supplier's revenue spreads across programmes*; **the discriminator is whether the supplier depends on a single programme winning**. The HEI articulation **supersedes** the NOC monopsony version | `_cross/technology-baseline_synthesis.md` §4.1; `artifacts/HEI/2026-09-18_2120_supply-chain_methodology.md`; `artifacts/NOC/…` | `DEMONSTRATED` |
| **The immateriality pattern** — *"capability real, business immaterial"*, 4–5 instances (GOOG, UTHR, MRCY, BWXT, NVDA), suppressing both disclosure and analytical effort | `_cross/technology-baseline_synthesis.md` §4.4 | `DEMONSTRATED` |
| **The tier's economic ordering is inverted relative to narrative** — *"the ordering is exactly inverted relative to narrative"*; no listed issuer offers both growth and margin other than TER and KRMN | `artifacts/KTOS/2026-09-18_2225_supply-chain_methodology.md` | `DEMONSTRATED` |
| **The supplier band is tighter than the prime band while containing more diverse businesses** — CW 19.3% agrees with KRMN 19.1% to 0.2 pts; **margin is position, not cycle** | `artifacts/CW/2026-09-18_2205_supply-chain_methodology.md` | `DEMONSTRATED` |
| **The space supply chain sells into the pure-plays' programmes** — Tier 3 is not an alternative to Tier 1, it is the layer beneath it | `theses/005-launch-spacecraft-services/spec.md` | `DEMONSTRATED` |

**Do not re-derive any of the above.** 008's questions are the four pillars in §1b.

### 0b. Inherited figures this spec consumes — with their state

| Name | Figure as 001 prints it | Where | State for 008's use |
|---|---|---|---|
| HWM | operating margin **27.9%**, R&D **0.3%** | `artifacts/HWM/2026-09-18_1239_supply-chain_methodology.md` | Usable. *"Certified aerospace components carry 28–45% operating margins."* A **disclosure ambiguity is recorded and unresolved** in that artifact — carry it, do not resolve it silently |
| TDG | operating **44.8%**, gross **59.4%** — universe highest | `artifacts/TDG/2026-09-18_1239_supply-chain_methodology.md` | Usable. **Positive control for P2** |
| HEI | operating **25.5%** (Q1 FY2026), R&D 2.6%, least levered (0.85×) | `artifacts/HEI/2026-09-18_2120_supply-chain_methodology.md` | Usable, but **DA-27 applies (n=4 of 4: PL, AVAV, WWD, HEI)** — the fiscal label is derived from the calendar quarter |
| WWD | **~17%, Aerospace segment only** | `artifacts/WWD/2026-09-18_2120_supply-chain_methodology.md` | **`OperatingIncomeLoss` is ABSENT at the consolidated level** — third issuer after MRK and BMY. **The consolidated margin cannot be computed**; the component identity cannot run. Ladder is **graded, not binary** |
| CW | operating **19.3%** (gross 39.4%, R&D 2.7%) | `artifacts/CW/2026-09-18_2205_supply-chain_methodology.md` | Usable |
| KRMN | operating **19.1%** (gross 43.0%), revenue **+58.2%** | `artifacts/KRMN/2026-09-18_2015_supply-chain_methodology.md` | Margin usable; **mechanism NOT established**, and the capital structure absorbs **60%** of operating income ($34.829M OI vs $14.032M NI). **KRMN is Tier 1 by primary revenue — declared cross-tier dependency, see §2** |
| MRCY | operating **0.03%** ($0.280M on $983.6M) | `artifacts/MRCY/2026-09-18_1239_secular-trends_methodology.md` | **Single quarter verified; census CONTESTED — see §0c(2)**. Not usable as the negative control until 002 re-tests all 13 periods |
| KTOS | operating **0.35%** on $458.800M (+30.5%), gross 21.8% | `artifacts/KTOS/2026-09-18_2225_supply-chain_methodology.md` | Usable. **Do not use the EPS bridge as a detector at sub-1% margins** (13.6% artefact) |
| TER | operating **32.9%** on $1,328.990M (**+103.9%**), gross 59.8% | `artifacts/TER/2026-09-18_2205_operational-kpi_methodology.md` | Usable — the **cleanest DA-23 confirmation** in the corpus (exact to the dollar). *"The constraint is not capability. It is queue position."* |
| BWXT | operating margin **12.4%**, R&D **0.5%** | `artifacts/BWXT/2026-09-18_1239_secular-trends_methodology.md` | **TWO-BASIS (DA-30) — an equity-inclusive and an equity-exclusive reading under one concept. Requires a basis field before use** |
| BA | operating margin **0.6%** on `$24,560M` Q2 revenue | `artifacts/BA/2026-09-18_1239_supply-chain_methodology.md` | Usable. **BA is now in this universe (§2) — Spectrolab is one leg of P1** |
| AVAV | — | `artifacts/AVAV/2026-09-18_2225_supply-chain_methodology.md` | **EXCLUDED — all three DA-23 detectors fail** (`net_income_loss` null in every row; `revenues` null in 5 of 10). 001's recommendation stands: *excluded not because its economics are unflattering, but because the platform cannot supply the inputs* |
| MOG-A, TDY, ATRO | — | **no artifact** | **NO DATA.** Three of the 21 Tier 3 names have no coverage. Record the gap; do not proxy |
| TRMB, GRMN, PLTR | — | **no artifact** | **`PARTIAL`** — Tier 3 members with no sector assignment. In the ladder's population only (§2) |
| GSAT | **operating margin 7.4%** | `_cross/technology-baseline_synthesis.md` §4.1 | **WRONG — SEE §0c(1). Do not consume this rung.** |
| PRIMES (LMT/RTX/LHX/NOC) | **12.4% / 11.4% / 11.1% / 10.1%** | `artifacts/RTX/2026-09-18_1239_supply-chain_methodology.md` §2 | Usable at subtotal level. **007's names** — consumed here as declared ladder inputs only (§2, §4) |

### 0c. What this spec-writing pass corrected — three items, two of them blocking

1. **GSAT's ladder rung is a DA-23 sign strip, and the strip is still propagating.**
   001's synthesis prints **+7.4%**; the filed components give `$4.775M / $64.772M` =
   **7.37%** — and 003's report prints **−7.37%, `DEMONSTRATED`**. *Opposite sign,
   identical magnitude to the thousandth* is the DA-23 signature (2 of 2 verified by
   independent arithmetic at SPCX and YSS). **Root cause**: 001 cleared GSAT on the *EPS
   bridge*, which the register rules **inadmissible as a sign test** — and GSAT is
   *"not in 002's universe"* (`theses/002-evidence-validation/entities.md`), so **no DA
   census was ever run on it** (003's `entities.md`: *"PL and GSAT carry NO DA census from
   002"*). GSAT's net income is genuinely positive while its operating line was flipped —
   a **false negative** that a net-income-based check cannot catch. **The corrected rung is
   negative, which strengthens the monopsony reading and changes the ordering.** Every
   inherited margin in this spec was checked against this trap; the 008 rungs are otherwise
   unaffected.
2. **MRCY's 0.03% is a verified quarter inside a contested census.** The Q2 FY2026 figure
   passes the strongest detector **in line**, so its *sign* is right. But the register
   **removed MRCY from the clean row** — 11 of 13 filed periods were stripped. 001's
   artifact declares MRCY clean; the register disagrees. **008 must not use MRCY as its
   negative control until 002 re-tests all 13 periods.** The *contested census* is the
   finding; the *margin* is provisional.
3. **BWXT's rung is two-basis and its clearance was back-solved.** **DA-30**: BWXT files
   operating income both equity-inclusive and equity-exclusive, collapsed into one concept
   with no basis field — and equity is **20.2%** of the Q1 2026 figure. **DA-29**: the
   clearance term **`$90.7M` appears nowhere in the filing** — the instrument's own
   mechanical test (if a term in a reconciliation appears nowhere in the source, the check
   is a back-solve). **Any BWXT figure entering P4 carries its basis explicitly.**

### 0d. What 001 did not do — and why this thesis exists

001 mapped the chain and found the inversions, but it **never priced anything**. It left:
the duopoly's pricing power unmeasured *as a non-disclosure finding rather than a dead
end*; the ladder **eight issuers long, selected by which artifacts happened to get
written**; MRCY's 0.03% as a single-quarter curiosity; and BWXT as arithmetic without a
revenue line. Those four gaps are the four pillars.

### 0e. Validation queue — open before the affected pillar can fire

| # | Item | Blocks | State |
|---|---|---|---|
| 1 | **Correct GSAT's rung to negative** and re-derive the ladder ordering; fix the `+7.4%` in the synthesis and in `PROGRAM.md` if it appears there. Route the sign through 002 (GSAT has no DA census) | **P3** | `blocking` |
| 2 | **Re-test MRCY across all 13 filed periods.** Until then MRCY cannot serve as P2's negative control | **P2** | `blocking` |
| 3 | **Add a basis field to BWXT's operating income** (equity-inclusive vs equity-exclusive, DA-30) and re-derive the clearance without the back-solved term (DA-29) | **P4** | `blocking` |
| 4 | **WWD: confirm `OperatingIncomeLoss` is genuinely absent at the consolidated level** (third issuer after MRK, BMY). If so, WWD's ladder rung is **segment-only and permanently graded** | **P3** | `blocking` |
| 5 | **BA: obtain the Spectrolab disclosure state directly** — confirm the unit has no separate revenue line in the 10-K segment note *and* in the MD&A (a negative claim needs a positive search) | **P1** | `blocking` |
| 6 | **Solar duopoly: search both legs for any capacity, backlog, unit-price or qualification disclosure** — the P1 falsifier is a count, so the search must be exhaustive and its negative register kept | **P1** | `warn` |
| 7 | **Confirm the prime rungs are component-identity-clean**, not EPS-bridged (001's LMT artifact shows only the EPS bridge, which is inadmissible) | **P3** | `warn` |
| 8 | **MOG-A / TDY / ATRO** — confirm the no-data state is current before recording them as gaps | **P3** | `warn` |

---

## 1. Research Question

**Across the component and subsystem layer, does anyone convert a genuine bottleneck into
pricing power — or does every node in this chain compete away its own scarcity?**

The thesis is the *test* of that question, not an assertion of an answer. 001's evidence
currently points at **no** — MRCY earns 0.03% on a billed F4 requirement, KTOS 0.35%, and
the ordering is inverted relative to narrative — but the negative rests on a contested
census and an eight-name sample. **008 exists to make the negative load-bearing or to break
it**, and either outcome is a result.

---

## 1b. Pillars

**Four pillars.** Each has a different claim-test, a different source, and an owner. No
pillar is absorbed from another thesis (§5).

### Pillar 1 — The space-grade solar-cell duopoly: both legs, structure versus price (Priority: P1)

**Claim.** SolAero (**RKLB**) and Spectrolab (**BA**) are the two suppliers of a component
every satellite requires, and whose efficiency is **F1's first term**. The structure is
`DEMONSTRATED`. The price is not: **neither parent discloses the unit**, so the duopoly's
pricing power is either (a) genuinely immaterial to both parents — BA's **0.6%** consolidated
margin and its `$24,560M` quarterly revenue make the unit invisible *by parent size*, and
RKLB's consolidated margin makes it invisible *by parent scale* — or (b) a disclosure gap
that capacity, backlog or qualification language would close. **The pillar decides which**,
and it decides it **on both legs, not one.**

**Why this priority.** It is the tier's clearest structural bottleneck and it is the
programme's most-cited unpriced finding. It is also the question 005 moved here: 005 holds
the pure-play **RKLB** leg, 008 holds **both** legs — this pillar and the BA leg are why
**BA is in this universe** (§2).

**Ownership.** Moved from 005's Pillar 5 at the v1.6.0 re-cut. 005's earlier *"the BA leg
belongs to 007"* line was **stale** and is now **corrected in 005** — it assigns
BA/Spectrolab to **008** and carries it under §2b cross-tier dependencies. 007's universe no
longer carries BA either. Verified by grep across 005, 007 and 008 at the close of this
pass: no `BA → 007` attribution survives anywhere.

**Falsifier (inherited verbatim from 005's P5).**
**wrong_if**: `metric=count_of_disclosed_space_grade_solar_cell_unit_revenue_price_capacity_or_backlog_figures_in_universe_filings threshold=0 source=10-K_10-Q_or_earnings_call_transcript op=>`

**Subscribed**: `RKLB × supply-chain`, `RKLB × competitive`, `BA × supply-chain`,
`BA × competitive`, `BA × business-model`, `BA × recent-quarter`, `RKLB × recent-quarter`.

**Verdict vocabulary.** If the count stays zero and both parents' unit economics cannot be
isolated, the correct disposition is **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — which is a
finding, and one that transfers directly to the price of every satellite programme the pure-
plays are underwriting. If it is `UNRESOLVABLE-FROM-PLATFORM`, that is a different and
remediable claim, and the two must not be conflated.

### Pillar 2 — The bottleneck-to-pricing-power test: does a demonstrated moat earn rent? (Priority: P2)

**Claim.** A supplier holding a genuine, physics-grounded advantage should show it in margin
*direction* under revenue growth. **MRCY is the sharpest test**: it holds the billed F4
(radiation-tolerance) advantage and earns **0.03%**. **TDG is the positive control** — the
tier's pricing-power benchmark, and the test of whether the defence-component model
transfers to space at all. The refined rule from 001 governs: **the discriminator is
single-programme dependence, not buyer concentration** (HEI 25.5% supersedes NOC's monopsony
articulation), reconciled against TDG 44.8% / HWM 27.9%.

**Why this priority.** It converts 001's inversion observation from an anecdote about eight
issuers into a tested rule about the tier's economics — and the negative is falsifiable,
which is what makes it worth running.

**Independently falsifiable.** Yes — mechanically, on MRCY against the tier median.

**wrong_if**: `metric=max_mrcy_operating_margin_over_last_four_clean_quarters_minus_tier_median_operating_margin threshold=0 source=10-Q_consolidated_income_statement_component_identity_clean op=>`

*(The condition fires if MRCY ever exceeds the tier median — i.e. if the moat does earn
rent.)* **Gated on §0e(2)**: until MRCY's 13-period census is
re-verified, this falsifier cannot fire, and **an unfireable pillar is a pillar that cannot
do work** — so the census is the first task, not a caveat.

**Subscribed**: `MRCY × ratio-analysis`, `TDG × ratio-analysis`, `HWM × ratio-analysis`,
`HEI × ratio-analysis`, `CW × ratio-analysis`, `KTOS × ratio-analysis`, `TER × ratio-analysis`,
`TDG × competitive`, `HEI × competitive`, `MRCY × competitive`.

**Boundary conditions.** (a) `DA-21` — each issuer's segment definitions are its own; no
cross-issuer segment aggregation. (b) **The EPS bridge is inadmissible as a sign test**
above all at sub-1% margins, where it produces artefacts (KTOS: 13.6%). (c) Margin
*direction* requires more than two periods — quarterly sequencing with the **DA-26** check
(an ANNUAL figure mislabelled as a quarter; 20 tested, 19 exhibiting; FLY the falsifying
counterexample) and **DA-27** (fiscal labels derived from calendar quarters, n=4 of 4).

### Pillar 3 — The margin ladder's monotonicity, extended to all 21 Tier 3 names (Priority: P3)

**Claim.** 001's ladder — one monotone ordering across eight issuers — is either a property
of the tier or an **artefact of an eight-name sample chosen by which artifacts happened to
get written**. 011's pressure test could not resolve the selection concern. **This pillar
resolves it by recomputing the ladder across the full 21-name Tier 3 population and reporting
the ordering with its rank correlation** against distance-from-programme-risk and against
revenue recurrence (aftermarket share).

**Why it is its own pillar, split out of the old workstream 5.** It is a **different
claim-test** from P2: P2 asks *whether a bottleneck earns rent*; P3 asks *whether the
ordering of rents is real or sampled*. Different metric, different source, different failure
mode, and P3 **spans 007's four primes**, which P2 does not. Running them as one workstream
would let a sampling artefact hide inside a pricing-power conclusion.

**This is a reconciliation job, not a lookup.** 001 prints values in prose for only some
names, and prints **11 of the 21** named margins. The state of every rung:

| Issuer | Tier | 001's printed rung | State entering P3 |
|---|---|---|:---|
| BA | 3b | 0.6% | Usable |
| HWM | 3b | 27.9% | Usable — disclosure ambiguity recorded, unresolved |
| TDG | 3b | 44.8% | Usable — universe highest |
| HEI | 3b | 25.5% | Usable — **DA-27** applies |
| WWD | 3b | ~17% | **Segment-only.** `OperatingIncomeLoss` absent at the consolidated level (after MRK, BMY) → **permanently graded, not binary** |
| CW | 3b | 19.3% | Usable — agrees with KRMN to 0.2 pts |
| KTOS | 3b | 0.35% | Usable — EPS bridge inadmissible here |
| MRCY | 3b | 0.03% | **Single quarter verified; census CONTESTED (11 of 13 stripped)** |
| AVAV | 3b | **excluded** | **All three detectors fail** — the platform cannot supply the inputs |
| TER | 3b | 32.9% | Usable — cleanest DA-23 confirmation |
| BWXT | 3b | 12.4% | **TWO-BASIS (DA-30); clearance BACK-SOLVED (DA-29)** |
| MOG-A / TDY / ATRO | 3b | — | **NO DATA** (three of 21) |
| TRMB / GRMN / PLTR | 3b | — | **`PARTIAL`** — sector assignment required by hand, not by screen |
| **GSAT** | *not Tier 3* | **7.4%** | **SIGN-CORRUPTED — filed is −7.37% (§0c(1)). Correct before recomputing the ordering** |
| KRMN | **1** | 19.1% | Cross-tier — see §2 |
| LMT / RTX / LHX / NOC | 3a | 12.4 / 11.4 / 11.1 / 10.1% | **007's names**, consumed as declared ladder inputs only |

**Sector-taxonomy hazard, load-bearing for the population count.** **BWXT** files under
`industrial.nuclear_energy`, **TER** under `tech.semiconductors`, and **GSAT** under
`tech.tech_hardware`. **A screen on `aerospace_defense` will silently drop them** — 001
documented the trap and this pillar's 21-name population is only complete if the screen is
name-driven, never sector-driven.

**wrong_if**: `metric=spearman_rank_correlation_between_ladder_position_and_distance_from_programme_risk_on_the_extended_tier_3_ladder threshold=0.5 source=recomputed_operating_margins_all_21_tier_3_names_component_identity_clean op=<`

**Report the ordering whichever way it falls.** A non-monotone fuller ladder narrows or fails
011's P1 mechanism claim, and reporting that is worth more than defending the claim. **This
pillar is where the programme is most likely to learn it was wrong, and that is its value.**

**Subscribed**: `ratio-analysis` across the full 21-name population at Standard depth;
`recent-quarter` on every name whose ladder rung moves the ordering; `peer-bench` for the
cross-tier comparison against 005's pure-plays.

### Pillar 4 — R&D intensity, and the BWXT escape hatch as a *monitored condition* (Priority: P4)

**Claim.** R&D/revenue separates a **development programme** from a **manufacturing
franchise**, and it separates the tier **into two regimes with no middle**: developers
(FLY 60.8%, PL 35.5%, RKLB 35.2%) against franchises (HEI 2.6%, RTX 2.9%, **BWXT 0.5%**).
Applied across the tier, the distribution says who is actually building space capability and
who is harvesting an installed base.

**BWXT is explicitly a monitored condition, not a pillar.** The 24× deployed-area reduction
(7,499 → 313 m²/MW) is **`MODELED`** arithmetic; under **P4 a `MODELED` grade can never
satisfy a falsifier**, and there is no space-nuclear revenue line, no segment and no R&D
signature to test against. **Writing a pillar here would manufacture a claim the data cannot
falsify.** It is instead recorded with three named triggers, any of which *creates* a pillar:
(i) a disclosed space-nuclear revenue or backlog line; (ii) an R&D step-change from 0.5%;
(iii) a named programme with a government customer. **F2 ownership stays with 009/001
PIL-2** — 008 owns BWXT the company, not the thermal physics bound.

**wrong_if**: `metric=count_of_tier_issuers_with_rd_intensity_between_5_and_20_percent_of_revenue threshold=0 source=10-Q_income_statement_rd_line op=>`

*(The claim is bimodality. A populated middle band falsifies it.)*

**Subscribed**: `secular-trends` across the tier; `unit-economics` at BWXT and TER;
`business-model` at the franchise pole (HWM, HEI, BWXT) against the developer pole (RKLB,
PL, FLY — read from 005/001 artifacts, not re-derived).

---

## 1c. Candidate binding constraint — `MANUFACTURING_RATE`

**To be tested in P2, not asserted.** The tier's constraint is production throughput and
unit cost, not demand — the evidence is YSS's 24.0% gross margin against a 68.6% opex ratio
(**2.9× fixed-cost multiple**: a scale problem, not a unit-economics problem), PL's 53.5%
gross margin against 90.6% opex (**1.69× break-even**), and TER's *"the constraint is not
capability. It is queue position."* **If P2 finds the tier competing its scarcity away at
every node, `MANUFACTURING_RATE` is not a binding constraint either — it is an absence of
one**, and the thesis must say so rather than keep the label.

---

## 2. Universe Definition

**Weights are analytical effort, not positions.** Market Data Stage is `none` across the
filings-based work; see §3 for the exceptions.

### 2a. The component and subsystem layer (deep coverage)

| Ticker | Company | Sector | Sub-sector | Weight | Pillar |
|---|---|---|:---:|:---:|
| MRCY | Mercury Systems | industrial.aerospace_defense | Space Components & Subsystems | 12% | P2 (negative control), P3 |
| TDG | TransDigm | industrial.aerospace_defense | Space Components & Subsystems | 12% | P2 (positive control), P3 |
| HWM | Howmet Aerospace | industrial.aerospace_defense | Space Components & Subsystems | 11% | P2, P3 |
| HEI | Heico | industrial.aerospace_defense | Space Components & Subsystems | 11% | P2, P3 |
| CW | Curtiss-Wright | industrial.aerospace_defense | Space Components & Subsystems | 10% | P2, P3 |
| WWD | Woodward | industrial.aerospace_defense | Space Components & Subsystems | 9% | P2, P3 (graded rung) |
| TER | Teradyne | **tech.semiconductors** | Space Components & Subsystems | 9% | P2, P3, P4 |
| KTOS | Kratos Defense | industrial.aerospace_defense | Space Components & Subsystems | 9% | P2, P3 |
| BWXT | BWX Technologies | **industrial.nuclear_energy** | Space Components & Subsystems | 8% | P4 (monitor), P3 (two-basis) |
| AVAV | AeroVironment | industrial.aerospace_defense | Space Components & Subsystems | 4% | P3 only — **excluded from the ladder on input availability** |
| **BA** | **Boeing** | industrial.aerospace_defense | Diversified Primes & Defense-Space | **5%** | **P1 — the Spectrolab leg.** BA is here for *one question only*; its 0.6% consolidated margin and its prime-level economics belong to no pillar of this thesis |

**BA's addition, and its limit.** BA enters this universe as **the second leg of P1's
duopoly**, moved in by the ownership table (BA / Spectrolab → 008). It does **not** bring
prime-level analysis with it: the diversified-prime multiple-dilution question is **007's**,
and 007's universe no longer carries BA. **The scope of BA here is Spectrolab.** Nothing
else about Boeing is in scope.

### 2b. `NOT_READY` — no data (record the gap; do not proxy)

| Ticker | Company | Gap |
|---|---|---|
| MOG-A | Moog | Space/defense motion control, satellite components. **Also carries a fund-sourced corpus case — Brown Advisory, ~2.1–2.5× on cost, ~28–38% IRR — with no issuer coverage. A case that cannot be validated against filings is a research liability, not an asset; record the asymmetry** |
| TDY | Teledyne | Space imaging and IR detectors |
| ATRO | Astronics | Power distribution and lighting |

These three are **Tier 3 members with no coverage**. They appear in P3's population as
**named absences**, and the ladder must report its population as **18 of 21 measurable, 3
absent** rather than silently running on the available names. The two most-cited gaps in the
tier are **MOG-A and TDY**.

### 2c. Ladder-only population (`PARTIAL`)

**TRMB, GRMN, PLTR** are Tier 3 members that no sector screen will assign — the constitution
records them as `PARTIAL` with *"sector must be assigned by hand."* They are **not** in this
thesis's supply-chain scope, but they **are** in P3's 21-name population, because the ladder
is a Tier 3 fact and the population is not optional. **P3 carries them at rung-only depth.**

### 2d. Declared cross-thesis and cross-tier inputs

| Name | Tier by primary revenue | 008's claim |
|---|---|---|
| **KRMN** (Karman Holdings) | **Tier 1** (constitution §Tier 1) | **DECLARED CROSS-TIER DEPENDENCY.** KRMN's primary revenue is launch/space hardware; **primary depth belongs to 005**, which carries it at 9%. 008 uses **only its ladder datum** (19.1%, gross 43.0%, +58.2% growth). The capital-structure fact — **60% of operating income absorbed** below the operating line — is recorded as context and is **not** an 008 finding. Under the constitution's cross-tier rule a spanning name is never absorbed as a pillar of the host thesis |
| **LMT, NOC, LHX, RTX** | **Tier 3a** | **007's names.** Consumed as **declared ladder inputs** for P3 only. 008 does not compute prime segment margins, does not run an SOTP, and does not touch the multiple-dilution question |
| **PL, RKLB, YSS, FLY** | Tier 1 / Tier 2 / others | Read from 001/005 artifacts for the developer pole in P4. **Not re-derived** |

---

## 3. Skill Deployment Matrix

| Skill | Vertical | Depth | Tickers | Market Data Stage | Pillar |
|---|---|---|---|:---:|:---:|
| `supply-chain` | equity-research-core | Deep | RKLB, BA | `none` | P1 — the duopoly's structure and the disclosure search |
| `competitive` | equity-research-core | Deep | RKLB, BA; Standard elsewhere | `none` | P1 (both legs), P2 (the rule) |
| `business-model` | equity-research-core | Standard | BA, RKLB, HWM, HEI, BWXT | `none` | P1, P4 — franchise versus developer |
| `ratio-analysis` | quantitative-analysis | **Deep across 21 names** | full Tier 3 population | `none` | P2, P3 — the ladder recomputation |
| `recent-quarter` | equity-research-core | Standard | every name whose rung moves | `none` | P2, P3 — DA-26 and DA-27 sequencing |
| `peer-bench` | equity-research-core | Standard | tier vs 005's pure-plays | `late` | P3 — is the supplier band really tighter than the prime band |
| `secular-trends` | equity-research-core | Standard | BWXT, TER, TDG, HEI | `none` | P4 — who is building capability |
| `unit-economics` | equity-research-core | Light | BWXT, TER, YSS (read) | `none` | P4 — franchise economics, break-even multiples |
| `operational-kpi` | equity-research-core | Light | TER, YSS (read) | `none` | P4 — queue position as the real constraint |
| `risk` | equity-research-core | Light | all | `none` | Every pillar — DA-23/29/30 discipline |
| `comps` | quantitative-analysis | Light | tier | `late` | Conditional — only if P2 finds a node with expanding margin |

**Market Data Stage.** The work here is filings-based (`none`). `peer-bench` and `comps`
need prices and a **keyless NASDAQ feed is available to the platform — do not assume `none`;
check the skill registry's true stage per skill** before scheduling. 004 established the same
for its valuation skills.

---

## 4. Dependencies

| Thesis | Dependency |
|---|---|
| **002** | **Mandatory.** Every ladder rung is computed under the Data-Integrity Register: **DA-23** (component identity — *the sign is never taken from XBRL alone*), **DA-24** (non-operating contamination), **DA-25** (normalised per-unit metrics), **DA-26** (annual mislabelled as quarterly), **DA-27** (fiscal label from calendar quarter), **DA-29** (back-solved checks), **DA-30** (two bases on one concept). **002 owns the census** — 008 does not re-run it, and P2's falsifier is blocked until 002 re-tests MRCY |
| **005** (Tier 1) | **The layer beneath this one.** The supply chain sells into the pure-plays' programmes. **005 relinquished the solar duopoly to this thesis; the RKLB leg is now shared, with the BA leg wholly here.** 005's *"the BA leg belongs to 007"* line is **stale** and should be corrected to 008 |
| **007** (Tier 3a) | **The sibling half, and the constitution says the split is deliberate** — 20+ names is too many for one spec, and the two halves ask different questions. **007 owns diversified-prime multiple dilution; 008 owns the component layer, the duopoly, BA/Spectrolab and the ladder.** 007 supplies the four prime rungs to P3 as a declared input; 008 supplies no pillar to 007 |
| **009** (Tier 4) | **008 ∩ 009 = ∅. There is no shared name.** *The previous version of this section claimed "some names sit in both" — that was false, and it is corrected here: the two universes were compared name-by-name against constitution §Tier 3 and §Tier 4 and the intersection is empty. **VRT — the one name that could have created an overlap — was moved OUT of Tier 4 membership at v1.6.0 to a named comparator role, and was never in 008's universe.*** **The real adjacency is conceptual, not membership**: 009 owns the enabling layer (power, thermal, compute) that this tier's components are sold *into*, and 009/001 PIL-2 own the **F2** thermal bound that BWXT's nuclear arithmetic touches. 008 owns BWXT the company; 009 owns the physics bound. Neither re-derives the other's |
| **010 / 011** | 011 graded the ladder and assigned the extension to 008 (it grades positions; it does not re-research businesses). 010 consumes power/thermal conclusions, not component margins |

---

## 5. Cross-Cutting — ownership boundaries

Each question has exactly one owner. 008 is the broadest universe in the programme and the
one most exposed to pillar theft; these boundaries are enforceable.

| Question | Sole owner | 008's relationship |
|---|---|---|
| Solar-cell duopoly & pricing power (**both legs**) | **008** | **Owned here** |
| BA / Spectrolab | **008** | **Owned here** — BA's only presence in any Tier 3 spec |
| The margin ladder's monotonicity | **008** | **Owned here** (P3), spanning all 21 names |
| Diversified-prime multiple dilution | **007** | **Not 008's.** 008 consumes prime *margins* as ladder inputs and runs no SOTP |
| Operator margins by segment | **006** | **Not 008's** — no operator is in this universe |
| Financing runway / fixed-cost absorption | **005** | **Not 008's** — 008 reads break-even multiples (YSS 2.9×, PL 1.69×) as cited context and computes none |
| Launch-cost curve / value migration | **003** | Not re-derived |
| Radiation/thermal physics bounds (F2, F4) | **001 / 009** | 008 owns the *suppliers* (MRCY, BWXT); the bounds stay with 001/009 |
| IRDM/RKLB deal gate chain | **006** | Not in this universe as a deal question |

---

## 6. Output Contract

1. **A duopoly disclosure register** for P1 — every place both parents could have disclosed
   the unit, searched, with what was and was not found. A negative claim is only worth the
   search behind it.
2. **The extended ladder** — all 21 Tier 3 names, each rung carrying its **basis**, its
   **grade** and its **clean/contested state**; the three absences named; AVAV's exclusion
   stated with its reason (input availability, not economics); WWD's rung marked permanently
   segment-only; BWXT's rung carrying its equity basis.
3. **The rank correlation** against distance-from-programme-risk and revenue recurrence,
   reported with its population (18 measurable of 21) and its uncertainty.
4. **The corrected ordering** — with GSAT's rung negative and the effect on the ordering
   stated explicitly.
5. **A `MANUFACTURING_RATE` verdict** — tested, not assumed.
6. **A disposition per pillar**, including the `UNRESOLVABLE-FROM-PUBLIC-SOURCES` versus
   `UNRESOLVABLE-FROM-PLATFORM` distinction wherever a figure cannot be obtained.

---

## 7. Thesis Phases

| Phase | Content | Gate |
|---|---|---|
| 1 | §0e validation queue — items 1–5 are `blocking` | Blocks everything |
| 2 | P1 — the disclosure search on both legs, with the negative register | Independent |
| 3 | P3 — the ladder recomputation across 21 names, on reconciled bases | Independent of P2 |
| 4 | P2 — the bottleneck test, **gated on MRCY's census** | Blocked until §0e(2) |
| 5 | P4 — R&D distribution, BWXT monitors registered | Independent |
| 6 | Output contract, `MANUFACTURING_RATE` verdict, dispositions | — |

**Clarifications**

- **2026-09-19** — Placeholder replaced. Changes: **BA added** to §2 as the Spectrolab leg
  of P1; the **solar-cell duopoly absorbed from 005** with **both legs** and 005's P5
  falsifier inherited verbatim; the old workstream 5 **split into its own pillar (P3)**
  because extending the ladder is a different claim-test from the pricing-power question and
  **spans 007's primes**; the **false dependency claim removed** (*"some names sit in both"*
  → **008 ∩ 009 = ∅**, verified name-by-name); the **stale wave header corrected** (003 was
  RESTORED to wave 1; 008's promotion stands on its own finding); the **BWXT nuclear escape
  hatch demoted from a workstream to an explicitly monitored condition** because a `MODELED`
  grade can never satisfy a falsifier under P4; three corrections to 001 recorded in §0c
  (**GSAT's rung is sign-corrupted to −7.37%**; MRCY's census is contested; BWXT is two-basis
  and back-solved); KRMN marked a **declared cross-tier dependency** on Tier 1/005 rather
  than absorbed; a **validation queue** added with five `blocking` items; constitution
  reference moved v1.4.0 → v1.6.0.
