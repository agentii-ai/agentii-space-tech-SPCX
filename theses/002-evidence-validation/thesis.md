# Thesis: 002 — Evidence Validation & Model Hardening

Living file. `spec.md` is the frozen specification; this file is updated as findings
land. Machine-readable frontmatter below is authoritative for the dispatcher.

```yaml
thesis_id: 002-evidence-validation
constitution_pin: 1.4.0
created: 2026-09-18
as_of: 2026-09-18
status: active

claim: >
  001's headline conclusions rest on a narrower base of DEMONSTRATED inputs than their
  stated precision implies. Three payload denominators underpinning the sector's cost
  conclusions are CLAIMED rather than filed; the constitution's named binding constraint
  for orbital compute (F2) rests on an admitted placeholder and an unclosed heat-pump
  loop; and the platform's XBRL extraction carries a measured defect (DA-23) whose
  remedy has been applied to 12 issuer-quarters rather than the universe. Validating
  these inputs will either confirm 001's conclusions within a quantified band or
  restate them — and the answer determines how much precision any downstream thesis is
  entitled to.

pillars:
  - id: PIL-1
    priority: P1
    title: The three CLAIMED denominators resolve and the $/kg conclusions hold within ±15%
    minimum_defensible_view: true
    wrong_if:
      - metric: abs_pct_change_in_demonstrated_price_per_kg_to_LEO_after_denominator_validation
        threshold: 0.15
        source: government_launch_manifest_or_issuer_filing
        op: ">"
    denominators_under_test:
      - {vehicle: Electron, claimed_kg: 300, carries: DA-01 basis A and basis B}
      - {vehicle: Falcon 9, claimed_t: 22.8, carries: DA-01 basis A, A-prime, B, C}
      - {vehicle: Starship, claimed_t: 100, carries: F5a propellant floor}
    subscriptions:
      - {ticker: RKLB, skill: unit-economics}
      - {ticker: RKLB, skill: operational-kpi}
      - {ticker: SPCX, skill: unit-economics}
      - {ticker: SPCX, skill: operational-kpi}
      - {ticker: FLY, skill: unit-economics}

  - id: PIL-2
    priority: P2
    title: F2's unsourced constants are replaced or bracketed and radiator mass per MW is bounded
    wrong_if:
      - metric: f2_radiator_mass_per_MW_uncertainty_band_pct
        threshold: 0.50
        source: peer_reviewed_literature_or_flown_hardware_disclosure
        op: ">"
    unsourced_inputs:
      - radiator_areal_density: "8 kg/m2 — admitted placeholder in _cross/phase-2"
      - heat_pump_COP: "not applied; F2 table is rejection-side only"
    subscriptions:
      - {ticker: BWXT, skill: secular-trends}
      - {ticker: GOOG, skill: secular-trends}
      - {ticker: NVDA, skill: secular-trends}
      - {ticker: VRT, skill: unit-economics}
      - {ticker: MRCY, skill: secular-trends}

  - id: PIL-3
    priority: P3
    title: The six-defect Data-Integrity Register is applied universe-wide and its open candidates resolve
    scope_corrected: >
      Raised from "DA-23 sign stripping" to the whole register during specification. The
      sweep that extended DA-23's census found five more defects in the same
      period-and-sign extraction layer, and established that they COMPOUND.
    wrong_if:
      - metric: count_of_universe_issuer_quarters_with_unresolved_defect_status
        threshold: 0
        source: data_integrity_register_application
        op: ">"
    register:
      - {defect: DA-23, coverage: "6 of 6 loss-making stripped; 19 of 19 profitable clean", detectors: 3}
      - {defect: DA-24, coverage: "SATS", independence: "contaminated but NOT stripped"}
      - {defect: DA-25, coverage: "RKLB", note: "51.6% implied vs 42.9% audited GM"}
      - {defect: DA-26, coverage: "19 of 19 issuers — universal", trap: "mislabelled period VARIES by issuer; cannot be screened by row position"}
      - {defect: DA-27, coverage: "n = 4 of 4", trap: "wrong LABEL on internally-consistent values; compounds with DA-26"}
      - {defect: DA-28, coverage: "HAWK", trap: "listing-date guard required or EPS screen false-positives"}
    coverage_hole: "OperatingIncomeLoss absent or segment-only at MRK, BMY, WWD — no detector can run; record UNRESOLVABLE-FROM-PLATFORM, never a passed check"
    open_candidates: [BA_2025Q3, LUNR, VOYG]
    sub_mechanism: "VOYG is not a sign inversion but an unreconcilable LEVEL — $51.408M operating against $4.457M gross profit, failing the gross-profit bound by $46,951M across three consecutive quarters"
    discarded_test: "EPS x shares — passes on BOTH sides of a flip at RKLB, FLY and VOYG; inadmissible"
    remedy: "validate_calculation / get_calculation_tree — automated component identity; gross-profit bound as fallback"
    subscriptions:
      - {ticker: YSS, skill: recent-quarter}
      - {ticker: SPCX, skill: recent-quarter}
      - {ticker: RKLB, skill: recent-quarter}
      - {ticker: FLY, skill: recent-quarter}
      - {ticker: IRDM, skill: recent-quarter}
      - {ticker: VRT, skill: recent-quarter}
      - {ticker: GOOG, skill: recent-quarter}
      - {ticker: MSFT, skill: recent-quarter}
      - {ticker: NVDA, skill: recent-quarter}
      - {ticker: BWXT, skill: recent-quarter}
      - {ticker: MRCY, skill: recent-quarter}
      - {ticker: UTHR, skill: recent-quarter}
      - {ticker: SATS, skill: recent-quarter}
      - {ticker: VOYG, skill: recent-quarter}
      - {ticker: LUNR, skill: recent-quarter}
      - {ticker: HAWK, skill: recent-quarter}
      - {ticker: BA, skill: recent-quarter}

  - id: PIL-4
    priority: P4
    title: SPCX's 1.4 GW nameplate restates to a facility draw and the restatement is computable
    wrong_if:
      - metric: spcx_facility_pue_ratio
        threshold: 1.5
        source: issuer_disclosure_or_industry_PUE_benchmark
        op: ">"
    registers: [DA-11]
    subscriptions:
      - {ticker: SPCX, skill: operational-kpi}
      - {ticker: SPCX, skill: business-model}
      - {ticker: VRT, skill: unit-economics}
      - {ticker: MSFT, skill: recent-quarter}

  - id: PIL-5
    priority: P5
    title: At least half of 001's headline figures convert from CLAIMED/MODELED to DEMONSTRATED
    wrong_if:
      - metric: share_of_001_headline_figures_converted_to_DEMONSTRATED
        threshold: 0.5
        source: validation_ledger
        op: "<"
    subscriptions:
      - {ticker: SPCX, skill: ratio-analysis}
      - {ticker: RKLB, skill: ratio-analysis}
      - {ticker: VRT, skill: ratio-analysis}
      - {ticker: GOOG, skill: ratio-analysis}

  - id: PIL-6
    priority: P6
    title: Every 001 falsifier is classified as evaluable, platform-blocked, or source-blocked
    wrong_if:
      - metric: count_of_001_falsifiers_unclassified_or_without_named_resolving_source
        threshold: 0
        source: validation_ledger
        op: ">"
    falsifiers_under_classification: [PIL-1, PIL-2, PIL-3, PIL-4, PIL-5, PIL-6]
    structurally_unreachable:
      - {pillar: PIL-4, class: UNRESOLVABLE-FROM-PUBLIC-SOURCES}
      - {pillar: PIL-6, class: UNRESOLVABLE-FROM-PLATFORM}
    subscriptions:
      - {ticker: SATS, skill: risk}
      - {ticker: IRDM, skill: competitive}
      - {ticker: UTHR, skill: unit-economics}
      - {ticker: YSS, skill: operational-kpi}

budget:
  max_tasks: 70          # raised 40 → 70 at specification review: the universe grew from
                         # 12 to 17 names when the register expanded to six defects, and
                         # 16 names × 10 matrix rows expand to ~65 mode-tasks.
                         # If it must come down: cut ratio-analysis and business-model
                         # first. NEVER the recent-quarter row — it is the delivery
                         # mechanism for PIL-3 in its entirety.
  max_retries_per_task: 2

expiry_triggers:
  - earnings_release
  - constitution_bump
  - skill_version_mix
  - issuer_discloses_payload_mass_or_compute_per_satellite

depends_on:
  - thesis_id: 001-technology-baseline
    claims:
      - demonstrable_price_per_kg_to_LEO_above_1000_threshold
      - F5_split_fully_vs_partially_reusable
      - A1b_falsification
      - DA-23_census_12_issuer_quarters
      - F1_array_ceiling_5000_to_5600_m2_per_MW

macro_sensitivity: low

methodology:
  validation_instruments:
    - XBRL calculation-arc cross-validation (validate_calculation, get_calculation_tree)
    - Definitional re-basing across all DA-01 cost bases
    - CLAIMED-to-source substitution with explicit failure classification
    - Page-level citation retrieval (the instrument that makes the other three auditable)
  citation_policy:            # added at clarify round 3, 2026-09-18 (spec §1d)
    binding: true
    canonical_form: "[📄 {ticker} {form_type} p.{N}](https://agentii.ai/v/{ticker}/{citation_id}/{N})"
    ticker_required: true
    ticker_note: >
      The round-3 instruction asked for agentii.ai/v/{citation_id}/{page_no}. The ticker
      is NOT optional: the portal redirects to
      api.agentii.ai/v1/view_document/{ticker}/{citation_id}?page_no=page{N} and resolves
      via pipeline.src_documents JOIN pipeline.sec_filings, which cannot join without it.
      Six independent plugin contracts include the ticker; none omits it. The short form
      would have produced broken links in every artifact. Implemented canonical and
      flagged for override — a one-line change if a ticker-less route exists.
    applies_to: [DEMONSTRATED figures, Data-Integrity Register findings, falsifier observations]
    exempt: [MODELED derivations (cite inputs), restatements of 001 (cite the 001 artifact)]
    failure_mode: "uncited DEMONSTRATED figure FAILS the contract — no warning tier"
    verified_at_specification: >
      read_source_pages(SPCX, sec8, page43) confirmed 4 of 4 inherited Connectivity
      figures from the primary source, upgrading them from DEMONSTRATED (per 001) to
      DEMONSTRATED (read-verified at source). It also resolved DA-10 in favour of
      mix-shift — the filing attributes the 22.4% ARPU decline to international expansion
      and lower-priced service plans, not price erosion.
  evidence_discipline: >
    Per P4 and the v1.3.0 Data-Integrity Register, any artifact reading operating_income
    shows the component derivation (gross profit - opex) in-line. EPS x shares is NOT a
    valid sign test and its use is a defect.
  correction_policy: >
    001's files are FROZEN. Where this thesis invalidates a 001 figure, the correction is
    recorded here and cross-cited by location rather than rewritten in place. This
    preserves the audit trail that makes 001's own in-place corrections legible.
```

