---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: cross
ticker: FLY
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
    chosen_reading: "The platform serves a filed negative as a positive of identical magnitude. FLY's served layer strips the sign of BOTH operating_income (+95,197,000 against filed (95,197)) and net_income (+92,319,000 against filed (92,319)) and then serves |loss| / revenue as a 'margin' worth 96% to 350% of revenue. Every figure here is recomputed from filed cells."
  - da_id: DA-24
    chosen_reading: "Non-operating contamination of operating_income. Tested, not assumed: gross profit - EXCLUSIVE opex closes to the filed operating line in 4 of 4 periods, despite a non-operating wedge that FLIPS SIGN between the two years (+2,878 in Q2 2026, -9,428 in Q2 2025). operating_income is uncontaminated on these periods."
  - da_id: DA-25
    chosen_reading: "Normalised per-unit metrics not reproducible from audited tables. FLY files NO launch count and NO cost per launch, so the per-launch reconciliation is UNEXERCISED here, not clean. Its only launch-linked numerator is a contract BACKLOG, which is a forward contract quantity and not a flown count; using it as a per-launch denominator would be a back-solve."
  - da_id: DA-26
    chosen_reading: "Annual figures mislabelled as quarterly. FLY is the brief's COUNTEREXAMPLE and remains so: its served rows carry interim cumulative figures (6M, 9M), never annual ones. The defect FLY exhibits is cumulative-vs-quarterly, which is a different and strictly milder one. NOT reported as universal."
  - da_id: DA-27
    chosen_reading: "Fiscal-period labels derived from the calendar quarter. FLY's most recent served row carries the QUARTER in `revenues` (117,683) and the HALF-YEAR in all three margins. The period basis is stated in-line on every figure below."
  - da_id: DA-28
    chosen_reading: "Capital-structure discontinuity around an IPO invalidates share-count detectors. FLY's weighted-average shares run 13,877k -> 161,784k on the 3M basis (11.7x) around its 2025 IPO, which the one-time IPO cost line dates. No share-count-derived detector is used anywhere in this artifact."
  - da_id: DA-29
    chosen_reading: "A reconciliation that closes is not thereby a check; a term appearing nowhere in the source makes it a back-solve. Applied to every reconciliation here and reported in S6. Two of FLY's four reconciliations are PARTIAL back-solves and are labelled so."
  - da_id: DA-30
    chosen_reading: "Two bases on one concept collapsed without a basis field. FLY files TWO BASES on the same three line labels in ONE 10-Q (income statement vs CODM expense-category table), which is the sharpest DA-30 instance in the trio. Both bases are reported side by side everywhere they exist."
