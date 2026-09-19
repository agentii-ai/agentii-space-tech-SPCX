---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-1/PIL-6"
ticker: SPCX
skill: sotp-valuation
mode: methodology
generated_at: 2026-09-19T13:40:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07305f5d5391"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "Component identity shown in-line on every segment table: gross profit - opex = operating_income. SPCX files NO segment gross-profit subtotal, so gross profit is DERIVED. EPS x shares is inadmissible as a sign test; the gross-profit bound is the fallback."
  - da_id: "DA-06"
    chosen_reading: "Space is captive_integrated — no transaction price exists. Its value comes from segment CONTRIBUTION and no external multiple is borrowed. The flag travels with the row."
  - da_id: "DA-02"
    chosen_reading: "Segment operating income is filed on a 3M and a 6M basis under one concept. This artifact annualises the 3M rate x4 for the multiple's denominator and SAYS SO — it does not blend 3M and 6M figures."
entity_claims:
  - claim_id: "sotp-q2-consolidated-revenue"
    ticker: SPCX
    metric: consolidated_revenue
    value: 7814000000
    unit: USD
    basis: "filed consolidated; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q spcx-20260630.htm p.30 (Note 18) — consumed via 003, re-read here; https://agentii.ai/v/SPCX/sec8/30"
  - claim_id: "sotp-q2-consolidated-operating-loss"
    ticker: SPCX
    metric: operating_income_loss
    value: -143000000
    unit: USD
    basis: "filed consolidated, DA-23-corrected; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q — segments sum exactly to (143); the served layer returns +143,000,000 (DA-23)"
  - claim_id: "sotp-shares-outstanding-2026-06-30"
    ticker: SPCX
    metric: common_shares_outstanding
    value: 13176000000
    unit: shares
    basis: "Class A 7,607,000,000 + Class B 5,569,000,000, instant 2026-06-30; closes exactly"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q spcx-20260630.htm — us-gaap:CommonStockSharesOutstanding x StatementClassOfStockAxis"
  - claim_id: "sotp-cursor-shares-issued"
    ticker: SPCX
    metric: shares_issued_acquisition
    value: 391041680
    unit: shares
    basis: "389,289,254 at close + 1,752,426 vested RSUs; instant 2026-08-14"
    period: "2026Q3"
    evidence_grade: DEMONSTRATED
    source: "8-K 0001628280-26-056945 (2026-08-14) Item 2.01 — https://agentii.ai/v/SPCX/sec9/2"
  - claim_id: "sotp-live-quote"
    ticker: SPCX
    metric: share_price
    value: 152.71
    unit: USD
    basis: "close, source nasdaq, data_class fast; observed 2026-09-18, retrieved 2026-09-19"
    period: "2026Q3"
    evidence_grade: DEMONSTRATED
    source: "data-tools/market_data.py get_quote — keyless NASDAQ"
key_metrics:
  consolidated_revenue_q2_2026_usd_m: 7814
  consolidated_operating_loss_q2_2026_usd_m: -143
  shares_outstanding_2026_06_30: 13176000000
  cursor_shares_issued: 391041680
  live_price_usd: 152.71
  segment_capex_total_q2_2026_usd_m: 18369
  ai_capex_q2_2026_usd_m: 15828
  connectivity_capex_q2_2026_usd_m: 1367
  space_capex_q2_2026_usd_m: 1174
  ai_capex_share_q2_2026: 0.8617
---

# SPCX × sotp-valuation × methodology

**The anchor. Three segments, three regimes, one dated market print — and a convergence the plan
did not expect.**

## 0. ⚠️ Three premises changed during this run, and each is stated before the valuation

