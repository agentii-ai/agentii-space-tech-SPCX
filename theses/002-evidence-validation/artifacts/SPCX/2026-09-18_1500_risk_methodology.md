---
# 002 / Phase 5 / T099–T101 — pillar PIL-7 (falsifier reachability), ticker SPCX.
# ONE artifact, two jobs: (1) DA-24 contamination scoping at SPCX; (2) classification of
# 001's six falsifiers against the disposition classes with a NAMED resolving source each.
thesis_id: "002-evidence-validation"
pillar: PIL-7
ticker: SPCX
skill: risk
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
# Written at 1.5.0, not grandfathered: the register gained DA-29 (defective checks — the
# circularity test) and DA-30 (a basis collapsed before an artifact sees it) at 002 Phase 3,
# and both are load-bearing here. §3, §5 and §6 discharge those two obligations in full.
constitution_pin: "1.5.0"
assumption_pin: "2"
# risk = 953fc5d396e7, one of the six pins tabled in theses/001-technology-baseline/reproduce.md
# and re-derived at scripts/dispatch.py:132 (sha256 over sorted(skill_dir.rglob("*")); name
# bytes then file bytes; first 12 hex). packaging/targets/{claude-code,codex,generic-cli,cowork}
# hold DECOY copies of every skill and all four fail the six known hashes — they are not the
# pin source. The pin is written, not UNRESOLVED.
skill_pin: "953fc5d396e7"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: DA-23
    chosen_reading: >
      Sign stripping — a served magnitude with the filed sign discarded. At SPCX the strip is
      not sporadic and it is perfectly partitioned by filed sign: 7 of 7 filed-negative
      instances across three concepts are served positive (OperatingIncomeLoss 4 of 4,
      OtherNonoperatingIncomeExpense 2 of 2, RestructuringCharges 1 of 1) and 7 of 7
      filed-positive instances are served correctly, plus 12 of 12 in the NetIncomeLoss
      family. A clearance is only EXERCISED if the concept is bidirectional; the unidirectional
      arcs (revenue +1, costs −1) make a sign test VACUOUS and are recorded as such.
  - da_id: DA-24
    chosen_reading: >
      NON-OPERATING CONTAMINATION of the operating line, in EITHER direction — the definition
      names a gain AND a charge, and the mechanism is COMPOSITION, not sign. At SPCX the
      contaminant is present and is proven from the filer's own calculation linkbase:
      us-gaap:RestructuringCharges and us-gaap:ImpairmentOfLongLivedAssetsHeldForUse are arc
      children of us-gaap:CostsAndExpenses at weight +1, and CostsAndExpenses is the −1 child
      of us-gaap:OperatingIncomeLoss. It runs both ways in the served periods: charges of
      190 (Q2 2025), 194 (H1 2025), 5 and 29 (impairment), 2 (Q2 2026), and a (9) CREDIT in
      H1 2026. Not refuted; refuted only in SEVERITY (§1.3).
  - da_id: DA-26
    chosen_reading: >
      An annual-basis fact served where a quarterly label is asserted, and the general case of
      a duration collision. SPCX supplies a duration-collision defect at the INSTRUMENT rather
      than the issuer level: get_segment_data reports total_revenue 32,531,000,000, which is
      exactly the sum of all four served revenue facts (7,814 + 12,508 + 4,071 + 8,138) with
      no period or duration de-duplication, and a segment row that serves the PRIOR-YEAR value
      under the current-year key (§6.2). Every figure quoted here names its period and its
      duration.
  - da_id: DA-27
    chosen_reading: >
      Calendar-derived fiscal labels and the MECHANISM-POPULATION identity: the sample is
      defined by the mechanism's own property and carries no information about the remainder.
      SPCX is a December-31 year-end filer (deferred revenue is measured at 12/31/25), so
      extending the DA-27 or PIL-3 samples with more December issuers buys nothing.
  - da_id: DA-28
    chosen_reading: >
      Listing/entity-boundary discontinuity. At SPCX the test is not whether a listing event
      exists — the IPO closed in June 2026 inside the served period (638.9 million shares at
      $135.00, net proceeds $85,675 million) and the reporting entity changed four times in the
      comparison window. The test is whether the boundary is DISCLOSED, and the recast basis
      for the common-control mergers is incorporated by reference into the Prospectus, which
      the served corpus does not carry (§2.5).
  - da_id: DA-29
    chosen_reading: >
      Back-solved or opaque checks: a reconciliation whose terms cannot all be located in the
      source, and instruments whose reported/computed columns are not the filed values. SPCX
      passes the TERM test on the Adjusted EBITDA bridge (all nine terms are filed cells on
      p.46) and fails the instrument test: validate_calculation returns 18 fails, and its own
      `diff` column is sign-contaminated because `reported` shares the stripped store, so the
      `diff` magnitudes (578 and 200) are not the identity gaps (458 and 1,940) — §5.
  - da_id: DA-30
    chosen_reading: >
      Two competing bases under one concept, collapsed without a basis field. At SPCX this
      binds on four figures and is quantified in §3: $/kg to LEO spans 12.8x (939 to 11,977)
      across three defensible denominator/numerator pairings in ONE filing; nameplate compute
      draw is GPU nameplate excluding cooling and facility overhead (1.4 GW) against a facility
      draw of 2.1–2.8 GW; Starlink subscribers exclude managed enterprise and government
      customers (12.0 million); and the instrument serves a segment row on the prior-year
      basis under the current-year key.
