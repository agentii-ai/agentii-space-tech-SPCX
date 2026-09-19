---
thesis_id: "002-evidence-validation"
pillar: PIL-1
ticker: SPCX
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-07"
    chosen_reading: "VERIFIED at source. Mass to orbit = 'verified mass ... from all successful orbital and flight tests', internal + customer combined, excluding failures and scrubs. The filed 485/652 t restatement is DEMONSTRATED and the −25.6% is exact."
  - da_id: "DA-08"
    chosen_reading: "VERIFIED at source. A customer launch requires an external payload as the PRIMARY payload; 'all Starship launches have been classified as internal'. THREE competing bases are reported side by side (Falcon-only 37; Falcon+Starship 38; customer-only 10) rather than collapsed — §1c."
  - da_id: "DA-11"
    chosen_reading: "VERIFIED at source and NARROWED. The metric is GPU count x GPU all-in draw — narrower than facility IT load, not equal to it. The disclosed 1.4 GW is GPU nameplate, explicitly excluding cooling, power distribution losses, lighting, security and facility overhead."
  - da_id: "DA-21"
    chosen_reading: "SPCX's three-segment frame is a MANAGEMENT-DRAWN segment boundary (001 §1c: 'segment boundaries are drawn by management and change over time'). Each series is classified separately for entity-boundary contamination rather than aggregated — see §4. NOTE: no registered DA covers common-control recasting; recorded in §7.5."
  - da_id: "DA-23"
    chosen_reading: "operating_income component identity run in-line at four levels (Space, Connectivity, AI, consolidated). All four close exactly on the face of the filing. The platform field IS stripped; the Space identity is verified at $(542)M by 962 − 329 − 1,076 − 99."
  - da_id: "DA-25"
    chosen_reading: "normalised per-unit metrics. Two per-unit figures are produced here (13.5 t realized per Falcon launch; $39.6M capex per MW of nameplate added) and BOTH are reported as bounded observations with their basis mismatches stated, neither recomputed as authoritative and neither substituted into a filed series."
  - da_id: "DA-28"
    chosen_reading: "SPCX's June 2026 IPO, May 2026 five-for-one split and preferred conversion invalidate share-count-based detectors; per-share items are quarantined from growth claims."
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
pue_proper_residual: "UNRESOLVABLE-FROM-PUBLIC-SOURCES"
citations:
  - figure: "Mass to orbit — DA-07 definition verbatim ('verified mass ... from all successful orbital and flight tests. This measure excludes failed or scrubbed attempts')"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "Mass to orbit 485 / 652 t (Q2) and 1,041 / 1,102 t (H1); customer payloads 87 / 88 and 132 / 163; internal payloads 397 / 563 and 908 / 938"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "DA-08 definition verbatim ('customer launch' = external payload is the PRIMARY payload) + 'To date, all Starship launches have been classified as internal'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "Falcon launches 37 / 45 (Q2) and 77 / 81 (H1); customer launches 10 / 9 and 17 / 21; internal launches 27 / 36 and 60 / 60; Starship 1 / 1 and 1 / 3"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "Starlink subscribers 12.0M / 6.0M; Starlink ARPU $66 / $85 per month"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "DA-11 definition verbatim (GPUs installed x all-in power draw; 'does not include power we install and use for our supporting infrastructure such as cooling systems, power distribution losses, lighting, security systems, or facility-level overhead') + 1.4 GW / 0.4 GW"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 36
    url: https://agentii.ai/v/SPCX/sec8/36
    located_via: read_source_pages
  - figure: "Note 18 segment loss from operations Q2 2026: Space (542) / Connectivity 1,656 / AI (1,257) / consolidated (143); segment capex 1,174 / 1,367 / 15,828 / 18,369; D&A 2,848; SBC 831"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 30
    url: https://agentii.ai/v/SPCX/sec8/30
    located_via: read_source_pages
  - figure: "Note 18 Q2 2025 comparatives (Space (369) / Connectivity 923 / AI (1,524) / consolidated (970)) — the RECAST comparator, disclosed for a period 7 months BEFORE the xAI merger; plus H1 2026 (1,204) / 2,844 / (3,726) / (2,086)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 31
    url: https://agentii.ai/v/SPCX/sec8/31
    located_via: read_source_pages
  - figure: "Note 18 H1 2025 segment loss from operations (439) / 1,956 / (2,460) / (943) — the recast AI comparative of $1,465M revenue and $(2,460)M loss"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 32
    url: https://agentii.ai/v/SPCX/sec8/32
    located_via: read_source_pages
  - figure: "IPO 638.9M Class A shares at $135.00, net proceeds $85,675M; three reportable segments; Cursor Merger expected to close Q3 2026"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 34
    url: https://agentii.ai/v/SPCX/sec8/34
    located_via: read_source_pages
  - figure: "Space segment table — revenue $962M, cost of revenue $329M, R&D $1,076M, SG&A $99M, total $1,504M, loss from operations $(542)M (the DA-23 identity)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 42
    url: https://agentii.ai/v/SPCX/sec8/42
    located_via: read_source_pages
  - figure: "Connectivity segment — revenue $4,291M (+65.8%), income from operations $1,656M (+79.4%), and the ARPU attribution"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 43
    url: https://agentii.ai/v/SPCX/sec8/43
    located_via: read_source_pages
  - figure: "AI segment — revenue $2,561M, cost of revenue $1,106M, R&D $2,178M, SG&A $532M, restructuring $2M, total $3,818M, loss from operations $(1,257)M"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 44
    url: https://agentii.ai/v/SPCX/sec8/44
    located_via: read_source_pages
  - figure: "'AI loss from operations for the three months ended June 30, 2026 decreased by $267 million, or 17.5%' — the AI loss in narrative prose"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 45
    url: https://agentii.ai/v/SPCX/sec8/45
    located_via: read_source_pages
  - figure: "Non-GAAP Segment Adjusted EBITDA reconciliation repeating (542) / 1,656 / (1,257) / (143) — the fourth venue the AI operating loss is disclosed"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 46
    url: https://agentii.ai/v/SPCX/sec8/46
    located_via: read_source_pages
  - figure: "Consolidated Q2 2026 revenue $7,814M (+91.9%), loss from operations $(143)M, net loss $(541)M; H1 2026 revenue $12,508M, loss from operations $(2,086)M, net loss $(4,817)M"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 5
    url: https://agentii.ai/v/SPCX/sec8/5
    located_via: read_source_pages
  - figure: "Note 1 Common Control Mergers — xAI Merger Date 2026-02-02; X Merger 2025-03-28; 'The Mergers were each effected through a share exchange'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 11
    url: https://agentii.ai/v/SPCX/sec8/11
    located_via: read_source_pages
  - figure: "Equity statement — IPO net proceeds $85,675M; xAI Merger preferred conversion $37,475M; xAI Merger repurchase $(2,413)M"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 7
    url: https://agentii.ai/v/SPCX/sec8/7
    located_via: read_source_pages
  - figure: "H1 2026 cash flow — operating +$3,466M, investing $(34,487)M, financing +$100,291M; capex increase $21,511M attributed to data centers and launch facilities"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 50
    url: https://agentii.ai/v/SPCX/sec8/50
    located_via: read_source_pages
  - figure: "Musk on the compute trajectory — 'over 2 gigawatts of compute' by year-end 2026, 'closer to 10 gigawatts of compute than 5' by end-2027; the Starmind AI satellite (optimized Vera Rubin NVL72) to 'start launching ... next year'; 'roughly 2,500 tons a year to orbit via Falcon'"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 1
    url: https://agentii.ai/v/SPCX/ect1/1
    located_via: read_source_pages
  - figure: "Shotwell — '78 total launches and 1,041 tons of mass to orbit delivered in the first half of this year, primarily allocated to our own internal Starlink missions'; +1.7M net Starlink adds; ARPU $66; ~10,200 satellites (9,600 broadband)"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 2
    url: https://agentii.ai/v/SPCX/ect1/2
    located_via: read_source_pages
  - figure: "Johnsen — 'We ended the second quarter with 1.4 gigawatts of nameplate compute, up from 1 gigawatt in Q1 and 400 megawatts a year earlier. We expect to end this year at over 2 gigawatts'; Q2 capex ~$18.4B of which ~$15.8B AI; 'narrowed our AI segment net operating loss to $1.3 billion'"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 3
    url: https://agentii.ai/v/SPCX/ect1/3
    located_via: read_source_pages
  - figure: "Musk — facility-side power DISCLOSED against nameplate: 'our tentative target is to actually have 20 gigawatts at the power and cooling level online by the end of next year ... I would expect that we still probably have at the power plant level, something close to 15 gigawatts ... our goal is to have far more power, cooling and electrical equipment than we have GPUs' — the PIL-4 restatement input"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 4
    url: https://agentii.ai/v/SPCX/ect1/4
    located_via: read_source_pages
