---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-2/PIL-3/PIL-4"
ticker: SPCX
skill: revenue-decomp
mode: methodology
generated_at: 2026-09-19T11:05:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "037b396ab004"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "Issuer-defined segment boundaries taken as filed, then decomposed ONE level deeper on the filer's OWN axis (srt:ProductOrServiceAxis). The deep cut is not our taxonomy — it is the filer's, read from XBRL dimensions. This is what spec §3a requires: 'derive the cuts from the filings, do not pre-declare a taxonomy.'"
  - da_id: "DA-26"
    chosen_reading: "Period labels — the 10-Q carries both 3M (quarter ended 2026-06-30) and 6M (six months ended 2026-06-30) durations under the SAME concept and axis. Every figure below names its duration. A 3M figure is never compared to a 6M figure."
  - da_id: "DA-23"
    chosen_reading: "Not engaged. This artifact reads REVENUE only, which carries no sign-strip exposure at SPCX (the DA-23 census found the defect in OperatingIncomeLoss, 16 of 20 served facts). Stated so its absence is a decision, not an oversight."
entity_claims:
  - claim_id: "rd-space-launchservices-h1-2026"
    ticker: SPCX
    metric: segment_product_revenue
    value: 978000000
    unit: USD
    basis: "filed, segment x product-or-service; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax x srt:ProductOrServiceAxis=spcx:LaunchServicesMember x us-gaap:StatementBusinessSegmentsAxis=spcx:SpaceMember"
  - claim_id: "rd-space-launchanddev-h1-2026"
    ticker: SPCX
    metric: segment_product_revenue
    value: 603000000
    unit: USD
    basis: "filed, segment x product-or-service; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=spcx:LaunchAndDevelopmentMember x spcx:SpaceMember"
  - claim_id: "rd-conn-consumer-h1-2026"
    ticker: SPCX
    metric: segment_product_revenue
    value: 4633000000
    unit: USD
    basis: "filed, segment x product-or-service; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=spcx:ConsumerMember x spcx:ConnectivityMember"
  - claim_id: "rd-conn-entgov-h1-2026"
    ticker: SPCX
    metric: segment_product_revenue
    value: 2915000000
    unit: USD
    basis: "filed, segment x product-or-service; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=spcx:EnterpriseAndGovernmentMember x spcx:ConnectivityMember"
  - claim_id: "rd-ai-solutions-h1-2026"
    ticker: SPCX
    metric: segment_product_revenue
    value: 2669000000
    unit: USD
    basis: "filed, segment x product-or-service; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=spcx:AISolutionsAndInfrastructureMember x spcx:AIMember"
  - claim_id: "rd-ai-advertising-h1-2026"
    ticker: SPCX
    metric: segment_product_revenue
    value: 710000000
    unit: USD
    basis: "filed, segment x product-or-service; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=us-gaap:AdvertisingMember x spcx:AIMember"
  - claim_id: "rd-nature-service-h1-2026"
    ticker: SPCX
    metric: consolidated_revenue_by_nature
    value: 11667000000
    unit: USD
    basis: "filed, consolidated x product-or-service NATURE; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=us-gaap:ServiceMember"
  - claim_id: "rd-nature-product-h1-2026"
    ticker: SPCX
    metric: consolidated_revenue_by_nature
    value: 841000000
    unit: USD
    basis: "filed, consolidated x product-or-service NATURE; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q, spcx-20260630.htm — …Axis=us-gaap:ProductMember"
key_metrics:
  space_launch_services_h1_2026_usd_m: 978
  space_launch_and_dev_h1_2026_usd_m: 603
  conn_consumer_h1_2026_usd_m: 4633
  conn_entgov_h1_2026_usd_m: 2915
  ai_solutions_h1_2026_usd_m: 2669
  ai_advertising_h1_2026_usd_m: 710
---

# SPCX × revenue-decomp × methodology

**The derivation path, stated so the numbers are reproducible.** Spec §3a requires the cut *inside*
each segment to be **derived from the filings, not declared by us.** This artifact establishes
which cuts the filer actually reports, proves each closes, and records the cuts that do **not**
exist — with their disposition class rather than silence.

> **⚠️ ROUND 4 OF THE PLAN SAID THESE CUTS WERE "NOT FORMABLE". THAT WAS WRONG, AND THIS ARTIFACT
> IS THE CORRECTION.** Plan finding **F7** concluded: *"`aviation` and `maritime` appear twice in
> all nine SPCX artifacts, as prose, with no revenue figure attached"* — **true, and it stopped
> there.** The filer's actual decomposition was in the **XBRL dimensional axes**, which none of
> 003's nine SPCX artifacts queried. **The correct conclusion is the opposite of "not formable":
> SPCX files a THREE-LEVEL revenue decomposition** — segment, then product-or-service within each
> segment, then a consolidated product/service nature split. **This is the single most consequential
> input to P2, P3 and P4 after the segment note itself.**

