# Context Brief — 002 Evidence Validation (stage-0)

> Q3/Q18: the brief carries Tier-1 Block-A slices ONLY; downstream keeps Tier-2 deep-read
> via `get_investment_case(depth=full)`. Q19 framing rules: closed tags same-name as open,
> `<` escaped inside blocks, tag set is a closed enum.

**corpus_version**: `UNPINNED` — no corpus-version endpoint is exposed by the installed
plugin, so retrieval is live rather than pinned to a snapshot. Recorded as a known gap
rather than a fabricated pin. Nearest available freshness markers:
`list_domains.meta.data_freshness` = **2026-08-26**; `list_sources.meta.data_freshness`
= **2027-04-12**.

## Retrieval outcome — the corpus gap, re-verified and corrected

001's brief recorded that the knowledge corpus has no space content. **This thesis
re-verified that finding and it holds — with one correction and one distinction that
matters for 002 specifically.**

**Verified absent.** `search_investment_strategies` on space keywords → **0 rows**.
`search_investment_cases` on space keywords → **0 rows**. `search_investment_strategies`
filtered `sectors=aerospace_defense` → **0 rows**. `list_domains` returns **9 domains
whose `applicable_sectors` are `["med","tech","fin"]` only** — **there is no industrial or
aerospace domain in the registry at all.**

**Root cause, and why it is not a temporary gap:** 30 of the 35 universe issuers file
under `industrial.*`, including SPCX itself. The knowledge base is structurally
med/tech/fin-centric.

**The distinction that matters here:** the sector filter is a dead end **by
construction** — any sector-keyed query returns zero rows, and **reporting that emptiness
as "no analogues exist" is a false negative.** It is a fact about the registry, not about
the world. This is recorded so no artifact in this thesis repeats the error.

**Correction to 001's framing.** The corpus does carry cases on **two names already in
this workspace's universe**, filed under `Industrials` rather than a space tag:
**Moog (`MOG-A`)** — Brown Advisory, **~2.1–2.5× on cost, ~110–150% total return over ~3
years, IRR ~28–38%** — and **EnerSys (`ENS`)**. **Both are `NOT_READY` on issuer
coverage.** A case that cannot be validated against filings, and coverage that would not
surface the manager's reasoning: **neither alone is sufficient.**

## Why this thesis does not attempt strategy or analogue retrieval at all

**This is a deliberate scope decision, not an omission.** Thesis 002 validates *figures
against filings* — it is an evidence-audit, not a thesis-generation exercise. Its inputs
are SEC filings, XBRL facts and source documents; a borrowed strategy analogue would
contribute nothing to a question of the form *"does $14,667/kg survive a corrected
denominator?"*

**Consequence for the Q7 method-selection table:** it is recorded as
**not-applicable-by-scope**, with the reason stated, rather than filled with a
cold-start fallback. Populating it would make the brief look complete while being
irrelevant — the same judgement 001 made, for a stronger reason: 001 at least *asked* a
sector question; 002 asks a numerical one.

| strategy id | adopted/rejected | rationale |
|---|---|---|
| — | **N/A** | Zero space/aerospace strategies exist in the corpus, **and none is relevant to this thesis's question**. Method derives from the constitution (P4, the Data-Integrity Register) and from primary-source verification, not from a retrieved strategy. |

**Where the analogous retrieval DOES happen:** 011, whose method is retrieval by
*structural situation* rather than sector tag. That work is not duplicated here.

## Reference blocks

No `<ref:strategy>`, `<ref:analogue_case>` or `<ref:technical_setup>` blocks are emitted.
Per Q19 the tag set is a closed enum and blocks must be drawn from retrieved content;
emitting placeholder blocks would fabricate provenance. The absence is recorded above.

## Retrieval keys used (Q18)

| key | value |
|---|---|
| mechanical prefilter | `applicable_sectors` ∋ industrial → **no match**; fell through |
| pillar FTS | "space satellite aerospace launch orbital" → **0 rows** |
| cold-start fallback | **deliberately not used** — a biotech or generic large-cap analogue cannot inform a denominator audit |

## What replaces retrieval in this thesis

Four instruments, all primary-source, none of them retrieval:

1. **`validate_calculation` / `get_calculation_tree`** — the automated component identity
   that DA-23's remedy requires. Delivers Pillar 3 across all 17 names.
2. **`search_keyword_in_source`** → page numbers, then **`read_source_pages`** → the page.
   This is the citation instrument added at clarify round 3 (spec §1d), and it **worked
   at specification**: four inherited Connectivity figures were confirmed at source and
   DA-10 was resolved as a side effect.
3. **`search_sec_filings`** — resolves `citation_id` for the URL the citation requirement
   demands (`sec8` for SPCX, `sec109` for RKLB, `sec9` for YSS's Q1 anomaly).
4. **`get_company_financials` metrics** — the *contaminated* surface. Every figure taken
   from it is re-derived from components before use, per the register.

> **The brief's headline finding for 002 is therefore inverted from 001's.** 001 found
> that the corpus could not help and that primary sources had to carry the work. 002
> **does not want the corpus** — a borrowed analogue would be a category error in an
> evidence audit. Primary sources are not the fallback here; they are the method.
