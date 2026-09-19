---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: cross
ticker: cross
skill: synthesis
mode: methodology
generated_at: 2026-09-19T17:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-01
    chosen_reading: "The basis register, applied without exception: A = customer list price; A' = issuer-realized variant (SPCX-specific, Launch-Services-only boundary at 002; the RKLB analogue is revenue-per-launch and is tagged A'); B = marginal cost per launch, the ONLY basis that tests an F5 architecture floor; C = fully-loaded amortized. Every cell in the matrix carries its basis letter AND its denominator convention. A cell that is empty is recorded empty with a reason and a resolving source, never filled by a neighbouring basis."
  - da_id: DA-02
    chosen_reading: "Denominator orbit. LEO is the denominator orbit on every row of the matrix, and where a figure is restated on a second denominator the row says so. GTO is ~3x LEO per kg, so a GTO-denominated figure would silently inflate. SPCX's mass-to-orbit metric is orbit-AGNOSTIC - it counts delivered kilograms without naming the orbit - and is flagged as such wherever it is used."
  - da_id: DA-03
    chosen_reading: "Architecture label. Each vehicle carries exactly one of fully_expendable, partially_reusable, fully_reusable. A bare 'reusable: true' fails and appears nowhere. Starship is the one vehicle carried on two architecture rows because the declared architecture and the as-flown architecture differ; the divergence is stated rather than resolved."
  - da_id: DA-06
    chosen_reading: "Price vs cost. Basis A and basis B are never reported as a single spread without naming both letters. Electron is the only vehicle in the universe where both are filed, and the pair is reported as a pair."
  - da_id: DA-07
    chosen_reading: "Capacity vs delivered mass. Electron's 300 kg and Neutron's 13,000 kg are CAPACITY figures; SPCX's 132 t customer payload and 1,041 t mass to orbit are DELIVERED figures. The matrix's denominator column records which it is, because the two are not interchangeable and the difference is what produces the 12.8x spread in section 6."
  - da_id: DA-08
    chosen_reading: "What counts as a launch. SPCX includes suborbital flight tests inside its launch count; RKLB's HASTE missions are suborbital testbeds. Both inflate a launch-count numerator with missions that carried zero kilograms to LEO. The matrix records mission counts only alongside the mission mix that produced them."
  - da_id: DA-21
    chosen_reading: "Issuer-drawn segment boundaries. SPCX's Space segment revenue is the CUSTOMER boundary, filed verbatim, and Starlink launch costs are capitalized into satellites in a different segment. Any SPCX ratio that divides segment revenue by all-launch count crosses the boundary the issuer drew, and is marked non-comparable wherever it appears."
  - da_id: DA-23
    chosen_reading: "Platform serves a filed negative as a positive of identical magnitude (absolute-value stripping, not inversion). The detector is the component identity: where components sum to the parent only after magnitude is applied, the sign was stripped. The census is carried in section 12 and the register entry is not re-derived here."
  - da_id: DA-25
    chosen_reading: "Normalised per-unit metrics are not reproducible from the audited tables. Both legs of the per-unit ratio are quarantined where the normaliser is a label rather than a quantity. FLY's '1,000-kilogram payload class' is the limiting case: a normalisation over a class label whose own filed width is 6x."
  - da_id: DA-27
    chosen_reading: "Fiscal-period labels. SPCX's 8-K Space table files five columns under one header with no per-value label; the order was RECOVERED by three exact reconciliations rather than assumed. Period basis is stated on every SPCX throughput figure, because the three-month and six-month bases give opposite-signed trends for the same metric."
  - da_id: DA-29
    chosen_reading: "A reconciliation that closes is not thereby a check; if a term appears nowhere in the source, the check is a back-solve. The 8-K's payload components sum to the filed mass-to-orbit total within 1 tonne on four of five columns - recorded, not smoothed. The $5,567/kg register low end recomputes to $5,568/kg with no filed explanatory term, so it is UNRESOLVED rather than 'a rounding difference'."
  - da_id: DA-30
    chosen_reading: "Two bases on one concept collapsed without a basis field. This artifact is built to be the antidote: four bases x five vehicles = 20 cells, each carrying its basis letter and denominator convention, with the competing readings reported side by side rather than one adopted. The 12.8x spread and the two F5b floor readings are the two confirmations carried here."
evidence_grade: DEMONSTRATED
citations:
  - figure: "Revenue and Cost Per Launch: Q2 2026 revenue per launch $9.1M and cost per launch $4.4M; Q2 2025 $7.9M and $5.0M; and the HASTE mission-mix sentence - two of six Electron missions in the quarter were suborbital testbeds carried inside both the revenue and the launch-count numerator"
    ticker: RKLB
    citation_id: sec109
    page_no: 37
    form_type: 10-Q
    url: https://agentii.ai/v/RKLB/sec109/37
    located_via: read_source_pages
  - figure: "Q1 2026 and Q1 2025 revenue per launch $9.3M / $7.1M and cost per launch $5.4M / $5.7M, filed natively"
    ticker: RKLB
    citation_id: sec104
    page_no: 31
    form_type: 10-Q
    url: https://agentii.ai/v/RKLB/sec104/31
    located_via: read_source_pages
  - figure: "Electron filed only as \"up to 300 kg\" to low Earth orbit across inclinations from 38 to 120 degrees - a CEILING, with no mass-to-orbit metric filed in any period; Neutron \"approximately 13,000 kg for reusable configuration\""
    ticker: RKLB
    citation_id: sec87
    page_no: 8
    form_type: 10-K
    url: https://agentii.ai/v/RKLB/sec87/8
    located_via: read_source_pages
  - figure: "Electron \"up to 300 kg\" - the second of two filing instances of the ceiling"
    ticker: RKLB
    citation_id: sec87
    page_no: 7
    form_type: 10-K
    url: https://agentii.ai/v/RKLB/sec87/7
    located_via: read_source_pages
  - figure: "Basis C is structurally unconstructible: \"Management does not regularly review either reporting segment's total assets or operating expenses. This is because in general, the Company's long-lived assets, facilities, and equipment are shared by each reporting segment.\""
    ticker: RKLB
    citation_id: sec109
    page_no: 33
    form_type: 10-Q
    url: https://agentii.ai/v/RKLB/sec109/33
    located_via: read_source_pages
  - figure: "Launch Services revenue $44,586 + Space Systems $189,480 = $234,066 = filed total revenues; Products $0 / Services $44,586 for Launch Services"
    ticker: RKLB
    citation_id: sec109
    page_no: 32
    form_type: 10-Q
    url: https://agentii.ai/v/RKLB/sec109/32
    located_via: read_source_pages
  - figure: "FY per-launch series and the FY2023 cost figure filed as excluding a $2.1M retention-credit benefit and a $4.1M contract-loss-reversal benefit"
    ticker: RKLB
    citation_id: sec87
    page_no: 46
    form_type: 10-K
    url: https://agentii.ai/v/RKLB/sec87/46
    located_via: read_source_pages
  - figure: "Space segment table, five columns in the order [Q2 2026, Q1 2026, Q2 2025, H1 2026, H1 2025]: customer launches 10/7/9/17/21; total launches 38/40/46/78/84; customer payloads 87/45/88/132/163 t; mass to orbit 485/556/652/1,041/1,102 t; launch services revenue $648/$330/$490/$978/$1,056M; Space revenue $962/$619/$746/$1,581/$1,611M; cost of revenue $329/$281/$330/$610/$627M; R&D $1,076/$930/$693/$2,006/$1,219M; SG&A $99/$70/$87/$169/$175M; and \"reduce the cost to orbit by 99% or more relative to the historical average\""
    ticker: SPCX
    citation_id: sec7
    page_no: 7
    form_type: 8-K
    url: https://agentii.ai/v/SPCX/sec7/7
    located_via: read_source_pages
  - figure: "Mass-to-orbit definition (total kilograms of payload delivered from all successful orbital and flight tests, excluding failed or scrubbed attempts); \"Our Space segment revenue only reflects our customer launches and customer activities.\"; Falcon launches 37/45/77/81 with Starship 1/1/1/3; \"To date, all Starship launches have been classified as internal.\""
    ticker: SPCX
    citation_id: sec8
    page_no: 35
    form_type: 10-Q
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "\"For launches of our Starlink satellites, the Company does not recognize any inter-segment revenue, rather those launch costs are capitalized in satellites in Property, plant, and equipment, net.\""
    ticker: SPCX
    citation_id: sec8
    page_no: 36
    form_type: 10-Q
    url: https://agentii.ai/v/SPCX/sec8/36
    located_via: read_source_pages
  - figure: "Revenue mix by type: Launch Services 67.4% against Launch and Development 32.6%; the Space segment cost-of-revenue definition including \"second stages flown ... launch operations and overhead, depreciation (inclusive of booster, Merlin engine, and fairing depreciation) ... launch testing and overhead, engineering costs, inventory excess and obsolescence, shared costs incurred in the production of launch hardware\"; R&D costs \"mainly relate to the development, build, and testing of Starship\""
    ticker: SPCX
    citation_id: sec8
    page_no: 37
    form_type: 10-Q
    url: https://agentii.ai/v/SPCX/sec8/37
    located_via: read_source_pages
  - figure: "\"Starship aims to quadruple payload capacity and reduce launch costs by 10x compared to our Falcon 9 rocket\" (Bret Johnsen)"
    ticker: SPCX
    citation_id: ect1
    page_no: 3
    form_type: earnings_call_transcript
    url: https://agentii.ai/v/SPCX/ect1/3
    located_via: read_source_pages
  - figure: "\"We are the only U.S. company with a liquid-powered orbital launch vehicle in the 1,000-kilogram payload class.\" and \"We operate as a single reportable segment\""
    ticker: FLY
    citation_id: sec21
    page_no: 34
    form_type: 10-Q
    url: https://agentii.ai/v/FLY/sec21/34
    located_via: read_source_pages
  - figure: "Alpha described only as a \"1,000-kilogram payload class\" - the class label appears four times across two filings and is never accompanied by a mass, an orbit, an inclination or a configuration"
    ticker: FLY
    citation_id: sec16
    page_no: 7
    form_type: 10-K
    url: https://agentii.ai/v/FLY/sec16/7
    located_via: read_source_pages
  - figure: "\"Alpha is the only provider of small size launch that has achieved orbit and addresses a critical gap in the market in the 1,000 kilograms category\"; \"the global market right-sized toward satellites between 200 kilograms to 1,200 kilograms, according to analysis by BryceTech in 2025\" - the category's own filed width, 6x"
    ticker: FLY
    citation_id: sec16
    page_no: 9
    form_type: 10-K
    url: https://agentii.ai/v/FLY/sec16/9
    located_via: read_source_pages
  - figure: "Launch revenue recognized on \"the initiation of the launch\" - POINT IN TIME, against RKLB's over-time HASTE recognition"
    ticker: FLY
    citation_id: sec21
    page_no: 16
    form_type: 10-Q
    url: https://agentii.ai/v/FLY/sec21/16
    located_via: read_source_pages
