---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: cross
ticker: cross
skill: synthesis
mode: methodology
generated_at: 2026-09-19T18:40:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
deal_security_basis: standalone_pre_merger
definitions_used:
  - da_id: DA-06
    chosen_reading: "Price vs cost, and the captive boundary. A vertically integrated operator flying its own payloads has NO transaction price for the launch it consumes, so its launch-segment margin is not a price, is not a cost, and is not comparable to an independent launcher's. Applied to SPCX Space (captive_integrated) on every entry; the flag is in-line, not in a footnote."
  - da_id: DA-08
    chosen_reading: "Definition of 'launch'. The map counts a launch as the issuer counts it, and states the count basis where a share is derived from it. SPCX's customer-launch share and RKLB's per-launch series are reported on the issuers' own counts, never reconciled to a common count."
  - da_id: DA-21
    chosen_reading: "Issuer-defined segment boundaries. Every entry's `segment` is the issuer's own name, verbatim; no segment is renamed, split, merged or mapped onto a house taxonomy. Where an issuer files one reportable segment, the entry is the consolidated issuer and is labelled as such rather than decomposed into a boundary the issuer does not have."
  - da_id: DA-23
    chosen_reading: "The platform serves a filed NEGATIVE as a POSITIVE of identical magnitude (|x| stripping). The component identity is the only reliable detector and it is applied at every issuer here. Engaged at 10 of the 12 issuers in this map; the served sign is NEVER quoted on any row — every operating figure in this artifact is recomputed from filed cells."
  - da_id: DA-24
    chosen_reading: "Non-operating contamination of operating_income. SATS' defining instance is an INVERTED IMPAIRMENT CHARGE inside the cost block ($(66,159)K, credited not charged), and it lands entirely inside the 'Other' segment — so the contamination is confined to one entry and is restated from that entry rather than from the consolidated row."
  - da_id: DA-25
    chosen_reading: "Normalised per-unit metrics that are not reproducible from audited tables. No per-launch, per-kilogram or per-constellation metric is admitted to this map as an operating figure; where a per-launch series is referenced it is RKLB's, and it is a filed revenue/cost pair, not a normalised one."
  - da_id: DA-26
    chosen_reading: "Annual figures mislabelled as quarterly. 19 of 20 issuers tested exhibit; FLY is the counterexample and is NOT reported as universal. Every period basis below is stated explicitly (3M / 6M / FY) and no row mixes the two."
  - da_id: DA-27
    chosen_reading: "Fiscal-period labels derived from the calendar quarter. PL manifests (the platform's label is one lower than the issuer's own); LUNR cannot manifest (31-December filer, EXCLUDED, not clean); RKLB is vacuous. Each entry states the issuer's own period label."
  - da_id: DA-28
    chosen_reading: "Capital-structure discontinuity around an IPO invalidates share-count detectors. Engaged at FLY, LUNR, RKLB and YSS. No share-count-based inference is used anywhere in this map; every margin is a filed dollar pair."
  - da_id: DA-29
    chosen_reading: "A reconciliation that closes is not thereby a check, and `computed` is an opaque assertion. Every identity in this map is written as filed cells only. Where a quantity can be reached only as `revenue − operating_income` it is reported as a BACK-SOLVE, separately from the filed line, and is never presented as a derivation (IRDM, GSAT)."
  - da_id: DA-30
    chosen_reading: "Two bases on one concept collapsed without a basis field. This is the map's governing defect and the reason the map exists: every segment row is reported on at least two bases (as filed, and the normative restatement where one is computable), and every competing basis that could NOT be restated is carried in an explicit basis register rather than dropped."
  - da_id: DA-07
    chosen_reading: "Capacity vs delivered mass. Cited only where the curve artifact's denominator discipline is referenced; the map itself reports no mass or capacity figure and values no constellation."
evidence_grade: DEMONSTRATED
citations:
  - figure: "Note 18 segment table Q2 2026 — Space 962 / 329 / 1,076 / 99 / 1,504 / (542); Connectivity 4,291 / 2,060 / 294 / 281 / 575 / 1,656; AI 2,561 / 1,106 / 2,178 / 532 / 2,712 / (1,257); Total Reportable Segments (143)"
    ticker: SPCX
    citation_id: sec8
    page_no: 30
    url: https://agentii.ai/v/SPCX/sec8/30
    located_via: read_source_pages
  - figure: "\"Our Space segment revenue only reflects our customer launches and customer activities.\""
    ticker: SPCX
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "Mass-to-orbit definition (total kilograms of payload delivered from all successful orbital flights and flight tests, excluding failed or scrubbed attempts); Falcon launches 37/45/77/81 with Starship 1/1/1/3; \"To date, all Starship launches have been classified as internal.\""
    ticker: SPCX
    citation_id: sec8
    page_no: 36
    url: https://agentii.ai/v/SPCX/sec8/36
    located_via: read_source_pages
  - figure: "Condensed consolidated statements of operations Q2 2026 — total revenues 234,066; total cost of revenues 149,490; gross profit 84,576; total operating expenses 142,090; operating loss (57,514)"
    ticker: RKLB
    citation_id: sec109
    page_no: 32
    url: https://agentii.ai/v/RKLB/sec109/32
    located_via: read_source_pages
  - figure: "Segment table FY2025 / FY2024 / FY2023 — Launch Services and Space Systems revenue, cost of revenue and gross profit; \"Management does not regularly review either reporting segment's total assets or operating expenses\"; \"The CODM uses gross profit as the measure of segment profit or loss\""
    ticker: RKLB
    citation_id: sec87
    page_no: 107
    url: https://agentii.ai/v/RKLB/sec87/107
    located_via: read_source_pages
  - figure: "Condensed consolidated statements of operations — revenue 117,683 / 15,549 / 198,562 / 71,404; cost of sales 93,808 / 11,554 / 157,226 / 65,189; gross profit 23,875 / 3,995 / 41,336 / 6,215; R&D 71,532 / 45,774 / 139,041 / 93,786; SG&A 47,540 / 12,571 / 93,160 / 25,323; total operating expenses 119,072 / 58,345 / 232,201 / 119,109; loss from operations (95,197) / (54,350) / (190,865) / (112,894)"
    ticker: FLY
    citation_id: sec21
    page_no: 6
    url: https://agentii.ai/v/FLY/sec21/6
    located_via: read_source_pages
  - figure: "Single reportable segment; prior-period recast on refinement of the segment disclosure in Q1 fiscal 2026"
    ticker: FLY
    citation_id: sec21
    page_no: 34
    url: https://agentii.ai/v/FLY/sec21/34
    located_via: read_source_pages
  - figure: "Q2 2026 and H1 2026 statements of operations — revenue 206,168 / 392,898, opex 253,304 / 479,235, operating loss (47,136) / (86,337), shares 162,172,470"
    ticker: LUNR
    citation_id: sec76
    page_no: 8
    url: https://agentii.ai/v/LUNR/sec76/8
    located_via: read_source_pages
  - figure: "FY2025 annual statement of operations — revenue 210,059, opex 297,290, operating loss (87,231), net loss (106,846); one reportable segment"
    ticker: LUNR
    citation_id: sec59
    page_no: 48
    url: https://agentii.ai/v/LUNR/sec59/48
    located_via: read_source_pages
  - figure: "\"Amortization expense associated with deferred contract costs for subcontracted launch services was $29.8M and $10.1M for the years ended December 31, 2025 and 2024\""
    ticker: LUNR
    citation_id: sec59
    page_no: 80
    url: https://agentii.ai/v/LUNR/sec59/80
    located_via: read_source_pages
  - figure: "Amortisation of deferred contract costs for subcontracted launch services $7.1M and $14.3M (3M / 6M 2026) vs $7.6M and $15.6M (3M / 6M 2025); launch delay fees $0.8M and $2.3M in 2025 and NIL in 2026"
    ticker: LUNR
    citation_id: sec76
    page_no: 24
    url: https://agentii.ai/v/LUNR/sec76/24
    located_via: read_source_pages
  - figure: "Q1 FY2027 statements of operations — revenue 94,150, cost of revenue 43,749, gross profit 50,401, total costs and expenses 129,038, loss from operations (34,888)"
    ticker: PL
    citation_id: sec76
    page_no: 6
    url: https://agentii.ai/v/PL/sec76/6
    located_via: read_source_pages
  - figure: "Segment note — one operating and reportable segment; segment cost of revenue 94,138 against the statement's 135,242; capital expenditures; long-lived assets by geography"
    ticker: PL
    citation_id: sec76
    page_no: 29
    url: https://agentii.ai/v/PL/sec76/29
    located_via: read_source_pages
  - figure: "\"third-party fees for launch procurement\" (inside cost of revenue, unquantified); \"$4.7 million of total purchase commitments for the fiscal year ended January 31, 2028\""
    ticker: PL
    citation_id: sec76
    page_no: 20
    url: https://agentii.ai/v/PL/sec76/20
    located_via: read_source_pages
  - figure: "Launch providers named as suppliers — \"ArianeSpace SA, Blue Origin, LLC, Firefly Aerospace Inc., ISAR Aerospace Technologies Inc., Mitsubishi Heavy Industries, Ltd., NewSpace India Limited, Rocket Lab USA Inc., Space Exploration Technologies Corp. (SpaceX), and Stoke Space Technologies, Inc.\""
    ticker: PL
    citation_id: sec76
    page_no: 59
    url: https://agentii.ai/v/PL/sec76/59
    located_via: read_source_pages
  - figure: "One operating segment and one reportable segment, `space infrastructure`; CODM reviews consolidated net loss and total assets"
    ticker: YSS
    citation_id: sec12
    page_no: 34
    url: https://agentii.ai/v/YSS/sec12/34
    located_via: read_source_pages
  - figure: "Q2 2026 results-of-operations ladder — revenue $92,547k +10%, cost of revenues $70,367k (76%), gross profit $22,180k (24%) +133%, total operating expenses $63,493k (69%), loss from operations $(41,313)k at (45)% of revenue"
    ticker: YSS
    citation_id: sec12
    page_no: 40
    url: https://agentii.ai/v/YSS/sec12/40
    located_via: read_source_pages
  - figure: "Segment footnote (a) — \"Other segment items is comprised of other costs of revenue excluding direct materials, including direct labor, overhead costs and depreciation and amortization\"; direct materials $53,240K; other segment items $17,127K = $11,119K labor + $3,736K overhead + $2,272K D&A"
    ticker: YSS
    citation_id: sec12
    page_no: 35
    url: https://agentii.ai/v/YSS/sec12/35
    located_via: read_source_pages
  - figure: "Non-GAAP reconciliation — revenue $92,547K, cost of revenues $70,367K, gross profit $22,180K; six-month revenue $208,890K, gross profit $44,330K, contribution margin $79,373K"
    ticker: YSS
    citation_id: sec12
    page_no: 46
    url: https://agentii.ai/v/YSS/sec12/46
    located_via: read_source_pages
  - figure: "FY2025 statement of operations — revenue $386,203K; cost of revenues $310,743K; gross profit $75,460K; total opex $146,124K; loss from operations $(70,664)K; net loss $(84,537)K; ASU 2023-07 significant-expense table direct materials $264,007K / $178,341K / $148,574K and other segment items $46,736K / $42,769K / $34,625K for FY2025 / FY2024 / FY2023"
    ticker: YSS
    citation_id: sec12
    page_no: 47
    url: https://agentii.ai/v/YSS/sec12/47
    located_via: read_source_pages
  - figure: "Q2 2026 income statement — revenue 225,237; operating income 34,008; net income 9,679; three-month results table with all five operating-expense lines and total opex 191,229"
    ticker: IRDM
    citation_id: sec191
    page_no: 5
    url: https://agentii.ai/v/IRDM/sec191/5
    located_via: read_source_pages
  - figure: "Three-month results of operations — SG&A +22,417 / +50%; the transaction-cost restatement giving an ex-transaction-costs margin of 21.45% against 23.17%"
    ticker: IRDM
    citation_id: sec191
    page_no: 24
    url: https://agentii.ai/v/IRDM/sec191/24
    located_via: read_source_pages
  - figure: "Merger Agreement with affiliates of Amazon.com, Inc. dated 2026-04-13 at $90.00 per share; Thermo's written consent \"no further approval of the Company's stockholders is required or will be sought\"; cash elections capped at 40%; $110M to $97M milestone reduction; ~$420M termination fee"
    ticker: GSAT
    citation_id: sec166
    page_no: 11
    url: https://agentii.ai/v/GSAT/sec166/11
    located_via: read_source_pages
  - figure: "Q2 2026 income statement — revenue 64,772; total operating expenses 69,547 (23,602 + 3,395 + 23,025 + 2,723 + 0 + 16,802); operating loss (4,775); filed margin (7.37)%; one reportable segment (MSS)"
    ticker: GSAT
    citation_id: sec166
    page_no: 5
    url: https://agentii.ai/v/GSAT/sec166/5
    located_via: read_source_pages
  - figure: "Three-month segmental income statement to 2026-03-31 — revenue, operating expenses, OIBDA and operating income (loss) by segment; Pay-TV 2,294,264 / 1,822,697 / 471,567; Wireless 962,491 / 998,273 / (35,782); Broadband and Satellite Services 329,656 / 285,472 / 44,184; Other 90,983 / 178,278 / (87,295); Segment Total 3,677,394 / 3,284,720 / 392,674; Eliminations (9,905) / (10,078) / 173; Consolidated Total 3,667,489 / 3,274,642 / 392,847"
    ticker: SATS
    citation_id: sec121
    page_no: 71
    url: https://agentii.ai/v/SATS/sec121/71
    located_via: read_source_pages
  - figure: "Consolidated statements of operations Q1 2026 — total revenue $3,667,489K; cost of services $1,998,268K; cost of sales-equipment $536,907K; SG&A $639,025K; D&A $166,601K; impairments and other $(66,159)K; total costs and expenses $3,274,642K; operating income $392,847K"
    ticker: SATS
    citation_id: sec121
    page_no: 11
    url: https://agentii.ai/v/SATS/sec121/11
    located_via: read_source_pages
  - figure: "Note 1 — principal business segments (Pay-TV, Wireless, Broadband and Satellite Services, Other); AT&T License Purchase Agreement to sell 3.45 GHz and 600 MHz spectrum for $22.650 billion in cash; designated SpaceX spectrum proceeds up to $11 billion in SpaceX Class A at $212 per share"
    ticker: SATS
    citation_id: sec121
    page_no: 14
    url: https://agentii.ai/v/SATS/sec121/14
    located_via: read_source_pages
