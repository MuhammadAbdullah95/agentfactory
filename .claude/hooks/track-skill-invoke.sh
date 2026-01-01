#!/usr/bin/env bash
# Track Skill tool invocations (when user runs /skill-name or agent uses Skill tool)
# Cross-platform: Windows (Git Bash), macOS, Linux
# Silently exit on any error to avoid blocking Claude Code

# Get script directory and source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

# Read JSON input from stdin
INPUT=$(cat 2>/dev/null) || exit 0

# Validate input is JSON
validate_json "$INPUT" || exit 0

# Extract tool name - only process Skill tool
TOOL=$(parse_json "$INPUT" "tool_name")
[ "$TOOL" != "Skill" ] && exit 0

# Extract skill name from tool input
SKILL_NAME=$(parse_json "$INPUT" "tool_input.skill")
[ -z "$SKILL_NAME" ] && exit 0

# Get optional args
ARGS=$(parse_json "$INPUT" "tool_input.args")

SESSION_ID=$(parse_json "$INPUT" "session_id")
[ -z "$SESSION_ID" ] && SESSION_ID="unknown"

TIMESTAMP=$(get_timestamp)

# Write invocation event
LOG_ENTRY=$(create_json "timestamp" "$TIMESTAMP" "session_id" "$SESSION_ID" "skill" "$SKILL_NAME" "args" "$ARGS" "event" "invoke" "source" "Skill_tool")
write_jsonl ".claude/activity-logs/skill-usage.jsonl" "$LOG_ENTRY"

exit 0
