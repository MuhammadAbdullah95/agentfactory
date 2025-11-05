---
title: "Implement Phase — AI-Driven Code Generation and Validation"
chapter: 31
lesson: 7
duration_minutes: 150

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Using /sp.implement Command"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can run /sp.implement to orchestrate code generation for tasks"

  - name: "Code Review and Comprehension"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can read AI-generated code and verify it matches specification before acceptance"

  - name: "Validation Against Acceptance Criteria"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student systematically validates each acceptance criterion (test, verify, sign-off)"

  - name: "Understanding PHR Auto-Creation"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student understands PHRs are auto-created by system, knows where to find them, when to request explicit PHRs"

  - name: "Executing Checkpoint Pattern During Implementation"
    proficiency_level: "B1"
    category: "Soft"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student reviews→tests→approves→commits for each implementation phase"

learning_objectives:
  - objective: "Use /sp.implement to orchestrate AI-driven code generation for calculator tasks"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful implementation orchestration with checkpoint reviews"

  - objective: "Validate AI-generated code against specification acceptance criteria"
    proficiency_level: "B2"
    bloom_level: "Evaluate"
    assessment_method: "Systematic validation of each criterion with pass/fail evidence"

  - objective: "Understand PHR auto-creation and know where to find them"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Navigation to PHR files and understanding their content"

  - objective: "Identify and request explicit PHRs when system auto-creation might miss important decisions"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Judgment about when to request PHR creation"

cognitive_load:
  new_concepts: 10
  assessment: "10 new concepts (Implement command, code generation, code review, validation protocol, acceptance criteria verification, PHR auto-creation, PHR locations, explicit PHR requests, checkpoint pattern execution, error handling during implementation) within B2 limit of 10 ✓"

differentiation:
  extension_for_advanced: "Request explicit PHRs for complex decisions; analyze generated PHRs for quality; run full test suite before committing"
  remedial_for_struggling: "Focus on core operations first; validate against top 3-4 acceptance criteria before diving into edge cases"

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/10-chapter-31-redesign/spec.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "manual-implementation"
version: "1.0.0"
---

# Lesson 7: Implement Phase — AI-Driven Code Generation and Validation

This is it: **Implementation**. Everything you've done—specification, planning, tasking—leads to this moment.

`/sp.implement` orchestrates AI code generation. The agent generates code, you review it, you validate against acceptance criteria, you commit. Then the next task.

This lesson teaches two critical skills:
1. **Code validation** — How to review AI-generated code
2. **PHR auto-creation** — Understanding automatic documentation of AI collaboration

---

## Part A: What Does /sp.implement Do? (20 minutes)

### The Implement Command

`/sp.implement` analyzes your tasks and generates:
- **Code implementing each task**
- **Tests validating the code**
- **Documentation (docstrings, comments)**

It works task-by-task, respecting your checkpoint pattern.

### How Implementation Works

**Input**: Your specifications, plans, tasks

**Agent's Process**:
1. Read spec, plan, and current task
2. Generate code matching the specification
3. Include type hints, docstrings, error handling
4. Generate tests verifying acceptance criteria
5. Output code + tests, ready for human review

**Your Process**:
1. Review generated code
2. Understand what it does
3. Verify acceptance criteria
4. Approve or request changes
5. Commit to git
6. Tell agent: "Next task"

### Example: Task 1 Implementation

**Task**: "Implement add(a, b) returning float"

**Agent Generates**:

```python
def add(a: float | int, b: float | int) -> float:
    """Add two numbers and return the sum.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        float: Sum of a and b

    Examples:
        >>> add(5, 3)
        8.0
        >>> add(-2, 5)
        3.0
    """
    return float(a + b)
```

**Tests**:

```python
def test_add_positive():
    assert add(5, 3) == 8.0

def test_add_negative():
    assert add(-2, 5) == 3.0

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_add_invalid_input():
    with pytest.raises(TypeError):
        add("5", 3)
```

**Your Review**:
- ✅ Code has type hints
- ✅ Code has docstring
- ✅ Tests cover acceptance criteria
- Questions: Is `float(a + b)` the right approach? What about very large numbers?

**Approval**: "Looks good. Committing."

---

## Part B: The Validation Protocol (30 minutes)

Validation is NOT just "does it work?" It's systematic verification against your specification.

### The 5-Step Validation Process

