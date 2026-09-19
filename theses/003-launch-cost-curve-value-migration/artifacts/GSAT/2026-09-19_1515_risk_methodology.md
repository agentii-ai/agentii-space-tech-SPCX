---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-6
ticker: GSAT
skill: risk
mode: methodology
generated_at: 2026-09-19T15:15:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "953fc5d396e7"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: >-
      A platform extraction defect: a filed negative served as a positive of identical
      magnitude. At GSAT the strip DOES reach OperatingIncomeLoss, so the register's carried
      "7.4% operating margin" is the absolute value of a filed operating LOSS of −7.37%.
      The filed statement governs; the served value is not a restatement.
  - da_id: DA-30
    chosen_reading: >-
      Two bases on one concept collapsed without a basis field. Live at GSAT: the Q1 2026
      standalone filing and the 6M 2026 filing report the same concept on different
      bases because ASU 2025-07 was adopted retrospectively mid-year. Every period figure
      below carries its basis and its source filing.
  - da_id: DA-24
    chosen_reading: >-
      Non-operating contamination measured, not assumed. GSAT's other-income block is
      reported separately on the as-filed statement and is never netted into operating
      income; the block's share of the bottom line is computed for four period bases and
      the results are reported as a range, not a point.
  - da_id: DA-25
    chosen_reading: >-
      Applied in the opposite direction from IRDM: GSAT's subscribers and ARPU ARE filed in
      audited tables, so the per-unit metrics here are reproducible. Recorded because the
      census must distinguish an untestable DA-25 (IRDM) from a testable one (GSAT).
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
citations:
  - figure: "GSAT sec166 p.5"
    ticker: GSAT
    citation_id: sec166
    page_no: 5
    url: https://agentii.ai/v/GSAT/sec166/5
    located_via: read_source_pages
  - figure: "GSAT sec128 p.48"
    ticker: GSAT
    citation_id: sec128
    page_no: 48
    url: https://agentii.ai/v/GSAT/sec128/48
    located_via: read_source_pages
  - figure: "GSAT sec166 p.37"
    ticker: GSAT
    citation_id: sec166
    page_no: 37
    url: https://agentii.ai/v/GSAT/sec166/37
    located_via: read_source_pages
  - figure: "GSAT sec166 p.36"
    ticker: GSAT
    citation_id: sec166
    page_no: 36
    url: https://agentii.ai/v/GSAT/sec166/36
    located_via: read_source_pages
  - figure: "GSAT sec166 p.33"
    ticker: GSAT
    citation_id: sec166
    page_no: 33
    url: https://agentii.ai/v/GSAT/sec166/33
    located_via: read_source_pages
  - figure: "GSAT sec166 p.6"
    ticker: GSAT
    citation_id: sec166
    page_no: 6
    url: https://agentii.ai/v/GSAT/sec166/6
    located_via: read_source_pages
  - figure: "GSAT sec166 p.42"
    ticker: GSAT
    citation_id: sec166
    page_no: 42
    url: https://agentii.ai/v/GSAT/sec166/42
    located_via: read_source_pages
  - figure: "GSAT sec166 p.15"
    ticker: GSAT
    citation_id: sec166
    page_no: 15
    url: https://agentii.ai/v/GSAT/sec166/15
    located_via: read_source_pages
  - figure: "GSAT sec128 p.35"
    ticker: GSAT
    citation_id: sec128
    page_no: 35
    url: https://agentii.ai/v/GSAT/sec128/35
    located_via: read_source_pages
  - figure: "GSAT sec166 p.28"
    ticker: GSAT
    citation_id: sec166
    page_no: 28
    url: https://agentii.ai/v/GSAT/sec166/28
    located_via: read_source_pages
  - figure: "GSAT sec166 p.32"
    ticker: GSAT
    citation_id: sec166
    page_no: 32
    url: https://agentii.ai/v/GSAT/sec166/32
    located_via: read_source_pages
  - figure: "GSAT sec166 p.34"
    ticker: GSAT
    citation_id: sec166
    page_no: 34
    url: https://agentii.ai/v/GSAT/sec166/34
    located_via: read_source_pages
  - figure: "GSAT sec166 p.43"
    ticker: GSAT
    citation_id: sec166
    page_no: 43
    url: https://agentii.ai/v/GSAT/sec166/43
    located_via: read_source_pages
  - figure: "GSAT sec166 p.40"
    ticker: GSAT
    citation_id: sec166
    page_no: 40
    url: https://agentii.ai/v/GSAT/sec166/40
    located_via: read_source_pages
