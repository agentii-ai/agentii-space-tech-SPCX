---
# 002 / Phase 5 / T096–T098 — pillar PIL-7 (falsifier reachability), ticker SATS.
# ONE artifact, two jobs: (1) DA-24 contamination scoping at SATS; (2) classification of
# 001's six falsifiers against the disposition classes with a NAMED resolving source each.
thesis_id: "002-evidence-validation"
pillar: PIL-7
ticker: SATS
skill: risk
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
# Written at 1.5.0, not grandfathered: the register gained DA-29 (defective checks — the
# circularity test) and DA-30 (a basis collapsed before an artifact sees it) at 002 Phase 3,
# and both are load-bearing here. §4, §5 and §6 discharge those two obligations in full.
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
      Sign stripping — a served magnitude with the filed sign discarded. At SATS this is not
      sporadic: every loss period of us-gaap:OperatingIncomeLoss is served as a POSITIVE
      magnitude (FY2025 +17,723,146,000 against a filed (17,723,146)), and the single
      sats:AssetImpairmentChargesAndOther tag serves a filed-positive instance correctly
      (+17,632,011 -> +17,632,011,000) and a filed-negative instance stripped ((66,159) ->
      +66,159,000) inside the same series. A clearance that has never exhibited a
      negative-filed instance is UNEXERCISED, not clean.
  - da_id: DA-24
    chosen_reading: >
      Non-operating contamination of the operating line, in EITHER direction — the definition
      names a gain AND a charge, and VRT supplied the charge case at a $62.0M contingent
      consideration. At SATS the founding instance is a non-cash 5G-Network IMPAIRMENT CHARGE
      of 16,481,468 thousand (Q3 2025) plus 1,150,543 thousand (Q4 2025), and the most recent
      instance runs the other way: a 66,159 thousand CREDIT from gains on the settlement of
      estimated exit, disposal and other costs related to the termination of the 5G Network
      deployment (Q1 2026).
  - da_id: DA-26
    chosen_reading: >
      An annual-basis fact served where a quarterly label is asserted; SATS is one of the
      19-of-19 issuers in the register. Every FY figure here is labelled FY and taken from the
      10-K, and no FY fact is used as a stand-in for a quarter — Q4 2025 is DERIVED as FY minus
      9M, is labelled as derived, and is decomposed to the note that produces it.
  - da_id: DA-27
    chosen_reading: >
      Calendar-derived fiscal labels. SATS is a December-year-end issuer, and is therefore an
      instance of the MECHANISM-POPULATION identity: the sample is defined by the mechanism's
      own property and carries no information about the remainder. This is why PIL-3's
      19-issuer risk-factor test cannot be advanced by adding more December issuers.
  - da_id: DA-28
    chosen_reading: >
      IPO capital-structure discontinuity. At SATS the test is whether any served period
      contains a listing event, and the answer is NO. That is a GENUINE ABSENCE from the
      source — not an ingestion gap — which is what places PIL-4 in
      UNRESOLVABLE-FROM-PUBLIC-SOURCES rather than on a re-run list.
  - da_id: DA-29
    chosen_reading: >
      Back-solved or opaque checks: a reconciliation whose terms cannot all be located in the
      source, and instruments whose reported/computed columns are not the filed values. SATS
      supplies both a tree-vs-store term failure (sats:InterestExpenseNetOfAmountCapitalized is
      named in the Q1 2026 calculation linkbase as a term of the non-operating identity and
      serves zero facts) and a demonstrated validator incapacity (validate_calculation returns
      status pass on ProfitLoss while the filing prints the loss in parentheses).
  - da_id: DA-30
    chosen_reading: >
      Two competing bases under one concept. Beyond the register's BWXT instance, SATS supplies
      a fifth instance at the SEGMENT level: the Q3 2025 charge is presented under Wireless
      16,199,344 + Broadband and Satellite Services 282,124 in the 10-Q (whose segment table
      has no Other column), while FY2025 Impairments and other is presented as BSS 1,529,982 +
      Other 16,102,029 with Wireless zero in the 10-K. Only a 97,315 thousand Q4 reversal
      separates the two presentations and there is no restatement note.
