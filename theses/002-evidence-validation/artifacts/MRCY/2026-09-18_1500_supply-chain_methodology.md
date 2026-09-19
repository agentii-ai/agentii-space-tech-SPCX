---
thesis_id: "002-evidence-validation"
pillar: PIL-2
ticker: MRCY
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: >
      Component identity `gross profit − opex = operating_income` run IN-LINE on all three fiscal
      years before any margin figure in this artifact is read. FY2026 closes (281,165 − 280,885 =
      280 = filed 280). FY2025 closes at −19,627 and FY2024 at −147,754, both matching the filed
      (19,627) and (147,754) — while the platform returns +19,627,000 and +147,754,000. Same
      magnitude, OPPOSITE SIGNS: two DA-23 hits on the comparators 001 used. The comparator
      corruption is what makes 001's "−98.6%" arithmetically obtainable and the true movement a
      favourable swing.
  - da_id: "DA-24"
    chosen_reading: >
      ASSET-SALE CONTAMINATION of `operating_income` — a gain on disposal flowing through the
      operating line, so the field measures a transaction rather than operations (register instance:
      EchoStar 2025 Q3, operating income 4.6x revenue; mechanism is COMPOSITION, not sign). TESTED AT
      MRCY AND NOT PRESENT: the candidate event is the Plan-Les-Ouates (Geneva) manufacturing
      disposal to Cicor Group (2025-04-15), and no disposal gain is identified in the operating line
      for FY2025 or FY2026 — FY2025's operating line is a loss of (19,627), and p.38 note (2) ties the
      Cicor transaction to *acquisition costs*, not a gain. MRCY is **DA-24-clean**. The Cicor event
      is nonetheless PRIMARY in this artifact for a DIFFERENT reason — it is the corpus's one
      observed instance of a defence-electronics manufacturing step moving outside the fence, with a
      measured delivery consequence. That is a supply-chain finding, and it is labelled as one, not
      as a DA-24 finding.
  - da_id: "DA-26"
    chosen_reading: >
      MRCY's full fiscal year (ended 2026-07-03) is labelled `fiscal_period: Q2` in the platform's
      metrics and filings records, and a Form 10-K is labelled `10-K / Q2`. Not in the published
      census; MRCY's value is `Q2`, a new value. Consequence: platform-derived quarterly capacity
      or revenue series for this issuer cannot be trusted to be quarterly.
  - da_id: "DA-27"
    chosen_reading: >
      MRCY's fiscal year ends in early July — a NEW CLASS beyond PL/AVAV/WWD/HEI (Jan/Apr/Sep/Oct).
      The platform label tracks the CALENDAR quarter of the period end, not the fiscal quarter,
      confirmed on 8 consecutive period ends. Any supply-chain time series taken from platform
      period labels for this issuer is offset by two fiscal quarters.
  - da_id: "DA-14"
    chosen_reading: >
      Radiation tolerance — rad-hard by process vs by design (TMR/redundancy) vs COTS with
      mitigation; the register notes these carry different cost curves by an order of magnitude, so a
      COTS claim and a rad-hard claim are not comparable. NOT RESOLVED by MRCY. The p.8 claim is
      "ruggedized, radiation-tolerant processing solutions" — no modality, no process, no
      redundancy scheme, no mitigation approach, no TID/SEU figure and no part-level identification.
      The largest cost-curve ambiguity in orbital compute stays ambiguous on this name, and by
      extension this issuer cannot be used to price the rad-hard premium.
  - da_id: "DA-15"
    chosen_reading: >
      Thermal rejection temperature — peak vs average; with or without an assumed heat pump.
      THE AMBIGUITY THIS PHASE MUST RESOLVE. Radiated power scales as T^4, so a 50 K assumption
      change moves radiator area by ~1.9x; the "with or without an assumed heat pump" branch is
      precisely the second F2 constant this phase seeks (COP at elevated rejection temperature).
      MRCY resolves neither branch — no rejection temperature, no peak/average basis, no heat pump,
      and (p.10) it PURCHASES rather than makes the thermal hardware. Recorded as the definition
      governing the UNRESOLVABLE finding rather than as a sourced reading.
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
f2_constants_from_this_leg: "NONE — and structurally so: MRCY BUYS its thermal hardware (blowers, p.10) rather than making it"
f2_falsifier_from_this_leg: "FIRES — no band sourced; the issuer is a thermal-hardware customer, not a supplier"
citations:
  - figure: "Thermal-management capability claim, verbatim — 'Mission-Ready ... Advanced thermal management and rugged packaging technology ensures optimal performance and reliable operation in the most challenging environments on Earth and beyond' — the ONLY thermal statement in the filing, carrying no magnitude of any kind"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 4
    url: https://agentii.ai/v/MRCY/sec205/4
    located_via: read_source_pages
  - figure: "Single- and limited-source component dependency, verbatim — 'certain components, including custom designed ASICs, static random access memory, FPGAs, microprocessors and other third party chassis peripherals (single board computers, power supplies, blowers, etc.), are currently available only from a single source or from limited sources' — 'blowers' is the only thermal-adjacent hardware noun in the filing and it is PURCHASED"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 10
    url: https://agentii.ai/v/MRCY/sec205/10
    located_via: read_source_pages
  - figure: "Supply-domain positioning, CLAIMED — 'The proliferation of low Earth orbit constellations requires ruggedized, radiation-tolerant processing solutions ... Space-qualified processing technologies will be required to address this growing segment of our addressable market' — no part, no standard, no TID/SEU figure"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 8
    url: https://agentii.ai/v/MRCY/sec205/8
    located_via: read_source_pages
  - figure: "Addressable market table by segment (Tier 2 defense electronics $66.1B 2026 → $106B 2031, 9.9% CAGR; Power Electronics, Platform & Mission Mgmt, C4I, Communications, EW, Radar, EO/IR, Acoustics, Weapons) — contains NO space segment. 'directed source'; 'the sole source for many unique capabilities'"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 7
    url: https://agentii.ai/v/MRCY/sec205/7
    located_via: read_source_pages
  - figure: "Customer posture — government/foreign-government programs 'approximately 97%, 97% and 95% of our total net revenues', 'primarily as a subcontractor or team member with defense prime contractors'; scaling risk naming 'our contract manufacturers such as Cicor in Europe'"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 13
    url: https://agentii.ai/v/MRCY/sec205/13
    located_via: read_source_pages
  - figure: "Contract-pricing rigidity, verbatim — 'supply chain, combined with our inability to adjust FFP contract pricing'; 'Our gross margins could be reduced, potentially significantly, if we cannot pass these costs to customers'; international revenue 2% of total FY2026 vs 5% FY2025 and FY2024; Cicor transitioning legacy Geneva manufacturing to Switzerland and the UK during fiscal 2027"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 16
    url: https://agentii.ai/v/MRCY/sec205/16
    located_via: read_source_pages
  - figure: "MD&A results table (component-identity source) — gross margin 281,165 / 254,494; total operating expenses 280,885 / 274,121; 'Income (loss) from operations | 280 | — | (19,627) | (2.1)'; Cicor strategic supply agreement dated April 15, 2025 with a five-year exclusive contract-manufacturing term; Star Lab asset acquisition April 30, 2025; platform revenue movements incl. Space +$22.0M and Airborne −$38.1M; 'no programs comprising 10% or more of our revenues'"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 32
    url: https://agentii.ai/v/MRCY/sec205/32
    located_via: read_source_pages
  - figure: "Gross-margin driver (cost, not price) — 'primarily driven by lower manufacturing variances of $15.8 million, partially offset by higher scrap, inventory reserves, and warranty provisions of $3.8 million, $2.3 million, and $1.1 million'; EAC net impact of changes in estimates (18,742) vs (21,070); R&D 'decreased $7.9 million, or 11.7% ... savings from headcount reductions of approximately 270 employees'; restructuring ~100 positions"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 33
    url: https://agentii.ai/v/MRCY/sec205/33
    located_via: read_source_pages
  - figure: "Consolidated statements of operations, three fiscal years — gross margin 281,165 / 254,494 / 195,901; total operating expenses 280,885 / 274,121 / 343,655; income (loss) from operations 280 / (19,627) / (147,754)"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 47
    url: https://agentii.ai/v/MRCY/sec205/47
    located_via: read_source_pages
  - figure: "Revenue disaggregation by platform — Space 78,021 / 55,972 / 60,546 with footnote (4) defining the Space platform; the disaggregation is by end platform, NOT by product or component, so it does not identify any supplied good"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 77
    url: https://agentii.ai/v/MRCY/sec205/77
    located_via: read_source_pages
  - figure: "One operating and reportable segment — no product-line or capability-level cost, margin or capacity disclosure exists; manufacturing footprint and AS9100 / IPC1791 / DMEA certifications; 518 R&D employees"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 9
    url: https://agentii.ai/v/MRCY/sec205/9
    located_via: read_source_pages
  - figure: "One operating and reportable segment — 'the CODM continues to evaluate and manage the Company on the basis of one operating and reportable segment'"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 75
    url: https://agentii.ai/v/MRCY/sec205/75
    located_via: read_source_pages
  - figure: "Demand is ARRIVING — record Q4 bookings $660M, +93.1% y/y, book-to-bill 2.3; record backlog >$1.9B; record next-12-month backlog ~$1B; full-year bookings $1.5B, +49.8%, book-to-bill 1.57; Q4 revenue $290M; FY2027 revenue 'approaching $1.1 billion'"
    ticker: MRCY
    form_type: earnings_call_transcript
    citation_id: ect70
    page_no: 1
    url: https://agentii.ai/v/MRCY/ect70/1
    located_via: read_source_pages
  - figure: "Backlog QUALITY, verbatim — 'burning down lower margin backlog and margins increasing as we move our way through the year'; guidance excludes unreceived demand: 'areas like CPA, effectors, munitions, space, missile defense, none of that is reflected in our outlook'"
    ticker: MRCY
    form_type: earnings_call_transcript
    citation_id: ect70
    page_no: 3
    url: https://agentii.ai/v/MRCY/ect70/3
    located_via: read_source_pages
  - figure: "⚠️ OBSERVED SUPPLY-CHAIN DISRUPTION from outsourcing, verbatim — 'over the last year, we have outsourced our manufacturing in our international business to a contract manufacturer. And we have seen a slowdown in deliveries as we have ramped up that contract manufacturer'; international sales down ~15%; and 'we do not talk about the margin profile of any of our products'"
    ticker: MRCY
    form_type: earnings_call_transcript
    citation_id: ect70
    page_no: 4
    url: https://agentii.ai/v/MRCY/ect70/4
    located_via: read_source_pages
  - figure: "Pipeline not yet converted — the multiyear munitions and framework opportunities 'are still potential tailwinds ... it is in our pipeline but yet to materialize in bookings'"
    ticker: MRCY
    form_type: earnings_call_transcript
    citation_id: ect70
    page_no: 5
    url: https://agentii.ai/v/MRCY/ect70/5
    located_via: read_source_pages
  - figure: "FY2026 gross margin 28.6% (+70bp); 'operating expenses as a percentage of revenue decreased by 150 basis points'; adjusted EBITDA $150M, +25.7%, 15.3% margin; free cash flow $68M; net debt $227M, −19.5%"
    ticker: MRCY
    form_type: earnings_call_transcript
    citation_id: ect70
    page_no: 2
    url: https://agentii.ai/v/MRCY/ect70/2
    located_via: read_source_pages
