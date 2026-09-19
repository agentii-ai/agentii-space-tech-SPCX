---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-5
ticker: RKLB
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
    chosen_reading: "|x| absolute-value stripping, not inversion: served = |filed|, magnitude preserved, sign discarded. At RKLB it flips THREE lines in one quarter — operating loss, net loss and diluted EPS."
  - da_id: DA-26
    chosen_reading: "annual figures mislabelled as quarterly. Screened at RKLB by reconciling every quarterly row against its cumulative and its fiscal-year total, and by comparing each fact's own duration. NOT CONFIRMED — all identities close and every label matches its duration."
  - da_id: DA-27
    chosen_reading: "fiscal-period labels derived from the calendar quarter. RKLB is a 31-Dec filer so the class is UNEXERCISED; the calendar's `report_date` field additionally carries three collapsed bases (`sec_grid_lag`, `ect_exact`, `ect_forward`) with no basis discriminator (DA-30)."
  - da_id: DA-30
    chosen_reading: "two bases on one concept collapsed without a basis field. RKLB carries three bases on EPS — filed $(0.08), platform-served +0.08, earnings-calendar -0.08 — and three bases on `report_date`. All are reported; none is quoted alone."
  - da_id: DA-28
    chosen_reading: "capital-structure discontinuity invalidates share-count and per-share detectors. Applied to RKLB's anti-dilutive convertible-note shares, which fall 69,261,530 -> 2,607,745 in one year while 7,451,200 collared-forward shares appear from zero."
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
citations:
  - figure: "RKLB sec109 p.6"
    ticker: RKLB
    citation_id: sec109
    page_no: 6
    url: https://agentii.ai/v/RKLB/sec109/6
    located_via: read_source_pages
key_metrics:
  operating_income_loss_served_usd_q2_2026: 57514000
  operating_loss_usdk_filed_q2_2026: -57514
  net_loss_usdk_filed_q2_2026: -49258
  anti_dilutive_convertible_note_shares_q2_2026: 2607745
---

# RKLB — recent quarter: three lines flipped in one quarter, and the component identity closes exactly

**All monetary quantities in this artifact are US$ thousands unless labelled otherwise.**
Source: Rocket Lab Corporation Form 10-Q for the quarterly period ended 2026-06-30, accession
`0001819994-26-000062`, filed 2026-08-10, 54 pages, `citation_id: sec109`.

**`deal_security_basis: standalone_pre_merger` (P11).** RKLB is a designated deal security;
every figure in this file is on the standalone pre-merger basis and is not comparable with a
post-close or combined-entity presentation.

## 1. The finding

**Four results, in descending order of consequence.**

1. **DA-23 FIRED on THREE lines in one quarter, and all three are confirmed against the filed
   statement.** Q2 2026: `OperatingIncomeLoss` served **+57,514,000** against filed
   **$(57,514)**; `NetIncomeLoss` served **+49,258,000** against filed **$(49,258)**;
   `EarningsPerShareDiluted` served **+0.08** against filed **$(0.08)**
   [📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6). **The sign is lost on the operating
   line, the bottom line and the per-share line simultaneously** — which is why every
   metrics-block screen that ranks this cohort is not degraded but *inverted*.

2. **The component identity closes exactly on the EXCLUSIVE opex definition — 4 of 4 periods.**
   `gross profit − total operating expenses = operating loss` to the filed thousand:
   84,576 − 142,090 = **(57,514)**; 46,388 − 106,027 = **(59,639)**; 161,069 − 274,552 =
   **(113,483)**; 81,635 − 200,462 = **(118,827)**. **The served magnitudes are correct, and that
   is now established rather than assumed.**

3. **The inclusive-opex reading does not merely fail at RKLB — it has no filed line to fail
   on.** Unlike SPCX, RKLB files **no** `Costs and expenses` total. It files `Total cost of
   revenues` and `Total operating expenses` in disjoint sections of the statement. The inclusive
   reading is a **platform-constructed sum the filer never presents**, and it is false by
   **exactly total cost of revenues** in all four periods.

4. **DA-26 screened NEGATIVE by annual reconciliation — and the screen actually ran.** Four
   fiscal years of quarterly rows reconcile exactly to their own cumulative totals and to their
   own fiscal-year totals. **No annual figure sits in a quarterly row at RKLB.** This is a
   positive negative finding: the test was exercised and it cleared.

