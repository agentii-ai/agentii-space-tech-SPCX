---
thesis_id: "004-tier0-spacex-anchor"
pillar: cross
ticker: SPCX
skill: synthesis
mode: methodology
generated_at: 2026-09-19T14:50:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "Every segment figure is read on the FILED sign with the component identity in-line. The served consolidated line returns +143,000,000 against a filed (143,000,000); 16 of 20 served SPCX OperatingIncomeLoss facts are sign-stripped."
  - da_id: "DA-06"
    chosen_reading: "Space is captive_integrated — no transaction price exists. Its row carries a non-comparability boundary and no external multiple is borrowed."
  - da_id: "DA-11"
    chosen_reading: "The 1.4 GW is IT load only. It is a CAPACITY figure and cannot be converted without a $/kW assumption no issuer discloses — which is why P3's headline is invested capital, a cost basis."
entity_claims:
  - claim_id: "anchor-live-market-cap"
    ticker: SPCX
    metric: market_capitalisation
    value: 2071800000000
    unit: USD
    basis: "13,567,041,680 shares x $152.71; price observed 2026-09-18, retrieved 2026-09-19, source nasdaq"
    period: "2026Q3"
    evidence_grade: DERIVED
    source: "10-Q share count 13,176,000,000 (2026-06-30) + 8-K Cursor 391,041,680 (2026-08-14) + live quote"
  - claim_id: "anchor-dated-market-cap"
    ticker: SPCX
    metric: market_capitalisation_dated
    value: 1620000000000
    unit: USD
    basis: "constitution's ~$1.62T anchor, struck 2026-06; implies $122.95/share on the filed share count — NOT the $135.00 IPO price"
    period: "2026Q2"
    evidence_grade: CLAIMED
    source: "constitution.md Research Scope Constraints; basis unreconciled"
  - claim_id: "anchor-multiple-on-only-profitable-segment"
    ticker: SPCX
    metric: market_cap_to_connectivity_operating_income
    value: 312.8
    unit: ratio
    basis: "2.0718T / (1,656 x 4 = 6,624M); Connectivity is the ONLY positive segment"
    period: "2026Q3"
    evidence_grade: DERIVED
    source: "arithmetic on the live market cap and filed segment operating income"
---

# THE ANCHOR — SPCX, three segments, three regimes

> **What this is.** The citable anchor for theses **005, 006 and 009**. Three multiple regimes, each
> with a source, a grade and a **comparability boundary**. **This is not a price target and produces
> no position** — sizing is 011's.
>
> **Read the boundaries, not just the rows.** P6 exists because an anchor published without a stated
> comparability set propagates a **false comparability** into every downstream thesis, and the error
> is invisible because each downstream thesis will look internally consistent.

## 1. The market side — BOTH bases, and neither is resolved

| Basis | Value | As of | Grade |
|---|---:|---|---|
| **LIVE** | **$2.0718T** | price observed **2026-09-18**, retrieved 2026-09-19, source `nasdaq` | `DERIVED` |
| **DATED** (constitution) | **~$1.62T** | struck 2026-06 | `CLAIMED` |
| **Spread** | **~28%** | | **reported as its own component** |

**Share count: 13,176,000,000** (10-Q, 2026-06-30 — Class A 7,607M + Class B 5,569M, **closes
exactly**) **+ 391,041,680** (Cursor, 8-K 2026-08-14) = **13,567,041,680**.

> ### 🔴 THE DATED ANCHOR DOES NOT RECONCILE, AND THIS IS A FINDING FOR EVERY CONSUMER
>
> `$1.62T ÷ 13,176,000,000 = **$122.95/share**`. **The IPO priced at `$135.00`.**
> **So the constitution's anchor and the IPO price do not reconcile on the filed share count.**
>
> **⇒ Any thesis quoting `~$1.62T` as a market reference must state that its basis is
> `UNRESOLVABLE-FROM-PUBLIC-SOURCES` on this workspace's pages.** An earlier draft measured the gap
> as *"+13.1%"* by comparing the live price to the **IPO price** — which is **not** the anchor.
> **The anchor-vs-live spread is ~28%, not 13.1%**, and the anchor's own basis is unstated.

## 2. THE ANCHOR TABLE — three regimes, three boundaries

| Segment | Revenue (3M) | Op. income | Margin | **Regime** | Grade | **Comparability boundary** |
|---|---:|---:|---:|---|---|---|
| **Space** | **$962M** | **$(542)M** | **−56.34%** | **Revenue multiple, range**, value from **segment contribution** | `MODELED` | ❌ **NON-COMPARABLE (DA-06).** No transaction price exists; **no external multiple borrowed.** RKLB/FLY `loss_making`. **Permitted consumers: 005, 007** |
| **Connectivity** | **$4,291M** | **$1,656M** | **+38.59%** | **Margin-anchored** | `MODELED` | ❌ **No satellite peer admitted.** IRDM/GSAT are **`P11` — price is a spread**; ASTS/VSAT `PARTIAL`. **Cross-check against terrestrial broadband.** **Permitted consumers: 006, 009** |
| **AI** | **$2,561M** | **$(1,257)M** | **−49.08%** | **INVESTED CAPITAL** *(company-level attribution)* | `MODELED` | ❌ **`non_disclosure`.** MSFT/GOOG compute are **cost centres**; NVDA is the supplier. **Under the A4/P10 ceiling.** **Permitted consumers: 009** |

