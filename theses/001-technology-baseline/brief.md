# Context Brief — 001 Technology Baseline (stage-0)

> Q3/Q18: the brief carries Tier-1 Block-A slices ONLY; downstream keeps Tier-2
> deep-read via `get_investment_case(depth=full)` (returns are equally `<ref:*>`
> framed). Q19 framing rules: closed tags same-name as open, `<` escaped inside
> blocks, tag set is a closed enum.

**corpus_version**: `UNPINNED` — no corpus-version endpoint is exposed by the
installed plugin, so retrieval is live rather than pinned to a snapshot. Recorded as a
known gap rather than a fabricated pin. Nearest available freshness markers:
`list_domains.meta.data_freshness` = 2026-08-26; coverage `meta.data_freshness` = 2027-04-12.

## Retrieval outcome — the corpus has no space content

**This is the brief's headline finding, and it is negative.** Three retrieval probes
were run:

| Probe | Query | Result |
|---|---|---|
| `search_investment_strategies` | "space satellite aerospace launch orbital" | **0 rows** |
| `search_investment_cases` | "space satellite launch rocket orbital" | **0 rows** |
| `retrieve_and_contextualize` (fundamental, `company_situation=technology_disruption`) | composite | Returned 5 cases and 5 strategies, **none space-related and none tagged `technology_disruption`** — the analogue filter did not match and fell through to a generic list (the Q18 cold-start fallback) |

Returned instead were biotech strategies (microbiome interventions, platform-IP
licensing, QALY arbitrage, psychedelic revaluation) and generic large-cap cases
(Petrobras, McDonald's, Microsoft, Thermo Fisher, MercadoLibre).

**Root cause, identified:** `list_domains` shows the registry holds 9 domains whose
`applicable_sectors` are `["med","tech","fin"]` only. **There is no industrial or
aerospace sector in the taxonomy.** Thirty of the 35 universe issuers file under
`industrial.*` — including SPCX itself. The knowledge base is structurally
med/tech/fin-centric and this thesis sits outside it.

**Consequence for the plan.** No sector analogue can be borrowed, and no fund-sourced
strategy maps onto launch economics or orbital thermal constraints. Phase 1–6 must
build the technology register from primary sources — SEC filings, XBRL facts, source
documents — with the P2 first-principles derivations doing the work that a sector
analogue would normally do. This raises the cost of the thesis and raises the value of
its output: the register will be original rather than a re-application.

## Reference blocks

No `<ref:strategy>`, `<ref:analogue_case>` or `<ref:technical_setup>` blocks are
emitted. Per Q19 the tag set is a closed enum and blocks must be drawn from retrieved
content; emitting placeholder blocks here would fabricate provenance. The absence is
the finding recorded above, not an omission.

Frameworks were queried and returned **0 rows** (`retrieve_and_contextualize`,
`modes=[frameworks]`), so the K-series analytical frameworks appear not to carry an
entry applicable to a physics-bounded industrial thesis either.

## Method selection (Q7 — one verdict per strategy candidate)

**No strategy candidates exist to select from.** Q7 requires a verdict per candidate
strategy; with zero space-domain strategies retrieved, the table is empty and the
verdict is recorded as **not-applicable-by-corpus-gap**, with the reason stated rather
than a fabricated adoption/rejection:

| strategy id | adopted/rejected | rationale |
|---|---|---|
| — | **N/A** | Zero space/aerospace strategies exist in the corpus. No candidate to adopt or reject. Method is therefore derived from the constitution (P2 first-principles gate, F1–F6) and from primary-source analysis, not from a retrieved strategy. |

**Implication for `reproduce.md`:** external review cannot reproduce this thesis's
method by retrieving a strategy. The reproducible unit is the constitution's F1–F6
derivations plus the cited filings, which is why `reproduce.md` pins the constitution
and the filing accession numbers rather than a strategy id.

## Retrieval keys used (Q18)

| key | value |
|---|---|
| mechanical prefilter | `applicable_sectors` ∋ industrial → **no match**; fell through |
| pillar FTS | "space satellite aerospace launch orbital" → **0 rows** |
| cold-start fallback | generic fundamental strategies (biotech-weighted) → **discarded as non-applicable** |

The cold-start fallback was deliberately **not** used to seed the method. Applying
biotech platform-licensing logic to launch economics would be a category error, and
using it would have made the brief look populated while being misleading.
