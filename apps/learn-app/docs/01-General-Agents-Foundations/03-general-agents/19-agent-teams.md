---
sidebar_position: 19
title: "Agent Teams: Orchestrating Multiple Claude Sessions"
description: "Create and coordinate teams of Claude Code instances for parallel research, code review, and feature development"
keywords:
  [
    agent teams,
    multi-agent,
    teamcreate,
    task list,
    delegation,
    parallel work,
    claude code,
  ]
chapter: 3
lesson: 19
duration_minutes: 90

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration)"
layer_1_foundation: "N/A"
layer_2_collaboration: "Creating agent teams, assigning tasks, coordinating parallel work, applying delegate mode and plan approval"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Team Orchestration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital-Content-Creation"
    measurable_at_this_level: "Student can create an agent team, assign tasks, message teammates, and use delegate mode to coordinate parallel work"

  - name: "Parallel Work Design"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can determine when to use agent teams vs subagents and design task breakdowns that minimize file conflicts"

  - name: "Team Communication"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Communication-Collaboration"
    measurable_at_this_level: "Student can send targeted messages, use broadcast sparingly, manage teammate lifecycle including shutdown"

learning_objectives:
  - objective: "Create and manage an agent team with shared task list and inter-agent communication"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates a 3-agent team, assigns tasks, and coordinates completion of a parallel code review"
  - objective: "Apply the subagent vs agent team decision framework to real scenarios"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student correctly identifies 3 scenarios suited for teams and 3 suited for subagents with reasoning"
  - objective: "Use delegate mode, plan approval, and quality hooks to control team behavior"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student configures delegate mode, requires plan approval for one teammate, and uses TeammateIdle hook"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (TeamCreate, shared task list, inter-agent messaging, delegate mode) - builds on subagent knowledge from L11, within B1 limit of 10"

differentiation:
  extension_for_advanced: "Configure TeammateIdle and TaskCompleted hooks to enforce quality gates on team output"
  remedial_for_struggling: "Start with Lab 1 only (2-agent team) before attempting the full 3-agent parallel review"

# Generation metadata
generated_by: "content-implementer v1.0.0"
created: "2026-02-10"
git_author: "Claude Code"
version: "1.0.0"

prerequisites:
  - "Lesson 11: Subagents and Orchestration (context isolation, delegation model)"
  - "Lesson 15: Hooks and Extensibility (event-driven automation)"
---

# Agent Teams: Orchestrating Multiple Claude Sessions

You just finished a 200-line pull request. You ask Claude to review it. It checks security, finds one issue, moves on to test coverage, then gets to performance. By the time it reaches the performance analysis, the security findings are buried in the conversation. Context is degrading. The review is shallow because one agent is doing three jobs.

What if three separate Claude instances could review simultaneously -- one dedicated to security, one to performance, one to test coverage -- each with a fresh, focused context window? And what if those three reviewers could then _discuss_ their findings with each other, debating whether a security fix would hurt performance, before delivering a unified report?

That is Agent Teams. Where subagents (Lesson 11) are fire-and-forget workers that report back to a single caller, Agent Teams are fully independent Claude Code instances that coordinate through a shared task list and direct messaging. Each teammate has its own context window, can message any other teammate, and self-coordinates work.

---

## Enable Agent Teams

Agent Teams is an experimental feature. Add this to your VS Code `settings.json` or Claude Code settings:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

**Verify it worked**: Start a new Claude Code session and type a prompt that requests a team. If the feature is enabled, you will see Claude creating teammates instead of subagents.

**A note on "experimental"**: The patterns you learn here -- task decomposition, parallel coordination, role assignment -- are fundamental to multi-agent systems. The specific API may evolve, but the thinking transfers.

---

## Lab 1: Your First Team

Let's create a 2-agent team. Open Claude Code in any project with at least a few files and type:

```
Create an agent team to investigate this project from two angles:
- One teammate examines the testing patterns (what's tested, what's missing, test quality)
- One teammate examines error handling (try/catch patterns, error messages, edge cases)
Have them share findings with each other before giving me the summary.
```

### What Happens (Watch Carefully)

1. **Claude creates the team.** You will see a team lead (your main session) and two teammates spawn. Each teammate gets its own context window.

2. **Tasks appear.** Press **Ctrl+T** to view the shared task list. You will see tasks assigned to each teammate.

3. **Teammates work independently.** Each teammate reads files, analyzes patterns, and builds findings -- all in its own isolated context. No context pollution between them.

4. **Navigate between teammates.** Use **Shift+Up** and **Shift+Down** to switch your view between the lead and each teammate. Watch them work in real time.

