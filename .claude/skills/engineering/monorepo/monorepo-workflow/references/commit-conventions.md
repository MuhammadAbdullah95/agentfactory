# Commit Conventions

## Conventional Commits Format

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

## Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(auth): add OAuth2 support` |
| `fix` | Bug fix | `fix(api): handle null user response` |
| `docs` | Documentation | `docs(readme): add setup instructions` |
| `style` | Formatting (no code change) | `style(ui): fix indentation` |
| `refactor` | Code change (no feature/fix) | `refactor(utils): extract helper` |
| `perf` | Performance improvement | `perf(query): add index for search` |
| `test` | Adding/updating tests | `test(auth): add login unit tests` |
| `build` | Build system changes | `build(deps): update typescript` |
| `ci` | CI configuration | `ci: add merge queue workflow` |
| `chore` | Other changes | `chore: update .gitignore` |
| `revert` | Revert previous commit | `revert: feat(auth): add OAuth2` |

## Scope

Scope should be the **package name** (without org prefix) or **domain area**:

```
feat(auth): ...           # packages/auth
feat(web): ...            # apps/web
feat(ui): ...             # packages/ui
feat(api): ...            # services/api
feat(ci): ...             # CI/CD changes
feat(deps): ...           # Dependency updates
```

## Description Guidelines

- Use imperative mood: "add" not "added" or "adds"
- Don't capitalize first letter
- No period at end
- Keep under 72 characters
- Explain WHAT and WHY, not HOW

### Good
```
feat(auth): add session timeout handling
fix(api): prevent duplicate user creation
refactor(utils): extract date formatting logic
```

### Bad
```
feat(auth): Added session timeout.        # Past tense, period
Fix: api bug                              # Vague, wrong format
refactor(utils): refactoring              # Doesn't explain what
```

## Body

Use body for:
- Explaining WHY the change was made
- Providing context not obvious from code
- Listing breaking changes

```
feat(auth): add session timeout handling

Sessions now expire after 24 hours of inactivity.
This improves security by limiting stale sessions.

Closes #123
```

## Footer

### Breaking Changes

```
feat(auth)!: remove legacy login function

BREAKING CHANGE: legacyLogin() has been removed.
Use login() instead. See migration guide at docs/auth.md
```

Or with footer:

```
feat(auth): update login API

BREAKING CHANGE: login() now requires an options object
instead of positional arguments.

Before: login(user, pass)
After: login({ user, pass })
```

### Issue References

```
feat(auth): add OAuth support

Implements OAuth2 authorization code flow with PKCE.

Closes #123
Refs #456
```

## Monorepo-Specific Conventions

### Multi-Package Changes

When changing multiple packages, list all scopes:

```
refactor(ui,web): extract Button component to shared package
```

Or use separate commits (preferred):

```
refactor(ui): add Button component
refactor(web): use Button from @myorg/ui
```

### Cross-Cutting Changes

```
chore(deps): update typescript to 5.3
build(turbo): optimize build caching
ci: add affected-only testing
```

### Breaking Changes in Monorepo

```
feat(auth)!: migrate to new session API

BREAKING CHANGE: Session interface changed.

Affected packages:
- @myorg/web (updated)
- @myorg/mobile (updated)
- @myorg/admin (updated)

Migration: See docs/auth-migration.md
```

## Commit Message Template

Create `.gitmessage`:

```
# <type>(<scope>): <description>
#
# [optional body]
#
# [optional footer(s)]
#
# Types: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert
# Scope: package name or domain area (auth, web, ui, api, etc.)
#
# Rules:
# - Use imperative mood in description
# - Don't capitalize first letter
# - No period at end
# - Keep description under 72 chars
# - Wrap body at 72 chars
# - Use footer for breaking changes and issue refs
#
# Example:
# feat(auth): add OAuth2 support
#
# Implements OAuth2 authorization code flow with PKCE
# for improved security.
#
# Closes #123
```

Configure:
```bash
git config commit.template .gitmessage
```

## Commit Hooks

### commitlint

```bash
# Install
pnpm add -D @commitlint/cli @commitlint/config-conventional

# commitlint.config.js
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'scope-enum': [2, 'always', [
      'auth', 'web', 'mobile', 'ui', 'utils', 'api',
      'deps', 'ci', 'turbo', 'docs'
    ]],
  },
};
```

### Husky

```bash
# Install
pnpm add -D husky
pnpm husky init

# .husky/commit-msg
pnpm commitlint --edit $1
```

## Quick Reference

```
# Feature
feat(scope): add new feature

# Bug fix
fix(scope): fix the bug

# Breaking change
feat(scope)!: breaking change

# With body and footer
feat(scope): short description

Longer explanation of the change
and why it was needed.

BREAKING CHANGE: explanation
Closes #123
```