evidence_grade: DEMONSTRATED
citations:
  - figure: "FLY condensed consolidated statements of operations: revenue 117,683 / 15,549 / 198,562 / 71,404; cost of sales 93,808 / 11,554 / 157,226 / 65,189; gross profit 23,875 / 3,995 / 41,336 / 6,215; R&D 71,532 / 45,774 / 139,041 / 93,786; SG&A 47,540 / 12,571 / 93,160 / 25,323; total operating expenses 119,072 / 58,345 / 232,201 / 119,109; loss from operations (95,197) / (54,350) / (190,865) / (112,894); net loss (92,319) / (63,778) / (188,995) / (123,871); EPS (0.57) / (5.78) / (1.18) / (11.17); weighted-average shares 161,784 / 13,877 / 160,711 / 13,659."
    ticker: "FLY"
    form_type: "10-Q"
    citation_id: "sec21"
    page_no: 6
    url: "https://agentii.ai/v/FLY/sec21/6"
    located_via: "read_source_pages"
  - figure: "FLY revenue disaggregation: Launch 9,400 / 6,349 / 22,652 / 11,519; Spacecraft Solutions 108,283 / 9,200 / 175,910 / 59,885."
    ticker: "FLY"
    form_type: "10-Q"
    citation_id: "sec21"
    page_no: 15
    url: "https://agentii.ai/v/FLY/sec21/15"
    located_via: "read_source_pages"
  - figure: "FLY segment determination: the Company operates in ONE operating segment and as a single reportable segment; segment reporting refined in Q1 fiscal 2026 with prior periods recast."
    ticker: "FLY"
    form_type: "10-Q"
    citation_id: "sec21"
    page_no: 32
    url: "https://agentii.ai/v/FLY/sec21/32"
    located_via: "read_source_pages"
  - figure: "FLY CODM expense-category table: revenue 117,683 / 15,549 / 198,562 / 71,404; SBC (17,027) / (760) / (29,539) / (1,191); D&A (9,309) / (3,920) / (20,762) / (7,916); amortisation of acquired intangibles (5,000) / - / (10,000) / -; cost of sales (92,507) / (10,621) / (154,132) / (63,272); R&D (56,501) / (42,666) / (113,538) / (87,602); SG&A (29,889) / (10,165) / (56,823) / (20,097); interest income 4,336 / 1,761 / 10,310 / 2,789; interest expense (1,717) / (6,998) / (5,399) / (13,190); one-time IPO costs - / (1,767) / - / (4,220); transaction-related (2,724) / - / (4,633) / -; consolidated net loss (92,319) / (63,778) / (188,995) / (123,871). Footnote 2: cost of sales excludes depreciation and amortisation and interest expense."
    ticker: "FLY"
    form_type: "10-Q"
    citation_id: "sec21"
    page_no: 33
    url: "https://agentii.ai/v/FLY/sec21/33"
    located_via: "read_source_pages"
  - figure: "FLY platform disclosure: single reportable segment; Launch (Alpha, Eclipse) and Spacecraft Solutions (Blue Ghost, Elytra); SciTec acquisition."
    ticker: "FLY"
    form_type: "10-Q"
    citation_id: "sec21"
    page_no: 34
    url: "https://agentii.ai/v/FLY/sec21/34"
    located_via: "read_source_pages"
  - figure: "FLY backlog: total 1,468,081 thousand at 30 June 2026 against 1,351,054 thousand at 31 December 2025; multi-launch agreement backlog 403,070 against 344,800."
    ticker: "FLY"
    form_type: "10-Q"
    citation_id: "sec21"
    page_no: 36
    url: "https://agentii.ai/v/FLY/sec21/36"
    located_via: "read_source_pages"
key_metrics:
  gross_margin_pct_3m: 20.29
  operating_margin_pct_3m: -80.90
  r_and_d_pct_of_revenue_3m: 60.78
  total_opex_pct_of_revenue_3m: 101.18
---

# FLY — ratio analysis: the margin ladder, the per-launch reconciliation, and the demand-side share

**Pillars served: PIL-3, PIL-5, PIL-6** (spec §3 purpose tag `(P2, P5, P6)`; the ladder in S2 also carries
PIL-2). The frontmatter carries `cross` because the field admits a single value or `cross`, and this
artifact spans three pillars.

## 0. The finding

**FLY is the worst margin in the verified universe, and it is a manufacturer — which falsifies the
"worst margin belongs to a network operator with one customer" anchor.** Gross margin **20.29% (3M) /
20.82% (6M)**, R&D intensity **60.78% (3M) / 70.02% (6M) — the highest of the three manufacturers checked on
both bases**, operating margin **−80.90% (3M) / −96.12% (6M)**. FLY sits below every launcher in the ladder
because at FLY the **operating expense base is 101.18% of revenue** (119,072 / 117,683): gross profit is
real and entirely consumed before a dollar of R&D is funded.

**Second finding: FLY files two bases on the same three line labels in one 10-Q, and the spread between them
is 6.00 pp on a single quarter.** The income statement's cost of sales (93,808) is inclusive of share-based
compensation, depreciation, intangible amortisation and transaction costs; the CODM table's (92,507) is
exclusive of them. Q2 2026 gross margin is **20.29%** on the first and **21.39%** on the second; Q2 2025 is
**25.69%** against **31.69%** — a **6.00 pp spread**. The brief's headline "gross margin 20.3%" is the
*inclusive* basis, and the divergence is largest in the comparison year, which is the year a trend reader
divides by.

**Third finding: 97.0% of FLY's Q2 revenue growth is the acquired entity's segment.** Spacecraft Solutions
rose 9,200 → 108,283 (+99,083) inside total growth of 102,134. **Launch grew 3,051, which is 3.0% of the
growth.** This is FLY's instance of the brief's "+$1,824M is not evidence of migration" correction: the
segment-mix story at FLY in Q2 2026 is an acquisition, not a launch business.

**Fourth finding: FLY's served layer strips the sign of a loss and then serves it as a margin.** Served
`operating_margin` **0.9612** and `net_margin` **0.9518** are |loss| ÷ revenue — **96.12% and 95.18% of
revenue**, reported as positive margins, on a row whose `revenues` cell is the *quarter* while all three
margins are the *half-year*.

