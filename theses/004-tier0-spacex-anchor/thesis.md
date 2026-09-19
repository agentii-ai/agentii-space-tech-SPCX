# Thesis: tier0-spacex-anchor

Living file. `spec.md` is the frozen specification; this file is updated as findings land.
Machine-readable frontmatter below is authoritative for the dispatcher.

```yaml
thesis_id: 004-tier0-spacex-anchor
constitution_pin: 1.5.0
    # Re-pinned at clarify round 2, 2026-09-19. Was 1.4.0 — one MINOR behind the ratified
    # constitution, and it excluded DA-29 (back-solved and opaque checks) and DA-30 (two
    # bases on one concept, collapsed without a basis field). DA-30 governs spec §1c's
    # component-identity rule, which is the same basis discipline on SPCX's segment tables.
    # A queued 1.5.0 -> 1.6.0 bump is registered below as an expiry trigger.
assumption_pin: "2"
created: 2026-09-18
as_of: 2026-09-18
status: active
wave: 1

claim: [TBD]
    # Populated from spec §1b once the round-2 body amendments A-1 … A-6 land. Recorded as
    # A-7 in spec.md's Clarify round 2. The claim is the SOTP, not the ecosystem framework:
    # round 2 placed the main line with 011 and fixed 004 as the programme's valuation layer.

pillars: []
    # See A-7. spec §1b carries six pillars (P1 separability, P2 Connectivity main line,
    # P3 AI admissibility, P4 Space standalone, P5 CAPITAL, P6 comparability boundaries).

known-open: []
    # Open items live in spec.md's Clarifications: Q-1 … Q-6, Q-8, Q-9, Q-10 carry provisional
    # readings. Q-7 was superseded and Q-11 closed at clarify round 2, 2026-09-19.

budget: {max_tasks: 40, max_retries_per_task: 2}
    # spec §4: the §3 matrix yields ~34 tasks across one member and five read-through names —
    # the narrowest universe in the program and the densest per name. If the budget must come
    # down, drop the Light rows first; never the Deep rows (they carry P1-P4), and never
    # recent-quarter or ratio-analysis (they are the delivery mechanism for V-2 and P5).

# Added at clarify round 2, 2026-09-19 — the deterministic scanner's single finding, plus
# three 004-specific triggers each naming a distinct way the anchor goes stale.
expiry_triggers:
  - earnings_release
      # The V-1 class of error: a 10-Q that restates the segment lines. V-1 itself was
      # resolved by 002 phase 1 only after an earlier artifact got it wrong.
  - constitution_bump
      # The queued 1.5.0 -> 1.6.0 (30 amendments: 3 PATCH, 27 MINOR, 0 MAJOR) marks all 42
      # artifacts stale. 004 was re-pinned to 1.5.0 in round 2 precisely so this is a bump it
      # saw coming rather than a version it had silently missed.
  - skill_version_mix
  - cursor_close  # ✅ FIRED 2026-08-14 — see below
      # ⚠️ THIS TRIGGER HAS ALREADY FIRED. Round 4 inverted its logic (the headline became
      # PRO-FORMA, so the close would MAKE the anchor real rather than invalidate it); the
      # implement pass then found the close had ALREADY HAPPENED, on 2026-08-14, per 8-K
      # 0001628280-26-056945 Item 2.01. Retained because the register should show a fired
      # trigger rather than quietly drop it. Cursor has been consolidated since that date.
      # ⚠️ REASON REVERSED at clarify round 4, 2026-09-19. The trigger STANDS but its logic
      # inverted: the headline basis is now PRO-FORMA, not pre-close (round 4 overrode the
      # round-0 provisional). So the close is no longer the event that INVALIDATES the anchor
      # — it is the event that MAKES IT REAL. Pre-close, Cursor's dilution was a sensitivity;
      # pro-forma, it is an input to P1, which is why V-5 moved from `warn` to `blocking`.
      # The trigger remains because the deal could still break: a terminated merger would
      # leave a pro-forma headline built on a consideration that no longer exists.
  - market_data_stage_regresses
      # ⚠️ REVISED at clarify round 3, 2026-09-19. This trigger read
      # `market_data_stage_advances` and HAS ALREADY FIRED — the stage advanced. Round 3
      # established a KEYLESS live feed (data-tools/market_data.py, source `nasdaq`) and
      # verified it serving SPCX at $152.71 (close 2026-09-18). The old rationale ("every
      # market-referenced figure is a dated print") is no longer true, so the trigger is
      # inverted: the risk is now that the feed STOPS, not that it starts. A regression to
      # `none`, or a source that refuses, dates the SOTP's discount measure back to the
      # constitution's ~$1.62T print.
  - issuer_discloses_orbital_compute_revenue
      # Would falsify A4's terrestrial/orbital boundary — the constitutional ceiling P3 is
      # built on. Also PROGRAM §0b's third falsifier for the main line.

depends_on:
  - 001-technology-baseline      # pin 1.2.0 — the artifacts this thesis values
  - 002-evidence-validation      # COMPLETE. 004 inherits its figures WITH THEIR BASIS
  - 003-launch-cost-curve-value-migration
      # ADDED at clarify round 2. PROGRAM §5 declared this edge ("SPCX sizes off the curve")
      # and 003's header asserted it supplies "the curve that 004 and 005 price off" — but
      # this spec did not carry it. 004 CONSUMES the curve matrix and the value-pool map and
      # never re-derives either.

informs: ["005", "006", "007", "008", "009", "011"]
    # QUOTED deliberately. Unquoted, YAML 1.1 resolves 005/006/007/011 as OCTAL integers
    # (-> 5, 6, 7, 9) while leaving 008 and 009 as strings, since invalid octal stays a
    # string. So a bare [005, ..., 011] silently loads as a mixed [5, 6, 7, '008', '009', 9].
    # 005-009 benchmark against the anchor. 006 and 009 are named explicitly at round 2:
    # 004 is the programme's ONLY valuation of SPCX's Connectivity and AI segments — SPCX is
    # in neither 006's universe nor 009's — so those two anchor rows are reusable references,
    # not 005-only.

market_data_stage: per_row
    # ⚠️ CORRECTED at clarify round 3, 2026-09-19. This read `none`, which was a declaration
    # and was WRONG — it contradicted the skill registry on two rows and pinned the primary
    # instrument at the one stage where it cannot obtain a price.
    #
    # Declared per §3 row (see spec §3a / §3b):
    #   late : sotp-valuation, reverse-dcf        <- the registry's own stage for both
    #   none : revenue-decomp, comps, competitive, risk, growth-strategy
    #   none : the nine skills consumed from 003 (003 ran them at `none`)
    #
    # Source, verified live 2026-09-19: data-tools/market_data.py, `nasdaq`, auth "none"
    # (keyless), SPCX $152.71 close 2026-09-18, 3,759 ms. live_snapshot.py already names
    # SPCX among its target tickers.
    #
    # Two price bases are published and the spread between them is a finding: the live quote
    # ($152.71) and the constitution's dated anchor (~$1.62T, struck against $135.00 in
    # 2026-06 — ~13.1% behind). Every market-referenced figure carries its basis, its stamp
    # and its source, or it is inadmissible.
    #
    # ⚠️ CORRECTED at plan time 2026-09-19 (spec A-15). Round 3 wrote "Q42 NOW BINDS:
    # entities.md must define a bars schema for the `late` rows" — that OVERSTATES it. Q42's
    # literal trigger is `market_data_stage: early`; 004 is `late` on two rows and `early` on
    # none, so the rule does not fire as written.
    #
    # What is actually required: a QUOTE/OBSERVATION schema — ticker, price, basis,
    # observed_at, retrieved_at, source, and the refusal envelope — for the two `late` rows.
    # That is a DIFFERENT schema from `early`'s OHLCV bars: a sotp-valuation run needs a price
    # at a timestamp, not a 250-day series. The registry has NO `late` example in this
    # workspace to copy — 001, 002 and 003 are all `none` — so 004 is the first and must
    # define it. entities.md carries it; see plan.md § "Q42".
```
