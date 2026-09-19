# Context Brief — 003 Launch Cost Curve & Value Migration (stage-0)

> Q3/Q18: Tier-1 Block-A slices ONLY. Downstream keeps Tier-2 deep-read via
> `get_investment_case(depth=full)`. Q19 framing: closed tags same-name as open, `<`
> escaped inside blocks, tag set is a closed enum.

**corpus_version**: `agentii-2026-09-18` · **as_of**: 2026-09-18 · **constitution_pin**: `1.5.0`

---

## Retrieval record — what the knowledge layer does and does not carry

Recorded before the reference blocks, because it bounds what they can be.

| Store | Query | Result |
|---|---|---|
| `search_investment_strategies` | *"cost curve arbitrage disruptive technology incumbent parity"* | **empty** — the query was too specific |
| `search_investment_strategies` | *"space"* | **20 rows, 1 page** — mostly med/fin; two relevant (below) |
| `search_investment_cases` | *"cost curve decline solar semiconductor platform monetisation licensing"* | **empty** |
| `search_investment_cases` | *"space launch"* | **8 rows** — **Baillie Gifford/SpaceX directly relevant** |
| `search_knowledge_entries` | (unfiltered) | **empty** |
| `search_by_analogue` | `market_regime="sector rotation"` | **empty** |
| `search_technical_setups` | (unfiltered) | **34 pages** — populated, but **entirely options/trading execution**; 003 produces no trades, so this store is not usable here |
| `list_domains` | — | **9 domains; every `applicable_sectors` ⊆ {med, tech, fin}** |

> **⚠️ The registry has no industrial, aerospace or defence domain.** Every sector-keyed
> query for this thesis fails **by construction**, not by absence of content. PROGRAM.md §4
> records the same finding and routes Part C to situation-shape retrieval. **The store is
> not empty — the index is.** The two blocks below were reached by keyword, not by sector.

---

## Reference blocks

<ref:analogue_case id="ic_baillie_gifford_spacex_investment_2019_2020" entity="SPCX" period="2019-2020" as_of="2026-09-18" retrieved_at="2026-09-18">
Baillie Gifford entered SpaceX at an estimated **$30–40B** valuation; secondary-market marks
exceeded **$200B** by 2024 — a 5–7× paper multiple, with the position reaching **17.9% of
Edinburgh Worldwide**. The stated thesis: SpaceX builds *infrastructure* rather than selling
a product, reusable rockets cut cost to orbit **~98%**, and Starlink is a monopoly-like
global broadband business. **Its own `wrong_if` is the standing test**: *"Starlink fails to
achieve profitable scale; Starship development stalls; or the 'infrastructure' thesis proves
to be a capital-intensive trap with no path to monopoly-like returns."* The recorded bear
case names competition from terrestrial 5G and other LEO constellations, a cyclical and
**commoditised launch market**, and key-man risk. `what_went_wrong` concedes the entry
multiple priced cash flows that "were not yet backed by mature businesses", and that
post-COVID liquidity "likely inflated private market multiples **before fundamental proof was
fully in place**."

**Why it is load-bearing for 003.** Two of this case's own failure conditions are now
**partially observable in filed data**, and 001/002 measured both: Starship development is
consuming **$1,076M per quarter, 111.9% of Space segment revenue**, and the Space segment
**fell 1.9% across H1 2026** while consolidated revenue rose 53.7%. The case therefore
arrives not as an analogue to admire but as **a falsifier with a scoreboard**.
</ref:analogue_case>

<ref:strategy id="ark_invest__wrights_law_valuation_framework" fund="ARK Invest" era="enduring" as_of="2026-09-18">
A cost-curve valuation method built on **Wright's Law** — unit cost falls by a fixed
percentage per cumulative production doubling. Named learning rates: batteries **20%**,
solar **28%**, DNA sequencing **~50%**, AI compute **60%+**. Adoption criteria are strict:
a documented learning rate *"sustained for ≥5 cumulative production doublings"*, a TAM that
expands at the cost-curve endpoint, and sub-20% S-curve penetration. **Red flags are equally
specific**: *"learning rate decay below 10–15%, demand saturation stalling the S-curve, or
substitution by a new technology with a steeper learning curve."* Risk is managed through
**thesis validation rather than stops**: *"If a learning rate falls below the model's
predicted bound for two consecutive doublings, the position is reduced by ~1/3."*

