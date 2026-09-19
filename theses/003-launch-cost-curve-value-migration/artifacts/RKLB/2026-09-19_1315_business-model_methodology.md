---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-2
ticker: RKLB
skill: business-model
mode: methodology
generated_at: 2026-09-19T13:15:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "9479220eef91"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
deal_security_basis: standalone_pre_merger
definitions_used:
  - da_id: DA-21
    chosen_reading: >
      Issuer-defined, management-drawn segment boundaries — taken from RKLB's Note 18 two-segment
      structure (launch services, space systems). For mixed contracts the boundary between the two
      is drawn by COST ALLOCATION: revenue is "generally allocated based upon the overall costs
      incurred for each of the reporting segments in comparison to total overall costs of the
      contract." The boundary is therefore a cost-allocation line, not a transaction-price line,
      and a change in the allocation key moves revenue between segments. LIMIT RECORDED: the
      boundary extends to revenue and gross profit ONLY — management does not review segment
      operating expenses, so no segment operating income exists on any filed basis.
  - da_id: DA-25
    chosen_reading: >
      Normalised per-unit metrics not reproducible from audited tables — and at RKLB the
      irreproducibility is DOCUMENTED BY THE FILING rather than inferred. "Revenue per launch"
      is defined on a launch-OCCURRENCE basis ("during the period in which the launch occurs,
      regardless of whether the revenue is recognized using the point-in-time or over-time
      method"), whereas the segment table is on a RECOGNITION basis. The two bases are different
      by construction, so the metric reconciles to no audited table and cannot be made to. All
      four periods are reported below on both bases.
  - da_id: DA-23
    chosen_reading: >
      Platform sign-strip, confirmed as a NEW instance at RKLB on four of four periods:
      XBRL-served `OperatingIncomeLoss` returns positive magnitudes against filed negatives.
      Detected only by the component identity; `EPS × shares` not used as a sign test.
  - da_id: DA-26
    chosen_reading: >
      Annual figures mislabelled as quarterly. Checked and NOT triggered in this artifact's
      periods: the four columns used are unambiguously "Three Months Ended June 30" and "Six
      Months Ended June 30", read from the face of the statements of operations rather than
      from an extracted metrics block. The check is ENGAGED (period labels were verified at
      source), not unexercised.
  - da_id: DA-27
    chosen_reading: >
      Fiscal-period labels derived from the calendar quarter rather than the issuer's fiscal
      calendar. Verified NOT APPLICABLE at RKLB: the issuer is a December fiscal-year-end filer
      (`fiscal_year_end_month: 12`, source `gold_companies`), so the calendar-quarter mapping is
      exact and produces no offset. ENGAGED and resolved as a clean negative.
  - da_id: DA-30
    chosen_reading: >
      Two bases on one concept collapsed without a basis field. "Launch revenue" has THREE
      competing bases at RKLB — segment-table total, point-in-time only, and per-launch-implied —
      and "launch gross margin" has TWO. Every basis is reported below and none is quoted alone.
evidence_grade: DEMONSTRATED
citations:
  - figure: "RKLB sec109 p.40"
    ticker: RKLB
    citation_id: sec109
    page_no: 40
    url: https://agentii.ai/v/RKLB/sec109/40
    located_via: read_source_pages
  - figure: "RKLB sec109 p.32"
    ticker: RKLB
    citation_id: sec109
    page_no: 32
    url: https://agentii.ai/v/RKLB/sec109/32
    located_via: read_source_pages
  - figure: "RKLB sec109 p.33"
    ticker: RKLB
    citation_id: sec109
    page_no: 33
    url: https://agentii.ai/v/RKLB/sec109/33
    located_via: read_source_pages
  - figure: "RKLB sec109 p.11"
    ticker: RKLB
    citation_id: sec109
    page_no: 11
    url: https://agentii.ai/v/RKLB/sec109/11
    located_via: read_source_pages
  - figure: "RKLB sec109 p.37"
    ticker: RKLB
    citation_id: sec109
    page_no: 37
    url: https://agentii.ai/v/RKLB/sec109/37
    located_via: read_source_pages
  - figure: "RKLB sec109 p.38"
    ticker: RKLB
    citation_id: sec109
    page_no: 38
    url: https://agentii.ai/v/RKLB/sec109/38
    located_via: read_source_pages
  - figure: "RKLB sec109 p.6"
    ticker: RKLB
    citation_id: sec109
    page_no: 6
    url: https://agentii.ai/v/RKLB/sec109/6
    located_via: read_source_pages
  - figure: "RKLB sec109 p.18"
    ticker: RKLB
    citation_id: sec109
    page_no: 18
    url: https://agentii.ai/v/RKLB/sec109/18
    located_via: read_source_pages
  - figure: "RKLB sec109 p.15"
    ticker: RKLB
    citation_id: sec109
    page_no: 15
    url: https://agentii.ai/v/RKLB/sec109/15
    located_via: read_source_pages
  - figure: "RKLB sec109 p.13"
    ticker: RKLB
    citation_id: sec109
    page_no: 13
    url: https://agentii.ai/v/RKLB/sec109/13
    located_via: read_source_pages
  - figure: "RKLB sec109 p.35"
    ticker: RKLB
    citation_id: sec109
    page_no: 35
    url: https://agentii.ai/v/RKLB/sec109/35
    located_via: read_source_pages
key_metrics:
  total_revenue_usdk_q2_2026: 234066
  launch_services_revenue_usdk_q2_2026: 44586
  space_systems_revenue_usdk_q2_2026: 189480
  pro_forma_total_revenue_usdk_q2_2026: 237842
---

# RKLB — Segment Boundaries and the DA-21 Restatement

## Finding

**At the company named Rocket Lab, the launch segment is the one segment that is not
growing — and it is also the one segment whose gross margin is rising fastest.** Both halves
are filed, and neither is visible without first fixing the segment boundary.

Filed, Q2 2026 vs Q2 2025 [📄 RKLB 10-Q p.40](https://agentii.ai/v/RKLB/sec109/40),
[p.32](https://agentii.ai/v/RKLB/sec109/32) `[FACT]` · `DEMONSTRATED`: total revenue rose
**+62%** (`$234.1M` vs `$144.5M`, `+$89.6M`), *"partially offset by a decrease in launch
revenue of $2.1 million."* Launch Services revenue **fell 4%** (`$44.6M` vs `$46.6M`) while
Space Systems revenue **rose 94%** (`$189.5M` vs `$97.9M`). Launch Services contributed
**−2.3%** of the quarter's total growth; Space Systems contributed **+102.3%**.

Yet Launch Services' **gross margin rose from 30.48% to 42.86%** and its **gross profit rose
34.4%** on revenue that fell 4.4% — the best margin in the company, above Space Systems'
34.55% [📄 RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32) `[FACT]` · `DEMONSTRATED`.
**The launch business is improving and shrinking at the same time.** That is the A1a/A1b
evidence in its sharpest form, and it is a fact about the *segment*, not about launch as an
activity.

**Three boundary facts must be fixed before any comparison, and they are stated in §1–§5.**
The segment line is drawn by cost allocation; it extends to gross profit and stops there
because the issuer says so; and the entity perimeter moved under it in the opposite direction
from SPCX's.

---

## 1. The segment boundary statement, verbatim

RKLB reports **two** operating and reportable segments. The boundary is filed as
[📄 RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32) `[FACT]` · `DEMONSTRATED`:

| Boundary element | Filed language | Source |
|---|---|---|
| Segment set | *"The Company manages its business primarily based upon two operating segments, launch services and space systems. Each of these operating segments represents a reportable segment."* | [p.32](https://agentii.ai/v/RKLB/sec109/32) |
| Launch Services scope | *"Launch Services provides launch and launch related services to customers on a dedicated mission or ride share basis."* | [p.32](https://agentii.ai/v/RKLB/sec109/32) |
| Space Systems scope | *"Space systems is predominately comprised of spacecraft components and spacecraft manufacturing."* | [p.32](https://agentii.ai/v/RKLB/sec109/32) |
| Why the line is drawn | *"each reporting segment is managed separately to better align with customer's needs and the Company's growth plans"* | [p.32](https://agentii.ai/v/RKLB/sec109/32) |
| **Mixed-contract allocation** | *"For contracts with customers that contain both space systems and launch services elements, revenues for each reporting segment are generally allocated based upon the overall costs incurred for each of the reporting segments in comparison to total overall costs of the contract."* | [p.32](https://agentii.ai/v/RKLB/sec109/32) |
| **The hard limit** | *"Management does not regularly review either reporting segment's total assets or operating expenses. This is because in general, the Company's long-lived assets, facilities, and equipment are shared by each reporting segment."* | [p.33](https://agentii.ai/v/RKLB/sec109/33) |

**Correct segment boundary statement for RKLB.** *Two segments — Launch Services and Space
Systems — drawn by management. Where a contract contains both elements, the boundary between
them is a **cost-allocation line**: revenue is split by each segment's share of total contract
cost, not by any observed transaction price. And the boundary extends to **revenue and gross
profit only** — it stops there by the issuer's own filed statement, because operating expenses,
long-lived assets, facilities and equipment are shared across both segments.*

**Two consequences that are load-bearing for P2.**

1. **No segment operating income exists at RKLB on any basis** — not on a filed basis, and not
   on a constructible one. This is not a platform defect; it is a permanent property of the
   disclosure, filed in the present tense. **Basis C is unconstructible.** A later artifact that
   compares "Launch Services operating margin" against "Space Systems operating margin" — or
   against SPCX's Space segment operating margin, which *does* exist — is comparing a
   constructed number against a filed one and will be wrong by whatever allocation it invented.
2. **Because the intra-entity line is a cost-allocation key, a change in that key moves revenue
   between segments with no change in the underlying business.** A shift in the relative cost
   of a combined launch-plus-spacecraft contract reallocates revenue between the two segments.
   The filing discloses the *method* but not the *key*, and does not quantify the allocation. So
   the Launch-vs-Space-Systems split is a management-drawn line inside a fixed legal perimeter
   — DA-21's exact case — with an additional property SPCX's boundaries lack: it is **sensitive
   to a cost input we cannot observe**. `[DEDUCTED]`

---

## 2. Segment tables — revenue and gross margin, 3M and 6M

All figures USD thousands, as filed. `[FACT]` · `DEMONSTRATED`.

### Revenue, cost of revenues, gross profit

| Segment | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---:|---:|---:|---:|
| **Launch Services** — revenue | 44,586 | 46,646 | 108,249 | 82,238 |
| cost of revenues | 25,476 | 32,426 | 60,916 | 60,801 |
| **gross profit** | **19,110** | **14,220** | **47,333** | **21,437** |
| **Space Systems** — revenue | 189,480 | 97,852 | 326,165 | 184,829 |
| cost of revenues | 124,014 | 65,684 | 212,429 | 124,631 |
| **gross profit** | **65,466** | **32,168** | **113,736** | **60,198** |
| **Total** — revenue | 234,066 | 144,498 | 434,414 | 267,067 |
| cost of revenues | 149,490 | 98,110 | 273,345 | 185,432 |
| **gross profit** | **84,576** | **46,388** | **161,069** | **81,635** |

Source: [📄 RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32). Segment revenue and cost of
revenues sum **exactly** to the consolidated figures in all four periods (`44,586 + 189,480 =
234,066`; `25,476 + 124,014 = 149,490`; `19,110 + 65,466 = 84,576`; and the three prior
periods likewise). This is a check that **ran and closed** on filed terms — not a back-solve
(DA-29), and not an `UNEXERCISED` test.

### Gross margin and revenue growth by segment

| Measure | LS Q2 2026 | LS Q2 2025 | SS Q2 2026 | SS Q2 2025 | LS H1 2026 | LS H1 2025 | SS H1 2026 | SS H1 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Gross margin | **42.86%** | 30.48% | 34.55% | 32.87% | **43.73%** | 26.07% | 34.87% | 32.57% |
| Revenue YoY | **−4.4%** | — | +93.6% | — | +31.6% | — | +76.5% | — |
| Gross profit YoY | **+34.4%** | — | +103.5% | — | +120.8% | — | +88.9% | — |
| Revenue share | 19.05% | 32.28% | 80.95% | 67.72% | 24.92% | 30.79% | 75.08% | 69.21% |
| Share of total growth | **−2.3%** | — | **+102.3%** | — | +15.5% | — | +84.5% | — |

Gross margins and shares are our arithmetic on the filed cells above — `MODELED` as ratios,
`DEMONSTRATED` as inputs. The issuer states the growth rates itself: Space Systems *"+$91.6
million, or 94%"* and Launch Services *"a decrease of $2.1 million, or 4%"*
[📄 RKLB 10-Q p.40](https://agentii.ai/v/RKLB/sec109/40) — our arithmetic agrees (`−4.42%`).

**The margin asymmetry is the finding.** Launch Services' gross margin improved **12.38 pp**
year-on-year (30.48% → 42.86%) while Space Systems' improved **1.68 pp** (32.87% → 34.55%).
Across H1 the gap is wider still: **+17.66 pp** vs **+2.30 pp**. Cost of revenues for Launch
Services *fell* 21% (`$32.4M` → `$25.5M`, −$7.0M) even as Space Systems' cost of revenues rose
89% (filed on [p.40](https://agentii.ai/v/RKLB/sec109/40)). `[DEDUCTED]` · `DEMONSTRATED` as
inputs. The launch segment is where the cost curve is actually moving — **and it is 19% of the
business and shrinking**, which is the tension this thesis exists to test.

### The segment boundary is visible in the products/services cut

The same note splits each segment by products and services
[📄 RKLB 10-Q p.33](https://agentii.ai/v/RKLB/sec109/33) `[FACT]` · `DEMONSTRATED`:

| Q2 2026 | Products | Services | Total | Product GM | Service GM |
|---|---:|---:|---:|---:|---:|
| Launch Services | **$0** | $44,586 | $44,586 | — | 42.86% |
| Space Systems | $181,347 | $8,133 | $189,480 | 35.24% | 19.16% |
| Total | $181,347 | $52,719 | $234,066 | 35.24% | **39.20%** |

Gross profit is filed in the same two tables and grounds every ratio above: Space Systems
products `$63,908` (`63,908 / 181,347 = 35.24%`), Launch Services services `$19,110`
(`19,110 / 44,586 = 42.86%`), Space Systems services `$1,558` (`1,558 / 8,133 = 19.16%`),
total services `20,668 / 52,719 = 39.20%`. Cost of revenues is filed alongside
(products `$117,439`; services `$25,476` and `$6,575`), so every cell closes on a filed
operand — the ratios are `MODELED` arithmetic, their inputs `DEMONSTRATED`.

**Launch Services is a 100% services segment — it has zero products revenue in all four
periods.** Space Systems is 95.7% products ($181,347 / $189,480) and its margin is a *products*
margin; its small services arm runs at **19.16%**, roughly half the segment rate. Two
implications. First, the consolidated products/services split is a proxy for the segment split
without being one: consolidated services revenue of $52,719k is Launch Services ($44,586k) plus
Space Systems services ($8,133k), so *"services revenue"* in any consolidated read is ~85%
launch. Second, comparing Launch Services' 42.86% margin against Space Systems' 34.55% is
**not** comparing like with like — it compares a services margin against a products margin. Both
bases are shown; neither is quoted alone (DA-30).

---

## 3. `launch revenue` has three bases — every basis reported (DA-30)

"Launch revenue" is a DA-registered metric at RKLB and it does not mean one thing. All three
bases for Q2 2026, all filed or derived from filed cells:

| Basis | Q2 2026 | Q2 2025 | What it measures | Source |
|---|---:|---:|---|---|
| **(A) Segment-table total** | **$44,586k** | $46,646k | Revenue *recognised* on launch contracts, incl. over-time HASTE and "other launch revenue" | [p.32](https://agentii.ai/v/RKLB/sec109/32) |
| **(B) Point-in-time only** | **$37,703k** | $39,256k | The subset recognised at launch completion | [p.11](https://agentii.ai/v/RKLB/sec109/11) |
| **(C) Per-launch implied** | **~$54,600k** | ~$39,500k | 6 missions × $9.1M / 5 missions × $7.9M, on a launch-**occurrence** basis | [p.37](https://agentii.ai/v/RKLB/sec109/37) |

**The spread between (A) and (C) is +22.5% in Q2 2026 and −15.3% in Q2 2025 — and the sign
flips.** The filing gives the reason, in its own words, and this is the cleanest DA-25
mechanism in the universe — the irreproducibility is *documented*, not inferred
[📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37) `[FACT]` · `DEMONSTRATED`:

- **"Revenue per launch" is defined on a different basis from the segment table.** *"Revenue per
  launch represents the average transaction price attributable to launch contract performance
  obligations **during the period in which the launch occurs, regardless of whether the revenue
  is recognized using the point-in-time or over-time method**."* The segment table is on the
  recognition basis. **The two bases differ by construction, so the metric cannot reconcile to
  any audited table** — that is a property of the disclosure, not a defect in our retrieval.
- **Q2 2026's occurrence basis exceeds the recognition basis** because *"Two of the six Electron
  launch missions ... were HASTE launch missions, for which revenue was recognized over time and
  was partially recognized in prior quarters."* Six missions occurred; more than their
  attributable revenue was recognised.
- **Q2 2025's occurrence basis falls short of the recognition basis** for the mirror reason: all
  five missions were point-in-time, and Launch Services revenue additionally contains
  *"increased other launch revenue of $5.7 million, which includes contract termination and
  study revenue"* — revenue inside the segment line that is attributable to **no launch** and so
  falls outside the per-launch numerator. `[DEDUCTED]` Bound on the residual: if the $5.7M
  increment is wholly "other launch revenue", adding it back to the occurrence basis moves the
  gap from **−15.3% to −3.1%** (`45.2 / 46.646 = −3.10%`). The *level* of other launch revenue is not
  disclosed, so this is a bound, not a reconciliation — `MODELED`, and it can never satisfy a falsifier.

**The margin side is the sharper exposure.** Cost per launch is `$4.4M` (Q2 2026) and `$5.0M`
(Q2 2025) [p.37](https://agentii.ai/v/RKLB/sec109/37). The implied gross margin is
`(9.1 − 4.4) / 9.1 = **51.65%**` against the audited segment rate of **42.86%** — a
**+8.79 pp** overstatement. In Q2 2025 it is `36.71%` vs `30.48%`, **+6.23 pp**. All four
periods, both bases:

| Period | Per-launch implied GM | Audited segment GM | Gap |
|---|---:|---:|---:|
| Q2 2026 | 51.65% | 42.86% | **+8.79 pp** |
| Q2 2025 | 36.71% | 30.48% | +6.23 pp |
| H1 2026 | 46.74% | 43.73% | +3.01 pp |
| H1 2025 | 29.33% | 26.07% | +3.26 pp |

**Both bases improve, and the per-launch basis overstates the level in every period.** A
cost-curve claim built on `revenue per launch − cost per launch` is `MODELED` and
**overstates margin by 3–9 pp against the audited table at every period tested.** The direction
(cost falling, `$5.0M` → `$4.4M`) survives both bases. The level survives neither.

---

## 4. The component identity — applied to every `operating_income` read

Every `operating_income` read is shown as `gross_profit − opex` in-line, with the opex
definition named. **Opex definition used: `Total operating expenses` = `Research and
development, net` + `Selling, general and administrative` — EXCLUSIVE of cost of revenues.**
The issuer states the definition itself: *"Our operating expenses consist of research and
development and selling, general and administrative expenses"*
[📄 RKLB 10-Q p.38](https://agentii.ai/v/RKLB/sec109/38) `[FACT]` · `DEMONSTRATED`.

| Period | Gross profit | Opex (R&D net + SG&A, excl. CoR) | `GP − opex` | Filed operating loss | ✓ |
|---|---:|---:|---:|---:|:-:|
| Q2 2026 | 84,576 | 142,090 | (57,514) | (57,514) | ✓ |
| Q2 2025 | 46,388 | 106,027 | (59,639) | (59,639) | ✓ |
| H1 2026 | 161,069 | 274,552 | (113,483) | (113,483) | ✓ |
| H1 2025 | 81,635 | 200,462 | (118,827) | (118,827) | ✓ |

All figures USD thousands; operands and results as filed on
[📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6); the subtractions are arithmetic directly
on filed cells.

**The trap, demonstrated.** RKLB's statement of operations has **no** `Costs and expenses`
subtotal line, so the inclusive operand must be constructed: `Total cost of revenues 149,490 +
Total operating expenses 142,090 = 291,580`. Using it, `84,576 − 291,580 = **(207,004)**` —
**false against the filed $(57,514)$ thousand by exactly the $149,490k cost of revenues**, an
overstatement of the loss by 3.6×. This is the same failure mode recorded at UTHR and at SPCX,
reached by construction here rather than by reading a filed subtotal.

**Segment-level component identity is unavailable, and that is a filed limit, not a gap.**
There is no segment operating income above because there is no segment opex: *"Management does
not regularly review either reporting segment's total assets or operating expenses"*
[📄 RKLB 10-Q p.33](https://agentii.ai/v/RKLB/sec109/33). The component identity therefore
**cannot be applied below the consolidated line at RKLB on any basis** — the gross-profit bound
is the only available segment-level operand, and §2 uses it.

**DA-23 sign-strip — CONFIRMED at RKLB, four of four periods.** The platform's XBRL layer serves
`us-gaap:OperatingIncomeLoss` for RKLB as `57514000`, `113483000`, `59639000` and `118827000` —
**all positive magnitudes** — against filed values of **$(57,514)k, $(113,483)k, $(59,639)k and
$(118,827)k** [📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6). This is the register's
original RKLB instance, re-verified against the filing rather than inherited: the component
identity returns the filed sign while the served fact returns `+`. `EPS × shares` is not an
admissible sign test and was not used. Note the page is *right* while the served fact is wrong
— `(57,514)` in parentheses on p.6 and `57514000` from the extractor — which locates the defect
in the extraction layer, not the filing.

---

## 5. The entity boundary moved the OPPOSITE way from SPCX's

DA-21 governs a line drawn inside a fixed legal perimeter. At RKLB the perimeter moved **four
times in eighteen months, and every move entered the perimeter forward-only** — the mirror
image of SPCX's retroactive common-control recast.

| Acquisition | Closed | Consideration | Where it lands |
|---|---|---|---|
| GEOST LLC | Aug 2025 | $275,000k + earnout | **Space Systems** — *"The goodwill has been allocated to the space systems operating segment"* [p.18](https://agentii.ai/v/RKLB/sec109/18) |
| Mynaric AG | 2026-04-14 | $160,802k | Space Systems (laser optical comms) [p.15](https://agentii.ai/v/RKLB/sec109/15) |
| Motiv Space Systems | 2026-05-26 | $40,000k cash + up to $20,000k earnout | Space Systems (SADAs, robotics) [p.13](https://agentii.ai/v/RKLB/sec109/13) |
| **Iridium Communications Inc.** | **pending** — agreement 2026-06-28, expected close 2027 | not disclosed | not disclosed [p.35](https://agentii.ai/v/RKLB/sec109/35) |

**The signature of purchase accounting is the existence of a pro forma table.** RKLB publishes
*"unaudited consolidated financial information ... gives effect to the GEOST, Mynaric and Motiv
acquisitions assuming they occurred on January 1, 2025"*
[📄 RKLB 10-Q p.18](https://agentii.ai/v/RKLB/sec109/18) `[FACT]` · `DEMONSTRATED`. Issuers
publish pro forma information precisely because the **primary comparatives are NOT recast**.
SPCX, presenting the same kind of event as a common-control share exchange, published **no**
pro forma table and recast its comparatives instead (§SPCX). The two issuers' entity boundaries
moved in the same direction — outward — and their reported growth rates are therefore not on
comparable bases.

The pro forma table quantifies RKLB's entity-boundary effect directly, and it is large:

| Basis | Q2 2026 | Q2 2025 | Q2 YoY | H1 2026 | H1 2025 | H1 YoY |
|---|---:|---:|---:|---:|---:|---:|
| **As filed** | 234,066 | 144,498 | **+62.0%** | 434,414 | 267,067 | **+62.7%** |
| **Pro forma (as if acquired 2025-01-01)** | 237,842 | 173,064 | **+37.4%** | 455,880 | 313,875 | **+45.2%** |
| **Spread** | | | **24.6 pp** | | | **17.4 pp** |

Pro forma figures as filed; growth rates are our arithmetic. `[DEDUCTED]` · `DEMONSTRATED` as
inputs. **Roughly two-fifths of RKLB's reported Q2 growth rate is the entity boundary.** This is
the RKLB analogue of SPCX's 34.3 pp ex-AI gap, and the comparison is instructive: SPCX's gap is
our construction, RKLB's is the issuer's own disclosure, and both exceed the effects this thesis
is trying to measure.

**The Launch Services series is the one that survives.** Goodwill was *"allocated to the space
systems operating segment"*, and the acquired businesses are laser optical communications,
satellite components, and robotics — all Space Systems. **No acquired entity lands in Launch
Services.** So Launch Services is an **organic** series; Space Systems is not. Backlog carries
the same contamination: total backlog rose from `$1,847.3M` to `$2,355.9M`, *"primarily a result
of continued bookings **and backlog added through acquisitions**"*, of which `$1,415.8M` is
space systems and `$940.2M` is launch services
[📄 RKLB 10-Q p.38](https://agentii.ai/v/RKLB/sec109/38) `[FACT]` · `DEMONSTRATED`. `[DEDUCTED]`
The launch-services backlog number is the only one of the two the issuer does not attribute to
acquisitions.

**This is the same structural result SPCX produced, reached from the opposite accounting
treatment.** At both issuers, the launch segment is the series that the entity boundary does not
touch — SPCX's Space (legacy, and the only segment earning launch revenue) and RKLB's Launch
Services (organic, no acquired entity). And at both issuers, that segment is the one that is not
growing with the consolidated total. `[DEDUCTED]`

---

## 6. Mode: `business-model-classification`

**Business Model**: **Product-led vertically integrated manufacturer with a services segment
attached** — and the services segment is the one the name advertises. `[VIEW]`

**Core Offering** [📄 RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32),
[p.35](https://agentii.ai/v/RKLB/sec109/35) `[FACT]` · `DEMONSTRATED`:

| Segment | Core offering | Revenue type | Q2 2026 revenue | Share |
|---|---|---|---:|---:|
| Launch Services | Dedicated mission and rideshare launch; HASTE suborbital | Service (fixed-price contract) | $44,586k | 19.05% |
| Space Systems | Spacecraft components (reaction wheels, star trackers, radios, separation systems, solar, batteries, optical) and spacecraft manufacturing | **Product** (95.7%) | $189,480k | 80.95% |

**Positioning**: **Mid-tier and converging.** `[VIEW]` The consolidated gross margin is
**36.13%** (Q2 2026) and **37.07%** (H1 2026), up from 32.10% and 30.57%. That is a
manufacturing profile, not a premium-services one — it sits between a components supplier and a
pure platform. The movement is what matters: **+4.03 pp Q2 / +6.50 pp H1** on a business growing
62%, which is the signature of *"increasing our production rate resulting in greater absorption
of these costs is our most critical cost reduction initiative"* — the issuer's own filed
statement of where its margin comes from
[📄 RKLB 10-Q p.38](https://agentii.ai/v/RKLB/sec109/38) `[FACT]` · `DEMONSTRATED`.

**The business model is `enabler`, not a launcher, on the value-pool map's enum.** `[DEDUCTED]`
Launch is 19.05% of revenue and contributed **−2.3%** of the quarter's growth. What RKLB
actually sells at scale is **components and spacecraft to the merchant market** — *"enabled
Rocket Lab to deliver high-volume manufacturing of critical spacecraft components and software
solutions at scale prices to the broader spacecraft merchant market"*
[📄 RKLB 10-Q p.35](https://agentii.ai/v/RKLB/sec109/35) — plus an *"end-to-end mission
solution encompassing launch, full spacecraft manufacturing, ground services, mission
operations and optical systems"*. The issuer is explicit that its own vertical integration
serves both itself and third parties: acquisitions *"brought incremental vertically-integrated
capabilities for our own spacecraft family and also enabled Rocket Lab to deliver ... to the
broader spacecraft merchant market."* **RKLB monetises the merchant market; SPCX does not.**
That is the structural distinction between the two issuers' business models, and it is filed.

**`operator_class` — and the non-comparability it forces, stated in-line.** On the value-pool
map's enum (`captive_integrated`, `independent_launch`, `payload_customer`, `enabler`,
`adjacent`) RKLB is **`enabler`**; SPCX is **`captive_integrated`**. `[DEDUCTED]` **RKLB's
Launch Services gross margin of 42.86% is therefore NOT comparable to SPCX's Space segment
margin of −56.34%, and neither is comparable to the other's on any margin line.** The reason is
DA-06's, not a scale effect: SPCX launches to itself, so for ~74% of its launches **no
transaction price exists at all** and the launch cost is capitalised into its own satellites,
while RKLB sells every Electron mission to a third party at a price set in the market. One
number prices a sale; the other prices an internal transfer that the issuer does not recognise
as revenue. **Any artifact in this thesis that ranks the two launch segments by margin is
comparing a market price to an accounting residual and is invalid** — the comparison must be
made on cost per kilogram or not at all (PIL-1's basis), and even there SPCX files no
denominator for the internal launches.

**Neutron is the model's open hinge, and the schedule is slipping in the issuer's own words.**
*"Production of the Stage 1 tank is currently aligned with the target delivery of Neutron to the
launch pad in Q4 2026. While the window for an end-of-year launch date is narrowing..."*
[📄 RKLB 10-Q p.35](https://agentii.ai/v/RKLB/sec109/35) `[FACT]` · `DEMONSTRATED`. Neutron is
the entire medium-lift case (PIL-4) and it has **no revenue in any period in this artifact**.

---

## 7. Mode: `distribution-channel-analysis`

**Distribution Model**: **Direct sales, with an unusual and disclosure-heavy third element —
vendor financing extended to the customer.** `[VIEW]`

| Segment | Channel | Evidence |
|---|---|---|
| Launch Services | Direct, dedicated mission or rideshare | [p.32](https://agentii.ai/v/RKLB/sec109/32) |
| Space Systems | Direct; components to the *"broader spacecraft merchant market"*; long-term fixed-price builds plus purchase-order component sales | [p.35](https://agentii.ai/v/RKLB/sec109/35), [p.38](https://agentii.ai/v/RKLB/sec109/38) |
| Both | **Subordinated customer loans** on multi-launch agreements | [p.13](https://agentii.ai/v/RKLB/sec109/13) |

No reseller or distributor channel is disclosed. The channel that matters analytically is the
third row, because it is a **financing channel embedded in a sales channel** — and it sits
entirely in the launch business [📄 RKLB 10-Q p.13](https://agentii.ai/v/RKLB/sec109/13)
`[FACT]` · `DEMONSTRATED`:

> *"In connection with the signing of three separate multi-launch agreements with commercial
> customers, the Company entered into subordinated loan and security agreements. The commercial
> customers may choose to have certain milestone payments financed under the terms of the
> subordinated loan and security agreements. The receivables will bear no interest until the
> initial launch date passes, after which interest will accrue at a fixed rate of 9.5%, 10.8% or
> 12.6%, based on the commercial customer."*

| Measure | June 30, 2026 | December 31, 2025 | Change |
|---|---:|---:|---:|
| Customer financing receivable, current | $9,000k | $6,750k | +33.3% |
| Customer financing receivable, non-current | $23,150k | $16,138k | +43.4% |
| **Total** | **$32,150k** | **$22,888k** | **+40.5%** |
| Interest income (Q2 / H1 2026) | $656k / $1,218k | $497k / $877k (2025) | +32.0% / +38.9% |

**Strategic Implication**: **the launch segment is buying volume with its balance sheet, and
the volumes are not showing up in launch revenue.** `[VIEW]` Three of RKLB's commercial
multi-launch customers are financed by subordinated loans at 9.5–12.6%; the receivable grew
40.5% in six months; and one prior facility was **fully paid off and terminated** in July 2025
(`$7,489k`). Meanwhile Launch Services revenue fell 4.4% in Q2. Two readings are live and the
disclosure does not separate them: this is a customer-acquisition tool that works, or it is
financing demand that would not otherwise exist — and the fact that financing receivable
(+40.5%) and launch revenue (−4.4%) move in opposite directions over the same window is the
observation that keeps both alive. `[DEDUCTED]` **What would resolve it:** the launch revenue
attributable to financed versus unfinanced customers. It is not disclosed.

**Historical Channel Mix Trend (Trailing 3 Years)**: **`UNEXERCISED`, not clean.** No channel
mix series is disclosed; the customer-financing disclosure begins with "three separate
multi-launch agreements" with no date for the programme's inception, so even the financing
channel has no multi-year series in this filing. Recorded as a coverage limit below.

---

## 8. Mode: `revenue-composition-and-concentration`

### Breakdown

**By recognition model** — Q2 2026, USD thousands, filed
[📄 RKLB 10-Q p.11](https://agentii.ai/v/RKLB/sec109/11) `[FACT]` · `DEMONSTRATED`:

| Segment | Point-in-time | Over-time | Total | PIT share |
|---|---:|---:|---:|---:|
| Launch Services | 37,703 | 6,883 | 44,586 | 84.6% |
| Space Systems | 56,623 | 132,857 | 189,480 | 29.9% |
| **Total** | **94,326** | **139,740** | **234,066** | 40.3% |

Q2 2025 comparatives: Launch Services `39,256 / 7,390 / 46,646`; Space Systems
`31,070 / 66,782 / 97,852`; Total `70,326 / 74,172 / 144,498`. H1 2026: `93,268 / 14,981 /
108,249`; `88,772 / 237,393 / 326,165`; `182,040 / 252,374 / 434,414`. H1 2025: `74,731 /
7,507 / 82,238`; `50,334 / 134,495 / 184,829`; `125,065 / 142,002 / 267,067`.

**The two segments are near-mirror images on recognition model.** Launch Services is 84.6%
point-in-time — recognised at the launch event. Space Systems is 70.1% over-time — recognised on
a cost-to-cost progress measure. `[DEDUCTED]` This has a direct consequence for the thesis: **a
quarter's Launch Services revenue is a lagging and lumpy function of mission completion, while a
quarter's Space Systems revenue is a smooth function of cost incurred.** The −4.4% launch
revenue print is therefore *not* a demand signal — the issuer names the cause (*"revenue
recognition timing"*, two HASTE missions partly recognised in prior quarters) — and an artifact
that reads it as one will be reading the recognition model, not the market.

**By product vs service (consolidated)**: products `$181,347k / $92,725k / $308,835k /
$173,529k`; services `$52,719k / $51,773k / $125,579k / $93,538k`
[📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6) `[FACT]` · `DEMONSTRATED`. Product
revenue grew **+95.6%** Q2 YoY and service revenue **+1.8%**. The composition shift is
overwhelming and it is entirely Space Systems.

**By end market**: no end-market split is filed. What *is* filed is a single counterparty
share, and it is the largest concentration in this artifact
[📄 RKLB 10-Q p.13](https://agentii.ai/v/RKLB/sec109/13) `[FACT]` · `DEMONSTRATED`.

**By geography**: not filed at the required granularity in this 10-Q —
`UNRESOLVABLE-FROM-PUBLIC-SOURCES`. Mynaric brought *"European footprint"* per the filing's
keywords but no regional revenue table is presented.

### Concentration Risk Matrix

| Counterparty | Basis | Value | Threshold ≥20%? |
|---|---|---:|---|
| **Government customer** | **% of total revenue, H1 2026** | **42%** | **FLAGGED** |
| MDA Corporation | % of total accounts receivable, net, at 2026-06-30 | 11% | Below on AR; revenue share not disclosed |

**The single largest concentration at RKLB is a customer *class*, not a named customer, and it
is 42% of revenue.** `[DEDUCTED]` The disclosure gives a percentage without a name
(*"Government customer | 42%"*), and it is on the **revenue** basis for the **six months** —
the prior-year comparative is not presented in the same table, so the *trend* in this
concentration is not determinable from this filing. On a ≥20% test, RKLB has exactly one
flagged concentration and it is governmental. That is a materially different risk profile from
SPCX, whose two flagged counterparties are both below 20% and split across segments.

Note the interaction with §7: the customer-financing channel is with **commercial** customers,
while the dominant concentration is **governmental**. `[DEDUCTED]` The financing programme is
not buying the revenue that dominates the book.

### Temporal Comparison

| Measure | Q2 2025 → Q2 2026 | H1 2025 → H1 2026 |
|---|---|---|
| Launch Services share of revenue | 32.28% → **19.05%** (−13.23 pp) | 30.79% → 24.92% (−5.87 pp) |
| Space Systems share | 67.72% → 80.95% | 69.21% → 75.08% |
| Launch Services gross margin | 30.48% → **42.86%** (+12.38 pp) | 26.07% → 43.73% (+17.66 pp) |
| Product revenue share | 64.17% → **77.48%** | 64.98% → 71.09% |

**Launch is losing revenue share and gaining margin.** Both movements are large, both are filed,
and they run in opposite directions — which is the single most important thing a later segment
comparison has to carry (P2). `[VIEW]`

---

## Coverage Gaps and Unresolved Items

| # | Item | Disposition | What would resolve it |
|---|---|---|---|
| 1 | **Basis C is permanently unconstructible.** No segment operating income, opex, or asset base exists or can be derived: *"Management does not regularly review either reporting segment's total assets or operating expenses"* — a filed, present-tense limit. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (structural, permanent) | Nothing short of a change in the issuer's internal reporting; the disclosure is not required by any standard |
| 2 | **This is a `standalone_pre_merger` artifact and the perimeter is about to move again, materially.** RKLB agreed on 2026-06-28 to acquire **Iridium Communications Inc.**, expected to close 2027 [p.35](https://agentii.ai/v/RKLB/sec109/35). No consideration, no segment allocation, and no pro forma are disclosed. **Flagged for the IRDM artifacts in this thesis: an IRDM `standalone_pre_merger` tag and an RKLB `standalone_pre_merger` tag will describe the same counterparty from two sides of one pending transaction.** | Open — future event, and cross-artifact | Note 1 of the next 10-Q; the merger proxy |
| 3 | **The mixed-contract revenue-allocation key is not disclosed.** Revenue is allocated *"based upon the overall costs incurred for each of the reporting segments in comparison to total overall costs of the contract"* — method filed, key and magnitude not. **This exposes the Launch/Space-Systems split to an unobservable input**, and it is the largest single DA-21 exposure at this issuer. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | The allocation key and the revenue subject to it; the issuer discloses neither |
| 4 | **The level of "other launch revenue" is not disclosed** (termination and study revenue), so the per-launch-to-segment reconciliation in §3 is a bound, not a reconciliation. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | The absolute amount, disclosed only as a $5.7M *change* |
| 5 | **Government-customer concentration has no prior-year comparative**, so its trend is indeterminable from this filing. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` from the 10-Q | Prior 10-Qs, or the annual report |
| 6 | **Geography is not disaggregated**, despite the Mynaric acquisition bringing a European footprint. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` from the 10-Q | The annual report |
| 7 | **Channel-mix trend is `UNEXERCISED`, not clean.** No multi-year series exists for any channel, including the financing channel. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | A multi-year channel or financing disclosure |
| 8 | **Capital structure is discontinuous, which invalidates share-count detectors (DA-28).** Convertible-note shares excluded from the diluted denominator fell from `69,261,530` to `2,607,745`, a collared-forward line of `7,451,200` appeared, and RSUs fell from `23,616,300` to `13,095,520` [p.32](https://agentii.ai/v/RKLB/sec109/32). Any per-share or market-cap-derived metric spanning these periods is not on one basis. | `DERIVED` — recorded, not resolved here | Out of scope for `business-model`; flagged for the `recent-quarter` / `ratio-analysis` artifacts |
| 9 | **`get_segment_data` is unusable** (fails on `column "k" does not exist` and double-counts); `data_freshness` reports 2027-04-12. Every segment figure here was read directly from filing pages. | `UNRESOLVABLE-FROM-PLATFORM` | Tool repair — no artifact-level remedy |

**Unresolved by design:** frontmatter carries `unresolvable: false` because the *segment
boundary* question this artifact exists to answer — RKLB's launch/space-systems line is a
cost-allocation line that terminates at gross profit — **is fully resolved from the filing**.
The nine items above are permanent structural limits and forward-looking perimeter changes
recorded for downstream artifacts, not failures of this artifact's own question.

---

## Citations

| Page | Used for |
|---|---|
| [📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6) | Condensed consolidated statements of operations — revenue, cost of revenues, R&D net, SG&A, operating loss, all four periods |
| [📄 RKLB 10-Q p.11](https://agentii.ai/v/RKLB/sec109/11) | Note 3 — revenue by recognition model (point-in-time / over-time) × segment |
| [📄 RKLB 10-Q p.13](https://agentii.ai/v/RKLB/sec109/13) | Concentration (MDA 11% of AR; government 42% of H1 revenue); **customer financing**; Note 4 Motiv |
| [📄 RKLB 10-Q p.15](https://agentii.ai/v/RKLB/sec109/15) | Mynaric acquisition, closed 2026-04-14; consideration and goodwill |
| [📄 RKLB 10-Q p.18](https://agentii.ai/v/RKLB/sec109/18) | GEOST intangibles and goodwill allocated to space systems; **unaudited pro forma information** |
| [📄 RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32) | Note 18 — **segment definition and cost-allocation rule**; segment revenue/cost of revenues/gross profit tables; EPS note; DA-28 inputs |
| [📄 RKLB 10-Q p.33](https://agentii.ai/v/RKLB/sec109/33) | Segment × products/services tables; **the Basis C limit**; Note 19 related party |
| [📄 RKLB 10-Q p.35](https://agentii.ai/v/RKLB/sec109/35) | Space systems overview and acquisition history; **Iridium pending acquisition**; Neutron schedule; Space Force awards |
| [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37) | Build-rate and cadence; **revenue/cost per launch definitions**; per-launch and per-cost figures; 62% / $2.1M launch-revenue decrease |
| [📄 RKLB 10-Q p.38](https://agentii.ai/v/RKLB/sec109/38) | **Opex definition**; cost-of-revenues drivers; **backlog** with segment split; revenue recognition |
| [📄 RKLB 10-Q p.40](https://agentii.ai/v/RKLB/sec109/40) | MD&A — segment revenue and cost-of-revenue changes; R&D; SG&A; interest expense |

*Accession `0001819994-26-000062`, filed 2026-08-10. citation_id `sec109`. All figures USD
thousands unless otherwise stated. `deal_security_basis: standalone_pre_merger` per P11.*
