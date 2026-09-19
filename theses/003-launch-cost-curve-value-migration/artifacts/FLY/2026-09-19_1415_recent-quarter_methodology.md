---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-5
ticker: FLY
skill: recent-quarter
mode: methodology
generated_at: 2026-09-19T14:15:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07d26b9c738b"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: "|x| absolute-value stripping, not inversion: served = |filed|, magnitude preserved, sign discarded. 4 of 4 quoted periods and 15 of 15 served operating facts positive, FY2023-Q2 2026."
  - da_id: DA-25
    chosen_reading: "normalised per-unit metrics not reproducible from audited tables. The earnings-calendar EPS for FLY reconciles to no filed cell in either period with a directly-read sign; it is a vendor normalisation, not a filed figure."
  - da_id: DA-26
    chosen_reading: "annual figures mislabelled as quarterly. Screened by reconciling every quarterly row against its cumulative and its fiscal-year total. NOT CONFIRMED — every identity closes exactly. FLY is the COUNTEREXAMPLE that falsifies universality."
  - da_id: DA-27
    chosen_reading: "fiscal-period labels derived from the calendar quarter. FLY's fiscal labels are correct; its `report_date` is a release date that drifts into the following calendar quarter. UNEXERCISED as a class (31-Dec filer); the date-keyed detector is refuted."
  - da_id: DA-28
    chosen_reading: "capital-structure discontinuity invalidates share-count and per-share detectors. CONFIRMED — an 11.659x weighted-average share step from a preferred-stock conversion, which inverts the sign of the per-share change against the underlying loss."
  - da_id: DA-29
    chosen_reading: "a reconciliation that closes is not thereby a check. FLY's EPS numerator and denominator bridge close exactly in all four windows; the closure does NOT make the series comparable across the 11.659x step."
  - da_id: DA-30
    chosen_reading: "two bases on one concept collapsed without a basis field. FLY carries THREE bases on EPS — filed $(0.57), platform-served +0.57, earnings-calendar -0.42 — and the third reconciles to neither of the first two."
evidence_grade: DEMONSTRATED
citations:
  - figure: "FLY sec21 p.6"
    ticker: FLY
    citation_id: sec21
    page_no: 6
    url: https://agentii.ai/v/FLY/sec21/6
    located_via: read_source_pages
key_metrics:
  weighted_average_share_step_x: 11.659
  filed_operating_facts_stripped_of_total: "15/15"
  inclusive_opex_overstatement_pct_of_revenue_3m: 79.7
  eps_filed_usd: -0.57
---

# FLY — recent quarter: the counterexample that falsifies DA-26 universality, and an 11.659× share step that no registered detector catches

**All monetary quantities in this artifact are US$ thousands unless labelled otherwise.**
Source: Firefly Aerospace Inc. Form 10-Q for the quarterly period ended 2026-06-30, accession
`0001860160-26-000023`, filed 2026-08-11, 54 pages, `citation_id: sec21`.

## 1. The finding

**FLY is the most valuable issuer in this artifact set precisely because it fails two of the
screens the others pass, in opposite directions.**

1. **DA-26 is NOT CONFIRMED at FLY, and FLY is the counterexample.** Every quarterly row
   reconciles exactly to its own cumulative total and to its own fiscal-year total, across
   FY2024, FY2025 and the two quarters of FY2026, **to the thousand, with no exceptions.** The
   register's "20 issuers tested, 19 exhibiting" must therefore be reported as **19 of 20 — not
   as universal, and not as a rule.** FLY is the falsifying instance.

2. **DA-23 FIRED on 4 of 4 quoted periods and 15 of 15 served operating facts, FY2023–Q2 2026**
   — the widest served operating census in the universe. Every value is `|filed|`. 4 of 4
   flipped on the quoted windows; the component identity closes exactly in all four.

3. **DA-28 CONFIRMED, with the step measured: 11.659×.** Weighted-average shares go from
   13,877 thousand in Q2 2025 to 161,784 thousand in Q2 2026 on a preferred-stock conversion.
   **And the registered EPS-bridge detector does not fire — because a detector that passes on an
   11.7× discontinuity is not a detector.** The proof is arithmetic and is in §4.3: **the
   reported per-share series has the OPPOSITE SIGN to the change in the loss it measures.**

