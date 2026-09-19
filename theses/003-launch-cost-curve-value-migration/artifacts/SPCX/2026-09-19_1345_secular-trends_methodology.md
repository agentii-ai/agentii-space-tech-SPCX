---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-2
ticker: SPCX
skill: secular-trends
mode: methodology
generated_at: 2026-09-19T13:45:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "e6b41dbb2426"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: "DA-08"
    chosen_reading: "a 'launch' is counted on the issuer's filed customer-launch definition — an EXTERNAL customer payload constitutes the PRIMARY payload and mission parameters are designed around it; Starship launches are all classified internal to date; the count is of successful orbital and flight tests only, excluding cancellations and scrubs"
  - da_id: "DA-07"
    chosen_reading: "mass to orbit is the filed metric in metric tons, read as the TOTAL and split into customer and internal payloads as filed; it is a throughput measure, not a capacity measure, and it is NOT the sum of vehicle capability"
  - da_id: "DA-21"
    chosen_reading: "SPCX's segment names are quoted verbatim and its Space boundary is read as the CUSTOMER boundary, because the issuer files that 'our Space segment revenue only reflects our customer launches and customer activities'; DA-21's recorded LIMIT applies here — it governs a boundary drawn by management inside a FIXED legal perimeter, and it does NOT reach the case where the comparative periods were drawn on a DIFFERENT perimeter (the xAI/X common-control mergers, which recast the comparatives)"
  - da_id: "DA-30"
    chosen_reading: "every cadence rate is quoted on BOTH the three-month and six-month bases, because they point in OPPOSITE directions for customer share and for customer-launch count; neither basis is adopted as THE reading, and the spread is reported as the finding"
  - da_id: "DA-25"
    chosen_reading: "the AI segment's filed +247.5% growth rate is a SEGMENT rate on a recast comparative; it is not an organic growth rate and it is not reproducible as a like-for-like series, so it is always reported alongside the ex-AI consolidated rate"
  - da_id: "DA-23"
    chosen_reading: "every negative read here (segment losses, net loss) is taken from the printed page and re-checked against the component identity, gross profit minus opex on an opex definition EXCLUSIVE of cost of revenue, rather than read from the extracted layer"
evidence_grade: DEMONSTRATED
key_metrics:
  ai_capex_h1_2026_musd: 23551
  space_capex_h1_2026_musd: 2226
  revenue_per_customer_launch_q2_2026_musd: 64.8
  customer_launch_share_q2_2026_pct: 26.3
citations:
  - figure: "SPCX sec8 p.35"
    ticker: SPCX
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "SPCX sec8 p.36"
    ticker: SPCX
    citation_id: sec8
    page_no: 36
    url: https://agentii.ai/v/SPCX/sec8/36
    located_via: read_source_pages
  - figure: "SPCX sec8 p.42"
    ticker: SPCX
    citation_id: sec8
    page_no: 42
    url: https://agentii.ai/v/SPCX/sec8/42
    located_via: read_source_pages
  - figure: "SPCX sec8 p.13"
    ticker: SPCX
    citation_id: sec8
    page_no: 13
    url: https://agentii.ai/v/SPCX/sec8/13
    located_via: read_source_pages
  - figure: "SPCX sec8 p.11"
    ticker: SPCX
    citation_id: sec8
    page_no: 11
    url: https://agentii.ai/v/SPCX/sec8/11
    located_via: read_source_pages
  - figure: "SPCX sec8 p.38"
    ticker: SPCX
    citation_id: sec8
    page_no: 38
    url: https://agentii.ai/v/SPCX/sec8/38
    located_via: read_source_pages
  - figure: "SPCX sec8 p.31"
    ticker: SPCX
    citation_id: sec8
    page_no: 31
    url: https://agentii.ai/v/SPCX/sec8/31
    located_via: read_source_pages
  - figure: "SPCX sec8 p.14"
    ticker: SPCX
    citation_id: sec8
    page_no: 14
    url: https://agentii.ai/v/SPCX/sec8/14
    located_via: read_source_pages
  - figure: "SPCX sec8 p.47"
    ticker: SPCX
    citation_id: sec8
    page_no: 47
    url: https://agentii.ai/v/SPCX/sec8/47
    located_via: read_source_pages
  - figure: "SPCX sec8 p.30"
    ticker: SPCX
    citation_id: sec8
    page_no: 30
    url: https://agentii.ai/v/SPCX/sec8/30
    located_via: read_source_pages
  - figure: "SPCX sec8 p.46"
    ticker: SPCX
    citation_id: sec8
    page_no: 46
    url: https://agentii.ai/v/SPCX/sec8/46
    located_via: read_source_pages
  - figure: "SPCX sec8 p.44"
    ticker: SPCX
    citation_id: sec8
    page_no: 44
    url: https://agentii.ai/v/SPCX/sec8/44
    located_via: read_source_pages
  - figure: "SPCX sec8 p.43"
    ticker: SPCX
    citation_id: sec8
    page_no: 43
    url: https://agentii.ai/v/SPCX/sec8/43
    located_via: read_source_pages
