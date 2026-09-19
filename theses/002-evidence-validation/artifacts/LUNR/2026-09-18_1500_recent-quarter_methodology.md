---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: LUNR
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
    chosen_reading: "CONFIRMED at LUNR, from components, in-line, and promoted from CANDIDATE. The component identity RUNS — the statement-subtotal form (`gross profit − opex`) is unavailable because LUNR files no gross-profit line, but the identity is the same identity with the subtotal left unfolded, and it closes to the dollar: `Revenues − CostsAndExpenses` = −87,231,000 against a reported `OperatingIncomeLoss` of +87,231,000. Exact magnitude, opposite sign, twelve periods out of twelve. This OVERTURNS the review's premise that the detector is unavailable; the unavailability was a CONCEPT-NAME artefact (`GrossProfit` returns zero facts at LUNR, while `CostsAndExpenses` carries the data). Separately the extracted row flips THREE further lines (`NetIncomeLoss` +83,294,000 and `EarningsPerShareDiluted` +0.73 against filed (83,294) and (0.73)), so LUNR is a whole-statement instance, not an operating-line instance. `EPS × shares` was NOT used and is recorded as inadmissible, with the arithmetic of its failure shown."
  - da_id: "DA-24"
    chosen_reading: "NOT PRESENT, with positive evidence rather than absence of search. The operating line at LUNR is composed entirely of cost of revenue, affiliated cost of revenue, D&A, impairment and G&A — no disposal gain appears in it. LUNR does carry large asset-sale-shaped items (`Loss on issuance of securities` of $(68,676)K in Q1 2024, $(93,136)K in FY2024) but they sit in `Other expense, net`, demonstrably BELOW the operating line. The register's contamination vector is absent and its absence is verifiable by line position."
  - da_id: "DA-25"
    chosen_reading: "NOT PRESENT — and its premise is INVERTED at LUNR. DA-25 is registered as normalised per-unit metrics not reproducible from segment tables. LUNR has ONE operating segment and ONE reportable segment, discloses no per-unit metric of any kind, and — decisively — its segment note (Note 21) reproduces the consolidated operating loss to the dollar. Far from being non-reproducible from segment tables, the segment table is a THIRD admissible presentation of the component identity at LUNR. The issuer's normalised measure is Adjusted EBITDA and the issuer states in the same note that its primary profitability measure is the GAAP measure of Net income (loss). No per-unit figure was substituted into any filed series."
  - da_id: "DA-26"
    chosen_reading: "CONFIRMED at LUNR, and 001's recorded EXCEPTION is OVERTURNED. The row 001 labelled `Q4 2025` is the FY2025 ANNUAL column on all four lines: revenue $207.132M = FY2025 `RevenueFromContractWithCustomerExcludingAssessedTax`; operating income $87.2M = |FY2025 annual operating loss|; net income $83.3M = |FY2025 annual net loss attributable to the Company|; EPS $0.73 = |FY2025 annual EPS|. The issuer separately discloses a genuine standalone Q4 2025 (revenue $44.785M) which the extract's row does not match. 001 recorded the exception because its revenue basis was truncated (contract revenue, grant excluded) against a wrongly-remembered annual; the row did not match 001's expected annual because 001's expected annual was itself wrong."
  - da_id: "DA-27"
    chosen_reading: "CANNOT MANIFEST at LUNR, by construction — a clean negative and a control case for the DA-27 partition rather than a test of it. LUNR's fiscal year ends in December, so calendar and fiscal quarters coincide. Verified two ways: the issuer's own column headers read `Three Months Ended December 31` and `Three Months Ended June 30`, and the platform fiscal calendar returns fiscal_year_end_month 12. LUNR therefore cannot discriminate for or against DA-27 and must be excluded from its denominator."
  - da_id: "DA-28"
    chosen_reading: "PARTIAL — the share-count discontinuity is present and large, the EPS-bridge-failure symptom is ABSENT. Weighted-average shares run 36,612,270 (Q1 2024) → 61,410,250 (FY2024) → 115,426,620 (FY2025), a 3.15× change driven by warrant exercises and the Lanteris issuance, so any EPS LEVEL series spanning this window is not comparable. But the bridge itself closes exactly at both audited periods (284,309,000 / 61,410,250 = $4.6297 → $(4.63); 83,910,000 / 115,426,620 = $0.7270 → $(0.73)), so no single EPS is internally unsound. One further attribution finding: the platform's `NetIncomeLoss` tag at LUNR holds the ATTRIBUTABLE-TO-THE-COMPANY figure, not consolidated net loss (Q2 2026 tag +46,445K against consolidated $(62,841)K, reconciled exactly: 62,841 − 16,781 + 385 = 46,445), so a bare `net income` line at LUNR is ambiguous among four attribution layers."
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: "FY2025 10-K consolidated statements of operations — Total revenues 210,059 / 228,000; Cost of revenue (excl. D&A) 177,247 / 190,369; Cost of revenue (excl. D&A) - affiliated companies 23,822 / 34,862; Depreciation and amortization 3,597 / 1,859; Impairment of property and equipment — / 5,044; General and administrative expense (excl. D&A) 92,624 / 53,262; Total operating expenses 297,290 / 285,396; VERBATIM 'Operating loss | (87,231) | (57,396)'; Net loss (106,846) / (346,922); VERBATIM 'Net loss per share of Class A common stock - basic and diluted | $ (0.73) | $ (4.63)'; Weighted average shares outstanding - basic and diluted 115426620 / 61410250. NO gross-profit subtotal is presented anywhere."
    ticker: LUNR
    form_type: 10-K
    citation_id: sec59
    page_no: 61
    url: https://agentii.ai/v/LUNR/sec59/61
    located_via: read_source_pages
  - figure: "8-K Exhibit 99.1, consolidated statements of operations, Q4 AND full-year 2025 vs 2024 — the decisive DA-26 page. Three Months Ended December 31: Service revenue 43,308 / 54,662; Grant revenue 1,477 / —; Total revenues 44,785 / 54,662; Total operating expenses 77,880 / 68,059; VERBATIM 'Operating loss | (33,095) | (13,397)'. Year Ended December 31: Service revenue 207,132 / 228,000; Total revenues 210,059 / 228,000; Total operating expenses 297,290 / 285,396; VERBATIM 'Operating loss | (87,231) | (57,396)'. Also Net loss (59,655) / (165,135) / (106,846) / (346,922); Net loss attributable to redeemable noncontrolling interest (20,115) / (17,003) / (25,059) / (67,004); Net income attributable to noncontrolling interest 335 / 1,066 / 1,507 / 3,495; Net loss attributable to the Company (39,875) / (149,198) / (83,294) / (283,413); Less: Preferred dividends (160) / (145) / (616) / (896); Net loss attributable to Class A common shareholders (40,035) / (149,343) / (83,910) / (284,309)"
    ticker: LUNR
    form_type: 8-K
    citation_id: sec51
    page_no: 9
    url: https://agentii.ai/v/LUNR/sec51/9
    located_via: read_source_pages
  - figure: "8-K Exhibit 99.1 financial highlights — VERBATIM 'Achieved $44.8 million of revenue in Q4 driven primarily by Commercial Lunar Payload Services (CLPS), Omnibus Multidiscipline Engineering Services III (OMES III), and Near Space Network Services (NSNS)' and VERBATIM 'Continued drive towards profitability with 19% positive gross margin in Q4, representing margin improvement throughout 2025'; backlog approximately $943 million; 2026 outlook full-year revenue $900 million - $1 billion. The 19% is reproducible to the percentage point from the statements on the cost-of-revenue-only basis: (44,785 − (31,242 + 5,055)) / 44,785 = 18.95%"
    ticker: LUNR
    form_type: 8-K
    citation_id: sec51
    page_no: 4
    url: https://agentii.ai/v/LUNR/sec51/4
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q condensed consolidated statements of operations — Product revenue 166,735 / — / 308,289 / —; Service revenue 36,677 / 50,313 / 78,753 / 112,837; Grant revenue 2,756 / — / 5,856 / —; Total revenues 206,168 / 50,313 / 392,898 / 112,837; Total cost of revenues 170,302 / 62,156 / 326,925 / 118,003; Depreciation and amortization 14,927 / 752 / 27,975 / 1,375; Research and development 7,729 / 461 / 13,318 / 1,372; General and administrative expense 60,346 / 15,584 / 111,017 / 30,804; Total operating expenses 253,304 / 78,953 / 479,235 / 151,554; VERBATIM 'Operating loss | (47,136) | (28,640) | (86,337) | (38,717)'; Net loss (62,841) / (38,206) / (115,369) / (37,231); Net loss attributable to the Company (46,445) / (25,181) / (83,832) / (36,577); VERBATIM 'Net loss per share of Class A common stock - basic and diluted | $ (0.29) | $ (0.22) | $ (0.54) | $ (0.33)'"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 8
    url: https://agentii.ai/v/LUNR/sec76/8
    located_via: read_source_pages
  - figure: "Q2 2026 10-Q Note 21 Segment Information — VERBATIM 'The Company operates in one operating segment and one reportable segment underpinned by three core pillars (delivery services, data transmission services, and infrastructure as a service)' and VERBATIM 'Our CODM reviews and evaluates consolidated Net income (loss), a U.S. GAAP measure, and Adjusted Earnings before Interest, Taxes, Depreciation, and Amortization (\"Adjusted EBITDA\"), a non-GAAP measure, and Total assets' and VERBATIM 'our primary profitability measure is the GAAP measure of Net income (loss)'. Segment table — Revenues 206,168 / 50,313 / 392,898 / 112,837; Cost of revenues 170,302 / 62,156 / 326,925 / 118,003; D&A 14,927 / 752 / 27,975 / 1,375; R&D 7,729 / 461 / 13,318 / 1,372; G&A 60,346 / 15,584 / 111,017 / 30,804; VERBATIM 'Operating loss | (47,136) | (28,640) | (86,337) | (38,717)'; Net loss (62,841) / (38,206) / (115,369) / (37,231). This is a THIRD admissible presentation of the component identity and it closes exactly at every column"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 43
    url: https://agentii.ai/v/LUNR/sec76/43
    located_via: read_source_pages
  - figure: "Q1 2024 10-Q condensed consolidated statements of operations — Revenue 73,068 / 18,236; Cost of revenue (excluding depreciation) 60,911 / 23,126; Depreciation 414 / 296; General and administrative expense (excluding depreciation) 17,143 / 8,777; Total operating expenses 78,468 / 32,199; VERBATIM 'Operating loss | (5,400) | (13,963)'; Total other expense, net (115,256) / (6,269) including 'Loss on issuance of securities | (68,676) | —' positioned BELOW the operating line; Loss before income taxes (120,656) / (20,232); Net loss (120,656) / (23,447); Net loss attributable to the Company (98,337) / (9,360); Net loss attributable to Class A common shareholders $ (98,808) / $ (9,688); VERBATIM 'Net loss per share of Class A common stock - basic and diluted | $ (2.70) | $ (0.64)'; Weighted average shares outstanding - basic and diluted 36612270 / 15224378. THIS IS THE PAGE THAT OVERTURNS 001's PLAUSIBILITY BENCHMARK: the filing prints 'Operating loss (5,400)', not operating income of $5.4M"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec67
    page_no: 7
    url: https://agentii.ai/v/LUNR/sec67/7
    located_via: read_source_pages
  - figure: "NEGATIVE RESULT, located — `search_keyword_in_source(LUNR, sec76, 'gain on sale')` returns ZERO pages in the Q2 2026 10-Q. Combined with the line-position evidence above, DA-24's contamination vector (a disposal gain inside the operating line) is absent, and absence was tested rather than assumed."
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 8
    url: https://agentii.ai/v/LUNR/sec76/8
    located_via: search_keyword_in_source