**FLY is also the third measured site of the inclusive-opex failure**, and the worst: the
inclusive reading overstates the operating loss by **79.7% of revenue** in the current quarter.

**One structural consequence for the whole thesis, stated here once:** because FLY's annual
reconciliation *closes*, FLY is the issuer that lets us **distinguish a detector that works from
a detector that happens to pass** — and the DA-28 result shows that the two are different things.

---

## 2. Mode `consolidated-p-and-l` — the DA-23 sign test

### 2.1 Filed cells (verbatim from the statement)

`[📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6)` — Condensed Consolidated Statements of Net
Loss and Comprehensive Loss, unaudited, in thousands except per share amounts.

| Line (US$ thousands) | 3M to 2026-06-30 | 3M to 2025-06-30 | 6M to 2026-06-30 | 6M to 2025-06-30 |
|---|---:|---:|---:|---:|
| Revenue | 117,683 | 15,549 | 198,562 | 71,404 |
| Cost of sales | 93,808 | 11,554 | 157,226 | 65,189 |
| **Gross profit** | **23,875** | **3,995** | **41,336** | **6,215** |
| Research and development | 71,532 | 45,774 | 139,041 | 93,786 |
| Selling, general, and administrative | 47,540 | 12,571 | 93,160 | 25,323 |
| **Total operating expenses** | **119,072** | **58,345** | **232,201** | **119,109** |
| **Loss from operations** | **(95,197)** | **(54,350)** | **(190,865)** | **(112,894)** |
| Total other income (expense), net | 2,843 | (9,428) | 1,902 | (10,977) |
| Loss before (benefit) provision for income taxes | (92,354) | (63,778) | (188,963) | (123,871) |
| **Net loss and comprehensive loss** | **(92,319)** | **(63,778)** | **(188,995)** | **(123,871)** |
| Less: Accretion of dividends of Series C Preferred Stock | — | (5,363) | — | (10,942) |
| Less: Accretion of dividends of Series D-1 Preferred Stock | — | (10,856) | — | (17,465) |
| Less: Accretion of dividends of Series D-3 Preferred Stock | — | (266) | — | (266) |
| **Net loss available to common stockholders** | **(92,319)** | **(80,263)** | **(188,995)** | **(152,544)** |
| **Basic and diluted loss per common share** | **$(0.57)** | **$(5.78)** | **$(1.18)** | **$(11.17)** |
| Weighted-average common shares outstanding (thousands) | 161,784 | 13,877 | 160,711 | 13,659 |

Grade for every cell above: **DEMONSTRATED** (filed figure, read from the statement page).

**Citation-integrity note, because it will bite a spot-checker.** The platform's page for this
statement is `page6`; the **printed folio in the page content reads "5"**. The citation above
follows the platform's `page_no`, which is the convention mandated by the brief. **A reader
navigating the source PDF by its printed footer will land one page off.** Recorded, not
corrected.

**Two structural facts, both load-bearing:**

- **As at RKLB, there is no `Costs and expenses` caption at FLY.** `Cost of sales` sits above
  `Gross profit`; `Total operating expenses` sits below it, in a disjoint section.
- **`Total operating expenses` is again the exact sum of its two components** in all four
  windows: 71,532 + 47,540 = 119,072 ✓; 45,774 + 12,571 = 58,345 ✓; 139,041 + 93,160 = 232,201 ✓;
  93,786 + 25,323 = 119,109 ✓. **The exclusive opex definition is a filed line.**
- **The accretion block switches off entirely at the conversion.** Three preferred series
  accrete $(16,485) in Q2 2025 and $(28,673) in H1 2025; in both 2026 windows the accretion is
  **zero** and net loss equals net loss available to common stockholders exactly. **The
  preferred-stock structure that produced the DA-28 share step is visible on the face of this
  statement, and so is its termination.**

### 2.2 The component identity, with the opex definition stated

**Opex definition used: EXCLUSIVE — `us-gaap:OperatingExpenses`, filed as `Total operating
expenses`** (= `Research and development` + `Selling, general, and administrative`). Cost of
sales is a cost-of-sales line and is **excluded**.