---

# MRCY — Supply-Chain Position: A Supplier to Whom, of What, and Does It Capture Rent?

**Sources.** Form 10-K, accession `0001049521-26-000045`, fiscal year ended 2026-07-03, filed
2026-08-18, 86 pages (`sec205`); Q4 FY2026 earnings call, 2026-08-18, 5 pages (`ect70`). Both
enumerated in full.

**The supply-chain question of record.** 002's matrix subscribes `supply-chain` Light for MRCY:
*"Validates the thermal and radiation supplier claims that F2/F4 rest on."* That is a claim about
MRCY's **position in a supply chain**, and position is answerable even when a physical constant is
not. This artifact answers it, and the answer is **negative on both axes** — MRCY is not on the
supply side of either F2's thermal hardware or F4's rad-hard parts, and the filing says so in
plain terms.

---

## 1. The DA-23 gate, first — the identity in-line before any margin is read

The contract requires the component derivation in-line for any artifact reading `operating_income`,
and the instrument rule forbids reading `validate_calculation`'s `status` column. Both applied.

**Component identity, `gross profit − total operating expenses`, on filed figures**
(`sec205` p.47 statements, cross-read against p.32 MD&A):

| Fiscal year | Gross profit | − Total opex | = Computed | Filed `Income (loss) from operations` | Closes? |
|---|---|---|---|---|---|
| **FY2026** (53wk, 2026-07-03) | 281,165 | 280,885 | **280** | **280** | ✅ |
| **FY2025** (52wk, 2025-06-27) | 254,494 | 274,121 | **−19,627** | **(19,627)** | ✅ |
| **FY2024** (52wk, 2024-06-28) | 195,901 | 343,655 | **−147,754** | **(147,754)** | ✅ |

