# Research Thesis: 002 — Evidence Validation & Model Hardening

**Constitution Ref**: constitution.md v1.4.0 (`constitution_pin: 1.4.0`)
**Created**: 2026-09-18
**Status**: Active
**Time Horizon**: 2026-Q4, terminating at the wave-1 hand-off to 003–006
**Depends on**: `001-technology-baseline` (pin 1.2.0 — the thesis this one validates)
**Produces**: no trade ideas. Produces a **validated input set** that 003–011 cite
instead of re-deriving.

---

## 0. Inherited baseline — what this thesis does NOT re-derive

001 established the following and this thesis **takes them as given**. Re-deriving any
of these is out of scope; the artifact cites 001's file rather than repeating its work.

| Inherited result | 001 artifact | Grade |
|---|---|---|
| Launch cost sits **15–30× above the $1,000/kg threshold** on every demonstrated basis | `RKLB/…_unit-economics_methodology.md` | `DEMONSTRATED` |
| RKLB is the **only** issuer disclosing `cost per launch` and `revenue per launch`; basis B = **$14,667/kg**, basis A = **$30,333/kg** (Electron) | `RKLB/…_unit-economics_methodology.md` | `DEMONSTRATED` |
| Electron is **10.3× Falcon 9 per kg** on basis A | same | `DEMONSTRATED` |
| F5 splits: propellant floor binds **fully reusable** vehicles only; Falcon 9's binding term is the expended second stage | `SPCX/…_unit-economics_methodology.md`; constitution F5a/F5b | `MODELED` |
| A1b falsified — growth at SPCX/RKLB/FLY comes from non-launch business | `FLY/…`, `RKLB/…`, `SPCX/…_operational-kpi_methodology.md` | `DEMONSTRATED` |
| DA-23 sign-stripping: **4 of 4 negative flipped, 8 of 8 positive clean, zero exceptions** | `MSFT/…_secular-trends_methodology.md` (census) | `DEMONSTRATED` |
| F1 array ceiling **~5,000–5,600 m²/MW** (not the naive 2,449) | `_cross/phase-2-constraint-envelope.md` | `MODELED` |
| Terrestrial compute is **constrained but expanding**; MSFT adds ~8× SPCX's nameplate per year | `MSFT/…_secular-trends_methodology.md` | `DEMONSTRATED` |
| MRCY earns a **0.03% operating margin** — the F4 supplier captures no rent | `MRCY/…_secular-trends_methodology.md` | `DEMONSTRATED` |

**What 001 did not do:** validate the *inputs* underneath those results. That is this
thesis's entire scope.

---

## 1. Research Question

**Which of 001's headline numbers survive primary-source validation — and which are
artefacts of a claimed denominator, an unsourced physical constant, or an extraction
defect that 001 identified but could not repair?**

**Claim**: 001's headline conclusions rest on a narrower base of `DEMONSTRATED` inputs than their stated precision implies — three payload denominators underpinning the sector's cost conclusions are `CLAIMED` rather than filed, the constitution's named binding constraint for orbital compute (F2) rests on an admitted placeholder and an unclosed heat-pump loop, and the platform's XBRL extraction carries a measured defect (DA-23) whose remedy has been applied to 12 issuer-quarters rather than the universe; validating these inputs will either confirm 001's conclusions within a quantified band or restate them, and the answer determines how much precision any downstream thesis is entitled to.

> **Format note 2026-09-19.** This claim must stay on **one line**.
> `synthesize_report.py:133` extracts it with `^\*\*Claim\*\*:\s*(.+)$` under
> `re.MULTILINE`, and `.+` does not cross a newline — so a wrapped claim reaches the
> report cover **truncated mid-sentence**, which is exactly what the first build of
> 002's report shipped. Thesis 001's claim is a single line for the same reason.
> Any rewording must preserve this.

> **Added 2026-09-19.** The claim was present in `thesis.md`'s frontmatter but absent from
> this spec as a `**Claim**:` line, which is the form the report packer reads
> (`synthesize_report.py:_header_facts`). Without it the report cover printed
> `claim: (none)`. No wording is new — this is the thesis's own stated claim, moved to where
> the toolchain reads it.

The premise is uncomfortable and worth stating plainly: **001's conclusions are more
precise than their inputs justify.** Three of the sector's headline figures rest on
denominators that are `CLAIMED` rather than filed; the constitution's *named binding
constraint for orbital compute* (F2) rests on two constants, one of which is an
admitted placeholder; and the platform's own XBRL extraction has a measured defect
(DA-23) that inverts any loss/profit ranking. Under **P4**, `MODELED` can never satisfy
a falsifier — so an unvalidated number is a pillar that cannot fire.

This thesis therefore produces no position and no valuation. Its output is a
**validation ledger**: every headline figure in 001's register, re-graded, with the
survivors separated from the artefacts.

### Why this thesis exists at all

The alternative was to let 003–011 inherit 001's numbers unexamined. That would
propagate three specific errors into every downstream valuation:

1. **A denominator error becomes a sector conclusion.** Electron's 300 kg payload is
   `CLAIMED`. It is the divisor of the *only demonstrated per-launch cost in the
   universe*. A ±15% error in the denominator is a ±15% error in basis B — and basis B
   is what let PIL-1 close without a model.
2. **An unsourced constant becomes a thesis.** F2's radiator areal density is 8 kg/m²
   *as a placeholder*, and its rejection-temperature table excludes heat-pump COP. F2
   is the binding constraint for the sector's largest narrative (orbital compute).
3. **An extraction defect becomes a ranking.** DA-23 is registered at v1.3.0 with a
   remedy, but the remedy has not been *applied across the universe* — only
   spot-checked on the 12 issuer-quarters 001 happened to examine.

---

## 1b. Pillars

### Pillar 1 — The three CLAIMED denominators resolve, and the $/kg conclusions hold within ±15% (Priority: P1) 🎯 Minimum Defensible View

001's launch-cost conclusions divide by payload masses that no issuer filed. Electron's
**300 kg**, Falcon 9's **22.8 t** and Starship's **100 t** are all `CLAIMED` figures
drawn from press and company material. RKLB's artifact flags this explicitly: *"seek a
filed source"*, noting ±15% moves every Electron number ±15%.

**The claim:** each denominator can be replaced with a **filed or manifest-sourced**
value — a NASA launch manifest, a range safety document, an FCC/ITU filing, a
customer contract, or the issuer's own SEC disclosure — and when it is, **the
demonstrated $/kg to LEO moves by less than 15%**. If so, PIL-1's conclusion survives
validation with a quantified band instead of an unstated assumption. If not, the band
must widen and every downstream cost figure restates.

**Why this priority**: it is the Minimum Defensible View because it protects the
workspace's single most load-bearing conclusion. PIL-1 is the only pillar 001 closed
*without* a model, and it closed on a claimed divisor. Everything in 003 and 005 — the
sector cost curve and the launch pure-plays — inherits it.

