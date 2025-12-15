# RFC: [Title]

**Status**: Draft
**Author**: @username
**Created**: YYYY-MM-DD
**Updated**: YYYY-MM-DD
**RFC Number**: RFC-XXXX

## Summary

<!-- One paragraph explaining the proposal. Keep it concise. -->

## Motivation

<!-- Why are we doing this? What problem does it solve? What use cases does it support? -->

### Problem Statement

<!-- Clear description of the problem -->

### Goals

<!-- What we want to achieve -->

-
-

### Non-Goals

<!-- What we explicitly are NOT trying to do -->

-
-

## Detailed Design

<!-- Technical details of the proposal -->

### Architecture

<!-- Diagrams, component interactions -->

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  Client  │────▶│  Server  │────▶│    DB    │
└──────────┘     └──────────┘     └──────────┘
```

### API Changes

<!-- New or modified APIs -->

```typescript
// New API
interface NewFeature {
  // ...
}
```

### Data Model

<!-- Database schema changes, if any -->

### Dependencies

<!-- New dependencies required -->

| Dependency | Version | Purpose |
|------------|---------|---------|
| example-lib | ^1.0.0 | Does X |

## Affected Packages

| Package | Impact | Changes Required |
|---------|--------|------------------|
| @myorg/package-a | High | Description |
| @myorg/package-b | Medium | Description |
| @myorg/package-c | Low | Description |

## Migration Strategy

### For Internal Consumers

<!-- How will our packages migrate? -->

1. Step 1
2. Step 2
3. Step 3

### For External Consumers (if applicable)

<!-- How will external users migrate? -->

### Codemod

<!-- Will we provide automated migration? -->

```bash
npx @myorg/codemods migrate-to-new-feature
```

### Deprecation Timeline

| Date | Milestone |
|------|-----------|
| YYYY-MM-DD | New API available |
| YYYY-MM-DD | Deprecation warnings added |
| YYYY-MM-DD | Old API removed |

## Alternatives Considered

### Alternative 1: [Name]

<!-- Description of alternative -->

**Pros:**
-

**Cons:**
-

**Why rejected:** <!-- Why we didn't choose this -->

### Alternative 2: [Name]

<!-- Repeat pattern -->

## Security Considerations

<!-- Security implications and mitigations -->

- [ ] Authentication/authorization impact?
- [ ] Data privacy implications?
- [ ] Input validation requirements?
- [ ] Audit logging needs?

## Performance Considerations

<!-- Performance implications -->

- Expected latency impact:
- Expected memory impact:
- Expected CPU impact:
- Caching strategy:

## Testing Strategy

<!-- How will this be tested? -->

- [ ] Unit tests
- [ ] Integration tests
- [ ] E2E tests
- [ ] Performance tests
- [ ] Security tests

## Rollout Plan

<!-- How will this be deployed? -->

### Phase 1: [Name]

- Duration:
- Scope:
- Success criteria:

### Phase 2: [Name]

- Duration:
- Scope:
- Success criteria:

### Rollback Plan

<!-- How to rollback if issues arise -->

## Open Questions

<!-- Questions that need resolution -->

1. Question 1?
2. Question 2?

## Timeline

| Phase | Duration | Description |
|-------|----------|-------------|
| RFC Review | 1 week | Gather feedback |
| Design Finalization | 1 week | Address feedback |
| Implementation | X weeks | Build the feature |
| Testing | X weeks | Comprehensive testing |
| Migration | X weeks | Update dependents |
| Release | 1 day | Ship to production |

## Approvals

<!-- Required approvals before implementation -->

- [ ] Architecture: @architect
- [ ] Security: @security-lead
- [ ] Platform: @platform-lead
- [ ] Affected Team 1: @team-lead-1
- [ ] Affected Team 2: @team-lead-2

## References

<!-- Related documents, prior art, inspiration -->

- [Related RFC](#)
- [Design Doc](#)
- [External Reference](#)

---

## Changelog

<!-- Track changes to this RFC -->

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial draft | @author |