key_metrics:
  operating_margin_pct_3m: -7.37
  retained_earnings_accumulated_deficit_thousands: -2206570
  stripped_concepts: 4
  monotonicity_violations: 3
---

# GSAT × risk — the register has absorbed the platform's own defect

## The finding

**The 003 register carries GSAT's operating margin as "7.4% — the thinnest operator margin in
the universe". The filed Q2 2026 figure is an operating LOSS of $(4,775) thousand, which is
−7.37% of revenue. The platform serves that cell as `+4,775,000`. The register's unsigned 7.4%
is the absolute value of a loss, and it is not reproducible at any sign convention other than
`|x|`.**

This is the single most load-bearing GSAT result, and it is a second-order failure rather than a
first-order one. The platform's DA-23 strip is the first-order defect. The second-order defect
is that **the thesis's own register consumed a stripped cell and recorded it as a positive
margin, then ranked the issuer on it.** A screen built on the served field inverts: GSAT's worst
quarter is served as its thinnest positive margin.

Three consequences follow, and they are the substance of this artifact:

1. **The "7.4%" claim must be withdrawn and restated as −7.4%.** It is a loss.
2. **The margin series is sign-alternating and violently non-monotone**, so "thinnest margin" is
   not a stable property of the issuer — it is one quarter's magnitude.
3. **GSAT is the only issuer in this cohort where the strip is detectable from the platform's
   own served values, without reading a filing at all** (§3). That makes GSAT the positive
   control for DA-23 and, per the task's mandate, the census is now run: **PRESENT, not CLEAN.**

## 1. Component identity, opex definition, units

**Opex definition used throughout: the `Total operating expenses` line as filed at GSAT —
INCLUSIVE of cost of sales** (cost of services exclusive of D&A and accretion, plus cost of
subscriber equipment sales), marketing and general and administrative, stock-based
compensation, and depreciation, amortisation and accretion.

| Period | Revenue ($k) | Opex ($k) | `revenue − opex` ($k) | Filed operating income ($k) | Margin |
|---|---|---|---|---|---|
| 3M 2026 | 64,772 | 69,547 | (4,775) | **(4,775)** ✓ | **−7.37%** |
| 3M 2025 | 67,148 | 61,002 | 6,146 | **6,146** ✓ | +9.15% |
| 6M 2026 | 134,836 | 131,441 | 3,395 | **3,395** ✓ | +2.52% |
| 6M 2025 | 127,180 | 129,535 | (2,355) | **(2,355)** ✓ | −1.85% |
| FY2025 | 272,986 | 265,556 | 7,430 | **7,430** ✓ | +2.72% |
| FY2024 | 250,349 | 251,298 | (949) | **(949)** ✓ | −0.38% |
| FY2023 | 223,808 | 223,973 | (165) | **(165)** ✓ | −0.07% |

The identity closes exactly on **7 of 7 period-pairs**. `[📄 GSAT 10-Q p.5](https://agentii.ai/v/GSAT/sec166/5)`
`[📄 GSAT 10-K p.48](https://agentii.ai/v/GSAT/sec128/48)`

**⚠️ The gross-profit bound is UNEXERCISED at GSAT, not passed.** GSAT files **no gross-profit
line**. The inclusive-versus-exclusive opex cross-check cannot run here. Recorded
`UNEXERCISED`.

**The served layer is arithmetically IMPOSSIBLE, and that is the detector.** Read the served
values in the row order above: Q2 2026 is served as **+4,775,000** and 6M 2026 as
**+3,395,000**. A three-month magnitude cannot exceed the six-month magnitude that contains it
if both are genuinely positive. The served stack violates monotonicity, and the only
reconciliation is that one of the two has lost its sign. **This detector needs no filing, no
concept, and no component identity — only the platform's own two numbers.**

**Units.** As-filed statements are in **thousands**; the platform's `value_numeric` is in
**dollars** (filed `(4,775)` thousands ↔ served `4,775,000`). The 1,000× offset is systematic
across the universe and is a unit conversion, not a defect — but it is the reason a consumer
comparing the two layers without normalising sees a discrepancy of three orders of magnitude.

## 2. DA census at GSAT — PRESENT, and the register's `CLEAN` is refuted

The task's mandate for GSAT is explicit: 002 recorded that GSAT carries **no** DA census, so the
checks had to be run here and anything unattempted marked `UNEXERCISED`, **never CLEAN**. The
register's finding F7 ("PL and GSAT carry no DA census") is a statement about *coverage*, not
about *state*. The state is now known.

