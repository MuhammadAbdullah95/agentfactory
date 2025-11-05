---
title: "Plan Phase — Architecture Decisions and ADRs"
chapter: 31
lesson: 5
duration_minutes: 120

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Using /sp.plan Command"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can run /sp.plan and interpret generated implementation plan"

  - name: "Understanding Implementation Plan Structure"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student understands plan components (phases, dependencies, milestones)"

  - name: "Identifying Architecturally Significant Decisions"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student recognizes which decisions warrant ADR documentation (long-term impact, alternatives, future questioning)"

  - name: "Writing Architectural Decision Records (ADRs)"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can write ADR documenting decision title, context, decision, consequences, alternatives"

  - name: "Recognizing Cascade Quality (Plan from Spec)"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student observes how clear specs produce clear plans and how vague specs produce vague plans"

learning_objectives:
  - objective: "Use /sp.plan to generate implementation plan from calculator specification"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful execution of /sp.plan and understanding of generated plan"

  - objective: "Identify 2-3 architecturally significant decisions in calculator implementation plan"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Articulation of decisions with long-term impact and multiple alternatives"

  - objective: "Write ADRs documenting calculator architecture decisions"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "ADR documentation completeness (title, context, decision, consequences, alternatives)"

  - objective: "Understand plan structure and recognize how spec quality determines plan quality"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explanation of plan components and cascade effect"

cognitive_load:
  new_concepts: 7
  assessment: "7 new concepts (Plan command, plan structure, architectural decisions, ADR components, decision significance, consequences analysis, alternatives consideration) within B1 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Write 3-5 ADRs; analyze which decisions would change if spec requirements changed"
  remedial_for_struggling: "Focus on identifying top 2 ADRs; use provided ADR template without multiple alternatives"

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/10-chapter-31-redesign/spec.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "manual-implementation"
version: "1.0.0"
---

# Lesson 5: Plan Phase — Architecture Decisions and ADRs

You have a clear specification. Now comes planning: **How will you build it?**

The Planning phase transforms **What** (specification) into **How** (architecture and implementation strategy).

`/sp.plan` generates an implementation plan that breaks your specification into:
- **Architectural components** (core library, error handlers, type system, tests)
- **Implementation phases** (build operations first, then tests, then documentation)
- **Dependencies** (what must be built before what)
- **Design decisions** (which ones matter enough to document)

This lesson teaches you how to work with generated plans and how to capture important architectural decisions using **ADRs (Architectural Decision Records)**.

---

## Part A: Understanding the /sp.plan Command (20 minutes)

### What Does /sp.plan Do?

`/sp.plan` analyzes your specification and generates a detailed implementation plan by:

1. **Breaking spec into components** — Which parts of your spec need separate modules?
2. **Ordering dependencies** — What must be built first?
3. **Identifying design decisions** — Where are there multiple valid approaches?
4. **Proposing architecture** — How should code be organized?

**Input**: Your specification (what the calculator must do)

**Output**: Implementation plan with:
- Architecture overview
- Implementation phases
- Component breakdown
- Dependencies and sequencing
- Design decisions highlighted

### Example: Simple vs Complex Plan

**Calculator Spec** (simple):
> "Build a calculator with add, subtract, multiply, divide, power. Return floats. Handle division by zero."

**Generated Plan** (might be simple):
```
Phase 1: Core Operations Module
- Implement add(x, y) → float
- Implement subtract(x, y) → float
- Implement multiply(x, y) → float
- Implement divide(x, y) → float (handle zero)
- Implement power(x, y) → float

Phase 2: Tests
- Unit tests for all 5 operations
- Edge case tests

Phase 3: Documentation
- Docstrings
- README with examples
```

**Calculator Spec** (detailed with edge cases, type validation, precision requirements):
> "Build calculator with 5 operations. Accept int/float, return float. Handle division by zero, negative exponents, type validation. Preserve 6+ decimal precision. Support operation chaining."

