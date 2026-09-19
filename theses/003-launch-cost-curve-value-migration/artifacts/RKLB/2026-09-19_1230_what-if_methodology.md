---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-4
ticker: RKLB
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
    chosen_reading: "Basis is a PAIR — a price convention AND a denominator convention. The four registered bases are A (customer list price), A' (realized revenue per customer launch), B (marginal cost per launch), C (fully-loaded amortized). Every $/kg below is stated with both the basis letter and the denominator convention (capacity or realized), because a basis letter alone does not identify the number."
  - da_id: DA-02
    chosen_reading: "Orbit is named per cell. Neutron's filed capacity is LEO; Electron's filed capacity is LEO; Falcon 9's matched-pair denominator is BLENDED-orbit (SPCX defines mass to orbit as all payload deployed to orbit, not LEO alone), and that non-commensurability is carried as a limitation, not smoothed."
  - da_id: DA-30
    chosen_reading: "The concept 'Falcon 9 USD per kg to LEO' carries at least five values from one filing set ($939 / $2,939 / $4,219 / $5,568-7,448 / $11,977). These are not rival estimates of one quantity — they are three different bases on two different denominators. Both axes are reported on every line; no single basis is adopted as 'the' answer."
  - da_id: DA-25
    chosen_reading: "RKLB's disclosed 'revenue per launch' / 'cost per launch' are normalisations the issuer defines and are NOT reproducible by summing to the audited Launch Services segment table. Used as a disclosed metric with its non-reproducibility stated, never as the segment revenue."
  - da_id: DA-23
    chosen_reading: "Served sign is not trusted. No figure in this artifact depends on the sign of an extracted value: the per-launch metrics, the segment table and the mass-to-orbit table are all read from page text with both directions present. The DA-23 component-identity test is therefore UNEXERCISED here, not CLEAN."
evidence_grade: MODELED
deal_security_basis: standalone_pre_merger
key_metrics:
  neutron_implied_cost_per_kg_leo_usd_low: 3846
  neutron_implied_cost_per_kg_leo_usd_high: 4231
  neutron_a_prime_breakeven_payload_kg_at_50m_asp: 11851
  neutron_a_prime_breakeven_payload_kg_at_55m_asp: 13035
---

# Neutron break-even: the verdict is set by Falcon 9's denominator, not by Neutron

**Pillar note.** T027 is dual-subscribed `[003:PIL-1 / 003:PIL-4]`. The `pillar` frontmatter
field is single-valued by contract (`contracts/artifact-frontmatter.yaml` line 12, enum
`[PIL-1..PIL-6, cross]`), so it carries `PIL-4`, whose claim this artifact tests directly.
`003:PIL-1` is served by the basis-mix sensitivity in §4. Both are named rather than merged.

## 1. The finding

**At Neutron's disclosed ASP the implied price is `$3,846–4,231/kg`. That figure FIRES the
withdrawn `$2,939/kg` bar and CLOSES on the corrected matched-pair band `[$5,567, $7,448]/kg`.
Both outcomes are correct on the same arithmetic, because the comparator moves 2.5× across
bases and 12.8× across denominators while Neutron does not move at all.**

The consequence for `003:PIL-4` is uncomfortable and is the real result:

> **The falsifier as corrected does not test Neutron. It tests Falcon 9's denominator
> convention.** Neutron's `$3,846–4,231/kg` uses a **capacity** denominator (13,000 kg, its
> maximum filed capability). The comparator band `$5,567–7,448/kg` uses a **realized**
> denominator (8,700–9,778 kg per customer launch — Falcon 9's actual flown average). The
> test passes because a full vehicle is being priced against a partly-empty one. This is
> **DA-30 reproduced inside the correction that was written to fix a DA-30 collapse.**

**Verdict, stated plainly, both ways:**

| Test | Threshold / band | Neutron implied | Outcome |
|---|---|---|---|
| Withdrawn bar | `> $2,939/kg` | $3,846–4,231/kg | **FIRES** (1.31–1.44× above) |
| Registered test (current) | `> $5,567/kg`, band `[5,567, 7,448]` | $3,846–4,231/kg | **CLOSES** (0.69–0.76× of the threshold) |
| Basis A′ (realized Space rev. ÷ customer launch ÷ 22.8 t) | `$4,219/kg` | $3,846–4,231/kg | **KNIFE-EDGE — flips inside the ASP band** |
| Pool-wide (`Launch Services ÷ ALL mass to orbit`) | `$939/kg` | $3,846–4,231/kg | **FIRES** (4.1–4.5× above) |

**PIL-4's case closes on the falsifier it currently registers, and it is not robust in doing
so.** The close is contingent on a utilization assumption (§3.4) that is *more favourable than
the comparator vehicle's own filed performance*. Carried per the correction note: **P4 may
FALSIFY, and on one basis it does.**

**Two stale premises are NOT repeated here.** Neutron's payload is **no longer a `CLAIMED`
input** — it is filed at ~13,000 kg. And **Neutron has not flown** (10-Q: target delivery to
the pad Q4 2026, first-launch window "narrowing").

**One live defect found in this thesis's own files.** `spec.md` §1b line 145 still tabulates
`Fully expendable → Constitution floor: none named`, which is the **pre-v1.3.0 reading**. It is
contradicted by §1c line 403 of the same file and by `contracts/launch-cost-curve.yaml`
(validation rule `floor_architecture_consistency`). This is the `A29` defect class — **a
correction that exists and is not read** — and it is the third instance recorded in 003.

## 2. Scenario setup

**The question.** `003:PIL-4` claims Neutron's medium-lift case "closes arithmetically only
above a stated payload bar, and it rests on F5b, not F5a." The scenario tests that claim under
the one architecture substitution that matters (partial → F5b, not F5a) and across every DA-01
basis the workspace registers.

**The vehicle, as filed — not as published.**

| Attribute | Value | Disposition | Grade | Source |
|---|---|---|---|---|
| Payload capacity | ~13,000 kg, **reusable configuration**, to LEO | FILED (narrative) | DEMONSTRATED | [📄 RKLB 10-Q p.34](https://agentii.ai/v/RKLB/sec109/34); [📄 RKLB 10-K p.8](https://agentii.ai/v/RKLB/sec87/8) |
| Architecture | Two stages; **reusable first stage** returning to launch site / ocean platform; reusable fairing systems; second stage expended | FILED | DEMONSTRATED | [📄 RKLB 10-K p.8](https://agentii.ai/v/RKLB/sec87/8); [📄 RKLB 10-Q p.35](https://agentii.ai/v/RKLB/sec109/35) |
| ASP | **$50–55M** per launch, "no significant discounting for early launches" | DISCLOSED (earnings call, not a filing) | CLAIMED | [📄 RKLB Q2 2026 call p.3](https://agentii.ai/v/RKLB/ect21/3) |
| Flight status | **Has not flown.** Pad delivery targeted Q4 2026; ramp characterised by the issuer as "1, 3, 5" | FILED | DEMONSTRATED | [📄 RKLB 10-Q p.35](https://agentii.ai/v/RKLB/sec109/35); [📄 RKLB Q2 2026 call p.3](https://agentii.ai/v/RKLB/ect21/3) |
| Expendable-configuration payload | **Absent — no filed source** | REACHABLE-BUT-NOT-RECORDABLE | — | see §6 |
| Neutron cost per launch | Not disclosed | UNRESOLVABLE-FROM-PUBLIC-SOURCES | — | see §6 |

**Per-term declaration — FILED cell vs DERIVED cell.** This is the load-bearing discipline,
because a break-even whose terms are all derived is a tautology, not a falsifier.

| Term | Cell type | Grade |
|---|---|---|
| Neutron payload ~13,000 kg | **FILED** (narrative page text in two filings) | DEMONSTRATED |
| Neutron ASP $50–55M | **DISCLOSED, not filed** (call transcript only) | CLAIMED |
| Implied $/kg (ASP ÷ payload) | **DERIVED** — the division is ours | MODELED |
| Falcon 9 matched-pair denominators (87 t, 88 t, 132 t customer payload) | **FILED** | DEMONSTRATED |
| Falcon 9 matched-pair numerators ($648M, $490M, $978M Launch Services) | **FILED** | DEMONSTRATED |
| Falcon 9 matched-pair $/kg | **DERIVED** | DEMONSTRATED (figures) / MODELED (the division) |
| Falcon 9 `22.8 t` denominator (basis A and A′) | **NEITHER — not filed and not recordable** | CLAIMED, and see §6 |

**The test therefore mixes a filed term with a claimed one.** Under `P4`, a `MODELED` input can
never satisfy a falsifier; here the *numerator* is `CLAIMED`. The falsifier is evaluable but it
is not `DEMONSTRATED` on either side of the comparison, and the artifact is graded `MODELED`
accordingly.

## 3. The arithmetic

### 3.1 Neutron's implied price per kg

```
reusable config, LEO, 13,000 kg filed         [RKLB 10-Q p.34 / 10-K p.8]
ASP $50M  ÷ 13,000 kg = $3,846/kg             ASP $55M ÷ 13,000 kg = $4,231/kg
```
The band is **1.10× wide**, and its width comes from the ASP, not from any basis choice.

### 3.2 The withdrawn bar, and why it is withdrawn — two independent reasons, both carried

The old test was `> $2,939/kg`, equivalently a payload bar of **~3.1 t**.

1. **Denominator-failed.** `$2,939/kg` is `$67M ÷ 22.8 t`, and **`"22.8"` returns zero pages**
   in the SPCX 10-Q (verified this session: `search_keyword_in_source(sec8, "22.8")` → 0
   results). The **matched-pair** basis, on filed terms, is **$5,568–7,448/kg** — a **1.34×**
   band. Compare the band, not the point.
2. **A basis collapse inside its own definition.** `~3.1 t` is `$9.1M ÷ $2,939/kg` —
   **an Electron price over a Falcon 9 denominator.** `$9.1M` is RKLB's disclosed **revenue per
   launch** ([📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37)); `$2,939/kg` is
   Falcon 9 **basis A**. Two vehicles, two architectures, two denominator conventions, one
   ratio, **no basis field. That is DA-30 inside the falsifier written to catch DA-30.**

### 3.3 The equivalent bar, and whether the case closes or fires

Bar (payload required at Neutron's ASP to match a comparator) `= ASP ÷ comparator $/kg`:

| Comparator basis | Value ($/kg) | Bar @ $50M | Bar @ $55M | vs Neutron's filed 13.0 t |
|---|---:|---:|---:|---|
| Pool-wide: LS ÷ **all** mass to orbit, H1 2026 | $939 | 53.2 t | 58.6 t | **FIRES** |
| **Basis A, withdrawn** ($67M ÷ 22.8 t) | $2,939 | **17.0 t** | **18.7 t** | **FIRES** |
| Basis A′ ($962M ÷ 10 ÷ 22.8 t) | $4,219 | 11.9 t | **13.0 t** | **KNIFE-EDGE** |
| Matched pair, Q2 2025 ($490M ÷ 88 t) | $5,568 | 9.0 t | 9.9 t | closes |
| Matched pair, H1 2026 ($978M ÷ 132 t) | $7,409 | 6.7 t | 7.4 t | closes |
| Matched pair, Q2 2026 ($648M ÷ 87 t) | $7,448 | 6.7 t | 7.4 t | closes |
| Space rev. ÷ customer payload, H1 2026 | $11,977 | 4.2 t | 4.6 t | closes |

The registered test's threshold is `$5,567/kg` ⇒ its bar is **9.0–9.9 t**, comfortably below
13.0 t. **On the registered test the case closes.** On the withdrawn bar (17.0–18.7 t vs 13.0 t)
**it fires, and by a wide margin.**

**The A′ knife-edge, stated precisely** (this is the sharpest single number in the artifact):
at `$4,219/kg`, `$50M` needs **11,851 kg** (closes by 8.8%) and `$55M` needs **13,035 kg**
(**fires by 35 kg — 0.27%**). A 0.27% margin is far inside the noise of an unfiled 22.8 t
denominator. **Do not read this cell as a pass.**

### 3.4 The contingency that carries the may-fire outcome

The registered close compares Neutron's **capacity** $/kg against Falcon 9's **realized** $/kg.
Make it like-for-like by asking what Neutron's *realized* average payload would have to be for
the registered test to fire:

```
fires if realized payload < ASP ÷ $5,567/kg  →  $50M → 8,981 kg ; $55M → 9,880 kg
```

So: **if Neutron's average customer payload lands below ~9.0–9.9 t, PIL-4 fires on the
corrected test too.** Falcon 9's own filed realized average is **8,700 kg (Q2 2026)** and
**9,778 kg (Q2 2025)** — i.e. **38.2%–42.9% of its 22.8 t capacity**. For Neutron to clear the
bar it must fly at **69.2%–76.2% of its 13 t capacity** — a utilization roughly **1.8× the
comparator's own filed utilization.**

That is the honest statement of the case: **PIL-4 closes only if Neutron is sold, on average,
nearly twice as full as Falcon 9 has been.** Nothing in the filings supports assuming that, and
the issuer's own "1, 3, 5" ramp language points the other way. **The close is a capacity-
denominator artefact until the first flight produces a realized payload.**

## 4. The sensitivity — how the answer moves across DA-01 bases A / A′ / B / C

### 4.1 The comparator ladder, both axes named

Every line states basis **and** denominator convention. Values marked ✔ are mine, recomputed
this session from filed cells; values marked ⤶ are inherited from `plan.md` §F19 and
`001/artifacts/SPCX/…_unit-economics_methodology.md`.

| # | Basis | Denominator | Value ($/kg) | Numerator | Denominator | Grade |
|---|---|---|---:|---|---|---|
| L1 | Pool-wide | all mass to orbit, H1 2026 | **$939** ⤶ | FILED | FILED | DEMONSTRATED / MODELED |
| L2 | **A (withdrawn)** | capacity, 22.8 t | **$2,939** ⤶ | CLAIMED | **UNFILED** | CLAIMED |
| L3 | **A′** | capacity, 22.8 t | **$4,219** ⤶ | FILED | **UNFILED** | DEMONSTRATED / MODELED |
| L4 | **B** | capacity, 22.8 t | **$525–875** ⤶ | MODELED | **UNFILED** | MODELED |
| L5 | Matched pair | realized, 88 t (Q2 2025) | **$5,568** ✔ | FILED | FILED | DEMONSTRATED / MODELED |
| L6 | **C** | capacity, 22.8 t | **$6,596** ⤶ | FILED | **UNFILED** | DEMONSTRATED / MODELED |
| L7 | Matched pair | realized, 132 t (H1 2026) | **$7,409** ⤶ | FILED | FILED | DEMONSTRATED / MODELED |
| L8 | Matched pair | realized, 87 t (Q2 2026) | **$7,448** ✔ | FILED | FILED | DEMONSTRATED / MODELED |
| L9 | Space-revenue matched pair | realized, 132 t (H1 2026) | **$11,977** ⤶ | FILED | FILED | DEMONSTRATED / MODELED |

Recomputation notes, recorded rather than smoothed:
- **L5 = $5,568/kg, not the $5,567/kg in the correction note.** `$490M ÷ 88,000 kg =
  $5,568.18`. The 0.02% difference is rounding-level and does not move the 1.34× band
  (`7,448 ÷ 5,568 = 1.338`; `7,448 ÷ 5,567 = 1.338`). **The band statement survives the
  discrepancy; the quoted point does not reproduce exactly, and that is recorded.**
- **L2, L3, L4, L6 all share the unfiled `22.8 t`.** Four of nine lines — including all four
  basis letters — rest on a denominator that **no filed source carries**.

### 4.2 What the ladder says about the falsifier

**Spread: L1 → L9 = $939 → $11,977 = 12.8×, from one issuer's one filing set.** The spread is
not uncertainty; it is definition. The falsifier's threshold sits at **L2, the second-lowest
rung**, so the *withdrawn* test was the **easiest of the nine to fire** — and it fired. The
*corrected* threshold sits at **L5**, the **median rung**. **The correction did not make the
test more accurate; it made it more lenient.** That is the mechanism behind the flip from FIRES
to CLOSES, and it is stated here so the flip is not mistaken for Neutron improving.

### 4.3 The small-lift penalty restated — `003:PIL-1`'s matrix under the same sensitivity

`003:PIL-1` inherits **"Electron is 10.3× Falcon 9 per kg on basis A."** Recomputed on both
lines with filed cells:

| Comparison | Denomination | Ratio |
|---|---|---:|
| Electron A ($9.1M ÷ 300 kg = **$30,333/kg**) ÷ Falcon 9 basis A ($2,939/kg) | capacity ÷ capacity | **10.32×** — reproduces the inherited 10.3× |
| Electron A ÷ Falcon 9 matched pair ($5,568–7,448/kg) | capacity ÷ **realized** | **4.07×–5.45×** |
| Electron B ($4.4M ÷ 300 kg = **$14,667/kg**) ÷ Falcon 9 matched pair | capacity ÷ **realized** | **1.97×–2.63×** |

**The headline "10.3× small-lift penalty" is 4.1–5.5× on a filed denominator, and the
marginal-cost penalty (basis B) is 2.0–2.6×.** The inherited 10.3× is not wrong — it is
correct *on a capacity-vs-capacity comparison where one of the two capacities is unfiled*. The
mismatched lines are flagged as mismatched, not presented as the answer.

**The structural result, which is the real product of this sensitivity:**

> **There is no basis on which Falcon 9 and Neutron — or Falcon 9 and Electron — both carry a
> fully-filed denominator.** Falcon 9's capacity is unfiled; Electron's and Neutron's realized
> payloads are unfiled (Neutron's does not exist). Every like-for-like comparison therefore
> mixes one filed term with one claimed or unfiled term. **This is not a research shortfall to
> be closed by searching harder — it is a property of what the issuers file.**

### 4.4 Architecture substitution — F5b, not F5a, and the floor is not numerically testable

| Vehicle | Architecture (filed) | Tier | Binding term | Floor |
|---|---|---|---|---|
| Neutron | **partially reusable** — reusable first stage + reusable fairing, **second stage expended** | **F5b** | upper-stage manufacturing | soft — a manufacturing curve |
| Alpha (FLY) | **fully expendable** — no recovery described | **F5c** | whole-vehicle manufacturing | the **only** tier with a DEMONSTRATED price |
| Falcon 9 | partially reusable | F5b | upper-stage manufacturing | soft |
| Starship | fully reusable | F5a | propellant | hard, ~$46–92/kg @ 100 t |

The F5 tiers are **exhaustive** (`contracts/launch-cost-curve.yaml`, rule
`floor_architecture_consistency`). **Applying F5a's $46–92/kg propellant floor to Neutron is a
category error** — it would understate achievable price by an order of magnitude, and it is the
named failure mode `003:PIL-1` exists to prevent.

An **indicative** F5b floor for Neutron is computable but **cannot satisfy a falsifier**: an
expended upper stage at the inherited `$8–12M` ÷ 13,000 kg = **$615–923/kg**, against which
Neutron's ASP $/kg of $3,846–4,231 is **4.2–6.9×** — no floor breach. But the `$8–12M` is a
`MODELED` inherited input, so **this floor test is `UNEXERCISED`, not `PASSED`.** An unengaged
check is not a passed check. What the F5b result *does* say qualitatively: for a partially
reusable vehicle the binding cost is a **manufacturing** term, so Neutron's economics yield to
production learning — the constraint on `003:PIL-4` is **demand and cadence, not the floor**.
That is why a price-bar falsifier, not a cost-floor falsifier, is the right instrument here —
and why its denominator discipline is the whole test.

## 5. What would change the answer

Ranked by how much of the verdict each would move.

1. **One filed Neutron price.** The ASP is the only `CLAIMED` term in the numerator and it
   exists solely on a call transcript (§6). A filed contract value or customer filing converts
   `$3,846–4,231/kg` from `CLAIMED`-denominated to filed, and under `P4` that is the difference
   between a falsifier that can fire and one that cannot.
2. **A filed Falcon 9 payload capacity.** This is the single highest-leverage item: it is the
   denominator of **four of nine ladder rungs, including all four basis letters**, and it is
   currently **unfiled and unrecordable** (§6). Filling it turns the capacity convention from
   `CLAIMED` into a real comparator and would settle whether L2/L3/L6 are comparable at all.
3. **The first Neutron flight with a disclosed payload mass.** This creates the **realized**
   denominator, which is the only thing that makes the registered test like-for-like (§3.4).
   Until then the registered "close" is a capacity-denominator artefact.
4. **Neutron's disclosed cost per launch.** Would make basis B — the only basis the F5 floor
   tests — exist for this vehicle. Currently absent.
5. **A filed Neutron expendable-configuration payload.** The reusable config is filed; the
   expendable one is not. An expendable figure would raise the capacity denominator and
   *strengthen* the close; its absence means the scenario is run on the weaker configuration.
6. **An orbit-matched comparator.** The matched-pair denominators (L5, L7, L8) are **blended
   orbit** — SPCX defines mass to orbit as total payload deployed, including higher-energy
   missions that pay more per kg. This **overstates** the pure-LEO comparator, which means the
   registered threshold is **too lenient**, which means the close is weaker than it looks. This
   is a `DA-02` non-commensurability and it moves in the direction of **firing**.
7. **A filed Alpha payload mass to a named orbit** (FLY's file, §6) — would supply the third
   point the peer comparison in the `003:PIL-4` subscription implies but cannot currently
   reach.

## 6. Retrieval scope

**Read this session (all agentii-citable):**

| Source | Pages | What it supplied |
|---|---|---|
| RKLB 10-Q Q2 2026 (`sec109`) | 33, 34, 35, 37 | Neutron payload + architecture; per-launch metrics; segment table |
| RKLB 10-K FY2025 (`sec87`) | 8 | Neutron payload (annual-filing cross-check); Electron 300 kg |
| RKLB Q2 2026 earnings call (`ect21`) | 3, 5, 6, 7 | Neutron ASP $50–55M; "1, 3, 5" ramp; pre-flight full-price sales |
| SPCX 10-Q Q2 2026 (`sec8`) | 13, 35, 42 | Launch Services revenue; mass to orbit; customer launches |
| FLY 10-Q Q2 2026 (`sec21`) | 34, 35, 40 | Alpha payload class label; Launch revenue |

**Searches that returned ZERO — each is a result, not a gap:**

- `"22.8"` in SPCX 10-Q → **0 pages.** The basis-A denominator is **denominator-failed**;
  independently reproduced.
- `"ASP"` in RKLB 10-Q → **0 pages**; `"50 million"` in RKLB 10-K → 2 pages, neither
  figure-bearing for Neutron. **The Neutron ASP has no filed source.**
- `"expendable"` in RKLB 10-K → risk-factor page only; in FLY 10-Q → **0 pages.** No filed
  architecture label for either the Neutron expendable config or Alpha.
- `"payload capacity"` in SPCX 10-Q → 2 pages, both the key-metrics definitions of **mass to
  orbit** (a realized metric), not a vehicle capacity. **Falcon 9's capacity is not filed.**
- `list_xbrl_concepts("Payload")` → **0 concepts. `list_xbrl_concepts("Launch")` → 0
  concepts**, against 109 for `"Revenue"`. The platform's structured layer contains **no
  payload and no launch concept at all.** This is a determination about the concept inventory,
  not about my query: **any downstream thesis that reads XBRL for a payload denominator gets
  nothing, and cannot tell that from a failed search.**

**Dispositions, in three classes:**

- **FILED / DISCLOSED (recordable):** Neutron payload 13,000 kg; Neutron architecture;
  Electron 300 kg; every SPCX and FLY figure used above; RKLB's per-launch series. The
  Neutron ASP is **disclosed but not filed** — recordable via `ect21`, graded `CLAIMED`.
- **`REACHABLE-BUT-NOT-RECORDABLE`** — the datum is reachable, but the citation contract
  (§3 rule 7: only `agentii.ai` URLs are admissible) cannot record it, because no agentii
  source contains it:
  - **Falcon 9's 22.8 t LEO capacity** — the denominator of basis A, A′, B and C. Publicly
    published as a vehicle spec; absent from the filing and from the concept inventory.
  - **Neutron's expendable-configuration payload** — published spec, no filed source. The
    correction note's own wording ("still has no filed source") is confirmed, not assumed.
  - **Alpha's actual payload mass to a named orbit** — only the class label is filed.
  - **F5a's propellant mass and price inputs** — inherited as `CLAIMED`/market-price, still
    unfiled.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`:** Neutron's realized payload (no flight); Neutron's
  cost per launch; Neutron's expendable-config payload; **RKLB basis C — permanently
  unconstructible, with the filed reason**: *"Management does not regularly review either
  reporting segment's total assets or operating expenses… long-lived assets, facilities, and
  equipment are shared by each reporting segment"* ([📄 RKLB 10-Q p.33](https://agentii.ai/v/RKLB/sec109/33)).
  This is a **filing-cited structural absence**, not a research shortfall, and it means
  `003:PIL-1`'s "all three DA-01 bases" cannot be delivered at RKLB on basis C.
- **`UNRESOLVABLE-FROM-PLATFORM`:** any attempt to source a payload or launch denominator from
  the structured layer — the concepts do not exist (§6). `get_segment_data` and
  `data_freshness` are unusable per the inherited constraints and were **not used**; every
  figure above is read from page text.

**Cross-check that materialised.** RKLB's disclosed per-launch metrics do **not** reconcile to
the audited segment table, and the inherited `DA-25` gap reproduces exactly on Q2 2026:

```
disclosed:  $9.1M ÷ $4.4M          → 51.6% gross margin
audited:    $19,110k ÷ $44,586k    → 42.9% gross margin
```

The audited Launch Services segment is **$44,586k** for six missions
([📄 RKLB 10-Q p.33](https://agentii.ai/v/RKLB/sec109/33)); the disclosed metric × 6 is
**$54.6M**, i.e. **22.5% higher**. The difference is a **definitional artefact, not an error**:
the issuer defines revenue per launch as the average transaction price attributable to launch
performance obligations *in the period the launch occurs*, regardless of when revenue is
recognised. Recorded because it is the reason the `$9.1M` numerator cannot be treated as a
filed contract value — **which is exactly why the withdrawn bar's `$9.1M` was an Electron
price standing in a Neutron calculation.**

---

**Bottom line for the caller.** T027's Neutron arithmetic is rebuilt and it is not
one-directional: the implied `$3,846–4,231/kg` **fires** the withdrawn `$2,939/kg` bar
(equivalent bar **17.0–18.7 t**, far above Neutron's filed **13.0 t**) and **closes** on the
registered `$5,567–7,448/kg` band — but the close is a **capacity-vs-realized denominator
artefact** and is contingent on a utilization assumption ~1.8× more favourable than Falcon 9's
own filed performance. `003:PIL-4`'s architecture substitution is confirmed as **F5b, not
F5a** on filed text, and F5c covers Alpha. The decisive missing input is not Neutron's payload
— it is **Falcon 9's**, and it is `REACHABLE-BUT-NOT-RECORDABLE`.
