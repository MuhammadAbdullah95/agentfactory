---
title: "Tasks Phase — Atomic Work Units and Checkpoints"
chapter: 31
lesson: 6
duration_minutes: 90

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Using /sp.tasks Command"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can run /sp.tasks to decompose plan into atomic work units"

  - name: "Understanding Atomic Task Definition"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student understands atomic task = 1-2 hour unit with single acceptance criterion"

  - name: "Recognizing Task Dependencies"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student understands which tasks must complete before others (dependency graph)"

  - name: "Human-Controlled Checkpoint Pattern"
    proficiency_level: "B1"
    category: "Soft"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student understands Agent→Review→Commit→Continue workflow and human's role in each checkpoint"

  - name: "Lineage Traceability"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can trace: specification requirement → plan component → task unit"

learning_objectives:
  - objective: "Use /sp.tasks to decompose calculator plan into atomic work units"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful execution of /sp.tasks and understanding of task breakdown"

  - objective: "Understand checkpoint pattern: Agent completes phase → Human reviews → Human commits → Agent continues"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explanation of checkpoint pattern and human's control role"

  - objective: "Trace requirement lineage from specification through plan to tasks"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Ability to follow a requirement from spec to task unit"

cognitive_load:
  new_concepts: 7
  assessment: "7 new concepts (Tasks command, atomic units, dependencies, checkpoint pattern, lineage traceability, human control, task acceptance criteria) within B1 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Draw dependency graph; analyze what would happen if one task failed; identify critical path"
  remedial_for_struggling: "Focus on top 3-4 tasks; understand dependencies; delay deep analysis of all tasks"

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/10-chapter-31-redesign/spec.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "manual-implementation"
version: "1.0.0"
---

# Lesson 6: Tasks Phase — Atomic Work Units and Checkpoints

You now have:
- ✅ A clear specification
- ✅ A detailed implementation plan
- ✅ Documented architecture decisions (ADRs)

Next: Break the plan into **atomic work units** (tasks) that you'll implement.

This lesson teaches the **checkpoint pattern**—the critical workflow practice that keeps YOU in control. The pattern is:

```
Agent: "Here's Phase 1 code"
You: "Review... looks good!"
You: "Commit to git"
You: "Tell me what's next"
Agent: "Phase 2"
```

NOT:

```
Agent: "Here's everything" (no human control)
```

The difference is huge. Checkpoints keep you in control and catch issues early.

---

## Part A: What Are Tasks? (15 minutes)

### Atomic Tasks

A **task** is a unit of work that:
- Takes 1-2 hours to complete
- Has a single, clear acceptance criterion
- Depends on specific other tasks
- Can be reviewed and approved individually

### Task Properties

**Size**: 1-2 hours
- Too small (30 min) = too many micro-tasks
- Too large (4+ hours) = hard to review, hard to fix if wrong

**Criterion**: Single, testable
- "Write add operation" ✅
- "Write add operation and all tests" ❌ (two things)
- "Write something" ❌ (untestable)

**Independence**: Can be reviewed individually
- Doesn't require other tasks to be done first
- Or clearly depends on specific other tasks

### Example: Calculator Tasks

**Phase 1: Core Operations**

Task 1.1: Write add operation
- Duration: 1-2 hours
- Criterion: `add(a, b)` returns float, handles negative numbers
- Depends on: Nothing (first task)

Task 1.2: Write subtract operation
- Duration: 1 hour
- Criterion: `subtract(a, b)` returns float
- Depends on: Task 1.1 (can reuse validation pattern)

Task 1.3: Write multiply and divide
- Duration: 2 hours
- Criterion: Both operations work, divide handles zero
- Depends on: Task 1.1

Task 1.4: Write power operation
- Duration: 2 hours
- Criterion: Handles positive/negative/fractional exponents
- Depends on: Task 1.1

**Phase 2: Testing**

Task 2.1: Unit tests for all operations
- Duration: 1.5 hours
- Criterion: 100% code coverage, all tests pass
- Depends on: Task 1.4 (all operations complete)

Task 2.2: Edge case tests
- Duration: 1 hour
- Criterion: Tests for division by zero, overflow, precision limits
- Depends on: Task 2.1

---

## Part B: The Checkpoint Pattern (CRITICAL) (30 minutes)

This is **the most important concept** in this lesson. The checkpoint pattern is how you maintain control of the workflow.

### Pattern Definition

```
Loop:
  1. Agent: "I've completed Phase X"
  2. Human: "Review the work"
  3. Human: "APPROVE" → Commit to git
  4. Human: "Tell me next step"
```

### Why Checkpoints Matter

