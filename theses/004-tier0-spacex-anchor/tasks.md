# Research Tasks: 004-tier0-spacex-anchor

> **APPEND-ONLY (Q26)**: never rewritten, renumbered, reordered or deleted
> from. `[x]` is written by `agentii.implement` and is a display hint —
> `agentii.converge` evaluates artifact state, not `[x]`. Corrections arrive as
> appended `## Phase N: Convergence` sections.

Task format: `- [ ] T### [P] [pillar] TICKER × SKILL × MODE — purpose (src: …)`

- **Brackets are re-attributed from `(ticker, skill)`** — the platform keys by
  skill only, so ~60% arrive wrong. See `plan.md`.
- **Phase = the FIRST pillar in the bracket.** Multi-pillar tasks serve every
  pillar listed; phase is a filing heuristic, not a scope limit.
- **A task's phase does not bound its scope.** A `[PIL-1/PIL-4/PIL-6]` task
  filed under Phase 1 does Phase 4 work too.

**Generated** 2026-09-19 · **37 tasks** · phase map PIL-1:7 · PIL-2:3 · PIL-3:4 · PIL-4:5 · PIL-5:6 · PIL-6:7
· re-attributed **0** brackets

| Phase | Filed here | **True load** |
|:---:|---:|---:|
| 3 | 5 | **5** |
| 4 | 12 | **17** **← +5 more** |
| 5 | 9 | **14** **← +5 more** |
| 6 | 6 | **9** **← +3 more** |
| 7 | 5 | **7** **← +2 more** |
| **Total** | **37** | **52** |

> **Filed-here counts UNDERSTATE the work whenever a pillar's tasks are
> carried by pairs whose first pillar is something else.** A task bracketed
> `[PIL-1/PIL-4/PIL-6]` is *filed* under Phase 1 but *serves* Phases 1, 4 and 4.
> **Plan the schedule off True load, not Filed here.** On 002 the gap reaches
> 8× — Phase 4 files 3 tasks while carrying 23 — because the entity-boundary
> pillar is entirely fed by SPCX pairs that name PIL-1 first.

---

## Phase 3

- [ ] T007 [P] [PIL-2/PIL-3/PIL-4] SPCX × revenue-decomp × triggers — **Added at round 3 — this is where the depth lives. RESCOPED at round 4.** The cut *inside* each segment, **derived from the filings' own decomposition rather than a pre-declared taxonomy** — the 10-Q/8-K narrative disclosure **and** the XBRL dimensional axes (**P2**, **P3**, **P4**). See the box below · mode: the trigger set — what would overturn this conclusion (src: spec-revenue-decomp)
- [ ] T008 [PIL-2/PIL-3/PIL-4] SPCX × revenue-decomp × defaults — **Added at round 3 — this is where the depth lives. RESCOPED at round 4.** The cut *inside* each segment, **derived from the filings' own decomposition rather than a pre-declared taxonomy** — the 10-Q/8-K narrative disclosure **and** the XBRL dimensional axes (**P2**, **P3**, **P4**). See the box below · mode: the default assumptions used where no filed figure exists (src: spec-revenue-decomp)
- [ ] T009 [PIL-2/PIL-3/PIL-4] SPCX × revenue-decomp × methodology — **Added at round 3 — this is where the depth lives. RESCOPED at round 4.** The cut *inside* each segment, **derived from the filings' own decomposition rather than a pre-declared taxonomy** — the 10-Q/8-K narrative disclosure **and** the XBRL dimensional axes (**P2**, **P3**, **P4**). See the box below · mode: the derivation path, stated so the number is reproducible (src: spec-revenue-decomp)
- [ ] T010 [PIL-2/PIL-3/PIL-4] SPCX × revenue-decomp × retrieval-scope — **Added at round 3 — this is where the depth lives. RESCOPED at round 4.** The cut *inside* each segment, **derived from the filings' own decomposition rather than a pre-declared taxonomy** — the 10-Q/8-K narrative disclosure **and** the XBRL dimensional axes (**P2**, **P3**, **P4**). See the box below · mode: which sources are admitted and which are excluded (src: spec-revenue-decomp)
- [ ] T011 [PIL-2/PIL-3/PIL-4] SPCX × revenue-decomp × retrieval-strategy — **Added at round 3 — this is where the depth lives. RESCOPED at round 4.** The cut *inside* each segment, **derived from the filings' own decomposition rather than a pre-declared taxonomy** — the 10-Q/8-K narrative disclosure **and** the XBRL dimensional axes (**P2**, **P3**, **P4**). See the box below · mode: how the sources were located, so the search repeats (src: spec-revenue-decomp)