evidence_grade: DEMONSTRATED
# P11. SATS is a deal security on the transaction fact even though the checker's
# DEAL_SECURITIES set is {IRDM, GSAT, RKLB}. Basis: BOTH purchase agreements are PENDING at
# 2026-03-31 (sec85 p.36: closing conditions "none of which have been satisfied yet"), the
# licences remain on SATS's balance sheet (sec121 p.46: net spectrum 34,550,802 thousand), and
# no gain has been recognised on either transaction. Nothing has closed, so the standalone
# pre-merger basis is the only admissible one.
deal_security_basis: standalone_pre_merger
unresolvable: false
citations:
  - figure: "Q1 2026 condensed consolidated statements of operations, cells: revenue 3,667,489 / 3,869,758; operating income (loss) 392,847 / (88,132)"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 11
    url: https://agentii.ai/v/SATS/sec121/11
    located_via: read_source_pages
  - figure: "Note on the SpaceX Transactions, cells/text: Seller Notes outstanding at March 31, 2026 $9.821 billion, 'secured by the AWS-4 and AWS-3 Licenses'; Equity Amount 'up to $8.5 billion ... in SpaceX's Class A Common Stock, valued at $212 per share'; Spectrum Acquisition Closing 'expected to occur on or about November 30, 2027'; Interim Debt Service 'approximately $2 billion'; '$414 million in cash interest payments' made"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 16
    url: https://agentii.ai/v/SATS/sec121/16
    located_via: read_source_pages
  - figure: "Note on the Amended SpaceX Transactions, cells/text: AWS-3 addition of 'up to an aggregate of 15 MHz of AWS spectrum in the frequency range of 1695-1710 MHz' for 'additional consideration of $2.6 billion ... paid in SpaceX's Class A Common Stock, valued at $212 per share'; total consideration 'increased from $17 billion to approximately $20 billion, with up to $11 billion to be paid in SpaceX's Class A Common Stock'"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 17
    url: https://agentii.ai/v/SATS/sec121/17
    located_via: read_source_pages
  - figure: "Note on the AT&T transaction: purchase price of '$22.650 billion' in cash on closing"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 18
    url: https://agentii.ai/v/SATS/sec121/18
    located_via: read_source_pages
  - figure: "Spectrum licence table, cells: per-band gross balances 1,928,688 + 1,671,506 + 2,035,433 + 6,449,578 + 7,199,380 + 677,409 + 701,803 + 24,000 + 0 + 2,883 + 11,772 + 202,392 + 912,200 + 2,969 + 972 + 7,793,854 = 29,614,839; less accumulated amortisation/impairment 5,334,473; net spectrum assets 34,550,802"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 46
    url: https://agentii.ai/v/SATS/sec121/46
    located_via: read_source_pages
  - figure: "Other segment results, cells: depreciation and amortisation 11,305 / 303,929 (variance (292,624), (96.3)%); impairments and other (66,159) / -; total costs and expenses 178,278 / 690,707; operating income (loss) (87,295) / (628,410); purchases of property and equipment 4,864 / 163,936"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 104
    url: https://agentii.ai/v/SATS/sec121/104
    located_via: read_source_pages
  - figure: "MD&A text: D&A 'primarily driven by no depreciation expense for the 5G Network assets impaired during the third quarter of 2025'; 'Impairments and other' of '$66 million ... primarily related to gains on the settlement of our estimated exit, disposal and other costs'; SG&A increase 'mainly due to RSA Settlement costs of $50 million'"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 105
    url: https://agentii.ai/v/SATS/sec121/105
    located_via: read_source_pages
  - figure: "Part II Item 1A Risk Factors: a two-line statement that Item 1A of the FY2025 Form 10-K 'includes a detailed discussion of our risk factors' — no refreshed risk factor for the Q1 2026 period; Item 3 market risk: 'no material changes'"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 118
    url: https://agentii.ai/v/SATS/sec121/118
    located_via: read_source_pages
  - figure: "Q3 2025 condensed consolidated statements of operations, cells: total revenue 3,614,258; total costs and expenses 20,256,133; operating income (loss) (16,641,875)"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec120
    page_no: 10
    url: https://agentii.ai/v/SATS/sec120/10
    located_via: read_source_pages
  - figure: "Q3 2025 impairment note, cells: components of the charge 391,972 + 5,409,517 + 5,682,226 + 4,191,133 + 806,620 = 16,481,468"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec120
    page_no: 19
    url: https://agentii.ai/v/SATS/sec120/19
    located_via: read_source_pages
  - figure: "Q3 2025 segment table, cells: Impairments and other - Pay-TV - / Wireless 16,199,344 / Broadband and Satellite Services 282,124 / Eliminations - / Consolidated Total 16,481,468; OIBDA (16,250,584); depreciation and amortisation 391,291; total costs and expenses 20,256,133; operating income (loss) (16,641,875) (no Other column presented)"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec120
    page_no: 75
    url: https://agentii.ai/v/SATS/sec120/75
    located_via: read_source_pages
  - figure: "Item 1A text: the closing conditions 'none of which have been satisfied yet'; completion not assured 'on the terms or timeline currently contemplated, or at all'; the two transactions are not contingent on each other"
    ticker: SATS
    form_type: 10-K
    citation_id: sec85
    page_no: 36
    url: https://agentii.ai/v/SATS/sec85/36
    located_via: read_source_pages
  - figure: "Item 1A text on the SpaceX investment: minority non-controlling position; the 'absence of a public market for its shares'; 'subjective valuation methodologies'"
    ticker: SATS
    form_type: 10-K
    citation_id: sec85
    page_no: 37
    url: https://agentii.ai/v/SATS/sec85/37
    located_via: read_source_pages
  - figure: "Item 1A text on the impairment trigger: the FCC's 'unequivocal position' and the pivot 'to selling certain wireless spectrum licenses'"
    ticker: SATS
    form_type: 10-K
    citation_id: sec85
    page_no: 39
    url: https://agentii.ai/v/SATS/sec85/39
    located_via: read_source_pages
  - figure: "Segment tables, cells: FY2025 Impairments and other - Pay-TV - / Wireless - / Broadband and Satellite Services 1,529,982 / Other 16,102,029 / Eliminations - / Consolidated Total 17,632,011, with FY2025 segment operating income (loss) 2,425,228 + (495,028) + (1,607,404) + (18,047,900) + 1,958 = (17,723,146); FY2024 Impairments and other all '-' and segment operating income (loss) 2,647,954 + (477,991) + (117,901) + (2,353,915) + (2,217) = (304,070); FY2023 Impairments and other 6,457 + 98,657 + 536,082 + 119,903 = 761,099 and segment operating income (loss) 2,699,810 + (643,184) + (458,609) + (1,881,369) + 5,443 = (277,909)"
    ticker: SATS
    form_type: 10-K
    citation_id: sec85
    page_no: 114
    url: https://agentii.ai/v/SATS/sec85/114
    located_via: read_source_pages
  - figure: "FY2025 consolidated statements of operations, cells: total revenue 15,004,989; total costs and expenses 32,728,135; operating income (loss) (17,723,146)"
    ticker: SATS
    form_type: 10-K
    citation_id: sec85
    page_no: 150
    url: https://agentii.ai/v/SATS/sec85/150
    located_via: read_source_pages
  - figure: "Impairments and other note, cells (FY2025): Prepaids and other 5,211 + 393,211 = 398,422; Regulatory authorizations 450,306 + 5,334,473 = 5,784,779; Property and equipment, net 969,128 + 5,487,286 = 6,456,414; Operating lease assets 66,591 + 4,191,133 = 4,257,724; Exit and disposal costs 38,746 + 747,642 = 786,388; (Gains) losses on costs paid or settled (51,716); Total 1,529,982 + 16,102,029 = 17,632,011. (FY2023): Goodwill 6,457 + 98,657 + 532,491 + 119,903 = 757,508 and Property and equipment, net 3,591; Total 761,099. Note 1: a $1.284 billion ROU asset and liability remeasurement and a 'one-time charge for variable lease payment expense ... of $457 million' in the third quarter of 2025"
    ticker: SATS
    form_type: 10-K
    citation_id: sec85
    page_no: 160
    url: https://agentii.ai/v/SATS/sec85/160
    located_via: read_source_pages
key_metrics:
  impairment_charge_thousands: 16481468
  da24_items_contaminated: 5
  da24_items_clean: 10
  second_order_improvement_share_pct: 80.6

---

# SATS — risk & reachability methodology (PIL-7)

## Headline

Two jobs, and the second is the one PIL-7 exists for.

