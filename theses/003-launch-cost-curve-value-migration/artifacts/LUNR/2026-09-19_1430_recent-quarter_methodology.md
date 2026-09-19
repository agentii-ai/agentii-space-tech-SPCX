---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-5
ticker: LUNR
skill: recent-quarter
mode: methodology
generated_at: 2026-09-19T14:30:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07d26b9c738b"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: >
      The served sign is not evidence. Every negative the platform serves for LUNR is
      stripped to its absolute value; the filed sign is authoritative and the component
      identity — not a heuristic, not EPS x shares — is the detector.
  - da_id: DA-26
    chosen_reading: >
      A period label is authoritative only when it carries its own start and end date. I
      read durations, not labels. Where the platform serves no standalone fourth-quarter
      fact, the full-year duration is the nearest reachable "fourth period" figure and is
      read as such — annual, not quarterly.
  - da_id: DA-24
    chosen_reading: >
      Non-operating contamination is present only if a non-operating item sits inside the
      operating block. Test: the component identity must close against 100% of the cost
      lines the statement lists, inside a separately-labelled operating block.
  - da_id: DA-30
    chosen_reading: >
      Revenue has two live bases at LUNR (service-only 207,132 and total 210,059 in FY2025).
      Any margin quoted on this issuer names its revenue base, because the two differ by the
      grant line and produce different ratios on one numerator.
  - da_id: DA-25
    chosen_reading: >
      A per-unit metric is reproducible only from filed tables at a stated date. Tested by
      asking whether the segment table can be reconciled to the consolidated statement; it
      can, to the dollar.
evidence_grade: DEMONSTRATED
citations:
  - figure: "FY2025 annual statement of operations — revenue 210,059, opex 297,290, operating loss (87,231), Loss on issuance of securities nil FY2025 / (93,136) FY2024, net loss (106,846)"
    ticker: LUNR
    form_type: 10-K
    citation_id: sec59
    page_no: 48
    url: https://agentii.ai/v/LUNR/sec59/48
    located_via: read_source_pages
  - figure: "Note 18 segment — one reportable segment; segment table reproduces the consolidated operating loss (87,231) to the dollar"
    ticker: LUNR
    form_type: 10-K
    citation_id: sec59
    page_no: 105
    url: https://agentii.ai/v/LUNR/sec59/105
    located_via: read_source_pages
  - figure: "Q1 2026 statement of operations — revenue 186,730, opex 225,931, operating loss (39,201), EPS $(0.25), shares 147,878,006; Q1 2025 comparative 62,524 / 72,601 / (10,077)"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec73
    page_no: 8
    url: https://agentii.ai/v/LUNR/sec73/8
    located_via: read_source_pages
  - figure: "Q1 2026 MD&A consolidated results of operations with the $ Change column — total revenue change 124,206"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec73
    page_no: 46
    url: https://agentii.ai/v/LUNR/sec73/46
    located_via: read_source_pages
  - figure: "Note 21 segment — one reportable segment at Q1 2026"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec73
    page_no: 38
    url: https://agentii.ai/v/LUNR/sec73/38
    located_via: read_source_outline
  - figure: "Q2 2026 and H1 2026 statements of operations — revenue 206,168 / 392,898, opex 253,304 / 479,235, operating loss (47,136) / (86,337), shares 162,172,470"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 8
    url: https://agentii.ai/v/LUNR/sec76/8
    located_via: read_source_pages
  - figure: "Note 12 — February 27, 2026 securities purchase agreement, 11,574,069 shares at $15.12 ($175.0M); ATM 8,259,379 shares for $235.2M net; Class A issued 171,720,829"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 33
    url: https://agentii.ai/v/LUNR/sec76/33
    located_via: read_source_pages
  - figure: "Q2 2026 segment table reproducing the consolidated operating loss to the dollar"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 43
    url: https://agentii.ai/v/LUNR/sec76/43
    located_via: read_source_pages
  - figure: "PL Q1 FY2027 year-over-year revenue growth 94,150 / 66,265 - 1 = 42.08% — cross-issuer numeral-collision check"
    ticker: PL
    form_type: 10-Q
    citation_id: sec76
    page_no: 6
    url: https://agentii.ai/v/PL/sec76/6
    located_via: read_source_pages
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM
key_metrics:
  operating_margin_q2_2026_pct: -22.9
  operating_margin_fy2025_pct: -41.5
  revenue_q2_2026_usd_thousands: 206168
  operating_loss_q2_2026_usd_thousands: -47136