**Instrument pair, `computed` vs `reported`, nothing else read.** FY2026
`us-gaap:OperatingIncomeLoss`: `computed = 280,000` / `reported = 280,000` — equal magnitude,
**same sign**, so **not** a DA-23 hit. `validate_calculation(0001049521-25-000024)` returned **no
`OperatingIncomeLoss` row**, so the FY2025 pair was obtained by pairing `search_xbrl_facts`
(**+19,627,000**) against the read-verified filed **(19,627)**.

**Result: two DA-23 hits, on the comparators, not on the headline period.**

| Period | Platform | Filed | Test | Verdict |
|---|---|---|---|---|
| FY2026 | +280,000 | 280 | same sign | **clean** |
| FY2025 | **+19,627,000** | **(19,627)** | equal, **opposite** | **HIT** |
| FY2024 | **+147,754,000** | **(147,754)** | equal, **opposite** | **HIT** |

**Competing bases, all reported (§1c, `no_single_basis_collapse`).** FY2025 operating income has
three, one dissenting: **Basis A** filed `(19,627)` at p.32 and p.47 (two venues); **Basis B**
component identity `254,494 − 274,121 = −19,627` (independent method); **Basis C** platform
`+19,627,000` (dissents in sign, agrees in magnitude). Two further instrument rows do not close and
are recorded rather than dropped: `us-gaap:GrossProfit` FY2026 `computed = −513,638,000` against
`reported = 281,165,000` (arc-selection artefact, no bearing on the `OperatingIncomeLoss` closure),
and `us-gaap:NetIncomeLoss` `computed = 28,105,000` against `reported = 29,673,000` (magnitudes
differ by 1,568k, so no sign claim is admissible).

**⚠️ Consequence for THIS artifact, stated before use.** 001's `"−98.6%"` is exactly
`(280 − 19,627)/19,627`, which requires the comparator to be **positive**. From the filed
comparator the movement is a **loss→profit sign crossing**, so no percentage is defined: the true
statement is a **+$19,907k favourable swing**, margin **+2.18 points** (`0.03%` vs `−2.15%`).
**001 consumed a sign-stripped comparator; it did not miscompute.** Also found here: the stripping
extends to `NetIncomeLoss` and `EarningsPerShareDiluted` (FY2026 +29,673k / +0.5 against filed
(29,673) / (0.50)), and the platform's MRCY metrics block contains **no negative value in any field
of any period** — so `EPS × shares` is inadmissible here not merely in principle but because the
platform's own EPS field is contaminated.

**Baseline established: FY2026 operating margin 0.03% is real and clean. FY2025 and FY2024 were
losses, and the trend is improvement, not collapse.**

---

## 2. MRCY's supply-chain position — the map

### 2.1 What MRCY supplies, and to whom

**Upstream, sub-tier, on fixed price.** Three filed facts define the position, and they are the
whole answer to the rent question:

> *"…approximately **97%, 97% and 95% of our total net revenues**"* come from U.S. and foreign
> government programmes, *"**primarily as a subcontractor or team member with defense prime
> contractors**."* — `sec205` p.13

> *"supply chain, combined with our **inability to adjust FFP contract pricing**…"* — `sec205` p.16

> *"Our gross margins could be reduced, **potentially significantly, if we cannot pass these costs
> to customers**."* — `sec205` p.16, on tariffs

> *"There were **no programs comprising 10% or more of our revenues** for fiscal 2026 or 2025."*
> — `sec205` p.32

Read as a supply-chain map rather than as a financial one:

| Layer | Who holds it | Evidence |
|---|---|---|
| End customer / demand | U.S. and allied governments | p.13 |
| **Prime contractor — the customer-facing layer** | **Raytheon, Lockheed, Northrop, Boeing et al.** | p.13, *"subcontractor or team member"* |
| Sub-tier supplier of electronics | **MRCY** | p.13 |
| Price setting | **The contract form (FFP), i.e. the prime/customer** | p.16 |
| Cost pass-through | **Not available** — filed as a risk, not a lever | p.16 |
| Programme concentration | **None ≥10%** — no chokepoint in either direction | p.32 |

**MRCY is the third layer down, sells on price terms it says it cannot adjust, and has no
programme large enough to withhold.** Scarcity rent requires an ability to price the scarce thing.
MRCY's own risk factors state it does not have that ability. **This is structural, not cyclical:**
it is a property of the contract form, so it does not change when demand arrives — a point that
matters directly to 001's open dichotomy, below.

