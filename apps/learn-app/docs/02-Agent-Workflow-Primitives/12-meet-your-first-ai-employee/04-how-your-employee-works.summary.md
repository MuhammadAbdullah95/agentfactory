---
title: "Summary: How Your Employee Works"
sidebar_label: "Summary"
sidebar_position: 4.5
---

# Summary: How Your Employee Works

## Key Concepts
- **Gateway**: Central daemon that routes all messages, manages sessions, authenticates users, loads skills, and coordinates the queue.
- **Channels**: I/O adapters (Telegram, WhatsApp, Discord, 30+) that normalize platform-specific messages into a common format.
- **Sessions**: Isolated per-conversation state stored as append-only JSONL files with auto-compaction for long conversations.
- **Agent Loop**: The 6-phase cycle (ingestion, access control, context assembly, model invocation, tool execution, response delivery) that processes every request.
- **Lane Queue**: FIFO concurrency control serializing runs per-session (1), capping main parallelism (4) and subagent parallelism (8).
- **Memory**: Three layers -- curated MEMORY.md, daily append-only logs, and vector search for semantic recall beyond the context window.
- **Skills**: Portable SKILL.md directories with YAML frontmatter, progressively disclosed (name/description at start, full content on invocation).

## Universal Pattern Map

| Pattern | What It Solves |
|---|---|
| **Orchestration** | Central coordinator for all components |
| **I/O Adapters** | Normalizes diverse communication sources |
| **State Isolation** | Prevents data leakage between users/conversations |
| **Capability Packaging** | Makes abilities teachable, composable, portable |
| **Externalized Memory** | Persists knowledge beyond the context window |
| **Concurrency Control** | Prevents race conditions and resource conflicts |

Bonus: **Autonomous Invocation** (cron/heartbeat) separates an AI Employee from an AI tool.

## Common Mistakes
- Skipping concurrency control -- two parallel runs on the same session corrupt state.
- Loading full skill content upfront instead of using progressive disclosure (wastes tokens).
- Sharing session state across users (breaks state isolation, leaks private data).

## Quick Reference
These 6 patterns appear in every agent framework (OpenClaw, Claude Code, CrewAI, LangGraph). The names change; the engineering necessities do not. Master them once, recognize them everywhere.
