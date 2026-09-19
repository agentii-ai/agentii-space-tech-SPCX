---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: BA
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
    chosen_reading: "EXHIBITED at BA, twice, both periods now CONFIRMED by detector 1 (component identity) in-line. The register's `−5,761 → +5,761` is Q3 2024; the register's open candidate is Q3 2025, filed (4,781) vs platform +4,781,000,000. The mechanism is refined: the platform stores |x| (absolute value), NOT an inversion — proven by two positive controls where the platform's value is exactly correct (2025 Q1 +461M and FY2025 +4,281M). `EPS × shares` was NOT used, and is recorded as inadmissible."
  - da_id: "DA-24"
    chosen_reading: "EXHIBITED, and materially so — but in the quarter AFTER the flip window, not inside it. BA's income statement routes disposal gains through the operating subtotal by construction (`Gain on dispositions, net` sits immediately above `Earnings/(loss) from operations`). The Digital Aviation Solutions / Thoma Bravo sale closed 2025-10-31 and booked a $9,566M gain into that line, inside FY2025 operating income. In the two flip periods the disposal effect was nil (Q3 2024) and $(1)M (Q3 2025), so the flip is NOT attributable to DA-24 — two independent defects, not one."
  - da_id: "DA-25"
    chosen_reading: "EXHIBITED. Boeing's `Program accounting quantities` (737 12,000 / 767 1,263 / 777 1,828 / 777X 600 / 787 1,900 at 2025-09-30) are an issuer-defined per-program unit metric that the segment tables cannot reproduce — the segment tables give only BCA/BDS/BGS revenue and loss from operations, with no program-level unit data. Contrast recorded: per-model DELIVERIES are disclosed inside the segment table and ARE reproducible, and segment operating margins are reproducible to the printed tenth."
  - da_id: "DA-26"
    chosen_reading: "EXHIBITED. The twelve-month figure is labelled `fiscal_period: \"Q4\"` in `get_company_financials`. Proof by arithmetic: FY2025 revenue 89,463 against 9M 2025 revenue 65,515 gives a true Q4 2025 revenue of 23,948, yet the Q4 row reports 89,463. At BA the mislabelled period is Q4 — consistent with the register's 'mislabelled period varies by issuer'."
  - da_id: "DA-27"
    chosen_reading: "NOT APPLICABLE, checked and cleared. BA is a December fiscal-year-end issuer (`fiscal_year_end_month: 12`), so the fiscal label and the calendar label coincide and the non-December off-by-one cannot arise. The platform's `FY2025 Q3 = 2025-07-01 → 2025-09-30` matches the filing's own 'three months ended September 30, 2025'."
  - da_id: "DA-28"
    chosen_reading: "NOT APPLICABLE as written — BA is not a recent IPO (10-Ks in the pipeline back to FY2016, filed 2017-02-08, CIK 0000012927), so the IPO capital-structure discontinuity never fires. BUT a capital-structure discontinuity of a different kind is present and must be registered: the 6.00% Series A Mandatory Convertible Preferred Stock (second listed security BA-PA) adds a preferred-dividend deduction line and lifts basic weighted-average shares 618.8M (Q3 2024) → 760.1M (Q3 2025). Per-share growth claims across that boundary are inadmissible."
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: "Q3 2024 income statement — total revenues 17,840; total costs and expenses (21,347); gross profit (3,507); income/(loss) from operating investments, net (15); G&A (1,085); R&D net (1,154); gain on dispositions, net blank; LOSS FROM OPERATIONS (5,761); 9M 2024 loss from operations (6,937); net loss attributable to Boeing shareholders (6,170) Q3 / (7,952) 9M; diluted EPS ($9.97) Q3 / ($12.91) 9M; weighted average diluted shares 618.8M Q3"
    ticker: BA
    form_type: 10-Q
    citation_id: sec215
    page_no: 3
    url: https://agentii.ai/v/BA/sec215/3
    located_via: read_source_pages
  - figure: "MD&A loss-from-operations narrative — 'Loss from operations for the three months ended September 30, 2024, increased by $4,953 million'; 'Core operating loss ... increased by $5,850 million and $4,900 million'; Unallocated items, eliminations and other Q3 2024 total (418): share-based plans 65, deferred comp (51), amortization of capitalised interest (24), R&D (105), eliminations and other unallocated (303)"
    ticker: BA
    form_type: 10-Q
    citation_id: sec215
    page_no: 43
    url: https://agentii.ai/v/BA/sec215/43
    located_via: read_source_pages
  - figure: "Q3 2025 income statement — total revenues 23,270; total costs and expenses (25,645); gross profit (2,375); income/(loss) from operating investments, net 14; G&A (1,522); R&D net (897); gain/(loss) on dispositions, net (1); LOSS FROM OPERATIONS (4,781); 9M 2025 loss from operations (4,496); net loss attributable to Boeing shareholders (5,337) Q3 / (5,985) 9M; less mandatory convertible preferred stock dividends 87 Q3 / 259 9M; diluted EPS ($7.14) Q3 / ($8.25) 9M"
    ticker: BA
    form_type: 10-Q
    citation_id: sec218
    page_no: 3
    url: https://agentii.ai/v/BA/sec218/3
    located_via: read_source_pages
  - figure: "Note 3 Digital Aviation Solutions Divestiture (as at 2025-09-30, UNCLOSED): agreement with Thoma Bravo to sell portions of the BGS segment's Digital Aviation Solutions business for $10.55 billion; 'We expect the transaction to close in 2025 and result in a gain at closing'; assets of $1,473 and liabilities of $524 classified as held for sale"
    ticker: BA
    form_type: 10-Q
    citation_id: sec218
    page_no: 12
    url: https://agentii.ai/v/BA/sec218/12
    located_via: read_source_pages
  - figure: "Segment-to-consolidated Loss from Operations bridge — Q3 2025 BCA (5,353) + BDS 114 + BGS 938 = segment operating loss (4,301); unallocated items (748); pension FAS/CAS 198; postretirement FAS/CAS 70; GAAP loss from operations (4,781); core operating loss non-GAAP (5,049); Q3 2024 comparatives (4,021)/(2,384)/834 → segment (5,571), unallocated (418), FAS/CAS 148 + 80 → GAAP (5,761), core (5,989); segment revenue Q3 2025 BCA 11,094 + BDS 6,902 + BGS 5,370 + unallocated (96) = 23,270"
    ticker: BA
    form_type: 10-Q
    citation_id: sec218
    page_no: 40
    url: https://agentii.ai/v/BA/sec218/40
    located_via: read_source_pages
  - figure: "Unallocated items detail Q3 2025 total (748): share-based plans 11, deferred comp (70), amortization of capitalised interest (22), R&D (102), eliminations and other unallocated (565); 9M 2025 total (2,145); DOJ agreement earnings charges $445M (2025) and $244M (2024) within G&A"
    ticker: BA
    form_type: 10-Q
    citation_id: sec218
    page_no: 41
    url: https://agentii.ai/v/BA/sec218/41
    located_via: read_source_pages
  - figure: "BCA segment results and DELIVERIES — Q3 2025 revenues 11,094, loss from operations (5,353), operating margin (48.3)%; Q3 2024 revenues 7,443, loss from operations (4,021), margin (54.0)%; quarterly deliveries 160 (2025) vs 116 (2024); 9M deliveries 440 vs 291"
    ticker: BA
    form_type: 10-Q
    citation_id: sec218
    page_no: 46
    url: https://agentii.ai/v/BA/sec218/46
    located_via: read_source_pages
  - figure: "PROGRAM ACCOUNTING QUANTITIES at 2025-09-30 — 737 12,000; 767 1,263; 777 1,828; 777X 600; 787 1,900 (at 2024-12-31: 11,600 / 1,263 / 1,822 / 500 / 1,800); BCA total backlog $534,613M vs $435,175M at 2024-12-31"
    ticker: BA
    form_type: 10-Q
    citation_id: sec218
    page_no: 47
    url: https://agentii.ai/v/BA/sec218/47
    located_via: read_source_pages
  - figure: "FY2025 Consolidated Statements of Operations — total revenues 89,463 (2024: 66,517); total costs and expenses (85,174); gross profit 4,289; income from operating investments, net 25; G&A (6,090); R&D net (3,615); GAIN ON DISPOSITIONS, NET 9,672; EARNINGS/(LOSS) FROM OPERATIONS 4,281 (2024: (10,707)); net earnings attributable to Boeing shareholders 2,235 (2024: (11,817)); diluted EPS $2.48 (2024: ($18.36))"
    ticker: BA
    form_type: 10-K
    citation_id: sec183
    page_no: 60
    url: https://agentii.ai/v/BA/sec183/60
    located_via: read_source_pages
  - figure: "Note 3 Digital Aviation Solutions Divestiture (CLOSED) — 'On October 31, 2025, we closed on the sale of portions of our BGS segment's Digital Aviation Solutions business ... to Thoma Bravo for proceeds of $10,550. The sale included Jeppesen, ForeFlight, AerData and OzRunways assets and liabilities and resulted in a gain of $9,566 recorded in Gain on dispositions, net in the Consolidated Statements of Operations.'"
    ticker: BA
    form_type: 10-K
    citation_id: sec183
    page_no: 78
    url: https://agentii.ai/v/BA/sec183/78
    located_via: read_source_pages