**Generated Plan** (more complex):
```
Phase 1: Type System & Validation
- Define input validation layer
- Decide: check types in each operation or in wrapper?
- Implement numeric type checking and coercion rules

Phase 2: Core Operations
- Implement basic operations (add, subtract, multiply)
- Implement division with zero-handling
- Implement power with negative/fractional exponent handling

Phase 3: Precision & Output Formatting
- Define float precision requirements
- Implement output formatting for 6+ decimal places
- Handle floating-point edge cases (overflow, underflow)

Phase 4: Testing Strategy
- Unit tests per operation
- Edge case tests (negative numbers, zero, overflow)
- Integration tests (operation chaining)

Phase 5: Documentation
- API documentation
- Usage examples
- Edge case documentation
```

**The Cascade Effect**: Detailed spec → detailed plan. Vague spec → vague plan.

---

## Part B: Generating Your Implementation Plan (30 minutes)

Let's generate the plan for your calculator.

### Step 1: Run /sp.plan

In Claude Code, from your calculator-project directory:

```
/sp.plan

My calculator specification is at specs/calculator/spec.md

Please generate an implementation plan that includes:
1. Architecture overview (how should code be organized?)
2. Implementation phases (in what order should I build?)
3. Component breakdown (what modules/functions are needed?)
4. Dependencies (what must be built before what?)
5. Design decisions (where are there multiple valid approaches?)

Output: Create specs/calculator/plan.md with the implementation plan.
```

### Step 2: Review Generated Plan

The generated plan should include:

- **Architecture Overview**: How code will be organized (one module? multiple? class-based?)
- **Implementation Phases**: 3-5 phases building from simple to complex
- **Component Breakdown**: Core operations, error handling, type validation, tests, docs
- **Sequencing**: Operations before tests? Validation before operations?
- **Design Decisions**: Where are there choices? (Class vs functions? Exception types? Precision handling?)

### Step 3: Save the Plan

The generated plan should be saved to `specs/calculator/plan.md`. Verify:

```bash
# Check that plan exists
cat specs/calculator/plan.md

# Verify it has structure
grep -E "^##|^Phase|^Decision" specs/calculator/plan.md
```

---

## Part C: Understanding ADRs (Architectural Decision Records) (20 minutes)

Planning exposes **architectural decisions** — choices about how to build that have long-term consequences.

### What Is an ADR?

An **ADR** documents:
- **The Decision**: What choice did you make?
- **The Context**: Why did you need to make this choice?
- **The Alternatives**: What other options existed?
- **The Rationale**: Why did you choose this over alternatives?
- **The Consequences**: What are the long-term impacts?

### When Should You Create an ADR?

**Create an ADR when**:
- The decision has **long-term impact** (affects code structure, not just style)
- **Multiple valid alternatives** existed (not an obvious choice)
- **Future developers will question** the decision
- The decision **constrains future choices** (e.g., choosing a data structure)

**Don't create ADRs for**:
- Style choices (naming conventions, formatting)
- Obvious choices (of course we use Python!)
- Temporary decisions (will revisit in 6 months)
- Out-of-scope decisions (already decided by Constitution)

### Calculator Examples

**ADR-Worthy Decisions**:

**Decision 1: Error Handling Strategy**
- Context: Need to handle division by zero, invalid inputs, overflow
- Alternatives:
  - A) Raise exceptions (Python standard)
  - B) Return None or error tuple
  - C) Silent failure (return 0)
- Chosen: A) Raise exceptions
- Rationale: Aligns with Python conventions; prevents silent errors; clear error messages
- Consequence: Callers must handle exceptions; no way to silently continue

**Decision 2: Type System (Strict Checking vs Coercion)**
- Context: Accept int or float inputs; what about strings?
- Alternatives:
  - A) Strict typing: reject non-numeric input (raise TypeError)
  - B) Lenient coercion: try to convert strings to numbers
  - C) Duck typing: accept anything with `__add__` method
- Chosen: A) Strict typing
- Rationale: Specification requires int/float only; Constitution mandates type hints; prevents silent bugs
- Consequence: Limits flexibility; callers must validate input first

**Not ADR-Worthy for Calculator**:
- Naming convention (add, subtract, multiply) — obvious from spec
- Using Python 3.13 — already Constitution decision
- Module organization (one file vs multiple) — implementation detail, not architectural