5. **Teammates message each other.** This is the key difference from subagents. The testing teammate might message the error-handling teammate: "I found untested error paths in auth.js -- did you see error handling there?" They discuss directly, without routing through the lead.

6. **Lead synthesizes.** Once both teammates finish, the lead reads their findings and produces a combined report.

### What to Notice

- Each teammate's conversation is clean and focused (no context from the other teammate's work)
- The shared task list shows progress without teammates needing to report status manually
- Inter-agent messages let teammates build on each other's findings

**Try it now.** Run the prompt above and observe each step.

---

## Subagents vs Agent Teams: The Decision

You already know subagents from Lesson 11. When should you use teams instead?

| Scenario                             | Subagents                             | Agent Teams                                    |
| ------------------------------------ | ------------------------------------- | ---------------------------------------------- |
| "Review this file for bugs"          | Use this. Focused, result-only.       | Overkill for one task.                         |
| "Review this PR from 3 angles"       | Too limited. Reviewers can't discuss. | Use this. Parallel perspectives that converge. |
| "Research 5 libraries and summarize" | Use this. Each returns a summary.     | Only if they need to compare findings.         |
| "Build frontend + backend + tests"   | Can't coordinate across layers.       | Use this. Each owns their layer, they sync.    |
| "Fix this one failing test"          | Use this. Quick and cheap.            | Way too expensive for one task.                |
| "Investigate a bug from 3 theories"  | Can't debate competing theories.      | Use this. Teammates disprove each other.       |

**The decision rule**: If teammates need to talk to each other, use teams. If they just need to report back, use subagents.

### Cost Consideration

Agent teams use more tokens than subagents because each teammate maintains its own full context window plus inter-agent messages. A 3-agent team review might cost 3-5x what a single-agent review costs. Use teams when the quality improvement justifies the cost.

---

## Lab 2: Parallel Code Review

This is the flagship exercise. You will run a real 3-agent parallel code review.

**Prerequisites**: You need a project with some code to review. Your own project works best, or clone any small open-source project.

Type this prompt:

```
Create an agent team to review the code in this project. Spawn three reviewers:

- Security reviewer: Check for vulnerabilities, input validation gaps,
  hardcoded secrets, injection risks, and auth issues.
- Performance reviewer: Check for N+1 queries, unnecessary allocations,
  missing caching opportunities, and algorithmic inefficiencies.
- Test reviewer: Check for coverage gaps, missing edge case tests,
  test quality issues, and fragile test patterns.

Each reviewer should work independently on the full codebase, then share
their top 3 findings with the other reviewers. After discussion, produce
a unified review report ranked by severity.
```

### Step-by-Step Walkthrough

**Step 1: Team Creation.** Claude creates a team lead and three teammates. The lead builds the task list and assigns review domains.

**Step 2: Watch the task list.** Press **Ctrl+T** periodically. You will see tasks transition from `todo` to `in_progress` to `done` as each reviewer works.

**Step 3: Navigate between reviewers.** Use **Shift+Up** / **Shift+Down** to watch each reviewer work. Notice how the security reviewer focuses entirely on attack surfaces while the performance reviewer focuses entirely on efficiency. Each has full context dedicated to their specialty.

**Step 4: Inter-agent discussion.** After initial reviews, watch teammates exchange messages. The security reviewer might flag that a function lacks input validation, and the test reviewer might respond: "I noticed that function has no tests at all -- adding validation tests would catch both issues." This cross-pollination is impossible with subagents.

**Step 5: Unified report.** The lead collects all findings, resolves conflicts (when the performance fix contradicts the security recommendation), and produces a single ranked report.

### Compare the Results

After the team review completes, try the same review with a single agent:

```
Review the code in this project for security vulnerabilities, performance
issues, and test coverage gaps. Produce a report ranked by severity.
```

Compare the depth and coverage. The team review typically catches more issues because each reviewer had a full context window dedicated to one concern, rather than one agent splitting attention across three domains.

---

## Controlling Your Team

Once you can create teams, the next skill is controlling their behavior. Each technique below includes a prompt you should try.

### Delegate Mode (Shift+Tab)

Delegate mode prevents the team lead from implementing anything directly. The lead can only coordinate: create tasks, send messages, review results. All implementation goes to teammates.

**When to use it**: Complex tasks where you want the lead to stay strategic instead of getting pulled into implementation details.

**Try it now**:

1. Press **Shift+Tab** to toggle delegate mode ON
2. Type this prompt:

```
I need you to refactor the utility functions in this project.
Create teammates to handle each file. You coordinate and review
their work, but do not edit any files yourself.
```