## Phase 4

- [ ] T006 [P] [PIL-3/PIL-6] SPCX × reverse-dcf × methodology — **Added at round 3.** Solves for the growth rate the live price implies — the price question asked backwards. A cross-check on the three regimes, and the market-implied limb of **P3**'s AI framing · mode: the derivation path, stated so the number is reproducible (src: spec-reverse-dcf)
- [ ] T012 [P] [PIL-3/PIL-6] SPCX × comps × retrieval-scope — **Cross-check only**, per the constitution — and now **priced live**: demonstrates which peer sets remain inadmissible (loss-making, `P11`, `PARTIAL`) even with a quote in hand (**P6**). **The AI framing set (MSFT, GOOG, NVDA, VRT) is carried here**, so those four read-through names are not orphaned universe rows · mode: which sources are admitted and which are excluded (src: spec-comps)
- [ ] T013 [P] [PIL-3/PIL-6] RKLB × comps × retrieval-scope — **Cross-check only**, per the constitution — and now **priced live**: demonstrates which peer sets remain inadmissible (loss-making, `P11`, `PARTIAL`) even with a quote in hand (**P6**). **The AI framing set (MSFT, GOOG, NVDA, VRT) is carried here**, so those four read-through names are not orphaned universe rows · mode: which sources are admitted and which are excluded (src: spec-comps)
- [ ] T014 [P] [PIL-3/PIL-6] FLY × comps × retrieval-scope — **Cross-check only**, per the constitution — and now **priced live**: demonstrates which peer sets remain inadmissible (loss-making, `P11`, `PARTIAL`) even with a quote in hand (**P6**). **The AI framing set (MSFT, GOOG, NVDA, VRT) is carried here**, so those four read-through names are not orphaned universe rows · mode: which sources are admitted and which are excluded (src: spec-comps)
- [ ] T015 [P] [PIL-3/PIL-6] GSAT × comps × retrieval-scope — **Cross-check only**, per the constitution — and now **priced live**: demonstrates which peer sets remain inadmissible (loss-making, `P11`, `PARTIAL`) even with a quote in hand (**P6**). **The AI framing set (MSFT, GOOG, NVDA, VRT) is carried here**, so those four read-through names are not orphaned universe rows · mode: which sources are admitted and which are excluded (src: spec-comps)
- [ ] T016 [P] [PIL-3/PIL-6] IRDM × comps × retrieval-scope — **Cross-check only**, per the constitution — and now **priced live**: demonstrates which peer sets remain inadmissible (loss-making, `P11`, `PARTIAL`) even with a quote in hand (**P6**). **The AI framing set (MSFT, GOOG, NVDA, VRT) is carried here**, so those four read-through names are not orphaned universe rows · mode: which sources are admitted and which are excluded (src: spec-comps)
- [ ] T017 [P] [PIL-3/PIL-6] ASTS × comps × retrieval-scope — **Cross-check only**, per the constitution — and now **priced live**: demonstrates which peer sets remain inadmissible (loss-making, `P11`, `PARTIAL`) even with a quote in hand (**P6**). **The AI framing set (MSFT, GOOG, NVDA, VRT) is carried here**, so those four read-through names are not orphaned universe rows · mode: which sources are admitted and which are excluded (src: spec-comps)
- [ ] T018 [P] [PIL-3/PIL-6] VSAT × comps × retrieval-scope — **Cross-check only**, per the constitution — and now **priced live**: demonstrates which peer sets remain inadmissible (loss-making, `P11`, `PARTIAL`) even with a quote in hand (**P6**). **The AI framing set (MSFT, GOOG, NVDA, VRT) is carried here**, so those four read-through names are not orphaned universe rows · mode: which sources are admitted and which are excluded (src: spec-comps)
- [ ] T019 [P] [PIL-3/PIL-6] MSFT × comps × retrieval-scope — **Cross-check only**, per the constitution — and now **priced live**: demonstrates which peer sets remain inadmissible (loss-making, `P11`, `PARTIAL`) even with a quote in hand (**P6**). **The AI framing set (MSFT, GOOG, NVDA, VRT) is carried here**, so those four read-through names are not orphaned universe rows · mode: which sources are admitted and which are excluded (src: spec-comps)
- [ ] T020 [P] [PIL-3/PIL-6] GOOG × comps × retrieval-scope — **Cross-check only**, per the constitution — and now **priced live**: demonstrates which peer sets remain inadmissible (loss-making, `P11`, `PARTIAL`) even with a quote in hand (**P6**). **The AI framing set (MSFT, GOOG, NVDA, VRT) is carried here**, so those four read-through names are not orphaned universe rows · mode: which sources are admitted and which are excluded (src: spec-comps)
- [ ] T021 [P] [PIL-3/PIL-6] NVDA × comps × retrieval-scope — **Cross-check only**, per the constitution — and now **priced live**: demonstrates which peer sets remain inadmissible (loss-making, `P11`, `PARTIAL`) even with a quote in hand (**P6**). **The AI framing set (MSFT, GOOG, NVDA, VRT) is carried here**, so those four read-through names are not orphaned universe rows · mode: which sources are admitted and which are excluded (src: spec-comps)
- [ ] T022 [P] [PIL-3/PIL-6] VRT × comps × retrieval-scope — **Cross-check only**, per the constitution — and now **priced live**: demonstrates which peer sets remain inadmissible (loss-making, `P11`, `PARTIAL`) even with a quote in hand (**P6**). **The AI framing set (MSFT, GOOG, NVDA, VRT) is carried here**, so those four read-through names are not orphaned universe rows · mode: which sources are admitted and which are excluded (src: spec-comps)