---

# BA — Recent Quarter, Phase 3 (Defect Census), PIL-3

Source filings read at page level: 10-Q `0000012927-24-000082` (**`sec215`**, 2024 Q3, filed
2024-10-23), 10-Q `0001628280-25-047023` (**`sec218`**, 2025 Q3, filed 2025-10-29), 10-K
`0001628280-26-004357` (**`sec183`**, FY2025, filed 2026-01-30). CIK 0000012927.

---

## 0. What was settled, in one table

The register recorded two statements about Boeing that looked like they might be one
statement, or might contradict each other. **They are two different periods, and both are
now confirmations.**

| Register statement | Period it actually refers to | Status after this pass |
|---|---|---|
| "**CONFIRMED DA-23 flip instance** — `−5,761 → +5,761`" | **Q3 2024**, three months ended 2024-09-30 (`sec215` p.3) | **CONFIRMED** — unchanged |
| "**OPEN CANDIDATE** — BA 2025 Q3 (net-loss bridge confirmed, margin unverified)" | **Q3 2025**, three months ended 2025-09-30 (`sec218` p.3) | **DISCHARGED → CONFIRMED** by detector 1 |

| Determination | Finding | Grade |
|---|---|---|
| Is `us-gaap:OperatingIncomeLoss` consolidated or segment-only at BA? | **CONSOLIDATED.** All 35 facts carry `dimensions: {}`; the label is "Loss from operations" on the face of the **Condensed Consolidated** Statements of Operations. BA's segment-only measure is a *different* extension element. | DEMONSTRATED |
| Is the flip an artefact of reading a segment line as consolidated? | **NO.** A second, independent identity built entirely from *segment* data closes on the same consolidated figure in both periods. | DEMONSTRATED |
| Does BA belong to the MRK/BMY/WWD coverage hole? | **NO.** No coverage hole — BA additionally files a complete three-segment bridge. | DEMONSTRATED |
| What is the mechanism? | **`\|x\|` absolute-value stripping, NOT inversion.** Two positive controls prove it. | DERIVED (arithmetically forced) |
| How many BA issuer-quarters remain unresolved? | **0.** BA's contribution to PIL-3's `wrong_if` count goes 1 → 0. | DEMONSTRATED |

**On the "small in percentage terms" framing.** The register's reasoning was that −$5,761M
against BA's revenue base "is small in percentage terms". That is true **only on the annual
base**:

| Figure | Numerator | Revenue base | Percentage |
|---|---|---|---|
| Q3 2024 loss from operations | −5,761 | **Q3 2024 revenue 17,840** | **−32.3%** |
| Q3 2024 loss from operations | −5,761 | 9M 2024 revenue 51,275 | −11.2% |
| Q3 2024 loss from operations | −5,761 | FY2024 revenue 66,517 | −8.7% |
| Q3 2025 loss from operations | −4,781 | **Q3 2025 revenue 23,270** | **−20.5%** |

A quarterly figure must be tested against a quarterly base. On that basis −32.3% is the
**largest single-quarter operating-loss margin in the series**, and it is not small. The
"invisible by inspection" intuition is right, but the reason is the one the register gives in
its second clause, not the first: at BA the flip is invisible **because the platform's sign
convention makes a $5.7B quarterly loss print identically to a $5.7B quarterly profit** —
not because the number is small. §4 shows that inside a single table the platform displays a
stripped −$10,707M FY2024 loss and a genuine +$4,281M FY2025 profit in the same
all-positive form.

---

## 1. DA-23 at BA, detector 1, component identity in-line

Per contract rule `data_integrity_register_applied`, the component derivation is shown for
every `operating_income` figure read here. `EPS × shares` was **not** used at any point and
is recorded as inadmissible.

### 1.1 Q3 2024 — the register's confirmed instance

