# 002 — Pending Amendment Queue

Register entries and rule changes surfaced by Phase 3 that are **not yet in the
constitution**. Held here rather than amended one-at-a-time so that Phase 3 closes
with **one** version bump carrying every finding, instead of a bump per finding.

**Why hold rather than bump immediately.** Three artifacts were in flight at pin `1.5.0`
when these landed. Amending per-finding would put three or four pins in the accepted set
within a single phase, and a version string that churns faster than artifacts can be
written stops being a provenance record. One bump at Phase 3 close, carrying all of it.

**Discharge route.** Every item below is folded into **Phase 7's `_cross/validation-ledger.md`**
— the artifact whose function is exactly this census — per the 1.3.0 precedent
(reported for the gate-5 budget confirm, not separately dispatched). **No artifact is
silently re-run** (Q56, filesystem-as-checkpoint).

---

## A1 — DA-31: CROSS-HOLDING / VALUATION-CIRCULARITY IN EARNINGS

**Source: `GOOG × recent-quarter`.** **Priority: highest of the four — GOOG's own artifact
argues it is load-bearing, on two independent grounds.**

| | |
|---|---|
| **Finding** | **68.7% of Alphabet's Q2 2026 net income is the mark on its SpaceX-containing equity stake.** Decomposition: `$77,354M` non-marketable "private company" (measurement alternative) + `$21,399M` marketable (includes SpaceX) + `$278M` realised = **`$99,031M`**. That is 68.7% of net income (`77,100 / 112,193`) and 68.7% of diluted EPS (`$6.26 / $9.11`). |
| **Why it needs its own entry — ground 1** | **`validate_calculation` PASSES the contaminated fact.** `NetIncomeLoss` Q2 2026 computes = reports = `112,193`. **Every existing remedy in the register is a *verification* remedy, and verification passes.** No current entry can catch this, because there is nothing to verify *against* — the arithmetic is internally consistent and the mark is legitimately part of GAAP earnings. |
| **Why it needs its own entry — ground 2** | **PIL-3's own falsifier breaks without it.** The falsifier counts issuer-quarters carrying an unresolved defect. Unregistered, **GOOG's quarter can never be marked unresolved and `count == 0` would report clean while a 68.7% circularity is live.** A falsifier that reports clean on a contaminated quarter is worse than no falsifier. |
| **Why it matters to THIS programme specifically** | The stake **contains SpaceX**. For a thesis about the space sector, **part of a Tier-0-adjacent mega-cap's reported earnings is the mark on its position in the sector's anchor private company.** It is simultaneously a real exposure and a valuation circle: SpaceX's mark is set by private rounds, and GOOG's earnings carry it into a public multiple. |
| **⚠️ CORRECTION from `MSFT × recent-quarter` — THE MECHANISM IS NOT NECESSARILY APPRECIATION, AND ASSUMING IT IS WOULD MIS-SPECIFY THE RULE** | MSFT holds **+$4,963M = 3.71% of net income** from its OpenAI stake — **recognised as a DILUTION GAIN under HLBV as its stake FELL.** **MSFT's net income grew partly because its position SHRANK.** So the entry must **not** be defined as *"the mark on an appreciating stake."* **The class is: earnings that are a function of a stake's CARRYING VALUE rather than of operations** — and that value can move **upward on dilution**, downward on an impairment, or be measured on at least three bases (fair value, equity method, HLBV/measurement alternative) with different period-to-period behaviour. |
| **Cross-issuer status** | **GOOG positive** (68.7%). **MSFT positive for the class, negative for SpaceX** (0 hits, with a working positive control — "OpenAI" → 8 pages). **The mechanism at MSFT is dilution, not appreciation — so the two instances are not the same mechanism under one name.** |
| **Proposed rule** | An artifact quoting `net_income` or EPS for any issuer carrying a material equity stake in an unconsolidated entity must **state the stake's contribution to the reported figure AND the measurement basis (fair value / equity method / HLBV / measurement alternative)**, or record the contribution as unresolvable. **Materiality threshold and the basis vocabulary to be set at amendment time.** |
| **Open** | The 68.7% is Q2 2026. The contribution's **volatility across periods** is not yet tabulated, and a mark-to-model that swings is a different hazard from a static one. **Nor is it established whether the dilution case can repeat in the same direction — a dilution gain requires the stake to fall while value rises, which is not a stable equilibrium.** |

## A2 — DA-32: SCALE ERROR CONFINED TO ONE ACCESSION

**Source: `YSS × recent-quarter`.**

| | |
|---|---|
| **Finding** | `WeightedAverageNumberOfSharesOutstandingBasic` served as **`116,022,676,000` against `116,022,676` filed** — a **1000× error** — **in `sec9` only, while the same concept and the same period are served CORRECTLY in `sec12`.** |
| **Why it is a new class** | **Every existing register entry is a SIGN defect, a LABEL defect, or an absence.** This is a **MAGNITUDE** defect with the correct sign and the correct concept. No sign test, no bound, and no identity check fires on it. |
| **Why it is worse than a general scale bug** | The defect is **period-consistent within an accession and inconsistent across accessions.** So **a clean read in one filing does NOT validate the concept, and a dirty read does not condemn the issuer.** It is a property of the *extraction run*, not of the concept or the period — which is why it cannot be screened for by testing a concept once. |
| **n = 1** | Registered at n=1 (as DA-28 was). The open question is whether this recurs; the census requirement is to test the **same concept across accessions** wherever a share count feeds a per-share figure. |

## A3 — DA-28 GENERALISATION → CAPITAL-STRUCTURE BASIS DISCONTINUITY

**Source: `GOOG × recent-quarter`.**

| | |
|---|---|
| **Current scope** | DA-28 names *"capital-structure discontinuity around an IPO"* — a **backward-looking** event. |
| **What GOOG adds** | A **scheduled forward discontinuity DA-28 cannot see**: Alphabet's preferred converts **on or about 15 May 2029** at a **price-dependent** rate (`2.2520–2.8160` Class A / `2.2740–2.8420` Class C). It is **disclosed, dated, and conditional on a price not yet known.** |
| **Why the existing scope misses it** | DA-28's detector is a **listing-date guard** — it screens for a past structural break. **A future conditional conversion has no listing date and no break to detect**, so the guard is silent by construction. It also converts at a *range*, so even at maturity the correct denominator is conditional. |
| **Proposed rule** | Generalise DA-28 to **capital-structure BASIS discontinuity**: any issuer with a **disclosed future** share-count-changing event, or a **present multi-class structure with non-identical per-share economics**, must have the basis named. **Alphabet already supplies a present-tense instance** — see A4. |

## A4 — DA-30 INSTANCE + A NON-BENIGN DA-27

**Source: `GOOG × recent-quarter`.**

