---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-5
ticker: SPCX
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
    chosen_reading: "|x| absolute-value stripping, not inversion: served = |filed|, magnitude preserved, sign discarded. Confined to the XBRL facts layer — the earnings-calendar layer for the same period carries the filed sign."
  - da_id: DA-26
    chosen_reading: "annual figures mislabelled as quarterly. At SPCX the screen CANNOT RUN: no annual row exists in the corpus and none can exist in public sources before FY2026 closes. Recorded UNRESOLVED (UNEXERCISED) — not CLEAN."
  - da_id: DA-27
    chosen_reading: "fiscal-period labels derived from the calendar quarter. SPCX's fiscal calendar is derived from a NULL year-end field and its cross-validation hint is false; the resulting label is nonetheless correct. Class UNEXERCISED — a 31-Dec filer has no label to get wrong."
  - da_id: DA-30
    chosen_reading: "two bases on one concept collapsed without a basis field. EPS at SPCX Q2 2026 carries three concurrent bases — filed (0.09), platform-served +0.09, earnings-calendar -0.09. All three are reported; none is quoted alone."
evidence_grade: DEMONSTRATED
key_metrics:
  revenue_q2_2026_3m_musd: 7814
  operating_income_q2_2026_3m_musd: -143
  net_income_q2_2026_3m_musd: -541
  gross_margin_q2_2026_3m_pct: 55.27
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "SPCX sec8 p.5"
    ticker: SPCX
    citation_id: sec8
    page_no: 5
    url: https://agentii.ai/v/SPCX/sec8/5
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
---

# SPCX — recent quarter: the sign test fires 4 of 4, and the annual-row test cannot run at all

**All monetary quantities in this artifact are US$ millions unless labelled otherwise.**
Source: SPCX Form 10-Q for the quarterly period ended 2026-06-30, accession
`0001628280-26-052535`, filed 2026-08-04, 55 pages, `citation_id: sec8`.

## 1. The finding

**Two results, one positive and one negative, and the negative is the more important one.**