evidence_grade: DEMONSTRATED
# P11. SPCX is not in the checker's DEAL_SECURITIES set {IRDM, GSAT, RKLB}, and SPCX is the
# ACQUIRER in the EchoStar transaction — but P11's logic still binds, because a partial CLOSE
# occurred inside the served period. Basis: the Spectrum Transfer Closing occurred 2026-05-22
# after FCC approval on 2026-05-12, and $856 million of Spectrum Credit Agreement payments had
# been made as of 2026-06-30 (sec8 p.49), recognised as payments for intangible assets
# (sec8 p.9). So the served H1 2026 figures are POST-CLOSE for the transferred licences, while
# the Spectrum Acquisition Closing (expected 2026-11-30) and the equity consideration leg
# (approximately 261.8 million shares at a fixed value of $42.40) remain PENDING — which is why
# the $24.2 billion divergence between that fixed value and the $135.00 IPO price is flagged as
# unreconciled rather than resolved (§1.5, §8).
deal_security_basis: post_close
unresolvable: false
citations:
  - figure: "Consolidated statements of operations, cells: Revenue 7,814 / 4,071 / 12,508 / 8,138; Cost of revenue 3,495 / 2,282 / 5,883 / 4,244; R&D 3,548 / 1,958 / 7,062 / 3,515; SG&A 912 / 606 / 1,658 / 1,099; Restructuring charges (credits) 2 / 190 / (9) / 194; Impairment - / 5 / - / 29; Total costs and expenses 7,957 / 5,041 / 14,594 / 9,081; Loss from operations (143) / (970) / (2,086) / (943); Interest expense (629) / (411) / (1,293) / (858); Interest income 340 / 98 / 553 / 215; Other income (expense), net (86) / 413 / (1,962) / 202; Loss before income taxes (518) / (870) / (4,788) / (1,384); Provision for income taxes 23 / 138 / 29 / 152; Net loss (541) / (1,008) / (4,817) / (1,536); Net loss attributable to shareholders (541) / (1,008) / (5,488) / (1,536); EPS basic and diluted (0.09) / (0.34) / (1.12) / (0.53); weighted average shares 5,864 / 2,929 / 4,879 / 2,902"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 5
    url: "https://agentii.ai/v/SPCX/sec8/5"
    located_via: read_source_pages
  - figure: "Consolidated statements of cash flows, cells: D&A 5,290 / 2,970; unrealized (gain) loss on digital assets 539 / (252); loss on debt extinguishment 1,545 / -; PP&E purchases (28,476) / (6,965); payments for intangible assets (856) / -; IPO proceeds 85,675 / -; operating 3,466 / 351; investing (34,487) / (6,032); net change in cash 69,228 / 3,593; beginning 25,124 / 11,501; ending 94,352 / 15,094"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 9
    url: "https://agentii.ai/v/SPCX/sec8/9"
    located_via: read_source_pages
  - figure: "Note 1, cells/text: three reportable segments (Space, Connectivity, AI); IPO 638.9 million Class A shares at $135.00, net proceeds $85,675 million, offering costs $575 million; five-for-one forward stock split in May 2026; xAI Merger completed 2026-02-02; X Merger 2025-03-28"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 11
    url: "https://agentii.ai/v/SPCX/sec8/11"
    located_via: read_source_pages
  - figure: "Note 3 revenue disaggregation, cells: Products 461 / 403 / 841 / 755; Services 7,353 / 3,668 / 11,667 / 7,383; total 7,814 / 4,071 / 12,508 / 8,138; Launch Services 648 / 490 / 978 / 1,056; Launch and Development 314 / 256 / 603 / 555; Space 962 / 746 / 1,581 / 1,611; Consumer 2,485 / 1,721 / 4,633 / 3,213; Enterprise and Government 1,806 / 867 / 2,915 / 1,849; Connectivity 4,291 / 2,588 / 7,548 / 5,062; Advertising 367 / 426 / 710 / 870; AI Solutions and Infrastructure 2,194 / 311 / 2,669 / 595; AI 2,561 / 737 / 3,379 / 1,465; deferred revenue 12,116 at 12/31/2025 and 14,286 at 6/30/2026"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 13
    url: "https://agentii.ai/v/SPCX/sec8/13"
    located_via: read_source_pages
  - figure: "Legal proceedings, cells/text: DSA fine of EUR 120 million on XIUC, X., x.AI and Elon Musk; Vidstream jury award $105 million plus $67 million prejudgment interest; NMPA matter dismissed by stipulation on 2026-07-16 and 'the matter is now closed'; 'The Company has recorded an accrual of $354 million for litigation losses that are probable and reasonably estimable in Accrued expenses and other current liabilities and Other liabilities ... For other matters, the Company is not currently able to estimate the reasonably possible loss or range of loss.'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 29
    url: "https://agentii.ai/v/SPCX/sec8/29"
    located_via: read_source_pages
  - figure: "Segment table, Q2 2026, cells: Revenue Space 962 / Connectivity 4,291 / AI 2,561 / Total 7,814; Cost of revenue 329 / 2,060 / 1,106 / 3,495; R&D 1,076 / 294 / 2,178 / 3,548; SG&A 99 / 281 / 532 / 912; Restructuring - / - / 2 / 2; Total costs 1,504 / 2,635 / 3,818 / 7,957; Income (loss) from operations (542) / 1,656 / (1,257) / (143); D&A 158 / 805 / 1,885 / 2,848; SBC 179 / 136 / 516 / 831; capex 1,174 / 1,367 / 15,828 / 18,369"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 30
    url: "https://agentii.ai/v/SPCX/sec8/30"
    located_via: read_source_pages
  - figure: "Segment table H1 2026 and Q2 2025, cells: H1 2026 Revenue 1,581 / 7,548 / 3,379 / 12,508 and Income (loss) from operations (1,204) / 2,844 / (3,726) / (2,086); Q2 2025 Revenue 746 / 2,588 / 737 / 4,071; Restructuring - / - / 190 / 190; Impairment 5 / - / - / 5; Total costs 1,115 / 1,665 / 2,261 / 5,041; Income (loss) from operations (369) / 923 / (1,524) / (970)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 31
    url: "https://agentii.ai/v/SPCX/sec8/31"
    located_via: read_source_pages
  - figure: "Segment table H1 2025, cells: Revenue 1,611 / 5,062 / 1,465 / 8,138; Restructuring - / - / 194 / 194; Impairment 29 / - / - / 29; Total costs 2,050 / 3,106 / 3,925 / 9,081; Income (loss) from operations (439) / 1,956 / (2,460) / (943). Note 19: 'In 2022, X, an indirect subsidiary of the Company (through the X Merger and subsequently, xAI Merger), initiated global employee workforce reductions, the effects of which continued into 2026'; total charges (credits) of '$2 million and $(9) million' for the three and six months ended June 30, 2026 and '$190 million and $194 million' for 2025; restructuring liabilities 443 / (9) / (168) / 2 = 268"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 32
    url: "https://agentii.ai/v/SPCX/sec8/32"
    located_via: read_source_pages
  - figure: "Merger notes, cells/text: Cursor Merger Agreement signed June 2026, closing expected Q3 2026, consideration of Class A shares based on an implied equity value of $60 billion; Mesh Optical Merger consideration approximately 3.8 million Class A shares plus up to $2.5 million cash per Class B holder, and 'The Mesh Optical Merger closed on July 6, 2026'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 33
    url: "https://agentii.ai/v/SPCX/sec8/33"
    located_via: read_source_pages
  - figure: "MD&A overview, cells/text: 'our final prospectus filed with the SEC pursuant to Rule 424(b)(4) under the Securities Act of 1933 ... on June 12, 2026 in connection with our initial public offering'; three reportable segments; IPO 638.9 million shares at $135.00 with net proceeds of $85,675 million after offering costs of $575 million; Cursor implied equity value $60 billion"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 34
    url: "https://agentii.ai/v/SPCX/sec8/34"
    located_via: read_source_pages
  - figure: "Key business metrics, Space, cells: Mass to orbit (metric tons) 485 / 652 / 1,041 / 1,102; of which customer payloads 87 / 88 / 132 / 163; of which internal payloads 397 / 563 / 908 / 938; Falcon launches 37 / 45 / 77 / 81; customer launches 10 / 9 / 17 / 21; internal launches 27 / 36 / 60 / 60; Starship launches 1 / 1 / 1 / 3"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 35
    url: "https://agentii.ai/v/SPCX/sec8/35"
    located_via: read_source_pages
  - figure: "Key business metrics, Connectivity and AI, cells: Starlink subscribers (millions) 12.0 / 6.0; Starlink ARPU (dollars per month) $66 / $85; Nameplate compute draw (gigawatts) 1.4 / 0.4, defined as 'the number of GPUs installed in our data centers at the end of the period multiplied by their respective all-in power draw ... does not represent actual power consumption or utilization. It does not include power we install and use for our supporting infrastructure such as cooling systems, power distribution losses, lighting, security systems, or facility-level overhead.'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 36
    url: "https://agentii.ai/v/SPCX/sec8/36"
    located_via: read_source_pages
  - figure: "AI segment accounting policy, text: 'Other income (expense), net consists of gain or loss on digital assets, gain or loss on foreign currency transactions, and loss on extinguishment of debt.'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 39
    url: "https://agentii.ai/v/SPCX/sec8/39"
    located_via: read_source_pages
  - figure: "MD&A consolidated results, cells: revenue $ change 3,743 / 91.9% (Q2) and 4,370 / 53.7% (H1); loss from operations change 827 / (85.3)% and (1,143) / 121.2%"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 40
    url: "https://agentii.ai/v/SPCX/sec8/40"
    located_via: read_source_pages
  - figure: "MD&A drivers, text: R&D increased $1,590 million (81.2%) and $3,547 million (100.9%); SG&A increased $306 million (50.5%) and $559 million (50.9%); other income (expense), net decreased $499 million and $2,164 million 'primarily due to the loss on extinguishment of debt and unrealized loss on digital assets'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 41
    url: "https://agentii.ai/v/SPCX/sec8/41"
    located_via: read_source_pages
  - figure: "AI segment table, cells: Revenue 2,561 / 737 / 1,824 / 247.5% and 3,379 / 1,465 / 1,914 / 130.6%; Cost of revenue 1,106 / 551 / 555 / 100.7% and 1,562 / 1,002 / 560 / 55.9%; R&D 2,178 / 1,122 / 1,056 / 94.1% and 4,557 / 2,030 / 2,527 / 124.5%; SG&A 532 / 398 / 134 / 33.7% and 995 / 699 / 296 / 42.3%; Restructuring 2 / 190 / (188) / (98.9)% and (9) / 194 / (203) / NM; Total costs 3,818 / 2,261 / 1,557 / 68.9% and 7,105 / 3,925 / 3,180 / 81.0%; Loss from operations (1,257) / (1,524) / 267 / (17.5)% and (3,726) / (2,460) / (1,266) / 51.5%"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 44
    url: "https://agentii.ai/v/SPCX/sec8/44"
    located_via: read_source_pages
  - figure: "AI segment drivers, text: SG&A 'increased by $134 million, or 33.7% ... primarily due to higher employee compensation expenses ... of $177 million ... partially offset by a decrease in legal expenses of $64 million due to a dismissal of litigation against the Company'; AI loss from operations 'decreased by $267 million, or 17.5%' for the quarter and 'increased by $1,266 million, or 51.5%' for the six months"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 45
    url: "https://agentii.ai/v/SPCX/sec8/45"
    located_via: read_source_pages
  - figure: "Adjusted EBITDA reconciliation, cells: Net loss (541) / (1,008) / (4,817) / (1,536); D&A 2,848 / 1,526 / 5,290 / 2,970; SBC 831 / 463 / 1,470 / 694; Restructuring 2 / 190 / (9) / 194; Impairments - / 5 / - / 29; Interest expense 629 / 411 / 1,293 / 858; Interest income (340) / (98) / (553) / (215); Other income (expense), net 86 / (413) / 1,962 / (202); Provision for income taxes 23 / 138 / 29 / 152; Adjusted EBITDA 3,538 / 1,214 / 4,665 / 2,944; Segment Adjusted EBITDA Q2 2026 (205) / 2,597 / 1,146 / 3,538"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 46
    url: "https://agentii.ai/v/SPCX/sec8/46"
    located_via: read_source_pages
  - figure: "Segment Adjusted EBITDA and liquidity, cells: H1 2026 (556) / 4,684 / 537 / 4,665; Q2 2025 (93) / 1,583 / (276) / 1,214; H1 2025 131 / 3,200 / (387) / 2,944; cash and cash equivalents 93,522; short-term marketable securities 6,487; $5,000 million available under the SpaceX Credit Facility; IPO net proceeds 85,675; SpaceX Notes 25,000"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 47
    url: "https://agentii.ai/v/SPCX/sec8/47"
    located_via: read_source_pages
  - figure: "Debt agreements, cells/text: '$38,433 million in aggregate principal amount of indebtedness'; no material principal payments due until 2031-07-15; SpaceX Notes five tranches, weighted average maturity 11.7 years, coupons 5.350%-6.650%; Consolidated Leverage Ratio covenant 'no greater than 3.75 to 1.0' with temporary increases to 4.25 to 1.0; 'As of June 30, 2026, the Company was in compliance with all covenants'; 'In March 2026, the Company entered into a First Amendment to Credit Agreement and Waiver ... (i) waived certain specified defaults and (ii) amended certain definitions and covenants'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 48
    url: "https://agentii.ai/v/SPCX/sec8/48"
    located_via: read_source_pages
  - figure: "Spectrum Transaction, cells/text: total consideration 'approximately $19.6 billion' = approximately $11.1 billion in equity 'through the issuance of approximately 261.8 million shares at a fixed value of $42.40 per share' plus 'up to $8.5 billion' for designated EchoStar debt payoff; Spectrum Transfer Closing occurred 2026-05-22 after FCC approval on 2026-05-12; Spectrum Acquisition Closing expected 2026-11-30; Spectrum Credit Agreement payments $1,241 million in 2026 of which $856 million paid as of June 30, 2026, $828 million in 2027, and a possible additional $827 million if closing slips to 2028-11-30"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 49
    url: "https://agentii.ai/v/SPCX/sec8/49"
    located_via: read_source_pages
  - figure: "Cash flow summary and market risk, cells/text: operating 3,466; investing (34,487); financing 100,291; Critical Accounting Estimates 'in our Prospectus'; effective interest rate on the SpaceX Notes 6.03%; 'no variable rate debt outstanding'; market-risk discussion 'in our Prospectus'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 50
    url: "https://agentii.ai/v/SPCX/sec8/50"
    located_via: read_source_pages
  - figure: "Item 4 and Item 1A, text: disclosure controls and procedures effective; 'The risk factor set forth below supplements the risk factors disclosed under the section titled Risk Factors in our Prospectus. Except as set forth below, there have been no material changes from the risk factors previously disclosed in our Prospectus' — one new AI-infrastructure risk factor naming customer concentration and 90-day termination rights"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 51
    url: "https://agentii.ai/v/SPCX/sec8/51"
    located_via: read_source_pages
---

# SPCX — risk & reachability methodology (PIL-7)

## Headline

Two jobs, and the second is the one PIL-7 exists for.

