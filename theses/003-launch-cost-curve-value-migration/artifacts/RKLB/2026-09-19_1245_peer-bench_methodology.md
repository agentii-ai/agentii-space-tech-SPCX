---
thesis_id: "003-launch-cost-curve-value-migration"
# The contract declares `pillar` as a scalar with an enum (artifact-frontmatter.yaml line 12).
# T062 brackets this artifact `[PIL-1/PIL-4]` and it discharges both: §2 IS P1's comparison
# table and §7 applies P4's F5b floor to Neutron. Recorded in the two-value form the task
# specifies, following the precedent at 002's
# artifacts/SPCX/2026-09-18_1500_business-model_methodology.md. NOT recorded silently — the
# declared type is scalar and this is a deviation from it. Primary pillar is PIL-1 (§2 is the
# deliverable); PIL-4 is carried second. The spec's skill-deployment matrix ALSO tags this row
# (P1, **P3**, **P4**) — PIL-3 is *served* by §3 (the demonstrated-vs-claimed census) but is not
# in the task's bracket, so it is named here in the comment rather than added to the field.
# Neither `check_contract.py` nor `check_citations.py` reads this field.
pillar: cross   # multi-pillar: {PIL-1, PIL-4} — 'cross' is the enum-valid value; check_contract does not validate this field, so a pillar SET passed silently. Stated in the body.
ticker: RKLB
skill: peer-bench
mode: methodology
generated_at: 2026-09-19T12:45:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
# skill_pin per impl-brief-003.md §2, the peer-bench row of the validated table. Canonical form
# (12 lowercase hex) confirmed against `tools/check_contract.py` rule `skill_pin_wellformed`,
# which was added 2026-09-19 precisely because four incompatible VALUES — including
# `registry-1.0.0`, a whole-registry version that pins nothing — previously validated
# identically. This pin is a per-skill hash, not a registry version.
skill_pin: "8c91d57a0d74"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: "DA-01"
    chosen_reading: "the four bases are A (customer list price), A′ (issuer-realized variant), B (marginal cost per launch — THE ONLY BASIS THAT TESTS THE F5 FLOOR) and C (fully-loaded amortized). Every basis a vehicle has is reported in §2 and no single basis is adopted as 'the' answer. The spread across bases IS the finding (§4)."
  - da_id: "DA-02"
    chosen_reading: "denominator orbit. Every entry on §2's table is LEO and the column is mandatory, because a $/kg without its orbit is a different number. One mismatch is carried rather than hidden: SPCX's filed mass-to-orbit series is ORBIT-AGNOSTIC ('deploy to orbit'), so substituting it into a LEO-denominated comparison is a stated DA-02 contamination, not a clean LEO figure."
  - da_id: "DA-03"
    chosen_reading: "architecture label, one of fully_expendable / partially_reusable / fully_reusable. A bare 'reusable: true' fails. Applied per vehicle in §2 and per F5 tier in §7; the two are one-to-one by contract `floor_architecture_consistency`."
  - da_id: "DA-07"
    chosen_reading: "capacity and delivered mass are held distinct. Electron's 300 kg and Neutron's ~13,000 kg are FILED CAPACITY (nameplate), not delivered mass; Falcon 9's 22,800 kg is a published spec with no filing page; SPCX's customer payloads (87 t, Q2 2026) are DELIVERED mass. Every $/kg in §2 names which of the two its divisor is."
  - da_id: "DA-08"
    chosen_reading: "'customer launch' = an external payload is the primary payload. Internal launches are excluded from every customer-denominated basis, and the exclusion is quantified (Falcon 9 Q2 2026: 10 customer of 38 total = 26.3%). The reason is filed: internal launch costs are capitalized in satellites rather than expensed through the Space segment, so an internal launch has no Space-segment revenue and no Space-segment cost of revenue."
  - da_id: "DA-21"
    chosen_reading: "segment boundaries are issuer-drawn. SPCX's Space segment boundary is the CUSTOMER boundary — 'Our Space segment revenue only reflects our customer launches and customer activities' — so a Space-segment $/kg is a $/kg over 26.3% of the mass moved, by construction, not by error."
  - da_id: "DA-25"
    chosen_reading: "an issuer-defined per-unit metric that is not reproducible from the audited tables. CONFIRMED at both RKLB metrics (§8.3): 'cost per launch' x missions does not equal Launch Services cost of revenues in any of four periods, and 'revenue per launch' x missions does not equal Launch Services revenues in any of four periods. Both are normalisations; neither is a segment line restated per launch."
  - da_id: "DA-30"
    chosen_reading: "two bases on one concept collapsed without a basis field. This artifact reports five distinct numerators over four distinct denominators for Falcon 9 alone (§4) and three distinct SPCX $/kg figures that differ 12.8x from ONE filing (§5). No SPCX or RKLB $/kg is quoted here without its basis and its denominator in the same row."
