---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-5
ticker: PL
skill: recent-quarter
mode: methodology
generated_at: 2026-09-19T14:30:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07d26b9c738b"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-27
    chosen_reading: >
      PL is a 31-January filer, so the fiscal-quarter label and the calendar quarter
      disagree by one period. I read the period-END DATE as the basis and treat any bare
      `Qn` label without its fiscal-year anchor as unreadable. This issuer is the reason the
      rule exists.
  - da_id: DA-23
    chosen_reading: >
      The served sign is not evidence. Every negative served for PL is stripped to its
      absolute value; the filed sign is authoritative and the component identity is the
      detector.
  - da_id: DA-26
    chosen_reading: >
      A period is what its duration says it is. Where the platform serves no standalone
      fourth-quarter fact and the annual duration is present, the annual is the nearest
      reachable figure for that slot — and must be labelled annual.
  - da_id: DA-30
    chosen_reading: >
      Cost of revenue has two live bases at PL — consolidated as filed, and the segment
      note's narrower caption. Every margin here names its basis, and I report the pair
      rather than either one alone.
  - da_id: DA-29
    chosen_reading: >
      A reconciliation that closes is not thereby a check; but a reconciliation whose terms
      are all named and traceable to the source is a check that ran. PL's backlog note is
      the latter and I say so, rather than reporting a warning as a finding.
evidence_grade: DEMONSTRATED
citations:
  - figure: "Q1 FY2027 three months ended April 30, 2026 statement of operations — revenue 94,150, cost of revenue 43,749, gross profit 50,401, opex 85,289, loss from operations (34,888), net loss $(138,872), EPS $(0.40), shares 345,524,328"
    ticker: PL
    form_type: 10-Q
    citation_id: sec76
    page_no: 6
    url: https://agentii.ai/v/PL/sec76/6
    located_via: read_source_pages
  - figure: "Annual statements of operations, Year Ended January 31 — FY2026 / FY2025 / FY2024 revenue 307,727 / 244,352 / 220,696, gross profit 172,485 / 139,725 / 112,950, loss from operations (95,073) / (116,122) / (169,748)"
    ticker: PL
    form_type: 10-K
    citation_id: sec60
    page_no: 95
    url: https://agentii.ai/v/PL/sec60/95
    located_via: read_source_pages
  - figure: "Note 15 segment and geographic information — one reportable segment; segment cost of revenue 33,074 against the statement's 43,749; anti-dilutive securities 80,949,121; 2030 Notes"
    ticker: PL
    form_type: 10-Q
    citation_id: sec76
    page_no: 28
    url: https://agentii.ai/v/PL/sec76/28
    located_via: search_keyword_in_source
  - figure: "Note 14 net loss per share — two-class method, basic and diluted"
    ticker: PL
    form_type: 10-Q
    citation_id: sec76
    page_no: 27
    url: https://agentii.ai/v/PL/sec76/27
    located_via: search_keyword_in_source
  - figure: "Note 10 convertible notes — 2030 Notes interest expense; $460.0M principal and the 83.6715 conversion rate behind the 38,488,890 if-converted shares"
    ticker: PL
    form_type: 10-Q
    citation_id: sec76
    page_no: 24
    url: https://agentii.ai/v/PL/sec76/24
    located_via: search_keyword_in_source
  - figure: "Backlog-to-RPO reconciliation — 816,008 + 90,047 = 906,055; prior 852,435 + 47,992 = 900,427"
    ticker: PL
    form_type: 10-Q
    citation_id: sec76
    page_no: 42
    url: https://agentii.ai/v/PL/sec76/42
    located_via: read_source_pages
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM
key_metrics:
  operating_margin_at_zero_cost_of_revenue_pct_quarter: 9.4
  operating_margin_at_zero_cost_of_revenue_pct_annual: 13.1
  filed_operating_facts_stripped_of_total: "33/33"
  inclusive_opex_pairing_multiple_of_filed_loss_x: 2.25
---

# recent-quarter × PL — the best gross margin in the universe, and a fixed-cost wall

## 1. The finding

**PL has the highest gross margin of any issuer in this universe, and the curve's pass-through
cannot reach its operating line at all.** Cost of revenue consumes **46.5 points** of a
100-point revenue dollar; operating expenses consume **90.6 points**. The operating loss of
**−37.1%** is therefore not a launch-cost phenomenon — it is the arithmetic difference
between a 53.5-point gross margin and a 90.6-point fixed-cost load
([📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)):