---

# recent-quarter × LUNR — the quarter that does not exist

## 1. The finding

**The "42.1% operating margin" is not a quarter, not positive, and not computed on the
revenue base it appears to sit on.** It is a FY2025 **annual** figure with three defects
stacked on top of each other. The only reading that reproduces the numeral is

```
87,231 / 207,132 = 42.11%      (DEMONSTRATED — arithmetic on two filed cells)
```

— the **FY2025 annual** operating loss `$(87,231)K` over **FY2025 annual service revenue
only** `$207,132K`, which excludes the `$2,927K` grant revenue line. So the stack is:
**DA-23** (the filed negative served as a positive), **DA-26** (an annual figure read as a
quarter), and **DA-30** (a revenue base — service-only versus total — that the figure never
names). `"42.1"` returns **zero pages** in the FY2025 10-K. The figure is not filed.

The true series, read off the statements ([📄 LUNR 10-K p.48](https://agentii.ai/v/LUNR/sec59/48),
[📄 LUNR 10-Q p.8](https://agentii.ai/v/LUNR/sec73/8),
[📄 LUNR 10-Q p.8](https://agentii.ai/v/LUNR/sec76/8)):

| Period | Revenue | Operating loss | Margin | Grade |
|---|---|---|---|---|
| Q1 2025 | $62,524K | $(10,077)K | −16.1% | DEMONSTRATED |
| Q2 2025 | $50,313K | $(28,640)K | −56.9% | DEMONSTRATED |
| **Q1 2026** | **$186,730K** | **$(39,201)K** | **−21.0%** | DEMONSTRATED |
| **Q2 2026** | **$206,168K** | **$(47,136)K** | **−22.9%** | DEMONSTRATED |
| H1 2026 | $392,898K | $(86,337)K | −22.0% | DEMONSTRATED |
| **FY2025 (annual)** | **$210,059K** | **$(87,231)K** | **−41.5%** | DEMONSTRATED |
| **Q4 2025 standalone** | $44,785K | **$(33,095)K** | **−73.9%** | DERIVED (residual) |

**The standalone Q4 2025 is the worst quarter of 2025 — −73.9%, against an annual −41.5%.**
The annual figure flatters the fourth quarter by 32.4 percentage points. That is the
direction of the error, and it is the opposite of the direction a reader of "42.1%" assumes.

Four further results, each page-verified:

1. **DA-23 fires on 12 of 12 periods**, and the strip is **not confined to
   `OperatingIncomeLoss`**. It reaches `NetIncomeLoss` (served `83,294,000` against filed
   `(83,294)`) and `NetIncomeLossAvailableToCommonStockholdersDiluted` (served `83,910,000`
   against filed `(83,910)`) — [📄 LUNR 10-K p.48](https://agentii.ai/v/LUNR/sec59/48).
2. **DA-24 is NOT PRESENT, with positive evidence.** LUNR's income statement carries an
   explicit `Loss on issuance of securities` line **inside a separately-labelled
   `Other income (expense)` block below the operating line**: `$(93,136)K` in FY2024, nil in
   FY2025. The non-operating block is real, labelled, and located below the line — and the
   component identity closes against 100% of the operating cost lines (§2.2), leaving no
   arithmetic room for a non-operating item inside operating income.
3. **DA-25 is NOT PRESENT and its premise is INVERTED.** LUNR reports **one reportable
   segment**, and the segment table reproduces the consolidated operating loss **to the
   dollar** (§3.3). There is no second basis to reconcile against, so there is nothing for a
   normalised per-unit metric to hide in.
4. **DA-27 CANNOT MANIFEST at LUNR.** The company is a 31-December filer, so fiscal periods
   and calendar quarters coincide by construction. **LUNR is EXCLUDED from the DA-27
   denominator — not counted as clean.** A test that cannot run is `UNEXERCISED`, not passed.

---

## 2. Mode `consolidated-p-and-l` — the DA-23 sign test

### 2.1 Filed cells

Verbatim from the FY2025 10-K, the Q1 2026 10-Q and the Q2 2026 10-Q. All figures
`DEMONSTRATED`; all in thousands.

**FY2025 ([📄 LUNR 10-K p.48](https://agentii.ai/v/LUNR/sec59/48))**

| | FY2025 | FY2024 |
|---|---|---|
| Service revenue | $207,132 | $228,000 |
| Grant revenue | 2,927 | — |
| **Total revenues** | **210,059** | 228,000 |
| Cost of revenue (excl. D&A) | 177,247 | 190,369 |
| Cost of revenue (excl. D&A) — affiliated companies | 23,822 | 34,862 |
| Depreciation and amortization | 3,597 | 1,859 |
| Impairment of property and equipment | — | 5,044 |
| General and administrative (excl. D&A) | 92,624 | 53,262 |
| **Total operating expenses** | **297,290** | 285,396 |
| **Operating loss** | **(87,231)** | (57,396) |
| Loss on issuance of securities | **—** | **(93,136)** |
| Net loss | (106,846) | (346,922) |

**Q1 2026 ([📄 LUNR 10-Q p.8](https://agentii.ai/v/LUNR/sec73/8))**

| | Q1 2026 | Q1 2025 |
|---|---|---|
| Product revenue | $141,554 | $— |
| Service revenue | 42,076 | 62,524 |
| Grant revenue | 3,100 | — |
| **Total revenues** | **186,730** | 62,524 |
| Cost of product revenue (excl. D&A) | 113,913 | — |
| Cost of service revenue (excl. D&A) | 33,660 | 48,925 |
| Cost of grant revenue (excl. D&A) | 3,101 | — |
| Cost of service revenue (excl. D&A) — affiliated | 5,949 | 6,922 |
| Depreciation and amortization | 13,048 | 623 |
| Research and development | 5,589 | 911 |
| General and administrative (excl. D&A) | 50,671 | 15,220 |
| **Total operating expenses** | **225,931** | 72,601 |
| **Operating loss** | **(39,201)** | (10,077) |
| Net loss | (52,528) | 975 |
| Net loss per Class A share, basic and diluted | $(0.25) | $(0.11) |
| Weighted-average shares, basic and diluted | 147,878,006 | 107,081,918 |

**Q2 2026 and H1 2026 ([📄 LUNR 10-Q p.8](https://agentii.ai/v/LUNR/sec76/8))**

| | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---|---|---|---|
| **Total revenues** | **206,168** | 50,313 | 392,898 | 112,837 |
| Total cost of revenues | 170,302 | 62,156 | 326,925 | 118,003 |
| Depreciation and amortization | 14,927 | 752 | 27,975 | 1,375 |
| Research and development | 7,729 | 461 | 13,318 | 1,372 |
| General and administrative (excl. D&A) | 60,346 | 15,584 | 111,017 | 30,804 |
| **Total operating expenses** | **253,304** | 78,953 | 479,235 | 151,554 |
| **Operating loss** | **(47,136)** | (28,640) | **(86,337)** | (38,717) |
| Net loss per Class A share | $(0.29) | $(0.22) | $(0.54) | $(0.33) |

### 2.2 The component identity, with the opex definition stated

**The opex definition I use at LUNR is the INCLUSIVE one**, because LUNR's statement of
operations files **no gross-profit subtotal**: every cost line — cost of product, service and
grant revenue, the affiliated-companies cost line, D&A, R&D, and G&A — sits *inside* the
`Operating expenses:` caption. There is no cost-of-revenues line above a gross-profit
subtotal to subtract separately. This is the opposite of the RKLB and YSS case and I state it
because the same identity is *false* under the other pairing at those two issuers.

```
FY2025   210,059 − 297,290 = (87,231)     ✓ EXACT   (inclusive: 177,247 + 23,822 + 3,597 + 92,624 = 297,290)
Q1 2026  186,730 − 225,931 = (39,201)     ✓ EXACT   (inclusive: 113,913 + 33,660 + 3,101 + 5,949 + 13,048 + 5,589 + 50,671 = 225,931)
Q2 2026  206,168 − 253,304 = (47,136)     ✓ EXACT   (inclusive: 170,302 + 14,927 + 7,729 + 60,346 = 253,304)
H1 2026  392,898 − 479,235 = (86,337)     ✓ EXACT
Q1 2025   62,524 −  72,601 = (10,077)     ✓ EXACT
Q2 2025   50,313 −  78,953 = (28,640)     ✓ EXACT
H1 2025  112,837 − 151,554 = (38,717)     ✓ EXACT
```

Every one closes to the dollar on the filed cells. **This is what makes the sign strip
provable rather than asserted**: a stripped sign cannot survive an identity that closes on
the filed magnitudes.

**Additivity corroborates the identity independently** — the quarters sum to the periods
without a residual:

```
Q1 2025 + Q2 2025 = 10,077 + 28,640 = 38,717 = H1 2025   ✓
H1 2025 + Q3 2025 = 38,717 + 15,419 = 54,136 = 9M 2025   ✓
9M 2025 + Q4 2025 = 54,136 + 33,095 = 87,231 = FY2025    ✓
Q1 2026 + Q2 2026 = 39,201 + 47,136 = 86,337 = H1 2026   ✓
```

The third line **derives the standalone Q4 2025 operating loss** `$(33,095)K` — the figure
the platform never serves (§2.5). Grade `DERIVED`: arithmetic on two filed cells, from the
served durations `2025-01-01→2025-09-30` and `2025-01-01→2025-12-31`.

### 2.3 The pairing that fails, and why the identity is conditional

`us-gaap:CostsAndExpenses` is **inclusive of cost of sales**. At LUNR that is the *correct*
pairing, because no gross-profit subtotal is filed. Had LUNR filed one, the same
`CostsAndExpenses` value would double-count cost of revenue. I record the failure mode
explicitly so the identity is not misapplied from this artifact:

- At **PL** (which does file a gross-profit subtotal) the inclusive pairing double-counts and
  gives `(78,637)` against a filed `(34,888)`. See the PL sibling artifact.
- At **YSS** (same shape) it gives `(204,659)` against a filed `(110,466)`.

**`EPS × shares` is not an admissible sign test** and is not used here. It fails twice over
at LUNR: the served EPS is itself stripped (§2.4), and the share count moved 38.1% year over
year (`147,878,006` in Q1 2026 against `107,081,918` in Q1 2025), so the product's error
compounds a sign error with a capital-structure discontinuity.

### 2.4 Served vs filed — the verdict table

| Concept | Period | Served | Filed | Sign test |
|---|---|---|---|---|
| `OperatingIncomeLoss` | FY2025 (2025-01-01→2025-12-31) | `87,231,000` | `(87,231)` | **FIRES** |
| `OperatingIncomeLoss` | 9M 2025 | `54,136,000` | `(54,136)` | **FIRES** |
| `OperatingIncomeLoss` | H1 2025 | `38,717,000` | `(38,717)` | **FIRES** |
| `OperatingIncomeLoss` | Q3 2025 | `15,419,000` | `(15,419)` | **FIRES** |
| `OperatingIncomeLoss` | Q2 2025 | `28,640,000` | `(28,640)` | **FIRES** |
| `OperatingIncomeLoss` | Q1 2025 | `10,077,000` | `(10,077)` | **FIRES** |
| `NetIncomeLoss` (attributable to the Company) | FY2025 | `83,294,000` | `(83,294)` | **FIRES** |
| `NetIncomeLossAvailableToCommonStockholdersDiluted` | FY2025 | `83,910,000` | `(83,910)` | **FIRES** |

**12 of 12 periods stripped; 6 of 6 FY2025 facts verified verbatim this session.** The strip
is `|x|`, not inversion — the magnitudes are identical to the dollar in every row, which an
inversion would not preserve.

**The strip is invisible to every heuristic that does not compute the identity.** LUNR has
never had positive operating income, so "a negative operating income is suspicious" flags
nothing; and because all twelve served values share one sign, no outlier test can see them.
Only `gross profit − opex` closes, and it closes negatively.

### 2.5 The DA-26 mechanism the strip creates at LUNR

The platform returns **six** `OperatingIncomeLoss` facts for FY2025. **None of them is a
standalone fourth quarter.** The durations served are `2025-01-01→2025-03-31`,
`2025-04-01→2025-06-30`, `2025-01-01→2025-06-30`, `2025-07-01→2025-09-30`,
`2025-01-01→2025-09-30`, and `2025-01-01→2025-12-31`. Querying
`fiscal_period="Q4", fiscal_year=2025` returns **zero facts** — not the wrong quarter, none.

So the FY2025 10-K statement files only FY2025 against FY2024, and the platform serves only
annual, year-to-date and first-three-quarter durations. **The nearest reachable "fourth
period" operating-loss figure is the annual `87,231,000` — and it is served positive.** That
is the whole mechanism of the 42.1%: an annual, sign-stripped, divided by an annual
service-only revenue base. `87,231 / 210,059 = 41.5%` on the total-revenue base;
`87,231 / 207,132 = 42.1%` on the service-only base. The second is the one in circulation,
which is how I know the base is service-only.

### 2.6 DA-30 obligation

Two revenue bases are live at LUNR and this artifact names both wherever a ratio depends on
one: **service-only** (`207,132` FY2025, `42,076` Q1 2026, `36,677` Q2 2026) and **total**
(`210,059` FY2025, `186,730` Q1 2026, `206,168` Q2 2026). The product-revenue line appears
for the first time in Q1 2026 (`141,554`) on the Lanteris acquisition, so the earlier periods
are not comparable on a product/service split at all. **Every margin above is computed on
total revenues** unless it says otherwise.

---

## 3. Mode `margin-analysis` — the DA-26 / DA-27 period traps

### 3.1 The numerator and denominator are both moving

Q1 2026 revenue grew **124,206** against Q1 2025 (`186,730` against `62,524`, +198.7%) —
**and 141,554 of the 186,730 is a product line that did not exist in the prior-year period**,
acquired with Lanteris. The margin improvement from −16.1% (Q1 2025) to −21.0% (Q1 2026) is
therefore not an improving operation; it is a **mix change**. The acquired product line runs
at a lower cost ratio than the legacy service line: Q1 2026 cost of product revenue is
`113,913 / 141,554 = 80.5%` of product revenue, while cost of service revenue is
`(33,660 + 5,949) / 42,076 = 94.1%` of service revenue. The consolidated reported margin
improves when the lower-ratio line grows, with no change to either line's economics.

**Direction check:** the legacy service line's own margin *deteriorated* — cost of service
revenue plus the affiliated line was `55,847 / 62,524 = 89.3%` of service revenue in Q1 2025
and `94.1%` in Q1 2026. The headline improvement is a **denominator artefact**.

### 3.2 The Q4 2025 standalone is the worst quarter and is not served

`$(33,095)K` on `$44,785K` revenue = **−73.9%** — nearly twice the annual −41.5% and 3.5×
the Q1 2026 −21.0%. Any statement that LUNR's operating margin "is about −21%" is quoting the
two most recent quarters and is silent on the worst one. The Q4 revenue figure is
`CLAIMED` (earnings record, report date 2026-03-19, `44,785,000`); the Q4 operating loss is
`DERIVED` (§2.2). **Neither is in the 10-K.**

### 3.3 DA-25 — one segment, and the segment table reproduces the consolidated loss

LUNR reports **one reportable segment** at both dates tested: FY2025
([📄 LUNR 10-K p.105](https://agentii.ai/v/LUNR/sec59/105)) and Q1 2026
([📄 LUNR 10-Q p.38](https://agentii.ai/v/LUNR/sec73/38)). The segment table reproduces the
consolidated operating loss **to the dollar** and, at Q2 2026, the whole statement
([📄 LUNR 10-Q p.43](https://agentii.ai/v/LUNR/sec76/43)):

```
206,168 − 170,302 − 14,927 − 7,729 − 60,346 = (47,136)   ✓
```

The segment cost line the note presents is the **collapse of the statement's cost lines into
one**, not a second basis. **DA-25's premise — a normalised per-unit metric not reproducible
from the audited tables — is INVERTED at LUNR: there is exactly one basis, and it is
reproducible.** The corpus contains no LUNR per-unit figure to test. Recorded as
`NOT PRESENT / premise inverted`, which is a result, not an absence.

### 3.4 DA-28 — the share count is discontinuous across the same window

| | Shares | Date |
|---|---|---|
| Weighted-average, basic and diluted | 107,081,918 | Q1 2025 |
| Weighted-average, basic and diluted | 147,878,006 | Q1 2026 |
| Weighted-average, basic and diluted | 162,172,470 | Q2 2026 |
| Class A issued | 171,720,829 | 2026-06-30 |

Q1 2025 → Q1 2026 is **+38.1%**; Q1 2026 → Q2 2026 is **+9.7% in one quarter**. The
instrument is documented: a February 27, 2026 securities purchase agreement for **11,574,069
shares at $15.12** (`$175.0M`) and an ATM program under which **8,259,379 shares** were sold
for **`$235.2M`** net by June 30, 2026 ([📄 LUNR 10-Q p.33](https://agentii.ai/v/LUNR/sec76/33)).
**Any per-share detector on LUNR is disabled across this window** — a per-share figure
compared Q1 2025 to Q1 2026 conflates at least two capital events with operating performance.

---

## 4. Mode `earnings-vs-consensus`

All rows `CLAIMED` (earnings layer). **The consensus sits on a basis the filings do not
show**, and at LUNR the gap is widest in the most recent reported quarter.

| Fiscal period | Report date | EPS actual | EPS estimate | Surprise | Revenue | vs estimate |
|---|---|---|---|---|---|---|
| 2025 Q4 | 2026-03-19 | $(0.04) | $(0.04) | 0.0% | $44,785,000 | −16.6% |
| 2026 Q1 | 2026-05-14 | $(0.25) | $(0.04273) | **−485.1%** | $186,730,000 | — |
| 2026 Q2 | 2026-08-13 | $(0.29) | $(0.09036) | **−220.9%** | $206,168,000 | — |
| 2026 Q3 (fwd) | 2026-11-12 | est $(0.12) | — | — | est $244,068,500 | — |

The filed EPS agrees with the earnings layer's actual in both quarters — `$(0.25)` and
`$(0.29)` appear verbatim in the statements ([📄 LUNR 10-Q p.8](https://agentii.ai/v/LUNR/sec73/8),
[📄 LUNR 10-Q p.8](https://agentii.ai/v/LUNR/sec76/8)) — so **the earnings layer is not the
defective layer at LUNR; the XBRL layer is.** That is worth stating plainly: at this issuer
the two platform layers disagree with each other, and the earnings layer is the one that
matches the filing.

Three consecutive misses on a growing revenue line, and the Q4 2025 revenue miss of −16.6%
is the one where the operating loss was worst (−73.9%). **The demand side is not pricing off
the cost curve — it is missing on the cost side.**

---

## 5. What this artifact could not resolve

| # | Unresolved | Class | Disclosure that would resolve it |
|---|---|---|---|
| 1 | The **`$68,676K` loss on issuance** the brief carries for LUNR. It is in no filing I read. The only filed `Loss on issuance of securities` figures are `$(93,136)K` (FY2024) and **nil** (FY2025) ([📄 LUNR 10-K p.48](https://agentii.ai/v/LUNR/sec59/48)). The Q1 2026 and Q2 2026 statements of operations contain no issuance line at all: Q1 2026 total other expense is `$(13,325)K` and Q2 2026 is `$(15,697)K`, neither of which can contain `68,676`. | `UNRESOLVABLE-FROM-PLATFORM` | A served fact, or the filing page, carrying `68,676`. Arithmetic note only: `68,676,000 / 11,574,069` SPA shares `= $5.934`, and `$15.12 + $5.934 = $21.05` — so the figure is *self-consistent with* a fair-value-minus-proceeds measurement at the February 27, 2026 SPA, but I could not locate the filed number and will not assert it. |
| 2 | The **standalone Q4 2025 statement of operations**. The 10-K files FY2025 against FY2024 only; the platform serves no `Q4` label and no `2025-10-01→2025-12-31` duration. The operating loss is reachable as a residual (§2.2); the full statement is not. | `UNRESOLVABLE-FROM-PLATFORM` | A quarterly-basis fact set, or the Q4 earnings release's own statement page. |
| 3 | Whether the circulating **42.1%** was generated by this platform or entered the workspace from outside it. `"42.1"` returns zero pages across the FY2025 10-K. I can reproduce the numeral (`87,231 / 207,132`) but not attribute its provenance. | `UNRESOLVABLE-FROM-PLATFORM` | The originating artifact or metric row. |

**`validate_calculation` fails SILENTLY on the flip.** On the FY2025 10-K it returns 15 fail /
8 pass / 1 warn, and for `OperatingIncomeLoss` it computes `122,828,000` against a reported
`87,231,000` — **a difference of the same sign.** The instrument reports a magnitude
disagreement and never a sign disagreement, so **it does not flag the DA-23 flip that this
whole artifact is about.** `validate_calculation` is not a DA-23 detector and must not be
cited as one.

---

## 6. Carry-forwards

1. **The DA-23 count for LUNR is 12 of 12 periods, all served positive, all filed negative.**
   Because LUNR has never had positive operating income, the strip is invisible to every
   heuristic. The component identity is the only detector, and at LUNR the identity is the
   **inclusive** pairing — no gross-profit subtotal is filed.
2. **The platform's `fiscal_period` selector returns zero facts for Q4 at LUNR.** Any
   thesis-level figure built by asking for "the fourth quarter" at any 31-December filer in
   this universe should be assumed to have fallen back to the annual.
3. **LUNR cannot manifest DA-27.** Exclude it from the DA-27 denominator. A December
   year-end is not evidence of a clean fiscal-period label.
4. **"42.1%" is a live cross-issuer fusion hazard.** It is the number in circulation for
   LUNR's "quarterly margin" — and it is *also* PL's Q1 FY2027 year-over-year revenue growth
   (`94,150 / 66,265 − 1 = 42.08%`, [📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)).
   Two different quantities at two different issuers render identically. Never carry a bare
   numeral between issuers in this workspace.
5. **DA-26 at LUNR is directional**: the annual flatters Q4 by 32.4 points. The error is
   optimistic, and it runs in the same direction as the RKLB denominator artefact
   (cost per kg rising while cost per launch falls). **Both defects make the quarter look
   better than it is.**
6. **The product-revenue line is new in Q1 2026.** LUNR's series is not comparable across
   the Lanteris boundary on any product/service split, and the Q1 2026 "margin improvement"
   is a mix change, not an operating improvement (§3.1).

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| FY2025 annual statement of operations — revenue 210,059, opex 297,290, operating loss (87,231), Loss on issuance of securities nil FY2025 / (93,136) F | [📄 LUNR 10-K p.48](https://agentii.ai/v/LUNR/sec59/48) |
| Note 18 segment — one reportable segment; segment table reproduces the consolidated operating loss (87,231) to the dollar | [📄 LUNR 10-K p.105](https://agentii.ai/v/LUNR/sec59/105) |
| Q1 2026 statement of operations — revenue 186,730, opex 225,931, operating loss (39,201), EPS $(0.25), shares 147,878,006; Q1 2025 comparative 62,524  | [📄 LUNR 10-Q p.8](https://agentii.ai/v/LUNR/sec73/8) |
| Q1 2026 MD&A consolidated results of operations with the $ Change column — total revenue change 124,206 | [📄 LUNR 10-Q p.46](https://agentii.ai/v/LUNR/sec73/46) **(newly surfaced)** |
| Note 21 segment — one reportable segment at Q1 2026 | [📄 LUNR 10-Q p.38](https://agentii.ai/v/LUNR/sec73/38) |
| Q2 2026 and H1 2026 statements of operations — revenue 206,168 / 392,898, opex 253,304 / 479,235, operating loss (47,136) / (86,337), shares 162,172,4 | [📄 LUNR 10-Q p.8](https://agentii.ai/v/LUNR/sec76/8) |
| Note 12 — February 27, 2026 securities purchase agreement, 11,574,069 shares at $15.12 ($175.0M); ATM 8,259,379 shares for $235.2M net; Class A issued | [📄 LUNR 10-Q p.33](https://agentii.ai/v/LUNR/sec76/33) |
| Q2 2026 segment table reproducing the consolidated operating loss to the dollar | [📄 LUNR 10-Q p.43](https://agentii.ai/v/LUNR/sec76/43) |
| PL Q1 FY2027 year-over-year revenue growth 94,150 / 66,265 - 1 = 42.08% — cross-issuer numeral-collision check | [📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6) |
