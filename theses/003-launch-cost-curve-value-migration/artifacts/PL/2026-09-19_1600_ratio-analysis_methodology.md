---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-6
ticker: PL
skill: ratio-analysis
mode: methodology
generated_at: 2026-09-19T16:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "2d27c7f751fa"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: "Absolute-value stripping in the served layer. Every served PL OperatingIncomeLoss is positive; every filed counterpart is parenthesised negative. The filed page is the authority for the sign."
  - da_id: DA-24
    chosen_reading: "Non-operating contamination of an operating disclosure. At PL the contamination is DISCLOSED, not hidden — the segment table's 'other segment items' bucket is footnoted to include interest income, the warrant fair-value change, other income/expense and income taxes."
  - da_id: DA-25
    chosen_reading: "A normalised per-unit metric not reproducible from the audited tables. PL files no per-unit metric at all, so DA-25 is UNEXERCISED here rather than clean."
  - da_id: DA-28
    chosen_reading: "Capital-structure discontinuity around the IPO. PL's warrant liabilities are a pre-IPO instrument whose remeasurement is the largest single number in the adjusted-EBITDA bridge; the share count is not used as a detector."
  - da_id: DA-29
    chosen_reading: "A reconciliation that closes is not thereby a check. Four PL reconciliations close exactly AND name every term on a filed page, so DA-29 is satisfied rather than merely untriggered."
  - da_id: DA-30
    chosen_reading: "Two bases on one concept collapsed without a basis field. PL reports cost of revenue on two filed bases that differ by $41,104 thousand in FY2026."
evidence_grade: DEMONSTRATED
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "Q1 FY2027 (3M ended 2026-04-30) condensed consolidated statements of operations: revenue $94,150k, cost of revenue $43,749k, gross profit $50,401k, total opex $85,289k, loss from operations $(34,888)k, net loss $(138,872)k"
    ticker: PL
    citation_id: sec76
    page_no: 6
    form_type: 10-Q
    url: https://agentii.ai/v/PL/sec76/6
    located_via: read_source_pages
  - figure: "Q1 FY2027 results-of-operations ladder with filed % of revenue and % change: revenue +42%, cost of revenue +47%, gross profit +38%, total opex +44%, loss from operations $(34,888)k change $(12,117)k at 53%"
    ticker: PL
    citation_id: sec76
    page_no: 38
    form_type: 10-Q
    url: https://agentii.ai/v/PL/sec76/38
    located_via: read_source_pages
  - figure: "Note 8 commitments: launch service purchase commitments $4.7 million total to FY ending 2028; Google hosting commitments $25,118k (remainder FY2027) + $33,427k (2028) = $58,545k"
    ticker: PL
    citation_id: sec76
    page_no: 20
    form_type: 10-Q
    url: https://agentii.ai/v/PL/sec76/20
    located_via: read_source_pages
  - figure: "\"The Company contracts with certain third-party service providers to launch satellites. Service providers who provide these services are limited.\""
    ticker: PL
    citation_id: sec76
    page_no: 11
    form_type: 10-Q
    url: https://agentii.ai/v/PL/sec76/11
    located_via: read_source_pages
  - figure: "FY2026 vs FY2025 results of operations: revenue $307,727k / $244,352k, cost of revenue $135,242k / $104,627k, gross profit $172,485k / $139,725k, total opex $267,558k / $255,847k, loss from operations $(95,073)k / $(116,122)k"
    ticker: PL
    citation_id: sec60
    page_no: 78
    form_type: 10-K
    url: https://agentii.ai/v/PL/sec60/78
    located_via: read_source_pages
  - figure: "Non-GAAP gross profit bridge (closes exactly) and Adjusted EBITDA bridge: gross margin 56% / 57%, non-GAAP gross margin 59% / 60%, Adjusted EBITDA $15,495k / $(10,627)k"
    ticker: PL
    citation_id: sec60
    page_no: 82
    form_type: 10-K
    url: https://agentii.ai/v/PL/sec60/82
    located_via: read_source_pages
  - figure: "Single reportable segment table: segment cost of revenue $94,138k vs income-statement cost of revenue $135,242k; 'other segment items' $148,351k / $6,242k / $(29,239)k; capital expenditures $81.5M / $49.6M / $42.4M"
    ticker: PL
    citation_id: sec60
    page_no: 146
    form_type: 10-K
    url: https://agentii.ai/v/PL/sec60/146
    located_via: read_source_pages
  - figure: "Capital expenditures as a percentage of revenue: 26% (FY2026) vs 20% (FY2025)"
    ticker: PL
    citation_id: sec60
    page_no: 75
    form_type: 10-K
    url: https://agentii.ai/v/PL/sec60/75
    located_via: search_keyword_in_source
  - figure: "Backlog reconciliation to remaining performance obligations, and liquidity and capital resources"
    ticker: PL
    citation_id: sec76
    page_no: 42
    form_type: 10-Q
    url: https://agentii.ai/v/PL/sec76/42
    located_via: search_keyword_in_source
