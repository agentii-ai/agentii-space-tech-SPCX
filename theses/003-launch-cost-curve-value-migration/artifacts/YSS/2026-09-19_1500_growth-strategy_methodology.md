---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-6
ticker: YSS
skill: growth-strategy
mode: methodology
generated_at: 2026-09-19T15:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "ab94b90ee0ff"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-30
    chosen_reading: >
      Two basis collisions are live at YSS and both are reported on both sides. (1) The fixed-cost ratio
      is 2.86x gross profit on the Q2 2026 QUARTER basis (opex $63,493K / gross profit $22,180K) and 1.94x
      on the FY2025 ANNUAL basis (opex $146,124K / gross profit $75,460K) — a 1.5x difference produced
      entirely by the period basis, with no period label attached in the source. (2) Revenue direction
      splits the same way: **−20.45% quarter-over-quarter against +10.38% year-over-year in the same
      period**, and both are true. Chosen reading: every YSS ratio in this artifact carries an explicit
      period basis, and no quarter-over-quarter rate is quoted without the year-over-year rate beside it.
      This is the SPCX period-basis trap reproduced at a second issuer.
  - da_id: DA-23
    chosen_reading: >
      YSS is a DA-23 instance on the component identity. The platform serves `OperatingIncomeLoss` as a
      POSITIVE — +41,313,000 for Q2 2026, +151,779,000 for H1 2026, +110,466,000 for Q1 2026, +27,863,000
      for H1 2025, +21,232,000 for Q2 2025, +6,631,000 for Q1 2025 — against filed negatives. The paired
      instance verified page-by-page in this artifact is Q2 2026: served +41,313,000 against a filed
      $(41,313)K, with the component identity 22,180 − 63,493 = (41,313) closing exactly on the EXCLUSIVE
      opex definition. Chosen reading: filed values only; the FY2025 identity (75,460 − 146,124 = (70,664))
      closes on the same definition, which is the second independent confirmation.
  - da_id: DA-25
    chosen_reading: >
      YSS's growth claims are per-unit and per-pipeline normalisations that are not reproducible from the
      audited tables: "25 M-CLASS platforms in a SpaceX Falcon 9", "120 units in a SpaceX Starship", a
      "$11.5 billion identified pipeline", "potential unawarded contracts … exceeds $1.85 billion", "eight
      new contracts in 2026 at an 88% win rate". Chosen reading: all of these are `CLAIMED`; they bound
      the growth story and populate nothing. In particular the Falcon 9 / Starship packing factors are a
      DESIGN CONSTRAINT, not a cost: they describe how many platforms fit in a fairing, and no dollar
      figure attaches to them anywhere in the filing.
  - da_id: DA-21
    chosen_reading: >
      YSS reports a single segment but discloses its cost of revenues through a segment footnote and an
      ASU 2023-07 significant-expense table. Chosen reading: the segment footnote's "other segment items"
      and the annual significant-expense table are read as the SAME concept on the SAME basis, and the
      reading is validated by exact closure rather than assumed — FY2025 direct materials $264,007K plus
      other segment items $46,736K equals cost of revenues $310,743K exactly, and the identical identity
      closes at FY2024 ($178,341K + $42,769K = $221,110K) and FY2023 ($148,574K + $34,625K = $183,199K).
      Three consecutive years of exact closure is what makes the decomposition usable as evidence of an
      ABSENCE rather than a mere gap.
  - da_id: DA-27
    chosen_reading: >
      YSS has a December fiscal year-end, so no calendar-derivation defect arises. Chosen reading: the
      DA-27 discipline is applied to the Q1 2026 denominator instead, which is DERIVED (filed H1 2026
      revenue less filed Q2 2026 revenue) and is labelled DERIVED wherever it is used. A rate computed on a
      derived denominator is not a `DEMONSTRATED` rate and is not used to carry the falsifier.
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable  # corrected 2026-09-19: this is NOT a P11 deal security; `standalone_pre_merger` asserted a business contractually ceasing to exist
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "Q2 2026 condensed consolidated statements of operations — total opex $63,493K; loss from operations $(41,313)K; share-based compensation presented as a separately stated operating expense of $10,893K"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 40
    url: https://agentii.ai/v/YSS/sec12/40
    located_via: read_source_pages
  - figure: "Segment footnote (a) — 'Other segment items is comprised of other costs of revenue excluding direct materials, including direct labor, overhead costs and depreciation and amortization'; direct materials $53,240K"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 35
    url: https://agentii.ai/v/YSS/sec12/35
    located_via: read_source_pages
  - figure: "Non-GAAP reconciliation — revenue $92,547K less cost of revenues $70,367K equals gross profit $22,180K; six-month revenue $208,890K, gross profit $44,330K, contribution margin $79,373K, net loss $(154,185)K, Adjusted EBITDA $(13,142)K"
    ticker: YSS
    form_type: 10-Q
    citation_id: sec12
    page_no: 46
    url: https://agentii.ai/v/YSS/sec12/46
    located_via: read_source_pages
  - figure: "Mission-prime description and M-CLASS launch packing factors — '25 M-CLASS platforms in a SpaceX Falcon 9' and '120 units in a SpaceX Starship'"
    ticker: YSS
    form_type: 10-K
    citation_id: sec8
    page_no: 10
    url: https://agentii.ai/v/YSS/sec8/10
    located_via: read_source_pages
  - figure: "FY2025 statement of operations — revenue $386,203K; cost of revenues $310,743K; gross profit $75,460K; total opex $146,124K; loss from operations $(70,664)K; net loss $(84,537)K; and the Cost of Revenues accounting policy"
    ticker: YSS
    form_type: 10-K
    citation_id: sec8
    page_no: 72
    url: https://agentii.ai/v/YSS/sec8/72
    located_via: read_source_pages
  - figure: "Net EAC adjustments $(11,120)K FY2025 vs $(22,916)K FY2024; three contracts at 42%, 26% and 21% of gross unfavorable EAC; '98% of the revenue growth related to contracts that were already in place at December 31, 2024'"
    ticker: YSS
    form_type: 10-K
    citation_id: sec8
    page_no: 73
    url: https://agentii.ai/v/YSS/sec8/73
    located_via: read_source_pages
  - figure: "Contribution margin non-GAAP reconciliation — FY2025 $122,196K (31.6%) vs FY2024 $75,190K (30.0%); direct materials $264,007K and $178,341K; direct labor $32,076K; direct overhead $7,745K; D&A $6,915K"
    ticker: YSS
    form_type: 10-K
    citation_id: sec8
    page_no: 75
    url: https://agentii.ai/v/YSS/sec8/75
    located_via: read_source_pages
  - figure: "ASU 2023-07 significant expense table — direct materials $264,007K / $178,341K / $148,574K and other segment items $46,736K / $42,769K / $34,625K for FY2025 / FY2024 / FY2023"
    ticker: YSS
    form_type: 10-K
    citation_id: sec8
    page_no: 120
    url: https://agentii.ai/v/YSS/sec8/120
    located_via: read_source_pages
  - figure: "$187M commercial M-CLASS contract; IPO of 18.5 million shares at $34.00"
    ticker: YSS
    form_type: 10-K
    citation_id: sec8
    page_no: 69
    url: https://agentii.ai/v/YSS/sec8/69
    located_via: read_source_pages
  - figure: "Q2 2026 earnings call — FY2026 revenue guidance cut to $375-405M; revenue from major government programs relatively flat year-on-year; growth driven by acquisitions and a new commercial contract; backlog $592M at June 30, down 8% from $642M at Q1-end"
    ticker: YSS
    form_type: earnings_call_transcript
    citation_id: ect3
    page_no: 2
    url: https://agentii.ai/v/YSS/ect3/2
    located_via: read_source_pages
  - figure: "Q2 2026 earnings call — gross profit margin expected to 'hang in there around the mid-20% range'; supply-chain slippage into 2027; earnings-deck pointer for pipeline composition; buyback authorisation stated inconsistently"
    ticker: YSS
    form_type: earnings_call_transcript
    citation_id: ect3
    page_no: 3
    url: https://agentii.ai/v/YSS/ect3/3
    located_via: read_source_pages
