#!/usr/bin/env bash
# archive_session.sh — copy a Claude Code session's context into a thesis's session-history/.
#
# WHY. The raw session record (transcript, subagent conversations, tool-call spill files,
# file-edit history) lives under ~/.claude/, OUTSIDE the repository and subject to cleanup.
# It is the only record of HOW each figure was arrived at. Theses 002 and 003 already carry
# archives; this makes the procedure repeatable rather than a one-shot.
#
# WHY RE-RUNNABLE. A live session is appended to while it is being copied, so any archive is a
# byte-exact PREFIX of the source at copy time. 002's MANIFEST says to "re-run the copy after
# the window closes" — this is that procedure. rsync -a overwrites with a longer prefix and
# never truncates, so re-running is safe and idempotent.
#
# USAGE:
#   tools/archive_session.sh                         # current session, thesis 004
#   tools/archive_session.sh <session-uuid> <thesis-dir>
#
# EXIT: 0 on success. Non-zero if the transcript is missing — a silent empty archive is worse
# than a loud failure.

set -uo pipefail

SESSION_ID="${1:-0ce27f1c-f394-4d1e-97e2-4b9770e6a11b}"
THESIS_DIR="${2:-theses/004-tier0-spacex-anchor}"

CLAUDE="$HOME/.claude"
PROJ="$CLAUDE/projects/-Users-frank-B-agentii-space-tech-SPCX"
SESSION_DIR="$PROJ/$SESSION_ID"
DEST="$THESIS_DIR/session-history/$SESSION_ID"

# --- preflight ------------------------------------------------------------------------------
# The transcript is the one artefact whose absence makes the archive meaningless.
if [[ ! -f "$PROJ/$SESSION_ID.jsonl" ]]; then
  echo "ERROR: transcript not found: $PROJ/$SESSION_ID.jsonl" >&2
  echo "       Refusing to write an empty archive." >&2
  exit 2
fi

echo "session : $SESSION_ID"
echo "thesis  : $THESIS_DIR"
echo "dest    : $DEST"
echo

mkdir -p "$DEST"

# --- 1. transcript (RENAMED — avoids <uuid>/<uuid>.jsonl nesting) ----------------------------
rsync -a "$PROJ/$SESSION_ID.jsonl" "$DEST/transcript.jsonl"

# --- 2. in-project session dirs --------------------------------------------------------------
for sub in subagents tool-results; do
  [[ -d "$SESSION_DIR/$sub" ]] && rsync -a "$SESSION_DIR/$sub/" "$DEST/$sub/"
done

# --- 3. session-scoped sources OUTSIDE the project folder ------------------------------------
# These are easy to miss: they do not live under projects/<mangled-workspace>/.

# 3a. process registry entry — name is the PID, so match on content, not filename.
for f in "$CLAUDE"/sessions/*.json; do
  [[ -f "$f" ]] || continue
  if grep -q "\"$SESSION_ID\"" "$f" 2>/dev/null; then
    cp "$f" "$DEST/session-registry.json"
    echo "  session-registry.json  <- $(basename "$f")"
    break
  fi
done

# 3b. file history — content-addressed snapshots (<hash>@v<N>), no path annotations.
[[ -d "$CLAUDE/file-history/$SESSION_ID" ]] && \
  rsync -a "$CLAUDE/file-history/$SESSION_ID/" "$DEST/file-history/"

# 3c. telemetry — ⚠️ the filename carries a SECOND UUID: 1p_failed_events.<session>.<other>.json
#     The second id is unpredictable, so GLOB it. Naming the file would silently copy nothing.
shopt -s nullglob
for f in "$CLAUDE/telemetry/1p_failed_events.$SESSION_ID".*.json; do
  mkdir -p "$DEST/telemetry"
  cp "$f" "$DEST/telemetry/"
  echo "  telemetry/$(basename "$f")"
done
shopt -u nullglob

# 3d. this window's approved plan, if one exists.
if [[ -f "$CLAUDE/plans/clever-meandering-locket.md" ]]; then
  mkdir -p "$DEST/plans"
  cp "$CLAUDE/plans/clever-meandering-locket.md" "$DEST/plans/"
fi

# --- 4. report: counts + hashes for the MANIFEST's verification table ------------------------
echo
echo "=== archive ==="
printf '  %-34s %s\n' "files:" "$(find "$DEST" -type f | wc -l | tr -d ' ')"
printf '  %-34s %s\n' "size:" "$(du -sh "$DEST" | cut -f1)"
echo
echo "=== transcript integrity ==="
SRC_BYTES=$(stat -f%z "$PROJ/$SESSION_ID.jsonl")
DST_BYTES=$(stat -f%z "$DEST/transcript.jsonl")
printf '  %-34s %s\n' "source bytes:" "$SRC_BYTES"
printf '  %-34s %s\n' "archived bytes:" "$DST_BYTES"
# The destination must be a byte-exact PREFIX of the source. A smaller size is expected on a
# live session (it grew during the copy); a MISMATCH inside that prefix is corruption.
if cmp -s -n "$DST_BYTES" "$DEST/transcript.jsonl" "$PROJ/$SESSION_ID.jsonl"; then
  echo "  ✅ archived copy is a byte-exact prefix of the source (Δ$((SRC_BYTES - DST_BYTES)) B of live growth)"
else
  echo "  ❌ MISMATCH — the archived copy is NOT a prefix of the source. Investigate before trusting it." >&2
fi
printf '  %-34s %s\n' "sha256 (archived):" "$(shasum -a 256 "$DEST/transcript.jsonl" | cut -c1-64)"
printf '  %-34s %s\n' "first record sessionId:" \
  "$(head -1 "$DEST/transcript.jsonl" | sed -n 's/.*"sessionId":"\([^"]*\)".*/\1/p')"
echo
echo "=== source→archive map (for the MANIFEST) ==="
printf '  %-26s <- %s\n' "transcript.jsonl"        "$PROJ/$SESSION_ID.jsonl"
printf '  %-26s <- %s\n' "subagents/"              "$SESSION_DIR/subagents/"
printf '  %-26s <- %s\n' "tool-results/"           "$SESSION_DIR/tool-results/"
printf '  %-26s <- %s\n' "session-registry.json"   "$CLAUDE/sessions/<pid>.json"
printf '  %-26s <- %s\n' "file-history/"           "$CLAUDE/file-history/$SESSION_ID/"
printf '  %-26s <- %s\n' "telemetry/"              "$CLAUDE/telemetry/1p_failed_events.$SESSION_ID.*.json"
printf '  %-26s <- %s\n' "plans/"                  "$CLAUDE/plans/clever-meandering-locket.md"
echo
echo "=== git (the archive must stay untracked) ==="
git check-ignore -v "$DEST/transcript.jsonl" 2>/dev/null || echo "  ⚠️ NOT ignored — check .gitignore"
