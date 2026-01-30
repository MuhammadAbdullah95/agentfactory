---
sidebar_position: 4
title: "The Tasks System: Persistent State for Context Management"
description: "How Claude Code's native Tasks system enables aggressive context management through filesystem-backed persistent state"
keywords:
  [
    "Tasks",
    "TaskCreate",
    "TaskUpdate",
    "TaskList",
    "context management",
    "persistent state",
    "DAG",
    "dependency graph",
    "cross-session coordination",
    "CLAUDE_CODE_TASK_LIST_ID",
  ]
chapter: 4
lesson: 4
duration_minutes: 25

# HIDDEN SKILLS METADATA
skills:
  - name: "Understanding Tasks as Context Engineering"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain why filesystem persistence enables aggressive context clearing without losing project state"

  - name: "Using Task Dependencies"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can create tasks with blockedBy relationships to represent work dependencies"

  - name: "Designing Multi-Session Workflows"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Communication"
    measurable_at_this_level: "Student can design task-based workflows that coordinate across multiple sessions or agents"

learning_objectives:
  - objective: "Explain why filesystem-backed Tasks enable aggressive context management"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student can articulate the relationship between plan-on-disk and context clearing"

  - objective: "Create tasks with dependency relationships using TaskCreate and TaskUpdate"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student demonstrates creating a task DAG with blockedBy relationships"

  - objective: "Design a cross-session workflow using CLAUDE_CODE_TASK_LIST_ID"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Student configures two sessions to share the same task list"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (Tasks vs ephemeral state, filesystem persistence, dependency DAGs, context-clearing freedom, cross-session coordination) appropriate for B1"

differentiation:
  extension_for_advanced: "Design a Writer/Reviewer pattern with two sessions using shared task coordination"
  remedial_for_struggling: "Focus on the core insight first (plan on disk = context freedom), then the mechanics"
---

# The Tasks System: Persistent State for Context Management

You're deep in a complex refactoring project. You've built a mental map of what needs to happen: fix the authentication module, then update the user service that depends on it, then run the integration tests. Claude knows this plan too. You've discussed it. It's all in context.

Then you hit the wall. Context is at 80%. Quality is degrading. You need to run `/clear`.

And the plan vanishes.

This is the ephemeral state problem. Your project roadmap lived only in the conversation. Clear the context, lose the roadmap.

Claude Code's Tasks system solves this. **Tasks are filesystem-backed persistent state.** Your plan lives on disk, not in context. Clear freely. The roadmap survives.

## The Old Problem: Ephemeral Todos

Before Tasks, Claude Code had Todos. You might have seen them in the sidebar: an orange sticky-note icon. They helped Claude remember what to do during a session.

The problem: Todos lived in the chat. When you ran `/clear` or `/compact`, they could disappear along with your conversation history. The plan existed only as long as the context existed.

| Aspect               | Old Todos       | New Tasks                          |
| -------------------- | --------------- | ---------------------------------- |
| **Storage**          | In conversation | On filesystem (`~/.claude/tasks/`) |
| **Survives /clear**  | No              | Yes                                |
| **Survives crashes** | No              | Yes                                |
| **Cross-session**    | No              | Yes (with environment variable)    |
| **Dependencies**     | No              | Yes (blockedBy, addBlocks)         |

This isn't a small upgrade. It's a paradigm shift in how plans relate to context.

## The Core Insight: Plan on Disk Enables Context Freedom

Here's the key insight, directly from the VentureBeat analysis of this feature:

> "Because the plan is stored on disk, users can run /clear or /compact to free up tokens for the model's reasoning, without losing the project roadmap."

This is context engineering in action. You've learned that context fills up and quality degrades. You've learned about the attention budget and position sensitivity. Now you have a tool that **decouples your plan from your context**.

**Before Tasks:**

- Plan lives in context
- Context fills up
- Can't clear without losing plan
- Quality degrades as you work

**After Tasks:**

- Plan lives on disk
- Context fills up
- Clear freely, plan persists
- Quality stays high through aggressive context management

## The Four Task Tools

Claude Code provides four tools for working with Tasks:

### TaskCreate

Creates a new task with a subject, description, and optional metadata.

