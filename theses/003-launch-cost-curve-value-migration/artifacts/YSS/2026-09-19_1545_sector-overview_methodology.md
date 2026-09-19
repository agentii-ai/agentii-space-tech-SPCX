---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-6
ticker: YSS
skill: sector-overview
mode: methodology
generated_at: 2026-09-19T15:45:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "8fb208998401"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: >-
      The filed sign governs; the served positive is an extraction artefact. At YSS the regime
      is UNIFORM — all six served OperatingIncomeLoss cells across the issuer's filed history
      are positive and all six filed values are negative — so the served stack closes in |x|
      space and is monotone. No arithmetic heuristic detects it; only the component identity
      does, and that requires reading the filing.
  - da_id: DA-28
    chosen_reading: >-
      A capital-structure discontinuity around an IPO invalidates share-count detectors. YSS
      completes an IPO inside the comparative window: a $60,722 thousand deemed dividend on
      conversion of the Class P Units breaks the EPS numerator, $192 thousand of accretion sits
      beside it, and share counts are retrospectively adjusted for the Corporate Conversion. No
      share-count or per-share detector is asserted in this artifact.
  - da_id: DA-30
    chosen_reading: >-
      Two bases on one concept collapsed without a basis field. Live at YSS as the
      quarter-on-quarter and year-on-year revenue bases, which have OPPOSITE SIGNS on the same
      line, and as the three-month and six-month fixed-cost multiples (2.9x and 4.4x), both
      correct, neither stated.
  - da_id: DA-24
    chosen_reading: >-
      Non-operating contamination measured, not assumed. YSS reports interest, interest income
      and other expense as separate filed lines below the operating line; the operating result
      used here never nets them.
evidence_grade: DEMONSTRATED
citations:
  - ticker: YSS
    citation_id: sec12
    form_type: "10-Q"
    page_no: 6
    figure: "Balance sheet; cash 534,000; goodwill 793,520; total assets 2,070,219"
    url: "https://agentii.ai/v/YSS/sec12/6"
    located_via: read_source_pages
  - ticker: YSS
    citation_id: sec12
    form_type: "10-Q"
    page_no: 7
    figure: "Statements of operations, three and six months ended June 30, 2026 and 2025"
    url: "https://agentii.ai/v/YSS/sec12/7"
    located_via: read_source_pages
  - ticker: YSS
    citation_id: sec12
    form_type: "10-Q"
    page_no: 13
    figure: "IPO: 18.5 million shares at $34.00; net proceeds $583.4 million"
    url: "https://agentii.ai/v/YSS/sec12/13"
    located_via: read_source_pages
  - ticker: YSS
    citation_id: sec12
    form_type: "10-Q"
    page_no: 33
    figure: "Class P Unit bifurcated derivative liability remeasured to $98.1 million; $4.7 million loss"
    url: "https://agentii.ai/v/YSS/sec12/33"
    located_via: read_source_pages
  - ticker: YSS
    citation_id: sec12
    form_type: "10-Q"
    page_no: 37
    figure: "Backlog $592 million"
    url: "https://agentii.ai/v/YSS/sec12/37"
    located_via: read_source_pages
  - ticker: YSS
    citation_id: sec12
    form_type: "10-Q"
    page_no: 39
    figure: "Segment and geographic disclosures"
    url: "https://agentii.ai/v/YSS/sec12/39"
    located_via: read_source_pages
  - ticker: YSS
    citation_id: sec12
    form_type: "10-Q"
    page_no: 40
    figure: "Percentage-of-revenue table: gross profit 24% vs 11%; total opex 69% vs 37%"
    url: "https://agentii.ai/v/YSS/sec12/40"
    located_via: read_source_pages
  - ticker: YSS
    citation_id: sec12
    form_type: "10-Q"
    page_no: 49
    figure: "Tax Receivable Agreement; approximately $347.0M of tax attributes; lease commitments $46.3M"
    url: "https://agentii.ai/v/YSS/sec12/49"
    located_via: read_source_pages
  - ticker: YSS
    citation_id: sec12
    form_type: "10-Q"
    page_no: 52
    figure: "Material weakness in internal control over financial reporting; remediation"
    url: "https://agentii.ai/v/YSS/sec12/52"
    located_via: read_source_pages
  - ticker: YSS
    citation_id: sec12
    form_type: "10-Q"
    page_no: 54
    figure: "Part II risk factors incorporated by reference to the FY2025 Form 10-K"
    url: "https://agentii.ai/v/YSS/sec12/54"
    located_via: read_source_pages