| | |
|---|---|
| **DA-30, a live instance** | **Diluted EPS is class-dependent and the platform collapses it.** Read-verified p.37: Class A **`$9.12`** vs Class C **`$9.11`** (both `$2.31` in Q2 2025). The platform serves **a single undimensioned `9.11`.** This is a `no_single_basis_collapse` violation occurring **before any artifact sees the data** — exactly the DA-30 shape registered at 1.5.0. |
| **⚠️ DA-27 IS NON-BENIGN, AND THE `source=="default"` DETECTOR MIS-FIRES AT THREE ISSUERS** | The register has treated DA-27 as a *cosmetic* label defect. **At GOOG** the source is **`fiscal_year_end_month: 2` for a December filer** (`gold_companies`) — **a STORED WRONG VALUE.** **At MSFT** it is **`fiscal_year_end_month: 7` for a June-30 filer** — also `gold_companies`. **At NVDA** likewise, **with 11 of 11 rows off by one fiscal year AND the two endpoints contradicting each other by a full year on the same date.** **Three issuers, one source field.** Consequences at GOOG: labels displaced by **~2 months *and* ~1 year**, and **FY2027 quarters synthesised that do not exist.** |
| **Correction to a standing premise** | **This falsifies my own working assumption that GOOG's fiscal year is the calendar year.** Recorded explicitly: the assumption was mine, it was untested, and it was wrong. |
| **Proposed rule** | DA-27 gains a **source discriminator**: a label defect *derived* from a null/absent issuer calendar is cosmetic; a label defect **sourced from a populated but incorrect registry field is MATERIAL**, because it is reproducible, persists across every artifact on that issuer, and cannot be corrected by a better derivation. **The register's proposed `source == "default"` screen is WRONG and must be replaced by a value-integrity check** — the source is not the default, it is a wrong stored value, so a screen keyed on the default would miss all three confirmed instances. **The census must record which kind it found**, since the two have different remedies. |

## A5 — A VALIDATOR-COMPLETENESS GAP: A NEW DISPOSITION CLASS

**Source: `VRT × recent-quarter`.** **This is the most dangerous class found so far, and it
is dangerous for a reason no other entry shares.**

| | |
|---|---|
| **Finding** | **`validate_calculation` cannot run at all on VRT's `OperatingIncomeLoss`** — 7 arcs, 3 accessions, **zero rows returned**. |
| **Why it is a NEW CELL** | The register's coverage hole is **data-availability**: the concept is absent or segment-only (MRK, BMY, WWD), so the remedy is `UNRESOLVABLE-FROM-PLATFORM`. **VRT's concept is PRESENT, fully filed, seven arcs deep, and the validator is still silent.** That is a **validator-completeness** gap. *The data exists and the check does not run.* |
| **⚠️ The consequence, which is why it outranks the others** | **A validator that NEVER RAN on VRT and one that RAN AND PASSED are the SAME ROW in every tally this programme keeps.** The absence of a verdict and a passing verdict are indistinguishable in the output. **A false negative that serialises identically to a pass cannot be found by counting passes** — so every coverage statistic the programme has reported (including "23/23 clean") is silent on this. |
| **Companion measurement** | Of 57 VRT validator rows, **39 `fail` / 3 `warn` yield THREE true defects — 92.9% false-positive**, independently reproducing the register's 93% — **and the one true finding is indistinguishable from the false ones by inspection.** |
| **Proposed rule** | `validate_calculation` output gains a **third status distinct from pass**: `NO_ROWS` / `NOT_APPLICABLE` when the instrument returns nothing for a concept that *is* filed. An artifact may not treat an empty validator result as a pass. Coverage tallies must report **three** numbers — ran-and-passed, ran-and-failed, **and never-ran** — or they are not coverage tallies. |
| **Disposition** | New class name required. Not `UNRESOLVABLE-FROM-PLATFORM` (the platform *has* the data) and not `UNRESOLVABLE-FROM-PUBLIC-SOURCES`. Proposed: **`UNVALIDATED-BY-PLATFORM`**. |
| **⚠️ REFINED at IRDM — the gap is NOT wholesale, and a binary class would misdescribe it** | IRDM returned **16 rows: 6 pass / 2 warn / 8 fail** — so it is **neither validated nor unvalidated**. **The precise finding is a linkbase ARC OMISSION**: `OperatingIncomeLoss` and `NonoperatingIncomeExpense` **never appear as a child of anything**, so **the arc that would expose the `NonoperatingIncomeExpense` strip is the absent one.** **Proposed class: `PARTIALLY-VALIDATED-BY-PLATFORM`,** scoped to the arc, not the issuer. **A binary class would have reported IRDM as validated and VRT as unvalidated when the operative fact at both is the same: the arc that matters is missing.** |

## A6 — STATEMENT-LEVEL CENSUS, AND A LINE-LEVEL BASIS DETECTOR

**Source: `VRT × recent-quarter`.**

| | |
|---|---|
| **Census widening** | DA-23 at VRT is **not on the income statement at all** — it is on the **cash-flow subtotals**. `NetCashProvidedByUsedInFinancingActivities` is **correct at `+11.9` in Q1 2026 and stripped at `−3.0` in H1 2026: same tag, same issuer, six months apart.** **The discriminator is the SIGN OF THE VALUE, not the concept and not the period.** VRT is the second instance of the 1.5.0 BWXT row and **the first where the stripped component sits on a different statement.** **So `\|x\|` stripping is not an income-statement phenomenon, and a census scoped to one statement cannot see it. The census requirement widens from component-level to STATEMENT-level.** |
| **Entity count** | DA-26's census row moves **19 → 20**; VRT was not previously listed. **VRT is the December-year-end sub-case where the misplacement is actively misleading** (the annual lands on the Q4 row). |
| **"Clean" vs "unexercised"** | All 61 of VRT's `OperatingIncomeLoss` facts are positive, so the `\|x\|` channel **has nothing to act on**. **VRT is UNEXERCISED, not CLEAN.** The census vocabulary must distinguish them, or a profitable issuer's inert sign channel will keep being counted as a passed test. |
| **DA-27's population problem** | The register explains DA-27 as *"exact for December-year-end issuers."* **That mechanism statement defines the testable population — so its n = 4 of 4 is not a sample, it is the ENTIRE testable population, and the statistic carries no information about the remainder.** Recorded as a general caution: **a defect whose mechanism is defined by the property that also defines the sample cannot be censused by that sample.** |
| **The basis detector** | A **systematically signed, exactly compensating** basis difference of **$134.9M–$183.6M annually** across 7 of 7 periods, **with the MD&A's own growth figures computed off a different basis than the income statement** (487.5/148.7 matches the note; the statement says 480.7/155.5). **`validate_calculation` is silent BY CONSTRUCTION**, because every total ties. **Proposed detector: compare LINE-LEVEL, not total-to-total**, using the §1 segment/consolidated cost-of-sales difference ($15.0M, footnoted, reconciles to 2,636.4) as the **negative control** — a difference that is legitimate and disclosed. |
| **DA-24's shape inverted** | Refuted **on both signs**: goodwill is positive on all three acquisitions, and the only acquisition item above the operating line is PurgeRite contingent consideration at a **$62.0M CHARGE**. **DA-24 assumed a gain; at VRT the same line item is a loss.** The entry's definition should name both directions. |

