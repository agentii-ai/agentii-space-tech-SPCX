---
thesis_id: "002-evidence-validation"
pillar: PIL-2
ticker: MRCY
skill: secular-trends
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "e6b41dbb2426"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: >
      Component identity `gross profit − opex = operating_income` run IN-LINE on three fiscal years.
      FY2026 CLOSES: 281,165 − 280,885 = 280 = filed 280. MRCY is NOT a DA-23 hit in the period the
      constitution names. FY2025 and FY2024 ARE HITS: the platform returns +19,627k and +147,754k
      against filed (19,627) and (147,754) — |computed| == |reported|, OPPOSITE SIGNS, on both.
      EXTENSION FOUND: the stripping is not confined to operating_income. `NetIncomeLoss` and
      `EarningsPerShareDiluted` are also stripped across every period checked, and the platform's
      MRCY metrics block contains NO negative value in any field of any period. Scope amendment
      proposed in §5.
  - da_id: "DA-26"
    chosen_reading: >
      MRCY is a DA-26 instance and is NOT in the published 19-issuer census. The full fiscal year
      (ended 2026-07-03, revenue 983,622k) sits in a metrics row labelled `fiscal_period: Q2`, and a
      Form 10-K is labelled `fiscal_period: Q2` in the filings block. The mislabelled period VARIES by
      issuer as registered; MRCY's value is `Q2`, a new value for the census table.
  - da_id: "DA-27"
    chosen_reading: >
      MRCY is a 5th DA-27 instance, and its early-July fiscal-year end is a NEW CLASS beyond
      PL/AVAV/WWD/HEI (Jan/Apr/Sep/Oct). The label tracks the CALENDAR quarter of the period end, not
      the issuer's fiscal quarter — verified on 8 consecutive period ends spanning FY2024-FY2026. MRCY
      sits exactly two fiscal quarters from its calendar label.
  - da_id: "DA-24"
    chosen_reading: >
      ASSET-SALE CONTAMINATION of `operating_income` — a gain on disposal flowing through the
      operating line, so the field measures a transaction rather than operations (register instance:
      EchoStar 2025 Q3, operating income 4.6x revenue). TESTED AT MRCY AND NOT PRESENT: the candidate
      event is the Plan-Les-Ouates (Geneva) manufacturing disposal to Cicor Group (2025-04-15), and
      no disposal gain is identified in the operating line for FY2025 or FY2026 — FY2025's operating
      line is a loss of (19,627) and p.38 note (2) ties the Cicor transaction to *acquisition costs*,
      not a gain. MRCY is **DA-24-clean**. The Cicor event is retained in this artifact for a
      DIFFERENT reason — cost and international-revenue comparability — and is labelled as such, not
      as a DA-24 finding.
  - da_id: "DA-14"
    chosen_reading: >
      radiation tolerance — rad-hard vs COTS modality. NOT RESOLVED by MRCY. The p.8 claim is
      "radiation-tolerant processing solutions"; no modality, no TID/SEU figure, no qualification
      standard, no part-level identification. The largest cost-curve ambiguity in orbital compute stays
      ambiguous on this name.
  - da_id: "DA-16"
    chosen_reading: >
      "Demonstrated" — flown once vs flown at cadence vs flown with disclosed economics vs audited;
      the rung decides whether a claim is `DEMONSTRATED` or `CLAIMED` under P4. APPLIED: MRCY's space
      narrative fails EVERY rung — it discloses no flight, no cadence, no economics and no audit for
      any radiation, thermal or space-qualification statement, anywhere in the 86-page filing or the
      5-page call. Every such claim is therefore graded `CLAIMED`, not by judgement but because it
      does not reach the first rung. The one space DATUM (platform revenue) is `DEMONSTRATED` — but it
      is a revenue disaggregation, not a capability disclosure, so it demonstrates nothing about the
      technology.
  - da_id: "DA-15"
    chosen_reading: >
      Thermal rejection temperature — peak vs average; with or without an assumed heat pump. THE
      AMBIGUITY THIS PHASE MUST RESOLVE. Radiated power scales as T^4, so a 50 K assumption change
      moves radiator area by ~1.9x, and the "with or without an assumed heat pump" branch is exactly
      the second F2 constant this phase is trying to source (the COP at elevated rejection
      temperature). MRCY does not resolve either branch: it discloses no rejection temperature, no
      peak/average basis, and no heat pump. Recorded as the definition governing the UNRESOLVABLE
      finding rather than as a sourced reading.
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
f2_constants_from_this_leg: "NONE — both F2 constants (radiator areal density, heat-pump COP) are absent from MRCY's disclosure"
f2_falsifier_from_this_leg: "FIRES — no band is sourced, so the ±50% threshold is met by construction"
citations:
  - figure: "Consolidated statements of operations, three fiscal years — net revenues 983,622 / 912,020 / 835,275; cost of revenues 702,457 / 657,526 / 639,374; gross margin 281,165 / 254,494 / 195,901; SG&A 175,031 / 154,412 / 166,786; R&D 59,736 / 67,647 / 101,328; total operating expenses 280,885 / 274,121 / 343,655; income (loss) from operations 280 / (19,627) / (147,754); net loss (29,673) / (37,904) / (137,640); diluted net loss per share (0.50) / (0.65) / (2.38); weighted-average diluted shares 59,460 / 58,746 / 57,738"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 47
    url: https://agentii.ai/v/MRCY/sec205/47
    located_via: read_source_pages
  - figure: "MD&A results-of-operations table (component identity source), incl. 'Income (loss) from operations | 280 | — | (19,627) | (2.1)' and the FY-basis revenue sentence 'increased $71.6 million, or 7.9%, to $983.6 million during fiscal 2026'; 53-week vs 52-week basis; Space platform revenue +$22.0M; 'an integrated space program' among the four largest program increases; 'no programs comprising 10% or more of our revenues'; Cicor five-year exclusive contract-manufacturing agreement (2025-04-15) and Star Lab asset acquisition (2025-04-30)"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 32
    url: https://agentii.ai/v/MRCY/sec205/32
    located_via: read_source_pages
  - figure: "Gross-margin driver verbatim — 'primarily driven by lower manufacturing variances of $15.8 million, partially offset by higher scrap, inventory reserves, and warranty provisions of $3.8 million, $2.3 million, and $1.1 million'; EAC changes-in-estimates table: gross favorable 28,847, gross unfavorable (47,589), net impact (18,742) vs (21,070) prior year; R&D 'decreased $7.9 million, or 11.7% ... savings from headcount reductions of approximately 270 employees'; SG&A +$20.6M / +13.4% 'of which $10.5 million was related to stock compensation'; restructuring ~100 positions"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 33
    url: https://agentii.ai/v/MRCY/sec205/33
    located_via: read_source_pages
  - figure: "Fiscal period definitions — 'fiscal 2026 are to the 53-week period from June 28, 2025 to July 3, 2026'; FY2026 revenue $983.6M, net loss $(29.7)M, diluted loss per share $(0.50), adjusted EPS $1.06, adjusted EBITDA $150.2M; FY2025 $912.0M, $(37.9)M, $(0.65), $0.64, $119.4M"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 3
    url: https://agentii.ai/v/MRCY/sec205/3
    located_via: read_source_pages
  - figure: "Revenue disaggregation by platform (fiscal 2026 / 2025 / 2024), incl. Space 78,021 / 55,972 / 60,546, and footnote (4) 'Space platform includes products that relate to personnel, equipment or pieces of equipment designed for space operations'"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 77
    url: https://agentii.ai/v/MRCY/sec205/77
    located_via: read_source_pages
  - figure: "R&D expenditures $59.7M / $67.6M / $101.3M; 518 employees engaged in engineering, research and product development; manufacturing footprint and certifications"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 9
    url: https://agentii.ai/v/MRCY/sec205/9
    located_via: read_source_pages
  - figure: "Space Domain Growth and Strategic Investment — 'The proliferation of low Earth orbit constellations requires ruggedized, radiation-tolerant processing solutions'; 'Space-qualified processing technologies will be required to address this growing segment of our addressable market' (CLAIMED, no figure)"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 8
    url: https://agentii.ai/v/MRCY/sec205/8
    located_via: read_source_pages
  - figure: "Thermal claim verbatim — 'Advanced thermal management and rugged packaging technology ensures optimal performance and reliable operation in the most challenging environments on Earth and beyond' — the ONLY thermal statement in the filing, with no magnitude of any kind"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 4
    url: https://agentii.ai/v/MRCY/sec205/4
    located_via: read_source_pages
  - figure: "Thermal hardware is PURCHASED, not made — 'certain components, including custom designed ASICs, static random access memory, FPGAs, microprocessors and other third party chassis peripherals (single board computers, power supplies, blowers, etc.), are currently available only from a single source or from limited sources'"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 10
    url: https://agentii.ai/v/MRCY/sec205/10
    located_via: read_source_pages
  - figure: "Single operating and reportable segment — 'the CODM continues to evaluate and manage the Company on the basis of one operating and reportable segment'"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 75
    url: https://agentii.ai/v/MRCY/sec205/75
    located_via: read_source_pages
  - figure: "Structural price-taker evidence — government/foreign-government programs 'approximately 97%, 97% and 95% of our total net revenues', 'primarily as a subcontractor or team member with defense prime contractors'; scaling risk incl. 'our contract manufacturers such as Cicor in Europe'"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 13
    url: https://agentii.ai/v/MRCY/sec205/13
    located_via: read_source_pages
  - figure: "FFP pricing rigidity verbatim — 'supply chain, combined with our inability to adjust FFP contract pricing'; tariff exposure 'Our gross margins could be reduced, potentially significantly, if we cannot pass these costs to customers'; international revenue 2% of total in FY2026 vs 5% in FY2025 and FY2024; Cicor transitioning legacy Geneva manufacturing to Switzerland and the UK during fiscal 2027"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 16
    url: https://agentii.ai/v/MRCY/sec205/16
    located_via: read_source_pages
  - figure: "Adjusted EBITDA reconciliation (competing basis to the GAAP operating line) — net loss (29,673) / (37,904) / (137,640); depreciation 33,779; amortization 38,904; restructuring 5,939; litigation and settlement 13,451; stock-based and other non-cash compensation 57,144; adjusted EBITDA 150,192 / 119,438 / 9,413. Bridge closes to the dollar."
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 38
    url: https://agentii.ai/v/MRCY/sec205/38
    located_via: read_source_pages
  - figure: "Segment note is a single segment; stock-based compensation expense before tax 41,132 / 25,019 / 25,669 (COMPETING BASIS to p.38's 57,144 / 38,273 / 41,257 'stock-based and other non-cash compensation')"
    ticker: MRCY
    form_type: 10-K
    citation_id: sec205
    page_no: 75
    url: https://agentii.ai/v/MRCY/sec205/75
    located_via: read_source_pages
  - figure: "FY2027 guidance and demand claims — 'increasing targeted organic revenue growth to low double digits while maintaining targeted adjusted EBITDA margin in the low to mid-20s'; 'For FY 2027, we expect revenue growth approaching double digits year over year with total revenue approaching $1.1 billion ... adjusted EBITDA approaching $200 million'; 'space and missile defense' named among production award areas"
    ticker: MRCY
    form_type: earnings_call_transcript
    citation_id: ect70
    page_no: 1
    url: https://agentii.ai/v/MRCY/ect70/1
    located_via: read_source_pages
  - figure: "Call restatement of the filing basis — 'Fiscal 26 revenues were 984 million up approximately $72 million or 7.9%'; 'Gross margin was 28.6% for fiscal 26, an increase of approximately 70 basis points from the 27.9%'; adjusted EBITDA $150M / 15.3% margin; free cash flow $68M; net debt $227M"
    ticker: MRCY
    form_type: earnings_call_transcript
    citation_id: ect70
    page_no: 2
    url: https://agentii.ai/v/MRCY/ect70/2
    located_via: read_source_pages
  - figure: "Backlog-margin mechanism and unreceived tailwinds — 'burning down lower margin backlog and margins increasing as we move our way through the year'; 'areas like CPA, effectors, munitions, space, missile defense, none of that is reflected in our outlook'"
    ticker: MRCY
    form_type: earnings_call_transcript
    citation_id: ect70
    page_no: 3
    url: https://agentii.ai/v/MRCY/ect70/3
    located_via: read_source_pages
  - figure: "No product-level margin disclosure — 'we do not talk about the margin profile of any of our products'; the only higher-margin niche located is memory security, not radiation — 'that part of our business tends to run at the higher end of our margin profile'"
    ticker: MRCY
    form_type: earnings_call_transcript
    citation_id: ect70
    page_no: 4
    url: https://agentii.ai/v/MRCY/ect70/4
    located_via: read_source_pages
  - figure: "Multiyear munitions frameworks 'are still potential tailwinds ... it is in our pipeline but yet to materialize in bookings'"
    ticker: MRCY
    form_type: earnings_call_transcript
    citation_id: ect70
    page_no: 5
    url: https://agentii.ai/v/MRCY/ect70/5
    located_via: read_source_pages