| Period | Gross profit | Opex (exclusive, filed total) | GP − Opex | Filed loss from operations | Verdict |
|---|---:|---:|---:|---:|:--|
| 3M 2026 | **23,875** | **119,072** | **(95,197)** | **(95,197)** | **exact** |
| 3M 2025 | **3,995** | **58,345** | **(54,350)** | **(54,350)** | **exact** |
| 6M 2026 | **41,336** | **232,201** | **(190,865)** | **(190,865)** | **exact** |
| 6M 2025 | **6,215** | **119,109** | **(112,894)** | **(112,894)** | **exact** |

4 of 4 exact. Grade: **DEMONSTRATED** (arithmetic directly on filed cells).

**This is the same result as at RKLB and SPCX: the identity closes exactly, on the exclusive
definition, at every issuer tested. Three issuers, twelve periods, twelve exact closures. The
component identity is not a heuristic here — it is a filed identity, and the only reason it can
be used to *establish* the served magnitudes is that it holds to the filed unit.**

### 2.3 The inclusive reading — refuted, and worst at FLY

| Period | Inclusive construct = Cost of sales + Total operating expenses | GP − inclusive | Filed operating loss | Discrepancy | = cost of sales? |
|---|---:|---:|---:|---:|---|
| 3M 2026 | 93,808 + 119,072 = **212,880** | (189,005) | (95,197) | **93,808** | ✓ exactly |
| 3M 2025 | 11,554 + 58,345 = **69,899** | (65,904) | (54,350) | **11,554** | ✓ exactly |
| 6M 2026 | 157,226 + 232,201 = **389,427** | (348,091) | (190,865) | **157,226** | ✓ exactly |
| 6M 2025 | 65,189 + 119,109 = **184,298** | (178,083) | (112,894) | **65,189** | ✓ exactly |

**The offset equals cost of sales to the unit in all four periods**, and the overstatement is the
largest in this artifact set:

| Period | Overstatement as % of revenue |
|---|---:|
| 3M 2026 | **79.7%** (93,808 / 117,683) |
| 6M 2026 | **79.2%** (157,226 / 198,562) |
| 3M 2025 | **74.3%** (11,554 / 15,549) |
| 6M 2025 | **91.3%** (65,189 / 71,404) |

Grade: **DEMONSTRATED**. **At FLY the inclusive reading does not misstate the operating loss by a
margin — it nearly doubles it.** Three issuers, three measured sites, one structural cause.

### 2.4 Served vs filed — the sign-test verdict

| Concept | Period | Filed | Platform-served | Relation | Verdict |
|---|---|---:|---:|---|:--|
| `OperatingIncomeLoss` | 3M 2026 | (95,197) | **+95,197,000** | served = \|filed\| | **FIRED** |
| `OperatingIncomeLoss` | 6M 2026 | (190,865) | **+190,865,000** | served = \|filed\| | **FIRED** |
| `OperatingIncomeLoss` | 3M 2025 | (54,350) | **+54,350,000** | served = \|filed\| | **FIRED** |
| `OperatingIncomeLoss` | 6M 2025 | (112,894) | **+112,894,000** | served = \|filed\| | **FIRED** |
| `NetIncomeLoss` | 3M 2026 | (92,319) | +92,319,000 | served = \|filed\| | **FIRED** |
| `EarningsPerShareDiluted` | 3M 2026 | (0.57) | **+0.57** | served = \|filed\| | **FIRED** |
| `EarningsPerShareDiluted` | 6M 2026 | (1.18) | **+1.18** | served = \|filed\| | **FIRED** |
| `EarningsPerShareDiluted` | 3M 2025 | (5.78) | **+5.78** | served = \|filed\| | **FIRED** |
| `EarningsPerShareDiluted` | 6M 2025 | (11.17) | **+11.17** | served = \|filed\| | **FIRED** |

**Verdict: DA-23 FIRED. 4 of 4 quoted periods; 9 of 9 quoted facts above; and the full served
operating census is 15 of 15 positive:**