## 1. The axis, and why it settles the question

`srt:ProductOrServiceAxis` is filed at SPCX with these members:

| Member | Segment it sits in |
|---|---|
| `spcx:LaunchServicesMember` | Space |
| `spcx:LaunchAndDevelopmentMember` | Space |
| `spcx:ConsumerMember` | Connectivity |
| `spcx:EnterpriseAndGovernmentMember` | Connectivity |
| `spcx:AISolutionsAndInfrastructureMember` | AI |
| `us-gaap:AdvertisingMember` | AI |
| `us-gaap:ServiceMember` | *(consolidated — cross-segment nature)* |
| `us-gaap:ProductMember` | *(consolidated — cross-segment nature)* |

**Eight members across two axes uses.** The six segment-scoped members are the deep cut; the two
nature members are a separate, consolidated reading of the same axis. **They are not alternatives
and neither is a substitute for the other.**

## 2. The matrix, H1 2026 — every level closes

Duration basis: **6M, six months ended 2026-06-30.** Units USD millions, as filed.

| Segment | Segment total | Product-or-service cut | Sum | Closes |
|---|---:|---|---:|---|
| **Space** | **1,581** | Launch Services **978** + Launch & Development **603** | 1,581 | ✅ **exact** |
| **Connectivity** | **7,548** | Consumer **4,633** + Enterprise & Government **2,915** | 7,548 | ✅ **exact** |
| **AI** | **3,379** | AI Solutions & Infrastructure **2,669** + Advertising **710** | 3,379 | ✅ **exact** |
| **Σ segments** | **12,508** | | 12,508 | ✅ **exact** |
| **Consolidated by nature** | **12,508** | Service **11,667** + Product **841** | 12,508 | ✅ **exact** |

> ### ⚠️ CORRECTION — `2,914` → `2,915`, AND THERE IS NO RESIDUAL
>
> The first draft read Enterprise & Government as **2,914**, which produced `7,547` against a filed
> parent of `7,548` — a **$1M residual** — and the artifact then reported closure as *"✅ ±1
> (rounding)"* **at three levels**. The filed child is **2,915**:
> **every row closes exactly, and the ±1 is gone.**
> Source: [SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13).
>
> **Caught by re-reading the filing rather than re-reading this table.** The error propagated into
> `defaults` D-1, which had constructed a default to absorb it, and into `metrics.json` as
> `connectivity_closure_residual_usd_m: 1`. **A closure chain with a rounding allowance anywhere in
> it cannot detect an error, because the allowance absorbs exactly the error it would surface.**

**Three independent closures, and the same 12,508 reached by two different routes** — the segment
sum and the nature split. **That is the derivation's own check**: if the deep cut were a taxonomy
we had imposed, it would not close to the filer's own totals. **With the ±1 removed, the check is
now exact rather than near-exact, which is the only form in which it can fail loudly.**

## 3. The same matrix, Q2 2026 — for period discipline (DA-26)

Duration basis: **3M, quarter ended 2026-06-30.** **Never compared against §2.**

| Segment | Segment total | Product-or-service cut | Sum | Closes |
|---|---:|---|---:|---|
| **Space** | **962** | Launch Services **648** + Launch & Development **314** | 962 | ✅ **exact** |
| **Connectivity** | **4,291** | Consumer **2,485** + Enterprise & Government **1,806** | 4,291 | ✅ **exact** |
| **AI** | **2,561** | AI Solutions & Infrastructure **2,194** + Advertising **367** | 2,561 | ✅ **exact** |
| **Σ segments** | **7,814** | | 7,814 | ✅ **exact** |
| **Consolidated by nature** | **7,814** | Service **7,353** + Product **461** | 7,814 | ✅ **exact** |

**The two durations are filed under the same concept and the same axes.** Without the duration
label in-line, `978` and `648` are the same number presented twice. **DA-26 is live here, and this
artifact names its duration on every row.**

## 4. What this changes for P2, P3 and P4

**P2 — Connectivity.** 003's map had Consumer and Enterprise&Government from the MD&A. **This is
the XBRL source beneath it, and it confirms 003's figures** (Consumer Q2 **2,485** and
Enterprise&Government Q2 **1,806** match 003's `secular-trends` artifact exactly). The mix-shift
question — *is the −22.4% ARPU decline price erosion or mix shift?* — now has a **filed revenue
basis on both sides of the channel line**, which is stronger than the ARPU series alone.