---

# MRCY — Is Radiation Tolerance a Scarce Input? And the Two F2 Constants

**Sources.** Form 10-K, accession `0001049521-26-000045`, fiscal year ended 2026-07-03, filed
2026-08-18, 86 pages (`sec205`); Q4 FY2026 earnings call, 2026-08-18, 5 pages (`ect70`).
Both enumerated in full.

**Why MRCY is the negative control.** Constitution Tier 3 lists it as *"radiation-tolerant
processing electronics — direct P2 evidence."* 001 found it earning a **0.03% operating
margin — $0.280M on $983.6M** — and read that as *"either the demand has not arrived, or
radiation tolerance is **not a scarce input** the way F2's thermal area is."*
**The job here was to settle which.** It settles, and the settlement survives — but 001's
evidence for it was itself corrupted, so the conclusion had to be re-derived from clean data.

---

## 1. The instrument first: DA-23 on the exact figure 001 quoted

001's `data_integrity_register_applied` reading was *"operating_income verified against
components; MRCY clean (components reconcile exactly)."* That is **true of FY2026 and false of
the comparator 001 used.** The component identity is mandatory here, so it is shown in full.

### 1.1 The identity, in-line, on three fiscal years

Basis: filed numbers, `sec205` p.47 (Consolidated Statements of Operations) cross-read against
p.32 (MD&A results table). Both are `DEMONSTRATED`.

