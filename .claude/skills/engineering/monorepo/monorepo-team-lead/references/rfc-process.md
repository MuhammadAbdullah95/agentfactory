# RFC Process for Monorepos

## What is an RFC?

RFC (Request for Comments) is a design document for proposing significant changes that:
- Affect multiple packages or teams
- Introduce breaking changes
- Add new architectural patterns
- Change fundamental workflows

## When to Write an RFC

| Scenario | RFC Required? |
|----------|---------------|
| New shared package | ✅ Yes |
| Breaking API change | ✅ Yes |
| New technology/framework | ✅ Yes |
| Cross-team workflow change | ✅ Yes |
| Bug fix | ❌ No |
| New feature in one package | ❌ No |
| Documentation update | ❌ No |
| Dependency update | ❌ Usually no |

## RFC Lifecycle

```
┌─────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Draft  │───▶│ Review   │───▶│ Approved │───▶│Implement │───▶│  Done    │
└─────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
     │              │                                               │
     │              │                                               │
     ▼              ▼                                               ▼
┌─────────┐    ┌──────────┐                                   ┌──────────┐
│Withdrawn│    │ Rejected │                                   │Superseded│
└─────────┘    └──────────┘                                   └──────────┘
```

### States

- **Draft**: Work in progress, not ready for review
- **Review**: Open for feedback and discussion
- **Approved**: Accepted, ready for implementation
- **Implement**: Work is being done
- **Done**: Fully implemented and released
- **Withdrawn**: Author chose not to proceed
- **Rejected**: Not accepted after review
- **Superseded**: Replaced by a newer RFC

## RFC Template

```markdown
# RFC: [Title]

**Status**: Draft | Review | Approved | Implementing | Done
**Author**: @username
**Created**: YYYY-MM-DD
**Updated**: YYYY-MM-DD

## Summary

One paragraph explaining the proposal at a high level.

## Motivation

Why are we doing this? What problem does it solve?
What use cases does it support?

## Detailed Design

Technical details of the proposal:
- Architecture diagrams
- API specifications
- Data models
- Integration points

## Affected Packages

| Package | Impact | Changes Required |
|---------|--------|------------------|
| @myorg/pkg-a | High | Complete rewrite |
| @myorg/pkg-b | Medium | API updates |
| @myorg/pkg-c | Low | Type updates |

## Migration Strategy

How will existing code migrate?
- Automated migration (codemod)
- Manual migration steps
- Deprecation timeline

## Alternatives Considered

What other approaches were considered?
Why were they rejected?

## Open Questions

1. Question 1?
2. Question 2?

## Timeline

| Phase | Duration | Description |
|-------|----------|-------------|
| RFC Review | 1 week | Gather feedback |
| Implementation | 2 weeks | Build the feature |
| Migration | 1 week | Update dependents |
| Release | 1 day | Ship to production |

## Approvals

- [ ] Architecture: @architect
- [ ] Security: @security-lead (if applicable)
- [ ] Affected Team 1: @team-lead-1
- [ ] Affected Team 2: @team-lead-2

## References

- [Related RFC](#)
- [Design Doc](#)
- [Prior Art](#)
```

## Process Steps

### 1. Create Draft

```bash
# Create RFC file
mkdir -p docs/rfcs
touch docs/rfcs/YYYY-MM-DD-feature-name.md

# Use template
cp templates/rfc.md docs/rfcs/YYYY-MM-DD-feature-name.md
```

### 2. Get Early Feedback

Before formal review:
- Share with 1-2 trusted colleagues
- Iterate on the design
- Fill in open questions

### 3. Open for Review

```bash
# Create PR for the RFC
gh pr create \
  --title "RFC: Feature Name" \
  --body "RFC for review. Please provide feedback." \
  --label "rfc"
```

### 4. Review Period

- **Duration**: 1 week minimum
- **Notify**: Tag all affected teams
- **Discuss**: Use PR comments for feedback
- **Iterate**: Update RFC based on feedback

### 5. Approval

Required approvals vary by impact:
- **Low impact**: 1 team lead
- **Medium impact**: 2+ team leads
- **High impact**: Architecture + affected teams
- **Breaking change**: All affected teams + senior

### 6. Implementation

After approval:
1. Create implementation issues
2. Break into PRs
3. Reference RFC in commits
4. Update RFC status as work progresses

### 7. Completion

When done:
1. Update RFC status to "Done"
2. Update documentation
3. Announce to affected teams
4. Archive if superseded

## RFC Review Checklist

For reviewers:

- [ ] Problem clearly stated?
- [ ] Solution addresses the problem?
- [ ] Alternatives considered?
- [ ] Migration path clear?
- [ ] Timeline realistic?
- [ ] All affected packages identified?
- [ ] Security implications addressed?
- [ ] Performance implications addressed?
- [ ] Testing strategy defined?

## Common Pitfalls

### 1. Too Broad
```
❌ "Rewrite everything to use new framework"
✅ "Migrate auth package to new framework"
```

### 2. Too Vague
```
❌ "Improve performance"
✅ "Reduce API response time by 50% through caching"
```

### 3. Missing Migration
```
❌ "Here's the new API"
✅ "Here's the new API + codemod + deprecation timeline"
```

### 4. No Alternatives
```
❌ "We should use X"
✅ "We considered X, Y, Z. X wins because..."
```

## Quick Commands

```bash
# Create new RFC
./scripts/create-rfc.sh "Feature Name"

# List open RFCs
gh pr list --label "rfc" --state open

# Find RFCs for a package
grep -r "@myorg/package-name" docs/rfcs/
```

## Templates Location

```
templates/
├── rfc.md
├── rfc-breaking-change.md
└── rfc-new-package.md
```
