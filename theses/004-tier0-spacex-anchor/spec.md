# Research Thesis: 004 — Tier 0: SpaceX Anchor, SOTP across Space / Connectivity / AI

**Claim**: SPCX's live $2.07 trillion capitalisation is 312.8× the annualised operating income of Connectivity — its only profitable segment. No conglomerate discount exists to measure, and no admissible comparator exists for any of the three regimes: the partition closes at zero of eleven.

**Constitution Ref**: constitution.md v1.5.0 (`constitution_pin: 1.5.0`) — **re-pinned at
clarify round 2, 2026-09-19.** Was `1.4.0`, which lagged the ratified constitution by one
MINOR and brought neither **DA-29** (back-solved and opaque checks) nor **DA-30** (two bases
on one concept, collapsed without a basis field) into scope. **DA-30 governs §1c's
component-identity rule.** A queued **1.5.0 → 1.6.0** bump is registered as an
`expiry_trigger`, not left as a surprise.
**Created**: 2026-09-18
**Status**: Active
**Time Horizon**: 2026-Q4, terminating at the wave-1 hand-off to 005–006
**Depends on**: `001-technology-baseline` (pin 1.2.0 — the artifacts this thesis values), `002-evidence-validation` (**COMPLETE** — the validated input set; 004 inherits its figures *with their basis*, per round 2), `003-launch-cost-curve-value-migration` (**added at clarify round 2** — **004 consumes the curve matrix and the value-pool map and never re-derives either**; `PROGRAM.md` §5 already declared this edge as *"SPCX sizes off the curve"*, and 003's own header asserts it supplies *"the curve that 004 and 005 price off"*)
**Layer**: **4 of 4 — the valuation layer.** 001 built the panorama (quantities), 002 validated
them (grade ≠ basis), 003 mapped the cost curve and *where* value sits by margin. **004 is the
first thesis that asks what it is worth.** See round 2.
**Market data**: **LIVE, and this is a change of state.** Round 3 established that a **keyless**
market feed is available and serving — `data-tools/market_data.py`, source **nasdaq**, verified
**SPCX $152.71 (close 2026-09-18)** on 2026-09-19. `sotp-valuation` and `reverse-dcf` run at
**`late`**; the other executed rows at `none`. **The constitution's ~$1.62T anchor does not reconcile with the IPO price**: it implies
**$122.95/share** on the filed count (`13,176,000,000`) and **$119.41** pro-forma, against an IPO
struck at `$135.00` — a **~9% gap before any market move**. The live quote is **+27.9%** above the
anchor's own implied price, **not the ~13.1%** an earlier draft derived by comparing the live price
to the *IPO price*. Both bases are published and the spread between them is a finding. See §5.
**Binding constraint**: `CAPITAL` (PROGRAM §2). See Clarification Q-4 — named against the `POWER` reading, deliberately. **Q-11 is CLOSED at round 2:** the ecosystem framework is 011's, so the main line's constraint belongs to 011 and `CAPITAL` holds here unamended.
**Produces**: the **anchor valuation** — three segment multiple regimes with stated comparability boundaries and grades. **No trade ideas**: sizing is 011's.

---

## 0. Inherited baseline — what this thesis does NOT re-derive

001 established the following and this thesis **takes them as given**. 001 ran `operational-kpi`
and `unit-economics` on SPCX and produced **throughput** (mass to orbit, launches, subscribers,
ARPU, nameplate draw) and **cost** ($/kg). **It produced no valuation.** That gap is this thesis.

**Path shorthand used throughout this table — declared, not implied.** Paths are real and
relative to *this spec's directory*; `001/` expands to `../001-technology-baseline/`, and the
mid-path `…` expands to `artifacts/SPCX/`. Every row therefore resolves to a file on disk —
e.g. row 2 reads `../001-technology-baseline/artifacts/SPCX/2026-09-18_1239_operational-kpi_methodology.md`.
Except for row 1, which names both artifacts because the three-segment frame is a claim about the
whole SPCX corpus. The two `2310` artifacts are post-10-Q reads and **supersede the `1239` pair**
where they overlap — 001 recorded that supersession in its own status log and did not rewrite
the earlier files.

| Inherited result | 001 artifact | Grade |
|---|---|---|
| SPCX reports **THREE** segments as of Q2 2026 — Space, Connectivity, AI — and the frame **supersedes every prior two-segment SPCX artifact** | `001/artifacts/SPCX/2026-09-18_2310_business-model_methodology.md` §2, §4 | `DEMONSTRATED` |
| **Space**: revenue **$962M** (+29.0%), cost of revenue **$329M** (−0.3%), R&D **$1,076M** (+55.3%) = **3.3× cost of revenue**, SG&A $99M, total costs **$1,504M**, operating loss **$(542)M widening +46.9%** | `001/…/2026-09-18_1239_operational-kpi_methodology.md`; refined in `…_2310_operational-kpi_methodology.md` §2 | `DEMONSTRATED` |
| Space earns a **65.8% gross margin** (gross profit $633M) and the loss is **Starship development R&D**, not launch economics — cost of revenue was *flat* while revenue rose 29% | `001/…/2026-09-18_2310_operational-kpi_methodology.md` §2 | `DEMONSTRATED` |
| **Connectivity**: revenue **$4,291M** (+65.8%), operating income **$1,656M** (+79.4%), subscribers **12.0M** (+101.2%), ARPU **$66/mo vs $85/mo (−22.4%)** | `001/…/2026-09-18_1239_operational-kpi_methodology.md`; `…_2310_operational-kpi_methodology.md` §4 | `DEMONSTRATED` |
| Connectivity is the **only segment with demonstrated operating leverage in the 35-name universe**; segment gross margin **52.0%**; **enterprise/government outgrew consumer** (+$939M vs +$764M) | `001/…/2026-09-18_1239_operational-kpi_methodology.md`; `…_2310_operational-kpi_methodology.md` §4 | `DEMONSTRATED` |
| **AI**: revenue **$2,561M** (+247.5%), operating loss **$(1,257)M** narrowing −17.5%, **nameplate compute draw 1.4 GW vs 0.4 GW (+250%)** | `001/…/2026-09-18_2310_operational-kpi_methodology.md` §2 (revised) | **`DERIVED`, not disclosed** — see V-1 resolution below. |
| **DA-23 at consolidation**: Space −542 + AI −1,257 + Connectivity +1,656 = **−143 operating LOSS**, while `get_company_financials` returns `OperatingIncomeLoss: +143,000,000` | `001/…/2026-09-18_1239_operational-kpi_methodology.md` §segment reconciliation; `…_1239_unit-economics_methodology.md` data-quality note | `DEMONSTRATED` |
| **DA-11**: the 1.4 GW is **IT load only** — explicitly excluding cooling, power distribution losses, lighting, security, facility overhead. True facility draw typically **1.2–1.5×**. Called *"the most dangerous figure in this thesis"* | `001/…/2026-09-18_1239_operational-kpi_methodology.md` §AI | `DEMONSTRATED` (the definition). **The restatement is 002's — not re-derived here.** |
| **A4 boundary**: the AI segment is **ground-based**. SPCX's separate filing for up to **1 million satellites at 100 kW of compute per tonne** is a **filed aspiration with no revenue line**, inadmissible as a valuation input | `001/…/2026-09-18_1239_operational-kpi_methodology.md`; constitution §0 A4 and §P10 | `CLAIMED` |
| **Mass to orbit 485 t vs 652 t (−25.6%)** while revenue rose +91.9%; customer payload **flat at 87 t vs 88 t**; Falcon launches 37 vs 45 (−17.8%); only **10 of 37** count as customer launches; internal 27 (−25.0%); Starship 3 → 1 across H1 | `001/…/2026-09-18_2310_operational-kpi_methodology.md` §1 | `DEMONSTRATED` |
| **A1b falsified on SPCX's own metrics** — revenue +91.9% with Falcon launches −18% and Space up only +29.0% | `001/…/2026-09-18_2310_operational-kpi_methodology.md` §1; constitution §0 A1b | `DEMONSTRATED` |
| **Capital**: H1 2026 operating CF **+$3,466M**, investing **$(34,487)M**, financing **+$100,291M**; IPO net proceeds **$85,675M** (638.9M shares at $135.00); **$40,869M** notes at a 6.03% effective rate; **$856M** EchoStar spectrum instalments | `001/…/2026-09-18_2310_operational-kpi_methodology.md` §5 | `DEMONSTRATED` |
| **Entity discontinuity**: X merger 2025-03-28, xAI merger **2026-02-02 (common control)**, IPO 2026-06, five-for-one split 2026-05, **Cursor $60B all-stock pending Q3 2026** — *"the single largest statement-level discontinuity in the universe"* | `001/…/2026-09-18_2310_business-model_methodology.md` §1 | `DEMONSTRATED` |
| **Segment revenue shares**: Connectivity **54.9%**, AI **32.8%**, Space **12.3%**; consolidated **$7,814M**; H1 Space **$1,581M vs $1,611M (−1.9%)** while H1 total rose +53.7% | `001/…/2026-09-18_2310_business-model_methodology.md` §2 | `DEMONSTRATED` |
| **DA-01 bases** — A ~$2,939/kg, A′ ~$4,220/kg, B ~$525–875/kg, C ~$6,596/kg: a **7–13× spread** round one Falcon mission; the **22.8 t denominator is `CLAIMED`** | `001/…/2026-09-18_1239_unit-economics_methodology.md`; `…_1239_operational-kpi_methodology.md` | `DEMONSTRATED` (A′, C figures) / `MODELED` (B) / `CLAIMED` (denominator) |
| **Market-cap anchor ~$1.62T** (SPCX anchors the top of the market-cap screen) | `constitution.md` §Research Scope Constraints | `CLAIMED` — a dated print, not a live one. **Market Data Stage is `none`.** |

**What 001 did not do:** convert throughput and cost into **value**. Every figure above is a
quantity, a price or a cost. None is a multiple, a segment value, or a discount. That is this
thesis's entire scope — and it is why 004 is the anchor rather than another segment thesis.

### Inherited from 003 — **added at clarify round 2, 2026-09-19**

`PROGRAM.md` §5 has always declared the edge — `003 ──> 004 (Tier 0) — SPCX sizes off the
curve` — and 003's own header states it supplies *"the curve that **004 and 005 price off**."*
**This spec did not carry it.** The string "003" appeared twice, both times incidentally
inside round 1's record. The edge is now explicit, and its direction is one-way:

| Inherited from 003 | 003 output | 004 consumes it as | 004 may **not** |
|---|---|---|---|
| **The curve matrix** — vehicle × reuse architecture × DA-01 basis, with the **per-architecture F5 floor** applied (F5a fully reusable, F5b partially reusable, **F5c fully expendable**) | `_cross/` curve matrix | The **Cost** limb of the Space segment's multiple regime (**P4**), and the DA-01 A/A′/B/C restatement | Re-derive any $/kg base, or apply a floor the constitution names for a different architecture |
| **The value-pool map** — revenue growth and operating margin by segment, on the issuer's own boundaries (**DA-21**) and on a normative restatement, across 9 names | `_cross/` value-pool map | The **prior** the SOTP's three regimes must be consistent with: 003 located where value sits; **004 prices it** | Re-map the pool, or re-run the cross-issuer launch-vs-non-launch margin test |
| **The demonstrated-versus-claimed split** across the vehicle set | curve matrix, P3 | The admissibility test for every $/kg that enters the SOTP | Treat a `CLAIMED` curve as a factual one — the error P1 of 003 exists to prevent |

**003's explicit limit is 004's mandate.** 003 states: *"This thesis produces no position and
no valuation"* and, under **P10**, *"It does **not** value any constellation."* 003 stops at
*"+38.6% operating margin, 12.0M subscribers"* and never converts it. **That conversion is
004's entire scope**, and it is the whole of the layering:

> **001 built the panorama (quantities). 002 validated them — and found grade ≠ basis.
> 003 mapped the cost curve and *where* value sits, by margin. 004 is the first thesis that
> asks what it is *worth*.**

**Scope consequence — 004's coverage is SPCX's three segments, and those three segments are
three 板块.** 004 is the programme's **only** valuation of satellite connectivity and
terrestrial compute at the anchor: 006's universe (IRDM, GSAT, SATS, ASTS, VSAT) does not
contain SPCX, 009's (VRT, NVDA, GOOG, MSFT, AMZN, AAPL) does not either, and 005 is space
pure-plays. **SPCX Connectivity — 54.9% of anchor revenue, the sector's largest connectivity
operator at 12.0M subscribers — is valued only here.** The Connectivity and AI anchor rows are
therefore built as **reusable references**, and §5's comparability boundaries name **006 and
009** as permitted to price off them, not 005 alone.

### Validation queue — segment attribution and valuation inputs

**Scope boundary, stated first.** `002-evidence-validation` owns **denominator and physics**
validation: the three `CLAIMED` payload masses (002 P1), F2's two unsourced constants (002 P2),
the universe-wide DA-23 census (002 P3) and the DA-11 PUE restatement (002 P4). **004 does not
re-derive any of them.** 004's queue is the one 002 does not carry: **whether the segment
attribution is real, and whether the valuation inputs are admissible.** Where 002 has not yet
landed, 004 inherits 001's grade unchanged and labels it.

| # | Item | Why it gates a pillar | Resolving source |
|---|---|---|---|
| **V-1** ✅ **RESOLVED — and the resolution was WRONG the first time.** **Does the AI segment file an operating result at all?** **YES — it is FILED, disclosed four times.** An earlier version of this row concluded the line was *"`DERIVED`, not disclosed"* on the strength of `2310_operational-kpi` §2. **Phase 1 of thesis 002 disproved that from the source:** `$(1,257)M` appears at **p.30 (Note 18), p.44 (with a full cost stack summing to the filed $3,818M total), p.45 (narrative prose) and p.46 (reconciliation)**, and the identity `2,561 − 1,106 − 2,178 − 532 − 2` closes exactly. **The earlier `1239` artifact was right; the nominal supersession introduced the error, and this row propagated it into 002's brief.** | **The MDV is REINFORCED, not merely preserved.** P1's separability test is **3 of 3 DISCLOSED**, not 2 of 3 — the stronger reading. The DERIVED subtraction is retained as a **confirming cross-check only**. **Lesson recorded:** a *supersession* claim is itself an evidence claim and needs the same page-level verification as any other; "newer artifact wins" is not a validation. | Corrected 2026-09-18 from `002/artifacts/SPCX/2026-09-18_1500_operational-kpi_methodology.md` |
| **V-2** | **Segment-to-consolidated reconciliation residual.** `value-checks.yaml` carries `segments_sum_to_total` at **`fail`** level | A non-zero residual means the SOTP denominator is broken before the first multiple is applied | 10-Q segment note; show the residual in-line |
| **V-3** | **Is the AI segment homogeneous enough to carry one multiple?** It aggregates **Grok, X (advertising) and compute** — DA-21 (issuer-defined segment boundaries) in operation | A multiple applied to a segment mixing advertising with compute infrastructure is not a multiple | Note 1 and Note 3, segment definitions |
| **V-4** | **Does the Space series survive the entity boundary?** Common-control recast (DA-19) means growth rates across 2025-03-28 / 2026-02-02 mix real growth with entity change. 001 found **Space is the one series that survives** | The SOTP's growth inputs for Connectivity and AI are contaminated; Space's are not | 10-Q MD&A, `2310_business-model` §1 |
| **V-5** | ✅ **RESOLVED at implement, 2026-09-19 — AND THE PREMISE WAS WRONG: THE DEAL HAS ALREADY CLOSED.** Round 4 made the headline **PRO-FORMA** and V-5 `blocking` on the ground that the dilution was *not determinable*. **It is determinable, and the transaction completed on 2026-08-14.** The **8-K `0001628280-26-056945` (filed 2026-08-14), Item 2.01**, states: *(i)* Cursor common and preferred converted into **389,289,254 shares of Class A**; *(ii)* vested Cursor RSUs converted into **1,752,426** more; *(iii)* unvested RSUs and options were **assumed and converted into ~29,128,326 Company RSUs and ~44,365,047 options**. **At close: 391,041,680 shares issued; total potential dilution 464,535,053.** ⚠️ **THE PRICING IS INVERTED FROM WHAT THE PLAN ASSUMED** — per-share consideration is the **VWAP of the seven consecutive trading days immediately preceding closing**, not `$60B ÷ 389.3M`. The $60.0bn is the *implied equity value*; **$60.0bn ÷ 389,289,254 = $154.13/share**, against a live quote of **$152.71** | **RESOLVED — the dilution that `blocking`-gated P1 is now a filed number.** The pro-forma headline is not merely admissible, it is **the actual basis**: Cursor has been consolidated since 2026-08-14, so a PRE-close headline would now be the counterfactual one | 8-K **`0001628280-26-056945`**, 2026-08-14, pages 2 and 55. **Route: `search_documents` → `read_source_pages`** — `get_segment_data` is broken and cannot help. ⚠️ **Page 55's capitalization schedule is dated 2026-04-15 and is therefore PRE-IPO and PRE-split — it is NOT the current share count** |
| **V-6** | **Price-input datability.** Market Data Stage `none` → no live price | The discount measure is **as-of a named print**, never live; the print and its date travel with every quoted figure | `$135.00` IPO price (2026-06); constitution's **~$1.62T** anchor |
| **V-7** | ✅ **RESOLVED at clarify round 4, 2026-09-19 — the percentages ARE in the platform, via XBRL dimensional facts, not Note 3 prose.** **Customer A: 17.89% H1 2026 · 18.30% Q2 2026 · 19.89% H1 2025 · 16.70% Q2 2025. Customer B: 12.20% H1 2026 · 19.50% Q2 2026.** Retrieved as `ConcentrationRiskPercentage1` under `srt:MajorCustomersAxis` × `ConcentrationRiskByTypeAxis: CustomerConcentrationRiskMember` × `ConcentrationRiskByBenchmarkAxis: RevenueFromContractWithCustomerMember`, source file `spcx-20260630.htm`, authority 2. **Three findings ride on the retrieval itself:** (a) **Customer A repeats 003's two-bases-opposite-signs pattern** — H1 falls (19.89% → 17.89%) while Q2 rises (16.70% → 18.30%), so a single quoted customer share is a basis choice, not a fact; (b) **Customer B has no 2025 comparative**, appearing only in 2026 — consistent with an entity acquired inside the period, and it must carry the **DA-19 common-control boundary flag**; (c) **combined concentration is 30.09% of H1 revenue**, which is the input the backlog limb needed | **The DCF's *backlog limb* is now evaluable at the Space segment** — the only place it could pass. Customer concentration is not itself a backlog figure, but it bounds the counterparty set the backlog could consist of, and it converts *"unquantified"* to *"bounded"* | `search_xbrl_facts(ticker=SPCX, concept=ConcentrationRiskPercentage1, view=detailed)`. **Not** `get_segment_data`, which is broken — see round 4 |

> **Under P4, an unvalidated number is a pillar that cannot fire.** **`blocking` set, as amended
> at round 4: V-1 (✅ resolved), V-2, V-5, V-7 (✅ resolved)** — P1 cannot be delivered without
> them. **V-3, V-4, V-6 are `warn`** and are reported as bounds rather than resolved to a point,
> per the §1c standing rule.
>
> **V-5 MOVED FROM `warn` TO `blocking` IN THIS ROUND, and the move is a direct cost of the
> pro-forma headline answer.** Pre-close, Cursor's dilution could be set aside as a sensitivity;
> pro-forma, it is an input to the headline. **V-7 moved the other way — resolved — and the two
> moves are independent.** Net: the blocking set is unchanged in size (2 cleared, 1 added) but
> the *composition* changed, and V-5 is now the critical path.

---

## 1. Research Question

**What is SPCX worth as three separate businesses — Space, Connectivity, AI — and does the
market price it as one?**

The constitution makes **scenario-weighted sum-of-the-parts primary for multi-segment issuers
precisely because SPCX's three segments are three different businesses with three different
multiples.** SPCX is the cleanest case the rule was written for: a 65.8%-gross-margin launch
business that loses money on development R&D, a 38.6%-operating-margin broadband operator that
is 54.9% of revenue, and a 247%-growth terrestrial compute business that is the largest single
contributor to consolidated growth. Valuing those three at one blended multiple is not a
simplification. It is a different claim, and the spread between the two is the finding.

This thesis therefore answers the question the constitution already told us to ask, and it
answers it in the register the constitution requires: **three multiple regimes, each with a
stated comparability boundary and a grade, scenario-weighted, and reconciled against a dated
market print.**

### Why this thesis exists at all

001 could have been extended with a valuation. It was not, and the reason is structural rather
than stylistic. Three specific facts make the SOTP the only admissible method — and each is a
finding in its own right:

1. **A consolidated earnings multiple is not available.** SPCX's DA-23-corrected operating
   result is **$(143)M** — a loss. Its H1 2026 free cash flow is deeply negative ($3,466M
   operating against $34,487M investing). Comps on consolidated earnings or on FCF are
   **inadmissible, not merely unattractive** — the constitution bars treating comps as primary
   for a pre-profit issuer, and at the consolidated line SPCX is one.
2. **A consolidated DCF is not admissible either.** SPCX fails the constitution's **≥3 years of
   positive FCF** limb outright, and the backlog limb reaches **only the Space segment** (1–14
   year Launch and Development contracts, themselves unquantified — V-7). Full gate at §1c.
3. **The segments are not arm's-length, and the SOTP must say so.** **27 of 37 Falcon launches
   were internal** (DA-08) and generate **no inter-segment revenue** — the cost is capitalised
   into satellites in PP&E. Space is therefore simultaneously a revenue business, a 12.3% segment
   *and* an unpriced capex input to Connectivity. A sum-of-the-parts on a company with material
   unpriced inter-segment transfers is not wrong, but it is only honest if the transfer is
   stated as a limitation rather than netted away.

---

## 1b. Pillars

### Pillar 1 — The three-segment SOTP is buildable, and the implied conglomerate discount is measurable (Priority: P1) 🎯 Minimum Defensible View

The constitution asserts that SPCX's three segments are three different businesses with three
different multiples. **That assertion is untested.** It requires each segment to carry a
discrete filed revenue line *and* a discrete filed operating result — and it requires the three
to reconcile to the consolidated total, which `value-checks.yaml` already enforces at `fail`
level via `segments_sum_to_total`.

**V-1 makes this pillar live rather than formal.** Two 001 artifacts disagree on whether the AI
segment files an operating result: `1239_operational-kpi` reports **$(1,257)M** and the
DA-23 reconciliation depends on it; `2310_operational-kpi` §2 records *"not disclosed."* If the
latter is right, the SOTP is **two segments plus an unattributable residual**, P1's threshold
cannot be met, and the Minimum Defensible View fails on its first test. This is not a
bookkeeping question — it decides whether SPCX can be decomposed at all.

**The claim:** all **three** segments carry a discrete filed revenue line **and** a discrete
filed operating result, the three reconcile to consolidated within 2%, and a
**scenario-weighted SOTP** built on those three regimes yields a value range that can be
compared against **both price bases — the live quote and the dated constitution print, with the
spread between them reported** — to quantify a **conglomerate discount or premium**, stated as
such, with each price's basis and stamp travelling with the number.

**Headline basis: PRO-FORMA (confirmed at clarify round 4, 2026-09-19 — overriding the round-0
provisional).** Cursor is **inside** the headline, not a separate sensitivity. **This converts
V-5 from `warn` to `blocking`**: the $60B all-stock consideration and its dilution become an
input to P1 rather than an optional footnote, and P1 cannot be delivered without them.

**Why this priority**: it is the Minimum Defensible View because it is the only deliverable that
makes 004 an anchor. 005, 006 and 007 all benchmark against it; if the decomposition does not
hold, the anchor degrades to a single blended multiple and **every downstream comparability
statement inherits that coarseness silently**.

**Independently falsifiable**: a segment without a discrete filed revenue line or operating
result — i.e. fewer than three separable businesses.

**wrong_if**: `metric=count_of_spcx_segments_with_a_discrete_filed_revenue_line_and_operating_result threshold=3 source=10-Q_segment_note op=<`

**Subscribed**: `SPCX × sotp-valuation`

**Consumes (003)**: `SPCX × business-model`, `SPCX × operational-kpi`, `SPCX × recent-quarter`, `SPCX × ratio-analysis` — cited from §3b, **generating no tasks by design**. *(This field is not parsed by `plan_audit` or `tasks_md`; `Subscribed` above carries only EXECUTED skills. See §3b's shape note.)*

**Binding constraint**: *comparability* — not `CAPITAL`. P1 is bounded by whether each segment's
inputs exist and reconcile, which no capital injection repairs.

---

### Pillar 2 — Connectivity is the value, and its operating leverage survives ARPU decay (Priority: P2)

Connectivity is the only segment in the 35-name universe with **demonstrated operating
leverage**: income from operations **+79.4%** on revenue **+65.8%**, at a **38.6% operating
margin** and a 52.0% gross margin. The constitution rates Satellite Connectivity
**OVERWEIGHT / High** on exactly this evidence.

**Against it stands a single number: ARPU fell −22.4% ($85 → $66) while subscribers rose
+101.2%.** Under **DA-10** the decline is genuinely ambiguous — subscriber service revenue only,
excluding enterprise, government, aviation and maritime, with SPCX attributing the fall to
*"international expansion and the addition of lower priced service plans."* **At least part of
the 22.4% is therefore a mix-shift artefact rather than price erosion, and the two readings are
not distinguishable from public disclosure.** That ambiguity is the whole pillar: a mix shift
means volume strategy and durable margin; price erosion means the cheap cohort compresses margin
as it scales.

**The claim:** the operating-leverage case **survives** the ARPU restatement on a
revenue-per-subscriber and margin basis, with **all four DA-10 readings reported side by side**
per the §1c standing rule — so the segment enters the SOTP on a margin that is **stable or
expanding**, not on a margin that is being bought.

**Why this priority**: P2 rather than P1 because it is the SOTP's largest input by value
(54.9% of revenue, and the only segment with positive operating income) but not the
decomposition's precondition. If P1 fails, P2 has nothing to sit inside; if P2 fails, P1 still
delivers a decomposition with a *declining* anchor segment — a worse but valid answer.

**Independently falsifiable**: a Connectivity operating margin that declines year over year on
the component identity, or a subscriber/revenue series in which revenue per subscriber falls
faster than ARPU, which would identify price erosion rather than mix shift.

**wrong_if**: `metric=connectivity_segment_operating_margin_yoy_change_pp threshold=0 source=10-Q_segment_note_component_identity_at_filed_segment_basis op=<`

> **Basis named in-line (A-2, applied at plan time 2026-09-19).** The falsifier reads
> **segment operating income ÷ segment revenue, at the issuer's own filed segment boundary,
> with the component identity (`gross profit − opex`) shown in-line.** It previously read
> `source=10-Q_segment_note_component_identity` alone, which does not name a basis — and 002's
> programme-level result is that **a grade does not carry a basis**: SPCX `operating_margin`
> reproduces exactly on two bases that differ by **46.47pp** (filed **−16.68%** vs platform-served
> **+29.79%**). **A falsifier whose `source` does not name its basis can fire on a basis the
> author never checked.** The metric token already said *segment*; the source now says so too.

**Subscribed**: `SPCX × revenue-decomp`

**Consumes (003)**: `SPCX × unit-economics`, `SPCX × operational-kpi`, `SPCX × recent-quarter`, `SPCX × what-if` — cited from §3b, **generating no tasks by design**.

**Binding constraint**: `DEMAND` — the segment is bounded by whether the price-volume trade
continues to add contribution, not by any physical or capital limit.

---

### Pillar 3 — The AI segment has no admissible multiple from filed or peer data, and must be carried at cost or as optionality (Priority: P3)

The AI segment is **32.8% of revenue**, the **largest single contributor to consolidated
growth** (+$1,824M), and the **largest recipient of capital allocation**. It is also the segment
with the **weakest valuation basis in the SOTP**, and the reason is constitutional rather than
analytical.

**A4 is explicit:** terrestrial and orbital compute are different businesses and must never be
valued as one; SPCX's AI segment is **ground-based**; the 1-million-satellite /
**100 kW-per-tonne** filing is a *filed aspiration with no revenue line*, **inadmissible as a
valuation input**. **P10 gates orbital compute** on five conditions, none of which SPCX's AI
segment meets — because it is not an orbital-compute business. **DA-11 then removes the
segment's own headline metric from the SOTP entirely**: the 1.4 GW is **IT load**, explicitly
excluding cooling, power distribution, lighting, security and facility overhead, so it is a
**capacity** figure, not a revenue or earnings figure, and it cannot be converted without a
$/kW-revenue assumption that no issuer discloses.

The usual escape — price it off peers — fails on inspection. **MSFT, GOOG and NVDA do not report
a discrete compute-infrastructure segment carrying a comparable multiple**: MSFT's compute sits
inside Intelligent Cloud as a cost centre, GOOG's inside Google Cloud, and NVDA is the silicon
supplier rather than the operator. Each is a read-through, not a comparable.

**The claim:** exactly three framings are evaluated side by side per §1c — **(a)** a terrestrial
compute comparable multiple where one can be bounded, **(b)** **invested capital**, using the
H1 2026 capex attributed *"first to the build out of DATA CENTERS and related infrastructure,"*
and **(c)** **optionality at a stated value, including zero** — and the SOTP headline names
**which one it uses**. At least one framing must be admissible from filed data; a segment carried
at zero is a legitimate output, but it must be *stated*, never implied.

**✅ CONFIRMED at clarify round 4, 2026-09-19 — the headline framing is (b) INVESTED CAPITAL.**
All three are still reported side by side per the §1c standing rule, and the choice is now named
rather than pending. **Why (b) rather than (a) or (c):** invested capital is the only framing that
**is disclosed, needs no comparable, and is auditable from filed cells** — the H1 capex
attribution names data centers first, so the number exists. **(a)** became materially stronger in
round 4, because a live feed makes a terrestrial-compute interval constructible for the first
time — but it is **admitted non-comparable** by construction (MSFT's compute is a cost centre
inside Intelligent Cloud, GOOG's inside Google Cloud, NVDA is the supplier), so it can inform the
range without carrying the headline. **(c)** remains legitimate and stated.

**Why this priority**: P3 because it changes the SOTP's answer by tens of percent while P1 and P2
change it by more — but its falsifier is genuinely reachable, and an anchor that publishes an
invented AI multiple **contaminates every downstream thesis that prices off it**.

**Independently falsifiable**: no admissible framing produced by any of the three — i.e. the AI
segment is carried `UNRESOLVABLE-FROM-PUBLIC-SOURCES` at zero, and P1's separability test then
governs whether the SOTP survives at all.

**wrong_if**: `metric=count_of_admissible_ai_segment_valuation_framings_derivable_from_filed_or_peer_data threshold=1 source=10-Q_segment_note_capex_disclosure_and_peer_bench_tables op=<`

**Subscribed**: `SPCX × revenue-decomp`, `SPCX × reverse-dcf`, `SPCX × comps`

**Consumes (003)**: `SPCX × business-model`, `SPCX × peer-bench`, `SPCX × secular-trends`, `SPCX × what-if` — cited from §3b, **generating no tasks by design**. **FC-2 flags that `peer-bench` was run by 003 on a different ticker set** (SPCX, RKLB, FLY) than 004's AI framing set needs.

**Binding constraint**: `POWER` is the constraint on the *business*, but the constraint on
*valuing* it here is `A4` — a constitution-level boundary, not an operational one. **Not
`CAPITAL`**: capital is being spent and is disclosed; what is missing is an admissible
capitalisation of it.

---

### Pillar 4 — Space is a public good with a private balance sheet: standalone value separable from Starship funding (Priority: P4)

Two facts about Space that point in opposite directions, and both are `DEMONSTRATED`:

- It carries **the highest gross margin in the universe — 65.8%** — with **cost of revenue flat
  (−0.3%) while revenue rose 29.0%**, so **the marginal Falcon launch is highly profitable**.
- It reports an **operating loss of $(542)M, widening +46.9%**, because **R&D is $1,076M — 3.3×
  cost of revenue and 111.9% of segment revenue** — driven by Starship production, engineering
  and test.

**The difference is the entire question.** Basis C's **$6,596/kg** fully-loaded figure is
**Starship-subsidised**: it divides a segment cost base inflated by a future vehicle by a
current-vehicle customer-tally. An analyst arguing *"SpaceX loses money on every launch"* and
one arguing *"SpaceX is profitable per launch"* can both cite the same filing; the difference is
whether Starship R&D is assigned to Falcon missions.

**The claim:** the standalone launch business is **separable** from Starship development funding —
the segment's **ex-Starship-development operating result is positive** — and therefore carries
standalone value in the SOTP rather than being carried as an input-cost centre. The
**inter-segment transfer limitation** (DA-08: 27 of 37 launches internal, no inter-segment
revenue) is **stated in the SOTP as a limitation**, not netted silently.

**Why this priority**: P4 because the segment is 12.3% of revenue and falling (−1.9% H1) — too
small to move the anchor, and large enough that mis-assigning Starship R&D changes whether the
SOTP has two or three positive-value segments. It is also where **A1b's falsification is priced**:
value migrated from launch to constellations and services, and the SOTP must show that migration
rather than assert it.

**Independently falsifiable**: an ex-R&D Space segment result that is **negative**, i.e. gross
profit less SG&A below zero — at which point launch has no standalone value even before any
Starship allocation, and Space enters the SOTP as an input cost with its revenue treated as
strategic rather than economic.

**wrong_if**: `metric=space_segment_operating_margin_ex_RD_pct threshold=0 source=10-Q_segment_note_component_identity_at_filed_segment_basis op=<`

> **Basis named in-line (A-2, applied at plan time 2026-09-19).** Same correction as **P2**: the
> reading is **segment operating income ÷ segment revenue at the filed segment boundary**, with
> the component identity in-line — and here the basis question is sharper still, because the
> metric is **ex-R&D** and the R&D split is **`MODELED`, not disclosed** (the filing does not
> separate Starship from Falcon R&D). **The ex-R&D numerator is therefore a construction, and the
> falsifier can only fire on the construction's own stated method.** That limit is carried in P4's
> binding-constraint note and is not repaired by naming the basis — naming it is what makes the
> limit visible.

**Subscribed**: `SPCX × revenue-decomp`, `SPCX × competitive`

**Consumes (003)**: `SPCX × operational-kpi`, `SPCX × unit-economics`, `SPCX × business-model` — cited from §3b, **generating no tasks by design**.

**Binding constraint**: `MANUFACTURING_RATE` in the medium term — F5b, the expended second-stage
manufacturing curve is the binding floor for a partially reusable vehicle, not propellant.
**The ex-R&D test itself is bounded by disclosure granularity**, since the filing does not split
Starship from Falcon R&D; the split is therefore `MODELED` and must be labelled so.

---

### Pillar 5 — `CAPITAL` is the binding constraint, and the SOTP's swing factor is the funding requirement (Priority: P5)

The constitution requires **exactly one** binding constraint per thesis, and PROGRAM §2 names
**`CAPITAL`** for 004. The operational reading is direct: SPCX is deploying capital at a scale no
internal cash flow approaches, and it is deploying it **on the ground**.

```
H1 2026 operating cash flow   +$3,466M
H1 2026 investing            $(34,487)M     ← coverage ≈ 0.10×
H1 2026 financing           +$100,291M      ← IPO $85,675M + notes $40,869M
```

**A company with a $(143)M quarterly operating loss raised $85.7B in equity and $40.9B in notes,
and named data centers before launch facilities when describing the capex.** The constraint that
binds is the **cost and availability of external capital** — because it is the only input whose
withdrawal stops the build, whereas a delay in any physical constraint merely moves it.

**The claim:** within the SOTP's forecast horizon, **internal cash flow does not cover the
compute build** (coverage ratio **below 1.0×**), so the anchor's downside scenario is governed by
the funding structure rather than by any physical or demand constraint — and the anchor **states
its financing assumption explicitly**, including the **Cursor** $60B all-stock dilution under
P11 and the single-class control structure that determines who can price that dilution.

**Why this priority**: it is P5, not P1, because it is a *context* claim rather than a *value*
claim — but it is the one that decides which scenario the SOTP's probability weights belong on,
and it is the **only pillar whose falsifier would re-rate every other pillar at once**.

**Independently falsifiable**: an internal coverage ratio at or above **1.0×** over the SOTP's
horizon, which would mean the build is self-funding and the capital constraint is not binding.

**wrong_if**: `metric=spcx_ttm_operating_cash_flow_coverage_of_investing_outflow_ratio threshold=1.0 source=10-Q_cash_flow_statement op=>=`

**Subscribed**: `SPCX × risk`, `SPCX × growth-strategy`, `SPCX × competitive`

**Consumes (003)**: `SPCX × ratio-analysis`, `SPCX × recent-quarter` — cited from §3b, **generating no tasks by design**. **FC-1 flags that `ratio-analysis` is registry-`late` while consumed at 003's `none`.**

**Binding constraint**: `CAPITAL` — the thesis-level constraint, carried here. **Index inclusion
and float structure ride on the same pillar**: the constitution records **no index inclusion at
ratification**, so the marginal buyer of the equity that funds the build is a **dated catalyst**,
not a standing assumption, and it must be recorded as such or dropped.

---

### Pillar 6 — The anchor publishes three regimes *with comparability boundaries*, not three numbers (Priority: P6)

004's value to the programme is not its number — it is that **005–009 benchmark against it**
(PROGRAM §5). An anchor published as a point estimate, or as a multiple without a stated
comparability set, propagates a **false comparability** into every downstream thesis, and the
error is invisible because the downstream theses will each look internally consistent.

**The failure is structural and each segment fails for a different constitutional reason:**
Space's pure-play comparables (RKLB, FLY) are **loss-making**, so no earnings multiple exists;
Connectivity's *profitable* comparables (IRDM, GSAT) are **P11 deal securities** whose prices
track spreads rather than fundamentals, so their multiples are inadmissible; and AI's comparables
**do not report a discrete compute segment** at all. **Three regimes, three different reasons no
natural comp set exists.** The SOTP must therefore source its multiples from SPCX's own segment
data and from bounded read-throughs, and say which comparators are **admissible** and which are
**excluded, and why.**

**The claim:** the anchor table publishes **one multiple regime per segment**, each with a
**source, a grade, and an explicit comparability boundary** naming which downstream names may
and may not price off it — and **zero** published anchors lack a boundary.

**✅ CONFIRMED at clarify round 4, 2026-09-19 — a boundary is a PARTITION, not a graded score.**
A name is **in or out**, and the excluded class is named with its reason — `P11`, loss-making,
`PARTIAL` coverage, or non-disclosure. **A graded score was considered and rejected**: it invites
the downstream thesis to pick its own threshold, which is the failure P6 exists to prevent.
**Round 3's live data makes this constraint harder, not easier** — a live multiple on a P11
spread (IRDM, GSAT) is *priced* and still *inadmissible as a fundamental*, so it lands in the
excluded class with `P11` as its reason, and the boundary is **verifiable** rather than asserted.

**Why this priority**: last because it is the hand-off, and it can only be written after P1–P5
land. Its payoff is that it is the mechanism by which the anchor **fails loudly instead of
silently** in someone else's thesis.

**Independently falsifiable**: any published segment anchor without a stated comparability
boundary — including an anchor whose boundary is "all peers," which is the same failure stated
politely.

**wrong_if**: `metric=count_of_published_segment_anchors_without_a_stated_comparability_boundary threshold=0 source=004_anchor_table op=>`

**Subscribed**: `SPCX × comps`, `SPCX × reverse-dcf`

**Consumes (003)**: `SPCX × peer-bench`, `SPCX × sector-overview`, `SPCX × ratio-analysis` — cited from §3b, **generating no tasks by design**.

**Binding constraint**: *disclosure granularity* — the anchor can only publish a boundary as
narrow as the comparables' own segment disclosure permits. **Not** `DEMAND`: the constraint on
the hand-off is what the peers disclose, not how much demand exists.

---

> **Delivering P1 alone yields a defensible partial conclusion** — SPCX either decomposes into
> three separable businesses or it does not, and 005–009 will know which before they size
> anything. That is the single most valuable output of this thesis and it is delivered first.

## 1c. Method — the valuation instruments

Four capabilities are specific to this thesis and are the reason an anchor valuation is a
distinct workstream rather than a pass over 001's artifacts.

1. **Scenario-weighted SOTP — the constitution-mandated primary instrument.** Three segments,
   three multiple regimes, probability-weighted scenarios. **The multiple-sourcing problem is the
   method's real content**, and it is worse than it looks: each segment fails to find a natural
   comp set for a different reason.

   **Two bases the instrument declares on its face (A-11, applied at plan time 2026-09-19):**
   **the headline is PRO-FORMA** — Cursor is inside it, so V-5's dilution is a prerequisite, not a
   sensitivity (see P1 and §5) — and **the Space segment enters on a stated non-comparability
   boundary**, carrying the **DA-06** flag, because a captive-integrated launcher has **no
   transaction price** and a multiple cannot be borrowed from an issuer that has one. Space's
   value therefore comes from **segment contribution**, and the SOTP says so rather than
   importing a comparable that would make it look comparable.

   | Segment | Natural comparables | Why no admissible comparable multiple exists | SOTP treatment |
   |---|---|---|---|
   | **Space** | RKLB, FLY (005); BA, LMT, NOC (007) as primes | Pure-plays are **loss-making** — there is no earnings multiple to borrow | Revenue or capacity multiple, `MODELED`, stated as a range |
   | **Connectivity** | IRDM, GSAT (006); ASTS, VSAT (006) | The profitable comparables are **P11 deal securities** — their price is a **spread**, not a fundamental. ASTS/VSAT are `PARTIAL` | Margin-anchored, `MODELED`, cross-checked against terrestrial broadband rather than satellite peers |
   | **AI** | MSFT, GOOG, NVDA (009) | **None reports a discrete compute-infrastructure segment carrying a comparable multiple** | One of three framings; see **P3** |

   **The only `DEMONSTRATED` inputs to the SOTP are the segment financials themselves.** Every
   multiple is `MODELED`, and P4 requires each to be labelled as such. Scenario weights are
   likewise `MODELED` — no vendor source exists for them, and `assumptions.yaml` carries no
   scenario-weight field, so a weight that is not justified in-line is **silent drift**.
2. **Comparability-boundary construction.** Every published anchor names (a) the peer set it was
   drawn from, (b) the comparators **excluded** and the reason — `P11`, loss-making, `PARTIAL`
   coverage, or non-disclosure — and (c) the downstream names permitted to price off it. This is
   where `peer-bench` and `comps` deploy, and comps are used **only here**: the constitution makes
   them a **cross-check**, never primary, and at the consolidated line SPCX is a pre-profit issuer.
3. **The DCF admissibility gate — run, and it fails on the FORWARD limb only. Amended at round 3.**
   The constitution admits DCF only with **≥3 years of positive FCF** *or* **a contracted backlog
   covering the forecast period**. SPCX fails the FCF limb: H1 2026 operating cash flow
   **+$3,466M** against investing **$(34,487)M**. The backlog limb is available **at the Space
   segment only**, where Launch and Development contracts run **1–14 years**, and it is
   unquantified (V-7).

   **The gate distinguishes FORWARD from REVERSE, and round 3 added the distinction because the
   old text barred both.** A **forward** DCF forecasts cash flows and discounts them to a present
   value — that requires the ≥3-years-of-positive-FCF history the gate exists to demand, and it
   remains **barred**: `dcf` is still deliberately absent from §3, and a consolidated forward DCF
   stays barred outright. A **reverse** DCF does the opposite — it takes an **observed price** as
   given and solves for the growth or margin the market is implying. It needs no positive-FCF
   history, because it forecasts nothing; it reads the price back. **`reverse-dcf` therefore enters
   §3 at the `late` stage** (its registry stage), and it is the only DCF-shaped instrument admitted.

   **Its status is a constraint, not a licence.** It is a **cross-check on the three regimes**, in
   the same class as `comps` — never primary, and its output is *"what the live price implies"*,
   not *"what SPCX is worth"*. Where its implied growth is absurd on its face, that is a **finding
   about the price**, reported as such. **A forward DCF on Space may still be commissioned after
   V-7 resolves**; commissioning one before the gate passes would violate the constitution's own
   sequencing.
4. **Component identity, in-line, always.** Per **DA-23**, an artifact reading `operating_income`
   shows `gross profit − opex` in-line. The SOTP reads the operating line for all three segments,
   so this applies to every segment table. **`EPS × shares` is not a valid sign test** — it passes
   spuriously on flipped issuers. The **gross-profit bound** (operating income can never exceed
   gross profit, at any sign) is the second detector and is cheap to run here.

**Standing rule — definitional ambiguity.** Per the §1c rule inherited from 001, where a term
admits multiple readings, artifacts report **all** of them, label which is quoted, and treat the
spread as a finding. Four classes bind this thesis directly: **DA-01** (cost bases — A, A′, B, C
are enumerated, never collapsed), **DA-08** (customer vs internal launches), **DA-10**
(Stubscriber/ARPU service-line definition), **DA-11** (IT load vs facility draw), **DA-19**
(common-control recast), **DA-21** (issuer-defined segment boundaries), and **DA-23** (sign).

**Correction policy.** 001's files are **frozen**. Where this thesis invalidates a 001 figure the
correction is recorded in 004 and cross-cited by location — matching 001's own
annotate-don't-rewrite policy. **One exception is inherited rather than created**: 001 itself
recorded that the two `2310` SPCX artifacts **supersede** the `1239` pair, and 004 follows that
ordering wherever they conflict (V-1).

## 2. Universe Definition

**Universe members: one.** A thesis is included as a member only if it receives its own
`artifacts/{ticker}/` output. This thesis sizes no trades, so weights are **analytical effort**,
not positions.

| Ticker | Company | Sector | Weight | Why it is in this thesis |
|---|---|:---:|---|
| SPCX | SpaceX | industrial.aerospace_defense | 100% | **The whole thesis.** Three reportable segments, three multiple regimes, one consolidated loss — the case the constitution's SOTP rule was written for |

**Read-through comparators — NOT universe members.** They receive no `artifacts/{ticker}/`
output of their own; they appear in §3 because read-through effort is spent on them, and they
supply benchmarking inputs consumed **inside** SPCX artifacts. Listed here so the effort is
visible and its limits are explicit.

| Ticker | Company | Sector | Weight | Role — and why it cannot be a universe member |
|---|---|:---:|---|---|
| MSFT | Microsoft | tech.platform_internet | read-through | **AI-segment framing (P3)**. The capex-derived capacity comparator. Compute is a **cost centre inside Intelligent Cloud**, not a segment — so no comparable multiple exists |
| GOOG | Alphabet | tech.platform_internet | read-through | **AI-segment framing (P3)** and the sector's most detailed orbital-compute disclosure (Project Suncatcher). Query as **`GOOG`**, never `GOOGL` |
| NVDA | NVIDIA | tech.semiconductors | read-through | The **silicon** leg of the AI stack. Supplies the capability, reports no compute segment — the read-through is to *feasibility*, never to a multiple |
| VRT | Vertiv | industrial.machinery | read-through | Thermal comparator. Supplies the **DA-11 restatement context that 002 owns** — consumed here, not re-derived |
| IRDM | Iridium Communications | tech.telecom_services | read-through | The **profitable-constellation benchmark** — 66 satellites, licensed L-band, 15.1% operating margin. **A P11 deal security**: its price is a spread, so its **multiple is inadmissible** as a comp (P6) |

**Excluded by design.** The remaining 52 names in the 57-name universe carry no SOTP input. They
enter when a *specific* segment of theirs supplies a comparator — GSAT, RKLB, FLY, ASTS and VSAT
appear in §3 for that reason and for no other — not because they are in the universe. Broadening
§2 would turn this into a second general baseline and repeat 001, which is the failure mode the
program exists to avoid.

## 3. Skill Deployment Matrix

**⚠️ REBUILT AT CLARIFY ROUND 3, 2026-09-19.** The matrix now splits into **what 004 EXECUTES**
and **what 004 CONSUMES from 003**. The reason is arithmetic: **003 is COMPLETE and has already
produced nine SPCX artifacts across nine of this matrix's fourteen rows** — so the old matrix
re-ran work that existed on disk. See round 3.

### 3a. Executed — 7 rows

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|:---:|---|:---:|---|
| sotp-valuation | valuation | Deep | SPCX | **`late`** | **The constitution-mandated primary instrument.** Three regimes, scenario weights, the discount/premium measure against **both** the live quote and the dated print (**P1**, **P6**) |
| reverse-dcf | quantitative-analysis | Standard | SPCX | **`late`** | **Added at round 3.** Solves for the growth rate the live price implies — the price question asked backwards. A cross-check on the three regimes, and the market-implied limb of **P3**'s AI framing |
| revenue-decomp | business-intelligence | Deep | SPCX | none | **Added at round 3 — this is where the depth lives. RESCOPED at round 4.** The cut *inside* each segment, **derived from the filings' own decomposition rather than a pre-declared taxonomy** — the 10-Q/8-K narrative disclosure **and** the XBRL dimensional axes (**P2**, **P3**, **P4**). See the box below |
| comps | models-and-pitches | Light | SPCX, RKLB, FLY, GSAT, IRDM, ASTS, VSAT, MSFT, GOOG, NVDA, VRT | none | **Cross-check only**, per the constitution — and now **priced live**: demonstrates which peer sets remain inadmissible (loss-making, `P11`, `PARTIAL`) even with a quote in hand (**P6**). **The AI framing set (MSFT, GOOG, NVDA, VRT) is carried here**, so those four read-through names are not orphaned universe rows |
| competitive | equity-research-core | Light | SPCX, RKLB, FLY | none | Launch competitive position behind the Space standalone-value test (**P4**); the capital-intensity comparison behind **P5** |
| risk | equity-research-core | Standard | SPCX | none | The funding-structure and dilution analysis (**P5**); **P11** treatment of Cursor (**V-5**); the beta / cost-of-equity input to the scenario weights |
| growth-strategy | equity-research-core | Light | SPCX | none | Capital-allocation narrative against the capex disclosure — data centers named before launch facilities (**P5**) |

> **Stage declaration — registry-faithful, and it is a correction.** Exactly **three** skills in
> the registry carry `market_data_stage: late` — **`sotp-valuation`, `ratio-analysis`,
> `reverse-dcf`** — all quantitative-analysis or models-and-pitches. The old matrix declared
> **`none` on all fourteen rows**, which contradicted the registry on two of them and pinned this
> thesis's primary instrument at the one stage where it could not obtain a price. The two executed
> `late` rows are set accordingly. **`ratio-analysis` is consumed from 003 (see 3b) at 003's
> `none`** — flagged as consequence **FC-1** below.

> #### ⚠️ `revenue-decomp` — the cuts come from the FILINGS, not from this spec
>
> **This row was written wrong at round 3 and corrected at round 4.** It named five Starlink tiers
> — *consumer / enterprise / **aviation** / **maritime** / government*. Checked against 003's
> artifacts, which is the feasibility gate that should have run first: **SPCX files two.**
>
> | Cut | Status | Evidence |
> |---|---|---|
> | Connectivity **Consumer** | ✅ **filed** | `1,721 → 2,485 (+44.4%)`, marked *"segment, filed"*. Carries Starlink Mobile inside it |
> | Connectivity **Enterprise & Government** | ✅ **filed** | `867 → 1,806 (+108.3%)` — **grew 2.4× faster than consumer**, which is the mix-shift evidence **P2** needs |
> | **aviation**, **maritime** | ❌ **not formable** | They appear **twice in all of 003's nine SPCX artifacts**, both times as qualitative prose — *"domains including aviation, maritime, land mobility, fixed sites, and government entities"*. **No revenue figure is attached to either.** Negotiated pricing lives in the managed channel, and that channel is *"disclosed as revenue but **not** as subscribers"* |
> | Subscribers / ARPU by channel | ❌ `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | 003 recorded it: managed enterprise/government is disclosed as revenue but not as subscribers, which is why price erosion cannot be separated from mix shift. `subscribers × ARPU × 3` **does not reproduce** consumer revenue |
>
> **⚠️ `get_segment_data` IS BROKEN — and 003 RECORDED THIS FIRST. Credit where it is due.**
> Round 4 found the breakage independently, but it was **already documented in
> `003/plan.md` § F4**, sourced from **002 §7**, and with a fuller diagnosis than round 4
> produced: the tool *"hard-errors at SPCX (`column "k" does not exist`) and elsewhere reports a
> `total_revenue` summing served facts **across two years and two durations with no
> de-duplication** — `segment_coverage_pct 116.2` **masking a 302.1% overlap**. 002's verdict:
> ***'Treat its output as unusable.'***"* **004's correction is not the discovery; it is that
> 004's spec never carried 003's finding.** The same class of gap as the missing `003 → 004`
> edge itself.
>
> **The working route is `search_xbrl_facts(…, view=detailed)`**, which returns the dimensional
> axes directly. Confirmed present at SPCX: `srt:ConsolidationItemsAxis`,
> `us-gaap:StatementBusinessSegmentsAxis` (`spcx:SpaceMember` / `spcx:ConnectivityMember` /
> `spcx:AIMember`), `srt:MajorCustomersAxis`, `us-gaap:StatementEquityComponentsAxis`,
> `us-gaap:AntidilutiveSecurities…Axis`, `us-gaap:DebtInstrumentAxis` / `LongtermDebtTypeAxis`,
> `srt:RangeAxis`. **The row therefore declares a method, not a taxonomy: discover the cuts from
> what the filer actually reports, and record each cut found as either `formable` or one of the
> named disposition classes.** Pre-declaring a five-way split the filer does not use is the F1
> failure of round 1 repeating inside this thesis's own method.

### 3b. Consumed from 003 — 9 rows, NOT re-run

These skills were executed by 003 on SPCX and their artifacts exist on disk. 004 **cites them and
does not repeat them.** `Subscribed` pairs in §1b resolve here as well as to 3a.

**⚠️ THIS TABLE MUST NOT USE 3a's COLUMN SHAPE, and getting that wrong cost a round.**
`tools/tasks_md.py` parses matrix rows with
`^\| ([a-z-]+) \| [a-z-]+ \| (\w+) \| ([^|]+) \|` — **positionally, with no knowledge of which
block a row sits in.** A consumed row in 3a's shape is therefore read as *work to dispatch*, and
the generator emits tasks for it. Measured on the first run: **33 matrix pairs → 63 tasks**, of
which `secular-trends` alone contributed **12**. **That defeats the entire consume decision.**

**A different column shape is the mechanism that makes "consumed" mean consumed.** This one puts
the 003 artifact path in the second cell, which cannot match `[a-z-]+`, so `MATRIX_ROW` skips
every row here while a human reads it normally.

| Skill | 003 artifact consumed (SPCX) | 004 uses it as | 003's stage |
|---|---|---|---|
| business-model | `003/artifacts/SPCX/2026-09-19_1315_business-model_methodology.md` | The filed segment boundaries and DA-21 restatement. **004 goes inside them** via `revenue-decomp` | none |
| unit-economics | `003/artifacts/SPCX/2026-09-19_1200_unit-economics_methodology.md` | Segment-level unit economics. The cohort cut is 004's `revenue-decomp` | none |
| operational-kpi | `003/artifacts/SPCX/2026-09-19_1215_operational-kpi_methodology.md` | Segment revenue, operating result, the DA-08 internal/customer split, the in-line DA-23 derivation | none |
| recent-quarter | `003/artifacts/SPCX/2026-09-19_1415_recent-quarter_methodology.md` | The quarterly segment series and the entity-boundary tagging (**V-4**) | none |
| ratio-analysis | `003/artifacts/SPCX/2026-09-19_1445_ratio-analysis_methodology.md` | The coverage ratio for the capital claim (**P5**) — price-independent, so `none` is apt. **See FC-1** | none |
| peer-bench | `003/artifacts/SPCX/2026-09-19_1615_peer-bench_methodology.md` | The vehicle and margin benchmark. **See FC-2** — 004's framing set is a *different* ticker set | none |
| sector-overview | `003/artifacts/SPCX/2026-09-19_1345_sector-overview_methodology.md` | Places the anchor in the Sector Preferences table (**P6**) | none |
| secular-trends | `003/artifacts/SPCX/2026-09-19_1345_secular-trends_methodology.md` | The terrestrial-compute capacity trend the AI framing is bounded against (**P3**) | none |
| what-if | `003/artifacts/SPCX/2026-09-19_1230_what-if_methodology.md` | Scenario construction and the DA-10 mix-shift sensitivity (**P2**, **P3**) | none |

> **⚠️ THE TWO TOOLS' CONTRACTS CONFLICT, AND THIS IS THE WORKAROUND.**
>
> | Tool | Wants | If violated |
> |---|---|---|
> | `plan_audit.py` **I2** | every `TICKER × skill` in a `**Subscribed**` line to **appear in the matrix** | reports *"generates ZERO tasks"* — reads as a gap |
> | `tasks_md.py` | every matrix row in 3a's shape to be **dispatched work** | emits tasks for consumed rows |
>
> **They pull in opposite directions for a consume-from-upstream design, and there is no shape
> that satisfies both.** Round 3 tried, and broke `tasks_md`. **The resolution is to stop asking
> one artifact to do both jobs:**
> 1. **3b uses a non-matrix shape** (this table) so `tasks_md` ignores it.
> 2. **The `Subscribed` lines name only EXECUTED skills**, so `plan_audit` I2 has nothing to
>    complain about. Each pillar gains a separate **`Consumes (003)`** line — a field neither
>    tool parses, so the information survives without being dispatched.
>
> **This is a third missing check, alongside I5 and I6** (see plan.md): *neither tool knows what a
> "consumed" row is*, because the concept was introduced by this thesis. `plan_audit` I2 and
> `tasks_md` both assume every named pair is work.

> **Read-through coverage.** The §2 read-through names **MSFT, GOOG, NVDA, VRT** are carried by
> 3a's `comps` row (all four). **`VRT` appears only in `comps`** — if that row narrows, VRT
> becomes an orphaned universe row, which is what invariant I1 exists to catch.

> **Two consequences of the consume decision, flagged rather than silently resolved.**
>
> - **FC-1 — `ratio-analysis` is registry-`late` but consumed at 003's `none`.** The coverage
>   ratio needs no price, so this is defensible. **But 003 itself declared `none` where the
>   registry says `late`** — the same class of mismatch this round corrected in 004. If 004 wants
>   price-stamped ratios (P/CF, EV/EBITDA) for the anchor, `ratio-analysis` moves to **3a at
>   `late`**, **+1 task**.
> - **FC-2 — `peer-bench` is consumed, but the ticker sets differ.** 003 ran it on
>   **SPCX, RKLB, FLY**; 004's purpose is the AI framing set — **MSFT, GOOG, NVDA, VRT, IRDM** —
>   which 003 never benchmarked. If the AI framing set must be benchmarked rather than read
>   across, `peer-bench` moves to **3a**, **+1 task**.

> **Coverage invariant — restated for the split.** Every universe member in §2 appears at least
> once across 3a and 3b; every `Subscribed` pair in §1b resolves to a row in **either** block;
> every row in either block is named in at least one `Subscribed` line. Read-through tickers
> generate **no** per-ticker artifacts. Verified by `tools/plan_audit.py` (I1–I4), which must be
> re-run against the two-block shape.

## 4. Depth Tiers

**Rebuilt at round 3. Tiers now describe EXECUTED rows only** — the nine consumed from 003 carry no
tier here, because 004 does not run them.

| Tier | Skills | mode-set | Tickers | Output |
|:---:|------|---|--------|------|
| Deep | **sotp-valuation**, **revenue-decomp** | all modes | SPCX | The valuation and the cut inside each segment — the two rows carrying P1–P4 |
| Standard | **reverse-dcf**, risk | essentials_modes | SPCX | The market-implied growth rate and the funding/dilution analysis |
| Light | comps, competitive, growth-strategy | essentials_modes | As listed | The boundary-setting checks that make P6 publishable |

**Budget note — materially changed in each direction at round 3.**

- **Down.** Nine rows moved to §3b as consumed, so they generate **no tasks**: the old estimate of
  **~34 tasks** was inflated by exactly the work 003 had already done. This is the largest single
  reduction this thesis has had.
- **Up.** Two rows were added — `revenue-decomp` (the depth row) and `reverse-dcf` — and each
  executed row now carries a market-data obligation (a quote fetch, a stamped series, or a
  refusal recorded) that the old `none`-everywhere matrix did not price. §5's three unlocks add
  beta estimation and event-window studies.
- **Net: the direction is down, but the final figure is `agentii:tasks`'s to compute**, not this
  spec's. `max_tasks: 40` is retained as the ceiling. If it must come down further, **drop the
  Light rows first** — never the Deep rows, which carry P1–P4.
- **FC-1 and FC-2 (see §3b)** are each **+1 task** if resolved toward execution. Both are recorded
  open, so the budget must be read as a band, not a point.

## 5. Cross-Cutting Analysis

- **The anchor table** is the cross-cutting output: one row per segment, each with its multiple
  regime, grade, source, and comparability boundary. This is what 005–009 cite.
- **The discount decomposition.** The gap between SOTP value and the market is
  reported as **three named components** — conglomerate discount, control/float discount, and
  unallocated corporate cost — and where a component cannot be separated from another, that is
  **reported as a finding**, not allocated arbitrarily. A single blended "discount" figure is a
  P6 violation.

  **Basis carried in-line (A-11, applied at plan time 2026-09-19).** Two things the decomposition
  must now state on its face, because round 4 changed both and neither had propagated here:

  1. **The headline is PRO-FORMA.** Cursor is inside the SOTP, so its $60B consideration and
     dilution are inside the denominator of every discount figure. **A discount computed on a
     pre-close value against a market price that already reflects the deal compares two different
     companies** — which is exactly the failure Q-6 exists to prevent. **V-5 is `blocking` for
     this reason**: the decomposition cannot be computed without the dilution.
  2. **The market side has two bases, not one.** The gap is reported against **both** the live
     quote (**$152.71**, close 2026-09-18, source nasdaq) and the constitution's dated print
     (**~$1.62T**, struck against `$135.00`, 2026-06) — **and the spread between the two discount
     figures is itself a named component**, because the price-base gap — the anchor's implied
     **$119.41** pro-forma against a live **$152.71**, i.e. **+27.9%** — is not a
     conglomerate discount and must not be silently attributed to one.

  **⚠️ The control/float component is now materially harder.** Pro-forma, the Cursor
  consideration is **Class A stock**, and the single-class control structure determines who can
  price that dilution (P5). So the control/float component is no longer a discount *on* the
  anchor — it is partly a discount *created by* the transaction the anchor now includes. Where
  the two cannot be separated, **that is the finding.**
- **Price-input discipline — rewritten at round 3, 2026-09-19.** The old text read *"Market Data
  Stage is `none`… no correlation, beta or relative-multiple regression against live prices is
  run."* **That was a declaration, and it was wrong.** `data-tools/market_data.py` serves a
  **keyless NASDAQ** quote (measured OK; `_sources.py` registers `{"name": "nasdaq", "auth":
  "none"}`), and `live_snapshot.py` already names **SPCX** among its target tickers. Verified
  live on 2026-09-19: **SPCX $152.71, close 2026-09-18**, 3,759 ms.

  **Two bases, both printed, and the spread between them is a finding.** Round 3's answer was
  *"both — live and dated, with the spread reported"*, and the reason is that they answer
  different questions. The **live quote** is the market fact and is stamped with its observation
  time and its source. The **constitution's ~$1.62T** anchor, struck against `$135.00` in
  2026-06, is the programme's **sanctioned governance reference** and is what 001–003 are
  comparable to — all three are print-based and carry no prices at all. **At $152.71 the live quote is +27.9% above the anchor's own implied $119.41 pro-forma**, and
  that gap is itself reported rather than resolved. **⚠️ Corrected 2026-09-19:** an earlier draft
  put this at ~13.1%, which compared the live price to the **IPO price** (`$135.00`) rather than to
  the anchor — same two prices, different denominator. **The anchor is ~28% behind, not ~13%.**
  **Every market-referenced figure carries its basis *and* its stamp in-line** — a figure quoted
  without saying which of the two it is on is not admissible.

  **What live data unlocks — three, and no more.** §5's old bar is lifted to exactly these:
  1. **Beta / cost of equity**, feeding P5's scenario weights directly. §5 already calls macro
     sensitivity *"high"* and makes the 10Y the scenario-weight input; beta is the other half of
     that estimate and was previously unavailable.
  2. **Live comps multiples**, so P6's comparability boundaries rest on **measured** multiples
     rather than on the assertion that no admissible comparable exists. **The constraint
     survives the data**: IRDM and GSAT are P11 deal securities, so their *prices still track
     spreads*, and a live multiple on a spread is no more admissible than a stale one. Live data
     makes the boundary **verifiable**; it does not make it disappear.
  3. **Event-window price reactions** — the studies 001 and 003 could not run: SATS's $16.48bn
     impairment triggered by the AT&T/SpaceX transactions, the xAI merger, the Cursor
     announcement. Each becomes a measured reaction rather than a named event.

  **Still barred:** a relative-multiple regression of SPCX **against live prices** as a valuation
  method. The constitution makes comps a cross-check and never primary; live data does not
  promote them.
- **Macro sensitivity: high.** SPCX is the longest-duration asset in the universe and the regime
  is hostile to duration — 10Y at 4.80%, 30Y at 5.26%, both at three-year highs, with hike risk
  priced. The constitution's **NEUTRAL** bias and its re-rate triggers (10Y > 5.25%, or a Fed
  pivot to cuts) are the **scenario-weight inputs** for P5's capital claim, not background.
- **Constitution interaction**: **A1b** (falsified — the SOTP must show value migrating out of
  launch, not assert it); **A4 / P10** (the AI segment's admissibility ceiling); **P3** (one
  binding constraint, `CAPITAL` — see Q-4); **P4** and the Data-Integrity Register (DA-23
  in-line, `EPS × shares` barred); **P11** (Cursor); **Risk Framework** (the 40% theme cap binds
  before the 25% sub-sector cap in a single-theme book, and SPCX is the largest single-theme
  exposure available).
- **Pair-trade candidates**: none produced here. This thesis produces the anchor and no positions.

## 6. Output Contract

- **Per-ticker (dispatcher-resumable)**: `artifacts/SPCX/{YYYY-MM-DD}_{skill}_{mode}.md` — the
  suffix **must** be `_{skill}_{mode}.md` with the real mode slug, so `dispatch.resume_verdict()`
  can find it.
- **⚠️ READ-THROUGH ROWS FILE UNDER SPCX — amended at plan time 2026-09-19.** `comps` names
  **11 tickers** and `competitive` names **3**, but §2 states read-through comparators *"receive
  no `artifacts/{ticker}/` output of their own"* — their effort is *"consumed **inside** SPCX
  artifacts."* So a read-through ticker in a matrix row **declares which tickers' data is READ,
  not where the artifact is WRITTEN.** The artifact is **one per `(skill, mode)`, filed under
  SPCX**, with `SPCX` in the path regardless of which comparator supplied the input.

  > **This is not stylistic — the resume mechanism depends on it.** `dispatch.resume_verdict()`
  > computes `root = thesis_dir / "artifacts" / ticker`, then globs for `*_{skill}_{mode}.md`.
  > Called with `ticker="RKLB"`, it looks in `artifacts/RKLB/` — **a directory §2 says must never
  > exist.** It finds nothing and returns **`"run"` on every dispatch, forever.** The eleven
  > `comps` tasks would re-execute in perpetuity, and creating `artifacts/RKLB/` to satisfy them
  > would violate §2's invariant and give a read-through a per-ticker artifact the spec forbids.
  >
  > **Dispatch rule, and it must be followed or those tasks never resume: call
  > `resume_verdict()` with `ticker="SPCX"` for every read-through row.** For `comps` that means
  > **11 generated tasks collapse to 1 artifact**; for `competitive`, **9 collapse to 3** (its
  > three modes, since SPCX is a genuine member). See the plan's phase crosswalk.
- **Cross-cutting (not resume-tracked)**: `_cross/{name}.md`.
- **Primary artifact**: `_cross/anchor-sotp.md` — the three-regime anchor table with grades,
  sources and comparability boundaries, plus the scenario weights and the discount decomposition.
  This is what 005–009 cite. **Amended at rounds 2 and 3**: each row names **which downstream
  theses may price off it** — **005, 006 and 009**, not 005 alone, because 004 is the programme's
  only valuation of SPCX's Connectivity and AI segments — and the discount is published against
  **both price bases** (live quote + the dated constitution print) with the spread reported.
- **Secondary artifact**: `_cross/segment-attribution-ledger.md` — the V-1 … V-7 validation queue
  with each item's disposition. Read-through tickers contribute **inputs only** and receive no
  per-ticker artifact of their own.
- **Price stamp — mandatory on every market-referenced figure (round 3).** Each carries its
  **basis** (live quote, or the dated constitution print) **and** its observation time **and** its
  source. A figure quoted without all three is not admissible. Where the feed **refuses**, the
  refusal is recorded with equal fidelity — `live_snapshot.py`'s own design principle: *"when the
  provider is rate-limited or blocked, the absence is the finding."*
- **Consumed-input citation (round 3).** Where an artifact uses 003's curve, map, or any of the
  nine consumed SPCX analyses, it cites the **003 artifact path and its basis**, per 002's rule
  that *"a downstream thesis citing a validated set must carry the basis as well as the grade."*
  A consumed figure quoted without its path is not traceable and is not admissible.
- Snapshot: `snapshots/004-tier0-spacex-anchor/{YYYY-MM-DD}_thesis.md`
- **Frontmatter**: per `contracts/artifact-frontmatter.yaml`, with `thesis_id:
  "004-tier0-spacex-anchor"`. All five pins are mandatory: `constitution_pin: 1.5.0`
  (**re-pinned at clarify round 2, 2026-09-19** — was `1.4.0`),
  `assumption_pin: "2"`, `skill_pin`, `as_of`, `corpus_version`.

## 7. Thesis Phases

**Rebuilt at round 3.** Phase 0 is new and is the consume edge; Phase 2 is new and is the depth
row; the old phases are otherwise retained but now **read 003 rather than re-derive.**

| Phase | Tasks | Duration | Dependencies |
|:---:|------|:---:|------|
| **0 — Consume 003** (new) | Read `003/_cross/launch-cost-curve.md` and `003/_cross/value-pool-map.md`; index the **nine consumed SPCX artifacts** in §3b; **capture the live quote** and stamp it | Week 1 | 003 **COMPLETE**; Constitution **v1.5.0** loaded (corrected at round 2 — the line read v1.3.0) |
| 1 — Separability (P1) | Read the segment note; **confirm** V-1 (already RESOLVED — read it as a given, do not re-litigate); run `segments_sum_to_total` in-line; build the segment-attribution ledger | Week 1 | Phase 0 |
| **2 — Granularity** (new — P2, P3, P4) | **`revenue-decomp`**: the cut *inside* each segment — Starlink by tier, Falcon vs Starship, Grok vs X-advertising vs compute. This is the phase that makes the multiples defensible rather than segment-level | Week 2 | Phase 1 |
| 3 — Connectivity (P2) | ARPU/subscriber/margin series **on the cohort cut from Phase 2**; all **DA-10** readings side by side; the price-erosion vs mix-shift test | Week 2 | Phase 2 |
| 4 — AI admissibility (P3) | Test framings (a) comparable, (b) invested capital, (c) optionality incl. zero; the MSFT/GOOG/NVDA framing set; apply the A4/P10 ceiling; **consume** 002's DA-11 restatement; the **market-implied limb** from `reverse-dcf` | Week 3 | Phase 3 |
| 5 — Space standalone (P4) | Ex-R&D margin; the Starship/Falcon R&D split labelled `MODELED`; **DA-08** internal-transfer limitation; **DA-01** A/A′/B/C restatement; **carry DA-06 as a stated non-comparability limitation** (round 3) | Week 3 | Phase 2 |
| 6 — Capital (P5) | Coverage ratio; funding structure and **Cursor/P11** dilution; control and float; index-inclusion catalyst datability; **beta / cost of equity from live data** | Week 4 | Phase 3 |
| 7 — SOTP (P1, P6) | Scenario weights with in-line justification; three regimes; **the PRO-FORMA basis stated on the headline, with V-5's dilution resolved first**; the discount decomposition **against both price bases, with the spread between them named as its own component**; `reverse-dcf` as cross-check; event-window studies | Weeks 5–6 | Phases 1–6, **and V-5** |
| 8 — Hand-off (P6) | Publish `_cross/anchor-sotp.md` with boundaries naming **005, 006 and 009**; record what could not be valued | Week 6 | Phase 7 |

## Clarifications

Recorded by `agentii.specify` at creation, 2026-09-18. No `agentii.clarify` round has run; the
following are recorded as open for that pass.

- **Q-1 (P1, price admissibility under Market Data Stage `none`)** — Is the constitution's
  **~$1.62T** anchor admissible as the market comparator when it cannot be refreshed?
  **Provisional answer, pending clarify:** admissible, but **only as a dated print with its date
  printed in-line**, and never described as a current price. A discount quoted against an
  undated market cap is not a finding.
- **Q-2 (P3, the AI framing)** — When no comparable exists, is the honest headline **(a)** zero,
  **(b)** invested capital, or **(c)** an interval from a terrestrial compute comp set admitted
  to be non-comparable? **Provisional:** evaluate all three, report all three per the §1c
  standing rule, and name which one the SOTP headline uses. A segment carried at zero is a
  legitimate output; an unstated choice is not.
- **Q-3 (P4, revenue basis vs capacity basis)** — Should the Space multiple sit on **revenue** or
  on **capacity** (mass to orbit / launches)? They are different businesses: revenue reflects
  customer activity only (**10 of 37** launches), while capacity includes the **27 internal
  launches that generate no inter-segment revenue**. **Provisional:** revenue for the multiple,
  capacity reported as a separate disclosure, and the internal-transfer limitation carried as a
  finding rather than netted.
- **Q-4 (P5, `CAPITAL` vs `POWER`)** — PROGRAM names `CAPITAL` as 004's binding constraint, but
  the AI segment's *business* is bounded by `POWER` (F1/F2). Is `CAPITAL` correctly named?
  **Provisional:** `CAPITAL` holds, because SPCX's AI segment is **terrestrial** and F1/F2 bound
  *orbital* compute — the physical constraints bind a business SPCX is not in. Flagged for human
  confirmation; **if answered differently this is a PATCH to spec, not a MAJOR event.**
- **Q-5 (P6, boundary shape)** — Is a comparability boundary a **partition** (a name is in or
  out) or a **graded score**? **Provisional:** partition, with the excluded class named and the
  reason recorded — `P11`, loss-making, `PARTIAL` coverage, or non-disclosure. A graded score
  invites the downstream thesis to pick its own threshold, which is the failure P6 exists to stop.
- **Q-6 (P1/P5, Cursor)** — Under **P11**, is the headline SOTP **pre-close** (excluding Cursor)
  or **pro-forma** (including the $60B all-stock consideration and its dilution)?
  **Provisional:** pre-close headline, with a pro-forma sensitivity reported separately, because
  the consideration is Class A stock whose dilution is not determinable from the pages read
  (**V-5**).
- **Q-7 (all pillars, 002 dependency)** — Where 002 has not landed, does 004 inherit 001's grades
  unchanged, or wait? **Provisional:** inherit and **label**, per the §1c standing rule. Waiting
  would idle the anchor behind a foundation thesis; inheriting silently is the drift P4 bars. The
  label is the whole remedy.

---

### Clarify round 1 — 2026-09-18 · **RE-CENTRING: SpaceX as the ecosystem keystone**

Owner instruction: *"spacex 作为体量最大的上市 space tech 公司，是整个板块的压舱石。本 thesis 需要把
spacex 作为中心，挖掘 space tech 整个生态下，spacex 的核心… 搜索 agentii 知识库里面的 strategies
cases… 构建一个两个分析 spacex 的框架（包括 spacex 在生态中的相互作用）"*

**Status of Q-1 … Q-7: UNCHANGED and still open.** This round is **orthogonal** to them — it
re-centres the thesis rather than resolving the existing questions. All seven provisional
readings stand as recorded.

#### Answer 1 — Framing: **two legs.** The ecosystem framework determines *where value sits*; the SOTP is its **valuation leg**.

The six existing pillars are **re-ranked, not deleted**:

| Pillar | Was | Becomes |
|---|---|---|
| **P2 Connectivity** | P2, second | **MAIN LINE** — the leg the framework predicts value settles in |
| **P3 AI** | P3, carry at cost | **Contested** — the framework must say whether AI is the platform or a distraction from it |
| **P4 Space** | P4, public good | **DEMOTED to "the unpriced input"** — §1's own finding: 27 of 37 Falcon launches are internal and produce no inter-segment revenue |
| **P1 / P5 / P6** | SOTP build, CAPITAL, boundaries | **Retained as the valuation leg's mechanics** |

#### Answer 2 — Frameworks: **all three**, and they are a STACK, not three legs.

The owner selected all three. They answer **different questions** and must be sequenced, or the
thesis will hold three unranked lenses and inherit 003's two-sections-disagree failure:

| # | Framework | Corpus ID | Answers | Yields |
|---|---|---|---|---|
| **F1** | **ARK Wright's Law & S-Curve Innovation Valuation** | `ark_invest__wrights_law_valuation_framework` (+ `ark_invest__innovation_disruption_investing`) | **Does SpaceX qualify as a cost-curve disruptor at all?** | **COMPUTABLE SCREENS** — see below |
| **F2** | **a16z Platform-Shift & Network-Effect Moats** | `a16z__platform_shift_network_effects` (+ `a16z__core_venture_methodology`) | **Which layer does SpaceX own by default?** | The **ecosystem keystone** map — the owner's stated centre |
| **F3** | **Platform Technology Monetisation via Licensing** | `med_bio-red-dividend__platform-technology-monetization-via-licensing` | **Does the platform owner capture more than the end-product developer?** | The **A1b test** — who captures the stack |

**⚠️ F1 supplies the falsifiable screens, and they are unusually concrete.** From the corpus,
verbatim selection criteria — each is checkable against 003's cost curve and SPCX's filings:

- **Wright's Law learning rate sustained for ≥5 cumulative production doublings.** *(Is launch
  there? A doubling is a 50% cost cut; five is ~97%. This is computable and it is the single
  sharpest question in the thesis.)*
- **S-curve position: sub-20% penetration.**
- **TAM >$1T at the cost-curve endpoint.**
- **"Platform-orchestrator characteristics (data network effects, scale advantages)."**
- **Red flags, verbatim: "learning rate decay below 10–15%, demand saturation stalling the
  S-curve, or substitution by a new technology with a steeper learning curve."**
- **A hard risk rule that is directly usable: *"If a learning rate falls below the model's
  predicted bound for two consecutive doublings, the position is reduced by ~1/3."***
- **Terminal value capped at 50–70% of total EV.**

**Closest case, and it is a strong one:** `ic_ark_tesla_valuation_2018_2023` — a traditional DCF
valued Tesla at **$150** while ARK's probability-weighted framework said **~$800**; Tesla reached
a **$745.44** pre-split equivalent by end-2023. The case's own lesson, verbatim: *"point-estimate
DCF structurally undervalues disruptive innovation when growth, margins, and TAM follow non-linear
S-curves."* Also available: `ic_ark_ev_adoption_prediction_2017_2023`,
`ic_ark_ai_training_cost_collapse_prediction_2020_2024`, `ic_ark_dna_sequencing_at_100_prediction_2014_2023`.

> #### ⚠️ FEASIBILITY CHECK ON F1's SCREENS — **they are NOT evaluable on this workspace's data.** Run at clarify round 1, 2026-09-18, and recorded BEFORE the screens are built into a pillar.
>
> **Wright's Law requires a learning rate fit to `cost per unit vs CUMULATIVE PRODUCTION`. Neither axis exists here, and the one that does is contaminated.**
>
> | Input the screen needs | What the workspace actually holds | Verdict |
> |---|---|---|
> | **A `$/kg` time series** | SPCX's unit-economics artifacts (001 and 002) carry **2026 (×50) and 2025 (×11) and nothing earlier.** A **point estimate across four DA-01 bases**, not a series | **ABSENT** |
> | **A cumulative-production series** | The only cumulative figure in reach is RKLB's *"87 successful missions … **including suborbital launches**"* — which **DA-08 already flagged as a mixed orbital+suborbital basis** | **PRESENT BUT BASIS-CONTAMINATED** |
>
> **So the screen "learning rate sustained for ≥5 cumulative production doublings" cannot be computed — the numerator has one year and the denominator mixes two populations.** A learning-rate fit needs several doublings *of cumulative production* against cost; five doublings is a 32× volume range, and the workspace holds a 2025→2026 window.
>
> **⚠️ THIS IS 002's F2 FINDING REPEATING, AND IT SHOULD BE TREATED THE SAME WAY.** 002 found the orbital-compute constants were not reproducible, **downgraded F2 to a qualitative bound**, and recorded the disposition as `UNRESOLVABLE-FROM-PLATFORM` with a named resolver. **F1's screens take the same disposition.** Historical launch prices are additionally `UNRESOLVABLE-FROM-PUBLIC-SOURCES` in part — SPCX is private and did not publish a systematic price history.
>
> **What SURVIVES from F1, and it is the more useful half:**
> - **The valuation METHOD** — probability-weighted bear/base/bull replacing point-estimate DCF, **with terminal value capped at 50–70% of total EV**, and a stated **15–25% required return (target IRR, not WACC)**. **This is directly usable and needs no learning rate.** It is also the piece 004 most needs, because §1 established that both a consolidated DCF and comps are *inadmissible* — F1 supplies a third admissible path.
> - **The platform-orchestrator criterion** (*"data network effects, scale advantages"*) — **a qualitative screen, and the falsifier for this thesis's main line.**
> - **The red-flag language** — *"learning rate decay"*, *"demand saturation stalling the S-curve"* — usable as **named risks**, not as measured triggers.
> - **The cases**, which are evaluated on their own facts and do not inherit the screen's data problem.
>
> **What DOES NOT survive:** the numeric triggers — *"≥5 cumulative doublings"*, *"sub-20% penetration"*, *"learning rate below the model's predicted bound for two consecutive doublings → reduce ~1/3"*. **A numeric trigger that cannot be computed is not a risk control; recording it as one would be the DA-29 failure inside this thesis's own method.** If a learning rate is ever to be fitted, it needs a **named external source for historical launch prices and cumulative counts** — the resolver, stated per the disposition rule.
>
> **Consequence for the spec.** **F1 enters as a *method and a criterion*, not as a *screen with thresholds*.** Its thresholds are recorded `UNRESOLVABLE-FROM-PLATFORM` with the resolver named — **not silently deleted, and not asserted.** *(Unchanged: F2 and F3 are qualitative moat frameworks and are unaffected.)*

**F2 supplies the founder variable, and the corpus has the right cases:** `ic_jeff_bezos_as_amazon_founder_ceo_for_27_years`,
`ic_mark_zuckerberg_as_meta_founder_ceo_through_existential_cris`, `ic_brian_chesky_as_airbnb_founder_ceo_through_pandemic_near_dea`,
`ic_reed_hastings_as_netflix_founder_ceo_through_dvd_to_streamin`, plus `ic_netscape_ipo_1995` and
`ic_netscape_vs_microsoft_browser_war_1995_1999`.

#### Answer 3 — Ecosystem scope: **all four dimensions**, mapped explicitly.

| Dimension | The question | Known hooks already in hand |
|---|---|---|
| **Vertical — suppliers + customers** | Who SpaceX depends on, and who depends on it | 27/37 internal launches; **cost capitalised into satellites in PP&E**; the Tier 3b supplier exposure (008's subject) |
| **Horizontal — competition and foreclosure** | Who SpaceX forecloses | A1b falsified; **SATS's $16.48bn impairment triggered by the AT&T/SpaceX transactions**; ASTS/Ligado; Amazon Leo |
| **Capital — who funds it, whom it funds** | The CAPITAL constraint, both directions | Cursor ~$60bn all-stock (P11, Q-6 open); the xAI merger 2026-02-02; the EchoStar spectrum transaction; post-IPO equity **2,573 → 127,224 (49.5×)** |
| **People — Musk as a single-point variable** | Founder-key-person risk and attention allocation | **⚠️ NO CORPUS CASE EXISTS** — `search_investment_cases("Musk")` returns **zero**. This leg must be **self-built** and needs a stated method. |

#### Answer 4 — Central thesis: **the causal chain, both halves.**

> **Keystone is the MECHANISM. "Value is not in the disruption" is the CONCLUSION.**

**⚠️ Three independent lines already converge on the conclusion, which is why it is worth
making the thesis's spine:**

1. **001's A1b** — falsified: value migrated *out of* launch.
2. **004's own §1** — 27 of 37 Falcon launches are internal, produce no inter-segment revenue, and
   are capitalised into Connectivity's PP&E. **Space is an unpriced input to the thing that earns.**
3. **ARK's own criterion (F1)** — value accrues to the *platform-orchestrator with data network
   effects*. **Launch has no network effects. Starlink does.**

**Three unrelated methods, one answer.** The thesis's job is to test whether the chain holds, not
to assert it. **The falsifier follows from F1 directly:** if launch *does* satisfy the
platform-orchestrator criterion — network effects, data advantages, switching costs — the
conclusion fails and the SOTP should centre Space instead of Connectivity.

#### ⚠️ Corpus retrieval — a finding that EXTENDS `PROGRAM.md` §4

**§4 records that sector-keyed retrieval returns zero, and it does — `search_investment_cases`
on `"space satellite launch rocket"` returns 0 rows, and `list_domains` carries
`applicable_sectors: ["med","tech","fin"]` with no industrial or aerospace domain anywhere.**
**That finding stands.** But this round found the corpus is **far richer by situation than §4
implies**: three complete, operational frameworks and a deep case set, all filed under
tech/innovation rather than space. **§4's conclusion — retrieve by structural situation — is
correct and this round is its strongest evidence.** What §4 understated is **how much is there**:
it listed analogues at the rate of one per row, and the ARK and a16z clusters alone supply
**six strategies and twenty-plus cases**, several with fully-populated `body` blocks containing
selection criteria, position sizing, exit rules and risk limits.

**⚠️ `search_by_analogue` by `company_situation` is itself a dead end** — `company_situation=category_creation`
returned 0 cases and 0 strategies, and the `analogue_tags` on nearly every row are **empty
arrays**. Retrieval must use **full-text `search`**, `practitioner`, `investment_style`, or
`domain`. Recorded so 011 does not repeat the query shape that fails.

#### New open questions this round creates — **Q-8 … Q-11**

- **Q-8 (F1 vs the SOTP — the frameworks are operationally OPPOSED).** ARK's risk rule is *"no
  stop-losses, no VaR, hold through 30–50% drawdowns, exit only on thesis break or bull-case EV."*
  The SOTP is a **valuation anchor that trims when price approaches base-case EV.** **Both cannot
  be primary.** *Provisional:* the frameworks govern **entry and holding**; the SOTP governs
  **what to pay** — and where they conflict, **the conflict is reported rather than resolved**,
  per the §1c no-single-basis-collapse rule.
- **Q-9 (F3's migration distance).** `med_bio-red-dividend__platform-technology-monetization-via-licensing`
  is a **medicine-domain** strategy. Transferring it to launch-vs-payload is a **structural**
  analogy, not a sector one. *Provisional:* admit it, grade the migration `MODELED`, and state
  what would make it inapplicable.
- **Q-10 (the People leg has no corpus support).** `search_investment_cases("Musk")` = 0. The
  founder-CEO crisis cases (Bezos, Zuckerberg, Chesky, Hastings) are **structural analogues with
  a different operator.** *Provisional:* use them as the method, and record Musk-specific claims
  as `CLAIMED` — **no artifact may grade a Musk-behaviour claim `DEMONSTRATED` from the corpus.**
- **Q-11 (does the re-centring change the binding constraint?) — this one is load-bearing.**
  PROGRAM.md names **`CAPITAL`** as 004's binding constraint, and Q-4 provisionally confirmed it.
  **But the re-centred thesis is about *where value settles*, and F1's criterion is a
  *technology* screen (learning rate, penetration) while F2's is a *moat* screen (network
  effects, default status).** Neither is a capital screen. *Provisional:* `CAPITAL` still binds
  the **valuation leg** (P5), but the **main line's** binding constraint is likely **`MOAT`** or
  **`NETWORK_EFFECT`** — and if so this is a **MINOR** amendment, not a PATCH, because it adds a
  constraint rather than rewording one.

---

### Clarify round 2 — 2026-09-19 · **THE LAYERING: 004 is the programme's valuation layer**

Owner instruction, verbatim: *"004 和003 什么关系，所有的 theses 应该是递进的，一层一层深入的，001 是浅层
调研构建全景图，002 是对 001 做了 validation，003 围绕 spacex 和发射构建 / 004 应该是怎样更进一步和覆盖其他板块"*

The owner rejected round 2's opening framing (framework ownership) as the wrong question and
substituted a **programme-architecture** question. It was the right substitution: the round
found a **declared upstream dependency that 004's spec did not carry at all.**

**The layering, on evidence.** Each layer's *output type* differs, and each spec states its
own limit in exactly those terms:

| Layer | Thesis | Universe | Output | Its own stated limit |
|---|---|---|---|---|
| 1 — Panorama | 001 | 35 names | Quantities: throughput, cost, margins for 3 issuers | *"It produced no valuation."* |
| 2 — Validation | 002 | 001's claims | Validated quantities — and **grade ≠ basis** | *"produces no trade ideas, adds no pillar"* |
| 3 — Cost axis + value map | 003 | 9 names | The **curve matrix** + the **value-pool map** | *"produces no position and no valuation"*; *"does not value any constellation"* (P10) |
| **4 — Value** | **004** | SPCX | The **valuation**: three regimes, scenario-weighted, against a dated print | Sizes no trades |

**003 tells you *where* value sits, by margin. 004 is the first thesis that asks what it is
*worth*.** 003 stops at *"+38.6% operating margin, 12.0M subscribers"* and never converts it.

- [2026-09-19] Q: `PROGRAM.md` §5 declares the edge `003 ──> 004 — SPCX sizes off the curve`, and `003/spec.md`'s header states it supplies *"the curve that **004 and 005 price off**"* — but 004's `Depends on` header carried only 001 and 002, §0 had no row for the curve or the value-pool map, and the string "003" appeared twice in this spec, both times incidentally inside round 1. How should the edge be encoded? → A: **004 consumes 003 — add the edge.** Add `003-launch-cost-curve-value-migration` to `Depends on`; add a §0 inherited row for the **curve matrix** (vehicle × architecture × DA-01 basis, with the per-architecture F5 floor) and the **value-pool map** (revenue growth and operating margin by segment); give §3 and §7 the rows that read them. **004 adds only the valuation and never re-derives the curve or the map.** Applied to §0 and `Depends on` in this round; the §3 and §7 rows are recorded as body amendments below.

- [2026-09-19] Q: *"004 应该是怎样更进一步和覆盖其他板块"* — which reading is intended? → A: **SPCX's three segments *are* the coverage.** 004's universe stays one issuer. Because 004 is the programme's **only** valuation of SPCX's Connectivity and AI segments — 006's universe is IRDM/GSAT/SATS/ASTS/VSAT and does **not** contain SPCX; 009 covers VRT/NVDA/GOOG/MSFT/AMZN/AAPL and does not either; 005 is space pure-plays — those two rows are built as **reusable references**, with §5 comparability boundaries naming **006 and 009** as permitted to price off them, not 005 alone. **SPCX Connectivity (54.9% of anchor revenue, the sector's largest connectivity operator at 12.0M subscribers) is valued only here.**

- [2026-09-19] Q: Given 004 is the valuation layer, where does round 1's ecosystem-keystone framework (F1/F2/F3) live? → A: **Consumed from 011 — recorded as a lens.** `PROGRAM.md` §0b assigns the main line and the a16z keystone lens to **011's P1** (*"the main line is 011's organizing claim; segment theses 004–010 supply its inputs and test its parts"*), and PROGRAM line 427 assigns the a16z `platform_shift_network_effects` cluster and the founder-CEO crisis cases to 011's retrieval. 011's spec was written **15:09**; 004's round 1 ran **18:19** — the re-centring predates §0b's ownership clause. Under the layering principle **004 is the valuation layer**: it *reads* the main line and its answer is *where value sits at SPCX*. **Round 1 is recorded as a lens applied inside the SOTP. §1b keeps its six pillars; no new pillar, no MAJOR event.**

- [2026-09-19] Q: 002 is COMPLETE and its programme-level result is that a grade does not carry a basis (SPCX `operating_margin`: filed **−16.68%** vs platform-served **+29.79%** — 46.47pp on one ratio). 004's §0 grades every inherited figure `DEMONSTRATED` with no basis column, and **P2 and P4 both falsify on operating-margin thresholds**. How should §0 and those `wrong_if` read? → A: **Add a basis column to §0; name the basis in P2/P4.** Every §0 row carries **grade + basis**. P2's and P4's `wrong_if` restate on the **filed segment basis** (segment operating income ÷ segment revenue, at the issuer's own segment boundary), because 002's remedy is explicit: *"a downstream thesis citing 002's validated set must carry the basis as well as the grade."* **The basis column is recorded as a body amendment (A-1), not applied here** — its *values* are research, established at Phase 1 by reading 002's six SPCX artifacts, and filling them by guess would reproduce the exact defect the answer removes. The P2/P4 `source=` restatement is recorded as **A-2**.

- [2026-09-19] Q: 004 pins `constitution_pin: 1.4.0` and §7 Phase 1 requires *"Constitution v1.3.0 loaded"*, but `constitution.md` is **ratified at v1.5.0** and 002 queues a **1.5.0 → 1.6.0** bump marking all 42 artefacts stale. Which version does 004 build against? → A: **Re-pin to 1.5.0 now; re-pin at 1.6.0 when it lands.** 004 adopts the ratified 1.5.0, which brings **DA-29** (back-solved and opaque checks — the mechanical circularity test) and **DA-30** (two bases on one concept, collapsed without a basis field) into scope. **DA-30 bears directly on §1c's component-identity rule**, which is the same basis discipline applied to SPCX's segment tables. The queued 1.6.0 is registered as an **expiry trigger**, not left as a surprise. Applied to the header, §6 and §7 in this round.

- [2026-09-19] Q: `thesis.md` declares no `expiry_triggers` — the deterministic scanner's single mechanical finding. What should invalidate 004? → A: **`[earnings_release, constitution_bump, skill_version_mix, cursor_close, market_data_stage_advances, issuer_discloses_orbital_compute_revenue]`.** The first three are the house trio, matching 003 verbatim. The last three are 004-specific and each names a distinct way the anchor goes stale: **`cursor_close`** — the $60B all-stock Cursor acquisition (V-5, Q-6) closes Q3 2026 and **re-bases the pre-close headline**, so the close dates the SOTP; **`market_data_stage_advances`** — Market Data Stage is `none`, so every market-referenced figure is a **dated print** ($135.00, 2026-06; ~$1.62T per the constitution) and the whole price discipline is print-bound; **`issuer_discloses_orbital_compute_revenue`** — an orbital-compute revenue line would falsify **A4**'s terrestrial/orbital boundary, the constitutional ceiling P3 is built on. Applied to `thesis.md` in this round.

#### Dispositions this round closes or changes

| Item | Round-1 status | Round-2 disposition |
|---|---|---|
| **Q-11** (`CAPITAL` vs `MOAT`/`NETWORK_EFFECT` for the main line) | *"load-bearing"*, open, provisional on `MOAT`/`NETWORK_EFFECT` | **CLOSED — dissolved, not answered.** The framework is 011's; 004 is the valuation layer. **`CAPITAL` holds unamended** and Q-4's confirmation stands. The main line's binding constraint belongs to **011**, which owns the claim. |
| **Q-7** (002 dependency: inherit 001's grades or wait?) | Open, provisional *"inherit and label"* | **SUPERSEDED.** 002 is **COMPLETE**. 004's inheritance question is no longer *whether* to wait but *what* it inherits — now answered by the basis-column row above. |
| **Q-8** (F1 vs the SOTP are operationally opposed) | Open, provisional *"frameworks govern entry and holding; the SOTP governs what to pay"* | **NARROWED, still open.** With F1/F2/F3 consumed as lenses, the opposition is **011's** to report where it produces positions. 004 reports it only if the SOTP's own scenario weights conflict with F1's method. |
| **Q-1 … Q-6, Q-9, Q-10** | Open, provisional readings recorded | **UNCHANGED.** No round-2 answer touches them. All provisional readings stand. |
| **Round 1's re-centring** | Recorded in Clarifications only; never written into the body | **RESOLVED AS A LENS.** §1b keeps six pillars. Round 1's pillar re-ranking is **rationale, not structure** — P2 Connectivity is the main line *because* the framework predicts value settles there, but it remains P2 in the pillar set. |

#### Body amendments recorded by this round — **not yet applied**

Recorded rather than silently written, because they span more than one change class and
`constitution.yaml` Q33 governs the bump. **The re-pin to 1.5.0 is itself a MINOR event.**

| # | Target | Amendment | Class |
|---|---|---|---|
| **A-1** | §0 inherited table | Add a **`Basis`** column to every row, populated at **Phase 1** from 002's six SPCX artifacts. Left unpopulated deliberately: the values are research, and a guessed basis reproduces the defect the answer removes. *(The §0 **inherited-from-003** block was applied in this round — see above.)* | MINOR |
| **A-2** | §1b P2 and P4 | Restate the `wrong_if` `source=` on the **filed segment basis** — P2 and P4 currently falsify on operating-margin readings that 002 proved basis-ambiguous to 46.47pp | PATCH |
| **A-3** | §3 Skill Deployment Matrix | Add the rows that **read 003's curve and map**; the matrix currently consumes no 003 output | MINOR |
| **A-4** | §5 Cross-Cutting | Add the **006 and 009** comparability boundaries on the Connectivity and AI anchor rows, per the coverage answer | MINOR |
| **A-5** | §7 Thesis Phases | Add the phase that reads 003; Phase 1's dependency line is already corrected to v1.5.0 | MINOR |
| **A-6** | §6 Output Contract | `_cross/anchor-sotp.md` carries **which downstream theses may price off each row** — 005, 006 **and 009**, not 005 alone | MINOR |
| **A-7** | `thesis.md` | `claim` and `pillars` are still `[TBD]`/`[]`; populate from §1b once A-1 … A-6 land | MINOR |

---

### Clarify round 3 — 2026-09-19 · **SCOPE AGAINST A COMPLETED 003, AND A LIVE PRICE FEED**

Owner instruction: *"我们还要再详细的clarify 004的研究范围 … 003 确实以 spacex 为重点，但是也覆盖了其他公司。
004 和 003 的区别是什么？004 一定是基于 003 的结果，004 应该是对 spacex 更深刻的分析"* — with nine
`003/artifacts/` directories attached as evidence.

**Two facts changed this round, and both were verified rather than assumed.**

**Fact 1 — 003 is COMPLETE, and it already did much of 004's P2 and P4.** 003 produced **nine SPCX
artifacts** across nine of 004's fourteen §3 rows, plus `_cross/launch-cost-curve.md` (1,013 lines)
and `_cross/value-pool-map.md` (1,408 lines). Its `value-pool-map` E-01/E-02/E-03 already carry all
three segments with **exact** component-identity derivations — Connectivity **+38.59%**, the
**122.14 pp** gross-to-operating swing decomposed (R&D **111.85 pp** + SG&A **10.29 pp**), the
cross-segment spread **94.93 pp**, and the finding that **`12.3%` is three things — launch-only is
8.29%**. **004's Q-3 was already answered there, and its P2 and P4 were partly pre-computed.**

**Fact 2 — a keyless live market feed exists and is serving.** `data-tools/market_data.py`; source
**nasdaq**, `auth: "none"`; `live_snapshot.py` already names **SPCX**. **Verified live 2026-09-19:
SPCX $152.71, close 2026-09-18, 3,759 ms.** 004's §3 declared **`none` on all fourteen rows**, which
contradicted the registry on two and pinned the primary instrument where it could not get a price.

- [2026-09-19] Q: 9 of 004's 14 §3 rows re-run skills 003 already ran on SPCX. What should §3 do? → A: **Consume 003's 9; run only the 5 new.** §3 is rebuilt into **3a Executed (7)** and **3b Consumed (9)**. The consumed block cites 003's artifact paths and states each is *not re-run*. Applied in this round.

- [2026-09-19] Q: *"004 应该是对 spacex 更深刻的分析"* — what does 更深 mean? → A: **Both, sequenced — granularity first, then capitalisation** — *and* 004 gains live market data. **A conflict with the answer above was raised rather than silently resolved**: 003 worked at the **segment** level, so "go inside the segments" is work on the very skills the consume answer said to skip. **Resolved by putting the depth in a new row — `revenue-decomp`** (registry stage `none`, vertical business-intelligence), a skill used by **neither** 003 nor 004, purpose-built for *"segment breakdown, geographic split, product-line waterfall"*. **The nine stay consumed untouched; no skill is re-run, and the depth is real.** Applied as §3a row 3 and Phase 2.

- [2026-09-19] Q: 003 flags Space as `captive_integrated` with **NO transaction price** — *"comparing a price to a non-price."* 004's P4 wants standalone value; P6 wants a comparable multiple. What is P4's multiple a multiple of? → A: **Carry it as a stated limitation, per P6.** Space enters the SOTP with an explicit non-comparability boundary; **no external multiple is borrowed**; its value comes from segment contribution, with the DA-06 flag travelling with the number. Keeps P6's partition rule intact and needs no new method. Applied to §7 Phase 5 and §1b P4's text.

- [2026-09-19] Q: 003's E-03 misstates SPCX's AI segment twice. How should this be handled? → A: **Raise to 003 — fix at source.** **FIXED IN PLACE in `003/_cross/value-pool-map.md`** with both corrections and a correction table recording what changed and why, since 004 **and 005** cite the map as their declared reference. See the separate finding below.

- [2026-09-19] Q: Which market-data stage should 004 declare? → A: **Registry-faithful — `late` on the valuation rows only.** The registry has exactly **three** `late` skills: **`sotp-valuation`, `ratio-analysis`, `reverse-dcf`**. The two **executed** `late` rows are set accordingly. **`ratio-analysis` is consumed from 003 at 003's `none`** — flagged as **FC-1**, because 003 itself declared `none` where the registry says `late`. Applied to §3a, §4, the header and §6.

- [2026-09-19] Q: A live quote exists ($152.71, 2026-09-18); the constitution's anchor (~$1.62T, against $135.00) is ~13.1% behind. **[Premise corrected 2026-09-19: the anchor implies $119.41/share pro-forma against a live $152.71, so the gap is +27.9%. The 13.1% compared the live price to the IPO price, not to the anchor. THE DECISION BELOW IS UNAFFECTED AND STANDS — it decides which bases to publish, and does not turn on the size of the gap.]** Which is the headline comparator? → A: **Both — live and dated, with the spread reported.** They answer different questions: the live quote is the **market fact**, stamped with observation time and source; the constitution's anchor is the programme's **sanctioned governance reference** and is what 001–003 are comparable to, since all three are print-based and carry no prices. **Every market-referenced figure now carries its basis, its stamp, and its source** — a figure quoted without all three is inadmissible. Applied to §5 and §6.

- [2026-09-19] Q: §5 bars correlation, beta and relative-multiple regression against live prices. What should that bar become? → A: **Three unlocks, and no more** — **(1) beta / cost of equity** for P5's scenario weights (the other half of an estimate §5 already calls *"high"* macro sensitivity); **(2) live comps multiples** for P6's boundaries, with the constraint explicitly surviving the data *(IRDM and GSAT are P11 deal securities — a live multiple on a spread is no more admissible than a stale one)*; **(3) event-window price reactions** — SATS's $16.48bn impairment, the xAI merger, the Cursor announcement. **Still barred:** a relative-multiple regression of SPCX against live prices **as a valuation method**. Applied to §5.

- [2026-09-19] Q: The DCF gate fails on the ≥3-years-positive-FCF limb. With a live price, does `reverse-dcf` enter §3? → A: **Yes — add `reverse-dcf`.** §1c's gate is **amended to distinguish FORWARD from REVERSE**, which it previously did not: a forward DCF forecasts and discounts, needs the FCF history, and **stays barred** (`dcf` remains absent from §3); a reverse DCF takes an **observed price** and solves for the implied growth, forecasting nothing, and so never faced that limb. It enters at its registry stage, **`late`**, as a **cross-check on the three regimes** in the same class as `comps` — never primary. Applied to §1c, §3a and Phase 7.

#### ⚠️ A separate finding — 003's `value-pool-map.md` was wrong about SPCX's largest segment

Found while reading the artifact 004 now consumes, and **raised to 003 as instructed.** Both errors
sat in one sentence in **E-03**:

| Read | Correct | What it was |
|---|---|---|
| **32.77%** of consolidated revenue (2,561 / 7,814) | **49.08%** | The sentence's **own printed operands** evaluate to 32.77%. The 49.08% is that entry's `operating_margin` — copied one line into the revenue-share slot. **A DA-30-class defect: a served value not matching its own stated basis, inside the map that fixes basis discipline for the programme.** |
| **Consolidated result (143)** | **1,438** | Unsourced; matched by nothing. Segment losses sum to (1,799); the consolidated result is (143), and **003's own `operational-kpi` artifact states `$(143)M` with the identity `7,814 − 7,957 = (143)` closing exactly.** |

**Fixed at source** with a correction table; **neither error changes a finding** — the corrected
revenue share keeps AI the largest single drag and the corrected loss basis makes it *more*
dominant, not less. **Because the same class of error is what 002's programme-level result is
about, the episode is recorded rather than absorbed:** *the artifact that enforces basis discipline
published a figure whose basis did not match its operands, and it took a downstream thesis reading
it as an input to catch it.*

#### Round-2 amendments — disposition at round 3

| # | Round-2 item | Round-3 disposition |
|---|---|---|
| **A-1** | §0 basis column | **STILL OPEN.** Unchanged; populated at Phase 1 from 002's SPCX artifacts |
| **A-2** | P2/P4 `source=` on the filed segment basis | ✅ **APPLIED at plan time, 2026-09-19.** Both `wrong_if` now read `source=10-Q_segment_note_component_identity_at_filed_segment_basis`, each with an in-line definition of the reading (segment operating income ÷ segment revenue at the issuer's filed segment boundary, component identity shown). P4's note records the additional limit that its **ex-R&D numerator is a `MODELED` construction**, since the filing does not split Starship from Falcon R&D — naming the basis makes that limit visible rather than repairing it |
| **A-3** | §3 reads 003's curve and map | ✅ **APPLIED** — §3 rebuilt into 3a/3b with the nine consumed artifacts cited by path |
| **A-4** | §5 names 006 and 009 as permitted to price off the anchor | **PARTIAL** — §6 and §1b carry it; §5's own boundary text still needs the sentence |
| **A-5** | §7 phase reading 003 | ✅ **APPLIED** — Phase 0 is the consume edge |
| **A-6** | §6 output contract names 005/006/009 | ✅ **APPLIED** — plus the price-stamp and consumed-input-citation rules |
| **A-7** | `thesis.md` `claim` / `pillars` | **STILL OPEN** |

#### New items this round

| # | Target | Item | Class |
|---|---|---|---|
| **FC-1** | §3a | `ratio-analysis` is registry-`late` but consumed from 003 at `none`. Price-independent as consumed (the coverage ratio needs no price), so defensible — **but 003 declared `none` where the registry says `late`**, the same mismatch round 3 corrected in 004. Move to 3a at `late` if price-stamped ratios are wanted: **+1 task** | MINOR |
| **FC-2** | §3a | `peer-bench` is consumed, but 003 ran it on **SPCX, RKLB, FLY** while 004's purpose is the **MSFT, GOOG, NVDA, VRT, IRDM** framing set, which 003 never benchmarked. Move to 3a if the framing set must be benchmarked rather than read across: **+1 task** | MINOR |
| **A-8** | §3b / §7 | ✅ **RESOLVED IN THIS ROUND — `plan_audit.py` returns 4/4.** Three parser-level defects were found and fixed while re-verifying: (i) the 3b table's bespoke 4-column shape failed the parser's `cells[3]` = tickers / ≥5 cells contract, so every consumed pair read as *"generates ZERO tasks"* — **3b now uses the canonical 6-column shape with `consumed` in the Depth column**; (ii) bolded skill names in `cells[0]` do not match the registry — `**sotp-valuation**` ≠ `sotp-valuation`, because the parser strips backticks but not asterisks; (iii) `revenue-decomp` and `reverse-dcf` were subscribed by no pillar and would have taken the `[P1]` fallback bracket, silently mislabelling them as Minimum-Defensible-View work. **The lesson generalises: this spec's tables are a machine contract as well as prose, and a layout chosen for readability can silently zero out a subscription.** | PATCH |
| **A-9** | §5, P5, §7 Phase 6 | Beta / cost of equity is now an input to the scenario weights, but `assumptions.yaml` carries **no beta field** — the same silent-drift exposure §1c already records for scenario weights | MINOR |
| **A-10** | `thesis.md` | ✅ **RESOLVED IN THIS ROUND.** `market_data_stage: none` became **`per_row`** with the declaration spelled out (two `late`, five `none` executed, nine `none` consumed), the source and its verification, the two price bases, and the **Q42 consequence**: `entities.md` must now define a bars schema, which 003 never needed. The **`market_data_stage_advances` trigger was revised to `market_data_stage_regresses`** — the old trigger **had already fired**, and the risk is now inverted: the exposure is that the feed *stops*, dating the discount measure back to the constitution's print. | PATCH |

---

### Clarify round 4 — 2026-09-19 · **THE DEPTH ROW CORRECTED, AND V-7 RESOLVED FROM XBRL**

**Provenance note, stated plainly.** This round opened from a request **identical to round 3's** —
same spec, same nine `003/artifacts/` directories, same three questions. **Round 3 was not re-run.**
The round instead checked whether the depth row round 3 had just written was *buildable*, which is
a question round 3 asked of 003 but never asked of its own output. **It was not.**

#### ⚠️ Self-correction: `revenue-decomp` named cuts that are not filed

Round 3 wrote *"Starlink by tier (consumer / enterprise / **aviation** / **maritime** /
government)"*. Checked against 003's artifacts:

| Cut | Verdict |
|---|---|
| Consumer; Enterprise & Government | ✅ **filed** — `1,721 → 2,485 (+44.4%)` and `867 → 1,806 (+108.3%)`, both *"segment, filed"* |
| **aviation**, **maritime** | ❌ **appear twice in all nine SPCX artifacts, both times as qualitative prose, with no revenue figure attached to either** |
| subscribers / ARPU by channel | ❌ `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — the managed channel is *"disclosed as revenue but not as subscribers"* |

**The filer files two; the spec specified five.** This is the round-1 F1-screens failure — *a screen
whose inputs do not exist* — committed inside 004's own method, one round after 004 recorded that
failure as a lesson. **The correction is a method, not a taxonomy:** the row now derives its cuts
from the filings and records each as `formable` or with its disposition class.

#### ⚠️ `get_segment_data` is broken — and it was the obvious route for this row

```
get_segment_data(ticker="SPCX", segment_type="product")
  → {"error": {"code": "INTERNAL_ERROR", "message": "column \"k\" does not exist"}}
```

**The working route is `search_xbrl_facts(…, view=detailed)`**, which returns dimensional axes
directly. Confirmed at SPCX: `srt:ConsolidationItemsAxis`, `us-gaap:StatementBusinessSegmentsAxis`
(`spcx:SpaceMember` / `spcx:ConnectivityMember` / `spcx:AIMember`), `srt:MajorCustomersAxis`,
`us-gaap:StatementEquityComponentsAxis`, `us-gaap:AntidilutiveSecurities…Axis`,
`us-gaap:DebtInstrumentAxis`, `srt:RangeAxis`. **286 facts for SPCX FY2026 across 10 pages.**

#### ✅ V-7 resolved — the percentages were in the platform all along

V-7 recorded that *"the extract does not carry the percentages"* of the Note 3 customer
concentration, and made the DCF's backlog limb unevaluable. **They are retrievable as XBRL
dimensional facts:**

| | H1 2026 | Q2 2026 | H1 2025 | Q2 2025 |
|---|---|---|---|---|
| **Customer A** | **17.89%** | **18.30%** | 19.89% | 16.70% |
| **Customer B** | **12.20%** | **19.50%** | — | — |

`ConcentrationRiskPercentage1` × `srt:MajorCustomersAxis` × `CustomerConcentrationRiskMember` ×
`RevenueFromContractWithCustomerMember`, `spcx-20260630.htm`, authority 2. **Three findings ride on
the retrieval itself:** (a) **Customer A repeats the two-bases-opposite-signs pattern** — H1 falls
(19.89% → 17.89%) while Q2 rises (16.70% → 18.30%); (b) **Customer B has no 2025 comparative**,
consistent with an entity acquired inside the period, and carries the **DA-19** boundary flag;
(c) **combined H1 concentration is 30.09%**. **Customer concentration is not a backlog figure, but
it bounds the counterparty set the backlog could consist of** — so the limb goes from *unquantified*
to *bounded*.

- [2026-09-19] Q: My `revenue-decomp` row names five Starlink tiers; SPCX files two. How should the depth row be scoped? → A: **"let 10-Q and 8-K filings define — they usually have revenue-decomp in filings and XBRL data."** The row now declares **a method, not a taxonomy**: discover the cuts from the 10-Q/8-K narrative disclosure **and** the XBRL dimensional axes, then record each as `formable` or with its disposition class. Applied to §3a plus the box below it.

- [2026-09-19] Q: Q-2 — the AI segment's headline framing? → A: **Report all three; headline = INVESTED CAPITAL.** Confirmed, not provisional. Applied to §1b P3. **(a)** — the terrestrial-compute interval — is materially stronger as of round 3, since live data makes it constructible for the first time, but it is **admitted non-comparable by construction**, so it informs the range without carrying the headline. **(c)** remains legitimate and stated.

- [2026-09-19] Q: Q-5 — is a comparability boundary a partition or a graded score? → A: **Partition — in or out, with the excluded class named.** Confirmed, not provisional. Applied to §1b P6. **Round 3's live data makes the constraint harder**: a live multiple on a P11 spread (IRDM, GSAT) is *priced* and still *inadmissible as a fundamental* — it lands in the excluded class with `P11` as its reason.

- [2026-09-19] Q: Q-6 — pre-close or pro-forma headline? → A: **PRO-FORMA — overriding the round-0 provisional, which said pre-close.** Cursor is inside the headline. **This is the round's most consequential answer, and it has a cost that is recorded rather than absorbed:** V-5 moves **`warn` → `blocking`**, because pro-forma requires the $60B all-stock consideration and its dilution, and V-5 previously recorded dilution as *not determinable*. **P1 cannot be delivered without it.** The `cursor_close` expiry trigger stands but its **logic inverted** — the close now *makes the anchor real* rather than *invalidating* it; the trigger survives because a terminated merger would leave a pro-forma headline built on a consideration that no longer exists. Applied to §1b P1, V-5, the blocking-set note, and `thesis.md`.

#### New items this round

| # | Target | Item | Class |
|---|---|---|---|
| **A-11** | §1c, §5, §7 Phase 7 | ✅ **APPLIED at plan time, 2026-09-19.** Applied to all three targets: **§1c** instrument 1 now declares the pro-forma basis and Space's DA-06 non-comparability on its face; **§5**'s discount decomposition carries both the pro-forma requirement and the **two-price-base rule with the spread named as its own component**; **§7 Phase 7** states the pro-forma headline and gates on V-5. **One substantive consequence surfaced during the application:** pro-forma, the Cursor consideration is **Class A stock**, so the **control/float component is no longer a discount *on* the anchor — it is partly a discount *created by* the transaction the anchor now includes.** Where the two cannot be separated, that is the finding | PATCH |
| **A-12** | §3a | ✅ **RESOLVED IN THIS ROUND, with a correction to round 4's own record.** The tool breakage was **already documented in `003/plan.md` § F4** (sourced from 002 §7, with a fuller diagnosis). Round 4 found it independently and presented it as new; §3a now **credits 003 and cross-cites F4**. The substantive fix stands: 004's spec never carried 003's finding, and the working route (`search_xbrl_facts(view=detailed)`) is now recorded | PATCH |
| **A-13** | §2, §3b | **Customer A / Customer B are now identified by percentage but not by name.** V-7's resolution bounds the counterparty set without naming it; if the names are disclosed, P4's inter-segment transfer limitation and 006's competitor set both change. Bounded read | MINOR |
| **A-14** | §3a | **`revenue-decomp` must report which cuts it *found*, not which it expected** — a run that discovers only the filed two-way split is a **pass**, not a gap. Stated so the artifact is not judged against round 3's five-tier error | MINOR |