---

# LUNR — Recent Quarter, Defect Census (PIL-3)

**Subject of validation**: the `001-technology-baseline` artifact
`artifacts/LUNR/2026-09-18_1239_operational-kpi_methodology.md`, whose table records
**LUNR Q4 2025 revenue $207.1M, operating income $87.2M, operating margin 42.1%**, grades
LUNR a **DA-23 CANDIDATE**, and records **DA-26 as an exception** — "the first issuer
examined where DA-26 does not clearly appear."

**Pin note on `skill_pin`.** This artifact's `skill_pin` is recorded as **UNRESOLVED, not
as a hash**, and the reason is a verified gap rather than a preference. 001's `reproduce.md`
resolved `skill_pin` on 2026-09-18 with real per-skill content hashes
(`theses/001-technology-baseline/reproduce.md:27-40`) — but the table holds **six** skills
(operational-kpi `0730fd170124`, unit-economics `e87ee63269a2`, secular-trends
`e6b41dbb2426`, supply-chain `8cb3ac1de486`, competitive `826995c722a4`, risk
`953fc5d396e7`) and **`recent-quarter` is not among them.** The mechanism for the residue
is stated in the same file: *"Remaining skills hash on first use and are **appended** to
`skill_pins.jsonl` (Q57 — never overwritten)."* **That ledger does not exist in the repo**
(`find . -name skill_pins.jsonl` returns nothing), so the append never happened and
`dispatch.skill_version_hash()` — documented as unreachable from this session — cannot
supply it. The one prior `recent-quarter` artifact
(`theses/001-technology-baseline/artifacts/SPCX/2026-09-18_2359_recent-quarter_methodology.md`)
carries `registry-1.0.0`, which is the **superseded whole-registry proxy** that
`reproduce.md:29` explicitly replaced; copying it forward would propagate a value the
corpus has already retired. So the pin is emitted as an explicit unresolved marker: a pin
that cannot be resolved is precisely the class of thing this thesis exists to surface, and
fabricating a hash to satisfy a schema would be the same failure the register catalogues.

