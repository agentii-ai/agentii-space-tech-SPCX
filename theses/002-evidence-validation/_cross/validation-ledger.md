---
thesis_id: "002-evidence-validation"
artifact: validation-ledger
pillar: [cross]
ticker: cross
skill: synthesis
mode: default
task: T900
generated_at: 2026-09-18T18:40:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "none"
as_of: "2026-09-18"
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
schema: validation_ledger
evidence_grade: DERIVED
unresolvable: false
definitions_used:
  - da_id: DA-23
    chosen_reading: >
      Sign stripping — a served magnitude carrying the filed sign discarded — and the
      census reading is the one the constitution now carries after Phase 3: `Clean` means
      SUBTOTAL-LEVEL ONLY, the test has POWER only on BIDIRECTIONAL concepts, and a
      clearance is admissible only if it EXHIBITS a filed-negative instance that survived.
      This ledger therefore reports UNEVIDENT (NVDA, zero negatives — the test can neither
      pass nor fail) and UNEXERCISED (VRT on the income statement, 61 of 61 facts positive,
      13 of 13 identities closing vacuously) as distinct from CLEAN. A test that cannot
      fail is not a passing test, and a census scoped to subtotals cannot see a component.
  - da_id: DA-24
    chosen_reading: >
      Non-operating contamination of the operating line, in EITHER direction — the
      definition names a gain AND a charge, and the mechanism is COMPOSITION, not sign.
      Carried with the Phase 3 correction: the entry's DEFINING INSTANCE was named for a
      gain and the thing it is named after is a LOSS (SATS 2025 Q3 is a non-cash 5G
      impairment CHARGE of $16,481,468 thousand, 4.605x revenue, with the licences still on
      the balance sheet at 2026-03-31), and its independence proof is WITHDRAWN.
  - da_id: DA-25
    chosen_reading: >
      An issuer-defined per-unit figure may be a NORMALISATION, not a derivation, and may
      not be reproducible from the audited segment tables. Read here as three separable
      failure shapes: the metric is filed but not reproducible (SPCX ARPU, YSS per-unit);
      the datum CLASS is not ingested at all (IRDM billable subscribers — a zero from a
      structured query on MD&A prose is a zero BY CONSTRUCTION); and the normalisation is
      an end-of-period balance substituted for a period average (VRT roa/roe at the ratio
      layer). The remedy is unchanged: report the issuer metric and the segment-table
      derivation side by side, and let the segment table govern any margin claim.
  - da_id: DA-26
    chosen_reading: >
      An annual-basis fact served where a quarterly label is asserted. Universality is
      FALSIFIED at this phase: FLY shows zero instances on either surface, so the register's
      "19 of 19" is withdrawn and the count moves to 20 issuers tested with one exception.
      Read also as the general DURATION COLLISION — SPCX supplies a six-month period served
      against a three-month label at the INSTRUMENT rather than the issuer level.
  - da_id: DA-27
    chosen_reading: >
      Fiscal-period labels derived from the CALENDAR quarter rather than the issuer's fiscal
      calendar, with the A4 source discriminator: a defect sourced from a POPULATED but
      incorrect registry field is a different defect from one synthesised from a default.
      December-year-end issuers are EXCLUDED FROM THE DENOMINATOR under the
      mechanism-population identity — the sample is defined by the mechanism's own property
      and carries no information about the remainder — so "not testable" here is NOT clean.
  - da_id: DA-28
    chosen_reading: >
      Capital-structure discontinuity around a listing event invalidating share-count-based
      detectors. Read as the A3 generalisation: any present multi-class structure with
      non-identical per-share economics, any funding event straddling a close, or any
      share-count regime change inside the comparison window. HAWK's registered mechanism
      is WRONG (a numerator-concept mismatch, not a denominator straddle) — the site is
      confirmed and the mechanism is replaced.
  - da_id: DA-29
    chosen_reading: >
      Back-solved and opaque checks. The mechanical test is run on the TERMS, not the
      closure: if any term in a reconciliation appears NOWHERE in the source, the check is a
      BACK-SOLVE, and a back-solve closes exactly so it cannot be caught on the closure.
      Carried with the four demonstrated failure modes of `validate_calculation`: `pass` on
      a wrong-signed value; `pass` when BOTH sides were stripped; ZERO ROWS on a filed
      concept; and a 93% false-positive rate when it fails. A pass is not evidence about
      sign or contamination. `computed` may not be cited as a derivation, and `reported` is
      not definitionally the filed value; neither wins by default.
  - da_id: DA-30
    chosen_reading: >
      Two bases on one concept, collapsed without a basis field. Applied here as the rule
      this ledger must obey on itself: every figure carries its issuer AND its basis in-line,
      and no percentage is presented whose DENOMINATOR has not been named. The register
      names four live instances at SPCX (the $/kg block spans 12.8x across three defensible
      denominators) and a fifth at SATS' segment-level impairment presentation.
falsifiers_under_classification:
  "001:PIL-1":
    wrong_if: "abs_pct_change_in_demonstrated_price_per_kg_to_LEO_after_denominator_validation > 0.15"
    class: EVALUABLE
    outcome: FIRED
    resolving_source: "issuer filings — on-platform (SPCX sec8, RKLB sec series)"
  "001:PIL-2":
    wrong_if: "f2_radiator_mass_per_MW_uncertainty_band_pct > 0.50"
    class: REACHABLE-BUT-NOT-RECORDABLE
    outcome: FIRED
    resolving_source: "NASA/peer-reviewed constants (outside the registry) + a contract rule admitting a non-agentii URL"
  "001:PIL-3":
    wrong_if: "count_of_universe_issuer_quarters_with_unresolved_defect_status > 0"
    class: EVALUABLE
    outcome: NOT DISCHARGED
    resolving_source: "each issuer's Item 1A — on-platform (~19 reads)"
  "001:PIL-4":
    wrong_if: "spcx_facility_pue_ratio > 1.5"
    class: UNRESOLVABLE-FROM-PUBLIC-SOURCES (issuer value) + UNRESOLVABLE-FROM-PLATFORM (PUE benchmark)
    outcome: FIRED on the facility-side target reading; AT THRESHOLD on the expected one
    resolving_source: "the issuer's facility-draw disclosure (monitor); the industry PUE benchmark (licensed)"
  "001:PIL-5":
    wrong_if: "share_of_001_headline_figures_converted_to_DEMONSTRATED < 0.5"
    class: EVALUABLE, BUT DENOMINATOR-UNSTATED
    outcome: FIRES on the readings where the BASIS matters
    resolving_source: "this ledger (§1) + a spec amendment naming the denominator"
  "001:PIL-6":
    wrong_if: "count_of_spcx_growth_figures_unclassified_for_entity_boundary_effects > 0"
    class: EVALUABLE
    outcome: DISCHARGED — 31/31 classified, 11 of 31 CONTAMINATED
    resolving_source: "SPCX 10-Q segment and restatement disclosures"
  "001:PIL-7":
    wrong_if: "count_of_001_falsifiers_unclassified_or_without_named_resolving_source > 0"
    class: EVALUABLE
    outcome: METRIC 0 for 001's six falsifiers, extended to 002's seven
    resolving_source: "this ledger (§2)"
citations:
  - figure: "SPCX operating_margin, filed −16.68% vs platform +29.79%"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 36
    url: "https://agentii.ai/v/SPCX/sec8/36"
    located_via: read_source_pages
  - figure: "SPCX Segment revenue 541 against segment operating result 4,817"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 5
    url: "https://agentii.ai/v/SPCX/sec8/5"
    located_via: read_source_pages
  - figure: "SPCX realized payload per customer launch"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 35
    url: "https://agentii.ai/v/SPCX/sec8/35"
    located_via: read_source_pages
  - figure: "SPCX launch counts and Launch Services revenue $64.8M"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec7
    page_no: 7
    url: "https://agentii.ai/v/SPCX/sec7/7"
    located_via: read_source_pages
  - figure: "SPCX facility-side power against the same compute basis (PIL-4 input, a transcript not a filing)"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 4
    url: "https://agentii.ai/v/SPCX/ect1/4"
    located_via: read_source_pages
  - figure: "GOOG: no Suncatcher/satellite/orbit disclosure across 216 filing + 17 transcript pages"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 15
    url: "https://agentii.ai/v/GOOG/sec156/15"
    located_via: read_source_pages
  - figure: "MRCY true quarter 232,872 against the served 983,622"
    ticker: MRCY
    form_type: 10-Q
    citation_id: sec202
    page_no: 4
    url: "https://agentii.ai/v/MRCY/sec202/4"
    located_via: read_source_pages
  - figure: "MRCY adjusted-income bridge, ten terms, closes for both periods"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec203
    page_no: 37
    url: "https://agentii.ai/v/MRCY/sec203/37"
    located_via: read_source_pages
  - figure: "IRDM billable-subscriber definition, filed as MD&A prose"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 25
    url: "https://agentii.ai/v/IRDM/sec191/25"
    located_via: read_source_pages
  - figure: "UTHR gross profit 683.8 on revenue 783.3 = 87.30%"
    ticker: UTHR
    form_type: 10-Q
    citation_id: sec219
    page_no: 4
    url: "https://agentii.ai/v/UTHR/sec219/4"
    located_via: read_source_pages
---

# Validation Ledger — thesis 002's primary artifact

