---
thesis_id: "002-evidence-validation"
pillar: PIL-7
ticker: SATS
skill: competitive
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
# competitive = 826995c722a4. Independently re-derived 2026-09-18 at
# scripts/dispatch.py:132 (skill_version_hash: sha256 over sorted(skill_dir.rglob("*")),
# name bytes then file bytes, first 12 hex). Two canonical roots AGREE:
#   plugins/vertical-plugins/equity-research-core/skills/agentii/competitive  826995c722a4
#   plugins/agent-plugins/agentii-equity-agent/skills/agentii/competitive     826995c722a4
# The same run reproduces this thesis's two predecessor pins — risk 953fc5d396e7 and
# recent-quarter 07d26b9c738b — matching what those artifacts record.
# THE DECOY TREES EXIST. They are at
#   /Users/frank/A/agenzym/agentii-investment-intelligence/packaging/targets/{claude-code,codex,cowork,generic-cli}/
# and all four FAIL this hash: claude-code 20281920abd9 (1 file), codex 9029baf458f9
# (2 files), cowork 72d0501ceab3 (2 files), generic-cli 20281920abd9 (1 file), against 5
# files in each canonical root. They are invisible to the `.claude/plugins/marketplaces/`
# install because the marketplace repo's .gitignore line 18 is `packaging/targets/`. That
# is why a parent listing cannot find them and a `find` from a shallower root can.
skill_pin: "826995c722a4"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: DA-23
    chosen_reading: >
      Sign stripping — a served magnitude carrying the filed sign discarded. This artifact
      exercises it on the COMPETITIVE figures rather than the operating ones: the SATS
      segment note serves `Impairments and other` as `(66,159)` at the Other segment, and the
      component identity `operating income = revenue − total costs and expenses` closes ONLY
      if that term enters as −66,159. A consumer who reads the served value as positive
      inflates Other's total costs and expenses to 310,596 thousand and its operating loss to
      (219,613) instead of (87,295) — an error of exactly 132,318 = 2 × 66,159. The strip
      therefore propagates straight into every segment-level competitive margin.
  - da_id: DA-24
    chosen_reading: >
      Non-operating contamination of the operating line, in either direction. The competitive
      reading is the one that decides a comparison: the Q1 2026 Other-segment outcome is
      carried by a 66,159 thousand CREDIT from gains on the settlement of estimated exit,
      disposal and other costs related to terminating the 5G Network deployment, and by the
      cessation of depreciation on the abandoned network. Neither is a competitive outcome,
      and the segment that contains them is the only SATS segment that "grew" in the quarter.
      A second route confirms the direction without the cost identity: Adjusted OIBDA at Other
      is (142,149) against OIBDA (75,990), a difference of exactly (66,159) — stripping a GAIN
      must lower the measure, and it does.
  - da_id: DA-26
    chosen_reading: >
      An annual-basis fact served where a quarterly label is asserted. SATS is clean here and
      this artifact cites no FY fact as a quarter. The instance that matters is on the
      COMPARISON side: the single named competitor with on-platform financials, VSAT, has the
      twelve-month value sitting in the Q1 slot (see §5). DA-26 is therefore not a property of
      SATS or of this thesis's subject — it is a property of the pipeline, and A12 makes it a
      property of both sides of every comparison.
  - da_id: DA-29
    chosen_reading: >
      Back-solved or opaque checks, and validators whose pass is not evidence. This artifact
      runs `validate_calculation` on BOTH sides of the comparison — the first artifact in this
      phase to do so — and finds the instrument failing at 34.6% on the subject (9/26) and
      63.3% on the comparator (19/30). Two exact fingerprints of the doubling family appear on
      the comparator, and a new failure mode appears on the subject: a consolidated-scope
      computation compared against a segment-column fact under the same concept.
  - da_id: DA-30
    chosen_reading: >
      Two competing bases under one concept. At SATS the register's fifth instance is the
      segment-level impairment presentation; this artifact adds that `OIBDA` and `Adjusted
      OIBDA` are two bases of one concept, that the two SATS documents place the impairments
      line on opposite sides of the OIBDA line, and — the reading that matters for a
      comparison — that the competitive universe itself has one name on three bases at once
      (AT&T as competitor, as network supplier, and as pending acquirer).
evidence_grade: DEMONSTRATED
# P11. SATS is a deal security on the transaction fact. `tools/check_contract.py`'s
# DEAL_SECURITIES set is {IRDM, GSAT, RKLB}, so the `deal_security_tagging` rule does not
# fire mechanically here; the basis is set anyway because the filings make it load-bearing.
# Basis: BOTH purchase agreements are PENDING at 2026-03-31. The licence table (sec121 p.46)
# still carries every transaction-subject licence family at a carrying amount, so nothing has
# closed, and the only completed step is a LEASE — "AT&T, subject to a short-term spectrum
# manager lease, exercised its right to lease certain 3.45 GHz licenses from us."
deal_security_basis: standalone_pre_merger
unresolvable: false
# The ARTIFACT is not an unresolvable datum; it is the classification record for a set of
# them. Both disposition classes are in play, so neither is asserted as the artifact's class.
disposition_classes_used:
  - "UNRESOLVABLE-FROM-PLATFORM"
  - "UNRESOLVABLE-FROM-PUBLIC-SOURCES"
situation_flags:
  - "REACHABLE-BUT-NOT-RECORDABLE"