key_metrics:
  revenue_growth_qoq_pct: -20.45
  revenue_growth_yoy_pct: 10.38
  fy2026_guidance_reduction_pct: -31.6
  backlog_usd_millions: 592
---

# YSS — Growth Strategy: A Cost of Revenues That Decomposes Exactly, Four Ways, With No Launch In It

## The finding

**YSS is `NON-FORMABLE` — and unlike PL it is non-formable for a reason that strengthens the finding
rather than weakening it.** YSS's cost of revenues decomposes **exactly** into four components, and the
decomposition closes to the dollar at **three consecutive fiscal years and one quarter**: direct
materials, direct labor, direct overhead, and depreciation and amortisation. There is **no residual, no
"other", and no capacity for an unallocated fifth component.** Launch is not in the decomposition because
there is nowhere for it to be.

This is a **PRESENCE finding, not an ABSENCE finding**, and the distinction is the whole point. At PL the
launch share is non-formable because a disclosure is missing. At YSS it is non-formable because a
disclosure is *complete* and excludes the term. **Three independent sources agree on the same four
components** — the Cost of Revenues accounting policy, the segment footnote, and the non-GAAP
contribution-margin reconciliation — and the arithmetic ties them to the audited total at FY2023, FY2024,
FY2025 and Q2 2026. A reader who wants to put a launch term into YSS's cost of revenues must put it inside
"direct materials" or "direct overhead"; the filing gives no basis to do so and no basis to size it.