3. Watch the lead create tasks and assign them to teammates without touching any files itself
4. Press **Shift+Tab** again to toggle delegate mode OFF when done

### Plan Approval

You can require a teammate to plan before implementing. The teammate works in read-only mode, creates a plan, and waits for the lead to approve before making any changes.

**Try it now**:

```
Create a teammate to refactor the authentication module.
Require plan approval before they make any changes -- I want to
review their approach first.
```

Watch the flow:

1. Teammate reads the codebase (read-only)
2. Teammate produces a plan
3. Lead receives the plan for review
4. You (through the lead) approve or reject with feedback
5. Only after approval does the teammate begin implementation

### Direct Messages

You can send targeted messages to individual teammates to redirect their work mid-task.

**Try it now**: During a team session, use **Shift+Up** / **Shift+Down** to select a specific teammate, then type a message:

```
Skip the UI layer for now and focus only on the database queries.
I'll have another teammate handle the UI.
```

The teammate receives your message and adjusts its work accordingly. Other teammates are not interrupted.

### Task Dependencies

Tasks can depend on other tasks using `blockedBy` relationships. A blocked task will not start until its dependency completes.

**Try it now**:

```
Create a team to update the API. Set up these tasks with dependencies:
1. Design the new API schema (no dependencies)
2. Update the backend endpoints (blocked by task 1)
3. Update the frontend API calls (blocked by task 2)
4. Write integration tests (blocked by tasks 2 and 3)

Assign each task to a different teammate. They should self-coordinate
based on the dependency chain.
```

Watch tasks unblock automatically as their dependencies complete. Teammates claim unblocked tasks without being told.

---

## Quality Hooks for Teams

Lesson 15 introduced hooks for single-agent workflows. Two hook events are designed specifically for teams.

### TeammateIdle: Keep Teammates Working

When a teammate runs out of tasks and goes idle, this hook fires. You can use it to assign more work or check if there are remaining tasks.

```json
{
  "hooks": {
    "TeammateIdle": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/check-remaining-tasks.sh"
          }
        ]
      }
    ]
  }
}
```

**The hook script** (`.claude/hooks/check-remaining-tasks.sh`):

```bash
#!/usr/bin/env bash
# Check if there are remaining tasks for idle teammates

INPUT=$(cat)
TEAMMATE=$(echo "$INPUT" | jq -r '.teammate_name // "unknown"')

# Check if the project still has TODO items
REMAINING=$(grep -r "TODO\|FIXME\|HACK" src/ 2>/dev/null | wc -l)

if [ "$REMAINING" -gt 0 ]; then
  echo "There are $REMAINING TODO/FIXME items remaining in src/. Pick one up."
  exit 2  # Exit code 2 = send feedback, keep working
fi

exit 0  # Exit code 0 = allow idle
```

Exit code `2` sends the stdout message as feedback and keeps the teammate working. Exit code `0` allows the teammate to go idle normally.

### TaskCompleted: Quality Gate

When a teammate marks a task as done, this hook fires before the task is accepted. You can use it to enforce quality standards.

```json
{
  "hooks": {
    "TaskCompleted": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/verify-task-quality.sh"
          }
        ]
      }
    ]
  }
}
```

**The hook script** (`.claude/hooks/verify-task-quality.sh`):

```bash
#!/usr/bin/env bash
# Verify task quality before accepting completion

INPUT=$(cat)
TASK_DESC=$(echo "$INPUT" | jq -r '.task_description // "unknown"')

# Run tests to verify nothing broke
npm test --silent 2>&1
TEST_EXIT=$?

if [ $TEST_EXIT -ne 0 ]; then
  echo "Tests are failing. Fix the failing tests before marking this task complete."
  exit 2  # Exit code 2 = reject completion, send feedback
fi

exit 0  # Exit code 0 = accept completion
```

**Try it now**: Add both hooks to your `.claude/settings.json`, then run a team task and observe how the hooks enforce quality automatically.

---

## When Teams Go Wrong (And How to Fix It)

Teams are powerful but introduce coordination complexity. Here are the common failure modes and their fixes.

### Problem 1: Lead Implements Instead of Delegating

**Symptom**: The lead starts editing files directly instead of assigning work to teammates.

**Fix**: Enable delegate mode (**Shift+Tab**) or include explicit instructions:

```
You are the team lead. NEVER edit files directly. Create tasks and
assign them to teammates. Your job is coordination and review only.
```

### Problem 2: Teammates Editing the Same File

**Symptom**: Git conflicts or overwritten changes because two teammates touched the same file.

**Fix**: Assign file ownership explicitly in your prompt:

```
IMPORTANT: Assign files clearly so no teammate touches another's files.
- Frontend teammate ONLY touches: src/components/, src/pages/
- Backend teammate ONLY touches: src/api/, src/services/
- Test teammate ONLY touches: tests/
```

### Problem 3: Teammate Lost Context

**Symptom**: A teammate does not know about project conventions or architecture decisions.

**Fix**: Teammates do NOT inherit the lead's conversation history. Include critical context in the spawn prompt or ensure your `CLAUDE.md` file contains the necessary information (teammates DO read project context files).

### Problem 4: Token Costs Are Too High

**Symptom**: A team review costs significantly more than expected.

**Fix**: Use a more efficient model for teammates while keeping the lead on the most capable model. Configure this in your team creation prompt:

```
Create a team where the lead uses Opus and teammates use Sonnet.
The teammates do the bulk analysis work, and the lead synthesizes.
```

### Problem 5: Tasks Stuck as In-Progress

**Symptom**: A task stays `in_progress` even though the teammate appears to have finished.

**Fix**: Check the teammate's view (**Shift+Up/Down**). The teammate may be waiting for a response or stuck in a loop. Send a direct message to redirect or unstick it.

---

## Real-World Patterns

These three patterns cover the most common team use cases. Each includes a prompt you can adapt to your projects.

### Pattern 1: Parallel Investigation

When a problem could have multiple root causes, send investigators down each path simultaneously.

```
Users report that search is slow. Create a team with 3 investigators:
- Database investigator: analyze queries in src/db/ for missing indexes,
  N+1 patterns, and slow joins
- API investigator: analyze endpoints in src/api/ for unnecessary
  processing, missing caching, and serialization overhead
- Frontend investigator: analyze components in src/pages/ for excessive
  re-renders, large payloads, and missing pagination

Each investigator should share their top finding with the others.
Converge on the most likely root cause with evidence.
```

### Pattern 2: Feature Build

When a feature spans multiple layers, assign one teammate per layer with explicit file ownership.

```
Create a team to build the user settings page:
- Frontend teammate: build components in src/components/settings/ and
  page in src/pages/settings.tsx
- Backend teammate: create API endpoints in src/api/settings/ and
  validation schemas in src/schemas/
- Test teammate: write unit tests in tests/unit/settings/ and
  integration tests in tests/integration/settings/

Dependencies:
- Backend completes API schema first (task 1)
- Frontend and tests start after API schema is done (tasks 2, 3)
- Integration tests run after both frontend and backend are complete (task 4)
```

### Pattern 3: Competing Hypotheses

When you are not sure what the right approach is, have teammates argue for different solutions.

```
We need to add real-time notifications to the app. Spawn 3 teammates,
each advocating for a different approach:
- Teammate 1: Argue for WebSockets. Research implementation complexity,
  scaling concerns, and browser support.
- Teammate 2: Argue for Server-Sent Events. Research same dimensions.
- Teammate 3: Argue for polling with long-poll fallback.

Each teammate should try to find weaknesses in the other approaches.
After discussion, the lead produces a recommendation with rationale.
```

---

### What's Next

You have learned to coordinate multiple Claude instances as a team. Lesson 20 introduces **Claude Cowork** -- the desktop-based version of Claude's agentic AI. Where Agent Teams give you parallel power in the terminal, Cowork brings agentic capabilities to knowledge workers who prefer a visual interface.

---

## Try With AI

**Create a Review Team:**

> "Create an agent team with 2 teammates to review this project from different angles. Teammate 1 focuses on code quality and maintainability. Teammate 2 focuses on security and error handling. Have them discuss findings before producing a combined report."

**What you're learning:** How to structure team roles so work does not overlap. Each teammate has a clear domain, and the discussion phase catches issues that span both domains.

**Delegate and Control:**

> "I want you to ONLY coordinate, never implement directly. Create a team of 3 to refactor the utils/ directory. One teammate per file. Require plan approval before any changes. Each teammate must run tests after their refactor."

**What you're learning:** How delegate mode plus plan approval gives you maximum control over team behavior while still parallelizing the work. This is the pattern for high-stakes refactoring where you want human review at every stage.

**Apply to Your Domain:**

> "Think about a complex task in [your field] that would benefit from parallel investigation. It could be researching a market from multiple angles, auditing a system from different perspectives, or building something with independent components. Design an agent team with 3-4 specialists. Describe each teammate's role, what they investigate, and how they share findings. Then create the team and run it."

**What you're learning:** Applying team orchestration to your own professional domain. The ability to decompose a problem into parallel workstreams and coordinate independent specialists is a skill that extends far beyond code review.
