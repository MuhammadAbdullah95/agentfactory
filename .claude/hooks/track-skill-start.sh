#!/usr/bin/env bash
# Track skill activations via SKILL.md reads (sync - fast operation)
# Silently exit on any error to avoid blocking Claude Code

# Read JSON input from stdin
INPUT=$(cat 2>/dev/null) || exit 0

# Validate input is JSON
echo "$INPUT" | jq -e . >/dev/null 2>&1 || exit 0

# Extract tool and file path - ONLY Read tool, not Bash
TOOL=$(echo "$INPUT" | jq -r '.tool_name // empty' 2>/dev/null) || exit 0
[ "$TOOL" != "Read" ] && exit 0

FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty' 2>/dev/null) || exit 0

# Only match SKILL.md reads in .claude/skills/[name]/
if [[ "$FILE_PATH" =~ \.claude/skills/([a-z][a-z0-9-]*)/SKILL\.md$ ]]; then
    SKILL_NAME="${BASH_REMATCH[1]}"
else
    exit 0
fi

# Validate skill exists (has SKILL.md)
SKILL_DIR=".claude/skills/$SKILL_NAME"
[ ! -f "$SKILL_DIR/SKILL.md" ] && exit 0

SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // "unknown"' 2>/dev/null) || exit 0
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Ensure log directory exists
mkdir -p .claude/activity-logs 2>/dev/null || exit 0

# Write start event
jq -nc --arg ts "$TIMESTAMP" --arg sid "$SESSION_ID" --arg skill "$SKILL_NAME" \
  '{timestamp: $ts, session_id: $sid, skill: $skill, event: "start"}' >> .claude/activity-logs/skill-usage.jsonl 2>/dev/null

exit 0
