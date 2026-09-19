---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-2
ticker: PL
skill: supply-chain
mode: methodology
generated_at: 2026-09-19T14:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: >
      The filing this artifact rests on is DA-23-AFFECTED: the platform serves
      `us-gaap:OperatingIncomeLoss` = **+34,888,000** for 2026-02-01→2026-04-30 against a filed
      **$(34,888)** thousand, equal magnitude and opposite sign, while the same period's
      `us-gaap:GrossProfit` = 50,401,000 is **genuinely positive**. **Every sign in this artifact is
      taken from the read page, never from a served fact.** The component identity in §1 is the
      detector and it closes on five periods, including one where the served and filed signs agree.
  - da_id: DA-30
    chosen_reading: >
      Two instances, both named at the point of use. (1) **Cost of revenue is disclosed by PL on
      two bases in the same filing** — consolidated GAAP (43,749k) and the segment-expense
      presentation "exclusive of" depreciation, stock-based compensation, restructuring, earnout
      payroll taxes and certain litigation (33,074k). A reader who takes the second as cost of
      revenue gets a 64.9% gross margin against a filed 53.5%. This artifact uses the **consolidated
      GAAP basis** for every ratio and says so. (2) **Gross margin is reported on two bases by the
      issuer** (GAAP 53.5% / non-GAAP 56.3% in the quarter) and both are given everywhere.
  - da_id: DA-27
    chosen_reading: >
      **CONFIRMED with a mechanism.** The platform labels the quarter ended 2026-04-30 as
      `fiscal_year 2026, fiscal_period Q1`; PL's own 10-Q labels it **Q1 FY2027**. Three matched
      pairs establish the rule: the platform's `fiscal_year` is the **calendar year in which PL's
      fiscal year begins**, while PL labels the fiscal year by the **calendar year in which it
      ends**. Every platform PL fiscal-year label is therefore exactly **one lower** than the
      issuer's. Issuer labels are used throughout this artifact, with the platform's label given
      where the platform is quoted.
  - da_id: DA-26
    chosen_reading: >
      **CONFIRMED at PL, and the proof is the absence of the underlying fact.** The platform's ratio
      row `fiscal_year 2025, fiscal_period Q4, gross_margin 0.5605` equals the **FY2026 ANNUAL**
      ratio exactly (172,485/307,727 = 0.56051), and `search_xbrl_facts(concept=GrossProfit,
      fiscal_period=Q4, ticker=PL)` returns **zero rows** — there is no Q4-only fact from which it
      could have been computed. An annual figure served in a quarterly slot. A second cell in the
      same row, `operating_margin 0.3774`, reconciles to **no same-period pairing at all** (§1.3).
  - da_id: DA-21
    chosen_reading: >
      PL's own boundary, as filed: **one reportable segment** — the note is titled "Financial
      information for the Company's reportable segment" (singular) and presents a single column.
      There is no launch/non-launch or product/service split to price against, which is what makes
      PIL-2's registered falsifier unevaluable here (§6) rather than satisfied. No normative
      restatement is attempted; the boundary is recorded as the reason the comparison does not exist.