## Status log

| Date | Event |
|---|---|
| 2026-09-18 | Thesis created via `agentii.specify` — IDs for the whole program (002–011) allocated in one mkdir-as-CAS pass so nothing drifts. Constitution pinned at **v1.3.0**, which was amended *before* specification so this thesis would not be born `stale`. Spec frozen with six pillars. |
| 2026-09-18 | **`agentii.clarify` round 3 — invoked on this thesis, and this round's requirement IS this thesis's**, unlike rounds 1–2 (which resolved to 011). Instruction: *"在thesis 002 的validation，必须给重要数据和facts的引用增加 citation url"* — every material figure and fact must carry a source-page citation. **Implemented as spec §1d + a `citations` block in the artifact contract** (three new level-`fail` validation rules). **⚠️ One deliberate divergence from the instruction as written: the requested form `agentii.ai/v/{citation_id}/{page_no}` omits the ticker and does not resolve** — the portal redirects to `api.agentii.ai/v1/view_document/{ticker}/{citation_id}?page_no=page{N}` and joins `src_documents` to `sec_filings`, which cannot be done without it. Six plugin contracts include the ticker; none omits it. Implemented the **canonical** form and flagged it for override. **The requirement was executed once rather than only specified**: `read_source_pages(SPCX, sec8, page43)` returned the Connectivity table and **confirmed 4 of 4 inherited figures at source**, upgrading them to `DEMONSTRATED (read-verified)` — and incidentally **resolved DA-10 in favour of mix-shift**, since the filing attributes the 22.4% ARPU decline to international expansion and lower-priced plans. **A structural finding also surfaced: every SPCX figure in the workspace resolves to `sec8`, the Q2 2026 10-Q — SPCX has exactly one.** The anchor's entire evidence base, including the A1b falsification, traces to a single filing. |
| 2026-09-18 | **`agentii.clarify` round 1 — invoked on this thesis.** Scanner reported **0 mechanical candidates**: no prose `wrong_if`, every universe row carries a rationale, budget and `expiry_triggers` present, all subscription tokens well-formed, pins and pillar priorities present. The single question raised was an **intent** ambiguity the deterministic scan cannot see: *"can we form a main-line investment logic for space tech in thesis 002 — a big logic running through all the segments, or several strategies?"* **Answer: yes, the main line is formable from 001 alone — but it does not belong here.** This thesis is chartered validation-only (*"produces no trade ideas, sizes no positions"*), and a governing investment argument is a synthesis output. **Disposition: 002 gains no pillar.** The main line was written into `theses/PROGRAM.md` §0b as the program's governing argument and became **011's P1**, with 011's dependency split so P1–P6 start immediately from 001 while sizing keeps the 004–010 gate. The full record lives in `theses/011-idea-generation/spec.md` §Clarifications, because that is where the main line now resides. |