| Period | Served `OperatingIncomeLoss` | Period | Served |
|---|---:|---|---:|
| **FY2023** | **+131,875,000** | 3M 2025 | +54,350,000 |
| FY2024 | +209,453,000 | 6M 2025 | +112,894,000 |
| 9M2024 | +132,235,000 | 9M 2025 | +175,087,000 |
| 6M2024 | +98,041,000 | **FY2025** | **+260,688,000** |
| 3M 2024 | +48,900,000 | 3M 2026 | +95,197,000 |
| 3M 2024 (Q1) | +49,141,000 | 6M 2026 | +190,865,000 |
| 3M 2024 (Q3) | +34,194,000 | Q1 2026 | +95,668,000 |
| Q3 2025 | +62,193,000 | — | — |

**15 of 15 operating facts positive, spanning FY2023 to Q2 2026 — the widest served operating
census in the universe.** All 15 `EarningsPerShareDiluted` facts are likewise positive.

**Additivity holds on the magnitudes**, which is why the defect survives inspection: Q1 2026
95,668 + Q2 2026 95,197 = **190,865** = 6M 2026 ✓. A stripped series that still adds up looks
correct to every check that does not compare it against a filed sub-line.

### 2.5 The DA-30 obligation — three bases on EPS, and the third reconciles to neither

| Basis | Q2 2026 | Q2 2025 | Source |
|---|---:|---:|---|
| Filed, as reported | **$(0.57)** | **$(5.78)** | [📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6) |
| Platform XBRL fact | **+0.57** | **+5.78** | served facts, `fly-20260630.htm` |
| Platform earnings calendar | **-0.42** | **-5.30** | earnings-calendar rows, `fiscal_source: ect_exact` |

**The third basis is not the filed basis with a different sign — it is a different number.**
−0.42 reconciles to no filed cell: the filed numerator $(92,319) over the filed 161,784 thousand
shares is **$(0.57)**, and no share count or numerator on the statement produces $(0.42). **This
is a DA-25-class normalisation** — a per-unit metric not reproducible from audited tables — and
it sits in a field a reader would reasonably take for a filed figure.

---

## 3. Mode `margin-analysis` — the DA-26 / DA-27 period traps

### 3.1 DA-26 — screened by annual reconciliation; **NOT CONFIRMED. FLY is the counterexample.**

**The screen, run as specified.** DA-26 is annual figures mislabelled as quarterly. It is screened
(a) by **reconciling each row against known annual totals** and (b) by **comparing a row's
duration, not its position in the sequence**. At FLY the corpus holds FY2023, FY2024 and FY2025
annual rows (`source_authority: 3`, from Forms 10-K), so both screens can run.

**(a) Duration screen.** Each served fact carries its own `period_start`/`period_end`. Every
`FY20xx` fact spans 1 January → 31 December (12 months); every quarterly fact spans exactly one
calendar quarter (3 months); every `6M`/`9M` fact spans its own duration. **Every label matches
its own duration. No 12-month fact carries a quarterly label.**

**(b) Annual-reconciliation screen.** Each quarterly row is reconciled against its cumulative
and against its fiscal-year total. All figures served magnitudes, sign-neutral, US$ thousands:

| Fiscal year | Q1 | Q2 | 1H (= Q1+Q2) | Q3 | 9M (= 1H+Q3) | FY | FY − 9M (implied Q4) |
|---|---:|---:|---:|---:|---:|---:|---:|
| **2023** | — | — | — | — | — | **131,875** | — |
| **2024** | 49,141 | 48,900 | **98,041 ✓** | 34,194 | **132,235 ✓** | **209,453** | 77,218 |
| **2025** | 58,544 | 54,350 | **112,894 ✓** | 62,193 | **175,087 ✓** | **260,688** | 85,601 |
| **2026** | 95,668 | 95,197 | **190,865 ✓** | — | — | — | — |

**Every cumulative identity closes exactly, in every year, to the thousand. No exceptions.**

**Why this is decisive and not merely negative.** If a single quarterly row carried an annual
figure, its cumulative identity would break: a 12-month number added to a 3-month number cannot
equal a filed 6-month or 9-month total. **Across FY2024, FY2025 and 1H FY2026 — six cumulative
identities — the break never occurs.** FLY is also the only issuer in this artifact set with a
*surviving* FY2023 fact and two full reconciliable fiscal years inside the corpus, so the screen
is exercised harder here than at RKLB and vastly harder than at SPCX, where it cannot run at all.