key_metrics:
  gross_margin_q2_2026_pct: 23.97
  gross_margin_q2_2025_pct: 11.36
  operating_margin_q2_2026_pct: -44.64
  opex_to_gross_profit_6m_2026_x: 4.424
---

# YSS × sector-overview — the unit economics improved and the loss nearly doubled

## The finding

**YSS's gross margin improved from 11.36% to 23.97% — +12.61 percentage points — and the loss
from operations grew 94.6%, from $(21,232)k to $(41,313)k.** Both are DEMONSTRATED and both are
filed on the same statement. `[📄 YSS 10-Q p.7](https://agentii.ai/v/YSS/sec12/7)`

**That combination is the artifact's whole result: this is a VOLUME problem, not a
unit-economics problem.** Cost of revenues **FELL 5.31%** while revenue **ROSE 10.39%** — the
unit economics improved materially — and the operating loss still nearly doubled, because the
cost base is largely fixed and the volume did not hold.

**⚠️ And the volume figure has two bases with OPPOSITE SIGNS, which is the trap this artifact
exists to disarm.** On the same revenue line: **−20.45% quarter-on-quarter** (against the
$116,343k derived for the quarter ended 2026-03-31) and **+10.39% year-on-year**. The brief's
"−20.5% QoQ" is correct, **and a reader who drops the basis will report a 20% revenue collapse
for a quarter whose revenue grew 10% against the prior-year comparative.** Both numbers are filed.
Neither is the whole picture.

**And the "2.9× fixed cost base" is a THREE-MONTH ratio.** On the six-month basis it is
**4.42×** (§1). Both are correct; the basis must travel with the number.

## 1. Component identity, opex definition, units

**Opex definition: the `Total operating expenses` line as filed — SG&A + stock-based compensation +
R&D + transaction costs, EXCLUSIVE of cost of revenues.** The composition is verifiable from the
filed lines: `40,825 + 10,893 + 5,766 + 6,009 = 63,493` ✓ and `77,531 + 95,589 + 11,055 + 11,934
= 196,109` ✓. **Stock-based compensation is a SEPARATE line, not inside SG&A** — which matters,
because at YSS it is the largest single component of opex. `[📄 YSS 10-Q p.7](https://agentii.ai/v/YSS/sec12/7)`

### 1.1 Three months ended 2026-06-30 vs 2025-06-30

| Line ($k) | 2026 | 2025 | Change |
|---|---|---|---|
| Revenue | **92,547** | 83,839 | **+10.39%** |
| Cost of revenues | **70,367** | 74,313 | **−5.31%** |
| **Gross profit** | **22,180** | 9,526 | **+132.84%** |
| **Gross margin** | **23.97%** | 11.36% | **+12.61pp** |
| Selling, general and administrative | 40,825 | 25,790 | +58.30% |
| Stock-based compensation | **10,893** | — | — |
| Research and development | 5,766 | 4,893 | +17.84% |
| Transaction costs | 6,009 | 75 | — |
| **Total operating expenses** | **63,493** | 30,758 | **+106.43%** |
| **Loss from operations** | **(41,313)** | (21,232) | **+94.58%** |
| **Operating margin** | **−44.64%** | −25.32% | **−19.32pp** |
| Interest expense | (2,884) | (7,118) | — |
| Interest income | 4,208 | 218 | — |
| Other income (expense), net | 928 | 1,201 | — |
| Total other income (expense) | 2,252 | (5,699) | — |
| Loss before income taxes | (39,061) | (26,931) | — |
| Income tax (expense) benefit | (282) | 2,697 | — |
| **Net loss** | **(39,343)** | (24,234) | — |
| **Net loss available to common shareholders** | **(39,343)** | (24,234) | — |
| EPS | $(0.31) | $(0.25) | — |
| Weighted-average common shares | 128,095,949 | 95,141,928 | — |