### 2.2 What MRCY buys, and from where

This is the reverse direction, and it is where the F2 evidence actually lives.

`sec205` p.10, verbatim:

> *"certain components, including **custom designed ASICs, static random access memory, FPGAs,
> microprocessors and other third party chassis peripherals (single board computers, power supplies,
> **blowers**, etc.), are currently available only from a single source or from limited sources."*

**⚠️ "Blowers" is the only thermal-adjacent hardware noun in the entire 86-page filing.** It appears
in a list of **purchased, third-party, single-or-limited-source** chassis peripherals. MRCY does not
manufacture thermal hardware. It **buys** it, from one or a few vendors, and files the dependency as
a supply risk.

**This is a stronger negative than silence.** An `UNRESOLVABLE-FROM-PUBLIC-SOURCES` finding because a
document says nothing is weak — the next filing, or a competitor, might fill it. A finding that also
shows the issuer is a **customer** of the capability is structural: no amount of future disclosure
by MRCY can make it an F2 supply-chain leg without a change in what it manufactures. The
`supply-chain` hypothesis for this name should be retired, not deferred.

Corroborating, from the same filing's self-description (`sec205` p.5): MRCY's value-add is
described as **Components, Modules and Sub-assemblies, and Integrated Solutions** — integration of
*other people's* silicon (**Altera Agilex 9, AMD FPGAs, NVIDIA GPUs**, p.6) onto boards and into
chassis, under open standards (**RACEway, RapidIO, VXS, VPX, REDI, OpenVPX, VITA100, SOSA**).
**Integration of purchased parts is the business model; the parts, including the thermal ones, are
inbound.**

### 2.3 The one place MRCY claims a supply position — and it is the wrong capability

`sec205` p.7 lists MRCY's addressable market as nine named defence-electronics segments totalling
**$66.1B (2026) → $106B (2031), 9.9% CAGR** — Power Electronics, Platform & Mission Management,
C4I, Communications, EW, Radar, EO/IR, Acoustics, Weapons — with the claim that MRCY is *"the sole
source for many unique capabilities."*

> **⚠️ The table contains no space segment.** The market MRCY sizes for itself is terrestrial
> defence electronics in all nine segments. Space appears in the filing only as narrative growth
> commentary (p.8) and as a revenue disaggregation line (p.77), never as a sized market.

The strongest supply-position claim MRCY makes anywhere in the corpus is on the call
(`ect70` p.4): *"we have been the **only provider of the CPA technology in the security
apparatus**"* — and the only higher-margin niche it identifies is **memory security**, *"that part
of our business tends to run at the higher end of our margin profile."*

**Both are terrestrial and neither is radiation.** If radiation-tolerant processing were the scarce
input MRCY supplies, the sole-source claim and the high-margin niche would be where it says so. It
names ruggedized servers in a security apparatus, and memory. `DA-14` (rad-hard vs COTS modality)
is therefore **not resolved by this name**, and the largest cost-curve ambiguity in orbital compute
stays ambiguous.

### 2.4 The radiation claim, graded

`sec205` p.8, verbatim:

> *"The proliferation of low Earth orbit constellations requires **ruggedized, radiation-tolerant
> processing solutions** that can operate reliably in the harsh space environment… **Space-qualified
> processing technologies will be required** to address this growing segment of our addressable
> market."*

Graded **`CLAIMED` (DA-16)**. No part number, no TID figure, no SEU/SEFI rate, no orbit or mission
profile, no qualification standard (no MIL-STD-1540, MIL-STD-883, no RHBD/RHBP), no revenue
attribution, and **no supply commitment of any kind.** It is a statement about where MRCY would like
to sell, written in the conditional future tense, in the same document that sizes its market without
a space segment (p.7) and that describes its thermal capability without a number (§3.1).

**A firm selling a scarce input describes what it ships. MRCY describes what will be required of
someone.**

---

## 3. The two F2 constants — `UNRESOLVABLE-FROM-PUBLIC-SOURCES`, and structurally so

PIL-2 asks this phase to source the **radiator areal density** (001 used **8 kg/m² as an admitted
placeholder**) and the **heat-pump COP at elevated rejection temperature**. **MRCY supplies
neither, and this artifact does not supply a value for either.** No padding.

### 3.1 The one thermal statement, and why it is not a source

`sec205` p.4, verbatim — the **only** thermal statement in the filing, and the sole basis for any
F2 supplier claim on this name:

> *"**Mission-Ready**: Fit for purpose to meet the demanding needs of our customers' missions.
> **Advanced thermal management and rugged packaging technology** ensures optimal performance and
> reliable operation in the most challenging environments **on Earth and beyond**. We deliver
> extended reliability and dependability through **thermal management, component selection,
> environmental protection and testing**."*

Three reasons this is not an F2 source:
1. **`CLAIMED`, no magnitude** — no W/m², kg/m², COP, ΔT, material, fluid, loop, or pump. Nothing.
2. **It describes packaging, not a thermodynamic cycle.** F2's constants characterise a rejection
   loop: area per MW, mass per MW, and the work required to lift heat to the rejection temperature.
   MRCY describes *"rugged packaging technology."*
3. **"on Earth and beyond" is the entire space content** — three words.

### 3.2 Search record, so the negative claim is auditable

Against `sec205` (86 pages) and `ect70` (5 pages):

| Term | `sec205` | `ect70` | Read-verified disposition |
|---|---|---|---|
| `radiator` | 1 hit (p.8) | 0 | ⚠️ **stemming false positive** — see below |
| `areal density` | 0 | not run | absent |
| `heat pump` | 0 | not run | absent |
| `coefficient of performance` | 0 | not run | absent |
| `waste heat` | 0 | not run | absent |
| `liquid cooling` | 0 | not run | absent |
| `cooling` | 0 | not run | absent |
| `heat` | 0 | not run | absent |
| `refrigerant` | 0 | not run | absent |
| `kW` | 0 | not run | absent |
| `thermal` | 2 hits (pp. 4, 8) | 0 | both read in full; neither carries a number |
| `thermal management` | 1 hit (p.4) | not run | quoted in full at §3.1 |
| `radiation` | 1 hit (p.8) | 0 | qualitative capability claim, §2.4 |
| `radiation hardened` | 0 | not run | absent |

