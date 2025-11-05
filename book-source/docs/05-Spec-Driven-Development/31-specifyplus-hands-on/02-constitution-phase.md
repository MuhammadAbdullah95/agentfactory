---
title: "Constitution Phase — Project-Wide Rules"
chapter: 31
lesson: 2
duration_minutes: 90

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Creating Project Constitution"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can write project Constitution defining quality, testing, error-handling standards"

  - name: "Distinguishing Global Rules from Feature Requirements"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain difference between Constitution (applies to ALL features) and Specification (applies to ONE feature)"

  - name: "Understanding Cascade Starting Point"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student recognizes that Constitution quality determines all downstream quality"

  - name: "Defining Quality Standards"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety & Security"
    measurable_at_this_level: "Student can define testable quality criteria (code style, type hints, error handling, test coverage)"

  - name: "Git Workflow Integration"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety & Security"
    measurable_at_this_level: "Student understands Constitution → Commit pattern (foundation before feature work)"

learning_objectives:
  - objective: "Write a project Constitution defining quality, testing, and error-handling standards for calculator project"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Constitution document review against template completeness and clarity"

  - objective: "Explain why Constitution is created once per project, not per feature"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Written or verbal explanation of Constitution scope"

  - objective: "Understand how Constitution quality cascades through all downstream phases"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Identification of how Constitution rules affect specifications and plans"

cognitive_load:
  new_concepts: 5
  assessment: "5 new concepts (Constitution role, Global rules vs feature specs, Cascade starting point, Quality standards, Git workflow) within A2 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Write Constitution for 2-3 different hypothetical projects (CLI tool, web API, data pipeline); compare how rules differ by project type"
  remedial_for_struggling: "Use provided Constitution template; fill in only essential sections (quality, error handling, testing) before moving to Lesson 3"

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/10-chapter-31-redesign/spec.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "manual-implementation"
version: "1.0.0"
---

# Lesson 2: Constitution Phase — Project-Wide Rules

Welcome to the second lesson of hands-on Spec-Kit Plus development. You've installed the framework and configured your AI tool. Now it's time to create the **foundational rules** that will guide every part of your calculator project.

The Constitution is Spec-Kit Plus's answer to a critical question: **What standards apply to every piece of work you do?** Not just for this feature, but for all features. Not just this week, but for the life of the project.

Think of your project Constitution like the U.S. Constitution—it's the foundational document that all laws (specifications), policies (plans), and implementation (code) must respect. It's written once, ratified (committed to git), and then every feature works within its constraints.

---

## Part A: What Is a Constitution? (10 minutes)

Before writing one, let's understand what a Constitution actually is and why it matters.

### Constitution: Global Rules, One Per Project

A **Constitution** is a document that defines **immutable standards** applying to **all features** in a project. It's distinct from a **Specification**, which applies to **one feature**.

**Constitution applies to**:
- Code quality standards (type hints, docstrings, naming conventions)
- Testing requirements (unit tests, integration tests, coverage targets)
- Error handling patterns (exception hierarchy, error messages, logging)
- Security practices (no hardcoded secrets, input validation, data handling)
- Documentation expectations (README, code comments, docstrings)

**Specification applies to**:
- Specific feature requirements (calculator should add, subtract, multiply, etc.)
- User stories for that feature
- Acceptance criteria for that feature
- Edge cases specific to that feature

**Example**:

```
CONSTITUTION (applies to ALL features):
  ✅ "All functions must have type hints"
  ✅ "All code must be 100% test-covered"
  ✅ "Division by zero raises ValueError"

SPECIFICATION (applies only to CALCULATOR feature):
  ✅ "Calculator must support add, subtract, multiply, divide, power"
  ✅ "Power operation handles negative exponents"
  ✅ "Results return float with 6-decimal precision"
```

### Why Constitution Matters: The Cascade

The Constitution is the **starting point of the cascade**:

```
Clear Constitution
    ↓
(ensures that every spec follows quality standards)
    ↓
Clear Specification
    ↓
(ensures that planning is feasible)
    ↓
Clear Plan
    ↓
(ensures that tasks are well-defined)
    ↓
Clear Tasks
    ↓
(enables correct code generation)
    ↓
Working Code
```

