---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: cross
ticker: SPCX
skill: ratio-analysis
mode: methodology
generated_at: 2026-09-19T14:45:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "2d27c7f751fa"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: "The platform serves a filed negative as a positive of identical magnitude. SPCX's metrics block returns operating_income +143,000,000 and net_income +541,000,000 against filed (143) and (541) million. Every figure here is recomputed from filed cells; no served value is an input."
  - da_id: DA-24
    chosen_reading: "Non-operating contamination of operating_income. Tested rather than assumed: gross profit - EXCLUSIVE opex closes to the filed operating line in 2 of 2 consolidated periods AND in 4 of 4 segment-sum ties, despite an H1 non-operating block of 2,731 million. operating_income is uncontaminated on these periods."
  - da_id: DA-25
    chosen_reading: "Normalised per-unit metrics not reproducible from audited tables. SPCX files NO cost per launch anywhere; the per-launch cost side is therefore UNEXERCISED on a filed basis and is reported here only as a labelled upper bound with its numerator/denominator mismatch stated."
  - da_id: DA-26
    chosen_reading: "Annual figures mislabelled as quarterly. Not observed at SPCX in the layer reached (its served row carries interim, not annual, cells). Reported as not-observed-in-this-pass, NOT as clean-workspace-wide."
  - da_id: DA-27
    chosen_reading: "Fiscal-period labels derived from the calendar quarter. One served response carries `fiscal_period: Q2` while its metrics block holds 3M cells (143, 541) and its ratio block's denominators hold 6M cells (12,508). Two periods, one label. The period basis is stated in-line on every figure below."
  - da_id: DA-28
    chosen_reading: "Capital-structure discontinuity around an IPO invalidates share-count detectors. SPCX's weighted-average shares run 2,929k -> 5,864k YoY with the 6M average (4,879k) BELOW the Q2 average, placing the change inside Q2 2026. No share-count-derived detector is used anywhere in this artifact."
  - da_id: DA-29
    chosen_reading: "A reconciliation that closes is not thereby a check; a term appearing nowhere in the source makes it a back-solve. Applied to every reconciliation here and reported in S6."
  - da_id: DA-30
    chosen_reading: "Two bases on one concept collapsed without a basis field. Three separate instances found at SPCX, all reported on both bases: segment vs consolidated (65.80% vs 55.27% gross margin); 'Net loss' (4,817) vs 'Net loss attributable to shareholders' (5,488); and the served ratio's segment numerator over a consolidated denominator."
evidence_grade: DEMONSTRATED
key_metrics:
  launch_services_share_of_consolidated_revenue_q2_2026_3m_pct: 8.2928
  launch_services_share_of_consolidated_revenue_h1_2026_6m_pct: 7.8190
  space_segment_gross_margin_pct: 65.80
  space_segment_operating_margin_pct: -56.34
citations:
  - figure: "SPCX sec8 p.42"
    ticker: SPCX
    citation_id: sec8
    page_no: 42
    url: https://agentii.ai/v/SPCX/sec8/42
    located_via: read_source_pages
  - figure: "SPCX sec8 p.30"
    ticker: SPCX
    citation_id: sec8
    page_no: 30
    url: https://agentii.ai/v/SPCX/sec8/30
    located_via: read_source_pages
  - figure: "SPCX sec8 p.13"
    ticker: SPCX
    citation_id: sec8
    page_no: 13
    url: https://agentii.ai/v/SPCX/sec8/13
    located_via: read_source_pages
  - figure: "SPCX sec8 p.5"
    ticker: SPCX
    citation_id: sec8
    page_no: 5
    url: https://agentii.ai/v/SPCX/sec8/5
    located_via: read_source_pages
  - figure: "SPCX sec8 p.31"
    ticker: SPCX
    citation_id: sec8
    page_no: 31
    url: https://agentii.ai/v/SPCX/sec8/31
    located_via: read_source_pages
  - figure: "SPCX sec8 p.32"
    ticker: SPCX
    citation_id: sec8
    page_no: 32
    url: https://agentii.ai/v/SPCX/sec8/32
    located_via: read_source_pages