## Phase 5

- [ ] T023 [P] [PIL-4/PIL-5] SPCX × competitive × direct-competitor-identification-and-analysis — Launch competitive position behind the Space standalone-value test (**P4**); the capital-intensity comparison behind **P5** (src: spec-competitive)
- [ ] T024 [PIL-4/PIL-5] SPCX × competitive × market-share-dynamics-analysis — Launch competitive position behind the Space standalone-value test (**P4**); the capital-intensity comparison behind **P5** (src: spec-competitive)
- [ ] T025 [PIL-4/PIL-5] SPCX × competitive × market-share-evolution-and-competitive-benchmarking — Launch competitive position behind the Space standalone-value test (**P4**); the capital-intensity comparison behind **P5** (src: spec-competitive)
- [ ] T026 [P] [PIL-4/PIL-5] RKLB × competitive × direct-competitor-identification-and-analysis — Launch competitive position behind the Space standalone-value test (**P4**); the capital-intensity comparison behind **P5** (src: spec-competitive)
- [ ] T027 [PIL-4/PIL-5] RKLB × competitive × market-share-dynamics-analysis — Launch competitive position behind the Space standalone-value test (**P4**); the capital-intensity comparison behind **P5** (src: spec-competitive)
- [ ] T028 [PIL-4/PIL-5] RKLB × competitive × market-share-evolution-and-competitive-benchmarking — Launch competitive position behind the Space standalone-value test (**P4**); the capital-intensity comparison behind **P5** (src: spec-competitive)
- [ ] T029 [P] [PIL-4/PIL-5] FLY × competitive × direct-competitor-identification-and-analysis — Launch competitive position behind the Space standalone-value test (**P4**); the capital-intensity comparison behind **P5** (src: spec-competitive)
- [ ] T030 [PIL-4/PIL-5] FLY × competitive × market-share-dynamics-analysis — Launch competitive position behind the Space standalone-value test (**P4**); the capital-intensity comparison behind **P5** (src: spec-competitive)
- [ ] T031 [PIL-4/PIL-5] FLY × competitive × market-share-evolution-and-competitive-benchmarking — Launch competitive position behind the Space standalone-value test (**P4**); the capital-intensity comparison behind **P5** (src: spec-competitive)