**What counts as resolution.** A source is admissible if it is a government manifest,
a filed document, or a customer contract. A company webpage stating its own payload
capacity is **not** adjudication — it is the same class of evidence as the original
claim. Where no independent figure exists, the denominator is recorded
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` and the ±15% test is reported as **not met**, not
as passed by default.

**Independently falsifiable**: a filed or manifest denominator that moves the
demonstrated $/kg by more than 15%.

**wrong_if**: `metric=abs_pct_change_in_demonstrated_price_per_kg_to_LEO_after_denominator_validation threshold=0.15 source=government_launch_manifest_or_issuer_filing op=>`

**⚠️ THE FALSIFIER AS WRITTEN FIRES ON ITS OWN QUESTION — corrected in Phase 1.** Three
defects were measured against RKLB, and all three are structural rather than incidental:

| # | Defect | Measured | Correction |
|---|---|---|---|
| **1** | **The `abs()`/`op=>` form is direction-blind.** Basis A can move **down** — at the circulating HASTE-ASP proxy it restates **−31.3% to $20,833/kg**. As written, *"restated upward, thesis strengthened"* and *"restated downward, thesis threatened"* register **identically**. | Confirmed | **A directional split is required**: report `up` and `down` separately, with the up-moves marked as strengthening and the down-moves as threatening. |
| **2** | **The test is not discriminable at quarterly frequency.** DA-25 escalated: **Q2 2025 had *zero* HASTE missions and RKLB's disclosed figures still diverged from the audited segment table by −15.3% (revenue) and −22.9% (cost).** Across four periods the gap ranges **−22.9% to +22.5% with no HASTE correlation** — so the divergence is the metric's **period-normalisation**, not the mission mix. | The metric's own noise is **±20%-class** — *larger than the 15% threshold* | **Evaluate at H1 or FY only.** A ±15% test against a quarterly RKLB figure cannot separate a denominator restatement from the metric's own noise. |
| **3** | **Two channels each move $/kg by ≥50%, and the filing closes neither.** **Channel O**: ~200 kg to SSO against 300 kg to low-inclination LEO → **+50.0%**, and *contradicted* by the 10-K's own "38 to 120 degrees" envelope. **Channel M**: **2 of 6** Q2 "Electron launch missions" were **HASTE — suborbital, 0 kg to LEO**, so a third of the Q2 denominator delivered nothing to orbit. Combined corner: **+125%**. | Falsifier fires | **Disposition: `unresolvable: true` / `UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — the *capacity* denominator resolved (300 kg, filed, Δ = 0.00%); the *±15% stability test* did not. |

**What survives, and it is the important part.** Every open channel on basis B is
**one-signed upward** — a capacity ceiling is the *largest* denominator the vehicle can
carry, so it **understates** cost per kilogram. **The residual flatters the metric, not the
thesis.** PIL-1's conclusion is strengthened by the uncertainty rather than threatened:
`$14,667/kg` and `$30,333/kg` are **floors**.

**Also recorded:** **DA-01 basis C is structurally unconstructible** for a vertically
integrated issuer, with a filed reason — *"Management does not regularly review either
reporting segment's total assets or operating expenses"* (`sec109` p.33). **Do not wait
for it.**

**Subscribed**: `RKLB × unit-economics`, `RKLB × operational-kpi`, `SPCX × unit-economics`, `SPCX × operational-kpi`, `FLY × unit-economics`

---

### Pillar 2 — F2's unsourced constants are replaced or bracketed, and the radiator mass per MW is bounded (Priority: P2)

The constitution names F2 — radiative heat rejection — as **the binding constraint for
orbital compute**. 001's Phase 2 derivation is sound in structure and rests on two
inputs that are not sourced:

| Input | 001's value | Status |
|---|---|---|
| Radiator areal density | **8 kg/m²** | **Admitted placeholder** in the Phase 2 cross artifact |
| Heat-pump COP at elevated rejection temperature | not applied | F2's table is **rejection-side only**; a heat pump that raises T_rad also consumes power, which becomes *more* heat to reject |

The gap matters because F2's headline is a *temperature* argument: radiator area falls
**7.7×** going from 300 K to 500 K (2,419 m²/MW → 313 m²/MW), which is the entire
quantitative case for nuclear (BWXT). If a heat pump is required to reach 500 K, its
own power draw and its own waste heat must be added back — and 001 never closed that
loop.

**The claim:** both inputs can be **replaced with cited values or bounded to a stated
interval** from peer-reviewed literature, flown-hardware disclosure, or a disclosed
spacecraft thermal subsystem mass. The resulting **radiator mass per MW** carries an
explicit uncertainty band, and the F2 nuclear case is restated *with* the COP penalty
rather than without it.

**Why this priority**: F2 is the constitution's named binding constraint, it governs
the sector's largest narrative, and it is currently the most-cited number in the
workspace resting on a placeholder. It is P2 rather than P1 only because P1 protects a
*closed* pillar while P2 corrects an *open* one.

**Independently falsifiable**: the sourced input set yields a radiator-mass band wider
than ±50%, meaning F2 cannot support a quantitative conclusion at all and must be
downgraded to a qualitative bound.

**wrong_if**: `metric=f2_radiator_mass_per_MW_uncertainty_band_pct threshold=0.50 source=peer_reviewed_literature_or_flown_hardware_disclosure op=>`

**Subscribed**: `BWXT × secular-trends`, `GOOG × secular-trends`, `NVDA × secular-trends`, `VRT × unit-economics`, `MRCY × secular-trends`, `BWXT × supply-chain`, `MRCY × supply-chain`

---

### Pillar 3 — The six-defect Data-Integrity Register is applied universe-wide, and its open candidates resolve (Priority: P3)

**Scope corrected upward during specification.** When this pillar was first drafted the
register held one defect (DA-23, sign stripping) on a 12-issuer-quarter census. The
universe-wide sweep that extended that census found **five more defects in the same
period-and-sign extraction layer** — and established that they **compound**. The pillar
is therefore scoped to the whole register, not to sign stripping.

| Defect | Coverage | The reason it cannot be patched in isolation |
|---|---|---|
| **DA-23** sign stripping | **6 of 6 loss-making stripped; 19 of 19 profitable clean** | Three detectors now registered in descending reliability. The **EPS × shares test is inadmissible** — it passes on both sides of a flip at RKLB, FLY *and* VOYG. |
| **DA-24** asset-sale contamination | SATS | Independent of DA-23 — SATS is contaminated but not stripped. |
| **DA-25** normalised per-unit metrics | RKLB | The disclosed `revenue per launch` implies 51.6% GM; the audited segment table implies 42.9%. |
| **DA-26** annual mislabelled as quarterly | **Universal — 19 of 19 issuers** | The mislabelled period **VARIES by issuer** (HWM `Q4`/`Q1`, TDG `Q3`), so it **cannot be screened by row position**. A "# ignore the Q4 row" checker passes the issuers it was written for and fails the rest. |
| **DA-27** calendar-derived fiscal labels | **n = 4 of 4** — partitions the population perfectly by fiscal year-end | Wrong **LABEL** on internally-consistent values; DA-26 is a wrong **VALUE** in a quarter row. Different blast radii, different remedies. |
| **DA-28** IPO capital-structure discontinuity | HAWK | Four share counts in one extract; EPS bridge fails by 72% against sub-1% for clean issuers. **There is no clean read on recent listings** — HAWK has no post-IPO quarterly history to fall back on. |