| Fiscal year | Gross profit | − Total opex | = Computed | Filed `Income (loss) from operations` | Closes? |
|---|---|---|---|---|---|
| **FY2026** (53wk, 2026-07-03) | 281,165 | 280,885 | **280** | **280** | ✅ |
| **FY2025** (52wk, 2025-06-27) | 254,494 | 274,121 | **−19,627** | **(19,627)** | ✅ |
| **FY2024** (52wk, 2024-06-28) | 195,901 | 343,655 | **−147,754** | **(147,754)** | ✅ |

Every year closes **to the dollar, in both directions.** The identity is fully available on this
issuer — no need for the weaker gross-profit bound.

### 1.2 The instrument pair — `computed` vs `reported`, and nothing else

`validate_calculation(0001049521-26-000045)`, `us-gaap:OperatingIncomeLoss`, period 2026-07-03:

```
computed = 280,000     reported = 280,000     →  equal magnitude, SAME sign  →  NOT a hit
```

Per the standing instrument rule the `status` column is **not read**. The pair is what governs.

`validate_calculation(0001049521-25-000024)` (FY2025 10-K) returned **no `OperatingIncomeLoss`
row at all**, so the FY2025 pair cannot be obtained from that instrument. Worked around by pairing
the platform fact against the read-verified filed value — which satisfies the stated DA-23 test
directly.

### 1.3 The hit is on the COMPARATORS

`search_xbrl_facts(MRCY, OperatingIncomeLoss)`, annual periods, against the filed values above:

| Period | Platform value | Filed value | Test `|computed| == |reported|`, opposite signs | Verdict |
|---|---|---|---|---|
| FY2026 (2025-06-28 → 2026-07-03) | **+280,000** | 280 | magnitudes equal, **same sign** | **CLEAN** |
| FY2025 (2024-06-29 → 2025-06-27) | **+19,627,000** | **(19,627)** | equal, **OPPOSITE** | **DA-23 HIT** |
| FY2024 (2023-07-01 → 2024-06-28) | **+147,754,000** | **(147,754)** | equal, **OPPOSITE** | **DA-23 HIT** |

**All competing bases are reported, none collapsed** (§1c). For FY2025 operating income there are
three, and one dissents:

- **Basis A — filed:** `(19,627)` at `sec205` p.32 *and* p.47. Two independent venues, same value.
- **Basis B — component identity:** 254,494 − 274,121 = **−19,627**. Independent of Basis A's text.
- **Basis C — platform:** **+19,627,000**. Dissents in sign, agrees in magnitude.

Basis C is the hit. Basis A and Basis B agree with each other and were produced by different
methods, which is what makes the dissent diagnosable rather than ambiguous.

**Two further platform fields do not close and are recorded as such, not used:**
`us-gaap:GrossProfit` for 2026-07-03 returns `computed = −513,638,000` against `reported =
281,165,000` — an arc-selection artefact (the aggregation role mixes signs across subtotals); it
**does not touch the `OperatingIncomeLoss` closure** and supports no sign claim either way.
`us-gaap:NetIncomeLoss` returns `computed = 28,105,000` against `reported = 29,673,000` —
magnitudes **differ** by 1,568k, so no sign claim is admissible from that pair. Reported, not used.

### 1.4 ⚠️ Register-scope amendment: the stripping is NOT confined to `operating_income`

This is the finding I did not expect and it is the most consequential thing in this artifact.

MRCY's metrics block (`get_company_financials`) contains **no negative value in any field of any
period** — ten periods × ten fields, all non-negative. The filing, in the same periods, contains
negative numbers in at least seven distinct line items. Confirmed stripping:

| Field | Period | Platform | Filed | Verdict |
|---|---|---|---|---|
| `operating_income` | FY2026 | 280,000 | 280 | clean |
| `operating_income` | FY2025 | 19,627,000 | (19,627) | **stripped** |
| `operating_income` | FY2024 | 147,754,000 | (147,754) | **stripped** |
| `net_income_loss` | FY2026 | 29,673,000 | (29,673) | **stripped** |
| `net_income_loss` | FY2025 | 37,904,000 | (37,904) | **stripped** |
| `net_income_loss` | FY2024 | 137,640,000 | (137,640) | **stripped** |
| `eps_diluted` | FY2026 | 0.5 | (0.50) | **stripped** |
| `eps_diluted` | FY2025 | 0.65 | (0.65) | **stripped** |
| `eps_diluted` | FY2024 | 2.38 | (2.38) | **stripped** |

Filed values verified at `sec205` p.47 (all three years) and independently at p.3 (FY2026 and
FY2025 narrative) and p.38 (net loss, all three years, inside the adjusted-EBITDA reconciliation).

**Two consequences, and the second one is the important one.**

**(a) DA-23's name is too narrow.** The register entry is scoped to `operating_income`. On this
issuer the same mechanism strips `NetIncomeLoss` and `EarningsPerShareDiluted`, and it appears to
strip *every* loss-type fact on the statement. I propose the entry be restated as **sign stripping
on loss-type facts**, with `operating_income` retained as the most damaging instance. I am
recording this rather than editing the constitution.

**(b) It is a second, stronger reason why `EPS × shares` is inadmissible.** The contract already
excludes it because it passes on both sides of a flip. On MRCY the exclusion is not a matter of
principle — **the platform's own EPS field is itself sign-stripped.** An `EPS × shares` detector
here would have returned a *positive* diluted EPS of $0.50 against a filed loss of $(0.50) and
confirmed the inversion instead of catching it. A detector built on a contaminated input does not
degrade gracefully; it inverts.

