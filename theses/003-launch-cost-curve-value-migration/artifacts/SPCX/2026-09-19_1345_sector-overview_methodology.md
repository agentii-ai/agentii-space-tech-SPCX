---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-2
ticker: SPCX
skill: sector-overview
mode: methodology
generated_at: 2026-09-19T13:45:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "8fb208998401"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "the issuer's own segment names are used VERBATIM — Space, Connectivity, AI — and its Space boundary is read as the CUSTOMER boundary, per the filed statement that 'our Space segment revenue only reflects our customer launches and customer activities'; DA-21's recorded LIMIT applies — it governs a boundary drawn inside a FIXED legal perimeter and does not reach a comparative drawn on a DIFFERENT perimeter"
  - da_id: "DA-06"
    chosen_reading: "price versus cost: for Starlink launches there is NO transaction price at all — the issuer files that it recognizes no inter-segment revenue and capitalizes those launch costs into satellites — so the launcher's captive activity has no priced counterpart and its segment margin is a cost-allocation result, not a market result"
  - da_id: "DA-30"
    chosen_reading: "every segment margin is reported on ALL THREE bases the issuer publishes — gross margin, operating margin, and Segment Adjusted EBITDA margin — because the ranking INVERTS between them at this issuer, and no basis is adopted as THE answer"
  - da_id: "DA-23"
    chosen_reading: "every operating income (loss) is taken from the printed page and re-derived in-line as gross profit minus opex on an opex definition EXCLUSIVE of cost of revenue (R&D + SG&A + restructuring + impairment), rather than read from the extracted layer"
  - da_id: "DA-01"
    chosen_reading: "the revenue-to-mass ratios in §5 are quoted on all three constructible bases with the spread reported; SPCX is NOT EVALUABLE on basis B (marginal cost), because no basis-B figure is filed"
evidence_grade: DEMONSTRATED
key_metrics:
  space_segment_gross_margin_pct: 65.80
  connectivity_segment_gross_margin_pct: 51.99
  space_segment_operating_margin_pct: -56.34
  consolidated_gross_margin_pct: 55.28
citations:
  - figure: "SPCX sec8 p.30"
    ticker: SPCX
    citation_id: sec8
    page_no: 30
    url: https://agentii.ai/v/SPCX/sec8/30
    located_via: read_source_pages
  - figure: "SPCX sec8 p.31"
    ticker: SPCX
    citation_id: sec8
    page_no: 31
    url: https://agentii.ai/v/SPCX/sec8/31
    located_via: read_source_pages
  - figure: "SPCX sec8 p.46"
    ticker: SPCX
    citation_id: sec8
    page_no: 46
    url: https://agentii.ai/v/SPCX/sec8/46
    located_via: read_source_pages
  - figure: "SPCX sec8 p.47"
    ticker: SPCX
    citation_id: sec8
    page_no: 47
    url: https://agentii.ai/v/SPCX/sec8/47
    located_via: read_source_pages
  - figure: "SPCX sec8 p.36"
    ticker: SPCX
    citation_id: sec8
    page_no: 36
    url: https://agentii.ai/v/SPCX/sec8/36
    located_via: read_source_pages
  - figure: "SPCX sec8 p.37"
    ticker: SPCX
    citation_id: sec8
    page_no: 37
    url: https://agentii.ai/v/SPCX/sec8/37
    located_via: read_source_pages
  - figure: "SPCX sec8 p.42"
    ticker: SPCX
    citation_id: sec8
    page_no: 42
    url: https://agentii.ai/v/SPCX/sec8/42
    located_via: read_source_pages
  - figure: "SPCX sec8 p.38"
    ticker: SPCX
    citation_id: sec8
    page_no: 38
    url: https://agentii.ai/v/SPCX/sec8/38
    located_via: read_source_pages
  - figure: "SPCX sec8 p.43"
    ticker: SPCX
    citation_id: sec8
    page_no: 43
    url: https://agentii.ai/v/SPCX/sec8/43
    located_via: read_source_pages
  - figure: "SPCX sec8 p.35"
    ticker: SPCX
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "SPCX sec8 p.13"
    ticker: SPCX
    citation_id: sec8
    page_no: 13
    url: https://agentii.ai/v/SPCX/sec8/13
    located_via: read_source_pages
  - figure: "SPCX sec8 p.44"
    ticker: SPCX
    citation_id: sec8
    page_no: 44
    url: https://agentii.ai/v/SPCX/sec8/44
    located_via: read_source_pages