```
TaskCreate:
  subject: "Implement authentication refactor"
  description: "Update auth module to use JWT instead of sessions..."
  activeForm: "Implementing authentication refactor"
```

The `activeForm` is what appears in the spinner while Claude works on the task.

### TaskList

Shows all tasks with their status, owner, and blocking relationships.

```
TaskList output:
- id: "1", subject: "Fix auth module", status: "completed"
- id: "2", subject: "Update user service", status: "in_progress", blockedBy: ["1"]
- id: "3", subject: "Run integration tests", status: "pending", blockedBy: ["1", "2"]
```

A task is "available" when:

- Status is `pending`
- No owner assigned
- `blockedBy` list is empty (all dependencies resolved)

### TaskGet

Retrieves full details for a specific task, including its complete description and dependency relationships.

```
TaskGet: "2"

Result:
  id: "2"
  subject: "Update user service"
  description: "Modify UserService to consume new JWT tokens from auth module..."
  status: "in_progress"
  blockedBy: ["1"]
  blocks: ["3"]
```

### TaskUpdate

Updates a task's status, adds dependencies, or marks completion.

```
TaskUpdate:
  taskId: "2"
  status: "completed"
```

When task 2 completes, task 3 automatically becomes unblocked and available for work.

## Dependency Graphs: Task DAGs

Tasks support **Directed Acyclic Graphs (DAGs)**. Task 3 can be blocked by Tasks 1 and 2. When both complete, Task 3 automatically becomes available.

This is powerful for complex projects:

```
┌─────────────────┐
│  1: Fix Auth    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│ 2: User Service │     │ 4: Admin Panel  │
└────────┬────────┘     └────────┬────────┘
         │                       │
         ▼                       │
┌─────────────────┐              │
│ 3: Integration  │◄─────────────┘
│    Tests        │
└─────────────────┘
```

Task 3 (integration tests) is blocked by Tasks 2 and 4. Both must complete before testing can begin.

To set this up with TaskUpdate:

```
TaskUpdate:
  taskId: "3"
  addBlockedBy: ["2", "4"]
```

## Filesystem Persistence: Where Tasks Live

Tasks are stored in `~/.claude/tasks/` on your filesystem. Each session gets its own directory of JSON files representing the task state.

This has three implications:

**1. Crash Recovery**: If your terminal crashes, your tasks persist. Resume your session, run `TaskList`, continue where you left off.

**2. Session Independence**: Tasks don't consume context. They live outside the conversation window. A complex 50-task project plan uses zero tokens in your conversation.

**3. Human Inspection**: You can examine tasks directly in the filesystem. Debug agent behavior by reading the raw JSON.

## The Pattern: Plan, Clear, Execute

Armed with Tasks, here's the pattern for long-running work:

**Phase 1: Plan**
Create tasks at the beginning of a work session when context is fresh:

```
TaskCreate: "Analyze existing authentication implementation"
TaskCreate: "Design JWT token structure", addBlockedBy: ["1"]
TaskCreate: "Implement token generation", addBlockedBy: ["2"]
TaskCreate: "Implement token validation", addBlockedBy: ["3"]
TaskCreate: "Update middleware", addBlockedBy: ["4"]
TaskCreate: "Write integration tests", addBlockedBy: ["5"]
```

**Phase 2: Clear**
When context fills up (60-80%), clear aggressively:

```
/clear
```

Your plan survives. The 6-task roadmap persists on disk.

**Phase 3: Execute**
After clearing, check what's available and continue:

```
TaskList
```

Claude sees which tasks are unblocked and continues execution.

**The key insight**: You're not losing information when you clear. You're freeing context for reasoning while your strategic plan persists.

## Cross-Session Coordination

For team workflows or parallel execution, multiple sessions can share the same task list using the `CLAUDE_CODE_TASK_LIST_ID` environment variable.

**Terminal A (Writer)**:

```bash
CLAUDE_CODE_TASK_LIST_ID=project-alpha claude
```

**Terminal B (Reviewer)**:

```bash
CLAUDE_CODE_TASK_LIST_ID=project-alpha claude
```

Both sessions now see the same tasks. When Writer marks a task complete, Reviewer sees it update. When Reviewer creates a feedback task, Writer sees it appear.

