---
title: "Summary: When Your Employee Needs a Coder"
sidebar_label: "Summary"
sidebar_position: 6.5
---

# Summary: When Your Employee Needs a Coder

## Key Concepts

- Your AI Employee is a **Custom Agent** that understands your context (projects, preferences, schedule) but cannot write code
- When coding is needed, it delegates to a **General Agent** like Claude Code, Codex, OpenCode, or Pi
- The `coding-agent` skill auto-detects which coding agents are available on your PATH
- **PTY mode** (`pty:true`) is required because coding agents are interactive terminal applications
- **One-shot mode** handles quick tasks synchronously -- employee waits for completion
- **Background mode** (`background:true`) handles long tasks -- employee monitors via session ID
- **Auto-notify** eliminates polling: the coding agent triggers an event when finished
- **Git worktrees** enable parallel delegation -- multiple coding agents working on separate branches simultaneously
- This is the **Agent Factory thesis** from Chapter 1 in action: Custom Agents manage, General Agents execute

## Delegation Commands Quick Reference

| Command                                                                   | Purpose                                          |
| ------------------------------------------------------------------------- | ------------------------------------------------ |
| `bash pty:true workdir:~/project command:"claude 'task'"`                 | One-shot delegation (waits for result)           |
| `bash pty:true workdir:~/project background:true command:"claude 'task'"` | Background delegation (returns session ID)       |
| `process action:poll sessionId:XXX`                                       | Check if background session is still running     |
| `process action:log sessionId:XXX`                                        | Read output from background session              |
| `process action:kill sessionId:XXX`                                       | Terminate a background session                   |
| `openclaw system event --text "Done: summary" --mode now`                 | Auto-notify on completion (appended to prompt)   |
| `git worktree add -b branch /tmp/workspace main`                          | Create isolated workspace for parallel execution |

## Supported Coding Agents

| Agent       | Command    | Notes                                               |
| ----------- | ---------- | --------------------------------------------------- |
| Claude Code | `claude`   | Full-featured, installed in Chapter 3               |
| Codex CLI   | `codex`    | Requires git repo, use `--full-auto` for background |
| OpenCode    | `opencode` | Model-agnostic, works with any LLM provider         |
| Pi          | `pi`       | Minimal (4 tools), fast for one-shot scripts        |

## The Two-Tier Model

```
You (Telegram) --> Employee (Custom Agent) --> Claude Code (General Agent) --> Code
                                            <-- Result <--                  <-- Files
```

## Common Mistakes

- Forgetting `pty:true` -- coding agents hang or produce broken output without a pseudo-terminal
- Delegating simple text tasks to a coding agent -- adds latency with no benefit (employee should handle directly)
- Not using `background:true` for long tasks -- blocks your employee from handling other messages while waiting
- Forgetting to clean up git worktrees after parallel execution -- `git worktree remove /tmp/workspace`
- Assuming your employee wrote the code -- it delegated; the coding agent did the work