---

# SPCX × sector-overview — the value-chain position map

**Which position in the stack holds the margin?**

**Answer: the position that owns the recurring customer and can capitalise the launcher's
output into an asset base it depreciates over a service life. That is the network operator's
customer-facing layer at SPCX (Connectivity, +38.59% operating margin), and it is the exact
opposite of the launcher's own position (Space, −56.34%).**

**And the same issuer returns the OPPOSITE ranking on the gross basis: Space has the highest
gross margin in the company, 65.80%, above Connectivity's 51.99%.** Both rankings are the
issuer's own, published eight pages apart. **The gap between them is the value migration.**

All figures: SPCX 10-Q for the quarter ended 2026-06-30, filed 2026-08-04. `DEMONSTRATED`
unless marked otherwise. Segment names are the issuer's own (DA-21).

---

## 0. The map, in one table

Segment operating margins, all three segments × four periods, from the filed segment note
([📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30),
[p.31](https://agentii.ai/v/SPCX/sec8/31)):

| Segment (verbatim) | Q2 2025 | Q2 2026 | Δ | H1 2025 | H1 2026 | Δ |
|---|---:|---:|---:|---:|---:|---:|
| **Space** (launch + launch & development) | **−49.46%** | **−56.34%** | −6.9 pp | **−27.25%** | **−76.15%** | **−48.9 pp** |
| **Connectivity** (Starlink services) | **+35.66%** | **+38.59%** | +2.9 pp | **+38.64%** | **+37.68%** | −1.0 pp |
| **AI** (terrestrial AI + X + compute) | **−206.78%** | **−49.08%** | +157.7 pp | **−167.92%** | **−110.27%** | +57.7 pp |

Read at the level of the value-chain question rather than the trend:

- **The launch segment is the only segment with a NEGATIVE operating margin in every period**
  (`DEMONSTRATED`). It is the worst position in the company on this basis in all four periods.
- **The service segment is the only segment with a POSITIVE operating margin in every period**
  (`DEMONSTRATED`), and its margin is stable to within 1.0 pp across the half-year.
- **The AI segment's improvement is a loss narrowing, not a margin**: −206.78% → −49.08% is
  still a loss, and §2 shows the improvement reverses entirely on the issuer's other basis.

**PIL-2's falsifier does not fire at SPCX.** The registered test is
`count_of_universe_issuers_where_launch_segment_operating_margin_exceeds_non_launch_segment_operating_margin`,
`threshold=0`, `op=>`, `source=issuer_segment_disclosure`. The launch segment's operating
margin (−56.34% Q2, −76.15% H1) is **below** every non-launch segment's in both periods.
**PIL-2 HOLDS at SPCX on `DEMONSTRATED` segment data** — and, per F19, this is constructible
rather than doubtful: SPCX files segment revenue *and* segment income (loss) from operations
for three segments × four periods, so *"SPCX does not disclose segment margins"* is false.

---

## 1. The ranking INVERTS between the gross basis and the operating basis

This is the artifact's load-bearing observation, and it is a one-issuer illustration of the
collapse the frontmatter contract forbids (`no_single_basis_collapse`; DA-30).

**Q2 2026, three bases, one issuer:**

| Segment | Gross profit ($M) | **Gross margin** | Operating income (loss) ($M) | **Operating margin** | Segment Adj. EBITDA ($M) | **Adj. EBITDA margin** |
|---|---:|---:|---:|---:|---:|---:|
| **Space** | 633 | **65.80%** ← 1st | (542) | **−56.34%** ← 3rd | (205) | **−21.31%** ← 3rd |
| **Connectivity** | 2,231 | **51.99%** ← 3rd | 1,656 | **+38.59%** ← 1st | 2,597 | **+60.52%** ← 1st |
| **AI** | 1,455 | **56.81%** ← 2nd | (1,257) | **−49.08%** ← 2nd | 1,146 | **+44.75%** ← 2nd |
| **Consolidated** | 4,319 | 55.28% | (143) | −1.83% | 3,538 | +45.28% |

**Space is FIRST on the gross basis and LAST on both profit bases. The swing is 122.1 pp.** No
single-basis statement about "the launch segment's margin" can be true without its basis.

**The relative position deteriorated, and it did so on the profit bases only:**

| Space segment | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 |
|---|---:|---:|---:|---:|
| Gross margin — rank within company | 55.76% (1st) | 65.80% (1st) | 61.08% (1st) | 61.42% (1st) |
| Operating margin — rank | −49.46% (2nd of 3) | **−56.34% (3rd of 3)** | −27.25% (2nd of 3) | **−76.15% (3rd of 3)** |
| Segment Adj. EBITDA margin — rank | −12.47% (2nd of 3) | **−21.31% (3rd of 3)** | **+8.13% (POSITIVE)** | **−35.17% (3rd of 3)** |

**On the issuer's most generous basis — segment income from operations excluding depreciation,
amortisation, share-based compensation, restructuring and impairments — the launch segment was
PROFITABLE in H1 2025 (+$131M on $1,611M of revenue) and is unprofitable in H1 2026
(−$556M on $1,581M).** The gross margin that makes the launcher look like the best business in
the company is intact and improved; every measure below it turned or worsened. Sources:
[📄 SPCX 10-Q p.46](https://agentii.ai/v/SPCX/sec8/46),
[p.47](https://agentii.ai/v/SPCX/sec8/47).

**Why the two bases diverge, on the filed cost definitions** — this is not a modelling choice,
it is where the issuer puts the money:

- **Cost of revenue excludes the internal launches.** *"For launches of our Starlink
  satellites, the Company does not recognize any inter-segment revenue, rather those launch
  costs are **capitalized in satellites** in Property, plant, and equipment, net"*
  ([📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36)). So ~74% of what SPCX flies never
  appears in Space cost of revenue (§3).
- **Cost of revenue excludes the development programme, which sits in R&D.** Space R&D is
  **$1,076M in Q2 2026 — 111.87% of Space segment revenue** — and it *"mainly relate[s] to the
  development, build, and testing of Starship"*, rising 55.3% YoY *"primarily driven by higher
  production and engineering costs of $311 million and higher launch and test costs of $73
  million to support continued development of the Starship vehicle"*
  ([📄 SPCX 10-Q p.37](https://agentii.ai/v/SPCX/sec8/37),
  [p.42](https://agentii.ai/v/SPCX/sec8/42)). **The segment spends more on developing the
  vehicle than the vehicle's segment earns.**
- **Connectivity's cost of revenue CONTAINS the capitalised launch cost** — *"depreciation
  (inclusive of launch, satellite, and ground infrastructure costs)"*
  ([📄 SPCX 10-Q p.38](https://agentii.ai/v/SPCX/sec8/38)) — and depreciation is the single
  largest identified driver of its cost increase: *"higher depreciation of $226 million
  primarily from capitalized launch and satellite costs"*
  ([📄 SPCX 10-Q p.43](https://agentii.ai/v/SPCX/sec8/43)).

**The launcher's output is an input to the operator, and the issuer's accounting says so.**
Space's cost of revenue is flat at $329M (Q2 2026) against $330M (Q2 2025) while total launches
fell 17.4%; the launch cost that matters is on Connectivity's balance sheet as a satellite
asset and in Connectivity's cost of revenue as depreciation.

**⚠️ The causal step is NOT formable.** The *contrast* — launcher negative, captive operator
+38.59% — is `DEMONSTRATED`. The *attribution* of Connectivity's margin to cheap internal
launch is **not**, because Connectivity D&A is a single filed line of $805M (Q2 2026) covering
*launch, satellite, and ground infrastructure* jointly, and the capitalised internal launch
component is not disclosed as a sub-amount. Recorded as `UNRESOLVABLE-FROM-PUBLIC-SOURCES`;
the resolving disclosure is a D&A decomposition. **A correlation consistent with the thesis is
not a measurement of it.**

---

## 2. The AI segment is the second-best position and the second-worst, on the same page

The AI segment is a `captive_integrated`-style position too — it consumes launch capacity the
issuer has said it will allocate to it (§3) — so it belongs on this map. But it cannot be
placed on a single basis:

| AI segment | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 |
|---|---:|---:|---:|---:|
| Revenue ($M) | 737 | 2,561 | 1,465 | 3,379 |
| Income (loss) from operations ($M) | (1,524) | (1,257) | (2,460) | (3,726) |
| Operating margin | −206.78% | **−49.08%** | −167.92% | **−110.27%** |
| Segment Adjusted EBITDA ($M) | (276) | **+1,146** | (387) | **+537** |
| **Adj. EBITDA margin** | −37.45% | **+44.75%** | −26.42% | **+15.89%** |
| Depreciation & amortisation ($M) | 811 | **1,885** | 1,584 | **3,378** |
| D&A as % of segment revenue | 110.04% | **73.60%** | 108.12% | **99.97%** |

Sources: [📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30),
[p.31](https://agentii.ai/v/SPCX/sec8/31), [p.46](https://agentii.ai/v/SPCX/sec8/46),
[p.47](https://agentii.ai/v/SPCX/sec8/47). **The AI segment is a −49.08% operating position and
a +44.75% EBITDA position in the same quarter, and its D&A is 73.60% of its revenue.** The AI
segment's sign is a function of whether its own depreciation is counted. **Reported on both
bases; neither is adopted.**

Two consequences for the map:

1. **The "AI segment is the growth engine" reading depends entirely on the EBITDA basis.** On
   the operating basis it is the second-worst position in the company after Space in Q2 2026.
2. **Its revenue increment is an acquisition artifact and is not evidence of migration** — see
   the secular-trends artifact for this issuer, §4. Recorded here only so the map is not read as
   a value-pool *shift*: within SPCX the shift is `buy vs build`, not `migrate`.

**P10 is respected: this artifact maps the pool and values no constellation.** No listed
issuer reports orbital-compute revenue, so orbital compute is a watch item, not a position.

---

## 3. `operator_class` and the structural reason the launch margin is not comparable

**`operator_class: captive_integrated`** — SPCX both owns the demand and flies the vehicle, and
the filing supports the flag on two independent statements:

| Evidence | Filed basis | Value |
|---|---|---|
| Customer launches, Q2 2026 (the only launches that produce Space revenue) | filed, count | **10** |
| Internal launches, Q2 2026 | filed: Falcon internal 27 + Starship 1 (all Starship classified internal) | **28** |
| **Share of launches producing NO Space revenue** | `DERIVED` (28 / 38) | **73.7%** |
| Customer share, Q2 2026 | filed counts | **26.3%** (from 19.6% in Q2 2025) |
| Customer share, H1 2026 | filed counts | **21.8%** (from 25.0% in H1 2025) |
| Revenue recorded on internal launches | filed policy: none — costs capitalised | **$0** |
| The boundary, verbatim | *"Our Space segment revenue only reflects our customer launches and customer activities."* | — |

Sources: [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35),
[p.36](https://agentii.ai/v/SPCX/sec8/36).

**The DA-06 consequence, stated plainly: for ~74% of SPCX's launches there is no transaction
price at all.** The Space segment's margin is therefore a **cost-allocation result over a
customer-only revenue base**, not a market result over the whole activity. This is the
structural reason a captive launcher's margin is not comparable to an independent launcher's,
and it is why the `captive_flagged` rule exists in the value-pool-map contract. **Any
cross-issuer comparison of "launch segment margin" that puts SPCX beside an independent
launcher is comparing a customer series to an activity series.**

**One consequence for cadence, carried from the sibling artifact:** because the Space boundary
is the customer boundary, **two opposite-signed rates exist on one activity and both are the
filing's** — customer launches +11.1% (Q2) while total launches fell 17.4%; and on the
half-year basis customer launches −19.0% while the customer *share* rose on the quarter and
fell on the half. **Quote either only with its basis** (DA-08, DA-30).

---

## 4. The margin ladder — where SPCX's positions sit in the universe ordering

**Consumed from the 001 universe panorama, not re-derived** (standing rule: 002's and 001's
census figures are consumed, never recomputed).

| Rung | Name | Operating margin | Note |
|---|---|---:|---|
| **Enabling / component** | TER | **32.9%** | best in the ordering |
| | HEI | 25.5% | |
| | CW | 19.3% | |
| | KRMN | 19.1% | |
| | WWD | ~17% | |
| **Prime** | LMT | 12.4% | |
| | RTX | 11.4% | |
| | LHX | 11.1% | |
| | NOC | 10.1% | |
| **Independent network operator** | GSAT | **7.4%** | **worst in the monotone ordering** |
| **Launch / space pure-plays** | RKLB | −24.6% | |
| | PL | −37.1% | |
| | YSS | −44.6% | |
| | LUNR | −56.3% | |
| | FLY | −80.9% | |
| **SPCX, captive operator** | **Connectivity** | **+38.59%** | **the highest operating margin in the universe** |
| **SPCX, launcher** | **Space** | **−56.34%** | |

**Three readings, and the third is the one that matters:**

1. **Component suppliers earn roughly 2× the primes they supply** (TER 32.9% / HEI 25.5% against
   LMT 12.4% / NOC 10.1%). The supplier position is the better position.
2. **The independent network operator is the worst position in the monotone ordering** (GSAT
   7.4%). Owning the demand is not sufficient.
3. **The best and worst network operators in the universe are both network operators, and the
   difference between them is whether the launch is bought at COST or at PRICE.** SPCX
   Connectivity, the captive operator, is **+38.59%**; GSAT, the independent operator that must
   buy launches on the market, is **7.4%**. The launcher between them earns nothing either way
   (SPCX Space **−56.34%**; the independent launch pure-plays −24.6% to −80.9%).

**The map's answer, therefore: the margin does not sit at the launcher and does not sit at the
operator as such. It sits at the position that owns the recurring customer AND owns the launch
that serves it.** A launcher's price is a cost to whoever buys it; a captive operator's launch
is a cost of revenue it pays to itself. Value accrues to the demand-owner only when it also
owns the supply — which is the direct expression of PIL-2 and the reason the pool did not stay
with the launcher.

**⚠️ Scope limit.** The 001 panorama figures are quoted as **inherited**, first-read by 001 and
not re-verified in this artifact. The SPCX figures are `DEMONSTRATED` here. IRDM's clearance was
**withdrawn** by 002 (F8) — its margin must not be used in this ladder until the component check
is re-run, and it is therefore **omitted** above rather than carried as a value.

---

## 5. The basis that must travel with any size claim

Three figures circulate for SPCX's launch share of revenue and **they are three different
things**. Per the inherited correction (F9), none is quotable without its basis:

| Figure | Construction | Basis | Grade |
|---|---:|---|---|
| **8.29%** | Launch Services **$648M** ÷ consolidated **$7,814M** | **Launch-only**, quarter | `DERIVED` (filed cells) |
| **7.82%** | Launch Services **$978M** ÷ consolidated **$12,508M** | **Launch-only**, half | `DERIVED` |
| **12.31%** | Space (Launch Services + Launch & Development) **$962M** ÷ consolidated **$7,814M** | **Space segment**, quarter | `DERIVED` |
| **18.31%** | **$962M** ÷ **$5,253M** (consolidated **ex-AI**) | **Space segment, ex-AI denominator** | `DERIVED` |
| **17.32%** | **$1,581M** ÷ **$9,129M** (consolidated **ex-AI**) | **Space segment, ex-AI denominator**, half | `DERIVED` |
| **65.80%** | **(962 − 329) / 962** | **Space segment GROSS margin — SEGMENT ONLY**; does not reproduce consolidated | `DERIVED` |

Sources: [📄 SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13),
[p.30](https://agentii.ai/v/SPCX/sec8/30). **`12.3%` is three things at once** — it is not
"launch", its denominator is entity-boundary contaminated, and it has been juxtaposed against
half-year growth rates. **For the launch-only statement use `8.29%`.** And `65.80%` reproduces
only on the segment basis: on the consolidated basis SPCX's gross margin is **55.28%**.

**PIL-6 reachability, tested before the threshold (F16/F17).** PIL-6's wrong_if is
`metric=launch_cost_share_of_total_program_cost_at_universe_demand_side_names`,
`threshold=0.10`, `op=>`. The datum at the issuer owning the largest launch business is
**8.29%** — **below the 10% bar**. And 002's NVDA carry-forward puts the demand-side share
*even lower* than 001 recorded (power+thermal only $2.3–4.6M/MW against a reported
$10–40M/MW all-in, with the dominant term being compute hardware and its replacement rate).
**So the falsifier may be unreachable by construction at the demanding names.** The correct
record is **`NON-FORMABLE` at this resolution — never `PASS`** (F16: recording an unformable
quantity as a pass on a technicality is the false clearance 002 exists to prevent).
**UNEXERCISED ≠ CLEAN.**

---

## 6. Component identity, in-line, on the opex definition used

Required by `data_integrity_register_applied`. The identity is `gross profit − opex =
operating_income`, and it is **CONDITIONAL**: `us-gaap:CostsAndExpenses` **includes** cost of
sales, so the inclusive form is false wherever a cost-of-sales line exists. **The opex
definition used here is EXCLUSIVE of cost of revenue: opex = R&D + SG&A + restructuring +
impairment.** `EPS × shares` is **not** an admissible derivation and is not used.

| Segment | Period | gross profit = revenue − cost of revenue | opex (definition above) | gross profit − opex | filed operating income (loss) | closes? |
|---|---|---:|---:|---:|---:|:--:|
| Space | Q2 2026 | 962 − 329 = **633** | 1,076 + 99 + 0 = **1,175** | **(542)** | **(542)** | ✓ |
| Connectivity | Q2 2026 | 4,291 − 2,060 = **2,231** | 294 + 281 = **575** | **1,656** | **1,656** | ✓ |
| AI | Q2 2026 | 2,561 − 1,106 = **1,455** | 2,178 + 532 + 2 = **2,712** | **(1,257)** | **(1,257)** | ✓ |
| Space | Q2 2025 | 746 − 330 = **416** | 693 + 87 + 5 = **785** | **(369)** | **(369)** | ✓ |
| Connectivity | Q2 2025 | 2,588 − 1,401 = **1,187** | 143 + 121 = **264** | **923** | **923** | ✓ |
| AI | Q2 2025 | 737 − 551 = **186** | 1,122 + 398 + 190 = **1,710** | **(1,524)** | **(1,524)** | ✓ |
| Space | H1 2026 | 1,581 − 610 = **971** | 2,006 + 169 = **2,175** | **(1,204)** | **(1,204)** | ✓ |
| Connectivity | H1 2026 | 7,548 − 3,711 = **3,837** | 499 + 494 = **993** | **2,844** | **2,844** | ✓ |
| AI | H1 2026 | 3,379 − 1,562 = **1,817** | 4,557 + 995 − 9 = **5,543** | **(3,726)** | **(3,726)** | ✓ |
| Space | H1 2025 | 1,611 − 627 = **984** | 1,219 + 175 + 29 = **1,423** | **(439)** | **(439)** | ✓ |
| Connectivity | H1 2025 | 5,062 − 2,615 = **2,447** | 266 + 225 = **491** | **1,956** | **1,956** | ✓ |
| AI | H1 2025 | 1,465 − 1,002 = **463** | 2,030 + 699 + 194 = **2,923** | **(2,460)** | **(2,460)** | ✓ |

**12 of 12, zero failures.** Segment rows also sum to the consolidated operating loss exactly
((542) + 1,656 + (1,257) = **(143)**; (1,204) + 2,844 + (3,726) = **(2,086)**), so the segment
table is internally consistent with the consolidated statement — **SPCX is a clean DA-23
control and the margins in this map are not sign-stripped.** Sources:
[📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30),
[p.31](https://agentii.ai/v/SPCX/sec8/31), [p.42](https://agentii.ai/v/SPCX/sec8/42),
[p.43](https://agentii.ai/v/SPCX/sec8/43), [p.44](https://agentii.ai/v/SPCX/sec8/44).

---

## 7. What could NOT be resolved

| # | Open item | Class | Resolving disclosure |
|---|---|---|---|
| 1 | **How much of Connectivity's margin comes from the capitalised internal launch cost.** D&A is one filed line ($805M Q2 2026) covering launch + satellite + ground jointly. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | A decomposition of Connectivity D&A, or the capitalised launch cost as a disclosed sub-amount. **The §1 causal claim is therefore not formable and has not been made.** |
| 2 | **SPCX's cost curve at DA-01 basis B.** No marginal-cost figure is filed, so "the launcher earns nothing *because* the curve passed through" cannot be tested here. | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (a disclosure SPCX does not make) | A filed per-launch cost or a marginal-basis cost table. **This is why §1's divergence is stated as a location, not a mechanism.** |
| 3 | **Any cross-issuer "launch segment margin" including SPCX.** The SPCX series is a customer series; independent launchers' series are activity series. | `UNRESOLVABLE-FROM-PLATFORM` at this resolution | A normative restatement putting every launch segment on one perimeter (the `_cross/value-pool-map.md` primary artifact's `as_restated` field). **The spread must be reported, not netted.** |
| 4 | **IRDM's rung in the ladder.** 002 **withdrew** IRDM's DA-23 clearance (F8) and removed it from the `Clean` row. | `UNRESOLVABLE-FROM-PLATFORM` pending a re-run | The component check re-run on IRDM before its margin is quoted. **Omitted from §4 rather than carried as a value.** |
| 5 | **PIL-6's 10% programme-cost bar at the demanding names.** The datum at SPCX is 8.29%, below the bar. | **`NON-FORMABLE`** — a third outcome, distinct from PASS and FAIL | A demand-side issuer disclosing launch as a share of programme cost. **Recorded as `NON-FORMABLE`, never `PASS`.** |
| 6 | **The AI segment's placement on the map.** Its margin sign depends on the basis (§2), so it has no single rung. | **Resolved as a two-basis entry** | Not an open item — the two-basis entry *is* the correct entry. |

**UNEXERCISED ≠ CLEAN.** Items 1, 2, 3 and 4 are absences, not clearances, and item 5 is a
non-formation, not a pass.

---

## 8. Carry-forwards

1. **The value-chain position map's answer: the margin sits with the position that owns the
   recurring customer AND owns the launch that serves it.** SPCX Connectivity **+38.59%**
   (captive operator) against GSAT **7.4%** (independent operator) inside the same rung, with
   SPCX Space **−56.34%** (launcher) between them. **The launcher earns nothing either way.**
2. **The ranking inverts between the gross basis and the operating basis, inside one issuer.**
   Space is **1st on gross (65.80%)** and **3rd on operating (−56.34%)** — a 122.1 pp swing.
   **No single-basis statement about the launch segment's margin is admissible** (DA-30).
3. **The launch segment's position deteriorated on the profit bases while holding first place
   on the gross basis.** On Segment Adjusted EBITDA — the most generous basis the issuer
   publishes — Space was **+$131M (H1 2025)** and is **−$556M (H1 2026)**. PIL-2's falsifier
   does not fire at SPCX: the launch segment's operating margin is below every non-launch
   segment's in all four periods (`DEMONSTRATED`).
4. **PIL-2 is testable at SPCX, and that was not a given.** F19: SPCX files segment revenue
   *and* segment operating income for three segments × four periods. Assume constructibility;
   do not treat it as doubtful.
5. **`operator_class: captive_integrated`, with the DA-06 consequence filed: ~73.7% of SPCX's
   Q2 2026 launches produce no Space revenue and no transaction price exists for them.** The
   Space margin is a cost allocation over a customer-only base — not comparable to an
   independent launcher's margin without an explicit restatement.
6. **`12.3%` is three things at once; the launch-only figure is `8.29%`; `65.80%` is segment-only
   and consolidated gross margin is `55.28%`.** Every one of these carries its basis or it is a
   §1c violation.
7. **PIL-6's 10% bar is above the datum (8.29%) at the issuer owning the largest launch
   business, and 002 puts the demand-side share lower still.** Test reachability **before** the
   threshold; record **`NON-FORMABLE`, never `PASS`**.
8. **The component identity closes 12 of 12** on an opex definition exclusive of cost of
   revenue, and the segments sum to the consolidated operating loss exactly.

---

## 9. Sources

| Ref | Citation | Used for |
|---|---|---|
| [📄 SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13) | Note 3 — Revenue | Revenue by type and segment; the 8.29% / 12.31% constructions |
| [📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30) | Note 18 — Segments (Q2 2026) | Segment revenue, cost of revenue, R&D, SG&A, operating income; D&A; capex |
| [📄 SPCX 10-Q p.31](https://agentii.ai/v/SPCX/sec8/31) | Note 18 — Segments (H1 2026, Q2 2025) | The H1 2026 and Q2 2025 segment tables |
| [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35) | Key Business Metrics — Space | Launch counts and the customer-launch definition |
| [📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36) | Description of Our Segments — Space | The customer boundary, verbatim; Starlink launch cost capitalisation |
| [📄 SPCX 10-Q p.37](https://agentii.ai/v/SPCX/sec8/37) | Expenses — Space | Space cost of revenue and R&D definitions (Starship development) |
| [📄 SPCX 10-Q p.38](https://agentii.ai/v/SPCX/sec8/38) | Expenses — Connectivity, AI | Connectivity cost of revenue including launch depreciation; AI cost lines |
| [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42) | MD&A — Space | Space revenue drivers; R&D and Starship; the segment MD&A table |
| [📄 SPCX 10-Q p.43](https://agentii.ai/v/SPCX/sec8/43) | MD&A — Connectivity | Depreciation from capitalised launch costs; subscriber/ARPU composition |
| [📄 SPCX 10-Q p.44](https://agentii.ai/v/SPCX/sec8/44) | MD&A — AI | AI segment revenue and cost drivers |
| [📄 SPCX 10-Q p.46](https://agentii.ai/v/SPCX/sec8/46) | Non-GAAP — Adjusted EBITDA | Adjusted EBITDA definitions; Q2 reconciliations |
| [📄 SPCX 10-Q p.47](https://agentii.ai/v/SPCX/sec8/47) | Non-GAAP — Segment; liquidity | H1 2026 / H1 2025 Segment Adjusted EBITDA; cash and IPO proceeds |

**Inherited, not re-derived:** the 001 universe margin ladder (TER, HEI, CW, KRMN, WWD, LMT,
RTX, LHX, NOC, GSAT) and the 001 launch-cohort margins (RKLB, PL, YSS, LUNR, FLY); the F9
`12.3%`/`8.29%` basis correction; the F16/F17 threshold-reachability rules; the F8 IRDM
clearance withdrawal; the F19 statement on SPCX's constructibility and its basis-B absence;
002's NVDA demand-side carry-forward. **Cross-thesis pillar references are namespaced:
`001:PIL-n`, `002:PIL-n`.**