**Without Checkpoints** (dangerous):
```
You: "Build my calculator"
Agent: "Done! 5000 lines of code, 47 files. All automated. You're welcome."
You: "Uh... wait, I need to review this..."
Agent: "Too late, already committed and deployed!"
```

**With Checkpoints** (controlled):
```
You: "Start implementation"
Agent: "Phase 1 (Core Operations) complete. 200 lines, ready for review."
You: "Read code... looks good. Commits. What's next?"
Agent: "Phase 2 (Tests) starting"
You: "Review tests... found a bug in edge case handling"
You: "Tell agent, agent fixes, re-reviews, commits"
Agent: "Phase 3..."
```

### Your Role in Each Checkpoint

**Step 1: Human Reviews**
- Read the generated code/tests
- Ask: "Does this match the spec?"
- Ask: "Are there bugs or edge cases missed?"
- Ask: "Is the code understandable?"

**Step 2: Human Decides**
- Approve ("Looks good, commit")
- Reject ("Fix this issue")
- Request clarification ("Explain this code")

**Step 3: Human Commits**
- Your decision to commit = approval
- Creates audit trail (git log shows human approval)
- Next phase only starts after human approval

**Step 4: Human Directs**
- "What's next?"
- You initiate next phase
- Agent doesn't autonomously continue

### Checkpoint in Practice

**Checkpoint 1: Core Operations (Phase 1)**

```
Agent: "Phase 1 complete. I've implemented:
- add(a, b) function with type hints and docstring
- subtract(a, b) function
- multiply(a, b) function
- divide(a, b) with zero-handling
- power(a, b) with negative exponent handling

Code is at calculator/core.py. Ready for review."

You: [Read calculator/core.py]
- ✅ All functions have type hints
- ✅ All functions have docstrings
- ✅ divide handles zero correctly
- ✅ power handles negative exponents
- Questions:
  - Line 45: Is the precision handling correct for very large powers?
  - Can you clarify the type validation in multiply?

Agent: [Explains code, addresses questions]

You: "Approved. Committing..."

git add calculator/
git commit -m "Phase 1: Core operations complete

- Implemented add, subtract, multiply, divide, power
- All functions include type hints and docstrings
- Division by zero raises ValueError
- Power handles negative/fractional exponents

Ready for Phase 2: Testing"

Agent: "Phase 1 committed. Proceeding to Phase 2..."
```

**Checkpoint 2: Tests (Phase 2)**

```
Agent: "Phase 2 complete. I've written:
- Unit tests for all 5 operations
- Edge case tests (zero, negative, large numbers)
- 100% code coverage achieved

Test summary:
- 25 tests total
- All passing
- Coverage: 100%

Ready for review."

You: [Run tests locally]
pytest tests/test_calculator.py -v --cov

You: [Review test code]
- ✅ All operations tested
- ✅ Edge cases covered
- ⚠️ Questions:
  - Are we testing floating-point precision limits?
  - Should we test operation chaining (add then multiply)?

Agent: [Adds precision limit tests, adds chaining tests]

You: "Approved. Committing..."

git add tests/
git commit -m "Phase 2: Comprehensive tests complete

- 25 unit tests covering all operations
- Edge case tests (zero, negative, overflow)
- Floating-point precision tests
- Operation chaining tests
- 100% code coverage

Tests passing on: Windows, Mac, Linux"

Agent: "Phase 2 committed. Proceeding to Phase 3..."
```

---

## Part C: Generating Your Tasks (20 minutes)

### Step 1: Run /sp.tasks

In Claude Code, from your calculator-project directory:

```
/sp.tasks

My calculator specification is at specs/calculator/spec.md
My implementation plan is at specs/calculator/plan.md

Please decompose the plan into atomic work units (tasks):

1. Size each task at 1-2 hours of work
2. Define single acceptance criterion per task
3. Show dependencies (which tasks must complete first)
4. Create dependency graph showing sequencing

Output: Create specs/calculator/tasks.md with the task breakdown.
```

### Step 2: Review Generated Tasks

The tasks.md should show:
- Task 1: [Description] - 1-2 hours - Depends on: Nothing
- Task 2: [Description] - 1.5 hours - Depends on: Task 1
- Task 3: [Description] - 2 hours - Depends on: Task 1, Task 2
- ...

### Step 3: Save and Verify

```bash
# Verify tasks file exists
cat specs/calculator/tasks.md

# Count tasks
grep "^## Task" specs/calculator/tasks.md | wc -l
```

You should have 6-10 tasks total.

---

## Part D: Understanding Your Task Breakdown (15 minutes)

Review your tasks and verify:

### Dependency Graph

Can you draw your tasks?

```
Task 1 (add) → Task 2 (subtract) → Task 3 (multiply, divide)
                                        ↓
                                    Task 4 (power)
                                        ↓
                                Task 5+ (tests, docs)
```

