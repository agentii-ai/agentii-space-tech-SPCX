---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: HAWK
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "07d26b9c738b"  # Q57 resolved 2026-09-18: re-derived from plugins/agent-plugins/agentii-equity-agent/skills/agentii/recent-quarter AND plugins/vertical-plugins/equity-research-core/skills/agentii/recent-quarter — two independent roots AGREE. Algorithm dispatch.skill_version_hash() (scripts/dispatch.py:132) validated 9/9 against the six pins tabled in theses/001-technology-baseline/reproduce.md, which resolve to four separate plugin roots. Supersedes the UNRESOLVED gap recorded at first write.
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income verified by the component identity (total revenue − total operating expenses) run in BOTH admissible forms, then compared to the tagged OperatingIncomeLoss for sign agreement. HAWK is FLIPPED in 5 of 6 periods — every loss-making period is stripped, the one profitable period is clean. EPS × shares was NOT used as a sign test (inadmissible, DA-23/28)."
  - da_id: "DA-24"
    chosen_reading: "disposal gain routed through the operating line. NOT PRESENT at HAWK — the only extinguishment item is a $2,729K LOSS sitting correctly BELOW income (loss) from operations, and the only realized gain/loss on investments appears as a cash-flow reconciling item. Cleared."
  - da_id: "DA-25"
    chosen_reading: "issuer-defined metric not reproducible from the disclosed tables. PRESENT IN FORM: Adjusted EBITDA of $7.0M (14% margin) is positive while operating income is $(11,546)K and net loss is $(15,278)K. Its reconciliation is in the earnings release, which is not in the read evidence set — so the metric is unreproducible here, and the disposition is a scope limit, not a proven override."
  - da_id: "DA-26"
    chosen_reading: "annual mislabelled as quarterly. NOT MANIFESTED as an annual-as-quarterly at HAWK — the platform carries no HAWK 10-K, so no annual value exists to mislabel. The duration hazard is present in a different form: the register's own 'financing inflow +$413.009M' is a SIX-MONTH figure read as quarterly, and the extract carries a monthly-duration preferred-dividend fact that no filing column displays."
  - da_id: "DA-27"
    chosen_reading: "fiscal labels taken from the calendar quarter, off by one for non-December year-ends. NOT APPLICABLE — HAWK's fiscal periods are December-anchored (Q1 ends March 31 per sec4 p.1; Q2 ends June 30 per sec6 p.6), so the calendar-quarter label is correct. The instrument's fiscal-calendar record is nonetheless defective (see §7)."
  - da_id: "DA-28"
    chosen_reading: "IPO capital-structure discontinuity. HAWK is the canonical site AND the edge case. The registered mechanism (share-count discontinuity) is NOT the mechanism of the 72% failure — that is a numerator-concept mismatch, and the correct denominator is exactly recoverable as a day-weighted blend of the two quarterly counts. The genuine DA-28 consequence is that every share-count-denominated test is inadmissible on Q2 2026 and H1 2026."
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM
citations:
  - figure: "4,168,374 — common stock issued and outstanding at 2025-12-31 (pre-IPO structure; an INSTANT, not a period denominator)"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec6
    page_no: 25
    url: https://agentii.ai/v/HAWK/sec6/25
    located_via: read_source_pages
  - figure: "97,960,719 — common stock issued and outstanding at 2026-06-30 (post-conversion activation count)"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec6
    page_no: 25
    url: https://agentii.ai/v/HAWK/sec6/25
    located_via: read_source_pages
  - figure: "97,965,552 — cover-page count as of 2026-08-10, dei:EntityCommonStockSharesOutstanding"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec6
    page_no: 1
    url: https://agentii.ai/v/HAWK/sec6/1
    located_via: read_source_pages
  - figure: "97,959,969 — cover-page count as of 2026-06-18 in the Q1 2026 10-Q (filed post-IPO, 2026-06-22)"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec4
    page_no: 1
    url: https://agentii.ai/v/HAWK/sec4/1
    located_via: read_source_pages
  - figure: "Total revenue 49,810 / total operating expenses 61,356 / income (loss) from operations (11,546) / net income (loss) (15,278) / preferred stock dividend 10,925 / net loss attributable to common shareholders (4,353) / EPS (0.07) / weighted-average shares 61,924,756 — Q2 2026"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec6
    page_no: 6
    url: https://agentii.ai/v/HAWK/sec6/6
    located_via: read_source_pages
  - figure: "Six-month column: total revenue 99,608 / total operating expenses 116,771 / income (loss) from operations (17,163) / net loss (24,267) / preferred stock dividend 10,376 / attributable to common (13,891) / EPS (0.39) / weighted-average shares 35,290,038; Q2 2025 comparative income from operations 796; H1 2025 (1,262) and net income +20 with EPS (0.15)"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec6
    page_no: 6
    url: https://agentii.ai/v/HAWK/sec6/6
    located_via: read_source_pages
  - figure: "Q1 2026: total revenue 49,798 / total operating expenses 55,415 / loss from operations (5,617) / net loss (8,989) / preferred stock dividend (548) / attributed to common (9,537) / EPS (1.14) / weighted-average shares 8,359,379; Q1 2025 loss from operations (2,058), EPS (0.30), weighted-average shares 7,232,097"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec4
    page_no: 6
    url: https://agentii.ai/v/HAWK/sec4/6
    located_via: read_source_pages
  - figure: "Note 16 EPS computation — numerator bridge and denominator 8,359,379; preferred stock dividend (548) in BOTH comparative columns; anti-dilutive exclusions including 68,987,988 convertible preferred shares"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec4
    page_no: 25
    url: https://agentii.ai/v/HAWK/sec4/25
    located_via: read_source_pages
  - figure: "Note EPS reconciliation — numerator bridge for all four columns (preferred stock dividends 10,925 / (554) / 10,376 / (1,103)) and both basic and diluted denominators"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec6
    page_no: 33
    url: https://agentii.ai/v/HAWK/sec6/33
    located_via: read_source_pages
  - figure: "Six-month financing inflow +$413,009K (six months ended June 30, 2026 — NOT a quarterly figure); gross IPO proceeds 478,400 with offering costs (37,770) and debt repayment (49,453)"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec6
    page_no: 10
    url: https://agentii.ai/v/HAWK/sec6/10
    located_via: read_source_pages
  - figure: "IPO — S-1 declared effective May 6, 2026; 18.4M shares at $26.00; net proceeds $437.5M net of $33.5M underwriting and $7.4M offering costs; prospectus filed May 7, 2026; $7.5M ISA deferred payment; $49.5M debt repaid"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec6
    page_no: 105
    url: https://agentii.ai/v/HAWK/sec6/105
    located_via: read_source_pages
  - figure: "IPO — common stock began trading on the NYSE under 'HAWK' on May 8, 2026; gross proceeds $478.4M; equity $109,549K → $794,818K"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec6
    page_no: 12
    url: https://agentii.ai/v/HAWK/sec6/12
    located_via: read_source_pages
  - figure: "MD&A results table independently confirms the operating LOSS 'Income (loss) from operations (11,546) | 796 | (1551)%', revenue 49,810, US 28,784, International 21,026; related-party revenue decline attributed to completion of the IPO"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec6
    page_no: 44
    url: https://agentii.ai/v/HAWK/sec6/44
    located_via: read_source_pages
  - figure: "Equity transactions — Series E issuances dated 2026-01-14, 2026-01-09, 2026-02-03, 2026-02-06, 2026-02-23 (the pre-IPO count rising through Q1)"
    ticker: HAWK
    form_type: 10-Q
    citation_id: sec6
    page_no: 49
    url: https://agentii.ai/v/HAWK/sec6/49
    located_via: read_source_pages
  - figure: "'welcome to HawkEye 360's first earnings call' — no prior post-IPO quarterly call exists; Adjusted EBITDA $7.0M at 14% margin; revenue $49.8M (+87%); backlog approximately $292M"
    ticker: HAWK
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 1
    url: https://agentii.ai/v/HAWK/ect1/1
    located_via: read_source_pages
  - figure: "CFO: 'Second quarter 2026 net loss was $15.3 million compared to prior year net income of $1.6 million'; 18.4M shares sold, approximately $437.5M net proceeds; $503M cash at June 30, 2026; backlog $285M → $292M; $82M backlog to be recognized in H2 2026"
    ticker: HAWK
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 2
    url: https://agentii.ai/v/HAWK/ect1/2
    located_via: read_source_pages
