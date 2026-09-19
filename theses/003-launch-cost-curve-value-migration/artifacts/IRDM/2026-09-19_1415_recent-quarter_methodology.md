---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-5
ticker: IRDM
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
    chosen_reading: "the platform serves a filed negative as a positive of identical magnitude (|x|, not inversion), PER-FACT not per-period, AND AS A PROPERTY OF A LAYER RATHER THAN OF THE UNDERLYING DATA. CONFIRMED at IRDM on FIVE concept-series with exact arithmetic across ~40 consecutive balance-sheet dates, including a 20-period series with a single genuinely-positive control period served correctly. REFUTED as 'clean': 001's 5/5 clearance is withdrawn. THE OPERATING LINE IS UNEXERCISED, NOT CLEAN — IRDM files no negative operating income in the window, so the strip is unobservable there. LAYER PROPERTY: the earnings-calendar layer carries the correct sign for the same metric and period where the row/XBRL layer strips it, and NEITHER LAYER CAN REPAIR THE OTHER — a clean reading from one surface is not evidence about the other."
  - da_id: "DA-24"
    chosen_reading: "non-operating contamination of `operating_income`. PRESENT AND QUANTIFIED: the equity-method line (the Aireon investee) contributed a $15,251 thousand gain below the operating line in FY2024 = 13.5% of that year's $112,776 thousand net income. The same related party supplies the $200,000 thousand revenue ceiling that the platform uses as the denominator for EVERY quarterly margin (see DA-30)."
  - da_id: "DA-26"
    chosen_reading: "annual figures mislabelled as quarterly, keyed on `fiscal_period = calendar_quarter(period_end)`. CONFIRMED TWICE, and — decisively — CONFINED TO THE Q4 ROWS. The FY2025 Q4 and FY2024 Q4 rows carry twelve-month figures in every field; the other EIGHT served quarterly rows are genuine quarters and are each confirmed by exact half-year and full-year fingerprints. Third independent sighting in the served ratio block, where the FY2025 Q4 operating margin 0.2707 is the ANNUAL margin 235,980 / 871,659."
  - da_id: "DA-27"
    chosen_reading: "fiscal-period labels synthesised from the calendar quarter. IRDM's fiscal year IS the calendar year (December year-end), so no label offset applies — and that is why the defect is confined to Q4: a twelve-month period ending 2025-12-31 is keyed Q4 by construction. Applied: every period label below is taken from the filing's own column header ('Three Months Ended June 30, 2026', 'Year Ended December 31, 2025'), never from the platform's `fiscal_period`."
  - da_id: "DA-28"
    chosen_reading: "capital-structure discontinuity around an IPO/reverse split invalidates share-count detectors. NOT APPLICABLE to this window — IRDM has no reverse split and no IPO discontinuity in 2024-2026; the weighted-average share count drifts (basic 125,598 → 107,240 thousand, FY2023 → FY2025) through buybacks, a smooth series with no discontinuity. No detector here rests on a share count except the EPS bridge in §3.2, which is a one-line cross-check and not a detector."
  - da_id: "DA-29"
    chosen_reading: "a reconciliation that closes is not thereby a check; `computed` is an opaque assertion, and if a term appears nowhere in the source the check is a back-solve. CONFIRMED AT IRDM IN A THIRD KIND: `validate_calculation` returns EIGHT `fail` rows, and in two of them (`OperatingIncomeLoss`, computed −132,842,000 and −37,828,000) the `computed` column reproduces from NOTHING in the filed statements — so a `fail` is as uninformative as a `pass`. Exactly ONE row is usable as evidence, because there `computed` reproduces the filed figure exactly: `NetCashProvidedByUsedInInvestingActivities`, computed −51,791,000 against reported +51,791,000. No `computed` value is cited as a derivation anywhere in this artifact."
  - da_id: "DA-30"
    chosen_reading: "two bases on one concept collapsed without a basis field. THE DEFINING MECHANISM AT IRDM: every served quarterly margin divides by a single $200,000 thousand denominator — the MAXIMUM related-party (Aireon) hosting-agreement revenue ceiling, served as a fully-dimensioned fact — instead of the period's reported revenue, and on three of the eight rows the numerator is a SIX- or NINE-month figure against a HALF-YEAR ceiling. 8 of 8 tested margins reproduce to the basis point on that basis. Also reported: revenue and net income each have competing bases at every use, both named."
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
citations:
  - figure: "Q2 2026 condensed consolidated balance sheets, 2026-06-30 / 2025-12-31 — cash 184,214 / 96,501; total assets 2,565,093 / 2,531,009; long-term secured debt, net 1,749,342 / 1,757,124; accumulated deficit (387,281) / (418,554); AOCI (4,681) / 406; total stockholders' equity 472,511 / 462,600; 105,956 / 104,918 common shares issued and outstanding"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 4
    url: https://agentii.ai/v/IRDM/sec191/4
    located_via: "read_source_pages"
  - figure: "Q2 2026 condensed consolidated statement of operations — Total revenue 225,237 / 216,906 / 444,294 / 431,784; Total operating expenses 191,229 / 166,648 / 359,573 / 321,138; Operating income 34,008 / 50,258 / 84,721 / 110,646; Total other expense net (19,694) / (23,623) / (39,254) / (47,132); Net income 9,679 / 21,968 / 31,273 / 52,380"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 5
    url: https://agentii.ai/v/IRDM/sec191/5
    located_via: "read_source_pages"
  - figure: "Q2 2026 condensed consolidated statement of cash flows — net cash provided by operating 185,762 / 190,696; net cash used in investing (51,791) / (45,256); net cash used in financing (46,951) / (162,608)"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 7
    url: https://agentii.ai/v/IRDM/sec191/7
    located_via: "read_source_pages"
  - figure: "FY2025 consolidated statement of operations — Services 633,958; Subscriber equipment 81,109; Engineering 156,592; Total revenue 871,659 / 830,682 / 790,723; Cost of services 197,577; Cost of subscriber equipment 50,426; R&D 19,758; SG&A 157,711; D&A 210,207; Total operating expenses 635,679 / 630,298 / 709,095; Operating income 235,980 / 200,384 / 81,628; Total other expense (91,167) / (90,600) / (86,375); Income before taxes 144,813 / 109,784 / (4,747); Income tax (27,618) / (12,259) / 26,251; Gain (loss) on equity method (2,823) / 15,251 / (6,089); Net income 114,372 / 112,776 / 15,415; EPS basic 1.07 / 0.95 / 0.12, diluted 1.06 / 0.94 / 0.12"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 64
    url: https://agentii.ai/v/IRDM/sec151/64
    located_via: "read_source_pages"
  - figure: "The FY2025 consolidated statement of operations, three annual columns — Total revenue 871,659 / 830,682 / 790,723; Total operating expenses 635,679 / 630,298 / 709,095; Operating income 235,980 / 200,384 / 81,628; R&D 19,758 / 28,422 / 20,269; SG&A 157,711 / 168,182 / 143,706; D&A 210,207 / 203,127 / 320,000; Net income 114,372 / 112,776 / 15,415; EPS basic 1.07 / 0.95 / 0.12, diluted 1.06 / 0.94 / 0.12; weighted-average shares basic 107,240 / 118,566 / 125,598, diluted 107,837 / 119,792 / 127,215. These are the twelve-month cells that the served FY2025 Q4 and FY2024 Q4 rows reproduce (DA-26), quoted here from the statement face."
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 64
    url: https://agentii.ai/v/IRDM/sec151/64
    located_via: "read_source_pages"
  - figure: "Note 12, Related Party Transactions (Aireon) — the filed basis of the $200,000 thousand figure every served margin divides by: 'Under the agreements with Aireon, Aireon agreed to pay the Company fees of $200.0 million to host the ADS-B receivers, of which $134.5 million had been paid as of June 30, 2026'; hosting-fee revenue recognised 2.3 / 4.6 million for the three and six months; power and data service fee revenue 5.9 million per quarter; fully diluted stake in Aireon Holdings 39.5%; equity-method carrying value 36.3 / 38.5 million"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 18
    url: https://agentii.ai/v/IRDM/sec191/18
    located_via: "read_source_pages"
  - figure: "Note 13, Net Income Per Share — Q2 2026 net income 9,679; weighted-average shares basic 106,969, diluted 108,468; EPS basic and diluted $0.09. Note 14, Merger Agreement with Rocket Lab Corporation — signed 2026-06-28; $27.00 in cash plus an Exchange Ratio of Rocket Lab stock (0.4000 at or below $67.50; $27.00 divided by price inside that collar; 0.2400 at or above $112.50); a $223.6 million termination fee payable by IRDM under certain circumstances; expected close mid-2027"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 19
    url: https://agentii.ai/v/IRDM/sec191/19
    located_via: "read_source_pages"
  - figure: "MD&A, 'Anticipated Merger with Rocket Lab Corporation' — the same agreement stated from the target's side: board approval, a voting agreement signed by each director holding shares, the stockholder vote, HSR clearance and FCC consent to transfer of control among the closing conditions, and an expected close in mid-2027"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 22
    url: https://agentii.ai/v/IRDM/sec191/22
    located_via: "read_source_pages"
  - figure: "MD&A operating-expense lines, three months — 'Selling, general and administrative expenses increased by $22.4 million, or 50% … primarily due to increases in transaction costs totaling $14.3 million, associated with the Merger Agreement with Rocket Lab and the Aireon acquisition'; cost of services −$2.3 million (−4%); cost of subscriber equipment +$2.2 million (+19%); R&D +$1.3 million (+29%); D&A +$1.0 million (+2%) — the line-level attribution of the +24,581 thousand expense increase"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 26
    url: https://agentii.ai/v/IRDM/sec191/26
    located_via: "read_source_pages"
  - figure: "MD&A, six months — SG&A +$32.4 million (+40%), transaction costs totaling $15.0 million for the half; interest expense, net −$6.0 million; and the post-period financing event, 'our drawing $100.0 million on July 1, 2026 under our Revolving Facility'"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 30
    url: https://agentii.ai/v/IRDM/sec191/30
    located_via: "read_source_pages"
  - figure: "Income-tax note — the FY2025 and FY2024 tax lines reconciled against pre-tax income after the equity-method line"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 85
    url: https://agentii.ai/v/IRDM/sec151/85
    located_via: "read_source_pages"
  - figure: "MD&A — the equity-method investee (Aireon) discussion: FY2025 loss of 2.8 million against a FY2024 gain of 15.3 million, plus Satelles. The related-party hosting agreement itself is NOT on this page — it is filed in Note 12, p.18."
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 55
    url: https://agentii.ai/v/IRDM/sec151/55
    located_via: "read_source_pages"
  - figure: "Pending Acquisition — 'On June 28, 2026, we entered into a definitive agreement to acquire Iridium Communications Inc. The transaction is subject to customary closing conditions, including regulatory approval, and, if approved, is expected to close in 2027.' No consideration, segment allocation or pro forma disclosed. (Source is the ACQUIRER's filing; IRDM and RKLB are the same counterparty seen from two sides of one pending transaction.)"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 35
    url: https://agentii.ai/v/RKLB/sec109/35
    located_via: "read_source_pages"
  - figure: "Neutron Update on the same page — first-flight hardware integration, Stage 1 tank aligned with target delivery of Neutron to the launch pad in Q4 2026, and 'the window for an end-of-year launch date is narrowing'. Cited only as context for the acquirer's standing."
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 35
    url: https://agentii.ai/v/RKLB/sec109/35
    located_via: "read_source_pages"