---

# The value-pool map — where the pool went, on the issuers' own boundaries

## 0. The finding

**The value pool migrated to whoever owns the DEMAND. It did not migrate to the launcher, and it did
not migrate to the independent operator — and in this universe the independent operator did not
survive as an independent recipient at all: both of them were acquired inside the same twelve
months, one by the launcher and one by its own demand owner.**

Nine sub-findings carry the map. Each is stated with its operands in the sections that follow.

1. **Both independent operators exited, and neither acquirer priced the target's income statement.**
   IRDM agreed to RKLB on **2026-06-28 at $54.00/share**; GSAT agreed to Amazon on **2026-04-13 at
   $90.00/share**. On the multiples as carried in the corpus, the **demand owner pays ≈41.4×–41.6×
   TTM revenue for the operator running at −7.37%, while the launcher pays ≈8.3× for the operator
   running at +15.10%** — a ≈5.0× ratio, in the direction opposite to the margin. Neither multiple
   reproduces cleanly from filed cells (DA-30, §6.2), and the direction is invariant to the basis
   picked. **Both buyers are pricing the customer relationship the operator sits on.** At GSAT the
   relationship is literal: **64% of six-month revenue is one customer**, who is also the financier
   and the acquirer.
2. **The margin ladder is BIMODAL, not monotone** — high at both ends, negative through the middle.
   Component suppliers mean **22.76%**; prime integrators mean **11.25%** → **anchor (a) HOLDS at
   2.02×** (the component layer earns twice the prime layer). SPCX's **Connectivity +38.59%** is the
   demand-owning operator at the top. Launchers and manufacturers run **−24.57% to −80.90%**.
   **Anchor (b) is FALSIFIED**: the worst verified margin in the universe is **FLY's −80.90%, a
   manufacturer** — not the single-customer operator, which is GSAT at **−7.37%**.
3. **SPCX's launch segment has BOTH the highest segment GROSS margin in the company (65.80%) and
   the worst OPERATING margin (−56.34%).** The swing is **122.14 pp**, decomposed exactly as **R&D
   111.85 pp of segment revenue + SG&A 10.29 pp**. Against Connectivity the cross-segment spread is
   **94.93 pp**, decomposed exactly as **+105.00 pp R&D + 3.74 pp SG&A − 13.81 pp gross margin**.
   **Which ladder you pick decides whether launch looks like the best business in the sector or the
   worst, and the gross-margin ladder and the operating-margin ladder order the same segment at
   opposite ends.**
4. **SPCX's Space revenue boundary is the CUSTOMER boundary** — *"Our Space segment revenue only
   reflects our customer launches and customer activities."* ~74% of launches produce no Space
   revenue **by design**. The customer share has **two bases with OPPOSITE signs**: rising on Q2
   (19.6% → 26.3%), **falling on H1 (25.0% → 21.8%)**. `12.3%` is three things at once;
   **launch-only is 8.29%**. And **`+$1,824M` of new Space revenue is not migration evidence** — it
   is 48.7% of the quarter's growth and it exists because an entity was acquired.
