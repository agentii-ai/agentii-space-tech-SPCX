---
thesis_id: "004-tier0-spacex-anchor"
constitution_pin: "1.5.0"
assumption_pin: "2"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
market_data_stage: per_row
---

# Entities and metric map — 004

Two schemas and one register:
1. **`entity_claims`** — the claim shape every artifact uses.
2. **`quote_observation`** — **NEW, and 004 is the first thesis in this workspace to define it.**
3. The **entity/metric map** — which entity carries which metric, with its DA exposure.

---

## 1. `entity_claims` schema

```yaml
entity_claims:
  - claim_id: <str>              # stable, content-derived
    ticker: <str>                # MUST be a §2 universe member or a §2 read-through
    metric: <str>                # snake_case, from the metric map below
    value: <number | str>
    unit: <str>                  # ALWAYS in-line; a bare number is inadmissible
    basis: <str>                 # ALWAYS in-line — see the basis rule below
    period: <str>                # ⚠️ FORMAT IS EXACTLY `YYYYQN` — e.g. "2026Q2". NOTHING ELSE.
                                 # ⚠️ TWO DEFECTS WERE FOUND HERE, AND BOTH SILENTLY DISABLE A LIVE CHECK.
                                 # (1) THE FIELD NAME. g1_gate reads `claim.get("period")`. 004's first
                                 #     draft called it `period_basis`, so the lookup returned None —
                                 #     falsy — and LOOKAHEAD_VIOLATION skipped. 001 and 003 use `period`.
                                 # (2) THE FORMAT. `g1_gate._PERIOD_RE` is `^(\d{4})Q([1-4])$`. A
                                 #     descriptive string like "6M (six months ended 2026-06-30)" fails
                                 #     the match, `_quarter_end()` returns None, and the check skips
                                 #     AGAIN — even with the right field name.
                                 # ⚠️ AND THE CHECK HAS NEVER RUN IN THIS WORKSPACE: measured
                                 #     2026-09-19, ZERO artifacts across 001, 002 and 003 carry
                                 #     `entity_claims` at all. It is the DA-29 class — a check that
                                 #     closes cleanly while testing nothing. 004 is the first thesis
                                 #     where it is live.
                                 # HOW TO KEEP DA-26 DISCIPLINE: the duration label (3M vs 6M) moves
                                 # into `basis`, which is free text. A bare "2026Q2" cannot say which
                                 # duration it is, and the 10-Q files BOTH under one concept — so
                                 # `basis` must carry "3M … quarter ended" or "6M … six months ended"
                                 # on every claim. First applied in
                                 # `artifacts/SPCX/2026-09-19_revenue-decomp_methodology.md`.
    evidence_grade: DEMONSTRATED | MODELED | CLAIMED | DERIVED
    source: <str>                # 10-Q p.N / 8-K date / 003 artifact path
    citation: <str>              # agentii.ai/v/{ticker}/{citation_id}/{page}
    consumed_from: <str|null>    # 003 artifact path when NOT re-derived
    dimensions: <map|null>       # XBRL axes, when the fact is dimensional
```

