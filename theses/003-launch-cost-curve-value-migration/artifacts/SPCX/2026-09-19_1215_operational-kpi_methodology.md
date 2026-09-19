---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: cross   # multi-pillar: {PIL-1, PIL-3} — 'cross' is the enum-valid value; check_contract does not validate this field, so a pillar SET passed silently. Stated in the body.
ticker: SPCX
skill: operational-kpi
mode: methodology
generated_at: 2026-09-19T12:15:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: "DA-07"
    chosen_reading: "Mass to orbit — filed definition taken as written: 'total kilograms of payload that we deploy to orbit in a given period', summed from 'all successful orbital and flight tests', excluding failed or scrubbed attempts, and reported as a TOTAL that includes internal payloads. Read as the filed three-row split (total / customer / internal), never as a single number. §1"
  - da_id: "DA-08"
    chosen_reading: "Launch counts — the filed basis set is THREE-way and never collapsed: Falcon-only (37 / 77), all-vehicles Falcon+Starship (38 / 78, derived, and the basis the call quotes), and customer-only (10 / 17, the filed demand basis). 'All Starship launches have been classified as internal' is taken as the boundary that makes the customer basis the demand basis. Every rate in this artifact names its basis; §3 shows two filed rates whose signs point in OPPOSITE directions on one quarter."
  - da_id: "DA-23"
    chosen_reading: "Sign strip on negative income facts — CONFIRMED at SPCX and quantified as a census, not a sample: 16 of the 20 served `us-gaap:OperatingIncomeLoss` facts carry a positive value against a filed negative. The four that survive are exactly the four whose filed sign is positive (Connectivity, every period) — which is what proves the defect is |x| absolute-value STRIPPING and not systematic inversion. Detector used is the component identity (revenue − total costs and expenses), run in-line at four levels. The GROSS-PROFIT BOUND is UNEXERCISED at SPCX, not CLEAN: the platform holds zero `us-gaap:GrossProfit` facts for SPCX and no statement files a gross-profit line. §7"
  - da_id: "DA-24"
    chosen_reading: "Non-operating contamination of `operating_income` — REFUTED at SPCX on both segment and consolidated lines. The non-operating items the filing actually names (interest expense, interest income, other income (expense) net, digital-asset marks, debt-extinguishment loss) are each filed BELOW loss from operations, and the segment table has no 'other income' row at all. The Space operating line is therefore uncontaminated. Recorded as REFUTED on the evidence, not as untested."
  - da_id: "DA-25"
    chosen_reading: "Normalised per-unit metric not reproducible from audited tables — CONFIRMED as a NULL at the Space layer and the operative limit on this whole artifact. SPCX files NO per-launch and NO per-kilogram series on any basis; the Space key business metrics are totals only. Every per-launch figure in §9 is therefore MODELED (our denominator choice), never filed, and can never satisfy a falsifier. The one cost-per-launch-like statement in the corpus is the issuer's forward-looking CLAIM of a '10x' launch-cost reduction — a ratio of targets with no filed basis and no denominator."
  - da_id: "DA-26"
    chosen_reading: "Annual figure mislabelled as quarterly — NOT TESTABLE at SPCX, recorded UNRESOLVED and NOT clean. Two independent blockers: (a) the platform's SPCX corpus is one 10-Q and eight 8-Ks with NO 10-K, so no annual row exists to be mislabelled; (b) `fiscal_period='Q4'` returns 0 facts. A probe of the label layer found the inverse-family defect — `fiscal_period='FY'` returns the same four HALF-YEAR and QUARTER durations as no filter at all, i.e. the FY label is not bound to a 12-month duration at SPCX — but that is not the registered DA-26 form and is not reported as DA-26 CONFIRMED. §8"
  - da_id: "DA-27"
    chosen_reading: "Fiscal-period labels derived from the calendar quarter — NOT TESTABLE as a defect at SPCX and NOT reported as clean. Every period in this artifact is read off the filing's own column header and cross-checked against `period_start` / `period_end`, never off a fiscal label. SPCX is a Dec-31 filer whose Q2 ends 2026-06-30, so label and calendar coincide and a label defect would be INVISIBLE here; the reader cannot distinguish 'correct' from 'correct by accident'. Sibling artifact 002 §7 found SPCX is correct-by-accident (source `default`), where GOOG's is actively wrong."
  - da_id: "DA-30"
    chosen_reading: "Two bases on one concept collapsed without a basis field — this is the DEFINING hazard of this artifact and the reason it exists. Three concepts in the Space series each carry competing bases that change the ANSWER, not just the presentation: launch counts (Falcon-only / all-vehicles / customer-only), revenue growth (+29.0% Q2 y/y vs −1.9% H1 y/y vs +55% sequential), and gross margin (Space segment 65.80% vs consolidated 55.27%). §3 and §9 carry every basis side by side and collapse to none."
  - da_id: "DA-21"
    chosen_reading: "SPCX's three-segment frame is a management-drawn boundary. Applied here only to the DENOMINATOR of the revenue-share ratios in §5: the 'Space share of consolidated revenue' is a ratio whose denominator is contaminated by the AI segment, which entered by common-control merger (xAI, 2026-02-02) and whose comparatives were recast. Reported on four denominators, never one."
evidence_grade: DEMONSTRATED
key_metrics:
  mass_to_orbit_q2_2026_3m_tonnes: 485
  mass_to_orbit_h1_2026_6m_tonnes: 1041
  space_segment_gross_margin_pct: 65.80
  consolidated_gross_margin_pct: 55.27
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM
citations:
  - figure: "SPCX sec8 p.36"
    ticker: SPCX
    citation_id: sec8
    page_no: 36
    url: https://agentii.ai/v/SPCX/sec8/36
    located_via: read_source_pages
  - figure: "SPCX ect1 p.3"
    ticker: SPCX
    citation_id: ect1
    page_no: 3
    url: https://agentii.ai/v/SPCX/ect1/3
    located_via: read_source_pages
  - figure: "SPCX sec8 p.35"
    ticker: SPCX
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "SPCX ect1 p.2"
    ticker: SPCX
    citation_id: ect1
    page_no: 2
    url: https://agentii.ai/v/SPCX/ect1/2
    located_via: read_source_pages
  - figure: "SPCX sec8 p.43"
    ticker: SPCX
    citation_id: sec8
    page_no: 43
    url: https://agentii.ai/v/SPCX/sec8/43
    located_via: read_source_pages
  - figure: "SPCX sec8 p.46"
    ticker: SPCX
    citation_id: sec8
    page_no: 46
    url: https://agentii.ai/v/SPCX/sec8/46
    located_via: read_source_pages
  - figure: "SPCX sec8 p.47"
    ticker: SPCX
    citation_id: sec8
    page_no: 47
    url: https://agentii.ai/v/SPCX/sec8/47
    located_via: read_source_pages
  - figure: "SPCX sec8 p.42"
    ticker: SPCX
    citation_id: sec8
    page_no: 42
    url: https://agentii.ai/v/SPCX/sec8/42
    located_via: read_source_pages
  - figure: "SPCX sec8 p.30"
    ticker: SPCX
    citation_id: sec8
    page_no: 30
    url: https://agentii.ai/v/SPCX/sec8/30
    located_via: read_source_pages
  - figure: "SPCX sec8 p.31"
    ticker: SPCX
    citation_id: sec8
    page_no: 31
    url: https://agentii.ai/v/SPCX/sec8/31
    located_via: read_source_pages
  - figure: "SPCX sec8 p.32"
    ticker: SPCX
    citation_id: sec8
    page_no: 32
    url: https://agentii.ai/v/SPCX/sec8/32
    located_via: read_source_pages
  - figure: "SPCX sec8 p.40"
    ticker: SPCX
    citation_id: sec8
    page_no: 40
    url: https://agentii.ai/v/SPCX/sec8/40
    located_via: read_source_pages
  - figure: "SPCX sec8 p.5"
    ticker: SPCX
    citation_id: sec8
    page_no: 5
    url: https://agentii.ai/v/SPCX/sec8/5
    located_via: read_source_pages
  - figure: "SPCX sec8 p.37"
    ticker: SPCX
    citation_id: sec8
    page_no: 37
    url: https://agentii.ai/v/SPCX/sec8/37
    located_via: read_source_pages
  - figure: "SPCX sec8 p.11"
    ticker: SPCX
    citation_id: sec8
    page_no: 11
    url: https://agentii.ai/v/SPCX/sec8/11
    located_via: read_source_pages
  - figure: "SPCX sec8 p.44"
    ticker: SPCX
    citation_id: sec8
    page_no: 44
    url: https://agentii.ai/v/SPCX/sec8/44
    located_via: read_source_pages
  - figure: "SPCX sec8 p.55"
    ticker: SPCX
    citation_id: sec8
    page_no: 55
    url: https://agentii.ai/v/SPCX/sec8/55
    located_via: read_source_pages
  - figure: "SPCX sec8 p.13"
    ticker: SPCX
    citation_id: sec8
    page_no: 13
    url: https://agentii.ai/v/SPCX/sec8/13
    located_via: read_source_pages
---

# SPCX — Operational KPI Methodology (Q2 2026, post-IPO)

