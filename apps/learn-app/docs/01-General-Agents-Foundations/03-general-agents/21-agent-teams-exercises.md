---
title: "Agent Teams Exercises: Team Creation, Task Coordination, and Multi-Agent Workflows"
sidebar_label: "Agent Teams Exercises"
sidebar_position: 21
chapter: 3
lesson: 21
duration_minutes: 90

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Hands-on practice applying Lesson 20 agent teams concepts through 10 guided exercises"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Team Orchestration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student creates agent teams, assigns tasks with dependencies, and coordinates multi-agent workflows"
  - name: "Multi-Agent Debugging"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student diagnoses broken team configurations, circular dependencies, and hook failures"

learning_objectives:
  - objective: "Create and coordinate agent teams with task dependencies and message routing"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Modules 1-2 exercises"
  - objective: "Debug multi-agent coordination failures including circular dependencies, ownership errors, and misconfigured hooks"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Exercises 1.2, 2.2, 3.2"
  - objective: "Design quality hooks that enforce standards across team workflows"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Module 3 exercises and capstones"

cognitive_load:
  new_concepts: 2
  assessment: "2 concepts (team debugging patterns, hook-based quality gates) -- within B1 limit. Exercises reinforce existing Lesson 20 knowledge."

differentiation:
  extension_for_advanced: "Complete both capstones; Capstone B applies agent teams to a professional domain of student's choice"
  remedial_for_struggling: "Start with Module 1 only; use the starter prompts provided"
---

# Agent Teams Exercises: Team Creation, Task Coordination, and Multi-Agent Workflows

You've learned to create agent teams with TeamCreate, coordinate tasks with dependencies using TaskCreate and TaskUpdate, communicate between agents with SendMessage, and set up hooks that fire when teammates go idle or complete tasks. Each of these capabilities extends Claude Code from a single-agent tool into a multi-agent orchestration platform. But orchestrating multiple agents introduces failure modes that don't exist with a single agent -- circular dependencies that deadlock your pipeline, tasks assigned to agents that don't exist, and hooks that silently fail while your team runs up API costs.

These 10 exercises are designed to build your **team orchestration**, **multi-agent debugging**, and **hook design** skills through hands-on practice. Modules 1-3 each contain two exercises: a **hands-on** exercise where you build or configure something real, and a **debug** exercise where you diagnose and fix something broken. Two capstones at the end combine everything into complete multi-agent workflows.

:::info Experimental Feature
Agent Teams requires an environment variable to enable:
```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```
Set this before starting any exercise. Without it, team-related tools (TeamCreate, SendMessage, etc.) will not be available.
:::