## Constitution amendment candidates (NOT executed — require human approval)

| # | Candidate | Trigger | Status |
|---|---|---|---|
| — | None. The v1.3.0 amendment absorbed the six candidates 001 had proposed (A1a/A1b, F5a/F5b, DA-23/24/25, `UNRESOLVABLE-FROM-PLATFORM`). Any candidate this thesis raises routes through the same gate. | — | — |

## Known open

- **Q-1 (PIL-1)**: Is a company-published payload capacity admissible as independent
  adjudication? Provisional answer: **no** — a company figure is the same evidence class
  as the original claim. Only a government manifest, a filed document or a customer
  contract counts. Flagged for `agentii.clarify`.
- **Q-2 (PIL-2)**: If reaching 500 K requires a heat pump, does F2 report the 313 m²/MW
  figure with the COP penalty folded in, both side by side, or a statement that no
  flight-qualified heat pump exists at that scale? Provisional: **both**, per the §1c
  standing rule, with the nuclear dependency stated.
- **Q-3 (PIL-3)**: If YSS's $110.466M figure is a genuine one-off rather than an
  extraction defect, does it belong in the Data-Integrity Register at all? Open.
- **Q-4 (methodology)**: Does the frozen-001 policy hold absolutely, or should 001's
  artifacts be annotated in place when this thesis invalidates a figure? Provisional:
  **frozen**, with cross-cited corrections — consistent with 001's own
  annotate-don't-rewrite handling of its uncounted census figures.
- **Q-5 (PIL-5)**: The 50% conversion threshold was set as the point at which a register
  stops being majority-untestable — reasoned, not measured. Flagged for human
  confirmation; a different answer is a PATCH to spec, not a MAJOR event.

## Notes for downstream theses (003–011)

This thesis exists so that 003–011 can **cite rather than re-derive**. When its
validation ledger is published at `_cross/validation-ledger.md`, downstream specs should
replace any inherited `CLAIMED` figure with the ledger's validated value **and its band**.
A downstream thesis that quotes a point estimate where the ledger supplies a band is
overstating precision — the exact failure this thesis was created to prevent.