**Verdict: DA-26 NOT CONFIRMED at FLY. Grade `DEMONSTRATED` — for the negative finding, because
the test was exercised rather than skipped.**

**The reporting consequence, which is the point of this section.** The register's formulation is
**"20 issuers tested, 19 exhibiting."** That is a **19-of-20 base rate, and FLY is the one
non-exhibiting issuer.** It must be carried as a base rate with a named counterexample.
**Reporting DA-26 as universal, or as a rule that can be applied without running the screen,
would be reporting something the corpus refutes.** *A rule with a known exception is a screen;
a rule without one is a substitute for a screen.*

### 3.2 DA-27 — UNEXERCISED as a class, and the date-keyed detector is refuted here

**Verdict on the class: UNEXERCISED.** FLY reports on a 31 December year; a 31-Dec filer has no
fiscal label that can differ from its calendar label. **Not `CLEAR` — inapplicable.** Recorded as
PRESENCE-vs-ABSENCE.

**But FLY is where the date-keyed DA-27 detector demonstrably misfires.** The earnings-calendar
row labelled **`2025 (Q2)`** carries:

| Field | Value |
|---|---|
| `fiscal_quarter` | **2025 (Q2)** — the quarter **ended 2025-06-30** |
| `report_date` | **2025-09-22** — which falls in **calendar Q3** |
| `fiscal_source` | `ect_exact` |
| `revenue_actual` | **15,549,000** |

**A detector that asks "does `report_date` fall inside the labelled fiscal quarter?" fires on
this row — and firing is WRONG.** `report_date` here is an **earnings release date**, and
2025-09-22 is a genuine release date: FLY became a public company in 2025, and its first
post-IPO earnings release for the quarter ended 30 June 2025 fell in September.

**The label is correct, and the correct screen proves it.** The row's `revenue_actual`
**15,549,000** reconciles to the thousand with the filed 3M 2025 revenue of **$15,549 thousand**
[📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6). **The row IS Q2 2025. The reconciliation
establishes it; the date field cannot, and the label alone must not be trusted to.**

**The generalisable rule, and FLY is the clean statement of it:**

- **A `report_date`-keyed DA-27 detector produces a false positive here**, on a row whose label
  the filing confirms.
- **The same detector is a tautology on `sec_grid_lag` rows** (see the RKLB artifact in this
  set), where `report_date` *is* the period end and can never fall outside its own quarter.
- **Therefore no date-keyed and no metadata-keyed DA-27 detector has a valid operating regime.**
  The only admissible screen is **the duration comparison plus reconciliation against filed
  totals** — which is what §3.1 runs, and which is issuer-agnostic.

**Forward rows are a third class and must not be conflated.** FLY's `2026 (Q3)` row carries
`fiscal_source: ect_forward` and null actuals — a scheduled future period, not a mislabelled
past one.

### 3.3 The safe-set margins — and a cost-side result that runs against the growth story

Per thesis 001's ratio audit, **gross margin is SAFE** and **operating margin is UNSAFE from the
metrics block**. Every figure below is rebuilt from the p.6 cells.

| Metric | 3M 2026 | 3M 2025 | 6M 2026 | 6M 2025 |
|---|---:|---:|---:|---:|
| Revenue (US$K) | 117,683 | 15,549 | 198,562 | 71,404 |
| Gross profit (US$K) | 23,875 | 3,995 | 41,336 | 6,215 |
| **Gross margin** | **20.29%** | **25.69%** | **20.82%** | **8.70%** |
| **Operating margin** (rebuilt, filed sign) | **−80.89%** | **−349.54%** | **−96.12%** | **−158.11%** |
| R&D / revenue | **60.78%** | **294.39%** | **70.02%** | **131.35%** |
| Revenue growth YoY | **+656.85%** | — | **+178.08%** | — |

All cells: **DEMONSTRATED** (arithmetic directly on filed p.6 cells). These reproduce thesis
001's peer-bench cells for FLY (20.3% gross margin, −80.9% operating margin, 60.8% R&D/revenue,
+657% growth) from an independent read.

