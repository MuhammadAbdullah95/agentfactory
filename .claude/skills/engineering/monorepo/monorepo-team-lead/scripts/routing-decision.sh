#!/bin/bash
# routing-decision.sh - Help decide task routing (Human vs AI)
# Usage: ./routing-decision.sh

set -euo pipefail

echo "=== Task Routing Decision Helper ==="
echo ""
echo "Answer the following questions to determine optimal task routing."
echo ""

# Question 1: Task type
echo "1. What type of task is this?"
echo "   a) Code implementation (new feature, bug fix)"
echo "   b) Code review / quality check"
echo "   c) Architecture / design decision"
echo "   d) Documentation / comments"
echo "   e) DevOps / CI/CD"
echo "   f) Dependency update"
echo "   g) Refactoring"
echo "   h) Testing"
echo ""
read -p "Enter choice (a-h): " TASK_TYPE

# Question 2: Scope
echo ""
echo "2. What is the scope of the change?"
echo "   a) Single file"
echo "   b) Single package"
echo "   c) Multiple packages (same domain)"
echo "   d) Cross-domain / cross-team"
echo "   e) Infrastructure / platform-wide"
echo ""
read -p "Enter choice (a-e): " SCOPE

# Question 3: Risk level
echo ""
echo "3. What is the risk level?"
echo "   a) Low (cosmetic, docs, tests)"
echo "   b) Medium (feature, bug fix)"
echo "   c) High (security, auth, payments)"
echo "   d) Critical (production, data, infrastructure)"
echo ""
read -p "Enter choice (a-d): " RISK

# Question 4: Judgment required
echo ""
echo "4. Does this require human judgment?"
echo "   a) No - well-defined, deterministic"
echo "   b) Some - has edge cases but manageable"
echo "   c) Yes - requires context, intuition"
echo "   d) Critical - business/ethical decisions"
echo ""
read -p "Enter choice (a-d): " JUDGMENT

# Question 5: Repetitive?
echo ""
echo "5. Is this task repetitive?"
echo "   a) One-time task"
echo "   b) Occasional (few times a month)"
echo "   c) Frequent (weekly)"
echo "   d) Very frequent (daily)"
echo ""
read -p "Enter choice (a-d): " REPETITIVE

echo ""
echo "=== Analysis ==="
echo ""

# Calculate routing score
SCORE=0
REASON=""

# Task type scoring
case $TASK_TYPE in
    a) SCORE=$((SCORE + 2)); REASON+="Implementation: AI can assist. " ;;
    b) SCORE=$((SCORE + 1)); REASON+="Review: Human primary, AI assists. " ;;
    c) SCORE=$((SCORE + 4)); REASON+="Architecture: Human required. " ;;
    d) SCORE=$((SCORE + 0)); REASON+="Docs: AI well-suited. " ;;
    e) SCORE=$((SCORE + 2)); REASON+="DevOps: AI can handle with review. " ;;
    f) SCORE=$((SCORE + 0)); REASON+="Deps: AI autonomous. " ;;
    g) SCORE=$((SCORE + 1)); REASON+="Refactor: AI with review. " ;;
    h) SCORE=$((SCORE + 1)); REASON+="Testing: AI well-suited. " ;;
esac

# Scope scoring
case $SCOPE in
    a) SCORE=$((SCORE + 0)); REASON+="Single file: Low coordination. " ;;
    b) SCORE=$((SCORE + 1)); REASON+="Single package: Moderate scope. " ;;
    c) SCORE=$((SCORE + 2)); REASON+="Multi-package: Needs awareness. " ;;
    d) SCORE=$((SCORE + 4)); REASON+="Cross-domain: Human coordination required. " ;;
    e) SCORE=$((SCORE + 3)); REASON+="Platform-wide: Senior review needed. " ;;
esac

# Risk scoring
case $RISK in
    a) SCORE=$((SCORE + 0)); REASON+="Low risk: Autonomous OK. " ;;
    b) SCORE=$((SCORE + 1)); REASON+="Medium risk: Review recommended. " ;;
    c) SCORE=$((SCORE + 3)); REASON+="High risk: Human required. " ;;
    d) SCORE=$((SCORE + 5)); REASON+="Critical risk: Senior human required. " ;;
esac

# Judgment scoring
case $JUDGMENT in
    a) SCORE=$((SCORE + 0)); REASON+="Deterministic: AI suitable. " ;;
    b) SCORE=$((SCORE + 1)); REASON+="Edge cases: AI with review. " ;;
    c) SCORE=$((SCORE + 3)); REASON+="Judgment needed: Human primary. " ;;
    d) SCORE=$((SCORE + 5)); REASON+="Critical judgment: Human only. " ;;
esac

# Repetitive scoring (inverse - more repetitive = more AI)
case $REPETITIVE in
    a) SCORE=$((SCORE + 1)); REASON+="One-time: Consider approach. " ;;
    b) SCORE=$((SCORE + 0)); REASON+="Occasional: Either works. " ;;
    c) SCORE=$((SCORE - 1)); REASON+="Frequent: AI saves time. " ;;
    d) SCORE=$((SCORE - 2)); REASON+="Very frequent: Automate with AI. " ;;
esac

echo "Score: $SCORE (lower = more AI suitable)"
echo ""
echo "Factors:"
echo "$REASON" | tr '.' '\n' | grep -v "^$" | sed 's/^/  - /'
echo ""

# Recommendation
echo "=== Recommendation ==="
echo ""

if [[ $SCORE -le 2 ]]; then
    echo "🤖 AI AUTONOMOUS"
    echo ""
    echo "This task is well-suited for AI to handle autonomously."
    echo ""
    echo "Workflow:"
    echo "  1. AI executes task"
    echo "  2. AI creates PR"
    echo "  3. Human reviews output"
    echo "  4. Merge if satisfactory"

elif [[ $SCORE -le 5 ]]; then
    echo "🤝 AI-ASSISTED (Human Reviews)"
    echo ""
    echo "AI can do the work, but human should review carefully."
    echo ""
    echo "Workflow:"
    echo "  1. Human provides clear requirements"
    echo "  2. AI implements solution"
    echo "  3. Human reviews thoroughly"
    echo "  4. Iterate if needed"
    echo "  5. Human approves and merges"

elif [[ $SCORE -le 8 ]]; then
    echo "👤 HUMAN PRIMARY (AI Assists)"
    echo ""
    echo "Human should lead, AI can help with specific subtasks."
    echo ""
    echo "Workflow:"
    echo "  1. Human designs approach"
    echo "  2. AI assists with implementation"
    echo "  3. Human makes key decisions"
    echo "  4. Human reviews all changes"
    echo "  5. Human approves and merges"

else
    echo "👤👤 HUMAN ONLY"
    echo ""
    echo "This task requires human judgment and cannot be delegated to AI."
    echo ""
    echo "Workflow:"
    echo "  1. Human plans and designs"
    echo "  2. Human implements"
    echo "  3. Human/team reviews"
    echo "  4. Senior approval required"
    echo ""
    echo "AI can assist with:"
    echo "  - Research and information gathering"
    echo "  - Generating test cases"
    echo "  - Documentation drafts"
    echo "  - Boilerplate code (human reviews)"
fi

echo ""
echo "=== Quick Reference ==="
echo ""
echo "HUMAN ONLY: Architecture, security, production deploys, cross-team"
echo "HUMAN + AI: Features, refactoring, bug fixes with review"
echo "AI + REVIEW: Tests, docs, deps, lint fixes"
echo "AI AUTONOMOUS: Formatting, simple deps, generated code"