---

# SPCX × secular-trends — the demand-side trajectory

**Is constellation cadence responding to the launch-cost curve at all?**

**Answer: no — and at SPCX the negative is unusually clean, because the demand that fell
hardest is the demand that pays no price.**

Filed evidence, three-and-six months ended 2026-06-30, from SPCX's 10-Q filed 2026-08-04.
All figures are `DEMONSTRATED` (filed cells, or exact arithmetic on filed cells) unless
marked otherwise.

---

## 0. The finding, on one page

The thesis's master COST variable is launch cost. If the curve were pulling demand, the
issuer with the lowest claimed cost and the only reusable vehicle at cadence would show
rising throughput. **It shows falling throughput on every filed measure.**

| Throughput measure | Q2 2026 | Q2 2025 | Δ | H1 2026 | H1 2025 | Δ |
|---|---:|---:|---:|---:|---:|---:|
| Mass to orbit (metric tons) | **485** | 652 | **−25.6%** | **1,041** | 1,102 | **−5.5%** |
| — attributable to customer payloads (t) | 87 | 88 | −1.1% | 132 | 163 | **−19.0%** |
| — attributable to internal payloads (t) | 397 | 563 | **−29.5%** | 908 | 938 | −3.2% |
| Falcon launches (number) | **37** | 45 | **−17.8%** | 77 | 81 | −4.9% |
| — of which customer launches | 10 | 9 | **+11.1%** | 17 | 21 | **−19.0%** |
| — of which internal launches | 27 | 36 | **−25.0%** | 60 | 60 | 0.0% |
| Starship launches (number) | 1 | 1 | 0.0% | **1** | 3 | **−66.7%** |
| Total launches (Falcon + Starship) | 38 | 46 | **−17.4%** | 78 | 84 | −7.1% |

Source: [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35). Total launches is the sum of
the two filed lines; it is not itself a printed line (`DERIVED`). Starship launches are all
classified internal to date — the issuer files that — so total = Falcon + Starship with no
double count.

**Three separate readings of the same page, and they do not agree with each other:**

1. **The issuer's own stated expectation is contradicted by the issuer's own numbers.** p.35
   files: *"Mass to orbit and launches generally grow more rapidly than Space segment revenue
   because these metrics include our internal constellation deployments from which we do not
   recognize inter-segment revenue."* In H1 2026 mass to orbit **fell 5.5%** while Space
   segment revenue fell 1.9% — the stated relationship held by 3.6 pp in the wrong direction,
   and both fell.
2. **The captive demand — the demand with no price in it at all — fell hardest.** Internal
   launches fell **25.0%** (Q2) against a 17.4% fall in total launches and a **+11.1%** rise in
   customer launches. Internal payload mass fell **29.5%** against 25.6% for the total. So on
   the quarter basis, **the more captive the demand, the larger the fall.**
3. **The customer share of launches is period-dependent.** Q2: **19.6% → 26.3%** (+6.7 pp).
   H1: **25.0% → 21.8%** (−3.2 pp). **The two bases disagree in sign.** At 38–46 launches per
   quarter, one launch is 2.2–2.6 pp of the share, so the +6.7 pp Q2 move is about 2.5
   launches — inside the granularity of the metric.

**The conclusion the evidence supports**: on the half-year basis — the longer, less lumpy of
the two, and the one with N ≈ 4× the quarterly count — **launch activity fell while the
claimed cost curve fell**, and the fall was concentrated in captive demand. The demand side is
**not** pricing off the curve; at SPCX it is not even *producing* off it.

**The conclusion the evidence does not support**: attributing the fall to price-insensitivity
*at the margin*. SPCX files **no basis-B (marginal cost) figure at all** (F2/F19), so at this
issuer the curve is `CLAIMED`, not `DEMONSTRATED` — and an unmeasured independent variable
cannot carry a causal claim. The *level* finding is `DEMONSTRATED`; the *mechanism* is open.

---

## 1. Mode 1 — `evaluate-company-s-exposure-to-major-secular-technology-trends`

### 1.1 The four secular trends SPCX is exposed to, and how each is actually filed

| Trend | Exposure | Where it is filed | Grade |
|---|---|---|---|
| **Falling cost of access to space / reusability** | The whole Space segment; the thesis's master COST variable | Space segment: revenue $962M (Q2), CoR $329M, R&D $1,076M | `CLAIMED` at SPCX — **no basis-B figure is filed** (F19) |
| **Satellite broadband as a terrestrial-access substitute** | Connectivity | 12.0M Starlink subscribers (from 6.0M); ARPU **$66** (from **$85**) | `DEMONSTRATED` |
| **AI compute build-out** | AI segment | Nameplate compute draw **1.4 GW** (from 0.4 GW); segment revenue $2,561M | `DEMONSTRATED` for the metric, `MODELED` for the orbital reading — see §2 |
| **Data as a monetisable asset** | AI segment (data licensing) and Connectivity (service data) | Data licensing is named as a revenue line but **not disaggregated** | `CLAIMED` — see §3 |