**⚠️ The `radiator` hit is a false positive and must not be counted as a disclosure.** It resolves
to p.8, which I read in full: the page contains *"**radiation**-tolerant processing solutions"* and
*"thermal extremes from arctic to desert operations"* — **no radiator.** The index is stemmed, so
`radiator` matches `radiation`. **Flagged explicitly, because a naive read of that hit would
fabricate an F2 source from a radiation claim — the worst available outcome in this phase.**

**⚠️ Honest limit on the zero rows.** `cooling` and `heat` returning zero in an 86-page
manufacturing disclosure that elsewhere mentions "blowers" indicates a coarse index, not absence.
The conclusion rests primarily on the **full outline sweep of both documents** — all 86 page
descriptions enumerated, every product/technology page (pp. 3–10) read in full — with the keyword
record as corroboration. Stated as *"no disclosure located via these searches,"* not as an absolute.

### 3.3 Acceptance test — the falsifier FIRES on this leg

Spec §1b: `metric=f2_radiator_mass_per_MW_uncertainty_band_pct`, `threshold=0.50`, `op=>`.

**MRCY yields no band for either constant** — and §2.2/§3.1 give the structural reason: it does
not manufacture the hardware class the constants describe. **The falsifier FIRES.**

> **⚠️ NOTIFICATION — CONDITION DISCHARGED, NOT PENDING.** `_cross/f2-constant-sourcing.md` records
> **two independent acceptance-test breaches**; **F2 has downgraded to a qualitative bound and 003
> and 009 have already been notified** (appended 2026-09-18). This leg does not re-open that.
> - The cross file sources radiator areal density at **1.0–11 kg/m²** (±83% un-scoped, **±56%
>   advanced-class**, ±35% crewed-class) — **the band is WIDE, not absent**, and two of three scopes
>   breach ±50% unaided. *(⚠️ Inherited; not independently verified in this leg.)*
> - The derivable COP axis alone spans **+43% to +150%** by thermodynamics.

**⚠️ Contract gap — surfaced by this leg, escalated in the cross file.** PIL-2's falsifier specifies
`source=peer_reviewed_literature_or_flown_hardware_disclosure`, while the artifact contract's
`citation_url_wellformed` rule (level `fail`) admits **only `agentii.ai` URLs**. **The source class
the falsifier tests against therefore cannot be recorded in any artifact** — a *passing* evaluation
would be unrecordable, not merely hard. This leg reaches the same conclusion from the supply side:
the entities that hold these constants are **thermal-subsystem houses publishing datasheets**, not
issuers filing 10-Ks, so a filing-only sweep across the subscribed company set **cannot** satisfy
the criterion regardless of how many legs run. Escalated to `_cross/f2-constant-sourcing.md` and
P7's disposition census.

**The 8 kg/m² placeholder remains `MODELED` and unsourced. Nothing here upgrades it** — and the
cross artifact supplies a stronger reason than this leg could: **8 kg/m² is a crewed/ISS-class
value** (5.3–11 kg/m²) applied to a **mass-optimized uncrewed platform** whose alternatives run
**1.0–3.5 kg/m²**, a **2.7–5× mismatch in F2's own favour**. *(Inherited from the cross artifact;
not verified in this leg.)* This leg adds only the negative: **it did not come from MRCY**, which
does not make the hardware it would describe.

---

## 4. ⚠️ The one live supply-chain datum: MRCY outsourced a manufacturing step and deliveries slipped

This is the most decision-relevant supply-chain finding in the artifact, and it is **observed, not
inferred.**

**Event — a supply-chain datum, NOT a DA-24 finding.** ⚠️ *The Cicor disposal was tested against
DA-24 (asset-sale contamination of `operating_income`) and MRCY is DA-24-CLEAN — no disposal gain
is identified in the FY2025 or FY2026 operating line. The event is recorded here for its physical
supply-chain consequence, and this section makes no DA-24 claim.* On **2025-04-15** MRCY entered a strategic supply agreement under which **Cicor
Group acquired MRCY's manufacturing operations at Plan-Les-Ouates, Switzerland**, and
*"**exclusively provides contract manufacturing** to supply the Company's international operations
with electronic products over the next **five years**"* (`sec205` p.32). Geneva manufacturing
transitions to Switzerland and the UK during fiscal 2027 (`sec205` p.16).

**Observed consequence** (`ect70` p.4, verbatim):

> *"over the last year, we have **outsourced our manufacturing in our international business to a
> contract manufacturer**. And we have **seen a slowdown in deliveries as we have ramped up that
> contract manufacturer**."*

**Measured consequence** (`sec205` p.16, `ect70` p.4): international revenue fell to **2% of total
net revenues in FY2026** from **5% in FY2025 and FY2024**, with international sales **down ~15%
y/y**.

**Why this is worth recording in a space thesis.** It is a **directly observed instance of what
happens to a defense-electronics supplier's delivery schedule when a manufacturing step moves
outside the fence** — in a low-volume, certified, AS9100/IPC1791/DMEA-regulated production
environment (`sec205` p.9). The relevant generalisation for the orbital buildout:

- **Certified manufacturing capacity is not fungible and not quickly scalable.** MRCY ran a
  contract-manufacturer ramp for roughly a year and lost delivery throughput the whole time, on
  ~2–5% of its revenue. That is the transition cost on a small, mature, already-qualified product
  set.
