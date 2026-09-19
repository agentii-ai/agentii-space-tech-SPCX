---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-6
ticker: LUNR
skill: growth-strategy
mode: methodology
generated_at: 2026-09-19T15:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "ab94b90ee0ff"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: >
      LUNR is read as a DA-23 instance on the component identity, not on any sign heuristic.
      The platform serves `OperatingIncomeLoss` as a POSITIVE at every period retrieved —
      +47,136,000 (Q2 2026), +38,717,000 (H1 2025) and +87,231,000 (FY2025) — against filed
      negatives of identical magnitude, $(47,136)K, $(38,717)K and $(87,231)K. Chosen reading:
      every LUNR operating result in this artifact is taken from the FILED statement of
      operations on the page cited, never from the served fact. The detector is
      `gross_profit − opex = operating_income` on the exclusive opex definition, which closes
      exactly at Q2 2026 (35,866 − 83,002 = (47,136)) and at FY2025 (8,990 − 96,221 =
      (87,231)). Because LUNR has never filed a positive operating income in the periods
      examined, the strip is INVISIBLE to any heuristic that expects a loss-maker's served
      values to be negative. DA-23 is UNRESOLVABLE-FROM-PLATFORM: no public filing fixes the
      served sign.
  - da_id: DA-30
    chosen_reading: >
      Four separate two-basis collisions are live at LUNR and each is reported on BOTH bases
      rather than collapsed. (1) The launch-cost numerator exists as a Q2 2026 CASH outflow of
      $17M to SpaceX and as a Q2 2026 P&L amortisation charge of $7.1M — a 2.39x gap whose
      basis field is cash vs expense. (2) "Backlog" is asserted at $1.8 billion on the Q2 2026
      earnings call while the filing's "remaining performance obligations" are $814.7M — a
      2.21x gap on an undefined concept. (3) "Gross profit" is quoted at "$36 million" on the
      call on a revenue-minus-cost-of-revenues basis that EXCLUDES $14.9M of depreciation and
      amortisation; a D&A-inclusive reading of the same words is materially smaller. (4) The
      IM-4 estimate-at-completion adjustment is quoted at $14.7M for the quarter on the call
      against a filed accrued-contract-loss increase of $13.5M for the quarter and $16.2M for
      the half. Chosen reading: where a numerator or denominator in this artifact has a
      competing basis, both are stated with a basis field, and no ratio is quoted on one basis
      alone.
  - da_id: DA-25
    chosen_reading: >
      LUNR's call-level per-unit and programme aggregates — the $1.8 billion backlog, the
      "$36 million" gross profit, the $17M milestone — are normalised or re-aggregated figures
      not reproducible from the audited tables on the same basis. Chosen reading: they are
      admissible to BOUND a ratio and may not POPULATE one. Every ratio in this artifact whose
      numerator is a call figure is labelled CLAIMED and is carried as a bound only; the
      falsifier is tested exclusively on the filed amortisation figure.
  - da_id: DA-27
    chosen_reading: >
      LUNR's fiscal-period labels are calendar-consistent (December year-end), so no DA-27
      restatement is required — but the DA-27 discipline is applied to the LUNR/Lanteris
      discontinuity instead: the acquisition closed in January 2026, so Q2 2026 is the second
      full post-acquisition quarter and FY2025 is entirely pre-acquisition. Chosen reading:
      every LUNR period in this artifact is stamped pre- or post-Lanteris, and no period-over-
      period rate is quoted across that line without saying so.
  - da_id: DA-21
    chosen_reading: >
      LUNR operates in ONE reportable segment (10-Q Note 21), so no segment boundary exists to
      cross and the consolidated denominator IS the segment denominator. Chosen reading: the
      ratio is consolidated by construction, and this is stated rather than left implicit —
      the absence of a segment split is the reason a denominator can be formed here at all,
      since at the multi-segment issuers in this task (PL, SATS) the programme cost sits inside
      one segment of several.
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable  # corrected 2026-09-19: this is NOT a P11 deal security; `standalone_pre_merger` asserted a business contractually ceasing to exist
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "Q2 2026 and H1 2026 condensed consolidated statements of operations — total revenues $206,168K and $392,898K; net loss attributable to the Company $46.4M and $83.8M"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 8
    url: https://agentii.ai/v/LUNR/sec76/8
    located_via: search_keyword_in_source
  - figure: "Amortisation of deferred contract costs for subcontracted launch services $7.1M and $14.3M (3M/6M 2026) vs $7.6M and $15.6M (3M/6M 2025); launch delay fees $0.8M and $2.3M in 2025 and NIL in 2026"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 24
    url: https://agentii.ai/v/LUNR/sec76/24
    located_via: search_keyword_in_source
  - figure: "IM-3 and IM-4 loss contracts; remaining performance obligations $814.7M"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 25
    url: https://agentii.ai/v/LUNR/sec76/25
    located_via: read_source_outline
  - figure: "Note 21 — the Company operates in one reportable segment"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 43
    url: https://agentii.ai/v/LUNR/sec76/43
    located_via: search_keyword_in_source
  - figure: "Results of operations — product revenue $166.7M of total revenues $206.2M; operating loss $47.1M; net loss $62.8M (3M 2026)"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 51
    url: https://agentii.ai/v/LUNR/sec76/51
    located_via: read_source_outline
  - figure: "Cost of revenue variance — Lanteris acquisition, IM-3/IM-4 mission cost adjustments, NSN and OMES III and LTV contract cost"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 53
    url: https://agentii.ai/v/LUNR/sec76/53
    located_via: read_source_outline
  - figure: "Adjusted EBITDA reconciliation — depreciation and amortisation and share-based compensation components"
    ticker: LUNR
    form_type: 10-Q
    citation_id: sec76
    page_no: 56
    url: https://agentii.ai/v/LUNR/sec76/56
    located_via: read_source_outline
  - figure: "Amortisation expense for subcontracted launch services in cost of revenue — $29.8M and $10.1M for the years ended December 31, 2025 and 2024"
    ticker: LUNR
    form_type: 10-K
    citation_id: sec59
    page_no: 80
    url: https://agentii.ai/v/LUNR/sec59/80
    located_via: read_source_pages
  - figure: "FY2025 and FY2024 consolidated statements of operations — revenues $210,059K and $228,000K; loss from operations $(87,231)K"
    ticker: LUNR
    form_type: 10-K
    citation_id: sec59
    page_no: 61
    url: https://agentii.ai/v/LUNR/sec59/61
    located_via: read_source_pages
  - figure: "Purchase commitments — remaining non-cancelable launch obligations $58.1M ($38.5M due 2026, $19.6M due 2027), stated as mixing launch services and component development"
    ticker: LUNR
    form_type: 10-K
    citation_id: sec59
    page_no: 102
    url: https://agentii.ai/v/LUNR/sec59/102
    located_via: read_source_pages
  - figure: "Q2 2026 earnings call — $17 million operating cash outflow associated with the IM-4 milestone payment to SpaceX; backlog cited as $1.8 billion"
    ticker: LUNR
    form_type: earnings_call_transcript
    citation_id: ect13
    page_no: 2
    url: https://agentii.ai/v/LUNR/ect13/2
    located_via: read_source_pages
  - figure: "Q2 2026 earnings call — gross profit described as $36 million against negative $12 million in the prior-year quarter"
    ticker: LUNR
    form_type: earnings_call_transcript
    citation_id: ect13
    page_no: 3
    url: https://agentii.ai/v/LUNR/ect13/3
    located_via: read_source_pages
