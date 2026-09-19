---
thesis_id: "002-evidence-validation"
artifact: spcx-nameplate-and-boundary
pillar: [cross]
ticker: SPCX
skill: synthesis
mode: default
task: T902
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
schema: spcx_nameplate_and_boundary
evidence_grade: MODELED
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
definitions_used:
  - da_id: DA-11
    chosen_reading: >
      Nameplate Compute Draw — an issuer-defined installed-capacity metric, read at its filing
      definition on sec8 p.36: GPU count x all-in GPU power draw, excluding cooling, power
      distribution losses, lighting, security and facility-level overhead. CONFIRMED and NARROWED:
      the quantity is GPU nameplate, which is a proper subset of IT load, which is a proper subset
      of facility draw. The narrowing is load-bearing here — it is what makes PIL-4's falsifier
      outcome depend on which quantity is put in the numerator.
  - da_id: DA-21
    chosen_reading: >
      Management-drawn segment boundaries. Read at the AI / Connectivity / Space axis as filed on
      sec8 pp. 13, 30, 31 and 44. CONFIRMED, and this artifact records its LIMIT: DA-21 governs a
      line drawn by management inside a fixed legal perimeter, and it does not reach the case where
      the comparative periods themselves were drawn on a different perimeter. That residual is the
      C-1 register gap (§5).
  - da_id: DA-23
    chosen_reading: >
      Sign stripping on a negative operating result. CONFIRMED at SPCX and reported here only as it
      bears on the two figures this artifact exists to settle: the platform serves `reported` = +143
      against a filed (143), and its validator's `computed` value (-4,578) is neither the filing's
      number nor its sign. The register's own DA-23 evidence for SPCX is the string "~65% GM", and
      that string reproduces on exactly ONE basis (§4.2) — so the register row is itself a basis
      collapse. DA-23's gross-profit bound is additionally declared near-useless at this issuer
      (false negative at every level at ~65% GM), so the detector is UNEXERCISED here, not passed.
  - da_id: DA-24
    chosen_reading: >
      Non-operating or non-recurring contamination of the operating line. PRESENT at SPCX, and
      PRESENT is established by the calculation linkbase, not by a face-level census:
      `us-gaap:RestructuringCharges` and `us-gaap:ImpairmentOfLongLivedAssetsHeldForUse` are arc
      children of `us-gaap:CostsAndExpenses` at weight +1. The qualifying half of DA-24 (a disposal
      gain sitting ABOVE the operating subtotal) is REFUTED — the linkbase carries exactly two arcs
      into `us-gaap:OperatingIncomeLoss`. Both verdicts are true simultaneously and §4.1 explains
      why two sibling artifacts appeared to disagree.
  - da_id: DA-25
    chosen_reading: >
      An issuer-defined per-unit metric not reproducible from the filed terms. CONFIRMED on the
      ARPU denominator (sec8 p.36): Starlink subscriber revenue over the AVERAGE subscriber count,
      and the average is never disclosed — only `As of` period-end counts, 12.0M and 6.0M. Bounds
      the DA-30 instance #6 in §4.3 and is the reason a subscriber-derived per-unit figure may not
      be cited downstream without its basis.
  - da_id: DA-28
    chosen_reading: >
      Capital-structure discontinuity around an IPO. CONFIRMED as an open exposure. Recorded here
      in its nameplate-relevant form: the numerator series (1.4 GW / 0.4 GW) and the balance-sheet
      denominators move on different sides of the same boundary — every balance-sheet denominator is
      post-IPO while numerators straddle it. Cells: preferred 38,752 -> nil; APIC 37,706 -> 167,344;
      total equity 2,573 -> 127,224 (49.46x); total assets 92,079 -> 192,770 (2.09x). Unprinted
      sub-term: the $671M H1-only, pre-IPO-only deduction between the two printed net-loss lines.
  - da_id: DA-29
    chosen_reading: >
      Defective checks — the mechanical circularity test. If any term in a reconciliation appears
      NOWHERE in the source, the check is a BACK-SOLVE, and a back-solve closes exactly, so it
      cannot be caught on the closure. Applied here to the $671M bridge between two adjacent printed
      lines, and to the choice between citing a `computed` value and a `reported` value: neither
      wins by default, and at SPCX the `OperatingIncomeLoss` row loses on both counts (§4.4).
  - da_id: DA-30
    chosen_reading: >
      Two bases collapsed onto one concept without a basis field. CONFIRMED at SPCX, SEVEN instances
      (§4.3), including one that sits INSIDE the register's own DA-23 row for this issuer and one
      that inverts a filed margin by 46.47 pp. Every figure this artifact hands downstream therefore
      carries an explicit basis string, and the register row is corrected by reference, not silently.
citations:
  - figure: "Nameplate compute draw, cells: 1.4 GW as of 2026-06-30 / 0.4 GW as of 2025-06-30, under the AI heading (Table 51); GPU-count x all-in-draw definition with the cooling/overhead exclusion; Space revenue customer-boundary sentence"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 36
    url: "https://agentii.ai/v/SPCX/sec8/36"
    located_via: read_source_pages
  - figure: "Facility-side power online: 20 GW power-and-cooling / 15 GW power-plant-level by end-2027 (Musk, verbatim)"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 4
    url: "https://agentii.ai/v/SPCX/ect1/4"
    located_via: read_source_pages
  - figure: "Compute basis for the same ratio: 'closer to 10 gigawatts of compute than 5'; 'over 2 gigawatts of compute' end-2026"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 1
    url: "https://agentii.ai/v/SPCX/ect1/1"
    located_via: read_source_pages
  - figure: "Nameplate trajectory restated on the call: 1.4 GW, up from 1 GW in Q1 and 400 MW a year earlier; >2 GW end-2026; $18.4B capex of which ~$15.8B AI"
    ticker: SPCX
    form_type: earnings_call_transcript
    citation_id: ect1
    page_no: 3
    url: "https://agentii.ai/v/SPCX/ect1/3"
    located_via: read_source_pages
  - figure: "Q2 2026 segment table (Table 42), cells: Space 962/329/(542); Connectivity 4,291/2,060/1,656; AI 2,561/3,818/(1,257); consolidated 7,814/7,957/(143); capex 1,174/1,367/15,828/18,369"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 30
    url: "https://agentii.ai/v/SPCX/sec8/30"
    located_via: read_source_pages
  - figure: "H1 2026 segment table (Table 43) and Q2 2025 comparatives (Table 44), cells: AI 3,379/7,105/(3,726) and 737/2,261/(1,524)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 31
    url: "https://agentii.ai/v/SPCX/sec8/31"
    located_via: read_source_pages
  - figure: "Revenue by type and segment (Table 17), all four periods incl. AI 2,561/737/3,379/1,465 and Space 962/746/1,581/1,611"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 13
    url: "https://agentii.ai/v/SPCX/sec8/13"
    located_via: read_source_pages
  - figure: "Launch counts (Table 48): Falcon 37/45/77/81 of which customer 10/9/17/21; Starship 1/1/1/3; Space-boundary sentence"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 35
    url: "https://agentii.ai/v/SPCX/sec8/35"
    located_via: read_source_pages
  - figure: "Consolidated revenue and operating-loss bridge (Table 53): revenue change 3,743 / 91.9% and 4,370 / 53.7%; loss from operations change 827 / (85.3%) and (1,143) / 121.2%"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 40
    url: "https://agentii.ai/v/SPCX/sec8/40"
    located_via: read_source_pages
  - figure: "AI segment MD&A (Table 56): revenue 2,561/737/247.5%, 3,379/1,465/130.6%; cost stack 1,106+2,178+532+2 = 3,818; loss from operations (1,257)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 44
    url: "https://agentii.ai/v/SPCX/sec8/44"
    located_via: read_source_pages
  - figure: "Statements of operations, four periods: revenue 7,814/4,071/12,508/8,138; restructuring 2/190/(9)/194; impairment —/5/—/29; loss from operations (143)/(970)/(2,086)/(943); net loss (541)/(1,008)/(4,817)/(1,536); net loss attributable to shareholders (541)/(1,008)/(5,488)/(1,536)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 5
    url: "https://agentii.ai/v/SPCX/sec8/5"
    located_via: read_source_pages
  - figure: "Consolidated balance sheets: preferred 38,752 -> nil; APIC 37,706 -> 167,344; equity 2,573 -> 127,224; assets 92,079 -> 192,770"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 4
    url: "https://agentii.ai/v/SPCX/sec8/4"
    located_via: read_source_pages
  - figure: "Note 1, the boundary events: IPO 638.9M Class A at $135.00, net proceeds $85,675M after $575M costs; five-for-one forward split May 2026; xAI Merger Date 2026-02-02; X Merger 2025-03-28; 'The Mergers were each effected through a share exchange'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 11
    url: "https://agentii.ai/v/SPCX/sec8/11"
    located_via: read_source_pages