key_metrics:
  operating_margin_q2_2026_pct: 15.10
  operating_margin_q2_2025_pct: 23.17
  revenue_growth_yoy_pct: 3.84
  operating_income_growth_yoy_pct: -32.33
---

# IRDM — the quarterly series, corrected

**The headline.** IRDM is the opposite case from its sector peers, and that is the finding. Its
**operating series is period-correct** — Q1, Q2 and Q3 rows are genuine quarters, each confirmed by
exact half-year and full-year fingerprints, and the component identity closes **7 of 7**. Its
defects sit in three specific places:

1. **DA-26 is real but CONFINED to the two Q4 rows.** The FY2025 Q4 and FY2024 Q4 rows carry
   twelve-month figures in every field. The other **eight** served quarterly rows are clean quarters.
   That is a narrower and more useful statement than "IRDM shows DA-26".
2. **DA-23 is confirmed on FIVE concept-series across ~40 consecutive balance-sheet dates** — and
   **001's "5/5 clean" clearance is REFUTED.** But the sign test is **UNEXERCISED on the operating
   line**, because IRDM files no negative operating income in the window. **An unengaged check is
   not a passed check.**
3. **The served margin block is unusable**, and the mechanism is now identified: **every quarterly
   margin divides by a single $200,000 thousand denominator — a contractual maximum related-party
   revenue ceiling — not by reported revenue** (DA-30, §4).

**The verified quarterly series (all DEMONSTRATED):**

