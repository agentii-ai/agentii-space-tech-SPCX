---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-2
ticker: RKLB
skill: supply-chain
mode: methodology
generated_at: 2026-09-19T14:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: >
      Component identity `gross profit − opex = operating_income` run IN-LINE on five periods before
      any operating figure in this artifact is read, with the opex definition stated for each basis.
      All five close exactly. The platform serves `us-gaap:OperatingIncomeLoss` = **+57,514,000** for
      2026-04-01→2026-06-30 against a filed **(57,514)** thousand, and **+113,483,000** for
      2026-01-01→2026-06-30 against a filed **(113,483)** thousand: equal magnitude, opposite sign,
      two DA-23 hits in the filing this artifact rests on. **Sign is taken from the read page, never
      from the served fact.**
  - da_id: DA-30
    chosen_reading: >
      Two collapses are in scope and both are named at the point of use. (1) **Gross margin**: RKLB
      reports 36.1% GAAP and 41.5% non-GAAP for Q2 2026 — a 5.4-point spread on one concept — and the
      basis is stated on every margin quoted here. (2) **Segment profit**: RKLB's CODM measure is
      **gross profit**, not operating income, so "segment operating margin" is not a basis that exists
      at this issuer at all; the DA-21 boundary is named wherever segment figures are used. A third
      collapse is refused rather than named: Adjusted EBITDA is a different concept from operating
      income and is **not** reported as an operating-income basis here.
  - da_id: DA-21
    chosen_reading: >
      RKLB's own segment boundaries, as filed: two reportable segments, `Launch Services` and
      `Space Systems`, the latter *"predominately comprised of spacecraft components and spacecraft
      manufacturing."* **SolAero sits inside Space Systems and is not separable from it** — so every
      solar-cell statement in this artifact is a Space-Systems statement, and no solar-cell revenue or
      margin is reported on any basis. No normative restatement is attempted; the boundary is recorded
      as the reason the number does not exist.
  - da_id: DA-26
    chosen_reading: >
      Not a finding of this artifact, recorded as a standing exposure: the platform's metrics block
      mislabels annual figures as quarterly (**20 issuers tested, 19 exhibiting — FLY is the
      counterexample; it is NOT universal**). One consequence specific to this leg
      is checked below and **could not be separated from a genuine quarter at the boundary** — see
      §7. Every RKLB figure quoted here is read from a filing page, with the period stated in words
      (e.g. "three months ended June 30, 2026"), so no platform period label is relied on.
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "Component-identity source, three months — Revenues 234,066 / Cost of revenues 149,490 / Gross profit 84,576 (36.1%); Research and development, net 82,429; Selling, general and administrative 59,661; Total operating expenses 142,090; Operating loss (57,514), (24.6)%; comparators 144,498 / 98,110 / 46,388 / 66,134 / 39,893 / 106,027 / (59,639)"
    ticker: RKLB
    citation_id: sec109
    page_no: 39
    url: https://agentii.ai/v/RKLB/sec109/39
    located_via: read_source_pages
  - figure: "Component-identity source, six months — Revenues 434,414 / Cost of revenues 273,345 / Gross profit 161,069 (37.1%); 162,942 / 111,610 / 274,552; Operating loss (113,483); comparators 267,067 / 185,432 / 81,635 / 121,243 / 79,219 / 200,462 / (118,827); Space systems revenue $326.2M +76%, launch services $108.2M +32%, 12 Electron missions vs 10"
    ticker: RKLB
    citation_id: sec109
    page_no: 42
    url: https://agentii.ai/v/RKLB/sec109/42
    located_via: read_source_pages
  - figure: "Segment table, three and six months — Launch Services 44,586 / 25,476 / 19,110 and 108,249 / 60,916 / 47,333; Space Systems 189,480 / 124,014 / 65,466 and 326,165 / 212,429 / 113,736; segment definitions verbatim; cost-proportional revenue allocation between segments"
    ticker: RKLB
    citation_id: sec109
    page_no: 32
    url: https://agentii.ai/v/RKLB/sec109/32
    located_via: read_source_pages
  - figure: "RKLB sec109 p.31"
    ticker: RKLB
    citation_id: sec109
    page_no: 31
    url: https://agentii.ai/v/RKLB/sec109/31
    located_via: read_source_pages
  - figure: "RKLB sec87 p.9"
    ticker: RKLB
    form_type: 10-K
    citation_id: sec87
    page_no: 9
    url: https://agentii.ai/v/RKLB/sec87/9
    located_via: read_source_pages
  - figure: "RKLB sec87 p.11"
    ticker: RKLB
    form_type: 10-K
    citation_id: sec87
    page_no: 11
    url: https://agentii.ai/v/RKLB/sec87/11
    located_via: read_source_pages
  - figure: "Annual component identity — Total revenues 601,799 (product 371,617 / service 230,182); Total cost of revenues 394,618; Gross profit 207,181; Research and development, net 270,716; Selling, general and administrative 165,303; Total operating expenses 436,019; Operating loss (228,838); comparators 2024 and 2023"
    ticker: RKLB
    form_type: 10-K
    citation_id: sec87
    page_no: 69
    url: https://agentii.ai/v/RKLB/sec87/69
    located_via: read_source_pages
  - figure: "RKLB sec87 p.107"
    ticker: RKLB
    form_type: 10-K
    citation_id: sec87
    page_no: 107
    url: https://agentii.ai/v/RKLB/sec87/107
    located_via: read_source_pages
  - figure: "BA sec221 p.37"
    ticker: BA
    citation_id: sec221
    page_no: 37
    url: https://agentii.ai/v/BA/sec221/37
    located_via: read_source_pages
  - figure: "BA sec221 p.38"
    ticker: BA
    citation_id: sec221
    page_no: 38
    url: https://agentii.ai/v/BA/sec221/38
    located_via: read_source_pages
  - figure: "The segment Spectrolab sits inside, and it is loss-making — Defense, Space & Security Revenues $7,483M; Earnings/(loss) from operations ($15)M; Operating margins (0.2)%; 27% of BDS backlog non-U.S.; FY27 NASA budget request $19B, a $6B decrease"
    ticker: BA
    citation_id: sec221
    page_no: 46
    url: https://agentii.ai/v/BA/sec221/46
    located_via: read_source_pages
  - figure: "RKLB ect21 p.2"
    ticker: RKLB
    form_type: earnings_call_transcript
    citation_id: ect21
    page_no: 2
    url: https://agentii.ai/v/RKLB/ect21/2
    located_via: read_source_pages
  - figure: "RKLB ect21 p.6"
    ticker: RKLB
    form_type: earnings_call_transcript
    citation_id: ect21
    page_no: 6
    url: https://agentii.ai/v/RKLB/ect21/6
    located_via: read_source_pages