---

# SPCX — ratio analysis: the margin ladder, the per-launch reconciliation, and the demand-side share

**Pillars served: PIL-3, PIL-5, PIL-6** (spec §3 purpose tag `(P2, P5, P6)`; the ladder in S3 also carries
PIL-2). The frontmatter carries `cross` because the field admits a single value or `cross`, and this
artifact spans three pillars.

## 0. The finding

**SPCX's launch business is 8.29% of its own revenue on the 3M basis and 7.82% on the 6M basis — and it is
the only issuer in this trio whose launch share sits BELOW PIL-6's 0.10 bar.** The thesis's PIL-6 note turns
on exactly this datum. The finding is that **the datum is a property of SPCX's revenue mix, not of launch**:
the identical construction at RKLB gives **19.05% (3M) / 24.92% (6M)**, both above the bar. A threshold that
one issuer clears by 2.3x and the largest launcher in the universe misses by 17% is a threshold on
diversification, not on launch economics.

**Second finding: the served ratio layer inverts SPCX's operating margin by 46.47 pp and it is not one
defect but three stacked.** The served `operating_margin` **+29.79%** is the **AI segment's** H1 operating
loss (3,726) divided by **consolidated** H1 revenue (12,508), against a filed consolidated operating margin
of **−16.68%**. A **segment** numerator over a **consolidated** denominator (DA-30), carrying a **half-year**
quantity under a `Q2` label whose sibling field carries the **quarter** (DA-27), with the sign stripped
(DA-23).

**Third finding, new, and it is an issuer-filed DA-30 rather than a platform one.** SPCX files two net
losses for H1 2026: `Net loss $(4,817)` and `Net loss attributable to shareholders $(5,488)`. On the Q2
column the two are equal (541 = 541), so a quarter-only reader never sees two bases. **The 671 is visible
only in the cumulative column.** EPS is struck on the attributable basis.

**Fourth finding: SPCX's segment gross and operating margins order in OPPOSITE directions.** Space has the
**highest** gross margin in the company (**65.80%**) and the **worst** operating margin (**−56.34%**), and
the entire 94.93 pp inversion is R&D at **111.85% of segment revenue**.

## 1. The acceptance test — run, and stated

> Accept an identification **only if it is (a) exact, (b) stable across periods, and (c) consistent with a
> formula the skill specifies or a basis the issuer files.** Everything else is `UNRESOLVED`, never
> "probably fine".

**This test was run on every identification in this artifact.** Its results are the spine of S5 and S7.

The *exactness* limb is the operative one. A ~2,500-candidate expression sweep over 36 filed cells at **0.5%
tolerance** produces **6–9 coincidental hits per metric**; at **4-decimal** exactness across ~1,300 ordered
filed-cell pairs the expected coincidence count is below one. **A 4-dp exact match on a filed cell pair is
admissible; a 0.5%-tolerant match is not** — and the brief's `quick_ratio == cash_ratio` byte-identity
result (6 of 15 comparable rows, with RKLB the counterexample at 0 of 9) is the demonstration that served
ratios are not merely noisy but *duplicative*.

Two served-ratio families were therefore not quoted anywhere: **not one served ratio is an input to this
artifact.** The served layer is used **only as a subject** — as evidence about the extraction layer — never
as a source of figures about SPCX.

## 2. The basis discipline this artifact obeys

The brief's period-basis trap applies to every SPCX quantity here, so **every SPCX figure below carries its
period basis inline**: `3M` = three months ended June 30, `6M` = six months ended June 30. The trap is live
in this filing: **Launch Services revenue rose +$158M on 3M and fell −$78M on 6M** (both stated in the
filing — [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42)), customer launches went **9 → 10 on 3M** and
**21 → 17 on 6M**, and net loss **fell 46.3% on 3M and rose 213.6% on 6M** (filed percentages, same page).
**Four consecutive quantities in one filing with opposite signs on the two bases.** A SPCX artifact that
quotes one number without its basis is not reporting a fact about the company.

