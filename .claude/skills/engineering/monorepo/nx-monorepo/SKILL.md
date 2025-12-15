---
name: nx-monorepo
description: |
  Nx monorepo management skill for AI-native development. This skill should be used when working with Nx workspaces, project graphs, affected detection, code generation, and caching. Use when: analyzing dependencies, running affected commands, generating code, configuring Nx Cloud, or optimizing build performance. Invoke nx-mcp tools for documentation queries.
version: "1.0.0"
---

# Nx Monorepo

## Overview

This skill provides expert-level capabilities for Nx monorepo management. Nx is the standard build orchestrator for this AI-native platform due to its official MCP server integration.

**Why Nx**: Official MCP server, TypeScript-native, 5-minute setup, auto-generates CLAUDE.md/AGENTS.md for AI assistants.

## MCP Tools Available

```
nx_docs          - Query Nx documentation
nx_available_plugins - List official Nx plugins (NOT installed by default)
```

**Key Insight**: MCP provides documentation lookup. Use **Nx CLI** for all operations.

## Core CLI Commands

### Project Graph Analysis

```bash
# View interactive project graph
nx graph

# JSON output for programmatic use
nx graph --file=output.json

# Show dependencies of specific project
nx graph --focus=my-app

# Show what depends on a project
nx graph --affected
```

### Affected Detection

```bash
# What's affected since main?
nx affected -t build
nx affected -t test
nx affected -t lint

# Compare against specific base
nx affected -t build --base=origin/main --head=HEAD

# Show affected projects only
nx show projects --affected
```

### Running Tasks

```bash
# Run task for all projects
nx run-many -t build
nx run-many -t test

# Run for specific projects
nx run-many -t build --projects=app-a,lib-b

# Run with parallelism control
nx run-many -t build --parallel=4

# Single project
nx build my-app
nx test my-lib
```

### Code Generation

```bash
# List available generators
nx list @nx/next
nx list @nx/react

# Generate new application
nx g @nx/next:app my-app
nx g @nx/react:app my-frontend

# Generate library
nx g @nx/js:lib shared-utils
nx g @nx/react:lib ui-components

# Dry run (preview)
nx g @nx/next:app my-app --dry-run
```

## Configuration Files

### nx.json (Workspace Config)

```json
{
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "cache": true
    },
    "test": {
      "cache": true
    },
    "lint": {
      "cache": true
    }
  },
  "namedInputs": {
    "default": ["{projectRoot}/**/*"],
    "production": ["default", "!{projectRoot}/**/*.spec.ts"]
  },
  "defaultBase": "main"
}
```

### project.json (Project Config)

```json
{
  "name": "my-app",
  "projectType": "application",
  "targets": {
    "build": {
      "executor": "@nx/next:build",
      "outputs": ["{options.outputPath}"],
      "options": {
        "outputPath": "dist/apps/my-app"
      }
    },
    "serve": {
      "executor": "@nx/next:server",
      "options": {
        "buildTarget": "my-app:build"
      }
    }
  }
}
```

## Caching

### Local Cache

```bash
# Cache is automatic for cacheable targets
nx build my-app  # First run: executes
nx build my-app  # Second run: cached (instant)

# Clear cache
nx reset
```

### Nx Cloud (Remote Cache)

```bash
# Connect to Nx Cloud
npx nx connect

# Or add manually
nx g @nx/workspace:ci-workflow

# Verify connection
nx run-many -t build
# Look for: "Remote cache hit"
```

### Cache Inputs

```json
// In project.json or nx.json
{
  "targets": {
    "build": {
      "inputs": [
        "default",
        "^production",
        { "externalDependencies": ["next"] }
      ]
    }
  }
}
```

## Common Patterns

### Adding a New App

```bash
# 1. Generate app
nx g @nx/next:app dashboard --directory=apps/dashboard

# 2. Verify in graph
nx graph --focus=dashboard

# 3. Build
nx build dashboard

# 4. Serve
nx serve dashboard
```

### Creating Shared Libraries

```bash
# UI library
nx g @nx/react:lib ui --directory=libs/shared/ui

# Utility library
nx g @nx/js:lib utils --directory=libs/shared/utils

# Domain library
nx g @nx/js:lib auth --directory=libs/domain/auth
```

### CI Pipeline (GitHub Actions)

```yaml
name: CI
on: [push, pull_request]

jobs:
  main:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: pnpm/action-setup@v2
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      # Affected-only builds
      - run: npx nx affected -t lint build test --base=origin/main
```

## Troubleshooting

### "Cannot find project"

```bash
# Regenerate project graph
nx reset
nx graph
```

### Cache Not Working

```bash
# Verify target is cacheable
cat nx.json | grep -A5 "targetDefaults"

# Check inputs are stable
nx build my-app --verbose
```

### Dependency Issues

```bash
# Show project dependencies
nx graph --focus=my-app

# Check for circular deps
nx graph --file=graph.json
# Review edges in JSON
```

## Quick Reference

| Task | Command |
|------|---------|
| Interactive graph | `nx graph` |
| Affected build | `nx affected -t build` |
| Run all tests | `nx run-many -t test` |
| Generate app | `nx g @nx/next:app name` |
| Generate lib | `nx g @nx/js:lib name` |
| Clear cache | `nx reset` |
| Show projects | `nx show projects` |
| List generators | `nx list @nx/next` |

## Related Skills

- **monorepo-workflow**: PR stacking, trunk-based development, code review
- **monorepo-team-lead**: CODEOWNERS, human-AI task routing, RFC process
