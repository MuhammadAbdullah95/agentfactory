---
sidebar_position: 6
title: "When Your Employee Needs a Coder"
description: "Watch your AI Employee delegate coding tasks to Claude Code, understand the PTY and background execution patterns, and see the Agent Factory thesis in action"
keywords:
  [
    coding-agent,
    claude code,
    agent delegation,
    pty mode,
    background execution,
    custom agent,
    general agent,
    multi-agent,
    openclaw,
  ]
chapter: 7
lesson: 6
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Agent Delegation"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can explain how a Custom Agent delegates coding tasks to a General Agent and describe the PTY execution pattern"

  - name: "Multi-Agent Coordination"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can trigger a coding-agent delegation via Telegram and monitor the background process"

learning_objectives:
  - objective: "Delegate a coding task from your AI Employee to Claude Code via Telegram"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student sends a coding request via Telegram and observes the delegation to Claude Code"

  - objective: "Explain the difference between PTY one-shot and background execution modes"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student can describe when to use each mode and explain the monitoring commands"

  - objective: "Connect the delegation pattern to the Agent Factory thesis from Chapter 1"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can explain how Custom Agents orchestrate General Agents, mapping to the Incubator vs Specialist model"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (coding-agent skill, PTY execution, background mode, delegation pattern) -- well within B1 range. Builds directly on L05 skills knowledge and Chapter 1 Agent Factory thesis."

differentiation:
  extension_for_advanced: "Set up parallel delegation using git worktree to have your employee dispatch multiple coding tasks simultaneously. Monitor all sessions and compare completion times."
  remedial_for_struggling: "Focus on the single one-shot delegation example. Skip background mode and parallel execution. The key concept is: employee delegates, coder executes."
---

# When Your Employee Needs a Coder

In Lesson 5, you created custom skills that made your AI Employee uniquely yours. Those skills handle text-based work -- meeting prep, research summaries, email drafts. But what happens when the task requires writing actual code? Your employee knows your projects, your preferences, your schedule. It does not know how to write a Python script, debug a React component, or set up a database migration. For that, it needs a specialist.

This is what any good manager does: delegate to someone with the right expertise. Your AI Employee is a Custom Agent -- it understands your context and orchestrates work. Claude Code (which you installed in Chapter 3) is a General Agent -- a specialist coder that can write, test, and debug software in any language. When your employee encounters a coding task, it spawns Claude Code with a focused brief, monitors the work, and returns the result to you on Telegram.

This is the Agent Factory thesis from Chapter 1, running live. Custom Agents manage. General Agents execute. Neither is complete without the other.

## Enabling the Coding-Agent Skill

Your AI Employee delegates coding through a built-in skill called `coding-agent`. This skill detects which coding agents are installed on your machine and uses whichever one is available.

### Supported Coding Agents

| Agent           | Command    | Best For                                                          |
| --------------- | ---------- | ----------------------------------------------------------------- |
| **Claude Code** | `claude`   | Full-featured coding with tool use, file editing, terminal access |
| **Codex CLI**   | `codex`    | OpenAI's coding agent, strong at multi-file refactoring           |
| **OpenCode**    | `opencode` | Model-agnostic, plugs into any LLM provider                       |
| **Pi**          | `pi`       | Minimal (4 tools, 300-word prompt), fast one-shot tasks           |

You already have Claude Code installed from Chapter 3. Confirm it is available:

```bash
claude --version
```

**Output:**

```
claude v1.x.x
```

If you see a version number, the coding-agent skill will automatically detect Claude Code and use it for delegation. No additional configuration needed -- the skill checks your PATH for available agents at runtime.

### Enabling the Skill

The coding-agent skill ships with OpenClaw. Verify it is active:

```
List your active skills
```

Send this to your employee on Telegram. You should see `coding-agent` in the list. If it does not appear, enable it:

```
Enable the coding-agent skill
```

**Output:**

```
Enabled skill: coding-agent
Available coding agents: claude (Claude Code)
```

---

## Hands-On: Delegate a Coding Task

Open Telegram. Send your employee a message that requires code:

```
Create a Python script called password_generator.py that generates
a random password. Requirements: 16 characters, mix of uppercase,
lowercase, digits, and symbols. Include a main block that prints
3 example passwords.
```

### What to Observe

Watch the response carefully. Your employee does not write the code itself. Instead, you see something like this:

```
Delegating to Claude Code...
Working in: ~/openclaw-workspace
Running: claude 'Create a Python script called password_generator.py...'
```

The employee passed your request to Claude Code as a one-shot command. Claude Code received the brief, created the file, and returned the result. Your employee then relays the output back to you on Telegram:

