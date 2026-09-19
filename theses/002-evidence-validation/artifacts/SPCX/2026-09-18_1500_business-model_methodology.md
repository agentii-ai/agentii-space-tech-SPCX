---
thesis_id: "002-evidence-validation"
# The contract declares `pillar` as a scalar with an enum (artifact-frontmatter.yaml line 12).
# T108–T110 bracket this artifact `[PIL-4/PIL-6]` and this artifact discharges BOTH — §3 answers
# PIL-4's attribution question and §2 answers PIL-6's classification question — so the recorded
# value is the two-value form the task specifies. NOT recorded silently: the declared type is
# scalar and this is a deviation from it. Primary pillar is PIL-6 (§2 is the longer discharge);
# PIL-4 is carried as the second. Neither `check_contract.py` nor `check_citations.py` reads this
# field, so the deviation is recorded here rather than passed over.
pillar: [PIL-4, PIL-6]
ticker: SPCX
skill: business-model
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
# Written at 1.5.0 because this artifact APPLIES the two rules the bump added: DA-29 (every
# reconciliation term named and located — §5.4 runs a fourteen-term cash-flow bridge, §11 refuses
# two `computed` values as derivations) and DA-30 (a basis named before use — §12 names six).
# `pins_match_thesis` accepts {1.4.0, 1.5.0}; 1.4.0 is the grandfathered set for the 23 artifacts
# written before the bump. This one is written after, and obeys the rules, so it records 1.5.0.
constitution_pin: "1.5.0"
assumption_pin: "2"
# skill_pin resolved 2026-09-18 by `dispatch.skill_version_hash()` (scripts/dispatch.py:132) —
# sha256 over sorted(skill_dir.rglob("*")), skipping __pycache__, feeding p.name.encode() then the
# file bytes, first 12 hex. Validated SIX OF SIX against the pins tabled in
# theses/001-technology-baseline/reproduce.md: operational-kpi 0730fd170124, unit-economics
# e87ee63269a2, secular-trends e6b41dbb2426, supply-chain 8cb3ac1de486, competitive 826995c722a4,
# risk 953fc5d396e7. `business-model` = 9479220eef91, and the value AGREES ACROSS THREE ROOTS —
# agent-plugins/agentii-equity-agent/skills/agentii/business-model,
# vertical-plugins/equity-research-core/skills/agentii/business-model, and
# ~/.claude/skills/agentii/business-model. NOTE for the Phase 7 ledger: the decoy tree set named in
# the task text (packaging/targets/{claude-code,codex,generic-cli,cowork}) NO LONGER EXISTS on disk
# — packaging/ now holds only README.md, export.py, export.sh, skillseekers.config.yaml, and
# adapters/* contain no skill copies. The 6/6 cross-validation plus the three-root agreement is the
# substitute control; 6/6 against known-good pins is what makes it a control rather than a guess.
skill_pin: "9479220eef91"
as_of: 2026-09-18
# No corpus-version endpoint is exposed by any permitted tool. The freshness stamps reachable
# DISAGREE: list_sources and search_documents report 2026-08-21; get_company_financials 2026-08-25;
# get_company_fiscal_calendar 2026-08-26; search_xbrl_facts, list_xbrl_concepts and
# validate_calculation all report `data_freshness: 2027-04-12` — seven months in the FUTURE of
# `as_of`, so it is not a corpus version and cannot be used as one. Nothing to pin.
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-07"
    chosen_reading: "the ISSUER's definition of mass to orbit, quoted verbatim — 'verified mass, including Starlink satellites, customer payloads, and development cargo, from all successful orbital and flight tests', excluding failed or scrubbed attempts. Applied here only to show that the Space series is boundary-clean because tonnage cannot be added by an acquisition."
  - da_id: "DA-08"
    chosen_reading: "'customer launch' = an external payload is the PRIMARY payload and the mission parameters are designed around it. THREE competing launch bases exist for one quarter (Falcon-only 37; Falcon+Starship 38; customer-only 10) and this artifact names all three rather than selecting one. Load-bearing for §4: the Space segment's revenue boundary is the CUSTOMER boundary, not the activity boundary."
  - da_id: "DA-11"
    chosen_reading: "the named nameplate metric is GPU count x GPU all-in power draw. It is NARROWER than IT load and strictly narrower than facility draw, and the filed definition excludes cooling, power distribution losses, lighting, security systems and facility-level overhead. Inherited from operational-kpi §3.1; not re-derived here."
  - da_id: "DA-21"
    chosen_reading: "segment boundaries are drawn by management and change over time. SPCX's three-segment frame is management-drawn and, on the evidence of §2.1, applies to periods that PREDATE the entity the AI segment belongs to."
  - da_id: "DA-23"
    chosen_reading: "sign stripping of a negative filed value, tested by the component identity run in-line at four levels and never by EPS x shares. CONFIRMED at SPCX and, for the first time in this thesis, confirmed by two of the instrument's OWN `pass` verdicts certifying sign-stripped magnitudes as correct (§5.3)."
  - da_id: "DA-24"
    chosen_reading: "a disposal gain sitting ABOVE the operating subtotal, tested by the arc set into OperatingIncomeLoss on the calculation linkbase. REFUTED at SPCX (§6), and the refutation extends to the segment level: no segment's income from operations has a disposal-gain arc."
  - da_id: "DA-25"
    chosen_reading: "an issuer-defined per-unit metric that cannot be reproduced from the filed terms. CONFIRMED at business-model scope and quantified (§7): the coarsest possible reproduction of Starlink ARPU lands 4.8 percentage points away from the disclosed change, and the metric's own definition excludes the fastest-growing customer class."
  - da_id: "DA-26"
    chosen_reading: "a twelve-month value served under a quarterly label. NOT TESTABLE at SPCX: no annual row exists anywhere in the served corpus. Recorded `unresolved (no test possible)`, NOT `clean`. But a SIBLING period defect IS present and is DA-30-class, not DA-26 (§12, instance 2)."
  - da_id: "DA-27"
    chosen_reading: "fiscal-period labels derived from the calendar rather than the issuer's fiscal calendar. CONFIRMED on method, benign on outcome — SPCX is a Dec-31 filer, so calendar and fiscal coincide. The register's detector, keyed on `source == 'default'`, mis-fires here (§9)."
  - da_id: "DA-28"
    chosen_reading: "capital-structure discontinuity around an IPO, tested on the equity rollforward and on per-share items. CONFIRMED as an open exposure, and §10 supplies the term the register lacked: a $671M H1 deduction printed on NO line of the statement of operations, arising only in the pre-IPO quarter."
  - da_id: "DA-29"
    chosen_reading: "defective CHECKS — the mechanical circularity test. If any term in a reconciliation appears nowhere in the source, the check is a BACK-SOLVE, and a back-solve closes exactly so it cannot be caught on the closure. Applied twice: §5.4 runs a fourteen-term cash-flow bridge with every term located, and §11.3 refuses two `computed` values because they are not reproducible from the instrument's own returned tree."
  - da_id: "DA-30"
    chosen_reading: "a basis the platform collapses before an artifact sees it. The artifact must NAME the basis and state WHERE it was established, PRIOR to use — which is prior to `no_single_basis_collapse`, because an artifact cannot comply by diligence alone. SIX instances found at SPCX (§12), two of them on the figures PIL-4 and PIL-6 exist to settle."
