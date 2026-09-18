---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: SPCX
skill: business-model
mode: methodology
generated_at: 2026-09-18T23:10:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "registry-1.0.0"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-20"
    chosen_reading: "AI segment revenue read as TERRESTRIAL on all four axes; reported side by side per §1c"
  - da_id: "DA-21"
    chosen_reading: "SPCX's own three-segment definitions replace the prior Space/Connectivity two-segment frame"
  - da_id: "DA-19"
    chosen_reading: "common-control mergers (xAI, X) treated as a change of reporting entity, not organic growth"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# SPCX — Business Model (post-IPO)

Source: Form 10-Q, accession `0001628280-26-052535`; Notes 1 and 3; MD&A Overview.

**⚠️ This artifact supersedes the segment frame used in every prior SPCX artifact.** SPCX now
reports **three** segments, and the one the thesis was built on is the smallest.

---

## 1. The reporting entity changed — and the change is not organic

**Three events between the prior SPCX artifacts and this filing:**

| Event | Date | Effect |
|---|---|---|
| **X Merger** — X Holdings and X.AI Corp into xAI | 2025-03-28 | Twitter/X and X.AI combined under xAI |
| **xAI Merger** — X.AI Holdings Corp into SPCX | **2026-02-02** | **common control**; xAI becomes a wholly-owned subsidiary |
| **IPO** | 2026-06 | 638.9M Class A shares at $135.00; **net proceeds $85,675M** |
| Five-for-one forward stock split | 2026-05 | all prior periods retroactively adjusted |
| **Cursor Merger** — Anysphere, Inc. | option exercised 2026-06 | **$60B implied equity value**, all-stock, closing expected Q3 2026 |

**Consequence for every prior SPCX artifact in this thesis**: the revenue base, segment
structure and growth rates are **not comparable across the mergers**. Common-control
combinations are accounted for as a **change of reporting entity**, so prior-period figures
have been recast — and **any growth rate quoted across the boundary mixes real growth with
entity change.** Both the DA-19 and DA-26 registers apply.

**This is the single largest statement-level discontinuity in the universe**, larger than any
of the extraction defects: the issuer the thesis anchors on **became a different company
mid-series.**

## 2. Revenue composition — the space business is the smallest and shrinking

| Segment | Q2 2026 | % | H1 2026 | H1 2025 | H1 change |
|---|---:|---:|---:|---:|---:|
| **Connectivity** (Starlink) | **$4,291M** | **54.9%** | **$7,548M** | $5,062M | **+49.1%** |
| **AI** (Grok, X, compute) | **$2,561M** | **32.8%** | **$3,379M** | — | — |
| **Space** (launch, Dragon) | **$962M** | **12.3%** | **$1,581M** | $1,611M | **−1.9%** |
| **Total** | **$7,814M** | 100% | $12,508M | $8,138M | +53.7% |

**Classification.** SPCX is not a launch company with adjacent businesses. On revenue it is
**a satellite broadband operator (54.9%) with a terrestrial AI business (32.8%) that also
launches rockets (12.3% and declining).**

**And the H1 comparison is the cleaner one** — H1 2025 predates the xAI merger, so the AI
column is absent, but **the Space column is directly comparable across both halves and it
FELL 1.9%** while total revenue rose 53.7%.

**Consequence for the universe's construction**: the thesis's five cohorts were built
treating SPCX as the core launch name. **On its own disclosure, SPCX's launch business is a
sub-scale, loss-making segment inside a company whose value is dominated by two non-launch
businesses.** Any thesis that uses SPCX as the launch-sector read-through is **reading 12% of
the company and 0% of its growth.**

## 3. The four distribution channels are economically different businesses

| Channel | Segment | Contract form | Margin | Backlog character |
|---|---|---|---|---|
| **Consumer subscription** | Connectivity | Starlink.com service lines, monthly | in the 52.0% segment gross margin | none — monthly churn |
| **Enterprise / government** | Connectivity | negotiated contracts: aviation, maritime, land mobility, fixed sites, government | **grew MORE than consumer** (+$939M vs +$764M) | contracted |
| **Launch, fixed-price** | Space | Launch Services **1–5 yr**; Launch and Development **1–14 yr**, cost-to-cost | 65.8% gross, **−56.3% after R&D** | long-dated, government-heavy |
| **AI** | AI | advertising, subscriptions, **data licensing, API access to Grok, cloud services** | not disclosed | mixed |