```
94,150 − 43,749 = 50,401        gross profit          = 53.5% of revenue
85,289 / 94,150                 opex, exclusive       = 90.6% of revenue
50,401 − 85,289 = (34,888)      loss from operations  = −37.1% of revenue
```

**Bound:** hold opex at its filed level and set cost of revenue to **zero** — the best case
any launch-cost pass-through could ever deliver to this line — and PL's operating margin is
still only **+9.4%** (annual basis: +13.1%). **Even the complete elimination of PL's cost of
revenue does not produce an operating margin above low-double digits.** The pass-through
question at PL is answered by the fixed-cost load, not by the cost curve. This is PIL-5's
cost-side result at the one issuer whose gross margin makes it plausible.

**Period basis, stated because it is the defect this artifact is about:** the 53.5% and the
−37.1% are **QUARTER** figures — the three months ended **April 30, 2026**, which PL files as
**Q1 of fiscal 2027** and which a calendar-quarter mapping calls **Q2 2026**. On the **annual**
basis (year ended January 31, 2026) the same two ratios are **56.1%** gross and **−30.9%**
operating ([📄 PL 10-K p.95](https://agentii.ai/v/PL/sec60/95)). **The quarter is 6.2 points
worse at the operating line and 2.6 points worse at the gross line than the annual.** An
artifact quoting either pair without its basis misstates the other by more than half the
distance to zero.

Six further results:

1. **The component identity closes EXACTLY, on the exclusive pairing**, at all three annual
   dates and the latest quarter. PL files a `Gross profit` subtotal, so pairing it against the
   **inclusive** `CostsAndExpenses` double-counts cost of revenue and gives `(78,637)` against
   a filed `(34,888)` — a 43.7-point error from one pairing choice (§2.3).
2. **DA-23 fires: 33 of 33 served `OperatingIncomeLoss` facts positive, every filed value
   negative.** At PL, as at RKLB, the strip is invisible to any heuristic because the company
   has never had positive operating income.
3. **DA-27 MANIFESTS at PL — this is the trio's differentiator.** See §3.1. LUNR and YSS
   cannot manifest it and are excluded from that denominator.
4. **DA-26's mechanism is PRESENT but UNMANIFESTED at PL.** The platform serves no standalone
   fourth-quarter fact for FY2026 and `fiscal_period="Q4"` returns **zero facts** — the same
   gap that produced LUNR's "42.1% quarter". At PL nothing has yet fallen into it. **PRESENCE
   of the mechanism is not PRESENCE of the defect**; I report the exposure, not a finding.
5. **DA-25's premise is INVERTED.** PL reports **one reportable segment**, and its segment
   table reproduces the consolidated statement to the dollar.
6. **DA-29 does NOT fire at PL, and that is a result.** The backlog-to-RPO reconciliation names
   both its bases and closes on both dates (§3.4).

---

## 2. Mode `consolidated-p-and-l` — the DA-23 sign test

### 2.1 Filed cells

**Q1 FY2027, three months ended April 30, 2026 and 2025**
([📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)) — all `DEMONSTRATED`, in thousands:

| | Q1 FY2027 | Q1 FY2026 |
|---|---|---|
| Revenue | $94,150 | $66,265 |
| Cost of revenue | 43,749 | 29,662 |
| **Gross profit** | **50,401** | 36,603 |
| Research and development | 33,420 | 23,074 |
| Sales and marketing | 22,782 | 16,314 |
| General and administrative | 29,087 | 19,986 |
| **Total operating expenses** | **85,289** | 59,374 |
| **Loss from operations** | **(34,888)** | (22,771) |
| Change in fair value of warrant liabilities | (106,474) | 10,387 |
| Total other income (expense), net | (102,973) | 11,071 |
| Net loss | $(138,872) | $(12,628) |
| Basic and diluted net loss per share | $(0.40) | $(0.04) |
| Basic and diluted weighted-average shares | 345,524,328 | 300,267,952 |

**Annual, three fiscal years**
([📄 PL 10-K p.95](https://agentii.ai/v/PL/sec60/95)) — the statement header reads
**`Year Ended January 31,`**, which is the period-basis evidence for §3.1:

| | FY2026 | FY2025 | FY2024 |
|---|---|---|---|
| Revenue | $307,727 | $244,352 | $220,696 |
| Cost of revenue | 135,242 | 104,627 | 107,746 |
| **Gross profit** | **172,485** | 139,725 | 112,950 |
| Research and development | 106,749 | 101,006 | 116,339 |
| Sales and marketing | 72,676 | 77,694 | 86,304 |
| General and administrative | 88,133 | 77,147 | 80,055 |
| **Total operating expenses** | **267,558** | 255,847 | 282,698 |
| **Loss from operations** | **(95,073)** | (116,122) | (169,748) |
| Net loss | $(246,860) | $(123,196) | $(140,509) |
| Basic and diluted weighted-average shares | 307,799,424 | 292,124,291 | 279,585,698 |

### 2.2 The component identity, with the opex definition stated

**The opex definition I use at PL is the EXCLUSIVE one.** PL files a `Gross profit` subtotal,
so `Total operating expenses` runs from research and development to general and administrative
and **excludes cost of revenue**. The identity is `gross profit − opex = operating income`:

```
Q1 FY2027  50,401  −  85,289 = (34,888)   ✓ EXACT
FY2026    172,485  − 267,558 = (95,073)   ✓ EXACT
FY2025    139,725  − 255,847 = (116,122)  ✓ EXACT
FY2024    112,950  − 282,698 = (169,748)  ✓ EXACT
```

All four close to the dollar on filed cells. The opex build also ties independently:

```
Q1 FY2027  33,420 + 22,782 + 29,087 = 85,289   ✓
FY2026    106,749 + 72,676 + 88,133 = 267,558  ✓
```

**Four quarters telescope to the annual** — `66,265 + 73,386 + 81,254 + 86,822 = 307,727` —
which is what lets me date the missing fourth-quarter fact in §2.5.

### 2.3 The pairing that fails

`us-gaap:CostsAndExpenses` is **inclusive** of cost of sales. At PL, subtracting it from the
filed `Gross profit` subtracts cost of revenue **twice**:

```
50,401 − (43,749 + 85,289) = 50,401 − 129,038 = (78,637)   ✗ WRONG — filed is (34,888)
```

A reader who takes the platform's inclusive `CostsAndExpenses` caption, pairs it against gross
profit because that is the line the statement prints first, and does not check the identity,
gets an operating loss **2.25× the filed one**. Recorded as the failure mode, not the reading.
`EPS × shares` is not used as a sign test anywhere in this artifact.

### 2.4 Served vs filed — the verdict table

| Concept | Period | Served | Filed | Sign test |
|---|---|---|---|---|
| `OperatingIncomeLoss` | FY2026 (2025-02-01→2026-01-31) | `95,073,000` | `(95,073)` | **FIRES** |
| `OperatingIncomeLoss` | FY2025 | `116,122,000` | `(116,122)` | **FIRES** |
| `OperatingIncomeLoss` | FY2024 | `169,748,000` | `(169,748)` | **FIRES** |
| `OperatingIncomeLoss` | Q1 FY2027 | `34,888,000` | `(34,888)` | **FIRES** |
| `OperatingIncomeLoss` | all served periods | all positive | all negative | **FIRES, 33 of 33** |

The magnitudes are identical to the dollar in every row — the strip is `|x|`, not inversion.
**PL is a second issuer where the strip covers 100% of the series and therefore cannot be
found by an outlier test.** Only `gross profit − opex` closes, and it closes negatively.

### 2.5 The DA-26 mechanism — present, not manifested

The served `RevenueFromContractWithCustomerExcludingAssessedTax` facts for the FY2026 fiscal
year are: `66,265` (2025-02-01→2025-04-30), `73,386` (2025-05-01→2025-07-31), `81,254`
(2025-08-01→2025-10-31), `139,651` (H1), `220,905` (9M), and `307,727`
(2025-02-01→2026-01-31).

**There is no `2025-11-01→2026-01-31` fact.** The standalone fourth quarter is absent, exactly
as at LUNR. Querying `fiscal_period="Q4", fiscal_year=2026` returns **zero facts** — not the
wrong quarter, none. The FY2026 value `307,727` is served with a true twelve-month duration,
so **it is not posted as a quarter**; but it is the nearest reachable figure for the
fourth-period slot.

**The mechanism that produced LUNR's 42.1% is therefore fully present at PL and has not yet
produced a defect here.** I can evidence the gap; I cannot evidence a manifestation. Recorded
`PRESENCE / UNMANIFESTED`. `UNEXERCISED` and `CLEAN` are different verdicts, and this is the
first.

---

## 3. Mode `margin-analysis` — the DA-26 / DA-27 period traps

### 3.1 DA-27 manifests at PL

**PL's fiscal year ends January 31.** Four independent confirmations:

| Evidence | Reading |
|---|---|
| 10-K statement header | `Year Ended January 31,` 2026 / 2025 / 2024 ([📄 PL 10-K p.95](https://agentii.ai/v/PL/sec60/95)) |
| 10-Q statement header | `Three Months Ended April 30,` 2026 / 2025 ([📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)) |
| Served XBRL durations | `2025-02-01→2026-01-31` annual; `2026-02-01→2026-04-30` quarter |
| Earnings layer | the period reported 2026-06-04 is labelled **`2027 (Q1)`** |

**A calendar-quarter mapping of "April 30, 2026" writes Q2 2026. The issuer writes Q1 FY2027.
One full quarter of disagreement, in the same numeral.** An artifact that says "PL's Q2 2026
operating loss was 37%" and one that says "PL's Q1 FY2027 operating loss was 37%" describe the
same filed period while appearing to describe adjacent ones. The remedy is mechanical: **quote
the period-end date.** Every figure in this artifact that depends on a period carries
"three months ended April 30, 2026" or "year ended January 31, 2026".

**LUNR and YSS cannot manifest DA-27** — both are 31-December filers. They are **excluded from
the denominator**, not counted as clean.

### 3.2 The margin direction is not the direction the pass-through story needs

| Basis | Gross margin | Operating margin |
|---|---|---|
| FY2024 (yr to Jan 31, 2024) | 51.2% | −76.9% |
| FY2025 | 57.2% | −47.5% |
| FY2026 | 56.1% | −30.9% |
| **Q1 FY2027 (3M to Apr 30, 2026)** | **53.5%** | **−37.1%** |

**The gross margin has fallen for two consecutive periods — 57.2% → 56.1% → 53.5%**, while the
annual operating margin improved 46.0 points over two years and then **went backwards 6.2
points in the latest quarter**. If input costs were being passed through to the customer, the
gross margin would be stable or rising. It is falling, at the same time as revenue is growing
**+42.1% year over year** (`94,150` against `66,265`). **PL is growing revenue, losing gross
margin, and losing operating margin in the same quarter.** The released value is not reaching
this customer on the gross line, and on the operating line the fixed-cost load (§1) means it
could not reach it even if it did.

### 3.3 DA-30 — cost of revenue has two live bases, and one of them is 11.4 points optimistic

The segment note presents a cost of revenue **`33,074`**, which is **not** the consolidated
statement's **`43,749`** ([📄 PL 10-Q p.28](https://agentii.ai/v/PL/sec76/28)). A footnote on
the same note excludes depreciation and amortization, stock-based compensation, restructuring,
earnout payroll taxes and certain litigation from that caption.

A reader who takes the segment figure computes:

```
94,150 − 33,074 = 61,076     →  64.9% gross margin   against the filed 53.5%
```

**An 11.4-point gross-margin overstatement from one basis collapse, on the same page as the
segment table.** The segment table itself is internally consistent — the `Less:` lines sum to
`233,022`, `94,150 − 233,022 = (138,872)` equals the filed net loss, and the operating
sub-block closes at `(34,888)` — which is exactly what makes the collapsed caption dangerous:
**the reconciliation closes, and the caption still means something else than the statement's.**

**Both bases, as required:** cost of revenue is `43,749` on the consolidated basis
([📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)) and `33,074` on the segment basis
([📄 PL 10-Q p.28](https://agentii.ai/v/PL/sec76/28)). **All margins in this artifact are
consolidated.**

### 3.4 DA-29 does NOT fire — a well-argued negative

PL reconciles **Backlog** to **Remaining performance obligations** with **both bases named and
traceable to the filing** ([📄 PL 10-Q p.42](https://agentii.ai/v/PL/sec76/42)):

```
816,008  (remaining performance obligations)     + 90,047 (cancelable) = 906,055   ✓
852,435  (prior period, RPO)                     + 47,992 (cancelable) = 900,427   ✓
```

Both close, both periods are named, and each term is a filed caption rather than a back-solve.
This is a reconciliation that closes **and** is a check, which is the distinction DA-29 exists
to draw. **Recorded as `NOT PRESENT` with the arithmetic shown, so that a later reader does not
have to re-run it.** `check_contract.py` raises a DA-29 candidate on this artifact; the
candidate is discharged here rather than dismissed.

### 3.5 DA-28 — the share count moved while the anti-dilutive count fell

| | Q1 FY2026 | Q1 FY2027 | Change |
|---|---|---|---|
| Basic and diluted weighted-average shares | 300,267,952 | **345,524,328** | **+15.1%** |
| Anti-dilutive securities excluded from diluted EPS | 100,702,198 | **80,949,121** | **−19.6%** |

([📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6),
[📄 PL 10-Q p.28](https://agentii.ai/v/PL/sec76/28),
[📄 PL 10-Q p.27](https://agentii.ai/v/PL/sec76/27))

**The anti-dilutive count falls 19.6% while the actual count rises 15.1%** — and in the same
window a new if-converted instrument appears at **38,488,890 shares**, fully reproducible as
`$460.0M principal / $1,000 × 83.6715 = 38,488,890`
([📄 PL 10-Q p.24](https://agentii.ai/v/PL/sec76/24)). A detector that reads the
anti-dilutive line as "potential overhang" reports *falling* dilution on an issuer whose share
count rose 15.1% in one year. **DA-28's class is capital-structure discontinuity, and the trap
is that the discontinuity is in the detector, not in the denominator.** Any per-share
comparison across this window is inadmissible.

---

## 4. Mode `earnings-vs-consensus`

All rows `CLAIMED` (earnings layer). PL's consensus **beats on EPS** in its latest quarter while
its operating margin went backwards — the estimate is not tracking the fixed-cost line.

| Fiscal period | Report date | EPS actual | EPS estimate | Surprise | Revenue |
|---|---|---|---|---|---|
| 2025 Q4 | 2025-03-20 | $(0.08) | $(0.02) | −300.0% | $61,554,000 |
| 2026 Q1 | 2025-06-04 | $(0.0421) | $(0.03569) | −18.0% | $66,265,000 |
| 2026 Q2 | 2025-09-08 | $(0.03) | $(0.03) | 0.0% | $73,386,000 |
| 2026 Q3 | 2025-12-10 | $(0.19) | $(0.03349) | −467.3% | $81,254,000 |
| 2026 Q4 | 2026-03-19 | $(0.48) | $(0.04721) | **−916.7%** | $86,822,000 |
| **2027 Q1** | **2026-06-04** | **$(0.03)** | **$(0.04181)** | **+28.2% beat** | **$94,150,000** |

The filed Q1 FY2027 EPS is **`$(0.40)`**
([📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)) while the earnings layer records the actual
as **`$(0.03)`** on the same report date. **Neither is wrong; they are different bases.**
`$(0.40)` is the loss per share attributable to common stockholders for the quarter;
`$(0.03)` tracks an analyst basis the filings do not print. **The estimate sits on the second
basis and is therefore not comparable to the filed figure** — the "+28.2% beat" is a statement
about one basis, and the same quarter's filed net loss grew **11.0×** year over year
(`$(138,872)` against `$(12,628)`).

**The −916.7% and −467.3% surprises are not operating events.** They are the warrant-liability
fair-value line, which swings from `+10,387` (Q1 FY2026) to `(106,474)` (Q1 FY2027) and prints
**below** the operating line ([📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)). An earnings
surprise series read as an operating series at this issuer is contaminated on the DA-24 axis —
not inside operating income, but inside the EPS the consensus is measured against.

---

## 5. What this artifact could not resolve

| # | Unresolved | Class | Disclosure that would resolve it |
|---|---|---|---|
| 1 | Whether the missing standalone fourth-quarter facts (§2.5) have already produced a circulated quarterly figure for PL, as they did for LUNR. I can evidence the gap; I have found no PL figure that exploits it. | `UNRESOLVABLE-FROM-PLATFORM` | The originating artifact or metric row, if one exists. |
| 2 | PL's **standalone Q4 FY2026 statement of operations**. The annual files three full years side by side; the platform serves no `Q4` label. The quarter's revenue `86,822` is reachable as a residual (`307,727 − 220,905`) but its operating loss is not, because the 9-month duration for operating loss was not served in the same query. | `UNRESOLVABLE-FROM-PLATFORM` | A quarterly-basis fact set. |
| 3 | The **basis** of the `$(0.03)` consensus-basis actual. It appears nowhere in the filings, and no basis field accompanies it. | `UNRESOLVABLE-FROM-PLATFORM` | A basis field on the earnings record (DA-30's remedy). |

**Not unresolved, and worth recording as tested:** DA-29 (§3.4, does not fire), DA-25 (§ below,
premise inverted), DA-27 (§3.1, manifests).

---

## 6. Carry-forwards

1. **The pass-through bound is the finding.** With cost of revenue at **zero**, PL's operating
   margin is **+9.4%** on the quarter and **+13.1%** on the annual, holding opex. **No
   improvement in launch cost can move PL's operating line further than that.** Any claim that
   a cheaper launch reaches PL's earnings must first dispose of 90.6 points of fixed cost.
2. **Never quote a PL margin without its period-end date.** The issuer's Q1 is the calendar's
   Q2. This is DA-27's only live instance in the trio.
3. **PL's gross margin is falling while its revenue grows +42.1%.** 57.2% → 56.1% → 53.5% across
   FY2025 / FY2026 / Q1 FY2027. That is the empirical answer to "is the released value being
   passed through" at this customer: **no, it is being absorbed.**
4. **Cost of revenue has two bases at PL and the segment one is 11.4 points optimistic.** Never
   quote the segment caption as the statement's. This is DA-30's strongest instance in the trio
   because the reconciliation closes and the caption still misleads.
5. **The anti-dilutive line moved opposite to the share count.** −19.6% against +15.1%, with a
   new 38,488,890-share if-converted instrument in the same window. Do not use the anti-dilutive
   total as a dilution detector on any issuer in this universe.
6. **PL's earnings surprises are warrant-fair-value events, not operating events.** The largest
   miss in the series (−916.7%) is a line that sits below the operating block.
7. **`fiscal_period="Q4"` returns zero facts at PL and at LUNR.** If a thesis-level figure is
   built by selecting a fourth quarter in this universe, assume it fell back to the annual
   until proven otherwise.

---

## Sources

> Every figure asserted above resolves to the page cited. The frontmatter `citations` block and
> this table carry the same URLs; spec §1d requires the links **in the body**.

| Figure | Source |
|---|---|
| Q1 FY2027 (3M to Apr 30, 2026) statement of operations — revenue `94,150`, cost of revenue `43,749`, gross profit `50,401`, opex `85,289`, loss from operations `(34,888)`, net loss `$(138,872)`, EPS `$(0.40)`, shares `345,524,328` / `300,267,952` | [📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6) |
| FY2026 / FY2025 / FY2024 annual statements of operations (`Year Ended January 31,`) — revenue `307,727` / `244,352` / `220,696`, gross profit `172,485` / `139,725` / `112,950`, operating loss `(95,073)` / `(116,122)` / `(169,748)` | [📄 PL 10-K p.95](https://agentii.ai/v/PL/sec60/95) |
| Note 15 segment and geographic information — one reportable segment; segment cost of revenue `33,074` against the statement's `43,749`; anti-dilutive securities `80,949,121`; 2030 Notes | [📄 PL 10-Q p.28](https://agentii.ai/v/PL/sec76/28) |
| Note 14 net loss per share — two-class method, basic and diluted | [📄 PL 10-Q p.27](https://agentii.ai/v/PL/sec76/27) |
| Note 10 convertible notes — 2030 Notes interest expense; `$460.0M` principal and the `83.6715` conversion rate behind the 38,488,890 if-converted shares | [📄 PL 10-Q p.24](https://agentii.ai/v/PL/sec76/24) |
| Backlog-to-RPO reconciliation — `816,008 + 90,047 = 906,055`; prior `852,435 + 47,992 = 900,427` | [📄 PL 10-Q p.42](https://agentii.ai/v/PL/sec76/42) |