key_metrics:
  gross_margin_gaap_pct_q1_fy2027: 53.53
  operating_margin_pct_q1_fy2027: -37.06
  net_margin_pct_q1_fy2027: -147.50
  hosting_to_launch_commitment_multiple_x: 12.5
---

# PL — the margin ladder, the served-sign defect, and the demand-side programme-cost shares

**Finding.** Planet Labs files a **53.5% gross margin** — the highest in this thesis's universe — against an
operating margin of **−37.1%** and a net margin of **−147.5%**. The company is not a launch-cost story at all:
its filed demand-side programme-cost commitment to *reach orbit* is **$4.7 million**, while its commitment to
*process the data* is **$58,545 thousand** — a ratio of **12.5× against launch**. PL therefore contributes a
**negative** result to PIL-6, and it is a sharp one: at the payload-integrator end of the value chain, the
binding programme cost is not the rocket. Separately, PL is **DA-23's cleanest instance in the universe**,
because the gross-profit bound test is **silent** here (P5).

## 1. Acceptance test — adopted and run

Every identification below is accepted only if it is **(a) exact**, **(b) stable across periods**, and
**(c) consistent with a specified formula or a filed basis**. Anything else is recorded `UNRESOLVED` — never
"probably fine". This test is not decorative: the register records a ~**2,500**-candidate sweep over **36 filed
cells** that produced **6–9 coincidental hits per metric**, and only **2 of 16** served ratio fields were the
ratio they claimed. **Every ratio in this artifact is recomputed from filed cells; no served ratio is quoted.**
`list_xbrl_concepts(search="ratio")` returns **no margin concept in the served layer**, so at PL there is nothing
to quote even in principle.

Formula for every margin below: `ratio = filed numerator ÷ filed denominator`, both read off a single filed page.

## 2. The margin ladder

All figures in $ thousands. Both columns are read from one page.

| Line | Q1 FY2027 | Q1 FY2026 | Basis | Grade |
|---|---|---|---|---|
| Revenue | 94,150 | 66,265 | consolidated, as filed | DEMONSTRATED |
| Cost of revenue | 43,749 | 29,662 | consolidated, as filed | DEMONSTRATED |
| **Gross profit** | **50,401** | **36,603** | consolidated, as filed | DEMONSTRATED |
| R&D | 33,420 | 23,074 | consolidated, as filed | DEMONSTRATED |
| Sales & marketing | 22,782 | 16,314 | consolidated, as filed | DEMONSTRATED |
| General & administrative | 29,087 | 19,986 | consolidated, as filed | DEMONSTRATED |
| **Total operating expenses** | **85,289** | **59,374** | the three lines above, summed | DEMONSTRATED |
| **Loss from operations** | **(34,888)** | **(22,771)** | filed, parenthesised | DEMONSTRATED |
| Net loss | (138,872) | (12,628) | consolidated, as filed | DEMONSTRATED |

Source: [📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6)

**The opex definition used here is the EXCLUSIVE one** — R&D + S&M + G&A only, i.e. the three operating-expense
lines printed below gross profit. This matters: `us-gaap:CostsAndExpenses` **includes** cost of sales, so the
component identity is false wherever a cost-of-sales line exists. At PL a cost-of-revenue line does exist, so
the inclusive pairing is inadmissible.