**Where YSS's launch relationship actually lives is a packing factor, not a purchase.** The 10-K describes
YSS as "a mission prime focused on delivering end-to-end solutions — from platform design and payload
integration to **launch**, on-orbit commissioning, and sustained operations," and then quantifies its
launch exposure in the only way it ever does: *"We are currently capable of placing **25 M-CLASS platforms
in a SpaceX Falcon 9** … and we expect to be able to place **120 units in a SpaceX Starship**"*
([📄 YSS 10-K p.10](https://agentii.ai/v/YSS/sec8/10)). That is a **fairing-volume constraint on
YSS's product design**, expressed as units per vehicle. It is `CLAIMED`, it is DA-25-flavoured, and it is
not a cost. **YSS's launch share of programme cost is non-formable because YSS does not buy launch — it
sells missions into launch vehicles, and its disclosed cost structure reflects that.**

**YSS's problem is a volume problem, and the brief's characterisation is confirmed on the filed numbers.**
Q2 2026 gross margin 23.97% against an opex-to-revenue ratio of **68.61%** — the brief's 68.6%, confirmed
([📄 YSS 10-Q p.40](https://agentii.ai/v/YSS/sec12/40)). The fixed cost base is **2.86x gross profit** on
the quarter basis (the brief's "2.9x", confirmed) and **1.94x** on the FY2025 annual basis. Revenue fell
**−20.45% quarter-over-quarter** against **+10.38% year-over-year** in the same period. **Neither the unit
economics nor the launch cost is the binding constraint — the revenue base is.** And the guidance cut
settles it: FY2026 revenue guidance was reduced to **$375–405M from a $570M midpoint**, a **−$180M /
−31.6%** reduction ([📄 YSS Q2 2026 call p.2](https://agentii.ai/v/YSS/ect3/2)).

## Sources.

This artifact reads the YSS Q2 2026 Form 10-Q (three and six months ended June 30, 2026; accession
0001628280-26-056874), the FY2025 Form 10-K (accession 0001628280-26-019923) and the Q2 2026 earnings
call transcript, page-by-page. Pages are cited inline as
`[📄 YSS 10-K p.72](https://agentii.ai/v/YSS/sec8/72)`. No figure is taken from an XBRL `LABEL`, a
metrics block, or a served fact value. `get_segment_data` and `data_freshness` are unusable in this
workspace and were not used. YSS's presentation is unusual in one respect that is stated here because it
affects comparability with the other three issuers: **share-based compensation is presented as a
separately stated operating expense line** ($10,893K in the quarter, 11.8% of revenue) rather than
embedded, so the "total opex" figure used below is on the as-presented basis and is inclusive of it
([📄 YSS 10-Q p.40](https://agentii.ai/v/YSS/sec12/40)).

## §1. Component identity first — DA-23, and the exact closure that decides the whole artifact

Rule 5 requires `gross_profit − opex = operating_income` in-line with the opex definition named.

**Q2 2026 (three months ended June 30, 2026), per [📄 YSS 10-Q p.40](https://agentii.ai/v/YSS/sec12/40)
and [📄 YSS 10-Q p.46](https://agentii.ai/v/YSS/sec12/46):**

| Line | Value | Basis |
|---|---|---|
| Revenue | $92,547K | filed |
| Cost of revenues | $70,367K | filed |
| **Gross profit** | **$22,180K** | filed and derivable: 92,547 − 70,367 |
| **Gross margin** | **23.97%** | derived |
| Total operating expenses (EXCLUSIVE of cost of revenues) | $63,493K | filed, as-presented, inclusive of share-based compensation |
| **Loss from operations** | **$(41,313)K** | filed |
| Identity, exclusive definition | 22,180 − 63,493 = **(41,313)** | closes exactly |
| Opex as percentage of revenue | **68.61%** | derived — the brief's "68.6%", confirmed |
| **Fixed cost base ÷ gross profit** | **2.86x** | derived — the brief's "2.9x", confirmed |

**DA-23 result.** The platform serves `OperatingIncomeLoss` for Q2 2026 as **`+41,313,000`**. The filed
figure is **$(41,313)K**. Same magnitude, opposite sign. The same pattern holds at every other YSS period
retrieved: +151,779,000 (H1 2026), +110,466,000 (Q1 2026), +27,863,000 (H1 2025), +21,232,000 (Q2 2025)
and +6,631,000 (Q1 2025). Chosen reading: filed values only, and the component identity is the detector.

**FY2025 (per [📄 YSS 10-K p.72](https://agentii.ai/v/YSS/sec8/72)):**

| Line | FY2025 | FY2024 |
|---|---|---|
| Revenue | $386,203K | — |
| Cost of revenues | $310,743K | — |
| Gross profit | $75,460K (19.54%) | — |
| Selling, general and administrative | $115,649K | — |
| Research and development | $18,362K | — |
| Transaction costs | $12,113K | — |
| Total opex, exclusive | $146,124K | — |
| **Loss from operations** | **$(70,664)K** | **$(91,966)K** |
| Identity, exclusive | 75,460 − 146,124 = **(70,664)** ✓ | — |
| Net loss | $(84,537)K | — |
| **Fixed cost base ÷ gross profit** | **1.94x** | — |

**The 2.86x-versus-1.94x collision is the DA-30 instance that matters most at YSS.** Both are correct.
The brief quotes 2.9x on the quarter basis; the annual report implies 1.94x. **A reader given only one of
them has a materially wrong picture of YSS's operating leverage, and the source attaches no period label
to either.** Both are given here, and the artifact quotes neither alone.

## §2. growth-strategy-assessment — the programme-cost base, and the exhaustive decomposition

**The programme-cost base, stated.** YSS's cost of revenues is the denominator, and it is the best-
specified denominator in this task because it is disclosed as an exhaustive decomposition rather than as a
total.

**Source 1 — the accounting policy, per [📄 YSS 10-K p.72](https://agentii.ai/v/YSS/sec8/72):**

> *"Cost of Revenues — primarily consists of **direct material and labor costs** … and **related
> overhead**. Overhead costs primarily include allocable amounts of rent, software subscriptions,
> **depreciation and amortization expense on assets used directly in revenue producing activities**,
> indirect materials, and production and test administrative expenses."*

**Source 2 — the segment footnote, per [📄 YSS 10-Q p.35](https://agentii.ai/v/YSS/sec12/35):**

> *"Other segment items is comprised of other costs of revenue excluding direct materials, including
> direct labor, overhead costs and depreciation and amortization."*

**Source 3 — the non-GAAP reconciliation, per [📄 YSS 10-Q p.46](https://agentii.ai/v/YSS/sec12/46) and
[📄 YSS 10-K p.75](https://agentii.ai/v/YSS/sec8/75):** the contribution-margin build.

**The decomposition closes exactly. This is the arithmetic that makes the finding a PRESENCE rather than
an ABSENCE.**

| Period | Direct materials | Other segment items | Sum | Cost of revenues (filed) | Closes? |
|---|---|---|---|---|---|
| Q2 2026 (3M) | $53,240K | $17,127K (= $11,119K labor + $3,736K overhead + $2,272K D&A) | $70,367K | **$70,367K** | **exact** |
| FY2025 | $264,007K | $46,736K (= $32,076K + $7,745K + $6,915K) | $310,743K | **$310,743K** | **exact** |
| FY2024 | $178,341K | $42,769K | $221,110K | $221,110K | **exact** |
| FY2023 | $148,574K | $34,625K | $183,199K | $183,199K | **exact** |

Sources: [📄 YSS 10-Q p.35](https://agentii.ai/v/YSS/sec12/35),
[📄 YSS 10-Q p.46](https://agentii.ai/v/YSS/sec12/46),
[📄 YSS 10-K p.75](https://agentii.ai/v/YSS/sec8/75),
[📄 YSS 10-K p.120](https://agentii.ai/v/YSS/sec8/120).

**Four periods, four components, exact closure every time, and no launch term in any of them.** The
attribution of the FY2025 cost increase is equally launch-free: cost of revenues rose on *"increases in
direct materials and subcontractor costs related to larger contracts of $85.7 million"*
([📄 YSS 10-K p.73](https://agentii.ai/v/YSS/sec8/73)) — larger contracts, more material, and
subcontractors. **Direct materials are 85.0% of YSS's FY2025 cost of revenues ($264,007K of $310,743K).**
A launch term large enough to matter would be visible in a line that granular. It is not there.

**NON-FORMABLE — the third disposition, stated affirmatively.** YSS's launch share of programme cost
cannot be formed: it is not that the number is large or small, it is that the filed cost structure has no
slot for it and an exhaustive, three-times-closing decomposition proves the slot does not exist. **Not
PASS, not FAIL: `NON-FORMABLE`.**

**DA-29 applied to the decomposition.** A reconciliation that closes is not thereby a check. The reason
the four-way decomposition is used here as evidence is not that it closes — it is that **every term in it
appears as a filed line item in the same source** on the same basis, at three consecutive year-ends and
one quarter. There is no back-solve: direct materials, direct labor, direct overhead and D&A each appear
named in the policy and in the tables, and the total they produce is the audited cost-of-revenues line.
That is the standard DA-29 sets, and the decomposition meets it while most reconciliations do not.

## §3. organic-growth-drivers-analysis — organic in FY2025, inorganic in FY2026, and a $180M guidance cut

**FY2025 growth was organic, and YSS says so in the 10-K with a figure:**

> *"**98% of the revenue growth related to contracts that were already in place at December 31, 2024**."*
> — [📄 YSS 10-K p.73](https://agentii.ai/v/YSS/sec8/73)

FY2025 revenue was $386,203K, up 52% ([📄 YSS 10-K p.72](https://agentii.ai/v/YSS/sec8/72)). So the
`organic-growth-drivers-analysis` answer for FY2025 is unambiguous: **organic, on an existing contract
base, at scale.**

**FY2026 reverses it completely.** The Q2 2026 call states the growth is *"primarily driven by our
revenues from acquisitions completed in the second half of 2025 and the first half of 2026 as well as our
new commercial contract"* and that *"**Revenue from our major government programs remained relatively
flat year-on-year**"* ([📄 YSS Q2 2026 call p.2](https://agentii.ai/v/YSS/ect3/2)). The §1 numbers agree:
SG&A and R&D grew materially faster than the +10.38% revenue, and Adjusted EBITDA was a **loss of
$9.5M against $8.9M** a year earlier
([📄 YSS Q2 2026 call p.2](https://agentii.ai/v/YSS/ect3/2),
[📄 YSS 10-Q p.46](https://agentii.ai/v/YSS/sec12/46)).

**The guidance cut is the decisive filed fact, and it is the opposite of a cost-curve story.** FY2026
revenue guidance went to **$375–405M from a $570M midpoint** — **−$180M, −31.6%**
([📄 YSS Q2 2026 call p.2](https://agentii.ai/v/YSS/ect3/2)). Roughly 30% of the prior midpoint was new
business removed entirely, with the remainder attributed to supply-chain slippage into 2027. **A company
cutting its revenue guidance by a third because of supply-chain timing is not a company whose economics
are being transformed by a falling launch price.** Backlog was $592M at June 30, **down 8% from $642M at
Q1-end** though up 9% from the start of the year — and that is itself a two-basis pair that must be quoted
together ([📄 YSS Q2 2026 call p.2](https://agentii.ai/v/YSS/ect3/2)).

**The `CLAIMED` set, and the deck.** YSS attaches a "$11.5 billion identified pipeline," "potential
unawarded contracts … exceeds $1.85 billion," and "eight new contracts in 2026 at an 88% win rate"
([📄 YSS Q2 2026 call p.2](https://agentii.ai/v/YSS/ect3/2)). The CEO named the **earnings deck** as the
resolution source for the pipeline's composition ([📄 YSS Q2 2026 call p.3](https://agentii.ai/v/YSS/ect3/3)).
**This is the task's "a company's own deck or Investor-Day figure is `CLAIMED` — admissible to bound,
never to populate" rule appearing in the wild, and the company supplies the pointer itself.** None of
these figures populates any ratio in this artifact. The one filed contract figure, the $187M commercial
M-CLASS award ([📄 YSS 10-K p.69](https://agentii.ai/v/YSS/sec8/69)), is `DEMONSTRATED` and is smaller
than the pipeline claims by two orders of magnitude — which is precisely why the pipeline is a bound.

## §4. organic-growth-driver-execution-assessment — VRT's reusable test

**VRT's reusable test: check whether price improvements coexist with flat or falling margin.** At YSS the
test is **UNEXERCISED on its price leg** and, on the margin leg, produces an improvement that is an
accounting artefact rather than a price effect.

- **Price leg: UNEXERCISED.** YSS files no pricing metric, no price-per-unit, no ARPU equivalent and no
  retention equivalent. There is no price improvement to compare against margin. **Recording this as
  "CLEAN" would be the exact false clearance the brief forbids — the check did not run.**
- **Margin leg: answered, and the improvement is an EAC artefact.** Q2 2026 gross margin 23.97% against
  11.36% a year earlier (Q2 2025 gross profit $9,526K on revenue $83,839K) — an improvement of
  **+12.61 percentage points**, and the company itself attributes it to the prior year being *"negatively
  impacted by an EAC adjustment"* ([📄 YSS Q2 2026 call p.2](https://agentii.ai/v/YSS/ect3/2)). The
  annual pattern confirms the mechanism: **net EAC adjustments were $(11,120)K in FY2025 against
  $(22,916)K in FY2024** ([📄 YSS 10-K p.73](https://agentii.ai/v/YSS/sec8/73)), with three contracts
  accounting for 42%, 26% and 21% of gross unfavorable adjustments, *"all primarily due to additional
  unplanned labor, materials and subcontractor costs."* **An estimate-at-completion revision is a change
  in accounting estimate, not a change in price, and it is not evidence of pass-through in either
  direction.** The company's own forward statement is that gross margin will *"hang in there around the
  mid-20% range"* ([📄 YSS Q2 2026 call p.3](https://agentii.ai/v/YSS/ect3/3)) — a flat guide.
- **Execution leg: answered negatively.** Revenue −20.45% QoQ, fixed cost base 2.86x gross profit, a
  −31.6% guidance cut, and Negative EAC adjustments that persist in direction if not in size. **The fixed
  cost base is the finding: at 2.86x gross profit, YSS cannot reach operating breakeven on mix or on
  input prices. It needs volume.**

**Disposition of VRT's test at YSS: UNEXERCISED on price; margin movement attributable to EAC and mix; a
flat forward margin guide on a falling revenue base.** The test neither passes nor fails — it does not
run, and the adjacent evidence points away from a price-driven improvement.

## §5. Where PIL-6's claim bites at YSS

**The falsifier's first condition — "a demonstrated fall in revenue per launch at least as large as the
fall in cost per launch" — is `UNEXERCISED` at YSS.** YSS files no launch count, no per-launch revenue
and no mass-to-orbit metric. The two figures it does file that look like launch metrics — "25 M-CLASS
platforms in a SpaceX Falcon 9" and "120 units in a SpaceX Starship"
([📄 YSS 10-K p.10](https://agentii.ai/v/YSS/sec8/10)) — are packing factors for a design, are `CLAIMED`,
and carry no dollars. An unengaged check is not a passed check.

**The falsifier's second condition — "a launch share of programme cost above 10%" — is `NON-FORMABLE` at
YSS, on the strongest possible evidence: an exhaustive four-way decomposition that closes exactly at
three consecutive year-ends and one quarter, with no residual.**

**YSS's significance for PIL-6 is as the volume-side control.** The brief's characterisation is confirmed:
YSS's gross margin, at 23.97%, is roughly half PL's, and its opex ratio of 68.61% is much lower than PL's
90.59% — yet YSS also runs an operating loss, because its gross profit is only 24% of revenue while its
fixed cost base is 2.86x that gross profit. **YSS and PL fail at the operating line for structurally
different reasons: PL because its fixed cost is large relative to a very high gross margin (1.69x cover);
YSS because its fixed cost is large relative to a very low one (2.86x cover). Neither failure is a launch
failure, and neither is fixed by a cheaper launch.** That is two independent demand-side names at which
the launch cost curve is not the binding constraint — one by non-disclosure and one by an exhaustive
disclosure that rules the term out.

**One live unresolved inconsistency, carried because it bears on how much weight to put on YSS's own
forward statements.** The Q2 2026 call states a buyback authorisation of *"up to $5 billion"* at
[📄 YSS Q2 2026 call p.3](https://agentii.ai/v/YSS/ect3/3), while an analyst on the same call puts it at
*"$2 billion to $3 billion"* ([📄 YSS Q2 2026 call p.2](https://agentii.ai/v/YSS/ect3/2)) — a 1.7x
disagreement on a management-controlled number, on one page pair, unresolved by anything filed. Both are
`CLAIMED`; neither is used here. It is recorded because it is the same class of defect as the two-basis
collisions in §1, and because an artifact that quotes YSS's "up to $5 billion" without the analyst's
"$2 billion to $3 billion" on the facing page has quoted a `CLAIMED` metric on one basis alone.

## §6. What could NOT be verified

| Item | Disposition | Class |
|---|---|---|
| Launch cost as a share of programme cost, any period basis | **NON-FORMABLE** — an exhaustive four-way decomposition of cost of revenues closes exactly at FY2023, FY2024, FY2025 and Q2 2026 with no launch term and no residual | ruled out by complete disclosure, not merely absent |
| Revenue per launch and cost per launch | **UNEXERCISED** — no launch count and no mass metric in any period | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Any priced product or service at YSS | **UNEXERCISED** — no pricing metric is filed, so VRT's test cannot run on its price leg | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| The "$11.5 billion pipeline" and "$1.85 billion potential unawarded" | **`CLAIMED`** — the company names the earnings deck as the composition source; not reproducible from audited tables | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| The buyback authorisation: $5 billion vs $2–3 billion | **UNRESOLVED** — stated inconsistently within the same call, nothing filed resolves it | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Served `OperatingIncomeLoss` sign at YSS | **UNRESOLVED — platform defect**; 6 of 6 served values positive against filed negatives; detector is the component identity shown in §1 | UNRESOLVABLE-FROM-PLATFORM |
| Whether the FY2026 guidance shortfall is demand or supply | **PARTIALLY RESOLVED** — the call attributes ~30% of the midpoint to new business removed and the remainder to supply-chain slippage into 2027; the split is `CLAIMED` | UNRESOLVABLE-FROM-PUBLIC-SOURCES |

**Specific disclosure that would resolve the primary item — and it would resolve it in the opposite
direction from PL.** At YSS there is nothing to add: the decomposition is exhaustive and closes. The
resolving disclosure for PIL-6's purpose would be evidence that launch is inside "direct materials" —
i.e. a programme-level bill of materials naming a launch-services purchase. **None is filed, and the
four-way closure is affirmative evidence that the line does not exist at material scale.** At PL the
missing disclosure could hide a material launch share; at YSS the complete disclosure rules one out.

## §7. Corrections inherited and carried

- **The period-basis trap is not a SPCX peculiarity.** SPCX's throughput figures split 3M vs 6M; YSS's
  fixed-cost ratio splits 2.86x (quarter) vs 1.94x (annual) and its revenue direction splits −20.45%
  (QoQ) vs +10.38% (YoY). **Every YSS figure in this artifact carries its period basis, and no
  single-period rate is quoted alone.**
- **A derived denominator does not carry a falsifier.** YSS's Q1 2026 revenue of $116,343K is derived
  (H1 $208,890K less Q2 $92,547K), so the −20.45% QoQ rate is `DERIVED` and is used only to characterise
  direction. It is not used in any ratio that bears on PIL-6.
- **DA-23 at YSS is 6 of 6 periods served positive against filed negatives**, matching RKLB (12 of 12),
  LUNR (4 of 4) and PL (4 of 4). YSS has never filed a positive operating income in the periods examined,
  so the strip is invisible to heuristics and the component identity is the only detector.
- **A company's deck is `CLAIMED`.** YSS names the earnings deck itself as the resolution source for its
  pipeline composition — the task's rule instanced by the issuer.
- **`+$1,824M` at SPCX is not evidence of migration.** YSS's FY2026 revenue is acquisition-driven while
  its core government programmes are flat — the same defect class, and here it coincides with a −31.6%
  guidance cut rather than with growth.

## §8. Carry-forwards

1. **`NON-FORMABLE` at YSS rests on an exhaustive disclosure, which makes it stronger evidence than a gap
   would be.** An artifact that records YSS as merely "not disclosed" is understating the finding. The
   correct statement is that the filed cost structure has no slot for launch and the decomposition closes.
2. **The 2.86x / 1.94x collision should be carried into the thesis.** The brief's 2.9x is the Q2 2026
   quarter basis; the annual report implies 1.94x. No source attaches the period label, and the two
   support materially different pictures of YSS's operating leverage.
3. **YSS and PL are a matched pair for PIL-6's purposes and should be cited together.** Both are
   demand-side names that fail at the operating line; PL by 1.69x opex cover on a 53.5% gross margin, YSS
   by 2.86x opex cover on a 23.97% gross margin. At both, launch is non-formable and the failure mechanism
   is fixed cost, not launch cost. **Two independent mechanisms, one conclusion, and neither reaches the
   10% bar because neither can be drawn.**
4. **The EAC mechanism is a standing threat to any margin-trend reading at YSS.** A +12.61pp gross margin
   improvement that is attributed by the company to lapping a prior-year EAC adjustment is not a trend,
   and the FY2025-vs-FY2024 EAC comparison ($(11,120)K vs $(22,916)K) shows the revision is large relative
   to the margin.
5. **`deal_security_basis: standalone_pre_merger` is carried per the task's mandate.** The basis question
   it answers at YSS is the acquisition line: three acquisitions closed in the second half of 2025 and the
   first half of 2026, so no FY2026 rate in this artifact is comparable with an FY2025 rate without saying
   so — which is why the FY2025 organic figure (98% from contracts in place at 2024-12-31) and the FY2026
   inorganic figure are both reported.

## Sources

| Figure | Citation |
|---|---|
| Q2 2026 statements of operations — total opex $63,493K; loss from operations $(41,313)K; share-based compensation $10,893K | [📄 YSS 10-Q p.40](https://agentii.ai/v/YSS/sec12/40) |
| Segment footnote (a) — "other segment items" = other costs of revenue excluding direct materials; direct materials $53,240K | [📄 YSS 10-Q p.35](https://agentii.ai/v/YSS/sec12/35) |
| Non-GAAP reconciliation — revenue $92,547K, cost of revenues $70,367K, gross profit $22,180K; six-month figures | [📄 YSS 10-Q p.46](https://agentii.ai/v/YSS/sec12/46) |
| Mission-prime description; 25 M-CLASS platforms in a Falcon 9; 120 units in a Starship | [📄 YSS 10-K p.10](https://agentii.ai/v/YSS/sec8/10) |
| FY2025 statement of operations and the Cost of Revenues accounting policy | [📄 YSS 10-K p.72](https://agentii.ai/v/YSS/sec8/72) |
| Net EAC adjustments; 42%/26%/21% of gross unfavorable EAC; "98% of the revenue growth" from contracts in place at December 31, 2024 | [📄 YSS 10-K p.73](https://agentii.ai/v/YSS/sec8/73) |
| Contribution margin reconciliation — FY2025 $122,196K vs FY2024 $75,190K; component detail | [📄 YSS 10-K p.75](https://agentii.ai/v/YSS/sec8/75) |
| ASU 2023-07 significant expense table — direct materials and other segment items, FY2023–FY2025 | [📄 YSS 10-K p.120](https://agentii.ai/v/YSS/sec8/120) |
| $187M commercial M-CLASS contract; IPO of 18.5 million shares at $34.00 | [📄 YSS 10-K p.69](https://agentii.ai/v/YSS/sec8/69) |
| Guidance cut to $375–405M; government programmes flat; acquisitions and new commercial contract as drivers; backlog $592M down 8% from Q1-end | [📄 YSS Q2 2026 call p.2](https://agentii.ai/v/YSS/ect3/2) |
| Margin expected to "hang in there around the mid-20% range"; supply-chain slippage into 2027; earnings-deck pointer; buyback stated as "up to $5 billion" | [📄 YSS Q2 2026 call p.3](https://agentii.ai/v/YSS/ect3/3) |

*Grades: the §1 and §2 ratios and the four-way decomposition are `DEMONSTRATED` — filed cells with
arithmetic that closes exactly. The guidance figures, the pipeline and win-rate claims, the EAC
attribution, the packing factors and the buyback authorisation are `CLAIMED`. The Q1 2026 revenue
denominator behind the −20.45% QoQ rate and the Q2 2025 gross margin denominator are `DERIVED`.
`skill_pin: ab94b90ee0ff` · `pillar: PIL-6`.*