**PIL-5's own claim gets a sharp edge from this quarter.** Product revenue grew **+95.6%** YoY
while service revenue grew **+1.8%** — and the per-launch disclosure PIL-5 rests on is a
*cost-side* measurement. The asymmetry PIL-5 asserts is visible in the mix before any per-launch
normalisation is attempted (§3.3).

---

## 2. Mode `consolidated-p-and-l` — the DA-23 sign test

### 2.1 Filed cells (verbatim from the statement)

`[📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6)` — Condensed Consolidated Statements of
Operations and Comprehensive Loss, unaudited, in thousands except share and per share data.

| Line (US$ thousands) | 3M to 2026-06-30 | 3M to 2025-06-30 | 6M to 2026-06-30 | 6M to 2025-06-30 |
|---|---:|---:|---:|---:|
| Product revenues | 181,347 | 92,725 | 308,835 | 173,529 |
| Service revenues | 52,719 | 51,773 | 125,579 | 93,538 |
| **Total revenues** | **234,066** | **144,498** | **434,414** | **267,067** |
| Cost of product revenues | 117,439 | 61,692 | 198,523 | 115,561 |
| Cost of service revenues | 32,051 | 36,418 | 74,822 | 69,871 |
| **Total cost of revenues** | **149,490** | **98,110** | **273,345** | **185,432** |
| **Gross profit** | **84,576** | **46,388** | **161,069** | **81,635** |
| Research and development, net | 82,429 | 66,134 | 162,942 | 121,243 |
| Selling, general and administrative | 59,661 | 39,893 | 111,610 | 79,219 |
| **Total operating expenses** | **142,090** | **106,027** | **274,552** | **200,462** |
| **Operating loss** | **(57,514)** | **(59,639)** | **(113,483)** | **(118,827)** |
| Total other income (expense), net | 13,583 | (3,837) | 22,738 | (6,078) |
| Loss before income taxes | (43,931) | (63,476) | (90,745) | (124,905) |
| **Net loss** | **(49,258)** | **(66,414)** | **(94,280)** | **(127,030)** |
| **Basic and diluted loss per share** | **$(0.08)** | **$(0.13)** | **$(0.15)** | **$(0.25)** |
| Weighted-average common shares outstanding | 629,681,803 | 515,086,631 | 617,625,210 | 510,376,584 |

Grade for every cell above: **DEMONSTRATED** (filed figure, read from the statement page).

**Two structural facts about this statement, both load-bearing:**

- **There is no `Costs and expenses` caption.** `Total cost of revenues` sits above `Gross
  profit`; `Total operating expenses` sits below it. The two totals are in disjoint sections and
  are never summed by the filer.
- **`Total operating expenses` is itself the exact sum of its two components** in every period:
  82,429 + 59,661 = 142,090 ✓; 66,134 + 39,893 = 106,027 ✓; 162,942 + 111,610 = 274,552 ✓;
  121,243 + 79,219 = 200,462 ✓. **The exclusive opex definition is not a choice at RKLB — it is
  a filed line, and its two components are the only two lines under it.**

### 2.2 The component identity, with the opex definition stated

**Opex definition used: EXCLUSIVE — `us-gaap:OperatingExpenses`, filed as `Total operating
expenses`** (= `Research and development, net` + `Selling, general and administrative`). Cost of
revenues is a cost-of-sales block and is **excluded**.

| Period | Gross profit | Opex (exclusive, filed total) | GP − Opex | Filed operating loss | Verdict |
|---|---:|---:|---:|---:|:--|
| 3M 2026 | **84,576** | **142,090** | **(57,514)** | **(57,514)** | **exact** |
| 3M 2025 | **46,388** | **106,027** | **(59,639)** | **(59,639)** | **exact** |
| 6M 2026 | **161,069** | **274,552** | **(113,483)** | **(113,483)** | **exact** |
| 6M 2025 | **81,635** | **200,462** | **(118,827)** | **(118,827)** | **exact** |

4 of 4 exact. Grade: **DEMONSTRATED** (arithmetic directly on filed cells).

### 2.3 The inclusive reading — refuted, and it has no filed line to stand on

If `us-gaap:CostsAndExpenses` is read **inclusively** (cost of sales **plus** operating
expenses), the identity is false. **At RKLB that quantity is not on the statement.** The nearest
construct is a platform-side sum the filer never presents:

| Period | Inclusive construct = Total cost of revenues + Total operating expenses | GP − inclusive | Filed operating loss | Discrepancy | = total cost of revenues? |
|---|---:|---:|---:|---:|---|
| 3M 2026 | 149,490 + 142,090 = **291,580** | (207,004) | (57,514) | **149,490** | ✓ exactly |
| 3M 2025 | 98,110 + 106,027 = **204,137** | (157,749) | (59,639) | **98,110** | ✓ exactly |
| 6M 2026 | 273,345 + 274,552 = **547,897** | (386,828) | (113,483) | **273,345** | ✓ exactly |
| 6M 2025 | 185,432 + 200,462 = **385,894** | (304,259) | (118,827) | **185,432** | ✓ exactly |

**The offset equals total cost of revenues to the unit in all four periods.** The inclusive
reading overstates the operating loss by 63.9% of revenue at 3M 2026 (149,490/234,066) and by
62.9% at 6M 2026 (273,345/434,414). Grade: **DEMONSTRATED**.

**This is a stronger statement than at UTHR or SPCX.** Those issuers file an inclusive caption,
so the inclusive reading is *available and wrong*. **At RKLB the inclusive reading is not
available at all**: `CostsAndExpenses` can only be a platform-constructed aggregation across
sections, and any component identity built on it is false by exactly the cost-of-revenues block.
**An issuer that never presents the inclusive total cannot be screened by a rule that assumes
it.** The applicable reading must be established per-issuer from the statement's own sub-total
structure, not applied from the register by default.

### 2.4 Served vs filed — the sign-test verdict

| Concept | Period | Filed | Platform-served | Relation | Verdict |
|---|---|---:|---:|---|:--|
| `OperatingIncomeLoss` | 3M 2026 | (57,514) | +57,514,000 | served = \|filed\| | **FIRED** |
| `OperatingIncomeLoss` | 6M 2026 | (113,483) | +113,483,000 | served = \|filed\| | **FIRED** |
| `OperatingIncomeLoss` | 3M 2025 | (59,639) | +59,639,000 | served = \|filed\| | **FIRED** |
| `OperatingIncomeLoss` | 6M 2025 | (118,827) | +118,827,000 | served = \|filed\| | **FIRED** |
| `NetIncomeLoss` | 3M 2026 | (49,258) | +49,258,000 | served = \|filed\| | **FIRED** |
| `NetIncomeLoss` | 6M 2026 | (94,280) | +94,280,000 | served = \|filed\| | **FIRED** |
| `NetIncomeLoss` | 3M 2025 | (66,414) | +66,414,000 | served = \|filed\| | **FIRED** |
| `NetIncomeLoss` | 6M 2025 | (127,030) | +127,030,000 | served = \|filed\| | **FIRED** |
| `EarningsPerShareDiluted` | 3M 2026 | (0.08) | +0.08 | served = \|filed\| | **FIRED** |
| `EarningsPerShareDiluted` | 6M 2026 | (0.15) | +0.15 | served = \|filed\| | **FIRED** |
| `EarningsPerShareBasic` | 3M 2026 | (0.08) | +0.08 | served = \|filed\| | **FIRED** |
| `EarningsPerShareBasic` | 6M 2026 | (0.15) | +0.15 | served = \|filed\| | **FIRED** |

**Verdict: DA-23 FIRED. 12 of 12 quoted sign-bearing facts; 3 of 3 concepts; 4 of 4 periods.**

**The wider served operating series, complete.** `OperatingIncomeLoss` returns **34 facts for
RKLB** and **every one is positive** — the served series has no negative value anywhere from
FY2020 through Q2 2026:

| Period | Served | Period | Served | Period | Served |
|---|---:|---|---:|---|---:|
| FY2020 | +54,952,000 | FY2023 | +177,918,000 | 9M2024 | +138,252,000 |
| FY2021 | +102,053,000 | Q1 2023 | +46,017,000 | Q2 2024 | +43,274,000 |
| Q1 2021 | +12,291,000 | Q2 2023 | +45,159,000 | Q1 2024 | +43,079,000 |
| Q2 2021 | +13,134,000 | 1H2023 | +91,176,000 | FY2024 | +189,801,000 |
| Q3 2021 | +52,295,000 | Q3 2023 | +38,859,000 | Q1 2025 | +59,188,000 |
| 9M2021 | +77,722,000 | 9M2023 | +130,035,000 | Q2 2025 | +59,639,000 |
| FY2022 | +135,204,000 | Q1 2024 | +43,079,000 | 1H2025 | +118,827,000 |
| Q1 2022 | +32,820,000 | Q2 2024 | +43,274,000 | Q3 2025 | +58,969,000 |
| Q2 2022 | +33,159,000 | 1H2024 | +86,353,000 | 9M2025 | +177,796,000 |
| 1H2022 | +65,979,000 | Q3 2024 | +51,899,000 | FY2025 | +228,838,000 |
| Q3 2022 | +32,002,000 | 9M2022 | +97,981,000 | Q1 2026 | +55,969,000 |
| — | — | — | — | Q2 2026 | +57,514,000 |