### 2.1 DA-23 — CONFIRMED, ≥18 strip cells across 4 concepts

| Concept | Served positive against a filed negative | Cells |
|---|---|---|
| `us-gaap:OperatingIncomeLoss` | Q2 2026 +4,775,000 (filed `(4,775)`); 6M 2025 +2,355,000 (filed `(2,355)`); FY2024 +949,000 (filed `(949)`); FY2023 +165,000 (filed `(165)`); Q1 2025 +8,501,000 (derived filed `(8,501)`); Q3 2024 +9,434,000 (derived); 9M 2024 +3,300,000 (derived) | **7** |
| `us-gaap:NetIncomeLoss` | Q2 2026 +26,539,000 (filed `(26,539)`); 6M 2026 +41,357,000 (filed `(41,357)`); FY2025 +8,651,000 (filed `(8,651)`); FY2024 +63,164,000 (filed `(63,164)`); Q1 2025 +17,331,000 (derived) | **5** |
| `us-gaap:NetIncomeLossAvailableToCommonStockholdersBasic` | Q2 2026 +29,183,000 (filed `(29,183)`); 6M 2026 +46,616,000 (filed `(46,616)`); FY2025 +19,256,000 (filed `(19,256)`); FY2024 +73,798,000 (filed `(73,798)`); Q1 2026 +20,035,000 | **5** |
| `us-gaap:RetainedEarningsAccumulatedDeficit` — **a BALANCE SHEET cell** | 2026-06-30 served +2,206,570,000 (filed `(2,206,570)`); 2025-06-30 served +2,126,269,000; 2024-06-30 served +2,087,861,000 | **3+** |

**Genuine positives — NOT stripped**, and their presence is what makes GSAT's regime the
informative one: `OperatingIncomeLoss` FY2025 (+7,430,000), Q2 2025 (+6,146,000), Q3 2025
(+10,156,000), 9M 2025 (+7,801,000), Q1 2026 (+8,170,000), 6M 2026 (+3,395,000), Q3 2024
(+9,434,000), Q2 2024 (+1,422,000), Q1 2024 (+4,712,000), 6M 2024 (+6,134,000), and the whole
2021–2022 run; `NetIncomeLoss` Q2 2025 (+19,208,000), 6M 2025 (+1,877,000), Q3 2025
(+1,090,000), 9M 2025 (+2,967,000), and all four 2024 periods.

### 2.2 The four strip regimes — a taxonomy the register does not yet carry

Running the census across the five issuers this artifact set covers yields **four distinct
regimes**. This is the reusable result, because it explains why a per-issuer clearance built on
any single detector is unsound.

| Issuer | Regime | Served stack behaviour | Detector that works | Detector that fails |
|---|---|---|---|---|
| **RKLB** | **UNIFORM** — never a positive operating income in its history | closes in `\|x\|` space; monotonic | component identity | period arithmetic; any sign heuristic |
| **PL** | **UNIFORM** — same | closes in `\|x\|` space; monotonic | component identity | period arithmetic |
| **YSS** | **UNIFORM** — same | closes in `\|x\|` space; monotonic | component identity | period arithmetic |
| **IRDM** | **CONCEPT-SELECTIVE** — top-of-statement untouched | positive cells genuine | component identity; concept coverage | any test sampling top-of-statement concepts |
| **GSAT** | **MIXED** — positive and stripped periods interleaved | **violates monotonicity in 3 places** | **period arithmetic alone**; component identity | a uniform-regime assumption |

**⚠️ And DA-23 is not an income-statement defect.** §2.6(a) shows it reaching
`RetainedEarningsAccumulatedDeficit` at GSAT — the **equity section of the balance sheet**. Every
census in the register counts it on flow metrics. A reader who has learned "check the P&L sign"
has learned half the defect.

**The consequence is a correction to the register.** 003 records DA-23 at RKLB as "12 of 12
periods" and reasons that "because RKLB has never had positive operating income, the strip is
INVISIBLE to any heuristic". Both halves are right and the reasoning generalises further than
the register states: the invisibility is not a property of RKLB — it is a property of the
**uniform regime**, and it applies identically at PL and YSS. **GSAT is the counterexample, and
it is the only issuer in this cohort where the defect is arithmetically self-evidencing.**

### 2.3 Three monotonicity violations at GSAT, stated so they can be checked