**This artifact's headline, stated first because it inverts the premise it was assigned:
the 42.1% is not a genuine one-off and it is not an artefact of a missing detector. It is
the absolute value of LUNR's FY2025 *annual* operating margin, mislabelled as a quarter.
The one reliable detector was never unavailable — all four registered detectors run at
LUNR, and two of them flag this figure.**

---

## 0. What was asked, and what the two competing statements actually were

The task brief carried two assertions that this artifact had to reconcile, and **both
resolve as misattributions** — recorded here explicitly because the resolution is the
answer, not a preliminary to it.

**(a) "001's Phase 2 artifact found LUNR at −34.888M → +34.888M (the cleanest DA-23
instance)."**

That figure is **PL (Planet Labs), not LUNR.** Verified at three locations:

| Location | Text |
|---|---|
| `theses/001-technology-baseline/artifacts/PL/2026-09-18_1239_operational-kpi_methodology.md:37` | `gross profit - opex = -$34.888M     <- arithmetic` / `XBRL OperatingIncomeLoss = +$34.888M  <- reported` |
| `constitution.md:841` | "**PL (−34.888 → +34.888 — the cleanest instance, an exact component match on directly-available quarterly figures)**" |
| `theses/005-tier1-space-pure-plays/spec.md:67` | "**PL Q2 loss $(34.888)M** — gross profit $50.401M − opex $85.289M, the cleanest DA-23 instance \| Resolved by 001" |

LUNR's own 001 artifact contains no such figure. **So the reconciliation is: PL is the
resolved quarter; LUNR was never resolved at component level by 001 — it was left a
CANDIDATE and carried forward. The brief conflated the two issuers' 001 artifacts.** The
resolution of one therefore does **not** constrain the other: PL's clean instance is on a
different issuer with a filed gross-profit line, and says nothing about LUNR's detector
availability.

**(b) "No quarterly gross-profit line exists, so the component identity CANNOT RUN."**

True of the *subtotal* and false of the *identity*. There is no gross-profit line — that
is confirmed and re-confirmed below. But the identity does not require the subtotal; it
requires the two sides of it, and LUNR tags and prints both. **The claim "no detector can
run" was reached by looking up a concept name (`GrossProfit`), finding zero facts, and
inferring detector failure from concept absence.** That inference is the defect this
artifact registers.

---

## 1. The 42.1%, fully decomposed

### 1.1 The arithmetic identifies the extraction basis exactly

Reproducing 001's own margin column from platform facts reproduces it to the displayed
digit, which identifies what the extract computed:

| 001's row | Revenue shown | Oper. income shown | 001 margin | Recomputed | Basis |
|---|---:|---:|---:|---:|---|
| Q2 2026 | $203.4M | $47.1M | 23.2% | 47.136 / 203.412 = **23.17%** | contract revenue, grant excluded |
| Q1 2026 | $183.6M | $39.2M | 21.3% | 39.201 / 183.630 = **21.35%** | contract revenue, grant excluded |
| "Q4 2025" | $207.1M | $87.2M | **42.1%** | 87.231 / 207.132 = **42.11%** | **FY2025 annual** contract revenue |

Three for three. The extraction basis is therefore
`|OperatingIncomeLoss| ÷ RevenueFromContractWithCustomerExcludingAssessedTax` — the
absolute value of operating income over **contract revenue only**, grant revenue removed
(a $1.45–5.86M/period line).

**The grant-revenue truncation is itself a finding, and it is not one of the six
registered defects.** It is a *basis* defect that no DA covers, and it is the specific
reason 001's row failed 001's own annual-equality test — see §4.

### 1.2 The row is the annual column, on all four lines

| 001's "Q4 2025" line | Value shown | What it is in the filing | True value | Defect |
|---|---:|---|---:|---|
| Revenue | $207.1M | FY2025 `RevenueFromContractWithCustomerExcludingAssessedTax` (annual) | — | DA-26 + basis |
| Operating income | +$87.2M | FY2025 `OperatingIncomeLoss` (annual) | **−$87.231M** | **DA-23 + DA-26** |
| Net income | +$83.3M | FY2025 `NetIncomeLoss` = attributable to the Company (annual) | **−$83.294M** | **DA-23 + DA-26** |
| EPS | +$0.73 | FY2025 `EarningsPerShareDiluted` (annual) | **−$0.73** | **DA-23 + DA-26** |

