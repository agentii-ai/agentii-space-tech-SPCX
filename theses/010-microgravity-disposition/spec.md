# Research Thesis: 010 — Tier 5: Microgravity Demand Side

**Claim**: **This is a disposition study, not a demand study.** The subject — microgravity
commercial manufacturing — **does not appear in the filings of any name in its own
universe**, and that absence is the finding, established by a keyword audit with a positive
control. Both halves of the economic test (value-per-kg-returned, cost-per-kg-returned) are
**non-existent in public sources**, a stronger condition than public-but-unreachable. The
correct output is a **watch-list with named triggers**, and the hurdle is each incumbent's
own margin at a **named basis** — not a universal 87.3%.

**Constitution Ref**: constitution.md **v1.6.0** (`constitution_pin: 1.6.0`) — **re-pinned
at re-scope, 2026-09-19.** Was `1.4.0`. The bump matters here for one reason: v1.6.0
corrected the **`PARTIAL` coverage class**, which this spec's §2 both mis-states and
mis-applies (see §2).
**Created**: 2026-09-18 · **Re-scoped**: 2026-09-19 (constitution 1.4.0 → 1.6.0)
**Status**: **PLANNED — spec COMPLETE and self-consistent. Not frozen. No tasks may be
generated.**
**Wave**: 2 (activates when a slot opens under `max_theses_active: 6`)
**板块**: Tier 5 · **Binding constraint**: `DEMAND` — retained, and now better justified:
the thesis's whole content is *whether a demand side exists at all*, and the measured answer
is that it does not appear in any filing.
**Depends on**: `001-technology-baseline` (artifacts below — Pillar 4 is the inheritance),
`002-evidence-validation` (**COMPLETE**), `003-launch-cost-curve-value-migration` (**owns the
cost half of the economic test**)
**Market data**: **declared, `per_row`** — see §5. The disposition turns partly on whether
optionality is *priced*, and the stub declared no stage.
**Produces**: a **named-trigger watch-list**. **No position, and no sizing** — the constitution
permits a pillar recorded `UNRESOLVABLE-FROM-PUBLIC-SOURCES` rather than dropped or failed.

---

## 0. Inherited baseline — what this thesis does NOT re-derive

**Restated at re-scope.** The stub framed this as a **demand study** — *"is microgravity
manufacturing a real demand side"* — with a caveat that the honest output *"may be a
watch-list with named triggers rather than a position."* **The caveat was the thesis.** The
re-scope promotes it: 010 is a **disposition study**, and the reason is §0.1.

**Path shorthand — declared, not implied.** `001/` expands to `../001-technology-baseline/`,
`002/` to `../002-evidence-validation/`, `003/` to `../003-launch-cost-curve-value-migration/`.
Every path below resolves to a file on disk.

### 0.1 The finding: the subject is absent from the filings

**This is the thesis's primary result and it was not in the stub.** The stub asserted *"UTHR's
Varda partnership (announced May 2026, first samples 'as early as 2027')"* as the headline
fact and treated the rest as unquantified. **It is not unquantified. It is absent.**

**How the absence was established.** Not by inference, and not by a search that returned
nothing — those are weak. By a **keyword audit against a positive control**, run on the
filings that post-date the announcement:

| Subject | Document | Accession | Filed | Result |
|---|---|---|---|---|
| **UTHR** | **Q2 2026 Form 10-Q** — the reporting period **after** the May 2026 Varda announcement | `0001082554-26-000027` (citation_id `sec219`; report_date 2026-06-30) | **2026-08-05** — i.e. *after* the announcement | `"Varda"` → **0 pages** · `"microgravity"` → **0 pages** · `"space"` → **0 pages** · **positive control `"revenue"` → 23 pages** |
| **UTHR** | Q2 2026 earnings call | — | 2026-08-05 | No mention of Varda, microgravity or space |
| **UTHR** | FY2025 Form 10-K | — | — | No mention of Varda, microgravity or space |
| **MRK** | FY2025 Form 10-K | — | — | No mention of Varda, microgravity or space |
| **LLY** | FY2025 Form 10-K | `0000059478-26-000013` (citation_id `sec175`) | 2026-02-12 | `"microgravity"` → **0 pages** · `"space"` → **0 pages** |
| **001, independently** | XBRL extract | — | — | **"no mention of Varda in the XBRL extract at all"** (`001/artifacts/UTHR/2026-09-18_1239_unit-economics_methodology.md` §1) |

