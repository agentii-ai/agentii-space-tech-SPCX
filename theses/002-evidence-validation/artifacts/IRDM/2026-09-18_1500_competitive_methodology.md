---
# 002 / Phase 5 / T102–T104 — pillar PIL-7 (falsifier reachability), ticker IRDM.
# ONE artifact, one job: classify the PIL-6 falsifier against the disposition classes,
# separating PLATFORM-BLOCKED from SOURCE-BLOCKED, with a NAMED resolving source each,
# and flag the falsifier whose passing result cannot be recorded at all (PIL-2).
#
# Written at 1.5.0, not grandfathered: the register gained DA-29 (defective checks) and
# DA-30 (a basis collapsed before an artifact sees it) at 002 Phase 3, and both are
# load-bearing here (§4's tie-out and §3's non-coterminous benchmark). §4 and §8 discharge
# those two obligations.
#
# skill_pin = 826995c722a4, one of the six pins tabled in
# theses/001-technology-baseline/reproduce.md. packaging/targets/{claude-code,codex,
# generic-cli,cowork} hold DECOY copies of every skill and all fail the six known hashes —
# they are not the pin source. The pin is written, not UNRESOLVED.
constitution_pin: "1.5.0"
thesis_id: "002-evidence-validation"
pillar: PIL-7
ticker: IRDM
skill: competitive
mode: methodology
skill_pin: "826995c722a4"
upstream_stale: "001@1.2.0"
as_of: 2026-09-18
assumption_pin: "2"
corpus_version: "UNPINNED"
generated_at: 2026-09-18T15:00:00Z

# P11. IRDM is a deal security on the transaction fact. Both filings read here are
# PRE-CLOSE on two different transactions at once:
#   (a) the Rocket Lab merger — PENDING at 2026-06-30 (sec191 p.23 lists "our ability to
#       complete the Transaction on the anticipated timeline or at all" and the parties'
#       termination rights under the Merger Agreement as live uncertainties);
#   (b) the Aireon step acquisition — agreement 2026-05-13, CONSUMMATED 2026-07-02
#       (sec191 p.20), i.e. after the 2026-06-30 period end.
# No gain is recognised on either, and nothing has been consolidated. The standalone
# pre-merger basis is the only admissible one.
deal_security_basis: standalone_pre_merger

# The flag records the DISPOSITION OF THE IN-SCOPE FALSIFIER (PIL-6), not a failure of
# this artifact's classification. PIL-7's own wrong_if is satisfied: 6 falsifiers in 001,
# 1 in scope here, 1 classified, 1 with a named resolving source (§2). PIL-6 is the
# register's canonical UNRESOLVABLE-FROM-PLATFORM case and this artifact confirms it at IRDM.
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM

evidence_grade: DEMONSTRATED

definitions_used:
  - da_id: DA-23
    chosen_reading: >
      Sign stripping is detectable ONLY on BIDIRECTIONAL concepts (A17). A clearance is
      admissible only if SCOPED to them AND it EXHIBITS a negative-filed instance;
      otherwise it is UNEXERCISED, not clean. Applied here to the equity-method line that
      carries IRDM's only competitively-relevant stake (§8).
  - da_id: DA-25
    chosen_reading: >
      Issuer-defined per-unit metrics (billable subscribers, ARPU) are MD&A PROSE and never
      XBRL-tagged, so a zero from a structured query on them is a zero BY CONSTRUCTION.
      Sharpened here from a fact-query zero to a CONCEPT-REGISTRY zero (§6).
  - da_id: DA-28
    chosen_reading: >
      A capital-structure basis discontinuity across a close date. The Aireon close adds
      ~$438.1M of debt after the last reported balance sheet (§7); the pre-close competitive
      benchmark is not the post-close entity's.
  - da_id: DA-29
    chosen_reading: >
      A reconciliation must name the source of EVERY term, and every term must appear in the
      source — a back-solve closes exactly and cannot be caught on the closure. §4 names the
      page and the filed cells for every term of the tie-out it presents; no term is
      reconstructed.
  - da_id: DA-30
    chosen_reading: >
      A concept the issuer reports on more than one basis must have its basis NAMED and the
      place the basis was established stated. §3's relative-size benchmark spans two
      non-coterminous fiscal years and three heterogeneous revenue bases and says so.
    # NOTE: DA-31 (cross-holding / valuation circularity) is directly implicated by the
    # Aireon stake but is a PROPOSED register entry (AMENDMENTS-PENDING A1), not yet
    # registered, so it is named in §7 prose and deliberately NOT declared here. Declaring
    # an unregistered id would be a fabricated definition reference.