**Step 1: Read and Understand**

Read the generated code without running anything:
- Do you understand what it does?
- Does it follow your Constitution (type hints, docstrings)?
- Is the logic clear or does it seem hacky?

**RED FLAG**: If you don't understand the code, don't approve it. Ask the agent to explain or simplify.

**Step 2: Check Against Specification**

Compare code to your specification:
- Does it do what the spec says?
- Does it handle the edge cases you specified?
- Does it match the error handling strategy (exceptions)?

**RED FLAG**: If code does something the spec doesn't mention, question it.

**Step 3: Run Acceptance Criteria Tests**

Run the generated tests:
- All tests pass?
- Coverage adequate?
- Edge cases included?

**RED FLAG**: Any failing tests = don't approve. Agent fixes and retries.

**Step 4: Manual Testing (Optional)**

Especially for core operations, manually test:

```python
# In Python REPL
from calculator import add

# Test basic cases
assert add(5, 3) == 8.0
assert add(-2, 5) == 3.0

# Test edge cases
assert add(0, 5) == 5.0
assert add(1.5, 2.5) == 4.0

# Test error cases
try:
    add("5", 3)
    assert False, "Should have raised TypeError"
except TypeError:
    pass  # Expected

print("All manual tests passed!")
```

**Step 5: Review and Approve**

If all checks pass:
- Mark as approved
- Commit to git
- Provide feedback to agent on quality
- Request next task

### Common Validation Issues

**Issue 1: Code Works But Doesn't Match Spec**

```python
# Specification says: "divide returns float"
# Code does:
def divide(a, b):
    return a / b if b != 0 else "Error: division by zero"
```

**Problem**: Returns string on error, not exception. Violates spec and error handling strategy.

**Your Response**: "Code works but violates error handling strategy. Use exception instead."

**Issue 2: Tests Pass But Code Seems Wrong**

```python
# Spec: "power(-2, 0.5) should raise ValueError"
# Code:
def power(a, b):
    return a ** b  # Python allows this! Returns complex number
```

**Problem**: Python's `**` allows complex results. Your spec forbids this.

**Your Response**: "Tests are incomplete. Test power(-2, 0.5) and verify it raises ValueError."

**Issue 3: Code Works But Is Unreadable**

```python
def calculate(a, b, op):
    return (
        a + b if op == '+' else
        a - b if op == '-' else
        a * b if op == '*' else
        a / b if b != 0 else
        None
    )
```

**Problem**: Violates Constitution ("clear code, docstrings"). No type hints.

**Your Response**: "Code works but violates Constitution. Add type hints and separate functions for each operation."

---

## Part C: PHRs — Automatic Documentation (20 minutes)

**CRITICAL CONCEPT**: PHRs are **automatically created by the system**. You don't manually write them.

### What Are PHRs?

**PHR** = **Prompt History Record**

A PHR automatically documents:
- What prompt you gave the agent
- What the agent responded with
- What decision was made
- When it happened

PHRs are auto-created for:
- Running `/sp.implement`
- Significant implementation decisions
- Complex debugging sessions
- Important clarifications during coding

### Where Are PHRs Stored?

```
history/prompts/
├── calculator/
│   ├── 001-specify-phase.md          (auto-created by /sp.specify)
│   ├── 002-clarify-phase.md          (auto-created by /sp.clarify)
│   ├── 003-plan-phase.md             (auto-created by /sp.plan)
│   ├── 004-tasks-phase.md            (auto-created by /sp.tasks)
│   ├── 005-implement-phase-pt1.md    (auto-created by /sp.implement)
│   ├── 006-implement-phase-pt2.md    (auto-created during implementation)
│   └── 007-implement-debugging.md    (auto-created during debugging)
└── general/
    └── [Other non-feature PHRs]
```

### What You Do With PHRs