**Weak Constitution** produces:
- Specs that are vague about error handling
- Plans that don't account for testing
- Code that's missing type hints
- Integration issues because standards weren't enforced upstream

**Strong Constitution** produces:
- Specs that automatically include quality criteria
- Plans with testing built in
- Code that's consistent and maintainable
- Integration that works because standards were clear from the start

### Constitution is One-Time, Feature Work is Repetitive

This is crucial: You write the Constitution **once per project**. Then, for each feature, you:

1. Write a specification (addressing this feature only)
2. Generate a plan
3. Generate tasks
4. Implement code

But you never rewrite the Constitution for each feature. It's the foundation everything builds on.

**Best Practice Pattern**:

```
1. Initialize project
2. Write Constitution
3. Commit Constitution to git
4. FOR EACH FEATURE:
   - Run /sp.specify (new specification)
   - Run /sp.clarify (refine specification)
   - Run /sp.plan (new plan for this feature)
   - Run /sp.tasks (new tasks for this feature)
   - Run /sp.implement (new code for this feature)
   - Commit feature to git
```

---

## Part B: Reading Existing Constitutions (15 minutes)

Before writing your own, let's look at real examples to understand what a good Constitution looks like.

### Example 1: Calculator Project Constitution (Our Project)

Here's what a Constitution for a calculator might include:

```markdown
# Calculator Project Constitution

## Code Quality Standards

- All functions must include type hints on parameters and return types
- All functions must include PEP 257 docstrings
- All code must follow PEP 8 naming conventions
- Maximum line length: 100 characters
- No hardcoded test data in production code

## Error Handling

- Division by zero raises ValueError with message: "Cannot divide by zero"
- Invalid input types raise TypeError with descriptive message
- All operations validate inputs before processing
- Errors are logged to stderr with full context
- No silent failures; errors must be explicit

## Type System

- Accept int or float inputs
- Return float for all operations
- Preserve floating-point precision (minimum 6 decimal places)
- Explicit type conversions where needed
- No implicit coercion between types

## Testing Requirements

- 100% code coverage required (no untested code)
- Unit tests for each operation
- Edge case tests (zero, negative, very large numbers)
- Integration tests for operation chains
- All tests must pass before code review
- Acceptable coverage gaps: only test infrastructure code

## Documentation

- README.md with installation and usage examples
- Docstrings for all public functions
- Inline comments for non-obvious logic
- Example usage in docstrings (doctests where appropriate)
```

### Example 2: Data Processing Pipeline Constitution

To see how Constitution varies by project type, here's what a data pipeline Constitution might look like:

```markdown
# Data Pipeline Constitution

## Data Integrity

- All datasets must pass validation before processing
- Track data lineage (where did this data come from?)
- Preserve original data (never mutate input files)
- Version all processed datasets with timestamps

## Logging & Monitoring

- All processes log start/end times and record counts
- Errors must include context (which record failed? why?)
- Performance warnings if processing exceeds SLA (e.g., > 1 hour)
- Daily summary email with metrics

## Failure Handling

- Partial failures are acceptable (skip bad records, log them)
- Every failed record must be retrievable for manual review
- Pipeline must be re-runnable (idempotent)
- Rollback procedure documented
```

**The Key Insight**: Constitutions are project-specific. Your calculator Constitution would never mention "data lineage" because that's not relevant. A data pipeline Constitution wouldn't need type hints or power operations.

---

## Part C: Writing Your Calculator Constitution (50 minutes)

Now let's write YOUR Constitution for the calculator project.

### Step 1: Create the Constitution File

In your project directory, open `.specify/memory/constitution.md` (you may have started this in Lesson 1). Replace its contents with your calculator-specific Constitution.

### Step 2: Define Quality Standards

Think about what "good code" means for a calculator project:

```markdown
# Calculator Project Constitution

## Code Quality Standards

- All functions must include type hints on parameters and return types
  - Example: `def add(a: float, b: float) -> float:`
- All functions must include docstrings explaining what they do
  - Example: `"""Add two numbers and return the sum."""`
- Follow PEP 8 naming conventions (lowercase_with_underscores for functions)
- Lines must be under 100 characters
- No magic numbers; use named constants
  - Bad: `if x > 10:`
  - Good: `if x > MAX_POWER_EXPONENT:`
```

