---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-5
ticker: RKLB
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
    chosen_reading: "The platform serves a filed negative as a positive of identical magnitude (|x| stripping). Detected ONLY by the component identity, because RKLB has never had positive operating income so no heuristic can flag it. Every figure below is recomputed from filed cells; no served value is used as an input."
  - da_id: DA-24
    chosen_reading: "Non-operating contamination of operating_income. Tested, not assumed: gross_profit - EXCLUSIVE opex closes to the filed operating loss exactly in 4 of 4 periods, so operating_income is uncontaminated on these periods."
  - da_id: DA-25
    chosen_reading: "Normalised per-unit metrics not reproducible from the audited tables. revenue per launch / cost per launch are treated as a SEPARATE disclosure from the audited segment table, never as the segment table, and the gap between them is the measurement."
  - da_id: DA-26
    chosen_reading: "Period-content vs period-label. The Q4-labelled served rows carry FULL-YEAR figures (verified: the Q4 row's revenue equals the sum of the filed annual segment revenues). Not annual-as-quarterly at FLY, so not reported as universal."
  - da_id: DA-27
    chosen_reading: "Fiscal-period labels derived from the calendar quarter. Accepted as a label hazard only; the period basis is stated in-line on every figure below."
  - da_id: DA-29
    chosen_reading: "A reconciliation that closes is not thereby a check. A term appearing nowhere in the source makes the check a back-solve. Applied to every reconciliation in this artifact; stated in S5."
  - da_id: DA-30
    chosen_reading: "Two bases on one concept collapsed without a basis field. Both competing bases are reported wherever they exist: segment vs consolidated, exclusive vs inclusive opex, quarter vs half-year."
deal_security_basis: standalone_pre_merger
evidence_grade: DEMONSTRATED
citations:
  - figure: "RKLB FY2025 / FY2024 / FY2023 segment table: Launch Services and Space Systems revenue, cost of revenue and gross profit."
    ticker: "RKLB"
    form_type: "10-K"
    citation_id: "sec87"
    page_no: 107
    url: "https://agentii.ai/v/RKLB/sec87/107"
    located_via: "read_source_pages"
  - figure: "RKLB condensed consolidated statements of operations: total revenues 234,066 / 144,498 / 434,414 / 267,067; total cost of revenues 149,490 / 98,110 / 273,345 / 185,432; gross profit 84,576 / 46,388 / 161,069 / 81,635; total operating expenses 142,090 / 106,027 / 274,552 / 200,462; operating loss (57,514) / (59,639) / (113,483) / (118,827)."
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec109"
    page_no: 6
    url: "https://agentii.ai/v/RKLB/sec109/6"
    located_via: "read_source_pages"
  - figure: "RKLB segment table, Q2 2026 / Q2 2025 / H1 2026 / H1 2025: Launch Services 44,586-25,476-19,110 and Space Systems 189,480-124,014-65,466 for the quarter."
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec109"
    page_no: 32
    url: "https://agentii.ai/v/RKLB/sec109/32"
    located_via: "read_source_pages"
  - figure: "RKLB revenue and cost per launch, Q2 2026 / Q2 2025 / H1 2026 / H1 2025: $9.1M / $7.9M / $9.2M / $7.5M revenue and $4.4M / $5.0M / $4.9M / $5.3M cost; six Electron missions against five, two of the six HASTE."
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec109"
    page_no: 37
    url: "https://agentii.ai/v/RKLB/sec109/37"
    located_via: "read_source_pages"
  - figure: "RKLB revenue and cost per launch, Q1 2026 and Q1 2025, with the verbatim metric definitions and the build/launch counts (14/16 in 2024, 24/21 in 2025, 5/6 in Q1 2026)."
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec104"
    page_no: 31
    url: "https://agentii.ai/v/RKLB/sec104/31"
    located_via: "read_source_pages"
  - figure: "RKLB products-and-services split of segment revenue and cost, Q2 2026 and H1 2026 (Launch Services 44,586-25,476-19,110)."
    ticker: "RKLB"
    form_type: "10-Q"
    citation_id: "sec109"
    page_no: 33
    url: "https://agentii.ai/v/RKLB/sec109/33"
    located_via: "read_source_pages"