**34 of 34 positive. There is no RKLB operating series with a sign in this corpus.** For a
company that has never reported a profitable quarter, a served operating series that is
uniformly positive is not a data series at all — it is a magnitude series.

**Additivity confirms the relation is `|x|` and not something stranger.** 55,969 + 57,514 =
113,483 = 6M 2026 ✓; 59,188 + 59,639 = 118,827 = 6M 2025 ✓; 118,827 + 58,969 = 177,796 = 9M
2025 ✓; 60,616 + 66,414 + 18,257 = 145,287 = 9M 2025 net loss ✓. **The stripping is applied
per fact and preserves additive structure** — which is exactly what makes it survive inspection:
a stripped series that still adds up looks correct.

### 2.5 The DA-30 obligation at RKLB

| Metric | Filed | Platform XBRL | Earnings calendar |
|---|---:|---:|---:|
| Q2 2026 EPS diluted | **$(0.08)** | **+0.08** | **-0.08** |
| Q2 2026 net loss | **$(49,258) thousand** | **+49,258,000** | — |
| Q2 2026 revenue | **$234,066 thousand** | +234,066,000 | **234,066,000** |

**Two of the three layers agree and the third does not, and which two agree depends on the
metric.** On EPS the calendar agrees with the filing and the facts layer does not; on revenue all
three agree (revenue is unsigned, so DA-23 has no purchase on it). **DA-23 is a layer property:
it lives in the XBRL facts extraction and nowhere else.** This is now confirmed at two issuers
(SPCX §2.5, RKLB here), on the same metric, in the same direction, against the same layer.

---

## 3. Mode `margin-analysis` — the DA-26 / DA-27 period traps

### 3.1 DA-26 — screened by annual reconciliation, NOT CONFIRMED

**The screen, run as specified.** DA-26 is annual figures mislabelled as quarterly. It is
screened (a) by **reconciling a row against known annual totals**, and (b) by **comparing a
row's duration, not its position in the sequence**. At RKLB both screens can run because the
corpus holds FY2025, FY2024, FY2023, FY2022, FY2021 and FY2020 annual rows
(`source_authority: 3`, from Forms 10-K).

**(a) Duration screen.** Every served fact carries its own `period_start`/`period_end`, and the
durations match their labels in every case inspected:

| Label class | Period span | Duration | Label correct? |
|---|---|---:|:--|
| `FY2025` | 2025-01-01 → 2025-12-31 | 12 months | ✓ |
| `9M2025` | 2025-01-01 → 2025-09-30 | 9 months | ✓ |
| `1H2025` / `1H2026` | 2025-01-01 → 2025-06-30 | 6 months | ✓ |
| `Q3 2025`, `Q1 2026`, `Q2 2026` | one calendar quarter each | 3 months | ✓ |

**Every label matches its own duration.** No 12-month fact carries a quarterly label.

**(b) Annual-reconciliation screen.** Each quarterly row is reconciled against its cumulative
total and its fiscal-year total. All arithmetic in US$ thousands; served magnitudes, sign-neutral:

| Fiscal year | Q1 | Q2 | 1H (= Q1+Q2) | Q3 | 9M (= 1H+Q3) | FY | FY − 9M (implied Q4) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2023 | 46,017 | 45,159 | **91,176 ✓** | 38,859 | **130,035 ✓** | **177,918** | 47,883 |
| 2024 | 43,079 | 43,274 | **86,353 ✓** | 51,899 | **138,252 ✓** | **189,801** | 51,549 |
| 2025 | 59,188 | 59,639 | **118,827 ✓** | 58,969 | **177,796 ✓** | **228,838** | 51,042 |
| 2026 | 55,969 | 57,514 | **113,483 ✓** | — | — | — | — |

**Every cumulative identity closes exactly, in every fiscal year, to the thousand.** If any
quarterly row carried an annual figure, the cumulative identity would break — a 12-month number
added to a 3-month number cannot equal a filed 6-month total. It does not break anywhere.

**Verdict: DA-26 NOT CONFIRMED at RKLB.** Both screens ran and both cleared. Grade:
**DEMONSTRATED** for the arithmetic; **DEMONSTRATED** for the negative finding, because the test
was exercised rather than skipped.