---

# SPCX — the Nameplate and the Boundary (T902)

> **Two things meet at SPCX and they are the same thing seen twice.** The `1.4 GW` is a *quantity*
> whose basis is narrower than it reads; and it is a *series* whose comparator predates the entity
> that now owns it. Both are the same defect — **a number that is quoted without its perimeter** —
> and both are handed to the same downstream theses (009 and 011).
>
> This is a `_cross/` artifact. It depends on every prior phase, it is **never `[P]`**, and it does
> no new filing discovery of its own: **every cell below was read directly from the page**, and the
> seven figure-classes it adjudicates were produced by the Phase 4/5/6 artifacts of this thesis.
> Where it contradicts a sibling artifact, it says so and gives the resolved verdict (§4).
>
> **Citation convention, stated because it is part of the finding.** The frontmatter `citations`
> block lists **only the thirteen pages whose cells I read directly** (`located_via:
> read_source_pages`). Pages cited in the body that I did **not** read — pp. 9, 12, 22, 42, 43, 45
> and 46 — are linked inline and **attributed to the artifact that located them**. A page number
> that was not located by a read is a guess; a guessed page number resolves to the wrong page,
> which is worse than no link because it looks correct.

---

## 0. The two answers in one screen

| # | Question | Answer | Grade |
|---|---|---|---|
| 1 | What does `1.4 GW` measure? | **GPU nameplate** — GPU count × all-in GPU draw, AI segment, as of 2026-06-30. Excludes cooling, distribution losses, lighting, security, facility overhead **and** host CPUs, DRAM, NICs, storage and PSU losses | DEMONSTRATED (filed cell) |
| 2 | What is the facility-side restatement? | **2.1 GW expected / 2.8 GW at the issuer's tentative target**, against 1.4 GW as filed and a 1.2–2.0× band | MODELED (projection onto a delivered fleet) |
| 3 | Does PIL-4's falsifier fire? | **It fires at the ceiling and is indistinguishable from the threshold at the floor.** `2.00 > 1.5` fires; `1.50 = 1.5` does not, on the same metric | DEMONSTRATED (arithmetic on filed + disclosed inputs) |
| 4 | What is the correct PUE reading? | **Not computable.** Bounded ≈1.3–1.7×, straddling the 1.5 threshold | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| 5 | Whose fleet is the 1.4 GW series? | **xAI's**, inside the AI segment. The 0.4 GW comparator is dated **7 months before** xAI was consolidated | DEMONSTRATED (filed cell + filed merger date) |
| 6 | What is the `+250%`? | **A within-xAI rate surfaced by recasting — NOT SPCX capital deployment.** No recast sentence exists anywhere in the filing | DEMONSTRATED (arithmetic signature) |
| 7 | How much of SPCX's growth came from outside the prior-year entity? | **48.7% of Q2 (43.8% H1)**; consolidated growth `+91.9% → +57.6%` ex-AI, a **59.5% relative** difference | DERIVED from filed cells |
| 8 | What does SPCX actually deploy? | **AI-segment capex $15,828M in Q2 for 0.4 GW of nameplate added — $39.6M/MW nameplate, $26.4M/MW facility-side** | MODELED (capex is not the cost of the increment) |
| 9 | What is the Space revenue boundary? | **The CUSTOMER boundary.** 10 of 38 launches were customer launches in Q2 (26.3%); the activity is far larger than the revenue | DEMONSTRATED (filed sentence + filed counts) |

**Per-series entity-boundary classification (spec §6), delivered:** **Space — CLEAN. Connectivity —
CLEAN. AI — CONTAMINATED.** The classification is per *series*, not per segment: Space's and
Connectivity's revenue series span the same legal periods on both sides; the AI series does not.

---

## 1. The nameplate — what `1.4 GW` measures, and what it excludes

### 1.1 The filed cell, and its heading