- **The direction of travel is contraction, not expansion.** MRCY divested manufacturing, cut
  ~270 positions (`sec205` p.33), cut ~100 more in FY2026 restructuring (p.33), and cut R&D 11.7%
  (p.33). Whatever the radiation-tolerant capability is, **its industrial capacity is shrinking.**
- **⚠️ Both readings, per §1c.** The alternative reading is that this is competent portfolio
  management: MRCY exited a non-core, low-scale European manufacturing footprint and freed cash —
  free cash flow was **$68M** and net debt fell 19.5% to **$227M** (`ect70` p.2). On that reading
  the delivery slowdown is a one-time transition cost, not evidence about the sector's supply
  elasticity. **The evidence does not discriminate**, and this artifact does not collapse it: what
  is established is that **the one observed instance of defence-electronics manufacturing
  re-sourcing in the corpus produced a delivery slowdown lasting more than a year.**

---

## 5. The rent question, answered on supply-chain grounds

001 asked whether *"the demand has not arrived"* or *"radiation tolerance is not a scarce input."*
**On this name it is the second, and the reason is contractual, so it will not resolve when demand
arrives.** Demand is, in fact, arriving.

### 5.1 Demand HAS arrived — this is the strongest form of the negative control

`ect70` p.1 and p.3, verbatim:

- **Q4 FY2026 bookings $660M, +93.1% y/y, book-to-bill 2.3**
- **Record backlog >$1.9B**; record next-12-month backlog ~$1B
- **FY2026 bookings $1.5B, +49.8%, book-to-bill 1.57**
- *"burning down **lower margin backlog** and margins increasing as we move our way through the
  year"*
- *"areas like CPA, effectors, munitions, **space**, missile defense, **none of that is reflected in
  our outlook**"*

**A 1.57 book-to-bill with record backlog is the demand signal.** It arrived in FY2026 and the
operating margin is still **$0.280M on $983.6M — 0.03%**. So 001's first branch is **closed by
evidence**: this is not a demand-arrival question. The rent is not appearing despite the bookings.

### 5.2 Why — and this is where the supply-chain lens adds what the financial one cannot

**Book-to-bill 1.57 with an operating margin of 0.03% is only possible if the incremental bookings
carry, at best, the same thin margin as the base.** The CFO says it directly: the backlog being
burned down in early FY2027 is **"lower margin backlog"** (`ect70` p.3). Compare the direction the
company says margin comes from (`sec205` p.33): **"lower manufacturing variances of $15.8 million"**
— factory execution — against the **changes-in-estimates table**: gross favourable 28,847 against
gross unfavourable **(47,589)**, net **(18,742)**, second consecutive year of a ~1.65:1 unfavourable
skew (p.33).

**This is the supply-chain signature of a price-taker, and it is the sharpest available test:**

| Signature of a supplier holding a scarce input | MRCY, FY2026 | Evidence |
|---|---|---|
| Books at rising prices as capacity tightens | **Books lower-margin backlog** at 1.57 book-to-bill | ect70 p.3 |
| Margin driven by price | Margin driven by **manufacturing variances** ($15.8M) | sec205 p.33 |
| Cost increases passed through | *"inability to adjust FFP contract pricing"*; *"cannot pass these costs to customers"* | sec205 p.16 |
| Contract estimates converge | **$47.6M unfavourable vs $28.8M favourable** estimate revisions, 2 yrs running | sec205 p.33 |
| Sole-source parts command premium | Sole-sources are **inbound** (ASICs, SRAM, FPGAs, blowers) | sec205 p.10 |

**Every row points the same way.** MRCY is a competent integrator in a competitive sub-tier
position, on cost-plus-like economics with none of the pass-through protections, and its margin is
manufacturing-execution noise around zero.

### 5.3 The quantitative statement, and the honest limit

**Space platform revenue grew +$22.0M** (`sec205` p.32; cross-checked against p.77 —
78,021 − 55,972 = **22,049**, a second component identity, and it closes) — a **+39.4%** increase —
while **consolidated operating income was +$0.280M.**

**Read carefully, because the causation is tempting and wrong.** The 0.03% margin is caused by
**opex absorbing gross profit** ($280,885k of opex against $281,165k of gross margin, §1) — not by
the space line. The space line is a **revenue disaggregation by end platform, not a segment**
(one segment, p.75; footnote (4) at p.77), so its margin is not separable and **its contribution to
that $0.280M is not knowable from disclosure.** What the numbers do establish is descriptive and
sufficient: **the gate-adjacent revenue line grew 39% inside a P&L that earns nothing at the
operating line, and did not change that.**

### 5.4 The capability is un-inspectable by design — and therefore unanswerable here

- **One operating and reportable segment** (`sec205` p.75).
- *"we do not talk about **the margin profile of any of our products**"* — CFO, `ect70` p.4.

There is **no product-level or capability-level margin, cost, capacity, unit, or lead-time
disclosure anywhere in either document.** "Does MRCY earn rent on radiation-tolerant parts?" is not
a question this issuer's disclosure can answer at any level of effort. Disposition:
**`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — the disclosure exists *as a business*, but the metric is
withheld. Distinct from the F2 constants (§3), where the physical quantity is simply absent.

---

## 6. What could NOT be verified

| Item | Disposition | Class |
|---|---|---|
| Radiator areal density (kg/m²) | **Not disclosed.** MRCY *buys* thermal hardware (p.10) | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — structurally |
| Heat-pump COP at elevated rejection temperature | **Not disclosed** in any form | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — structurally |
| Any F2-relevant magnitude (W/m², kg/kW, ΔT, mass) | **Absent.** p.4 claim is packaging, unquantified | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Rad-hard vs COTS **modality** (DA-14) | **Not resolved.** p.8 says "radiation-tolerant," unqualified | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Mission-specific TID / SEU (F4) | **Not disclosed** — no figure, no standard, no mission | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Product / capability-level margin, cost, capacity | **Withheld by policy** — one segment; *"we do not talk about the margin profile of any of our products"* | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| MRCY's **supplier** identities beyond "single or limited source" | **Not named** except Cicor; ASICs/SRAM/FPGA/microprocessor/blower vendors are undisclosed | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Cicor contract value, volume, pricing, capacity | **Not disclosed** — only the five-year exclusivity (p.32) | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| FY2023 `OperatingIncomeLoss` DA-23 status | Platform returns **+21,685,000**; filed figure **not read-verified** and FY2023 is outside `sec205`'s three-year presentation. **Recorded as open; no claim made.** | `UNRESOLVABLE-FROM-PLATFORM` for the current corpus |
| `validate_calculation` FY2025 pair | Instrument returned **no `OperatingIncomeLoss` row** for `0001049521-25-000024` | `UNRESOLVABLE-FROM-PLATFORM` |
| ⚠️ **"Organic growth 7.9%"** | **Competing basis, flagged.** *"There were **53 weeks and 52 weeks** included in the results of operations for fiscal 2026 and fiscal 2025, respectively"* (p.32). The +7.9% and the call's "FY 2026 **organic** revenue growth of 7.9%" (`ect70` p.1) are on a **53-vs-52-week basis**; the extra week's contribution is **not quantified anywhere**. Correctly computed; comparability unquantified. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` for the extra-week adjustment |