**P4 — Space standalone.** This is the find that matters most. The plan treated Space as a single
revenue line. **The filer splits it: `LaunchServices` vs `LaunchAndDevelopment`.** For H1 2026 that
is **978 vs 603** — **launch services is 61.9% of the segment and 7.82% of consolidated revenue**;
on the Q2 basis, **648 of 962, or 8.29% of consolidated** — *which is the figure 003's map derived
independently.* **P4's "separable from Starship funding" test now has a filed numerator**, and the
"launch-only" reading is no longer a derived share but a **filed line item.**

**P3 — AI.** The plan's V-3 asked *"is the AI segment homogeneous enough to carry one multiple?"*
and named Grok, X-advertising and compute as the aggregation risk. **The filer splits it two ways,
not three: `AISolutionsAndInfrastructure` 2,669 and `Advertising` 710.** So **the homogeneity
question is sharper than the plan assumed** — advertising is **21.0% of the segment** and is a
genuinely different business from compute, while **Grok and compute are NOT separately filed.**
V-3 is partly answered and partly bounded: *the advertising limb is separable and should be carried
separately; the Grok/compute limb is not separable from public disclosure.*

## 5. Cuts that do NOT exist — named, with their class

| Intended cut | Status | Evidence |
|---|---|---|
| **aviation, maritime** | ❌ **NOT FORMABLE** | Both appear **twice in all nine SPCX artifacts**, as qualitative prose only — *"domains including aviation, maritime, land mobility, fixed sites, and government entities."* **No revenue figure is attached to either.** They sit inside the `EnterpriseAndGovernmentMember` line, which is the finest granularity the filer reports |
| **Grok vs compute** | ❌ **NOT separately filed** | The AI segment splits two ways. Both Grok and compute sit inside `AISolutionsAndInfrastructureMember` (2,669). `UNRESOLVABLE-FROM-PUBLIC-SOURCES` for a further split |
| **Subscribers / ARPU by channel** | ❌ `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | 003 recorded it: managed enterprise/government is *"disclosed as revenue but **not** as subscribers."* **Revenue decomposes; the subscriber denominator does not** — so a per-channel ARPU cannot be computed |
| **Falcon vs Starship** | ❌ `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | `LaunchServicesMember` mixes vehicles. No vehicle-level revenue line is filed |
| **Geographic split** | ⚠️ **not yet queried** | No `srt:StatementGeographicalAxis` fact appeared in the queries run for this artifact. **Recorded as unqueried, not as absent** — absence needs its own negative search |

> **`NON-FORMABLE` is not `PASS`** (003's F16). Each row above is recorded with the class and, where
> one exists, the disclosure that would resolve it.

## 6. Method — reproducible in four steps

```bash
# 1. Which product-or-service members does the filer use? Read the DIMENSIONS, not the values.
search_xbrl_facts(ticker="SPCX",
                  concept="RevenueFromContractWithCustomerExcludingAssessedTax",
                  view="detailed", fiscal_year=2026)
# → returns srt:ProductOrServiceAxis members, each paired with a segment where scoped

# 2. Cross each member against its segment total (StatementBusinessSegmentsAxis).
# 3. Prove closure: Σ(children) == parent, per segment AND at consolidation.
# 4. Name the duration (DA-26) on every figure — 3M and 6M share concept and axis.
```

**⚠️ DO NOT route this through `get_segment_data`.** It hard-errors at SPCX
(`column "k" does not exist`). **003's plan recorded this first** (F4, from 002 §7), with a fuller
diagnosis: it *"reports a `total_revenue` summing served facts across two years and two durations
with no de-duplication — `segment_coverage_pct 116.2` masking a 302.1% overlap."*
**`search_xbrl_facts(view=detailed)` is the working route**, and it is the route this artifact used.

**A note on the `srt:ConsolidationItemsAxis`.** Most segment facts carry
`us-gaap:OperatingSegmentsMember` as well. **Facts appear twice — with and without it — carrying
the same value.** Both were observed above (`7,548` and `4,291` each appear twice). **Take the
dimensioned one**, which names which consolidation item the figure belongs to, and do not sum
across the pair.

## 7. Sources

| Source | What it supplied |
|---|---|
| `SPCX 10-Q, spcx-20260630.htm` (filing `34ca500a-5978-4820-ad0f-fce2f39dfab6`) | Every figure in §2 and §3, as `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` under `srt:ProductOrServiceAxis` × `us-gaap:StatementBusinessSegmentsAxis` |
| `003/_cross/value-pool-map.md` § E-01/E-02/E-03, § 0 sub-finding 4 | The segment totals this decomposition reconciles to, and the independently-derived `8.29%` launch-only share |
| `003/artifacts/SPCX/2026-09-19_1345_secular-trends_methodology.md` | Consumer 2,485 / Enterprise&Government 1,806 (Q2) — **matched exactly** |
| `003/plan.md` § F4, from 002 §7 | The `get_segment_data` verdict and the routing instruction |
