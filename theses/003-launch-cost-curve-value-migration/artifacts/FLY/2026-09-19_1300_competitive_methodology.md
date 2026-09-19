---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: cross   # multi-pillar: {PIL-1, PIL-3, PIL-4, PIL-5} — 'cross' is the enum-valid value; check_contract does not validate this field, so a pillar SET passed silently. Stated in the body.
ticker: FLY
skill: competitive
mode: methodology
generated_at: 2026-09-19T13:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "826995c722a4"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-01
    chosen_reading: "the four cost bases (A list price, A-prime realized transaction price, B marginal cost per launch, C fully-loaded cost per kg) are reported separately for Alpha; ALL FOUR ARE ABSENT at FLY and are recorded as a cited absence with their resolving source, never estimated and never collapsed to one basis"
  - da_id: DA-02
    chosen_reading: "no denominator orbit is stated for Alpha; the payload figure is a CLASS LABEL ('1,000 kilograms payload class'), so no $/kg conversion is attempted at FLY and the class label is refused as a denominator"
  - da_id: DA-06
    chosen_reading: "'cost per launch' (cost side) and 'revenue per launch' (price side) are distinct metrics; FLY discloses NEITHER, and the absence is the finding, cited from the filing rather than assumed"
  - da_id: DA-21
    chosen_reading: "Launch vs Spacecraft Solutions is FLY's own revenue disaggregation inside a SINGLE reportable segment; the Q1-2026 segment-reporting refinement recast prior-period segment results, so pre-2026 segment figures sit on the superseded boundary"
  - da_id: DA-23
    chosen_reading: "operating_income is served sign-stripped; the filed cells show four LOSSES in the four quoted periods and the component identity (gross profit - total operating expenses = loss from operations) closes at each, so the filed sign governs"
  - da_id: DA-25
    chosen_reading: "RKLB's per-launch metrics are normalised and do not reconcile to the audited segment table; both legs (revenue-side 22.5%, margin-side 51.6% vs audited 42.9%) are carried from 003 plan.md, not re-derived here"
  - da_id: DA-26
    chosen_reading: "reported PER LAYER: FLY's served-facts layer shows NO annual-figure-under-quarterly-label instance (every label matches its duration), while FLY's metrics-block layer DOES show one. 'Universal' is withdrawn; the layer split is registered"
  - da_id: DA-28
    chosen_reading: "the 11.659x share-count step at the 2025-08-08 IPO (preferred-stock conversion) invalidates share-count detectors; the registered EPS x shares bridge passes in all four periods and therefore does not fire"
  - da_id: DA-30
    chosen_reading: "SciTec's purchase price is reported on THREE bases ($855.6M contractual at closing / $547.0M acquisition-date allocation / $550.3M measurement-period-updated) and all three are reported together; gross margin and revenue are likewise reported on both the as-reported and the pro forma basis"
evidence_grade: DEMONSTRATED
unresolvable: false
citations:
  - figure: "RKLB sec109 p.37"
    ticker: RKLB
    citation_id: sec109
    page_no: 37
    url: https://agentii.ai/v/RKLB/sec109/37
    located_via: read_source_pages
  - figure: "RKLB sec109 p.36"
    ticker: RKLB
    citation_id: sec109
    page_no: 36
    url: https://agentii.ai/v/RKLB/sec109/36
    located_via: read_source_pages
  - figure: "FLY sec21 p.34"
    ticker: FLY
    citation_id: sec21
    page_no: 34
    url: https://agentii.ai/v/FLY/sec21/34
    located_via: read_source_pages
  - figure: "FLY sec21 p.38"
    ticker: FLY
    citation_id: sec21
    page_no: 38
    url: https://agentii.ai/v/FLY/sec21/38
    located_via: read_source_pages
  - figure: "FLY sec21 p.32"
    ticker: FLY
    citation_id: sec21
    page_no: 32
    url: https://agentii.ai/v/FLY/sec21/32
    located_via: read_source_pages
  - figure: "FLY sec21 p.17"
    ticker: FLY
    citation_id: sec21
    page_no: 17
    url: https://agentii.ai/v/FLY/sec21/17
    located_via: read_source_pages
  - figure: "FLY sec16 p.94"
    ticker: FLY
    citation_id: sec16
    page_no: 94
    url: https://agentii.ai/v/FLY/sec16/94
    located_via: read_source_pages
  - figure: "FLY sec21 p.42"
    ticker: FLY
    citation_id: sec21
    page_no: 42
    url: https://agentii.ai/v/FLY/sec21/42
    located_via: read_source_pages
  - figure: "FLY sec16 p.11"
    ticker: FLY
    citation_id: sec16
    page_no: 11
    url: https://agentii.ai/v/FLY/sec16/11
    located_via: read_source_pages
  - figure: "FLY sec21 p.36"
    ticker: FLY
    citation_id: sec21
    page_no: 36
    url: https://agentii.ai/v/FLY/sec21/36
    located_via: read_source_pages
  - figure: "FLY sec16 p.13"
    ticker: FLY
    citation_id: sec16
    page_no: 13
    url: https://agentii.ai/v/FLY/sec16/13
    located_via: read_source_pages
  - figure: "FLY sec5 p.1"
    ticker: FLY
    citation_id: sec5
    page_no: 1
    url: https://agentii.ai/v/FLY/sec5/1
    located_via: read_source_pages
  - figure: "FLY sec21 p.1"
    ticker: FLY
    citation_id: sec21
    page_no: 1
    url: https://agentii.ai/v/FLY/sec21/1
    located_via: read_source_pages
  - figure: "FLY sec16 p.7"
    ticker: FLY
    citation_id: sec16
    page_no: 7
    url: https://agentii.ai/v/FLY/sec16/7
    located_via: read_source_pages
  - figure: "FLY sec16 p.9"
    ticker: FLY
    citation_id: sec16
    page_no: 9
    url: https://agentii.ai/v/FLY/sec16/9
    located_via: read_source_pages
  - figure: "FLY sec16 p.14"
    ticker: FLY
    citation_id: sec16
    page_no: 14
    url: https://agentii.ai/v/FLY/sec16/14
    located_via: read_source_pages
  - figure: "FLY sec16 p.15"
    ticker: FLY
    citation_id: sec16
    page_no: 15
    url: https://agentii.ai/v/FLY/sec16/15
    located_via: read_source_pages
  - figure: "FLY sec21 p.40"
    ticker: FLY
    citation_id: sec21
    page_no: 40
    url: https://agentii.ai/v/FLY/sec21/40
    located_via: read_source_pages
  - figure: "FLY sec21 p.10"
    ticker: FLY
    citation_id: sec21
    page_no: 10
    url: https://agentii.ai/v/FLY/sec21/10
    located_via: read_source_pages
  - figure: "FLY sec16 p.82"
    ticker: FLY
    citation_id: sec16
    page_no: 82
    url: https://agentii.ai/v/FLY/sec16/82
    located_via: read_source_pages
  - figure: "FLY sec5 p.2"
    ticker: FLY
    citation_id: sec5
    page_no: 2
    url: https://agentii.ai/v/FLY/sec5/2
    located_via: read_source_pages
  - figure: "FLY sec16 p.90"
    ticker: FLY
    citation_id: sec16
    page_no: 90
    url: https://agentii.ai/v/FLY/sec16/90
    located_via: read_source_pages
  - figure: "FLY sec21 p.13"
    ticker: FLY
    citation_id: sec21
    page_no: 13
    url: https://agentii.ai/v/FLY/sec21/13
    located_via: read_source_pages
  - figure: "FLY sec16 p.95"
    ticker: FLY
    citation_id: sec16
    page_no: 95
    url: https://agentii.ai/v/FLY/sec16/95
    located_via: read_source_pages
  - figure: "FLY sec16 p.96"
    ticker: FLY
    citation_id: sec16
    page_no: 96
    url: https://agentii.ai/v/FLY/sec16/96
    located_via: read_source_pages
  - figure: "FLY sec21 p.6"
    ticker: FLY
    citation_id: sec21
    page_no: 6
    url: https://agentii.ai/v/FLY/sec21/6
    located_via: read_source_pages
