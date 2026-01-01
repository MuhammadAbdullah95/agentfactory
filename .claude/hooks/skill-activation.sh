#!/usr/bin/env bash
# Force Claude to evaluate skills before proceeding
# Based on research showing 84% activation vs 20% with simple hooks
# Cross-platform: Windows (Git Bash), macOS, Linux

echo '{"async":false}'

# Get script directory and source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

# Read JSON input from stdin
INPUT=$(cat 2>/dev/null) || exit 0

# Validate input is JSON
validate_json "$INPUT" || exit 0

PROMPT=$(parse_json "$INPUT" "prompt")

# Skip short prompts (greetings, confirmations)
[ ${#PROMPT} -lt 20 ] && exit 0

# Get list of available skills
SKILLS_DIR=".claude/skills"
if [ ! -d "$SKILLS_DIR" ]; then
    exit 0
fi

# Build skill list with triggers
SKILL_LIST=""
for skill_dir in "$SKILLS_DIR"/*/; do
    [ -d "$skill_dir" ] || continue
    skill_name=$(basename "$skill_dir")
    skill_file="$skill_dir/SKILL.md"

    if [ -f "$skill_file" ]; then
        # Extract description (first 200 chars after "description:")
        desc=$(grep -A5 "^description:" "$skill_file" 2>/dev/null | head -6 | tail -5 | tr '\n' ' ' | cut -c1-200)
        if [ -n "$desc" ]; then
            SKILL_LIST="$SKILL_LIST- $skill_name: $desc
"
        fi
    fi
done

# Skip if no skills found
[ -z "$SKILL_LIST" ] && exit 0

# Output the forced evaluation prompt
cat << EOF

<skill-evaluation>
MANDATORY SKILL EVALUATION - Complete before implementation

Available skills:
$SKILL_LIST
INSTRUCTIONS:
1. EVALUATE each skill against the user's request - state YES or NO with brief reason
2. For each YES skill, use Skill(skill-name) to activate it NOW
3. Only proceed with implementation AFTER activating relevant skills

CRITICAL: Skipping activation wastes the skill's knowledge. Evaluate explicitly.
</skill-evaluation>

EOF

exit 0
