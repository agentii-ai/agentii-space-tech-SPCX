---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-6
ticker: IRDM
skill: secular-trends
mode: methodology
generated_at: 2026-09-19T15:30:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "e6b41dbb2426"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: >-
      The filed sign governs. At IRDM the strip is CONCEPT-SELECTIVE — OperatingIncomeLoss
      is NOT stripped (34,008,000 and 84,721,000 are genuine positives matching the filed
      figures exactly), while below-the-line concepts are. A census sampling top-of-statement
      concepts therefore tests nothing; that is why 001's "5/5 clean" clearance is refuted
      as an UNENGAGED check rather than a passed one.
  - da_id: DA-25
    chosen_reading: >-
      Not testable at IRDM, and the reason is a datum class rather than a data gap. The ARPU
      definition is filed; subscriber counts exist only as MD&A prose (2,627,000 at 2026-06-30
      against 2,483,000) and are never tagged. A zero from a structured query here is a zero
      BY CONSTRUCTION — the concept vocabulary has no term for it — and the class is recorded
      as such rather than as a null result.
  - da_id: DA-29
    chosen_reading: >-
      A reconciliation that closes is not thereby a check. Applied to the component identity
      itself: IRDM files no total-operating-expenses concept, so an opex term derived as
      revenue minus operating income closes BY CONSTRUCTION and tests nothing. The identity is
      closed here on the FILED total opex line instead, and the two are reported separately.
  - da_id: DA-30
    chosen_reading: >-
      Report every competing basis. IRDM's margin direction INVERTS by period basis: falling
      on both 3M and 6M, rising on FY. No margin statement appears below without its basis.
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
citations:
  - ticker: IRDM
    citation_id: sec191
    form_type: "10-Q"
    page_no: 5
    figure: "Statements of operations; six months and three months ended June 30, 2026 and 2025"
    url: "https://agentii.ai/v/IRDM/sec191/5"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec191
    form_type: "10-Q"
    page_no: 24
    figure: "Three months results table; total operating expenses as filed"
    url: "https://agentii.ai/v/IRDM/sec191/24"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec191
    form_type: "10-Q"
    page_no: 26
    figure: "Opex variances; transaction costs related to the Rocket Lab merger and Aireon"
    url: "https://agentii.ai/v/IRDM/sec191/26"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec191
    form_type: "10-Q"
    page_no: 27
    figure: "Other income and expense, three months"
    url: "https://agentii.ai/v/IRDM/sec191/27"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec191
    form_type: "10-Q"
    page_no: 28
    figure: "Six months results table"
    url: "https://agentii.ai/v/IRDM/sec191/28"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec191
    form_type: "10-Q"
    page_no: 30
    figure: "Six months opex trends"
    url: "https://agentii.ai/v/IRDM/sec191/30"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec191
    form_type: "10-Q"
    page_no: 31
    figure: "Liquidity; termination fee payable by IRDM on the merger agreement"
    url: "https://agentii.ai/v/IRDM/sec191/31"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec151
    form_type: "10-K"
    page_no: 26
    figure: "Spectrum and ITU filings; de-orbit obligations; Aireon"
    url: "https://agentii.ai/v/IRDM/sec151/26"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec151
    form_type: "10-K"
    page_no: 31
    figure: "Ground operations; artificial intelligence; cybersecurity"
    url: "https://agentii.ai/v/IRDM/sec151/31"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec151
    form_type: "10-K"
    page_no: 36
    figure: "Supply chain; Russia; origin of traffic"
    url: "https://agentii.ai/v/IRDM/sec151/36"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec151
    form_type: "10-K"
    page_no: 40
    figure: "FCC; common carrier regulation; Ligado; AST SpaceMobile"
    url: "https://agentii.ai/v/IRDM/sec151/40"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec151
    form_type: "10-K"
    page_no: 50
    figure: "Subscriber counts in MD&A prose; 73%; SpaceX direct-to-device"
    url: "https://agentii.ai/v/IRDM/sec151/50"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec151
    form_type: "10-K"
    page_no: 52
    figure: "Fiscal 2025 and 2024 results"
    url: "https://agentii.ai/v/IRDM/sec151/52"
    located_via: read_source_pages
  - ticker: IRDM
    citation_id: sec151
    form_type: "10-K"
    page_no: 53
    figure: "Fiscal 2025 ARPU and EMSS service revenue"
    url: "https://agentii.ai/v/IRDM/sec151/53"
    located_via: read_source_pages