## 1. The acceptance test — run, and stated

> Accept an identification **only if it is (a) exact, (b) stable across periods, and (c) consistent with a
> formula the skill specifies or a basis the issuer files.** Everything else is `UNRESOLVED`, never
> "probably fine".

**This test was run on every identification in this artifact.** Its results are the spine of S3, S5 and S6.

The *exactness* limb is the operative one. A ~2,500-candidate expression sweep over 36 filed cells at **0.5%
tolerance** produces **6–9 coincidental hits per metric**; at **4-decimal** exactness across ~1,300 ordered
filed-cell pairs the expected coincidence count is below one. **A 4-dp exact match on a filed cell pair is
admissible; a 0.5%-tolerant match is not.** Every identification below is stated at 4 dp, and the two that
cannot be closed on filed cells are called out rather than named.

FLY's served layer carries **two** byte-duplicative pairs, both of which are why no served ratio is an input
to this artifact: `quick_ratio == cash_ratio` in **5 of 5** comparable rows, and `roic == roa` in **5 of 5**
rows. A layer that returns the same value under two different names twice over is not a source.

## 2. The margin ladder, ordered by distance from programme risk

Ordering criterion: **the share of the issuer's P&L exposed to the outcome of any single programme**,
farthest first. Rows 1–10 are inherited from `sector-overview` §4; rows 11 and 13–18 were **verified here**
and row 17 is **FLY's rung**.

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
| 11 | demand-owning operator | SPCX Connectivity | segment op margin | **+38.59%** | Q2 2026 3M | DEMONSTRATED |
| 12 | manufacturer (reference) | SPCX Space | segment **gross** margin | 65.80% | 3M | DEMONSTRATED |
| 13 | launcher/space mfr | RKLB (consolidated) | op margin | −24.57% | 3M | DEMONSTRATED |
| 14 | launcher/space mfr | SPCX AI | segment op margin | −49.08% | 3M | DEMONSTRATED |
| 15 | launcher | SPCX Space (launch + dev) | segment op margin | −56.34% | 3M | DEMONSTRATED |
| 16 | launcher/space mfr | LUNR | op margin | −56.3% | inherited | CLAIMED |
| 17 | **launcher/space mfr** | **FLY** | **op margin** | **−80.90%** | **3M** | **DEMONSTRATED** |
| 18 | manufacturer (reference) | RKLB Launch Services | segment **gross** margin | 42.86% | 3M | DEMONSTRATED |

FLY's rung recomputed from filed cells: 117,683 − 93,808 = 23,875 gross profit;
23,875 − 119,072 = **(95,197)**; 95,197 / 117,683 = **−80.8950% → −80.90%** on the 3M basis
([📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6)). On the 6M basis it is
190,865 / 198,562 = **−96.1235% → −96.12%**.

### The two anchors, tested

**(a) "Component suppliers earn ~2x the primes they supply" — HOLDS.** Suppler tier mean
(32.9 + 25.5 + 19.3 + 19.1 + 17.0)/5 = **22.76%** against prime tier mean (12.4 + 11.4 + 11.1 + 10.1)/4 =
**11.25%**: **2.02x**. It is a tier central tendency, not a pairwise law (TER 32.9% is 2.65x LMT; WWD ~17%
is 1.68x RTX).

**(b) "The worst margin in the universe belongs to a network operator with one customer" — FALSIFIED as
stated, and FLY is the counterexample row.** The worst **verified** margin in the ladder is **FLY's
−80.90%**, a launch-and-spacecraft **manufacturer**, 24.56 pp below the next-worst verified row. The
one-customer network operator (GSAT, +7.4%) is the **thinnest positive operator margin** and the **best** of
the six loss-exposed rungs. The anchor's entity identification is right and its ordering claim is inverted:
**the bottom of the ladder is manufacturers, not operators.**

### The ordering is not monotone — it is bimodal

Both ends carry high margins (Connectivity **+38.59%**; TER **32.9%**) and the **middle rungs are negative**
(RKLB −24.57%, SPCX AI −49.08%, SPCX Space −56.34%, FLY −80.90%). The value pool sits with the party that
**owns the demand** and the party that **sells components into every programme**. **FLY sits in the hole** —
and unlike SPCX, FLY has no high-margin segment to be dragged down by: it is a **single reportable
segment**, so the whole company is the launch-and-spacecraft rung.