**Try writing 3-4 quality standards for your calculator. Think about**:
- How will you know if code is "good"?
- What would "bad" code look like?
- What would make code hard to maintain?

### Step 3: Define Error Handling Rules

Calculators are all about edge cases. What should happen when:

```markdown
## Error Handling

- Division by zero raises ValueError("Cannot divide by zero")
  - Never return None or infinity
  - Always raise an explicit error
- Operations with invalid input types raise TypeError
  - Example: calculator.add("5", 3) should raise TypeError, not crash silently
- All errors include clear messages that help debugging
  - Bad: "Error"
  - Good: "Cannot divide by zero: attempted 10 / 0"
- Errors are immediate; no silent failures
```

**Try writing**:
- What happens when you try to do power(0, 0)?
- What happens when you try to do power(-2, 0.5) (negative number, fractional exponent)?
- Should floats like power(2, 0.5) be allowed? What's the rule?

### Step 4: Define Type System Rules

```markdown
## Type System

- Accept int or float inputs
  - Both 5 and 5.0 are valid
- Always return float for all operations
  - 3 + 4 returns 7.0 (not 7)
  - This ensures consistency
- Preserve floating-point precision
  - Minimum 6 decimal places for results
  - Example: 1/3 = 0.333333 (not 0.33)
- No implicit type coercion
  - `add(5, "3")` should raise TypeError
  - Don't try to be "helpful" by converting
```

**Try writing**:
- Should power(2, 2) return 4 or 4.0? Why does it matter?
- What precision is "good enough"? 6 decimals? 10? 15?

### Step 5: Define Testing Requirements

```markdown
## Testing Requirements

- Every function must have unit tests
  - test_add(), test_subtract(), test_multiply(), test_divide(), test_power()
- 100% code coverage
  - No untested code paths
  - Tool: Use pytest with coverage plugin
- Edge case tests for each operation
  - Zero as input or output
  - Negative numbers
  - Very large numbers
  - Very small numbers (close to zero)
- Integration tests
  - Chains of operations (3 + 4 * 5)
  - Error conditions don't break subsequent calls
- All tests must pass before committing
```

**Try writing**:
- What edge cases should division handle?
  - Dividing by very small numbers?
  - Dividing very large numbers?
- What edge cases should power handle?
  - Negative exponents (2^-2 = 0.25)?
  - Fractional exponents (2^0.5 = 1.414...)?
  - Power of zero (5^0 = 1)?

### Step 6: Complete Your Constitution

Using the examples and prompts above, write a complete Constitution for your calculator project. Your Constitution should have:

- ✅ Code Quality Standards (3-4 items)
- ✅ Error Handling (4-5 items)
- ✅ Type System (3-4 items)
- ✅ Testing Requirements (4-5 items)

**Example Complete Constitution** (simplified):

```markdown
# Calculator Project Constitution

## Code Quality Standards

All functions must include type hints and docstrings. Follow PEP 8 naming (lowercase_with_underscores). Maximum line length is 100 characters. No magic numbers; use named constants.

## Error Handling

- Division by zero raises ValueError("Cannot divide by zero")
- Invalid input types raise TypeError with descriptive message
- Operations validate inputs before processing
- Errors include clear messages for debugging

## Type System

- Accept int or float inputs
- Always return float
- Preserve floating-point precision (6+ decimals)
- Explicit type handling; no implicit coercion

## Testing Requirements

- 100% code coverage required
- Unit tests for each operation (add, subtract, multiply, divide, power)
- Edge case tests (zero, negative, very large, very small inputs)
- Integration tests for operation chains
- All tests must pass before committing
```

---

## Part D: Commit Constitution to Git (15 minutes)

Here's a critical best practice: **Always commit the Constitution before starting feature work.**

### Why Commit First?

1. **Immutability**: Constitution is foundational; committing it signals "this is our standard"
2. **Clarity**: Everyone (including your AI orchestrator) sees the Constitution as the baseline
3. **Traceability**: Git history shows when and why Constitution was created
4. **Reversibility**: If you need to, you can revert to a previous Constitution (rarely happens, but important)

### Commit Steps

In your terminal, from the `calculator-project` directory:

```bash
# Verify your Constitution is in place
cat .specify/memory/constitution.md

# Add the Constitution to git
git add .specify/memory/constitution.md

# Commit with a clear message
git commit -m "Initial Constitution for calculator project

- Code quality: type hints, docstrings, PEP 8 compliance
- Error handling: explicit error messages, no silent failures
- Type system: accept int/float, return float, 6+ decimal precision
- Testing: 100% coverage, unit/edge/integration tests"

# Verify commit succeeded
git log --oneline -n 3
```

**What you should see**:
```
abcd1234 Initial Constitution for calculator project
xyz9876w Initial Spec-Kit Plus setup
```

The Constitution is now **the foundation** for all your feature work. Every specification you write, every plan you generate, every task you break down—they all work within the Constitution's constraints.

---

## Validation Checklist

Before moving to Lesson 3, verify your Constitution:

**Content Completeness**:
- [ ] Constitution defines code quality standards (type hints, docstrings, naming, line length)
- [ ] Constitution defines error handling rules (at least 3 rules)
- [ ] Constitution defines type system rules (accepted inputs, return types, precision)
- [ ] Constitution defines testing requirements (100% coverage, unit/edge/integration tests)
- [ ] Constitution is specific to calculator project (not generic boilerplate)

**File & Git**:
- [ ] Constitution is at `.specify/memory/constitution.md`
- [ ] Constitution is committed to git
- [ ] Git log shows the commit message clearly

**Quality**:
- [ ] Constitution is written in clear, testable language (not vague)
- [ ] Each rule is something you (and AI) can verify during code review
- [ ] Constitution balances strictness (not too permissive) and practicality (not impossible)

---

## Try With AI: Validate Your Constitution

Now let's use your AI companion to review your Constitution and ensure it's clear enough that specs, plans, and code can build on it without ambiguity.

### Setup

**Tool**: Claude Code (or your configured AI orchestrator)

**Context**: Your calculator-project directory with Constitution ready for review

**Goal**: Ensure Constitution is clear, testable, and specific enough to guide downstream work

### Prompt Set (Copy-Paste Ready)

**Prompt 1 — Constitution Clarity Check**

Copy and paste this into Claude Code:

```
I've written a Constitution for my calculator project. Please review it for clarity:

1. Are all rules testable? (Can you verify during code review?)
2. Are any rules vague or ambiguous?
3. Do I cover the essential categories (quality, error handling, types, testing)?

Here's my Constitution:

[PASTE YOUR CONSTITUTION HERE]

Please identify any rules that need clarification.
```

**Prompt 2 — Cascade Validation**

After reviewing clarity, ask:

```
Now imagine I'm writing a specification for the calculator's divide operation.
Looking at my Constitution, what constraints must my spec respect?

- What error handling must the divide spec include?
- What type system rules must divide follow?
- What testing requirements must divide meet?

This helps me understand if my Constitution is specific enough to guide specs.
```

**Prompt 3 — Reality Check**

Finally, ask:

```
Is my Constitution realistic for a calculator project, or am I being too strict?
- Type hints on every function: reasonable?
- 100% test coverage: reasonable?
- 6+ decimal precision: reasonable?

Any advice on making it more practical without sacrificing quality?
```

### Expected Outcomes

After these prompts, you should understand:

✅ **Constitution clarity**: Rules are testable and specific (not vague philosophy)
✅ **Cascade impact**: You can trace how Constitution rules flow into specifications
✅ **Realism**: Standards are ambitious but achievable
✅ **Readiness**: You're prepared to write specifications that respect the Constitution

### Safety & Ethics Note

**Constitution as Constraint, Not Straitjacket**:

The Constitution is a **guide, not a prison**. If you discover during specification that one rule is impractical (e.g., 6 decimal precision causes float precision issues), you can refine the Constitution in the future. But start strict—it's easier to relax rules than to add rigor later.

**Important**: The AI orchestrator will reference your Constitution when generating plans and code. A clear Constitution makes the orchestrator's job easier and produces better output.

---

**You've completed Lesson 2**. Your Constitution is now the foundation for all calculator project work. In Lesson 3, you'll write your first Specification—and you'll see how Constitution quality enables clear specifications.

Next: [Lesson 3: Specify Phase — Writing Complete Specifications](./03-specify-phase.md)