key_metrics:
  rklb_consolidated_operating_margin_pct_q2_2026_3m: -24.57
  rklb_launch_services_segment_gross_margin_pct_q2_2026_3m: 42.86
  rklb_space_systems_segment_gross_margin_pct_q2_2026_3m: 34.55
  rklb_launch_share_of_revenue_pct_q2_2026_3m: 19.05
---

# RKLB — ratio analysis: the margin ladder, the per-launch reconciliation, and the demand-side share

**Pillars served: PIL-5 (primary), PIL-3, PIL-6.** The frontmatter carries the enum-valid primary only;
`pillar` admits one value. The spec's §3 purpose tag for this skill is `(P2, P5, P6)`.

## 0. The finding

**RKLB's per-launch disclosure is a cost-side measurement whose audited reconciliation fails its own 5%
threshold in 3 of 6 periods, and a revenue-side normalisation whose sign is not stable.** The disclosed
`cost per launch x missions` reproduces the audited Launch Services cost of revenue to **+0.4% / −22.9% /
−12.8% / −8.6% / +3.6% / −3.5%** across the six periods where the multiplicand is observable. Three of
those six exceed PIL-5's 5% bar. The revenue leg spans **−17.5% to +22.5%** and changes sign twice. The
metric the thesis calls a durable cost-side measurement is durable in *kind* — it is always the same
construction — and not in *tolerance*.

**Second finding, and it is new: the served-ratio layer at RKLB uses three different period conventions on
rows within a single ticker, so no served ratio is recomputable.** The row stamped `2026 Q2` carries a
**half-year** gross margin (161,069 / 434,414 = 37.08%), a **prior-year half-year** net numerator over the
*current* half-year (127,030 / 434,414 = 29.24%), and an operating margin that reproduces **neither** under
the same row's own rounding convention. The rows stamped `Q4` carry **full-year** figures. The row stamped
`2026 Q1` carries its own quarter. Three conventions, one ticker, ten rows.

## 1. The acceptance test — run, and stated

> Accept an identification **only if it is (a) exact, (b) stable across periods, and (c) consistent with a
> formula the skill specifies or a basis the issuer files.** Everything else is `UNRESOLVED`, never
> "probably fine".

**This test was run on every identification in this artifact.** Its results are the spine of S4 and S6.

The reason the *exactness* limb is the operative one here: a ~2,500-candidate expression sweep over 36 filed
cells at **0.5% tolerance** produces **6–9 coincidental hits per metric**. At 4-decimal exactness the
collision space collapses — 36 filed cells give ~1,300 ordered pairs against a 1e-4 match window, so the
expected coincidence count is well below one. **A 4-dp exact match on a filed cell pair is admissible
evidence; a 0.5%-tolerant match is not.** Every identification below is therefore stated at 4 dp, and the
one that needs a *truncation* convention its own row does not use is called `UNRESOLVED` rather than named.

Served-ratio usability: of 16 ratio fields served for RKLB, **not one is quoted anywhere in this artifact.**

## 2. The margin ladder, ordered by distance from programme risk

Ordering criterion: **the share of the issuer's P&L that is exposed to the outcome of any single programme**,
farthest first. Component supply (revenue on component delivery, many programmes) is farthest; the
single-customer network operator is nearest. Rows 1–10 are inherited from `sector-overview` §4 with
provenance; rows 11–18 are **verified here** and are the RKLB contribution to the ladder.

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
| 10 | single-customer operator | GSAT | op margin | **−7.37%** | filed Q2 2026 | DEMONSTRATED |
| 11 | demand-owning operator | SPCX Connectivity | segment op margin | **+38.59%** | Q2 2026 3M | DEMONSTRATED |
| 12 | — reference | RKLB Space Systems | segment **gross** margin | 34.55% | Q2 2026 3M | DEMONSTRATED |
| 13 | launcher/space mfr | **RKLB (consolidated)** | op margin | **−24.57%** | Q2 2026 3M | DEMONSTRATED |
| 14 | launcher/space mfr | SPCX AI | segment op margin | −49.08% | Q2 2026 3M | DEMONSTRATED |
| 15 | launcher/space mfr | SPCX Space (launch) | segment op margin | −56.34% | Q2 2026 3M | DEMONSTRATED |
| 16 | launcher/space mfr | LUNR | op margin | −56.3% | inherited | CLAIMED |
| 17 | launcher/space mfr | FLY | op margin | **−80.90%** | Q2 2026 3M | DEMONSTRATED |
| 18 | — reference | RKLB Launch Services | segment **gross** margin | 42.86% | Q2 2026 3M | DEMONSTRATED |

