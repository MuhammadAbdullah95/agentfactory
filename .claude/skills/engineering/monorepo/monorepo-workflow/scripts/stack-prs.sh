#!/bin/bash
# stack-prs.sh - Helper for PR stacking workflow
# Usage: ./stack-prs.sh [create|rebase|status|submit]

set -euo pipefail

ACTION=${1:-"status"}

# Check for graphite
HAS_GRAPHITE=false
if command -v gt &> /dev/null; then
    HAS_GRAPHITE=true
fi

case "$ACTION" in
    "status")
        echo "=== PR Stack Status ==="
        echo ""

        if $HAS_GRAPHITE; then
            echo "Using Graphite:"
            gt log --oneline 2>/dev/null || echo "  (not in a stack)"
        else
            echo "Using Git:"
            # Show branch relationship
            current=$(git branch --show-current)
            echo "Current branch: $current"
            echo ""

            # Find stacked branches (branches based on current)
            echo "Branches based on $current:"
            git branch --list | while read branch; do
                branch=$(echo "$branch" | tr -d '* ')
                base=$(git merge-base "$current" "$branch" 2>/dev/null || true)
                if [[ -n "$base" ]] && [[ "$branch" != "$current" ]]; then
                    ahead=$(git rev-list --count "$base..$branch" 2>/dev/null || echo "0")
                    if [[ "$ahead" -gt 0 ]]; then
                        echo "  $branch (+$ahead commits)"
                    fi
                fi
            done
        fi

        # Show open PRs
        echo ""
        echo "Open PRs from current user:"
        gh pr list --author="@me" --state=open --json number,title,baseRefName,headRefName \
            --jq '.[] | "#\(.number) \(.headRefName) → \(.baseRefName): \(.title)"' 2>/dev/null || true
        ;;

    "create")
        TITLE=${2:-""}
        if [[ -z "$TITLE" ]]; then
            echo "Usage: $0 create \"commit message\""
            exit 1
        fi

        if $HAS_GRAPHITE; then
            echo "Creating stacked branch with Graphite..."
            gt create -m "$TITLE"
        else
            echo "Creating stacked branch manually..."

            # Get current branch as base
            BASE=$(git branch --show-current)

            # Generate branch name from title
            BRANCH=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//' | sed 's/-$//')
            BRANCH="feat/$BRANCH"

            # Create and switch to new branch
            git checkout -b "$BRANCH"

            echo ""
            echo "Created branch: $BRANCH (based on $BASE)"
            echo ""
            echo "After committing, create PR with:"
            echo "  gh pr create --base $BASE"
        fi
        ;;

    "rebase")
        echo "=== Rebasing Stack ==="

        if $HAS_GRAPHITE; then
            echo "Syncing with Graphite..."
            gt sync
        else
            echo "Manual rebase..."
            current=$(git branch --show-current)

            # Check if base branch exists
            if gh pr view --json baseRefName --jq '.baseRefName' &>/dev/null; then
                base=$(gh pr view --json baseRefName --jq '.baseRefName')
                echo "Rebasing $current onto $base..."
                git fetch origin "$base"
                git rebase "origin/$base"
                echo "Pushing with force-with-lease..."
                git push --force-with-lease
            else
                echo "No PR found for current branch"
                echo "Rebasing onto main..."
                git fetch origin main
                git rebase origin/main
            fi
        fi
        ;;

    "submit")
        echo "=== Submitting Stack ==="

        if $HAS_GRAPHITE; then
            echo "Submitting with Graphite..."
            gt submit --stack
        else
            echo "Manual submission..."
            current=$(git branch --show-current)

            # Push current branch
            git push -u origin "$current"

            # Check if PR exists
            if gh pr view &>/dev/null; then
                echo "PR already exists"
                gh pr view --web
            else
                echo "Creating PR..."
                gh pr create --fill
            fi
        fi
        ;;

    "merge")
        echo "=== Merging Stack ==="

        if $HAS_GRAPHITE; then
            echo "Note: Merge bottom of stack first in Graphite UI"
            gt log --oneline
        else
            echo "Manual merge workflow:"
            echo "1. Merge the bottom PR first (the one targeting main)"
            echo "2. After merge, update remaining PRs to target main"
            echo "3. Repeat until all merged"
            echo ""
            echo "Commands:"
            echo "  gh pr merge --squash --delete-branch"
            echo "  gh pr edit --base main"
        fi
        ;;

    *)
        echo "PR Stacking Helper"
        echo ""
        echo "Usage: $0 [action]"
        echo ""
        echo "Actions:"
        echo "  status  - Show current stack status (default)"
        echo "  create  - Create new branch in stack"
        echo "  rebase  - Rebase stack onto updated base"
        echo "  submit  - Submit/push stack for review"
        echo "  merge   - Help with merging stack"
        echo ""
        echo "Requirements:"
        echo "  - GitHub CLI (gh): required"
        echo "  - Graphite CLI (gt): optional, provides better UX"
        echo ""
        echo "Install Graphite: https://graphite.dev/docs/installing-the-cli"
        ;;
esac