## 3. The margin ladder, ordered by distance from programme risk

Ordering criterion: **the share of the issuer's P&L exposed to the outcome of any single programme**,
farthest first. Rows 1–10 are inherited from `sector-overview` §4; rows 11 and 13–18 were **verified here**
and rows 12, 14, 15 and 18 are **SPCX's contribution to the ladder**.

| # | Rung | Issuer | Metric | Value | Basis | Grade |
|---|---|---|---|---|---|---|
| 1 | component supply | TER | op margin | 32.9% | inherited | CLAIMED |
| 2 | component supply | HEI | op margin | 25.5% | inherited | CLAIMED |
| 3 | component supply | CW | op margin | 19.3% | inherited | CLAIMED |
| 4 | component supply | KRMN | op margin | 19.1% | inherited | CLAIMED |
| 5 | component supply | WWD | op margin | ~17% | inherited | CLAIMED |
| 6 | prime integrator | LMT | op margin | 12.4% | inherited | CLAIMED |
| 7 | prime integrator | RTX | op margin | 11.4% | inherited | CLAIMED |
| 8 | prime integrator | LHX | op margin | 11.1% | inherited | CLAIMED |
| 9 | prime integrator | NOC | op margin | 10.1% | inherited | CLAIMED |
| 10 | single-customer operator | GSAT | op margin | **+7.4%** | inherited | CLAIMED |
| 11 | **demand-owning operator** | **SPCX Connectivity** | **segment op margin** | **+38.59%** | **3M** | **DEMONSTRATED** |
| 12 | manufacturer (reference) | SPCX Space | segment **gross** margin | 65.80% | 3M | DEMONSTRATED |
| 13 | launcher/space mfr | RKLB (consolidated) | op margin | −24.57% | 3M | DEMONSTRATED |
| 14 | launcher/space mfr | SPCX AI | segment op margin | **−49.08%** | 3M | DEMONSTRATED |
| 15 | **launcher** | **SPCX Space (launch + dev)** | **segment op margin** | **−56.34%** | **3M** | **DEMONSTRATED** |
| 16 | launcher/space mfr | LUNR | op margin | −56.3% | inherited | CLAIMED |
| 17 | launcher/space mfr | FLY | op margin | −80.90% | 3M | DEMONSTRATED |
| 18 | manufacturer (reference) | RKLB Launch Services | segment **gross** margin | 42.86% | 3M | DEMONSTRATED |
| — | — reference | **SPCX (consolidated)** | **op margin** | **−1.83%** | **3M** | **DEMONSTRATED** |

Rungs 11, 14 and 15 recomputed from filed cells:
7,814 − 3,495 = 4,319 and 4,319 − (3,548 + 912 + 2) = **4,319 − 4,462 = (143)**, so 143 / 7,814 = **−1.83%**
consolidated; 1,656 / 4,291 = **+38.59%** Connectivity; 1,257 / 2,561 = **−49.08%** AI;
542 / 962 = **−56.34%** Space ([📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30)).

**The rung that belongs to SPCX is rung 11, and it is the top of the computable ladder.** The demand-owning
integrator — the segment that sells the service the launch buys — earns **+38.59%**, above every component
supplier and 2.55x the best prime. **The launch segment earns −56.34%, below every prime, below the
one-customer operator, below the space manufacturer.** The value-pool migration PIL-2 asserts is visible
inside a single issuer's segment table: the two segments sit **94.93 pp apart** and the launch side is the
negative one.

### The ordering is not monotone — it is bimodal

Both ends carry high margins (Connectivity **+38.59%**; TER **32.9%**) and the **middle rungs are negative**
(RKLB −24.57%, SPCX AI −49.08%, SPCX Space −56.34%, FLY −80.90%). The value pool sits with the party that
**owns the demand** and the party that **sells components into every programme**; the launcher is the middle
of the stack and the hole in the ladder.