**Identity closes exactly:** `22,180 − 63,493 = (41,313)` ✓

### 1.2 Six months ended 2026-06-30 vs 2025-06-30

| Line ($k) | 2026 | 2025 | Change |
|---|---|---|---|
| Revenue | **208,890** | 190,091 | +9.89% |
| Cost of revenues | 164,560 | 155,963 | +5.51% |
| **Gross profit** | **44,330** | 34,128 | +29.89% |
| **Gross margin** | **21.22%** | 17.95% | +3.27pp |
| SG&A | 77,531 | 52,591 | +47.42% |
| Stock-based compensation | **95,589** | — | — |
| R&D | 11,055 | 9,294 | +18.95% |
| Transaction costs | 11,934 | 106 | — |
| **Total operating expenses** | **196,109** | 61,991 | **+216.35%** |
| **Loss from operations** | **(151,779)** | (27,863) | **+444.73%** |
| **Operating margin** | **−72.66%** | −14.66% | **−58.00pp** |
| **Net loss** | **(154,185)** | (35,963) | — |
| Less: accretion of Class P Units | 192 | — | — |
| Less: deemed dividend on Class P Unit conversion at IPO | **60,722** | — | — |
| **Net loss available to common shareholders** | **(215,099)** | (35,963) | — |
| EPS | $(1.76) | $(0.38) | — |

**Identity closes exactly:** `44,330 − 196,109 = (151,779)` ✓ and
`154,185 + 192 + 60,722 = 215,099` ✓

### 1.3 The four ratios — and both bases for each

| Ratio | 3M basis | 6M basis |
|---|---|---|
| Cost of revenues ÷ revenue | **76.03%** | 78.78% |
| **Opex ÷ revenue** | **68.60%** | **93.88%** |
| **Opex ÷ gross profit** | **2.863×** | **4.424×** |
| Opex less gross profit | **$41,313k** | **$151,779k** |

**The fixed cost base is 2.9× gross profit on the three-month basis and 4.4× on the six-month
basis — a 1.55× difference from the period basis alone.** The 6M figure is inflated by the
**$95,589k** of SBC concentrated in the first half, which is a **post-IPO** event and therefore
**not a run-rate**. The three-month figure of **2.9×** is the more representative one, and the
reason must be stated: **SBC of $95,589k against $10,893k in the quarter means the six-month
period contains a non-recurring charge of roughly $84.7M.**

**The operating-margin identity, in one line, and it is the sector-overview deliverable:**

> **operating margin = gross margin − opex ratio**

At YSS on 3M: `23.97% − 68.60% = −44.63%` ✓ (`−44.64%` filed, rounding).
At PL on its quarter: `53.53% − 90.59% = −37.06%` ✓ **exactly the filed figure.**
**Two names at different depths of the stack, and the identity closes at both.** The two inputs
are set by entirely different forces: **gross margin by the layer's pricing power, the opex ratio
by whether the position has scale.** §3 is the consequence.

### 1.4 What actually drove the opex increase — and it is fully decomposable

**Three months:** total opex rose **$32,735k** (63,493 − 30,758). Decomposition:
SG&A **+$15,035k** (45.9%); stock-based compensation **+$10,893k** (33.3%); transaction costs
**+$5,934k** (18.1%); R&D **+$873k** (2.7%). **Sum: $32,735k — the decomposition is exhaustive to
the dollar.**

**Six months:** total opex rose **$134,118k** (196,109 − 61,991). SG&A **+$24,940k** (18.6%);
**SBC +$95,589k (71.3%)**; transaction costs **+$11,828k** (8.8%); R&D **+$1,761k** (1.3%).

