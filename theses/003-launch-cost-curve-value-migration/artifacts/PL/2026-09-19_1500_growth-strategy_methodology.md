---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-6
ticker: PL
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
      PL reports "gross margin" on at least TWO bases and they are 2-3 percentage points apart — GAAP
      (53.53% at Q1 FY2027) and non-GAAP (56% at Q1 FY2027, which adds back share-based compensation and
      amortisation of acquired intangibles). Chosen reading: where "gross margin", "gross profit",
      "operating income" or "EBITDA" appears in this artifact, the basis is named in-line, both bases are
      reported, and no movement is quoted on one basis alone. The two bases move in the SAME direction at
      PL (both down), which is the only reason a single-basis quotation here would not have inverted the
      finding — and that is luck, not discipline. A second DA-30 instance is the period basis: PL states
      capital expenditure as a percentage of revenue on an annual basis (FY2026 10-K) and on a
      three-month basis (Q1 FY2027 10-Q, segment note), and the two are not interchangeable.
  - da_id: DA-23
    chosen_reading: >
      PL is a DA-23 instance on the component identity. The platform serves `OperatingIncomeLoss` as a
      POSITIVE at every period retrieved — 34,888,000 (Q1 FY2027), 95,073,000 (FY ended 2026-01-31),
      116,122,000 (FY ended 2025-01-31), 22,771,000 (Q1 FY2026) — against filed negatives $(34,888)K,
      $(95,073)K, $(116,122)K and $(22,771)K. Chosen reading: every PL operating result is read from the
      filed statement of operations on the page cited. The detector is `gross_profit − opex =
      operating_income`, which closes exactly at all five periods shown in §1 on the EXCLUSIVE opex
      definition. The inclusive pairing is shown alongside because `us-gaap:CostsAndExpenses` includes
      cost of sales and a reader who takes the inclusive total for opex gets a false identity.
  - da_id: DA-29
    chosen_reading: >
      PL files a reconciliation from "backlog" to "remaining performance obligations". Chosen reading: a
      reconciliation that closes is not thereby a check. Every term in this artifact's ratios is required
      to appear in the cited source on the same basis it is used here; where a term in a PL reconciliation
      is not a filed line item, the reconciliation is treated as a back-solve and the figures sourced from
      it are marked DERIVED rather than DEMONSTRATED. This is the reason §3 refuses to construct a launch
      denominator out of PL's cost-of-revenue driver list: the drivers are narrative percentages, not a
      filed table, and no reconciliation ties them to the cost-of-revenue line.
  - da_id: DA-21
    chosen_reading: >
      PL reports in ONE reportable segment. Chosen reading: PL's revenue and cost-of-revenue figures are
      consolidated-by-construction, and no segment boundary can be crossed — which means the reason a
      launch share is not formable at PL is NOT a segment-boundary problem (DA-21 is satisfied) but a
      disclosure problem: launch is named inside cost of revenue and never quantified. Stating this
      matters, because the two failures have different remedies.
  - da_id: DA-27
    chosen_reading: >
      PL's fiscal year ends January 31, so its "Q1 FY2027" is the three months ended April 30, 2026 —
      three months ahead of a calendar-quarter reading. Chosen reading: every PL period is labelled with
      its actual end date in addition to its fiscal label, and no PL period is compared with a
      calendar-quarter-labelled figure from another issuer in this task without a date stamp.
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable  # corrected 2026-09-19: this is NOT a P11 deal security; `standalone_pre_merger` asserted a business contractually ceasing to exist
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "PL ect19 p.6"
    ticker: PL
    citation_id: ect19
    page_no: 6
    url: https://agentii.ai/v/PL/ect19/6
    located_via: read_source_pages
  - figure: "PL sec76 p.6"
    ticker: PL
    citation_id: sec76
    page_no: 6
    url: https://agentii.ai/v/PL/sec76/6
    located_via: read_source_pages
  - figure: "PL sec76 p.38"
    ticker: PL
    citation_id: sec76
    page_no: 38
    url: https://agentii.ai/v/PL/sec76/38
    located_via: read_source_pages
  - figure: "PL sec60 p.95"
    ticker: PL
    citation_id: sec60
    page_no: 95
    url: https://agentii.ai/v/PL/sec60/95
    located_via: read_source_pages
  - figure: "PL sec60 p.82"
    ticker: PL
    citation_id: sec60
    page_no: 82
    url: https://agentii.ai/v/PL/sec60/82
    located_via: read_source_pages
  - figure: "PL sec60 p.76"
    ticker: PL
    citation_id: sec60
    page_no: 76
    url: https://agentii.ai/v/PL/sec60/76
    located_via: read_source_pages
  - figure: "PL sec60 p.108"
    ticker: PL
    citation_id: sec60
    page_no: 108
    url: https://agentii.ai/v/PL/sec60/108
    located_via: read_source_pages
  - figure: "PL sec76 p.36"
    ticker: PL
    citation_id: sec76
    page_no: 36
    url: https://agentii.ai/v/PL/sec76/36
    located_via: read_source_pages
  - figure: "PL sec76 p.20"
    ticker: PL
    citation_id: sec76
    page_no: 20
    url: https://agentii.ai/v/PL/sec76/20
    located_via: read_source_pages
  - figure: "PL sec60 p.128"
    ticker: PL
    citation_id: sec60
    page_no: 128
    url: https://agentii.ai/v/PL/sec60/128
    located_via: read_source_pages
  - figure: "PL sec76 p.42"
    ticker: PL
    citation_id: sec76
    page_no: 42
    url: https://agentii.ai/v/PL/sec76/42
    located_via: read_source_pages
  - figure: "PL sec76 p.34"
    ticker: PL
    citation_id: sec76
    page_no: 34
    url: https://agentii.ai/v/PL/sec76/34
    located_via: read_source_pages
  - figure: "PL ect19 p.2"
    ticker: PL
    citation_id: ect19
    page_no: 2
    url: https://agentii.ai/v/PL/ect19/2
    located_via: read_source_pages
  - figure: "PL sec60 p.75"
    ticker: PL
    citation_id: sec60
    page_no: 75
    url: https://agentii.ai/v/PL/sec60/75
    located_via: read_source_pages
  - figure: "PL sec76 p.29"
    ticker: PL
    citation_id: sec76
    page_no: 29
    url: https://agentii.ai/v/PL/sec76/29
    located_via: read_source_pages
