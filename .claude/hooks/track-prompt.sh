#!/usr/bin/env bash
# Track user prompt submissions (sync - fast operation)
# Silently exit on any error to avoid blocking Claude Code

# Read JSON input from stdin
INPUT=$(cat 2>/dev/null) || exit 0

# Validate input is JSON
echo "$INPUT" | jq -e . >/dev/null 2>&1 || exit 0

# Extract fields using jq
PROMPT=$(echo "$INPUT" | jq -r '.prompt // empty' 2>/dev/null) || exit 0
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // "unknown"' 2>/dev/null) || exit 0
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Skip if no prompt
[ -z "$PROMPT" ] && exit 0

# Ensure log directory exists
mkdir -p .claude/activity-logs 2>/dev/null || exit 0

# Write log entry using jq for proper JSON (compact for JSONL)
jq -nc --arg ts "$TIMESTAMP" --arg sid "$SESSION_ID" --arg prompt "$PROMPT" \
  '{timestamp: $ts, session_id: $sid, prompt: $prompt}' >> .claude/activity-logs/prompts.jsonl 2>/dev/null

exit 0