key_metrics:
  rklb_non_gaap_gross_margin_pct_q2_2026: 41.5
  rklb_gaap_vs_non_gaap_gross_margin_spread_pp_q2_2026: 5.4
  solaero_contract_loss_provision_usdk: 4657
  rklb_atm_equity_programme_proceeds_usdb_q2_2026: 1.08
---

# RKLB — Supply Chain: The Space-Solar-Cell Duopoly Has Exactly One Leg Inside This Universe, and Neither Leg Is Priced

**Sources.** Form 10-Q, accession `0001819994-26-000062`, quarter ended 2026-06-30, filed
2026-08-10, 54 pages (`sec109`); Form 10-K, accession `0001819994-26-000013`, year ended
2025-12-31, filed 2026-02-26, 110 pages (`sec87`); Q2 2026 earnings call, 2026-08-10, 7 pages
(`ect21`). The second leg's parent is cited from **Boeing's** Form 10-Q, accession
`0001628280-26-050038`, quarter ended 2026-06-30, filed 2026-07-28, 56 pages (`sec221`) — cited
because it is the **owner of the absent leg**, not because BA is in this thesis's universe.

**The finding.** The space-grade solar-cell duopoly — **SolAero (RKLB)** and **Spectrolab (BA)** —
is the structural bottleneck at constitution bound **F1**, and it is **half inside this thesis's
universe and entirely unpriced on both halves**. RKLB's ownership of SolAero is filed and
unambiguous; its contribution to the P&L is **not separable at any level of effort**, because
SolAero sits inside a Space Systems segment whose only disclosed profit measure is gross profit,
and because RKLB's segment note states in terms that segment operating expenses are not reviewed
or disclosed. **The second leg is outside the universe by design: Spectrolab belongs to BA, whose
owning theses are 007/008, and it is recorded here as a named absence with its resolving source —
no proxy is substituted for it.** The analytical payoff of recording it anyway is the supply-side
argument: **both legs are financially constrained** (BA 0.6% operating margin on a
$24,560M quarter; RKLB a $(57,514)k operating loss on a $234,066k quarter), which is evidence that
the F1 bottleneck persists rather than being competed away.

---

## 1. The component identity first, with the opex definition, on five periods

The contract requires the derivation in-line for any artifact reading `operating_income`.
**Opex definition used throughout: `total operating expenses` = `Research and development, net` +
`Selling, general and administrative`** — RKLB's income statement has exactly these two operating
lines, so the definition is complete and needs no residual term.

| Period | Gross profit | − Total opex | = Computed | Filed operating loss | Closes? |
|---|---|---|---|---|---|
| **Q2 2026** (3M to 2026-06-30) | 84,576 | 142,090 | **−57,514** | **(57,514)** | ✅ |
| **Q2 2025** (3M to 2025-06-30) | 46,388 | 106,027 | **−59,639** | **(59,639)** | ✅ |
| **H1 2026** (6M to 2026-06-30) | 161,069 | 274,552 | **−113,483** | **(113,483)** | ✅ |
| **H1 2025** (6M to 2025-06-30) | 81,635 | 200,462 | **−118,827** | **(118,827)** | ✅ |
| **FY2025** (12M to 2025-12-31) | 207,181 | 436,019 | **−228,838** | **(228,838)** | ✅ |