| Served 3M figure | Served covering figure | Violation |
|---|---|---|
| Q2 2026 `OperatingIncomeLoss` +4,775,000 | 6M 2026 +3,395,000 | 3M > 6M |
| Q1 2025 `OperatingIncomeLoss` +8,501,000 | 6M 2025 +2,355,000 | 3M > 6M |
| Q3 2024 `OperatingIncomeLoss` +9,434,000 | 9M 2024 +3,300,000 | 3M > 9M |

Each violation resolves to exactly one stripped negative in the filed statement. In all three
cases the filed value is the **loss** of the served magnitude. Three independent instances; one
mechanism.

### 2.4 DA-30 — CONFIRMED, a mid-year retrospective adoption

Served `NetIncomeLoss` for **Q1 2026 standalone** is `+17,420,000`, i.e. a filed Q1 2026 net loss
of **$(17,420) thousand**. But **6M 2026 `$(41,357)` minus Q2 2026 `$(26,539)` gives Q1 2026 =
$(14,818) thousand** — a difference of **2,602 thousand**. The 10-Q states the reconciliation
itself: *"The $2.6 million loss recorded during the first quarter of 2026 was reclassified back
to the derivative asset"* on adoption of **ASU 2025-07**, which GSAT adopted **in Q2 2026**.
`[📄 GSAT 10-Q p.37](https://agentii.ai/v/GSAT/sec166/37)` `[📄 GSAT 10-Q p.36](https://agentii.ai/v/GSAT/sec166/36)`

**So Q1 2026 is filed on a pre-adoption basis and 6M 2026 on a post-adoption basis, on the same
concept, with no basis field.** That is DA-30 — two bases on one concept collapsed — and it is
**live at GSAT**, not hypothetical. The same adoption moved **$11.8M / $12.5M** of interest that
"was not present in 2025" and made it "eligible for capitalization", and raised capitalised
interest by **$13.8M / $15.7M**. A consumer reading Q1 2026 and 6M 2026 as one series is mixing
bases. `[📄 GSAT 10-Q p.36](https://agentii.ai/v/GSAT/sec166/36)`

### 2.5 The carried "93% of net income is non-operating" — TESTED, NOT REPRODUCIBLE AS STATED

This figure was carried into the task and it does not reproduce at 93% on any period basis.
Computing the non-operating-plus-tax block as a share of the bottom line:

| Period basis | Non-operating + tax ($k) | Net income (loss) ($k) | Share |
|---|---|---|---|
| 3M 2026 (as filed) | (21,764) | (26,539) | **82.0%** |
| 6M 2026 (as filed) | (44,752) | (41,357) | **108.2%** |
| 3M 2025 (as filed) | 13,062 | 19,208 | **68.0%** |
| FY2025 (as filed) | (16,081) | (8,651) | **185.9%** |
| FY2024 (as filed) | **62,215** — a **derived difference**, not a filed line | (63,164) | **98.5%** |
| 6M 2026 (**served, i.e. stripped**) | (41,357 − 3,395) | 41,357 | **91.8%** |

**The FY2024 row is the closest to the claim and is disqualifying on its own terms.** FY2024
files an operating loss of $(949) thousand against a net loss of $(63,164) thousand; the
**$62,215 thousand** gap that would produce 98.5% **appears nowhere in the statement** — it is
our subtraction of two filed cells, i.e. a **derived difference, not a filed line**. So even at
its best-fitting period the "93%" is a back-solved ratio with no filed counterpart, which is the
**DA-29 shape** (a reconciliation that closes is not thereby a check) sitting on top of the
**DA-30 basis ambiguity**. The brief's `98.5%` and the four bases above are the same finding from
different periods: **the metric has no filed basis at any of them.**

**The direction is confirmed and the magnitude is not.** Non-operating items and tax dominate
the bottom line on every period basis tested — the reproducible values are 68.0%, 82.0%, 91.8%,
108.2% and 185.9%, spanning a factor of 2.7. The nearest approach to 93% is **91.8% on 6M 2026
computed on the STRIPPED served values** — i.e. the figure is reproducible only by consuming the
platform's defect. The only exact 93% in the neighbourhood is **Total service revenue ÷ Total
revenue = 59,998 / 64,772 = 92.63%**, which is a **revenue** ratio and has nothing to do with
net income. `[📄 GSAT 10-Q p.33](https://agentii.ai/v/GSAT/sec166/33)`