### Rung 12 and rung 15 are the same segment — and they point opposite ways

**Space has the highest gross margin in the company and the worst operating margin.** Gross:
(962 − 329)/962 = 633 / 962 = **65.80%** — *segment* basis, and **it does not reproduce the consolidated
55.27%** (4,319 / 7,814) because a segment numerator over a consolidated denominator is a different
quantity (DA-30). Against Connectivity's (4,291 − 2,060)/4,291 = 2,231 / 4,291 = **51.99%**. Operating:
**−56.34%** against Connectivity's **+38.59%**. The whole 94.93 pp inversion is R&D — Space R&D is
**1,076 / 962 = 111.85% of segment revenue** against Connectivity's 294 / 4,291 = **6.85%**.

**A ladder built on gross margin puts the launch segment at the top of the universe; the same ladder built
on operating margin puts it at the bottom.** Rank order is not a property of the issuer; it is a property of
the line chosen. The brief's anchor figure 65.80% is confirmed at 4 dp and confirmed to be SEGMENT basis.

## 4. The per-launch reconciliation

PIL-5's reconciliation is RKLB's; at SPCX the same construction is only half-testable, and the half that is
missing is the load-bearing half.

### The revenue leg — filed, and it reproduces exactly

| Period | Launch Services revenue | Customer launches | Revenue per customer launch |
|---|---|---|---|
| Q2 2025 (3M) | 490 | 9 | 54.44 |
| **Q2 2026 (3M)** | **648** | **10** | **64.80** (+19.03%) |
| H1 2025 (6M) | 1,056 | 21 | 50.29 |
| **H1 2026 (6M)** | **978** | **17** | **57.53** (+14.41%) |

Cells from [📄 SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13) (Launch Services 648 / 490 / 978 / 1,056)
and launch counts filed in MD&A on [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42) (9 → 10 on 3M,
21 → 17 on 6M). **The MD&A deltas reproduce exactly from the disaggregation table**: 648 − 490 = **+158** and
978 − 1,056 = **−78**, matching the filing's own "+$158 million" and "decreased by $78 million" verbatim;
Launch and Development 314 − 256 = +58 and 603 − 555 = +48 match its "+$58 million" and "+$48 million". **Four
of four filed narrative deltas close exactly against the table.**

**Revenue per customer launch ROSE on both bases** — +19.03% on 3M and +14.41% on 6M — while volume moved
**up** on 3M and **down** on 6M. A per-launch revenue figure that rises under both signs of the volume
change is a **mix** result, not a volume result: the filing names a "favorable customer mix shift" on 3M.
This is DA-25's class, and it is the correct reading rather than an anomaly.

### The cost leg — UNEXERCISED on a filed basis

**SPCX files no cost per launch in any period.** The resolving disclosure is a launch-segment cost of
revenue per mission on a filed basis; SPCX disaggregates Launch Services **revenue only**. So the cost leg
of PIL-5 **cannot be run at SPCX**, and it is recorded **`UNEXERCISED`**, not CLEAN.

The nearest construct, reported **as a labelled upper bound and not as a cost per launch**:

| Period | Space segment cost of revenue | Customer launches | Segment CoR per customer launch |
|---|---|---|---|
| Q2 2025 (3M) | 330 | 9 | 36.67 |
| Q2 2026 (3M) | 329 | 10 | **32.90** (−10.28%) |
| H1 2025 (6M) | 627 | 21 | 29.86 |
| H1 2026 (6M) | 610 | 17 | **35.88** (+20.18%) |