**Why it is load-bearing for 003.** It supplies the test P3 has been missing. P3 asserts the
curve is `CLAIMED`, not `DEMONSTRATED`; Wright's Law says precisely what would make it a
curve — **a learning rate measured over ≥5 doublings**. Rocket Lab's Electron is the
universe's only measured point. **One point is not a learning rate, and one quarter is not a
doubling**, so 003 can state P3's finding as a *definitional* result rather than an
evidential shortfall: **launch does not currently qualify as a Wright's Law technology, and
the reason is structural, not disclosure-lazy.**
</ref:strategy>

---

## Method selection (Q7 — one verdict per strategy candidate)

| strategy id | adopted/rejected | rationale |
|---|---|---|
| `ark_invest__wrights_law_valuation_framework` | **ADOPTED — as an evaluative frame for P1/P3, not as a valuation model** | 003 produces no prices and no positions, so ARK's sizing and exit rules do not transfer. What transfers is the **admissibility test**: ≥5 doublings, documented rate, stated decay bound. 003 applies it to the curve and reports which vehicles survive it. |
| `baillie_gifford__big_picture_thematic_scenario` | **ADOPTED — as the P2 value-migration frame** | The "platform over product" judgment is exactly P2's claim (value migrated to the integrator owning demand, not the launcher). 003 tests it against segment data rather than adopting it. |
| `steve_eisman__ignored_unloved_sector_specialization` | **REJECTED** | Structurally appealing — space is under-followed — but 003's universe is deliberately nine names chosen for curve contribution, not for neglect. Applying this would re-open the universe §2 closes. Logged as a candidate for 011. |
| `gmo__disruptive_technology` | **REJECTED** | Requires recurring-revenue and valuation-discipline tests 003 cannot run: no prices (`market_data_stage: none`), and the curve is a cost series, not a revenue one. |
| (no case for the exclusion tier) | **NOT RETRIEVED** | PROGRAM.md §4 names a Cross-Listed Biotech analogue for Eutelsat/Avio/Astroscale. **No sector case exists for that tier on the platform** — recorded as a gap, not proxied. |

---

## Framed blocks carried into the spec

<ref:regime as_of="2026-09-18">
**Macro, per spec §5.** The curve is a cost series and largely price-independent; the
**value-pool map is not**. The demand side funds cadence from capital markets and the long
end sits at **three-year highs with hike risk priced**. The honest reading is that the
demand side's ability to absorb the curve is **constrained** — carried as a **P6 input, not
an opinion**.
</ref:regime>

<ref:constitution_f5 as_of="2026-09-18">
**F5 is split THREE ways and the tiers are EXHAUSTIVE.** F5a (fully reusable — propellant
floor, hard), F5b (partially reusable — upper-stage manufacturing floor, soft), **F5c (fully
expendable — whole-vehicle manufacturing floor, and *"the only architecture with a
`DEMONSTRATED` price"*)**. F5c was *"added at v1.3.0, completing the split."*

**⚠️ Corrected 2026-09-18.** An earlier version of this block recorded "F5a/F5b do not reach
Electron and Alpha" as an **open amendment candidate**. **That was wrong** — the gap was
closed at v1.3.0, five minor versions below 003's pin, and re-raising it was 003's own
instance of the A29 defect (a correction that exists and is not read).

**The real finding, and it is stronger than the one it replaces.** The constitution registers
an **inversion**, not a gap: the sector's cost conversation is conducted about the
architectures whose floor is **unproven** (F5a/F5b — no `DEMONSTRATED` price on either),
while the architecture with the only **demonstrated** price is **F5c**, which F5 as
originally written did not bound at all. **003's P3 should state it this way**: the curve is
`CLAIMED` where it is discussed and `DEMONSTRATED` where it is not.
</ref:constitution_f5>
