---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-1/PIL-6"
ticker: SPCX
skill: sotp-valuation
mode: preflight
generated_at: 2026-09-19T14:10:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07305f5d5391"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-21"
    chosen_reading: "The three-way decomposition is the issuer's own filed segment boundary. The preflight checks that the decomposition the SOTP depends on actually exists before any multiple is applied."
entity_claims:
  - claim_id: "sotp-preflight-separable-segments"
    ticker: SPCX
    metric: count_of_spcx_segments_with_a_discrete_filed_revenue_line_and_operating_result
    value: 3
    unit: count
    basis: "Space, Connectivity, AI — each with a filed revenue line AND a filed operating result; 3M duration, quarter ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q spcx-20260630.htm p.30 (Note 18) — three segments, each with Income (loss) from operations"
key_metrics:
  separable_segments: 3
---

# SPCX × sotp-valuation × preflight

**Does the SOTP have a subject?** P1's falsifier is
`count_of_spcx_segments_with_a_discrete_filed_revenue_line_and_operating_result < 3`. This artifact
runs it **before** the valuation, because a decomposition that failed here would make every
multiple below meaningless.

## 1. The separability test — 3 of 3, DISCLOSED

| Segment | Discrete filed revenue line | Discrete filed operating result | Passes? |
|---|---|---|---|
| **Space** | ✅ **962** (3M) | ✅ **(542)** | ✅ |
| **Connectivity** | ✅ **4,291** | ✅ **1,656** | ✅ |
| **AI** | ✅ **2,561** | ✅ **(1,257)** | ✅ |

**All three carry BOTH a revenue line and an operating result, filed.** `threshold=3`, `op=<` → the
count is **3**, so **the falsifier does not fire.**

> ### ⚠️ THIS PILLAR'S ANSWER WAS ALMOST LOST TO A SUPERSESSION CLAIM
>
> Two 001 artifacts disagreed on whether the AI segment files an operating result:
> `1239_operational-kpi` reported **$(1,257)M**; `2310_operational-kpi` §2 recorded *"not
> disclosed."* An intermediate draft concluded the line was **`DERIVED`** on the strength of the
> nominal supersession — and **propagated that error into 002's brief.**
>
> **Phase 1 of 002 disproved it from the source.** `$(1,257)M` appears at **p.30 (Note 18),
> p.44, p.45 (narrative) and p.46 (reconciliation)**, and the identity closes exactly.
> **The earlier `1239` artifact was right.**
>
> **⇒ The separability test is 3 of 3 DISCLOSED, not 2 of 3** — the stronger reading. **And the
> lesson travels: a *supersession* claim is itself an evidence claim and needs the same page-level
> verification as any other. "Newer artifact wins" is not a validation.**

## 2. The reconciliation residual — V-2

`value-checks.yaml` carries `segments_sum_to_total` at **`fail`** level. Run in-line:

```
-542 (Space) + 1,656 (Connectivity) + (-1,257) (AI) = 143 ... signed
```

⚠️ **The residual is ZERO on the filed signs, and the CLOSURE is the trap.** The segments sum to
**$(143)M** and the consolidated line is **$(143)M** — **`7,814 − 7,957 = (143)` closes exactly.**
But the **platform's served layer returns `OperatingIncomeLoss: +143,000,000`** — the **DA-23
sign strip**, quantified by 002 as **16 of 20** served SPCX facts.

**⇒ V-2 resolves as: residual = 0 on the filed signs, and the apparent `+143` is a DA-23 artefact,
not a residual.** **A SOTP built on the served layer would reconcile to the wrong number with no
error raised.**

## 3. Preflight checklist

| Check | Result |
|---|---|
| Three segments with discrete filed revenue lines | ✅ **3 of 3** |
| Three segments with discrete filed operating results | ✅ **3 of 3** — the AI line is **FILED** |
| Segments sum to consolidated | ✅ **exact on filed signs** (`7,814 − 7,957 = (143)`) |
| Component identity available per segment | ✅ derived gross profit − opex closes on all three |
| Market print available | ✅ live quote **$152.71**, plus the dated constitution anchor |
| Share count available | ✅ **13,176,000,000** at 2026-06-30, closes exactly |
| Comparability set | ⚠️ **partition admits 0 of 11** — the regimes are sourced from SPCX's own data |
| **Cursor dilution** | ✅ **RESOLVED** — 391,041,680 shares, closed 2026-08-14 |

**⇒ Preflight PASSES. The SOTP proceeds.**