key_metrics:
  key_metrics_section_pages: 0
  payload_class_label_width_x: 6.0
  multi_launch_backlog_thousands_as_of_2026_06_30: 403070
  total_backlog_thousands_as_of_2026_06_30: 1468081
---

# FLY — Competitive Methodology

**Disclosure-uniqueness control.** FLY's analytical value in this thesis is what it does **not**
disclose. Everything below is read from the filings, not from the metrics block.

**Modes covered in this one file**: `direct-competitor-identification-and-analysis` (§4) ·
`market-share-dynamics-analysis` (§5) · `market-share-evolution-and-competitive-benchmarking` (§6).

**Sources read**: FLY Form 10-Q, accession `0001860160-26-000023`, filed 2026-08-11 (`sec21`,
54 pp.) · FLY Form 10-K, accession `0001193125-26-116309`, filed 2026-03-20 (`sec16`, 137 pp.) ·
FLY Form 8-K, accession `0001193125-25-267129`, filed 2025-11-05 (`sec5`, 6 pp.) · RKLB Form 10-Q,
accession `0001819994-26-000062`, filed 2026-08-10 (`sec109`).

**Conventions**: `K` = US$ thousand, `M` = US$ million, both as filed; all quantities are US
dollars unless stated. `X x` denotes a dimensionless multiple. Grade key: **DEMONSTRATED** (a filed
figure or arithmetic directly on filed cells) / **CLAIMED** (an issuer or third-party assertion) /
**MODELED** (our derivation).

---

## 0. The central finding

**FLY discloses NEITHER `cost per launch` NOR `revenue per launch`.** Not in the 10-K, not in the
10-Q, on any basis, in any period. The negative is filed-cited, not assumed (§1), and it is a
property of the company rather than an analyst's oversight (§2).

Three consequences, and they are the reason this artifact exists:

1. **RKLB's per-launch disclosure is a FINDING, not a CONVENTION.** Basis B — the only
   DEMONSTRATED marginal launch cost in the universe — is disclosed by **exactly one issuer**
   ([📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37)). **PIL-1's demonstrated anchor is
   single-source** and stays single-source: no competitor of RKLB's discloses a comparable metric,
   and the one control that could have widened it (FLY) cannot.
2. **Basis B is therefore not a curve.** One point is not a curve, and one issuer is not a
   convention. `CLAIMED`-versus-`DEMONSTRATED` (PIL-3) is decided at FLY the same way it is decided
   at RKLB's other peers: **nothing to measure.**
3. **FLY cannot be placed on the cost curve at all** — not because the arithmetic is hard, but
   because neither coordinate is disclosed and the one payload figure that exists is a **class
   label**, which is not a denominator (§3). Recorded as **ABSENT**, with the resolving source
   named, never estimated.

---

## 1. The cited absence, from the filing

### 1.1 The census

