---
title: "Summary: Your Employee Orchestrating Agents"
sidebar_label: "Summary"
sidebar_position: 6.5
---

# Summary: Your Employee Orchestrating Agents

## Key Concepts

- Your AI Employee is a **Custom Agent** that understands your context (projects, preferences, schedule)
- When tasks need specialist capabilities, it delegates to a **General Agent** like Claude Code
- Delegation is **invisible** -- the employee decides when, how, and to which agent to delegate
- The **two-tier delegation pattern**: Custom Agent manages context, General Agent executes tasks
- Neither agent is sufficient alone: the employee has context but needs capability; the specialist has capability but lacks context
- This is the **Agent Factory thesis** from Chapter 1 running live

## The Two-Tier Model

```
You (Telegram) → Employee (Custom Agent) → General Agent → Result
                                         ← Files/Reports ←
```

| Role              | Type          | What It Knows                                          |
| ----------------- | ------------- | ------------------------------------------------------ |
| **Your Employee** | Custom Agent  | Your projects, preferences, schedule, domain           |
| **Claude Code**   | General Agent | Research, file operations, analysis, document creation |

## Common Mistakes

- Micro-managing the delegation (your employee handles this internally -- just ask for results)
- Delegating simple tasks that don't need a specialist (adds latency with no benefit)
- Not reviewing the output (delegation doesn't mean blind trust)
- Assuming you need to configure delegation manually (the employee decides automatically)

## What Transfers

| Concept                 | In OpenClaw                    | In Any Framework                    |
| ----------------------- | ------------------------------ | ----------------------------------- |
| Custom Agent manages    | Employee knows your context    | Orchestrator holds user preferences |
| General Agent executes  | Claude Code performs tasks     | Specialist agent performs task      |
| Delegation is invisible | Employee decides internally    | Orchestrator routes to best agent   |
| Parallel execution      | Multiple agents simultaneously | Async task execution                |
