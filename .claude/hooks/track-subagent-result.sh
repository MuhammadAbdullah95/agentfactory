#!/usr/bin/env bash
# Track Task tool results (subagent completion)
# Cross-platform: Windows (Git Bash), macOS, Linux
# Silently exit on any error to avoid blocking Claude Code

# Get script directory and source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

# Read JSON input from stdin
INPUT=$(cat 2>/dev/null) || exit 0

# Validate input is JSON
validate_json "$INPUT" || exit 0

# Extract tool name - only process Task tool
TOOL=$(parse_json "$INPUT" "tool_name")
[ "$TOOL" != "Task" ] && exit 0

# Extract result info
SUBAGENT_TYPE=$(parse_json "$INPUT" "tool_input.subagent_type")
[ -z "$SUBAGENT_TYPE" ] && SUBAGENT_TYPE="unknown"

AGENT_ID=$(parse_json "$INPUT" "tool_result.agent_id")
RESULT_TEXT=$(parse_json "$INPUT" "tool_result")

# Determine status
STATUS="completed"
if echo "$RESULT_TEXT" | grep -qi "error\|failed\|exception" 2>/dev/null; then
    STATUS="error"
fi

SESSION_ID=$(parse_json "$INPUT" "session_id")
[ -z "$SESSION_ID" ] && SESSION_ID="unknown"

TIMESTAMP=$(get_timestamp)

# Write subagent completion event
LOG_ENTRY=$(create_json "timestamp" "$TIMESTAMP" "session_id" "$SESSION_ID" "subagent" "$SUBAGENT_TYPE" "agent_id" "$AGENT_ID" "status" "$STATUS" "event" "complete")
write_jsonl ".claude/activity-logs/subagent-usage.jsonl" "$LOG_ENTRY"

exit 0