**Two findings here, and the first is adverse to the growth narrative:**

1. **Gross margin COMPRESSED 5.4 points YoY, from 25.69% to 20.29%**, while revenue grew 657%.
   Cost of sales grew **+711.9%** (11,554 → 93,808) against revenue **+656.9%**. **At FLY, the
   scale-up degraded gross margin** — the opposite of the fixed-cost-absorption story. Against
   the 6M comparison the margin *expanded* 12.1 points (8.70% → 20.82%), so **the direction of
   the margin result depends entirely on which window is quoted.** Grade: **DEMONSTRATED** for
   both; the *choice of window* is the analyst's, and quoting one alone would be a basis
   collapse of exactly the DA-30 kind. **Both windows are reported.**
2. **The operating margin from the metrics block would read `+80.89%`** — a profitable company at
   an 80.9% operating margin, with an R&D intensity of 60.8% of revenue, in the correct relative
   rank order against a cohort of loss-makers. **This is the DA-23 failure mode at its most
   extreme in the universe, and it is plausible-but-wrong rather than null.**

---

## 4. Mode `earnings-vs-consensus`

FLY has six earnings-calendar rows. **The revenue series is clean and exact; the EPS series is
`UNRESOLVED` and partially sign-inverted.**

### 4.1 The revenue series — CLEAN, and exact

| Row | `revenue_actual` | Reconciles to | Verdict |
|---|---:|---|:--|
| 2025 (Q2) | 15,549,000 | filed 3M 2025 $15,549K | **exact ✓** |
| 2026 (Q1) | 80,879,000 | — | — |
| 2026 (Q2) | 117,683,000 | filed 3M 2026 $117,683K | **exact ✓** |
| 2026 (Q1)+(Q2) | 198,562,000 | filed 6M 2026 $198,562K | **exact ✓** |

Grade: **DEMONSTRATED**. **The calendar revenue layer reconciles exactly at both horizons —
confirming the SPCX and RKLB result that DA-23 cannot affect revenue, because revenue has no
sign.**

### 4.2 The EPS series — UNRESOLVED, and here is exactly why

| Period | Filed as-reported EPS | Basis of the filed sign | Vendor `eps_actual` | Reconciles? |
|---|---:|---|---:|:--|
| 3M 2026 | **(0.57)** | **read from p.6** | −0.42 | **NO** |
| 3M 2025 | **(5.78)** | **read from p.6** | −5.30 | **NO** |
| 1Q 2026 | (0.61) | DERIVED — served 0.61; no filing read | −0.46 | **NO** |
| 3Q 2025 | (1.50) | DERIVED — served 1.50; no filing read | −1.50 | yes (magnitude) |

**On the two periods where the filed sign was read directly from a filing, the vendor EPS
reconciles in ZERO of two.** Both mismatches are in the *magnitude*, not the sign: −0.42 against
filed $(0.57), and −5.30 against filed $(5.78). **Neither difference is explained by any cell on
the statement.**

**Disposition: `UNRESOLVED`.** The series is (a) not exact — 0 of 2; (b) not stable — it matches
a served magnitude in one of four periods and fails in three; and (c) not consistent with any
formula or filed basis this artifact can identify. **It fails all three limbs of the stability
rule, and it must never be used to repair the XBRL layer.**

**Class: `UNRESOLVABLE-FROM-PLATFORM`.** Every filed as-reported EPS is in the corpus; the vendor
figure is not reproducible from the filings.

### 4.3 DA-28 CONFIRMED — the 11.659× discontinuity, and the detector that does not fire

**The step, measured from the filed statement.** Q2 2025 weighted-average common shares
**13,877 thousand**; Q2 2026 **161,784 thousand**.

**161,784 / 13,877 = 11.659×.** (H1: 160,711 / 13,659 = 11.766×.) Grade: **DEMONSTRATED**.

**Its cause is on the face of the statement:** the three Series C / D-1 / D-3 preferred
accretion lines that consumed $(16,485) thousand in Q2 2025 and $(28,673) thousand in H1 2025
fall to **zero** in both 2026 windows. **The preferred stock converted; the conversion is
visible; the step is not a restatement and not an error.**