```
Done. Created password_generator.py

Generated passwords:
kR7#mP2xL9@nQ4wB
Yt5&dH8vF3!jA6sE
Wz1$cN4gM7*bK0rX
```

The file exists on your machine. Check it:

```bash
cat ~/openclaw-workspace/password_generator.py
```

**Output:**

```python
import random
import string

def generate_password(length: int = 16) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

if __name__ == "__main__":
    for i in range(3):
        print(generate_password())
```

### The Takeaway

Your employee did not learn Python. It delegated to a specialist that already knows Python. The employee's value is knowing **what you need** (a password generator for your project) and **who to ask** (Claude Code). This is the two-tier delegation pattern: the Custom Agent understands your context, the General Agent has the technical expertise.

---

## How Delegation Works Under the Hood

The coding-agent skill uses OpenClaw's bash tool with PTY (pseudo-terminal) mode. This is necessary because coding agents like Claude Code are interactive terminal applications -- they need a real terminal environment to work correctly. Without PTY, the output breaks.

### One-Shot Mode (Quick Tasks)

For tasks that complete in under a minute:

```
bash pty:true workdir:~/project command:"claude 'Your task here'"
```

| Parameter                | Purpose                                                                  |
| ------------------------ | ------------------------------------------------------------------------ |
| `pty:true`               | Creates a pseudo-terminal so the coding agent runs correctly             |
| `workdir:~/project`      | Sets the working directory -- the coding agent sees this project's files |
| `command:"claude '...'"` | The one-shot command passed to Claude Code                               |

The employee waits for completion, captures the output, and reports back on Telegram. Simple, synchronous, done.

### Background Mode (Long Tasks)

Some coding tasks take minutes -- refactoring a module, writing tests for an entire file, debugging a complex issue. For these, the employee runs the agent in the background:

```
bash pty:true workdir:~/project background:true command:"claude 'Refactor auth module'"
```

This returns immediately with a session ID:

```
Started background session: abc-12345
```

### Monitoring a Background Session

While the coding agent works, you can check on it:

**Check if it is still running:**

```
process action:poll sessionId:abc-12345
```

**Read the output so far:**

```
process action:log sessionId:abc-12345
```

**Output:**

```
[Claude Code] Reading auth.py...
[Claude Code] Found 3 functions to refactor...
[Claude Code] Rewriting validate_token()...
```

### Auto-Notify (No Polling Needed)

The best pattern avoids manual polling entirely. The coding-agent skill appends a completion trigger to the prompt:

```
When completely finished, run: openclaw system event --text "Done: [summary]" --mode now
```

This wakes your employee immediately when the coding agent finishes. Your employee then reads the final output and sends you a Telegram message:

```
Refactoring complete. Changed 3 functions in auth.py:
- validate_token(): Added expiry check
- refresh_token(): Fixed race condition
- create_token(): Added type hints

All existing tests pass.
```

You asked once. Your employee delegated, monitored, and reported -- all without you checking in.

---

## The Delegation Pattern

Step back and see what just happened:

```
You (Telegram) → Employee (Custom Agent) → Claude Code (General Agent) → Code
                                         ← Result ←                    ← Files
```

This is the two-tier model from Chapter 1's Agent Factory thesis:

| Role              | Type          | What It Knows                                      |
| ----------------- | ------------- | -------------------------------------------------- |
| **Your Employee** | Custom Agent  | Your projects, preferences, schedule, domain       |
| **Claude Code**   | General Agent | How to code in any language, debug, test, refactor |

Neither is sufficient alone. Claude Code can write excellent code, but it does not know which project you are working on, what your priorities are, or that you prefer functional style over object-oriented. Your employee knows all of that context, but it cannot write a line of code.

Together, they form a complete system: the manager who understands your needs and the specialist who has the skills to deliver. This is why Chapter 1 called it a "factory" -- you are not building one agent that does everything. You are assembling specialists managed by an agent that knows you.

### What Else Can Your Employee Delegate To?

The coding-agent skill is not locked to Claude Code. It works with whichever coding agent is on your PATH:

| If You Have Installed  | The Employee Uses                                    |
| ---------------------- | ---------------------------------------------------- |
| `claude` (Claude Code) | Full-featured coding with deep file understanding    |
| `codex` (Codex CLI)    | Strong at multi-file refactoring, requires git repo  |
| `opencode` (OpenCode)  | Model-agnostic -- use any LLM provider you prefer    |
| `pi` (Pi)              | Minimal and fast -- 4 tools, ideal for quick scripts |

The pattern stays the same regardless of which specialist is behind it. Your employee sends the brief, monitors the work, and reports the result. The specialist changes; the delegation pattern does not.