**Two observations that matter for the thesis:**

**(a) The revenue-recognition asymmetry inside Space.** Launch Services is recognised **at a
point in time** — revenue and cost are deferred until the payload reaches orbit. Launch and
Development is recognised **over time** on a cost-to-cost input method. **So a launch that
slips moves revenue between quarters, and a development contract that overruns books
revenue as it burns cost.** These two are aggregated into one segment line. **Any
quarterly Space revenue series is a blend of two recognition methods with opposite
sensitivities to delay** — register as a definitional caveat on PIL-1 and PIL-3.

**(b) Concentration is disclosed but not quantified here.** Note 3 carries explicit
`concentration of risk` disclosure naming **Customer A and Customer B** against the backlog.
**The extract does not carry the percentages in the pages read**; the named-customer
disclosure is the place to resolve any question about how much of the backlog rests on two
counterparties. **Carried forward as a bounded read, not as a finding.**

## 4. The AI segment is terrestrial, and it is the fastest-growing part of the company

**Revenue increased $1,824M in Q2 2026 — the largest single contributor to consolidated
growth, ahead of Connectivity's $1,703M.** The segment is described as *"AI computational
infrastructure,"* and its key metric is **nameplate compute draw: 1.4 GW (from 0.4 GW)**.

**On the DA-20 four-way reading required by §1c, all four axes reported:**

| Axis | Reading |
|---|---|
| compute **in** orbit | **No.** Nameplate compute draw counts GPUs installed **in data centers**; explicitly excludes cooling, power distribution and facility overhead — the vocabulary of a terrestrial build |
| compute **for** orbit | No |
| communications **from** orbit | **No** — this is Connectivity, a separate segment |
| **terrestrial compute with satellite-delivered distribution** | **Yes** |

**SPCX's AI business is a data-center business.** Its fastest-growing segment and its
largest capital deployment are both on the ground, at the company with the cheapest orbital
access in existence.

**Consequence for the business-model classification**: SPCX is best described as **a
vertically integrated compute-and-connectivity company that owns its own launch capability**
— not the reverse. **That is the same vertical-integration logic the F2/BWXT analysis
identified, applied to compute rather than power.**

## 5. What the model implies for capital allocation

```
H1 2026 capex increase $21,511M:
  "the build out of DATA CENTERS and related infrastructure,
   and space launch facilities and related infrastructure"
```

**Data centers are named first.** Against a $541M quarterly net loss and $4,817M H1 net loss,
the company raised $85.7B in equity and $40.9B in notes and is **spending the majority of
its investing outflow on compute capacity.**

**This is the cleanest capital-allocation signal in the universe**, and it is a stated
priority ordering rather than an inference: **the company with the strongest strategic
position in launch is allocating marginal capital to terrestrial compute.**

---

## Carry-forwards

1. **The reporting entity changed mid-series** (X merger 2025-03-28, xAI merger 2026-02-02,
   IPO 2026-06, Cursor pending). **Common-control accounting recasts prior periods, so
   growth rates across the boundary mix real growth with entity change.** DA-19 and DA-26
   both apply, and **this is a larger discontinuity than any extraction defect.**
2. **Launch is 12.3% of revenue and fell 1.9% across a half in which total revenue rose
   53.7%.** The universe was built treating SPCX as the core launch read-through; **that
   reads 12% of the company and 0% of its growth.**
3. **Space's revenue blends two recognition methods** — point-in-time Launch Services and
   over-time cost-to-cost Launch and Development — **with opposite sensitivities to delay.**
   A definitional caveat on PIL-1 and PIL-3, not a defect.
4. **The AI segment is terrestrial on all four DA-20 axes**, is the largest contributor to
   consolidated growth, and commands the largest capital allocation. **SPCX is a
   compute-and-connectivity company that owns its own launch capability, not a launch
   company with adjacent businesses.**
5. **Backlog concentration (Customer A / Customer B) is disclosed but not quantified on the
   pages read** — carried as a bounded read.