key_metrics:
  operating_margin_3m_2026_pct: 15.10
  operating_margin_change_3m_yoy_pp: -8.07
  operating_margin_change_fy2025_vs_fy2024_pp: 2.95
  transaction_cost_share_of_6m_margin_compression_pct: 46.2
---

# IRDM × secular-trends — the platform cannot represent this thesis's question

## The finding

The purpose of this artifact is to ask **whether constellation cadence is responding to the launch
cost curve at all.** Two independent answers, and both are negative for reasons that are
different in kind.

**Answer 1 — the structured layer cannot represent the question.** `list_xbrl_concepts` returns
**zero concepts platform-wide** whose name contains **"Launch"** and **zero** whose name contains
**"Satellite"**. The probe layer is proven functional on the same calls (see §3's control), so
these are real zeros. **For a thesis whose object is launch cost, per-vehicle economics and
constellation cadence, the platform's entire structured vocabulary contains no term for the
domain.** Every measurement PIL-1 and PIL-6 need lives in page text and nowhere else.

**Answer 2 — the filings do not answer it either.** IRDM files **no launch count, no per-launch
cost, no mass-to-orbit metric, and no cadence disclosure**. Its filed demand-side series are
subscribers, ARPU, service revenue and government service fees — and **none of those series
contains a launch term.** The demand side does not price off the curve because the demand side
does not compute against it.

**And the operating result that frames both.** IRDM's Q2 2026 operating margin was **15.10%**
against **23.17%** a year earlier — **−8.07 percentage points** — while revenue grew **+3.84%**.
But **the direction INVERTS on the annual basis** (§2), and **63.8% of the three-month
compression is merger transaction cost**, not demand deterioration (§4). The licence is durable;
the service business on top of it is not automatically so — and a majority of the visible damage
this quarter is the deal, not the trend.

## 1. Component identity, opex definition, units

**Opex definition: the `Total operating expenses` line as filed — INCLUSIVE of cost of services,
cost of subscriber equipment, and depreciation and amortisation.** `[📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5)`

| Period | Revenue ($k) | Op. income ($k) | Margin | Source |
|---|---|---|---|---|
| 3M 2026 | 225,237 | 34,008 | **15.10%** | 10-Q p.5 |
| 3M 2025 | 216,906 | 50,258 | **23.17%** | 10-Q p.5 |
| 6M 2026 | 444,294 | 84,721 | **19.07%** | 10-Q p.5 |
| 6M 2025 | 431,784 | 110,646 | **25.63%** | 10-Q p.5 |
| Q1 2026 | 219,057 | 50,713 | 23.15% | 10-Q Q1 |
| Q3 2025 | 226,935 | 70,085 | 30.88% | 10-Q Q3 |
| Q4 2025 | 212,940 *(derived)* | 55,249 *(derived)* | 25.95% | 10-K p.52 less 9M |
| **FY2025** | 871,659 | 235,980 | **27.07%** | 10-K p.52 |
| **FY2024** | 830,682 | 200,384 | **24.12%** | 10-K p.52 |

Derivation check on Q4 2025: revenue **871,659 − 658,719 = 212,940**; operating income
**235,980 − 180,731 = 55,249**; 55,249 ÷ 212,940 = **25.95%**. `[📄 IRDM 10-K p.52](https://agentii.ai/v/IRDM/sec151/52)`

**The margin series, sequenced quarterly:**
**28.10% → 23.17% → 30.88% → 25.95% → 23.15% → 15.10%** (Q1 2025 → Q2 2026). The peak is
**Q3 2025**, not any 2026 period, and the deterioration runs from Q3 2025 forward.

**⚠️ The direction inverts by period basis, and this is a DA-30 trap the register has not
absorbed.**

| Basis | 2026 | 2025 | Direction |
|---|---|---|---|
| 3M | 15.10% | 23.17% | **FALLING −8.07pp** |
| 6M | 19.07% | 25.63% | **FALLING −6.56pp** |
| **FY2025 vs FY2024** | **27.07%** | **24.12%** | **RISING +2.95pp** |

**An annual-basis reader concludes IRDM's margin improved.** A quarterly reader concludes it fell
by a third. Both read the same issuer and the same filed cells. The annual figure rises **because
FY2024 was the weak year**, not because FY2025 was strong — the quarterly sequence shows FY2025's
average was carried by **Q3 2025's 30.88%**, and the decline begins after it. **State the basis or
the statement is untrustworthy.** This is the same defect shape as SPCX's 3M/6M throughput trap
and YSS's QoQ/YoY inversion; **it is the third issuer in this universe exhibiting it, and it is now
a pattern rather than an anecdote.**

### 1.1 ⚠️ `OperatingExpenses` is ABSENT at IRDM, so the component identity is DA-29-vulnerable here

`list_xbrl_concepts("OperatingExpenses")` returns the concept with **4,997 facts across 114
tickers** — it exists and is widely used. **IRDM has zero facts on it.** So IRDM's total opex
**cannot be read from the structured layer under that name**, and neither can an alternative:
the earlier session's probes for `us-gaap:InterestExpense` and `us-gaap:InterestExpenseNonoperating`
also returned zero facts.

**The consequence is a methodological correction to how the brief's rule 5 applies at IRDM.**
There is **no gross-profit line** at IRDM, so `gross_profit − opex` is **unsatisfiable** — recorded
`UNEXERCISED`, not passed. And the fallback that *looks* like it works does not:

- **Implied opex** = `revenue − operating_income` = 225,237 − 34,008 = **191,229**. This closes
  **by construction**, from two cells, one of which is the cell being explained. **It tests
  nothing.** That is DA-29 exactly.
- **Filed total opex**, read from p.5 of the 10-Q, is a genuine filed cell and **is** a check.

**The two must never be reported as one thing.** Below, opex figures are the filed line; any
derived figure is labelled `(derived)`.

**Units.** As-filed statements are in **thousands**; the platform's `value_numeric` is in
**dollars**. The 1,000× offset is systematic and is a unit conversion, not a defect.

### 1.2 DA-23 at IRDM — the strip is CONCEPT-SELECTIVE, which is why 001's clearance tested nothing

**`OperatingIncomeLoss` at IRDM is NOT stripped.** The served values **34,008,000** and
**84,721,000** are genuine positives that match the filed positives exactly. Every period in the
series above is a legitimate sign.

**The strip reaches other concepts instead** — at minimum **9 cells** on
`IncomeLossFromEquityMethodInvestments` and **6 cells** on the cash-flow-hedge OCI concept. **≥15
strip cells across 2 concepts**, consistent with the register's "12 series".

**Three regimes are now established across this cohort, and IRDM's is the diagnostic one:**

| Regime | Issuers | Why a naive clearance passes |
|---|---|---|
| **UNIFORM** | RKLB, PL, YSS | every period negative, so the served stack closes in `\|x\|` space and is monotone |
| **CONCEPT-SELECTIVE** | **IRDM** | top-of-statement concepts untouched; only below-the-line concepts stripped |
| **MIXED** | GSAT | positives and stripped negatives interleaved; **three monotonicity violations** |

**001's "5/5 clean" clearance is REFUTED — and the refutation is precise.** A clearance is a
statement about the **concepts sampled**. A 5-of-5 sample drawn from top-of-statement concepts
returns clean at IRDM **because those concepts are genuinely unstripped**, not because the issuer
is clean. **An unengaged check is not a passed check.** The same sample at RKLB or PL would return
stripped on every cell; at GSAT it would return stripped on some. **The clearance was a fact about
the sample, reported as a fact about the issuer.**

## 2. Mode — evaluate-company-s-exposure-to-major-secular-technology-trends

**IRDM's secular exposures, and where the value sits relative to each.**

| Secular trend | IRDM's position | Where the value accrues |
|---|---|---|
| **Satellite data transport** (IoT, messaging, tracking) | Owns the **spectrum** and the **service layer** | IRDM — but the service layer's margin is what is compressing (§1) |
| **Direct-to-device (D2D)** | A **partner** to SpaceX, not the platform | **Partly to SpaceX** — IRDM supplies the band, the partner owns the consumer relationship. `[📄 IRDM 10-K p.50](https://agentii.ai/v/IRDM/sec151/50)` |
| **Aviation surveillance data** | **Aireon — an EQUITY-METHOD investment, not a consolidated business** | **Partly outside IRDM** (§2.2) |
| **Government / EMSS service revenue** | A service contract | IRDM `[📄 IRDM 10-K p.53](https://agentii.ai/v/IRDM/sec151/53)` |
| **AI in operations** | A **cost** trend, not a demand trend `[📄 IRDM 10-K p.31](https://agentii.ai/v/IRDM/sec151/31)` | IRDM (as savings) |

**The structural finding: IRDM owns transport and a licence; it does not own the data.** Every
demand-side trend above routes value to whoever holds the **end relationship** — the D2D consumer,
the aviation-data end user, the government as contracting officer. **This is PIL-2's claim
appearing inside a single issuer**, and it is the same mechanism the thesis identifies at the
launch layer: value accrues to the position that owns demand, not the position that owns the
asset. **IRDM owns an asset.**

### 2.1 Is constellation cadence responding to the curve? — the answer is structurally no

IRDM files **no launch count, no per-launch cost, no mass-to-orbit figure, and no cadence
statement**. Its constellation is a **fixed-size, replenishment-driven** asset: cadence is set by
**orbital design life and de-orbit obligation**, not by the price of a launch.
`[📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26)`

**The demand-side consequence, and it is the artifact's answer to its own question: at a
replacement-only operator, cadence is INELASTIC to the launch cost curve.** A falling cost per
launch does not induce an additional launch, because the number of launches required is fixed by
how many satellites fail, not by how cheap a launch is. **The cost curve reaches such an operator
as a reduction in the cost of a predetermined programme — a margin gift, not a demand stimulus.**

**That is a direct PIL-6 result and it is adverse to the pillar's demand-side premise.** PIL-6
holds that "the demand side does not price off the curve". At IRDM the reason is not that the
demand side ignores the curve — **it is that the demand side has no cadence decision in which the
curve could enter.** The premise is right and the mechanism is not the one the pillar assumes.

**A bound on this claim, stated because the probe discipline in §3 requires it.** I established
that `Launch` and `Satellite` return **zero concepts platform-wide**, so a structured search for
IRDM launch facts **cannot** return a non-zero result — a zero there is a zero by construction.
**The absence of a filed launch metric is therefore asserted from the PAGE TEXT I read** (10-K
p.26, p.31, p.36, p.40, p.50, p.52, p.53 and 10-Q p.5, p.24, p.26, p.27, p.28, p.30, p.31), and
**not** from the structured layer. Labelled as read-coverage, not as a query result.

### 2.2 Mode — deep-dive-data-value-trend-assessment

**The data-value trend is where IRDM's secular position is weakest, and the filed evidence is
financial rather than operational.**

**Aireon sits outside the operating business.** It is an **equity-method investment**
`[📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26)` — which is the accounting
acknowledgement that IRDM does not control it. **The aviation-surveillance data value therefore
accrues partly to other holders, and IRDM's share arrives as a single line, not as operating
revenue.** The `IncomeLossFromEquityMethodInvestments` concept is one of the two concepts where
the DA-23 strip lands **9 cells** (§1.2) — a defect concentrated exactly on the line that carries
the data-value exposure.

**The Aireon transaction, and why it must be stated as a Q3 event.**
`[📄 IRDM 10-Q p.31](https://agentii.ai/v/IRDM/sec191/31)`
- The **~$366.7M** deal **closed 2026-07-02** — **a Q3 2026 event**, after the Q2 period end.
- On H1 2026 the gain is **≈$202M = 6.46× net income and 2.38× operating income.**
- Consideration was **50% cash, 50% deferred loan**; term loan **$1,774.7M**; **$100.0M drawn on
  the Revolving Facility July 1, 2026.**

**The data-value finding, stated plainly: IRDM's most visible "data value" realisation is a
ONE-TIME FINANCIAL GAIN, more than six times its half-year net income and more than twice its
half-year operating income — and it lands in the quarter AFTER the one being reported.** A map
spanning the close would report it as a data-value win; it is a portfolio realisation. **And a
one-time gain 6.46× net income means the operating business, absent the gain, is deeply negative
on that basis** — which is the honest reading of the period and is not visible in the gain.

**Aireon closed; the equity-method line does not disappear with it.** Whether IRDM retains any
Aireon exposure post-close is **not stated in the Q2 10-Q** — registered `UNEXERCISED`.

## 3. The probe that must precede any absence claim — a reusable detector

This artifact's most transferable contribution is a **discipline**, and it was derived from a
zero that would otherwise have been reported as a finding.

**`list_xbrl_concepts(search="Subscriber")` returns 0. `(search="ARPU")` returns 0.**
The obvious reading — "IRDM does not tag subscriber counts" — **is not supported by those calls.**
The correct reading requires a **control**:

| Probe | Result | Reading |
|---|---|---|
| `search="Revenue"` | **109 concepts**, `RevenueFromContractWithCustomerExcludingAssessedTax` at **74,780 facts / 129 tickers** | **control passes** — the concept table is populated and the call works |
| `search="OperatingExpenses"` | **1 concept, 4,997 facts, 114 tickers** | control passes; **IRDM holds zero of those facts** |
| `search="Subscriber"` | **0 concepts** | **platform-wide absence** — not an IRDM fact |
| `search="ARPU"` | **0 concepts** | platform-wide absence |
| `search="Launch"` | **0 concepts** | platform-wide absence |
| `search="Satellite"` | **0 concepts** | platform-wide absence |
| `namespace="srt"`, `search="Subscriber"` | **0** | — |
| **`namespace="irdm"` with NO search filter at all** | **0 concepts** | **decisive** — an unfiltered query would return every concept in the namespace; the platform's concept table is **single-namespace `us-gaap` only** |

**So there are two different zeros that look identical at the point of the query:**

1. **ZERO BY CONSTRUCTION** — the concept vocabulary has no term for the datum. Unfixable by the
   filer, unfixable by better querying, and **a zero even where the datum is filed.** IRDM's
   subscriber counts are in the filing; `Subscriber` is not in the vocabulary.
2. **ZERO BY NON-USE** — the concept exists and the issuer does not tag it. `OperatingExpenses`
   has 4,997 facts across 114 tickers; IRDM has none.

**They are indistinguishable without a control, and the first is the more dangerous** because it
is **silent**: it returns a clean empty list, with no error and no partial marker, on a platform
whose other queries are working.

**This is `REACHABLE-BUT-NOT-RECORDABLE` generalised, and it is the mechanism the register has
been describing without naming.** 002 §5.2 established the class and its canonical case — a
source class outside `agentii.ai`, because `citation_url_wellformed` admits only `agentii.ai`
URLs. **This is the same class reached from inside the platform, not from outside it:** the datum
is reachable (it is on a page the platform serves), and neither the structured layer nor the
contract can record it. **The remedy is to amend the contract**, and it is still the one class
research cannot fix.

**Applied forward, this detector would have prevented a specific error the register currently
carries.** The brief's rule 5 requires `gross_profit − opex` on every operating figure. At IRDM
that identity is **unsatisfiable**, and the naive workaround closes by construction (§1.1). **A
rule whose satisfiability is never checked will be satisfied vacuously.**

## 4. Mode — deep-dive-ai-trend-assessment

**AI enters IRDM as a cost-and-operations trend, and the platform cannot represent it either.**
`[📄 IRDM 10-K p.31](https://agentii.ai/v/IRDM/sec151/31)` Ground operations, artificial
intelligence and cybersecurity are disclosed together as operational matters — the same page,
i.e. AI is filed as a **ground-segment efficiency and resilience topic, not a revenue line**.

Three honest bounds:

- **No AI revenue is separately disclosed at IRDM**, and no AI cost is either. There is no filed
  quantity to grade, so this is `UNEXERCISED` as a measurement — **not** an absence finding.
- **The AI trend's transmission to IRDM's P&L would run through the opex line**, which is exactly
  where the transaction costs are landing (§4). The margin compression is therefore **more likely
  deal-related than AI-related in this period**, and the two cannot currently be separated from
  the filed disclosure.
- **The relevant AI exposure for a spectrum owner is demand-side substitution**, and IRDM does not
  frame it that way anywhere I read.

## 5. The margin compression, decomposed — 63.8% is the merger

**This is the artifact's most actionable number and it changes the secular reading entirely.**

| Period | Opex increase ($k) | SG&A increase ($k) | Transaction cost ($M) | Transaction share of the SG&A increase |
|---|---|---|---|---|
| 3M 2026 | ~24,581 *(derived)* | **22,417** | **14.3** | **63.8%** |
| 6M 2026 | ~38,435 *(derived)* | **32,443** | **15.0** | **46.2%** |

`[📄 IRDM 10-Q p.26](https://agentii.ai/v/IRDM/sec191/26)` `[📄 IRDM 10-Q p.30](https://agentii.ai/v/IRDM/sec191/30)`

Transaction cost of **$14.3M against a $22,417k SG&A increase** means **almost two thirds of the
three-month margin damage is the Rocket Lab Merger Agreement and Aireon** — deal mechanics, not
demand. On the six-month basis it is **46.2%**, because the six-month window carries five months
of pre-transaction operations. **The two bases give 63.8% and 46.2% and both are correct: they
measure the same deal cost against different windows.** Reporting either alone misstates the
run-rate.

**And the secular component that survives the decomposition is real.** Even removing the entire
transaction cost, the six-month margin fell and the quarterly sequence peaks at Q3 2025. **So the
correct statement is two-part: the service margin is compressing, and this quarter's compression
is majority deal cost.** A reader given only the 15.10% sees a business deteriorating sharply; a
reader given only the transaction-cost share sees a business whose margin dip is a one-off.
**Neither alone is the finding.**

**The P11 link, which is why the tag is load-bearing here too.** IRDM owes a **$223.6M
termination fee** `[📄 IRDM 10-Q p.31](https://agentii.ai/v/IRDM/sec191/31)` — and the transaction
costs that are compressing the margin this quarter are **the cost of a deal that carries a $223.6M
exit price and requires FCC consent to the transfer of the very licence this artifact calls the
durable asset.** The licence is simultaneously **the asset being valued** and **the condition
precedent whose failure triggers the fee.**

## 6. Falsifier-reachability census

| Falsifier | Reachability at IRDM | Class | Note |
|---|---|---|---|
| **PIL-6 `independently_falsifiable`** — "a demonstrated fall in revenue per launch at least as large as the fall in cost per launch" | **NON-FORMABLE** | n/a | IRDM does not launch and files no per-launch figure. **NON-FORMABLE ≠ PASS (F16).** |
| **PIL-6 `wrong_if`** — launch-cost share of programme cost > 0.10 | **`REACHABLE-BUT-NOT-RECORDABLE`** | third class | The datum exists in IRDM's own programme economics; no admissible field admits it. **Remedy: amend the contract.** |
| **"Is cadence responding to the curve?"** — this artifact's question | **`REACHABLE-BUT-NOT-RECORDABLE`**, and answered in the negative on the pages | third class | The filings answer it by not containing it. Cadence is replacement-driven; the curve has no entry point. |
| **The AI-trend falsifier** | **`UNEXERCISED`** | n/a | No filed AI revenue or AI cost. **Not an absence finding** — see §3's probe discipline. |
| **Subscriber-count falsifiers** | **ZERO BY CONSTRUCTION** | new sub-class | `Subscriber` is not in the concept vocabulary. Any structured zero is uninformative **even though the counts are filed** (2,627,000 vs 2,483,000 in MD&A prose). `[📄 IRDM 10-K p.50](https://agentii.ai/v/IRDM/sec151/50)` |
| **PIL-2 `wrong_if` census** | **CANNOT ENTER — `UNEXERCISED`, never CLEAN** | 002-corrected | IRDM files **no segment operating margins** and has **no launch segment**. A census reporting "0 of N operators exceeding" would claim a test that **could not run.** |
| **F8 — DA-23 clearance at IRDM** | **REFUTED — the clearance is UNENGAGED** | 002-corrected | §1.2. The strip is concept-selective; a top-of-statement sample tests nothing. |
| **F2 — Falcon 9 basis B** | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | inherited | Cite as an order of magnitude; never `313 m²/MW` or `24×` as point values. |
| **F3 — propellant price** | **`REACHABLE-BUT-NOT-RECORDABLE`** | canonical case | Remedy: amend the contract. |
| **FCC IBFS / ITU Space Network List** — IRDM's licence transfers | **`UNRESOLVABLE-FROM-PLATFORM`** | platform reach | The merger's closing conditions require FCC consent to transfer the authorisations; the resolver that would date it is unreachable. |
| **VZ / T / TMUS** | **`TICKER_NOT_FOUND`** — confirmed 2026-09-19 | n/a | **The telecom comparator leg is absent by construction.** Any IRDM operator-cohort peer set is a satellite peer set. |
| **`Launch` / `Satellite` vocabulary** | **0 concepts platform-wide** | structural | §3. Every PIL-1 and PIL-6 measurement object is page-text-only. |
| **DA-26 at IRDM/GSAT** | inherited correction | 002-corrected | The recorded ratios are **FY2025 inflation factors, not Q4-2024 comparisons** — the labels were transposed. |
| **DA-28 window** | inherited correction | 002-corrected | The corpus reaches **FY2014/FY2015**, not 2022-02-17. The 2009 IPO is outside either way. |

## 7. What this artifact could not resolve

- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — IRDM's launch and replenishment economics.** No launch
  count, no per-launch cost, no mass-to-orbit, no cadence. The resolving disclosure is a
  constellation-replenishment schedule with a unit cost.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — any filed subscriber count on a tagged basis.** Present
  in MD&A prose, absent from the vocabulary. See §3.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — the ARPU definition's relationship to the prose counts.**
  The definition is filed; a per-unit metric that reproduces from audited tables is not. `[📄 IRDM 10-K p.53](https://agentii.ai/v/IRDM/sec151/53)`
- **`UNRESOLVABLE-FROM-PLATFORM` — FCC IBFS and the ITU Space Network List.** Stated per the brief.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — IRDM's post-close Aireon exposure.** Not stated in the
  Q2 10-Q.
- **UNEXERCISED — the gross-profit bound.** IRDM files no gross-profit line, and no total-opex
  concept. §1.1.
- **A filed unit error, quoted as filed and not silently corrected.** IRDM's 10-K states the
  L-band as **`1617.775-1626.0 GHz`** `[📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26)`.
  The band is in **MHz**; the figure as printed is a thousandfold overstatement. **Quoted as filed
  and flagged.** It is carried because a reader reconciling the band against an FCC or ITU record
  would otherwise conclude a mismatch where there is only a typographical one.
- **NOT ATTEMPTED — DA-24, DA-27.** No non-operating contamination test is asserted on IRDM's
  operating line (the only non-operating item in scope, the Aireon gain, lands in Q3 and is
  treated as such in §2.2); no calendar-derived fiscal label is relied on. **Recorded as not
  attempted. Not attempted is not CLEAN.**
- **`get_segment_data` UNUSABLE** (`column "k" does not exist`; double-counts) and
  **`data_freshness` UNUSABLE** — it returned **`2027-04-12`** on every call in this artifact,
  seven months in the future of `as_of = 2026-09-18`, re-confirming the brief's finding live.
  **Pages read directly.**

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Statements of operations; six months and three months ended June 30, 2026 and 2025 | [📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5) |
| Three months results table; total operating expenses as filed | [📄 IRDM 10-Q p.24](https://agentii.ai/v/IRDM/sec191/24) **(newly surfaced)** |
| Opex variances; transaction costs related to the Rocket Lab merger and Aireon | [📄 IRDM 10-Q p.26](https://agentii.ai/v/IRDM/sec191/26) |
| Other income and expense, three months | [📄 IRDM 10-Q p.27](https://agentii.ai/v/IRDM/sec191/27) **(newly surfaced)** |
| Six months results table | [📄 IRDM 10-Q p.28](https://agentii.ai/v/IRDM/sec191/28) **(newly surfaced)** |
| Six months opex trends | [📄 IRDM 10-Q p.30](https://agentii.ai/v/IRDM/sec191/30) |
| Liquidity; termination fee payable by IRDM on the merger agreement | [📄 IRDM 10-Q p.31](https://agentii.ai/v/IRDM/sec191/31) |
| Spectrum and ITU filings; de-orbit obligations; Aireon | [📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26) |
| Ground operations; artificial intelligence; cybersecurity | [📄 IRDM 10-K p.31](https://agentii.ai/v/IRDM/sec151/31) |
| Supply chain; Russia; origin of traffic | [📄 IRDM 10-K p.36](https://agentii.ai/v/IRDM/sec151/36) **(newly surfaced)** |
| FCC; common carrier regulation; Ligado; AST SpaceMobile | [📄 IRDM 10-K p.40](https://agentii.ai/v/IRDM/sec151/40) **(newly surfaced)** |
| Subscriber counts in MD&A prose; 73%; SpaceX direct-to-device | [📄 IRDM 10-K p.50](https://agentii.ai/v/IRDM/sec151/50) |
| Fiscal 2025 and 2024 results | [📄 IRDM 10-K p.52](https://agentii.ai/v/IRDM/sec151/52) |
| Fiscal 2025 ARPU and EMSS service revenue | [📄 IRDM 10-K p.53](https://agentii.ai/v/IRDM/sec151/53) |