The issuer's own FY2025 statements print the sign four times over: "Operating loss
(87,231)", "Net loss (106,846)", "Net loss attributable to the Company (83,294)", "Net
loss per share of Class A common stock - basic and diluted $ (0.73)"
[📄 LUNR 10-K p.61](https://agentii.ai/v/LUNR/sec59/61)
[📄 LUNR 8-K p.9](https://agentii.ai/v/LUNR/sec51/9).

**And the issuer discloses a genuine standalone Q4 2025, which the extract's row does not
match.** The Q4 column of the same 8-K page reads Total revenues **$44,785K** and
**"Operating loss (33,095)"** [📄 LUNR 8-K p.9](https://agentii.ai/v/LUNR/sec51/9); the
earnings release headline reads **"$44.8 million of revenue in Q4"**
[📄 LUNR 8-K p.4](https://agentii.ai/v/LUNR/sec51/4). The extract says $207.1M. It is not
a rounding difference — it is a different period.

So the true LUNR margin series is:

| Period | Revenue | Operating result | **True margin** |
|---|---:|---:|---:|
| Q4 2025 | $44.785M | **$(33.095)M** | **−73.9%** |
| Q1 2026 | $186.730M | $(39.201)M | −21.0% |
| Q2 2026 | $206.168M | $(47.136)M | −22.9% |
| FY2025 | $210.059M | $(87.231)M | **−41.5%** |

**There is no profitable period anywhere in the extract window.** The 42.1% is the
absolute value of the FY2025 annual figure, and the real number for that year is a
41.5% *loss*; the real number for the quarter 001 attributed it to is a 73.9% *loss*.

---

## 2. The component identity, in-line, and it runs

### 2.1 Form 1 — the filed statement (source-verified)

```
LUNR FY2025, as printed by the issuer (sec51 p.9 / sec59 p.61), $ thousands

  Total revenues                                    210,059
  Operating expenses:
    Cost of revenue (excl. D&A)                     177,247
    Cost of revenue (excl. D&A) - affiliated         23,822
    Depreciation and amortization                     3,597
    Impairment of property and equipment                 —
    General and administrative (excl. D&A)           92,624
                                                   ────────
  Total operating expenses                          297,290
                                                   ────────
  Operating loss                                   (87,231)   <- printed with its sign
  ─────────────────────────────────────────────────────────
  XBRL OperatingIncomeLoss (FY2025, platform)     +87,231,000  <- SIGN STRIPPED
```

Sub-total check: `177,247 + 23,822 + 3,597 + 0 + 92,624 = 297,290` ✓ closes on the filed
total. Identity check: `210,059 − 297,290 = −87,231` ✓ closes on the filed loss.

### 2.2 Form 2 — two platform aggregates, no gross-profit line required

This is the form that matters for DA-23, because it needs **no subtotal**:

```
|computed| == |reported|, opposite signs — run on platform facts

  us-gaap:Revenues          (FY2025)  =  +210,059,000
  us-gaap:CostsAndExpenses  (FY2025)  =  +297,290,000
  ───────────────────────────────────────────────────
  Revenues − CostsAndExpenses         =   −87,231,000   <- computed
  XBRL OperatingIncomeLoss  (FY2025)  =   +87,231,000   <- reported
  ───────────────────────────────────────────────────
  magnitudes equal, signs opposite    →  DA-23 CONFIRMED
```

Run across every period the platform carries, it closes **twelve out of twelve**:

| Period | Revenues | CostsAndExpenses | Identity | Reported | Disposition |
|---|---:|---:|---:|---:|---|
| Q1 2024 | 73,219,000 | 75,994,000 | **−2,775** | +2,775,000 | **STRIPPED** |
| Q2 2024 | 41,641,000 | 69,141,000 | **−27,500** | +27,500,000 | **STRIPPED** |
| H1 2024 | 114,860,000 | 145,135,000 | **−30,275** | +30,275,000 | **STRIPPED** |
| Q3 2024 | 58,478,000 | 72,202,000 | **−13,724** | +13,724,000 | **STRIPPED** |
| FY2024 | 228,000,000 | 285,396,000 | **−57,396** | +57,396,000 | **STRIPPED** |
| Q1 2025 | 62,524,000 | 72,601,000 | **−10,077** | +10,077,000 | **STRIPPED** |
| Q2 2025 | 50,313,000 | 78,953,000 | **−28,640** | +28,640,000 | **STRIPPED** |
| Q3 2025 | 52,437,000 | 67,856,000 | **−15,419** | +15,419,000 | **STRIPPED** |
| FY2025 | 210,059,000 | 297,290,000 | **−87,231** | +87,231,000 | **STRIPPED** |
| Q1 2026 | 186,730,000 | 225,931,000 | **−39,201** | +39,201,000 | **STRIPPED** |
| Q2 2026 | 206,168,000 | 253,304,000 | **−47,136** | +47,136,000 | **STRIPPED** |
| H1 2026 | 392,898,000 | 479,235,000 | **−86,337** | +86,337,000 | **STRIPPED** |

**Twelve for twelve, exact magnitude, opposite sign, zero exceptions.** Cumulative
consistency was checked too: FY2025 `−87,231` minus 9M 2025 `−54,136` = `−33,095`, which
equals the issuer's independently printed Q4 2025 "Operating loss (33,095)" to the
dollar — so the identity holds both cumulatively and on the standalone quarter.

**Basis note on the 2024 rows, disclosed because it is not self-evident.** The Q1/Q2/H1
2024 figures above are the **restated** values carried in the FY2024 10-K; the Q1 2024 and
Q2 2024 10-Qs as originally filed print `−5,400` and `−28,174` (see §8.3). The restated
set is the one that closes cumulatively to the dollar — `73,219 + 41,641 + 58,478 +
54,662 = 228,000` exactly, and `75,994 + 69,141 + 72,202 + 68,059 = 285,396` exactly —
while the as-filed set does **not** (`227,616` against a filed `228,000`). **Both sets are
losses and both are stripped**, so the DA-23 disposition is identical either way; the
restated set is shown because it is the one the platform carries and the only one that is
internally additive.

**Disposition: DA-23 is CONFIRMED at LUNR and the CANDIDATE status is withdrawn.** LUNR
is flip instance #7, after SPCX, YSS, RKLB, FLY, BA and PL. The census reads **7 of 7
loss-making stripped**, and LUNR contributes **no profitable quarter** to the 19-of-19
clean positive control.

### 2.3 Form 3 — the segment note (a third admissible presentation)

Note 21 reproduces the same operating loss with the cost lines unfolded
[📄 LUNR 10-Q p.43](https://agentii.ai/v/LUNR/sec76/43):

```
Q2 2026: 206,168 − (170,302 + 14,927 + 7,729 + 60,346) = −47,136  ✓ exact
H1 2026: 392,898 − (326,925 + 27,975 + 13,318 + 111,017) = −86,337 ✓ exact
Q2 2025:  50,313 − ( 62,156 +    752 +    461 +  15,584) = −28,640 ✓ exact
H1 2025: 112,837 − (118,003 +  1,375 +  1,372 +  30,804) = −38,717 ✓ exact
```

### 2.4 What CANNOT be run, and it is not the identity

**The statement-subtotal form (`gross profit − opex`) is genuinely unavailable.** LUNR
files no gross-profit subtotal: `search_xbrl_facts(LUNR, GrossProfit)` returns **zero
facts**, and the filed statement runs Revenues → Operating expenses → Operating loss with
no intervening subtotal. `CostOfRevenue` and `CostOfGoodsAndServicesSold` also return
zero.

**This is the concept-name trap, and it is the specific mechanism of the false
"detector unavailable" finding.** The absence of `GrossProfit` was read as the absence of
the detector. The data is present under a different name — `CostsAndExpenses` carries the
operating-expense total, and the cost-of-revenue lines are individually tagged and
printed. `GrossProfit` is not a platform gap: it exists for 87 other tickers. It is an
issuer-specific presentation choice.

**The correct lesson for the universe-wide census**: *"detector unavailable" is a claim
that must be tested by attempting the detector, not inferred from the absence of a
concept name.* A concept-name lookup produces false unavailability; the correct
unavailability class remains the coverage hole where `OperatingIncomeLoss` is **absent or
segment-only (MRK, BMY, WWD)** — an absence of the *subject*, not of a *name*. **LUNR is
not in that class**, despite the register having grouped it with the detector-availability
cases.

---

## 3. The gross-profit bound is constructible at LUNR — and the extracted value FAILS it

The register's second detector is the bound that caught VOYG: *operating income can never
exceed gross profit, at any sign.* At LUNR the bound was believed untestable for the same
reason as the identity. It is testable.

**Construction, validated against the issuer's own disclosure.** LUNR discloses a gross
margin in its earnings release — **"19% positive gross margin in Q4"**
[📄 LUNR 8-K p.4](https://agentii.ai/v/LUNR/sec51/4). The cost-of-revenue-only basis
reproduces that from the statements to the percentage point:

```
Q4 2025:  revenue 44,785 − (cost of revenue 31,242 + affiliated 5,055) = 8,488
          8,488 / 44,785 = 18.95%   ≈  the issuer's own "19%"   ✓ basis validated

FY2025:   revenue 210,059 − (177,247 + 23,822) = 8,990
```

**The bound test:**

```
bound:  operating income  <=  gross profit, at any sign

   extracted "Q4 2025" / FY2025 operating income      +87,231
   constructed FY2025 gross profit                      8,990
   ─────────────────────────────────────────────────────────
   VIOLATED by                                         78,241   (9.7x gross profit)

   control — the TRUE value:
   actual FY2025 operating loss                       −87,231  <=  8,990   ✓ bound holds
   actual Q4 2025 operating loss                      −33,095  <=  8,488   ✓ bound holds
```

**Detector 2 runs at LUNR and it flags.** The bound holds on the truth and fails on the
extraction — which is exactly the VOYG pattern, one register entry over.

---

## 4. DA-26 and DA-27 — checked first, as instructed

### DA-26 — CONFIRMED, and 001's recorded exception is OVERTURNED

The brief's instruction was to check DA-26 first because "a 42.1% margin on one quarter is
exactly what a mislabelled annual row looks like." It is. §1.2 shows all four lines of
the row are FY2025 annual magnitudes.

**Why 001 recorded the exception, and why that reasoning fails.** 001's artifact states:
*"LUNR's FY2025 annual was ~$450M, so this row is ambiguous — it does not equal the
annual"*, and separately *"LUNR's FY2025 revenue across four quarters ($62.5M + $50.3M +
$51.0M + $207.1M) = $370.9M, and its reported annual is not in the extract."*

Both statements fail on their own terms:

1. **The annual was in the extract.** LUNR's FY2025 annual revenue is **$210,059K**
   — printed at [📄 LUNR 8-K p.9](https://agentii.ai/v/LUNR/sec51/9) and
   [📄 LUNR 10-K p.61](https://agentii.ai/v/LUNR/sec59/61). It is **not "~$450M."** The
   $450M figure appears nowhere in LUNR's filings. 001 compared the row against a
   remembered number that was approximately double the real one, so of course the row
   "did not equal the annual" — it was being compared to the wrong annual.
2. **The four-quarter sum double-counts the annual.** 001's own list includes the Q4 row
   *as* a quarter. Since the Q4 row *is* the annual, the sum adds the annual to the three
   real quarters and gets $370.9M — a number that can only arise from the defect. 001
   used the artefact to reason about the artefact.
3. **The row's revenue is on a truncated basis**, contract revenue only. On Total
   revenues the Q2 2026 row is $206.168M, not $203.4M, and the FY2025 row is $210.059M,
   not $207.1M. The basis truncation is what made the row fail an equality test against a
   total-revenue annual.

**The competing hypothesis — "a genuine one-off" — is refuted by the issuer's own Q4
column.** 001 offered it explicitly: *"The Q4 row may simply be a genuine strong quarter —
LUNR had a major lunar mission in that period."* The issuer discloses that quarter, and it
was not strong. Standalone Q4 2025 is the **weakest** quarter of 2025 by revenue
(**$44.785M** against $52.437M in Q3) and its operating margin is **−73.9%** — the worst
of the year, not the best [📄 LUNR 8-K p.9](https://agentii.ai/v/LUNR/sec51/9). The
lunar-mission period is real, and it is a *revenue-incumbent, margin-negative* quarter.
**So the three candidate explanations resolve cleanly: not a genuine one-off, not DA-27
(§4.2), and not merely an extraction artefact — a mislabelled annual (DA-26) with a
sign strip (DA-23) on top of a basis truncation (§9.5).**

**001 also mislabelled an annual as a quarter in the very sentence where it recorded the
DA-26 exception.** It states LUNR "reported **net losses** of $(98.3)M in Q1 2024 and
**$(283.4)M in Q4 2024**." The $283.4M is the **FY2024 annual** net loss attributable to
the Company — `(283,413)` at [📄 LUNR 8-K p.9](https://agentii.ai/v/LUNR/sec51/9) — not a
Q4 2024 figure. The actual Q4 2024 attributable net loss is `(149,198)`. (The $(98.3)M
figure for Q1 2024 is correctly stated: *"Net loss attributable to the Company (98,337)"*
at [📄 LUNR 10-Q p.7](https://agentii.ai/v/LUNR/sec67/7).)

**So LUNR is not an exception to DA-26. It is an instance — recorded as an exception by
an artifact that was applying the same defect to the neighbouring sentence.** DA-26's
"universal — 19 of 19" coverage is restored at LUNR, and `001-technology-baseline/thesis.md:230`
("**Exception recorded**: LUNR's Q4 row does *not* equal its annual, the first issuer
where the pattern does not clearly appear") is corrected by this artifact. Per the
frozen-001 policy, 001 is not rewritten; the correction is recorded here and cross-cited
by location.

### DA-27 — CANNOT MANIFEST, and LUNR is a control case, not a test

LUNR's fiscal year ends in December, so its fiscal quarters are calendar quarters and the
calendar-derived labelling defect has no room to operate. Verified two independent ways:

- The issuer's own column headers read **"Three Months Ended December 31"** against
  "Year Ended December 31" [📄 LUNR 8-K p.9](https://agentii.ai/v/LUNR/sec51/9), and
  **"three months ended June 30"** against "six months ended June 30"
  [📄 LUNR 10-Q p.8](https://agentii.ai/v/LUNR/sec76/8). Calendar and fiscal columns are
  the same columns.
- The platform fiscal calendar returns `fiscal_year_end_month: 12`.

**Recorded as a clean negative.** LUNR must be excluded from DA-27's denominator rather
than counted as a passing case: an issuer that cannot exhibit a defect cannot provide
evidence about it. This is worth stating because DA-27's registered coverage is "n = 4 of
4 … partitions the population perfectly by fiscal year-end" — LUNR is a member of the
complement class, and the complement class has now been examined at least once.

---

## 5. The remaining register — DA-24, DA-25, DA-28

### DA-24 — NOT PRESENT, with positive evidence

`search_keyword_in_source(LUNR, sec76, "gain on sale")` returns **zero pages**. More
usefully, the operating line's composition is verifiable and contains no disposal item:
cost of revenue, affiliated cost of revenue, D&A, impairment, G&A — the full set, at
[📄 LUNR 8-K p.9](https://agentii.ai/v/LUNR/sec51/9).

LUNR *does* carry large asset-sale-shaped items, and their **position** is the evidence:
`Loss on issuance of securities` of `$(68,676)K` (Q1 2024) and `$(93,136)K` (FY2024) sits
inside **"Other expense, net"**, below the operating line
[📄 LUNR 10-Q p.7](https://agentii.ai/v/LUNR/sec67/7). The register's contamination
vector — a disposal gain *inflating the operating line* — is absent, and it fails on line
position rather than on not-being-found.

### DA-25 — NOT PRESENT, and its premise is inverted here

DA-25 is registered at RKLB as: *the disclosed `revenue per launch` implies 51.6% GM; the
audited segment table implies 42.9%.* Its premise is that a normalised per-unit metric is
**not reproducible from the segment tables**. At LUNR the segment table is the
best-behaved thing in the filing:

- **One operating segment, one reportable segment** — verbatim: *"The Company operates in
  one operating segment and one reportable segment underpinned by three core pillars
  (delivery services, data transmission services, and infrastructure as a service)"*
  [📄 LUNR 10-Q p.43](https://agentii.ai/v/LUNR/sec76/43).
- **No per-unit metric of any kind was located** — no $/kg, no $/mission, no $/spacecraft.
- The normalised measure the issuer does disclose is **Adjusted EBITDA**, and the same
  note discloses that *"our primary profitability measure is the GAAP measure of Net
  income (loss)"* — the non-GAAP figure is not substituted for the GAAP one by the issuer
  itself.
- Decisively: §2.3 shows the segment table **reproduces the consolidated operating loss
  exactly.** The premise — non-reproducibility from segment tables — does not merely fail
  to apply; the segment table is an *additional* detector source, not a degraded one.

### DA-28 — PARTIAL: the discontinuity is real, the bridge-failure symptom is absent

DA-28 is registered at HAWK as four non-agreeing share counts with an EPS bridge failing
by 72%. At LUNR:

| Period | Weighted-average shares | Source |
|---|---:|---|
| Q1 2024 | 36,612,270 | [📄 LUNR 10-Q p.7](https://agentii.ai/v/LUNR/sec67/7) |
| FY2024 | 61,410,250 | [📄 LUNR 10-K p.61](https://agentii.ai/v/LUNR/sec59/61) |
| FY2025 | 115,426,620 | [📄 LUNR 10-K p.61](https://agentii.ai/v/LUNR/sec59/61) |

A **3.15× change in under two years**, driven by warrant exercises and the Lanteris
issuance [📄 LUNR 10-Q p.7](https://agentii.ai/v/LUNR/sec67/7) documents the warrant
activity. So the *discontinuity* is present and large: **any EPS-level series spanning
this window is not comparable.**

But the **bridge itself closes exactly** at both audited periods:

```
FY2024:  284,309,000 / 61,410,250  = $4.6297  ->  reported $(4.63)   ✓
FY2025:   83,910,000 / 115,426,620 = $0.7270  ->  reported $(0.73)   ✓
```

Both numerators are "Net loss attributable to Class A common shareholders"
[📄 LUNR 8-K p.9](https://agentii.ai/v/LUNR/sec51/9). **No single EPS is internally
unsound, so DA-28's discriminating symptom does not fire.** One attribution finding is
recorded rather than a defect: the platform's `NetIncomeLoss` tag at LUNR holds the
**attributable-to-the-Company** figure, not consolidated net loss (Q2 2026 tag
`+46,445,000` against a consolidated `$(62,841)K`, reconciled exactly:
`62,841 − 16,781 + 385 = 46,445`). A bare "net income" line at LUNR is therefore
ambiguous among four attribution layers — consolidated → less RNC-I → plus NCI →
attributable to the Company → less preferred dividends → attributable to Class A.

---

## 6. The detector-availability finding — the core deliverable

**All four registered detectors run at LUNR. Two of them flag this figure. None is
unavailable.** The register's four detectors, in its own descending-reliability order,
with LUNR disposition:

| # | Detector (register order) | Status at LUNR | Result |
|---|---|---|---|
| **D1** | **Component identity** — "the only fully reliable test" | **RUNS.** Not in the subtotal form 001 assumed; in the two-aggregate and segment-note forms. | **FLAGS** — 12/12 periods, exact magnitude, opposite sign |
| **D2** | **Gross-profit bound** — OI ≤ GP at any sign | **RUNS.** GP constructible from the cost-of-revenue lines; basis validated against the issuer's own "19%" disclosure. | **FLAGS** — exceeds GP by 9.7× on the extracted value; bound holds on the true value |
| **D3** | **Below-the-line plausibility bridge** — used at BA and RKLB | **RUNS but DOES NOT DISCRIMINATE** | no flag — see below |
| **D4** | **Margin plausibility vs industry norms** — "weakest", the detector 001 actually used at LUNR | **RUNS, with a corrupted comparator** | fired, right verdict, wrong reason |

**D3's non-discrimination is structural and worth registering.** The bridge tests whether
the gap between the operating line and the net line is plausible. LUNR's extracted row
shows `+87.2M → +83.3M`, a gap of **$3.9M**. The true figures are `−87.231 → −83.294`, a
gap of **the same $3.937M**, because a *uniform* sign strip preserves the difference
between two stripped endpoints. The extracted gap is small and entirely plausible, so the
bridge returns clean — **on a figure that is wrong by $174.5M in aggregate.** D3 is
therefore **transcription-preserving and sign-blind by construction**: it fires only when
a uniform strip produces an *implausible magnitude* (as at RKLB, where the strip implied
$106.772M of unavailable below-the-line income), not when it produces a plausible one.
This is a limitation of D3 that the register does not currently record, and it is the
mechanism by which a whole-statement strip can pass a bridge test.

**D4's comparator was itself a sign-stripped figure — at the same issuer.** 001's entire
DA-23 case at LUNR rested on this sentence, verbatim from its artifact:

> "No company in this sector — none — earns that at the operating line. **LUNR's own 2024
> quarters ran at 7.4%** (Q1 2024, $5.4M on $73.1M), which *is* plausible."

The issuer's Q1 2024 filing prints **"Operating loss (5,400)"** against Total operating
expenses of 78,468 — and `73,068 − 78,468 = −5,400` closes the identity exactly
[📄 LUNR 10-Q p.7](https://agentii.ai/v/LUNR/sec67/7). **The "plausible 7.4% positive" is
a sign-stripped −7.4% loss.** Corroborating: 001's own DV list for Q1 2024 recorded the
net loss correctly as negative `$(98.337)M` — the same page — so **001's table holds a
negative net loss and a positive operating income for the same company-quarter**, which
is internally impossible.

**So the verdict was right and every input to it was wrong.** 001 concluded "42.1% is not
credible" (correct), by comparing it against "LUNR's 2024 quarters ran at 7.4%"
(sign-stripped loss), using a detector the register itself lists as the weakest, on a
comparator drawn from the same defect class. The conclusion survives; the evidence chain
does not. **D4 produced a true positive for a false reason, which means it cannot be
trusted as a detector — a false negative from the same instrument would have looked
identical.**

**Instrument check — `validate_calculation`, and what it does and does not show.**
Run against the FY2025 10-K (`0001628280-26-019865`) it returns **15 fail / 8 pass /
1 warn**, matching the rate the constitution registers for a normal filing. Consistent
with the standing instrument rule, the `status` column is not read here. The two
`computed` vs `reported` pairs that matter:

| Concept | computed | reported | Reading |
|---|---:|---:|---|
| `OperatingIncomeLoss` FY2025 | 122,828,000 | 87,231,000 | **same sign — the instrument does NOT flag the flip.** The magnitudes differ by 35.597M, so the arc set is aggregating arcs the concept does not aggregate. Available, but not load-bearing as a sign test. |
| `NetCashProvidedByUsedInInvestingActivities` | −56,580,000 | +56,580,000 | **pure sign inversion, magnitudes identical** — the arc-selection artefact VRT documented, reproduced at LUNR |
| `GeneralAndAdministrativeExpense` FY2025 | 92,624,000 | 92,624,000 | pass — and 92,624 is exactly the G&A line in §2.1, so the arc set is reading the right line |

**The instrument's computed column is a different quantity from the filed one, so it must
not be used as a substitute for the identity.** Two further instrument data points: its
`Revenues` pair is `computed 3,927,000` vs `reported 210,059,000` (a 206M artefact of a
single arc), and its `NetIncomeLoss` pair is `computed −23,722,000` vs
`reported +83,294,000` — the computed side carrying a negative sign against a positive
reported fact, which is the strip showing through from the other direction.

---

## 7. `EPS × shares` — inadmissible, and here is the arithmetic of its failure

The register rules this test inadmissible (it passes on both sides of a flip at RKLB, FLY
and VOYG). LUNR supplies the cleanest demonstration of *why*, because it has an exact,
auditable EPS bridge:

```
LUNR FY2025:   $0.73  x  115,426,620 shares  =  $84.26M

  compare to the extract's own "Q4 2025" operating income     $87.2M   -> 3.4% apart
  compare to the filed net loss attributable to Class A       $83.91M  -> exact
```

**Applied to the extract's own row, `EPS × shares` returns $84.26M — within 3.4% of the
row's $87.2M operating income, and it therefore "passes."** The row is the FY2025 annual,
mislabelled as a quarter, with all three signed lines stripped. A test that certifies it
agrees with itself has no discriminating power at all.

The structural reason it can never be admissible: `EPS × shares` reconstructs **net loss
attributable to Class A common shareholders** — five steps and four attribution layers
below the operating line (other expense $(15,653)K, tax $(3,962)K, RNC-I $(25,059)K,
NCI $1,507K, preferred dividends $(616)K in FY2025 alone). It is not a proxy for
operating income and cannot stand in for the component identity.

---

## 8. What could NOT be verified

Recorded as non-verifications, not as defects, and none of them is load-bearing for the
findings above.

1. **The 8-K's Adjusted EBITDA figures are not page-verified.** Q4 2025 Adjusted EBITDA
   $(19,077)K and FY2025 $(64,243)K appear in the outline of
   [📄 LUNR 8-K](https://agentii.ai/v/LUNR/sec51/4) but the reconciliation page was not
   read, so no Adjusted EBITDA figure is asserted in this artifact. The *existence* of
   Adjusted EBITDA as the CODM's non-GAAP measure is asserted, and that is page-verified
   at [📄 LUNR 10-Q p.43](https://agentii.ai/v/LUNR/sec76/43).
2. **Q1 2026 was not read at page level.** Its Revenues and CostsAndExpenses platform
   facts are used in §2.2 and close the identity, but no page citation for Q1 2026 is
   given. The figures are corroborated by 001's independently-recorded 21.3% margin,
   which §1.1 reproduces to the digit.
3. **The Q1 2024 restatement is observed but not explained.** The Q1 2024 10-Q reports
   Q1 2024 operating loss `$(5,400)` on total opex 78,468; the FY2024 10-K carries Q1 2024
   as `−2,775` on opex 75,994 — a $2.625M restatement, with Q2 2024 restated in the same
   direction (`−28,174` → `−27,500`). Both readings are losses and both are stripped, so
   the DA-23 finding is unaffected, but **the restatement's cause was not investigated**
   and it is listed so it is not assumed away. The FY2024 H1 figure `−30,275` is
   independently confirmed: `FY2024 −57,396` less Q3 `−13,724` less Q4 `−13,397` (the
   last printed at [📄 LUNR 8-K p.9](https://agentii.ai/v/LUNR/sec51/9)) `= −30,275`.
4. **DA-24 was tested by keyword and by line position, not by reading every note.**
   Business-combination accounting for KinetX and Lanteris could in principle generate a
   bargain-purchase gain; no such item is in the operating line of any period read, and
   the keyword test returned zero, but the acquisition notes were not read in full.
5. **The `sec76` citation-ID collision with the specification is unresolved.** Spec §1d's
   verified-citation table asserts `PL | Q1 FY2026 10-Q | sec76`; `sec76` resolves
   empirically to **LUNR's Q2 2026 10-Q**, which is what this artifact cites it as, and
   which is page-verified here. Recorded rather than silently reconciled — one of the two
   is wrong and this artifact does not have the evidence to say which.

---

## 9. Carry-forwards

1. **Register DA-23: LUNR moves from CANDIDATE to CONFIRMED (instance #7), and the
   recorded reason for its candidacy is withdrawn.** The census reads **7 of 7
   loss-making stripped**; LUNR contributes no profitable quarter to the positive
   control. The register's open-candidate list shrinks to **BA 2025 Q3** and **VOYG**.
2. **A false "detector unavailable" finding is itself a register-worthy failure mode, and
   it is distinct from the MRK/BMY/WWD coverage hole.** LUNR was classified
   detector-unavailable on a **concept-name** absence (`GrossProfit` = 0 facts) while the
   detector's inputs were present under `CostsAndExpenses`. Every "no detector can run"
   claim in the universe sweep must be re-tested by *attempting* the detector. The
   genuine unavailability class remains `OperatingIncomeLoss` absent-or-segment-only.
3. **Detector 3 (below-the-line bridge) is sign-blind under a uniform strip and should be
   re-registered with that limitation.** LUNR is the demonstration: a gap of $3.9M,
   transcription-preserved, on a figure wrong by $174.5M. D3 fires only on
   implausible-magnitude strips, not on plausible ones.
4. **Detector 4 (margin plausibility) produced a true positive from a sign-stripped
   comparator at LUNR.** Its verdict was right and its evidence chain was defective end
   to end. Recommend the register demote D4 from "weakest" to **non-probative**, and
   require any D4-sourced verdict to be re-run through D1 or D2 — which, at LUNR, is now
   possible.
5. **A seventh defect class is not in the register: revenue-basis truncation.** The
   extract's revenue column is `RevenueFromContractWithCustomerExcludingAssessedTax`,
   excluding grant revenue ($1.45–5.86M/period at LUNR). This is why 001's row failed its
   own annual-equality test, and it will corrupt any margin or growth series computed
   from the extract. It compounds with DA-26 by disguising exactly the equality test that
   detects DA-26.
6. **`001-technology-baseline/thesis.md:230` and
   `artifacts/LUNR/2026-09-18_1239_operational-kpi_methodology.md` §1 and §3 are
   corrected by this artifact**, per the frozen-001 policy: the DA-26 "exception" is
   withdrawn, the DA-23 candidacy is withdrawn, and the "component identity cannot run"
   premise is refuted.
7. **DA-26 coverage restored to 19 of 19** — LUNR was the sole recorded exception and it
   is an instance. DA-26's "cannot be screened by row position" conclusion is
   *strengthened* by this: LUNR's Q4 row was missed by an author who was actively looking
   for the pattern and had just written it down.