**Job 1 — the DA-24 contamination scope: PRESENT, and refuted only in SEVERITY.** DA-24 is
**not** refuted at SPCX and it is **not** untestable. It is present in the register's corrected
either-direction form, and it is proven from the **filer's own calculation linkbase**, not from
inference: `us-gaap:RestructuringCharges` and `us-gaap:ImpairmentOfLongLivedAssetsHeldForUse`
are arc children of `us-gaap:CostsAndExpenses` at **weight +1**, and `CostsAndExpenses` is the
**−1** child of `us-gaap:OperatingIncomeLoss` — so both items sit inside the operating line by
the filer's own declared structure, which is the register's founding shape (a non-operating item
flowing through the operating line). It runs in **both** directions in the served periods: a
**2** charge in Q2 2026 and a **(9) credit in H1 2026**, against **190 / 194** restructuring and
**5 / 29** impairment charges in the 2025 comparatives. The magnitude is **1.4% (Q2 2026), 0.4%
(H1 2026), 20.1% (Q2 2025) and 23.6% (H1 2025) of the operating result** — and, as a share of
the comparison the thesis actually quotes, DA-24 items account for **193 of the 827 improvement
in the Q2 loss (23.3%)** while the filed H1 deterioration of **1,143 understates the ex-item
deterioration of 1,375 by 232, or 20.3%**. The item is acquisition-driven in the filer's own
words (Note 19: "X, an indirect subsidiary of the Company (through the X Merger and subsequently,
xAI Merger) ... initiated global employee workforce reductions, the effects of which continued
into 2026"), which is what makes it a transaction inside the operating line rather than
operations. **The not-testable residual is the $354 million litigation accrual — kind 2, genuine
absence from the source** (§1.6) — and it is bounded: 4.4% of Q2 2026 costs, 2.4% of H1 2026
costs, **21.4% of H1 2026 SG&A**.

**The adjacent hazard is NOT DA-24, and conflating the two would be the error.** The consolidated
`OperatingIncomeLoss` identity fails **twice on a computable datum, with a different substituted
member in each period**: Q2 2026 computed **−4,578 = 3,379 (the AI segment, H1 duration) −
7,957**, and Q2 2025 computed **−4,615 = 426 (the ADVERTISING line, not AI) − 5,041**, against
filed (143) and (970). The correct revenue member is served correctly in all four periods
(7,814 / 12,508 / 4,071 / 8,138, and 7,814 − 7,957 = **−143 = the filed (143)**), so this is a
**kind-7 detector gap at a computable datum — remedy is the INSTRUMENT**, not the pipeline and not
the source (§1.6, §5).

**Job 2 — the classification.** Six falsifiers, **six classified, six with a named resolving
source** — PIL-7's `wrong_if` metric is **0**. **Three are structurally or commercially
unreachable** (PIL-4 `UNRESOLVABLE-FROM-PUBLIC-SOURCES` kind 2; PIL-6 `UNRESOLVABLE-FROM-PLATFORM`
kind 5; PIL-5 platform-blocked on its denominator, kind 5, with its numerator a kind-2 genuine
absence). **One is blocked by EFFORT, not reachability** (PIL-3) and I coded its first row at
SPCX to prove the surface is on-platform. **One carries the third situation — a passing result
that cannot be recorded** (PIL-2), and SPCX's filing supplies a second flavour of it that the
register has not yet named (§2.4). **One is now computable from two filed cells in a single
document** (PIL-1): SPCX files both legs of $/kg to LEO, and the spread across defensible bases
is **12.8×** — 939 to 11,977 dollars per kilogram from the same filing (§3).

## Register version note

Written at `constitution_pin: 1.5.0`, not grandfathered. Two obligations that 1.5.0 added are
discharged in full here: **DA-29** (defective checks — the circularity test on terms, §5) and
**DA-30** (a basis collapsed before an artifact sees it — §3, where four SPCX figures are shown to
carry competing bases and the spread is quantified). The successor artifact
(`2026-09-18_1500_ratio-analysis_methodology.md`, same ticker, same phase) is the sibling this one
must reconcile with; §1.7 records why its DA-24 verdict of **NOT EVIDENT** does not survive the
linkbase evidence, and why the recent-quarter artifact's scoped **REFUTED** does.

## Inheritance from 001 and from the SPCX siblings