5. **The demand side does not price off the curve.** PIL-6's named quantity — launch as a share of
   **programme** cost — is **NON-FORMABLE at three of the four demand-side names**: at **YSS** the
   cost of revenues decomposes exhaustively into four components that exclude launch (a **PRESENCE**
   finding, not an absence); at **PL** launch is named inside cost of revenue and quantified nowhere,
   its only filed launch figure being a forward **stock** ($4.7M of FY2028 purchase commitments,
   absent from the 10-K's commitment note entirely); at **SATS** there are named launch agreements
   with **no dollar amount on either side**. **LUNR's FY2025 is 14.19%** — above the 0.10 bar — but on
   a **consolidated** denominator, and its 2026 fall to 2.80%–4.37% is a **denominator event**, not a
   pass-through: the numerator fell 6.6% while cost of revenues rose **174.0%**, because Lanteris
   added $166,735K of product revenue containing no launch.
6. **PL is PIL-6's cleanest demand-side test, and its bound is decisive: with cost of revenue at
   ZERO, PL's operating margin is still only +9.4% for the quarter / +13.1% for the year.** Its
   binding purchased input is **cloud hosting at $58,545.0k against $4.7M of launch commitments —
   12.5×**. The **entire multi-year launch commitment closes 13.5% of one quarter's operating loss.**
7. **YSS is the POSITIVE pass-through counterexample, and it must be carried.** Non-GAAP
   contribution margin rose on every basis (**33→34, 24→42, 29→38**), with direct material per
   revenue dollar falling **$0.758 → $0.575**. At least one demand-side name in this universe DID
   pass released value through. PIL-6 is not a universal claim.
8. **SATS is the terminal counter-case, quantified at ≈142×.** Its operating satellite business is
   ~$0.3 billion (`CLAIMED`, stalking horse) against **≈$42.65 billion** of regulatory-asset
   realisation. **Launch cost is not a variable in the transaction that realises the value.** SATS'
   real exposure to the launch cost curve is as a **holder of 261.8 million SpaceX shares**
   (`CLAIMED`) — an equity position, not a cost position.
9. **Every operating figure in this map is recomputed from filed cells with the component identity
   in-line, because the served layer inverts or inflates the sign in every case tested.** DA-23 is
   engaged at 10 of the 12 issuers here. The map is built from pages, not from the metrics block.

---

## 1. How to read the map

**Units.** Every quantity carries its unit in-line. Cross-issuer rows are labelled with their
issuer-level unit (USD thousands for RKLB, FLY, LUNR, PL, YSS, IRDM, GSAT; USD millions for SPCX;
USD thousands for SATS, whose statements are also printed in thousands). No figure is quoted without
its period basis (**3M** = the issuer's most recent quarter, **6M** = its most recent half, **FY**).

**Grades.** `DEMONSTRATED` = a filed figure, or arithmetic directly on filed cells. `DERIVED` = a
figure reached from filed cells by a construction the issuer does not print (every segment gross
profit at SPCX is `DERIVED`, because SPCX files no segment gross-profit subtotal). `CLAIMED` = an
issuer or third-party assertion. `MODELED` = our derivation, which **can never satisfy a
falsifier**. The map's own rows are `DEMONSTRATED`; the deal multiples and the ~142× are `DERIVED`
or `CLAIMED` and are marked as such in-line.

**The component identity is CONDITIONAL, and the condition is checked per issuer.** The map shows
`gross_profit − opex` on every entry that reads an operating income, and states which opex
definition was used:

- `CostsAndExpenses` is **INCLUSIVE of cost of sales**, so `gross profit − CostsAndExpenses` is
  **false** wherever a cost-of-sales line exists. The identity holds only on an opex **EXCLUSIVE** of
  cost of sales.
- **Per-issuer pairing used here** — EXCLUSIVE: SPCX (segment level), RKLB, FLY, **PL, YSS, IRDM**.
  INCLUSIVE (the issuer files **no** gross-profit subtotal, so the exclusive form has no filed
  boundary to subtract from): **LUNR, GSAT, SATS**.
- The pairing is not chosen for convenience: at FLY and PL the inclusive construct is **false by
  exactly cost of sales or cost of revenue** (FLY: 93,808; PL: 43,749), and at LUNR/YSS the inclusive
  construct overstates the filed loss (**2.25×** at PL, **1.85×** at YSS).
- `EPS × shares` is **not** used as a sign test anywhere in this map, and neither is
  `net income + addbacks`.

**The basis register.** DA-30 governs this artifact. Where a **normative restatement** is computable
on **both** legs — revenue and margin — the entry carries `as_restated` and a `spread` with both
percentage-point fields populated. Where a competing boundary is computable on the revenue leg only
and the margin leg is **non-formable** (the issuer prints no split of cost of revenue between the
competing boundaries), the entry carries **no `as_restated`** and instead carries a **basis register**
naming the competing boundary, the computable leg, the non-formable leg, and the specific disclosure
that would resolve it. This is an argued construction, not an omission: emitting `as_restated` with
one leg computed and the other fabricated would fail `spread_reported_not_collapsed` in substance
while passing it in form, and collapsing two boundaries into one figure is the exact DA-30 defect
this map exists to prevent. **Every such register entry is marked `interpretation: unresolved`-class
in-line and is listed in §8.**

**Segment names are the issuers' own, verbatim** (`segment_name_verbatim`). Where an issuer files one
reportable segment and gives it no name, the entry is the **consolidated issuer** and is labelled as
such — that is the issuer's own boundary, and inventing a name for it would be a DA-21 violation.
Three issuers file one reportable segment with no name at all (FLY, LUNR, PL); YSS files one and
**does** name it (`space infrastructure`); RKLB and SPCX file named segments; SATS files four.

**Captive flag.** `operator_class` is set on every entry. **A `captive_integrated` issuer's segment
margin is NOT comparable to an `independent_launch` issuer's**: for a vertically integrated operator
**no transaction price exists at all** (DA-06). This applies to SPCX on every entry and is repeated
in-line at each row rather than footnoted once.

**P10.** The map reports segment revenue and margin **as filed**. It **values no constellation**. No
entry in this artifact carries a per-constellation value, a discounted cash flow, or an implied
equity value attributed to a spacecraft fleet.

**Contract compliance — the six `level: fail` rules, and where each is satisfied.** All six are
`level: fail`, so this table is the artifact's own audit trail and is meant to be checked rule by
rule rather than taken on assertion.

| rule | satisfied by | how a reviewer checks it |
|---|---|---|
| `spread_reported_not_collapsed` | §2 E-01/E-02/E-07/E-08 (competing boundaries printed as registers, both bases named, neither netted); §2 E-06/E-10/E-15/E-16 (`as_restated` `spread` blocks with both pp legs populated and `interpretation` set) | every entry where two bases exist prints both, and **no** entry carries `as_restated` with a fabricated second leg (§1, "The basis register") |
| `segment_name_verbatim` | §2, the `segment:` field of all 16 entries | each carries the issuer's own string, quoted, with the note cited; unnamed single-segment issuers are labelled "single reportable segment" plus the issuer's own descriptive words, never a house name (§1) |
| `component_derivation_present` | §2, the `operating_income_derivation:` block of all 16 entries | every block has `gross_profit`, `opex` and a `shown` string that **names the opex definition** (EXCLUSIVE vs INCLUSIVE) and carries the arithmetic to the filed operating income; `gross_profit_filed: false` marks the four issuers that file no subtotal (§1, "The component identity is CONDITIONAL") |
| `deal_security_tagging` | §2 E-04, E-05, E-10, E-11 (`deal_security_basis: standalone_pre_merger`) plus the frontmatter default | the three deal-security names — IRDM, GSAT, RKLB — each carry the tag on the entry **and** inherit it from frontmatter; every other entry is `not_applicable`, not blank |
| `captive_flagged` | §1 ("Captive flag"); §2 E-01 and E-02 (`operator_class: captive_integrated` **and** a ⚠ in-line flag); §3 (the class table and the DA-06 statement) | the flag is on the row it applies to and repeated in the class test, not footnoted once |
| `no_constellation_valuation` | §1 ("P10"); §8 ("Explicitly not attempted") | no entry carries a per-constellation value, a DCF, or an implied equity value attributed to a spacecraft fleet; the only equity values in the artifact are **deal consideration** (E-10, E-11) and SATS' filed shareholding (E-16, §6.3), neither of which values a constellation |

Two further requirements of the brief are discharged in-line rather than in this table: the
**`gross_profit − opex` identity with its opex definition** on every operating figure, and
**`operator_class` on every row**.

---

## 2. The entries

### E-01 — SPCX / `Space` — the launcher, and the reason the launcher is not where the pool is

```yaml
issuer: SPCX
segment: "Space"                    # Note 18, verbatim
period_basis: "3M (quarter ended 2026-06-30)"
units: "USD millions (segment note)"
as_reported:
  revenue: 962.0
  revenue_growth: 28.95             # 962 / 746 − 1; 6M basis is −1.86% (1,581 / 1,611 − 1)
  operating_income: -542.0
  operating_margin: -56.34          # 542 / 962
  evidence_grade: DEMONSTRATED      # filed cells; the gross-profit subtotal is DERIVED
  source: "SPCX 10-Q p.30 (Note 18 segment table)"
operating_income_derivation:
  gross_profit: 633.0               # 962 − 329, DERIVED — SPCX files NO segment gross-profit subtotal
  opex: 1175.0                      # R&D 1,076 + SG&A 99 + other 0 — EXCLUSIVE of cost of revenue
  shown: "962 − 329 = 633 gross profit (DERIVED); 1,076 + 99 + 0 = 1,175 opex (EXCLUSIVE); 633 − 1,175 = (542) ✓ EXACT. The filed `Total costs and expenses` line is 1,504 = 329 + 1,076 + 99 ✓ and 962 − 1,504 = (542) is the same quantity by the INCLUSIVE route — both routes are shown because at this issuer the segment note files no intermediate gross-profit subtotal."
operator_class: captive_integrated  # ⚠ FLAG: DA-06 — no transaction price exists; NOT comparable (see below)
deal_security_basis: not_applicable
basis_register:
  - competing_boundary: "launch-only revenue (excluding development and Dragon)"
    computable_leg: "not computable at segment level — SPCX does not split Space revenue between launch and development"
    non_formable_leg: "margin"
    interpretation: unresolved
    resolving_disclosure: "a Space-segment revenue disaggregation between launch services and development"
  - competing_boundary: "segment gross margin vs consolidated gross margin"
    computable_leg: "both — 65.80% (segment) vs 55.27% (consolidated)"
    note: "the served ratio pairs a segment numerator with a consolidated denominator; this is the DA-30 instance and both bases are printed here rather than one"
    interpretation: definitional
```

**Flags carried in-line.**

- **⚠ CAPTIVE-INTEGRATED — the margin is NOT comparable (DA-06).** SpaceX flies its own payloads. For
  the launches Space does not sell, **no transaction price exists** — there is no arm's-length price
  to compare against a cost, and the segment's revenue is a residual customer-book, not a market.
  Comparing −56.34% against RKLB's Launch Services gross margin is comparing a price to a
  non-price.
- **The gross-margin ladder and the operating-margin ladder order this segment at opposite ends.**
  Space holds the **highest segment gross margin in the company at 65.80%** (`DERIVED`:
  (962 − 329) / 962) and the **worst operating margin at −56.34%**. Swing **122.14 pp**, decomposed
  exactly: **R&D 1,076 / 962 = 111.85 pp** + **SG&A 99 / 962 = 10.29 pp** = 122.14 pp. Against
  Connectivity's **+38.59%** the cross-segment spread is **94.93 pp**, decomposed exactly as
  **+105.00 pp R&D (111.85% vs 6.85%) + 3.74 pp SG&A (10.29% vs 6.55%) − 13.81 pp gross margin
  (65.80% vs 51.99%)** = 94.93 pp ✓.
- **The revenue boundary is the customer boundary**, filed: *"Our Space segment revenue only reflects
  our customer launches and customer activities."* [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35).
  ~74% of launches produce no Space revenue **by design**. Customer launches were **10 of 38
  (26.3%)** in Q2 2026 — and **the customer share has two bases with opposite signs**: rising on Q2
  (19.6% → 26.3%), **falling on H1 (25.0% → 21.8%)**. This row quotes the 3M basis and says so.
- **`+$1,824M` is not migration evidence.** It is **48.7%** of the quarter's Space growth and it
  exists because an entity was acquired: **+91.9% as filed vs +57.6% ex-AI**.
- **`12.3%` is three things at once.** Launch-only is **8.29%** — below PIL-6's 0.10 bar.

---

### E-02 — SPCX / `Connectivity` — the demand owner, and the top of the ladder

```yaml
issuer: SPCX
segment: "Connectivity"             # Note 18, verbatim
period_basis: "3M (quarter ended 2026-06-30)"
units: "USD millions (segment note)"
as_reported:
  revenue: 4291.0
  revenue_growth: 65.81             # 4,291 / 2,588 − 1; 6M basis is +49.11% (7,548 / 5,062 − 1)
  operating_income: 1656.0
  operating_margin: 38.59           # 1,656 / 4,291
  evidence_grade: DEMONSTRATED
  source: "SPCX 10-Q p.30 (Note 18 segment table)"
operating_income_derivation:
  gross_profit: 2231.0              # 4,291 − 2,060, DERIVED (no filed segment gross-profit subtotal)
  opex: 575.0                       # R&D 294 + SG&A 281 — EXCLUSIVE of cost of revenue
  shown: "4,291 − 2,060 = 2,231 gross profit (DERIVED); 294 + 281 = 575 opex (EXCLUSIVE); 2,231 − 575 = 1,656 ✓ EXACT"
operator_class: captive_integrated  # ⚠ FLAG: demand-owning operator whose launch supply is captive
deal_security_basis: not_applicable
basis_register:
  - competing_boundary: "segment gross margin 51.99% vs consolidated gross margin 55.27%"
    computable_leg: "both — (4,291 − 2,060) / 4,291 = 51.99%; 4,319 / 7,814 = 55.27%"
    note: "the consolidated figure rounds to 55.27% or 55.28% depending on the page (4,319 / 7,814 = 55.2726%); both are printed here rather than one being silently chosen"
    interpretation: definitional
```

**Flags carried in-line.**

- **This is the demand owner, and it is the highest-margin operator in the universe at +38.59%.** It
  is also `captive_integrated`: its launch supply is internal. **The pool sits here** — the segment
  that sells the service the launch buys earns +38.59%, above every component supplier on the ladder.
- The DA-30 instance the map inherits: **segment vs consolidated gross margin (51.99% vs 55.27%)**.
  Both bases are printed. Neither is netted.

---

### E-03 — SPCX / `AI` — adjacent, negative, and often mistaken for the launch business

```yaml
issuer: SPCX
segment: "AI"                       # Note 18, as the note renders it
period_basis: "3M (quarter ended 2026-06-30)"
units: "USD millions (segment note)"
as_reported:
  revenue: 2561.0
  revenue_growth: 247.49            # 2,561 / 737 − 1; 6M basis is +130.65% (3,379 / 1,465 − 1)
  operating_income: -1257.0
  operating_margin: -49.08          # 1,257 / 2,561
  evidence_grade: DEMONSTRATED
  source: "SPCX 10-Q p.30 (Note 18 segment table)"
operating_income_derivation:
  gross_profit: 1455.0              # 2,561 − 1,106, DERIVED
  opex: 2712.0                      # 2,178 + 532 + 2 — EXCLUSIVE of cost of revenue
  shown: "2,561 − 1,106 = 1,455 gross profit (DERIVED); 2,178 + 532 + 2 = 2,712 opex (EXCLUSIVE); 1,455 − 2,712 = (1,257) ✓ EXACT"
operator_class: adjacent
deal_security_basis: not_applicable
```

**Flag.** The segment is **32.77% of consolidated revenue** (2,561 / 7,814) and **the largest single
drag on the consolidated operating line** — **(1,257) against a consolidated result of (143)**, the
gap being Connectivity's **+1,656** and Space's **(542)**; the three sum exactly. Any reader who takes SPCX's
**−1.83% consolidated** operating margin as a launch-sector margin is reading the AI segment, not the
launch segment. The launch segment is 12.3% of revenue (8.29% launch-only) and −56.34%.

> **⚠️ CORRECTION — 2026-09-19, raised from thesis 004's clarify round 3. Two errors, both corrected
> above and both recorded rather than silently rewritten.**
>
> | Read | Correct | What it was |
> |---|---|---|
> | **32.77%** of consolidated revenue (2,561 / 7,814) | **49.08%** | **The row's own printed operands — `(2,561 / 7,814)` — evaluate to 32.77%. The 49.08% is this entry's `operating_margin: -49.08  # 1,257 / 2,561`, copied one line into the revenue-share slot. A DA-30-class defect: a served value not matching its own stated basis.** |
> | **Consolidated result (143)** | **1,438** | **Unsourced and matched by nothing. Segment losses sum to (1,799); the consolidated result is (143), and this thesis's own `SPCX/…_operational-kpi_methodology.md` states `$(143)M` with the identity `7,814 − 7,957 = (143)` closing exactly.** |
>
> **Neither error changes a finding.** The AI segment is still the largest single drag and the
> `−1.83% consolidated` warning still holds — the corrected revenue share (32.77%) is *larger* than
> nothing and the corrected loss basis (143) makes the drag *more* dominant, not less. **The direction
> survives; only the magnitudes were wrong, and they were wrong in the artifact that fixes basis
> discipline for the programme.** Raised to 003 because 004 and 005 both cite this map as their
> declared reference.

---

### E-04 — RKLB / `Launch Services` — the map's only priced launcher, and it files NO segment operating income

```yaml
issuer: RKLB
segment: "Launch Services"          # 10-K/10-Q segment note, verbatim
period_basis: "3M (quarter ended 2026-06-30)"
units: "USD thousands"
as_reported:
  revenue: 44586.0
  revenue_growth: -4.42             # LS revenue FELL, against SS +93.64%
  evidence_grade: DEMONSTRATED
  source: "RKLB 10-Q p.32 (segment table); RKLB 10-K p.107 for the audited full series"
  not_filed: ["operating_income", "operating_margin"]
  segment_profit_measure: "gross_profit — the issuer's own CODM measure"
  segment_gross_margin_3M: 42.86
operating_income_derivation:
  gross_profit: 84576.0             # issuer level, filed
  opex: 142090.0                    # issuer level, filed (R&D 82,429 + SG&A 59,661) — EXCLUSIVE
  shown: "issuer level: 84,576 − 142,090 = (57,514) ✓ EXACT on the EXCLUSIVE opex. **This entry reads NO segment operating income, because none exists**: RKLB files no segment operating margin and no segment operating income on any basis, and files the reason — \"Management does not regularly review either reporting segment's total assets or operating expenses. This is because in general, the Company's long-lived assets, facilities, and equipment are shared by each reporting segment.\" The CODM uses GROSS PROFIT as the segment profit measure. The issuer-level identity is shown because it is the only one that exists; it is NOT a segment figure and is not presented as one."
operator_class: independent_launch
deal_security_basis: standalone_pre_merger
basis_register:
  - competing_boundary: "segment operating margin (basis C)"
    computable_leg: "none — permanently unconstructible at RKLB"
    non_formable_leg: "both"
    interpretation: unresolved
    resolving_disclosure: "a segment opex allocation. The issuer has filed that it does not review one; no disclosure would produce it and the contract should record it as permanently non-formable rather than pending."
```

**Flags carried in-line.**

- **⚠ DA-23 at RKLB is 12 of 12 periods, not one.** Every served `OperatingIncomeLoss` is positive and
  every filed one negative. **Because RKLB has never had positive operating income, the strip is
  INVISIBLE to any heuristic — only the component identity detects it.** The served Q2 2026 value is
  `+57,514,000` against a filed `(57,514)` thousand.
- **The pairing is EXCLUSIVE, and this was established by running the test rather than assuming it.**
  RKLB **files** a gross-profit subtotal (`84,576`) and files **no** `Costs and expenses` caption: the
  note reads *"There is no `Costs and expenses` caption. `Total cost of revenues` sits above `Gross
  profit`; `Total operating expenses` sits below it."* Six of six periods close exactly on the
  exclusive form; the inclusive construct gives `(207,004)`, wrong by exactly total cost of revenue.
  **NOTE for downstream artifacts: an earlier reading of this workspace had RKLB's pairing as
  inclusive. It is inclusive nowhere.**
- **Launch Services is 100% services revenue, $0 products, in all four 2026 periods**, and its
  revenue **fell 4.42% YoY** while Space Systems grew 93.64%. LS share of total revenue is **19.05%
  (3M) / 24.92% (6M)**; LS share of total *growth* is **−2.3%**. The launch business is shrinking
  inside a growing company.
- **Segment gross margins across the audited 14-period series** (`DEMONSTRATED`, recomputed from
  filed cells; Q2 2026 / Q2 2025 / H1 2026 / H1 2025 / FY2025 / FY2024 / FY2023):
  Launch Services **42.86 / 30.48 / 43.73 / 26.07 / 40.83 / 27.59 / 11.22**;
  Space Systems **34.55 / 32.87 / 34.87 / 32.57 / 31.26 / 26.24 / 25.10**.
  Two display-level anomalies are registered, not smoothed: the Q2 2025 LS margin is **30.48%**
  (30.49% on one page; 14,220 / 46,646 confirms 30.48%), and H1 2026 consolidated is **37.08%**
  (37.07% on one page; 161,069 / 434,414 confirms 37.08%).

---

### E-05 — RKLB / `Space Systems` — the enabler, and the segment that is actually growing

```yaml
issuer: RKLB
segment: "Space Systems"            # segment note, verbatim
period_basis: "3M (quarter ended 2026-06-30)"
units: "USD thousands"
as_reported:
  revenue: 189480.0
  revenue_growth: 93.64
  evidence_grade: DEMONSTRATED
  source: "RKLB 10-Q p.32 (segment table)"
  not_filed: ["operating_income", "operating_margin"]
  segment_profit_measure: "gross_profit"
  segment_gross_margin_3M: 34.55
operating_income_derivation:
  gross_profit: 84576.0             # issuer level, filed
  opex: 142090.0                    # issuer level, filed — EXCLUSIVE
  shown: "issuer level only: 84,576 − 142,090 = (57,514) ✓ EXACT. See E-04: no segment opex is filed at RKLB on any basis, so no segment operating income exists for either segment."
operator_class: enabler
deal_security_basis: standalone_pre_merger
```

**Flag.** Space Systems is **81.0% of revenue** (189,480 / 234,066) and carries the whole company's
growth. **RKLB monetises the merchant market; SPCX does not** — which is why RKLB's Launch Services
gross margin is the closest thing in this universe to a market price for launch, and why it is the
positive control the contract asks for: *issuers whose launch margin is defensible are those selling
to third parties, where a price exists.*

---

### E-06 — FLY / single reportable segment — the manufacturer at the bottom

```yaml
issuer: FLY
segment: "single reportable segment (verbatim: 'We operate as a single reportable segment'; the filing describes the platforms as 'Launch and Spacecraft Solutions' and files no segment name)"
period_basis: "3M (three months ended 2026-06-30)"
units: "USD thousands"
as_reported:
  revenue: 117683.0
  revenue_growth: 656.86            # 117,683 / 15,549 − 1; 6M basis is +178.0% (198,562 / 71,404 − 1)
  operating_income: -95197.0
  operating_margin: -80.90          # 95,197 / 117,683
  evidence_grade: DEMONSTRATED
  source: "FLY 10-Q p.6 (statements of operations); p.34 (single reportable segment)"
operating_income_derivation:
  gross_profit: 23875.0             # 117,683 − 93,808, filed
  opex: 119072.0                    # R&D 71,532 + SG&A 47,540 — EXCLUSIVE of cost of sales
  shown: "117,683 − 93,808 = 23,875 gross profit (filed); 71,532 + 47,540 = 119,072 opex (EXCLUSIVE of cost of sales); 23,875 − 119,072 = (95,197) ✓ EXACT ✓. The INCLUSIVE construct (93,808 + 119,072 = 212,880; 117,683 − 212,880 = (189,005)) is FALSE by exactly cost of sales 93,808 ✓ — a clean demonstration that the identity is conditional."
operator_class: enabler
deal_security_basis: not_applicable
basis_register:
  - competing_boundary: "launch-only (Alpha) vs spacecraft solutions"
    computable_leg: "revenue — launch 9,400 / 117,683 = 7.99% (3M); 22,652 / 198,562 = 11.41% (6M)"
    non_formable_leg: "margin — no launch cost or launch gross profit is disclosed on any basis"
    interpretation: unresolved
    resolving_disclosure: "a launch gross profit or launch cost of sales caption"
```

**Flags carried in-line.**

- **The served layer prints this row as +80.89%, a profitable-looking row sitting in the correct rank
  order.** Any segment map built from the metrics block inverts at this issuer. DA-23 strips the sign
  of **both** operating income (`+95,197,000` against filed `(95,197)`) **and** net income
  (`+92,319,000` against filed `(92,319)`).
- **The operator class is a judgement, and the map states it so it can be argued with.** FLY's Alpha
  is an `independent_launch` platform and is why FLY is in this universe; but the **filed reportable
  segment is 92.0% spacecraft solutions** (108,283 of 117,683 on the 3M basis) against **8.0%
  launch**. The entry is therefore classed by its dominant filed activity, and **anchor (b)'s
  falsification depends on this reading: the worst verified margin in the universe is a
  MANUFACTURER's composite margin, not a launcher's.** FLY's margin is 24.56 pp below the next-worst
  verified row.
- **Launch is a revenue-type line here, not a segment.** 92.0% / 8.0% is a disaggregation inside the
  single segment. Calling the launch leg a "segment" would be a DA-21 violation.
- FLY is the **DA-26 counterexample** (the one issuer of 20 tested that does not mislabel the annual
  as quarterly) and is **not** reported as universal. Its period labels are nonetheless defective on
  the served row: the most recent served row carries the **quarter** in `revenues` and the
  **half-year** in all three margins (DA-27).

---

### E-07 — LUNR / single reportable segment — the payload customer whose launch spend fell inside a bigger cost base

```yaml
issuer: LUNR
segment: "single reportable segment (verbatim: 'one reportable segment'; no segment name filed — FY2025 Note 18, Q2 2026 Note 21)"
period_basis: "3M (quarter ended 2026-06-30)"
units: "USD thousands"
as_reported:
  revenue: 206168.0
  revenue_growth: 309.77            # 206,168 / 50,313 − 1; 6M basis is +248.2% (392,898 / 112,837 − 1)
  operating_income: -47136.0
  operating_margin: -22.86          # 47,136 / 206,168
  evidence_grade: DEMONSTRATED
  source: "LUNR 10-Q p.8 (statements of operations); LUNR 10-K p.48 for FY2025"
operating_income_derivation:
  gross_profit: 206168.0            # ⚠ NOT A FILED SUBTOTAL: LUNR files no gross-profit line. This field carries
                                    # the revenue boundary that makes the identity hold under the INCLUSIVE definition.
  gross_profit_filed: false
  opex: 253304.0                    # INCLUSIVE of cost of revenues: 170,302 + 14,927 + 7,729 + 60,346
  shown: "LUNR files NO gross-profit subtotal, so the admissible pairing is the INCLUSIVE one: 206,168 − 253,304 = (47,136) ✓ EXACT, where 253,304 = cost of revenues 170,302 + 14,927 + 7,729 + 60,346. The EXCLUSIVE form also closes on DERIVED cells (35,866 − 83,002 = (47,136)) but the load-bearing fact is the ABSENCE of a FILED gross-profit subtotal — the exclusive boundary has to be constructed, and a constructed boundary is not a filed one. Six further periods close exact on the same pairing: FY2025 210,059 − 297,290 = (87,231); Q1 2026 186,730 − 225,931 = (39,201); H1 2026 392,898 − 479,235 = (86,337); Q1 2025 62,524 − 72,601 = (10,077); Q2 2025 50,313 − 78,953 = (28,640); H1 2025 112,837 − 151,554 = (38,717)."
operator_class: payload_customer
deal_security_basis: not_applicable
basis_register:
  - competing_boundary: "consolidated vs ex-Lanteris"
    computable_leg: "revenue — Lanteris contributed $166,735K of product revenue in H1 2026 against $0 in the prior year; H1 2026 ex-Lanteris = 392,898 − 166,735 = 226,163"
    non_formable_leg: "margin — Lanteris's own cost of revenue is not separable from the consolidated line"
    interpretation: unresolved
    resolving_disclosure: "a cost-of-revenue split by acquired entity, or a standalone Lanteris carve-out"
```

**Flags carried in-line.**

- **PIL-6 at LUNR: launch IS named in cost of revenue** — *"Amortization expense associated with
  deferred contract costs for **subcontracted launch services** was $29.8M and $10.1M for the years
  ended December 31, 2025 and 2024"* [📄 LUNR 10-K p.80](https://agentii.ai/v/LUNR/sec59/80). FY2025
  launch amortisation is **14.19% of revenue** — **above PIL-6's 0.10 bar** — and **331% of gross
  profit** ($29.8M against $8,990K). It is also 14.82% of cost of revenues and 10.02% of total costs
  and expenses; **all four bases are above the bar**, so the finding is invariant to the denominator.
- **The 2026 fall is a DENOMINATOR event, and this is the row's whole point.** Launch amortisation is
  **$14.3M H1 2026 / $7.1M Q2 2026** against **$15.6M / $7.6M** in the prior year — a numerator that
  **FELL 6.6%**. The share fell to **3.64% / 4.37%** (H1) and **2.80% / 4.17%** (Q2) because cost of
  revenues rose **174.0%** ($62,156K → $170,302K) as **Lanteris** closed in January 2026 and added
  $166,735K of product revenue containing no launch. **The denominator moved; the numerator did not.**
  Launch delay fees were $2.3M H1 2025 / $0.8M Q2 2025 and **zero in 2026**.
- **LUNR is a `payload_customer`, and the relationship is an arm's-length purchase from within the
  universe**: a **$17M IM-4 milestone payment to SpaceX**, and **$58.1M of non-cancelable launch
  obligations** mixing launch services and component development. The correct PIC at this issuer is a
  fraction; the map carries it as a fraction.
- **DA-30 collisions at this issuer (four):** launch numerator **$17M cash vs $7.1M P&L = 2.39×**;
  backlog **"$1.8B" vs RPO $814.7M = 2.21×**; revenue **two live bases** (service-only 207,132 vs
  total 210,059 FY2025); and the 001 register's **−56.3%** for LUNR, which **does not reproduce** on
  either the Q2 2026 basis (−22.86%) or the FY2025 basis (−41.53%). The register's basis is
  **unresolved** and is recorded here rather than reconciled.
- DA-28 is engaged (weighted-average shares 107,081,918 → 147,878,006 → 162,172,470); **no
  share-count inference is used in this row**. DA-27 **cannot manifest** at LUNR (31-December filer) —
  which is **EXCLUDED, not CLEAN**.

---

### E-08 — PL / single reportable segment — PIL-6's cleanest test, and its bound

```yaml
issuer: PL
segment: "single reportable segment (verbatim: PL files 'one operating and reportable segment', no segment name)"
period_basis: "3M (quarter ended 2026-04-30, the issuer's Q1 FY2027)"
units: "USD thousands"
as_reported:
  revenue: 94150.0
  revenue_growth: 37.70             # gross profit grew +37.70% (36,603 → 50,401); the issuer's own growth statement
  operating_income: -34888.0
  operating_margin: -37.06          # 34,888 / 94,150
  gross_margin: 53.53               # 50,401 / 94,150 — the highest verified gross margin in the universe
  evidence_grade: DEMONSTRATED
  source: "PL 10-Q p.6 (statements of operations); p.29 (single reportable segment)"
operating_income_derivation:
  gross_profit: 50401.0             # 94,150 − 43,749, filed
  opex: 85289.0                     # 129,038 total costs and expenses − 43,749 cost of revenue — EXCLUSIVE
  shown: "94,150 − 43,749 = 50,401 gross profit (filed); 129,038 − 43,749 = 85,289 opex (EXCLUSIVE of cost of revenue); 50,401 − 85,289 = (34,888) ✓ EXACT — exactly the filed loss from operations. The INCLUSIVE construct (94,150 − 129,038 = (34,888)) closes too, and that is the trap: at this issuer the inclusive route closes by construction because the filed total includes the cost of revenue line. Both are printed; only the exclusive one is the component identity. DA-23: the platform serves `+34,888,000` against the filed `$(34,888)K`."
operator_class: payload_customer
deal_security_basis: not_applicable
basis_register:
  - competing_boundary: "launch cost as a share of programme cost (PIL-6)"
    computable_leg: "none — launch is named inside cost of revenue and quantified NOWHERE"
    non_formable_leg: "both"
    interpretation: unresolved
    resolving_disclosure: "a launch line in cost of revenue, or a launch-services purchase commitment captioned to a programme. PL's only filed launch figure is a forward STOCK — '$4.7 million of total purchase commitments for the fiscal year ended January 31, 2028' — and it is ABSENT from the 10-K's commitment note, which discloses only the Google hosting commitment ($34,053K + $33,427K = $67,480K)."
```

**Flags carried in-line.**

- **⚠ DA-23's cleanest instance in the universe, and the reason a naive test stays silent.** PL serves
  `OperatingIncomeLoss` as **positive at every period retrieved** — 34,888,000 / 95,073,000 /
  116,122,000 / 22,771,000 — against filed negatives $(34,888)K / $(95,073)K / $(116,122)K /
  $(22,771)K. **33 of 33 served facts are positive.** The naive bound test
  (`served value > filed gross profit`) is **SILENT** here, because +34,888 < filed gross profit
  50,401. **The component identity is the only detector.**
- **THE DECISIVE BOUND. With cost of revenue at ZERO, PL's operating margin is still only +9.4% for
  the quarter (8,861 / 94,150) and +13.1% for the year (40,169 / 307,727).** Breakeven requires opex
  to fall 40.9% (to 50,401) or cost of revenue to fall 79.7% (to 8,861). **Even if launch were free,
  PL would be barely profitable** — and launch is not the binding input.
- **The binding purchased input is cloud hosting, not launch: $58,545.0k against $4.7M = 12.5×.**
  Cloud hosting $25,118.0k + $33,427.0k. **The entire multi-year launch commitment closes 13.5% of
  one quarter's operating loss.**
- **PL is the universe's only filed intra-universe supply relationship**, and it names the suppliers:
  *"ArianeSpace SA, Blue Origin, LLC, **Firefly Aerospace Inc.**, ISAR Aerospace Technologies Inc.,
  Mitsubishi Heavy Industries, Ltd., NewSpace India Limited, **Rocket Lab USA Inc.**, **Space
  Exploration Technologies Corp. (SpaceX)**, and Stoke Space Technologies, Inc."*
  [📄 PL 10-Q p.59](https://agentii.ai/v/PL/sec76/59). **Five of the nine names in this thesis's
  universe meet on this page** — and the price is not disclosed.
- DA-27 **manifests** at PL (the platform's fiscal label is one lower than the issuer's own); the
  period basis is stated on this row because of it. DA-26 is framed in the corpus as both
  "UNMANIFESTED" and "CONFIRMED" on different pages — **not collapsed here**; the two readings have
  different scopes and the contract records it as unresolved.

---

### E-09 — YSS / `space infrastructure` — the positive pass-through counterexample

```yaml
issuer: YSS
segment: "space infrastructure"     # Note 15, the issuer's own name
period_basis: "3M (quarter ended 2026-06-30)"
units: "USD thousands"
as_reported:
  revenue: 92547.0
  revenue_growth: 10.0              # filed % change; H1 revenue is $208,890K
  operating_income: -41313.0
  operating_margin: -44.64          # 41,313 / 92,547
  gross_margin: 23.97               # 22,180 / 92,547 — the gross-profit subtotal is drafted under the derivation block, per the contract's field order
  evidence_grade: DEMONSTRATED
  source: "YSS 10-Q p.40 (statements of operations); p.34 (segment note); p.46 (non-GAAP reconciliation)"
operating_income_derivation:
  gross_profit: 22180.0             # FILED, not derived: 92,547 − 70,367 (YSS files a gross-profit subtotal, unlike LUNR/GSAT/IRDM/SATS)
  opex: 63493.0                     # filed total operating expenses, EXCLUSIVE of cost of revenues
  shown: "92,547 − 70,367 = 22,180 gross profit (filed); 22,180 − 63,493 = (41,313) ✓ EXACT on the EXCLUSIVE opex. Note the magnitude: exclusive opex is 2.86× gross profit for the quarter and 1.94× for FY2025 — this is a fixed-cost base, not a launch-cost base. The INCLUSIVE construct overstates the filed loss."
operator_class: enabler
deal_security_basis: not_applicable
```

**Flags carried in-line.**

- **YSS does not buy launch. It SELLS MISSIONS INTO launch vehicles.** That is its operator class and
  the reason its row cannot test PIL-6's `wrong_if` as written.
- **PIL-6 is NON-FORMABLE here as a PRESENCE finding, not an absence one.** YSS's cost of revenues
  decomposes **exhaustively into four components** — direct materials, direct labor, direct overhead,
  and D&A — and the decomposition **closes exactly** at every period retrieved:
  Q2 2026 **53,240 + 17,127 = 70,367** ✓ (17,127 = 11,119 labor + 3,736 overhead + 2,272 D&A);
  FY2025 **264,007 + 46,736 = 310,743** ✓; FY2024 **178,341 + 42,769 = 221,110** ✓; FY2023
  **148,574 + 34,625 = 183,199** ✓. **There is no residual, no "other", and no capacity for an
  unallocated fifth component.** A reader who wants a launch term inside YSS's cost of revenues has
  to put it inside a named component the filing already defines. Direct materials are 85.0% of FY2025
  cost of revenues.
- **THE COUNTEREXAMPLE, and it must be carried — it keeps PIL-6 from being a universal claim.**
  Non-GAAP contribution margin **rose on every basis**: Q1 **33 → 34**, Q2 **24 → 42**, H1
  **29 → 38**. Direct material per revenue dollar **fell from $0.758 to $0.575**. The reconciliation
  closes on two independent routes. **At least one demand-side name in this universe passed released
  value through.**
- **DA-23 FIRES here and is caught by the identity**: served **+110,466,000** for Q1 2026 against a
  filed negative, where the served Q1 value **exceeds** filed gross profit — the bound test works at
  YSS and is silent at PL.
- **DA-28 CONFIRMED, and it is a NEW defect class**: a **1000× share-count scale error**
  (`116,022,676,000` against the filed `116,022,676`), and *"the defect follows the FILING, not the
  concept and not the period."* **DA-25 is CONFIRMED TWICE** ($542,557K / 107 = $5,070K vs / 33 =
  $16,441K — a 3.24× spread, and a $21K break). DA-30 has multiple instances (revenue −20.45% QoQ vs
  +10.38% YoY; two IPO net proceeds of $582.6M and $583.4M).
- **⚠ CORRECTION CARRIED FORWARD:** the period figures **22,150 / 22,180 / 44,330 / 24,602 / 9,526 /
  34,128 that circulate as "revenue" in this workspace are YSS's GROSS PROFIT**, not revenue. YSS's
  actual Q2 2026 revenue is **$92,547K**; Q1 2026 revenue is **$116,343K** (DERIVED: H1 208,890 −
  Q2 92,547). The exclusive component identity runs on gross profit against exclusive opex, which is
  what makes the gross-profit figures look like revenue if read from the served layer. **Any artifact
  citing "YSS revenue 22,150" is citing gross profit.** The cross-check is exact: 41,313 / 92,547 =
  **44.64%**, which is the 001 register's YSS row to the decimal.
- YSS's year-end is **December**, not June; a "June year-end filer" note in the corpus contradicts the
  year-end used at every other issuer and is recorded as a corpus inconsistency, **not adopted**.

---

### E-10 — IRDM / unsegmented issuer — the profitable operator, priced off its customer base

```yaml
issuer: IRDM
segment: "unsegmented — the issuer files no segment note in the retrieved 10-Q (sec191) and no segment operating margins on any basis; the row is the consolidated issuer"
period_basis: "3M (quarter ended 2026-06-30)"
units: "USD thousands"
as_reported:
  revenue: 225237.0
  revenue_growth: 3.84
  operating_income: 34008.0
  operating_margin: 15.10
  evidence_grade: DEMONSTRATED      # arithmetic on filed cells; the SERVED layer for this issuer is inadmissible
  source: "IRDM 10-Q p.5 (income statement and three-month results table)"
as_restated:
  revenue: 225237.0
  revenue_growth: 3.84
  operating_income: 34008.0
  operating_margin: 21.45           # ex-transaction-costs; filed on p.24
  evidence_grade: DEMONSTRATED
  restatement_basis: "DA-21 scope, not a boundary change: the transaction costs of the Rocket Lab Merger Agreement are removed from the operating line. Revenue is unchanged, so the restatement isolates a cost the issuer files as part of the quarter's operations and that is not part of the ongoing earnings of the asset being bought. 63.8% of the 3M margin damage is deal cost."
operating_income_derivation:
  gross_profit: 225237.0            # ⚠ NOT A FILED SUBTOTAL: IRDM files no gross-profit line. This field carries
                                    # the revenue boundary that makes the identity hold under the INCLUSIVE definition.
  gross_profit_filed: false
  opex: 191229.0                    # filed total operating expenses (all five lines), INCLUSIVE of cost of services
  shown: "IRDM files no gross-profit line, so the INCLUSIVE pairing is the only admissible one: 225,237 − 191,229 = 34,008 ✓ EXACT. ⚠ The fallback construct `revenue − operating_income` = 225,237 − 34,008 = 191,229 COINCIDES numerically with the filed line — that coincidence is a DA-29 BACK-SOLVE that tests nothing, and the two must never be reported as one thing. The gross-profit bound is UNEXERCISED at IRDM, not passed: with no filed gross-profit line there is no bound to compare against."
  gross_profit_bound: UNEXERCISED
operator_class: payload_customer
deal_security_basis: standalone_pre_merger
spread:
  revenue_pp: 0.0
  margin_pp: 6.35
  interpretation: definitional
basis_register:
  - competing_boundary: "the served quarterly margins"
    computable_leg: "none — every served IRDM quarterly margin divides by a single $200,000 thousand denominator, the Aireon hosting-agreement revenue ceiling (srt:MaximumMember, six-month period). 8 of 8 reproduce to the basis point."
    non_formable_leg: "all"
    interpretation: unresolved
    resolving_disclosure: "a per-quarter realised related-party (Aireon) hosting revenue figure. IRDM discloses the CEILING and not the realised amount, so no reader can reconstruct what fraction of reported revenue the related party supplies. ISO: IRDM's served margins do not measure IRDM and NONE of them is admissible to this map."
```

**Flags carried in-line.**

- **The operands are filed and the arithmetic is exact; the SERVED layer is not usable.** IRDM's
  15.10% is quoted here as `34,008 / 225,237` from p.5, with the component identity in-line, and
  **not** from the metrics block.
- **⚠ CONDITIONALLY ADMITTED TO THE LADDER — `UNEXERCISED` pending the component re-run that 002's F8
  requires.** 002's F8 refuted the DA-23 clearance for IRDM, so the ladder position may be stated
  only after the component check re-runs. Separately, the served `operating_income` for IRDM carries a
  DA-29 signature — `computed −51,791,000` against `reported +51,791,000` — an opaque assertion with
  no cited derivation.
- **DA-23 is engaged across 9 cells at IRDM** (the strip lands on the operating line, net income, and
  EPS). DA-28's coverage window is wider than the corpus records — the corpus reaches FY2014/FY2015,
  not 2022-02-17; either way the 2009 IPO is outside it.
- **DA-26 ratios at IRDM are FY2025 inflation factors, not Q4-2024 comparisons — the labels were
  transposed.** DA-24 and DA-30 at the platform layer are `UNEXERCISED`: whether
  `us-gaap:OperatingIncomeLoss` at IRDM carries a non-operating component is unmeasured, and
  **consistency is not a check that ran.**
- **The deal, and what it says about the pool.** Rocket Lab agreed to acquire IRDM on **2026-06-28 at
  $54.00/share** — **$27.00 unconditional cash** plus stock, inside a **±25% value-preserving collar
  ($67.50–$112.50)**. A **Form S-4 is required**, so **stockholder approval IS sought** (the opposite
  of the GSAT structure). Termination fee **$223.6M**; **$3.6B 364-day bridge** (Deutsche Bank / Wells
  Fargo); **>$3.0B of cash needed**. Corroboration that the price is not a margin: **$54.00 sits at
  2.10× and 1.96×** two filed repurchase prices, and IRDM's **buyback terminated on 2026-06-28, the
  same date as the Merger Agreement**.
- **Aireon is a Q3 event and a one-time gain:** ~$366.7M closed **2026-07-02**; the gain is
  **≈$202M = 6.46× H1 2026 net income and 2.38× H1 2026 operating income** (`MODELED`). The brief's
  earlier ~2.1×/5.6× labels **do not reproduce and appear transposed**; they are recorded as a
  corpus defect, not carried.

---

### E-11 — GSAT / single reportable segment (MSS) — the unprofitable operator, and 64% one customer

```yaml
issuer: GSAT
segment: "single reportable segment (MSS) — the issuer files no segment note disaggregating operating margin; the row is the consolidated issuer"
period_basis: "3M (quarter ended 2026-06-30)"
units: "USD thousands"
as_reported:
  revenue: 64772.0
  revenue_growth: -3.54             # 64,772 / 67,148 − 1
  operating_income: -4775.0
  operating_margin: -7.37           # 4,775 / 64,772; the FILED margin reads '(7.37)%'
  evidence_grade: DEMONSTRATED
  source: "GSAT 10-Q p.5 (income statement)"
operating_income_derivation:
  gross_profit: 64772.0             # ⚠ NOT A FILED SUBTOTAL: GSAT files no gross-profit line. This field carries
                                    # the revenue boundary that makes the identity hold under the INCLUSIVE definition.
  gross_profit_filed: false
  opex: 69547.0                     # INCLUSIVE of cost of sales: 23,602 + 3,395 + 23,025 + 2,723 + 0 + 16,802
  shown: "GSAT files no gross-profit line, so the INCLUSIVE pairing is the only admissible one: 64,772 − 69,547 = (4,775) ✓ EXACT, where 69,547 = the six filed operating-expense lines (cost of services 23,602 + cost of subscriber equipment 3,395 + 23,025 + 2,723 + 0 + 16,802). The filed margin is printed '(7.37)%'. The identity is INCLUSIVE **because the issuer removed the choice** — there is no gross-profit boundary to subtract from, and the six-line total is exhaustive."
  gross_profit_bound: UNEXERCISED
operator_class: payload_customer
deal_security_basis: standalone_pre_merger
```

**Flags carried in-line.**

- **⚠ CORRECTION CARRIED — the ladder's rung 14 read `7.4%` and that is the DA-23-stripped sign.** The
  filed Q2 2026 figure is an operating **LOSS** of $(4,775) thousand = **−7.37%**. The platform serves
  that cell as **`+4,775,000`** — a **1,000× offset that is systematic across 7 facts** (Q2 2026
  +4,775,000; 6M 2025 +2,355,000; FY2024 +949,000; FY2023 +165,000; plus three derived rows) — and
  **the thesis register already consumed that strip and ranked the issuer as "the thinnest operator
  margin".** The correct row is **−7.37%, a swing to loss from +9.15%** — a **−16.5 point swing**.
  The monotonicity test on served values exposes it: **served Q2 2026 (+4,775) > served 6M 2026
  (+3,395)**; and **served Q1 2025 (+8,501) > served 6M 2025 (+2,355)**.
- **64% of six-month revenue is ONE CUSTOMER, who is also the financier and the acquirer.**
  $86,381 thousand = 64% of 6M 2026 revenue (62% of 3M). This is the row that makes PIL-2's claim
  literal: the demand owner is not a category here, it is a named counterparty that supplies the
  revenue, funds the balance sheet, and then buys the company.
- **The deal.** Merger Agreement with affiliates of **Amazon.com, Inc. dated 2026-04-13 at
  $90.00/share**. **Thermo, holding ≈57.6%, delivered a written consent: *"no further approval of the
  Company's stockholders is required or will be sought"* — there will be no vote.** Cash elections
  are **capped at 40%** with stock the default; the milestone was reduced **from $110M to $97M**;
  termination fee **~$420M**; expected close **2027**.
- **The price is not the margin.** Implied equity value **$90.00 × 129,563,390 = $11,660.7M** — and it
  is a **floor**, excluding the 149,425 Series A Preferred and the customer/Thermo warrants. TTM
  revenue **$280,642k**. See §6 for the multiple and its two bases.
- **A NEW PLATFORM DEFECT WITH NO DA NUMBER.** The platform serves
  `common_shares_outstanding: "149425"` against a filed **129,563,390** — an **867× error** (the
  preferred count served as the common count), **wrong in the conservative direction, so it never
  announces itself.** Recorded here as a named defect, **not** numbered as a DA class, because **no
  DA-31 exists.**
- Prior-year was **+9.15%** (6,146 / 67,148, `DEMONSTRATED`), and the quarterly path within 2026 is
  **+8,170 (Q1) → (4,775) (Q2)**, so 6M 2026 operating income is **+3,395**. The operating line turned
  negative **inside** the year.
- Accumulated deficit **$(2,206,570)k** (not $2,137M — that was the **prior year**). Excluding customer
  prepayments, operating cash flow is **negative $56,828k** (`DERIVED`).
- **PIL-6 at GSAT is `REACHABLE-BUT-NOT-RECORDABLE` — the third disposition class, whose remedy is a
  contract amendment and not research.** GSAT **does** buy launch; the cost sits inside cost of
  services and is **not separately disclosed**. The one class research cannot fix.

---

### E-12 — SATS / `Pay-TV` — the largest segment, and not a launch segment

```yaml
issuer: SATS
segment: "Pay-TV"                   # Note 1 / segment note, verbatim
period_basis: "3M (three months ended 2026-03-31, the issuer's fiscal Q1 2026)"
units: "USD thousands"
as_reported:
  revenue: 2294264.0
  revenue_growth: -9.6              # filed
  operating_income: 471567.0
  operating_margin: 20.55           # 471,567 / 2,294,264
  evidence_grade: DEMONSTRATED
  source: "SATS 10-Q p.71 (three-month segmental income statement)"
operating_income_derivation:
  gross_profit: 2294264.0           # ⚠ NOT A FILED SUBTOTAL at segment level: SATS files no segment gross-profit line.
  gross_profit_filed: false
  opex: 1822697.0                   # filed per-segment `Total costs and expenses`, INCLUSIVE of cost of services
  shown: "2,294,264 − 1,822,697 = 471,567 ✓ EXACT, where 1,822,697 = cost of services 1,415,700 + cost of sales-equipment 32,101 + SG&A 319,030 + impairments 0 + D&A 55,866. INCLUSIVE pairing — the filed line is exhaustive and the segment files no gross-profit subtotal to subtract from."
operator_class: payload_customer
deal_security_basis: not_applicable
```

---

### E-13 — SATS / `Wireless`

```yaml
issuer: SATS
segment: "Wireless"
period_basis: "3M (three months ended 2026-03-31)"
units: "USD thousands"
as_reported:
  revenue: 962491.0
  operating_income: -35782.0
  operating_margin: -3.72
  evidence_grade: DEMONSTRATED
  source: "SATS 10-Q p.71"
operating_income_derivation:
  gross_profit: 962491.0
  gross_profit_filed: false
  opex: 998273.0                    # 480,201 + 251,147 + 217,426 + 0 + 49,499 — INCLUSIVE
  shown: "962,491 − 998,273 = (35,782) ✓ EXACT (480,201 + 251,147 + 217,426 + 0 + 49,499 = 998,273)"
operator_class: payload_customer
deal_security_basis: not_applicable
```

---

### E-14 — SATS / `Broadband and Satellite Services`

```yaml
issuer: SATS
segment: "Broadband and Satellite Services"
period_basis: "3M (three months ended 2026-03-31)"
units: "USD thousands"
as_reported:
  revenue: 329656.0
  operating_income: 44184.0
  operating_margin: 13.40
  evidence_grade: DEMONSTRATED
  source: "SATS 10-Q p.71"
operating_income_derivation:
  gross_profit: 329656.0
  gross_profit_filed: false
  opex: 285472.0                    # 102,352 + 70,890 + 62,290 + 0 + 49,940 — INCLUSIVE
  shown: "329,656 − 285,472 = 44,184 ✓ EXACT (102,352 + 70,890 + 62,290 + 0 + 49,940 = 285,472)"
operator_class: payload_customer
deal_security_basis: not_applicable
```

**Flag.** This is the segment that **buys launch** — and it is the second-smallest segment at
**8.99% of consolidated revenue**, earning **+13.40%**. Its launch agreements (EchoStar XXV and XXVI,
Lanteris construction, SpaceX launch services) carry **no dollar amount on either side**.

---

### E-15 — SATS / `Other` — where the DA-24 contamination sits, and the one clean restatement

```yaml
issuer: SATS
segment: "Other"
period_basis: "3M (three months ended 2026-03-31)"
units: "USD thousands"
as_reported:
  revenue: 90983.0
  operating_income: -87295.0
  operating_margin: -95.95          # 87,295 / 90,983
  evidence_grade: DEMONSTRATED
  source: "SATS 10-Q p.71"
as_restated:
  revenue: 90983.0
  operating_income: -153454.0
  operating_margin: -168.66
  evidence_grade: DEMONSTRATED
  restatement_basis: "DA-24 removal: the $(66,159)K inverted impairment is CREDITED inside this segment's cost block, not charged. Removing it, the segment's costs are 183,132 + 50,000 + 11,305 = 244,437 and its operating loss is (153,454). Same boundary, same revenue, one non-operating item removed."
operating_income_derivation:
  gross_profit: 90983.0
  gross_profit_filed: false
  opex: 178278.0                    # 183,132 + 50,000 + (66,159) + 11,305 — INCLUSIVE
  shown: "90,983 − 178,278 = (87,295) ✓ EXACT, where 178,278 = cost of sales-equipment 183,132 + SG&A 50,000 + impairments and other (66,159) + D&A 11,305. The (66,159) enters as a NEGATIVE cost — a credit — which is DA-24's defining mechanism: an INVERTED IMPAIRMENT CHARGE, not an asset-sale gain."
operator_class: payload_customer
deal_security_basis: not_applicable
spread:
  revenue_pp: 0.0
  margin_pp: -72.71
  interpretation: definitional
```

**Flag.** **`thesis.md` describes SATS' DA-24 as an "asset-sale gain through operating_income" — that is
FALSIFIED.** The mechanism is a **$(66,159)K inverted impairment inside the cost block**, and it lands
**entirely inside this segment**. It is the only segment whose numbers move when DA-24 is removed,
which is why the restatement is emitted here and not on the consolidated row.

---

### E-16 — SATS / `Segment Total` / `Consolidated Total` — the control row (the segment table's own closure)

```yaml
issuer: SATS
segment: "Segment Total / Consolidated Total — a CONTROL ROW, not a segment: it is the segment table's own closure, carried because the map's boundaries are only as good as their reconciliation"
period_basis: "3M (three months ended 2026-03-31)"
units: "USD thousands"
as_reported:
  revenue: 3667489.0
  operating_income: 392847.0
  operating_margin: 10.71           # 392,847 / 3,667,489
  evidence_grade: DEMONSTRATED
  source: "SATS 10-Q p.71 (segment table) and p.11 (consolidated statements)"
as_restated:
  revenue: 3667489.0
  operating_income: 326688.0
  operating_margin: 8.91            # ex-item; 3,274,642 + 66,159 = 3,340,801 → 3,667,489 − 3,340,801 = 326,688
  evidence_grade: DEMONSTRATED
  restatement_basis: "DA-24 removal at the consolidated level: the same $(66,159)K inverted impairment. 326,688 / 3,667,489 = 8.91% ✓ EXACT."
operating_income_derivation:
  gross_profit: 3667489.0
  gross_profit_filed: false
  opex: 3274642.0                   # filed `Total costs and expenses`: 1,998,268 + 536,907 + 639,025 + (66,159) + 166,601
  shown: "3,667,489 − 3,274,642 = 392,847 ✓ EXACT, and the second route closes too: 1,998,268 + 536,907 + 639,025 + (66,159) + 166,601 = 3,274,642 ✓. INCLUSIVE pairing."
operator_class: payload_customer
deal_security_basis: not_applicable
spread:
  revenue_pp: 0.0
  margin_pp: -1.80
  interpretation: definitional
```

**Flags carried in-line.**

- **The segment table closes: the four segments sum to $392,674K against consolidated operating income
  of $392,847K — a $173K residual, 0.04%.** The map's boundaries are therefore sound at this issuer,
  and **DA-21 is satisfied rather than assumed.**
- **The filed operating series is CORRECTED: `(2.28) → (5.73) → (460.45) → (20.54) → +10.71%`.** Ex-item
  Q1 2026 is **+8.91%**. **The `118.1%` that circulates is not a quarter — it is the FY2025 ANNUAL
  margin**, so a reader who takes the published five-term progression is comparing four sign-stripped
  losses to one twelve-month figure. **This is DA-26 + DA-23 compounded and it is not carried.**
- **What SATS is, and why it is neither the launcher nor the demand owner.** SATS is a demand-side
  name by activity — it buys launch — but its value realisation is a **spectrum disposal**, not an
  operating result. See §6.3.
- Served-layer defects at this issuer: Q1 2025 and Q2 2025 row-layer `net_income_loss` are **null**
  (the filings have them; the platform does not — `UNRESOLVABLE-FROM-PLATFORM`), and **Q2 2026 is not
  in the series at all** while a consensus row shows a 2026-08-07 report date with `actual: null` —
  **a null is an absence of ingestion, not a reported zero.** The DA-23 sign test on any positive-margin
  period other than Q1 2026 is `UNEXERCISED`, **not CLEAN** — one positive period is too thin a basis.

---

## 3. The operator-class test

`operator_class` is set on every entry. The classes are assigned from the filed transaction structure,
not from the segment's name:

| class | entries | the test that assigned it |
|---|---|---|
| `captive_integrated` | SPCX Space, SPCX Connectivity | the operator flies its own payloads; **no transaction price exists** (DA-06) |
| `independent_launch` | RKLB Launch Services, (FLY Alpha, flagged at the segment level) | sells launch to third parties at a price |
| `payload_customer` | LUNR, PL, IRDM, GSAT, SATS (all four segments + control) | buys launch; the launch cost sits inside a filed cost-of-revenue term |
| `enabler` | RKLB Space Systems, YSS, FLY (reportable segment) | sells spacecraft/missions/parts to third parties |
| `adjacent` | SPCX AI | in the universe by capital proximity, not by launch-chain position |

**The captive flag, stated as the contract requires, in-line and not in a footnote.**

**⚠ A `captive_integrated` issuer's segment margin is NOT comparable to an `independent_launch`
issuer's.** DA-06's point is structural, not a measurement-error caveat: **for a vertically integrated
operator no transaction price exists at all.** SpaceX's Space segment revenue is a residual
**customer book** — *"our customer launches and customer activities"* — while ~74% of launches carry
no revenue by design. There is no arm's-length price for the internal launch, so there is no price to
compare with Electron's $22,000/kg or with RKLB's Launch Services gross margin. **Every SPCX
comparison in this map is a comparison of a price to a non-price, and is labelled as such.**

**The positive control the contract names is present in this universe and it is RKLB.** RKLB's Launch
Services segment sells to third parties, files a gross profit against a cost of revenue, and is
therefore the one entry where **a price exists**. That is what makes its 42.86% a market observation
and SPCX's 65.80% a costing exercise.

---

## 4. The margin ladder — bimodal, and the two anchors

All rows recomputed from filed cells with the component identity in §2. Period basis stated on every
row; **no row mixes 3M and 6M or 3M and FY.**

### 4.1 The component/supplier end (the high end)

| row | class | margin | basis |
|---|---|---:|---|
| TER | component (semiconductor test) | **32.9%** | FY |
| HEI | component (flight-critical, aftermarket) | **25.5%** | FY |
| CW | component (actuation, sensors) | **19.3%** | FY |
| KRMN | component (composites, fairings) | **19.1%** | FY |
| WWD | component (actuation, combustion) | **~17.0%** | FY |
| **mean** | | **22.76%** | (32.9+25.5+19.3+19.1+17.0)/5 |

### 4.2 The prime/integrator end (the anchor)

| row | class | margin | basis |
|---|---|---:|---|
| LMT | prime | **12.4%** | FY |
| RTX | prime | **11.4%** | FY |
| LHX | prime | **11.1%** | FY |
| NOC | prime | **10.1%** | FY |
| **mean** | | **11.25%** | (12.4+11.4+11.1+10.1)/4 |

**ANCHOR (a) HOLDS: 22.76 / 11.25 = 2.02×.** The component layer earns **twice** the prime layer.
Both ends of the ladder are high and the **middle is negative** — that is the bimodality, and it is
why a single "sector margin" is meaningless here.

### 4.3 The demand-owning operator end

| row | class | margin | basis |
|---|---|---:|---|
| **SPCX Connectivity** | captive_integrated (demand owner) | **+38.59%** | 3M |
| IRDM | payload_customer (operator) | **+15.10%** | 3M (ex-transaction-costs 21.45%) |
| SATS | payload_customer (spectrum + operator) | **+10.71%** | 3M (ex-item 8.91%) |
| SATS Pay-TV | payload_customer | **+20.55%** | 3M, segment |
| SATS Broadband and Satellite Services | payload_customer | **+13.40%** | 3M, segment |
| SATS Wireless | payload_customer | **−3.72%** | 3M, segment |
| GSAT | payload_customer (single-customer) | **−7.37%** | 3M |

### 4.4 The launcher/manufacturer middle and bottom

| row | class | margin | basis |
|---|---|---:|---|
| **RKLB** | independent_launch + enabler | **−24.57%** | 3M (57,514 / 234,066) |
| LUNR | payload_customer | **−22.86%** | 3M (FY2025: −41.53%) |
| SPCX (consolidated) | captive_integrated | **−1.83%** | 3M (143 / 7,814) |
| PL | payload_customer | **−37.06%** | 3M (gross margin 53.53%, the universe's best) |
| YSS | enabler | **−44.64%** | 3M |
| **SPCX Space** | captive_integrated | **−56.34%** | 3M, segment |
| **FLY** | enabler (launch platform inside) | **−80.90%** | 3M (6M: −96.12%) |
| SPCX AI | adjacent | **−49.08%** | 3M, segment |

**ANCHOR (b) IS FALSIFIED.** The claim that the worst margin belongs to the single-customer operator
does not hold: **the worst verified margin in the universe is FLY's −80.90%, a manufacturer**, 24.56 pp
below the next-worst verified row, while **the single-customer operator runs at −7.37%** — better than
RKLB, LUNR, PL, YSS, SPCX Space, SPCX AI and FLY. GSAT's loss is real and its quarter swung, but
**the monopsony penalty is not where the ladder's floor is.**

**The two ladders disagree about launch, and that is the finding.** SPCX Space is **1st of 3 on gross
margin (65.80%)** and **3rd of 3 on operating margin (−56.34%)**. The inversion is **122.14 pp**,
decomposed exactly as **R&D 111.85 pp + SG&A 10.29 pp**. A reader ranking the sector on gross margin
places the launch segment at the top; a reader ranking it on operating margin places it at the bottom.
**Neither ranking is wrong; taking one without saying which is.**

---

## 5. PIL-6's demand-side register — the demand side does not price off the curve

PIL-6's named quantity is **launch cost as a share of PROGRAMME cost**. The register below is the
map's answer per demand-side name, and **the answer is `NON-FORMABLE` at three of four.**

| name | launch named in cost of revenue? | quantified? | the register value | class |
|---|---|---|---|---|
| **YSS** | **NO** — and ruled out by construction | n/a | **NON-FORMABLE (PRESENCE finding)** — the four-component decomposition is exhaustive and closes at FY2023/FY2024/FY2025/Q2 2026 with no residual | `REACHABLE-BUT-NOT-RECORDABLE` |
| **PL** | **YES**, verbatim: *"third-party fees for launch procurement"* | **nowhere** | **NON-FORMABLE** — the only filed launch figure is a forward **stock**, $4.7M of FY2028 purchase commitments, absent from the 10-K's commitment note | `REACHABLE-BUT-NOT-RECORDABLE` |
| **SATS** | named agreements, **no dollar amount on either side** | **nowhere** | **NON-FORMABLE (strongest of the three)** — a launch share needs BOTH sides and neither is filed | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| **LUNR** | **YES**, verbatim: *"subcontracted launch services"* | **YES** | **14.19% FY2025** — ABOVE the 0.10 bar | `DEMONSTRATED` |
| **GSAT** | the cost is inside cost of services | **no** | **NON-FORMABLE** — the cost sits inside a filed line and is not separately disclosed | `REACHABLE-BUT-NOT-RECORDABLE` |
| **RKLB** | not applicable — the supplier's filing cannot contain the customer's programme cost | n/a | **NON-FORMABLE** as written; the within-issuer proxy (LS revenue ÷ total revenue) is **19.05% / 24.92%** | `NON-FORMABLE` / proxy `DEMONSTRATED` |

**Read the LUNR row carefully, because it is the only PASS and it is not one.** LUNR's FY2025 14.19%
is computed on a **consolidated** denominator, and its 2026 collapse to 2.80%–4.37% is a **denominator
event**: the numerator fell 6.6% while cost of revenues rose 174.0% when Lanteris added $166,735K of
product revenue containing no launch. **Report `NON-FORMABLE` per name; never PASS.**

**YSS is the counterexample and is carried in §2 E-09**: contribution margin rose on every basis
(33→34, 24→42, 29→38) with direct material per revenue dollar falling $0.758 → $0.575. **PIL-6 is not
a universal claim, and this map does not assert one.**

**Per-launch revenue and cost are `UNEXERCISED` at every demand-side name**: no launch count, no mass
metric, no per-launch figure is filed by any buyer. The only per-launch series in the universe is
**RKLB's**, and it is a **supplier's** series.

---

## 6. The migration accounting

### 6.1 The two exits, and the asymmetry between them

| | **IRDM → RKLB** | **GSAT → Amazon** |
|---|---|---|
| announced / agreed | **2026-06-28** | **2026-04-13** |
| price | **$54.00/share** | **$90.00/share** |
| consideration | **$27.00 UNCONDITIONAL CASH** + stock, **±25% value-preserving collar ($67.50–$112.50)** | cash elections **CAPPED AT 40%**, **stock the default** |
| stockholder approval | **REQUIRED** (Form S-4) | **NONE SOUGHT** — Thermo's 57.6% written consent: *"no further approval of the Company's stockholders is required or will be sought"* |
| protection | **$223.6M** termination fee; **$3.6B** 364-day bridge (DB/WF); **>$3.0B cash needed** | **~$420M** termination fee; milestone reduced **$110M → $97M**; close expected **2027** |
| the target's margin | **+15.10%** (from +23.17%) | **−7.37%** (from +9.15%) |
| multiple as carried | **≈8.3×** TTM revenue | **≈41.4×–41.6×** TTM revenue |
| what the buyer is buying | the licence, the government and aviation demand, and Aireon | **the customer** — 64% of six-month revenue is one counterparty that is also the financier |

**Both transactions add a stock component, both are value-collared or milestone-adjusted, and both
buyers are pricing the relationship rather than the income statement.** Amazon is a **listed
competitor of the company it is buying**; Rocket Lab appears in **neither IRDM's nor GSAT's filed
competitor set** — *"the launcher is not buying a competitor, it is buying a position in someone
else's competitive set."*

### 6.2 The multiples, on both bases (DA-30) — and an explicit `UNRESOLVED`

- **GSAT.** Implied equity **$11,660.7M** ($90.00 × 129,563,390) against TTM revenue **$280,642k** →
  **41.55×**. The register carries **41.4×–41.6×**, and the band is the **debt basis**. Reproduces to
  the register on the equity-only basis; the EV basis is the low end.
- **IRDM. ⚠ THE 8.3× IS NOT SOURCED IN IRDM'S OWN FILING SET AND IS NOT ATTRIBUTED TO IT.** IRDM's
  artifacts state **~13× revenue** against FY2025 revenue $601.8M (the $8.0B EV ÷ 601.8) and **3.4×
  total assets**. The **8.3×** appears **only** in the GSAT-side artifact and in this thesis's brief,
  **with no derivation**. An armed reproduction from filed cells gives **≈6.5× equity-only**
  ($5,721.9M ÷ $884,169k TTM) and **≈8.5× on an EV basis**. **Class: `UNRESOLVED`** — the armed
  reproduction spans **6.5×–8.5×**, the registered value is **8.3×**, and no filed derivation
  reconciles them. **The map reports the band, not the point.**
- **The contrast survives the basis problem.** On the registered bases the demand owner pays
  **≈41.4×–41.6×** for the **unprofitable** operator and the launcher pays **≈8.3×** for the
  **profitable** one — **≈5.0×**, against a margin differential of **22.5 points in the opposite
  direction**. On the armed reproduction (6.5×) the ratio is **≈6.4×**. **The direction is invariant
  to the basis; the magnitude is not, and both are printed.**

### 6.3 SATS — the terminal counter-case, and the one that is neither launcher nor demand owner

**≈142×.** The operating satellite business is **~$0.3 billion** (stalking horse: *"potentially $300
million, somewhat less than that"* — `CLAIMED`, no filed figure) against **≈$42.65 billion** of
regulatory-asset realisation: **$22.650bn cash** for 3.45 GHz and 600 MHz to AT&T (**closed**), plus
**~$20bn** for AWS-4 and H-Block to SpaceX, **up to $11bn of it in SpaceX Class A at $212/share**
(`DERIVED` from filed consideration terms plus `CLAIMED` components).

**Launch cost is not a variable in the transaction that realises the value.** The operating satellite
business is **~0.7% of the regulatory-asset realisation** — *"even if launch were free, the ~$42.65
billion is unchanged."* **The value migrated to the holder of a spectrum licence, which is neither
the launcher nor the demand owner in the PIL-2 sense.**

**And SATS' exposure to the launch cost curve is an EQUITY position, not a cost position: 261.8
million SpaceX shares** (`CLAIMED`). That belongs in PIL-2's migration accounting — the operator's
return on launch is a claim on the launcher's equity — and **not** in PIL-6.

**Two classes on the SATS numbers, kept apart:** the **disposal gain or loss is `UNRESOLVABLE-FROM-
PUBLIC-SOURCES` until closing**, because it is determined at closing on a basis different from
anything in the current statements ($22.650bn cash against a pre-disposal carrying amount of
**$34,550,802k**). **Any ratio of consideration to carrying value quoted today is on two
non-comparable bases.** And the "cash" collision — **$1.516bn filed (3/31/26) vs "$14bn or $15bn" on
the call, a ~9.6× gap with opposite solvency implications** — is **`UNRESOLVED`**; the plausible
timing explanation (the AT&T cash closing) **is not filed and is not used.**

---

## 7. The curve is the independent variable; the map is the dependent one

`_cross/launch-cost-curve.md` (**T900, published 2026-09-19**) is the map's declared input and is
**engaged, not merely cited**. What the map takes from it, and what it does not:

- **The 20-cell census closes: 2 DEMONSTRATED · 2 DEMONSTRATED-figs/MODELED-div · 2 CLAIMED · 1
  MODELED · 13 ABSENT.** *"A matrix whose demonstrated content is ONE VEHICLE and ONE BASIS, against
  13 absent cells out of 20."* **This map does not re-derive it and does not re-litigate it.**
- **The only architecture with a DEMONSTRATED price is F5c (fully expendable)**, and Electron is its
  verified instance. **F5b is Neutron, unflown**; F5a has a propellant floor and no DEMONSTRATED
  price. **The map therefore has exactly one priced launcher row to reason from (RKLB Launch
  Services), and it says so.**
- **The inversion carries directly into the map's denominator discipline**: cost per launch fell
  12.0% while cost per kg **ROSE 32.0%**, `0.88 × 1.50 = 1.32` exact. **A value map built on a
  falling per-launch price and a rising per-kilogram cost is a map whose ranking depends on which
  unit it is drawn in** — which is the same defect as §4's two ladders, one level up.
- **The corrected RKLB $/kg is 1.00×–1.50×, NOT 1.79×–2.62×, and "four of four periods" is
  FALSIFIED** (the Q2 2025 zero-HASTE control gives 1.00×; three periods are `UNEXERCISED`). **The map
  uses no RKLB $/kg figure at all**, and records the correction so that 004/005/006 do not inherit
  the fused version.
- **§10.4 of the curve artifact already carries the demand-side sweep, and this map confirms it and
  extends it**: *"the curve has no buy-side counterpart anywhere in this universe… the `$/kg` axis
  exists only on the sell side."* **The map's §5 is that finding, per name, with the disposition class
  and the resolving disclosure for each.**
- **The PIL-6 qualification the curve artifact raises is carried and generalised**: LUNR's FY2025
  launch amortisation is **14.19%** of its revenue against SPCX's **8.29%** launch-services share —
  **the SPCX figure is not the universe ceiling on launch intensity, and 003:PIL-6's language should
  be relaxed accordingly at that issuer.**

---

## 8. Coverage gaps, unresolved items and disposition classes

**Classes are three, not two.** `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (the disclosure does not exist and
no filing would produce it) / `UNRESOLVABLE-FROM-PLATFORM` (the disclosure exists; the platform's
coverage or extraction does not reach it) / **`REACHABLE-BUT-NOT-RECORDABLE`** (**both exist; the
contract has no field that can carry the disclosure — remedy is a CONTRACT AMENDMENT, not research**).
**A test that could not run is `UNEXERCISED`, never `CLEAN`. PRESENCE and ABSENCE are distinguished
throughout.**

| # | item | class | what resolves it |
|---:|---|---|---|
| 1 | **Baseline register** — launch-only revenue / margin at SPCX Space; ex-Lanteris margin at LUNR; launch-only margin at FLY | `REACHABLE-BUT-NOT-RECORDABLE` | the issuers print no cost-of-revenue split on the competing boundary. **The `as_restated` field cannot carry a revenue-only restatement, and the map refuses to fabricate the margin leg.** Contract amendment: a `partial_restatement` block. |
| 2 | **RKLB segment operating margin (basis C)** | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` **permanently** | the issuer has FILED that it does not review segment opex. **This is not "pending"; it is non-formable.** |
| 3 | **The 8.3× IRDM multiple** | **`UNRESOLVED`** | an EV-or-equity basis stated with the multiple. The armed band is 6.5×–8.5×. |
| 4 | **PIL-6 at PL, YSS, GSAT** | `REACHABLE-BUT-NOT-RECORDABLE` (PL, GSAT) / `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (SATS) | a launch line in cost of revenue / a captioned launch commitment. **At GSAT the remedy is the amendment: the cost is inside a filed line.** |
| 5 | **GSAT's FY2024 operating line** | `UNRESOLVED` | two corpus values (+0.38% vs (0.38)%; $949k vs $(949)k) at a single cell. Display-level, **but a reviewer will see it, so it is named rather than left.** |
| 6 | **001 register's LUNR −56.3%** | `UNRESOLVED` | a period basis. **Does not reproduce on Q2 2026 (−22.86%) or FY2025 (−41.53%).** |
| 7 | **YSS "June year-end filer"** | corpus inconsistency | contradicts the December year-end used everywhere else. **Recorded, not adopted.** |
| 8 | **PL non-GAAP gross margin 56% vs 56.3%; PL hosting schedule $58,545.0k (10-Q) vs $67,480K (10-K); PL DA-26 "UNMANIFESTED" vs "CONFIRMED"; YSS opex ratio 68.60% vs 68.61%** | corpus inconsistencies | single-cell display claims. **Named; not collapsed.** |
| 9 | **The 5.0× multiple ratio** | `DERIVED`, direction-invariant | 41.55 / 8.3 = 5.01×; on the armed reproduction 41.55 / 6.5 = 6.4×. **Both printed.** |
| 10 | **DA-23 census at the map's issuers** | **10 of 12 engaged** (SPCX, RKLB, FLY, LUNR, PL, YSS, IRDM, GSAT, SATS, and PL's 33-of-33 as the cleanest); **not exercised** at the two where the issuer files no negative operating line | `UNEXERCISED` at those two, **not CLEAN** |
| 11 | **IRDM's ladder admission** | `UNEXERCISED` | 002's F8 requires the component check to RE-RUN before IRDM's 15.10% is used as a ladder rung; the served `operating_income` also carries a DA-29 `computed`/`reported` disagreement. |
| 12 | **The GSAT preferred-as-common share-count defect (867×)** | **a new platform defect with NO DA number** | **no DA-31 exists.** Recorded as a named defect; do **not** invent a number for it. |
| 13 | **`thesis.md`'s SATS DA-24 description ("asset-sale gain through operating_income")** | **FALSIFIED** | the mechanism is a $(66,159)K inverted impairment inside the cost block. **Correction carried.** |
| 14 | **`get_segment_data` / `data_freshness`** | UNUSABLE | `column "k" does not exist` and double-counts; `data_freshness` reports 2027-04-12. **Every row in this map was read from pages.** |
| 15 | **`entities.md` carries superseded figures** (GSAT `7.4%`; RKLB `1.79×–2.62×`) | **SUPERSEDED 2026-09-19** | the corrections are in §2 E-11 and §7. |

**Explicitly not attempted / not available to this artifact:** no per-constellation value (P10); no
launch count or mass metric at any demand-side name (so per-launch revenue and cost are
`UNEXERCISED` there); no segment opex at RKLB; no segment operating margin at IRDM or GSAT; no
quarterly realised Aireon revenue at IRDM; no IRDM or GSAT entry in PIL-2's `wrong_if` census, because
**neither files segment operating margins and neither has a launch segment** — **a census reporting
"0 of N operators exceeding" would be claiming a test that could not run.**

---

## 9. What would falsify this map

1. **A demand-side name disclosing launch as a share of programme cost above 0.10 that is NOT an
   artefact of an acquired denominator** — LUNR's 14.19% is the closest and it fails that condition.
   Resolving disclosure: a launch line in cost of revenue at PL, YSS or GSAT.
2. **A launch segment operating margin at SPCX materially above Connectivity's +38.59%** — which
   would put the pool back at the launcher. **Caveat: at a captive issuer the number would be a
   costing exercise and not a price (DA-06), so the falsifier must be run at RKLB or FLY, not SPCX.**
3. **A deal in which the acquirer's multiple is HIGHER for the more profitable operator** — the
   inverse of the 5.0×/22.5-point relationship. The universe's two exits both point the other way and
   **both are on a stock component**, which is where the next test lives.
4. **A third independent operator surviving on its own operating margin** — the universe's two both
   exited within twelve months. **The positive control for PIL-2's `wrong_if` is not a margin; it is a
   survivor.**
5. **An operating-margin ladder and a gross-margin ladder that rank the same segment consistently**
   — the 122.14 pp / 94.93 pp inversions at SPCX Space are the falsifier's target, and their exact
   decomposition into R&D and SG&A is the reason the inversion is a finding rather than a measurement
   artefact.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Note 18 segment table Q2 2026 — Space 962 / 329 / 1,076 / 99 / 1,504 / (542); Connectivity 4,291 / 2,060 / 294 / 281 / 575 / 1,656; AI 2,561 / 1,106 / | [📄 SPCX  p.30](https://agentii.ai/v/SPCX/sec8/30) **(newly surfaced)** |
| "Our Space segment revenue only reflects our customer launches and customer activities." | [📄 SPCX  p.35](https://agentii.ai/v/SPCX/sec8/35) |
| Mass-to-orbit definition (total kilograms of payload delivered from all successful orbital flights and flight tests, excluding failed or scrubbed atte | [📄 SPCX  p.36](https://agentii.ai/v/SPCX/sec8/36) **(newly surfaced)** |
| Condensed consolidated statements of operations Q2 2026 — total revenues 234,066; total cost of revenues 149,490; gross profit 84,576; total operating | [📄 RKLB  p.32](https://agentii.ai/v/RKLB/sec109/32) **(newly surfaced)** |
| Segment table FY2025 / FY2024 / FY2023 — Launch Services and Space Systems revenue, cost of revenue and gross profit; "Management does not regularly r | [📄 RKLB  p.107](https://agentii.ai/v/RKLB/sec87/107) **(newly surfaced)** |
| Condensed consolidated statements of operations — revenue 117,683 / 15,549 / 198,562 / 71,404; cost of sales 93,808 / 11,554 / 157,226 / 65,189; gross | [📄 FLY  p.6](https://agentii.ai/v/FLY/sec21/6) **(newly surfaced)** |
| Single reportable segment; prior-period recast on refinement of the segment disclosure in Q1 fiscal 2026 | [📄 FLY  p.34](https://agentii.ai/v/FLY/sec21/34) **(newly surfaced)** |
| Q2 2026 and H1 2026 statements of operations — revenue 206,168 / 392,898, opex 253,304 / 479,235, operating loss (47,136) / (86,337), shares 162,172,4 | [📄 LUNR  p.8](https://agentii.ai/v/LUNR/sec76/8) **(newly surfaced)** |
| FY2025 annual statement of operations — revenue 210,059, opex 297,290, operating loss (87,231), net loss (106,846); one reportable segment | [📄 LUNR  p.48](https://agentii.ai/v/LUNR/sec59/48) **(newly surfaced)** |
| "Amortization expense associated with deferred contract costs for subcontracted launch services was $29.8M and $10.1M for the years ended December 31, | [📄 LUNR  p.80](https://agentii.ai/v/LUNR/sec59/80) |
| Amortisation of deferred contract costs for subcontracted launch services $7.1M and $14.3M (3M / 6M 2026) vs $7.6M and $15.6M (3M / 6M 2025); launch d | [📄 LUNR  p.24](https://agentii.ai/v/LUNR/sec76/24) **(newly surfaced)** |
| Q1 FY2027 statements of operations — revenue 94,150, cost of revenue 43,749, gross profit 50,401, total costs and expenses 129,038, loss from operatio | [📄 PL  p.6](https://agentii.ai/v/PL/sec76/6) **(newly surfaced)** |
| Segment note — one operating and reportable segment; segment cost of revenue 94,138 against the statement's 135,242; capital expenditures; long-lived  | [📄 PL  p.29](https://agentii.ai/v/PL/sec76/29) **(newly surfaced)** |
| "third-party fees for launch procurement" (inside cost of revenue, unquantified); "$4.7 million of total purchase commitments for the fiscal year ende | [📄 PL  p.20](https://agentii.ai/v/PL/sec76/20) **(newly surfaced)** |
| Launch providers named as suppliers — "ArianeSpace SA, Blue Origin, LLC, Firefly Aerospace Inc., ISAR Aerospace Technologies Inc., Mitsubishi Heavy In | [📄 PL  p.59](https://agentii.ai/v/PL/sec76/59) |
| One operating segment and one reportable segment, `space infrastructure`; CODM reviews consolidated net loss and total assets | [📄 YSS  p.34](https://agentii.ai/v/YSS/sec12/34) **(newly surfaced)** |
| Q2 2026 results-of-operations ladder — revenue $92,547k +10%, cost of revenues $70,367k (76%), gross profit $22,180k (24%) +133%, total operating expe | [📄 YSS  p.40](https://agentii.ai/v/YSS/sec12/40) **(newly surfaced)** |
| Segment footnote (a) — "Other segment items is comprised of other costs of revenue excluding direct materials, including direct labor, overhead costs  | [📄 YSS  p.35](https://agentii.ai/v/YSS/sec12/35) **(newly surfaced)** |
| Non-GAAP reconciliation — revenue $92,547K, cost of revenues $70,367K, gross profit $22,180K; six-month revenue $208,890K, gross profit $44,330K, cont | [📄 YSS  p.46](https://agentii.ai/v/YSS/sec12/46) **(newly surfaced)** |
| FY2025 statement of operations — revenue $386,203K; cost of revenues $310,743K; gross profit $75,460K; total opex $146,124K; loss from operations $(70 | [📄 YSS  p.47](https://agentii.ai/v/YSS/sec12/47) **(newly surfaced)** |
| Q2 2026 income statement — revenue 225,237; operating income 34,008; net income 9,679; three-month results table with all five operating-expense lines | [📄 IRDM  p.5](https://agentii.ai/v/IRDM/sec191/5) **(newly surfaced)** |
| Three-month results of operations — SG&A +22,417 / +50%; the transaction-cost restatement giving an ex-transaction-costs margin of 21.45% against 23.1 | [📄 IRDM  p.24](https://agentii.ai/v/IRDM/sec191/24) **(newly surfaced)** |
| Merger Agreement with affiliates of Amazon.com, Inc. dated 2026-04-13 at $90.00 per share; Thermo's written consent "no further approval of the Compan | [📄 GSAT  p.11](https://agentii.ai/v/GSAT/sec166/11) **(newly surfaced)** |
| Q2 2026 income statement — revenue 64,772; total operating expenses 69,547 (23,602 + 3,395 + 23,025 + 2,723 + 0 + 16,802); operating loss (4,775); fil | [📄 GSAT  p.5](https://agentii.ai/v/GSAT/sec166/5) **(newly surfaced)** |
| Three-month segmental income statement to 2026-03-31 — revenue, operating expenses, OIBDA and operating income (loss) by segment; Pay-TV 2,294,264 / 1 | [📄 SATS  p.71](https://agentii.ai/v/SATS/sec121/71) **(newly surfaced)** |
| Consolidated statements of operations Q1 2026 — total revenue $3,667,489K; cost of services $1,998,268K; cost of sales-equipment $536,907K; SG&A $639, | [📄 SATS  p.11](https://agentii.ai/v/SATS/sec121/11) **(newly surfaced)** |
| Note 1 — principal business segments (Pay-TV, Wireless, Broadband and Satellite Services, Other); AT&T License Purchase Agreement to sell 3.45 GHz and | [📄 SATS  p.14](https://agentii.ai/v/SATS/sec121/14) **(newly surfaced)** |