**Two specific loose ends this pillar owns:**

1. **The coverage hole.** `OperatingIncomeLoss` is **absent or segment-only at MRK, BMY
   and WWD**. On those three issuers **no detector can run.** This is a distinct hazard
   from a wrong value: an artifact that treats absence as zero, or as a clean read, fails
   **silently**. The pillar's obligation is to record these as
   `UNRESOLVABLE-FROM-PLATFORM` rather than as passed checks.
2. **The three open candidates** — BA 2025 Q3 (net-loss bridge confirmed, margin
   unverified), LUNR (RESOLVED: annual row mislabelled Q4; component identity RUNS — see §2)
   — no gross profit line), and **VOYG** — ⚠️ **MIS-CLASSIFIED HERE, CORRECTED IN PHASE 3: VOYG is the PLAINEST DA-23 sign strip in the register, not a different sub-mechanism.** `us-gaap:OperatingIncomeLoss` stores a filed `Loss from operations` of **$(51,408)K** as its absolute value; the component identity closes **17 of 17 periods, zero failures**. **The error in the original classification: the gross-profit bound was applied to the SIGN-STRIPPED MAGNITUDE (51.408 > 4.457 fires correctly), and the violation was then treated as MUTUALLY EXCLUSIVE with sign-stripping. It is not** — a sign-stripped loss whose magnitude exceeds gross profit fails the bound too. Restored, `−51.408 < +4.457` violates nothing. **⚠️ AND THE TRAP WARNING BELOW WAS INVERTED: VOYG is CAUGHT by a sign test and MISSED by a bound-only test.** The bound is a **SCREEN, not a classifier** — it fires on **16 of 17 periods**, continuously since FY2024, not "three consecutive quarters." Each candidate is
   either explained or registered as a further defect.

**The claim:** every universe issuer is tested against the **register as a whole** — not
against DA-23 alone — **zero remain unresolved or silently passed**, and each open
candidate is either explained or promoted to a registered defect.

**Why this priority**: any downstream thesis screening on `operating_income`, or
building a quarterly trend from the metrics block, is wrong without this. **DA-26 alone
contaminates every quarterly series in the universe**, and it was invisible until the
census was extended.

**Note the two discarded tests.** `EPS × shares` is inadmissible as a sign test
(passes on both sides of a flip at RKLB, FLY, VOYG) **and** needs a listing-date guard
(DA-28) or it false-positives on recent listings. Neither disqualification was known
when this thesis was scoped.

**Independently falsifiable**: any issuer-quarter whose defect status cannot be
established, or any defect discovered after this thesis closes that was present in the
data it examined.

**wrong_if**: `metric=count_of_universe_issuer_quarters_with_unresolved_defect_status threshold=0 source=data_integrity_register_application op=>`

**Subscribed**: `YSS × recent-quarter`, `YSS × operational-kpi`, `RKLB × recent-quarter`, `FLY × recent-quarter`, `SPCX × recent-quarter`, `IRDM × recent-quarter`, `VRT × recent-quarter`, `GOOG × recent-quarter`, `MSFT × recent-quarter`, `NVDA × recent-quarter`, `BWXT × recent-quarter`, `MRCY × recent-quarter`, `UTHR × recent-quarter`, `SATS × recent-quarter`, `VOYG × recent-quarter`, `LUNR × recent-quarter`, `HAWK × recent-quarter`, `BA × recent-quarter`

---

### Pillar 4 — SPCX's 1.4 GW nameplate restates to a facility draw, and the restatement is computable (Priority: P4)

Constitution **DA-11** records the trap: SPCX's stated **1.4 GW** compute draw is
**IT load only**, *"explicitly excluding cooling, power distribution losses, lighting,
security and facility overhead."* 001's SPCX artifact calls this *"the most dangerous
figure in this thesis"* and escalates it as **plan risk #2**, requiring a
cooling-inclusive restatement before Phase 6.

The figure matters because it is the numerator of the one like-for-like comparison the
orbital-compute debate actually turns on: **1.4 GW of ground-based AI compute at SPCX
against MSFT's ~2.9–11.6 GW of annual new-build capacity.** Comparing an IT-load
number against a capex-derived number is comparing two different quantities.

**⚠️ The claim as written is WRONG, and Phase 1 found the input the specification missed.**
This pillar asserted the ratio *"lands within 1.2–1.5×"*. Measured against a source the
spec never read — the **Q2 2026 earnings call (`ect1` p.4)**, where facility-side power is
disclosed against the same compute basis — the ratio is **1.50× expected and 2.00×
tentative target**, giving a restated facility draw of **2.1 GW central / 2.8 GW at the
issuer's own target, against 1.4 GW as filed.** **So the falsifier FIRES on the target
reading and sits exactly at threshold on the expected one: the 1.2–1.5× claim holds at the
floor and fails at the ceiling.** Recorded rather than quietly widened — a claim that
survives only on its most favourable reading is not the claim that was made.

**A second correction: DA-11's quantity is narrower than "IT load."** The 1.4 GW is **GPU
nameplate** — it excludes host CPUs, DRAM, NICs, storage and PSU losses *as well as*
cooling. So there are two readings, and the artifact reports both.

**The claim (restated):** the facility draw can be restated from disclosed inputs, and the
ratio is **1.50× expected / 2.00× at target** — i.e. the restatement *does not* land inside
the conventional hyperscale band, which is itself the finding.

**Why this priority**: P4 rather than P1 because the comparison is directional rather
than knife-edge. Even at the top of the range, MSFT's annual build dwarfs SPCX's
cumulative base; the restatement sharpens the argument without changing its sign. That
is exactly why it can be deferred one priority level.

**Independently falsifiable**: a disclosed or benchmarked PUE for SPCX-class AI
facilities outside 1.2–1.5×.

**wrong_if**: `metric=spcx_facility_pue_ratio threshold=1.5 source=issuer_disclosure_or_industry_PUE_benchmark op=>`

**Subscribed**: `SPCX × operational-kpi`, `SPCX × business-model`, `VRT × unit-economics`, `MSFT × recent-quarter`

---

### Pillar 5 — At least half of 001's headline figures convert from `CLAIMED`/`MODELED` to `DEMONSTRATED` (Priority: P5)