001 is **frozen** and is not rewritten. This artifact **validates its facts** and records
corrections (§7). Three of 001's SPCX figures reproduce **exactly** from p.30's cells — the
"AI is 32.8% of SPCX revenue" case (2,561 ÷ 7,814 = 32.77%), its **clean** Connectivity
counterpart (4,291 ÷ 7,814 = 54.91%), and the clean Space series that "FELL 1.9% H1"
(1,581 ÷ 1,611 − 1 = **−1.86%**) — and 001's **$19.6 billion** spectrum reference mark
reproduces as a **filed** figure whose components foot exactly: 11.1 (equity) + 8.5 (debt payoff)
= **19.6** ([sec8 p.49](https://agentii.ai/v/SPCX/sec8/49)). Inherited without re-litigation: the
DA-23 census (extended here to a sign-partitioned 7/7 and 7/7), the articulation and overshoot
detectors, the `validate_calculation` incapacity, and the served-fact-has-no-URL traceability
gap. New here: the **linkbase proof of DA-24's mechanism**, the **sign-partitioned strip census**,
the **18-fail validator census with a sign-contaminated `diff` column**, the **four-basis spread**,
the **duration-collision defect in `get_segment_data`**, and the **classification census with the
PIL-4 identity collision**.

## Summary verdicts

| Question | Verdict |
|---|---|
| Is DA-24 present, refuted, or not testable at SPCX? | **PRESENT** — restructuring and impairment are +1 arc children of `CostsAndExpenses` in the filer's own linkbase. **Refuted in severity only.** |
| In which direction does the contaminant run? | **Both** — charges 190 / 194 / 5 / 29 / 2, and a **(9) credit in H1 2026**. |
| How big is it? | 0.03% / 0.06% / 3.87% / 2.46% of total costs; **1.4% / 0.4% / 20.1% / 23.6%** of the operating result; margin effect ≤ **4.79 pp**. |
| Does it change the headline comparison? | **Yes, at the H1 line:** the filed 1,143 deterioration understates the ex-item **1,375** by **20.3%**; at Q2 it supplies **193 of 827 (23.3%)** of the improvement. |
| Is the brief's named flow the contaminant? | **No.** The $856 million EchoStar flow is a **capitalized outflow** in investing, and the 539 + 1,545 losses sit **below** the operating line. |
| What cannot be tested? | The **$354 million** litigation accrual's period allocation — **kind 2**, bounded at **21.4% of H1 2026 SG&A**. |
| Does the adjacency explain the validator's failures? | **No — different mechanism.** A **kind-7 detector gap** at a computable datum, remedy = the instrument. |
| How many falsifiers lack a class or a named source? | **0 of 6.** |
| How many are unreachable? | **3 of 6** — PIL-4 (Class A, kind 2), PIL-5 (Class B, kind 5), PIL-6 (Class B, kind 5); the register's `structurally_unreachable` names two. |
| Can the register's PIL-4 be read unambiguously? | **No** — see §2.3. Two theses number two different claims PIL-4, and one of them FIRES. |

## 1. Job 1 — DA-24 contamination scoping at SPCX

### 1.1 Where the contaminant lives, proven from the filer's own structure

The register's DA-24 is "a non-operating item flows through the operating line, so the field
measures a transaction or a write-down rather than operations." The question at any issuer is
therefore **structural before it is economic**: is there an item whose *arc* places it inside the
operating line, and whose *nature* is a transaction? At SPCX the calculation linkbase answers the
first question and Note 19 answers the second.

`get_calculation_tree(0001628280-26-052535)`, role
`http://www.spacex.com/role/ConsolidatedStatementsofOperations` — the arcs into
`us-gaap:OperatingIncomeLoss` are **exactly two**:

```
us-gaap:OperatingIncomeLoss
  ← us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax   weight +1  "Revenue, net"
  ← us-gaap:CostsAndExpenses                                      weight -1
        ← us-gaap:CostOfRevenue                                    weight +1
        ← us-gaap:ResearchAndDevelopmentExpense                     weight +1
        ← us-gaap:SellingGeneralAndAdministrativeExpense            weight +1
        ← us-gaap:RestructuringCharges                              weight +1   <-- order 4
        ← us-gaap:ImpairmentOfLongLivedAssetsHeldForUse             weight +1   <-- order 5
```

So `RestructuringCharges` and `ImpairmentOfLongLivedAssetsHeldForUse` are **inside the operating
line by the filer's own declaration**, at +1, in the same position as cost of revenue and R&D.
That is the register's mechanism, and it is not an interpretation of captions: it is the
calculation relationship the issuer filed. The same tree places the two large non-operating flows
**outside** it — `us-gaap:OtherNonoperatingIncomeExpense` is a **+1 child of
`IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest`
("Total income (loss)")**, a sibling of `OperatingIncomeLoss`, with
`InterestExpenseNonoperating` at −1 and `InvestmentIncomeInterest` at +1. The filer's policy note
agrees with its own tree: "**Other income (expense), net consists of gain or loss on digital
assets, gain or loss on foreign currency transactions, and loss on extinguishment of debt**"
([sec8 p.39](https://agentii.ai/v/SPCX/sec8/39)).

**The nature test, from the filing's own words.** Note 19 attributes the restructuring line to an
acquisition: "In 2022, **X, an indirect subsidiary of the Company (through the X Merger and
subsequently, xAI Merger)**, initiated global employee workforce reductions, the effects of which
continued into 2026" ([sec8 p.32](https://agentii.ai/v/SPCX/sec8/32)). The impairment line is
presented as its own operating caption on the statement face and in the segment tables
([sec8 p.5](https://agentii.ai/v/SPCX/sec8/5), [sec8 p.31](https://agentii.ai/v/SPCX/sec8/31)).
Both are transaction/write-down items inside operations — **DA-24, present, either direction.**

### 1.2 The contamination scope table

All values in millions, as filed; parentheses are filed negatives. The DA-24 item is
`Restructuring charges (credits)` + `Impairment` as they appear **inside** total costs and
expenses. "Ex-item" removes the item from the operating line (a charge is added back; a credit is
subtracted), which is the only treatment consistent with it being inside the line.

| Period | Filed loss from operations | DA-24 item inside the operating line | Ex-item loss from operations | Filed margin | Ex-item margin | Δ (pts) |
|---|---|---|---|---|---|---|
| Q2 2026 | (143) | 2 charge | **(141)** | (1.83)% | **(1.80)%** | +0.03 |
| H1 2026 | (2,086) | **(9) credit** | **(2,095)** | (16.68)% | **(16.75)%** | −0.07 |
| Q2 2025 | (970) | 190 + 5 = **195 charge** | **(775)** | (23.83)% | **(19.04)%** | +4.79 |
| H1 2025 | (943) | 194 + 29 = **223 charge** | **(720)** | (11.59)% | **(8.85)%** | +2.74 |

Item as a share of the period's total costs and expenses (7,957 / 14,594 / 5,041 / 9,081):
**0.025% / 0.062% / 3.87% / 2.46%**. As a share of the operating result:
**1.40% / 0.43% / 20.10% / 23.65%**.

The Q1 2026 restructuring credit is **derived** (H1 2026 (9) less Q2 2026 2 = **(11)**), and it is
labelled derived: the filing gives only the two durations. It is the instance that shows the item
is bidirectional **within the current year**, which is the case the register's corrected
definition exists to cover — VRT supplied the charge case at a $62.0M contingent consideration,
and SPCX supplies both cases in adjacent quarters of the same fiscal year.

### 1.3 What DA-24 does to the comparison the thesis actually quotes

The level effect is small in the current year and large in the comparative, and that asymmetry is
the finding:

- **Q2:** the filed loss improved by **827** (970 → 143, disclosed as 827 / (85.3)% at
  [sec8 p.40](https://agentii.ai/v/SPCX/sec8/40)). Ex-item it improved by 775 − 141 = **634**. So
  **193 of the 827 improvement — 23.3% — is DA-24 items**, concentrated entirely in the
  *prior-year* quarter's 195 charge.
- **H1:** the filed loss deteriorated by **1,143** (943 → 2,086, disclosed as (1,143) / 121.2%).
  Ex-item it deteriorated by 2,095 − 720 = **1,375**. **The filed figure understates the ex-item
  deterioration by 232, or 20.3%.**

So a thesis quoting the filed H1 swing gets the **direction** right and the **magnitude 20%
wrong**, and a thesis quoting the Q2 swing attributes to the current period an improvement that is
**23% a prior-year comparative effect**. Both statements are quantitative and both are avoidable.

**Second-order, and not removable by add-back.** Impairment does not merely add a charge: it
removes the D&A that the asset would otherwise have generated. The evidence is in the segment
tables — Q2 2025 carries **5** of impairment in the Space column with no offsetting D&A relief in
the served periods, so at SPCX the second-order effect is **not** quantified, and the honest record
is that the ex-item series above removes the **first-order** item only. That distinction is carried
to C3.

### 1.4 DA-23 and DA-24 co-occur inside one figure

The register's SATS instance of co-occurrence has a direct SPCX analogue: the **H1 2026
restructuring credit is served with its sign stripped**.

| Period | Filed (p.5 / p.31 / p.32) | Served by the fact store | Verdict |
|---|---|---|---|
| Q2 2026 | 2 | 2,000,000 | **correct** |
| H1 2026 | **(9)** | **9,000,000** | **STRIPPED** |
| Q2 2025 | 190 | 190,000,000 | **correct** |
| H1 2025 | 194 | 194,000,000 | **correct** |

3 of 4 correct, 1 of 4 stripped, **partitioned exactly by filed sign** — the same partition holds
consolidated across concepts: **7 of 7 filed-negative instances stripped** (`OperatingIncomeLoss`
4 of 4: 2,086 / 143 / 943 / 970 against filed (2,086) / (143) / (943) / (970);
`OtherNonoperatingIncomeExpense` 2 of 2: 1,962 / 86 against filed (1,962) / (86);
`RestructuringCharges` 1 of 1) and **7 of 7 filed-positive instances correct** (restructuring 2 /
190 / 194; other income 202 / 413; impairment 29 / 5) — plus **12 of 12** in the `NetIncomeLoss`
family. Two of the instrument's own `pass` verdicts certify stripped values as correct:
`NetIncomeLossAvailableToCommonStockholdersDiluted` returns computed = reported = 541,000,000 /
diff 0 for Q2 2026 and 1,008,000,000 / diff 0 for Q2 2025, both against filed losses in
parentheses.

**The de-contamination trap.** Because the credit is *filed* as (9) and *served* as +9, a reader
who de-contaminates H1 2026 from the served store computes 2,086 + 9 = **2,095** — which happens
to be right — while a reader who does the same arithmetic from the served **parent** and the
served **item** without restoring the sign gets 2,086 − 9 = **2,077**, an error of **2 × 9 = 18**
in the wrong direction. The byte-level invariant is the register's: **the discrepancy is exactly
twice the stripped term**, and here the stripped term is small enough that only an exact identity
would catch it.

### 1.5 What is NOT DA-24 — the brief's named flow, and the register's other candidate

**The `$856 million` EchoStar flow never touches the operating line.** It is an investing outflow
recognised as an intangible asset — `Payments for intangible assets (856)` in the H1 2026 cash-flow
statement ([sec8 p.9](https://agentii.ai/v/SPCX/sec8/9)) — matching "**$856 million paid as of
June 30, 2026**" under the Spectrum Credit Agreement ([sec8 p.49](https://agentii.ai/v/SPCX/sec8/49)).
The recent-quarter artifact's scoped refutation therefore **reproduces**, and its label is
corrected: the amount is capitalised as an **intangible asset**, not to prepaid assets (§7).

**The two large non-operating losses are below the line, by both the tree and the policy.** The
H1 2026 other-income line is **(1,962)**, and the cash-flow reconciliation carries
**539** unrealized digital-asset loss and **1,545** loss on debt extinguishment
([sec8 p.9](https://agentii.ai/v/SPCX/sec8/9)). Their sum is **2,084 = 106.2% of the line**, with a
**122** residual (6.2%) consistent with the net FX position the same policy note names. The line
decomposes **completely** into the three components p.39 declares — which is what **refutes the
disposal-gain premise** the sibling artifact labelled DA-31: there is no gain on disposal in any
served period, and the two largest non-operating items are losses that were **added back** in the
Adjusted EBITDA bridge rather than hidden inside operations.

**The AI SG&A legal-expense credit is a third DA-24-shaped item, and it is disclosed.** AI SG&A
"increased by $134 million, or 33.7% ... primarily due to higher employee compensation expenses ...
of $177 million ... **partially offset by a decrease in legal expenses of $64 million due to a
dismissal of litigation against the Company**" ([sec8 p.45](https://agentii.ai/v/SPCX/sec8/45)) —
a litigation outcome inside the operating line, in the segment whose operating line is the thesis
case. Two arithmetic observations follow and both are recorded rather than smoothed: the two named
drivers leave **21 of the 134 change unfooted** (177 − 64 = 113 against 134, a 15.7% residual),
and the $64 million reduction is a **non-operating event inside operating expense** in the same
sense DA-24 names — smaller than the restructuring item in absolute terms, but **32× the Q2 2026
restructuring charge** and therefore material to the AI segment's Q2 expense story.

### 1.6 The residual untestable surface, and the adjacent hazard that is not DA-24

**(a) The $354 million litigation accrual — kind 2, genuine absence from the source.** The filing
records the accrual but not its period allocation and not its income-statement caption: "The
Company has recorded an accrual of **$354 million** for litigation losses that are probable and
reasonably estimable in **Accrued expenses and other current liabilities and Other liabilities**
on the consolidated balance sheet as of June 30, 2026. For other matters, the Company is not
currently able to estimate the reasonably possible loss or range of loss"
([sec8 p.29](https://agentii.ai/v/SPCX/sec8/29)). Both named captions are **balance-sheet**
captions. So the question "did any part of the $354 million run through the operating line in the
period, and in which caption?" **cannot be answered from any public source** — and the reason is
genuine absence, not ingestion. Bound: 354 ÷ 7,957 = **4.4% of Q2 2026 costs**; 354 ÷ 14,594 =
**2.4% of H1 2026 costs**; 354 ÷ 1,658 = **21.4% of H1 2026 SG&A**. One dated sub-event is
resolved and one is not: the NMPA matter was "dismissed by stipulation on 2026-07-16" and "the
matter is now closed" ([sec8 p.29](https://agentii.ai/v/SPCX/sec8/29)) — a **post-period** event,
so it cannot be the source of a charge taken in the quarter.

**(b) The consolidated `OperatingIncomeLoss` failure — kind 7, remedy the INSTRUMENT.** This is
the adjacent hazard, and the ratio artifact already found it. Reproduced and attributed:

| Period | Computed | Composition | Filed | Substituted member |
|---|---|---|---|---|
| Q2 2026 | **−4,578** | 3,379 (AI segment revenue, **H1** duration) − 7,957 (consolidated Q2 costs) | (143) | segment for consolidated, and the wrong duration |
| Q2 2025 | **−4,615** | **426** (the **Advertising** line, Q2 2025) − 5,041 | (970) | a revenue-disaggregation member, not the consolidated line |

Neither computed value appears anywhere in the filing. The correct member is served with the
correct value and duration in all four periods, and the identity closes exactly against the filed
statement: **7,814 − 7,957 = −143**. That combination — a datum the platform computes, whose
correct inputs it demonstrably holds, returning a value that has no referent — is **kind 7 as A19
supplies it** (VRT `gross_margin` null 10 of 10 while the issuer publishes it and the arithmetic
closes), and the remedy is **the instrument**: not a re-ingestion, not a new source. It is
**not** DA-24, and the distinction matters: DA-24 corrupts the composition of a **filed** subtotal;
this corrupts a **computed** one while the filed subtotal is unaffected.

### 1.7 Reconciliation with the two sibling SPCX artifacts

Both siblings reached a DA-24 verdict, and they are **superseded in part**:

| Artifact | Its verdict | Why it is superseded |
|---|---|---|
| `2026-09-18_1500_ratio-analysis_methodology.md` | **NOT EVIDENT** — "the component census of total costs and expenses closes to the dollar with zero residual at every period, so no third-party amount is embedded" | The census is correct and the inference is wrong: a contaminant **inside** a filed subtotal is *necessarily* absorbed by that subtotal, so a census that closes proves the subtotal foots, not that nothing non-operating is in it. The artifact says so itself ("the test with power is the component census above, not the subtraction") — and the census, read against the linkbase, is the **proof of presence**, not of absence. |
| `2026-09-18_1500_recent-quarter_methodology.md` | **REFUTED**, scoped: "the $856M EchoStar flow is a cash outflow capitalized to prepaid assets and never enters the operating line" | The scoped conclusion **reproduces** (it is an intangible-asset outflow, §1.5), but the verdict is scoped to one flow and the artifact states the scope. It is not a statement about DA-24 at SPCX. |

**The corrected verdict is PRESENT, with severity refuted.** The census does not conflict with it:
restructuring (2 / (9)) and impairment (5 / 29) are among the five named operating components the
census sums, which is exactly how a DA-24 item behaves inside a subtotal.

## 2. Job 2 — falsifier reachability classification (P6)

### 2.1 The classification vocabulary, stated before use

Two **registered** disposition classes (`check_contract.UCLASSES`), one **proposed** class, one
**flagged situation**, and one non-defect state. Stating this explicitly is required, because the
remedies differ and a verdict without a class is exactly what PIL-7's `wrong_if` counts.

| Label | Meaning | Remedy |
|---|---|---|
| `EVALUABLE` | reachable and evaluated | record the result |
| `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | the disclosure does not exist publicly | **name the specific disclosure and MONITOR** |
| `UNRESOLVABLE-FROM-PLATFORM` | public but unreachable / licensed / external registry | **record a platform-reach gap** |
| `UNVALIDATED-BY-PLATFORM` *(proposed; A5/VRT)* | the concept is filed and the structure exists, but the instrument returns nothing | record an **instrument** gap; validate by another instrument |
| **flag: `REACHABLE-BUT-NOT-RECORDABLE`** | the data is reachable, but the falsifier's *passing* result cannot be recorded as a passing datum | **replace with a recordable predicate** (a third situation, not a class — §2.4) |
| non-defect: `EFFORT-BLOCKED` | reachable, on-platform, unmeasured | **budget the reads**; not a disposition |

**Cross-cutting rules applied throughout:** `processing_status` is **non-discriminating** and is
not used here as an ingestion-absence marker. Every not-testable **kind** is assigned from the
**full seven**, none merged — and the seventh exists because a detector gap at a computable datum
has a different remedy (a fix to the instrument) from both an ingestion gap and a source gap:

| Kind | Definition | Home example |
|---|---|---|
| 1 | Ingestion absence — a period returns 0 facts; a 10-K `processing_status: pending` | the coverage endpoints that report SPCX `xbrl_filings` record_count **0** while 1,517 facts are served (§6.4) |
| 2 | **Genuine absence from the source** | SPCX's **$354 million** accrual period allocation; 001-PIL-4's microgravity value-per-kg |
| 3 | Validator-completeness — concept present, filed, arcs deep, validator returns zero rows | VRT → `UNVALIDATED-BY-PLATFORM` |
| 4 | Mechanism-population identity — the sample is defined by the mechanism's own property | a December-31 filer for DA-27; **SPCX is one** (deferred revenue measured at 12/31/2025) |
| 5 | Ingestion absence of a DATUM CLASS | licensed colocation rates (PIL-5); **FCC IBFS / ITU registries** (PIL-6) |
| 6 | Coverage window — coverage opens after the event | IRDM's IPO, outside coverage from 2022-02-17 |
| 7 | **Detector gap at a computable datum** — issuer publishes it, structure exists, arithmetic closes, instrument returns null or a substituted member | VRT `gross_margin` null 10 of 10; **SPCX `OperatingIncomeLoss` computed −4,578 / −4,615** (§1.6b) |

### 2.2 The six falsifiers, classified

| PIL | 001 state (as transcribed in `spec.md` §Pillar 7) | Class | Kind | Named resolving source |
|---|---|---|---|---|
| **PIL-1** $/kg to LEO, bases A/A′/B/C | **HOLDS on A, A′ and C; NOT EVALUABLE on B** (with an important correction, §7) | **EVALUABLE** | n/a on A/A′/C; **2** on basis B | **The 10-Q's own key-business-metrics tables + its revenue disaggregation** — both served: mass to orbit 485 / 652 / 1,041 / 1,102 t with customer bucket 87 / 88 / 132 / 163 ([sec8 p.35](https://agentii.ai/v/SPCX/sec8/35)) against Launch Services revenue 648 / 490 / 978 / 1,056 ([sec8 p.13](https://agentii.ai/v/SPCX/sec8/13)). Basis B's resolving source is a **marginal cost per launch** disclosure, which **no issuer has ever filed** → kind 2; proxy: the propellant floor, 46–92 $/kg. |
| **PIL-2** orbital power/thermal envelope; F2 constants | **PENDING** — "depends on catching a disclosure that may coincide with an immaterial-to-counterparty initiative" | **EVALUABLE** on the disclosure leg; **FLAG: `REACHABLE-BUT-NOT-RECORDABLE`** on the F2 leg; **`UNRESOLVABLE-FROM-PLATFORM`** on the generic constants | n/a on the disclosure leg (recordability, not testability); **5** on the constants leg | Disclosure leg: **the next Item 1A / segment refresh** — SPCX's current Item 1A is **one new AI-infrastructure risk factor** (customer concentration, 90-day termination rights) and otherwise incorporates the **Prospectus** by reference ([sec8 p.51](https://agentii.ai/v/SPCX/sec8/51)). Constants leg: the **peer-reviewed / NASA source class** named by the `_cross/f2-constant-sourcing` artifact (areal density 1.0–11 kg/m²; ±83% un-scoped, breaching ±50% in two of three scopes) — **nameable but not citable** under the contract. |
| **PIL-3** manufacturing rate vs launch capacity | **PENDING / UNMEASURED** — ~19 issuer risk-factor reads; 001 proposed re-scoping to two cheaper tests | **EVALUABLE — blocked by EFFORT, not reachability** | n/a; **4** applies to any sample extension | **Each of the 19 issuers' Item 1A + MD&A, served on-platform.** First row now coded: **SPCX does not cite launch availability** — its risk disclosure is customer concentration plus 90-day termination rights ([sec8 p.51](https://agentii.ai/v/SPCX/sec8/51)) and its cost drivers are R&D (+3,547 / 100.9%) and AI data-centre expansion ([sec8 p.41](https://agentii.ai/v/SPCX/sec8/41)). Second row available: SATS Item 1A. Proxy test: "does the latest Item 1A name a primary delay cause, and is it launch availability?", on a **small** sample — **not** 19, because kind 4 caps what more December issuers buy. |
| **PIL-4** microgravity economics (UTHR/MRK/BMY/AMGN) | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — "the clearest case in the workspace" | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** | **2** — genuine absence from the source | **A value-per-kg or cost-per-kg figure for a microgravity-manufactured product**, from a listed pharma's segment disclosure (UTHR / MRK / BMY / AMGN) **or Varda's financials (private)**. SPCX carries **no burden and no evidence**: it is not subscribed to this falsifier, and no microgravity-manufacturing disclosure exists in its served corpus. Proxy: the **72%** incumbent terrestrial gross margin 001 already quantifies. |
| **PIL-5** orbital-vs-terrestrial $/kW | **PENDING** — "terrestrial denominator is commercially licensed" | **`UNRESOLVABLE-FROM-PLATFORM`** on the denominator; **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** on the numerator | **5** (licensed datum class) / **2** (numerator does not exist) | Denominator: the **commercially licensed colocation / greenfield cost dataset, named by supplier and product** (basis B), plus the **VRT PUE benchmark**. Numerator: an **operator-disclosed orbital cost per kW, capacity in kW, or orbital-compute revenue** — none exists. **Proxy, and SPCX makes it computable:** the terrestrial side is now filed — AI capex **23,551** against a nameplate of **1.4 GW** = **$16,822 million per GW** of installed capacity ([sec8 p.36](https://agentii.ai/v/SPCX/sec8/36), [sec8 p.31](https://agentii.ai/v/SPCX/sec8/31)). |
| **PIL-6** spectrum / orbital-slot scarcity | **`UNRESOLVABLE-FROM-PLATFORM`** — needs FCC IBFS / ITU sources the platform does not carry | **`UNRESOLVABLE-FROM-PLATFORM`** | **5** — ingestion absence of a datum class (regulatory registries) | **FCC IBFS file numbers and the ITU Space Network List entries** for the AWS-4 / H-Block / AWS-3 blocks and for any new-entrant primary grant. **Proxy, and at SPCX it is partly decisive:** the acquisition branch of the falsifier is **answerable from the served filing** — the Spectrum Transaction is with an **incumbent** (EchoStar), FCC-approved 2026-05-12, transfer closed **2026-05-22**, acquisition closing expected **2026-11-30**, $19.6 billion total consideration ([sec8 p.49](https://agentii.ai/v/SPCX/sec8/49)). Because 001's falsifier counts only **primary** grants *without* an incumbent acquisition, this event is **excluded by construction** — it is a non-falsifying observation, and it is 001's own reference mark. |

**PIL-7 metric = 0. Six falsifiers, six classified, six with a named resolving source.**

Counted: **3 unreachable** (PIL-4, PIL-5, PIL-6), **1 effort-blocked** (PIL-3), **1 flagged** for
recordability (PIL-2), **2 reachable and evaluated or evaluable now** (PIL-1, PIL-2's disclosure
leg). The register's `structurally_unreachable` names **two** — PIL-4 and PIL-6 — and §2.3 records
why the third (PIL-5) belongs in the same list per 001's own text.

### 2.3 The identity collision: two pillars numbered PIL-4, and one of them FIRES

The reachability pillar's input is an **id list**, and at SPCX the list does not resolve
unambiguously. `PIL-7.falsifiers_under_classification: [PIL-1 … PIL-6]` sits in `002/thesis.md`,
where **PIL-4 is 002's own pillar: "SPCX's 1.4 GW nameplate restates to a facility draw, and the
restatement is computable"**, `metric: spcx_facility_pue_ratio`, `threshold: 1.5`. **001's PIL-4
is a different claim** — microgravity economics, sub-scribed to UTHR — and it is the one
`002/spec.md` calls "the clearest `UNRESOLVABLE-FROM-PUBLIC-SOURCES` case (P6)".

Both readings are live in the same register, and they behave differently:

| Reading | Class | State |
|---|---|---|
| **002's PIL-4** (1.4 GW nameplate → PUE ratio) | **`EVALUABLE`** | **The falsifier FIRES**: ratio **1.50× expected / 2.00× at the issuer's own target** → a facility draw of **2.1 GW / 2.8 GW against 1.4 GW as filed** |
| **001's PIL-4** (microgravity economics) | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** | kind 2, monitor |

**The basis must be named, or the census is not reproducible** — the same discipline DA-30
imposes on concepts, applied to pillar ids in adjacent files. This artifact assigns **both**, and
records the collision as a required fix (C6). The SPCX filing strengthens the 002 reading and is
quoted here as evidence: the metric's own definition settles the **direction** of the restatement —
nameplate compute draw "**does not represent actual power consumption or utilization. It does not
include power we install and use for our supporting infrastructure such as cooling systems, power
distribution losses, lighting, security systems, or facility-level overhead**"
([sec8 p.36](https://agentii.ai/v/SPCX/sec8/36)). So the facility draw is **strictly greater** than
1.4 GW by the filer's own definition, and what is genuinely absent is the **PUE value** that would
place the ratio against the 1.5 threshold — a **kind-2** absence layered on an evaluable claim.

### 2.4 The third situation: a passing result that cannot be recorded

**PIL-2 carries it, and the reason is a contract defect, not a reachability one.** PIL-2's falsifier
names `source=peer_reviewed_literature_or_flown_hardware_disclosure`. The artifact contract's
`citation_url_wellformed` rule is level **`fail`** and its pattern admits **only `agentii.ai`
URLs**, so **the source class PIL-2 tests against cannot be recorded in any artifact**: a passing
evaluation would be unrecordable. That is not "the data does not exist" and not "the platform
cannot reach it" — it is that **the falsifier's passing state has no recordable form**. Flagged
`REACHABLE-BUT-NOT-RECORDABLE`, with the remedy: replace it with a **recordable predicate**
(e.g. "an artifact quoting a radiator areal density names the source's class and its scope"), and
carry the contract gap to the amendment queue.

**A second flavour, which SPCX supplies and the register has not named.** 001's PIL-4 passes
**because the disclosure does not exist** — "zero of four" listed pharma disclose commercial
microgravity manufacturing — and 001 itself calls this "the same immaterial-to-the-counterparty
suppression named in §4". The distinction the task requires here is exact: **an absent disclosure is
evidence only when absence is not explained by immateriality to the counterparty.** So PIL-4's
`HOLDS` is a **non-recordable pass of a second kind**: the observation is indistinguishable from
the four filers simply not caring. The remedy is the same shape — a recordable predicate — but the
named source is different, and merging the two flavours would hide that one is a contract bug and
the other is an evidential one.

**At SPCX the same test is run on a filer that DOES care, and that is the useful contrast.**
SPCX has the segment that would carry an orbital-compute line — AI, disaggregated to four revenue
lines, with an explicit compute metric ([sec8 p.13](https://agentii.ai/v/SPCX/sec8/13),
[sec8 p.36](https://agentii.ai/v/SPCX/sec8/36)) — and it discloses **terrestrial** nameplate
compute draw with a scoped definition and **no orbital line at all**. That absence is not
immateriality to a counterparty: it is the filer declining to report a business it is otherwise
building. So PIL-2's disclosure leg at SPCX is **`EVALUABLE`, evaluated, and a true non-disclosure**
— which is a finding about the filer, distinct from both of 001 §4.4's cases.

### 2.5 Proxy tests for the structurally unreachable

For each falsifier that cannot fire, PIL-7 requires a **proxy test that is evaluable**, or an
explicit re-scope — not an unbounded carry.

- **PIL-4** (Class A, kind 2). No listed pharma discloses a microgravity value-per-kg and Varda is
  private; re-running cannot resolve it. Proxy: the **72% terrestrial incumbent gross margin** 001
  already quantifies from filed numbers — it tests the falsifier's *mechanism* (an orbital process
  must beat the buyers' existing margin) without pretending to be the missing cost figure.
- **PIL-5** (Class B, kind 5, numerator kind 2). Proxy at SPCX: **terrestrial capex per GW from
  filed cells** — AI capex **23,551** ([sec8 p.31](https://agentii.ai/v/SPCX/sec8/31)) over
  nameplate **1.4 GW** ([sec8 p.36](https://agentii.ai/v/SPCX/sec8/36)) = **$16,822 million per
  GW**, with the facility-draw sensitivity 2.1–2.8 GW reducing it to **$8,411–11,215 million per
  GW**. The comparator 002 already names is MSFT's capex-derived capacity. This is a proxy and is
  labelled one: it cannot substitute for the licensed colocation rate, and it cannot form the
  orbital ratio, because the numerator does not exist.
- **PIL-6** (Class B, kind 5). Proxy, and it is a strong one: SPCX's own licence-transfer
  disclosure is a **filed, dated institutional event** ([sec8 p.49](https://agentii.ai/v/SPCX/sec8/49)),
  and it is the register's reference mark. Together with the post-period acquisition of Mesh
  Optical (closed 2026-07-06, [sec8 p.33](https://agentii.ai/v/SPCX/sec8/33)), the served corpus
  shows **two** incumbent-acquisition events and **zero** primary grants to new entrants — which is
  the falsifier's own exclusion rule working on filed evidence. The unanswerable remainder is
  precisely the new-entrant class, and that is the IBFS/ITU gap: **platform-blocked, not
  source-blocked**, which is the distinction 002's competitive tasks exist to record.

## 3. Method — the weight discriminator, directionality, and a basis spread of 12.8×

The discriminator: a concept at **weight −1** may legitimately carry a positive magnitude (the
weight supplies the sign); a concept at **weight +1 with a parenthesised filed cell** has been
stripped. **The completing test is DIRECTIONALITY:** a **unidirectional** concept absorbs the sign
into the weight and a sign test on it is **VACUOUS**; only a **bidirectional** concept has power.

| Arc (parent ← child) | Weight | Directionality | Verdict |
|---|---|---|---|
| `OperatingIncomeLoss` ← `RevenueFromContractWithCustomerExcludingAssessedTax` | +1 | unidirectional | **VACUOUS** |
| `OperatingIncomeLoss` ← `CostsAndExpenses` | −1 | unidirectional | **VACUOUS** |
| `CostsAndExpenses` ← cost of revenue / R&D / SG&A | +1 each | unidirectional | **VACUOUS** |
| `CostsAndExpenses` ← **`RestructuringCharges`** | +1 | **BIDIRECTIONAL** (charges 190 / 194 / 2; credit (9) / derived (11)) | **EXERCISED → FAILED** (H1 2026 served +9,000,000 against filed (9)) |
| `CostsAndExpenses` ← **`ImpairmentOfLongLivedAssetsHeldForUse`** | +1 | bidirectional in principle (a reversal is possible; none served) | **UNEXERCISED** — no negative-filed instance exists, so no clearance is recorded |
| `OperatingIncomeLoss` (parent, at the consolidated level) | — | **BIDIRECTIONAL** (four loss periods, two of them loss-making) | **EXERCISED → FAILED 4 of 4** |
| `OtherNonoperatingIncomeExpense` | +1 into pre-tax income | **BIDIRECTIONAL** (2 negative, 2 positive filed) | **EXERCISED → FAILED 2 of 2 negatives** |
| `NetIncomeLoss` family | — | bidirectional | **EXERCISED → FAILED 12 of 12** |

**The rule this yields:** any clearance of a sign defect must name the **concept**, the **weight**
and a **negative-filed instance** — or be recorded `UNEXERCISED`. Applied here, every bidirectional
line is exercised and fails, the unidirectional ones are vacuous, and the impairment arc is
**honestly unexercised**.

**The DA-30 discharge — four concepts whose basis must be named, and the spread quantified.** A
basis collapsed before an artifact sees it is unrecoverable, so each is recorded with its spread:

1. **$/kg to LEO spans 12.8× in ONE filing.** Three defensible pairings from filed cells:

| Basis (H1 2026) | Numerator | Denominator | $/kg |
|---|---|---|---|
| Launch Services ÷ customer payload | 978 | 0.132 Mt | **7,409** |
| Launch Services + Launch & Development ÷ customer payload | 1,581 | 0.132 Mt | **11,977** |
| Launch Services ÷ **all** mass to orbit | 978 | 1.041 Mt | **939** |

   And the year over year: Q2 2026 648 ÷ 87 = **$7,448/kg** against Q2 2025 490 ÷ 88 =
   **$5,568/kg**, **+33.7%** — with mass to orbit **down 25.6%** and launches **down 17.8%** in the
   same quarter. Any downstream $/kg quote without a named bucket is a figure that differs by
   **an order of magnitude** from the same filing's other legitimate reading.
2. **Nameplate compute draw is GPU nameplate, not IT load and not facility draw** — 1.4 GW
   excluding cooling, distribution losses, lighting, security and facility overhead
   ([sec8 p.36](https://agentii.ai/v/SPCX/sec8/36)). Facility draw 2.1–2.8 GW (§2.3).
3. **Starlink subscribers 12.0 million is a service-line count** excluding managed enterprise and
   government customers, and expressly "distinct from the number of unique devices, account
   holders, end users or physical persons" ([sec8 p.36](https://agentii.ai/v/SPCX/sec8/36)). The
   companion metric moves the other way: **ARPU $66 against $85, −22.4%**.
4. **Segment revenue is on the segment's own basis** in the instrument: a served Space revenue of
   **1,611** is the filed **H1 2025** value under the 2026 key (§6.2).

## 4. The two portable detectors, fired at SPCX

Both are the register's recoveries from the MRCY refutation, re-run here on a different issuer, a
different concept and a different sign.

**(1) Articulation: a served series fails articulation by exactly 2 × the stripped term.**

```
Pre-tax income, Q2 2026, served components:
  143 (OperatingIncomeLoss, stripped) − 629 + 340 + 86 (stripped) = −60
Filed:                        −143 − 629 + 340 − 86 = (518)
gap = 458 = 2 × (143 + 86)                    ← EXACT
```

Two stripped terms, both at weight +1 into "Total income (loss)" per the linkbase. Q2 2025, one
stripped term:

```
970 (stripped) − 411 + 98 + 413 = 1,070    filed: −970 − 411 + 98 + 413 = (870)
gap = 1,940 = 2 × 970                        ← EXACT
```

**The instrument's own `diff` column is itself sign-contaminated.** `validate_calculation` reports
Q2 2026 `diff` **578** and Q2 2025 `diff` **200** — neither is the identity gap (458, 1,940) —
because **`reported` shares the stripped store**: both sides of the comparison are drawn from the
same corrupted series. **So `diff` magnitudes cannot be used as detector inputs.** That is the
operational consequence of the register's rule that `computed` may not be cited as a derivation and
`reported` is not the filed value.

**(2) Overshoot, at the SEGMENT level.** The served segment operating lines sum to
2,844 (Connectivity) + 3,726 (AI, stripped) + 1,204 (Space, stripped) = **7,774** against a filed
**−2,086**:

```
7,774 − (−2,086) = 9,860 = 2 × (1,204 + 3,726) = 2 × 4,930     ← EXACT
```

The invariant is **2 × |every negative component|**, and it fires on the instrument's segment view
with the same byte-level law as on the consolidated statement. **A detector wired to the
consolidated statement only would not see it.**

## 5. `validate_calculation` at SPCX: 18 fails, 9 passes, and what the passes are worth

The census across accession `0001628280-26-052535`: **pass 9, warn 2, fail 18**.

| Concept | Period | Instrument output | Filed | Verdict |
|---|---|---|---|---|
| `OperatingIncomeLoss` | Q2 2026 | computed **−4,578,000,000** / reported 143,000,000 / diff 4,721,000,000 | **(143)** | **fail** — and the computed value has no referent |
| `OperatingIncomeLoss` | Q2 2025 | computed **−4,615,000,000** / reported 970,000,000 | **(970)** | **fail** — a different substituted member |
| `CostsAndExpenses` | Q2 2025 | computed = reported = 5,041,000,000 / diff 0 | 5,041 | **pass** — correct, and it tells you nothing about the parent |
| pre-tax income | Q2 2026 / Q2 2025 | −60,000,000 / 1,070,000,000 | (518) / (870) | **fail** — gaps 458 and 1,940 = 2 × the stripped terms |
| `NetIncomeLoss` | Q2 2026 | computed 489,000,000 / reported 4,817,000,000 | (4,817) | **fail** |
| `NetIncomeLossAvailableToCommonStockholdersDiluted` | Q2 2026 / Q2 2025 | computed = reported = 541,000,000 and 1,008,000,000 / **diff 0** | (541) / (1,008) | **`pass`** on both — **a pass certifying a sign-stripped loss as correct** |
| `NetIncomeLossAvailableToCommonStockholdersBasic` | Q2 2026 | computed 4,146,000,000 / reported 541,000,000 | (541) | **fail** |

**A `validate_calculation` pass is not evidence about sign, and at SPCX two of the nine passes are
passes on stripped losses.** The mechanism is the shared store: `diff = 0` means the two columns
agree, not that either matches the filing.

**DA-29's mechanical circularity test, run on the terms.** If any term in a reconciliation appears
nowhere in the source, the check is a **back-solve** — and a back-solve closes exactly, so it can
only be caught on terms. At SPCX the Adjusted EBITDA bridge **passes the term test**:

```
H1 2026:  −4,817 + 5,290 + 1,470 − 9 + 0 + 1,293 − 553 + 1,962 + 29 = 4,665
          net loss  D&A   SBC   restr. imp. int.exp  int.inc  other   tax   = Adjusted EBITDA
          add-backs = 9,482 = 196.9% of the (4,817) net loss
```

Every one of the nine terms is a filed cell on [sec8 p.46](https://agentii.ai/v/SPCX/sec8/46), and
the bridge foots exactly at all four periods (3,538 / 1,214 / 4,665 / 2,944). **So this is not a
back-solve, and the test is discharged as a PASS on terms** — which is precisely why the criticism
of the bridge is *not* a DA-29 finding. It is arithmetic: **9,482 of add-backs convert a (4,817)
GAAP loss into +4,665**, and the resulting "margin" of **37.30%** sits **53.98 points** from the
filed operating margin of **(16.68)%**. The same construction at the segment level: AI Segment
Adjusted EBITDA **+537** against an AI GAAP operating loss of **(3,726)** — a **4,263** gap equal
to its own D&A 3,378 + SBC 894 − restructuring 9, on a segment that consumed **82.7%** of
consolidated capex (23,551 of 28,476) and **63.9%** of consolidated D&A (3,378 of 5,290).

## 6. Instrument traps that produce false zeros and false coverage

These are the ways a *zero* or a *false aggregate* was produced at SPCX without any absence in the
filing. They are recorded so no downstream artifact reads one as a finding.

1. **The query form.** A `us-gaap:`-prefixed `search_xbrl_facts` concept returns **0 rows by
   construction**; the bare concept name returns the full series. Every fact-store value in this
   artifact was retrieved with the bare name, and the six series used all returned complete.
2. **A served row on the wrong period.** `get_segment_data(fiscal_year=2026)` serves business-unit
   rows in which **Space revenue is 1,611 — the filed H1 2025 value — against a filed H1 2026
   1,581**, while Connectivity revenue 7,548 and AI revenue 3,379 are the current-year values. In
   the product rows, **3 of 11 revenue rows carry the prior-year value**: Launch Services 1,056
   (filed 978), Advertising 870 (filed 710) and Space 1,611 (filed 1,581). **All three are lines
   that FELL year over year, and each is served at its higher prior-year level** — so the period
   mixing removes exactly the three declines from the growth picture and inflates the served
   revenue row set by **268** (78 + 30 + 160).
3. **A duration collision presented as a total.** `get_segment_data` reports
   **`total_revenue: 32,531,000,000`** — which is exactly **7,814 + 12,508 + 4,071 + 8,138**, the
   sum of all four served revenue facts across **two fiscal years and two durations**, with no
   de-duplication. And **`segment_coverage_pct: 116.2`** is that total's ratio to the served
   segment-row sum (**37,792 ÷ 32,531 = 116.17%**), so the coverage figure that *looks* like a
   modest double-count **masks a 302.1% overlap** against the filed consolidated H1 2026 revenue
   (37,792 ÷ 12,508). A reader who saw only 116.2% would conclude the mix was nearly clean.
4. **Coverage endpoints that disagree with each other and with the facts.** `list_coverage(SPCX)`
   reports `xbrl_filings` **record_count 0**, and `get_ticker_coverage(SPCX)` reports `xbrl_facts`
   **record_count 1,517** — while both mark the source `data_freshness_tier: missing`. Meanwhile
   the six fact series used here are complete, correct in magnitude, and the identity closes to the
   dollar. **A zero from a coverage endpoint is evidence about the endpoint**, and this is kind 1's
   shape: an apparent ingestion absence that is not one. The same endpoints report 8 `sec_filings`
   against 10 `src_documents`.
5. **Keyword-search zeros.** A zero from `search_keyword_in_source` is **not** evidence the filing
   lacks the word. Absence in this artifact is established by **reading pages**, and the method is
   stated where it is claimed (§2.4).
6. **`processing_status` is non-discriminating** and is not used here as an ingestion-absence
   marker.
7. **A citation to a table page must quote the CELLS.** The `read_source_outline` description is
   LLM-generated, fluent and figure-dense, and it inherits the filing's signs. Every quotation in
   this artifact comes from a page I read with `read_source_pages`, and every table is quoted as
   cells.
8. **Freshness metadata is not a recency argument.** The platform reports
   `data_freshness: 2027-04-12`, seven months **ahead** of `as_of` (A11). It is not used here.
9. **The instrument's `diff` column is sign-contaminated** (§4, §5) and **its segment view is
   period-mixed** (§6.2) — neither is a DA-24 finding, and both are instrument defects.

## 7. Corrections recorded

**001 is frozen and is not rewritten.** Corrections are recorded, and the artifacts that consumed
them must restate.

| Item | Status | Basis |
|---|---|---|
| 001's **$19.6B** spectrum reference mark | **REPRODUCES as filed, and its components foot** | "$19.6 billion" = $11.1B equity + up to $8.5B debt payoff ([sec8 p.49](https://agentii.ai/v/SPCX/sec8/49)) — 11.1 + 8.5 = 19.6, exact |
| 001's "**AI is 32.8% of SPCX revenue**" | **REPRODUCES exactly** | 2,561 ÷ 7,814 = 32.77% ([sec8 p.30](https://agentii.ai/v/SPCX/sec8/30)); and the segment **decomposes** into Advertising 367 + AI Solutions & Infrastructure 2,194 ([sec8 p.13](https://agentii.ai/v/SPCX/sec8/13)) |
| 001's clean **Connectivity 54.9%** and “Space **FELL 1.9%** H1” | **REPRODUCE exactly** | 4,291 ÷ 7,814 = 54.91% and 1,581 ÷ 1,611 − 1 = **−1.86%** ([sec8 p.30](https://agentii.ai/v/SPCX/sec8/30), [sec8 p.31](https://agentii.ai/v/SPCX/sec8/31)) |
| 001 DA-01's premise "**no issuer discloses a per-launch price at commercial cadence, so $/kg must be inferred from contract values and payload mass**" | **SUPERSEDED at SPCX** | SPCX files **both legs**: Launch Services revenue by period ([sec8 p.13](https://agentii.ai/v/SPCX/sec8/13)) and mass to orbit split into customer and internal buckets ([sec8 p.35](https://agentii.ai/v/SPCX/sec8/35)). The *inference* is no longer required; the **basis must be named**, and it spans 12.8× (§3) |
| 001's **falsifier census** | **CORRECTED on membership** | 001's synthesis states "three of six falsifiers cannot fire ... **PIL-3, PIL-5 and PIL-6**", but its own text calls PIL-3 "**an unbuilt census, not an unavailable disclosure**". PIL-3's class is **`EVALUABLE`/effort-blocked**; PIL-4's microgravity economic test is the genuine source-gap. Corrected set: **PIL-4, PIL-5, PIL-6** — same count, one member different |
| 001 DA-11's reading of the 1.4 GW figure ("IT load only") | **CONFIRMED and NARROWED** | The filing's own definition ([sec8 p.36](https://agentii.ai/v/SPCX/sec8/36)) excludes cooling **and** facility overhead **and** is a GPU nameplate — so it also excludes host CPUs, DRAM, NICs, storage and PSU losses. Facility draw **2.1–2.8 GW** |
| 002's `_thesis.md` **PIL-7 id list** | **AMBIGUOUS — fix required** | `falsifiers_under_classification: [PIL-1 … PIL-6]` sits where PIL-4 is the **nameplate** pillar, while `structurally_unreachable.PIL-4` means **microgravity** (001's). The ids must carry the thesis (§2.3, C6) |
| Sibling `recent-quarter` artifact's "$856M … capitalized to **prepaid assets**" | **LABEL CORRECTED** | The cash-flow caption is "**Payments for intangible assets** (856)" ([sec8 p.9](https://agentii.ai/v/SPCX/sec8/9)); the conclusion is unaffected |
| Sibling `ratio-analysis` artifact's DA-24 verdict **NOT EVIDENT** | **SUPERSEDED → PRESENT** | A contaminant inside a filed subtotal is absorbed by that subtotal; the linkbase shows `RestructuringCharges` and `ImpairmentOfLongLivedAssetsHeldForUse` at **+1** inside `CostsAndExpenses` (§1.1, §1.7) |
| Reference to "**DA-31**" in the sibling's numbering | **REFUTED, and out of register** | The register's `REGISTERED` set is DA-01…DA-30, so the disposal-gain premise has no registered id at this pin; and at SPCX it is refuted on the facts — no disposal gain exists in any served period (§1.5) |
| `$(1,257)M` **AI operating line** | **CONFIRMED FILED — not derived** | Filed on pp. 30, 31, 44, 45 and 46 ([sec8 p.44](https://agentii.ai/v/SPCX/sec8/44), [sec8 p.30](https://agentii.ai/v/SPCX/sec8/30)). An earlier 004 resolution calling it "DERIVED, never filed" is false and is **not** propagated |

## 8. Could not be verified

- **Every quotation is page-verified; the served XBRL series are not.** The fact-store values cited
  here (`OperatingIncomeLoss`, `RestructuringCharges`, `OtherNonoperatingIncomeExpense`,
  `ImpairmentOfLongLivedAssetsHeldForUse`, the `NetIncomeLoss` family, `get_calculation_tree` and
  `validate_calculation` output) come from instruments, and **a served fact has no page-resolvable
  URL** — the platform offers no citation form for a stored fact. Provenance is recorded as
  *instrument-served* (instrument, concept, accession and source_file named in text). This is a
  **traceability gap in the platform** (C5).
- **The Prospectus is not in the served corpus.** Item 1A, Material Cash Commitments, Critical
  Accounting Estimates and Market Risk all **incorporate it by reference**, and p.34 dates it
  precisely: "our final prospectus filed with the SEC pursuant to **Rule 424(b)(4) … on June 12,
  2026**" ([sec8 p.34](https://agentii.ai/v/SPCX/sec8/34), [sec8 p.51](https://agentii.ai/v/SPCX/sec8/51),
  [sec8 p.50](https://agentii.ai/v/SPCX/sec8/50)). The served corpus holds 10 documents and no
  registration statement, so **every risk-factor statement outside the one new factor, and the
  common-control recast basis, is unread** (C4).
- **The $354 million accrual's period allocation is genuinely absent** — kind 2, bounded in §1.6a.
- **FY2025 segment data is unreachable.** `get_segment_data(SPCX, fiscal_year=2025)` returns
  `INTERNAL_ERROR: column "k" does not exist`, so the prior-year segment basis could not be
  checked, and the FY2025 10-K is not in the corpus.
- **A $830 million cash-balance difference is unexplained.** The cash-flow statement's ending
  balance is **94,352** ([sec8 p.9](https://agentii.ai/v/SPCX/sec8/9)) while the liquidity
  discussion gives cash and cash equivalents of **93,522** ([sec8 p.47](https://agentii.ai/v/SPCX/sec8/47)).
  The difference is consistent with a combined cash-and-restricted-cash caption on the statement,
  but **the caption itself was not read**, so the mechanism is **not asserted**. The internal
  consistency of the statement is exact: 3,466 − 34,487 + 100,291 = 69,270, less FX (42) = 69,228,
  and 25,124 + 69,228 = 94,352.
- **The equity consideration's valuation is unreconciled.** Approximately **261.8 million shares at
  a fixed value of $42.40** ([sec8 p.49](https://agentii.ai/v/SPCX/sec8/49)) against an IPO price of
  **$135.00** ([sec8 p.11](https://agentii.ai/v/SPCX/sec8/11)): 261.8 × (135.00 − 42.40) =
  **$24.2 billion**, or **3.18×** the fixed value. Whether the agreement provides a true-up is not
  disclosed in the served filing. **DERIVED, and flagged rather than resolved** — it bears directly
  on `deal_security_basis` and on PIL-6's consideration.
- **The segment tables' `get_segment_data` basis is not documented by the instrument** — the
  served values are checked against filed pages here rather than trusted, which is itself a finding
  (§6.2, §6.3).
- **The Q1 2026 restructuring credit of (11) is DERIVED** (H1 (9) less Q2 2), labelled as derived.
- **The Segment Adjusted EBITDA reconciliation's full definition was not read.** The components I
  read (segment operating income + D&A + SBC + restructuring) foot exactly to the segment totals at
  all periods (e.g. Q2 2026 AI: (1,257) + 1,885 + 516 + 2 = **1,146**), but the footnote-level
  adjustments, if any, were not read.
- **PIL-3's 19-issuer census was not performed.** One row is coded (SPCX, §2.2); the census is not
  claimed.

## Carry-forwards

- **C1.** The DA-24 verdict at SPCX is **PRESENT / severity-refuted**, and the sibling ratio
  artifact's **NOT EVIDENT** must be restated to it. The census it performed is the proof of
  presence, not of absence.
- **C2.** Any ex-item series at SPCX must carry the **second-order** flag: impairment removes the
  D&A the asset would have generated, that relief is not quantified here, and it is not removable
  by add-back.
- **C3.** The **$354 million** litigation accrual must be carried as a **kind-2** bound, not as a
  passed check: 4.4% of Q2 2026 costs, **21.4% of H1 2026 SG&A**.
- **C4.** Four disclosure blocks at SPCX are **incorporation-by-reference into a document the
  corpus does not carry** (Item 1A, Material Cash Commitments, Critical Accounting Estimates, Market
  Risk). Resolving them is a **platform-reach** item: obtain the **Rule 424(b)(4) prospectus filed
  2026-06-12**.
- **C5.** The platform has **no citation form for a served XBRL fact**. Until it does, every
  fact-store value in this thesis is provenance-recorded by instrument, not by link.
- **C6.** `002/thesis.md` PIL-7's id list is **ambiguous across files**: PIL-4 names 002's nameplate
  pillar (which **FIRES**) in one place and 001's microgravity pillar (Class A, kind 2) in another.
  Qualify every id with its thesis, or the census is not reproducible.
- **C7.** PIL-2 and 001's PIL-4 both carry **unrecordable passing results** — the first because the
  citation contract admits only `agentii.ai` URLs and the falsifier's source class is peer-reviewed
  literature, the second because a zero-disclosure pass is indistinguishable from
  immateriality-to-the-counterparty. Both need **recordable predicates**.
- **C8.** PIL-4, PIL-5 and PIL-6 must be carried as **proxy-tested**, not as pending-and-waiting. A
  downstream thesis that sizes against them is sizing against something that cannot happen.
- **C9.** The instrument defects recorded here — the **substituted revenue member** in
  `OperatingIncomeLoss`, the **sign-contaminated `diff` column**, the **period-mixed segment rows**,
  the **duration-collision `total_revenue`** and the **coverage endpoints reporting 0 against 1,517
  served facts** — are **kind-7 instrument gaps**, and none is remedied by re-ingestion.

## Sources

| Figure (as filed) | Source |
|---|---|
| Consolidated statement of operations: revenue 7,814 / 4,071 / 12,508 / 8,138; total costs 7,957 / 5,041 / 14,594 / 9,081; loss from operations (143) / (970) / (2,086) / (943); net loss (541) / (1,008) / (4,817) / (1,536) | [📄 SPCX 10-Q p.5](https://agentii.ai/v/SPCX/sec8/5) |
| Cash-flow statement: D&A 5,290; digital assets 539 / (252); debt extinguishment 1,545; intangible assets (856); IPO proceeds 85,675; ending 94,352 | [📄 SPCX 10-Q p.9](https://agentii.ai/v/SPCX/sec8/9) |
| Note 1: three segments; IPO 638.9 million shares at $135.00; net proceeds $85,675 million; xAI Merger 2026-02-02; X Merger 2025-03-28 | [📄 SPCX 10-Q p.11](https://agentii.ai/v/SPCX/sec8/11) |
| Note 3 revenue disaggregation: Advertising 367 / 426 / 710 / 870; AI Solutions and Infrastructure 2,194 / 311 / 2,669 / 595; AI 2,561 / 737 / 3,379 / 1,465 | [📄 SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13) |
| Legal proceedings: $354 million accrual in balance-sheet captions; "not currently able to estimate"; NMPA dismissed 2026-07-16 | [📄 SPCX 10-Q p.29](https://agentii.ai/v/SPCX/sec8/29) |
| Segment table Q2 2026: revenue 962 / 4,291 / 2,561 / 7,814; income (loss) from operations (542) / 1,656 / (1,257) / (143) | [📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30) |
| Segment tables H1 2026 / Q2 2025: H1 revenue 1,581 / 7,548 / 3,379 / 12,508; H1 OI (1,204) / 2,844 / (3,726) / (2,086); Q2 2025 OI (369) / 923 / (1,524) / (970) | [📄 SPCX 10-Q p.31](https://agentii.ai/v/SPCX/sec8/31) |
| Segment table H1 2025 and Note 19: OI (439) / 1,956 / (2,460) / (943); restructuring 443 / (9) / (168) / 2 = 268; "through the X Merger and subsequently, xAI Merger" | [📄 SPCX 10-Q p.32](https://agentii.ai/v/SPCX/sec8/32) |
| Cursor Merger expected to close Q3 2026 at a $60 billion implied equity value; Mesh Optical Merger closed 2026-07-06 | [📄 SPCX 10-Q p.33](https://agentii.ai/v/SPCX/sec8/33) |
| MD&A overview: final prospectus filed under Rule 424(b)(4) on June 12, 2026; IPO net proceeds $85,675 million after offering costs of $575 million | [📄 SPCX 10-Q p.34](https://agentii.ai/v/SPCX/sec8/34) |
| Key business metrics, Space: mass to orbit 485 / 652 / 1,041 / 1,102 t; customer payloads 87 / 88 / 132 / 163; Falcon launches 37 / 45 / 77 / 81 | [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35) |
| Key business metrics, Connectivity and AI: Starlink subscribers 12.0 / 6.0 million; ARPU $66 / $85; nameplate compute draw 1.4 / 0.4 GW excluding cooling and facility overhead | [📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36) |
| AI segment policy: other income (expense), net consists of digital assets, FX and debt extinguishment | [📄 SPCX 10-Q p.39](https://agentii.ai/v/SPCX/sec8/39) |
| MD&A consolidated results: revenue change 3,743 / 91.9% and 4,370 / 53.7%; loss from operations change 827 / (85.3)% and (1,143) / 121.2% | [📄 SPCX 10-Q p.40](https://agentii.ai/v/SPCX/sec8/40) |
| MD&A drivers: R&D +3,547 / 100.9%; SG&A +559 / 50.9%; other income (expense), net down $2,164 million on debt extinguishment and digital assets | [📄 SPCX 10-Q p.41](https://agentii.ai/v/SPCX/sec8/41) |
| AI segment table: revenue 2,561 / 737 / 1,824 / 247.5% and 3,379 / 1,465 / 1,914 / 130.6%; loss from operations (1,257) / (1,524) / 267 / (17.5)% and (3,726) / (2,460) / (1,266) / 51.5% | [📄 SPCX 10-Q p.44](https://agentii.ai/v/SPCX/sec8/44) |
| AI drivers: compensation +$177 million and legal expenses down $64 million on a litigation dismissal; AI SG&A +$134 million / 33.7% | [📄 SPCX 10-Q p.45](https://agentii.ai/v/SPCX/sec8/45) |
| Adjusted EBITDA reconciliation: net loss (4,817); D&A 5,290; SBC 1,470; restructuring (9); interest 1,293 / (553); other 1,962; tax 29; Adjusted EBITDA 4,665; segment 3,538 | [📄 SPCX 10-Q p.46](https://agentii.ai/v/SPCX/sec8/46) |
| Segment Adjusted EBITDA H1 2026 (556) / 4,684 / 537 / 4,665; cash 93,522; marketable securities 6,487; SpaceX Notes 25,000 | [📄 SPCX 10-Q p.47](https://agentii.ai/v/SPCX/sec8/47) |
| Debt: $38,433 million principal; leverage covenant 3.75 to 1.0; compliance affirmed; March 2026 First Amendment and Waiver of "certain specified defaults" | [📄 SPCX 10-Q p.48](https://agentii.ai/v/SPCX/sec8/48) |
| Spectrum Transaction: $19.6 billion = $11.1 billion equity (261.8 million shares at a fixed $42.40) + up to $8.5 billion debt payoff; FCC approval 2026-05-12; transfer closed 2026-05-22; acquisition closing expected 2026-11-30; $856 million paid as of June 30, 2026 | [📄 SPCX 10-Q p.49](https://agentii.ai/v/SPCX/sec8/49) |
| Cash flow summary: operating 3,466; investing (34,487); financing 100,291; SpaceX Notes effective rate 6.03%; "no variable rate debt outstanding"; estimates and market risk referred to the Prospectus | [📄 SPCX 10-Q p.50](https://agentii.ai/v/SPCX/sec8/50) |
| Item 1A: "supplements the risk factors disclosed under the section titled Risk Factors in our Prospectus … no material changes"; one new AI-infrastructure risk factor | [📄 SPCX 10-Q p.51](https://agentii.ai/v/SPCX/sec8/51) |