---

## 7. Corrections to 001 — frozen-001 policy applied

001 is **not rewritten**; corrections are recorded here and cross-cited.

| # | 001 says | Primary source shows | Status |
|---|---|---|---|
| 1 | *"Form 10-K, accession `0001049521-26-000045` (FY2026 **Q2**, period ended 2026-07-03)"* | It is the **FY2026 full-year 10-K** (53 weeks, p.3); $983.6M is **annual** revenue | **Corrected** |
| 2 | *"Q2 FY2026 / Q2 FY2025"* column headers | Both are **fiscal years** (p.32, p.47) | **Corrected** |
| 3 | *"Operating income … $19.6M … **−98.6%**"* | Filed comparator **$(19,627)k**; true movement **+$19,907k favourable**, margin **+2.18 pts**. −98.6% is obtainable only from the stripped value | **Corrected** |
| 4 | Operating margin *"2.2% / −2.1 pts"* | Filed **(2.1)**; FY2026 **+0.03%** → **+2.18 points of improvement** | **Corrected** |
| 5 | *"MRCY is clean (components reconcile exactly)"* | **True for FY2026; false for both comparators** — DA-23 hits on FY2025 and FY2024 | **Corrected** |
| 6 | *"no space segment, no rad-hard revenue…"* | **Space platform revenue IS disclosed** — 78,021 / 55,972 / 60,546 (p.77), 7.9% of revenue, +39.4% y/y; *"an integrated space program"* is a named largest increase (p.32); a dedicated space growth section at p.8 | **Overturned** |
| 7 | MRCY *"cannot serve as evidence of the radiation-tolerance market"* | **Conclusion stands, premise does not.** Revenue *is* broken out; margin is not — one segment (p.75), no product margins (`ect70` p.4) | **Reasoning replaced** |
| 8 | — (new here) | **MRCY is not an F2 supply-chain leg and cannot become one without changing what it manufactures** — it *buys* thermal hardware (p.10) | **Added** |

**Mechanism note, because it recurs.** `get_company_financials` returns the filing record as
`{document_type: 10-K, fiscal_year: 2026, fiscal_period: "Q2", period_end: 2026-07-03}` — **a 10-K
labelled `Q2`.** 001 did not misread; it **faithfully transcribed a platform label.** Same failure
path as #3: nothing computed wrong, a corrupt input consumed. **The defect is systematic, not
author-specific** — any artifact reading `fiscal_period` from this platform for this issuer
reproduces it.

---

## 8. Carry-forwards

1. **⚠️ F2's falsifier FIRES on the MRCY leg, and the platform-level condition is DISCHARGED**
   (§3.3). `_cross/f2-constant-sourcing.md` records two independent breaches, **F2 has downgraded to
   a qualitative bound, and 003 and 009 have already been notified.** The band is **wide (±56%
   advanced-class ±83% un-scoped)**, not absent, so the downgrade survives the constants being
   found. **Do not restate this as pending.**
2. **⚠️ Retire MRCY from the F2 sourcing plan — do not merely mark it "no disclosure found."**
   It **buys** its thermal hardware ("blowers," single/limited source, p.10). It is a customer of the
   capability, not a supplier of it, and no future MRCY filing changes that (§2.2). **This is the
   leg's whole contribution to the F2 lock, and it is a deletion, not a datum.**
3. **⚠️ F2's falsifier source class cannot be recorded, let alone met, from filings.** The spec
   accepts `peer_reviewed_literature_or_flown_hardware_disclosure`; the contract's
   `citation_url_wellformed` rule (`fail`) admits **only `agentii.ai` URLs**, so a *passing*
   evaluation is unrecordable. Independently, the entities holding these constants are
   **thermal-subsystem houses publishing datasheets**, not issuers filing 10-Ks — so **no number of
   filing-reading legs can satisfy the criterion.** Both halves escalated to
   `_cross/f2-constant-sourcing.md` and to P7's disposition census; this is a **contract amendment**,
   not a research gap.
4. **⚠️ `EPS × shares` inverts rather than merely degrades.** The platform's own `eps_diluted` for
   MRCY is sign-stripped (+0.5 / +0.65 / +2.38 against filed (0.50) / (0.65) / (2.38)). A detector
   built on it returns a *positive* EPS for a loss year and would **confirm** an inversion. Restate
   the contract exclusion to DA-23 with this reason attached.
5. **⚠️ Run DA-23 on every period an artifact quotes, not the headline period** (§1). This is the
   mechanism that corrupted 001 with a correct register entry, and it generalises across every
   multi-period table in this program. **Highest-value carry-forward.**
