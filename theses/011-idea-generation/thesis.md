# Thesis: 011 — Idea Generation, Strategies & Cases

Living file. `spec.md` is the frozen specification; this file is updated as findings
land. Machine-readable frontmatter below is authoritative for the dispatcher.

> **Sequencing note.** This thesis was upgraded from a stub at the 2026-09-18 clarify
> round on 002. Its dependency is **split**: P1–P6 depend on **001 alone** and start
> immediately; P7 (sizing) keeps the original 004–010 gate. The cost — an unpositioned
> main line published first — is stated in `spec.md` §1d rather than hidden.

```yaml
thesis_id: 011-idea-generation
constitution_pin: 1.4.0
created: 2026-09-18
as_of: 2026-09-18
status: active

claim: >
  Space is a cost curve, not a value pool. A1a holds — cheap launch makes orbital
  businesses possible — but A1b is falsified, so cheap launch does not distribute the
  value to launchers. Value settles in the layers indifferent to which operator or
  programme wins, and in the finite allocated assets that are priced rather than granted.
  The consequence is uncomfortable and is the thesis's headline: you cannot buy this
  theme cleanly — the space-pure names carry the sector's worst economics, and the names
  with the best margins are mostly not space companies. Of seven strategy candidates the
  evidence supports, four are actionable, and not one of the four is a bet on space
  technology succeeding.

pillars:
  - id: PIL-1
    priority: P1
    title: The main line is real — one argument explains four independent findings
    minimum_defensible_view: true
    mechanism_axes:        # narrowed at clarify round 2: BOTH operate jointly
      - programme_concentration: "single-programme dependence is the discriminator; HEI/KRMN top vs GSAT monopsony bottom"
      - revenue_recurrence: "aftermarket/installed-base vs programme-contingent OEM"
    mechanism_note: >
      The strongest counter-argument is that the ladder is an aftermarket-vs-OEM artifact
      rather than a programme-structure fact. It is not — the ladder HOLDS WITHIN OEM
      (KRMN, OEM components, 19.1% vs LMT, OEM prime, 12.4%), so both axes operate jointly.
      A thesis attributing the ladder to either axis alone is UNFRAMED_REFERENCE.
    wrong_if:
      - metric: count_of_the_four_findings_attributable_to_a_single_common_mechanism
        threshold: 4
        source: cross_issuer_filing_analysis
        op: "<"
    wrong_if_companion: >
      Added at clarify round 2 to prevent a false fire: the spread must invert WHILE BOTH
      LAYERS' REVENUE IS GROWING, and persist across a full cycle. A single negative print
      with falling component-layer revenue is a cycle, not a falsification.
    ladder_scope: "8 issuers measured — selected by which artifacts 001 wrote. Extension to all 21 Tier 3 names assigned to 008; until it runs the claim is DEMONSTRATED on 8 and MODELED beyond."
    the_four_findings:
      - {id: margin_ladder, source: "001 synthesis 4.1", register: who_earns}
      - {id: value_migrated_out_of_launch, source: "001 synthesis 4.6", register: where_value_went}
      - {id: fixed_cost_absorption_binds, source: "001 synthesis 4.2", register: why_operators_lose}
      - {id: orbital_compute_out_chosen, source: "001 synthesis Line 5", register: why_narrative_did_not_convert}
    migration_evidence_clean:
      - {series: SPCX_Space, boundary: clean, quoted: true, note: "the series that SURVIVES the boundary — and it fell 1.9% H1 2026"}
      - {series: SPCX_Connectivity, boundary: clean, quoted: true, note: "never merged; wholly organic; 54.9% of revenue"}
      - {series: SPCX_AI, boundary: CONTAMINATED, quoted: false, note: "xAI merged 2026-02-02 under common control, prior periods recast — must not be cited as organic migration. Routed to 002 P6."}
    subscriptions:
      - {ticker: HEI, skill: business-model}
      - {ticker: KRMN, skill: business-model}
      - {ticker: GSAT, skill: competitive}
      - {ticker: SPCX, skill: business-model}
      - {ticker: PL, skill: unit-economics}

  - id: PIL-2
    priority: P2
    title: Strategy 1 is actionable but is NOT a space investment, and the report must say so
    wrong_if:
      - metric: count_of_component_layer_candidates_with_a_disclosed_space_revenue_share_above_0.25
        threshold: 0
        source: 10-K_segment_and_revenue_disaggregation_tables
        op: ">"
    dilution_case: "HEI runs 2.6% R&D — an aerospace aftermarket franchise; space exposure is incidental"
    subscriptions:
      - {ticker: HEI, skill: business-model}
      - {ticker: HEI, skill: ratio-analysis}
      - {ticker: KRMN, skill: business-model}
      - {ticker: KRMN, skill: competitive}
      - {ticker: WWD, skill: business-model}
      - {ticker: TDG, skill: business-model}

  - id: PIL-3
    priority: P3
    title: Strategy 2 — fixed-cost absorption is a valid screen and a statement about timing, not about space
    wrong_if:
      - metric: count_of_preprofit_names_closing_a_break_even_multiple_above_2x_without_external_financing
        threshold: 0
        source: 10-Q_cash_flow_statement_and_liquidity_note
        op: ">"
    worked_cases:
      - {ticker: PL, break_even_multiple: 1.69, gross_margin: 0.535, opex_ratio: 0.906}
      - {ticker: YSS, break_even_multiple: 2.86, gross_margin: 0.240, opex_ratio: 0.686}
    subscriptions:
      - {ticker: PL, skill: unit-economics}
      - {ticker: YSS, skill: unit-economics}
      - {ticker: RKLB, skill: unit-economics}
      - {ticker: FLY, skill: unit-economics}
      - {ticker: LUNR, skill: unit-economics}

  - id: PIL-4
    priority: P4
    title: Strategy 3 — the terrestrial expression has the strongest evidence and the weakest space content
    wrong_if:
      - metric: listed_issuer_orbital_compute_revenue_disclosed
        threshold: 0
        source: 10-K_or_10-Q_segment_disclosure
        op: ">"
    strongest_datum: "MSFT FY2026 capex $115,948M implies 2.9-11.6 GW/yr vs SPCX's 1.4 GW cumulative"
    trap_registered: "SPCX 'AI computational infrastructure' is terrestrial compute with satellite delivery — fails the DA-20 four-way test"
    subscriptions:
      - {ticker: VRT, skill: unit-economics}
      - {ticker: NVDA, skill: secular-trends}
      - {ticker: MSFT, skill: recent-quarter}
      - {ticker: GOOG, skill: secular-trends}
      - {ticker: VRT, skill: competitive}

  - id: PIL-5
    priority: P5
    title: Strategy 4 — the deal spread is actionable and is not a space view at all
    wrong_if:
      - metric: count_of_deal_securities_closing_without_clearing_a_named_gate
        threshold: 0
        source: FCC_8-K_and_merger_proxy_disclosures
        op: ">"
    p11_discipline: "do not underwrite standalone fundamentals; size at the 2% binary cap; re-underwrite from scratch on a break"
    gate_chain: [FCC_licence_transfer, ITU_coordination, DCSA_CFIUS_adjacent, national_market_access]
    subscriptions:
      - {ticker: IRDM, skill: competitive}
      - {ticker: GSAT, skill: competitive}
      - {ticker: SATS, skill: risk}
      - {ticker: IRDM, skill: recent-quarter}

  - id: PIL-6
    priority: P6
    title: Strategies 5-7 are watch items with named triggers, not positions
    wrong_if:
      - metric: count_of_watch_items_with_a_named_resolving_trigger
        threshold: 3
        source: this_thesis_artifact
        op: "<"
    watch_items:
      - {strategy: 5, name: licensed_asset_play, blocked_by: UNRESOLVABLE-FROM-PLATFORM, trigger: "a transferable $/MHz-pop basis, or FCC/ITU registry access"}
      - {strategy: 6, name: unpriced_duopolies, blocked_by: UNRESOLVABLE-FROM-PUBLIC-SOURCES, trigger: "a unit disclosure from RKLB/SolAero or BA/Spectrolab, or a comparable transaction"}
      - {strategy: 7, name: demand_asymmetry, blocked_by: UNRESOLVABLE-FROM-PUBLIC-SOURCES, trigger: "any value/kg or cost/kg figure; a Varda listing or disclosure"}
    subscriptions:
      - {ticker: SATS, skill: competitive}
      - {ticker: IRDM, skill: competitive}
      - {ticker: UTHR, skill: unit-economics}

  - id: PIL-7
    priority: P7
    title: The book is sized, and the theme cap binds before the sub-sector cap
    blocked_on: [004, 005, 006, 007, 008, 009, 010]
    wrong_if:
      - metric: count_of_positions_without_a_dateable_catalyst_within_180_days
        threshold: 0
        source: constitution_Methodology_Foundation_catalyst_requirement
        op: ">"
    binding_constraint: "CONC_THEME 40% binds before CONC_SECTOR 25% in a single-theme book"
    subscriptions:
      - {ticker: SPCX, skill: ratio-analysis}
      - {ticker: RKLB, skill: ratio-analysis}
      - {ticker: KRMN, skill: ratio-analysis}
      - {ticker: VRT, skill: ratio-analysis}

budget:
  max_tasks: 30          # deliberately small — this thesis consumes 001's conclusions and
                         # does not re-research businesses. P1-P6 use ~20; the P7 block
                         # reserves ~10 for when 004-010 land.
  max_retries_per_task: 2

expiry_triggers:
  - earnings_release
  - constitution_bump
  - issuer_discloses_orbital_compute_revenue
  - component_layer_margin_converges_with_primes

depends_on:
  - thesis_id: 001-technology-baseline
    claims:
      - margin_ladder_monotone_in_programme_distance
      - value_migrated_out_of_launch
      - fixed_cost_absorption_binds
      - orbital_compute_out_chosen
      - no_listed_issuer_offers_both_growth_and_margin_except_TER_and_KRMN
  - thesis_id: 002-evidence-validation
    claims: [disposition_classes, validated_input_set_with_bands]
    gate: soft           # P1-P6 can start; figures carry 001's grade until 002 lands
  - thesis_id: "*004-010-segment-theses"
    claims: [segment_rankings]
    gate: hard           # P7 ONLY. P1-P6 are unblocked by design.

macro_sensitivity: high

methodology:
  corpus_retrieval: >
    The knowledge corpus has no industrial or aerospace domain — list_domains returns
    applicable_sectors ["med","tech","fin"] only — so sector-keyed retrieval returns zero
    rows BY CONSTRUCTION. Reporting that emptiness as "no analogues exist" is a false
    negative. Retrieval is therefore by STRUCTURAL SITUATION, and every borrowed analogue
    is labelled borrowed: a cost-curve strategy derived from cultivated meat is a shape
    match, not sector evidence.
  strategy_reads_findings_not_businesses: >
    This thesis grades positions against 001's conclusions rather than analysing
    businesses afresh. Where it needs a business fact, it cites the artifact that
    established it.
```