**Why the positive control is load-bearing.** A keyword search returning zero has two
explanations: the term is absent, or the tool failed to index the document. **`"revenue"`
returning 23 pages on the same document, through the same tool, discriminates between them.**
Without the control, the zero is not evidence; with it, the zero is a **measurement**.

**Why the filing window is load-bearing.** The announcement was **May 2026**; the 10-Q was
**filed 2026-08-05** covering the period to **2026-06-30**. A company that had signed a
partnership in May and considered it material had a June-quarter 10-Q, an earnings call, and
a subsequent-events note in which to say so. **It said nothing, in any of them.** The absence
survives the strongest available test — a document that *could* have contained it, published
*after* the event, from the one issuer with a disclosed reason to mention it.

**This is why the thesis is a disposition study.** A demand study measures demand. 010 cannot
measure demand, because the demand side does not describe the demand in any document a
public filer is required to produce.

### 0.2 The economic test is unexecutable — and it is a *stronger* condition than unreachable

- **The correct test is value-per-kg-returned versus fully-loaded cost-per-kg-returned** —
  launch, on-orbit processing, reentry capsule and recovery combined. **Not TAM.**
- **Value-per-kg is not disclosed** — Varda has no revenue line anywhere.
- **Cost-per-kg is not disclosed** — Varda is private; the **~$329M raised** and **~50
  kg/mission** figures are **`CLAIMED` press figures only**.
- 001's verdict: *"the clearest `UNRESOLVABLE-FROM-PUBLIC-SOURCES` case in the thesis"* — a
  **stronger** condition than PIL-6 (public but unreachable) or P5 (commercially licensed),
  because **these figures do not exist publicly at all.**

### 0.3 The margin ladder — component-verified, and it is per-issuer

**The stub carried a single bar — *"an 87.3% gross margin… the bar any microgravity process
must clear."* That is wrong twice over**, and this is the corrected form. **It takes the
cohort's highest gross margin and universalises it, and it compares a *gross* margin against
a *process cost* without naming the basis.**

Every figure below is **sign- and component-verified** against the filed statement, per the
DA-23 discipline (§0.5). The component identity closes exactly on UTHR and AMGN; where it
cannot run, **no operating margin is quoted at all**.

| Issuer | Period | Revenue | **Gross margin** | **Operating margin** | Component identity |
|---|---|---|---|---|---|
| **UTHR** | Q2 2026 | $783.3M (−1.9% YoY) | **87.3%** | **42.2%** (vs 45.6%, **−3.4 pts**) | ✅ **closes exactly**: GP $683.8M = $783.3M − COGS $99.5M; OI $330.8M = $683.8M − (R&D $146.3M + SG&A $206.7M) |
| **AMGN** | Q2 2026 | $10,054M | **72.0%** | **35.0%** | ✅ **closes exactly**: GP $7,243M = $10,054M − COGS $2,811M; OI $3,514M = $7,243M − (R&D $1,868M + SG&A $1,745M + Other $116M) |
| **BMY** | FY | $12,973M | **71.3%** | **not quotable** | ⚠️ **`OperatingIncomeLoss` is NULL for BMY** — the component-identity detector cannot run |
| **MRK** | FY | $16,607M | **not established** | **not quotable** | ⚠️ gross margin **not disclosed** in the extract; **`OperatingIncomeLoss` is NULL for MRK** |
| **LLY** | — | — | — | — | **No 001 artifact exists.** LLY is researchable (§2) and **not yet researched** |

**The corrected bar.** The hurdle is **the incumbent's own margin, at a named basis, per
issuer** — and it spans **71.3–87.3% gross / 35.0–42.2% operating** across the cohort. A
microgravity process is a **cost of goods** item, so the *gross* row is the relevant
comparator — but the correct statement is *"UTHR's 87.3% gross margin is UTHR's bar,"* not
*"87.3% is the bar."* **Against AMGN the bar is 72.0%; against BMY it is 71.3%; against MRK
it is unestablished.**