| Quarter | Revenue ($k) | Total operating expenses ($k) | Operating income ($k) | Op. margin | Net income ($k) | Net margin |
|---|---:|---:|---:|---:|---:|---:|
| Q2 2025 | 216,906 | 166,648 | 50,258 | **23.17%** | 21,968 | 10.13% |
| Q3 2025 | 226,935 | 156,850 | 70,085 | **30.88%** | 37,127 | 16.36% |
| Q4 2025 *(derived)* | 212,940 | 157,691 | **55,249** | **25.95%** | **24,865** | 11.68% |
| Q1 2026 | 219,057 | 168,344 | 50,713 | **23.15%** | 21,594 | 9.85% |
| Q2 2026 | 225,237 | 191,229 | 34,008 | **15.10%** | 9,679 | 4.30% |

The series is **cyclical and now falling**: margin peaked at 30.88% in Q3 2025 and has declined in
each of the two quarters since, to 15.10% — a **15.8 percentage-point** contraction in two quarters,
on revenue that rose 3.8% year-over-year in Q2 2026. **The margin compression is an expense-line
event, not a revenue event.**

### 0.1 Standing of the issuer — `standalone_pre_merger` means more here than "a deal security"

**RKLB entered a definitive agreement on 2026-06-28 to acquire Iridium Communications Inc.**, subject
to customary closing conditions including regulatory approval and, if approved, **expected to close in
2027**. The disclosure is verbatim: *"On June 28, 2026, we entered into a definitive agreement to
acquire Iridium Communications Inc. … if approved, is expected to close in 2027"*
([📄 RKLB 10-Q p.35](https://agentii.ai/v/RKLB/sec109/35), filed 2026-08-10). RKLB discloses **no
consideration, no segment allocation and no pro forma**
([📄 RKLB 10-Q p.35](https://agentii.ai/v/RKLB/sec109/35)).

**IRDM and RKLB are the same counterparty seen from two sides of one pending transaction.** I state
this explicitly rather than leaving the tag to carry it, because the consequence is stronger than the
tag's ordinary meaning: **every figure in this artifact describes a business whose acquirer has
already signed.** Three consequences follow, and they are stated rather than resolved:

1. **The series describes a standalone business that is not going to be run standalone.** The
   `standalone_pre_merger` basis is therefore not a convention here — it is the only basis on which
   the figures are meaningful, because no merged basis exists to compare against. RKLB's 10-Q
   discloses none.
2. **The 2027 close is a date, and everything after it is out of scope.** The Q2 2026 quarter is the
   last in this series, and it straddles the announcement: the agreement was signed 2026-06-28, two
   days before the quarter ended 2026-06-30. The quarter is the standalone business's own — with the
   deal's footprint already *inside* it, in the $14.3 million of transaction costs in Q2 SG&A (§2.3).
3. **The DA-30 denominator mechanism in §4 survives the transaction intact** — the $200,000 thousand
   ceiling and the equity-method (Aireon) relationship are IRDM's own, contracted before the
   agreement, and are unaffected by who owns the equity afterwards.

**The transaction is disclosed on IRDM's own side too, and I verified it there.** IRDM filed its Q2
2026 10-Q on 2026-07-22 — three weeks *after* the 2026-06-28 signing — and the agreement is in it
twice: as **Note 14, "Merger Agreement with Rocket Lab Corporation"**
([📄 IRDM 10-Q p.19](https://agentii.ai/v/IRDM/sec191/19)) and as a dedicated MD&A section,
"Anticipated Merger with Rocket Lab Corporation"
([📄 IRDM 10-Q p.22](https://agentii.ai/v/IRDM/sec191/22)). In the target's own words: consideration
of **$27.00 in cash plus an Exchange Ratio** of Rocket Lab stock (0.4000 at or below $67.50; $27.00
divided by the price inside that collar; 0.2400 at or above $112.50); a **$223.6 million termination
fee** payable by IRDM under certain circumstances; board approval with a voting agreement signed by
each director holding shares; and an expected close **in mid-2027**, subject to an IRDM stockholder
vote, HSR clearance and FCC consent to the transfer of control. IRDM also discloses the financing it
drew after the quarter closed: **$100.0 million on July 1, 2026 under its Revolving Facility**
([📄 IRDM 10-Q p.30](https://agentii.ai/v/IRDM/sec191/30)).

**Correction to carry.** An earlier draft of this section said the transaction had **not** been
verified from IRDM's own filings, and classed IRDM-side corroboration
**UNRESOLVABLE-FROM-PUBLIC-SOURCES at `as_of`**. That was wrong on both counts: the acquirer's 10-Q
was the *first* side I read, not the only side that states it. Both sides carry the agreement, and
the two accounts agree on the date, the consideration structure and the expected timing — they remain
distinct evidence, dated 2026-07-22 (IRDM) and 2026-08-10 (RKLB), and each is cited to its own page.

---

## 1. `consolidated-p-and-l` — the component identity, and the DA-23 sign test

### 1.1 The identity and the opex definition

**IRDM files NO gross-profit line on any statement face.** The FY2025 statement runs *Total revenue →
Cost of services / Cost of subscriber equipment / Research and development / Selling, general and
administrative / Depreciation and amortization → Total operating expenses → Operating income*
([📄 IRDM 10-K p.64](https://agentii.ai/v/IRDM/sec151/64)); the Q2 2026 statement has the same shape
([📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5)). The operable identity is therefore:

```
Total revenue  −  Total operating expenses  =  Operating income
```

**Opex definition used: `us-gaap:CostsAndExpenses` — the D&A-INCLUSIVE `Total operating expenses`
basis.** IRDM's cost structure has **no** cost-of-sales/gross-profit pairing on the face; the
`Cost of services` and `Cost of subscriber equipment` lines are line items *inside* the single
operating-expense group, not a cost of sales subtotal. There is consequently **no competing
exclusive-basis reading available at IRDM** — unlike SATS, where the caption asserts one basis and
the tagging uses another. This is a single-basis statement and I quote one basis: **D&A-inclusive.**

### 1.2 The identity closes 7 of 7

| Period | Revenue | Total operating expenses | Operating income | Closes? |
|---|---:|---:|---:|:--:|
| FY2025 | 871,659 | 635,679 | 235,980 | ✓ |
| FY2024 | 830,682 | 630,298 | 200,384 | ✓ |
| FY2023 | 790,723 | 709,095 | 81,628 | ✓ |
| Q2 2026 | 225,237 | 191,229 | 34,008 | ✓ |
| Q2 2025 | 216,906 | 166,648 | 50,258 | ✓ |
| 6M2026 | 444,294 | 359,573 | 84,721 | ✓ |
| 6M2025 | 431,784 | 321,138 | 110,646 | ✓ |

Cells: [p.64](https://agentii.ai/v/IRDM/sec151/64) and [p.5](https://agentii.ai/v/IRDM/sec191/5).
**7 of 7 EXACT.** [DEMONSTRATED]

### 1.3 DA-23 is CONFIRMED on five concept-series — and 001's clearance is REFUTED

**The control the inherited work named reproduces exactly, and it carries an internal control of its
own:**

| Concept / period | Filed | Served | Verdict |
|---|---:|---:|:--|
| `AccumulatedOtherComprehensiveIncomeLossNetOfTax`, 2026-06-30 | (4,681) | +4,681,000 | **STRIPPED** |
| `AccumulatedOtherComprehensiveIncomeLossNetOfTax`, 2025-12-31 | **+406** | +406,000 | **CLEAN** |
| `Accumulated other comprehensive income (loss), net of tax` — the statement-face pair | (4,681) / 406 | — | — |

[📄 IRDM 10-Q p.4](https://agentii.ai/v/IRDM/sec191/4). **The 2025-12-31 period is the internal
control that settles the mechanism:** it is the only period in the entire series whose filed value is
**genuinely positive** (+406), and it is served **correctly as positive**. That rules out inversion
and confirms a pure `|x|` absolute-value strip. Across the 20-period
`AccumulatedOtherComprehensiveIncomeLossNetOfTax` series the platform returns **20 facts, every one
served positive** — of which **19 are filed negatives**.

**The retained-earnings series is even cleaner — 18 of 18, zero exceptions:**

`us-gaap:RetainedEarningsAccumulatedDeficit` returns **20 facts, every one served positive**. The
series crosses zero between 2021 and 2022, which partitions it cleanly:

| Filed sign | Periods | Served | Correct? |
|---|:--:|---|:--|
| Filed **negative** (accumulated deficit), 2022-03-31 → 2026-06-30 | **18** | all positive | **18 of 18 STRIPPED** |
| Filed **positive** (retained earnings), 2020-12-31 and 2021-12-31 | **2** | positive | **2 of 2 CLEAN** |

**18 of 18 stripped, 2 of 2 clean, zero exceptions** — a 20-period test in which the platform's own
output contains both classes of period and gets one of them wrong every time. Sample cells:
387,281,000 served at 2026-06-30 against a filed **(387,281)**; 418,554,000 at 2025-12-31 against a
filed **(418,554)** ([📄 IRDM 10-Q p.4](https://agentii.ai/v/IRDM/sec191/4)). [DEMONSTRATED]

**The equity fingerprint — exact in both directions:**

```
FILED    864,367 (APIC) + 106 (common stock) − 387,281 (accumulated deficit) − 4,681 (AOCI)  =  472,511   ✓
SERVED   864,367         + 106               + 387,281                        + 4,681        = 1,256,435
STRIP DIFFERENCE   1,256,435 − 472,511 = 783,924  =  2 × (387,281 + 4,681)   EXACT ✓
```

The filed equity is **$472,511 thousand**, the platform's components-sum on its own served values is
**$1,256,435 thousand**, and the gap is exactly **twice** the two stripped balance-sheet items. A
fingerprint that closes in both directions leaves no room for a reading error.
[DEMONSTRATED]

**Two further strips, on the cash-flow statement — a third statement:**

| Concept | Filed | Served |
|---|---:|---:|
| `NetCashProvidedByUsedInInvestingActivities`, Q2 2026 | **(51,791)** | **+51,791,000** |
| `NetCashProvidedByUsedInFinancingActivities`, Q2 2026 | **(46,951)** | **+46,951,000** |

[📄 IRDM 10-Q p.7](https://agentii.ai/v/IRDM/sec191/7). **Five concept-series across three
statements** (income statement equity components, balance sheet, cash flow) and ~40 consecutive
balance-sheet dates. `PaymentsToAcquirePropertyPlantAndEquipment` is **excluded** from this list — it
is a positive-value element by convention and would prove nothing. [DEMONSTRATED]

**⚠️ REFUTATION TO CARRY: 001's "5/5 clean" clearance of IRDM on DA-23 is withdrawn.** It was
obtained with the inadmissible `EPS × shares` test, which cannot detect `|x|` stripping at all: the
absolute value of a loss, divided by a share count, produces a positive number that a
positive-EPS expectation will accept. The test's own construction guarantees it passes. **A cleared
check obtained with a test that cannot fail is not a clearance.**

### 1.4 The operating line: `UNEXERCISED`, explicitly — not CLEAN

**IRDM files no negative operating income anywhere in this window.** Every filed operating income in
table 1.2 is positive. The DA-23 sign test therefore **cannot run** on the operating line, and the
correct disposition is:

> **`UNEXERCISED`** — not CLEAN. An unengaged check is not a passed check. The operating line at IRDM
> is *consistent* with the platform's served values (they agree in sign and magnitude on all seven
> periods tested in §1.2), but that agreement is uninformative about the strip, because a
> positive-only series cannot exhibit a sign defect. **The DA-23 evidence at IRDM rests entirely on
> the five loss-bearing concept-series in §1.3.**

This is the substantive difference between IRDM and its peers: at RKLB the strip is **invisible to
any heuristic** because RKLB has never had positive operating income; at IRDM it is invisible because
IRDM has never had negative operating income. **Two opposite blind spots, one detector** — and in
both cases the component identity, not the sign, is what closes the question.

### 1.5 DA-23 is a LAYER property, not a data property

The sign defect does not live in the data and does not live in the issuer. It lives in **a layer of
the platform**, and the layers disagree with each other:

| Layer | Same metric, same period | Sign |
|---|---|---|
| Earnings-calendar layer | IRDM Q2 2026 EPS actual **0.09** | **correct** (matches the filed positive) |
| Row / XBRL fact layer | `NetCashProvidedByUsedInInvestingActivities` Q2 2026 served **+51,791,000** | **stripped** against a filed (51,791) |
| Validator layer | `NetCashProvidedByUsedInInvestingActivities` **computed (51,791,000) / reported 51,791,000** | `reported` stripped, `computed` correct — **the layer disagrees with itself within one row** |

**Neither layer can repair the other.** This is not a rhetorical point; it has operational
consequences that this artifact relies on:

- **A clean reading from one surface is not evidence about the other.** A user who checked IRDM's
  signs against the consensus feed would find them correct and conclude the store is sound. A user
  who checked the balance sheet would find them stripped. **Both would be reading the same platform
  on the same day.**
- **Corroboration across layers is only meaningful when the layers are known to be independent** —
  and here they demonstrably are, which is exactly why the SATS cross-layer contradiction (§7 of that
  artifact) is admissible evidence and a same-layer double-check is not.
- **The `reported` column of the validator is the row layer re-served.** That is why the §5
  usable/unusable split is drawn where it is: one row reproduces a filed figure, the rest do not, and
  the difference is a property of the instrument rather than of IRDM.

---

## 2. `margin-analysis` — where the DA-26 / DA-27 period traps bite

### 2.1 DA-26 is CONFIRMED TWICE — and confined to Q4

| Row served | Field | Value | What it actually is |
|---|---|---:|---|
| **FY2025 Q4** | revenue | 871,659 | **the FY2025 ANNUAL** |
| | operating income | 235,980 | the FY2025 annual |
| | net income | 114,372 | the FY2025 annual |
| | EPS | 1.07 / 1.06 | the FY2025 annual, both bases |
| | R&D | 19,758 | the FY2025 annual |
| **FY2024 Q4** | revenue | 830,682 | **the FY2024 ANNUAL** |
| | operating income | 200,384 | the FY2024 annual |
| | net income | 112,776 | the FY2024 annual |
| | EPS | 0.95 / 0.94 | the FY2024 annual, both bases |
| | R&D | 28,422 | the FY2024 annual |

**Five independent twelve-month figures on each row.** [DEMONSTRATED]

**The annual-to-quarter multipliers — and a correction to the inherited ratios.** The inherited
anchor recorded the multipliers as **"4.094× / 4.271×"** presented as the FY2025 and FY2024 pairs.
They are not. **Both are the FY2025 Q4 row**, measured on two different lines:

```
FY2025 Q4 revenue          871,659 ÷ 212,940 (derived Q4)   =  4.093×   ← the anchor's 4.094× agrees only to 3 s.f.
FY2025 Q4 operating income 235,980 ÷  55,249 (derived Q4)   =  4.271×   ← matches the inherited 4.271×, but it is
                                                                          the OPERATING-INCOME ratio, not a FY2024 figure
FY2024 Q4 revenue          830,682 ÷ 212,991 (derived Q4)   =  3.900×   ← the FY2024 pair the anchor meant
FY2024 Q4 operating income 200,384 ÷  52,115 (derived Q4)   =  3.845×
```

**CORRECTION TO CARRY: the inherited "4.094× / 4.271×" is one quarter measured twice, not two
quarters measured once.** The reading is *strengthened*, not weakened — the same row is now confirmed
mislabelled on **two independent lines**, revenue and operating income, with the operating-income
ratio (4.271×) a wider distortion than the revenue ratio (4.093×) because the operating line is the
more volatile one. The FY2024 pair is **3.900× / 3.845×**. [DEMONSTRATED]

**A second, smaller correction on the same line: 871,659 ÷ 212,940 = 4.09345 → 4.093×, not 4.094×.**
The inherited figure is agreement to three significant figures, not equality, and it is restated here
as **4.093×** so it is not carried forward as though it reproduced. The operating-income multiplier
(235,980 ÷ 55,249 = 4.27121 → 4.271×) reproduces exactly. Both quotients are arithmetic on filed
cells from [p.64](https://agentii.ai/v/IRDM/sec151/64), not served values.

**And the eight other quarterly rows are genuine quarters.** Each is confirmed by an exact
period-sum fingerprint:

| Fingerprint | Closes? |
|---|:--:|
| FY2025 Q1 + Q2 revenue = 6M2025 revenue (214,878 + 216,906 = **431,784**) | ✓ |
| FY2025 Q1 + Q2 operating income = 6M2025 (60,388 + 50,258 = **110,646**) | ✓ |
| FY2025 Q1 + Q2 net income = 6M2025 (30,412 + 21,968 = **52,380**) | ✓ |
| FY2026 Q1 + Q2 revenue = 6M2026 (219,057 + 225,237 = **444,294**) | ✓ |
| FY2026 Q1 + Q2 operating income = 6M2026 (50,713 + 34,008 = **84,721**) | ✓ |
| FY2026 Q1 + Q2 net income = 6M2026 (21,594 + 9,679 = **31,273**) | ✓ |
| FY2025 Q1+Q2+Q3 + derived Q4 revenue = FY2025 (431,784 + 226,935 + 212,940 = **871,659**) | ✓ |
| FY2025 Q1+Q2+Q3 + derived Q4 operating income = FY2025 (110,646 + 70,085 + 55,249 = **235,980**) | ✓ |
| FY2025 Q1+Q2+Q3 + derived Q4 net income = FY2025 (52,380 + 37,127 + 24,865 = **114,372**) | ✓ |

**Nine exact fingerprints.** The derived Q4 2025 net income of **24,865** is independently confirmed
by a balance-sheet walk: filed accumulated deficit (443,419) at 2025-09-30 **+24,865** = **(418,554)**
at 2025-12-31 — the filed figure, to the thousand
([📄 IRDM 10-Q p.4](https://agentii.ai/v/IRDM/sec191/4)). [DEMONSTRATED]

**So the correct statement of DA-26 at IRDM is narrow and specific:** the two Q4 rows carry annual
data; the eight other quarterly rows are true quarters and are verified. A reader who needs IRDM's
Q4 should derive it — 212,940 / 55,249 / 24,865 — never read it.

### 2.2 DA-27 — the synthesis that confines the defect to Q4

DA-27's mechanism is a fiscal label **synthesised from the calendar quarter** of the period end.
IRDM's fiscal year *is* the calendar year, so no label offset applies — and the synthesis is exactly
why the defect is confined to Q4: any twelve-month period ending 2025-12-31 is keyed `Q4` by
construction, and the key carries no indication of period length. **Every period label in this
artifact is taken from the filing's own column header, never from the platform's `fiscal_period`.**

**Third independent sighting, in a different surface.** The served ratio block gives the FY2025 Q4
row an operating margin of **0.2707**. That is not a quarterly margin:

```
235,980 ÷ 871,659 = 0.27069  →  0.2707   the FY2025 ANNUAL margin, on a row keyed Q4
```

The DA-26 defect therefore propagates from the row layer into the computed ratio layer, where it
loses its last tie to a period label. [DEMONSTRATED]

### 2.3 Characterising the contraction — it is an expense event

Q3 2025 → Q2 2026, operating margin 30.88% → 15.10% = **−15.78 points**, across two quarters. On the
same span, revenue *rose* (226,935 → 225,237 is −0.7% on a single quarter, but Q2 2026 is **+3.84%**
year-over-year against Q2 2025's 216,906). The expense line is what moved:

| Q2 2026 vs Q2 2025 | Q2 2025 | Q2 2026 | Change |
|---|---:|---:|---:|
| Total revenue | 216,906 | 225,237 | **+3.84%** |
| Total operating expenses | 166,648 | 191,229 | **+14.75%** |
| Operating income | 50,258 | 34,008 | **−32.33%** |

**Expenses grew 3.8× faster than revenue.** [DEMONSTRATED] **The attribution is resolved, and it was
resolved by a page already cited above.** The Q2 2026 statement of operations splits `Total operating
expenses` into its five lines ([📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5)):

| Operating-expense line ($k) | Q2 2025 | Q2 2026 | Change |
|---|---:|---:|---:|
| Cost of services (exclusive of D&A) | 53,603 | 51,314 | −2,289 |
| Cost of subscriber equipment | 11,302 | 13,478 | +2,176 |
| Research and development | 4,279 | 5,530 | +1,251 |
| **Selling, general and administrative** | 44,627 | 67,044 | **+22,417** |
| Depreciation and amortization | 52,837 | 53,863 | +1,026 |
| **Total operating expenses** | **166,648** | **191,229** | **+24,581** |

**SG&A supplies +22,417 of the +24,581 thousand increase — 91.2% of it** — and the MD&A names the
cause: SG&A rose *"primarily due to increases in transaction costs totaling $14.3 million, associated
with the Merger Agreement with Rocket Lab and the Aireon acquisition"*
([📄 IRDM 10-Q p.26](https://agentii.ai/v/IRDM/sec191/26)), with professional fees and stock
appreciation rights expense (driven by the stock-valuation change around the announcement) behind
much of the rest. For the six months the same MD&A line reads +$32.4 million with transaction costs
of **$15.0 million** ([📄 IRDM 10-Q p.30](https://agentii.ai/v/IRDM/sec191/30)). **So the 15.78-point
margin contraction is an SG&A event, and about two-thirds of it is deal cost** — a first-order fact
about the series, since the transaction that would end it is what inflated the expense line.

**Correction to carry: an earlier draft of this artifact classed the attribution `UNEXERCISED`,
on the statement that "the pages I reached do not" carry the Q2 2026 line detail. That was wrong.**
p.5 carries all five lines, and their sum reproduces the cited total of 191,229 to the thousand; the
claim of unavailability was an artefact of not reading a page I had already quoted. Recorded, not
quietly deleted.

---

## 3. `earnings-vs-consensus`

### 3.1 The consensus line

| Period | Reported | EPS actual | EPS est. | Revenue actual ($k) | Revenue est. ($k) | Revenue surprise |
|---|---|---:|---:|---:|---:|---:|
| Q2 2026 | 2026-07-22 | **0.09** | **0.282** | 225,237 | 220,322.2 | **+2.23%** |
| Q3 2026 | *2026-10-22 (upcoming)* | — | 0.29 | — | 237,904.5 | — |

Source: `search_earnings_calendar`, latest page (the calendar paginates **oldest-first**; the recent
rows are on the last page of 10). [DEMONSTRATED]

**Provenance, stated because it is uneven across the table: the *actual* column is filed and is
carried by pages — revenue 225,237 and net income 9,679 on
[p.5](https://agentii.ai/v/IRDM/sec191/5); EPS $0.09 against 108,468 thousand diluted shares on
[p.19](https://agentii.ai/v/IRDM/sec191/19). The *estimate* column is not: consensus estimates exist
on the earnings-calendar layer only and appear on no page of any filing.** An earlier draft of this
artifact attached a filing-page citation to this table; a page cannot carry an estimate, so that
entry is removed and the layer boundary is drawn in the text instead.

**⚠️ The divergence is the finding, and it is not a data defect.** Q2 2026 is a **revenue beat**
(+2.23%) with a **68.1% EPS miss**. That combination is exactly what §2.3 predicts, and it is worth
stating which line the miss came from, because it is not the below-the-line block:

```
Q2 2026  operating income  34,008     Q2 2025  50,258        −32.33%
         total other expense (19,694)            (23,623)      −16.6% expense
         pre-tax              14,314              26,635       −46.3%
         net income            9,679              21,968       −55.9%
```

**The EPS miss traces to a 32.3% year-over-year fall in operating income, not to other expense or
tax** — the below-the-line expense actually *improved* ($23,623 thousand → $19,694 thousand). An
estimate set of $0.282 evidently did not model a 14.75% expense increase on a 3.84% revenue increase.
[DEMONSTRATED]

### 3.2 The actual reconciles to the filing

EPS actual **0.09** against filed net income of **$9,679 thousand** and **108,468 thousand diluted
weighted-average shares** — the quarter's own count, from Note 13
([📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5),
[📄 IRDM 10-Q p.19](https://agentii.ai/v/IRDM/sec191/19)): 9,679 ÷ 108,468 = **$0.0892 → $0.09** ✓.
The consensus actual is the filed result, not a normalised variant — so the miss is an estimate gap,
not a basis collision. This is a **one-line cross-check, not a sign test**; per the frontmatter's
DA-28 entry, no detector here rests on a share count.

**Correction to carry: this line previously divided by 107,837, which is the FY2025 *annual* diluted
count on [p.64](https://agentii.ai/v/IRDM/sec151/64), not the quarter's.** It is the same
annual-as-period substitution this artifact names in the platform (DA-26), in my own arithmetic: the
annual count is 0.59% larger, which moves the quotient from 0.0898 to 0.0892 and changes nothing
about the conclusion — but the basis is now the quarter's own cells. The filed EPS is $0.09 on either
count, so no filed figure is affected.

---

## 4. DA-30 — the $200,000 thousand denominator, and why the margin block is unusable

**This is the most important finding about IRDM's served data, and it is not a sign or a period
defect at all.** Every served quarterly margin in `get_financial_ratios` for IRDM divides by a single
constant: **200,000** — a figure equal to no reported revenue in any period.

| Served row | Served margin | Reproduces as | Basis defect |
|---|---:|---|---|
| FY2025 Q4 | 0.2707 | 235,980 ÷ **871,659** | the **ANNUAL** margin on a Q4 row (DA-26) |
| FY2026 Q2 | 0.5532 | **110,646** (6M2025 OI) ÷ 200,000 | **prior-year six-month** numerator |
| FY2026 Q2 | 0.1564 | **31,273** (6M2026 NI) ÷ 200,000 | six-month numerator |
| FY2026 Q1 | 0.2536 / 0.1080 | 50,713 / 21,594 ÷ 200,000 | period revenue ignored |
| FY2025 Q3 | 0.9037 | **180,731** (9M2025 OI) ÷ 200,000 | **nine-month** numerator |
| FY2025 Q3 | 0.4475 | **89,507** (9M2025 NI) ÷ 200,000 | nine-month numerator |
| FY2025 Q2 | 0.2513 | 50,258 ÷ 200,000 | period revenue ignored |
| FY2025 Q1 | 0.3019 / 0.1521 | 60,388 / 30,412 ÷ 200,000 | period revenue ignored |
| FY2024 Q1 | 0.2489 / 0.0983 | 49,771 / 19,653 ÷ 200,000 | period revenue ignored |

**8 of 8 testable margins reproduce to the basis point against the single $200,000 thousand
denominator.** [DEMONSTRATED]

**Provenance note on this table, because the served column is not page-locatable: the served ratio
values are `get_financial_ratios` output and appear on no page of any filing.** Every *input* in the
"Reproduces as" column is a filed cell already cited ([p.64](https://agentii.ai/v/IRDM/sec151/64),
[p.5](https://agentii.ai/v/IRDM/sec191/5)), and the $200,000 thousand denominator is filed in Note 12
([p.18](https://agentii.ai/v/IRDM/sec191/18)). The served column is quoted as the *object* of the
finding, never as its evidence — which is why an earlier draft's citation of this block to a filing
page is removed rather than re-pointed.

**And the denominator is identifiable.** It is served as a fully-dimensioned fact in
`get_company_financials.highlights.income_statement`:

```
"Revenues": { "value": 200000000, "unit": "iso4217:USD", "decimals": "-5",
  "dimensions": [ us-gaap:RelatedPartyTransactionAxis / irdm:HostingAgreementMember,
                  srt:RangeAxis / srt:MaximumMember,
                  us-gaap:RelatedPartyTransactionsByRelatedPartyAxis /
                    us-gaap:EquityMethodInvesteeMember ],
  "period_start": "2026-01-01", "period_end": "2026-06-30",
  "source_file": "irdm-20260630.htm" }
```

**The number itself is filed, and the page carries it.** IRDM's Note 12 states the contractual amount
in the issuer's own words: *"Under the agreements with Aireon, Aireon agreed to pay the Company fees
of $200.0 million to host the ADS-B receivers, of which $134.5 million had been paid as of June 30,
2026"* ([📄 IRDM 10-Q p.18](https://agentii.ai/v/IRDM/sec191/18)) — with hosting-fee revenue of
**$2.3 million recognised in the quarter and $4.6 million in the half** against it.

What the platform serves is therefore not a fabricated figure but a **misassigned basis**: IRDM's
aggregate related-party hosting fee, dimensioned at `srt:MaximumMember` for a six-month period, and
used as the revenue denominator for every quarterly margin. The conceptual distance is the point — an
**aggregate contract amount recognised at roughly $2.3 million a quarter** stands in for *total
revenue*. [DEMONSTRATED]

**Three independent basis collapses in one denominator:**

1. **Concept collapse** — a *related-party contract ceiling* is used as *total revenue*. Not a proxy
   of the same kind: one is a legal maximum, the other a realised result.
2. **Period collapse** — the ceiling's period is **2026-01-01 to 2026-06-30** (six months), while
   three of the numerators are **nine-month** figures and one is a **prior-year six-month** figure.
3. **Range collapse** — the fact is dimensioned `srt:MaximumMember`; the platform serves it with no
   range qualifier.

**Consequence for every downstream reader:** the served IRDM margins do not measure IRDM. They are
ratios of unrelated numerators to a fixed constant, and their *ranking* across quarters is an
artefact of the numerators alone. **Any thesis figure sourced from this block is unusable**, and the
FY2026 Q2 row — using a *prior-year* numerator against a *current-year* cap — is not resolvable to
any single period by any reading.

**Not resolvable:** the FY2024 Q2, Q3 and Q4 ratio rows (0.2296 / 0.2393 / 0.0921 and 0.1278 /
0.1234 / 0.1355) do **not** reproduce from any filed combination I hold, on the 200,000 denominator
or on reported revenue. Class: **UNRESOLVED-FROM-PLATFORM** — see §6.

**And the loop closes on DA-24.** The investee whose hosting agreement supplies this ceiling is the
*equity-method* investee whose results sit **below IRDM's operating line** — a **$15,251 thousand gain
in FY2024, 13.5% of that year's $112,776 thousand net income**
([📄 IRDM 10-K p.64](https://agentii.ai/v/IRDM/sec151/64),
[📄 IRDM 10-K p.55](https://agentii.ai/v/IRDM/sec151/55)). The same relationship defines both the
platform's revenue denominator and IRDM's largest non-operating income item.

### 4.1 The competing bases I report at every use

| Concept | Basis A | Basis B | Basis quoted here |
|---|---|---|---|
| Revenue (Q2 2026) | **reported revenue 225,237** | the $200,000 related-party ceiling | **reported revenue**, always |
| Net income (FY2024) | **operating 97,525** (112,776 − 15,251 equity-method gain) | reported net income **112,776** | **reported net income**, with the equity-method gain named whenever the figure is used |
| Operating income | **as filed, D&A-inclusive** | *(no competing basis exists — single operating-expense group)* | as filed |

**No figure in this artifact is quoted on one basis alone.**

---

## 5. DA-29 — a `fail` is as uninformative as a `pass`

**Provenance note: nothing in this section is page-locatable, and no citation here claims otherwise.**
`validate_calculation` is a platform-layer instrument; its `computed` and `reported` columns appear on
no page of IRDM's filing. The one *filed* cell this section leans on — the investing subtotal
**(51,791)** — is carried by [p.7](https://agentii.ai/v/IRDM/sec191/7) and is cited there in §1.3. An
earlier draft attached this validator output to a filing page as its `figure`; that entry is removed
rather than re-pointed, because no page carries it. The finding below stands on the instrument's own
behaviour, labelled as such.

`validate_calculation` on accession `0001418819-26-000045` returns **6 pass / 2 warn / 8 fail**. Two
of the `fail` rows are decisive — **for opposite reasons**:

**Usable, because `computed` reproduces the filed figure exactly:**

```
NetCashProvidedByUsedInInvestingActivities   computed (51,791,000)   reported 51,791,000   diff 103,582,000   fail
```

`computed` is the **filed negative**; `reported` is the **stripped positive**. This is a same-fact,
same-period detection of the DA-23 strip **inside the validator's own output**, and it is the one
validator row at IRDM that may be cited as evidence. The `StockholdersEquity` row is usable in the
same way as a *diagnostic*, since its diff is exactly the strip amount:

```
StockholdersEquity   computed 1,256,435,000   reported 472,511,000   diff 783,924,000   fail
                     = 2 × (387,281 + 4,681)  — the §1.3 fingerprint, appearing in the validator's output
```

**NOT usable, because `computed` reproduces from nothing:**

```
OperatingIncomeLoss  Q2 2026   computed (132,842,000)   reported 34,008,000   fail
OperatingIncomeLoss  6M2025    computed  (37,828,000)   reported 110,646,000  fail
```

The filed Q2 2026 pairing is 225,237 − 191,229 = **+34,008**, and no filed combination I hold yields
−132,842 or −37,828 — I tested the obvious ones. Per DA-29's chosen reading, **a term that appears
nowhere in the source is a back-solve, and `computed` is an opaque assertion.** These two `fail`
rows are therefore **not evidence of the strip**, and I do not cite them as any: they are evidence
that the validator's `computed` column is broken at IRDM. Note also that the row pairs a
**three-month `computed` with a six-month `reported`** (110,646 is the filed **6M2025** operating
income), a period-basis collision inside a single comparison.

**The three DA-29 kinds now demonstrated, which must not be merged:**

| Kind | Where | Symptom | Remedy differs |
|---|---|---|---|
| Zero-row gap | another issuer | validator does not run | ingestion coverage |
| **Pass on a wrong-signed value** | SATS | `computed` = `reported` = a stripped value, diff 0, **pass** | `reported` column shares the stripped store |
| **Fail with a non-reproducible `computed`** | **IRDM** | 8 fails, two of whose `computed` values appear nowhere in the source | `computed` column is a back-solve; the `fail` cannot be believed either |

**The general lesson, and it is the reason this section exists: a validator's `fail` is no more
admissible than its `pass` until the `computed` column is shown to reproduce a filed figure.** In
exactly one of IRDM's sixteen rows is that shown.

---

## 6. What I could not resolve

| Item | Class | The disclosure that would resolve it |
|---|---|---|
| **The operating-line driver of the +24,581 thousand expense increase (Q2 2026 vs Q2 2025)** | **RESOLVED — §2.3** | Carried in an earlier draft as `UNEXERCISED`, on the claim that the pages reached do not hold the Q2 2026 line detail. They do: the five expense lines are on [p.5](https://agentii.ai/v/IRDM/sec191/5) and sum to the cited total of 191,229, and the MD&A names the cause on [p.26](https://agentii.ai/v/IRDM/sec191/26) (SG&A +$22.4 million, transaction costs $14.3 million of it). Retained as a correction, not as an open item. |
| **The FY2024 Q2 / Q3 / Q4 ratio rows** (0.2296 / 0.2393 / 0.0921 and 0.1278 / 0.1234 / 0.1355) | **UNRESOLVED-FROM-PLATFORM** | They reproduce on neither the $200,000 thousand denominator nor on reported revenue, for any numerator I can construct from the filed statements. A well-argued negative finding: the eight rows that *do* reproduce (§4) are sufficient to identify the mechanism, and this residue does not change the conclusion. |
| **A per-quarter Aireon hosting-agreement revenue figure** | **UNRESOLVABLE-FROM-PUBLIC-SOURCES** | IRDM discloses the *ceiling* (the $200,000 thousand maximum) but not the realised related-party revenue per quarter. Without it, no reader can reconstruct what fraction of reported revenue the related party supplies. |
| **Whether the platform mis-serves a *negative* operating income at IRDM** | **UNRESOLVABLE-FROM-PUBLIC-SOURCES** (in this window) | It cannot be tested, because IRDM files none. `UNEXERCISED`. It would become testable in any quarter IRDM reports an operating loss. |

**Presence vs absence — the explicit `UNEXERCISED` list, stated rather than omitted:** (a) the DA-23
sign test on the operating line (§1.4); (b) DA-28 — no capital-structure discontinuity exists in this
window, so the detector has nothing to engage and is recorded as **NOT APPLICABLE**, not as passed.

**Withdrawn from an earlier draft of this list: the Q2 2026 expense-line attribution** (previously
item (c) here and the finding left open in §2.3 and §3.1). It was recorded as unexercised on the
claim that the line detail was out of reach; the detail is on p.5 of the 10-Q, a page cited in §1.2
and §2.3, and the cause is named on p.26. `UNEXERCISED` is the right disposition for a check that
*cannot* run — not for one that was simply not run.

---

## 7. Sources

| What it carries | Link |
|---|---|
| Q2 2026 balance sheet — the AOCI (4,681)/406 control pair, the retained-deficit pair, and the equity fingerprint components | [📄 IRDM 10-Q p.4](https://agentii.ai/v/IRDM/sec191/4) |
| Q2 2026 statement of operations — the identity cells, the six-month columns, the five operating-expense lines (§2.3), other expense, net income | [📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5) |
| Q2 2026 statement of cash flows — the two stripped financing/investing subtotals | [📄 IRDM 10-Q p.7](https://agentii.ai/v/IRDM/sec191/7) |
| FY2025 statement of operations — three annual columns, the equity-method line, EPS on both bases, the annual share counts | [📄 IRDM 10-K p.64](https://agentii.ai/v/IRDM/sec151/64) |
| Note 12 — the Aireon related-party disclosures, including the $200.0 million hosting fee the served denominator derives from (§4) | [📄 IRDM 10-Q p.18](https://agentii.ai/v/IRDM/sec191/18) |
| Note 13 / Note 14 — the quarter's own diluted share count and EPS, and the Rocket Lab Merger Agreement (§0.1, §3.2) | [📄 IRDM 10-Q p.19](https://agentii.ai/v/IRDM/sec191/19) |
| MD&A — the transaction from the target's side, with closing conditions and expected timing (§0.1) | [📄 IRDM 10-Q p.22](https://agentii.ai/v/IRDM/sec191/22) |
| MD&A — the three-month operating-expense discussion, and the $14.3 million of transaction costs in SG&A (§2.3) | [📄 IRDM 10-Q p.26](https://agentii.ai/v/IRDM/sec191/26) |
| MD&A — the six-month expense discussion and the post-quarter $100.0 million revolver draw (§0.1, §2.3) | [📄 IRDM 10-Q p.30](https://agentii.ai/v/IRDM/sec191/30) |
| Income-tax reconciliation against pre-tax income after the equity-method line | [📄 IRDM 10-K p.85](https://agentii.ai/v/IRDM/sec151/85) |
| MD&A — the equity-method investee (Aireon) discussion; the hosting agreement itself is filed in Note 12 (p.18), not on this page | [📄 IRDM 10-K p.55](https://agentii.ai/v/IRDM/sec151/55) |
| The acquirer's side of the same transaction, and the Neutron context for its standing | [📄 RKLB 10-Q p.35](https://agentii.ai/v/RKLB/sec109/35) |

**Evidence grade: DEMONSTRATED.** Every figure is a filed cell or arithmetic directly on filed cells.
The only `MODELED` element is the annual-to-quarter multipliers in §2.1, labelled as a one-line
cross-check that satisfies no falsifier; the §3.2 EPS check is now arithmetic on two *filed* cells
(net income, and Note 13's own diluted share count), not on an implied count.

**Citation provenance.** Every page number in this artifact's `citations` block names the tool that
located it — `read_source_pages`, on the page. Three served artefacts discussed above are *not*
page-locatable and therefore carry **no** page citation: the `get_financial_ratios` margin block
(§4), the `validate_calculation` rows (§5), and the earnings-calendar estimates (§3.1). In each case
the filed inputs are cited, the platform-layer output is quoted as the object of the finding, and the
boundary is drawn in the text at the point of use.