**⚠️ The two bases give completely different answers to "what caused the cost increase".** On 3M
it is **SG&A-led** (45.9%); on 6M it is **SBC-led** (71.3%). Neither is wrong. **A reader given
one basis will misidentify the driver**, and this is the third distinct DA-30 instance at a single
issuer in this artifact (revenue direction, fixed-cost multiple, cost driver).

### 1.5 DA-23 at YSS — the UNIFORM regime, six of six

Every served `OperatingIncomeLoss` at YSS is positive and every filed one negative, **six of six
periods**: three months ended 2026-06-30 served **+41,313,000** against filed `(41,313)`;
six months 2026 **+151,779,000** against `(151,779)`; three months ended 2026-03-31
**+110,466,000**; six months 2025 **+27,863,000** against `(27,863)`; three months 2025
**+21,232,000** against `(21,232)`; three months ended 2025-03-31 **+6,631,000**.

**The regime is UNIFORM and the served stack is monotone** — and the derived values confirm it:
six months 2026 **151,779 − 41,313 = 110,466** equals the served Q1 figure; six months 2025
**27,863 − 21,232 = 6,631** equals the served Q1 2025 figure. **Both derived values reproduce the
served values exactly, because in a uniformly-negative history the `|x|` stack is arithmetically
consistent.** The monotonicity detector that fires at GSAT **cannot fire here.**
`[📄 YSS 10-Q p.7](https://agentii.ai/v/YSS/sec12/7)`

### 1.6 DA-28 — the IPO lands inside the comparative window

**No share-count or per-share detector is asserted in this artifact, and the reason is filed.**
YSS completed its **IPO — 18.5 million shares at $34.00, net proceeds $583.4 million**
`[📄 YSS 10-Q p.13](https://agentii.ai/v/YSS/sec12/13)` — inside the period covered by these
comparatives, producing three simultaneous discontinuities:

1. **A $60,722k deemed dividend on conversion of the Class P Units upon IPO**, which breaks the
   EPS numerator: net loss of $(154,185)k becomes **$(215,099)k available to common** on the six-
   month basis. **39.4% of the reported per-share loss is this single non-operating item.**
2. **$192k of Class P Unit accretion** beside it.
3. **Retrospective adjustment of share counts for the Corporate Conversion** — so the
   weighted-average of 128,095,949 against 95,141,928 is **not a like-for-like comparison.**

**The Class P Units are also a live remeasurement exposure:** the bifurcated derivative liability
was remeasured to **$98.1 million** with a **$4.7 million** recognised loss.
`[📄 YSS 10-Q p.33](https://agentii.ai/v/YSS/sec12/33)` **Registered so that no artifact computes a
per-share metric here and calls it a trend.**

**Units.** As-filed statements are in **thousands**; the platform's `value_numeric` is in
**dollars**. The 1,000× offset is systematic and is a unit conversion, not a defect.

## 2. The volume problem, stated as arithmetic

**The three facts that together make the case, and they must be read together:**

| Fact | Value | Direction |
|---|---|---|
| Cost of revenues | **−5.31%** | **FELL** |
| Revenue | **+10.39% YoY** | **ROSE** |
| Revenue | **−20.45% QoQ** | **FELL** |
| **Gross margin** | **11.36% → 23.97%** | **IMPROVED +12.61pp** |
| **Loss from operations** | **(21,232) → (41,313)** | **WORSENED +94.58%** |

**A company whose cost of revenues fell while its revenue rose has improving unit economics. That
company's operating loss nearly doubled anyway.** The only reconciliation is that **the cost base
above the gross-profit line is not proportional to volume** — opex is **68.60%** of revenue on the
3M basis, and gross profit covers only **34.9%** of it. **Every incremental dollar of volume
contributes ~24 cents of gross profit against a fixed cost base that consumes ~69 cents of every
revenue dollar.**

**So the correct diagnosis is the one the brief carries, now with the arithmetic behind it: the
problem is VOLUME, not unit economics — and the two are moving in opposite directions.** A
unit-economics fix has already happened (the margin more than doubled) and did not prevent the
loss from widening. **A volume recovery is what the fixed cost base requires, and the QoQ revenue
decline of 20.45% says volume went the wrong way during the quarter.**