**Job 1 — the DA-24 contamination scope.** The contaminant at SATS is a **non-cash 5G-Network
impairment charge**, not a sale and not a gain. The founding instance is
**16,481,468 thousand** in Q3 2025 (Wireless 16,199,344 + Broadband and Satellite Services
282,124, per the segment table at [sec120 p.75](https://agentii.ai/v/SATS/sec120/75)), with a
further **1,150,543 thousand** in Q4 2025 — **17,632,011 thousand** for FY2025. The most recent
instance runs the **other way**: Q1 2026 carries a **66,159 thousand credit** from gains on the
settlement of estimated exit and disposal costs. Of **15 filed operating-income values verified
against the statements, 5 are contaminated and 10 are not**, and the contamination runs in both
directions. The largest single restatement of a period margin is Q3 2025: **filed (460.46)% →
(4.44)% ex-item**, a **456.0 percentage-point** swing; FY2025 goes **(118.11)% → (0.61)%**.

**The co-occurrence.** DA-24's item and DA-23's strip live inside one figure. The credit is
*filed* as `(66,159)` and *served* as `+66,159,000`. The correct ex-item operating income is
392,847 − 66,159 = **326,688**; a reader who de-contaminates using the served fact computes
392,847 + 66,159 = **459,006**. The de-contamination therefore **doubles** the sign error
instead of removing it, and the error is **2 × 66,159 = 132,318 thousand = 3.61% of Q1 2026
revenue**.

**Job 2 — the classification.** Six falsifiers, **six classified, six with a named resolving
source** — PIL-7's `wrong_if` metric is **0**. **Two are structurally unreachable**
(PIL-4 `UNRESOLVABLE-FROM-PUBLIC-SOURCES`, PIL-6 `UNRESOLVABLE-FROM-PLATFORM`) and one more is
platform-blocked for a licensed dataset (PIL-5). **One is reachable but not recordable**
(PIL-2) and is flagged as a distinct situation rather than folded into a class. **PIL-3 is
reachable and is not blocked by reachability at all** — its blocking condition is effort, and
I read SATS's Item 1A on the platform to prove it.

## Register version note

Written at `constitution_pin: 1.5.0`, not grandfathered. Two obligations that 1.5.0 added are
discharged in full here: **DA-29** (defective checks) in §5, and **DA-30** (a basis collapsed
before an artifact sees it) in §1.5 and §3. The predecessor artifact
(`2026-09-18_1500_recent-quarter_methodology.md`, `skill_pin 07d26b9c738b`) is the template for
structure and pin discipline; this artifact does not repeat its questions, it uses its verified
component identities and extends them.

## Inheritance from 001 and from the SATS recent-quarter artifact

001 is **frozen** and is not rewritten. This artifact **validates its facts** and records
corrections (§7). Inherited without re-litigation: the eight component identities of the recent
quarter artifact (now extended to 15 filed operating-income values), the articulation and
overshoot detectors, the `validate_calculation` incapacity, the extension-tag gap, and the
`tmb-` / `sats-` source-file-stem hazard. New here: the **scope** of DA-24 across every period
001 and 003 quote, the **weight discriminator applied at SATS** (§3), the **two-sided
articulation firing** (§4), the **tree-vs-store term failure** (§5), and the **classification
census** (§2).

## Summary verdicts

| Question | Verdict |
|---|---|
| Is there a spectrum gain in any served period? | **No.** A 17,632,011 thousand charge was recognised. "Spectrum gains" is **REFUTED**; the licences are still on the balance sheet at 34,550,802 thousand ([sec121 p.46](https://agentii.ai/v/SATS/sec121/46)). |
| What contaminates the operating line? | A 5G-Network impairment **charge** (Q3/Q4 2025, FY2023, FY2025) and a settlement **credit** (Q1 2026). Both directions. |
| Can the strip be detected from served data? | **Yes** — the articulation detector fires at **exactly 132,318 = 2 × 66,159** (§4). |
| Does `validate_calculation` detect it? | **No, and it cannot.** It returns `pass` while the filing prints the loss in parentheses (§5). |
| How many falsifiers lack a class or a named source? | **0 of 6.** |
| How many are structurally unreachable? | **2 of 6** (PIL-4, PIL-6), plus 1 platform-blocked (PIL-5). |

## 1. Job 1 — DA-24 contamination scoping

### 1.1 The contaminant, identified from filed cells

The founding instance is inside the operating line, in a caption that sits **above** operating
income and **below** D&A:

> `Impairments and other | — | 16,199,344 | 282,124 | — | 16,481,468`
> — the Q3 2025 segment table, consolidated column, at [sec120 p.75](https://agentii.ai/v/SATS/sec120/75)

The same page closes the identity with the charge **in**: total costs and expenses
20,256,133 = cost of services 2,370,363 + cost of sales 391,524 + SG&A 621,487 + impairments
16,481,468 + D&A 391,291, and revenue 3,614,258 − 20,256,133 = **(16,641,875)** = filed
operating income. Verified against the statement face at
[sec120 p.10](https://agentii.ai/v/SATS/sec120/10) and decomposed in the impairment note at
[sec120 p.19](https://agentii.ai/v/SATS/sec120/19) as
391,972 + 5,409,517 + 5,682,226 + 4,191,133 + 806,620 = **16,481,468** (exact).

The FY2025 note at [sec85 p.160](https://agentii.ai/v/SATS/sec85/160) gives the composition of
the full-year charge, and it settles the single most important scoping question for the
spectrum thesis:

| Asset class (FY2025) | Broadband & Satellite Services | Other | Total |
|---|---|---|---|
| Prepaids and other | 5,211 | 393,211 | 398,422 |
| **Regulatory authorizations** | 450,306 | 5,334,473 | **5,784,779** |
| Property and equipment, net | 969,128 | 5,487,286 | 6,456,414 |
| Operating lease assets | 66,591 | 4,191,133 | 4,257,724 |
| Exit and disposal costs | 38,746 | 747,642 | 786,388 |
| (Gains) losses on costs paid or settled | — | (51,716) | (51,716) |
| **Total impairments and other** | **1,529,982** | **16,102,029** | **17,632,011** |

Only **5,784,779 of 17,632,011 (32.8%)** struck regulatory authorisations — the spectrum
licences. The remaining **11,847,232 (67.2%)** struck prepaids, PP&E, ROU assets and exit
costs. **A thesis that reads the 17,632,011 as a spectrum write-down over-reads it by
11,847,232 thousand.** (This corrects a scoping figure recorded earlier in this phase as
12,297,538; the filed columns are 11,847,232 and the difference is the BSS-labelled
regulatory-authorisation line, 450,306.) Footnote 1 on the same page quantifies a further
component: a **$1.284 billion** ROU asset and liability remeasured in Q3 2025, producing a
"one-time charge for variable lease payment expense ... of **$457 million**".

### 1.2 The contamination scope table

Contaminated = a DA-24 item is inside the operating line. All values in thousands, as filed.
Margins are `operating income ÷ revenue` for the same period; parentheses are filed negatives.

| Period | Filed operating income | DA-24 item inside the operating line | Ex-item operating income | Filed margin | Ex-item margin | Δ (pts) |
|---|---|---|---|---|---|---|
| FY2023 | (277,909) | 761,099 charge | **+483,190** | (1.63)% | **+2.84%** | +4.47 |
| FY2024 | (304,070) | — | (304,070) | (1.92)% | (1.92)% | 0 |
| Q1 2024 | (15,244) | — | (15,244) | — | — | 0 |
| Q2 2024 | (65,369) | — | (65,369) | — | — | 0 |
| Q3 2024 | (160,767) | — | (160,767) | — | — | 0 |
| Q1 2025 | (88,132) | — | (88,132) | (2.28)% | (2.28)% | 0 |
| Q2 2025 | (213,408) | — | (213,408) | (5.73)% | (5.73)% | 0 |
| Q3 2025 | (16,641,875) | 16,481,468 charge | **(160,407)** | (460.46)% | **(4.44)%** | +456.02 |
| Q4 2025 *(derived)* | (779,731) | 1,150,543 charge | **+370,812** | (20.54)% | **+9.77%** | +30.31 |
| FY2025 | (17,723,146) | 17,632,011 charge | **(91,135)** | (118.11)% | **(0.61)%** | +117.50 |
| Q1 2026 | 392,847 | (66,159) **credit** | **326,688** | +10.71% | **+8.91%** | −1.80 |

Q4 2025 is derived as FY2025 minus 9M 2025 (17,723,146 − 16,943,415 = 779,731) and its
contaminant as 17,632,011 − 16,481,468 = 1,150,543; the derived quarter closes on the sum
(88,132) + (213,408) + (160,407) + 370,812 = **(91,135)** = FY2025 ex-item operating income.
The Q3 2025 ex-item result, (160,407), is within 361 thousand of Q3 2024's filed (160,767) —
i.e. **once the charge is removed, SATS's wireless operating performance in the two quarters is
the same to within 0.2%**, which is the strongest single statement of what the charge did to
the series.

### 1.3 First-order and second-order contamination

The charge is a level shift, and the definition's "contamination" obligation is not discharged
by adding it back. The same event flows through the operating line in **three** places:

1. **The charge/credit itself** (first-order, quantified in §1.2).
2. **D&A relief** (second-order, not removable by an add-back). The Other segment's D&A fell
   from 303,929 to 11,305 — **(292,624), (96.3)%** ([sec121 p.104](https://agentii.ai/v/SATS/sec121/104)) —
   and MD&A attributes it explicitly: "This change was primarily driven by **no depreciation
   expense for the 5G Network assets impaired during the third quarter of 2025**"
   ([sec121 p.105](https://agentii.ai/v/SATS/sec121/105)). The Q1 2026 vs Q1 2025 bridge closes
   exactly at **+480,979** (= the filed OI swing from (88,132) to 392,847), of which the DA-24
   effects contribute **+321,732 (D&A) + 66,159 (credit) = +387,891 = 80.6% of the entire
   year-over-year improvement**. The D&A relief is a **permanent** level shift: the assets are
   impaired, so there is no depreciation to add back.
3. **The accretion tail** (second-order, disclosed as forward-looking). "We expect the
   accretion for these liabilities to **continue prospectively**" — the exit, disposal and lease
   liabilities accrete and are charged ([sec121 p.104](https://agentii.ai/v/SATS/sec121/104)).

**Consequence for 001 and 003:** an ex-item series that adds back only the charge will still
show a flattered FY2026 margin. The correct ex-item Q1 2026 figure (326,688) is already
*lower* than the filed figure; the D&A relief keeps flowing and cannot be normalised away.

There is also a **disclosed one-time item in the same quarter**: SG&A rose 14.4% "mainly due to
**RSA Settlement costs of $50 million**" ([sec121 p.105](https://agentii.ai/v/SATS/sec121/105)).
Removing both the credit and that charge gives 392,847 − 66,159 + 50,000 = **376,688**, a margin
of **+10.27%**. That normalisation is **DERIVED** (two disclosed one-time items, both located),
and it is offered as a sensitivity, not as the headline: 003 may legitimately decline to
normalise legal settlements.

### 1.4 DA-23 and DA-24 co-occur inside one figure — which is which

This is the case the register names ("At SATS the two co-occur inside one figure"), and the
scoping must say which is which so that neither masks the other.

| | DA-24 (composition) | DA-23 (sign) |
|---|---|---|
| What it is | the `(66,159)` credit is a non-operating/non-recurring item inside operating income | the same `(66,159)` cell is served as `+66,159,000` |
| Where it lives | sec121 p.104 (segment table), p.105 (MD&A), p.11 (statement) | the XBRL fact store, tag `sats:AssetImpairmentChargesAndOther`, `source_file sats-20260331x10q.htm` |
| Who sees it | anyone reading the filing | anyone querying the platform and NOT reading the filing |
| Correct treatment | **subtract** it from operating income: 392,847 → 326,688 | **restore the negative** before any arithmetic |
| Wrong treatment | ignore it: 392,847 | use the served value: 392,847 + 66,159 = 459,006 |

The two errors are **independent and additive in magnitude**: ignoring DA-24 leaves a 66,159
overstatement of ex-item operating income; acting on DA-23 while attempting to remove DA-24
produces a 66,159 *under*statement of the true figure plus a 66,159 error in the wrong
direction — a total error of **132,318 = 2 × 66,159 thousand = 3.61% of Q1 2026 revenue**.

The served series proves the strip is sign-blind and not structural. The **same tag**, in the
**same filing family**, serves:

| Period | Filed | Served | Verdict |
|---|---|---|---|
| FY2025 | +17,632,011 | +17,632,011,000 | **correct** (unit scaling thousands → units is exact) |
| Q1 2026 | **(66,159)** | +66,159,000 | **STRIPPED** |

A clearance based on the FY2025 instance would have been *merely clean*; the Q1 2026 instance
**exercises** it and it **fails**. This is the register's directionality rule applied at home:
one series, two verdicts, one tag.

### 1.5 The segment-attribution discontinuity (a fifth DA-30 instance)

The two filings present the same charge under **different segments** with no restatement note:

| Filing | Presentation | Wireless | BSS | Other |
|---|---|---|---|---|
| Q3 2025 10-Q ([sec120 p.75](https://agentii.ai/v/SATS/sec120/75)) | Q3 2025 as incurred | **16,199,344** | 282,124 | *(no Other column)* |
| FY2025 10-K ([sec85 p.114](https://agentii.ai/v/SATS/sec85/114)) | FY2025 as presented | **—** | 1,529,982 | **16,102,029** |

The reconciliation is exact and is a **reclassification, not an error**:
**16,199,344 (Q3 in Wireless) + (−97,315) (Q4 in Other) = 16,102,029 (FY in Other)**. So the
10-K moved 16,199,344 thousand out of the Wireless segment into Other, offset by a 97,315
thousand Q4 reversal, and the segment tables on the two bases both foot: FY2025 segment
operating income sums to (17,723,146) on the 10-K's basis, and the Q3 column sums to
(16,641,875) on the 10-Q's basis. **The platform collapses the two bases under one caption.**
Any artifact quoting "SATS Wireless segment operating loss" must name the basis (Q3-incurred
vs FY-presented) or it is quoting a figure that differs by 16,199,344 thousand between two
filings of the same issuer for the same year.

### 1.6 Risk factors as primary evidence

Item 1A at SATS is not boilerplate for this purpose — it names counterparties, dates and bases.
Read as primary evidence:

- **Closing risk is unresolved, in the filer's own words.** The closing conditions are "**none
  of which have been satisfied yet**"; completion is not assured "on the terms or timeline
  currently contemplated, **or at all**"; and the two transactions are "not contingent on each
  other" ([sec85 p.36](https://agentii.ai/v/SATS/sec85/36)). This is the basis for
  `deal_security_basis: standalone_pre_merger` — nothing has closed.
- **The reciprocal of A1's valuation circularity is disclosed with a counterparty, an amount
  and a basis.** SATS will *receive* SpaceX Class A Common Stock at $212 per share — the Equity
  Amount is "up to $8.5 billion ... valued at $212 per share" ([sec121 p.16](https://agentii.ai/v/SATS/sec121/16)),
  and up to $11 billion of the ~$20 billion total SpaceX consideration is payable in that stock
  ([sec121 p.17](https://agentii.ai/v/SATS/sec121/17)) — while the filer's own risk factors
  disclose the "**absence of a public market for its shares**" and reliance on "**subjective
  valuation methodologies**" ([sec85 p.37](https://agentii.ai/v/SATS/sec85/37)). A valuation
  basis that the issuer itself flags as unobservable is a \(DERIVED\) basis, not a DEMONSTRATED
  one. **Candidate reconciliation, DERIVED and not exact:** 8.5 (p.16) + 2.6 (p.17) = 11.1
  against a filed "up to $11 billion" — consistent within the "up to" language, off by 0.1B,
  and **not** asserted as filed.
- **The impairment's cause is disclosed as a regulatory position, not a market event**: the
  FCC's "**unequivocal position**" and the pivot "**to selling certain wireless spectrum
  licenses**" ([sec85 p.39](https://agentii.ai/v/SATS/sec85/39)). This matters for PIL-6 and
  PIL-4: the disposal route is disclosed, and so is its absence of completion.
- **Disclosure absence, correctly classified.** The Q1 2026 10-Q's Item 1A is a **two-line
  incorporation by reference** to the FY2025 10-K ([sec121 p.118](https://agentii.ai/v/SATS/sec121/118)) —
  and Item 3 market risk likewise says "no material changes". The risk disclosure is therefore
  **10 weeks stale relative to the Q1 2026 result**, and **no refreshed risk factor exists for
  the Q1 2026 period**. This is a third case, distinct from both of 001 §4.4's: (a) a risk
  factor absent because the item is **immaterial to the counterparty** is a finding about the
  counterparty's disclosure policy; (b) a risk factor absent because it is **not disclosed** is
  a finding about this filer; (c) here the item is **not refreshed because the filer elected
  incorporation by reference** — a **period-scoping** fact about the corpus, which is evidence
  of neither suppression nor immateriality, and must not be recorded as either.

## 2. Job 2 — falsifier reachability classification (P6)

### 2.1 The classification vocabulary, stated before use

Two **registered** disposition classes (`check_contract.UCLASSES`), one **proposed** class, one
**flagged situation**, and one non-defect state. Stating this explicitly is required, because
the remedies differ and a verdict without a class is exactly what PIL-7's `wrong_if` counts.

| Label | Meaning | Remedy |
|---|---|---|
| `EVALUABLE` | reachable and evaluated | record the result |
| `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | the disclosure does not exist publicly | **name the specific disclosure and MONITOR** |
| `UNRESOLVABLE-FROM-PLATFORM` | public but unreachable / licensed / external registry | **record a platform-reach gap** |
| `UNVALIDATED-BY-PLATFORM` *(proposed; A5/VRT)* | the concept is filed and the structure exists, but the instrument returns nothing | record an **instrument** gap; validate by another instrument |
| **flag: `REACHABLE-BUT-NOT-RECORDABLE`** | the data is reachable, but the falsifier's *passing* result cannot be recorded as a passing datum | **replace with a recordable predicate** (this is a third situation, not a class — see §2.3) |

**Cross-cutting rules applied throughout:** `processing_status` is **non-discriminating** (IRDM:
all 9 accessions read "pending" including ones that serve facts; SATS: every filing reads
"pending" while all figures are readable; MRCY: 36 filings "pending" and 10 of 10 pages served
full cell-level text) and is **not** used here as an ingestion-absence marker. And every
not-testable **kind** is assigned from the full six, none merged:

| Kind | Definition | Home example |
|---|---|---|
| 1 | Ingestion absence — period returns 0 facts; 10-K `processing_status: pending` | — |
| 2 | **Genuine absence from the source** | SATS DA-28: no listing event in any served period |
| 3 | Validator-completeness — concept present, filed, 7 arcs deep, validator returns zero rows | VRT → `UNVALIDATED-BY-PLATFORM` |
| 4 | Mechanism-population identity — the sample is defined by the mechanism's own property | a December-year-end issuer for DA-27; SATS is such an issuer |
| 5 | Ingestion absence of a DATUM CLASS | IRDM subscriber counts: MD&A prose, never XBRL-tagged |
| 6 | Coverage window — coverage opens after the event | IRDM DA-28: SEC coverage opens 2022-02-17, IPO falls outside |

### 2.2 The six falsifiers, classified

| PIL | 001 state | Class | Kind | Named resolving source |
|---|---|---|---|---|
| **PIL-1** cross-holding / counterparty valuation | HOLDS on A, A′ and C; NOT EVALUABLE on B | **EVALUABLE** | n/a | `sec85` Item 1A p.37 + `sec121` pp.16–17 |
| **PIL-2** immaterial-to-counterparty disclosure | PENDING | **FLAG: REACHABLE-BUT-NOT-RECORDABLE** | n/a (recordability, not testability) | the next **Item 1A refresh — the FY2026 Form 10-K**; the Q1 2026 leg is closed by incorporation by reference (`sec121` p.118) |
| **PIL-3** ~19 issuer risk-factor reads | PENDING / UNMEASURED | **EVALUABLE — blocked by EFFORT, not reachability** | n/a | each issuer's **Item 1A**, served on-platform (SATS: `sec85` pp.36–41) |
| **PIL-4** listing event | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | **Class A** | **2** — genuine absence from the source | a **registration statement (Form S-1) or an 8-K announcing a listing/spin-off**; monitor. Proxy: the disclosed preconditions (`sec121` p.16) |
| **PIL-5** terrestrial denominator | PENDING | **Class B** `UNRESOLVABLE-FROM-PLATFORM` | **5** — ingestion absence of a datum class | the **commercially licensed colocation/greenfield cost dataset** (named by supplier and product); proxy: issuer capex disclosures (`sec121` p.104) |
| **PIL-6** FCC IBFS / ITU | `UNRESOLVABLE-FROM-PLATFORM` | **Class B** | **5** — ingestion absence of a datum class (regulatory registry) | **FCC IBFS file numbers and ITU filings**; proxy: the issuer's own licence table (`sec121` p.46) + impairment by asset class (`sec85` p.160) |

**PIL-7 metric = 0. Six falsifiers, six classified, six with a named resolving source.**

Detail on the three that need it most:

- **PIL-1** is the one falsifier whose evidence got *better* this phase. The SATS side supplies
  a disclosed instance with a counterparty (SpaceX), an amount (up to $8.5B / up to $11B), a
  price ($212 per share) and the issuer's own statement that no public market exists and the
  valuation is subjective. It is classed `EVALUABLE`; 001's residual not-evaluable leg (case B)
  is a **scoping** question about 001's own case set, not a reachability failure, and is
  returned to 001 as a re-classification candidate rather than carried as unclassified.
- **PIL-2** is the **third situation** (§2.3).
- **PIL-3** is **not** a reachability problem, and saying so is the point: the risk factors are
  **on the platform**. I opened SATS's Item 1A and read pages 36, 37 and 39 of `sec85`
  ([sec85 p.36](https://agentii.ai/v/SATS/sec85/36) carries the closing-conditions text quoted
  in §1.6). There is no source that would resolve PIL-3; there are **19 retrievals** that would,
  at roughly 6 pages each. It is a **labour and context-budget** block. **Additionally, the
  DA-27 mechanism-population identity caps what more issuers can buy**: SATS is a
  December-year-end issuer, the mechanism's sample is defined by that property, and adding
  December issuers adds no information about the remainder (kind **4**). PIL-3 must be re-scoped
  to a **positive predicate on a small sample** — e.g. "does the latest Item 1A name a
  counterparty, an amount, or a date?" — evaluated on 3 issuers including SATS, rather than
  measured on 19.

### 2.3 The third situation: a passing result that cannot be recorded

PIL-2's falsifier depends on catching a disclosure whose *absence* would be the evidence, when
that absence may be explained by **immateriality to the counterparty** (001's cross-cutting
finding 4.4). This is not a reachability problem and not a class: the datum is reachable. The
problem is that the falsifier's **passing state cannot be recorded as a passing datum** — there
is no affirmative observation that corresponds to "it passed", so the falsifier can never be
retired, only re-run. It is flagged in the table as
**`REACHABLE-BUT-NOT-RECORDABLE`**, and PIL-7's count of *unclassified or without named
resolving source* remains 0 **because the flag carries a named source and an explicit remedy**:
replace the falsifier with a **recordable predicate** (e.g. "the latest Item 1A names counterparty
X or amount Y in a risk factor" — a predicate that is recorded as true *or* false), evaluated
against a named refresh point. **At SATS that refresh point is now precisely dated: the FY2026
Form 10-K**, because the Q1 2026 10-Q's Item 1A contains no risk factor at all
([sec121 p.118](https://agentii.ai/v/SATS/sec121/118)). Until then, PIL-2's observation window
at SATS is **closed**, which is a fact about the corpus, not about the counterparty.

### 2.4 Structurally unreachable: proxy tests and re-scoping

For each falsifier that cannot fire, PIL-7's claim requires a **proxy test that is evaluable**,
or an explicit re-scope — not an unbounded carry.

- **PIL-4** (`UNRESOLVABLE-FROM-PUBLIC-SOURCES`, kind 2). No served period contains a listing
  event; the absence is genuine, so **no amount of re-running will resolve it**. Remedy per the
  class: name the disclosure (a registration statement or an 8-K announcing the listing/spin-off)
  and **monitor**. **Proxy test that is evaluable:** the falsifier's *preconditions* are
  disclosed — the Spectrum Acquisition Closing is expected "on or about November 30, 2027",
  which is also "the date on which the Convertible Notes due 2030 become eligible for
  redemption" ([sec121 p.16](https://agentii.ai/v/SATS/sec121/16)). A test on that date, plus
  the disclosed Seller Notes balance ($9.821 billion outstanding at 2026-03-31, secured by the
  AWS-4 and AWS-3 Licences), is evaluable from served pages, is falsifiable, and stands in for
  the listing test without pretending to be it.
- **PIL-5** (`UNRESOLVABLE-FROM-PLATFORM`, kind 5). The terrestrial denominator is
  **commercially licensed** data — public, but not carried and not licensed to the workspace.
  Remedy per the class: **record a platform-reach gap**, and if the thesis needs it, a licensing
  decision, which is a budget item rather than a research item. **Proxy:** the issuer's own
  capex and segment disclosures are evaluable and served — e.g. the Other segment's purchases of
  property and equipment of **4,864 in Q1 2026 against 163,936 in Q1 2025** ((159,072), (97.0)%
  — [sec121 p.104](https://agentii.ai/v/SATS/sec121/104)) — and can bound the trend while the
  licensed denominator remains unobtained. Flagged as a proxy throughout.
- **PIL-6** (`UNRESOLVABLE-FROM-PLATFORM`, kind 5). FCC IBFS and ITU filings are public
  registries the platform does not carry — the register's canonical `UNRESOLVABLE-FROM-PLATFORM`
  case. **Proxy test, and it is a good one:** the issuer's own licence table and its own
  impairment-by-asset-class note are served and evaluable.
  [sec121 p.46](https://agentii.ai/v/SATS/sec121/46) gives the gross spectrum balances
  band-by-band — 1,928,688 + 1,671,506 + 2,035,433 + 6,449,578 + 7,199,380 + 677,409 + 701,803
  + 24,000 + 0 + 2,883 + 11,772 + 202,392 + 912,200 + 2,969 + 972 + 7,793,854 = **29,614,839**,
  with 10,270,436 of additions and **5,334,473** of accumulated impairment, closing to a net
  **34,550,802** (exact). Against a gross balance of 39,885,275, the accumulated impairment is
  **13.4%**, all of it recognised in FY2025. Together with [sec85 p.160](https://agentii.ai/v/SATS/sec85/160)
  (5,784,779 of regulatory authorisations impaired, 32.8% of the year's charge), the proxy test
  is: **is the impairment concentrated in the bands subject to the build-out obligation?** —
  answerable from served pages, and it tests the falsifier's *mechanism* rather than its
  identity. **It is a proxy and must be labelled one**: it cannot substitute for the IBFS filing,
  which is the primary evidence of the deadline and the licence-specific status.

## 3. Method — the weight discriminator, its boundary, and SATS's own linkbase

The discriminator: a concept at **weight −1** may legitimately carry a positive magnitude (the
weight supplies the sign); a concept at **weight +1 with a parenthesised filed cell** has been
stripped. **But weight −1 carries concepts with different verdicts** — capex under −1 is
CORRECT, the FY2023 tax line under −1 is STRIPPED — so weight alone does not decide. **The
completing test is DIRECTIONALITY:** a **unidirectional** concept absorbs the sign into the
weight and a sign test on it is **VACUOUS**; only a **bidirectional** concept has power.

At SATS, from the Q1 2026 calculation linkbase:

| Arc (parent ← child) | Weight | Directionality | Verdict |
|---|---|---|---|
| `us-gaap:OperatingIncomeLoss` ← `RevenueFromContractWithCustomerExcludingAssessedTax` | +1 | unidirectional | **VACUOUS** |
| `us-gaap:OperatingIncomeLoss` ← `us-gaap:CostsAndExpenses` | −1 | unidirectional | **VACUOUS** |
| `us-gaap:CostsAndExpenses` ← *each cost child* (cost of goods and services, other cost of operating revenue, SG&A, D&A) | +1 | unidirectional | **VACUOUS** — a sign test here proves nothing |
| `us-gaap:CostsAndExpenses` ← **`sats:AssetImpairmentChargesAndOther`** | +1 | **BIDIRECTIONAL** (charges in FY2023/FY2025, a credit in Q1 2026) | **EXERCISED → FAILED** (served +66,159,000 against a filed (66,159)) |
| `us-gaap:ProfitLoss` ← pre-tax income / ← `us-gaap:IncomeTaxExpenseBenefit` | +1 / −1 | **BIDIRECTIONAL** (loss years at SATS) | **EXERCISED → FAILED** (Q1 2026 `ProfitLoss` served 147,300,000 against a filed (147,300)) |
| `us-gaap:NonoperatingIncomeExpense` ← `sats:InterestExpenseNetOfAmountCapitalized` | −1 | bidirectional in principle | **UNEXERCISED** — see below |

Two further findings from the same tree:

1. **The tax line is UNEXERCISED, not clean.** SATS's tax concept is bidirectional (a loss year
   with a valuation-allowance movement produces either sign) and I read **no** negative-filed
   tax instance, so no clearance is recorded. `us-gaap:IncomeTaxExpenseBenefit` is served for
   Q1 2026 as `20,920,000`; the served FY2025 deferred-tax magnitudes are large and positive,
   which is *consistent* with a valuation-allowance year and is **not** sign evidence either way.
2. **The label/concept basis mismatch.** `us-gaap:ProfitLoss` carries the arc label "Net income
   before taxes" in two roles while the concept is after-tax. A label is not a basis, and this is
   the same class of trap as DA-30 at the caption level.

The rule this yields for this thesis: **any clearance of a sign defect must name the concept,
the weight, and a negative-filed instance — or be recorded `UNEXERCISED`.** Applied to SATS,
every bidirectional line I read is exercised and fails; the unidirectional ones are vacuous; and
one line is left honestly unexercised.

## 4. The two portable detectors, fired at SATS

Both detectors are the register's portable recoveries from the MRCY refutation, and both were
derived at 001. They are re-run here on SATS to show they are portable in the direction that
matters — a *different* issuer, a *different* concept, a *different* sign.

**(1) Articulation: a served series fails articulation by exactly 2 × the stripped term.**
Feeding the served components through the filing's own calculation arcs for Q1 2026:

```
CostsAndExpenses (served components) = 1,998,268 + 536,907 + 639,025 + 166,601 + 66,159
                                     = 3,406,960
OperatingIncomeLoss (derived)        = 3,667,489 − 3,406,960 = 260,529
OperatingIncomeLoss (served)         =                          392,847
                                              gap = 132,318
132,318 = 2 × 66,159 = 2 × |the stripped term|          ← EXACT
```

And the correction is two-sided and exact: `3,406,960 − 2 × 66,159 = 3,274,642`, which **is** the
filed total costs and expenses, and `3,667,489 − 3,274,642 = 392,847`, which **is** the filed
operating income. **The strip is fully detectable from served data**, in both directions, from
the platform's own arcs and facts.

**(2) Overshoot: served components exceed the parent by exactly 2 × |every negative component|.**
At UTHR this fired six of six. At SATS the byte-level law is identical — **132,318 = 2 × 66,159**
— but the **polarity is inverted**, and that inversion is the finding: UTHR's parent was
mis-served, so the components overshot it; SATS's parent (`OperatingIncomeLoss` = +392,847) is
served *correctly* because the filed value is positive, so the components sum **above** the
parent and the derived child undershoots. The invariant is **2 × |the negative term|**; the
sign of the discrepancy tells you **which side of the identity was mis-served**. A detector
wired to look only for overshoot would miss SATS entirely.

## 5. `validate_calculation` at SATS: a constitutive incapacity

The validator is **structurally incapable of detecting the strip at SATS**, and this is not a
bug that a re-run fixes:

| Accession | Concept | Instrument output | Filing prints | Verdict |
|---|---|---|---|---|
| Q1 2026 | `us-gaap:ProfitLoss` | computed = reported = 147,300,000, diff 0 | **(147,300)** | **`pass`** |
| Q1 2026 | `NetIncomeLossAvailableToCommonStockholdersBasic` | 146,885,000 both sides | **(146,885)** | **`pass`** |
| Q1 2026 | `us-gaap:OperatingIncomeLoss` | matches no filed line | 392,847 | instrument mis-selection |
| Q3 2025 | `us-gaap:ProfitLoss` | computed = reported = 12,781,348,000, diff 0 | **(12,781,348)** | **`pass`** |
| Q3 2025 | `us-gaap:OperatingIncomeLoss` | computed 224,000 / reported 563,000 | (16,641,875) | **`pass`** on a value ~4 orders of magnitude away |

The mechanism: the instrument's `reported` column **shares the stripped store**. Both sides of
the comparison are drawn from the same corrupted series, so `diff = 0` and `pass` is returned on
a figure the filing prints in parentheses. **A `validate_calculation` pass is not evidence about
sign.** It can also return **zero rows** on a filed concept (VRT → the proposed
`UNVALIDATED-BY-PLATFORM` class) and `pass` when **both** sides were stripped (MRCY). The Q3 2025
`OperatingIncomeLoss` row is worse than a miss: it is a `pass` on a figure that is not the one
under test.

**DA-29's mechanical circularity test applied here.** If any term in a reconciliation appears
nowhere in the source, the check is a **back-solve** — and a back-solve closes exactly, so it
cannot be caught on closure, only on terms. At SATS the test produces a **term failure**, not a
closure failure:

| Query (concept-keyed) | Rows returned |
|---|---|
| `sats:InterestExpenseNetOfAmountCapitalized` (named in the linkbase as a term) | **0** |
| `us-gaap:InterestExpenseNonoperating` | **0** |
| `us-gaap:InterestExpense` | **0** |
| `us-gaap:NonoperatingIncomeExpense` (the parent) | **0** |

So the non-operating identity at SATS **cannot be validated at all**: the tree names a term the
store does not serve, and the parent is not served either. Per the register's rule this is
recorded as a **term-level `UNVALIDATED-BY-PLATFORM` finding**, *not* as a passed check and *not*
as "the filing has no interest expense" — a zero from a concept-keyed query is evidence about
the **tag**, not the filing. The locating method that *would* settle it is the fact view of the
statement page, not concept guessing. **Carry-forward C4.**

Two further instrument caveats, both exercised this phase: **`computed` may not be cited as a
derivation** (NVDA: 37× error), and **`reported` is not definitionally the filed value** — the
corruption can be **inverse** (IRDM: `computed` carried the filed sign while `reported` was
stripped — the reverse of MSFT — so "trust `computed`" does not generalise). At SATS the
mis-selection is visible directly: Q1 2026 `OperatingIncomeLoss` `reported` = 173,000 and
Q3 2025 `computed`/`reported` = 224,000 / 563,000, none of which is a filed figure.

## 6. Instrument traps that produce false zeros

These are the ways a *zero* was produced at SATS without any absence in the filing, and they are
recorded so that no downstream artifact reads one as an absence.

1. **Extension tags.** `us-gaap:`-keyed queries **silently miss filer extensions**, and SATS's
   own impairment concept is an extension (`sats:AssetImpairmentChargesAndOther`). A zero from a
   `us-gaap` query is evidence about the tag, not the filing. Worse, the registry **denies the
   concept exists**: `list_xbrl_concepts(namespace="sats")` returns **0 rows** while
   `search_xbrl_facts(namespace="sats", concept="AssetImpairmentChargesAndOther")` returns the
   full series. The instrument that would tell you the concept exists cannot see it.
2. **Source-file stems.** Every SATS filing before Q1 2026 is stored under the **`tmb-`** stem
   (`tmb-20251231x10k.htm`, `tmb-20250930x10q.htm`, `tmb-20241231x10k.htm`); only the Q1 2026 10-Q
   is `sats-20260331x10q.htm`. Any query keyed on a `sats-` stem returns nothing for every
   earlier period **by construction**.
3. **Keyword-search zeros.** A zero from `search_keyword_in_source` is **not** evidence the
   filing lacks the word (NVDA: "space" → 0 hits, "Revenue" → 23). Absence must be established by
   reading pages, and the method must be stated.
4. **`processing_status`.** Non-discriminating, everywhere: IRDM 9 of 9 "pending" including
   accessions that serve facts; SATS all "pending" with every figure readable; MRCY 36 filings
   "pending" and 10 of 10 pages served. It must not be used as an ingestion-absence marker.
5. **The description-field trap, and this artifact's own hygiene.** A citation to a table page
   must quote the **cells**. The `read_source_outline` description is LLM-generated, fluent,
   figure-dense, in the register of the filing, **inherits its negative signs**, and is the
   vector behind all three of 001's page-attributed quotations. Every quotation in this artifact
   comes from a page I read with `read_source_pages`, and every table is quoted as cells. Where I
   could not read a page I have **not** cited it (see §8).
6. **Freshness metadata is not a recency argument.** The platform reports `data_freshness:
   2027-04-12`, seven months **ahead** of `as_of` (the A11 defect). It is not used here.

## 7. Corrections recorded

**001 is frozen and is not rewritten.** Corrections are recorded, and the artifacts that
consumed them must restate.

| Item | Status | Basis |
|---|---|---|
| `$15.0B` (FY2025 revenue) | **reproduces exactly** | 15,004,989 filed, [sec85 p.150](https://agentii.ai/v/SATS/sec85/150) |
| `$19.6B` | **reproduces arithmetically; re-grade DERIVED** | $17B + $2.6B, both disclosed on [sec121 p.17](https://agentii.ai/v/SATS/sec121/17) — a sum of two filed figures, not a filed figure. The $2.6B buys **15 MHz of AWS-3** (1695–1710 MHz), **not** AWS-4/H-Block |
| `~$27B` | **DOES NOT REPRODUCE** | no filed figure equals it. Nearest filed aggregates: 34,550,802 (net spectrum), 39,885,275 (gross spectrum), 29,614,839 (pre-addition balance) — all [sec121 p.46](https://agentii.ai/v/SATS/sec121/46) — and $22.650B of AT&T cash on closing ([sec121 p.18](https://agentii.ai/v/SATS/sec121/18)) |
| "Spectrum gains" | **REFUTED** | a 17,632,011 thousand **charge** was recognised and **nothing has closed**: the closing conditions are "none of which have been satisfied yet" |
| `2.3% → 5.7% → 460.5% → 118.1% → 10.7%` | magnitude-of-loss series, needs a sign fix | reproduces exactly as \|OI\| ÷ revenue; the register's corrected filed series is `(2.28)% → (5.73)% → (460.46)% → (20.54)% → +10.71%` |

**Correction to 003 (recorded here because 003's spec quotes SATS):** 003 quotes SATS's operating
margin at **"10.7%"**. That is exactly the Q1 2026 **filed** figure, and it carries the
**(66,159) credit** — it corrects to **8.91%**. 003's contamination note also names the wrong
contaminant and the wrong sign: it says "the asset-sale gain runs through `operating_income`".
**There was no asset-sale gain.** There was a 5G-Network impairment charge, and the only gain in
the served series is the 66,159 thousand settlement credit in Q1 2026.

## 8. Could not be verified

- **Every quotation is page-verified; the served XBRL series are not.** The fact-store values
  cited here (`OperatingIncomeLoss`, `AssetImpairmentChargesAndOther`, the served components)
  come from `search_xbrl_facts` / `get_calculation_tree` / `validate_calculation`, and **a served
  fact has no page-resolvable URL** — the platform offers no citation form for a stored fact.
  Provenance is therefore recorded as *instrument-served* (instrument, concept, accession and
  source_file named in text) rather than page-cited. This is a **traceability gap in the
  platform**, not a citation shortcut, and it is carry-forward **C5**.
- **The $8.5B / $11B equity figures are not reconciled to each other.** They are on two pages
  and two mechanics; 8.5 + 2.6 = 11.1 is *consistent with* "up to $11 billion" but is a DERIVED
  observation of mine, off by 0.1B, and is not filed as a reconciliation.
- **The non-operating block at SATS is not locatable** (four concept-keyed queries returned zero
  — §5). Any falsifier depending on interest, pre-tax income subtotals or the tax line at SATS
  cannot be validated from the store until the served tags are located by reading the statement's
  fact view. Carry-forward **C4**.
- **The FY2025 tax sign is not verified.** No statement page was read for the tax line, so no
  direction is asserted and no clearance is recorded (§3).
- **PIL-3's 19-issuer census was not performed.** It is classified and its blocking condition is
  identified; the census itself is not claimed.
- **The Q3 2025 impairment note's component identity** (391,972 + 5,409,517 + 5,682,226 +
  4,191,133 + 806,620 = 16,481,468) is recorded from my read of
  [sec120 p.19](https://agentii.ai/v/SATS/sec120/19). It closes exactly and is consistent with
  the FY2025 note's larger decomposition, but I did **not** re-read p.19 during the final pass as
  I re-read pp.75, 104, 105, 114, 118 and 160; it carries a lower, single-read confidence than the
  other cells in this artifact.
- **Freshness metadata is unusable** (A11, §6.6).

## Carry-forwards

- **C1.** Restate 003's SATS margin from "10.7%" to **8.91%** ex-DA-24, and correct its
  "asset-sale gain" to the 5G-Network impairment charge with a 66,159 thousand settlement credit.
- **C2.** 001's `~$27B` must be withdrawn or re-based to a filed aggregate; `$19.6B` must be
  re-graded DERIVED. Both are recorded here, neither may be carried silently.
- **C3.** Any ex-item series must carry the **second-order** flag: the D&A relief (292,624 in
  Q1 2026 alone) and the accretion tail are not removable by add-back.
- **C4.** Locate SATS's served tags for the non-operating block by reading the statement's fact
  view; record the result as `UNVALIDATED-BY-PLATFORM` until then.
- **C5.** The platform has **no citation form for a served XBRL fact**. Until it does, every
  fact-store value in this thesis is provenance-recorded by instrument, not by link.
- **C6.** PIL-2's observation window at SATS is **closed** until the FY2026 10-K; PIL-3's
  blocking condition is **effort**, and any re-scope must respect the DA-27 mechanism-population
  identity (adding December issuers adds nothing).
- **C7.** PIL-4, PIL-5 and PIL-6 must be carried as **proxy-tested**, not as pending-and-waiting.
  A downstream thesis that sizes against them is sizing against something that cannot happen
  (PIL-6's whole claim).

## Sources

| Figure (as filed) | Source |
|---|---|
| Q1 2026 revenue 3,667,489; operating income 392,847 / (88,132) | [📄 SATS 10-Q p.11](https://agentii.ai/v/SATS/sec121/11) |
| Seller Notes $9.821 billion; Equity Amount up to $8.5 billion at $212; closing on or about 2027-11-30 | [📄 SATS 10-Q p.16](https://agentii.ai/v/SATS/sec121/16) |
| AWS-3 15 MHz for $2.6 billion; $17 billion → approximately $20 billion; up to $11 billion in Class A | [📄 SATS 10-Q p.17](https://agentii.ai/v/SATS/sec121/17) |
| AT&T purchase price $22.650 billion in cash on closing | [📄 SATS 10-Q p.18](https://agentii.ai/v/SATS/sec121/18) |
| Spectrum table: 29,614,839 + 10,270,436 − 5,334,473 = 34,550,802 | [📄 SATS 10-Q p.46](https://agentii.ai/v/SATS/sec121/46) |
| Other segment: D&A 11,305 / 303,929; impairments and other (66,159); OI (87,295) | [📄 SATS 10-Q p.104](https://agentii.ai/v/SATS/sec121/104) |
| "no depreciation expense for the 5G Network assets impaired"; $66 million credit; RSA Settlement costs $50 million | [📄 SATS 10-Q p.105](https://agentii.ai/v/SATS/sec121/105) |
| Item 1A: incorporation by reference; Item 3: no material changes | [📄 SATS 10-Q p.118](https://agentii.ai/v/SATS/sec121/118) |
| Q3 2025 revenue 3,614,258; total costs and expenses 20,256,133; OI (16,641,875) | [📄 SATS 10-Q p.10](https://agentii.ai/v/SATS/sec120/10) |
| Q3 2025 impairment note components = 16,481,468 | [📄 SATS 10-Q p.19](https://agentii.ai/v/SATS/sec120/19) |
| Q3 2025 segment table: impairments Wireless 16,199,344 + BSS 282,124 = 16,481,468 | [📄 SATS 10-Q p.75](https://agentii.ai/v/SATS/sec120/75) |
| Closing conditions "none of which have been satisfied yet" | [📄 SATS 10-K p.36](https://agentii.ai/v/SATS/sec85/36) |
| SpaceX investment: "absence of a public market for its shares"; "subjective valuation methodologies" | [📄 SATS 10-K p.37](https://agentii.ai/v/SATS/sec85/37) |
| FCC "unequivocal position"; pivot "to selling certain wireless spectrum licenses" | [📄 SATS 10-K p.39](https://agentii.ai/v/SATS/sec85/39) |
| Segment tables FY2025 / FY2024 / FY2023: impairments 17,632,011 / — / 761,099 | [📄 SATS 10-K p.114](https://agentii.ai/v/SATS/sec85/114) |
| FY2025 revenue 15,004,989; total costs and expenses 32,728,135; OI (17,723,146) | [📄 SATS 10-K p.150](https://agentii.ai/v/SATS/sec85/150) |
| Impairments and other note: regulatory authorizations 5,784,779 of 17,632,011; $457 million; $1.284 billion | [📄 SATS 10-K p.160](https://agentii.ai/v/SATS/sec85/160) |
