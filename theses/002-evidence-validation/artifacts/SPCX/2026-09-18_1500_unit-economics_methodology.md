---
thesis_id: "002-evidence-validation"
pillar: PIL-1
ticker: SPCX
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-01"
    chosen_reading: "ALL BASES REPORTED — A, A-prime, B, C, plus two added filed readings (A-double-prime = Launch Services revenue only; and the realized-mass denominator variants D2/D3). No basis is adopted as 'the' answer; the pairing of numerator to denominator is stated for each."
  - da_id: "DA-02"
    chosen_reading: "LEO. The filed mass-to-orbit metric is ORBIT-AGNOSTIC ('deploy to orbit'), so substituting it into a LEO-denominated comparison introduces a stated DA-02 mismatch. Recorded as a limitation, not hidden."
  - da_id: "DA-06"
    chosen_reading: "price and cost reported separately, never conflated. The filed Launch Services / Launch & Development revenue split is what makes the separation possible."
  - da_id: "DA-07"
    chosen_reading: "the ISSUER's own definition, quoted verbatim at source: 'verified mass, including Starlink satellites, customer payloads, and development cargo, from all successful orbital and flight tests', excluding failed or scrubbed attempts. Not a capacity figure."
  - da_id: "DA-08"
    chosen_reading: "'customer launch' = an external payload is the PRIMARY payload and mission parameters are designed around it. The 8-K folds Starship into 'internal launches' while the 10-Q separates it; reconciled in section 2 rather than treated as a conflict."
  - da_id: "DA-23"
    chosen_reading: "component identity applied in-line (gross profit minus opex) for every operating figure read; EPS x shares NOT used, and the platform's calculation-arc instrument is additionally reported as unusable on this filing."
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "Mass to orbit 485 t (Q2 2026), of which customer payloads 87 t and internal payloads 397 t; Falcon launches 37, of which 10 customer and 27 internal; Starship launches 1; the issuer's verbatim definition of mass to orbit"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: search_keyword_in_source
  - figure: "Space revenue recognition basis: Launch Services point-in-time vs Launch and Development over-time cost-to-cost; Starlink subscribers 12.0M vs 6.0M and ARPU $66 vs $85; AI nameplate compute draw 1.4 GW vs 0.4 GW"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 36
    url: https://agentii.ai/v/SPCX/sec8/36
    located_via: search_keyword_in_source
  - figure: "Launch Services / Launch and Development revenue mix (67.4% / 32.6% Q2 2026); Space cost of revenue 'includes second stages flown related to the Company's Falcon 9 and Falcon Heavy launches'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 37
    url: https://agentii.ai/v/SPCX/sec8/37
    located_via: search_keyword_in_source
  - figure: "Consolidated results: revenue $7,814M, cost of revenue $3,495M, R&D $3,548M, SG&A $912M, restructuring $2M, loss from operations $(143)M (Q2 2026); $(2,086)M (H1 2026)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 40
    url: https://agentii.ai/v/SPCX/sec8/40
    located_via: read_source_pages
  - figure: "Space segment: revenue $962M, cost of revenue $329M, R&D $1,076M, SG&A $99M, total costs and expenses $1,504M, loss from operations $(542)M; customer launches 10 vs 9"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 42
    url: https://agentii.ai/v/SPCX/sec8/42
    located_via: search_keyword_in_source
  - figure: "Business highlights: 78 total launches YTD, mass to orbit 1,041 t (YTD), 1.4 GW nameplate compute draw"
    ticker: SPCX
    form_type: 8-K
    citation_id: sec7
    page_no: 5
    url: https://agentii.ai/v/SPCX/sec7/5
    located_via: read_source_outline
  - figure: "Segment financial highlights: Total income (loss) from operations $(143)M (Q2 2026); segment sum -542 + 1,656 + (1,257) = (143)"
    ticker: SPCX
    form_type: 8-K
    citation_id: sec7
    page_no: 6
    url: https://agentii.ai/v/SPCX/sec7/6
    located_via: read_source_outline
  - figure: "Space segment operating data BY PERIOD: customer launches 10/7/9/17/21, internal launches 28/33/37/61/63, total launches 38/40/46/78/84; customer payloads 87/45/88/132/163 t, internal payloads 397/511/563/908/938 t, mass to orbit 485/556/652/1,041/1,102 t; Launch services revenues $648/$330/$490/$978/$1,056M; Launch & development revenues $314/$289/$256/$603/$555M; Flight 12 'suborbital' with 'deployment of modified V2 Starlink satellites'; Flight 13 'deploying 20 production V3 satellites'; Starship 'expected to reduce the cost to orbit by 99% or more'"
    ticker: SPCX
    form_type: 8-K
    citation_id: sec7
    page_no: 7
    url: https://agentii.ai/v/SPCX/sec7/7
    located_via: read_source_outline
  - figure: "Starship has not reached operational orbit: 'Flight 13 demonstrated core capabilities necessary to achieve an orbital mission'; 'Flight 14 will be our first flight to fly our Version 3 Starlink satellites ... to operational orbit'; Falcon delivers 'roughly 2,500 tons a year to orbit'; Starship aspiration 'well over 1 million tons to orbit per year'"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 1
    url: https://agentii.ai/v/SPCX/ect1/1
    located_via: read_source_outline
  - figure: "'78 total launches and 1,041 tons of mass to orbit delivered in the first half of this year'; 'on the precipice of operationalizing Starship'; near-term goals 'of reaching orbit'"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 2
    url: https://agentii.ai/v/SPCX/ect1/2
    located_via: read_source_outline
---

# Phase 1 — Denominators: Falcon 9 and Starship (PIL-1)

**Purpose**: settle the divisor. PIL-1's four DA-01 bases all divide by **22.8 t**, a figure
001 recorded `CLAIMED` (published vehicle spec, in no filing), and F5a's propellant floor
divides by **100 t**, likewise unfiled. PIL-1's falsifier is a *per-kilogram* quantity, so it has
two inputs that can each move it — the price and the divisor. 001 examined the numerators
closely and held the divisor fixed at a single `CLAIMED` value across all four bases. **This
artifact settles the divisor; the numerators are inherited unchanged.**