## Phase 6

- [ ] T032 [P] [PIL-5] SPCX × risk × general-risk-factors-identification-assessment — The funding-structure and dilution analysis (**P5**); **P11** treatment of Cursor (**V-5**); the beta / cost-of-equity input to the scenario weights (src: PIL-5)
- [ ] T033 [PIL-5] SPCX × risk × technology-disruption-risk-analysis — The funding-structure and dilution analysis (**P5**); **P11** treatment of Cursor (**V-5**); the beta / cost-of-equity input to the scenario weights (src: PIL-5)
- [ ] T034 [PIL-5] SPCX × risk × regulatory-compliance-risk-assessment — The funding-structure and dilution analysis (**P5**); **P11** treatment of Cursor (**V-5**); the beta / cost-of-equity input to the scenario weights (src: PIL-5)
- [ ] T035 [P] [PIL-5] SPCX × growth-strategy × growth-strategy-assessment — Capital-allocation narrative against the capex disclosure — data centers named before launch facilities (**P5**) (src: PIL-5)
- [ ] T036 [PIL-5] SPCX × growth-strategy × organic-growth-drivers-analysis — Capital-allocation narrative against the capex disclosure — data centers named before launch facilities (**P5**) (src: PIL-5)
- [ ] T037 [PIL-5] SPCX × growth-strategy × organic-growth-driver-execution-assessment — Capital-allocation narrative against the capex disclosure — data centers named before launch facilities (**P5**) (src: PIL-5)

## Phase 7

- [ ] T001 [P] [PIL-1] SPCX × sotp-valuation × preflight — **The constitution-mandated primary instrument.** Three regimes, scenario weights, the discount/premium measure against **both** the live quote and the dated print (**P1**, **P6**) (src: PIL-1)
- [ ] T002 [PIL-1] SPCX × sotp-valuation × triggers — **The constitution-mandated primary instrument.** Three regimes, scenario weights, the discount/premium measure against **both** the live quote and the dated print (**P1**, **P6**) · mode: the trigger set — what would overturn this conclusion (src: PIL-1)
- [ ] T003 [PIL-1] SPCX × sotp-valuation × defaults — **The constitution-mandated primary instrument.** Three regimes, scenario weights, the discount/premium measure against **both** the live quote and the dated print (**P1**, **P6**) · mode: the default assumptions used where no filed figure exists (src: PIL-1)
- [ ] T004 [PIL-1] SPCX × sotp-valuation × methodology — **The constitution-mandated primary instrument.** Three regimes, scenario weights, the discount/premium measure against **both** the live quote and the dated print (**P1**, **P6**) · mode: the derivation path, stated so the number is reproducible (src: PIL-1)
- [ ] T005 [PIL-1] SPCX × sotp-valuation × retrieval-scope — **The constitution-mandated primary instrument.** Three regimes, scenario weights, the discount/premium measure against **both** the live quote and the dated print (**P1**, **P6**) · mode: which sources are admitted and which are excluded (src: PIL-1)

## Phase 8 — Cross-cutting

> ⚠️ **Hand-emitted by `tools/tasks_md.py`.** The platform generator emits only
> `ticker × skill × mode` rows and has **no concept of a cross-cutting task** —
> 001 documented this gap and hand-added its synthesis task every time. These are
> parsed from the spec's Output Contract. **Never `[P]`** (skill contract): a
> `_cross/` artifact depends on every prior phase.

- [ ] T900 [cross] cross × synthesis × default — publish `_cross/anchor-sotp.md` 🔴 **PRIMARY ARTIFACT**  ⚠️ hand-emitted; not `[P]` (src: spec-§6 Output Contract)
- [ ] T901 [cross] cross × synthesis × default — publish `_cross/segment-attribution-ledger.md` 🔴 **PRIMARY ARTIFACT**  ⚠️ hand-emitted; not `[P]` (src: spec-§6 Output Contract)

<!-- agentii.converge appends below this point; never edit above it -->