citations:
  - figure: "Competition: 'our principal mobile satellite services competitors are Viasat, Globalstar, ORBCOMM, and Thuraya Telecommunications Co. (Thuraya)'; 'In September 2025, SpaceX signed an agreement to acquire certain rights and licenses to an aggregate of 50MHz of S-band spectrum'; R&D $19.8M/$28.4M/$20.3M"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 27
    url: https://agentii.ai/v/IRDM/sec151/27
    located_via: search_keyword_in_source
  - figure: "'We hold licenses to use up to 8.725 MHz of contiguous spectrum in the L-band (1617.775-1626.0 GHz)'; 200 MHz K-Band (23 GHz); 400 MHz Ka-Band (19.4-19.6 / 29.1-29.3 GHz); AIS 156.0125-162.0375 MHz; ADS-B 1087.7-1092.3 MHz; ITU Master International Frequency Register; 'Filings to the ITU are made on our behalf by the United States'; country codes 8816 and 8817; 25-year de-orbit standard"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 26
    url: https://agentii.ai/v/IRDM/sec151/26
    located_via: read_source_pages
  - figure: "'VSAT services providers, such as Eutelsat Communications S.A. (Eutelsat) and SES S.A.'; 'Newer entrants' primary offerings, such as Starlink broadband from Space Exploration Technology Corp. (SpaceX) and Eutelsat's OneWeb Holdings Limited'; 'utilizing spectrum purchased from EchoStar in 2025'; '66 operational satellites'"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 9
    url: https://agentii.ai/v/IRDM/sec151/9
    located_via: read_source_pages
  - figure: "'2,537,000 billable subscribers' at 12/31/2025, +3%; 'Total revenue increased from $830.7 million in 2024 to $871.7 million in 2025, representing a 5% increase'; 'Satellite based L- and S-band frequencies were fully allocated by the International Telecommunications Union (ITU) in the early 1990s'"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 8
    url: https://agentii.ai/v/IRDM/sec151/8
    located_via: read_source_pages
  - figure: "'the FCC granted a waiver in 2020 to Ligado Networks ... includes a 10 MHz band close to the spectrum that we use for all of our services'; 'These petitions remain pending'; Jan 2025 Chapter 11 and 'an agreement to lease and potentially transfer its satellites, ground assets and L-band spectrum to AST SpaceMobile, Inc'"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 40
    url: https://agentii.ai/v/IRDM/sec151/40
    located_via: read_source_pages
  - figure: "2,537,000 billable subscribers, 'an increase of 77,000, or 3%', from approximately 2,460,000; 'Service revenue represented 73% and 74% of total revenue'; hosted payload revenue 'principally from Aireon'; SpaceX 'recently announced plans to acquire a significant amount of spectrum enabling global D2D services'"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 50
    url: https://agentii.ai/v/IRDM/sec151/50
    located_via: read_source_pages
  - figure: "Commercial Service Revenue table cells — Voice and data 232.2/402/$47 vs 226.1/415/$46; IoT data 181.4/1,998/$7.78 vs 166.2/1,887/$7.70; Broadband 50.7/16.1/$259 vs 56.1/16.6/$282; Hosted payload and other data 61.6 vs 60.2; Total commercial services 525.9/2,416 vs 508.6/2,319, Change 17.3/97. Government service revenue table cells — 108.0/121 vs 106.3/141, Change 1.7/(20). EMSS 'fixed at $110.5 million per year', expires September 2026"
    ticker: IRDM
    form_type: 10-K
    citation_id: sec151
    page_no: 53
    url: https://agentii.ai/v/IRDM/sec151/53
    located_via: read_source_pages
  - figure: "Intangible assets table cells: 'Spectrum and licenses', useful life Indefinite, gross carrying value 14030, accumulated amortization —, net carrying value 14030 at BOTH June 30, 2026 and December 31, 2025; total intangible assets 109251 / (26,585) / 82666"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 11
    url: https://agentii.ai/v/IRDM/sec191/11
    located_via: search_keyword_in_source
  - figure: "Aireon: '$50.0 million in exchange for an approximate 6% preferred membership interest'; carrying value 'was $36.3 million and $38.5 million as of June 30, 2026 and December 31, 2025'; 'fully diluted ownership stake ... was approximately 39.5%'; agreement 'On May 13, 2026 ... which was consummated on July 2, 2026'; hosting fees $200.0M of which $134.5M paid; power/data fees ~$23.5M per year; $2.3M and $5.9M recognised in the quarter"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 18
    url: https://agentii.ai/v/IRDM/sec191/18
    located_via: read_source_pages
  - figure: "Subsequent Events: 'completed its previously announced acquisition of the remaining 60.5% of equity interests in Aireon Holdings'; 'approximately $366.7 million', 50% cash and 50% deferred as a seller loan; 'drew down $100.0 million on its Revolving Facility'; '$183.4 million one-year, non-interest-bearing loan from the sellers'; Aireon's existing term loans 'had an outstanding balance of $154.7 million at the closing date'"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 20
    url: https://agentii.ai/v/IRDM/sec191/20
    located_via: read_source_pages
  - figure: "'approximately 2,627,000 billable subscribers worldwide, an increase of 144,000, or 6%, from approximately 2,483,000' at June 30, 2026; 'architecture of 66 operational satellites with in-orbit spares'; Aireon acquisition description"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 21
    url: https://agentii.ai/v/IRDM/sec191/21
    located_via: search_keyword_in_source
  - figure: "Material Trends and Uncertainties: 'increased competition or potential competition from other satellite service providers, including SpaceX following its announced plans to acquire a significant amount of spectrum enabling global direct-to-device (D2D) services'; 'our ability to complete the Transaction on the anticipated timeline or at all'; 'the right of one or both of Rocket Lab or us to terminate the Merger Agreement'"
    ticker: IRDM
    form_type: 10-Q
    citation_id: sec191
    page_no: 23
    url: https://agentii.ai/v/IRDM/sec191/23
    located_via: search_keyword_in_source
  - figure: "Comparator-side detector: 'Our largest global competitors are Viasat, Iridium and ORBCOMM'; 'Our principal regional MSS competitor in the Middle East and Africa is Thuraya'; 'aperture terminal companies, such as Hughes and Gilat Satellite Networks'; 'SpaceX's Starlink, Amazon Leo and AST SpaceMobile'; 'Anterix, Nextwave and TerraStar'"
    ticker: GSAT
    form_type: 10-K
    citation_id: sec128
    page_no: 10
    url: https://agentii.ai/v/GSAT/sec128/10
    located_via: search_keyword_in_source
  - figure: "Comparator-side excluder: 'recent terrestrial spectrum sales, such as between EchoStar and SpaceX and EchoStar and AT&T'; 'significant barriers to entry, including the cost and difficulty associated with obtaining spectrum licenses'"
    ticker: GSAT
    form_type: 10-K
    citation_id: sec128
    page_no: 11
    url: https://agentii.ai/v/GSAT/sec128/11
    located_via: search_keyword_in_source
  - figure: "Comparator-side detector: Iridium named in the aviation competition list ('Amazon Leo, Anuvu, Gogo, Iridium, Panasonic Avionics Corporation, SES, SpaceX and Thales Group') and the government list ('BAE Systems, Collins Aerospace, EchoStar (Hughes Network Systems), Eutelsat, General Dynamics, Iridium, L3Harris, OneWeb, SES, SpaceX, Telesat')"
    ticker: VSAT
    form_type: 10-K
    citation_id: sec183
    page_no: 16
    url: https://agentii.ai/v/VSAT/sec183/16
    located_via: search_keyword_in_source
  - figure: "'Competition — The markets in which we compete are highly competitive and competition is increasing'; competitive factor list includes 'our spectrum and market access'"
    ticker: VSAT
    form_type: 10-K
    citation_id: sec183
    page_no: 15
    url: https://agentii.ai/v/VSAT/sec183/15
    located_via: search_keyword_in_source
---

# IRDM × competitive — PIL-6 falsifier reachability (P6), and the competitor set that is not blocked

**Job.** T102–T104 at IRDM, in `competitive` `methodology` mode. The Skill Deployment
Matrix row is *"Confirms which PIL-6 falsifiers are platform-blocked rather than
source-blocked (P6)."* **The output is a classification, not a narrative.** This artifact
does not re-ask 001's questions; it validates 001's facts and classifies the falsifier
001 attached to them.

**Verdict up front.**

| | |
|---|---|
| **PIL-6 falsifier** | **`UNRESOLVABLE-FROM-PLATFORM`** — public and reachable in principle, **not reachable by this toolchain**. **Kind 5 — ingestion absence of a datum class (regulatory registry).** |
| **Not** | **NOT `UNRESOLVABLE-FROM-PUBLIC-SOURCES`.** Both named sources are public, free and queryable by a human today. Nothing needs to be fetched from a private party. |
| **Named resolving source** | **FCC International Bureau Filing System (IBFS)** and the **ITU Space Network List / Master International Frequency Register**. |
| **Competitor set** | **Partly NOT platform-blocked.** 2 of IRDM's 4 named principal MSS comparators are US-listed SEC filers with full platform reach and were read here. The other 2 are private and foreign. |
| **Third situation** | **PIL-2 is `REACHABLE-BUT-NOT-RECORDABLE`** — flagged, §2.4. Remedy is neither monitoring nor platform reach. |
| **Correction to 001** | **Arithmetic stands**; DA-23 clearance already REFUTED at 002 Phase 5. **New here:** the strip reaches the equity-method line — the line that carries IRDM's only competitively-relevant stake — and 001's Pillar-6 subscription is **proxy-only** (§8). |