**Primary PIL-1 (the cost curve and every basis it is measurable on), carrying PIL-3 (the
curve is CLAIMED, not DEMONSTRATED).**

Source: Form 10-Q, accession `0001628280-26-052535`, filed 2026-08-04, quarter ended
2026-06-30 (**`sec8` — the only SPCX 10-Q on the platform**, 55 pages), plus the Q2 2026
earnings call transcript (`ect1`, 2026-08-04, 6 pages).

---

## The finding

**SPCX files no `cost per launch` and no `revenue per launch` series on any basis. What it
files is a throughput series — mass to orbit and launch counts — and a segment table. The
two do not describe the same activity, and the boundary between them is stated by the
issuer in one sentence:**

> *"Our Space segment revenue only reflects our customer launches and customer
> activities."* — [📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36) · **DEMONSTRATED**

**In Q2 2026, 10 of 38 launches were customer launches — 26.3%. The other 28 (73.7%, "~74%")
produce no Space revenue by design**, because their payload is Starlink's own constellation
and the launch cost is capitalised into satellites rather than recognised as revenue
([📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36)). On the H1 basis the same ratio is
17 of 78 = **21.8%**, or **78.2% producing no Space revenue**.

**This single boundary governs everything downstream.** It means:

1. **The denominator is the whole argument.** Cost per launch moves **−10.3% or +20.7% in
   the same quarter on the same numerator**, purely by choosing customer launches or all
   launches. §9.
2. **The headline and the demand signal point in opposite directions, and both are the
   filing's.** Customer launches **+11.1%** while total launches **−17.4%**; Space revenue
   **+29.0%** in a quarter when launch activity **fell 17.4%**. §3.
3. **"12.3%" is not a launch share and not a stable level.** Launch-only is **8.29%**; on an
   ex-AI denominator it is **18.31%** (Q2) / **17.32%** (H1); the direction — Space's share
   is falling — survives every basis, and **the level survives none**. §5.
4. **The curve stays CLAIMED (PIL-3).** The corpus's only cost-per-launch-like statement is
   the issuer's forward target — *"Starship aims to quadruple payload capacity and reduce
   launch costs by 10x compared to our Falcon 9 rocket"* ([📄 SPCX Q2 2026 call
   p.3](https://agentii.ai/v/SPCX/ect1/3), **CLAIMED**) — a ratio of targets with no filed
   basis, no denominator, and no period. **There is one vehicle architecture in this corpus
   with a cost claim and none with a measured unit cost.**

---

## 0. What was settled, in one table

| # | Question | Answer | Grade |
|---|---|---|---|
| 1 | The filed throughput metrics, Q2 and H1, with prior-year comparatives | **ALL FIVE restatement figures reproduce — but on TWO different period bases, and the inherited list silently mixes them.** Four are Q2-only, one is H1-only. §1 | DEMONSTRATED |
| 2 | The customer/internal split | **THE finding. 10 of 38 = 26.3% (Q2); 17 of 78 = 21.8% (H1). ~74% / ~78% of launches produce no Space revenue BY DESIGN** — filed sentence, p.36 | DEMONSTRATED |
| 3 | Two opposite-signed rates on one activity | **Both filed, both correct: customer launches +11.1%, total launches −17.4%, Space revenue +29.0%. Quote only with the basis attached.** §3 | DEMONSTRATED |
| 4 | The segment table | **Space revenue $962M · cost of revenue $329M (−0.3% against +29.0% revenue) · gross margin 65.80% on the SEGMENT basis, which does NOT reproduce consolidated (55.27%) · operating result $(542)M · Starship R&D $1,076M = 111.9% of segment revenue.** All read from pages; `get_segment_data` is unusable. §4 | DEMONSTRATED |
| 5 | The `12.3%` correction | **Three things at once, and it is FOUR bases, not two: 12.3% (Q2, consolidated denominator) · 8.29% launch-only · 18.31% ex-AI Q2 · 18.32% prior-year Q2. Direction survives all four; level survives none.** §5 | DEMONSTRATED |
| 6 | Is `$(1,257)M` filed or derived? | **FILED — four separate times**, including as its own column in Note 18 and inside a reconciliation that closes exactly. §6 | DEMONSTRATED |
| 7 | DA-23 at SPCX | **CONFIRMED as a census: 16 of 20 served `OperatingIncomeLoss` facts are \|x\|-stripped; the 4 survivors are exactly the always-positive ones. The GROSS-PROFIT BOUND is UNEXERCISED, not CLEAN.** §7 | DEMONSTRATED |
| 8 | DA-26 at SPCX | **NOT TESTABLE — UNRESOLVED, not clean.** No annual row exists; `fiscal_period="Q4"` returns 0 facts. A probe found the inverse-family defect (`fiscal_period="FY"` returns H1/Q2 durations) but it is not the registered form. §8 | — |
| 9 | The per-launch series | **MODELED, and basis-unstable by 3.4× on revenue and SIGN-FLIPPING on cost.** §9 | MODELED |

---

## 1. The key business metrics, as filed, with period and basis

**Mode: methodology — the derivation path, stated so the number is reproducible.**

### 1.1 Mass to orbit — DA-07

Filed verbatim: *"Mass to orbit is the total kilograms of payload that we deploy to orbit in
a given period ... We calculate this metric by summing verified mass, including Starlink
satellites, customer payloads, and development cargo, from all successful orbital and flight
tests. This measure excludes failed or scrubbed attempts."*
([📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35)) · **DEMONSTRATED**

| Metric tons | Q2 2026 | Q2 2025 | **Δ (3M)** | H1 2026 | H1 2025 | **Δ (6M)** |
|---|---:|---:|---:|---:|---:|---:|
| **Mass to orbit** | 485 | 652 | **−25.6%** | 1,041 | 1,102 | **−5.5%** |
| of which customer payloads | 87 | 88 | −1.1% | 132 | 163 | **−19.0%** |
| of which internal payloads | 397 | 563 | −29.5% | 908 | 938 | −3.2% |

Arithmetic: **(485 − 652) ÷ 652 = −25.61%** ✓ reproduces the inherited **−25.6%**.
**(1,041 − 1,102) ÷ 1,102 = −5.54%**.

⚠️ **The inherited list quotes −25.6% as though it were the H1 figure beside four H1
companions. It is the 3M figure. On 6M the same series is −5.5%** — a 4.6× smaller
decline. The filing's own footnote also warns the components *"may not add up to the
corresponding totals due to rounding"*.

### 1.2 Launches — DA-08

Filed verbatim: *"Launches in a period represent the sum of all successful orbital and
flight tests across our rockets, including internal Starlink deployments, development tests,
and launches for our third-party customers, and excluding any cancellations or scrubs."*
A customer launch requires that *"an external customer payload constitutes the primary
payload"*; *"To date, all Starship launches have been classified as internal."*
([📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35)) · **DEMONSTRATED**

| Number | Q2 2026 | Q2 2025 | **Δ (3M)** | H1 2026 | H1 2025 | **Δ (6M)** |
|---|---:|---:|---:|---:|---:|---:|
| **Falcon launches** | 37 | 45 | **−17.8%** | 77 | 81 | **−4.9%** |
| of which customer launches | 10 | 9 | **+11.1%** | 17 | 21 | **−19.0%** |
| of which internal launches | 27 | 36 | **−25.0%** | 60 | 60 | 0.0% |
| **Starship launches** | 1 | 1 | 0.0% | **1** | **3** | **3 → 1** |

Arithmetic: (37 − 45) ÷ 45 = **−17.78%** ✓ · (10 − 9) ÷ 9 = **+11.11%** ✓ ·
(27 − 36) ÷ 36 = **−25.00%** ✓ · (17 − 21) ÷ 21 = **−19.05%** ✓ · Starship H1 3 → 1 ✓.

**All five inherited figures reproduce exactly.** The correction is not to any value — it is
that **they span two period bases and the inherited list does not say so.** Three are 3M
(−25.6%, −17.8%, −25.0%), one is explicitly 6M (−19.0%), and Starship's *"3 → 1"* is
**6M only** — on 3M Starship is **1 vs 1, flat**. A reader who takes the list as one vintage
would compute the Starship decline on a basis where it does not exist.

### 1.3 The derived all-vehicles basis

Falcon + Starship, **derived by addition on filed cells**:

| Number | Q2 2026 | Q2 2025 | **Δ** | H1 2026 | H1 2025 | **Δ** |
|---|---:|---:|---:|---:|---:|---:|
| **Total launches (all vehicles)** | **38** | **46** | **−17.4%** | **78** | **84** | **−7.1%** |

Arithmetic: (38 − 46) ÷ 46 = **−17.39%** ✓ reproduces the inherited **−17.4%**.
(78 − 84) ÷ 84 = −7.14%.

**Cross-confirmed by the call:** Shotwell — *"**78 total launches** and 1,041 tons of mass to
orbit delivered in the first half of this year"* ([📄 SPCX Q2 2026 call
p.2](https://agentii.ai/v/SPCX/ect1/2)) · **CLAIMED** (matches the derived 78 exactly, and
matches the filed 1,041 t).