**Disposition: the claim is BASIS-UNIDENTIFIABLE.** It names neither a numerator (other income
net? other income net plus tax? the "$4,181 contingent-interest gain" alone?), nor a period, nor
a form. Registered as a **DA-30 basis ambiguity** with a **DA-25 shape** (a normalised ratio not
reproducible from the audited tables). It is carried here as `CLAIMED`-and-not-reproduced, with
all six reproducible bases reported so a reader can see which one, if any, was meant.

### 2.6 A fourth stripped concept, and a defect that lives in a different layer

Two corrections to the carried GSAT record. Both were re-tested rather than inherited, and both
come back **confirmed with an amendment**.

**(a) `RetainedEarningsAccumulatedDeficit` is ALSO stripped — a fourth DA-23 concept at GSAT.**
The platform serves `2,206,570,000` at 2026-06-30, at 2025-06-30 `2,126,269,000`, at 2024-06-30
`2,087,861,000` — **every one of them positive**. The filed figure is the accumulated **deficit**,
$(2,206,570) thousand.

**This is provable from the equity identity alone, with no page read.** If retained earnings were
genuinely **+**$2,206,570 thousand, then with total assets of **$2,444,812 thousand** the equity
of **$292,613 thousand** would require every other equity component (APIC, treasury, AOCI) to
sum to **−$1,913,957 thousand** — a negative paid-in capital on a company that has raised capital
repeatedly. The arithmetic admits only one sign. `[📄 GSAT 10-Q p.6](https://agentii.ai/v/GSAT/sec166/6)`

So the GSAT strip is **not confined to the income statement** — it reaches the **balance sheet
equity section**, and the register's DA-23 census for this issuer was counted only at the
operating and net-income lines. **≥18 cells, 4 concepts.**

**(b) The accumulated deficit is $(2,206,570) thousand — confirmed — but $2,137M was not a stale
figure, it was the PRIOR YEAR.** Both are true and they are different periods. The correct
current value is **$(2,206,570) thousand**; a reader carrying $2,137M is one period behind.

**(c) ⚠️ The `common_shares_outstanding` defect is in the DERIVED METRICS BLOCK, not the XBRL
fact layer — and that distinction is the finding.** The register records the platform's
`common_shares_outstanding` as the **preferred** count (`149,425`) against a filed common of
**129,563,390** — an **867× error**, wrong in the **conservative** direction, so it never
announces itself.

Re-testing the **XBRL fact layer** for the same quantity returns **correct common counts**, and
they carry the capital-structure discontinuity on their face:

| Instant | Served `CommonStockSharesOutstanding` |
|---|---|
| 2025-02-10 | `1,896,635,805` |
| 2025-02-11 | `126,442,583` |

The ratio is **14.9995** — the **1:15 reverse split effectuated February 10, 2025**, captured as
two instants one day apart. **The fact layer is right and the metrics block is wrong on the same
issuer for the same quantity.** No DA number exists for this class (the register is DA-01…DA-30),
so it is registered here by description. *This is the strongest single argument in this artifact
for the brief's §5 rule: read pages and read facts, never the metrics block.*

**Why (a)–(c) belong in a risk artifact.** All three are *level* errors on cells a risk screen
reads directly — the share count a per-share loss is divided by, the deficit that measures how
much of the equity base has been consumed, and the equity section itself. §1 established the
equity cushion is **12.0%** of assets; a strip in the equity section changes the picture of how
fast that cushion was consumed. And **the `data_freshness` stamp returned with both queries was
`2027-04-12`** — seven months in the future of `as_of = 2026-09-18`, re-confirming the brief's
`UNUSABLE` finding **live**, on the same call that produced the correct share counts.

## 3. Mode — general-risk-factors-identification-assessment

**GSAT's Q2 2026 Item 1A contains a NEGATIVE disclosure that is itself the finding.** The filing
states that there are **no material changes to the risk factors** other than "risks related to
the pending Amazon merger" — i.e. the general risk set is stable **and** is incorporated by
reference to the FY2025 Form 10-K. `[📄 GSAT 10-Q p.42](https://agentii.ai/v/GSAT/sec166/42)`

Two P6 reachability consequences:

- **The general risk set is reachable only through a different filing period.** The current
  document carries its own pointer and nothing else. A census reading Item 1A of the 10-Q alone
  finds one block.
