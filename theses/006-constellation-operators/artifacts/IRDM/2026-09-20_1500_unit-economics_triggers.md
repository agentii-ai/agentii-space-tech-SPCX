---
thesis_id: "006-constellation-operators"
pillar: "PIL-1"
ticker: IRDM
skill: unit-economics
mode: triggers
generated_at: 2026-09-20T15:00:00Z
constitution_pin: "1.6.0"
assumption_pin: "2"
skill_pin: "80483892ed01"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
deal_security_basis: standalone_pre_merger
definitions_used:
  - da_id: "DA-02"
    chosen_reading: "Every trigger below is dated and carries its own duration (3M or 6M). No trigger is stated on a blended period."
  - da_id: "DA-23"
    chosen_reading: "Each trigger names the filed line it would move and the sign convention it would move it in. A trigger that cannot be evaluated on filed cells is not a trigger."
  - da_id: "DA-30"
    chosen_reading: "Every threshold below names its denominator. A trigger stated as a bare percentage is inadmissible."
key_metrics:
  irdm_falsifier_value_now: 0.505
  irdm_falsifier_threshold: 0.5
  irdm_falsifier_range_low: 0.505
  irdm_falsifier_range_high: 0.646
  cost_of_services_decline_usd_k: -2289
  trigger_count: 6
  triggers_resolvable_within_thesis: 3
  triggers_requiring_a_future_filing: 3
evidence_grade: DEMONSTRATED
citations:
  - figure: "the results-of-operations table, the three revenue lines and five expense lines, and both component identities"
    ticker: IRDM
    citation_id: sec191
    page_no: "24"
    url: https://agentii.ai/v/IRDM/sec191/24
    located_via: read_source_pages
  - figure: "the $14.3M transaction cost disclosure and the engineering-and-support commercial/government split"
    ticker: IRDM
    citation_id: sec191
    page_no: "26"
    url: https://agentii.ai/v/IRDM/sec191/26
    located_via: read_source_pages
---

# IRDM × unit-economics × triggers

**What would overturn P1 at IRDM. Six triggers, each with a datum and a threshold — and the
honest headline is that the current answer sits 0.5 points above the bar, so two of the six are
live rather than hypothetical.**

## 0. What P1 asserts at IRDM, so the triggers have something to overturn

**P1**: *"the residual decline is attributable by revenue line, and **less than half of it falls on
the licensed-spectrum service line**."* The measured value is **50.5%**, against a **0.5**
threshold, `op=<`. **The claim is currently TRUE by half a point.**

| | |
|---|---:|
| Operating-income decline, Q2 2026 vs Q2 2025 | **16,250** |
| Licensed line's own favourable contribution | **8,047** (`+5,758` revenue, `−2,289` cost) |
| **Non-licensed share** | **8,203 / 16,250 = 50.5%** |
| Threshold | **0.5** — falsifier fires at **or above** |

**A claim that passes by 0.5 points has triggers that are cheap to fire.** That is the point of
listing them rather than declaring victory.

## 1. The triggers, ranked by proximity

### T-1 · The cost-of-services split becomes disclosed — **LIVE NOW, and it is the binding one**

**Datum:** `Cost of services` fell `(2,289)` — filed, p.24. **IRDM does not decompose it**, and
states it *"includes ... cost of services for government and commercial engineering and support
service revenue"* — so **the line carries the licensed service line's cost AND the engineering
line's**, and the split is not published.

**Threshold:** the falsifier's value is a **linear function** of that split, and it is already
computed across its full range:

| Attribution of the `(2,289)` decline | Non-licensed share | Verdict |
|---|---:|---|
| **All to the licensed line** (most favourable) | **50.5%** | passes by 0.5 pts |
| All to the engineering line | **64.6%** | passes by 14.6 pts |

**So the trigger is not "does the split change the answer" — the answer is bounded to `[50.5%,
64.6%]` and holds across the entire range.** The trigger is narrower and sharper: **any
disclosure showing that MORE than the whole `(2,289)` decline belongs to the licensed line would
push the share below 0.50.** Since the total decline is only `2,289`, that requires the licensed
line's cost to have fallen by more than the *entire* cost-of-services decline — **arithmetically
impossible on this line.** **T-1 cannot fire.** Recorded as a trigger that resolves *against*
firing, which is worth more than one that stays open.

**⚠️ But the range's LOWER end is 50.5%, and that is where the exposure actually is** — not in the
cost line, but in **whether the licensed-line revenue growth is durable.** See T-3.

### T-2 · Aireon consolidation — **FIRED ALREADY, and the artifact is pre-close on purpose**

**Datum:** the Aireon acquisition **closed 2026-07-02**, twelve days after the period end.
**Threshold:** Q3 2026 (period ending 2026-09-30) is **the first quarter in which Aireon is
consolidated**, and the `Services` line's composition changes on that event.

**IRDM's `Services` line stops being the licensed-spectrum stream alone** once Aireon's hosting
and data revenue consolidates into it. **P1's instrument would then be measuring a different
object under the same label** — the segment boundary does not move, the contents do.

