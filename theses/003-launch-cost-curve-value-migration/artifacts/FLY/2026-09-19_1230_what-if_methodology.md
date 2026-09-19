---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-1
ticker: FLY
skill: what-if
mode: methodology
generated_at: 2026-09-19T12:30:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "87af28d574e9"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-03
    chosen_reading: "An architecture LABEL is a filed string, not an inference from a described vehicle. FLY's filing contains no architecture label for Alpha at all — `\"expendable\"` returns zero pages — so the F5c assignment required by contract `floor_architecture_consistency` is OUR derivation from the described two-stage, five-engine, no-recovery design. Declared as DERIVED, because the contract mandates the floor while the filing does not supply the label."
  - da_id: DA-01
    chosen_reading: "Basis is a PAIR — price convention AND denominator convention. For Alpha BOTH axes are absent: no price on any of A / A' / B / C, and no denominator on either the capacity or the realized convention. The four-basis table is therefore returned as four absences, and an absence is recorded as absent rather than filled with an estimate."
  - da_id: DA-02
    chosen_reading: "Orbit is named per cell. Alpha's filed payload disclosure names NO orbit — it is a payload CLASS, not a mass to a destination. Orbit is therefore not merely unstated but structurally unavailable at the precision a denominator requires, and no LEO/SSO/GTO bucket is assigned."
  - da_id: DA-06
    chosen_reading: "Price and cost are distinct objects, and neither is revenue. FLY's Launch revenue is not a launch price: the period increase is attributed by the issuer to progress on ENGINEERING-SERVICES contracts for launch-facility development, so the line is a services series. Reading it as a price would be a price/cost/revenue conflation on top of a class-label denominator."
  - da_id: DA-30
    chosen_reading: "Two bases on one concept collapsed without a basis field. Tested POSITIVELY for FLY: the only denominator the filing offers is a payload CLASS whose own disclosed span is 200-1,200 kg. Using it would place a 5-6x ambiguity inside a denominator that carries no basis field — strictly worse than the 1.34x band the correction note withdrew a test over. The correct disposition is ABSENT, not estimated."
  - da_id: DA-26
    chosen_reading: "Annual figures mislabelled as quarterly — established at 19 of 20 issuers, with FLY as the documented COUNTEREXAMPLE. Recorded here as a bounded non-exposure rather than a clean bill: FLY is not reported as universal, and the correction's own carve-out is honoured."
evidence_grade: MODELED
key_metrics:
  payload_class_label_span_min_kg: 200
  payload_class_label_span_max_kg: 1200
  payload_class_label_width_x: 6.0
  class_label_dollar_per_kg_overstatement_at_200kg_x: 5.0
---

# FLY cannot be placed on the curve, and that is a result about F5c, not a gap in FLY

**Pillar note.** T029 is dual-subscribed `[003:PIL-1 / 003:PIL-4]`. The `pillar` frontmatter
field is single-valued by contract (`contracts/artifact-frontmatter.yaml` line 12), so it
carries `PIL-1`, whose matrix FLY's absence is a finding about. `003:PIL-4` is served by the
architecture substitution in §3.3. Both are named rather than merged.

## 1. The finding

**Alpha is `fully_expendable` → F5c. F5c is the only tier in the five-tier split that has a
DEMONSTRATED price. Alpha is the only F5c vehicle in the universe with a filed payload
disclosure — and it emits a payload CLASS, not a payload. It therefore supplies neither term of
a $/kg, and the tier's demonstrated status rests on Electron alone.**

Two consequences, and the second is the one that matters:

**(a) FLY is absent from the curve for a structural reason, not a shortage of research.** The
filing's only payload disclosure is *"the only U.S. company with a liquid-powered orbital
launch vehicle in the **1,000-kilogram payload class**"*
([📄 FLY 10-Q p.34](https://agentii.ai/v/FLY/sec21/34)). That is a **CLASS LABEL**: no
mass, no orbit, no configuration. **A payload class is not a payload denominator.** A class is
a **market span** — the workspace's own figure puts FLY's addressable span at **200–1,200 kg, a
**6× range** — so a $/kg built on the class midpoint would carry a **5–6× ambiguity inside the
denominator** while displaying no basis field. **That is a more severe `DA-30` collapse than the
one the correction note withdrew a test over (a 1.34× band).** The discipline is not pedantry:
**it is the difference between a 1.34× band and a 6× band.** FLY is recorded as **absent**, and
**must not be estimated**.

**(b) The F5c tier's "only architecture with a demonstrated price" status is a ONE-VEHICLE
result, and FLY is the vehicle that would have tested it.** Electron supplies demonstrated list
price (`$9.1M` → `$30,333/kg`, capacity-denominated) **and** demonstrated marginal cost
(`$4.4M` → `$14,667/kg`) — the only vehicle in the universe with a demonstrated marginal cost,
which is `003:PIL-3`'s entire basis. FLY, the other F5c vehicle, supplies **none of the four
bases**: A ✗, A′ ✗, B ✗, C ✗. So a tier-level claim that reads as an architecture property
("fully expendable is where the demonstrated price lives") is in fact **one observation**, and
**the second candidate observation is a non-observation.** The tier assignment is sound; the
**generalisation is not supported by the universe**, and saying so is the result.

**Carried from the correction, stated plainly and unchanged by FLY.** The corrected falsifier
(`threshold=5567`, band `[5567,7448]`) is a **Neutron test**, and FLY contributes no term to it:
`003:PIL-4`'s case **CLOSES** on the registered test and **FIRES** on the withdrawn `$2,939/kg`
bar (equivalent bar **17.0–18.7 t** vs Neutron's filed **13.0 t**). **The case may fire.** FLY's
contribution to that verdict is the **architecture substitution only** — F5c, whole-vehicle
manufacturing floor, no denominator available to test it against.

## 2. Scenario setup

**The what-if.** Place Alpha on the `003:PIL-1` cost curve: assign F5c per the architecture,
denominate on the filed payload, and test the whole-vehicle-manufacturing floor.

**Answer: the scenario cannot be run, on either term, and the failure mode is instructive at
the pillar level.** The architecture assignment succeeds (with a declared derivation); the
denominator does not exist; the price does not exist. **Both terms of the ratio are absent, so
the ratio is absent** — which is a different and better outcome than a ratio whose terms are all
derived. *(A break-even whose terms are all derived is a tautology, not a falsifier; a break-even
with no terms is not a weak falsifier — it is correctly a non-entry.)*

**The vehicle, as filed.**

| Attribute | Value | Disposition | Grade | Source |
|---|---|---|---|---|
| Payload | **"1,000-kilogram payload class"** — class label; no mass, no orbit, no configuration | FILED as a LABEL | DEMONSTRATED (the string) / **ABSENT as a denominator** | [📄 FLY 10-Q p.34](https://agentii.ai/v/FLY/sec21/34) |
| Architecture | Two-stage liquid-powered orbital vehicle, five engines on stage one; **no recovery system described** | FILED as described design | DEMONSTRATED | [📄 FLY 10-Q p.34](https://agentii.ai/v/FLY/sec21/34) |
| Architecture **label** | **"expendable" → 0 pages.** No filed architecture label exists | **ABSENT** | — | see §6 |
| F5c assignment | Required by `contracts/launch-cost-curve.yaml` rule `floor_architecture_consistency` (a `fully_expendable` vehicle MUST carry F5c) | **DERIVED** — the contract mandates it, the filing does not label it | DERIVED | see §3.3 |
| Launch revenue | Filed, but **not a launch price** — attributed to engineering-services contracts for launch-facility development | FILED | DEMONSTRATED | [📄 FLY 10-Q p.40](https://agentii.ai/v/FLY/sec21/40) |
| Payload capacity to a named orbit | none | **UNRESOLVABLE-FROM-PUBLIC-SOURCES** (at the required precision) | — | §6 |
| Price on any of A / A′ / B / C | none | **ABSENT — no basis exists** | — | §3.1 |

**Per-term declaration — FILED cell vs DERIVED cell.** The declaration is short because the
finding is that **there are no terms**:

| Term | Cell type | Grade |
|---|---|---|
| `"1,000-kilogram payload class"` | **FILED string** | DEMONSTRATED |
| Alpha mass to LEO | **DOES NOT EXIST** as a filed cell | — |
| Alpha orbit | **DOES NOT EXIST** as a filed cell | — |
| Alpha launch price | **DOES NOT EXIST** as a filed cell | — |
| Alpha marginal cost | **DOES NOT EXIST** as a filed cell | — |
| **F5c tier assignment** | **DERIVED** — ours, from the described architecture | DERIVED |
| **Any Alpha $/kg** | **NOT PRODUCED** — see §3.2 | — |

## 3. The arithmetic

### 3.1 The four-basis table, returned as four absences

Per **DA-01**, a basis is a **pair**: a price convention and a denominator convention. For
Alpha, **both axes are empty**:

| Basis | Price convention | Numerator | Capacity denominator | Realized denominator |
|---|---|---|---|---|
| **A** (customer list price) | not disclosed | **ABSENT** | **ABSENT** (class label) | **ABSENT** (n/a — see below) |
| **A′** (realized rev./customer launch) | not disclosed | **ABSENT** — and Launch revenue is *services*, not launch (§3.4) | **ABSENT** | **ABSENT** |
| **B** (marginal cost) | not disclosed | **ABSENT** | **ABSENT** | **ABSENT** |
| **C** (fully-loaded) | not disclosed | **ABSENT** | **ABSENT** | **ABSENT** |

**This is a `2 × 2` of absences, and every cell is empty for a reason independent of the
others.** That matters: the table is not empty because FLY is early-stage or because the
extraction failed. **It is empty because FLY discloses a market class where the other issuers
disclose a vehicle.** The one cell that could have been filled — realized revenue per customer
launch on basis A′ — is filled with **services revenue**, which is the wrong object (§3.4).

**The inherited table is confirmed, not merely cited:** plan §F20 records FLY as
**A ✗ / A′ ✗ / B ✗ / C ✗**, and this artifact reproduces that result from the filing rather
than inheriting it. **Reproduction is the point** — an inherited absence and a verified absence
are different evidence classes, and only the second one is a finding.

### 3.2 The denominator that must not be built

If the class label were used as a denominator, the $/kg's ambiguity is computable:

```
span as filed in the workspace                         :  200 kg – 1,200 kg  = 6.0x
denominator ambiguity if the midpoint (1,000 kg) is used:  1,200 / 200    = 6.0x
displacement of the true value from the midpoint at the ends:
     200 kg → $/kg overstated by 5.00x
   1,200 kg → $/kg understated by 1.20x
```

So a single `$X/kg` built on the class label would be **wrong by up to 5× in one direction**,
with **no way for a downstream reader to detect it** — the number would carry no basis field and
the class label reads like a specification. **Compare the magnitudes honestly:**

| Collapse | Ambiguity inside the number | Basis field? |
|---|---|---|
| The withdrawn `$2,939/kg` bar | 1.34× (band across the matched pair) | **none** |
| **A class-label denominator for Alpha** | **6.0×** | **none** |

**The class-label denominator is 4.5× worse than the defect the correction note was written to
remove.** That is why FLY is recorded as **absent** and not as an estimate with a wide
uncertainty band — **a wide band is not a substitute for a basis**, and this is the artifact's
clearest demonstration of the difference.

### 3.3 The architecture substitution, and the label problem (`DA-03`)

`003:PIL-4`'s substance is an architecture substitution: **partially reusable → F5b, not F5a.**
FLY supplies the third tier of the same partition.

| Vehicle | Filed support for the architecture | Tier | Binding cost term | Floor character |
|---|---|---|---|---|
| Neutron | reusable first stage + reusable fairing; **second stage expended** | **F5b** | upper-stage **manufacturing** | soft — a production-learning curve |
| Falcon 9 | reusable first stage; upper stage expended | **F5b** | upper-stage manufacturing | soft |
| Starship | fully reusable | **F5a** | **propellant** | hard, ~$46–92/kg @ 100 t, MODELED |
| **Alpha** | **two stages, five engines, no recovery system described** | **F5c** | **whole-vehicle manufacturing** | **the only tier with a DEMONSTRATED price** |

The tiers are **exhaustive** (`floor_architecture_consistency`), and the mapping is one-to-one.
Two properties of the F5c cell are worth stating plainly because they cut against each other:

- **F5c is the tier that is actually observable.** Electron's `$9.1M` list and `$4.4M` marginal
  cost are both filed, so the whole-vehicle-manufacturing floor is the one floor in the
  five-tier split that a reader can check against a real number.
- **F5c is the tier whose label is not filed for Alpha.** `"expendable"` returns **0 pages** in
  the FLY 10-Q. The F5c assignment is therefore **ours**, derived from the described design, and
  it is mandated by the contract rather than evidenced in the filing. **This is `DA-03` exactly:
  an architecture label treated as known when it is inferred** — and it is the one input in this
  artifact that is ours rather than FLY's. It is not a serious inference (a two-stage vehicle
  with no recovery system is expendable), but **it is an inference, it is load-bearing, and it
  is declared.**

**The honest shape of the F5c claim, therefore:** *the tier with the demonstrated price is
populated by two vehicles, one of which has the price and no denominator and the other of which
has been assigned to the tier by us because the filing does not label it.* `003:PIL-1` should
carry that sentence, not the cleaner "F5c is demonstrated."

### 3.4 The floor cannot be tested, and `UNEXERCISED` is not `CLEAN`

The F5c test would be: **does Alpha's realized $/kg approach the whole-vehicle manufacturing
floor?** It cannot be run — there is no realized $/kg (§3.1) and no filed floor for Alpha. **The
check is `UNEXERCISED`.** Per the standing rule, **an unengaged check is not a passed check**,
and this artifact does **not** report Alpha as clearing its floor.

One asymmetry worth recording, because it is the closest FLY comes to a usable floor
comparison: **on F5c the floor is the whole vehicle's manufacturing cost, so the binding term
does not shrink with reuse — there is no recovery to amortise.** A fully expendable vehicle
therefore cannot escape its own manufacturing cost by flying more; only **production learning**
moves it. That is why F5c is where a demonstrated *price* exists while F5b is where the
*learning curve* lives — and it is the structural reason `003:PIL-4`'s Neutron claim is about
**F5b** and about a **production** curve, not about a propellant floor. **FLY's contribution to
the Neutron scenario is this boundary, established from the tier that sits on the other side
of it.**

### 3.5 Launch revenue is not a launch price (`DA-06`)

The one place Alpha comes near a price is its Launch revenue line, **and it is not a price.**
The period increase is attributed by the issuer to *"our progress on engineering services
contracts for the development of launch facilities"*
([📄 FLY 10-Q p.40](https://agentii.ai/v/FLY/sec21/40)). Consequences:

1. **Basis A is absent for a second, independent reason** — the first being that no price is
   disclosed, the second being that the nearest revenue line is **services-for-facilities**, not
   launch. **Two independent reasons means the absence is robust**, not one search away from
   resolution.
2. **Basis A′ is absent for the same reason**, and this is the specific cell where a careless
   reconstruction would have produced a number: `Launch revenue ÷ payload` reads like a
   matched-pair $/kg and is a **services-revenue-per-class-label** figure. **It would have both
   a wrong numerator and a wrong denominator** — a two-sided `DA-30` collapse.
3. **The services line is a demand signal, not a cost signal.** Engineering-services revenue for
   launch-facility development is the **customer building the ground segment**, which is
   `003:PIL-2` territory (value captured by the party that owns the demand) and is explicitly
   **not** curve evidence. Recorded here so the number is not silently repurposed into `PIL-1`.

**`DA-26` bounded, not waved away.** FLY is the **documented counterexample** to the
annual-as-quarterly defect (19 of 20 issuers). That is recorded as a **bounded non-exposure with
the correction's own carve-out honoured** — FLY is **not** reported as universal, and the
carve-out is not treated as a general clean bill. It does not make the absent terms present.

## 4. The sensitivity — how the answer moves across DA-01 bases A / A′ / B / C

**For Alpha: the answer does not move, because there is nothing to move.** Stating the
sensitivity honestly requires stating that the sensitivity is **empty**, and showing that it is
empty for **four independent reasons** rather than one:

| Basis | Would-be denominator | Would-be numerator | Blocker | `UNEXERCISED` or `ABSENT`? |
|---|---|---|---|---|
| A | class label (6× span) | no disclosed price | **both terms** | ABSENT |
| A′ | class label (6× span) | Launch revenue is **services**, not launch | **both terms, independently** | ABSENT |
| B | class label (6× span) | no disclosed marginal cost | **both terms** | ABSENT |
| C | class label (6× span) | no filed fully-loaded segment | **both terms** | ABSENT |

**Every row is blocked on both axes**, which is the qualitative difference between FLY and the
other two vehicles in this scenario. Neutron has a **filed denominator** and a **claimed
numerator**. Falcon 9 has **filed realized denominators** and an **unfiled capacity
denominator**. **FLY has neither**, and so it is the one vehicle in the scenario whose absence
cannot be narrowed by better research — only by **FLY disclosing a vehicle**, which is a
corporate event, not a retrieval task.

**The cross-vehicle comparison the sensitivity is for** — this is where FLY earns its place in
the scenario, because it is the **third point** that shows the discipline is doing work:

| Vehicle | Denominator | Numerator | Comparable on the curve? |
|---|---|---|---|
| Falcon 9 | filed (realized) / **unfiled** (capacity) | filed, on 3 of 4 bases | **partially** — basis A and A′ unfiled |
| Neutron | **filed** (13,000 kg capacity) | `CLAIMED` ($50–55M ASP) | **yes, as a cell** — both terms exist |
| **Alpha** | **absent** (class label) | **absent** (no price; nearest line is services) | **no — recorded ABSENT** |

**The corrected 1.34× band is a two-vehicle band.** It is the spread between two
**matched-pair** readings of **one** vehicle's two quarters (`$5,568` and `$7,448`), not a
cross-vehicle band. With neutral third-point contributions, **the "sector cost curve" in
`003:PIL-1` currently has two properly-denominated points (Falcon 9 matched-pair and Neutron),
one improperly-denominated point (Falcon 9 basis A/A′), one absent point (Alpha), and one
`MODELED` point (F5a/Starship).** Stating the census that way is more useful than stating a
spread, because the spread's width depends on which points are admitted — **and the correction
changed which points are admitted.**

## 5. What would change the answer

1. **A filed Alpha payload mass to a named orbit.** The single input that creates the
   denominator and moves FLY from `ABSENT` to a curve entry. Without an orbit, a mass alone
   is still not comparable — **`DA-02` requires both.**
2. **A filed Alpha launch price, or a launch-contract value.** Creates basis A. Note that
   **basis B (marginal cost) is what the F5c floor test actually needs**, and no launch provider
   in this universe has filed one except Electron — so (2) would produce a **price**, not a
   floor test.
3. **A filed architecture label.** Would move the F5c assignment from `DERIVED` to
   `DEMONSTRATED` and close the `DA-03` exposure in §3.3. Low effort, real effect: it is the
   only one of these five that FLY could satisfy **without disclosing anything new about the
   vehicle.**
4. **A disclosed bill of materials or production cost for the vehicle.** The F5c floor is a
   whole-vehicle manufacturing cost, so this is the direct route to the tier's own floor — and
   it would supply the **second observation** F5c currently lacks.
5. **A spaceport-integrity restriction or a demand-side shock on the services pipeline.** Would
   move the Launch revenue line for reasons **unrelated to launch economics** — a warning that
   the one FLY series that reads like a curve input is exposed to a driver the curve does not
   model.

## 6. Retrieval scope

**Read this session:**

| Source | Pages | What it supplied |
|---|---|---|
| FLY 10-Q Q2 2026 (`sec21`) | 34 | the **payload class label**; the described two-stage design |
| FLY 10-Q Q2 2026 (`sec21`) | 40 | Launch revenue; the **engineering-services** driver |
| FLY 10-Q Q2 2026 (`sec21`) | 15 | revenue disaggregation cross-check |

**Searches that returned ZERO — each is a result:**

- `"expendable"` in `sec21` → **0 pages.** **No filed architecture label exists.** The F5c
  assignment is `DERIVED` (§3.3) — and this zero is the evidence for that declaration, not an
  excuse for it.
- **No filed Alpha payload mass, at any orbit, was located.** The class label is the only
  payload disclosure in the corpus. **A payload class is not a payload denominator.**
- `list_xbrl_concepts("Payload")` → **0 concepts; `list_xbrl_concepts("Launch")` → 0
  concepts**, against **109** for `"Revenue"`. The platform's structured layer contains **no
  payload and no launch concept at all**, so no denominator for Alpha could be assembled from
  `search_xbrl_facts` **even if the filing carried one.**

**Dispositions, three classes:**

- **FILED (recordable):** the class-label string; the described two-stage design; the Launch
  revenue series; the engineering-services attribution.
- **`REACHABLE-BUT-NOT-RECORDABLE`** — the datum is reachable, but the citation contract (§3
  rule 7: only `agentii.ai` URLs admissible) cannot record it, because no agentii source
  contains it:
  - **Alpha's payload mass to a named orbit.** Reachable from published vehicle
    specifications; absent from the filing, which stops at the class label. **This is the
    specific datum whose absence keeps FLY off the curve.**
  - **FLY's addressable payload span (200–1,200 kg, 6×)** — inherited as a market span; no
    agentii source records it, so the **magnitude** in §3.2 is carried as inherited context and
    is **not** used to construct a denominator. *(Using it to construct one is precisely the
    error §3.2 forbids.)*
  - **F5a's propellant mass and price inputs** — inherited as `CLAIMED`, still unfiled.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`:** Alpha's payload to a **named orbit** at the precision
  a denominator requires (a class label cannot be refined into one); Alpha's **marginal cost on
  basis B** — the input the F5c floor test needs and the one no provider except Electron has
  ever filed; Alpha's **fully-loaded segment cost on basis C**.
- **`UNRESOLVABLE-FROM-PLATFORM`:** any payload or launch denominator assembled from the
  structured layer — the concepts **do not exist** (§6). `get_segment_data` and
  `data_freshness` are unusable per the inherited constraints and were **not used**; every
  figure above is read from page text.

**`UNEXERCISED`, explicitly — not `CLEAN`:**

- **The F5c whole-vehicle-manufacturing floor test on Alpha.** No floor, no realized $/kg, so
  no comparison. **Alpha is not reported as clearing its floor.**
- **Basis B and basis C for Alpha** — every cell absent (§3.1), each for an independent reason.
- The `DA-23` sign test. **No FLY figure in this artifact depends on the sign of an extracted
  value**: the class label is a string, the revenue series is read as positive-by-construction
  from page text, and no per-share or per-unit figure is used. The test is **unexercised**, and
  this artifact does **not** claim FLY is clean of `DA-23`.
- `DA-26` is recorded as a **bounded non-exposure** with the correction's carve-out honoured —
  **not** as a general clean bill.

---

**Bottom line for the caller.** T029's disposition is a **verified absence**, reproduced from
the filing rather than inherited: **Alpha is F5c (fully expendable → whole-vehicle manufacturing
floor), and it contributes no term to the curve.** The filing's only payload disclosure is a
**class label** with no mass, no orbit and no configuration, and a class label is a **market
span (200–1,200 kg, 6×)**, not a denominator — using it would place a **6.0× ambiguity** inside
the number, **4.5× worse than the 1.34× defect the correction note withdrew a test over**. So
FLY is recorded **ABSENT, not estimated**, and **all four DA-01 bases are empty on both axes,
each for an independent reason** — the sharpest being that the nearest revenue line is
**engineering-services-for-launch-facilities**, a services series misreadable as a launch price.
The finding that matters at pillar level: **F5c is the only tier with a DEMONSTRATED price, and
FLY is the vehicle that would have tested that generalisation — it fails to, so the tier's
demonstrated status is a one-vehicle result.** The architecture label `"expendable"` returns
**zero pages**, so the F5c assignment is **ours** (declared `DA-03`), and the F5c floor test
stays **`UNEXERCISED`** — which is not `CLEAN`.