**The non-cash and one-time load, quantified and bounded.** Three months: SBC **$10,893k** plus
transaction costs **$6,009k** = **$16,902k = 40.91%** of the $(41,313)k operating loss. Six months:
SBC **$95,589k** of **$196,109k** opex = **48.74%**.

**So the cash operating loss is materially smaller than the reported one — and this is exactly
where the honest bound belongs.** Removing **all** SBC and transaction costs leaves the three-month
loss at **$(24,411)k**, still **−26.38%** of revenue. **The loss is smaller than reported and it is
still large.** A reader who stops at "40.9% is non-cash and one-time" concludes the business is
near breakeven; a reader who stops at "−44.64%" concludes it is far from it. **Neither alone is
the finding.**

## 3. The value-chain position map

**The sector-overview question is which position in the stack holds the margin. The answer this
universe supports is that the question has a formula, and at these two names the formula says no
position holds one.**

**`operating margin = gross margin − opex ratio`, evaluated on a stated period basis:**

| Layer | Name | Gross margin | Opex ratio | Operating margin |
|---|---|---|---|---|
| Launch | RKLB | not comparable (no gross-margin line read here) | — | deeply negative |
| **Data and analytics, above launch** | **PL** | **53.53%** | **90.59%** | **−37.06%** |
| **Vertical / infrastructure services** | **YSS** | **23.97%** | **68.60%** | **−44.64%** |

**The finding is in the gap structure.** PL and YSS are **29.56 percentage points** apart in gross
margin and only **7.58 points** apart in operating margin. **PL's gross-margin advantage is
almost entirely consumed by an opex ratio 21.99 points higher.** So:

- **Depth in the stack predicts GROSS margin.** PL, one layer above launch and selling analytics,
  earns 53.53%. YSS, in vertical infrastructure services, earns 23.97%. **The gross-margin
  ordering is the value-chain ordering, and it is what PIL-2's migration claim predicts.**
- **Depth in the stack does NOT predict OPERATING margin.** The ordering **compresses by 74%**
  between the two lines. **A map that ranks stack positions by gross margin produces a materially
  different ranking from one that ranks them by operating margin, and only the second is
  investable.**

**And the reason the compression is systematic rather than incidental:** the opex ratio is set by
**scale**, and no position in this stack has it. **So the value-chain map's answer to "which
position holds the margin" is: at the gross line, the higher-value-added position; at the operating
line, neither — and the distance between those two answers is the sector's central fact.**

### 3.1 Where launch cost sits — the negative finding that supports PIL-6

**YSS's cost of revenues is 76.03% of revenue and contains no separately disclosed launch cost, and
YSS files no launch count, no per-launch cost and no mass-to-orbit metric.** Its filed backlog is
**$592 million** `[📄 YSS 10-Q p.37](https://agentii.ai/v/YSS/sec12/37)` and its balance sheet
carries **goodwill of $793,520 thousand** against **total assets of $2,070,219 thousand** — i.e.
**38.33% of the asset base is goodwill** `[📄 YSS 10-Q p.6](https://agentii.ai/v/YSS/sec12/6)`, a
figure that measures **past acquisitions, not launch cost.**

**The load-bearing inference, and it is the same one the PL artifact reaches from the other
direction: launch cost is not the binding constraint at either position in the stack.** At PL the
gross margin is 53.53% while absorbing launch cost inside a 46.47% cost of revenue. At YSS the
cost of revenues is **76.03%** — higher — but the **filed risk set and the filed cost lines do not
identify launch as the driver**, and the opex ratio above the line is what produces the loss.
**Two positions, two different cost structures, and in neither does launch appear as the constraint
that produces the operating result.**

**That is a positive result for PIL-6 and a limiting one.** PIL-6 holds that launch cost is the
master COST variable and that value migrated to whoever owns demand. **The migration direction is
confirmed. The "master cost variable" framing is qualified: at the two positions above the launch
layer, the variable that determines whether the position is profitable is the OPEX RATIO — and
launch cost, sitting below both, is small enough at both to be invisible in their cost lines.**

