---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-1
ticker: SPCX
skill: what-if
mode: methodology
generated_at: 2026-09-19T12:30:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "87af28d574e9"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-01
    chosen_reading: "Basis is a PAIR — a price convention AND a denominator convention. A (list price), A' (realized revenue per customer launch), B (marginal cost), C (fully-loaded amortized). On this vehicle the denominator axis moves the answer more than the basis axis does, so both are named per cell."
  - da_id: DA-02
    chosen_reading: "Orbit is named per cell. SPCX defines mass to orbit as ALL customer payload deployed, not LEO alone. The matched-pair denominator is therefore BLENDED-orbit and is not commensurable with a LEO-only capacity denominator. Carried as a stated limitation that moves in one direction (see §4.4), not smoothed away."
  - da_id: DA-21
    chosen_reading: "The segment boundary is the ISSUER's, and here it is drawn at the CUSTOMER, not the launch: ~73% of launches produce no Space segment revenue by design. The Space segment is therefore not a launch-price series and cannot be read as one."
  - da_id: DA-30
    chosen_reading: "The concept 'SPCX USD per kg' carries at least six defensible values from one 10-Q ($939 / $2,939 / $4,219 / $5,568 / $6,596 / $7,409 / $7,448 / $11,977). These are bases and denominators, not rival estimates. Every line below carries its basis letter AND its denominator convention; no single basis is adopted as 'the' answer."
  - da_id: DA-29
    chosen_reading: "A reconciliation that closes is not thereby a check. Applied in the negative direction here: the $158M Launch Services variance DOES appear in the source text, so the cross-check on the matched-pair reconstruction is a PRESENCE check, not a back-solve — and is admissible for that reason only."
  - da_id: DA-25
    chosen_reading: "Whether SPCX's published per-kg figures are reproducible from filed cells is tested directly, not asserted. The matched-pair reconstruction that reproduces them is shown in full so the reader can test the reproduction."
evidence_grade: MODELED
key_metrics:
  usd_per_kg_ladder_low_launch_services_over_mass_to_orbit: 939
  usd_per_kg_ladder_high_space_segment_over_customer_payload: 11977
  usd_per_kg_ladder_spread_ratio: 12.8
  internal_launch_share_of_falcon_launches_pct: 73.0
---

# Falcon 9's price per kg is a denominator choice, and Neutron lands on its knife-edge

**Pillar note.** T028 is dual-subscribed `[003:PIL-1 / 003:PIL-4]`. The `pillar` frontmatter
field is single-valued by contract (`contracts/artifact-frontmatter.yaml` line 12), so it
carries `PIL-1`, whose matrix this artifact builds and whose sensitivity it tests.
`003:PIL-4` is served by the bar test in §3.4. Both are named rather than merged.

## 1. The finding

**SPCX's filed figures support a $/kg band of `$939` to `$11,977` — a 12.8× spread — from one
10-Q. That is not uncertainty. It is five bases on two denominator conventions, and the
correction note's own `$5,567/kg` threshold is one rung on that ladder, not a measurement of
the vehicle.**

Three consequences, in order of importance:

**(a) The corrected falsifier's threshold is an SPCX construct, and it sits at the ladder's
median rung.** `$5,567/kg` is `$490M ÷ 88,000 kg` — Launch Services revenue over **realized**
customer payload. The withdrawn `$2,939/kg` is `$67M ÷ 22.8 t` — a **list price** over a
**capacity**. The correction moved the threshold from the second rung to the median rung, i.e.
it moved it from `CLAIMED`/unfiled to `DEMONSTRATED`/filed. **That is a genuine improvement in
admissibility and it is also a 1.9× relaxation of the bar.** Both are true and both are stated.

**(b) Neutron at its disclosed ASP lands inside SPCX's basis A′ to within 0.3%.** Basis A′ is
`$4,219/kg` (`$962M ÷ 10 ÷ 22.8 t`). Neutron's implied band is **`$3,846–4,231/kg`**
(`$50–55M ÷ 13,000 kg`). **The A′ point estimate sits 12 dollars below the top of Neutron's ASP
band.** So the proposition *"Neutron undercuts Falcon 9 on realized revenue per launch"* is
**TRUE at $50M and FALSE at $55M** — a verdict that turns on a 10% ASP move and on a
denominator neither vehicle files. This is the sharpest expression of the whole scenario and it
is an accident of two unfiled conventions meeting, not a finding about either rocket.