Page-level keyword census, run against both documents. The platform's keyword search returns
*candidate pages* (it matches the page's extracted text and outline, not an exact phrase), so every
returned page was read rather than counted:

| Keyword | FLY 10-K (`sec16`, 137 pp.) | FLY 10-Q (`sec21`, 54 pp.) |
|---|---|---|
| `key metrics` | **0 pages** | **0 pages** |
| `cost per launch` | 7 candidate pages | 4 candidate pages |
| `revenue per launch` | 4 candidate pages | 3 candidate pages |

**Every candidate page was read.** 10-K pages 11, 13, 82, 90, 94, 95, 96 and 10-Q pages 10, 13, 15,
16, 17. **On none of them does either metric appear with a value, a definition, or a
reconciliation.** What those pages actually contain is Launch revenue-recognition policy, pro forma
data, deferred revenue, property and equipment, and contract balances — the word "launch" is
ubiquitous in the filings; the *per-launch metric* is absent from all of them.

**The load-bearing cell is the zero on `key metrics`.** The disclosure FLY lacks is not a number
buried somewhere; it is a **section** — and the section that would contain it does not exist in
either document.

### 1.2 The contrast object — the same disclosure, at the only issuer that makes it

RKLB's Q2 2026 10-Q carries the section heading FLY does not have, and under it the metric FLY does
not produce:

> **"Key Metrics and Select Financial Data — We monitor the following key financial and operational
> metrics that assist us in evaluating our business, measuring our performance, identifying trends
> and making strategic decisions."** — [📄 RKLB 10-Q p.36](https://agentii.ai/v/RKLB/sec109/36)

> **"Revenue and Cost Per Launch … For the three months ended June 30, 2026 and 2025, revenue per
> launch was $9.1 million and $7.9 million, respectively. Meanwhile, cost per launch for the three
> months ended June 30, 2026 and 2025 was $4.4 million and $5.0 million, respectively. … For the
> six months ended June 30, 2026 and 2025, revenue per launch was $9.2 million and $7.5 million …
> cost per launch … was $4.9 million and $5.3 million, respectively."** — [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37)

| Metric | RKLB Q2 2026 | RKLB Q2 2025 | FLY Q2 2026 | Grade |
|---|---:|---:|---:|---|
| `revenue per launch` | $9.1M | $7.9M | **not disclosed** | DEMONSTRATED (RKLB) / ABSENT (FLY) |
| `cost per launch` | $4.4M | $5.0M | **not disclosed** | DEMONSTRATED (RKLB) / ABSENT (FLY) |
| `revenue per launch`, H1 | $9.2M | $7.5M | **not disclosed** | DEMONSTRATED (RKLB) / ABSENT (FLY) |
| `cost per launch`, H1 | $4.9M | $5.3M | **not disclosed** | DEMONSTRATED (RKLB) / ABSENT (FLY) |
| launch count, Q2 | 6 Electron (2 HASTE) | 5 Electron | **not disclosed** | DEMONSTRATED (RKLB) / ABSENT (FLY) |

Source for the RKLB row: [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37). RKLB also
discloses build-rate and cadence in the same block — approximately 14 Electron built in 2024, 24 in
2025, 11 in H1 2026; 16 launched in 2024, 21 in 2025, 12 in H1 2026; **87 Electron launches through
2026-06-30** — [📄 RKLB 10-Q p.36](https://agentii.ai/v/RKLB/sec109/36),
[📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37).

**The two disclosure regimes are not variants of one another.** RKLB publishes a per-launch cost
series, a per-launch revenue series, a build rate and a launch count. FLY publishes **none of the
four**, and the difference is not one of emphasis: it is the presence or absence of a section.

### 1.3 What the absence does to PIL-1 and PIL-5

- **PIL-1**: basis B is DEMONSTRATED for exactly one vehicle-and-issuer pair (Electron/RKLB). The
  control that could have falsified "single-source" — a second launcher publishing a per-launch
  cost — **does not exist at FLY**, and FLY is the closest listed comparable (a dedicated small
  launcher, post-IPO, with a live launch program).
- **PIL-5**: RKLB's per-launch disclosure is durable on the **cost side** (a definition, a series,
  both periods, both the point-in-time and over-time recognition methods named) and unreconciled on
  the **revenue side** (DA-25, §7). FLY's absence removes the second data point that would let
  either leg be tested against a competitor. **The revenue-side normalisation cannot be
  cross-checked at any other issuer**, because no other issuer publishes the metric.

---

## 2. Why the disclosure is thin — four structural reasons, and it is permanent

Each of the four is a citation, not an inference. Together they establish the absence as a
**property of the company**, which is what makes it usable as a control.

### (a) There is no "Key Business Metrics" section — and there is no MD&A metrics block

`key metrics` returns **0 pages** in the 10-K and **0 pages** in the 10-Q. FLY's MD&A goes from
"Overview" to "Components of Results of Operations" with no metrics section between
([📄 FLY 10-Q p.34](https://agentii.ai/v/FLY/sec21/34),
[📄 FLY 10-Q p.38](https://agentii.ai/v/FLY/sec21/38)). RKLB's goes "Key Factors Affecting Our
Performance" → **"Key Metrics and Select Financial Data"** → the metric
([📄 RKLB 10-Q p.36](https://agentii.ai/v/RKLB/sec109/36)). **The container is missing, so the
metric has nowhere to live.**

### (b) A single reportable segment — and the CODM's metric is net loss, so no launch P&L exists

> *"The Company has determined that it operates in one operating segment and as a result, manages
> its operations and allocates resources as a single operating segment. The Company's Chief
> Operating Decision Maker ('CODM') is its Chief Executive Officer, who reviews financial
> information presented on a consolidated basis for purposes of making operating decisions,
> assessing financial performance, and allocating resources. **The CODM uses net income or loss to
> evaluate the return on assets** and to determine investment opportunities…"* — [📄 FLY 10-Q p.32](https://agentii.ai/v/FLY/sec21/32)

> *"We operate as a single reportable segment and serve this critical domain through our
> differentiated and scalable platforms of Launch and Spacecraft Solutions."* — [📄 FLY 10-Q p.34](https://agentii.ai/v/FLY/sec21/34)

This is stronger than "segment margin not disclosed". **A Launch cost, a Launch gross profit and a
Launch margin are not produced anywhere in FLY's internal or external reporting** — the CODM's own
performance metric is consolidated net loss. The only Launch-level figures FLY produces at all are
**revenue** and **deferred revenue** ([📄 FLY 10-Q p.17](https://agentii.ai/v/FLY/sec21/17):
Launch deferred revenue $72,371K at 2026-06-30 vs $77,843K at 2025-12-31).

**DA-21 note**: FLY recast its segment presentation *in the current year* — *"In the first quarter
of fiscal 2026, the Company refined its segment reporting to better reflect how the CODM evaluates
segment performance. Prior period segment results have been recast to conform to the current period
presentation."* ([📄 FLY 10-Q p.32](https://agentii.ai/v/FLY/sec21/32)). Any pre-2026
Launch/Spacecraft split is on the **superseded boundary** and must not be mixed with post-recast
figures without saying which boundary is in use.

### (c) "Launch revenue" is definitionally mixed — it is not launch services

> *"**Launch revenue includes revenues** from contracts with commercial and government entities to
> provide launch and integration services … **We also enter into contracts with our customers to
> provide engineering services, including the development of launch sites and related components,
> and to develop and provide licenses to intellectual property.** In these cases, our service
> obligation is satisfied over time…"* — [📄 FLY 10-Q p.38](https://agentii.ai/v/FLY/sec21/38)

The same definition appears in the 10-K ([📄 FLY 10-K p.94](https://agentii.ai/v/FLY/sec16/94)):
the *launch* performance obligation is *"the initiation of the launch"*, recognized **point in
time**; engineering services and IP licences are recognized **over time**; and where a contract
holds multiple performance obligations, standalone selling prices are set by *"cost plus margin or
market prices for similar goods and services"*. **A per-launch metric derived from this line would
divide mixed revenue by an undisclosed count** — a DA-30 collapse of two bases (launch-services
revenue vs the whole Launch reporting line) onto one number.

### (d) No launch count is disclosed — only contracted capacity

FLY names **one** flight in the entire H1 2026 discussion: *"our successful Alpha Flight 7 launch"*
([📄 FLY 10-Q p.42](https://agentii.ai/v/FLY/sec21/42)). No count is given for any period.

What FLY *does* disclose is **contracted capacity**, on the demand side:

| Disclosed | Value | Grade | Source |
|---|---|---|---|
| Lockheed Martin multi-launch agreement | up to **25 missions** over five years | CLAIMED | [📄 FLY 10-K p.11](https://agentii.ai/v/FLY/sec16/11) |
| L3Harris multi-launch agreement | up to **20 Alpha launches**, 2–4/yr from 2027 to 2031 | CLAIMED | [📄 FLY 10-K p.11](https://agentii.ai/v/FLY/sec16/11) |
| Multi-launch agreement backlog | $403,070K at 2026-06-30 vs $344,800K at 2025-06-30 | DEMONSTRATED | [📄 FLY 10-Q p.36](https://agentii.ai/v/FLY/sec21/36) |
| Total backlog | $1,468,081K at 2026-06-30 vs $1,351,054K at 2025-06-30 | DEMONSTRATED | [📄 FLY 10-Q p.36](https://agentii.ai/v/FLY/sec21/36) |
| Remaining performance obligations | $563.7M at 2026-06-30 (different definition — see §5.4) | DEMONSTRATED | [📄 FLY 10-Q p.17](https://agentii.ai/v/FLY/sec21/17) |
| Production rate | *"expanding our processes to manufacture one Alpha launch vehicle per month"* | CLAIMED | [📄 FLY 10-K p.13](https://agentii.ai/v/FLY/sec16/13) |

**FLY discloses the forward denominator and never the realized one.** It will tell an investor how
many launches it has *contracted*; it will not tell them how many it *flew* — the one input a
per-launch metric needs. Even the mission *name* ("Alpha Flight 7") implies a count without
disclosing one; taking the number in a mission name as a launch count is MODELED, not
DEMONSTRATED, and is not used here.

### The structural explanation is voluntary and permanent, not transitional

FLY is an **emerging growth company** — the 10-K cover and the 8-K cover both carry *"Emerging
growth company ☒"* ([📄 FLY 8-K p.1](https://agentii.ai/v/FLY/sec5/1)) — **and has not elected
to forgo the extended transition period** (*"If an emerging growth company, indicate by check mark
if the registrant has elected not to use the extended transition period … ☐"*, same page). Two
points make this an explanation rather than an excuse:

1. **FLY is NOT a smaller reporting company.** The 10-Q cover shows Non-accelerated filer ☒ and
   **Smaller reporting company ☐** ([📄 FLY 10-Q p.1](https://agentii.ai/v/FLY/sec21/1)) — so
   **scaled-disclosure relief cannot explain the missing metrics**. EGC status is doing the work,
   and EGC status is a **disclosure-election regime the issuer controls**.
2. **The EGC exemption is not a Q4-reporting-window artefact**: it lapses on a fixed clock, but the
   *per-launch metric is not a scaled-disclosure item under any regime* — it is voluntary
   disclosure. FLY's status is therefore a **permanent structural explanation for an
   absence that would persist even at full disclosure**: nothing in Regulation S-K requires a
   per-launch cost. **The correct disposition is not "FLY will tell us later" — it is "FLY has
   chosen not to, and no rule compels it."**

---

## 3. Alpha on the cost curve — A ✗ / A′ ✗ / B ✗ / C ✗, and why a CLASS is not a DENOMINATOR

### 3.1 The basis table (this is the artifact's contribution to PIL-1)

| DA-01 basis | What it requires | At Alpha / FLY | Grade of the disposition |
|---|---|---|---|
| **A** — list/published price per launch | a published price for a named vehicle | **✗ ABSENT** — no price is published anywhere in the 10-K or 10-Q | ABSENT (cited) |
| **A′** — realized transaction price per launch | contract value ÷ launches, or an equivalent | **✗ ABSENT** — no per-launch revenue, no launch count; Launch revenue is mixed (§2c) | ABSENT (cited) |
| **B** — marginal cost per launch | cost of the launch vehicle + period costs ÷ launches | **✗ ABSENT** — no per-launch cost; no launch cost line; no segment P&L | ABSENT (cited) |
| **C** — fully-loaded cost per kg | (cost) ÷ (payload kg to a stated orbit) | **✗ ABSENT on BOTH coordinates** — the numerator is absent and the denominator is a class label | ABSENT (cited) |

**All four bases are absent.** Alpha is the only dedicated launch vehicle in the universe that
cannot be placed at *any* point on the curve — not even a contested one.

**Resolving source, for each**: bases A/A′ require a published price or a per-launch revenue metric
(the RKLB form: [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37)); basis B requires a
per-launch cost metric; basis C requires a **payload mass and a target orbit for a named mission**.
None of the four exists at FLY. **Disposition: `UNRESOLVABLE-FROM-PUBLIC-SOURCES` for all four —
not a modelling gap.**

### 3.2 The payload class label — quoted, and refused as a denominator

FLY's five filed payload statements, verbatim:

| # | Cell | Source |
|---|---|---|
| 1 | *"the first and only U.S. commercial company with a rocket ready to fulfill critical space missions in the **1,000 kilograms payload class**"* | [📄 FLY 10-K p.7](https://agentii.ai/v/FLY/sec16/7) |
| 2 | *"We are the only U.S. company with a liquid-powered orbital launch vehicle in the **1,000-kilogram payload class**."* | [📄 FLY 10-Q p.34](https://agentii.ai/v/FLY/sec21/34) |
| 3 | *"Alpha is the only provider of small size launch that has achieved orbit and addresses a critical gap in the market in the **1,000 kilograms category**."* | [📄 FLY 10-K p.9](https://agentii.ai/v/FLY/sec16/9) |
| 4 | market span: *"the global market right-sized toward satellites **between 200 kilograms to 1,200 kilograms**"* (BryceTech, 2025); *"64% of the satellites launched since 2015 fit within this range"* | [📄 FLY 10-K p.9](https://agentii.ai/v/FLY/sec16/9) |
| 5 | Eclipse: *"greater payload capacity and customizable five meter payload fairing"* — **also unquantified** | [📄 FLY 10-K p.9](https://agentii.ai/v/FLY/sec16/9) |

**Diagnosis.** Statements 1–3 are **class labels**. They carry **no mass**, **no orbit**, and **no
configuration** — not for Alpha, not for Eclipse. The only mass range FLY does cite is the
**market's**, at **200–1,200 kg — a 6× span** (1,200 ÷ 200 = 6.0×; DEMONSTRATED arithmetic on the
filed range, which is itself a CLAIMED third-party figure).

**Why a class is not a denominator.** A $/kg figure is `(cost) ÷ (mass delivered to a stated
orbit)`. "1,000 kg class" is a **boundary label applied to a vehicle**, not the mass of a payload
on a mission, and it is stated without an orbit (DA-02). Two failure modes follow, and both are
fatal to the ratio rather than merely noisy:

- **Denominator sensitivity**: if the class label (1,000 kg) is used but the typical delivered
  payload sits nearer the band's floor (200 kg), the resulting $/kg is understated by **5.0×**
  (1,000 ÷ 200). This is a **MODELED** sensitivity on a CLAIMED range — but it is an order of
  magnitude, not a rounding.
- **Orbit sensitivity (DA-02)**: with no orbit stated, the same payload mass can move the true
  $/kg by a further multiple (the register's GTO-vs-LEO factor is ~3×), and the direction is
  unknowable from the filing.

**Disposition: Alpha's basis C is ABSENT, not estimated.** The correct output is the **absence with
its resolving source** (a named mission's payload mass and target orbit). Estimating it from the
class label would produce a number that is *unfalsifiable and wrong in a known direction* — the
precise defect class this thesis exists to prevent.

---

## 4. Mode 1 — `direct-competitor-identification-and-analysis`

### 4.1 FLY's own competitive disclosure names ZERO competitors

The 10-K carries a **"Competition"** section. It contains a **taxonomy of categories** and **no
names**:

> *"We primarily compete with businesses in the following categories: companies providing dedicated
> small and medium launch vehicles to deliver payloads to various preferred orbits; companies
> providing spacecraft such as orbital vehicles and related solutions; companies providing lander
> solutions, **including our competitors on the NASA CLPS contracts**; and, companies providing
> mission data processing software applications and enterprise transformation of mission ground
> systems for national security."* — [📄 FLY 10-K p.14](https://agentii.ai/v/FLY/sec16/14),
> [📄 FLY 10-K p.15](https://agentii.ai/v/FLY/sec16/15)

> *"The principal competitive factors in our market include: flight heritage and reliability;
> delivery schedule; ability to customize products to meet specific needs of the customer;
> performance and technical features; **price**; and customer experience. We believe that we
> compete favorably across these factors."* — [📄 FLY 10-K p.15](https://agentii.ai/v/FLY/sec16/15)

**Two findings here.** (i) The competitor set is **unnamed** — even the CLPS competitors are
referred to as a class. The only named third parties in the 10-K are **partners and customers**:
Lockheed Martin (a multi-launch agreement), **Northrop Grumman** (exclusive Eclipse partnership,
supported by a $50M equity investment), L3Harris (multi-launch agreement), USSF, SDA, NRO and NASA
([📄 FLY 10-K p.11](https://agentii.ai/v/FLY/sec16/11)). **FLY's competitive set cannot be
constructed from FLY's filing.** (ii) **"Price" is declared a principal competitive factor while
no price is disclosed** — the same asymmetry as §1, restated by the issuer itself.

### 4.2 FLY's self-positioning is CLAIMED and, as stated, unfalsifiable

| Claim | Grade | Why it is not testable |
|---|---|---|
| *"the only U.S. commercial company with a rocket ready to fulfill critical space missions in the 1,000 kilograms payload class"* | **CLAIMED** | the class is self-defined; no rival's payload is stated on a common basis in the filing; "ready to fulfill" has no filed threshold |
| *"the only U.S. launch vehicle in its class"* | **CLAIMED** | the cited addressable band is **6× wide** (§3.2), so the class boundary is the elastic term in the claim |
| *"micro launch players lack the capacity to carry multiple payloads, leading to unfavorable unit economics"* | **CLAIMED** | a unit-economics assertion about unnamed rivals with **no figure attached** |

**A competitive claim whose defining term is authored by the claimant and unquantified is a
positioning statement, not a finding.** This is the same shape as the thesis's central
`CLAIMED`-vs-`DEMONSTRATED` problem, at the competitive layer rather than the cost layer.

### 4.3 The competitor set, constructed from the outside

| Competitor | Basis of comparability | Data available on it | Grade |
|---|---|---|---|
| **RKLB / Electron** | dedicated small launch, the only vehicle in the universe with a **DEMONSTRATED** marginal cost | `cost per launch` $4.4M (Q2 2026); 6 launches (Q2 2026); 12 (H1 2026) | DEMONSTRATED ([📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37)) |
| **SPCX / Falcon 9** | partially reusable medium-lift; competes for the same dedicated/rideshare demand | basis A is denominator-failed; the matched-pair band is $5,567–7,448/kg (inherited correction) | CLAIMED/derived elsewhere — **not re-derived here** |
| **Unnamed "micro launch players"** | named as a category by FLY | nothing filed | CLAIMED, no figure |
| **Unnamed "small and medium launch" peers** | FLY's own category | nothing filed | CLAIMED, no figure |

**A three-vehicle comparison cannot be built on a common basis.** Electron has a per-launch cost
and a launch count; Falcon 9 has neither a usable denominator nor a count in the compared metric;
Alpha has **no coordinate at all** (§3.1). The competitive comparison therefore reduces to
**FLY's absence versus RKLB's disclosure** — which is the finding, not a gap in it.

---

## 5. Mode 2 — `market-share-dynamics-analysis`

### 5.1 FLY's launch series — the only launch trajectory FLY discloses

All cells below are filed; ratios are arithmetic on filed cells (DEMONSTRATED).

| Period | Launch revenue | Total revenue | Launch share of own revenue |
|---|---:|---:|---:|
| FY2023 | $33,017K | $55,235K | **59.8%** |
| FY2024 | $22,631K | $60,792K | **37.2%** |
| FY2025 | $28,620K | $159,855K | **17.9%** |
| H1 2025 | $11,519K | $71,404K | 16.1% |
| H1 2026 | $22,652K | $198,562K | 11.4% |
| Q2 2025 | $6,349K | $15,549K | 40.8% |
| Q2 2026 | $9,400K | $117,683K | **8.0%** |

Sources: FY cells [📄 FLY 10-K p.94](https://agentii.ai/v/FLY/sec16/94); H1 and Q2 cells
[📄 FLY 10-Q p.42](https://agentii.ai/v/FLY/sec21/42) and
[📄 FLY 10-Q p.40](https://agentii.ai/v/FLY/sec21/40).

**The dynamics, on the as-reported basis**: launch revenue **fell** from FY2023 to FY2024
($33,017K → $22,631K, −31.5%), partly recovered by FY2025 ($28,620K, still **−13.3% below**
FY2023), and grew in H1 2026 ($22,652K vs $11,519K, +97%). Over the same two years total revenue
compounded at **+70.1%/yr** (($159,855K ÷ $55,235K)^(1/2) − 1) while launch revenue compounded at
**−6.9%/yr**. **Launch fell from 59.8% of FLY's revenue to 8.0%.** On the as-reported basis,
launch is converging on a *rounding error* inside FLY's own P&L.

**DA-30 — the second basis.** FLY also files a **pro forma** revenue basis that puts the SciTec and
Spaceflight acquisitions in for the whole of each year: FY2025 pro forma revenue **$328,240K** vs
as-reported **$159,855K** ([📄 FLY 10-K p.94](https://agentii.ai/v/FLY/sec16/94)). On the pro
forma basis, FY2025 launch share is **8.7%** ($28,620K ÷ $328,240K), not 17.9%. **Both bases are
reported here and neither is quoted alone.**

### 5.2 The growth is ACQUIRED — the same defect class as SPCX's AI recast

Q2 2026 vs Q2 2025, filed cells and the issuer's own attribution:

| Line | Q2 2026 | Q2 2025 | Change | FLY's stated driver |
|---|---:|---:|---:|---|
| Revenue | $117,683K | $15,549K | +$102,134K (**+657%**) | — |
| **Spacecraft Solutions** | $108,283K | $9,200K | **+$99,083K (+1,077%)** | *"driven by the inclusion of SciTec, which was acquired in the fourth quarter of 2025"* |
| **Launch** | $9,400K | $6,349K | **+$3,051K (+48%)** | *"primarily due to our progress on **engineering services contracts for the development of launch facilities**"* |

Source: [📄 FLY 10-Q p.40](https://agentii.ai/v/FLY/sec21/40). SciTec closed **2025-10-31**
([📄 FLY 10-Q p.10](https://agentii.ai/v/FLY/sec21/10),
[📄 FLY 10-K p.82](https://agentii.ai/v/FLY/sec16/82)); the Q2 2025 comparative ends
**2025-06-30**. **The acquisition closed after the entire comparative window, so 100% of SciTec's
Q2 2026 revenue is absent from the Q2 2025 figure by construction** (DEMONSTRATED arithmetic on
filed dates). Spacecraft Solutions supplies **97.0%** of the total quarterly revenue increase
($99,083K ÷ $102,134K).

**And the Launch increase is not launch services.** FLY attributes +$3,051K to *engineering
services contracts for launch facilities* — over-time services revenue that shares the Launch line
by §2(c), not revenue from flying rockets. H1 2026's Launch driver list is the same shape:
*"our successful Alpha Flight 7 launch, **increased progress on Eclipse design and manufacturing**,
and **engineering services contracts for the development of launch facilities**"*
([📄 FLY 10-Q p.42](https://agentii.ai/v/FLY/sec21/42)). **Two of the three named drivers are
development and services, not launch.**

**This is the same defect class as SPCX's AI-segment recast**: growth that exists because an
**entity or a scope was acquired or redefined**, presented in a comparison whose prior period
cannot contain it. `+$102,134K` is not evidence that FLY's launch franchise grew.

### 5.3 Science of the denominator — what is paid, on three bases (DA-30)

FLY reports the SciTec purchase price **three ways**, and all three are filed:

| Basis | Figure | Composition | Source |
|---|---:|---|---|
| **Contractual, at closing** | **≈$855.6M** | $300M cash + **11,111,116 shares** valued at **$50.00/share** ≈ $555.6M | [📄 FLY 8-K p.2](https://agentii.ai/v/FLY/sec5/2) |
| **Acquisition-date allocation (ASC 805)** | **$547.0M** | $277.4M cash **net of cash acquired** + $269.6M common stock | [📄 FLY 10-K p.90](https://agentii.ai/v/FLY/sec16/90) |
| **Measurement-period-updated** | **$550.3M** | the $547.0M basis + a **$3.3M working-capital adjustment** | [📄 FLY 10-Q p.13](https://agentii.ai/v/FLY/sec21/13) |

Both internal reconciliations close with **all their terms named in the source** — $300M + $555.6M
= $855.6M ✓; $547.0M + $3.3M = $550.3M ✓ — so neither is a DA-29 back-solve. **The cross-basis
bridge is a back-solve, and is labelled as one**: $855.6M − $547.0M = **$308.6M**, decomposable
only into (i) **$286.0M** of share revaluation ($555.6M − $269.6M) and (ii) **$22.6M** of cash
acquired ($300.0M − $277.4M). **Neither figure appears anywhere in any source.** Grade: **MODELED**
— my derivation, admissible as an explanation of the gap and **not admissible as a filed figure**.
The implied acquisition-date value per share, $269.6M ÷ 11.111116M shares = **$24.26/share**, is
likewise **MODELED** against the **agreed $50.00/share** (DEMONSTRATED).

**Consequence.** A reader taking the closing headline as the price of the acquisition **overstates
the recorded purchase price by 1.564×** ($855.6M ÷ $547.0M). The stock component was worth
**0.485×** at closing what the contract said ($269.6M ÷ $555.6M). Any statement of the form "FLY
paid $855.6M for SciTec" — or "$547.0M", or "$550.3M" — is a statement **on one basis**, and per
DA-30, this artifact reports all three together.

### 5.4 What the market-share analysis cannot do

**FLY's launch market share is undefined.** Share requires a numerator (FLY launches) and a
denominator (market launches). FLY discloses **neither**, and no issuer in the universe publishes
an industry launch total. The three near-misses are all traps:

1. **Backlog is not share.** $1,468,081K of total backlog and $403,070K of multi-launch-agreement
   backlog ([📄 FLY 10-Q p.36](https://agentii.ai/v/FLY/sec21/36)) are **contracted demand**,
   denominated in dollars, not missions flown.
2. **RPO is not backlog.** FLY's remaining performance obligations were **$563.7M at 2026-06-30**
   with ~42% expected within 12 months ([📄 FLY 10-Q p.17](https://agentii.ai/v/FLY/sec21/17))
   versus **$684.9M at 2025-12-31** ([📄 FLY 10-K p.95](https://agentii.ai/v/FLY/sec16/95)) —
   a **declining** balance, while *backlog* rose. The two are **different definitions** and must
   never be summed or substituted.
3. **Deferred revenue is not share either** — and the Launch component **fell** from $77,843K
   (2025-12-31) to $72,371K (2026-06-30) ([📄 FLY 10-Q p.17](https://agentii.ai/v/FLY/sec21/17),
   [📄 FLY 10-K p.96](https://agentii.ai/v/FLY/sec16/96)). The Launch contract-liability balance
   is **not growing** while Launch *revenue* is, which is consistent with §5.2 (the growth is
   over-time services, not the pre-launch deposit base FLY collects ~90% of contract value from —
   [📄 FLY 10-K p.13](https://agentii.ai/v/FLY/sec16/13)). Grade: cells DEMONSTRATED;
   the consistency inference **MODELED**.

---

## 6. Mode 3 — `market-share-evolution-and-competitive-benchmarking`

### 6.1 The count denominator — who discloses it

| Operator | Launch count disclosed? | Q2 2026 | H1 2026 | FY2025 |
|---|---|---:|---:|---:|
| **SPCX (Falcon)** | yes | 37 launches, of which **27 internal** (inherited from thesis 001; **not re-derived here**) | — | — |
| **RKLB (Electron)** | yes | **6** (2 HASTE suborbital) | **12** | **21** (16 in FY2024) |
| **FLY (Alpha)** | **NO** | **not disclosed** | **not disclosed** — only *"Alpha Flight 7"* is named | **not disclosed** |

RKLB cells: [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37). FLY negative:
§1.1, §2(d). SPCX row carried by reference from
`theses/001-technology-baseline/artifacts/RKLB/2026-09-18_2359_competitive_methodology.md` §3 —
**UNEXERCISED in this artifact**.

**Market share is not constructible for FLY, and for reasons that are issuer-specific rather than
industry-wide**: RKLB discloses counts (so RKLB's *own* trajectory is measurable), FLY does not (so
FLY's is not), and no one publishes the market total. **FLY is the only dedicated launch provider
in the universe for which neither numerator nor denominator exists.**

### 6.2 Margin and intensity benchmarking — Q2 2026

| Issuer | Revenue | Gross margin | R&D / revenue | Operating result |
|---|---:|---:|---:|---:|
| **RKLB** | $234.1M | **36.1%** | 35.2% | $(57.5)M loss |
| **YSS** | — | 24.0% | 6.2% | $(41.3)M loss |
| **FLY** | **$117.7M** | **20.3%** | **60.8%** | **$(95.2)M loss** |

FLY row computed here from filed cells (DEMONSTRATED): gross profit $23,875K ÷ revenue $117,683K =
**20.29% → 20.3%**; R&D $71,532K ÷ $117,683K = **60.78% → 60.8%**; loss from operations $(95,197)K
— [📄 FLY 10-Q p.40](https://agentii.ai/v/FLY/sec21/40),
[📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6). RKLB and YSS rows are **carried by
reference** from `theses/001-technology-baseline/artifacts/FLY/2026-09-18_1239_unit-economics_methodology.md`
§4 and are **not re-derived here**; RKLB's gross margin cross-checks on filed cells at 36.1%
($84,576K ÷ $234,066K, [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37), primary
`us-gaap:GrossProfit` Q2 2026 = $84,576,000).

**FLY combines the lowest gross margin, the highest R&D intensity and the largest operating loss.**
Two further shapes matter:

- **FLY's gross margin FELL while revenue rose 657%**: 25.7% in Q2 2025 ($3,995K ÷ $15,549K) →
  **20.3%** in Q2 2026, **−5.4 points** (DEMONSTRATED). The acquired/integrated business is
  **dilutive to margin**, not accretive.
- **R&D intensity is not comparable across the three on the same denominator**: FLY's 60.8% is
  60.8% of *revenue*; RKLB's 35.2% is 35.2% of **twice the revenue base**. In dollars, FLY spent
  $71,532K on R&D against $117,683K of revenue; RKLB spent ~$82M against $234.1M. The **absolute**
  research budgets are within ~15% of each other; the **revenue bases** are not.

### 6.3 Operator-versus-launcher margin positioning (P2, P3, P5)

The question this section answers: **is the launch margin observable at any of the three, and does
an operator's margin differ from a launcher's?**

| Issuer | Consolidated gross margin | Launch-level margin | Why |
|---|---:|---|---|
| **FLY** | 20.3% (DEMONSTRATED) | **NONE EXISTS** | single reportable segment; CODM metric is net loss; Launch line mixes services and IP (§2b, §2c) |
| **RKLB** | 36.1% (DEMONSTRATED) | observable on **two bases that do not reconcile**: disclosed per-launch figures imply **51.6%**, the audited segment table gives **42.9%** | DA-25 — carried from `theses/003-launch-cost-curve-value-migration/plan.md` §"Phase 4" (revenue-side gap 22.5%: $9.1M × 6 = $54,600K vs segment revenue $44,586K; margin-side gap 51.6% vs 42.9%). **UNEXERCISED here — not re-derived.** |
| **SPCX** | — | **boundary is the CUSTOMER boundary**: ~74% of launches produce no Space-segment revenue by design (inherited from theses 001/002) | the integrated operator's launch "revenue" is largely internal |

**Conclusion for P2/P3/P5** — and it is the honest form of the answer:

1. **The launcher's margin is measured once, in one place, on a basis that does not reconcile to
   the audited table** (RKLB, DA-25). Everywhere else it is unavailable: FLY does not produce it,
   SPCX's segment boundary excludes most of its launches.
2. **The operator-versus-launcher margin comparison cannot be made on the launch dimension at
   all.** The only margin comparison available across these issuers is **consolidated**, where the
   number prices **business mix, acquisition accounting and R&D intensity** — not the launch cost
   curve. FLY at 20.3% and RKLB at 36.1% differ because FLY carries an 11.77× larger Spacecraft
   Solutions line and a 60.8% R&D load, not because Alpha's marginal launch cost is known to differ
   from Electron's. **Alpha's marginal launch cost is not known at all.**
3. **The direction of P2 is supported, but not from launch margins.** The highest consolidated
   gross margin in the universe sits at a **demand-owning services operator, not a launcher** — PL
   at **53.5%**, while still running a **−37%** operating margin (carried from
   `theses/003-launch-cost-curve-value-migration/entities.md`; **UNEXERCISED here — not
   re-derived**). That is consistent with value pooling at the demand owner, and it is
   **not** a launch-margin datum. **P2 cannot be tested on launch margin; it can only be tested on
   mix and ownership boundary — which is exactly what §5.2 measured.**

### 6.4 Competitive benchmarking, stated as bounds only

| Comparison | Result | Grade |
|---|---|---|
| FLY launch revenue vs RKLB launch revenue | **not comparable** — FLY's Launch line includes engineering services, launch-site development and IP licensing; RKLB's per-launch metric is a normalisation over launch contract performance obligations | ABSENT |
| FLY launch margin vs RKLB launch margin | **not constructible** — one side does not exist, the other is internally unreconciled | ABSENT |
| FLY gross margin vs RKLB gross margin | 20.3% vs 36.1% — **−15.8 points** | DEMONSTRATED |
| FLY R&D intensity vs RKLB R&D intensity | 60.8% vs 35.2% of revenue — **+25.6 points** | DEMONSTRATED (FLY side), by-reference (RKLB side) |
| FLY backlog vs RKLB backlog | $1,468.1M vs $2,355.9M at 2026-06-30 — ratio **0.62×** | DEMONSTRATED (FLY [📄 10-Q p.36](https://agentii.ai/v/FLY/sec21/36)); RKLB figure **carried from thesis 001, UNEXERCISED here** |

---

## 7. DA register — what FLY confirms, what FLY falsifies, and the layer that splits the verdict

### 7.1 DA-23 — CONFIRMED, 4 of 4 quoted periods; 15 of 15 served facts are positive

| Period | Gross profit | − Total operating expenses | = Loss from operations (filed) | Extract serves |
|---|---:|---:|---:|---:|
| Q2 2026 | $23,875K | $119,072K | **$(95,197)K** | **+$95,197K** |
| Q2 2025 | $3,995K | $58,345K | **$(54,350)K** | **+$54,350K** |
| H1 2026 | $41,336K | $232,201K | **$(190,865)K** | **+$190,865K** |
| H1 2025 | $6,215K | $119,109K | **$(112,894)K** | **+$112,894K** |

**Opex definition used**: total operating expenses **as filed** = research and development +
selling, general and administrative ([📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6),
[📄 FLY 10-Q p.40](https://agentii.ai/v/FLY/sec21/40)). **Cost of sales is EXCLUDED and must be**
— it sits above gross profit. `us-gaap:CostsAndExpenses` **includes** cost of sales, so the identity
would be false with that definition; it is not the definition used here. All four identities close
exactly.

`search_xbrl_facts` returns **17 `OperatingIncomeLoss` rows / 15 distinct periods (FY2023–H1 2026),
ALL 15 POSITIVE.** The served series is **internally additive on the wrong sign**: Q1 2026
$95,668K + Q2 2026 $95,197K = $190,865K, exactly the served H1 2026 value. **A consumer who sums
quarters obtains the right magnitude with the wrong sign at every level.**

### 7.2 DA-26 — **NOT CONFIRMED at FLY. This is the counterexample that falsifies universality.**

**Every served FLY `fiscal_period` label matches its fact's duration.** Zero mismatches. Supporting
controls: `fiscal_period=Q3` returns exactly the two genuine three-month Q3 facts; the FY2025 fact
carries a twelve-month duration from the 10-K.

**The register's universality claim is WITHDRAWN**: the census is **20 issuers tested, 19
exhibiting** — not "19 of 19", not "universal". **Do not report DA-26 as universal.**

⚠️ **One control that is NOT a discriminator** (recorded so it is not misreported): the
`fiscal_period=Q4` filter returns **zero** FLY rows. That is not evidence of a clean layer — the
same filter returns zero at **VRT**, a register-confirmed DA-26 exhibitor. The Q4 bucket has no
population; the empty return tests nothing.

⚠️ **Scope qualification — the verdict is LAYER-SCOPED, and the other layer does exhibit it.**

The falsification above is a statement about the **served-facts layer** (what
`search_xbrl_facts` returns with `fiscal_period` labels). FLY's **metrics block** — a different
layer of the same platform — carries a textbook DA-26 instance:

| `get_company_financials` row | Served value | What it actually is |
|---|---:|---|
| **2025 Q4** revenue | **$159,855,000** | **FY2025 ANNUAL** revenue ([📄 FLY 10-K p.94](https://agentii.ai/v/FLY/sec16/94)) |
| **2025 Q4** operating_income | **$260,688,000** | an annual figure, and **sign-stripped** (DA-23) |

**Proof that the row is not a quarter, from filed cells only**: FY2025 total revenue $159,855K
([📄 FLY 10-K p.94](https://agentii.ai/v/FLY/sec16/94)) **exceeds** H1 2025 total revenue
$71,404K ([📄 FLY 10-Q p.42](https://agentii.ai/v/FLY/sec21/42)). Revenue is non-negative at
every level, so Q4 2025 revenue alone ≤ $159,855K − $71,404K = **$88,451K < $159,855K**.
**Therefore the served 2025-Q4 value cannot be a quarter.** (Implied Q4 2025 = $57,673K, giving a
row **2.77× too large** — **MODELED**, because it borrows the served Q3 2025 row as a genuine
quarter.)

**Disposition**: the register entry should record **DA-26 per layer** — *exhibited in the
metrics-block layer at FLY; not exhibited in the served-facts layer at FLY* — and the census should
be described as **layer-scoped**. The exit condition for re-opening is a **per-layer re-census** of
the 20 issuers, not a re-run of the mixed census.

### 7.3 DA-28 — CONFIRMED, and the registered detector does NOT fire

| Measure | Q2 2026 | Q2 2025 | Step |
|---|---:|---:|---:|
| Weighted-average shares, basic and diluted | **161,784K** | **13,877K** | **11.659×** |
| Net loss | $(92,319)K | $(63,778)K | **+44.8% worse** |
| Net loss available to common stockholders | $(92,319)K | $(80,263)K | **+15.0% worse** |
| Basic and diluted EPS | **$(0.57)** | **$(5.78)** | **−90.1% "improved"** |

Source: [📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6),
[📄 FLY 10-Q p.32](https://agentii.ai/v/FLY/sec21/32). The step comes from the **preferred-stock
conversion at the 2025-08-08 IPO** — visible in the dilutive-securities table, where every
convertible preferred class is **zero at 2026-06-30** against 2,023K–20,851K shares per class at
2025-06-30, total exclusions falling 73,523K → 18,375K
([📄 FLY 10-Q p.32](https://agentii.ai/v/FLY/sec21/32)); the IPO itself was 22.2M shares at
$45.00 for $998.6M gross ([📄 FLY 10-K p.82](https://agentii.ai/v/FLY/sec16/82)).

**DA-30 — both harm bases are reported above.** The **44.8%** deterioration is against
**consolidated net loss**; against **net loss available to common stockholders** it is **15.0%**,
because the 2025 comparative carried $16,485K of preferred dividend accretion that the 2026 period
does not ([📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6): $5,363K + $10,856K + $266K).
**Quoting one basis alone would misstate the harm by a factor of three.**

**⚠️ The registered EPS × shares bridge passes in all four periods** (computed from the filed cells
above; used **only** as the registered detector, **not** as a sign test — `EPS × shares` is not an
admissible sign test):

| Period | \|EPS × shares\| | Net loss available to common | Gap |
|---|---:|---:|---:|
| Q2 2026 | $92,217K | $92,319K | 0.11% |
| Q2 2025 | $80,209K | $80,263K | 0.07% |
| H1 2026 | $189,639K | $188,995K | 0.34% |
| H1 2025 | $152,571K | $152,544K | 0.02% |

**All four gaps ≤ 0.34% — the detector does not fire.** **A detector that passes on an 11.659×
share-count discontinuity is not a detector**, and the harm is precisely where the bridge is blind:
net loss deteriorated **44.8%** while EPS "improved" **90.1%**. 002 §3.3 further records
`search_earnings_calendar` propagating the artefact as `eps_yoy_change_pct: 0.9208` (**inherited;
not re-derived here**).

---

## 8. What could not be resolved

| # | Item | Class | Resolving source |
|---|---|---|---|
| 1 | **Alpha's payload mass per mission** — no mass is stated for any flight | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a named mission's delivered payload mass |
| 2 | **Alpha's denominator orbit (DA-02)** — no LEO/SSO/GTO reference for any Alpha mission | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a target orbit per mission |
| 3 | **FLY's launch count / realized cadence** — only contracted capacity is disclosed | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a launch-count metric, or a dated mission log |
| 4 | **FLY's Launch gross margin** — not produced internally (CODM metric is net loss) | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a Launch reportable segment P&L, or a cost-of-sales split |
| 5 | **SciTec's standalone revenue** — the pro forma increment ($328,240K − $159,855K = $168,385K FY2025, DEMONSTRATED arithmetic) covers **SciTec *and* Spaceflight** and cannot be attributed | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | an ASC 805 acquiree-revenue disclosure (absent; no such note in the 10-K or 10-Q) |
| 6 | **The DA-26 layer census** — FLY splits the verdict across two platform layers | `UNRESOLVABLE-FROM-PLATFORM` | a per-layer re-census of the 20 tested issuers |
| 7 | **RKLB Launch-segment 42.9% margin and the DA-25 gap percentages** — carried from 003 `plan.md`, not re-derived | **UNEXERCISED** in this artifact | the RKLB segment tables themselves, read directly |
| 8 | **SPCX launch counts / internal share, RKLB backlog $2,355.9M, PL 53.5% margin, YSS margin row** — carried from theses 001/002/003 | **UNEXERCISED** in this artifact | those artifacts' own filings |

**Resolved during this pass** (recorded so it is not carried forward as a mystery): the SciTec
purchase price is **not** an unexplained discrepancy. Three filed bases exist and both internal
reconciliations close with all terms named (§5.3). The cross-basis bridge is a **MODELED**
back-solve and is labelled as such.

---

## 9. Carry-forwards

1. **RKLB's per-launch disclosure is unique, and now proven so against a control.** FLY — a listed
   dedicated small launcher, post-IPO, with a live launch program — discloses **neither** `cost per
   launch` **nor** `revenue per launch`, has **no "Key Business Metrics" section** (`key metrics` →
   0 pages in both the 10-K and the 10-Q), and **does not produce a launch margin internally**.
   **PIL-1's demonstrated basis-B anchor is single-source and will stay single-source.**
2. **Alpha's basis table is A ✗ / A′ ✗ / B ✗ / C ✗.** Alpha cannot be placed on the curve at any
   point. **PIL-3's `CLAIMED`-not-`DEMONSTRATED` verdict is decided at FLY by absence, not by
   contest.**
3. **A payload CLASS is not a payload DENOMINATOR.** "1,000 kilograms payload class" carries no
   mass, no orbit and no configuration, against a cited addressable span of **200–1,200 kg (6×)**;
   converting on the class label can misstate $/kg by **5.0×** before the orbit is considered.
   **Record as ABSENT with its resolving source. Never estimate.**
4. **DA-23 CONFIRMED at FLY, 4 of 4 quoted periods**; 15 of 15 served `OperatingIncomeLoss` facts
   positive across FY2023–H1 2026; the series is internally additive, so summing quarters gives the
   **right magnitude and the wrong sign at every level**.
5. **DA-26 IS NOT CONFIRMED AT FLY — and the register's universality claim is withdrawn.**
   *20 issuers tested, 19 exhibiting.* **Do not report DA-26 as universal.** The verdict is
   **layer-scoped**: FLY's served-facts layer is clean, its **metrics-block layer is not** (§7.2).
6. **DA-28 CONFIRMED at FLY on an 11.659× share step from the IPO preferred conversion — and the
   registered EPS × shares bridge DOES NOT FIRE** (≤0.34% in all four periods). **Harm: net loss
   −44.8% while EPS "improved" 90.1%** — and on the second basis (net loss available to common
   stockholders) the harm is **−15.0%**, a 3× difference between two filed bases of the same event.
   **A detector that passes on an 11.7× discontinuity is not a detector.**
7. **FLY's revenue growth is ACQUIRED, and its Launch growth is not launch services.** SciTec closed
   **2025-10-31**, after the entire Q2 2025 comparative, so **100%** of its current-period revenue
   is incremental by construction; Spacecraft Solutions supplies **97.0%** of the $102,134K
   quarterly increase; and the Launch line's +$3,051K is attributed to **engineering services
   contracts for launch facilities**. **Same defect class as SPCX's AI recast.**
8. **Operator-versus-launcher margin positioning cannot be established on the launch dimension.**
   FLY has no launch margin; RKLB's launch margin exists on **two unreconciled bases** (51.6%
   implied vs **42.9%** audited, DA-25); SPCX's boundary is the **customer** boundary. The only
   available comparison is consolidated (FLY **20.3%** vs RKLB **36.1%**), which prices mix,
   acquisition accounting and R&D intensity — **not the cost curve**.
9. **⚠️ DA-30 at FLY is not hypothetical — one acquisition, three filed prices** ($855.6M / $547.0M
   / $550.3M), and one event with two harm magnitudes (44.8% / 15.0%). **Quote the basis or do not
   quote the number.**
10. **Two headline-grade statements in FLY's filing are CLAIMED and unfalsifiable as drafted**:
    *"the only U.S. launch vehicle in its class"* (a self-authored class against a **6×**-wide
    band) and *"we expect our cost structure and unit economics to meaningfully improve"*
    (quantified nowhere — [📄 FLY 10-K p.13](https://agentii.ai/v/FLY/sec16/13)). **Neither may
    be cited as evidence of anything.**