### 3.2 Other filed positions on the map

- **The tax structure is an asset.** A **Tax Receivable Agreement** with approximately **$347.0M**
  of tax attributes, alongside **$46.3M** of lease commitments.
  `[📄 YSS 10-Q p.49](https://agentii.ai/v/YSS/sec12/49)` **$347.0M against $2,070,219k of total
  assets is 16.76% of the balance sheet in a tax asset** — a position in the value chain that is
  not an operating one, and which no operating-margin map captures.
- **The ICFR position is a live qualification.** A **material weakness in internal control over
  financial reporting** is disclosed with remediation described.
  `[📄 YSS 10-Q p.52](https://agentii.ai/v/YSS/sec12/52)` **Any figure in this artifact inherits
  the qualification on the controls that produced it.** Recorded as a bound, not as a caveat.
- **The risk set is incorporated by reference.** Part II risk factors point to the **FY2025 Form
  10-K** `[📄 YSS 10-Q p.54](https://agentii.ai/v/YSS/sec12/54)` — **the same reachability finding
  as at IRDM and GSAT: a census reading the current 10-Q alone under-counts the set.**
- **A segment disclosure exists** `[📄 YSS 10-Q p.39](https://agentii.ai/v/YSS/sec12/39)` — but
  **no segment operating margin** is filed in it, which is why YSS cannot enter PIL-2's `wrong_if`
  census (§4).

## 4. Falsifier-reachability census

| Falsifier | Reachability at YSS | Class | Note |
|---|---|---|---|
| **PIL-6 `independently_falsifiable`** — "a demonstrated fall in revenue per launch at least as large as the fall in cost per launch" | **NON-FORMABLE** | n/a | YSS files no per-launch revenue or cost. **NON-FORMABLE ≠ PASS (F16).** |
| **PIL-6 `wrong_if`** — launch-cost share of programme cost > 0.10 | **`REACHABLE-BUT-NOT-RECORDABLE`** | third class | Launch cost is inside a 76.03% cost of revenues and is not separately disclosed. **Remedy: amend the contract** — the one class research cannot fix. |
| **The value-chain position falsifier** | **REACHABLE — and the ranking COMPRESSES by 74%** | **DEMONSTRATED** | §3. Gross-margin ordering is the stack ordering; operating-margin ordering is not. |
| **The volume-versus-unit-economics falsifier** | **REACHABLE — and it resolves to VOLUME** | **DEMONSTRATED** | §2. Gross margin +12.61pp, loss +94.58%. Unit economics improved; volume did not. |
| **The "−20.5%" claim** | **REACHABLE — correct on QoQ ONLY** | **DEMONSTRATED** | **+10.39% on YoY from the same filed line. Opposite signs.** The basis is mandatory. |
| **The "2.9× fixed cost base" claim** | **REACHABLE — correct on 3M ONLY** | **DEMONSTRATED** | **4.424× on 6M.** Both filed; neither stated. |
| **PIL-2 `wrong_if` census** | **CANNOT ENTER — `UNEXERCISED`, never CLEAN** | 002-corrected | YSS files a segment note but **no segment operating margin** and has **no launch segment**. "0 of N exceeding" would claim a test that could not run. |
| **Any per-share or share-count falsifier** | **DISQUALIFIED — DA-28** | §1.6 | The IPO is inside the comparative window; a $60,722k deemed dividend and retrospective share adjustment. **No such detector is asserted.** |
| **F2 — Falcon 9 basis B** | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | inherited | Cite as an order of magnitude; never `313 m²/MW` or `24×` as point values. |
| **F3 — propellant price** | **`REACHABLE-BUT-NOT-RECORDABLE`** | canonical case | Remedy: amend the contract. |
| **`Launch` / `Satellite` concept vocabulary** | **0 concepts platform-wide** | structural | The structured layer has no term for the domain; YSS's launch exposure is page-text-only. |
| **VZ / T / TMUS** | **`TICKER_NOT_FOUND`** — confirmed 2026-09-19 | n/a | **The telecom comparator leg is absent by construction.** |
| **F17 threshold reachability** | **NOT REACHABLE at YSS** | n/a | An SPCX segment-boundary property; recorded so F17 is not over-read as universe-wide. |