evidence_grade: DEMONSTRATED
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "Component identity, quarter — Revenue 94,150 / Cost of revenue 43,749 / Gross profit 50,401 / Total operating expenses 85,289 / Loss from operations (34,888); prior-year 66,265 / 29,662 / 36,603 / 59,374 / (22,771); cost-of-revenue drivers +5.8 subcontractors, +2.6 spacecraft hardware, +2.0 ground station, +2.0 employee-related, +1.2 hosting"
    ticker: PL
    citation_id: sec76
    page_no: 38
    url: https://agentii.ai/v/PL/sec76/38
    located_via: read_source_pages
  - figure: "Component identity, annual, three years — Revenue 307,727 / 244,352 / 220,696; Cost of revenue 135,242 / 104,627 / 107,746; Gross profit 172,485 / 139,725 / 112,950; R&D 106,749 / 101,006 / 116,339; S&M 72,676 / 77,694 / 86,304; G&A 88,133 / 77,147 / 80,055; Total operating expenses 267,558 / 255,847 / 282,698; Loss from operations (95,073) / (116,122) / (169,748); years ended January 31, 2026 / 2025 / 2024"
    ticker: PL
    form_type: 10-K
    citation_id: sec60
    page_no: 95
    url: https://agentii.ai/v/PL/sec60/95
    located_via: read_source_pages
  - figure: "PL sec76 p.29"
    ticker: PL
    citation_id: sec76
    page_no: 29
    url: https://agentii.ai/v/PL/sec76/29
    located_via: read_source_pages
  - figure: "Gross margin on both bases, and Adjusted EBITDA — GAAP Gross Profit 50,401 / prior 36,603; SBC 1,804; amortization of acquired intangibles 820; earnout payroll taxes (57); Non-GAAP Gross Profit 52,968 / 38,850; Gross Margin 54% / 55%; Non-GAAP Gross Margin 56% / 59%; Adjusted EBITDA $(1,033) vs $1,199"
    ticker: PL
    citation_id: sec76
    page_no: 41
    url: https://agentii.ai/v/PL/sec76/41
    located_via: read_source_pages
  - figure: "PL sec76 p.59"
    ticker: PL
    citation_id: sec76
    page_no: 59
    url: https://agentii.ai/v/PL/sec76/59
    located_via: read_source_pages
  - figure: "Where the cost concentration actually is — launch services non-cancelable purchase commitments $4.7 million total (fiscal years through 2028) against Google hosting minimum purchase commitments $25,118.0 thousand plus $33,427.0 thousand"
    ticker: PL
    citation_id: sec76
    page_no: 20
    url: https://agentii.ai/v/PL/sec76/20
    located_via: read_source_pages
  - figure: "PL sec76 p.60"
    ticker: PL
    citation_id: sec76
    page_no: 60
    url: https://agentii.ai/v/PL/sec76/60
    located_via: read_source_pages
  - figure: "PL sec76 p.36"
    ticker: PL
    citation_id: sec76
    page_no: 36
    url: https://agentii.ai/v/PL/sec76/36
    located_via: read_source_pages
  - figure: "PL sec76 p.11"
    ticker: PL
    citation_id: sec76
    page_no: 11
    url: https://agentii.ai/v/PL/sec76/11
    located_via: read_source_pages
  - figure: "PL sec60 p.79"
    ticker: PL
    form_type: 10-K
    citation_id: sec60
    page_no: 79
    url: https://agentii.ai/v/PL/sec60/79
    located_via: read_source_pages
  - figure: "The 10-K version of the launch-availability risk factor, truncated relative to the 10-Q — the supplier list runs to SpaceX without Stoke Space Technologies, Inc."
    ticker: PL
    form_type: 10-K
    citation_id: sec60
    page_no: 29
    url: https://agentii.ai/v/PL/sec60/29
    located_via: read_source_pages
key_metrics:
  hosting_to_launch_commitment_multiple_x: 12.5
  cost_of_revenue_two_basis_difference_pct_of_line: 32.3
  segment_basis_gross_margin_overstatement_pp: 11.4
  cost_of_revenue_reduction_needed_to_close_gap_pct: 79.7
---

# PL — Supply Chain: The Universe's Best Gross Margin, and the Binding Constraint Is Fixed Cost, Not Launch Cost