1. **DA-23 has FIRED at SPCX on every sign-bearing line and every served period — 4 of 4.**
   The served `OperatingIncomeLoss` for Q2 2026 is `+143,000,000`; the filed figure is
   **$(143) million** [📄 SPCX 10-Q p.5](https://agentii.ai/v/SPCX/sec8/5). Fourteen of fourteen
   quoted sign-bearing facts across four periods are served as the **absolute value** of the
   filed number. **The component identity closes exactly to the filed sub-line in all four
   periods** on the exclusive opex definition, which is the only reason we can state the
   served magnitudes are correct rather than merely present.

2. **DA-26 is `UNRESOLVED`, not `CLEAN`, and its disposition class is
   `UNRESOLVABLE-FROM-PUBLIC-SOURCES`.** The screen — reconcile quarter rows against a known
   annual total — requires an annual row. SPCX has none, and cannot have one: a query of the
   corpus for SPCX Form 10-K returns **zero rows**, and the filing in hand presents only
   three-month and six-month columns. **An unengaged check is not a passed check.**

**SPCX is also a SECOND SITE of the inclusive-opex failure**, after UTHR. Because SPCX files a
literal `Total costs and expenses` line, the `us-gaap:CostsAndExpenses` reading of the identity
is refuted here **directly on a filed line**, and it is wrong by **exactly cost of revenue** in
all four periods. The offset is measured, not asserted.

**There is no SPCX quarterly series in this corpus.** There are two disclosed windows (three
months and six months) inside one 10-Q. Every pillar that wants a trend at SPCX must first
acknowledge that the trend is unavailable — the constraint is in §3.1 and it is the single most
consequential line in this artifact.

---

## 2. Mode `consolidated-p-and-l` — the DA-23 sign test

### 2.1 Filed cells (verbatim from the statement)

`[📄 SPCX 10-Q p.5](https://agentii.ai/v/SPCX/sec8/5)` — Consolidated Statements of Operations,
unaudited, in millions except per share data.

| Line (US$ millions) | 3M to 2026-06-30 | 3M to 2025-06-30 | 6M to 2026-06-30 | 6M to 2025-06-30 |
|---|---:|---:|---:|---:|
| Revenue | 7,814 | 4,071 | 12,508 | 8,138 |
| Cost of revenue | 3,495 | 2,282 | 5,883 | 4,244 |
| Research and development | 3,548 | 1,958 | 7,062 | 3,515 |
| Selling, general, and administrative | 912 | 606 | 1,658 | 1,099 |
| Restructuring charges (credits) | 2 | 190 | (9) | 194 |
| Impairment | — | 5 | — | 29 |
| **Total costs and expenses** | **7,957** | **5,041** | **14,594** | **9,081** |
| **Loss from operations** | **(143)** | **(970)** | **(2,086)** | **(943)** |
| Net loss | (541) | (1,008) | (4,817) | (1,536) |
| Net loss attributable to shareholders — basic and diluted | (541) | (1,008) | (5,488) | (1,536) |
| Basic and diluted loss per share | $(0.09) | $(0.34) | $(1.12) | $(0.53) |
| Weighted average shares (millions) | 5,864 | 2,929 | 4,879 | 2,902 |

Grade for every cell above: **DEMONSTRATED** (filed figure, read from the statement page).

Note the shape of the equity line: at 6M 2026 net loss is $(4,817)M but net loss **attributable
to shareholders** is $(5,488)M — a $671M gap that does **not** exist in the 3M column (541 =
541) nor in either 2025 column. A per-share figure built from the 6M net-loss line rather than
the attributable line would be wrong by $0.14/share at 6M 2026 on the filed 4,879M share count.
**The applicable line is the attributable line**, and it is the one the filed $1.12 is built on.

### 2.2 The component identity, with the opex definition stated

**Opex definition used: EXCLUSIVE — `Research and development + Selling, general, and
administrative + Restructuring charges (credits) + Impairment`.** Cost of revenue is treated as
a cost of sales line and is **excluded** from opex. This is the definition the filer's own
sub-total structure implies: the `Costs and expenses` caption heads all five lines, but only
four of them sit outside cost of revenue.

| Period | Gross profit = Revenue − Cost of revenue | Opex (exclusive) | GP − Opex | Filed loss from operations | Verdict |
|---|---:|---:|---:|---:|:--|
| 3M 2026 | 7,814 − 3,495 = **4,319** | 3,548 + 912 + 2 + 0 = **4,462** | **(143)** | **(143)** | **exact** |
| 3M 2025 | 4,071 − 2,282 = **1,789** | 1,958 + 606 + 190 + 5 = **2,759** | **(970)** | **(970)** | **exact** |
| 6M 2026 | 12,508 − 5,883 = **6,625** | 7,062 + 1,658 + (−9) + 0 = **8,711** | **(2,086)** | **(2,086)** | **exact** |
| 6M 2025 | 8,138 − 4,244 = **3,894** | 3,515 + 1,099 + 194 + 29 = **4,837** | **(943)** | **(943)** | **exact** |

4 of 4 exact, to the filed thousand of the reported unit. Grade: **DEMONSTRATED** (arithmetic
directly on filed cells).

**The identity is used here to establish that the served magnitudes are right, not to discover
the sign.** It cannot do the latter: gross profit and opex are both unsigned, so the identity
returns a *signed* result from *unsigned* inputs and the sign it returns is the filer's. That is
precisely why it is the only admissible DA-23 detector and why `EPS × shares` is not — `EPS ×
shares` round-trips the stripped sign into both terms and cancels it.

### 2.3 The inclusive-definition failure, measured against a filed line

`us-gaap:CostsAndExpenses` **includes** cost of sales, so on that reading the identity is false
wherever a cost-of-sales line exists. At SPCX the inclusive total is not inferred — it is a
**filed line**, `Total costs and expenses`:

| Period | GP − inclusive total | Filed loss from operations | Discrepancy | = cost of revenue? |
|---|---:|---:|---:|---|
| 3M 2026 | 4,319 − 7,957 = (3,638) | (143) | **3,495** | ✓ exactly |
| 3M 2025 | 1,789 − 5,041 = (3,252) | (970) | **2,282** | ✓ exactly |
| 6M 2026 | 6,625 − 14,594 = (7,969) | (2,086) | **5,883** | ✓ exactly |
| 6M 2025 | 3,894 − 9,081 = (5,187) | (943) | **4,244** | ✓ exactly |

**The offset equals the cost-of-revenue line to the unit in all four periods.** This is a
*measured* structural offset, not a residual. Consequences:

- Any artifact that reports SPCX operating income as `gross profit − Total costs and expenses`
  is wrong by **44.7% of revenue** at 3M 2026 (3,495/7,814), 56.1% at 3M 2025, 47.0% at 6M
  2026 and 52.2% at 6M 2025. Grade: **DEMONSTRATED**.
- SPCX therefore joins **UTHR** as a site where the inclusive reading is not merely risky but
  **refuted on a filed line**. The register's example (UTHR, 6 of 6) is not idiosyncratic; it is
  the general case for any issuer that files a cost-of-sales line **and** an inclusive caption.
- **The correct reading is not a matter of preference at SPCX.** `Total costs and expenses`
  (7,957) exceeds the sum of its own non-cost-of-revenue components (4,462) by exactly the cost
  of revenue; the inclusive caption is a *superset* caption, and pricing operating income off it
  double-counts cost of sales.

### 2.4 Served vs filed — the sign-test verdict

| Concept | Period | Filed | Platform-served | Relation | Verdict |
|---|---|---:|---:|---|:--|
| `OperatingIncomeLoss` | 3M 2026 | (143) | +143,000,000 | served = \|filed\| | **FIRED** |
| `OperatingIncomeLoss` | 3M 2025 | (970) | +970,000,000 | served = \|filed\| | **FIRED** |
| `OperatingIncomeLoss` | 6M 2026 | (2,086) | +2,086,000,000 | served = \|filed\| | **FIRED** |
| `OperatingIncomeLoss` | 6M 2025 | (943) | +943,000,000 | served = \|filed\| | **FIRED** |
| `NetIncomeLoss` | 3M 2026 | (541) | +541,000,000 | served = \|filed\| | **FIRED** |
| `NetIncomeLoss` | 3M 2025 | (1,008) | +1,008,000,000 | served = \|filed\| | **FIRED** |
| `NetIncomeLoss` | 6M 2026 | (4,817) | +4,817,000,000 | served = \|filed\| | **FIRED** |
| `NetIncomeLoss` | 6M 2025 | (1,536) | +1,536,000,000 | served = \|filed\| | **FIRED** |
| `NetIncomeLossAvailableToCommonStockholdersDiluted` | 3M 2026 | (541) | +541,000,000 | served = \|filed\| | **FIRED** |
| `NetIncomeLossAvailableToCommonStockholdersDiluted` | 6M 2026 | (5,488) | +5,488,000,000 | served = \|filed\| | **FIRED** |
| `EarningsPerShareDiluted` / `Basic` | 3M 2026 | (0.09) | +0.09 | served = \|filed\| | **FIRED** |
| `EarningsPerShareBasic`/`Diluted` | 3M 2025 | (0.34) | +0.34 | served = \|filed\| | **FIRED** |
| `EarningsPerShareBasic`/`Diluted` | 6M 2026 | (1.12) | +1.12 | served = \|filed\| | **FIRED** |
| `EarningsPerShareBasic`/`Diluted` | 6M 2025 | (0.53) | +0.53 | served = \|filed\| | **FIRED** |

Grade for the "Filed" column: **DEMONSTRATED** (p.5, above). Grade for the "served" column:
**DEMONSTRATED** (platform fact, `source_file: spcx-20260630.htm`, `source_authority: 2`).

**Verdict: DA-23 FIRED. 14 of 14 quoted sign-bearing facts, 4 of 4 periods, 4 of 4 concepts.**

**The served series is complete and small.** `OperatingIncomeLoss` returns exactly **4 facts in
the entire served series for SPCX** — the four above and nothing else. There is no SPCX
operating series with a sign anywhere in the corpus. The whole of it is the absolute value of
the whole of the filed series.

**Relation is `|x|`, not `-x`.** Every served value is positive; the filed partner is negative;
the magnitudes agree to the unit. Nothing in this set is an inversion, and nothing is a
coincidence of two negatives. **A detector tuned to "sign is wrong" would also fire on a genuine
inversion; a detector tuned to `served == |filed|` distinguishes them, and that is the detector
used here.**

### 2.5 The DA-30 obligation — three bases on one concept, all reported

At 3M 2026 the same metric, `EPS diluted`, is asserted on three bases simultaneously:

| Basis | Value | Source |
|---|---:|---|
| Filed, as reported | **$(0.09)** | [📄 SPCX 10-Q p.5](https://agentii.ai/v/SPCX/sec8/5) |
| Platform XBRL fact | **+0.09** | served fact, `spcx-20260630.htm` |
| Platform earnings calendar | **-0.09** | earnings calendar row `2026 (Q2)`, `fiscal_source: ect_exact` |

**The third basis agrees with the filing and contradicts the platform's own facts layer.**
That is the load-bearing observation of this file: **DA-23 is a property of one layer, not of the
data.** The same platform, the same quarter, the same metric: `+0.09` from the facts layer and
`-0.09` from the calendar layer. **Neither layer can be used to repair the other, and a reader
who takes whichever layer is convenient will take a different answer in each section of the same
artifact.** Per the standing rule, all three bases are reported and none is quoted alone.

---

## 3. Mode `margin-analysis` — the DA-26 / DA-27 period traps

### 3.1 DA-26 — `UNRESOLVED` (UNEXERCISED), because no annual row exists

**The screen and how it is supposed to run.** DA-26 is tested by **reconciling a row against a
known annual total**, and by **comparing a row's duration, not its position in the sequence**.
The duration test requires a 12-month fact; the reconciliation test requires an annual total.
Both require an annual row.

**What the corpus holds for SPCX:**

| Query | Result |
|---|---|
| `search_sec_filings(SPCX, form_type="10-K")` | **0 rows** |
| `get_ticker_coverage(SPCX)` → `sec_filings` | 8 filings, latest 2026-08-04 |
| 10-Q statement of operations columns | three months and six months — **no annual column** |
| `OperatingIncomeLoss` facts in the entire served series | **4** — 3M 2026, 6M 2026, 3M 2025, 6M 2025 |

**Verdict: `UNRESOLVED` — specifically `UNEXERCISED`. NOT `CLEAN`.** The disposition class is
**`UNRESOLVABLE-FROM-PUBLIC-SOURCES`**, and here the class is structural rather than incidental:
SPCX reports on a 31 December year and, as of `as_of` 2026-09-19, **FY2026 has not closed**.
No SPCX annual report can exist yet. The disclosure that would resolve this is **SPCX's first
Form 10-K (FY2026)**, filed 2027, which will carry FY2025-comparative annual columns. Until
then the absence of an annual row is a fact about the calendar, not about the issuer and not
about the platform.

**What this costs the thesis, stated plainly.** Because the 10-Q discloses only 3M and 6M
windows, SPCX's "quarterly series" in this corpus is **two overlapping windows from a single
filing**, not a time series. From those two windows the implied Q1 2026 revenue is
12,508 − 7,814 = **$4,694M** (grade: **DERIVED** — a subtraction, not a filed figure), and
***nothing else about Q1 2026 exists in this corpus***. Therefore:

- **No SPCX quarter-over-quarter, seasonality, or trend claim is admissible from this corpus.**
- Any SPCX series presented elsewhere in thesis 003 with more than two points is either
  (a) built from the earnings-calendar layer's single row, or (b) not sourced from this corpus.
  Both cases must be labelled as such. **PIL-5's cost-curve work, PIL-4's Neutron arithmetic and
  PIL-6's pass-through test all inherit this limit at SPCX.**
- The segment tables carry the same two windows. `[📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30)`
  and `[📄 SPCX 10-Q p.31](https://agentii.ai/v/SPCX/sec8/31)` present the segment split on the
  same 3M/6M basis, so **the Space segment's margin series has no quarterly resolution either** —
  and the segment boundary is the CUSTOMER boundary (DA-21), not the launch boundary, with
  roughly 74% of launches producing no Space revenue by design and customer 10 of 38 = 26.3% of
  Q2 2026 launches. **A segment margin and a launch count are not two views of one thing at
  SPCX; they are two views of two different boundaries.**

### 3.2 DA-27 — `UNEXERCISED`; and the metadata that would screen it is demonstrably false

**The screen and how it is supposed to run.** DA-27 is fiscal-period labels derived from the
calendar quarter. It is screened by **comparing a row's duration, not its position**, and by
reconciling against known totals — never by trusting the label or the date field.

**What the platform's fiscal calendar returns for SPCX:**

| Field | Value |
|---|---|
| `company.fiscal_year_end_month` | **`null`** |
| `fiscal_year_end_month_source` | **`"default"`** |
| `cross_validation_hint` | **"No XBRL data available for this ticker — fiscal calendar may be inaccurate. Confirm fiscal year-end manually before relying on computed quarter ranges."** |
| quarters returned | FY2025 Q1–Q4, FY2026 Q1–Q4, **FY2027 Q1–Q4** (through 2027-12-31) |

**The hint is false, and its falsity is numerically verifiable.** The corpus holds **1,517 XBRL
facts for SPCX** (`get_ticker_coverage`, `xbrl_facts`), and `spcx-20260630.htm` alone supplies
the complete statement of operations quoted in §2 — revenue, gross profit, opex, operating loss,
net loss and EPS for four windows. **A cross-validation hint that reports "no XBRL data" over
1,517 facts is measuring its own derivation path, not the data.**

**The label is nonetheless correct.** The filed statement covers three and six months ended
June 30; a 31 December year-end follows. The platform derived the right label from a null field.

**Verdict: DA-27 `UNEXERCISED` at SPCX — not `CLEAR`.** The class requires a non-calendar
issuer; a 31 December filer has no fiscal label that can differ from its calendar label. **A
31-Dec filer cannot exhibit DA-27, so its absence here carries no information about the
detector** — which is why this is recorded as PRESENCE-vs-ABSENCE and not as a pass.

**Two further observations from the same response, both carried forward:**

1. **The FY2027 rows are forward-synthesised, not mislabelled.** They lie in the future, carry
   no actuals, and are a different defect class from DA-26 (which puts a *real* annual figure in
   a *past* quarterly row). Do not conflate them.
2. **A metadata-keyed DA-27 detector cannot work, and this is the proof.** A detector keyed on
   `fiscal_year_end_month_source == "default"` **fires at SPCX — where the label is right** —
   and would clear at a correctly-populated non-calendar issuer only by accident. It measures
   the derivation path. **The only admissible screen is the duration comparison and the
   annual-total reconciliation**, and neither can run at SPCX (§3.1). **At SPCX, DA-27 is not
   merely unexercised; the platform's own metadata contradicts itself and must not be quoted as
   evidence of anything.**

### 3.3 The safe-set margins, rebuilt from filed cells

Per thesis 001's ratio audit, **gross margin is SAFE** (unsigned inputs) and **operating margin
is UNSAFE from the metrics block** (DA-23 strips the sign, so a loss reads as a profit).
Every figure below is rebuilt from the p.5 cells, not from any metrics block.

| Metric | 3M 2026 | 3M 2025 | 6M 2026 | 6M 2025 |
|---|---:|---:|---:|---:|
| Revenue (US$M) | 7,814 | 4,071 | 12,508 | 8,138 |
| Gross profit (US$M) | 4,319 | 1,789 | 6,625 | 3,894 |
| **Gross margin** | **55.27%** | **43.94%** | **52.97%** | **47.85%** |
| **Operating margin** (rebuilt, filed sign) | **−1.83%** | **−23.83%** | **−16.68%** | **−11.59%** |
| R&D / revenue | **45.41%** | **48.10%** | **56.46%** | **43.19%** |
| Revenue growth YoY | **+91.94%** | — | **+53.70%** | — |

All cells: **DEMONSTRATED** (arithmetic directly on filed p.5 cells).

**Three things this table is for:**

- **It reproduces thesis 001's peer-bench cells exactly** — 55.3% gross margin, −1.8% operating
  margin, 45.4% R&D/revenue, +91.9% growth — from an independent read of the same page. The
  safe set behaves as documented across a corpus vintage change.
- **The operating margin line is the DA-23 trap in one cell.** Read from the metrics block, SPCX's
  3M 2026 operating margin is **+1.83%**. The filed figure is **−1.83%**. **A screen that ranks
  this cohort on operating margin from the metrics block ranks SPCX, RKLB and FLY as profitable
  and then ranks them in an order determined by loss size.** The order is not random — which is
  the dangerous part. **The failure mode here is plausible-but-wrong, not null.**
- **Gross margin's 11.3-point YoY expansion at 3M is not a cost-curve result.** Cost of revenue
  rose 53.2% (2,282 → 3,495) while revenue rose 91.9%; the margin expansion is revenue mix and
  scale, and gross margin is computed from unsigned lines so it is safe. **But "safe" and
  "interpretable" are different claims** — PIL-1 and PIL-3 need a *cost* per launch, and this
  statement contains no launch count. The launch-count/cost join at SPCX is not available in
  this artifact and is not attempted here.

---

## 4. Mode `earnings-vs-consensus`

SPCX has **exactly one** earnings-calendar row in the corpus — the same single-row ceiling
recorded in §3.1, arriving from the other side.

| Field | Value | Reconciles to the filing? |
|---|---|---|
| `fiscal_quarter` | 2026 (Q2) | — |
| `report_date` | 2026-08-04 | = 10-Q filing date ✓ |
| `fiscal_source` | `ect_exact` | — |
| `eps_actual` | **−0.09** | ✓ **exact** to the filed $(0.09) |
| `eps_estimated` | −0.22547 | n/a |
| `eps_surprise` | +0.13547 (+70.18%) | — |
| `revenue_actual` | 7,814,000,000 | ✓ **exact** to filed $7,814M |
| `revenue_estimated` | 6,826,709,000 | n/a |
| `revenue_surprise` | +987,291,000 (**+14.46%**) | — |

Grade: **DEMONSTRATED** for the reconciliation; **CLAIMED** for the estimate and surprise
fields (third-party consensus, not a filed figure — and a `CLAIMED` input can never satisfy a
falsifier).

**Four results:**

1. **The consensus EPS is correctly signed and reconciles exactly to the filing.** The
   sign-stripping does not exist in this layer. Combined with §2.4, **DA-23 is localised to the
   XBRL facts layer** — that is a new, generalisable result from this artifact.
2. **The consensus revenue reconciles exactly too, and it must**: `Revenue` is unsigned, so
   DA-23 has no purchase on it. **DA-23 cannot corrupt a revenue series anywhere.** Any revenue
   series in this thesis is safe from it; every *signed* line is not.
3. **n = 1.** One row is a point, not a series. **No surprise history, no estimate-revision
   series, no beat/miss pattern, and no seasonality is admissible at SPCX.** A trend claim built
   on this row would be a MODELED artefact wearing a DEMONSTRATED label. Class:
   **`UNRESOLVABLE-FROM-PLATFORM`** — the underlying quarterly consensus data exists publicly;
   the corpus holds one row of it.
4. **The one row's surprise is +14.46% on revenue against a consensus of $6,826.7M.** Reported
   as a fact. It is not used here as evidence for any pillar: PIL-5's claim is about *cost-side
   measurement vs revenue-side normalisation* and PIL-2's is about *where the value pool sits*,
   and neither is testable from a single consensus row. **Recording the number is not the same
   as admitting it as evidence.**

---

## 5. What this artifact could not resolve

| # | Unresolved | Class | The disclosure that would resolve it |
|---|---|---|---|
| 1 | **DA-26 at SPCX** — no annual row exists to mislabel | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** | SPCX's first Form 10-K (FY2026), filed 2027; carries FY2025-comparative annual columns. Structural: cannot exist before FY2026 closes. |
| 2 | **DA-27 at SPCX** — class inapplicable to a 31-Dec filer | n/a (`UNEXERCISED`) | Nothing. A 31-Dec filer has no fiscal label that can differ from its calendar label. **Not a gap to close; a test that does not apply.** |
| 3 | **SPCX quarterly series** — 3M and 6M from one filing | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** (in this corpus) | Each subsequent 10-Q; the series builds one filing at a time. Q1 2026 exists in no filing and never will as a filed figure — it is only ever a subtraction. |
| 4 | **Consensus series at SPCX** — n = 1 | **`UNRESOLVABLE-FROM-PLATFORM`** | The corpus holding more earnings-calendar rows; the data exists publicly. |
| 5 | **Standalone Q4** — the Q4 hole | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** | No 31-Dec filer files a Q4 10-Q, so a standalone Q4 is never filed. It is derivable only as `FY − 9M`, and **at SPCX neither term exists yet.** A Q4 "row" at SPCX is a back-solve, and per **DA-29** a reconciliation that closes is not thereby a check. |
| 6 | **The fiscal-calendar metadata at SPCX** — `null` year-end, `default` source, false hint | **`UNRESOLVABLE-FROM-PLATFORM`** | Nothing. The field is wrong and the label it produced is right; the metadata is simply not evidence. **Do not quote it in either direction.** |

**The distinction that matters, stated as a rule for the rest of the thesis:** items 1, 3 and 5
are absent because the *world* has not produced them yet. Items 4 and 6 are absent or wrong
because the *platform* has not produced them. **The remedies differ, so the classes must.**

---

## 6. Carry-forwards

1. **DA-23 FIRED at SPCX: 14 of 14 quoted sign-bearing facts, 4 of 4 periods, 4 of 4 concepts.**
   The served series is `|filed|` and the component identity closes exactly — so the magnitudes
   are trustworthy and the signs are not. **Trust the magnitude, derive the sign.**
2. **DA-23 is a LAYER property, not a data property.** The facts layer serves +0.09 where the
   calendar layer serves −0.09 and the filing says $(0.09) for the same quarter. **Never repair
   one layer from the other, and never quote one basis alone (DA-30).** Three bases on EPS are
   reported because three exist.
3. **DA-26 is `UNRESOLVED`, not `CLEAN`, at SPCX.** Cite this artifact for that specific
   disposition. **Do not report SPCX as DA-26-negative anywhere in thesis 003.**
4. **SPCX has no quarterly series in this corpus.** Two overlapping windows from one filing.
   **Every SPCX trend claim in PIL-1 through PIL-6 inherits this limit** and must be labelled
   `MODELED` or `DERIVED` where it exceeds the two disclosed windows — and per P4, **a `MODELED`
   input can never satisfy a falsifier.**
5. **SPCX is the second measured site of the inclusive-opex failure** (after UTHR, 6 of 6). The
   offset is **exactly cost of revenue** in all four periods: 3,495 / 2,282 / 5,883 / 4,244.
   `Total costs and expenses` is a superset caption. **The component identity is the only
   admissible operating-income derivation at SPCX, and it must state the EXCLUSIVE definition.**
6. **`EPS × shares` remains inadmissible as a sign test** — and at SPCX the reason is visible:
   the share count itself steps 2,929M → 5,864M (2.00×) between the two 3M windows, so
   `EPS × shares` inherits a capital-structure discontinuity on top of the sign stripping.
7. **The fiscal-calendar metadata for SPCX is false and the label it produced is correct.** Both
   halves matter: the metadata is not evidence, and a correct label is not evidence that the
   mechanism is sound. **Screen by duration and by annual totals; never by metadata.**
8. **The stability rule applied here.** Every identification in this file is (a) exact — to the
   filed unit; (b) stable — across all four periods and all four concepts; and (c) consistent
   with a specified formula (the component identity on a stated opex definition) or with a filed
   basis (the p.5 cells). **Where any of the three fails, the answer is `UNRESOLVED`, not
   "probably fine."**