**Headline result — and it is not the one this task expected.** A filed denominator **does**
exist, in the issuer's own SEC disclosure, exactly as PIL-1's `wrong_if` source clause allows.
Substituting it moves every demonstrated $/kg by **+79% to +162%** — **5.3× to 10.8× the ±15%
tolerance**. The test is **NOT MET**.

**But the failure strengthens PIL-1 rather than falsifying it.** The filed denominator is
*smaller* than the claimed one, so cost per kilogram goes **up**, not down. What breaks is not
the conclusion — launch is expensive — but 001's published *numbers*, which are 1.79× to 2.62×
too low on the realized basis, and its assertion that marginal cost sits *below* the $1,000/kg
threshold, which turns out to be denominator-dependent.

**Disposition summary**

| Denominator | Carries | Disposition | ±15% test |
|---|---|---|---|
| Falcon 9 **22.8 t** (capacity) | DA-01 A, A′, B, C | **`CLAIMED` stands.** No filed or manifest source states a Falcon 9 capacity. Recorded `UNRESOLVABLE-FROM-PUBLIC-SOURCES` **as a capacity**. | n/a — not substituted |
| Falcon 9 **realized 8.70 t / customer launch** (Q2 2026) | replacement for A′, C | **`DEMONSTRATED`** — filed, read-verified | **NOT MET** (+162%) |
| Falcon 9 **realized 12.76 t / launch, all launches** | replacement for A, B | **`DEMONSTRATED`** — filed, read-verified | **NOT MET** (+79%) |
| Starship **100 t** | **F5a** propellant floor | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — no filed source, and **no orbital payload delivery has been demonstrated** | **NOT MET** (denominator cannot be substituted at all) |

---

## 0. Inherited from 001 — cited, not recomputed

Per `spec.md` §0, the following are **taken as given**. Their inputs are used; their derivations
are not repeated.

| Inherited result | Source |
|---|---|
| The four-base spread A / A′ / B / C spans **~$525/kg to ~$6,596/kg** — a **7–13× spread around one Falcon 9 mission** | 001 `SPCX/2026-09-18_1239_unit-economics_methodology.md` §DA-01 |
| **F5a/F5b split**: propellant binds fully reusable vehicles only; Falcon 9's propellant is **~$0.36M of a $12–20M marginal cost (~2–3%)** and the **expended second stage at $8–12M dominates** | same, Finding 2; constitution §F5a/§F5b |
| **Basis B is `MODELED`** and therefore **cannot satisfy a falsifier** | same, §PIL-1 falsifier evaluation; constitution P4 |
| The `operating_income` **sign-convention trap** at SPCX (XBRL `+143M` against a filed `$(143)M`) | same, Data-quality note |
| **A1b falsified** — the axiom "launch is the master VALUE variable" does not hold; growth at SPCX comes from non-launch business | spec §0 row 5. **Evidence artifact, and therefore owner, is `SPCX/…_operational-kpi_methodology.md` — not this one.** A1b's mandatory qualification is carried in §7 below |

**What this artifact adds:** only the denominator. §0's rows are untouched.

---

## 1. Retrieval scope — what was admitted, and what the corpus can and cannot settle

**Admissibility rule (spec §1b, Q-1).** Only a **government manifest, a filed document, or a
customer contract** counts as adjudication. A company webpage or an issuer statement restates
the claim. An **issuer SEC disclosure is explicitly named as admissible** in PIL-1's own
`wrong_if` source clause (`government_launch_manifest_or_issuer_filing`) — which is the clause
this artifact is tested against.

**The SPCX corpus on the platform is 10 documents.** `list_sources(SPCX)` returns source types
`10_q`, `8_k`, `earnings_call_transcript` and nothing else:

| Source | `citation_id` | Date | Relevance to a payload denominator |
|---|---|---|---|
| 10-Q (accession `0001628280-26-052535`) | `sec8` | 2026-08-04 | **Primary.** Mass to orbit, launches, payload masses |
| 8-K — earnings release, Ex. 99.1 | `sec7` | 2026-08-04 | **Primary.** Per-period payload table, revenue split |
| Earnings call transcript | `ect1` | 2026-08-04 | Context only — issuer statement, **not** adjudication |
| 8-K — IPO completion | `sec1` | 2026-06-15 | No payload content |
| 6 further 8-Ks (notes offering, Cursor merger, board) | — | 2026-06/08 | No payload content |

**Two structural findings about the corpus, both material to the disposition:**

1. **There is exactly one 10-Q.** Every SPCX figure in the workspace traces to a single
   document — the concentration `spec.md` §1d already named. This artifact corroborates it from
   a second route: the earnings 8-K's per-period table is the *only* independent source for Q1
   and prior-year payload masses, and it is a press release exhibit, not an audited statement.
2. **The admissible class "government launch manifest" is `UNRESOLVABLE-FROM-PLATFORM`.** The
   platform carries SEC filings and issuer transcripts for SPCX and no manifest, range-safety,
   FCC/ITU or NASA source. That class cannot be searched here at all — a different limitation
   from "we searched and found nothing". **All substitution below therefore rests on the
   `issuer_filing` half of the source clause.**

**Negative search results, stated so they are not mistaken for absence of effort.** The
following keyword passes returned **no payload-capacity figure** anywhere in the corpus:

| Query | Source | Result |
|---|---|---|
| `mass to orbit` | `sec8` | 1 page (p.35) — **a mass figure, not a capacity figure** |
| `metric tons` | `sec8` | 1 page (p.35) |
| `payload` | `sec8` | 3 pages (p.34, 35, 36) — no capacity |
| `payload capacity` | `sec8` | 2 pages (p.35, 36) — **the string does not occur** |
| `capacity` | `sec8` | 11 pages — all compute capacity, credit facility, or launch-capacity allocation logic |
| `22.8` | `sec8`, `sec7` | **0 pages on both** |
| `100` | `sec7` | 2 pages (p.4, p.13) — cash balance and cash flow, not payload |
| `payload` / `Starship` | `sec1` (IPO 8-K), 2 further 8-Ks | **0 pages** |
| `payload` | `ect1` | 2 pages (p.3, p.5) — no capacity |
| `Falcon` | RKLB `sec109` (competitor cross-check) | **0 pages** |