**Sources.** Form 10-Q, accession `0001193125-26-258304`, quarter ended 2026-04-30 (**Q1 FY2027** on
the issuer's calendar), filed 2026-06-05, 92 pages (`sec76`); Form 10-K, accession
`0001193125-26-119957`, year ended 2026-01-31 (`FY2026`), filed 2026-03-23, 155 pages (`sec60`).
PL's fiscal year ends January 31; the issuer labels by the year the fiscal year **ends**.

**The finding.** Planet Labs buys launch from **three universe members** — it names **RKLB, FLY
(Firefly) and SPCX (SpaceX)** among nine qualified providers — and **launch is not where its money
goes.** PL's cost concentration is **people, subcontractors and cloud hosting**: the entire
non-cancelable launch commitment through fiscal 2028 is **$4.7M**, against **$58,545k** of Google
hosting commitments, a factor of **12.5×**. The consequence for this thesis is a clean, arithmetic
answer to the demand-side question: PL books the universe's **best gross margin — 53.5% GAAP
(56.3% non-GAAP) in the quarter** — and still loses **$(34,888)k, or (37.1)% of revenue, at the
operating line**, because **opex is 90.6% of revenue**. Closing that gap by the cost-of-revenue
route needs a **79.7%** reduction; by the opex route, **40.9%**. **The whole multi-year launch
commitment, spent at once, would close 13.5% of one quarter's operating loss.** PL is the cleanest
test of PIL-6 in the universe precisely because **a collapse in launch price would barely move its
operating line.** And its supply-chain leg is also where two platform defects land hard: PL
discloses **cost of revenue on two bases** whose difference is 32.3% of the line (§2), and the
platform serves its operating margin with the sign stripped (§1.3).

---

## 1. The component identity first, with the opex definition, on five periods

The contract requires the derivation in-line for any artifact reading `operating_income`.
**Opex definition used throughout: `total operating expenses` = `Research and development` +
`Sales and marketing` + `General and administrative`**, with **cost of revenue excluded** — PL's
income statement has exactly these three operating-expense lines and no others, so the definition
is complete and carries no residual term. (Do **not** reach for `us-gaap:CostsAndExpenses` here: it
would include cost of revenue and the identity would be false by exactly that amount.)

| Period | Revenue | − Cost of revenue | = Gross profit | − Total opex | = Computed | Filed loss from operations | Closes? |
|---|---|---|---|---|---|---|---|
| **Q1 FY2027** (3M to 2026-04-30) | 94,150 | 43,749 | **50,401** *(53.5%)* | 85,289 | **(34,888)** | **(34,888)** | ✅ |
| **Q1 FY2026** (3M to 2025-04-30) | 66,265 | 29,662 | **36,603** *(55.2%)* | 59,374 | **(22,771)** | **(22,771)** | ✅ |
| **FY2026** (12M to 2026-01-31) | 307,727 | 135,242 | **172,485** *(56.0%)* | 267,558 | **(95,073)** | **(95,073)** | ✅ |
| **FY2025** (12M to 2025-01-31) | 244,352 | 104,627 | **139,725** *(57.2%)* | 255,847 | **(116,122)** | **(116,122)** | ✅ |
| **FY2024** (12M to 2024-01-31) | 220,696 | 107,746 | **112,950** *(51.2%)* | 282,698 | **(169,748)** | **(169,748)** | ✅ |

Five periods, all close exactly. Thousands of USD. Quarter sources:
[📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38) and
[📄 PL 10-Q p.41](https://agentii.ai/v/PL/sec76/41); annual source:
[📄 PL 10-K p.95](https://agentii.ai/v/PL/sec60/95). The annual rows close a **second** way too:
R&D 106,749 + S&M 72,676 + G&A 88,133 = **267,558** = the filed Total operating expenses line for
FY2026, and likewise for FY2025 and FY2024.

**Grade: `DEMONSTRATED`** throughout — filed cells and arithmetic directly on them.

### 1.1 ⚠️ DA-23 at PL — CONFIRMED at fact level, and the neighbouring fact is genuinely positive

| Period | Platform serves | Filed | Test | Verdict |
|---|---|---|---|---|
| Q1 FY2027 | `OperatingIncomeLoss` **+34,888,000** | **(34,888)** k | equal magnitude, **opposite sign** | **HIT** |
| Q1 FY2027 | `GrossProfit` **50,401,000** | 50,401 k | equal magnitude, **same sign** | clean |

The second row matters: **the gross-profit bound is non-binding at PL because the filed gross
profit is genuinely positive.** The identity in §1 is therefore the only admissible detector, and
it is the one used. No sign in this artifact comes from a served fact.

### 1.2 ⚠️ DA-27 and DA-26 at PL — CONFIRMED, with the mechanism

| Served platform value | Equals, exactly | True period (issuer's label) | Served label | Defect |
|---|---|---|---|---|
| `gross_margin` **0.5353** | 50,401 / 94,150 | **Q1 FY2027** (3M to 2026-04-30) | `fiscal_year 2026, Q1` | **DA-27**, one year low |
| `gross_margin` **0.5524** | 36,603 / 66,265 | **Q1 FY2026** (3M to 2025-04-30) | `fiscal_year 2025, Q1` | **DA-27**, one year low |
| `gross_margin` **0.5605** | 172,485 / 307,727 | **FY2026 ANNUAL** (12M to 2026-01-31) | `fiscal_year 2025, Q4` | **DA-26** *and* DA-27 |

**Three matched pairs give the rule: the platform's `fiscal_year` is the calendar year in which
PL's fiscal year BEGINS; PL labels the fiscal year by the calendar year in which it ENDS.** Every
platform PL fiscal-year label is therefore exactly one lower than the issuer's own. Grade:
`DERIVED` — an observed pattern from three exact matched pairs, not from any documentation.

**DA-26's proof is an absence.** The `fiscal_year 2025, Q4` row carries the **annual** gross margin,
and `search_xbrl_facts(ticker=PL, concept=GrossProfit, fiscal_period=Q4)` returns **zero rows**:
there is no Q4-only gross-profit fact from which 0.5605 could have been computed. An annual figure
served in a quarterly slot, with the underlying quarter absent from the store.

### 1.3 ⚠️ Two further cells in the same platform block that reconcile to nothing

Reported because they are **platform-layer** values with no page, and because the thesis's cohort
tables drew on this block. **No figure in this artifact is sourced from them.**

| Served value | What it should be | What it appears to be |
|---|---|---|
| `fiscal_year 2025, Q4` → `operating_margin` **0.3774** | FY2026: **0.3089** (95,073/307,727) | **116,122 / 307,727 = 0.37736** — the **FY2025** operating loss over **FY2026** revenue. **Numerator and denominator from different fiscal years.** No same-period pairing among the five periods in §1 reproduces it. |
| `fiscal_year 2026, Q1` → `operating_margin` **0.3706** | (37.06)% — **negative** | **34,888 / 94,150 = 0.37056** — the correct magnitude, **sign-stripped**: DA-23 propagated into the ratio layer |
| `fiscal_year 2026, Q1` → `net_margin` **1.4750** | (147.50)% — **negative** | **138,872 / 94,150 = 1.47499** — same defect |
| `roic` ≡ `roa` in **all ten** served rows (0.1110/0.1110, 0.2155/0.2155, …) | independent measures | **flagged, unexplained** — PL carries interest expense ($3,436k in FY2026, [📄 PL 10-K p.95](https://agentii.ai/v/PL/sec60/95)), so equality is not structurally expected |

**The second and third rows are the important ones: the platform's PL margin block reports
negative margins as positive numbers.** Anyone building a cohort table from this block without the
component identity will read PL as a **+37% operating-margin** business. That is the DA-23 failure
mode one layer up from the facts, and it is unfixable at the artifact level — it can only be
refused.

---

## 2. ⚠️ DA-30 at PL: cost of revenue is disclosed on TWO bases in one filing

PL's segment note is, unexpectedly, the most detailed cost disclosure in the universe on this leg —
**one** reportable segment, and a full table of "significant and other segment expenses". It is also
on a **different basis** from the consolidated statement:

| Line (3M to 2026-04-30, thousands of USD) | Segment-expense basis | Footnote says |
|---|---|---|
| Cost of revenue (1) | **33,074** | *"Exclusive of the following items shown separately"* |
| Research and development (1) | 25,934 | idem |
| Sales and marketing (1) | 19,533 | idem |
| General and administrative (1) | 16,642 | idem |
| **Shown separately:** D&A 11,189 · SBC 16,461 · restructuring — · earnout payroll taxes (6) · certain litigation 6,211 | | |
| **Bottom line** | **Consolidated net loss (138,872)** | matches the income statement |

Source: [📄 PL 10-Q p.29](https://agentii.ai/v/PL/sec76/29), footnote (1) verbatim.

**The reconciliation closes, at the total level, exactly:**

```
Consolidated functional costs (GAAP)   Cost of revenue 43,749 + Total opex 85,289  = 129,038
Segment-expense basis                  33,074 + 25,934 + 19,533 + 16,642           =  95,183
Difference                                                                          =  33,855
Separately-shown items                 11,189 + 16,461 + 0 + (6) + 6,211            =  33,855  ✅
```

**Differences cancel to zero.** But note what DA-29 requires: **this closure is a check only
because both terms are filed.** The per-line allocation (how much of the 33,855 sits in cost of
revenue versus R&D) is **not disclosed** and is **not** derived here — see §7.

**⚠️ The trap, and it is a large one.** A reader who takes the segment table's `Cost of revenue
33,074` at face value computes a gross margin of **(94,150 − 33,074) / 94,150 = 64.9%**, against a
filed **53.5%** — an **11.4-point overstatement**, on the single most-quoted number in this thesis's
PL entity row. **This artifact uses the consolidated GAAP basis for every ratio, and states the
basis at each use.** Any downstream artifact quoting a PL gross margin on the segment-expense basis
is quoting a **different concept**, and 64.9% must not enter the corpus as PL's gross margin.

---

## 3. The 53.5% headline, on every basis it is reported

The thesis's entity row for PL reads *"the universe's best gross margin (53.5%)"*. That number is
correct, and it is correct on **one** basis only, for **one** quarter:

| Basis | Q1 FY2027 | Q1 FY2026 | FY2026 annual | FY2025 annual |
|---|---|---|---|---|
| **GAAP gross margin** | **53.5%** *(filing labels it "54%")* | **55.2%** *(filing: "55%")* | **56.0%** | **57.2%** |
| **Non-GAAP gross margin** | **56.3%** *(filing: "56%")* | **58.6%** *(filing: "59%")* | — | — |
| Non-GAAP gross profit | 52,968 | 38,850 | — | — |
| GAAP gross profit | 50,401 | 36,603 | 172,485 | 139,725 |

Sources: [📄 PL 10-Q p.41](https://agentii.ai/v/PL/sec76/41),
[📄 PL 10-K p.95](https://agentii.ai/v/PL/sec60/95). The non-GAAP bridge is filed and small:
GAAP 50,401 + SBC 1,804 + amortization of acquired intangibles 820 − earnout payroll taxes (57) =
**52,968** ✅.

**Three things follow, and the second is a correction to how the thesis quotes this name.**

1. **53.5% is a single-quarter GAAP ratio, not an annual, and not the best of the bases.** On the
   issuer's own non-GAAP basis the same quarter is **56.3%**; on an annual basis FY2025 was
   **57.2%**.
2. **The GAAP gross margin FELL year over year** — 55.2% → **53.5%**, down **1.7 points** — while
   non-GAAP fell 58.6% → 56.3%. The headline "universe's best gross margin" is a *falling* number,
   and the reason is stated by the issuer: mix shift toward satellite platforms and the Mynaric
   acquisition. Grade: `DEMONSTRATED` for the ratios, `CLAIMED` for the cause.
3. **Best-in-universe is a coin-flip on basis.** PL's non-GAAP 56.3% versus the FY2026 annual GAAP
   **56.0%** is a **0.3-point** difference; a cohort table mixing bases can flip the ranking
   without any underlying change. **Every PL margin in this artifact carries its basis.**

---

## 4. What PL sources, and where the cost concentration actually is

### 4.1 Launch is purchased, from three universe members

PL does not own launch. It contracts for it, and the qualified-provider list is filed verbatim:

> *"There are also a limited number of suppliers able to launch our satellites, including
> **ArianeSpace SA, Blue Origin, LLC, Firefly Aerospace Inc., ISAR Aerospace Technologies Inc.,
> Mitsubishi Heavy Industries, Ltd., NewSpace India Limited (Indian Space Research Organization),
> Rocket Lab USA Inc., Space Exploration Technologies Corp. (SpaceX), and Stoke Space
> Technologies, Inc.** Increased tariffs on our suppliers' products are expected to increase the
> cost of manufacturing and deploying our satellites."*
> — [📄 PL 10-Q p.59](https://agentii.ai/v/PL/sec76/59)

**Three of the nine are universe members: RKLB, FLY (Firefly), SPCX (SpaceX).** This is the
universe's only filed, explicit **intra-universe supply relationship** on the launch side: a PL
launch purchase is Launch Services revenue at RKLB or FLY, or Space revenue at SPCX. PL is also the
demand-side confirmation of the same scarcity the launchers assert — *"Service providers who provide
these services are **limited**"* ([📄 PL 10-Q p.11](https://agentii.ai/v/PL/sec76/11)).

**⚠️ The list is not stable between documents.** The FY2026 10-K version of the same risk factor
runs the list to SpaceX **without Stoke Space Technologies, Inc.**
([📄 PL 10-K p.29](https://agentii.ai/v/PL/sec60/29)). A supply-chain count taken from one filing
and quoted against another will disagree by one provider; **state which filing.**

### 4.2 ⚠️ The cost concentration is hosting, not launch — and the ratio is 12.5×

| Commitment (non-cancelable, thousands of USD unless noted) | Amount | Ratio |
|---|---|---|
| **Launch services** — all future years through fiscal 2028 | **$4.7 million** | 1.0× |
| **Google hosting** — minimum purchase commitments | **25,118.0 + 33,427.0 = $58,545.0k** | **12.5×** |

Source: [📄 PL 10-Q p.20](https://agentii.ai/v/PL/sec76/20). The contrast is the whole supply-chain
story for this name: **PL's binding purchased-input commitment is cloud hosting, not launch, by a
factor of roughly twelve and a half.** It is structural, not a one-quarter artefact — *"We
**outsource substantially all** of the infrastructure relating to our cloud-accessible products to
third-party hosting services"* ([📄 PL 10-Q p.60](https://agentii.ai/v/PL/sec76/60)) — and the
concentration is on **single-source components** as well: *"for a **small number of components, we
rely on a single supplier**"*, alongside Uyghur Forced Labor Prevention Act sourcing constraints
(same page).

**Grade and caveat: `DEMONSTRATED` for the commitment figures as filed; the 12.5× is arithmetic on
filed cells, but it compares two *commitment* tables, not two *spend* totals.** Non-cancelable
commitments are a floor on one input and not a measure of all launch spend; PL may buy missions
outside this table. The direction of the finding is robust (a $4.7M multi-year commitment cannot
harbour a large hidden launch line), the magnitude is not a spend ratio. **`DEMONSTRATED` for the
figures, `DERIVED` for the ratio's interpretation.**

### 4.3 Where the money actually went — the issuer's own driver list

| Pool | FY2026 vs FY2025 (12M to 2026-01-31) | Q1 FY2027 drivers |
|---|---|---|
| **Cost of revenue** | **+$30.6M, +29%** → $135.2M | +$5.8M solution partners and subcontractors · +$2.6M spacecraft hardware · +$2.0M ground station · +$2.0M employee-related · +$1.2M hosting |
| ↳ composition | **+$14.5M** solution partners and subcontractors · **+$11.8M** employee-related (labor allocated to satellite services) — **$26.3M of the $30.6M, or 86%** | |
| ↳ depreciation inside cost of revenue | net **−$3.5M**, incl. **−$10.1M** from fully depreciated high-resolution satellites | |
| **R&D** | +$5.7M, +6% → $106.7M | incl. **−$2.6M launch provider costs**, for a satellite classified as experimental |

Sources: [📄 PL 10-K p.79](https://agentii.ai/v/PL/sec60/79),
[📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38). Two things to carry:

1. **86% of the annual cost-of-revenue increase is people and subcontractors**, not hardware and not
   launch. And cost of revenue itself contains a **fixed-cost element** — satellite and ground
   station depreciation ([📄 PL 10-Q p.36](https://agentii.ai/v/PL/sec76/36)) — which the FY2026
   driver list shows moving with the *fleet's* depreciation schedule (−$10.1M from fully
   depreciated satellites), not with volume. **Fixed cost sits on both sides of PL's gross-profit
   line**, which is a refinement to the "gross margin is clean" reading.
2. **The only quantified launch-cost line in PL's entire accounts is a $2.6 million decrease**, and
   it sits inside *R&D*, for one experimental satellite. That is the scale of launch in this
   company's disclosed cost structure: **single-digit millions, disclosed as a decrement, one
   line.** The demand side does not price off the launch curve because launch is not, for this
   buyer, a material input.

---

## 5. Fixed cost, not launch cost — the P6 test, stated as arithmetic

Q1 FY2027, all thousands of USD, all on filed cells
([📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38)):

```
Revenue                  94,150   100.0%
Cost of revenue         (43,749)  (46.5%)
Gross profit             50,401    53.5%   ← the universe's best gross margin
Total opex              (85,289)  (90.6%)  ← R&D + S&M + G&A
Loss from operations    (34,888)  (37.1%)
```

**The loss is entirely an opex phenomenon: gross profit (50,401) minus opex (85,289) = (34,888),
and that difference IS the filed operating loss.** Two breakeven routes, both `DEMONSTRATED`
arithmetic on filed cells:

| Route to breakeven | Required move | Reduction |
|---|---|---|
| **Cut operating expenses** | 85,289 → **50,401** | **−40.9%** |
| **Cut cost of revenue** | 43,749 → **8,861** | **−79.7%** |

**The opex route is the shorter one by roughly 2×, and the launch-cost route is not on the list at
all.** The bound that makes this a *PIL-6* result rather than a *PL* result:

> **The entire non-cancelable launch commitment through fiscal 2028 — $4.7M — spent at once,
> closes 13.5% of one quarter's operating loss ($34,888k).** And a **10%** reduction in PL's
> *total* cost of revenue (all materials, all launch procurement, all hosting pass-through, all
> satellite depreciation) closes **12.5%** of the loss and moves the operating margin from
> **(37.1)%** to **(32.4)%** — six percentage points of margin for a tenth of the entire cost of
> revenue.

**That is PIL-6's demand-side leg, in one issuer:** the released value would arrive at PL as a
sub-single-digit-millions item inside a cost of revenue that is itself out-earned by opex, while
the company's actual constraint — **90.6% of revenue in operating expenses** — is untouched by the
launch curve. **PL does not price off the curve because the curve is not its binding input.**
Grade: `DEMONSTRATED` for the arithmetic; the *inference* that a launch-price collapse leaves PL's
operating line roughly where it is, is `MODELED` and is stated as a bound, not a forecast.

**And the market has already given its verdict on the same arithmetic**, on the issuer's own
non-GAAP basis: **Adjusted EBITDA $(1,033)k** in the quarter against **$1,199k** a year earlier —
the company is at breakeven on the measure that *excludes* depreciation, SBC and litigation, while
a **$(34,888)k** GAAP operating loss sits on top of it ([📄 PL 10-Q p.41](https://agentii.ai/v/PL/sec76/41)).
The 33,855 gap between the two is precisely the "shown separately" column of §2 — the same items,
appearing a second time. Two presentations, one company.

---

## 6. PIL-2's falsifier is `UNEXERCISED` at PL — not satisfied, not violated

> `metric=count_of_universe_issuers_where_launch_segment_operating_margin_exceeds_non_launch_segment_operating_margin threshold=0 source=issuer_segment_disclosure op=>`

**PL reports exactly one segment.** The note is titled *"Financial information for the Company's
reportable segment was as follows"* — singular — and presents a single column
([📄 PL 10-Q p.29](https://agentii.ai/v/PL/sec76/29)). There is **no launch segment and no
non-launch segment**, therefore no segment operating margin on either side of the comparison.

**The falsifier cannot run. Recorded `UNEXERCISED`; PL counts toward neither PIL-2's numerator nor
its denominator, and must not be scored as "no violation".** A test that could not run is not a
passed test.

**Disposition: `UNRESOLVABLE-FROM-PUBLIC-SOURCES`.** The disclosure does not exist publicly. The
specific disclosure that would resolve it: **a second reportable segment** — most plausibly a split
of satellite-services from data/analytics, or of the satellite-systems business from the rest —
with an allocation of operating expenses to it. PL's segment note supplies the *expense detail*
(§2, unusually) but **not a second segment to allocate it to**. Remedy: *monitor*, not *search
harder*.

**What PIL-2 can use from this name instead, with the basis named:** §5's two breakeven routes and
the 90.6% opex ratio are a **direct test of PIL-2's mechanism** — value did not migrate to the
launcher, and on this name it did not migrate to the payload customer either, because the payload
customer's problem is its own fixed-cost base. **This is a substituted line of argument, not the
registered metric, and this artifact does not substitute it into the census.**

---

## 7. What could NOT be verified

| Item | Disposition | Class |
|---|---|---|
| **A launch segment operating margin, or any second segment** | **Does not exist** — one reportable segment (p.29) → PIL-2's falsifier `UNEXERCISED` (§6) | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| **PL's total launch spend in any period** | Only two fragments exist: a **$4.7M** non-cancelable commitment (p.20) and a **−$2.6M** R&D decrement (p.79). **Neither is a spend total**, and the cost of revenue note lumps *"third-party fees for launch procurement"* with materials and ground station | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| **How the 33,855 "shown separately" pool allocates across cost of revenue, R&D, S&M and G&A** | The **total** closes exactly (§2); the **per-line allocation is not disclosed**. Not derived — a per-line split obtained by subtraction would be a back-solve (DA-29) | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |
| **PL's fiscal-year labelling on the platform** | Off by one, mechanism identified (§1.2). The served values are reproducible; the **labels** are not usable as-is | `UNRESOLVABLE-FROM-PLATFORM` |
| **`fiscal_year 2025, Q4` `operating_margin 0.3774`** | Reconciles to a **cross-year** ratio (116,122/307,727) and to **no** same-period pairing among five periods. Mechanism unexplained | `UNRESOLVABLE-FROM-PLATFORM` |
| **`roic` ≡ `roa` in all ten served ratio rows** | Flagged, unexplained, not used for any figure (§1.3) | `UNRESOLVABLE-FROM-PLATFORM` |
| **`gross_margin` cells older than FY2025 in the served ratio block** (e.g. `2023 Q4` = **0.8608**) | **Implausible on its face** — PL's gross margin has never been 86%, and the FY2024 annual ratio is 51.2%. Not investigated further; the block is **not used as a source** for any figure here | `UNRESOLVABLE-FROM-PLATFORM` |
| **Whether the two-basis cost of revenue persists in the FY2026 10-K segment note** | The 10-K segment note was **not read** in this leg. The two-basis issue is established from the 10-Q (p.29); the annual segment table is `UNEXERCISED` | `UNEXERCISED` |
| **Customer concentration** (one customer 33% of AR; two at 15% and 11% of revenue, p.11) | Read, and **named but not decomposed** — counterparty identity is not disclosed | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |

---

## 8. Corrections to 001 (frozen-001 policy: 001 is not rewritten)

| # | 001 / prior usage says | Primary source shows | Status |
|---|---|---|---|
| 1 | PL **"53.5%"** gross margin, quoted alongside a **"−37%"** operating line | **Both correct**, and now fully based: 53.5% is the **GAAP single-quarter** ratio 50,401/94,150 for the quarter ended 2026-04-30; the same quarter on the issuer's **non-GAAP** basis is **56.3%**, and the **annual** basis is **56.0%** (FY2026) and **57.2%** (FY2025). **GAAP gross margin fell 1.7 points y/y** (§3) | **Confirmed on one basis; competing bases added** |
| 2 | 001 records the platform's `Q4` row and the **$307.727M** annual revenue under a fiscal-year label one lower than the issuer's | **The amount is right and the label is off by one.** $307,727k is the revenue of the year **ended 2026-01-31**, which **PL labels FY2026** and the platform labels FY2025. The mechanism is now identified: the platform's `fiscal_year` = the year the fiscal year **begins** (§1.2) | **DA-27 + DA-26 confirmed with mechanism** |
| 3 | — (new here) | **The platform serves PL's operating and net margins as POSITIVE numbers** — `operating_margin 0.3706` (= \|−37.06%\|) and `net_margin 1.4750` (= \|−147.50%\|). Anyone reading the ratio block sees a +37% operating-margin business (§1.3) | **Added — DA-23 at the ratio layer** |
| 4 | — (new here) | **PL discloses cost of revenue on two bases**, differing by 32.3% of the line; the segment-expense basis yields a **64.9%** gross margin against the filed 53.5% (§2) | **Added — DA-30** |
| 5 | — (new here) | **PL names three universe members (RKLB, FLY, SPCX) as launch suppliers**, and its binding purchased-input commitment is **cloud hosting, 12.5× launch** (§4) | **Added** |

## 9. Carry-forwards

1. **⚠️ Never quote PL's gross margin without its basis.** 53.5% (Q1 FY2027 GAAP) · 56.3% (same
   quarter non-GAAP) · 56.0% (FY2026 annual) · 57.2% (FY2025 annual) · **and 64.9% if a reader takes
   the segment-expense cost-of-revenue line, which is not cost of revenue** (§2). The universe's
   "best gross margin" is a **falling** number on both GAAP and non-GAAP bases.
2. **⚠️ Every platform PL fiscal-year label is one lower than the issuer's.** Platform `fiscal_year`
   = the calendar year PL's fiscal year **begins**. Convert before any cross-name comparison (§1.2).
3. **⚠️ The platform's PL ratio block sign-strips operating and net margins** (`0.3706` for −37.06%,
   `1.4750` for −147.50%), and one cell (`0.3774`) mixes two fiscal years. **Do not build PL rows
   from the ratio block** — build them from `gross_profit − opex` on read pages (§1.3).
4. **⚠️ PL is `UNEXERCISED` on PIL-2's falsifier, and must not be counted.** One reportable
   segment; the registered metric has no launch/non-launch pair here (§6).
5. **⚠️ PL is PIL-6's cleanest demand-side test, and the number to carry is the breakeven split:**
   −40.9% opex or −79.7% cost of revenue, with the **entire** multi-year launch commitment closing
   **13.5%** of a single quarter's operating loss (§5). The demand side does not price off the cost
   curve because **the curve is not its binding input**.
6. **⚠️ The only intra-universe supply relationship filed anywhere in this corpus on the launch
   side: PL buys launch from RKLB, FLY and SPCX** (p.59), and the provider list **differs between
   the 10-K and the 10-Q** (Stoke absent from the 10-K). State the filing (§4.1).
7. **Cost concentration at PL is hosting, not launch**: **$58,545.0k** Google hosting commitments
   against **$4.7M** of launch commitments — **12.5×** (§4.2).
8. **⚠️ Citation-resolution note, observed on these documents:** the platform's page number and the
   document's own printed footer **do not always agree** — `sec60 p.79` prints "75" and `sec60 p.95`
   prints "91" (offset 4), while `sec76` prints match. **Cite the platform page** (it is what the
   URL carries); do not "correct" a citation to the printed footer.
9. **Fixed cost sits on both sides of the gross-profit line at PL** — satellite and ground station
   depreciation live inside cost of revenue (p.36, p.79). "High gross margin" does not mean
   "variable cost" at this issuer (§4.3).

---

## Sources

> Every figure asserted above resolves to the page cited. The links also appear in-line at each
> section, per spec §1d, which requires them in the body and not only in frontmatter. The platform
> `sec76`/`sec60` page numbers are the platform's own; see carry-forward 8.

| Figure | Source |
|---|---|
| Component identity, quarter — 94,150 / 43,749 / 50,401 / 85,289 / (34,888); prior-year 66,265 / 29,662 / 36,603 / 59,374 / (22,771); cost-of-revenue drivers | [📄 PL 10-Q p.38](https://agentii.ai/v/PL/sec76/38) |
| Component identity, annual, three years — 307,727 / 244,352 / 220,696; GP 172,485 / 139,725 / 112,950; opex 267,558 / 255,847 / 282,698; loss (95,073) / (116,122) / (169,748) | [📄 PL 10-K p.95](https://agentii.ai/v/PL/sec60/95) |
| One reportable segment, the two-basis cost of revenue, the segment reconciliation, capex $18.0M vs $9.3M, PP&E $159,145k | [📄 PL 10-Q p.29](https://agentii.ai/v/PL/sec76/29) |
| Gross margin on both bases — GAAP 50,401 / non-GAAP 52,968; "54%" vs "56%"; Adjusted EBITDA $(1,033) vs $1,199 | [📄 PL 10-Q p.41](https://agentii.ai/v/PL/sec76/41) |
| What PL sources for launch — nine named providers including RKLB, Firefly and SpaceX; tariffs | [📄 PL 10-Q p.59](https://agentii.ai/v/PL/sec76/59) |
| Cost concentration — launch commitments $4.7M vs Google hosting $25,118.0k + $33,427.0k | [📄 PL 10-Q p.20](https://agentii.ai/v/PL/sec76/20) |
| Component sourcing and the cloud boundary — single supplier for a small number of components; UFLPA; cloud infrastructure outsourced | [📄 PL 10-Q p.60](https://agentii.ai/v/PL/sec76/60) |
| Cost-of-revenue definition — satellite inventory materials, third-party launch procurement fees, ground station infrastructure, satellite and ground station depreciation | [📄 PL 10-Q p.36](https://agentii.ai/v/PL/sec76/36) |
| Demand-side and launch-availability concentration — limited launch service providers; customers at 33% of AR and 15% / 11% of revenue | [📄 PL 10-Q p.11](https://agentii.ai/v/PL/sec76/11) |
| Annual cost drivers and the only quantified launch-cost line — +$14.5M subcontractors, +$11.8M employee-related; R&D incl. −$2.6M launch provider costs | [📄 PL 10-K p.79](https://agentii.ai/v/PL/sec60/79) |
| The 10-K version of the launch-availability risk factor, truncated without Stoke Space Technologies | [📄 PL 10-K p.29](https://agentii.ai/v/PL/sec60/29) |