**The basis rule (from 002's programme-level result).** *"A downstream thesis citing 002's
validated set must carry **the basis as well as the grade**."* SPCX `operating_margin` reproduces
exactly on two bases differing by **46.47pp** — filed **−16.68%** vs platform-served **+29.79%**.
**A claim whose `basis` is null is inadmissible**, and `check_contract.py`'s `basis_named` rule is
`warn`-only, so this is a discipline rather than a gate.

---

## 2. `quote_observation` schema — the Q42 instrument

> ### ⚠️ Why this schema exists and why it is NOT the bars schema
>
> **Q42's literal rule:** *"Technical (`market_data_stage: early`) theses MUST emit the entities.md
> bars schema — without it, `implement` refuses."*
>
> **004 is `late` on two rows and `early` on none, so the rule does not fire as written.** A
> round-3 note in `thesis.md` claimed *"Q42 NOW BINDS"*; **that overstates it and is corrected
> (spec A-15).**
>
> **What 004 actually needs is a different instrument.** An `early` thesis reads a 250-day OHLCV
> *series* to compute technical levels. A `late` thesis reads **a price at a timestamp** to compute
> a multiple. **A bars schema would be the wrong shape — it would carry 250 observations where one
> is needed, and omit the fields the one actually requires** (`basis`, `source`, and the refusal
> envelope).
>
> **This workspace has no `late` example to copy.** 001, 002 and 003 are all `none`. **004 defines
> it, and 011 — which sizes positions off live prices — will be the next consumer.**

```yaml
quote_observation:
  ticker: <str>
  price: <float>
  price_basis: close | intraday | previous_close
  currency: <str>                     # "USD"
  observed_at: <ISO 8601>             # the MARKET's time for this price
  retrieved_at: <ISO 8601>            # OUR fetch time — Q71: the two are never conflated
  source: <str>                       # "nasdaq" | "yfinance" | ...
  data_class: <str>                   # "fast" | "delayed"
  latency_ms: <int>
  cache_hit: <bool>
  rate_limit_remaining: <int|null>

  # --- the refusal envelope, carried WITH EQUAL FIDELITY ---
  status: ok | refused | unavailable
  error: <str|null>

  # --- the identity of the WORKSPACE reference this observation is compared against ---
  dated_reference:
    label: <str>                      # "constitution ~$1.62T anchor"
    price: <float>                    # 135.00
    as_of: <date>                     # 2026-06
    grade: CLAIMED
```

**Three rules this schema enforces, each from a round-3/4 finding:**

1. **`observed_at` and `retrieved_at` are separate fields.** SPCX's verified observation is
   **$152.71 with `observed_at` 2026-09-18** and `retrieved_at` 2026-09-19 — *a day apart.*
   Conflating them would date the anchor to the fetch.
2. **A refusal is recorded, not omitted.** `live_snapshot.py`'s own design principle: *"when the
   provider is rate-limited or blocked, **the absence is the finding**, and a success-only harness
   would hide it."* **`status: refused` with a populated `error` is a valid, publishable
   observation.**
3. **The dated reference travels with the observation.** Round 4's answer was *"both — live and
   dated, with the spread reported"*, so an observation that does not name the reference it is
   measured against cannot compute the spread. **At $152.71 against $135.00 the spread is
   +13.1%, and it is a named component of the discount decomposition, not a conglomerate
   discount.**

**Fetch route (verified live 2026-09-19):**
```bash
cd /Users/frank/A/agenzym/agentii-investment-intelligence/data-tools
python3 market_data.py --ticker SPCX --json      # ← get_quote — the ALLOWED half
```
`_sources.py` registers `nasdaq` as `auth: "none"` (keyless).

> ### 🔴 WHEN THIS MAY BE CALLED — a platform rule 004 is the first thesis to face
>
> `data-tools/refusal.py` implements **`PRICE_ACCESS_PREMATURE`**, which
> `contracts/taxonomy.yaml` describes as *"**plan-declared** (Q41 late-mode early-quote
> refusal)"*:
>
> ```python
> if stage == "late" and tool == "get_price_history":
>     return refuse("PRICE_ACCESS_PREMATURE",
>         "price is the FINAL CHECK for fundamental work, never the raw material")
> ```
>
> | Tool | `late` stage | Note |
> |---|---|---|
> | `market_data.get_quote` | ✅ **allowed — at the END only** | This is the fetch route above |
> | `market_data.get_price_history` | ❌ **REFUSED at any time** | The 250-day series is an `early` instrument. A fundamental thesis never uses it |
>
> **⚠️ `live_snapshot.py` calls BOTH** (`get_quote` line 99, `get_price_history` line 100), so
> **it must not be pointed at a `late` thesis's early phases** — its second call trips the refusal.
>
> **Consequence for this thesis's plan:** the price is captured at **Phase 7 (T700)**, adjacent
> to `sotp-valuation` — **not at Phase 0.** An earlier draft of the plan had it at Phase 0, which
> is precisely the forbidden pattern (*price as raw material*). **The schema above is unchanged;
> only its timing was wrong.**
>
> **001, 002 and 003 are all `market_data_stage: none`, so no thesis in this workspace has ever
> exercised this rule. 004 is the first, and 011 — which sizes positions — is the next.**

**Other tools:** **`get_segment_data` is NOT usable** — see the DA register below.

---

## 3. Entity / metric map

**Universe member: one.** Read-through names supply benchmark inputs and receive no artifacts.

| Ticker | Role | Metrics it carries | DA exposure |
|---|---|---|---|
| **SPCX** | **Universe member — the whole thesis** | `segment_revenue`, `segment_operating_income`, `segment_gross_margin`, `cohort_revenue` (consumer / enterprise & government), `subscriber_count`, `arpu`, `mass_to_orbit`, `launch_count`, `internal_launch_share`, `coverage_ratio`, `customer_concentration` | **DA-06** (captive-integrated — **no transaction price**), **DA-08** (customer vs internal launches), **DA-10** (ARPU service-line definition), **DA-11** (IT load vs facility draw), **DA-19** (common-control recast), **DA-21** (segment boundaries), **DA-23** (sign), **DA-29/DA-30** |
| MSFT | Read-through — AI framing set | `capex`, `intelligent_cloud_revenue`, `compute_capacity` | DA-21 (**compute is a cost centre, not a segment**) |
| GOOG | Read-through — AI framing + orbital-compute disclosure | `capex`, `google_cloud_revenue`, `Project Suncatcher` disclosure | DA-21. **Query as `GOOG`, never `GOOGL`** |
| NVDA | Read-through — the silicon leg | `data_center_revenue` | **DA-21: NVDA is the supplier, not the operator** — the read-through is to *feasibility*, never to a multiple |
| VRT | Read-through — thermal comparator | `revenue`, `operating_margin` | Supplies the **DA-11 restatement context that 002 owns** — consumed, never re-derived |
| IRDM | Read-through — profitable-constellation benchmark | `revenue`, `operating_margin`, `subscriber_count` | **P11 deal security** — price is a **spread**. **A live multiple on a spread is no more admissible than a stale one** (round 4) |
| GSAT | Read-through — via `comps` only | `revenue`, `operating_margin` | **P11 deal security**; 64% one customer |
| RKLB, FLY, SATS, ASTS, VSAT | Read-through — via `comps` only | comp multiples | **P11** (RKLB, GSAT); **DA-24 contaminated** (SATS); **`PARTIAL` coverage** (ASTS, VSAT) |