key_metrics:
  gross_margin_gaap_pct_q1_fy2027: 53.53
  gross_margin_non_gaap_pct_q1_fy2027: 56
  operating_loss_gaap_thousands_fy2026: -95073
  adjusted_ebitda_thousands_fy2026: 15495
---

# PL — Growth Strategy: A Launch Share That Cannot Be Drawn, at the Customer the Curve Is Supposed to Reach

## The finding

**PL is `NON-FORMABLE`.** Launch is *named* as a cost of revenue component in every PL filing, in identical
words, and is quantified **nowhere** on any period basis. The only launch figure in the entire PL
disclosure set is a single forward **stock** — $4.7 million of noncancelable launch purchase commitments
for the fiscal year ending January 31, 2028 — disclosed in one 10-Q and, notably, **absent from the
annual report's commitments note entirely**. There is no filed launch *flow* to divide by any denominator.

**This is the sharpest form of PIL-6's non-formability, because PL is precisely the customer the curve is
supposed to reach.** PL has the best gross margin in the task's universe at **53.5% GAAP** — and a
**−37.1% operating margin** on the same revenue. Its problem is not launch cost and it is not gross
margin. It is **fixed cost**: operating expenses of $85,289K against a gross profit of $50,401K in the
quarter, i.e. **1.69x cover needed and not available.** A pass-through of a cheaper launch would land in a
cost line that is 46% of revenue and be consumed by an opex line that is 91% of revenue. Nothing about
PL's economics turns on the launch price.