citations:
  - figure: "BSS competition — ViaSat, SpaceX/Starlink, Gilat Satellite Networks, ST Engineering iDirect; 5G Network terminated Aug 2025 with no customer traffic from 2025-11-15; over $30 billion invested in wireless spectrum licenses"
    url: "https://agentii.ai/v/SATS/sec85/22"
    citation_id: "sec85"
    ticker: "SATS"
    page_no: 22
    form_type: "10-K"
    located_via: "read_source_pages"
  - figure: "Risk factor — competition requires greater subscriber acquisition and retention spend; SpaceX is a potential MINORITY, NON-CONTROLLING equity investment, not a controlled business"
    url: "https://agentii.ai/v/SATS/sec85/37"
    citation_id: "sec85"
    ticker: "SATS"
    page: 37
    page_no: 37
    form_type: "10-K"
    located_via: "read_source_pages"
  - figure: "Wireless competition — Verizon, AT&T and T-Mobile 'each with substantial market share'; market saturation; cost of attracting exceeds cost of retaining"
    url: "https://agentii.ai/v/SATS/sec85/40"
    citation_id: "sec85"
    ticker: "SATS"
    page_no: 40
    form_type: "10-K"
    located_via: "read_source_pages"
  - figure: "Dependence on T-Mobile (MNSA) and AT&T (NSA, Amended NSA) for the network the Hybrid MNO runs on; minimum purchase commitments; three-role overlap on AT&T"
    url: "https://agentii.ai/v/SATS/sec85/42"
    citation_id: "sec85"
    ticker: "SATS"
    page_no: 42
    form_type: "10-K"
    located_via: "read_source_pages"
  - figure: "Pay-TV segment — 6.998 million Pay-TV subscribers at 2025-12-31 (5.022M DISH TV, 1.976M SLING TV); IBM/OTT competition; retention costs"
    url: "https://agentii.ai/v/SATS/sec85/85"
    citation_id: "sec85"
    ticker: "SATS"
    page_no: 85
    form_type: "10-K"
    located_via: "search_keyword_in_source"
  - figure: "Wireless segment — 7.511 million subscribers at 2025-12-31; Hybrid MNO completed 2025-11-15; named competitor list including MVNO brands"
    url: "https://agentii.ai/v/SATS/sec85/95"
    citation_id: "sec85"
    ticker: "SATS"
    page_no: 95
    form_type: "10-K"
    located_via: "read_source_pages"
  - figure: "BSS segment at FY2025 — contracted revenue backlog ~$1.4 billion at 2025-12-31; competition paragraph naming ViaSat, SpaceX, Gilat, ST Engineering iDirect"
    url: "https://agentii.ai/v/SATS/sec85/102"
    citation_id: "sec85"
    ticker: "SATS"
    page_no: 102
    form_type: "10-K"
    located_via: "search_keyword_in_source"
  - figure: "Wireless spectrum licence table at 2026-03-31 — carrying amounts by licence family, build-out deadlines, expiration dates; Subtotal 29,614,839; capitalized interest 10,270,436; impairment (5,334,473); Total 34,550,802; note (2) AT&T short-term spectrum manager lease"
    url: "https://agentii.ai/v/SATS/sec121/46"
    citation_id: "sec121"
    ticker: "SATS"
    page_no: 46
    form_type: "10-Q"
    located_via: "read_source_pages"
  - figure: "Segment note Q1 2026 — full income statement by segment with the Eliminations column; Other segment 'Impairments and other' served (66,159); Other D&A 11,305 against 303,929"
    url: "https://agentii.ai/v/SATS/sec121/71"
    citation_id: "sec121"
    ticker: "SATS"
    page_no: 71
    form_type: "10-Q"
    located_via: "read_source_pages"
  - figure: "Segment note Q1 2025 comparatives — intersegment revenue 71,592 of which Other 60,234; Other connectivity services 343,080; consolidated D&A 488,333"
    url: "https://agentii.ai/v/SATS/sec121/72"
    citation_id: "sec121"
    ticker: "SATS"
    page_no: 72
    form_type: "10-Q"
    located_via: "read_source_pages"
  - figure: "Segment revenue and operating income table Q1 2026 vs Q1 2025 — Pay-TV 2,294,264 vs 2,538,727; Wireless 962,491 vs 969,668; BSS 329,656 vs 370,658; Other 90,983 vs 62,297; Eliminations (9,905) vs (71,592); Total 3,667,489 vs 3,869,758"
    url: "https://agentii.ai/v/SATS/sec121/89"
    citation_id: "sec121"
    ticker: "SATS"
    page_no: 89
    form_type: "10-Q"
    located_via: "search_keyword_in_source"
  - figure: "Pay-TV segment at 2026-03-31 — 6.632 million Pay-TV subscribers (4.845M DISH TV, 1.787M SLING TV); pay-TV competition paragraph"
    url: "https://agentii.ai/v/SATS/sec121/90"
    citation_id: "sec121"
    ticker: "SATS"
    page_no: 90
    form_type: "10-Q"
    located_via: "read_source_pages"
  - figure: "Pay-TV subscriber metrics — DISH TV gross activations 32,000 vs 46,000; DISH TV churn 1.41% vs 1.36%; SLING net losses 189,000 vs 198,000; ESPN Unlimited and FOX One launched August 2025"
    url: "https://agentii.ai/v/SATS/sec121/94"
    citation_id: "sec121"
    ticker: "SATS"
    page_no: 94
    form_type: "10-Q"
    located_via: "read_source_pages"
  - figure: "Wireless segment — 7.527 million subscribers at 2026-03-31; Hybrid MNO; nationwide MNO competitor paragraph and MVNO brand list"
    url: "https://agentii.ai/v/SATS/sec121/97"
    citation_id: "sec121"
    ticker: "SATS"
    page_no: 97
    form_type: "10-Q"
    located_via: "read_source_pages"
  - figure: "BSS competition paragraph in the 10-Q — backlog ~$1.4 billion at 2026-03-31; 'Amazon Leo when launched' added to the primary satellite competitor list"
    url: "https://agentii.ai/v/SATS/sec121/100"
    citation_id: "sec121"
    ticker: "SATS"
    page_no: 100
    form_type: "10-Q"
    located_via: "read_source_pages"
  - figure: "BSS results of operations — Total revenue 329,656 vs 370,658; SG&A 62,290 vs 90,096 of which subscriber acquisition costs 28,389 vs 46,432; D&A 49,940 vs 104,898; Operating income 44,184 vs (19,195); OIBDA 94,124 vs 85,703; broadband subscribers 0.681M vs 0.853M"
    url: "https://agentii.ai/v/SATS/sec121/101"
    citation_id: "sec121"
    ticker: "SATS"
    page_no: 101
    form_type: "10-Q"
    located_via: "read_source_pages"
  - figure: "Segment Adjusted OIBDA reconciliation — segment operating income, D&A, OIBDA, impairments and other, Adjusted OIBDA by segment; Consolidated OIBDA 559,448 and Adjusted OIBDA 493,289"
    url: "https://agentii.ai/v/SATS/sec121/108"
    citation_id: "sec121"
    ticker: "SATS"
    page_no: 108
    form_type: "10-Q"
    located_via: "read_source_pages"
---

# SATS × competitive — the PIL-7 reachability census for PIL-6

**T105 / T106 / T107 — direct-competitor-identification-and-analysis, market-share-dynamics-analysis, market-share-evolution-and-competitive-benchmarking.**

**The question, literally.** *Confirms which PIL-6 falsifiers are platform-blocked rather than
source-blocked (P6).* The output below is a **classification, not a narrative**: every PIL-6
falsifier in scope, the not-testable kind that applies, the disposition, and — where the answer
is *"the source has it but the platform cannot reach it"* — **the name of the source**.

**What is new here against the predecessor.** The SATS × risk artifact
(`2026-09-18_1500_risk_methodology.md`) carries **one** PIL-6 row: `UNRESOLVABLE-FROM-PLATFORM`,
kind 5, resolving source *FCC IBFS file numbers and ITU filings*, proxy *the issuer's own licence
table + impairment by asset class*. That row is **confirmed and not re-derived**. This artifact
**extends** it in four ways: it decomposes the single `wrong_if` metric into nine atomic
sub-claims; it adds **two** platform blockers the risk census does not carry (the comparator
set, and the market-share denominator); it isolates the **one** comparator that is *not*
platform-blocked and shows that its served facts are **not recordable** as a quarterly
comparison anyway; and it separates out the **one** source-blocked leg, which has a different
remedy from all the others.

---

## §1 The competitor set, as filed, with its reachability (T105)

The set is **named on the face of the filings**, not inferred. Every name below was read off a
page, and the page is cited. The right-hand column is the *reachability* verdict, established by
query, not by assumption.