**One honest caveat, because the screen has a tolerance floor.** One cross-vintage
reconciliation misses by $2 thousand: `9M2021` (77,722) minus `1H2021` (25,425) = 52,297, while
the served `Q3 2021` is 52,295 — a **$2 thousand (0.004%) non-additivity** between facts read
from different filing vintages (`rklb-20220930.htm` supplies both, but the comparatives were
restated across the 2021 SPAC-merger period). **The screen is exact within a filing vintage and
approximately exact across vintages.** A detector with a zero tolerance would fire here — wrongly.

**The Q4 hole, recorded.** There is **no `Q4` fact for any year** in the RKLB served series —
31 December filers never file a Q4 10-Q, so a standalone Q4 is never filed and exists only as
`FY − 9M`. The earnings calendar fills the gap for FY2025 (`2025 (Q4)`, `report_date`
2026-02-26, revenue_actual 179,652,000) — **a cross-layer complement worth using, and per DA-29
a Q4 that reconciles is not thereby a checked Q4.** It is a back-solve with a filed total above
it; that is all.

### 3.2 DA-27 — UNEXERCISED at RKLB, and the `report_date` field carries three collapsed bases

**Verdict on the class: UNEXERCISED.** RKLB reports on a 31 December year and its earnings
calendar resolves from `gold_companies` with a `null` cross-validation hint. **A 31-Dec filer has
no fiscal label that can differ from its calendar label, so DA-27 cannot manifest here.** Not
`CLEAR` — inapplicable. Recorded as PRESENCE-vs-ABSENCE.

**But the date field is a genuine DA-30 site.** `report_date` is populated on **three different
bases with no basis discriminator on the row**:

| Row | `report_date` | `fiscal_source` | What the date actually is |
|---|---|---|---|
| 2020 (Q1) | 2020-03-31 | `sec_grid_lag` | **the fiscal period END** |
| 2021 (Q2) | 2021-09-08 | `ect_exact` | **the earnings release date** |
| 2025 (Q1) | 2025-05-08 | `ect_exact` | the earnings release date |
| 2025 (Q4) | 2026-02-26 | `ect_exact` | the earnings release date |
| 2026 (Q3) | 2026-11-09 | `ect_forward` | **a scheduled future release date** |

**A single date column means three different things depending on a sibling field that a reader
must know to consult.** This is DA-30 in its textbook form: two (here three) bases on one
concept, collapsed without a basis field.

**Consequence for any DA-27 detector, and the reason this is worth recording:**

- **A `report_date`-keyed detector is a tautology on `sec_grid_lag` rows** — the date *is* the
  period end, so it can never fall outside its own quarter. It cannot fail.
- **The same detector produces false positives on `ect_exact` rows** — a release date for a
  quarter ending 30 June can easily fall in calendar Q3. **FLY's 2025 (Q2) row is exactly that
  case** (see the FLY artifact in this set), and firing on it is wrong.
- **No metadata-keyed DA-27 detector has a valid operating regime.** The only admissible screen
  is the **duration comparison and annual reconciliation** of §3.1, which is keyed to the fact's
  own `period_start`/`period_end` and to filed totals — never to a label and never to a date
  field.

**Forward rows are distinguishable and are not a DA-26/27 instance.** The `2026 (Q3)` row sits
**in the future** relative to `as_of` 2026-09-19, carries `fiscal_source: ect_forward` and null
actuals. Forward-synthesised rows are a third class: not a mislabelled past period, and not to
be conflated with one.

### 3.3 The safe-set margins, and the mix that PIL-5 actually needs

Per thesis 001's ratio audit, **gross margin is SAFE** (unsigned inputs) and **operating margin
is UNSAFE from the metrics block**. Every figure below is rebuilt from the p.6 cells.

| Metric | 3M 2026 | 3M 2025 | 6M 2026 | 6M 2025 |
|---|---:|---:|---:|---:|
| Total revenues (US$K) | 234,066 | 144,498 | 434,414 | 267,067 |
| Gross profit (US$K) | 84,576 | 46,388 | 161,069 | 81,635 |
| **Gross margin** | **36.13%** | **32.10%** | **37.08%** | **30.57%** |
| **Operating margin** (rebuilt, filed sign) | **−24.57%** | **−41.27%** | **−26.12%** | **−44.49%** |
| R&D / revenue | **35.22%** | **45.77%** | **37.51%** | **45.40%** |
| Revenue growth YoY | **+61.99%** | — | **+62.66%** | — |

