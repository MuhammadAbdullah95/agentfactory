---
title: "Summary: Patterns That Transfer"
sidebar_label: "Summary"
sidebar_position: 6.5
---

# Summary: Patterns That Transfer

## The 6 Universal Patterns

The 6 patterns (Orchestration, I/O Adapters, State Isolation, Capability Packaging, Externalized Memory, Autonomous Invocation) were introduced in Lesson 4. Lesson 6 synthesizes why these specific 6 are essential -- remove any one and the system breaks in a specific, predictable way.

## What OpenClaw Proved vs Didn't Solve

**Proved**: Demand exists (200k stars), architecture is engineering not research, UX drives adoption more than features, MIT license unlocked community growth.

**Didn't solve**: Enterprise security (ClawHavoc showed exfiltration risks), governance (who reviews skills for safety?), reliability at scale (single-Gateway limits), cost control (500x variance per task), founder dependency (6,600+ commits from one person).

## Quick Reference: Cross-Framework Pattern Map

| Pattern               | OpenClaw         | Claude Code          | ChatGPT             | LangGraph         |
| --------------------- | ---------------- | -------------------- | ------------------- | ----------------- |
| Orchestration         | Gateway daemon   | CLI process          | API orchestrator    | StateGraph        |
| I/O Adapters          | Channels         | Terminal/MCP         | Web UI/API          | Input nodes       |
| State Isolation       | Sessions (JSONL) | Conversation context | Thread IDs          | State checkpoints |
| Capability Packaging  | SKILL.md         | SKILL.md             | Custom GPTs/Actions | Tool nodes        |
| Externalized Memory   | MEMORY.md + logs | CLAUDE.md + memory   | Memory feature      | State persistence |
| Autonomous Invocation | Cron + Heartbeat | Cron + hooks         | Scheduled actions   | Trigger nodes     |