The meta-pillar, and the one that measures whether this thesis achieved anything. 001's
register is honest about its own evidence quality — and the honest reading is that a
large share of its headline numbers are `CLAIMED` (roadmaps, press figures, company
assertions) or `MODELED` (our own derivations). Under P4 those cannot satisfy a
falsifier, so a register that is majority-`MODELED` is a register of **untestable
pillars**.

**The claim:** a **validation ledger** tracking every headline figure from 001's
artifacts and thesis.md shows **≥50% moved to `DEMONSTRATED`** by the end of this
thesis, with the residue explicitly classified into the two disposition classes.

**Why this priority**: it is last because it is the *aggregate* of P1–P4 plus the loose
ends — it cannot be pursued directly, only accumulated. Its value is as the thesis's
own scorecard, and as the honest input to 011's sizing: a book sized on `MODELED`
numbers should be sized smaller than one sized on `DEMONSTRATED` ones.

**Independently falsifiable**: fewer than half of 001's headline figures convert.

**⚠️ What counts as a conversion — clarified at the implement preflight (CHK004).** A
figure that **P6 classifies boundary-contaminated**, or that **P2 leaves unbounded**, does
**not** convert to `DEMONSTRATED` — it becomes `DERIVED` or stays `CLAIMED`. This matters
because it means **P6 succeeding can push P5's share *down*.** That is not a contradiction:
the conversion share is a measure of the **evidence base**, not of effort, and it is
*supposed* to fall when figures turn out to be contaminated. Had this not been stated, two
pillars could each have counted the same figure in opposite directions.

**wrong_if**: `metric=share_of_001_headline_figures_converted_to_DEMONSTRATED threshold=0.5 source=validation_ledger op=<`

**Subscribed**: `SPCX × ratio-analysis`, `RKLB × ratio-analysis`, `VRT × ratio-analysis`, `GOOG × ratio-analysis`

---

### Pillar 6 — Every SPCX-dependent finding is checked for entity-boundary contamination (Priority: P6 — inserted at specification review)

**Added after reading 001's published synthesis**, which carries this as carry-forward 0b
and leaves it unresolved: *"REVIEW EVERY SPCX-DEPENDENT FINDING FOR ENTITY-BOUNDARY
CONTAMINATION."*

SPCX's reporting entity changed **four times inside the comparison window**: the **xAI
merger (2026-02-02)**, the **X merger (2025-03-28)**, the **June 2026 IPO**, and the
**pending ~$60B all-stock Cursor acquisition** (announced, closing Q3 2026). Under
common-control accounting, **prior periods are recast**, so **any growth rate spanning
those boundaries mixes real growth with entity change** — and the mixture is
unguessable from the growth rate alone.

**Why this is a validation pillar and not a footnote.** SPCX is the workspace's anchor
entity (P1). Its figures are cited by 003, 004, and 009. If a headline growth rate is
partly an artefact of recasting, **every downstream thesis that quotes it is
mis-specified** — and this is the same class of hazard as DA-23: a number that is
internally plausible, silently wrong, and load-bearing.

001's own synthesis already applies the test once and finds that **the Space-segment
series is the one that survives the boundary — and it is the one that fell.** That is a
single application, not a systematic review.

**The claim:** every SPCX figure quoted across a merger or IPO boundary is classified as
**boundary-clean** or **boundary-contaminated**, with the specific recasting event named;
contaminated figures are either restated on a comparable basis or **flagged and excluded
from growth-rate claims**.

**⚠️ The named case, added at clarify round 2 (2026-09-18).** The workspace currently
quotes **"AI is 32.8% of SPCX revenue"** as evidence that value migrated out of launch.
**That figure is boundary-contaminated.** The AI segment contains xAI, merged
**2026-02-02 under common control** — which recasts prior periods — so the segment's
growth mixes organic expansion with an entity that was not previously inside the
reporting entity. **It may not be quoted as evidence of organic migration** without the
restatement.

| SPCX series | Boundary status | May be quoted for migration? |
|---|---|---|
| **Space** (launch, Dragon) | **Clean** — the one series that survives the boundary | **Yes** — and it is the one that *fell* (−1.9% H1) |
| **Connectivity** (Starlink) | **Clean** — never merged; wholly organic to SPCX | **Yes** (54.9% of revenue) |
| **AI** | **Contaminated** — xAI merged 2026-02-02, common control, prior periods recast | **No** — report as `contaminated`, restate or exclude |

**This strengthens the main line rather than weakening it**: the migration claim rests on
**Space falling** and **Connectivity's organic scale**, not on the contaminated AI figure.
But every artifact quoting "AI 32.8%" must carry the flag, and the figure is a worked
example of why this pillar exists.

**Independently falsifiable**: an SPCX growth rate quoted in a downstream 001 result
that cannot be classified as either clean or contaminated.

**wrong_if**: `metric=count_of_spcx_growth_figures_unclassified_for_entity_boundary_effects threshold=0 source=spcx_10q_segment_and_restatement_disclosures op=>`

**Subscribed**: `SPCX × business-model`, `SPCX × recent-quarter`, `SPCX × operational-kpi`

---

### Pillar 7 — Every 001 falsifier is classified as evaluable, platform-blocked, or source-blocked (Priority: P7)

001 left **six** `wrong_if` criteria, several of which were never evaluated. Their
current states are heterogeneous and were never systematically classified:

| PIL | Falsifier state per 001 |
|---|---|
| PIL-1 | **HOLDS on A, A′ and C; NOT EVALUABLE on B** |
| PIL-2 | PENDING — depends on catching a disclosure that may coincide with an immaterial-to-counterparty initiative |
| PIL-3 | **PENDING / UNMEASURED** — needs ~19 issuer risk-factor reads; 001 proposed re-scoping to two cheaper tests |
| PIL-4 | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — the clearest case in the workspace |
| PIL-5 | PENDING — terrestrial denominator is commercially licensed |
| PIL-6 | **`UNRESOLVABLE-FROM-PLATFORM`** — needs FCC IBFS / ITU sources the platform does not carry |

Two of these are **structural**, not temporary: PIL-4's data does not exist publicly,
and PIL-6's data is public but unreachable. A downstream thesis that plans around
"the falsifier will fire" is planning around something that cannot happen.

**The claim:** each of the six is classified against the v1.3.0 disposition classes
with the **specific** disclosure or source that would resolve it named explicitly, and
any falsifier that is structurally unreachable is replaced with a **proxy test** that
is evaluable — or the pillar is re-scoped rather than carried as unbounded.

**Why this priority**: last because it is bookkeeping with a strategic payoff. Its
output is what stops 011 from sizing against a catalyst that cannot occur.

**Independently falsifiable**: any falsifier that cannot be placed in one of the three
classes with a named resolving source.

**wrong_if**: `metric=count_of_001_falsifiers_unclassified_or_without_named_resolving_source threshold=0 source=validation_ledger op=>`

**Subscribed**: `SATS × risk`, `SATS × competitive`, `SPCX × risk`, `IRDM × competitive`, `UTHR × unit-economics`, `YSS × operational-kpi`