All cells: **DEMONSTRATED** (arithmetic directly on filed p.6 cells). These reproduce thesis
001's peer-bench cells for RKLB (36.1% gross margin, −24.6% operating margin, 35.2%
R&D/revenue, +62.0% growth) from an independent read.

**The product/service split is where PIL-5's asymmetry is visible — with one caveat.**

| Split | 3M 2026 | 3M 2025 | YoY | Margin 3M 2026 | Margin 3M 2025 |
|---|---:|---:|---:|---:|---:|
| **Product** revenues | 181,347 | 92,725 | **+95.58%** | **35.24%** | 33.47% |
| **Service** revenues | 52,719 | 51,773 | **+1.83%** | **39.20%** | 29.66% |
| Product share of revenue | **77.48%** | 64.17% | **+13.31 pp** | — | — |

Grade: **DEMONSTRATED** (arithmetic on filed cells). Weighted back: 0.7748 × 35.24% + 0.2252 ×
39.20% = 36.14% ≈ the filed 36.13% ✓ — the split reconciles to the consolidated margin.

**The caveat is DA-21 and it is not decoration: the product/service split is an ISSUER-DEFINED
boundary and it is NOT the Launch Services / Space Systems segment split.** Product vs service
is a revenue-recognition classification; Launch Services is a reporting segment. **Launch
revenue is not equal to service revenue**, and this artifact does not claim it is. What the
table does establish is directional and conservative: **the component of RKLB's revenue that
grows is the product component, and the component that grows 1.8% is the one launch revenue
sits inside.** Read the other way, and equally validly: **service gross margin expanded 9.5
points (29.66% → 39.20%) on 1.8% revenue growth** — which is a cost-side result on a flat
revenue base, and that is precisely the shape PIL-5 asserts.

**The 34-of-34 sign result is what makes this section usable at all.** Without §2.4, this
margin table read from the metrics block would show RKLB with a **+24.57% operating margin** and
a **+26.12% H1 operating margin** — a profitable company with expanding margins, in the correct
relative rank order against its peers, from a company that has never had a profitable quarter.
**Plausible-but-wrong, not null.**

---

## 4. Mode `earnings-vs-consensus`

RKLB's earnings calendar is the richest in this artifact set and the most internally
inconsistent. Two things it does: **the revenue series reconciles exactly; the EPS series does
not.**

### 4.1 The revenue series — CLEAN, and exact

| Row | `revenue_actual` | Reconciles to | Verdict |
|---|---:|---|:--|
| 2025 (Q1) | 122,569,000 | — | — |
| 2025 (Q2) | 144,498,000 | filed 3M 2025 $144,498K | **exact ✓** |
| 2025 (Q1)+2025 (Q2) | 267,067,000 | filed 6M 2025 $267,067K | **exact ✓** |
| 2026 (Q1) | 200,348,000 | — | — |
| 2026 (Q2) | 234,066,000 | filed 3M 2026 $234,066K | **exact ✓** |
| 2026 (Q1)+2026 (Q2) | 434,414,000 | filed 6M 2026 $434,414K | **exact ✓** |

Grade: **DEMONSTRATED**. **The calendar revenue layer reconciles to filed cumulative totals
exactly at both the 3-month and 6-month horizons.** This is a second independent confirmation of
the point in §2.5: **DA-23 cannot affect revenue, because revenue has no sign.**

**One flag: the `2025 (Q3)` revenue_actual is `155,000,000` — an exactly round figure at the
$1 million level, where every other value in the series is exact to the thousand.** It cannot be
reconciled from this artifact (the Q3 2025 10-Q, `rklb-20250930.htm`, is in the corpus but was
not read here). **Verdict: `UNRESOLVED` — not "probably a rounding". A round number in an
otherwise exact series is a provenance question, and the dangerous failure mode is
plausible-but-wrong.** The disclosure that would resolve it is the Q3 2025 statement of
operations revenue line.

### 4.2 The EPS series — UNRESOLVED, and it must not be used to repair the XBRL layer