### ADR Structure Template

```markdown
# ADR-XXX: [Decision Title]

**Status**: Decided

**Context**
[Why did we need to make this decision? What problem are we solving?]

**Decision**
[What did we decide?]

**Alternatives Considered**
- A) [Alternative 1 and why we rejected it]
- B) [Alternative 2 and why we rejected it]
- C) [Chosen alternative and why]

**Rationale**
[Why is this the best choice? How does it align with Constitution?]

**Consequences**
- Positive: [Benefits of this decision]
- Negative: [Costs or limitations]

**Related Decisions**
- [Other ADRs this relates to, if any]
```

---

## Part D: Creating ADRs for Your Calculator Plan (40 minutes)

Now let's identify and document the architectural decisions from your calculator plan.

### Step 1: Identify Architectural Decisions

Review your generated plan and identify:
- **3-5 significant architectural decisions**
- Where the plan discusses options or tradeoffs

Example decisions to look for:
- Error handling strategy (exceptions vs return codes)
- Type system (strict typing vs coercion)
- Code organization (single module vs multiple modules)
- Precision handling (rounding strategy, format strings)
- Testing strategy (unit vs integration, coverage targets)

### Step 2: Create ADRs

For each significant decision, create an ADR file:

```bash
# Create ADRs directory if it doesn't exist
mkdir -p history/adr/

# Create first ADR
touch history/adr/001-error-handling-strategy.md
```

### Step 3: Write ADR Content

**Example ADR-001: Error Handling Strategy**

```markdown
# ADR-001: Error Handling Strategy for Calculator

**Status**: Decided (from calculator specification and Constitution)

**Context**
The calculator must handle error conditions (division by zero, invalid input types,
overflow on very large exponents). We need to decide how to report these errors to
the caller.

**Decision**
Use Python exceptions for all error conditions. Raise explicit exception types:
- ValueError for mathematical errors (e.g., division by zero)
- TypeError for invalid input types
- OverflowError for computation overflow

**Alternatives Considered**
- A) Return error tuples: (success: bool, result: float|None, error: str|None)
  - Rejected because forces callers to check tuple[0], less Pythonic
- B) Silent failure: return 0 or None on error
  - Rejected because hides bugs, Constitution requires clear error messages
- C) Use exceptions (chosen)
  - Aligns with Python conventions and Constitution error-handling standards
  - Error messages can be descriptive

**Rationale**
Exceptions are the Python standard for error handling. Constitution mandates
"Division by zero raises ValueError with descriptive message." Exceptions make
errors explicit and prevent silent bugs.

**Consequences**
- Positive: Clear error reporting, Pythonic, Constitution-compliant
- Negative: Callers must implement try/except blocks

**Related Decisions**
- Constitution requirement: "All errors logged with context"
- ADR-002: Type validation strategy (enforces TypeError on bad input)
```

**Example ADR-002: Type System (Strict vs Coercion)**

```markdown
# ADR-002: Type System — Strict Validation vs Lenient Coercion

**Status**: Decided

**Context**
Specification requires accepting "int or float" inputs. Question: Should we
strictly require numeric types, or try to coerce strings to numbers?

**Decision**
Strict validation: accept only int or float. Reject strings, lists, or other
types with TypeError.

**Alternatives Considered**
- A) Strict validation: only int/float (chosen)
  - Forces input validation by caller, prevents bugs
- B) Lenient coercion: try to convert strings to float
  - More flexible but hides bugs (add("5", 3) silently becomes 5 + 3)
  - Harder to debug when coercion fails
- C) Duck typing: accept anything with arithmetic operations
  - Too permissive, might accept wrong types

**Rationale**
Specification says "accept int or float"—string is neither. Constitution mandates
type hints and explicit type handling. Strict validation catches errors early.

**Consequences**
- Positive: Type-safe, catches bugs early, matches Constitution, easier to debug
- Negative: Less flexible, callers must validate input before calling

**Related Decisions**
- ADR-001: Exception-based error handling (TypeError for bad types)
- Constitution: "Type system — explicit type handling, no implicit coercion"
```

**Example ADR-003: Precision Handling**

