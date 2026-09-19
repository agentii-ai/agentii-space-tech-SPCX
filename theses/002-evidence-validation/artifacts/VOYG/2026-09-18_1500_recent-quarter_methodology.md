---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: VOYG
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "07d26b9c738b"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: >
      PRESENT at VOYG, and this is the artifact's finding. The registered detector
      `|computed| == |reported|` AND opposite signs FIRES — but the register's §1b
      classification of VOYG as a *different sub-mechanism* ("an unreconcilable LEVEL",
      because "operating income can never EXCEED gross profit") is FALSIFIED. Read the
      bound as a SCREEN, not a classifier: it fires on a sign-stripped loss whose
      magnitude exceeds gross profit, which is exactly VOYG. The classifier is the
      component identity `gross profit − opex`, run in-line below for seventeen periods,
      all seventeen closing with zero residue. `EPS × shares` NOT used, and independently
      disqualified here on arithmetic grounds (§4.3), not merely on policy.
  - da_id: "DA-24"
    chosen_reading: >
      NOT PRESENT in the registered form (no disposal gain in the operating line — proved
      by the exact closing of the component identity on 17 of 17 periods; a leaked
      non-operating item would leave a residue). But a DIFFERENT contamination of the
      SAME line is present and registered below as a new entry: an outside-funding
      contra-expense. NASA SAA grant assistance is deducted from R&D inside the
      operating line — $3,305K in Q2 2026 — and in FY2023 the credit exceeded gross R&D
      outright, producing a filed NEGATIVE R&D expense of $(18,542)K.
  - da_id: "DA-25"
    chosen_reading: >
      NOT PRESENT, with the reading stated because the register's gloss is ambiguous. The
      register says "not reproducible from segment tables". Read literally, VOYG's
      `innovation spend` satisfies that (§3.3): it spans cost of sales + R&D + capitalised
      PP&E and is not derivable from the segment tables. But a non-GAAP measure can only
      ever be checked against the issuer's OWN reconciliation, and VOYG supplies one that
      closes 4-for-4 on the quarters and H1 periods. Chosen reading: DA-25's test is
      non-reproducibility from the issuer's disclosed components. Under that reading it
      does not fire. Adjusted EBITDA (4/4), adjusted net loss per share (4/4), free cash
      flow (4/4) and innovation spend (4/4) all close exactly.
  - da_id: "DA-26"
    chosen_reading: >
      NOT PRESENT at VOYG, tested at the presentation layer where the register locates it
      (001: "Q4 rows carry ANNUAL figures — 23 of 23 issuers"). VOYG's Q4 2025 earnings
      release prints a GENUINE Q4 column — 46,651 / (34,029) / $(0.52) / 58,410,709 — not
      the annual 166,419 / (108,498) / $(2.89) / 40,213,015, and the Q4 figures reconcile
      to the annual by subtraction. Corroborated independently at the XBRL fact layer:
      all 15 `OperatingIncomeLoss` and all 15
      `RevenueFromContractWithCustomerExcludingAssessedTax` duration facts carry
      period_start/period_end spans that match their span exactly. VOYG is a DA-26
      negative on two layers.
  - da_id: "DA-27"
    chosen_reading: >
      NOT APPLICABLE, by the register's own rule ("exact for December year-ends, off by
      one for every other"). `get_company_fiscal_calendar(VOYG)` returns fiscal year end
      month 12. Every retrieved fact's period_start/period_end aligns on calendar
      quarter boundaries, and every label in the filings is a calendar quarter-end.
  - da_id: "DA-28"
    chosen_reading: >
      PRESENT at VOYG, and the task ordered this checked FIRST. Two independent
      manifestations: (i) within-table split discontinuity — the Q4 2025 earnings release
      presents Q4 2024 weighted-average basic shares at 8,758,462 while the FY2024 column
      beside it is 12,736,454. A four-quarter reconstruction of 2024 lands **4 shares** from
      the filed annual when the printed count is scaled by 1.5, and **8.6% below** it when
      the printed count is used as-is — so the comparative is unadjusted for the 1.5-for-1
      split the issuer applies retroactively everywhere else; (ii) three
      non-agreeing Class A counts inside the single Q2 2026 10-Q extract. It does NOT
      explain the $51.408M and produces no EPS-bridge failure — the bridge closes 4-for-4.
      The listing-date guard the register asks for is nonetheless REQUIRED.
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: "Q2 2026 income statement — net sales 52,746; cost of sales 48,289; gross profit 4,457; SG&A 43,672; R&D 7,336; amortization of acquired intangibles 4,857; Loss from operations (51,408); net loss available to common shareholders (46,490); EPS $(0.79); weighted-average basic and diluted 58,521,968"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec18
    page_no: 10
    url: https://agentii.ai/v/VOYG/sec18/10
    located_via: read_source_pages
  - figure: "Cover page — 'There were 55,270,494 shares of registrant's Class A common stock and 5,758,566 shares of Class B common stock outstanding as of July 31, 2026'; non-accelerated filer; emerging growth company"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec18
    page_no: 4
    url: https://agentii.ai/v/VOYG/sec18/4
    located_via: read_source_pages
  - figure: "MD&A results of operations, three months — 'Loss from operations $ (51,408) | $ (24,137) | $ (27,271) | 113.0%'"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec18
    page_no: 44
    url: https://agentii.ai/v/VOYG/sec18/44
    located_via: read_source_pages
  - figure: "MD&A results of operations, six months — 'Loss from operations $ (96,055) | $ (50,426) | $ (45,629) | 90.5%'; gross profit down 78.9%"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec18
    page_no: 45
    url: https://agentii.ai/v/VOYG/sec18/45
    located_via: read_source_pages
  - figure: "Segment reporting — Q2 2026: Defense and Space Technologies net sales 53,211; Starlab 0; total reportable 53,211; intersegment eliminations (465); Total net sales 52,746. Other segment expenses: Defense 63,196; Starlab 6,624; total 69,820; intersegment (465); Corporate and other 21,017; Total 90,372. Adjusted EBITDA: Defense (9,985); Starlab (6,624); total segments (16,609) → reconciles to Loss before income taxes (50,941)"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec18
    page_no: 33
    url: https://agentii.ai/v/VOYG/sec18/33
    located_via: read_source_pages
  - figure: "Government grants — 'When the government grant assistance is related to costs incurred, the assistance is deducted from the related expense'; NASA SAA via Nanoracks LLC 2021-12-01, $217.5M funding, 'All milestone payments have now been earned as of June 30, 2026. As of June 30, 2026, we have cumulatively earned $211.0 million'; offset against R&D: Q2 2026 $3,305K, H1 2026 $8,895K, Q2 2025 $2,250K, H1 2025 $4,250K; gross R&D costs $10.6M (Q2 2026) and $23.7M (H1 2026)"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec18
    page_no: 43
    url: https://agentii.ai/v/VOYG/sec18/43
    located_via: read_source_pages
  - figure: "Key performance metrics — gross profit 4,457 / 8,210 / 2,911 / 13,795 (matching p.10); total backlog 335,512 vs 265,590; Adjusted EBITDA $(37,500) / $(9,066) / $(70,831) / $(30,422); adjusted net loss per share $(0.70) / $(0.52) / $(1.31) / $(2.10); free cash flow $(72,829) / $(27,194) / $(139,623) / $(50,518)"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec18
    page_no: 51
    url: https://agentii.ai/v/VOYG/sec18/51
    located_via: read_source_pages
  - figure: "Adjusted EBITDA reconciliation — net loss attributable to Voyager (46,490) + finance and interest 1,905 + D&A 7,170 + tax (2,195) = EBITDA (39,610); + SBC 3,762 + business acquisition costs 2,008 + restructuring 966 + NCI (2,256) + interest income (3,279) + other 909 = Adjusted EBITDA (37,500), closing exactly"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec18
    page_no: 52
    url: https://agentii.ai/v/VOYG/sec18/52
    located_via: read_source_pages
  - figure: "Adjusted net loss per share reconciliation — net loss attributed to common shareholders (46,490) + SBC 3,762 + BAC 2,008 + restructuring 966 + deferred tax (2,179) + other 909 = adjusted net loss attributable to common shareholders (41,024) → $(0.70) on 58,521,968 shares, closing exactly; free cash flow reconciliation (44,315) + (35,536) + 7,022 = (72,829), closing exactly"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec18
    page_no: 53
    url: https://agentii.ai/v/VOYG/sec18/53
    located_via: read_source_pages
  - figure: "Innovation spend — 'comprised of various costs recognized in cost of sales and research and development costs within our consolidated statements of operations, as well as certain costs capitalized within property and equipment, net'; qualified R&D under section 174 32,939 + development program innovation spend 20,866 = innovation spend 53,805; 102.0% of net sales (Q2 2026). Also capital expenditures — total 35,536; less Starlab 18,760; excluding Starlab 16,776"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec18
    page_no: 54
    url: https://agentii.ai/v/VOYG/sec18/54
    located_via: read_source_pages
  - figure: "Note 2 — 'On June 2, 2025, the Company effected a 1.5-for-1 forward split of its Common stock ... All share and per share information, including share-based compensation, throughout the unaudited interim condensed consolidated financial statements has been retroactively adjusted to reflect the stock split'"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec18
    page_no: 18
    url: https://agentii.ai/v/VOYG/sec18/18
    located_via: read_source_pages
  - figure: "Q1 2026 income statement — net sales 35,246; cost of sales 36,792; Gross (loss) profit (1,546); SG&A 31,357; R&D 7,511; amortization 4,233; Loss from operations (44,647); weighted-average basic and diluted 58,339,505"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec15
    page_no: 9
    url: https://agentii.ai/v/VOYG/sec15/9
    located_via: read_source_pages
  - figure: "Q1 2026 MD&A results of operations — 'Gross (loss) profit $ (1,546) | $ 5,585 | $ (7,131) | (127.7)%'; 'Loss from operations $ (44,647) | $ (26,289) | $ (18,358) | 69.8%'"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec15
    page_no: 38
    url: https://agentii.ai/v/VOYG/sec15/38
    located_via: read_source_pages
  - figure: "Q2 2025 10-Q income statement — 2024 comparative weighted-average basic shares: Q2 2024 12,574,261; H1 2024 12,536,053 (diluted 12,577,013 / 12,538,805). Also the 2024 comparatives' component identity: Q2 2024 net sales 36,653 − cost of sales 27,390 − (13,295 + 6,870 + 1,745) = (12,647); H1 2024 66,869 − 51,425 − (28,885 + 7,637 + 3,489) = (24,567). Also Q2 2024 filed basic EPS $(2.29) against diluted $(2.73) — diluted MORE negative than basic on a net loss"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec13
    page_no: 9
    url: https://agentii.ai/v/VOYG/sec13/9
    located_via: read_source_pages
  - figure: "Q3 2025 10-Q income statement — nine months ended September 30, 2024 weighted-average basic 12,603 (thousands) and Q3 2024 12,736 (thousands), the anchors for the four-quarter reconstruction. Q3 2024 research and development filed as a NEGATIVE expense (397); 9M 2024 R&D 7,240 = H1 2024 7,637 − 397 exactly. Q3 2025 net sales 39,587 and loss from operations (24,043); 9M 2025 net sales 119,768 and loss from operations (74,469), so the ladder closes: 119,768 − 80,181 = 39,587 and (74,469) − (50,426) = (24,043)"
    ticker: VOYG
    form_type: 10-Q
    citation_id: sec14
    page_no: 9
    url: https://agentii.ai/v/VOYG/sec14/9
    located_via: read_source_pages
  - figure: "FY2025 consolidated statements of operations — net sales 166,419; cost of sales 136,544; SG&A 117,085; R&D 12,753; impairment losses 0; amortization 8,535; Loss from operations (108,498) for 2025, (48,442) for 2024, (14,173) for 2023. NO gross-profit subtotal is presented at the annual level. FY2023 research and development is presented as a NEGATIVE expense (18,542)"
    ticker: VOYG
    form_type: 10-K
    citation_id: sec12
    page_no: 99
    url: https://agentii.ai/v/VOYG/sec12/99
    located_via: read_source_pages
  - figure: "Q4 2025 earnings release — condensed consolidated statements of operations. GENUINE Q4 column: net sales 46,651; cost of sales 36,661; SG&A 35,452; R&D 5,173; amortization 3,394; Loss from operations (34,029); EPS $(0.52); weighted-average basic 58,410,709. Annual column beside it: 166,419 / (108,498) / $(2.89) / 40,213,015. The Q4 2024 comparative weighted-average basic is 8,758,462 against a FY2024 figure of 12,736,454 — a ratio of exactly 1.5"
    ticker: VOYG
    form_type: 8-K
    citation_id: sec7
    page_no: 11
    url: https://agentii.ai/v/VOYG/sec7/11
    located_via: read_source_pages
  - figure: "Q4 2025 earnings release non-GAAP tables — Q4 2025 net sales by segment total 46,651; Adjusted EBITDA reconciliation: net loss attributable to Voyager (30,221) + 1,369 + 4,975 + 1,193 = EBITDA (22,684); + 3,527 + 2,450 + 494 + (2,781) + (3,764) + 934 = Adjusted EBITDA (21,824), closing exactly"
    ticker: VOYG
    form_type: 8-K
    citation_id: sec7
    page_no: 13
    url: https://agentii.ai/v/VOYG/sec7/13
    located_via: read_source_pages
  - figure: "Recast 8-K (filed 2026-08-14) — consolidated statements of operations FY2025/2024/2023, UNCHANGED from the original 10-K: Loss from operations (108,498) / (48,442) / (14,173); FY2023 R&D (18,542). The recast is a segment re-presentation only and does NOT restate the statements of operations"
    ticker: VOYG
    form_type: 8-K
    citation_id: sec19
    page_no: 40
    url: https://agentii.ai/v/VOYG/sec19/40
    located_via: read_source_pages
  - figure: "Recast 8-K — Research and Development and Government Grants: 'For the years ended December 31, 2025 and 2024, gross research and development costs were $19.0 million and $13.0 million'; NASA SAA $217.5M, cumulatively earned $187.2M (2025) and $127.2M (2024); 'When the government grant assistance is related to costs incurred, the assistance is deducted from the related expense'"
    ticker: VOYG
    form_type: 8-K
    citation_id: sec19
    page_no: 20
    url: https://agentii.ai/v/VOYG/sec19/20
    located_via: read_source_pages
  - figure: "Recast 8-K — government grant assistance offset against research and development $6,225K (2025) and $5,420K (2024); offset against construction in progress $54,000K (2025) and $54,930K (2024); plus recast FY2025 results of operations repeating Loss from operations $(108,498)"
    ticker: VOYG
    form_type: 8-K
    citation_id: sec19
    page_no: 21
    url: https://agentii.ai/v/VOYG/sec19/21
    located_via: read_source_pages
  - figure: "Recast 8-K consent of independent registered public accounting firm — audit report dated March 10, 2026, noting 'the change in reportable segments effective August 14, 2026'. Establishes that the recast is a segment re-presentation, not a restatement"
    ticker: VOYG
    form_type: 8-K
    citation_id: sec19
    page_no: 3
    url: https://agentii.ai/v/VOYG/sec19/3
    located_via: read_source_outline