evidence_grade: DEMONSTRATED
# P11 / contract rule `deal_security_tagging`. RKLB trades as a standalone pre-merger security
# in this corpus's frame; the tag is mandatory and is not a statement about any announced
# transaction.
deal_security_basis: standalone_pre_merger
citations:
  - figure: "RKLB sec109 p.33"
    ticker: RKLB
    citation_id: sec109
    page_no: 33
    url: https://agentii.ai/v/RKLB/sec109/33
    located_via: read_source_pages
  - figure: "RKLB sec109 p.37"
    ticker: RKLB
    citation_id: sec109
    page_no: 37
    url: https://agentii.ai/v/RKLB/sec109/37
    located_via: read_source_pages
  - figure: "RKLB sec87 p.7"
    ticker: RKLB
    citation_id: sec87
    page_no: 7
    url: https://agentii.ai/v/RKLB/sec87/7
    located_via: read_source_pages
  - figure: "RKLB sec87 p.8"
    ticker: RKLB
    citation_id: sec87
    page_no: 8
    url: https://agentii.ai/v/RKLB/sec87/8
    located_via: read_source_pages
  - figure: "RKLB sec87 p.46"
    ticker: RKLB
    citation_id: sec87
    page_no: 46
    url: https://agentii.ai/v/RKLB/sec87/46
    located_via: read_source_pages
  - figure: "RKLB sec104 p.31"
    ticker: RKLB
    citation_id: sec104
    page_no: 31
    url: https://agentii.ai/v/RKLB/sec104/31
    located_via: read_source_pages
  - figure: "RKLB ect21 p.3"
    ticker: RKLB
    citation_id: ect21
    page_no: 3
    url: https://agentii.ai/v/RKLB/ect21/3
    located_via: read_source_pages
  - figure: "SPCX sec7 p.7"
    ticker: SPCX
    citation_id: sec7
    page_no: 7
    url: https://agentii.ai/v/SPCX/sec7/7
    located_via: read_source_pages
  - figure: "SPCX sec7 p.6"
    ticker: SPCX
    citation_id: sec7
    page_no: 6
    url: https://agentii.ai/v/SPCX/sec7/6
    located_via: read_source_pages
  - figure: "SPCX sec8 p.36"
    ticker: SPCX
    citation_id: sec8
    page_no: 36
    url: https://agentii.ai/v/SPCX/sec8/36
    located_via: read_source_pages
  - figure: "FLY sec21 p.34"
    ticker: FLY
    citation_id: sec21
    page_no: 34
    url: https://agentii.ai/v/FLY/sec21/34
    located_via: read_source_pages
  - figure: "FLY sec21 p.16"
    ticker: FLY
    citation_id: sec21
    page_no: 16
    url: https://agentii.ai/v/FLY/sec21/16
    located_via: read_source_pages
  - figure: "FLY sec16 p.7"
    ticker: FLY
    citation_id: sec16
    page_no: 7
    url: https://agentii.ai/v/FLY/sec16/7
    located_via: read_source_pages
key_metrics:
  electron_basis_a_cost_per_kg_leo_300kg_q2_2026: 30333
  electron_basis_b_cost_per_kg_leo_300kg_q2_2026: 14667
  falcon9_basis_a_cost_per_kg_leo_usd: 2939
  demonstrated_cost_per_kg_vehicle_and_issuer_pairs_of_5: 1
---

# RKLB × peer-bench — the cross-vehicle $/kg table, and the fact that one cell on it is measured

**The finding.** Across the five vehicles that carry 003's cost curve, **exactly one `$/kg`
cell is `DEMONSTRATED` without qualification** — Electron's, on both of its bases, from a
per-launch metric RKLB alone discloses. Basis B is the only basis that tests the F5 floor, and
it is `DEMONSTRATED` for **one vehicle-and-issuer pair in the universe**, `MODELED` for one, and
**absent for three**. On the 5 × 4 matrix of vehicles against DA-01 bases, **2 of 20 cells are
`DEMONSTRATED`, 2 are `CLAIMED`, 1 is `MODELED`, 2 are arithmetic on filed cells with our
division, and 13 are absent.** A comparison table whose most-populated column is "absent" is the
result, not a defect in the search.

Two structural consequences follow, and both are reported rather than resolved.

**First, the spread is in the numerator, not the denominator — and the two are separable.** Four
bases over ONE Falcon 9 mission span **7.5×–12.6×** (registered as 7–13×). That ratio is
*denominator-invariant*: it is the ratio of the numerators, and any denominator cancels. The
separate disease 002 diagnosed — pairing customer revenue with a vehicle-capacity divisor — is a
**multiplicative 1.61×–2.62×** applied to every base equally. Collapsing the two into one
"spread of 7–13×" hides that they need different remedies.