- **GSAT's Item 1 Legal Proceedings is "None".** `[📄 GSAT 10-Q p.42](https://agentii.ai/v/GSAT/sec166/42)`
  That is an affirmative clean, **not** an `UNEXERCISED` — a filed statement that there is
  nothing to report is a datum. It contrasts directly with IRDM, whose regulatory exposure
  includes live federal litigation and a counterparty bankruptcy. **On legal proceedings the
  operator with the smaller balance sheet is the cleaner name**, and the register does not
  currently carry that inversion.

The identifiable general risk set, on the as-filed basis:

- **A wholesaler's revenue concentration.** Wholesale capacity services were **$40,114 thousand =
  62% of total revenue** in 3M 2026 and **$86,381 thousand = 64%** in 6M 2026. Total service
  revenue is **93%** of total revenue. GSAT is not primarily a subscriber-facing business.
  `[📄 GSAT 10-Q p.33](https://agentii.ai/v/GSAT/sec166/33)`
- **A filed annual service fee with an acceleration clause.** The Updated Services Agreements
  carry annual service fees of **$30M accelerated**. `[📄 GSAT 10-Q p.15](https://agentii.ai/v/GSAT/sec166/15)`
- **The fixed cost base is a live drag at a 15-year satellite life.** D&A fell **$6.2M / $10.1M**
  as second-generation satellites complete their **15-year lives**.
  `[📄 GSAT 10-Q p.36](https://agentii.ai/v/GSAT/sec166/36)` The fleet completing its life is
  both a cost relief and a capacity cliff — and it is the same fleet whose replacement is a
  merger condition (§5).
- **Tariff and input-cost exposure, filed with an amount.** Cost of subscriber equipment sales
  rose **39%** in FY2025 "including $1.1M of tariffs". `[📄 GSAT 10-K p.35](https://agentii.ai/v/GSAT/sec128/35)`
- **Compensation cost that has now stopped.** SBC fell **$12.1M** in FY2025 (to $23.4M from
  $35.5M) and **$3.2M / $7.5M** in 2026, with the **PSU award fully recognised at the end of Q2
  2026**. `[📄 GSAT 10-K p.35](https://agentii.ai/v/GSAT/sec128/35)` `[📄 GSAT 10-Q p.36](https://agentii.ai/v/GSAT/sec166/36)`
  A cost tailwind that terminates is a risk to the *rate of change*, not to the level.
- **A thin equity cushion against a large asset base.** Total assets **$2,444,812 thousand**
  against stockholders' equity of **$292,613 thousand** — an equity ratio of **12.0%**.
  `[📄 GSAT 10-Q p.6](https://agentii.ai/v/GSAT/sec166/6)`
- **One reportable segment.** GSAT discloses **MSS as its only reportable segment**.
  `[📄 GSAT 10-Q p.28](https://agentii.ai/v/GSAT/sec166/28)` A single-segment filer offers no
  segment boundary inside which a launch-cost share could be isolated — which is itself a
  PIL-6 reachability fact (§6).

## 4. Mode — technology-disruption-risk-analysis

GSAT's technology-disruption exposure is not in the SDARS or IoT product lines; it is in **the
next constellation, which does not exist yet and whose spectrum is filed by a foreign
administration.**

- **The C-3 System is filed with the ITU by the Republic of France, not by the United States.**
  GSAT "acquired operational rights to the AST-NG-C-3 system filing made by the Republic of
  France with the ITU" and "applied to the French government for C-3 System authorizations."
  `[📄 GSAT 10-Q p.32](https://agentii.ai/v/GSAT/sec166/32)` This is the structural mirror of
  IRDM: where IRDM's orbital rights are filed by the United States on its behalf, **GSAT's
  next-generation rights are filed by France.** Two consequences — the filing administration is
  a sovereign counterparty GSAT does not control, and the same reachability problem that makes
  the ITU resolver `UNRESOLVABLE-FROM-PLATFORM` at IRDM applies here with a different sovereign.
- **US market access for C-3 is an open FCC proceeding.** In **February 2025** GSAT filed a
  petition for US market access for the C-3 System, and **"the FCC Space Bureau has accepted
  our petition for filing and published it for public comment."**
  `[📄 GSAT 10-Q p.32](https://agentii.ai/v/GSAT/sec166/32)` Accepted-for-filing is a procedural
  milestone and **not** a grant. The distinction matters because the merger's closing conditions
  depend on the authorisations (§5).