**Load-bearing absences, named rather than proxied:** BA (Spectrolab) is outside this universe and
belongs to 007/008; BWXT is F2's nuclear escape hatch and belongs to 002.

---

## 4. The DA register and the two class distinctions

| DA | Instance in this thesis | Handling |
|---|---|---|
| **DA-06** | **Space is `captive_integrated`** — a vertically integrated operator flying its own payloads has **no transaction price**. 003: *"comparing a price to a non-price."* | **Round 4: carry as a stated limitation per P6's partition rule.** No external multiple borrowed; Space's value comes from segment contribution |
| **DA-08** | 27 of 37 Falcon launches internal; ~74% produce no Space revenue **by design** | The inter-segment transfer is **stated as a limitation in the SOTP**, never netted silently |
| **DA-10** | ARPU is **subscriber service revenue only** — excludes enterprise, government, aviation, maritime | All four readings reported side by side; **managed-channel subscribers/ARPU are `UNRESOLVABLE-FROM-PUBLIC-SOURCES`**, so price erosion cannot be fully separated from mix shift |
| **DA-11** | The 1.4 GW is **IT load only**, excluding cooling, distribution losses, lighting, security, overhead | **002 owns the PUE restatement.** Consumed here, never re-derived. **It is a capacity figure, not a revenue or earnings figure** |
| **DA-19** | xAI merged 2026-02-02 under common control; **Customer B has no 2025 comparative** | Growth rates across the boundary mix real growth with entity change. **Only Space's series survives** |
| **DA-21** | AI aggregates **Grok, X (advertising) and compute** — three businesses | The homogeneity test is **P1's** and **P3's** |
| **DA-23** | Consolidated operating result is **$(143)M**, while the platform serves `+143,000,000` | **Component identity in-line on every segment table.** `EPS × shares` is **inadmissible** as a sign test |
| **DA-29** | New at 1.5.0 — back-solved checks (the mechanical circularity test) | Any reconciliation term appearing **nowhere in the source** is a back-solve |
| **DA-30** | New at 1.5.0 — two bases on one concept collapsed without a basis field | **Three instances at SPCX**: segment vs consolidated gross margin (65.80% vs 55.27%); Customer A's two bases (H1 falls, Q2 rises); the platform's two `operating_margin` bases (46.47pp apart) |

### Two disposition classes, never collapsed

| Class | Meaning | Remedy |
|---|---|---|
| `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | The disclosure does not exist anywhere | A **named external source** that would resolve it |
| `UNRESOLVABLE-FROM-PLATFORM` | The disclosure exists; the platform cannot reach it | A **read route or a tool fix** |

**`NON-FORMABLE` is not `PASS`** (003's F16). A falsifier whose inputs do not exist is recorded,
never marked passing.

---

## 5. Tool register — what works and what does not

| Tool | Status | Route |
|---|---|---|
| `search_xbrl_facts(…, view=detailed)` | ✅ **works** — returns dimensional axes | **The route for all segment/customer facts.** 286 SPCX facts FY2026 |
| `search_documents` | ✅ works | Source discovery; the Cursor 8-K (2026-08-14) was found this way |
| `market_data.py --ticker SPCX` | ✅ **works, keyless** | The `late` rows' price source. **Verified $152.71** |
| **`get_segment_data`** | ❌ **BROKEN** — `column "k" does not exist` at SPCX | **003's F4 recorded this first** (from 002 §7), with a fuller diagnosis: *"elsewhere reports a `total_revenue` summing served facts across two years and two durations with no de-duplication — `segment_coverage_pct 116.2` masking a 302.1% overlap. 002's verdict: 'Treat its output as unusable.'"* **Use `search_xbrl_facts` instead.** 008 and 009 are the likely next callers |
| `list_sources(year=2026, source_type=sec_filing)` | ⚠️ returned **empty** for SPCX | Recorded so a future reader does not mistake the empty result for *"no filings exist"* — the filings are there and reachable by other routes |