> **Task T900 · Phase 7 · the last writer.** This artifact is `_cross/`: it depends on every
> prior phase and carries no `[P]` tag of its own. It is the artifact `spec.md` §6 names as
> PIL-5's `source`, and the artifact PIL-7's falsifier names as its own.
>
> **Its own evidentiary status is `DERIVED`.** The headline arithmetic in §1 — every
> conversion share, every threshold comparison — was computed by this artifact from figures
> carried out of the other 41, and is graded `DERIVED`, not `DEMONSTRATED`. Per-row grades
> are stated in the tables. **This is a deliberate application of the brief's rule: if a
> number in these tables was derived here rather than read from an artifact, it is graded
> `DERIVED` and said so.** No figure below is quoted from a linkbase `LABEL`, none is
> sourced from a `computed` column, and no percentage appears without its denominator named
> in the same row.

**What this ledger found, in one paragraph.** PIL-5's falsifier is **denominator-dependent,
and the denominator is unstated** — that is the finding, and it is stated rather than
resolved. Under nine admissible readings it lands **exactly on its 0.5 threshold three
times with zero margin** and **fires four times**, and the reading with the most support is
one of the firings. Worse than the arithmetic: **converting a figure to `DEMONSTRATED` does
not convert its BASIS**, and the two come apart by **46.47 percentage points on a single
ratio** — so a ledger that counts platform reads as conversions **over-counts by
construction**, and on the readings where the basis matters **the pillar fails**. Separately,
**30 amendments are queued and none is registered**; **six corrections to 001 were derived
and ZERO propagated**; and 001's own claim that PIL-3, PIL-5 and PIL-6 are its unreachable
set is **wrong — the set is PIL-4, PIL-5, PIL-6**.

---

## §1 — PIL-5's verdict, computed under EVERY reading

### 1.1 The falsifier exactly as written

> **`metric=share_of_001_headline_figures_converted_to_DEMONSTRATED threshold=0.5 source=validation_ledger op=<`**
>
> "**Independently falsifiable**: fewer than half of 001's headline figures convert."
> — `spec.md` L276–L294

`spec.md` §6 defines the share as `rows whose grade moved to DEMONSTRATED ÷ total rows`,
**published with its row count**. It does not say what a "row" is. The CHK004 clarification
at the implement preflight supplies the conversion rule and makes it *harder*, not easier:

> A figure that **P6 classifies boundary-contaminated**, or that **P2 leaves unbounded**,
> does **not** convert to `DEMONSTRATED` — it becomes `DERIVED` or stays `CLAIMED`. … the
> conversion share … is *supposed* to fall when figures turn out to be contaminated.

**So the rule is stated and the population is not.** 001's headline set is not a single
list. It is at minimum: **the six figures in 001's summary table** (one per technology line),
**the claim's `12.3% of revenue`**, and **the 27 graded claims in 001's register**. These are
three different populations, and the share is not invariant across them.

### 1.2 The ledger's denominator, and why every row is named

Per DA-29's mechanical rule applied to this artifact — *do not present a percentage whose
denominator you have not named* — **this ledger does not select a denominator.** It publishes
the fraction under each admissible one, with the population enumerated in the table so a
reader can recount it. The six headline figures are read from 001's own summary table:

| # | Line | Governing bound | Value | Unit | Verdict at 001 |
|---|---|---|---|---|---|
| 1 | Launch cost floor | Propellant mass × price ÷ payload | **46.0** | USD per kg to LEO | **HOLDS** |
| 2 | Orbital power envelope | Array area per MW delivered BOL | **5,080** | m² per MW | **HOLDS** |
| 3 | Constellation economics | Break-even revenue at observed gross margin | **1.69** | × current revenue | UNRESOLVABLE |
| 4 | Microgravity economics | Incumbent terrestrial gross margin | **72.0** | percent | **HOLDS** |
| 5 | Orbital compute closure | Rejection area per MW at 300 K | **2,419** | m² per MW | UNRESOLVABLE |
| 6 | Spectrum and slots | Reference transaction for three spectrum blocks | **19.6** | USD billions | UNRESOLVABLE |

Two conversion counts are live, and the difference between them is a **specification** point
rather than a judgement call:

- **C = 3 — the verdict reading.** Lines 1, 2 and 4 carried `HOLDS` at 001 and no artifact
  overturns the bound. This is the reading 001's own summary table supports.
- **C = 2 — the CHK004-strict reading.** Line 2 cannot convert, because **P2's falsifier
  FIRED**: the radiator band breaches ±50% in **two of three scopes** (±83% un-scoped, ±56%
  advanced-class, ±35% crewed-class), and CHK004 says in terms that a figure **P2 leaves
  unbounded does not convert**. Its point value was also corrected — the eclipse multiplier
  is **1.587×, not 8×**, so for a dawn-dusk SSO the array falls **5,080 → 3,201 m²/MW
  (−34.8%)** and the surviving result is an **order of magnitude (10³ m², 10¹ t per MW)**,
  stable across a 7.72× area range and a 3× density range. **A corrected order of magnitude
  is not a `DEMONSTRATED` point figure.**

### 1.3 The reading ladder — every admissible denominator, its row count, and the result

| # | Reading — the denominator, named | Rows | Converted | **Share** | `op=<` vs 0.5 |
|---|---|---|---|---|---|
| **R-A** | **001's summary table, all six technology lines** | **6** | 3 (C=3: Lines 1, 2, 4) | **0.5000** | **NOT below — threshold met with ZERO MARGIN** |
| **R-A′** | same, CHK004-strict | 6 | 2 (Lines 1, 4) | **0.3333** | **TRIGGERED** |
| **R-B** | **the six + the claim's `12.3% of revenue`** | **7** | 3 | **0.4286** | **TRIGGERED** |
| **R-C** | **the four lines that carried a value** — set named below | **4** | 3 | **0.7500** | NOT below |
| **R-C′** | same, CHK004-strict | 4 | 2 | **0.5000** | **NOT below — ZERO MARGIN** |
| **R-D** | **every numeric claim in 001's register** | **27** | 0–21 | **[0.0000, 0.7778]** | **UNRESOLVED — see 1.4** |
| **R-E** | SPCX ratio block, value-only | 12 | 10 | 0.8333 | NOT below |
| **R-E′** | SPCX ratio block, value + components | 12 | 6 | 0.5000 | **NOT below — ZERO MARGIN** |
| **R-E″** | SPCX ratio block, value + components + one labelled basis | 12 | 3 | **0.2500** | **TRIGGERED** |
| **R-E‴** | SPCX ratio block incl. the null slot | 13 | 10 / 6 / 3 | 0.7692 / **0.4615** / **0.2308** | **TRIGGERED at the middle reading too** |
| **R-F** | VRT ratio block, fields that are the ratio they claim to be | 16 | 2 | **0.1250** | NOT below; most generous admissible = 2/10 = **0.2000** |
| **R-G** | GOOG ratio block, cells | 140 | 79 | 0.5643 | NOT below |
| **R-G′** | GOOG ratio block, series | 14 | 2 | **0.1429** | **TRIGGERED** |

**R-C's set, named — because `thesis.md` L308 uses the phrase without defining it.** The
four lines whose Value cell is an engineering **LEVEL with a unit**: Lines **1, 2, 4, 5**
(USD/kg, m²/MW, percent, m²/MW). Lines 3 and 6 carry a break-even **multiple** and a
reference **transaction price**. Substituting Line 6 for Line 5 changes nothing: both are
UNRESOLVABLE, so the share is 3/4 or 2/4 on either set. **The set is stated here so a reader
can dispute it rather than inherit it.**

### 1.4 R-D: why the register reading cannot be adjudicated, and why that is a finding

001's register holds **27 graded claims — 21 DEMONSTRATED, 3 CLAIMED, 3 MODELED**. **21 of
the 27 are already `DEMONSTRATED` and therefore cannot "move to" `DEMONSTRATED`; they are
inert in this metric by construction.** That single fact is the most important thing in this
table: **the register denominator is 78% inert, so it is the one reading that guarantees
whatever result the reader expects.** A share computed over it measures 001's original
grading discipline, not 002's validation.

Six claims are **contradicted or downgraded by name** by 002's corpus and therefore cannot
convert:

| Claim (001's register) | Why it cannot convert | Artifact |
|---|---|---|
| "The only issuer disclosing a per-launch figure discloses $14,667/kg" | 001's published numbers are **1.79×–2.62× too low**; the DA-25 gap is present in **4 of 4** periods | RKLB unit-economics |
| "The capability is real and immaterial to its listed owner" | MRCY discloses space platform revenue at **7.9% of revenue, +39.4% y/y** — the premise is inverted | MRCY recent-quarter |
| "Hyperscaler capex implies terrestrial capacity far exceeding any orbital plan" | the **"8×"** and **"dwarfs"** do not survive; the pessimistic case is **0.74×–1.04×** and straddles | MSFT recent-quarter |
| "The demand side turns over 73× the pure-play cohort, annually" | the cohort aggregate is **72.13%**; 001's "within 0.7 points" is **0.7621 pp unrounded**, and P10 reaches **0 of 5** gates | UTHR unit-economics |
| "Merck's R&D alone is 7.3× the combined annual revenue" | the **`$12,700M`** sits in a gross-profit column as an R&D *sum*; the convergence is not a cohort statistic | UTHR unit-economics |
| "equity cushions span 32.3% (MRK), 25.5% (BMY), 12.2% (AMGN)" | AMGN is reported on **four bases** and 001 selected the **second-lowest** | UTHR unit-economics |

The remaining **21 claims are neither converted-by-name nor contradicted-by-name in this
ledger.** So the register reading is **[0/27, 21/27] = [0.0000, 0.7778]**, and **the
uncertainty band is wider than the threshold distance on either side. A metric whose
uncertainty band straddles its own threshold is not a metric.** Recorded as `UNRESOLVED` —
**not** as a pass, and not as a fail.

### 1.5 The ratio artifacts' own on-record readings

These are the four artifacts PIL-5 subscribes to (`SPCX × ratio-analysis`, `RKLB ×
ratio-analysis`, `VRT × ratio-analysis`, `GOOG × ratio-analysis`). They reported the full
set rather than choosing, which is what this ledger is doing one level up.

- **SPCX — 0.8333 / 0.5000 / 0.2500** at denominators 12, 12, 12. The **value-only** reading
  is 10 of 12, the **value + own components** reading is 6 of 12 and is *saved only by the
  strict inequality*, and **value + components + one labelled basis collapses to 3 of 12 =
  0.2500, which TRIGGERS.** Including the null slot at **denominator 13** flips the middle
  reading to **0.4615 — also TRIGGERED.** **Two of the three SPCX readings fire.**
- **VRT — 2 of 16 ratio fields are the ratio they claim to be = 0.1250.** Every admissible
  reading is below 0.5, including the most generous (crediting all 6 UNRESOLVED rows as
  neutral → 2/10 = **0.2000**), and **none is close.** VRT is the only subscribed artifact
  where the answer is stable across every reading, and it is stable *failing*.
- **GOOG — 0.5643 / 0.1429 / 0.1429.** The cell-level reading passes at **79 of 140**; both
  series-level readings collapse to **2 of 14**. **The flattering self-credit reading of 6/14
  was reported by the artifact and explicitly rejected**, and is recorded here as rejected.
- **RKLB — the contribution is structural, not fractional.** For **LOSS-MAKING issuers the
  operating-income class cannot convert via a platform read at all**: every loss period is
  served as a positive magnitude, so a "conversion" recorded from the platform's own read is
  a read of the *defect*. **A ledger counting platform reads as conversions OVER-COUNTS BY
  CONSTRUCTION**, and RKLB proves it on itself:
  > `NetIncomeLoss` Q2 2026 `diff = 10,654 = 2 × 5,327` — and the tax was **NOT** stripped.
  > `IncomeTaxExpenseBenefit` is **correct at Q2 2026 and stripped at FY2025, at the same arc
  > weight.** "**The largest error at RKLB was not a sign error**" — FY2025 balance-sheet rows
  > read the **PRIOR-YEAR COMPARATIVE COLUMN**: current ratio **2.071** against a filed
  > **4.083** (**−49.3%**), quick **−53.2%**, working capital **−65.8%** — at platform
  > severity **`warn`**.

### 1.6 🔴 THE VERDICT, STATED PLAINLY

> **PIL-5's falsifier fires on the reading with the most support, and lands exactly on its
> threshold with ZERO MARGIN on three more. This is a PARTIAL FALSIFICATION OF THESIS 002,
> and it is recorded as one rather than deferred.**
>
> **On the readings where the BASIS matters, the pillar fails.** The basis is what decides a
> conversion, and when it is named the SPCX block falls from 0.8333 to 0.2500 and the GOOG
> block from 0.5643 to 0.1429. Those are not marginal movements; they are the majority of
> the denominator changing sides.
>
> **And the ambiguity is itself the finding** — it is the same defect class as PIL-2's
> unrecordable source class, and it is constitution §DA-29's family: **a test whose terms
> cannot be located in the source is not a test. A falsifier that passes or fails on an
> unstated denominator choice is not falsifiable.**

Three independent reasons the specified test fails, each sufficient on its own:

1. **The population is unstated.** Nine admissible readings, four of which fire and three of
   which sit exactly on the threshold. **A metric that lands exactly on its threshold three
   times out of nine is not a metric with margin; it is a metric with a decision rule.**
2. **The population is inert by 78%** under the only reading that could look comfortable
   (§1.4) — 21 of 27 rows cannot move, so that reading cannot test the claim.
3. **The numerator is method-dependent, not evidence-dependent** (§1.6, below). The share
   measures which tools were used as much as what the filings say.

### 1.6.1 The substantive finding — a converted FIGURE is not a converted BASIS

> **Converting a figure to `DEMONSTRATED` does not convert its BASIS, and the two come apart
> by 46.47 percentage points on a single ratio.**
>
> SPCX `operating_margin`: the platform serves **+29.79%**. The filed figure, computed from
> the AI-segment loss over consolidated revenue at a named basis, is **−16.68%**. The
> difference is **46.47 pp** — and the platform value is internally plausible, so nothing
> about it invites a second look. The conversion status of that figure and the basis on which
> it was computed are **independent properties**, and a ledger that records only the first is
> silent about the second.
>
> This is why the arithmetic in §1.3 is not the deliverable. **A ledger can be built that
> reports 0.8333 and is entirely correct about grades and entirely silent about bases.** The
> `12.3% of revenue` claim is the clean instance in the other direction: it recomputes at
> **12.31%** from filed cells (Segment revenue 541 against the segment operating result 4,817
> is the NAIVE reading of the same page — [📄 SPCX 10-Q p.5](https://agentii.ai/v/SPCX/sec8/5))
> and it converts only once the **basis** is named. A `/kg` claim has the same structure: the
> realized denominator restates every demonstrated $/kg by **+79% to +162%** against a
> tolerance of ±15%, and the filed cells that do it are on the statement face
> ([📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35); [📄 SPCX 10-Q p.7](https://agentii.ai/v/SPCX/sec7/7)).

**One ratio field carries the whole finding.** `operating_margin` at SPCX is the field where
grade and basis diverge most, and it is the field the ratio artifact used to demonstrate
that they diverge at all. The filed figure it should carry is reachable, and the page that
carries the segment result it turns on is [📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36).
The same relationship governs 001's `72.0 percent` microgravity bound: it **converts** as a
value and **needed an attribution correction** at the same time — the filed gross profit is
**683.8 on revenue 783.3 = 87.30%** at UTHR
([📄 UTHR 10-Q p.4](https://agentii.ai/v/UTHR/sec219/4)), against 001's `72.0` which is
AMGN's on a named basis. Both figures are `DEMONSTRATED`. Only one of them was the one
quoted.

---

## §2 — The falsifier reachability census (PIL-7's output)

### 2.1 Vocabulary, and the four outcomes

PIL-7's metric is *count of 001 falsifiers unclassified **or** without a named resolving
source*. An item can therefore be **evaluable**, **unreachable**, or **reachable but not
recordable** — and only the third is new. The four outcomes this census uses:

| Outcome | Meaning |
|---|---|
| **EVALUABLE** | the falsifier can be run on-platform, today, with the tools in this registry |
| **UNRESOLVABLE-FROM-PUBLIC-SOURCES** | the disclosure does not exist publicly at all → name the disclosure that would resolve it; monitor |
| **UNRESOLVABLE-FROM-PLATFORM** | the data is public but unreachable, licensed, or in a registry the platform does not carry → record as a finding about platform reach, never as absence of evidence |
| **REACHABLE-BUT-NOT-RECORDABLE** | the datum is reachable **and the artifact contract cannot record it** → a passing evaluation would be unrecordable. **This is proposed as a third situation (A22) and is not yet a registered class** |

### 2.2 The seven KINDS of "not testable"

"Not testable" is not one thing. A13's heading read *FOUR* and the table carried **seven**;
the mismatch was caught by `IRDM × competitive`, which is the artifact that earned the
correction. **A "not testable" recorded without its kind is a failure of PIL-7**, because the
kinds have different remedies and only one of them is a research task:

| # | Kind | What it means | Resolving source / remedy | Home instance |
|---|---|---|---|---|
| **1** | **Ingestion absence** | the document exists and is not on the platform | ingest it | **YSS 10-K** (DA-26 untestable only for want of it) |
| **2** | **Genuine absence from source** | nothing was ever disclosed | name the disclosure; monitor | **SATS listing event**; UTHR programme economics; VRT's pre-listing structure |
| **3** | **Validator-completeness** | the validator cannot express the test | amend the validator | **PIL-2's source class**; the citation contract's URL pattern |
| **4** | **Mechanism-population identity** | the sample is defined by the mechanism's own property and carries no information about the remainder | **exclude from the denominator** | **DA-27 at every December-year-end issuer** (SATS, VRT, RKLB, LUNR, VOYG, BA, BWXT) |
| **5** | **Ingestion absence of a DATUM CLASS** | a whole class of datum is not ingested | name the class | **DA-25 at IRDM** — the definition **IS filed**, as MD&A prose that no structured query can reach ([📄 IRDM 10-Q p.25](https://agentii.ai/v/IRDM/sec191/25)), so the zero is **a zero BY CONSTRUCTION**; **PIL-5's terrestrial colocation cost**; **PIL-6's FCC IBFS / ITU** |
| **6** | **Coverage window** | the data exists but outside the served window | widen the window | **DA-28 at IRDM** (SEC coverage opens **2022-02-17**, `sec147`; the IPO is outside it) |
| **7** | **Detector gap at a computable datum** | the datum **is present and computable** and no detector exists | **write the detector** | **DA-25 at GOOG** (no per-unit ratio is served and none exists in the skill's formula table); **DA-27 at the ratio layer** |

**Kind 7 is the only kind that is a defect of *this programme* rather than of the world or
the platform.** A detector gap at a computable datum is fixable by work and by nothing else,
and it is the kind most easily mistaken for "not testable" in the passive sense.

### 2.3 The per-pillar classification, 001's six falsifiers and 002's seven `wrong_if` blocks

**Reconciling the two risk artifacts and extending them.** The SPCX risk artifact classified
**six** falsifiers and closed at **"PIL-7 metric = 0. Six falsifiers, six classified, six
with a named resolving source."** That census is correct for 001's six. This ledger extends
it in two directions: it **corrects which of 001's falsifiers are unreachable**, and it
classifies **002's own seven `wrong_if` blocks**, which the risk artifact did not cover
because they were not yet all written.

| Falsifier | Class | Kind | Fired / discharged | Resolving source (named — mandatory) |
|---|---|---|---|---|
| **001:PIL-1** launch cost floor, ±15% after denominator validation | **EVALUABLE** | — | **FIRED** | issuer filings, on-platform |
| **001:PIL-2** radiator band > ±50% | **REACHABLE-BUT-NOT-RECORDABLE** | **3** validator-completeness | **FIRED** (band ±83/±56/±35%; **two of three scopes breach**) | NASA/peer-reviewed constants **+ a contract rule admitting a non-agentii URL** |
| **001:PIL-3** unresolved-defect issuer-quarters > 0 | **EVALUABLE — blocked by EFFORT, not reachability** | — | not discharged | each issuer's Item 1A, on-platform (~19 reads) |
| **001:PIL-4** facility PUE > 1.5 | **UNRESOLVABLE-FROM-PUBLIC-SOURCES** (issuer value) + **UNRESOLVABLE-FROM-PLATFORM** (PUE benchmark) | **2** + **5** | **FIRED on the facility-side target reading; AT THRESHOLD on the expected one** | the issuer's facility-draw disclosure (monitor); the industry PUE benchmark (licensed) |
| **001:PIL-5** conversion share < 0.5 | **EVALUABLE, DENOMINATOR UNSTATED** | **4** mechanism-population identity | **FIRES where the basis matters** | this ledger (§1) + a spec amendment naming the denominator |
| **001:PIL-6** unclassified growth figures > 0 | **EVALUABLE** | — | **DISCHARGED — 31/31 classified, 11 of 31 CONTAMINATED** | SPCX 10-Q segment and restatement disclosures |
| **001:PIL-7** falsifiers unclassified / without named source > 0 | **EVALUABLE** | — | **METRIC 0** for 001's six | this ledger |
| **002:PIL-1 … PIL-4** | EVALUABLE | — | PIL-1 FIRED; PIL-4 at threshold | on-platform |
| **002:PIL-5** | see §1 | 4 | **PARTIAL FALSIFICATION** | this ledger |
| **002:PIL-6** | EVALUABLE | — | DISCHARGED | SPCX 10-Q |
| **002:PIL-7** | EVALUABLE | — | metric 0 | this ledger |

### 2.4 ⚠️ 001's unreachable set is **PIL-4, PIL-5, PIL-6** — not PIL-3, PIL-5, PIL-6

> 001's own headline reads: *"Headline finding: three of six falsifiers cannot fire from any
> public source. **PIL-3, PIL-5 and PIL-6**."*

**That is wrong, and 001's own text says so.** 001 calls PIL-3 *"an unbuilt census, not an
unavailable disclosure"* — the falsifier is blocked by **effort**, and the resolution is
**19 Item 1A reads on-platform**, not a disclosure that does not exist. Meanwhile **PIL-4 was
omitted**, and PIL-4 is the one that genuinely cannot fire from public sources: its input is
**a transcript, not a filing** ([📄 SPCX transcript p.4](https://agentii.ai/v/SPCX/ect1/4)),
and the universe contains **no issuer disclosure of a facility draw at all** — Alphabet's
entire SpaceX-related SEC disclosure across **216 filing pages and 17 transcript pages** is
a **$94.1B equity stake** and **$99.0B of earnings**, in which `Suncatcher`, `satellite`,
`orbit` and `orbital` return **zero** hits ([📄 GOOG 10-Q p.15](https://agentii.ai/v/GOOG/sec156/15)).
**Not an oversight: the correct application of a materiality threshold.** The number PIL-4
needs will not be disclosed until it is financially material — which is exactly when it stops
mattering to the falsifier.

**The corrected unreachable set is PIL-4, PIL-5, PIL-6, and each carries a kind**: PIL-4 is
kinds **2 + 5**, PIL-5 is kind **4**, PIL-6 is kind **5**. PIL-3 moves to **EVALUABLE**.

### 2.5 What FIRED, what was DISCHARGED, what could not be evaluated

| State | Falsifiers | Note |
|---|---|---|
| **FIRED** | 001:PIL-1, 001:PIL-2, 001:PIL-4 (facility-side reading) | three, and **two of the three are the ones 001 expected to hold** |
| **PARTIAL FALSIFICATION** | 001:PIL-5 / 002:PIL-5 | §1.6 |
| **AT THRESHOLD, zero margin** | 001:PIL-4 (expected reading) | cannot be evaluated further without the undisclosed draw |
| **DISCHARGED** | 001:PIL-6, 001:PIL-7, 002:PIL-6, 002:PIL-7 | **PIL-6 is discharged at 31/31 classified — and 11 of 31 are CONTAMINATED**, which is a discharge of the *counting* obligation, not a clearance of the data |
| **NOT DISCHARGED — effort, not reachability** | 001:PIL-3 | ~19 issuer Item 1A reads; on-platform |
| **COULD NOT BE EVALUATED** | none — **every falsifier carries a named resolving source** | PIL-7's own metric |

**PIL-7's metric for this ledger is 0.** Eleven falsifier-blocks classified (001's six plus
002's own seven, deduplicated where they are the same block), **every one with a named
resolving source**, and **no falsifier is left without one**. *A falsifier without a named
resolving source is a failure of PIL-7* — and on that test, PIL-7 passes.

### 2.6 ⚠️ The identity collision — preserve the `001:` namespace

`PIL-4` names **two different things**: 001's microgravity pillar and 002's own nameplate
pillar. The same collision exists for `PIL-2` (001's power envelope vs 002's constant
sourcing) and `PIL-6` (001's spectrum vs 002's entity-boundary check). The frontmatter's
`falsifiers_under_classification` block therefore **namespaces every key as `001:PIL-n` or
`002:PIL-n`**, and this ledger preserves that distinction throughout. **A census that
reports "PIL-4 fired" without the namespace is ambiguous between a microgravity falsifier and
a nameplate ratio**, and the two have different thresholds, different sources and different
verdicts.

---

## §3 — The DA census across all 41 artifacts

### 3.1 Method, and why it is not a regex

**Verdict vocabulary in this corpus is uncontrolled, and the census was built by reading.**
Field reports include `EXHIBITED`, `PRESENT`, `CONFIRMED`, `CLEAN on the issuer CONTAMINATED
on the instrument`, `UNEXERCISED`, `UNEVIDENT`, `NOT-TESTABLE — kind 4`, `REFUTED on positive
evidence`, `PASSES the circularity test`, `NOT APPLICABLE — checked`, `NOT PRESENT`,
`NOT EXHIBITED`, `EXPLAINED — not present under the declared reading`, `PROMOTED TO REGISTERED
DEFECT`, `CANNOT MANIFEST by construction`, `does not fire`, and `APPLIED — self-clean`. A
regex over any single token would produce exactly the failure mode this thesis spent Phase 3
documenting: **a check that closes cleanly while testing nothing.**

**The census also has to carry two verdicts for the same issuer on the same DA where the
statement axis differs** — BWXT's DA-23 is legitimately **both** clean at subtotals **and**
present at a component, and those are not contradictory. **A single-valued census cell is
the defect, not the fix.**

**Third: an `X` in the matrix below means the DA is not engaged by any artifact for that
issuer. It is NOT clean, and this ledger does not count it as clean.** Refusal to read an
unengaged cell as a pass is the entire point of the register.

### 3.2 DA-23…DA-30, per issuer

Legend: **C** CONFIRMED · **K** CLEAN (subtotal-level only) · **R** REFUTED · **N** NOT
TESTABLE · **U** UNEXERCISED · **E** UNEVIDENT · **P** PRESENT (unregistered class or
adjacent mechanism) · **V** UNVALIDATED-BY-PLATFORM · **X** not engaged.

| Issuer | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|---|---|---|---|---|---|---|---|---|
| **BA** | C ×2 | P (EXHIBITED) | P (EXHIBITED) | P (EXHIBITED) | N/A-checked | N/A + P | X | X |
| **BWXT** | **C at component / K at subtotal** | P | R (not present) | X | N-A by construction | X | X | **defining instance** |
| **FLY** | **C 4/4, 15/15** | R | R | **R — falsifies universality** | R (not confirmed) | C | X | X |
| **GOOG** | **K on issuer / C on instrument** | C on NI ratios / R on operating ratios | N (kind 7) | C ×2 | N (kind 7) | C (live, non-IPO) | X | C |
| **HAWK** | **C 5/6** | R (not present) | P (scope-limited) | N (no 10-K) | N/A-checked | **C site / R mechanism** | X | X |
| **IRDM** | **K scoped; 001 clearance REFUTED** | R | **N — kind 5 datum class** | C ×2 | R (does not fire) | **N — kind 6 coverage window** | P | P |
| **LUNR** | **C (candidate → #7)** | R (not present) | R (premise inverted) | C (exception overturned) | N-A by construction | X | X | X |
| **MRCY** | **C 11/13** | R (+ variant) | R | C | **C + self-contradiction** | R | **P (clean bridge)** | R |
| **MSFT** | **C — "the default"** | R (discharged, clean) | X | C | **C + third source value** | X | **C (passes)** | P |
| **NVDA** | **E income / P cash-flow** | R | R (not exhibited) | P 3/3 | **P 11/11** | N/A + P split | **C (passes)** | **C — class present** |
| **RKLB** | **C (two regimes)** | E (magnitude) | X | C ×2 | **N — kind 4, excluded** | U registered / P discontinuity | P | P |
| **SATS** | **C 12/12** | **R as recorded / C INVERTED** | R | C 4/4 | **N — kind 4** | **N — kind 2** | **P + new failure kind** | C ×4 |
| **SPCX** | **C 7/7** | R | C | **N (no annual row)** | C method / benign | **C as open exposure** | **F + P** | **C, quantified** |
| **UTHR** | **C 11/11 component** | R (clean) | X (not engaged) | R (does not reproduce) | X | X | P | **9 sites** |
| **VOYG** | **C (plain strip)** | X | R (not present) | R (not present) | N/A | **P — promoted** | X | X |
| **VRT** | **C cash-flow / U income** | R (clean) | **N — no object** | C (Q4) | **N — kind 4** | R | **C (passes)** | C |
| **YSS** | **C (FLIPPED)** | X | **C ×2** | **N — kind 1 ingestion** | C method / benign | **C — cleanest in universe** | X | X |

**Counts.**

- **DA-23: 14 of 17 issuers carry an exhibited instance** (BA, BWXT, FLY, HAWK, LUNR, MRCY,
  MSFT, RKLB, SATS, SPCX, UTHR, VOYG, VRT on the cash-flow axis, YSS). **2 clean at
  subtotal-level only** (GOOG, IRDM). **1 UNEVIDENT** (NVDA — zero negatives). **1
  UNEXERCISED** (VRT on the income-statement axis — 61 of 61 facts positive, 13 of 13
  identities closing vacuously). **This is not a census of a rare defect. It is a census of a
  default.**
- **DA-24: 4 exhibited or present** (BA, BWXT, GOOG on net-income-bearing ratios, SATS
  inverted), **1 UNEVIDENT** (RKLB — magnitude not reproducible), **1 partial** (GOOG), **11
  refuted or clean.**
- **DA-25: 8 confirmed or present** (BA, BWXT, GOOG, HAWK, SPCX, VRT, YSS, UTHR-adjacent),
  **5 refuted**, **2 not testable** with named kinds (IRDM kind 5, VRT "no object").
- **DA-26: 9 confirmed**, **4 not testable** with named kinds, **1 falsifies universality**
  (FLY), **1 not engaged** (BWXT).
- **DA-27: confirmed at 6 issuers** (GOOG, MRCY, MSFT, NVDA, SPCX, YSS), **not-testable at 5
  with kind 4 named**, **not applicable/refuted at 4**.
- **DA-28: 8 present or confirmed** (FLY, GOOG, HAWK, RKLB, SPCX, VOYG, YSS, and NVDA's
  adjacent split), **2 not testable with kinds 2 and 6**, **3 refuted or not applicable**.
- **DA-29: engaged at 7 issuers only** (IRDM, MRCY, MSFT, NVDA, SATS, SPCX, VRT). **10 issuers
  never engage it.** For those 10 it is **UNEXERCISED, not clean.** Where it *is* applied it
  passes **on the terms, not on the closure**: MRCY's adjusted-income bridge carries **all ten
  terms on the page and closes exactly for both periods** — `−30,471 + 2,894…`
  ([📄 MRCY 10-K p.37](https://agentii.ai/v/MRCY/sec203/37)) — and MSFT's reading states the
  rule this ledger adopts throughout: **"DA-29 passes: no term is a back-solve, and the
  closure is not the evidence — the terms are."**
- **DA-30: engaged at 7 issuers only** (GOOG, MRCY, NVDA, SATS, SPCX, UTHR, VRT). **10 issuers
  never engage it**, including the instance's own home issuer's peers. **UNEXERCISED, not
  clean.**

**So the honest headline count is that DA-29 and DA-30 — the two entries added at 1.5.0 —
are engaged by 7 of 17 issuers and unengaged by 10**, and an unengaged cell is not a passed
check. That is a coverage finding about the register, not about the issuers.

### 3.3 Corrections superseding the constitution's census row

These correct the register in place. **They are carried here because the ledger is the
artifact that reconciles the register against what the artifacts actually found.**

1. **DA-23's `Clean` row now means SUBTOTAL-LEVEL ONLY, and the qualifier is load-bearing.**
   The constitution carries this correction; the ledger records that it is **not cosmetic**.
   **A subtotal-level census CANNOT support an unqualified `Clean`** — an issuer can be clean
   at every subtotal while a **component** of the same statement is sign-corrupted.
2. **MRCY, UTHR and SATS are REMOVED from the `Clean` row.** MRCY: **11 of 13 filed periods
   stripped**; the clean verdict came from testing **only the filed-positive period**. UTHR:
   **11 of 11 verified negative components stripped while all 35 parent facts are correctly
   positive**, localised to one dimension member. SATS: **12/12 filed-negative subtotals
   stripped, 8/8 filed-positive clean.**
3. **NVDA is `UNEVIDENT`, not clean.** The entire income statement has **zero negatives**
   (`OperatingIncomeLoss` 69 facts, all non-negative 2014–2026), so **the sign test can
   neither pass nor fail.** 001's "12 issuer-quarters" rule count must be re-scored to
   *issuer-quarters where DA-23 was TESTABLE*.
4. **VRT is `UNEXERCISED`, not clean.** All **61** `OperatingIncomeLoss` facts are positive,
   so the `|x|` channel **had nothing to act on** — 13 of 13 identities close **vacuously**.
   **`Unexercised` and `Clean` are different results and must not be reported as the same.**
5. **BWXT and VRT are clean at subtotals and stripped elsewhere on the statement.** The
   discriminator is the **SIGN OF THE VALUE**, not the concept and not the period — VRT
   `NetCashProvidedByUsedInFinancingActivities` is **correct at `+11.9` in one period and
   stripped at `−3.0` in another**; NVDA investing **+26,429,000,000 against a filed
   `(26,429)`**. **A census scoped to the income statement cannot see this.**
6. **DA-26's entity count moved 19 → 20, and universality is FALSIFIED.** FLY shows **zero
   instances on either surface**, so one counterexample is sufficient to falsify the coverage
   claim: **the "19 of 19" figure should be withdrawn.** LUNR was the sole recorded exception
   and it is **overturned**; GOOG and VRT are added at the Q4 position. **The register's
   sentence must read "20 issuers tested, 19 exhibiting", not "universal".**
7. **DA-24's defining SATS instance is an INVERTED IMPAIRMENT, not a sale, and its
   independence proof is WITHDRAWN.** `16,641,875 / 3,614,258 = 4.605×` reproduces — but the
   item is a **non-cash 5G-Network impairment CHARGE of `$16,481,468` thousand**, the licences
   **remain on the balance sheet at 2026-03-31 (`$34,550,802` thousand)**, AT&T took a
   **short-term spectrum manager lease**, and **no gain is recognised because nothing has
   closed.** The entry was **named for a gain and the thing it is named after is a loss.**
   The progression `2.3% → 5.7% → 460.5% → 118.1% → 10.7%` is wrong twice: four of five terms
   are **absolute values of losses**, and the 118.1% term is **annual-on-annual** — a DA-26
   instance sitting inside a DA-24 exhibit. Correct filed series:
   **`(2.28)% → (5.73)% → (460.46)% → (20.54)% → +10.71%`.** The independence proof fails on
   two independent grounds: it uses `EPS × shares`, a test **the register forbids**, and the
   residual `|EPS|×shares − |NI|` is **invariant under a global flip** — it cannot detect the
   defect it was used to rule out. **And the claim is substantively false: DA-23 IS present at
   SATS in the same periods.** Independence is **UNSUPPORTED**, not disproven.
8. **A `Clean` cell can be legitimately two-valued, and the census must carry both.** BWXT's
   DA-23 is clean at subtotals **and** present at a component; GOOG's is clean on the issuer
   **and** contaminated on the instrument. **Neither is a contradiction.**
9. **No reference to `DA-31` is admissible.** The SPCX risk artifact records a sibling's
   reference to `DA-31` as **REFUTED and out of register**: `REGISTERED` is DA-01…DA-30. Any
   `da_id` outside that set fails `da_id_registered`, and this ledger's frontmatter uses
   **DA-23…DA-30 only.**

### 3.4 Verdict drift — where artifacts disagree, and which governs

Four live disagreements are recorded rather than smoothed:

| Site | Artifacts | Resolution |
|---|---|---|
| **SPCX DA-24** | business-model **REFUTED** · recent-quarter **REFUTED** · ratio-analysis **NOT EVIDENT** · risk **PRESENT, refuted only in SEVERITY** | **The risk artifact governs** — it explicitly supersedes ratio-analysis, is recorded as **A28**, and establishes that **a contaminant inside a filed subtotal is ABSORBED by it**: item as share of the operating result **1.4 / 0.4 / 20.1 / 23.6%**, and **193 of the 827 Q2 improvement = 23.3%**. The ratio artifact read DA-24 as "NOT EVIDENT" **from a census that closed with zero residual — and a zero residual is EXACTLY what a contaminant inside the subtotal produces.** |
| **VRT DA-25** | recent-quarter **NOT TESTABLE — no object** · ratio-analysis **CONFIRMED (new instance)** · unit-economics **applied** | **All three stand, because the object differs by layer.** At the statement layer there is no per-unit metric; at the ratio layer `roa`/`roe` use **end-of-period balances where the schedule requires an average** — a normalisation substituted for a derivation. |
| **SPCX DA-28** | recent-quarter **"CONFIRMED as an open exposure; the split mechanism is NOT demonstrated"** · ratio-analysis **"CONFIRMED, mechanism named"** | **Both recorded, and the divergence is the finding**: the mechanism is named at the ratio layer (preferred `38,752 → nil`, APIC `37,706 → 167,344` on **85,675** of IPO proceeds) and **not demonstrated** on the face of the statement. Seven share counts, three axes, **no basis label.** |
| **VRT vs GOOG, `packaging/targets/*`** | VRT ratio-analysis asserts the path **does not exist**; GOOG ratio-analysis asserts it **EXISTS with decoy trees, all 32 hashes failing**, and withdraws any prior statement of absence | **These cannot both stand.** Recorded as an **unresolved contradiction between two artifacts in the same phase**, escalated rather than arbitrated: a ledger that picks a winner here would be choosing the more convenient instrument state. **It is a hard input to whichever thesis next touches the packaging path.** |

**Verdict attribution.** **No artifact in the set states that it produced a new A-number.** A-numbers appear in artifacts only as *citations*; every A-attribution in §6 therefore comes from `AMENDMENTS-PENDING.md`'s own `Source:` lines, and is recorded as such.

---

## §4 — The corrections ledger, and whether each PROPAGATED

### 4.1 ⚠️ A29 — the most consequential process finding in the thesis

> **A corrected figure has been derived THREE TIMES AND ABSORBED ZERO TIMES.**

| Derivation | Artifact | Status |
|---|---|---|
| 1st | 001's UTHR artifact (`1239`) | derived |
| 2nd | 002 recent-quarter artifact (`1500`) | re-derived, independently |
| 3rd | 002 unit-economics artifact | re-derived again |
| **Absorbed** | **—** | **001's L57 STILL READS `72.0`** |

**`upstream_stale: 001@1.2.0` records staleness without triggering anything — it is a
five-pin contract field with no consumer.** The field is present, correct, and read by
nothing. **A correction that is recorded and never propagated is indistinguishable, in
effect, from one never made.** This is not a documentation gap: the figure is wrong in the
published artifact, three artifacts know it is wrong, the contract announces that they know,
and the wrong figure is what a downstream reader sees.

### 4.2 Corrections to 001, and propagation status

| # | Correction | Produced by | Propagated to 001? |
|---|---|---|---|
| 1 | **UTHR `72.0` → `87.30`** (filed 683.8 / 783.3), and `72.0` re-attributed to AMGN on a named basis | UTHR unit-economics | **NO — 001 L57 still reads `72.0`. Derived 3×, absorbed 0×.** |
| 2 | **001's unreachable set is PIL-4, PIL-5, PIL-6** — not PIL-3, PIL-5, PIL-6 | SPCX risk §2 | **NO** |
| 3 | **The 24× nuclear reduction is 9.6×–16.8×** — 001 varies two things at once (`3.10×` array removal × `7.72×` 300→500 K), which compound unpriced and do not compound priced | f2-constant-sourcing | **NO to 001; YES to 003 and 009** — both carry written notifications appended 2026-09-18 |
| 4 | **The eclipse multiplier is 1.587×, not 8×**; 5,080 → **3,201 m²/MW (−34.8%)**; the "8× more productive" claim implies an **unstated reference CF of 18.6%** | f2-constant-sourcing | **NO to 001; YES to 003 and 009** |
| 5 | **001's 8 kg/m² placeholder was never declared as a class choice** — a crewed/ISS-class value (5.3–11) applied to a mass-optimized uncrewed platform (1.0–3.5), a **2.7–5× mismatch IN F2's OWN FAVOUR** | f2-constant-sourcing | **NO** |
| 6 | **DA-26's "19 of 19" is withdrawn** (FLY is a counterexample); count moves to **20 tested** | FLY recent-quarter + NVDA + VRT + LUNR + GOOG | **NO** |
| 7 | **DA-24's SATS instance is inverted** and its independence proof withdrawn | SATS recent-quarter | **YES — recorded in the constitution.** The only correction on this list that reached a pin. |
| 8 | **DA-23's `Clean` row narrowed to subtotal-level only; MRCY, UTHR, SATS removed** | BWXT, MRCY, UTHR, SATS, VRT | **YES — in the constitution** |
| 9 | **NVDA `UNEVIDENT`; VRT `UNEXERCISED`** | NVDA + VRT recent-quarter | **YES — in the constitution** |
| 10 | **The `2 ×` formula has TWO REGIMES** — parent SOUND `diff = 2 × Σ|stripped child|`, parent MIRRORED `diff = 2 × Σ|CORRECTLY-SIGNED child|`. *"The formula is numerically identical; the meaning is inverted."* Worked: RKLB Q2 2026 `NetIncomeLoss`, `diff = 10,654 = 2 × 5,327`, **tax NOT stripped** | RKLB | **NO** |
| 11 | **`computed` vs `reported` has NO default winner** — *"Four rows, four different resolutions, ONE filing … `NetIncomeLoss` → NEITHER"* | RKLB | **NO** |
| 12 | **A figure may not be sourced from a linkbase `LABEL`** — a twelve-year-stale AND figure-bearing fabrication vector. A label reads *"Preferred Stock; 5,000 shares authorized … at December 31, 2014 or 2013"* against a filed **100,000,000 authorized / 40,951,250 issued**; PP&E's label says *"net of $32,412 and $28,145"* against filed **(90,865) / (65,585)** | A25 | **NO** |
| 13 | **The weight rule LICENSES at w = −1 and CANNOT CERTIFY** — proven powerless on bidirectional concepts by **ONE concept at RKLB in ADJACENT PERIODS**: `IncomeTaxExpenseBenefit` is correct at Q2 2026 and stripped at FY2025, **at the same arc weight** | A26 | **NO** |
| 14 | **A THIRD CASE EXISTS: SINGLE-MEMBER SUBSTITUTION** — understating by **69.4%**; signature `computed = 2 × reported, diff = reported` | A26 | **NO** |
| 15 | **The registered identity `gross profit − opex = operating_income` is FALSE at UTHR by exactly cost of sales, six of six periods** — `CostsAndExpenses` INCLUDES cost of sales, and **001's AMGN check silently used opex NET of cost of sales** | A27 | **NO** |
| 16 | **The subtotal sign axis is `UNEXERCISED` on BOTH sides at UTHR/AMGN** — **61** UTHR and **61** AMGN facts, all positive | A27 | **NO** |
| 17 | **A contaminant inside a filed subtotal is ABSORBED** — 193 of the 827 Q2 improvement = **23.3%**; item as share of the operating result **1.4 / 0.4 / 20.1 / 23.6%** | A28 | **NO** |
| 18 | **`validate_calculation` has FOUR demonstrated failure modes** — `pass` on a wrong-signed value; `pass` when BOTH sides were stripped; **ZERO ROWS** on a filed concept; **93% false positives when it fails** | SATS, MRCY, VRT, SPCX | **NO** |
| 19 | **The test must be run on the COMPARATOR, not only the subject** — VSAT returns **10 pass / 1 warn / 19 fail = 63.3%** against SATS' **34.6%**, and **11 of VSAT's 19 failures carry the `2 ×` fingerprint NINE EXACT TO THE THOUSAND** | A30 | **NO** |
| 20 | **VSAT's Q1 slot carries a TWELVE-MONTH duration**; the served row overstates **3.97×**; correct quarter DERIVED **1,171,288**, so **VSAT is 0.32× SATS, not 1.27×** | A30 | **NO** |
| 21 | **A new failure mode: DIMENSION-BLIND JOINING** — SATS `OperatingIncomeLoss` `computed` **3,657,411** = consolidated revenue **3,667,489** − eliminations **10,078**, compared against `reported` **173** = the **ELIMINATIONS COLUMN's** value while consolidated is **392,847** | A30 | **NO** |
| 22 | **A clean tie-out is not evidence of a stable boundary** — intersegment revenue collapsed **71,592 → 9,905 = −86.2%**; one segment produced **112.5%** of the entire consolidated improvement; **63.4%** cost cessation and **54.1%** depreciation relief | A30 | **NO** |
| 23 | **001's DA-23 clearance is REFUTED for GOOG, IRDM, VRT, UTHR, NVDA** — and not vacuously | GOOG, IRDM, VRT recent-quarter | **NO** |
| 24 | **MRCY's edge case is retested and REFUTED** — 001 ran the identity on **the period it was reporting** and not on **the period it was comparing against**; the reported period is one of the two filed-positive ones, so it passed **by construction**. *"A detector run only on the subject of a comparison cannot detect a comparison error."* 001's `−98.6%` reproduces **only from the stripped comparator**; on filed signs the movement is **+19,907 favourable and the percent change is UNDEFINED, because it crosses zero**; the prior-year margin is filed **(2.1)%, so the movement is +2.1 points of IMPROVEMENT**; and the `—` for prior-year gross profit **hides a filed 254,494 = 27.9%** | MRCY recent-quarter ([📄 MRCY 10-Q p.4](https://agentii.ai/v/MRCY/sec202/4)) | **NO** |
| 25 | **001's DA-23 clearance for BWXT is CIRCULAR and does not discharge it** — a `$90.7M` term appears **in no BWXT filing**; the check closed and was a back-solve | BWXT | **NO** |
| 26 | **RKLB's realized-$/kg correction: 001's published numbers are 1.79×–2.62× too low**, four of four periods | RKLB unit-economics | **NO** |
| 27 | **MSFT's "8×" and "dwarfs" do not survive**; pessimistic case **0.74×–1.04×** | MSFT recent-quarter | **NO** |
| 28 | **VOYG's gross-profit-bound "violation" is a plain DA-23 sign strip** — `−51.408 < +4.457` violates nothing; the bound fires on **16 of 17 periods, continuously since FY2024**, not three | VOYG + constitution §DA-23 detector 2 | **YES — in the constitution** |
| 29 | **A zero from a `us-gaap:` query is evidence about the TAG, not the filing.** `GrossProfit` returns **0 facts** AND plain `Revenues` returns **0 facts** at BWXT (the filed concepts are `RevenuesFromExternalCustomers` / `RevenueFromContractWithCustomerExcludingAssessedTax`) | BWXT | **NO** |
| 30 | **`fiscal_year_end_month_source` is a populated-but-wrong registry field** at HAWK — a defect class of its own under the A4 discriminator | HAWK | **NO** |
| 31 | **PIL-2's source class cannot be recorded** — `citation_url_wellformed` is level `fail` and admits only agentii.ai URLs, so **a passing evaluation would be unrecordable** | f2-constant-sourcing | **NO — a spec/contract defect, escalated** |
| 32 | **PIL-5's denominator is unstated** | thesis.md L308 + §1 above | **NO — a spec defect, escalated** |

**Propagation count: 3 of 32 reached a pin** (items 7, 8/9, 28 — all three landed in the
constitution). **The other 29 are recorded in artifacts and absorbed nowhere.**
**Worst-in-class: the UTHR `72.0`, derived three times and absorbed zero times.**

**Why the aggregate matters more than any single row.** A stale upstream is *supposed* to be
visible: 001 is pinned at **1.2.0** while the constitution is at **1.5.0**, and 002's own
phase 3 produced a **1.4.0 → 1.5.0 MINOR bump**. `upstream_stale: "001@1.2.0"` is
**contract-required and check-enforced** — `check_citations.py` fails any 002 artifact whose
`upstream_stale` is not exactly that string. **The field is therefore present in all 41
artifacts, correct in all 41, and consumed by none of them.** The programme built a staleness
signal, made it mandatory, and then read it as a label rather than a trigger.

### 4.3 The cross-thesis correction — delivered to thesis 003

002 delivered a correction to **thesis 003** on the SATS side. **The delivery named the wrong
contaminant AND the wrong sign.** The corrected finding: SATS' 2025 Q3 operating income at
**4.6× revenue** is a **non-cash impairment charge**, not a spectrum-licence sale — so a
downstream thesis that treated it as a realized gain and sized a spectrum-value claim on it
would be **wrong in the direction that flatters the thesis**. Recorded as delivered, with the
correction carried as the second-order item: **the correction itself needed correcting**, and
003 holds the first version.

### 4.4 ⚠️ Structural hazard: `report-input.md` is TWO DOCUMENTS

> **`theses/001-technology-baseline/report-input.md` is 7,025 lines and contains 001's report
> at L1–965, then 44 embedded downstream artifacts from L966.**
> **So a bare line citation into it is ambiguous by default — and the ambiguity is not
> flagged anywhere in the file.**

The worked instance: **the `87.3%` a reader would naturally attribute to 001 is the 1239
artifact's.** A citation of the form `report-input.md:1239` resolves to an *embedded artifact*,
not to 001's report — and the same line-number shape resolves to the report above L965. **This
is a citation-hygiene defect with the same structure as DA-30: two documents under one
identifier, collapsed without a discriminator field.** Remedy: always cite the embedded
artifact by name, or cite the report by a line number below 966.

### 4.5 The A29 obligation, and what "propagated" must mean going forward

A29's own text names the obligation: **a correction that is recorded and never propagated is
indistinguishable, in effect, from one never made.** The mechanism this thesis needs is a
**consumer for `upstream_stale`** — the pin exists, is mandatory, and currently does nothing.
Until a gate reads it, every correction in §4.2 will land where this one landed: in an
artifact, correctly, and in no one's hands.

---

## §5 — The disposition census, and what could not be resolved

### 5.1 Totals by class, with the named resolving source for each

| Class | Count | Named resolving source | Items |
|---|---|---|---|
| **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** | **9 named** | each carries the disclosure that would resolve it | 001 PIL-4's value-per-kg and cost-per-kg (**Varda is private**; UTHR's programme economics are immaterial to a **$783M/quarter** issuer and never broken out); 001 PIL-4's listing event (**Form S-1 / 8-K**); BWXT's radiator areal density (**monitor disclosure**); BWXT/MRCY heat-pump COP (**literature/hardware review — outside every registry skill**); MRCY's product/capability margin (**withheld by policy; no source exists by design**); UTHR's per-unit metrics (**genuine absence from source**); RKLB's R&D "net" contra magnitude; SPCX unit-economics; VRT unit-economics; GOOG secular-trends |
| **`UNRESOLVABLE-FROM-PLATFORM`** | **12 named** | record as a finding about **platform reach**, never as absence of evidence | SPCX DA-23 coverage hole at **MRK, BMY and WWD** (`OperatingIncomeLoss` absent or segment-only — **no detector can run at all**); `list_coverage` `record_count` 0; YSS DA-26 (**10-K ingestion pending**); IRDM DA-25 (**datum class**); IRDM DA-28 (**coverage window**); UTHR/MRK's third 72% → **`UNVALIDATED-BY-PLATFORM`**; MSFT residuals (`IncomeTaxExpenseBenefit` `computed` 70,454 / 35,780); DA-27's population at RKLB, VRT, BWXT, LUNR, UTHR; **001 PIL-5's terrestrial denominator** (colocation and greenfield costs are **commercially licensed**); **001 PIL-6's FCC IBFS / ITU Space Network List** |
| **`REACHABLE-BUT-NOT-RECORDABLE`** *(third situation, proposed at A22 — NOT yet a registered class)* | **2** | the datum **is** reachable; the **contract** cannot record it | **PIL-2's `peer_reviewed_literature_or_flown_hardware_disclosure`** (a passing evaluation would be unrecordable); the citation contract's URL pattern, which admits only `agentii.ai` |
| **`UNVALIDATED-BY-PLATFORM`** *(A5; refined to `PARTIALLY-VALIDATED-BY-PLATFORM` at IRDM, scoped to the missing linkbase ARC)* | **3** | the validator ran and its result is not admissible | UTHR/MRK's third 72%; IRDM's absent ARC; `validate_calculation`'s four failure modes wherever a `pass` was relied on |
| **`UNEXERCISED` / `UNEVIDENT` / `NOT TESTABLE` with a named kind** | **31** | the kind's own remedy (§2.2) | DA-23 NVDA (UNEVIDENT), DA-23 VRT (UNEXERCISED); DA-25 IRDM (kind 5), DA-25 VRT (no object), DA-25 GOOG (kind 7); DA-26 SPCX, YSS (kind 1), HAWK (no 10-K); DA-27 SATS, VRT, RKLB, LUNR, VOYG, BWXT, BA (kind 4); DA-28 IRDM (kind 6), SATS/VRT (kind 2); DA-29 and DA-30 across **10 unengaged issuers each** |
| **`EVALUABLE — blocked by EFFORT`** | **1** | on-platform work | **001:PIL-3's ~19 issuer Item 1A reads** |

### 5.2 The three situations, distinguished

The register previously conflated two failure modes; this thesis proposes a **third**, and the
distinction is the operative one:

1. **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — *the disclosure does not exist.* Remedy: name the
   specific disclosure that would resolve it; monitor. **This is a finding about the world.**
2. **`UNRESOLVABLE-FROM-PLATFORM`** — *the data is public but unreachable, licensed, or in a
   registry the platform does not carry.* Remedy: record it as a finding about platform reach.
   **This is a finding about the instrument.**
3. **`REACHABLE-BUT-NOT-RECORDABLE`** — *the datum is reachable and the contract cannot record
   it.* Remedy: **amend the contract.** **This is a finding about the programme's own rules**,
   and it is the one that cannot be resolved by any amount of research. PIL-2 is its canonical
   case: the constants are reachable by direct search, **no skill in this registry can read
   them**, and even if one could, **a passing evaluation would be unrecordable** because
   `citation_url_wellformed` is level `fail` and admits only agentii.ai URLs.

**A pillar in any of the three states is not dropped and not failed.** It is carried in
`known-open` with the specific disclosure or source that would resolve it.

### 5.3 The seven kinds, with counts

| Kind | Count of instances recorded | Remedy class |
|---|---|---|
| 1 — ingestion absence | 2 (YSS 10-K; SPCX no annual row) | ingest |
| 2 — genuine absence from source | 6 (SATS, VRT, IRDM-listing, UTHR, Varda, 001 PIL-4 value-per-kg) | name and monitor |
| 3 — validator-completeness | 2 (PIL-2 source class; the citation contract) | **amend the contract** |
| 4 — mechanism-population identity | 8 (DA-27 across every December-year-end issuer; PIL-5's denominator) | **exclude from the denominator** |
| 5 — ingestion absence of a datum class | 4 (IRDM DA-25; PIL-5 terrestrial; PIL-6 FCC/ITU; MRK/BMY/WWD coverage hole) | name the class |
| 6 — coverage window | 2 (IRDM DA-28; 001's three-year presentation) | widen |
| 7 — **detector gap at a computable datum** | 3 (DA-25 GOOG; DA-27 ratio layer; MSFT residuals) | **write the detector** |

### 5.4 What could NOT be resolved — and why none of it is a silent gap

**Every falsifier carries a named resolving source; PIL-7's metric is 0** (§2.5). The items
that could not be resolved are enumerated with their classes above, and the three that are
**irreducible** are stated plainly:

1. **SPCX's facility draw is not disclosed.** PIL-4's expected reading sits **exactly at
   threshold** and cannot be resolved further from public sources. The input is **a
   transcript, not a filing** ([📄 SPCX transcript p.4](https://agentii.ai/v/SPCX/ect1/4)),
   and the universe's second-largest relevant issuer discloses nothing: Alphabet's entire
   SpaceX-related disclosure across **216 filing pages and 17 transcript pages** is a
   **$94.1B equity stake** and **$99.0B of earnings**, with `Suncatcher`, `satellite`, `orbit`
   and `orbital` returning **zero** hits ([📄 GOOG 10-Q p.15](https://agentii.ai/v/GOOG/sec156/15)).
2. **The FCC IBFS and ITU Space Network List are not on the platform.** 001:PIL-6's
   falsifier is unreachable *in principle* for this instrument.
3. **`MRK`, `BMY` and `WWD` file no consolidated `OperatingIncomeLoss`** — at those three
   issuers **no DA-23 detector can run at all**, and absence must be recorded as
   `UNRESOLVABLE-FROM-PLATFORM`, never as a passed check.

**One item could not be verified in this ledger itself and is recorded as such: DA-29 and
DA-30 are engaged by 7 of 17 issuers.** The remaining **10 issuers × 2 entries = 20 cells**
are **UNEXERCISED by absence of engagement**, and this ledger does **not** count them as
clean. That is a coverage gap in the register's application, stated as a number.

---

## §6 — The amendment queue's disposition

### 6.1 Thirty items queued, NONE registered

**`AMENDMENTS-PENDING.md` holds A1–A30. Not one is registered in the constitution, and not
one has been executed.** This ledger's job is to report them for the gate-5 budget confirm —
**as the 1.3.0 precedent did — not to execute them.** What each would change, and which
artifact produced it:

| # | Would change | Produced by |
|---|---|---|
| **A1–A4** | register additions or scope generalisations — **no principle, axiom, bound, sector bias or disposition class changes** | Phase 3 registrations |
| **A5** | adds `UNVALIDATED-BY-PLATFORM` as a disposition label (refined to `PARTIALLY-VALIDATED-BY-PLATFORM` at IRDM, scoped to the missing linkbase ARC) | IRDM |
| **A6** | DA-27's denominator rule — **mechanism-population identity**: December-year-end issuers are excluded from the denominator, and "not testable" must not be reported as clean | SATS, VRT, RKLB, LUNR, VOYG, BA, BWXT |
| **A7** | the DA-24 independence requirement — an artifact asserting independence must supply an admissible measurement | SATS |
| **A8** | the weight rule's **licence ≠ certification** boundary | BWXT, VRT, RKLB |
| **A9** | falsified as a complete statement — a **THIRD CASE EXISTS: SINGLE-MEMBER SUBSTITUTION**, understating by **69.4%** | RKLB |
| **A13** | the "not testable" heading corrected from **FOUR to SEVEN** kinds | `IRDM × competitive` (caught the heading/table mismatch) |
| **A17** | DA-23's power boundary — a clearance is admissible only on **BIDIRECTIONAL** concepts **and** only if it exhibits a filed-negative instance | IRDM |
| **A22** | the **third situation**: `REACHABLE-BUT-NOT-RECORDABLE` | f2-constant-sourcing |
| **A23** | PIL-7's classification table, with the EVALUABLE-PROXY requirement: *"not a verdict on reachability, but a means of testing anyway"* | SPCX risk |
| **A24** | **the `2 ×` formula has TWO REGIMES**; `computed` vs `reported` has **no default winner** | RKLB |
| **A25** | **"A figure may not be sourced from a linkbase `LABEL`"** | the linkbase-labelling case |
| **A26** | A8/A17 completed; A9 falsified as complete; new signature `computed = 2 × reported, diff = reported`; the largest RKLB error was **not** a sign error | RKLB |
| **A27** | the registered identity `gross profit − opex = operating_income` is **false at UTHR by exactly cost of sales, six of six periods**; the sign axis is **UNEXERCISED on both sides** | UTHR |
| **A28** | **a contaminant inside a filed subtotal is ABSORBED by it**; a zero residual is exactly what that produces; otherwise the verdict is **`UNTESTED AT THIS LEVEL`** | SPCX risk |
| **A29** | **a correction recorded and never propagated is indistinguishable from one never made**; needs a **consumer for `upstream_stale`** | this ledger's §4 |
| **A30** | test the **comparator**, not only the subject; **dimension-blind joining**; a clean tie-out is not evidence of a stable boundary | A30's own case |

**Note the queue's own line: "No principle, axiom, bound, sector bias or disposition class
changes. A1–A4 are all register additions or scope generalisations. Every falsifier in
`spec.md` stands as written, with the single exception already recorded: PIL-5's denominator
is unstated … and PIL-2's source class cannot be recorded under the citation contract — both
are specification defects, not register items, and both go to Phase 7."** §1 and §2 above are
that Phase 7 disposition.

### 6.2 What the SemVer rule implies

The constitution's rule, at **1.5.0**:

> **MAJOR** = a principle removed or incompatibly redefined. **MINOR** = a principle added or
> substantially extended. **PATCH** = wording only. **MAJOR/MINOR bumps mark
> `constitution_pin`-older theses `stale` and dispatch re-examination after the gate-5 budget
> confirm. PATCH never triggers review.**

Applied to the queue, **three classes separate cleanly**:

| Class | Items | SemVer | Why |
|---|---|---|---|
| **PATCH** | A13 (heading FOUR → SEVEN), A25's wording, A30's wording | **PATCH** | wording and enumeration only; no test changes behaviour. **A13 is the clearest PATCH in the queue** — the table already carried seven rows and only the heading was wrong, so no artifact's result moves. |
| **MINOR** | **A22** (a third disposition situation), **A23** (PIL-7's classification vocabulary and the proxy requirement), **A5** (`UNVALIDATED-BY-PLATFORM`), **A24** (the two-regime reading of `2 ×`), **A26** (a third substitution case), **A27** (a registered identity is false), **A28** (`UNTESTED AT THIS LEVEL`), **A29** (a correction-propagation obligation), **A6/A7/A8/A17** (power and denominator boundaries) | **MINOR** | each **adds or substantially extends a principle**. **A27 is the strongest MINOR case**: it does not remove `gross profit − opex = operating_income`, it establishes that the identity is **false by exactly cost of sales at a whole class of issuers** — a substantial extension of the register's scope. |
| **MAJOR** | **none** | — | **no item removes a principle or redefines one incompatibly.** The queue says so in terms, and this ledger's reading agrees. |

**Consequence if the queue is accepted as classified: one MINOR bump, 1.5.0 → 1.6.0 (plus
PATCH items that may ride the same bump, since PATCH never triggers review), and NO MAJOR
bump.** Under the rule, a MINOR bump **marks `constitution_pin`-older theses `stale` and
dispatches re-examination after the gate-5 budget confirm.** Thesis 002 is pinned at **1.5.0**
and would be marked stale by its own amendment; thesis 001 is pinned at **1.2.0** and is
**already stale** on three separate bump events.

**The budget consequence is the operative one.** All 41 artifacts are pinned at 1.4.0 or
1.5.0. **A MINOR bump marks every one of them stale and dispatches re-examination.** The
gate-5 budget confirm must therefore price **42 artifacts of re-examination** — not one
correction — and this ledger's §4 shows what happens when a correction is not priced: **the
UTHR `72.0` was derived three times and absorbed zero times under exactly that condition.**

### 6.3 The two obligations carried forward, undistributed

`AMENDMENTS-PENDING.md` records two items under *"already registered, obligation NOT yet
discharged"*:

1. **DA-29 / DA-30 (added at 1.5.0).** The constitution says the obligations these two place
   on the **23 pre-existing artifacts** are *"not separately dispatched — folded into Phase
   7's validation ledger."* **They are discharged here, by census rather than by re-running
   artifacts** (§3.2–§3.4) — and the discharge is honest about its own limit: **DA-29 and
   DA-30 are engaged by 7 of 17 issuers, and the other 10 are UNEXERCISED, not clean.**
2. **DA-23's component-level census.** BWXT established that an issuer can be **clean at
   every subtotal while a component of the same statement is sign-corrupted.** **Only BWXT
   was tested at component level.** The remaining issuers are **subtotal-level-verified only**,
   and **the census statistic cannot see the difference.** Recorded as a **known understatement
   in the register's coverage**, not as a clean result.

### 6.4 Recommendation for the gate-5 budget confirm

**Reported, not executed.**

1. **Classify the queue: 3 PATCH, 27 MINOR, 0 MAJOR.** One MINOR bump, 1.5.0 → 1.6.0.
2. **Price the re-examination at 42 artifacts**, and note that 001 is already stale on three
   events — so the incremental cost of this bump is *lower* than it appears and the *unpaid*
   cost of the previous three is higher.
3. **Build the `upstream_stale` consumer before the bump**, not after. A29's mechanism is the
   only thing standing between a corrected figure and a third silent derivation.
4. **Amend `spec.md` for PIL-5's denominator and the contract for PIL-2's source class**
   before any downstream thesis reads either falsifier. **An unrecordable passing evaluation
   and an unfalsifiable threshold are the same defect**, and 002 is the thesis whose whole
   purpose was to detect it.

---

## §7 — What this ledger could not do

Stated plainly, because a ledger that closes cleanly while testing nothing is the failure mode
this thesis was built to catch.

1. **It could not select PIL-5's denominator, because selecting one is the defect.** It
   published the ladder instead, and §1.6 states the verdict under each.
2. **It could not adjudicate 21 of 001's 27 register claims** — and says so with the number
   rather than reporting a share (§1.4).
3. **It could not verify the `packaging/targets/*` contradiction** between VRT's and GOOG's
   ratio artifacts. Both cannot stand; this ledger will not pick one (§3.4).
4. **It could not engage DA-29 and DA-30 for 10 of 17 issuers**, because no artifact did
   (§3.2). Those 20 cells are unexercised, not clean.
5. **It could not test any issuer at component level except BWXT.** The DA-23 census is a
   subtotal-level census and **cannot see** the defect that BWXT proved exists (§6.3).
6. **It could not resolve the facility draw, PIL-6's registries, or MRK/BMY/WWD's absent
   operating income** — three irreducible gaps, each with a named class (§5.4).
7. **It did not execute a single amendment.** A1–A30 are reported for the gate-5 budget
   confirm, as the 1.3.0 precedent did.

**And the one result that is not a limitation.** The falsification in §1.6 stands: **on the
readings where the basis matters, the pillar fails, and the two come apart by 46.47
percentage points on a single ratio.** That is the thesis's finding about itself, and it is
the reason the ledger is the primary artifact rather than a summary of the others.