**(c) Falcon 9's capacity is not filed, and '22.8' returns zero pages.** Verified this session:
`search_keyword_in_source(sec8, "22.8")` → **0 pages**; `"payload capacity"` → 2 pages, both
definitions of **mass to orbit** (a *realized* metric), not a vehicle capacity. **Every basis
letter A / A′ / B / C is denominated on that one unfiled number.** The filed denominators —
87 t, 88 t, 132 t — are all realized. **SPCX's own ladder therefore has four rungs it cannot
source and four it can, and the two sets are not comparable to each other.**

**Carried from the correction, stated plainly.** On the registered test
(`> $5,567/kg`, band `[5,567, 7,448]`), Neutron's `$3,846–4,231/kg` **CLOSES**. On the withdrawn
`$2,939/kg` bar it **FIRES**, with an equivalent bar of **17.0–18.7 t** against Neutron's filed
**13.0 t**. **The case closes on the current registration and may fire**; §3.4 gives the exact
condition under which it fires on the corrected test too.

## 2. Scenario setup

**The what-if.** Neutron reaches the market at its disclosed ASP and flies at its filed
capacity. **Does SPCX's point on the `003:PIL-1` curve move?**

**Answer, established below: no.** SPCX's curve point is not a price and does not respond to a
competitor's price; it is a basis choice. What the scenario actually moves is **which rung of
SPCX's own ladder the falsifier is denominated on** — and that is why the thesis's verdict
flipped without any input about Neutron changing at all.

**The vehicle, as filed.**