### 1.5 ⚠️ 001's `−98.6%` is arithmetically obtainable ONLY from the flipped comparator

This is a proof, not an inference.

- Filed basis: 280 − (−19,627) = **+19,907 favourable swing**. The percent change is
  **undefined** — the sign crosses from loss to profit, so no percentage exists.
- 001's figure: (280 − 19,627) / 19,627 = −19,347 / 19,627 = **−98.57% → "−98.6%"** ✅

The numerator `19,347` equals `19,627 − 280`, and the denominator is `+19,627`. Both require the
comparator to be **positive**. With the filed comparator the denominator is negative and the
operation is undefined. **001's −98.6% therefore cannot have been produced from the filing. It can
only have been produced from the DA-23-stripped platform value.** The artifact did not compute a
wrong number; it *consumed* a wrong number.

The same holds for the margin row: 001 reported the comparator as `2.2%` (= 19,627 / 912,020), where
the filing prints **(2.1)** at `sec205` p.32. And 001's *"−2.1 pts"* should read **+2.18 points of
improvement** — `+0.03% − (−2.15%)`.

### 1.6 Why the constitution's clean verdict is not wrong, only incomplete

The constitution states: *"MRCY is DA-23-clean with an operating income of $0.280M on $983.6M of
revenue (0.03% margin). A sign error there would be invisible by inspection — the magnitude is
plausible either way."*

**That sentence is correct as to the period it names.** FY2026 is genuinely clean, and clean by the
strongest available test: the identity closes to the dollar, the instrument pair agrees at
280,000/280,000 same-sign, and the metrics block agrees. 001's own edge-case reasoning — that the
component identity, not magnitude plausibility, is the discriminator — is also correct and is
borne out here.

**It is incomplete because it certifies one period and the artifact consumed two.** 001's table has
six rows and quotes two fiscal years; the clean test was applied to one of them. The generalisable
rule this artifact contributes:

> **A single-period clean verdict does not certify a two-period comparison.** DA-23 screening must
> be run on *every period an artifact quotes*, not on the headline period.

That is the mechanism by which a correct register entry produced a corrupt artifact — and it will
have hit every other artifact in this program that quoted a multi-period table and trusted the
headline clean verdict. **This is the highest-value carry-forward in this artifact.**

---

## 2. The 28.6% gross margin against the 28.6% opex ratio

001 put this pairing correctly and it survives re-derivation. What it lacks is the *driver* — and
the driver is where the rent question is actually answered.

| | FY2026 | FY2025 | FY2024 |
|---|---|---|---|
| Gross margin % | **28.6%** | 27.9% | 23.5% |
| Opex ratio % | **28.6%** | 30.0% | 41.1% |
| **Operating margin %** | **+0.03%** | **(2.15%)** | **(17.7%)** |
| R&D % of revenue | **6.1%** (filed) | 7.4% (filed) | 12.1% (derived) |
| SG&A % of revenue | 17.8% | 16.9% | 20.0% |

The coincidence at 28.6% / 28.6% is exact enough to be worth stating as a fact about this issuer:
**MRCY converts its entire gross profit into operating expense.** Operating income is $280
thousand — the residual after $280,885 thousand of opex against $281,165 thousand of gross profit.

### 2.1 ⚠️ The margin improvement is cost-driven, not price-driven — and it is 70bp of variance, not pricing

`sec205` p.33, verbatim: the higher gross margin *"was primarily driven by **lower manufacturing
variances of $15.8 million**, partially offset by higher scrap, inventory reserves, and warranty
provisions of $3.8 million, $2.3 million, and $1.1 million, respectively. The increase was also
driven by net EAC change impact on our programs recognized over time of $18.7 million recorded in
the period, an incremental improvement of approximately $2.3 million, or 40 basis points, when
compared to the prior period."*

**Not one dollar of the 70bp improvement is price.** It is factory execution ($15.8M) plus a
*smaller* drag from revised program estimates ($2.3M less bad). A supplier of a scarce input reports
price. This one reports variance.

### 2.2 The EAC table is the sharpest single instrument in this artifact

`sec205` p.33, changes-in-estimates table (in thousands):

| | July 3, 2026 | June 27, 2025 |
|---|---|---|
| Gross favourable | 28,847 | 26,642 |
| Gross unfavourable | **(47,589)** | (47,712) |
| **Net impact** | **$(18,742)** | $(21,070) |

MRCY is booking **$47.6M of unfavourable estimate revisions against $28.8M favourable**, two years
running — a structurally negative skew of roughly 1.65:1. **A supplier pricing a scarce input does
not repeatedly discover that its programmes cost more than it estimated.** This is a company whose
contract economics are set by customers and by programme risk, not by scarcity. It is a rent test
with a numeric answer, and the answer is no.

### 2.3 Competing basis — adjusted EBITDA, reported in full (§1c)

An artifact that stopped at "0.03% margin" would be collapsing bases. The company's own non-GAAP
view is materially different, so it is reported:

| | FY2026 | FY2025 | FY2024 |
|---|---|---|---|
| Net loss | (29,673) | (37,904) | (137,640) |
| Other non-operating adjustments, net | 2,963 | (7,742) | (592) |
| Interest expense, net | 21,867 | 29,823 | 33,816 |
| Income tax provision (benefit) | 784 | (12,520) | (51,635) |
| Depreciation | 33,779 | 39,178 | 40,369 |
| Amortization of intangible assets | 38,904 | 42,849 | 47,661 |
| Restructuring and other charges | 5,939 | 7,216 | 26,170 |
| Acquisition, financing and other third party costs | 4,509 | 6,638 | 4,370 |
| Fair value adjustments from purchase accounting | 525 | 617 | 710 |
| Litigation and settlement expense, net | 13,451 | 13,010 | 4,927 |
| Stock-based and other non-cash compensation expense | 57,144 | 38,273 | 41,257 |
| **Adjusted EBITDA** | **150,192** | **119,438** | **9,413** |

The bridge closes to the dollar (`sec205` p.38). **Adjusted EBITDA margin = 150,192 / 983,622 =
15.3%**, matching the call's figure, against a GAAP operating margin of 0.03%. Free cash flow was
$68M = 6.9% of revenue.

**How to weigh the two bases.** The gap is $149.9M, and it is composed almost entirely of
**D&A ($72.7M) and non-cash compensation ($57.1M)** — 87% of the bridge. So the correct statement
is not "MRCY earns nothing"; it is **"MRCY earns nothing after the cost of the acquisitions that
built it and the stock it pays its people with."** Both readings are true and they imply different
things:

- On **cash-generation** grounds MRCY is a real, improving business: 15.3% adjusted EBITDA, +25.7%
  y/y, on target for "low to mid-20s."
- On **rent-capture** grounds the answer is unchanged and is *strengthened*: a 15.3% adjusted
  EBITDA margin is a **normal defense-electronics level, not a scarcity premium** — and the fact
  that $57.1M (5.8% of revenue) is paid as non-cash compensation to hold the workforce is the
  opposite of a moat. A firm that owns a scarce input prices the input; it does not need to pay
  retention equity worth 5.8% of revenue to keep the people who make it.
- `sec205` p.33 confirms the direction: SG&A rose 13.4% *"primarily driven by higher compensation
  expense of $20.5 million, of which $10.5 million was related to stock compensation."*

**⚠️ Competing basis inside the competing basis.** `sec205` p.75 gives stock-based compensation
**before tax** as **41,132 / 25,019 / 25,669**, while p.38 gives *"stock-based and other non-cash
compensation expense"* as **57,144 / 38,273 / 41,257** — a $16.0M difference in FY2026. The two
figures are not the same concept and neither is wrong; both are reported and neither is substituted
for the other.

---

## 3. PIL-2's question: is radiation tolerance a scarce input?

**Answer: no — and the reason is structural, not cyclical, so it does not resolve when demand
arrives.** 001's conclusion survives. Its reasoning does not; it is replaced below.

### 3.1 MRCY describes itself as a price-taker in its own risk factors

This is the decisive evidence and 001 did not use it.

- **97% / 97% / 95%** of total net revenues, FY2026 / FY2025 / FY2024, come from U.S. and foreign
  government programmes, *"primarily as a subcontractor or team member with defense prime
  contractors"* (`sec205` p.13). **MRCY is sub-tier. The prime holds the customer.** Scarcity rent
  accrues where the customer relationship sits, and MRCY states plainly that it does not sit there.
- *"supply chain, combined with our **inability to adjust FFP contract pricing**, could materially
  and adversely affect our business"* (`sec205` p.16). Fixed-price contracts. A supplier of a scarce
  input treats cost pass-through as a **lever**; MRCY files it as a **risk**.
- *"Our gross margins could be reduced, potentially significantly, if we **cannot pass these costs
  to customers**"* (`sec205` p.16), on tariffs. Same posture, different input.
- *"There were **no programs comprising 10% or more of our revenues** for fiscal 2026 or 2025"*
  (`sec205` p.32). No programme concentration in either direction — nothing to hold to ransom, and
  nothing to rent from.

A company with all four of those characteristics cannot capture scarcity rent even if the input it
supplies *is* scarce. Its contracts are structured so that the surplus goes elsewhere. **That is why
"the demand has not arrived" is the wrong branch of 001's dichotomy: the demand can arrive in full
and this P&L shape does not change, because the pricing mechanism does not pass scarcity through.**

### 3.2 ⚠️ The rent question is not merely unanswered — it is *unanswerable* from this issuer

- MRCY reports **one operating and reportable segment** (`sec205` p.75).
- The CFO, on the call: *"we do not talk about the margin profile of any of our products"*
  (`ect70` p.4).

So there is **no product-level or capability-level margin to inspect, by design.** "Does MRCY earn
rent on radiation-tolerant parts?" is not a question MRCY's disclosure can answer at any level of
effort. This is `UNRESOLVABLE-FROM-PUBLIC-SOURCES`, and it is a **different** unresolvable from the
F2 constants in §4: here the disclosure *exists as a business* but the metric is withheld; there the
physical constant is simply absent.

### 3.3 The only higher-margin niche MRCY locates is not radiation

Asked about a multiyear memory-securing agreement, the CEO: *"that part of our business tends to run
at the **higher end of our margin profile**"* (`ect70` p.4). And the sole-provider claim MRCY makes
is *"we have been the **only provider of the CPA technology in the security apparatus**"*
(`ect70` p.4) — **CPA ruggedized servers, in security, not rad-hard parts.**

**The one place in the entire record where MRCY claims a defensible position, it names the wrong
capability.** If radiation tolerance were the scarce input, this is where it would be named. It
isn't.

### 3.4 The quantitative statement of "no rent"

Space platform revenue grew **+$22.0M** (`sec205` p.32, cross-checked: 78,021 − 55,972 = 22,049 at
p.77 — a second component identity, and it closes). Consolidated operating income for the same year
is **+$0.280M**.

**A 39% increase in the gate-adjacent revenue line moved consolidated operating income by a quarter
of a million dollars.** That is the finding in one sentence. Stated carefully — this is descriptive,
not causal: the tiny margin is caused by opex absorbing gross profit, not by the space line; but the
space line is growing *inside* a P&L that earns nothing at the operating line, and it is not
changing that.

---

## 4. ⚠️ PIL-2's two physical constants: `UNRESOLVABLE-FROM-PUBLIC-SOURCES`

The phase's question is to source two constants: the **radiator areal density** (001 used
**8 kg/m² as an admitted placeholder**) and the **heat-pump COP at elevated rejection
temperature**. No skill here is a literature review, and an `UNRESOLVABLE` finding is a legitimate
output. **I am not padding a thin answer into a confident one. Neither constant is present in
MRCY's disclosure, and this artifact does not supply a value for either.**

### 4.1 Search record — the exact terms, so the negative claim is auditable

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
| `thermal management` | 1 hit (p.4) | not run | **CLAIMED, no magnitude** — quoted below |
| `thermal` | 2 hits (pp. 4, 8) | 0 | both read in full; neither carries a number |
| `radiation` | 1 hit (p.8) | 0 | qualitative capability claim |
| `radiation hardened` | 0 | not run | absent |

**⚠️ The `radiator` hit is a false positive and must not be counted as a disclosure.** It resolves
to `sec205` p.8, which I read in full: the page contains *"**radiation**-tolerant processing
solutions"* and *"thermal extremes from arctic to desert operations."* There is **no radiator** on
it. The keyword index is stemmed, so `radiator` matches `radiation`. Recording this explicitly
because **a naive read of that hit would have produced a fabricated F2 source** — the single worst
available outcome here.

**⚠️ Honest limit on the zero-hit rows.** `cooling` and `heat` returning zero in an 86-page
manufacturing disclosure that elsewhere mentions "blowers" is a sign the index is coarse, not proof
of absence. The `UNRESOLVABLE` finding therefore rests primarily on the **full outline sweep of both
documents** — every one of the 86 pages' descriptions enumerated, every page with product or
technology content (pp. 3–10) read in full — with the keyword record as corroboration. Stated as
"no disclosure located via these searches," not as an absolute.

