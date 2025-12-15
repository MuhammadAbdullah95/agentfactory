#!/bin/bash
# breaking-change.sh - Create breaking change announcement and tracking
# Usage: ./breaking-change.sh <package-name> <short-description>

set -euo pipefail

PACKAGE=${1:-""}
DESCRIPTION=${2:-""}

if [[ -z "$PACKAGE" ]] || [[ -z "$DESCRIPTION" ]]; then
    echo "Usage: $0 <package-name> <short-description>"
    echo ""
    echo "Example: $0 @myorg/auth \"Remove legacy login function\""
    exit 1
fi

# Get current date
DATE=$(date +%Y-%m-%d)
SLUG=$(echo "$DESCRIPTION" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g')

echo "=== Creating Breaking Change Announcement ==="
echo "Package: $PACKAGE"
echo "Description: $DESCRIPTION"
echo ""

# Find dependents
echo "Finding affected packages..."
DEPENDENTS=$(grep -r "\"$PACKAGE\"" --include="package.json" . 2>/dev/null | grep -v node_modules | cut -d: -f1 | xargs -I {} dirname {} | sort -u || true)

if [[ -n "$DEPENDENTS" ]]; then
    echo "Affected packages:"
    echo "$DEPENDENTS" | sed 's/^/  /'
else
    echo "No dependent packages found (or package name not found)"
fi

# Create announcement file
ANNOUNCE_FILE="BREAKING-CHANGE-$DATE-$SLUG.md"

cat > "$ANNOUNCE_FILE" << EOF
# Breaking Change: $PACKAGE

**Date**: $DATE
**Status**: 🟡 Announced

## Summary

$DESCRIPTION

## Package

\`$PACKAGE\`

## Affected Packages

$(if [[ -n "$DEPENDENTS" ]]; then echo "$DEPENDENTS" | sed 's/^/- /'; else echo "- (none detected)"; fi)

## Migration Guide

### Before

\`\`\`typescript
// OLD API - will be removed
import { oldFunction } from '$PACKAGE';

oldFunction(args);
\`\`\`

### After

\`\`\`typescript
// NEW API - use this instead
import { newFunction } from '$PACKAGE';

newFunction({ ...args });
\`\`\`

## Timeline

| Date | Milestone |
|------|-----------|
| $DATE | 📢 Announcement |
| $(date -d "+7 days" +%Y-%m-%d 2>/dev/null || date -v+7d +%Y-%m-%d) | ⚠️ Deprecation warning added |
| $(date -d "+21 days" +%Y-%m-%d 2>/dev/null || date -v+21d +%Y-%m-%d) | 🗑️ Old API removed |

## Required Approvals

- [ ] Package owner (@team-owner)
$(if [[ -n "$DEPENDENTS" ]]; then echo "$DEPENDENTS" | head -5 | while read dep; do
    team=$(echo "$dep" | sed 's|.*/||' | sed 's/-.*//');
    echo "- [ ] $dep owner (@team-$team)";
done; fi)

## Deprecation Code

Add this to the old function:

\`\`\`typescript
/**
 * @deprecated Use newFunction() instead. Will be removed in v2.0.
 * Migration guide: [link to this file]
 */
export function oldFunction(...args) {
  console.warn(
    '⚠️ oldFunction is deprecated and will be removed in v2.0. ' +
    'Please migrate to newFunction(). ' +
    'See: [migration guide URL]'
  );
  return newFunction(...convertArgs(args));
}
\`\`\`

## Checklist

- [ ] Announcement created (this file)
- [ ] RFC/Discussion opened
- [ ] All affected team owners notified
- [ ] Deprecation warning added to old API
- [ ] Migration guide complete with examples
- [ ] Codemod created (if applicable)
- [ ] All dependents migrated
- [ ] Old API removed
- [ ] Release notes updated

## Notes

<!-- Add any additional context, discussion links, or notes here -->

EOF

echo ""
echo "Created: $ANNOUNCE_FILE"
echo ""

# Create GitHub issue (optional)
read -p "Create GitHub issue for tracking? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    if command -v gh &> /dev/null; then
        ISSUE_URL=$(gh issue create \
            --title "Breaking Change: $PACKAGE - $DESCRIPTION" \
            --body "$(cat "$ANNOUNCE_FILE")" \
            --label "breaking-change" 2>/dev/null || echo "")

        if [[ -n "$ISSUE_URL" ]]; then
            echo "Created issue: $ISSUE_URL"
        else
            echo "Failed to create issue (check gh auth status)"
        fi
    else
        echo "GitHub CLI not installed. Install with: brew install gh"
    fi
fi

echo ""
echo "Next steps:"
echo "1. Review and edit $ANNOUNCE_FILE"
echo "2. Get approvals from affected teams"
echo "3. Add deprecation warnings to old API"
echo "4. Create migration codemod if needed"
echo "5. Monitor for migration completion"
echo "6. Remove old API after timeline"