**Now the detector test — this is the load-bearing arithmetic.**

| Quantity | Q2 2025 | Q2 2026 | Change |
|---|---:|---:|---:|
| Net loss available to common stockholders (US$K) | (80,263) | (92,319) | **+15.02% wider** |
| Weighted-average shares (thousands) | 13,877 | 161,784 | **11.659×** |
| **Reported EPS, as filed** | **$(5.78)** | **$(0.57)** | **90.14% SMALLER per-share loss** |
| **Constant-share counterfactual** (grade `MODELED`) | $(5.78) | **$(6.65)** | **+15.1% WIDER per-share loss** |

The constant-share counterfactual is $(92,319) / 13,877 = **$(6.65)** per share, and it is
**`MODELED`** — a derivation, and per P4 **a `MODELED` input can never satisfy a falsifier**. It
is used here for exactly one purpose, which it is sufficient for: **to show the direction of the
reported series is an artefact of the denominator.**

**The result: the reported per-share series and the underlying loss change have OPPOSITE SIGNS.**
The loss available to common stockholders grew **+15.0%**; the reported loss per share shrank
**90.1%**; the constant-share per-share loss grew **+15.1%**. **The entire discrepancy is the
11.659× share step.**

**And the platform's own year-over-year field confirms the inversion without flagging it.**
The Q2 2026 row carries `eps_yoy_change_pct: 0.920754716981132` — **+92.1%**, computed from
`eps_prior_year: -5.3` to `eps_actual: -0.42` as (5.30 − 0.42) / 5.30 = 0.9208 ✓. **A +92.1%
"improvement" is reported for a company whose loss available to common stockholders grew 15.0%
in the same quarter.**

**The registered EPS-bridge detector does not fire.** It is presented the numerator
(92,319 vs 80,263), the denominator (161,784 vs 13,877) and the reported per-share figures
(0.57 vs 5.78), and **all four numbers are internally consistent in both periods:**

- 80,263 / 13,877 = **5.784** → filed $(5.78) ✓
- 92,319 / 161,784 = **0.571** → filed $(0.57) ✓

**Both bridges close exactly.** There is nothing for a closure-based detector to catch, because
**the numbers are not wrong — the series is not comparable.** Per **DA-29**, *a reconciliation
that closes is not thereby a check*, and this is the cleanest instance of that rule in the
corpus: **the EPS bridge closes perfectly on both sides of an 11.7× discontinuity.**

> **A detector that passes on an 11.7× discontinuity is not a detector.**

**What a working detector requires, stated so the next artifact can use it:** the denominator
must be **reconciled across the comparison boundary** before any per-share series is read, and
the accretion block's termination (§2.1) is the filed signal that the boundary is there.
**FLY's own statement discloses everything needed. The detector was not looking at the
denominator.**

**Wider relevance beyond FLY.** The same discipline applies to the *cumulative* EPS series at
FLY, where it produces an unmistakable signature: **FY2025 EPS $(4.83) is SMALLER in magnitude
than 9M 2025 EPS $(7.25)**, even though the FY2025 operating loss (260,688) exceeds the 9M 2025
operating loss (175,087) by the Q4 loss of 85,601. **On a stable denominator, a cumulative loss
series grows; this one shrinks.** That signature is cheap to compute from the served series and
**it is the check that should have fired.**

---

## 5. What this artifact could not resolve

