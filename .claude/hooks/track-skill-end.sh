#!/usr/bin/env bash
# Track skill verification results (sync - fast operation)
# Cross-platform: Windows (Git Bash), macOS, Linux
# Silently exit on any error to avoid blocking Claude Code

# Get script directory and source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

# Read JSON input from stdin
INPUT=$(cat 2>/dev/null) || exit 0

# Validate input is JSON
validate_json "$INPUT" || exit 0

# Extract command and exit code
COMMAND=$(parse_json "$INPUT" "tool_input.command")
EXIT_CODE=$(parse_json "$INPUT" "tool_result.exit_code")

[ -z "$COMMAND" ] && exit 0

# Normalize path separators for cross-platform matching
NORMALIZED_CMD=$(echo "$COMMAND" | sed 's/\\/\//g')

# Check if command is running verify.py
SKILL_NAME=""
if [[ "$NORMALIZED_CMD" =~ skills/([^/]+)/scripts/verify\.py ]]; then
    SKILL_NAME="${BASH_REMATCH[1]}"
elif [[ "$NORMALIZED_CMD" =~ verify\.py ]] && [[ "$NORMALIZED_CMD" =~ skills/([^/]+)/ ]]; then
    SKILL_NAME="${BASH_REMATCH[1]}"
fi

[ -z "$SKILL_NAME" ] && exit 0

# Determine status from exit code
if [ "$EXIT_CODE" = "0" ]; then
    STATUS="success"
else
    STATUS="failure"
fi

SESSION_ID=$(parse_json "$INPUT" "session_id")
[ -z "$SESSION_ID" ] && SESSION_ID="unknown"

TIMESTAMP=$(get_timestamp)

# Write verify event
LOG_ENTRY=$(create_json "timestamp" "$TIMESTAMP" "session_id" "$SESSION_ID" "skill" "$SKILL_NAME" "event" "verify" "status" "$STATUS")
write_jsonl ".claude/activity-logs/skill-usage.jsonl" "$LOG_ENTRY"

exit 0