**Every row's boundary is a PARTITION** — a name is in or out, and the excluded class is named with
its reason (`P11` · `loss_making` · `PARTIAL` · `non_disclosure`). **A graded score was considered
and rejected** (round 4): it invites the downstream thesis to pick its own threshold.

### The component identity, in-line (DA-23)

| Segment | Revenue | − Cost of rev. | = **Gross profit** *(DERIVED)* | − R&D | − SG&A | − Other | = **Op. income** *(filed)* |
|---|---:|---:|---:|---:|---:|---:|---:|
| Space | 962 | 329 | **633** | 1,076 | 99 | — | **(542)** |
| Connectivity | 4,291 | 2,060 | **2,231** | 294 | 281 | — | **1,656** |
| AI | 2,561 | 1,106 | **1,455** | 2,178 | 532 | **2** | **(1,257)** |
| **Σ** | **7,814** | 3,495 | **4,319** | 3,548 | 912 | 2 | **(143)** |

**`7,814 − 7,957 = (143)` closes exactly.** ⚠️ **The served layer returns `+143,000,000`** — see §5.
**SPCX files NO segment gross-profit subtotal**, so gross profit is `DERIVED` on every row.

## 3. THE HEADLINE — and it is not a discount

```
Live market cap                                      $2.0718T
÷ Connectivity operating income (1,656 × 4 = 6,624M)  = 312.8×
   ...and Connectivity is the ONLY profitable segment
```

**The standard SOTP asks whether the parts exceed the whole.** **Here the whole already requires the
one profitable segment to carry ~313× while Space and AI run losses of $(2.2)bn and $(5.0)bn
annualised.**

> **⇒ A conglomerate DISCOUNT is not the live question. The live question is whether the market
> credits the loss-making segments at all.**

**And the finding survives every allocation:**

| If Space + AI are worth | Connectivity's implied multiple |
|---|---:|
| **$0** | **312.8×** |
| **$0.5T** | **237.3×** |
| **$1.0T** | **161.8×** |
| **$1.5T** | **86.3×** |

**Even granting the two loss-making segments $1.5T, Connectivity carries 86×.** That robustness is
what makes it a finding rather than an artefact of framing.

## 4. The discount decomposition — three components, and one that cannot be separated

| Component | Status |
|---|---|
| **Conglomerate discount** | ⚠️ **Cannot be measured as a discount** — the parts do not sum to less than the whole under any admissible multiple. **Reported as the inverse (§3)** |
| **Control / float discount** | ⚠️ **Harder pro-forma.** The Cursor consideration is **Class A**, so this component is partly a discount **created by** the transaction the anchor now includes. **Where the two cannot be separated, that is the finding** |
| **Unallocated corporate cost** | ❌ **Not separable.** SPCX files no corporate/unallocated line. **Reported as a bound, not allocated** |
| **Price-basis spread** | ✅ **~28%**, reported as its own component (§1) |

## 5. What a consumer MUST carry — the transfer conditions

1. **The DA-23 filed sign.** The segments sum to **$(143)M**; the served layer returns
   **`+143,000,000`.** **A consumer reading the served line inherits a sign-stripped figure.**
2. **The basis of every market figure** — live or dated, **with the date**. §1's ~28% spread is a
   **component**, not noise.
3. **DA-06 on Space** — a captive-integrated segment has **no transaction price**. A downstream
   thesis comparing Space's margin to a peer launcher is **comparing a price to a non-price**.
4. **DA-11 on AI** — 1.4 GW is **IT load**, a capacity figure. **It cannot be converted.**
5. **A4/P10** — the 1M-satellite filing is **inadmissible as a valuation input**.
6. **The A1b showing.** A1b is **falsified**, and the SOTP must **show** value migrating out of
   launch, not assert it: **Space is 12.3% of revenue and fell 1.9% across H1 while consolidated
   revenue rose 53.7%.** ✅ Shown, not asserted.

## 6. Coverage and provenance

- **004 is the programme's ONLY valuation of SPCX's Connectivity and AI segments.** SPCX appears in
  **neither 006's universe** (IRDM, GSAT, SATS, ASTS, VSAT) **nor 009's** (VRT, NVDA, GOOG, MSFT,
  AMZN, AAPL). **Those two rows are reusable references**, which is why the boundaries name
  **006 and 009** and not 005 alone.
- **Nine skills were CONSUMED from 003**, which is COMPLETE — the curve matrix, the value-pool map,
  and nine SPCX artifacts. **004 adds the valuation and does not re-derive the curve.**
- **All seventeen per-ticker artifacts** are G1-clean at `constitution_pin: 1.5.0`.
- **Cursor closed 2026-08-14** (8-K `0001628280-26-056945`); **V-5 RESOLVED**; the headline is
  **pro-forma** and the deal is **actual**, not projected.

## 7. What could not be valued — recorded, not implied

| Item | Class |
|---|---|
| Aviation / maritime revenue splits | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — inside `EnterpriseAndGovernmentMember` |
| Grok vs compute within the AI segment | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — **advertising IS separable (21.0%)**; the rest is not |
| Subscribers / ARPU by channel | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — revenue decomposes, the subscriber denominator does not |
| Segment-level capex for the AI invested-capital framing | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — company-level attribution only |
| The constitution's ~$1.62T basis | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` on the pages read |
| A forward DCF at any level | **Barred** — fails the ≥3-year positive-FCF limb. `reverse-dcf` is the admissible DCF-shaped instrument |
| **Any comparable multiple** | **The partition admits 0 of 11.** Not a search failure — **three different structural reasons**, one per segment |
