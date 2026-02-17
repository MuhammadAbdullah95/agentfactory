---
title: "Summary: Teaching Skills & Staying Safe"
sidebar_label: "Summary"
sidebar_position: 5.5
---

# Summary: Teaching Skills & Staying Safe

## Key Concepts

- **SKILL.md**: A directory containing a Markdown file with YAML frontmatter (`name`, `description`) plus structured instructions -- no SDK, no compilation, just text that encodes portable expertise
- **Build Your Own Skill**: 5-step exercise (choose task, write frontmatter, write instructions, add output/error handling, test and iterate) that produces a working skill for your domain
- **Skill Design Principles**: Specific activation, step-by-step instructions, defined output format, error handling, single responsibility
- **ClawHavoc**: Coordinated campaign of 335 malicious skills deploying Atomic Stealer (AMOS) via fake prerequisite error messages on ClawHub
- **CVE-2026-25253**: Critical (CVSS 8.8) WebSocket origin bypass enabling one-click remote code execution on OpenClaw instances
- **Lethal Trifecta**: Private data access + untrusted content + external communication in a single process -- the fundamental, unsolvable architectural tension in all agent systems

## Security Checklist

1. **Never bind to 0.0.0.0** -- exposes your agent to the entire internet
2. **Always read skills before installing** -- 12% of ClawHub was malicious
3. **Use Gateway authentication token** -- prevents unauthorized WebSocket connections
4. **Keep OpenClaw updated** -- security patches ship for known vulnerabilities
5. **Enable sandboxing for untrusted skills** -- isolates tool execution from your host
6. **Never store secrets in skill instructions** -- skill text passes through LLM context in plaintext

## Common Mistakes

- Installing community skills without reading every line of the SKILL.md
- Binding to `0.0.0.0` for remote access convenience (135,000+ instances were exposed)
- Trusting marketplace rankings as a proxy for safety (the #1 ranked skill was malware)
- Writing vague skill descriptions that cause unpredictable activation
- Skipping error handling in skills (causes hallucination on failure)

## Quick Reference

```markdown
---
name: lowercase-hyphenated
description: One clear sentence explaining when to activate
---

# Skill Title

Step-by-step instructions for the LLM.

## Output Format

Where and how to save results.

## Error Handling

What to do when things go wrong.
```