| Period | Filed as-reported EPS | Basis of the filed sign | Vendor `eps_actual` | Reconciles? |
|---|---:|---|---:|:--|
| 3M 2026 | **(0.08)** | read from p.6 | −0.08 | **YES** |
| 6M 2026 | **(0.15)** | read from p.6 | (no row) | n/a |
| 3M 2025 | **(0.13)** | read from p.6 | −0.10 | **NO** |
| 6M 2025 | **(0.25)** | read from p.6 | (no row) | n/a |
| 1Q 2026 | **(0.07)** | **DERIVED** — served 0.07; magnitude cross-checked 45,022 / 617,625,210 = 0.073 | −0.02 | **NO** |
| 3Q 2025 | sign **UNEXERCISED** — no p.6 equivalent read; served +0.03 and +18,257,000 | — | +0.01 | **UNRESOLVED** |

**Result: of the four periods with a filed-sign basis, the vendor EPS reconciles in ONE (3M 2026)
and fails in TWO (3M 2025, 1Q 2026), with one `UNRESOLVED` on a sign that was never read from a
filing.**

**Two separate defects, and they must not be merged:**

1. **A magnitude mismatch.** 3M 2025: vendor −0.10 against filed $(0.13). 1Q 2026: vendor −0.02
   against filed $(0.07). Neither difference is explained by any filed cell.
2. **A sign question that is UNEXERCISED, not answered.** For 3Q 2025 the served fact is
   `+0.03` and the served net loss is `+18,257,000`. **On the `|x|` pattern the filed values are
   $(0.03) and $(18,257) thousand — but this artifact did not read a filing that states them, so
   asserting the filed sign would be inference dressed as evidence.** The vendor's `+0.01` is
   positive and the served `+0.03` is positive; they agree in sign and disagree in magnitude.
   **Disposition: `UNEXERCISED`. A test that could not run is not a passed test.**