### 4.2 What MRCY actually says about thermal — and why it is not a source

`sec205` p.4, the **only** thermal statement in the filing, verbatim:

> *"**Mission-Ready**: Fit for purpose to meet the demanding needs of our customers' missions.
> **Advanced thermal management and rugged packaging technology** ensures optimal performance and
> reliable operation in the most challenging environments **on Earth and beyond**. We deliver
> extended reliability and dependability through **thermal management, component selection,
> environmental protection and testing**."*

This is the closest thing in the record to an F2 supplier claim, and it is:
- **`CLAIMED`, not `DEMONSTRATED`** — no number of any kind: no W/m², no kg/m², no COP, no
  temperature, no material, no fluid, no loop, no pump.
- **about packaging, not about a thermodynamic cycle.** "Rugged packaging technology" is the noun.
  F2's constants describe a rejection loop — area, mass, and the work required to lift heat to the
  rejection temperature. MRCY describes neither.
- **"on Earth and beyond" is the entire space content of the claim** — three words, unquantified.

### 4.3 ⚠️ The decisive negative: MRCY *buys* its thermal hardware

`sec205` p.10, verbatim:

> *"certain components, including custom designed ASICs, static random access memory, FPGAs,
> microprocessors and other third party chassis peripherals (single board computers, power supplies,
> **blowers**, etc.), are currently available only from a single source or from limited sources."*

**"Blowers" is the only thermal-adjacent hardware noun in the entire 86-page filing**, and it
appears as a **purchased third-party chassis peripheral available from a single or limited
source.** MRCY does not manufacture thermal hardware. It **buys** it, from someone else, and lists
that dependency as a supply risk.

**This settles the F2 supplier question in the negative direction and it is a stronger result than
a bare absence.** An `UNRESOLVABLE` finding because a document is silent is weak. An `UNRESOLVABLE`
finding that also shows the issuer is a *customer* of the capability rather than a supplier of it is
structural: **MRCY cannot be an F2 evidence source at any point in the future without changing what
it manufactures.** Its thermal content is inbound, not outbound.

### 4.4 F4 (radiation) — `CLAIMED` with no mission-specific value

`sec205` p.8, verbatim:

> *"**Space Domain Growth and Strategic Investment.** Space represents a critical growth area for us
> with substantial Pentagon focus and investment. ... The proliferation of low Earth orbit
> constellations requires **ruggedized, radiation-tolerant processing solutions** that can operate
> reliably in the harsh space environment. ... **Space-qualified processing technologies will be
> required** to address this growing segment of our addressable market."*

This is a direct claim of positioning in the radiation-tolerant market and it is the disclosure 001
said does not exist. Graded **`CLAIMED` (DA-16)**: no TID figure, no SEU/SEFI rate, no orbit or
mission profile, no qualification standard (no MIL-STD-1540, no MIL-STD-883, no RHBD/RHBP), no
part-level identification, and no revenue attribution. **F4's mission-specific TID/SEU remains
unsourced from this issuer**, which is consistent with F4's own framing that the requirement is
mission-specific and must be sourced per mission profile.

### 4.5 Acceptance test — the falsifier FIRES on this leg

Spec §1b falsifier: `metric=f2_radiator_mass_per_MW_uncertainty_band_pct`, `threshold=0.50`,
`op=>`.

**MRCY supplies no band.** For either constant — and, as §4.3 shows, not because it is being coy:
it does not make the hardware class the constants describe. An absent value from a leg is not a
narrow uncertainty, and **the falsifier FIRES on the MRCY leg** either way.

MRCY is one of seven subscribed legs and the aggregate lives in `_cross/f2-constant-sourcing.md`,
which this artifact does not own. **That file has since closed, and its verdict supersedes any
conditional this leg could state:**

> **⚠️ NOTIFICATION — CONDITION DISCHARGED, NOT PENDING.** `_cross/f2-constant-sourcing.md` records
> **two independent acceptance-test breaches** and **F2 has downgraded to a qualitative bound.**
> **003 and 009 have already received written notification (appended 2026-09-18).**
> - **The band is WIDE, not merely absent** — the cross file sources radiator areal density at
>   **1.0–11 kg/m²** (±83% un-scoped, **±56% advanced-class**, ±35% crewed-class), so **two of three
>   scopes breach ±50% on their own.** *(⚠️ Inherited from the cross artifact; not independently
>   verified in this leg — this leg read MRCY, not the literature. Attributed, not asserted.)*
> - **The derivable COP axis alone spans +43% to +150%** by thermodynamics, needing no source.

**⚠️ This corrects a framing this leg would otherwise have carried.** "MRCY discloses no band" is
true of MRCY. It is **not** true of the platform: the constants are reachable, and they are **too
wide to support a point value** — a stronger and more useful verdict than "no data," because it
survives the constants being found. The MRCY leg's contribution is not that it supplies the
missing number; it is that it **removes a name from the supplier list** (§4.3).

**⚠️ Also inherited from the cross artifact, and it bears directly on 001's placeholder:** the
**8 kg/m² figure is a crewed/ISS-class value** (the 5.3–11 kg/m² band) applied to a
**mass-optimized uncrewed platform**, whose alternatives run **1.0–3.5 kg/m²** — a **2.7–5×
mismatch in F2's own favour.** F2's published area figures inherit it. *(Attributed to
`_cross/f2-constant-sourcing.md`; not verified in this leg.)*

The 8 kg/m² placeholder remains a **`MODELED`** value with no source. **Nothing in this artifact
upgrades it, and nothing here should be read as supporting it.**

---

## 5. What this artifact could NOT verify