| Segment | Named comparators, as filed | Filed where | Reachability on this platform |
|---|---|---|---|
| **Wireless** | Verizon, AT&T, T-Mobile — "the only nationwide MNOs in the United States", "each with substantial market share"; plus Metro PCS (T-Mobile), Cricket Wireless (AT&T), Visible / Tracfone / Total Wireless (Verizon), Mint Mobile (T-Mobile); plus MVNOs Consumer Cellular, Spectrum Mobile, Xfinity Mobile | [sec121 p.97](https://agentii.ai/v/SATS/sec121/97), [sec85 p.95](https://agentii.ai/v/SATS/sec85/95), [sec85 p.40](https://agentii.ai/v/SATS/sec85/40) | **VZ, T, TMUS: absent.** `search_xbrl_facts` returns `TICKER_NOT_FOUND` for each. CHTR, CMCSA: coverage 14% (a 13F holdings row only). Consumer Cellular: private. **The entire named Wireless comparator set is unreachable.** |
| **Pay-TV** | Own brands DISH TV and SLING TV; "established pay-TV providers and broadband service providers"; live-linear OTT; and — named explicitly as new direct entrants — **ESPN Unlimited and FOX One**, launched August 2025 | [sec121 p.90](https://agentii.ai/v/SATS/sec121/90), [sec85 p.85](https://agentii.ai/v/SATS/sec85/85), [sec121 p.94](https://agentii.ai/v/SATS/sec121/94) | OTT comparators are not carried as a comparator set under any ingested source type. The two named programme-level entrants are subsidiaries of listed issuers (Disney, Fox) but the filing names *products*, not issuers, and no ingested source resolves a product to an issuer. |
| **Broadband and Satellite Services** | **ViaSat** and **SpaceX/Starlink** as "primary satellite competitors in the North American consumer market"; **Gilat Satellite Networks Ltd** and **ST Engineering iDirect, Inc.** as "principal competitors for the supply of satellite technology platforms"; and, added in the 10-Q only, **Amazon Leo "when launched"** | [sec121 p.100](https://agentii.ai/v/SATS/sec121/100), [sec85 p.102](https://agentii.ai/v/SATS/sec85/102) | **VSAT: reachable** (xbrl_facts 21,898; src_documents 98; transcripts 19). **AMZN: issuer reachable** (775 FY2025 facts, source_authority 3) but the Leo datum is not disclosed. **SpaceX/Starlink: private.** **GILT: `TICKER_NOT_FOUND`.** **ST Engineering iDirect: not covered at all** (SGX-listed parent). |
| **Other** | None. The segment is the legacy 5G Network and its decommissioning, and by 2025-11-15 it has "no customer traffic" | [sec85 p.22](https://agentii.ai/v/SATS/sec85/22) | Not a competitive segment. It is nonetheless the segment that moved the consolidated result most (§5), which is the point of §5. |

**The answer to the question the census turns on.** *Is there a competitor set that is NOT
platform-blocked?* **Yes — and it is exactly one member deep, and it is the wrong member.**

- **One** named comparator has on-platform financials: **ViaSat (VSAT)**. And its served facts
  are unusable as a quarterly comparator without a re-derivation the platform does not perform
  (§4). So the reachable comparator is `REACHABLE-BUT-NOT-RECORDABLE`.
- **Six** named comparators are on the platform's registry gap list: **VZ, T, TMUS, GILT, CHTR,
  CMCSA** all return `TICKER_NOT_FOUND` from the fact store. The three most consequential —
  the nationwide MNOs SATS competes against in Wireless, its largest segment after Pay-TV — are
  **entirely absent**.
- **Two** named comparators are private or effectively so: **SpaceX/Starlink** (no periodic
  financial disclosure exists to ingest) and **Consumer Cellular**.
- **One** named comparator, **ST Engineering iDirect**, is a product line inside a foreign
  parent and is not a disclosure unit.

**The structural shape, stated plainly.** The comparator that is reachable is not the
comparator that is filed for; and the comparator that is filed for is not reachable. SATS's own
`entities.md` names the adjacent case — MOG-A and ENS carry fund-sourced cases with zero issuer
coverage. Here the mismatch runs the other way and is sharper: **IRDM is 100% covered on all
seven source types and sits in the same taxonomy node as SATS (`tech.telecom_services`), but
Iridium is not named as a competitor anywhere in SATS's filings that this search reached.** The
workspace's corpus gap and SATS's filed comparator set do not intersect. The one fully-covered
comparability in the corpus is a company the issuer does not compare itself to; and IRDM is
itself a 002 deal security, so using it as a "competitor" would need its own P11 tag.

**Also recorded, because it will mislead a sector-keyed retrieval:** `GSAT` files under
`tech.tech_hardware`, not `tech.telecom_services`. A comparator set assembled by taxonomy node
therefore silently omits the 001-pinned `GSAT × competitive` leg.

---

## §2 The PIL-6 falsifier, decomposed, and the classification

001's PIL-6 `wrong_if` is a **single** metric:

```
metric = new_entrant_primary_spectrum_or_slot_grant_without_incumbent_acquisition
threshold = 0
source = FCC_IBFS_or_ITU_Space_Network_List
op = >
```

"Falsifiers" plural therefore requires decomposing that metric into its atomic sub-claims and
classifying each. Nine rows. The **KIND** column uses A13's six kinds plus A19's kind 7; the
**disposition** column uses the two enumerable checker classes plus A22's flagged situation.

| # | PIL-6 falsifier sub-claim | Disposition | Not-testable KIND | Named resolving source |
|---|---|---|---|---|
| **F0** | **The falsifier as written**: any new entrant holds a primary spectrum or slot grant obtained without acquiring from an incumbent | `UNRESOLVABLE-FROM-PLATFORM` | **kind 5** — ingestion absence of a datum class (regulatory licence-grant registry) | **FCC IBFS / Universal Licensing System grant records**; **ITU Space Network List** for slots. Public, in principle reachable, not reachable by this toolchain. This is the subject of the risk artifact's row; **confirmed, unchanged.** |
| **F1** | **`new_entrant`** — the numerator's population: which firms are entrants | `UNRESOLVABLE-FROM-PLATFORM` | **kind 5** (no licensee or security-master registry ingested) **+ kind 1** at three specific tickers — VZ, T and TMUS return `TICKER_NOT_FOUND` | **FCC licensee registry** + a security master. Distinct remedy from F0: this blocks even if IBFS were ingested, because the *comparison side* has no facts. |
| **F2** | **`primary` vs `without_incumbent_acquisition`** — the term that actually decides the falsifier | `UNRESOLVABLE-FROM-PLATFORM` | **kind 5** | **FCC IBFS grant records** (application → grant chain per licence). No ingested source carries a grant chain for any firm. |
| **F3** | **`spectrum grant` against the subject** — SATS's own licence base, the 006-adopted proxy | **EVALUABLE** — computed, tied out, **CLEAN** | none | [sec121 p.46](https://agentii.ai/v/SATS/sec121/46). **Proxy adopted from thesis 006, not regenerated** (plan.md line 171). It does **not** fire the falsifier: it is the subject's own asset register, not a grant registry, and 006's rule holds — *the proxy triggers external verification; it does not fire the falsifier.* |
| **F4** | **`slot grant`** — ITU orbital-slot coordination status | `UNRESOLVABLE-FROM-PLATFORM` | **kind 5** | **ITU Space Network List.** Note the asymmetry: the *asset* side is reachable — the same licence table carries DBS 677,409, MVDDS 24,000 and LMDS 0 thousands — but slot status and coordination are not. |
| **F5** | **Market share and share evolution** (T106/T107's own requirement) | `UNRESOLVABLE-FROM-PLATFORM` | **kind 5** — the **DENOMINATOR CLASS** is not ingested | **CTIA Wireless Industry Survey**, **Leichtman Research Group**, **Nielsen**, **SNL Kagan**. The numerators are on-platform (7.527M wireless, 6.632M Pay-TV, 0.681M broadband); no industry-aggregate denominator is. This row is **new** — the risk census does not carry it, and it blocks every share figure in T106/T107 independently of F0. |
| **F6** | **Competitor benchmarking on the reachable comparator** (T105/T107) | **`REACHABLE-BUT-NOT-RECORDABLE`** | **kind 7** — detector gap at a computable datum (A19) | Not a new source. **Resolution is a pipeline repair of the comparison-side fiscal-period labelling (DA-26).** See §4. |
| **F7** | **SpaceX/Starlink and ST Engineering iDirect as comparators** | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** | **kind 2** — genuine absence from source | A **monitoring task**, not a platform ticket. SpaceX publishes no periodic financials; ST Engineering does not disclose to the iDirect line. **This is the only source-blocked leg in the set, and its remedy is the one the task says must never be merged with platform-blocked.** |
| **F8** | **Amazon Leo as a comparator** | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** for the datum, while the **issuer is on-platform** | **kind 2** — genuine absence from source | AMZN is reachable (775 FY2025 facts, `source_authority` 3); LEO is **not a reportable segment** and its revenue and subscriber base are not disclosed. Resolution: a change in AMZN's segment disclosure, or the FCC grant record. **Platform presence of an issuer is not availability of a datum — this row is the worked example of that distinction.** |

**Counts.** 9 rows: **6** `UNRESOLVABLE-FROM-PLATFORM` (F0, F1, F2, F4, F5, F6-part), **2**
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` (F7, F8), **1** evaluable (F3), **1** flagged
`REACHABLE-BUT-NOT-RECORDABLE` (F6). Kinds used: **1, 2, 5 and 7.** Kinds **3, 4 and 6 are
`UNEXERCISED`** here and are not claimed as clean: kind 3 (validator-completeness) is exercised
in §4 on the wrong question — it is a *sign* failure, not a *reachability* failure; kind 4
(mechanism-population identity) has no instance in a competitive frame; kind 6 (coverage window)
is not reached because the window that fails is the fiscal-period *label*, not the period
*captured*.

---

## §3 The three-way distinction, discharged

**Platform-blocked** — public and reachable in principle, not by this toolchain. Remedy: platform
reach. Class: `UNRESOLVABLE-FROM-PLATFORM`. Rows **F0, F1, F2, F4, F5** and the registry half of
**F6**.

**Source-blocked** — no public source carries it. Remedy: monitoring task. Class:
`UNRESOLVABLE-FROM-PUBLIC-SOURCES`. Rows **F7, F8**. **Never merged with the above** — a bigger
platform does not resolve F7, and a monitoring task does not resolve F0.

**The third case.** `REACHABLE-BUT-NOT-RECORDABLE` (A22) applies and is flagged on **F6**: the
datum is on-platform, the arithmetic is available, and the *served fact* still cannot be
recorded as the comparison it is needed for. It is neither of the two dispositions, because its
remedy is neither new reach nor a monitor — it is **re-labelling**. See §4.

---

## §4 A12 — the detector on BOTH sides, and what it returns

> *A detector run only on the subject of a comparison cannot detect a comparison error.*

Market-share and benchmarking work **is** comparison work, so this applies here more than to any
other artifact in the phase. Three detectors were run on the comparison side. Two ran; one could
not be run to closure.

### 4a. `validate_calculation` on the comparator — ran, and fails worse than the subject

| Side | Accession | pass | warn | fail | fail rate |
|---|---|---|---|---|---|
| **Subject** — SATS Q1 2026 10-Q | `0001104659-26-058150` | 15 | 2 | **9** | **34.6%** |
| **Comparator** — VSAT FY2026 10-K | `0001193125-26-248290` | 10 | 1 | **19** | **63.3%** |

This is the **first run of the validator on a comparator anywhere in this phase**, and it
changes the register's DA-29 caution from a subject-side observation to a **both-sides** finding.
The `2 ×` articulation fingerprint (A24) is **not a SATS property**. Eleven of VSAT's nineteen
failures carry the doubling signature, of which nine are exact to the thousand:

| VSAT concept | computed | reported | diff | exact doubling |
|---|---|---|---|---|
| `NetCashProvidedByUsedInFinancingActivities` | −694,421,000 | 694,421,000 | 1,388,842,000 | **2 × 694,421,000** |
| `CashCashEquivalentsRestrictedCash…IncreaseDecrease` | 3,045,040,000 | 134,730,000 | 2,910,310,000 | **2 × 1,455,155,000** |
| `AllocatedShareBasedCompensationExpenseNetOfTax` | 4,445,000 | 78,015,000 | 73,570,000 | **2 × 36,785,000** |
| `NetIncomeLoss` | −3,926,000 | 34,086,000 | 38,012,000 | **2 × 19,006,000** |
| `ComprehensiveIncomeNetOfTax` | −11,808,000 | 11,808,000 | 23,616,000 | **2 × 11,808,000** |
| `Assets` | 14,013,750,000 | 15,226,596,000 | 1,212,846,000 | **2 × 606,423,000** |
| `LongTermDebtAndCapitalLeaseObligations` | 6,506,358,000 | 6,390,852,000 | 115,506,000 | **2 × 57,753,000** |
| `LongTermDebt…IncludingCurrentMaturities` | 7,166,617,000 | 6,585,115,000 | 581,502,000 | **2 × 290,751,000** |
| `FiniteLivedIntangibleAssetsNet` | 2,822,436,000 | 825,000,000 | 1,997,436,000 | **2 × 998,718,000** |
| `FinanceLeaseLiabilityPaymentsDue` | 517,892,000 | 258,946,000 | 258,946,000 | **computed = 2 × reported** |
| `LesseeOperatingLeaseLiabilityPaymentsDue` | 1,265,134,000 | 632,567,000 | 632,567,000 | **computed = 2 × reported** |

`NetCashProvidedByUsedInFinancingActivities` is the sharpest: the computed value is the exact
negative of the reported value, on a line where the filing itself is unambiguous — a financing
inflow of 694,421 thousand is classified as a *use* of cash on one side and a *source* on the
other. **A `pass` on this side is not evidence about sign either.** The instrument is now shown
to be equally incautious about both parties to a comparison, which is exactly the failure A12
predicts and no prior artifact had tested.

### 4b. A new validator failure mode, found on the SUBJECT — scope confusion

SATS `OperatingIncomeLoss`, Q1 2026: `computed` **3,657,411,000**, `reported` **173,000**,
`diff` 3,657,238,000, status `fail`. Neither number is the consolidated operating income, which
is **392,847** thousand.

- `computed` 3,657,411 **exactly equals** consolidated revenue 3,667,489 minus the Eliminations
  cost line 10,078. The computation aggregated a consolidated-scope numerator against a
  segment-scope denominator.
- `reported` 173 **is the Eliminations column's operating income** — not the consolidated total.
  The two figures the validator compared are of **different scopes**, and the reported side
  silently picked up a segment-column fact under the consolidated concept.

The 2025 comparative fails the same way: `computed` 22,185,000 against `reported` 63,000, and
**63 is the Q1 2025 Eliminations operating income** (−63 thousand). This is a **new failure
mode** — the validator joined on concept without resolving scope — and it is a candidate for the
Phase-6 amendment queue, because the mechanism is *segment tables reuse the same concept under
dimensions*, which is standard practice, not a defect the issuer introduced.

### 4c. The period-label defect on the comparator — this is the one that makes F6 not recordable

`get_company_financials` serves VSAT's fiscal periods thus (revenues, thousands):

| Served label | Served `period_start` → `period_end` | Served duration | Revenues | EPS basic |
|---|---|---|---|---|
| FY2026 **Q1** | 2025-04-01 → **2026-03-31** | **twelve months** | **4,640,280** | 0.25 |
| FY2026 Q2 | 2026-04-01 → 2026-06-30 | three months | 1,156,543 | 0.38 |
| FY2025 Q4 | → 2025-12-31 | three months | 1,157,045 | 0.18 |
| FY2025 Q3 | → 2025-09-30 | three months | 1,140,893 | 0.45 |
| FY2025 Q2 | → 2025-06-30 | three months | 1,171,054 | 0.43 |
| FY2025 **Q1** | 2025-04-01 → 2025-03-31 | **twelve months** | **4,519,571** | **4.48** |
| FY2024 **Q1** | → 2024-03-31 | **twelve months** | **4,283,758** | **9.12** |

**The Q1 slot carries the fiscal-year aggregate.** FY2025 Q1 EPS is 4.48 and FY2024 Q1 EPS is
9.12 — annual magnitudes — against 0.18–0.45 in the Q2/Q3/Q4 slots. The FY2026 Q1 row is worse
than merely mislabelled: its *duration* is twelve months while its EPS (0.25) and net income
(34,086) are quarterly, so **a single served row is internally inconsistent across concepts**.
DA-26 is reproduced on the comparison side, and it mixes with DA-27 within one row.

**Two consequences, both quantified.**

1. **The served row overstates the comparator ~3.97×.** A benchmark that reads VSAT's FY2026 Q1
   as a quarter compares 4,640,280 against SATS's Q1 2026 consolidated revenue of 3,667,489 and
   concludes VSAT is 1.27× SATS. The correct quarterly comparison is the *residual* March-2026
   quarter: 4,640,280 − (1,171,054 + 1,140,893 + 1,157,045) = **1,171,288 thousand** (DERIVED),
   against SATS's 3,667,489 — **VSAT is 0.32× SATS, not 1.27×.** The sign of the conclusion
   flips.
2. **Therefore F6 is `REACHABLE-BUT-NOT-RECORDABLE`.** The datum is on-platform, the arithmetic
   closes, and the served fact still cannot be recorded as a quarterly comparator without a
   re-derivation the platform neither performs nor labels. **The remedy is a label repair, not a
   new source** — which is why this is neither disposition class.

**Detector not run to closure, recorded as `UNEXERCISED` and not as `CLEAN`.** The component
identity on the comparator — `operating income = revenue − operating expenses` — does **not**
close from the served VSAT concepts: 4,640,280 − 4,271,443 = 368,837, against a served
`OperatingIncomeLoss` of 108,125. That result is **not** a finding of a defect: VSAT's income
statement places cost of revenues on a tag boundary this artifact did not read, so the identity
may simply be missing a term. **What would resolve it: reading VSAT's filed income-statement
page.** Per the method, an identity that cannot be closed is `UNEXERCISED`, and a zero or a
non-closure is evidence about the *tags*, not about the *filing*.

---

## §5 A18 — the entity-boundary detector, run mechanically, and the artefacts it finds

A18's detector is arithmetic and needs no filing text: **tie the segment contributions to the
consolidated change.**

### 5a. The tie-out CLOSES, exactly

| Segment | Q1 2026 | Q1 2025 | Variance |
|---|---|---|---|
| Pay-TV | 2,294,264 | 2,538,727 | (244,463) |
| Wireless | 962,491 | 969,668 | (7,177) |
| Broadband and Satellite Services | 329,656 | 370,658 | (41,002) |
| Other | 90,983 | 62,297 | 28,686 |
| Eliminations | (9,905) | (71,592) | 61,687 |
| **Total revenue** | **3,667,489** | **3,869,758** | **(202,269)** |

Σ variances = −244,463 − 7,177 − 41,002 + 28,686 + 61,687 = **−202,269**. **Exact.** Operating
income ties identically: −181,863 + 58,112 + 63,379 + 541,115 + 236 = **+480,979**, against a
consolidated move from (88,132) to 392,847. Identity **NOT VACUOUS** — the eliminations term is
independently disclosed and non-zero in both periods.

**Methodological finding: a clean tie is NOT evidence of a stable boundary.** It certifies
internal consistency of the table as filed. It cannot certify that the segments are comparable
to their own prior-period selves, and here they are not. **A second detector is required, and
A18 should record it**: the *period-over-period composition* test, which is 5b.

### 5b. The boundary HAS moved, inside the filed perimeter

The eliminations line is the tell. Intersegment revenue **collapsed from 71,592 to 9,905
thousand, −86.2%**, and within it the Other segment's intersegment revenue went **60,234 → 107**
while Other's *external* equipment revenue went **2,063 → 90,876**. Roughly **$90 million of
activity crossed from internal to external** between the two periods. Correspondingly, Other's
"Cost of services — connectivity services" went **343,080 → 0**.

The mechanism is filed and is not competitive: *"we terminated our deployment of our 5G Network
… we began the abandonment and decommission process"* and *"we migrated all customer traffic from
our 5G Network to AT&T's network."* The internal 5G network service relationship ended
([sec85 p.22](https://agentii.ai/v/SATS/sec85/22), [sec121 p.97](https://agentii.ai/v/SATS/sec121/97)).

**The consequence a share or growth figure will trip on.** **Other is the only segment that
"grew": +46.0% revenue, and +541,115 thousand of operating income — 112.5% of the entire
consolidated operating-income improvement of 480,979.** That number is not a competitive
outcome. Decomposed exactly:

| Other segment income effect, Q1 2026 vs Q1 2025 | thousands | share |
|---|---|---|
| Revenue | +28,686 | 5.3% |
| Cessation of connectivity-services cost | +343,080 | **63.4%** |
| New equipment cost of sales | (183,132) | −33.8% |
| SG&A | (6,302) | −1.2% |
| Impairment credit | +66,159 | 12.2% |
| Depreciation relief (303,929 → 11,305) | +292,624 | **54.1%** |
| **Total** | **+541,115** | **100.0%** |

**Any competitive share or growth figure computed on the "Other" segment is an artefact of a
reporting-boundary move and of an asset's abandonment — not of competition.** This is the direct
answer to the A18 question the task poses.

**A second boundary artefact, at segment-asset level.** Depreciation moved across segments:

| Segment | D&A Q1 2026 | D&A Q1 2025 | change |
|---|---|---|---|
| Pay-TV | 55,866 | 76,443 | −20,577 (−26.9%) |
| **Wireless** | **49,499** | **20,187** | **+29,312 (+145.2%)** |
| Broadband and Satellite Services | 49,940 | 104,898 | −54,958 (−52.4%) |
| Other | 11,305 | 303,929 | −292,624 (−96.3%) |
| Eliminations | (9) | (17,124) | +17,115 |
| **Consolidated** | **166,601** | **488,333** | **−321,732 (−65.9%)** |

Wireless's asset base more than doubled in D&A terms in one year, because the Hybrid MNO retains
the 5G core that Other abandoned. **Any segment-margin comparison for Wireless — against
Verizon, AT&T or T-Mobile — is a comparison against a segment whose charged depreciation
changed 2.45× within the window.** The cause of the BSS half (-52.4%) is **not** established on
the pages read; it is carried forward, not asserted.

---

## §6 A21 — second-order contamination, applied to the competitive figures, with one correction

**The predecessor's 80.6% reproduces exactly.** Consolidated D&A relief 321,732 plus impairment
credit 66,159 = 387,891, against a consolidated operating-income improvement of 480,979:
**387,891 / 480,979 = 80.65%.** ✓

**But the figure does not propagate the way "it applies to any competitive share or growth
figure" implies, and the correction runs in both directions.** The contaminated measure is
**operating income and every margin built on it**. OIBDA **adds D&A back**, so it is invariant to
the D&A relief; the impairment credit is the only item that reaches it. Applying 80.6% to an
OIBDA-based comparison **overstates** the contamination. Applying it to a *segment* margin
**understates** it, because the segment-level contamination is larger than the consolidated one:

**Broadband and Satellite Services, the segment with the named comparators:**

| | Q1 2026 | Q1 2025 | change |
|---|---|---|---|
| Total revenue | 329,656 | 370,658 | (41,002) (−11.1%) |
| Cost of services | 102,352 | 113,125 | (10,773) |
| Cost of sales — equipment and other | 70,890 | 81,734 | (10,844) |
| SG&A | 62,290 | 90,096 | (27,806) (−30.9%) |
| — of which **subscriber acquisition costs** | **28,389** | **46,432** | **(18,043) (−38.9%)** |
| D&A | 49,940 | 104,898 | (54,958) (−52.4%) |
| **Operating income (loss)** | **44,184** | **(19,195)** | **+63,379** |
| **OIBDA** | **94,124** | **85,703** | **+8,421 (+9.8%)** |
| Broadband subscribers, period end | 0.681M | 0.853M | (0.172M) (−20.2%) |

- Operating margin went from **−5.18% to +13.40%**, a swing of **18.58 percentage points** of
  which **54,958 / 63,379 = 86.7% is D&A relief** — *above* the consolidated 80.6%.
- On the D&A-invariant measure the improvement is **+9.8%**, and its composition is
  **27,806 / 49,423 = 56.3%** cost reduction, of which **18,043 / 27,806 = 64.9% is lower
  subscriber-acquisition spending** — a *demand-side* reduction, not an efficiency gain. The
  identity closes exactly: −41,002 + 10,773 + 10,844 + 27,806 = **+8,421**.
- So: **BSS OIBDA rose 9.8% while revenue fell 11.1% and broadband subscribers fell 20.2%, and
  65% of the rise is the arithmetic of a deliberately shrinking business.** The filing states
  the mechanism itself: *"The increase in net Broadband subscriber losses was primarily due to
  lower gross subscriber additions. We continue to experience increased competition from
  satellite-based competitors and other technologies"* ([sec121 p.101](https://agentii.ai/v/SATS/sec121/101)).

Pay-TV is the mirror image and needs no normalisation to see it: DISH TV gross activations
**32,000 vs 46,000, −30.4%**; DISH TV churn **1.41% vs 1.36%**; SLING net losses 189,000 vs
198,000; and two new direct-to-consumer entrants named by the issuer as the cause — **ESPN
Unlimited and FOX One, launched August 2025** ([sec121 p.94](https://agentii.ai/v/SATS/sec121/94)).

---

## §7 DA-30 and DA-23 on the competitive figures

**Two bases under one concept, at the segment level.** `OIBDA` and `Adjusted OIBDA` differ by
exactly the impairments item, and the **two SATS documents place that item on opposite sides of
the OIBDA line** — the segment note deducts it before OIBDA
([sec121 p.71](https://agentii.ai/v/SATS/sec121/71)), the MD&A adds it back after OIBDA to reach
Adjusted OIBDA ([sec121 p.108](https://agentii.ai/v/SATS/sec121/108)). At the Other segment the
pair is OIBDA **(75,990)** and Adjusted OIBDA **(142,149)**; the difference is **exactly
(66,159)**, checked, and it is the credit itself — not a perimeter, not a rounding. Consolidated,
the same pair is **559,448** and **493,289**.

**The `(66,159)` sign, confirmed by two independent routes.**

1. **Cost identity.** Other's total costs and expenses = 0 + 183,132 + 50,000 − 66,159 + 11,305
   = **178,278**, which is the served value, and revenue 90,983 − 178,278 = **(87,295)**, the
   served operating loss. The identity closes **only** with the term entering as −66,159.
2. **The OIBDA/Adjusted OIBDA gap.** Stripping a *gain* must lower the measure; 75,990 − 66,159
   = 142,149 in magnitude, and the direction is correct. A charge would have produced the
   opposite sign.

**The de-contamination error the register warns about, reproduced to the thousand.** A consumer
who takes the served value as positive makes Other's total costs and expenses 178,278 + 132,318
= 310,596 and its operating loss (219,613) instead of (87,295) — an error of **exactly 132,318 =
2 × 66,159**. The risk artifact's DA-23/DA-24-inside-one-figure finding is **confirmed and now
located at the cell**: the same served token `(66,159)` appears in the segment note and the MD&A
reconciliation, is filed negative, is served negative, and *means* a gain.

**The three-role overlap, which is the DA-30 reading that bears on competition.** One name,
**AT&T**, appears in SATS's filings on three bases at once:

| Basis | Filed evidence |
|---|---|
| **Competitor** | *"The wireless services industry has incumbent and established competitors such as Verizon, AT&T and T-Mobile, each with substantial market share"* ([sec85 p.40](https://agentii.ai/v/SATS/sec85/40), [sec121 p.97](https://agentii.ai/v/SATS/sec121/97)) |
| **Supplier** | *"Through the MNSA and the NSA, we depend on T-Mobile and AT&T to provide network services to our Wireless subscribers"*; the Amended NSA carries minimum data thresholds ([sec85 p.42](https://agentii.ai/v/SATS/sec85/42)) |
| **Pending acquirer** | the AT&T Transactions block in the licence table, still at carrying amount; *"AT&T, subject to a short-term spectrum manager lease, exercised its right to lease certain 3.45 GHz licenses from us"* ([sec121 p.46](https://agentii.ai/v/SATS/sec121/46)) |

**SpaceX repeats the pattern**: named a primary BSS competitor
([sec121 p.100](https://agentii.ai/v/SATS/sec121/100)) and simultaneously the subject of a
potential **minority, non-controlling** equity investment
([sec85 p.37](https://agentii.ai/v/SATS/sec85/37)).

**Pre-close / post-close, stated for every figure.** Every competitive figure in this artifact is
**`standalone_pre_merger`**, and the basis is on the face of the filings: the licence table still
carries every transaction-subject licence family at 2026-03-31, so **nothing has closed**; the
only completed step is a **lease**. The competitive set's **membership does not change on
close** — but the **role** of two of its members does, from single-role to multi-role, and the
**spectrum asset itself leaves the balance sheet**. Therefore: **every share figure computed on
the spectrum base, and every growth figure spanning the close, must state pre/post basis or it
is comparing two different entities.** That is P11, and it is not discharged by a tag alone.

**A25 compliance, recorded.** No figure in this artifact is sourced from a linkbase `LABEL`.
Every value quoted as filed is quoted as a **cell**; every value this artifact computed is
labelled **DERIVED** and its arithmetic shown. Specifically: the licence-table component sum
(§F3, below), the 86.7% and 80.65% ratios, the 3.97× and 0.32× VSAT ratios, the residual VSAT
quarter 1,171,288, and the transaction-subject carrying sum **19,284,585 thousand** are **all
DERIVED** — that last one is a *carrying-amount* sum, not consideration, and it is **not** the
same quantity as any headline transaction value.

---

## §8 The PIL-6 proxy, tied out (F3), and one refinement to 001's arithmetic

The adopted 006 proxy is [sec121 p.46](https://agentii.ai/v/SATS/sec121/46). Its component
identity **closes exactly**, and it is **not vacuous** — eleven licence families, each
independently disclosed, plus three non-zero aggregates:

| Component | thousands |
|---|---|
| SpaceX Transactions block — AWS-4 1,928,688 + H Block 1,671,506 + AWS-3 2,035,433 | 5,635,627 |
| AT&T Transactions block — 600 MHz 6,449,578 + 3.45–3.55 GHz 7,199,380 | 13,648,958 |
| Remaining families — DBS 677,409; 700 MHz 701,803; MVDDS 24,000; LMDS 0; 28 GHz 2,883; 24 GHz 11,772; 37/39/47 GHz 202,392; 3550–3650 MHz 912,200; 3.7–3.98 GHz 2,969; 1695–1780/2155–2180 MHz 972; AWS-3 7,793,854 | 10,330,254 |
| **Subtotal (served)** | **29,614,839** |
| Capitalized interest (served) | 10,270,436 |
| Impairment of indefinite-lived intangible assets (served) | (5,334,473) |
| **Total as of March 31, 2026 (served)** | **34,550,802** |

5,635,627 + 13,648,958 + 10,330,254 = **29,614,839** ✓ exactly as served.
29,614,839 + 10,270,436 − 5,334,473 = **34,550,802** ✓ exactly as served.

**This independently reproduces the established fact that the licences REMAIN ON THE BALANCE
SHEET at $34,550,802 thousand at 2026-03-31**, and it does so from components rather than by
reading the total — so the fact is now *derived*, not merely *reported*, and it survives a
component-identity cross-check. The transaction-subject carrying sum is **19,284,585 thousand
(DERIVED)**.

**Refinement to 001, recorded — not a rewrite.** The established correction is that `$19.6B`
reproduces arithmetically but must be re-graded `DERIVED`, and that its `$2.6B` is 15 MHz of
AWS-3. On this table the SpaceX-block **AWS-3 carrying amount is 2,035,433 thousand** — not
`$2.6B` — and AWS-4/H-Block are 1,928,688 and 1,671,506. **So `$2.6B` is not the carrying amount
of that AWS-3 block.** Either `$2.6B` is measured on a different basis (MHz-POP, or
consideration) or it belongs to a different block. **This artifact does not assert which.** It is
recorded as a **DA-30 two-bases-on-one-concept hazard**: a single "AWS-3" token carrying more
than one measure, where the served filing gives carrying amount and the circulating figure gives
something else. Stated as a refinement and not a contradiction, because the two measures are not
required to agree.

**And the `$27B` does not reproduce here either** — consistent with the established fact.

---

## §9 Corrections to 001 (recorded; 001 is frozen and is not rewritten)

1. **PIL-6's `reference mark` is not supported by SATS's filings.** 001's PIL-6 reference mark
   reads *"\$19.6B for AWS-4, H-Block and AWS-3 spectrum, FCC-approved with the spectrum transfer
   closed."* §8 shows the transaction-subject licences are **still at carrying amount on SATS's
   own books at 2026-03-31** and that the only completed step is a **short-term spectrum manager
   lease**. **"the spectrum transfer closed" is REFUTED** at SATS. This is the same finding the
   risk artifact records, reached here from the licence table rather than the notes.
2. **"Spectrum gains" is REFUTED.** The Q3 2025 \$16.6B event is a **NON-CASH 5G-NETWORK
   IMPAIRMENT CHARGE**, and the Q1 2026 movement is a **66,159 thousand credit** from settlement
   of exit and disposal costs — §7 confirms the sign twice over. There is no spectrum gain in
   either period.
3. **PIL-6's premise is testable and `DEMONSTRATED`; only its falsifier is unreachable.** This is
   consistent with 001's own thesis and is restated here because the competitive frame makes it
   concrete: SATS's wireless segment carries a **spectrum asset of 34,550,802 thousand** — about
   **9.4× the BSS segment's annualised revenue** (329,656 × 4 = 1,318,624) and **1.8× SATS's own
   annual revenue** — while operating on a **−3.7% Wireless operating margin** and a **13.4% BSS
   operating margin that is 86.7% D&A relief**. The scarcity claim's *substance* is visible in
   the filings. The *allocation test* is not.
4. **001's `wrong_if` source pair is the right pair and both halves are platform-unreachable.**
   `FCC_IBFS` and `ITU_Space_Network_List` are named as sources in 001 from the start; the
   platform ingests neither, and no surrogate in the corpus substitutes for the grant chain
   (§F2).
5. **New: 001's competitor framing cannot be evaluated for its own subject's largest segment.**
   See §1. This is an addition to 001's PIL-6 evidence base, not a contradiction of it.

---

## §10 What could NOT be verified, and why

| Item | Status | Why | Named resolver |
|---|---|---|---|
| Any grant chain, for any firm | `UNRESOLVABLE-FROM-PLATFORM` | FCC IBFS / ULS and the ITU Space Network List are not ingested source types | Ingest FCC IBFS/ULS; ingest ITU SNL |
| Any market-share figure | `UNRESOLVABLE-FROM-PLATFORM` | denominator class (industry aggregates) not ingested | CTIA / Leichtman / Nielsen / SNL Kagan |
| Wireless comparator facts | `UNRESOLVABLE-FROM-PLATFORM` | VZ, T, TMUS return `TICKER_NOT_FOUND`; CHTR, CMCSA at 14% | Ingest the comparators |
| Quarterly comparator benchmark vs VSAT | `REACHABLE-BUT-NOT-RECORDABLE` | Q1 slot carries the twelve-month value; one row is internally inconsistent across concepts | Repair comparison-side fiscal-period labelling (DA-26/DA-27) |
| Component identity on VSAT | **`UNEXERCISED`** — not `CLEAN` | `operating income = revenue − opex` does not close from served concepts; may be a missing tag, not a defect | Read VSAT's filed income-statement page |
| Cause of the BSS D&A halving (−52.4%) | **`UNEVIDENT`** | Not established on any page read; impairment, useful-life change and asset transfer are all consistent with the arithmetic | Read the 10-Q D&A note and the FY2025 property/impairment notes |
| Entrant universe completeness | `UNRESOLVABLE-FROM-PLATFORM` | Enumerable only from a licensee registry | FCC licensee registry |
| PIL-6 kinds 3, 4 and 6 | **`UNEXERCISED`** | No competitive-frame instance reached | — |
| `get_segment_data(SATS, business_unit)` | **PLATFORM ERROR** | Returns `column "k" does not exist` — an internal SQL failure, not a "no data" answer. Every segment figure in this artifact was therefore read from the filed pages instead, which is the stronger route | File as a platform defect; do not read the error as absence |
| `get_ticker_coverage` as an absence test | **NON-DISCRIMINATING** | It reports `missing`/14% for tickers that are genuinely absent **and** reports `sec_filings` count 0 for VSAT, whose 10-Q and 10-K facts are demonstrably present. A zero from this view is evidence about the view | Use `search_xbrl_facts` / `get_company_financials`; a registry error (`TICKER_NOT_FOUND`) is the stronger absence signal |

---

## §11 Carry-forwards

- **C1.** A18's mechanical tie-out returns **CLEAN and is not sufficient**. Add the
  *period-over-period composition* detector (§5b) to A18, because the eliminations line is the
  only place a within-perimeter boundary move is visible, and the tie-out cannot see it.
- **C2.** **A12's mandate extends to the validator, not just to the identity checks.** The
  `2 ×` fingerprint on VSAT (§4a) makes the `validate_calculation` instrument a
  both-sides finding. Phase 6 should run it on every comparator in every comparison artifact.
- **C3.** **New validator failure mode candidate for the amendment queue:** consolidated-scope
  computation compared against a segment-column fact under the consolidated concept (§4b). The
  mechanism is dimension-blind joining, which segment tables trigger everywhere.
- **C4.** **`REACHABLE-BUT-NOT-RECORDABLE` is real and its remedy is a label repair.** §4c.
  A22 should record that the third case can arise from a *served-label* defect on the comparison
  side, not only from a subject-side one.
- **C5.** **The competitor set is a PIL-6 blocker in its own right** (F1), with a remedy distinct
  from F0's. The risk census merges them under one row; they should not be merged.
- **C6.** **The market-share denominator is a distinct datum class** (F5) and should be an
  explicit line in the 002 reachability census, because PIL-7's `wrong_if` counts falsifiers
  *without a named resolving source* — and this one has a name that no other artifact has yet
  written down.
- **C7.** **The taxonomy node does not bound the comparator set.** GSAT sits under
  `tech.tech_hardware`; a node-keyed comparator query silently drops the 001-pinned
  `GSAT × competitive` leg.
- **C8.** **Read the decoys, and read them from the right root.** §frontmatter. The four
  `packaging/targets` trees are real, are the *only* place a skill pin can be checked against a
  shipped artifact, and are invisible to a `find` rooted at the marketplace install because
  `.gitignore:18` excludes them. Two agents in this phase reported them absent. **They are not
  absent; they are elsewhere.**

---

## Sources

> Every figure asserted above resolves to the page cited; the pages were located by the tool
> named in each entry's `located_via`. Values quoted from a table are quoted as that table's
> cells. Values this artifact computed are labelled DERIVED in the body.

| Figure | Source |
|---|---|
| BSS competition — ViaSat, SpaceX/Starlink, Gilat Satellite Networks, ST Engineering iDirect; 5G Network terminated Aug 2025; over $30 billion invested in spectrum licenses | [📄 SATS 10-K p.22](https://agentii.ai/v/SATS/sec85/22) |
| Competition and Economic Risks; SpaceX as a potential minority, non-controlling investment | [📄 SATS 10-K p.37](https://agentii.ai/v/SATS/sec85/37) |
| Wireless incumbents Verizon, AT&T, T-Mobile each with substantial market share | [📄 SATS 10-K p.40](https://agentii.ai/v/SATS/sec85/40) |
| Dependence on T-Mobile (MNSA) and AT&T (NSA, Amended NSA); minimum commitments | [📄 SATS 10-K p.42](https://agentii.ai/v/SATS/sec85/42) |
| Pay-TV segment, 6.998M subscribers at 2025-12-31; pay-TV competition and retention costs | [📄 SATS 10-K p.85](https://agentii.ai/v/SATS/sec85/85) |
| Wireless segment, 7.511M subscribers at 2025-12-31; named competitor and MVNO brand list | [📄 SATS 10-K p.95](https://agentii.ai/v/SATS/sec85/95) |
| BSS segment FY2025 — contracted backlog ~$1.4 billion at 2025-12-31; competition | [📄 SATS 10-K p.102](https://agentii.ai/v/SATS/sec85/102) |
| Wireless spectrum licence table at 2026-03-31 — components, subtotal 29,614,839, capitalized interest 10,270,436, impairment (5,334,473), total 34,550,802; AT&T short-term spectrum manager lease | [📄 SATS 10-Q p.46](https://agentii.ai/v/SATS/sec121/46) |
| Segment note Q1 2026 — the Eliminations column; Other impairments and other (66,159); Other D&A 11,305 | [📄 SATS 10-Q p.71](https://agentii.ai/v/SATS/sec121/71) |
| Segment note Q1 2025 — intersegment revenue 71,592 (Other 60,234); Other connectivity services 343,080; consolidated D&A 488,333 | [📄 SATS 10-Q p.72](https://agentii.ai/v/SATS/sec121/72) |
| Segment revenue and operating income, Q1 2026 vs Q1 2025, all five columns and the total | [📄 SATS 10-Q p.89](https://agentii.ai/v/SATS/sec121/89) |
| Pay-TV segment at 2026-03-31 — 6.632M subscribers (4.845M DISH TV, 1.787M SLING TV) | [📄 SATS 10-Q p.90](https://agentii.ai/v/SATS/sec121/90) |
| Pay-TV metrics — DISH TV gross activations 32,000 vs 46,000; churn 1.41% vs 1.36%; ESPN Unlimited and FOX One | [📄 SATS 10-Q p.94](https://agentii.ai/v/SATS/sec121/94) |
| Wireless segment, 7.527M subscribers at 2026-03-31; Hybrid MNO; MNO competitor paragraph | [📄 SATS 10-Q p.97](https://agentii.ai/v/SATS/sec121/97) |
| BSS competition in the 10-Q — backlog ~$1.4 billion at 2026-03-31; "Amazon Leo when launched" | [📄 SATS 10-Q p.100](https://agentii.ai/v/SATS/sec121/100) |
| BSS results of operations — revenue 329,656 vs 370,658; SG&A 62,290 vs 90,096 (SAC 28,389 vs 46,432); D&A 49,940 vs 104,898; operating income 44,184 vs (19,195); OIBDA 94,124 vs 85,703; broadband subscribers 0.681M vs 0.853M | [📄 SATS 10-Q p.101](https://agentii.ai/v/SATS/sec121/101) |
| Segment Adjusted OIBDA reconciliation — OIBDA 559,448, Adjusted OIBDA 493,289; Other OIBDA (75,990) vs Adjusted OIBDA (142,149) | [📄 SATS 10-Q p.108](https://agentii.ai/v/SATS/sec121/108) |
