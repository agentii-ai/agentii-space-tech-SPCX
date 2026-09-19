---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-5
ticker: SATS
skill: recent-quarter
mode: methodology
generated_at: 2026-09-19T14:15:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07d26b9c738b"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "the platform serves a filed negative as a positive of identical magnitude (|x|, not inversion), PER-FACT and not per-period. CONFIRMED at SATS on four independent axes: 9 of 9 served `operating_income` values for loss periods are stripped while the 1 genuine profit period is clean, and 12 of 12 served-negative subtotals strip across the row layer against 8 of 8 positives clean. Applied everywhere below: every figure I read from the platform is checked against the filed sign on a statement face or against an issuer reconciliation that forces the sign."
  - da_id: "DA-24"
    chosen_reading: "non-operating contamination of `operating_income`. THE DEFINING INSTANCE IS AN INVERTED IMPAIRMENT, NOT A GAIN: the Q3 2025 event is a non-cash 5G-Network impairment CHARGE of $16,481,468 thousand, the spectrum licences remain on the balance sheet, nothing has closed, and therefore NO gain is recognised. The widely-quoted entry was named for a gain and the thing it is named after is a loss."
  - da_id: "DA-26"
    chosen_reading: "annual figures mislabelled as quarterly, keyed on `fiscal_period = calendar_quarter(period_end)`. CONFIRMED at SATS three times: the FY2025, FY2024 and FY2023 Q4 rows each carry a twelve-month figure in every field. The trap is not cosmetic — the 118.1% term in the widely-quoted margin series IS the FY2025 annual margin, a DA-26 instance sitting inside a DA-24 exhibit."
  - da_id: "DA-27"
    chosen_reading: "fiscal-period labels synthesised from the calendar quarter. SATS' fiscal year IS the calendar year (December year-end), so no label offset applies — but the synthesis is the MECHANISM that hides the mislabelled Q4 rows, since a 12-month period ending 2025-12-31 is keyed Q4 by construction. Applied: I take every period label from the filing's own column header, never from the platform's `fiscal_period`."
  - da_id: "DA-28"
    chosen_reading: "capital-structure discontinuity around an IPO invalidates share-count detectors. NOT APPLICABLE to the share counts used here — four filed share counts (Q1 2026 289,014; Q1 2025 286,513; FY2025 287,589; Q3 2025 288,051) are used only as cross-checks on derived EPS and no detector rests on them; the Q4 2025 weighted count of 282,713 thousand implied by the $−4.27 EPS versus a derived $(1,207,183) thousand net loss is an ORDER-OF-MAGNITUDE cross-check, not a detector."
  - da_id: "DA-29"
    chosen_reading: "a reconciliation that closes is not thereby a check; `computed` is an opaque assertion, and if a term appears nowhere in the source the check is a back-solve. CONFIRMED at SATS IN A NEW KIND: `validate_calculation` runs and returns `status: pass` on a value whose sign is wrong (ProfitLoss Q3 2025 computed = reported = 12,781,348,000, diff 0, pass, against a filing printing $(12,781,348) thousand), because its `reported` column draws from the same stripped store. No `computed` value is cited as a derivation anywhere in this artifact."
  - da_id: "DA-30"
    chosen_reading: "two bases on one concept collapsed without a basis field. FOUR live instances at SATS, all carried with both bases named at every use: (1) the caption-vs-content cost grouping (D&A-inclusive 3,274,642 vs the caption's asserted exclusive basis 3,108,041); (2) net income consolidated (147,300) vs attributable (146,885), served from two platform surfaces under one undimensioned idea; (3) the spectrum asset on two bases in one table ($29,614,839 tranche subtotal vs $34,550,802 fully loaded); (4) segment vs consolidated (operating income 392,674 vs 392,847; revenue 3,677,394 vs 3,667,489)."
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
citations:
  - figure: "SATS sec121 p.11"
    ticker: SATS
    citation_id: sec121
    page_no: 11
    url: https://agentii.ai/v/SATS/sec121/11
    located_via: read_source_pages
  - figure: "SATS sec85 p.150"
    ticker: SATS
    citation_id: sec85
    page_no: 150
    url: https://agentii.ai/v/SATS/sec85/150
    located_via: read_source_pages
  - figure: "SATS sec121 p.108"
    ticker: SATS
    citation_id: sec121
    page_no: 108
    url: https://agentii.ai/v/SATS/sec121/108
    located_via: read_source_pages
  - figure: "SATS sec120 p.10"
    ticker: SATS
    citation_id: sec120
    page_no: 10
    url: https://agentii.ai/v/SATS/sec120/10
    located_via: read_source_pages
  - figure: "SATS sec85 p.76"
    ticker: SATS
    citation_id: sec85
    page_no: 76
    url: https://agentii.ai/v/SATS/sec85/76
    located_via: read_source_pages
  - figure: "SATS sec121 p.46"
    ticker: SATS
    citation_id: sec121
    page_no: 46
    url: https://agentii.ai/v/SATS/sec121/46
    located_via: read_source_pages
  - figure: "SATS sec121 p.14"
    ticker: SATS
    citation_id: sec121
    page_no: 14
    url: https://agentii.ai/v/SATS/sec121/14
    located_via: read_source_pages
  - figure: "SATS sec121 p.15"
    ticker: SATS
    citation_id: sec121
    page_no: 15
    url: https://agentii.ai/v/SATS/sec121/15
    located_via: read_source_pages
  - figure: "SATS sec121 p.16"
    ticker: SATS
    citation_id: sec121
    page_no: 16
    url: https://agentii.ai/v/SATS/sec121/16
    located_via: read_source_pages
  - figure: "SATS sec121 p.25"
    ticker: SATS
    citation_id: sec121
    page_no: 25
    url: https://agentii.ai/v/SATS/sec121/25
    located_via: read_source_pages
  - figure: "SATS sec121 p.71"
    ticker: SATS
    citation_id: sec121
    page_no: 71
    url: https://agentii.ai/v/SATS/sec121/71
    located_via: read_source_pages
  - figure: "SATS sec121 p.13"
    ticker: SATS
    citation_id: sec121
    page_no: 13
    url: https://agentii.ai/v/SATS/sec121/13
    located_via: read_source_pages
  - figure: "SATS sec120 p.12"
    ticker: SATS
    citation_id: sec120
    page_no: 12
    url: https://agentii.ai/v/SATS/sec120/12
    located_via: read_source_pages
  - figure: "SATS sec85 p.152"
    ticker: SATS
    citation_id: sec85
    page_no: 152
    url: https://agentii.ai/v/SATS/sec85/152
    located_via: read_source_pages
  - figure: "SATS sec85 p.157"
    ticker: SATS
    citation_id: sec85
    page_no: 157
    url: https://agentii.ai/v/SATS/sec85/157
    located_via: read_source_pages