Verified RKLB row: 84,576 − 142,090 = **(57,514)k**, so 57,514 / 234,066 = **−24.57%**
([📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6)). The inherited −24.6% row is this figure, which
**fixes the ladder's basis as Q2 2026 3M** — a basis the sector-overview panorama did not state. FLY's
−80.90% and SPCX Space's −56.34% are on the same basis and were verified the same way, so the basis is
consistent at the three rungs I re-derived.

### Two anchors, tested

**(a) "Component suppliers earn ~2x the primes they supply" — HOLDS.** Tier means: suppliers
(32.9 + 25.5 + 19.3 + 19.1 + 17.0)/5 = **22.76%**; primes (12.4 + 11.4 + 11.1 + 10.1)/4 = **11.25%**.
Ratio **2.02x**. Note this is a *tier-mean* result: the largest single supplier (TER 32.9%) is 2.65x LMT and
the smallest (WWD ~17%) is 1.68x RTX, so the "2x" is a central tendency and not a pairwise law.

**(b) "The worst margin in the universe belongs to a network operator with one customer" — FALSIFIED as
stated.** The worst verified margin in the ladder is **FLY's −80.90%**, a launch-and-spacecraft
manufacturer. GSAT's **−7.37%** — ⚠️ **CORRECTED 2026-09-19: this row previously read `+7.4%`, which is the DA-23 STRIPPED SIGN.** The filed Q2 2026 figure is a LOSS. GSAT is not a thin positive margin; it is a swing to loss from `+9.15%`. The row is retained at its corrected value because it still sits where the ladder puts it, but **the 'thinnest positive' reading is withdrawn** — and its `inherited` grade was a signal that should have been followed up, not carried. GSAT is also the one-customer network operator, so its move to loss sharpens rather than softens the ladder's finding: the rung closest to monopsony is not the safest rung.
operator, so the anchor's *entity identification is right and its ordering claim is wrong*: the
one-customer operator is the **best** of the six loss-exposed operator/manufacturer rungs, not the worst.
The margin ladder's bottom is occupied by **manufacturers**, not operators.

### The ordering is not monotone — it is bimodal, and that is the result

Both ends of the ladder carry high margins (**SPCX Connectivity +38.59%** nearest to programme risk;
**TER 32.9%** farthest) and the **middle rungs are negative** (RKLB −24.57%, SPCX AI −49.08%, SPCX Space
−56.34%, FLY −80.90%). The value pool sits with the party that **owns the demand** and with the party that
**sells components into every programme**; the launcher is the middle of the stack and the hole in the
ladder. The sector-overview's reading ("independent network operator worst in monotone ordering") is not
supported by the values in either direction: the ordering is not monotone, and the operator end is not the
worst end.

### The gross-margin line and the operating-margin line order in OPPOSITE directions

At SPCX the segment with the **highest gross margin** has the **worst operating margin**: Space
(962 − 329)/962 = **65.80%** gross against **(542)/962 = −56.34%** operating, while Connectivity is
(4,291 − 2,060)/4,291 = **51.99%** gross against **+38.59%** operating. The whole 94.93 pp inversion is R&D:
Space R&D is 1,076 / 962 = **111.85% of revenue** against Connectivity's 294 / 4,291 = **6.85%**
([📄 SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30)). **A ladder built on gross margin puts the launch
segment at the top; the same ladder built on operating margin puts it at the bottom.** DA-30 in one table.

## 3. The per-launch margin reconciliation (PIL-5's core measurement)