**Status: fired, and the consequence is scheduled rather than hypothetical.** *This artifact and
its methodology sibling are `standalone_pre_merger` and pre-close on two axes (deal not closed;
Aireon not consolidated), so **they expire at the Q3 print** — which is the correct and honest
life for them.*

### T-3 · The licensed line's `+5,758` growth reverses

**Datum:** `Services` **+5,758**, or **+4%** — the number P1's claim rests on, because it is what
*absorbs* the decline.
**Threshold:** **the falsifier's lower bound is set by this line alone.** If `Services` revenue
were **flat instead of `+5,758`**, the non-licensed share becomes `(16,250 − 0) / 16,250` on the
most favourable cost attribution... **no — restated correctly:** with the cost decline still
credited to the licensed line, licensed contribution falls from `8,047` to `2,289`, and the
non-licensed share rises to **`13,961 / 16,250 = 85.9%`** — *further* from firing.

**So T-3 fires in the opposite direction from intuition: a WEAKER licensed line strengthens P1's
pass.** That is a property of the metric's construction, and it is recorded because it means
**P1 as written cannot be refuted by the licensed line doing badly** — only by it doing
*impossibly well*. **A falsifier that is unreachable in the direction of the claim's own risk is
a weak falsifier**, and this is the second place in this thesis where that shape appears.

### T-4 · The `96.1%` government concentration in engineering-and-support turns

**Datum:** commercial engineering-and-support **`(0.7)`**, government **`+2.0`**, total **`+1.3`** —
so **`41.5 / 43.2 = 96.1%` of the line is government** and the commercial half **shrank 29%**.
**Threshold:** the line is **`43,142`, or 19% of revenue**, and it is the *second* place the
overlay compresses. **A single government contract award or loss moves it by more than the
commercial half's entire movement.** Datum: the next 10-Q's government engineering figure.

### T-5 · Subscriber-equipment margin inverts

**Datum:** equipment revenue `+7%` against its cost **`+19%`** — the compression P1 predicts.
**Threshold:** the line is small — `20,767` revenue against `13,478` cost, a **cost ratio of
64.9%** (filed), **up from `11,302 / 19,455 = 58.1%`** a year earlier. **A 6.8-point
deterioration in the cost of earning the same revenue line.**
**A further 7-point cost-ratio deterioration adds roughly `+1,500` to the expense side and moves
the non-licensed share up — again away from firing.** Same weak-falsifier shape as T-3.

### T-6 · A Q2 restatement

**Datum:** the served `operating_income` carries a **DA-29 back-solve signature**
(`computed −51,791,000` against `reported +51,791,000`, per 003's value-pool-map §8 item 11) —
**a value that appears to have been solved for rather than read.**
**Threshold:** any 10-K or 10-Q/A that restates Q2 2026 operating income to a figure other than
**34,008**. If the filed figure holds, **the served block's defect is a serving defect, not a
filing defect** — which is this artifact's working assumption and is confirmed by the identity
closing exactly on both periods.

## 2. What the trigger set says in aggregate

| # | Trigger | Status | Direction |
|---|---|---|---|
| T-1 | Cost-of-services split disclosed | **cannot fire** | — |
| T-2 | Aireon consolidation | **fired** (2026-07-02) | expires the artifact at Q3 |
| T-3 | Licensed line growth reverses | live | **away from firing** |
| T-4 | Government eng-support turns | live | away from firing |
| T-5 | Equipment margin inverts | live | away from firing |
| T-6 | Q2 restatement | open | confirms or removes DA-29 |

> ### ⚠️ FIVE OF SIX TRIGGERS CANNOT MOVE THE FALSIFIER ACROSS ITS BAR — and that is the finding
> **T-1 is arithmetically closed; T-3, T-4 and T-5 all move the share further from 0.5; T-2 is a
> clock, not a test.** **Only T-6 can change the verdict, and only by removing the figure
> entirely.**
>
> **This is not a comfortable position and it is not reported as one.** P1's IRDM falsifier passes
> at **50.5% against 0.5**, and the trigger set shows that **the pass is robust for reasons that
> have little to do with the thesis's actual risk.** The claim survives because the metric's
> construction makes the licensed line's weakness *count in its favour* — a property no reader
> would infer from the claim's wording, and **the reason this artifact exists.**
>
> **The correct reading of P1's IRDM pass is therefore: not falsified, AND not strongly tested.**
> **T-2 is the only thing that will produce a real test** — when Aireon consolidates, the licensed
> line is no longer isolable, and the instrument must be rebuilt rather than re-run.

**Carried, not resolved:** whether a falsifier that cannot fire in the direction of its claim's
own risk should be recorded as a **pass** or as **`UNEXERCISED`**. The thesis's own rule
(§0.2: a check that closes cleanly while testing nothing must be reported as itself) argues for
the latter. **Recorded as a finding for the P5 queue close-out rather than settled here.**

---

**Sources.** [IRDM 10-Q p.24](https://agentii.ai/v/IRDM/sec191/24) — the results-of-operations
table, all eight lines, and both component identities ·
[IRDM 10-Q p.26](https://agentii.ai/v/IRDM/sec191/26) — the $14.3M transaction cost disclosure
and the engineering-and-support commercial/government split.