| # | Unresolved | Class | The disclosure that would resolve it |
|---|---|---|---|
| 1 | **Vendor EPS basis at FLY** — 0 of 2 on directly-read signs | **`UNRESOLVABLE-FROM-PLATFORM`** | Every filed as-reported EPS is in the corpus; the vendor figure is not reproducible from any filed cell. |
| 2 | **1Q 2026 and 3Q 2025 filed EPS signs** — served magnitudes only | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** (in this artifact's scope) | The 1Q 2026 and 3Q 2025 10-Qs. Present in the corpus; not read here. **Recorded as `UNEXERCISED`, not filled in by inference.** |
| 3 | **Standalone Q4 for any year** — the Q4 hole | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** | No 31-Dec filer files a Q4 10-Q. Derivable only as `FY − 9M` (implied Q4 2024 = 77,218; Q4 2025 = 85,601). Per **DA-29**, a reconciliation that closes is not thereby a check. |
| 4 | **DA-27 at FLY** | n/a (`UNEXERCISED`) | Nothing. A 31-Dec filer has no fiscal label that can differ from its calendar label. |
| 5 | **Accretion-block termination date** — the exact conversion date within FY2025 | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** (in this artifact's scope) | The preferred-stock conversion is disclosed in the 3Q 2025 or FY2025 equity note. **Its absence does not affect §4.3: the step is measured from the filed weighted-average share counts, which is sufficient for the finding.** |
| 6 | **The printed-folio / platform-page offset on the statement page** | **`UNRESOLVABLE-FROM-PLATFORM`** | Nothing available. The citation follows the platform `page_no`, per the brief's mandated form. |

---

## 6. Carry-forwards

1. **DA-26 is NOT CONFIRMED at FLY, and FLY is the counterexample.** Every cumulative identity
   closes exactly across FY2024, FY2025 and 1H FY2026. **Report the register's result as 19 of
   20 with FLY named — never as universal, and never as a rule that can be applied without
   running the screen.**
2. **DA-23 FIRED at FLY: 4 of 4 quoted periods, 15 of 15 served operating facts, FY2023–Q2 2026**
   — the widest census in the universe. Magnitudes correct; **derive the sign**.
3. **The component identity closes exactly, 4 of 4, on `gross profit − Total operating expenses`.**
   FLY files **no** inclusive `Costs and expenses` total; the inclusive reading is a
   platform-constructed sum, false by **exactly cost of sales** (93,808 / 11,554 / 157,226 /
   65,189), overstating the operating loss by **74.3%–91.3% of revenue**.
4. **DA-28 CONFIRMED: 11.659× (161,784 / 13,877), from a preferred-stock conversion whose
   termination is visible on the face of the statement** (accretion $(16,485) and $(28,673) →
   zero). **The registered EPS-bridge detector does not fire, because both bridges close
   exactly.** The reported per-share series moves 90.1% *down* while the underlying loss moves
   15.0% *up*. **A detector that passes on an 11.7× discontinuity is not a detector** — reconcile
   the denominator across the boundary before reading any per-share series.
5. **The cumulative-EPS signature is the cheap check that should have fired:** FY2025 EPS
   $(4.83) is smaller in magnitude than 9M 2025 EPS $(7.25) while the FY loss exceeds the 9M loss.
   **On a stable denominator a cumulative loss series grows. This one shrinks.**
6. **DA-27 UNEXERCISED at FLY (31-Dec filer) and the date-keyed detector is REFUTED here.** The
   `2025 (Q2)` row's `report_date` 2025-09-22 falls in calendar Q3 and the row is nonetheless
   correct — proven by its revenue reconciling to the filed $15,549 thousand. **No date-keyed
   and no metadata-keyed DA-27 detector has a valid operating regime.**
7. **FLY's gross margin COMPRESSED 5.4 points YoY (25.69% → 20.29%)** while revenue grew 657%,
   and **expanded** 12.1 points on the 6M comparison. **The direction of the margin result
   depends on the window; both windows are reported.** Cost of sales grew +711.9% against
   revenue +656.9%.
8. **The earnings-calendar revenue layer is CLEAN and exact; the EPS layer is `UNRESOLVED`.**
   **Reconcile each field of a calendar row separately — one row can carry both a checked and an
   unchecked figure.**
9. **`EPS × shares` remains inadmissible as a sign test** — and FLY is the proof of both reasons
   at once: the sign is stripped in one layer, and the share count steps 11.659× in the same
   comparison window.
10. **The stability rule applied throughout.** Every identification here is (a) exact, (b) stable
    across periods, and (c) consistent with a specified formula or a filed basis — or it is marked
    `UNRESOLVED`/`UNEXERCISED`. **FLY is the issuer that shows why the rule is stated that way:
    its numbers reconcile perfectly, and reconciling perfectly was not the same as being
    comparable. The dangerous failure mode is plausible-but-wrong, not null.**