---

# The launch cost curve — vehicle × architecture × basis, with applied floors, grades and named absences

**Finding.** This is the thesis's per-kilogram cost curve, stated as a matrix rather than a line because the
curve's only measured point is a **single cell**: **Electron basis B, `DEMONSTRATED`, the only such cell on the
table.** Across five vehicles and four bases — **20 cells** — the census is
**2 `DEMONSTRATED` · 2 `DEMONSTRATED`-figures-with-`MODELED`-division · 2 `CLAIMED` · 1 `MODELED` · 13 ABSENT.**

**And the one measured point moves the wrong way.** When Electron's denominator is corrected for the filed
mission mix, cost per launch **fell 12.0%** ($5.0M → $4.4M) while cost per kilogram to LEO **rose 32.0%**
($16,667 → $22,000/kg). `0.88 × 1.50 = 1.32`, exact. **The disclosed improvement is a denominator artefact in
the OPTIMISTIC direction**, and the sector's cost conversation is conducted on architectures whose floors
(F5a, F5b) are `MODELED`, while the one tier with a `DEMONSTRATED` price (F5c) is the tier the conversation
treats as obsolete.

## 0. How to read this table

**Five rules, and every cell in §1 obeys all five.**

| # | Rule | Consequence here |
|---|---|---|
| 1 | **Every cell carries a basis letter AND a denominator convention** (DA-01, DA-30) | A `$/kg` with no letter is not reported, even where it is correct arithmetic |
| 2 | **A `MODELED` input can never satisfy a falsifier** | The floors are fences, not results; only basis B tests an F5 floor, and basis B is `DEMONSTRATED` on exactly one vehicle |
| 3 | **`PRESENCE ≠ ABSENCE`** — a test that could not run is `UNEXERCISED`, never `CLEAN` | 13 of 20 cells are `UNEXERCISED`. Nothing on this table is evidence that an F5a or F5b floor holds |
| 4 | **Absences carry THREE disposition classes**, not two | Two are reachable by research; the third is not. §10 |
| 5 | **Capacity is not delivered mass** (DA-07) | The denominator column says which, because the difference is what produces the 12.8× spread in §6 |

**Basis register (DA-01).** `A` customer list price · `A′` issuer-realized variant (SPCX-specific
Launch-Services-only boundary; the RKLB analogue is revenue per launch) · `B` **marginal cost per launch — the
only basis that tests an F5 floor** · `C` fully-loaded amortized.

**Grades.** `DEMONSTRATED` — a filed figure, or arithmetic directly on filed cells · `CLAIMED` — an issuer or
third-party assertion · `MODELED` — our derivation. `DERIVED` appears nowhere on this table: every figure is
either filed or arithmetic on filed cells, and the divisions are flagged where the denominator convention is
ours.

**On the frontmatter's absent `unresolvable` flag.** The contract's `unresolvable_class` enum carries two
classes; this artifact's per-cell register carries **three**, and the third — `REACHABLE-BUT-NOT-RECORDABLE` —
is not representable in the enum. Rather than flatten three dispositions into two at the document level, the
flag is omitted and the register lives per-cell in §10. The artifact's central claim is a measurement, not a
declaration of unreachability.

---

## 1. THE MATRIX — 5 vehicles × 4 bases = 20 cells

Denominator orbit is **LEO** on every row (DA-02). `$/kg` figures are USD per kilogram to LEO.

| Vehicle | Operator | Architecture | F5 tier | Basis A | Basis A′ | Basis B | Basis C |
|---|---|---|---|---|---|---|---|
| **Electron** | RKLB | `fully_expendable` | **F5c** | **$45,500/kg `DEMONSTRATED`** | **ABSENT** — n/a | **$22,000/kg `DEMONSTRATED`** | ABSENT — permanent |
| **Falcon 9** | SPCX | `partially_reusable` | **F5b** | $2,939/kg `CLAIMED` — **denominator-failed** | **$7,448/kg** `DEMO`-figs / `MODELED`-div | $1,379–2,299/kg **`MODELED`** | $17,287/kg `DEMO`-figs / `MODELED`-div |
| **Starship** | SPCX | `fully_reusable` (declared) | **F5a** | **ABSENT** | **ABSENT** | **ABSENT** | **ABSENT** |
| **Neutron** | RKLB | `partially_reusable` | **F5b** | $3,846–4,231/kg `CLAIMED` | **ABSENT** — n/a | **ABSENT** — unflown | **ABSENT** — permanent |
| **Alpha** | FLY | `fully_expendable` ⚠️ **`DERIVED`** | **F5c** | **ABSENT** | **ABSENT** | **ABSENT** | **ABSENT** |

**Census, and it closes exactly:**

| Disposition | Cells | Count |
|---|---|---:|
| `DEMONSTRATED` | Electron A, Electron B | **2** |
| `DEMONSTRATED` figures / `MODELED` division | Falcon 9 A′, Falcon 9 C | **2** |
| `CLAIMED` | Falcon 9 A, Neutron A | **2** |
| `MODELED` | Falcon 9 B | **1** |
| **ABSENT** | Starship A/A′/B/C · Electron A′/C · Neutron A′/B/C · Alpha A/A′/B/C | **13** |
| | | **20** |

*⚠️ Within the ABSENT count, **two cells are `n/a` rather than missing** — Electron A′ and Neutron A′, since
A′ is defined as the SPCX-specific realized variant and has no RKLB counterpart. **So of the 20 cells, 18 are
real questions: 11 unanswered and 7 populated.** (13 ABSENT − 2 `n/a` = 11; and
2 + 2 + 2 + 1 = 7 populated.) **The `n/a` pair is not a disclosure failure and is not carried as one.** Note
also that **Electron's basis A is its realized revenue per launch** — no separate list price is filed — which
is why the cell is `DEMONSTRATED` rather than `CLAIMED`. And Alpha's `fully_expendable` architecture label is
`DERIVED` rather than filed (§2.2).*

**Read the matrix's shape before its values.** **One vehicle and one basis carry the curve's demonstrated,
floor-testing content** — Electron on basis B. Basis B is `DEMONSTRATED` on **1 of 5 vehicles**, and that count
**will not widen on current disclosures**: no other vehicle in this universe files a cost-per-launch figure on
any basis. The remaining demonstrated content is SPCX arithmetic (two cells in which filed figures are divided
by a denominator convention that is ours), one `MODELED` construction, and two claims.

**`Eclipse` (FLY, `partially_reusable`, unflown) is not a sixth row** because it has no filed payload, no
filed price and no flight; where artifacts in this thesis carry it, it is carried as a column of absences. Its
disposition is the same as Starship's: `UNEXERCISED`.

---

## 2. Architecture → F5 tier, and the tiers are exhaustive

Constitution pin **1.5.0**; the F5 split is at v1.3.0, which **closed the coverage gap** — F5a and F5b had
covered only the two reusable architectures, leaving the fully expendable class unbounded. **That gap is
closed. This artifact does not re-raise it.**