| Item | Disposition | Class |
|---|---|---|
| Radiator areal density (kg/m²) | **Not disclosed by MRCY** in any form | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Heat-pump COP at elevated rejection temperature | **Not disclosed by MRCY** in any form | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Product- or capability-level margin (the rent test) | **Withheld by policy** — one segment (p.75); *"we do not talk about the margin profile of any of our products"* (ect70 p.4) | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Rad-hard vs COTS **modality** (DA-14) | **Not resolved.** p.8's claim is "radiation-tolerant," unqualified | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Mission-specific TID / SEU (F4) | **Not disclosed** — no figure, no standard, no mission profile | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| Space **margin** (as opposed to Space revenue) | Revenue is disclosed; margin is inside the single segment and not separable | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| FY2023 `OperatingIncomeLoss` DA-23 status | Platform returns **+21,685,000** (from `mrcy-20230630.htm`); the corresponding filed figure was **not read** and the FY2023 statement is not in `sec205` (three-year presentation). **Recorded as open; no claim made.** | `UNRESOLVABLE-FROM-PLATFORM` for the current corpus |
| `validate_calculation` FY2025 pair | Instrument returned **no `OperatingIncomeLoss` row** for `0001049521-25-000024` | `UNRESOLVABLE-FROM-PLATFORM` |
| ⚠️ **"Organic growth 7.9%"** | **Competing basis, flagged.** `sec205` p.32: *"There were 53 weeks and 52 weeks included in the results of operations for fiscal 2026 and fiscal 2025, respectively."* The +7.9% and the call's "FY 2026 **organic** revenue growth of 7.9%" (`ect70` p.1) are stated on a **53-vs-52-week basis**. The extra week's revenue contribution is **not quantified anywhere in either document**, and neither 001 nor the call flags it as a growth caveat. **The figure is correctly computed from the filed numbers; its comparability is unquantified.** | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` for the extra-week adjustment |

---

## 6. Corrections to 001 — frozen-001 policy applied

001's file is **not rewritten.** Corrections are recorded here and cross-cited, per policy.

| # | 001 says | Primary source shows | Status |
|---|---|---|---|
| 1 | *"Form 10-K, accession `0001049521-26-000045` (FY2026 **Q2**, period ended 2026-07-03)"* | It is the **FY2026 10-K for the full fiscal year** ended 2026-07-03 (53 weeks, p.3); $983.6M is **annual** revenue | **Corrected** |
| 2 | Table header *"Q2 FY2026 / Q2 FY2025"* | Both columns are **fiscal years**, not quarters (p.32, p.47) | **Corrected** |
| 3 | *"Operating income … $19.6M … **−98.6%**"* | Filed comparator is **$(19,627)k**; the true movement is **+$19,907k favourable**, margin **+2.18 pts**; −98.6% requires the stripped value (§1.5) | **Corrected** |
| 4 | Operating margin *"2.2% / −2.1 pts"* | Filed: **(2.1)** for FY2025; **+0.03%** FY2026, so **+2.18 points of improvement** | **Corrected** |
| 5 | *"MRCY is clean (components reconcile exactly)"* | **True for FY2026; false for both comparators.** DA-23 hits on FY2025 and FY2024 (§1.3) | **Corrected** |
| 6 | *"It discloses no space segment, no rad-hard revenue, and no orbital customer concentration"* | **Space platform revenue IS disclosed** — $78,021k / $55,972k / $60,546k (p.77), 7.9% of revenue, +39.4% y/y; an *"integrated space program"* is among the four largest program increases (p.32); p.8 carries a dedicated space growth-driver section naming radiation-tolerant processing | **Overturned** |
| 7 | *"MRCY cannot serve as evidence of the radiation-tolerance market because the market is inside a larger business it does not break out"* | **The conclusion stands; the premise does not.** Revenue *is* broken out; margin is not (one segment, p.75; no product margins, ect70 p.4). See §3.2 | **Reasoning replaced** |

**Note on #1 and the mechanism, which matters more than the error.** `get_company_financials`
returns the filing record itself as
`{accession: 0001049521-26-000045, document_type: 10-K, fiscal_year: 2026, fiscal_period: "Q2", period_end: 2026-07-03}`
— **a Form 10-K labelled `Q2`.** 001 did not misread the filing. It faithfully transcribed a
**platform period label** and inherited the label's defect. That is the same failure path as #3
(nothing computed wrong; a corrupt input consumed), and it means **the defect is systematic, not
author-specific** — any artifact reading `fiscal_period` off this platform for this issuer will
reproduce it.

### 6.1 Two new register candidates from this artifact

- **DA-26 — MRCY is an instance and was not in the census.** The annual FY2026 figure
  (revenue 983,622k) sits in a row labelled `fiscal_period: Q2`, as do the FY2025 and FY2024
  annuals. The mislabelled period **varies by issuer** as registered; **MRCY's value is `Q2`, a new
  value** for the census table.
- **DA-27 — MRCY is a 5th instance, n=5, in a new fiscal-year class.** Its early-July year-end is
  not among PL/AVAV/WWD/HEI (Jan/Apr/Sep/Oct). The registered mechanism is that the label derives
  from the **calendar** quarter of the period end rather than the issuer's fiscal quarter, and MRCY
  confirms it on 8 consecutive period ends:

  | Period end | MRCY fiscal quarter | Platform label |
  |---|---|---|
  | 2026-07-03 | FY2026 Q4 (and full FY2026) | `2026 Q2` |
  | 2026-03-27 | FY2026 Q3 | `2026 Q1` |
  | 2025-12-26 | FY2026 Q2 | `2025 Q4` |
  | 2025-09-26 | FY2026 Q1 | `2025 Q3` |
  | 2025-06-27 | FY2025 Q4 (and full FY2025) | `2025 Q2` |
  | 2025-03-28 | FY2025 Q3 | `2025 Q1` |
  | 2024-12-27 | FY2025 Q2 | `2024 Q4` |
  | 2024-09-27 | FY2025 Q1 | `2024 Q3` |

  Every label is the calendar quarter containing the period end; **no label is the fiscal quarter**,
  and the two annuals land on `Q2` because their June/early-July period ends fall in calendar Q2.
  MRCY sits **exactly two fiscal quarters** from its calendar label, which is what an early-July
  year-end must produce. **This is mechanism confirmation, not a new candidate** — but the July
  year-end class is new, and it is the first instance where the offset is large enough (+2) to be
  unmistakable from a single row.

### 6.2 Extension to record against DA-23

Restate the entry as **sign stripping on loss-type facts**, not sign stripping on `operating_income`.
Evidence in §1.4: `NetIncomeLoss` and `EarningsPerShareDiluted` are stripped on this issuer across
every period checked, and the metrics block carries no negative value anywhere. The consequence for
the program is concrete: **`EPS × shares` is inadmissible not only in principle but because the
platform's EPS field is itself contaminated on this issuer.**

---

## 7. Carry-forwards

1. **⚠️ `EPS × shares` is worse than inadmissible — it inverts.** §1.4 shows the platform's
   `eps_diluted` is sign-stripped on MRCY. Any detector built on it returns a *positive* EPS for a
   loss-making year and would **confirm** an inversion rather than catch it. The contract's
   exclusion should be restated with this reason attached.
2. **⚠️ Run DA-23 on every period an artifact quotes, not on the headline period.** §1.6. This is
   the mechanism that corrupted 001 with a correct register entry, and it is general across the
   program's multi-period tables. **Highest-value carry-forward here.**
3. **⚠️ Period labels from `get_company_financials` / the filings block do not identify fiscal
   periods on non-December year-ends** (§6.1). Any artifact quoting `fiscal_period` from the platform
   on such an issuer inherits DA-26/DA-27. A calendar-quarter cross-check should be mandatory.
4. **F2's falsifier FIRES on the MRCY leg, and the platform-level condition is DISCHARGED**
   (§4.5). `_cross/f2-constant-sourcing.md` records two independent acceptance-test breaches,
   **F2 has downgraded to a qualitative bound, and 003 and 009 have already been notified.** The
   band is **wide (±56% advanced-class)**, not absent — so the downgrade survives the constants
   being found. This leg adds only that **MRCY is not a supplier of them.**
5. **MRCY cannot be an F2 source at any horizon** (§4.3) — it *buys* its thermal hardware (blowers,
   single/limited source, p.10) and does not make it. Downgrade it in the F2 sourcing plan from
   "no disclosure found" to "structurally not a supplier," so no future phase re-queries it.
6. **The rent conclusion stands, on structural grounds** (§3.1): 97% government revenue as a
   sub-tier subcontractor on FFP contracts that MRCY itself describes as un-repricable. **This does
   not resolve when demand arrives**, so PIL-2 should stop hedging between "demand has not arrived"
   and "not a scarce input" — on this issuer it is the second, for reasons that are contractual.
7. **"Organic growth 7.9%" carries an unquantified 53rd-week benefit** (§5). Flag for 003/009 as a
   comparability caveat on MRCY's growth rate.
8. **001 correction #6 must propagate.** *"MRCY discloses no space segment"* is false and is cited
   in 001 §1 and §3. Space revenue is disclosed at p.77. The correction is recorded here; 001's file
   is frozen and not rewritten.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Consolidated statements of operations, three fiscal years — net revenues 983,622 / 912,020 / 835,275; cost of revenues 702,457 / 657,526 / 639,374; gr | [📄 MRCY 10-K p.47](https://agentii.ai/v/MRCY/sec205/47) **(newly surfaced)** |
| MD&A results-of-operations table (component identity source), incl. 'Income (loss) from operations | 280 | — | (19,627) | (2.1)' and the FY-basis reve | [📄 MRCY 10-K p.32](https://agentii.ai/v/MRCY/sec205/32) **(newly surfaced)** |
| Gross-margin driver verbatim — 'primarily driven by lower manufacturing variances of $15.8 million, partially offset by higher scrap, inventory reserv | [📄 MRCY 10-K p.33](https://agentii.ai/v/MRCY/sec205/33) **(newly surfaced)** |
| Fiscal period definitions — 'fiscal 2026 are to the 53-week period from June 28, 2025 to July 3, 2026'; FY2026 revenue $983.6M, net loss $(29.7)M, dil | [📄 MRCY 10-K p.3](https://agentii.ai/v/MRCY/sec205/3) **(newly surfaced)** |
| Revenue disaggregation by platform (fiscal 2026 / 2025 / 2024), incl. Space 78,021 / 55,972 / 60,546, and footnote (4) 'Space platform includes produc | [📄 MRCY 10-K p.77](https://agentii.ai/v/MRCY/sec205/77) **(newly surfaced)** |
| R&D expenditures $59.7M / $67.6M / $101.3M; 518 employees engaged in engineering, research and product development; manufacturing footprint and certif | [📄 MRCY 10-K p.9](https://agentii.ai/v/MRCY/sec205/9) **(newly surfaced)** |
| Space Domain Growth and Strategic Investment — 'The proliferation of low Earth orbit constellations requires ruggedized, radiation-tolerant processing | [📄 MRCY 10-K p.8](https://agentii.ai/v/MRCY/sec205/8) **(newly surfaced)** |
| Thermal claim verbatim — 'Advanced thermal management and rugged packaging technology ensures optimal performance and reliable operation in the most c | [📄 MRCY 10-K p.4](https://agentii.ai/v/MRCY/sec205/4) **(newly surfaced)** |
| Thermal hardware is PURCHASED, not made — 'certain components, including custom designed ASICs, static random access memory, FPGAs, microprocessors an | [📄 MRCY 10-K p.10](https://agentii.ai/v/MRCY/sec205/10) **(newly surfaced)** |
| Single operating and reportable segment — 'the CODM continues to evaluate and manage the Company on the basis of one operating and reportable segment' | [📄 MRCY 10-K p.75](https://agentii.ai/v/MRCY/sec205/75) **(newly surfaced)** |
| Structural price-taker evidence — government/foreign-government programs 'approximately 97%, 97% and 95% of our total net revenues', 'primarily as a s | [📄 MRCY 10-K p.13](https://agentii.ai/v/MRCY/sec205/13) **(newly surfaced)** |
| FFP pricing rigidity verbatim — 'supply chain, combined with our inability to adjust FFP contract pricing'; tariff exposure 'Our gross margins could b | [📄 MRCY 10-K p.16](https://agentii.ai/v/MRCY/sec205/16) **(newly surfaced)** |
| Adjusted EBITDA reconciliation (competing basis to the GAAP operating line) — net loss (29,673) / (37,904) / (137,640); depreciation 33,779; amortizat | [📄 MRCY 10-K p.38](https://agentii.ai/v/MRCY/sec205/38) **(newly surfaced)** |
| Segment note is a single segment; stock-based compensation expense before tax 41,132 / 25,019 / 25,669 (COMPETING BASIS to p.38's 57,144 / 38,273 / 41 | [📄 MRCY 10-K p.75](https://agentii.ai/v/MRCY/sec205/75) **(newly surfaced)** |
| FY2027 guidance and demand claims — 'increasing targeted organic revenue growth to low double digits while maintaining targeted adjusted EBITDA margin | [📄 MRCY earnings call transcript p.1](https://agentii.ai/v/MRCY/ect70/1) **(newly surfaced)** |
| Call restatement of the filing basis — 'Fiscal 26 revenues were 984 million up approximately $72 million or 7.9%'; 'Gross margin was 28.6% for fiscal  | [📄 MRCY earnings call transcript p.2](https://agentii.ai/v/MRCY/ect70/2) **(newly surfaced)** |
| Backlog-margin mechanism and unreceived tailwinds — 'burning down lower margin backlog and margins increasing as we move our way through the year'; 'a | [📄 MRCY earnings call transcript p.3](https://agentii.ai/v/MRCY/ect70/3) **(newly surfaced)** |
| No product-level margin disclosure — 'we do not talk about the margin profile of any of our products'; the only higher-margin niche located is memory  | [📄 MRCY earnings call transcript p.4](https://agentii.ai/v/MRCY/ect70/4) **(newly surfaced)** |
| Multiyear munitions frameworks 'are still potential tailwinds ... it is in our pipeline but yet to materialize in bookings' | [📄 MRCY earnings call transcript p.5](https://agentii.ai/v/MRCY/ect70/5) **(newly surfaced)** |