key_metrics:
  operating_margin_q1_2026_pct: 10.71
  operating_margin_q1_2026_ex_impairment_credit_pct: 8.91
  impairment_credit_q1_2026_usd_thousands: 66159
  operating_margin_q3_2025_pct: -460.45
---

# SATS — the quarterly series, corrected

**The headline.** SATS is the most defect-dense series in the universe, and the defects are not
scattered — they stack on one five-quarter window. The widely-quoted margin progression
`2.3 / 5.7 / 460.5 / 118.1 / 10.7` is wrong in **four of five terms**, and wrong in a specific,
reproducible way: **the first three are the absolute values of losses** (DA-23 sign stripping),
**the fourth is not a quarter at all** — 118.1% is the **FY2025 ANNUAL** margin sitting on a row
labelled Q4 (DA-26) — and the fifth, while arithmetically correct, **carries a one-off impairment
credit and overstates the underlying run rate by 1.80 percentage points** (10.71% → 8.91%).

**The corrected operating-margin series (all DEMONSTRATED, arithmetic on filed cells):**

| Quarter | Revenue ($k) | Operating income (loss) ($k) | Corrected margin | Widely quoted |
|---|---:|---:|---:|---:|
| Q1 2025 | 3,869,758 | **(88,132)** | **(2.28)%** | 2.3% |
| Q2 2025 | 3,724,959 | **(213,408)** | **(5.73)%** | 5.7% |
| Q3 2025 | 3,614,258 | **(16,641,875)** | **(460.45)%** | 460.5% |
| Q4 2025 | 3,796,014 | **(779,731)** | **(20.54)%** | 118.1% ← *not a quarter* |
| Q1 2026 | 3,667,489 | **392,847** | **+10.71%** | 10.7% |
| Q1 2026 ex-item | 3,667,489 | **326,688** | **+8.91%** | — |

Four of the five quoted terms are losses printed as gains; the fifth is a twelve-month figure
printed as a quarter. There is no quarter in this window in which SATS' operating margin was
between 0% and 460% *and* positive, except Q1 2026 — and that one carries an impairment credit.

---

## 1. `consolidated-p-and-l` — the component identity, and the DA-23 sign test

### 1.1 The identity and the opex definition