:::info Download Exercise Files
**[Download Agent Teams Exercises (ZIP)](https://github.com/panaversity/claude-code-agent-teams-exercises/releases/latest/download/agent-teams-exercises.zip)**

After downloading, unzip the file. Each exercise has its own folder with an `INSTRUCTIONS.md` and any starter files you need.

If the download link doesn't work, visit the [repository releases page](https://github.com/panaversity/claude-code-agent-teams-exercises/releases) directly.
:::

:::caution API Costs
Agent Teams exercises have higher API costs than single-agent exercises because each teammate is a separate Claude instance. The exercise guide inside the ZIP provides budget-friendly paths -- start with Module 1 to calibrate costs before tackling larger exercises. Capstone A (3-agent parallel code review) will use roughly 3x the tokens of a single-agent session.
:::

---

## How to Use These Exercises

**Start the exercises after finishing Lesson 20:**

| After Lesson...          | Do Module...                                |
| ------------------------ | ------------------------------------------- |
| Lesson 20: Agent Teams   | **Modules 1-3:** All exercises              |
| All of the above         | **Module 4:** Capstones                     |

The workflow for every exercise is the same:

1. **Open the exercise folder** from the `claude-code-agent-teams-exercises/` directory
2. **Read the INSTRUCTIONS.md** inside the folder -- it has setup steps and starter files
3. **Read the walkthrough below** for context on what you're practicing and why
4. **Start Claude Code** and point it at the exercise folder
5. **Work through the exercise** -- write your own prompts, don't just copy the starter
6. **Reflect** using the questions provided -- this is where the real learning happens

---

## Tool Guide

- Claude Code -- Terminal-based, required for all agent team exercises. Agent teams operate through the terminal using TeamCreate, TaskCreate, TaskUpdate, SendMessage, and related tools.

Agent teams are a terminal-only feature. Cowork does not support multi-agent team orchestration.

---

## The Team Orchestration Workflow

Use this for every exercise:

1. **Design** -- What agents do you need? What does each one own?
2. **Create** -- Set up the team with TeamCreate and spawn teammates
3. **Coordinate** -- Create tasks with dependencies using TaskCreate and TaskUpdate
4. **Communicate** -- Use SendMessage for DMs and broadcasts
5. **Monitor** -- Watch for idle notifications and task completions
6. **Validate** -- Verify all tasks completed and outputs are correct

This workflow mirrors real multi-agent orchestration: before spawning agents, design the team structure. After spawning, coordinate through tasks and messages rather than micromanaging each agent's work.

---

## Module 1: Team Fundamentals

> **Core Skill:** Creating teams, spawning teammates, and navigating team structure

### Exercise 1.1 -- Create and Navigate a Team (Hands-on)

**The Problem:**
Open the `module-1-team-fundamentals/exercise-1.1-create-team/` folder. You'll find a 6-file Node.js project (`package.json`, `routes.js`, `db.js`, and others) with several issues including a missing `package-lock.json`. The project needs a code review, but doing it alone means switching context between routes, database logic, and configuration.

**Your Task:**
Create an agent team with 3 teammates: one to review routes, one to review database code, and one to review configuration. Use TeamCreate to set up the team, spawn teammates, create tasks for each reviewer, and assign them. Verify the team structure by reading the team config file.

**What You'll Learn:**

- How TeamCreate initializes a team with config and task directories
- How spawning teammates creates agents that can receive tasks
- That team structure is stored in files you can inspect at `~/.claude/teams/`

**Starter Prompt:**

> "Create a team to review this Node.js project with 3 agents."

**Better Prompt (Build Toward This):**
"Create a team called 'code-review' using TeamCreate. Spawn 3 teammates: 'routes-reviewer' to review routes.js for security and validation issues, 'db-reviewer' to review db.js for connection handling and query safety, and 'config-reviewer' to review package.json and config files for missing dependencies. Create a task for each reviewer describing what to look for. Assign tasks using TaskUpdate with the owner parameter. After setup, read `~/.claude/teams/code-review/config.json` to verify all members are registered."

**Reflection Questions:**

1. How many files were created when you ran TeamCreate? What does each one contain?
2. When you spawned teammates, how did you specify what each one should focus on? What happened when instructions were vague vs. specific?
3. If you needed to add a 4th teammate mid-review, what steps would you take?

---

### Exercise 1.2 -- Diagnose a Broken Team (Debug)

**The Problem:**
Open the `module-1-team-fundamentals/exercise-1.2-broken-team/` folder. You'll find a team configuration and task list with 3 planted bugs: (1) a circular `blockedBy` dependency where Task A blocks Task B and Task B blocks Task A, (2) a teammate with an empty name string in the config, and (3) a task assigned to an owner that doesn't match any team member name.

**Your Task:**
Read the team config and task files. Identify all three bugs, explain why each one causes problems, and fix them. For the circular dependency, redraw the dependency chain so tasks can actually complete. For the empty name, assign a proper name. For the wrong owner, match it to an actual team member.

**What You'll Learn:**

- How circular `blockedBy` dependencies create deadlocks that prevent any task from starting
- That teammate names must be non-empty and consistent between config and task assignment
- The debugging technique of reading all team files before changing any

**Reflection Questions:**

1. How did you detect the circular dependency? What tool or technique made it visible?
2. What would happen at runtime if you launched a team with these bugs? Which bug would surface first?
3. How would you prevent circular dependencies in a real project with 20+ tasks?

---

## Module 2: Task Coordination

> **Core Skill:** Creating task pipelines with dependencies and managing task ownership

### Exercise 2.1 -- Build a Dependency Pipeline (Hands-on)

**The Problem:**
Open the `module-2-task-coordination/exercise-2.1-dependency-pipeline/` folder. You'll find a project that needs a migration from string-based IDs to UUIDs across multiple files. The migration has strict ordering requirements: database schema must update first, then data migration, then application code, then tests. If any step runs out of order, the system breaks.

**Your Task:**
Create a task pipeline with 4 tasks where each task is blocked by the previous one. Use `addBlockedBy` in TaskUpdate to enforce the ordering. Assign each task to a different teammate. Start the pipeline and verify that tasks unlock in sequence as each one completes.

**What You'll Learn:**

- How `addBlockedBy` creates sequential dependencies between tasks
- That blocked tasks cannot be claimed until their dependencies resolve
- The difference between parallel tasks (no dependencies) and sequential pipelines

**Starter Prompt:**

> "Create tasks for a UUID migration and make sure they run in order."

**Better Prompt (Build Toward This):**
"Create 4 tasks for a string-to-UUID migration: (1) 'Update database schema' -- add UUID columns alongside string IDs, (2) 'Migrate existing data' -- populate UUID columns from string IDs, (3) 'Update application code' -- change all blockedBy arrays from string references to UUID references, (4) 'Update tests' -- fix test fixtures to use UUIDs. Set dependencies: task 2 blockedBy task 1, task 3 blockedBy task 2, task 4 blockedBy task 3. Assign each to a different teammate. Start task 1 and verify tasks 2-4 show as blocked in TaskList."

**Reflection Questions:**

1. What did TaskList show for tasks 2-4 while task 1 was in progress? How does the `blockedBy` field appear?
2. What would happen if you tried to set task 2 to `in_progress` before task 1 completed?
3. When would you use parallel tasks (no dependencies) instead of a pipeline? Give an example from this project.

---

### Exercise 2.2 -- Fix a Micromanaging Lead (Debug)

**The Problem:**
Open the `module-2-task-coordination/exercise-2.2-micromanaging-lead/` folder. You'll find a session transcript of a team lead agent that is micromanaging its teammates. Instead of creating tasks and letting teammates work autonomously, the lead sends a message after every small step, reassigns tasks mid-work, and broadcasts status updates that interrupt all teammates simultaneously.

**Your Task:**
Read the session transcript. Identify at least 4 anti-patterns the lead is exhibiting. For each anti-pattern, explain what the lead should do instead. Then write a corrected version of the lead's key prompts that delegate effectively.

**What You'll Learn:**

- Why broadcasting every status update wastes tokens and interrupts focused work
- That reassigning tasks mid-work destroys teammate context and forces restarts
- The difference between effective delegation (create task, assign, wait for completion) and micromanagement (message after every step)

**Starter Prompt:**

> "What's wrong with this team lead's behavior?"

**Better Prompt (Build Toward This):**
"Read the session transcript in `transcript.md`. For each message the lead sends, classify it as: (A) necessary coordination, (B) unnecessary interruption, or (C) harmful micromanagement. Count how many messages fall into each category. For every category C message, write what the lead should have done instead. Focus on: when to use DM vs broadcast, when to let teammates work without checking in, and how task status (TaskList) replaces manual status checks."

**Reflection Questions:**

1. How many of the lead's messages were category C (harmful micromanagement)? What percentage of total communication was wasted?
2. The lead used `broadcast` 7 times. How many of those should have been DMs or not sent at all?
3. What signals should a team lead watch for instead of sending check-in messages? (Hint: what notifications does the system send automatically?)

---

## Module 3: Quality Hooks

> **Core Skill:** Designing hooks that enforce quality standards across team workflows

### Exercise 3.1 -- Build Team Quality Hooks (Hands-on)

**The Problem:**
Open the `module-3-quality-hooks/exercise-3.1-team-hooks/` folder. You'll find a set of service files (`auth-service.js`, `payment-service.js`, `notification-service.js`) that contain TODO comments, FIXME markers, and console.log debugging statements that should never reach production. Your team of 3 agents will review and fix these files, but you need hooks to enforce quality standards automatically.

**Your Task:**
Design hooks that fire during team workflows: (1) a `TeammateIdle` hook that checks whether the idle teammate's assigned tasks are actually complete before the lead assigns new work, (2) a `TaskCompleted` hook that scans the completed file for remaining TODO/FIXME markers and rejects the task if any are found, and (3) a notification hook that alerts the lead when any teammate has been idle for more than 2 consecutive turns without progress.

**What You'll Learn:**

- How `TeammateIdle` and `TaskCompleted` hooks integrate with team lifecycle events
- That hooks can enforce quality gates automatically instead of relying on manual review
- The pattern of using exit codes to block or allow team actions (exit 0 = allow, exit 2 = block)

**Starter Prompt:**

> "Create hooks that check code quality when teammates finish tasks."

**Better Prompt (Build Toward This):**
"Create team quality hooks in the settings configuration: (1) A hook on `TaskCompleted` that runs `grep -rn 'TODO\|FIXME\|console\.log' <completed-file>` and exits with code 2 if any matches are found, blocking task completion until cleanup is done. (2) A hook on `TeammateIdle` that reads the teammate's task list and logs whether all assigned tasks show status 'completed'. (3) A notification script that the lead can run manually to check which teammates have open tasks. Put hook scripts in `.claude/hooks/` with proper execute permissions."

**Reflection Questions:**

1. What exit code did your TaskCompleted hook use to block completion? What happens to the task status when a hook blocks?
2. How would you modify the TeammateIdle hook to automatically reassign tasks from a stuck teammate?
3. If a hook script has a bug and always exits with code 2, what happens to the team workflow? How would you debug this?

---

### Exercise 3.2 -- Debug Hook Failures (Debug)

**The Problem:**
Open the `module-3-quality-hooks/exercise-3.2-debug-hooks/` folder. You'll find a team configuration with 3 hooks that are all broken. Bug 1: A `TeammateIdle` hook is registered as `teammateIdle` (wrong casing -- the event name is case-sensitive). Bug 2: A quality check hook script exits with code 1 instead of code 2, so it logs an error but never actually blocks the action. Bug 3: A hook script file exists but is missing the execute permission (`chmod +x`), so it never runs.

**Your Task:**
Diagnose and fix all three bugs. For each bug, document: what the symptom was, what the root cause was, and what you changed to fix it. Run the hooks after fixing to verify they work.

**What You'll Learn:**

- That hook event names are case-sensitive: `TeammateIdle` works, `teammateIdle` does not
- The critical difference between exit codes: 0 = success, 1 = error (logged but not blocking), 2 = block the action
- That file permissions are a silent killer -- a hook without `chmod +x` never executes and produces no error

**Starter Prompt:**

> "These 3 hooks aren't working. Find out why."

**Better Prompt (Build Toward This):**
"Read the settings configuration and all hook scripts in `.claude/hooks/`. For each hook: (1) Check the event name matches the exact casing from the documentation (TeammateIdle, TaskCompleted, not lowercase variants). (2) Check the exit code -- if the hook should BLOCK an action, it must exit 2, not exit 1. (3) Check file permissions with `ls -la .claude/hooks/` -- scripts need execute permission. Fix each bug, then test by triggering each hook event manually."

**Reflection Questions:**

1. Which bug was hardest to diagnose? The casing issue, the exit code issue, or the permissions issue?
2. How would you write a quick validation script that checks all 3 potential issues for any hook file?
3. If you were documenting a "team hooks debugging checklist" for your team, what would the first 5 items be?

---

## Module 4: Capstones

> **Choose one (or both). These combine team creation, task coordination, and quality hooks -- no starter prompts provided.**

Capstones are different from the exercises above. There are no guided prompts -- you design the entire approach yourself. Each project requires combining team fundamentals, task coordination, and quality hooks into a complete multi-agent workflow.

### Capstone A -- Full 3-Agent Parallel Code Review

Open the `module-4-capstones/capstone-A-parallel-review/` folder. You'll find a Node.js project with 19 planted issues across 4 files: `routes.js` (authentication bypass, missing input validation, SQL injection), `jwt.js` (weak signing algorithm, token expiration issues), `db.js` (connection pool leaks, missing error handling), and `api.test.js` (missing edge case tests, hardcoded values). Design a complete team: create 3 specialized reviewer agents (security, reliability, testing), create tasks with appropriate dependencies, add quality hooks that verify each reviewer found a minimum number of issues, and compile a final review report. The goal is to find all 19 issues through parallel team coordination.

**What You'll Learn:**

- How to decompose a code review into parallel workstreams that don't duplicate effort
- That task dependencies matter even in parallel work -- the final report depends on all reviews completing
- How quality hooks can enforce minimum standards (e.g., each reviewer must find at least 3 issues)

---

### Capstone B -- Your Professional Domain

Open the `module-4-capstones/capstone-B-professional-domain/` folder for a self-assessment template. Design an agent team for a real workflow in your professional domain. Examples: a content team (researcher, writer, editor) for producing technical documentation, a data pipeline team (extractor, transformer, validator) for ETL workflows, or a testing team (unit tester, integration tester, report generator) for quality assurance. Define the team structure, create at least 4 tasks with dependencies, add at least one quality hook, and run the team on a real (or realistic) project.

**What Makes This Special:**
Unlike Capstone A, this one applies to YOUR actual work. The team structure you design could become a reusable pattern you use daily. Most professionals discover that even 2-agent teams save significant time on tasks they were doing sequentially.

**What You'll Learn:**

- How to identify workflows in your domain that benefit from parallelization
- That team design requires thinking about task boundaries -- what can run in parallel vs what must be sequential
- How to evaluate whether a multi-agent approach saved time compared to doing it yourself

---

## Assessment Rubric

After completing the exercises, evaluate yourself on each dimension:

| Criteria                |        Beginner (1)         |          Developing (2)          |                Proficient (3)                |                  Advanced (4)                  |
| ----------------------- | :-------------------------: | :------------------------------: | :------------------------------------------: | :--------------------------------------------: |
| **Team Creation**       | Can't create team or spawn  |  Creates team but wrong structure |    Correct team, members, and config          |  Designs teams optimized for task parallelism  |
| **Task Coordination**   |  Tasks have no dependencies | Dependencies exist but incorrect |  Correct blockedBy chains and task ownership  |  Pipelines with parallel and sequential stages |
| **Hook Design**         |     Hooks don't fire        | Hooks fire but wrong exit codes  |  Correct events, scripts, and exit semantics  |  Hooks compose into team-wide quality gates    |
| **Debug Skill**         |    Can't identify issue     |   Finds issue but wrong fix      |       Correct diagnosis and fix               |  Prevents class of issues proactively          |

**Target**: Proficient (3) across all dimensions by Module 3. Advanced (4) is demonstrated through capstone completion.

---

## What's Next

You've practiced the three core skills -- **team orchestration**, **multi-agent debugging**, and **hook-based quality gates** -- across 10 exercises. These skills compound: every exercise builds intuition for when to create a team vs work solo, how to design task dependencies that prevent deadlocks, and where quality hooks catch mistakes that humans miss. Agent teams are how professionals scale from individual Claude Code sessions to coordinated multi-agent workflows. Next in **Lesson 22: Claude Cowork -- From Terminal to Desktop**, you'll transition from terminal-based workflows to the visual desktop experience, learning when each interface serves you best.