---

# VOYG — what the $51.408M is

**Pillar PIL-3, defect census. Deliverable question:** the register records VOYG as
reporting `operating_income` of **$51.408M** against gross profit of **$4.457M**, failing
the gross-profit bound by $46.951M, and classifies it as **"a different sub-mechanism:
not a sign inversion but an unreconcilable LEVEL"** — a value that "cannot be an operating
income at any sign."

**The answer: the $51.408M is a sign-stripped `Loss from operations` of $(51,408)
thousand for the three months ended June 30, 2026.** The level *is* reconcilable, exactly,
with zero residue. **VOYG is the plainest DA-23 instance in the register.** The register's
classification is falsified, and the reasoning that produced it contains an error that
matters beyond this ticker (§2).

---

## 1. The level determination

### 1.1 Component identity, in-line — `gross profit − opex`

The three months ended June 30, 2026, as filed
([📄 VOYG 10-Q p.10](https://agentii.ai/v/VOYG/sec18/10)):

```
VOYG — CONDENSED CONSOLIDATED STATEMENTS OF OPERATIONS
Three months ended June 30, 2026 (Unaudited, in thousands)

  Net sales                                                        52,746
  Cost of sales                                                   (48,289)
  Gross profit                                                      4,457
    Operating expenses:
      Selling, general, and administrative                        (43,672)
      Research and development                                     (7,336)
      Amortization of acquired intangibles                         (4,857)
      opex subtotal                                               (55,865)
  Loss from operations                                            (51,408)   ← filed "(51,408)"

  4,457 − (43,672 + 7,336 + 4,857)  =  4,457 − 55,865  =  −51,408
```

**The identity closes on −51,408 exactly.** The filed figure is a **loss**, written
`(51,408)` and labelled "*Loss* from operations." The MD&A repeats it as a negative in
the year-over-year bridge: `Loss from operations $ (51,408) | $ (24,137) | $ (27,271) |
113.0%` ([📄 VOYG 10-Q p.44](https://agentii.ai/v/VOYG/sec18/44)). The platform stores
`us-gaap:OperatingIncomeLoss` for this period as **`+51408000`** — the magnitude with the
sign stripped.

### 1.2 The arc set, independently

The calculation linkbase carries arcs into `us-gaap:OperatingIncomeLoss` under role
`http://voyager.com/role/CONDENSEDCONSOLIDATEDSTATEMENTSOFOPERATIONS` from `GrossProfit`
(+1), `SellingGeneralAndAdministrativeExpense` (−1), `ResearchAndDevelopmentExpense` (−1)
and `AmortizationOfIntangibleAssets` (−1). Summing child × weight gives **−51,408**. Both
admissible forms of the identity — the component derivation and the arc set — land on the
same signed value. This is the exactly the VRT §1.1/§1.2 method.

### 1.3 The instrument pair — `computed` vs `reported`

`validate_calculation` on accession `0001628280-26-052292` returned, for
`us-gaap:OperatingIncomeLoss`, period `Tue Jun 30 2026`:

```
computed: -51408000      reported: 51408000      diff: 102816000
```

Per the instrument rule, only the **`computed` vs `reported` pair** was read; the `status`
column is not reported here. The pair satisfies **`|computed| == |reported|` (both
51,408,000) AND opposite signs** — the registered DA-23 signature. Unlike the VRT case,
the instrument *did* return a result for this concept at VOYG, so VOYG does **not** exhibit
the arc-coverage gap; and unlike the ~93% false-positive class, this one is a genuine
positive, corroborated independently twice above.

### 1.4 Seventeen component identities, all closing

The same identity was run for every period the filings reach. **All seventeen close with
zero residue.** Δ marks a gross profit that is **DERIVED** (net sales − cost of sales),
because the annual and Q3 statements present no gross-profit subtotal (§2.2). ΔΔ marks a
period that is *wholly* derived — Q1 2024 is H1 2024 less Q2 2024 — so it tests the mutual
consistency of those two columns rather than standing alone.

**R&D sign convention, stated because this issuer requires it:** R&D appears as a *negative*
where it is a net expense and as a **positive** where the grant credit makes it a net
benefit. The `opex` column is the arithmetic sum of the four operating-expense rows exactly
as printed. The filer's own nine-month column proves the convention is theirs, not ours:
9M 2024 R&D is filed as **7,240**, which is H1 2024's **7,637** less Q3 2024's **397** —
exactly ([📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec14/9)).

| Period | Net sales | Cost of sales | Gross profit | SG&A | R&D | Impair. | Amort. | opex | Loss from ops | Identity |
|---|---|---|---|---|---|---|---|---|---|---|
| FY2023 | 136,062 | (108,277) | 27,785 Δ [📄19/40](https://agentii.ai/v/VOYG/sec19/40) | (54,043) | **+18,542** | — | (6,457) | (41,958) | (14,173) | ✓ |
| Q1 2024 ΔΔ | 30,216 | (24,035) | 6,181 Δ | (15,590) | (767) | — | (1,744) | (18,101) | (11,920) | ✓ |
| Q2 2024 | 36,653 | (27,390) | 9,263 Δ [📄13/9](https://agentii.ai/v/VOYG/sec13/9) | (13,295) | (6,870) | — | (1,745) | (21,910) | (12,647) | ✓ |
| H1 2024 | 66,869 | (51,425) | 15,444 Δ [📄13/9](https://agentii.ai/v/VOYG/sec13/9) | (28,885) | (7,637) | — | (3,489) | (40,011) | (24,567) | ✓ |
| Q3 2024 | 39,599 | (30,276) | 9,323 Δ [📄14/9](https://agentii.ai/v/VOYG/sec14/9) | (15,173) | **+397** | (3,594) | (3,046) | (21,416) | (12,093) | ✓ |
| 9M 2024 | 106,468 | (81,701) | 24,767 Δ [📄14/9](https://agentii.ai/v/VOYG/sec14/9) | (44,058) | (7,240) | (3,594) | (6,535) | (61,427) | (36,660) | ✓ |
| FY2024 | 144,180 | (109,265) | 34,915 Δ [📄19/40](https://agentii.ai/v/VOYG/sec19/40) | (62,570) | (7,611) | (3,594) | (9,582) | (83,357) | (48,442) | ✓ |
| Q1 2025 | 34,507 | (28,922) | 5,585 [📄15/9](https://agentii.ai/v/VOYG/sec15/9) | (26,286) | (4,040) | — | (1,548) | (31,874) | (26,289) | ✓ |
| Q2 2025 | 45,674 | (37,464) | 8,210 [📄18/10](https://agentii.ai/v/VOYG/sec18/10) | (30,241) | (502) | — | (1,604) | (32,347) | (24,137) | ✓ |
| H1 2025 | 80,181 | (66,386) | 13,795 [📄18/10](https://agentii.ai/v/VOYG/sec18/10) | (56,527) | (4,542) | — | (3,152) | (64,221) | (50,426) | ✓ |
| Q3 2025 | 39,587 | (33,497) | 6,090 Δ [📄14/9](https://agentii.ai/v/VOYG/sec14/9) | (25,106) | (3,038) | — | (1,989) | (30,133) | (24,043) | ✓ |
| 9M 2025 | 119,768 | (99,883) | 19,885 Δ [📄14/9](https://agentii.ai/v/VOYG/sec14/9) | (81,633) | (7,580) | — | (5,141) | (94,354) | (74,469) | ✓ |
| Q4 2025 | 46,651 | (36,661) | 9,990 Δ [📄7/11](https://agentii.ai/v/VOYG/sec7/11) | (35,452) | (5,173) | — | (3,394) | (44,019) | (34,029) | ✓ |
| FY2025 | 166,419 | (136,544) | 29,875 Δ [📄19/40](https://agentii.ai/v/VOYG/sec19/40) | (117,085) | (12,753) | — | (8,535) | (138,373) | (108,498) | ✓ |
| Q1 2026 | 35,246 | (36,792) | **(1,546)** [📄15/9](https://agentii.ai/v/VOYG/sec15/9) | (31,357) | (7,511) | — | (4,233) | (43,101) | (44,647) | ✓ |
| Q2 2026 | 52,746 | (48,289) | 4,457 [📄18/10](https://agentii.ai/v/VOYG/sec18/10) | (43,672) | (7,336) | — | (4,857) | (55,865) | **(51,408)** | ✓ |
| H1 2026 | 87,992 | (85,081) | 2,911 [📄18/10](https://agentii.ai/v/VOYG/sec18/10) | (75,029) | (14,847) | — | (9,090) | (98,966) | (96,055) | ✓ |

Read the two positive R&D rows carefully. **FY2023 and Q3 2024 are not extraction
artefacts and must not be "corrected":** each is a filed *negative expense*, $(18,542)K and
$(397)K, and the identity closes *only* when the credit reduces the opex subtotal. This is
the second trap on this ticker (§5.2).

---

## 2. The gross-profit bound: a screen, not a classifier

### 2.1 The register's logic error

Spec §1b reasons: VOYG's figure "cannot be an operating income at any sign, because
**operating income can never EXCEED gross profit**." The premise is applied to the
**sign-stripped magnitude** — 51.408 > 4.457 fires correctly as a bound violation — and
the violation is then read as evidence of a *level* defect **mutually exclusive with** sign
stripping.

**It is not exclusive.** A sign-stripped loss whose magnitude exceeds gross profit fails
the bound too. Restore the sign and `−51.408 < +4.457` violates nothing. The bound is a
**displacement detector**: it tells you something is wrong, never *what*. Both causes
produce identical bound violations. **The register ran the screen and skipped the
classifier** — the component identity, which it did not run for VOYG.

Two further cautions on the bound, both load-bearing:

1. **The bound rests on a premise the issuer itself strains.** `operating income ≤ gross
   profit` holds only while total opex ≥ 0. VOYG's FY2023 filed R&D is *negative*. Total
   opex stayed positive there, so the bound held — but the register states the rule as
   absolute, and at this issuer it is contingent.
2. **The register's "three consecutive quarters" is an undercount.** The bound fires on
   **16 of the 17 periods tested** (all but FY2023):

| Period | `OperatingIncomeLoss` as stored | Gross profit | Bound fires? |
|---|---|---|---|
| FY2023 | 14,173 | 27,785 Δ | no |
| Q1 2024 | 11,920 | 6,181 Δ | **YES** |
| Q2 2024 | 12,647 | 9,263 Δ | **YES** |
| H1 2024 | 24,567 | 15,444 Δ | **YES** |
| Q3 2024 | 12,093 | 9,323 Δ | **YES** |
| 9M 2024 | 36,660 | 24,767 Δ | **YES** |
| FY2024 | 48,442 | 34,915 Δ | **YES** |
| Q1 2025 | 26,289 | 5,585 | **YES** |
| Q2 2025 | 24,137 | 8,210 | **YES** |
| H1 2025 | 50,426 | 13,795 | **YES** |
| Q3 2025 | 24,043 | 6,090 Δ | **YES** |
| 9M 2025 | 74,469 | 19,885 Δ | **YES** |
| Q4 2025 | 34,029 | 9,990 Δ | **YES** |
| FY2025 | 108,498 | 29,875 Δ | **YES** |
| Q1 2026 | 44,647 | 1,546 (gross **loss**) | **YES** |
| Q2 2026 | 51,408 | 4,457 | **YES** |
| H1 2026 | 96,055 | 2,911 | **YES** |

"Three consecutive quarters" describes the quarters the register happened to check, not
the population. **Fifteen of the sixteen firing periods are unreported by the register**,
and the bound has fired continuously since at least FY2024 — every period the register did
not look at. A screen with that hit rate carries no information about *cause*.

### 2.2 The bound is not computable at the annual level from filed data

The Q2 2026 10-Q presents a **gross profit subtotal**
([📄 VOYG 10-Q p.10](https://agentii.ai/v/VOYG/sec18/10)). The annual statements do
**not** — neither the original 10-K ([📄 VOYG 10-K p.99](https://agentii.ai/v/VOYG/sec12/99))
nor the recast 8-K ([📄 VOYG 8-K p.40](https://agentii.ai/v/VOYG/sec19/40)) carries a
gross-profit row. Consistent with that, `search_xbrl_facts` returns **six `GrossProfit`
facts, all interim, and no annual fact at all.** So for FY2023–FY2025 the register's own
test can only be run on a **derived** gross profit, and the derived figure is not what the
register's bound presumes. **The screen is unavailable exactly where the register used it
loudest.**

---

## 3. The six-defect census

Each candidate resolves to exactly one outcome: **explained, with a citation**, or
**promoted to a registered defect, with the settling detector named.**

**Disposition of record — every one of the six, settled:**

| Candidate | Outcome | Settled by |
|---|---|---|
| **DA-23** sign stripping | **REGISTERED DEFECT CONFIRMED — this is the mechanism.** §1.1–§1.4 | Detector that settles it: `\|computed\| == \|reported\|` AND opposite signs, **classified by the component identity** (`gross profit − opex`), never by the status column. Fires at Q2 2026 and 16 other periods |
| **DA-24** asset-sale contamination | **EXPLAINED — not present.** §3.2, [📄 VOYG 10-Q p.10](https://agentii.ai/v/VOYG/sec18/10) | 17/17 exact identities leave no residue for a leaked disposal gain; all non-operating items sit below the line |
| **DA-25** normalised per-unit metrics | **EXPLAINED — not present under the declared reading.** §3.3, [📄 VOYG 10-Q p.52](https://agentii.ai/v/VOYG/sec18/52) | Every issuer-defined measure self-reconciles on the issuer's own disclosed components, 4/4 |
| **DA-26** annual mislabelled as quarterly | **EXPLAINED — not present on two layers.** §3.4, [📄 VOYG 8-K p.11](https://agentii.ai/v/VOYG/sec7/11) | Genuine Q4 column reconciling to the annual by subtraction; all 30 duration facts span-correct |
| **DA-27** calendar-quarter fiscal labels | **EXPLAINED — not applicable.** §3.5, `fiscal_year_end_month: 12` | The register's own rule makes DA-27 exact for December year-ends |
| **DA-28** IPO capital-structure discontinuity | **PROMOTED TO REGISTERED DEFECT — present, and it does not cause the anomaly.** §4, [📄 VOYG 8-K p.11](https://agentii.ai/v/VOYG/sec7/11) | Detector that settles it: primary-fact collision on concept + dimension + instant, run **before** any `EPS × shares` test |

Plus **three further defects promoted** from this ticker that the register does not yet
carry — §3.7 (outside-funding contra-expense inside the operating line) and §3.8 (two
detector-coverage gaps). Those are new; the six above are the register's.

### 3.1 DA-23 — sign stripping · **PRESENT. This is the mechanism.**

Confirmed three independent ways (§1.1, §1.2, §1.3) and by seventeen exact component
identities (§1.4). The register's sub-mechanism claim is **falsified** (§2.1).

**Two further DA-23-class findings on the same accession:**

- **`GrossProfit` is sign-stripped too.** Q1 2026's `GrossProfit` is stored as
  `+1,546,000` while the filing reads `Gross (loss) profit (1,546)`
  ([📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec15/9)). Same extractor behaviour, a
  second concept. **A DA-23 detector scoped to `OperatingIncomeLoss` only would miss it.**
- **One filed line has NO numeric fact at all.** `ResearchAndDevelopmentExpense` returns
  twelve facts with **no FY2023, FY2024 or FY2025 annual value** — so the FY2023 negative
  R&D line of $(18,542)K is *unretrievable* from the platform. The nearest stored concept,
  `ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost`, holds the **gross** figure
  (`18,500,000` for FY2023), which is the *wrong quantity*. A consumer rebuilding FY2023
  from facts cannot close it. **This is an absence, not a wrong value** — the same class
  as the VRT `OperatingIncomeLoss` no-result gap.

### 3.2 DA-24 — asset-sale contamination · **NOT PRESENT, and positively excluded.**

No disposal gain flows through the operating line: **a leaked non-operating item would
leave a residue, and seventeen of seventeen component identities close to the dollar**
(§1.4). The
non-operating items are correctly below the line — loss on debt extinguishment
`(7,804)` in Q2 2025 only, finance and interest expense `(1,905)`, other income `2,372`
all sit *after* `Loss from operations`
([📄 VOYG 10-Q p.10](https://agentii.ai/v/VOYG/sec18/10)).

**But a different contamination of the same line is present — promoted in §3.7.**

### 3.3 DA-25 — normalised per-unit metrics · **NOT PRESENT under the stated reading.**

Every issuer-defined normalised figure self-reconciles exactly:

| Measure | Q2 2026 | Identity closes? | Source |
|---|---|---|---|
| Adjusted EBITDA | $(37,500)K | ✓ 4/4 quarters and H1 periods | [📄 18/52](https://agentii.ai/v/VOYG/sec18/52) |
| Adjusted net loss per share | $(0.70) | ✓ 4/4 — (41,024) / 58,521,968 = −0.70098 | [📄 18/53](https://agentii.ai/v/VOYG/sec18/53) |
| Free cash flow | $(72,829)K | ✓ 4/4 | [📄 18/53](https://agentii.ai/v/VOYG/sec18/53) |
| Innovation spend | $53,805K | ✓ 4/4 — 32,939 + 20,866 = 53,805 | [📄 18/54](https://agentii.ai/v/VOYG/sec18/54) |

**Reading stated, because the register's gloss is ambiguous.** Literally, "innovation
spend" *is* non-reproducible from the segment tables — it is "comprised of various costs
recognized in cost of sales and research and development costs ... as well as certain
costs capitalized within property and equipment, net", so it spans three statements and
exceeds net sales outright (102.0% of them). Read that way DA-25 fires. But a non-GAAP
measure can only ever be checked against the issuer's **own** reconciliation, and VOYG
supplies one for every measure that closes 4-for-4. **Chosen reading: DA-25's test is
non-reproducibility from the issuer's disclosed components. Under it, DA-25 does not
fire** — and the figure is never substituted into a filed GAAP line. Recorded in
`definitions_used`.

### 3.4 DA-26 — annual mislabelled as quarterly · **NOT PRESENT. Tested on two layers.**

**Presentation layer — the decisive test.** 001's DA-26 reading is that the *Q4 row* is
where the annual hides ("23 of 23 issuers"). VOYG's Q4 2025 earnings release prints a
**genuine** Q4 column
([📄 VOYG 8-K p.11](https://agentii.ai/v/VOYG/sec7/11)):

| | Q4 2025 | FY2025 |
|---|---|---|
| Net sales | **46,651** | 166,419 |
| Loss from operations | **(34,029)** | (108,498) |
| Net loss per common share (basic) | **$(0.52)** | $(2.89) |
| Weighted-average shares (basic) | **58,410,709** | 40,213,015 |

Not one of the four is the annual value, and the Q4 column reconciles to the annual by
subtraction: 166,419 − 119,768 (9M) = 46,651; 108,498 − 74,469 (9M) = 34,029. **The
mislabelling mechanism is absent.**

**Fact layer, independent corroboration.** All fifteen `OperatingIncomeLoss` duration
facts and all fifteen `RevenueFromContractWithCustomerExcludingAssessedTax` duration facts
carry `period_start`/`period_end` spans matching their span exactly. No 12-month span sits
in a quarter slot, and the ladder closes at every rung:
`Q1 26 35,246 + Q2 26 52,746 = 87,992 = H1 26`, and on the 2025 ladder
`9M 119,768 − H1 80,181 = 39,587 = Q3 2025` and `(74,469) − (50,426) = (24,043) = Q3 2025`
— both matching the Q3 2025 10-Q's own column exactly
([📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec14/9)). **VOYG is a DA-26 negative on two
layers, and the second layer is now checked against a third filing.**

*Residual:* the earnings *call transcripts* were not screened for a mislabelled row. Named
in §7.

### 3.5 DA-27 — calendar-quarter fiscal labels · **NOT APPLICABLE.**

`get_company_fiscal_calendar(VOYG)` returns **fiscal year end month 12** — a December
year-end. The register's own rule: DA-27 is exact for December year-ends and off by one
for every other. Every retrieved fact aligns on calendar quarter boundaries
(e.g. `2026-04-01 → 2026-06-30` for the quarter ended June 30, 2026), and every filing
label is a calendar quarter-end. **The trap cannot bite.**

### 3.6 DA-28 — IPO capital-structure discontinuity · **PRESENT. Does not explain the anomaly.**

Treated in full in §4. **Disposition: PRESENT in two independent forms; does NOT produce
the $51.408M and does NOT produce an EPS-bridge failure.**

### 3.7 Promoted to registered defect — an outside-funding contra-expense inside the operating line

**Not DA-24** (no disposal), and **not an extraction defect** — a disclosed accounting
policy, faithfully extracted. It is nonetheless a genuine contamination of the operating
line, and it is not in the register.

NASA SAA grant assistance is **deducted from R&D inside the operating line**:
"*When the government grant assistance is related to costs incurred, the assistance is
deducted from the related expense*"
([📄 VOYG 10-Q p.43](https://agentii.ai/v/VOYG/sec18/43);
[📄 VOYG 8-K p.20](https://agentii.ai/v/VOYG/sec19/20)).

| | Q2 2026 | H1 2026 | FY2025 | FY2024 |
|---|---|---|---|---|
| Gross R&D (disclosed) | $10.6M | $23.7M | $19.0M | $13.0M |
| R&D expense on the income statement | $7,336K | $14,847K | $12,753K | $7,611K |
| **Grant credit inside the operating line** | **$3,305K** | **$8,895K** | **$6,225K** | **$5,420K** |

**Consequence:** without the Q2 2026 credit, the operating loss would be **$(54,713)K**
rather than $(51,408)K — the reported operating loss is understated by 6.4%.** Cumulative
earned funding is **$211.0M of $217.5M, with all milestones now earned**
([📄 VOYG 10-Q p.43](https://agentii.ai/v/VOYG/sec18/43)) — so the credit **goes to zero
from Q3 2026**, mechanically widening the operating loss with no change in operations.
That is a forward-looking fact a recent-quarter read must carry.

**The signature case is FY2023**, where the credit exceeded gross R&D and the issuer filed
a **negative R&D expense of $(18,542)K**
([📄 VOYG 8-K p.40](https://agentii.ai/v/VOYG/sec19/40)). The component identity requires
carrying it as a **+18,542 credit** against the other operating expenses (§1.4).

**It is not a one-off.** Q3 2024 research and development is also filed as a **negative
expense, $(397)K** ([📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec14/9)) — and the filer's
own nine-month column confirms the treatment arithmetically: 9M 2024 R&D of **7,240** is
H1 2024's **7,637** less Q3's **397**, exactly. **Two negative-expense periods in one
issuer, both required by the arithmetic, make this a recurring presentation rather than a
tagging error** — which is precisely what a sign-strip detector is most likely to mangle.
Note also the swing the credit produces in the year-over-year R&D line: $6,870K in Q2 2024
against $502K in Q2 2025 ([📄 13/9](https://agentii.ai/v/VOYG/sec13/9)) is not a research
program being wound down; it is the same program net of a grant.

**Detector that would settle it — a contra-expense detector, cheap and universal:** reconcile
the issuer's disclosed *gross* R&D note against the income-statement R&D line. A non-zero
gap is an outside-funding credit inside the operating line. At VOYG it fires on all four
periods above. **This detector is not in the register, and its absence is why a
negative-expense trap survives alongside the sign-strip trap.** Register it.

### 3.8 Promoted to registered defect — a detector-coverage gap in DA-28

`EntityCommonStockSharesOutstanding` returns **zero facts** for VOYG. A DA-28 detector
keyed on the cover-page concept therefore finds nothing and silently clears an issuer with
**three different Class A counts in a single extract** (§4.2). **Settling detector:** key on
`CommonStockSharesOutstanding` *with* `StatementClassOfStockAxis` dimensions **and** on the
cover-page value, and flag any two `is_primary` facts sharing concept + dimension + instant
with **differing** values. Recorded for the register.

**The gap is wider than DA-28.** `us-gaap:WeightedAverageNumberOfSharesOutstandingBasic`
and `us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding` — the two concepts an EPS
check needs — also return **zero facts for VOYG** (against 7,187 and 7,214 facts across
162 and 163 tickers platform-wide, so the concept names are right and the absence is
issuer-specific). **Every EPS bridge in §4.1 is reproducible from filing pages only, never
from the fact set.** The same primary-fact-presence assertion covers all three.

---

## 4. The DA-28 check — run first, as the task ordered

VOYG is a June 2025 IPO with a dual-class structure, so the register's warning ("VOYG
listed recently — check DA-28 FIRST, because it can explain an EPS failure that is not
DA-23") is well-aimed. **Result: DA-28 is present, and it explains nothing about the
$51.408M.**

### 4.1 The EPS bridge closes 4-for-4

| Period | Net loss available to common | Weighted-average basic | Computed | Reported | Bridge |
|---|---|---|---|---|---|
| Q2 2026 | $(46,490)K | 58,521,968 | $(0.7944) | **$(0.79)** | ✓ |
| Q2 2025 | $(36,640)K | 29,695,203 | $(1.2339) | **$(1.23)** | ✓ |
| H1 2026 | $(90,473)K | 58,430,737 | $(1.5484) | **$(1.55)** | ✓ |
| H1 2025 | $(69,579)K | 22,017,362 | $(3.1601) | **$(3.16)** | ✓ |

All four from a single page ([📄 VOYG 10-Q p.10](https://agentii.ai/v/VOYG/sec18/10)).
Basic equals diluted on every period shown.

### 4.2 Manifestation (i) — one extract, three Class A counts

The Q2 2026 10-Q's own XBRL extract carries, for `us-gaap:CommonStockSharesOutstanding`
at instant 2026-06-30, **two non-identical `is_primary` facts for the same class**:

| Value | Dimension | File |
|---|---|---|
| 53,598,000 | `CommonClassAMember` + `CommonStockMember` | `voyg-20260630.htm` |
| 53,598,284 | `CommonClassAMember` alone | `voyg-20260630.htm` |

...plus the cover page's **55,270,494** Class A at 2026-07-31
([📄 VOYG 10-Q p.4](https://agentii.ai/v/VOYG/sec18/4)). Two of the three are primary
facts in the same file; the third is a different date. The Q2 2026 extract also mixes in
zero-valued and null-valued `CommonStockSharesOutstanding` facts, and the FY2025 10-K
carries a **zero** "common stock" fact at 2025-12-31 beside a 53,383,859 Class A fact for
the same instant.

**This is why `EPS × shares` is not merely inadmissible on policy but arithmetically
unstable at VOYG:** there are three candidate denominators in one extract and none of them
is the operating income. `$(0.79) × 61,029,060` (cover-page total) = $(48,213)K — a
plausible-looking number that is neither the net loss available to common $(46,490)K nor
the operating loss $(51,408)K. **The inadmissibility is a numeric fact here, not a
preference.**

### 4.3 Manifestation (ii) — a within-table 1.5× split discontinuity `[NEW]`

The Q4 2025 earnings release
([📄 VOYG 8-K p.11](https://agentii.ai/v/VOYG/sec7/11)) places two weighted-average share
counts side by side **in one table**:

- Q4 2024 (three months): **8,758,462**
- FY2024 (year): **12,736,454**

**The test is a four-quarter reconstruction of 2024, and it excludes the printed Q4 count
outright.** Every other 2024 quarter is available on the retroactively split-adjusted basis
the issuer says it applied "throughout"
([📄 VOYG 10-Q p.18](https://agentii.ai/v/VOYG/sec18/18)):

| 2024 period | Weighted-average basic | Source |
|---|---|---|
| Q1 2024 | 12,497,845 — derived: `2 × 12,536,053 − 12,574,261` | from [📄 13/9](https://agentii.ai/v/VOYG/sec13/9) |
| Q2 2024 | 12,574,261 | [📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec13/9) |
| H1 2024 | 12,536,053 | [📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec13/9) |
| Q3 2024 | 12,736 (thousands) | [📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec14/9) |
| 9M 2024 | 12,603 (thousands) | [📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec14/9) |
| **Q4 2024 as printed** | **8,758,462** | [📄 VOYG 8-K p.11](https://agentii.ai/v/VOYG/sec7/11) |
| FY2024 as printed | 12,736,454 | [📄 VOYG 8-K p.11](https://agentii.ai/v/VOYG/sec7/11) |

**Test A — the printed Q4 count, taken at face value.**
`(12,497,845 + 12,574,261 + 12,736,000 + 8,758,462) / 4 = 11,641,642`, which is **8.6%
below** the filed FY2024 average of **12,736,454**. The printed Q4 column is inconsistent
with the annual column in the same table.

**Test B — the same count scaled by the split factor.**
`8,758,462 × 1.5 = 13,137,693`, and
`(12,497,845 + 12,574,261 + 12,736,000 + 13,137,693) / 4 = **12,736,450**` — against the
filed FY2024 of **12,736,454**. **Agreement to four shares on a 12.7-million base**, with
the residual absorbed by the thousands-rounding of the Q3 2024 input. Independently, the
ratio `13,137,693 / 8,758,462 = **1.5000**`, and the Q4 count implied by the annual and the
nine-month figures (`4 × 12,736,454 − 3 × 12,603,xxx`, which ranges over
`13,133,819 … 13,136,816`) brackets it to within 0.03%.

So the Q4 2024 comparative is on a **pre-split** basis while the FY2024 column beside it
**is** split-adjusted, by a factor of exactly 1.5 — the 1.5-for-1 split
([📄 VOYG 10-Q p.18](https://agentii.ai/v/VOYG/sec18/18)) that the issuer says was applied
retroactively "throughout" its financial statements. The release's own arithmetic is
internally consistent on each column separately — Q4 2024 EPS $(1.68) = 14,697 / 8,758,462
✓; FY2024 EPS $(6.59) = 83,888 / 12,736,454 ✓ — **and that is precisely the hazard: two
columns that each pass a self-consistency check on incompatible share bases.** The printed
Q4 2024 EPS is not comparable to the printed FY2024 EPS in the same table, and a reader
comparing them would find 2024 losses *improving* quarter-over-quarter for a reason that
does not exist.

Corroborating context: inside calendar 2025 the weighted-average basic count steps
14,339,521 (Q1) → 29,695,203 (Q2) → 58,407,000 (Q3) — two ~100% discontinuities in two
quarters, from the split (effective 2025-06-02) and the IPO (closing 2025-06-12) both
landing inside Q2 2025.

**The same trap, one layer down.** Q2 2024 filed basic EPS is $(2.29) against diluted
$(2.73), and H1 2024 $(3.88) against $(4.32)
([📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec13/9)) — **diluted more negative than
basic on a net loss**, where anti-dilution should force the two together, as it does in
every 2025 and 2026 period. The denominators differ by only ~0.02% (12,574,261 vs
12,577,013), so the divergence is in the *numerator*, and the $5,481K of preferred
dividends in the same column does not close it exactly. **Not resolved — carried in §7.**

### 4.4 DA-28 verdict

**PRESENT, in both the multiple-share-count form and a split-discontinuity form. It causes
no EPS failure and does not touch the $51.408M.** The DA-23 detector does not *need* the
listing-date guard to fire here — the `|computed| == |reported|` sign signature is
capital-structure-independent — but **any detector that reaches for an EPS-based
cross-check does**, and would still be wrong at VOYG because of §4.2. Recorded as the
guard's justification, not its counterexample.

---

## 5. What the register should now say

### 5.1 The VOYG entry is reclassified

| Register says (spec §1b) | This artifact finds |
|---|---|
| "a **different sub-mechanism**: not a sign inversion but an **unreconcilable level**" | **Same mechanism. Plain DA-23.** The level reconciles to −51,408 with zero residue |
| "cannot be an operating income at any sign" | It is not an operating income at any sign — it is a sign-stripped operating **loss**. The register reached the right verdict from a premise that does not support it |
| "failing the gross-profit bound by $46,951M" | The bound fires on **16 of 17** periods tested, not three, continuously since FY2024. It is a **screen**, not a classifier |
| "An artifact testing only for sign will pass VOYG and be wrong" | **Inverted.** VOYG is *caught* by a sign test (`|computed| == |reported|`, opposite signs). It is *missed* by a bound-only test, which cannot distinguish this from a genuine level defect |

### 5.2 The trap, restated correctly

The register's stated trap — "a detector testing only for *sign* passes VOYG and is wrong"
— does not hold. The real trap at VOYG is the mirror image, and it has two jaws:

1. **A bound-only detector misclassifies.** It fires on a sign-stripped loss and, absent
   the component identity, reports a *level* defect where the truth is a sign defect. That
   is exactly what happened to this entry.
2. **A naive "flip the negative" detector breaks on R&D.** Both FY2023 ($(18,542)K) and
   Q3 2024 ($(397)K) carry a *genuine* filed negative expense (§3.7) — required by the
   arithmetic and confirmed by the filer's own nine-month column. A detector that treats
   any negative expense as a sign-strip artefact inverts a correct value, twice.
   **VOYG punishes the sign test and the anti-sign test in the same filings.**

### 5.3 The classifier that settles it

**The component identity — `gross profit − opex`, run in-line — or equivalently the arc
set into `OperatingIncomeLoss`.** Both are capital-structure-independent, both are
insensitive to which document layer the value came from, and both close to the dollar at
VOYG on **17 of 17** periods. **It is the only admissible test that distinguishes a
sign-stripped loss from a genuine level defect**, which is the question this entry
actually poses. The register already requires it in the output contract
(`data_integrity_register_applied`); the VOYG entry shows what happens when the register
itself does not follow its own rule.

---

## 6. Data-integrity register — VOYG

| Register | Application to VOYG | Disposition |
|---|---|---|
| **DA-23** sign stripping | **FIRES.** `OperatingIncomeLoss` Q2 2026 `computed −51,408,000` vs `reported +51,408,000`, `|computed| == |reported|`, opposite signs. Component identity closes **17/17**. **Also: `GrossProfit` Q1 2026 stripped (+1,546 vs filed `(1,546)`), and FY2023 R&D has NO retrievable fact.** `EPS × shares` NOT used and independently disqualified (§4.2) | **PRESENT — the mechanism.** Register's sub-mechanism claim FALSIFIED |
| **DA-24** asset-sale contamination | No disposal gain in the operating line; positively excluded by **17/17** exact component identities. All non-operating items sit below the line | **NOT PRESENT** |
| **DA-25** normalised per-unit | Adjusted EBITDA 4/4, adjusted net loss per share 4/4, free cash flow 4/4, innovation spend 4/4 — all close on the issuer's own disclosed components | **NOT PRESENT** (reading stated in `definitions_used`) |
| **DA-26** annual as quarterly | Tested on two layers, with a third filing as the ladder check. Q4 2025 release prints a genuine Q4 column (46,651 / (34,029) / $(0.52) / 58,410,709) reconciling to the annual by subtraction; all 30 duration facts span-correct; Q3 2025 and 9M 2025 columns confirm the ladder exactly | **NOT PRESENT** on both layers |
| **DA-27** calendar-quarter labels | December year-end; register's own rule makes it exact; every fact aligns on calendar quarters | **NOT APPLICABLE** |
| **DA-28** IPO discontinuity | **PRESENT, two forms:** (i) within-table split discontinuity — Q4 2024 basic 8,758,462 beside FY2024 12,736,454; the **four-quarter reconstruction lands 8.6% low on the printed count and 4 shares off on the count × 1.5**; (ii) three non-agreeing Class A counts in one extract (53,598,000 / 53,598,284 / 55,270,494). EPS bridge closes 4-for-4 | **PRESENT — explains nothing here.** Guard still required |
| **NEW — outside-funding contra-expense** | NASA SAA grant assistance deducted from R&D **inside the operating line**: $3,305K Q2 2026, $8,895K H1 2026, $6,225K FY2025. R&D filed **negative** in two periods, FY2023 $(18,542)K and Q3 2024 $(397)K. All milestones earned; credit goes to zero from Q3 2026 | **PROMOTED.** Detector: **gross-R&D-note vs income-statement-R&D-line reconciliation** |
| **NEW — DA-28 detector coverage gap** | `EntityCommonStockSharesOutstanding` returns **zero facts** for VOYG, so a cover-page-keyed DA-28 detector silently clears an issuer with three Class A counts in one extract | **PROMOTED.** Detector: **primary-fact collision on concept+dimension+instant** |
| **NEW — DA-23 detector scope gap** | `ResearchAndDevelopmentExpense` has **no annual fact at all** for FY2023–FY2025; the nearest concept holds the *gross* figure, the wrong quantity. An **absence**, not a wrong value | **PROMOTED.** Detector: **assert fact presence per income-statement line per period** |
| **NEW — share-count concepts absent** | `WeightedAverageNumberOfSharesOutstandingBasic` and `WeightedAverageNumberOfDilutedSharesOutstanding` each return **zero facts for VOYG**, against 7,187 / 7,214 facts over 162 / 163 tickers platform-wide — so the concept names are right and the absence is issuer-specific. **Every EPS bridge in §4.1 is page-only** | **PROMOTED.** Detector: **same presence assertion, scoped to the EPS numerator/denominator pair** |

---

## 7. What could NOT be verified

1. **The FY2023 component identity from platform facts.** It closes from the filing page
   ([📄 VOYG 8-K p.40](https://agentii.ai/v/VOYG/sec19/40)) but **cannot** be closed from
   the XBRL fact set: the FY2023 `ResearchAndDevelopmentExpense` fact does not exist.
   Recorded as `UNRESOLVABLE-FROM-PLATFORM` **at the sub-item level**.
2. **Why the Q4 2025 release's Q4 2024 share count is unadjusted** (§4.3). The arithmetic
   is exact — the printed count lands 8.6% below the filed annual in a four-quarter
   reconstruction and the same count × 1.5 lands 4 shares away — and the 1.5× factor is
   unambiguous. **Whether it is a drafting error or an intentional basis choice is stated
   nowhere I read. The discrepancy is DEMONSTRATED; its cause is not.**
3. **Gross profit for the annual and Q3 periods.** Not filed as a subtotal anywhere: neither
   the FY2025 10-K ([📄 p.99](https://agentii.ai/v/VOYG/sec12/99)) nor the recast 8-K
   ([📄 p.40](https://agentii.ai/v/VOYG/sec19/40)) presents a gross-profit row. Every Δ row
   in §1.4 is **DERIVED** (net sales − cost of sales), not DEMONSTRATED as filed. The
   identities still close exactly, but they close *given* the derivation.
4. **The earnings-call transcripts.** Four VOYG transcripts exist (Q2 2026, Q1 2026,
   Q4/FY2025, Q3 2025) and were **not** screened. A DA-26 presentation-layer mislabel
   inside a transcript would not be caught by anything in this artifact.
5. **The Q4 2025 standalone `OperatingIncomeLoss` fact.** No such fact exists — only FY
   (108,498) and 9M (74,469, [📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec14/9)). The Q4
   figure of (34,029) is derived and confirmed from the release
   ([📄 VOYG 8-K p.11](https://agentii.ai/v/VOYG/sec7/11)), but it is not a fact.
6. **`skill_pin` — RESOLVED during this run.** The frontmatter pin is now the real content
   hash `07d26b9c738b`, computed by `dispatch.skill_version_hash()` (defined at
   `scripts/dispatch.py:132` of the agentii-investment-intelligence tree) over
   `/Users/frank/.claude/skills/agentii/recent-quarter/`. The algorithm was **not assumed**:
   it was validated by re-deriving the six pins already on record and reproducing
   **6 of 6 exactly** — `operational-kpi` `0730fd170124`, `unit-economics` `e87ee63269a2`,
   `secular-trends` `e6b41dbb2426`, `supply-chain` `8cb3ac1de486`, `competitive`
   `826995c722a4`, `risk` `953fc5d396e7`. An earlier draft of this artifact carried an
   `UNRESOLVED` gap string here; that gap was a limitation of the artifact context, not of
   the program, and it is now closed. Note the residual: the hash is over the *installed*
   skill directory, so a skill edit mid-thesis changes it — which is precisely what Q57
   intends the pin to detect.
7. **Any share-count quantity from the platform.** `WeightedAverageNumberOfSharesOutstandingBasic`
   and `WeightedAverageNumberOfDilutedSharesOutstanding` both return **zero facts** for VOYG
   (§3.8, §6). The EPS bridges in §4.1 and the 2024 quarterly counts in §4.3 come from
   filing pages across three separate filings, not from the fact set.
8. **The basic-versus-diluted divergence in the 2024 comparatives.** Q2 2024 filed basic EPS
   $(2.29) against diluted $(2.73), and H1 2024 $(3.88) against $(4.32)
   ([📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec13/9)) — **diluted more negative than
   basic on a net loss.** The denominators differ by ~0.02%, so the divergence is in the
   numerator; the $5,481K of preferred dividends accrued in the same column does not close
   it exactly. The 2025 and 2026 periods show basic = diluted throughout, so this is
   confined to the 2024 comparatives. **Not resolved.** It is not an `operating_income`
   figure and does not touch the $51.408M, but a reader comparing 2024 to 2025 loss-per-share
   trends will hit it.
9. **A $1K cross-table discrepancy between VOYG's own non-GAAP tables.** Free cash flow
   reports Q2 2025 purchases of property and equipment of $(30,895)K
   ([📄 p.53](https://agentii.ai/v/VOYG/sec18/53)) while the capital-expenditure table on
   the next page reports $30,894K ([📄 p.54](https://agentii.ai/v/VOYG/sec18/54)). H1 2025
   agrees at $57,865K. Immaterial, unrelated to any sign, noted so it is not silently
   normalised.

---

## 8. Carry-forwards

1. **PIL-3 — amend the register (§1b).** The VOYG entry's classification is falsified
   (§5.1). The gross-profit bound must be re-labelled a **screen**; the classifier is the
   component identity. **A bound-only detector cannot distinguish DA-23 from a genuine
   level defect, and this entry is the proof.**
2. **PIL-3 — four new register entries** (§3.7, §3.8, §6): the outside-funding
   contra-expense; the DA-28 primary-fact-collision coverage gap; the DA-23
   absent-fact/per-line-presence gap; and the absent share-count concepts (which take the
   `EPS × shares` test off the table for this issuer before admissibility is even reached).
3. **PIL-3 — the "three consecutive quarters" count is wrong for every issuer it was
   computed for by hand.** At VOYG the bound fires on **16 of 17** periods and has fired
   continuously since FY2024. Recompute programmatically or drop the count.
4. **PIL-6 — two R&D lines are genuine filed negatives** (FY2023 $(18,542)K, Q3 2024
   $(397)K). Any downstream consumer that "corrects" negative expense lines will corrupt
   both, and the Q3 2024 case sits inside a comparative column that a casual reader would
   never check. Flag VOYG explicitly.
5. **Forward-looking, for whoever picks up VOYG next:** the NASA SAA grant credit **goes to
   zero from Q3 2026** (all $217.5M of milestones earned as of 2026-06-30; $211.0M
   received). The Q2 2026 operating loss of $(51,408)K is understated by $3,305K against
   gross cost. **Expect a mechanical ~6% widening of the operating loss with no change in
   operations**, and do not read it as deterioration.

**Instrument caveat, per the standing rule.** `validate_calculation` on accession
`0001628280-26-052292` returned 9 pass / 0 warn / 11 fail. **The `fail` rows were not read
as failures.** One is a genuine positive (§1.3). Others are internally impossible on the
pair alone — `ProfitLoss` Q2 2025 `computed 60,784,000` vs `reported 33,065,000`, where the
computed side is H1 2025's pre-tax loss less Q2 2025's tax, i.e. a **3-month/6-month
column-mixing artefact** — and `PropertyPlantAndEquipmentNet` `computed −20,241,000` vs
`reported 154,983,000`. These corroborate rather than contradict the 93% false-positive
rate. **Only `computed` vs `reported` pairs for the concept in question were used, through
the component identity. The `status` column is not reported here.**

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Q2 2026 income statement — net sales 52,746; cost of sales 48,289; gross profit 4,457; SG&A 43,672; R&D 7,336; amortization of acquired intangibles 4, | [📄 VOYG 10-Q p.10](https://agentii.ai/v/VOYG/sec18/10) |
| Cover page — 'There were 55,270,494 shares of registrant's Class A common stock and 5,758,566 shares of Class B common stock outstanding as of July 31 | [📄 VOYG 10-Q p.4](https://agentii.ai/v/VOYG/sec18/4) |
| MD&A results of operations, three months — 'Loss from operations $ (51,408) | $ (24,137) | $ (27,271) | 113.0%' | [📄 VOYG 10-Q p.44](https://agentii.ai/v/VOYG/sec18/44) |
| MD&A results of operations, six months — 'Loss from operations $ (96,055) | $ (50,426) | $ (45,629) | 90.5%'; gross profit down 78.9% | [📄 VOYG 10-Q p.45](https://agentii.ai/v/VOYG/sec18/45) **(newly surfaced)** |
| Segment reporting — Q2 2026: Defense and Space Technologies net sales 53,211; Starlab 0; total reportable 53,211; intersegment eliminations (465); Tot | [📄 VOYG 10-Q p.33](https://agentii.ai/v/VOYG/sec18/33) **(newly surfaced)** |
| Government grants — 'When the government grant assistance is related to costs incurred, the assistance is deducted from the related expense'; NASA SAA | [📄 VOYG 10-Q p.43](https://agentii.ai/v/VOYG/sec18/43) |
| Key performance metrics — gross profit 4,457 / 8,210 / 2,911 / 13,795 (matching p.10); total backlog 335,512 vs 265,590; Adjusted EBITDA $(37,500) / $ | [📄 VOYG 10-Q p.51](https://agentii.ai/v/VOYG/sec18/51) **(newly surfaced)** |
| Adjusted EBITDA reconciliation — net loss attributable to Voyager (46,490) + finance and interest 1,905 + D&A 7,170 + tax (2,195) = EBITDA (39,610); + | [📄 VOYG 10-Q p.52](https://agentii.ai/v/VOYG/sec18/52) |
| Adjusted net loss per share reconciliation — net loss attributed to common shareholders (46,490) + SBC 3,762 + BAC 2,008 + restructuring 966 + deferre | [📄 VOYG 10-Q p.53](https://agentii.ai/v/VOYG/sec18/53) |
| Innovation spend — 'comprised of various costs recognized in cost of sales and research and development costs within our consolidated statements of op | [📄 VOYG 10-Q p.54](https://agentii.ai/v/VOYG/sec18/54) |
| Note 2 — 'On June 2, 2025, the Company effected a 1.5-for-1 forward split of its Common stock ... All share and per share information, including share | [📄 VOYG 10-Q p.18](https://agentii.ai/v/VOYG/sec18/18) |
| Q1 2026 income statement — net sales 35,246; cost of sales 36,792; Gross (loss) profit (1,546); SG&A 31,357; R&D 7,511; amortization 4,233; Loss from  | [📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec15/9) |
| Q1 2026 MD&A results of operations — 'Gross (loss) profit $ (1,546) | $ 5,585 | $ (7,131) | (127.7)%'; 'Loss from operations $ (44,647) | $ (26,289) | | [📄 VOYG 10-Q p.38](https://agentii.ai/v/VOYG/sec15/38) **(newly surfaced)** |
| Q2 2025 10-Q income statement — 2024 comparative weighted-average basic shares: Q2 2024 12,574,261; H1 2024 12,536,053 (diluted 12,577,013 / 12,538,80 | [📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec13/9) |
| Q3 2025 10-Q income statement — nine months ended September 30, 2024 weighted-average basic 12,603 (thousands) and Q3 2024 12,736 (thousands), the anc | [📄 VOYG 10-Q p.9](https://agentii.ai/v/VOYG/sec14/9) |
| FY2025 consolidated statements of operations — net sales 166,419; cost of sales 136,544; SG&A 117,085; R&D 12,753; impairment losses 0; amortization 8 | [📄 VOYG 10-K p.99](https://agentii.ai/v/VOYG/sec12/99) |
| Q4 2025 earnings release — condensed consolidated statements of operations. GENUINE Q4 column: net sales 46,651; cost of sales 36,661; SG&A 35,452; R& | [📄 VOYG 8-K p.11](https://agentii.ai/v/VOYG/sec7/11) |
| Q4 2025 earnings release non-GAAP tables — Q4 2025 net sales by segment total 46,651; Adjusted EBITDA reconciliation: net loss attributable to Voyager | [📄 VOYG 8-K p.13](https://agentii.ai/v/VOYG/sec7/13) **(newly surfaced)** |
| Recast 8-K (filed 2026-08-14) — consolidated statements of operations FY2025/2024/2023, UNCHANGED from the original 10-K: Loss from operations (108,49 | [📄 VOYG 8-K p.40](https://agentii.ai/v/VOYG/sec19/40) |
| Recast 8-K — Research and Development and Government Grants: 'For the years ended December 31, 2025 and 2024, gross research and development costs wer | [📄 VOYG 8-K p.20](https://agentii.ai/v/VOYG/sec19/20) |
| Recast 8-K — government grant assistance offset against research and development $6,225K (2025) and $5,420K (2024); offset against construction in pro | [📄 VOYG 8-K p.21](https://agentii.ai/v/VOYG/sec19/21) **(newly surfaced)** |
| Recast 8-K consent of independent registered public accounting firm — audit report dated March 10, 2026, noting 'the change in reportable segments eff | [📄 VOYG 8-K p.3](https://agentii.ai/v/VOYG/sec19/3) **(newly surfaced)** |