**SATS files NO gross-profit line on any statement face.** The Q1 2026 statement of operations runs
*Total revenue → Costs and Expenses → Total costs and expenses → Operating income (loss)*, with
`Cost of services` and `Cost of sales - equipment and other` as the first two cost lines and no
gross-profit subtotal anywhere
([📄 SATS 10-Q p.11](https://agentii.ai/v/SATS/sec121/11)); the FY2025 statement is the same shape
([📄 SATS 10-K p.150](https://agentii.ai/v/SATS/sec85/150)). A `GrossProfit` XBRL query returns
zero facts — but **a zero-fact return is evidence about the CONCEPT NAME, not about the ISSUER**, so
the absence is established by reading the face, not by the zero return.

The operable identity is therefore:

```
Total revenue  −  Total costs and expenses  =  Operating income (loss)
```

**Opex definition used: the D&A-INCLUSIVE `Total costs and expenses` basis** (the tagged total,
3,274,642 at Q1 2026). This is a DA-30 choice and both bases are named here, because the statement
groups its cost lines under the caption **"Costs and Expenses (exclusive of depreciation and
amortization)"** and then includes a `Depreciation and amortization` line **inside** that group:

| Basis | Q1 2026 total costs and expenses | Identity result | What it actually is |
|---|---:|---:|---|
| **D&A-inclusive** (tagged total) | **3,274,642** | 3,667,489 − 3,274,642 = **392,847** ✓ | **Operating income (loss)** |
| D&A-exclusive (caption's asserted basis) | 3,108,041 | 3,667,489 − 3,108,041 = 559,448 | **OIBDA — NOT operating income** |

The exclusive basis differs from the inclusive by exactly the quarterly D&A of **166,601**
([📄 SATS 10-Q p.108](https://agentii.ai/v/SATS/sec121/108)). **A reader who takes the caption at
face value computes OIBDA and mislabels it operating income — a 166,601 thousand error, 42% of the
reported operating result.** Basis quoted throughout: **D&A-inclusive**.

### 1.2 The identity closes 6 of 6, including the derived quarter

| Period | Total revenue | Total costs and expenses | Operating income (loss) | Closes? |
|---|---:|---:|---:|:--:|
| Q1 2026 | 3,667,489 | 3,274,642 | 392,847 | ✓ |
| Q4 2025 *(derived)* | 3,796,014 | 4,575,745 | **(779,731)** | ✓ |
| Q3 2025 | 3,614,258 | 20,256,133 | (16,641,875) | ✓ |
| FY2025 | 15,004,989 | 32,728,135 | (17,723,146) | ✓ |
| FY2024 | 15,825,516 | 16,129,586 | (304,070) | ✓ |
| FY2023 | 17,015,598 | 17,293,507 | (277,909) | ✓ |

Cells: [p.11](https://agentii.ai/v/SATS/sec121/11) and [p.10](https://agentii.ai/v/SATS/sec120/10)
and [p.150](https://agentii.ai/v/SATS/sec85/150). **The identity is not the problem. The store is.**
[DEMONSTRATED]

The Q4 2025 column is derived by subtraction from the filed FY2025 and nine-month columns:
revenue 15,004,989 − 11,208,975 = **3,796,014**; total costs and expenses 32,728,135 − 28,152,390 =
**4,575,745**; operating loss 17,723,146 − 16,943,415 = **(779,731)**. Q4 2025 revenue is
**independently confirmed** by the consensus feed's Q4 2025 revenue actual, which is also 3,796,014.
[DEMONSTRATED]

### 1.3 The DA-23 sign test — CONFIRMED 12/12 and 9/9, on four independent axes

**Axis 1 — the served row layer against the statement face.** Every `operating_income` value the
platform serves for SATS' loss periods is a positive of identical magnitude; the single genuine
profit period is served correctly.

| Row served | Served `operating_income` | Filed | Verdict |
|---|---:|---:|:--|
| FY2026 Q1 | +392,847 | +392,847 | **CLEAN** |
| FY2025 Q4 | +17,723,146 | (17,723,146) | **STRIPPED** (+ annually mislabelled) |
| FY2025 Q3 | +16,641,875 | (16,641,875) | **STRIPPED** |
| FY2025 Q2 | +213,408 | (213,408) | **STRIPPED** |
| FY2025 Q1 | +88,132 | (88,132) | **STRIPPED** |
| FY2024 Q4 | +304,070 | (304,070) | **STRIPPED** (+ annually mislabelled) |
| FY2024 Q3 | +160,767 | (160,767) | **STRIPPED** |
| FY2024 Q2 | +65,369 | (65,369) | **STRIPPED** |
| FY2024 Q1 | +15,244 | (15,244) | **STRIPPED** |
| FY2023 Q4 | +277,909 | (277,909) | **STRIPPED** (+ annually mislabelled) |

**9 of 9 served losses stripped, 1 of 1 served profit clean, zero unexplained.** Across the whole
row layer the count is **12 of 12 served-negative subtotals stripped against 8 of 8 positives
clean**. [DEMONSTRATED]

**Axis 2 — the period-sum fingerprints, which are independent of how parentheses are read.** Two
nine-month columns reconstruct **exactly** from their quarters *only* with the filed negative signs:

- 9M2024: 15,244 + 65,369 + 160,767 = **241,380** = the filed **9M2024 operating income** column ✓
- 9M2025: 88,132 + 213,408 + 16,641,875 = **16,943,415** = the filed **9M2025 operating loss** ✓

The second fingerprint also **confirms the derived Q2 2025 operating loss of (213,408)** — a value I
derived from the nine-month and full-year columns before reading it back from the served row.
[DEMONSTRATED]

**Axis 3 — the issuer's own reconciliation forces the sign.** The Segment Adjusted OIBDA bridge
([📄 SATS 10-Q p.108](https://agentii.ai/v/SATS/sec121/108)) bridges OIBDA 559,448 to Adjusted OIBDA
493,289 by exactly one term, "Impairments and other", printed as **(66,159)**:

```
559,448 − 66,159 = 493,289   ✓  the filed Adjusted OIBDA
559,448 + 66,159 = 625,607   ✗  appears NOWHERE in the filing
```

**The reconciliation only closes if the term is negative.** The served `+66,159,000` is therefore
demonstrably wrong independently of how the parentheses are read, and independently of any
screen-scrape. [DEMONSTRATED]

**Axis 4 — the platform contradicts itself on the same cells.** The consensus feed carries SATS'
signs **correctly** (−44.37, −4.27, −0.51) while the platform's own row layer serves the identical
periods stripped (+44.37, +50.41, +0.51). Two platform surfaces, one period, opposite signs — so
this is not an artefact of my reading. [DEMONSTRATED]

**Row-layer EPS is stripped in 10 of 10 periods** — every served EPS is positive against a filing in
which every period in the window is a loss. Note the trap: those stripped EPS values are *larger*
than the losses in several rows (e.g. FY2025 Q4 EPS served as +50.41), which is the signature of an
absolute value taken on a loss divided by a *shrinking* share count — not of a profit.

### 1.4 DA-23 is a LAYER property, not a data property

Axis 4 above is not an oddity, it is the **shape of the defect**, and it must be stated as such.
DA-23 does not live in the data and it does not live in the issuer: it lives in **one layer of the
platform**, and the layers disagree with each other on the **same metric and the same period**:

| Layer | Same metric, same period | Sign served | Filed |
|---|---|---|---|
| **Earnings-calendar** | SATS Q3 2025 EPS actual **−44.37** | **correct** | loss ✓ |
| **Earnings-calendar** | SATS Q4 2025 EPS actual **−4.27** | **correct** | loss ✓ |
| **Earnings-calendar** | SATS Q1 2026 EPS actual **−0.51** | **correct** | loss ✓ |
| **Row / XBRL fact** | SATS Q3 2025 EPS served **+44.37** | **stripped** | loss |
| **Row / XBRL fact** | SATS Q4 2025 EPS served **+50.41** | **stripped** + annually mislabelled | annual loss |
| **Row / XBRL fact** | SATS Q1 2026 EPS served **+0.51** | **stripped** | loss |
| **Row / XBRL fact** | Q3 2025 `operating_income` served **+16,641,875** | **stripped** | (16,641,875) |
| **Validator** | `ProfitLoss` computed = reported = **12,781,348,000**, diff 0, **pass** | **stripped** | $(12,781,348)$ |

**NEITHER LAYER CAN REPAIR THE OTHER.** A reader who checked SATS' signs against the consensus feed
would find every negative served correctly and conclude the store is sound; the same reader checking
the income-statement rows would find nine stripped losses in one window. Both are reading the same
platform on the same day. **A clean reading from one surface is not evidence about the other** — and
the word *layer* is load-bearing precisely because the surfaces are demonstrably independent, which
is what makes their disagreement admissible evidence rather than a curiosity.

**One refinement, established across the three P11 issuers, and it cuts the other way too:** the
calendar layer carries the **sign**, not necessarily the **magnitude**. At SATS the two layers agree
on magnitude for Q3 2025 (44.37 both) and Q1 2026 (0.51 both) but **diverge on Q4 2025** — the row
serves **+50.41** (the FY2025 *annual* loss per share, a DA-26 substitution) where the calendar
serves **−4.27** (the *quarter*). Two defects stacked on one cell: the sign is stripped *and* the
period base is the annual. **Use the calendar layer for the sign; never for the magnitude, and never
for the period basis.** [DEMONSTRATED]

---

## 2. `margin-analysis` — where the DA-26 / DA-27 period traps bite

### 2.1 The 118.1% term is not a quarter

The widely-quoted series' fourth term, **118.1%**, is **SATS' FY2025 ANNUAL operating margin**:

```
−17,723,146  ÷  15,004,989  =  118.11%      FY2025 twelve-month figures
```

It is served on a row keyed **FY2025 Q4** whose every field is the FY2025 annual statement:
revenue 15,004,989 (= the annual), operating income 17,723,146 (= |the annual loss|), net income
14,497,180 (= the annual loss attributable), EPS 50.41 (= the annual loss per share). **Four
independent twelve-month figures on one "quarterly" row.** Same defect on FY2024 Q4 (15,825,516 /
304,070 / 0.44) and FY2023 Q4 (17,015,598 / 277,909 / 6.28).

**Annual-to-quarter multipliers on the derived quarters:** FY2025 15,004,989 ÷ 3,796,014 = **3.95×**;
FY2024 15,825,516 ÷ 3,890,984 = **4.07×**; FY2023 17,015,598 ÷ 4,014,843 = **4.24×**. A genuine
quarterly reading would require a 4× sequential jump. [DEMONSTRATED]

**The nesting is the point.** DA-26 does not merely sit beside DA-24 — the 118.1% term is a **DA-26
instance inside a DA-24 exhibit**. A reader who takes the published series as a quarterly margin
progression is reading a twelve-month margin as the fourth of five quarters, in a window where the
other four are sign-stripped losses. The two defects interlock to produce a series whose *signs*,
*periods* and *magnitudes* are all wrong at once.

### 2.2 DA-27 — why the mislabelling is invisible

DA-27's mechanism is that the fiscal-period label is **synthesised from the calendar quarter** of the
period end. SATS' fiscal year *is* the calendar year, so no label offset applies — which is exactly
why the defect survives: a twelve-month period ending 2025-12-31 is keyed `Q4` by construction, and
nothing in the key distinguishes it from a three-month period ending the same day.

**Applied throughout: every period label in this artifact is taken from the filing's own column
header** ("Three Months Ended March 31, 2026", "Year Ended December 31, 2025"), **never** from the
platform's `fiscal_period`. SATS' relative fiscal-period format is `Q1…Q4` / `FY` on the calendar
year, verified against the filing dates.

### 2.3 The ex-item correction: 10.71% is arithmetically right and materially wrong

The Q1 2026 margin of **10.71%** is correct as filed — it is the one term in the published series
that reproduces from a genuine quarter. But it carries a **one-off impairment CREDIT of 66,159**
(axis 3 above), which is 1.80 percentage points of the 10.71%:

```
392,847 − 66,159 = 326,688        326,688 ÷ 3,667,489 = 8.91%
```

**Corrected: +8.91% ex-item.** [DEMONSTRATED] The unadjusted 10.71% overstates the quarter's
underlying operating rate by **1.80 points**, and it is the *only* term in the published series a
reader could reasonably have quoted.

---

## 3. `earnings-vs-consensus`

| Period | Reported | EPS actual | EPS est. | Revenue actual ($k) | Revenue est. ($k) | Revenue surprise |
|---|---|---:|---:|---:|---:|---:|
| Q3 2025 | 2025-11-06 | **−44.37** | −1.21 | 3,614,258 | 3,732,766 | **−3.17%** |
| Q4 2025 | 2026-03-02 | **−4.27** | −0.93644 | 3,796,014 | 3,766,687 | **+0.78%** |
| Q1 2026 | 2026-05-11 | **−0.51** | −0.47828 | 3,667,489 | 3,650,024 | **+0.48%** |
| Q2 2026 | 2026-08-07 | **null** | −0.02 | null | — | — |
| Q3 2026 | *2026-11-11 (upcoming)* | — | −0.12 | — | — | — |

Source: `search_earnings_calendar`, latest page (the calendar paginates **oldest-first** — page 1
returns 2005-2010 rows; the 2025-2026 rows are on the last page of 10). [DEMONSTRATED]

Three points carry:

1. **The consensus feed is the only platform surface that gets SATS' signs right.** Q3 2025 EPS
   actual **−44.37** against an estimate of **−1.21** — a **36.7×** miss, and the absolute value of
   the same figure the row layer serves as **+44.37**. The consensus line is the independent
   arbitration between the row layer and the filing, and it sides with the filing every time.
2. **The Q4 2025 revenue actual, 3,796,014, is an independent confirmation of my derived Q4
   revenue** to the thousand — it is not a figure the row layer serves at all.
3. **Q3 2025's estimate did not anticipate the impairment** (est −1.21 vs actual −44.37). Anyone
   reading the consensus line as a "beat/miss" series rather than a raw sign carrier would read the
   largest single-quarter loss in the window as an 36.7× *miss on an operating basis* — when it is
   an impairment charge that the estimate set did not model.

**Coverage gap, not a zero:** Q2 2026 (reported 2026-08-07) carries `actual: null` on both EPS and
revenue. A null is an absence of ingestion, not a reported zero, and must not be read as one.

---

## 4. DA-24 — the defining instance is an INVERTED IMPAIRMENT, not a gain

**The event.** A non-cash **5G-Network impairment CHARGE of $16,481,468 thousand** — Wireless
16,199,344 + Broadband and Satellite Services 282,124 — taken in Q3 2025 and triggered by the AT&T
and SpaceX transactions. The FY2025 10-K's MD&A records the year's charges directly: *"we recorded a
total charge of $17.632 billion, $16.481 billion and $1.151 billion during the third and fourth
quarters of 2025, respectively"*
([📄 SATS 10-K p.76](https://agentii.ai/v/SATS/sec85/76)). [DEMONSTRATED]

**The naming failure, which is the whole finding.** The widely-quoted entry for this event was named
for a **gain**. The thing it is named after is a **loss**:

- **No gain is recognised, because nothing has closed.** The spectrum licences remain on SATS' own
  balance sheet at 2026-03-31 — **$34,550,802 thousand** fully loaded ($29,614,839 tranche subtotal +
  $10,270,436 capitalised interest − $5,334,473 accumulated impairment)
  ([📄 SATS 10-Q p.46](https://agentii.ai/v/SATS/sec121/46)). The AT&T-transaction licences (600 MHz
  $6,449,578; 3.45–3.55 GHz $7,199,380) are still listed as the company's own.
- **All AT&T took was a short-term spectrum manager lease.** *"AT&T, subject to a short-term
  spectrum manager lease, exercised its right to lease certain 3.45 GHz licenses from us"* — filed
  both at [p.14](https://agentii.ai/v/SATS/sec121/14) and in note (2) at
  [p.46](https://agentii.ai/v/SATS/sec121/46). That lease is precisely why the licences stay on the
  balance sheet at all.
- **Both transactions were still pending** FCC and DOJ approval; the AT&T closing was expected in
  H1 2026, the SpaceX Spectrum Transfer Closing in H1 2026 and the Spectrum Acquisition Closing on or
  about 2027-11-30 ([p.15](https://agentii.ai/v/SATS/sec121/15),
  [p.16](https://agentii.ai/v/SATS/sec121/16)).

**The structural shape:** DA-24 is registered as *non-operating contamination of operating income*.
At its own defining instance the contamination is present **with the opposite sign** — the
operating-income collapse of (16,641,875) in Q3 2025 is a non-cash **charge inside** the operating
line, not a gain below it. The register's entry points at a gain; the exhibit is a loss. **The entry
was named for a gain and the thing it is named after is a loss.** [DEMONSTRATED]

---

## 5. Second-order contamination — the add-back-only normalisation still flatters FY2026

**This is the finding that survives the ex-item correction, and it is the reason the 8.91% figure
above is not a clean number either.**

The Q1 2026 year-over-year operating-income improvement is **+480,979 thousand** (from (88,132) to
392,847). Decomposed exactly, from the issuer's own segment bridge on
[📄 SATS 10-Q p.108](https://agentii.ai/v/SATS/sec121/108), using
`Operating income = Adjusted OIBDA − D&A − Impairments and other`:

| Component | Amount ($k) | Share of the improvement |
|---|---:|---:|
| **Depreciation and amortisation relief** | **+321,732** | **66.88%** |
| Impairments and other (the Q1 2026 credit) | **+66,159** | **13.76%** |
| All other operating factors | +93,088 | 19.36% |
| **Total** | **+480,979** | **100.00%** ✓ |

**⚠️ CORRECTION TO CARRY.** The inherited formulation — *"the Q1 2026 YoY improvement is **80.6%** D&A
relief plus the credit"* — is arithmetically exact but mis-assigned: **80.64% is the D&A relief and
the credit COMBINED** (321,732 + 66,159 = 387,891 ÷ 480,979 = **80.64%**). The D&A relief **alone is
66.88%**; the credit **alone is 13.76%**. The residual organic component is **19.36%**. Reading
80.6% as the D&A share overstates the D&A mechanism and understates the credit's contribution by
13.8 points of the improvement. [DEMONSTRATED]

**And the D&A relief is a PERMANENT reset, not a one-off.** Like-for-like, three months versus three
months, from the same table:

| D&A, three months ended March 31 | Q1 2025 ($k) | Q1 2026 ($k) | Change |
|---|---:|---:|---:|
| Pay-TV | 76,443 | 55,866 | −26.9% |
| Wireless | 20,187 | 49,499 | +145.2% |
| Broadband and Satellite Services | 104,898 | 49,940 | −52.4% |
| **Other** | **303,929** | **11,305** | **−96.28%** |
| Eliminations | (17,124) | (9) | — |
| **Consolidated** | **488,333** | **166,601** | **−65.88%** |

The Other segment alone accounts for **292,624 of the 321,732 consolidated relief — 91.0%**. Other
segment D&A was **62.24%** of all consolidated D&A in Q1 2025 and **6.79%** in Q1 2026. Consolidated
D&A fell from **12.62% of revenue** (488,333 ÷ 3,869,758) to **4.54%** (166,601 ÷ 3,667,489) — a
fall of **8.08 percentage points of revenue** in one year. [DEMONSTRATED]

**⚠️ CORRECTION TO CARRY, and this is the substantive one.** The inherited framing — *"the D&A relief
is PERMANENT"* — is correct, but its consequence is stronger than the framing implies: **an
add-back-only normalisation still flatters FY2026.** Removing the one-off credit (the ex-item
calculation in §2.3) is *insufficient*, because the recurring cost base itself has been reset 65.9%
lower. Every future quarter reports against a D&A charge that no longer exists. The Other segment's
operating loss improved from **(628,410)** to **(87,295)** — a **+541,115** improvement — of which
**292,624 is D&A relief** and only 182,332 is an OIBDA-level change. Real "clean" operating
performance at SATS must be struck on a pre-impairment D&A base that the company no longer reports,
which is not obtainable from any filed column. Class: **UNRESOLVABLE-FROM-PUBLIC-SOURCES** — the
disclosure that would resolve it is a restated prior-period D&A schedule on the post-impairment
asset base, which no issuer produces.

---

## 6. DA-29 — a validator `pass` on a wrong-signed value

`validate_calculation` **runs** at SATS (33 / 26 / 41 rows across three accessions — the zero-row
gap seen at another issuer does **not** reproduce) and returns **`status: pass` on a value whose
sign is wrong**:

```
ProfitLoss, Q3 2025     computed 12,781,348,000   reported 12,781,348,000   diff 0   status pass
                        filing prints $ (12,781,348) thousand    [📄 SATS 10-Q p.10](https://agentii.ai/v/SATS/sec120/10)
ProfitLoss, FY2025      computed 14,506,939,000   reported 14,506,939,000   diff 0   status pass
                        filing prints $ (14,506,939) thousand    [📄 SATS 10-K p.150](https://agentii.ai/v/SATS/sec85/150)
```

**A validator PASS coexisting with a wrong-signed value on the very concept checked.** Its
`reported` column draws from the same stripped fact store, so **it cannot detect the strip by
construction.**

**And `computed` is unusable independently of that.** For `OperatingIncomeLoss` at Q1 2026 the
instrument's `computed` is **3,657,411,000** against a filed **392,847** thousand — wrong by ~9.3×;
for Q3 2025 the instrument gives `computed 224,000` / `reported 563,000` while the served fact for
the same concept and period is **16,641,875,000**. **Three mutually inconsistent values for one
concept and period, none matching the filed (16,641,875).** Per DA-29's chosen reading, **no
`computed` value is cited anywhere in this artifact as a derivation, and no term used here appears
nowhere in the source.** [DEMONSTRATED]

**Carry-forward (register-level):** this is a **new kind** of DA-29 failure, distinct from a
zero-row validator gap — *validator-affirms-stripped-value*. The two have different remedies and
must not be merged: a zero-row gap is an absence of checking; a pass-on-stripped-value is a check
that ran against a compromised input column and certified it.

---

## 7. DA-30 — four live basis collisions, all named at every use

| # | Concept | Basis A | Basis B | Difference | Basis quoted here |
|---|---|---|---:|---:|---|
| 1 | Q1 2026 total costs and expenses | D&A-inclusive **3,274,642** (tagged) | D&A-exclusive **3,108,041** (caption's claim) | 166,601 | **D&A-inclusive** |
| 2 | Q1 2026 net income (loss) | consolidated **(147,300)** | attributable **(146,885)** | 415 | **consolidated**, except per-share |
| 2 | FY2025 net loss | consolidated **(14,506,939)** | attributable **(14,497,180)** | 9,759 | **consolidated**, except per-share |
| 3 | Spectrum licences at 2026-03-31 | tranche subtotal **$29,614,839** | fully loaded **$34,550,802** | 16.7% | **fully loaded** |
| 4 | Q1 2026 segments | Segment Total OI **392,674**, revenue **3,677,394** | Consolidated OI **392,847**, revenue **3,667,489** | 173 / (9,905) | **consolidated** |

Sources: [p.11](https://agentii.ai/v/SATS/sec121/11), [p.25](https://agentii.ai/v/SATS/sec121/25),
[p.46](https://agentii.ai/v/SATS/sec121/46), [p.71](https://agentii.ai/v/SATS/sec121/71),
[p.108](https://agentii.ai/v/SATS/sec121/108), [p.150](https://agentii.ai/v/SATS/sec85/150).
[DEMONSTRATED]

**Instance 2 is the sharpest, because the platform serves the two bases from two different surfaces
under the same undimensioned idea:** `get_company_financials` serves `net_income_loss` on the
**attributable** basis (146,885,000 at Q1 2026; 14,497,180,000 at FY2025) while
`validate_calculation`'s `ProfitLoss` row serves the **consolidated** basis (12,781,348,000 at Q3
2025). **Two values for "net income", one period, no basis field.** A per-share figure and a
statement-face figure for the same quarter are therefore not quotable against each other.

**Instance 1 is the one that produces a wrong number rather than an ambiguous one** — see §1.1.

---

## 8. What I could not resolve

| Item | Class | The disclosure that would resolve it |
|---|---|---|
| Q1 2025 and Q2 2025 row-layer `net_income_loss` is **null** | **UNRESOLVABLE-FROM-PLATFORM** | The filed figures exist (Q1 2025 attributable net loss (202,669) thousand at [p.11](https://agentii.ai/v/SATS/sec121/11); Q2 2025 derived **(306,132)** from the 9M2025 column). Only the platform's row layer is silent — so the *only* sign test the platform supports in those two periods is the inadmissible `EPS × shares`, which this artifact does not use. |
| Q2 2026 (quarter ended 2026-06-30) is not in this series | **UNRESOLVABLE-FROM-PLATFORM** | The consensus calendar shows a 2026-08-07 report date with `actual: null`; no filed cells for that quarter were reachable through the fact store or the row layer. The filing itself exists; the platform's coverage does not include it at `as_of`. |
| Clean operating performance on the post-impairment D&A base | **UNRESOLVABLE-FROM-PUBLIC-SOURCES** | A restated prior-period D&A schedule on the post-impairment asset base (§5). No issuer produces one. |
| The gain or loss on the spectrum disposal | **UNRESOLVABLE-FROM-PUBLIC-SOURCES** (until closing) | It will be determined **at closing**, on a basis different from anything in the current statements: $22.650 billion cash (minimum $18.6 billion) from AT&T ([p.14](https://agentii.ai/v/SATS/sec121/14)) against a pre-disposal carrying amount of $34,550,802 thousand ([p.46](https://agentii.ai/v/SATS/sec121/46)). Any ratio of consideration to carrying value quoted today is on two non-comparable bases. |

**Presence vs absence — an explicit `UNEXERCISED`:** the DA-23 sign test **could not run on any
positive-margin period other than Q1 2026**, because SATS has none. The test is therefore
**12/12 confirmed on the periods where it could run**, and `UNEXERCISED` on the question of whether
the platform mis-serves a *positive* operating income in a loss-heavy series — one positive period
is too thin a basis to clear that, and it is reported as **UNEXERCISED, not CLEAN**.

---

## 9. Sources

| What it carries | Link |
|---|---|
| Q1 2026 statement of operations — identity cells, the D&A-inclusive/exclusive basis pair, consolidated vs attributable net loss | [📄 SATS 10-Q p.11](https://agentii.ai/v/SATS/sec121/11) |
| Q1 2026 Segment Adjusted OIBDA bridge, both periods — the D&A relief decomposition and the (66,159) term that forces its own sign | [📄 SATS 10-Q p.108](https://agentii.ai/v/SATS/sec121/108) |
| Q1 2026 statement of cash flows | [📄 SATS 10-Q p.13](https://agentii.ai/v/SATS/sec121/13) |
| Note 1 — AT&T License Purchase Agreement, $22.650bn, Minimum $18.6bn, short-term spectrum manager lease | [📄 SATS 10-Q p.14](https://agentii.ai/v/SATS/sec121/14) |
| Both transactions pending FCC/DOJ; AT&T closing expected H1 2026 | [📄 SATS 10-Q p.15](https://agentii.ai/v/SATS/sec121/15) |
| SpaceX closing schedule; $414m reimbursable Seller Notes interest | [📄 SATS 10-Q p.16](https://agentii.ai/v/SATS/sec121/16) |
| Note 3 EPS — combined Class A and B denominator; 58m anti-dilutive convertibles | [📄 SATS 10-Q p.25](https://agentii.ai/v/SATS/sec121/25) |
| Wireless Spectrum Licenses — $29,614,839 subtotal vs $34,550,802 fully loaded | [📄 SATS 10-Q p.46](https://agentii.ai/v/SATS/sec121/46) |
| Segment vs consolidated reconciliation — 392,674 vs 392,847; 3,677,394 vs 3,667,489 | [📄 SATS 10-Q p.71](https://agentii.ai/v/SATS/sec121/71) |
| Q3 2025 statement of operations — the (16,641,875) impairment quarter and the 9M columns | [📄 SATS 10-Q p.10](https://agentii.ai/v/SATS/sec120/10) |
| Q3 2025 statement of cash flows | [📄 SATS 10-Q p.12](https://agentii.ai/v/SATS/sec120/12) |
| FY2025 MD&A — the $17.632bn / $16.481bn / $1.151bn charge schedule | [📄 SATS 10-K p.76](https://agentii.ai/v/SATS/sec85/76) |
| FY2025 statement of operations — the three annual columns | [📄 SATS 10-K p.150](https://agentii.ai/v/SATS/sec85/150) |
| FY2025 statement of cash flows | [📄 SATS 10-K p.152](https://agentii.ai/v/SATS/sec85/152) |
| Debt note — 2026 maturities; additional AWS-3 consideration | [📄 SATS 10-K p.157](https://agentii.ai/v/SATS/sec85/157) |

**Evidence grade: DEMONSTRATED.** Every figure above is a filed cell or arithmetic directly on
filed cells. The only `MODELED` elements are the two annual-to-quarter multipliers in §2.1 and the
implied Q4 2025 share count in the frontmatter's DA-28 entry, which are **order-of-magnitude
cross-checks and satisfy no falsifier**; they are labelled as such where they appear and are used
for nothing else.