**This basis is not filed as a row.** It is the sum of two filed rows, and it is the basis
the issuer speaks on. **Quoting it without saying "Falcon + Starship" is the DA-08 trap.**

---

## 2. The customer/internal split is THE finding

**The boundary is the customer boundary, and the issuer states it:**

> *"For launches of our Starlink satellites, the Company does not recognize any inter-segment
> revenue, rather those launch costs are capitalized in satellites in Property, plant, and
> equipment, net. ... **Our Space segment revenue only reflects our customer launches and
> customer activities.**"* — [📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36) ·
> **DEMONSTRATED**

| | Q2 2026 | H1 2026 |
|---|---:|---:|
| Customer launches | 10 | 17 |
| Total launches (all vehicles) | 38 | 78 |
| **Customer share of launches** | **26.3%** | **21.8%** |
| **Launches producing NO Space revenue, by design** | **28 = 73.7% (~74%)** | **61 = 78.2% (~78%)** |

Arithmetic: 10 ÷ 38 = **26.32%** ✓ · 17 ÷ 78 = **21.79%** ✓ · 28 ÷ 38 = **73.68%** ✓ ·
61 ÷ 78 = **78.21%**.

**Three consequences, each of which changes a number a reader would otherwise quote:**

1. **Space revenue per launch is undefined on the total-launch basis.** Dividing Space
   revenue by all launches divides a customer-only numerator by an all-customer+internal
   denominator. §9.