**Codex-specific note:** Codex CLI requires a git repository. If you delegate a task to a directory without one, the coding-agent skill creates a temporary repo automatically. For long-running Codex tasks, use `codex --full-auto` mode to avoid interactive prompts.

---

## Parallel Delegation with Git Worktrees

When your employee needs to fix three issues at once, it does not wait for them sequentially. It creates isolated workspaces using git worktrees and runs coding agents in parallel:

```bash
# Issue 1: fix login bug
git worktree add -b fix/issue-78 /tmp/issue-78 main
bash pty:true workdir:/tmp/issue-78 background:true command:"claude 'Fix login validation bug described in issue #78'"

# Issue 2: add tests
git worktree add -b test/auth /tmp/test-auth main
bash pty:true workdir:/tmp/test-auth background:true command:"claude 'Write unit tests for the auth module'"

# Issue 3: update docs
git worktree add -b docs/api /tmp/docs-api main
bash pty:true workdir:/tmp/docs-api background:true command:"claude 'Update API documentation for v2 endpoints'"
```

Each coding agent runs in its own branch, in its own directory, against the same codebase. No conflicts. No waiting. Your employee monitors all three sessions and reports as each completes.

This is advanced usage -- you do not need it today. But notice how the pattern scales: one employee managing multiple specialists working in parallel. That is a team, not a tool.

---

## What Transfers

The delegation pattern you just learned is not specific to OpenClaw. It is the architectural foundation of every multi-agent system:

| Concept                       | In OpenClaw                            | In Any Framework                              |
| ----------------------------- | -------------------------------------- | --------------------------------------------- |
| **Custom Agent manages**      | Your employee knows your context       | Orchestrator agent holds user preferences     |
| **General Agent executes**    | Claude Code writes code                | Specialist agent performs task                |
| **PTY execution**             | `bash pty:true` for terminal apps      | Process spawning with proper I/O              |
| **Background tasks**          | `background:true` + session monitoring | Async task execution + polling                |
| **Auto-notify on completion** | `openclaw system event`                | Callback/webhook on task finish               |
| **Parallel via isolation**    | Git worktrees                          | Separate workspaces, containers, or sandboxes |

When you move to Chapter 13 (building your own AI Employee), you will implement this exact pattern: a Custom Agent that knows your domain, delegating to General Agents that have technical skills. The employee you used in this chapter is your prototype. The one you build will be yours from the ground up.

---

## Try With AI

### Prompt 1 -- Delegation Decision Framework

```
I have an AI Employee (Custom Agent) that can delegate coding tasks
to Claude Code (General Agent). Help me create a decision framework:

For each of these task types, should my employee handle it directly
or delegate to a coding agent?

1. Summarize a meeting transcript
2. Write a Python web scraper
3. Draft a project status email
4. Debug a failing CI pipeline
5. Research competitor pricing
6. Refactor a 500-line module into smaller files
7. Generate a weekly report from CSV data
8. Set up a new Express.js API endpoint

Create a table with columns: Task, Handle Directly or Delegate,
Why, and Estimated Time Saved.
```

**What you're learning:** Judgment about when delegation adds value versus overhead. Not every task should go to a coding agent -- the latency of spawning a specialist only pays off when the task genuinely requires coding expertise. A good manager (human or AI) knows the difference between work they should do themselves and work they should hand off.

### Prompt 2 -- Multi-Agent Workflow Design

```
Design a workflow where my AI Employee coordinates between a coding
agent and itself to complete this task:

"Every Monday morning, pull the latest analytics data from our API,
generate a visualization dashboard in Python, and send me a summary
with the key metrics on Telegram."

Break this into steps. For each step, specify:
- Who does it (Employee or Coding Agent)
- What tool/skill they use
- What they pass to the next step
- What could go wrong

Then identify: which steps could run in parallel?
```

**What you're learning:** Multi-agent workflow design. Real productivity comes not from single delegations but from orchestrated workflows where different agents handle different parts of a pipeline. This prompt forces you to think about handoffs, data passing, error handling, and parallelization -- the same concerns that professional agent architects face when building production systems.

### Prompt 3 -- Human Manager vs AI Manager

```
Compare how a human engineering manager delegates coding tasks to
developers versus how an AI Employee delegates to Claude Code.

Create a comparison table covering:
- How they communicate the task
- How they provide context
- How they monitor progress
- How they handle mistakes
- How they learn from results

Then answer: What can the AI manager do that a human can't?
And what can the human manager do that the AI currently can't?
```

**What you're learning:** The boundaries of agent delegation. By comparing AI delegation to human delegation, you develop intuition for where agent systems excel (speed, consistency, parallelization) and where they fall short (judgment, relationship management, creative direction). This comparison will inform how you design your own AI Employee in Chapter 13 -- knowing the limits shapes what you build.