---

# SPCX — Operational KPI Methodology (Q2 2026, post-IPO)

**Phase 1 · `SPCX × operational-kpi` · primary PIL-1, carrying PIL-4 and PIL-6.**

Source: Form 10-Q, accession `0001628280-26-052535`, filed 2026-08-04, quarter ended
2026-06-30 (**`sec8` — the only SPCX 10-Q on the platform**, 55 pages), plus the Q2 2026
earnings call transcript (`ect1`, 2026-08-04, 6 pages).

**This artifact does three things and overturns one inherited position.** It verifies the
DA-07/DA-08 restatement at source; it *resolves* PIL-4 from issuer disclosure the spec
records as non-existent; and it classifies the SPCX series for entity-boundary
contamination. The overturn is in §7.

---

## 0. What was settled, in one table

| # | Question | Answer | Grade |
|---|---|---|---|
| 1 | DA-07 / DA-08 restatement | **VERIFIED — every figure matches the filing exactly.** 485 vs 652 t (−25.6%), 37 vs 45 Falcon (−17.8%), 27 vs 36 internal (−25.0%), Starship 3→1, 10 of 37 customer, customer payload 87 vs 88 t | DEMONSTRATED |
| 2 | PIL-4 nameplate restatement | **1.5× expected / 2.0× tentative target** on the issuer's own disclosed facility-side power → **2.1 GW (central) to 2.8 GW (target)** against the filed 1.4 GW. Full band **1.2–2.0×** | MODELED *(on a CLAIMED forward input)* |
| 3 | PIL-4 falsifier | **FIRES on one of the two disclosed readings** (2.0 > 1.5), sits *exactly at* the threshold on the other (1.5). PIL-4's own claim — "lands within 1.2–1.5×" — **fails at the issuer's tentative target** | — |
| 4 | PIL-6 boundary | **Space clean · Connectivity clean · AI contaminated · consolidated contaminated**, and **the 1.4 GW series itself is contaminated** — it is xAI's fleet | DEMONSTRATED |
| 5 | Inherited "AI operating line is DERIVED, never as filed" | **WRONG.** The AI loss from operations is **filed four separate times** with the component identity closing exactly. §7 | DEMONSTRATED |

---

## 1. DA-07 / DA-08 — the restatement VERIFIED at source

### 1.1 The definitions, verbatim from the filing

**DA-07 — Mass to Orbit** (filed definition, [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35)):

> *"Mass to orbit is the total kilograms of payload that we deploy to orbit in a given
> period… We calculate this metric by summing **verified mass**, including Starlink
> satellites, customer payloads, and development cargo, from **all successful orbital and
> flight tests**. This measure **excludes failed or scrubbed attempts**."*

**DA-08 — a "customer launch"** (filed definition, same page):

> *"We designate a launch as a 'customer launch' if an external customer payload
> constitutes the **primary payload** (i.e., where the principal objective is to deliver
> the customer payload) and the mission parameters (e.g., launch window, orbital
> parameters, mission profile) are designed around the primary payload's requirements.
> **To date, all Starship launches have been classified as internal.**"*

**Both definitions are verified as written in 001 `spec.md` §1c. Neither is a paraphrase.**
The parenthetical `(i.e., …)` and the Starship carve-out are the filing's own words, and
the Starship carve-out is load-bearing: it is why the 1 Starship launch in H1 2026 does
**not** appear in the customer column.

### 1.2 The restatement, read-verified

**Mass to orbit** — [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35):

| Mass to orbit (t) | Q2 2026 | Q2 2025 | Change | H1 2026 | H1 2025 | Change |
|---|---:|---:|---:|---:|---:|---:|
| **Total** | **485** | 652 | **−25.6%** | **1,041** | 1,102 | **−5.5%** |
| — customer payloads | 87 | 88 | **−1.1%** | 132 | 163 | −19.0% |
| — internal payloads | 397 | 563 | −29.5% | 908 | 938 | −3.2% |

**Launches** — same page:

| Launches | Q2 2026 | Q2 2025 | Change | H1 2026 | H1 2025 | Change |
|---|---:|---:|---:|---:|---:|---:|
| **Falcon** | **37** | 45 | **−17.8%** | **77** | 81 | **−4.9%** |
| — customer | **10** | 9 | +11.1% | 17 | 21 | −19.0% |
| — internal | **27** | 36 | **−25.0%** | 60 | 60 | 0.0% |
| **Starship** | **1** | 1 | — | **1** | 3 | **−66.7%** |

**Every figure in the inherited brief is confirmed: 485 vs 652 (−25.6%); 37 vs 45
(−17.8%); 27 vs 36 (−25.0%); Starship 3 → 1 across H1; 10 of 37 count as customer
launches; customer payload flat at 87 vs 88 t.** The task's "−25.0% internal" figure is
the **launch** count (27/36), not the payload mass (397/563 = −29.5%) — two different
internal-contraction numbers, both filed, and both are quoted above so neither is read
as the other.