| Tier | Architecture | Floor | Derivation | Floor grade | `DEMONSTRATED` price? |
|---|---|---|---|---|---|
| **F5a** | `fully_reusable` | Propellant mass × price → **$46–92/kg** at 100 t | ~4,600 t propellant at $1–2/kg = $4.6–9.2M ÷ 100,000 kg | **`MODELED`** | **No** |
| **F5b** | `partially_reusable` | Expended upper stage → **$920–2,299/kg** at 8,700 kg *[two readings — §2.1]* | the recoverable stage returns; the expended second stage does not | **`MODELED`** | **No** |
| **F5c** | `fully_expendable` | Whole vehicle manufactured once and expended | entire vehicle cost, no amortisation object | **MEASURED at Electron** | **Yes — the only one** |

**Contract rule `floor_architecture_consistency`:** the three tiers map one-to-one onto
`{fully_reusable, partially_reusable, fully_expendable}`. **All three appear on this table, all three are
populated, and no vehicle is left outside them. `tier: none` is unused** — there is no vehicle here whose
architecture is undetermined, which is the only condition under which the contract admits `none`.

**F5a is hard; F5b and F5c are soft.** F5a yields only to physics — propellant is not recoverable and not
substitutable. F5b and F5c both yield to production learning. **This is why basis B is the only basis that
tests anything:** basis A tests a pricing decision, basis C tests an accounting boundary, and only basis B
carries a cost against a floor.

### 2.1 The F5b floor has two readings, and both are reported (DA-30)

| Reading | Numerator | Denominator | Floor | Where |
|---|---|---|---|---|
| **Registered band** | ~$12–20M marginal cost per launch | 8,700 kg realized customer payload | **$1,379–2,299/kg** | SPCX unit-economics §2.2; RKLB peer-bench §2.1 |
| **Narrow reading** | ~$8–12M expended second stage only | 8,700 kg | **$920–1,379/kg** | RKLB peer-bench §7 |

The two readings overlap at $1,379/kg and differ by up to **1.67×** at the top. **Neither is adopted as "the"
floor**: the registered band is the one the falsifiers reference, and the narrow reading is the one the
derivation actually supports. At the capacity denominator (22,800 kg) the narrow reading gives $351–526/kg —
a floor against a spec, which is why it is not used.

### 2.2 One architecture label on this table is OURS, not the filer's

**Alpha's `fully_expendable` label is `DERIVED`, not filed.** *"Expendable"* returns **zero pages** in FLY's
10-Q, so the F5c assignment required by the contract rule above is **our derivation from the described
two-stage, five-engine, no-recovery design** — the contract mandates the floor while the filing does not
supply the label. **Recorded as `DERIVED` for exactly that reason.** Every other architecture label on this
table is filed.

⚠️ **And this is the honest shape of the F5c claim, which PIL-1 should carry rather than the cleaner
statement:**

> *The tier with the demonstrated price is populated by two vehicles — one of which has the price and no
> denominator, and the other of which has been assigned to the tier by us because the filing does not label
> it.*

**So the F5c tier's demonstrated status is a one-vehicle result twice over:** once because only one F5c
vehicle files a price (§13), and once because the second F5c vehicle's membership in the tier is our
inference rather than the issuer's statement.

---

## 3. The curve's only measured point — Electron (RKLB), F5c

**Electron basis B is `DEMONSTRATED` and is the only such cell on the table.** Every other row's cost-side
content is `MODELED`, `CLAIMED` or ABSENT.