2. **The internal launches are not "unmonetised" — they are capitalised.** Their cost lands
   in Connectivity's depreciation, not in Space's cost of revenue. That is why Connectivity
   cost of revenue rose on *"higher depreciation of $226 million primarily from capitalized
   launch and satellite costs"* ([📄 SPCX 10-Q p.43](https://agentii.ai/v/SPCX/sec8/43)).
   **The Space segment's cost line is therefore not the cost of SPCX's launches** — it is the
   cost of its customer launches plus its development work.

   **The magnitude is visible in the non-GAAP reconciliation, and it is large:** consolidated
   depreciation and amortisation ran **$1,526M → $2,848M (+86.6%)** in Q2 and **$2,970M →
   $5,290M (+78.1%)** in H1, against revenue growth of 91.9% Q2 ([📄 SPCX 10-Q
   p.46](https://agentii.ai/v/SPCX/sec8/46), [📄 p.47](https://agentii.ai/v/SPCX/sec8/47)) ·
   **DEMONSTRATED**. Of the Q2 2026 $2,848M, **$1,885M sits in the AI segment and $805M in
   Connectivity** — the two segments that consume internal launch capacity — against
   **$158M in Space** ([📄 SPCX 10-Q p.46](https://agentii.ai/v/SPCX/sec8/46)). **The
   capitalised launch cost surfaces three segments away from the segment that performed the
   launch.** ⚠️ This is the single strongest corroboration of the boundary finding: it is
   also why a Space cost-per-launch ratio cannot be repaired by adding "the launch cost" back
   in — **that cost is not separately disclosed anywhere.**
3. **A launch-count decline is not a revenue decline here, and vice versa.** §3.

⚠️ **Correction inherited, not re-derived:** sibling artifact
`002/artifacts/SPCX/2026-09-18_1500_operational-kpi_methodology.md` §2 established that
**customer 10 ÷ 78 = 12.8%** is an *artefact of mixing bases* — filed customer launches over
a call-basis denominator. **It is a number that appears in neither document.** Carried
forward unchanged.

---

## 3. Two opposite-signed rates on one activity

**This is the artifact's central DA-30 case, and both rates are the filing's:**

| Rate | Value | Basis | Source |
|---|---:|---|---|
| **Customer launches** | **+11.1%** | Q2 2026 vs Q2 2025, 3M | [📄 p.35](https://agentii.ai/v/SPCX/sec8/35) |
| **Total launches (all vehicles)** | **−17.4%** | Q2 2026 vs Q2 2025, 3M | derived, [📄 p.35](https://agentii.ai/v/SPCX/sec8/35) |
| **Falcon launches** | **−17.8%** | Q2 2026 vs Q2 2025, 3M | [📄 p.35](https://agentii.ai/v/SPCX/sec8/35) |
| **Space segment revenue** | **+29.0%** | Q2 2026 vs Q2 2025, 3M | [📄 p.42](https://agentii.ai/v/SPCX/sec8/42) |

**The filing explains the divergence itself, and names the customer count as the driver:**

> *"This increase was primarily driven by an increase in Launch Services revenue of $158
> million and an increase in Launch and Development revenue of $58 million due to an increase
> in customer launches period over period **from 9 ... to 10** ... and a favorable customer
> mix shift."* — [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42) · **DEMONSTRATED**

**So the mechanism is: one more customer launch — a 3M increase of one — plus mix, against
nine fewer internal launches.** Internal launches are 73.7% of the volume and 0% of the
segment revenue. **The aggregate fell by 17.4% while the revenue-bearing subset rose 11.1%,
and nothing in the two numbers is inconsistent.** They are rates on different populations.

⚠️ **Rule for every downstream artifact in this thesis: neither rate may be quoted without
its basis attached.** "+11.1%" alone reads as growth in a shrinking business. "−17.4%" alone
reads as a demand collapse that the revenue line contradicts. **Both are true of the same
quarter.**

**And the period basis flips it again:**

| Space segment revenue | Q2 y/y | H1 y/y | Q2 sequential |
|---|---:|---:|---:|
| Filed change | **+29.0%** | **(1.9)%** | **+55%** (call) |

The **+55% sequential** is Bret Johnsen's: *"Space segment revenue grew **55% sequentially**
and 29% year-over-year to $962 million"* ([📄 SPCX Q2 2026 call
p.3](https://agentii.ai/v/SPCX/ect1/3)) · **CLAIMED**. It reconciles: Q1 2026 Space revenue
= $1,581M − $962M = **$619M**; 962 ÷ 619 − 1 = **+55.4%** ✓. **Three growth rates on one
segment, one quarter, all filed or stated, spanning +29.0% to −1.9%.**

---

## 4. The segment table

**Read from pages. `get_segment_data` is unusable — see §12.3.**

### 4.1 Space segment, all four periods

| $M | Q2 2026 | Q2 2025 | Δ | H1 2026 | H1 2025 | Δ |
|---|---:|---:|---:|---:|---:|---:|
| **Revenue** | **962** | 746 | **+29.0%** | 1,581 | 1,611 | **(1.9)%** |
| Cost of revenue | **329** | 330 | **(0.3)%** | 610 | 627 | (2.7)% |
| Research and development | **1,076** | 693 | +55.3% | 2,006 | 1,219 | +64.6% |
| Selling, general, and administrative | 99 | 87 | +13.8% | 169 | 175 | (3.4)% |
| Impairment | — | 5 | NM | — | 29 | NM |
| **Total costs and expenses** | **1,504** | 1,115 | +34.9% | 2,785 | 2,050 | +35.9% |
| **Loss from operations** | **(542)** | (369) | 46.9% worse | **(1,204)** | (439) | 174.3% worse |

Sources: [📄 p.30](https://agentii.ai/v/SPCX/sec8/30) · [📄 p.31](https://agentii.ai/v/SPCX/sec8/31) ·
[📄 p.32](https://agentii.ai/v/SPCX/sec8/32) · [📄 p.42](https://agentii.ai/v/SPCX/sec8/42) · **DEMONSTRATED**

**Cost of revenue flat while revenue rose 29.0% — and the filing decomposes the flatness:**

> *"Cost of revenue for the three months ended June 30, 2026 was flat compared to the three
> months ended June 30, 2025. This was primarily driven by **higher customer and launch
> overhead costs of $42 million, offset by a decrease in production related costs of $43
> million**"* — [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42)

**The decomposition closes on the filed change line:** +42 − 43 = **$(1)M**, which is exactly
the filed $(1)M / (0.3)% change from $330M to $329M. ✓

**And the H1 counterpart is attributed to the launch decline:**
> *"...a decrease in our Space segment of $17 million **due to fewer customer launches**"*
> — [📄 SPCX 10-Q p.40](https://agentii.ai/v/SPCX/sec8/40)

### 4.2 Space gross margin — SEGMENT basis, and it does NOT reproduce consolidated (DA-30)

| Gross margin | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---:|---:|---:|---:|
| **Space — SEGMENT basis** `(rev − CoR) / rev` | **65.80%** | 55.76% | 61.42% | 61.08% |
| **Consolidated** `(rev − CoR) / rev` | 55.27% | 43.95% | 52.97% | 47.85% |

Arithmetic: **(962 − 329) ÷ 962 = 633 ÷ 962 = 65.80%** ✓ · 641 ÷ 746 = 55.76% ·
971 ÷ 1,581 = 61.42% · 984 ÷ 1,611 = 61.08% · 4,319 ÷ 7,814 = **55.27%**.

**65.80% is a SEGMENT figure and it does not reproduce consolidated (55.27%) — a 10.53 pp
gap at the same instant on the same revenue definition.** ⚠️ **Neither may be quoted as "the
gross margin" without its basis.** The gap exists because Space is a high-margin
customer-revenue segment sitting beside AI at (1,106) cost of revenue on 2,561 revenue
([📄 p.30](https://agentii.ai/v/SPCX/sec8/30)).

**And the margin expansion is itself basis-dependent: +10.04 pp on 3M (55.76% → 65.80%),
but only +0.34 pp on 6M (61.08% → 61.42%).** The quarterly expansion is real, filed, and
**does not persist on the half-year basis.**

⚠️ **No gross-profit LINE exists.** These are arithmetic on filed cells, not filed rows —
SPCX's statement of operations runs revenue → *costs and expenses* → loss from operations
with no gross-profit subtotal ([📄 p.5](https://agentii.ai/v/SPCX/sec8/5)). **This is the
fact that leaves the DA-23 gross-profit bound unexercised (§7).**

### 4.3 The three-segment table, both periods

| $M, Q2 2026 | Space | Connectivity | AI | **Total Reportable Segments** |
|---|---:|---:|---:|---:|
| Revenue | 962 | 4,291 | 2,561 | **7,814** |
| Cost of revenue | 329 | 2,060 | 1,106 | 3,495 |
| Research and development | 1,076 | 294 | 2,178 | 3,548 |
| Selling, general, and administrative | 99 | 281 | 532 | 912 |
| Restructuring charges | — | — | 2 | 2 |
| **Total costs and expenses** | **1,504** | 2,635 | 3,818 | **7,957** |
| **Income (loss) from operations** | **(542)** | **1,656** | **(1,257)** | **(143)** |

H1 2026: Space **1,581 / (1,204)** · Connectivity **7,548 / 2,844** · AI **3,379 / (3,726)** ·
total **12,508 / (2,086)**. Q2 2025: Space **746 / (369)** · Connectivity **2,588 / 923** ·
AI **737 / (1,524)** · total **4,071 / (970)**. H1 2025: Space **1,611 / (439)** ·
Connectivity **5,062 / 1,956** · AI **1,465 / (2,460)** · total **8,138 / (943)**.
Sources: [📄 p.30](https://agentii.ai/v/SPCX/sec8/30) · [📄 p.31](https://agentii.ai/v/SPCX/sec8/31) ·
[📄 p.32](https://agentii.ai/v/SPCX/sec8/32) · **DEMONSTRATED**

**The segment sums close exactly in all four periods** (962 + 4,291 + 2,561 = 7,814 ✓;
1,581 + 7,548 + 3,379 = 12,508 ✓; 746 + 2,588 + 737 = 4,071 ✓; 1,611 + 5,062 + 1,465 =
8,138 ✓), and the segment total also equals the consolidated revenue line on every period.
**The arithmetic is sound; what is not sound is comparability (§4.4).**

### 4.4 Starship R&D = 111.9% of segment revenue

| | Q2 2026 | H1 2026 | Q2 2025 | H1 2025 |
|---|---:|---:|---:|---:|
| Space R&D ($M) | **1,076** | 2,006 | 693 | 1,219 |
| Space revenue ($M) | 962 | 1,581 | 746 | 1,611 |
| **R&D as % of segment revenue** | **111.9%** | **126.9%** | 92.9% | 75.7% |

Arithmetic: **1,076 ÷ 962 = 111.85% → 111.9%** ✓.

**The Space segment spends more developing Starship than the entire segment earns.**
Filed definition: *"Space segment's research and development ... mainly relate to the
development, build, and testing of Starship."* ([📄 p.37](https://agentii.ai/v/SPCX/sec8/37)).
Driver, filed: *"higher production and engineering costs of $311 million and higher launch
and test costs of $73 million to support continued development of the Starship vehicle"*
(Q2) / *"$653 million ... and ... $134 million"* (H1) ([📄 p.42](https://agentii.ai/v/SPCX/sec8/42),
[📄 p.43](https://agentii.ai/v/SPCX/sec8/43)).

**This is where the launch cost actually sits.** Starship R&D is $1,076M against a cost of
revenue of $329M — **the development cost is 3.27× the recognised cost of revenue.** Any
"cost per launch" built from the segment's cost-of-revenue line omits the largest cost in
the segment by a factor of three. §9.4.

### 4.5 The one reconciliation that does close

| $M | Q2 2026 | H1 2026 | Q2 2025 | H1 2025 |
|---|---:|---:|---:|---:|
| Space loss from operations | (542) | (1,204) | (369) | (439) |
| + D&A | 158 | 324 | 146 | 308 |
| + Share-based compensation | 179 | 324 | 125 | 233 |
| + Restructuring / impairment | — | — | 5 | 29 |
| **= Space Segment Adjusted EBITDA** | **(205)** | **(556)** | **(93)** | **131** |

Identity closes exactly on every period: −542 + 158 + 179 = **(205)** ✓;
−1,204 + 324 + 324 = **(556)** ✓; −369 + 146 + 125 + 5 = **(93)** ✓;
−439 + 308 + 233 + 29 = **131** ✓. Segments sum to consolidated Adjusted EBITDA
(−205 + 2,597 + 1,146 = **3,538** ✓; −556 + 4,684 + 537 = **4,665** ✓).
[📄 p.46](https://agentii.ai/v/SPCX/sec8/46) · [📄 p.47](https://agentii.ai/v/SPCX/sec8/47) · **DEMONSTRATED**

**Note the sign change: Space Segment Adjusted EBITDA was POSITIVE $131M in H1 2025 and is
$(556)M in H1 2026 — a $(687)M swing on a fully-reconciling filed metric.** This
reconciliation is the ONE place segment figures tie to consolidated without a
contamination gap, and it is a non-GAAP measure.

---

## 5. The `12.3%` correction

**`12.3%` is the Space segment's share of consolidated revenue, Q2 2026: 962 ÷ 7,814 =
12.31%.** It is **our arithmetic on filed cells, not a filed figure — a phrase search of the
10-Q returns no page carrying "12.3%" on any basis** · **DEMONSTRATED** (arithmetic).

**It is three things at once:**

1. **It is not "launch."** The numerator is the whole Space **segment**, which is 67.4%
   Launch Services **and 32.6% Launch & Development** (spacecraft development and mission
   services for government programmes) at Q2 2026 ([📄 p.37](https://agentii.ai/v/SPCX/sec8/37)).
   **Launch-only is 648 ÷ 7,814 = 8.29%.**
2. **The denominator is entity-boundary contaminated.** The consolidated denominator
   includes the AI segment, which entered by **common-control merger on 2026-02-02** and
   whose comparatives were recast ([📄 p.11](https://agentii.ai/v/SPCX/sec8/11)).
3. **The sentence juxtaposes a Q2 SHARE against H1 GROWTH rates.** The share is 3M; the
   growth rates typically paired with it (−19.0% customer launches, 3 → 1 Starship) are 6M.
   §1.

**Per DA-30, all four denominators, side by side:**

| Space revenue share | Q2 2026 | H1 2026 | Q2 2025 | H1 2025 | Δ direction |
|---|---:|---:|---:|---:|---|
| **Consolidated** (the quoted 12.3%) | **12.31%** | 12.64% | 18.32% | 19.80% | **falling** |
| **Launch-only** (Launch Services ÷ consolidated) | **8.29%** | 7.82% | 12.04% | 12.98% | **falling** |
| **Ex-AI** (Space ÷ (consolidated − AI)) | **18.31%** | 17.32% | 22.38% | 24.14% | **falling** |
| Segment-of-segment (Space ÷ Space+Connectivity) | 18.31% | 17.32% | 22.38% | 24.14% | **falling** |

Arithmetic: 962 ÷ 7,814 = **12.31%** · 648 ÷ 7,814 = **8.29%** · 962 ÷ (7,814 − 2,561) =
962 ÷ 5,253 = **18.31%** · 746 ÷ 4,071 = 18.32% · 746 ÷ (4,071 − 737) = 746 ÷ 3,334 = 22.38% ·
1,611 ÷ (8,138 − 1,465) = 1,611 ÷ 6,673 = 24.14% ·
978 ÷ 12,508 = 7.82% · 1,581 ÷ 9,129 = 17.32%.

> **Direction survives every basis. Level survives none.** Space's share of revenue falls on
> all four denominators in both period pairs — but the *level* spans **8.29% to 18.31%** at
> the same instant, a **2.21×** spread. **Any artifact quoting 12.3% as "Space is 12.3% of
> SPCX" is quoting one of four defensible numbers as though it were the only one.**

⚠️ **`12.3%` must never be paired with a launch rate without saying which activity it
measures.** It is not the launch share, and the launch share on the launch-only basis
(8.29%) is not it either.

---

## 6. `$(1,257)M` is FILED, not DERIVED

**The AI segment's loss from operations is $(1,257)M for Q2 2026 and $(3,726)M for H1 2026.
It is a filed line item, disclosed four separate times, and no artifact may report it as
derived.**

| Venue | Source | What it shows |
|---|---|---|
| **Note 18, Segment Information** | [📄 p.30](https://agentii.ai/v/SPCX/sec8/30) | `Income (loss) from operations \| (542) \| 1,656 \| (1,257) \| (143)` — **AI as its own filed column** |
| **MD&A, AI Segment Results** | [📄 p.44](https://agentii.ai/v/SPCX/sec8/44) | the full cost stack — revenue 2,561, cost of revenue 1,106, R&D 2,178, SG&A 532, restructuring 2, total 3,818, **loss from operations (1,257)** |
| **Non-GAAP Segment Adjusted EBITDA** | [📄 p.46](https://agentii.ai/v/SPCX/sec8/46) | repeats `(542) \| 1,656 \| (1,257) \| (143)` |
| **Earnings call** | [📄 ect1 p.3](https://agentii.ai/v/SPCX/ect1/3) | *"meaningfully narrowed our AI segment net operating loss to **$1.3 billion**"* — **the issuer calls it a loss** |

**Component identity, in-line, on the filed cells:**
`2,561 − 1,106 − 2,178 − 532 − 2 = (1,257)` ✓ and the cost lines sum to the filed total of
$3,818M ✓. **DEMONSTRATED — FILED.**

**And the call is an independent confirmation of the SIGN.** The issuer describes the same
figure as a *loss*, which is the second detector against the platform's served `+1,257`.

⚠️ **Carried forward from 002 §7.1:** the inherited position that this line is "DERIVED,
never as filed" is **WRONG for the second time.** 002 overturned it; this artifact re-verifies
it at source on this thesis's own pin. **Do not re-derive it, and do not label it derived.**

---

## 7. DA-23 at SPCX

**CONFIRMED — and as a census, not a sample.**

**The served value: `us-gaap:OperatingIncomeLoss`, Q2 2026, consolidated = `+143,000,000`
against a filed `$(143)M`** — exactly the inherited instance. **The filed value is $(143)M.**

### 7.1 The detector — the component identity, run in-line

**Mandatory under the register. `EPS × shares` is inadmissible and is not used.**

The identity is CONDITIONAL: `us-gaap:CostsAndExpenses` is **INCLUSIVE** of cost of sales,
so at SPCX — which files a cost-of-revenue line — the `gross profit − opex` form is false if
opex is taken as `CostsAndExpenses`; the **cost of revenue would be counted twice.** The
admissible form at SPCX is therefore `revenue − total costs and expenses`, where total costs
and expenses already contains cost of revenue. **Both forms are shown so the opex definition
is explicit:**

```
SPCX CONSOLIDATED Q2 2026        filed cells (10-Q p.5; MD&A p.40)
  revenue                                 7,814
  total costs and expenses               (7,957)      <- OpexDefinition: CostsAndExpenses, INCLUSIVE of cost of revenue
  loss from operations                     (143)      <- identity: 7,814 - 7,957 = (143)  CLOSES
  cross-form (gross margin basis):
    7,814 - 3,495 = 4,319  gross margin on segment-style basis
    4,319 - 3,548(R&D) - 912(SG&A) - 2(restruct) - 0(impair) =     (143)  CLOSES
  components: 3,495 + 3,548 + 912 + 2 + 0 = 7,957 = filed total line  CLOSES
```

H1 2026: `12,508 − 14,594 = (2,086)` ✓, components sum to 14,594 ✓.
Q2 2025: `4,071 − 5,041 = (970)` ✓. H1 2025: `8,138 − 9,081 = (943)` ✓.

**All four consolidated identities close exactly, and all four are negative. The served
values are positive in all four cases.**

```
SPCX SPACE SEGMENT Q2 2026       filed cells (10-Q p.30; MD&A p.42)
  revenue                                  962
  cost of revenue                         (329)
  research and development              (1,076)
  selling, general, and administrative     (99)
  total costs and expenses              (1,504)   <- filed line; 329 + 1,076 + 99 = 1,504 ✓
  loss from operations                    (542)   <- 962 - 1,504 = (542)  CLOSES
```

### 7.2 The census — 16 of 20, and the 4 survivors prove the mechanism

| Dimension key | Period | Filed | Served | Status |
|---|---|---:|---:|---|
| Space | Q2 2026 | (542) | +542 | **STRIPPED** |
| Space | H1 2026 | (1,204) | +1,204 | **STRIPPED** |
| Space | Q2 2025 | (369) | +369 | **STRIPPED** |
| Space | H1 2025 | (439) | +439 | **STRIPPED** |
| AI | Q2 2026 | (1,257) | +1,257 | **STRIPPED** |
| AI | H1 2026 | (3,726) | +3,726 | **STRIPPED** |
| AI | Q2 2025 | (1,524) | +1,524 | **STRIPPED** |
| AI | H1 2025 | (2,460) | +2,460 | **STRIPPED** |
| Total Reportable Segments | Q2 2026 | (143) | **+143** | **STRIPPED ← the inherited instance** |
| Total Reportable Segments | H1 2026 | (2,086) | +2,086 | **STRIPPED** |
| Total Reportable Segments | Q2 2025 | (970) | +970 | **STRIPPED** |
| Total Reportable Segments | H1 2025 | (943) | +943 | **STRIPPED** |
| Consolidated (undimensioned) | Q2 2026 | (143) | +143 | **STRIPPED** |
| Consolidated (undimensioned) | H1 2026 | (2,086) | +2,086 | **STRIPPED** |
| Consolidated (undimensioned) | Q2 2025 | (970) | +970 | **STRIPPED** |
| Consolidated (undimensioned) | H1 2025 | (943) | +943 | **STRIPPED** |
| **Connectivity** | **Q2 2026** | **+1,656** | **+1,656** | **CORRECT** |
| **Connectivity** | **H1 2026** | **+2,844** | **+2,844** | **CORRECT** |
| **Connectivity** | **Q2 2025** | **+923** | **+923** | **CORRECT** |
| **Connectivity** | **H1 2025** | **+1,956** | **+1,956** | **CORRECT** |

**16 of 20 served facts are sign-destroyed. The only four that survive are the four whose
filed sign is POSITIVE.** That is decisive: the defect is **`|x|` absolute-value stripping,
not inversion** — a systematic inverter would have flipped the Connectivity facts too.

⚠️ **Two additional hazards in the same served set:**
- **Double-counting.** The four "Total Reportable Segments" facts and the four
  "Consolidated (undimensioned)" facts are the **same four magnitudes served twice** under
  different dimension keys. **Any consumer that sums across dimension keys double-counts
  $(143)M / $(2,086)M / $(970)M / $(943)M.**
- **Every screen on the raw field inverts.** Space, AI and the consolidated total all rank
  as profitable on the served values. **A screen on the raw field puts the worst loss-makers
  at the top.**

### 7.3 The gross-profit bound is UNEXERCISED — not CLEAN

**The register's alternative detector ("invoke the gross-profit bound where the component
identity is unavailable") cannot run at SPCX.**

- **Zero `us-gaap:GrossProfit` facts exist for SPCX** on any period, any dimension
  (`search_xbrl_facts`, concept `GrossProfit` → `total_count: 0`). The concept is populated
  platform-wide (5,551 facts across 87 tickers) — **the absence is SPCX-specific.**
- **No statement files a gross-profit line.** The consolidated statement of operations runs
  `Revenue` → `Costs and expenses` → `Loss from operations`, and the segment tables likewise
  ([📄 p.5](https://agentii.ai/v/SPCX/sec8/5),
  [📄 p.30](https://agentii.ai/v/SPCX/sec8/30)). **The subtotal does not exist to be bound
  against.**

**Recorded as `UNEXERCISED`. It is NOT clean. An unengaged check is not a passed check.**

**And the reason it matters here is specific:** SPCX's Space segment runs a **65.80%** gross
margin (§4.2) — high enough that a reader would not expect a loss. **A gross-profit bound
would have bounded the served magnitude against a large positive gross profit; with no
gross-profit line, the sign error is detectable ONLY by the component identity.** The
identity is available and was run (§7.1), so this artifact is not blocked — but the
second detector is **absent**, and its absence is recorded as absence.

---

## 8. DA-26 at SPCX — NOT TESTABLE

**Recorded `UNRESOLVED`, not clean. Class: `UNRESOLVABLE-FROM-PLATFORM`.**

Two independent blockers, each verified:

1. **No annual row exists.** The platform's SPCX SEC corpus is **one 10-Q (`sec8`), eight
   8-Ks, and one earnings-call transcript — there is NO 10-K.** DA-26 is "an annual figure
   mislabelled as quarterly"; with no annual figure on the platform the defect has no input.
2. **`fiscal_period="Q4"` returns 0 facts.** The probe is empty.

**A probe of the label layer found a same-family defect in the INVERSE direction, and it is
NOT reported as DA-26 CONFIRMED:**

| `fiscal_period` filter on `OperatingIncomeLoss` | Facts returned |
|---|---|
| **`"Q2"`** | **2** — Q2 2026 (2026-04-01→06-30) and Q2 2025. **Filter works.** |
| **`"Q4"`** | **0** |
| **`"FY"`** | **4 — the SAME four as NO filter at all:** Q2 2026, H1 2026, Q2 2025, H1 2025 |

**`fiscal_period="FY"` at SPCX returns half-year and quarter durations — the FY label is not
bound to a 12-month duration here.** A researcher asking for "FY" data silently receives a
mix of Q2 and H1 facts and could mistake the **$12,508M H1 revenue / $(4,817)M H1 net loss**
for a full year. **This is the DA-26 family (a period label not bound to its duration) but
in the inverse direction from the registered form, and it is recorded as a label-layer
observation, not as DA-26.** ⚠️ **`fiscal_period` is not a reliable period-type discriminator
at SPCX; use `period_start` / `period_end`, which is what this artifact does throughout.**

**Resolution path:** SPCX was private through FY2025, so its first 10-K is **FY2026, not yet
due** (a Dec-31 filer files ~Feb 2027). **Until then the registered DA-26 test has no annual
row to run on, on the platform or in public sources.** The platform-side block is that its
SPCX corpus contains one interim report; the public-side block is that no annual filing
exists yet.

---

## 9. The per-launch series — derivation path (methodology)

**Mode: methodology — the derivation path, stated so the number is reproducible.**

### 9.1 There is no filed per-launch series. This is a NULL finding.

**SPCX files mass to orbit and launch counts as totals, and no per-unit series on any
basis.** Read in full across the pages that would carry it — the key business metrics
([📄 p.35](https://agentii.ai/v/SPCX/sec8/35),
[📄 p.36](https://agentii.ai/v/SPCX/sec8/36)), the segment revenue-recognition and expense
definitions ([📄 p.37](https://agentii.ai/v/SPCX/sec8/37)) and the whole Space segment
results discussion ([📄 p.42](https://agentii.ai/v/SPCX/sec8/42),
[📄 p.43](https://agentii.ai/v/SPCX/sec8/43)) — **no per-launch and no per-kilogram figure
appears.** A phrase-level search for "cost per launch" returns no page of the 10-Q.

**Everything in §9.2–§9.4 is therefore `MODELED`: our denominator choice, on filed
numerators. Per §3.2 of the brief, a `MODELED` input can never satisfy a falsifier.**

### 9.2 Revenue per launch — denominator choice moves the answer 3.4×

| $M unless noted | Q2 2026 | Q2 2025 | **Δ** | H1 2026 | H1 2025 | **Δ** |
|---|---:|---:|---:|---:|---:|---:|
| Space segment revenue | 962 | 746 | +29.0% | 1,581 | 1,611 | (1.9)% |
| ÷ **customer launches** (the boundary-consistent basis) | 10 | 9 | +11.1% | 17 | 21 | (19.0)% |
| **= $M per customer launch** | **96.2** | **82.9** | **+16.1%** | **93.0** | **76.7** | **+21.3%** |
| ÷ **total launches** (all vehicles — the boundary-violating basis) | 38 | 46 | (17.4)% | 78 | 84 | (7.1)% |
| **= $M per launch** | **25.3** | **16.2** | **+55.4%** | **20.3** | **19.2** | **+5.7%** |

Arithmetic: 962 ÷ 10 = **96.2**; 746 ÷ 9 = 82.89; 96.2 ÷ 82.89 = **+16.06%**.
1,581 ÷ 17 = 93.0; 1,611 ÷ 21 = 76.71; 93.0 ÷ 76.71 = **+21.23%**.
962 ÷ 38 = 25.32; 746 ÷ 46 = 16.22; 25.32 ÷ 16.22 = **+55.44%**.
1,581 ÷ 78 = 20.27; 1,611 ÷ 84 = 19.18; 20.27 ÷ 19.18 = **+5.69%**.

⚠️ **The same numerator over two denominators gives +16.1% or +55.4% in the same quarter —
a 3.4× spread.** The customer basis is the only one consistent with the filed revenue
boundary (§2). **The total-launch basis divides a customer-only numerator by a denominator
73.7% of which is contractually revenue-free.**

### 9.3 Cost per launch — the denominator choice FLIPS THE SIGN

**The only cost-side filed line for the Space segment is cost of revenue ($329M Q2 2026).
It is NOT a launch cost — see §9.4.**

| $M unless noted | Q2 2026 | Q2 2025 | **Δ** | H1 2026 | H1 2025 | **Δ** |
|---|---:|---:|---:|---:|---:|---:|
| Space segment cost of revenue | 329 | 330 | (0.3)% | 610 | 627 | (2.7)% |
| ÷ customer launches | 10 | 9 | +11.1% | 17 | 21 | (19.0)% |
| **= $M per customer launch** | **32.9** | **36.7** | **−10.3%** | **35.9** | **29.9** | **+20.2%** |
| ÷ total launches | 38 | 46 | (17.4)% | 78 | 84 | (7.1)% |
| **= $M per launch** | **8.66** | **7.17** | **+20.7%** | **7.82** | **7.46** | **+4.8%** |

Arithmetic: 329 ÷ 10 = 32.9; 330 ÷ 9 = 36.67; 32.9 ÷ 36.67 = **−10.27%**.
329 ÷ 38 = 8.658; 330 ÷ 46 = 7.174; 8.658 ÷ 7.174 = **+20.69%**.
610 ÷ 17 = 35.88; 627 ÷ 21 = 29.86; 35.88 ÷ 29.86 = **+20.18%**.
610 ÷ 78 = 7.821; 627 ÷ 84 = 7.464; 7.821 ÷ 7.464 = **+4.77%**.

> **Cost per launch FELL 10.3% and ROSE 20.7% in the SAME QUARTER on the SAME numerator.**
> **The denominator choice flips the sign of the reported direction.** No artifact in this
> thesis may state a per-launch cost direction without stating which denominator produced it.

**Read together on the consistent basis (§9.2 + §9.3, customer denominator):**
cost per customer launch **−10.3%**, revenue per customer launch **+16.1%**. **That is the
mechanism by which Space revenue rose 29.0% while its cost of revenue fell 0.3%** — the
margin expansion of §4.2 resolved into its per-unit components. ⚠️ **But it does not persist:
on H1 the same pair is cost +20.2% and revenue +21.3%, near-identical growth — consistent
with the 6M margin expansion of only +0.34 pp against the 3M +10.04 pp.**

### 9.4 Why no per-launch cost is definable at SPCX — three disqualifications

1. **The cost line excludes the largest cost.** Starship R&D $1,076M is **3.27×** the
   $329M cost of revenue (§4.4). A per-launch cost built on cost of revenue omits it. The
   fully-loaded Space cost and expenses are **$1,504M**, i.e. **156.3%** of segment revenue.
2. **The cost line is not launch-only.** The filed definition includes *"second stages flown
   ... launch operations and overhead, depreciation (inclusive of booster, Merlin engine, and
   fairing depreciation), employee compensation ... launch testing and overhead, engineering
   costs, inventory excess and obsolescence, shared costs incurred in the production of
   launch hardware, and ongoing product support"* ([📄 p.37](https://agentii.ai/v/SPCX/sec8/37))
   — **and it covers the Launch & Development revenue too, which is 32.6% of the segment and
   is spacecraft development, not launch** ([📄 p.37](https://agentii.ai/v/SPCX/sec8/37)).
3. **The internal launches' cost is not in the segment at all.** It is capitalised into
   satellites and surfaces as Connectivity depreciation (§2). **So the denominator "total
   launches" contains 73.7% of the volume whose cost is in a different segment than the
   numerator.**

### 9.5 The only cost-per-launch-like statement in the corpus is CLAIMED

> *"Starship aims to quadruple payload capacity and **reduce launch costs by 10x** compared
> to our Falcon 9 rocket"* — Bret Johnsen, [📄 SPCX Q2 2026 call
> p.3](https://agentii.ai/v/SPCX/ect1/3) · **CLAIMED**

**A ratio of two forward-looking targets, with no filed basis, no cost level, no denominator
definition, and no period.** It cannot be converted to a $/kg or $/launch figure, and it
cannot be reconciled to the segment table. **It is the PIL-3 finding in one sentence: the
cost curve at SPCX is CLAIMED, and the claim is a multiplier on an unstated base.**
⚠️ Per the inherited correction, **F2 must be cited as an order of magnitude** — this "10x"
is likewise an order-of-magnitude CLAIM, never a point value.

⚠️ **Related CLAIMED statement, flagged for tension, not resolved:** Shotwell — *"We're
currently launching at our highest Falcon cadence"* ([📄 ect1
p.2](https://agentii.ai/v/SPCX/ect1/2)). **The filed Q2 count is 37 against 45 (a 17.8%
decline) and H1 is 77 against 81.** The statement is about a current run-rate on an
unstated period; **it is not reconciled to any filed quarter.** Recorded as CLAIMED and
**not** used in any series.

---

## 10. Triggers — what would overturn this conclusion

**Mode: triggers — the trigger set that would overturn this conclusion.**

| # | Trigger | What it overturns | Status |
|---|---|---|---|
| **T1** | A filed **per-launch or per-kilogram** series on any basis, any period | §9.1's null; would convert the whole §9 series from MODELED to DEMONSTRATED | **NOT TRIGGERED** — no such line exists in the corpus |
| **T2** | A customer-launch count that **moves with** total launches over two or more periods | §3's divergence is structural, not a one-period artefact | **NOT TRIGGERED** — Q2 diverges (+11.1% vs −17.4%); H1 converges (−19.0% vs −7.1%). **One period of each — the divergence is NOT yet established as structural** |
| **T3** | A quarter where the **customer share of launches exceeds ~50%** | §2's "~74% produce no Space revenue" as a standing property | **NOT TRIGGERED** — 26.3% (Q2), 21.8% (H1) |
| **T4** | Space segment cost of revenue rising **with** launch counts | §4.1's flat-cost-against-29.0%-revenue reading | **NOT TRIGGERED** — cost of revenue (0.3)% against revenue +29.0% |
| **T5** | Disclosure of a **Space-segment-only** gross margin, or a gross-profit line anywhere | §7.3's `UNEXERCISED` gross-profit bound — the bound would become exercisable | **NOT TRIGGERED** — 0 `us-gaap:GrossProfit` facts |
| **T6** | An **FY2026 10-K** (due ~Feb 2027) | §8's `NOT TESTABLE` DA-26 verdict — an annual row would exist to test the label layer against | **PENDING — the single highest-value resolution** |
| **T7** | A filed AI-segment comparative that is **not recast**, or a disaggregation of SPCX-native vs merged AI revenue | §5's entity-boundary contamination of the denominator | **NOT TRIGGERED** — the AI segment appears in periods predating the 2026-02-02 merger ([📄 p.31](https://agentii.ai/v/SPCX/sec8/31), [📄 p.32](https://agentii.ai/v/SPCX/sec8/32)) |
| **T8** | A **Starship cost per launch** once operational | §9.5's CLAIMED status; the 10x target becoming measurable | **NOT TRIGGERED** — all Starship launches internal to date; zero operational V3 deployments |
| **T9** | Platform serving the sign **correctly** on a later SPCX filing | §7's DA-23 census as a standing property of the served layer | **NOT TRIGGERED** — 16 of 20 stripped at this filing |
| **T10** | Any **revenue-bearing internal launch** (e.g. an inter-segment AI launch recognised in Space) | §2's customer boundary as the revenue boundary | **NOT TRIGGERED** — the filing states no inter-segment revenue is recognised for Starlink launches ([📄 p.36](https://agentii.ai/v/SPCX/sec8/36)) |

**T2 is the weakest joint and the most important.** The divergence in §3 — customer launches
up while total launches fall — is **demonstrated in Q2 and absent in H1**: on the 6M basis
both are negative (−19.0% customer, −7.1% total), so the *aggregate* fell less than the
*customer* subset. **The "opposite-signed rates" finding is a 3M phenomenon.** It is filed,
correct, and reproducible — but **an artifact asserting it as a standing property of the
business would be over-reading one quarter.** Recorded as the primary constraint on §3.

---

## 11. Defaults — the assumptions used where no filed figure exists

**Mode: defaults — the default assumptions used where no filed figure exists.**

| # | Where no filed figure exists | Default adopted | Why, and what it costs |
|---|---|---|---|
| **D1** | **Total launch count** — the filing files Falcon and Starship as separate rows; no "total launches" row exists | **Falcon + Starship, summed.** 38 (Q2 2026), 78 (H1 2026) | Vindicated by the issuer, not assumed: the call says *"78 total launches"*. **Cross-confirmed.** Where the two disagree the filing governs |
| **D2** | **The denomination of a launch** for per-launch ratios | **Customer launches are the ONLY admissible denominator for a Space-revenue ratio** | Not a preference — it is the filed revenue boundary (§2). **A total-launch denominator is not an alternative basis, it is a category error** |
| **D3** | **The cost numerator** for any per-launch cost | **None adopted. Reported as undefined.** | §9.4's three disqualifications; any single choice would misstate by a factor of three or more |
| **D4** | **Gross margin** — no filed gross-profit line exists | **`(revenue − cost of revenue) / revenue`, labelled by basis** | Arithmetic on filed cells. **The consolidated and segment figures differ by 10.53 pp (§4.2); the default must never be quoted without its basis** |
| **D5** | **Space-segment operating income** on a clean basis | **The filed $(542)M, accepted as filed** | DA-24 REFUTED on evidence (§definitions); no non-operating item sits above the line |
| **D6** | **The AI segment's entity-boundary attribution** — SPCX-native vs merged revenue is not disaggregated | **Treat the whole AI segment as contaminated** | Conservative. The X merger (2025-03-28) falls inside H1 2025 and the xAI merger (2026-02-02) inside H1 2026, so **no clean AI sub-period exists to carve out** |
| **D7** | **A fiscal-period label** for any XBRL fact | **`period_start` / `period_end`, never `fiscal_period`** | §8: `fiscal_period="FY"` is not duration-bound at SPCX |
| **D8** | **The per-launch figures of §9** | **`MODELED`, stated as MODELED** | Per brief §3.2, a MODELED input can never satisfy a falsifier. **None of §9 may be used to discharge a trigger** |
| **D9** | **Rounding** in the mass-to-orbit split | **Filed totals govern; components may not sum** | The filing's own footnote: *"Amounts presented may not add up to the corresponding totals due to rounding"* ([📄 p.35](https://agentii.ai/v/SPCX/sec8/35)) |

---

## 12. Retrieval scope — sources admitted and excluded

**Mode: retrieval-scope — which sources are admitted and which are excluded.**

### 12.1 Admitted

| Source | Identifier | Role |
|---|---|---|
| **SPCX Form 10-Q**, quarter ended 2026-06-30, filed 2026-08-04 | **`sec8`** (accession `0001628280-26-052535`) | **The primary and controlling source.** All §1–§9 figures |
| **SPCX Q2 2026 earnings call transcript**, 2026-08-04 | **`ect1`** | **Secondary, CLAIMED grade only.** Used for cross-confirmation (the 78-launch check), for the sequential growth rate, and for §9.5's cost claim |

### 12.2 Excluded, and why

| Excluded | Why |
|---|---|
| **All eight SPCX 8-Ks** (`sec1`–`sec7`, `sec9`) | Event filings — IPO pricing, note offerings, Cursor merger agreement, board election. **No Space operating metrics**; none is a source of the series in this artifact |
| **`get_segment_data`** | **UNUSABLE — see 12.3** |
| **`data_freshness` metadata** | Reports `2027-04-12` on a 2026-09-19 corpus. **Not a usable freshness signal**; every response in this artifact carries it |
| **Sibling artifacts 001 / 002** | Admitted only as **inherited corrections** (the customer-boundary finding, the `$(1,257)M` FILED verdict, the F2 order-of-magnitude rule), **never as a figure source.** Every figure here is re-read at source |
| **Issuer website / press / third-party $/kg** | Not reached; no admissible `agentii.ai` citation path. **The RKLB $/kg corrections (§4 of the brief) are inherited, not re-derived** |

### 12.3 `get_segment_data` — UNUSABLE, and its failure mode has changed

**Called for SPCX and it did NOT error. It returned data — and the data is wrong.** This is
a worse failure mode than the inherited one and is recorded as such.

| Observed | Filed | Verdict |
|---|---|---|
| `Space` row: revenue **$1,611M**, operating_income **+$1,204M** | Space H1 **2025** revenue is **$1,611M**; Space H1 **2026** loss is **$(1,204)M** | **Period-mixed AND sign-stripped.** The revenue column is H1 2025 and the operating column is H1 2026 — **the row reconciles to no single filed period** |
| `A I` row: operating_income **+$3,726M** | filed **$(3,726)M** (H1 2026) | **DA-23, second site** |
| `Connectivity` row: revenue $7,548M, operating_income +$2,844M | both H1 2026, both correct signs | correct — and the contrast proves stripping |
| `total_revenue` **$32,531M**, `segment_coverage_pct` **116.2%** | consolidated H1 2026 revenue **$12,508M** | **Sum is 260% of actual** — the tool sums product-dimension rows, segment rows and multiple periods together |
| Rows named `Grok`, `Vidstream L L C`, `Gwynne Shotwell`, `Antonio J. Gracias`, `Bret Johnsen`, `Surety Bond`, `Federal Funds Rate`, `Jane Doe V. X. A. I Corp. …` | — | **Every dimension member is emitted as a segment.** These are not segments |

⚠️ **`segment_coverage_pct: 116.2%` is the tool's own metadata admitting >100% coverage —
i.e. its own double-count.** **The tool reports no `note` and no error.** An artifact that
trusted it would inherit a period-mixed, sign-stripped, double-counted segment table that
looks like a successful call. **Read pages.**

### 12.4 The source layer has its own label defect — one instance

The `read_source_outline` description for **p.55** reads *"Signature page of the **10-K**
report"*. **Read at source, p.55 is the signature page of this 10-Q** — *"Pursuant to the
requirements of the Securities Exchange Act of 1934, the registrant has duly caused **this
report** to be signed"*, dated August 4, 2026, signed by the CFO
([📄 SPCX 10-Q p.55](https://agentii.ai/v/SPCX/sec8/55)). **The outline layer mislabels the
form; the page does not.** Recorded as a caution: *the outline descriptions are a routing
aid, not evidence, and figures must be read from pages.*

---

## 13. Retrieval strategy — how the sources were located

**Mode: retrieval-strategy — how the sources were located, so the search repeats.**

Reproducible sequence. Every step names its tool.

| # | Step | Tool | Result |
|---|---|---|---|
| 1 | Confirm coverage and locate the filing | `get_ticker_coverage` | SPCX: 8 SEC filings, 1 transcript; `data_freshness` **2027-04-12** (unusable) |
| 2 | Enumerate the corpus | `search_sec_filings(ticker=SPCX)` | 9 rows — **one 10-Q (`sec8`)**, eight 8-Ks. **No 10-K.** Establishes §8's blocker |
| 3 | Map the 10-Q | `read_source_outline(ticker=SPCX, citation_id=sec8)` | 55 pages. Key pages: **35–37** (key metrics, definitions), **30–32** (Note 18 segments), **40–44** (MD&A), **13** (disaggregation), **5** (statement of operations), **46–47** (non-GAAP), **11** (entity boundary) |
| 4 | Read the metric and boundary pages | `read_source_pages` p.35, 36, 13 | **Mass to orbit and launch tables; the boundary sentence; the revenue disaggregation** |
| 5 | Read the segment tables | `read_source_pages` p.30, 31, 32 | Note 18, all four periods |
| 6 | Read the MD&A | `read_source_pages` p.42, 43, 40, 44, 41 | **Space drivers (§3), the 29.0% / (1.9)% table, the AI cost stack** |
| 7 | Read the face and the definitions | `read_source_pages` p.5, 34, 37 | **No gross-profit line; the Launch Services % table; the cost-of-revenue definition** |
| 8 | Read the reconciliations and boundary | `read_source_pages` p.46, 47, 11 | Segment Adjusted EBITDA (§4.5); merger dates (§5) |
| 9 | **Null test** — is there a per-launch series? | `search_keyword_in_source(sec8, "cost per launch")` | **0 pages.** Corroborated by full reads of p.35–37 and p.40–44. ⚠️ **The keyword tool is a loose token match, not a phrase match** (see caveat below) |
| 10 | **Prove 12.3% is not filed** | `search_keyword_in_source(sec8, "12.3%")` | **0 pages** — 12.3% is our arithmetic, not a disclosure |
| 11 | **DA-23 census** | `search_xbrl_facts(concept=OperatingIncomeLoss)` — standard, then **`view="detailed"`** | **20 facts: 16 stripped, 4 correct** (§7.2). **The `detailed` view is required** — the standard view returns only the 4 undimensioned facts and hides the 12 segment facts |
| 12 | **Gross-profit bound** | `search_xbrl_facts(concept=GrossProfit)` | **0 facts** → **UNEXERCISED** (§7.3). Concept existence confirmed platform-wide via `list_xbrl_concepts(search="GrossProfit")` (5,551 facts / 87 tickers) — **the absence is SPCX-specific, not a concept that does not exist** |
| 13 | **DA-26 probes** | `search_xbrl_facts(fiscal_period="Q4")` → 0; `fiscal_period="FY"` → 4 (= no filter); `fiscal_period="Q2"` → 2 | §8. **The `Q2` control is what makes the `FY` result interpretable** |
| 14 | Cross-confirm on the transcript | `list_sources(source_type="earnings_call_transcript")` → `source_id`; `read_source_outline(source_id=…)` → citation_id **`ect1`**; `read_source_pages(ect1, p.2, p.3)` | The 78-launch check; the +55% sequential; **the 10x cost CLAIM (§9.5)** |
| 15 | **Confirm the segment tool is unusable** | `get_segment_data(ticker=SPCX)` | Returned data, all of it wrong (§12.3) |

**Caveat on step 9, stated so the null is not over-read.** The `search_keyword_in_source`
tool matched `"revenue per launch"` to p.36 and `"cost per launch"` to two transcript pages
that contain **"launch costs"** and **"revenue"** separately — **it is a token match, not a
phrase match.** The null for §9.1 therefore rests on the **full page reads** of p.35–37 and
p.40–44, which is the stronger evidence; the keyword probes are corroborative only.

**The one step that must not be skipped: step 11's `view="detailed"`.** The default
`standard` view reports only the four *undimensioned* consolidated facts — **all four
stripped, but no segment fact visible.** The census that distinguishes stripping from
inversion is only obtainable from the `detailed` view, where the four correct Connectivity
facts appear beside the twelve stripped segment facts.

---

## 14. What this could not resolve

| # | Unresolved | Class | What would resolve it |
|---|---|---|---|
| **U1** | **DA-26 is not testable at SPCX** — no annual row exists; `fiscal_period="Q4"` returns 0 facts | **UNRESOLVABLE-FROM-PLATFORM** | The **FY2026 10-K**, due ~Feb 2027. SPCX was private through FY2025, so **no annual filing exists to test against on any source, not only this platform.** Registered as `unresolvable: true` in frontmatter |
| **U2** | **No per-launch or per-kilogram cost exists on any basis** — and none is definable from the filed lines (§9.4) | **UNRESOLVABLE-FROM-PUBLIC-SOURCES** | Disclosure of a Starship or Falcon cost per launch once Starship is operational. **The issuer has the figure and discloses only the forward 10x target (§9.5)** |
| **U3** | **Starship launches were 1 in H1 2026 against 3 in H1 2025** — no cost or revenue is separable for a one-unit population | **UNRESOLVABLE-FROM-PUBLIC-SOURCES** | A Starship launch count large enough to form a rate, plus any Starship cost disclosure |
| **U4** | **Whether the Q2 customer/total launch divergence is structural** — it is absent on the H1 basis (§10 T2) | **UNRESOLVABLE-FROM-PLATFORM** | Two or more further quarters of the filed launch table. **This filing supplies exactly one period of divergence** |
| **U5** | **SPCX-native vs merged AI revenue** is not disaggregated; the X merger sits inside H1 2025 and xAI inside H1 2026 | **UNRESOLVABLE-FROM-PUBLIC-SOURCES** | A carve-out disclosure. **Default D6 treats the whole AI segment as contaminated** |
| **U6** | **The four "Total Reportable Segments" and four consolidated facts are the same magnitudes served twice** — no dimension-key reconciliation is published | **UNRESOLVABLE-FROM-PLATFORM** | A dimension-key contract for `OperatingIncomeLoss`. Recorded as a double-count hazard (§7.2) |

**Not unresolved, and stated so it is not mistaken for one:**
- **`$(1,257)M` is FILED** (§6) — four venues, identity closes. **Not derived.**
- **DA-23 is CONFIRMED, not unresolved** (§7) — 16 of 20, mechanism proven by the survivors.
- **DA-24 is REFUTED on evidence, not untested** (frontmatter) — the non-operating items are
  filed below the line.

**And one disposition that is neither resolved nor unresolved — it is unengaged:**

> **The DA-23 gross-profit bound is `UNEXERCISED` at SPCX.** Zero `us-gaap:GrossProfit`
> facts; no gross-profit line in any statement. **This is an absent check, not a passed
> check, and it is recorded as absent.** The component identity carried the sign test
> instead, and it closed exactly at four levels.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| SPCX sec8 p.36 | [📄 SPCX  p.36](https://agentii.ai/v/SPCX/sec8/36) |
| SPCX ect1 p.3 | [📄 SPCX  p.3](https://agentii.ai/v/SPCX/ect1/3) |
| SPCX sec8 p.35 | [📄 SPCX  p.35](https://agentii.ai/v/SPCX/sec8/35) |
| SPCX ect1 p.2 | [📄 SPCX  p.2](https://agentii.ai/v/SPCX/ect1/2) |
| SPCX sec8 p.43 | [📄 SPCX  p.43](https://agentii.ai/v/SPCX/sec8/43) |
| SPCX sec8 p.46 | [📄 SPCX  p.46](https://agentii.ai/v/SPCX/sec8/46) |
| SPCX sec8 p.47 | [📄 SPCX  p.47](https://agentii.ai/v/SPCX/sec8/47) |
| SPCX sec8 p.42 | [📄 SPCX  p.42](https://agentii.ai/v/SPCX/sec8/42) |
| SPCX sec8 p.30 | [📄 SPCX  p.30](https://agentii.ai/v/SPCX/sec8/30) |
| SPCX sec8 p.31 | [📄 SPCX  p.31](https://agentii.ai/v/SPCX/sec8/31) |
| SPCX sec8 p.32 | [📄 SPCX  p.32](https://agentii.ai/v/SPCX/sec8/32) |
| SPCX sec8 p.40 | [📄 SPCX  p.40](https://agentii.ai/v/SPCX/sec8/40) |
| SPCX sec8 p.5 | [📄 SPCX  p.5](https://agentii.ai/v/SPCX/sec8/5) |
| SPCX sec8 p.37 | [📄 SPCX  p.37](https://agentii.ai/v/SPCX/sec8/37) |
| SPCX sec8 p.11 | [📄 SPCX  p.11](https://agentii.ai/v/SPCX/sec8/11) |
| SPCX sec8 p.44 | [📄 SPCX  p.44](https://agentii.ai/v/SPCX/sec8/44) |
| SPCX sec8 p.55 | [📄 SPCX  p.55](https://agentii.ai/v/SPCX/sec8/55) |
| SPCX sec8 p.13 | [📄 SPCX  p.13](https://agentii.ai/v/SPCX/sec8/13) **(newly surfaced)** |