> **So: the number 22.8 t does not appear in any filing on this platform, and neither does any
> other statement of Falcon 9 payload capacity.** The claim stands exactly where 001 left it.
> What the filings contain instead is something more useful — a **measured** mass.

---

## 2. What the filings actually disclose — the realized denominator

The issuer does not report a vehicle capacity. It reports **what it actually lifted.** Both
documents agree, on two different bases, and both were read at source.

### 2a — The 10-Q key-business-metrics definition ([📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35))

> *"Mass to Orbit: Mass to orbit is the total kilograms of payload that we deploy to orbit in a
> given period... We calculate this metric by summing **verified mass**, including Starlink
> satellites, customer payloads, and development cargo, from all successful orbital and flight
> tests. **This measure excludes failed or scrubbed attempts.**"*

This is **DA-07's definition verbatim** — a realized, verified, success-only mass. It is
**not** a capacity, and the distinction is the whole finding: a capacity is what the vehicle
*could* carry; this is what it *did* carry.

| Q2 2026 ([p.35](https://agentii.ai/v/SPCX/sec8/35)) | Value |
|---|---|
| Mass to orbit | **485 t** |
| — attributable to customer payloads | **87 t** |
| — attributable to internal payloads | **397 t** |
| Falcon launches | **37** (10 customer, 27 internal) |
| Starship launches | **1** ("to date, all Starship launches have been classified as internal") |

### 2b — The 8-K Space segment table gives the full per-period series ([📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7))

This is the document that makes the validation possible, and it is the one 001 did not use.
It is a **filed** exhibit (Ex. 99.1 to an Item 2.02 8-K), not a slide:

| | Q2 2026 | Q1 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---|---|---|---|---|
| Customer launches | 10 | 7 | 9 | 17 | 21 |
| Internal launches | 28 | 33 | 37 | 61 | 63 |
| **Total launches** | **38** | **40** | **46** | **78** | **84** |
| Customer payloads (t) | **87** | 45 | 88 | **132** | 163 |
| Internal payloads (t) | **397** | 511 | 563 | **908** | 938 |
| **Mass to orbit (t)** | **485** | **556** | **652** | **1,041** | **1,102** |
| Launch services revenues ($M) | **648** | 330 | 490 | **978** | 1,056 |
| Launch & development revenues ($M) | 314 | 289 | 256 | 603 | 555 |
| **Space revenues ($M)** | **962** | 619 | 746 | **1,581** | **1,611** |

Cross-checked against the 10-Q's own narrative at [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42)
(Space revenue $962M, cost of revenue $329M, R&D $1,076M, SG&A $99M) and the
[8-K p.5](https://agentii.ai/v/SPCX/sec7/5) headline ("78 total launches YTD, mass to orbit
1,041 t"). All three agree.

**Reconciliation checks run, all clean:**
- Segments sum to total: Launch services + Launch & development = Space revenue in all five periods ($648+$314 = $962 ✓).
- Payload components sum to mass to orbit within the filing's own rounding note ($87+$397 = 484 vs 485 ✓; the 10-Q states *"Amounts presented may not add up to the corresponding totals due to rounding"*).
- **The 10-Q / 8-K launch-count presentation trap.** The 10-Q reports *"Falcon launches 37, internal 27"* and, separately, *"Starship launches 1"*; the 8-K reports *"Internal launches 28"* with no vehicle split. These are the same fact: **27 Falcon internal + 1 Starship = 28**. Reconciles exactly in all four comparable periods (Q2 2025: 36+1 = 37 ✓; H1 2026: 60+1 = 61 ✓; H1 2025: 60+3 = 63 ✓). **An analyst diffing the two documents without this note finds a phantom one-launch discrepancy.** Registered for P3 as a DA-08-adjacent presentation hazard.

### 2c — The realized denominator, derived

| | Q2 2026 | Q1 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---|---|---|---|---|
| **t per customer launch** | **8.70** | 6.43 | 9.78 | **7.76** | 7.76 |
| **t per internal launch** | **14.18** | 15.48 | 15.22 | **14.89** | 14.89 |
| **t per launch (all)** | **12.76** | 13.90 | 14.17 | **13.35** | 13.12 |

> **Which launch count divides "all".** The row above uses the **Falcon + Starship** basis
> (Q2 2026: 38; H1: 78) because the filed 485 t includes Starship-contributed development cargo
> under DA-07's own definition. The **Falcon-only** basis (37 / 77 — the 10-Q's headline count)
> gives **13.11 t** and **13.52 t** instead, a **2.7%** difference. Both are defensible; the
> choice is stated because it is the exact seam the 10-Q/8-K trap in §2b runs along, and because
> the sibling artifact `SPCX/2026-09-18_1500_operational-kpi_methodology.md` uses the Falcon-only
> basis. **The two artifacts are consistent — they differ by a disclosed DA-08 population choice,
> not by arithmetic.** Every $/kg figure in §3 uses the **38 / 78** basis.

**Two readings of this table matter, and they point the same way:**

1. **The claimed 22.8 t is 2.6–2.9× the realized customer payload per customer launch** and
   1.6–1.8× the realized mass per launch on *any* reading, including the heaviest (internal
   Starlink batches at ~14.9 t, which are the fleet's fullest missions). **The claimed capacity
   is above every realized mission average the issuer reports.** That is expected — capacity is
   a ceiling — but it means 22.8 t was never a description of a typical Falcon 9 flight.
2. **Internal launches carry 1.6–2.3× the payload of customer launches, consistently.**
   That is DA-07 and DA-08 operating together and is the structural reason the four DA-01 bases
   disagree: A′ and C divide *customer* revenue by a denominator shaped by *Starlink* missions.

> **Observation, recorded not asserted.** The H1 2026 and H1 2025 per-launch averages are
> identical to two decimals on **both** the customer series (7.76 t) and the internal series
> (14.89 t) — five quarters apart, on different payload counts. That is an improbable
> coincidence and the filing does not explain it. The components do sum correctly in both
> periods, so this is **not** presented as a defect; it is flagged for a second look because two
> identical ratios would imply zero mix or mass change across a year in which customer launches
> fell 21→17 and the reported mix shifted materially.

---

## 3. The ±15% test — evaluated, and **NOT MET**

PIL-1's `wrong_if`: `metric=abs_pct_change_in_demonstrated_price_per_kg_to_LEO_after_denominator_validation`,
`threshold=0.15`, `op=>`.

### 3a — Denominator-only effect

Because each DA-01 numerator is already a **per-launch** quantity, the percentage change in
$/kg is set entirely by the denominator ratio `22.8 / t_new − 1`, and it is **identical across
all four bases**:

| Denominator reading | Basis | t | Change vs 22.8 t | $/kg multiplier | Verdict |
|---|---|---|---|---|---|
| Nameplate capacity (001's) | `CLAIMED` | 22.8 | — | 1.00× | (status quo) |
| Realized, internal launch | `DEMONSTRATED` | 14.18 | **−37.8%** | **1.61×** | **FAIL** |
| Realized, all launches | `DEMONSTRATED` | 12.76 | **−44.0%** | **1.79×** | **FAIL** |
| Realized, customer launch | `DEMONSTRATED` | 8.70 | **−61.8%** | **2.62×** | **FAIL** |

**The most conservative filed reading still moves $/kg by +61% — 4.05× the tolerance.** The
correctly population-matched readings move it +79% to +162%, i.e. **5.3× to 10.8× the
tolerance.** There is no filed denominator, on any of the three readings the issuer's own
disclosure supports, that lands inside ±15%.

**The band the spec asks for (§5: "Denominator sensitivity (P1) is reported as a band, not a
point").** Collapsing the three filed readings to the **defensible span** — the matched
customer-payload reading (8.70 t) at one end and the all-launches reading (12.76 t) at the
other, excluding the internal-launch reading as unmatched — gives a **±31.8% denominator band**
(8.70 / 12.76 = 0.682). **This band is multiplicative and identical for all four bases**, so it
composes with any numerator uncertainty rather than replacing it:

| Basis | Point (matched, 8.70 t) | Band | Range across the denominator span |
|---|---|---|---|
| A″ — Launch Services revenue | $7,448/kg | **±32%** | $5,078 – $7,448/kg |
| A′ — Space segment revenue | $11,057/kg | **±32%** | $7,539 – $11,057/kg |
| C — fully-loaded segment cost | $17,287/kg | **±32%** | $11,787 – $17,287/kg |
| B — marginal cost (`MODELED`) | $1,379–2,299/kg | **±32%** | $940 – $2,299/kg |

> **Note what the band does *not* cover.** It is the *denominator* band only. Basis B carries a
> second, independent uncertainty (the $12–20M marginal-cost model, inherited `MODELED`), and
> basis A carries the `CLAIMED` list-price uncertainty — both of which compose multiplicatively
> on top. **The ±32% is a floor on the total band, not the total.** Stated so no downstream thesis
> reads it as a complete error bar.

### 3b — Restatement of the four DA-01 bases (Q2 2026, all bases reported per §1c)

| Basis | Numerator (per customer launch) | vs **22.8 t** (`CLAIMED`) | vs **8.70 t** (customer payload) | vs **12.76 t** (all launches) | Grade of the restated figure |
|---|---|---|---|---|---|
| **A** — customer list price | ~$67M | ~$2,939/kg | ~$7,701/kg | ~$5,251/kg | `MODELED` (the `CLAIMED` price ÷ a filed mass) |
| **A″** — filed Launch Services revenue | **$64.8M** | ~$2,842/kg | **~$7,448/kg** | ~$5,078/kg | `DEMONSTRATED` inputs / `MODELED` division |
| **A′** — filed Space segment revenue | $96.2M | ~$4,220/kg | **~$11,057/kg** | ~$7,539/kg | `DEMONSTRATED` inputs / `MODELED` division |
| **B** — marginal cost (F5b) | ~$12–20M | ~$526–877/kg | **~$1,379–2,299/kg** | ~$940–1,567/kg | `MODELED` (unchanged) |
| **C** — fully-loaded segment cost | $150.4M | ~$6,596/kg | **~$17,287/kg** | ~$11,787/kg | `DEMONSTRATED` inputs / `MODELED` division |

*001's published B range ($525–875/kg) recomputes exactly to **$526–877/kg**; a $1–2 rounding
difference, noted for completeness rather than corrected in 001's frozen file (spec §1c
correction policy).*

**Pairing rule applied.** The denominator must come from the same population as the numerator.
A′ and C divide **customer-launch** revenue and **customer-launch** costs, so the matched
denominator is the **customer payload** reading (8.70 t). B is a per-launch marginal cost and
takes the reading matching the launch class in question. This is the `no_single_basis_collapse`
rule applied to the *denominator* as well as the basis — 001 varied the numerator across four
bases and held the denominator fixed at a single `CLAIMED` value, which is where the spread
became unresolvable.

### 3c — The consequence 001 did not anticipate: basis B crosses the threshold

001's PIL-1 evaluation states: *"On basis B the value sits **below** the $1,000 threshold."*
**That statement is a property of the denominator, not of the cost.**

| Denominator reading | Basis B ($/kg) | Position vs $1,000/kg |
|---|---|---|
| 22.8 t (001's) | $526–877 | wholly **below** |
| 12.76 t (all launches) | $940–1,567 | **straddles** |
| 8.70 t (customer launch) | $1,379–2,299 | wholly **above** |

Basis B remains `MODELED` and under P4 cannot satisfy a falsifier on any reading — so **PIL-1
still holds**. But the honest correction is: *prices are demonstrated above $1,000/kg on every
disclosed basis; marginal cost is modelled, and whether the model sits above or below $1,000/kg
depends entirely on the denominator.* 001's sharper claim — that the gap between a demonstrable
price and a non-demonstrable cost is the sector's key structural fact — survives and is
*sharpened*, because the modelled cost may already be above the threshold.

---

## 4. A filed correction to 001: the Launch Services split exists

001 states of basis A′: *"Restating it to launch services alone is **not possible from public
disclosure**"* — and grades A′ an **upper bound** on a launch price, not a price.

**That is falsified.** The 8-K separates the two revenue lines in every period
([📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7)), and the 10-Q gives the same split as a
percentage ([📄 SPCX 10-Q p.37](https://agentii.ai/v/SPCX/sec8/37), Launch Services 67.4% of
Space revenue in Q2 2026 — recomputes to 67.36% from $648M/$962M ✓).

**Sharper, and unflattering: the 10-Q alone refutes it.** 001's caveat sits on a page that
cites the 10-Q's own p.35 and p.42; the Launch Services percentage split is on p.37 of the same
document, at the same level of the segment note. The claim was not blocked by disclosure
granularity — it was a failure to sweep the note 001 was already reading. **Registered as a P3
retrieval-completeness finding**: the miss is a *within-document* omission, the failure mode a
citation-completeness gate is meant to catch and did not.

**Added basis A″ — filed Launch Services revenue ÷ customer launches:**

| | Q2 2026 | Q1 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---|---|---|---|---|
| Launch services revenue ($M) | 648 | 330 | 490 | 978 | 1,056 |
| Customer launches | 10 | 7 | 9 | 17 | 21 |
| **A″ — revenue per customer launch** | **$64.8M** | $47.1M | $54.4M | $57.5M | $50.3M |
| A″ per kg at 8.70 t | **$7,448** | $7,332 | $5,567 | $7,414 | $6,481 |

**Two results follow.**

1. **Basis A's $67M list price is corroborated to within 3.4%.** Against the filed realized
   Launch Services revenue per customer launch of **$64.8M**, a $67M list price implies a
   discount/mix premium of 3.4% — **inside ±15%**. The *numerator* half of PIL-1 validates
   cleanly. Only the denominator fails. That asymmetry is itself the finding: **the price is
   real; the divisor was assumed.**
2. **But the realized price is volatile — $47.1M to $64.8M across five quarters — so "$67M per
   launch" is not a stable descriptor of a Falcon 9 mission.** The Q2 figure is the high end,
   and the filing attributes it to *"a higher number of large customer launches and a favorable
   customer shift"* ([p.42](https://agentii.ai/v/SPCX/sec8/42)). A single-quarter price
   extrapolated across the fleet understates the mix sensitivity.

**A third, narrower result.** On the matched pair (Launch Services revenue ÷ customer payload
mass), the five periods cluster at **$5,567–7,448/kg** — a **1.34× band**. 001's four-base
spread is 7–13×. **The spread shrinks by an order of magnitude once the numerator and the
denominator are drawn from the same population.** The residual gap between A″ ($7,448/kg) and
A′ ($11,057/kg) is exactly the Launch & Development contamination 001 flagged as DA-21 in
operation — and it is now *quantified*: **$3,609/kg of the A′ figure is non-launch revenue.**

---

## 5. Starship's 100 t — the F5a denominator

**Disposition: `UNRESOLVABLE-FROM-PUBLIC-SOURCES`, and the test is NOT MET.**

F5a's output — the **$46–92/kg** propellant floor, which is the constitution's bound on the
entire orbital-compute narrative — is the quotient of two `MODELED`/`CLAIMED` inputs, and the
denominator has no filed source:

| F5a input | Source status |
|---|---|
| Propellant 4,600 t; $1–2/kg; $4.6–9.2M per flight | constitution §F5a, `MODELED` — **inherited, not re-derived here** |
| **Payload 100 t** | **`CLAIMED` — company figure, in no filing on this platform** |

**Three filed facts that bear on the denominator, all read at source:**

1. **Starship has never delivered payload to operational orbit.** The 8-K describes Flight 12 as
   *"Starship V3's **first suborbital mission**"* ([p.7](https://agentii.ai/v/SPCX/sec7/7)).
   Musk on the call: *"Flight 13 demonstrated core capabilities **necessary to achieve** an
   orbital mission... Flight 14 will be **our first flight to fly** our Version 3 Starlink
   satellites or communication satellites **to operational orbit**"*
   ([ect1 p.1](https://agentii.ai/v/SPCX/ect1/1)). Shotwell: *"on the **precipice of**
   operationalizing Starship"*, near-term goals *"of reaching orbit"*
   ([ect1 p.2](https://agentii.ai/v/SPCX/ect1/2)). **The 100 t denominator describes a
   capability the vehicle has not yet demonstrated.**
2. **The only filed Starship payload datapoint is a count, not a mass.** Flight 13 deployed
   *"20 production V3 satellites"* ([p.7](https://agentii.ai/v/SPCX/sec7/7)). No satellite mass
   is disclosed anywhere in the corpus, so the count **cannot be converted to tonnes on this
   platform** — recorded as a blocked conversion, not a failed search.
3. **The 10-Q itself declines to separate Starship's contribution.** *"To date, all Starship
   launches have been classified as internal"* ([p.35](https://agentii.ai/v/SPCX/sec8/35)), and
   the mass-to-orbit definition includes *"development cargo"* from *"successful orbital **and
   flight tests**"*. Whether suborbital Flight 12's deployed satellites sit inside the 485 t is
   **not disclosed**. Flagged as a definitional ambiguity in DA-07, handed to P3.

**Arithmetic bound on the 100 t, using `CLAIMED` inputs and clearly flagged as such.** Musk's
Starship aspiration of *"well over 1 million tons to orbit per year"*
([ect1 p.1](https://agentii.ai/v/SPCX/ect1/1)) requires, at 100 t per flight,
**≈10,000 flights per year ≈ 27 flights per day** (and "well over" makes that a floor). Either
the 100 t denominator or the aspiration is wrong by an order of magnitude; they cannot both be
right at any flight rate close to the *demonstrated* cadence — **78 launches in H1 2026 across
SPCX's entire fleet, Falcon and Starship together** ([p.5](https://agentii.ai/v/SPCX/sec7/5)),
i.e. ~0.43/day. **This is not adjudication** — both inputs are issuer
statements, inadmissible per Q-1 — but it tells a downstream thesis using the 100 t exactly
what it is assuming.

**Consequence for F5a.** The floor is **not falsified** — the propellant physics is sound and is
inherited. But F5a's *output* is `MODELED` for two independent reasons now instead of one: its
numerator is a constitution estimate, and its denominator is an unfiled company claim on a
vehicle with **zero demonstrated orbital payload**. A thesis that applies $46–92/kg to a
Starship cost curve is dividing a model by a claim.

---

## 6. Two further filed results, reported because they change adjacent figures

### 6a — The filing supplies a cost-to-orbit claim of its own

The 8-K states Starship *"is expected to reduce the cost to orbit by **99% or more** relative to
the historical average"* ([📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7)). Applying a 99%
reduction to the cost bases in §3b gives a target band of roughly **$56–74/kg** on the
matched-pair realized bases, **$111/kg** on A′ (customer-payload denominator), and **$173/kg**
on basis C — the spread is the basis spread, not a range in the claim.

Read against the constitution, that band **straddles F5a's $46–92/kg floor rather than
clearing it**: the low end sits inside the floor's band, the high end reaches 1.9× above it.
It **does** sit clear of the sub-$10/kg figure the constitution treats as a marketing figure —
`constitution.md` §F5a (`constitution_pin: 1.4.0`, not a platform source, so uncited by URL):
*"any claim of sub-$10/kg to LEO is below the propellant floor... Treat sub-$10/kg as a
marketing figure, not an input."* **So the issuer's own aspirational target is consistent with
F5a and inconsistent with the sub-$10/kg narrative**, which is the cross-check this row
contributes. Recorded as `CLAIMED` — forward-looking and unfiled — and **not** as a
replacement for F5a.

### 6b — A consolidated operating figure, with the component identity shown in-line (DA-23)

Per the contract's `data_integrity_register_applied` rule, `operating_income` is **never** read
as a bare number here. Derivation from [📄 SPCX 10-Q p.40](https://agentii.ai/v/SPCX/sec8/40):

| | Q2 2026 | H1 2026 |
|---|---|---|
| Revenue | $7,814M | $12,508M |
| − Cost of revenue | $3,495M | $5,883M |
| **= Gross profit** | **$4,319M** | **$6,625M** |
| − R&D / − SG&A / − restructuring / − impairment | $3,548 / $912 / $2 / — | $7,062 / $1,658 / $(9) / — |
| **= Opex** | **$4,462M** | **$8,711M** |
| **Gross profit − opex** | **$(143)M** | **$(2,086)M** |
| Filed "Loss from operations" | **$(143)M** ✓ | **$(2,086)M** ✓ |

**Independent second route** — the segment table ([8-K p.6](https://agentii.ai/v/SPCX/sec7/6)):
$(542) + $1,656 + $(1,257) = **$(143)M** ✓; H1: $(1,204) + $2,844 + $(3,726) = **$(2,086)M** ✓.
**Space segment** ([8-K p.7](https://agentii.ai/v/SPCX/sec7/7)):
$962 − $329 = $633 gross profit; − ($1,076 + $99) = $(542)M ✓.

**Two findings for P3, both confirmed here rather than inherited.**

1. **DA-23 re-confirmed at SPCX.** `search_xbrl_facts(SPCX, OperatingIncomeLoss)` returns
   **`+143,000,000`** (Q2 2026) and **`+2,086,000,000`** (H1 2026). The filed values are
   **$(143)M** and **$(2,086)M**. Signs stripped on both, exactly as 001 recorded.
2. **⚠️ The calculation-arc instrument fails on this filing.**
   `validate_calculation(0001628280-26-052535)` reports `OperatingIncomeLoss` as
   **computed $(4,578)M vs reported `+$143M` → `fail`**, against a filed truth of **$(143)M**.
   **All three values disagree.** Broadly, 18 of 29 arcs fail and 9 pass on this accession —
   several failures look dimensional, but the operating-income arc fails in a way that produces
   a number agreeing with neither the filing nor the XBRL extract. **P3's stated primary
   instrument is unusable on SPCX; the in-line component derivation above is the only reliable
   route for this issuer.** Escalated — this is a P3 delivery risk, not a P1 result.

---

## 7. Entity-boundary flags (P6 owns the classification — marked here only)

Per `spec.md` §1b P6, every SPCX series is marked before it is quoted. Reporting the marks
without re-deriving them:

| Series quoted in this artifact | Boundary status | May be used for migration / growth claims? |
|---|---|---|
| Space segment — revenue, cost of revenue, R&D, SG&A, loss from operations, launches, payloads, mass to orbit | **clean** | **Yes** — this is the series that survives the boundary, and it is the one that **fell** (−1.9% H1, [p.42](https://agentii.ai/v/SPCX/sec8/42)) |
| Consolidated revenue / cost of revenue / opex (§6b, DA-23 derivation only) | **contaminated** — xAI common-control merger 2026-02-02 recasts prior periods; X merger 2025-03-28; June 2026 IPO | **No.** Quoted **only** as the component identity for the sign test, **never** as a growth rate. The consolidated H1 +53.7% and Q2 +91.9% figures are **not** used anywhere in this artifact. |
| AI segment (any figure) | **contaminated** | **No.** Quoted below **once**, and only to *measure the contamination* — never as a growth rate, and the 1.4 GW nameplate (P4's) is not touched here. |

**The Space series is what PIL-1 rests on, and it is the boundary-clean one.** Every denominator
in §2 and §3 is a Space-segment quantity. **No restatement of a denominator in this artifact
crosses an entity boundary** — the payload masses, launch counts and Space revenue are organic
to the pre-merger operating business in every period shown.

**Why the mark matters, in one exhibit** ([📄 SPCX 8-K p.6](https://agentii.ai/v/SPCX/sec7/6)).
The contrast between a clean series and a contaminated one is stark enough that the classification
is not academic:

| H1 2026 vs H1 2025 | Space (**clean**) | Connectivity (**clean**) | AI (**contaminated — shown to size the contamination only**) |
|---|---|---|---|
| Revenue | $1,581M vs $1,611M = **−1.9%** | $7,548M vs $5,062M = **+49.1%** | $3,379M vs $1,465M = +130.6% |
| Loss from operations | $(1,204)M vs $(439)M | $2,844M vs $1,956M | $(3,726)M vs $(2,460)M |
| Capex | $2,226M | $2,699M | $23,551M |

**Two consequences.** (1) The **A1b falsification** — growth comes from non-launch business
(`spec.md` §0 row 5; the *evidence artifact* is `SPCX/…_operational-kpi_methodology.md`, not
this one) gains a **boundary-clean exhibit** here: the Space series *fell* 1.9% while Connectivity
grew 49.1%, and neither figure needs a boundary caveat. (2) **The Space:AI capex ratio is
1:10.6** ($2,226M vs $23,551M in H1 2026). The capital is overwhelmingly going to the segment
whose series cannot be compared across the boundary. Any thesis that reads SPCX's *consolidated*
growth as evidence about the space business is reading the AI segment's ramp — this row is the
exhibit.

> **⚠️ A1b's mandatory qualification, carried here because A1b is named above** (`constitution.md`
> §0: *"A1b never travels without its qualification"*). **Falcon launch economics are good; one
> rocket is being funded.** The Space segment carries a **65.8% gross margin** — the highest in
> the universe — with **cost of revenue flat ($330M → $329M) while revenue rose 29.0%**. The
> segment loss is **Starship development R&D at $1,076M in the quarter — 111.9% of segment
> revenue** — a reinvestment choice, not an operating failure. All three figures are read from
> [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42) and [📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7)
> and recompute exactly.
>
> **This qualification is load-bearing for *this* artifact, not an appendix.** §3b's basis C
> restates to **~$17,287/kg**, which is the highest number in it — and it is the figure most
> likely to be quoted as *"SpaceX loses money on every launch."* It does not: basis C is
> **Starship-subsidised**, and the same segment note that produces it produces the 65.8% gross
> margin. **Quoting C without A1b's qualification is `UNFRAMED_REFERENCE`.** Any citation of the
> §3b table must carry the basis *and* the segment-profitable-per-Falcon-launch correction.

---

## 8. What could not be verified

Stated as limitations, not as passing checks (spec §1b: an unresolvable is reported **not met**,
never passed by default).

| # | Unverified | Class | Why it matters |
|---|---|---|---|
| 1 | **Falcon 9 payload capacity** (22.8 t) | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` on this platform; the manifest class is `UNRESOLVABLE-FROM-PLATFORM` | No filed source states one. The figure is a ceiling, and this artifact substitutes a measured mass instead — which changes the basis, and the change is disclosed, not elided |
| 2 | **Starship payload capacity** (100 t) | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | F5a's divisor. No filing states it and no flight has demonstrated it |
| 3 | **Orbit mix of customer payloads** | DA-02 residual | The filed metric is orbit-agnostic ("deploy to orbit"); DA-01's basis is LEO. Cannot confirm the 87 t was delivered to LEO. **Flagged, not corrected** |
| 4 | **Starship's share of the 485 t** | definitional ambiguity in DA-07 | Suborbital Flight 12 deployed satellites; whether they count is undisclosed. Handed to P3 |
| 5 | **V3 satellite mass** | blocked conversion | "20 production V3 satellites" cannot become tonnes without it |
| 6 | **Internal vs external launch cost allocation** | cost-accounting ambiguity — **and one assertion withdrawn** | The Space segment's cost base mixes two recognitions: Launch Services recognized **point in time** and Launch & Development **over time, cost-to-cost** ([p.36](https://agentii.ai/v/SPCX/sec8/36)), against a cost of revenue that includes *"second stages flown related to the Company's Falcon 9 and Falcon Heavy launches"* ([p.37](https://agentii.ai/v/SPCX/sec8/37)). **A search for `capitaliz*` across the 10-Q returns only capitalized interest, capital expenditures and paid-in capital — nothing about capitalizing internal launch costs into satellites.** That mechanism is widely believed true of Starlink and is **not asserted here**: it appears in no filed text this artifact could locate, so it is recorded as an open question for P3, not as a finding. Either way the conclusion holds: a fully-loaded cost **per tonne of total mass to orbit** (C ÷ 485 t = **$3,101/kg**) is arithmetically available but **not clean**. Recorded so no downstream thesis adopts it as demonstrated |
| 7 | **The H1/H1 identical per-launch averages** (§2c) | observation | Flagged for a second look; components reconcile, so not asserted as a defect |
| 8 | **The $67M list price's own source** | `CLAIMED`, and 001's artifact is its only citation in this workspace | Corroborated to 3.4% by A″ but **not adjudicated** — the corroboration is one quarter, at the high end of a $47.1–64.8M range |
| 9 | **`skill_pin` true content hash** | platform gap | `dispatch.skill_version_hash()` is not reachable from the artifact context; recorded, not fabricated |

---

## 9. Ledger rows contributed (P5)

Schema per `spec.md` §6. Rows marked **NEW** are figures this artifact introduces; the rest are
001 figures whose grade or value moves.

| Figure | Source artifact | Original grade | Validated grade | Band | Citation | Pillar | Disposition |
|---|---|---|---|---|---|---|---|
| Falcon 9 payload **22.8 t** | 001 `unit-economics` | `CLAIMED` | **`CLAIMED` (unchanged)** | — | (no source exists) | PIL-1 | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — **as a capacity** |
| **NEW** — realized payload per customer launch | this artifact | — | **`DEMONSTRATED`** | 6.43–9.78 t; **8.70 t** Q2 2026 | [sec8 p.35](https://agentii.ai/v/SPCX/sec8/35), [sec7 p.7](https://agentii.ai/v/SPCX/sec7/7) | PIL-1 | **adopted as the denominator for A′/C** |
| **NEW** — realized payload per launch (all) | this artifact | — | **`DEMONSTRATED`** | 12.76–14.17 t; **12.76 t** Q2 2026 | [sec7 p.7](https://agentii.ai/v/SPCX/sec7/7) | PIL-1 | adopted for A/B |
| DA-01 **basis A** ~$2,939/kg | 001 | `CLAIMED` | `MODELED` | **$5,251–7,701/kg** realized | [sec8 p.35](https://agentii.ai/v/SPCX/sec8/35) | PIL-1 | **restated upward**; list price `CLAIMED`, corroborated 3.4% |
| DA-01 **basis A′** ~$4,220/kg | 001 | `DEMONSTRATED` figs / `MODELED` div | `MODELED` | **~$11,057/kg** | [sec8 p.35](https://agentii.ai/v/SPCX/sec8/35), [sec7 p.7](https://agentii.ai/v/SPCX/sec7/7) | PIL-1 | **restated +162%**; still an upper bound — but now a **quantified** one (+$3,609/kg above A″) |
| **NEW — basis A″** Launch Services rev./customer launch | this artifact | — | **`DEMONSTRATED`** | $47.1–64.8M; **$64.8M** Q2 2026 | [sec7 p.7](https://agentii.ai/v/SPCX/sec7/7) | PIL-1 | **001's "not possible from public disclosure" FALSIFIED** |
| DA-01 **basis B** ~$525–875/kg | 001 | `MODELED` | `MODELED` (unchanged) | **$1,379–2,299/kg** customer pairing | [sec8 p.35](https://agentii.ai/v/SPCX/sec8/35) | PIL-1 | **crosses $1,000/kg**; 001's "sits below the threshold" corrected |
| DA-01 **basis C** ~$6,596/kg | 001 | `DEMONSTRATED` figs / `MODELED` div | `MODELED` | **~$17,287/kg** | [sec8 p.42](https://agentii.ai/v/SPCX/sec8/42), [sec7 p.7](https://agentii.ai/v/SPCX/sec7/7) | PIL-1 | **restated +162%** |
| Starship payload **100 t** (F5a) | 001 / constitution §F5a | `CLAIMED` | **`CLAIMED` (unchanged)** | — | (no source exists) | PIL-1 | `UNRESOLVABLE-FROM-PUBLIC-SOURCES`; F5a output `MODELED` |
| **NEW** — Starship cost-to-orbit target "−99% or more" | this artifact | — | `CLAIMED` | implies **~$56/kg to ~$173/kg** across bases | [sec7 p.7](https://agentii.ai/v/SPCX/sec7/7) | PIL-1 | forward-looking; **straddles** F5a, consistent with it and inconsistent with sub-$10/kg |
| `operating_income` sign at SPCX | 001 `unit-economics` | defect noted | **`DEMONSTRATED` defect** | XBRL `+143M` vs filed **$(143)M** | [sec8 p.40](https://agentii.ai/v/SPCX/sec8/40) | PIL-3 | **DA-23 re-confirmed**; instrument failure escalated |
| **NEW** — 10-Q/8-K launch-count presentation trap | this artifact | — | **`DEMONSTRATED`** | 27 Falcon + 1 Starship = 28 internal | [sec8 p.35](https://agentii.ai/v/SPCX/sec8/35), [sec7 p.7](https://agentii.ai/v/SPCX/sec7/7) | PIL-3 | DA-08-adjacent hazard registered |

**P5 note, per the CHK004 clarification.** The realized-mass rows convert to `DEMONSTRATED`
(they are filed, read-verified, and Space-segment — therefore boundary-clean). The four DA-01
basis rows **do not** convert: their divisions are our own, so they land at `MODELED` even
though their inputs are now `DEMONSTRATED`. **The denominator validation raises evidentiary
quality and lowers the reported numbers at the same time** — exactly the direction CHK004
predicted P6/P3 success can push the conversion share.

---

## 10. Next actions (Phase 1 hand-off)

1. **`RKLB × unit-economics` and `FLY × unit-economics` must run the same test.** Electron's
   300 kg and Alpha's payload denominators have no filed substitute either, but the *question*
   "does the realized mass basis exist?" is issuer-dependent and must be asked per issuer. If
   RKLB discloses a launch count and a mass, basis B's $14,667/kg moves the same way.
2. **Every downstream thesis quoting a Falcon 9 $/kg must quote a band, per `spec.md` §5
   ("Downstream theses quote `$X ± Y%`, not `$X`")** — and the band this artifact supplies is
   the **denominator-choice band: ±31.8%, from 8.70 t (customer-payload, matched) to 12.76 t
   (all launches)**. The quotable form:
   `basis A′ = $11,057/kg ± 32%` (Launch & Development included);
   `basis A″ = $7,448/kg ± 32%` (Launch Services only — the narrower and better-matched basis).
   The 001 figures ($2,939 / $4,220 / $6,596) are **1.79×–2.62× low** on the realized basis and
   must not be cited unqualified; **their failure is a denominator failure, not a numerator one.**
3. **PIL-1's own wrong_if is NOT MET and must be recorded as such**, with the direction stated:
   the failure **strengthens** the conclusion and **invalidates the published numbers**.
4. **P3 must be told that `validate_calculation` fails on SPCX's only 10-Q.** The remedy P3
   applies universe-wide may not be executable on the anchor issuer.
5. **Standing recommendation to 003 and 005** (the inheritors): the sector cost curve and the
   launch pure-play comparison should be built on the **matched-pair** basis of §4, where the
   band is 1.34× instead of 7–13×. **The spread 001 reported is largely an artefact of pairing
   customer revenue with a vehicle-capacity divisor.**
6. **F5a should be restated as a two-input `MODELED` bound** in any downstream citation, with
   the 100 t denominator marked `CLAIMED` and the zero-orbital-delivery fact attached. Not a
   constitution amendment request — F5a's *physics* is untouched; only its evidentiary tier
   needs stating.

---

*Format exemplar: `theses/001-technology-baseline/artifacts/SPCX/2026-09-18_1239_unit-economics_methodology.md`.
Inherited per `spec.md` §0. 001's files are frozen; corrections recorded here and cross-cited (spec §1c).*
