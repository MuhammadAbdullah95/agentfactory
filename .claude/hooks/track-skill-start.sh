#!/usr/bin/env bash
# Track skill activations via SKILL.md reads (sync - fast operation)
# Cross-platform: Windows (Git Bash), macOS, Linux
# Silently exit on any error to avoid blocking Claude Code

# Get script directory and source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

# Read JSON input from stdin
INPUT=$(cat 2>/dev/null) || exit 0

# Validate input is JSON
validate_json "$INPUT" || exit 0

# Extract tool name - only process Read tool
TOOL=$(parse_json "$INPUT" "tool_name")
[ "$TOOL" != "Read" ] && exit 0

FILE_PATH=$(parse_json "$INPUT" "tool_input.file_path")
[ -z "$FILE_PATH" ] && exit 0

# Normalize path separators for cross-platform matching
NORMALIZED_PATH=$(echo "$FILE_PATH" | sed 's/\\/\//g')

# Only match SKILL.md reads in .claude/skills/[name]/
if [[ "$NORMALIZED_PATH" =~ \.claude/skills/([a-z][a-z0-9-]*)/SKILL\.md$ ]]; then
    SKILL_NAME="${BASH_REMATCH[1]}"
else
    exit 0
fi

# Validate skill exists (has SKILL.md)
SKILL_DIR=".claude/skills/$SKILL_NAME"
[ ! -f "$SKILL_DIR/SKILL.md" ] && exit 0

SESSION_ID=$(parse_json "$INPUT" "session_id")
[ -z "$SESSION_ID" ] && SESSION_ID="unknown"

TIMESTAMP=$(get_timestamp)

# Write start event
LOG_ENTRY=$(create_json "timestamp" "$TIMESTAMP" "session_id" "$SESSION_ID" "skill" "$SKILL_NAME" "event" "start")
write_jsonl ".claude/activity-logs/skill-usage.jsonl" "$LOG_ENTRY"

exit 0