## A7 — THE REGISTER'S OWN INDEPENDENCE PROOF USES A TEST THE REGISTER FORBIDS

**Source: found while scoping `SATS × recent-quarter`; not an artifact finding — a
self-contradiction read directly off the constitution.**

| | |
|---|---|
| **What DA-24 says** | *"**Independence — measured**: SATS exhibits **DA-24 without DA-23** (its EPS × shares reconciles to 0.3%). **This is the cleanest proof the two diagnoses are distinct** and must remain separate register entries, not merged."* |
| **What DA-23 says** | *"~~`EPS × shares ≈ net income`~~ — **INADMISSIBLE as a sign test.** Confirmed unreliable: it **passes on both sides of a flip** at RKLB, FLY *and* VOYG. **Its use is a defect, not a shortcut.**"* |
| **The contradiction** | **DA-24's "cleanest proof" of independence is exactly the forbidden use.** DA-24 infers *"DA-23 is absent at SATS"* from a passing `EPS × shares` check — which is the inference DA-23's row rules inadmissible, on the ground that the test **passes whether or not a flip is present**. |
| **Why it has to be fixed, not just noted** | **Independence is the entry's load-bearing claim.** DA-24's justification for existing separately from DA-23 is this measurement. If the measurement is inadmissible, then **the register has no admissible evidence that the two defects are distinct** — and a register that merges them would mis-remedy every SATS-class issuer. **This is not a stale citation; it is the entry's foundation.** |
| **What would restore it** | An **admissible** test: the component identity (`gross profit − opex = operating_income`) in-line, per period. If SATS's component identity closes to its filed operating income while a spectrum-sale gain sits inside the operating stack, **the independence claim is restored on a sound basis.** If it does not close, **the claim fails and DA-24's status must be restated.** |
| **Status** | **✅ RESOLVED by `SATS × recent-quarter` — THE INDEPENDENCE CLAIM FAILS, ON TWO INDEPENDENT GROUNDS.** **(1) It rests on a test the register forbids** — `EPS × shares` is INADMISSIBLE as a sign test, so DA-24's foundation was a measurement the register had already declared unusable. **(2) Even at face value it is arithmetically BLIND**: the residual `\|EPS\|×shares − \|NI\|` is **invariant under a global flip**, because both operands carry the same strip — so the check returns its 0.3% (measured 0.35%) **whether or not a strip is present.** **And the claim is substantively false: DA-23 IS present at SATS in the same periods** (12/12 filed-negative subtotals stripped, 8/8 filed-positive clean, zero exceptions). **Independence is now UNSUPPORTED rather than disproven** — the two defects co-occur, consistent with either a shared cause or a coincidence, and **no admissible measurement currently separates them.** DA-24's entry has been rewritten in the constitution accordingly, and its *definition* widened to cover a **charge**, since the defining instance turned out to be an **inverted impairment, not a sale.** |
| **Note on the class** | This is the third instance in this thesis of the same failure shape — **an inference drawn from a tool that cannot support it** (001's back-solved clearance; PIL-2's unrecordable source class; now DA-24's inadmissible independence proof). **All three close cleanly and none of them ran.** DA-29 is the register entry that names the family; this adds the case where the defective check is *inside the register itself*, not inside an artifact. |

## A8 — DA-23'S CALCULATION-WEIGHT DISCRIMINATOR

**Source: `MSFT × recent-quarter`.** **Without this rule, the obvious cash-flow detector is
wrong in both directions.**

| | |
|---|---|
| **The rule** | **A concept entering its calculation parent at WEIGHT −1 carries a positive magnitude LEGITIMATELY. At WEIGHT +1, with a parenthesised filed cell, it is STRIPPED.** |
| **Verification** | **38 MSFT facts, ZERO miscalls.** It is what separates `PaymentsToAcquirePropertyPlantAndEquipment` (**+115,948, CORRECT**) from `NetCashProvidedByUsedInInvestingActivities` (**+139,500, STRIPPED**) — **two cash outflows in the same subtree, opposite verdicts.** |
| **Why it must be registered rather than left as an artifact finding** | The naive reading — *"this is a cash-flow concept, so a positive value is a strip"* — **gets `PaymentsToAcquirePropertyPlantAndEquipment` wrong.** The register cannot state a cash-flow rule without the weight qualifier, because the weight is what makes the same sign correct or corrupt. |
| **Operational consequence** | **A DA-23 test on any concept requires reading the calculation linkbase for that concept's arc weight.** A sign test without the weight is not a test. |

## A9 — THE SEGMENT-TOTAL SUBSTITUTION: THE CONDITION THAT MAKES IT SILENT

**Source: `NVDA × recent-quarter`, refining the mechanism first identified at `GOOG`.**

| | |
|---|---|
| **What was established at GOOG** | A **segment member served as the consolidated value** — three exact arithmetic matches (Q2 2025 OI 2,826 = Google Cloud's OI; FY2024 OI 4,444 = \|Other Bets loss\|; Q1 2026 OI 2,100 = \|Other Bets loss\|), **and the member differs between periods of the same filing.** |
| **What NVDA adds — the CONDITION** | `Revenues` is served on four bases (`{}` / geography / market platform / segment) and **ALL FOUR SUM TO 81,615 — so substitution is SILENT on revenue.** But **unallocated items are not allocated**, so for **operating income** the segment total **EXCEEDS** the consolidated figure. **Silent where nothing is unallocated; an OVERSTATEMENT where something is.** |
| **Why this is the sharpest form** | It explains **why the defect was invisible on revenue and visible on operating income** — not luck, but arithmetic. It also gives a **predictive screen**: the substitution matters exactly where the concept has unallocated items, and is undetectable where it does not. |
| **The airtight instance, both facts existing simultaneously** | `view=standard` returns `OperatingIncomeLoss` **53,536,000,000** with `dimensions: {}`, `is_primary: true`; `view=detailed` returns **56,276,000,000** under `ConsolidationItemsAxis: OperatingSegmentsMember` — **same concept, same period, same unit.** The served `reported` was the segment figure: **68.95% vs a true 65.60% — +3.36 pts / +$2,740M (+5.12%).** |
| **⚠️ The corruption can enter via a CHILD** | **`GrossProfit` itself has ZERO dimensional facts**, yet its `computed` was **−19,168** = exactly `1,290 − 20,458`, where 1,290,000,000 is a served `nvda:OtherCountriesMember` revenue fact. **It cannot be found by inspecting the parent.** |
| **⚠️ `is_primary: true` is NOT a basis guard** | Two facts were served with `is_primary: true` for **one cell**. The flag does not mean "the consolidated one." |
| **Proposed rule** | Any artifact reading a consolidated subtotal must **state which view produced it** (`standard` vs `detailed` vs segment), and **may not treat `is_primary: true` as evidence of the consolidated basis.** |

## A10 — `fiscal_period=FY` IS NOT A DURATION FILTER (and is a plausible cause of DA-26/27)

**Source: `NVDA × recent-quarter`.**

| | |
|---|---|
| **Finding** | `fiscal_period=FY` returned **six durations in one bucket, none labelled.** |
| **Why it matters** | **A filter that groups by label rather than by duration silently mixes periods.** This is a **plausible upstream cause of DA-26 and DA-27** — both are period-attribution defects, and both would follow mechanically if the period dimension is carried as a *label* rather than as a *duration*. |
| **Consequence for every artifact** | **A period-scoped query must be validated against a known duration, not trusted from its label.** Related: **the compound `fiscal_year`+`fiscal_period` filter returns ZERO where either alone returns the fact (MSFT) — so silence from a compound filter is not absence.** |

## A11 — TWO HOUSEKEEPING DEFECTS WITH OPERATIONAL CONSEQUENCES

| | |
|---|---|
| **`data_freshness` reports the future** | Returned **`2027-04-12`** — seven months ahead of `as_of = 2026-09-18` — on two surfaces (NVDA). **It is unusable for judging corpus currency**, and a freshness check built on it would pass a stale corpus. |
| **The description-field asymmetry runs BOTH ways** | The workspace finding recorded that `read_source_outline`'s LLM description can be quoted as if it were the filing. **The reciprocal is equally dangerous and was not recorded: at NVDA, `read_source_pages` returned `description: null` for pages where `search_keyword_in_source` returned rich descriptions for the same ids.** So **"I read the page and it had no description" is NOT evidence the description does not exist** — and a `total_count: 0` from keyword search is **not evidence the filing lacks the word** ("space" → 0 hits while "Revenue" → 23). **Absence must be established by reading pages, and the method must be stated.** |

## A12 — A DETECTOR RUN ON ONE SIDE OF A COMPARISON CANNOT DETECT A COMPARISON ERROR

**Source: `MRCY × recent-quarter`.** **This is the single most transferable method rule the
phase produced, and it invalidated the register's own showcase example.**

| | |
|---|---|
| **The rule** | **A detector run only on the subject of a comparison cannot detect a comparison error.** |
| **What it caught** | The register held MRCY up as the reason the component identity is *"mandatory rather than a spot-check."* **The identity WAS run — on the period 001 was REPORTING, and not on the period it was COMPARING AGAINST.** The reported period is one of the two filed-positive ones, **so it passed by construction.** |
| **The verdict that follows** | **MRCY is the most contaminated issuer in the phase**: 11 of 13 filed periods are losses served as identical positive magnitudes, and **the only 2 correct values are the only 2 filed-positive periods.** 001's `−98.6%` is reproducible **only from the stripped comparator** — on filed signs the change is **+19,907 favourable and the percent is UNDEFINED, because it crosses zero.** |
| **Proposed rule** | **Wherever a figure is presented against a comparator, the detector must run on BOTH sides, and the artifact must state that it did.** A one-sided detector report is not evidence about a comparison. |

## A13 — THE NOT-TESTABLE TAXONOMY IS NOW **SEVEN** KINDS, NOT TWO

> **⚠️ Correction to this entry's own heading.** It first read *"now FOUR KINDS"* while its
> table already enumerated **six**, and kinds 5 and 6 were added after the heading was
> written. **`IRDM × competitive` caught the mismatch and correctly noted that the table is
> operative.** The count is now **seven** (kind 7 was added at `VRT × ratio-analysis`).
> *Recorded rather than silently fixed: a heading that contradicts its own table is the
> same defect class as everything else in this queue, and it was introduced here.*

**Source: accumulated across Phases 3–6.** The register previously carried two dispositions.
**They have different remedies and must not be merged — and five more were added.**

| # | Kind | Instance | Remedy |
|---|---|---|---|
| 1 | **Ingestion absence** | `fiscal_period=Q4`/`Q3` return 0 facts at YSS; a 10-K with `processing_status: pending` | Pipeline completion |
| 2 | **Genuine absence from the source** | SATS DA-28: no listing event in any served period. Also MRCY's standalone filed Q4 — **MRCY files no Q4 10-Q, so "every period" means 13 filed, not 16** | Nothing to fetch; scope the claim |
| 3 | **Validator-completeness** *(new, A5)* | VRT: concept present, fully filed, 7 arcs deep — validator returns **zero rows** | Instrument fix |
| 4 | **Mechanism-population identity** *(new, SATS)* | DA-27 at a December-year-end issuer: **the sample is defined by the mechanism's own property**, so it carries **no information about the remainder** (SATS, UTHR, VRT, MRCY all excluded on this ground) | Remove from the denominator; do not report as a clean result |
| 5 | **Ingestion absence of a DATUM CLASS** *(new, IRDM)* | DA-25: subscriber counts are **MD&A prose, never XBRL-tagged**, so the query returns zero **BY CONSTRUCTION** — not because a period returned zero | Nothing to fetch; the datum class is not in the tagged corpus |
| 6 | **Coverage window** *(new, IRDM)* | DA-28: **SEC coverage opens 2022-02-17**; the IPO falls outside it | Widen the window or exclude from the denominator |
| **⚠️ And a NEGATIVE CONTROL that must travel with it** | At MRCY, `processing_status: pending` appeared on all 36 filings **yet 10 of 10 pages served full cell-level text**; at IRDM **all 9 accessions read `pending` including ones that demonstrably serve facts** (sec191 served 40 pages and ran the validator). **`processing_status` is NON-DISCRIMINATING and must NOT be used as an ingestion-absence marker.** **The YSS inference does not generalise**, and a `pending` flag alone is not evidence of missing data. | | |

## A17 — THE WEIGHT DISCRIMINATOR NEEDS A BOUNDARY: DIRECTIONALITY

**Source: `IRDM × recent-quarter`, refining A8.** **A8 as stated would have produced a false clearance, and IRDM is where that became visible.**

| | |
|---|---|
| **What replicated** | **Perfectly.** Capex `+51,791` at **w = −1** is **CORRECT** while investing `+51,791` at **w = +1** is **STRIPPED** — **the same number, the same period, the same statement, the same parentheses** — reproduced again at H1 2025. |
| **⚠️ What broke** | **Weight −1 carries THREE concepts with THREE different verdicts**: capex **CORRECT**; **FY2023 tax STRIPPED**; and equity-method income entering **two parents at opposite weights — one served number correct for one parent and wrong for the other.** **So weight alone does not determine the verdict.** |
| **The completing test** | **DIRECTIONALITY.** A **UNIDIRECTIONAL** concept absorbs the sign into the weight, so a sign test on it is **VACUOUS**. A **BIDIRECTIONAL** concept carries sign as **substance**, so the test has power. |
| **The scoping requirement that follows** | **DA-23 is detectable ONLY on bidirectional concepts. Any clearance must be SCOPED to them AND must EXHIBIT A NEGATIVE-FILED INSTANCE — otherwise it is `UNEXERCISED`, not clean.** |
| **Also — the two instrumentation columns must be tested INDEPENDENTLY per issuer** | At IRDM, investing shows `computed` = `−51,791,000` (**the filed sign**) while `reported` = `+51,791,000` (**stripped**) — **the REVERSE of MSFT**, where `computed` was the wrong column. **"Trust `computed`" does not generalise.** |
| **The sharpest per-fact demonstration in the thesis** | `AccumulatedOtherComprehensiveIncomeLossNetOfTax` is **STRIPPED** as `(4,681) → +4,681,000` **while `406` in the ADJACENT COLUMN of the SAME ROW is served CORRECTLY as `+406,000`.** No concept- or row-level transformation can produce that — **the strip is per-FACT, at the finest granularity the filing offers.** |
| **Scope of the defect** | **12 concept-series confirmed stripped across FOUR statements** — income statement, cash flow, **balance sheet** (`RetainedEarningsAccumulatedDeficit` 20/20 positive), and per-share. Fingerprints exact: `3,020 = 2 × 1,510`; `1,720 = 2 × 860`; `197,484 = 2 × (51,791 + 46,951)`; `783,924 = 2 × (387,281 + 4,681)`. |

## A14 — `validate_calculation` CAN RETURN `pass` ON A WRONG-SIGNED VALUE

**Source: `SATS × recent-quarter`.** **Stronger than A5's zero-row gap — not a validator that failed to run, but one that ran, returned pass, and could not have returned anything else.**

| | |
|---|---|
| **Instance** | `ProfitLoss` Q3 2025 computed = reported = **`12,781,348,000`**, `diff 0`, **`status: pass`** — while the filing prints **`(12,781,348)`**. |
| **Why** | **The `reported` column SHARES THE STRIPPED STORE.** So the validator compares a stripped value against a stripped value and finds agreement. **It is CONSTITUTIVELY INCAPABLE of detecting the strip it is running on.** |
| **Corollary already observed** | At MRCY, `status` read **`pass` on a row where BOTH SIDES were stripped.** |
| **Proposed rule** | **A `validate_calculation` pass is not evidence about sign.** Any artifact relying on it for a sign question must say so explicitly and supply an independent test. **Three distinct failure modes now exist for one tool: never ran (A5), ran and passed a wrong-signed value (A14), and ran with 93% false positives when it failed (A5).** |

## A15 — THE STRIP IS LOCALISED TO NUMERIC FACT EXTRACTION

**Source: `SATS × recent-quarter`.**

| | |
|---|---|
| **Finding** | **The table-TEXT facts retain correct signs while the NUMERIC facts are stripped.** |
| **Why it matters** | It **localises the defect to one pipeline stage**, which is what makes a targeted fix possible — and it explains the whole class's persistence: **the correct value is often already present in the same document, in prose, where no numeric query will find it.** |
| **Corollary — the extension-tag gap** | The SATS 2025 charge is a **filer extension** (`sats:AssetImpairmentChargesAndOther`), and **`us-gaap:AssetImpairmentCharges` returns 6 facts, none from 2025.** **Any `us-gaap:`-keyed census SILENTLY MISSES EXTENSION TAGS.** *A zero from a `us-gaap` query is evidence about the TAG, not about the filing.* |

## A16 — DETECTOR AVAILABILITY AND DETECTOR POWER ARE SEPARATE QUESTIONS

**Source: `UTHR × recent-quarter`.**

| | |
|---|---|
| **Finding** | **The registered gross-profit bound found 0 of UTHR's 11 strips at an 87.30% margin.** UTHR sits in the cell where the detector **is available** (no gross-profit face line, but `OperatingIncomeLoss` is a filed first-class subtotal) and its **power is nil**. |
| **The replacement detector** | **Served-component overshoot = `2 × \|every negative component\|`, six of six exact** (Q2 2026 692.2 vs 683.8 = 8.4; FY2025 2,826.3 vs 2,798.3 = 28.0). |
| **Proposed rule** | **A detector must be reported with its power, not only its availability** — the register already states this for the gross-profit bound's margin-conditioning, and UTHR shows the same conflation arising one level up. **Registering a detector as "available" at an issuer where it cannot fire is the same error as reporting an inert sign test as a clean result.** |

## A18 — A RECAST DISCLOSED ONLY BY ITS ARITHMETIC SIGNATURE

**Source: `SPCX × business-model`.** **No filing sentence discloses it; the numbers are the only evidence.**

| | |
|---|---|
| **Finding** | SPCX has an **AI segment whose comparatives predate it by 7 and 11 months** — and **no recast, reclassification or restatement sentence exists anywhere in the filing.** |
| **The mechanical legibility** | **48.7% of Q2 revenue growth came from a segment SPCX did not own a year earlier** (43.8% H1). Consolidated **Q2 +91.9% → +57.6% ex-AI**, a **59.5% relative** difference. **The three segment contributions tie exactly to the consolidated increase**, which is what makes the change detectable without any disclosure. |
| **Why it needs a register entry** | **Common-control and step-acquisition boundaries can change a consolidated growth rate by more than half without a single sentence of disclosure.** The existing entries cover *labels* (DA-26/27) and *values* (DA-23/24) — **neither covers a boundary that moved and was never described.** |
| **Proposed rule** | **Before quoting any consolidated growth rate, tie the segment contributions to the consolidated change.** If they do not tie, or if a segment carries comparatives it did not have, **the growth rate is an entity-boundary artefact** and must be quoted both ways. **The detector is mechanical and needs no filing text.** |

## A19 — THE RATIO LAYER: SILENT COMPONENT-DROP, INERT SLOTS, SUBSTITUTED DENOMINATORS

**Source: `SPCX × ratio-analysis` and `VRT × ratio-analysis`.** **Two issuers, independently, and the defects replicate.**

| Defect | Evidence |
|---|---|
| **⚠️ The ratio-layer identity theorem** | **`net_margin × asset_turnover = roa` closes 7/10 exactly and 9/10 within 2e-4 — AND THE FY2024 Q4 BACK-SOLVE PASSES IT** (rows implying **8,700** against a filed **450,256 — a 51.75× collapse**). **A ratio-layer identity is a CONSISTENCY check, not a correctness check: it certifies that the ratios agree with EACH OTHER, never that any of them is the quantity it names.** *All three terms are corrupted together, so they cohere.* **This is the DA-29 family arriving one level up — and it is why a ratio block can be internally flawless and wholly wrong.** |
| **Silent component-drop — CONFIRMED AT THREE ISSUERS** | **`quick_ratio ≡ cash_ratio` EXACTLY at SPCX, VRT AND GOOG** — byte-identical in **8 of 8** VRT periods; identical to 4 dp at SPCX (**the slot is inert**); at GOOG `0.4433 = 55,911/126,111` **with AR 69,175 silently dropped** against a skill quick ratio of **0.9919 — a 54.86 pp gap.** **Cause: the receivables input is absent** (`receivables_turnover: null`, `dso: null` in **10 of 10**). VRT's correct quick ratio is `0.9058` against a served `0.3880` — **2.33× understated**. **⚠️ The failure is SILENT: it returns a PLAUSIBLE DIFFERENT RATIO, not null.** |
| **Substituted denominator — CONFIRMED AT THREE ISSUERS** | **`debt_to_equity` = TOTAL LIABILITIES ÷ equity** — **VRT (2.3422, a 3.79× overstatement, confirmed at three periods)**, **SPCX (both terms substituted, 26.6% high)**, **GOOG (0.4395 = 281,503/640,480 against the skill's long-term-debt 0.1533 — ≈+28.5 pp)**. Also SPCX `roe` uses **APIC** (167,344) instead of equity (127,224) — **31.5% low.** **Three issuers, two causes, ONE ENGINE.** |
| **Segment substitution at the ratio layer** | SPCX `operating_margin` = **AI segment 6M loss ÷ consolidated revenue** — it **inverts a filed `−16.68%` into `+29.79%, a 46.47 pp swing.** |
| **Unnamed period basis** | **Four VRT ratios carry a SIX-MONTH basis on a quarterly-labelled row** (`inventory_turnover` 1.81×, `operating_cf_ratio` 1.70×, `roa`/`roe` 1.78×), the last two also **skipping the averaging the skill's own methodology mandates.** |
| **Label/computation mismatch** | **14 of 20 VRT growth figures carry a five-year label on a three-year computation.** |
| **Proposed kind 7 of not-testable: DETECTOR GAP AT A COMPUTABLE DATUM** | VRT `gross_margin` is **null in 10 of 10** periods **while the issuer publishes it** (p.28 prints `Gross profit \| 1,234.9 \| 896.6 \| 338.3 \| 37.7`, and the arithmetic closes exactly). **The datum is filed, published and reconstructible; the platform returns null with no fallback notice** — and **the skill's own fallback contract (widen the range and retry; try alternative concepts) was neither executed nor reported.** **Remedy is the INSTRUMENT — distinct from pipeline (kind 1) and from source (kind 2).** |
| **⚠️ And the register's own component identity is VACUOUS at VRT** | `us-gaap:GrossProfit` and `us-gaap:OperatingExpenses` each return **0 facts** and no gross-profit line is filed, so the identity reduces to `(rev − COGS) − ((rev − COGS) − OP) = OP`. **It closes 5/5 by construction.** Replaced by a **seven-term FILED identity** closing 5/5 EXACT, plus a third exact identity at segment level. **A detector that closes by construction is the DA-29 family appearing inside a skill's own methodology.** |

## A20 — A DETECTOR THAT CLEARS BOTH DIRECTIONS (record the one that works)

**Source: `VRT × ratio-analysis`.** **The first detector in this thesis to pass a positive case AND a negative control.**

| | |
|---|---|
| **The negative control (must NOT fire)** | Segment cost of sales Δ**`$15.0M`** — **footnoted** and reconciles to 637.9. It produces **+45.8 bps**, roughly 90× the rounding tolerance, **and correctly does NOT fire — because it is footnoted and closing.** |
| **The positive case (must fire)** | Note 4 revenue disaggregation vs the statement: Δ**±40.3, exactly compensating so every total ties**, **no reconciling footnote**. **It fires on a MIX ratio (−123.1 bps)** — not merely on a total. |
| **Why it matters to record a success** | Almost every entry in this queue is a defect. **This one is the reason to trust the others**: a rule that fires on everything is as useless as one that fires on nothing, and **this is the only detector so far demonstrated to distinguish a legitimate basis difference from an illegitimate one.** |
| **The upgrade** | The detector is **documented, not merely inferred**: VRT's MD&A prints product +$487.5 / services +$148.7, which match **Note 4** and **not** the statement (480.7 / 155.5). **The issuer computes its growth narrative on one basis and its gross-profit line on another, on the same page.** |

## A21 — SECOND-ORDER CONTAMINATION: REMOVING THE ONE-OFF IS NOT SUFFICIENT

**Source: `SATS × risk`.** **The most actionable finding of Phase 5, because it invalidates the standard remedy.**

| | |
|---|---|
| **Finding** | The Q1 2026 vs Q1 2025 bridge closes at **`+480,979`**, of which **D&A relief `+321,732` and the impairment credit `+66,159` together are `+387,891 = 80.6% of the ENTIRE year-over-year improvement`.** |
| **⚠️ Why the usual fix fails** | **The D&A relief is PERMANENT** — the Other segment's D&A fell **303,929 → 11,305** — **and accretion is disclosed as continuing prospectively.** **So an add-back-only normalisation STILL FLATTERS FY2026.** **Removing the one-off is the standard remedy and it is not sufficient here**, because a permanent step-change in the cost base rides along with the one-off that caused it. |
| **Proposed rule** | **A normalisation must state, for each item removed, whether its EFFECT is one-off or persistent.** Where a one-off also resets a recurring cost, **removing only the one-off leaves a residual that looks like improved operations.** The detector: **after de-contaminating, compare the de-contaminated growth rate against the bridge's own components — if the improvement is concentrated in items whose effect persists, the normalised figure is still wrong and in the same direction as the raw one.** |
| **Companion scoping correction (this phase's own error)** | Only **`5,784,779` of the `17,632,011` (32.8%)** struck regulatory authorisations; the other **`11,847,232`** hit prepaids / PP&E / ROU / exit costs. **A scoping figure recorded earlier in this same phase as `12,297,538` is WRONG.** *Recorded because the correction is ours, not an agent's.* |

## A22 — REACHABLE-BUT-NOT-RECORDABLE: THE THIRD SITUATION

**Source: `SATS × risk`, confirming and naming what `_cross/f2-constant-sourcing` had flagged.**

| | |
|---|---|
| **The three situations** | **(1)** `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — no public source carries it. **(2)** `UNRESOLVABLE-FROM-PLATFORM` — public and reachable in principle, not by this toolchain. **(3) REACHABLE-BUT-NOT-RECORDABLE** — **the data is reachable AND the platform can read it, but a passing result CANNOT BE RECORDED**, because the falsifier's named source class is incompatible with the level-`fail` citation contract (which admits only `agentii.ai` URLs). |
| **Why it must be separate** | Situations (1) and (2) have remedies — monitor, or extend platform reach. **Situation (3) has neither: the test can be run and its result has nowhere to go.** The artifact would have to fail its own citation contract in order to report a pass. |
| **Confirmed instance** | **PIL-2's falsifier** names `source=peer_reviewed_literature_or_flown_hardware_disclosure`. **A passing evaluation is UNRECORDABLE.** Resolving source identified: the next **Item 1A refresh = FY2026 10-K**, with the Q1 2026 leg closed by incorporation by reference. |
| **Contract consequence** | **The citation contract needs a third `located_via`-adjacent allowance** — a declared non-platform source class, recorded with its resolver, so that a falsifier can pass *and be recorded as passing*. **Until then, every such falsifier is reported as unresolvable whether or not it is satisfied** — a systematic bias toward false negatives. |

## A23 — PIL-7's OUTPUT: THE REACHABILITY CENSUS AND ITS PROXIES

**Source: `SATS × risk`. Recorded because it is the shape PIL-7 was specified to produce, and downstream theses need it.**

| Falsifier | Class | Kind | Named resolving source |
|---|---|---|---|
| PIL-1 valuation circularity | **EVALUABLE** | — | Form S-1-equivalent disclosures (`sec85` p.37; `sec121` pp.16–17) |
| PIL-2 immaterial-to-counterparty | **REACHABLE-BUT-NOT-RECORDABLE** *(A22)* | recordability | next Item 1A refresh = FY2026 10-K |
| PIL-3 19-issuer risk-factor test | **EVALUABLE — blocked by EFFORT, not reachability** | — | each issuer's Item 1A, on-platform |
| PIL-4 listing event | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | **2** genuine absence | Form S-1 / 8-K; **proxy: the disclosed preconditions** |
| PIL-5 terrestrial denominator | `UNRESOLVABLE-FROM-PLATFORM` | **5** datum class | the licensed colocation dataset; **proxy: issuer capex** |
| PIL-6 FCC IBFS / ITU | `UNRESOLVABLE-FROM-PLATFORM` | **5** regulatory registry | FCC IBFS / ITU filings; **proxy: licence table + impairment by asset class** |

**Two structurally unreachable, one platform-blocked, one unrecordable — and every one carries an EVALUABLE PROXY TEST.** *That is the deliverable: not a verdict on reachability, but a means of testing anyway.*

## A24 — THE `2 ×` FORMULA HAS TWO REGIMES, AND THE SECOND MEANS THE OPPOSITE OF THE FIRST

**Source: `RKLB × ratio-analysis`.** **The register states the formula; it does not state that the formula is ambiguous. Applied without the regime, it attributes the error to the wrong line.**

| | |
|---|---|
| **Regime (a) — parent SOUND** | `diff = 2 × Σ\|stripped child\|`. **This is the register's rule, and it is only the first regime.** |
| **Regime (b) — parent MIRRORED** | `diff = 2 × Σ\|CORRECTLY-SIGNED child\|`. **The formula is numerically identical; the meaning is inverted.** |
| **⚠️ The worked case that exposes it** | RKLB Q2 2026 `NetIncomeLoss`: **`diff = 10,654 = 2 × 5,327`** invites *"the tax was stripped."* **IT WAS NOT — the served tax `+5,327` is CORRECT (an expense). The failure is the PRETAX child (error `87,862 = 2 × 43,931`). The diff equals `2 × tax` only because `reported` is the MIRROR.** |
| **Proposed rule** | **State the regime before applying the formula.** The disambiguator: compare `computed` against the filed value for the PARENT — if the parent itself is mirrored, regime (b) applies and **the residual localises to the correctly-signed child, not the stripped one.** |
| **Companion: `computed` vs `reported` has NO default winner** | **Four rows, four different resolutions, ONE filing** — `OperatingIncomeLoss` → `computed` right; `NonoperatingIncomeExpense` → `reported` right; `GrossProfit` → `reported` right; **`NetIncomeLoss` → NEITHER.** **"Trust `computed`" and "trust `reported`" are both wrong as general rules.** |

## A25 — THE LINKBASE LABEL FIELD IS A FABRICATION VECTOR

**Source: `RKLB × ratio-analysis`.** **A new vector, and it was not in the register's model of the citation hazard at all.**

| | |
|---|---|
| **Finding** | **The linkbase `LABEL` field is twelve years stale AND FIGURE-BEARING.** A label reads *"Preferred Stock; 5,000 shares authorized … at December 31, 2014 or 2013"* against a filed **100,000,000 authorized / 40,951,250 issued.** A PP&E label reads *"net of $32,412 and $28,145"* against filed **(90,865)/(65,585)**. |
| **Why it is the same class as the LLM-description hazard** | **A figure taken from a label is as fabricated as one taken from an LLM description** — it is fluent, figure-dense, in the register of the filing, and **not the filing's current numbers.** The register had generalised the hazard to *descriptions*; **labels are a second instance of the same failure mode in the structured layer**, where it was assumed safe because it is machine-generated metadata rather than generated prose. |
| **Proposed rule** | **A figure may not be sourced from a `LABEL`.** Labels are disclosure *names*, not values; **a label carrying numbers is a historical caption and must be read against the filed cells before use**, exactly as a description field must be. |

## A26 — THE COMPLETION OF A8/A17, AND A THIRD SUBSTITUTION CASE

**Sources: `RKLB × ratio-analysis` completing `MSFT` (A8), `NVDA` (A9) and `IRDM` (A17).**

| | |
|---|---|
| **A8/A17 completed** | **The weight rule LICENSES at w = −1 and CANNOT CERTIFY.** It is **powerless on bidirectional concepts** — proven by **ONE concept at RKLB in ADJACENT PERIODS**: `IncomeTaxExpenseBenefit` is **correct at Q2 2026** (an expense) and **stripped at FY2025** (a benefit), **at the same arc weight.** **And A16's overshoot detector is a COROLLARY of A8, with ZERO POWER in a pure-w−1 subtree.** |
| **A9 falsified as a complete statement** | NVDA gave the dichotomy *silent where nothing is unallocated / overstatement where something is*. **A THIRD CASE EXISTS: SINGLE-MEMBER SUBSTITUTION — understating by `69.4%` (validator `14,220` vs consolidated `46,388`) WITH NOTHING UNALLOCATED**, because the store holds **no undimensioned `GrossProfit` at all** for that comparative. **So the substitution can understate as well as overstate, and can bite where the dichotomy says it is silent.** |
| **A new instrument signature** | **SELF-REFERENCE:** `computed = 2 × reported`, `diff = reported` (RKLB lease-payment rows 49,220/24,610 and 252,818/126,409). |
| **And the largest error at RKLB was not a sign error** | **FY2025's served balance-sheet rows read the PRIOR-YEAR COMPARATIVE COLUMN**: current ratio `2.071` vs filed `4.083` (**−49.3%**), quick **−53.2%**, working capital **−65.8%** — **at platform severity `warn`.** |

## A27 — THE REGISTER'S COMPONENT IDENTITY IS FALSE AS WRITTEN AT UTHR

**Source: `UTHR × unit-economics`.** **A correction to the register's own detector, found by running it on a comparison.**

| | |
|---|---|
| **Finding** | The registered identity `gross profit − opex = operating_income` **is false at UTHR by exactly cost of sales, six of six periods.** |
| **Why** | **`CostsAndExpenses` INCLUDES cost of sales.** So the correct form is `gross profit − (opex NET of cost of sales)`, and **the register's form double-counts cost of sales.** |
| **⚠️ How it was hidden** | **001's AMGN check silently used opex NET of cost of sales** — the correct form — **while the register states the gross form. TWO ISSUERS IN ONE COMPARISON, OPPOSITE SIDES OF AN UNSTATED TERM.** That is a DA-30-class basis collapse **occurring inside the comparison itself.** |
| **Why the comparison suppressed it** | **The subtotal sign axis is `UNEXERCISED` on BOTH sides** (61 UTHR and 61 AMGN facts, all positive) — **so neither issuer could expose the discrepancy, and the identity appeared to close.** |
| **Proposed rule** | **The identity must name whether `opex` is inclusive or exclusive of cost of sales, per issuer.** The register states one form as though it were universal; **it is not, and running it on the wrong side produces a false pass that a sign test cannot catch.** |

## A28 — A CONTAMINANT INSIDE A FILED SUBTOTAL IS ABSORBED BY IT

**Source: `SPCX × risk`, superseding `SPCX × ratio-analysis`'s `NOT EVIDENT` verdict.**

| | |
|---|---|
| **Finding** | DA-24 is **PRESENT** at SPCX, proven from the linkbase (`RestructuringCharges` and `ImpairmentOfLongLivedAssetsHeldForUse` are arc children of `CostsAndExpenses` at **weight +1**). Item as share of the operating result: **1.4 / 0.4 / 20.1 / 23.6%**; **193 of the 827 Q2 improvement (23.3%) is DA-24.** |
| **⚠️ Why the earlier verdict was wrong** | The ratio artifact read DA-24 as *"NOT EVIDENT"* from a `total costs and expenses` census that **closed with zero residual** — **and a zero residual is EXACTLY what a contaminant inside the subtotal produces.** |
| **Proposed rule** | **A census that brackets a subtotal cannot detect a contaminant INSIDE the subtotal. It proves PRESENCE, never ABSENCE.** A `NOT EVIDENT` verdict is only available from a test that **decomposes the subtotal**, i.e. the calculation linkbase's arc children with their weights. **Otherwise the correct verdict is `UNTESTED AT THIS LEVEL`.** |
| **Generalisation** | This is the DA-29 family once more: a check that closes cleanly **because it is measuring the wrong level.** |

## A29 — CORRECTIONS DO NOT PROPAGATE, AND `upstream_stale` DOES NOT MAKE THEM

**Source: `UTHR × unit-economics`.** **The most consequential process finding of the phase, because it is about the programme's own machinery.**

| | |
|---|---|
| **Finding** | **A corrected figure has now been derived THREE TIMES AND ABSORBED ZERO TIMES** — 001's UTHR artifact (1239) → the recent-quarter artifact (1500) → the unit-economics artifact. **001's L57 STILL READS `72.0`.** |
| **Why** | **The register has no rule requiring a downstream correction to REACH the upstream headline.** `upstream_stale: 001@1.2.0` **records staleness without triggering anything** — it is a five-pin contract field with no consumer. |
| **⚠️ Why this matters more than any single figure** | **A correction that is recorded and never propagated is indistinguishable, in effect, from one never made.** Every artifact in this thesis carries `upstream_stale` and **not one correction has travelled upstream.** *This is the same family the thesis has documented all phase — a check that closes while changing nothing — except that here the check is the programme's own freshness mechanism.* |
| **Proposed rule** | **A correction to a quoted figure must name its UPSTREAM TARGET and either (a) be applied there, or (b) be recorded in a resumption queue that Phase 7's ledger discharges by name.** A pin that records staleness and dispatches nothing is decoration. |
| **Companion structural hazard in 001** | **`report-input.md` IS TWO DOCUMENTS** — 001's report at **L1–965**, then **44 embedded downstream artifacts from L966**. **So the `87.3%` a reader would attribute to 001 is the 1239 artifact's, and BARE LINE CITATIONS INTO THAT FILE ARE AMBIGUOUS BY DEFAULT.** Recorded because it caused a misreading during this phase. |

## A30 — TEST THE COMPARATOR, NOT ONLY THE SUBJECT

**Sources: `SATS × competitive`, `IRDM × competitive`.**

| | |
|---|---|
| **⚠️ The `2 ×` fingerprint is not an issuer property** | **`validate_calculation` was run on a COMPARATOR for the first time this phase**: VSAT returns **`10 pass / 1 warn / 19 fail = 63.3%`** against SATS's **`34.6%`**, and **11 of the 19 VSAT failures carry the `2 ×` fingerprint — NINE EXACT TO THE THOUSAND.** *A defect classified from one issuer had been generalised without ever testing a second.* |
| **⚠️ The comparator's served row can flip a conclusion's sign** | **VSAT's Q1 slot carries a TWELVE-MONTH duration** (EPS 4.48/9.12 in Q1 vs 0.18–0.45 in Q2–Q4). **The served row overstates VSAT `3.97×`; the correct quarter is DERIVED `1,171,288` — so VSAT is `0.32×` SATS, NOT `1.27×`.** |
| **A new instrument failure mode: dimension-blind joining** | SATS `OperatingIncomeLoss` computed `3,657,411` = consolidated revenue `3,667,489` − **eliminations** cost `10,078`, compared against `reported` **`173` = the ELIMINATIONS COLUMN's** value (consolidated is `392,847`). **Two different scopes joined on a period key.** |
| **⚠️ And a clean tie-out is not evidence of a stable boundary** | See A18. At SATS the revenue variances **close to the dollar** while **intersegment revenue collapsed `71,592 → 9,905 (−86.2%)`** and one segment produced **112.5% of the entire consolidated improvement** — 63.4% cost cessation, 54.1% depreciation relief. **A mechanical tie-out certifies that the numbers add up, NOT that the entity is the same one. The segment-composition check must be run separately.** |
| **Proposed rule** | **A benchmarking artifact must run its detectors on the comparator with the same rigour as on the subject, and must report the comparator's period basis, scope basis and sign posture before comparing.** *Two of the three findings above would have been caught by that single practice.* |

---

## Carried forward — already registered, obligation NOT yet discharged

**DA-29 / DA-30 (added at 1.5.0).** None of the artifacts written at pin `1.4.0` names the
source of every reconciliation term, and none names an operating-income basis.
**Discharged in Phase 7's ledger, not by re-running artifacts.**

**DA-23's component-level census.** BWXT established that an issuer can be **clean at every
subtotal while a component of the same statement is sign-corrupted**. Only BWXT has been
tested at component level. **The remaining issuers are subtotal-level-verified only**, and
the census statistic cannot see the difference. Recorded as a **known understatement in the
register's coverage**, not as a clean result.

---

## What this queue does NOT contain

No principle, axiom, bound, sector bias or disposition class changes. **A1–A4 are all
register additions or scope generalisations.** Every falsifier in `spec.md` stands as
written, with the single exception already recorded: **PIL-5's denominator is unstated**
(see `thesis.md`), and **PIL-2's source class cannot be recorded under the citation
contract** — both are specification defects, not register items, and both go to Phase 7.
