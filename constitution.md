---
# The constitution's writer. `amend` is the owner's deliberate rewrite;
# any other writer's write to this file is refused. The same rule governs
# the thesis instruments — see contracts/thesis.md.
writer: agentii.constitution
---

<!--
Sync Impact Report (spec 046 Q33 — executable input, not decoration):
  version: 1.4.0 → 1.5.0
  amended: §Data-Integrity Register — TWO NEW ENTRIES, and both are a different KIND
           from DA-23…DA-28. Those describe defective DATA. DA-29 describes a defective
           CHECK; DA-30 describes a basis the PLATFORM collapses before any artifact
           sees it. Neither could have been violated by an artifact written earlier,
           because neither rule existed — but both name obligations no existing
           artifact discharged, which is why this is a MINOR bump and not a PATCH.
  added: DA-29 BACK-SOLVED AND OPAQUE CHECKS, carrying THE MECHANICAL CIRCULARITY
         TEST: *if any term in a reconciliation appears NOWHERE in the source, the
         check is a BACK-SOLVE.* Three instances registered: (1) 001's BWXT clearance,
         assembled from a `$90.7M` term that appears in no filing — the filed Total
         Costs and Expenses is $775.1M, and the check nevertheless CLOSED; (2) the
         instrument's `computed` column is not reproducible from the instrument's own
         returned tree (Q1 2026 operating income: computed 71,139,000 vs tree
         106,691,000, internally inconsistent within one run); (3) three `reported`
         mis-selections in a single filing, including PP&E `reported` carrying GROSS
         for a NET concept. Consequence: `computed` may not be cited as a derivation,
         and `reported` is not definitionally the filed value.
  added: DA-30 TWO BASES ON ONE CONCEPT, COLLAPSED WITHOUT A BASIS FIELD. BWXT files
         operating income equity-inclusive and equity-exclusive under one concept;
         equity is 20.2% of the Q1 2026 figure. This is PRIOR TO the artifact
         contract's `no_single_basis_collapse` rule — that rule governs an artifact
         quoting one basis; here the platform has already collapsed two, so an
         artifact cannot comply by diligence alone. It must first discover a second
         basis exists.
  corrected: DA-23's census. BWXT moves from **Clean** to a new row —
         **CLEAN AT EVERY SUBTOTAL, STRIPPED AT A COMPONENT**, the first issuer where
         both are simultaneously true. `GainLossOnSalesOfAssetsAndAssetImpairmentCharges`
         is served as an absolute magnitude (4 of 4 verified losses stripped, 3 of 3
         gains untouched, 0 negatives in a 29-fact series over six fiscal years), with
         the exact strip signature `diff = 2 x 125` — and `status` marked the row
         `pass`. **A census testing only parent concepts reports a clean issuer while a
         component of the same statement is sign-corrupted.**
  corrected: DA-23's detector-availability note, from ONE axis to TWO. The register
         recorded only "gross profit is absent" and the coverage hole was phrased that
         way. The second axis is whether `OperatingIncomeLoss` is a filed first-class
         consolidated subtotal. **BWXT is RESOLVABLE (with LUNR) despite filing no
         gross-profit line — MRK, BMY and WWD are not. A single-axis flag would bucket
         BWXT with MRK when their dispositions are OPPOSITE.** Also recorded: the
         absence is PRESENTATIONAL (BWXT files CostOfGoodsAndServicesSold), and two
         independent NAME TRAPS sit on the detector — `GrossProfit` and plain
         `Revenues` each return 0 facts — so **a zero-fact return is evidence about the
         CONCEPT NAME, not about the ISSUER.**
  NOT amended: no principle, axiom, bound, disposition class or sector bias changes.
           Every bias and every falsifier stands as written at 1.4.0.
  deferred: the DA-29/DA-30 obligations are NOT discharged by any of the 23 artifacts
            written at pin 1.4.0 — none names the source of every reconciliation term,
            and none names an operating-income basis. Per the 1.3.0 precedent this is
            REPORTED and NOT separately dispatched: the obligation is folded into
            Phase 7's validation ledger, which is the artifact whose function is
            exactly this census. All 23 remain valid at their recorded pin; none is
            silently re-run (Q56 filesystem-as-checkpoint).
  Re-examination scope: bounded to artifacts that read `operating_income` or cite a
  reconciliation — the class DA-29/DA-30 bind. Everything else is untouched.
-->

<!--
Sync Impact Report (spec 046 Q33 — executable input, not decoration):
  version: 1.3.0 → 1.4.0
  amended: §Sector Preferences — three rows restated. The v1.3.0 A1a/A1b split was not
           propagated to this table, leaving it internally contradictory: Launch
           Services was Overweight/High on the rationale "The toll road", which IS
           A1b — the axiom v1.3.0 declared falsified. Space Infrastructure & Components
           was Neutral/Medium on "high program-concentration risk; a single program
           cancellation can reset estimates", which inverts the measured mechanism:
           the component layer holds the margin ladder's top rungs (HEI 25.5%, KRMN
           19.1%, ~2x the primes they supply) and the refined discriminator is
           SINGLE-PROGRAMME DEPENDENCE, not buyer concentration. Earth Observation
           was Underweight/Low on "persistent negative unit economics", refuted by PL's
           53.5% gross margin — the best in the universe — with the loss arising from
           fixed-cost absorption (opex 90.6%, break-even 1.69x current revenue).
  NOT amended: every bias is retained. Launch stays Overweight/High, restated on an
           A1a-consistent basis (unit economics and the cost curve, not value
           accrual); Space Infrastructure stays Neutral/Medium because the layer is
           not space-pure (HEI runs 2.6% R&D); Earth Observation stays Underweight/Low
           as a TIMING judgment rather than a structural one. This is a rationale
           correction, not a reallocation — no wave ordering or position cap changes.
  added: the reinforcement notes on Space Compute (the orbital-compute
         disconfirmation is now positive, not an absence) and Microgravity (the 73x
         demand asymmetry), and the margin-ladder pricing of the primes tier.
  corrected: nothing numeric. No figure previously stated is revised.
  removed: nothing.
  deferred: (a) IG/HY credit-spread level — STILL unsourced, and now the only
            pre-trade-idea blocker carried across three amendment eras; (b) ERP and
            terminal-growth remain provisional model inputs; (c) private-company
            valuations remain CLAIMED under P4; (d) thirteen universe names remain
            NOT_READY, and the MOG-A / ENS asymmetry (corpus cases, no issuer
            coverage) is now recorded as an acquisition priority in 011's amendment
            candidates rather than only here.
  Re-examination scope: 001-technology-baseline (pin 1.2.0) and the five wave-1 theses
  specified at pin 1.3.0 are marked `stale` by this MINOR bump. Scope is bounded to
  the Sector Preferences table, which only theses that cite a sub-sector bias depend
  on: 002 (no bias citations), 003, 005, 006, 011. The artifacts already written are
  unaffected — no artifact quotes a sub-sector bias. Reported for the gate-5 budget
  confirm; NOT dispatched.
-->

<!--
Sync Impact Report (spec 046 Q33 — executable input, not decoration):
  version: 1.2.0 → 1.3.0
  amended: A1 — split into A1a (launch cost is the master COST variable) and A1b
           (launch is the master VALUE variable). A1b does NOT hold on current
           disclosure: three independent issuers show revenue growth with flat or
           declining launch revenue. This is a split, not a redefinition — A1a
           preserves the founding axiom's binding half.
           F5 — split into F5a (fully reusable: propellant floor, hard) and F5b
           (partially reusable: upper-stage manufacturing floor, soft). F5 as
           written bounds Starship-class vehicles only; applying it to Falcon-class
           vehicles is a category error, since propellant is ~2–3% of Falcon 9's
           marginal cost while the expended second stage dominates.
  added: §Data-Integrity Register (P4) — SIX measured defects in the platform's
         period-and-sign extraction layer, each with a census, a discriminator and
         a remedy. The register's scope is broader than sign: it covers any
         extraction failing the gross-profit bound.
         DA-23 SIGN STRIPPING — 6 of 6 loss-making issuers return negative
         operating income as positive of identical magnitude; 19 of 19 profitable
         issuers unaffected; zero exceptions on either side. An INVERSION, not a
         footnote: every `operating_income` ranking places the worst loss-makers
         first. THREE detectors now registered in descending reliability — the
         component identity (fully reliable), the gross-profit bound (new;
         strictly stronger than sign reconciliation WHERE GROSS MARGIN IS LOW — its power
         scales INVERSELY with gross margin, so it is near-useless at high-margin issuers
         (a false negative at every level at SPCX, ~65% GM; 4 of 4 at FLY, ~20% GM).
         §CORRECTED at 002 Phase 3: VOYG does NOT fail it — see the entry below
         across three consecutive quarters), and margin plausibility (weakest).
         The EPS x shares test is INADMISSIBLE — it passes on both sides of a flip
         at RKLB, FLY and VOYG. Three open candidates (BA 2025 Q3, LUNR, VOYG),
         and a COVERAGE HOLE: OperatingIncomeLoss is absent or segment-only at
         MRK, BMY and WWD, where no detector can run and absence must be recorded
         as UNRESOLVABLE-FROM-PLATFORM rather than as a passed check.
         DA-24 ASSET-SALE CONTAMINATION (EchoStar 2025 Q3 operating income = 4.6x
         revenue). DA-25 NORMALISED PER-UNIT METRICS. DA-26 ANNUAL MISLABELLED AS
         QUARTERLY — universal, 19 of 19 issuers [⚠️ SUPERSEDED at v1.6.0 —
         corrected to "20 tested, 19 exhibiting; FLY is the falsifying
         counterexample". This entry is the record of what was decided at v1.3.0 and
         is NOT rewritten; the live claim is in §Data-Integrity Register]; the
         mislabelled period VARIES by
         issuer so it cannot be screened by position; it is a whole-statement
         failure (at AMGN the Q4 row carries the annual for revenue AND operating
         income). DA-27 FISCAL-PERIOD LABELS DERIVED FROM THE CALENDAR QUARTER —
         n = 4 of 4, partitioning the population perfectly by fiscal year-end;
         distinct from DA-26 (wrong LABEL on internally-consistent values vs wrong
         VALUE in a quarter row) and catastrophically compounding with it at
         non-calendar issuers. DA-28 IPO CAPITAL-STRUCTURE DISCONTINUITY
         invalidates share-count detectors (HAWK: four share counts in one
         extract; EPS bridge fails by 72% against sub-1% for every clean issuer) —
         so the DA-23 detector requires a listing-date guard or it produces false
         positives on recent listings. Independences established: SATS exhibits
         DA-24 without DA-23; HWM is clean on DA-23 and exhibits DA-26.
         §Disposition Classes (P4) — adds `UNRESOLVABLE-FROM-PLATFORM` as a class
         distinct from `UNRESOLVABLE-FROM-PUBLIC-SOURCES`. The former is data that
         is public but unreachable or commercially licensed; the latter is data
         that does not exist publicly at all. The two demand different remedies
         and were previously conflated.
  corrected: nothing. No figure previously stated in this document is revised.
  removed: nothing.
  deferred: (a) IG/HY credit-spread level — STILL unsourced, now blocking a
            seventh consecutive era; must be populated before the first trade idea;
            (b) ERP and terminal-growth remain provisional model inputs;
            (c) private-company valuations remain CLAIMED under P4;
            (d) thirteen universe names remain NOT_READY — and two of them, MOG-A
            and ENS, now have fund-sourced cases in the knowledge corpus while
            carrying no issuer coverage. That asymmetry is recorded as a corpus
            acquisition priority, not a coverage change.
  Re-examination scope: 001-technology-baseline is pinned at 1.2.0 and is marked
  `stale` by this MINOR bump. Scope is the pillars depending on amended principles:
  PIL-1 and PIL-3 (A1a/A1b, F5a/F5b) and PIL-5/PIL-6 (disposition classes), plus
  every artifact whose conclusions rest on a DA-23-sensitive `operating_income`
  read. Bounded precisely: the 14 artifacts already written each IDENTIFIED the
  DA-23 defect in-line and carry in-place corrections, so re-examination is a
  confirmation pass, not new research. The 112 unrun tasks regenerate against
  1.3.0 natively and require no re-examination. This scope is reported for the
  gate-5 budget confirm; no dispatch has occurred.
-->

<!--
Sync Impact Report (spec 046 Q33 — executable input, not decoration):
  version: 1.1.0 → 1.2.0
  amended: Universe Definition — the Data column is replaced by an audited,
           three-class agent-coverage classification (READY / PARTIAL / NOT_READY)
           derived from per-ticker get_ticker_coverage across all seven source types;
           the "unverified for Tiers 3–4" caveat is now discharged.
  added: Principle Register (Section 0b) — maps every P-number to the section that
         defines it, and retires five phantom identifiers (P1, P5, P7, P8, P9) that
         were declared in the 1.0.0 Sync Impact Report but never given a body
         definition. No new principle is created: each maps to existing substance.
         Also added: the ticker-alias rule and the bulk-endpoint prohibition.
  corrected: listed-name count. The 1.1.0 report claimed "28 → 46"; the audited figures
         are 45 (at 1.0.0) → 57 (at 1.1.0). Both prior numbers were estimates, not
         counts — a P4 violation now repaired. Extension count by tier, audited:
         T1 +2, T2 +4, T3 +6, T4 +0, adjacents +2.
  removed: the phantom P-identifiers P1/P5/P7/P8/P9 as standalone principles; their
           substance is preserved under the register as named facets of existing
           sections.
  deferred: (a) IG/HY credit-spread level — still no source captured; must be populated
            before the first trade idea; (b) ERP and terminal-growth values remain
            provisional model inputs, not sourced market prints; (c) private-company
            valuations are press-reported and unaudited — CLAIMED under P4, never
            DEMONSTRATED; (d) thirteen universe names remain NOT_READY and cannot host
            a thesis until coverage is acquired.
  Re-examination scope: none — no theses are pinned yet, so no re-examination is
  dispatched. Were any thesis in flight, the affected scope would be the Universe
  Definition and the P6 proxy rule.