### 1.2 The cadence test, stated so it can fail

The question the matrix asks is whether constellation cadence responds to the curve. The test
used here is the issuer's own throughput disclosure, because it is the one measure that is
**not** filtered through a revenue boundary.

Why SPCX is the right test case, and why the test has power:

- **Single issuer, single vehicle family, single constellation.** No cross-issuer period or
  boundary normalisation is needed. The denominator problem that makes the sector's cost
  claims fragile (DA-01 A/B/C, DA-02) does not enter a *count*.
- **The captive half has no price in it.** SPCX files that for Starlink launches *"the Company
  does not recognize any inter-segment revenue, rather those launch costs are capitalized in
  satellites in Property, plant, and equipment, net"*
  ([📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36)). So internal launches carry no
  transaction price (DA-06) and no budget friction. If price elasticity were driving cadence
  anywhere, it cannot be here — and this is where the fall is largest.
- **The comparison is against the issuer's own filed expectation** (§0, item 1), so the
  interpretation does not depend on our model of what should have happened.

### 1.3 What the filing does and does not say about the decline

The key-metrics block offers **no explanation for the fall**. The MD&A explanations that do
exist are about revenue, not throughput, and they run the other way:

- Space revenue Q2 **+$216M, +29.0%**, which the issuer attributes to *"an increase in customer
  launches period over period from 9 … to 10 … and a favorable customer mix shift"*
  ([📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42)). **One additional customer launch
  is credited with a 29.0% revenue increase** — a price/mix statement, not a volume statement.
- Space revenue H1 **−$30M, −1.9%** — *"primarily driven by a decrease in customer launches
  period over period from 21 … to 17"* (same page). **The half-year revenue line is explained
  by the launch count; the quarter's is explained by price.**

**Two opposite-signed rates on one activity, both correct and both the filing's** (F5
consequence 3). Any quotation of one without its basis is a DA-30 collapse. On the
revenue-per-launch arithmetic — valid here because the issuer files that *"the Company
recognizes Launch Services revenue at a point in time … Revenue and costs are deferred and not
recognized until upon the launch or deployment of the customer's payload"*
([📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36)), so the recognized revenue maps to
the launches in the period:

| Per-customer-launch arithmetic (Segment basis, `DERIVED`) | Q2 2026 | Q2 2025 | Δ |
|---|---:|---:|---:|
| Launch Services revenue (filed, $M) | 648 | 490 | +32.2% |
| Customer launches (filed, count) | 10 | 9 | +11.1% |
| **Implied revenue per customer launch ($M)** | **64.8** | **54.4** | **+19.0%** |
| Space segment cost of revenue (filed, $M) | 329 | 330 | −0.3% |
| **Implied Space cost per customer launch ($M)** | **32.9** | **36.7** | **−10.3%** |

`DERIVED`: exact arithmetic on filed cells, but the numerator↔denominator mapping is an
assumption — Launch Services revenue is a Space-segment line and customer launches are a Space
operational line, and Space cost of revenue also absorbs Launch & Development
([📄 SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13)). **Read as a direction, not a level.**
The direction is: at SPCX the customer-facing launch price rose ~19% while the customer-facing
launch cost fell ~10% in the same quarter that total launch activity fell 17.4%. **That is the
pass-through question, and at this issuer the answer on the only constructible basis is that
the released value stayed with the launcher** (PIL-6's half-claim; `DERIVED`, one period, and
it cannot carry a falsifier under P4).

### 1.4 Verdict on the cadence question

| Basis | Activity | Curve | Response |
|---|---|---|---|
| H1 2026 vs H1 2025 (**preferred** — larger N) | mass to orbit −5.5%; total launches −7.1%; customer launches −19.0% | `CLAIMED` falling | **NONE** |
| Q2 2026 vs Q2 2025 | mass to orbit −25.6%; total launches −17.4%; internal launches −25.0% | `CLAIMED` falling | **NONE** |
| Customer share | Q2 +6.7 pp / H1 −3.2 pp | — | **sign-unstable** |

**Demand-side cadence is not responding positively to the cost curve.** On the preferred
half-year basis, mass to orbit and total launches both fell, and customer launches — the only
demand with a price in it — fell 19.0%.