### 1.3 Three findings beyond the brief

**(a) The launch components sum EXACTLY; the mass components do NOT.**
10 + 27 = 37 ✓ · 9 + 36 = 45 ✓ · 17 + 60 = 77 ✓ · 21 + 60 = 81 ✓ — every launch quarter
closes with zero residual. But 87 + 397 = 484 against a stated 485, and 132 + 908 = 1,040
against a stated 1,041. **This is not a defect and must not be registered as one**: the
table carries an explicit footnote — *"Amounts presented may not add up to the
corresponding totals due to rounding"* — and the wedge is ±1 t, i.e. **0.2% of the Q2
total and immaterial to the −25.6%.** Registered here as a *disclosed* rounding basis, so
that a later artifact running a component-identity check on p.35 does not report a false
DA-23-class finding. ([📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35))

**(b) The 25.6% decline is a decline in SPCX's OWN payload, not in customer demand.**
Internal payload mass fell 29.5% while customer payload mass fell 1.1% — **customer
payload is essentially flat.** The DA-07 metric is an *aggregate* of two businesses with
opposite trends, and the contraction is entirely the internal (Starlink deployment) leg.
This is the number that decides whether the decline is a demand signal or a deployment
schedule, and the filing answers it on its own metric.

**(c) Musk's verbal mass figure is ~20% above the filed run-rate.** On the call he states
they *"deliver, call it, roughly **2,500 tons a year** to orbit via Falcon"*
([📄 SPCX Q2 2026 call p.1](https://agentii.ai/v/SPCX/ect1/1)). The filed H1 2026 figure
annualises to **2,082 t** (1,041 × 2) — and 2025's H1 annualised to 2,204 t, so 2026 is
running *below* 2025. **2,500 t is ~20% above the current filed run-rate and ~13% above
2025's.** Register as `CLAIMED`, and do not let a spoken round number replace a filed one.

---

## 2. DA-08's basis spread — three "launch" numbers for one quarter

**The same quarter carries three different, simultaneously-true launch counts, and the
filing and the call each quote a different one.**

| Basis | Q2 2026 | H1 2026 | Where it is quoted |
|---|---:|---:|---|
| **Falcon only** | **37** | **77** | the 10-Q key-metrics table, "Falcon launches" |
| **Falcon + Starship** | **38** | **78** | **the earnings call** — Shotwell: *"**78 total launches** and 1,041 tons of mass to orbit delivered in the first half of this year"* |
| **Customer only** | **10** | **17** | the 10-Q, the DA-08 basis |

The 77 / 1 vs 78 is **not a discrepancy** — it is the Falcon-only basis against the
all-vehicles basis (77 + 1 Starship = 78). **But it is the exact DA-08 hazard in the
wild.** A reader taking "78 launches" from the call and pairing it with the filing's 10
customer launches gets a customer share of **12.8%** — a number that appears in neither
document and is an artefact of mixing the two bases:

| Customer share of launches | Denominator | Q2 2026 | H1 2026 |
|---|---:|---:|---:|
| **Falcon-only** (the filed basis) | 37 / 77 | **27.0%** | **22.1%** |
| **All vehicles** (the call basis) | 38 / 78 | 26.3% | 21.8% |
| **Mixed bases — the artefact** | 10 ÷ 78 | **12.8%** | 21.8% |

**Per §1c this artifact reports all three bases and collapses to none.** The DA-08
reading is that **the customer-launch basis is the only one that excludes internal
payloads**, so it is the only basis admissible for a demand comparison — and it is the
one where Q2 *rose* (+11.1%) while the headline count *fell* (−17.8%). **The headline and
the demand signal point in opposite directions, and the definition is what separates
them.**

Sources: [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35) ·
[📄 SPCX Q2 2026 call p.2](https://agentii.ai/v/SPCX/ect1/2)

---

## 3. PIL-4 — the DA-11 restatement, and the falsifier's outcome

### 3.1 The exclusion, verbatim

**DA-11 — Nameplate Compute Draw** ([📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36)):

> *"We calculate nameplate compute draw for a period as the **number of GPUs installed in
> our data centers** at the end of the period multiplied by their respective **all-in power
> draw**. Nameplate compute draw reflects **installed capacity and does not represent
> actual power consumption or utilization**. It **does not include power we install and use
> for our supporting infrastructure such as cooling systems, power distribution losses,
> lighting, security systems, or facility-level overhead**."*

**The exclusion is exactly as DA-11 registers it, and the filed figures are 1.4 GW as of
2026-06-30 against 0.4 GW as of 2025-06-30.**

**⚠️ One correction to the inherited framing, and it changes which denominator the band
applies to.** 001's artifact calls the 1.4 GW *"IT load only."* **The filing does not say
that, and the metric it defines is narrower than IT load.** It is *GPU count × GPU all-in
draw* — so beyond cooling and distribution it also excludes the **host CPUs, DRAM,
NICs, storage, PSU conversion losses and the network fabric** that sit inside the
facility's IT load but outside the GPU nameplate. **DA-11's quantity is GPU nameplate
⊂ IT load ⊂ facility draw.** Any restatement that treats the 1.4 GW as IT load
**understates** the gap, and any PUE computed against it **overstates** the PUE. That
distinction is what §3.3 turns on.

### 3.2 The restatement — from an ISSUER-DISCLOSED facility-side figure

**The input the spec records as non-existent is disclosed on the Q2 2026 earnings call.**
Musk, asked about compute capacity, restates the same trajectory on a facility-side basis
([📄 SPCX Q2 2026 call p.4](https://agentii.ai/v/SPCX/ect1/4)):

> *"So we're actually aiming to far exceed that gigawatt number in terms of **power online,
> power cooling and electrical equipment**. So our tentative target is to actually have
> **20 gigawatts at the power and cooling level online by the end of next year** … but I
> would expect that we still probably have **at the power plant level, something close to
> 15 gigawatts** … So **our goal is to have far more power, cooling and electrical
> equipment than we have GPUs**."*

The **same speaker, in the same answer, on the same basis**, puts compute at *"closer to
10 gigawatts of compute than 5"* by end-2027 ([📄 SPCX Q2 2026 call p.1](https://agentii.ai/v/SPCX/ect1/1)).
**That gives a same-basis, same-utterance multiple:**

```
facility-side / compute     expected case   15 GW power-plant-level / 10 GW compute  =  1.50x
                            tentative target 20 GW power-and-cooling  / 10 GW compute  =  2.00x
```

**Applying it to the filed 1.4 GW nameplate:**

| Basis | Multiple | Restated facility-side draw |
|---|---:|---:|
| Delivered 1.4 GW nameplate, no adjustment | 1.00× | 1.4 GW |
| Issuer-disclosed **expected** facility-side | **1.50×** | **2.1 GW** |
| Issuer-disclosed **tentative target** facility-side | **2.00×** | **2.8 GW** |

> ### **The restated nameplate ratio: 1.5× (central) · 1.2–2.0× (full band).**
> **Restated facility draw: 2.1 GW central, 2.8 GW at the issuer's own target — against
> 1.4 GW as filed.**

**Cross-check on the numerator, from a second disclosed input.** SPCX added 0.4 GW of
nameplate in Q2 (1.4 GW at 2026-06-30 against **1.0 GW at 2026-03-31**), and spent
**$15,828M** of AI-segment capex in the quarter
([📄 SPCX Q2 2026 call p.3](https://agentii.ai/v/SPCX/ect1/3) ·
[📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30)). That is **$39.6M per MW of
nameplate added**, or **$26.4M per MW of facility-side power** at the 1.5× restatement —
inside the range reported for hyperscale AI build. **The disclosed capex and the disclosed
facility-side multiple are mutually consistent**, which is the strongest statement
available without a filed PUE. *(MODELED; the Q1 ⇒ 1.0 GW datapoint is transcript-only
and the filing carries only the 0.4 and 1.4 endpoints.)*

**And the forward guidance is on-trend, not heroic**: *"We expect to end this year at
over 2 gigawatts of compute capacity"* — from 1.4 GW that is ≥+43% over two quarters,
against the **+40% just delivered in a single quarter**. On the restated basis, end-2026
guidance implies **≥3.0 GW of facility-side power**.

### 3.3 Two readings, both reported — §1c `no_single_basis_collapse`

**PIL-4's falsifier is `metric=spcx_facility_pue_ratio threshold=1.5
source=issuer_disclosure_or_industry_PUE_benchmark op=>`. Two different quantities can be
put in that numerator, and the falsifier's outcome FLIPS between them.** Both are reported;
neither is collapsed.

| | **Reading A — DA-11 basis** (facility-side power ÷ the filed 1.4 GW) | **Reading B — PUE proper** (facility draw ÷ full IT load) |
|---|---|---|
| Value | **1.50× expected · 2.00× target** | **Bounded, not sourced** |
| Inputs | issuer-disclosed (call p.4) + issuer-filed (10-Q p.36) | **none** |
| Threshold | **2.00 > 1.5 → FIRES** on the target; **1.50 = 1.5 → does not fire** on the expected case | straddles 1.5 |
| Why | both halves of the ratio are named by the same speaker on the same basis | the filing defines the metric as **GPU nameplate, not IT load**, so the PUE denominator is not the 1.4 GW |

**Reading B cannot be computed, and I am bounding it rather than sourcing it, as
required.** Three facts establish the bound: (i) **`PUE` returns zero hits in the 10-Q**
and *"power usage effectiveness"* returns zero — **SPCX does not disclose a PUE**;
(ii) **no industry PUE benchmark is carried on the platform** — VRT's 10-Q returns zero
PUE hits and no workspace artifact carries a sourced PUE value; (iii) since
GPU nameplate ⊂ IT load, `PUE_proper ≤ facility-side ÷ nameplate`, i.e. **strictly below
Reading A's multiple.** Under the conventional non-GPU IT-load share of 10–20%, Reading B
lands at **≈1.3–1.7×** — which **straddles the 1.5 threshold and cannot be resolved
without a disclosure that does not exist.**

**So the honest answer to PIL-4's "restate it PUE-inclusive and report the ratio" is:**
**the ratio is reportable on the DA-11 basis (1.5–2.0×) and only boundable on the PUE
basis (≈1.3–1.7×, ±the IT-load assumption).** The residual is recorded in frontmatter as
`pue_proper_residual: UNRESOLVABLE-FROM-PUBLIC-SOURCES`.

### 3.4 Falsifier outcome — and the spec's disposition is contradicted

`spec.md` §PIL-7 records **PIL-4 as `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — "the clearest
case in the workspace"** — and asserts flatly that *"PIL-4's data does not exist
publicly."* **That is contradicted by the issuer's own Q2 2026 earnings call.** The input
exists, is public, is issuer-sourced, and **is exactly the class of input the falsifier's
`source=` clause names** (`issuer_disclosure`). PIL-4 was mis-dispositioned because the
search stayed inside the 10-Q and the transcript was never read.

Consequences to hand off:

1. **PIL-4 → evaluable, partially.** The DA-11 reading is computable from disclosure and
   the falsifier fires at the target (2.00 > 1.5) and is indistinguishable from the
   threshold at the expected case (1.50). **PIL-4 is no longer `UNRESOLVABLE`, and it is
   no longer PENDING.**
2. **PIL-4's stated claim is falsified.** *"The ratio of true facility draw to stated
   load lands within 1.2–1.5×"* — **the floor holds; the ceiling does not, on the
   issuer's own tentative target (2.0×).** The 1.2–1.5× band is a *reference* range for
   PUE-proper, and it was applied to a quantity that is not IT load.
3. **PIL-7 inherits a second-classified falsifier** and should record PIL-4's disposition
   as moved from `UNRESOLVABLE-FROM-PUBLIC-SOURCES` to **evaluable**, with a named
   residual (PUE-proper) that remains source-blocked.

### 3.5 The MSFT comparison, restated

`spec.md` §PIL-4 sets **1.4 GW of SPCX ground-based AI compute against MSFT's ~2.9–11.6 GW
of annual new-build capacity**, and closes with: *"Even at the top of the range, MSFT's
annual build dwarfs SPCX's cumulative base."*

| Pairing | SPCX | MSFT | Ratio |
|---|---:|---:|---:|
| Filed vs MSFT floor | 1.4 GW | 2.9 GW/yr | 0.48× |
| **Restated target vs MSFT floor** | **2.8 GW** | **2.9 GW/yr** | **0.97×** |
| Restated target vs MSFT top | 2.8 GW | 11.6 GW/yr | 0.24× |

**The sign survives; the word "dwarfs" does not.** At the most favourable pairing, SPCX's
**entire cumulative facility-side base is ~0.97× MSFT's annual build** — a ratio of
roughly one, not a dwarfing. **The directional conclusion PIL-4 depends on holds**
(SPCX's cumulative base does not exceed even the floor of a single peer's annual build),
**but it holds by 3%, not by an order of magnitude, and only once the restatement is
applied.** Two basis caveats stay attached: MSFT's figure is **capex-derived capacity
addition** while SPCX's is **nameplate power**, and the two are still not the same
quantity — the restatement narrows the gap PIL-4 names, it does not close it.

---

## 4. PIL-6 — entity-boundary classification, per figure

**Boundary events inside the comparison window** ([📄 SPCX 10-Q p.11](https://agentii.ai/v/SPCX/sec8/11)):

| Event | Date | Accounting effect |
|---|---|---|
| **X Merger** — X Holdings into xAI | **2025-03-28** | inside the H1 2025 comparative window |
| **xAI Merger** — X.AI Holdings into SPCX | **2026-02-02** | **common control → prior periods RECAST**; "effected through a share exchange" |
| Five-for-one forward split | 2026-05 | per-share items retroactively adjusted |
| **IPO** — 638.9M Class A at $135.00, net $85,675M | 2026-06 | capital-structure discontinuity (DA-28) |
| **Cursor Merger** — Anysphere, ~$60B implied, all-stock | pending, Q3 2026 | **not yet in any figure** |

**The recasting is directly visible, and this is the proof.** The filing discloses an AI
segment for **Q2 2025** (revenue **$737M**, loss from operations **$(1,524)M**) and for
**H1 2025** (**$1,465M** revenue, **$(2,460)M** loss) — periods that **predate the
2026-02-02 xAI merger by seven months and eleven months respectively.** An AI segment
cannot appear in a comparative for a period before the entity existed unless the
comparative was **recast**. And the H1 2025 compare does not stop there: **the X merger
(2025-03-28) falls *inside* H1 2025**, so the 2025 AI column blends pre- and post-X xAI.
Sources: [📄 SPCX 10-Q p.31](https://agentii.ai/v/SPCX/sec8/31) ·
[📄 SPCX 10-Q p.32](https://agentii.ai/v/SPCX/sec8/32)

**The segment sums close exactly, so segment revenue is directly readable** — 962 + 4,291
+ 2,561 = **7,814** ✓ · 1,611 + 5,062 + 1,465 = **8,138** ✓ · 1,581 + 7,548 + 3,379 =
**12,508** ✓ · 746 + 2,588 + 737 = **4,071** ✓. **Recasting does not break the arithmetic;
it breaks comparability.** Every figure below is arithmetically sound and still
boundary-contaminated where marked.

### The classification table

| SPCX figure | Boundary status | Basis for the call |
|---|---|---|
| Mass to orbit — 485 / 652 / 1,041 / 1,102 t | **CLEAN** | payload mass to orbit; mergers cannot add tonnage to a Falcon fairing |
| Customer payload 87 / 88 t · internal 397 / 563 t | **CLEAN** | same |
| Falcon launches 37 / 45 · 77 / 81 | **CLEAN** | launch operations are SPCX-native |
| Starship launches 1 / 1 · 1 / 3 | **CLEAN** | same |
| Customer launches 10 / 9 · 17 / 21 | **CLEAN** | same |
| Starlink subscribers 12.0M / 6.0M; ARPU $66 / $85 | **CLEAN** | Starlink was never merged; wholly organic |
| **Space revenue $962M / $1,581M (H1 −1.9% vs $1,611M)** | **CLEAN** | the one growth series that survives the boundary — **and it fell** |
| Space cost of revenue, R&D, SG&A, loss from ops | **CLEAN** | same segment, same basis both periods |
| Connectivity revenue $4,291M · op income $1,656M | **CLEAN** | never merged |
| Connectivity ARPU attribution | **CLEAN** | same |
| **AI revenue $2,561M (+247.5%) · $3,379M H1** | **CONTAMINATED** | xAI, common control 2026-02-02; comparatives recast |
| **AI loss from operations $(1,257)M · $(3,726)M H1** | **CONTAMINATED** | same |
| **"AI is 32.8% of SPCX revenue"** | **CONTAMINATED — DO NOT QUOTE** | recast segment; the spec's named case |
| **Nameplate compute draw 1.4 GW vs 0.4 GW** | **CONTAMINATED** | **xAI's fleet.** The 0.4 GW "as of 2025-06-30" is a date on which xAI was **not inside the SPCX reporting entity**. The +250% y/y is a within-xAI growth rate surfaced by recasting — **not evidence of SPCX's own capital deployment** |
| **AI segment capex $15,828M (Q2) · $23,551M (H1)** | **CONTAMINATED** | same |
| Consolidated revenue $7,814M · loss from ops $(143)M · net loss $(541)M | **CONTAMINATED** | includes the AI segment |
| Total capex $18,369M (Q2) · $28,476M (H1) | **CONTAMINATED** | includes AI |
| Cash flow — operating +$3,466M · investing $(34,487)M · financing +$100,291M | **CONTAMINATED** | includes an $85,675M IPO (itself a boundary event) and xAI-era financing |
| Balance sheet, Dec-31-2025 column | **CONTAMINATED** | recast post-merger |
| EPS $(0.09) · weighted-average shares | **CONTAMINATED (DA-28)** | 5-for-1 split 2026-05 + June 2026 IPO + $37,475M preferred conversion ([📄 SPCX 10-Q p.7](https://agentii.ai/v/SPCX/sec8/7)) — the weighted average straddles two capital structures. **Quarantine from any per-share growth series** |
| Cursor — ~$60B implied equity value, all-stock, closing Q3 2026 | **PENDING** | not yet in any reported figure |

Sources for the contaminated and clean rows:
[📄 SPCX 10-Q p.34](https://agentii.ai/v/SPCX/sec8/34) ·
[📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42) ·
[📄 SPCX 10-Q p.43](https://agentii.ai/v/SPCX/sec8/43) ·
[📄 SPCX 10-Q p.44](https://agentii.ai/v/SPCX/sec8/44) ·
[📄 SPCX 10-Q p.5](https://agentii.ai/v/SPCX/sec8/5) ·
[📄 SPCX 10-Q p.50](https://agentii.ai/v/SPCX/sec8/50)

### The AI revenue share, on both bases — because the single-basis quote is the trap

| Basis | AI revenue | Consolidated revenue | **Share** | Status |
|---|---:|---:|---:|---|
| **Q2 2026 (the quoted figure)** | $2,561M | $7,814M | **32.8%** | contaminated |
| H1 2026 | $3,379M | $12,508M | 27.0% | contaminated |
| **H1 2025 (recast)** | $1,465M | $8,138M | **18.0%** | contaminated, both periods |

**The 32.8% is a quarterly figure on a contaminated base; the same segment is 27.0% on the
half-year basis and 18.0% on the recast prior-year half.** Quoting only 32.8% maximises
the apparent migration *and* silently drops the recast. **Per §1c both are reported.** The
migration finding itself **survives** — but it rests on **Space falling (−1.9% H1)** and
**Connectivity's clean organic scale ($7,548M H1, 60.4% of revenue)**, exactly as PIL-6
requires, and on nothing in the AI column.

**Hand-off to the Phase 4 deliverable `_cross/spcx-nameplate-and-boundary.md`:** this
section is the per-figure classification PIL-6 owns, and it extends the spec's three-row
table (Space / Connectivity / AI) to **23 rows**, including the case the spec did not
name — **the 1.4 GW nameplate series is itself boundary-contaminated.** PIL-6's falsifier
(`count_of_spcx_growth_figures_unclassified_for_entity_boundary_effects = 0`) is
discharged for every figure quoted in this artifact.

**Verdict, extended: the Space series survives; the AI series does not; Connectivity also
survives; and the CONSOLIDATED series does not.**

---

## 5. DA-23 — four component identities, in-line, all closing exactly

**Mandatory under the register: an artifact reading `operating_income` shows
`gross profit − opex` in-line. `EPS × shares` is inadmissible and is not used anywhere in
this artifact.** All four identities below are built from the filing's own line items.

```
SPACE  (10-Q p.42)      revenue            962
                        cost of revenue   (329)   ->  gross profit  633   =  65.8% gross margin
                                                       R&D        (1,076)
                                                       SG&A          (99)
                        loss from ops                    (542)   <- closes EXACTLY
                        check: 329 + 1,076 + 99 = 1,504 total costs  =  filed total line, and 962 - 1,504 = (542)

CONNECTIVITY (p.43)     revenue          4,291
                        cost of revenue (2,060)   ->  gross profit 2,231  =  52.0% gross margin
                                                       R&D         (294)
                                                       SG&A        (281)
                        income from ops              1,656   <- closes EXACTLY

AI (p.44)               revenue          2,561
                        cost of revenue (1,106)   ->  gross profit 1,455
                                                       R&D       (2,178)
                                                       SG&A        (532)
                                                       restruct.     (2)
                        loss from ops               (1,257)  <- closes EXACTLY; 1,106+2,178+532+2 = 3,818 filed total

CONSOLIDATED (p.5)      revenue          7,814
                        cost of revenue (3,495)   ->  gross profit 4,319
                                                       R&D       (3,548)
                                                       SG&A        (912)
                                                       restruct.     (2)
                        loss from ops                 (143)  <- closes EXACTLY; and net loss (541)
```

**The Space identity required by this task closes exactly as stated: revenue $962M − cost
of revenue $329M = gross profit $633M (65.8%); − R&D $1,076M − SG&A $99M = $(542)M.**
Sources: [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42) ·
[📄 SPCX 10-Q p.43](https://agentii.ai/v/SPCX/sec8/43) ·
[📄 SPCX 10-Q p.44](https://agentii.ai/v/SPCX/sec8/44) ·
[📄 SPCX 10-Q p.5](https://agentii.ai/v/SPCX/sec8/5)

### The DERIVED cross-check — reported as a cross-check, not as the basis

```
consolidated loss from ops   (143)
  less Connectivity op income (1,656)
  less Space loss from ops      542        <- add back the loss
                              ---------
  AI loss from operations    (1,257)   <- EXACT match to the filed AI segment line
```

**The subtraction closes to the dollar — which is confirmation that the three segments
partition the company exactly, not that the AI line had to be derived.** §7 records why
that distinction matters.

### The platform IS stripped, at SPCX — and the filing is not

`search_xbrl_facts` returns `OperatingIncomeLoss` **+143,000,000** for Q2 2026 and
**+2,086,000,000** for H1 2026, and `get_company_financials` returns
`"operating_income": "143000000"` — **against a filing that prints `(143)` on the face of
the statements, in the segment note, and in the MD&A.** **The DA-23 flip census entry for
SPCX is CONFIRMED, and the flip is confirmed by the component identity above (detector 1,
fully reliable), not by sign reconciliation and not by `EPS × shares`.**

**A bounded observation handed to PIL-3, and it is not a PIL-3 conclusion.**
`validate_calculation` on accession `0001628280-26-052535` returns **9 pass / 2 warn / 18
fail** — including identities that close on the face of the filing. `get_calculation_tree`
shows the cause is structural: the `ConsolidatedStatementsofOperations` role builds
`OperatingIncomeLoss = Revenue − CostsAndExpenses` correctly, **but the balance-sheet arcs
carry stale comparative labels from an unrelated filer** (`"Preferred Stock; 5,000 shares
authorized; no shares issued and outstanding at December 31, 2014 or 2013"`,
`"45,000 shares authorized; 14,824 shares issued"`) — i.e. **the role set is partly
inherited from a different issuer's taxonomy.** The instrument therefore reports failures
that are **arc-selection artefacts, not filing defects**, and a PIL-3 artifact must
**not** read the 18 fails as 18 defective identities. Handed off with the accession and
the specific mislabelled arcs named.

---

## 6. A4 — the AI segment is ground-based, and the 1M-satellite filing is inadmissible

**Constitution A4, verbatim:** *"Terrestrial AI compute and orbital compute are different
businesses. They must never be valued as one. As of ratification, SPCX's AI segment is
ground-based (1.4 GW nameplate compute draw, Q2 2026); no listed issuer reports orbital
compute revenue. SPCX has separately sought approval for a constellation of up to 1
million satellites delivering **100 kW of compute per tonne** — a filed aspiration, not a
revenue line, and inadmissible as a valuation input."*

**The operational-KPI evidence is unambiguous on all four DA-20 axes.**

| Axis | SPCX's AI segment |
|---|---|
| compute **in** orbit | **No.** DA-11 counts *"GPUs installed in our data centers"* — the vocabulary of a terrestrial build |
| compute **for** orbit | **No** |
| communications **from** orbit | **No** — that is Connectivity, a separate segment |
| **terrestrial compute, ground-based** | **Yes** |

**Say it plainly: SPCX's AI segment is a ground-based data-center business.** Its 1.4 GW
is installed in data centers on the ground; its $15.8B quarterly capex is spent on data
centers on the ground; and the AI segment reports **no orbital revenue line** because
there is none.

**On the 1M-satellite / 100 kW-per-tonne filing: inadmissible as a valuation input, and
it is not even present here.** Three separate findings:

1. **It is not in this filing.** `search_keyword_in_source sec8 "kW"` returns **zero
   results**, and *"100 kW"* returns **zero**. The 10-Q the entire SPCX financial series
   rests on **does not contain the orbital-compute aspiration at all.**
2. **What the transcript adds is a launch timeline, not a revenue line.** Musk describes
   the **Starmind AI satellite** as *"essentially an optimized Vera Rubin NVL72
   computer"* and says *"we expect to start launching these next year"* — and, in the same
   answer, *"we expect to actually deploy this on the ground as well as in orbit"*
   ([📄 SPCX Q2 2026 call p.1](https://agentii.ai/v/SPCX/ect1/1)). **The same design is
   being deployed on the ground first.** A `CLAIMED` date with `MODELED`-at-best revenue,
   and by P10 condition 1 *"aspiration is not offtake."*
3. **P10's gate is not approached.** No named orbital-compute revenue line, no signed
   offtake, no radiator derivation, no array derivation, no flight $/kg, no TID
   assumption. **Orbital compute remains a watch item at SPCX, and the operational-KPI
   evidence strengthens the disconfirmation rather than weakening it:** the only actor
   with cheap orbital access deployed **1.4 GW — restated, up to 2.8 GW — on the ground**,
   and its own words are *"far more power, cooling and electrical equipment than we have
   GPUs"*, which is a statement about **terrestrial** infrastructure.

**Registered as the false-positive trap A4 and the constitution already name:** SPCX's
*"AI computational infrastructure"* is terrestrial compute and must never be read as
orbital compute. **This artifact is a second, independent confirmation of that trap.**

---

## 7. Corrections to 001 — frozen-001 policy applied

Per `spec.md` §1c: **001's artifacts are frozen and are not rewritten. Corrections are
recorded here and cited by location.** Two corrections and one platform note.

### 7.1 The AI operating line is FILED, not DERIVED — the inherited position is wrong

**Inherited instruction:** the 2310 pair supersedes the 1239 pair, and *"the superseding
position is that the AI operating line is NOT disclosed — it is `DERIVED` by subtraction
(consolidated $(143)M − Connectivity $1,656M − Space $(542)M). Report it as DERIVED,
never as filed."*

**The primary source contradicts this. The AI loss from operations is disclosed as
$(1,257)M four separate times:**

| Venue | Location | What it prints |
|---|---|---|
| **Note 18, Segment Information** | [📄 p.30](https://agentii.ai/v/SPCX/sec8/30) | `Income (loss) from operations \| (542) \| 1,656 \| (1,257) \| (143)` — **AI as its own column** |
| **MD&A, AI Segment Results** | [📄 p.44](https://agentii.ai/v/SPCX/sec8/44) | the **full cost stack** — revenue 2,561, cost of revenue 1,106, R&D 2,178, SG&A 532, restructuring 2, total 3,818, **loss from operations (1,257)** |
| **MD&A narrative prose** | [📄 p.45](https://agentii.ai/v/SPCX/sec8/45) | *"AI **loss from operations** for the three months ended June 30, 2026 decreased by $267 million, or 17.5%…"* |
| **Non-GAAP Segment Adjusted EBITDA reconciliation** | [📄 p.46](https://agentii.ai/v/SPCX/sec8/46) | repeats `(542) \| 1,656 \| (1,257) \| (143)` |

Plus the call: *"narrowed our AI segment net operating loss to **$1.3 billion**"*
([📄 SPCX Q2 2026 call p.3](https://agentii.ai/v/SPCX/ect1/3)).

**And on p.44 the component identity closes exactly**: 2,561 − 1,106 − 2,178 − 532 − 2 =
**$(1,257)M**, with the cost lines summing to the filed total of $3,818M. **Detector 1 —
fully reliable — confirms the value.** A DERIVED figure cannot have a filed cost stack
behind it summing to a filed total.

**Verdict:**
- **001's `1239` artifact was right** to report the AI operating line as $(1,257)M.
- **001's `2310` artifact — the nominal superseding one — is WRONG**, and its
  `AI (Grok, X, compute) | $2,561M | 32.8% | not disclosed | —` row replaced a correct
  disclosed figure with a false non-disclosure.
- **The DERIVED subtraction is a confirming cross-check** (it closes to the dollar) **and
  must not be reported as the primary basis.** Reporting it as the basis *understates
  what the issuer discloses*, which is the opposite failure from the usual one and just
  as damaging: an artifact that says "not disclosed" cannot be validated against the
  filing, and a reader would conclude the segment result is opaque when it is filed four
  ways.
- **A DERIVED grade here would fail the contract's own P4 logic** — it would attach the
  weaker grade to a stronger source.

**Corrected inheritance, for the ledger: AI loss from operations = $(1,257)M Q2 2026 /
$(3,726)M H1 2026, `DEMONSTRATED`, four citations, and boundary-contaminated (§4).**

### 7.2 The 1.4 GW is GPU nameplate, not "IT load"

001's artifact states the 1.4 GW is *"IT load only."* **The filed definition is narrower
than IT load** — *"the number of GPUs installed in our data centers … multiplied by their
respective all-in power draw"* ([📄 p.36](https://agentii.ai/v/SPCX/sec8/36)). **See §3.1.**
The consequence is not pedantic: it determines whether PIL-4's 1.2–1.5× reference band
applies to the ratio at all, and it is why §3.3 reports two readings. **The supersession
should be recorded in the ledger: DA-11's quantity is GPU nameplate ⊂ IT load.**

### 7.3 The 32.8% figure is contaminated, and 001's own files carry it unaudited

Both 001 SPCX artifacts quote the AI revenue share as migration evidence. **PIL-6's spec
already names this.** This artifact supplies the per-figure classification (§4) and the
two comparison bases (27.0% H1 2026; 18.0% H1 2025 recast) that make the contamination
visible. **No correction to 001's text is made here — the flag is recorded for the
Phase 4 `_cross/` deliverable and for the P5 ledger.**

### 7.4 Platform-instrument note for PIL-3

The 18 `validate_calculation` fails on this accession are **arc artefacts** — the
balance-sheet role carries another filer's stale share-count labels. **Recorded as a
bounded tool observation** (§5), with the accession named so PIL-3 can reproduce it.

### 7.5 A REGISTER GAP: no DA covers entity-boundary contamination

**Found while writing this artifact's own frontmatter, and it is a defect in the register,
not in this artifact.**

001 `spec.md` §1c registers **DA-01 through DA-22**. I checked all of them for the
hazard PIL-6 exists to test — **common-control recasting across a change of reporting
entity** — and **none covers it.** DA-19 is *orbital slot priority* (ITU filing date vs
bring-into-use milestone); DA-20 is *revenue recognition vs commitment* (ASC 606 vs
contract value vs backlog); DA-21 is *management-drawn segment boundaries*; DA-22 is
*private-company valuation*. **A search for "common control", "reporting entity" and
"recast" across 001 `spec.md` returns nothing.**

**Consequence: PIL-6 owns a named hazard class that the register does not name, and 001
already mis-labelled a different DA to fill the hole.** 001's
`2026-09-18_2310_business-model_methodology.md` lists `DA-19` with the chosen reading
*"common-control mergers (xAI, X) treated as a change of reporting entity, not organic
growth"* — **but DA-19 is orbital slot priority.** The mislabel passes the contract's
`da_id_registered` rule (which checks existence, not aptitude), so it is **mechanically
clean and substantively wrong** — the same silent-plausibility structure the whole
Data-Integrity Register exists to catch. **I did not propagate it**: this artifact's
frontmatter carries DA-21 (management-drawn segment boundaries, which is apt) and **no DA
pretending to be the recasting rule.**

**Hand-off, and it is actionable:** the register needs a **DA-29 — entity-boundary /
common-control recasting**, with the census the P6 sweep will produce (SPCX is the
worked case; the class recurs for any issuer that merges under common control mid-series).
Until it exists, PIL-6's per-figure classification has **no `da_id` to cite**, and every
002 artifact that touches SPCX's AI series will face the same choice between an
inapplicable DA and a silent omission. **Recommend routing to PIL-6, PIL-7 and the
constitution amendment queue.**

---

## Carry-forwards

1. **DA-07 / DA-08 VERIFIED at source, every figure.** 485 vs 652 t (**−25.6%**),
   Falcon 37 vs 45 (**−17.8%**), internal launches 27 vs 36 (**−25.0%**), Starship H1
   3 → 1, **10 of 37** customer, customer payload **87 vs 88 t (flat)**.
   [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35) — **two independent
   internal-contraction numbers exist (launches −25.0%, payload mass −29.5%); quote
   which.** *Escalate to PIL-1.*
2. **The decline is internal, not commercial.** Customer payload mass fell 1.1% while
   internal payload mass fell 29.5%. **DA-07 aggregates two businesses with opposite
   trends.** The launch-count decline is a **Starlink-deployment** signal, and the
   customer-launch count actually **rose 11.1% in Q2**. *PIL-1 and the synthesis.*
3. **PIL-4 IS RESOLVABLE and the spec says it is not.** The issuer-disclosed
   facility-side multiple is **1.5× expected / 2.0× tentative target**, giving a restated
   draw of **2.1 GW central, 2.8 GW target** against the filed 1.4 GW — full band
   **1.2–2.0×**. [📄 SPCX Q2 2026 call p.4](https://agentii.ai/v/SPCX/ect1/4).
   **PIL-4's falsifier fires on the target reading (2.00 > 1.5) and sits exactly at the
   threshold on the expected reading (1.50).** *PIL-4 and PIL-7 — the disposition moves
   from `UNRESOLVABLE-FROM-PUBLIC-SOURCES` to evaluable, with PUE-proper as the residual.*
4. **PIL-4's own claim fails at its ceiling.** "Lands within 1.2–1.5×" — **the 1.2× floor
   holds, the 1.5× ceiling does not.** The band is a PUE-proper reference range and was
   applied to a quantity that is not IT load. *PIL-4.*
5. **The MSFT comparison survives at ~0.97×, not "dwarfs."** At the top of the restated
   range SPCX's **entire cumulative** facility-side base is **roughly equal to the floor
   of MSFT's annual build**, not an order of magnitude below it. **Sign holds; magnitude
   must be restated.** *PIL-4 and 011.*
6. **PUE is neither disclosed nor benchmarkable on this platform.** Zero hits for "PUE"
   and "power usage effectiveness" in `sec8`; zero in VRT's 10-Q; no workspace artifact
   carries a sourced PUE. **The PUE-proper reading is BOUNDED (≈1.3–1.7×), not sourced**,
   and is frontmatter-registered as `pue_proper_residual:
   UNRESOLVABLE-FROM-PUBLIC-SOURCES`. *PIL-4.*
7. **PIL-6 CLASSIFIED, 23 figures, with the case the spec did not name: the 1.4 GW
   nameplate series is itself boundary-contaminated.** It is **xAI's fleet**; the 0.4 GW
   "as of 2025-06-30" is a date on which xAI was not inside the reporting entity.
   **Space CLEAN · Connectivity CLEAN · AI CONTAMINATED · consolidated CONTAMINATED.**
   For the growth-rate claim: **"AI is 32.8%" is contaminated; the same segment is 27.0%
   H1 2026 and 18.0% H1 2025 recast — all three must travel together or none may.**
   *Phase 4 `_cross/spcx-nameplate-and-boundary.md`; soft gate on 011.*
8. **The migration finding survives on the clean series only** — **Space fell 1.9% across
   the half while consolidated revenue rose 53.7%**, and Connectivity is $7,548M of H1
   revenue (60.4%). **Nothing in the contaminated AI column is needed to sustain it.**
9. **THE INHERITED POSITION IS WRONG: the AI operating line is FILED four times, not
   DERIVED.** $(1,257)M at [p.30](https://agentii.ai/v/SPCX/sec8/30),
   [p.44](https://agentii.ai/v/SPCX/sec8/44), [p.45](https://agentii.ai/v/SPCX/sec8/45),
   [p.46](https://agentii.ai/v/SPCX/sec8/46), with the cost stack summing to the filed
   $3,818M total. **001's `1239` was right; the `2310` supersession introduced the
   error.** The DERIVED subtraction is a confirming cross-check only. *Correction recorded
   under the frozen-001 policy; the ledger must grade it DEMONSTRATED.*
10. **DA-23 CONFIRMED at SPCX by detector 1, not by sign reconciliation.** All four
    segment identities close exactly in-line (§5); the platform field returns **+143M**
    for a filed **(143)M**. `EPS × shares` was not used. *PIL-3.*
11. **One platform-instrument caveat for PIL-3:** the 18 `validate_calculation` fails on
    this accession are **arc-selection artefacts** from stale comparative labels inherited
    in the balance-sheet role — **not 18 defective identities.** Accession named for
    reproduction. *PIL-3, bounded.*
12. **A4 CONFIRMED and the aspiration is not even in the filing.** `sec8` returns zero
    hits for "kW" and "100 kW"; the transcript adds only a `CLAIMED` launch timeline for
    the Starmind satellite, with the same design *"deploy[ed] on the ground as well as in
    orbit."* **Inadmissible as a valuation input; P10's five conditions are nowhere
    approached.** *A4, P10, PIL-2.*
13. **Two `CLAIMED` spoken figures must not displace filed ones:** *"roughly 2,500 tons a
    year to orbit via Falcon"* is **~20% above the filed H1 2026 annualised 2,082 t**; and
    the transcript's *"78 total launches"* is the Falcon+Starship basis against the filed
    Falcon-only **77**. *PIL-1.*
14. **NOT VERIFIED, and named as such:** no **per-vehicle payload capacity** appears
    anywhere in `sec8` — *"22.8"* returns zero hits and *"payload capacity"* returns only
    the mass-to-orbit metric pages. **PIL-1's Falcon 9 denominator stays
    `UNRESOLVABLE-FROM-PUBLIC-SOURCES` on this platform.** The filing supplies the
    **aggregate mass numerator** (1,041 t H1 2026) but **not** a per-launch, per-vehicle or
    per-destination denominator, and a realized average of 1,041 t ÷ 77 launches =
    **13.5 t** is **not** a substitute for the 22.8 t capability figure — it is a
    utilization-average across a mixed destination set (LEO, SSO, GTO, ISS), the same
    basis mismatch DA-11 warns about. **Reported to PIL-1 as a bound on the basis gap
    (~57–59% of the claimed capability), not as a denominator.**
15. **REGISTER GAP (§7.5): no DA covers entity-boundary / common-control recasting.**
    DA-01…DA-22 contain nothing for the hazard PIL-6 exists to test, and 001's
    `2310_business-model` artifact **mis-labels DA-19** (orbital slot priority) as
    "common-control mergers" — **mechanically clean under `da_id_registered`,
    substantively wrong.** **Recommend DA-29 — entity-boundary recasting.** *PIL-6, PIL-7,
    amendment queue.*