**The caveat is structural and is stated, not buried:** the numerator is the **whole Space segment's** cost
of revenue, which carries Launch & Development cost alongside Launch Services cost, while the denominator
counts **only customer launches**. The quotient is therefore an **upper bound on launch cost per mission**,
and it is a bound of unknown tightness because SPCX does not disclose the split. It is admissible only as a
**sign and magnitude** statement: **SPCX's launch-adjacent unit cost FELL 10.3% on 3M and ROSE 20.2% on
6M.** A **30.5 pp swing between the two period bases of the same activity, in opposite directions** — the
period-basis trap on the cost side of the curve, on the issuer whose curve the thesis's PIL-3 says is not
demonstrated.

### The comparison that matters for PIL-3

At RKLB, cost per launch fell **12.0%** YoY on 3M (a **filed** metric) while its revenue per launch rose
**15.2%**. At SPCX the analogous 3M readings are −10.3% and +19.0%. **Two independent issuers, two
independent filings, the same direction on both legs on the 3M basis** — a cost falling and a price rising,
with the spread widening. That is the pass-through test PIL-6 specifies, run twice, and **it does not fire:
no demonstrated fall in revenue per launch accompanies the fall in cost per launch. The retained value
widened at both issuers.** The 6M SPCX basis reverses the cost leg, which is why the basis must travel with
the claim.

## 5. The demand-side programme-cost shares (PIL-6)

PIL-6's metric is `launch_cost_share_of_total_program_cost_at_universe_demand_side_names`, bar **0.10**,
op `>`. The demanded quantity needs the **customer's** programme-cost base. **No issuer files one.**
PIL-6 instructs: *IF THE QUANTITY IS NON-FORMABLE, RECORD NON-FORMABLE — NOT PASS.*

**→ PIL-6's metric is `NON-FORMABLE`.** The resolving disclosure is a customer-side programme-cost base
(capex or total programme value) set against the launch price paid. Class:
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — a supplier's filing cannot contain the customer's programme cost.

**The bar's filed datum, and what it actually measures.** The thesis's note reads *"Launch Services is 8.29%
of SPCX consolidated revenue — below the 0.10 bar."* Verified exactly:

| Period | Launch Services revenue | Consolidated revenue | Launch share |
|---|---|---|---|
| Q2 2026 (3M) | 648 | 7,814 | **8.2928%** |
| H1 2026 (6M) | 978 | 12,508 | **7.8190%** |

**Both bases are below the 0.10 bar**, and the 3M figure is the 8.29% the thesis quotes —
648 / 7,814 = 8.2928%, rounded-exact, DEMONSTRATED.

**The transfer test.** The same construction at the third issuer in this trio:

| Issuer | 3M | 6M | vs bar |
|---|---|---|---|
| **SPCX** | 8.29% | 7.82% | **below on both** |
| **RKLB** | 19.05% | 24.92% | **above on both** |
| **FLY** | 7.99% | 11.41% | **crosses between bases** |

**FLY crosses the bar purely by changing period basis** — 7.99% on 3M, 11.41% on 6M. A threshold whose
verdict flips on basis alone is not a threshold on the underlying quantity. **PIL-6's bar is not
discriminating launch economics across this universe; it is discriminating revenue-mix composition.** SPCX
is below the bar because Connectivity and AI are 87.7% of its revenue (4,291 + 2,561 = 6,852 of 7,814), not
because launch is cheap.

### The quantity SPCX *does* let you test: the boundary of the measured item

The brief records that SPCX's Space segment revenue boundary is the **customer** boundary — ~74% of launches
produce no Space revenue by design. That is the reason PIL-6 cannot be formed here: **the launch cost SPCX
incurs on internal missions appears nowhere as revenue, so no share can be computed against any programme
base, the customer's or SPCX's own.** The resolving disclosure is a per-mission cost of revenue for
internally-flown missions.

## 6. DA-23 / DA-24 residuals, and the DA-29 circularity rule

### DA-24 — `CLEAN`, and the check was EXERCISED in 6 of 6

gross profit − **EXCLUSIVE** opex (R&D + SG&A + restructuring + impairment; excludes cost of revenue),
against the filed operating line:

| Period | Gross profit | Exclusive opex | Difference | Filed loss from ops |
|---|---|---|---|---|
| Q2 2026 | 7,814 − 3,495 = 4,319 | 3,548 + 912 + 2 = 4,462 | **(143)** | **(143)** ✓ |
| H1 2026 | 12,508 − 5,883 = 6,625 | 7,062 + 1,658 + (−9) = 8,711 | **(2,086)** | **(2,086)** ✓ |
| Q2 2025 | 4,071 − 2,282 = 1,789 | 1,958 + 606 + 190 + 5 = 2,759 | **(970)** | **(970)** ✓ |
| H1 2025 | 8,138 − 4,244 = 3,894 | 3,515 + 1,099 + 194 + 29 = 4,837 | **(943)** | **(943)** ✓ |

**4 of 4 EXACT.** The **INCLUSIVE** pairing — `us-gaap:CostsAndExpenses`, which is the `Total costs and
expenses` line and *includes* cost of revenue — gives 7,814 − 7,957 = (143) **only because the inclusive
total is what the statement shows**; the identity `gross profit − opex = operating_income` is true here with
the **exclusive** definition and the statement's own total is the inclusive one. **The opex definition used
throughout is the exclusive one, named in-line, as the contract requires.**

**The segment ties close 4 of 4, exactly:**

| Period | Space | + Connectivity | + AI | = Sum | Filed |
|---|---|---|---|---|---|
| Q2 2026 | (542) | 1,656 | (1,257) | **(143)** | (143) ✓ |
| H1 2026 | (1,204) | 2,844 | (3,726) | **(2,086)** | (2,086) ✓ |
| Q2 2025 | (369) | 923 | (1,524) | **(970)** | (970) ✓ |
| H1 2025 | (439) | 1,956 | (2,460) | **(943)** | (943) ✓ |

and the segment totals close too: 1,504 + 2,635 + 3,818 = 7,957 ✓; 2,785 + 4,704 + 7,105 = 14,594 ✓;
1,115 + 1,665 + 2,261 = 5,041 ✓; 2,050 + 3,106 + 3,925 = 9,081 ✓.