key_metrics:
  launch_amortisation_share_fy2025_revenue_pct: 14.19
  launch_amortisation_share_q2_2026_revenue_pct: 3.44
  launch_amortisation_numerator_change_yoy_pct: -6.6
  cost_of_revenues_growth_yoy_pct: 174.0
---

# LUNR — Growth Strategy: The Programme-Cost Base, and a Launch Share That Flips on a Denominator

## The finding

**The launch-cost share of programme cost IS formable at LUNR — and it is the only one of the four
issuers in this task where it is.** LUNR files launch as a period expense, in a named line, in both
formats, on two periods of history. The ratio can therefore be drawn rather than estimated.

**And on every pre-acquisition basis it CLEARS the 10% bar that PIL-6's falsifier names.** Launch
amortisation was 14.19% of FY2025 revenue, **14.82% of FY2025 cost of revenues** and **10.02% of
FY2025 total costs and expenses**; 15.87% / 15.17% / 11.81% on the H1 2025 (six-month) basis; and
16.70% / 13.51% / **10.64%** on the Q2 2025 (three-month) basis. On the gross-profit denominator the
launch charge is **331% of FY2025 gross profit** — the entire gross profit of the launch-services
demand side, three times over.

**Then it collapses to 2.80%–4.37% on every 2026 basis — and the collapse is not a cost-curve event.**
The numerator barely moved: $7.6M → $7.1M on the Q2 comparison (**−6.6%**), $15.6M → $14.3M on the H1
comparison (**−8.3%**). The denominator moved enormously: Q2 cost of revenues $62,156K → $170,302K
(**+174.0%**) and Q2 revenue $50,313K → $206,168K (**+309.8%**), because the **Lanteris** acquisition
closed in January 2026 and contributed $166,735K of product revenue containing no launch at all. This
is the same defect class as the `+$1,824M` item in thesis 001: a migration-shaped reading that exists
because an entity was acquired, not because a curve moved.