**And VRT's reusable test resolves NEGATIVE here, on fully filed numbers.** Price/expansion improvements
demonstrably exist — net dollar retention is **113% at Q1 FY2027 quarter-end, 114% including win-backs**,
over a base that was 106% a year earlier — and they coexist with a **FALLING** GAAP gross margin (55.24%
→ 53.53%, −1.70pp), a **FALLING** non-GAAP gross margin (59% → 56%, −3pp), operating expenses growing
**faster** than revenue (+43.65% vs +42.08%), and an operating loss **widening 53.21%**. A genuine
price-and-expansion improvement that coexists with a widening loss is exactly what VRT's test is for, and
it fails here.

**PL's own CEO supplies the most direct demand-side testimony in this task.** Asked about supply-chain and
launch stress, Will Marshall said launch is "a little bit more competitive than it used to be," that PL
has "launched 40 rockets … on 10 different launch vehicles," and that he is "excited about" the new
entrants and "increased competitiveness in the launch sector"
([📄 PL Q1 FY2027 call p.6](https://agentii.ai/v/PL/ect19/6)). The same call describes PL as "focused more
on growth than profitability," buying components to buy down supply-chain risk, and obtaining "better
pricing by buying more upfront." **That is a complete description of capture without pass-through: PL
takes the launch-cost decline as an input-cost benefit, reinvests it, and prices on growth.**

## Sources.

This artifact reads the PL Q1 FY2027 Form 10-Q (three months ended April 30, 2026; accession
0001193125-26-258304), the FY2026 Form 10-K (accession 0001193125-26-119957) and the Q1 FY2027 earnings
call transcript, page-by-page. Pages are cited inline as
`[📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)`. No figure is taken from an XBRL `LABEL`, a metrics
block, or a served fact value. `get_segment_data` and `data_freshness` are unusable in this workspace and
were not used.

## §1. Component identity first — DA-23, and the opex definition that decides it

Rule 5 requires `gross_profit − opex = operating_income` in-line with the opex definition named. PL is a
DA-23 issuer, so the served value must be discarded before the identity is even computed.

**Q1 FY2027 vs Q1 FY2026, per [📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6) and
[📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38) — three months ended April 30:**

| Line | Q1 FY2027 | Q1 FY2026 | Change |
|---|---|---|---|
| Revenue | $94,150K | $66,265K | +42.08% |
| Cost of revenue | $43,749K | $29,662K | +47.49% |
| **Gross profit** | $50,401K | $36,603K | +37.70% |
| **GAAP gross margin** | **53.53%** | **55.24%** | **−1.70pp** |
| **Non-GAAP gross margin** | **56%** | **59%** | **−3pp** |
| Research and development | $33,420K | — | — |
| Sales and marketing | $22,782K | — | — |
| General and administrative | $29,087K | — | — |
| **Opex, EXCLUSIVE of cost of revenue** | **$85,289K** | $59,374K | **+43.65%** |
| Total costs and expenses (INCLUSIVE) | $129,038K | $88,953K | +45.06% |
| **Loss from operations** | **$(34,888)K** | **$(22,771)K** | **widened 53.21%** |
| Opex as a percentage of revenue (exclusive) | **90.59%** | 89.60% | +0.99pp |
| Net loss | $(138,872)K | — | — |

Identities, both definitions:
- **Exclusive**: 50,401 − 85,289 = **(34,888)** ✓ exactly the filed loss from operations.
- **Inclusive**: 94,150 − 129,038 = **(34,888)** ✓ — this is the
  `gross_profit − CostsAndExpenses` pairing rule 5 warns about. It closes by coincidence here because the
  inclusive total *is* cost of revenue plus opex; the identity that carries information is the exclusive
  one.

**DA-23 result.** The platform serves `OperatingIncomeLoss` for Q1 FY2027 as **`+34,888,000`** against a
filed **$(34,888)K**. Same magnitude, opposite sign — `|x|` stripping. The same pattern reproduces at
FY ended 2026-01-31 (`+95,073,000` vs filed $(95,073)K), FY ended 2025-01-31 (`+116,122,000` vs filed
$(116,122)K) and Q1 FY2026 (`+22,771,000` vs filed $(22,771)K). Chosen reading: filed values only.

**Annual periods, per [📄 PL 10-K p.95](https://agentii.ai/v/PL/sec60/95):**

| Line | FY2026 | FY2025 | FY2024 |
|---|---|---|---|
| Revenue | $307,727K | $244,352K | $220,696K |
| Cost of revenue | $135,242K | $104,627K | $107,746K |
| Gross profit | $172,485K | $139,725K | $112,950K |
| GAAP gross margin | 56.05% | 57.18% | 51.18% |
| Opex, exclusive | $267,558K | $255,847K | $282,698K |
| **Loss from operations** | **$(95,073)K** | **$(116,122)K** | **$(169,748)K** |
| Identity, exclusive | 172,485 − 267,558 = **(95,073)** ✓ | 139,725 − 255,847 = **(116,122)** ✓ | 112,950 − 282,698 = **(169,748)** ✓ |
| Non-GAAP gross margin | 59% | 60% | — |
| Adjusted EBITDA | $15,495K | $(10,627)K | — |

**Two readings of the FY2026 result, both required.** On the GAAP operating line PL lost $(95,073)K. On
the Adjusted EBITDA basis it earned **$15,495K** — a swing of $110,568K on the same revenue
([📄 PL 10-K p.82](https://agentii.ai/v/PL/sec60/82)). The gap is depreciation, amortisation, share-based
compensation and warrant fair-value movement, and the Q1 FY2027 net loss of $(138,872)K sits almost
entirely below the operating line for the same reason
([📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)). **A growth-strategy reading that quotes "PL turned
EBITDA-positive" without the $(95,073)K GAAP operating loss is reading a different company.** Both are
given; neither alone.

## §2. growth-strategy-assessment — the programme-cost base, its basis, and the NON-FORMABLE verdict

**The programme-cost base, stated.** PL reports one reportable segment (DA-21 chosen reading), so the
denominator candidates are the consolidated lines. **The relevant denominator for a launch-cost share is
`cost of revenue`, because that is where PL itself says launch sits:**

> *"Cost of revenue for our satellite services arrangements includes employee-related costs of designing
> and manufacturing customer-owned satellites, mission systems engineering, satellite operations, software
> development, and maintenance, as well as satellite inventory materials, **third-party fees for launch
> procurement**, and ground station infrastructure."*
> — [📄 PL 10-K p.76](https://agentii.ai/v/PL/sec60/76), repeated verbatim at
> [📄 PL 10-K p.108](https://agentii.ai/v/PL/sec60/108) and [📄 PL 10-Q p.36](https://agentii.ai/v/PL/sec76/36)

PL names a launch-procurement cost component and **never quantifies it** — not as a dollar amount, not as
a percentage of cost of revenue, not as a driver. The Q1 FY2027 cost-of-revenue variance analysis itemises
its drivers by name and amount — solution partners and subcontractors, spacecraft hardware, ground
station, employee-related costs, hosting — and **launch procurement is not among them**
([📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38)).

**NON-FORMABLE.** There is no filed launch flow at PL on any period basis. The quantity PIL-6 names —
launch cost as a share of total programme cost — cannot be formed, and **this is the second of the
register's three dispositions: `NON-FORMABLE`, not PASS and not FAIL.** A band that cannot be drawn is not
a band within ±50%.

**The single launch figure, and why it must not be divided.** The only filed launch number at PL is a
forward commitment stock:

> *"Future purchase commitments under noncancelable launch service contracts as of April 30, 2026
> consisted of **$4.7 million** of total purchase commitments for the fiscal year ended January 31, 2028."*
> — [📄 PL 10-Q p.20](https://agentii.ai/v/PL/sec76/20)

Every ratio one could compute from it is inadmissible, and the range is wide enough to have changed the
answer:

| Denominator (period) | Ratio | Why inadmissible |
|---|---|---|
| Q1 FY2027 cost of revenue $43,749K (3M) | 10.74% | forward stock over a single quarter's flow — **spuriously above the 10% bar** |
| Q1 FY2027 total costs and expenses $129,038K (3M) | 3.64% | same defect |
| Q1 FY2027 opex $85,289K (3M) | 5.51% | same defect |
| FY2026 cost of revenue $135,242K (12M) | 3.48% | different period basis from the commitment's own FY2028 stamp |

The first row is the trap that matters: **dividing a stock by the wrong flow produces 10.74% and would
clear the falsifier by construction.** It is not reported as a reading. The $4.7M is a stock on an FY2028
period basis; DA-30 requires the basis be named, and naming it disqualifies the ratio.

**A second non-formability, and it is the interesting one: PL's ANNUAL report discloses no launch
commitment at all.** The FY2026 10-K's commitments note discloses non-cancelable purchase commitments in
one category — the Google hosting commitment at **$34,053K (FY2027) + $33,427K (FY2028) = $67,480K**
([📄 PL 10-K p.128](https://agentii.ai/v/PL/sec60/128)). **The launch commitment appears in a quarterly
report and not in the annual one.** So PL's launch disclosure is not merely unquantified, it is
*intermittent*: a reader of the annual report alone would not learn that launch procurement is a
committed purchase category at all. The resolving disclosure is a launch-services commitment line in the
annual commitments note on the same basis the 10-Q uses.

**DA-29 discipline, applied to the one PL reconciliation that touches this question.** PL files a
reconciliation from "backlog" to "remaining performance obligations"
([📄 PL 10-Q p.42](https://agentii.ai/v/PL/sec76/42)). The register's rule is that a reconciliation which
closes is not thereby a check, and that if a term appears nowhere in the source the check is a back-solve.
**This artifact therefore does not build a launch denominator out of the cost-of-revenue driver list on
p.38**, even though that list is the closest thing PL files to a cost decomposition: the drivers are
narrative line items at varying levels of aggregation with no table and no tie to the cost-of-revenue
total. Layering them into a "programme cost" would be a `MODELED` construction, and under rule 2 a
`MODELED` input cannot satisfy a falsifier.

## §3. organic-growth-drivers-analysis — and the period-basis collision

**PL's growth is organic and it is real.** Revenue grew 42.08% year-over-year in the quarter
($66,265K → $94,150K) and 25.94% across FY2026 ($244,352K → $307,727K)
([📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6), [📄 PL 10-K p.95](https://agentii.ai/v/PL/sec60/95)).
There is no acquisition in the PL record for these periods. This is the one issuer in this task where the
growth is unambiguously **organic**, and the driver is the defence-and-intelligence demand mix, not a
cost-curve position.

**The expansion metric is filed and it is improving on one basis and improving on both.** Net Dollar
Retention Rate is defined and tabulated at [📄 PL 10-Q p.34](https://agentii.ai/v/PL/sec76/34); the call
reports **113% at Q1 FY2027 quarter-end, 114% including win-backs**
([📄 PL Q1 FY2027 call p.2](https://agentii.ai/v/PL/ect19/2)). **Both bases are above 100%, and both are
improving** — the two-basis collision at PL does not invert the direction, which is worth stating
explicitly because at SPCX the same class of collision *does* invert (the customer share rises on Q2 and
falls on H1). Discipline, not luck, is what makes the two-basis comparison safe.

**DA-30 instance on the period basis.** PL states capital expenditure as a percentage of revenue on the
annual basis in the 10-K (**FY2026 26% vs FY2025 20%**,
[📄 PL 10-K p.75](https://agentii.ai/v/PL/sec60/75)) and discloses capital expenditures inside the
three-month segment note in the 10-Q ([📄 PL 10-Q p.29](https://agentii.ai/v/PL/sec76/29)). An annual
percentage of revenue and a quarterly capital-expenditure disclosure are not interchangeable bases, and
neither is a launch metric. It is recorded here because the FY2026 10-K's non-GAAP gross margin (59%) and
the Q1 FY2027 10-Q's non-GAAP gross margin (56%) are likewise different **period** bases on the same
**concept** — an annual figure and a quarter figure — and an artifact that reads 59% → 56% as a
one-period collapse has crossed a period basis without saying so.

## §4. organic-growth-driver-execution-assessment — VRT's reusable test, resolved NEGATIVE

**VRT's reusable test: check whether price improvements coexist with flat or falling margin.** At PL all
three legs are filed and the test runs.

| Leg | Reading | Direction |
|---|---|---|
| **Price / expansion** | NDR 113%, 114% including win-backs; expanding defence-and-intelligence mix | **IMPROVING** |
| **GAAP gross margin** | 55.24% → 53.53% (−1.70pp) | **FALLING** |
| **Non-GAAP gross margin** | 59% → 56% (−3pp) | **FALLING** |
| **Cost discipline** | Opex +43.65% vs revenue +42.08%; opex 90.59% of revenue | **WORSENING** |
| **Operating result** | Loss widened 53.21% ($(22,771)K → $(34,888)K) | **WORSENING** |

**Result: price and expansion improvements coexist with falling margins on BOTH bases and a widening
operating loss.** On VRT's own logic the improvement did not stick — it was competed, reinvested or
absorbed, and the operating line did not receive it. PL's gross margin fell **while** its expansion metric
rose by 7 percentage points. That is the failure VRT's test is designed to detect.

**The causal question, and PL's own answer.** Is the margin decline *attributable* to launch? PL does not
say so, and its own variance analysis attributes the cost-of-revenue increase to solution partners and
subcontractors, spacecraft hardware, ground station, employee-related costs and hosting — not launch
([📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38)). **This is why the PL finding is a consequence of
PIL-6 rather than a test of it: the pass-through cannot be observed at PL because the launch component is
not observable, and the margin decline is explained by other inputs entirely.** The honest disposition is
that **the launch-cost share is NON-FORMABLE and the margin behaviour is explicable without reference to
launch at all.** No inference about launch pass-through may be drawn from PL's margin path in either
direction.

**What PL does say about launch, in its own words.** The CEO's answer to the launch-cost question is the
most direct demand-side testimony in this task, and it describes **capture, not pass-through**:

> *"Yes, we're seeing launch being -- be a little bit more competitive than it used to be … we've launched
> 40 rockets, I think on 10 different launch vehicles … And I would also say, despite a little bit of
> extra competition for the space right now, there's a lot of new players coming onto the for right now.
> And so we're excited about them, we're excited about what they can offer as well and increased
> competitiveness in the launch sector."*
> — [📄 PL Q1 FY2027 call p.6](https://agentii.ai/v/PL/ect19/6)

Three things follow, and they are mutually consistent: **(1)** PL experiences the launch-cost decline as a
real input-cost improvement; **(2)** PL captures it — the same call describes buying components to buy
down supply-chain risk and obtaining "better pricing by buying more upfront," i.e. the benefit is taken
into PL's own cost structure; **(3)** PL does not pass it to customers, because it is "focused more on
growth than profitability" and its gross margin falls while its retention rate rises
([📄 PL Q1 FY2027 call p.6](https://agentii.ai/v/PL/ect19/6),
[📄 PL Q1 FY2027 call p.2](https://agentii.ai/v/PL/ect19/2)). **This is PIL-6's claim stated by the
customer itself, and it is `CLAIMED` — admissible to bound, never to populate.** It bounds the
interpretation of a NON-FORMABLE ratio; it does not convert that ratio into a measurement.

## §5. Where PIL-6's claim bites at PL

**The falsifier's first condition — "a demonstrated fall in revenue per launch at least as large as the
fall in cost per launch" — is `UNEXERCISED` at PL.** PL files no launch count, no per-launch revenue and
no mass-to-orbit metric. This is an unengaged check, not a passed one.

**The falsifier's second condition — "a launch share of programme cost above 10%" — is `NON-FORMABLE` at
PL.** Not above, not below: undrawable. The register's third disposition applies, and the reason it
applies is stated in PIL-6's own reachability note: *"recording it as a pass on a technicality is the
false clearance class 002 exists to prevent."* The 10.74% that one gets by dividing the $4.7M forward
stock by one quarter's cost of revenue is exactly that technicality, and it is refused here.

**PL's significance for PIL-6 is therefore as the counter-test, not as a data point.** PL is the
best-gross-margin customer in the universe. If the curve's released value were going to reach anyone, it
should reach a customer whose cost of revenue is 46% of revenue and whose opex is 91% of revenue — a
customer for whom a lower input price is close to pure operating leverage. **The test is unavailable, and
the available proxies point the other way:** margins falling on both bases, opex growing faster than
revenue, the operating loss widening 53% in a quarter of 42% revenue growth, and a CEO describing launch
competition as something to be "excited about" while explaining that the company is buying components and
buying ahead for better pricing. **A customer that can absorb a lower launch price without its margin
moving is a customer for whom launch is not the binding constraint.** That is consistent with PIL-6 and it
is not evidence *for* it, because the quantity was never drawn.

## §6. What could NOT be verified

| Item | Disposition | Class |
|---|---|---|
| Launch cost as a share of programme cost, any period basis | **NON-FORMABLE** — launch is named inside cost of revenue and never quantified; no launch flow is filed | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Launch-services purchase commitment in the ANNUAL report | **ABSENT** — the FY2026 10-K commitments note discloses only the Google hosting commitment; the launch commitment appears only in the Q1 FY2027 10-Q | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Revenue per launch and cost per launch | **UNEXERCISED** — no launch count and no mass metric is filed in any period | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Whether the margin decline is launch-attributable | **EXPLICABLE WITHOUT LAUNCH** — PL's filed cost-of-revenue drivers (partners/subcontractors, spacecraft hardware, ground station, employee costs, hosting) do not include launch | n/a — a disclosed explanation exists |
| Served `OperatingIncomeLoss` sign at PL | **UNRESOLVED — platform defect**; 4 of 4 paired periods serve a positive against a filed negative; detector is the component identity shown in §1 | UNRESOLVABLE-FROM-PLATFORM |
| Launch-dedicated segment or cost centre | **DOES NOT EXIST** — PL reports one reportable segment, so no DA-21 boundary exists to cross | n/a |

**Specific disclosure that would resolve the primary item:** the launch-procurement component of cost of
revenue stated as a dollar amount or a percentage on the annual basis — the same sentence PL already
writes at [📄 PL 10-K p.76](https://agentii.ai/v/PL/sec60/76), with a number attached. PL already names
the component; the disclosure is one basis field away from formability.

## §7. Corrections inherited and carried

- **The `+$1,824M` / acquisition-shaped-growth defect is general.** PL is the counterexample at this
  issuer — its growth is organic — but the PL artifact records the class because the LUNR artifact in this
  task exhibits it, and because the two were designed as a pair.
- **SPCX's customer-share two-basis collision inverts the direction; PL's NDR two-basis collision does
  not.** Both are DA-30 instances, and the pair is the argument for reporting every basis rather than for
  reporting the convenient one.
- **DA-23 is invisible to sign heuristics wherever an issuer has never filed a positive operating income.**
  PL has never filed a positive operating income in the periods examined, and 4 of 4 paired served values
  are stripped positives. Same property as RKLB (12 of 12) and LUNR (4 of 4).
- **A `CLAIMED` figure is admissible to bound, never to populate.** Applied here to the CEO's
  launch-competition testimony and to the call's non-GAAP gross margin percentages, and applied in the
  LUNR artifact to the $17M IM-4 milestone payment.

## §8. Carry-forwards

1. **`NON-FORMABLE` at PL is a result, not a gap.** The falsifier's demand-side leg cannot be drawn at the
   best-gross-margin customer in the universe, on a 42%-growth quarter, from the filings as written.
2. **The intermittent-launch-disclosure finding should be carried to the thesis.** The FY2026 10-K
   discloses no launch commitment; the Q1 FY2027 10-Q discloses one. An artifact reading only the annual
   report would conclude PL has no committed launch purchases at all. This is a disclosure-frequency
   defect, and it is the kind of thing a per-period census would catch and a single-period read would not.
3. **PL's margin path must not be used as evidence about launch in either direction.** The variance
   analysis gives a non-launch explanation for every cost-of-revenue driver, and the launch component is
   unquantified. Any artifact attributing PL's GAAP gross margin decline (55.24% → 53.53%) to the launch
   cost curve is over-reading.
4. **`deal_security_basis: standalone_pre_merger` is carried per the task's mandate**, with the note that
   PL is not a deal security in the P11 sense; the field is included because the task makes it mandatory
   for these four artifacts, and it is read as declaring that the figures are consolidated as-filed
   results of a single continuing entity with no pro-forma adjustment.
5. **The 10.74% spurious ratio is the reason the register's `NON-FORMABLE` disposition must be stated
   affirmatively.** Left unstated, the arithmetic is one division away, and that division clears the bar.

## Sources

| Figure | Citation |
|---|---|
| Q1 FY2027 statements of operations, three months ended April 30, 2026 — revenue $94,150K; net loss $(138,872)K | [📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6) |
| $4.7 million of noncancelable launch service purchase commitments, fiscal year ended January 31, 2028 | [📄 PL 10-Q p.20](https://agentii.ai/v/PL/sec76/20) |
| Segment note — single reportable segment; capital expenditures; long-lived assets by geography | [📄 PL 10-Q p.29](https://agentii.ai/v/PL/sec76/29) |
| Net Dollar Retention Rate and NDR including win-backs — definitions and period tables | [📄 PL 10-Q p.34](https://agentii.ai/v/PL/sec76/34) |
| Cost of revenue for satellite services arrangements includes third-party fees for launch procurement | [📄 PL 10-Q p.36](https://agentii.ai/v/PL/sec76/36) |
| Condensed consolidated results of operations, Q1 FY2027 vs Q1 FY2026 | [📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38) |
| Reconciliation of backlog to remaining performance obligations | [📄 PL 10-Q p.42](https://agentii.ai/v/PL/sec76/42) |
| MD&A components of results of operations — third-party fees for launch procurement | [📄 PL 10-K p.76](https://agentii.ai/v/PL/sec60/76) |
| Note — composition of cost of revenue, research and development, and sales and marketing | [📄 PL 10-K p.108](https://agentii.ai/v/PL/sec60/108) |
| FY2026 / FY2025 / FY2024 statements of operations — revenue $307,727K / $244,352K / $220,696K; loss from operations $(95,073)K / $(116,122)K / $(169,748)K | [📄 PL 10-K p.95](https://agentii.ai/v/PL/sec60/95) |
| Non-GAAP gross margin 59% vs 60%; Adjusted EBITDA $15,495K vs $(10,627)K | [📄 PL 10-K p.82](https://agentii.ai/v/PL/sec60/82) |
| Capital expenditures 26% of revenue vs 20% on the annual basis | [📄 PL 10-K p.75](https://agentii.ai/v/PL/sec60/75) |
| Commitments note — Google hosting only; no launch commitment disclosed | [📄 PL 10-K p.128](https://agentii.ai/v/PL/sec60/128) |
| Non-GAAP gross margin 56% vs 59%; net dollar retention 113% / 114% | [📄 PL Q1 FY2027 call p.2](https://agentii.ai/v/PL/ect19/2) |
| CEO on launch competition; 40 rockets on 10 launch vehicles | [📄 PL Q1 FY2027 call p.6](https://agentii.ai/v/PL/ect19/6) |

*Grades: the Q1 FY2027 and FY2026 ratios in §1 and §4 are `DEMONSTRATED` — filed cells with direct
arithmetic. The non-GAAP gross margins, the Adjusted EBITDA figures and the CEO's launch testimony are
`CLAIMED`. The FY2024 operating margin is `DERIVED` from the filed revenue and total costs and expenses.
`skill_pin: ab94b90ee0ff` · `pillar: PIL-6`.*