---

> **Delivering P1 alone yields a defensible partial conclusion** — the launch-cost
> conclusions rest on validated denominators with a stated band, or they do not. That
> is the single most valuable output of this thesis and it is delivered first.

## 1c. Method — the validation instruments

Three capabilities are specific to this thesis and are not used elsewhere in the
program. They are the reason a validation thesis is a distinct workstream rather than
a review pass.

1. **XBRL calculation-arc cross-validation.** `validate_calculation` and
   `get_calculation_tree` compute `SUM(child × weight)` for each parent concept and
   compare against the reported fact. This is the **automated form of the component
   identity** that DA-23's remedy requires, and it is the cheapest way to test every
   issuer-quarter at once rather than one at a time. **P3 is primarily delivered by
   this instrument.**
2. **Definitional re-basing.** Every headline $/kg and $/kW figure is restated on all
   competing bases per the §1c standing rule. A figure whose basis is unstated is
   treated as **unvalidated**, not as validated at its face value.
3. **`CLAIMED` → source substitution.** For each CLAIMED figure, the artifact names
   the *specific* document class that would settle it, then attempts retrieval. Where
   retrieval fails, the figure is classified, not silently retained.

**Evidence discipline.** Per P4 and the v1.3.0 register, an artifact that reads
`operating_income` shows the component derivation in-line. `EPS × shares` is **not** a
valid sign test and its use is a defect, not a shortcut.

**Correction policy.** Where this thesis invalidates a 001 figure, the 001 artifact is
**not** rewritten. 001's files are frozen; the correction is recorded here and cited by
location. This preserves the audit trail that makes 001's own in-place corrections
legible.

## 1d. Citation requirement — binding, added at clarify round 3 (2026-09-18)

**Every material figure and fact in a 002 artifact must carry a clickable citation to the
source page.** This is a hard contract requirement, not a style preference: the thesis's
entire output is a claim about what is *demonstrated*, and a `DEMONSTRATED` grade with no
reachable source is unverifiable by construction.

### The canonical form

Per the platform contract `contracts/citation-and-memory.md`:

```
[📄 {ticker} {form_type} p.{N}](https://agentii.ai/v/{ticker}/{citation_id}/{N})
```

**Example, verified against this workspace's own anchor filing:**
`[📄 SPCX 10-Q p.43](https://agentii.ai/v/SPCX/sec8/43)`

> **⚠️ The ticker is NOT optional, and this is the one place the round-3 instruction was
> followed against its literal wording.** The short form `agentii.ai/v/{citation_id}/{page}`
> **does not resolve.** The portal route is `agentii.ai/v/{ticker}/{citation_id}/{N}`, which
> redirects to `api.agentii.ai/v1/view_document/{ticker}/{citation_id}?page_no=page{N}` and
> resolves the document via `pipeline.src_documents JOIN pipeline.sec_filings`. Without the
> ticker the join cannot be performed. **Six independent places in the plugin contracts
> include the ticker; none omits it.** If a ticker-less route exists that this workspace
> cannot see, this is a one-line change — but shipping the short form would have produced
> broken links in every artifact.

### What must be cited

| Requires a citation | Does NOT |
|---|---|
| Every inherited figure this thesis validates (P1–P4) | `MODELED` derivations of our own — cite the **inputs** instead |
| Every Data-Integrity Register finding (DA-23/24/26/27/28) | Restatements of 001's conclusions — cite the **001 artifact**, per §0 |
| Every falsifier observation and its page | Physical constants (cite the standard instead) |
| Every claim graded `DEMONSTRATED` | `CLAIMED` figures where no source exists — those are recorded `UNRESOLVABLE`, not cited |

**Failure mode.** An artifact asserting a `DEMONSTRATED` figure with no citation **fails
the contract** (`uncited_demonstrated_figure`, level `fail`). There is no warning tier:
under P4 a `DEMONSTRATED` grade is a claim about a source, and the source is the evidence.

### Verified citation IDs for the anchor figures

Retrieved at specification time so the pattern is **demonstrated rather than described**.
Every one resolves. Page numbers were located via `search_keyword_in_source`, not guessed.

| Figure | Source | Citation |
|---|---|---|
| Three reportable segments; IPO; Cursor Merger | SPCX 10-Q, **p.34** | `https://agentii.ai/v/SPCX/sec8/34` |
| **Mass to orbit, launches, Starlink subscribers, ARPU** — the key business metrics | SPCX 10-Q, **p.35** | `https://agentii.ai/v/SPCX/sec8/35` |
| **AI nameplate compute draw** (the DA-11 figure) | SPCX 10-Q, **p.36** | `https://agentii.ai/v/SPCX/sec8/36` |
| **Connectivity: revenue $4,291M (+65.8%), income from operations $1,656M (+79.4%)**, ARPU decline | SPCX 10-Q, **p.43** | `https://agentii.ai/v/SPCX/sec8/43` |
| R&D / SG&A / loss from operations — AI data center expansion and Starship attribution | SPCX 10-Q, **p.41** | `https://agentii.ai/v/SPCX/sec8/41` |
| **Segment reporting tables — revenue and income from operations by segment** (the DA-23 identity) | SPCX 10-Q, **p.30** | `https://agentii.ai/v/SPCX/sec8/30` |
| Consolidated revenue $7,814M (+91.9%); net loss $541M | SPCX 10-Q, **p.40** | `https://agentii.ai/v/SPCX/sec8/40` |
| Cash flow: operating **+$3,466M**, investing **$(34,487)M**, financing **+$100,291M** | SPCX 10-Q, **p.50** | `https://agentii.ai/v/SPCX/sec8/50` |
| Nature of business; three segments; IPO at $135.00; xAI and X common-control mergers | SPCX 10-Q, **p.11** | `https://agentii.ai/v/SPCX/sec8/11` |
| **Entity-boundary evidence** — IPO proceeds $85,675M, xAI Merger transactions (P6) | SPCX 10-Q, **p.7** | `https://agentii.ai/v/SPCX/sec8/7` |

> **One structural finding surfaces from this table.** Every SPCX figure above resolves to
> **a single document** — `sec8`, the Q2 2026 10-Q. **SPCX has exactly one 10-Q on the
> platform.** The anchor thesis's entire evidence base, including the A1b falsification the
> constitution now rests on, traces to **one filing**. That is not a defect, but it is a
> concentration worth naming: a restatement or a re-read of `sec8` would move the whole
> program, and there is no second source to corroborate against.

### ✅ The requirement was executed once at specification, and it re-verified four anchor figures

Rather than specify the citation rule and stop, the anchor row was **fetched**:
`read_source_pages(SPCX, sec8, page43)` returned the Connectivity table directly. It
confirmed, from the primary source and independently of any 001 artifact:

| Figure 001 inherited | What `sec8/page43` actually says |
|---|---|
| Connectivity revenue **$4,291M (+65.8%)** | Revenue **$4,291M** vs $2,588M — **+65.8%** ✓ |
| Income from operations **$1,656M (+79.4%)** | Income from operations **$1,656M** vs $923M — **+79.4%** ✓ |
| Starlink subscribers **+101.2%**, ARPU **−22.4%** | *"101.2% growth in Starlink subscribers, offset by a 22.4% decline in Starlink subscriber ARPU"* ✓ |
| Consumer **+$764M** vs enterprise **+$939M** | *"an increase of $764 million in revenue from our consumer subscribers… as well as an increase of $939 million in our government, aviation, maritime, and other enterprise businesses"* ✓ |

**Four for four.** This is the argument for the requirement rather than an illustration of
it: **adding the citation forced a re-check that confirmed the numbers**, and it converted
four inherited figures from `DEMONSTRATED (per 001)` to **`DEMONSTRATED (read-verified at
source)`** — a different and stronger grade. It also located the ARPU attribution: the
decline is *"primarily due to international expansion and the addition of lower priced
service plans,"* which is the DA-10 mix-shift reading that 001 flagged as unresolved. The
filing states the cause, so **DA-10's ambiguity resolves in favour of mix-shift, not price
erosion** — a finding this thesis did not set out to obtain and would not have obtained
without the citation work.

**Consequence for the artifact contract:** `located_via` records *how* the page was found,
and a page located only by keyword carries less weight than one confirmed by reading the
page. Both are admissible; the distinction is recorded rather than flattened.

**Citation IDs for the other universe names**, resolved at specification time and to be
page-located by the artifact author at read time:

| Ticker | Filing | `citation_id` |
|---|---|---|
| RKLB | Q2 2026 10-Q (report 2026-06-30) | `sec109` |
| RKLB | Q1 2026 10-Q (report 2026-03-31) | `sec104` |
| YSS | Q2 2026 10-Q | `sec12` |
| YSS | **Q1 2026 10-Q — the $110.466M anomaly lives here** | `sec9` |
| PL | Q1 FY2026 10-Q (report 2026-04-30) — the 1.69× break-even source | `sec76` |

## 2. Universe Definition

Deliberately narrow, and **not** the full 57-name universe. A thesis is included only
if it contributes a figure to the validation ledger. Weights are analytical effort, not
positions — this thesis sizes no trades.

| Ticker | Company | Sector | Weight | Why it is in this thesis (and the figure it validates) |
|---|---|:---:|---|
| SPCX | SpaceX | industrial.aerospace_defense | 18% | **Largest validation surface**: Falcon 9's 22.8 t denominator, Starship's 100 t, the DA-11 1.4 GW nameplate (P4), and the segment reconciliation that produced the DA-23 census |
| RKLB | Rocket Lab | industrial.aerospace_defense | 16% | **Electron's 300 kg denominator (P1)** — the divisor of the universe's only `DEMONSTRATED` per-launch cost. Also DA-25's normalised `revenue per launch` |
| FLY | Firefly Aerospace | industrial.aerospace_defense | 8% | Alpha's payload denominator; DA-23 flip instance; EGC disclosure-quality variable |
| BWXT | BWX Technologies | industrial.nuclear_energy | 10% | **F2's nuclear case (P2)** — the 24× area reduction rests on the unsourced COP and areal-density inputs |
| GOOG | Alphabet | tech.platform_internet | 8% | Suncatcher's compute-per-satellite figure — 001 found it **not stated**, making PIL-2's falsifier untestable against the sector's most detailed disclosure |
| VRT | Vertiv | industrial.machinery | 8% | Terrestrial thermal comparator; supplies the PUE benchmark for P4 |
| MSFT | Microsoft | tech.platform_internet | 6% | The capex-derived capacity figure that P4's restatement is compared against |
| NVDA | NVIDIA | tech.semiconductors | 6% | The H100 thermal-failure datapoint and the $/kW cost stack |
| MRCY | Mercury Systems | industrial.aerospace_defense | 5% | The 0.03% margin edge case where a sign error is **invisible by inspection** |
| YSS | York Space Systems | industrial.aerospace_defense | 8% | **P3's named anomaly** — the $110.466M operating figure on $116.343M revenue |
| UTHR | United Therapeutics | med.medicines_biotech | 4% | The clearest `UNRESOLVABLE-FROM-PUBLIC-SOURCES` case (P6) and the 87.3% gross-margin benchmark |
| SATS | EchoStar | tech.telecom_services | 5% | DA-24 asset-sale contamination, and proof that DA-23 and DA-24 are independent |
| VOYG | Voyager Technologies | industrial.aerospace_defense | 4% | **DA-23 candidate and a new sub-mechanism** — not a sign inversion but an unreconcilable **level**: `OperatingIncomeLoss` $51.408M against gross profit $4.457M, failing the gross-profit bound by **$46,951M** across three consecutive quarters |
| LUNR | Intuitive Machines | industrial.aerospace_defense | 3% | **RESOLVED in Phase 3 — and this spec row was WRONG.** The 42.1% is the **absolute value of LUNR's FY2025 *ANNUAL* operating margin mislabelled as Q4 2025** (DA-26 + DA-23 + an unregistered **revenue-basis truncation**). **The claim "no quarterly gross-profit line exists, so the component identity cannot run" is false** — all four detectors run; the error came from a **concept-name trap** (`GrossProfit` returns zero facts, so `CostsExpenses` was never tried). `Revenues − CostsExpenses = −87,231,000` vs reported `+87,231,000`, **closing exactly twelve for twelve periods.** **DA-23 CONFIRMED, instance #7.** |
| HAWK | HawkEye 360 | industrial.aerospace_defense | 3% | **DA-28 site** — four non-agreeing share counts (4.2M–98.0M) in one extract; EPS bridge fails by **72%** against sub-1% for clean issuers, because a Q2 2026 listing straddles two capital structures |
| BA | Boeing | industrial.aerospace_defense | 3% | **DA-23 flip instance #5** (−5,761 → +5,761) **and a DA-23 candidate** — 2025 Q3 net-loss bridge confirmed but the margin remains unverified, so it is resolved by detector 3 (margin plausibility) only |
| IRDM | Iridium Communications | tech.telecom_services | 4% | **DA-23 control group** — one of the 19 issuer-quarters where the profitable side is clean (+34.0 → +34.0). The positive control matters: a detector that clears everything is not a detector. Also **P11 deal security** (RKLB acquiring at $54/sh) |

**Four of these seventeen names are in the universe for a single reason: they are defect
sites, not research subjects.** VOYG, LUNR, HAWK and BA each carry an open register item
that no other thesis can resolve, because no other thesis reads the extraction layer.
They are included at low weight for that purpose alone — not as businesses.

**Excluded by design:** the remaining universe names have no figure in the validation
ledger. Including them would turn this into a second general baseline and repeat 001 —
the failure mode this program exists to avoid. Names enter this thesis when a *specific*
figure of theirs is contested, not because they are in the universe.