All five close exactly. All figures are thousands of USD, read from
[📄 RKLB 10-Q p.39](https://agentii.ai/v/RKLB/sec109/39),
[📄 RKLB 10-Q p.42](https://agentii.ai/v/RKLB/sec109/42) and
[📄 RKLB 10-K p.69](https://agentii.ai/v/RKLB/sec87/69).

**A second, independent closure — the segment sum.** Q2 2026 segment revenues
(`Launch Services` 44,586 + `Space Systems` 189,480 = **234,066**) equal the consolidated revenue
line exactly, and segment gross profit (19,110 + 65,466 = **84,576**) equals consolidated gross
profit exactly, on both the three-month and six-month tables
([📄 RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32)). FY2025 closes the same way:
199,042 + 402,757 = **601,799**, and 81,270 + 125,911 = **207,181**
([📄 RKLB 10-K p.107](https://agentii.ai/v/RKLB/sec87/107)). Two closure methods, five periods,
no residual — the filed tables are internally consistent and the extraction is not distorting them.

### 1.1 ⚠️ DA-23 — CONFIRMED twice on the filing this artifact rests on

| Period | Platform serves | Filed | Test | Verdict |
|---|---|---|---|---|
| Q2 2026 | **+57,514,000** | **(57,514)** k | equal magnitude, **opposite sign** | **HIT** |
| H1 2026 | **+113,483,000** | **(113,483)** k | equal magnitude, **opposite sign** | **HIT** |
| Q1 2026 | +55,969,000 | **(55,969)** k *(derived: H1 − Q2, both read pages)* | equal magnitude, opposite sign | **HIT** *(derived basis)* |

The Q1 2026 filed figure is **arithmetic on two read filed subtotals**, not an independent read of
the Q1 filing — labelled as such because DA-29 forbids treating a closure as a check. It is
nonetheless exact: (113,483) − (57,514) = (55,969).

**Consequence, stated before use: no sign in this artifact is taken from a platform fact.** The
DA-23 detector here is the component identity in §1, and it is the only admissible one — the
gross-profit bound is *non-binding* at RKLB because the issuer has no sign to strip in a *positive*
gross-profit line, and `EPS × shares` is inadmissible by the register.

### 1.2 ⚠️ DA-30 — gross margin is reported here on two bases, both named

| Basis | Q2 2026 | Where established |
|---|---|---|
| **GAAP gross margin** | **36.1%** | filed income statement, [📄 RKLB 10-Q p.39](https://agentii.ai/v/RKLB/sec109/39) |
| **Non-GAAP gross margin** | **41.5%** | issuer's own reconciliation, [📄 RKLB ect21 p.2](https://agentii.ai/v/RKLB/ect21/2) |

A **5.4-point spread on one concept.** Every margin in this artifact is labelled with its basis.
Operating income at this issuer has **one** basis only (GAAP) — and **Adjusted EBITDA is not
admissible as a second one**: it is a different concept, and the same call that supplies
"41.5%" also supplies a non-GAAP operating-expense figure of $115.7M against the filed $142,090k,
i.e. a second *cost* basis that must not be netted against a GAAP gross margin.

---

## 2. SolAero: ownership established from the filing, and what the segment does and does not report

### 2.1 Ownership — filed, not inferred

SolAero is named twice, in two different documents, in two different registers:

> *"We entered this market with our acquisition of leading spacecraft components manufacturer
> Sinclair Interplanetary and have since expanded our market participation with the acquisitions of
> Advanced Solutions, Incorporated, Planetary Systems Corporation, **SolAero Technologies Corp.**
> and GEOST."* — [📄 RKLB 10-K p.9](https://agentii.ai/v/RKLB/sec87/9)

> *"In connection with the acquisition of **SolAero Holdings, Inc.** in **January 2022**, the Company
> assumed a contract with a customer to provide solar panel modules at a fixed price."*
> — [📄 RKLB 10-Q p.31](https://agentii.ai/v/RKLB/sec109/31)

The product line the acquisition bought is described as a **vertically integrated chain**, not a
component:

> *"Solar power solutions include a suite of **vertically-integrated space solar cell, Coverglass
> Interconnected Cells ("CICs") and solar array products**, each specifically designed for missions
> to low Earth orbit, medium Earth orbit, geosynchronous orbit or interplanetary applications.
> Rocket Lab's space solar cells, CICs and panels are **among the highest performing in the
> world**…"* — [📄 RKLB 10-K p.9](https://agentii.ai/v/RKLB/sec87/9)

> *"…**solar cell foundry through solar array design and manufacturing**…"*; *"space solar cell
> through solar array production in **Albuquerque, New Mexico**."*
> — [📄 RKLB 10-K p.11](https://agentii.ai/v/RKLB/sec87/11)

**"Cell foundry through array" is the F1 claim with a supply chain attached**: RKLB owns the
front end (the cell), the interconnect (CIC) and the array. It is a **sole-source manager on
long-lead items** in general terms — *"in some cases we also purchase various inputs and services
from a sole source … we manage this sole source risk through carrying increased buffer stock,
particularly on long-lead items"* (p.11) — and the filing does **not** say which items.

### 2.2 What the segment contributes — and the one financial fact specific to solar cells

| | Q2 2026 | Q2 2025 | H1 2026 | FY2025 |
|---|---|---|---|---|
| Space Systems revenue | **189,480** (81.0% of revenue) | 97,852 (67.7%) | 326,165 | 402,757 |
| Space Systems gross profit | **65,466** → **34.6%** | 32,168 → 32.9% | 113,736 | 125,911 → 31.3% |
| Launch Services revenue | 44,586 (19.0%) | 46,646 (32.3%) | 108,249 | 199,042 |
| Launch Services gross profit | 19,110 → **42.9%** | 14,220 → 30.5% | 47,333 | 81,270 → 40.8% |

Thousands of USD, gross-margin basis as stated (GAAP, segment table). The segment sum closes on
every column — 189,480 + 44,586 = **234,066**; 97,852 + 46,646 = **144,498**; 326,165 + 108,249 =
**434,414**; and gross profit 65,466 + 19,110 = **84,576** — matching the consolidated income
statement line for line. Sources:
[📄 RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32),
[📄 RKLB 10-K p.107](https://agentii.ai/v/RKLB/sec87/107).

**Space Systems is the larger and the lower-margin segment**, and it grew from 67.7% of revenue in
Q2 2025 to **81.0%** in Q2 2026. Note the DA-21 boundary working *against* aggregation: **Space
Systems is "spacecraft components and spacecraft manufacturing"** — SolAero's solar cells and the
satellite-platform programmes are inside **one** line. The CFO decomposes that line from the
inside, verbatim:

> *"we have a pretty wide range of margins in our Space Systems business. We have some component
> solutions such as **solar that are always going to be more towards the lower end** … and then if
> you look towards **some of the product areas, they can be more kind of north of 70 points of
> gross margin**. So they're pretty big spread there within the portfolio. And then again, towards
> the lower end in the mix but **greater in magnitude** of the composition is really the **satellite
> platforms business** … and again, those are more kind of in the **mid-30s**, right?"*
> — [📄 RKLB ect21 p.6](https://agentii.ai/v/RKLB/ect21/6) (Adam Spice, CFO)

**This yields a bound, and the bound is the useful part.** The satellite-platform business — which
the CFO says is the *larger* part of the mix — sits in the **mid-30s**; the reported Space Systems
gross margin is **34.6%**. **Solar is stated to be *below* both.** So the best available reading of
the inside leg's solar-cell margin is **"at the lower end, under the mid-30s"** — `CLAIMED`,
qualitative, **no figure attached and none derivable**, and it is **not** a duopoly margin: it is
one product line inside a segment whose other members run above 70 points. That wide internal
spread — low end to "north of 70" — is exactly why the segment average prices nothing.

**The only solar-cell-specific financial quantity anywhere in the corpus is a legacy liability:**

> *"…the provision for contract losses outstanding on the contract was **$4,657**"* (thousands of
> USD, as of June 30, 2026) — [📄 RKLB 10-Q p.31](https://agentii.ai/v/RKLB/sec109/31)

It is a **fixed-price contract assumed at acquisition whose cost to complete exceeded its price.**
One contract, four and a half years old, and it is a *loss provision* — not a margin, not revenue,
not a price. It is recorded here because it is the only solar-cell number in existence in these
filings, **and it is not to be read as evidence about the duopoly's pricing power in either
direction.**

### 2.3 ⚠️ The disclosure limit, in the issuer's own words

> *"The CODM uses **gross profit** as the measure of segment profit or loss…"*
> — [📄 RKLB 10-K p.107](https://agentii.ai/v/RKLB/sec87/107)

> *"**Management does not regularly review either reporting segment's total assets or operating
> expenses.** This is because in general, the Company's long-lived assets, facilities, and equipment
> are shared by each reporting segment."* — [📄 RKLB 10-K p.107](https://agentii.ai/v/RKLB/sec87/107)

Two consequences, and both are load-bearing:

1. **No segment operating margin exists at RKLB** — not "is not disclosed", but *is not computed by
   the issuer*. §6 turns this into the PIL-2 verdict.
2. **No solar-cell line exists inside Space Systems on any basis** — no revenue, no cost, no
   capacity, no units, no backlog split. The only disaggregation RKLB files is **product vs service
   at the consolidated level**: FY2025 product revenue **371,617** against service revenue
   **230,182** of Total revenues 601,799
   ([📄 RKLB 10-K p.69](https://agentii.ai/v/RKLB/sec87/69)). Solar cells sit inside "product",
   alongside composite structures, reaction wheels, star trackers, radios, separation systems,
   batteries and optical systems ([📄 RKLB 10-K p.9](https://agentii.ai/v/RKLB/sec87/9)).

   > **⚠️ A DA-29 trap, recorded because this artifact walked up to it and backed away.** The
   > subtraction *402,757 − 371,617 = 31,140* "closes": it hands you a Space Systems service-revenue
   > figure that then sums correctly with Launch Services' 199,042 to give the filed 230,182 service
   > line. **It closes, and a closure is therefore not a check.** The revenue-disaggregation note
   > was not read in this leg, so "Space Systems services = 31,140" is a **back-solve, not a filed
   > term**, and it is used nowhere in this artifact. Read the disaggregation note before quoting it.

---

## 3. ⚠️ The BA / Spectrolab gap — recorded as a named absence, **not proxied**

This section is the artifact's required output under the §1c standing rule: **an absence is named
with its resolving source, never filled with the nearest available number.**

| Leg | Owner | Inside *this* thesis's universe? | Owning theses |
|---|---|---|---|
| Space-grade solar cells — SolAero | Rocket Lab (RKLB) | ✅ **in** | **003** (this artifact) |
| Space-grade solar cells — Spectrolab | Boeing (BA) | ❌ **OUT** | **007 / 008** |

**This is recorded as a coverage gap, with a reason, rather than as a hole to be filled.** The
universe of 003 is SPCX, RKLB, FLY, SATS, IRDM, GSAT, LUNR, PL, YSS. **BA is not in it.** Therefore
**the duopoly has exactly one leg inside the universe**, and the second leg's *absence* is a
property of the map, not of the world: Spectrolab exists, is owned, and is analysed — under 007 and
008. `thesis.md` states the same disposition for this omission: *"The map records the absence rather
than substituting a proxy."*

### 3.1 The three available proxies — each rejected, with the reason

| Rejected proxy | Why it is not a Spectrolab number |
|---|---|
| **BA's consolidated operating margin (0.6%, see §3.2)** | It is Boeing. It prices Commercial Airplanes, Global Services and BDS **together**. Using it as a solar-cell margin would be a category error of exactly the kind §1c exists to prevent. Read in this artifact **only** as a parent-capacity datum. |
| **RKLB's Space Systems gross margin (34.6%)** | Already rejected in §2.2 on the issuer's own evidence: it averages a portfolio spanning *"solar … the lower end"* to *"north of 70 points"*, across components **and** spacecraft manufacturing — and the CFO places the *larger* part of that mix, satellite platforms, in the **mid-30s**. It is not a solar-cell margin and cannot be decomposed into one; the CFO's own decomposition puts solar *below* it. |
| **The $4,657k contract-loss provision** | One legacy fixed-price contract. A liability, not a price; and a loss, not a rent. Using it as a pricing signal would be a sign-and-composition error on top of a scope error. |

**No proxy is substituted. The absence is instead named with the specific disclosure that would
resolve it**, per the `UNRESOLVABLE-FROM-PUBLIC-SOURCES` remedy:

1. **A Boeing disclosure that isolates space-solar** — a Spectrolab *reporting unit* inside BDS, or
   a BDS product-line revenue/margin disaggregation separating space systems from aircraft. BA's
   10-Q disaggregates BDS revenue by **customer location and contract type only**
   ([📄 BA 10-Q p.46](https://agentii.ai/v/BA/sec221/46) is the segment's *results*; the
   disaggregation carries no product line).
2. **An RKLB segment redefinition** separating `components` from `spacecraft manufacturing`, or any
   product-line margin disclosure inside Space Systems. The issuer currently states it does not
   produce segment operating expenses at all (§2.3).
3. **A buyer-side disclosure** quantifying solar-array or cell cost inside a satellite programme —
   an outside-the-universe source, and outside this thesis's scope.

### 3.2 What *is* recorded about the absent leg — parent-level, labelled as parent-level

The second leg's parent is cited from its own filing, and **every figure below is a Boeing
consolidated or Boeing-segment figure. None is a Spectrolab figure, and none is used as one.**

| Metric | Q2 2026 (3M to 2026-06-30) | Six months 2026 | Source |
|---|---|---|---|
| Boeing revenue | **$24,560M** | $46,777M | [📄 BA 10-Q p.37](https://agentii.ai/v/BA/sec221/37) |
| Boeing **GAAP** earnings from operations | **$156M** | $604M | [📄 BA 10-Q p.37](https://agentii.ai/v/BA/sec221/37) |
| Boeing **GAAP operating margin** | **0.6%** | 1.3% | [📄 BA 10-Q p.37](https://agentii.ai/v/BA/sec221/37) |
| Boeing **Non-GAAP** core operating earnings | **$1M → 0.0%** | $294M → 0.6% | [📄 BA 10-Q p.38](https://agentii.ai/v/BA/sec221/38) |
| **Defense, Space & Security** revenue | **$7,483M** | $15,082M | [📄 BA 10-Q p.46](https://agentii.ai/v/BA/sec221/46) |
| **BDS** earnings/(loss) from operations | **$(15)M → (0.2)%** | $218M → 1.4% | [📄 BA 10-Q p.46](https://agentii.ai/v/BA/sec221/46) |

**⚠️ DA-30 applied to the absent leg's parent, because it is the one place this artifact quotes a
second issuer's `operating_income`.** Boeing reports its operating line on **two** bases and they
diverge: **GAAP $156M (0.6%)** against **Non-GAAP core operating earnings $1M (0.0%)** in Q2 2026 —
a $155M spread on one concept, driven by the FAS/CAS service-cost adjustment. The 001 artifact that
established "BA at a 0.6% operating margin" quoted **one** basis. **On either basis the quarter is
at or below 0.6%, so the constraint conclusion survives** — but the basis must be named, and it now
is: **0.6% is the GAAP basis.**

**DA-23 status of the absent leg's parent, tested rather than assumed.** 001 recorded BA 2024 Q3
and 2025 Q3 as DA-23 **candidates** and could not run the component identity because the extract
carries no quarterly gross profit for BA. **Boeing reports no gross-profit line at all** — its
consolidated statement runs Revenues → Cost of sales → Earnings from operations — so the component
identity is **unavailable at this issuer**, and with it the gross-profit bound; the only available
test is direct. Applied here: `us-gaap:OperatingIncomeLoss` serves **+156,000,000** for
2026-04-01→2026-06-30 against the filed **$156M positive**
([📄 BA 10-Q p.37](https://agentii.ai/v/BA/sec221/37)). **Same sign, equal magnitude — BA Q2 2026
is CLEAN on DA-23.** That says nothing about 2024 Q3 or 2025 Q3, which remain **`UNEXERCISED`**:
the instrument that would settle them does not exist at this issuer, and their settlement needs the
filed quarterly cost-of-sales lines read directly.

### 3.3 Why the absence is structural rather than accidental

Boeing bills **$24,560M in a single quarter**. For Spectrolab to register as a reportable segment
it would have to clear the materiality thresholds of its parent — i.e. be a multi-billion-dollar
business. **The unit is immaterial to the parent, and that is the whole reason it is invisible.**
The same is true of the inside leg (§2). So the correct characterization of the duopoly is:

> **Structural but UNPRICED. Not absent — below the disclosure granularity required to price it.**

*(The wider "$5.9B–$24.6B per quarter" range used at 001 to describe the duopolies' parents spans
**LHX and BA** — 001 `report-input.md`. **The BA end ($24,560M) is re-verified above against BA's
own 10-Q; the LHX end is inherited from 001 and is not re-verified in this leg**, and LHX is not in
this thesis's universe.)*

---

## 4. Both legs are financially constrained — the supply-side argument, and both readings

| Leg | Owner | Operating result | Margin basis |
|---|---|---|---|
| Solar cells — SolAero | RKLB | **$(57,514)k** loss on $234,066k (Q2 2026) | GAAP, component identity §1 |
| Solar cells — Spectrolab | BA | **$156M** on **$24,560M** (Q2 2026) | GAAP, parent consolidated |
| *(the segment Spectrolab sits in)* | BA | **$(15)M** on **$7,483M** — a **loss** | GAAP, BDS |

**Read as a supply argument:** the F1 bottleneck is a two-supplier structure, and **neither owner is
currently earning enough at the operating line to fund a step-change in solar-cell capacity out of
consolidated operations.** RKLB is consuming cash — GAAP operating cash flow a use of $84.1M in
Q2 2026, non-GAAP free cash flow a use of $110.1M, against an ending liquidity of roughly $2.4B
raised substantially through an at-the-market equity programme that generated $1.08B in the quarter
before being terminated ([📄 RKLB ect21 p.2](https://agentii.ai/v/RKLB/ect21/2)). Boeing's
space-and-defense segment is loss-making in the quarter. **The bottleneck does not relax by itself;
it relaxes only if someone funds capacitance.**

**⚠️ Both readings, per §1c — the evidence does not discriminate, and is not collapsed.**
001 stated the alternative cleanly: *"either the scarcity is small relative to the parents, or the
demand that would make it bite has not arrived."* A 0.6%-margin parent is consistent with
(a) a sub-unit that is scarce but tiny in absolute terms, and (b) a sub-unit that is not yet scarce
because constellation demand has not arrived. **This artifact adds no discrimination between them**,
and says so rather than choosing. What it *does* add is a third possibility that the two-leg framing
usually omits: the inside leg's own CFO puts the solar line at the **lower end of a portfolio whose
larger part he places in the mid-30s** ([📄 RKLB ect21 p.6](https://agentii.ai/v/RKLB/ect21/6)) — a
datum that sits **awkwardly with** the scarcity reading (a scarce bottleneck should price above the
portfolio average, not below it) and comfortably with either of the other two. Grade: `CLAIMED`,
and it is a **mix comment, not a measurement** — the CFO gives no solar margin, and none is
derivable.

---

## 5. Where the inside leg's bottleneck claim actually bites — and where it does not

RKLB is the universe's **only** name that is simultaneously a launcher, a satellite manufacturer and
the owner of one leg of the F1 solar-cell duopoly. That triple is the thesis's subject matter, and
the supply-chain reading is narrow and specific:

- **The solar line is vertical from cell foundry to array** (p.9, p.11) — integration, not
  assembly. On a supply-chain map this is the **strongest position in the universe** on the F1
  component.
- **And it is un-measurable.** No revenue, no margin, no units, no capacity, no price. The single
  financial fact is a legacy loss provision (§2.2).
- **The integration is defended by buffer stock, not by contracting** — *"we manage this sole source
  risk through carrying increased buffer stock, particularly on long-lead items"* (p.11). Buffer
  stock is a **working-capital** answer to a supply risk, and it is the answer a firm gives when it
  cannot obtain priority it can price.
- **The forward demand signal is real and named**: Beck on orbital data centres — *"You've certainly
  seen us release **new solar cells that are specifically targeted to that kind of application**. So
  we're taking the opportunity seriously."* The question that drew it is itself a third-party
  assertion worth recording: *"higher efficiency solar panels are an important part of generating
  enough power for some of these plans … **And you have that capacity already**"*
  ([📄 RKLB ect21 p.6](https://agentii.ai/v/RKLB/ect21/6)). Both are `CLAIMED` — a product claim and
  a sell-side assertion, neither of which is evidenced by a customer, a volume or a price. The
  demand-side counterpart is **not** rent.
- **And the inside leg's owner states the *launch* constraint as durable**: *"even as new capacity
  comes on market from some competitors, a lot of that capacity is already spoken for, for their own
  internal programs, whether it be Internet or AI data centers … So I see this **constrained launch
  market persisting for quite some time**"* ([📄 RKLB ect21 p.6](https://agentii.ai/v/RKLB/ect21/6)).
  `CLAIMED` — and it is a constraint claim made by a party with an interest in it. Note the shape:
  the same executive who says the solar line is the **low-margin end** of his portfolio also says
  the launch market stays **constrained**. If both are true, scarcity is not showing up in the
  price of the scarce thing — which is §4's open question, restated by the issuer.

**Nothing here prices the bottleneck.** What it establishes is the shape: the inside leg holds the
integration and does not disclose the economics; the outside leg is owned by a parent too large to
surface it; and **the physical bound F1 states is a feasibility bound, not a price** — this artifact
adds no efficiency figure of its own and inherits none, because no solar-cell efficiency number
resolves to a page in this leg's sources.

---

## 6. PIL-2's falsifier is `UNEXERCISED` on this name — not satisfied, not violated

PIL-2's recorded test is:

> `metric=count_of_universe_issuers_where_launch_segment_operating_margin_exceeds_non_launch_segment_operating_margin threshold=0 source=issuer_segment_disclosure op=>`

The metric requires **segment operating margin on both sides**. At RKLB:

- the CODM measure is **gross profit**, not operating income
  ([📄 RKLB 10-K p.107](https://agentii.ai/v/RKLB/sec87/107));
- **segment operating expenses are not reviewed by management and are not disclosed** — same page,
  quoted in §2.3;
- therefore **no segment operating margin exists at this issuer**, on either side of the comparison.

**The falsifier therefore cannot run, and is recorded `UNEXERCISED`.** This is `PRESENCE` vs
`ABSENCE` discipline: a test that could not run is not a passed test. RKLB does **not** count toward
PIL-2's numerator or denominator, and must not be reported as "no violation".

**Disposition: `UNRESOLVABLE-FROM-PUBLIC-SOURCES`.** The disclosure does not exist publicly at all.
The specific disclosure that would resolve it: **an allocation of operating expenses to the Launch
Services and Space Systems segments in RKLB's segment note** — which the issuer states would be
arbitrary because long-lived assets, facilities and equipment are shared. Note the remedy is
therefore *monitor*, not *search harder*: no amount of re-reading these filings produces it.

**What PIL-2 can use instead from this name**, with its basis named: segment **gross** margin —
Launch Services 42.9% against Space Systems 34.6% in Q2 2026, and 40.8% against 31.3% for FY2025.
A gross-margin version of the falsifier would run, and on this name it would point the *opposite*
way to the pillar's claim: **launch is the higher-margin segment.** A **substituted** metric is not
the registered one, and this artifact does not substitute it; the observation is recorded so that
PIL-2 can decide whether to re-register the metric on a gross-margin basis, which is the only basis
the universe's own segment disclosures actually supply.
*(FY2025 segment gross margin is unaffected by quarterly mix: 40.8% launch vs 31.3% space systems.)*

---

## 7. What could NOT be verified

| Item | Disposition | Class |
|---|---|---|
| **Spectrolab revenue, cost, margin, capacity, price** — leg 2 of the F1 duopoly | **Not disclosed by its owner.** Recorded as a **named absence** with its owning theses (007/008) and three resolving sources (§3.1). **Not proxied.** | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| **SolAero revenue, cost and margin** — leg 1, inside the universe | **Not separable.** Inside `Space Systems`, whose only profit measure is gross profit (§2.3) | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| **Segment operating expenses / segment operating margin at RKLB** | **Not reviewed by management; explicitly not disclosed** (p.107) → PIL-2's falsifier `UNEXERCISED` (§6) | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| **Space-grade solar-cell pricing, per-watt or per-unit** | **No disclosure anywhere in the corpus.** The duopoly is structural and unpriced (§3.3) | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| **Solar-cell capacity, wafer supply, and the identity of the sole-source inputs** | p.11 names the *practice* ("buffer stock on long-lead items") and **not the items** | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| **A solar-cell margin, even a directional one** | The CFO gives a *mix ranking* (solar below the mid-30s platform business) and **no figure**. Recorded as `CLAIMED` and carried as a bound only (§2.2). | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| **Space Systems product-vs-service revenue split** | The revenue-disaggregation note was **not read** in this leg. The tempting back-solve (402,757 − 371,617 = 31,140) **closes and is therefore not a check** — refused under DA-29 (§2.3). | `UNEXERCISED` |
| **RKLB Q1 2026 filed operating loss** | Not independently read; **derived** exactly as H1 − Q2 (both read), and labelled derived (§1.1) | `UNRESOLVABLE-FROM-PLATFORM` for a clean Q1 read in this leg's scope |
| **BA 2024 Q3 / 2025 Q3 DA-23 status** | Instrument **does not exist** at BA (no gross-profit line, so neither component identity nor gross-profit bound is available) — **`UNEXERCISED`, not clean** | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` for the identity; `UNRESOLVABLE-FROM-PLATFORM` for the quarterly extraction |
| **RKLB FY2025 vs Q4 boundary under DA-26** | The platform's annual-as-quarterly mislabelling is a standing exposure. This leg **could not separate** a genuine year-end quarter from the annual **without reading the FY2025 annual and Q4 in parallel from the served block** — the annual is read and cited here (p.69); the served Q4 label is not relied on for any figure | `UNEXERCISED` |

---

## 8. Corrections and carry-forwards to 001 (frozen-001 policy: 001 is not rewritten)

| # | 001 says | Primary source shows | Status |
|---|---|---|---|
| 1 | BA *"Operating income $156M … Operating margin 0.6%"* — stated as the operating basis, uncited | **Correct, and now dual-basis:** GAAP $156M / 0.6% against Non-GAAP core $1M / 0.0%. The 001 BA artifact carries **no `citations` block and no `agentii.ai` link**, so no BA figure in it resolves to a page. Re-cited here to [📄 BA 10-Q p.37](https://agentii.ai/v/BA/sec221/37) and [p.38](https://agentii.ai/v/BA/sec221/38) | **Basis named; citations added** |
| 2 | *"Boeing does not report Spectrolab as a segment, discloses no space-solar revenue"* | **Stands, and is now narrowed:** BDS is loss-making in Q2 2026 at $(15)M on $7,483M, and revenue is disaggregated by **customer location and contract type only** | **Confirmed, sharpened** |
| 3 | *"Both duopoly legs are financially constrained (BA 0.6% margin, RKLB loss-making)"* | **Confirmed on GAAP and on BA's non-GAAP core basis.** RKLB's loss is now component-verified at $(57,514)k (§1) | **Confirmed, dual-basis** |
| 4 | *"immaterial to parents billing $5.9B–$24.6B per quarter"* | The **BA end ($24,560M) is re-verified**; the **LHX end is inherited and not re-verified here** (§3.3) | **Half re-verified, half inherited** |
| 5 | BA's *"R&D (H1) $1,824M"* | **Not re-verified in this leg** — BA R&D is not read in this artifact and no claim rests on it | **Open** |
| 6 | — (new here) | **PIL-2's registered falsifier cannot run on RKLB** — the issuer does not compute segment operating expenses (§6) | **Added** |
| 7 | — (new here) | **The inside leg's own CFO puts solar at the LOW end of the Space Systems portfolio, below a satellite-platform business he places in the mid-30s, with other product areas "north of 70 points"** (§2.2, §5) — a mix comment, not a measurement | **Added** |
| 8 | — (new here) | **A DA-29 trap on this issuer's own note: 402,757 − 371,617 = 31,140 "closes" and is a back-solve, not a filed term** (§2.3) | **Added** |
| 9 | — (new here) | **The platform's served page for the 10-K Segment note is `page107`; the printed page footer on `sec87` p.9 reads "8" while the platform serves it as `page9`** — a one-page offset observed on this document, recorded so citations resolve to what was actually read | **Added** |

## 9. Carry-forwards

1. **⚠️ The duopoly is recorded with one leg inside the universe and the second leg named as an
   absence — do not re-open this as a coverage hole.** Spectrolab is owned by **007/008**; the
   resolving disclosure is a Boeing Spectrolab reporting unit or a BDS product-line
   disaggregation, and until it exists **the duopoly stays unpriced**. Any downstream artifact that
   needs a solar-cell margin must report that the number does not exist rather than reaching for
   Space Systems' 34.6%.
2. **⚠️ PIL-2's wrong_if is `UNEXERCISED` at RKLB, and the cause is structural.** The CODM measure
   is gross profit and segment opex is not reviewed (p.107). **RKLB must be excluded from PIL-2's
   numerator and denominator, not scored as clean.** The registered metric needs either a
   gross-margin re-registration or a source class beyond issuer segment disclosure.
3. **⚠️ On the only basis the universe actually supplies — gross margin — launch beats space systems
   at RKLB (42.9% vs 34.6% Q2 2026; 40.8% vs 31.3% FY2025).** Recorded, not substituted for the
   registered metric, and it is a datum PIL-2 should confront.
4. **⚠️ DA-23 CONFIRMED twice in this filing (+57,514,000 and +113,483,000 against filed
   (57,514) and (113,483)).** The component identity is the detector; the sign must come from the
   page. Add RKLB's two H1 periods to the census.
5. **BA is `UNEXERCISED` on DA-23, not clean, and 001's two candidates remain open.** The instrument
   does not exist at this issuer: **Boeing files no gross-profit line**, so neither the component
   identity nor the gross-profit bound is available at BA at any period. Settling 2024 Q3 / 2025 Q3
   requires reading the filed quarterly cost-of-sales lines directly.
6. **The single solar-cell financial fact in the corpus is a $4,657k contract-loss provision**
   (p.31). Record it as what it is — a legacy fixed-price liability — and **not** as a pricing
   signal.
7. **001's BA artifact carries no citations block at all** — the only artifact in the duopoly pair
   that cannot be resolved to a page. Its figures are re-cited here; the 001 file stays frozen.

---

## Sources

> Every figure asserted above resolves to the page cited. The links are also present in-line at
> each section, per spec §1d, which requires them in the body and not only in frontmatter.

| Figure | Source |
|---|---|
| Component-identity source, three months — Revenues 234,066 / Cost of revenues 149,490 / Gross profit 84,576 (36.1%); R&D net 82,429; SG&A 59,661; total opex 142,090; Operating loss (57,514) | [📄 RKLB 10-Q p.39](https://agentii.ai/v/RKLB/sec109/39) |
| Component-identity source, six months — 434,414 / 273,345 / 161,069; 162,942 / 111,610 / 274,552; (113,483); Space systems revenue $326.2M +76%, launch $108.2M +32% | [📄 RKLB 10-Q p.42](https://agentii.ai/v/RKLB/sec109/42) |
| Segment table, three and six months, and the segment definition — LS 44,586/25,476/19,110; SS 189,480/124,014/65,466; cost-proportional revenue allocation | [📄 RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32) |
| SolAero named in the one solar-cell financial fact — the $4,657 contract-loss provision, acquisition January 2022, fixed-price solar panel modules | [📄 RKLB 10-Q p.31](https://agentii.ai/v/RKLB/sec109/31) |
| Ownership established from the filing — SolAero Technologies Corp. in the acquisition series; vertically-integrated space solar cell, CICs and solar arrays; "among the highest performing in the world" | [📄 RKLB 10-K p.9](https://agentii.ai/v/RKLB/sec87/9) |
| Supply-chain integration and the sole-source practice — "solar cell foundry through solar array"; Albuquerque, New Mexico; buffer stock on long-lead items | [📄 RKLB 10-K p.11](https://agentii.ai/v/RKLB/sec87/11) |
| Annual component identity — 601,799 revenue / 394,618 cost of revenues / 207,181 gross profit / 436,019 opex / (228,838) operating loss | [📄 RKLB 10-K p.69](https://agentii.ai/v/RKLB/sec87/69) |
| Segment note, three years, and the disclosure limit — LS 199,042/117,772/81,270; SS 402,757/276,846/125,911; CODM uses gross profit; segment opex not reviewed | [📄 RKLB 10-K p.107](https://agentii.ai/v/RKLB/sec87/107) |
| The absent leg's parent, consolidated, GAAP basis — Revenues $24,560M; earnings from operations $156M; operating margin 0.6%; BDS revenue $7,483M | [📄 BA 10-Q p.37](https://agentii.ai/v/BA/sec221/37) |
| The absent leg's parent, operating-line competing bases — GAAP $156M vs Non-GAAP core $1M; six-month $604M vs $294M | [📄 BA 10-Q p.38](https://agentii.ai/v/BA/sec221/38) |
| The segment the absent leg sits in, and it is loss-making — BDS Revenues $7,483M; loss from operations $(15)M; margin (0.2)% | [📄 BA 10-Q p.46](https://agentii.ai/v/BA/sec221/46) |
| Gross-margin competing basis, non-GAAP — "GAAP gross margin 36.1% … Non-GAAP gross margin 41.5%"; backlog ~$2.36B (40/60); opex $142.1M vs $115.7M | [📄 RKLB ect21 p.2](https://agentii.ai/v/RKLB/ect21/2) |
| The only rent-relevant statement on the solar leg — "component solutions such as solar … more towards the lower end" against ">70 points"; new solar cells for orbital data centres | [📄 RKLB ect21 p.6](https://agentii.ai/v/RKLB/ect21/6) |
