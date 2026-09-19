# Research Thesis: 006 — Tier 2 — Constellation Operators: Connectivity, Spectrum & Geospatial

**Constitution Ref**: constitution.md v1.6.0 (`constitution_pin: 1.6.0`) — **re-pinned at the
tier re-cut, 2026-09-19.** The spec was written against `1.4.0`, which predated four things
this thesis depends on: the **one-axis universe re-cut** (Tier 2 is now *operating a
constellation*, and **PL, BKSY, HAWK and SPIR have moved into it from Tier 1**), the
**DA-24 redefinition** (the defining SATS instance is an inverted impairment, not a sale —
the independence proof is withdrawn), the **DA-26 falsified census** (20 tested, 19
exhibiting; FLY the counterexample), and the **register's DA-29/DA-30** entries. A stale pin
is a hard failure under P4, not a footnote.
**Created**: 2026-09-18
**Status**: Active
**板块**: Tier 2 · Wave 1 · **Binding constraint**: `REGULATORY_SPECTRUM`
**Time Horizon**: 2026-Q4, terminating at the wave-1 hand-off to 007, 009 and 011
**Depends on**: `001-technology-baseline` (pin 1.2.0 — the panorama) · `002-evidence-validation`
(**COMPLETE** — the validated input set, inherited *with its verdicts, not just its grades*) ·
`003-launch-cost-curve-value-migration` (**added at the re-cut** — 006 consumes the value-pool
map and the corrected operator margin ladder and never re-derives either) ·
`004-tier0-spacex-anchor` (the operating-leverage benchmark and the **permitted Connectivity
reference**; 004's comparability boundaries name 006) ·
`005-launch-spacecraft-services` (**added at the 2026-09-20 clarify round, Q-11** — a
**citation-only** dependency: 005 completes first and 006 cites its Tier 1 cross-section for
RKLB's financing facts, the $3.6B committed bridge and the consideration mix. **006
re-derives none of it, and the edge does not run the other way** — 005 carries its RKLB gate
`known-open` pending 006's P4 rather than waiting)
**Owns**: two questions, and only these two, per the constitution's ownership table —
(a) the **IRDM/RKLB deal gate chain** (FCC → ITU → DCSA, dated catalysts, break re-underwrite);
(b) **operator margins by segment**. Everything else in the tier is a cited dependency, not a
pillar (§5b).
**Produces**: the **segment thesis for Tier 2** — a licence-versus-business value attribution
per name, a direct-to-cell (D2D) placement map, and **one dated regulatory gate checklist per
name**. Sizes no position above P11's 2% binary cap.

---

## 0. Inherited baseline — what this thesis does NOT re-derive

001 built the panorama, 002 validated it, 003 mapped the cost curve and the value pools, and
004 valued the anchor. **006 takes all four as given.** Re-deriving any row below is out of
scope; the artifact cites the source file rather than repeating its work. A result is
inherited **with its verdict as well as its grade** — several rows carry a verdict this thesis
would otherwise silently re-assert in its stale form, and those are marked ⚠️.

**Path shorthand — declared, not implied.** `00N/` expands to `theses/00N-…/` for N = 1…4, so
`002/artifacts/IRDM/2026-09-18_1500_recent-quarter_methodology.md` reads
`theses/002-evidence-validation/artifacts/IRDM/2026-09-18_1500_recent-quarter_methodology.md`.
Every row below resolves to a file on disk.

**Grade vocabulary, declared — and this is load-bearing.** 002's register asserts verdicts this
programme's four-term P4 vocabulary (`DEMONSTRATED` / `CLAIMED` / `MODELED` / `DERIVED`) does
not contain: **`UNEXERCISED`** (the test ran on nothing), **`UNEVIDENT`** (the test could not
run), **`WITHHELD`**, **`REFUTED` / `CONFIRMED`** (verdicts, not grades), and **`NOT TESTABLE —
kind N`**. **`UNEXERCISED` and `Clean` are different results and must not be reported as the
same** — 002's ledger states it directly: *"a check that closes cleanly while testing nothing."*
006 preserves the distinction rather than collapsing it into `PENDING`.

**Corrections index — the stale scalars, and where each one is routed.** Four inherited figures
are **withdrawn or restated**, and each is listed here so that a downstream reader who greps the
*old* value lands on the correction rather than on the row that still quotes it verbatim (the
rows below preserve what was inherited, per the frozen-artifact policy, and the ⚠️ verdict cell
in each is authoritative):

| Stale inherited value | Status | The value that replaces it | Row |
|---|---|---|---|
| **GSAT operating margin `+7.4%`** | **`REFUTED` — a DA-23 sign strip** | **`−7.37%`** (a $(4,775) thousand operating loss) — *and `7.4×` leverage at GSAT is a separate, correct figure that must not be swept up with it* | §0.1, §0.3, §2 |
| **SATS `~$27B` of spectrum gains** | **`REFUTED` — withdrawn** | A **non-cash 17,632,011 thousand impairment CHARGE**; licences still carried at **34,550,802** net | §0.1, §0.2 |
| **SATS margin `10.7%`** | **restated ex-item** | **`8.91%`** (`392,847 − 66,159 ÷ 3,667,489`), against the filed `10.71%` | §0.1, §0.2 |
| **SATS margin progression `2.3% → 5.7% → 460.5% → 118.1% → 10.7%`** | **`REFUTED` — absolute values of losses, plus a DA-26 annual-in-a-quarterly** | Filed sign series **`(2.28)% → (5.73)% → (460.46)% → (20.54)% → +10.71%`** | §0.1 |
| **IRDM `23.2% → 15.1% is a decline`** | **confirmed as arithmetic, corrected as a *direction*** | The FY-basis margin **rises** (**24.12% → 27.07%**); the Q2 decline is **63.8% transaction cost**, and ex-those the margin is **21.45%** | §0.1, §0.3, §1b P1 |
| **`DA-24 is independent of DA-23`** | **`REFUTED` — the independence proof is withdrawn** | **Both defects apply at SATS** (DA-23: 12/12 filed-negative subtotals stripped) | §0.1, §1c |
| **`GSAT / VSAT / ASTS statements validated by 002`** | **does not apply** | **002 carries no DA-census row for GSAT, VSAT or ASTS.** No §0 row may imply otherwise | §0.2 |

### 0.1 Inherited from 001 — the panorama

| Inherited result | 001 artifact | Grade |
|---|---|---|
| **IRDM is profitable on licensed L-band** — the buy-side test PIL-6 needed. Q2 2026 revenue **$225.237M (+3.8%)**, operating income **$34.008M (−32.3%)**, operating margin **15.10% vs 23.17% (−8.07 pts)**, net income **$9.679M (−55.9%)**, R&D **$5.530M (+29.2%)** | `001/artifacts/IRDM/2026-09-18_1239_competitive_methodology.md` | `DEMONSTRATED` |
| **The direction of that margin is itself the finding** — *"the licence is durable, the service business on top of it is not automatically so"* — and 001 left the cause open, nominating it for Phase 6: *"test whether that decay is competitive (Starlink/D2D pressure) or cyclical"* | same | `DEMONSTRATED`. ⚠️ **The premise now needs 003's qualifier**: on the **fiscal-year** basis IRDM's margin **rises** — 24.12% (FY2024) → 27.07% (FY2025) — and the Q2 decline is **63.8% non-recurring deal cost**. See §0.3. The *question* stands; the *framing* is corrected. |
| **"The spectrum, not the constellation, is the scarce input."** Satellites can be rebuilt; L-band licences cannot be created | same | `DEMONSTRATED` |
| ⚠️ **SATS realised ~$27B of gains across 2025 H2 from selling spectrum licences**, against **$15.0B of full-year 2025 revenue** — the regulatory asset was worth **~1.8×** the entire operating business that held it | `001/_cross/phase-4-regulatory-allocation.md` | **`REFUTED` — the row is withdrawn.** `~$27B` **does not reproduce**; no filed figure equals it. The nearest filed aggregates are net spectrum **$34,550.8M**, gross **$39,885.3M**, pre-addition balance **$29,614.8M**, and AT&T cash **$22.650B**. **Nothing closed and no gain was recognised** — the 2025 item is a **non-cash 5G-Network impairment CHARGE** (§0.2). 006 carries the correction, not the row. |
| **The SPCX–EchoStar mark prices spectrum: ~$19.6B** for AWS-4 / H-Block / AWS-3, **FCC-approved with the transfer closed**. It is a transaction value, **not** a $/MHz-pop (DA-17) | `001/_cross/phase-4-regulatory-allocation.md`; constitution F6 | **Re-graded `DERIVED`** — it is `$17.0B + $2.6B`, a sum of two disclosed figures, not a filed one. And the **$2.6B buys 15 MHz of AWS-3 (1695–1710 MHz), not AWS-4/H-Block**; the two quantities must not be merged (DA-17) |
| ⚠️ **DA-24 registered — asset-sale contamination.** SATS 2025 Q3 operating income was **4.6× revenue** ($16.6B on $3.6B); margin progression **2.3% → 5.7% → 460.5% → 118.1% → 10.7%** | constitution §Data-Integrity Register; `001/artifacts/SATS/2026-09-18_1239_risk_methodology.md` | **Corrected at v1.6.0 — the class is now "non-operating contamination — a GAIN *or* a CHARGE", and the defining SATS instance is an INVERTED IMPAIRMENT, not a sale.** The quoted progression reproduces only as `abs(OI) ÷ revenue`; the **filed sign series is `(2.28)% → (5.73)% → (460.46)% → (20.54)% → +10.71%`** — four of five terms were the absolute values of losses and the `118.1%` term is annual-on-annual (a DA-26 instance inside a DA-24 exhibit). **Q4 2025 was absent from the progression entirely** |
| ⚠️ **DA-24 is independent of DA-23** — SATS is contaminated but **not** sign-stripped (EPS × shares reconciles to 0.3%). Exactly one defect, not both | `001/artifacts/SATS/2026-09-18_1239_risk_methodology.md` | **`REFUTED` — the independence proof is WITHDRAWN**, on two independent grounds: it uses `EPS × shares`, **a test the register forbids** (it passes on both sides of a flip), and its residual is **invariant under a global flip** — it cannot detect the defect it was used to rule out. **And the claim is substantively false: DA-23 IS present at SATS** (12/12 filed-negative subtotals stripped, 8/8 filed-positive clean). *"DA-24 without DA-23" is false at SATS.* |
| ⚠️ **SATS's clean quarter** — revenue **$3,667.5M**, operating income **$392.8M**, operating margin **10.7%**, net income **$146.9M (4.0%)** | same | **Corrected — 10.71% is the *filed* Q1 2026 figure and it carries a (66,159) thousand settlement credit. Ex-item the margin is `(392,847 − 66,159) ÷ 3,667,489` = **8.91%**.** See §0.2, carry-forward C1 |
| **The regulatory gates are SEQUENTIAL, not parallel** — FCC licence transfer (**passed**) → ITU international coordination (**named** in RKLB's Iridium risk factors) → DCSA / CFIUS-adjacent review (**also named**) → national market access (**not evidenced**). DA-18 upgraded from ambiguity to checklist | `001/artifacts/SATS/…_risk_methodology.md`; `001/_cross/phase-4-regulatory-allocation.md` | `DEMONSTRATED` for gate identity and naming; the *ordering* is `MODELED`. ⚠️ **The ITU limb is corrected at §1b P4**: the filings say IRDM does not file at the ITU — **the United States files on its behalf** — so ITU coordination is not a consent the issuer can be asked to obtain |
| **PIL-6's disposition splits**: the *premise* is `DEMONSTRATED` from filings; only the *falsifier* is `UNRESOLVABLE-FROM-PLATFORM` (FCC IBFS / ITU Space Network List) | same; `001/_cross/technology-baseline_synthesis.md` line 6 | `DEMONSTRATED`. **002 sharpened the class**: this is **kind 5** — the registries exist, are public and are free; **the block is platform reach**, and the remedy is a connector |
| ⚠️ **GSAT is the purest monopsony in the universe** — revenue **$64.772M (−3.5%)**, operating margin **7.4%**, **93% of net income non-operating**, **7.4×** leverage, **12.0%** equity/assets, **$2,136.8M** accumulated deficit | `001/artifacts/GSAT/2026-09-18_2040_competitive_methodology.md` | ⚠️ **The operating margin is WRONG as inherited. GSAT's filed Q2 2026 operating margin is −7.37%, an operating LOSS of $(4,775) thousand** — the `7.4%` is the **DA-23 sign strip** (plus a systematic 1,000× unit offset). Corrected at §0.3; 003 recorded the correction and it is applied everywhere in this spec. The other five figures stand |
| **SPCX Connectivity is the tier's operating-leverage benchmark** — operating income **$1,656M** on **$4,291M** revenue (Q2 2026, **+79.4% YoY**), ARPU **$66 (−22.4%)** against subscribers **+101.2%** | constitution §Sector Preferences; `001/artifacts/SPCX/2026-09-18_2310_operational-kpi_methodology.md` | `DEMONSTRATED`. **004 re-derived it and graded the *regime* `MODELED`** — see §0.4 |
| **DA-17 / DA-18 / DA-19 are registered ambiguity classes** — spectrum quantity (MHz vs MHz-pop vs licensed footprint); "regulatory approval" (ITU coordination vs national licence vs market access); orbital slot priority (ITU filing date vs bring-into-use milestone vs operation — **priority can lapse for non-use**, so a filing is not a durable asset) | `001/spec.md` §1c (DA-01 … DA-22) | `DEMONSTRATED` as *registrations*; **none is resolved** |
| **P11 binds IRDM and GSAT** — do not underwrite standalone fundamentals; the price tracks a spread; binding constraint `REGULATORY_SPECTRUM`; size at the 2% binary cap; **on a break, re-underwrite from scratch** | constitution §In-Flight M&A Treatment | `DEMONSTRATED` as policy |

### 0.2 Inherited from 002 — the validation, and the reason this §0 exists

**The propagation finding is the reason the table below is written out.** 002's ledger
measured it: **only 3 of 32 corrections reached a pin**, and `upstream_stale` is *"mandatory in
all 41 artifacts, correct in all 41, and consumed by none."* Its conclusion is the standing
instruction for every downstream thesis: **"A correction that is recorded and never propagated
is indistinguishable, in effect, from one never made."** 006's §0 is a propagation mechanism,
not a courtesy.

| Inherited result | 002 artifact | Grade / verdict |
|---|---|---|
| **The programme-level correction 006 inherits: `DEMONSTRATED` is not a sufficient grade for an input** — SPCX's `operating_margin` served **+29.79%** against a filed **−16.68%**, a **46.47 pp** divergence. A downstream thesis must carry **the basis as well as the grade** | `002/_cross/validation-ledger.md` §1.6.1; `002/_cross/002-evidence-validation_synthesis.md` §1 | `DEMONSTRATED` (both figures); the divergence is the finding |
| **IRDM component identity closes with ZERO residual on 7 of 7 periods**: Q2 2026 `225,237 − 191,229 = 34,008`; Q2 2025 `216,906 − 166,648 = 50,258`; H1 2026 `444,294 − 359,573 = 84,721`; H1 2025 `431,784 − 321,138 = 110,646`; FY2025 `871,659 − 635,679 = 235,980`; FY2024 `830,682 − 630,298 = 200,384`; FY2023 `790,723 − 709,095 = 81,628` | `002/artifacts/IRDM/2026-09-18_1500_recent-quarter_methodology.md` | `DEMONSTRATED` (filed cells) |
| **001's IRDM arithmetic reproduces exactly** — the re-derivation is 002's, and nothing in 001 is rewritten | same | `DEMONSTRATED` |
| **DA-23 at IRDM: 12 concept-series carry confirmed `|x|` strips, spanning all four statements.** The both-directions control is a single filed row — `AOCI (loss), net of tax \| (4,681) \| 406` served as **+4,681,000** and **+406,000** | `002/artifacts/IRDM/2026-09-18_1500_recent-quarter_methodology.md` §3.3 | `DEMONSTRATED` |
| **`IRDM`'s `OperatingIncomeLoss` is NOT stripped — the defect is CONCEPT-SELECTIVE**, so a clearance that samples one region of the statement generalises to nothing | same §3.5, §8 | `DEMONSTRATED` |
| ⚠️ **001's "5/5 clean" DA-23 clearance at IRDM is REFUTED** — *"not a passed check but an unengaged one: it sampled the region of the statement where the defect is absent and then generalised to the issuer."* The correct grade for that row is **`WITHHELD`, not `CLEAN`** | `002/artifacts/IRDM/2026-09-18_1500_recent-quarter_methodology.md` §8 | **`WITHHELD`** |
| **DA-24 at IRDM: `REFUTED`, discharged both directions.** Exactly **two** arcs into `OperatingIncomeLoss` (revenue **+1**, `CostsAndExpenses` **−1**); exactly **three** into `NetIncomeLoss`. **No disposal/sale-gain arc exists** | same §8 | **`REFUTED`** |
| **DA-25 at IRDM: `NOT TESTABLE — kind 5`** (ingestion absence of a datum class). The ARPU definition **is filed** (10-Q p.25), but subscribers appear **only as MD&A prose** (`2,627,000` vs `2,483,000`, **+144,000 or 6%**) and are **never XBRL-tagged** → zero by construction | same §8; `002/artifacts/IRDM/2026-09-18_1500_competitive_methodology.md` §6 | `UNRESOLVABLE-FROM-PLATFORM` (kind 5) |
| **DA-26 CONFIRMED ×2 at IRDM** — the metrics block's Q4-2025 row carries the **FY2025 annuals** (871,659 / 235,980) and Q4-2024 carries the **FY2024 annuals** (830,682 / 200,384), against derived quarterlies 212,940 / 55,249 (**4.094×** / **4.271×** off) | same §8 | Row + annual values `DEMONSTRATED`; ratios `DERIVED` |
| **DA-27 does not fire and DA-28 is `NOT TESTABLE — kind 6` at IRDM** (SEC coverage opens **2022-02-17**; the IPO falls outside it) | same §8 | not-tested, with a named kind |
| ⚠️ **`validate_calculation` has FOUR demonstrated failure modes**: `pass` on a wrong-signed value; `pass` when **both** sides were stripped; **ZERO ROWS** on a filed concept; and a **93% false-positive rate when it fails**. **"A pass is not evidence about sign or contamination. `computed` may not be cited as a derivation, and `reported` is not definitionally the filed value."** At SATS it returns **`pass` on a value ~4 orders of magnitude away** | `002/_cross/validation-ledger.md` §4.2 #18; `002/artifacts/SATS/2026-09-18_1500_risk_methodology.md` §5 | `DEMONSTRATED` failure modes |
| **DA-29's mechanical test**: *"if any term in a reconciliation appears NOWHERE in the source, the check is a BACK-SOLVE — and a back-solve closes exactly, so it cannot be caught on the closure."* **IRDM passes it: every term of every reconciliation is on a named page** | `002/artifacts/IRDM/2026-09-18_1500_recent-quarter_methodology.md` §7 | `DEMONSTRATED` |
| **DA-30 at IRDM — four competing bases named before use**, including **capex on three bases** (cash paid **51,791**; accrual **59,712**, `+7,921` received-not-paid; **+2,073** capitalised SBC) and a **P11 discontinuity with no single basis flag**: Q2 2026 is `standalone_pre_merger` *and* pre-Aireon-consolidation | same §6 | `DEMONSTRATED` (basis establishment) |
| **DA-30's self-binding rule — inherited verbatim:** *"every figure carries its issuer AND its basis in-line, and no percentage is presented whose DENOMINATOR has not been named."* | `002/_cross/validation-ledger.md` frontmatter | Rule (inherited) |
| **The sign-clearance rule 006 applies:** any clearance of a sign defect must name **the concept, the weight, and a negative-filed instance** — or be recorded **`UNEXERCISED`** | `002/artifacts/SATS/2026-09-18_1500_risk_methodology.md` §3 | Rule (inherited) |
| ⚠️ **SATS: the contaminant is a non-cash 5G-Network IMPAIRMENT CHARGE, not a sale and not a gain.** Founding instance **16,481,468** thousand (Q3 2025) = Wireless **16,199,344** + BSS **282,124**; plus **1,150,543** (Q4 2025) = **17,632,011** for FY2025. **The licences are still on the balance sheet at 34,550,802 thousand** — *"Spectrum gains" is REFUTED* | `002/artifacts/SATS/2026-09-18_1500_risk_methodology.md` §1.1, §7 | `DEMONSTRATED` / **`REFUTED`** (the gain) |
| **Only 32.8% (5,784,779 of 17,632,011) of the charge struck regulatory authorisations** — the spectrum licences. The remaining **67.2% (11,847,232)** struck prepaids, PP&E, ROU assets and exit costs. **A thesis that reads 17,632,011 as a spectrum write-down over-reads it by 11,847,232 thousand** | same §1.1 | `DEMONSTRATED` |
| **Of 15 filed SATS operating-income values verified, 5 are contaminated and 10 are not** — and the contamination runs in **both directions**. Largest single restatement: Q3 2025 **filed (460.46)% → (4.44)% ex-item**, a **456.02 pp** swing | same §1.2 | `DEMONSTRATED` |
| **Second-order contamination — D&A relief is a PERMANENT level shift, not removable by add-back.** Other-segment D&A fell **303,929 → 11,305 = (292,624), (96.3)%**; the Q1 2026 YoY bridge closes at **+480,979**, of which DA-24 effects contribute **+321,732 (D&A) + 66,159 (credit) = +387,891 = 80.6% of the entire YoY improvement** | same §1.3 | `DEMONSTRATED` |
| **DA-23 and DA-24 co-occur INSIDE ONE FIGURE.** Correct ex-item OI = `392,847 − 66,159 = 326,688`; a reader de-contaminating with the **served** fact computes `392,847 + 66,159 = 459,006`. **Total error 132,318 = 2 × 66,159** = 3.61% of Q1 2026 revenue | same §1.4 | `DEMONSTRATED` |
| **The same tag, two verdicts, one series** — `sats:AssetImpairmentChargesAndOther`: FY2025 filed **+17,632,011** → served correct; Q1 2026 filed **(66,159)** → served **+66,159,000 = STRIPPED** | same §1.4 | `DEMONSTRATED` |
| **DA-30 fifth instance — segment-attribution discontinuity.** Q3 2025 10-Q: Wireless **16,199,344** + BSS **282,124**, **no Other column**. FY2025 10-K: Wireless **—**, BSS **1,529,982**, Other **16,102,029**. Reconciliation exact: `16,199,344 + (−97,315) = 16,102,029`. **Any "SATS Wireless segment operating loss" must name its basis or it differs by 16,199,344 thousand between two filings of the same issuer for the same year** | same §1.5 | `DEMONSTRATED` |
| **SATS deal terms as filed** — Seller Notes outstanding at 2026-03-31 **$9.821bn**, secured by the **AWS-4 and AWS-3 licences**; Equity Amount *"up to $8.5bn in SpaceX's Class A Common Stock, valued at $212 per share"*; Spectrum Acquisition Closing *"expected to occur on or about **November 30, 2027**"*; Interim Debt Service *"approximately $2bn"*; **$414M** cash interest paid. Amended: **15 MHz of AWS-3 (1695–1710 MHz) for $2.6bn** in stock; total consideration **"$17bn → approximately $20bn, with up to $11bn in SpaceX Class A"**. AT&T: **$22.650bn** cash on closing | same §1.6 | `DEMONSTRATED` |
| **BOTH SATS purchase agreements are PENDING, no gain recognised, and they are "not contingent on each other."** Completion is not assured *"on the terms or timeline currently contemplated, or at all."* `deal_security_basis: standalone_pre_merger` | same, frontmatter + §1.6 | `DEMONSTRATED` |
| ⚠️ **Carry-forward C1** — restate 003's SATS margin from `10.7%` to **8.91%** ex-DA-24, and correct its "asset-sale gain" to the 5G-Network impairment charge with a **66,159 thousand** settlement credit. **C2** — 001's `~$27B` must be **withdrawn or re-based**; `$19.6B` must be **re-graded `DERIVED`**; *"both are recorded here, neither may be carried silently."* **C3** — any ex-item series must carry the **second-order** flag. **C7** — PIL-4/5/6 must be carried as **proxy-tested**, not pending-and-waiting: *"a downstream thesis that sizes against them is sizing against something that cannot happen."* | same §7, carry-forwards | Instructions — **006 discharges C1, C2 and C3 in §0.1 and §0.2; C7 in §1b P4** |
| **IRDM's licence carrying value — RESOLVED.** *"Spectrum and licenses"* is an **indefinite-life intangible, net $14,030K**, unchanged and unimpaired at both **2026-06-30** and **2025-12-31** — **1.6% of FY2025 revenue**. It answers 006's Q-3 for the buy side, and the answer is a finding: **the balance sheet carries the L-band licence at 1.6% of revenue while the observed transaction market prices a spectrum block at multiples of it** | `002/artifacts/IRDM/2026-09-18_1500_competitive_methodology.md` §4 (10-Q p.11) | `DEMONSTRATED` (cells) |
| **IRDM licence inventory — the only licence-inventory datum in the corpus:** **8.725 MHz** contiguous L-band (1617.775–1626.0 MHz); **200 MHz** K-Band (23 GHz) inter-satellite; **400 MHz** Ka-Band feeder; AIS **156.0125–162.0375 MHz**; ADS-B **1087.7–1092.3 MHz**; ITU country codes **8816 / 8817** | same §4 (10-K p.26) | `DEMONSTRATED` (prose) |
| **The excluder branch, 3-for-3 and 0-for-1.** SpaceX acquires **50 MHz** S-band from EchoStar; AST to lease/acquire Ligado's L-band; AT&T acquires spectrum from EchoStar — **all three are incumbent dispositions, the branch PIL-6 excludes.** The one *grant*-shaped event (FCC's 2020 Ligado waiver, **10 MHz** — **wider than IRDM's entire 8.725 MHz L-band allocation**) went to an **incumbent MSS licensee** and is **not final** | same §5 | `DEMONSTRATED` |
| **The corpus is reporter-conditioned, and the condition selects AGAINST the falsifier's positive branch.** An SEC filing records a spectrum transaction only when an SEC filer is a party — and every such party is acquirer or incumbent vendor. **So the absence of a primary-grant event is not evidence that the falsifier survives** | same §5 | `DEMONSTRATED` (structural) |
| **Market share is DOUBLE-BLOCKED** — no `us-gaap` concept exists (`search="MarketShare"` → **0**; `"Spectrum"` → **0**; `"Subscriber"` → **0**) **and** no issuer in the set discloses a quantified share or MSS TAM. Remedy = a licensed market-research dataset | same §6 | `UNRESOLVABLE-FROM-PLATFORM` (datum class, kind 5) |
| **The three disposition situations, distinguished** — `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (the disclosure does not exist: a finding about **the world**) · `UNRESOLVABLE-FROM-PLATFORM` (public but unreachable: a finding about **the instrument**) · **`REACHABLE-BUT-NOT-RECORDABLE`** (proposed at A22, not yet registered: the datum is reachable and **the contract cannot record it** — a finding about the programme's own rules, *"the one that cannot be resolved by any amount of research"*) | `002/_cross/validation-ledger.md` §5.2; `002/artifacts/SATS/…_risk_methodology.md` §2.1 | Class definitions (inherited framework) |
| **PIL-6's falsifier for 001's spectrum pillar is `UNRESOLVABLE-FROM-PLATFORM`, kind 5** — classified identically and independently at IRDM and at SATS. Named resolving sources: **FCC IBFS** and **ITU Space Network List / Master International Frequency Register** | `002/artifacts/IRDM/…_competitive_methodology.md` §2; `002/artifacts/SATS/…_risk_methodology.md` §2.2; ledger §2.2 | `UNRESOLVABLE-FROM-PLATFORM` (kind 5) |
| **`threshold=0` makes PIL-6's falsifier worse, not easier** — combined with F6-iii it is not merely untestable here, **it is UNCLEARABLE**: no quantity of null evidence can discharge it, because the corpus supplying the nulls structurally omits the positive. Report **`UNEXERCISED` on F6-iii, not `CLEAN`** | `002/artifacts/IRDM/…_competitive_methodology.md` §2, §5 | `UNEXERCISED` (stated) |
| **VSAT — the comparator carries the defect too, and the served row is 3.97× wrong.** VSAT returns **10 pass / 1 warn / 19 fail = 63.3%** against SATS's 34.6%, and **11 of VSAT's 19 failures carry the `2 ×` fingerprint exact to the thousand**. Its Q1 slot carries a **TWELVE-MONTH duration**, overstating **3.97×**; the correct quarter is **`DERIVED` 1,171,288** | `002/_cross/validation-ledger.md` §4.2 #19–20 | `DERIVED` — explicitly |
| **A clean tie-out is not evidence of a stable boundary** — VSAT intersegment revenue collapsed **71,592 → 9,905 = −86.2%**; one segment produced **112.5%** of the entire consolidated improvement | same §4.2 #22 | `DERIVED` |
| **Relative-size benchmark, DA-30 basis named:** VSAT FY2026 **$4,640,280K** (2025-04-01 → 2026-03-31); IRDM FY2025 **$871,659K**; GSAT FY2025 **$272,986K**. **VSAT ÷ IRDM = 5.32×; IRDM ÷ GSAT = 3.19×.** Periods are **not coterminous** (VSAT's FY ends 31 March) and the bases are heterogeneous — **this is not a market share** | `002/artifacts/IRDM/…_competitive_methodology.md` §3 | `DERIVED` — explicitly |
| **ASTS is a spectrum COUNTER-PARTY, not a named competitor.** It enters IRDM's competitive field only via the **regulatory** route (Ligado's Chapter 11 agreement to lease and potentially transfer its satellites, ground assets and L-band spectrum). *"Treating ASTS as a named competitor would be a comparison the issuer did not make."* ASTS's FY2025 10-K exists (`sec125`) — **reachable**, and its figures were never read | same §3, §5 | `DEMONSTRATED` (text location). ⚠️ **No ASTS financials, licence inventory or defect status exist anywhere in 002** — any §0 row beyond this would be an invention |
| **GSAT is fully platform-reachable and was read, not assumed** (`sec128` FY2025 10-K pp.10–11). GSAT and IRDM **mutually attest** the same competitor set: *"Our largest global competitors are Viasat, Iridium and ORBCOMM"*; GSAT names *"SpaceX's Starlink, Amazon Leo and AST SpaceMobile"* as newer systems | same §5 | `DEMONSTRATED` |
| **IRDM's Aireon secondary event, and the unconstructibility finding.** Aireon closed **2026-07-02** (period end 2026-06-30 — a **two-day** interval) for **~$366.7M**; equity-method carrying value **$36.3M**; **~39.5%** fully diluted; the close adds **$438.1M** of new/newly-consolidated debt = **3.83× FY2025 net income**. **Aireon-attributable revenue recognised by IRDM from Aireon (~$32.8M/yr) becomes intercompany and eliminates on consolidation while Aireon's external revenue is added for the first time — so a post-close benchmark cannot be constructed from the pre-close filings in either direction** | same §7 (10-Q pp.18, 20) | `DEMONSTRATED`; the unconstructibility is the finding |

### 0.3 Inherited from 003 — the curve, the value-pool map, and the GSAT sign

003 supplies the **operator margin ladder** 006 prices off, and it supplies the correction that
this spec previously carried in its stale form.

| Inherited result | 003 artifact | Grade |
|---|---|---|
| ⚠️ **GSAT Q2 2026 filed operating margin is −7.37%** — an operating **LOSS** of **$(4,775) thousand** on revenue **$64,772 thousand**. The filing prints `(7.37)%`. **Prior year was +9.15% (`6,146 ÷ 67,148`) — a −16.5 point swing** | `003/_cross/value-pool-map.md` line 888; `003/artifacts/GSAT/2026-09-19_1515_risk_methodology.md` §"The finding" | `DEMONSTRATED` |
| **The component identity is INCLUSIVE because the issuer removed the choice** — GSAT files **no gross-profit line**, so the pairing is `64,772 − 69,547 = (4,775)` **exact**, where 69,547 = the six filed operating-expense lines (23,602 + 3,395 + 23,025 + 2,723 + 0 + 16,802). `gross_profit_bound: UNEXERCISED` | `003/_cross/value-pool-map.md` lines 891–899 | `DEMONSTRATED` (identity) / **`UNEXERCISED`** (the bound) |
| **What the platform serves**: `+4,775,000` — a sign strip **plus a systematic 1,000× unit offset**, across **7 `OperatingIncomeLoss` facts** (Q2 2026 +4,775,000; 6M 2025 +2,355,000; FY2024 +949,000; FY2023 +165,000; plus three derived rows). **Deviations reach ≥18 cells across 4 concepts, including a balance-sheet cell** (`RetainedEarningsAccumulatedDeficit` served `+2,206,570,000` against filed `$(2,206,570)` thousand) | `003/artifacts/GSAT/2026-09-19_1515_risk_methodology.md` lines 199–206, 311–324 | `DEMONSTRATED` |
| **The detector that needs no filing — monotonicity.** Served **Q2 2026 (+4,775) > served 6M 2026 (+3,395)**; also Q1 2025 (+8,501) > 6M 2025 (+2,355) and Q3 2024 (+9,434) > 9M 2024 (+3,300) | same, lines 180–185, 241–251 | `DEMONSTRATED` |
| **The corrected operator margin ladder** (3M basis unless noted): SPCX `Connectivity` **+38.59%** · SATS `Pay-TV` **+20.55%** · **IRDM +15.10%** (ex-transaction-costs **21.45%**) · SATS `Broadband and Satellite Services` **+13.40%** · SATS consolidated **+10.71%** · SPCX consolidated **−1.83%** · SATS `Wireless` **−3.72%** · **GSAT −7.37%** · LUNR **−22.86%** · RKLB **−24.57%** · **PL −37.06%** (gross margin **53.53%**, the universe's best) · YSS **−44.64%** · SPCX `AI` **−49.08%** · SPCX `Space` **−56.34%** · FLY **−80.90%** (the floor) · SATS `Other` **−95.95%** as reported / **−168.66%** ex-DA-24 | `003/_cross/value-pool-map.md` §4; `003/_cross/launch-cost-curve-value-migration_synthesis.md` §3 | `DEMONSTRATED` — **the anchor rows are FY basis and the operator rows are 3M; the two ends are not on the same basis** |
| **The ladder is BIMODAL, not monotone — high at both ends, negative through the middle.** ANCHOR (a) **holds at 2.02×** (component suppliers mean **22.76%** ÷ prime integrators mean **11.25%**, both FY basis). ANCHOR (b) is **FALSIFIED**: the worst verified margin is FLY's **−80.90%, a manufacturer**, 24.56 pp below the next-worst row — **not** the single-customer operator at −7.37% | same, lines 1143–1197; synthesis §3 | `DEMONSTRATED` |
| ⚠️ **IRDM's 15.10% and 23.17% are CONFIRMED — but the DIRECTION claim is corrected, and this changes P1's arithmetic.** On the fiscal-year basis IRDM's margin **RISES**: **24.12% (FY2024) → 27.07% (FY2025)**. *"The direction of the 'trend' therefore depends on the period basis chosen, and the only basis on which it is a decline is one contaminated by non-recurring deal costs."* **63.8% of the $22,417 thousand SG&A increase is Rocket Lab Merger Agreement and Aireon transaction costs** ($14.3M); on the six-month basis **46.2%** ($15.0M of $32,443 thousand). Ex-transaction-cost margin **21.45%** | `003/artifacts/IRDM/2026-09-19_1515_risk_methodology.md` lines 138, 152–155; `003/_cross/value-pool-map.md` lines 818–824, 834–837 | `DEMONSTRATED` |
| **IRDM's ladder admission is `UNEXERCISED`**, pending the component re-run 002-F8 requires. The served `operating_income` carries a **DA-29 signature**: `computed −51,791,000` against `reported +51,791,000` | `003/_cross/value-pool-map.md` lines 851–855, §8 item 11 | **`UNEXERCISED`** — not a pass |
| **DA-30 at IRDM, worse than at any other name:** every served quarterly margin **divides by a single `$200,000` thousand denominator** — the Aireon hosting-agreement revenue **ceiling** (`srt:MaximumMember`, six-month period). **8 of 8 reproduce to the basis point.** *"IRDM's served margins do not measure IRDM and NONE of them is admissible to this map."* | `003/_cross/value-pool-map.md` lines 838–843 | `DEMONSTRATED` (the defect) |
| **The tier's two observed deal multiples, and one is `UNRESOLVED`.** GSAT **41.55×** ($11,660.7M ÷ $280,642K TTM; band 41.4×–41.6×). **IRDM's `8.3×` is NOT sourced in IRDM's own filing set** — IRDM's artifacts give **~13× revenue** ($8.0B EV ÷ $601.8M FY2025) and **3.4× total assets**; the armed reproduction gives **≈6.5× equity-only** and **≈8.5× EV**. **Class: `UNRESOLVED`, band 6.5×–8.5×** | `003/_cross/value-pool-map.md` lines 1257–1273, §8 item 3 | `DERIVED` / **`UNRESOLVED`** |
| **The contrast, and its direction is basis-invariant:** the demand owner pays **≈41.4–41.6×** for the **unprofitable** operator; the launcher pays **≈6.5–8.5×** for the **profitable** one — against a **22.5-point** margin differential in the **opposite** direction | same, lines 1269–1273 | `DERIVED` |
| **SPCX's two-ladder inversion** — `Space` holds the **highest segment gross margin at 65.80%** and the **worst operating margin at −56.34%**, a **122.14 pp** swing decomposed exactly as **R&D 111.85 pp + SG&A 10.29 pp** | `003/_cross/value-pool-map.md` lines 390–396; synthesis line 169 | `DEMONSTRATED` (segment gross profit is `DERIVED` — SPCX files no segment gross-profit subtotal) |
| **The RKLB/IRDM gate chain, as filed** — see §1b P4 for the full checklist. Source rows: merger agreement dated **2026-06-28**, $54.00/share, **$27.00 cash + RKLB stock**, **±25% value-preserving collar** ($67.50–$112.50); **$223.6M termination fee**; **$3.6B 364-day senior secured bridge**; RKLB needs **>$3.0bn** cash and **~$1.8bn** to refinance; **DCSA mitigation** named on the acquirer's side; **IRDM's ITU filings are made by the United States on its behalf** | `003/artifacts/IRDM/2026-09-19_1515_risk_methodology.md` §6 (lines 362–395); `003/artifacts/RKLB/2026-09-19_1515_risk_methodology.md` §4–5 | `DEMONSTRATED` (conditions, prices, parties) / `DERIVED` (the FOCI reading) / **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** (the bridge's drawn pricing) |
| **Gaps this thesis inherits, stated rather than discovered later.** 003 carries **no ASTS row and no VSAT row** — neither appears in the ladder or among entries E-01…E-16. 003's map **does** carry a PL row (**−37.06%**). **RKLB files no segment operating margin on any basis and has filed that it does not review one** — that basis is `UNRESOLVABLE-FROM-PUBLIC-SOURCES` **permanently**: *"This is not 'pending'; it is non-formable."* | `003/_cross/value-pool-map.md` lines 511–517, §8 item 2 | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` |

### 0.4 Inherited from 004 — the operating-leverage benchmark

**004 is the programme's only valuation of SPCX's Connectivity segment, and its comparability
boundaries name 006 as a permitted consumer.** What 006 may price off is bounded, and the
bound is inherited:

| Inherited result | 004 artifact | Grade |
|---|---|---|
| **There is NO per-segment enterprise value.** *"No point estimate. Every regime is a `MODELED` range."* **006 cannot price off a Connectivity EV; it prices off the filed segment financials and the assigned regime** | `004/artifacts/SPCX/2026-09-19_sotp-valuation_methodology.md` §5; `004/artifacts/SPCX/2026-09-19_sotp-valuation_defaults.md` line 110 | `MODELED` |
| **Connectivity: revenue $4,291M** (Q2 2026, **54.9%** of consolidated, **+65.8%**); **operating income $1,656M** (**+38.59%** margin); cost of revenue **$2,060M**; identity `4,291 − 2,635 = 1,656` closes exactly | `004/artifacts/SPCX/2026-09-19_sotp-valuation_methodology.md` §1, §3; `004/_cross/anchor-sotp.md` §2 | figure filed; **row regime `MODELED`**; segment gross profit `DERIVED` (SPCX files no segment gross-profit subtotal) |
| **Connectivity is the only positive segment and the sector's benchmark**: operating income **+79.4%** on revenue **+65.8%** = a **+13.6 pp rate spread**; channel mix Enterprise & Government **+108.3%** vs Consumer **+44.4%** — the managed channel grew **2.4× faster** | `004/artifacts/SPCX/2026-09-19_sotp-valuation_methodology.md` §3; `004/artifacts/SPCX/2026-09-19_growth-strategy_organic-growth-drivers-analysis.md` §1 | `MODELED` (spread) / `DEMONSTRATED` (channel fact) |
| **The permitted reference, and its boundary:** Connectivity's regime is *"Margin-anchored, `MODELED`"*, **cross-checked against terrestrial broadband, not satellite peers** — because **the comparability partition admits 0 of 11**, and *"❌ No satellite peer admitted. IRDM/GSAT are `P11` — price is a spread; ASTS/VSAT `PARTIAL`."* **Permitted consumers: 006, 009** | `004/_cross/anchor-sotp.md` §2, §6; `004/artifacts/SPCX/2026-09-19_sotp-valuation_retrieval-scope.md` line 58 | `MODELED` |
| **"Verifiable ≠ admissible."** IRDM and GSAT remain excluded from the anchor's peer set **even though they are priceable** — *"a live multiple on a P11 spread is priced and still inadmissible as a fundamental."* **006 does not re-open the class**: it values them as deal securities and re-underwrites the break leg from its own basis B, never by importing a peer multiple | `004/artifacts/SPCX/2026-09-19_comps_retrieval-scope.md` line 107; `004/_cross/tier0-spacex-anchor_synthesis.md` | `DEMONSTRATED` |
| **Live market data now exists — a change of state the tier does not share.** SPCX **$152.71** (close observed 2026-09-18, source `nasdaq`, keyless); market cap **$2.0718T** `DERIVED`; **Market Data Stage is `per_row`** (two rows at `late`, the rest at `none`). **006's rows remain `none`** — no price series exists for any Tier 2 name | `004/artifacts/SPCX/2026-09-19_sotp-valuation_methodology.md`; `004/_cross/tier0-spacex-anchor_synthesis.md` line 26 | `DEMONSTRATED` |
| **The market-derived multiple, as a benchmark and not a value:** **312.8×** = `$2.0718T ÷ $6,624M` annualised Connectivity operating income — *"the whole already requires the one profitable segment to carry ~313×."* `r − g = 0.32%` | `004/_cross/anchor-sotp.md` §3; `004/artifacts/SPCX/2026-09-19_reverse-dcf_methodology.md` §1 | `DERIVED` |
| **Segment capex, filed (Note 18, 3M ended 2026-06-30):** Space **$1,174M (6.4%)**, **Connectivity $1,367M (7.4%)**, AI **$15,828M (86.2%)**, total **$18,369M**. *"Connectivity, the only profitable segment, receives 7.4%."* ⚠️ **004's own segment-attribution ledger still carries a row claiming segment-level capex is `UNRESOLVABLE-FROM-PUBLIC-SOURCES`; the synthesis RETRACTED it. 006 inherits the figures, not the retracted row** | `004/artifacts/SPCX/2026-09-19_sotp-valuation_methodology.md` §1; retraction box in `004/_cross/tier0-spacex-anchor_synthesis.md` | `DEMONSTRATED` |
| **AMZN is carried at 006 by 004's own disposition.** *"Amazon Leo — competes with Connectivity, not with the launch or AI segments. **Carried at 006**."* | `004/artifacts/SPCX/2026-09-19_risk_technology-disruption-risk-analysis.md` line 97 | `DEMONSTRATED` |
| **004's trigger T-5 is 006's event.** *"Any of IRDM, GSAT, RKLB ceasing to be a deal security"* — a terminated merger — is the anchor's first admissible satellite comparator. **006 owns the event that unblocks the anchor's peer set** | `004/artifacts/SPCX/2026-09-19_sotp-valuation_triggers.md` line 78 | `MODELED` |
| **The anchor's own DA-23 hazard, which is why the tier's margins are recomputed from components rather than read**: the served layer returns `OperatingIncomeLoss: +143,000,000` against a filed **`(143,000,000)`**; **16 of 20 served SPCX facts are sign-stripped** | `004/_cross/anchor-sotp.md` §5.1 | `DEMONSTRATED` |

### 0.5 What 001–004 did not do — and why this thesis exists

001 covered Tier 2 through PIL-6 and closed the *premise* two-sidedly: the sell side
(EchoStar realised the price) and the buy side (IRDM holds it profitably). 002 validated the
data underneath it and found the platform's extraction layer defective in ways that change
which figures may be quoted at all. 003 mapped the value pool and corrected the ladder. 004
valued the anchor and named 006 as a permitted consumer of the Connectivity reference. **None
of them asked the investment question.** Three things were left on the table, and they are
this thesis's entire scope:

1. **What are these businesses worth?** The licence has an observed price and the operating
   businesses have filed margins, and nobody has put the two side by side.
2. **What does the D2D transition do to them?** Direct-to-cell could commoditise the
   service layer while *raising* the value of the licensed layer — a claim never tested.
3. **What do the two deal spreads price?** Two of the tier's names are P11 securities, so a
   quarter of the tier is not an operating business at all.

**006 is the segment thesis. It inherits the premise and the validation, and it owns the
valuation, the transition and the deal mechanics.** The Tier 2-specific contested figures it
must convert are enumerated below.

---

## 0b. Validation queue — the Tier 2 figures this thesis owns

**002 owns the cross-cutting denominators and physics inputs** (Electron's 300 kg, Falcon 9's
22.8 t, F2's unsourced constants, the DA-23 universe census). **006 owns the Tier 2-specific
contested figures** and must not re-open 002's. Under P4, `MODELED` can never satisfy a
falsifier — so an unconverted figure here is a pillar that cannot fire. **Owner labels are
updated to the five-pillar structure at the re-cut: the former P4 (deal mechanics) and P5
(gate chain) are now one pillar, P4; the former P6 (queue scorecard) is now P5.**

| Contested figure | Grade now | Why it is contested | Owner | The source that resolves it |
|---|---|---|---|---|
| ⚠️ **the `~$27B` SATS licence gain and the 1.8× ratio** | **`REFUTED` — withdrawn** | `~$27B` does not reproduce; no filed figure equals it. The 2025 item is a **non-cash impairment charge of 17,632,011 thousand**, the licences remain on the balance sheet at **34,550,802**, and no gain was recognised because nothing closed (carry-forward C2) | P2 | **Discharged in §0.1/§0.2.** The replacement input is the **filed spectrum carrying value** (net 34,550,802; gross 39,885,275) and the **filed deal consideration** ($17bn → ~$20bn; AT&T $22.650bn) |
| **the $19.6B mark used as a *unit* price** | **`DERIVED`** — a transaction value, **not** usable as $/MHz-pop | DA-17: the coverage denominator for each block is undisclosed, so the mark prices one specific combination and cannot be transferred to another licence without a denominator. **And the $2.6B AWS-3 amendment buys 15 MHz in 1695–1710 MHz — a different block from the one the headline names** | P2 | FCC licence files and the coverage footprint per block — **platform-unreachable** |
| **IRDM's licence carrying value** | ✅ **RESOLVED** — net **$14,030K**, indefinite-lived, flat and unimpaired at both dates, **1.6% of FY2025 revenue** | The answer is itself a finding: **the balance sheet carries the asset at a rounding error against the transaction market's price for spectrum.** It closes Q-3 for the buy side and creates a third basis | P2 | Discharged at §0.2; 006 reports it as basis (C) of the SOTP |
| **GSAT's licence carrying value** | **unverified** | If GSAT's licence sits on the balance sheet as an indefinite-lived intangible it is an independent valuation basis; if it is aggregated, it is not. IRDM's resolves; GSAT's does not | P2 | GSAT 10-K intangible-asset notes and purchase accounting |
| ⚠️ **the two deal prices and their conditions** — IRDM **$54.00/sh** (RKLB), GSAT **$90.00/sh** (AMZN, agreed 2026-04-13, ~$11.57B) | **`DEMONSTRATED` for IRDM** (filed conditions, collar, termination fee, bridge); **`CLAIMED` for GSAT** | IRDM's merger agreement is filed with conditions, a ±25% collar, a **$223.6M** termination fee and the **$3.6B** bridge. **GSAT's is not yet read to the same depth.** The bridge's **drawn pricing** is `UNRESOLVABLE-FROM-PUBLIC-SOURCES`: *"$3.6B is committed; the drawn pricing is not stated"* | P4 | GSAT's merger agreement and proxy; the RKLB bridge's pricing exhibits |
| **ASTS's D2D capacity, coverage and commercial-service claims** | `CLAIMED` (issuer) — **reachable, unread** | No filed revenue line has been read; the platform's `sec_filings` counter reads 0 while **142 source documents** exist (the bulk partial-view trap), and 002 confirms the FY2025 10-K is reachable at `sec125` **with no figures read** | P3, P4 | ASTS 10-K / 10-Q, and a first filed service-revenue disclosure |
| **VSAT's GEO/LEO mix and government-satcom backlog** | **unverified — and the served data is actively misleading** | `PARTIAL`; the sector must be assigned manually before any sector-aggregate constraint evaluates (PROGRAM.md §7). **And 002 measured the comparator defect: 19 of 30 rows fail, 11 with the `2 ×` fingerprint, and the Q1 slot carries a twelve-month duration overstating 3.97×** | P2, P3 | VSAT 10-K segment tables, read on a component identity — **never from the served metrics block** |
| ⚠️ **"connectivity has demonstrated operating leverage" as a Tier 2 property** | `DEMONSTRATED` **only at the anchor** | The entire evidence base is one segment of one issuer (SPCX Connectivity). **003's corrected ladder now shows the tier's own names at −7.37% (GSAT) to +15.10% (IRDM), and the geospatial names at −37.06% (PL)** — so the inherited claim is not merely unproven in the tier, it reads **against** the tier on the 3M basis | P1, P5 | IRDM, GSAT, SATS and the geospatial segment-level margin series |
| **PIL-6's falsifier** (`new_entrant_primary_spectrum_or_slot_grant_without_incumbent_acquisition`) | `UNRESOLVABLE-FROM-PLATFORM`, **kind 5** — and **`UNCLEARABLE` at `threshold=0`** | The registers are public, free and outside the reachable corpus; worse, the corpus is **reporter-conditioned against the falsifier's positive branch**. 002: *"Report `UNEXERCISED` on F6-iii, not `CLEAN`"* | P4 | **not re-attempted** — 006 builds a reachable proxy instead (§1b P4) |
| 🆕 **the geospatial trio's licensed-asset share** — is an Earth-observation and downlink licence >50% of attributable EV at PL, BKSY or HAWK? | **untested — new at the re-cut** | This is the question that separates *"the licence is scarce"* from *"the licence is merely required"*. Without it P2's claim is single-sided: every prior member of this tier held a scarce licence, so the tier could not distinguish the two | P2 | PL / BKSY / HAWK 10-K balance-sheet intangible notes, segment disclosure, and filed licence inventories |
| 🆕 **HAWK's capital structure — four non-agreeing share counts (4.2M–98.0M), EPS bridge failing by 72%** | **`DA-28` candidate**, extract inconsistent three independent ways | Any EPS- or share-count-based screen **false-positives on recent listings**; a **listing-date guard is mandatory**, and no DA-23 detector may be run on HAWK without one | P5 | HAWK 10-K cover and equity note; the FY2026 annual once filed |
| 🆕 **BKSY's `sector` field is unassigned** | **precondition, not an assumption** | Reclassified from `PARTIAL` to READY at v1.6.0 with `sector` unassigned on the served record. **No sector-aggregate constraint evaluates until it is assigned by hand, and the assignment is recorded in every artifact's frontmatter** | P5 | PROGRAM.md §7; the constitution's coverage audit |

> **`blocking` set for delivery: the GSAT licence carrying value, the geospatial licensed-asset
> share, and BKSY's sector assignment.** P2 cannot be delivered without them. Everything else
> is `warn` and is reported as a bound rather than resolved to a point, per the §1c standing rule.

---

## 1. Research Question

**Connectivity is the only space sub-sector with demonstrated operating leverage. Is
that leverage durable — or is it a temporary consequence of a licensed asset that
cannot be replicated and will be repriced?**

The question is uncomfortable, and the inherited numbers state it better than any
framing: **IRDM's operating margin fell from 23.17% to 15.10% year over year while revenue
grew 3.8%** — an 8.07-point compression on a licence that cannot be duplicated. **And 003
found the compression is 63.8% non-recurring deal cost** (Rocket Lab Merger Agreement and
Aireon transaction costs, $14.3M of a $22.417M SG&A increase): ex-those, the margin is
**21.45%**, and on the fiscal-year basis IRDM's margin **rises**, 24.12% → 27.07%. Meanwhile
**the tier's own operator ladder runs from −7.37% (GSAT) to +15.10% (IRDM)**, against the
anchor's **+38.59%** — and EchoStar's spectrum licences sit on its balance sheet at
**34,550,802 thousand** while the same assets were impaired by **16,481,468** in a single
quarter. The asset was repriced; the businesses operating on top of it were not.

So the tier poses two opposed readings, and this thesis exists to decide between them:

- **Reading A — the licence is the asset and the business is a thin margin on it.**
  Then the correct valuation is an SOTP that splits a durable, priced licence from a
  competitive service business, and the market's single blended multiple for these names
  is wrong. D2D *raises* the licence's value even as it compresses service pricing.
- **Reading B — the licence is the asset and the business is now being priced by D2D.**
  Then the licence is not a moat but a **toll that is being routed around**: ASTS and
  Starlink direct-to-cell attack the service layer from orbit, and the incumbent licence
  is what the attacker *rents or buys* (Apple holds ~20% of GSAT and rights to **85%** of
  its network capacity; AMZN pays **$90.00/sh** for the rest of it).

Both readings agree the licence is real — 001 settled that. They disagree about **who
captures the rent**, which is the only question a valuation can answer.

**The re-cut adds the discriminating case, and it is the reason this question is now
answerable rather than merely stated.** PL, BKSY and HAWK operate constellations under
licences that are **granted on application and contested**, not allocated once and closed.
They share the licensed-orbital-and-data-product structure the question tests, so running it
across both groups separates the two readings mechanically: if the licence dominates value
only where the licence is scarce, Reading A is a statement about **L-band**, not about
constellations; if it dominates value everywhere, the tier's returns are a regulatory artefact
regardless of the competitive layer on top.

### Why this thesis exists at all

The alternative was to leave Tier 2 covered by PIL-6's premise and move on. Three
concrete costs follow from that:

1. **A quarter of the tier would be underwritten as a business.** IRDM and GSAT are P11 deal
   securities. Under P11 their price tracks a spread, their binding constraint is
   `REGULATORY_SPECTRUM`, and on a break the standalone case is **not** the
   pre-announcement case. A thesis that values them on fundamentals is valuing something
   that is contractually ceasing to exist.
2. **The tier's best-evidenced fact would go unexploited.** The ~$19.6B mark is the only
   observed price of spectrum in the universe. Without an attribution that applies it,
   the mark is an anecdote rather than a valuation input.
3. **A live falsifier would stay un-evaluated.** PIL-6's falsifier needs FCC IBFS / ITU
   sources the platform does not carry. 001 split the disposition and recommended
   carrying the pillar rather than dropping it. 006 is where that split becomes a
   *method* — a reachable proxy test — instead of a note.

---

## 1b. Pillars

**Five pillars, from six.** The re-cut ended a three-way duplication: 005 P6, 006 P4 and 006 P5
each independently declared that *"what this adds is the date"* for the same FCC → ITU → DCSA
gate chain on the same IRDM/RKLB transaction, sourced from the same document — and 005 P6
repeated this thesis's break sentence verbatim. **005 P6 is deleted and its dated-consent work
is absorbed here; the former P4 and P5 are merged into one pillar with one deliverable.** The
numbering below is the post-merge numbering, and §0b's owner column has been updated to match.

### Pillar 1 — The licence is durable and the business on top of it is not, and the IRDM margin decay is decomposable by line (Priority: P1) 🎯 Minimum Defensible View

The inherited fact is a **contradiction against the tier's own thesis**: the
constitution rates Satellite Connectivity **Overweight / High** because it is *"the only
space sub-sector with demonstrated operating leverage."* Yet the tier's only profitable
constellation operator lost **8.07 points of operating margin on +3.84% revenue growth**.
001 flagged the cause as open and nominated it for Phase 6.

**The arithmetic is now two-thirds answered, and that is what sharpens the pillar.** 003
supplied the decomposition 001 did not have, and it moves most of the decline off the
operating side entirely:

```
Q2 2026 operating income     $34.008M      on revenue $225.237M  →  15.10%
Q2 2025 operating income     $50.258M      on revenue $216.906M  →  23.17%
operating-income decline     $16.250M                            →  −8.07 pts

  revenue contributed         +$8.331M   (filed: 225.237 − 216.906)
  opex increase              −$24.581M   (filed: 191.229 − 166.648)
    of which transaction costs  $14.300M  = 63.8% of the $22.417M SG&A increase
                                          (Rocket Lab Merger Agreement + Aireon)
    of which R&D step-up         $1.251M  (5.530 − 4.279)
    residual                     $9.030M  ← the pillar's actual object
ex-transaction-cost margin   $48.308M  →  21.45%   (vs 23.17% prior year)
```

**The disclosed R&D step-up explains 7.7% of the decline and the disclosed transaction costs
explain 88.0% of it. Together they leave $9.030M — 55.6% of the operating-expense increase —
that is neither reinvestment nor deal cost.** On the component arithmetic alone the decay is
**not** a reinvestment story, and it is **not** primarily a deal-cost story either.

**The claim:** the residual decline is attributable **by revenue line**, and **less than half
of it falls on the licensed-spectrum service line** — i.e. the licence's own revenue stream
holds while the competition-exposed overlay (equipment, wholesale, adjacent services) absorbs
the compression. If instead the residual is concentrated *in* the licensed-service line, then
the licence itself is being repriced, the "durable asset / weak business" separation fails at
IRDM, and P2's attribution premise must be rebuilt before it is used anywhere else in the tier.

**Why this priority**: it is the Minimum Defensible View because it decides whether the
inherited Tier 2 premise is *actionable* or merely *true*. Everything else in this
thesis — the SOTP, the D2D placement, the peer comparison — rests on the licence and the
service business being separable in the financials. It is also the only Tier 2 figure
currently **moving against** the constitution's conviction ranking, which makes it the
highest-information number in the tier.

**What counts as resolution.** A line-level attribution must come from IRDM's own
reported revenue and cost disaggregation (service vs subscriber equipment vs other, and
the operating-expense lines beneath them) — **not** from a company narrative about
"investment in growth." Two inherited limits bound it and are recorded rather than glossed:
**(a)** the SPCX-free reading is 002's, and the p.53 disaggregation explains only **46.4%** of
IRDM's revenue movement — **$21,977K (53.6%) sits outside it**, because that table is a
*service-revenue* disaggregation, not a total-revenue one; **(b)** IRDM's **served** margins are
inadmissible (DA-30: 8 of 8 divide by a single $200,000 thousand denominator, the Aireon hosting
ceiling), so the decomposition must be recomputed from filed components — which is also the
component re-run **002-F8** requires before IRDM's ladder admission can move off `UNEXERCISED`.
Where the filing does not disaggregate finely enough, the pillar defaults to the coarser
gross-profit − opex test and the limitation is recorded.

**Independently falsifiable**: a line-level decomposition in which half or more of the
residual margin decline lands on the licensed-spectrum service line.

**wrong_if**: `metric=share_of_irdm_operating_margin_decline_attributable_to_lines_other_than_licensed_spectrum_services threshold=0.5 source=IRDM_10-Q_revenue_and_cost_disaggregation op=<`

**Subscribed**: `IRDM × unit-economics`, `IRDM × operational-kpi`, `IRDM × recent-quarter`, `IRDM × ratio-analysis`, `IRDM × competitive`, `GSAT × unit-economics`

---

### Pillar 2 — The licensed asset and the operating business price separately, and the licence is the majority of the value — **where the licence is scarce** (Priority: P2)

If the licence is an asset with an observed price and the business on top is a
single-digit-to-low-teens operating margin, the two must be valued apart. The reference
mark is **~$19.6B** for AWS-4 / H-Block / AWS-3 — **a transaction value, not a unit
price** (DA-17), and **`DERIVED` rather than filed** (it is `$17.0B + $2.6B`). Applied to
SATS, it was **~1.8× the annual revenue** of the business that held it. Applied
to the rest of the tier, it has never been tried.

**The claim:** running a two-basis SOTP per name — **(A) transaction-mark transfer**,
**(B) capitalised licence-attributable cash flow** — the licensed asset accounts for
**more than half** of the tier's attributable enterprise value **where the licence is scarce
and cannot be created**, and the operating businesses account for the rest at margins in the
**observed band, which now runs from −7.37% (GSAT) to +15.10% (IRDM)**. If the licence is a
minority of value everywhere, then the tier is a service business with a permit attached, the
mark is an outlier rather than a comparable, and P1's separation matters far less than the
tier's narrative implies.

**A third basis now exists, and it points the other way — inherited, not derived here.**
002 resolved IRDM's licence carrying value: *"Spectrum and licenses"* is an **indefinite-life
intangible, net $14,030K, unchanged and unimpaired** at both period ends, **1.6% of FY2025
revenue**. So **(C) the accounting basis** is available for IRDM and it is **two orders of
magnitude below any transaction reading**. That is not a reason to prefer it — it is the third
of three bases that must be printed side by side, and the gap between (A) and (C) is itself a
finding about how indefinite-lived spectrum is carried.

**The geospatial operators are now in this pillar, and they are the test's control.** PL,
BKSY and HAWK join Tier 2 at the v1.6.0 re-cut on the membership test — their primary revenue
comes from **operating a constellation and delivering a data product from orbit** — and they
share exactly the structure P2 tests: **a licensed orbital-and-downlink position plus a data
product delivered from orbit.** (SPIR is a member of the tier and is `NOT_READY`; it cannot
host an artifact and **no proxy is substituted** for it — the gap is recorded.)

Their admission does something the licence names could not do alone: **it separates "the
licence is scarce" from "the licence is present."** An L-band MSS licence was fully allocated
by the ITU in the early 1990s and cannot be created. An Earth-observation licence is granted,
renewable, and contested by dozens of operators — including, as GSAT's own 10-K names,
Starlink and Amazon Leo. So the same test, run across both groups, is discriminating in a way
it was not before:

| Group | Members | The licensed asset | P2's predicted reading |
|---|---|---|---|
| **Scarce-licence operators** | IRDM, GSAT, SATS | Globally harmonised L-band / MSS / AWS blocks — allocated, not creatable | The licence exceeds half of attributable EV |
| **Granted-licence data operators** | PL, BKSY, HAWK | Earth-exploration and downlink licences — granted on application, contested | The **data product**, not the licence, carries the value |

**The claim is therefore two-sided, and a single blended number cannot test it.** The licence
exceeds half of attributable enterprise value **where it is scarce**, and does not **where it
is merely required**. If the licence also dominates at the geospatial names, the tier's value
is a regulatory artefact everywhere and P1's separation is a general property of the sector
rather than of L-band; if it dominates nowhere, including at SATS, the mark is an outlier.
Both single-sided outcomes are informative and neither is assumed. **The wrong_if below is
stated tier-wide deliberately — it is the harder test — and what counts as resolution requires
the share reported per group as well as tier-wide.**

**Why this priority**: it is the valuation the inherited premise implies, and it is the
instrument the rest of the tier consumes — P3's placement rule and 007's competitive
read-through both need a per-name answer to "how much of this is the licence?". It is P2
rather than P1 because P1 decides whether the separation exists at all; P2 prices it.

**Basis discipline, stated before the numbers.** Both bases must be reported side by side
under the §1c standing rule. **Basis A** is the only observed print and prices **one**
combination of blocks for **one** footprint; carrying it forward to a different licence
requires a coverage denominator the disclosures do not provide, and a bare $/MHz-pop ratio
would be a DA-17 violation. **The $2.6B AWS-3 amendment buys 15 MHz in 1695–1710 MHz — a
different block from the one the headline names, and the two must not be merged.** **Basis B**
is derived and therefore `MODELED` until the cash-flow split is filed. **Basis C** is filed
but is an accounting allocation, not a price.

**What counts as resolution.** A per-name attribution survives only if the licence's
revenue and cost can be identified from filed disaggregation or from a disclosed
transaction of *that* issuer's own assets. An attribution that depends on a management
assertion of licence value is `CLAIMED` and cannot satisfy a falsifier. **The output is the
share tier-wide and per group, with the licensed position's basis named in-line.**

**Independently falsifiable**: an SOTP in which the operating businesses alone account
for half or more of attributable enterprise value, at the scarce-licence names.

**wrong_if**: `metric=share_of_tier2_attributable_enterprise_value_attributable_to_the_licensed_asset_per_sotp threshold=0.5 source=SPCX_EchoStar_transaction_mark_issuer_filed_operating_financials_and_filed_licence_carrying_values op=<`

**Subscribed**: `SATS × unit-economics`, `SATS × business-model`, `SATS × ratio-analysis`, `GSAT × unit-economics`, `GSAT × ratio-analysis`, `IRDM × unit-economics`, `VSAT × business-model`, `PL × unit-economics`, `BKSY × business-model`, `HAWK × business-model`

---

### Pillar 3 — The D2D transition compresses the service layer while raising the value of the licensed layer, and every Tier 2 name is placeable on one side (Priority: P3)

Direct-to-cell is the first technology in the sector's history that can serve a handset
without an incumbent's distribution — and it needs exactly what the incumbents hold.
The two halves move in opposite directions:

| Layer | What D2D does to it | Evidence in hand |
|---|---|---|
| **Service** (voice/data/SOS delivered) | **Compresses price** — the number of routes to a handset rises while the handset population is fixed | GSAT revenue **−3.5% y/y**, the only negative-growth operator in the universe; SPCX consumer ARPU **$66, −22.4%** against subscribers **+101.2%** (borrowed from the anchor as a comparator, never as Tier 2 evidence) |
| **Licence** (globally harmonised L-band / MSS) | **Raises value** — a D2D entrant must rent, partner for, or buy it | Apple holds **~20%** of GSAT and rights to **85%** of its network capacity; AMZN bids **$90.00/sh** for GSAT; RKLB bids **$54.00/sh** for IRDM's L-band |

**The claim:** the placement is **total and mechanical**. A name sits on the **licence
side** if P2's attribution assigns the majority of its value to the licensed asset, and
on the **service side** if it does not — and the split cuts across the tier rather than
along it. ASTS is the adversarial case that makes the axis real: it is a **service-layer
attacker that owns a spectrum position**, which means it can be on both sides at once —
and if it cannot be placed, the axis is not discriminating and this pillar is a
framework, not a finding.

**The geospatial members test something ASTS cannot: whether the axis is real without D2D.**
PL, BKSY and HAWK have a licensed position and a service layer, and **no D2D pressure on
either** — the mechanism simply does not reach them. So they are the case that decides what
this axis *is*. If they place cleanly by P2's rule, the licence-versus-service split is a
structural property of operating a constellation and D2D is merely the force currently moving
names along it. If they cannot be placed, then the axis is a D2D story wearing a structural
name, and the pillar must be restated as a statement about direct-to-cell rather than about
the tier. **That is a materially stronger falsifier than the pre-re-cut version had, and it is
the reason the pillar's wrong_if is now tested across eight names instead of five.**

**Why this priority**: it is the mechanism that links the tier's valuation (P2) to its
competitive future, and it is what 009 consumes as a compute-adjacent demand signal. It
is P3 rather than P1/P2 because it *interprets* the attribution rather than producing it
— and because its central claim (which side appreciates) is a **direction, not a level**.
It is evaluated over the **same 2026-Q4 horizon** as every other pillar, against the next
disclosed quarter; no pillar in this thesis carries a different `as_of` or holding period.

**Independently falsifiable**: a Tier 2 name that cannot be placed on the licence/service
axis by P2's attribution rule.

**wrong_if**: `metric=count_of_tier2_names_not_placeable_on_the_licence_service_axis_by_the_P2_attribution_rule threshold=0 source=SOTP_attribution_per_P2 op=>`

**Subscribed**: `ASTS × competitive`, `ASTS × secular-trends`, `ASTS × operational-kpi`, `VSAT × competitive`, `VSAT × sector-overview`, `GSAT × competitive`, `GSAT × business-model`, `GSAT × operational-kpi`, `IRDM × secular-trends`, `PL × competitive`, `BKSY × competitive`, `HAWK × operational-kpi`

---

### Pillar 4 — The deal gate chain is a dated checklist per name, and a break is re-underwritten from scratch (Priority: P4)

> **Sole owner, declared.** The constitution's ownership table assigns the **IRDM/RKLB deal
> gate chain (FCC → ITU → DCSA, dated catalysts, break re-underwrite)** to this thesis, and to
> no other. It was previously declared **three times** — 005 P6, 006 P4 and 006 P5 each stated
> that *"what this adds is the date"* for the same gate chain on the same transaction, sourced
> from the same document (RKLB's risk factors) — and 005 P6 repeated this pillar's break
> sentence verbatim. **005 P6 is deleted at the re-cut; its dated-consent work is absorbed
> here.** This is **one pillar, not three**, and it produces **one deliverable: a dated gate
> checklist per name.**

**The deal securities.** **IRDM ($54.00/sh, RKLB) and GSAT ($90.00/sh, AMZN) are P11
securities.** Under P11 the binding constraint for both is `REGULATORY_SPECTRUM` —
antitrust, CFIUS and national-security review — and neither clears trivially: **IRDM
carries safety-of-life and defense communications; GSAT carries globally harmonised L-band
and an Apple capacity agreement.** This pillar's job is **not** to underwrite them on
fundamentals, which P11 forbids, nor to trade the spread, which the platform cannot price at
Market Data Stage `none` for these names. It is to establish **what the spread is a price
of**, from filings.

**The claim — and the gate chain is now filed, not merely named.** 003's risk artifacts read
IRDM's and RKLB's Q2 2026 10-Qs. The consents, conditions, prices and parties are all there;
what is **absent** is a date on any of them:

| Gate | Status as filed | Source |
|---|---|---|
| **Merger agreement** | **Signed 2026-06-28**, **$54.00/share** — **$27.00 cash + RKLB stock**, with a **±25% value-preserving collar**: exchange ratio **0.4000** at RKLB ≤ **$67.50**; **$27.00 ÷ price** in between; **0.2400** at ≥ **$112.50** | IRDM 10-Q p.22 |
| **Target stockholder vote** | Required — **no date filed** | merger agreement conditions |
| **HSR** | Expiration required — **no date filed** | IRDM 10-Q p.22 |
| **FCC consent to transfer of control** | Named as a closing condition — *"certain of our telecommunication authorizations"* — **no date filed** | IRDM 10-Q p.22 |
| **Foreign-investment review (DCSA / FOCI)** | Named, **on the acquirer's side**: *"DCSA mitigation."* Adding a target holding US telecom authorisations *"converts a launch company's FOCI surface into a launch-plus-carrier FOCI surface."* **No date filed** | RKLB 10-Q p.49 |
| **ITU coordination** | ⚠️ **Not a gate on the issuer at all.** *"Only member states have full standing within this inter-governmental organization. Filings to the ITU are made on our behalf by the United States."* The recorded network is **not keyed to the issuer**, so IRDM cannot be asked to obtain this consent | IRDM 10-K p.26 |
| **National market access** | **Not evidenced** | — |
| **Close** | Expected **mid-2027** | IRDM / RKLB filings |
| **Break price** | **$223.6M termination fee, payable by IRDM** | IRDM 10-Q p.22 |
| **Financing** | **$3.6B 364-day senior secured bridge** (Deutsche Bank, Wells Fargo). RKLB needs **>$3.0bn** of cash for the stock consideration, the acquisition-indebtedness repayment and fees, **plus ~$1.8bn** to repay or refinance Iridium term debt. **The bridge is committed; the drawn pricing is not stated** → `UNRESOLVABLE-FROM-PUBLIC-SOURCES` (the bridge is *committed*; the drawn pricing is not stated in the Q2 2026 10-Q) | RKLB 10-Q pp.35, 44 |

**The ITU row is the sharpest single result, and it corrects the inherited chain.** 001
recorded the gates as **FCC → ITU → DCSA → national market access** and 002's and 003's
readings preserved it. The filing says the ITU leg is **an American action, not IRDM's**: the
issuer does not file at the ITU, the United States does, on its behalf. So *"ITU coordination"*
is not a consent the target can be asked to obtain, and the three-gate framing named **one gate
too many at the target**. The chain that actually binds IRDM is **FCC consent → foreign
investment review (DCSA/FOCI) → national market access**, with HSR and the stockholder vote
ahead of both. This is recorded as a correction to the inherited checklist, not a re-derivation
of it, and it is the kind of result a "dated checklist" instrument exists to produce.

**The acquirer is the harder case, and it is inside this pillar.** RKLB is a deal security *as
acquirer*, so P11 requires the **combined entity to be modelled including deal financing and
dilution** — the $3.6B bridge and the stock consideration. **Pro-forma combined financials are
not disclosed, so the combined-entity model is `MODELED` by construction and can never satisfy
a falsifier under P4.** That is stated, not hidden.

**A model caveat that must travel with the output.** RKLB is loss-making, so any pro-forma
leverage ratio has a **sign-sensitive denominator**. The pro-forma net-debt-to-gross-profit
test is carried as a **stated bar of 6.0×** — a spec-set threshold, **not a measurement** — and
the component arithmetic is shown in-line per P4. **The pillar's falsifier does not rest on
this bar**; it rests on the consent-date test, which is mechanical. (Absorbed from 005 P6 and
005's Clarification Q-2; see Q-9 below.)

**Why the 180-day Catalyst Requirement bites here.** F6 requires **a dateable catalyst within
180 days** for any trade idea. As filed, **no consent date is disclosed** — the chain is named
but undated, and the close is expected **mid-2027**, far outside the window. So the position is
instrumented only if a clearance or milestone lands inside 180 days; if none does, it is
**un-sizeable even at the 2% binary cap** and must be carried as `known-open`, **not as a
position**.

**The spectrum-grant limb — the same checklist instrument, applied to the non-deal names.**
F6 names orbital slots, spectrum rights and FCC/ITU coordination as **gating assets, not
paperwork**. DA-18 was converted from an ambiguity into a checklist by 001; this pillar makes
the checklist **dated and sourced per name and per gate**, and classifies each gate as
**filing-evidenced** (reachable) or **registry-blocked** (FCC IBFS / ITU Space Network List —
`UNRESOLVABLE-FROM-PLATFORM`, inherited and not re-attempted). **A gate with no dateable
expectation is recorded as a finding about disclosure quality, not quietly omitted** — and
that is the limb that now extends to PL, BKSY and HAWK, whose Earth-exploration and downlink
licences carry build-out and renewal obligations of exactly the kind DA-19 warns can lapse for
non-use.

**PIL-6's falsifier is bridged, not retired.** The falsifier —
`new_entrant_primary_spectrum_or_slot_grant_without_incumbent_acquisition` — needs registries
the platform does not carry, and 001's split disposition (premise `DEMONSTRATED`, falsifier
unreachable) is inherited as settled. 002 sharpened the class to **`UNRESOLVABLE-FROM-PLATFORM`
kind 5** — *"the FCC IBFS and the ITU SNL both exist, are public, and are free"*; the block is
**platform reach** — and added the finding that at `threshold=0` the falsifier is not merely
untestable but **`UNCLEARABLE`**, because the corpus is **reporter-conditioned against its
positive branch**. What 006 adds is a **reachable proxy**: whether a D2D entrant reaches
commercial service on **primary** grants it applied for rather than on an acquired incumbent
licence, documented in its own SEC filings. ASTS is the live candidate and is the reason this
proxy is Tier 2-specific. **The proxy triggers external verification; it does not fire the
falsifier** — issuer statements are `CLAIMED` under P4 and a `CLAIMED` figure can never satisfy
a falsifier. The proxy's job is to tell 011 when the FCC/ITU query is worth paying for.

**The break case is a distinct re-underwrite, not a discount to the deal.** On a break,
**the standalone case is not the pre-announcement case**: a failed deal leaves the target
*and* the acquirer re-rated, with the acquirer carrying deal costs — and here the acquirer's
exposure is priced: **$223.6M is payable by IRDM**, while RKLB carries the bridge, the
financing cost and the integration spend against a loss-making denominator. For IRDM that
means the pre-merger artifacts (`002/artifacts/IRDM/…`, `003/artifacts/IRDM/…`, tagged
`standalone_pre_merger`) are **inputs to the re-underwrite, not its answer** — and the
re-underwrite must clear three inherited obstacles that only appear on the break leg:
**Aireon's consolidation** (closed 2026-07-02; ~$32.8M/yr of revenue becomes intercompany and
eliminates while external revenue is added, **so no post-close benchmark is constructible from
the pre-close filings in either direction**), the **$438.1M** of new/newly-consolidated debt
(**3.83× FY2025 net income**), and **P11's basis discontinuity with no single basis flag** (Q2
2026 is `standalone_pre_merger` *and* pre-Aireon-consolidation). The scenario pair — close
versus break — is run as a `what-if`, and the break leg re-derives value from P2's **basis B**,
never from the announced price.

**Why this priority**: it is P4 because it is a *boundary condition* on the tier rather
than a finding about it — and because its output is a discipline (what may and may not be
sized) rather than a number. Note that under the Risk Framework the tier also caps at
**≤ 2 positions in any single sub-sector**, so the Tier 2 expression is at most two names
across eight.

**Independently falsifiable**: a Tier 2 name whose next required regulatory gate carries
neither a recorded expected date nor a filed source — which would leave the position with no
datable catalyst and no P9-compliant entry. **On the deal names the test is strictly the
180-day one**: a gate that is dated to mid-2027 satisfies the checklist and does **not**
satisfy P9, and the position is then carried `known-open` rather than sized.

**wrong_if**: `metric=count_of_tier2_names_whose_next_required_regulatory_gate_lacks_a_recorded_expected_date_and_a_filed_source threshold=0 source=merger_agreement_conditions_8-K_10-K_10-Q_risk_factors_and_transaction_filings op=>`

**Subscribed**: `IRDM × risk`, `GSAT × risk`, `SATS × risk`, `ASTS × risk`, `VSAT × risk`, `PL × risk`, `BKSY × risk`, `HAWK × risk`, `IRDM × recent-quarter`, `GSAT × recent-quarter`, `IRDM × what-if`, `GSAT × what-if`, `ASTS × growth-strategy`, `GSAT × growth-strategy`, `PL × growth-strategy`, `BKSY × growth-strategy`, `SATS × sector-overview`

---

### Pillar 5 — Every Tier 2 contested figure converts to `DEMONSTRATED` or is recorded as unresolvable (Priority: P5)

The meta-pillar and the scorecard for §0b. The queue is not decoration: under P4,
`MODELED` can never satisfy a falsifier, so **an unvalidated Tier 2 figure is a pillar
that cannot fire** — and the tier's headline ratio (**1.8×**) was precisely such a figure
until it was **withdrawn outright** rather than converted (§0.1).

**The claim:** every row of §0b ends the thesis either **converted to `DEMONSTRATED`**
with the source that moved it, or **classified** into one of the disposition classes with the
specific resolving disclosure named. At least half the queue converts. The residue is not a
failure — it is a finding about disclosure or platform reach, and it is reported as one.
**The class matters as much as the grade**: `UNRESOLVABLE-FROM-PUBLIC-SOURCES` is a finding
about **the world**, `UNRESOLVABLE-FROM-PLATFORM` a finding about **the instrument**, and the
proposed `REACHABLE-BUT-NOT-RECORDABLE` a finding about **the programme's own rules** — *"the
one that cannot be resolved by any amount of research."* **And a verdict is not a grade**:
`UNEXERCISED`, `UNEVIDENT` and `WITHHELD` are reported as themselves, never collapsed into
`PENDING`, because *"a check that closes cleanly while testing nothing"* is the exact defect
002 was built to catch.

**Why this priority**: it cannot be pursued directly, only accumulated — and its output
is what stops 011 from sizing against a number that was never real. It is now P5 rather than
P6 only because the former P4 and P5 merged into one pillar at the re-cut; the meta-pillar's
function is unchanged.

**Independently falsifiable**: any Tier 2 contested figure left unclassified or without a
named resolving source.

**wrong_if**: `metric=count_of_tier2_contested_figures_unclassified_or_without_a_named_resolving_source threshold=0 source=validation_queue_scorecard op=>`

**Subscribed**: `IRDM × peer-bench`, `GSAT × peer-bench`, `SATS × peer-bench`, `ASTS × peer-bench`, `VSAT × peer-bench`, `PL × peer-bench`, `BKSY × peer-bench`, `HAWK × peer-bench`, `SATS × recent-quarter`

---

> **Delivering P1 alone yields a defensible partial conclusion** — the tier's one
> profitable constellation operator either holds its licence revenue while the service
> overlay absorbs the compression, or it does not. That single decomposition decides
> whether the rest of this thesis's instrument is usable, and it is delivered first.

## 1c. Method — the attribution and gate instruments

Two capabilities are specific to this thesis and are not used elsewhere in the program.

1. **The split of the regulatory asset from the operating business.** Every Tier 2 name
   is decomposed into (a) the licensed position and (b) the operating business, valued on
   **two bases each** — transaction-mark transfer and capitalised licence-attributable
   cash flow for the licence, **plus a third accounting basis wherever the licence is
   separable on the balance sheet** (available at IRDM: net $14,030K, indefinite-lived);
   filed operating margin at the `satellite_connectivity` WACC band (**8.5–11.5%**,
   `assumptions.yaml`) for the business. This is the instrument P1 delivers, P2 prices and
   P3 places on an axis. It is also the reason the tier cannot be read with a single
   blended multiple — and, per 004, the reason the anchor's **312.8×** Connectivity
   multiple is a *benchmark* and never a borrowed input.
2. **The sequential-gate discipline.** DA-18 was upgraded from ambiguity to checklist by
   001; this thesis makes the checklist **dated and sourced per name and per gate** and
   instruments the Catalyst Requirement directly. **It produces one deliverable, not two:
   one dated gate checklist per name**, covering both the deal consents (§1b P4) and the
   spectrum grants. The instrument's value is negative evidence as much as positive: a gate
   that cannot be dated is a disclosure-quality finding. It has already produced one — the
   **ITU leg is not a gate on the issuer**, because the United States files on IRDM's behalf —
   and the inherited `UNRESOLVABLE-FROM-PLATFORM` boundary is respected rather than
   re-attempted.

**Evidence discipline.** Per P4 and the v1.3.0 register, any artifact reading
`operating_income` shows the component derivation in-line — which is mandatory here for a
specific reason: **SATS is DA-24-contaminated** (a non-cash 5G-Network impairment charge
flowed through the operating line: **17,632,011 thousand** for FY2025, of which only
**32.8%** struck regulatory authorisations) and **DA-23 IS ALSO PRESENT at SATS** (12/12
filed-negative subtotals stripped, 8/8 filed-positive clean). ⚠️ **The spec previously
asserted "DA-24 is independent of DA-23 — exactly one defect applies." That assertion is
WITHDRAWN**, on the constitution's and 002's authority: the independence proof used `EPS ×
shares`, a test the register forbids, and its residual is invariant under a global flip.
**Both defects apply at SATS, and at DA-24 names generally.** 002 measured the consequence
exactly: a reader de-contaminating with the *served* fact computes `392,847 + 66,159 =
459,006` where the correct ex-item figure is `392,847 − 66,159 = 326,688` — **a total error of
132,318 = 2 × 66,159.** Reading SATS's 2025 quarters as operating performance is a
`DATA_STALE` error, and the clean read is the **latest-quarter margin with the credit
removed (8.91%, not the filed 10.71%)**.

**Instrument limits, inherited and applied.** Three of the platform's tools are known not to
be evidence: **`validate_calculation` has four demonstrated failure modes** (pass on a
wrong-signed value; pass when both sides were stripped; zero rows on a filed concept; a 93%
false-positive rate when it fails); **`computed` may not be cited as a derivation**, and
`reported` is not definitionally the filed value; and **the served metrics block is
DA-26-contaminated** at IRDM (Q4 rows carrying annuals, off by **4.094×** and **4.271×**) and
**duration-corrupted at VSAT** (its Q1 slot carries twelve months, overstating **3.97×**).

**Definitional discipline (inherited by reference).** DA-17 (spectrum quantity), DA-18
("regulatory approval"), DA-19 (orbital slot priority) and DA-21 (segment definitions)
are live in every artifact here. **DA-21 matters most at the deal names**: Apple's "85% of
network capacity" and IRDM's "2.5M subscribers" are not commensurable quantities, and
aggregating them across issuers is the error the no-single-basis-collapse rule exists to
prevent. **DA-24's defining instance is an inverted impairment, not a sale**, and its
independence proof is withdrawn. **DA-30 — registered at v1.5.0 — binds P2 directly**: two
bases on one concept collapsed without a basis field. IRDM's served margins are its home
instance (8 of 8 divide by the Aireon hosting-agreement ceiling), and SATS's segment
attribution is its fifth (Wireless differs by **16,199,344 thousand** between two filings of
the same issuer for the same year). Per the §1c standing rule, artifacts report all competing
bases and label which one is quoted; **no percentage is presented whose denominator has not
been named.**

**Corpus discipline — a documented dead end.** PROGRAM.md §4 records that the knowledge
registry has **no industrial or aerospace domain** (`list_domains` returns 9 domains
whose `applicable_sectors` are `["med","tech","fin"]` only), so **any sector-keyed
strategy or case retrieval returns zero rows by construction**. 006 must **not** attempt
it. Where an analogue is wanted — an asset sale of a licence, an in-flight merger spread,
a monopoly asset with a commoditising service layer — it is retrieved by **structural
situation shape** and labelled borrowed, never presented as sector evidence.

**Correction policy.** Where this thesis invalidates a 001, 002, 003 or 004 figure, the
source artifact is **not** rewritten. Those files are frozen; the correction is recorded in
§0 with its location, per 002's own finding that **only 3 of 32 corrections reached a pin**
and that *"a correction that is recorded and never propagated is indistinguishable, in
effect, from one never made."* 006's §0 is a propagation mechanism.

## 2. Universe Definition

**Eight researchable names, drawn on the v1.6.0 membership test: primary revenue from
OPERATING a constellation — a licensed spectrum position, a subscriber base, or a data
product delivered from orbit.** The tier grew by three at the re-cut (PL, BKSY, HAWK from
Tier 1) and now spans two licence regimes: **allocated-and-not-creatable** (L-band / MSS /
AWS) and **granted-on-application-and-contested** (Earth observation and downlink). Weights
are analytical effort, not positions; this thesis sizes nothing above the 2% binary cap.

| Ticker | Company | Sector | Weight | Coverage / Deal | Why it is in this thesis |
|---|---|:---:|---|---|---|
| IRDM | Iridium Communications | tech.telecom_services | 22% | READY — 77 filings, cohort `tier2_2026q3` | **P1's subject and the universe's only profitable constellation operator.** 66 satellites, licensed L-band (**8.725 MHz**), ~2.5M subscribers, $871.7M revenue, $114.4M net income (2025); licence carried at **$14,030K** net. **DEAL — acquired by RKLB at $54.00/sh (P11)** |
| SATS | EchoStar | tech.telecom_services | 22% | READY — 62 filings, cohort `tier2_2026q3` | **The sell-side case and the tier's only observed spectrum price**: ~$19.6B AWS-4/H-Block/AWS-3 sale to SPCX (**`DERIVED`**, and FCC-approved with transfer closed); spectrum licences on the balance sheet at **34,550,802** net against a **17,632,011** FY2025 impairment charge. **Both purchase agreements PENDING** — no gain recognised, `standalone_pre_merger` |
| GSAT | Globalstar | tech.tech_hardware | 18% | READY — 65 filings, cohort `tier2_2026q3` | **The monopsony case**: filed operating margin **−7.37%** (a $(4,775) thousand loss — **not** the `+7.4%` the platform serves), 93% of net income non-operating, the only negative-growth operator, **64% of six-month revenue from one customer who is also the financier and the acquirer**. Apple holds ~20% equity and rights to 85% of capacity. **DEAL — acquired by AMZN at $90.00/sh (P11)** |
| ASTS | AST SpaceMobile | **`PARTIAL` — sector unassigned** | 14% | `PARTIAL` — `sector` null, `sec_filings` counter 0, but 18,536 XBRL facts and 142 source documents; FY2025 10-K reachable at `sec125`, **figures unread** | **The D2D attacker and P4's proxy test** — a new entrant pursuing primary grants rather than buying a licensee. 002 is explicit that ASTS is a **spectrum counter-party**, not a competitor IRDM names. Sector must be assigned by hand before any aggregate constraint evaluates |
| VSAT | Viasat | **`PARTIAL` — sector unassigned** | 8% | `PARTIAL` — `sector` null, `sec_filings` counter 0, but 21,898 XBRL facts and 98 source documents | **The pure service-layer comparator**: GEO/LEO broadband and government satcom with no licensed MSS position at stake. **The control that makes P3's axis falsifiable** — and a name whose served rows fail **19 of 30**, 11 with the `2 ×` fingerprint, with its Q1 slot overstating **3.97×** |
| PL | Planet Labs | industrial.aerospace_defense | 8% | READY — 62 filings, 20,957 XBRL facts, 80 source documents, 18 transcripts, cohort `tier2_2026q3`, **100% complete** | 🆕 **New at v1.6.0 — the granted-licence control for P2.** Earth-observation constellation and data product; **−37.06% operating margin on a 53.53% gross margin — the universe's best gross margin** (inherited from 003). No D2D exposure: the name that tests whether P3's axis is structural or a D2D story |
| BKSY | BlackSky | **`sector` unassigned** | 5% | READY — **17,568 XBRL facts, 79 source documents, 19 transcripts**, 86% complete. **Reclassified from `PARTIAL` at v1.6.0.** The constitution records `sector` as the only unassigned field; the live `get_ticker_coverage` record also returns null `industry` and `cohort`, so the manual-assignment precondition applies in full | 🆕 **New at v1.6.0** — Earth observation and analytics. The second granted-licence name, and the one where the licence's contribution to EV is most likely to be dominated by the analytics layer |
| HAWK | HawkEye 360 | industrial.aerospace_defense | 3% | READY — 4 filings, 2,117 XBRL facts, 7 source documents, 1 transcript, cohort `tier2_2026q3`; **no institutional-holdings row** | 🆕 **New at v1.6.0** — RF geolocation and space-based signals intelligence. The purest *data-product-from-orbit* model in the tier, and the smallest: **its capital structure is a `DA-28` candidate — four non-agreeing share counts (4.2M–98.0M), EPS bridge failing by 72% — so no EPS-based screen may run on it without a listing-date guard** |

> **Sector-assignment precondition (not an assumption).** ASTS, VSAT and BKSY are the three
> names whose `sector` must be supplied by hand before any sector-aggregate constraint can
> evaluate (PROGRAM.md §7). The assignment is recorded explicitly in each artifact's
> frontmatter. Note also that the platform files **GSAT under `tech.tech_hardware`**, not
> telecom services, and **PL and HAWK under `industrial.aerospace_defense`** — a sector
> screen on telecom would silently omit three of the tier's eight names, and an
> `aerospace_defense` screen would omit six.

**Cited third parties — counterparties and comparators, NOT universe members.** Four names
appear throughout this spec because the tier's mechanics run through them. **None is a member
of this thesis, none may be screened, ranked or sized here, and each is cited with its source
named at the point of use.** The constitution's rule is explicit: where a name spans
functions, the tier is set by primary revenue and **every other function is carried as a
DECLARED CROSS-TIER DEPENDENCY — never absorbed as a pillar of the host thesis.** These four
are the reverse case: they are the *other tier's* names appearing inside this thesis's
mechanics.

| Ticker | Tier | Role **inside 006** | Where cited | Why it is not a member here |
|---|---|---|---|---|
| **SPCX** | Tier 0 — 004's | The **spectrum counterparty** (~$19.6B mark), the **operating-leverage benchmark** (+38.59% Connectivity margin), and P3's **borrowed ARPU comparator** | §0.1, §0.4, §1b P2, §1b P3, §0b | Valued by 004 and only by 004. **Priced off as a permitted consumer, per 004's §5 boundary — cited, never re-derived** (Q-4) |
| **AMZN** | Tier 4 — 009's | **Acquirer of GSAT at $90.00/sh** (agreed 2026-04-13, ~$11.57B, close expected 2027) and **Amazon Leo**, ~180–200 satellites with a target of 3,200 by 2029 and ~$17B capex committed — **a direct competitor to the tier's connectivity layer** | §1, §1b P3, §1b P4, §2 | 009's membership; also `PARTIAL` (sector unassigned). **004's own disposition carries it here as a competitor**: *"Amazon Leo — competes with Connectivity… Carried at 006"* — carried as a **cited competitor in P3**, not as a universe row |
| **AAPL** | Tier 4 — 009's | Holds **~20% of GSAT** and rights to **85% of its network capacity** — the **demand owner on the other side of the tier's largest monopsony**, and the counterparty that makes GSAT's 64% single-customer concentration literal | §1, §1b P3, §2 | 009's membership; also `PARTIAL` (sector unassigned). Cited as the counterparty whose capacity agreement appears in GSAT's filings and in the constitution |
| **RKLB** | Tier 1 — 005's | **Acquirer of IRDM**; the deal's other half; holder of the **$3.6B bridge** and the share consideration | §0.1, §0.3, §1b P4, §2 | 005's membership. Under the re-cut, **RKLB reads IRDM as a cross-tier dependency and cites 006 for the gate chain** — the edge 005's Q-6 was written to resolve (§5b) |

> **The flags are stated in the affirmative, so the failure mode is checkable:** AMZN and
> AAPL appear in this thesis **only** as (i) the GSAT counterparties named in the constitution
> and in GSAT's filings, (ii) Amazon Leo as a *named competitor* inside P3's placement table,
> and (iii) the capacity-concentration facts in §1's Reading B. **Neither appears in §3's
> Skill Deployment Matrix, in §4's Depth Tiers, or in any `Subscribed` pair**, and neither may
> be added to them without a spec amendment.

**Named but not researchable — recorded as coverage gaps, not proxied.**

| Ticker | Company | Class | Why it cannot host research |
|---|---|---|---|
| SPIR | Spire Global | `NOT_READY` | 🆕 **A Tier 2 member at the re-cut** — space-based data (weather, maritime, aviation). `xbrl_facts` = 0, `src_documents` = 0, `sec_filings` = 0; the only populated source is an institutional-holdings stub dated **2025-12-31**. **It is the tier's third granted-licence data operator and it cannot be read** — so P2's geospatial group is a group of three, not four, and that limitation travels with the pillar |
| MDA | MDA Space | `NOT_READY` | Canadian space robotics and satellite subsystems — a load-bearing read-through for the tier's supply side. `xbrl_facts` = 0, `src_documents` = 0 |
| TSAT | Telesat | `NOT_READY` | Lightspeed LEO constellation — the closest listed analogue to a *primary* constellation entrant, and therefore the name P4's proxy would most want. Unavailable |
| GILT | Gilat Satellite Networks | `NOT_READY` | Ground segment and satellite networking — the service-layer cost base this thesis cannot size |
| SGBAF | SES S.A. | `NOT_READY` | Luxembourg GEO/MEO fleet operator (OTC ADR) — the European licence-comparator absent from the tier. A registry row exists (**CIK 0001347408**) and yields **0 filings and 0 documents**: covered in name only |

**Excluded by design**: JOBY and ACHR are atmospheric and out of scope; Eutelsat, Avio and
SKY Perfect JSAT are listed elsewhere and platform-uncovered — tracked as competitive inputs,
never as theses. **No proxy is substituted for a `NOT_READY` name**: where SPIR, MDA or TSAT
would have carried a datapoint, the gap is recorded and the conclusion is stated without it.

**Empty-result disposition.** This tier can genuinely empty out, and the path is live
rather than hypothetical: SATS's spectrum is being transferred to SPCX, and if the two
P11 deals close, **IRDM and GSAT leave the listed universe** and the licence layer is held
entirely privately. If screening then returns no researchable expression, the tier is
**not** closed as a null result and the premise is **not** withdrawn. It converts to a
**holdings-level read-through** recorded in `_cross/`, with the attribution register
retained for 007 and 011 and the tier marked `no_listed_expression` rather than
`no_thesis`. The inherited premise survives; only its expressibility is lost — which is
itself a finding 011 must size against. **Note that the re-cut makes this path less likely
than it was: PL, BKSY and HAWK are not party to either deal, and their addition means the
tier retains a listed expression even if both transactions close.**

## 3. Skill Deployment Matrix

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|:---:|---|:---:|---|
| unit-economics | business-intelligence | Deep | IRDM, GSAT, SATS, PL, BKSY, HAWK | none | **P1's decomposition instrument** and P2's per-name split of licence revenue from service revenue — including the geospatial trio's data-product margin |
| operational-kpi | business-intelligence | Deep | IRDM, GSAT, ASTS, PL, HAWK | none | Subscribers, ARPU, capacity and constellation KPIs — the tier's operating-leverage series (**P1**, **P3**) |
| competitive | equity-research-core | Deep | IRDM, GSAT, ASTS, VSAT, PL, BKSY, HAWK | none | **P3's D2D placement**: who attacks the service layer and who holds the licence layer — and whether the granted-licence names place at all |
| risk | equity-research-core | Deep | IRDM, GSAT, SATS, ASTS, VSAT, PL, BKSY, HAWK | none | **P4's single deliverable**: the dated gate checklist per name, the deal conditions in the agreements, and the licensing obligations on the Earth-observation constellation |
| business-model | equity-research-core | Standard | SATS, GSAT, VSAT, PL, BKSY, HAWK | none | Classify each model and separate licence revenue from service revenue before any comparison (**DA-21**; **P2**, **P3**) |
| recent-quarter | equity-research-core | Standard | IRDM, GSAT, SATS, ASTS, VSAT, PL, BKSY, HAWK | none | Latest reported quarters on the component identity — **and DA-24/DA-23 hygiene at SATS, DA-26 at IRDM, the duration defect at VSAT** (**P1**, **P4**) |
| ratio-analysis | quantitative-analysis | Standard | IRDM, SATS, GSAT, PL, BKSY | none | Margin and return ratios recomputed from components; catches DA-23/DA-24/DATA_STALE residues (**P1**, **P2**) |
| peer-bench | industry-analysis | Standard | IRDM, GSAT, SATS, ASTS, VSAT, PL, BKSY, HAWK | none | All eight names against each other: **the corrected margin ladder**, leverage, and the licence/service mix — reported **per licence regime, not blended** (**P5**) |
| sector-overview | industry-analysis | Standard | VSAT, SATS, PL, BKSY, HAWK | none | D2D, GEO/LEO and Earth-observation segment structure; where the tier's capacity and data products are actually sold (**P3**, **P4**) |
| secular-trends | equity-research-core | Standard | ASTS, IRDM, PL | none | The D2D transition as a secular force, the licence-value read-through, and whether the granted-licence regime moves with it (**P3**) |
| what-if | business-intelligence | Light | IRDM, GSAT | none | The close-versus-break scenario pair; on a break, re-underwrite from scratch (**P4**) |
| growth-strategy | equity-research-core | Light | ASTS, GSAT, PL, BKSY | none | Primary-grant path versus acquisition path — the reachable proxy for PIL-6's falsifier (**P4**) |

> **Coverage invariant.** Every ticker in §2's member table appears at least once above;
> every `Subscribed` pair in §1b generates at least one task. Verified mechanically by
> `tools/plan_audit.py` — invariants **I1** (universe ⊆ matrix), **I2** (subscribed ⊆
> matrix), **I3** (skills resolve against the registry) and **I4** (every matrix skill is
> subscribed somewhere, so no row gets the `[P1]` fallback bracket). **The four cited third
> parties — SPCX, AMZN, AAPL, RKLB — and the five `NOT_READY` names are deliberately outside
> the matrix: none can host research in this thesis.**

## 4. Depth Tiers

| Tier | Skills | mode-set | Tickers | Output |
|:---:|------|---|--------|------|
| Deep | unit-economics, operational-kpi, competitive, risk | all modes | IRDM, GSAT, SATS, ASTS | Full-mode work on the names carrying P1–P4 |
| Standard | business-model, recent-quarter, ratio-analysis, peer-bench, sector-overview, secular-trends | essentials_modes | As listed | Cross-sectional comparison, the corrected margin ladder, the placement map |
| Light | what-if, growth-strategy | essentials_modes | As listed | The break scenario and the falsifier proxy |

**Budget note — RESOLVED at Q-12, 2026-09-20.** The matrix yields **67 distinct (ticker,
skill) analyses across 8 names** — up from 39 across 5 before the re-cut. Mode expansion
applies multiplicatively, as it did at 001 (2.07×), giving roughly **140 mode-tasks**.
⚠️ *This note previously read "the `max_tasks: 40` currently recorded in `thesis.md`" and
closed "recorded as an open item rather than silently reconciled". **Both statements are now
wrong and are corrected in place**: `thesis.md` records **60**, not 40, and the item is **no
longer open** — **the budget stays at 60 and the Standard and Light rows are pruned to
essentials-only before dispatch.** The decision, and the binding prune order, are at **Q-12**.*
If it must come down further, drop the
Light rows first — never the `risk` row, which is the entire delivery mechanism for **P4**,
never `recent-quarter` at SATS, which carries the DA-24 hygiene the tier's only clean
operating read depends on, and never `recent-quarter` at VSAT, where the served duration
defect means the row is the only way the correct quarter is ever produced.

## 5. Cross-Cutting Analysis

- **The attribution register** is the cross-cutting output: per name, licence value on all
  three bases, operating-business value, the resulting placement, the licence regime, and the
  deal status — the Tier 2 analogue of 001's technology-line register, and the artifact 007,
  009 and 011 cite instead of re-deriving.
- **The gate chain** is a dated checklist per name, with each gate marked
  filing-evidenced or registry-blocked. It is **one artifact, not two** — the former
  `tier2-gate-chain` and the deal-conditions work are the same list. The blocked entries are
  reported as a finding about platform reach, per the disposition classes — **not as absence
  of evidence** — and the **ITU row is the first result it produced**: the issuer is not a
  party to that gate.
- **Macro sensitivity: high but bifurcating.** **Six names are long-duration operating
  equities** in a NEUTRAL-bias, long-end-hostile regime (10Y at 4.80%); **two are
  spread-driven and therefore almost rate-insensitive at the margin.** The tier's macro
  sensitivity falls as the deal securities become a larger share of it — an unusual and
  worth-stating property in a single-theme book. **Market Data Stage is `none` for all eight
  names** while 004 runs at `per_row`: the tier cannot price its own spreads, and Q-5 records
  that as an open question rather than a workaround.
- **Constitution interaction.** P11 governs IRDM and GSAT at every step — no standalone
  underwriting, 2% binary cap, re-underwrite on a break. **DA-24 governs any SATS read** (a
  non-cash impairment charge flowed through the operating line; the clean read is the
  latest-quarter margin **with the credit removed — 8.91%, not the filed 10.71%**) **and DA-23
  applies at SATS too**, the independence claim having been withdrawn. DA-17/18/19/21/30
  govern every cross-name quantity, and **DA-30's rule binds P2's three-basis reporting
  directly**. **F6 supplies the Catalyst Requirement** that P4 instruments. The Sector
  Preferences ranking (**Overweight / High**) is the prior this thesis tests, not a finding it
  inherits — and 003's corrected ladder is the first evidence against it.
- **Corpus note.** Per PROGRAM.md §4 the registry has no industrial or aerospace domain,
  so sector-keyed strategy retrieval returns zero rows by construction. Any analogue used
  here is retrieved by **structural situation shape** — a licence sale, an in-flight
  merger spread, a monopoly asset with a commoditising service layer — and labelled
  borrowed. 006 does not attempt a sector-tagged lookup. **Two asymmetries are on record and
  are not closed here**: the registry carries **fund-sourced cases for MOG-A and ENS** while
  neither has issuer coverage, and **442 of 446 corrections never reached a pin.**
- **Pair candidates are constrained, not absent.** The licence-layer-versus-service-layer
  pair is the natural expression of P3, but the Risk Framework caps the tier at **≤ 2
  positions in any single sub-sector** and the theme cap (40% NAV) binds first in a
  single-theme book. With two of eight names being P11 securities, at most two Tier 2
  expressions exist at any time, and the pair is one of them. Size is 011's decision; this
  thesis supplies the attribution and the gates.

## 5b. Cross-tier dependencies — declared, not absorbed

**Every name below spans more than one function. The tier is set by primary revenue, and the
other functions travel as declared dependencies with a named owner.** This section exists
because the constitution's membership rule requires it and because its absence was measured:
thesis 005 had grown three pillars belonging to other tiers until only one of its six was about
its own cohort.

| Dependency | Owner | What 006 does | What 006 may **not** do |
|---|---|---|---|
| **The IRDM/RKLB deal gate chain** (FCC → ITU → DCSA, dated catalysts, break re-underwrite) | **006 — sole owner** | Produces the dated checklist per name and the break-leg re-underwrite (§1b P4) | — |
| **Operator margins by segment** | **006 — sole owner** | Produces the corrected ladder and the licence-versus-service split (§1b P1, P2) | — |
| **Solar-cell duopoly and its pricing power** (RKLB/SolAero · BA/Spectrolab) | **008** | Cites it as the launch-side input cost, and stops | Re-derive the structure or price the unit. **BA/Spectrolab belongs to 008 and appears nowhere in this thesis** |
| **BA / Spectrolab** specifically | **008** | None | Cite it at all — the name is not a Tier 2 name, not a counterparty, and not a comparator |
| **Financing runway and fixed-cost absorption** | **005** | Accepts RKLB's **$3.6B bridge, >$3.0bn cash need and ~$1.8bn refinancing** as *filed deal facts* inside P4's gate checklist | Underwrite RKLB's runway, endorse the 6.0× bar as a measurement, or model the combined entity beyond what P11 requires |
| **RKLB read as a combined entity** (005's Q-6) | **005** | Reads IRDM as a **Tier 2 name** under the membership test and supplies the gate checklist 005 cites | Hold both halves of one entity as separate positions, or price the same cash flows twice. **005's Q-6 provisional answer — "one name in 005" — is superseded by the re-cut: IRDM's primary revenue is operating a constellation, so it is 006's, and 005 takes the gate chain by citation** |
| **The anchor's Connectivity reference** (004's reusable row) | **004** | Consumes the filed Connectivity figures and the assigned `MODELED` regime; cross-checks against **terrestrial broadband**, per 004's boundary | Import a satellite peer multiple. **004's comparability partition admits 0 of 11, and IRDM/GSAT are excluded as `P11` regardless of priceability** |
| **SPCX as a borrowed comparator** (ARPU series) | **004** | Uses it labelled as a comparator, never as Tier 2 evidence (Q-4) | Count it as Tier 2 evidence, or re-derive the segment |
| **Amazon Leo and Apple's capacity agreement** | **009** | Carries them in P3's placement table as **cited competitors and counterparties**, with the source named | Screen, rank or size either name. **AMZN and AAPL appear in no matrix row and no `Subscribed` pair** |
| **The value-pool map and the corrected ladder** | **003** | Consumes both and re-derives neither | Re-run the cross-issuer launch-vs-non-launch margin test, or re-map the pool. **Where 006 corrects a 003 figure — SATS's 10.7% → 8.91% (carry-forward C1) — the correction is recorded in §0.2 and 003's file is left frozen** |
| **The validated input set and the defect register** | **002** | Inherits the verdicts with their grades and their kinds, per §0.2 | Re-open 002's denominators or physics, or collapse `UNEXERCISED`/`UNEVIDENT`/`WITHHELD` into `PENDING` |
| **PIL-6's falsifier** | **Split — 001 (premise) / 006 (proxy)** | Builds the reachable proxy and triggers external verification | Claim the proxy **fires** the falsifier. Issuer statements are `CLAIMED` and cannot satisfy a falsifier; the real falsifier stays `UNRESOLVABLE-FROM-PLATFORM` and is not retired |

**The one-way rule.** 006 **cites** upward and sideways and **owns** only the two questions the
constitution assigns it. Where a dependency is cited, the consuming artifact names the owning
thesis and the source artifact — never the conclusion alone. **A cross-tier question answered
here without a citation back to its owner is the failure mode this section prevents**, and it
is the same failure the constitution records as the reason 005 was re-cut.

## 6. Output Contract

- **Per-ticker (dispatcher-resumable)**: `artifacts/{ticker}/{YYYY-MM-DD}_{skill}_{mode}.md`
  — the suffix **must** be `_{skill}_{mode}.md` with the real mode slug, so
  `dispatch.resume_verdict()` can find it.
- **Cross-cutting (not resume-tracked)**: `_cross/{name}.md` — `_cross/tier2-attribution-register.md`
  (primary), **`_cross/tier2-gate-chain.md` (the single dated checklist per name, absorbing the
  former deal-conditions artifact)**, `_cross/tier2-d2d-placement.md`.
- **Primary artifact**: `_cross/tier2-attribution-register.md` — per name: licence value on
  **all three bases (A transaction-mark, B capitalised licence cash flow, C filed carrying
  value where separable)**, operating-business value, the licence/service placement, the
  licence regime (allocated vs granted), the dated next gate, and the deal status. This is
  what 007, 009 and 011 cite.
- **⚠️ P11 — `deal_security_basis` is mandatory on IRDM and GSAT artifacts.** Every
  artifact written for IRDM or GSAT **must set `deal_security_basis`** in its frontmatter
  (`standalone_pre_merger` while the transaction is unclosed; `post_close` after), and
  every operational metric drawn from those names is tagged pre-merger basis. This is the
  `deal_security_tagging` validation rule in `contracts/artifact-frontmatter.yaml` and it
  is a **fail-level** rule: an artifact on either name that omits the field is rejected,
  not re-run. `not_applicable` is admissible only on SATS, ASTS, VSAT, PL, BKSY and HAWK.
  **On a break, the IRDM break leg re-derives from basis B and must carry the Aireon
  consolidation, the $438.1M of new debt and the basis discontinuity explicitly** (§1b P4).
- **Frontmatter**: per `contracts/artifact-frontmatter.yaml`, with `thesis_id:
  "006-constellation-operators"`. All five pins are mandatory: `constitution_pin:
  **1.6.0**`, `assumption_pin: "2"`, `skill_pin`, `as_of`, `corpus_version`. `definitions_used`
  is required with at least one `DA-NN` — **DA-17, DA-18, DA-19, DA-21 and DA-24 are live
  for every artifact in this thesis.**
  > ⚠️ **Two contract gaps, recorded rather than silently worked around.** (1) The
  > `pillar` enum is `[PIL-1 … PIL-6, cross]`; after the P4/P5 merge this thesis assigns
  > **PIL-1 … PIL-5 only**, so **PIL-6 is unused and must not be assigned** — an artifact
  > carrying PIL-6 would be mapped to a pillar that no longer exists. (2) The
  > `da_id_registered` rule validates against **DA-23…DA-28**, so **DA-29 and DA-30 —
  > registered at v1.5.0 and binding P2's two-basis reporting — cannot yet be declared** in
  > `definitions_used` without failing the rule. §1c carries them as prose obligations until
  > the enum is extended. Both are housekeeping for the next contract revision, not blockers.
- **The ERI decision**: `Astro-ERI-1.0` — `inquiry_type: analytical`, `coherence_state: coherent_emergent`
- **`PARTIAL` precondition**: ASTS, VSAT and BKSY artifacts record the manual sector
  assignment in the frontmatter before any sector-aggregate constraint evaluates. **HAWK
  artifacts carry a listing-date guard**: no EPS- or share-count-based screen may run on HAWK
  without one (DA-28).
- Snapshot: `snapshots/006-constellation-operators/{YYYY-MM-DD}_thesis.md`

## 7. Thesis Phases

| Phase | Tasks | Duration | Dependencies |
|:---:|------|:---:|------|
| 1 — Decomposition (P1) | Line-level attribution of IRDM's residual decline on the component identity; isolate the 63.8% transaction-cost share and the $1.251M R&D step-up; test the licensed-service line against the $9.030M residual | Week 1 | **Constitution v1.6.0 loaded**; 002's validated inputs where they apply; the component re-run **002-F8** |
| 2 — Attribution (P2) | Build the three-basis SOTP; assemble the $19.6B mark with its DA-17 limits and its re-grade to `DERIVED`; run the split for all eight names, **reported per licence regime** | Week 2 | Phase 1 |
| 3 — D2D placement (P3) | Service-layer compression evidence; place all eight names on the axis by the P2 rule; test whether ASTS is placeable at all, **and whether the granted-licence trio places without D2D** | Week 3 | Phase 2 |
| 4 — **The gate chain (P4)** | **One deliverable, one phase**: the dated checklist per name and per gate for both deals and both licence regimes; classify filing-evidenced vs registry-blocked; build the primary-grant proxy test; run close-versus-break on IRDM with the Aireon and basis-discontinuity adjustments | Week 4–5 | Phase 3 |
| 5 — Queue close-out (P5) | Scorecard for §0b: convert or classify every Tier 2 contested figure, **preserving verdicts as verdicts** | Week 6 | Phase 4 |
| 6 — Hand-off | The attribution register for 007 (primes as incumbent satcom competition), 009 (D2D as compute-adjacent demand), 011 (positions, sizing, analogues). **005 takes the gate chain by citation to `_cross/tier2-gate-chain.md`** | Week 7 | Phase 5 |

> **Phases 4 and 5 are merged.** They were separate phases in the pre-re-cut spec and they
> produced the same artifact twice. One pillar, one phase, one checklist per name.

## Clarifications

- [2026-09-20] Q: Q-11 (the 005 edge, and whether the two theses may run in parallel) — 006 and 005 each cite the other in the body (§5b / §2b) but NEITHER declares the other in its `Depends on` header, and the wave declarations disagree: 005's header reads "wave-2 hand-off to 006/008/009" while PROGRAM.md §3 and 006 both place 006 in wave 1. The edge is substantively two-way — 006 owns the IRDM/RKLB gate chain that 005's RKLB row turns on, and 006 §5b names 005 as owner of the financing-runway and combined-entity framing. Which way does the edge run, and do the two run concurrently? → A: **005 completes first and 006 consumes it by citation — the edge is declared ONE-WAY, on the consuming side only.** The gate chain stays 006's sole deliverable, but 005 does not wait for it: 005's RKLB row is carried `known-open` pending 006's P4, and 005's `Depends on` header is unchanged. **006 adds `005` to its own `Depends on`** as a citation dependency — it cites 005's Tier 1 cross-section for RKLB's financing facts (the $3.6B committed bridge, the consideration mix) and re-derives nothing. 006's §5b rows naming 005 are therefore re-read as citations, not as blockers. ⚠️ **A WAVE DEFECT IS RECORDED AND NOT RESOLVED BY THIS ANSWER:** PROGRAM.md §3 places **006 and 008 in wave 1** and 006 self-declares Wave 1, so **005's header is the outlier** — and it mislabels 008 and 009 in the same sentence. That is a separate PATCH to 005's header, not part of this answer, and it is left open rather than papered over by the sequencing decision.
- [2026-09-20] Q: Q-12 (budget) — three sources disagree: `thesis.md` records `max_tasks: 60`, this spec's Q-7 states `thesis.md` records 40 (stale), and §3's matrix yields 67 analyses / ~140 mode-tasks. Raise the budget, or prune the matrix? → A: **Keep `max_tasks: 60`; prune the Standard and Light rows to essentials-only.** The prune order is this spec's own and is binding: **drop the Light rows first** (`what-if`, `growth-strategy`), **never the `risk` row** — it is P4's entire delivery mechanism — **never `recent-quarter` at SATS**, which carries the DA-24/DA-23 hygiene the tier's only clean operating read depends on, and **never `recent-quarter` at VSAT**, where the served duration defect means that row is the only route to the correct quarter. Q-7's premise is corrected here: the 40 it attributes to `thesis.md` is stale, the file records **60**. §7's phase structure and the P5 hand-off are unaffected.
- [2026-09-20] Q: Q-13 (expiry triggers) — neither `thesis.md` nor `spec.md` declares `expiry_triggers` (Q59 requires them; 004 declares six). What should 006's be? → A: **Six, at the finest granularity.** (1) **`deal_close_or_break`** — either IRDM/RKLB or GSAT/AMZN closing or terminating; both are P11 and a break re-underwrites from scratch. (2) **`sats_spectrum_agreement_completion`** — EchoStar's two pending agreements completing; P2's sell-side basis and the ~$19.6B mark both move. (3) **`next_quarter_filing`** — the DA-26, DA-23 and duration defects are re-verified against every new filing set, and P1–P3 are quarter-bound. (4) **`constitution_bump`** — the 1.6.0 pin expires. (5) **`spir_coverage_arrival`** — P2's granted-licence control moves from three names to four. (6) **`asts_first_filed_service_revenue`** — the trigger for P4's primary-grant proxy test, which is the only evaluable route to PIL-6's falsifier.
- [2026-09-20] Q: Q-14 (P2's granted-licence control size) — the control group is three names (PL, BKSY, HAWK) because SPIR is `NOT_READY`. Is three enough for P2's two-sided claim to be falsifiable, or is SPIR's coverage a precondition? → A: **Three is sufficient and SPIR's coverage is NOT made a precondition.** P2's two-sided claim requires at least one counter-group; **one name would not distinguish the readings and three does**. The limitation travels with the pillar as a recorded bound under the §1c standing rule: the granted-licence group is a group of **three, not four**, because SPIR's `xbrl_facts`, `src_documents` and `sec_filings` are all **zero**. Waiting for coverage would suspend P2 indefinitely, which is the disposition this answer rejects — the same reasoning 004 applied to its own `UNRESOLVABLE` bounds.

Recorded by `agentii.specify` at creation, 2026-09-18; **revised at the v1.6.0 re-cut,
2026-09-19.** **The first `agentii.clarify` round ran 2026-09-20** — its four answers are
Q-11 … Q-14 at the head of this section.

**Which entries that round moved, stated exactly rather than implied:**
**Q-7 (budget) is ANSWERED at Q-12** and **Q-10 (control-group size) at Q-14.**
**Q-1, Q-2, Q-3, Q-4, Q-5, Q-6, Q-8 and Q-9 retain their provisional answers** — Q-5 and
Q-8 remain **flagged for human confirmation** and are carried as bounds, not resolved.
A provisional answer that has not been confirmed is still a provisional answer, and this
spec does not report it as settled.

- **Q-1 (P1, attribution granularity)** — Does IRDM's filed disaggregation separate
  licensed-spectrum service revenue from the equipment and other lines finely enough to
  attribute the margin decline by line, or does it stop at the operating-expense level?
  **Provisional answer, pending clarify:** if the filing stops short, P1 defaults to the
  coarser gross-profit − opex test, the limitation is recorded in-line, and the pillar is
  carried as partially evaluated rather than dropped. **Now partly answered:** the p.53
  service-revenue disaggregation explains only **46.4%** of IRDM's revenue movement, so the
  default path is provisionally the live one.
- **Q-2 (P2, one mark, different assets)** — The $19.6B mark prices one combination of
  blocks for one footprint (DA-17). Is a **mark-based** transfer admissible as a primary
  SOTP basis for a different licence, or must basis B (capitalised licence cash flow) be
  primary with the mark shown only as the single observed print? **Provisional:** all
  bases reported side by side; the mark labelled as a transaction value, **`DERIVED` rather
  than filed**, and never as a unit price. **The re-cut sharpens this**: with granted-licence
  names now in the tier, a mark-based transfer across licence *regimes* is a category error,
  not merely an evidentiary one — the $2.6B AWS-3 amendment buying 15 MHz in a different
  block from the one the headline names is the worked example.
- **Q-3 (P2, licence carrying value)** — Is the in-place licence separable on the balance
  sheet, or is it an indefinite-lived intangible inside a line that also carries other assets?
  **RESOLVED for IRDM — yes, and it is net $14,030K (1.6% of revenue), flat and unimpaired.
  STILL OPEN for GSAT, and now also for PL, BKSY and HAWK**, where the answer decides whether
  basis C exists for the granted-licence group.
- **Q-4 (P3, borrowed comparator)** — SPCX's ARPU series is the universe's only
  demonstrated service-layer price series, but SPCX is Tier 0 and belongs to 004. Is it
  admissible inside 006 as a **cited comparator**, or must every Tier 2 price claim rest
  on Tier 2 names alone? **Provisional:** admissible as a comparator, labelled as such,
  and never counted as Tier 2 evidence. **Confirmed at the re-cut and extended**: 004's
  §5 comparability boundary names 006 as a permitted consumer of the Connectivity row, so
  the citation is now authorised by the owning thesis rather than by convention.
- **Q-5 (P4, Market Data Stage `none`)** — The spread is the central object of P4 and the
  platform carries no price series for any Tier 2 name, so spread *width* is not measurable
  here — while 004 has moved to `per_row`. Does 006 carry the spreads qualitatively (a spread
  exists, its width unmeasured) or does it request a market-data stage for these two names?
  **Flagged for human confirmation; if answered differently this is a PATCH to spec, not a
  MAJOR event.**
- **Q-6 (P4, proxy admissibility)** — Is the primary-grant proxy (a D2D entrant reaching
  commercial service on its own filings rather than an acquired licence) admissible as the
  evaluable substitute for PIL-6's falsifier? **Provisional:** yes as a **trigger for
  external verification**, explicitly not as the falsifier firing — issuer statements are
  `CLAIMED` under P4 and cannot satisfy a falsifier. The real falsifier stays
  `UNRESOLVABLE-FROM-PLATFORM` and is not retired. **002 adds a constraint the provisional
  answer did not carry**: at `threshold=0` the falsifier is **`UNCLEARABLE`**, so the proxy
  is not a substitute for a test that could pass — it is the only test that can run.
- **Q-7 (P5, budget)** — **ANSWERED at Q-12, 2026-09-20.** `thesis.md` records
  `max_tasks:` **60** — *this entry previously read 40, which was stale; corrected in place.*
  The matrix still yields **67 analyses / ~140 mode-tasks**, well above 60. **Decision: keep 60
  and prune the Standard and Light rows to essentials-only**, with a binding prune order —
  Light rows first, never `risk` (P4's whole delivery mechanism), never `recent-quarter` at
  SATS (DA-24/DA-23 hygiene) or at VSAT (the duration defect is only correctable there).
  The pre-clarify provisional ("raise to ~140") is **superseded**.
- **Q-8 (P4, the 6.0× pro-forma bar — absorbed from 005's Q-2)** — The pro-forma
  net-debt-to-gross-profit test is a **spec-set threshold, not a measurement**, and RKLB's
  loss-making status makes any leverage denominator sign-sensitive. Is 6.0× the right bar to
  carry into 006 now that the acquirer-side model lives here? **Provisional:** carry it as a
  **stated bar**, show the component arithmetic in-line, and keep the pillar's falsifier off
  it — the falsifier rests on the consent-date test, which is mechanical. **Flagged for human
  confirmation.**
- **Q-9 (all pillars, the cited-party boundary)** — SPCX, AMZN, AAPL and RKLB all appear
  inside this thesis's mechanics and none is a universe member. Is the §2 "cited third
  parties" table — plus the affirmative rule that none may enter §3's matrix or any
  `Subscribed` pair without an amendment — the right discharge of the constitution's
  cross-tier dependency rule, or does each citation need a per-row owner tag? **Provisional:**
  the table discharges it; per-row owner tags would be the stronger form and are the natural
  next revision if a citation is ever found to have become load-bearing.
- **Q-10 (P2, the granted-licence group's size)** — The geospatial control is a group of
  **three** (PL, BKSY, HAWK), because SPIR is `NOT_READY`. Is a three-name group large enough
  for the two-sided P2 claim to be falsifiable, or does the pillar need SPIR's coverage
  acquired first? **Provisional:** three is enough to distinguish the readings — one name
  would not be — and the limitation is recorded with the pillar rather than resolved by
  waiting. **Flagged for human confirmation.**