Source: [📄 BA 10-Q (2024 Q3) p.3](https://agentii.ai/v/BA/sec215/3). Values in $ millions.

```
Total revenues                                          17,840
Total costs and expenses                               (21,347)
                                                       -------
Gross profit                                            (3,507)    = -19.66% of revenue
  Income/(loss) from operating investments, net            (15)
  General and administrative expense                    (1,085)
  Research and development expense, net                 (1,154)
  Gain on dispositions, net                                  -     <- blank in the filing
                                                        -------
Loss from operations                                    (5,761)    <- CLOSES EXACTLY

platform us-gaap:OperatingIncomeLoss         +5,761,000,000         <- SIGN STRIPPED
```

- **Identity closes exactly:** −3,507 − 15 − 1,085 − 1,154 = **−5,761**. ✔
- **Opex slack is fully accounted for:** gross profit − operating income = −3,507 − (−5,761)
  = **2,254** = 15 + 1,085 + 1,154. No residual, so no unstated line can be carrying the
  difference.
- **Gross-profit bound:** a company's operating income cannot exceed its gross profit when
  opex ≥ 0. Filed −5,761 ≤ −3,507 ✔ **passes**. Platform +5,761 > −3,507 ✘ **fails the
  bound by 9,268.** This is the DA-23 clause "also any level failing the gross-profit bound",
  and it fires on the platform's value while the filed value passes.
- **Magnitude identical, sign inverted** — the register's `−5,761 → +5,761`, confirmed.

### 1.2 Q3 2025 — the register's open candidate

Source: [📄 BA 10-Q (2025 Q3) p.3](https://agentii.ai/v/BA/sec218/3). Values in $ millions.

```
Total revenues                                          23,270
Total costs and expenses                               (25,645)
                                                       -------
Gross profit                                            (2,375)    = -10.21% of revenue
  Income/(loss) from operating investments, net             14
  General and administrative expense                    (1,522)
  Research and development expense, net                   (897)
  Gain/(loss) on dispositions, net                          (1)
                                                        -------
Loss from operations                                    (4,781)    <- CLOSES EXACTLY

platform us-gaap:OperatingIncomeLoss         +4,781,000,000         <- SIGN STRIPPED
```

- **Identity closes exactly:** −2,375 + 14 − 1,522 − 897 − 1 = **−4,781**. ✔
- **Opex slack:** −2,375 − (−4,781) = **2,406** = −14 + 1,522 + 897 + 1. Exact. ✔
- **Gross-profit bound:** filed −4,781 ≤ −2,375 ✔ **passes**; platform +4,781 > −2,375 ✘
  **fails by 7,156**.

**This is the register's open candidate, and the "margin unverified" residue is now
discharged.** The register's note that the period was *"resolved by detector 3 (margin
plausibility) only"* was correct as a scope statement — a +20.5% operating margin is
implausible for Boeing — but detector 3 is the weakest of the three detectors and was only
ever a stopgap. Detector 1 now closes on the filed components; the period no longer rests on
plausibility.

### 1.3 A second, INDEPENDENT identity — built from segment data

Because the concern was that the consolidation level might have been misread from a segment
line, the strongest available check is an identity that runs *through* the segments. BA
publishes one, on [📄 BA 10-Q (2025 Q3) p.40](https://agentii.ai/v/BA/sec218/40), $ millions:

| | 9M 2025 | 9M 2024 | **Q3 2025** | **Q3 2024** |
|---|---|---|---|---|
| Commercial Airplanes | (6,447) | (5,879) | **(5,353)** | **(4,021)** |
| Defense, Space & Security | 379 | (3,146) | **114** | **(2,384)** |
| Global Services | 2,930 | 2,620 | **938** | **834** |
| **Segment operating loss** | (3,138) | (6,405) | **(4,301)** | **(5,571)** |
| Unallocated items, eliminations and other | (2,145) | (1,364) | **(748)** | **(418)** |
| Pension FAS/CAS service cost adjustment | 588 | 608 | **198** | **148** |
| Postretirement FAS/CAS service cost adjustment | 199 | 224 | **70** | **80** |
| **Loss from operations (GAAP)** | **(4,496)** | **(6,937)** | **(4,781)** | **(5,761)** |
| FAS/CAS service cost adjustment | (787) | (832) | (268) | (228) |
| Core operating loss (Non-GAAP) | (5,283) | (7,769) | **(5,049)** | **(5,989)** |

- **Segment subtotal first:** −4,021 + 834 − 2,384 = **−5,571** ✔ (Q3 2024);
  −5,353 + 114 + 938 = **−4,301** ✔ (Q3 2025).
- **Then segment → consolidated:** −5,571 − 418 + 148 + 80 = **−5,761** ✔ (Q3 2024);
  −4,301 − 748 + 198 + 70 = **−4,781** ✔ (Q3 2025).

**Both close to the dollar.** This is what settles the segment-artefact question: an identity
that begins from three *segment* operating results and ends on the consolidated subtotal
cannot close on a figure that was misread from a segment line. The consolidated level is
real, and it is a loss.

The unallocated block is corroborated on [📄 p.41](https://agentii.ai/v/BA/sec218/41):
Q3 2025 share-based plans 11, deferred comp (70), amortisation of capitalised interest (22),
R&D (102), eliminations and other unallocated (565) → total **(748)** ✔ — matching the bridge.

### 1.4 Arc-level corroboration (detector 2) — and where it stops

From `get_calculation_tree` on both accessions, the `CondensedConsolidatedStatementsofOperations`
role defines `us-gaap:OperatingIncomeLoss` as:

| Child (parent = OperatingIncomeLoss) | Weight | Present in Q3 2024 tree | Present in Q3 2025 tree |
|---|---|---|---|
| `us-gaap:GrossProfit` | +1 | yes | yes |
| `ba_IncomeLossfromInvestments` | +1 | yes | yes |
| `us-gaap:GeneralAndAdministrativeExpense` | −1 | yes | yes |
| `us-gaap:GainLossOnDispositionOfAssets` | +1 | yes | yes |
| `us-gaap:ResearchAndDevelopmentExpense` | −1 | **yes** | **NO — ARC ABSENT** |
| | | 5 arcs | 4 arcs |

- **Q3 2024 arc set closes exactly** on the filed value:
  −3,507 + (−15) + 0 − 1,085 − 1,154 = **−5,761** ✔
- **Q3 2025 arc set cannot close**, because it is short by exactly the R&D line:
  −2,375 + 14 + (−1) − 1,522 = **−3,884**, against the filed **−4,781** — a gap of **897**,
  which is precisely "Research and development expense, net (897)" on the face of the same
  statement. The filer's own linkbase is incomplete for this accession.

**The load-bearing consequence:** in Q3 2024 the filer's own calculation linkbase
independently reconstructs **−5,761**, while the platform stores **+5,761,000,000**. The
stored fact contradicts the filer's asserted arc set. The flip is therefore not an arc
artefact — where the arcs are complete, the arcs are right and the stored fact is wrong.

---

## 2. Is BA's `OperatingIncomeLoss` consolidated or segment-only?

**CONSOLIDATED.** Three independent lines of evidence:

1. **The facts are undimensioned.** `search_xbrl_facts` for BA `OperatingIncomeLoss` returned
   35 rows, and **every one carries `dimensions: {}`** — no `us-gaap:StatementBusinessSegmentsAxis`
   member anywhere in the set. There is no segment-dimensioned `OperatingIncomeLoss` fact to
   misread.
2. **The label is the consolidated face.** The concept's label is "Loss from operations",
   positioned on the **Condensed Consolidated Statements of Operations**, above "Other income,
   net" and "Interest and debt expense"
   ([📄 sec215 p.3](https://agentii.ai/v/BA/sec215/3), [📄 sec218 p.3](https://agentii.ai/v/BA/sec218/3)).
3. **BA's segment-only measure is a different element.** The calculation tree carries a
   BA-specific extension, `ba_OperatingIncomeLossExcludingUnallocatedPensionAndPostretirementAdjustments`,
   whose children are the five unallocated items, and the segment subtotal is reported in
   prose as "Segment operating loss" on
   [📄 sec218 p.40](https://agentii.ai/v/BA/sec218/40). Neither is `us-gaap:OperatingIncomeLoss`.

**BA is therefore NOT in the MRK/BMY/WWD class.** There is no coverage hole at BA, and the
flip is not an artefact of a segment line being read as consolidated. This is the specific
question the register flagged, and the answer is a clean negative.

---

## 3. The mechanism: absolute-value stripping, not inversion

The register's DA-23 wording is "inverts/strips signs on negative values". The two are
different defects with different detection profiles, and BA separates them. **BA has two
positive controls — quarters where the platform's stored value is exactly right because the
filed value was already positive.**

Field-wide series for `us-gaap:OperatingIncomeLoss`, $ millions:

| Period | As filed | Platform | Verdict |
|---|---|---|---|
| Q1 2024 | (86) ᴰ | **+86** | stripped |
| Q2 2024 | (1,090) ᴰ | **+1,090** | stripped |
| **Q3 2024** | **(5,761)** ˢ | **+5,761** | **STRIPPED — the register's instance** |
| 9M 2024 | (6,937) ˢ | +6,937 | stripped |
| FY2024 | (10,707) ˢ | +10,707 | stripped |
| **Q1 2025** | **+461** ᴰ | **+461** | **CORRECT — positive control** |
| **Q2 2025** | **(176)** ᴰ | **+176** | **stripped** |
| 1H 2025 | +285 ᴰ | +285 | correct |
| **Q3 2025** | **(4,781)** ˢ | **+4,781** | **STRIPPED — the register's candidate** |
| 9M 2025 | (4,496) ˢ | +4,496 | stripped |
| **FY2025** | **+4,281** ˢ | **+4,281** | **CORRECT — positive control** |

ˢ = read at source in this pass. ᴰ = derived arithmetically; see the note below.

**How Q1/Q2 2025 is forced.** Two source-read figures from
[📄 sec218 p.3](https://agentii.ai/v/BA/sec218/3) — 9M 2025 loss from operations **(4,496)**
and Q3 2025 loss from operations **(4,781)** — fix the first half exactly:
−4,496 − (−4,781) = **+285**. The platform stores Q1 2025 at +461 and Q2 2025 at +176
(= 637 ≠ 285). If *both* were stripped, the true values would be −461 and −176, summing to
−637, which cannot equal +285; if *neither* were, they would sum to 637, which also cannot.
The only assignment satisfying +285 is **Q1 = +461 and Q2 = −176**: 461 − 176 = 285 ✔. So
Q1 2025's stored value is correct and Q2 2025's is stripped. Corroborated by the platform's
own 1H 2025 fact of +285 (`ba-20250630.htm`).

If the defect were a blanket inversion, Q1 2025 would read **−461** and 1H 2025 would read
**−285**. They do not. **The mechanism is `|x|`: negative values are stripped, positive values
pass through untouched** — exactly the register's "strips signs on negative values", and this
pass supplies the first two positive controls in the register's record that distinguish it
from inversion.

**Why this matters beyond bookkeeping.** Because the strip is conditional on the sign, and
because BA's series crosses zero (losses in 2024, a genuine profit in FY2025), the platform's
`get_company_financials` table contains **both** a stripped loss and a genuine profit,
rendered in the same all-positive form. See §4.

---

## 4. DA-24 — a $9,566M disposal gain through the operating line

### 4.1 The exposure is structural at BA, not incidental

BA's income statement places disposal results **inside** the operating subtotal by
construction. On the face of the statement the line order is:

```
  Research and development expense, net
  Gain/(loss) on dispositions, net        <- HERE
  Loss from operations                    <- operating subtotal
```

Both the [📄 2025 Q3 face statement](https://agentii.ai/v/BA/sec218/3) and the
[📄 FY2025 10-K face statement](https://agentii.ai/v/BA/sec183/60) place it there, and the
calculation linkbase agrees: `us-gaap:GainLossOnDispositionOfAssets` is a child of
`us-gaap:OperatingIncomeLoss` with **weight +1** in both the Q3 2024 and Q3 2025 roles.

### 4.2 In the two flip periods the disposal effect is immaterial

| Period | `Gain/(loss) on dispositions, net` | Against loss from operations |
|---|---|---|
| Q3 2024 | blank / nil | 0.00% |
| Q3 2025 | **(1)** | 0.02% of (4,781) |
| 9M 2024 | 5 | 0.07% |
| 9M 2025 | 63 | 1.4% |

**So the two defects are separate and must not be conflated.** The DA-23 flip in Q3 2024 and
Q3 2025 is *not* caused by a disposal gain, and no part of the flip is explained by DA-24.

### 4.3 But the very next quarter is a DA-24 instance of extreme magnitude

The register asked specifically: *"check: BA has divestitures"*. BA does, and the largest one
landed one quarter after the flip window.

- **At 2025-09-30 the sale had not closed.** Note 3 on
  [📄 sec218 p.12](https://agentii.ai/v/BA/sec218/12): agreement with Thoma Bravo to sell
  portions of the BGS segment's Digital Aviation Solutions business for **$10.55 billion**,
  *"We expect the transaction to close in 2025 and result in a gain at closing"*, with
  $1,473M of assets and $524M of liabilities held for sale. **No gain was recognised in 9M
  2025** — consistent with the 9M disposal line being only 63.
- **It closed on 2025-10-31, inside Q4.** Note 3 of the FY2025 10-K,
  [📄 sec183 p.78](https://agentii.ai/v/BA/sec183/78), verbatim: *"On October 31, 2025, we
  closed on the sale of portions of our BGS segment's Digital Aviation Solutions business
  (Digital Aviation Solutions Divestiture) to Thoma Bravo for proceeds of $10,550. The sale
  included Jeppesen, ForeFlight, AerData and OzRunways assets and liabilities and resulted in
  **a gain of $9,566 recorded in Gain on dispositions, net in the Consolidated Statements of
  Operations**."*
- **And that line is above the operating subtotal.** FY2025 as filed
  ([📄 sec183 p.60](https://agentii.ai/v/BA/sec183/60)), $ millions:

```
Total revenues                                          89,463
Total costs and expenses                               (85,174)
                                                       -------
Gross profit                                             4,289
  Income from operating investments, net                    25
  General and administrative expense                    (6,090)
  Research and development expense, net                 (3,615)
  Gain on dispositions, net                              9,672     <- 96.7% of it is the DAS gain
                                                        -------
Earnings/(loss) from operations                          4,281     <- CLOSES EXACTLY
platform us-gaap:OperatingIncomeLoss                +4,281,000,000  <- correct (filed positive)
```

  Identity closes exactly: 4,289 + 25 − 6,090 − 3,615 + 9,672 = **4,281** ✔. Checked against
  FY2024 for good measure: −1,991 + 71 − 5,021 − 3,812 + 46 = **−10,707** ✔.

**The consequence.** Boeing's FY2025 GAAP operating result is a **profit of $4,281M — its
first positive operating year since 2018**. Of that, **$9,672M is a disposal gain** (of which
$9,566M is the DAS sale), leaving an ex-disposal operating result of **−5,391M**. At the
quarter level: FY2025 4,281 less 9M 2025 (4,496) gives **Q4 2025 operating income of
+8,777M**; Q4 dispositions were 9,672 − 63 = **9,609M**; so **Q4 2025 ex-disposal operating
income was −832M**. A reported +$8.8B quarterly operating profit whose sign is entirely
supplied by a one-time divestiture gain sitting inside the operating line.

**DA-24 disposition: EXHIBITED, materially, one quarter after the flip window — with a
magnitude ($9,566M) that exceeds every quarterly operating result in the series. Not
attributable to the DA-23 flip, and therefore recorded as a separate defect.**

---

## 5. DA-25 — issuer-defined per-unit metric not reproducible from segment tables

**EXHIBITED.** Boeing discloses **program accounting quantities** on
[📄 sec218 p.47](https://agentii.ai/v/BA/sec218/47):

| Program | 2025-09-30 | 2024-12-31 |
|---|---|---|
| 737 | **12,000** | 11,600 |
| 767 | **1,263** | 1,263 |
| 777 | **1,828** | 1,822 |
| 777X | **600** | 500 |
| 787 | **1,900** | 1,800 |

These are the program-accounting block sizes over which Boeing amortises tooling and
non-recurring costs — an **issuer-defined, per-program unit metric**. The segment tables
(on [📄 p.40](https://agentii.ai/v/BA/sec218/40) and [📄 p.46](https://agentii.ai/v/BA/sec218/46))
give revenue and loss from operations for BCA/BDS/BGS only. **There is no program-level unit
data in the segment tables, and no segment-level decomposition in the accounting-quantity
table.** The metric is not reproducible from the segment tables, which is DA-25's test.

**Two clean contrasts, both checked and cleared, which sharpen the finding:**

- **Per-model deliveries ARE reproducible** from the segment tables. [📄 p.46](https://agentii.ai/v/BA/sec218/46)
  gives BCA deliveries by model: 9M 2025 **440** (737 330, 767 20, 777 29, 787 61) vs 9M 2024
  **291**; Q3 2025 **160** vs Q3 2024 **116**. Deliveries sit *inside* the segment table, so
  DA-25 does not bite on them.
- **Segment operating margins ARE reproducible.** [📄 p.46](https://agentii.ai/v/BA/sec218/46)
  prints BCA margins of (48.3)% Q3 2025 and (54.0)% Q3 2024. Recomputed from the same table:
  −5,353 / 11,094 = −48.26% ✔ and −4,021 / 7,443 = −54.02% ✔. Reproducible to the printed
  tenth.

**A loaded side-observation for DA-23.** Those segment margins are **negative** and come from
the same filing whose consolidated XBRL fact the platform stores as **+4,781,000,000**. The
filing therefore contradicts the platform's sign *internally*: a +20.5% consolidated
operating margin is impossible alongside a −48.3% margin at the largest segment. This is
detector 3 arriving at the same answer as detector 1, from inside the same document.

---

## 6. DA-26, DA-27, DA-28

### 6.1 DA-26 — annual mislabelled as quarterly: **EXHIBITED at BA**

`get_company_financials` (statement_type `income_statement`) returns a `metrics` array whose
Q4 row carries the **twelve-month** figure under `fiscal_period: "Q4"`:

| Row | period_end | revenues | operating_income | eps_basic |
|---|---|---|---|---|
| FY2025 **Q4** | 2025-12-31 | **89,463** | 4,281 | 2.49 |
| FY2025 Q3 | 2025-09-30 | 23,270 | 4,781 | 7.14 |
| FY2024 **Q4** | 2024-12-31 | **66,517** | 10,707 | 18.36 |

**Proof by arithmetic.** Q1 + Q2 + Q3 2025 revenues = 19,496 + 22,749 + 23,270 = **65,515**,
which equals the 9M 2025 total on [📄 sec218 p.3](https://agentii.ai/v/BA/sec218/3) ✔ — so the
Q1–Q3 rows are genuine three-month periods. Reduced against the FY total of **89,463** on
[📄 sec183 p.60](https://agentii.ai/v/BA/sec183/60), the true Q4 2025 revenue is
**89,463 − 65,515 = 23,948**. The Q4 row reports **89,463**. The same holds for FY2024
(66,517 = the annual revenue, not the fourth quarter's). The Q4 row is the annual row.

**The mislabelled period at BA is Q4.** The register says the mislabelled period "varies by
issuer", and BA is the case where it falls on the fourth quarter rather than an interim one.
The `operating_income` on that row (4,281) is the annual figure, and the FY2024 row's 10,707
is a sign-stripped annual loss (§3).

### 6.2 DA-27 — fiscal labels from the calendar quarter: **NOT APPLICABLE, checked**

`get_company_fiscal_calendar` returns `fiscal_year_end_month: 12` for BA, with quarter
boundaries at 2025-03-31 / 06-30 / 09-30 / 12-31. The fiscal label and the calendar label
coincide, so the non-December off-by-one cannot arise. The platform's `FY2025 Q3 =
2025-07-01 → 2025-09-30` matches the filing's own "three months ended September 30, 2025".
**Recorded as a checked negative**, consistent with the register's own scope condition
(n = 4 of 4, all non-December year-ends).

### 6.3 DA-28 — IPO capital-structure discontinuity: **NOT APPLICABLE as written**

BA is not a recent IPO. The 10-K series in the pipeline runs back to FY2016 (accession
`0000012927-17-000006`, filed 2017-02-08, citation `sec174`), under a long-standing CIK
0000012927 NYSE listing. The IPO trigger never fires.

**But a capital-structure discontinuity of a different kind is present, and it must be
registered rather than passed over.** Boeing issued 6.00% Series A Mandatory Convertible
Preferred Stock in 2025 — visible as a second listed security, **BA-PA**, in the filing
metadata, and on the face of the income statement
([📄 sec218 p.3](https://agentii.ai/v/BA/sec218/3)) as a new line, *"Less: mandatory
convertible preferred stock dividends accumulated during the period"*: **87** for Q3 2025 and
**259** for 9M 2025, rising to **345** for FY2025 ([📄 sec183 p.60](https://agentii.ai/v/BA/sec183/60)).
The EPS note on [📄 sec218 p.12](https://agentii.ai/v/BA/sec218/12) confirms the instrument
uses the **if-converted method** for dilution, and basic weighted-average shares rose from
**618.8M** (Q3 2024) to **760.1M** (Q3 2025) — a **22.8%** increase from the combined effect
of the preferred conversion and share issuance.

**Consequence for PIL-3: the per-share series must be quarantined across this boundary.**
Any Q3 2024 → Q3 2025 per-share comparison mixes a capital-structure change with an operating
change. The same section supplies the DSPX-style per-share caveat the register's DA-23/28
note anticipates — and note that the platform's own `eps_basic` for Q3 2025 reads **+7.14**
where the filing prints **($7.14)**: the strip reaches EPS too. That observation is recorded
as evidence of the strip's breadth, **not** as a sign test — `EPS × shares` remains
inadmissible for the operating line, and was not used.

---

## 7. Data-integrity register — application table

| DA | Test | BA result | Basis |
|---|---|---|---|
| **DA-23** | `\|computed\| == \|reported\|`, opposite signs; any level failing the gross-profit bound | **EXHIBITED ×2 — both periods CONFIRMED.** Q3 2024 (5,761) → +5,761,000,000; Q3 2025 (4,781) → +4,781,000,000. Both fail the gross-profit bound on the platform's value and pass on the filed value. Field is consolidated. | §1.1, §1.2, §2 |
| **DA-24** | Disposal gain flowing through the operating line | **EXHIBITED.** $9,566M DAS/Thoma Bravo gain recorded in `Gain on dispositions, net`, which sits above the operating subtotal. Q4 2025 reported operating income +8,777 vs **−832** ex-disposal. Immaterial in the two flip periods (nil / $(1)M) — separate defect. | §4 |
| **DA-25** | Issuer-defined per-unit metric not reproducible from segment tables | **EXHIBITED.** Program accounting quantities (737 12,000 / 767 1,263 / 777 1,828 / 777X 600 / 787 1,900). Deliveries and segment margins checked and are reproducible — clean contrasts. | §5 |
| **DA-26** | Annual mislabelled as quarterly | **EXHIBITED.** Q4 row carries the twelve-month figure: FY2025 revenue 89,463 under `fiscal_period: "Q4"` where the quarter is 23,948. Mislabelled period at BA = **Q4**. | §6.1 |
| **DA-27** | Fiscal labels from the calendar quarter, off-by-one for non-December year-ends | **NOT APPLICABLE — checked.** `fiscal_year_end_month: 12`; labels coincide. | §6.2 |
| **DA-28** | IPO capital-structure discontinuity | **NOT APPLICABLE — checked**, no recent IPO. **But a preferred-stock discontinuity of a different kind exists** (BA-PA mandatory convertible; shares 618.8M → 760.1M, +22.8%). | §6.3 |

---

## 8. Instrument hazards, measured at BA

The standing instrument rule was measured four ways before this pass. BA supplies
**five further measurements**, and the first is the most consequential.

### 8.1 🔴 `validate_calculation` returns NO ROW AT ALL for `us-gaap:OperatingIncomeLoss`

`validate_calculation` was run on both accessions. Its `results` arrays contain 19 rows
(2024 Q3) and 30 rows (2025 Q3) — and **`us-gaap:OperatingIncomeLoss` is absent from both**.
It evaluated `GrossProfit`, `CostOfRevenue`, `ProfitLoss`, `NetIncomeLoss`,
`StockholdersEquity`, `DefinedBenefitPlanNetPeriodicBenefitCost` and a dozen others. It did
not evaluate the one concept the register is about.

The VRT artifact recorded this as "NO RESULT for a concept with seven arcs". BA reproduces it
for a concept with **five arcs** (Q3 2024) and **four arcs** (Q3 2025). **Two of two issuers
tested now show silence on the tested concept, at three different arc counts. This is a
pattern, not a VRT idiosyncrasy.**

**Why this is the worst hazard of the set: silence is indistinguishable from a clean pass.**
A consumer who runs this tool, sees no `fail` row for `OperatingIncomeLoss`, and concludes the
field is clean has been misled by an omission it cannot see. The tool reports no coverage
manifest — not which arcs it evaluated, not which it declined, not why. Until it does, its
silence on a concept carries no evidential weight whatsoever.

### 8.2 `reported` is sign-stripped on negatives — so both columns are corrupted

`reported` is the instrument's reference column, and it is corrupted in the same direction as
the value under test:

| Row | `computed` | `reported` | As filed |
|---|---|---|---|
| `GrossProfit` Q3 2025 | −20,275,000,000 | **+2,375,000,000** | (2,375) |
| `IncomeLossFromContinuingOperationsBeforeIncomeTaxes...` Q3 2025 | 520,000,000 | **+5,199,000,000** | (5,199) |
| `GrossProfit` 9M 2024 | −46,141,000,000 | **+3,507,000,000** | (3,507) |

Because both sides are stripped, **the failure is invisible in the `diff` column** where the
strip cancels. This is strictly worse than the GOOG finding ("`reported` is corrupted on
comparatives"): here `reported` is corrupted on the *current* period, on negatives, by the
same mechanism that corrupts the fact.

### 8.3 A PASS row asserts $5.34B of net income for a quarter with a $5.34B net loss

The single most damning row in either accession:

```
us-gaap:NetIncomeLoss   period 2025-09-30
  computed  5,335,000,000
  reported  5,337,000,000
  diff          2,000,000
  status            PASS
```

The filed value for that quarter — net loss attributable to Boeing shareholders, on
[📄 sec218 p.3](https://agentii.ai/v/BA/sec218/3) — is **(5,337)**. The row passes because
|−5,337| ≈ 5,335 and both sides are positive. **"`pass` does not certify a sign" is not a
caution here; it is a demonstrated false assurance about the sign of a $5.3B item.**

### 8.4 `computed` is short by exactly one cost line — and which line is short flips between filings

The arc `CostOfRevenue → CostOfGoodsAndServicesSold (+1)` is structurally incomplete, and the
omitted line is not stable:

| Row | `computed` | `reported` | Difference | Equals which cost line? |
|---|---|---|---|---|
| `CostOfRevenue` Q3 2025 | 2,908,000,000 | 25,645,000,000 | **22,737** | "Cost of products" Q3 2025 |
| `CostOfRevenue` Q3 2024 (comparative, `sec218`) | 2,934,000,000 | 21,347,000,000 | **18,413** | "Cost of products" Q3 2024 |
| `CostOfRevenue` Q3 2023 (comparative, `sec215`) | 14,464,000,000 | 16,939,000,000 | **2,475** | "Cost of services" Q3 2023 |

Every difference is exact against the filed statements on
[📄 sec218 p.3](https://agentii.ai/v/BA/sec218/3) and
[📄 sec215 p.3](https://agentii.ai/v/BA/sec215/3). So the arc binds to a *single* cost element
while claiming to be the total — and **which element it binds to changes between accessions**.
The incompleteness propagates upward into `GrossProfit` (§8.2). This is the "incomplete arcs"
mechanism named in the standing rule, made explicit and quantified.

Reported rates: **13 of 19 rows fail on the 2024 Q3 accession (68%)** and **18 of 30 on the
2025 Q3 accession (60%)** — against a rule that measured 93% false-positive. Neither figure
is read as evidence about the filings; §8.1–§8.4 show the failures are the instrument's.

### 8.5 Period-key ambiguity binds a three-month value to a nine-month key

The validator's `period` field is an undifferentiated date — `Mon Sep 30 2024` — with no
duration. The `ProfitLoss` row under that key reports `reported` 6,170,000,000, which is the
**three-month** figure for Q3 2024 (net loss attributable, (6,170)), not the nine-month figure
of **(7,952)** on [📄 sec215 p.3](https://agentii.ai/v/BA/sec215/3). A three-month value is
therefore reported under a key that also denotes nine months, and nothing in the output
distinguishes them. This is the "3-month/6-month column mixing" hazard rendered invisible.

### 8.6 `search_keyword_in_source` false positives — measured twice at BA

Per the standing rule, every page cited in this artifact was confirmed by `read_source_pages`
before being cited, and **no page number here is inferred from a keyword hit**.

| Query | Pages returned | Materially relevant | Dilution |
|---|---|---|---|
| `deliveries` on `sec218` | 21 | **2** (`p.46`, `p.50`) | **90%** |
| `Gain on dispositions, net` on `sec183` | 5 | **2** (`p.60`, `p.78`) | **60%** |

The `deliveries` hit list includes environmental-remediation, investments and capital-resources
pages. The `Gain on dispositions, net` hit list includes the statements of comprehensive income
and cash flows — pages containing the phrase but not the line. Both would have produced a
plausible-looking wrong citation.

### 8.7 Arc sets are role-scoped, and `OperatingIncomeLoss` appears as a parent in two incompatible roles

On `sec218` alone, `us-gaap:OperatingIncomeLoss` is a parent in **two** roles:

- `CondensedConsolidatedStatementsofOperations` — the four arcs in §1.4, a coherent operating
  subtotal (missing only R&D).
- `SegmentandRevenueInformationReconciliationofRevenuefromSegmentstoConsolidatedDetails` — a
  role that names the *revenue* reconciliation but whose arcs declare
  `OperatingIncomeLoss = Revenues − SegmentReportingOtherItemAmount − ResearchAndDevelopmentExpense`.

The second set cannot define an operating subtotal. **Any consumer that unions arcs across
roles computes garbage**, and the union is not distinguishable from the correct set in the
tool's flat output. This also supplies a caution against reading a calculation role URI as a
statement of what is being calculated.

### 8.8 Cross-instrument agreement — a cleared item, not a defect

The platform's sign on `IncomeTaxExpenseBenefit` is the opposite of the printed sign in both
quarters (filed **+50** benefit → platform **−50,000,000**; filed **(140)** expense → platform
**+140,000,000**). This was investigated as a possible second defect and **cleared**: it is the
standard XBRL convention (positive = expense), confirmed by the filing's own label order
flipping between accessions — "Income tax **benefit/(expense)**" in 2024 Q3, "Income tax
**(expense)/benefit**" in 2025 Q3 — tracking the same convention. With the filed signs both
statements foot exactly (−6,224 + 50 = −6,174; −5,199 − 140 = −5,339). **Recorded as checked
and clean.**

### 8.9 A double-counting hazard in `get_statement`

`get_statement` emits the same $ value twice under two concepts on both accessions —
`us-gaap:CostOfGoodsAndServicesSold` ("Cost of products and services") and
`us-gaap:CostOfRevenue` ("Total costs and expenses"), both = 21,347 / 25,645. Summing the
platform's cost rows double-counts total costs. Every derivation in this artifact uses the
filing's own line structure, read at page level, rather than summing platform rows.

### 8.10 The `skill_pin` is not reproducible across artifacts — the Q57 ledger was never created

`skill_pin` is one of the five mandatory pins, and `theses/001-technology-baseline/reproduce.md`
declares it **RESOLVED 2026-09-18**: the registry carries no per-skill hash, but
`dispatch.skill_version_hash()` computes a content hash of the skill directory, and — verbatim —
*"Remaining skills hash on first use and are **appended** to `skill_pins.jsonl` (Q57 — never
overwritten)."*

Two measurements show that mechanism did not operate:

1. **`skill_pins.jsonl` does not exist.** A repo-wide search returns nothing — not at the
   program root, not under either thesis, not under `tools/`. No skill was ever appended.
2. **`recent-quarter` is absent from the resolved table.** `reproduce.md` lines 33–40 list
   exactly six hashes — operational-kpi, unit-economics, secular-trends, supply-chain,
   competitive, risk. `recent-quarter` is a thesis-002 skill and is not among them.

The consequence is a pin that cannot do its job. **Four `recent-quarter` artifacts, three
different treatments of the same pin:**

| Artifact | `skill_pin` | Assessment |
|---|---|---|
| `001/artifacts/SPCX/…_recent-quarter_…` | `registry-1.0.0` | a whole-registry proxy — expressly rejected by `reproduce.md` |
| `002/artifacts/LUNR/…_recent-quarter_…` | `registry-1.0.0` | same proxy |
| `002/artifacts/SPCX/…_recent-quarter_…` | `0730fd170124` | **wrong value** — that is the `operational-kpi` hash, inherited from the sibling artifact |
| `002/artifacts/HAWK/…` and **this** artifact | *UNRESOLVED* (marker) | honest, but not a pin |

A pin whose value differs across artifacts that pin the *same skill* cannot detect a skill
version change — which is its only purpose. The `002/SPCX` case is the concrete failure: a
copy-paste from an adjacent skill's frontmatter produces a value that *looks* like a real hash
and validates cleanly (`skill_pin` has no const in the contract), so nothing flags it.

**This artifact records `UNRESOLVED` with the reason, rather than inventing a hash.** It is
carried forward as a register item (§12.9) rather than silently resolved, because the fix is a
program-level one: create the ledger, or hash `recent-quarter` once and publish it.

### 8.11 Platform page numbers do not match the printed page footers

Every citation here uses the **platform** page number, because that is what the canonical URL
`/v/BA/{citation_id}/{N}` resolves to. Those numbers do not always match the page footer
printed in the document:

| Citation | Platform page no. | Printed footer |
|---|---|---|
| `sec215` MD&A loss-from-operations | **43** | 41 |
| `sec218` segment bridge | **40** | 38 |
| `sec183` consolidated statements of operations | **60** | 54 |

The offset is not constant (2, 2, 6), so it cannot be corrected by a fixed rule, and it grows
with the document. **A reader who opens one of these links and checks the footer will see a
mismatch and may conclude the citation is wrong.** It is not: the platform number is the
correct addressing unit, and it is the one `located_via: read_source_pages` records. Recorded
here so that a future verifier does not "correct" a right citation into a wrong one.

---

## 9. §1c `no_single_basis_collapse` — every competing basis, none collapsed

Boeing's "operating result" is reported on five distinct bases in these filings. All five are
stated here; none is presented as *the* answer, and the identity converting between them is
given in §1.3.

| # | Basis | Q3 2024 | Q3 2025 | What it excludes |
|---|---|---|---|---|
| 1 | **GAAP loss from operations** (consolidated, = `us-gaap:OperatingIncomeLoss`) | (5,761) | (4,781) | nothing |
| 2 | **Segment operating loss** (BCA + BDS + BGS) | (5,571) | (4,301) | unallocated items and both FAS/CAS adjustments |
| 3 | **Core operating loss** (Non-GAAP) | (5,989) | (5,049) | FAS/CAS service cost adjustment |
| 4 | **Ex-disposal operating result** | (5,761) — nil disposal | (4,780) — disposal (1) | gain/loss on dispositions |
| 5 | **Platform-stored value** | +5,761 | +4,781 | *the sign* |

And for the FY2025 period where DA-24 bites: GAAP **+4,281** vs ex-DAS-gain **−5,391** — a
$9,672M spread between two defensible readings of the same line, both reported.

The register's `wrong_if` metric is denominated in *issuer-quarters with unresolved defect
status*, and the basis choice materially changes which quarters count. **This artifact does not
collapse that: BA's Q4 2025 is "a profit of $4,281M" on basis 1 and "a loss of $832M" on
basis 4, and both are recorded.**

---

## 10. Corrections to the register as inherited from 001 (frozen-001 policy)

001's artifacts are not rewritten. The corrections are recorded here and cited by location,
per the frozen-001 policy.

**10.1 §1b / §2 — the BA row in the register table needs amending.** The inherited entry reads
`BA | Boeing | industrial.aerospace_defense | 3% | "DA-23 flip instance #5 (−5,761 → +5,761)
and a DA-23 candidate — 2025 Q3 net-loss bridge confirmed but the margin remains unverified,
so it is resolved by detector 3 (margin plausibility) only"`. The correction:

- The **confirmed flip instance** and the **candidate** are **two different periods** — Q3
  2024 and Q3 2025 respectively — not two statements about one quarter.
- The **2025 Q3 candidate is discharged**: resolved by **detector 1** (component identity,
  closes exactly) and by a **second independent identity** (the segment-to-consolidated
  bridge, closes exactly), not by detector 3 alone.
- **BA's `us-gaap:OperatingIncomeLoss` is CONSOLIDATED.** BA is **not** in the MRK/BMY/WWD
  coverage-hole class; the "if the field is segment-only the flip may be an artefact" caveat
  does not apply.
- The **mechanism is `|x|`, not inversion**, on the strength of two positive controls
  (2025 Q1 +461M, FY2025 +4,281M).
- **BA contributes 1 → 0** to PIL-3's `wrong_if` count.

**10.2 Proposed register addition for PIL-3 — instrument coverage, not issuer behaviour.**
The register covers *data-asset* defects. §8.1 is a defect of the **instrument**, and it is
the one that most threatens the register's own evidence chain: `validate_calculation` omits
the concept under test without saying so, in 2 of 2 issuers tested. Recommend a registered
item of the form:

> **`validate_calculation` must return a coverage manifest** — which arcs it evaluated, which
> it declined, and why. Absent that, a concept's absence from its output carries no evidential
> weight, and "we ran the validator and `operating_income` did not fail" is an unfalsifiable
> claim. Measured at BA: 2 of 2 accessions silent on `us-gaap:OperatingIncomeLoss` at 5 arcs
> and 4 arcs; VRT silent at 7 arcs.

**10.3 Proposed register addition — DA-24 needs a magnitude clause.** The register's DA-24 test
("disposal gain flowing through the operating line") is satisfied by $(1)M and by $9,566M
alike. At BA both occur in adjacent quarters, and only the second changes the sign of an
annual result. Recommend DA-24 carry a materiality condition tied to the *sign* of the
operating result it produces.

---

## 11. What could NOT be verified

1. **The Q1 2025 / Q2 2025 split was not read at source.** The two 10-Qs for those quarters
   (`ba-20250331.htm`, `ba-20250630.htm`) were not paged. The split is **arithmetically
   forced** from two source-read values (9M 2025 (4,496) and Q3 2025 (4,781) on `sec218` p.3)
   and corroborated by the platform's own 1H 2025 fact of +285 — the only assignment
   satisfying +285 is Q1 +461 / Q2 −176 — but a direct page read would upgrade it from
   DERIVED to DEMONSTRATED. **The positive-control claim rests on this derivation**, so it is
   flagged rather than asserted as source-read.
2. **Q1 2024 and Q2 2024 were not read at source.** Their stripped values (86, 1,090) are
   inferred from the sum-to-9M identity: 86 + 1,090 + 5,761 = 6,937 = the source-read 9M 2024
   loss from operations. The 9M total is source-read; the quarterly split is DERIVED.
3. **Q4 2025 has no standalone filing read.** The +8,777 GAAP / −832 ex-disposal figures are
   derived from source-read FY2025 (`sec183` p.60) less source-read 9M 2025 (`sec218` p.3).
   No Q4 2025 10-K quarterly column or 8-K was paged, and the Q4 disposal-line figure (9,609)
   is a residual, not a printed number.
4. **The DAS gain's allocation between segments is not established.** The $9,566M gain is
   attributed to the BGS divestiture in the note, but whether any part is eliminated at the
   segment bridge (as distinct from the consolidated operating line) was not traced. The
   consolidated operating line is settled; the segment attribution is not.
5. **`validate_calculation` was run on the two 10-Qs only.** The FY2025 10-K (`sec183`) was
   not run through it, so the arc-coverage gap (§8.1) is measured on 2 of 3 relevant
   accessions.
6. **The FY2025 10-K's own calculation tree was not retrieved**, so it is not established
   whether the `ResearchAndDevelopmentExpense` arc missing from the Q3 2025 10-Q tree (§1.4)
   is present in the 10-K tree. The incompleteness is established for the 10-Q.
7. **No transcript was read.** No earnings call was used; every figure here comes from a
   filed statement or note. If management characterised the FY2025 operating profit as
   underlying rather than disposal-driven, that statement is not tested here.
8. **`skill_pin` is unresolved**, not fabricated — `dispatch.skill_version_hash()` is not
   reachable from this artifact context (see frontmatter).
9. **PIL-3's `wrong_if` is a cross-issuer count and is not closed by this artifact.** BA's
   contribution is 0 resolved-and-unresolved; the universe-level `count_of_universe_issuer_quarters_with_unresolved_defect_status`
   depends on the sibling VOYG/LUNR/HAWK/SPCX register artifacts.

---

## 12. Carry-forwards

1. **PIL-3 — the register's BA row is stale in five respects** (§10.1). BA moves from
   "1 unresolved quarter" to **0**, and the "resolved by detector 3 only" characterisation is
   superseded by detector 1 plus a second independent identity.
2. **PIL-3 — register the instrument coverage gap (§8.1).** `validate_calculation` is silent
   on the concept the register audits, in 2 of 2 issuers tested. This is the highest-value
   addition to the register in this pass, because every other PIL-3 finding is validated by
   the instrument whose blindness it exposes.
3. **PIL-3 — DA-24 needs a magnitude clause (§10.3).** $(1)M and $9,566M both satisfy the
   current test; only one of them changes the sign of an annual result.
4. **DA-23's mechanism should be recorded as `|x|` stripping, not inversion** (§3), with BA's
   Q1 2025 (+461M) and FY2025 (+4,281M) as the register's first two positive controls. The
   operational consequence is that the platform renders a $10,707M annual loss and a $4,281M
   annual profit in the identical all-positive form — a reader cannot tell which is which.
5. **The DA-24 exposure is dated and should be carried to any BA research use:** FY2025's
   "first profitable operating year since 2018" is a disposal gain. Any growth series that
   runs through FY2025 without an ex-disposal adjustment is inadmissible.
6. **The per-share series is quarantined across the preferred issuance** (§6.3): weighted
   shares +22.8% Q3 2024 → Q3 2025, and the platform's EPS is itself sign-stripped. This is
   an analogue of DA-28 that DA-28's IPO trigger does not catch.
7. **Tools to re-run for the residual gaps:** page-read `ba-20250331.htm` and `ba-20250630.htm`
   to upgrade §11.1–11.2 to DEMONSTRATED; `get_calculation_tree` on `sec183` for §11.6;
   `validate_calculation` on `sec183` for §11.5.
8. **§1c:** `no_single_basis_collapse` observed — five operating bases reported (§9), including
   the FY2025 +4,281 / −5,391 spread, with none collapsed.
9. **Program-level: create `skill_pins.jsonl`, or publish a `recent-quarter` hash** (§8.10).
   Four `recent-quarter` artifacts currently carry three different `skill_pin` values, one of
   them the wrong skill's hash, and nothing in the contract flags it. A pin that varies across
   artifacts pinning the same skill cannot detect a skill version change.
10. **Program-level: record the platform-vs-printed page offset** (§8.11) so a future verifier
    does not "correct" a right citation into a wrong one. The offset is 2, 2 and 6 on the three
    filings read here — not constant, so it cannot be applied as a fixed rule.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Q3 2024 income statement — total revenues 17,840; total costs and expenses (21,347); gross profit (3,507); income/(loss) from operating investments, n | [📄 BA 10-Q p.3](https://agentii.ai/v/BA/sec215/3) |
| MD&A loss-from-operations narrative — 'Loss from operations for the three months ended September 30, 2024, increased by $4,953 million'; 'Core operati | [📄 BA 10-Q p.43](https://agentii.ai/v/BA/sec215/43) **(newly surfaced)** |
| Q3 2025 income statement — total revenues 23,270; total costs and expenses (25,645); gross profit (2,375); income/(loss) from operating investments, n | [📄 BA 10-Q p.3](https://agentii.ai/v/BA/sec218/3) |
| Note 3 Digital Aviation Solutions Divestiture (as at 2025-09-30, UNCLOSED): agreement with Thoma Bravo to sell portions of the BGS segment's Digital A | [📄 BA 10-Q p.12](https://agentii.ai/v/BA/sec218/12) |
| Segment-to-consolidated Loss from Operations bridge — Q3 2025 BCA (5,353) + BDS 114 + BGS 938 = segment operating loss (4,301); unallocated items (748 | [📄 BA 10-Q p.40](https://agentii.ai/v/BA/sec218/40) |
| Unallocated items detail Q3 2025 total (748): share-based plans 11, deferred comp (70), amortization of capitalised interest (22), R&D (102), eliminat | [📄 BA 10-Q p.41](https://agentii.ai/v/BA/sec218/41) |
| BCA segment results and DELIVERIES — Q3 2025 revenues 11,094, loss from operations (5,353), operating margin (48.3)%; Q3 2024 revenues 7,443, loss fro | [📄 BA 10-Q p.46](https://agentii.ai/v/BA/sec218/46) |
| PROGRAM ACCOUNTING QUANTITIES at 2025-09-30 — 737 12,000; 767 1,263; 777 1,828; 777X 600; 787 1,900 (at 2024-12-31: 11,600 / 1,263 / 1,822 / 500 / 1,8 | [📄 BA 10-Q p.47](https://agentii.ai/v/BA/sec218/47) |
| FY2025 Consolidated Statements of Operations — total revenues 89,463 (2024: 66,517); total costs and expenses (85,174); gross profit 4,289; income fro | [📄 BA 10-K p.60](https://agentii.ai/v/BA/sec183/60) |
| Note 3 Digital Aviation Solutions Divestiture (CLOSED) — 'On October 31, 2025, we closed on the sale of portions of our BGS segment's Digital Aviation | [📄 BA 10-K p.78](https://agentii.ai/v/BA/sec183/78) |