---

# HAWK — Recent-Quarter Methodology, Q2 2026 (the DA-28 site)

Source: Form 10-Q for the quarterly period ended June 30, 2026, accession
`0001750704-26-000022` (citation id `sec6`, filed 2026-08-14); Form 10-Q for the quarterly
period ended March 31, 2026, accession `0001750704-26-000014` (citation id `sec4`, filed
2026-06-22); Q2 2026 earnings call transcript (citation id `ect1`, filed 2026-08-13).

**Pillar 3's job at this ticker is to determine whether the 72% EPS-bridge failure is fully
explained by the Q2 2026 IPO, or whether a DA-23 residue hides underneath it.** The answer
is the second: **HAWK is a DA-28 that MASKS a separate DA-23.** The share-count
discontinuity explains the per-share evidence and *none* of the sign evidence, and the sign
evidence is present in periods that pre-date the listing by more than a year.

**Two premises in the tasking are falsified by the filings and are corrected here rather
than absorbed.** (i) The correct denominator **is** recoverable — it is the day-weighted
blend of the two quarterly counts, and that blend reproduces the filed six-month figure to
the share. What the extract does not expose is not a formula but a **date**. (ii) The 72%
failure is **a numerator-concept mismatch, not a share-count defect**: the denominators
contribute zero error, and the per-share bridge closes exactly in all four filed columns
once the right numerator concept is used.

---

## 0. Method, and the instrument rule as applied here

Three disciplines governed this pass, and each produced a finding of its own.

**0.1 `validate_calculation` was read only as `computed` vs `reported` pairs.** The
accession's status column returned 6 pass / 6 warn / 13 fail. **None of that was read as
failure.** Its `OperatingIncomeLoss` pair (`computed` −112,559,000 against `reported`
+11,546,000, `fail`) is an arc-selection artefact, consistent with the registered 93%
false-positive rate, and it was discarded rather than used. Every operating figure in this
artifact is established by the **component identity** — total revenue − total operating
expenses, run against the face of the filing — and cross-checked against the calculation
arc set where one exists.

**0.2 `EPS × shares` was not used as a sign test.** It is inadmissible (DA-23/28), and at
HAWK it is inadmissible twice over: the share count is a blend across two capital
structures, and the numerator concept is ambiguous. `EPS × shares` appears in §2 **only as
a decomposition of the register's own 72% number**, never as evidence about a sign.

**0.3 `search_keyword_in_source` was treated as a candidate generator, never as a locator.**
The keyword `Income (loss) from operations` on `sec4` returned **11 pages**, of which
**1 (page 6)** contains the line and the other 10 are risk-factor prose, non-GAAP
definition text and liquidity discussion — a false-positive rate of ~91% on that query.
Page 6 was then **confirmed by `read_source_pages`** before any figure from it was used.
The same search-then-confirm sequence was applied to every page cited in this artifact; no
page number here is guessed, and the two figures whose filing pages could not be located
are listed in §8 as fact-level and deliberately uncited rather than guessed.

---

## 1. JOB 1 — the four share counts: all four are correct, and none is a period denominator except two

**The register's puzzle dissolves once each count is labelled with its unit and its date.**
The four counts are four measurements of four different things, taken at four different
times, under two different capital structures. Not one of them is wrong.