## Status log

| Date | Event |
|---|---|
| 2026-09-18 | Thesis ID reserved via `agentii.specify` in the program-wide mkdir-as-CAS pass. Stub spec written with the corpus-gap finding. |
| 2026-09-18 | **Upgraded from stub to specified** by `agentii.clarify` **round 1**, invoked on **002**. The question — *"can we form a main-line investment logic for space tech, and several strategies?"* — was answered **yes**, and the disposition was to write the main line into `theses/PROGRAM.md` §0b and make it **this thesis's P1** rather than adding a pillar to 002. **Dependency split**: P1–P6 depend on 001 alone and start now; P7 (sizing) keeps the 004–010 gate. Three answered (Q-1 scope, Q-2 sequencing, Q-3 purity), two carried open (Q-4, Q-5). |
| 2026-09-18 | **`agentii.clarify` round 2** — same invocation, and this round did what a second pass should: it **pressure-tested the claim** rather than restating it. **(1) Found a constitution defect round 1 missed**: §Sector Preferences still rated Launch Services **OW/High on the rationale "The toll road" — which IS the A1b claim §0 declares falsified.** The v1.3.0 split was never propagated to the sub-sector table, leaving it internally contradictory in three rows (Launch; Space Infrastructure, whose "program-concentration risk" rationale inverts the measured mechanism; Earth Observation, whose "persistent negative unit economics" is refuted by PL's universe-leading 53.5% gross margin). **Executed as constitution v1.4.0** — rationales fixed, **all biases retained**. **(2) Four counter-arguments tested against the main line; it survives all four**, but three required tightening: **P1's mechanism narrows to two joint axes** (programme concentration *and* revenue recurrence — the ladder holds within OEM, so it is not an aftermarket artifact); **the falsifier gains a companion condition** (invert *while both layers grow*, across a full cycle, or a cyclical print fires it falsely); and **"AI 32.8%" is boundary-contaminated** (xAI merged 2026-02-02, prior periods recast) and is **routed to 002 P6** — the migration claim now rests on **Space (clean, and the series that fell)** and **Connectivity (clean, organic)**. **(3)** The margin ladder's **8-issuer selection concern is assigned to 008** for extension across all 21 Tier 3 names. **Q-4 and Q-5 resolved**: watch items accepted as outputs; **wave 1 becomes 002, 004, 005, 006, 008** — 003 swaps out, 006 stays. |

## Constitution amendment candidates (NOT executed — require human approval)

| # | Candidate | Trigger | Status |
|---|---|---|---|
| 1 | **Register a cross-listing gap.** The Research Scope Constraints exclude foreign-listed space names (Eutelsat, Avio, SKY Perfect JSAT, Astroscale) for lack of platform coverage and US listing. The corpus carries a **Cross-Listed Biotech Arbitrage ("US Premium")** strategy describing exactly that discount — so the analogue exists while the instrument does not. Either the constraint is revisited or the exclusion is recorded as a *known-unexpressible* theme. | 011 §1c; PROGRAM.md §4 | **Proposed — awaiting approval** |
| 2 | **Record the `MOG-A` / `ENS` coverage asymmetry.** Both carry fund-sourced cases in the knowledge corpus under `Industrials` while the platform shows zero issuer coverage. A case that cannot be validated against filings is a research liability. | 011 §1c; PROGRAM.md §4 | **Proposed — awaiting approval** |

## Known open

- **Q-4 — RESOLVED (round 2).** Watch items with named triggers are accepted as outputs;
  strategy 6 (unpriced duopolies) will **not** be attempted, since 001 established neither
  parent discloses the unit and there is nothing to size.
- **Q-5 — RESOLVED (round 2).** P7 is unblocked early by **promoting 008 into wave 1**,
  swapping out **003** (001 already settled the cost curve's level) while **006 stays**
  (Connectivity is the one OW/High rating 001's evidence supports).
- **P7 still blocked on 004–010 for sizing.** No positions, entries or catalyst calendar
  until those land. Stated in `spec.md` §1d as the deliberate cost of the sequencing split.
- **Macro tension, unresolved by construction.** The main line's actionable strategies are
  long-duration, and the constitution's bias is NEUTRAL because the 10Y sits at 4.80% with
  hike risk priced. **A NET_LONG expression of the main line is a bet on duration, not on
  space.** P7 must size through that lens or state why not.
- **The ladder's selection concern — delegated, not discharged.** The mechanism claim
  stands on **8 issuers chosen by which artifacts 001 wrote**. Until 008 extends it across
  all 21 Tier 3 names, the claim is `DEMONSTRATED` on 8 and `MODELED` beyond them, and any
  artifact quoting it must say so.
- **The "AI 32.8%" flag is now 002 P6's to enforce** — this thesis must not quote that
  figure as organic migration while 002's boundary classification is outstanding.