**Recorded as `NON-FORMABLE`, not PASS:** the strong form of the question ("cadence responds to
*the curve*") requires the curve as an input, and at SPCX the curve is `CLAIMED`. Per §4 of the
brief, a `MODELED` input can never satisfy a falsifier; here the missing input is worse than
modelled — it is absent by construction (no basis-B figure is filed). So the *positive* claim
is not established, and the *negative* claim (cadence did not rise) is established
independently of the curve. **The falsifier outcome is UNEXERCISED on the causal limb and
DEMONSTRATED on the observational limb.**

---

## 2. Mode 2 — `deep-dive-ai-trend-assessment-for-companies-with-identified-ai-exposure`

### 2.1 What SPCX's AI segment actually is — and what it is not

Verbatim, from the issuer's own segment description:

> *"the AI segment operates a vertically integrated AI platform spanning a frontier LLM Grok,
> AI solutions for consumer and enterprise customers, X — a real-time information,
> entertainment, and free speech platform — and **AI computational infrastructure**."*
> — [📄 SPCX 10-Q p.11](https://agentii.ai/v/SPCX/sec8/11)

**There is no mention of orbit anywhere in that sentence, or in the AI segment's revenue and
expense descriptions** ([📄 SPCX 10-Q p.38](https://agentii.ai/v/SPCX/sec8/38)): advertising on
X; premium subscriptions on X and Grok; data licensing; API access to Grok models; *"the sale of
cloud services"*. Cost of revenue is *"data center facilities, including lease and hosting
costs, related support, maintenance, energy, and bandwidth costs, depreciation of servers and
networking equipment, public cloud hosting costs"*. R&D is *"the training of Grok … cloud
computing expenses … power generation costs, and depreciation of data center assets, including
processors"*.

**"AI computational infrastructure" is terrestrial. Reading it as orbital compute is a
false positive, and it is registered as one in `PROGRAM.md` §0.**

The independent confirmation is the metric the segment chose to disclose: *"Nameplate Compute
Draw: We calculate nameplate compute draw for a period as **the number of GPUs installed in our
data centers at the end of the period** multiplied by their respective all-in power draw… It
does not include power we install and use for our supporting infrastructure such as cooling
systems, power distribution losses, lighting, security systems, or facility-level overhead."*
([📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36)). **1.4 GW, from 0.4 GW** — a
3.5× increase in ground-based installed compute. The AI segment's own disclosed capacity metric
counts GPUs **in data centers**, and the disclosure names no orbital counterpart.

### 2.2 Orbital compute is not being out-built — it is being out-*chosen*

Three filing facts, none of which requires interpretation:

1. **The issuer states the intent to divert launch capacity to the terrestrial AI business**,
   twice, in identical words: *"We allocate a significant amount of launch capacity to our
   Connectivity segment, and **expect to allocate a significant amount to our AI segment in the
   future**"* ([📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35),
   [p.36](https://agentii.ai/v/SPCX/sec8/36)). The only party in the universe that could build
   an orbital compute constellation is stating where its launch capacity is going instead.
2. **The capital went to the ground.** H1 2026 capital expenditures: **AI $23,551M**, Space
   **$2,226M**, Connectivity **$2,699M** — AI is **~4.7× the other two combined** and
   **~10.6× the Space segment** ([📄 SPCX 10-Q p.31](https://agentii.ai/v/SPCX/sec8/31)). The
   capital-expenditure narrative names data centers *before* launch facilities: *"Interest is
   capitalized during the construction period for significant long term construction projects,
   such as the **AI infrastructure data centers and launch facilities**"*
   ([📄 SPCX 10-Q p.14](https://agentii.ai/v/SPCX/sec8/14)).
3. **The launch fleet's book value is shrinking while the compute base grows.** In the same
   PP&E note: **Servers and networking equipment $22,694M → $34,771M (+53.2%)**;
   **Data center infrastructure $2,960M → $3,991M**; **Construction-in-progress
   $4,604M → $12,554M (+172.7%)**, described as *"primarily … AI infrastructure that has not yet
   been placed in service"*; and **Flight vehicle hardware $1,689M → $1,557M (−7.8%)**
   ([📄 SPCX 10-Q p.14](https://agentii.ai/v/SPCX/sec8/14)).

**The AI segment is also the segment the issuer describes as the flexible one.** *"If our
near-term data center needs decrease in scale or ramp more slowly than expected … we may reduce
future capital expenditures in this segment and reallocate those expenditures to other
segments"* ([📄 SPCX 10-Q p.47](https://agentii.ai/v/SPCX/sec8/47)). Read with item 2: the
terrestrial AI build is the discretionary line, and launch capacity is the thing that may be
held back to feed it.

### 2.3 AI segment economics — and a basis collapse inside the segment

Component identity, in-line, on an **opex definition EXCLUSIVE of cost of revenue**
(opex = R&D + SG&A + restructuring + impairment; cost of revenue is the cost of sales):

| Segment | Period | Gross profit = revenue − cost of revenue | opex (R&D + SG&A + other) | gross profit − opex | filed income (loss) from operations |
|---|---|---:|---:|---:|---:|
| AI | Q2 2026 | 2,561 − 1,106 = **1,455** | 2,178 + 532 + 2 = **2,712** | **(1,257)** | **(1,257)** ✓ |
| Space | Q2 2026 | 962 − 329 = **633** | 1,076 + 99 = **1,175** | **(542)** | **(542)** ✓ |
| Connectivity | Q2 2026 | 4,291 − 2,060 = **2,231** | 294 + 281 = **575** | **1,656** | **1,656** ✓ |
| AI | H1 2026 | 3,379 − 1,562 = **1,817** | 4,557 + 995 − 9 = **5,543** | **(3,726)** | **(3,726)** ✓ |

All four close exactly ([📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30),
[p.31](https://agentii.ai/v/SPCX/sec8/31)). Extended to all three segments × four periods the
identity closes **12 of 12, zero failures** — SPCX is a clean site for DA-23, and the segment
rows sum to the consolidated operating loss exactly in both periods
((542) + 1,656 + (1,257) = **(143)**; (1,204) + 2,844 + (3,726) = **(2,086)**). Because
`us-gaap:CostsAndExpenses` INCLUDES cost of sales, the inclusive form of the identity is
**not** the one used here; the definition used is stated above.

**The basis collapse:** the AI segment's margin changes sign with the basis, and both bases are
the issuer's own:

| AI segment | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 |
|---|---:|---:|---:|---:|
| Revenue ($M) | 737 | 2,561 | 1,465 | 3,379 |
| Income (loss) from operations ($M) | (1,524) | **(1,257)** | (2,460) | (3,726) |
| **Operating margin** | −206.8% | **−49.1%** | −167.9% | −110.3% |
| **Segment Adjusted EBITDA ($M)** | (276) | **+1,146** | (387) | **+537** |
| **Segment Adj. EBITDA margin** | −37.5% | **+44.7%** | −26.4% | **+15.9%** |

Sources: [📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30),
[p.46](https://agentii.ai/v/SPCX/sec8/46), [p.47](https://agentii.ai/v/SPCX/sec8/47). **The AI
segment is loss-making by 49.1% of revenue and profitable by 44.7% of revenue in the same
period, on two bases the issuer publishes adjacently.** Neither may be quoted alone (DA-30).
`Segment Adjusted EBITDA` is defined as segment income (loss) from operations excluding
depreciation and amortization, share-based compensation, restructuring charges and impairments
— and the AI segment's D&A alone is **$1,885M in Q2 2026**, which is 73.6% of segment revenue.
**The AI segment's profit is entirely a function of how its own depreciation is treated.**

### 2.4 The AI revenue increment is concentrated in one new line and one new customer

| Item | Filed | Grade |
|---|---|---|
| AI segment revenue, Q2 2026 vs Q2 2025 | 2,561 vs 737 = **+1,824 (+247.5%)** | `DEMONSTRATED` |
| AI **solutions and infrastructure** revenue increase | **+$1,883M** | `DEMONSTRATED` |
| — of which **AI infrastructure revenue** | **+$1,600M**, *"as we began to offer cloud services to customers"* | `DEMONSTRATED` |
| — of which Grok and X subscription revenue | +$258M | `DEMONSTRATED` |
| — residual not named by the issuer | **+$25M** | `DERIVED` (1,883 − 1,600 − 258) |
| Advertising revenue | **−$59M** (the line *declined*) | `DEMONSTRATED` |
| Customer B — AI segment only — share of **consolidated** Q2 revenue | **19.5%** (below 10% in Q2 2025) | `DEMONSTRATED` |
| Implied Customer B revenue, Q2 2026 | 19.5% × 7,814 = **≈$1,524M** | `MODELED` |
| Implied Customer B revenue, H1 2026 | 12.2% × 12,508 = **≈$1,526M** | `MODELED` |
| **Implied Customer B revenue, Q1 2026 (by subtraction)** | **≈$2M** | `MODELED` |
| Customer B as share of the new AI infrastructure line | 1,524 / 1,600 ≈ **95%** | `MODELED` |

Sources: [📄 SPCX 10-Q p.44](https://agentii.ai/v/SPCX/sec8/44),
[p.13](https://agentii.ai/v/SPCX/sec8/13), [p.14](https://agentii.ai/v/SPCX/sec8/14). The
`MODELED` rows are flagged as such: the concentration disclosure gives a percentage of
consolidated revenue, not a dollar amount, and the Q1 figure is a subtraction of two modelled
figures.

**What is `DEMONSTRATED` and survives every reading**: the AI segment's **$1,600M** new line
is a cloud service the issuer says it *began* to offer, and a single AI-segment customer
accounts for a mid-teens-to-19.5% share of *consolidated* revenue whose dollar value is within
a rounding error of that line's entire increment. **A revenue line that begins, sold to one
customer, is not a value pool that migrated; it is a pool that was transacted.**

---

## 3. Mode 3 — `deep-dive-data-value-trend-assessment-for-companies-with-identified-data-exposure`

### 3.1 The data assets SPCX actually monetises

| Data asset | How it is monetised | Filed line | Quantified? |
|---|---|---|---|
| Starlink service data / network | Connectivity subscriptions and enterprise/government contracts | Consumer; Enterprise & Government; *includes Starlink Mobile* | Yes, but **not** as data |
| X platform engagement data | Advertising | Advertising **$367M** (Q2 2026), **declining** from $426M | Yes |
| X / Grok corpus | ****Data licensing** — *"data licensing arrangements"*; recognized ratably *"as the customer consumes and benefits from the use of the licensed data"* | **inside AI Solutions & Infrastructure** | **No — not disaggregated** |
| Earth-observation / remote-sensing data | Not filed anywhere in this 10-Q | — | **No** |

Source: [📄 SPCX 10-Q p.38](https://agentii.ai/v/SPCX/sec8/38),
[p.13](https://agentii.ai/v/SPCX/sec8/13).

**The data-value trend cannot be measured at SPCX.** The issuer names data licensing as a
revenue stream and its recognition policy, then reports it inside a single $2,194M
"AI Solutions & Infrastructure" line bundled with subscriptions, Grok API access and cloud
services. **There is no filed time series for the data asset.**

### 3.2 What the disclosed data-adjacent series do show

| Series | Basis | Q2 2025 | Q2 2026 | Δ |
|---|---|---:|---:|---:|
| Starlink subscribers (millions) | **end-of-period** count of unique service lines | 6.0 | **12.0** | **+100.0%** |
| Starlink ARPU ($/month) | period service revenue ÷ **average** subscribers ÷ months | 85 | **66** | **−22.4%** |
| Connectivity consumer revenue ($M) | segment, filed | 1,721 | **2,485** | **+44.4%** |
| Connectivity Enterprise & Government revenue ($M) | segment, filed | 867 | **1,806** | **+108.3%** |

Sources: [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35),
[p.36](https://agentii.ai/v/SPCX/sec8/36), [p.13](https://agentii.ai/v/SPCX/sec8/13). The issuer
states the composition itself: consumer growth is *"composed of 101.2% growth in Starlink
subscribers, offset by a 22.4% decline in Starlink subscriber ARPU, primarily due to
international expansion and the addition of lower priced service plans"*
([📄 SPCX 10-Q p.43](https://agentii.ai/v/SPCX/sec8/43)).

**Three findings, and one basis trap:**

1. **Connectivity monetisation is volume-led and price-declining.** Subscriber count doubled;
   ARPU fell 22.4%. The growth is in reach, not in yield per unit.
2. **The enterprise/government line grew 2.4× faster than consumer** (+108.3% vs +44.4%) — and
   this is the line the trailing-subscriber metric *excludes by definition* (the issuer files
   that subscriber count *"does not include managed enterprise and government customers"*).
3. **The basis trap: subscriber count is end-of-period; ARPU's denominator is the average over
   the period.** So `subscribers × ARPU × 3` does **not** reproduce consumer revenue
   (`DERIVED`, and it does not close: 12.0M × $66 × 3 ≈ $2,376M against a filed $2,485M, a
   −4.4% residual explained by the average-vs-end-of-period mismatch, not by an error in either
   filed figure). **Neither series may be combined with the other algebraically without
   restating the basis** (DA-10, DA-30).

**The data-value trend at SPCX is therefore a connectivity-volume trend with a declining unit
price, plus an unquantified licensing line.** It is not, on this filing, a data-monetisation
inflection.

---

## 4. The entity-boundary correction — why `+$1,824M` is not evidence of migration

This section exists because the most inviting evidence for PIL-2 — SPCX's AI-segment growth —
is an **acquisition artifact**, and the two merger dates sit *inside* the comparative periods.

**What is filed** ([📄 SPCX 10-Q p.11](https://agentii.ai/v/SPCX/sec8/11)): *"On February 2,
2026 ('xAI Merger Date'), the Company completed its acquisition of X.AI Holdings Corp.
('xAI')… Prior to the xAI Merger, on **March 28, 2025**, xAI completed its acquisition of X
Holdings Corp. ('X') and X.AI Corp. … **The Mergers were each effected through a share
exchange.**"* Plus: IPO June 2026 (638.9M Class A at $135.00, net proceeds **$85,675M**) and a
five-for-one forward split in May 2026.

**Two readings, both correct, and neither may be collapsed into the other:**

- **Reading 1 — recast comparative.** The AI column **is present in the 2025 comparative**:
  AI segment revenue is **$737M for Q2 2025** and **$1,465M for H1 2025**
  ([📄 SPCX 10-Q p.31](https://agentii.ai/v/SPCX/sec8/31),
  [p.13](https://agentii.ai/v/SPCX/sec8/13)). Common-control share exchanges are presented as
  if the combination had occurred at the beginning of the earliest period presented, so on this
  reading the comparatives are on a **constant perimeter** and the ex-AI figures are a
  **decomposition**, not an adjustment.
  - **Basis:** the AI column's presence in the comparative, and the segment note's filing of
    three segments in both periods.
- **Reading 2 — entity change.** The comparatives are a **pro-forma composite of a business
  SPCX did not operate**, so the growth rate does not measure growth of the operating entity.
  - **Basis:** the merger disclosure and its share-exchange mechanics.

**The correction this forces on an inherited artifact.** Thesis 001's SPCX business-model
artifact asserts that *"H1 2025 predates the xAI merger, so the AI column is absent."* **That
is false as filed**: AI revenue for Q2 2025 ($737M) and H1 2025 ($1,465M) is printed in this
10-Q on two separate pages. The comparative is **recast as-if-combined under common control**,
not absent. Corrected here.

**The rates, on both bases:**

| Basis | Q2 2026 vs Q2 2025 | H1 2026 vs H1 2025 | Grade |
|---|---:|---:|---|
| **Consolidated, as filed** | **+91.9%** (7,814 vs 4,071; +$3,743M) | **+53.7%** (12,508 vs 8,138; +$4,370M) | `DEMONSTRATED` |
| **Consolidated, ex-AI** | **+57.6%** (5,253 vs 3,334) | **+36.8%** (9,129 vs 6,673) | `DERIVED` (exact arithmetic on filed segments) |
| **Spread** | **34.3 pp** | **16.9 pp** | `DERIVED` |
| AI as share of the quarter's consolidated revenue increase | **48.7%** (1,824 / 3,743) | 43.8% (1,914 / 4,370) | `DERIVED` |

**Why the AI half of that growth does not support PIL-2.** PIL-2 claims the value pool
**migrated** to the integrator that owns the demand. A migrated pool is one that moved between
positions. The AI increment is not that:

- **It was acquired, not migrated.** The line begins *"as we began to offer cloud services to
  customers"* — a service that did not exist at scale in the comparative — and it is sold to a
  customer (B) that represented **below 10% of consolidated revenue in Q2 2025** and **19.5% in
  Q2 2026** ([📄 SPCX 10-Q p.14](https://agentii.ai/v/SPCX/sec8/14)).
- **It is not launch value.** Even taken at face value, it accrues to the **AI** segment. It is
  evidence about where SPCX's *non-launch* value sits — which supports PIL-2's second half
  ("not the launcher") without supporting its first half ("the integrator's launch business
  captured it").
- **The DA-21 limit is load-bearing here, and it is a LIMIT.** DA-21 governs a segment line
  drawn by management **inside a fixed legal perimeter** — LMT's Space ≠ NOC's Space. **It does
  not reach the case where the comparative periods were drawn on a different perimeter.** That
  is what the common-control mergers did. **So DA-21 cannot be cited to resolve this, and
  neither can its absence be read as clearance.**
- **No registered DA class covers it.** The register is DA-01…DA-30 (*no `DA-31` exists*). The
  closest is DA-28 (capital-structure discontinuity around an IPO invalidates share-count
  detectors) — which does apply to the IPO's effect on per-share series — but **no entry
  governs a change of reporting entity presented as a comparative.** Recorded as a **register
  gap**, with the resolving disclosure named in §5.

---

## 5. What could NOT be resolved

| # | Open item | Class | Resolving disclosure |
|---|---|---|---|
| 1 | **Why mass to orbit and internal cadence fell.** The key-metrics block files the levels and offers no explanation; the MD&A explains revenue, not throughput. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` on *mechanism*; the *levels* are `DEMONSTRATED` | A filing that decomposes mass to orbit by satellite variant and mission type, or any statement of the deployment target. **No registered DA class covers a change of reporting perimeter** — recorded as a register gap, not as a pending check. |
| 2 | **SPCX's cost curve at basis B.** No marginal-cost figure is filed, so the independent variable in "does cadence respond to the curve" is absent. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (basis B is not a disclosure SPCX makes) | A filed per-launch cost, or a segment cost table on a marginal basis. **This is the specific absence that returns `NON-FORMABLE` in §1.4.** |
| 3 | **Data licensing revenue as a series.** Named as a line; reported only inside a $2,194M bundle. | `REACHABLE-BUT-NOT-RECORDABLE` — the concept exists and is described, but no line item carries it | A disaggregation of AI Solutions & Infrastructure into subscriptions, data licensing, API, cloud services. |
| 4 | **Customer B's identity and dollar value.** Only a percentage of *consolidated* revenue is filed; the dollar figures in §2.4 are `MODELED`. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (issuers are not required to name a customer) | Not resolvable by any filing. **The `MODELED` figures must never be used to satisfy a falsifier.** |
| 5 | **The AI segment's orbital reading.** The AI segment's own definition, revenue, cost and capacity metric are all terrestrial. | **Resolved — and the resolution is negative** | The `PROGRAM.md` §0 false-positive trap for "AI computational infrastructure" is confirmed here rather than discovered; it is not an open item. |
| 6 | **Whether orbital compute is being out-built.** No listed issuer reports orbital-compute revenue (P10). | `UNRESOLVABLE-FROM-PLATFORM` — no issuer in the universe files the concept | Nothing in this corpus resolves it; it is a watch item, not a pool. |

**UNEXERCISED ≠ CLEAN.** Four items above are absences, not clearances.

---

## 6. Carry-forwards

1. **The cadence test returns a negative, and the captive demand fell hardest.** Internal
   launches −25.0%, internal payload mass −29.5%, against the total's −17.4%/−25.6% (Q2). The
   demand that pays no price is the demand that contracted most — which removes price
   elasticity as the explanation without supplying the real one.
2. **The customer-share direction is period-dependent (+6.7 pp on Q2, −3.2 pp on H1).** Quote
   either only with its basis. At 38–46 launches a quarter, one launch moves the share 2.2–2.6
   pp.
3. **Mass to orbit fell while the issuer's own filed expectation is that it grows faster than
   Space revenue.** The issuer's stated relationship between throughput and revenue is
   contradicted by its own H1 2026 cells.
4. **`+$1,824M` is not migration.** It is 48.7% of the quarter's growth, it sits in a segment
   whose own definition contains no orbit, it begins as a cloud service, and it is within a
   rounding error of one customer's entire contribution. **DA-21's LIMIT applies: it does not
   reach comparatives drawn on a different perimeter, and no DA class in the register does
   either.**
5. **001's "the AI column is absent from H1 2025" is FALSE as filed** — AI revenue is $737M
   (Q2 2025) and $1,465M (H1 2025). The comparative is recast as-if-combined, not absent.
   Corrected here.
6. **Orbital compute is being out-*chosen*.** The only party that could choose it files that it
   *"expect[s] to allocate a significant amount to our AI segment"*, puts $23,551M of H1 capex
   into AI against $2,226M into Space, and lets flight vehicle hardware book value fall 7.8%
   while servers and networking equipment rise 53.2%.
7. **The AI segment's margin changes sign with the basis** (operating −49.1% vs Segment
   Adjusted EBITDA +44.7%, Q2 2026), and its D&A is 73.6% of segment revenue. **Never quote
   either basis alone.**
8. **The component identity closes 12 of 12 at SPCX**, on an opex definition exclusive of cost
   of revenue, and the segments sum to the consolidated operating loss exactly. SPCX is a clean
   DA-23 control.

---

## 7. Sources

| Ref | Citation | Used for |
|---|---|---|
| [📄 SPCX 10-Q p.11](https://agentii.ai/v/SPCX/sec8/11) | Note 1 — Nature of Business | Segment definition (verbatim); xAI merger 2026-02-02; X merger 2025-03-28; IPO; stock split |
| [📄 SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13) | Note 3 — Revenue | Products/services split; revenue by type and segment; deferred revenue; backlog |
| [📄 SPCX 10-Q p.14](https://agentii.ai/v/SPCX/sec8/14) | Note 5 — PP&E; concentration | Flight vehicle hardware, servers, CIP; interest capitalisation ordering; Customer A/B |
| [📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30) | Note 18 — Segments (Q2 2026) | Segment revenue, cost of revenue, R&D, SG&A, income (loss) from operations; capex |
| [📄 SPCX 10-Q p.31](https://agentii.ai/v/SPCX/sec8/31) | Note 18 — Segments (H1 2026, Q2 2025) | H1 2026 and Q2 2025 segment tables |
| [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35) | Key Business Metrics — Space | Mass to orbit; launches; customer-launch definition; the throughput/revenue relationship |
| [📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36) | Key Business Metrics — Connectivity, AI | Subscribers; ARPU; nameplate compute draw; Starlink launch cost capitalisation; the launch-capacity-allocation statement |
| [📄 SPCX 10-Q p.38](https://agentii.ai/v/SPCX/sec8/38) | Components of Results — AI | AI revenue (advertising, data licensing, API, cloud services); AI cost of revenue; AI R&D |
| [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42) | MD&A — Space; net loss | Space revenue drivers; Space R&D and Starship; net loss changes |
| [📄 SPCX 10-Q p.43](https://agentii.ai/v/SPCX/sec8/43) | MD&A — Connectivity | Consumer/enterprise drivers; subscriber growth vs ARPU decline; CoR composition |
| [📄 SPCX 10-Q p.44](https://agentii.ai/v/SPCX/sec8/44) | MD&A — AI | **+$1,824M / +247.5%; +$1,600M cloud services; +$258M subscriptions; −$59M advertising** |
| [📄 SPCX 10-Q p.46](https://agentii.ai/v/SPCX/sec8/46) | Non-GAAP — Adjusted EBITDA | Adjusted EBITDA definitions; Q2 reconciliations |
| [📄 SPCX 10-Q p.47](https://agentii.ai/v/SPCX/sec8/47) | Non-GAAP — Segment; liquidity | H1 2026 and H1 2025 Segment Adjusted EBITDA; cash; the AI capex flexibility statement |

**Inherited, not re-derived** (consumed from 001/002 per the standing rule): the DA-23
sign-strip census and its detector hierarchy; the component-identity conditionality
(`CostsAndExpenses` inclusive of cost of sales); the F19 statement that SPCX is not evaluable
on DA-01 basis B; the launch-cost-curve contract's F5a/F5b/F5c tiering. **Cross-thesis pillar
references are namespaced: `001:PIL-n`, `002:PIL-n`.**
