#!/usr/bin/env bash
# Track Task tool invocations (subagent spawning)
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

# Extract subagent details
SUBAGENT_TYPE=$(parse_json "$INPUT" "tool_input.subagent_type")
[ -z "$SUBAGENT_TYPE" ] && SUBAGENT_TYPE="unknown"

DESCRIPTION=$(parse_json "$INPUT" "tool_input.description")
RUN_IN_BACKGROUND=$(parse_json_bool "$INPUT" "tool_input.run_in_background")
MODEL=$(parse_json "$INPUT" "tool_input.model")
[ -z "$MODEL" ] && MODEL="inherit"

SESSION_ID=$(parse_json "$INPUT" "session_id")
[ -z "$SESSION_ID" ] && SESSION_ID="unknown"

TIMESTAMP=$(get_timestamp)

# Write subagent spawn event
LOG_ENTRY=$(create_json "timestamp" "$TIMESTAMP" "session_id" "$SESSION_ID" "subagent" "$SUBAGENT_TYPE" "description" "$DESCRIPTION" "background" "$RUN_IN_BACKGROUND" "model" "$MODEL" "event" "spawn")
write_jsonl ".claude/activity-logs/subagent-usage.jsonl" "$LOG_ENTRY"

exit 0
