---
pillar: PIL-7
thesis_id: "002-evidence-validation"
ticker: UTHR
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
as_of: 2026-09-18
deal_security_basis: not_applicable
definitions_used:
  - da_id: DA-23
    chosen_reading: >-
      Sign stripping is reproduced and localised to one dimension member:
      `us-gaap:GrossProfit` under `srt:ProductOrServiceAxis` =
      `us-gaap:ProductAndServiceOtherMember` is stored at its absolute value in
      six of six periods where the filed table prints a parenthetical loss. The
      filed sign is recovered from the filing's parentheses and corroborated by
      the served-component overshoot, which equals `2 x |component|` exactly.
  - da_id: DA-24
    chosen_reading: >-
      Non-operating contamination of the operating line is tested and CLEAN at
      UTHR: the filed statements of operations place `Other income (expense),
      net` BELOW `Operating income`, so no equity-securities or asset-sale term
      can enter the $330.8M operating subtotal. The benchmark is uncontaminated.
  - da_id: DA-25
    chosen_reading: >-
      Not engaged. No normalised or per-unit metric is used anywhere in this
      artifact; every margin is filed dollars over filed dollars, and no
      `per-share`, `per-launch` or `per-kW` normaliser appears.
  - da_id: DA-26
    chosen_reading: >-
      Does NOT reproduce on this concept set. 122 duration facts across the
      `GrossProfit`, `CostsAndExpenses` and `OperatingIncomeLoss` families were
      read; every `period_start`/`period_end` pair matches the filed caption.
      Recorded as NOT-REPRODUCED on this population, not as clean in general.
  - da_id: DA-29
    chosen_reading: >-
      001's own derivation is re-run from filed cells rather than accepted as a
      close. The derivation is a two-term arithmetic identity whose every term
      is present in the named filing, so it is NOT a back-solve; but 001's
      convergence statistic is computed on ROUNDED values and is therefore
      quoted here on unrounded ones.
  - da_id: DA-30
    chosen_reading: >-
      `incumbent terrestrial gross margin` is DA-30 at five sites in the
      subject and four in the comparator. Every figure in this artifact carries
      its issuer AND its basis in-line; no figure is quoted on an unnamed basis.
evidence_grade: DEMONSTRATED
unresolvable: false
citations:
  - figure: >-
      Statements of operations: Total revenues 783.3 / 798.6 / 1,564.8 /
      1,593.0; Cost of sales 99.5 / 87.6 / 232.9 / 180.1; Total operating
      expenses 452.5 / 434.1 / 908.2 / 845.7; Operating income 330.8 / 364.5 /
      656.6 / 747.3. No gross-profit line is filed on the statement face.
    ticker: UTHR
    form_type: 10-Q
    citation_id: sec219
    page_no: 4
    url: https://agentii.ai/v/UTHR/sec219/4
    located_via: read_source_pages
  - figure: >-
      Note 11 product table, Q2 2026 and Q2 2025 and H1 2026 and H1 2025:
      Other gross profit `(4.2)` / `(1.5)` / `(11.0)` / `(2.5)`; Total gross
      profit 683.8 / 711.0 / 1,331.9 / 1,412.9; Tyvaso DPI 275.5 on 326.6.
    ticker: UTHR
    form_type: 10-Q
    citation_id: sec219
    page_no: 20
    url: https://agentii.ai/v/UTHR/sec219/20
    located_via: read_source_pages
  - figure: >-
      Note 11 product table, Q1 2026: Tyvaso DPI gross profit 247.1 on revenue
      330.3; Other gross profit `(6.8)`; Total gross profit 648.1 on total
      revenues 781.5.
    ticker: UTHR
    form_type: 10-Q
    citation_id: sec215
    page_no: 18
    url: https://agentii.ai/v/UTHR/sec215/18
    located_via: search_keyword_in_source
  - figure: >-
      Note 13 segment table, FY2025 / FY2024 / FY2023: Other gross profit
      `(14.0)` / `(4.8)` / `(6.5)`; Total gross profit 2,798.3 / 2,567.7 /
      2,070.0 on total revenues 3,182.7 / 2,877.4 / 2,327.5.
    ticker: UTHR
    form_type: 10-K
    citation_id: sec212
    page_no: 96
    url: https://agentii.ai/v/UTHR/sec212/96
    located_via: search_keyword_in_source
  - figure: >-
      Condensed consolidated statements of income: Total revenues 10,054;
      Operating expenses: Cost of sales 2,811, R&D 1,868, SG&A 1,745, Other
      116; Total operating expenses 6,540; Operating income 3,514. No
      gross-profit line is filed.
    ticker: AMGN
    form_type: 10-Q
    citation_id: sec193
    page_no: 6
    url: https://agentii.ai/v/AMGN/sec193/6
    located_via: read_source_pages
  - figure: >-
      Segment note: Manufacturing cost of sales 2,139; Profit share and
      royalties in cost of sales 672 (sum 2,811); footnote 1, amortization of
      finite-lived intangible assets 890 for Q2 2026.
    ticker: AMGN
    form_type: 10-Q
    citation_id: sec193
    page_no: 14
    url: https://agentii.ai/v/AMGN/sec193/14
    located_via: read_source_pages
  - figure: >-
      MD&A operating expenses: Cost of sales 2,811; `% of product sales 29.5%`;
      `% of total revenues 28.0%`; Total operating expenses 6,540.
    ticker: AMGN
    form_type: 10-Q
    citation_id: sec193
    page_no: 45
    url: https://agentii.ai/v/AMGN/sec193/45
    located_via: read_source_pages
  - figure: >-
      Consolidated statements of earnings: Net product sales 12,588; Alliance
      and other revenues 385; Total Revenues 12,973; Cost of products sold
      3,726; Amortization of acquired intangible assets 437; Total Expenses
      8,887. Footnote (a): `Excludes amortization of acquired intangible
      assets.` No gross-profit and no operating-income subtotal is filed.
    ticker: BMY
    form_type: 10-Q
    citation_id: sec232
    page_no: 3
    url: https://agentii.ai/v/BMY/sec232/3
    located_via: read_source_pages
---

# UTHR × unit-economics — the corrected benchmark, and the basis it sits on