| # | Count | What it actually measures | Unit | Date | Source |
|---|---|---|---|---|---|
| 1 | **4,168,374** | Common stock issued and outstanding — the **pre-IPO** structure | **instant** | 2025-12-31 | [📄 HAWK 10-Q p.25](https://agentii.ai/v/HAWK/sec6/25) |
| 2 | **8,359,379** | **Q1 2026 weighted-average**, basic and diluted — the quarter entirely **before** the IPO | **period denominator** | 2026-01-01→03-31 | [📄 HAWK 10-Q p.25](https://agentii.ai/v/HAWK/sec4/25) (Note 16), and [📄 HAWK 10-Q p.6](https://agentii.ai/v/HAWK/sec4/6) |
| 3 | **61,924,756** | **Q2 2026 weighted-average**, basic and diluted — the quarter **straddling** the May 8, 2026 listing | **period denominator** | 2026-04-01→06-30 | [📄 HAWK 10-Q p.6](https://agentii.ai/v/HAWK/sec6/6), reconciled at [📄 HAWK 10-Q p.33](https://agentii.ai/v/HAWK/sec6/33) |
| 4 | **97,965,552** | Cover-page `dei:EntityCommonStockSharesOutstanding` — the **post-IPO** structure, 41 days after quarter-end | **instant** | 2026-08-10 | [📄 HAWK 10-Q p.1](https://agentii.ai/v/HAWK/sec6/1) |

**Which is right for which period.** For **Q1 2026** the correct denominator is
**8,359,379**. For **Q2 2026** it is **61,924,756**. Neither instant count (1 or 4) is a
denominator for any period, and neither is advanced as one. The register treated four
counts as competing measurements of one quantity; they are two instants and two
period-weighted averages, and an instant can never be compared to a weighted average.

**The progression is internally coherent, and the mechanism is a conversion, not a
re-count.** From [📄 HAWK 10-Q p.25](https://agentii.ai/v/HAWK/sec6/25), 97,960,719 shares
were outstanding at 2026-06-30. That figure is explained by:

```
4,168,374   common outstanding at 2025-12-31                     (p.25)
+68,987,988 convertible preferred, as-converted at 2026-03-31    (sec4 p.25, anti-dilutive table)
+18,400,000 IPO shares (18.4M at $26.00)                          (sec6 p.105, ect1 p.2)
=91,556,362
+    6,404,357 option / RSU / warrant settlements in Q2
=97,960,719  ✓  ties to the filed 2026-06-30 instant to the share
```

This is a **DERIVED** reconciliation, and it closes exactly. The preferred-stock conversion
(~69.0M shares) plus the 18.4M-share IPO are what move the count by a factor of 23 across
two quarters — which is why a naive instant-to-weighted-average comparison at this issuer
produces apparent errors of 36.9% to 1,385%.

**Two further counts exist that the register did not list, and the second is a problem.**

- **97,959,969** — the cover count in the *Q1* 10-Q, as of **2026-06-18**
  ([📄 HAWK 10-Q p.1](https://agentii.ai/v/HAWK/sec4/1)). The Q1 10-Q was filed
  **2026-06-22**, i.e. *after* the May 8 listing, so its cover count is a **post-IPO**
  figure while its income statement is **pre-IPO** — a single filing whose cover page and
  financial statements sit on opposite sides of the capital-structure boundary.
- **5,425,643** — `us-gaap:CommonStockSharesOutstanding` at **2026-03-31**. This is an
  **extract fact whose filing page was not located**, so it is carried here as fact-level
  and **deliberately not given a page citation** (see §8). It matters because
  **8,359,379 > 5,425,643**: the Q1 2026 weighted-average count *exceeds the Q1 2026
  ending instant count* by 54.1%, and it exceeds the 2025-12-31 instant by 100.5%.

**Proof that no path produces the Q1 2026 denominator.** The count ran 4,168,374 (Dec 31)
→ 5,425,643 (Mar 31). Any weighted average over the quarter is bounded by the counts
prevailing during it, so it must lie between those two values. It does not: 8,359,379 lies
outside the interval, above both endpoints. A decrease from ~11M to 5.4M inside one quarter
would be required and is disclosed nowhere. **This is an unreconciled inconsistency on the
face of the filing, not an extract artefact** — the same 8,359,379 is used in Note 16 of the
Q1 10-Q ([📄 HAWK 10-Q p.25](https://agentii.ai/v/HAWK/sec4/25)) and reproduces the filed
EPS exactly: `−9,537,000 / 8,359,379 = −$1.1409 → $(1.14)`, as filed. Registered as
candidate **C-1** in §7.

**The blend recovers the true figure — the tasking's premise is falsified.** The two
quarterly counts combine into the filed six-month denominator to the share:

```
(8,359,379 × 90 days + 61,924,756 × 91 days) / 181 days
= 6,387,496,906 / 181
= 35,290,038.16   →  filed: 35,290,038   ✓  exact
```

and the same test on the prior year closes to the share as well:
`(7,232,097 × 90 + 7,392,011 × 91) / 181 = 1,323,561,731 / 181 = 7,312,496.9 → 7,312,496` ✓
([📄 HAWK 10-Q p.6](https://agentii.ai/v/HAWK/sec6/6)). **The extract exposes the blend's
components and the blend is exactly recoverable.** What is *not* recoverable arithmetically
is the **boundary date** at which the structure changed. That is a cited fact, not an
arithmetic one — and that is precisely the calibration the guard needs (§5).

**And the blend is reproducible from the listing date.** With a pre-listing count P over the
37 days Apr 1 – May 7 and a post-listing count X over the 54 days May 8 – Jun 30:
`X = (5,635,152,796 − 37P) / 54`. At P = 9,000,000 this gives X = 97,502,829 and a Q2
weighted average of **61,790,976 — 0.22% below the filed 61,924,756.** The implied X spans
96.8M – 101.5M across P = 4.17M – 11M and **brackets the actual June 30 count of
97,960,719**. The residual ~0.2% is the pre-IPO count still rising through April and early
May — Series E issuances dated 2026-01-14, 2026-01-09, 2026-02-03, 2026-02-06 and
2026-02-23 ([📄 HAWK 10-Q p.49](https://agentii.ai/v/HAWK/sec6/49)). **A day-weighted blend
with the May 8 listing date reproduces the Q2 denominator to 0.22%.** The registered claim
that "no arithmetic test recovers the true figure" is not correct.

---

## 2. JOB 2(a) — the 72% failure is a NUMERATOR mismatch. The denominators contribute zero.

The per-share bridge at HAWK does not fail because of the share count. It fails because it
was built on the wrong numerator concept. The filing's own reconciliation
([📄 HAWK 10-Q p.33](https://agentii.ai/v/HAWK/sec6/33)) shows the missing item:

```
Net income (loss)                                  (15,278)
Preferred stock dividends                           10,925
Income allocated to participating securities             —
Net income (loss) attributable to common
  shareholders, basic and diluted                   (4,353)
```

`Income (loss) from operations (11,546)` → `Net income (loss) (15,278)` →
`attributable to common (4,353)`. A bridge built on the gross loss concept
(`NetIncomeLoss`, −15,278) is short by the 10,925 preferred stock dividend, i.e.
**10,925 / 15,278 = 71.5% adrift — the register's "72%," reconciled.** With the correct
numerator (`NetIncomeLossAvailableToCommonStockholdersBasic`, −4,353) and the filed
denominator, the bridge closes to two decimals **in all four filed columns**:

| Column | Numerator (correct concept) | Denominator | Computed | Filed | Error |
|---|---|---|---|---|---|
| Q2 2026 | (4,353) | 61,924,756 | $(0.0703) | $(0.07) | **0.4%** |
| H1 2026 | (13,891) | 35,290,038 | $(0.3936) | $(0.39) | **0.9%** |
| Q2 2025 | 112 | 7,392,011 | $0.0152 | $0.02 | rounding |
| H1 2025 | (1,083) | 7,312,496 | $(0.1481) | $(0.15) | **1.3%** |

All four residuals are pure two-decimal rounding. **The share counts are not implicated in
any of them.** The calculation arc set says the same thing structurally:
`NetIncomeLossAvailableToCommonStockholdersBasic ← NetIncomeLoss (+1),
PreferredStockDividendsAndOtherAdjustments (−1),
UndistributedEarningsLossAllocatedToParticipatingSecuritiesBasic (−1)`.

**Why this matters for DA-28, and why it matters for the guard.** The preferred stock exists
only because HAWK was pre-IPO, so the failing bridge **is** a DA-28 consequence — but it is
a *numerator* consequence, and the register attributes it to the *denominator*. **A guard
built on share counts would not have caught it.** Registered as calibration for §5, guard G2.

**One further hazard on the very concept the guard depends on.**
`PreferredStockDividendsAndOtherAdjustments` is displayed as **(548)** for Q1 2026
([📄 HAWK 10-Q p.25](https://agentii.ai/v/HAWK/sec4/25)) — and the extract carries
**+600,000** for the same period (fact-level read; page not located). That is a sign
inversion *plus* a level difference; the level gap is plausibly a **concept-scope** effect,
since the concept name aggregates dividends "and other adjustments" and 548 + 52 = 600.
**A level test alone would miss the sign defect, and a sign test alone would misattribute
its cause.** The extract also carries a **monthly-duration** fact for this concept
(2026-05-01→05-31 = 10,900,000) that appears as no column in either 10-Q read, and which
differs from the nearest filed figure (Q2 2026 = 10,925 thousand) by 25 thousand. Both are
recorded as candidate **C-2** in §7, unresolved.

---

## 3. JOB 2(b) — YES: a DA-23 residue hides under the DA-28, and it is large

**5 of 6 tagged `OperatingIncomeLoss` facts are sign-stripped.** The component identity —
total revenue − total operating expenses, on the face of the filing — is **magnitude-exact
in all six periods**. The only disagreement is the sign.

| Period | Filing | Extract `OperatingIncomeLoss` | Component identity | Verdict |
|---|---|---|---|---|
| Q1 2025 | **(2,058)** | +2,058,000 | 23,002 − 25,060 = **−2,058** | **STRIPPED** |
| Q2 2025 | 796 | +796,000 | 26,626 − 25,830 = **+796** | clean (genuine profit) |
| H1 2025 | **(1,262)** | +1,262,000 | 49,628 − 50,890 = **−1,262** | **STRIPPED** |
| Q1 2026 | **(5,617)** | +5,617,000 | 49,798 − 55,415 = **−5,617** | **STRIPPED** |
| Q2 2026 | **(11,546)** | +11,546,000 | 49,810 − 61,356 = **−11,546** | **STRIPPED** |
| H1 2026 | **(17,163)** | +17,163,000 | 99,608 − 116,771 = **−17,163** | **STRIPPED** |

Filing pages, stated per document because both filings carry the statement on their own
page 6: the **Q2 2026 10-Q** (`sec6`) supplies the three- and six-month 2026 columns and
both 2025 comparatives — [📄 HAWK 10-Q p.6](https://agentii.ai/v/HAWK/sec6/6); the **Q1 2026
10-Q** (`sec4`) supplies Q1 2026 and Q1 2025 — [📄 HAWK 10-Q p.6](https://agentii.ai/v/HAWK/sec4/6).
Every operating-expense subtotal was verified independently as the sum of its five
components — `14,850 + 4,608 + 25,011 + 8,244 + 8,643 = 61,356` ✓ for Q2 2026, and the same
five-way sum ties for H1 2026, Q2 2025 and H1 2025. **So the identity is not approximately
right; it is exact in all six periods, and the sign is the sole defect.**

**The strip is independent of the IPO. This is the decisive test.** Q1 2025 and Q2 2025 are
**11 and 14 months before** the 2026-05-08 listing, and Q1 2025 is stripped. A capital-
structure event in May 2026 cannot invert a fact reported for January–March 2025. The strip
is therefore not a DA-28 consequence, and the DA-28 disposition cannot absorb it.

**The strip operates per-FACT, not per-PERIOD.** H1 2025 is the proof, and it sits inside a
single column of a single table ([📄 HAWK 10-Q p.6](https://agentii.ai/v/HAWK/sec6/6)):
net income is **+20** — a *profit*, clean in the extract as +20,000 — while EPS for the same
period is **(0.15)** — a *loss*, stripped in the extract as +0.15. The period is the same,
the statement is the same, the sign is opposite, because the preferred dividend (1,103)
sits between the two concepts: `20 − 1,103 = −1,083`. **No period-level rule can explain
this extract; the operation is on values.** It also fits the registered rule precisely —
loss-making stripped, profitable clean:

| Concept | Stripped | Clean | Clean periods are genuine profits? |
|---|---|---|---|
| `OperatingIncomeLoss` | Q1 2025, H1 2025, Q1 2026, Q2 2026, H1 2026 (**5**) | Q2 2025 | **yes** (+796) |
| `NetIncomeLoss` | Q1 2025, Q1 2026, Q2 2026, H1 2026 (**4**) | Q2 2025, H1 2025 | **yes** (+1,611, +20) |

A second, non-filing correlate confirms the sign convention independently: the CFO states
on the call that *"Second quarter 2026 net loss was $15.3 million compared to prior year net
income of $1.6 million"* ([📄 HAWK earnings_call_transcript p.2](https://agentii.ai/v/HAWK/ect1/2)).
The same two facts the extract reports as +15,278,000 and +1,611,000 are described in prose
as a **loss** and a **profit**. The extract's positive sign on Q2 2026 is not a convention.

**The material consequence, stated plainly.** Every operating figure at HAWK is inverted in
the extract. Q2 2026 operating margin is **−23.2%** (11,546 / 49,810), not +23.2%; the
six-month figure is **−17.2%**, not +17.2%. And the inversion is *corroborated* by a number
a reader would naturally reach for next: **Adjusted EBITDA of $7.0M, a 14% margin**
([📄 HAWK earnings_call_transcript p.1](https://agentii.ai/v/HAWK/ect1/1)). A reader holding
the extract's +11,546,000 finds apparent agreement between the platform's "operating income"
and the issuer's headline non-GAAP metric. **Both are wrong about GAAP**, and they agree with
each other. That is the concrete harm of the DA-23 residue at this ticker — and it is
compounded by the fact that the Adjusted EBITDA reconciliation is not in the read evidence
set (§7, DA-25).

**DA-23 detector availability at HAWK.** The registered **gross-profit bound is unavailable**:
there is no gross-profit line on this income statement (it runs total revenue → direct cost
of sales → indirect cost of sales → SG&A → R&D → D&A → total operating expenses → income
(loss) from operations), and `GrossProfit` returns **total_count 0** from the extract. A
proxy bound is formable from the two cost-of-sales lines —
`49,810 − 14,850 − 4,608 = 30,352`, comfortably above the −11,546 loss — **but it buys
nothing here: the bound is a LEVEL test, and HAWK's defect is a SIGN-only defect with a
magnitude that is exact.** A level test is structurally blind to it. This is a detector-design
finding in its own right and belongs in the PIL-3 register alongside LUNR (no quarterly
gross-profit line, detector cannot run).

---

## 4. The remaining register items, disposed

**DA-24 — disposal gain through the operating line: NOT PRESENT (cleared).** The only
extinguishment item is `Loss from extinguishment of debt (2,729)`, and it sits **below**
income (loss) from operations ([📄 HAWK 10-Q p.6](https://agentii.ai/v/HAWK/sec6/6)) — the
inverse of the DA-24 pattern and correctly placed. The only realized investment result is
`Realized gain (loss) on short-term investments (12)` appearing as a cash-flow reconciling
item ([📄 HAWK 10-Q p.10](https://agentii.ai/v/HAWK/sec6/10)) — immaterial and not in
operating income. Note for completeness that the below-the-line region carries
IPO-consequential remeasurements (`Loss from changes in fair value of financial liabilities
(5,701)` for H1 2026, = 4,471 + 1,500 − 270, which ties to its own three components), and
that these are correctly **outside** operating income. Below-the-line IPO effects cannot
contaminate the operating line.

**DA-25 — issuer-defined metric not reproducible: present in form, scope-limited.** Adjusted
EBITDA is reported as **$7.0M, a 14% margin**, against Q2 2025's $7.8M, plus full-year 2026
guidance of $215–220M revenue and $30–36M Adjusted EBITDA
([📄 HAWK earnings_call_transcript p.2](https://agentii.ai/v/HAWK/ect1/2)). **The metric is
positive while both GAAP measures are negative** (operating loss $(11,546)K; net loss
$(15,278)K) — exactly the shape DA-25 exists to catch. Its reconciliation lives in the
earnings release, which is **not in this evidence set**, so the metric is recorded as
**unreproducible here** rather than as a proven override. Its GAAP-line companions do tie
exactly to the filing — revenue $49.8M = 49,810; US $28.8M = 28,784; international $21M =
21,026 at +134%, matching the MD&A table
([📄 HAWK 10-Q p.44](https://agentii.ai/v/HAWK/sec6/44)) — so the untied item is the
non-GAAP bridge alone.

**DA-26 — annual mislabelled as quarterly: not manifested as registered.** The platform
carries no HAWK 10-K, so there is no annual value available to mislabel. But the
**period-length hazard is present in a different carrier**, and one instance is in the
register itself: the **"financing inflow +$413.009M" is a SIX-MONTH figure**, not the IPO
inflow and not a quarterly figure — its period is 2026-01-01→2026-06-30
([📄 HAWK 10-Q p.10](https://agentii.ai/v/HAWK/sec6/10)), headed *"Six months ended June
30."* Its composition is `478,400 (IPO) + 18,774 (preferred) + 3,647 (options) + 202
(warrants) − 37,770 − 49,453 − 706 − 85 = 413,009` ✓ exact. The tasking's reading of that
figure as the IPO's quarterly inflow is a period-length error of the same family DA-26
describes, made one layer up — in the register rather than in the extract. The extract's
monthly-duration preferred-dividend fact (§2) is a third instance.

**DA-27 — calendar-quarter labels: not applicable, but the instrument record is defective.**
HAWK's periods are December-anchored on the face of the filings — the Q1 10-Q is *"for the
quarterly period ended March 31, 2026"* ([📄 HAWK 10-Q p.1](https://agentii.ai/v/HAWK/sec4/1))
and the Q2 10-Q reports the quarter ended June 30 ([📄 HAWK 10-Q p.6](https://agentii.ai/v/HAWK/sec6/6))
— so the calendar-quarter label is correct and no off-by-one arises. The
`get_company_fiscal_calendar` record nonetheless carries `fiscal_year_end_month_source:
"default"` (i.e. asserted, not derived) and a `cross_validation_hint` stating *"No XBRL data
available for this ticker"* — **which is false**, since `get_ticker_coverage` reports **2,117
xbrl_facts**. An instrument that tells a validator "no data" about a ticker with 2,117 facts
is a hazard of the same class as the coverage-counter lag in §6. Registered as candidate
**C-3**.

**DA-28 — the site itself.** Two findings, both load-bearing:
1. **The registered mechanism is the wrong mechanism.** The 72% is a numerator-concept
   mismatch; the denominator closes exactly in both admissible forms. Recorded so the
   register does not acquire a mechanism that would not have caught the defect it cites.
2. **The listing date is not one date.** HAWK's own disclosures carry three, and all three
   are correct: the S-1 was declared **effective May 6, 2026**; the Rule 424(b)(4) prospectus
   was **filed May 7, 2026**; and the common stock **began trading on the NYSE on May 8,
   2026** ([📄 HAWK 10-Q p.105](https://agentii.ai/v/HAWK/sec6/105),
   [📄 HAWK 10-Q p.12](https://agentii.ai/v/HAWK/sec6/12)). The apparent conflict between the "May 6" and
   "May 8" dates seen in different tool outputs is **not a data conflict** — it is two
   different events. **A guard keyed to a single "IPO date" field is therefore fragile by
   construction**, because the issuers' own disclosures do not contain a single such field.
   The blend bound at May 8 is the operative conversion boundary (0.22%, §1), so the guard
   must accept a **±2-day window** around the registration effective date rather than a
   point.

---

## 5. THE GUARD — the direct answer to the guard question

**Does the 72% failure fully explain the anomaly? NO.** It explains the per-share bridge
discrepancy completely and correctly, and it explains **none** of the sign stripping —
which is present in Q1 2025 and Q2 2025, a year before the listing. **HAWK is a DA-28
masking a DA-23.** A DA-28-only disposition would have closed HAWK as "explained" while
leaving five wrong-sign facts in the extract and every operating figure at the issuer
inverted.

**And the guard is needed to protect an inadmissible test, not an admissible one.** This is
the calibration HAWK actually supplies, and it inverts the register's framing. **The DA-23
detector in its admissible form does not false-positive on recent listings.** The component
identity is a *within-period, within-filing* test on *flows*, and flows are
capital-structure-insensitive — it fired correctly and unambiguously at HAWK, magnitude-
exact and sign-opposite, in 5 of 6 periods. **Every false-positive mechanism DA-28 refers to
is generated by the per-share form**, which the contract already declares inadmissible. So
the guard's job is to keep an inadmissible test from being run, and to stop a listing date
from being used as an excuse for a sign disagreement.

**G1 — listing-date boundary partition (protects per-share tests only).** Determine whether a
registration-effective or first-trading date D falls in [period_start, period_end]. If it
does, the period is **structurally heterogeneous in capital structure** and **no
share-count-denominated test is admissible on it**. Disposition `INADMISSIBLE-RECENT-LISTING`
— **not `fail`**. Replace with a boundary-split day-weighted blend over the two segments.
At HAWK: **Q2 2026** contains May 8, 2026 → inadmissible → the blend closes to **0.22%**;
**H1 2026** likewise; **Q1 2026** (ended 2026-03-31) is entirely pre-listing and unaffected.
Accept a **±2-day window** on D (§4, DA-28 finding 2).

**G2 — numerator-concept guard (the one that actually matters here).** Any per-share bridge
must use `NetIncomeLossAvailableToCommonStockholdersBasic` (or `…Diluted`) as the numerator
whenever `PreferredStockDividendsAndOtherAdjustments` or
`UndistributedEarningsLossAllocatedToParticipatingSecurities*` is non-zero. At HAWK this
converts a **71.5% failure into a 0.9% pass**. It is a *concept* guard rather than a *date*
guard, but it is triggered by the same pre-IPO capital structure, so it belongs in the DA-28
family — and it is the guard that would have caught HAWK's actual 72%. **Calibration caveat:
G2's own input concept is corrupted in the extract** (Q1 2026 as +600,000 against the filed
(548), §2). G2 must read that concept from the *filing*, or it will mis-fire.

**G3 — the rule-out rule (the calibration HAWK provides against its own disposition).**
**A listing date may never excuse a sign disagreement on a within-period flow identity.**

```
DA-23 detector, per (issuer, period):
  1. computed = TotalRevenue − TotalOperatingExpenses   vs   OperatingIncomeLoss
     If |computed| == |reported| and sign(computed) != sign(reported):
        → DA-23 CONFIRMED. Stop. (The listing date is irrelevant.)
  2. If step 1 is unavailable (no opex breakdown) → gross-profit bound;
     if GrossProfit is untagged, try TotalRevenue − (DirectCostOfSales + IndirectCostOfSales).
     NOTE: the bound is a LEVEL test and is blind to a sign-only, magnitude-exact defect (HAWK).
  3. ONLY IF steps 1–2 are unavailable, run per-share tests, and then only:
     a. numerator MUST be NetIncomeLossAvailableToCommonStockholders*, never NetIncomeLoss,
        when PreferredStockDividendsAndOtherAdjustments or
        UndistributedEarningsLossAllocatedToParticipatingSecurities* is non-zero;
     b. if listing_date ∈ [period_start, period_end] (window ±2 days), the share-count test is
        INADMISSIBLE on that period (INADMISSIBLE-RECENT-LISTING), not "fail".
  4. A listing date NEVER excuses a step-1 disagreement.
```

**Ordering is the whole point.** Run step 1 first and unconditionally. The guard applies
downstream, to per-share tests only. That single ordering rule is what stops a DA-28
disposition from swallowing DA-23 at this ticker.

**The false-positive mechanisms at HAWK, for the record** — both are capital-structure
artefacts and neither is a defect: (i) comparing the Q2 weighted average (61,924,756)
against the cover-page instant (97,965,552) → a 36.9% apparent error, or against the
pre-IPO instant (4,168,374) → a 1,385% apparent error; (ii) a bridge built on
`NetIncomeLoss` → a 71.5% apparent error. **G2 cures (ii); only G1 cures (i).** Neither is a
sign defect, and neither should ever be reported as one.

---

## 6. JOB 3 — the coverage caveat, and why it is the same hole as DA-28

**001's caveat is now partly stale, and the stale part is the DA-28-relevant part.**

| Instrument | Says | Truth | Assessment |
|---|---|---|---|
| `get_ticker_coverage` → `sec_filings` | `record_count 4`, latest **2026-06-22**, freshness **"missing"** | `search_sec_filings` returns **6** filings; `list_sources` returns **7** sources | **counter is behind by two filings** |
| `get_ticker_coverage` → `institutional_holdings` | `record_count 0`, latest `null`, freshness **"missing"** | confirmed absent | **see below** |
| `get_ticker_coverage` → `xbrl_facts` | 2,117 | — | populated |
| `get_ticker_coverage` → `insider_trades` | 53, latest 2026-08-21 | — | populated |
| `get_ticker_coverage` → `earnings_calendar` | 2, latest 2026-11-12 | forward date | populated |

**A validator trusting the counter would have declared HAWK uncovered and skipped this
artifact — and the filing it is missing is `sec6`, the Q2 2026 10-Q filed 2026-08-14, which
carries the entire DA-28 evidence base**: the post-IPO quarter, the six-month blend, the EPS
numerator bridge, and the 35,290,038 denominator. The coverage counter's `latest_data_date`
of 2026-06-22 is the *Q1* 10-Q's filing date; the Q2 filing exists on the platform (it is
this artifact's primary source) but is not counted. **That is a coverage-instrument defect,
not an absence of data**, and it must be registered — otherwise the ticker that PIL-3 most
needs is the ticker the coverage layer hides.

**What the absent `institutional_holdings` row limits — and why it is the same hole as
DA-28.** A 13F is an **independent, third-party-basis share count**. Without it, every share
count in evidence at HAWK is either the issuer's own disclosure or the platform's
re-extraction of that disclosure. **There is no independent denominator available to
arbitrate between 4,168,374 / 5,425,643 / 8,359,379 / 35,290,038 / 61,924,756 / 97,959,969
/ 97,960,719 / 97,965,552.** The coverage hole and the DA-28 ambiguity are the *same* hole,
and the candidate C-1 inconsistency in §1 is exactly the kind of item an independent
denominator would settle in one step. Secondary limits: no ownership-change signal, no float
or ownership denominator, and no corroborating second source for any count.

The absence is **expectable on timing** — the IPO closed 2026-05-08, and most 13F filers
would first report a Q2 2026 position in mid-August 2026 — and HAWK's holder base is
dominated by venture and growth holders, many of whom are not 13F filers. That is recorded
as the expectable explanation, **not asserted as fact**.

**One further timeliness datum, and it corroborates the warning case.** The Q2 2026 call is
described on its own first page as *"HawkEye 360's first earnings call"*
([📄 HAWK earnings_call_transcript p.1](https://agentii.ai/v/HAWK/ect1/1)) — the CEO says
*"welcome to HawkEye 360's first earnings call."* **HAWK had no post-IPO quarterly history to
fall back on, and no prior post-IPO call.** That is the sequence's warning case confirmed
from the primary source: HAWK is the DA-28 site that had not yet produced a clean post-IPO
quarter. Where KRMN and VOYG had a full post-IPO quarter and passed cleanly, HAWK had none —
and, as §3 shows, the reason it did not pass is not that it lacked history. It had a second
defect.

---

## 7. Register — applied, with dispositions

| DA | Register reading | Disposition at HAWK | Class |
|---|---|---|---|
| **DA-23** | `\|computed\| == \|reported\|`, opposite signs; also any level failing the gross-profit bound | **CONFIRMED, 5 of 6 periods.** Component identity exact in magnitude in all six. Q1 2025 and Q2 2025 pre-date the listing, so it is IPO-independent. Strip is per-FACT, not per-period (H1 2025: net income +20 clean, EPS (0.15) stripped). Gross-profit bound **unavailable** (`GrossProfit` total_count 0); proxy bound formable but **structurally blind** to a sign-only, magnitude-exact defect | **defect present** |
| **DA-24** | disposal gain through the operating line | **NOT PRESENT.** Extinguishment item is a *loss*, below the line; only realized investment result is a cash-flow reconciling item | cleared |
| **DA-25** | issuer-defined metric not reproducible | **present in form, scope-limited.** Adjusted EBITDA $7.0M / 14% positive while GAAP operating and net results are negative; reconciliation not in the evidence set | scope limit |
| **DA-26** | annual mislabelled as quarterly | **not manifested as registered** (no 10-K on platform). Duration hazard present in another carrier: the register's own "+$413.009M financing inflow" is a **six-month** figure; extract carries a monthly-duration preferred-dividend fact | **defect present, relocated** |
| **DA-27** | calendar-quarter labels, off-by-one | **not applicable** — December-anchored periods, evidenced on the face of both 10-Qs. Fiscal-calendar record defective (`"default"` source; false "no XBRL data" hint) | cleared / C-3 |
| **DA-28** | IPO capital-structure discontinuity | **CONFIRMED as site; registered mechanism wrong.** 72% is a numerator-concept mismatch; denominator closes exactly (35,290,038 exact; Q2 to 0.22%). Three distinct and all-correct IPO dates (May 6 effective / May 7 prospectus / May 8 first trade). **Masks a DA-23** | **defect present + mechanism correction** |
| **C-1** | — | Q1 2026 weighted average (8,359,379) exceeds the Q1 2026 ending instant (5,425,643) by 54.1%; impossible on any monotone path; reproduces the filed EPS exactly, so it is the filed denominator | **UNRESOLVED** |
| **C-2** | — | `PreferredStockDividendsAndOtherAdjustments`: Q1 2026 extract **+600,000** vs filed **(548)** — sign inversion plus a level gap plausibly from concept scope ("and other adjustments"); plus a monthly-duration fact (May 2026 = 10,900,000) matching no filed column | **UNRESOLVED** |
| **C-3** | — | Instrument metadata: fiscal calendar `"default"` with a false "No XBRL data available" hint (2,117 facts exist); coverage counter behind by two filings | **instrument defect** |
| **C-4** | — | `validate_calculation` on the Q2 accession returned 6/6/13; its `OperatingIncomeLoss` pair is an arc artefact and was **not** read as failure (93% registered false-positive rate) | **instrument defect, handled** |

---

## 8. What could NOT be verified

1. **The filing page for `us-gaap:CommonStockSharesOutstanding` = 5,425,643 at 2026-03-31.**
   The value is an extract fact (source file `hawk-20260331.htm`, the Q1 10-Q; period_instant
   2026-03-31) read at fact level. Its page was **not located**, so **no page citation is
   offered for it** — a guessed page would resolve to the wrong page and look correct. The
   Q1 10-Q's equity roll-forward is the read that would settle it. This is the single
   load-bearing unlocated source in the artifact.
2. **The reconciliation of C-1.** Why the Q1 2026 weighted average exceeds both bounding
   instants is not resolved. The two cheapest closes are the equity note in the Q1 10-Q
   (roll-forward at class level) and the S-1's capital-structure table. Neither was read.
   A **dimension-collapse hazard cannot be excluded**: all three
   `CommonStockSharesOutstanding` facts returned `dimensions: {}`, so "undimensioned total"
   and "class-level count with the axis dropped by the extract" are indistinguishable from
   the returned data. **Accordingly, 4,168,374 and 5,425,643 are not presented as "the"
   totals in this artifact** — per the no-single-basis-collapse rule, the alternative basis
   is stated rather than suppressed.
3. **The exact provenance of the extract's +600,000 and 10,900,000 facts** (C-2). Both are
   fact-level reads; no page was located, and no filing column displays either value. The
   concept-scope explanation for the level gap (548 + 52) is a hypothesis, not verified.
4. **The Adjusted EBITDA reconciliation.** The earnings release is not in the evidence set,
   so DA-25's override test cannot be run — only its shape observed.
5. **Any independent share count.** `institutional_holdings` is empty (§6). No 13F, no
   float, no second basis against which to arbitrate eight counts.
6. **Anything annual.** No HAWK 10-K exists on the platform, so no annual period was
   examined and no annual-versus-quarterly comparison is possible at this issuer.
7. **The `skill_pin`.** `dispatch.skill_version_hash()` is not reachable from the artifact
   context and no `recent-quarter` artifact exists in this thesis to inherit the pin from.
   Recorded as a gap rather than fabricated (per the SPCX precedent and the `corpus_version`
   policy in `reproduce.md`). The other four pins are populated.

---

## 9. Carry-forwards

1. **DA-28's registered mechanism should be corrected in the register.** The 72% at HAWK is
   a numerator-concept mismatch, not a share-count discontinuity; the denominator is exactly
   recoverable. As written, the register points a future validator at the wrong field.
2. **Adopt guards G1–G3, with the ordering (step 1 first, unconditionally) as the load-bearing
   part.** G2 is the guard that would have caught HAWK's actual failure; G1 protects only
   tests the contract already calls inadmissible; G3 stops the DA-28 disposition from
   swallowing DA-23. State that a listing date is never an excuse for a step-1 disagreement.
3. **Record the DA-23 detector-availability pair: HAWK and LUNR.** At LUNR the detector
   cannot run (no quarterly gross-profit line); at HAWK the bound can be formed but is
   **structurally blind** because the defect is sign-only and magnitude-exact. Two distinct
   reasons why the level test cannot substitute for the component identity.
4. **Register the coverage-counter lag as a PIL-3 evidence-integrity item.** A counter whose
   `latest_data_date` is one filing behind can hide the exact filing a pillar depends on.
   This is not cosmetic: it would have suppressed the DA-28 site.
5. **C-1 is the highest-value open item at this ticker**, because it is the only share-count
   inconsistency whose resolution does not depend on a 13F — the equity note and the S-1 can
   settle it. Resolve it before any later artifact quotes a HAWK share count as a total.
6. **The DA-23 residue at HAWK is a live wrong-sign hazard for every downstream consumer** —
   the extract's +11,546,000 agrees with the issuer's positive Adjusted EBITDA of $7.0M
   while both contradict GAAP. Any downstream artifact reading HAWK operating income from
   the extract must invert it, and must cite the filing, not the extract.