**Second, the single source is RKLB, it is 003's own ticker, and it will not widen.** FLY's 10-Q
contains no `cost per launch` and no `revenue per launch`. Neither does SPCX's. **`cost per
launch` and `revenue per launch` are disclosed by RKLB alone**, and the anchor is therefore
permanent rather than transitional — 003:PIL-3 rests on it, and 003:PIL-1's floor test has
exactly one measured instance to run against.

---

## 1. Method, stated once so it can be disputed

**The grading rule applied to every `$/kg` cell in §2.** A cell is graded by its *weakest
admissible input*:

| Grade | Condition | Cells in §2 |
|---|---|---|
| `DEMONSTRATED` | a **filed per-launch metric** divided by a **filed payload cell**; the only operation we add is the division | 2 |
| `DEMONSTRATED` (figures) / `MODELED` (division) | every input is a filed segment cell, but the population pairing is ours | 2 |
| `CLAIMED` | the numerator is an issuer assertion or a published spec, whatever the denominator | 2 |
| `MODELED` | the numerator is our own cost construction | 1 |
| **ABSENT** | no numerator exists on that basis | 13 |

`MODELED` is not a weaker `DEMONSTRATED`; it is a different kind of object. **A `MODELED` input
can never satisfy a falsifier** (brief §3 rule 2, carried from 003 spec §1c), so the 13 absent
cells and the 1 `MODELED` cell are not evidence for or against the curve — they are the shape of
what is not yet testable.

**Denominator discipline.** Every row names its denominator orbit and its denominator *mass
kind*. Three kinds appear: **capacity** (nameplate, claimed or published), **delivered customer**
and **delivered total**. A $/kg without its basis, its orbit and its payload is not a number — it
is a different number.

**Reuse discipline.** DA-03 architectures are stated per vehicle and map one-to-one onto the F5
tiers (§7). No vehicle on this table is outside F5, so `tier: none` does not appear.

---

## 2. The cross-vehicle table — the deliverable

Denominator orbit is **LEO** for every row (DA-02). Where a figure is restated on a second
denominator the row says so. `$/kg` figures are USD per kilogram to LEO.

### 2.1 Falcon 9 — SPCX — Falcon-class, partially reusable

| Basis | Numer-ator | $/kg, capacity denominator (22,800 kg) | $/kg, realized customer denominator (8,700 kg) | $/kg, realized all-launch denominator (12,760 kg) | Grade |
|---|---|---|---|---|---|
| **A** — customer list price | ~$67M/launch | **$2,939/kg** ⚠️ **denominator-failed** | $7,701/kg | $5,251/kg | `CLAIMED` |
| **A** (Launch-Services-only boundary — 002's A″) | $648M ÷ 10 = $64.8M | $2,842/kg | **$7,448/kg** | $5,078/kg | `DEMONSTRATED` figs / `MODELED` div |
| **A′** — Space segment revenue | $962M ÷ 10 = $96.2M | $4,220/kg | $11,057/kg | $7,539/kg | `DEMONSTRATED` figs / `MODELED` div |
| **B** — marginal cost | ~$12–20M | **$526–877/kg** | $1,379–2,299/kg | $940–1,567/kg | **`MODELED`** |
| **C** — fully loaded | $1,504M ÷ 10 = $150.4M | **$6,596/kg** | $17,287/kg | $11,787/kg | `DEMONSTRATED` figs / `MODELED` div |

**The 22,800 kg denominator is failed, not merely claimed.** `"22.8"` returns zero pages across
SPCX's filings — the figure is a published vehicle spec with no filing behind it. The registered
`$2,939/kg` is therefore a number divided by an unfiled capacity, and the third column exists to
show what happens when it is divided by a realized mass instead.

**Basis C is not a launch cost.** Its $150.4M numerator decomposes as cost of revenue $32.9M
(21.9%), R&D $107.6M (**71.5%**), SG&A $9.9M (6.6%). **71.5% of the fully-loaded `$6,596/kg` is
Starship development spending charged in the same quarter** — an R&D programme for a *different*
vehicle, expensed through the same segment. Per-kg, the three components are $1,443/kg,
**$4,719/kg** and $434/kg. Any consumer of basis C is consuming a Starship R&D rate, not a
Falcon 9 cost.

**The closest SPCX analogue to a marginal cost is not basis B.** It is cost of revenue alone:
$32.9M ÷ 8,700 kg = **$3,782/kg** at the realized customer denominator ($1,443/kg at capacity).
It sits *between* A″ and B, and it is the reason §4 reports the spread rather than picking a
winner — where the "cost" line is drawn inside the P&L moves the answer by ~2.7×.

**Per-period matched-pair series, basis A″ at the customer denominator** — this is the band
003:PIL-4's falsifier is registered against:

| Period | Launch Services revenue | Customer payloads | Customer launches | $/kg |
|---|---|---|---|---|
| Q2 2026 | $648M | 87 t | 10 | **$7,448/kg** |
| Q1 2026 | $330M | 45 t | 7 | $7,333/kg |
| H1 2026 | $978M | 132 t | 17 | **$7,409/kg** |
| Q2 2025 | $490M | 88 t | 9 | **$5,568/kg** |
| H1 2025 | $1,056M | 163 t | 21 | $6,479/kg |

**Band $5,567–7,448/kg, 1.34×.** The lower edge is registered at `$5,567`; the cell computes to
`$5,568` (490 ÷ 88 = 5.56818) and the difference is 002's rounding of the quotient, carried
unchanged because 003:PIL-4's falsifier text carries the literal `5567`.

### 2.2 Starship — SPCX — fully reusable

| Basis | Denominator | $/kg | Grade |
|---|---|---|---|
| A, A′, B, C | — | **ABSENT on all four bases** | — |

No price, no cost, no contracted rate, and no filed payload mass. The 100,000 kg-to-LEO figure is
a **published vehicle spec and is not in any filing in this corpus**. The only two Starship
flights in the corpus are described as **suborbital** (Flight 12, May 2026: "first suborbital
mission"; Flight 13, July 2026), so Starship has no orbital delivery to denominate even if a
numerator existed. Resolving source in §8.

### 2.3 Electron — RKLB — fully expendable

| Basis | Filed per-launch cell | $/kg at 300 kg to LEO | Grade |
|---|---|---|---|
| **A** — revenue per launch | $9.1M (Q2 2026) | **$30,333/kg** | **`DEMONSTRATED`** |
| **B** — cost per launch | $4.4M (Q2 2026) | **$14,667/kg** | **`DEMONSTRATED`** |
| **A′** | — | ABSENT | A′ is defined SPCX-only (spec §1b) and has no RKLB counterpart |
| **C** — fully loaded | — | **ABSENT, permanently** | not a pending disclosure — see §8.1 |

**The denominator is filed twice.** 300 kg to LEO appears on two pages of one 10-K: "up to
300 kg" and "up to 300 kg to low earth orbit across a wide range of orbital inclinations from 38
to 120 degrees". It is a **capacity** figure (DA-07), never a delivered mass.

**The full series, seven periods, one vehicle.** Both cells are filed in every period; the Q1
2026 cells are filed directly in the Q1 10-Q.

| Period | Missions launched | Cost/launch | Revenue/launch | Basis B $/kg | Basis A $/kg | (rev − cost)/rev |
|---|---|---|---|---|---|---|
| FY2023 | 10 | $7.0M | $7.1M | $23,333/kg | $23,667/kg | 1.4% |
| FY2024 | 16 | $5.7M | $7.8M | $19,000/kg | $26,000/kg | 26.9% |
| FY2025 | 21 | $4.8M | $8.5M | $16,000/kg | $28,333/kg | 43.5% |
| Q2 2025 | 5 | $5.0M | $7.9M | $16,667/kg | $26,333/kg | 36.7% |
| H1 2025 | 10 | $5.3M | $7.5M | $17,667/kg | $25,000/kg | 29.3% |
| Q1 2026 | 6 | $5.4M | $9.3M | $18,000/kg | $31,000/kg | 41.9% |
| Q2 2026 | 6 | $4.4M | $9.1M | **$14,667/kg** | **$30,333/kg** | **51.6%** |
| H1 2026 | 12 | $4.9M | $9.2M | $16,333/kg | $30,667/kg | 46.7% |

**One vehicle is now eight filed period-cells on each side — the curve's only measured segment.**
Across it: **basis B falls −37.1%** ($23,333 → $14,667/kg) while **basis A rises +28.2%**
($23,667 → $30,333/kg), and the spread between the two widens from **1.01× to 2.07×**. On the
stated demand side of 003:PIL-6, that is the whole claim in one line: the released cost was kept,
not passed through.

**Caveat, carried from 002 and not weakened here.** FY2023's $7.0M excludes a $2.1M retention-credit
benefit and a $4.1M contract-loss-reversal benefit credited to Launch Services cost of revenue.
The filed metric is already the conservative reading. And the series is noisy: the Q2 2025
zero-HASTE control diverges −15.3% / −22.9% from the segment table (§8.3), so the **direction** is
robust and the **level** is not.

### 2.4 Neutron — RKLB — partially reusable (forward, unflown)

| Basis | Cell | $/kg at ~13,000 kg to LEO | Grade |
|---|---|---|---|
| **A** — disclosed ASP | $50–55M/launch | **$3,846–4,231/kg** | `CLAIMED` (numerator) ÷ filed (payload) |
| **B** — marginal cost | — | **ABSENT** — not flown, no cost per launch can exist | — |
| **C** — fully loaded | — | **ABSENT** — structurally unconstructible at RKLB (§8.1) | — |

~13,000 kg is filed twice, and **both filings specify the reusable configuration**. The payload of
the expendable configuration is nowhere filed, so the implied $/kg is for a configuration RKLB
has not said it will fly first.

**The PIL-4 payload bar, as arithmetic.** $50–55M at $5,567–7,448/kg implies **6,713–9,882 kg**
of the 13,000 kg nameplate. `MODELED`, and it is the number 003:PIL-4 is about — the medium-lift
case closes only above the bar, and it rests on F5b, not F5a, because the recoverable stage is
the *first* stage.

### 2.5 Alpha — FLY — fully expendable

| Basis | Cell | Grade |
|---|---|---|
| A, A′, B, C | **ABSENT on all four bases** | — |
| payload_kg (DA-02 companion) | **ABSENT — "1,000 kilograms payload class" is a class label** | — |

Alpha cannot be placed on the curve at all, and not because FLY is small. FLY files no per-launch
cost and no per-launch revenue (§3), and its payload is a **class label** in five statements
across two filings, with no mass, no orbit and no configuration. FLY's own market framing puts
the category at "satellites between 200 kilograms to 1,200 kilograms" — **a 6× interval**, so even
if a numerator existed the class label alone would produce a 6× $/kg band. Resolving source in
§8.2.

### 2.6 The matrix as the contract sees it

Vehicle × DA-01 basis, with the F5 tier each vehicle's architecture forces:

| Vehicle | Operator | DA-03 architecture | F5 tier | A | A′ | B | C |
|---|---|---|---|---|---|---|---|
| Falcon 9 | SPCX | partially_reusable | **F5b** | `CLAIMED` | DEMO-fig/MODEL-div | **`MODELED`** | DEMO-fig/MODEL-div |
| Starship | SPCX | fully_reusable | **F5a** | ABSENT | ABSENT | ABSENT | ABSENT |
| Electron | RKLB | fully_expendable | **F5c** | **`DEMONSTRATED`** | n/a | **`DEMONSTRATED`** | ABSENT (permanent) |
| Neutron | RKLB | partially_reusable | **F5b** | `CLAIMED` | ABSENT | ABSENT | ABSENT |
| Alpha | FLY | fully_expendable | **F5c** | ABSENT | ABSENT | ABSENT | ABSENT |

**20 cells: 2 `DEMONSTRATED` · 2 `DEMONSTRATED`-figures/`MODELED`-division · 2 `CLAIMED` ·
1 `MODELED` · 13 ABSENT.**

---

## 3. The demonstrated-vs-claimed split — the stark part

**Counts, on the rule stated in §1:**

| Population | `DEMONSTRATED` | Total | Share |
|---|---|---|---|
| **Basis B** (the F5-floor-testing basis) | **1** (Electron/RKLB) | 5 vehicles | **20%** |
| All DA-01 basis cells | **2** | 20 | **10%** |
| Adding arithmetic-on-filed-cells | 4 | 20 | 20% |
| Vehicle-and-issuer **pairs** with any `DEMONSTRATED` `$/kg` | **1** (RKLB) | 5 | **20%** |

**The single-source anchor, stated explicitly because 003:PIL-3 rests on it:**
`cost per launch` and `revenue per launch` are disclosed by **RKLB alone**. FLY's 10-Q contains
neither — a tool-located search of FLY's whole 10-Q for both strings returns only the Launch
revenue-recognition policy (cost-to-cost input method) and the revenue-disaggregation note, two
different concepts. SPCX's 10-Q likewise returns only a revenue-recognition page, and SPCX's
Key Business Metrics section discloses **Starlink subscribers, Starlink ARPU and nameplate
compute draw — Connectivity and AI only. There is no Space-segment cost metric and no $/kg
anywhere in it.**

**And it will not widen.** FLY's absence is not an EGC accommodation: FLY's 10-Q does not carry
the reduced-disclosure profile that would excuse it, and an absence that a later filing could
fill would be `UNRESOLVABLE-FROM-PLATFORM`, not the `UNRESOLVABLE-FROM-PUBLIC-SOURCES` class this
is. For SPCX the structural reason is filed: internal launch costs are **capitalized in
satellites** rather than expensed through the Space segment, so the segment RKLB-style metric
would have to be built across a boundary SPCX does not report on.

**Consequence for 003:PIL-3.** Its metric is the share of universe cost-reduction claims with a
filed, flown or audited basis, threshold 0.5, op `<`. On the claims that carry a quantum, stated
here so a reader can dispute the set:

| Claim | Quantum | Basis | Grade |
|---|---|---|---|
| SPCX — Starship "reduce the cost to orbit by **99% or more** relative to the historical average" | relative to an unnamed average | none | `CLAIMED` |
| RKLB — Neutron reusable first stage "enabling … **decreased launch costs** for customers" | direction only | none | `CLAIMED` |
| RKLB — "cost of launch vehicles **to decline**" | direction only | none | `CLAIMED` |
| RKLB — Electron cost per launch $7.0M → $4.4M | **−37.1%**, both cells filed in every period of the 8-period series | filed per-launch metric | **`DEMONSTRATED`** |

**1 of 4 = 25% < 50%.** 003:PIL-3's falsifier does **not** fire — and it does not fire for the
right reason, which is that the one demonstrated cost reduction is on the *expendable* vehicle
everyone has written off, not that the sector's claims were verified.

---

## 4. The basis spread, reported and not collapsed

**One Falcon 9 mission, Q2 2026, four registered bases, one denominator held constant (22,800 kg
— the denominator 001 used, and the one that is failed):**

```
  B   ~$525–875/kg     marginal cost            MODELED
  A   ~$2,939/kg       customer list price      CLAIMED   (denominator-failed)
  A′  ~$4,220/kg       Space segment revenue     DEMO-fig / MODEL-div
  C   ~$6,596/kg       fully loaded              DEMO-fig / MODEL-div
  ─────────────────────────────────────────────────────────
  span  $525 → $6,596/kg  =  7.5×–12.6×     (registered as 7–13×)