Disclosed metrics, verbatim from
[📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37) and
[📄 RKLB 10-Q p.31](https://agentii.ai/v/RKLB/sec104/31):

| Period | Rev/launch | Cost/launch | Missions | Implied GM | Audited LS GM | Margin leg |
|---|---|---|---|---|---|---|
| Q1 2025 | $7.1M | $5.7M | 5 | 19.72% | 20.28% | **−0.56 pp** |
| Q2 2025 | $7.9M | $5.0M | 5 | 36.71% | 30.48% | **+6.23 pp** |
| H1 2025 | $7.5M | $5.3M | 10 | 29.33% | 26.07% | **+3.26 pp** |
| Q1 2026 | $9.3M | $5.4M | 6 | 41.94% | 44.33% | **−2.39 pp** |
| Q2 2026 | $9.1M | $4.4M | 6 | 51.65% | 42.86% | **+8.79 pp** |
| H1 2026 | $9.2M | $4.9M | 12 | 46.74% | 43.73% | **+3.01 pp** |

Audited Launch Services gross margins are recomputed from filed cells
([📄 RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32),
[📄 RKLB 10-K p.107](https://agentii.ai/v/RKLB/sec87/107)): 42.86 / 30.48 / 43.73 / 26.07 / 40.83 / 27.59 /
11.22 for Launch Services and 34.55 / 32.87 / 34.87 / 32.57 / 31.26 / 26.24 / 25.10 for Space Systems
(reverse-chronological Q2 2026, Q2 2025, H1 2026, H1 2025, FY2025, FY2024, FY2023). **All 14 cells
reproduce.** Period-level Launch Services cells for Q1 2025 and Q1 2026 are derived as H1 minus Q2, which is
arithmetic directly on filed cells.

**The margin leg changes sign in 2 of 6 periods** (−0.56, −2.39) and is positive in 4 of 6. The disclosed
per-launch revenue therefore over-states the audited segment in four periods and under-states it in two — it
is a **period normalisation**, not a directional bias, which is the correct reading and is *not* the
"timing" reading the thesis already falsified.

### The cost leg against PIL-5's 5% bar

`|disclosed cost per launch x missions − audited LS cost of revenue| / audited`, with the multiplicand
filed at every period:

| Period | Disclosed x missions | Audited LS CoR | Gap |
|---|---|---|---|
| Q1 2025 | $5.7M x 5 = $28,500k | $28,375k | **+0.44%** |
| Q2 2025 | $5.0M x 5 = $25,000k | $32,426k | **−22.90%** |
| H1 2025 | $5.3M x 10 = $53,000k | $60,801k | **−12.83%** |
| Q1 2026 | $5.4M x 6 = $32,400k | $35,440k | **−8.58%** |
| Q2 2026 | $4.4M x 6 = $26,400k | $25,476k | **+3.63%** |
| H1 2026 | $4.9M x 12 = $58,800k | $60,916k | **−3.47%** |

**PIL-5's falsifier FIRES: 3 of 6 periods exceed the 5% bar.** ⚠️ The thesis's interpretation note records
this as **"4 of 6"**; the six values listed alongside that count are **3 of 6** above 5%
(|+0.44|, |+3.63|, |−3.47| are below). **The count in the thesis is a miscount against its own list.**

**Stability test, run.** PIL-5 requires the construction to reproduce in every period the multiplicand is
observable or be quarantined. All six multiplicands are filed (5, 5, 10, 6, 6, 12), so the construction is
**not quarantined for unobservability** — it is **falsified on tolerance** in half the periods. The
remaining reading is the thesis's: the metric's own noise is larger than its 5% threshold, so the threshold
is not discriminable.

### The revenue leg — the unreconciled half

| Period | Disclosed x missions | Audited LS revenue | Gap |
|---|---|---|---|
| Q1 2025 | $7.1M x 5 = $35,500k | $35,592k | **−0.26%** |
| Q2 2025 | $7.9M x 5 = $39,500k | $46,646k | **−17.47%** |
| H1 2025 | $7.5M x 10 = $75,000k | $82,238k | **−8.80%** |
| Q1 2026 | $9.3M x 6 = $55,800k | $63,663k | **−12.35%** |
| Q2 2026 | $9.1M x 6 = $54,600k | $44,586k | **+22.46%** |
| H1 2026 | $9.2M x 12 = $110,400k | $108,249k | **+1.99%** |

**The two legs are asymmetric in a specific and measurable way.** The cost leg's 2026 readings (+3.63%,
−3.47%) both sit **inside** the 5% bar; the revenue leg's Q2 2026 reading (+22.46%) is the largest single
gap in the whole table and the revenue leg is the only leg that spans a wider range than the audited
quantity it is meant to track. Mean absolute gap: revenue **10.56%**, cost **8.64%**.

### The falsified anchor: "The Launch − Space differential is positive in every period"

**FALSE.** Differentials: Q2 2026 **+8.31** / Q2 2025 **−2.39** / H1 2026 **+8.86** / H1 2025 **−6.50** /
FY2025 **+9.57** / FY2024 **+1.35** / FY2023 **−13.88** pp. **Negative in 3 of 7.**

This fails **independently of period-alignment interpretation.** The seven Launch Services values are
{42.86, 30.48, 43.73, 26.07, 40.83, 27.59, 11.22} and the seven Space Systems values {34.55, 32.87, 34.87,
32.57, 31.26, 26.24, 25.10}. The Launch Services value 11.22 is below **every** Space Systems value
(minimum 25.10), so **at least one differential is negative under every possible re-pairing.** No
period-alignment reading rescues the claim.

**A second, sharper result:** FY2025's differential is **+9.57 pp on the annual basis** but **negative on both
2025 interim bases** (Q2 2025 −2.39, H1 2025 −6.50). This is a **period-basis sign flip inside one fiscal
year** — the same trap class the brief flags at SPCX, here on the launch-vs-non-launch comparison itself.
Also note the quantity tested: the anchor is a **gross**-margin differential, while PIL-2's specified metric
is an **operating**-margin differential. RKLB files segment gross profit only; **segment operating margin is
not disclosed**, so PIL-2's specified test is `NON-FORMABLE` at RKLB (see S4).

## 4. The demand-side programme-cost shares (PIL-6)

PIL-6's metric is `launch_cost_share_of_total_program_cost_at_universe_demand_side_names`, bar **0.10**,
op `>`. The demanded quantity needs the **customer's** programme-cost base. **No issuer in this artifact
files one.** PIL-6 instructs: *IF THE QUANTITY IS NON-FORMABLE, RECORD NON-FORMABLE — NOT PASS.*

**→ PIL-6's metric at RKLB is `NON-FORMABLE`.** The resolving disclosure: a customer-side programme-cost
base (capex or total programme value) against the launch price paid. Class:
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` at issuer level — a supplier's filing cannot contain the customer's
programme cost.

The **analogous within-issuer construction** — Launch Services revenue as a share of the issuer's own
revenue — is computable and is **not** the P6 quantity. Reported as a **proxy**, labelled:

| Period | Launch Services revenue | Total revenue | Launch share of revenue |
|---|---|---|---|
| Q2 2026 (3M) | $44,586k | $234,066k | **19.05%** |
| H1 2026 (6M) | $108,249k | $434,414k | **24.92%** |
| FY2025 | $199,042k | $601,800k | **33.07%** |

Both 2026 readings are **above the 0.10 bar**, on both period bases. This matters because the thesis's
PIL-6 note turns on the datum **"Launch Services is 8.29% of SPCX consolidated revenue — below the 0.10
bar"**. That figure is SPCX-specific and is a property of **SPCX's revenue mix** (a large Connectivity
business), not of launch. Applied to RKLB the identical construction gives **19.05% (3M) / 24.92% (6M)** —
**2.3x to 3.0x the SPCX figure and above the bar on both bases.** The "threshold above the datum" reasoning
does not transfer to the universe; it holds at one issuer.

**The pass-through test, which PIL-6 can carry.** PIL-6's independent falsifier is *"a demonstrated fall in
revenue per launch at least as large as the fall in cost per launch"*. At RKLB: cost per launch **fell 12.0%**
($5.0M → $4.4M, Q2 2025 → Q2 2026) while revenue per launch **ROSE 15.2%** ($7.9M → $9.1M). **No
pass-through. The falsifier does not fire, and the direction is the opposite of pass-through** — the
retained value widened from $2.9M to $4.7M per launch. Note the cost side of this comparison is a
**DISCLOSED** issuer metric and the revenue side likewise; neither is my derivation.

## 5. DA-23 / DA-24 residuals, and the DA-29 circularity rule

### DA-24 — `CLEAN`, and the check was EXERCISED

gross profit − **EXCLUSIVE** opex (the `Total operating expenses` line, which excludes cost of revenues),
against the filed operating loss, 4 of 4 periods:

| Period | Gross profit | Exclusive opex | Difference | Filed operating loss |
|---|---|---|---|---|
| Q2 2026 | 84,576 | 142,090 | (57,514) | **(57,514)** ✓ |
| Q2 2025 | 46,388 | 106,027 | (59,639) | **(59,639)** ✓ |
| H1 2026 | 161,069 | 274,552 | (113,483) | **(113,483)** ✓ |
| H1 2025 | 81,635 | 200,462 | (118,827) | **(118,827)** ✓ |

**4 of 4 EXACT.** The **INCLUSIVE** pairing (`us-gaap:CostsAndExpenses`, which includes cost of sales) gives
84,576 − 291,580 = **(207,004)** — false, as the rule says it must be. **The opex definition used
throughout is the exclusive one.** No non-operating item is inside RKLB's operating_income on these
periods, so **DA-24 does not fire at RKLB, and this is a passed check rather than an unengaged one.**

### DA-23 — FIRES, and only the component identity detects it

The served metrics block returns `operating_income 57,514,000` and `net_income_loss 49,258,000`, both
**positive**, against filed **(57,514)k** and **(49,258)k**, both negative
([📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6)). Magnitudes identical, sign stripped — the `|x|`
signature, not an inversion.

**It is invisible to every heuristic**: RKLB has **no period with positive operating income** in any filing
reached, so "operating income is positive" looks ordinary. The component identity is what exposes it, and it
exposes it twice over — once in the metrics block (sign), once in the ratio block (below).

### The served ratio block: three period conventions on one ticker

Ten rows served. **Every non-null `operating_margin` is positive** (0.2735, 0.2794, 0.3803, 0.4212, [null],
0.7325, 0.4079, 0.5889, 0.6658, 0.7663) for an issuer with no profitable period. Recomputed against filed
cells:

| Served row | Field | Served | Recomputed | Verdict |
|---|---|---|---|---|
| 2026 Q1 | `gross_margin` | 0.3818 | 76,493 / 200,348 = 38.18% — **own quarter** | round-exact |
| 2026 Q1 | `operating_margin` | 0.2794 | 55,969 / 200,348 = 27.9359% → 0.2794 — **own quarter** | round-exact |
| 2026 Q2 | `gross_margin` | 0.3708 | 161,069 / 434,414 = 37.0772% — **HALF-YEAR on a Q2 row** | round-exact |
| 2026 Q2 | `net_margin` | 0.2924 | 127,030 / 434,414 = 29.2417% — **prior-year HALF-YEAR net loss over CURRENT half-year revenue** | round-exact |
| 2026 Q2 | `operating_margin` | 0.2735 | nearest filed pair 118,827 / 434,414 = 27.3562% — needs **truncation**, which this row's `gross_margin` does not use | **UNRESOLVED** |
| 2025 Q4 | `operating_margin` | 0.3803 | 228,838 / 601,800 = 38.026% — **FULL-YEAR on a Q4 row** | round-exact |
| 2025 Q4 | `gross_margin` | 0.3443 | 207,181 / 601,800 = 34.427% — **FULL-YEAR** | round-exact |

The Q4 rows carry annual figures: the Q4 2025 row's revenue (601,799) equals the sum of the filed annual
segment revenues (199,042 + 402,757), and the Q4 2024 row's (436,214) equals 125,376 + 310,838. **DA-26
fires at RKLB on the Q4 rows.**

**The 2026 Q2 `operating_margin` is called `UNRESOLVED` deliberately.** Its nearest filed pair needs a
4th-decimal truncation while `gross_margin` and `net_margin` on the *same row* both round correctly. A pair
that fits only under a convention the row itself contradicts is exactly the **plausible-but-wrong**
identification the brief names as the dangerous failure mode, so it is not named. **What IS certain: no
numerator-over-denominator pair drawn from filed cells can make RKLB's operating margin positive.** The sign
defect is certain even where the construction is not.

### The DA-29 circularity rule — applied to every reconciliation above

> *If any term appears nowhere in the source, the check is a back-solve.*

**I ran this rule on all four reconciliations in this artifact.** Its findings:

1. **The component identity (S5).** Every term — gross profit, exclusive opex, operating loss — is a filed
   cell on [📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6). **Not a back-solve.**
2. **The cost-leg reconciliation (S3).** Every term is filed: the per-launch cells, the mission counts, and
   the audited segment cost of revenue. **Not a back-solve** — but note the mission count for Q1 2025 (5)
   and Q1 2026 (6) is inferred as H1 minus Q2 launches, and is confirmed at Q1 2026 by the independently
   filed count on [📄 RKLB 10-Q p.31](https://agentii.ai/v/RKLB/sec104/31). Q1 2025's count of 5 is
   inferred only; it is *stable* (it is the value that reproduces the thesis's +0.4%), but a single
   inferred term is a weakened check and I mark it as such.
3. **The revenue-leg reconciliation (S3).** Same terms, same status. **Not a back-solve.**
4. **The served-ratio reconstructions (S5).** Here the rule bites: the 2026 Q2 `operating_margin` closes only
   if a truncation convention is *assumed*, and that assumption appears nowhere in the source.
   **It is a back-solve, and it is recorded `UNRESOLVED` for exactly that reason.**

### Also carried

- **DA-25** — the per-launch metrics are issuer normalisations; the reconciliation above is possible only
  because the multiplicand is separately filed. Where it is not (Q1 2025's mission count), the check
  weakens. The metric is never used here as a substitute for the audited segment table.
- **DA-30** — reported both bases wherever they exist: segment vs consolidated (S2), exclusive vs inclusive
  opex (S5), quarter vs half-year (S5).

## 6. What is UNRESOLVED

| # | Item | Class | Resolving disclosure |
|---|---|---|---|
| 1 | RKLB 2026 Q2 served `operating_margin` 0.2735 — construction | `UNRESOLVABLE-FROM-PLATFORM` | the layer's numerator and denominator cells, and one stated rounding convention. Two sibling cells on the same row round; this one needs truncation. |
| 2 | PIL-2's specified metric (launch segment **operating** margin vs non-launch) at RKLB | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a segment operating-income table. RKLB files segment gross profit only, so `count_..._launch_segment_operating_margin_exceeds_non_launch` is **NON-FORMABLE** at RKLB — the gross-margin differential (S3) is a proxy, and it is negative in 3 of 7 periods. |
| 3 | PIL-6's demanded quantity at RKLB | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a customer-side programme-cost base. |
| 4 | Q1 2025 mission count (5) | not read in this pass | an explicitly filed Q1 2025 launch count. Inferred as H1 minus Q2; stable, and marked a weakened term in S5. |
| 5 | PIL-5's "4 of 6" | **resolved — a miscount** | the thesis's own six listed values give **3 of 6** above the 5% bar. |

## Sources

| Source | Used for |
|---|---|
| [📄 RKLB 10-K p.107](https://agentii.ai/v/RKLB/sec87/107) | FY2025 / FY2024 / FY2023 segment revenue, cost of revenue, gross profit — the 9 annual cells in S3 |
| [📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6) | Consolidated statements of operations: the component identity (S5), the consolidated margin (S2) |
| [📄 RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32) | Q2 2026 / Q2 2025 / H1 2026 / H1 2025 segment table — the 8 interim cells in S3 |
| [📄 RKLB 10-Q p.33](https://agentii.ai/v/RKLB/sec109/33) | Products/services split of the segment cells |
| [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37) | Revenue and cost per launch, Q2 2026 / Q2 2025 / H1 2026 / H1 2025; mission counts; the two HASTE missions |
| [📄 RKLB 10-Q p.31](https://agentii.ai/v/RKLB/sec104/31) | Revenue and cost per launch, Q1 2026 / Q1 2025; the verbatim metric definitions; build and launch counts |