6. **⚠️ Period labels from `get_company_financials` do not identify fiscal periods on
   non-December year-ends** (§7). MRCY is a **5th DA-27 instance in a new class** (early-July
   year-end) and a **DA-26 instance with a new label value** (`Q2`). A calendar-quarter cross-check
   should be mandatory before any platform period label is used.
7. **⚠️ Record the Cicor delivery slowdown as the corpus's one observed manufacturing
   re-sourcing event** (§4): outsource in 2025-04, *"a slowdown in deliveries as we have ramped up
   that contract manufacturer"* (`ect70` p.4), international revenue 5% → 2%. Relevant to any
   buildout thesis that assumes certified defense-electronics capacity scales on demand. Both
   readings reported; not collapsed.
8. **The rent conclusion is now closed on the demand branch** (§5.1). Book-to-bill **1.57** with
   record backlog **>$1.9B** and an operating margin of **0.03%** means demand arrived and the rent
   did not. PIL-2 should stop hedging: on this name it is **not a scarce input**, for contractual
   reasons (97% government, sub-tier subcontractor, FFP unable to reprice) that do not resolve with
   demand.
9. **001 correction #6 must propagate** — *"MRCY discloses no space segment"* is false and is cited
   in 001 §1 and §3. Space revenue is at p.77. 001's file is frozen; the correction lives here.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Thermal-management capability claim, verbatim — 'Mission-Ready ... Advanced thermal management and rugged packaging technology ensures optimal perform | [📄 MRCY 10-K p.4](https://agentii.ai/v/MRCY/sec205/4) **(newly surfaced)** |
| Single- and limited-source component dependency, verbatim — 'certain components, including custom designed ASICs, static random access memory, FPGAs,  | [📄 MRCY 10-K p.10](https://agentii.ai/v/MRCY/sec205/10) **(newly surfaced)** |
| Supply-domain positioning, CLAIMED — 'The proliferation of low Earth orbit constellations requires ruggedized, radiation-tolerant processing solutions | [📄 MRCY 10-K p.8](https://agentii.ai/v/MRCY/sec205/8) **(newly surfaced)** |
| Addressable market table by segment (Tier 2 defense electronics $66.1B 2026 → $106B 2031, 9.9% CAGR; Power Electronics, Platform & Mission Mgmt, C4I,  | [📄 MRCY 10-K p.7](https://agentii.ai/v/MRCY/sec205/7) **(newly surfaced)** |
| Customer posture — government/foreign-government programs 'approximately 97%, 97% and 95% of our total net revenues', 'primarily as a subcontractor or | [📄 MRCY 10-K p.13](https://agentii.ai/v/MRCY/sec205/13) **(newly surfaced)** |
| Contract-pricing rigidity, verbatim — 'supply chain, combined with our inability to adjust FFP contract pricing'; 'Our gross margins could be reduced, | [📄 MRCY 10-K p.16](https://agentii.ai/v/MRCY/sec205/16) **(newly surfaced)** |
| MD&A results table (component-identity source) — gross margin 281,165 / 254,494; total operating expenses 280,885 / 274,121; 'Income (loss) from opera | [📄 MRCY 10-K p.32](https://agentii.ai/v/MRCY/sec205/32) **(newly surfaced)** |
| Gross-margin driver (cost, not price) — 'primarily driven by lower manufacturing variances of $15.8 million, partially offset by higher scrap, invento | [📄 MRCY 10-K p.33](https://agentii.ai/v/MRCY/sec205/33) **(newly surfaced)** |
| Consolidated statements of operations, three fiscal years — gross margin 281,165 / 254,494 / 195,901; total operating expenses 280,885 / 274,121 / 343 | [📄 MRCY 10-K p.47](https://agentii.ai/v/MRCY/sec205/47) **(newly surfaced)** |
| Revenue disaggregation by platform — Space 78,021 / 55,972 / 60,546 with footnote (4) defining the Space platform; the disaggregation is by end platfo | [📄 MRCY 10-K p.77](https://agentii.ai/v/MRCY/sec205/77) **(newly surfaced)** |
| One operating and reportable segment — no product-line or capability-level cost, margin or capacity disclosure exists; manufacturing footprint and AS9 | [📄 MRCY 10-K p.9](https://agentii.ai/v/MRCY/sec205/9) **(newly surfaced)** |
| One operating and reportable segment — 'the CODM continues to evaluate and manage the Company on the basis of one operating and reportable segment' | [📄 MRCY 10-K p.75](https://agentii.ai/v/MRCY/sec205/75) **(newly surfaced)** |
| Demand is ARRIVING — record Q4 bookings $660M, +93.1% y/y, book-to-bill 2.3; record backlog >$1.9B; record next-12-month backlog ~$1B; full-year booki | [📄 MRCY earnings call transcript p.1](https://agentii.ai/v/MRCY/ect70/1) **(newly surfaced)** |
| Backlog QUALITY, verbatim — 'burning down lower margin backlog and margins increasing as we move our way through the year'; guidance excludes unreceiv | [📄 MRCY earnings call transcript p.3](https://agentii.ai/v/MRCY/ect70/3) **(newly surfaced)** |
| ⚠️ OBSERVED SUPPLY-CHAIN DISRUPTION from outsourcing, verbatim — 'over the last year, we have outsourced our manufacturing in our international busine | [📄 MRCY earnings call transcript p.4](https://agentii.ai/v/MRCY/ect70/4) **(newly surfaced)** |
| Pipeline not yet converted — the multiyear munitions and framework opportunities 'are still potential tailwinds ... it is in our pipeline but yet to m | [📄 MRCY earnings call transcript p.5](https://agentii.ai/v/MRCY/ect70/5) **(newly surfaced)** |
| FY2026 gross margin 28.6% (+70bp); 'operating expenses as a percentage of revenue decreased by 150 basis points'; adjusted EBITDA $150M, +25.7%, 15.3% | [📄 MRCY earnings call transcript p.2](https://agentii.ai/v/MRCY/ect70/2) **(newly surfaced)** |