```markdown
# ADR-003: Floating-Point Precision Strategy

**Status**: Decided

**Context**
Specification says "Results accurate to 6+ decimal places." Python's float has
~15-17 significant digits. How do we handle rounding, formatting, and precision
limits?

**Decision**
- Use Python's native float (IEEE 754 double precision)
- Results computed to full float precision (~15-17 significant digits)
- Results returned unrounded (user can format if needed)
- Document that results are accurate to float precision limits

**Alternatives Considered**
- A) Use Decimal for exact arithmetic
  - Would ensure exact 6+ decimals but adds complexity, slower
  - Overkill for calculator purposes
- B) Round all results to 6 decimals
  - Oversimplifies precision, loses information
- C) Native float (chosen)
  - Aligns with Python conventions, fast, sufficient for calculator use

**Rationale**
Python float is standard and sufficient. Specification says 6+ decimals, but
doesn't require rounding or Decimal precision. Native float achieves this.

**Consequences**
- Positive: Fast, standard Python behavior, sufficient precision
- Negative: Floating-point precision limits (e.g., 0.1 + 0.2 != 0.3 exactly)

**Related Decisions**
- Specification requirement: "6+ decimal place accuracy"
```

### Step 4: Commit ADRs

```bash
# Add all ADRs to git
git add history/adr/

# Commit with descriptive message
git commit -m "Document calculator architecture decisions

- ADR-001: Error handling strategy (exceptions)
- ADR-002: Type system (strict validation)
- ADR-003: Floating-point precision strategy"
```

---

## Part E: Cascade Validation

Observe the cascade:

**Specification Quality → Plan Quality → ADR Clarity**

Your clear, detailed specification from Lessons 3-4 should have produced:
- ✅ Clear implementation plan (not vague)
- ✅ Obvious architectural decisions (not ambiguous)
- ✅ Easy-to-write ADRs (clear context and rationale)

If your plan is vague or ADRs are hard to write, it signals that your specification needed more detail.

---

## Try With AI: Validate Your Plan and ADRs

Use your AI companion to review your implementation plan and ADRs.

### Setup

**Tool**: Claude Code (or your configured AI orchestrator)

**Context**: Your plan.md and 2-3 ADRs

**Goal**: Confirm plan is sound and ADRs capture key architectural decisions

### Prompt Set (Copy-Paste Ready)

**Prompt 1 — Plan Review**

Copy and paste this into Claude Code:

```
I've generated an implementation plan for my calculator.

My plan includes these phases:
[List your plan phases]

Looking at my specification, does this plan address all requirements?
Are the phases in the right order? Any missing components?

Here's my plan:
[PASTE YOUR PLAN.MD HERE]
```

**Prompt 2 — ADR Completeness**

After plan review, ask:

```
I've documented these architectural decisions:
[List your ADR titles]

Are these the most important decisions? Did I miss any critical architectural
choices? Should I add more ADRs, or are 2-3 sufficient for a calculator?
```

**Prompt 3 — Plan to Tasks Readiness**

Finally, ask:

```
Based on my plan and ADRs, am I ready for the Tasks phase (Lesson 6)?

Tasks will break my plan into atomic work units (1-2 hour tasks).
Is my plan detailed enough that tasks will be clear and unambiguous?
```

### Expected Outcomes

✅ **Plan is sound and complete**
✅ **ADRs capture key architectural decisions**
✅ **Specification quality has cascaded into plan and ADR quality**
✅ **Ready for task breakdown (Lesson 6)**

### Safety & Ethics Note

**On AI-Generated Plans**:

Your AI companion generates plans based on your specification. If you think the plan is wrong, **check your specification first**. Most planning issues trace back to spec gaps. ADRs document why you chose your approach—they're not "final word," but reasoning that future you can reference.

---

**You've completed Lesson 5**. Your calculator has an implementation plan and documented architectural decisions. In Lesson 6, you'll use the `/sp.tasks` command to break this plan into atomic work units—and learn the critical **checkpoint pattern** that keeps you in control of the workflow.

Next: [Lesson 6: Tasks Phase — Atomic Work Units and Checkpoints](./06-tasks-phase.md)