| Attribute | Value | Disposition | Grade | Source |
|---|---|---|---|---|
| Architecture | reusable first stage, expended upper stage — **partially reusable** | FILED | DEMONSTRATED | [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35) |
| Applied floor tier | **F5b** (upper-stage manufacturing floor, soft) | DERIVED from the filed architecture | DEMONSTRATED (architecture) / MODELED (tier label) |
| Payload capacity | **not filed** — no LEO capacity number exists in the 10-Q | **REACHABLE-BUT-NOT-RECORDABLE** | see §6 |
| Realized customer payload | 87 t (Q2 2026); 88 t (Q2 2025); 132 t (H1 2026) | FILED | DEMONSTRATED | [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35) |
| Launch Services revenue | $648M (Q2 2026); $490M (Q2 2025); $978M (H1 2026) | FILED | DEMONSTRATED | [📄 SPCX 10-Q p.13](https://agentii.ai/v/SPCX/sec8/13) |
| Segment boundary | **the CUSTOMER boundary** — most launches carry no Space revenue | FILED | DEMONSTRATED | [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42) |

**Per-term declaration — FILED cell vs DERIVED cell.**

| Term | Cell type | Grade |
|---|---|---|
| $648M / $490M / $978M Launch Services revenue | **FILED** | DEMONSTRATED |
| 87 t / 88 t / 132 t customer payload | **FILED** | DEMONSTRATED |
| $158M Launch Services YoY variance | **FILED** (appears in MD&A text) | DEMONSTRATED |
| **All four matched-pair $/kg values** | **DERIVED** — the divisions are ours | figures DEMONSTRATED / division MODELED |
| `22.8 t` capacity (A, A′, B, C) | **NEITHER** — not filed, not recordable | CLAIMED |
| `$67M` list price (basis A) | **DISCLOSED, unfiled** | CLAIMED |
| `~$12–20M` marginal cost (basis B) | **MODELED** — inherited, never filed | MODELED |
| `$962M ÷ 10` Space-segment per-launch (A′) | **DERIVED** from a filed total ÷ a filed count | DEMONSTRATED / MODELED |

**The reproduction test, run in the open** (this is the DA-25 discipline — a published
normalisation must be reproducible or it is an artefact):

```
Q2 2026 : $648M ÷ 87,000 kg = $7,448/kg      ✔ reproduced this session
Q2 2025 : $490M ÷ 88,000 kg = $5,568/kg      ⚠ note below
H1 2026 : $978M ÷ 132,000 kg = $7,409/kg     ✔ reproduced this session
```

**Two recorded discrepancies, neither smoothed:**
1. The correction note gives the Q2 2025 figure as **`$5,567/kg`**. Exact computation gives
   **`$5,568/kg`** (`490,000,000 ÷ 88,000 = 5,568.18`). The 0.02% gap is rounding-level and
   **does not move the band**: `7,448 ÷ 5,568 = 1.338` against `7,448 ÷ 5,567 = 1.338`. The
   **1.34× band statement survives**; the quoted point does not reproduce exactly, and is
   recorded rather than adjusted.
2. The inherited statement *"~74% of Falcon launches produce no Space revenue by design"* is
   **approximately** reproduced: the Q2 2026 filed cells give **27 of 37 = 73.0%** internal.
   The inherited figure is carried as approximately reproduced, **not** as an exact match.

**Independent confirmation that the reconstruction is the intended one.** MD&A states the
Launch Services variance of **`+$158M`** year over year
([📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42)), which closes against `$648M −
$490M` exactly. Per **DA-29**, note *why* this is admissible: the `$158M` term **appears in the
source text** — this is a **PRESENCE check, not a back-solve**. A reconciliation whose terms
cannot be located in the source proves nothing; this one's can be, and it is cited.

## 3. The arithmetic

### 3.1 The comparator ladder built from filed cells only

| # | Basis | Denominator convention | Value | Grade | Filed numerator? | Filed denominator? |
|---|---|---|---:|---|---|---|
| L1 | Pool-wide | all mass to orbit (blended orbit) | **$939/kg** | DEMONSTRATED figures / MODELED division | yes | yes |
| L2 | **A** (withdrawn) | capacity, 22.8 t | **$2,939/kg** | **CLAIMED** | **no** ($67M unfiled) | **no** |
| L3 | **A′** | capacity, 22.8 t | **$4,219/kg** | DEMONSTRATED / MODELED | yes | **no** |
| L4 | **B** | capacity, 22.8 t | **~$525–875/kg** | **MODELED** | **no** | **no** |
| L5 | matched pair | **realized**, 88 t (Q2 2025) | **$5,568/kg** | DEMONSTRATED / MODELED | yes | yes |
| L6 | **C** | capacity, 22.8 t | **$6,596/kg** | DEMONSTRATED / MODELED | yes | **no** |
| L7 | matched pair | **realized**, 132 t (H1 2026) | **$7,409/kg** | DEMONSTRATED / MODELED | yes | yes |
| L8 | matched pair | **realized**, 87 t (Q2 2026) | **$7,448/kg** | DEMONSTRATED / MODELED | yes | yes |
| L9 | Space rev. matched pair | **realized**, 132 t (H1 2026) | **$11,977/kg** | DEMONSTRATED / MODELED | yes | yes |

**Spread: `$939 → $11,977` = 12.76× ≈ 12.8×.** Four of nine rungs (L2, L3, L4, L6) rest on
the **unfiled** `22.8 t` — and they are precisely the four that carry the **basis letters**.

### 3.2 The axis that does the work

Decompose the spread into its two axes:

| Move | From → To | Factor |
|---|---|---:|
| **Basis axis**, capacity denominator held | L3 (A′) → L6 (C) | **1.56×** |
| **Basis axis**, realized denominator held | L8 (A′-convention) → L9 (fully-loaded) | **1.61×** |
| **Denominator axis**, basis A′ held | L3 (capacity 22.8 t) → L8 (realized 87 t) | **1.77×** |
| **Denominator axis**, same revenue convention | L8 (realized) → L3 (capacity) | **1.77×** |
| **Convention axis** (list → realized), capacity held | L2 (A) → L3 (A′) | **1.44×** |

**The denominator axis moves the answer at least as much as the basis axis does, and it is the
axis the correction note did not name as an axis.** `$2,939 → $4,219` was read as a basis
correction (A → A′). It is equally a **1.44× convention change**, and the companion move that
actually produced `$5,567` is a **denominator** change. **The falsifier's threshold moved 1.9×
because two things changed at once and only one was labelled.**

### 3.3 DA-30 evaluated, not just cited

The single-concept-many-values defect is normally reported as a platform extraction fault. Here
it is **structural**: the values are not extraction errors, they are **faithful readings of
different things**. The test is whether each value's **basis field is recoverable**.

| Value | Basis recoverable? |
|---|---|
| $939/kgg | **no** — no basis field; "all mass to orbit" is a realized denominator that no basis letter owns |
| $2,939/kg | partially — basis A, denominator unfiled |
| $4,219/kg | partially — basis A′, denominator unfiled |
| $525–875/kg | **no** — basis B is MODELED, so there is nothing to denominate |
| $5,568 / $7,409 / $7,448 / $11,977 /kg | **yes** — fully filed on both axes |

**Five of nine values carry an unrecoverable or partially-recoverable basis.** The four
fully-recoverable ones are the matched pair. **That is the argument for the correction**: not
that `$5,567` is more accurate, but that it is the only family on the ladder with **both axes
filed**. The argument is sound, and its cost — a 1.9× leniency — is what §3.4 quantifies.

### 3.4 The bar, and whether `003:PIL-4` closes or fires

Bar (payload required for Neutron at its ASP to match an SPCX comparator) `= ASP ÷ comparator`:

| SPCX comparator | $/kg | Bar @ $50M | Bar @ $55M | vs Neutron's filed 13.0 t |
|---|---:|---:|---:|---|
| L1 pool-wide | $939 | 53.2 t | 58.6 t | **FIRES** |
| **L2 basis A — withdrawn** | **$2,939** | **17.0 t** | **18.7 t** | **FIRES** |
| **L3 basis A′** | **$4,219** | **11.9 t** | **13.0 t** | **KNIFE-EDGE** |
| L5 matched pair Q2 2025 | $5,568 | 9.0 t | 9.9 t | closes |
| L7 matched pair H1 2026 | $7,409 | 6.7 t | 7.4 t | closes |
| L8 matched pair Q2 2026 | $7,448 | 6.7 t | 7.4 t | closes |
| L9 Space-rev matched pair | $11,977 | 4.2 t | 4.6 t | closes |

**Stated plainly, both ways.** `003:PIL-4`'s case **CLOSES** on the currently registered
falsifier (`threshold=5567`, band `[5567,7448]`): its bar is 9.0–9.9 t against a filed 13.0 t.
It **FIRES** on the withdrawn `$2,939/kg` bar, where the equivalent bar is **17.0–18.7 t** —
i.e. Neutron would need **31–44% more payload than it files**. **The case may fire and the
scenario carries that outcome.** The A′ cell is the one to watch: at `$4,219/kg`, `$50M` needs
**11,851 kg** (closes by 8.8%) while `$55M` needs **13,035 kg** — **fires by 35 kg, 0.27%**.

**The condition under which the registered test also fires** — this is the honest form of the
close:

```
fires on the CORRECTED test if Neutron's REALIZED payload < ASP ÷ $5,568/kg
       →  $50M → 8,981 kg        $55M → 9,880 kg
```

**Both are below Neutron's filed capacity, and both are near Falcon 9's own filed realized
average.** SPCX's realized average is **8,700 kg (Q2 2026)** and **9,778 kg (Q2 2025)** —
**38.2%–42.9% of its 22.8 t capacity**. So the corrected test passes only if Neutron flies at
**69.2%–76.2% of its own capacity**, roughly **1.8× the comparator's filed utilization**.

**The registered "close" compares Neutron's CAPACITY $/kg against SPCX's REALIZED $/kg.** The
comparison is therefore not like-for-like in Neutron's favour, and the thesis should say so:
**the close is a denominator artefact until Neutron's first flight produces a realized
payload.**

## 4. The sensitivity — how the answer moves across DA-01 bases A / A′ / B / C

### 4.1 The scenario run per basis

"What happens to SPCX's `003:PIL-1` curve point if Neutron enters at `$50–55M`?"

| Basis | SPCX value | Neutron value | Neutron cheaper? | Does SPCX's curve point move? |
|---|---:|---:|---|---|
| A (list) | $2,939/kg (unfiled) | $3,846–4,231/kg | **NO — Neutron is 1.31–1.44× dearer** | no |
| **A′ (realized rev./launch)** | **$4,219/kg** | **$3,846–4,231/kg** | **STRADDLES — cheaper at $50M, dearer at $55M** | **no, but the ordering flips** |
| B (marginal cost) | ~$525–875/kg (MODELED) | **absent** | **UNEXERCISED** | no |
| C (fully-loaded) | $6,596/kg | absent | **UNEXERCISED** | no |

**Why SPCX's curve point does not move under any of the four.** Because the point is a
**realized** figure and the scenario supplies a **price**. `003:PIL-1`'s curve is a cost curve;
`$50–55M` is a price (`DA-06`). A competitor's price cannot move a cost curve — it can only
move **where on the curve the market clears**, which is a demand question this artifact does
not have the inputs to answer and does not pretend to.

**Basis B and basis C are `UNEXERCISED` for Neutron**, and per the standing rule **an
unengaged check is not a passed check**. Neutron's marginal cost and fully-loaded cost are both
absent; every Neutron-vs-SPCX comparison in circulation is therefore a **price-vs-price**
comparison being read as if it were **price-vs-cost**. That mis-reading is the mechanism by
which "Neutron is cheaper" is converted into a claim about margin, and **nothing in either
filing supports the conversion.**

### 4.2 The matrix consequence — `003:PIL-1`'s headline re-derived

`003:PIL-1` inherits **"the cost curve spans ~$500 to ~$6,600, a 7–13× spread."** Run through
the basis-mix sensitivity:

- The **endpoints are not on the same basis**: `$500`-class is **basis B** (marginal cost,
  `MODELED`, capacity denominator); `$6,600`-class is **basis C** (fully-loaded, capacity
  denominator). **Those two are commensurable** — same denominator convention, adjacent basis
  letters. **The 7–13× spread survives as a statement about SPCX alone.**
- What does **not** survive is the reading of that spread as the **sector's** cost curve.
  Adding RKLB's basis-B point (`$4.4M ÷ 300 kg = $14,667/kg`, **filed**) to SPCX's
  `$525–875/kg` gives **16.8×–27.9×**, and the comparison is **filed over unfiled** — Electron's
  marginal cost is a filed cell and Falcon 9's is a `MODELED` one.
- **On the matched-pair basis the sector spread is 1.34×** (`$5,568–7,448/kg`), which is the
  correction's own number and is **the narrowest defensible reading**. The 7–13× and the 1.34×
  are both correct; they answer different questions, and **the artifact that quotes one without
  the other is the DA-30 violation the correction exists to prevent.**

### 4.3 The customer boundary, quantified as a curve caveat (`DA-21`)

SPCX draws the segment boundary at the **customer**, not the launch. Consequence for the
curve: **the Space segment is not a launch-price series.** With **27 of 37 (73.0%)** Q2 2026
launches carrying no Space revenue, `Launch Services revenue ÷ customer payload` (`$7,448/kg`)
is the price of launches that **have an external customer**, not the price of a Falcon 9.

**Therefore `$7,448/kg` is an upper bound on a launch price under a customer-selection filter**,
and the filter is not neutral: the missions that produce no Space revenue are disproportionately
the ones with a *different* economics (internal Starlink-class deployment). **The corrected
falsifier's threshold inherits that filter.** A threshold built on a customer-filtered
numerator is a **`CLAIMED`-flavoured** threshold even though both its terms are filed — because
the **selection rule** is issuer-defined. This does not invalidate the threshold; it bounds its
claim to *"external-customer launches,"* which is narrower than *"Falcon 9."*

### 4.4 The direction of the orbit non-commensurability (`DA-02`)

The matched-pair denominators are **blended-orbit**: mass to orbit counts all customer payload
deployed, including higher-energy missions that pay more per kilogram and deliver less mass.
Neutron's filed `13,000 kg` is **LEO**. So `$5,568–7,448/kg` **overstates** a pure-LEO
comparator.

**The bias runs one way and it is knowable:** an orbit-matched LEO-only denominator would be
**larger than 87 t**, which makes the $/kg **smaller**, which makes the threshold **lower**,
which makes the test **more likely to fire**. **The registered falsifier is therefore
`DA-02`-biased in Neutron's favour, and the bias is stated rather than corrected** — correcting
it would require an orbit-split of the mass-to-orbit table that SPCX does not file, i.e. a
denominator that is `REACHABLE-BUT-NOT-RECORDABLE` (§6).

## 5. What would change the answer

1. **A filed Falcon 9 payload capacity.** One number, and it converts **four of nine ladder
   rungs and all four basis letters** from `CLAIMED` to filed. It is the highest-leverage
   missing input in the entire pillar and it is **not in the filing** (§6).
2. **An orbit-split of mass to orbit (LEO vs higher energy).** Would remove the `DA-02` bias in
   §4.4, which currently runs **in Neutron's favour** and makes the close look better than it is.
3. **A Neutron marginal cost, or a Neutron flight with a disclosed realized payload.** Either
   one converts the price-vs-price comparison of §4.1 into the price-vs-cost comparison the
   curve actually requires. Without one, **basis B stays `UNEXERCISED`** on the entering vehicle.
4. **SPCX's own marginal cost per launch, filed.** Basis B is the only basis the F5 floor tests.
   It is `MODELED` here and has been for the life of the thesis; `003:PIL-3`'s "one measurable
   vehicle, and it is Electron" depends on this staying unfiled, so **its appearance would be a
   pillar-level event, not an artifact-level one.**
5. **A quarterly restatement of launch count on the Space-segment boundary.** If the internal/
   external split shifts, `$7,448/kg` shifts mechanically with no vehicle change. The threshold
   is exposed to a **disclosure-policy** variable, not an engineering one.

## 6. Retrieval scope

**Read this session:**

| Source | Pages | What it supplied |
|---|---|---|
| SPCX 10-Q Q2 2026 (`sec8`) | 13 | Launch Services revenue $648M / $490M |
| SPCX 10-Q Q2 2026 (`sec8`) | 35 | mass to orbit 87 t / 88 t; architecture; launch counts |
| SPCX 10-Q Q2 2026 (`sec8`) | 42 | Space segment; `+$158M` Launch Services variance; customer boundary |

**Searches that returned ZERO — each is a result:**

- `"22.8"` in `sec8` → **0 pages** (run twice). The **basis-A denominator is
  denominator-failed**, reproduced independently rather than inherited.
- `"per kilogram"` in `sec8` → **0 pages.** No filed $/kg exists on any basis; **every $/kg in
  this artifact is our division**, not the issuer's number.
- `"payload capacity"` in `sec8` → **2 pages**, both the **key-business-metrics definitions of
  mass to orbit** (a realized metric). **No vehicle capacity is filed any basis A/A′/B/C rests
  on an unfiled denominator.**
- `list_xbrl_concepts("Payload")` → **0 concepts; `list_xbrl_concepts("Launch")` → 0
  concepts**, against **109** for `"Revenue"`. The platform's structured layer contains **no
  payload and no launch concept at all** — so a $/kg can never be assembled from
  `search_xbrl_facts`, and a downstream query that finds nothing **cannot distinguish that from
  a failed search.** This is the platform-layer determination, and it is the reason every
  figure above is read from page text.

**Dispositions, three classes:**

- **FILED (recordable):** all revenue figures; all mass-to-orbit figures; launch counts; the
  `+$158M` variance; the `$962M ÷ 10` components of basis A′.
- **`REACHABLE-BUT-NOT-RECORDABLE`** — the datum is reachable but the citation contract
  (§3 rule 7: only `agentii.ai` URLs admissible) cannot record it, because no agentii source
  contains it:
  - **Falcon 9's `22.8 t` LEO capacity.** Published vehicle spec; absent from the filing and
    from the concept inventory. **The denominator of all four basis letters.**
  - **The `$67M` list price** (basis A numerator). Publicly quoted; not in the filing — which is
    why removing it removed a `CLAIMED` term and not just a denominator.
  - **The orbit split of mass to orbit** (LEO vs higher-energy). The data exists in the launch
    manifest; the filing aggregates it.
  - **F5a's propellant mass/price inputs** — inherited as `CLAIMED`, still unfiled.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`:** SPCX's **marginal cost per launch** (basis B) — the
  only basis the F5 floor can test, and it has never been filed by any launch provider in this
  universe; the **per-launch orbit assignment** needed to make the matched pair orbit-commensurable.
- **`UNRESOLVABLE-FROM-PLATFORM`:** any $/kg assembled from the structured layer — the payload
  and launch concepts **do not exist** there (§6). `get_segment_data` and `data_freshness` are
  unusable per the inherited constraints and were **not used**.

**`UNEXERCISED`, explicitly — not `CLEAN`:**

- The F5b floor test on SPCX (no marginal cost → no floor comparison).
- Basis B and basis C for Neutron (§4.1).
- The `DA-23` sign test. **No SPCX figure in this artifact depends on the sign of an extracted
  value**: revenue, payload mass and launch counts are all positive-by-construction quantities
  read from page text. The test is therefore **unexercised**, and this artifact does **not**
  claim SPCX is clean of DA-23.

---

**Bottom line for the caller.** T028's contribution to the Neutron scenario is the **threshold
itself**. SPCX's filing supports **nine** values for one concept, spread **12.8×**; the
correction moved the falsifier from rung 2 (`CLAIMED`, unfiled denominator) to rung 5
(`DEMONSTRATED`, both axes filed) — **more admissible and 1.9× more lenient at the same time**.
On the registered test Neutron at `$3,846–4,231/kg` **CLOSES**; on the withdrawn `$2,939/kg`
bar it **FIRES**, equivalent bar **17.0–18.7 t** vs a filed **13.0 t**. It **straddles basis A′
to within 0.3%**, so the ordering of SPCX and Neutron reverses on a 10% ASP move. The close is
contingent on Neutron achieving a filed-realized utilization **~1.8× Falcon 9's own**, and the
test is **`DA-02`-biased in Neutron's favour** by an aggregation SPCX does not break out. The
decisive missing input is **Falcon 9's filed capacity**, and it is
`REACHABLE-BUT-NOT-RECORDABLE`.