**And the honest reading runs against the thesis.** UTHR's operating margin fell **3.4 pts**
to 42.2% — the cohort's highest-margin issuer is **already compressing**. A process that must
clear an 87.3% gross bar is being asked to clear a bar its own incumbent is currently falling
through.

### 0.4 The "immaterial-to-the-counterparty" pattern

UTHR is large enough that its Varda partnership (announced **May 2026**, first samples *"as
early as 2027"*) is **financially irrelevant** to it — so it is never broken out, **which
suppresses the very evidence the falsifier needs to fire.** This is the same pattern 009's
P2 records, in a different tier, with the same mechanism: **the counterparty's size is what
makes the disclosure unnecessary.** It is the second instance; the pattern is now
cross-thesis methodology, not a local observation.

### 0.5 A standing discipline carried into every figure above (DA-23)

The platform's `search_xbrl_facts` **strips the sign** from `OperatingIncomeLoss`;
`get_statement` on the same accession preserves it. 001 declared GSAT *"clean on DA-23"* —
*"clean-positive count: 15 of 15"* — and built a section on the stripped figure. **GSAT's
filed operating margin is −7.37%, not +7.4%.** GSAT is **not** in this thesis's universe;
**the instrument is.** Every margin in §0.3 passed the component identity before it was
quoted, and **every pillar falsifier below is a count or a disclosed figure, never a
sign-stripped extract value.**

### 0.6 P6 — private-company coverage

**Varda enters as a value-chain node only, with UTHR as its named listed proxy.** No private
company receives its own thesis. **Varda is *not* a universe member and never was** — the
stub's §0 treated it as the subject while its §2 listed only listed pharma. **The subject of
this thesis is the *disposition* of the listed cohort toward microgravity.** Varda is the
node that gives the disposition a name.

---

## 1. Research Question

**Given that the subject does not appear in the filings, that both halves of the economic
test are non-existent in public sources, and that the hurdle is each incumbent's own margin
at a named basis — the question is not "is there demand" but: what is the correct
disposition of the listed cohort toward microgravity, and precisely which events would change
it?**

**The answer, stated as the thesis rather than as a caveat:** the disposition is a
**watch-list with named triggers** (§1b Pillar 4). The stub said this *"may be"* the output.
**It is the output.** A thesis whose subject is absent from every document it can read has
one honest result, and the constitution permits it: a pillar may be recorded
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` rather than dropped or failed.

**What this thesis does not do.** It does not estimate a TAM. It does not value Varda. It
does not forecast demand from a `CLAIMED` press figure. **A falsifier that cannot fire is not
evidence**, and §0.2 records that neither half of the test can be made to fire.

### 1a. Why the disposition is not "uninvestable"

Two of the stub's three candidate postures are live, and the third is not:

- ❌ **(b) treat it as uninvestable until a listed pure-play or a disclosure exists** — this
  is **not a disposition**, it is the *same* disposition as the watch-list with the triggers
  left unnamed. Naming them is the work.
- ✅ **(a) hold microgravity as unpriced optionality within UTHR** — testable, and Pillar 5
  tests it. **If it is priced, UTHR is not the vehicle; if it is not priced, the optionality
  is free but unmeasurable, which is a reason to hold at zero weight rather than to size.**
- ✅ **(c) monitor for the specific events that would make it investable** — **this is the
  thesis.** Pillar 4 names them.

---

## 1b. Pillars

### Pillar 1 — The subject is absent from the cohort's filings, and the absence is a *measured* zero (Priority: P1) 🎯 Minimum Defensible View

**Claim.** The count of cohort filings or transcripts containing a microgravity or Varda
reference **in a financial disclosure** is **zero** — established by keyword audit against a
positive control (§0.1), not by inference. The stub's own note that 001 recorded *"no mention
of Varda in the XBRL extract at all"* is the independent second measurement of the same fact.

**Why P1**: it is the MDV because **the absence is the finding**. Everything the thesis can
say follows from it: no demand study is possible, the economic test cannot be built, and the
disposition must therefore be trigger-based.

**Independently falsifiable**: a single mention of Varda, microgravity, or space-based
manufacturing in a financial disclosure — a revenue line, a cost line, an R&D programme
breakout, a risk factor, or a subsequent-events note — at any cohort issuer.

**wrong_if**: `metric=count_of_cohort_pharma_filings_and_transcripts_containing_a_microgravity_or_varda_reference_in_a_financial_disclosure threshold=0 source=10-Q_10-K_and_earnings_call_transcript_keyword_audit_with_positive_control op=>`

**Subscribed**: `UTHR × business-model`, `MRK × business-model`, `BMY × business-model`, `AMGN × business-model`, `LLY × business-model`, `UTHR × recent-quarter`, `UTHR × secular-trends`, `LLY × secular-trends`

---

### Pillar 2 — Both halves of the economic test are non-existent in public sources, which is a stronger condition than unreachable (Priority: P2)

**Claim.** The count of the economic test's two halves available from a public source is
**zero**. Value-per-kg-returned is not disclosed; cost-per-kg-returned is not disclosed. This
is **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`**, which 001 called *"the clearest case in the
thesis"* — and it is categorically different from PIL-6 (public but unreachable) and P5
(commercially licensed), because **there is no source to reach.**

**Why P2**: it forecloses the most tempting failure mode — substituting a `CLAIMED` press
figure (~$329M raised, ~50 kg/mission) for a filed one and calling the test "framed rather
than settled." **Framed on claimed inputs is not framed.**

**Independently falsifiable**: any public source disclosing either half — a value-per-kg
figure, a fully-loaded cost-per-kg-returned figure, or the component inputs (launch $/kg,
capsule cost, recovery cost) for a named microgravity process.

**wrong_if**: `metric=count_of_the_two_economic_test_halves_available_from_a_public_source threshold=0 source=issuer_filing_or_regulatory_document_disclosing_value_per_kg_returned_or_fully_loaded_cost_per_kg_returned op=>`

**Subscribed**: `UTHR × unit-economics`, `MRK × unit-economics`, `AMGN × unit-economics`

*The economic test's **launch** component is consumed from 003 and is **not** subscribed
here — see §3b. 003 owns 003's curve.*

---

### Pillar 3 — The hurdle is the incumbent's own margin at a named basis, per issuer — not a universal 87.3% (Priority: P3)

**Claim.** The count of cohort pharmas whose **operating** margin equals or exceeds **87.3%**
is **zero** — UTHR 42.2%, AMGN 35.0%, BMY and MRK not quotable. **The stub's 87.3% bar is
inapplicable as stated on two independent axes**: it is a **gross** margin compared against a
**process cost**, and it is **UTHR-specific** universalised to the cohort (71.3–87.3% gross;
35.0–42.2% operating — §0.3).

**And the direction is adverse.** The cohort's highest-margin issuer, the one that *is* the
Varda partner, saw its operating margin **fall 3.4 pts** to 42.2%.

**Why P3**: it is where the stub's one quantified claim was wrong, and it determines the
answer to Pillar 1's follow-on — **a process must beat a *specific* incumbent's *specific*
margin, so "the bar" does not exist and cannot be used to size a value uplift.**

**Independently falsifiable**: a cohort pharma reporting an operating margin at or above
87.3%, or a filing disclosing a microgravity process cost directly comparable to a named
issuer's gross margin **on the same basis**.

**wrong_if**: `metric=count_of_cohort_pharmas_with_an_operating_margin_at_or_above_87_3pct threshold=0 source=10-Q_income_statement_component_identity_at_a_named_basis op=>`

**Subscribed**: `UTHR × unit-economics`, `MRK × unit-economics`, `BMY × unit-economics`, `AMGN × unit-economics`, `LLY × unit-economics`, `UTHR × ratio-analysis`, `MRK × ratio-analysis`, `BMY × ratio-analysis`, `AMGN × ratio-analysis`, `LLY × ratio-analysis`, `UTHR × peer-bench`, `MRK × peer-bench`

---

### Pillar 4 — The disposition is a watch-list with named triggers, and zero have fired (Priority: P4)

**Claim.** The count of named triggers fired inside the thesis window is **zero**. **The
triggers, named rather than described** — each is a disclosure a public source would carry:

| # | Trigger | Why it matters | Source that would carry it |
|---|---|---|---|
| **T-1** | **A listed pure-play** — Varda or a competitor files an S-1/8-A | Converts the exposure from a private node into a priced security, and makes Pillar 2 potentially resolvable | SEC EDGAR — S-1, 8-A |
| **T-2** | **UTHR breaks out programme economics** — a microgravity revenue or cost line in a 10-Q/10-K, or a dedicated segment note | Fires Pillar 1's falsifier **and** Pillar 2's; the single highest-value trigger | UTHR 10-Q segment note / subsequent events |
| **T-3** | **A second named listed pharma partner** for Varda (or a competitor) | Refutes the "one company's science project" reading; tests whether the cohort acts as a cohort | 8-K / press release mirrored in a filing |
| **T-4** | **A commercial-scale volume commitment** — a disclosed kg/year figure or a supply agreement with a value | Separates pilot from production, which is the whole question the disposition defers | 8-K Item 1.01 |
| **T-5** | **A disclosed value-per-kg or cost-per-kg-returned figure** from any public source | Fires Pillar 2 directly and makes the economic test executable for the first time | Filing, regulatory document, or peer-reviewed publication with disclosed inputs |
| **T-6** | **A priced per-kg commercial return service** — an ISS-successor or commercial station offering return capacity at a published rate, against the ISS deorbit horizon (~2030) | Supplied the cost half's return component; **a dated event, not a forecast** | Commercial station operator's published price list or filing |

**Why P4**: it is the thesis, restated from caveat to claim (§1).

**Independently falsifiable**: any named trigger firing.

**wrong_if**: `metric=count_of_named_triggers_fired_inside_the_thesis_window threshold=0 source=SEC_filings_8-K_S-1_and_10-Q_and_published_commercial_price_lists op=>`

**Subscribed**: `UTHR × recent-quarter`, `UTHR × risk`, `UTHR × growth-strategy`

---

### Pillar 5 — Microgravity is optionality, not a response to pressure — so adoption will not be forced (Priority: P5)

**Claim.** UTHR's revenue **fell 1.9% YoY** to $783.3M. **A declining top line is not a
pipeline emergency**, and microgravity addresses none of the four names' disclosed
problems. **The count of cohort pharmas combining a named microgravity programme with
positive YoY revenue growth is zero** — so microgravity is what a well-resourced company does
with slack, not what a company does under pressure. **This is why the demand side is silent,
and why it will stay silent until something other than growth forces it.**

**Why P5**: it is the mechanism behind Pillar 1's zero. Without it, Pillar 1 reads as "not
yet"; with it, Pillar 1 reads as **"not until the incentive changes."**

**Independently falsifiable**: UTHR revenue growth at or above zero at any period, **or** a
cohort pharma with a named microgravity programme and growth that is nonetheless flat or
falling (which would indicate a *pipeline-driven* rather than slack-driven programme).

**wrong_if**: `metric=utthr_yoy_revenue_growth_rate threshold=0 source=10-Q_income_statement_total_revenues op=>=`

**Subscribed**: `UTHR × growth-strategy`, `MRK × growth-strategy`, `UTHR × unit-economics`, `UTHR × reverse-dcf`

---

## 2. Universe Definition

**Membership test, applied as written** (constitution v1.6.0 §Universe Definition): Tier 5 is
the **demand side** — *"buys space services; space is not its business."* Tier 5 membership
is by **revenue composition**, and every name below is a pharmaceutical theses whose primary
revenue is medicines.

| Ticker | Company | Sector | Weight | Relevance — and coverage class (**v1.6.0**) |
|---|---|---|---|---|
| UTHR | United Therapeutics | med.medicines_biotech | equal | **Named Varda partner** (announced May 2026) — the listed proxy for the exposure. **READY** — 68 filings; `cohort: tier2_2026q3`, completion **100%** |
| MRK | Merck | med.medicines_biotech | equal | ISS protein-crystallization research history. **READY** — 52 filings |
| BMY | Bristol Myers Squibb | med.medicines_biotech | equal | Microgravity biologics research. **READY** — 74 filings |
| AMGN | Amgen | med.medicines_biotech | equal | Microgravity protein research. **READY** — 71 filings |
| LLY | Eli Lilly | *(PARTIAL — unassigned)* | equal | Microgravity protein/formulation research. **PARTIAL** — **`sector` is null. That is the whole of the class** (v1.6.0). **Researchable at 86% completion; see below** |

*Weights are `equal` and carry no sizing meaning — **010 produces no position and no
weight** (§4). A watch-list entry is not a weight.*

### The `PARTIAL` correction — the stub contradicted itself in-file

**The stub's §2 table labelled LLY `PARTIAL — sector unassigned` while its own prose, one
line below, asserted *"All five sit in `med.medicines_biotech`."* Both cannot be true. The
prose was wrong.**

**What `PARTIAL` means at v1.6.0, and what it does not.** The pre-amendment `PARTIAL` class
required `sec_filings == 0`. **That condition was a bookkeeping artefact and has been
removed** — at v1.6.0, `PARTIAL` means **`sector` is null and nothing more.** The distinction
is not cosmetic: the old class implied *unresearchable*, and **it was never true of LLY.**
Verified coverage for LLY:

| LLY source | Count | Latest |
|---|---|---|
| xbrl_facts | **75,248** | — |
| src_documents | **81** | — |
| earnings_call_transcript | **19** | 2026-08-05 |
| earnings_calendar | 159 | — |
| institutional_holdings | 46 | — |
| insider_trades | 53 | — |
| **`completion_pct`** | **86** | **6 of 7 populated sources** — *only `sector` is missing* |

**LLY is researchable, on six of seven source types, at 86% completion. It is not yet
researched — 001 has no LLY artifact** (001's artifact set covers UTHR, MRK, BMY and AMGN,
and not LLY). **The correct statement is: four names carry `med.medicines_biotech` on the
platform; LLY carries no sector and must be assigned by hand before any sector-aggregate
constraint evaluates.** That assignment is a **precondition, not an assumption** — and it
does not imply missing data.

**The tier's defining screening hazard survives the correction.** **None of the five will
surface on an aerospace screen** — they are all pharmaceuticals by revenue composition.
That is the honest form of the stub's claim, and it is why this thesis exists.

### Explicitly not members

- **Varda** — a **private company** and a value-chain node under P6 (§0.6). It receives no
  `artifacts/{ticker}/` directory and no thesis. **It appears in §0 only as the event that
  gives the UTHR line a name.**
- **009's cohort** (GOOG, MSFT, AMZN, NVDA, VRT) — **not Tier 5.** They *sell* rather than
  buy. 009 is the seller's thesis; 010 is the demand side.

---

## 3. Skill Deployment Matrix

**`tasks_md.py` parses §3a only.** §3b is deliberately a different column shape so it parses
as prose — **the mechanism that makes "consumed" mean consumed** (004's convention).

### 3a. Executed

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|---|---|---|---|
| business-model | business-intelligence | Deep | UTHR, MRK, BMY, AMGN, LLY | none | **Where a microgravity line would appear if one existed** — segment boundaries (DA-21), R&D disaggregation, subsequent-events notes. Gates **P1** |
| unit-economics | business-intelligence | Deep | UTHR, MRK, BMY, AMGN, LLY | none | **The margin ladder at a named basis, per issuer** (§0.3), with the component identity run wherever `OperatingIncomeLoss` exists. Gates **P3** |
| recent-quarter | business-intelligence | Standard | UTHR | none | The quarterly series behind P5's revenue trend and P1's zero, dated against the May 2026 announcement window |
| secular-trends | business-intelligence | Deep | UTHR, LLY | none | **Is microgravity a stated trend at any cohort issuer, and if not, what does it say instead?** The negative-space read |
| growth-strategy | business-intelligence | Standard | UTHR, MRK | none | **P5's mechanism** — is microgravity on any disclosed strategic roadmap, and against what stated problem |
| ratio-analysis | quantitative-analysis | Standard | UTHR, MRK, BMY, AMGN, LLY | **`late`** | The cohort margin ladder **price-stamped**; the basis discipline for §0.3 |
| reverse-dcf | quantitative-analysis | Standard | UTHR | **`late`** | **Pillar 1a's test**: what growth does UTHR's live quote require, and is any of it attributable to microgravity? The strongest available form of *"is the optionality priced"* |
| risk | risk-management | Light | UTHR | none | **The named-trigger watch-list (P4)**, with each trigger's expected source; and the disclosure-suppression risk in §0.4 |
| peer-bench | quantitative-analysis | Light | UTHR, MRK, BMY, AMGN, LLY | none | The cohort ladder's cross-member rank, with the LLY sector assignment shown as an explicit precondition |

### 3b. Consumed — not executed here

| Consumed from | What | Why this thesis does not run it |
|---|---|---|
| **001** Pillar 4 (UTHR unit-economics, the PIL-4 measured zero, DA-22) | The inherited baseline: the absence, the `UNRESOLVABLE-FROM-PUBLIC-SOURCES` verdict, the margin ladder | §0. Re-deriving it would produce the same zeros |
| **002** disposition-classification framework (002's P6) | The classification 010 applies to microgravity's `CLAIMED` figures | 002 owns it; 010 is an instance, not a re-derivation |
| **003** launch cost curve | **The launch component of the cost half** of the economic test | **003 owns 003's curve.** 010 cites it and never rebuilds it |
| **009** | The "immaterial-to-the-counterparty" pattern's first instance and its mechanism | The second instance is here (§0.4). Cross-reference, not shared universe |

---

## 4. Dependencies

- **001** — Pillar 4 is the inheritance: the UTHR artifact, the PIL-4 measured zero, DA-22
  (microgravity R&D not separately disclosed). **Consumed, not re-derived.**
- **002** — carries the disposition-classification framework (002's P6) that 010 applies.
- **003** — **owns the cost half's launch component.** 010 cites the curve and does not
  rebuild it.
- **009** — shares the "immaterial-to-the-counterparty" pattern; 010's is the second
  instance.
- **011** — sizing. **010 produces no position and no weight**, so 011 has nothing to size
  here until a trigger fires.

---

## 5. Market data

**Stage: `per_row` — declared, where the stub declared nothing.**

The stub's posture **(a)** — *hold microgravity as unpriced optionality within UTHR* — is a
claim about **price**, and a claim about price needs a price. It is also the one posture in
§1a that can be tested rather than merely named.

- **`late`** — `reverse-dcf` (UTHR, the pricing limb of Pillar 1a) and `ratio-analysis`
  (the price-stamped cohort ladder).
- **`none`** — every other executed row. **The filing-audit rows take no market input**, and
  saying so is part of the declaration.

**The feed is live and keyless.** `data-tools/market_data.py`, source `nasdaq`; verified in
004 round 3 (SPCX `$152.71`, close 2026-09-18). **Every price quoted here carries its date.**

⚠️ **The finding this stage is expected to produce, stated in advance so it is not
retrofitted.** If `reverse-dcf` shows UTHR's live quote is fully justified by the base
business's required growth, then **microgravity contributes nothing to the price — and
cannot, given that it contributes nothing to the disclosures.** *"Unpriced optionality"* is
then true but **not investable**: an asset the market cannot observe is not mispriced, it is
unobservable. **That is a real result, and it belongs to Pillar 1a, not to a sizing
decision.**

---

## 6. Known-open at re-scope

| # | Item | Disposition |
|---|---|---|
| **K-1** | **LLY has no 001 artifact** — researchable at 86% completion, not yet researched | `business-model` and `unit-economics` run on LLY fresh. **Sector assignment precedes any aggregate** |
| **K-2** | **The constitution's Tier 5 table carries the stale LLY row** (`PARTIAL — sector unassigned` under the *pre*-v1.6.0 class meaning) | §2 states the corrected reading. **Register the stale row for the next amendment** — the *class definition* was corrected at v1.6.0; the row was not re-stamped |
| **K-3** | **DA-22 — microgravity R&D is not separately disclosed** | This is the *mechanism* of §0.1's absence, not a defect in the audit. Recorded so a future reader does not read the zero as a search failure |
| **K-4** | **Varda's `CLAIMED` figures (~$329M raised, ~50 kg/mission)** | Carried as `CLAIMED` press figures with no filing. **Never substituted into the economic test** (Pillar 2's purpose) |
| **K-5** | **The ISS deorbit horizon (~2030) is T-6's timing anchor** | Recorded as a dated external event, not a forecast. If the horizon moves, T-6 moves with it |