**Why this is a real test at SPCX and not a formality: the non-operating block is large.** H1 2026's
operating loss is (2,086) while its net loss is (4,817) — a **2,731 non-operating wedge**, of which
`Other income (expense), net (1,962)` is the bulk ([📄 SPCX 10-Q p.5](https://agentii.ai/v/SPCX/sec8/5)).
**The component identity closes on the operating line anyway, which is precisely what distinguishes an
uncontaminated `operating_income` from a contaminated one. DA-24 does not fire at SPCX, and this is a
passed check rather than an unengaged one.**

### DA-23 — FIRES on sign, at both layers

The served metrics block returns `operating_income +143,000,000` and `net_income +541,000,000` against filed
**(143)** and **(541)** million, both negative. Magnitudes identical, signs stripped — the `|x|` signature.
**Three issuers, three issuers affected** (RKLB +57,514,000 / (57,514); SPCX +143,000,000 / (143); FLY
+95,197,000 / (95,197)). The strip is uniform across the served layer and **only the component identity
detects it.**

### The served ratio layer: three stacked defects on one row

One served row, `fiscal_period: Q2`. Its two margins recomputed against filed cells:

| Served field | Served | Construction | Verdict |
|---|---|---|---|
| `operating_margin` | **+0.2979** | 3,726 (AI segment, **6M**, operating loss) / 12,508 (consolidated, 6M revenue) = 29.7889% | **rounded-exact** |
| `net_margin` | **+0.3851** | 4,817 (consolidated **6M** net loss) / 12,508 = 38.5110% | **rounded-exact** |

**Defect 1 — the sign (DA-23).** Filed consolidated H1 operating margin is
(2,086) / 12,508 = **−16.6773%**. Served: **+29.7889%**. **Inversion = 46.4662 pp → 46.47 pp**, and the
brief's 46.47 pp is reproduced exactly. The served line is a **profit** margin of +29.79% on an issuer whose
H1 was a loss of 16.68% of revenue.

**Defect 2 — numerator and denominator are on different entities (DA-30).** The numerator 3,726 is the **AI
segment's** operating loss; the denominator 12,508 is **consolidated** revenue. The AI segment is 27.0% of
consolidated revenue (3,379 / 12,508) and 178.6% loss-heavy relative to its own revenue
(−3,726 / 3,379 = **−110.27%**). **A segment loss over a consolidated base is not a margin of anything.**
This is the *same shape* as the RKLB Q2 2025 served `gross_margin` 0.2254 (H1 2025 Space Systems gross
profit over H1 2025 consolidated revenue) — **one defect class, two issuers, two line items.**

**Defect 3 — one label, two periods (DA-27).** The same response's metrics block is **3M** (143, 541) while
its ratio block's denominators are **6M** (12,508). **Two periods inside one `Q2`-labelled payload:**

| Quantity | 3M | 6M |
|---|---|---|
| operating loss | (143) | (2,086) |
| net loss | (541) | (4,817) |
| revenue | 7,814 | 12,508 |

The served `net_margin` is the **6M** net loss over **6M** revenue = 38.51%. The 3M net loss over 3M revenue
is 541 / 7,814 = **6.92%**. **The two bases differ by 31.59 pp and only one of them is in the payload's
label.**

**And the served pair is byte-duplicated where the brief says it is:** `quick_ratio` equals `cash_ratio`
exactly in every SPCX row served (1 of 1). A ratio layer that returns the same value under two names is not
a source, whatever the label says.

### The DA-30 instance that is issuer-filed, not platform-made

| H1 2026 | Value | Basis |
|---|---|---|
| `Net loss` | **$(4,817)** | consolidated |
| `Net loss attributable to shareholders` | **$(5,488)** | after the noncontrolling interest |
| **Difference** | **671** | |

On the Q2 column the two are **equal** (541 = 541). **The divergence exists only in the cumulative column**,
so a quarter-only reader sees one number and a half-year reader sees two. EPS of $(1.12) is struck on the
**attributable** basis (5,488 / 4,879 = 1.1248 → $(1.12) ✓), while the served `net_margin` silently uses the
**4,817** basis (4,817 / 12,508 = 38.5110% → 0.3851 ✓ — the 5,488 basis would give 43.8759% → 0.4388, which
is *not* the served value). **Every competing basis is reported here; the served layer reported one and did
not name it.**

**DA-28 boundary.** Weighted-average shares run 2,929k (Q2 2025) → 5,864k (Q2 2026), and the 6M average
(4,879k) sits **below** the Q2 average, which places the bulk of the change **inside** Q2 2026. The
capital-structure discontinuity is real and IPO-scale. **No share-count-derived detector is used anywhere in
this artifact, and `EPS × shares` is not used as a sign test** — note that here EPS and shares are mutually
consistent (both struck on the attributable basis), which is exactly the trap: consistency would have made
the inadmissible check *look* admissible.

### DA-29 — the circularity rule, applied to every reconciliation above

> *If any term appears nowhere in the source, the check is a back-solve.*

**I ran this rule on all five reconciliations in this artifact.** Its findings:

1. **The component identity (S6).** Every term — revenue, cost of revenue, R&D, SG&A, restructuring,
   impairment, the filed operating line — is a filed cell on
   [📄 SPCX 10-Q p.5](https://agentii.ai/v/SPCX/sec8/5). **Not a back-solve.**
2. **The segment-sum ties, 4 of 4 (S6).** Every term is a filed segment cell on
   [📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30) / [p.31](https://agentii.ai/v/SPCX/sec8/31) /
   [p.32](https://agentii.ai/v/SPCX/sec8/32). **Not a back-solve.**
3. **The launch-share and revenue-per-launch series (S4, S5).** Both terms filed —
   [📄 SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13) for revenue,
   [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42) for the counts. **Not a back-solve.**
4. **The served-ratio reconstructions (S6).** Both constructions are **exact on filed cell pairs**, so no
   invented term was needed. **Not a back-solve** — but note what that means: **the served ratio was
   reproducible to 4 dp and still wrong.** The defect is not in the arithmetic; it is that the payload never
   says which period, which entity, or which sign basis it used. **A reconstruction that closes is not
   thereby a correct ratio** — DA-29's rule holds in the direction the brief does not stress: closure is not
   a warrant of *meaning*, only of *derivation*.
5. **The Space-segment cost-per-launch bound (S4).** Here the rule bites. The **split of Space segment cost
   of revenue between Launch Services and Launch & Development appears nowhere in the source**, and that
   split is what would turn the bound into a measurement. **It is a back-solve, and it is labelled an upper
   bound for exactly that reason** — never reported as a cost per launch.

### Also carried

- **DA-25** — SPCX files no normalised per-unit metric on cost; the per-launch cost side is `UNEXERCISED`.
  The revenue side's 3M/6M sign flip on revenue per launch is the DA-25 class and is reported as mix.
- **DA-26** — not observed at SPCX in the layer reached (its served row carries interim cells, not annual
  ones). **Reported as not-observed-in-this-pass, which is not the same as CLEAN.** The brief's correction
  stands: DA-26 is 19 of 20 issuers with **FLY the counterexample**, and RKLB the instance where the Q4
  rows carry full-year figures.

## 7. What is UNRESOLVED

| # | Item | Class | Resolving disclosure |
|---|---|---|---|
| 1 | Launch-only revenue share of Space segment margin | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a cost-of-revenue split between Launch Services and Launch & Development. SPCX disaggregates Launch Services **revenue only**, so the launch-only margin — the rung the ladder most wants — cannot be isolated from the segment figure. |
| 2 | SPCX cost per launch, any period | `UNEXERCISED` (not CLEAN) | a per-mission cost of revenue, filed or disclosed. |
| 3 | PIL-6's demanded quantity at SPCX | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a customer-side programme-cost base. |
| 4 | The served row's `fiscal_period` | `UNRESOLVABLE-FROM-PLATFORM` | a basis field on the served payload. Both margin constructions reproduce exactly, so the defect is the missing basis label, not the arithmetic. |
| 5 | Space segment R&D at 111.85% of segment revenue — Starship-capitalisation boundary | not read in this pass | the capitalised-development-cost note and the R&D line's own composition. ⚠️ **This matters for rung 15: a segment loss this deep is a function of where Starship development sits.** If any Starship cost is capitalised rather than expensed, rung 15's −56.34% is an **unfloored** comparison against peers who expense. Recorded `UNRESOLVED` rather than adjusted. |
| 6 | DA-26 presence at SPCX | not read in this pass | a served row whose revenue equals a filed annual total. Not observed at SPCX; not asserted absent. |

## Sources

| Source | Used for |
|---|---|
| [📄 SPCX 10-Q p.5](https://agentii.ai/v/SPCX/sec8/5) | Consolidated statements of operations: the component identity (S6), the two net-loss bases (S6), the non-operating wedge, EPS and share counts |
| [📄 SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13) | Revenue disaggregation Table16 / Table17: Launch Services, Launch and Development, Space, Connectivity, AI |
| [📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30) | Q2 2026 segment table: Space / Connectivity / AI revenue, cost of revenue, R&D, SG&A, operating result |
| [📄 SPCX 10-Q p.31](https://agentii.ai/v/SPCX/sec8/31) | H1 2026 and Q2 2025 segment tables: the 6M basis of every SPCX ratio, and the Q2 2025 comparison |
| [📄 SPCX 10-Q p.32](https://agentii.ai/v/SPCX/sec8/32) | H1 2025 segment table: the second 6M comparison |
| [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42) | Space segment MD&A: the +158 / −78 Launch Services deltas, customer launches 9 → 10 and 21 → 17, net loss −46.3% / +213.6% |