### Lineage Traceability

Pick one task. Can you trace it back?

```
Specification: "Calculator must add two numbers"
  ↓
Plan: "Phase 1: Core Operations - Implement basic arithmetic"
  ↓
Task 1.1: "Implement add(a, b) returning float, handling negative inputs"
  ↓
Acceptance Criterion: "add(5, 3) = 8.0, add(-2, 5) = 3.0, add('5', 3) raises TypeError"
```

If you can trace this lineage, your tasks are well-connected to your specification.

---

## Part E: Commit Your Tasks (10 minutes)

Commit the generated tasks to git:

```bash
# Add tasks
git add specs/calculator/tasks.md

# Commit with description
git commit -m "Generate calculator tasks from plan

- 8 atomic work units created
- Phase 1: Core operations (tasks 1-5)
- Phase 2: Testing (tasks 6-7)
- Phase 3: Documentation (task 8)

Ready for implementation phase"
```

---

## Validation Checklist

Before moving to Lesson 7 (Implementation), verify:

**Tasks Completeness**:
- [ ] All plan phases have corresponding tasks
- [ ] Each task is 1-2 hours (not too small, not too large)
- [ ] Each task has single acceptance criterion
- [ ] Tasks include both implementation and testing

**Dependencies**:
- [ ] Tasks are ordered correctly
- [ ] Dependencies are explicit (Task X depends on Task Y)
- [ ] No circular dependencies
- [ ] Critical path is clear (what's the minimum path to "done"?)

**Readiness**:
- [ ] Tasks are saved to specs/calculator/tasks.md
- [ ] Tasks are committed to git
- [ ] You understand the checkpoint pattern (you'll use it in Lesson 7)

---

## Try With AI: Validate Task Breakdown

Use your AI companion to confirm your tasks are well-decomposed and ready for implementation.

### Setup

**Tool**: Claude Code (or your configured AI orchestrator)

**Context**: Your tasks.md file

**Goal**: Confirm tasks are atomic, dependencies are correct, and checkpoint pattern will work

### Prompt Set (Copy-Paste Ready)

**Prompt 1 — Task Atomicity Check**

Copy and paste this into Claude Code:

```
I've broken my calculator plan into tasks. Here's my task breakdown:

[PASTE YOUR TASKS.MD HERE]

For each task, is it:
1. Atomic? (Does it do one thing with one acceptance criterion?)
2. Sized appropriately? (1-2 hours, not too small or large?)
3. Independent? (Can it be reviewed and tested separately?)

Any tasks that are too big, too small, or trying to do multiple things?
```

**Prompt 2 — Dependency Validation**

After task validation, ask:

```
Looking at my task dependencies, are they correct?

For example:
- Task 1 (add) depends on: Nothing
- Task 2 (subtract) depends on: Task 1
- Task 3 (multiply) depends on: Task 1
- Task 4 (divide) depends on: Task 1, 3
- Task 5 (power) depends on: Task 1, 4
- Task 6 (tests) depends on: All above

Are these dependencies logical? Would you change the order?
What's the critical path (minimum tasks to complete before "done")?
```

**Prompt 3 — Checkpoint Pattern Understanding**

Finally, ask:

```
I'm about to start the implementation phase, and I want to use the
checkpoint pattern (Agent→Human Review→Commit→Next).

Here's my understanding:
- Phase 1: Agent completes Task 1 (add operation)
- I review code against spec and acceptance criteria
- I decide: approve or revise
- I commit to git
- Phase 2: Agent completes Task 2 (subtract operation)
- Repeat...

Is this the right approach? Any guidance on what to look for during review?
```

### Expected Outcomes

✅ **Tasks are atomic and appropriately sized**
✅ **Dependencies are correct**
✅ **You understand the checkpoint pattern**
✅ **Ready for implementation (Lesson 7)**

### Safety & Ethics Note

**On Task Granularity**:

If your tasks seem too many (15+) or too few (2-3), that's a signal:
- **Too many**: Your plan might be too detailed, or tasks are too small. Next time, consider 1.5-2 hour sizing.
- **Too few**: Your plan might be too vague, or tasks are too large. Next time, break larger tasks into more detail.

Neither is wrong—you're learning. The checkpoint pattern lets you adapt as you discover the right granularity.

---

**You've completed Lesson 6**. Your calculator implementation is now broken into atomic, manageable tasks with clear dependencies. In Lesson 7, you'll implement these tasks using the `/sp.implement` command—and you'll experience the checkpoint pattern in action, keeping you in control the whole time.

Next: [Lesson 7: Implement Phase — AI-Driven Code Generation and Validation](./07-implement-phase.md)
