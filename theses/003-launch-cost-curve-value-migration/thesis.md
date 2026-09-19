# Thesis: 003 — Launch Cost Curve & Value Migration

Living file. `spec.md` is the frozen specification; this file is updated as findings land.
Machine-readable frontmatter below is authoritative for the dispatcher.

> **Restored to Wave 1** at post-002 review, 2026-09-18. The demotion's premise was
> falsified (`001:PIL-1` HOLDS at ±15%), and 002's completion freed a slot under
> `max_theses_active: 6`. See `spec.md` §Clarifications for the superseded answer, retained.

```yaml
thesis_id: 003-launch-cost-curve-value-migration
constitution_pin: 1.5.0
assumption_pin: "2"
skill_pin: none      # ⚠️ CORRECTED 2026-09-19. This read `registry-1.0.0` — a WHOLE-REGISTRY
                     # version, not a per-skill hash — which is the exact value the new
                     # `skill_pin_wellformed` rule (tools/check_contract.py, added 2026-09-19)
                     # names as the worst case: "it reads as a pin, passes every check, and
                     # pins NOTHING". A thesis spans many skills, so there is no single hash to
                     # pin here; `none` is the declared sentinel. The PER-SKILL hashes — which
                     # are real, validated 12-hex values — are in `reproduce.md`.
corpus_version: agentii-2026-09-18
created: 2026-09-18
as_of: 2026-09-18
status: active
wave: 1

claim: >
  Launch cost is the sector's master COST variable and not its master VALUE variable. The
  cost curve is real but thin — exactly one vehicle in the universe (Electron) has a
  demonstrated marginal cost, and one point is not a curve — while the value pool has
  migrated to the integrator that owns the demand rather than to the launcher or the
  independent operator. The released value was captured upstream and did not pass through
  to the payload customer.

binding_constraint: MASS_LAUNCH_COST

pillars:
  - id: PIL-1
    priority: P1
    title: The complete cost curve — every vehicle x every reuse architecture x all three DA-01 bases, each with the floor its architecture actually implies
    minimum_defensible_view: true
    wrong_if:
      - metric: count_of_universe_vehicles_with_a_demonstrated_price_per_kg_to_LEO_below_their_architecture_applied_launch_cost_floor
        threshold: 0
        source: issuer_filing_or_audited_segment_table
        op: ">"
    subscriptions:
      - {ticker: SPCX, skill: unit-economics}
      - {ticker: RKLB, skill: unit-economics}
      - {ticker: SPCX, skill: operational-kpi}
      - {ticker: RKLB, skill: operational-kpi}
      - {ticker: RKLB, skill: peer-bench}
      - {ticker: FLY, skill: competitive}
      - {ticker: RKLB, skill: what-if}

  - id: PIL-2
    priority: P2
    title: The value pool migrated to the integrator that owns the demand, not to the launcher and not to the independent operator
    wrong_if:
      - metric: count_of_universe_issuers_where_launch_segment_operating_margin_exceeds_non_launch_segment_operating_margin
        threshold: 0
        source: issuer_segment_disclosure
        op: ">"
    note: >
      A1b is TESTED here, not assumed. A thesis assuming it without a test is
      UNFRAMED_REFERENCE (spec §5).
    subscriptions:
      - {ticker: SPCX, skill: business-model}
      - {ticker: RKLB, skill: business-model}
      - {ticker: SPCX, skill: sector-overview}
      - {ticker: RKLB, skill: sector-overview}
      - {ticker: SPCX, skill: secular-trends}
      - {ticker: IRDM, skill: competitive}
      - {ticker: GSAT, skill: competitive}
      - {ticker: RKLB, skill: supply-chain}

  - id: PIL-3
    priority: P3
    title: The curve is CLAIMED, not DEMONSTRATED — exactly one vehicle has a measurable cost series, and its single observed step may be a definitional artefact
    wrong_if:
      - metric: share_of_universe_cost_reduction_claims_with_a_filed_flown_or_audited_basis
        threshold: 0.5
        source: issuer_filing_or_audited_segment_table
        op: "<"
    admissibility_frame: >
      ark_invest__wrights_law_valuation_framework. Wright's Law requires a documented
      learning rate sustained over >=5 cumulative production doublings. Electron supplies
      ONE measured point. One point is not a learning rate and one quarter is not a
      doubling, so this pillar's negative finding is DEFINITIONAL rather than an
      evidential shortfall — launch does not currently qualify as a Wright's Law
      technology, structurally, not for want of disclosure effort.
    subscriptions:
      - {ticker: RKLB, skill: operational-kpi}
      - {ticker: SPCX, skill: operational-kpi}
      - {ticker: RKLB, skill: unit-economics}
      - {ticker: SPCX, skill: peer-bench}
      - {ticker: FLY, skill: competitive}
      - {ticker: YSS, skill: ratio-analysis}

  - id: PIL-4
    priority: P4
    title: Neutron's medium-lift case closes arithmetically only above a stated payload bar, and it rests on F5b, not F5a
    conditional_from_the_start: true
    conditional_note: >
      ⚠️ CORRECTED 2026-09-18, in three ways. (1) The premise "the payload is a CLAIMED
      input" is STALE — Neutron's payload is now FILED at ~13,000 kg (reusable config;
      the expendable config still has no filed source, and Neutron HAS NOT FLOWN).
      (2) The price is now disclosed as an ASP of $50–55M. (3) Under P4 a MODELLED input
      still cannot carry a falsifier, so the pillar stays conditional — but on the
      ACTUAL inputs now, not on the stale ones.
    wrong_if:
      - metric: implied_neutron_price_per_kg_to_LEO_at_disclosed_ASP
        threshold: 5567                # the BAND's lower edge — the conservative scalar
        threshold_band: [5567, 7448]   # Falcon 9 matched-pair $/kg, 1.34x band
        source: RKLB_filing_and_published_vehicle_spec
        op: ">"
        basis_note: >
          ⚠️ THE OLD THRESHOLD (2,939) WAS DENOMINATOR-FAILED AND IS WITHDRAWN.
          001's Falcon 9 basis A is $2,939/kg @ 22.8 t — and "22.8" returns ZERO pages
          in the filing. On the matched-pair payload basis the figure is $5,567-7,448/kg
          (Q2 2025 $5,568 vs Q2 2026 $7,448; band 1.34x). A band, not a point.
        basis_collapse_carried: >
          ⚠️ AND THE OLD FALSIFIER COLLAPSED TWO BASES INSIDE ITS OWN DEFINITION: the
          ~3.1 t bar is $9.1M / $2,939/kg — an ELECTRON-class price over a NEUTRON
          denominator. On Neutron's own disclosed ASP the implied figure is
          $3,846-4,231/kg, which EXCEEDS 2,939 and FIRES; the equivalent bar is
          17.0-18.7 t, far above Neutron's filed ~13 t capacity. P4 may well FALSIFY,
          and 003 must carry that possibility rather than assume the case closes.
    independently_falsifiable:
      - a sourced payload that puts Neutron on the F5a architecture rather than F5b
      - an implied $/kg exceeding the Falcon 9 matched-pair band
    subscriptions:
      - {ticker: RKLB, skill: what-if}
      - {ticker: RKLB, skill: unit-economics}
      - {ticker: FLY, skill: competitive}
      - {ticker: RKLB, skill: peer-bench}
      - {ticker: SPCX, skill: unit-economics}
      - {ticker: FLY, skill: peer-bench}   # added 2026-09-19 — PIL-4's ONLY unique pair.
                                           # Without it PIL-4 ⊆ PIL-1, so it never filed
                                           # first and Phase 5 generated zero tasks.
                                           # Also closes an orphaned §3 matrix row.

  - id: PIL-5
    priority: P5
    title: RKLB's per-launch disclosure is a durable COST-side measurement and an unreconciled REVENUE-side normalisation; the asymmetry is the finding
    wrong_if:
      - metric: abs_pct_gap_between_disclosed_cost_per_launch_times_missions_and_audited_launch_segment_cost_of_revenue
        threshold: 0.05
        source: RKLB_10-Q_launch_services_segment_table
        op: ">"
    both_legs_recorded:
      - revenue_side_gap_pct: 22.5    # $9.1M x 6 = $54,600k vs segment revenue $44,586k
      - margin_side_gap_pp: 8.7       # disclosed revenue-per-launch implies 51.6% vs the audited table's 42.9%
      - interpretation: period_normalisation   # ⚠️ NOT "timing" — see the note below
    interpretation_note: >
      ⚠️ CORRECTED 2026-09-18: 003's original hypothesis ("the gap is a recognition-TIMING
      artefact") is FALSIFIED, and the falsification is clean. Q2 2025 is the ZERO-HASTE
      control period and the gap still diverges −15.3% (revenue) / −22.9% (cost). With no
      HASTE missions in the period, timing cannot be the mechanism. The gap is a property
      of the METRIC'S PERIOD-NORMALISATION, not of HASTE. And the 5% threshold is not
      discriminable on the metric's own noise: the cost-side gap exceeds 5% in 4 of 6
      periods (+0.4 / −22.9 / −12.8 / −8.6 / +3.6 / −3.5%).
      ⚠️ STABILITY TEST REQUIRED BEFORE QUOTING: the ×6 construction ($9.1M × 6 = $54,600k)
      must reproduce in EVERY period the multiplicand is observable, or it is QUARANTINED.
      A construction that closes at one period and fails at the next is a coincidence, not
      a mechanism.
    subscriptions:
      - {ticker: RKLB, skill: operational-kpi}
      - {ticker: RKLB, skill: recent-quarter}
      - {ticker: RKLB, skill: ratio-analysis}
      - {ticker: FLY, skill: competitive}
      - {ticker: SPCX, skill: recent-quarter}
      - {ticker: IRDM, skill: recent-quarter}
      - {ticker: GSAT, skill: recent-quarter}
      - {ticker: PL, skill: recent-quarter}
      - {ticker: YSS, skill: recent-quarter}
      - {ticker: LUNR, skill: recent-quarter}
      - {ticker: SATS, skill: recent-quarter}

  - id: PIL-6
    priority: P6
    title: The released value was captured at the launcher, not passed through to the customer, and the demand side does not price off the curve
    wrong_if:
      - metric: launch_cost_share_of_total_program_cost_at_universe_demand_side_names
        threshold: 0.10
        source: issuer_filing_capex_and_launch_price_disclosure
        op: ">"
        threshold_reachability: >
          ⚠️ THE THRESHOLD IS ABOVE THE DATUM AT THE ONE ISSUER THAT OWNS THE LARGEST
          LAUNCH BUSINESS. Launch Services is 8.29% of SPCX consolidated revenue — below
          the 0.10 bar. And 002's NVDA carry-forward says the launch-cost share at the
          demand side is EVEN SMALLER than 001 recorded (power+thermal is only
          $2.3-4.6M/MW against a reported $10-40M/MW all-in; the dominant term is compute
          hardware and its replacement rate). So P6's falsifier may be UNREACHABLE BY
          CONSTRUCTION at the demanding names, not merely unevaluated.
          IF THE QUANTITY IS NON-FORMABLE, RECORD NON-FORMABLE — NOT PASS. A band that
          cannot be drawn is not a band within ±50%; recording it as a pass on a technicality
          is the false clearance class 002 exists to prevent.
    independently_falsifiable:
      - a demonstrated fall in revenue per launch at least as large as the fall in cost per launch (pass-through occurred)
      - a launch share of programme cost above 10% at the demand-side names (the curve does bind them)
    partial_delivery: >
      The cost/price half is demonstrated and is delivered regardless. The programme-cost
      half rests on a modelled input and under P4 cannot carry the falsifier alone.
    subscriptions:
      - {ticker: RKLB, skill: operational-kpi}
      - {ticker: RKLB, skill: unit-economics}
      - {ticker: PL, skill: growth-strategy}
      - {ticker: YSS, skill: growth-strategy}
      - {ticker: LUNR, skill: growth-strategy}
      - {ticker: SATS, skill: growth-strategy}
      - {ticker: PL, skill: ratio-analysis}
      - {ticker: YSS, skill: ratio-analysis}
      - {ticker: PL, skill: sector-overview}
      - {ticker: YSS, skill: sector-overview}
      - {ticker: IRDM, skill: secular-trends}
      - {ticker: GSAT, skill: secular-trends}
      - {ticker: IRDM, skill: risk}
      - {ticker: GSAT, skill: risk}
      - {ticker: RKLB, skill: risk}

known-open:
  - question: >
      Falcon 9 basis B — the marginal-cost stack — has no filed anchor. 001 named the
      candidate: NASA CRS/Commercial Crew contract values as a revealed-price floor.
      Carried UNRESOLVABLE-FROM-PUBLIC-SOURCES with that resolving disclosure named,
      not UNRESOLVABLE-FROM-PLATFORM — the two remedies differ.
    owner: PIL-1
    blocking: false

  - question: >
      F5 is split THREE ways — F5a (fully reusable, propellant, hard), F5b (partially
      reusable, upper-stage manufacturing, soft), F5c (fully expendable, whole-vehicle
      manufacturing) — and the tiers are EXHAUSTIVE. CORRECTED 2026-09-18: an earlier
      version of this file recorded F5a/F5b as not reaching Electron and Alpha and
      registered that as an open amendment candidate. THAT WAS WRONG; F5c was added at
      v1.3.0, completing the split, and nothing is open. The constitution's own finding
      is an INVERSION, not a gap: the architectures whose floor is unproven (F5a/F5b —
      no DEMONSTRATED price on either) dominate the cost conversation, while F5c holds
      the only DEMONSTRATED price. Carried as a P3 finding, not an amendment.
    owner: PIL-1, PIL-3
    blocking: false

  - question: >
      BA (Spectrolab) is the second leg of the space-solar-cell duopoly and is OUTSIDE
      this universe — 007/008 own it. SolAero (RKLB) is the only leg inside. The map
      records the absence rather than substituting a proxy.
    owner: PIL-2
    blocking: false

  - question: >
      IRDM, GSAT and RKLB are P11 deal securities. Every figure drawn from them describes
      a standalone business contractually ceasing to exist, and must be tagged
      pre-merger basis. ⚠️ **BOTH ITEMS CORRECTED 2026-09-19, and both were wrong.**
      **SATS is NOT "asset-sale gain through operating_income"** — there is **no gain**. It is
      an **INVERTED IMPAIRMENT**: `impairments and other` of **$(66,159)K** sitting *inside*
      the cost block, which **reduces** total costs and expenses and **raises** operating
      income. Filed Q1 2026 operating income is $392,847K; excluding the credit it is
      **$459,006K — 16.8% apart**. **LUNR's "42.1% operating margin" is CLOSED, not a
      credulity question** — it is a **stripped loss of −42.1%** (DA-23), with the FY2025
      component identity closing on the negative.
    owner: PIL-2, PIL-5, PIL-6
    blocking: false

  - question: >
      ⚠️ CORRECTED 2026-09-18. Sector values for IRDM and GSAT were to follow the platform's
      assignment for SATS (tech.telecom_services). IRDM CONFIRMED; **GSAT is
      `tech.tech_hardware`, not telecom_services** — so a comparator set assembled by
      taxonomy node SILENTLY OMITS the P6-subscribed `GSAT × competitive` leg. **No source
      states a YSS sector value at all.** The universe is therefore pinned BY TICKER, not
      by node, and any phase deriving a peer set from a sector field must verify membership
      explicitly.
    owner: all
    blocking: false

  - question: >
      ⚠️ PL and GSAT carry NO DA census from 002 — no artifact folder exists for either,
      17% of analytical weight between them. GSAT appears in 002 only as a comparator inside
      the SATS competitive artifact; PL is also implicated in a `sec76` citation-ID collision
      (002 spec §1d asserts sec76 = PL's Q1 FY2026 10-Q, but sec76 resolves to LUNR's Q2 2026
      10-Q — one of the two is wrong, unresolved). 003 runs the census on both itself.
    owner: PIL-3, PIL-5, PIL-6
    blocking: false

budget:
  max_tasks: 115         # RAISED 80 -> 115 on 2026-09-19 by the owner's instruction, which is
                         # the sign-off the Deviation Register was waiting for. The generator
                         # measured 109 mode-tasks against the declared 80 — a 36% overrun, and
                         # the spec's own remedy ("drop the Light rows first") was tested and
                         # FAILED: dropping all 23 Light tasks still leaves 88 > 80. 115 covers
                         # 109 with headroom for the 2 hand-emitted synthesis tasks plus retries.
  max_retries_per_task: 2
  # This counts MODE-TASKS. The 45 distinct (ticker, skill) analyses decompose into
  # ~90 mode-tasks. Real unit of work is 45 analyses.

expiry_triggers:
  - earnings_release
  - constitution_bump
  - skill_version_mix

depends_on: []
informs: [004, 005, 006, 011]     # 003 publishes the citable curve and map these consume

macro_sensitivity: medium
# Carried as a P6 input, not an opinion: the curve is a cost series and largely
# price-independent, but the value-pool map is not — the demand side funds cadence from
# capital markets, and the long end sits at three-year highs with hike risk priced.

market_data_stage: none
# Every §3 row. This thesis produces no positions by design (spec §5), so Q42 does not
# bind and no bars schema is required. Scalar constitution constraints are N/A.

methodology:
  definitional_ambiguity: >
    Inherited standing rule. This sector's vocabulary is not standardised and most
    headline numbers are self-defined by the issuer reporting them. Definitions are
    DOCUMENTED AND REPORTED FROM ALL ANGLES, never collapsed. On this thesis the DA-01
    basis discipline is the load-bearing instance: the four bases span ~$500 to ~$6,600
    per kg — a 7-13x spread around ONE Falcon 9 mission — so a $/kg without its basis is
    not a weaker number, it is a different number. Every artifact labels which
    definition it quotes and the spread is itself a finding.
  unresolvable_disposition: >
    A pillar whose wrong_if cannot be evaluated for want of a disclosure is NOT dropped
    and NOT failed — it is recorded UNRESOLVABLE-FROM-PUBLIC-SOURCES or
    UNRESOLVABLE-FROM-PLATFORM, carried in known-open, and reported with the specific
    disclosure that would resolve it. The class matters: the two have different remedies.
  inherited_denominators: >
    This thesis consumes 001's physics (F1/F2/F5) and 002's denominators and NEVER
    re-derives them. Where 003 invalidates a 001 figure, 001's files are NOT rewritten —
    001 is frozen, and the correction is recorded here and cited by location, matching
    001's own annotate-don't-rewrite policy.
```

## Status log

| Date | Event |
|---|---|
| 2026-09-18 | Thesis created via `agentii.specify`. Six pillars. Constitution pinned at v1.2.0 at creation; **now 1.5.0**. |
| 2026-09-18 | `agentii.clarify` and `agentii.plan` run. `plan` is **not implemented in the kit** (`agentii_cmd.py` registers `{specify, clarify, tasks, constitution}` only), so `plan.md` was **authored by hand** against `plan-template.md`. |
| 2026-09-18 | **Restored to Wave 1** at post-002 review. Three reasons: (1) §5's annotation to 005 — *"launch pure-plays ARE the curve"* — is far stronger than "soft input"; 005 without 003 redoes 003's *raison d'être*, which is the duplication 002's brief existed to prevent. (2) The demotion's premise was falsified (`001:PIL-1` HOLDS; PIL-1 FIRED). (3) 002's completion freed a slot under `max_theses_active: 6`. Corroborating: 002's finding that `DEMONSTRATED` does not include *basis* — the two differ by **46.47 pp** on SPCX `operating_margin` — means 004 and 005 pricing off 001's register would consume a register whose labels were just shown unreliable and whose curve height was shown out of tolerance. |