- **The disruption channel that is actually filed is price, not capability.** SPOT revenue fell
  **7% / 7%** on "competitive pressure" and Duplex fell **26% / 26%** on the discontinuation of
  manufacture. `[📄 GSAT 10-Q p.34](https://agentii.ai/v/GSAT/sec166/34)` GSAT's filed
  disruption is demand-side substitution in its legacy product lines, at a **$4.31 monthly IoT
  ARPU** — which is where the secular-trends artifact for this ticker takes the argument.
- **The capability cliff is dated and filed.** The second-generation constellation is completing
  **15-year lives** during 2026, which is why D&A is falling. A decline in depreciation that
  precedes the replacement constellation is a cost relief inside the current period, not an
  improvement in the business. `[📄 GSAT 10-Q p.36](https://agentii.ai/v/GSAT/sec166/36)`

## 5. Mode — regulatory-compliance-risk-assessment

GSAT's regulatory surface is narrower than IRDM's in number of proceedings and **wider in
deal-contingency**.

- **A $420 million termination fee** — larger than the entire stockholders' equity of the
  company ($292,613 thousand). `[📄 GSAT 10-Q p.43](https://agentii.ai/v/GSAT/sec166/43)`
  `[📄 GSAT 10-Q p.6](https://agentii.ai/v/GSAT/sec166/6)`
- **HSR has already cleared**: the waiting period **expired July 17, 2026**.
- **Stockholder approval is already satisfied** — by **Written Consent (Thermo)**, so the vote
  condition that remains open at IRDM is closed at GSAT.
- **What remains open is regulatory and operational, and it is specific**: the closing conditions
  include **HIBLEO-4 replacement satellite launch and operations milestones** and **receipt of
  governmental authorizations related to the C-3 System**.
- **The consideration is contingent on those milestones**: a downward adjustment of up to
  **$110 million, currently approximately $97 million**, if they are not met.
- **Consideration form**: a **$90/share cash-or-stock election**, with **proration if cash
  elections exceed 40%**.
- **Outside date April 13, 2027**, extendable to **October 13, 2027** and then **April 13,
  2028**. `[📄 GSAT 10-Q p.43](https://agentii.ai/v/GSAT/sec166/43)`

**The regulatory-compliance finding is the inversion of IRDM's.** At IRDM the regulator holds the
*licence being transferred*. At GSAT the regulator's grant is a *condition to a payment*: the
$97M adjustment is denominated in a C-3 authorisation that the FCC has accepted for filing and
not granted, before a French administration that GSAT has applied to but does not control.
**GSAT's regulatory risk is priced into the deal consideration rather than into the operating
business**, and that is a materially different P11 exposure from IRDM's.

## 6. Falsifier-reachability census

| Falsifier | Reachability at GSAT | Class | Why |
|---|---|---|---|
| **PIL-6 `independently_falsifiable`** — "a demonstrated fall in revenue per launch at least as large as the fall in cost per launch" | **NON-FORMABLE**, not PASS | n/a | GSAT does not launch and files no per-launch cost or revenue. **NON-FORMABLE ≠ PASS (F16).** |
| **PIL-6 `wrong_if`** — launch-cost share of programme cost > 0.10 | **NON-FORMABLE**, not PASS | `REACHABLE-BUT-NOT-RECORDABLE` | GSAT is a **single-reportable-segment** filer (`[📄 GSAT 10-Q p.28](https://agentii.ai/v/GSAT/sec166/28)`), so there is no segment boundary inside which a programme cost could be isolated even in principle. The datum is reachable (capex is filed); the contract admits no field for it. |
| **F17 threshold reachability** | **NOT REACHABLE — not addressable at this issuer** | n/a | F17 is an SPCX segment-boundary property. Recorded so the census does not over-read F17 as universe-wide. |
| **A1a reconciliation statement** (`12.3%` / `8.29%`) | **UNEXERCISED** | n/a | Requires SPCX segment data; not reachable from GSAT's filings. |
| **F2 — Falcon 9 basis B** | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | inherited | 002 §5.1; not re-derived. |
| **F3 — propellant price** | **`REACHABLE-BUT-NOT-RECORDABLE`** | canonical case | The register's canonical instance. Remedy: amend the contract. |
| **GSAT merger C-3 authorisation docket** | `UNRESOLVABLE-FROM-PLATFORM` **+** `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | both, composed | GSAT names "governmental authorizations related to the C-3 System" and no docket or file number. The *specific* instrument is undisclosed by the filer; the *resolver* is unreachable. |
| **ITU Space Network List** (the AST-NG-C-3 filing) | `UNRESOLVABLE-FROM-PLATFORM` | platform reach | And the recorded network is keyed to **France**, not to GSAT — the issuer-keyed lookup fails for a reason the platform cannot fix. |
| **VZ / T / TMUS** | **`TICKER_NOT_FOUND`** — confirmed 2026-09-19 | n/a | All three verified this session. **The telecom comparator leg is absent by construction.** |
| **GSAT sector classification** | **inherited, currently CLAIMED** | n/a | The task carries that GSAT files under **`tech.tech_hardware`, NOT `tech.telecom_services`**, so a node-derived peer set silently omits this leg. Recorded as carried; **not independently verified in this session** — stated as inherited rather than promoted to DEMONSTRATED. |

## 7. What this artifact could not resolve

- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — the C-3 authorisation instrument.** The resolving
  disclosure is the **FCC file number for the February 2025 C-3 market-access petition** and the
  **French authorisation** GSAT applied for. GSAT describes both and names neither. This is the
  document that would convert the $97M consideration adjustment from a contingency into a
  dateable event.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — the HIBLEO-4 replacement satellite milestone dates.**
  The merger's closing conditions reference "launch and operations milestones" without a date or
  a satellite count in the Q2 2026 10-Q.
- **`UNRESOLVABLE-FROM-PLATFORM` — both PIL-6 resolvers.** FCC IBFS and the ITU Space Network
  List. Stated per the brief.
- **PMI: `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — the "93%" numerator.** No filed quantity at GSAT
  reproduces 93% as a non-operating share of net income. The resolving disclosure is a
  definition of the metric, which does not exist; the five reproducible bases are in §2.5.
