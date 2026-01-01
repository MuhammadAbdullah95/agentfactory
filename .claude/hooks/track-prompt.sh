#!/usr/bin/env bash
# Track user prompt submissions (sync - fast operation)
# Cross-platform: Windows (Git Bash), macOS, Linux
# Silently exit on any error to avoid blocking Claude Code

# Get script directory and source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

# Read JSON input from stdin
INPUT=$(cat 2>/dev/null) || exit 0

# Validate input is JSON
validate_json "$INPUT" || exit 0

# Extract fields
PROMPT=$(parse_json "$INPUT" "prompt")
SESSION_ID=$(parse_json "$INPUT" "session_id")
[ -z "$SESSION_ID" ] && SESSION_ID="unknown"

# Skip if no prompt
[ -z "$PROMPT" ] && exit 0

TIMESTAMP=$(get_timestamp)

# Write log entry
LOG_ENTRY=$(create_json "timestamp" "$TIMESTAMP" "session_id" "$SESSION_ID" "prompt" "$PROMPT")
write_jsonl ".claude/activity-logs/prompts.jsonl" "$LOG_ENTRY"

exit 0