**The consequence for PIL-6 is a correction, and it runs against the thesis's own hedge.** PIL-6's
`threshold_reachability` note argues the falsifier "may be UNREACHABLE BY CONSTRUCTION at the demanding
names." At LUNR, on the FY2025 and H1/Q2 2025 bases, it is **reachable and reached** — on a substituted
denominator (consolidated period cost) rather than on the named one (programme cost). The named quantity
is still non-formable, because LUNR's consolidated cost base includes $83,002K of period operating
expenses and the OMES III, NSN and LTV service contracts that are not the lunar programme. So the honest
disposition is: **the falsifier is NOT satisfied; the substitute ratio is reported as a bound; and the
thesis's "unreachable by construction" language is too strong at this issuer and should be relaxed.**
The 8.29%-of-consolidated-revenue datum is also not the universe's maximum launch intensity — LUNR's
FY2025 launch amortisation is 14.19% of its revenue, higher than SPCX's own launch share.

## Sources.

This artifact reads the LUNR Q2 2026 Form 10-Q (accession 0001628280-26-056821) and FY2025 Form 10-K
(accession 0001628280-26-019865) page-by-page plus the Q2 2026 earnings call transcript. Pages are cited
inline as `[📄 LUNR 10-Q p.8](https://agentii.ai/v/LUNR/sec76/8)`. No figure is taken from an XBRL
`LABEL`, a metrics block, or a served fact value; every operating result is read from the filed statement
of operations on the page cited, for the DA-23 reason set out below. `get_segment_data` and
`data_freshness` are unusable in this workspace and were not used.

## §1. Component identity first — and the DA-23 finding it exposes

Rule 5 requires every `operating_income` read to show `gross_profit − opex` in-line and to name the opex
definition. LUNR requires a second step, because **LUNR is a DA-23 instance and the platform's served sign
is wrong at every period retrieved.**

The trap is that LUNR's cost base is reported INCLUSIVELY. `us-gaap:CostsAndExpenses` includes cost of
sales, so the "$253,304K" on the face of the statement is **cost of revenues plus operating expenses**,
not operating expenses. Both pairings close exactly:

**Q2 2026 (three months ended June 30, 2026), per [📄 LUNR 10-Q p.8](https://agentii.ai/v/LUNR/sec76/8):**

| Line | Value | Basis |
|---|---|---|
| Total revenues | $206,168K | filed |
| Cost of revenues | $170,302K | filed |
| Gross profit | $35,866K | **derived**: 206,168 − 170,302 |
| Gross margin | 17.40% | derived |
| Operating expenses (EXCLUSIVE of cost of revenues) | $83,002K | **derived**: 253,304 − 170,302 |
| Total costs and expenses (INCLUSIVE) | $253,304K | filed |
| **Loss from operations** | **$(47,136)K** | filed |
| Identity, exclusive definition | 35,866 − 83,002 = **(47,136)** | closes exactly |
| Identity, inclusive definition | 206,168 − 253,304 = **(47,136)** | closes exactly |

**The DA-23 result.** The platform serves `OperatingIncomeLoss` for this period as
**`+47,136,000`**. The filed figure is **$(47,136)K**. Same magnitude, opposite sign — `|x|` stripping,
not an inversion, per DA-23. Chosen reading: the filed value is used throughout. The detector that
establishes it is the component identity above, and it is the *only* reliable detector here: LUNR has
never filed a positive operating income in the periods examined, so any heuristic expecting a loss-maker's
served values to be negative would find nothing to flag. The same pattern reproduces at FY2025
(`+87,231,000` served; filed $(87,231)K; FY2025 identity 8,990 − 96,221 = (87,231) closes), at H1 2025
(`+38,717,000` served; filed $(38,717)K; identity 112,837 − 151,554 = (38,717) closes) and at Q2 2025
(`+28,640,000` served; filed $(28,640)K; identity −11,843 − 16,797 = (28,640) closes).

**Carry-forward — this resolves an open item in `thesis.md`.** `known-open` records: *"LUNR is a DA-23
candidate (a 42.1% operating margin at Q4 2025 is not credible for a lunar lander)."* It is not a margin
at all. The served Q4 2025 value is positive while the FY2025 filed loss is $(87,231)K and the FY2025
identity closes exactly on the negative; the "42.1% operating margin" is a **stripped loss of −42.1%**.
The open item can be closed on the DA-23 reading rather than left as a credulity judgement.

**FY2025 and FY2024 (per [📄 LUNR 10-K p.61](https://agentii.ai/v/LUNR/sec59/61)):**

| Line | FY2025 | FY2024 |
|---|---|---|
| Revenue | $210,059K | $228,000K |
| Cost of revenues | $201,069K | $225,231K |
| Gross profit (derived) | $8,990K (4.28%) | $2,769K (1.21%) |
| Opex, exclusive (derived) | $96,221K | $60,165K |
| Total costs and expenses | $297,290K | $285,396K |
| **Loss from operations** | **$(87,231)K** | **$(57,396)K** |
| Identity, exclusive | 8,990 − 96,221 = **(87,231)** ✓ | 2,769 − 60,165 = **(57,396)** ✓ |

FY2024's operating loss is **DERIVED** (revenue minus total costs and expenses) and is not used in any
ratio below.

## §2. growth-strategy-assessment — the programme-cost base, its basis, and the launch share

**The programme-cost base, stated.** LUNR is a one-segment issuer (DA-21 chosen reading, §1 above), so
the denominator question the brief asks admits three answers rather than one, and DA-30 requires all
three be given with a basis field:

| Denominator | FY2025 | Q2 2026 | Basis of the number |
|---|---|---|---|
| Total revenue | $210,059K | $206,168K | consolidated as-filed |
| Total cost of revenues | $201,069K | $170,302K | consolidated as-filed, segment = consolidated |
| Total costs and expenses (inclusive) | $297,290K | $253,304K | `CostsAndExpenses`, includes cost of revenues |
| Gross profit | $8,990K | $35,866K | derived, revenue − cost of revenues |

**The numerator, stated.** LUNR discloses launch as a cost of revenue item, in a single sentence, in both
formats:

> *"Amortization expense associated with deferred contract costs for **subcontracted launch services** was
> recorded in cost of revenue and was **$29.8 million and $10.1 million for the years ended December 31,
> 2025 and 2024**."* — [📄 LUNR 10-K p.80](https://agentii.ai/v/LUNR/sec59/80)

> *"$7.1 million and $14.3 million for the three and six months ended June 30, 2026 … compared to $7.6
> million and $15.6 million for the three and six months ended June 30, 2025 … Launch delay fees … were
> $0.8 million and $2.3 million for the three and six months ended June 30, 2025 and **no launch delay
> fees were incurred for the three and six months ended June 30, 2026**."* — [📄 LUNR 10-Q p.24](https://agentii.ai/v/LUNR/sec76/24)

The 2026 figure is therefore **strictly comparable** to the 2025 figure only if the delay fees are added
back on the 2025 side. Both variants are shown below, and the delay-fee-inclusive variant is the
like-for-like one.

**The launch share of programme cost, on every basis (DEMONSTRATED — arithmetic on filed cells):**

| Period | Launch numerator | ÷ Revenue | ÷ Cost of revenues | ÷ Total costs & expenses | ÷ Gross profit |
|---|---|---|---|---|---|
| FY2025 | $29.8M | 14.19% | **14.82%** | **10.02%** | **331%** |
| H1 2025 (6M, incl. $2.3M delay fees) | $17.9M | **15.87%** | **15.17%** | **11.81%** | n/m (GP negative) |
| Q2 2025 (3M, incl. $0.8M delay fees) | $8.4M | **16.70%** | **13.51%** | **10.64%** | n/m (GP negative) |
| H1 2026 (6M) | $14.3M | 3.64% | 4.37% | 2.98% | 21.7% |
| Q2 2026 (3M) | $7.1M | 3.44% | 4.17% | 2.80% | 19.8% |

*Every pre-acquisition basis exceeds the 0.10 threshold. Every post-Lanteris basis is below it.*

**Why the flip is a denominator event and not a curve event.** The numerator is close to flat while the
denominator more than triples:

- Q2 2025 → Q2 2026 launch amortisation: $8.4M → $7.1M = **−15.5%** (or $7.6M → $7.1M = **−6.6%**
  excluding the delay fees that were incurred in 2025 and not in 2026).
- Q2 2025 → Q2 2026 cost of revenues: $62,156K → $170,302K = **+174.0%**.
- Q2 2025 → Q2 2026 revenue: $50,313K → $206,168K = **+309.8%**, of which product revenue
  contributed **$166,735K against $0** — the Lanteris step-up, per
  [📄 LUNR 10-Q p.51](https://agentii.ai/v/LUNR/sec76/51), with the cost-of-revenue drivers
  (Lanteris acquisition, IM-3/IM-4 mission cost adjustments, NSN, OMES III, LTV) itemised at
  [📄 LUNR 10-Q p.53](https://agentii.ai/v/LUNR/sec76/53).

So this is not a company that grew its way out of launch cost. It is a company that **bought a
satellite-manufacturing business whose cost base contains no launch, and thereby diluted its own launch
intensity.** The consolidation choice, not the cost curve, produced a −12.2 percentage-point move in the
cost-of-revenues ratio in four quarters.

**DA-30 instance #1 — the numerator has TWO bases and they are 2.39x apart.** The Q2 2026 call reports a
**cash** outflow to the same supplier for the same programme:

> *"Operating cash included … **$17 million associated with the IM-4 milestone payment to SpaceX**."*
> — [📄 LUNR Q2 2026 call p.2](https://agentii.ai/v/LUNR/ect13/2)

Against the filed Q2 2026 **expense** of $7.1M ([📄 LUNR 10-Q p.24](https://agentii.ai/v/LUNR/sec76/24)),
that is a **2.39x** gap on one concept. The two are not substitutes: a milestone payment is capitalised
into deferred contract costs and amortised, so the cash basis front-loads and the expense basis smooths.
Substituting the $17M into the ratio gives 8.25% of revenue or 9.98% of cost of revenues for Q2 2026 —
i.e. **the choice of basis moves the answer by ~6 percentage points and very nearly re-crosses the 10%
bar.** Both bases are stated; neither is quoted alone.

## §3. organic-growth-drivers-analysis — and the single-mission bound

**Growth at LUNR is overwhelmingly inorganic on a one-year view, and the filed decomposition says so.**
Q2 2026 net revenue growth of +309.8% is dominated by the Lanteris product line at $166,735K from a
$0 base ([📄 LUNR 10-Q p.51](https://agentii.ai/v/LUNR/sec76/51)). On the service side the launch-
adjacent programmes are IM-3, IM-4, NSN, OMES III and LTV ([📄 LUNR 10-Q p.53](https://agentii.ai/v/LUNR/sec76/53)),
and the IM-3/IM-4 contracts are filed as **loss contracts** with the remaining performance obligation
position at $814.7M ([📄 LUNR 10-Q p.25](https://agentii.ai/v/LUNR/sec76/25)). Growth that requires an
accrued contract-loss provision is not a curve-capture: it is a programme that is costing more than it
sells for.

**The single-mission bound — above the bar, and CLAIMED-only.** The sharpest available reading of LUNR's
launch share is not consolidated at all, it is per programme. The Q2 2026 call reports a $17M IM-4
milestone payment to SpaceX ([📄 LUNR Q2 2026 call p.2](https://agentii.ai/v/LUNR/ect13/2)); against
IM-4's filed total estimated contract revenue of $123.7M ([📄 LUNR 10-Q p.25](https://agentii.ai/v/LUNR/sec76/25))
that is **13.74% — above the bar, on a programme denominator.** **This may bound and may not populate.**
The numerator is a call figure (DA-25 chosen reading): it is `CLAIMED`, and under rule 2 a `CLAIMED` or
`MODELED` input cannot satisfy the falsifier. It is reported here precisely because it is the directional
indicator that the consolidated 2.80%–4.17% understates LUNR's launch intensity on the programmes where
launch actually is the dominant input.

**DA-30 instance #2 and #3 on LUNR's own aggregates.** The call asserts *"backlog $1.8 billion"*
([📄 LUNR Q2 2026 call p.2](https://agentii.ai/v/LUNR/ect13/2)) against a filed **remaining performance
obligations of $814.7M** ([📄 LUNR 10-Q p.25](https://agentii.ai/v/LUNR/sec76/25)) — a **2.21x** gap on an
undefined concept, one basis signed and one unsigned. And the call's *"gross profit … $36 million … up
significantly from negative $12 million in the prior year"*
([📄 LUNR Q2 2026 call p.3](https://agentii.ai/v/LUNR/ect13/3)) is revenue minus cost of revenues only;
LUNR's quarterly depreciation and amortisation ([📄 LUNR 10-Q p.56](https://agentii.ai/v/LUNR/sec76/56))
is of the order of $14.9M, so a D&A-inclusive reading of the same words is roughly **1.7x smaller**.
Both quarters reconcile on the inclusive basis (−$11,843K for Q2 2025 reproduces the "negative $12
million"), which is why the call's arithmetic is internally consistent and still not the filed concept.

## §4. organic-growth-driver-execution-assessment — VRT's reusable test

**VRT's reusable test: check whether price improvements coexist with flat or falling margin.** At LUNR
the test is **UNEXERCISED on its price leg and answered on its margin leg.**

- **Price/expansion leg: UNEXERCISED.** LUNR files no pricing metric, no ARPU, no price-per-unit and no
  net-dollar-retention equivalent. There is therefore no price improvement to compare against margin, and
  it would be false to score the test CLEAN. What LUNR does file is a **gross margin** direction:
  17.40% at Q2 2026 against −23.54% at Q2 2025, and 4.28% at FY2025. That is an improvement.
- **Margin leg: answered, and the improvement is not evidence of pass-through.** The 2025 gross margins
  are negative or near-zero **because the launch charge is large relative to a small service revenue
  base** — at FY2025, the $29.8M launch charge is 331% of the $8,990K gross profit. In 2026 the margin
  improves to 17.40% while the launch charge falls to 19.8% of gross profit — but the improvement is
  **denominator-driven**: it is the Lanteris product line, not a launch-cost pass-through, that lifts
  revenue past the fixed programme cost. A margin recovery caused by acquiring a business with no launch
  content is not the curve reaching the customer.
- **Execution leg: answered negatively.** IM-3 and IM-4 are filed as **loss contracts**
  ([📄 LUNR 10-Q p.25](https://agentii.ai/v/LUNR/sec76/25)) and the cost-of-revenue variance attributes
  cost growth to IM-3/IM-4 mission adjustments ([📄 LUNR 10-Q p.53](https://agentii.ai/v/LUNR/sec76/53)).
  **Launch delay fees went from $2.3M (H1 2025) to nil (H1 2026)**
  ([📄 LUNR 10-Q p.24](https://agentii.ai/v/LUNR/sec76/24)) — a real schedule improvement, and the one
  place in this artifact where a launch-side input improvement is both filed and traceable. It did not,
  however, convert into a lower launch share: the amortisation charge fell only 6.6%.

**Disposition of VRT's test at LUNR: half-UNEXERCISED, half-negative.** No price metric exists to test;
the margin improvement that does exist is inorganic and launch-dilutive rather than launch-driven.

## §5. Where PIL-6's claim bites at LUNR

**PIL-6 claims the released value was captured at the launcher and not passed through, and that the
demand side does not price off the curve.** LUNR is the universe's cleanest test of the second half,
because LUNR is unambiguously a *demand-side* name — a lunar-services prime that buys launch — and it
discloses the launch charge as a period cost.

**The falsifier's first independently-falsifiable condition — "a demonstrated fall in revenue per launch
at least as large as the fall in cost per launch" — cannot be tested at LUNR and is recorded
`UNEXERCISED`.** LUNR files no launch count and no mass-to-orbit metric; the number of launches it
purchased in any period is not disclosed. A per-launch figure is therefore non-formable, and this is
PRESENCE-versus-ABSENCE discipline: **an unengaged check is not a passed check.**

**The falsifier's second condition — "a launch share of programme cost above 10% at the demand-side
names" — is FORMABLE at LUNR, and is BOTH above and below the bar depending on period and denominator.**
The full statement is:

| Basis | Verdict against the 0.10 threshold |
|---|---|
| FY2025, any denominator (revenue 14.19% / cost of revenues 14.82% / total costs 10.02%) | **ABOVE** |
| H1 2025 (6M), any denominator (15.87% / 15.17% / 11.81%) | **ABOVE** |
| Q2 2025 (3M), any denominator (16.70% / 13.51% / 10.64%) | **ABOVE** |
| H1 2026 (6M) and Q2 2026 (3M) on any denominator (2.80%–4.37%) | **BELOW** |
| Named quantity as written — launch ÷ **programme** cost | **NON-FORMABLE** (no programme-scoped denominator is filed) |

**The disposition, stated in the register's own terms.** The quantity is **NOT NON-FORMABLE and NOT a
PASS**. It is formable on a substituted denominator and, so formed, it **trips** on every 2025 basis. The
falsifier is nevertheless **NOT SATISFIED**, on two independent grounds: (a) the denominator is
consolidated period cost, not programme cost, so the ratio is a neighbour of the named quantity rather
than the quantity; and (b) the one basis that *is* programme-scoped — the single-mission IM-4 ratio of
13.74% — rests on a `CLAIMED` numerator and under rule 2 cannot populate a falsifier.

**What this does to the thesis.** PIL-6's `threshold_reachability` note asserts the threshold "may be
UNREACHABLE BY CONSTRUCTION at the demanding names." At LUNR that over-reads. The threshold is reachable
in the neighbourhood of the demand side, and it was reached as recently as FY2025. The 8.29%
SPCX-consolidated datum, offered in the note as evidence that the bar sits above the data, is **below**
LUNR's FY2025 launch share of revenue (14.19%) — so the note's premise that the largest launch owner sets
the universe ceiling is false on the filed numbers. The corrected statement is: **the named quantity is
non-formable at three of these four demand-side names and formable-but-denominator-dependent at the
fourth; the threshold is not unreachable, it is un-tested on the quantity as written.**

## §6. What could NOT be verified

| Item | Disposition | Class |
|---|---|---|
| Launch ÷ **programme** cost, the quantity PIL-6 names | **NON-FORMABLE** — no programme-scoped cost denominator is filed at LUNR; consolidated period cost is the nearest available | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Revenue per launch, and cost per launch (falsifier condition 1) | **UNEXERCISED** — no launch count and no mass-to-orbit metric is filed in any period | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Reconciliation of the $17M IM-4 cash payment to the $7.1M Q2 2026 amortisation charge | **UNRESOLVED** — the deferred-contract-cost roll-forward that would tie them is not presented | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Whether the $58.1M remaining non-cancelable obligation is launch-only | **NON-FORMABLE as filed** — the disclosure states it mixes launch services *and* component development, so it is not a launch-only numerator (DA-30) | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Served `OperatingIncomeLoss` sign at LUNR | **UNRESOLVED — platform defect**; detector is the component identity, which is why the identity is shown in §1 | UNRESOLVABLE-FROM-PLATFORM |
| IM-4 EAC adjustment, quarter basis | **THREE BASES** — $14.7M (call, quarter) vs $13.5M filed (quarter) vs $16.2M filed (half); no basis field in the call | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Q1 2025 launch amortisation | Not disclosed; the comparable series begins at Q2 2025 | UNRESOLVABLE-FROM-PUBLIC-SOURCES |

**Specific disclosure that would resolve the primary item:** a programme-level cost of revenue
split — or, more cheaply, the launch-services component within cost of revenues stated as a
percentage of total cost of revenues — on the same page as the existing $29.8M / $14.3M / $7.1M
amortisation sentence. LUNR already files the numerator and the disclosure is one basis field away from
being formable as written.

## §7. Corrections inherited and carried

- **`thesis.md` `known-open`, LUNR item — RESOLVED.** "a 42.1% operating margin at Q4 2025 is not credible
  for a lunar lander" is not a credulity question: it is a **stripped loss of −42.1%**, DA-23, with the
  FY2025 component identity closing exactly on the negative.
- **`thesis.md` `known-open`, SATS item — confirmed independently in this task.** SATS is DA-24
  contaminated; see the SATS artifact. The two issuers are also operationally linked: **Lanteris Space LLC
  builds the two satellites SATS is launching** and is a LUNR subsidiary as of January 2026.
- **DA-23 is 12-of-12 at RKLB and invisible to heuristics.** At LUNR it is at least 4-of-4 with the same
  invisibility property. The component identity remains the only detector, and it is shown inline here
  rather than asserted.
- **`+$1,824M` at SPCX is not evidence of migration.** LUNR's own −12.2pp cost-of-revenues ratio move in
  four quarters is the same defect class, one issuer removed: an acquisition, not a curve.

## §8. Carry-forwards

1. **The DA-23 served-sign defect is the single largest threat to any cross-issuer negative-value screen
   in this workspace.** Four of four LUNR periods tested are affected, the magnitudes are exact, and the
   issuer has never filed a positive operating income — so no sign heuristic can find it. Recommend the
   component identity be computed mechanically for every served `OperatingIncomeLoss`.
2. **LUNR is the counterexample to PIL-6's reachability hedge, not a confirmation of it.** The thesis
   should be amended from "unreachable by construction" to "non-formable on the named quantity at three
   of four demand-side names; formable-and-above-bar on a substituted denominator at LUNR's FY2025 and
   2025-period bases."
3. **The SPCX 8.29% figure is not the universe ceiling on launch intensity.** LUNR FY2025 is 14.19%.
   Any artifact that cites 8.29% as evidence the bar sits above the whole demand side is over-reading.
4. **The 2.39x cash-versus-expense gap on the LUNR launch numerator is the reason no single launch share
   should be quoted at this issuer without its basis.** A reader given only the $17M cash figure would
   compute 8.25% and could clear the bar; a reader given only the $7.1M expense figure could not.
5. **`deal_security_basis: standalone_pre_merger` is carried per the task's mandate.** The basis question
   it answers at LUNR is the Lanteris pre/post line: FY2025 and the 2025 periods are entirely
   pre-acquisition, Q2 2026 is the second full post-acquisition quarter, and no rate in this artifact
   crosses that line without saying so.

## Sources

| Figure | Citation |
|---|---|
| Q2 2026 and H1 2026 statements of operations — total revenues $206,168K and $392,898K; net loss attributable to the Company $46.4M and $83.8M | [📄 LUNR 10-Q p.8](https://agentii.ai/v/LUNR/sec76/8) |
| Amortisation for subcontracted launch services $7.1M / $14.3M (2026) vs $7.6M / $15.6M (2025); launch delay fees $0.8M / $2.3M in 2025 and nil in 2026 | [📄 LUNR 10-Q p.24](https://agentii.ai/v/LUNR/sec76/24) |
| IM-3 and IM-4 loss contracts; remaining performance obligations $814.7M | [📄 LUNR 10-Q p.25](https://agentii.ai/v/LUNR/sec76/25) |
| Note 21 — one reportable segment | [📄 LUNR 10-Q p.43](https://agentii.ai/v/LUNR/sec76/43) |
| Results of operations — product revenue $166.7M of total revenues $206.2M; operating loss $47.1M | [📄 LUNR 10-Q p.51](https://agentii.ai/v/LUNR/sec76/51) |
| Cost of revenue variance — Lanteris, IM-3/IM-4 adjustments, NSN, OMES III, LTV | [📄 LUNR 10-Q p.53](https://agentii.ai/v/LUNR/sec76/53) |
| Adjusted EBITDA reconciliation — depreciation and amortisation and share-based compensation | [📄 LUNR 10-Q p.56](https://agentii.ai/v/LUNR/sec76/56) |
| FY2025 amortisation for subcontracted launch services $29.8M and FY2024 $10.1M, in cost of revenue | [📄 LUNR 10-K p.80](https://agentii.ai/v/LUNR/sec59/80) |
| FY2025 and FY2024 statements of operations — revenues $210,059K and $228,000K; loss from operations $(87,231)K | [📄 LUNR 10-K p.61](https://agentii.ai/v/LUNR/sec59/61) |
| Purchase commitments — $58.1M remaining, stated as mixing launch services and component development | [📄 LUNR 10-K p.102](https://agentii.ai/v/LUNR/sec59/102) |
| $17M operating cash outflow, IM-4 milestone payment to SpaceX; backlog cited as $1.8 billion | [📄 LUNR Q2 2026 call p.2](https://agentii.ai/v/LUNR/ect13/2) |
| Gross profit described as $36 million against negative $12 million in the prior-year quarter | [📄 LUNR Q2 2026 call p.3](https://agentii.ai/v/LUNR/ect13/3) |

*Grades: every ratio in §2 is `DEMONSTRATED` — the numerator and denominator are both filed cells and the
arithmetic is direct. Every figure sourced to the Q2 2026 call (the $17M IM-4 payment, the $1.8 billion
backlog, the $36 million gross profit, the 13.74% single-mission ratio) is `CLAIMED` and is carried as a
bound only. FY2024's operating loss is `DERIVED`. The Q1 2025 launch amortisation does not exist in the
filed record. `skill_pin: ab94b90ee0ff` · `pillar: PIL-6`.*