The cell is on the segment page, in Table 51, **under the `AI` heading**
([sec8 p.36](https://agentii.ai/v/SPCX/sec8/36)):

```
| (in gigawatts)         | As of          | As of          |
|                        | June 30, 2026  | June 30, 2025  |
| Nameplate compute draw |      1.4       |      0.4       |
```

Two facts follow from the heading and are not suppressed anywhere in the filing: the series is
**the AI segment's**, and it is a **two-point series whose comparator is a date, not a perimeter**
(§2).

### 1.2 The definition, and the exclusion the register already names

The metric definition at the same page, verbatim: *"the **number of GPUs installed in our data
centers** at the end of the period multiplied by their respective **all-in power draw**. …
It **does not include power we install and use for our supporting infrastructure such as cooling
systems, power distribution losses, lighting, security systems, or facility-level overhead**."*

**DA-11 is CONFIRMED and NARROWED.** 001's inherited framing called the 1.4 GW *"IT load only."*
The filing does not say that, and the quantity it defines is **narrower than IT load**. Beyond
cooling and distribution it also excludes the **host CPUs, DRAM, NICs, storage, PSU conversion
losses and the network fabric** that sit inside the facility's IT load but outside the GPU
nameplate. The chain is:

```
GPU nameplate  ⊂  IT load  ⊂  facility draw
    1.4 GW          (undisclosed)   (undisclosed, restated in §1.3)
```

**The direction of the error matters and it is one-directional.** Any artifact that treats 1.4 GW
as IT load **understates** the gap to facility draw; any PUE computed against the 1.4 GW
**overstates** the PUE. Neither error is symmetric with the other.

### 1.3 The restatement — one number per basis, none of them interchangeable

| Basis | Multiple | Figure | What it measures | What it excludes | Quotable for | Grade |
|---|---:|---:|---|---|---|---|
| **As filed** | 1.00× | **1.4 GW** | Installed GPU nameplate, AI segment, 2026-06-30 | Cooling, distribution, lighting, security, facility overhead; host CPU/DRAM/NIC/storage/PSU losses; utilisation | Installed compute capacity; capacity-planning ratios; a GPU-side denominator | **DEMONSTRATED** (filed cell) |
| Band floor (spec's reference) | 1.20× | 1.68 GW | — | — | **Nothing.** Recorded only to show where the claimed band's floor sits | DERIVED, reference only |
| **Facility-side, issuer-expected** | **1.50×** | **2.1 GW** | Facility-side power *implicit in the issuer's own forward expected case, applied back to the delivered fleet* | Actual delivered facility draw; utilisation; everything the 1.4 GW excludes is now included | Power procurement, cooling and electrical-equipment planning, grid interconnect | **MODELED** on a CLAIMED forward input |
| **Facility-side, issuer target** | **2.00×** | **2.8 GW** | As above, on the issuer's tentative target | As above | Same, as the issuer's own ceiling — and it is the reading on which PIL-4's falsifier fires | **MODELED** on a CLAIMED forward input |
| **PUE proper** | ≈1.3–1.7× | **not computable** | Facility draw ÷ **full IT load** | — | **Nothing yet.** Not a restatement of the 1.4 GW, and must not be multiplied by it (§1.6) | **UNRESOLVABLE-FROM-PUBLIC-SOURCES** |
| **Delivered facility draw** | — | **not reported** | — | — | **Nothing.** No figure for delivered facility-side power exists anywhere in the corpus | **UNEVIDENT** |

**The single sentence a downstream thesis should carry:** *As of 2026-06-30 the AI segment's
installed GPU nameplate is 1.4 GW as filed; the issuer's own forward disclosure puts facility-side
power at 1.5–2.0× the compute basis, i.e. 2.1–2.8 GW, which is a projection and not a delivered
draw.*

### 1.4 Where the multiple comes from — same speaker, same answer, same horizon

The input the spec records as non-existent **is disclosed**, on the Q2 2026 earnings call, by the
same speaker, in the same answer, on the same basis
([ect1 p.4](https://agentii.ai/v/SPCX/ect1/4)): *"we're actually aiming to far exceed that gigawatt
number in terms of **power online, power cooling and electrical equipment**. So our tentative target
is to actually have **20 gigawatts at the power and cooling level online by the end of next year**
… but I would expect that we still probably have **at the power plant level, something close to 15
gigawatts** … our goal is to have far more power, cooling and electrical equipment than we have
GPUs."*

The compute denominator for the same horizon, from the same speaker
([ect1 p.1](https://agentii.ai/v/SPCX/ect1/1)): *"closer to 10 gigawatts of compute than 5
gigawatts of compute."* Hence a **same-basis, same-utterance, same-horizon multiple**:

```
15 GW power-plant-level    / 10 GW compute  =  1.50x   expected case
20 GW power-and-cooling    / 10 GW compute  =  2.00x   tentative target
```

**The horizon mismatch is recorded, not smoothed.** The multiple is an **end-2027 forward ratio**;
applying it to the **delivered 2026-06-30 nameplate** produces a projection of where facility draw
will sit under the issuer's own plan. That is why the restated rows are MODELED and not
DEMONSTRATED, and why they may not be described as delivered:

> *Note what this is not.* It is not a measurement of facility draw at 2026-06-30. Reading it as one
> would convert a sponsor's end-2027 aspiration into a current-period quantity — the shape P10
> forbids on the orbital side (*"aspiration is not offtake"*), and which has no more standing on
> the terrestrial side.

### 1.5 The falsifier: it holds at the floor and fails at the ceiling

PIL-4's stated claim is that the ratio of true facility draw to stated load lands within **1.2–1.5×**.
Its falsifier is `metric=spcx_facility_pue_ratio threshold=1.5 source=issuer_disclosure_or_industry_PUE_benchmark op=>`.

| Reading | Value | Against `> 1.5` | Outcome |
|---|---:|---|---|
| Expected case (`15 GW / 10 GW`) | **1.50** | `1.50 > 1.5` is **false** — the operator is strict | **Does not fire. Sits exactly at threshold.** |
| Tentative target (`20 GW / 10 GW`) | **2.00** | `2.00 > 1.5` is **true** | **FIRES** |

**So the 1.2–1.5× claim holds at the floor and fails at the ceiling, on the issuer's own tentative
target.** The claim is not falsified — it is *undetermined on a basis-dependent knife edge*, and the
spec's flat disposition (*"PIL-4's data does not exist publicly"*, `UNRESOLVABLE-FROM-PUBLIC-SOURCES`)
is contradicted by the issuer's own transcript. **PIL-4 is evaluable and partially falsified; it is
no longer UNRESOLVABLE and no longer PENDING.**

### 1.6 The second reading, reported and not collapsed

Two different quantities can be put in that numerator and the falsifier's outcome flips between
them. Both are reported; neither is collapsed (spec §1c `no_single_basis_collapse`):

- **Reading A — DA-11 basis** (facility-side power ÷ the filed 1.4 GW): **1.50× / 2.00×**. Both
  halves named by the same speaker on the same basis. Computable.
- **Reading B — PUE proper** (facility draw ÷ **full IT load**): **bounded ≈1.3–1.7×**, which
  straddles 1.5 and cannot be resolved. Three facts establish the bound: (i) `PUE` and *"power usage
  effectiveness"* return **zero** hits in the 10-Q — SPCX discloses no PUE; (ii) **no industry PUE
  benchmark is carried on the platform** — the VRT 10-Q returns zero PUE hits and no workspace
  artifact carries a sourced PUE value; (iii) since GPU nameplate ⊂ IT load,
  `PUE_proper ≤ facility-side ÷ nameplate` — **strictly below Reading A's multiple**.

**The prohibition that follows, and it is the one 009 and 011 are most likely to break: do NOT
multiply 1.4 GW by Reading B.** Reading B's denominator is *not* the 1.4 GW, because the 1.4 GW is
not IT load (§1.2). Multiplying a PUE bound against a nameplate denominator is exactly the
two-bases-on-one-concept error DA-30 registers — performed by the artifact that exists to prevent it.

### 1.7 The numerator cross-check — and it closes

SPCX added **0.4 GW** of nameplate in Q2 (1.4 GW at 2026-06-30 against **1.0 GW at 2026-03-31**,
[ect1 p.3](https://agentii.ai/v/SPCX/ect1/3)) and spent **$15,828M** of AI-segment capex in the
quarter ([sec8 p.30](https://agentii.ai/v/SPCX/sec8/30)):

| per unit of power added | figure | note |
|---|---:|---|
| per MW of **nameplate** added | **$39.6M/MW** | `15,828 / 400` |
| per MW of **facility-side** at 1.5× | **$26.4M/MW** | `15,828 / 600` |
| per MW of **facility-side** at 2.0× | **$19.8M/MW** | `15,828 / 800` |

**Grade MODELED, and the direction of the bias is named:** capex is not the cost of the increment
(some spend is not yet energised), so `$39.6M/MW` is an **upper bound** on the nameplate cost per MW
and the facility-side figures inherit that. Within that limit the disclosed capex and the disclosed
facility-side multiple are **mutually consistent** — which is the strongest statement available
without a filed PUE.

Two further context figures, both filed: AI capex was **86.2%** of total company capex in Q2
(`15,828 / 18,369`) and **82.7%** for H1 (`23,551 / 28,476`). And the forward guidance is
**on-trend, not heroic**: *"We expect to end this year at over 2 gigawatts of compute capacity"*
([ect1 p.1](https://agentii.ai/v/SPCX/ect1/1), [ect1 p.3](https://agentii.ai/v/SPCX/ect1/3)) — from
1.4 GW that is **≥+43% over two quarters**, against the **+40% just delivered in a single quarter**.
On the restated basis, end-2026 guidance implies **≥3.0 GW facility-side at 1.5× and ≥4.0 GW at 2.0×.**

---

## 2. The boundary — the `1.4 GW` series is not a single entity's fleet

### 2.1 The comparator is a date, not a perimeter

The AI segment's comparative column is dated **2025-06-30**. The entity that owns the AI segment
today was consolidated on **2026-02-02** — the **xAI Merger Date**, from Note 1: *"The Mergers were
each effected through a share exchange"* ([sec8 p.11](https://agentii.ai/v/SPCX/sec8/11)), the other
being the **X Merger, 2025-03-28**. So:

| | Date | Relation to the AI series |
|---|---|---|
| AI comparative column **close** (3M25 / 6M25) | 2025-06-30 | **7 months before** the xAI Merger Date |
| AI comparative column **open** (6M25) | 2025-01-01 | **13 months before** the xAI Merger Date |
| Shorter gap between the two mergers themselves | 2025-03-28 → 2026-02-02 | **10.2 months** |

**The `+250%` (`1.4 / 0.4 − 1`) is therefore a WITHIN-xAI rate surfaced by recasting.** It measures
xAI's build-out across two periods, one of which lies entirely outside SPCX's ownership. It is not
SPCX capital deployment, and no artifact should present it as SPCX's growth rate.

### 2.2 No recast sentence exists anywhere — and absence is established by reading

**Method, stated, because a zero from a keyword search is not evidence.** `search_keyword_in_source`
returns zero for the recast vocabulary, but a zero from that tool is evidence about the **index**,
not the filing. **Absence here is established by reading** the segment and MD&A pages that would
carry such a sentence — pp. 30, 31, 35, 36, 40 and 44 — and finding, on each, the recast's
**arithmetic signature** in place of any statement about it.

**The signature.** The AI segment carries full 3M25 and 6M25 comparatives on
[sec8 p.13](https://agentii.ai/v/SPCX/sec8/13) (revenue `2,561 | 737 | 3,379 | 1,465`),
[sec8 p.31](https://agentii.ai/v/SPCX/sec8/31) and [sec8 p.44](https://agentii.ai/v/SPCX/sec8/44)
(cost stack `737 / 2,261 / (1,524)` for 3M25 and `1,465 / 3,925 / (2,460)` for 6M25) — **for periods
that predate the consolidation of xAI by 7 and 13 months.** A segment with comparatives predating
its own parent's consolidation is a segment that was **recast**, and the filing never says so.

> **This is A18's exact shape, and SPCX is a second instance of it.** The hazard is registered as
> the C-1 register gap (§5): **no DA covers common-control recasting across a change of reporting
> entity.** DA-21 covers management-drawn segment boundaries inside a fixed perimeter; DA-28 covers
> capital-structure discontinuity. **Neither reaches a comparative restated to a different legal
> perimeter.**

### 2.3 The contamination, quantified — and it closes to the dollar

The three segment contributions to the consolidated revenue increase tie **exactly**, every term a
printed cell:

```
Q2 2026:   AI 2,561 -   737 = 1,824        H1 2026:  AI 3,379 - 1,465 = 1,914
           Connectivity 4,291-2,588=1,703            Connectivity 7,548-5,062=2,486
           Space      962 -   746 =   216            Space     1,581 - 1,611 =   (30)
                                     -----                                          -----
                                     3,743 = 7,814 - 4,071  EXACT                    4,370 = 12,508-8,138 EXACT
```

| Statistic | Filed | Ex-AI | Difference | Relative | AI's share of the change |
|---|---:|---:|---:|---:|---:|
| Q2 2026 revenue growth | **+91.9%** | **+57.6%** | **34.3 pp** | **59.5%** | **1,824 / 3,743 = 48.7%** |
| H1 2026 revenue growth | **+53.7%** | **+36.8%** | **16.9 pp** | **45.9%** | **1,914 / 4,370 = 43.8%** |

`(7,814 − 2,561) / (4,071 − 737) − 1 = 5,253 / 3,334 − 1 = 57.56%`;
`(12,508 − 3,379) / (8,138 − 1,465) − 1 = 9,129 / 6,673 − 1 = 36.80%`. The flagship share statistic
moves **6.0 points** on the same substitution (`12.31%` Space-of-consolidated → `18.31%` Space-of-ex-AI).
Source pages: [sec8 p.13](https://agentii.ai/v/SPCX/sec8/13), [sec8 p.40](https://agentii.ai/v/SPCX/sec8/40).

**And the affected line is the operating line, not only revenue.** The AI segment is the source of
the loss: H1 2026 AI loss from operations **$(3,726)M** against a consolidated **$(2,086)M**
([sec8 p.31](https://agentii.ai/v/SPCX/sec8/31)).

### 2.4 A clean tie-out is not a stable boundary — A18's lesson, applied

**The tie-out in §2.3 closes to the dollar, and that is not evidence about the boundary.** A18's
transplant case is the control: at SATS the variances **closed to the dollar while intersegment
revenue collapsed 86.2%**. *A mechanical tie-out certifies that the numbers add up, not that the
entity is the same one.* **The segment-composition check must be run separately** — and when it is
run here, 48.7% of the quarter's growth originates in a segment that did not exist inside SPCX a
year earlier. Both statements are true; only one of them was being tested.

### 2.5 DA-28 — the same boundary, on the balance-sheet side

**DA-28 is CONFIRMED at SPCX**, and it is the *same* discontinuity seen through a second face
([sec8 p.4](https://agentii.ai/v/SPCX/sec8/4), [sec8 p.11](https://agentii.ai/v/SPCX/sec8/11)):

| Cell | 2025-12-31 | 2026-06-30 | Movement |
|---|---:|---:|---:|
| Redeemable convertible preferred stock | 38,752 | **—** | converted at IPO |
| Additional paid-in capital | 37,706 | **167,344** | **+129,638** |
| Total shareholders' equity | 2,573 | **127,224** | **49.46×** |
| Total assets | 92,079 | **192,770** | **2.09×** |

On IPO proceeds of **$85,675M** net of $575M costs (638.9M Class A at $135.00), plus a **five-for-one
forward split** in May 2026 ([sec8 p.11](https://agentii.ai/v/SPCX/sec8/11)). **Every balance-sheet
denominator is post-IPO while numerators straddle the boundary** — which is why `roa`, `roe`,
`debt_to_equity`, `current_ratio` and `asset_turnover` all carry a basis that must be named before
use. And the sub-mechanism: a **$671M** H1-only, pre-IPO-only deduction between the two printed
net-loss lines ([sec8 p.5](https://agentii.ai/v/SPCX/sec8/5): net loss `(4,817)` vs net loss
attributable to shareholders `(5,488)`), **printed on no line of any statement** and refused rather
than derived per DA-29. The consequence binds any downstream net-loss quote directly: **the EPS
denominator is struck on `$(5,488)M`, not `$(4,817)M`** (`5,488 / 4,879 = $1.1248 → $(1.12)`, filed),
so a net-loss figure quoted without its basis carries a **13.9% error bar.**

### 2.6 The correct characterisation, in one paragraph

> **Not:** *"SPCX grew AI compute 250% year over year."*
>
> **But:** *"SPCX's AI segment reported **1.4 GW** of installed GPU nameplate at 2026-06-30 against a
> **0.4 GW** comparative dated 2025-06-30 — a date **7 months before** the segment's legal parent,
> xAI, was consolidated (2026-02-02). The `+250%` is therefore a **within-xAI build rate surfaced by
> recasting, not a rate of SPCX capital deployment**; the filing states no recast because no recast
> sentence exists. What SPCX deployed in the quarter is filed on a different axis: **AI-segment capex
> of $15,828M**, capitalising **0.4 GW** of nameplate at **$39.6M per MW of nameplate** / **$26.4M
> per MW of facility-side power**."*

---

## 3. The Space boundary is the CUSTOMER boundary

The second boundary finding is not about a period; it is about **what a segment's revenue counts**.
From the Launches definition and the Space revenue description, verbatim, **printed on both pages**
([sec8 p.35](https://agentii.ai/v/SPCX/sec8/35) and [sec8 p.36](https://agentii.ai/v/SPCX/sec8/36)):

> *"We allocate a significant amount of launch capacity to our Connectivity segment, and expect to
> allocate a significant amount to our AI segment in the future. **Our Space segment revenue only
> reflects our customer launches and customer activities.**"*

with the metric note: *"Mass to orbit and launches generally grow more rapidly than Space segment
revenue because these metrics include our internal constellation deployments from which we do not
recognize inter-segment revenue."* **So the Space segment's revenue boundary is the customer
boundary, not the activity boundary — and the gap is filed:**

| | Q2 2026 | H1 2026 | Q2 2025 | H1 2025 |
|---|---:|---:|---:|---:|
| Customer launches | **10** | 17 | 9 | 21 |
| Internal launches (all Starship is internal by footnote) | **28** | 61 | 37 | 63 |
| **Total** | **38** | 78 | 46 | 84 |
| **Customer share** | **26.3%** | **21.8%** | **19.6%** | **25.0%** |

`37` Falcon + `1` Starship = `38`; `27 + 1 = 28` internal; `10` customer
([sec8 p.35](https://agentii.ai/v/SPCX/sec8/35), Table 48).

**Three consequences, and the third is the one 011 needs:**

1. **Three quarters of the launches produced no Space revenue by design**, not by underperformance.
   Any Space-segment revenue or margin series is a **customer** series.
2. **The customer share is rising** — 19.6% → 26.3% in the quarter, i.e. customer launches **+11.1%**
   while total launches fell **−17.4%** (38 vs 46). Space revenue rose **+29.0%** in a quarter in
   which launch *activity* fell 17.4%. **Two opposite-signed rates on one activity, both correct,
   both the filing's** — quote either one only with its basis attached.
3. **The AI segment's growth consumes Space capacity invisibly.** Internal launch costs are
   capitalised rather than expensed as Space cost, so **the buildout that produces the 1.4 GW draws
   on the Space segment's capacity without appearing in the Space segment's revenue or margin.**
   The 86.2% of capex that is AI is **not** the whole of the AI segment's call on the company.

---

## 4. Cross-artifact adjudications — and the DA-24 contradiction, resolved

### 4.1 DA-24: two sibling artifacts, opposite verdicts. A28 resolves them, and the negative half has no power

| Artifact | Verdict | Test it ran |
|---|---|---|
| `business-model_methodology` §6 | **REFUTED** at consolidated and segment level | the calculation-linkbase **arc set into `OperatingIncomeLoss`** — exactly two arcs, `Revenue` at +1 and `CostsAndExpenses` at −1, so **no disposal-gain arc exists** |
| `risk_methodology` §1 | **PRESENT** | the calculation-linkbase **arc set into `CostsAndExpenses`** — `us-gaap:RestructuringCharges` and `us-gaap:ImpairmentOfLongLivedAssetsHeldForUse` are children at **weight +1** |

**Both verdicts are correct and they are about different halves of DA-24.**

- The **qualifying half** — a disposal gain sitting **above** the operating subtotal — is
  **REFUTED**. The arc set settles it structurally, which is what distinguishes a refutation from a
  non-observation.
- The **contamination half** — non-operating or non-recurring items folded **into** the operating
  line — is **PRESENT**. Restructuring and impairment sit **inside `CostsAndExpenses` at +1**.

**And the face-level census that concluded ABSENCE has no power to do so.** This is A28:
**A CONTAMINANT INSIDE A FILED SUBTOTAL IS ABSORBED BY IT.** A census that brackets a subtotal proves
the subtotal foots; it can prove **PRESENCE**, never **ABSENCE**. The `ratio-analysis` artifact's own
note that the census "closes to the dollar with zero residual at every period" is correct as
arithmetic and **is superseded as an inference**: read against the linkbase, the census is a proof of
presence. The identity `revenue − total costs = operating income` cannot detect the defect either,
for the same reason. **The test with power is the arc set; the subtraction and the census are
articulation checks, not detectors.**

**Magnitude, since it is not cosmetic** (`risk_methodology` §1, on
[sec8 p.5](https://agentii.ai/v/SPCX/sec8/5) and [sec8 p.40](https://agentii.ai/v/SPCX/sec8/40)):

| Measure | Value |
|---|---|
| DA-24 items as a share of the operating result (Q2 26 / H1 26 / Q2 25 / H1 25) | **1.4% / 0.4% / 20.1% / 23.6%** |
| DA-24 items inside the Q2 2026 improvement | **193 of 827 = 23.3%** |
| H1 2026 filed deterioration vs ex-item | **1,143 filed vs 1,375 ex-item — understated by 232, or 20.3%** |

**Carry-forward, and this is the part that must not be lost:** the `ImpairmentOfLongLivedAssetsHeldForUse`
arm is **UNEXERCISED** — no negative-filed instance exists, so no clearance is recorded. Reporting it
as "clean" would be reporting a test that cannot fail.

### 4.2 The `~65% GM` basis collapse **inside the register row**

The Data-Integrity Register's row for DA-23 records **"~65% GM"** for SPCX. That string reproduces on
**exactly one basis**: the **Space segment, three months 2026** — `(962 − 329) / 962 = 65.80%`
([sec8 p.30](https://agentii.ai/v/SPCX/sec8/30)). It does **not** reproduce consolidated (43.95% –
55.27%), nor on Connectivity 3M26 (`2,231 / 4,291 = 51.99%`), nor on AI 3M26
(`1,455 / 2,561 = 56.81%`). **The register row names no basis.** That is a **DA-30 basis collapse
inside the register itself** — the defect class the register registers, present in its own evidence
column. It is corrected by reference here, not silently.

Two further consequences for that row:

- **`65.8%` is two different quantities in two different 001 artifacts.** It is Space's Q2 **gross
  margin** `(962 − 329) / 962 = 65.80%` **and** Connectivity's Q2 **revenue growth** (p.43). One
  string, two quantities, no basis field — the same collapse, twice.
- **DA-23's detector is declared near-useless at this issuer** — the gross-profit bound is *"a false
  negative at every level at SPCX, ~65% GM."* So the DA-23 column for SPCX is **UNEXERCISED**, not
  CLEAN, and the "~65% GM" figure is the reason it is unexercised.

### 4.3 DA-30 — SEVEN instances, and the worst of them is a 46.47 pp inversion

| # | Concept | Basis A | Basis B | Spread | Where |
|---|---|---|---|---|---|
| 1 | `12.3% of revenue` | Space ÷ consolidated = 12.31% | Launch Services ÷ ex-AI = 12.34% | both round to the quoted string | business-model §1.5 |
| 2 | `NetIncomeLoss`, key `2026-06-30` | **4,817 = SIX months** | **541 = THREE months** (same fiscal year) | **8.9× on one key** | business-model §10 / [sec8 p.5](https://agentii.ai/v/SPCX/sec8/5) |
| 3 | Net loss, H1 2026 | `NetIncomeLoss` = 4,817 | attributable to common = 5,488 | **671 (13.9%)** | business-model §10 |
| 4 | `us-gaap:Assets` | true 192,770 / 92,079 | served `reported` = 25,124 = a **cash subtotal** | **7.7×** | business-model §12 (p.12) |
| 5 | `CashCashEquivalentsRestrictedCash…` | correct for 2025-12-31 = 25,124 | served `reported` = 11,501 = the **2024** opening balance | **one year** | business-model §12 (p.9) |
| 6 | Starlink subscribers | `As of` period-end 12.0M → implies +100.0% | disclosed +101.2%, requiring an **undisclosed average** | 1.2 pp | business-model §12 / [sec8 p.36](https://agentii.ai/v/SPCX/sec8/36) |
| 7 | **`operating_margin`** | filed consolidated `(2,086)/12,508 = −16.68%` | served `3,726/12,508` = **AI segment loss ÷ consolidated revenue** | **+29.79% vs −16.68% = 46.47 pp** | `ratio-analysis` §2.5 |

**Instance 7 is the single largest distortion this thesis has found**, and it is a **basis
substitution in a served ratio**: it inverts a filed **−16.68%** into **+29.79%**, a **46.47
percentage-point swing**. It is established by cell, not by prose — the AI table's own identity
closes exactly at all four periods (`2,561 − 3,818 = (1,257)`; `737 − 2,261 = (1,524)`;
`3,379 − 7,105 = (3,726)`; `1,465 − 3,925 = (2,460)`).

### 4.4 `OperatingIncomeLoss` fails twice, exactly — a different substituted member each period

The platform's `computed` value for `OperatingIncomeLoss` is `−4,578`. It is reproducible —
**and it is not the filing's number, in either direction**:

```
-4,578  =  3,379 (AI segment, SIX-month revenue)        - 7,957 (Q2 total costs)
-4,615  =    426 (the ADVERTISING segment, Q2 2025)     - 5,041 (Q2 2025 total costs)
```

Two exact reproductions; **a different substituted member in each** (one segment, one sub-segment
axis, and mismatched durations in the first). The filing's own six-month subtraction is
`12,508 − 14,594 = (2,086)`. Meanwhile the served `reported` is **+143** against a filed **`(143)`**
([sec8 p.5](https://agentii.ai/v/SPCX/sec8/5)). **`computed` may not be cited as a derivation;
`reported` is not the filed value; and NEITHER wins by default.** At SPCX the row loses on both
counts, and at RKLB four rows in one filing resolved four different ways, one of them to neither.

### 4.5 `validate_calculation`'s `pass` is not a sign attestation

The instrument returns **two `pass` verdicts with `diff == 0` on sign-stripped magnitudes** for this
accession. **A pass is not evidence about sign.** Recommended census vocabulary, carried as C-2:
distinguish **`pass-that-certifies-a-sign`** from **`pass-vacuous`**. Any consumer filtering on
`status == pass` receives wrong-signed values here. Two further failure modes are on record for this
tool: `pass` **when both sides were stripped**, and **ZERO ROWS on a filed concept** — a zero-row
return is evidence about the **tag**, not about the filing.

### 4.6 `$(1,257)M` IS FILED — and this artifact corrects the record in three directions

The **AI segment loss from operations** is disclosed as **`$(1,257)M` for Q2 2026** in **four filed
venues**, plus the call:

| Venue | Location | What it prints |
|---|---|---|
| Note 18, Segment Information | [sec8 p.30](https://agentii.ai/v/SPCX/sec8/30) | `Income (loss) from operations \| (542) \| 1,656 \| (1,257) \| (143)` — **AI as its own column** |
| MD&A, AI Segment Results | [sec8 p.44](https://agentii.ai/v/SPCX/sec8/44) | the full cost stack: `2,561 − 1,106 − 2,178 − 532 − 2 = (1,257)`, total costs `3,818` |
| MD&A narrative prose | [sec8 p.45](https://agentii.ai/v/SPCX/sec8/45) *(located by `operational-kpi` §7.1; not read by this artifact)* | *"AI loss from operations for the three months ended June 30, 2026 decreased by $267 million, or 17.5%…"* |
| Non-GAAP Segment Adj. EBITDA reconciliation | [sec8 p.46](https://agentii.ai/v/SPCX/sec8/46) *(located by `operational-kpi` §7.1; not read by this artifact)* | repeats `(542) \| 1,656 \| (1,257) \| (143)` |

**An earlier resolution claiming this figure was "DERIVED, never filed" is FALSE and has now been
corrected from three independent directions.** A DERIVED figure cannot have a filed cost stack behind
it summing to a filed total, and **a DERIVED grade here would fail P4's own logic** — it attaches the
weaker grade to the stronger source, and it *understates what the issuer discloses*, which is the
opposite failure from the usual one and just as damaging.

**Correction to the T902 brief's page list.** The brief records the four venues as *"pp. 30, 31, 44,
45, 46"*. I read **p.31** directly: it is the **six-month** segment table and prints the AI
**H1** figure `(3,726)`, not `(1,257)`. `(1,257)` is a **three-month** figure and appears on the
**quarterly** tables only. **The correct venue set is pp. 30, 44, 45, 46** — `{Note 18, MD&A table,
MD&A prose, Non-GAAP reconciliation}`. The correction is recorded because a page list that resolves
to a page not carrying the figure is the same class of defect this artifact exists to document.

### 4.7 DA-29 — the `$671M` residual, refused rather than derived

DA-29's mechanical test: **if any term in a reconciliation appears NOWHERE in the source, the check
is a BACK-SOLVE, and a back-solve closes exactly, so it cannot be caught on the closure.**
The `$671M` bridge between the two printed net-loss lines (§2.5) has **no printed term**, and
`us-gaap:ProfitLoss` — the concept that would carry a pre-NCI total — returns **ZERO facts** on this
accession, so no reconciling concept exists. **It is recorded and refused, not decomposed.** At BWXT,
by the same test, a **`$90.7M`** clearance term appeared in no filing (the filed figure was
`$775.1M`). **A reconciliation that closes is not a check.**

---

## 5. PIL-6 — discharged, not clean; eleven of thirty-one are contaminated

`wrong_if: count_of_spcx_growth_figures_unclassified_for_entity_boundary_effects > 0`.
**The counter is ZERO: 31 of 31 classified.** The falsifier is **DISCHARGED — not fired.**

**This is recorded as a pass of the test, not as a clean bill**, and the two halves must travel
together:

- **11 of the 31 are CONTAMINATED** by entity-boundary effects. The discharge is a statement about
  **classification**, not about **usability**. **A growth figure that has been correctly labelled
  "contaminated" is still contaminated.**
- The artifact that created the exposure is **001's own business-model artifact**, whose flagship
  figure carries it — `+$1,824M` was reported as evidence of *migration*, and it is **48.7% of the
  quarter's growth arising because an entity was acquired** (§2.3).
- **PIL-6 therefore moves AWAY from its falsifier firing and TOWARD its named case being true, and
  larger than named.**

**Register gap (C-1), referred to the Phase 7 ledger.** **No registered DA covers common-control
recasting across a change of reporting entity.** DA-21 covers management-drawn segment boundaries;
DA-28 covers capital-structure discontinuity. The **measured** cost at SPCX: **34.3 points** on a
reported growth rate, **48.7%** of a quarter's growth contribution, and **6.0 points** on the
flagship share statistic. The detector needs no filing and is mechanical: *for each issuer, find a
segment whose comparative-period revenue exceeds the entity's revenue in the period before the
segment's legal parent was consolidated.* SPCX's signature is `AI H1 2025 = 1,465` against an xAI
merger date of 2026-02-02. The 23 issuers DA-26 already flagged are the natural first pass.

---

## 6. One number per purpose — what 009 and 011 may cite, and at what grade

**This is the operative table.** One number per purpose, with its basis and its grade. A figure cited
without the basis column is a basis collapse (DA-30) regardless of whether the number is right.

| Purpose | Cite this | Basis / label that MUST travel with it | Grade | Source |
|---|---|---|---|---|
| Installed compute capacity | **1.4 GW** @ 2026-06-30 | "AI segment, **GPU nameplate** (GPU count × all-in GPU draw); not IT load, not facility draw" | **DEMONSTRATED** | [sec8 p.36](https://agentii.ai/v/SPCX/sec8/36) |
| Facility-side power (planning) | **2.1 GW** expected / **2.8 GW** target | "**implied** by the issuer's **forward end-2027** ratio applied to the delivered nameplate — **projection, not a delivered draw**" | **MODELED** | [sec8 p.36](https://agentii.ai/v/SPCX/sec8/36) × [ect1 p.4](https://agentii.ai/v/SPCX/ect1/4), [ect1 p.1](https://agentii.ai/v/SPCX/ect1/1) |
| Nameplate growth rate | **+250%** | "**within-xAI rate surfaced by recasting**; comparator predates consolidation by 7 months; **NOT SPCX capital deployment**" | **DERIVED** (arithmetic on a filed cell) | [sec8 p.36](https://agentii.ai/v/SPCX/sec8/36) |
| SPCX's own AI deployment | **$15,828M** Q2 AI capex | "capitalising 0.4 GW of nameplate = **$39.6M/MW nameplate / $26.4M/MW facility-side**; an upper bound" | **MODELED** | [sec8 p.30](https://agentii.ai/v/SPCX/sec8/30) + [ect1 p.3](https://agentii.ai/v/SPCX/ect1/3) |
| Consolidated revenue growth | **+91.9%** Q2 / **+53.7%** H1 | "as filed, **entity-boundary contaminated**" | **DEMONSTRATED** | [sec8 p.40](https://agentii.ai/v/SPCX/sec8/40) |
| Growth excluding the acquired entity | **+57.6%** Q2 / **+36.8%** H1 | "**ex-AI**, computed from filed segment cells; 34.3 pp / 16.9 pp below filed" | **DERIVED** | [sec8 p.13](https://agentii.ai/v/SPCX/sec8/13), [sec8 p.40](https://agentii.ai/v/SPCX/sec8/40) |
| AI's share of growth | **48.7%** Q2 / **43.8%** H1 | "computed from filed segment cells; ties exactly" | **DERIVED** | [sec8 p.13](https://agentii.ai/v/SPCX/sec8/13) |
| AI segment revenue | **2,561** Q2 / **3,379** H1 | filed segment cell; prior-year comparatives = **737 / 1,465**, both **pre-merger** | **DEMONSTRATED** | [sec8 p.13](https://agentii.ai/v/SPCX/sec8/13), [sec8 p.44](https://agentii.ai/v/SPCX/sec8/44) |
| AI operating result | **$(1,257)M** Q2 / **$(3,726)M** H1 | filed four ways; **do not** report as DERIVED | **DEMONSTRATED** | [sec8 p.30](https://agentii.ai/v/SPCX/sec8/30), [sec8 p.44](https://agentii.ai/v/SPCX/sec8/44) |
| Consolidated operating margin | **−16.68%** H1 | `(2,086)/12,508` — the filed basis | **DERIVED** | [sec8 p.5](https://agentii.ai/v/SPCX/sec8/5) |
| Space segment gross margin | **65.80%** 3M26 | "(962 − 329)/962 — **SEGMENT basis**; does NOT reproduce consolidated; the register's bare '~65% GM' is this and only this" | **DERIVED**, segment basis mandatory | [sec8 p.30](https://agentii.ai/v/SPCX/sec8/30) |
| Space revenue boundary | customer launches only | *"Our Space segment revenue only reflects our customer launches and customer activities"* | **DEMONSTRATED** | [sec8 p.36](https://agentii.ai/v/SPCX/sec8/36) (also p.35) |
| Space launch activity | **10 of 38 = 26.3%** customer launches Q2 | "the other 73.7% are internal and produce no Space revenue **by design**" | **DERIVED** | [sec8 p.35](https://agentii.ai/v/SPCX/sec8/35) |
| Net loss | **$(4,817)M** H1 **vs $(5,488)M** attributable | "**basis must be named** — 13.9% apart; EPS is struck on 5,488" | **DEMONSTRATED** | [sec8 p.5](https://agentii.ai/v/SPCX/sec8/5) |
| Shareholders' equity | **127,224** @ 2026-06-30 | "**post-IPO**; the comparative 2,573 is 49.46× smaller; **not comparable as a denominator**" | **DEMONSTRATED** | [sec8 p.4](https://agentii.ai/v/SPCX/sec8/4) |

**Which of the three GW figures for which purpose — the short form:**

- **1.4 GW** is quotable as **filed installed GPU nameplate, AI segment**, and for **nothing else**.
  It is not IT load, not facility draw, not energy consumption, and it is not a series spanning one
  owner.
- **2.1 GW** is quotable for **power, cooling, electrical-equipment and interconnect planning** — as
  a **projection from the issuer's own forward expected case**, never as a delivered draw.
- **2.8 GW** is quotable only as **the issuer's tentative target**, and it is the reading on which
  **PIL-4's falsifier fires**.
- **No figure in the corpus reports delivered facility-side power.** A downstream thesis that needs
  one must either derive it under a named multiple or record it as **UNEVIDENT**.

---

## 7. What could NOT be verified, and why — `UNEXERCISED` and `UNEVIDENT` are not `CLEAN`

| Item | Disposition | Why |
|---|---|---|
| **Delivered facility-side power draw** | **UNEVIDENT** | No figure exists anywhere in the corpus at any basis. Established by reading the pages that would carry it (pp. 30, 31, 36, 40, 44) — not by a keyword zero |
| **PUE proper** | **UNRESOLVABLE-FROM-PUBLIC-SOURCES** | `PUE` and *"power usage effectiveness"* return zero hits in the 10-Q; no benchmark is carried on the platform. Bounded ≈1.3–1.7×, straddling the threshold. Not multiplied against the 1.4 GW (§1.6) |
| **Q1 2026 nameplate (1.0 GW)** | **transcript-only** | [ect1 p.3](https://agentii.ai/v/SPCX/ect1/3) only. The 10-Q files two endpoints (0.4 / 1.4) and no 3M26 nameplate. The `$39.6M/MW` figure inherits this |
| **Whether the capex-per-MW rate held in Q1** | **NOT TESTED** | Q1 capex was not read; with one observation the rate is a single point, not a trend |
| **`get_segment_data(SPCX)`** | **UNVALIDATED-BY-PLATFORM** | Hard-errors (`column "k" does not exist`). Elsewhere the same tool reports a `total_revenue` that sums several served facts across **two years and two durations with no de-duplication** (`segment_coverage_pct 116.2` masking a **302.1%** overlap). **Treat its output as unusable.** Every segment figure in this artifact comes from a direct page read, not from that surface |
| **`data_freshness` (all XBRL tools)** | **UNUSABLE** | Reports `2027-04-12` — **seven months in the future** of `as_of = 2026-09-18`. Reproduces A11 exactly. No corpus-version endpoint exists, and the freshness stamps reachable **disagree** (2026-08-21 / 08-25 / 08-26). Hence `corpus_version: "UNPINNED"` |
| **`ImpairmentOfLongLivedAssetsHeldForUse` arm of DA-24** | **UNEXERCISED** | The arc is present at weight +1, but **no negative-filed instance exists**, so no clearance is recorded. A test that cannot fail is not a passing test |
| **DA-23's gross-profit bound at SPCX** | **UNEXERCISED** | The statements carry **no gross-profit line**, and the detector is declared a false negative at every level at ~65% GM. The detector cannot act here; that is not the same as passing |
| **Register row "~65% GM"** | **basis established by reproduction only** | The register carries **no basis field**, so the basis is recoverable only by finding the one construction that reproduces it (§4.2) |
| **The brief's "7 and 11 months"** | **not reproducible as stated** | The filed separations are **7 months** (AI comparative close 2025-06-30 → xAI Merger 2026-02-02) and **10.2 months** (X Merger 2025-03-28 → xAI Merger 2026-02-02). No filed date pair yields 11 months |
| **2025 three-month share-based compensation** | **NOT READ** | Its absence is why the 2025 columns of the Adjusted EBITDA reconciliation are recorded **NOT READ**, not fitted and not reported as a pass |
| **Common stock par line ($0.001)** | **incomplete capture** | Leaves a **13** residual in the equity section — recorded as an incomplete capture, **not** as a gap in the filing |

**The distinction this table exists to preserve:** *CLEAN* means a test ran and the subject passed.
*UNEXERCISED* means the test could not act. *UNEVIDENT* means the quantity has no source. **None of
the last two may be reported as a pass**, and the register will drift if they are.

---

## 8. Corrections to 001 and to the inherited record

1. **The `—` in the AI H1 2025 column is FALSE** — and it is the PIL-6 evasion. 001's revenue table
   reads `| AI (Grok, X, compute) | $2,561M | 32.8% | $3,379M | — | — |`. **The filing prints AI
   H1 2025 revenue as `$1,465M`** ([sec8 p.44](https://agentii.ai/v/SPCX/sec8/44) Table 56:
   `2,561 | 737 | 247.5% | 3,379 | 1,465 | 130.6%`; independently
   [sec8 p.13](https://agentii.ai/v/SPCX/sec8/13) Table 17). The cell was not unavailable. **The
   blank concealed the very recast signature §2.2 had to be constructed to find** — the correct
   instinct (*"H1 2025 predates the xAI merger"*) reached by the wrong route, since the column's
   **presence** is the evidence of the recast.
2. **`1.4 GW is an IT load` is not the filing's statement** — and the error is one-directional
   (§1.2). The distinction is precisely what makes PIL-4's falsifier outcome basis-dependent:
   `2.00 > 1.5` fires and `1.50 = 1.5` does not, **on the same metric**, because the two readings put
   different quantities in the numerator.
3. **`$(1,257)M` is FILED, not DERIVED** — four venues plus the call (§4.6). The earlier
   "DERIVED, never filed" resolution is FALSE and has been corrected from three directions; **do not
   propagate it.**
4. **`+$1,824M` is not evidence of migration.** It is **48.7%** of the quarter's growth and it exists
   because an entity was acquired (§2.3).
5. **`65.8%` and `−56.3%` are two quantities each** (§4.2). `65.8%` is Connectivity's Q2 revenue
   **growth** *and* Space's Q2 gross **margin**. `−56.3%` is the Space operating margin **including
   SG&A** (`(962 − 1,504)/962`); after R&D alone it is **−46.05%** (`(962 − 329 − 1,076)/962`). Both
   are Q2 figures, both correct as calculations, **both labels wrong**.
6. **The AI operating line's H1 direction is the OPPOSITE of its Q2 direction on the same line**:
   Q2 *"decreased by $267 million, or 17.5%"* against H1 *"increased by $1,266 million, or 51.5%"*.
   001's `−17.5% narrowing` is a Q2 figure presented without its period and without its H1 reversal.
7. **`12.3% of revenue` is Space ÷ consolidated, and it is three things at once**: not "launch"
   (launch-only is **8.29%**); the denominator is entity-boundary contaminated (ex-AI **18.31%** Q2 /
   **17.32%** H1); and the sentence juxtaposes a Q2 share against H1 growth rates. **Direction
   survives every basis; level survives none.**

---

## Sources

> Every figure asserted above resolves to the page cited. Frontmatter `citations` lists only pages
> whose cells this artifact read directly; pages marked *(located by a sibling artifact)* are linked
> inline and attributed in the body.

| Figure | Source |
|---|---|
| Nameplate 1.4 / 0.4 GW (Table 51, under the `AI` heading); GPU-count × all-in-draw definition and the cooling/overhead exclusion; Space customer-boundary sentence | [SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36) |
| Facility-side 20 GW power-and-cooling / 15 GW power-plant-level by end-2027 | [SPCX Q2 2026 call p.4](https://agentii.ai/v/SPCX/ect1/4) |
| Compute basis: "closer to 10 than 5"; "over 2 gigawatts of compute" end-2026 | [SPCX Q2 2026 call p.1](https://agentii.ai/v/SPCX/ect1/1) |
| 1.4 GW up from 1 GW in Q1 and 400 MW a year earlier; $18.4B capex, ~$15.8B AI | [SPCX Q2 2026 call p.3](https://agentii.ai/v/SPCX/ect1/3) |
| Q2 2026 segment table (Table 42) incl. AI capex 15,828 and total 18,369 | [SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30) |
| H1 2026 segment table (Table 43) and Q2 2025 comparatives (Table 44) | [SPCX 10-Q p.31](https://agentii.ai/v/SPCX/sec8/31) |
| Revenue by type and segment (Table 17), all four periods | [SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13) |
| Launch counts (Table 48): customer 10 / internal 28 of 38 | [SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35) |
| Consolidated revenue and operating-loss bridge (Table 53): 91.9% / 53.7% | [SPCX 10-Q p.40](https://agentii.ai/v/SPCX/sec8/40) |
| AI segment MD&A (Table 56) and the closing cost stack | [SPCX 10-Q p.44](https://agentii.ai/v/SPCX/sec8/44) |
| Statements of operations, four periods | [SPCX 10-Q p.5](https://agentii.ai/v/SPCX/sec8/5) |
| Consolidated balance sheets | [SPCX 10-Q p.4](https://agentii.ai/v/SPCX/sec8/4) |
| Note 1: IPO **$85,675M** net; **xAI Merger 2026-02-02**; **X Merger 2025-03-28**; five-for-one split | [SPCX 10-Q p.11](https://agentii.ai/v/SPCX/sec8/11) |
| AI loss from operations narrative, p.45 *(located by `operational-kpi` §7.1)* | [SPCX 10-Q p.45](https://agentii.ai/v/SPCX/sec8/45) |
| Non-GAAP Segment Adjusted EBITDA reconciliation, p.46 *(located by `operational-kpi` §7.1)* | [SPCX 10-Q p.46](https://agentii.ai/v/SPCX/sec8/46) |