### FLY's own rung is the one rung the ladder cannot take apart

`The Company has determined that it operates in one operating segment and as a result, manages its
operations and allocates resources as a single operating segment` — and in Q1 fiscal 2026 it "refined its
segment reporting", recasting prior periods ([📄 FLY 10-Q p.32](https://agentii.ai/v/FLY/sec21/32));
`We operate as a single reportable segment` with Launch (Alpha, Eclipse) and Spacecraft Solutions (Blue
Ghost, Elytra) as platforms, not segments
([📄 FLY 10-Q p.34](https://agentii.ai/v/FLY/sec21/34)). **PIL-2's specified metric — launch segment
operating margin vs non-launch segment operating margin — is `NON-FORMABLE` at FLY for a second and
different reason than at RKLB** (RKLB files segment gross profit but not segment operating income; FLY files
one segment). The universe consequence is stated in S3.

### FLY's margin is a cost-structure result, not a pricing result

| Intensity, 3M basis (Q2 2026) | FLY | RKLB | SPCX |
|---|---|---|---|
| Gross margin | **20.29%** | 36.14% | 55.27% |
| R&D / revenue | **60.78%** | 35.22% | 45.41% |
| SG&A / revenue | 40.39% | 25.49% | 11.67% |
| Total opex / revenue | **101.18%** | 60.71% | 56.51% |
| Operating margin | **−80.90%** | −24.57% | −1.83% |

**FLY has the highest R&D intensity of the three manufacturers on both period bases** — 60.78% (3M) and
**70.02% (6M)** against RKLB's 35.22% / 37.51% and SPCX's 45.41% / 56.46% — and the **lowest** gross margin on
both. The R&D intensity is the **SPCX Space pattern taken to its end**: at SPCX the launch segment's R&D is
111.85% of *segment* revenue while the company is carried by a high-margin segment; at FLY there is no other
segment, so a 60–70% R&D load lands on a 20% gross margin and produces a −81% operating margin. **The
brief's 60.8% figure is confirmed at 60.78% on the 3M basis, and its basis is the quarter — the 6M figure is
70.02%, 9.24 pp higher.**

## 3. The per-launch reconciliation — `UNEXERCISED` at FLY

PIL-5's reconciliation requires a filed per-launch quantity. **FLY files no launch count and no cost per
launch in any period reached.** The resolving disclosure is a launches-flown count paired with a launch
cost of revenue, filed or disclosed. The test therefore **`UNEXERCISED`** — not clean, not passed.

**Why the available substitute is inadmissible.** FLY's only launch-linked numerator is a **contract
backlog**: multi-launch agreement backlog **403,070** thousand at 30 June 2026 against **344,800** thousand
at 31 December 2025 ([📄 FLY 10-Q p.36](https://agentii.ai/v/FLY/sec21/36)), against total backlog
1,468,081 and 1,351,054.

| Quantity | 30 Jun 2026 | 31 Dec 2025 | Change |
|---|---|---|---|
| Multi-launch agreement backlog | 403,070 | 344,800 | **+58,270 (+16.90%)** |
| Total backlog | 1,468,081 | 1,351,054 | +117,027 (+8.66%) |
| Multi-launch share of backlog | **27.46%** | 25.52% | +1.94 pp |

A backlog is a **forward contract quantity**, not a flown count and not a price: dividing it by missions
would be a **back-solve** under DA-29 (the denominator appears nowhere in the source). It is reported as a
demand-side contract signal and is **not** used to form a per-launch figure. **Its one admissible reading:
FLY's launch-contract backlog grew 1.95x faster than total backlog, so the launch side of FLY's order book
is gaining share of its own backlog** — the direction PIL-2's migration claim would predict, on contract
quantity rather than margin.

### The revenue leg, and FLY's contribution to PIL-3

FLY disaggregates Launch revenue (9,400 / 6,349 / 22,652 / 11,519) with **no cost** attached
([📄 FLY 10-Q p.15](https://agentii.ai/v/FLY/sec21/15)), and the disaggregation ties to the income statement
**4 of 4 exactly**:

| Period | Launch | Spacecraft Solutions | Sum | Filed revenue |
|---|---|---|---|---|
| Q2 2026 (3M) | 9,400 | 108,283 | **117,683** | 117,683 ✓ |
| Q2 2025 (3M) | 6,349 | 9,200 | **15,549** | 15,549 ✓ |
| H1 2026 (6M) | 22,652 | 175,910 | **198,562** | 198,562 ✓ |
| H1 2025 (6M) | 11,519 | 59,885 | **71,404** | 71,404 ✓ |

**FLY adds a launch-revenue point to the universe and no launch-cost point to it.** PIL-3's claim that the
curve is `CLAIMED` and not `DEMONSTRATED` therefore survives a third issuer: **Electron remains the only
vehicle in this trio with a demonstrated marginal cost.** FLY's launch growth — 6,349 → 9,400 (+48.05%) on
3M, 11,519 → 22,652 (+96.65%) on 6M — is a **revenue** rise with no disclosed cost against it, so it cannot
distinguish a falling cost curve from a rising price.

**And the growth is not the launch business** (S4): of Q2's +102,134 total revenue increase, **+99,083
(97.0%) is Spacecraft Solutions**, the segment the SciTec acquisition sits in, against **+3,051 (3.0%) from
Launch**. On 6M the split is 116,025 of 127,158 = **91.2%** against 11,133 = **8.8%**. **This is the FLY
instance of the brief's "+$1,824M is not evidence of migration — it exists because an entity was
acquired."** FLY's transition from a 41% launch-revenue company to a 8% one happened in the space of a year
and it is an M&A fact, not a launch-market fact.

## 4. The demand-side programme-cost shares (PIL-6)

PIL-6's metric is `launch_cost_share_of_total_program_cost_at_universe_demand_side_names`, bar **0.10**,
op `>`. The demanded quantity needs the **customer's** programme-cost base. **No issuer files one.**
PIL-6 instructs: *IF THE QUANTITY IS NON-FORMABLE, RECORD NON-FORMABLE — NOT PASS.*

**→ PIL-6's metric is `NON-FORMABLE`.** Resolving disclosure: a customer-side programme-cost base (capex or
total programme value) set against the launch price paid. Class:
`UNRESOLVABLE-FROM-PUBLIC-SOURCES`.

The **analogous within-issuer construction** — Launch revenue as a share of the issuer's own revenue — is
computable, is **not** the P6 quantity, and is reported as a labelled proxy:

| Issuer | 3M | 6M | vs the 0.10 bar |
|---|---|---|---|
| **FLY** | **7.99%** | **11.41%** | **crosses between bases** |
| SPCX | 8.29% | 7.82% | below on both |
| RKLB | 19.05% | 24.92% | above on both |

FLY: 9,400 / 117,683 = **7.9876% → 7.99%**; 22,652 / 198,562 = **11.4073% → 11.41%**.

**FLY is the sharpest demonstration that the bar is not measuring launch.** The identical construction on
the identical issuer flips from below the bar to above it **purely by changing the period basis** — 7.99% on
3M, 11.41% on 6M — because Launch revenue grew 96.65% over the half while total revenue grew 178% and the
two periods weight the pre-growth and post-growth quarters differently. The bar's verdict at FLY is
therefore a statement about **when you look**, not about launch economics. Across the trio, the 3M ordering
is SPCX (8.29%) > FLY (7.99%) and the 6M ordering reverses to FLY (11.41%) > SPCX (7.82%). **A metric whose
cross-issuer ordering reverses on basis alone, and whose bar crossing flips on basis alone, is not a
discriminator between issuers.**

### The pass-through test, run on FLY's own numbers

PIL-6's independent falsifier is *"a demonstrated fall in revenue per launch at least as large as the fall
in cost per launch"*. At FLY the cost side is not filed (S3), so the test **cannot run**:
`UNEXERCISED`, not CLEAN. **But the test can be run in the negative direction with the data that does
exist**: FLY's Launch revenue rose 96.65% over the half while the launch-side cost is undisclosed, so
**no fall in revenue per launch can be demonstrated, and none is claimed.** The pass-through falsifier
therefore does not fire at FLY — on absence of evidence, which is exactly why it is recorded as
`UNEXERCISED` rather than as a pass.

## 5. DA-23 / DA-24 residuals, and the DA-29 circularity rule

### DA-24 — `CLEAN`, and the check was EXERCISED in 4 of 4

gross profit − **EXCLUSIVE** opex (R&D + SG&A; FLY has no other operating expense line, and their sum equals
the filed `Total operating expenses` exactly), against the filed operating line:

| Period | Gross profit | Exclusive opex | Difference | Filed loss from ops |
|---|---|---|---|---|
| Q2 2026 | 23,875 | 119,072 | **(95,197)** | **(95,197)** ✓ |
| Q2 2025 | 3,995 | 58,345 | **(54,350)** | **(54,350)** ✓ |
| H1 2026 | 41,336 | 232,201 | **(190,865)** | **(190,865)** ✓ |
| H1 2025 | 6,215 | 119,109 | **(112,894)** | **(112,894)** ✓ |

**4 of 4 EXACT**, and R&D + SG&A = total operating expenses exactly in all four columns
(71,532 + 47,540 = 119,072; 45,774 + 12,571 = 58,345; 139,041 + 93,160 = 232,201; 93,786 + 25,323 = 119,109).
The **INCLUSIVE** pairing gives 23,875 − (93,808 + 119,072) = **(189,005)**, which is not the filed (95,197).
**The opex definition used throughout is the exclusive one, named in-line.**

**Why this is a genuine test at FLY and not a formality.** FLY's non-operating wedge is large and **flips
sign between the two years**: Q2 2026 net loss (92,319) against operating loss (95,197) → **+2,878** of
non-operating income; Q2 2025 (63,778) against (54,350) → **−9,428**; H1 2025 → **−10,977**. The largest
visible movers in the CODM table are interest expense (6,998 → 1,717, −75.5%) and interest income
(1,761 → 4,336). **The component identity closes on the operating line anyway, despite a ~12.3M sign
flip** — which is exactly what distinguishes an uncontaminated `operating_income` from a contaminated one.
**DA-24 does not fire at FLY, and this is a passed check rather than an unengaged one.**

### DA-23 — FIRES, and FLY is the deepest case in the trio

FLY's served layer strips the sign of **both** lines: `operating_income +95,197,000` against filed
(95,197)k and `net_income +92,319,000` against filed (92,319)k. Then, because a **margin** is formed
afterwards, the strip is served as a *ratio*:

| Served field (row labelled Q2 2026) | Served | Recomputed from filed cells | Verdict |
|---|---|---|---|
| `operating_margin` | **+0.9612** | 190,865 / 198,562 = **96.1235%** — **6M/6M** | rounded-exact |
| `net_margin` | **+0.9518** | 188,995 / 198,562 = **95.1821%** — **6M/6M** | rounded-exact |
| `gross_margin` | **+0.2082** | 41,336 / 198,562 = **20.8176%** — **6M/6M** | rounded-exact |
| `revenues` (same row) | **117,683** | **the QUARTER** | — |

**All three margins on the row are half-year ratios; the row's own revenue cell is the quarter.** Both
periods are filed and the payload says neither. **Every non-null FLY `operating_margin` served is `|operating
loss| / revenue`** — the served "margins" are **96% to 350% of revenue**, positive. The deepest reading is
Q2 2025's **3.4954** (54,350 / 15,549), served as a positive operating margin of 349.54%.

**The brief's gross-margin headline is a different basis than the served value.** The brief's **20.3%** is the
**3M filed** figure (23,875 / 117,683 = 20.2888% → 20.29%); the served `gross_margin` **0.2082** is the **6M**
figure (20.8176%). Both are filed; **they differ by 0.53 pp and the payload does not say which it served.**
The brief's value is the better-grounded of the two, and it is the one used in this artifact's ladder
comparison in S2.

**Period content varies row to row within FLY's own payload.** Reconstructed against the payload's own
cells: the row labelled **Q3 2025** carries **cumulative 9M** constructions (the served `operating_margin`
1.7134 and `net_margin` 2.5179 reproduce as |loss| ÷ **102,182**, a nine-month revenue magnitude, giving
1.7135 by rounding and 1.7134 only by truncation — **one served row using two rounding conventions**), while
the rows labelled **Q1 2026** and **Q4 2025** carry **discrete-quarter** constructions. **Four rows, three
period contents, one field name.** State the basis or the number is not a fact about FLY.

### The DA-30 instance that is issuer-filed, in one 10-Q, on the same three line labels

FLY presents the same revenue with **two different cost-of-sales bases** in one filing: the income statement
([📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6)) and the CODM expense-category table
([📄 FLY 10-Q p.33](https://agentii.ai/v/FLY/sec21/33)), whose footnote 2 states that *cost of sales
excludes depreciation and amortisation, and interest expense, which are presented separately*.

| Gross margin, both bases, same issuer, same quarter | Inclusive (p.6) | CODM / exclusive (p.33) | **Spread** |
|---|---|---|---|
| Q2 2026 (3M) | 23,875 / 117,683 = **20.29%** | 25,176 / 117,683 = **21.39%** | 1.10 pp |
| **Q2 2025 (3M)** | 3,995 / 15,549 = **25.69%** | 4,928 / 15,549 = **31.69%** | **6.00 pp** |
| H1 2026 (6M) | 41,336 / 198,562 = **20.82%** | 44,430 / 198,562 = **22.38%** | 1.56 pp |
| H1 2025 (6M) | 6,215 / 71,404 = **8.70%** | 8,132 / 71,404 = **11.39%** | 2.69 pp |

**A 6.00 pp spread on a single quarter, from the same issuer, in the same document, on a line with the same
name.** The 2025 columns of the CODM table are labelled **"(Recast)"** — FLY restated them when it refined
segment reporting in Q1 2026 — so the 6.00 pp spread sits in the **comparison** year, which is the year a
trend reader divides by. **Both bases are reported here; neither is quoted alone.** This is the sharpest
DA-30 instance in the trio because it is the issuer's own filing rather than a platform artefact.

### DA-29 — the circularity rule, applied to every reconciliation above

> *If any term appears nowhere in the source, the check is a back-solve.*

**I ran this rule on all five reconciliations in this artifact.** Its findings:

1. **The component identity (S5).** Every term is a filed cell on
   [📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6). **Not a back-solve.**
2. **The revenue disaggregation tie, 4 of 4 (S3).** Every term is filed on
   [📄 FLY 10-Q p.15](https://agentii.ai/v/FLY/sec21/15). **Not a back-solve.**
3. **The two-basis CODM bridge (S5).** Every term is filed on p.6 and p.33, and the bridge **closes exactly
   in 3 of 4 columns**: Q2 2025 (6,447 = 760 + 3,920 + 1,767), H1 2025 (13,327 = 1,191 + 7,916 + 4,220) and
   H1 2026 (64,934 = 29,539 + 20,762 + 10,000 + 4,633) — where each left side is the sum of the three
   line-by-line differences between the two bases and each right side is the sum of the excluded items.
   **Not a back-solve on those three columns.**
4. **Q2 2026's column of that same bridge — PARTIAL BACK-SOLVE, and it is labelled so.** The three
   line-by-line differences sum to **33,983** while the excluded items sum to **34,060**: a residual of
   **exactly 77**. The filing does not say where the 77 sits. **A candidate placement (the interest-expense
   line, whose two bases differ by 77) is an inference the source does not state, so I do not place it.**
   What IS established by arithmetic on filed cells: the **H1 2026 column closes exactly**, so if the
   excluded-item set is the same in both quarters — which the line labels assert and the filing does not
   prove — then **Q1 2026's residual is exactly −77 and the 77 reverses within the half.** The reversal is
   `DERIVED`; the placement is `UNRESOLVED`.
   **The methodological point stands without the attribution: FLY's two-basis reconciliation closes on the
   cumulative column and does not close on the discrete-quarter column.** A reader who checks only the
   half-year sees a perfect tie; the within-half placement difference is visible **only** at quarter
   granularity.
5. **The Spacecraft-Solutions share of growth (S3).** Every term is filed on p.15. **Not a back-solve.**

### Also carried

- **DA-25** — FLY files no per-unit metric on launch at all. The per-launch test is `UNEXERCISED`, and the
  multi-launch **backlog** is refused as a denominator for exactly this reason.
- **DA-26 — FLY is the brief's counterexample and remains so.** FLY's served rows carry **interim cumulative**
  figures (6M, 9M), **never annual ones**. The defect FLY exhibits is cumulative-vs-quarterly, which is a
  **different and strictly milder** class than annual-as-quarterly (19 of 20 issuers; RKLB the instance where
  a Q4-labelled row's revenue equals a filed full-year total). **Not reported as universal.**
- **DA-28** — weighted-average shares run **13,877k → 161,784k** on the 3M basis (11.7x) and EPS runs
  $(5.78) → $(0.57). The one-time IPO cost lines (1,767 in Q2 2025, 4,220 in H1 2025) date the event inside
   2025 and the SciTec transaction lines (2,724 in Q2 2026, 4,633 in H1 2026) date the acquisition inside
   2026. **No share-count-derived detector is used anywhere in this artifact, and `EPS × shares` is not used
  as a sign test.** Note that FLY's EPS and shares **are** mutually consistent — which is the trap, since
  consistency would have made the inadmissible check look admissible.
- **DA-27** — the Q2 2026 row's `revenues` is the quarter and its three margins are the half-year. Basis
  stated in-line throughout this artifact.

## 6. What is UNRESOLVED

| # | Item | Class | Resolving disclosure |
|---|---|---|---|
| 1 | The placement of the 77 residual in Q2 2026's two-basis bridge | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a line-level allocation of the excluded items (SBC, D&A, intangibles, transaction costs) to the three expense lines at quarter granularity. The reversal within the half is `DERIVED`; the placement is not. |
| 2 | FLY cost per launch, any period | `UNEXERCISED` (not CLEAN) | a launches-flown count paired with a launch cost of revenue. |
| 3 | PIL-6's demanded quantity at FLY | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | a customer-side programme-cost base. |
| 4 | PIL-2's specified metric at FLY | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | segment-level operating income. FLY reports **one** segment, so the launch-vs-non-launch comparison **cannot be formed** — `NON-FORMABLE`, not "equal by construction". |
| 5 | FLY's Launch-only gross margin | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | cost of revenue by platform (Alpha / Eclipse vs Blue Ghost / Elytra). Launch revenue is disaggregated **without** cost, so the only launch margin obtainable is the company's single-segment one. |
| 6 | Attribution of the non-operating wedge's sign flip (+2,878 vs −9,428 on 3M) | not read in this pass | the CODM table's lines beyond `transaction-related`, which were not captured. The largest visible movers are stated in S5; no closure is claimed for the wedge. |
| 7 | DA-26 presence at FLY | **resolved — negative** | FLY's rows carry interim cumulative figures, never annual ones. FLY is the brief's counterexample and this pass re-confirms it. |

**One universe-level consequence, recorded here because FLY is where it becomes visible.** PIL-2's metric
`count_of_universe_issuers_where_launch_segment_operating_margin_exceeds_non_launch_segment_operating_margin`
(op `>`, threshold 0 — "A1b is TESTED here, not assumed") **is `<NON-FORMABLE` at FLY (one segment) and at
RKLB (segment gross profit only, no segment operating income)**. It is computable at exactly **one** issuer,
SPCX, and there the launch segment's **−56.34%** exceeds **neither** non-launch segment (+38.59%
Connectivity, −49.08% AI) nor their revenue-weighted aggregate
((1,656 − 1,257) / (4,291 + 2,561) = 399 / 6,852 = **+5.82%**). **The count is 0 of 1 computable — tested
on the only issuer where the test can run, and failing there.** A pillar whose supporting metric is
non-formable at two of three issuers and 0 at the third is not supported by the ratio layer; the gross-margin
proxy at RKLB (positive in 4 of 7 periods, negative in 3) is not stable enough to carry it either.

## Sources

| Source | Used for |
|---|---|
| [📄 FLY 10-Q p.6](https://agentii.ai/v/FLY/sec21/6) | Condensed consolidated statements of operations: the component identity (S5), the inclusive cost-of-sales basis, the non-operating wedge, EPS and share counts |
| [📄 FLY 10-Q p.15](https://agentii.ai/v/FLY/sec21/15) | Revenue disaggregation: Launch and Spacecraft Solutions, and the 97.0% / 3.0% split of Q2 growth (S3) |
| [📄 FLY 10-Q p.32](https://agentii.ai/v/FLY/sec21/32) | Single operating segment determination; the Q1 2026 segment-reporting refinement and the 2025 recast |
| [📄 FLY 10-Q p.33](https://agentii.ai/v/FLY/sec21/33) | CODM expense-category table: the exclusive cost-of-sales basis, the excluded items, and the four columns of the two-basis bridge (S5) |
| [📄 FLY 10-Q p.34](https://agentii.ai/v/FLY/sec21/34) | Single reportable segment; Alpha / Eclipse / Blue Ghost / Elytra platforms; SciTec acquisition |
| [📄 FLY 10-Q p.36](https://agentii.ai/v/FLY/sec21/36) | Backlog and multi-launch agreement backlog: the demand-side contract signal (S3) |