---

## 0. Register version note, and the pin

Written at `constitution_pin: "1.5.0"` — not grandfathered. The register gained **DA-29**
(defective checks / back-solves) and **DA-30** (a basis collapsed before an artifact sees
it) at 002 Phase 3, and **both are load-bearing here**: §4 presents a reconciliation and
must name every term, and §3's benchmark spans two fiscal years and three revenue bases.
Both obligations are discharged in full, not by reference.

`skill_pin: "826995c722a4"` is one of the six pins tabled in
`theses/001-technology-baseline/reproduce.md`. It is **written, not `UNRESOLVED`**.
`packaging/targets/{claude-code,codex,generic-cli,cowork}` hold **DECOY** copies of every
skill and all four fail the six known hashes; they are not the pin source.

**One correction to the amendment queue's own text.** `AMENDMENTS-PENDING.md` **A13** is
titled *"THE NOT-TESTABLE TAXONOMY IS NOW FOUR KINDS, NOT TWO"*, but the table beneath that
heading enumerates **SIX** kinds (1 ingestion absence, 2 genuine absence from the source,
3 validator-completeness, 4 mechanism-population identity, 5 ingestion absence of a datum
class, 6 coverage window). The heading is stale; the table is the operative text. The task
brief says "six" and the table agrees. Recorded so the census in A23 is not read as
inconsistent with the taxonomy it cites.

---

## 1. Basis: the entity that this artifact describes

**Every competitive figure below is `standalone_pre_merger`.** State it before any figure,
because two independent transactions move the boundary and **neither has closed inside the
reported periods**:

| Transaction | Status at the periods read | Evidence |
|---|---|---|
| **Rocket Lab merger** | **PENDING.** Termination rights live; management lists completion risk as an uncertainty | [📄 IRDM 10-Q p.23](https://agentii.ai/v/IRDM/sec191/23) |
| **Aireon step acquisition** (remaining 60.5%, ~$366.7M) | Agreement **2026-05-13**; **consummated 2026-07-02** — **after** the 2026-06-30 period end | [📄 IRDM 10-Q p.20](https://agentii.ai/v/IRDM/sec191/20) |

**The interval, stated precisely.** The Q2 2026 reporting period ends **2026-06-30**
(`report_date` of accession `0001418819-26-000045`); the Aireon Closing is **2026-07-02**.
That is **two days**, not four. The briefing note for this task says four. The verified
interval is two, and it does not change the conclusion — the balance sheet at the period
end is **pre-Aireon-consolidation** either way, and Aireon is still carried as an **equity
method** investment at `$36.3 million` (June 30, 2026) against `$38.5 million` at
December 31, 2025, at an **approximately 39.5%** fully diluted stake
([📄 IRDM 10-Q p.18](https://agentii.ai/v/IRDM/sec191/18)). Recorded because the artifact
quotes the date, and a quoted date carries the same obligation as a quoted number.

**Consequence, stated once and carried everywhere.** No competitive conclusion below
describes the entity that exists after 2026-07-02. §7 quantifies why that matters.

---

## 2. The PIL-6 falsifier, decomposed and classified

001's falsifier, verbatim from `theses/001-technology-baseline/spec.md` line 249:

> `metric=new_entrant_primary_spectrum_or_slot_grant_without_incumbent_acquisition threshold=0 source=FCC_IBFS_or_ITU_Space_Network_List op=>`

Pillar 6's own prose supplies the reading: *"if a new entrant secures primary coordination
or a grant in a contested band or shell **without** acquiring it from an incumbent, the
scarcity premise weakens."* The metric is **compound** — one metric name, four separable
predicates. Classifying the sentence whole would hide which predicate carries the block.
So it decomposes:

| # | Predicate | Class | **KIND** | Named resolving source |
|---|---|---|---|---|
| **F6-i** | A **new entrant** obtains a **primary spectrum** grant (FCC grant / ITU coordination priority) in a contested band | `UNRESOLVABLE-FROM-PLATFORM` | **5** — ingestion absence of a DATUM CLASS (regulatory registry) | **FCC IBFS** and **ITU Space Network List / Master International Frequency Register** |
| **F6-ii** | An **orbital slot** grant in a contested shell | `UNRESOLVABLE-FROM-PLATFORM` | **5** — same datum class | **ITU SNL** (orbital location + assignment record); **FCC Part 25** authorisations |
| **F6-iii** | …**without** incumbent acquisition — the excluder clause | `UNRESOLVABLE-FROM-PLATFORM` | **5**, with an **A12 structural component** (§5) | Same registries, **plus** a negative-branch method; the SEC corpus alone is reporter-conditioned |
| **F6-iv** | `threshold=0` — a single instance falsifies | **not a datum question** — a decision rule with a consequence | n/a | Carried from i–iii |

**Why kind 5 and not kind 2.** Kind 2 is *genuine absence from the source*: nothing to
fetch, scope the claim. That is **not** the case here. The FCC IBFS and the ITU SNL both
**exist, are public, and are free**. IRDM's own filing describes the second one and
resolves the query key: *"the ITU maintains a **Master International Frequency Register**
of radio frequency assignments"* and *"**Filings to the ITU are made on our behalf by the
United States**"* ([📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26)). So the ITU
record for IRDM's network is held under the **US administration**, and a competent human
researcher can pull it in an afternoon. **The block is platform reach, and the remedy is a
connector.** Merging this with `UNRESOLVABLE-FROM-PUBLIC-SOURCES` would send the register
to a monitoring task for a source that is already public — the exact error the two
dispositions exist to prevent.

**Why `threshold=0` makes it worse, not easier.** A zero-threshold falsifier is settled by
**one observation**. Combined with F6-iii, that means this falsifier is not merely
untestable here — it is **unclearable**. No quantity of null evidence can discharge it,
because the corpus that supplies the nulls is the corpus that structurally omits the
positive. An artifact that reported "no new-entrant primary grants observed" as a clean
result would be reporting a **sample defined by the mechanism's own property** — A13 kind
4's failure, wearing kind 5's clothes.

### 2.4 The third situation, flagged

The brief requires the unrecordable case be surfaced separately, and it is **not** PIL-6.
**PIL-2's** falsifier names `source=peer_reviewed_literature_or_flown_hardware_disclosure`.
That class is **reachable** and the platform can **read** it, but a passing result **cannot
be recorded**: the level-`fail` citation contract admits only `agentii.ai` URLs. This is
`REACHABLE-BUT-NOT-RECORDABLE` — **A22's third situation** — and its remedy is **neither**
monitoring **nor** platform reach. It is a contract amendment, or replacement of the
falsifier with a recordable predicate. Until then every such falsifier reports as
unresolvable **whether or not it is satisfied** — a systematic bias toward false negatives.
Confirmed instance and resolver: the next **Item 1A refresh (FY2026 Form 10-K)**; the
Q1 2026 leg is closed by incorporation by reference.

---

## 3. The competitor set, and whether it is platform-blocked

The brief asks directly: *is there a competitor set that is NOT platform-blocked?* **Yes —
partially, and the reachable half is the half that matters.**

IRDM names its set in two places, and they are **different lists with different scopes**:

- **Principal MSS competitors** — *"our principal mobile satellite services competitors are
  **Viasat, Globalstar, ORBCOMM, and Thuraya Telecommunications Co. (Thuraya)**"*
  ([📄 IRDM 10-K p.27](https://agentii.ai/v/IRDM/sec151/27)).
- **Adjacent sector and new entrants** — *"VSAT services providers, such as **Eutelsat
  Communications S.A. (Eutelsat)** and **SES S.A.**"*; *"Newer entrants' primary offerings,
  such as Starlink broadband from **Space Exploration Technology Corp. (SpaceX)** and
  **Eutelsat's OneWeb Holdings Limited**"*
  ([📄 IRDM 10-K p.9](https://agentii.ai/v/IRDM/sec151/9)).

| Comparator | Named at | Listing / control | Platform reach | Class |
|---|---|---|---|---|
| **Viasat, Inc.** (`VSAT`) | sec151 p.27 | NASDAQ | **REACHABLE** — read `sec183` FY2026 10-K pp.15–16 | **not blocked** |
| **Globalstar, Inc.** (`GSAT`) | sec151 p.27 | NASDAQ | **REACHABLE** — read `sec128` FY2025 10-K pp.10–11 | **not blocked** (note: GSAT is itself a deal security) |
| **ORBCOMM Inc.** | sec151 p.27 | **Private** — no SEC filings | **NOT REACHABLE** | **Kind 2** — genuine absence from the source. Remedy: none. P6 admits it only as value-chain node / listed proxy / feasibility comparator |
| **Thuraya Telecommunications Co.** | sec151 p.27 — *"a division of UAE-based Space42 PLC"* | **Foreign** (Abu Dhabi-listed parent) | **NOT REACHABLE** | `UNRESOLVABLE-FROM-PLATFORM` — remedy is non-US issuer coverage |
| **Eutelsat Communications S.A.** | sec151 p.9 | Euronext Paris | **NOT REACHABLE** — `search_companies(search="Eutelsat")` returns **0 rows**: no workspace registry entry at all | `UNRESOLVABLE-FROM-PLATFORM` — remedy: add to the universe registry |
| **SES S.A.** | sec151 p.9 | **CIK 0001347408, ticker `SGBAF`** | **NOT REACHABLE** — registry row **exists** with every coverage field null; `search_sec_filings` 0 rows, `search_documents` 0 rows; `entities.md` lists `SGBAF` as `NOT_READY` | `UNRESOLVABLE-FROM-PLATFORM` — **remedy is INSIDE the platform**: ingest CIK 0001347408 |
| **SpaceX / Starlink** | sec151 p.27, p.9 | **Private** | **NOT REACHABLE** | **Kind 2** — P6 admits it only as feasibility comparator |
| **OneWeb Holdings Limited** | sec151 p.9 | Eutelsat subsidiary | **NOT REACHABLE** | Inherits Eutelsat |
| **AST SpaceMobile, Inc.** (`ASTS`) | **sec151 p.40 only** — the Ligado transfer path, **NOT** the p.27 comparator list | NASDAQ | **REACHABLE** — `sec125` FY2025 10-K exists | **not blocked** |

**So the answer is a qualified yes.** **Two of the four named principal comparators —
`VSAT` and `GSAT` — are fully platform-reachable**, and both were read here rather than
assumed. What is blocked is **not the comparator set**: it is (a) two specific private or
foreign issuers, and (b) **the market-share denominator**, which no issuer discloses and
no `us-gaap` concept exists for (§6).

**A precision worth keeping.** `ASTS` is **not** in IRDM's p.27 competitor paragraph. It
enters IRDM's competitive field only through the **regulatory** route at p.40 — Ligado's
Chapter 11 agreement to *"lease and potentially transfer its satellites, ground assets and
L-band spectrum to AST SpaceMobile, Inc"*
([📄 IRDM 10-K p.40](https://agentii.ai/v/IRDM/sec151/40)). Treating ASTS as a named
competitor would be a comparison the issuer did not make. It is a **spectrum counter-party**,
which is the more interesting fact and the reason it appears in §5.

**The evaluable benchmark, with its basis named (DA-30).** Relative size on a
revenue basis, from `search_xbrl_facts` (`RevenueFromContractWithCustomerExcludingAssessedTax`,
`source_authority` 3 = 10-K/20-F): `VSAT` FY2026 **$4,640,280K** (period 2025-04-01 →
2026-03-31); `IRDM` FY2025 **$871,659K** (2025-01-01 → 2025-12-31); `GSAT` FY2025
**$272,986K** (2025-01-01 → 2025-12-31). Ratios: **VSAT ÷ IRDM = 5.32×**;
**IRDM ÷ GSAT = 3.19×**.

**Three basis statements, because this figure has three exposures:**
1. **The periods are not coterminous.** VSAT's fiscal year ends **31 March**; IRDM's and
   GSAT's end **31 December**. The "FY" comparison spans a nine-month offset.
2. **The revenue bases are not comparable businesses.** VSAT's total revenue is not MSS —
   it spans fixed broadband, aviation, maritime and a defence/advanced-technologies
   segment. This is a **relative-size benchmark across heterogeneous revenue bases**, **not**
   a market share and **not** a like-for-like MSS comparison.
3. **It carries no page citation, and is therefore reported at `DERIVED`, not
   `DEMONSTRATED`.** The instrument that served it is `search_xbrl_facts`, which is **not**
   an admissible `located_via` under the contract's four-value enum. Promoting it to
   `DEMONSTRATED` requires reading each issuer's income-statement face, which was not done
   here. Recorded as a limitation rather than dressed with a citation that would not have
   located it.

---

## 4. The proxy test — what *is* computable at IRDM, and its tie-out

A23's rule is that the deliverable is *"not a verdict on reachability, but a means of
testing anyway."* At IRDM the proxy has three legs, and the first two are filed cells.

**Leg 1 — the source is named and its query key is disclosed, by the issuer.**
[📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26) gives the full licence inventory
as prose: **8.725 MHz** of contiguous L-band (1617.775–1626.0 GHz); **200 MHz** of K-Band
(23 GHz) for inter-satellite links; **400 MHz** of Ka-Band (19.4–19.6 GHz and
29.1–29.3 GHz) for feeder links; **156.0125–162.0375 MHz** for AIS reception;
**1087.7–1092.3 MHz** for ADS-B reception; ITU country codes **8816** and **8817**; a
**25-year de-orbit standard** under the FCC authorisation of the current constellation.
This is a licence *inventory*, not a licence *grant record* — it establishes what IRDM
holds, and cannot establish what a new entrant was granted.

**Leg 2 — the scarcity premise, dated, in the issuer's words.** *"Satellite based L- and
S-band frequencies were **fully allocated** by the International Telecommunications Union
(ITU) **in the early 1990s** and are utilized by a limited number of mobile satellite
operators like Iridium"* ([📄 IRDM 10-K p.8](https://agentii.ai/v/IRDM/sec151/8)). This is
the strongest single proxy datum available, and its shape is the point: **the issuer states
that the primary allocation channel for its own bands closed three decades ago.** A
falsifier whose positive branch requires a *primary* grant in those bands is one the
subject of the test asserts to be impossible. That is a **CLAIMED**-grade issuer
assertion, admissible as corroboration — not as the test.

**Leg 3 — the asset-class carrier, and it is flat.** The PIL-6 proxy A23 names second is
"impairment by asset class". The indefinite-life **"Spectrum and licenses"** intangible is
carried at gross **$14,030K**, no accumulated amortization, net **$14,030K**, **identical
at June 30, 2026 and December 31, 2025**
([📄 IRDM 10-Q p.11](https://agentii.ai/v/IRDM/sec191/11)). Against FY2025 revenue of
$871,659K that is **1.6%** of revenue, **unimpaired and unchanged** over six months. So the
asset-class test returns **no impairment signal in either direction** — it neither
corroborates a new-entrant threat nor a scarcity rent.

**The tie-out (DA-29).** Every term below is a filed cell, and the page is named; no term is
reconstructed and none is a back-solve. From the **Commercial Service Revenue** and
**Government Service Revenue** tables
([📄 IRDM 10-K p.53](https://agentii.ai/v/IRDM/sec151/53)), quoted as cells:

| Test | Filed cells | Arithmetic | Filed total | Result |
|---|---|---|---|---|
| Commercial services, FY2025 | 232.2 + 181.4 + 50.7 + 61.6 | **525.9** | `525.9` | **exact** ✓ |
| Commercial services, FY2024 | 226.1 + 166.2 + 56.1 + 60.2 | **508.6** | `508.6` | **exact** ✓ |
| Commercial subscribers, FY2025 | 402 + 1,998 + 16.1 | **2,416.1** | `2,416` | ✓ (rounding) |
| Commercial subscribers, FY2024 | 415 + 1,887 + 16.6 | **2,318.6** | `2,319` | ✓ (rounding) |
| **Cross-page, to p.8** | 2,416 + 121 (government) | **2,537** | p.8: `2,537,000` | **exact** ✓ |
| **Cross-page, to p.50** | 2,319 + 141 (government) | **2,460** | p.50: `~2,460,000` | **exact** ✓ |
| **Cross-page, the change** | 2,537 − 2,460 | **77** | p.50: `77,000, or 3%` | **exact** ✓ |

**This is a passing component-identity cross-check across three pages and two statements
with zero residual** — and note *where* it lands: on the **subscriber** line, which is
**not XBRL-tagged** (§6). The check was runnable **only** at page level. The platform's
structured layer cannot perform it, and a structured query on it returns zero **by
construction** — which is precisely why a zero there is not evidence of anything.

**The one residual, and it is a scoping fact, not a defect (A18, run here).** Tying the
segment contributions to the consolidated change at FY2025: commercial services **+$17.3M**
and government **+$1.7M** sum to **+$19.0M**; consolidated revenue moved **$830,682K →
$871,659K = +$40,977K**. So the two disclosed service lines explain **46.4%** of the
consolidated increase, and **+$21,977K (53.6%)** sits in revenue lines **outside this
disaggregation** (subscriber equipment, and engineering & support). The p.53 table is a
**service-revenue** disaggregation, not a total-revenue one. **Any competitive growth
narrative built on the two service lines is incomplete by construction** — the denominator
must be carried. This detector ran on **both** the consolidated figure and the components.

---

## 5. The A12 detector: run on both sides of the comparison

A12: *"a detector run only on the subject of a comparison cannot detect a comparison
error."* Market-share and benchmarking work is comparison work, so this obligation binds
directly. **The competitor-identification detector was therefore run on the comparators'
own filings, not only on IRDM's.**

**Side A — IRDM, the subject.** p.27 names Viasat, Globalstar, ORBCOMM, Thuraya
([📄 IRDM 10-K p.27](https://agentii.ai/v/IRDM/sec151/27)).

**Side B — GSAT, the comparator.** *"Our **largest global competitors** are **Viasat,
Iridium and ORBCOMM**"* and *"Our principal regional MSS competitor in the Middle East and
Africa is **Thuraya**"* ([📄 GSAT 10-K p.10](https://agentii.ai/v/GSAT/sec128/10)).

**Result — CLEAN, and bidirectionally.** The two issuers name each other, and the overlap
is not partial: **Viasat, Iridium, ORBCOMM and Thuraya** appear on **both** lists. The
comparator set is **mutually attested by two independent issuers**, which is a stronger
identification than either filing alone. GSAT additionally names *"SpaceX's Starlink,
Amazon Leo and AST SpaceMobile"* as newer systems in the same page — so the newer-entrant
set is also independently corroborated from the comparator side.

**Side B′ — VSAT, the second comparator.** VSAT names **Iridium** in both its aviation and
its government competition lists
([📄 VSAT 10-K p.16](https://agentii.ai/v/VSAT/sec183/16)): *"Amazon Leo, Anuvu, Gogo,
**Iridium**, Panasonic Avionics Corporation, SES, SpaceX and Thales Group"* and *"BAE
Systems, Collins Aerospace, EchoStar (Hughes Network Systems), Eutelsat, General Dynamics,
**Iridium**, L3Harris, OneWeb, SES, SpaceX, Telesat"*. VSAT's own framing is candid about
the comparison hazard — *"In many cases our competitors can also be our customers or
partners"* and *"the identity and composition of competitors may change"*
([📄 VSAT 10-K p.15](https://agentii.ai/v/VSAT/sec183/15)).

**Now the result that is not clean — and it is the falsifier's own excluder.** Running the
spectrum-allocation detector across the reachable corpus returns **three events, and all
three are incumbent dispositions** — i.e. exactly the branch PIL-6 **excludes**:

| Event | Direction | Source |
|---|---|---|
| **SpaceX** acquires 50 MHz of S-band rights and licences from **EchoStar**, Sept 2025 | incumbent → new entrant | [📄 IRDM 10-K p.27](https://agentii.ai/v/IRDM/sec151/27); corroborated [📄 GSAT 10-K p.11](https://agentii.ai/v/GSAT/sec128/11) *"between EchoStar and SpaceX"* |
| **AST SpaceMobile** to lease / potentially acquire Ligado's L-band spectrum, Jan 2025 | incumbent → new entrant | [📄 IRDM 10-K p.40](https://agentii.ai/v/IRDM/sec151/40) |
| **AT&T** acquires spectrum from **EchoStar** | incumbent → acquirer | [📄 GSAT 10-K p.11](https://agentii.ai/v/GSAT/sec128/11) *"between EchoStar and AT&T"* |

**Three for three on the excluded branch, zero for one on the included branch.** The one
event with a *grant's* shape — *"the FCC granted a waiver in 2020 to **Ligado Networks** to
operate a terrestrial nationwide network … on MSS spectrum that includes a 10 MHz band
close to the spectrum that we use for all of our services"* — went to an **incumbent MSS
licensee**, not a new entrant, and is **not final**: *"We, along with a variety of other
private parties and the National Telecommunications and Information Administration on
behalf of federal government users, filed petitions for reconsideration opposing this
waiver … **These petitions remain pending**"* ([📄 IRDM 10-K p.40](https://agentii.ai/v/IRDM/sec151/40)).
Note also the 10 MHz band width against IRDM's own 8.725 MHz — the waiver band is **wider
than IRDM's entire L-band allocation**, which is the scarcity claim stated as a ratio by
the filing's own cells.

**Why this is a structural component of F6-iii, not just a small sample.** An SEC filing
records a spectrum transaction only when an SEC filer is a **party** to it. Every such
party is either the **acquirer** or the **incumbent vendor** — both of which are, by
definition, the branch the falsifier excludes. A primary grant *to a new entrant* is a
**regulatory registry event**, and it enters an SEC filing only if the new entrant
independently chooses to describe it. **The corpus is reporter-conditioned, and the
condition selects against the falsifier's positive branch.** So the absence in §5's table
is **not evidence that the falsifier survives** — it is evidence that this corpus cannot
supply the observation. Report `UNEXERCISED` on F6-iii; do not report `CLEAN`.

---

## 6. Kind 5, proven at the concept registry rather than at the query

DA-25's original evidence at IRDM was a **fact-query zero**. That understates the block, and
the brief's rule — *a zero from a `us-gaap:` query is evidence about the TAG, not the
filing* — points at the stronger test. Run the same question one level out, against the
**concept registry**:

| Query | Result |
|---|---|
| `list_xbrl_concepts(namespace="us-gaap", search="Subscriber")` | **0 concepts** |
| `list_xbrl_concepts(namespace="us-gaap", search="Spectrum")` | **0 concepts** |
| `list_xbrl_concepts(namespace="us-gaap", search="MarketShare")` | **0 concepts** |
| `list_xbrl_concepts(namespace="us-gaap", search="License")` | 7 concepts, **none a spectrum licence** — `LicenseAndServicesRevenue`, `LicenseCosts`, `EntertainmentLicenseAgreementForProgramMaterialLiabilityNoncurrent`, `FiniteLivedLicenseAgreementsGross`, … |

**Three of the four datum classes the `competitive` skill needs — subscriber base,
spectrum licences, and market share — have no `us-gaap` concept at all.** A zero returned
on any of them is a zero **by construction at the registry level**, which is a different
and stronger statement than a zero on a period: no issuer *could* have tagged them under
`us-gaap` even if it wanted to.

**And the remedies differ per class, which is why the classes must not be merged:**

| Datum class | Status | Remedy |
|---|---|---|
| **Subscriber base** | **Reachable-AS-PROSE, unqueryable-AS-TAGGED.** Disclosed in full at [📄 IRDM 10-K p.53](https://agentii.ai/v/IRDM/sec151/53) and it **ties exactly** (§4) | A derived layer over page text. **Nothing to fetch** — the datum is already on-platform |
| **Spectrum / licence inventory** | Same — reachable as prose at p.26, plus one asset-class carrier at [📄 IRDM 10-Q p.11](https://agentii.ai/v/IRDM/sec191/11) | Derived layer for the inventory; **the registry datum (FCC IBFS / ITU SNL) is off-platform entirely** |
| **Market share** | **Double-blocked.** No `us-gaap` concept exists **and no issuer in the set discloses a quantified share or a quantified MSS TAM** — the qualitative industry structure at p.27/p.9 and GSAT p.10 is prose | **Kind 5, datum class = commercial market-research dataset.** Remedy = a licensed dataset connector. **This is T103/T104's actual block, and it is not the competitor set** |

**Distinguish the three outcomes.** `CLEAN` is not available for any of them.
**`UNEXERCISED`** — the detector exists and was not run at power (F6-iii). **`UNEVIDENT`** —
the detector cannot exist at the structured layer at all (all three classes above). The
distinction matters because only one of them is fixed by running the detector harder.

---

## 7. The entity boundary: A18 and A21 applied to the competitive benchmark

A18's rule is to tie segment contributions to the consolidated change before quoting any
consolidated growth rate; §4 does that and finds the 46.4% / 53.6% split. **A18's deeper
question here is the boundary itself, and the answer is that every figure in this artifact
describes an entity that ceased to exist two days after the period end.**

The Aireon close is **not a one-off whose removal restores comparability** — it is a
**persistent step-change**, which is A21's finding applied to the entity rather than to a
cost line:

| Effect | Magnitude | Persistence |
|---|---|---|
| Seller loan (one-year, non-interest-bearing) | **$183.4M** | persistent within the year |
| Consolidation of Aireon's existing term loans | **$154.7M** | **permanent** — the loans are now group debt |
| Revolving facility drawn 2026-07-01 | **$100.0M** | **permanent** |
| **Total new / newly-consolidated debt** | **$438.1M** | **= 3.83× FY2025 net income of $114,372K** |
| Cash consideration paid at close (50% of $366.7M) | ~$183.4M | executed |

All cells from [📄 IRDM 10-Q p.20](https://agentii.ai/v/IRDM/sec191/20) and
[📄 IRDM 10-Q p.18](https://agentii.ai/v/IRDM/sec191/18).

**The second-order effect that defeats the obvious normalisation (A21's rule).** Removing
the acquisition cost alone does not restore the pre-close benchmark, because the close also
**eliminates revenue that is currently third-party**:

> *"Aireon agreed to pay the Company fees of $200.0 million to host the ADS-B receivers, of
> which $134.5 million had been paid as of June 30, 2026"*; *"the Company recognized $2.3
> million … of hosting fee revenue … for the three months ended June 30, 2026"*; *"Aireon
> has paid power and data services fees of approximately $23.5 million per year … The
> Company recorded $5.9 million of power and data service fee revenue from Aireon for each
> of the three months ended June 30, 2026"*
> — [📄 IRDM 10-Q p.18](https://agentii.ai/v/IRDM/sec191/18)

That is **$8.2M per quarter, ~$32.8M per year**, of Aireon-attributable service revenue
**recognised by IRDM from Aireon** — which becomes **intercompany and eliminates** on
consolidation, while Aireon's own external revenue is **added for the first time**. The
consolidated revenue line therefore **moves in both directions at once**, and the size of
the inbound addition **is not disclosed anywhere in the pre-close corpus**, because Aireon
was an equity-method investee. **A post-close revenue or margin benchmark cannot be
constructed from the pre-close filings in either direction**, and this is a permanent
change to the boundary, not a transaction cost to be added back.

**Grade and scope of every competitive figure in this artifact: `standalone_pre_merger`,
pre-Aireon-consolidation, pre-RKLB-merger.** A competitor set computed on this entity is
**valid for 2026-06-30 and invalid for 2026-07-02 onward** — P11's moving-boundary warning,
quantified.

**Competitive relevance of the stake itself.** Aireon is *"the operator of the world's only
space-based ADS-B air traffic surveillance system"* (p.18), and IRDM's ADS-B reception band
(1087.7–1092.3 MHz, p.26) is the spectrum that feeds it. So the acquired entity sits on a
**licence IRDM already holds** — the transaction converts a 39.5% equity interest in a
service riding IRDM's spectrum into 100% ownership of it. This is the **DA-31**
cross-holding / valuation-circularity shape (a stake whose value is set by a transaction
the holder is a party to); DA-31 is a **proposed** register entry (AMENDMENTS-PENDING A1)
and is therefore named here in prose, **not declared in `definitions_used`** — declaring an
unregistered id would be a fabricated definition reference.

---

## 8. Corrections to 001

001 is **frozen** and is **not rewritten**. These are recorded, not applied.

**1. 001's IRDM arithmetic is CORRECT and stands.** Restated, not re-derived:
`225,237 − 191,229 = 34,008` ✓; `50,258 ÷ 216,906 = 23.17%` ✓; `34,008 ÷ 225,237 = 15.10%` ✓;
`225,237 ÷ 216,906 − 1 = +3.84%` ✓. Nothing in this artifact disturbs any of them.

**2. 001's DA-23 clearance is REFUTED** — established at 002 Phase 5 §11 and **restated here,
not re-derived**: 12 concept-series carry confirmed strips across **four** statements,
including **four concepts in the Q2 2026 10-Q that 001's own quarter reads**; the
`positive | positive | no (5/5)` row clears IRDM on a population where `|x|` stripping is
**unobservable**; and the two positives-in-both-columns that 001 counted are the exact shape
of `NonoperatingIncomeExpense`, **where the validator also passes**. The correct grade for
that row is **WITHHELD, not CLEAN**.

**3. NEW — the strip reaches the line that carries IRDM's competitive-adjacency stakes.**
This is the competitive-specific extension, and it is why the correction is not merely a
data-quality note. The **equity-method** line — `IncomeLossFromEquityMethodInvestments` —
is among the stripped series (fingerprints `3,020 = 2 × 1,510` and `1,720 = 2 × 860`), and
that is the line that carries the **39.5% Aireon stake**, the only competitively-relevant
equity holding IRDM has and the entity it acquires on 2026-07-02. Under **A17** the
detector's boundary applies: the line is **bidirectional** (equity-method income and loss
both occur — the FY2023 sign differs from FY2025's), so a sign test on it has **power**,
and it has a **negative-filed instance**. The DA-23 defect is therefore **not confined to
financing and tax lines**: it reaches the competitive-adjacency line. **`UNEXERCISED` is
not available here — the test was exercised and it failed.**

**4. NEW — 001's Pillar-6 subscription is PROXY-ONLY.** `001/spec.md` line 251 subscribes
`IRDM × competitive` to Pillar 6. This artifact finds that **PIL-6's named source is
platform-unreachable at IRDM exactly as it is at SATS**, so `IRDM × competitive` **cannot
discharge PIL-6's falsifier** and supplies **only the proxy test** of §4. This is a **grade
consequence, not an arithmetic error**: 001's Pillar-6 evidence base is
**proxy-only and should be graded as such**. It does not move 001's Pillar-6 *conclusion*
— IRDM's own filing asserts the scarcity premise directly (*"fully allocated … in the early
1990s"*, p.8) — but the falsifier that is supposed to be able to overturn it was never
testable from the artifact 001 assigned to test it.

**5. Recorded discrepancy in the task briefing itself.** The briefing states the Aireon
close was *"FOUR DAYS after the quoted period end"*; the verified interval is **two days**
(period end **2026-06-30**; closing **2026-07-02**). Conclusion unaffected; the date is
quoted in §1 and a quoted date carries the same obligation as a quoted number.

**6. Recorded discrepancy in the amendment queue's own text.** A13's heading says *"FOUR
KINDS"*; its table enumerates **six**. The table is operative (§0). Recorded because A23's
census cites A13's kinds, and a reader comparing the two would otherwise find a
contradiction that is not there.

---

## 9. Could not be verified, and why

| Not verified | Why — and the specific instrument behaviour |
|---|---|
| **FCC IBFS grant records; ITU Space Network List / Master International Frequency Register** | **No connector exists.** These are the falsifier's own named sources and are public and free — this is a platform-reach gap, not a source gap. Remedy: connector. |
| **Any quantified market share, or a quantified MSS TAM** | No `us-gaap` concept exists (`search="MarketShare"` → **0**), and **no issuer in the set discloses one** — IRDM p.27/p.9 and GSAT p.10 give qualitative industry structure only. Double-blocked; remedy is a licensed market-research dataset. |
| **ORBCOMM** | Private; no SEC filings. No competitive datum exists in any source class this artifact can reach. P6 bars it from anything but proxy use. |
| **Thuraya / Space42 PLC; Eutelsat** | Not reachable. `search_companies(search="Eutelsat")` → **0 rows** — no registry entry at all. |
| **SES S.A. filings** | Registry row **exists** (CIK 0001347408, `SGBAF`) but is **not ingested**: `search_sec_filings` **0 rows**, `search_documents` **0 rows**, all coverage fields null, `entities.md` `NOT_READY`. **Remedy is inside the platform** — ingest a CIK the registry already holds. |
| **Post-close Aireon revenue and cost base** | **Not disclosed in the pre-close corpus.** Aireon was an equity-method investee; the size of the revenue IRDM consolidates on 2026-07-02 is nowhere in `sec191` or `sec151`, and the **~$32.8M/yr** of Aireon-attributable revenue already flowing to IRDM **eliminates** on consolidation. A post-close benchmark is therefore unconstructible in both directions (§7). |
| **The revenue benchmark promoted to `DEMONSTRATED`** | `search_xbrl_facts` served the values but is **not an admissible `located_via`**. Recoverable by reading each issuer's income-statement face; not done here. Reported at `DERIVED` (§3). |
| **`citation_id` discovery via `list_sources`** | `list_sources(ticker="IRDM")` **timed out**; retried per-ticker with `source_type=sec_filings`, which returned **`{"data":[],"total_count":0}` for IRDM despite IRDM having 12 10-K/10-Q accessions on the platform and demonstrably serving pages**. The same call for VSAT returned 0 and for GSAT 0. **Recorded as a tool-capability finding about the discovery surface — not as issuer absence**, per the standing rule that a zero is evidence about the instrument, not the filing. The working path used throughout is `search_sec_filings`, whose `filing_metadata.citation_id` field served every id in this artifact (`sec151`, `sec191`, `sec128`, `sec183`, `sec125`, `sec131`). |

**Instrument traps encountered and handled.** (i) `processing_status: pending` appeared on
**every** accession read here, including ones that served full cell-level text — it is
**non-discriminating** and was not used as an ingestion-absence marker (A13's negative
control). (ii) `get_ticker_coverage` reports `sec_filings: 0` for VSAT and ASTS while
`search_documents` returns 98 and 142 documents for the same tickers — the bulk
partial-view trap; VSAT and ASTS are **not** document-discovery blocked, and the `VSAT`
finding in §3 rests on pages actually read, not on that row.

---

## Sources

> Every figure asserted above resolves to the page cited. Each page was read with
> `read_source_pages` — no page number in this artifact is a guess, and no table page is
> quoted through the platform's LLM-generated `read_source_outline` description field.
> Table pages (`sec151` p.53; `sec191` p.11) are quoted as **cells**, not as sentences
> about the table, per the level-`fail` rule `table_pages_quote_cells_not_prose`.

| Figure | Source |
|---|---|
| Competition — principal MSS competitors Viasat, Globalstar, ORBCOMM, Thuraya; SpaceX 50 MHz S-band agreement Sept 2025; R&D $19.8M/$28.4M/$20.3M | [📄 IRDM 10-K p.27](https://agentii.ai/v/IRDM/sec151/27) |
| Spectrum inventory — 8.725 MHz L-band; 200 MHz K-Band; 400 MHz Ka-Band; AIS 156.0125-162.0375 MHz; ADS-B 1087.7-1092.3 MHz; ITU Master International Frequency Register; "Filings to the ITU are made on our behalf by the United States"; country codes 8816/8817; 25-year de-orbit standard | [📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26) |
| Eutelsat and SES S.A. as VSAT providers; SpaceX Starlink and OneWeb as newer entrants; "spectrum purchased from EchoStar in 2025"; 66 operational satellites | [📄 IRDM 10-K p.9](https://agentii.ai/v/IRDM/sec151/9) |
| 2,537,000 billable subscribers at 12/31/2025; revenue $830.7M → $871.7M; "fully allocated by the ITU in the early 1990s" | [📄 IRDM 10-K p.8](https://agentii.ai/v/IRDM/sec151/8) |
| Ligado — FCC 2020 waiver, 10 MHz band; "petitions remain pending"; Oct 2023 litigation; Jan 2025 Chapter 11; lease/potential transfer of L-band spectrum to AST SpaceMobile | [📄 IRDM 10-K p.40](https://agentii.ai/v/IRDM/sec151/40) |
| 2,537,000 / +77,000 / 3% from ~2,460,000; service revenue 73% and 74% of total; hosted payload revenue "principally from Aireon"; SpaceX D2D spectrum plans | [📄 IRDM 10-K p.50](https://agentii.ai/v/IRDM/sec151/50) |
| **Table cells** — Commercial services 232.2/402/$47, 181.4/1,998/$7.78, 50.7/16.1/$259, 61.6 vs 226.1/415/$46, 166.2/1,887/$7.70, 56.1/16.6/$282, 60.2; **Total commercial services 525.9/2,416 vs 508.6/2,319, Change 17.3/97**; Government service revenue 108.0/121 vs 106.3/141, Change 1.7/(20); EMSS "$110.5 million per year", expires September 2026 | [📄 IRDM 10-K p.53](https://agentii.ai/v/IRDM/sec151/53) |
| **Table cells** — "Spectrum and licenses", Indefinite, gross 14030, accumulated amortization —, net **14030 at both June 30, 2026 and December 31, 2025**; total intangible assets 109251 / (26,585) / 82666 | [📄 IRDM 10-Q p.11](https://agentii.ai/v/IRDM/sec191/11) |
| Aireon — $50.0M for ~6% preferred; carrying value $36.3M / $38.5M; ~39.5% fully diluted; agreement May 13, 2026, consummated July 2, 2026; hosting fees $200.0M of which $134.5M paid; power/data fees ~$23.5M per year; $2.3M and $5.9M in the quarter | [📄 IRDM 10-Q p.18](https://agentii.ai/v/IRDM/sec191/18) |
| Subsequent Events — remaining 60.5% of Aireon; ~$366.7M, 50% cash / 50% seller loan; $100.0M revolver drawn July 1, 2026; $183.4M seller loan; Aireon term loans $154.7M at closing | [📄 IRDM 10-Q p.20](https://agentii.ai/v/IRDM/sec191/20) |
| 2,627,000 billable subscribers at June 30, 2026, +144,000 or 6% from ~2,483,000; 66 operational satellites with in-orbit spares; Aireon acquisition description | [📄 IRDM 10-Q p.21](https://agentii.ai/v/IRDM/sec191/21) |
| Material Trends — SpaceX D2D spectrum competition; "our ability to complete the Transaction on the anticipated timeline or at all"; Rocket Lab Merger Agreement termination rights | [📄 IRDM 10-Q p.23](https://agentii.ai/v/IRDM/sec191/23) |
| **Comparator side (A12)** — "Our largest global competitors are Viasat, Iridium and ORBCOMM"; Thuraya as principal regional MSS competitor; Hughes, Gilat; SpaceX's Starlink, Amazon Leo, AST SpaceMobile; Anterix, Nextwave, TerraStar | [📄 GSAT 10-K p.10](https://agentii.ai/v/GSAT/sec128/10) |
| **Comparator side (A12, excluder)** — "recent terrestrial spectrum sales, such as between EchoStar and SpaceX and EchoStar and AT&T"; "significant barriers to entry, including the cost and difficulty associated with obtaining spectrum licenses" | [📄 GSAT 10-K p.11](https://agentii.ai/v/GSAT/sec128/11) |
| **Comparator side (A12)** — Iridium named in VSAT's aviation and government competition lists | [📄 VSAT 10-K p.16](https://agentii.ai/v/VSAT/sec183/16) |
| **Comparator side (A12)** — "The markets in which we compete are highly competitive and competition is increasing"; competitive factor "our spectrum and market access" | [📄 VSAT 10-K p.15](https://agentii.ai/v/VSAT/sec183/15) |