-->

# Investment Constitution — Agentii Space & Orbital Economy (SPCX Core)

**CONSTITUTION_VERSION**: 1.6.0
**constitution_pin**: 1.5.0
**RATIFICATION_DATE**: 2026-09-18
**LAST_AMENDED_DATE**: 2026-09-18

> Thesis creation is refused while `constitution_pin: unratified` (spec 046 Q83).
> This document is ratified: every placeholder carries a real value. Any change to a
> principle below is a SemVer event — see the rules at the foot of this file.

---

## 0. Scope and Axioms

This workspace researches the **space launch, orbital infrastructure, and orbital
application economy**, anchored on **SpaceX (SPCX, Nasdaq, CIK 0001181412)** as the
core entity. The founding axioms are:

1. **A1 — Launch cost is the master variable.** *Split into A1a/A1b at v1.3.0 — the
   two halves no longer hold together, and the amendment records which one does.*
   - **A1a — Launch cost is the master COST variable.** Every orbital business case
     is a derivative of cost-per-kilogram-to-orbit. When $/kg falls, new businesses
     become viable; when it stalls, the entire application layer stalls with it.
     **HOLDS.** This is the half that sets the floor under every downstream case and
     it is not in question: no application-layer business becomes viable by
     re-pricing launch upward.
   - **A1b — Launch is the master VALUE variable.** The corollary that an operator's
     return tracks its launch business, so a falling $/kg accrues to the launcher.
     **FALSIFIED — and now on the issuer's OWN chosen metrics, which is the strongest
     available form of the evidence.** SPCX's Q2 2026 10-Q reports its own throughput
     indicators *falling*: **mass to orbit −25.6%** (485 t vs 652 t), **Falcon launches
     −17.8%** (37 vs 45), **internal Starlink launches −25.0%** (27 vs 36), **Starship
     launches 3 → 1** across H1 — while the company itself calls mass to orbit *"a key
     indicator of SpaceX's capacity and scalability."* **Consolidated revenue rose 53.7%
     in the same period.** The Space segment is **12.3% of revenue and fell 1.9% across
     H1 2026**; Connectivity is **54.9%** and AI **32.8%**. Corroborated independently:
     RKLB revenue **+62%** with launch revenue **−$2.1M**; FLY revenue **+657%** from
     Spacecraft Solutions. **In all three cases growth comes from non-launch business,
     and in two of three launch revenue declined.** Value is migrating from transport to
     constellations and services — the mechanism behind A5's merger wave, not a
     separate puzzle.
   - **⚠️ A qualification that MUST travel with A1b wherever it is cited.** SPCX's Space
     segment carries a **65.8% gross margin — the highest in the universe** — with cost
     of revenue **flat while revenue rose 29%**. **The marginal Falcon launch is highly
     profitable.** The segment loss is **Starship development R&D ($1,076M/quarter,
     111.9% of segment revenue)** — a reinvestment choice, not an operating failure.
     **State the distinction explicitly: Falcon launch economics are good; one rocket is
     being funded.** A thesis citing A1b to argue *"launch is a bad business"* has
     misread the finding and is `UNFRAMED_REFERENCE`. A1b says value **accrues elsewhere**,
     not that launch **fails to earn**.
   - **Consequence for theses.** A thesis may treat A1a as settled and needs no
     pillar to prove it. A thesis that assumes A1b — that value accrues to the
     launcher as $/kg falls — must test it explicitly and is `UNFRAMED_REFERENCE`
     if it does not. The two halves are separately falsifiable and must be cited by
     their own identifiers, and A1b never travels without its qualification.
2. **A2 — Orbital businesses are physics-bounded before they are market-bounded.**
   Power, thermal rejection, mass, and radiation set hard ceilings that no business
   model can exceed. Feasibility is settled by these bounds, not by narrative.
3. **A3 — Reusability changes the cost curve but not the physics.** Flyback and
   refurbishment reduce hardware amortization; they do not reduce propellant mass,
   radiative area, or solar-array area. Claims that violate a physical floor are false
   regardless of engineering progress.
4. **A4 — Terrestrial AI compute and orbital compute are different businesses.**
   They must never be valued as one. As of ratification, SPCX's AI segment is
   ground-based (1.4 GW nameplate compute draw, Q2 2026); no listed issuer reports
   orbital compute revenue. SPCX has separately sought approval for a constellation of
   up to 1 million satellites delivering **100 kW of compute per tonne** — a filed
   aspiration, not a revenue line, and inadmissible as a valuation input.
5. **A5 — The sector is consolidating while it is still being defined.** Two
   multi-billion-dollar mergers were in flight at ratification: Rocket Lab acquiring
   Iridium (~$8B, announced 2026-06-29, close expected mid-2027) and Amazon acquiring
   Globalstar (~$11.57B, announced 2026-04-14, close expected 2027). Several Tier 1–2
   tickers are therefore *deal securities* whose price tracks a spread, not a
   standalone business. Treat them under P11, never as ordinary exposure.

---

## 0b. Principle Register

**Read this before citing any P-number.** Every identifier below resolves to the
section that actually defines it. An identifier with no defining section is not a
principle and must not appear in a Sync Impact Report, a re-examination scope, or a
thesis pillar reference.

