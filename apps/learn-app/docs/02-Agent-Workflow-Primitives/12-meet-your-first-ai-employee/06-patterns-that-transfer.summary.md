---
title: "Summary: Patterns That Transfer"
sidebar_label: "Summary"
sidebar_position: 6.5
---

# Summary: Patterns That Transfer

## The 6 Universal Patterns

| # | Pattern | Without It |
|---|---------|------------|
| 1 | **Orchestration Layer** | Nothing routes messages; the agent cannot receive work |
| 2 | **I/O Adapters** | Locked to one channel; adding another means rewriting the agent |
| 3 | **State Isolation** | Conversations contaminate each other; multi-user is impossible |
| 4 | **Capability Packaging** | New abilities require core code changes; the agent becomes brittle |
| 5 | **Externalized Memory** | Everything forgotten between sessions; no learning across days |
| 6 | **Autonomous Invocation** | Agent only responds when prompted; cannot monitor, alert, or schedule |

## What OpenClaw Proved vs Didn't Solve

**Proved**: Demand exists (199k stars), architecture is engineering not research, UX drives adoption more than features, MIT license unlocked community growth.

**Didn't solve**: Enterprise security (ClawHavoc showed exfiltration risks), governance (who reviews skills for safety?), reliability at scale (single-Gateway limits), cost control (500x variance per task), founder dependency (6,600+ commits from one person).

## Quick Reference: Cross-Framework Pattern Map

| Pattern | OpenClaw | Claude Code | ChatGPT | LangGraph |
|---------|----------|-------------|---------|-----------|
| Orchestration | Gateway daemon | CLI process | API orchestrator | StateGraph |
| I/O Adapters | Channels | Terminal/MCP | Web UI/API | Input nodes |
| State Isolation | Sessions (JSONL) | Conversation context | Thread IDs | State checkpoints |
| Capability Packaging | SKILL.md | SKILL.md | Custom GPTs/Actions | Tool nodes |
| Externalized Memory | MEMORY.md + logs | CLAUDE.md + memory | Memory feature | State persistence |
| Autonomous Invocation | Cron + Heartbeat | Cron + hooks | Scheduled actions | Trigger nodes |