**You don't create them.** You:
1. **Know they exist** (understand they're being created automatically)
2. **Know where to find them** (`history/prompts/<feature>/`)
3. **Review them later** (for learning, compliance, debugging)
4. **Request explicit PHRs** (only when system might miss something)

### When to Request Explicit PHRs

Normally, the system auto-creates PHRs for every `/sp.*` command and major decisions. But occasionally you might ask:

```
Agent, this debugging session was complex and taught me something important
about floating-point precision. Can you record this as a PHR for future reference?

[Describe what you learned]
```

**When to request**:
- ✅ Novel problem-solving approach
- ✅ Non-obvious error resolution
- ✅ Complex tradeoff decision
- ✅ Learning moment worth preserving

**When NOT to request**:
- ❌ Routine coding (PHRs already auto-created)
- ❌ Simple bug fixes (already captured in git history)
- ❌ Repeated issues (first occurrence captured, repeats unnecessary)

### Example: What a PHR Looks Like

**Auto-Created PHR** (from `/sp.implement`):

```markdown
# PHR-005: Implement Phase, Tasks 1-3 (Add, Subtract, Multiply)

**Date**: 2025-11-05
**Feature**: calculator
**Stage**: implement
**ID**: 005

## Input
- Specification: `specs/calculator/spec.md`
- Plan: `specs/calculator/plan.md`
- Tasks: `specs/calculator/tasks.md` (Tasks 1-3)
- Status: Core operations implementation

## Prompt
"Implement Tasks 1-3:
- add(a, b) returning float
- subtract(a, b) returning float
- multiply(a, b) returning float

Include type hints, docstrings, error handling for type mismatches.
Generate tests verifying all acceptance criteria."

## Response
Generated code with:
- All type hints present
- All docstrings present
- Error handling for invalid input types (raises TypeError)
- Tests for basic cases and edge cases (negative, zero, float inputs)

## Implementation Decision
- Used built-in Python operators (a + b, a - b, a * b)
- No custom validation; rely on type hints for clarity
- All operations return float(result) to ensure consistent type

## Tests
- 12 tests generated
- All tests passing
- 100% code coverage for core operations

## Status
✅ Approved by human. Committed to git.
```

### Your Interaction With PHRs

**During Implementation**:
- You don't think about PHRs; agent creates them automatically
- Focus on reviewing code and validating

**After Implementation**:
- Browse `history/prompts/calculator/` to see all implementation decisions
- Review PHRs to understand "why" decisions were made
- Use for documentation, compliance, or learning

**If System Misses Something**:
- "Record this debugging session as PHR"
- Agent creates explicit PHR for that decision
- Rare; most things are auto-captured

---

## Part D: Implementing Your Calculator (50 minutes)

Now let's implement your calculator using the checkpoint pattern.

### Step 1: Run /sp.implement

In Claude Code, from your calculator-project directory:

```
/sp.implement

My calculator tasks are at specs/calculator/tasks.md

Please implement tasks 1-3 (core operations: add, subtract, multiply):

1. Implement each operation with full type hints and docstrings
2. Generate comprehensive tests (unit + edge case + error handling)
3. Verify 100% code coverage for each operation
4. Output ready for my review

After I review and approve, I'll request the next tasks.
```

### Step 2: Review Generated Code

Agent generates:
- `calculator/operations.py` (or similar) with add, subtract, multiply functions
- `tests/test_operations.py` with comprehensive tests
- Docstrings and type hints

**Your Review Checklist**:
- [ ] Code is understandable (clear variable names, readable logic)
- [ ] Type hints present on all functions
- [ ] Docstrings present and clear
- [ ] Follows Constitution standards
- [ ] Handles edge cases specified
- [ ] Error handling matches your error strategy
- [ ] Tests cover all acceptance criteria

### Step 3: Run Tests

```bash
# Navigate to project
cd calculator-project

# Run tests
python -m pytest tests/test_operations.py -v

# Check coverage
python -m pytest tests/test_operations.py --cov=calculator --cov-report=html
```

All tests should pass with 100% coverage.

### Step 4: Validate Acceptance Criteria

For each operation, verify:

**Addition**:
- ✅ add(5, 3) = 8.0
- ✅ add(-2, 5) = 3.0
- ✅ add('5', 3) raises TypeError
- ... (all acceptance criteria from spec)

**Subtraction**:
- ✅ subtract(10, 3) = 7.0
- ... (all acceptance criteria)

**Multiplication**:
- ✅ multiply(4, 5) = 20.0
- ... (all acceptance criteria)

### Step 5: Approve and Commit

If all checks pass:

```bash
# Add generated code and tests
git add calculator/
git add tests/

# Commit with clear message
git commit -m "Implement core operations (add, subtract, multiply)

- add(a, b) returns float, handles negative numbers
- subtract(a, b) returns float
- multiply(a, b) returns float
- Type validation: non-numeric inputs raise TypeError
- Tests: 15 tests, 100% coverage, all passing

Acceptance criteria verified:
- All basic cases pass
- All edge cases covered
- Error handling matches spec"
```

### Step 6: Continue Implementation (Divide, Power, Tests, Docs)

Repeat the checkpoint pattern for remaining tasks:
- Task 4: Division (with zero-handling)
- Task 5: Power (with negative/fractional exponents)
- Tasks 6-8: Comprehensive tests, edge case tests, documentation

---

## Part E: Understanding Your PHRs (10 minutes)

After implementation completes, explore your PHRs:

```bash
# List all PHRs created during calculator implementation
ls -la history/prompts/calculator/

# Review a specific PHR (e.g., implementation decisions)
cat history/prompts/calculator/005-implement-phase-pt1.md

# See all calculator-related PHRs
grep -l "calculator" history/prompts/*/*.md
```

Typical feature generates **8-10 PHRs** (one per command phase + major decisions).

---

## Validation Checklist

Before declaring implementation complete:

**Code Quality**:
- [ ] All functions have type hints
- [ ] All functions have docstrings
- [ ] No hardcoded test data in production code
- [ ] Code follows PEP 8
- [ ] No security issues (no secrets in code)

**Testing**:
- [ ] 100% code coverage
- [ ] All acceptance criteria tested
- [ ] Edge cases covered
- [ ] Error handling tested
- [ ] Tests pass on your machine

**Commits**:
- [ ] Each phase committed separately
- [ ] Commit messages are descriptive
- [ ] Git history shows progression

**PHRs**:
- [ ] You understand PHRs are auto-created
- [ ] You know where to find them
- [ ] You've browsed at least one PHR

---

## Try With AI: Reflect on Implementation and Decisions

Use your AI companion to reflect on your implementation and capture important decisions.

### Setup

**Tool**: Claude Code (or your configured AI orchestrator)

**Context**: Your completed implementation code and tests

**Goal**: Validate implementation quality and reflect on key decisions captured in PHRs

### Prompt Set (Copy-Paste Ready)

**Prompt 1 — Implementation Quality**

Copy and paste this into Claude Code:

```
I've completed implementation of core operations (add, subtract, multiply).

Summary:
- 3 functions implemented
- Type hints included
- Docstrings included
- 15 tests written, all passing
- 100% coverage achieved

Review my code at: calculator/operations.py
Review my tests at: tests/test_operations.py

Is the implementation quality good? Any suggestions for improvement?
What patterns from this implementation should I maintain for the remaining operations?
```

**Prompt 2 — Decision Capture**

After quality review, ask:

```
During implementation, we made several design decisions:

1. [Decision 1]: [What you decided]
   Reason: [Why]

2. [Decision 2]: [What you decided]
   Reason: [Why]

These decisions are being captured in PHRs automatically.
If I need to understand "why" something was implemented this way in the future,
where would I look?
```

**Prompt 3 — PHR Exploration**

Finally, ask:

```
Can you help me understand the PHRs created during my calculator implementation?

Which files in history/prompts/calculator/ were auto-created?
What does each one capture?

And if I had discovered something surprising during implementation
(like floating-point precision issues), should I request an explicit PHR?
When is that warranted?
```

### Expected Outcomes

✅ **Implementation is high quality and production-ready**
✅ **You understand how decisions are automatically captured in PHRs**
✅ **You know when to request explicit PHRs (rare)**
✅ **Ready for Lesson 8 (Capstone)**

### Safety & Ethics Note

**On AI-Generated Code**:

Your AI companion generated production-ready code. But YOU validated it. Trust the code only because YOU reviewed it. Never accept code you don't understand. The checkpoint pattern ensures this—you're not an observer, you're a validator.

Validation is not a box to check; it's your protection against bugs. Invest time in it.

---

**You've completed Lesson 7**. Your calculator is now fully implemented with comprehensive tests, passing all acceptance criteria. PHRs automatically captured key decisions along the way.

In Lesson 8 (Capstone), you'll apply the entire Spec-Kit Plus workflow from scratch on a new project—temperature converter or unit converter—consolidating everything you've learned.

Next: [Lesson 8: Capstone Integration — Complete Workflow End-to-End](./08-capstone-integration.md)