**Component identity, run on four periods:**

```
Q1 FY2027:  50,401 − 85,289  = (34,888)   exact
Q1 FY2026:  36,603 − 59,374  = (22,771)   exact
FY2026:    172,485 − 267,558 = (95,073)   exact
FY2025:    139,725 − 255,847 = (116,122)  exact
```

Annual lines from [📄 PL 10-K p.78](https://agentii.ai/v/PL/sec60/78). All four close to the dollar. This is the
**only** reliable sign detector, and PL is the case that demonstrates why.

### 2.1 Derived ratios

| Ratio | Q1 FY2027 | Q1 FY2026 | Formula | Grade |
|---|---|---|---|---|
| Gross margin | **53.53%** | 55.24% | gross profit ÷ revenue | DEMONSTRATED |
| Operating margin | **−37.06%** | −34.36% | loss from operations ÷ revenue | DEMONSTRATED |
| Opex ratio | **90.59%** | 89.60% | total opex ÷ revenue | DEMONSTRATED |
| **Opex ÷ gross profit** | **1.692×** | 1.622× | total opex ÷ gross profit | DEMONSTRATED |
| Net margin | −147.50% | −19.06% | net loss ÷ revenue | DEMONSTRATED |
| Cost of revenue growth | **+47%** | — | filed % change column | DEMONSTRATED |
| Revenue growth | +42% | — | filed % change column | DEMONSTRATED |

The filed % change column is at [📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38). **Cost of revenue grew 47%
against revenue growth of 42%** — margin compression of **1.71 percentage points**, filed as such. The ladder's
shape is: a genuinely high gross margin, entirely consumed by a fixed cost base running at **1.69× gross
profit**. On the FY2026/FY2025 pair the same structure holds: gross margin **56.05% → 57.18%**, i.e.
**172,485 ÷ 307,727 = 56.05%** (filed **56%**) and **139,725 ÷ 244,352 = 57.18%** (filed **57%**), both at
[📄 PL 10-K p.82](https://agentii.ai/v/PL/sec60/82). **PL's gross margin is one of the ratios that IS the ratio
it claims** — it reproduces from filed cells to the rounded percent. That is a positive result and it is stated
as one.

## 3. P5 — DA-23 at PL is the cleanest instance in the universe, because the bound test is silent

**Every served `OperatingIncomeLoss` value in the PL fact set is POSITIVE.** The served window spans **18
distinct fiscal periods from FY2024 Q1 (2024-02-01→2024-04-30) to FY2027 Q1 (2026-02-01→2026-04-30)**, and no
negative value appears anywhere in it. Values include `+34,888,000`, `+95,073,000`, `+116,122,000`,
`+22,771,000`, `+169,748,000`, `+135,830,000`. Grade: DEMONSTRATED, from the served layer — which is exactly
where DA-23 lives.

**The filed pages print every one of those with parentheses.** The four periods reconciled above are filed as
`(34,888)`, `(22,771)`, `(95,073)`, `(116,122)` — at [📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6) and
[📄 PL 10-K p.78](https://agentii.ai/v/PL/sec60/78). Same magnitude, opposite sign. That is DA-23's definition:
**absolute-value stripping, not inversion.**

**Why PL is the cleanest instance.** The naive bound test is: *a positive operating income cannot exceed gross
profit.* At PL the served value **+34,888 is BELOW filed gross profit 50,401**, so the bound **does not fire**.
The strip is invisible to it. At YSS — the sibling artifact — the bound *does* fire, because that served value
exceeds its gross profit. So the detector that works at one issuer is silent at another, on the same defect,
in the same register. **The component identity is the only detector that runs at PL**, and §2 shows it closing
exactly on all four periods. `EPS × shares` is **not** an admissible sign test and was not used.

## 4. P6 — DA-24 and DA-30 in the segment table

PL files **one operating and reportable segment** whose table runs all the way to consolidated net loss
([📄 PL 10-K p.146](https://agentii.ai/v/PL/sec60/146)). Two register classes fire there.

**DA-24 — non-operating contamination, disclosed rather than hidden.** The table's `Other segment items` line is
footnoted: *"Includes interest income, change in fair value of warrant liabilities, other income (expense), net
and provision for income taxes."* The identification satisfies all three legs of the acceptance test:

```
−interest income          −14,329
+warrant FV change        +161,400
+other income (expense)    −3,375
+income tax provision      +4,655
                          ─────────
                           148,351   = filed "other segment items"   exact
```

**Exact**, consistent with the footnoted formula, and reproducible in FY2025 (**6,242**) and FY2024 by the same
construction. Note FY2024's value is **$(29,239)$ — negative**, a *negative expense* bucket. A sign-strip in
that cell would be undetectable from the value alone; the segment table's own reconciliation to
`Consolidated net loss` is the check that constrains it.

**The magnitude is the finding.** The warrant fair-value change is **$161,400 thousand — 10.4× the entire
Adjusted EBITDA the reconciliation produces.** This is a pre-IPO instrument (DA-28 shape): the share count is
not used as a detector anywhere in this artifact, and the same discipline applies to the warrant liability.

**DA-30 — two filed bases on one concept.** Cost of revenue is filed at **$135,242k** on the income statement
and at **$94,138k** in the segment table. The table's footnote (1) explains the segment figure is *"exclusive of
… depreciation and amortization, stock-based compensation, restructuring costs …"*. Difference: **$41,104k**.
Both numbers are correct; **neither is comparable to the other**, and neither carries a basis label in the
served layer. **Every cost-of-revenue figure in this artifact therefore names its basis.** The same split
applies to R&D (106,749 vs 80,251), S&M (72,676 vs 63,591) and G&A (88,133 vs 54,252).

## 5. DA-29 — four reconciliations that close, with every term located

DA-29 warns that *a reconciliation that closes is not thereby a check*. The test is whether its terms appear
**in the source**. At PL four reconciliations close exactly **and** name every term on a filed page:

| Reconciliation | Closes to | All terms filed? | Page |
|---|---|---|---|
| Component identity (4 periods) | the dollar | Yes | p.6, p.78 |
| Non-GAAP gross profit bridge | 182,617 / 147,517 | Yes — 6,881 + 2,933 + 15 + 303 = 10,132 | p.82 |
| Adjusted EBITDA bridge | 15,495 / (10,627) | Yes — 11 terms, all on the page | p.82 |
| Segment table → consolidated net loss | (246,860) | Yes — 11 lines sum exactly | p.146 |

**DA-29 is SATISFIED at PL, four times over** — not merely untriggered. This is the positive inverse of the
register's own warning and it is stated because an unengaged check is not a passed check.

**Adjusted EBITDA is positive: $15,495 thousand in FY2026.** The bridge closes, so the number is arithmetically
sound — but its single largest input is the **$161,400k warrant remeasurement**, a non-operating, non-cash item
that is 10.4× the metric it produces. PL's one positive "profitability" figure is a capital-structure artefact.

## 6. PIL-6 — the demand side does not price off the cost curve

PL **buys** launches; it does not sell them. It therefore contributes **no point to the cost curve** — and that
is a result, not a gap.

Its Note 8 programme commitments ([📄 PL 10-Q p.20](https://agentii.ai/v/PL/sec76/20)) put the two sides of its
demand-side cost in one place:

| Commitment | Amount | Window | Grade |
|---|---|---|---|
| Launch services (third-party) | **$4.7 million** | FY ending 2028 | DEMONSTRATED |
| Google hosting | **$58,545 thousand** | remainder FY2027 + FY2028 | DEMONSTRATED |
| **Hosting ÷ launch** | **12.5×** | — | DEMONSTRATED |

`58,545 ÷ 4,700 = 12.457 → 12.5×`. Exact, formula-consistent, and stable — the hosting line is a two-period
schedule, so the ratio is reproducible from the table rather than from a single cell.

The complementary filed statement is at [📄 PL 10-Q p.11](https://agentii.ai/v/PL/sec76/11): *"The Company
contracts with certain third-party service providers to launch satellites. **Service providers who provide these
services are limited.**"* PL is a price-taker on launch with a thin supplier set — and still spends **12.5×**
more on hosting than on reaching orbit. **At the payload-integrator end of the chain, the rocket is not the
binding programme cost.** For PIL-6's claim that *the demand side does not price off the curve*, this is
confirming evidence from the demand side itself.

**Capex corroborates the direction of spend:** $81.5M / $49.6M / $42.4M for FY2026 / FY2025 / FY2024
([📄 PL 10-K p.146](https://agentii.ai/v/PL/sec60/146)) — **+64.3%** in the latest year — filed as *"Capital
Expenditures as a Percentage of Revenue: 26% vs 20%"* at [📄 PL 10-K p.75](https://agentii.ai/v/PL/sec60/75).
Recomputed: **81.5 ÷ 307.727 = 26.49% → 26%** and **49.6 ÷ 244.352 = 20.30% → 20%**. Both reproduce. Capital is
going into satellites and ground segment, not into launch.

## 7. What this artifact could NOT resolve

| Unresolved | Why | Class | Disclosure that would resolve it |
|---|---|---|---|
| PL's position on the cost curve | PL files **no** per-launch price, per-launch cost, launch count, or mass-to-orbit — in any period | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | A per-launch cost or a kg-to-orbit metric in a filed table, on a DA-01-named basis |
| DA-25 at PL | No normalised per-unit metric is filed at all | `UNEXERCISED` — **not** `CLEAN` | Any filed per-unit metric | 
| The FY2024 negative "other segment items" sign | A negative expense bucket is a DA-23-shaped hazard that the served layer cannot rule out from the value alone | `UNRESOLVED` | A quarter-level segment table where the sign is constrained by a second line |

**DA-25 is `UNEXERCISED`, not `CLEAN`.** PL files no normalised per-unit metric, so the check could not run. An
unengaged check is not a passed check, and recording it as clean would be the exact failure mode DA-29 warns
about.

**`UNRESOLVABLE-FROM-PUBLIC-SOURCES`, not `FROM-PLATFORM`.** The missing quantity is absent from the filings
themselves, not from the extraction. Re-querying the platform will not produce it.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Q1 FY2027 (3M ended 2026-04-30) condensed consolidated statements of operations: revenue $94,150k, cost of revenue $43,749k, gross profit $50,401k, to | [📄 PL 10-Q p.6](https://agentii.ai/v/PL/sec76/6) |
| Q1 FY2027 results-of-operations ladder with filed % of revenue and % change: revenue +42%, cost of revenue +47%, gross profit +38%, total opex +44%, l | [📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38) |
| Note 8 commitments: launch service purchase commitments $4.7 million total to FY ending 2028; Google hosting commitments $25,118k (remainder FY2027) + | [📄 PL 10-Q p.20](https://agentii.ai/v/PL/sec76/20) |
| "The Company contracts with certain third-party service providers to launch satellites. Service providers who provide these services are limited." | [📄 PL 10-Q p.11](https://agentii.ai/v/PL/sec76/11) |
| FY2026 vs FY2025 results of operations: revenue $307,727k / $244,352k, cost of revenue $135,242k / $104,627k, gross profit $172,485k / $139,725k, tota | [📄 PL 10-K p.78](https://agentii.ai/v/PL/sec60/78) |
| Non-GAAP gross profit bridge (closes exactly) and Adjusted EBITDA bridge: gross margin 56% / 57%, non-GAAP gross margin 59% / 60%, Adjusted EBITDA $15 | [📄 PL 10-K p.82](https://agentii.ai/v/PL/sec60/82) |
| Single reportable segment table: segment cost of revenue $94,138k vs income-statement cost of revenue $135,242k; 'other segment items' $148,351k / $6, | [📄 PL 10-K p.146](https://agentii.ai/v/PL/sec60/146) |
| Capital expenditures as a percentage of revenue: 26% (FY2026) vs 20% (FY2025) | [📄 PL 10-K p.75](https://agentii.ai/v/PL/sec60/75) |
| Backlog reconciliation to remaining performance obligations, and liquidity and capital resources | [📄 PL 10-Q p.42](https://agentii.ai/v/PL/sec76/42) **(newly surfaced)** |