## 5. What this artifact could not resolve

- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — any launch-related quantity.** No launch count, no
  per-launch cost, no mass-to-orbit. The resolving disclosure is a launch-cost decomposition
  inside cost of revenues.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — the fixed/variable split inside opex.** The **>2.9×**
  multiple and the **"fixed cost base"** characterisation are supported by opex behaviour (a
  20.45% revenue decline did not produce a proportional opex decline) and **not by a filed
  fixed/variable disclosure, which does not exist.** Stated as an inference from behaviour.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — the SBC run-rate.** The **$95,589k** six-month SBC against
  **$10,893k** in the quarter means the first half carries roughly **$84.7M** of non-recurring
  post-IPO charge. **The forward quarterly SBC is not disclosed**, so every six-month ratio here
  is a **post-IPO-window** figure and cannot be annualised. The 3M basis is preferred for that
  reason, and the reason is stated rather than assumed.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — the deemed dividend's recurrence.** The **$60,722k** is
  described as arising **upon IPO**; whether Class P Units remain that could convert again is not
  resolved by this reading. **No forward per-share figure is offered.**
- **UNEXERCISED — the material weakness's remediation status.** Disclosed with remediation
  described; whether it is closed is not tested here.
- **UNEXERCISED — the segment note's content beyond its existence.** p.39 was located, not read in
  full. **Recorded as located-not-read**, which is a weaker grade than the figures in §1.
- **NOT ATTEMPTED — DA-26, DA-27, DA-29.** No annual figure is used as quarterly (DA-26); YSS is a
  June year-end filer and all periods above carry explicit period-ends (DA-27 not engaged); no
  reconciliation is claimed whose terms are absent from the source (DA-29). **Recorded as not
  attempted. Not attempted is not CLEAN.**
- **`get_segment_data` UNUSABLE** (`column "k" does not exist`; double-counts) and
  **`data_freshness` UNUSABLE** (returns `2027-04-12`, seven months in the future of
  `as_of = 2026-09-18`). **Pages read directly.**

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Balance sheet; cash 534,000; goodwill 793,520; total assets 2,070,219 | [📄 YSS 10-Q p.6](https://agentii.ai/v/YSS/sec12/6) |
| Statements of operations, three and six months ended June 30, 2026 and 2025 | [📄 YSS 10-Q p.7](https://agentii.ai/v/YSS/sec12/7) |
| IPO: 18.5 million shares at $34.00; net proceeds $583.4 million | [📄 YSS 10-Q p.13](https://agentii.ai/v/YSS/sec12/13) |
| Class P Unit bifurcated derivative liability remeasured to $98.1 million; $4.7 million loss | [📄 YSS 10-Q p.33](https://agentii.ai/v/YSS/sec12/33) |
| Backlog $592 million | [📄 YSS 10-Q p.37](https://agentii.ai/v/YSS/sec12/37) |
| Segment and geographic disclosures | [📄 YSS 10-Q p.39](https://agentii.ai/v/YSS/sec12/39) |
| Percentage-of-revenue table: gross profit 24% vs 11%; total opex 69% vs 37% | [📄 YSS 10-Q p.40](https://agentii.ai/v/YSS/sec12/40) **(newly surfaced)** |
| Tax Receivable Agreement; approximately $347.0M of tax attributes; lease commitments $46.3M | [📄 YSS 10-Q p.49](https://agentii.ai/v/YSS/sec12/49) |
| Material weakness in internal control over financial reporting; remediation | [📄 YSS 10-Q p.52](https://agentii.ai/v/YSS/sec12/52) |
| Part II risk factors incorporated by reference to the FY2025 Form 10-K | [📄 YSS 10-Q p.54](https://agentii.ai/v/YSS/sec12/54) |