**The vendor series is internally consistent and externally wrong.** Each row's `eps_prior_year`
matches its own prior row (−0.08 prior −0.10 → the 3M 2025 row says −0.10; −0.10 prior −0.08 →
the 3M 2025 row's prior is −0.08... the chain closes on itself). **Internal consistency is not
evidence of correctness, and here it actively conceals the mismatch: the series is a closed loop
that never touches a filed figure except in one period.** Per the stability rule, the vendor EPS
series is (a) **not exact** — 1 of 4; (b) **not stable** — it matches in one period and fails in
two; and (c) **not consistent with any specified formula or filed basis** that this artifact can
identify. **All three limbs fail. Disposition: `UNRESOLVED`.**

**Classification: `UNRESOLVABLE-FROM-PLATFORM`** — the filed as-reported EPS exists in every
10-Q in the corpus; the vendor series is simply not derived from it in a way this artifact can
reproduce.

### 4.3 The capital-structure discontinuity — DA-28, at a non-IPO event

Disclosed verbatim in a served text fact (nonNumeric — **text facts are not sign-stripped, so
this one is usable as filed**):

> *"The following equity shares were excluded from the calculation of diluted net loss per share
> attributable to common stockholders because their effect would have been anti-dilutive: June 30,
> 2026 / 2025. Stock options and restricted stock units 13,095,520 / 23,616,300. Shares
> underlying our convertible senior notes 2,607,745 / 69,261,530. Shares underlying our collared
> forward transactions 7,451,200 / —."*

| Anti-dilutive bucket | 2026-06-30 | 2025-06-30 | Change |
|---|---:|---:|---:|
| Stock options and RSUs | 13,095,520 | 23,616,300 | −44.5% |
| Convertible senior notes | **2,607,745** | **69,261,530** | **−96.2% (26.5×)** |
| Collared forward transactions | **7,451,200** | **0** | **from zero** |
| Common stock warrants | — | 728,835 | extinguished |

Grade: **DEMONSTRATED** (filed text, read as filed). The FY2025 10-K supplies the intermediate
point: convertible-note shares 69,261,530 → 30,368,547 → 2,607,745 across three filings.

**Why this matters even though it does not change the sign test:** the diluted-share denominator
at RKLB is **not on a stable basis across the comparison window**. A 69.3-million-share
convertible bucket fell to 2.6 million while a 7.5-million-share collared-forward bucket
appeared from zero. **Any detector that bridges per-share metrics across this boundary, and any
`EPS × shares` reconstruction, is measuring the capital structure and not the business.** This
is the DA-28 class applied to a non-IPO event — the register's IPO framing is the common case,
not the definition. **DA-28 is about a capital-structure step, not about an IPO.** The rule it
implies is the same at RKLB as at FLY: **per-share series are not comparable across a
capital-structure step, and the step must be established from the filing before any per-share
series is used at all.**

---

## 5. What this artifact could not resolve

| # | Unresolved | Class | The disclosure that would resolve it |
|---|---|---|---|
| 1 | **Vendor EPS basis at RKLB** — 1 of 4 reconcile | **`UNRESOLVABLE-FROM-PLATFORM`** | Every 10-Q in the corpus carries the filed as-reported EPS; the vendor series is not reproducible from them. Resolvable in principle, not from what is here. |
| 2 | **3Q 2025 filed EPS sign** — never read from a filing | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** (in this artifact's scope) | The 3Q 2025 10-Q (`rklb-20250930.htm`) — present in the corpus, not read here. **This is a scope limit, not a data limit, and it is recorded as `UNEXERCISED` rather than filled in by inference.** |
| 3 | **`2025 (Q3)` revenue = 155,000,000 exactly** | **`UNRESOLVED`** | The 3Q 2025 statement of operations revenue line. |
| 4 | **Standalone Q4 for any year** — the Q4 hole | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** | No 31-Dec filer files a Q4 10-Q. Derivable only as `FY − 9M`; per **DA-29** a reconciliation that closes is not thereby a check. |
| 5 | **Launch-only revenue at RKLB** | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** unless the segment note disaggregates it | The Launch Services segment revenue line. The p.6 product/service split is a different axis (DA-21) and is not a substitute. |
| 6 | **The per-launch $/kg normalisation** | carried, not re-derived here | RKLB's published $/kg figures are **1.79×–2.62× too low, four of four periods**; the realized denominator restates every demonstrated $/kg by **+79% to +162%** against a **±15%** tolerance. **Reconvert; never inherit a $/kg blindly.** Re-derived in the unit-economics artifact, not in this one. |
| 7 | **DA-27 at RKLB** | n/a (`UNEXERCISED`) | Nothing. A 31-Dec filer has no fiscal label that can differ from its calendar label. |

---

## 6. Carry-forwards

1. **DA-23 FIRED at RKLB: 12 of 12 quoted sign-bearing facts, 3 concepts, 4 periods — and
   34 of 34 `OperatingIncomeLoss` facts across FY2020–Q2 2026 are positive.** Three lines flip in
   one quarter: operating loss, net loss and diluted EPS. **Trust the magnitude, derive the sign.**
2. **The component identity closes exactly at RKLB, 4 of 4, on `gross profit − Total operating
   expenses`.** The exclusive opex definition is a **filed line** here, not a choice.
3. **RKLB files no inclusive `Costs and expenses` total.** The inclusive reading is a
   platform-constructed sum across disjoint sections, false by **exactly total cost of revenues**
   in all four periods (149,490 / 98,110 / 273,345 / 185,432). **An issuer that never presents
   the inclusive total cannot be screened by a rule that assumes one.**
4. **DA-26 NOT CONFIRMED at RKLB** — screened by duration AND by annual reconciliation, both
   exercised, both cleared, across FY2023–FY2026 to the thousand. **The screen's tolerance floor
   is $2K across filing vintages (the 3Q 2021 case); a zero-tolerance detector would misfire.**
5. **DA-27 UNEXERCISED at RKLB** (31-Dec filer) — and the `report_date` field carries **three
   collapsed bases** (`sec_grid_lag` = period end, `ect_exact` = release date, `ect_forward` =
   scheduled future). **No metadata-keyed DA-27 detector has a valid operating regime; screen on
   durations and filed totals only.**
6. **The vendor revenue layer is CLEAN and exact; the vendor EPS layer is `UNRESOLVED`.** Two
   different conclusions about two fields on the same rows. **Reconcile each field separately.**
7. **DA-28 applies to RKLB on a non-IPO event** — the convertible-note anti-dilutive bucket fell
   26.5× (69,261,530 → 2,607,745) while 7,451,200 collared-forward shares appeared from zero.
   **Per-share series are not comparable across that boundary.**
8. **PIL-5's asymmetry, from this quarter's filed cells:** product revenue **+95.6%** and service
   revenue **+1.8%**; service gross margin **29.66% → 39.20%**. The cost-side measurement is
   durable and the revenue-side normalisation is unreconciled — **and the split is a
   revenue-recognition axis (DA-21), not the Launch Services segment axis.**
9. **`deal_security_basis: standalone_pre_merger` (P11)** applies to all of the above and must be
   carried by anything citing this file.
10. **The stability rule applied throughout.** Every identification here is (a) exact, (b) stable
    across periods, and (c) consistent with a specified formula or a filed basis — or it is
    marked `UNRESOLVED`/`UNEXERCISED`. **Where it fails, the answer is not "probably fine."**