## 3. Skill Deployment Matrix

| Skill | Vertical | Depth | Tickers | Market Data Stage | Purpose |
|---|---|:---:|---|:---:|---|
| unit-economics | business-intelligence | Deep | RKLB, SPCX | none | Rebuild $/kg from filed components on all DA-01 bases; test the denominator sensitivity that **P1** turns on |
| operational-kpi | business-intelligence | Deep | SPCX, RKLB, YSS | none | Payload masses, launch counts, mass-to-orbit restated on DA-07/DA-08 bases; the DA-11 nameplate restatement (**P4**); YSS's $110.466M operating figure |
| secular-trends | equity-research-core | Standard | BWXT, GOOG, NVDA, MRCY | none | F2's nuclear path and Suncatcher's compute-per-satellite claim, graded against sourced physics (**P2**); NVDA's H100 thermal datapoint; MRCY's 0.03% margin. **Reduced from Deep to Standard at plan evaluation** — see `plan.md` §Evaluation. `secular-trends` at **Deep expands to 8 modes**, five of which (EV-trend, quantum/renewable, strategic-position, capacity-and-readiness, market-perception) **cannot source a physics constant**, which is what P2 asks for. Kept as a **single row**: splitting it into Deep+Standard rows caused the generator to silently drop one, leaving BWXT — the name carrying P2's nuclear case — with **zero** secular-trends tasks |
| recent-quarter | equity-research-core | Standard | SPCX, RKLB, FLY, BWXT, GOOG, VRT, MSFT, NVDA, MRCY, YSS, UTHR, SATS, VOYG, LUNR, HAWK, BA, IRDM | none | **The register is applied here** — `validate_calculation` / gross-profit bound across every issuer-quarter, all seventeen names, three detectors (**P3**) |
| ratio-analysis | quantitative-analysis | Standard | SPCX, RKLB, VRT, GOOG | none | Cross-check every derived ratio against the component identity; catches DA-23/DA-24 residuals (**P3**, **P5**) |
| unit-economics | business-intelligence | Standard | VRT, UTHR, FLY | none | Terrestrial PUE and cooling benchmarks (**P4**); UTHR's margin benchmark (**P6**) |
| risk | equity-research-core | Standard | SATS, SPCX | none | DA-24 contamination scoping; falsifier reachability classification (**P6**) |
| competitive | equity-research-core | Light | IRDM, SATS | none | Confirms which PIL-6 falsifiers are platform-blocked rather than source-blocked (**P6**) |
| business-model | equity-research-core | Light | SPCX | none | Segment-boundary check before the P4 restatement, so the 1.4 GW is attributed to the right segment; **the entity-boundary classification (P6)** |
| supply-chain | industry-analysis | Light | BWXT, MRCY | none | Validates the thermal and radiation supplier claims that F2/F4 rest on |

> **Coverage invariant.** Every ticker in §2 appears at least once above; every
> `Subscribed` pair in §1b generates at least one task. Verified by `tools/plan_audit.py`
> — **4/4 invariants hold.** The `recent-quarter` row names all sixteen tickers
> explicitly rather than by prose, because the auditor parses literal tickers: an
> earlier draft wrote *"all 12 universe names"* and silently generated zero tasks.

**Budget consequence, recorded rather than reconciled silently.** Sixteen universe names
across ten matrix rows expand to roughly **65 mode-tasks** after mode expansion — not the
~34 the row count suggests, and above the `max_tasks: 40` this file initially set. The
budget is raised to **70** in `thesis.md`. If it must come down, cut the `ratio-analysis`
and `business-model` rows first; **never** the `recent-quarter` row, which is the entire
delivery mechanism for P3.

## 4. Depth Tiers

| Tier | Skills | mode-set | Tickers | Output |
|:---:|------|---|--------|------|
| Deep | unit-economics, operational-kpi, secular-trends | all modes | SPCX, RKLB, **BWXT** | Full-mode validation on the three names carrying P1, P2 and P4. **Reduced from four at plan evaluation** — GOOG moved to Standard because `secular-trends` at Deep expands to **8 modes** (EV-trend, quantum/renewable, data-value, AI-trend, strategic-position, capacity-and-readiness, market-perception, exposure) and its Pillar 2 contribution is **one sourced constant**, which the `exposure` mode alone can carry |
| Standard | recent-quarter, ratio-analysis, unit-economics, risk | essentials_modes | As listed | Census, cross-checks, reachability classification |
| Light | competitive, business-model, supply-chain | essentials_modes | As listed | Scoping checks that bound the above |

**Budget note.** Evidence validation is cheaper per name than original research and
narrower in scope: this matrix yields roughly **34 tasks** across 12 names, against
001's 126 across 35. The budget is set to **40** in `thesis.md`. If it must come down,
drop the Light rows first — never the Deep rows, which carry P1, P2 and P4 — and never
the `recent-quarter` row, which is the entire delivery mechanism for P3.

## 5. Cross-Cutting Analysis

- **The validation ledger** is the cross-cutting output: every headline figure from
  001, its original grade, its validated grade, and the source that moved it — or the
  named source that would.
- **Denominator sensitivity** (P1) is reported as a band, not a point. Downstream
  theses quote `$X ± Y%`, not `$X`.
- **Macro sensitivity: low.** This thesis reads physics and filings, not prices. Its
  output is price-independent and does not decay with the rate cycle — which is
  precisely why it is the right thing to build during a NEUTRAL-bias, long-end-hostile
  regime.
- **Constitution interaction**: P4 governs the whole thesis; the v1.3.0 Data-Integrity
  Register supplies the remedy P3 applies; P10 constrains what P2's output may be used
  for.
- **Pair-trade candidates**: none. This thesis produces no positions by design.

## 6. Output Contract

- **Per-ticker (dispatcher-resumable)**: `artifacts/{ticker}/{YYYY-MM-DD}_{skill}_{mode}.md`
  — the suffix **must** be `_{skill}_{mode}.md` with the real mode slug, so
  `dispatch.resume_verdict()` can find it.
- **Cross-cutting (not resume-tracked)**: `_cross/{name}.md`.
- **Primary artifact**: `_cross/validation-ledger.md` — the table of every 001 headline
  figure with its validated grade and source. This is what 003–011 cite.
  **Schema — one row per figure:** `{figure, source_artifact, original_grade,
  validated_grade, band, citation, pillar, disposition}`. The **`citation` column is
  mandatory** per §1d, and the conversion share is
  `rows whose grade moved to DEMONSTRATED ÷ total rows` — **published with its row
  count**, so the 50% threshold in P5 can be judged against a real denominator rather
  than pre-committed (Clarification Q-5).
- **Phase 2 deliverable**: `_cross/f2-constant-sourcing.md` — each of F2's two unsourced
  constants with its citation, its uncertainty interval, and the **re-derived radiator
  mass per MW both with and without the heat-pump COP penalty**. If the band exceeds
  ±50%, F2 downgrades to a qualitative bound and **003 and 009 must be notified**.