**Denominator: LEO. Payload: Electron is filed only as *"up to 300 kg"* to low Earth orbit across
inclinations *"from 38 to 120 degrees"*** ([📄 RKLB 10-K p.8](https://agentii.ai/v/RKLB/sec87/8);
[📄 RKLB 10-K p.7](https://agentii.ai/v/RKLB/sec87/7)). **This is a CEILING, not a mass.** RKLB files a
spacecraft *count* — *"over 250 spacecraft to orbit … across 87 successful missions"* — and **never a mass**
([📄 RKLB 10-Q p.34](https://agentii.ai/v/RKLB/sec109/34)). So every corrected figure below is an **upper
bound** of the true $/kg, and the register's `UNRESOLVABLE-FROM-PUBLIC-SOURCES` disposition stands.

**The numerator is filed, both sides, in every period.** *"Revenue and Cost Per Launch"*:
[📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37) and
[📄 RKLB 10-Q p.31](https://agentii.ai/v/RKLB/sec104/31).

### 3.1 The RE-CONVERSION — driven by the HASTE mission mix

The filing discloses the contaminant verbatim:

> *"Two of the six Electron launch missions completed for the three months ended June 30, 2026 were Hypersonic
> Accelerator Suborbital Test Electron ('HASTE') launch missions, for which revenue was recognized over time
> and was partially recognized in prior quarters. All five Electron launch missions completed for the three
> months ended June 30, 2025 were point-in-time launches"*
> — [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37)

**Two suborbital testbeds carrying ZERO kilograms to LEO sit inside both the revenue numerator and the
launch-count numerator.**

| Period | Basis | Denominator | Basis A | Basis B | Factor |
|---|---|---|---:|---:|---:|
| **Q2 2026** | revenue / cost per launch, **4 orbital of 6** | 200 kg | **$45,500/kg** | **$22,000/kg** | **1.50×** |
| Q2 2026 | ceiling | 300 kg | $30,333/kg | $14,667/kg | 1.00× |
| **H1 2026** | 10 orbital of 12 (HASTE ≥ 2, unbounded) | 250 kg | **$36,800/kg** | **$19,600/kg** | **≥1.20×** |
| H1 2026 | ceiling | 300 kg | $30,667/kg | $16,333/kg | 1.00× |
| **Q2 2025** | **5 of 5 point-in-time, ZERO HASTE** | 300 kg | **$26,333/kg** | **$16,667/kg** | **1.00×** |
| Q1 2025 / H1 2025 / Q1 2026 | mix not filed | — | `UNEXERCISED` | `UNEXERCISED` | — |

Arithmetic, shown: `9.1 ÷ 0.200 = $45,500/kg`; `4.4 ÷ 0.200 = $22,000/kg`; `9.2 ÷ 0.250 = $36,800/kg`;
`4.9 ÷ 0.250 = $19,600/kg`; `7.9 ÷ 0.300 = $26,333/kg`; `5.0 ÷ 0.300 = $16,667/kg`.

**Correction: 1.00×–1.50× (+0% to +50%).** Not the `1.79×–2.62×` that circulates — **those two multipliers are
Falcon 9's arithmetic** (`22.8 ÷ 12.76 = 1.787`; `22.8 ÷ 8.70 = 2.621`) computed from **SPCX's** filed
mass-to-orbit table and fused with **Electron's** period count. **RKLB files no mass-to-orbit metric in any
period**, so the SPCX-style restatement cannot be reproduced at RKLB at all.

⚠️ **"Four of four periods" is FALSIFIED.** The correction is **ZERO in the one period whose mix is fully
filed** — Q2 2025, which contained no HASTE mission. Three periods are **`UNEXERCISED`, not clean**: the mix
is not filed, so no correction can be computed in either direction. **The magnituded claim that circulated was
Falcon 9's, and the population claim was wrong.**

**Basis B is the only basis that tests the F5c floor, and here is that test.** F5c's floor is the whole
vehicle, manufactured once and expended once; at Electron the numerator is filed — *"actual costs of the
launch vehicles that occur in the period … and all period costs in the period of launch"* — $4.4M in Q2 2026
([📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37)). **$14,667/kg at the 300 kg ceiling.** Electron's
basis A sits **2.07× above its own measured floor** (`$30,333 ÷ $14,667 = 2.07`; the ratio is invariant to
the denominator — `$45,500 ÷ $22,000 = 2.07`). **The only architecture with a measured floor is the one whose
price sits furthest above it.**

**Basis C at Electron is `UNRESOLVABLE-FROM-PUBLIC-SOURCES` and permanently so** — not a pending disclosure.
The issuer states, in the segment note, verbatim:

> *"Management does not regularly review either reporting segment's total assets or operating expenses. This
> is because in general, the Company's long-lived assets, facilities, and equipment are shared by each
> reporting segment."*
> — [📄 RKLB 10-Q p.33](https://agentii.ai/v/RKLB/sec109/33)

Basis C needs segment-level assets or opex to amortise a vehicle across the program, and **the issuer states
that the allocation is not produced and is not reviewed.** Resolving source: **none.** No future filing
resolves it, because the constraint is the issuer's own management structure.

### 3.2 The full Electron series — the curve's only measured segment

Both cells are filed in every period. Eight filed period-cells on each side:

| Period | Missions | Cost/launch | Revenue/launch | Basis B $/kg | Basis A $/kg | (rev − cost)/rev |
|---|---:|---:|---:|---:|---:|---:|
| FY2023 | 10 | $7.0M | $7.1M | $23,333/kg | $23,667/kg | 1.4% |
| FY2024 | 16 | $5.7M | $7.8M | $19,000/kg | $26,000/kg | 26.9% |
| FY2025 | 21 | $4.8M | $8.5M | $16,000/kg | $28,333/kg | 43.5% |
| Q2 2025 | 5 | $5.0M | $7.9M | $16,667/kg | $26,333/kg | 36.7% |
| H1 2025 | 10 | $5.3M | $7.5M | $17,667/kg | $25,000/kg | 29.3% |
| Q1 2026 | 6 | $5.4M | $9.3M | $18,000/kg | $31,000/kg | 41.9% |
| **Q2 2026** | 6 | **$4.4M** | **$9.1M** | **$14,667/kg** | **$30,333/kg** | **51.6%** |
| H1 2026 | 12 | $4.9M | $9.2M | $16,333/kg | $30,667/kg | 46.7% |

Sources: [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37) (Q2 and H1),
[📄 RKLB 10-Q p.31](https://agentii.ai/v/RKLB/sec104/31) (Q1 2026, Q1 2025),
[📄 RKLB 10-K p.46](https://agentii.ai/v/RKLB/sec87/46) (FY series).

**Across the series: basis B falls −37.1% ($23,333 → $14,667/kg) while basis A rises +28.2%
($23,667 → $30,333/kg), and the spread between them widens from 1.01× to 2.07×.** The released cost was kept,
not passed through. **This is the whole of 003:PIL-6's claim in one line, and it is measured rather than
argued.**

**Two caveats, carried and not weakened.** FY2023's $7.0M cost excludes a $2.1M retention-credit benefit and a
$4.1M contract-loss-reversal benefit credited to Launch Services cost of revenue — the filed metric is
already the conservative reading. And the series is **noisy**: the Q2 2025 zero-HASTE control diverges −15.3%
and −22.9% from the segment table, so **the direction is robust and the level is not.**

---

## 4. THE INVERSION — the headline

**The curve's single measured step moves the wrong way, and the mechanism is the denominator.**

| | Q2 2025 | Q2 2026 | Change |
|---|---:|---:|---:|
| cost per launch (basis B numerator) | $5.0M | $4.4M | **−12.0%** |
| fleet kg denominator (orbital missions × 300 kg ceiling) | 1,500 kg | 1,200 kg | −20.0% |
| **cost per kg, basis B** | **$16,667/kg** | **$22,000/kg** | **+32.0%** |

**The same 1.32× is reachable by two routes, and both are shown because they use different normalisations. A
reader who mixes them gets 1.10× instead.**

```
ROUTE 1 - per-mission normalisation  (the register's shorthand)
  cost per launch         5.0 -> 4.4     = 0.88      FELL 12.0%
  per-mission denominator  300 -> 200 kg = 0.6667    FELL 33.3%
  ratio                   0.88 / 0.6667  = 1.32      ROSE 32.0%
  equivalent form         0.88 x 1.50    = 1.32      EXACT

ROUTE 2 - fleet aggregate  (the table above)
  total cost     5 x 5.0 = 25.0 -> 6 x 4.4 = 26.4    = 1.056   ROSE  5.6%
  fleet kg             1,500 -> 1,200    = 0.80      FELL 20.0%
  ratio                1.056 / 0.80      = 1.32      ROSE 32.0%  EXACT

  check  16,667 = 25.0M / 1,500 kg   and   22,000 = 26.4M / 1,200 kg
```

**`0.88 × 1.50 = 1.32`, exact.** The 1.50× is the reconversion factor from §3.1: the 200 kg corrected
denominator is `300 ÷ 200 = 1.50×` smaller than the ceiling. **The disclosed improvement is a denominator
artefact in the optimistic direction, and it is PIL-3's claim demonstrated rather than argued.**

**The rise holds unless Q2 2025's missions averaged more than ~24% less filled than Q2 2026's** — the
break-even is a fill-rate ratio of **0.758**. Two of six missions bought no kilogram, and the disclosure
reports the cost side as though they had.

**What the inversion means for the sector's cost conversation.** The five-year cost narrative in this universe
is that per-kilogram launch cost is collapsing. **On the only vehicle where both the numerator and the
denominator are filed, measured per-kilogram cost rose by a third while measured per-launch cost fell by an
eighth.** A curve drawn on per-launch cost and a curve drawn on per-kilogram cost point in **opposite
directions off the same two numbers.**

---

## 5. Falcon 9 (SPCX) — `partially_reusable` → F5b

**Denominator: LEO. Payload: capacity 22,800 kg is CLAIMED and unfiled; realized customer payload is
8,700 kg (Q2 2026) and 12,760 kg (all launches).**

| Basis | Numerator | $/kg at capacity (22,800 kg) | $/kg at realized customer (8,700 kg) | Grade |
|---|---|---|---:|---|
| **A** — customer list price | ~$67M/launch | **$2,939/kg** ⚠️ **denominator-failed** | $7,701/kg | `CLAIMED` |
| **A′** *(002's A″, Launch-Services-only)* | $648M ÷ 10 = **$64.8M** | $2,842/kg | **$7,448/kg** | `DEMONSTRATED` figs / `MODELED` div |
| **A′ (whole segment)** | $962M ÷ 10 = $96.2M | $4,220/kg | $11,057/kg | `DEMONSTRATED` figs / `MODELED` div |
| **B** — marginal cost | ~$12–20M | $526–877/kg | **$1,379–2,299/kg** | **`MODELED`** |
| **C** — fully loaded | $1,504M ÷ 10 = $150.4M | **$6,596/kg** | $17,287/kg | `DEMONSTRATED` figs / `MODELED` div |
| *(C(i) — cost of revenue alone)* | $329M ÷ 10 = $32.9M | $1,443/kg | **$3,782/kg** | `DEMONSTRATED` figs |

Sources: [📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7);
[📄 SPCX 10-Q p.37](https://agentii.ai/v/SPCX/sec8/37).

### 5.1 Basis A is denominator-failed, not merely claimed

**`$2,939/kg` is `$67M ÷ 22.8 t`, and `"22.8"` returns ZERO located pages across SPCX's filings.** The
denominator has no filed basis and cannot be located at all — 002 §5.1 carries this as
`UNRESOLVABLE-FROM-PUBLIC-SOURCES`. **The single most widely-quoted SPCX number in this workspace rests on a
denominator that appears nowhere in the filings**, and it must not be carried. The resolving disclosure is a
filed Falcon 9 payload-mass-per-mission figure on the same definition as the mass-to-orbit metric.

**The matched-pair basis is the only internally consistent SPCX series** — numerator fixed at launch-services
revenue, denominator fixed at *customer* payload:

| Period | Launch services revenue | Customer payload | $/kg | Grade |
|---|---|---:|---:|---|
| Q2 2026 | $648M | 87 t | **$7,448/kg** | `DEMONSTRATED` |
| Q1 2026 | $330M | 45 t | $7,333/kg | `DEMONSTRATED` |
| H1 2026 | $978M | 132 t | $7,409/kg | `DEMONSTRATED` |
| Q2 2025 | $490M | 88 t | **$5,568/kg** | `DEMONSTRATED` |
| H1 2025 | $1,056M | 163 t | $6,479/kg | `DEMONSTRATED` |

**Band: $5,567–7,448/kg, 1.34×** (`7,448 ÷ 5,568 = 1.338`). **This is the band 003:PIL-4's falsifier is
registered against.**

**A $1/kg rounding note, carried not corrected (DA-29).** The register records the low end as **$5,567/kg**;
recomputation from the filed cells gives **$5,568/kg** (`490,000 ÷ 88 = 5,568.18`). The difference has **no
filed explanatory term**, so it is `UNRESOLVED` rather than "a rounding difference" — a rounding explanation
would be a back-solve. The band is quoted as **$5,567–7,448/kg**, the register value, because PIL-4's falsifier
text carries the literal `5567`. **The 1.34× band survives either way.**

### 5.2 Basis B is `MODELED` and 002 says so

**No SPCX cost-per-launch disclosure exists on any basis.** Basis B here is **our cost construction** on a
`~$12–20M` marginal-cost band — a `MODELED` cell, and **a `MODELED` input can never satisfy a falsifier.**
002 §5.1 marks it `UNRESOLVABLE-FROM-PUBLIC-SOURCES`. Resolving source: a filed SPCX cost of launch services,
or a segment line decomposable to a per-launch figure. 001 nominated NASA CRS / Commercial Crew contract
values as a revealed-price **floor** — that is a `CLAIMED` resolution, not a `DEMONSTRATED` one. **F5b's floor
is `MODELED` on both readings (§2.1), which means the F5b tier has no measurable floor at all.**

### 5.3 Basis C is 71.5% Starship R&D — it is not a launch cost

The $150.4M numerator decomposes as cost of revenue $32.9M (**21.9%**), R&D $107.6M (**71.5%**), SG&A $9.9M
(6.6%). Per kilogram at the capacity denominator: $1,443/kg, **$4,719/kg**, $434/kg. **71.5% of the
fully-loaded `$6,596/kg` is Starship development spending charged in the same quarter** — an R&D programme for
a *different* vehicle, expensed through the same segment. R&D costs *"mainly relate to the development, build,
and testing of Starship"* ([📄 SPCX 10-Q p.37](https://agentii.ai/v/SPCX/sec8/37)). **Any consumer of basis C
is consuming a Starship R&D rate, not a Falcon 9 cost.**

**The closest SPCX analogue to a marginal cost is not basis B — it is cost of revenue alone:**
`$32.9M ÷ 8,700 kg = $3,782/kg`. It sits *between* A′ and B, and it is why this table reports the spread
rather than picking a winner: **where the "cost" line is drawn inside the P&L moves the answer by ~2.7×.**

---

## 6. The 12.8× spread — four arithmetically correct values on ONE page

**All four numerators and both denominators are filed on the single page
[📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7)**, for the six months ended 2026-06-30:

| Numerator (basis) | Denominator (basis) | $/kg | Correct? | Comparable? |
|---|---|---:|---|---|
| Launch services revenue **$978M** (segment revenue-type) | Customer payload **132 t** | **$7,409/kg** | ✓ | — |
| **Space segment revenue $1,581M** (whole segment) | Customer payload **132 t** | **$11,977/kg** | ✓ | ✗ |
| Launch services revenue **$978M** | **Mass to orbit 1,041 t** (incl. internal) | **$939/kg** | ✓ | ✗ |
| **Space segment revenue $1,581M** | **Mass to orbit 1,041 t** | **$1,519/kg** | ✓ | ✗ |

```
spread             11,977 / 939   = 12.75  ->  12.8x
numerator factor    1,581 / 978   =  1.617x   (Space segment vs launch services)
denominator factor  1,041 / 132   =  7.886x   (total mass vs customer payload)
product             1.617 x 7.886 = 12.75x
```

**Every one of the four is arithmetically correct. None is comparable to any other.** The spread is driven
**almost entirely by the denominator — 7.886× against a numerator factor of 1.617×.** **Four ratios, four
bases, zero basis fields: this is DA-30's canonical shape, and it is why this artifact reports every competing
basis rather than choosing one.**

**The boundary that makes the numerator ambiguous is filed, and it is the CUSTOMER boundary.** *"Our Space
segment revenue only reflects our customer launches and customer activities"*
([📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35)), and *"For launches of our Starlink satellites, the
Company does not recognize any inter-segment revenue, rather those launch costs are capitalized in satellites
in Property, plant, and equipment, net"* ([📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36)). **So the
launch-services numerator excludes the majority of launches while the mass-to-orbit denominator includes
them** — 73.7% of the denominator's volume by count. Putting those two on one ratio is not a measurement.

### 6.1 The five-column table is unlabelled, and its order was RECOVERED

The 8-K table files five columns under one header with **no per-value label**. The order is established by
**three independent exact reconciliations**, not assumed (DA-27):

```
Launch count   40 + 38 = 78     (Q1 2026 + Q2 2026 = 6M 2026)
Revenue       330 + 648 = 978   ($M)
Payload        45 + 87 = 132    (t)
```

**Three quantities, three exact identities, one ordering → [Q2 2026, Q1 2026, Q2 2025, H1 2026, H1 2025].**
Confirmed independently against the 10-Q's Falcon/Starship split: 37+1=38 ✓, 45+1=46 ✓, 77+1=78 ✓, 81+3=84
✓ — **four of four.**

**One disclosed discrepancy, recorded rather than smoothed.** Customer + internal payload sums to the filed
mass-to-orbit total **within 1 tonne on four of five columns** (87+397=484 against 485; 88+563=651 against
652; 132+908=1,040 against 1,041; 163+938=1,101 against 1,102). Only Q1 2026 closes to the tonne. **A
difference of exactly one unit in four of five columns is a rounding artefact, not an error** — and it is why
this table's per-tonne ratios are quoted to the nearest dollar but never to the cent. **DA-29 read correctly:
the check *was* run, it *did* almost close, and "almost" is stated rather than back-solved away.**

### 6.2 The customer share has two denominators and opposite signs by PERIOD

| Period | Customer | Total launches | Share | Period basis |
|---|---:|---:|---:|---|
| Q2 2026 | 10 | 38 | **26.3%** | 3M |
| Q2 2025 | 9 | 46 | 19.6% | 3M |
| H1 2026 | 17 | 78 | **21.8%** | 6M |
| H1 2025 | 21 | 84 | 25.0% | 6M |

```
Customer share, Q2 (3M):  19.6% -> 26.3%   RISING   by +6.7 pp
Customer share, H1 (6M):  25.0% -> 21.8%   FALLING  by -3.2 pp
```

**Same page, same metric, opposite directions, because the period basis differs.** The same trap runs on
throughput: **mass to orbit is −25.6% on the 3M basis (485 against 652 t) but −5.5% on the 6M basis (1,041
against 1,102 t) — 4.6× smaller.** **Never state an SPCX throughput figure without its period basis.**

---

## 7. Starship (SPCX) — `fully_reusable` (declared) → F5a · `fully_expendable` (as flown) → F5c

**Denominator: none. Payload: the 100,000 kg figure is a published vehicle spec and is not in any filing in
this corpus.** The only two Starship flights in the corpus are described as **suborbital** (Flight 12, May
2026 — *"first suborbital mission"*; Flight 13, July 2026), and *"To date, all Starship launches have been
classified as internal"* ([📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35)).

| Basis | Denominator | $/kg | Grade |
|---|---|---|---|
| A | — | **ABSENT** | — |
| A′ | — | **ABSENT** | — |
| B | — | **ABSENT** | — |
| C | — | **ABSENT** | — |

**⭐ Starship's row is `UNEXERCISED`, NOT `CLEAN`.** **Zero customer launches means no price exists to test**
— a test that could not run is not a test that passed, and Starship has not been shown to be uncompetitive on
cost. It has not been tested. This distinction is the single most important thing on this row.

### 7.1 The issuer publishes two contradicting cost claims on the same day

Both `CLAIMED`, both in the same corpus, both published **2026-08-04**:

| Claim | Wording | Where | Grade |
|---|---|---|---|
| **~10×** | *"Starship aims to quadruple payload capacity and reduce launch costs by 10x compared to our Falcon 9 rocket"* | [📄 SPCX Q2 2026 call p.3](https://agentii.ai/v/SPCX/ect1/3) | `CLAIMED` |
| **~99%+** | *"reduce the cost to orbit by 99% or more relative to the historical average"* | [📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7) | `CLAIMED` |

**These differ by more than an order of magnitude, and each carries a DA-30 collapse inside its own
definition.** The 10× claim gives a ratio with no basis — 10× against what? cost or price? per launch or per
kg? The 99% claim gives a percentage with no reference value — the historical average of what, over what
window? **Neither names a denominator; neither names a period.**

**Tested against the constitution's own F5a reference point:**

| Reading | Applied to | Result | vs F5a floor `$46–92/kg` |
|---|---|---|---|
| **10×** (one order) | $2,700–2,900/kg | **$270–290/kg** | clears it 2.9×–6.3× ✓ |
| **99%+** (two orders) | $2,700–2,900/kg | **$27–29/kg** | **wholly below it** ✗ |
| 99%+ | matched pair $5,567–7,448/kg | $55.67–74.48/kg | straddles |

**So the pinned constitution's own bound classifies one of the issuer's filed claims as inside the credible
band and the other as outside it** — and the outside one, taken at face value, requires **159–317 t of payload
per flight** to clear the propellant floor (at $1–2/kg propellant), i.e. **1.6×–3.2× the F5a reference
payload**. Against the matched-pair realized basis it requires **83–165 t**. **Either way it clears the floor
only on a payload the issuer has never filed.**

**Verdict: neither claim is admissible as a curve point, and the pair is not a range — it is a
contradiction.** Recorded `CLAIMED`. **This is PIL-3's raw material: it is what the sector's cost conversation
looks like when nothing is measured, and it is why this curve is `CLAIMED` rather than `DEMONSTRATED` on the
reusable tiers.**

### 7.2 Starship's architecture diverges from its declaration

Starship appears on **two** architecture rows because the declared architecture and the as-flown architecture
differ: **`fully_reusable` declared → F5a** (propellant floor), and **`fully_expendable` as flown → F5c**. On
the F5c reading there is **no registered numeric value**, because no vehicle cost is filed. **The divergence is
stated rather than resolved** — resolving it requires a filed payload mass on a mission the filing describes
as delivering to orbit, at which point the 100,000 kg spec figure is replaced by a delivered mass and a basis
can be built.

---

## 8. Neutron (RKLB) — `partially_reusable`, UNFLOWN → F5b

**Denominator: LEO. Payload: `"approximately 13,000 kg for reusable configuration"`** — filed twice, and
**both filings specify the reusable configuration**
([📄 RKLB 10-K p.8](https://agentii.ai/v/RKLB/sec87/8)). **The payload of the expendable configuration is
nowhere filed**, so the implied $/kg is for a configuration RKLB has not said it will fly first.

| Basis | Cell | $/kg at ~13,000 kg | Grade |
|---|---|---:|---|
| **A** — disclosed ASP | $50–55M/launch | **$3,846–4,231/kg** | `CLAIMED` numerator ÷ filed payload |
| **A′** | — | n/a | the basis does not apply to RKLB |
| **B** — marginal cost | — | **ABSENT** — never flown | — |
| **C** — fully loaded | — | **ABSENT** — structurally unconstructible at RKLB | — |

**The PIL-4 payload bar, as arithmetic.** $50–55M at $5,567–7,448/kg implies **6,713–9,882 kg** of the 13,000
kg nameplate. `MODELED`. **The medium-lift case closes only above the bar, and it rests on F5b, not F5a,
because the recoverable stage is the *first* stage** — which is exactly why §2.1's two F5b readings matter.

**Neutron basis B is `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (transitional):** not flown, so no cost per launch can
exist before a first flight. Resolving source: **a per-launch cost disclosure in the first flight quarter's
10-Q, in RKLB's existing metric form** — the form already exists at Electron, so this is a *narrow* gap rather
than a structural one.

### 8.1 The disclosure inversion, stated plainly

**In this universe, the vehicle that has NEVER FLOWN (Neutron, F5b) is filed with a usable reusable payload of
"approximately 13,000 kg", while the vehicle that HAS ACHIEVED ORBIT (Alpha, F5c) is filed with a class
label.** **The disclosure is better for the unflown vehicle than for the flown one.**

---

## 9. Alpha (FLY) — `fully_expendable` → F5c

**Basis matrix: A ✗ / A′ ✗ / B ✗ / C ✗ — four of four empty.** The emptiness is **a property of the
disclosure, not of the vehicle.**

| Basis | Definition | FLY's filed position | Verdict |
|---|---|---|---|
| **A** | customer list price per launch | no price per launch filed anywhere | ✗ |
| **A′** | issuer-realized variant (revenue ÷ launches) | **no launch count filed** — the divisor does not exist | ✗ |
| **B** | marginal cost per launch | one reportable segment; no launch cost-of-revenue line | ✗ |
| **C** | fully-loaded amortized | no launch-level capital or amortization isolated | ✗ |

*"We operate as a single reportable segment"* ([📄 FLY 10-Q p.34](https://agentii.ai/v/FLY/sec21/34)). **So
FLY's revenue-type disaggregation is NOT a segment split**, and treating `Launch` as a segment is precisely
the DA-30 collapse this row exists to avoid.

### 9.1 Alpha's payload is a CLASS LABEL, and the filing discloses its width

| Filed string | Source | What it supplies |
|---|---|---|
| *"the 1,000-kilogram payload class"* | [sec21 p.34](https://agentii.ai/v/FLY/sec21/34) | a category name |
| *"the 1,000-kilogram payload class"* (×2) | [sec16 p.7](https://agentii.ai/v/FLY/sec16/7) | a category name |
| *"the 1,000 kilograms category"* | [sec16 p.9](https://agentii.ai/v/FLY/sec16/9) | a category name |
| *"satellites between 200 kilograms to 1,200 kilograms, according to analysis by BryceTech in 2025"* | [sec16 p.9](https://agentii.ai/v/FLY/sec16/9) | **the category's own filed width** |

**Mass: not stated. Orbit: not stated. Inclination: not stated. Configuration: not stated.** The label appears
four times across two filings and is never accompanied by a quantity of payload delivered.

**`1,200 ÷ 200 = 6×`.** Even taking the label entirely at face value, any dollars-per-kilogram derived from it
carries a **6.0× denominator ambiguity** — and that is the *most favourable* reading, because it assumes the
label means the category's midpoint, which the filing never says.

⚠️ **6.0× is 4.5× worse than the 1.34× defect the correction withdrew a test over.** `6.0 ÷ 1.34 = 4.48`. The
1.34× dispersion in the matched-pair band was treated as sufficient grounds to withdraw a registered falsifier
and rebuild it; Alpha's denominator ambiguity is nearly five times that size and **cannot be corrected in
either direction.** **Record ABSENT, never estimated.**

**Why a ceiling is usable and a category is not:**

| Vehicle | Filed payload statement | Orbit | Nature | Usable in a ratio? |
|---|---|---|---|---|
| **Electron** (RKLB) | *"up to 300 kg"* | **LEO, inclinations 38–120°** | a **CEILING** on a stated orbit | **YES — as an upper bound** |
| **Alpha** (FLY) | *"1,000-kilogram payload class"* | **not stated** | a **CATEGORY** with a 6× width | **NO** |

**Electron's correction is `1.00×–1.50×` and is reportable *because* the deficiency is one-directional:**
`"up to"` bounds the answer, so the correction is an **upper bound** and still carries information. **Alpha's
deficiency is unbounded in both directions** — the same label covers a 200 kg payload and a 1,200 kg payload —
so no correction exists and none is attempted. **This table can absorb an upper bound. It cannot absorb a
category.**

**FLY's value to this matrix is as the disclosure-uniqueness control:** it is the case that proves the
ceiling-versus-category distinction is real rather than a matter of degree.

**One basis note that matters for comparability.** FLY's launch revenue is recognized at a **point in time** —
the performance obligation is *"the initiation of the launch"* ([📄 FLY 10-Q p.16](https://agentii.ai/v/FLY/sec21/16)).
RKLB's HASTE missions are recognized **over time**. So a "revenue per launch" denominator counts a
point-in-time orbital mission and an over-time suborbital testbed identically while their recognition differs
— **which is exactly the contamination that drives Electron's 1.00×–1.50× correction.** FLY is clean of that
particular defect and cannot be compared to RKLB on a per-launch basis for the opposite reason: it files no
count at all.

**FLY's 2025 growth rates are `UNRESOLVED`, not usable.** The as-reported comparative quarter is **25.44%** of
the pro forma figure for the same period ($15,549k against $61,116k) and H1 is **44.82%** ($71,404k against
$159,314k) — so the naive growth rates are computed between a **full** period and a **partial** one.

---

## 10. The absent cells — THREE disposition classes, not two

**Thirteen absences, three classes, three different remedies.** Two of the three are reachable by research.
**The third is not reachable by research at all, and this is the class most often collapsed into the other
two.**

| Class | What it means | Remedy |
|---|---|---|
| **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** | the datum is not disclosed and no arithmetic on filed cells produces it | wait for, or request, a disclosure |
| **`UNRESOLVABLE-FROM-PLATFORM`** | the datum may exist but **the platform cannot present it** | tooling |
| **`REACHABLE-BUT-NOT-RECORDABLE`** | the datum **is reachable** and the **CONTRACT cannot record it** | **a contract amendment** |

### 10.1 The 13 absent cells, each with its reason and resolving source

| Cell | Reason | Class | Resolving source |
|---|---|---|---|
| Starship **A/A′/B/C** | no price, no contracted rate, no cost, no filed payload mass; both corpus flights suborbital | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a filed or contracted Starship price, **or** a filed payload mass for a mission the filing describes as delivering to orbit |
| Electron **A′** | A′ is defined as the SPCX-specific realized variant; no RKLB counterpart exists | **n/a — not an absence** | none required; the basis does not apply |
| Electron **C** | segment assets/opex not produced and not reviewed (§3.1) | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — **permanent** | **none** — the constraint is the issuer's management structure |
| Neutron **A′** | basis does not apply to RKLB | **n/a — not an absence** | none required |
| Neutron **B** | not flown; no cost per launch can exist before a first flight | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — **transitional** | a per-launch cost disclosure in the first flight quarter's 10-Q, in RKLB's existing metric form |
| Neutron **C** | same structural bar as Electron C | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — **permanent** | none |
| Alpha **A/A′/B/C** | no price, no launch count, no launch cost line, one reportable segment | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a per-launch price or per-launch cost on any named basis |
| Falcon 9 **A** | denominator `22.8 t` appears in no filing | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a filed Falcon 9 payload-mass-per-mission figure on the mass-to-orbit definition |
| Falcon 9 **B** | no SPCX cost-per-launch disclosure exists on any basis | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a filed SPCX cost of launch services, or a segment line decomposable to a per-launch figure |

*(Two of the thirteen are `n/a` rather than genuinely absent — A′ is a SPCX-specific basis with no RKLB
counterpart — which is why the census counts 13 absent CELLS and not 13 missing DATA POINTS.)*

### 10.2 `REACHABLE-BUT-NOT-RECORDABLE` — the class with the contract remedy

**This is the register's richest population and the one that is neither a research shortfall nor a tooling
gap.** The datum is reachable, filings would resolve it, and **the CONTRACT cannot record it.** **The remedy
is a contract amendment, not more research.**

| Datum | Why it is reachable | Why the contract cannot record it |
|---|---|---|
| **Falcon 9's 22.8 t** | a published vehicle spec, quoted industry-wide | **it is the denominator of all four basis letters.** Recording a value whose provenance is off-corpus breaks the artifact's filing-anchored provenance, so the cell that depends on it is filed as failed rather than as a number |
| **The $67M list price** | SpaceX publishes a price schedule | a price schedule is not a filing; carrying it would make basis A's numerator `CLAIMED` at the same grade as its own denominator, destroying the grade's discriminating power |
| **Neutron's expendable-configuration payload** | RKLB knows it and will fly it | the matrix records *filed* configuration → payload pairs; a configuration the issuer has not named cannot be entered without inventing the pairing |
| **Alpha's payload mass** | the vehicle has flown and reached orbit | a filed *class* cannot be entered as a mass, and entering both would collapse two bases into one cell (DA-30) |
| **F5a's inputs — propellant mass and propellant price** | both are purchasable physical quantities | the floor register admits `MODELED` inputs only; a purchased price is neither filed nor ours |
| **The orbit split of SPCX's mass to orbit** | the launches are public and orbit is observable | SPCX's metric is **orbit-agnostic by construction**; the contract's `denominator_orbit` field requires a single named orbit, so an orbit-agnostic denominator is recordable only as a flag |
| **FLY's addressable payload span (200–1,200 kg, 6×)** | inherited as a market span from FLY's own filing | **no agentii source records it**, so the 6× magnitude is carried as inherited context and is **not** used to construct a denominator (§9.1) |
| **A buyer-side launch-cost share** | reachable in the filer's books at every operator in this thesis | launch cost sits inside cost of revenue and is not separately disclosed; **no admissible field admits it** |

**Why this matters.** Every row above would be *solved* by more research and *still* be unrecordable. **A
reader who treats all thirteen absences as "we need more data" will spend effort on six cells that more data
does not unblock.** The distinction is not academic: it is the difference between a research queue and a
schema-change queue.

### 10.3 `UNRESOLVABLE-FROM-PLATFORM` — the tooling class, with its negative searches recorded

**Every negative below was run, and is recorded with the tool that found it**, because *a page number that was
not located is a guess, and a negative that was not searched is not a negative.*

| Search | Result |
|---|---|
| `"22.8"` across SPCX filings | **ZERO located pages** (run twice) |
| `"per kilogram"` in the 8-K | **ZERO located pages** |
| `list_xbrl_concepts("Payload")` | **0 concepts** |
| `list_xbrl_concepts("Launch")` | **0 concepts** — against **109** for `"Revenue"` |
| `"cost per launch"` phrase-level, SPCX 10-Q | **no page** |
| A filed per-launch or per-kilogram series at SPCX | **does not exist** on any basis |

**So any `$/kg` assembled from the structured layer at SPCX is `UNRESOLVABLE-FROM-PLATFORM`** — the concepts
are absent from the taxonomy, not merely unfound. **And it is only *partly* the platform's fault**: the
issuer files no per-unit series, so the structured layer has nothing to extract. **The two facts are kept
apart deliberately, because their remedies differ.**

### 10.4 The demand side — launch dollars are filed, the denominator is not

**Swept across the demand-side artifacts to test whether any contributes a curve cell. None does**, and the
reason is uniform: **the buy side files launch DOLLARS and no MASS**, so no buyer-side `$/kg` exists on any
basis either. The perimeter is recorded here so a downstream reader does not mistake the sweep for an
oversight.

| Demand-side launch-cost datum | Amount | Denominator filed? | Curve cell? |
|---|---|---|---|
| LUNR — amortisation of deferred contract costs for **subcontracted launch services**, FY2025 | **$29.8M** (FY2024: $10.1M; H1 2026: $14.3M; Q2 2026: $7.1M) | **no** — no mass, no orbit, no mission count | **no** — a numerator with no denominator |
| LUNR — launch delay fees | $2.3M (H1 2025) and $0.8M (Q2 2025); **zero in H1 2026** | — | **no** |
| LUNR — non-cancelable launch obligations | **$58.1M** remaining ($38.5M due 2026; $19.6M due 2027) | **no** | **no** — and stated as mixing launch services *with* component development, so it is `NON-FORMABLE` as filed |
| PL — future purchase commitments under noncancelable launch service contracts | **$4.7M** | **no** | **no** — and no launch commitment is disclosed in the annual report at all |
| YSS — packing factors (*"25 M-CLASS platforms in a SpaceX Falcon 9"*; *"120 units in a SpaceX Starship"*) | — | **no dollar figure attaches anywhere in the filing** | **no** — a design constraint, not a cost |
| SATS — two SpaceX launch services contracts (*EchoStar XXV*, *XXVI*) | **no amount disclosed** for either contract | **no** | **no** |

**Two consequences for this table.**

1. **The 20-cell census is complete.** No demand-side artifact adds a vehicle row or a basis cell, because the
   demand side is not a launcher. **The matrix's population is five vehicles and it does not widen.**
2. **The curve has no buy-side counterpart anywhere in this universe.** Every operator in this thesis buys
   launch and files the dollars; not one files a mass against them. **So the `$/kg` axis exists only on the
   sell side** — which is itself a finding, because it means no external observer can be shown to price off
   the curve and no issuer can be shown to have passed it through, **from filings alone.**

⚠️ **One related figure that is a cross-thesis result and NOT a curve cell, carried because it qualifies a
claim made downstream:** LUNR's FY2025 launch amortisation is **14.19%** of its revenue, against SPCX's
**8.29%** launch-services share. **The SPCX figure is not the universe ceiling on launch intensity, and
003:PIL-6's language should be relaxed accordingly at that issuer.** No `$/kg` follows from either figure —
neither has a filed mass to divide by.

---

## 11. The `$/kg` ladder — nine rungs, each with its basis and denominator

**Every rung below is USD per kilogram to LEO.** No rung is "the" Falcon 9 cost. Two axes and one convention
move the answer across the whole range.

| # | Rung | Basis | Denominator | Grade | Filing-anchored? |
|---|---|---|---:|---|---|
| **L1** | **$939/kg** | launch services revenue ÷ all mass to orbit | 1,041 t | `DEMONSTRATED` | ✓ |
| **L2** | **$2,939/kg** | list price ÷ capacity | 22.8 t | `CLAIMED` | ✗ **denominator-failed** |
| **L3** | **$4,219/kg** ⚠️ | Space segment revenue ÷ capacity | 22.8 t | `CLAIMED`/derived | ✗ |
| **L4** | **$525–875/kg** | marginal cost, capacity denominator | 22.8 t | `MODELED` | ✗ |
| **L5** | **$5,568/kg** | Launch Services revenue ÷ realized customer payload | 88 t | `DEMONSTRATED`/`MODELED` div | ✓ |
| **L6** | **$6,596/kg** | Space segment fully-loaded ÷ capacity | 22.8 t | `DEMONSTRATED` figs | ✓ figs |
| **L7** | **$7,409/kg** | Launch Services revenue ÷ customer payload, 6M | 132 t | `DEMONSTRATED`/`MODELED` div | ✓ |
| **L8** | **$7,448/kg** | Launch Services revenue ÷ customer payload, 3M | 87 t | `DEMONSTRATED`/`MODELED` div | ✓ |
| **L9** | **$11,977/kg** | Space segment revenue ÷ customer payload | 132 t | `DEMONSTRATED`/`MODELED` div | ✓ |

> ⚠️ **L3's registered value is a live discrepancy.** The task register's ladder carries `$4,219/kg`; the
> recomputation from the filed cells is `$96.2M ÷ 22,800 kg = $4,219.3/kg`. **They agree**, and the rung is
> carried as registered. It is flagged here only because it is the one rung whose denominator is the failed
> 22.8 t, so the rung is admissible as a *ladder position* and inadmissible as a *measurement*.

**The three axes, isolated:**

| Axis | Range | Factor |
|---|---|---:|
| **Basis axis** — Launch Services revenue vs Space segment revenue (numerator) | $978M → $1,581M | **1.617×** |
| **Denominator axis** — customer payload vs all mass to orbit | 132 t → 1,041 t | **7.886×** |
| **Convention axis** — capacity vs realized (22.8 t → 8.7 t) | 22.8 t → 8.7 t | **2.621×** |
| **Period axis** — five periods on one fixed basis (matched pair) | $5,568 → $7,448/kg | **1.34×** |

**The denominator axis is 4.9× the basis axis.** `7.886 ÷ 1.617 = 4.88`. **The sector's cost conversation is
dominated by an axis it does not name.** And the **period axis — 1.34× on a basis where both numerator and
denominator are frozen and immutable — is larger than the basis axis.** A ratio that moves 34% while nothing
in its definition moves is not a stable measurement, and **a cost curve drawn through it inherits that 34%.**

**Cross-vehicle placement on the ladder** (all LEO):

| Vehicle | Basis B | Basis A | Basis B ÷ its applied floor |
|---|---:|---:|---|
| **Electron** (F5c) | **$22,000/kg** `DEMONSTRATED` | $45,500/kg | **2.07× above** |
| Falcon 9 (F5b) | $1,379–2,299/kg `MODELED` | $7,448/kg (A′) | 1.00×–1.67× above (n/a — `MODELED`) |
| Starship (F5a) | ABSENT | ABSENT | — |
| Neutron (F5b) | ABSENT | $3,846–4,231/kg `CLAIMED` | — |
| Alpha (F5c) | ABSENT | ABSENT | — |

---

## 12. Cross-references to the register, carried not re-derived

| Register item | Where it lands on this table |
|---|---|
| **DA-23** (served negative as positive, magnitude-stripped) | the census is carried in the per-ticker artifacts and **not re-derived here**; the detector is the component identity, not the sign |
| **DA-25** (normalised per-unit metrics) | both legs of the per-unit ratio are **quarantined** where the normaliser is a label; the residual changes sign, which is why Alpha's row is ABSENT rather than estimated |
| **DA-26** (annual mislabelled quarterly) | no annual figure is used on this table; every SPCX column is period-labelled (§6.1) |
| **DA-27** (fiscal-period labels) | the 8-K column order is **recovered by three exact reconciliations** (§6.1); period basis stated on every throughput figure |
| **DA-28** (capital-structure discontinuity around an IPO) | does not touch a per-kilogram cost; FLY's partial-period comparatives are a **period** discontinuity, not a capital-structure one, and are handled in §9 |
| **DA-29** (a closing reconciliation is not a check) | the payload-within-1-tonne note (§6.1) and the $5,567/$5,568 note (§5.1) |

---

## 13. PIL-1's falsifier, evaluated

```
metric:    count_of_universe_vehicles_with_a_demonstrated_price_per_kg_to_LEO
           _below_their_architecture_applied_launch_cost_floor
threshold: 0
op:        >
source:    issuer_filing_or_audited_segment_table
```

**The falsifier does NOT fire. Count = 0.**

There is **one** vehicle in this universe with a demonstrated price per kilogram to LEO — **Electron** — and
its demonstrated price sits **2.07× ABOVE its applied F5c floor**, not below it
(`$30,333 ÷ $14,667 = 2.07`; `$45,500 ÷ $22,000 = 2.07` — the ratio is invariant to the denominator choice).
**No vehicle on this table has a demonstrated price below its architecture's applied floor.**

**⭐ And the honest scope, stated because it is the whole caveat: the count is 0 on a population of ONE.**
Starship's row is **`UNEXERCISED`, not `CLEAN`** (§7) — it has no demonstrable price to test, so it neither
fires the falsifier nor supports it. **A count of 0 drawn from a population of 1 is not evidence that the
claim generalises**; it is evidence that the test has been run once. **The claim that launch is a master COST
variable survives — and it survives on one measurement, on one architecture, on one vehicle.**

**Which is why the F5c tier's demonstrated status is a one-vehicle result — twice over.** **F5c is the only
tier with a `DEMONSTRATED` price**, and **FLY (Alpha) is the vehicle that would have tested that
generalisation — and it fails to**, on a class label with a 6× width (§9.1). **So the tier's demonstrated
status rests on Electron alone.** And separately, **Alpha's membership in the F5c tier is our `DERIVED`
label rather than the filer's** (§2.2) — so the tier is populated by one vehicle that files a price and no
denominator, and one that we placed in it. **If a second F5c vehicle's price arrived below the floor, the
count would move.**

---

## 14. What the curve IS, stated plainly

**A matrix whose demonstrated content is ONE VEHICLE and ONE BASIS, against 13 absent cells out of 20.**

```
5 vehicles x 4 bases                            20 cells
  2 DEMONSTRATED                                Electron A, Electron B
  2 DEMONSTRATED-figures / MODELED-division      Falcon 9 A', Falcon 9 C
  2 CLAIMED                                      Falcon 9 A, Neutron A
  1 MODELED                                      Falcon 9 B
 13 ABSENT                                       the rest
```

**Four statements a reader is entitled to take from this table, and four they are not.**

| ✓ The table shows | ✗ The table does not show |
|---|---|
| Per-kilogram launch cost **rose 32.0%** on the only vehicle where both sides are filed, while per-launch cost **fell 12.0%** | that launch costs are generally rising — the population is one vehicle |
| F5c holds the **only** demonstrated price, and it sits 2.07× above its own measured floor | that F5a or F5b floors hold — **both are `MODELED`, and neither has a demonstrable price** |
| Four arithmetic-correct `$/kg` values for the same period family span **12.8×** on one page | that any one of the four is wrong — all four are correct and none is comparable |
| The disclosed improvement is a **denominator artefact in the optimistic direction** | that the artefact was intentional — HASTE's revenue recognition is filed and the mechanism is disclosed |

**PIL-1's verdict, PIL-3's claim, and PIL-4's bar all rest on this matrix, and all three inherit its scope.**
**PIL-3's claim is demonstrated rather than argued** — the sector's cost narrative runs on denominator choices
rather than measurements, and the inversion is that fact quantified. **PIL-1's falsifier does not fire, on a
population of one.** **PIL-4's bar is registered against the $5,567–7,448/kg band** (§5.1), which is the only
internally consistent SPCX series on the table.

---

## 15. What would change this table — triggers

| # | Trigger | What it would change | Status |
|---|---|---|---|
| **T1** | A filed **per-launch or per-kilogram** series at SPCX on any basis | every Falcon 9 basis-B cell converts from `MODELED`/ABSENT to `DEMONSTRATED`; the F5b floor becomes measurable | **NOT TRIGGERED** |
| **T2** | A **filed Electron payload mass** to a named orbit | the ceiling becomes a mass; the 1.00×–1.50× correction becomes a point instead of an upper bound | **NOT TRIGGERED** |
| **T3** | A **filed Starship payload mass ≥ 159 t** | rescues the "99% or more" claim from below the F5a floor; below that the claim stands falsified against F5a | **NOT TRIGGERED** |
| **T4** | A **filed Starship price or contracted rate** | Starship's row moves from 4 ABSENT cells to at least 1 populated | **NOT TRIGGERED** — zero customer launches |
| **T5** | A **second F5c vehicle** with a filed price AND a filed cost | tests whether the F5c generalisation is a one-vehicle result | **NOT TRIGGERED** — FLY files neither |
| **T6** | A **Neutron first flight** with a per-launch cost disclosure in RKLB's existing metric form | Neutron B converts from ABSENT to `DEMONSTRATED` — the cheapest available trigger, since the form already exists at Electron | **NOT TRIGGERED** |
| **T7** | A **filed Falcon 9 payload-mass-per-mission figure** on the mass-to-orbit definition | rescues basis A from denominator-failure | **NOT TRIGGERED** |
| **T8** | A **filed pro forma revenue-by-type** at FLY | resolves FLY's `UNRESOLVED` growth rates — not a curve cell | **NOT TRIGGERED** |

**T6 is the trigger this table would most like to see**, because it is the only one that requires no new
disclosure *form* — merely a first flight and the same table RKLB already files for Electron. **T3 and T4 are
the highest-value resolutions** because Starship carries four of the thirteen absences.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Revenue and Cost Per Launch: Q2 2026 revenue per launch $9.1M and cost per launch $4.4M; Q2 2025 $7.9M and $5.0M; and the HASTE mission-mix sentence - | [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37) |
| Q1 2026 and Q1 2025 revenue per launch $9.3M / $7.1M and cost per launch $5.4M / $5.7M, filed natively | [📄 RKLB 10-Q p.31](https://agentii.ai/v/RKLB/sec104/31) |
| Electron filed only as "up to 300 kg" to low Earth orbit across inclinations from 38 to 120 degrees - a CEILING, with no mass-to-orbit metric filed in | [📄 RKLB 10-K p.8](https://agentii.ai/v/RKLB/sec87/8) |
| Electron "up to 300 kg" - the second of two filing instances of the ceiling | [📄 RKLB 10-K p.7](https://agentii.ai/v/RKLB/sec87/7) |
| Basis C is structurally unconstructible: "Management does not regularly review either reporting segment's total assets or operating expenses. This is  | [📄 RKLB 10-Q p.33](https://agentii.ai/v/RKLB/sec109/33) |
| Launch Services revenue $44,586 + Space Systems $189,480 = $234,066 = filed total revenues; Products $0 / Services $44,586 for Launch Services | [📄 RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32) **(newly surfaced)** |
| FY per-launch series and the FY2023 cost figure filed as excluding a $2.1M retention-credit benefit and a $4.1M contract-loss-reversal benefit | [📄 RKLB 10-K p.46](https://agentii.ai/v/RKLB/sec87/46) |
| Space segment table, five columns in the order [Q2 2026, Q1 2026, Q2 2025, H1 2026, H1 2025]: customer launches 10/7/9/17/21; total launches 38/40/46/ | [📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7) |
| Mass-to-orbit definition (total kilograms of payload delivered from all successful orbital and flight tests, excluding failed or scrubbed attempts); " | [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35) |
| "For launches of our Starlink satellites, the Company does not recognize any inter-segment revenue, rather those launch costs are capitalized in satel | [📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36) |
| Revenue mix by type: Launch Services 67.4% against Launch and Development 32.6%; the Space segment cost-of-revenue definition including "second stages | [📄 SPCX 10-Q p.37](https://agentii.ai/v/SPCX/sec8/37) |
| "Starship aims to quadruple payload capacity and reduce launch costs by 10x compared to our Falcon 9 rocket" (Bret Johnsen) | [📄 SPCX earnings call transcript p.3](https://agentii.ai/v/SPCX/ect1/3) |
| "We are the only U.S. company with a liquid-powered orbital launch vehicle in the 1,000-kilogram payload class." and "We operate as a single reportabl | [📄 FLY 10-Q p.34](https://agentii.ai/v/FLY/sec21/34) |
| Alpha described only as a "1,000-kilogram payload class" - the class label appears four times across two filings and is never accompanied by a mass, a | [📄 FLY 10-K p.7](https://agentii.ai/v/FLY/sec16/7) |
| "Alpha is the only provider of small size launch that has achieved orbit and addresses a critical gap in the market in the 1,000 kilograms category";  | [📄 FLY 10-K p.9](https://agentii.ai/v/FLY/sec16/9) |
| Launch revenue recognized on "the initiation of the launch" - POINT IN TIME, against RKLB's over-time HASTE recognition | [📄 FLY 10-Q p.16](https://agentii.ai/v/FLY/sec21/16) |