evidence_grade: DEMONSTRATED
# Not required for SPCX: contract rule `deal_security_tagging` names only IRDM, GSAT and RKLB, and
# SPCX is none of them. Recorded as `not_applicable` so the field is present and explicitly answered
# rather than merely omitted. P11's "if the acquirer is the thesis" bullet DOES reach SPCX through
# the pending Cursor/Anysphere merger — treated in §3.5 and carried as C-4, not silently dropped.
deal_security_basis: not_applicable
# The platform-side attribution question cannot be settled on its own terms: `get_segment_data`
# errors on this accession, and the nameplate metric is absent from every served fact surface.
# That is the PLATFORM disposition. The PUE-proper ratio is a separate, PUBLIC-SOURCES residual,
# carried in its own key below because the contract's enum admits only one class per artifact.
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM
pue_proper_residual: "UNRESOLVABLE-FROM-PUBLIC-SOURCES"
citations:
  - figure: "Income statement face: Revenue $ 7814 | $ 4071 | $ 12508 | $ 8138; Total costs and expenses 7957 | 5041 | 14594 | 9081; Loss from operations (143) | (970) | (2,086) | (943); Net loss $ (541) | $ (1,008) | $ (4,817) | $ (1,536); Net loss attributable to shareholders - basic and diluted $ (541) | $ (1,008) | $ (5,488) | $ (1,536); Basic and Diluted $ (0.09) | $ (0.34) | $ (1.12) | $ (0.53); Weighted average shares 5864 | 2929 | 4879 | 2902"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 5
    url: https://agentii.ai/v/SPCX/sec8/5
    located_via: read_source_pages
  - figure: "Cash-flow face, all fourteen operating terms: Net loss $ (4,817); Depreciation and amortization 5290; Share-based compensation 1470; Deferred income taxes (9); Unrealized (gain) loss on digital assets 539; Impairment and loss on disposal of fixed assets, net 40; Loss on debt extinguishment 1545; Other (72); Accounts receivable (2,003); Inventory (827); Prepaid expenses and other assets 102; Accounts payable (88); Deferred revenue 2169; Other liabilities 127; Net cash provided by operating activities $ 3466"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 9
    url: https://agentii.ai/v/SPCX/sec8/9
    located_via: read_source_pages
  - figure: "Note 1 Organization: three reportable segments; xAI Merger Date 2026-02-02; X Merger 2025-03-28; 'The Mergers were each effected through a share exchange.' No recast or reclassification sentence appears in the note."
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 11
    url: https://agentii.ai/v/SPCX/sec8/11
    located_via: read_source_pages
  - figure: "Table 15 cash and restricted cash: Cash and cash equivalents $ 93522 | $ 24747 ... 'Total as presented in the consolidated statements of cash flows | $ 94352 | $ 25124' — establishing that 25,124 is the Dec-31-2025 restricted-cash-inclusive subtotal and 11,501 the Dec-31-2024 opening balance, both of which the instrument mis-serves (§12, instance 4)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 12
    url: https://agentii.ai/v/SPCX/sec8/12
    located_via: read_source_pages
  - figure: "Table 17 segment revenue axes, all four periods: Space Launch Services 648|490|978|1056; Launch & Development 314|256|603|555; Space 962|746|1581|1611; Consumer 2485|1721|4633|3213; Enterprise & Government 1806|867|2915|1849; Advertising 367|426|710|870; AI Solutions & Infrastructure 2194|311|2669|595; AI 2561|737|3379|1465; Total 7814|4071|12508|8138 — column order Q2 2026 | Q2 2025 | H1 2026 | H1 2025"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 13
    url: https://agentii.ai/v/SPCX/sec8/13
    located_via: read_source_pages
  - figure: "Note 18, Table 42 (Q2 2026): Income (loss) from operations | (542) | 1656 | (1,257) | (143); segment capital expenditures 1174 | 1367 | 15828 | 18369; 'The Company's CODM does not evaluate operating and reportable segments using asset or liability information.'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 30
    url: https://agentii.ai/v/SPCX/sec8/30
    located_via: read_source_pages
  - figure: "Table 43 (H1 2026): Space 1581 / 2785 / (1,204); Connectivity 7548 / 4704 / 2844; AI 3379 / 7105 / (3,726); Total 12508 / 14594 / (2,086); segment capex 2226 | 2699 | 23551 | 28476. Table 44 (Q2 2025): 746 / (369); 2588 / 923; 737 / (1,524); total 4071 / (970)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 31
    url: https://agentii.ai/v/SPCX/sec8/31
    located_via: read_source_pages
  - figure: "MD&A Overview — 'we operate our business in three reportable segments'; IPO 638.9M Class A shares at $135.00 with net proceeds $85,675M; Cursor Merger ~$60B implied equity value expected to close in Q3 2026"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 34
    url: https://agentii.ai/v/SPCX/sec8/34
    located_via: read_source_pages
  - figure: "Table 47 mass to orbit 485 | 652 | 1041 | 1102; of which customer payloads 87 | 88 | 132 | 163; of which internal payloads 397 | 563 | 908 | 938. Table 48 Falcon launches 37 | 45 | 77 | 81; customer launches 10 | 9 | 17 | 21; internal launches 27 | 36 | 60 | 60; Starship launches 1 | 1 | 1 | 3; and the segment boundary sentence 'Our Space segment revenue only reflects our customer launches and customer activities.'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "Table 51 nameplate compute draw | 1.4 | 0.4 (gigawatts, 'As of') under the AI heading, with the definition 'the number of GPUs installed in our data centers at the end of the period multiplied by their respective all-in power draw ... does not include power we install and use for our supporting infrastructure such as cooling systems, power distribution losses, lighting, security systems, or facility-level overhead.' Table 50 Starlink Subscriber ARPU $66 | $85 | $66 | $85"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 36
    url: https://agentii.ai/v/SPCX/sec8/36
    located_via: read_source_pages
  - figure: "Table 52 revenue mix within the Space segment: Launch Services 67.4% | 65.7% | 61.9% | 65.5%; Launch & Development 32.6% | 34.3% | 38.1% | 34.5%; Space 100.0% | 100.0% | 100.0% | 100.0% — the cell that bounds what the word 'launch' covers"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 37
    url: https://agentii.ai/v/SPCX/sec8/37
    located_via: read_source_pages
  - figure: "Table 53 consolidated growth: Revenue 7814 | 4071 | 91.9% | 12508 | 8138 | 53.7%; Total costs and expenses 7957 | 5041 | 57.8% | 14594 | 9081 | 60.7%; Loss from operations (143) | (970) | (85.3)% | (2,086) | (943) | 121.2%; Net loss $ (541) | $ (1,008) | $ (4,817) | $ (1,536)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 40
    url: https://agentii.ai/v/SPCX/sec8/40
    located_via: read_source_pages
  - figure: "'Other income (expense), net ... decreased by $2,164 million ... primarily due to the loss on extinguishment of debt and unrealized loss on digital assets.' — the second, independent confirmation that the filed 539 is a LOSS"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 41
    url: https://agentii.ai/v/SPCX/sec8/41
    located_via: read_source_pages
  - figure: "Space segment results, four periods: revenue 962 | 746 | 1,581 | 1,611; total costs and expenses 1,504 | 1,115 | 2,785 | 2,050; Loss from operations (542) | (369) | (1,204) | (439); customer launches 10 | 9 | 17 | 21"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 42
    url: https://agentii.ai/v/SPCX/sec8/42
    located_via: read_source_pages
  - figure: "Connectivity segment results, four periods: revenue 4,291 | 2,588 | 7,548 | 5,062 with growth 65.8% | 49.1%; Income from operations 1,656 | 923 | 2,844 | 1,956 with growth 79.4% | 45.4%; a 22.4% decline in Starlink subscriber ARPU against 101.2% growth in Starlink subscribers; Enterprise and government revenue growth of $939M against consumer growth of $764M"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 43
    url: https://agentii.ai/v/SPCX/sec8/43
    located_via: read_source_pages
  - figure: "Table 56 AI segment, four periods: revenue 2,561 | 737 | 247.5% | 3,379 | 1,465 | 130.6%; cost of revenue 1,106; research and development 2,178; selling, general and administrative 532; restructuring 2; total 3,818; Loss from operations $ (1,257) | $ (1,524) | $ (3,726) | $ (2,460)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 44
    url: https://agentii.ai/v/SPCX/sec8/44
    located_via: read_source_pages
  - figure: "'AI loss from operations for the three months ended June 30, 2026 decreased by $267 million, or 17.5%' and 'for the six months ended June 30, 2026 increased by $1,266 million, or 51.5%' — the AI operating line in narrative prose, and the H1 direction reversed against the Q2 direction on the same line"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 45
    url: https://agentii.ai/v/SPCX/sec8/45
    located_via: read_source_pages
  - figure: "Table 57 non-GAAP bridge terms (Q2 2026): (541) + 2848 + 831 + 2 + 0 + 629 - 340 + 86 + 23 = 3538; Table 58 segment Adjusted EBITDA (205) | 2597 | 1146 | 3538 — every term of the operating-subtotal reconciliation named"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 46
    url: https://agentii.ai/v/SPCX/sec8/46
    located_via: read_source_pages
  - figure: "'an increase in capital expenditures of $21,511 million related to the build out of data centers and related infrastructure, and space launch facilities and related infrastructure' — the issuer's own allocation narrative, which §3.6 replaces with the filed number"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 50
    url: https://agentii.ai/v/SPCX/sec8/50
    located_via: read_source_pages
  - figure: "Balance sheet: Digital assets 1098 | 1637; Total assets $ 192770 | $ 92079; Cash and cash equivalents $ 93522 | $ 24747 — the 1,637 -> 1,098 move that corroborates the 539 digital-asset loss arithmetically"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 4
    url: https://agentii.ai/v/SPCX/sec8/4
    located_via: read_source_pages
  - figure: "Johnsen: 'We ended the second quarter with 1.4 gigawatts of nameplate compute, up from 1 gigawatt in Q1 and 400 megawatts a year earlier. We expect to end this year at over 2 gigawatts'; 'Total company capital expenditures in the second quarter were approximately $18.4 billion, of which roughly $15.8 billion supported AI compute infrastructure'"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 3
    url: https://agentii.ai/v/SPCX/ect1/3
    located_via: read_source_pages
  - figure: "Musk: 'our tentative target is to actually have 20 gigawatts at the power and cooling level online by the end of next year'; 'we expect to have far in excess of the power cooling that's needed'; 'our goal is to have far more power, cooling and electrical equipment than we have GPUs' — the facility-side comparator, on a different date and a different scope from Table 51"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 4
    url: https://agentii.ai/v/SPCX/ect1/4
    located_via: read_source_pages
---

# SPCX × business-model — Segment Boundary and Entity Boundary, Q2 2026

**Pillar** PIL-6 (primary) · PIL-4 (second) — the two subscriptions `thesis.md` attaches to
`SPCX × business-model`. **Ticker** SPCX · **Skill** `business-model` · **Mode** `methodology`
· **As of** 2026-09-18.

**Role in this thesis.** T108–T110 scope this artifact as *"Segment-boundary check before the P4
restatement, so the 1.4 GW is attributed to the right segment; the entity-boundary classification
(P6)."* It exists to settle two things. **For PIL-6:** of every SPCX growth figure 001 quoted, which
is a clean read of one legal/segment entity and which is an artefact of a boundary change — with
the `12.3% of revenue` figure, whose *denominator was never stated*, reproduced or corrected. **For
PIL-4:** which segment the 1.4 GW belongs to, established from the filing, and whether the
platform's extraction attributes it correctly. This artifact does **not** re-derive the PUE
restatement; that is owned by `operational-kpi` §3 and is cited, not recomputed, per the
inherited-figure convention `unit-economics` §0 established.

**Scope of the census.** It goes deeper than 001 rather than repeating it. Every SPCX figure 001
attributed to a page in the six 001 SPCX artifacts is either reproduced here from a read page or
corrected here. 001 is frozen; corrections are recorded in §14. Where a figure is already
established by one of this thesis's three earlier SPCX artifacts, it is cross-referenced rather
than re-derived, and the cross-reference is named.

**Provenance of every page number.** Every page number in this artifact was established by
`read_source_pages` on the accession named, and **every quoted figure is a CELL read off a page,
or a served XBRL fact named as such with its `dimensions`.** No platform `description` field is
quoted anywhere, and no sentence *about* a table is offered as evidence — which is the failure
mode contract rule `table_pages_quote_cells_not_prose` exists for, and the mode by which all three
of 001's page-attributed quotations were produced. Only two sources are cited: `sec8` (10-Q
accession `0001628280-26-052535`, 55 pages, filed 2026-08-04) and `ect1` (Q2 2026 earnings call,
2026-08-04). The same-day earnings 8-K `sec7` is **deliberately not cited**, because this artifact
did not read it and the two sibling artifacts that did have already extracted what it holds.
Platform page numbers are used throughout; the offset between platform numbering and printed
footers on the pages read is +4 (p.36 prints "35"), and **the offset is not corrected anywhere in
this artifact**, because a right citation "corrected" into a wrong one is worse than no citation.

---

## Summary of verdicts

| # | Question | Verdict | Where |
|---|---|---|---|
| 1 | What is the `12.3% of revenue` figure 12.3% **of**? | **Space segment revenue ÷ consolidated total revenue, Q2 2026** — `962 ÷ 7,814 = 12.31%`. It is **not** "launch" (launch-only is 8.29%) and the denominator is **entity-boundary contaminated** (ex-AI: 18.31%) | §1 |
| 2 | **PIL-6** — how many of 001's SPCX growth figures are unclassified for entity-boundary effects? | **ZERO unclassified — 31 classified.** But **11 of 31 are CONTAMINATED**, including two 001 treated as clean and one of them its flagship | §2 |
| 3 | **PIL-4** — which segment does the 1.4 GW belong to? | **The AI segment**, unambiguously — Table 51, p.36, under the `AI` heading in Key Business Metrics | §3.1 |
| 4 | **PIL-4** — does the platform's extraction attribute it correctly? | **NO — but not by mislabelling it.** The metric is absent from every served fact surface, and the *adjacent* consolidated operating figure is computed from a **segment's revenue in both periods**, exactly twice (§3.2) | §3.2 |
| 5 | **PIL-4** — does the PUE falsifier fire? | **Cannot fire on this artifact's evidence.** Not testable: no like-for-like pair exists. Direction disclosed (ratio > 1.0 by design). Inherited band: 1.50–2.00×, which fires only at the ceiling | §3.4 |
| 6 | **P10** — does the Orbital-Compute Underwriting Rule bind? | **Partly, and decisively on one gate.** P10's power/manufactured-score gate binds nothing here (the AI segment is terrestrial). Its launch-cost floor and its inadmissibility clause both reach the figures | §3.5 |
| 7 | **DA-23** | **CONFIRMED, and strengthened** — 12 of 12 `NetIncomeLoss`-family facts sign-stripped, and **two of the instrument's own `pass` verdicts certify sign-stripped magnitudes as correct** | §5 |
| 8 | **DA-24** | **REFUTED** — at consolidated and at segment level | §6 |
| 9 | **DA-25** | **CONFIRMED** and quantified — the coarsest reproduction lands 4.8pp from the disclosed change, and the metric excludes the fastest-growing customer class by definition | §7 |
| 10 | **DA-26** | **NOT TESTABLE** — no annual row exists. Recorded unresolved, **not** clean | §8 |
| 11 | **DA-27** | **CONFIRMED on method, benign on outcome**; the register's detector mis-fires at a third issuer | §9 |
| 12 | **DA-28** | **CONFIRMED as open exposure**, and the unprinted term is found: **$671M**, H1-only, pre-IPO-only | §10 |
| 13 | **DA-29** | **FAILS on the instrument, PASSES on this artifact.** 14-term bridge, every term located, closure exact. Two `computed` values refused as derivations | §11 |
| 14 | **DA-30** | **SIX instances**, two of them on the figures this artifact exists to settle | §12 |

**The two sentences that carry this artifact.** *The 12.3% is Space ÷ consolidated — a numerator that is
segment-clean over a denominator that contains a company SPCX did not own a year earlier; on the
revenue line that same entity change produced **48.7% of the quarter's growth**, and 001 quoted that
contribution as evidence of organic migration.* And: *the 1.4 GW is an AI-segment metric, and the
platform's numeric layer substituted **a segment's revenue for consolidated revenue** in computing
the consolidated operating line — in two periods, against a different segment each time, exactly.*

---

## 1. The figure this artifact exists to settle: what `12.3%` is 12.3% **of**

### 1.1 Reproduction

001's carry-forward reads, verbatim: *"Launch is 12.3% of revenue and fell 1.9% across a half in
which total revenue rose 53.7%."* The number appears in four 001 files, always without a
denominator. It reproduces exactly, and the denominator is the **consolidated total**, not the
segment total:

```
962  /  7,814  =  0.123113  ->  12.31%      Q2 2026, Space revenue / consolidated revenue
1,581 / 12,508 =  0.126399  ->  12.64%      H1 2026, same pair
```

Space revenue `962` for Q2 2026 and `1,581` for H1 2026, and consolidated revenue `7,814` /
`12,508`, are all printed cells ([📄 sec8 p.13](https://agentii.ai/v/SPCX/sec8/13) Table 17;
[📄 sec8 p.40](https://agentii.ai/v/SPCX/sec8/40) Table 53). So the figure is a **segment share of
consolidated revenue**, and the segment it is a share *of* is named in its own table.

**Three things follow, and none of them is the thing 001 said.**

### 1.2 The numerator is not "launch"

The Space segment is not the launch business. The filing breaks it:

| Within Space, % of segment revenue | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---|---|---|---|
| Launch Services | 67.4% | 65.7% | 61.9% | 65.5% |
| Launch & Development | 32.6% | 34.3% | 38.1% | 34.5% |
| Space | 100.0% | 100.0% | 100.0% | 100.0% |

[📄 sec8 p.37](https://agentii.ai/v/SPCX/sec8/37) Table 52. The absolute cells agree with the
revenue axis ([📄 sec8 p.13](https://agentii.ai/v/SPCX/sec8/13) Table 17): Launch Services `648` +
Launch & Development `314` = `962` = Space revenue for Q2 2026 ✓; `978` + `603` = `1,581` = H1 2026
Space revenue ✓. **So a third of the segment 001 called "launch" is Launch & Development**, which
is the development-contract line, and the launch-only share of consolidated revenue is

```
648 / 7,814  =  0.082928  ->  8.29%
```

**001's label overstates the launch business's revenue share by 4.0 percentage points, or 48.5%
relative** (`12.31 ÷ 8.29 = 1.485`). "Launch is 12.3% of revenue" is false as written; launch is
**8.3%**, and the segment is 12.3%.

### 1.3 The denominator contains an entity SPCX did not own a year earlier

This is the PIL-6 finding, and it is not the named case. The named case is *"AI is 32.8% of SPCX
revenue."* **The contamination is broader than the named case: it reaches every ratio whose
denominator is consolidated revenue, which includes 001's flagship Space-share statistic.** Removing
the AI segment from both periods:

| Basis | Q2 2026 | Q2 2025 | Q2 change | H1 2026 | H1 2025 | H1 change |
|---|---|---|---|---|---|---|
| As reported (consolidated) | 7,814 | 4,071 | **+91.9%** | 12,508 | 8,138 | **+53.7%** |
| Ex-AI (denominator only) | 5,253 | 3,334 | **+57.6%** | 9,129 | 6,673 | **+36.8%** |
| **Inflated by** | | | **34.3 pp** | | | **16.9 pp** |

`7,814 - 2,561 = 5,253` ✓; `4,071 - 737 = 3,334` ✓; `12,508 - 3,379 = 9,129` ✓;
`8,138 - 1,465 = 6,673` ✓. AI segment revenue for all four periods is a printed cell
([📄 sec8 p.44](https://agentii.ai/v/SPCX/sec8/44) Table 56: `2,561 | 737 | 247.5% | 3,379 | 1,465`).
The reported growth rates are the filing's own ([📄 sec8 p.40](https://agentii.ai/v/SPCX/sec8/40)
Table 53: `91.9%` and `53.7%`).

**The consolidated growth rate overstates the growth of the pre-existing business by 34.3 points in
the quarter — 59.5% of the reported figure — and 16.9 points over the half, 45.9%.** And the same
correction applied to 001's flagship:

| Space share of revenue | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---|---|---|---|
| ÷ consolidated (001's implied basis) | **12.31%** | 19.80% | **12.64%** | 17.32% |
| ÷ ex-AI | **18.31%** | 24.14% | **17.32%** | 24.14% |

*(H1 2025 Space `1,611` and consolidated `8,138`; the ex-AI denominators are `5,253`, `3,334`,
`9,129`, `6,673`.)*

**The direction of 001's claim survives every basis — Space's share falls on all four — but the
level does not.** On the as-reported basis the fall is **7.5 points** (19.80 → 12.31, Q2) or
**4.7 points** (17.32 → 12.64, H1). On the ex-AI basis it is **5.8 points** (24.14 → 18.31) or
**6.8 points** (24.14 → 17.32). **A share that ranges from 8.29% to 18.31% depending on a
denominator the artifact never named cannot support a level claim, and 001's "12% of the company"
phrase is a level claim.** The direction is the honest part and 001 had it right.

### 1.4 The period bases are mixed

001's sentence pairs a **Q2** share (`12.3%`) with an **H1** growth rate (`−1.9%`) and an **H1**
consolidated comparator (`+53.7%`). The three figures are on two different periods. The correct
pairs are `12.64% / −1.9% / +53.7%` (all H1) or `12.31% / +29.0% / +91.9%` (all Q2) — and note the
second triple reverses the rhetorical point, because Space revenue **rose 29.0%** in the quarter
([📄 sec8 p.42](https://agentii.ai/v/SPCX/sec8/42): Space revenue `962 | 746`).

**The half-year is the honest frame and 001 chose it correctly.** Space's H1 revenue fell `1.9%`
(`1,581` vs `1,611`) while the quarter rose `29.0%`. That is a real divergence and it is the
filing's, not the artifact's. But the share and the growth rate in one sentence must share a period.

### 1.5 DA-30 on the quoted figure: two bases both round to 12.3%

The figure is ambiguous **as quoted**, independently of any calculation:

```
Space segment revenue    / consolidated revenue   =  962 / 7,814  =  12.31%
Launch Services revenue  / ex-AI consolidated     =  648 / 5,253  =  12.34%
```

Both round to "12.3%". **The quote cannot be disambiguated from its own text.** This is DA-30 in its
purest form — a basis the platform (and the artifact) collapsed before a reader saw it — and it is
the reason §12 is written as a basis register rather than as a footnote.

---

## 2. PIL-6 — every 001 growth figure, classified

### 2.1 The boundary events, and what the filing does **not** say

| Event | Date | Effect on the comparison window |
|---|---|---|
| X Merger — X Holdings and X.AI Corp into xAI | 2025-03-28 | inside the H1 2025 comparative |
| **xAI Merger — X.AI Holdings Corp into SPCX** | **2026-02-02** | **common control; prior periods recast** |
| Five-for-one forward stock split | 2026-05 | per-share items adjusted retroactively |
| IPO — 638.9M Class A at $135.00, net proceeds $85,675M | 2026-06 | capital-structure discontinuity (DA-28) |
| Cursor Merger — Anysphere, ~$60B implied | pending, Q3 2026 | not in any reported figure |

The first three rows are filed ([📄 sec8 p.11](https://agentii.ai/v/SPCX/sec8/11) Note 1; the
split is in the equity note). The IPO and the Cursor Merger are filed on
[📄 sec8 p.34](https://agentii.ai/v/SPCX/sec8/34).

**What the filing does not say is the load-bearing part.** Note 1 discloses the mergers and then
stops. Its operative sentence is *"The Mergers were each effected through a share exchange."* There
is **no recast sentence, no reclassification sentence, and no restatement sentence anywhere in the
filing**: `search_keyword_in_source("recast")` returns **zero** hits on this accession, and the only
`reclassif` hit is p.22's *"Reclassification of Class C Common Stock,"* which is an equity
presentation matter and not a segment one.

**That zero is not evidence the word is absent** — the standing rule applies, and this artifact
discharges it by the stronger route: **the pages were read.** [📄 sec8 p.11](https://agentii.ai/v/SPCX/sec8/11)
says only "effected through a share exchange." [📄 sec8 p.12](https://agentii.ai/v/SPCX/sec8/12)
says the interim statements are *"prepared on the same basis as the annual consolidated financial
statements"* and lists only **Cloud Services Arrangements** and **Business Combinations** as new or
changed policies. [📄 sec8 p.50](https://agentii.ai/v/SPCX/sec8/50) states *"no material changes to
our critical accounting policies."* **The retrospective combination is disclosed ONLY by its
arithmetic signature, never by narrative.**

And the signature is unmistakable. The AI segment reports a comparative for **Q2 2025** — revenue
`737`, loss from operations `(1,524)` — and for **H1 2025** — revenue `1,465`, loss `(2,460)`
([📄 sec8 p.44](https://agentii.ai/v/SPCX/sec8/44) Table 56) — periods that **predate the merger by
seven and eleven months respectively.** A segment cannot appear in a comparative for a period before
its entity existed unless the comparative was recast.

**This is the PIL-6 hazard in one paragraph.** The recast is real, the recast is material, and **no
page says so.** An automated reader — and 001 — sees `+247.5%` with no boundary flag on the page,
because there is none.

### 2.2 The classification table

Sixty-one figures were extracted from 001's six SPCX artifacts before classification. Deduplicating
to the distinct growth claims and the distinct ratio claims gives **31**. Every one is classified.
The axes are: **CLEAN** — numerator and denominator both inside a single entity throughout the
window; **CONTAMINATED** — the figure mixes real change with entity change; **NOT TESTABLE** — the
figure cannot be classified from any filed disclosure.

| # | Figure 001 quoted | Claim | Class | Why |
|---|---|---|---|---|
| 1 | Space revenue `$962M → $1,581M`; Q2 `+29.0%`, H1 `−1.9%` | 001 §2, carry-fwd 2 | **CLEAN** | SpaceX inside the entity throughout; comparatives `746` / `1,611` filed |
| 2 | Launch Services revenue `648` / `978`; H1 `−7.4%` | §1.2 | **CLEAN** | sub-line of a clean segment |
| 3 | Launch & Development `314` / `603`; H1 `+8.6%` | §1.2 | **CLEAN** | sub-line of a clean segment |
| 4 | Connectivity revenue `$4,291M`; Q2 `+65.8%`, H1 `+49.1%` | 001 §2 | **CLEAN** | Starlink never merged |
| 5 | Consumer revenue `2,485`; Q2 `+44.4%` | 001 §2 | **CLEAN** | sub-line of a clean segment |
| 6 | Enterprise & Government `1,806`; Q2 `+108.3%` | 001 §2 | **CLEAN** | sub-line of a clean segment |
| 7 | Connectivity operating income `$1,656M`; Q2 `+79.4%` | 001 §2 | **CLEAN** | clean segment, clean subtotal |
| 8 | Starlink subscribers `12.0M` vs `6.0M`; `+101.2%` | 001 §2 | **CLEAN** (level) / see #9 | subscriber count is a Connectivity fact |
| 9 | Starlink ARPU `$66` vs `$85`; `−22.4%` | 001 §2 | **CLEAN but DA-25** | not entity-boundary contaminated; denominator contaminated in the DA-25 sense — §7 |
| 10 | Connectivity R&D `$294M`; `+105.6%` | 001 §2 | **CLEAN** | clean segment |
| 11 | Connectivity gross margin `52.0%` | 001 §2 | **CLEAN** | `(4,291 − 2,060) / 4,291` |
| 12 | Mass to orbit `485` vs `652` t; Q2 `−25.6%`, H1 `−5.5%` | 001 §1 | **CLEAN** | tonnage in a fairing is not acquirable — DA-07 metric |
| 13 | Customer payloads `87` vs `88` t; `−1.1%` | 001 §1 | **CLEAN** | as #12 |
| 14 | Internal payloads `397` vs `563` t; `−29.5%` | 001 §1 | **CLEAN** | as #12 |
| 15 | Falcon launches `37` vs `45`; `−17.8%` | 001 §1 | **CLEAN** | hardware count |
| 16 | Internal launches `27` vs `36`; `−25.0%` | 001 §1 | **CLEAN** | hardware count |
| 17 | Customer launches `10` vs `9`; Q2 `+11.1%`, H1 `−19.0%` | 001 §1 | **CLEAN** | DA-08 count |
| 18 | Starship launches `1` vs `1` Q2; `1` vs `3` H1 | 001 §1 | **CLEAN** | hardware count |
| 19 | Space R&D `$1,076M`; `+55.3%` | 001 §4 | **CLEAN** | clean segment |
| 20 | Space cost of revenue `329` vs `330`; `−0.3%` | 001 §2 | **CLEAN** | clean segment |
| 21 | Space operating loss `$(542)M`; `+46.9%` wider | 001 §2 | **CLEAN** | clean segment, clean subtotal |
| 22 | **`12.3% of revenue`** | 001 §2, carry-fwd 2 | **CONTAMINATED** | clean numerator, **contaminated denominator** — §1.3 |
| 23 | Space operating margin `−56.3%` | 001 §2 | **CONTAMINATED** | a ratio; denominator is consolidated only in the `12.3%` form — as a *segment* margin it is CLEAN. 001's label conflates the two |
| 24 | **Consolidated revenue `+91.9%` Q2 / `+53.7%` H1** | 001 §1, §5 | **CONTAMINATED** | 34.3 / 16.9 points of the reported figure is entity change — §1.3 |
| 25 | **AI revenue `$2,561M`, `32.8%` of revenue** | 001 §2 | **CONTAMINATED — DO NOT QUOTE** | the named case; xAI's segment on a recast base |
| 26 | **AI revenue `+247.5%` Q2 / `+130.6%` H1** | 001 §1, §4 | **CONTAMINATED** | 100% inorganic; SPCX did not own xAI in either comparative |
| 27 | **AI H1 2025 comparative = `—`** | 001 §2 table | **CONTAMINATED — and false** | the filing prints `$1,465M` ([📄 sec8 p.44](https://agentii.ai/v/SPCX/sec8/44)) — §14.1 |
| 28 | **`AI is the largest contributor to consolidated growth, +$1,824M`** | 001 §4 | **CONTAMINATED** | **48.7% of the quarter's growth is the entity change** — §2.3 |
| 29 | Connectivity contributor `+$1,703M` | 001 §4 | **CLEAN contrast** | 45.5% of the growth, organic |
| 30 | **Nameplate compute draw `1.4 GW` from `0.4 GW`; `+250%`** | 001 §4 | **CONTAMINATED** | xAI's fleet; the `0.4 GW` comparator is a date on which xAI was outside the entity — §3.3 |
| 31 | `H1 2026 capex increase $21,511M`, "data centers named first" | 001 §5 | **CLEAN as filed; the ATTRIBUTION is not** | the increase is filed; the *split* is the finding — §3.6 |

**Verdict, extended: Space CLEAN · Connectivity CLEAN · AI CONTAMINATED · consolidated
CONTAMINATED · and every ratio whose denominator is consolidated CONTAMINATED, which includes the
flag's own flagship statistic.** 001's own classification instinct was right and incomplete: it
called the AI series contaminated and stopped there, leaving the consolidated series — which 001
quoted six times — unclassified.

### 2.3 The contamination, quantified

The three segment revenue contributions to the consolidated quarterly revenue increase tie exactly:

```
AI           2,561 -   737  =  1,824
Connectivity 4,291 - 2,588  =  1,703
Space          962 -   746  =    216
                              -----
                              3,743   =  7,814 - 4,071   ✓ EXACT
```

and for the half:

```
AI           3,379 - 1,465  =  1,914
Connectivity 7,548 - 5,062  =  2,486
Space        1,581 - 1,611  =    (30)
                              -----
                              4,370   = 12,508 - 8,138   ✓ EXACT
```

Every term is a printed cell ([📄 sec8 p.13](https://agentii.ai/v/SPCX/sec8/13) Table 17;
[📄 sec8 p.40](https://agentii.ai/v/SPCX/sec8/40) Table 53). Therefore:

- **`1,824 / 3,743 = 48.7%` of SPCX's Q2 2026 revenue growth came from a segment the company did not
  own a year earlier.**
- **`1,914 / 4,370 = 43.8%` of the half-year's growth did.**

**001 reported the `$1,824M` as evidence of migration** — *"the largest single contributor to
consolidated growth, ahead of Connectivity's $1,703M."* Both numbers are correct as filed. **The
inference is not: an increase that exists because an entity was acquired is not migration, and it is
48.7% of the total.** This is the case PIL-6 was convened on, arriving through a figure 001 quoted
as clean.

### 2.4 The register gap

**No registered DA covers what §2.1 found.** DA-21 covers management-drawn segment boundaries;
DA-28 covers capital-structure discontinuity around an IPO; DA-26 and DA-27 cover period labelling.
**None covers common-control recasting across a change of reporting entity** — the hazard where the
comparative itself is restated to a different legal perimeter and every growth rate spanning the
boundary silently changes meaning. This was first raised at `operational-kpi` §7.5 and
`recent-quarter` §10.4 and is **re-raised here with the flagged cost measured**: 34.3 points on a
reported growth rate, 48.7% of a growth contribution, and a flagship share statistic whose level
moves 6.0 points. Recommended as a register addition, referred to the Phase 7 ledger (C-1).

### 2.5 PIL-6 falsifier outcome

`wrong_if: count_of_spcx_growth_figures_unclassified_for_entity_boundary_effects > 0`. **The
counter is ZERO on this artifact's population: 31 of 31 classified, none left unclassified.** The
strict reading of the falsifier is therefore **discharged, not fired.**

**This is recorded as a pass of the test and not as a clean bill**, because the population is the
figures 001 quoted and the classification is bounded by the pages read. Two consequences follow and
both point the same way: **11 of the 31 are CONTAMINATED**, so the discharge is a statement about
classification and not about usability; and the artifact that created the exposure (001's business-model
artifact) is the one whose flagship figure carries it. **PIL-6 moves AWAY from its falsifier firing
and TOWARD its named case being true and larger than named.**

---

## 3. PIL-4 — the 1.4 GW, and which segment it belongs to

### 3.1 The filed cell, and its heading

Under `Key Business Metrics`, under the section heading `AI`, the filing prints:

```
| Nameplate compute draw | 1.4 | 0.4 |        (gigawatts, "As of")
```

[📄 sec8 p.36](https://agentii.ai/v/SPCX/sec8/36) Table 51, with columns `As of June 30, 2026` and
`As of June 30, 2025`. The definition on the same page is verbatim: *"the number of GPUs installed
in our data centers at the end of the period multiplied by their respective all-in power draw.
Nameplate compute draw reflects installed capacity and does not represent actual power consumption
or utilization. It does not include power we install and use for our supporting infrastructure such
as cooling systems, power distribution losses, lighting, security systems, or facility-level
overhead."*

**The attribution is unambiguous and it is the filing's, not an inference:** the cell sits inside
the AI section of Key Business Metrics, and the AI segment is defined as *"AI computational
infrastructure"* ([📄 sec8 p.34](https://agentii.ai/v/SPCX/sec8/34)). The metric is also a
**point-in-time** quantity (`As of`), not a period flow.

**So the platform's extraction cannot be accused of mislabelling it** — because, as §3.2 shows, the
platforms's fact layer does not carry it. The attribution failure is one layer removed and it is
demonstrable.

**Corroborated on the call, on the same basis and at higher granularity.** The metric has an
intra-year path the filing does not print: *"We ended the second quarter with 1.4 gigawatts of
nameplate compute, up from 1 gigawatt in Q1 and 400 megawatts a year earlier. We expect to end this
year at over 2 gigawatts"* ([📄 ect1 p.3](https://agentii.ai/v/SPCX/ect1/3)). That is `0.4 → 1.0 →
1.4 → >2.0 GW` across four `As of` dates — so the filing's two-date table is the sparse form of a
four-point series, and the Q1 `1.0 GW` is the only intermediate. **It also independently confirms the
`AI` attribution:** the sentence sits inside the AI-segment discussion, and the same call reports
*"total company capital expenditures in the second quarter were approximately $18.4 billion, of
which roughly $15.8 billion supported AI compute infrastructure"* — against the filed segment capex
of AI `$15,828M` of `$18,369M` = **86.2%** (§3.6), a match to the hundred million on both terms.

### 3.2 Does the platform's extraction attribute it correctly?

**The metric itself: not testable, and honestly so.** `get_segment_data(SPCX)` — the platform's only
segment-attribution surface — **returns an error on this accession**:
`INTERNAL_ERROR: column "k" does not exist`. And the metric is absent from every served fact
surface reachable with the permitted tools. **The zero here is NOT evidence of absence**, and the
reason matters: `list_xbrl_concepts` does not index extension concepts at all. Proved by positive
control — `list_xbrl_concepts(search="FinanceLeaseExpense")` returns **zero**, while
`spcx:FinanceLeaseExpense` **is present in this accession's calculation tree**. So the concept
index covers `us-gaap` only, and a zero from it says nothing about `spcx:*`. Whether the 1.4 GW
exists as an extension fact is `UNRESOLVABLE-FROM-PLATFORM`; the disposition is recorded in
frontmatter.

**The adjacent consolidated figure IS testable, and it fails — twice, exactly.** The instrument
serves a `computed` value for `OperatingIncomeLoss` that is not the filed value, and both instances
decompose to the same mechanism: **a SEGMENT's revenue in the parent's slot.**

```
Q2 2026   computed  -4,578,000,000   reported  143,000,000   diff  4,721,000,000   fail
          -4,578  =  3,379  (AI segment revenue, H1 2026, dimension us-gaap:StatementBusinessSegmentsAxis: spcx:AIMember)
                   - 7,957  (consolidated Total costs and expenses, Q2 2026)              ✓ EXACT

Q2 2025   computed  -4,615,000,000   reported  970,000,000   diff  5,585,000,000   fail
          -4,615  =    426  (Advertising segment revenue, Q2 2025, dimension spcx:AdvertisingMember)
                   - 5,041  (consolidated Total costs and expenses, Q2 2025)              ✓ EXACT
```

`426` is the Advertising segment's Q2 2025 revenue ([📄 sec8 p.13](https://agentii.ai/v/SPCX/sec8/13)
Table 17: Advertising `367 | 426 | 710 | 870`). `5,041` is the Q2 2025 consolidated total costs and
expenses ([📄 sec8 p.5](https://agentii.ai/v/SPCX/sec8/5): `Total costs and expenses | 7957 | 5041`).

**The truth is `$(143)M` and `$(970)M`** ([📄 sec8 p.5](https://agentii.ai/v/SPCX/sec8/5)), established
at four independent levels in §5.2. Three readings follow, and the third is the PIL-4 one:

1. **Neither `computed` nor `reported` equals the filed value in either period.** There is no rule of
   thumb between the two columns; *"trust `computed`"* is wrong on both rows and *"trust `reported`"*
   is wrong on both rows.
2. **The substituted member is DIFFERENT in the two periods** — `spcx:AIMember` at H1 2026 duration in
   one, `spcx:AdvertisingMember` at Q2 2025 duration in the other, and in the second case the cost
   term is from the *same* period while in the first the revenue term is from a *different, longer*
   period. So the defect is not a stable mis-selection that could be patched; it is an unstable one.
3. **This is the PIL-4 answer.** The instrument's consolidated operating-income computation is
   populated, in both periods, by **a dimensioned segment fact** — and in Q2 2026 it is populated by
   **the AI segment's revenue**, the very segment the 1.4 GW belongs to. The extraction does not
   merely fail to attribute the AI segment; **it imports the AI segment's revenue into the
   consolidated slot.** This is the NVDA child-for-parent substitution (NVDA §3a, candidate N-1)
   recurring at SPCX in the SAME concept and with a WORSE signature: at NVDA the substituted value
   was at least the same period's segment total; here it is a different period's.

**Regime test, per NVDA's condition.** NVDA established: substitution is **silent** where nothing is
unallocated and produces an **overstatement** where something is. **SPCX is in the SILENT regime,
and the test is not vacuous because the check was run.** Every segment sum ties exactly in all four
periods — revenue, every expense line, operating income, D&A, SBC, restructuring and capex:

```
Q2 2026   (1,257) + (542) + 1,656  =  (143)   ✓
H1 2026   (3,726) + (1,204) + 2,844 = (2,086) ✓
Q2 2025   (1,524) + (369) +   923  =  (970)   ✓
H1 2025   (2,460) + (439) + 1,956  =  (943)   ✓
capex    1,174 + 1,367 + 15,828 = 18,369      ✓
capex    2,226 + 2,699 + 23,551 = 28,476      ✓
```

[📄 sec8 p.30](https://agentii.ai/v/SPCX/sec8/30), [📄 sec8 p.31](https://agentii.ai/v/SPCX/sec8/31),
[📄 sec8 p.42](https://agentii.ai/v/SPCX/sec8/42), [📄 sec8 p.43](https://agentii.ai/v/SPCX/sec8/43),
[📄 sec8 p.44](https://agentii.ai/v/SPCX/sec8/44). All child axes tie too (Launch Services +
Launch & Development = Space; Consumer + Enterprise & Government = Connectivity; Advertising + AI
Solutions & Infrastructure = AI; Products + Services = consolidated). The reconciling items —
interest expense `629` / `1,293`, interest income `340` / `553`, other expense `86` / `1,962`, tax
`23` / `29` — sit **below** the operating line in the Total Reportable Segments column and are added
back identically in both Adjusted EBITDA reconciliations. **Nothing is unallocated.** And the filing
confirms the absence of an allocation apparatus rather than merely implying it: *"The Company's CODM
does not evaluate operating and reportable segments using asset or liability information."*
([📄 sec8 p.30](https://agentii.ai/v/SPCX/sec8/30), Note 18).

**Consequence for the extraction: the silent regime is the DANGEROUS one here, not the safe one.**
Because nothing is unallocated, every total ties — and a segment-substituted child is therefore
indistinguishable from a correct parent *at the total*. The defect is visible only by comparing
`computed` against the filed cell, one line at a time. **The detector is line-level, not
total-to-total** — which is the VRT lesson (A6) recurring on the operating line itself.

### 3.3 The comparator is a date, not a perimeter

The `0.4 GW` is an `As of June 30, 2025` value ([📄 sec8 p.36](https://agentii.ai/v/SPCX/sec8/36)).
**On 2025-06-30, xAI was not a subsidiary of SPCX** — the merger date is 2026-02-02
([📄 sec8 p.11](https://agentii.ai/v/SPCX/sec8/11)). So the disclosed `+250%` compares a fleet
consolidated into the entity in February 2026 against a comparator measured seven months before it
was consolidated. The comparative is recast for *revenue* (§2.1) but the recast is a presentation
convention, not an acquisition: it does not make 2025-06-30 a date on which SPCX owned xAI's GPUs.

**The `1.4 GW` series is therefore CONTAMINATED on the numerator-perimeter axis**, and this is a
PIL-6 finding sited inside PIL-4's own metric. The current-period value `1.4` is a fact about SPCX's
consolidated fleet as of 2026-06-30 and is usable as a level. **The `+250%` growth rate over it is
not, and the `0.4 GW` comparator is not a like-for-like base.** `operational-kpi` §4 classified this
series CONTAMINATED and reached the same conclusion; this artifact adds the mechanism (the comparator
is a **pre-acquisition date**) and the consequence for the metric's use.

### 3.4 PUE — the falsifier, and its disposition

PIL-4's `wrong_if` is `metric=spcx_facility_pue_ratio threshold=1.5 source=issuer_disclosure_or_industry_PUE_benchmark op=">"`.

**This artifact cannot fire it, and says so rather than reporting an inert test as a passed one.**
The reason is structural, and it is the opposite of a missing number: **the two bases are disclosed on
different dates and different scopes, so no like-for-like ratio is formable.**

| Basis | Value | Date | Scope |
|---|---|---|---|
| Nameplate compute draw (filed) | **1.4 GW** | As of 2026-06-30 | GPU count × all-in GPU draw; **excludes** cooling, distribution losses, lighting, security, facility overhead |
| Facility-side power **and cooling** (spoken) | **20 GW** *target* | End of 2027 | different date, different period, a target |

[📄 sec8 p.36](https://agentii.ai/v/SPCX/sec8/36) and [📄 ect1 p.4](https://agentii.ai/v/SPCX/ect1/4).
The transcript figure is Musk's: *"our tentative target is to actually have 20 gigawatts at the power
and cooling level online by the end of next year."* **A 2027 target divided by a 2026 actual is not a
PUE ratio**; `operational-kpi` §3.2 forms the restatement against a *same-period* facility-side
disclosure and obtains a **1.50× central / 2.00× target** band, which fires PIL-4's falsifier at the
ceiling and sits exactly at the threshold centrally. **That result is inherited, cited, and NOT
recomputed here** — this artifact did not read the page that carries the same-period comparator and
will not assert a term it has not located (DA-29). **PUE-proper — the true facility-to-IT ratio — is
`UNRESOLVABLE-FROM-PUBLIC-SOURCES`**, carried in its own frontmatter key because the contract's enum
admits one class.

**What the filing DOES settle is the direction, and it is disclosed in words twice:** *"we expect to
have far in excess of the power cooling that's needed"* and *"our goal is to have far more power,
cooling and electrical equipment than we have GPUs"* ([📄 ect1 p.4](https://agentii.ai/v/SPCX/ect1/4)).
**The ratio is greater than 1.0 by design, the company says so, and the magnitude is undisclosed.**
That is a `CLAIMED` directional statement and it is admissible as one.

### 3.5 P10 — the Orbital-Compute Underwriting Rule, and whether it binds

**It binds this artifact on two of its five gates and on its admissibility clause, and on a third it
does not bind at all.** Stated plainly rather than gestured at:

| P10 gate | Binds? | Why |
|---|---|---|
| Array area **~5,000–5,600 m² per MW** (not the naive ~2,450 m²) | **NO — not reached** | The 1.4 GW is explicitly **terrestrial**: the AI segment is *"AI computational infrastructure"* ([📄 sec8 p.34](https://agentii.ai/v/SPCX/sec8/34)), the metric's own definition says *"GPUs installed in our data centers"* and excludes *"facility-level overhead"* ([📄 sec8 p.36](https://agentii.ai/v/SPCX/sec8/36)), and the issuer's capital narrative names *"data centers"* first ([📄 sec8 p.50](https://agentii.ai/v/SPCX/sec8/50)). No orbital array is claimed, so no area-per-MW test has a subject |
| Launch cost vs the **~$46/kg** F5a floor | **YES — binds** | The Space segment's Launch Services line is the read-through, and `unit-economics` §3 already carried this gate to a verdict on this issuer. This artifact adds only the boundary fact: Launch Services is `648` of the quarter's `962` Space revenue and `8.29%` of consolidated — **the P10 gate is being tested on 8.29% of the company** (§1.2) |
| **Admissibility** — SPCX's *"up to 1 million satellites at 100 kW/tonne"* filing is `CLAIMED` | **YES — binds** | 001 quoted it as `CLAIMED` and 001 was right. This artifact **does not use it as an input anywhere**, and re-confirms the grade: it is an aspiration in a separate filing with no revenue line, and P10's admissibility clause excludes it from underwriting |
| Payload-per-flight justification for any sub-`$46/kg` assumption | **YES — binds** | Any sub-floor launch cost must clear it; not invoked here |
| Manufactured-score / mass-to-orbit conversion | **NO — not reached** | same reason as gate 1 |

**The load-bearing consequence is the second row.** P10's launch-cost gate is a gate on the launch
business, and **on this filing the launch business is 8.29% of consolidated revenue** — so a P10
verdict sourced from SPCX's Space segment is a verdict about one twelfth of the company, and a
P10 verdict sourced from SPCX's *consolidated* figures would be a verdict about a company whose
growth is 48.7% entity change. **This is the boundary problem reaching P10 itself.**

**P11 is adjacent and does reach SPCX**, though `deal_security_basis` is not required for it.
SPCX is not a deal security under P11's definition (it is not itself subject to an announced
unclosed acquisition); **it is the acquirer**, and the Cursor/Anysphere merger is an announced,
unclosed, all-stock transaction at a ~$60B implied equity value expected to close in Q3 2026
([📄 sec8 p.34](https://agentii.ai/v/SPCX/sec8/34)). P11's *"if the acquirer is the thesis"* bullet
therefore binds SPCX: the combined entity, the deal financing and the dilution are in scope, and the
close date is the dated catalyst. **No figure in this artifact includes Cursor.** Carried as C-4.

### 3.6 Capital allocation — replacing 001's word-order argument with the filed number

001 argued *"Data centers are named first"* from the ordering of a noun phrase in the investing
narrative ([📄 sec8 p.50](https://agentii.ai/v/SPCX/sec8/50)):
*"an increase in capital expenditures of $21,511 million related to the build out of data centers and
related infrastructure, and space launch facilities and related infrastructure."* **The filing has
the number, so the word-order argument is not needed:**

| H1 2026 segment capex | $M | Share |
|---|---|---|
| **AI** | **23,551** | **82.7%** |
| Connectivity | 2,699 | 9.5% |
| Space | 2,226 | 7.8% |
| **Total** | **28,476** | 100% |

([📄 sec8 p.31](https://agentii.ai/v/SPCX/sec8/31) Table 43.) Q2 2026 is more concentrated still:
AI `15,828` of `18,369` = **86.2%** ([📄 sec8 p.30](https://agentii.ai/v/SPCX/sec8/30) Table 42). And
the segment capex total is the **same basis** as the consolidated line, which is checkable:
`28,476` = `Purchases of property, plant, and equipment` on the cash-flow face
([📄 sec8 p.9](https://agentii.ai/v/SPCX/sec8/9)) to the million. **So the AI segment is
82.7% of SPCX's capital expenditure and 32.8% of its revenue, and the Space segment — the company
001's thesis anchors on — is 7.8% of the capex and 8.29% of consolidted revenue on the
launch-only basis.** That is the capital-allocation statement, and it is a cell.

---

## 4. Segment boundary, delivered: what the Space segment's revenue boundary **excludes**

The single most important sentence for the business-model read is on
[📄 sec8 p.35](https://agentii.ai/v/SPCX/sec8/35), verbatim:

> *"We allocate a significant amount of launch capacity to our Connectivity segment, and expect to
> allocate a significant amount to our AI segment in the future. **Our Space segment revenue only
> reflects our customer launches and customer activities.**"*

and the metric definition preceding it: *"Mass to orbit and launches generally grow more rapidly
than Space segment revenue because these metrics include our internal constellation deployments from
which we do not recognize inter-segment revenue."*

**So the Space segment's revenue boundary is the CUSTOMER boundary, not the activity boundary.** The
activity is far larger than the revenue and the gap is filed:

| Q2 2026 | Count | Share of launches |
|---|---|---|
| Customer launches | **10** | **26.3%** |
| Internal launches (all Starship is internal by footnote) | **28** | **73.7%** |
| **Total** | **38** | 100% |

`37` Falcon + `1` Starship = `38`; `27` + `1` = `28` internal; `10` customer
([📄 sec8 p.35](https://agentii.ai/v/SPCX/sec8/35) Table 48). The same arithmetic for the other three
periods: H1 2026 `17` customer of `78` = **21.8%**; Q2 2025 `9` of `46` = **19.6%**; H1 2025 `21` of
`84` = **25.0%**.

**Three consequences, and the third is the business-model finding:**

1. **"Launch is 12.3% of revenue" is not merely mislabelled — the segment it names is a customer
   boundary.** Three quarters of the launches produced no Space revenue *by design*, not by
   underperformance.
2. **The customer share is RISING** — 19.6% → 26.3% in the quarter, i.e. customer launches `+11.1%`
   while total launches fell `−17.4%` (`38` vs `46`). So Space revenue rose `29.0%` in a quarter in
   which the launch *activity* fell `17.4%`. **Two opposite-signed rates on one activity, both
   correct, both the filing's.**
3. **The AI segment's growth consumes Space capacity invisibly.** The filing states the intent —
   *"expect to allocate a significant amount to our AI segment in the future"* — and the mechanic —
   internal launch costs are *capitalised* rather than expensed as Space cost, per
   `operational-kpi` §3.1 and the p.36 inter-segment sentence. **So the buildout that produces the
   1.4 GW will draw on the Space segment's capacity without appearing in the Space segment's
   revenue or margin.** The 82.7% of capex is not the whole of the AI segment's call on the company.

---

## 5. DA-23 — the component identity, in-line, at four levels

### 5.1 The statements have no gross-profit line

**SPCX does not file a `gross profit` subtotal.** The statement face runs Revenue → Cost of revenue →
Research and development → Selling, general, and administrative → Restructuring charges (credits) →
Impairment → **Total costs and expenses** → **Loss from operations**
([📄 sec8 p.5](https://agentii.ai/v/SPCX/sec8/5); the MD&A version is identical,
[📄 sec8 p.40](https://agentii.ai/v/SPCX/sec8/40)). **Consequence for DA-23's detector set:**
Detector 1 in its canonical `gross profit − opex = operating_income` form is **UNAVAILABLE**, and
the gross-profit bound is **UNEXERCISED** — there is no gross-profit line to bound. This is recorded
as *unexercised*, **not as clean**. The generalised form IS available and is fully reliable, because
`Total costs and expenses` is itself a filed subtotal summing all five expense lines:

```
Revenue  -  Total costs and expenses  =  Loss from operations
```

encoded in the linkbase as `OperatingIncomeLoss = Revenue (+1) + CostsAndExpenses (−1)`.
**Detector availability is therefore a THIRD axis, additional to the two the register records: whether
the issuer files a `CostsAndExpenses`-class subtotal at all.**

### 5.2 The four identities, in-line, every period

```
SPACE         962 - 329 =  633  (65.8% gross)   1,076 + 99 = 1,175  ->  (542)  ✓
H1          1,581 - 1,115 =  466               1,670      = 1,670  ->  (1,204) ✓
CONNECTIVITY  4,291 - 2,060 = 2,231 (52.0%)     294 + 281  =   575  ->  1,656  ✓
H1          7,548 - 4,704 = 2,844                                    ->  2,844  ✓
AI            2,561 - 1,106 = 1,455             2,178 + 532 + 2 = 2,712 -> (1,257) ✓
H1          3,379 - 7,105 = (3,726)                                  -> (3,726) ✓
CONSOLIDATED  7,814 - 3,495 = 4,319             3,548 + 912 + 2 = 4,462 ->  (143) ✓
H1         12,508 - 5,883 = 6,625               7,062 + 1,658 + (9) = 8,711 -> (2,086) ✓
```

**The two H1 segment rows are stated in the two-cell form and the expense decomposition is NOT
printed for them**, and that asymmetry is deliberate rather than an omission. For Connectivity H1
and AI H1 this artifact does not hold the individual `cost of revenue` / `R&D` / `SG&A` cells
verbatim; it holds the **filed totals** — Connectivity H1 `7,548 / 4,704 / 2,844` and AI H1
`3,379 / 7,105 / (3,726)` ([📄 sec8 p.31](https://agentii.ai/v/SPCX/sec8/31) Table 43) — and so it
prints `Revenue − Total costs and expenses = Income (loss) from operations` with both terms quoted
and **refuses to name a component it did not locate.** Printing a plausible decomposition here would
be exactly the back-solve DA-29 forbids: it would close, and it would close on an invented term. The
quarterly rows can be decomposed because the segment expense lines are printed on
[📄 sec8 p.42](https://agentii.ai/v/SPCX/sec8/42)/[p.43](https://agentii.ai/v/SPCX/sec8/43)/[p.44](https://agentii.ai/v/SPCX/sec8/44).

Segment cells from [📄 sec8 p.42](https://agentii.ai/v/SPCX/sec8/42) / [📄 sec8 p.43](https://agentii.ai/v/SPCX/sec8/43) / [📄 sec8 p.44](https://agentii.ai/v/SPCX/sec8/44);
consolidated cells from [📄 sec8 p.5](https://agentii.ai/v/SPCX/sec8/5). **8 of 8 close with zero
residual**, and each is a two-term form — `Revenue − Total costs` — where every term is printed.
EPS × shares was not used anywhere in this artifact and is **inadmissible** (the DA-28 arrow cuts
both ways: at SPCX the weighted-average share count moved `2,929M → 5,864M` across the split, the
preferred conversion and the IPO, so a per-share product is a different basis each period).

### 5.3 The instrument: two `pass` verdicts that are wrong on sign

**This is the cleanest DA-23 instance this thesis has produced, because it is not a `fail`.** From
`validate_calculation` on accession `0001628280-26-052535`:

```
us-gaap:NetIncomeLossAvailableToCommonStockholdersDiluted | Jun 30 2026 | computed  541,000,000 | reported  541,000,000 | diff 0 | pass
us-gaap:NetIncomeLossAvailableToCommonStockholdersDiluted | Jun 30 2025 | computed 1,008,000,000 | reported 1,008,000,000 | diff 0 | pass
```

Both verdicts are `pass`. **The filed values are `$ (541)` and `$ (1,008)` — negative**
([📄 sec8 p.5](https://agentii.ai/v/SPCX/sec8/5)). The instrument certifies as correct the
**sign-stripped magnitudes of two net losses.** A consumer filtering on `status == pass`, or on
`diff == 0`, receives a value that is wrong by 2× with a clean bill of health.

**And the strip is total on this concept family: all twelve served `NetIncomeLoss`-family facts are
positive**, against twelve filed negative cells — `(541)`, `(1,008)`, `(4,817)`, `(1,536)` for each of
the three concepts. Per-fact, not per-period; uncorrelated with profitability or with period. The
weight discriminator explains the other side of the ledger and produces **zero miscalls in six
testable pairs** at SPCX (and +38 at MSFT): `CostsAndExpenses` enters at **weight −1** and is stored
positive `7,957` and is **correct, not stripped**; `OperatingIncomeLoss` enters the pretax parent at
**weight +1**, is filed parenthesised, and is **STRIPPED**; `InterestExpenseNonoperating` at
**weight −1** → positive `629`, correct; `InvestmentIncomeInterest` at **+1**, filed positive, stored
positive, correct.

### 5.4 The cash-flow face: fourteen terms, every term located (DA-29)

```
  Net loss                                      (4,817)
+ Depreciation and amortization                  5,290
+ Share-based compensation                       1,470
+ Deferred income taxes                             (9)
+ Unrealized (gain) loss on digital assets         539
+ Impairment and loss on disposal of fixed
  assets, net                                       40
+ Loss on debt extinguishment                    1,545
+ Other                                            (72)
                                                   473
+ Accounts receivable                           (2,003)
+ Inventory                                       (827)
+ Prepaid expenses and other assets                102
+ Accounts payable                                 (88)
+ Deferred revenue                               2,169
+ Other liabilities                                127
                                                ------
  Net cash provided by operating activities      3,466   ✓ EXACT
```

All fourteen signed terms are printed cells on [📄 sec8 p.9](https://agentii.ai/v/SPCX/sec8/9) — the
signs above are the filing's, with the two parenthesised negatives kept parenthesised — and the
closure is exact to the million with zero residual. **DA-29 compliance: no term is a back-solve, no term is `computed`, and the closure is not
the evidence — the terms are.** Two consequences beyond compliance:

1. **The filing's own arithmetic settles the sign of the digital-asset item.** `539` is **added
   back**, and non-cash losses are added back while non-cash gains are subtracted. Therefore the
   filed `539` under the caption *"Unrealized (gain) loss on digital assets"* is a **LOSS**, and the
   parenthesised `(252)` is a **GAIN**. Three independent corroborations: the caption's own
   `(gain) loss` ordering; the MD&A sentence *"primarily due to the loss on extinguishment of debt
   and unrealized loss on digital assets"* ([📄 sec8 p.41](https://agentii.ai/v/SPCX/sec8/41)); and
   the balance sheet, where Digital assets moved `1,637 → 1,098`, i.e. **−539 exactly**
   ([📄 sec8 p.4](https://agentii.ai/v/SPCX/sec8/4)).
2. **The H1 non-GAAP bridge is reproducible from the statement faces and closes exactly** — so this
   artifact needs no page it did not read:

   ```
   Net loss (4,817) + D&A 5,290 + SBC 1,470 + restructuring (9) + impairment 0
           + interest expense 1,293 - interest income 553 + other expense 1,962 + tax 29
   = 4,665   ✓ EXACT
   ```

   Every term is a cell on [📄 sec8 p.5](https://agentii.ai/v/SPCX/sec8/5) or
   [📄 sec8 p.9](https://agentii.ai/v/SPCX/sec8/9). **A GAAP net loss of `$(4,817)M` and an Adjusted
   EBITDA of `+$4,665M` is a gap of `$9,482M`** — and the two items that make most of the gap are the
   two that §6 examines. The Q2 bridge is the filing's own and matches:
   `(541) + 2,848 + 831 + 2 + 0 + 629 − 340 + 86 + 23 = 3,538` ([📄 sec8 p.46](https://agentii.ai/v/SPCX/sec8/46) Table 57).

**And the instrument fails DA-29 on this same statement.** `NetCashProvidedByUsedInOperatingActivities`
returns `computed 6,010,000,000 / reported 3,466,000,000 / diff 2,544,000,000 / fail` — a `fail` on a
reported value that is **exactly right** (`3,466` is the filing's cell). Worse: **evaluating the
platform's own returned linkbase arcs against the platform's own served facts does not reproduce
`6,010`**, so the `computed` column is not a derivation from the instrument's own tree. That is the
contract's DA-29 corollary demonstrated mechanically rather than argued: *`computed` may not be cited
as a derivation.* Related: the tree weights on this role disagree with the statement face on at least
five arcs — the two **loss-captioned** items (`Unrealized (gain) loss on digital assets`,
`Loss on debt extinguishment`) are carried at **weight −1** where the filing adds both.

---

## 6. DA-24 — REFUTED at SPCX, at consolidated and at segment level

DA-24 is a disposal gain sitting **above** the operating subtotal. Tested by the arc set into
`OperatingIncomeLoss` on the calculation linkbase, not by the absence of a line on a face:

**The linkbase carries exactly two arcs into `OperatingIncomeLoss`** — `Revenue` at `w = +1` and
`CostsAndExpenses` at `w = −1`. There is no disposal-gain arc and no place for one, at any of the
four levels. That is the structural test, and it is what distinguishes a refutation from a
non-observation.

Corroborated on the face: the $856M EchoStar flow is an **investing outflow** — *"Payments for
intangible assets | (856) | —"* ([📄 sec8 p.9](https://agentii.ai/v/SPCX/sec8/9)) — paid to a Trust on
2026-05-22 and carried as a prepaid asset until the Spectrum Acquisition closing. **An outflow
capitalised to an intangible is not a gain, and it never enters the operating line.** 001's premise
was inverted and `recent-quarter` §4 recorded the refutation; **this artifact re-refutes it at the
segment level, which is the level a business-model artifact could have been misled at, and confirms
no segment's income from operations carries a disposal-gain arc either.** Verdict: **REFUTED, not
"not exhibited."**

---

## 7. DA-25 — CONFIRMED, and quantified at business-model scope

`DA-25` is an issuer-defined per-unit metric that cannot be reproduced from the filed terms. The
metric here is **Starlink Subscriber ARPU**, defined on [📄 sec8 p.36](https://agentii.ai/v/SPCX/sec8/36)
as service revenue from Starlink subscribers over the period divided by **the average number of
Starlink subscribers during the period** — *and the average is never disclosed.* Only period-**end**
subscriber counts are, `As of`, `12.0M` and `6.0M`.

**The coarsest possible reproduction fails by a measurable margin, and the margin is informative.**
Taking the two disclosed series a reader would naturally pair:

```
Connectivity revenue growth     +65.8%
Starlink subscriber growth     +101.2%
implied ARPU change  1.658 / 2.012  =  0.8241  ->  -17.6%
DISCLOSED ARPU change                          ->  -22.4%
WEDGE                                            4.8 pp
```

**4.8 percentage points.** That wedge is *not* noise; it is the enterprise/government mix, and the
filing supplies the confirming cells. Connectivity splits:

| | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Consumer | 2,485 | 1,721 | **+44.4%** |
| Enterprise & Government | 1,806 | 867 | **+108.3%** |
| **Connectivity** | **4,291** | **2,588** | **+65.8%** |

([📄 sec8 p.13](https://agentii.ai/v/SPCX/sec8/13) Table 17; the `$939M` vs `$764M` contribution
split is on [📄 sec8 p.43](https://agentii.ai/v/SPCX/sec8/43).) **And the ARPU definition explicitly
excludes enterprise and government customers** — *"does not include managed enterprise and
government customers with contracts in domains including aviation, maritime, land"*
([📄 sec8 p.35](https://agentii.ai/v/SPCX/sec8/35)).

**Verdict: DA-25 CONFIRMED, and this is the mechanism.** *The metric's own definition excludes the
customer class that is growing at `+108.3%`, while including only the class growing at `+44.4%`.*
ARPU falls `−22.4%` **because the mix is shifting toward a class the metric does not count.** The
`−22.4%` is therefore not price erosion, not churn, and not a normalisation artefact in the
usual sense — it is a **boundary effect inside the per-unit metric**, and it is the same species of
defect as PIL-6's, one level down. `operational-kpi` and `recent-quarter` both flagged DA-25 as
CONFIRMED; this artifact supplies the magnitude and the mechanism, which neither had.

---

## 8. DA-26 — NOT TESTABLE

DA-26 is a twelve-month value served under a quarterly label. **There is no annual row anywhere in
the served corpus for this accession** — it is an interim filing and no Q4 or FY period exists to
check. **Recorded `unresolved (no test possible)`, NOT `clean`.** An untestable rule reported as
clean is the failure mode the VRT census established (A6: *"`Unexercised` and `Clean` are different
results and must not be reported as the same"*).

**But a sibling period defect IS present at SPCX and it is DA-30-class, not DA-26** — see §12,
instance 2: the instrument serves a **six-month** value under a key that also serves a **three-month**
value for the prior year, on the same concept, with no field distinguishing them.

---

## 9. DA-27 — CONFIRMED on method, benign on outcome; the detector mis-fires

`get_company_fiscal_calendar` returns `fiscal_year_end_month_source: default` for SPCX, and the
periods are synthesised into **FY2027** — i.e. the labels are generated from the calendar rather
than read from the issuer's fiscal calendar. **Method CONFIRMED.**

**Outcome benign:** SPCX is a **Dec-31** filer, so calendar and fiscal coincide and no label is
wrong in this accession. Recorded as confirmed-on-method / benign-on-outcome, which is the same
disposition `recent-quarter` §7 reached.

**And the register's detector mis-fires here — a THIRD issuer.** The DA-27 detector is keyed on
`source == "default"`; **SPCX's source field is `gold_companies`, not `default`**, so a detector
looking for the literal string would report SPCX clean while the synthesised labels are demonstrably
present. MRCY and FLY were the first two. **The detector must key on the synthesised-vs-filed
distinction, not on the string.**

---

## 10. DA-28 — CONFIRMED as an open exposure, and the unprinted term is found

**CONFIRMED as exposure.** Seven disagreeing share counts on three axes across three dates, no basis
label: `5,864M` (Q2 2026 weighted average, [📄 sec8 p.5](https://agentii.ai/v/SPCX/sec8/5)),
`4,879M` (H1 2026 weighted average, same page), `2,929M` (Q2 2025), `2,902M` (H1 2025), `638.9M`
Class A issued at the IPO, plus post-split and pre-split bases across a five-for-one split, a
preferred conversion (`$37,475M`, equity statement) and a repurchase (`$(2,413)M`). The specific
split-basis mechanism is **NOT demonstrated** — 001's `recent-quarter` reached the same conclusion and
this artifact does not upgrade it.

**What this artifact adds is the term the register lacked: a $671M deduction that is printed on NO
line.**

```
Six months ended June 30, 2026:
  Net loss                                   $ (4,817)
  Net loss attributable to shareholders      $ (5,488)
  DIFFERENCE                                 $    671   <- printed nowhere
Three months ended June 30, 2026:
  Net loss                                   $   (541)
  Net loss attributable to shareholders      $   (541)
  DIFFERENCE                                 $      -   <- none in the quarter
```

Both cells are on the statement face ([📄 sec8 p.5](https://agentii.ai/v/SPCX/sec8/5)). **There is no
"net income attributable to noncontrolling interests" line, and no other reconciling line.** `us-gaap:ProfitLoss`
— the concept that would carry a pre-NCI total — **returns ZERO facts on this accession.** So the
`$671M` bridge between two printed numbers has **no printed term**, and per DA-29 that is a
back-solve-shaped residual: **this artifact records it and REFUSES to derive it.** It is H1-only, and
therefore **Q1-2026-only**, i.e. **pre-IPO-only** (`4,817 − 541 = 4,276` vs `5,488 − 541 = 4,947` for
Q1). A pre-IPO-quarter deduction attributed to common shareholders, associated with the Class C
reclassification on [📄 sec8 p.22](https://agentii.ai/v/SPCX/sec8/22) and the merger-related preferred
conversion, is the shape — **but the shape is not the term, and the term is not filed.** Recorded as
a DA-28 sub-mechanism candidate (**S-1**): *the capital-structure discontinuity produced a deduction
that the issuer printed as an unexplained delta between two adjacent lines.*

**The consequence binds this thesis directly: the EPS denominator is struck on `$(5,488)M`, not on
`$(4,817)M`.** `5,488 / 4,879 = $1.1248` → `$(1.12)` ✓ and `4,817 / 4,879 = $0.987` → `$(0.99)` ✗. The
filed `$(1.12)` proves which net loss the per-share figure uses. **Any artifact quoting "SPCX's H1
2026 net loss" without naming the basis carries a 13.9% error bar.**

---

## 11. DA-29 — applied to the platform's own instrument

DA-29's mechanical test: *if any term in a reconciliation appears nowhere in the source, the check is
a back-solve, and a back-solve closes exactly so it cannot be caught on the closure — it must be
caught on the terms.*

**11.1 — This artifact PASSES.** §5.2's four identities (8 frames) name every term, all printed.
§5.4's cash-flow bridge names all fourteen terms, all printed on one page, closure exact. §5.4's
non-GAAP bridge names all nine terms, all printed, closure exact. §7's ARPU wedge names both terms
and prints the residual rather than absorbing it. **No term in this artifact is a back-solve, no
`computed` is cited as a derivation, and every `reported` is reconciled to a statement face.**

**11.2 — The instrument FAILS on two counts.**

*(a) `computed` is not reproducible from the instrument's own tree.*
`NetCashProvidedByUsedInOperatingActivities` `computed = 6,010,000,000` against a filed `3,466`. The
platform's own returned arcs, applied to the platform's own served facts, do not produce `6,010`.
**A value that cannot be derived from the instrument that emits it is not a derivation**, and the
contract's DA-29 corollary says so in terms.

*(b) The tree's weights disagree with the statement face on at least five arcs.* Two of them are the
**loss-captioned** items, both carried at **weight −1** where the filing **adds** both
(`Unrealized (gain) loss on digital assets` `539`; `Loss on debt extinguishment` `1,545`). And the
error is **self-consistent** — the stored sign and the tree weight agree with each other and both
disagree with the filing — **so no check that only tests internal consistency can see it.** That is
DA-29's own failure mode, exhibited by the instrument, on the statement that carries this thesis's
non-GAAP headline.

**11.3 — Two `computed` values REFUSED as derivations.** `NetIncomeLossAvailableToCommonStockholdersBasic`
`computed = 4,146,000,000` for Q2 2026: **the residual `3,605,000,000` is located nowhere in the
filing.** And `IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` `computed = -60,000,000` against
a filed `(518)`. Both are recorded as **back-solve-shaped residuals, refused, `UNRESOLVED`** — not
explained, not used, not propagated.

**11.4 — `UNVALIDATED-BY-PLATFORM`, reported as its own class and NOT as a pass.** Twelve concepts
carry arcs in this accession's calculation tree and return **zero** rows from `validate_calculation`,
while being **filed**: `LiabilitiesAndStockholdersEquity`, `StockholdersEquity`,
`PrepaidExpenseAndOtherAssetsCurrent`, `LeaseCost`, `spcx_FinanceLeaseExpense`,
`spcx_OperatingLeaseCostTotal`, `LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities`,
`DebtInstrumentCarryingAmount`, `UnrecordedUnconditionalPurchaseObligationBalanceSheetAmount`,
`AssetsFairValueDisclosure`, `TemporaryEquityCarryingAmountAttributableToParent`,
`CommitmentsAndContingencies`. **Zero rows is not a pass.** Instrument totals for this accession:
**`pass_count 9, warn_count 2, fail_count 18`** — and §5.3 shows two of the 9 passes are wrong.

---

## 12. DA-30 — six instances, and two sit on the figures this artifact exists to settle

DA-30 is a basis the platform collapses before an artifact sees it; the artifact must **name** the
basis **and state where it was established**, and this is *prior* to `no_single_basis_collapse`.

| # | Concept | Basis A | Basis B | Spread | Where the basis is established |
|---|---|---|---|---|---|
| 1 | **`12.3% of revenue`** | Space segment ÷ consolidated = **12.31%** | Launch Services ÷ ex-AI = **12.34%** | both round to the quoted string | §1.5 — the quoted figure does not state its basis and cannot be disambiguated from its text |
| 2 | **`NetIncomeLoss` (key `2026-06-30`)** | **`4,817` = SIX months** (H1 2026) | **`1,008` = THREE months** (Q2 2025, same key) | **8.9× on the same key across periods** | §10 / [📄 sec8 p.5](https://agentii.ai/v/SPCX/sec8/5) — one key serves H1 for one period and Q2 for the other |
| 3 | **Net loss, H1 2026** | `NetIncomeLoss` = **4,817** | `NetIncomeLossAvailableToCommonStockholdersBasic`/`Diluted` = **5,488** | **671 (13.9%)** | §10 — both printed on p.5; `ProfitLoss` = 0 facts, so no reconciling concept exists |
| 4 | **`us-gaap:Assets`** | true total assets `192,770` / `92,079` | served `reported` = **25,124** = the Dec-31-2025 cash-and-restricted-cash subtotal | **7.7×** | [📄 sec8 p.12](https://agentii.ai/v/SPCX/sec8/12) Table 15 — `24,747 + 182 + 195 = 25,124` |
| 5 | **`CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents`** | correct for Dec-31-2025 = **25,124** | served `reported` = **11,501** = the Dec-31-**2024** opening balance | **one year** | [📄 sec8 p.9](https://agentii.ai/v/SPCX/sec8/9) — `beginning of the period | 25124 | 11501`; the instrument served the 2025 column for a 2026 balance |
| 6 | **Starlink subscribers** | `As of` period-**end** `12.0M` → implies **+100.0%** | disclosed growth **+101.2%**, requiring an **undisclosed average** | **1.2 pp** | §7 / [📄 sec8 p.36](https://agentii.ai/v/SPCX/sec8/36) — the ARPU denominator is an average that is never disclosed |

**Instances 1 and 2 are the two this artifact exists to settle**, and instance 1 is the PIL-6
figure while instance 2 governs every net-loss quote. **Instance 4 and 5 are a matched pair and the
sharpest single exhibit:** the same number (`25,124`) is filed under **two** concepts — as an
*opening* balance under the cash concept and as a *subtotal* under the cash-and-restricted-cash
concept — and the instrument assigned it to the wrong one while serving a **different year's** value
under the right one. It is DA-30 and DA-23 and a period error at once, on the balance sheet.

**Instance 6 is the mechanism behind §7's DA-25**, and naming it here is what converts the ARPU
finding from an assertion into a basis statement.

---

## 13. The register is incomplete at business-model scope

Two hazards this artifact tested have **no registered DA**:

- **C-1 — common-control recasting across a change of reporting entity** (§2.4). DA-21 covers
  management-drawn *segment* boundaries and DA-28 covers *capital-structure* discontinuity; neither
  covers a comparative restated to a different **legal perimeter**. Measured cost here: 34.3 points on
  a reported growth rate, 48.7% of a quarter's growth contribution, 6.0 points on the flagship share.
- **C-5 — a filed line with a comparative and no current-period value.** *"Investments in
  unconsolidated affiliates | — | (86)"* appears on [📄 sec8 p.9](https://agentii.ai/v/SPCX/sec8/9)
  with the **current period blank** and H1 2025 at `(86)`. `PaymentsToAcquireEquityMethodInvestments`
  is `null` for H1 2026 against `86,000,000` for H1 2025. **This is how DA-31 (cross-holding) is
  REFUTED at SPCX: the line exists, the activity stopped, and there is no equity-method stake whose
  mark reaches earnings.** The MSFT mechanism — a dilution gain recognised as a stake FELL, HLBV,
  3.71% of net income — **is absent here.** What SPCX has instead is a different non-operating
  contamination, quantified in §13.1. Recorded as a register candidate: *a departing line* is a
  distinct object from *a changed basis*, and no DA names it.

### 13.1 The contamination SPCX does have — and it is not the cross-holding one

```
Unrealized (gain) loss on digital assets      539      (H1 2026)
Loss on debt extinguishment                 1,545      (H1 2026)
                                           ------
                                            2,084   =  106.2% of  Other income (expense), net  (1,962)
```

Both are printed cells on [📄 sec8 p.9](https://agentii.ai/v/SPCX/sec8/9); the `(1,962)` is a printed
cell on [📄 sec8 p.5](https://agentii.ai/v/SPCX/sec8/5); and the attribution is the filing's own:
*"primarily due to the loss on extinguishment of debt and unrealized loss on digital assets"*
([📄 sec8 p.41](https://agentii.ai/v/SPCX/sec8/41)). **106.2% means the residual FX component is
negative (a small gain), which is consistent with the `(42)` exchange-rate line on the cash-flow
face — but `1,962 − 2,084 = (122)` is NOT a located term, so this artifact states the 106.2% and
REFUSES to decompose the residual further (DA-29).**

**Both items are added back in full in the non-GAAP bridge of §5.4, which is the whole of the
`$9,482M` gap between a `$(4,817)M` GAAP net loss and a `+$4,665M` Adjusted EBITDA.** The
`$1,545M` extinguishment loss is a financing-structure event, not an operating one, and adding it
back is conventional. **The `$539M` is a mark on a balance-sheet asset and its add-back means the
non-GAAP headline excludes the change in value of a holding** — which is the *shape* of the MSFT
cross-holding adjustment even though the *mechanism* (equity-method stake, HLBV, dilution gain) is
absent. **Worth flagging for the register: MSFT's is a gain recognised as a stake FELL; SPCX's is a
loss recognised as an asset fell. Opposite signs, same structural position in the bridge.**

---

## 14. Corrections to 001

001 is frozen. Corrections are recorded here.

**14.1 — The `—` in the AI H1 2025 column is false, and it is the PIL-6 evasion.** 001's revenue table
reads `| AI (Grok, X, compute) | $2,561M | 32.8% | $3,379M | — | — |`. **The filing prints AI H1 2025
revenue as `$1,465M`** ([📄 sec8 p.44](https://agentii.ai/v/SPCX/sec8/44) Table 56:
`2,561 | 737 | 247.5% | 3,379 | 1,465 | 130.6%`; and independently on
[📄 sec8 p.13](https://agentii.ai/v/SPCX/sec8/13) Table 17 as the `AI` axis). The cell is not
unavailable. **It is simultaneously a factual error and a classification evasion**: 001's own
prose on the facing line says *"H1 2025 predates the xAI merger, so the AI column is absent"* — which
is the correct *instinct* arrived at by the wrong route, because the column is present and that
presence is the *evidence* of the recast. **The `—` concealed the very signature §2.1 had to be
constructed to find.**

**14.2 — `12.3% of revenue` is Space ÷ consolidated, and it is three things at once.** It is not
"launch" (launch-only is **8.29%**); the denominator is entity-boundary contaminated (ex-AI
**18.31%** Q2 / **17.32%** H1); and the sentence juxtaposes a Q2 share against H1 growth rates.
**Direction survives every basis; level survives none.** §1.

**14.3 — `+$1,824M` is not evidence of migration.** It is **48.7%** of the quarter's revenue growth
and it exists because an entity was acquired. §2.3.

**14.4 — The AI operating line is never stated as a number in 001's later artifacts, while the
earlier one has it.** 001's `2310_business-model` and `2310_operational-kpi` print *"not disclosed"*;
001's `1239_operational-kpi` prints `$(1,257)M`. **The number is filed four times** — pp.30, 44, 45
and 46 — and the earlier artifact was right. `operational-kpi` §7.1 established this; **this artifact
re-confirms it from the four cells and adds that the H1 direction is the OPPOSITE of the Q2
direction on the same line:** Q2 *"decreased by $267 million, or 17.5%"* against H1 *"increased by
$1,266 million, or 51.5%"* ([📄 sec8 p.45](https://agentii.ai/v/SPCX/sec8/45)). **001's `−17.5%
narrowing` is a Q2 figure presented without its period and without its H1 reversal.**

**14.5 — `65.8%` is two different quantities, and so is `−56.3%`.** `65.8%` is Connectivity's Q2
**revenue growth** ([📄 sec8 p.43](https://agentii.ai/v/SPCX/sec8/43)) *and* Space's Q2 **gross
margin** (`(962 − 329) / 962 = 65.80%`). 001 uses both, in different artifacts, without
disambiguation. Separately, **001's "−56.3% after R&D" is the operating margin including SG&A**
(`(962 − 1,504) / 962 = −56.34%`); **after R&D alone it is `−46.05%`** (`(962 − 329 − 1,076) / 962`).
**Both are Q2 figures and both are correct as calculations — the labels are wrong.**

**14.6 — `So 1.4 GW is an IT load, not a facility load` is not the filing's statement.** The filing
defines it as GPU count × GPU all-in draw and excludes cooling, distribution losses, lighting,
security and facility overhead ([📄 sec8 p.36](https://agentii.ai/v/SPCX/sec8/36)). **GPU nameplate ⊂
IT load ⊂ facility draw**, so treating it as IT load **understates** the gap and any PUE computed
against it **overstates** the PUE. `operational-kpi` §3.1 recorded this correction; **this artifact
adds that the distinction is what makes PIL-4's falsifier outcome basis-dependent** — `2.00 > 1.5`
fires and `1.50 = 1.5` does not, on the same metric, because the two readings put different
quantities in the numerator.

**14.7 — 001 mislabels DA-19 as "common-control mergers."** `2310_business-model` carries
`da_id: "DA-19"`, `chosen_reading: "common-control mergers (xAI, X) treated as a change of reporting
entity"`. **No DA-19 in the register covers common-control mergers** — the hazard is unregistered,
which is precisely C-1. 001 reached the right *conclusion* under a *definition that does not exist*,
and the register gap outlived it into this thesis. §2.4.

**14.8 — 001 quoted the 1.4 GW segment-less in five of its twelve locations**, including every
rendered-report location except one stat tile. The filing puts it under the `AI` heading. §3.1.

---

## Carry-forwards

1. **C-1 (highest value).** Register **common-control recasting across a change of reporting entity**
   as a DA. The detector is mechanical and needs no filing: *for each issuer, find a segment whose
   comparative-period revenue exceeds the entity's revenue in the period before the segment's legal
   parent was consolidated.* SPCX's signature is `AI H1 2025 = 1,465` against an xAI merger date of
   2026-02-02, with **no recast sentence anywhere**. Re-run across the 35-name universe; the 23
   issuers DA-26 already flagged are the natural first pass.
2. **C-2.** **`validate_calculation`'s `pass` must not be used as a sign attestation.** §5.3 shows two
   `pass` verdicts with `diff == 0` on sign-stripped magnitudes. Any consumer filtering on
   `status == pass` receives wrong-signed values. Recommend the register carry this as a DA-23
   corollary and the census vocabulary distinguish `pass-that-certifies-a-sign` from `pass-vacuous`.
3. **C-3.** **The `OperatingIncomeLoss` substitution must be re-tested universe-wide on the
   line-level detector**, not the total. SPCX is the SILENT regime with **zero unallocated items**,
   which is the regime where every total ties and the defect is invisible at the total — the same
   condition NVDA §3b identified. §3.2 shows it is a **different segment each period**, so no
   per-issuer patch exists; the test must be per-period and per-fact.
4. **C-4.** **Cursor/Anysphere is unmodelled and is in scope under P11.** ~$60B implied equity value,
   all-stock, expected close Q3 2026 ([📄 sec8 p.34](https://agentii.ai/v/SPCX/sec8/34)). No figure in
   this artifact includes it. SPCX is the acquirer, so P11's *"if the acquirer is the thesis"* bullet
   binds: the combined entity, the dilution and the close date as dated catalyst.
5. **C-5.** Register **the departing line** — a filed line with a comparative and a blank current
   period — as distinct from a changed basis. SPCX's *"Investments in unconsolidated affiliates | — |
   (86)"* is one, and it is what refutes DA-31 here.
6. **C-6.** **Re-run the DA-30 census with "two printed values on adjacent lines with no reconciling
   concept" as the detector.** That is how §10's `$671M` was found, and it found it because
   `ProfitLoss` returns zero facts — i.e. the detector is *the absence of the concept that should
   bridge two printed cells.*

## Could not be verified

1. **`sec7` (the same-day earnings 8-K) was not read by this artifact**, and is not cited. The two
   sibling SPCX artifacts have extracted its segment tables and its per-period launch series. **The
   8-K's `10 customer / 28 internal / 38 total` basis differs from the 10-Q's `37 Falcon + 1
   Starship` presentation**, and reconciling the two is `unit-economics` §2's task, not this one's.
2. **`get_segment_data(SPCX)` returns `INTERNAL_ERROR: column "k" does not exist`** on this
   accession, reproducibly. It is the platform's only segment-attribution surface, so **no
   segment-attribution claim in this artifact is sourced from it.** §3.2's findings come from the
   calculation linkbase and the served facts instead.
3. **The `spcx:*` extension concept set is unenumerable with the permitted tools.**
   `list_xbrl_concepts` does not index extension concepts — proved by positive control, since
   `search="FinanceLeaseExpense"` returns zero while `spcx:FinanceLeaseExpense` is in this
   accession's calculation tree. **Therefore "the 1.4 GW is absent from the fact layer" is NOT
   asserted**; the assertion is that it is absent from every surface it can be located on, which is
   weaker and is the honest form. Frontmatter records `UNRESOLVABLE-FROM-PLATFORM`.
4. **The `$671M` (§10) is not decomposed.** `ProfitLoss` returns zero facts and no reconciling line
   is printed. The Q1-only, pre-IPO-only location is arithmetic; the cause is not filed. **Refused as
   a derivation (DA-29), not explained.**
5. **The `(122)` residual in §13.1 is not decomposed**, for the same reason.
6. **`IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` `computed = -60,000,000`** against a
   filed `(518)` and `NetIncomeLossAvailableToCommonStockholdersBasic` `computed = 4,146,000,000`
   with a residual of `3,605,000,000` are **both unexplained.** Their residuals are located nowhere in
   the filing. Refused as derivations.
7. **PUE-proper is not computed here** and is carried as `UNRESOLVABLE-FROM-PUBLIC-SOURCES` in a
   separate frontmatter key. The same-period facility-side comparator that makes the restatement
   possible was read by `operational-kpi`, not by this artifact, and **no term of that restatement is
   reproduced here** — DA-29 forbids naming a term whose source I did not locate.
8. **The printed-footer offset was measured on the pages read (+4: p.36 prints "35") and is NOT
   corrected anywhere in this artifact.** A right citation "corrected" into a wrong one is worse than
   no citation.
9. **`search_keyword_in_source` is unreliable in BOTH directions and was not used as evidence of
   absence anywhere here.** The zero case is the standing rule. This artifact supplies the
   **nonzero** case as a positive-direction demonstration: on this accession the phrase
   `equity method` returns **one hit, on p.12**, and p.12 does **not** contain equity-method text —
   the index matches the platform's LLM-generated `description` field, not the page. **Both
   directions of the tool's output are therefore inadmissible as evidence about a page's contents,
   and every absence claim in this artifact rests on a page that was READ.**