| ID | Principle | Defined in | Kind |
|---|---|---|---|
| A1 | Launch cost is the master variable — *superseded at v1.3.0 by A1a/A1b; retained as the parent identifier* | §0 Axioms | axiom |
| A1a | Launch cost is the master **COST** variable — **HOLDS** | §0 Axioms | axiom |
| A1b | Launch is the master **VALUE** variable — **does not hold on current disclosure** | §0 Axioms | axiom |
| A2 | Orbital businesses are physics-bounded before they are market-bounded | §0 Axioms | axiom |
| A3 | Reusability changes the cost curve but not the physics | §0 Axioms | axiom |
| A4 | Terrestrial and orbital compute are different businesses | §0 Axioms | axiom |
| A5 | The sector is consolidating while it is still being defined | §0 Axioms | axiom |
| P1 | Core-Entity Anchor (SPCX is the workspace's anchor entity) | §0 Scope | **facet** |
| P2 | First-Principles Feasibility Gate | §First-Principles Feasibility Gate | section |
| P3 | Binding-Constraint Naming | §Binding-Constraint Naming | section |
| P4 | Evidence and Anti-Drift Rules | §Evidence and Anti-Drift Rules | section |
| P5 | Listed-Universe Primacy (listed issuers are the unit of analysis) | §Research Scope Constraints + §P6 | **facet** |
| P6 | Private-Company Coverage Rule | §Private-Company Coverage Rule | section |
| P7 | Launch-Cost Floor Discipline | §F5a / §F5b | **facet** |
| P8 | Sub-Sector Cap | §Risk Framework | **facet** |
| P9 | Catalyst Datability | §Methodology Foundation | **facet** |
| P10 | Orbital-Compute Underwriting Rule | §Orbital-Compute Underwriting Rule | section |
| P11 | In-Flight M&A Treatment | §In-Flight M&A Treatment | section |
| F5a | Fully reusable launch-cost floor (propellant, hard) | §F5a | bound |
| F5b | Partially reusable launch-cost floor (upper stage, soft) | §F5b | bound |
| F5c | Fully expendable launch-cost floor (whole-vehicle manufacturing, and the only architecture with a `DEMONSTRATED` price) | §F5c | bound |
| DA-23 | Sign stripping on negative `operating_income`; also any level failing the gross-profit bound | §Data-Integrity Register | **defect** |
| DA-24 | **Non-operating contamination** of `operating_income` — a GAIN *or* a CHARGE (the defining SATS instance is an inverted impairment, not a sale; independence proof withdrawn) | §Data-Integrity Register | **defect** |
| DA-25 | Normalised per-unit metrics | §Data-Integrity Register | **defect** |
| DA-26 | Annual figures mislabelled as quarterly in the metrics block — **20 tested, 19 exhibiting; FLY is the falsifying counterexample (corrected v1.6.0, was "universal, 19 of 19")** | §Data-Integrity Register | **defect** |
| DA-27 | Fiscal-period labels derived from the calendar quarter, not the issuer's fiscal calendar — **n = 4 of 4** | §Data-Integrity Register | **defect** |
| DA-28 | Capital-structure discontinuity around an IPO invalidates share-count detectors | §Data-Integrity Register | **defect** |
| DA-29 | **Back-solved and opaque checks** — a reconciliation that closes is not thereby a check; `computed` is an opaque assertion, not a derivation | §Data-Integrity Register | **defective CHECK** (not defective data) |
| DA-30 | **Two bases on one concept, collapsed without a basis field** — prior to `no_single_basis_collapse` | §Data-Integrity Register | **platform collapse** |

**DA-01 … DA-22** remain defined in `001-technology-baseline/spec.md` §1c and are
inherited workspace-wide by reference; they are **definitional ambiguities**, not
defects. The DA-23/24/25 block above is a different class and lives here because it
binds every artifact in every thesis, not one spec.

**Superseded identifiers.** A1 and F5 remain valid identifiers — they now name the
*parent* claim rather than the operative bound, and an artifact may cite them only
alongside the relevant child (A1a/A1b, F5a/F5b). Citing A1 or F5 as though it settled
the question is an `UNFRAMED_REFERENCE` error: the split exists precisely because the
parent statement is ambiguous between its two halves.

**Facets vs sections.** A *section* is a standalone normative block with its own
heading. A *facet* is a named obligation that lives inside another block and has no
heading of its own — it is binding, but it is cited by its home section, not as a
free-standing rule. The 1.0.0 Sync Impact Report declared P1, P5, P7, P8 and P9 as
added principles without ever giving them a definition; the register retires that
ambiguity by mapping each to the substance it always referred to.

**Rule.** A Sync Impact Report may only name an identifier that appears in this
register. Adding a row is a SemVer event; citing a row that does not exist is a
`UNFRAMED_REFERENCE` error under the taxonomy.

---

## Macro Regime (updated monthly)

- **Regime**: EXPANSION — late cycle, with inflation re-accelerating
- **Portfolio Bias**: NEUTRAL
- **Key Leading Indicators**:
  - ISM Manufacturing PMI 54.6 (Aug 2026, 8th consecutive month above 50)
  - ISM Services PMI 55.4 (Aug 2026)
  - Yield Curve 2s10s: +40 bps (positive — normalized from the 2022–24 inversion)
  - 10Y UST 4.80% / 30Y 5.26% / 2Y 4.37% — at the highest long-end levels since 2023
  - ISM prices-paid 71.1 — elevated; WTI ~$90
  - Credit Spreads: **NOT YET SOURCED** (see deferred item a)

**Bias rationale.** The long-duration profile of this universe is the dominant
macro sensitivity, and the rate backdrop is hostile to it: the long end is at
three-year highs and the market has priced *hike* risk, not cuts. A NET_LONG bias
would be a bet on duration, not on space. NEUTRAL is therefore the honest posture —
we hold the theme at benchmark weight and express conviction through **catalyst-dated,
near-term-revenue names** rather than pre-revenue duration. Re-rate this section
immediately if the 10Y breaks 5.25% (deepen caution) or the Fed pivots to cuts
(permit NET_LONG).

---

## Sector Preferences

Sub-sector is the primary unit — "space" as one sector is too coarse to size risk.

| Sub-sector | Bias | Conviction | Rationale |
|--------|------|:---:|------|
| Launch Services & Reusable Transport | Overweight | High | **Restated at v1.4.0.** Launch is a good *business* even though it is **not the sector's value pool**. SPCX's Space segment runs a **65.8% gross margin — the highest in the universe** — with cost of revenue flat while revenue rose 29%, so **the marginal Falcon launch is highly profitable**; RKLB holds the **only demonstrated per-launch economics in the universe** (basis B $14,667/kg) and owns SolAero, half of the space-solar-cell duopoly. **This rating rests on A1a (launch cost is the master *cost* variable) and on unit economics — NOT on A1b, which is falsified.** Launch is 12.3% of the anchor's revenue and fell 1.9% across H1 2026 while consolidated revenue rose 53.7%. **Overweight as a cost-curve and picks-and-shovels position; a thesis citing this row as evidence that value accrues to launchers is `UNFRAMED_REFERENCE`.** |
| Satellite Connectivity & Direct-to-Cell | Overweight | High | The only space sub-sector with demonstrated operating leverage: SPCX Connectivity earned $1,656M operating income on $4,291M revenue in Q2 2026 (+79.4% YoY), with ARPU declining as volume scales. **This is the one OW/High rating that survives A1b's falsification unamended** — and it is where the value went. **Note: two of the five listed names (IRDM, GSAT) are in-flight deal securities — see P11.** |
| Space Power & Thermal | Overweight | Medium | The binding engineering-constraint layer. Benefits from any orbital build-out **regardless of which operator wins** — the purest picks-and-shovels exposure to A2. **This rationale is the general case of `PROGRAM.md` §0b's main line: the sector pays for indifference to outcome. It was correct here first, and v1.4.0 generalizes it rather than revising it.** |
| Space Infrastructure & Components | Neutral | Medium | **Restated at v1.4.0 — the rationale is inverted, the rating is not.** This is **where the margin ladder's top rungs sit**: HEI **25.5%**, KRMN **19.1%**, roughly **2× the primes they supply**, and the only tier offering both growth and margin (KRMN, TER). The refined rule: **component concentration predicts margin when the supplier's revenue spreads across programmes** — the discriminator is **single-programme dependence**, not buyer concentration, so the former "program-concentration risk" framing was **backwards**. **Held at Neutral/Medium rather than raised because the layer is not space-pure**: HEI runs **2.6% R&D** and its space exposure is incidental. Own it for margin quality with the dilution stated, not implied. |
| Space Compute & Orbital Data Centers | Neutral | Low | Large thematic optionality, zero reported revenue from any listed issuer. Do not underwrite until a named operator discloses orbital compute revenue or a signed offtake. **Strengthened at v1.3.0: the disconfirmation is now positive, not merely an absence** — the one actor with cheap orbital access (SPCX) deployed **1.4 GW on the ground**, naming data centers before launch facilities in its own capex narrative. Orbital compute is not out-built; it is out-*chosen*. **Registered false-positive trap: SPCX's *"AI computational infrastructure"* segment is terrestrial compute with satellite-delivered distribution and must not be read as orbital compute.** |
| Microgravity Processing & Space Biopharma | Neutral | Low | The physics is real and demonstrated; the economics are unproven and pre-revenue. No listed pure-play exists — Varda is private. **Reinforced at v1.3.0**: this is the workspace's clearest `UNRESOLVABLE-FROM-PUBLIC-SOURCES` case — value-per-kg and cost-per-kg returned **do not exist publicly at all**, a stronger condition than a disclosure merely being unreachable. **The demand asymmetry is nonetheless real: three pharma buyers turn over $39,634M/quarter against a ~$2,170M/yr pure-play cohort — 73×.** |
| Diversified Primes & Defense-Space | Neutral | Medium | Space is a minority of revenue at BA/LMT/NOC/LHX/RTX. Use for low-beta space exposure and supply-chain read-through, never as a space thesis in itself. **The margin ladder now prices this tier: LMT 12.4%, RTX 11.4%, LHX 11.1%, NOC 10.1% — mid-ladder, below the component suppliers and above the operators. Only LMT reports Space as a named segment; ULA is equity-method and invisible at both parents, so the disclosure granularity needed to isolate space exposure does not exist at any prime (DA-21).** |
| Earth Observation & Geospatial | Underweight | Low | **Restated at v1.4.0 — the rating is retained, the reason is different.** The former rationale, *"persistent negative unit economics,"* is **refuted**: PL earns **the best gross margin in the universe (53.5%)**. PL loses money to **fixed-cost absorption** — opex is **90.6%** of revenue, so break-even needs **1.69× current revenue** — which A2's discipline distinguishes sharply from a cost problem: *"a cost problem yields to engineering, a volume problem yields only to order flow."* **The Underweight therefore rests on government-concentrated demand and commoditized imagery, and it is a *timing* judgment, not a structural one. Re-rate on evidence of an order-flow inflection, not on margin.** |

---

## Research Scope Constraints

- **Market Cap**: $250M minimum, no maximum (SPCX anchors the top at ~$1.62T)
- **Liquidity Floor**: 20-day average daily dollar volume ≥ $5M for any position —
  a market-cap screen alone admits untradeable microcaps
- **Regions**: US-listed primary common stock and ADRs; non-US-domiciled issuers
  permitted only via ADR with ≤ 1% position cap
- **Sectors Out of Scope**: terrestrial defense procurement not tied to a space
  program; China- and Russia-domiciled space entities (data access and geopolitical
  risk); digital-asset and crypto-adjacent vehicles; SPAC shells with no defined
  space operating business
- **Max Concurrent Positions**: 12

---

## Universe Definition

The universe is tiered by **one axis: function in the value chain.** Tier 0 is the anchor;
the number of positions drawn from each tier is capped by the risk framework below.

**The membership test, stated so a new name does not need judgement.** For each tier, ask:
*does the issuer's **primary revenue** come from this function?* Membership is settled by
revenue composition, not by market cap, index membership, or thematic resemblance.

**Where a name spans functions, the tier is set by primary revenue and every other function
is carried as a DECLARED CROSS-TIER DEPENDENCY — never absorbed as a pillar of the host
thesis.** This rule exists because its absence was measured: thesis 005 (Tier 1) had grown
three pillars belonging to other tiers — a supply-chain duopoly, a single-deal merger model,
and a financing screen — until only one of its six pillars was about its own cohort. A
cross-tier question belongs to the thesis that owns that tier, and the host thesis cites it.

> ⚠️ **RE-CUT at v1.6.0.** The previous framing claimed to tier by *"role in the value
> chain, not by market cap"* while doing neither consistently: **Tier 1 spanned at least
> nine distinct value-chain roles** (launch, lunar, Earth observation, components, stations,
> satellite manufacturing, RF/SIGINT, space data, suborbital tourism) and was in fact a
> **size cohort**; **Tier 4 spanned at least five unrelated industries** (data-centre
> thermal, GPU silicon, hyperscale cloud, batteries, telecom) and was in fact a **theme**.
> A taxonomy that mixes axes cannot tell you whether a new name belongs in a thesis, which
> is the failure the membership test above is written to prevent.
>
> **Two membership moves follow**, and both are consequences of the test rather than
> judgement calls: **PL, BKSY, HAWK and SPIR move Tier 1 → Tier 2** (operating a
> constellation is not manufacturing one), and **VRT leaves Tier 4's membership** for a
> named comparator role (a thesis cannot hold its subject and its control; thesis 009's own
> §3 called the hyperscalers *"the alternative the orbital case must beat"* while listing
> them as members).
>
> **WHEN THE TEST IS EVALUATED — added at v1.6.0 because the test alone is not decidable
> across time.** A membership test that is applied once and never revisited goes stale the
> moment a name changes function, and **M&A moves names across tiers by design** — a launch
> company that acquires a constellation becomes a constellation operator. Accordingly:
>
> 1. **Membership is evaluated as of the thesis's `as_of` date**, and the evaluation is
>    recorded in the thesis's §2 — not left implicit in the tier table.
> 2. **A name whose primary revenue changes function re-tiers at the NEXT constitution
>    amendment**, not mid-thesis. **Work already produced is grandfathered at the pin it
>    records** (Q56 — the filesystem is the checkpoint), so a re-tier never discards
>    verified work.
> 3. **Where a pending transaction would move a name, the thesis states the
>    empty-result disposition in advance** — the measured instance: thesis 005's own
>    membership test says **RKLB leaves Tier 1 if the Iridium acquisition closes**, taking
>    the cohort's only build-versus-launch discloser with it. That is a `no_listed_expression`
>    outcome for the tier, not a `no_thesis` outcome for the question, and it is recorded
>    rather than discovered.

### Agent-Coverage Audit

**Audited 2026-09-18 by per-ticker query against all seven agentii source types.**
Fifty-nine named securities; thirty-seven are agent-ready today.

| Class | Definition | Agent-ready | Count |
|---|---|---|---|
| **READY** | Sector + industry + cohort assigned, `sec_filings` > 0, `xbrl_facts` > 0, `src_documents` > 0. Fully usable without manual setup. | Yes | 37 |
| **PARTIAL** | **`sector` is `null` — nothing more.** These names carry rich XBRL facts, source documents and transcripts; the sector must be supplied by hand before any sector-aggregate constraint can evaluate. | Yes, with manual sector | 9 |
| **NOT_READY** | `xbrl_facts` = 0 and `src_documents` = 0. Nothing but an institutional-holdings stub dated 2025-12-31. | No | 13 |

*Classification is by research readiness, not raw row count: institutional holdings
and insider trades are supplementary, so a name missing only those (e.g. HAWK, which
is otherwise fully cohort-assigned) still counts as READY.*

> ⚠️ **CORRECTED at v1.6.0 — the `PARTIAL` definition previously required `sec_filings == 0`
> as a second condition, and that was a bookkeeping artifact dressed as a data gap.** The
> bulk `list_coverage` endpoint does not report `sec_filings` for every covered ticker — the
> document's own caveat, four paragraphs below, says so: *"Tickers absent from it are not
> thereby uncovered."* Measured on names this table had deferred: **LLY 75,248 XBRL facts /
> 81 documents / 19 transcripts; AMZN 22,062 / 86 / 19; AAPL 16,450 / 77 / 19; BKSY 17,568 /
> 79 / 19** — all `completion_pct: 86`. **They were researchable throughout.** The lesson is
> the register's own: a field that is *absent* is not a field that is *false*, and a
> readiness class must not be defined by a counter the platform does not guarantee.

**Two methodology caveats — both cost real analysis time before they were found:**

1. **Ticker aliasing is live.** `GOOGL` returns an empty record while **`GOOG`** is
   fully covered (146 filings, 65,003 XBRL facts, cohort `mvp_2026q2`). The platform
   keys on the primary listed symbol. Before concluding a name is uncovered, test the
   alternate share class.
2. **The bulk `list_coverage` endpoint is not the source of truth.** It returns only
   `sec_filings` and `xbrl_filings` rows across 729 of the registry's 1,146 tickers.
   Tickers absent from it are *not* thereby uncovered — `AMZN`, `AAPL` and `LLY` are
   all absent from the bulk output yet carry 16,000–75,000 XBRL facts. Only
   per-ticker `get_ticker_coverage` is authoritative.

**Coverage rule.** A `NOT_READY` ticker **cannot host a thesis** — without filings,
documents or facts it cannot satisfy the Evidence and Anti-Drift Rules and will fail
the gate. `PARTIAL` names are researchable but their sector must be assigned manually
before any aggregate constraint evaluates. `COHORTED` names need no preparation.

**Deal column** marks securities whose price is governed by an announced but unclosed
transaction rather than by standalone fundamentals. `DEAL` names are subject to P11.

### Tier 0 — Core Anchor
| Ticker | Company | Role | Coverage |
|---|---|---|---|
| SPCX | SpaceX (Space Exploration Technologies Corp.) | Launch, Starlink connectivity, AI compute. Reports three segments as of Q2 2026: Space, Connectivity, AI. | READY — 8 filings, 1,517 XBRL facts |

### Tier 1 — Launch, Spacecraft & In-Space Services

*Membership test: primary revenue from building or flying launch vehicles, spacecraft, landers
or in-space infrastructure. Operating a constellation is the next tier's function, not this
one — which is why PL, BKSY, HAWK and SPIR now sit in Tier 2.*
| Ticker | Company | Role | Coverage | Deal |
|---|---|---|---|---|
| RKLB | Rocket Lab | Launch (Electron/Neutron) + space systems; owns SolAero, a space-solar-cell supplier. **Acquiring Iridium ~$8B** to become a vertically integrated launch-plus-constellation operator | READY — 83 filings | DEAL (as acquirer) |
| FLY | Firefly Aerospace | Launch and lunar/spacecraft systems | READY — 19 filings | — |
| LUNR | Intuitive Machines | Lunar landers and space services | READY — 69 filings | — |
| KRMN | Karman Holdings | Missile/space and defense component supplier | READY — 30 filings | — |
| VOYG | Voyager Technologies | Space station (Starlab), defense and space systems; **acquired Astrobotic for ~$300M** | READY — 18 filings | — |
| YSS | York Space Systems | Satellite manufacturing and space systems; IPO'd Jan 2026 above $4B; **acquired All.Space for ~$355M** | READY — 10 filings | — |
| RDW | Redwire | Space infrastructure, deployable structures, in-space biotech payloads | **NOT_READY** — no data | — |
| SPCE | Virgin Galactic | Suborbital human spaceflight | **NOT_READY** — no data | — |

> Astroscale (TYO: 186A, space debris removal) is a listed pure-play but is **not**
> platform-covered and trades in Tokyo — out of scope until an ADR exists.

### Tier 2 — Constellation Operators: Connectivity, Spectrum & Geospatial

*Membership test: primary revenue from OPERATING a constellation — a licensed spectrum
position, a subscriber base, or a data product delivered from orbit. The geospatial
operators (PL, BKSY, HAWK, SPIR) were moved here at v1.6.0: they share the licensed-orbit
and data-product structure this tier's valuation question tests, and they do not manufacture
anything, which is what the previous tier was for.*
| Ticker | Company | Role | Coverage | Deal |
|---|---|---|---|---|
| IRDM | Iridium Communications | LEO voice/data constellation. 66 satellites, licensed L-band spectrum, 2.5M subscribers, $871.7M revenue and $114.4M net income (2025) | READY — 77 filings | **DEAL — being acquired by RKLB at $54/sh** |
| GSAT | Globalstar | LEO spectrum and satellite services; powers Apple Emergency SOS; Apple holds ~20% equity and rights to 85% of network capacity | READY — 65 filings | **DEAL — being acquired by AMZN at $90/sh** |
| SATS | EchoStar | Spectrum holder; ~$19.6B AWS-4/H-Block/AWS-3 spectrum sale to SPCX (FCC-approved, transfer closed) | READY — 62 filings | — |
| ASTS | AST SpaceMobile | Direct-to-cell satellite broadband | **PARTIAL** — sector unassigned | — |
| VSAT | Viasat | GEO/LEO broadband and government satcom | **PARTIAL** — sector unassigned | — |
| PL | Planet Labs | Earth observation constellation and data product | READY — 62 filings | — |
| HAWK | HawkEye 360 | RF geolocation and space-based signals intelligence | READY — 4 filings (no institutional-holdings row) | — |
| BKSY | BlackSky | Earth observation and analytics | READY — **17,568 XBRL facts, 79 source documents, 19 transcripts**, 86% complete; only `sector` is unassigned. Reclassified from `PARTIAL` at v1.6.0 | — |
| SPIR | Spire Global | Space-based data (weather, maritime, aviation) | **NOT_READY** — no data | — |
| MDA | MDA Space | Canadian space robotics (Canadarm heritage), satellite subsystems | **NOT_READY** — no data | — |
| TSAT | Telesat | GEO/LEO operator; Lightspeed LEO constellation | **NOT_READY** — no data | — |
| GILT | Gilat Satellite Networks | Ground segment and satellite networking | **NOT_READY** — no data | — |
| SGBAF | SES S.A. | Luxembourg GEO/MEO fleet operator (OTC ADR) | **NOT_READY** — no data | — |

> **Europe/Japan listed but not platform-covered:** Eutelsat (ETL.PA), Avio (AVIO.MI),
> SKY Perfect JSAT (9412.T). Read-through only until coverage is acquired.

### Tier 3 — Primes and Supply Chain

> Tiers 3–5 are now individually verified (see the Agent-Coverage Audit above). Note
> that the platform's sector taxonomy files several of these outside aerospace —
> `BWXT` under `industrial.nuclear_energy`, `TER` under `tech.semiconductors`, `VRT`
> under `industrial.machinery`. **A sector screen on `aerospace_defense` will not
> surface them**, which is a screening hazard worth remembering.

| Ticker | Company | Space Exposure | Coverage |
|---|---|---|---|
| BA | Boeing | Spectrolab space solar cells; SLS, Starliner, satellite systems | READY — 76 filings |
| LMT | Lockheed Martin | Space segment; ULA joint venture | READY — 70 filings |
| NOC | Northrop Grumman | Space systems, solid rocket motors, Cygnus | READY — 63 filings |
| LHX | L3Harris | Aerojet Rocketdyne propulsion, space payloads | READY — 89 filings |
| RTX | RTX | Space sensors and electronics (Collins, Raytheon) | READY — 66 filings |
| HWM | Howmet Aerospace | Engine and structural castings, fasteners | READY — 84 filings |
| TDG | TransDigm | Aerospace and defense components | READY — 112 filings |
| HEI | Heico | Replacement parts and electronic components | READY — 60 filings |
| WWD | Woodward | Control systems for propulsion | READY — 75 filings |
| CW | Curtiss-Wright | Actuation and defense electronics | READY — 60 filings |
| KTOS | Kratos Defense | Space/satellite command-and-control, ground systems | READY — 56 filings |
| MRCY | Mercury Systems | Radiation-tolerant processing electronics | READY — 56 filings |
| BWXT | BWX Technologies | **Nuclear power and thermal propulsion for space** — the only credible path to raising radiator temperature and shrinking F2's area penalty | READY — 57 filings (sector: nuclear_energy) |
| AVAV | AeroVironment | Defense autonomy and space/stratospheric systems | READY — 87 filings |
| TER | Teradyne | Robotics and semiconductor test; space-adjacent automation | READY — 62 filings (sector: semiconductors) |
| MOG-A | Moog | Space and defense motion control, satellite components | **NOT_READY** — no data |
| TDY | Teledyne | Space imaging and IR detectors | **NOT_READY** — no data |
| ATRO | Astronics | Power distribution and lighting for aerospace | **NOT_READY** — no data |
| TRMB | Trimble | Positioning and geospatial infrastructure — downstream consumer of GNSS | **PARTIAL** — sector unassigned |
| GRMN | Garmin | GNSS device demand; satellite messaging integration | **PARTIAL** — sector unassigned |
| PLTR | Palantir | Defense and space data fusion; downstream analytics layer | **PARTIAL** — sector unassigned |

> **Advanced air mobility (adjacent, not orbital):** JOBY (Joby Aviation) and ACHR
> (Archer Aviation) appear in space thematic funds but operate in the atmosphere. They
> are admissible only as a read-through on electric propulsion and FAA certification
> timelines, never as space exposure. Both are READY (87 and 86 filings) and both are
> filed under `industrial.aerospace_defense`.

### Tier 4 — Enabling Layer (Power, Thermal, Compute)

*Membership test: primary revenue from SELLING power, thermal management or compute capacity,
where the orbital case is a stated demand path. The layer where A2's constraints bind, and
where the orbital-compute question lives or dies under P10.*

> ⚠️ **VRT MOVED OUT OF MEMBERSHIP at v1.6.0.** Vertiv is the **terrestrial comparator** — the
> thing orbital compute must beat — and a thesis cannot hold its subject and its control.
> Thesis 009's own §3 said so while listing it as a member: *"the **alternative** the orbital
> case must beat."* VRT is retained as a **named comparator**, cited for the cooling penalty
> and the terrestrial cost floor, and is **not a universe member of any Tier 4 thesis**. The
> same rule applies to any name whose role is to bound the thesis rather than to be subject
> to it.

| Ticker | Company | Relevance to A2 | Coverage |
|---|---|---|---|
| NVDA | NVIDIA | Compute silicon. An H100 already flew on Starcloud-1; radiation tolerance and thermal coupling determine viability of orbital inference | READY — 169 filings, cohort mvp_2026q2 |
| **GOOG** | Alphabet | **Project Suncatcher** — TPU-based orbital data centers, two prototypes targeted by early 2027, 81-satellite reference configuration. The most detailed public engineering disclosure in the sector | READY — 146 filings, cohort mvp_2026q2. **Query as `GOOG`, not `GOOGL`** — the latter returns an empty record |
| MSFT | Microsoft | Azure Space; cloud-side demand for orbital data | READY — 52 filings, cohort mvp_2026q2 |
| AMZN | Amazon | **Amazon Leo** (~180–200 satellites, target 3,200 by 2029, ~$17B capex committed). Acquiring Globalstar for D2D spectrum; Blue Origin founder affiliation | **PARTIAL** — sector unassigned |
| AAPL | Apple | ~20% of Globalstar plus rights to 85% of its network capacity; D2D anchor demand | **PARTIAL** — sector unassigned |
| AMPX | Amprius Technologies | High-specific-energy silicon-anode cells; space and HAPS flight heritage | **NOT_READY** — no data |
| ENS | EnerSys | Battery systems including space-qualified cells | **NOT_READY** — no data |
| TMUS | T-Mobile US | Starlink direct-to-cell commercial partner | **NOT_READY** — no data |

**Orbital-compute reference points (all CLAIMED, none DEMONSTRATED).** Reported cost
of orbital compute infrastructure is **$10,000–40,000 per kW** against a terrestrial
build far below that; NASA-sourced analysis puts large-scale viability at a launch
price of **$100–200/kg**, versus Falcon 9 at $2,600–3,400/kg and the F5a propellant
floor of ~$46–92/kg. The gap between those numbers *is* the orbital-compute thesis.
Note the ordering the split exposes: the **$100–200/kg viability threshold sits *above*
the F5a floor**, so the orbital-compute case is not physically foreclosed — it requires
roughly a 2–4× improvement in a fully reusable vehicle's economics, not a breakthrough.
F5b does not bound this question at all, because no partially reusable vehicle can
reach the threshold on its upper-stage manufacturing curve.
China has launched 12 orbital-compute satellites and targets a 2,800-module
constellation.

### Tier 5 — Microgravity Demand Side (Pharmaceutical)
All five sit in `med.medicines_biotech` — none will surface on an aerospace screen.
| Ticker | Company | Relevance | Coverage |
|---|---|---|---|
| UTHR | United Therapeutics | Named partner of Varda Space Industries for microgravity small-molecule processing (announced May 2026) — the listed proxy for the Varda exposure | READY — 68 filings |
| MRK | Merck | ISS protein-crystallization research history | READY — 52 filings |
| BMY | Bristol Myers Squibb | Microgravity biologics research | READY — 74 filings |
| AMGN | Amgen | Microgravity protein research | READY — 71 filings |
| LLY | Eli Lilly | Microgravity protein/formulation research | **PARTIAL** — sector unassigned |

### Pre-IPO and Venture Roster

The private layer is where the technology is actually being proven, and it is the
leading indicator for the listed layer. **Every figure below is press-reported and
unaudited — grade all of it `CLAIMED` under P4.** Valuations move fast; re-verify
before citing. Coverage is governed by the Private-Company Coverage Rule (P6).

**Sector funding context:** global space- and satellite-company funding reached a
record **~$20.3B in 2026 year-to-date** (US ~$12.7B / >60%; China >20%; Europe ~10%),
against >$12B for all of 2025. The SPCX IPO is the direct catalyst.

**Launch, Reusable Transport, and In-Space Logistics**
| Company | Last round | Valuation | Status / note |
|---|---|---|---|
| Blue Origin | ~$10B raise (2026) | ~$130B | Bezos $2B, Coatue $4B. The largest private space asset; New Glenn + Blue Moon |
| Stoke Space | ~$1B (Aug 2026) | ~$9B | Fully reusable second stage; private bids ~$50/sh, up >260%; no IPO announced |
| Relativity Space | — | — | Terran R medium-lift; long-dated |
| Impulse Space | $500M Series D | — | In-space logistics and orbital transfer |
| K2 Space | $500M Series D (Jul 2026) | — | Large high-power satellite buses |
| Apex | $200M (2026) | ~$2.3B | Satellite buses and reentry vehicles |
| Aetherflux / Cowboy Space | $275M | — | Space-based solar power |
| Aalyria | $100M Series B | — | Laser/optical comms networking |

**Orbital Compute** — the purest exposure to the A4 theme
| Company | Last round | Valuation | Status / note |
|---|---|---|---|
| Starcloud (ex-Lumen Orbit) | $170M Series A (Mar 2026); ~$200M total | ~$1.1B | **Starcloud-1 flew an NVIDIA H100 and ran Gemini plus a nano-GPT training run. The H100 cannot run at full power — insufficient cooling capacity.** That single fact is F2 demonstrated in the field. Starcloud-2 targeted 2027 |

**Connectivity**
| Company | Last round | Valuation | Status / note |
|---|---|---|---|
| Astranis | ~$450M incl. $300M Series E | ~$2.8B | GEO smallsat broadband |
| Yuanxin Satellite / SpaceSail | $1B (Aug 2026) | — | China LEO constellation |

**Earth Observation**
| Company | Last round | Valuation | Status / note |
|---|---|---|---|
| ICEYE | €450M Series F | ~€10B (~$12B) | SAR constellation; the highest-valued private EO firm |
| Capella Space / Umbra / Albedo / Muon Space / Pixxel | various | — | SAR and hyperspectral; consolidating |

**Space Stations and Habitats** — the ISS end-of-life replacement market
| Company | Last round | Valuation | Status / note |
|---|---|---|---|
| Sierra Space | ~$1.7B raised | ~$8B | IPO preparations under way; could list 2026 |
| Vast Space | $500M (Mar 2026) | — | Listing talks for late 2026 / early 2027 |
| Axiom Space | $350M (Feb 2026); ~$1.64B total | ~$2.5B | $2.2B in contracts; targeting an IPO within a year |

**Microgravity Processing and Space Biopharma**
| Company | Last round | Valuation | Status / note |
|---|---|---|---|
| Varda Space Industries | $187M Series C (Jul 2025); ~$329M total | — | Founders Fund, Khosla, Lux, Thiel, Natural Capital. W-6 reentered May 2026 at Koonibba, South Australia; ~50 kg API returned per mission; FAA Part 450 license. **Listed proxy: UTHR.** Pre-revenue on the pharma side — no microgravity-manufactured drug has reached market |

**Defense Technology with Space Exposure**
| Company | Last round | Valuation | Status / note |
|---|---|---|---|
| Anduril | $5B Series H (May 2026) | — | The largest single space-sector recipient in 2026, though it is a diversified defense-tech firm containing space and satellite lines |

**China Commercial Space — read-through only, no thesis permitted**
> Excluded from thesis creation by the Research Scope Constraints (no platform
> coverage, no US listing). Tracked because Chinese cadence and pricing are direct
> competitive inputs to SPCX and RKLB.
> **The "Five Little Dragons"** — LandSpace (蓝箭航天, ~RMB 20B, STAR Market IPO
> accepted), CAS Space (中科宇航), Space Pioneer (天兵科技), Galactic Energy
> (星河动力), iSpace (星际荣耀, RMB 7B Series E at RMB 23.5B pre-money, STAR Market
> IPO targeted H2 2027). Combined valuation passed RMB 100B by Feb 2026, up from
> RMB 67.5B in Jan 2025. Satellite side: MinoSpace (微纳星空), Galaxy Space
> (银河航天), ADA Space (国星宇航, HKEX, self-described "first space AI stock").

**Venture investors to track for signal** (round leadership is the leading indicator
of where the next listed cohort comes from): Founders Fund, Khosla Ventures, Lux
Capital, Coatue, a16z, Sequoia, General Catalyst, DCVC, Space Capital, Seraphim
Space, Playground Global, Natural Capital, Shrug Capital.

---

## First-Principles Feasibility Gate (P2)

**No thesis may advance past specification until it clears this gate.** Each thesis
must state the physical bound that bounds its business case, with units and a source.
Narrative market sizing is inadmissible on its own.

### F1 — Solar power ceiling
- Solar constant at 1 AU: **1,361 W/m²** (AM0)
- Space-qualified multi-junction cell efficiency: **~30–32% BOL** (triple-junction
  IMM, e.g. Spectrolab/SolAero class); **~35%** for quad-junction, at higher cost
- → Usable electrical power: **~410–480 W/m² BOL**, degrading ~1–2%/yr
- LEO eclipse: at ~500 km the eclipse fraction is roughly **35 minutes of a ~94-minute
  orbit (~37%)**. Batteries must carry the full load through eclipse, and Li-ion space
  packs deliver roughly 150–200 Wh/kg at cell level — so eclipse storage is a
  first-order mass driver, not an afterthought.

**Derived ceiling — the multiplier chain matters.** The naive figure (1 MW ÷ 400 W/m²
≈ 2,450 m²) understates the real requirement by more than half. The honest derivation
for 1 MW of *continuous* delivered load is:

| Step | Factor | Area |
|---|---|---|
| Cell-level, BOL, continuous | 1,000,000 ÷ (1,361 × 0.30) | 2,449 m² |
| ÷ eclipse duty cycle (0.63 sunlight fraction) | × 1.587 | 3,886 m² |
| ÷ array packing factor (~0.85 — cells do not tile the full panel) | ÷ 0.85 | 4,572 m² |
| ÷ end-of-life degradation (~0.90 retention over mission life) | ÷ 0.90 | **~5,080 m²** |

This reconciles with the independently published estimate of **~5,640 m² of array per
MW** for an orbital data center. **Use ~5,000–5,600 m²/MW, not 2,450 m²/MW.** A thesis
that sizes its array off the naive figure is wrong by a factor of two.

### F2 — Thermal rejection ceiling (the binding constraint for orbital compute)
In vacuum there is no convection and no conduction sink. All waste heat must be
radiated: **P = ε·σ·A·(T_rad⁴ − T_sink⁴)**, σ = 5.6704×10⁻⁸ W·m⁻²·K⁻⁴.
- At T_rad = 300 K, ε = 0.9 → **~413 W/m² rejected**
- At T_rad = 350 K, ε = 0.9 → **~765 W/m² rejected**
- Since essentially all electrical power in a compute payload becomes heat,
  **radiator area scales 1:1 with compute power**, and at 300 K the radiator is
  roughly the same area as the solar array that powers it.
- **Worked bound — 1 MW orbital data center**: ~2,450 m² array + ~2,420 m² radiator
  ≈ **~4,900 m² of deployed surface**, all of which must be launched, deployed, and
  attitude-controlled.
- **The comparison that matters**: a terrestrial 1 MW IT load rejects the same heat
  through chillers and cooling towers at a small fraction of the mass and area cost,
  drawing on an effectively unbounded atmospheric sink. **Orbital compute is a
  thermal-and-mass problem, not a silicon problem.** Any orbital-compute thesis must
  show its radiator mass and area, or it fails the gate.

### F3 — Microgravity as a processing advantage
Absent buoyancy, there is no natural convection and no sedimentation. This is a
genuine processing advantage for: protein crystal growth (higher-quality crystals →
better structures), ZBLAN fluoride optical fiber (suppresses crystallization),
bioprinting and organoid culture (no settling), and small-molecule polymorph control
(the demonstrated ritonavir Form III result).
- **The economic test**: microgravity is a *quality* advantage, not a *cost* advantage.
  A thesis must show that the value uplift per kilogram exceeds the fully-loaded
  launch + on-orbit processing + reentry-capsule + recovery cost per kilogram.
- Varda Space Industries returns roughly **50 kg of active pharmaceutical ingredient
  per mission**. The bound to interrogate is revenue per kg returned versus cost per
  kg returned — not total addressable market.

### F4 — Radiation environment
Total ionizing dose and single-event-upset rates are functions of altitude,
inclination, shielding mass, and solar cycle. They are **mission-specific and must be
sourced per mission profile**. Any thesis claiming commercial off-the-shelf silicon in
orbit must state its assumed TID tolerance and SEU mitigation (redundancy, triple
modular redundancy, scrub rates) — generic assertions that "rad-hardening is solved"
fail the gate.

### F5 — Launch-cost floor
*Split three ways at v1.3.0.* As originally written this bound applied to every
reusable vehicle. It does not. **The binding term differs by reuse architecture**, and
applying the propellant floor to a partially reusable vehicle is a category error.
Measure which floor applies by asking what is *expended* on each flight. **Three
architectures, three floors — and a thesis must name which one it is using.**

| Architecture | Floor | Character | Demonstrated price? |
|---|---|---|---|
| **F5a** fully reusable | Propellant mass × price | **Hard** — yields only to physics | No — `MODELED` |
| **F5b** partially reusable | Expended upper stage (manufacturing) | Soft — yields to production learning | No — `MODELED` |
| **F5c** fully expendable | Entire vehicle (manufacturing) | Soft — but nothing to amortise against | **Yes — the only one** |

#### F5a — Fully reusable: the propellant floor (hard)
A first-principles floor exists that reusability does **not** remove: propellant mass
is consumed on every flight.
- Starship consumes roughly **4,600 t of propellant** (Super Heavy ~3,400 t + Ship
  ~1,200 t) per flight. Blended cryogenic propellant cost is on the order of
  $1–2/kg delivered to the pad.
- → **Propellant-only floor ≈ $4.6M–9.2M per flight.** At a 100 t payload that is
  **~$46–92/kg**; at 150 t, **~$31–61/kg**.
- **Therefore any claim of sub-$10/kg to LEO is below the propellant floor** and is
  false unless payload per flight rises several-fold. Treat sub-$10/kg as a
  marketing figure, not an input.
- This bound applies **only** where both stages are recovered. On such a vehicle
  propellant is ~100% of marginal cost and the floor is genuinely hard.

#### F5b — Partially reusable: the upper-stage manufacturing floor (soft)
Where only the booster is recovered, propellant is **not** the dominant term and F5a
does not bound the vehicle.
- Falcon 9 consumes roughly **485 t** of RP-1/LOX. At ~$0.75/kg that is
  **~$0.36M per flight**. Against a marginal cost of **~$12–20M**, propellant is
  **~2–3%**.
- The dominant unrecoverable term is the **expended second stage**, at roughly
  **$8–12M**, followed by range and launch operations ($2–5M) and booster
  refurbishment ($1–3M).
- → **The binding floor for a partially reusable vehicle is a *manufacturing* cost
  curve, not a propellant curve.** It is soft: it yields to production learning,
  whereas F5a yields only to physics.
- **Consequence.** A thesis quoting a sub-$10/kg figure is below F5a and false as
  stated. A thesis applying F5a's $46–92/kg floor to a Falcon-class vehicle is
  misapplying the bound and will understate that vehicle's achievable price by an
  order of magnitude. **State which architecture the floor is being applied to.**
- Reference points: Falcon 9 reusable is roughly $2,700–2,900/kg to LEO on customer
  list price. The credible Starship band is a one-order-of-magnitude improvement,
  not two.

#### F5c — Fully expendable: the manufacturing floor (hard, and unpriced)
*Added at v1.3.0, completing the split.* **F5a and F5b between them cover only the two
reusable architectures — which means the vehicles with the *only demonstrated cost data
in the universe* had no applicable floor at all.** Electron and Alpha are fully
expendable: neither vehicle nor booster is recovered, so F5a's propellant floor does not
apply (propellant is again ~2–3% of marginal cost) and F5b's upper-stage term does not
apply either (there is no recovered stage to amortise against).

- **The binding floor is the entire vehicle**, manufactured once and expended once. It
  is a **pure manufacturing cost curve** with no recovery term to divide by, and it is
  therefore the *hardest* of the three floors in the sense that no reuse-learning
  offsets it — while being the *softest* in that it yields to production scale.
- **This is the only architecture with a `DEMONSTRATED` price.** RKLB discloses
  `cost per launch` at **$4.4M (Q2) / $4.9M (H1)** and `revenue per launch` at **$9.1M /
  $9.2M**, giving **basis B = $14,667/kg** and **basis A = $30,333/kg** at 300 kg to LEO
  — **15–30× above the $1,000/kg threshold**.
- **Consequence.** A thesis must state which of the three architectures its floor applies
  to. **The sector's cost conversation is dominated by reusable vehicles (F5a), whose
  floor is `MODELED`; while the only `DEMONSTRATED` price belongs to an expendable
  vehicle (F5c), which F5 as originally written did not bound at all.** That inversion —
  demonstrated data on the unbounded architecture, modelled bounds on the undemonstrated
  one — is itself a finding about the sector's evidence base.

### F6 — Regulatory and spectrum
Orbital slots, spectrum rights, reentry licenses (FAA Part 450), and FCC/ITU
coordination are gating assets, not paperwork. The SPCX–EchoStar AWS-4/H-Block/AWS-3
spectrum transfer (~$19.6B) is the reference transaction for how spectrum is priced.
Any thesis whose value depends on un-granted spectrum or an un-issued license must
carry that as an explicit, dated regulatory catalyst.

---

## Binding-Constraint Naming (P3)

Every thesis must name **exactly one** binding constraint — the thing that, if it
moved, would most change the outcome. Permitted values:

`POWER` · `THERMAL` · `MASS_LAUNCH_COST` · `RADIATION` · `REGULATORY_SPECTRUM` ·
`DEMAND` · `CAPITAL` · `MANUFACTURING_RATE`

A thesis that cannot name its binding constraint is not yet a thesis. A thesis whose
narrative depends on two or more constraints relaxing simultaneously is a
**compound bet** and must be sized as a binary catalyst.

---

## Private-Company Coverage Rule (P6)

Non-listed companies are **not standalone theses** — they have no mark, no filed
financials, and no enforceable disclosure. Varda Space Industries is the canonical
example. A private company may enter the workspace only in one of three roles:

1. **Value-chain node** — as a supplier, customer, or competitor inside a listed
   thesis (e.g. Varda as a customer of launch and reentry services).
2. **Listed proxy** — through a listed entity whose economic exposure can actually be
   sized. Varda's proxy is **UTHR** (named pharma partner). The proxy must be named
   explicitly; if no listed proxy exists, the thesis must say so in those words.
3. **Feasibility comparator** — as evidence about what is physically achievable,
   cited as a technical datapoint rather than a valuation input.

A private company receives its own thesis **only** if it lists or files. Until then it
is documented inside a listed thesis, never as one.

---

## Orbital-Compute Underwriting Rule (P10)

Orbital compute is the highest-optionality and lowest-evidence idea in this universe.
It produced no revenue for any listed issuer at ratification, yet it anchors the
SPCX AI narrative and a dozen private pitch decks. It is therefore gated hardest.

**No orbital-compute thesis may be specified unless it carries all five of:**

1. **Revenue or offtake** — a named operator reporting an orbital-compute revenue
   line, or a signed offtake with a named counterparty. Aspiration is not offtake.
2. **Radiator derivation** — explicit mass and area, computed against F2, at a stated
   rejection temperature. If it assumes a hotter radiator, it must justify the heat
   pump or nuclear source that permits it.
3. **Array derivation** — explicit area against F1's corrected chain
   (**~5,000–5,600 m² per MW**, not the naive ~2,450 m²).
4. **Launch cost** — a $/kg assumption tested against the **F5a** propellant floor,
   and against **F5b** if the vehicle is partially reusable. An assumption below
   ~$46/kg without payload-per-flight justification fails. An assumption below
   ~$46/kg is necessarily an F5a-class (fully reusable) claim: **state which vehicle
   architecture is assumed, because the two floors differ by an order of magnitude.**
5. **Radiation** — a stated TID assumption and SEU mitigation for the chosen orbit.

Absent all five, orbital compute is a **watch item, not a thesis**. Constellation
applications (including SPCX's filing for up to 1 million satellites at 100 kW/tonne)
are `CLAIMED` under P4 and are inadmissible as valuation inputs. The sector's own
evidence supports this caution: Starcloud-1 flew an H100 that **cannot run at full
power because of insufficient cooling**, and reported orbital-compute infrastructure
cost is **$10,000–40,000 per kW** against a terrestrial build far below it.

---

## In-Flight M&A Treatment (P11)

A security subject to an announced but unclosed transaction is a *deal security*, not
an operating business. Both current cases — IRDM (acquired by RKLB) and GSAT (acquired
by AMZN) — sit in Tier 2 and would otherwise be underwritten on fundamentals.

- **Do not underwrite standalone fundamentals.** The price tracks the spread, not the business.
- **The binding constraint is `REGULATORY_SPECTRUM`** — antitrust, CFIUS, and
  national-security review. IRDM carries safety-of-life and defense communications;
  GSAT carries globally harmonized L-band spectrum and an Apple capacity agreement.
  Neither clears trivially.
- **Size under the binary catalyst cap (2%)**, per the Risk Framework.
- **If the acquirer is the thesis**, model the combined entity including deal
  financing and dilution — e.g. RKLB's $3.6B bridge facility and stock consideration —
  and treat the close date as the dated catalyst.
- **On a break, re-underwrite from scratch.** The standalone case is not the
  pre-announcement case: a failed deal leaves both the target and the acquirer
  re-rated, and the acquirer carrying deal costs.

---

## Evidence and Anti-Drift Rules (P4)

1. **Evidence grading.** Every material claim is tagged `DEMONSTRATED` (flown,
   reported, or filed), `CLAIMED` (company or press assertion), or `MODELED` (our own
   derivation). Physical constants and filed financials are DEMONSTRATED; roadmaps and
   target cost curves are CLAIMED until flown.
2. **No unaudited numbers.** Figures come from SEC filings, the company's own
   transcripts, or a cited external series. A number without a source is an error, not
   an estimate.
3. **First-principles claims are shown, not asserted.** Any physical or economic bound
   restated in a thesis must be re-derived or re-cited with units.
4. **`constitution_pin` and `assumption_pin`.** Every artifact pins the versions it
   was built against. Compiling against a stale pin is a hard failure.
5. **Silent drift is the cardinal sin.** Deviating from a value in `assumptions.yaml`
   without an explicit declared justification invalidates the artifact.

---

## Data-Integrity Register (P4)

**Added at v1.3.0.** P4 governs what a claim *means*. This register governs whether the
number underneath it is **real**. Each entry below is a *measured* extraction defect —
not a convention, not a preference — with a census, a discriminator that decides whether
a given figure is affected, and a remedy. An artifact that reads an affected field
without applying the remedy is `DATA_STALE` under the taxonomy.

**Standing rule for definitional ambiguity.** Where a term admits multiple defensible
readings, artifacts report **all** of them, label which one is quoted, and treat the
spread as a finding. This rule is workspace-wide, not thesis-local; it originated as
§1c of `001-technology-baseline` and is inherited by every subsequent thesis. The
thesis-local register of 22 ambiguity classes (DA-01 … DA-22) remains in that spec and
is inherited by reference.

### DA-23 — SIGN STRIPPING on negative `operating_income`

| | |
|---|---|
| **Census** | **6 of 6 loss-making issuers** return negative operating income as a **positive value of identical magnitude**. **19 of 19 profitable issuers** are unaffected. **Zero exceptions on either side.** |
| **Flipped** | SPCX (−143.0 → +143.0), YSS (−41.3 → +41.3), RKLB (−57.5 → +57.5), FLY (−95.2 → +95.2), **BA (−5,761 → +5,761)**, **PL (−34.888 → +34.888 — the cleanest instance, an exact component match on directly-available quarterly figures)** |
| **Clean — SUBTOTAL-LEVEL ONLY, and the qualifier is load-bearing** | GOOG, IRDM, LHX, HWM, TDG, NOC, LMT, RTX, KRMN, AMGN, BMY, MRK, WWD, HEI. **⚠️ `Clean` here means only that the PARENT series tests clean. At 002 Phase 3 it was established that an issuer can be clean at every subtotal while a COMPONENT of the same statement is sign-corrupted — BWXT, VRT, UTHR and MRCY are all instances. FOUR issuers previously listed in this row have been REMOVED for exactly that reason: MRCY (11 of 13 filed periods stripped; the clean verdict came from testing only the filed-positive period), UTHR (11 of 11 verified negative components stripped while all 35 parent facts are correctly positive), SATS (12/12 filed-negative subtotals stripped, 8/8 filed-positive clean), and — **added at v1.6.0, on thesis 003's finding — GSAT**, whose `OperatingIncomeLoss` is served as **+4,775,000 against a filed (4,775)K loss**; the strip was **verified directly at v1.6.0 by calling both endpoints on one accession** (see the endpoint note below). A subtotal-level census CANNOT support an unqualified `Clean`.** |
| **⚠️ THE STRIP IS ENDPOINT-SPECIFIC — established at v1.6.0, and it is a REMEDY, not a caveat** | On **one filing, one concept, one period** (GSAT accession `0001366868-26-000039`, `us-gaap:OperatingIncomeLoss`, Q2 2026): **`search_xbrl_facts` returns `4775000`; `get_statement` returns `-4775000`**, labelled *"(Loss) income from operations"*. Magnitude agrees exactly; **only the sign differs.** So DA-23 is **not "the platform"** — it is **one extraction endpoint disagreeing with another on the same filed fact**, which means the defect is **localised and fixable at that endpoint**, and that **`get_statement` is the reliable read where the two disagree**. Any artifact quoting `search_xbrl_facts` alone inherits the strip silently. |
| **⚠️ UNEVIDENT — the test could not run** | **NVDA.** The entire income statement has **zero negatives** (`OperatingIncomeLoss` 69 facts, all non-negative 2014–2026), so **the sign test can neither pass nor fail.** *This is not clean; it is unevident* — the DA-23 analogue of the register's own margin-conditioned-power rule. **A test that cannot fail is not a passing test, and 001's "12 issuer-quarters" rule count must be re-scored to *issuer-quarters where DA-23 was TESTABLE*.** |
| **⚠️ UNEXERCISED — the test ran on nothing** | **VRT.** All 61 `OperatingIncomeLoss` facts are positive, so the `\|x\|` channel **had nothing to act on** — 13/13 identities close but vacuously. **`Unexercised` and `Clean` are different results and must not be reported as the same.** |
| **⚠️ CLEAN AT SUBTOTALS, STRIPPED ELSEWHERE ON THE STATEMENT** | **VRT and NVDA** — the stripping sits on CASH-FLOW subtotals (VRT `NetCashProvidedByUsedInFinancingActivities` correct at `+11.9` in one period and stripped at `−3.0` in another; NVDA investing `+26,429,000,000` vs filed `(26,429)`). **The discriminator is the SIGN OF THE VALUE, not the concept and not the period. A census scoped to the income statement cannot see this.** |
| **⚠️ CLEAN AT EVERY SUBTOTAL, STRIPPED AT A COMPONENT — registered at 002 Phase 3, BWXT** | **BWXT is the first issuer where "clean" and "stripped" are simultaneously true, and the census statistic above cannot see the second.** Every subtotal reconciles; the defect is one level down. `GainLossOnSalesOfAssetsAndAssetImpairmentCharges` is served as an **absolute magnitude — 4 of 4 page-verified filed losses stripped to positive, 3 of 3 gains untouched, 0 negatives in the entire 29-fact served series across six fiscal years.** The arithmetic signature is exact: **`diff 250 = 2 × 125`, the mark of a strip** — and `status` marked that row **`pass`**. **Consequence: a census that tests only the parent concepts reports a clean issuer while a component of that same statement is sign-corrupted. Component-level census is a distinct requirement from subtotal-level census.** |
| **Consequence** | **An inversion, not a footnote.** Any `operating_income` ranking places the *worst loss-makers at the top* — SPCX's $143M loss outranks IRDM's $34M profit. Every margin, ratio and screen built on the raw field is wrong for every loss-making issuer in the universe, and **silently so**, because the returned value is internally plausible. |
| **Remedy** | Recompute from components before any use. An artifact quoting a raw `operating_income` must show the component derivation in-line. |

**Three detectors, in descending reliability.** The register previously named one test
and one anti-test. The universe-wide pass surfaced a second detector that is *stronger*
than the first in a specific way, and the ordering now matters.

| # | Detector | Rule | Reliability |
|---|---|---|---|
| **1** | **Component identity** | `gross profit − opex = operating_income` | **Fully reliable where quarterly gross profit exists.** The only test that confirms a *value*, not just a sign. |
| **2** | **Gross-profit bound** | **Operating income can never EXCEED gross profit, at any sign.** Contributed by the universe-wide pass. | **A SCREEN, not a classifier**, and its power scales **inversely with gross margin**: near-useless at high-margin issuers (a **false negative at every level at SPCX**, ~65% GM; **4 of 4 at FLY**, ~20% GM). **⚠️ CORRECTED at 002 Phase 3: the entry originally claimed *"VOYG fails it by $46,951M across three consecutive quarters"* — that was computed by applying the bound to the SIGN-STRIPPED MAGNITUDE, and then treating the violation as mutually exclusive with sign-stripping. VOYG is a PLAIN DA-23 sign strip. Restored, `−51.408 < +4.457` violates nothing. The bound fires on 16 of 17 VOYG periods, continuously since FY2024 — not three.** |
| **3** | **Margin plausibility vs industry norms** | An operating margin far outside the sector's range | **Weakest.** Used only where 1 and 2 are unavailable — at BA 2025 Q3 and LUNR. |
| **—** | ~~`EPS × shares ≈ net income`~~ | — | **INADMISSIBLE as a sign test.** Confirmed unreliable: it **passes on both sides of a flip** at RKLB, FLY *and* VOYG. Its use is a defect, not a shortcut. |

**Three open candidates — recorded, not yet resolved.** BA 2025 Q3 (net-loss bridge
confirmed, margin unverified); LUNR (a 42.1% operating margin is implausible and the
component identity is unavailable — no gross profit line); VOYG (see below).

**A second sub-mechanism at VOYG — unreconcilable LEVEL, not sign.** VOYG does not
invert a sign. It returns `OperatingIncomeLoss` of **$51.408M against gross profit of
$4.457M** — a value that cannot be an operating income at any sign, failing detector 2
outright. **The register's scope therefore extends beyond sign stripping to any
extraction that fails the gross-profit bound**, and an artifact testing only for sign
will pass VOYG and be wrong.

> **⚠️ Coverage hole — a silent-failure class.** `OperatingIncomeLoss` is **absent or
> segment-only at MRK, BMY and WWD**. On those three issuers **no detector can run at
> all**, so the field is not *wrong* there — it is *unavailable*, and an artifact that
> treats absence as a zero, or as a clean read, is failing silently. **Absence must be
> recorded as `UNRESOLVABLE-FROM-PLATFORM`, never as a passed check.**
>
> **⚠️ CORRECTED at 002 Phase 3 — DETECTOR AVAILABILITY IS TWO AXES, NOT ONE, and the
> single-axis reading put opposite dispositions in the same bucket.** The register
> previously recorded only one axis — *"gross profit is absent"* — and the coverage hole
> above is phrased that way. The second axis is **whether `OperatingIncomeLoss` is filed
> as a first-class consolidated subtotal.** **BWXT sits in the RESOLVABLE cell (with
> LUNR): it files no gross-profit line, yet operating income is recoverable exactly,
> because the filer's own calculation linkbase supplies the identity. MRK, BMY and WWD
> sit in the unresolvable cell. Recording only `gross_profit_line_present` would bucket
> BWXT with MRK when their dispositions are OPPOSITE.**
>
> **And the absence is PRESENTATIONAL, not conceptual.** BWXT files
> `CostOfGoodsAndServicesSold` (662,849) — the filer simply presents **no subtotal**.
> **Two independent NAME TRAPS sit on the same detector:** `GrossProfit` returns 0 facts
> **and plain `Revenues` returns 0 facts** (the filed concept is
> `RevenuesFromExternalCustomers` / `RevenueFromContractWithCustomerExcludingAssessedTax`).
> **A zero-fact return is therefore evidence about the CONCEPT NAME, not about the
> ISSUER** — resolved only by reading the statement face.

> **⚠️ Edge case — RETESTED AND REFUTED AT 002 PHASE 3.** The register recorded MRCY as
> *"DA-23-clean with an operating income of $0.280M on $983.6M of revenue (0.03% margin)…
> This is why the component identity is mandatory rather than a spot-check."*
> **The identity WAS run, and the verdict was still wrong. MRCY is the most contaminated
> issuer in the phase: 11 of 13 filed periods are losses served as identical positive
> magnitudes, and the only 2 correct values are the only 2 filed-positive periods.**
>
> **The method error is the finding.** 001 ran the identity on **the period it was
> reporting** and not on **the period it was comparing against** — and the reported period
> is one of the two filed-positive ones, so it passed **by construction**.
>
> > **A detector run only on the subject of a comparison cannot detect a comparison error.**
>
> **What follows is the most compact DA-23 reproduction in the thesis.** 001's `−98.6%`
> **is reproducible only from the stripped comparator**: on filed signs the movement is
> **+19,907 favourable and the percent change is UNDEFINED, because it crosses zero.**
> Its prior-year margin of `2.2%` is filed as **(2.1)%** — so the movement is **+2.1 points
> of IMPROVEMENT, not deterioration.** And its `—` for prior-year gross profit **hides a
> filed 254,494 = 27.9%**, with p.33 stating the **70 bp improvement** verbatim.
>
> **Two portable detectors came out of this issuer.** (1) **Articulation:** a served series
> fails articulation by **exactly 2 × the stripped term**. (2) **Per-value-sign, provable in
> one line:** `Other (expense) income, net` filed `(3,093) | 2,304 | (5,613) | (2,900)` — 12
> of 13 filed negatives served as magnitudes, and **the one filed-positive is the one cell
> served unchanged. No concept- or issuer-level transformation can produce that.**

### DA-24 — NON-OPERATING CONTAMINATION of `operating_income`

A non-operating item flows through the operating line, so the field measures a
transaction or a write-down rather than operations.

> **⚠️ CORRECTED AT 002 PHASE 3 — THIS ENTRY'S DEFINING INSTANCE WAS MISCHARACTERISED, AND ITS
> INDEPENDENCE PROOF DOES NOT HOLD.** Both corrections come from re-testing the entry against
> its own origin issuer. **The entry was named for a GAIN and the thing it was named after is
> a LOSS.**

| | |
|---|---|
| **Instance — CORRECTED** | EchoStar (SATS) 2025 Q3 operating income was **4.6× revenue** — the magnitude reproduces exactly (`16,641,875 / 3,614,258 = 4.605×`). **But it is NOT a spectrum-licence sale.** It is a **non-cash 5G-Network IMPAIRMENT CHARGE of `$16,481,468` thousand**, triggered by the AT&T/SpaceX transactions. **The licences REMAIN ON THE BALANCE SHEET at 2026-03-31 (`$34,550,802` thousand); AT&T took only a SHORT-TERM SPECTRUM MANAGER LEASE; and NO GAIN IS RECOGNISED BECAUSE NOTHING HAS CLOSED.** **This is the entry's shape with the OPPOSITE SIGN.** |
| **The progression was contaminated too** | The quoted series `2.3% → 5.7% → 460.5% → 118.1% → 10.7%` reproduces arithmetically **but is wrong twice over: four of its five terms are the ABSOLUTE VALUES OF LOSSES, and the 118.1% term is annual-on-annual (a DA-26 instance sitting inside a DA-24 exhibit). Q4 2025 is therefore ABSENT from the progression entirely.** Correct filed series: **`(2.28)% → (5.73)% → (460.46)% → (20.54)% → +10.71%`.** |
| **⚠️ The definition must name a GAIN *AND* a CHARGE** | **VRT supplies the charge case independently**: its only acquisition item above the operating line is PurgeRite contingent consideration at a **`$62.0M` charge**. **A definition written for a gain will not fire on a write-down, and vice versa.** |
| **Distinct mechanism** | **Composition**, not sign. DA-23 corrupts the *sign*; DA-24 corrupts the *composition*. **At SATS the two co-occur inside one figure** — the impairment is both a DA-24 contamination *and* sign-stripped — which is why the independence claim below failed. |
| **⚠️ Independence — MEASURED, AND THE MEASUREMENT FAILS** | The entry previously claimed: *"SATS exhibits DA-24 without DA-23 (its EPS × shares reconciles to 0.3%). This is the cleanest proof the two diagnoses are distinct."* **THE PROOF IS INVALID, on two independent grounds.** **(1) It uses a test the register forbids.** DA-23's own detector table rules `EPS × shares` **INADMISSIBLE as a sign test** — it passes on both sides of a flip. **DA-24's foundation rested on a measurement the register had already declared unusable.** **(2) Even taken at face value it is arithmetically blind.** The residual `\|EPS\|×shares − \|NI\|` is **INVARIANT UNDER A GLOBAL FLIP** — both operands carry the same strip, so the check returns the same value whether or not a strip is present. **It cannot detect the defect it was used to rule out.** **AND the claim is substantively false: DA-23 IS present at SATS in the same periods** (12/12 filed-negative subtotals stripped, 8/8 filed-positive clean, zero exceptions). **"DA-24 without DA-23" is false at SATS.** |
| **Status of the entry** | The entry **remains valid as a defect class** — non-operating contamination of the operating line is real and VRT, SATS and MRCY all exhibit it in one direction or the other. **What is withdrawn is the specific SATS instance's characterisation and the independence proof.** **Independence is now UNSUPPORTED rather than disproven** — the two defects co-occur at SATS, which is consistent with both a shared cause and a coincidence, and **no admissible measurement currently separates them.** Any artifact asserting independence must supply one. |

### DA-25 — NORMALISED PER-UNIT METRICS

An issuer-defined "per unit" figure may be a **normalisation**, not a derivation, and
may not be reproducible from the audited segment tables.

| | |
|---|---|
| **Instance** | RKLB discloses `revenue per launch` implying a **51.6%** launch gross margin; the audited segment table implies **42.9%**. The disclosed metric is defined by the issuer as *"average transaction price attributable to launch contract performance obligations… regardless of recognition method."* |
| **Why it matters** | The metric is **the only demonstrated per-launch disclosure in the universe** (it converted DA-01 basis B from `MODELED` to `DEMONSTRATED`), so it carries unusual weight — and it does not reconcile to the audited segment table. |
| **Remedy** | Report the issuer-defined metric **and** the segment-table derivation side by side. Never quote one as though it were the other. Where they diverge, the segment table governs any margin claim; the issuer-defined metric governs only itself. |

### DA-26 — ANNUAL figures mislabelled as QUARTERLY in the metrics block

**20 issuers tested, 19 exhibit it — and the twentieth falsifies "universal".** HWM, TDG,
BA, GOOG, MSFT, NVDA, SATS, NOC, LMT, RTX, PL, KRMN, VOYG, GSAT, MRK, AMGN, BMY, WWD, HEI
all exhibit it. **FLY does not**: its served rows carry **interim cumulative** figures and
never annual ones, and every cumulative identity reconciles. Most exhibitors show it
**twice, in consecutive years**.

> ⚠️ **CORRECTED at v1.6.0 — this entry read "universal, 19 of 19" until thesis 003
> tested a twentieth issuer.** The count was not wrong about the nineteen it named. It was
> **untestable as stated**: a population of nineteen that happens to exclude the one
> counterexample cannot distinguish a universal defect from a merely common one, and the
> word "universal" was doing work the census could not support. Thesis 003's
> `_cross/launch-cost-curve-value-migration_synthesis.md` correction #4 records this, and
> its instruction travels with the finding: **do not report DA-26 as universal, and do not
> apply it without running the screen.** DA-26 is **screen-conditional**, not universal.

| | |
|---|---|
| **The label VARIES by issuer** | HWM's annual figure appears as `Q4`/`Q1`; TDG's as `Q3`. It therefore **cannot be screened by position** — only by reconciliation against known annual totals. A checker written as "ignore the Q4 row" passes every issuer it was written for and fails the rest. |
| **Whole-statement, not a revenue quirk** | At **AMGN the Q4 row carries the annual for BOTH revenue and operating income**, so a Q4-row model overstates both by roughly **4×**. |
| **Lands on the year-end quarter at non-calendar issuers** | PL (January), HEI (October), WWD (September). This is the subtlest form, because a year-end quarter is *legitimately* the largest — the error is invisible without a reconciliation. |
| **⚠️ Rows are reliably "not a quarter" but NOT reliably "a full year"** | WWD FY2024 conforms; its FY2025 row implies a year-end quarter that **dips 16% sequentially** mid-sequence, which no other issuer's annual reading requires. **Two readings are live** — a genuinely weak quarter, or trailing-twelve-month contamination — and the extract cannot separate them. |
| **Consequence** | Any quarterly trend built from `get_company_financials` metrics is contaminated. |
| **Independence** | This is the **third independent defect in the same extracted block**, alongside DA-23 and DA-24. **HWM is clean on DA-23 and exhibits DA-26** — the proof of independence. |

### DA-27 — fiscal-period LABELS derived from the CALENDAR quarter, not the issuer's fiscal calendar

**Confirmed n = 4 of 4, and the pattern partitions the population perfectly.** The
platform buckets a period by **calendar quarter measured from 1 January**, then labels
the bucket with the issuer's *fiscal* year. That is **exact for December-year-end issuers
and off by one for every other fiscal year-end.**

| Issuer | Fiscal year-end | The error |
|---|---|---|
| PL | January | Period ending 2026-04-30 — its FY2026 Q1 — labelled `Q1` |
| AVAV | April | All four rows offset; a **full fiscal year** labelled `Q1` |
| WWD | September | Period ending 2026-06-30 — its FY2026 **Q3** — labelled `Q2` |
| HEI | October | The six-month H1 period ending 2026-04-30 labelled `Q1` |

**Every December-year-end issuer in the universe shows no offset.** A pattern that
separates a population perfectly on one variable and on nothing else is a **mechanism,
not a coincidence.**

**Distinct from DA-26 — do not merge them.** DA-26 is a wrong **VALUE** in a quarter row;
DA-27 is a wrong **LABEL** on internally-consistent values. A labelling error misorders a
time series; a value error corrupts every ratio computed from it. The blast radii and
the remedies differ, so the register entries must.

> **They compound at non-calendar issuers** — supplying the wrong label *and* the wrong
> value, producing the same wrong conclusion by two independent routes.

**A correction recorded in place.** WWD was initially read as *not* offset because its
values are internally consistent. **Internal consistency of values is not evidence about
labels** — correcting that removed the only counterexample and turned n = 3 of 4 into
n = 4 of 4.

### DA-28 — capital-structure discontinuity around an IPO invalidates share-count-based detectors

At **HAWK**, four different share counts coexist in a single extract: **4,168,374**
tagged, **8,359,379** Q1 weighted, **61,924,756** Q2 weighted, **97,965,552** extract
field. The EPS bridge fails by **72%**, against **sub-1% for every clean issuer in the
universe.**

| | |
|---|---|
| **Cause — identifiable, and NOT DA-23** | A listing in Q2 2026 (financing inflow **+$413.009M**; equity **$109.5M → $794.8M**) means the weighted-average share count straddles two capital structures. **No arithmetic test recovers the true figure, because the correct denominator is a time-weighted blend the extract does not expose.** |
| **Why this matters beyond HAWK** | The universe contains several recent listings. **Any issuer whose first reported quarter straddles its IPO will fail the EPS bridge for a legitimate reason.** |
| **Consequence for the DA-23 detector** | A thesis screening for DA-23 by EPS reconciliation will produce **false positives** on recent listings. **The DA-23 detector requires a listing-date guard.** KRMN and VOYG both passed cleanly — *because both had already reported a full post-IPO quarter.* HAWK had not. |

**Why three new entries were added at once.** DA-26, DA-27 and DA-28 were each found by
the same universe-wide sweep that extended DA-23's census. They share a cause — a
period-and-sign extraction layer that is reliable for December-year-end US issuers and
degrades for everyone else — and they were registered together because **a thesis that
patches one and not the others will still be wrong**, by a route it has not tested.

### DA-29 — BACK-SOLVED AND OPAQUE CHECKS: a reconciliation that closes is not thereby a check

**This entry is a different kind from DA-23…DA-28.** Those describe **defective data**. This
describes a **defective check** — an inconsistency that *closes* while testing nothing. It is
registered because the programme has now been misled by this class more than once, and
because **a passing check is the artifact most likely to be accepted without examination.**

> **THE MECHANICAL CIRCULARITY TEST.** **If any term in a reconciliation appears NOWHERE in
> the source, the check is a BACK-SOLVE.** A genuine reconciliation is assembled from values
> that exist independently and then shown to agree. A back-solve takes the one value it wants
> to produce and derives the rest to fit. **The two are indistinguishable by arithmetic — both
> close exactly — so the test cannot be run on the closure. It must be run on the TERMS.**
> **Operationally: locate every term in the filed statement. If one cannot be located, the
> closure is uninformative regardless of its precision.**

| | |
|---|---|
| **Instance 1 — 001's unsourced clearance** | 001 cleared BWXT via a reconciliation containing **`$90.7M`**. The filed `Total Costs and Expenses` is **$775.1M**; the two differ by **684,391**, and **$90.7M appears in no BWXT filing.** The check closed. **It was a back-solve, and 001 read it as a clearance.** 002's replacement (775,091 and 21,565) has **every term filed**. |
| **Instance 2 — `computed` is not reproducible from the instrument's own tree** | At BWXT Q1 2026, `OperatingIncomeLoss` `computed` = **71,139,000** while **the instrument's own returned calculation tree yields 106,691,000 — internally inconsistent within a single run**, with the same run reporting the parent concept exact. **The instrument never discloses which role produced each `computed` row**, so a `computed` value cannot be independently reproduced from the material the instrument itself returns. **Consequence: `computed` is an opaque assertion, not a derivation, and may not be cited as one.** |
| **Instance 3 — `reported` mis-selection, three times in one filing** | At the same filing: Q1 2025 operating income `reported` **97,746** vs filed **96,630**; equity `reported` **1,286,000** vs `computed` **1,280,614,000**; and **PP&E `reported` carrying GROSS for a NET concept.** **The `reported` column is therefore not definitionally the filed value.** It must be reconciled to the statement face before use. |

**Why the class is dangerous.** Every other register entry produces a *wrong number*, which a
downstream reader may catch by plausibility. **This class produces a RIGHT-LOOKING number and
a closed check**, and it survives review *precisely because the arithmetic is exact.* The
remedy is procedural and cannot be automated away: **name the source of every term.**

### DA-30 — TWO BASES ON ONE CONCEPT, COLLAPSED WITHOUT A BASIS FIELD

| | |
|---|---|
| **Instance** | **BWXT files `OperatingIncomeLoss` on two bases** — equity-inclusive (per its calculation linkbase and its own footnote) and equity-exclusive otherwise. **The platform serves both under one concept with no basis field. Equity is 20.2% of the Q1 2026 figure.** |
| **Relation to the artifact contract** | Distinct from, and prior to, the contract's `no_single_basis_collapse` rule. That rule governs an **artifact** that quotes one competing basis and not the others. **This is the platform collapsing two bases before any artifact sees them** — so the artifact cannot comply by diligence alone; it must first *discover* that a second basis exists. |
| **Consequence** | Quoting "operating income" for a BWXT-class issuer is **incomplete by construction** until the basis is named. **Requirement: any artifact quoting a multi-basis concept must name the basis, and must state where the basis was established.** No artifact in thesis 002 names it — recorded as a live §1c gap. |

### Disposition Classes (P4)

Two failure modes were previously conflated under one label. They demand different
remedies and are now separate.

| Class | Definition | Remedy | Canonical case |
|---|---|---|---|
| `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | The disclosure **does not exist publicly at all**. | Name the specific disclosure that would resolve it; monitor. | **PIL-4 microgravity** — Varda's cost-per-kg-returned (Varda is private) and UTHR's programme economics (immaterial to a $783M/quarter issuer, so never broken out). |
| `UNRESOLVABLE-FROM-PLATFORM` | The data **is public but unreachable**, or is commercially licensed, or requires an external registry the platform does not carry. | Record the gap as a finding about *platform reach*, not about the world; do not report it as an absence of evidence. | **PIL-6** — FCC IBFS / ITU Space Network List. **P5 terrestrial denominator** — colocation and greenfield costs are *commercially licensed* data. |

A pillar in either state is **not** dropped and **not** failed. It is carried in
`known-open` and reported with the specific disclosure or source that would resolve it.
A pillar in this state is a finding about **disclosure or platform quality** — itself
relevant output, not a gap in the research.

---

## Risk Framework

- **Single Position**: 4% default; 2% for binary catalysts (launch outcomes, licensing
  and spectrum decisions, contract award/termination); 6% absolute maximum
- **Sub-Sector Concentration**: ≤ 25% of NAV in any single sub-sector from the Sector
  Preferences table
- **Space Theme Aggregate**: ≤ 40% of NAV — this workspace is a single-theme book, so
  the theme cap binds before the sub-sector cap in practice
- **Macro-Driven Exposure**: ≤ 15% of NAV in positions whose primary driver is a macro
  variable rather than a company catalyst
- **Stop-Loss**: 30% thesis-driven — a thesis is exited when its stated falsifier
  triggers, regardless of price; 20% technical invalidation for entry-level protection.
  Stops are wide by design: this universe routinely moves ±40% on single events, and
  tight stops convert volatility into permanent loss.
- **Concentration Rule**: at most 3 positions in Tier 1, and at most 2 in any single
  sub-sector, to prevent a basket of correlated small caps masquerading as
  diversification

---

## Methodology Foundation

- **Equity Research**: the agentii arc — constitution → specify → plan → tasks →
  implement → converge. Skills deploy per the spec's Skill Deployment Matrix; depth is
  Deep for SPCX and any position above 3%, Standard elsewhere.
- **Valuation**: scenario-weighted **sum-of-the-parts** is primary for multi-segment
  issuers (SPCX reports Space, Connectivity, and AI — three different businesses with
  three different multiples). **DCF** is admissible only where an issuer has ≥ 3 years
  of positive free cash flow or a contracted backlog covering the forecast period.
  **Comps are a cross-check only** and are never primary for a pre-profit issuer.
- **Orbital-specific valuation test**: for any space-compute or space-manufacturing
  thesis, the model must carry an explicit **cost-per-kilogram-launched** line and a
  **revenue-per-kilogram-returned** line. A model without both is rejected.
- **Catalyst Requirement**: a dateable catalyst within **180 days** for any trade idea.
  Where the catalyst is regulatory (FCC, FAA, ITU) or programmatic (contract award,
  launch window, FDA action), the expected date and its source must be recorded.

---

## Amendment Log

### 1.5.0 — 2026-09-18 — Two register entries of a new kind: DA-29, DA-30

**Added DA-29 — BACK-SOLVED AND OPAQUE CHECKS**, the register's first entry describing a
defective *check* rather than defective *data*. A reconciliation that closes is not thereby
a check: **if any term appears nowhere in the source, it is a back-solve**, and a back-solve
closes exactly, so the test must be run on the terms and not on the closure. 001's BWXT
clearance contained a `$90.7M` term that appears in no filing — the filed Total Costs and
Expenses is **$775.1M** — and closed anyway.

**Added DA-30 — TWO BASES ON ONE CONCEPT, COLLAPSED WITHOUT A BASIS FIELD.** BWXT files
operating income equity-inclusive and equity-exclusive under one platform concept; equity is
**20.2%** of the Q1 2026 figure. This is *prior to* the artifact contract's
`no_single_basis_collapse` rule, and therefore not dischargeable by diligence alone.

**Corrected DA-23 twice.** (1) **BWXT moves out of `Clean`** into a new row — **clean at
every subtotal, stripped at one component**, the first issuer where both hold at once:
`GainLossOnSalesOfAssetsAndAssetImpairmentCharges` served as an absolute magnitude, with the
exact strip signature `diff = 2 × 125`, and `status` marked `pass`. (2) **Detector
availability is TWO axes, not one** — BWXT is *resolvable* despite filing no gross-profit
line (its own calculation linkbase supplies the identity), while MRK, BMY and WWD are not. A
single-axis flag would bucket BWXT with MRK when their dispositions are **opposite**.

**No principle, axiom, bound, disposition class or sector bias changed.** Every bias and
every falsifier stands as written at 1.4.0. Reported for the gate-5 budget confirm; **not
separately dispatched** — the DA-29/DA-30 obligations on the 23 pre-existing artifacts are
folded into Phase 7's validation ledger, which is the artifact whose function is that census.

### 1.4.0 — 2026-09-18 — MINOR: Sector Preferences rationales restated against A1b
Caught by `agentii.clarify` round 2 on 002. **The v1.3.0 A1a/A1b split was not propagated
to the Sector Preferences table**, leaving the document internally contradictory in three
rows. Launch Services was **Overweight/High on the rationale *"The toll road"* — which is
A1b**, the axiom v1.3.0 had declared falsified in the immediately preceding section. Space
Infrastructure & Components was Neutral/Medium on a **"program-concentration risk"**
rationale that the measured mechanism **inverts**. Earth Observation was Underweight/Low
on **"persistent negative unit economics"**, refuted by PL's universe-leading 53.5% gross
margin. **Every bias is retained; only the reasoning changes.** Launch stays OW/High on an
A1a-consistent basis — SPCX Space runs a 65.8% gross margin, the highest in the universe,
with cost of revenue flat while revenue rose 29%, and RKLB holds the only demonstrated
per-launch economics. Space Infrastructure stays Neutral/Medium because the layer is not
space-pure. Earth Observation stays UW/Low as a **timing** judgment, not a structural one.
Nothing numeric is corrected or removed.

### 1.3.0 — 2026-09-18 — MINOR: A1 split, F5 split, Data-Integrity Register, disposition classes
Split **A1** into **A1a** (launch cost is the master *cost* variable — holds) and
**A1b** (launch is the master *value* variable — **falsified**). The decisive evidence
is **SPCX's own Q2 2026 10-Q reporting its own chosen throughput metrics falling** —
mass to orbit −25.6%, Falcon launches −17.8%, internal Starlink launches −25.0%,
Starship 3 → 1 — while consolidated revenue rose 53.7% and the Space segment fell to
12.3% of revenue. Corroborated by RKLB (+62% revenue, launch revenue −$2.1M) and FLY
(+657% from Spacecraft Solutions). This is a **split, not a redefinition** — A1a
preserves the founding axiom's binding half, which is why the bump is MINOR rather than
MAJOR. **A qualification now travels with A1b**: SPCX's Space segment carries a **65.8%
gross margin**, the highest in the universe, with cost of revenue flat while revenue
rose 29% — so **Falcon launch economics are good; the segment loss is Starship R&D
reinvestment.** Citing A1b to argue "launch is a bad business" misreads it.
Split **F5** into **F5a** (fully reusable: propellant floor, hard) and **F5b**
(partially reusable: upper-stage manufacturing floor, soft); F5 as written bounded
Starship-class vehicles only, and applying it to Falcon-class vehicles understates
achievable price by an order of magnitude, since propellant is ~2–3% of Falcon 9's
marginal cost. Added the **Data-Integrity Register** — **six** defects, not three:
DA-23 sign stripping (**census extended to 6 of 6 loss-making stripped, 19 of 19
profitable clean**, with three detectors registered in descending reliability and the
EPS test ruled inadmissible), DA-24 asset-sale contamination, DA-25 normalised per-unit
metrics, and three found by the same universe-wide sweep — **DA-26** annual figures
mislabelled as quarterly (**universal, 19 of 19** — ⚠️ SUPERSEDED at v1.6.0: *20
tested, 19 exhibiting; FLY is the falsifying counterexample*; kept as the v1.3.0
decision record, not rewritten), **DA-27** fiscal-period labels
derived from the calendar quarter (**n = 4 of 4**, partitioning the population by fiscal
year-end), **DA-28** IPO capital-structure discontinuity invalidating share-count
detectors. Also registered: the **coverage hole** at MRK, BMY and WWD where
`OperatingIncomeLoss` is absent and no detector can run. Added
**`UNRESOLVABLE-FROM-PLATFORM`** as a disposition class distinct from
`UNRESOLVABLE-FROM-PUBLIC-SOURCES`. Corrected nothing and removed nothing: no figure
previously stated in this document is revised. Re-examination scope is bounded to
PIL-1, PIL-3, PIL-5, PIL-6 and the DA-sensitive artifacts of `001-technology-baseline`;
reported for the gate-5 budget confirm, **not dispatched**.

### 1.2.0 — 2026-09-18 — MINOR: principle register, agent-coverage audit, count corrections
Added Section 0b (Principle Register) mapping every identifier to its defining section,
which retires five phantom identifiers — P1, P5, P7, P8 and P9 were declared as added
principles in the 1.0.0 report but never given a body definition; P7 and P8 appeared
nowhere in the document at all. No new principle was created: each maps to substance
that already existed. Replaced the universe Data column with an audited three-class
coverage classification (READY 37 / PARTIAL 9 / NOT_READY 13) derived from per-ticker
queries against all seven source types, discharging the "unverified for Tiers 3–4"
caveat. Documented two methodology traps: the GOOGL→GOOG ticker alias, and the bulk
`list_coverage` endpoint being a partial view that must not be treated as authoritative.
Corrected the listed-name count from the erroneous "28 → 46" to the audited
45 → 57. No theses pinned, so no re-examination dispatched.

### 1.1.0 — 2026-09-18 — MINOR: universe expanded, orbital-compute gate added
Extended the listed universe by 18 names across Tiers 1–4 (YSS, HAWK, MDA, TSAT,
GILT, SGBAF, BWXT, AVAV, TRMB, GRMN, PLTR, TER, plus the AAM adjacents JOBY/ACHR),
replaced the 6-name Private Watchlist with a full Pre-IPO and Venture Roster across
eight segments, added a China Commercial Space read-through tier, refined F1's solar
chain to reconcile with the published ~5,640 m²/MW figure, added A5, and introduced
P10 (Orbital-Compute Underwriting Rule) and P11 (In-Flight M&A Treatment).
No theses were pinned, so no re-examination was dispatched.

### 1.0.0 — 2026-09-18 — Ratification
Initial ratification. No prior pins existed; no re-examination dispatched.

---

*SemVer rules (Q33): MAJOR = a principle removed or incompatibly redefined; MINOR =
a principle added or substantially extended; PATCH = wording only. MAJOR/MINOR bumps
mark `constitution_pin`-older theses `stale` and dispatch re-examination after the
gate-5 budget confirm. PATCH never triggers review. Current version: **1.5.0**.*

*Note on the A1 and F5 splits (v1.3.0): both are MINOR, not MAJOR, because each
**preserves** its parent's binding half and adds a child that carries the previously
collapsed ambiguity. A split that left the parent's claim false would be MAJOR. Here
A1a and F5a remain true as written; A1b is newly stated and newly falsified; F5b
replaces a misapplication rather than a truth.*

<!--
Sync Impact Report entry
  bump: minor
  note: Universe expanded by 18 listed names + full Pre-IPO/Venture Roster + China read-through tier; F1 solar chain refined (eclipse/packing/EOL multipliers); A5 added; P10 Orbital-Compute Underwriting; P11 In-Flight M&A Treatment
  old → new: F1 array ceiling 2,450 m²/MW → 5,000–5,600 m²/MW (eclipse/packing/EOL
             multipliers added); Universe Tiers 1–4 [CORRECTED at 1.2.0: this entry
             originally read "28 names → 46 names" — both figures were estimates,
             not counts. Audited figures are 45 → 57]; Private Watchlist 6 names →
             Pre-IPO Roster, 8 segments; A4 → A4 + A5; principles P1–P9 → P1–P11
  deferred: (a) credit-spread source; (b) ERP / terminal-growth confirmation;
            (c) private valuations are CLAIMED, not DEMONSTRATED; (d) Tier 3–4 coverage
            [DISCHARGED at 1.2.0 — now individually verified]; (e) Europe/Japan listed
            names lack platform coverage [CONFIRMED at 1.2.0: Eutelsat, Avio,
            SKY Perfect JSAT, Astroscale all carry no coverage]
-->

<!--
Sync Impact Report entry
  bump: minor
  note: Added Section 0b Principle Register (retires phantom P1/P5/P7/P8/P9); replaced universe Data column with audited three-class agent-coverage READY/PARTIAL/NOT_READY (37/9/13); documented GOOGL-to-GOOG ticker alias and the bulk list_coverage partial-view trap; corrected listed-name count 45 -> 57; fixed stale SemVer footer
  old → new: [record changed principles here]
  deferred: [none]
-->

<!--
Sync Impact Report entry
  bump: minor
  note: A1 split into A1a/A1b (launch cost = master COST variable holds; launch = master VALUE variable does not hold — 3 independent issuer confirmations); F5 split into F5a/F5b (fully vs partially reusable launch-cost floor); Data-Integrity Register added (DA-23 sign stripping 12 issuer-quarters zero exceptions, DA-24 asset-sale contamination, DA-25 normalised per-unit metrics); UNRESOLVABLE-FROM-PLATFORM added as disposition class distinct from UNRESOLVABLE-FROM-PUBLIC-SOURCES
  old → new: [record changed principles here]
  deferred: [none]
-->

<!--
Sync Impact Report entry
  bump: minor
  note: Sector Preferences rationales restated against A1a/A1b (three rows: Launch Services, Space Infrastructure & Components, Earth Observation). All biases retained — Launch stays OW/High on an A1a-consistent basis; Infrastructure stays Neutral/Medium on dilution grounds; EO stays UW/Low as a timing rather than structural judgment. Corrects an internal contradiction left by v1.3.0, which amended A1 without propagating to the sub-sector table.
  old → new: [record changed principles here]
  deferred: [none]
-->

<!--
Sync Impact Report entry
  bump: minor
  note: DA-26 corrected to a falsified census (20 tested, 19 exhibiting; FLY the counterexample) per 003 correction #4; the PARTIAL class redefined to drop the sec_filings==0 condition that mislabelled researchable names; §Universe Definition re-cut to ONE axis (function in the value chain) with an explicit membership test, moving PL/BKSY/HAWK/SPIR to Tier 2 and VRT out of Tier 4 membership
  old → new: 1.5.0 → 1.6.0
  deferred: [none]
-->