**The Writer/Reviewer Pattern**:

1. Session A writes code, marks `implement-feature` complete
2. System creates `review-feature` task blocked by `implement-feature`
3. When `implement-feature` completes, `review-feature` becomes available
4. Session B picks up `review-feature`, provides feedback
5. If issues found, Session B creates `fix-issues` task
6. Session A picks up `fix-issues`, continues work

This enables **parallel execution with coordination**. No stepping on each other's work. No duplicate effort. The task system manages handoffs.

## Tasks vs. Progress Files

You might wonder: "How are Tasks different from the progress files we'll learn about later in this chapter?"

| Aspect            | Tasks                           | Progress Files                    |
| ----------------- | ------------------------------- | --------------------------------- |
| **Purpose**       | Track what needs to be done     | Track what has been learned       |
| **Scope**         | Action items and dependencies   | Decisions, context, discoveries   |
| **Persistence**   | Automatic (via tools)           | Manual (you write them)           |
| **Cross-session** | Built-in (environment variable) | Manual (git or shared filesystem) |

**Use both together**: Tasks track the WHAT (action items). Progress files track the WHY (decisions and discoveries). Tasks tell you what to do next. Progress files tell you what you've learned along the way.

## Lab: Building a Task-Managed Workflow

**Objective:** Experience the plan-clear-execute pattern with real work.

**Setup:**

1. Choose a multi-step task in your domain (refactoring, content creation, analysis)
2. Start a fresh Claude Code session

**Protocol:**

**Step 1: Plan with Dependencies**

Ask Claude to create a task plan:

```
Create tasks for [your project] with proper dependencies.
Each task should have clear completion criteria.
Tasks that depend on others should use blockedBy.
```

Verify with `TaskList` that dependencies are correctly set.

**Step 2: Work Until Context Fills**

Execute tasks until you notice quality degradation (typically 60-80% context usage).

Check with `/context`.

**Step 3: Clear and Verify**

Run `/clear`.

Then immediately run `TaskList`.

**Observation:** Your plan survived the clear. Your strategic roadmap persists even though your conversation history is gone.

**Step 4: Continue Execution**

Ask Claude to pick up the next available task:

```
What tasks are available? Let's continue with the highest-priority unblocked task.
```

**Expected Finding:** The workflow continues seamlessly despite the context clear. This is the power of filesystem-backed state.

## What You Learned

1. **Tasks are filesystem-backed**: They live in `~/.claude/tasks/`, not in your conversation
2. **Plan on disk enables context freedom**: You can `/clear` aggressively without losing your roadmap
3. **Dependencies form DAGs**: Tasks can block other tasks, automatically managing execution order
4. **Cross-session coordination**: `CLAUDE_CODE_TASK_LIST_ID` lets multiple sessions share task state
5. **Tasks complement progress files**: Tasks track actions; progress files track learnings

## Try With AI

### Prompt 1: Create a Dependent Task Plan

```
I have a project that involves:
1. Auditing existing code
2. Designing improvements
3. Implementing changes
4. Testing the implementation
5. Documenting the changes

Create these as tasks with proper dependencies.
Each task should have a clear description and activeForm.
Tasks should only become available when their prerequisites complete.
```

**What you're learning:** How to structure a project as a dependency graph. Pay attention to how Claude sets up the `blockedBy` relationships.

### Prompt 2: The Clear-and-Continue Pattern

```
Let's test persistence:
1. First, show me the current TaskList
2. Explain what would happen if I ran /clear right now
3. After I clear context, what command would I use to resume work?
```

**What you're learning:** Building intuition for the plan-on-disk pattern. Understanding that `/clear` frees context without losing state.

### Prompt 3: Design a Handoff Workflow

```
I want to set up a Writer/Reviewer workflow where:
- Writer creates implementation tasks
- Reviewer creates review tasks
- Work automatically flows between them

How would I configure CLAUDE_CODE_TASK_LIST_ID for both terminals?
What task structure enables automatic handoffs?
```

**What you're learning:** Cross-session coordination patterns. This is advanced context engineering: multiple agents, shared state, coordinated execution.

**Safety reminder:** When using cross-session coordination, ensure both sessions are working on the same project. Conflicting edits from different contexts can cause confusion.