```

**Everything on the table above the fold is `$500/kg` to `$6,600/kg` around ONE mission, and the
span is the *basis*, not the economics.** Two readers given "$2,939/kg" and "$6,596/kg" hold the
same asset and disagree about its unit economics by 2.2×; a third told "$525/kg" believes the
F5a floor has already arrived on a partially reusable vehicle.

**The spread is denominator-invariant — and that is the point.** Restating all five Falcon 9
numerators on the realized *customer* denominator (8,700 kg) gives $1,379–2,299 / $7,448 /
$7,701 / $11,057 / $17,287 per kg. The span is **7.5×–12.6× again**: 17,287 ÷ 2,299 = 7.52 and
17,287 ÷ 1,379 = 12.54. Identical, because the ratio of numerators is unchanged when one
denominator replaces another. So:

- **basis choice = 7.5×–12.6×**, a pure numerator effect; and
- **denominator choice = 1.61×–2.62×**, a separate multiplier applied to *every* basis equally.

002's finding that "the spread 001 reported is largely an artefact of pairing customer revenue
with a vehicle-capacity divisor" is right about *which published number is wrong* — the $2,939 —
and it does not reduce the **basis** spread, which survives any denominator. The two defects
compound into a single figure if they are reported as one; separated, one is a fixed data error
and the other is the structural finding DA-30 exists to protect.

**Electron's own two-basis spread is 2.07×** ($30,333 vs $14,667/kg) on one denominator, one
filing, one period, and this time **both readings are `DEMONSTRATED`**. So even in the only
vehicle where the evidence permits a firm comparison, price sits at **2.07× measured cost** — and
that ratio, unlike Falcon 9's, is not a modelling artefact. It is the F5c floor and the F5c price,
measured in the same quarter.

---

## 5. The SPCX spread is 12.8× from ONE filing

Three `$/kg` figures, all H1 2026, all from one page of one exhibit, all arithmetically correct,
none comparable:

| Numerator | Denominator | $/kg | What it answers |
|---|---|---|---|
| Launch Services $978M | customer payloads 132 t | **$7,409/kg** | what a customer's kg costs on the customer boundary |
| Launch Services + Launch & Development $1,581M | customer payloads 132 t | **$11,977/kg** | what the whole Space segment earns per customer kg |
| Launch Services $978M | **mass to orbit 1,041 t** | **$939/kg** | revenue per kg the company actually put up |

**$11,977 ÷ $939 = 12.75 — a 12.8× spread from one filing.** Every one of the three is correct.
The first is a price; the second is not a price because Launch & Development revenue comes from
contracts with terms **up to fourteen years** and is largely spacecraft and mission-services work,
not launch; the third is not a price either, because it divides customer revenue by a mass that is
**87.2% internal** (908 t internal of 1,041 t total) and it is a **DA-02 contaminated** divisor —
SPCX's mass-to-orbit series is orbit-agnostic, not LEO.

**And on the matched basis, the direction of travel is the opposite of a cost curve.**

| | Q2 2025 | Q2 2026 | Change |
|---|---|---|---|
| Launch Services revenue | $490M | $648M | **+32.2%** |
| Customer payloads | 88 t | 87 t | **−1.1%** |
| Basis A″ $/kg | $5,568/kg | **$7,448/kg** | **+33.8%** |
| Mass to orbit (all) | 652 t | 485 t | **−25.6%** |

**$/kg rose 33.8% while the mass actually delivered to orbit fell 25.6%.** The $/kg movement is
entirely revenue-side (+32.2% on −1.1% of payload) — a price and mix effect, not a cost effect.
For a cost curve the operative variable is the fourth row. Any comparison that puts SPCX and RKLB
`$/kg` side by side without this table is comparing a price series with a cost series.

The registered `+33.8%` is carried as `+33.7%` in the task register; 7,448.28 ÷ 5,568.18 = 1.3376.
Same ratio, quotient rounded to whole dollars.

---

## 6. Electron's reconversion — what it gives, and what does not reproduce

**The carried correction, inherited and not recomputed:** 001's published Electron $/kg figures
are **1.79×–2.62× too low**, and the DA-25 gap is present in **4 of 4** periods, against a ±15%
tolerance. Both of 001's cells are therefore **TO BE RECONVERTED, DO NOT INHERIT**.

**What the reconversion gives, on the carried factor:**

| Basis | 001's published value | ×1.79 | ×2.62 | Reconverted range |
|---|---|---|---|---|
| A — revenue per launch | $30,333/kg | $54,296/kg | $79,472/kg | **$54,296–79,472/kg** |
| B — cost per launch | $14,667/kg | $26,254/kg | $38,427/kg | **$26,254–38,427/kg** |
| Both, corner | — | — | — | **×2.25 = the corner 002's channels give** |

**What RKLB's own record can build.** Unlike SPCX, **RKLB files no mass-to-orbit metric in any
period** — there is no filed delivered-mass denominator to restate against, and
`list_xbrl_concepts(search="payload")` returns zero rows, so no XBRL path exists either. Only two
channels are open, both from 002's Electron denominator artifact:

- **Channel O** — the filed orbit envelope runs to 120°, and the SSO end of a small-launch vehicle
  is ~200 kg, not 300 kg: **+50.0%**, period-independent.
- **Channel M** — 2 of 6 Q2 2026 missions were HASTE, suborbital, delivering no mass to LEO:
  **0 to +50%**.
- **Corner: +125% → ×2.25.**

**The honest verdict, and it is a finding rather than a hedge.** RKLB's own record supports
**1.50×–2.25×**. The carried correction claims **1.79×–2.62×**. The intervals overlap on
**1.79–2.25**, and the overlap is real: the lower half of the carried correction reproduces from
RKLB's own filing.

**But the endpoints `1.79×` and `2.62×` are SPCX's.** They are the realized-denominator factors
for Falcon 9 exactly — 22.8 ÷ 12.76 = **1.79**, 22.8 ÷ 8.70 = **2.62** — derived from SPCX's filed
mass-to-orbit table, which RKLB does not have. And "four of four periods" is Electron's DA-25
period count, not a $/kg restatement. **The register's correction fuses a Falcon 9 denominator
factor with an Electron period count.** Recorded here rather than silently inherited: the
*direction* of the correction is confirmed and 001's figures must not be inherited; the portion
of the magnitude above 2.25× is `UNRESOLVABLE-FROM-PUBLIC-SOURCES` at RKLB, and the remedy is for
the register to name which issuer each endpoint came from.

**This is an A29-class item — a correction that exists and is not read at the scope where it
applies — and it propagates: 003:PIL-1's table and 003:PIL-4's band both inherit it.**

### 6.1 The arithmetic-mean assumption is now exact, not provisional

003 spec's open question Q-2 asked whether RKLB's half-year per-launch metric is an arithmetic
mean over the period's missions. Q1 2026 is filed directly, so it is testable:

- cost: 2 × $4.9M − $4.4M = **$5.4M** — matches the filed Q1 2026 cell exactly;
- revenue: 2 × $9.2M − $9.1M = **$9.3M** — matches the filed Q1 2026 cell exactly.

**Exact on both sides.** Q-2 closes provisionally: the mean is confirmed; the *weighting* is not
testable, because every half-year in the series is composed of two equal-count quarters (5+5, 6+6).

### 6.2 Both Electron metrics are normalisations, in four of four periods

Against the closest filed comparator — the Launch Services segment line — neither metric is a
segment line restated per launch:

| Period | `revenue/launch` × missions | LS revenues (filed) | Gap | `cost/launch` × missions | LS cost of revenues (filed) | Gap |
|---|---|---|---|---|---|---|
| Q2 2026 | $54.6M | $44.586M | **+22.5%** | $26.4M | $25.476M | +3.6% |
| Q2 2025 | $39.5M | $46.646M | **−15.3%** | $25.0M | $32.426M | **−22.9%** |
| H1 2026 | $110.4M | $108.249M | +2.0% | $58.8M | $60.916M | −3.5% |
| H1 2025 | $75.0M | $82.238M | −8.8% | $53.0M | $60.801M | −12.8% |

Both half-year periods reconcile within ±13%; **both quarter periods breach ±15%** on at least the
revenue side. The quarter-level revenue gap is what 003:PIL-5 names — the filing itself gives the
cause: 2 of 6 Q2 2026 missions were HASTE, **recognized over time and partially recognized in
prior quarters**, while all 5 of Q2 2025's were point-in-time. So the metric labelled "revenue per
launch" is defined as *average transaction price attributable to the launch obligations of the
period in which the launch occurs*, which is not the period's revenue. **The cost side is the
stabler series; the revenue side is the normalisation, and PIL-5's asymmetry is now quantified
rather than asserted** — with the caveat that the segment line includes "other launch revenue"
(contract termination and study revenue) that is not attributable to a mission, which cuts the
other way and is the reason the comparison is stated as a reconciliation of gaps rather than as a
derivation of either metric.

---

## 7. F5 applied per architecture — three tiers, exhaustive, and the registered inversion

| Tier | Architecture | Vehicles | Floor | Floor grade | `DEMONSTRATED` price? |
|---|---|---|---|---|---|
| **F5a** | fully_reusable | Starship | propellant-dominated; **$46–92/kg** at 100 t | **`MODELED`** | **No** |
| **F5b** | partially_reusable | Falcon 9, Neutron | expended upper stage, ~$8–12M → **$920–1,379/kg** at 8,700 kg | **`MODELED`** | **No** |
| **F5c** | fully_expendable | Electron, Alpha | whole-vehicle manufacture + all period costs → **$14,667/kg** at 300 kg | **MEASURED** at Electron; absent at Alpha | **Yes — Electron only** |

**Coverage check, per contract rule `floor_architecture_consistency`:** the three tiers map
one-to-one onto `{fully_reusable, partially_reusable, fully_expendable}`. All three are present on
this table, all three are populated, and no vehicle is left outside. `tier: none` is unused and
would be inadmissible here. **The F5 coverage gap was closed at constitution v1.3.0; this artifact
does not re-raise it.**

**F5a's derivation, shown not asserted.** ~4,600 t of propellant at $1–2/kg = $4.6–9.2M; ÷
100,000 kg = **$46–92/kg**. Hard floor: propellant is not recoverable and not substitutable. The
tier has **no demonstrated price**, and the vehicle it describes has **not delivered payload to
orbit in this corpus**.

**F5b's derivation, shown not asserted.** The recoverable stage returns; ~$8–12M of expended
second stage does not. At the realized customer denominator (8,700 kg) that is **$920–1,379/kg**;
at the capacity denominator (22,800 kg) it is $351–526/kg. Soft floor: it moves with upper-stage
manufacturing cost, which is exactly what RKLB says it is attacking, and exactly what
**Neutron's F5b, not F5a, economics rest on** — the reusable stage is the first stage.

**F5c's derivation, shown not asserted — and this is the inversion.**
F5c's floor is the whole vehicle, manufactured once and expended once. At Electron the numerator
is filed: *"actual costs of the launch vehicles that occur in the period … and all period costs in
the period of launch"*, $4.4M in Q2 2026; the denominator is filed: 300 kg. **$14,667/kg.**
F5c is the only one of the three floors that is **measured rather than derived from physics**,
and Electron is the only F5c vehicle where it can be measured — Alpha discloses no cost at all.

**The registered inversion, restated against this table because the table is where it is
visible.** F5a and F5b carry **three of five vehicles and 100% of the sector's quantum-bearing
cost claims** (§3), and **both of their floors are `MODELED`**. F5c carries the **only
`DEMONSTRATED` price in the universe**, and it sits **2.07× above its own measured floor** — not
below it. The sector's cost conversation is conducted about the architectures whose floor is
unproven; the architecture with a demonstrated price is the one the conversation treats as
obsolete.

**003:PIL-1's falsifier, evaluated.** `metric = count_of_universe_vehicles_with_a_demonstrated_
price_per_kg_to_LEO_below_their_architecture_applied_launch_cost_floor`, threshold 0, op `>`.
There is **one** vehicle with a demonstrated price (Electron) and its price is **above** its
applied F5c floor, 2.07×. **Count = 0. The falsifier does not fire** — on a population of one,
which is the honest scope of the statement.

---

## 8. What is absent, named, with the disclosure that would resolve it

### 8.1 RKLB basis C — permanently unconstructible, not pending

Basis C needs segment-level assets or opex. RKLB says, in the segment note, verbatim:

> **"Management does not regularly review either reporting segment's total assets or operating
> expenses. This is because in general, the Company's long-lived assets, facilities, and
> equipment are shared by each reporting segment."**

This is not a disclosure that will arrive. It is a filed statement that the allocation basis does
not exist inside the company. **Disposition: `UNRESOLVABLE-FROM-PUBLIC-SOURCES`, and permanently
so.** Resolving source: none — no future filing resolves it, because the constraint is the
issuer's own management structure rather than the platform's extraction. (`UNRESOLVABLE-FROM-
PLATFORM` would be the wrong class: there is nothing to extract.)

### 8.2 FLY's payload is a class label, so Alpha cannot be placed

"I,000-kilogram payload class" is filed five times across two filings, with **no mass, no orbit
and no configuration**. It is a market-positioning claim, not a denominator. **Disposition:
`UNRESOLVABLE-FROM-PUBLIC-SOURCES`.** Resolving source: a filed payload mass to a **named orbit** —
reachable via a NASA or USSF launch-services award stating the payload mass, a customer contract
disclosure, or a later FLY filing that states the mass rather than the class. **The class label
alone is not sufficient even if a numerator arrived:** FLY's own category interval (200–1,200 kg)
is 6×, so a class-denominated `$/kg` would carry a 6× band before any cost question is asked.

### 8.3 Starship has no `$/kg` on any basis, and no orbital delivery to denominate

No price, no contracted rate, no cost, no filed payload mass; the only two flights in the corpus
are suborbital; the Space segment's disclosed Key Business Metrics are Connectivity and AI only.
**Disposition: `UNRESOLVABLE-FROM-PUBLIC-SOURCES`.** Resolving source: **either** a filed or
contracted Starship price (a customer launch contract, or a segment revenue line attributable to
Starship), **or** a filed payload mass for a mission the filing describes as delivering to orbit —
at which point the 100,000 kg spec figure is replaced by a delivered mass and a basis can be
built. Until then the `99%-or-more` claim is a relative claim against an **unnamed** historical
average and cannot be evaluated on this table at all.

### 8.4 The remaining absences, each with its source

| Cell | Reason | Class | Resolving source |
|---|---|---|---|
| Neutron **B** | not flown; no cost per launch can exist before a first flight | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (transitional) | a per-launch cost disclosure in the first flight quarter's 10-Q, in RKLB's existing metric form |
| Neutron **C** | same structural bar as 8.1 | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (permanent) | none — see 8.1 |
| Falcon 9 **B** | no SPCX cost-per-launch disclosure exists; basis B is our cost construction | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a filed SPCX cost of launch services, or a segment line decomposable to a per-launch figure. 001 nominated NASA CRS / Commercial Crew contract values as a revealed-price **floor** — a `CLAIMED` resolution, not a `DEMONSTRATED` one |
| Electron **A′** | A′ is defined as the SPCX-specific realized variant; no RKLB counterpart exists | n/a — not an absence | none required; the basis does not apply |
| Propellant price | reachable but never disclosed by any issuer on this table | `REACHABLE-BUT-NOT-RECORDABLE` | already flagged in 002; carried, not re-derived |

**PRESENCE vs ABSENCE.** The 13 absent cells are `UNEXERCISED`, not `CLEAN`. Nothing in §2 is
evidence that an F5a or F5b floor holds — the tests could not run. And the two negative searches
that *did* run (§3) are recorded with the tool that found them, because a page number that was
not located is a guess, and a negative that was not searched is not a negative.

---

## 9. What this fixes for the three pillars it serves

- **003:PIL-1** — the comparison table exists, with 5 vehicles × 4 bases, every cell graded and
  every absence named with its resolving source. The curve's measured segment is **one vehicle,
  eight filed period-cells**, and the floor that is *measured* is F5c's.
- **003:PIL-3** — the demonstrated share is **2 of 20 cells, 1 of 5 vehicles, 25% of quantum-
  bearing cost-reduction claims**. Under half. The falsifier does not fire, and the reason is the
  inversion rather than the sector's rigour.
- **003:PIL-4** — the matched-pair band is **$5,567–7,448/kg, 1.34×**, confirmed on the customer
  boundary; Neutron's implied `$/kg` at the disclosed ASP is **$3,846–4,231/kg**, implying a
  **6,713–9,882 kg** payload bar against a 13,000 kg nameplate in the reusable configuration. The
  case rests on **F5b**, and F5b's floor is `MODELED`.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| RKLB sec109 p.33 | [📄 RKLB  p.33](https://agentii.ai/v/RKLB/sec109/33) **(newly surfaced)** |
| RKLB sec109 p.37 | [📄 RKLB  p.37](https://agentii.ai/v/RKLB/sec109/37) **(newly surfaced)** |
| RKLB sec87 p.7 | [📄 RKLB  p.7](https://agentii.ai/v/RKLB/sec87/7) **(newly surfaced)** |
| RKLB sec87 p.8 | [📄 RKLB  p.8](https://agentii.ai/v/RKLB/sec87/8) **(newly surfaced)** |
| RKLB sec87 p.46 | [📄 RKLB  p.46](https://agentii.ai/v/RKLB/sec87/46) **(newly surfaced)** |
| RKLB sec104 p.31 | [📄 RKLB  p.31](https://agentii.ai/v/RKLB/sec104/31) **(newly surfaced)** |
| RKLB ect21 p.3 | [📄 RKLB  p.3](https://agentii.ai/v/RKLB/ect21/3) **(newly surfaced)** |
| SPCX sec7 p.7 | [📄 SPCX  p.7](https://agentii.ai/v/SPCX/sec7/7) **(newly surfaced)** |
| SPCX sec7 p.6 | [📄 SPCX  p.6](https://agentii.ai/v/SPCX/sec7/6) **(newly surfaced)** |
| SPCX sec8 p.36 | [📄 SPCX  p.36](https://agentii.ai/v/SPCX/sec8/36) **(newly surfaced)** |
| FLY sec21 p.34 | [📄 FLY  p.34](https://agentii.ai/v/FLY/sec21/34) **(newly surfaced)** |
| FLY sec21 p.16 | [📄 FLY  p.16](https://agentii.ai/v/FLY/sec21/16) **(newly surfaced)** |
| FLY sec16 p.7 | [📄 FLY  p.7](https://agentii.ai/v/FLY/sec16/7) **(newly surfaced)** |