**Mode `methodology`.** This artifact does not open a position, does not size one, and
does not ask 001's questions. It validates one of 001's facts — the incumbent terrestrial
gross margin that PIL-4 makes the microgravity case's hurdle — and it reports what the
hurdle actually is, on which basis, and what it costs the case.

**The one-line answer.** 001's Line 4 `72.0 percent`, labelled *"Incumbent terrestrial
gross margin"*, is **not UTHR's margin and is not any issuer's filed gross margin at all**.
It is AMGN's *cost-of-sales ratio complement* on the total-revenues denominator. UTHR —
the issuer PIL-4's buyer set names and the microgravity pillar's incumbent comparator —
files a consolidated gross margin of **87.30%** for Q2 2026 (gross profit `$683.8M` on
total revenues `$783.3M`, [UTHR Q2 2026 10-Q p.4](https://agentii.ai/v/UTHR/sec219/4) and
[p.20](https://agentii.ai/v/UTHR/sec219/20)). The barrier is therefore **15.30 pp higher**
than 001 states, and the microgravity case is that much harder.

**And the `72.0` is not thereby wrong — it is answering a different question.** Revenue-weighted,
the three named buyers with filed gross profit average **72.13%** (§2.4), so `~72%` survives
as a *cohort aggregate*. **001 presented a cohort aggregate as a single-issuer bound without
recording that a weighting choice had been made.** Both figures are correct; one number was
doing two jobs, and the job the microgravity case needs is the 87.30%.

---

## 1. The instrument, and what it was asked to do

| | |
|---|---|
| Skill | `unit-economics`, `business-intelligence` vertical, **Standard** depth |
| Pin | `e87ee63269a2` — recorded, not re-derived in this artifact |
| Spec row | `theses/002-evidence-validation/spec.md` L570: *"`unit-economics` \| `business-intelligence` \| Standard \| VRT, UTHR, FLY \| none \| Terrestrial PUE and cooling benchmarks (**P4**); UTHR's margin benchmark (**P6**)"* |
| Pillar | **PIL-7** — every 001 falsifier classified as evaluable, platform-blocked, or source-blocked |
| Discharge of the spec row | The row has **two clauses and two tickers**. Clause 2 (**UTHR's margin benchmark**, P6) is discharged here. Clause 1 (**terrestrial PUE and cooling benchmarks**, P4) is VRT's and is discharged by `artifacts/VRT/2026-09-18_1500_unit-economics_methodology.md`. **No PUE or cooling figure enters this artifact**; §5 states why that is a scope boundary and not an omission. |

**The job, stated as a question with a falsifier.** *What is the actual incumbent
terrestrial gross margin the microgravity case must beat, what basis does it sit on, and
does UTHR's own filed margin support the weight 001 gave it?* This falsifies as:
`metric=count_of_headline_figures_in_001_whose_issuer_or_basis_is_unstated, threshold=0,
source=001 report-input.md, op=>`.

---

## 2. The corrected benchmark, by basis

### 2.1 UTHR — filed, consolidated, total-revenues basis

Every figure below is two filed cells divided into each other. The gross-profit totals are
filed as table cells in the Note 11 / Note 13 product tables; the revenue denominators are
filed as table cells on the same pages or on the statement face.

| Period | Issuer basis | Gross profit ($M) | Total revenues ($M) | Gross margin | Source |
|---|---|---:|---:|---:|---|
| Q2 2026 | consolidated, total revenues | 683.8 | 783.3 | **87.30%** | sec219 pp.4, 20 |
| Q1 2026 | consolidated, total revenues | 648.1 | 781.5 | **82.93%** | sec215 p.18 |
| H1 2026 | consolidated, total revenues | 1,331.9 | 1,564.8 | **85.12%** | sec219 pp.4, 20 |
| Q2 2025 | consolidated, total revenues | 711.0 | 798.6 | **89.03%** | sec219 pp.4, 20 |
| H1 2025 | consolidated, total revenues | 1,412.9 | 1,593.0 | **88.69%** | sec219 pp.4, 20 |
| FY2025 | consolidated, total revenues | 2,798.3 | 3,182.7 | **87.92%** | sec212 p.96 |
| FY2024 | consolidated, total revenues | 2,567.7 | 2,877.4 | **89.24%** | sec212 p.96 |
| FY2023 | consolidated, total revenues | 2,070.0 | 2,327.5 | **88.94%** | sec212 p.96 |

**Eight of the predecessor's nine periods re-validated cell-by-cell.** Band **82.93% –
89.24%**; the ninth period (Q3 2025) is carried forward, not dropped, and cannot move
either endpoint (§10).

### 2.2 The product basis — Tyvaso DPI

| Period | Gross profit ($M) | Revenue ($M) | Gross margin |
|---|---:|---:|---:|
| Q2 2026 | 275.5 | 326.6 | 84.35% |
| **Q1 2026** | **247.1** | **330.3** | **74.81%** |
| H1 2026 | 522.6 | 656.9 | 79.56% |
| Q2 2025 | 266.7 | 315.2 | 84.61% |
| H1 2025 | 521.1 | 617.7 | 84.35% |
| FY2025 | 1,081.9 | 1,292.5 | 83.71% |
| FY2024 | 885.2 | 1,033.6 | 85.64% |
| FY2023 | 615.5 | 731.1 | 84.19% |

**Tyvaso DPI Q1 2026 at 74.81% is the closest any UTHR basis comes to 72.00 — and it is
2.81 pp above it** (`74.8108% − 72.0000%`; against the comparator's unrounded 72.0410% it
is 2.77 pp above). It is a *quarterly product line with an inventory-reserve distortion*:
[sec215 p.18](https://agentii.ai/v/UTHR/sec215/18) footnote (1) records `$39.2 million` of
Tyvaso DPI inventory reserve expense in Q1 2026 against `$5.8 million` a year earlier —
`$26.8 million` of it an estimated loss on a commercial supply agreement. **It is not
rounded into agreement with 72.00 and must not be quoted as support for it.**

### 2.3 What 72.0 actually is

001's derivation is reproduced exactly from
`theses/001-technology-baseline/report-input.md` lines 322–326:

> *"AMGN Q2 2026: revenue $10,054M - COGS $2,811M = gross profit $7,243M -> $7,243M /
> $10,054M = 72.0%. BMY Q2 2026: revenue $12,973M - COGS $3,726M = gross profit $9,247M ->
> $9,247M / $12,973M = 71.3%."*

Both terms of both legs are verified at their named filings:

- **AMGN**: `Total revenues 10,054` and `Cost of sales 2,811` are filed cells
  ([sec193 p.6](https://agentii.ai/v/AMGN/sec193/6)). `7,243 / 10,054 = 72.0409%` — 001's
  `72.0` is arithmetically exact.
- **BMY**: `Total Revenues 12,973` and `Cost of products sold(a) 3,726` are filed cells
  ([sec232 p.3](https://agentii.ai/v/BMY/sec232/3)). `9,247 / 12,973 = 71.2788%` — 001's
  `71.3` is arithmetically exact.

**Neither figure is a filed gross margin.** AMGN's `72.0409%` is `1 − 28.0%`, the
complement of the *cost-of-sales ratio the issuer publishes*, and AMGN publishes that ratio
on **two denominators in one table** (§3.2). BMY's `71.2788%` is `1 − (3,726 / 12,973)`,
and its cost line is footnoted *"Excludes amortization of acquired intangible assets"* with
the amortization filed as a separate line (§3.3). **The two legs therefore sit on
different, individually unstated bases** — which is DA-30 appearing inside 001's own
derivation rather than inside a platform response.

**001's report also displays a third `72%` it never derives.** The value-chain diagram at
`report-input.md` L807 reads `MRK $16,607M/qtr 72% GM`, one line above
`BMY $12,973M/qtr 71% GM` and two above `AMGN $10,054M/qtr 35% OM` and `UTHR 42% OM`. **A
third issuer's gross margin is therefore asserted at the same 72% with no derivation
anywhere in the report** — the derivation block at L319–331 names only AMGN and BMY. **MRK
was not opened by this artifact**, so this is recorded as unsourced, not as wrong (§10).

### 2.4 The reconciliation 001 never performed: `72.0` and `87.30` are the same quantity under two weightings

This is the finding that resolves the artifact's central question, and it is why the honest
correction is neither "001 is wrong" nor "001 is right."

**`~72%` is defensible as a revenue-weighted cohort aggregate; `72.0` is not the bound for
UTHR, because a buyer adopts a process one issuer at a time.** Computed from the same filed
cells as §2.1:

| Cohort | Revenue ($M) | Gross profit ($M) | Revenue-weighted gross margin |
|---|---:|---:|---:|
| BMY + AMGN (the two 001 derives) | 23,027 | 16,490 | **71.61%** |
| BMY + AMGN + **UTHR** (001's PIL-4 roll-up set, less MRK) | 23,810.3 | 17,173.8 | **72.13%** |

**Adding UTHR — the 87.30% issuer — moves the four-name revenue-weighted cohort margin by
0.52 pp, from 71.61% to 72.13%.** UTHR's revenue is small against the cohort, so the outlier
is nearly invisible in the aggregate and decisive for itself. **Both numbers are correct
statements about different objects**, and 001 made a weighting choice without recording that
it had made one:

- as the **cohort's** incumbent return, `~72%` survives scrutiny (72.13% on the three names
  with filed gross profit);
- as the **barrier the microgravity case must clear**, the bound is **87.30%**, because
  gross margin is earned per product line and per issuer, and no process is adopted by a
  revenue-weighted average.

**001's report never states which object its Line 4 value is.** That omission is the defect;
the arithmetic on both sides is clean.

---

## 3. DA-30 at the benchmark

### 3.1 Five bases at UTHR

The predecessor artifact (`..._recent-quarter_methodology.md` §3) established five named
bases for one concept at UTHR. This artifact confirms the two that the benchmark rests on
and adds the *comparator's* count.

### 3.2 Four bases at AMGN — and 001 selected the second-lowest

AMGN files **no gross-profit line** ([sec193 p.6](https://agentii.ai/v/AMGN/sec193/6):
`Total revenues 10,054` → `Operating expenses:` `Cost of sales 2,811`, `R&D 1,868`,
`SG&A 1,745`, `Other 116` → `Total operating expenses 6,540` → `Operating income 3,514`).
A `us-gaap:GrossProfit` query returns **zero facts** for AMGN — evidence about the tag, and
consistent with the face.

[sec193 p.45](https://agentii.ai/v/AMGN/sec193/45) gives the same cost numerator on two
denominators, in one table, two rows apart:

> `| Cost of sales | $ 2,811 |` … `| % of product sales | 29.5% |` …
> `| % of total revenues | 28.0% |`

[sec193 p.14](https://agentii.ai/v/AMGN/sec193/14) supplies the composition and the
amortization: `Manufacturing cost of sales 2,139` + `Profit share and royalties in cost of
sales 672` = `2,811`; footnote (1): *"amortization of our finite-lived intangible assets
was $890 million … primarily included in Cost of sales."*

| AMGN basis | Arithmetic | Gross margin |
|---|---|---:|
| Cost of sales as % of **product sales** | (9,537 − 2,811) / 9,537 = 6,726 / 9,537 | **70.53%** |
| Cost of sales as % of **total revenues** — **001's selection** | (10,054 − 2,811) / 10,054 = 7,243 / 10,054 | **72.04%** |
| **Manufacturing-only** cost of sales | (10,054 − 2,139) / 10,054 = 7,915 / 10,054 | **78.72%** |
| **Ex-amortization** ($2,811 − $890 = $1,921) | (10,054 − 1,921) / 10,054 = 8,133 / 10,054 | **80.89%** |

**The comparator's "incumbent gross margin" spans 70.53% – 80.89% across four bases, and
001 picked the second-lowest.** The selection is not arithmetically wrong; it is
*basis-unstated*, which is what the register forbids. And the direction matters: on the
higher bases AMGN's margin is **closer** to UTHR's 87.30%, so 001's choice maximised the
apparent gap between incumbent pharma and the 72% barrier the microgravity case was
measured against.

### 3.3 Three bases at BMY

BMY files **neither a gross-profit nor an operating-income subtotal**
([sec232 p.3](https://agentii.ai/v/BMY/sec232/3): `Total Revenues 12,973` → expense lines
→ `Total Expenses 8,887` → `Earnings/(Loss) before income taxes 4,086`). Footnote (a):
*"Excludes amortization of acquired intangible assets."*

| BMY basis | Arithmetic | Gross margin |
|---|---|---:|
| Cost of products sold **incl.** amortization | (12,973 − 3,726 − 437) / 12,973 = 8,810 / 12,973 | **67.91%** |
| **001's selection** — excl. amortization, total revenues | (12,973 − 3,726) / 12,973 = 9,247 / 12,973 | **71.28%** |
| Product-sales denominator | (12,588 − 3,726) / 12,588 = 8,862 / 12,588 | **70.40%** |

**Span 67.91% – 71.28%, three bases.** As at AMGN, 001 selected the basis that made the
comparator's margin highest — here the *most generous* of the three, which narrows the
apparent gap to UTHR.

---

## 4. Detectors, run on BOTH sides of the comparison

**A12: a detector run only on the subject of a comparison cannot detect a comparison
error. A benchmark artifact IS a comparison.** Every detector below is reported for UTHR
**and** for the comparator it is measured against.

### 4.1 The component identity — ill-posed at UTHR, and exactly by how much

The register's component identity is `gross profit − opex = operating_income`. At UTHR it
is **false, in every period tested, by exactly the filed cost of sales**:

| Period | Gross profit | Total operating expenses (`CostsAndExpenses`) | Difference | Filed operating income | Gap | = filed cost of sales |
|---|---:|---:|---:|---:|---:|---:|
| Q2 2026 | 683.8 | 452.5 | 231.3 | 330.8 | **99.5** | 99.5 |
| Q1 2026 | 648.1 | 455.7 | 192.4 | 325.8 | **133.4** | 133.4 |
| H1 2026 | 1,331.9 | 908.2 | 423.7 | 656.6 | **232.9** | 232.9 |
| Q2 2025 | 711.0 | 434.1 | 276.9 | 364.5 | **87.6** | 87.6 |
| H1 2025 | 1,412.9 | 845.7 | 567.2 | 747.3 | **180.1** | 180.1 |
| FY2025 | 2,798.3 | 1,690.2 | 1,108.1 | 1,492.5 | **384.4** | 384.4 |

**Why.** [sec219 p.4](https://agentii.ai/v/UTHR/sec219/4) files `Cost of sales 99.5`
*inside* the `Operating expenses:` block, and `Total operating expenses 452.5` includes
it — while `GrossProfit` (683.8) is already net of it. The identity as written
double-counts cost of sales. It **holds exactly** in two other forms, both verified:

- `Revenue − CostsAndExpenses = OperatingIncome`: `783.3 − 452.5 = 330.8` ✓; `781.5 −
  455.7 = 325.8` ✓; `1,564.8 − 908.2 = 656.6` ✓; `798.6 − 434.1 = 364.5` ✓; `1,593.0 −
  845.7 = 747.3` ✓; `3,182.7 − 1,690.2 = 1,492.5` ✓. **Six of six.**
- `GrossProfit − (CostsAndExpenses − CostOfSales) = OperatingIncome`: `683.8 − (452.5 −
  99.5) = 683.8 − 353.0 = 330.8` ✓.

**And the comparator sits on the other side of the same unstated term.**
[sec193 p.45](https://agentii.ai/v/AMGN/sec193/45) files `Total operating expenses 6,540`
*including* `Cost of sales 2,811`. 001's own AMGN check (`$7,243M − $3,729M = $3,514M`) is
exact **only because `$3,729M = $6,540M − $2,811M`** — 001 silently used opex *net* of cost
of sales. **Two issuers in one comparison, opposite sides of a term definition the
register's detector never states.** That is the finding: the identity is not a property of
the register, it is a property of an unstated choice.

### 4.2 The sign strip — reproduced, localised, and quantified

The predecessor's replacement detector — **served-component overshoot = `2 × |every
negative component|`** — is reproduced here and the mechanism is now identified at the fact
layer. The stripped member is **`us-gaap:ProductAndServiceOtherMember`**, the `Other`
column of the product table, not Adcirca:

| Period | Filed `Other` gross profit (loss) | Fact-layer value | Overshoot `2 × |neg|` | Platform `computed` vs filed total |
|---|---:|---:|---:|---|
| Q2 2026 | **$ (4.2)** | `+4,200,000` | **8.4** | 692.2 vs 683.8 = 8.4 ✓ |
| Q2 2025 | **$ (1.5)** | `+1,500,000` * | **3.0** | 714.0 vs 711.0 = 3.0 ✓ |
| Q1 2026 | **$ (6.8)** | `+6,800,000` | **13.6** | 661.7 vs 648.1 = 13.6 ✓ |
| H1 2026 | **$ (11.0)** | `+11,000,000` | **22.0** | 1,353.9 vs 1,331.9 = 22.0 ✓ |
| H1 2025 | **$ (2.5)** | `+2,500,000` * | **5.0** | 1,417.9 vs 1,412.9 = 5.0 ✓ |
| FY2025 | **$ (14.0)** | `+14,000,000` | **28.0** | 2,826.3 vs 2,798.3 = 28.0 ✓ |

\* The fact-layer magnitude for these two rows is reconstructed from the overshoot identity
rather than read directly; the other four are read facts. The filed parentheticals for all
six are read cells
([sec219 p.20](https://agentii.ai/v/UTHR/sec219/20) for four of them,
[sec215 p.18](https://agentii.ai/v/UTHR/sec215/18) and
[sec212 p.96](https://agentii.ai/v/UTHR/sec212/96) for the rest).

**The filed side closes exactly, which is what makes the platform side a defect rather than
a source ambiguity.** In every period read, the product table foots three ways — revenue,
cost of sales, and gross profit — with `Other` **negative**:

- Q2 2026: `275.5 + 117.1 + 108.9 + 119.6 + 63.2 + 3.7 − 4.2 = 683.8` ✓ and revenue
  `326.6 + 126.0 + 126.3 + 125.7 + 65.2 + 6.7 + 6.8 = 783.3` ✓ and cost
  `51.1 + 8.9 + 17.4 + 6.1 + 2.0 + 3.0 + 11.0 = 99.5` ✓
- Q1 2026: `247.1 + 118.6 + 110.5 + 128.2 + 48.6 + 1.9 − 6.8 = 648.1` ✓
- H1 2026: `522.6 + 235.7 + 219.4 + 247.8 + 111.8 + 5.6 − 11.0 = 1,331.9` ✓
- Q2 2025: `266.7 + 148.8 + 120.4 + 117.2 + 55.6 + 3.8 − 1.5 = 711.0` ✓
- H1 2025: `521.1 + 304.1 + 244.8 + 229.6 + 108.6 + 7.2 − 2.5 = 1,412.9` ✓
- FY2025: `1,081.9 + 558.5 + 477.5 + 468.2 + 209.3 + 16.9 − 14.0 = 2,798.3` ✓

**Six of six, exact, on the filed side.** The platform's overshoot is `2 × |Other|` exactly,
six of six, on the served side. **Verdict: DA-23 CONFIRMED — a seventh instance of the
mechanism, localised to one dimension member and one column.**

**DA-26 does not reproduce here.** 122 duration facts across `GrossProfit`,
`CostsAndExpenses` and `OperatingIncomeLoss` were read; every label matches the filed
caption. Recorded as **NOT-REPRODUCED on this population** — degree-of-freedom kind 4
(mechanism-population identity) does not apply, because the population was chosen by value
family, not by the mechanism's own property.

### 4.3 Detector availability vs power — A16, with the reasoning restated

The register carries two detector axes. Both are reported for both issuers:

| Axis | UTHR | Comparator (AMGN) | Verdict |
|---|---|---|---|
| **1 — gross-profit line on the statement face** | **NO** | **NO** | Available-but-powerless at both |
| **2 — `OperatingIncomeLoss` filed as a first-class consolidated subtotal** | **YES** | **YES** | Available |

At UTHR an 87.30% gross margin sits far above any operating margin the gross-profit bound
could ever catch, so the registered bound found **0 of 11 strips** — the register's own
margin-conditioning note predicts exactly this, one level up. **Availability and power are
separate questions, and this issuer is the proof.** The replacement detector is the one that
works, and it is the one used above.

### 4.4 The subtotal sign axis is UNEXERCISED on both sides

**UTHR**: 61 `OperatingIncomeLoss` facts, 60 retrieved in one page, **every one positive**.
**AMGN**: 61 facts, 40 retrieved, **every one positive**. Neither issuer has a filed-negative
operating subtotal in the window, so the sign test on that axis **can neither pass nor
fail**. Per A17, a unidirectional concept absorbs the sign into the weight and a sign test
on it is vacuous. **Recorded as `UNEXERCISED` — not as clean, and not as a passing test.**

**`validate_calculation` was run and reproduces the predecessor**: **17 pass / 1 warn / 10
fail of 28 arcs**, on a filing whose Q2 2026 `GrossProfit` line passes at
`683,800,000 / 683,800,000 diff 0` — and every failure at a shared `period_end`. Per A14 this
tool is **constitutively incapable** of detecting the strip it runs on, because the
`reported` column shares the stripped store. **No verdict in this artifact rests on a
`validate_calculation` pass.**

---

## 5. P10 — which gates are reached, and which are assumed

**P10 — the Orbital-Compute Underwriting Rule** requires all five gates before an
orbital-compute thesis may be *specified*
(`theses/001-technology-baseline/plan.md` L126): **gate 1 revenue/offtake; gate 2 radiator
derivation; gate 3 array derivation; gate 4 launch-cost-vs-F5; gate 5 radiation statement.**
`theses/002-evidence-validation/plan.md` L311 records 002's position: *"002 validates F2's
constants; it does not underwrite orbital compute, value it, or propose a position. P10
gates underwriting."*

**Verdict for this artifact: P10 reaches 0 of its 5 gates here.** Not "binds partly" as at
SPCX — **zero**, and for a reason that is the mirror image of SPCX's:

| Gate | Reached by this artifact? | Why |
|---|---|---|
| **1 — revenue / offtake** | **No** | No orbital-compute revenue or offtake exists in evidence, and no UTHR filing can supply one. The benchmark is not gate 1; it is the *number gate 1's economics would have to clear*. |
| **2 — radiator derivation** | **No** | No thermal derivation is in UTHR's filings. The `sec219` p.20 footnote records an **inventory reserve** ($19.2M Q2 2026, $64.1M H1 2026), not a thermal input. |
| **3 — array derivation** | **No** | No area or power-per-mass content. |
| **4 — launch cost vs the ~$46/kg F5a floor** | **No** | UTHR has no launch exposure of any kind. **This is the gate that bound at SPCX**, and it is invisible from here. |
| **5 — radiation statement** | **No** | No radiation content. |

**What P10's zero-reach means, stated as the load-bearing consequence.** The five gates are
all gates on the *orbital* side. This artifact's entire contribution is a **terrestrial**
number — 87.30% — being used as an *orbital* hurdle. **The number is `DEMONSTRATED`; the
bridge between terrestrial gross margin and orbital-compute viability is entirely
assumed.** No gate of P10 tests that bridge. So the corrected benchmark **sharpens the
hurdle without moving any gate**, and a downstream thesis that treats "the barrier is 87.3%"
as a P10 result would be quoting a `DEMONSTRATED` figure into an `UNEXERCISED` slot.

**The PUE/cooling clause of the spec row.** Clause 1 (`Terrestrial PUE and cooling
benchmarks`, P4) is discharged by the VRT artifact, which is where the PUE benchmark
lives in this universe (`spec.md` L538: *"VRT — Terrestrial thermal comparator; supplies
the PUE benchmark for P4"*). **No PUE or cooling figure enters this artifact, and its
absence here is a scope boundary, not a finding** — I did not run an absence test on UTHR's
filing for PUE content, so I record no absence claim at all.

---

## 6. The PIL-7 classification: what the falsifier is, and what is unresolvable

PIL-7's obligation is to classify every 001 falsifier and name the specific source that
would resolve it. PIL-4's falsifier is
`metric=listed_pharma_microgravity_commercial_manufacturing_disclosure, threshold=0,
source=UTHR_MRK_BMY_AMGN_10-K_or_10-Q, op=>`.

**This artifact's finding is that two different objects share one disposition in the spec,
and they should not.**

| Object | Disposition | Named resolving source |
|---|---|---|
| **The PIL-4 falsifier** — a *disclosure count* over four issuers' 10-K/10-Q filings | **Evaluable, and it is a documentary count** | The four issuers' SEC filings, which the platform serves. The check is a positive-disclosure search: `threshold=0, op=>` fires if any listed pharma discloses microgravity commercial manufacturing. |
| **The pillar's underlying data** — what a microgravity buyer's unit economics actually are | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** | Varda is private; no public source carries its unit economics. `spec.md` L364 (*"the clearest case in the workspace"*) and L368 (*"PIL-4's data does not exist publicly"*) are correct **about this object**. |
| **The benchmark the falsifier is measured against** | **Resolved by this artifact** | 87.30%, filed cells, §2.1. |

**These are not the same claim, and the spec runs them together.** L364's
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` is stated of *PIL-4* and justified at L368 by data
absence; L543 separately records UTHR as *"the clearest `UNRESOLVABLE-FROM-PUBLIC-SOURCES`
case (P6)"* — which is P6's **private-company proxy rule**, about Varda, not about PIL-4.
The falsifier itself is a count of disclosures in filings the platform already serves, and
**that count is evaluable today.** A pillar whose falsifier is evaluable but whose data is
absent is a different problem from one whose falsifier is unreachable, and the remedy
differs: the first is scoped, the second is proxied.

**And this artifact records that the spec is already right where 001 is wrong.** The spec
carries the corrected figure in its own universe table — `spec.md` L543: *"UTHR \|
United Therapeutics \| med.medicines_biotech \| 4% \| The clearest
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` case (P6) and the **87.3% gross-margin benchmark**"* —
while 001's Line 4 and its PIL-4 roll-up row carry `72.0`. **The 002 spec and 001 disagree
about the microgravity barrier by 15.3 pp, and the spec is the one that is right.** The
spec's `87.3%` traces to the **1239 UTHR artifact** — same skill, same mode as this one —
so the corrected figure **reached the 002 spec and never reached the 001 headline**. §7
records the correction and its provenance; per the task, **001 is frozen and is not
rewritten.**

**001's PIL-4 roll-up row is where the correction bites hardest.** `report-input.md` L898
reads `MRK, BMY, AMGN, UTHR — must beat a 72% incumbent gross margin`. **UTHR does not face
that bound; it is 15.30 pp above it.** The row names four issuers as subjects of a bound that
one of them has already passed, and **UTHR is the only issuer whose own filed margin is in
evidence at 87.30%.** For the microgravity case this is not a detail: the barrier for the
named incumbent is the **higher** number, and the case is correspondingly harder.

---

## 7. Corrections to 001

**Provenance note, because it decides which document each line number belongs to.**
`theses/001-technology-baseline/report-input.md` is **two documents in one file**: 001's
report occupies **L1–965**, and from **L966** the file is a concatenation of **44 embedded
per-issuer artifacts** (first is `artifacts/AMGN/2026-09-18_2055_unit-economics_methodology.md`;
the UTHR one is `artifacts/UTHR/2026-09-18_1239_unit-economics_methodology.md` at L6362).
Every line cited below is scoped to the document it actually belongs to. **This matters: the
`87.3%` figure is NOT 001's** — it is the **1239 UTHR artifact's**, which has the **same skill
and the same mode as this artifact** and which **001's report never absorbed**.

001's **per-ticker UTHR arithmetic is clean and none of it is corrected here.** Re-verified
from filed cells: revenue `−15.3/798.6 = −1.917%`; operating income `−33.7/364.5 =
−9.246%`; R&D `+12.3/134.0 = +9.179%`; net income `+23.5/309.5 = +7.593%`; diluted EPS
`+0.86/6.41 = +13.417%`; operating margins `330.8/783.3 = 42.232%` and `364.5/798.6 =
45.642%`; R&D intensity `146.3/783.3 = 18.678%`. **Every one reproduces.** The defect is the
headline attribution, its basis, and the unstated weighting object — not the sums.

| # | What 001's report says | What the filings say | Class |
|---|---|---|---|
| 1 | **L57**, Line 4: governing bound `Incumbent terrestrial gross margin` = **72.0 percent**, issuer unstated | `72.0` **is AMGN's** and is not UTHR's. **UTHR's is 87.30%.** 001's report contains **no UTHR gross margin at all** — its only UTHR figure is **L842: `~42%`**, the *operating* margin | **DA-30, attribution** — the load-bearing correction |
| 2 | **L322–326**: the derivation is `1 − COGS/revenue`, presented as the incumbent's return | `72.04%` is `1 − 28.0%`, the complement of **a cost-of-sales ratio**, on a denominator the issuer publishes a second version of on the same page (`29.5%` of product sales → `70.53%`) | **DA-30, basis** — AMGN spans **70.53–80.89%** |
| 3 | **L331 / L374**: *"Two independent buyers cluster within **0.7 points**"* | On unrounded values the gap is **0.7621 pp** (`72.0409 − 71.2788`). **`0.7` is the gap between 001's two ROUNDED figures** | **Rounding into agreement** — understates the gap |
| 4 | **L807**: the value-chain diagram asserts `MRK … 72% GM` | **No derivation for MRK appears anywhere in 001's report** — L319–331 names only AMGN and BMY. A third `72%` is displayed that the report never derives. **MRK not opened by this artifact** (§10) | **Unsourced third leg** |
| 5 | **L898** (PIL-4 roll-up): `MRK, BMY, AMGN, UTHR — must beat a 72% incumbent gross margin` | **UTHR does not face that bound — it is 15.30 pp ABOVE it.** UTHR is the one issuer in the set that has already passed it. The bound is a floor for UTHR, not a hurdle | **The load-bearing consequence** |
| 6 | **L56** presents `72.0` as a *governing bound* with no weighting object stated | It is a viable **revenue-weighted cohort aggregate** (72.13%, §2.4) and simultaneously **the wrong bound for the subject issuer** (87.30%). Both true; 001 records neither | **Unstated weighting choice** |
| 7 | 001's AMGN component identity `$7,243M − $3,729M = $3,514M` (**embedded AMGN artifact, L1024**) | **Exact** — but only because `$3,729M = $6,540M − $2,811M`, i.e. opex **net** of cost of sales. UTHR's served `CostsAndExpenses` **includes** it | **Basis dependency invisible in the check** (§4.1) |
| 8 | The **embedded BMY artifact** (L1503) tables the cohort with MRK's `Implied gross margin` cell **blank**, then (L1506) a `Combined` row of `$12,700M+` and `~72%` | `$12,700M = MRK R&D $9,741M + BMY R&D $2,959M` **exactly** — an R&D sum in a gross-profit column. And `~72%` is the **unweighted mean of two rounded figures** (`(71.3 + 72.0)/2 = 71.65`), not a cohort margin. The table's own `$12,700M / $39,634M = 32.04%` | **The convergence is not a cohort statistic** — and it is *also* the correct cohort answer by coincidence (§2.4) |

**The corrected headline, for downstream use — stated as two objects, because 001's one
number was doing two jobs:**

```
Incumbent terrestrial gross margin — COHORT, revenue-weighted, BMY+AMGN+UTHR
  = 72.13%  (filed gross profit $17,173.8M / filed revenue $23,810.3M)
  → 001's ~72% survives as an AGGREGATE. MRK contributes no filed margin.

Incumbent terrestrial gross margin — UTHR, consolidated, total-revenues basis, Q2 2026
  = 87.30%  (filed gross profit $683.8M / filed total revenues $783.3M)
  → THIS is the barrier a microgravity process must clear for UTHR, +15.30 pp above the
    cohort figure (unrounded +15.2563 pp). Eight-period filed band 82.93%–89.24%.
```

**And the correction has now been independently derived three times without reaching 001's
headline**: the 1239 UTHR artifact computed `87.3%` and wrote *"UTHR's 87.3% gross margin is
the hurdle rate"* (L6489); the 1500 predecessor recorded it; this artifact re-verifies it
cell-by-cell from the filing. **001's Line 4 still reads `72.0`.** Per the task, **001 is
frozen and is not rewritten.**

---

## 8. Is UTHR's weight justified on the corrected benchmark?

**001's weights, from `report-input.md` L12 — the four PIL-4 buyers:** `UTHR 7% ; MRK 3% ;
BMY 3% ; AMGN 2%`. **002's spec carries UTHR at 4%** (`spec.md` L543). So the question is
answerable with numbers on both sides.

**UTHR carries the largest weight of the four named buyers, and on the corrected benchmark it
is the least representative of them.** On the 72.0% reading UTHR's weight rested on an
apparent likeness — a pharma buyer whose margin sat near the barrier, i.e. a plausible
near-term adopter. On the filed number **UTHR is the outlier of the set**: its 87.30% is
**16.02 pp above BMY's 71.28%** and **15.26 pp above AMGN's 72.04%**, and it sits **15.30 pp
above the very bound its own roll-up row is measured against.** **The weight is therefore
inverted relative to the pillar's own claim**: the issuer least like a marginal, cost-pressured
buyer holds 7%, more than twice either of the two that are.

**Three answers, because the weight is doing two jobs:**

1. **As a research subject — an issuer likely to procure a microgravity process — 7% is not
   justified and the correction argues it DOWN.** An 87.30% gross margin is an incumbent a
   lower-cost orbital process must beat by a wider margin: a harder case and a slower
   catalyst. 001's own L842 already shows the honest UTHR number as `~42%` — an *operating*
   margin, and one the report never connects to the 42.23% the filings support.
2. **As the benchmark source — the issuer whose filed margin defines the barrier — the weight
   is justified but for a different reason than 001 gave.** Here UTHR is not a buyer at all;
   it is the *measurement*, and the measurement is now `DEMONSTRATED` where 001's 72.0 was
   `DERIVED` from a comparator's cost complement.
3. **As a defect site, 4% is the right order and the spec already has it.** This is exactly
   the role `spec.md` L551–554 assigns: *"Four of these seventeen names are in the universe
   for a single reason: they are defect sites, not research subjects."* §4.1 and §4.2 put
   UTHR at the centre of two detector failures — the ill-posed component identity and a
   seventh DA-23 localisation.

**Verdict: the spec's 4% is defensible; 001's 7% is not, on either reading.** Raising UTHR's
weight on the corrected benchmark would be weighting it for having been misattributed.

---

## 9. DA-31 — the cross-holding check (queued, not registered)

The queued entry asks whether an earnings figure is a function of a stake's **carrying
value** rather than of operations. Tested here against the one UTHR concept the benchmark
touches:

| Test | Filed cells | Result |
|---|---|---|
| Does the operating line carry a stake term? | `Operating income 330.8`; `Other income (expense), net 13.3` filed **below** it; `330.8 + 41.9 = 372.7 = Income before income taxes` ✓ | **NO — the operating line is structurally clean** |
| Magnitude of the stake-sensitive line | `Other income (expense), net`: `13.3 / (0.1) / (33.0) / (4.4)` (Q2 2026 / Q2 2025 / H1 2026 / H1 2025); Q1 2026 = `−33.0 − 13.3 = **−46.3**` | Swing of `59.6` between Q1 and Q2 2026 |
| As a share of net income | `13.3 / 333.0 = **3.99%**` of Q2 2026; `33.0 / 607.9 = **5.43%**` of H1 2026 | **An order of magnitude below GOOG's 68.7%** |
| The HLBV dilution-gain mechanism (MSFT precedent) | Absent — a dilution gain recognised as a stake *falls* requires an equity-method carrying value the filings do not present in the periods read | **Mechanism ABSENT** |

**Verdict: DA-31 is NOT a defect at UTHR, and it does not touch the benchmark.** The
$330.8M operating subtotal that produces 42.23% and, indirectly, the 87.30% gross margin,
contains no equity-stake term. **The composition of the `Other income (expense), net` line
is recorded as `CLAIMED`-by-predecessor, not `DEMONSTRATED` here** — the predecessor read
`sec219` p.39 and recorded that it is attributed to net unrealized gains and losses on
equity securities; **this artifact did not re-read p.39**, so it does not assert the
composition. The *position* and *magnitude* tests above, which are what the contamination
question turns on, are `DEMONSTRATED` from p.4 alone.

---

## 10. What could NOT be verified, by KIND

Named per A13's taxonomy, with the A19-proposed kind 7 noted where it applies.

| # | Item | Kind | Why |
|---|---|---|---|
| 1 | **Q3 2025 period** of the UTHR margin band | **Kind 2 — genuine absence from the served set, partially** | The predecessor validated nine periods; this artifact re-validated eight cell-by-cell. Q3 2025 can move neither band endpoint (`82.93%` from Q1 2026, `89.24%` from FY2024, both re-read), so the *band* is not exposed — but the ninth period is `PARTIALLY-VALIDATED-BY-PLATFORM`. |
| 2 | **Fact-layer magnitude** of `Other` for Q2 2025 and H1 2025 | **Kind 1 — ingestion-scope** | The overshoot identity fixes them at `+1,500,000` / `+2,500,000` exactly, but I did not read those two facts directly. The filed parentheticals **are** read cells. |
| 3 | **Composition of `Other income (expense), net`** | **Kind 2 — source-scope, self-imposed** | p.39 not re-read (§9). Recorded as `CLAIMED`-by-predecessor. |
| 4 | **Any PUE or cooling disclosure in UTHR's filings** | **Kind 5 — datum class not in the corpus, and I ran no absence test** | PUE/cooling is VRT's clause of the spec row. **I am recording no absence claim**, because a keyword zero is evidence about the keyword, not the filing. |
| 5 | **MRK's third `72%`** — `report-input.md` L807 `MRK … 72% GM`, and the embedded BMY artifact's L1503 cell leaving MRK's `Implied gross margin` **blank** | **Kind 2 — scope, and the absence is 001's own** | **MRK was not opened by this artifact.** 001's report derives no MRK margin, so the diagram's third `72%` is `UNVALIDATED-BY-PLATFORM` here. **The blank cell at L1503 is 001's own absence, not mine** — that is a finding (§7 row 8), not a gap in this artifact. The cohort reconciliation in §2.4 therefore rests on **three** issuers, not four. |
| 6 | **DA-31's HLBV mechanism at UTHR** | **Kind 2 — absence established by reading, not by query** | Established by reading the statements of operations face and finding no equity-method carrying value presented; a stronger absence test would need the balance-sheet note, which is out of this artifact's scope. |
| 7 | **The whole PUE / thermal leg** | **Kind 4 — mechanism-population identity, avoided** | Recorded as a scope boundary (§5), not as a clean result. Not counted in any denominator here. |

**A negative control that travelled with this artifact.** `processing_status: pending` is
**non-discriminating** and was not used as an ingestion-absence marker anywhere above. All
eight cited pages served full cell-level text.

---

## 11. Carry-forwards

1. **`check_contract.py`'s `basis_named` heuristic cannot see this artifact's defect class.**
   The DA-30 regex fires on a *multi-basis concept quoted without a basis word*. 001's Line 4
   defect is the **opposite**: 72.0 is quoted with a basis-shaped label
   (*"Incumbent terrestrial gross margin"*) that names **no issuer**. **A label that names a
   metric but not its issuer passes the heuristic cleanly.** Proposed: extend `BASIS_WORD`
   to require an issuer for any figure in a cross-issuer comparison.
2. **The register's component identity needs a term-definition field.** §4.1 shows the
   identity is true or false depending on whether `opex` includes cost of sales, and the two
   issuers in *one* comparison are on opposite sides. This is DA-30's mechanism appearing
   inside the register's own detector.
3. **The `Other`/`ProductAndServiceOtherMember` strip is a new localisation of DA-23** — a
   *dimension-member* strip on the gross-profit concept, recoverable by `2 × |component|`.
   It should be added to DA-23's instance list as instance **#8**, with UTHR as the site.
4. **`reconciliation_terms_located` should test the *comparator's* leg too.** It fired
   nothing here because the body names sources; the defect it was written for is invisible
   to a single-document check (**A12**).
5. **The PIL-4 disposition should be split** (§6): the falsifier is evaluable; the pillar's
   data is `UNRESOLVABLE-FROM-PUBLIC-SOURCES`. One disposition for both objects will keep
   stopping 011 from sizing against a catalyst that *can* fire.
6. **A corrected figure has now been derived three times and absorbed zero times.** The
   **1239** UTHR artifact — same skill, same mode as this one — computed `87.3%` and wrote
   *"UTHR's 87.3% gross margin is the hurdle rate"*; the **1500** predecessor recorded the
   correction; this artifact re-verifies it cell-by-cell from `sec219`. **`report-input.md`
   L57 still reads `72.0` and L898 still assigns that bound to a set including UTHR.** The
   register has no rule requiring a downstream artifact's correction to reach the upstream
   headline it corrects — `upstream_stale: "001@1.2.0"` *records* the staleness without
   triggering anything. **A correction that cannot propagate is a finding that will be
   re-derived a fourth time.**
7. **`report-input.md` is two documents in one file (L1–965 are 001's; L966+ are 44 embedded
   artifacts), and line-number citations into it are therefore ambiguous by default.** Any
   census that greps this file will attribute downstream artifacts' findings to 001 — the
   `87.3%` at L6403 is the clearest case, and I initially read it as 001's own. **Line
   citations into `report-input.md` should carry the owning document, not just the line.**

---

## Sources

| # | Citation | URL |
|---|---|---|
| 1 | UTHR Q2 2026 10-Q, statements of operations | https://agentii.ai/v/UTHR/sec219/4 |
| 2 | UTHR Q2 2026 10-Q, Note 11 product gross profit table | https://agentii.ai/v/UTHR/sec219/20 |
| 3 | UTHR Q1 2026 10-Q, Note 11 product gross profit table | https://agentii.ai/v/UTHR/sec215/18 |
| 4 | UTHR FY2025 10-K, Note 13 segment gross profit table | https://agentii.ai/v/UTHR/sec212/96 |
| 5 | AMGN Q2 2026 10-Q, condensed consolidated statements of income | https://agentii.ai/v/AMGN/sec193/6 |
| 6 | AMGN Q2 2026 10-Q, segment note and amortization footnote | https://agentii.ai/v/AMGN/sec193/14 |
| 7 | AMGN Q2 2026 10-Q, MD&A operating expenses | https://agentii.ai/v/AMGN/sec193/45 |
| 8 | BMY Q2 2026 10-Q, consolidated statements of earnings | https://agentii.ai/v/BMY/sec232/3 |