- **Phase 4 deliverable**: `_cross/spcx-nameplate-and-boundary.md` — the PUE-inclusive
  restatement of the 1.4 GW nameplate **and** the per-series entity-boundary
  classification (Space: clean · Connectivity: clean · AI: **contaminated**).
  **This is a soft gate on 011**, whose migration claim cannot finalise without it.
- Snapshot: `snapshots/002-evidence-validation/{YYYY-MM-DD}_thesis.md`
- **Frontmatter**: per `contracts/artifact-frontmatter.yaml`, with `thesis_id:
  "002-evidence-validation"`. All five pins are mandatory: `constitution_pin: 1.4.0`,
  `assumption_pin: "2"`, `skill_pin`, `as_of`, `corpus_version`.
- **⚠️ Citations — mandatory (§1d).** Every artifact carries a `citations:` block in
  frontmatter **and** inline clickable links in the body, in the canonical form
  `[📄 {ticker} {form_type} p.{N}](https://agentii.ai/v/{ticker}/{citation_id}/{N})`.
  **The `validation-ledger.md` table carries a citation column for every row** — that is
  the artifact's purpose, and an uncited row makes it useless. Validation rules
  `citations_present` and `citation_url_wellformed` are both level `fail`.

## 7. Thesis Phases

| Phase | Tasks | Duration | Dependencies |
|:---:|------|:---:|------|
| 1 — Denominators (P1) | Filed/manifest payload masses for Electron, Falcon 9, Starship, Alpha; recompute basis A/B/C; report the ±15% band | Week 1 | Constitution v1.3.0 loaded |
| 2 — Physics inputs (P2) | Source radiator areal density; close the heat-pump COP loop; restate F2 with and without the penalty; re-derive the nuclear 24× case | Week 2 | Phase 1 |
| 3 — Defect census (P3) | `validate_calculation` across all 12 names; resolve the YSS $110.466M anomaly; complete the DA-23 census universe-wide | Week 3 | Phase 2 |
| 4 — Nameplate restatement (P4) | PUE-inclusive restatement of SPCX's 1.4 GW; re-benchmark against MSFT capex capacity | Week 4 | Phase 3 |
| 5 — Reachability (P6) | Classify all six 001 falsifiers; name the resolving source for each; propose proxy tests for the structurally unreachable | Week 5 | Phase 4 |
| 6 — Ledger (P5) | Assemble the validation ledger; compute the conversion share; publish | Week 6 | Phase 5 |
| 7 — Hand-off | Write the citable input set for 003–006; record what could not be validated | Week 7 | Phase 6 |

## Clarifications

Recorded by `agentii.specify` at creation, 2026-09-18, and updated by `agentii.clarify`
**round 3**, which was the first round whose subject was this thesis rather than the main
line (rounds 1–2 resolved to 011 — see `011/spec.md` §Clarifications). The scanner
reported **0 mechanical candidates** on all three rounds; every item below was raised
manually, since a deterministic scan cannot see intent — and it cannot see a citation
requirement, a claim that needs narrowing, or a constitution table that contradicts itself.

- **Q-1 (P1, denominator admissibility)** — Is a company-published payload capacity
  admissible as adjudication, or does it simply restate the claim? **Provisional
  answer, pending clarify:** not admissible. A company figure is the same evidence
  class as the original claim; only a government manifest, a filed document or a
  customer contract counts as independent.
- **Q-2 (P2, COP loop)** — If reaching 500 K requires a heat pump, is the honest
  output of F2 (a) the 313 m²/MW figure *with* the COP penalty folded in, (b) both
  figures reported side by side, or (c) a statement that no flight-qualified heat pump
  exists at that scale? **Provisional:** report both, per the §1c standing rule, and
  state which one the nuclear case depends on.
- **Q-3 (P3, YSS anomaly)** — If the $110.466M figure is a genuine one-off rather than
  an extraction defect, does it belong in the Data-Integrity Register at all, or is it
  a legitimate operating result that simply needs a footnote? **Open.**
- **Q-4 (all pillars, frozen-001 policy)** — When this thesis invalidates a 001 figure,
  should 001's artifact be annotated in place, or does the frozen-file policy hold
  absolutely? **Provisional:** frozen, with the correction recorded here and cross-cited
  — matching 001's own annotate-don't-rewrite policy, which corrected uncounted figures
  in place rather than deleting them.
- **Q-5 (P5, the 50% threshold)** — Is 50% the right bar? It was set as the point at
  which a register stops being majority-untestable, not from any measurement. **Flagged
  for human confirmation; if answered differently this is a PATCH to spec, not a
  MAJOR event.**

### Round 3 (2026-09-18) — the citation requirement

- [2026-09-18] **Q-6 (all pillars; instruction)**: *"在thesis 002 的validation，必须给重要
  数据和facts的引用增加 citation url agentii.ai/v/{citation_id}/{page_no}"* — every
  material figure and fact must carry a source-page citation. → **A: implemented as
  spec §1d, with a `citations` block in `contracts/artifact-frontmatter.yaml` and three
  new level-`fail` validation rules.** Applies to every `DEMONSTRATED` figure, every
  Data-Integrity Register finding, and every falsifier observation. `MODELED`
  derivations cite their inputs instead; restatements of 001 cite the 001 artifact.
  **Not a style preference**: under P4 a `DEMONSTRATED` grade *is* a claim about a
  source, so an uncited one is unverifiable by construction.

- [2026-09-18] **Q-7 (format — ⚠️ a deliberate divergence from the instruction as
  written)**: the requested form **`agentii.ai/v/{citation_id}/{page_no}` omits the
  ticker**. → **A: implemented the canonical form with the ticker, and flagged for
  override.** The portal route is `agentii.ai/v/{ticker}/{citation_id}/{N}`, redirecting
  to `api.agentii.ai/v1/view_document/{ticker}/{citation_id}?page_no=page{N}`, which
  resolves the document via `pipeline.src_documents JOIN pipeline.sec_filings` — **a join
  that cannot be performed without the ticker.** Six independent places in the plugin
  contracts (`contracts/citation-and-memory.md`, `analogue-retrieval-pattern.md`,
  `skill-methodology-template.md`, `knowledge-frameworks-template.md`, and two more)
  include the ticker; **none omits it.** Shipping the short form would have put broken
  links in every artifact. **If a ticker-less route exists that this workspace cannot
  see, this is a one-line change to §1d and the contract's URL pattern.**

- [2026-09-18] **Q-8 (scope — should this propagate?)**: the requirement was given for
  002. → **A: applied to 002 as instructed; not propagated.** The other theses' contracts
  are unchanged. **Recommended for propagation** — the main line's migration claim now
  rests on figures that would benefit from the same source verification — but that is a
  separate decision and is recorded here rather than taken unilaterally.