- **UNEXERCISED — the gross-profit bound.** GSAT files no gross-profit line.
- **UNEXERCISED — DA-24 at the platform layer.** The substance is handled (the other-income block
  is reported separately as filed, and §2.5 reports its share rather than assuming it). The
  *platform-layer* test — whether `OperatingIncomeLoss` at GSAT carries a non-operating
  component — was not run. The served value matches the filed value exactly in every period
  checked, so the service is *consistent*; consistency is not a test having run.
- **NOT ATTEMPTED — DA-26, DA-27, DA-28, DA-29.** No annual figure is used as quarterly (DA-26);
  no calendar-derived fiscal label is relied on (DA-27 — GSAT is a December year-end filer);
  no share-count detector crosses the **1:15 reverse split effectuated February 10, 2025**
  (DA-28) — the split is named here as the reason a share-count test would be disqualified, and
  no such test is asserted; no reconciliation is claimed whose terms are absent from the source
  (DA-29). **Each recorded as not attempted. Not attempted is not CLEAN.**

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| GSAT sec166 p.5 | [📄 GSAT  p.5](https://agentii.ai/v/GSAT/sec166/5) |
| GSAT sec128 p.48 | [📄 GSAT  p.48](https://agentii.ai/v/GSAT/sec128/48) |
| GSAT sec166 p.37 | [📄 GSAT  p.37](https://agentii.ai/v/GSAT/sec166/37) |
| GSAT sec166 p.36 | [📄 GSAT  p.36](https://agentii.ai/v/GSAT/sec166/36) |
| GSAT sec166 p.33 | [📄 GSAT  p.33](https://agentii.ai/v/GSAT/sec166/33) |
| GSAT sec166 p.6 | [📄 GSAT  p.6](https://agentii.ai/v/GSAT/sec166/6) |
| GSAT sec166 p.42 | [📄 GSAT  p.42](https://agentii.ai/v/GSAT/sec166/42) |
| GSAT sec166 p.15 | [📄 GSAT  p.15](https://agentii.ai/v/GSAT/sec166/15) |
| GSAT sec128 p.35 | [📄 GSAT  p.35](https://agentii.ai/v/GSAT/sec128/35) |
| GSAT sec166 p.28 | [📄 GSAT  p.28](https://agentii.ai/v/GSAT/sec166/28) |
| GSAT sec166 p.32 | [📄 GSAT  p.32](https://agentii.ai/v/GSAT/sec166/32) |
| GSAT sec166 p.34 | [📄 GSAT  p.34](https://agentii.ai/v/GSAT/sec166/34) |
| GSAT sec166 p.43 | [📄 GSAT  p.43](https://agentii.ai/v/GSAT/sec166/43) |
| GSAT sec166 p.40 | [📄 GSAT  p.40](https://agentii.ai/v/GSAT/sec166/40) **(newly surfaced)** |
