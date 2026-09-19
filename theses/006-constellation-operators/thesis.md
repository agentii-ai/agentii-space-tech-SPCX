# Thesis: tier2 connectivity spectrum

Living file. `spec.md` is the frozen specification; this file is updated as findings land.
Machine-readable frontmatter below is authoritative for the dispatcher.

```yaml
thesis_id: 006-constellation-operators
tier: Tier 2 — Constellation Operators: Connectivity, Spectrum & Geospatial
constitution_pin: 1.6.0
constitution_pin_at_specification: 1.4.0
pin_note: >
  Specified at 1.4.0; re-pinned to 1.6.0 at the post-004 re-specification. The 1.6.0
  amendment was NORMATIVE, not cosmetic: it re-cut §Universe Definition to a single axis
  (function in the value chain) with an explicit membership test and a cross-tier
  dependency rule, corrected the DA-26 census, redefined the PARTIAL readiness class, and
  registered that the DA-23 sign strip is ENDPOINT-SPECIFIC (search_xbrl_facts strips;
  get_statement preserves). This thesis has no artifacts yet, so nothing is grandfathered
  at 1.4.0; the second pin records where it was SPECIFIED.
claim: >
  The licence is durable and the business on top of it is not, and the IRDM margin decay is decomposable by line
pillars:
  - The licence is durable and the business on top of it is not, and the IRDM margin decay is decomposable by line
  - The licensed asset and the operating business price separately, and the licence is the majority of the value — **where the licence is scarce**
  - The D2D transition compresses the service layer while raising the value of the licensed layer, and every Tier 2 name is placeable on one side
  - The deal gate chain is a dated checklist per name, and a break is re-underwritten from scratch
  - Every Tier 2 contested figure converts to `DEMONSTRATED` or is recorded as unresolvable
  - The sector book: every investable name carries a strategy, an entry condition and a dated catalyst — or is recorded as having none
known-open: []
# Q58. Raised 60 -> 180 at the 2026-09-20 clarify round (spec Q-17), aligning 006 with 005.
# The scope expansion was OWNER-DIRECTED (Q-15: the sector book, the strategy set, the
# structural analogues, three new matrix rows), and 005's governing reasoning transfers
# verbatim: a budget that silently truncates an owner-directed scope is the failure mode the
# budget exists to prevent. The Q-12 answer ("keep 60, prune Standard and Light") was correct
# on its premise -- an unchanged scope -- and Q-15 voided that premise.
budget: {max_tasks: 180, max_retries_per_task: 2}
# Q59. Declared at the 2026-09-20 clarify round (spec Q-13). Six, at the finest granularity,
# because each names a distinct datum that would move a verdict -- and two of them name events
# that may never occur, which is why they are triggers and not assumptions.
expiry_triggers:
  - deal_close_or_break                # IRDM/RKLB or GSAT/AMZN closing or terminating; both are
                                       # P11, and on a break the standalone case is NOT the
                                       # pre-merger case
  - sats_spectrum_agreement_completion # EchoStar's two pending agreements; moves P2's
                                       # sell-side basis AND the ~$19.6B mark
  - next_quarter_filing                # DA-26 / DA-23 / duration defects re-verified against
                                       # each new filing set; P1-P3 are quarter-bound
  - constitution_bump                  # the 1.6.0 pin expires
  - spir_coverage_arrival              # P2's granted-licence control moves from three names
                                       # to four
  - asts_first_filed_service_revenue   # the trigger for P4's primary-grant proxy test -- the
                                       # only evaluable route to PIL-6's falsifier
```