| # | What the plan assumed | What the filings show |
|---|---|---|
| **1** | Cursor **pending**, closing Q3 2026; dilution **not determinable** — V-5 `blocking` | **Cursor CLOSED 2026-08-14** ([8-K Item 2.01](https://agentii.ai/v/SPCX/sec9/2)). Dilution is **391,041,680 shares issued**, **464,535,053** including assumed awards. **V-5 RESOLVED** |
| **2** | Market Data Stage `none`; price is a dated print (`$135.00`, 2026-06) | **A keyless live feed exists.** **$152.71**, close **2026-09-18**, source `nasdaq` |
| **3** | The constitution's ~$1.62T anchor is ~13.1% behind the live price | **It is further behind than that, and on a basis we can now check** — §2 |

**The valuation below is built on the filings, not on the plan's assumptions about them.**

## 1. The segment table — component identity in-line, per DA-23

**Duration basis: 3M, quarter ended 2026-06-30. SPCX files NO segment gross-profit subtotal**, so
gross profit is **`DERIVED`** and shown as such.

| Segment | Revenue | Cost of rev. | **Gross profit** *(DERIVED)* | R&D | SG&A | Restr. | **Op. income** *(filed)* | Margin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Space** | 962 | 329 | **633** | 1,076 | 99 | — | **(542)** | **−56.34%** |
| **Connectivity** | 4,291 | 2,060 | **2,231** | 294 | 281 | — | **1,656** | **+38.59%** |
| **AI** | 2,561 | 1,106 | **1,455** | 2,178 | 532 | **2** | **(1,257)** | **−49.08%** |
| **Σ segments** | **7,814** | 3,495 | **4,319** | 3,548 | 912 | 2 | **(143)** | **−1.83%** |

**Identity closes exactly on every row and at consolidation:**
`962 − 1,504 = (542)` · `4,291 − 2,635 = 1,656` · **`2,561 − 3,818 = (1,257)`** · **`7,814 − 7,957 = (143)`** ✓

> ### ⚠️ CORRECTION, MADE IN THIS ARTIFACT'S FIRST DRAFT — A $2M "OTHER" TERM
>
> The first draft's AI row showed only **R&D 2,178 + SG&A 532 = 2,710**, giving
> `1,455 − 2,710 = (1,255)` — **$2M short of the filed `(1,257)`** — while the surrounding text
> asserted *"the identity closes exactly on every row."* **It did not.**
>
> **The missing term is the filed `Restructuring charges` line of $2M** — and a later pass found the draft had **also mislabelled the column "Other"**. The 10-Q names it. 003's `value-pool-map` E-03 has it right:
> `2,178 + 532 + 2 = 2,712 opex … 1,455 − 2,712 = (1,257) ✓ EXACT`. **This artifact dropped it**
> in transcription and then claimed exactness it had not verified.
>
> **Caught by running the arithmetic rather than trusting the assertion** — which is the only way
> this class of error is ever caught. **It is recorded rather than silently fixed because the
> claim "closes exactly" is precisely the kind of sentence that travels downstream unchecked**, and
> a reader who re-derived the row would have found a $2M hole with no note explaining it.
>
> **Reconciled total opex: `3,548 + 912 + 2 = 4,462`**, and `7,814 − (3,495 + 4,462) = (143)` ✓

> **⚠️ DA-23 IS LIVE ON THE CONSOLIDATED LINE.** The segments sum to **$(143)M**; the platform's
> served layer returns **`+143,000,000`**. 002's census found **16 of 20** served
> `OperatingIncomeLoss` facts at SPCX carry a positive value against a filed negative. **The
> artifact reads the filed sign.** `EPS × shares` would not have caught this.

### The supplemental block, which this artifact's first draft did not read

**Note 18 files three more segment lines below the income table. They are the capital-allocation
finding. An earlier version of `_cross/tier0-spacex-anchor_synthesis.md` recorded segment-level
capex as `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — it is filed, on this page.**

| Segment | D&A | Share-based comp. | **Capital expenditures** | Share of capex |
|---|---:|---:|---:|---:|
| Space | 158 | 179 | **1,174** | **6.4%** |
| Connectivity | 805 | 136 | **1,367** | **7.4%** |
| **AI** | 1,885 | 516 | **15,828** | **86.2%** |
| **Σ** | **2,848** | **831** | **18,369** | **100%** |

> **The AI segment absorbs `15,828 / 18,369 = 86.17%` of quarterly capital expenditure** while
> running the **largest operating loss** in the company — and **Connectivity, the only profitable
> segment, receives 7.4%.** Source: [SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30).

## 2. The market print — two bases, and a discrepancy that is a finding

| Basis | Value | Source |
|---|---:|---|
| **Shares outstanding**, 2026-06-30 | **13,176,000,000** | 10-Q, `CommonStockSharesOutstanding`; Class A 7,607M + Class B 5,569M — **closes exactly** |
| **+ Cursor**, issued 2026-08-14 | **391,041,680** | 8-K `0001628280-26-056945` |
| **Pro-forma shares** | **13,567,041,680** | |
| **Live price**, close 2026-09-18 | **$152.71** | `nasdaq`, keyless |
| **⇒ LIVE MARKET CAP** | **≈ $2.072T** | 13.567bn × $152.71 |
| Constitution anchor | **~$1.62T** | struck at `$135.00`, 2026-06 |

> ### 🔴 THE CONSTITUTION'S ANCHOR IMPLIES ~$122.95/SHARE ON THIS SHARE COUNT — NOT $135.00
>
> `$1.62T ÷ 13,176,000,000 = $122.95`. **The IPO priced at `$135.00`.** So the constitution's
> anchor and the IPO price **do not reconcile on the filed share count**, and the gap is **~9%
> at the anchor** before any price move.
>
> **⇒ The anchor is NOT "13.1% behind". Against the live price it is further behind, and the basis
> is unstated.** Round 4's provisional measured the gap as `152.71/135.00 − 1 = +13.1%` — **that
> compares the live price to the IPO price, not to the anchor's own implied price.**
>
> **This artifact therefore publishes BOTH and resolves neither**, per round 4's answer (*"both —
> live and dated, with the spread reported"*). **The reconciliation of the ~$1.62T anchor is
> `UNRESOLVABLE-FROM-PUBLIC-SOURCES` on the pages read**: it requires the basis the constitution
> struck it on, which is not in this workspace.

## 3. The regimes — one per segment, each with its boundary

### Space — `DA-06` non-comparability; value from contribution

| | |
|---|---|
| **Revenue** | **$962M** (3M) — **customer launches only.** ~74% of launches produce no Space revenue |
| **Gross margin** | **65.80%** — **the highest in the company** |
| **Operating margin** | **−56.34%** — **the worst in the company** |
| **The 122.14 pp swing** | **R&D 111.85 pp** + **SG&A 10.29 pp** — decomposed exactly |
| **Comparability** | ❌ **NONE.** `captive_integrated`; **no transaction price exists**. RKLB and FLY are `loss_making` |
| **Regime** | **Revenue multiple, `MODELED`, stated as a range** — and **no external multiple is borrowed** |

**P4's test — ex-R&D operating result is positive:** `633 gross profit − 99 SG&A = +$534M`. ✅
**The launch business is profitable before Starship development**, which is P4's claim. **The R&D
split is `MODELED`** (the filing does not separate Starship from Falcon), and that limit travels.

### Connectivity — margin-anchored; the only profitable segment

| | |
|---|---|
| **Revenue** | **$4,291M** (3M), **+65.8%**; **54.9% of consolidated** |
| **Operating margin** | **+38.59%** — **the only positive segment, and the highest-margin operator in the universe** |
| **Operating leverage** | Income **+79.4%** on revenue **+65.8%** — **+13.6 pp of rate spread** |
| **Channel mix** | **Enterprise&Gov +108.3%** vs **Consumer +44.4%** — the managed channel grew **2.4× faster** |
| **Comparability** | ❌ IRDM and GSAT are **`P11` deal securities — the price is a spread**. ASTS/VSAT `PARTIAL` |
| **Regime** | **Margin-anchored, `MODELED`** — cross-checked against **terrestrial broadband**, not satellite peers |

### AI — invested capital, under the A4 ceiling

| | |
|---|---|
| **Revenue** | **$2,561M** (3M), **+247.5%** — **contaminated** (xAI merged 2026-02-02, prior periods recast) |
| **Operating margin** | **−49.08%** — the largest single drag on the consolidated line |
| **Headline metric** | **1.4 GW IT load** — **DA-11: unconvertible.** It is a **capacity** figure |
| **Comparability** | ❌ MSFT/GOOG compute are **cost centres**; **NVDA is the supplier** |
| **Regime** | **INVESTED CAPITAL** (round 4's confirmed headline) |

## 4. 🔴 The finding: there is no conventional discount to measure

**Annualising the 3M rate ×4** — stated as an annualisation, not a forecast:

| | Annualised |
|---|---:|
| **Connectivity operating income** | **$6,624M** |
| Space operating loss | $(2,168)M |
| AI operating loss | $(5,028)M |
| **Consolidated** | **$(572)M — a LOSS** |

**Now the arithmetic that is the thesis:**

> **Live market cap ≈ $2.072T ÷ Connectivity's annualised operating income $6.624bn = 312.8×**
>
> **And Connectivity is the ONLY profitable segment.**

**So the "conglomerate discount" question inverts.** The standard SOTP asks: *does the sum of parts
exceed the whole?* **Here the whole already requires the one profitable segment to carry a ~313×
operating multiple while two segments run losses of $(2.2)bn and $(5.0)bn annualised.** A
conglomerate DISCOUNT is not the live question. **The live question is whether the market is
crediting the loss-making segments with value at all — or whether it is paying 313× for
Connectivity and treating Space and AI as options with a large embedded premium.**

**Stating it as the three components §5 requires:**

| Component | Status |
|---|---|
| **Conglomerate discount** | ⚠️ **Cannot be measured as a discount** — the parts do not sum to less than the whole under any admissible multiple. **Reported as the inverse** |
| **Control / float discount** | ⚠️ **Made harder by pro-forma.** The Cursor consideration is **Class A**, so the control/float component is partly a discount **created by** the transaction the anchor now includes. **Where the two cannot be separated, that is the finding** |
| **Unallocated corporate cost** | ❌ **Not separable from the segment table** — SPCX files no corporate/unallocated line. **Reported as a bound, not allocated arbitrarily** |
| **Price-basis spread** | **~$122.95 → $152.71 implied**, plus the anchor's own unreconciled basis (§2) |

## 5. What this artifact does NOT claim

- **No point estimate.** Every multiple above is `MODELED`, and the regimes are ranges.
- **No `dcf`.** Consolidated FCF is negative; the ≥3-year limb fails. **`reverse-dcf` is the
  admissible DCF-shaped instrument** and runs separately.
- **No borrowed multiple.** The comparability partition admits **zero of eleven** comparators.
- **No blended multiple.** Valuing three businesses at one rate is *a different claim*, and the
  spread between the two is the finding.

## 6. Hand-off

`_cross/anchor-sotp.md` publishes the three regimes with boundaries naming **005, 006 and 009** —
not 005 alone, because SPCX is in neither 006's nor 009's universe. **The 313× figure is the
anchor's headline and 011's problem to act on**: it is a *valuation* fact, and this thesis produces
no positions.
