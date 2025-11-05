---
title: "Specify Phase — Writing Complete Specifications"
chapter: 31
lesson: 3
duration_minutes: 120

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Evals-First Thinking (Pre-Specification Collaboration)"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can conduct informal human-AI conversation about success criteria BEFORE formal specification"

  - name: "Writing SMART Acceptance Criteria"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can convert vague requirements into Specific, Measurable, Achievable, Relevant, Time-bound criteria"

  - name: "Complete Specification Writing"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can write specification with Overview, Scope, Requirements, Acceptance Criteria, Constraints"

  - name: "Identifying Edge Cases"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify edge cases (division by zero, negative exponents, type mismatches, boundary conditions)"

  - name: "Distinguishing User Stories from Acceptance Criteria"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain that user stories describe intent while acceptance criteria describe testable verification"

learning_objectives:
  - objective: "Conduct informal evals-first discussion with AI to clarify success criteria before writing formal specification"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Completion of pre-specification conversation with AI companion"

  - objective: "Write complete calculator specification with 5 operations and clear acceptance criteria"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Specification completeness review (all required sections included)"

  - objective: "Convert vague requirements into SMART acceptance criteria"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "SMART criteria validation (Specific, Measurable, Achievable, Relevant, Time-bound)"

  - objective: "Identify and document edge cases for calculator operations"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Edge case documentation completeness and relevance"

cognitive_load:
  new_concepts: 5
  assessment: "5 new concepts (Evals-first thinking, SMART criteria, Specification structure, Edge cases, User stories vs criteria) within B1 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Write specifications for 2 additional projects; compare how specification style differs based on project type (CLI tool vs library vs API)"
  remedial_for_struggling: "Use provided specification template with examples; focus only on the 5 core operations before exploring edge cases"

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/10-chapter-31-redesign/spec.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "manual-implementation"
version: "1.0.0"
---

# Lesson 3: Specify Phase — Writing Complete Specifications

Welcome to the most important phase: **Specification**. This is where you translate your vague ideas ("I want a calculator") into crystal-clear requirements that AI can build from.

Here's the paradigm shift: In AI-native development, **your ability to write a clear specification is more valuable than your ability to write code**. Bad code can be refactored. A bad spec causes cascading problems through planning, tasks, and implementation.

This lesson teaches you a professional practice called **evals-first thinking**—before you write a formal specification, you have an informal conversation with your AI companion about what "success" looks like. Then, you formalize that thinking into a specification.

---

## Part A: Evals-First Thinking (What Success Looks Like) (25 minutes)

Before writing a specification, professional teams define **evals**: criteria for evaluating whether the solution succeeds. This is NOT a formal phase; it's an informal human-AI conversation that clarifies intent.

### What Are Evals? (Beyond Testing)

**Evals** answer the question: **How will we know if this works?**

Not "does it compile?" or "do tests pass?" (those are technical validation). Real evals are **business/user criteria** that define success:

- **For a calculator**:
  - ✅ "Can perform basic arithmetic (add, subtract, multiply, divide)"
  - ✅ "Handles edge cases without crashing (division by zero, negative exponents)"
  - ✅ "Results are accurate to 6+ decimal places"
  - ✅ "Error messages are clear enough for users to understand what went wrong"

- **For a user-facing feature**:
  - ✅ "Users can complete the task in < 30 seconds"
  - ✅ "Error messages help users recover without contacting support"
  - ✅ "Experienced and new users succeed at same rate"

- **For an API**:
  - ✅ "API responds in < 200ms for 95% of requests"
  - ✅ "Requests with invalid input are rejected with helpful error messages"
  - ✅ "Pagination works for results of any size"

### Evals ≠ Test Cases

**Common misconception**: "Evals are just test cases."

Not quite. Here's the difference:

```
TEST CASE (technical validation):
- Input: 5, 3
- Expected: 8
- Validation: Assert result == 8

EVAL (business/user validation):
- "Calculator adds two positive integers correctly"
- "Results are accurate to floating-point precision"
- "User can chain operations without intermediate rounding errors"
```

Tests verify that implementation works. Evals verify that implementation solves the right problem.

### Evals-First Pattern: The Pre-Specification Conversation

Here's how professionals work:

**Step 1: YOU Drive the Exploration Through Questions**

**Critical**: YOU ask the questions to explore the problem space. The AI doesn't interview you; you use the AI to think through requirements.

```
You: "I want to build a calculator"

You: "What operations should a basic calculator include?"

AI: "Common operations are add, subtract, multiply, divide, and power (exponentiation).
     Those five operations cover most basic arithmetic needs."

You: "What edge cases do I need to consider for these operations?"

AI: "Key edge cases:
     - Division by zero (should error)
     - Negative exponents (e.g., 2^-3)
     - 0^0 (mathematically undefined)
     - Very large numbers (overflow handling)
     - Type mixing (int and float inputs)"

You: "Should results be integers or floats?"

AI: "Floats are better for arithmetic operations because:
     - Division naturally produces decimals (5/2 = 2.5)
     - Power operations often produce decimals (2^0.5 = 1.414...)
     - Consistent return type simplifies usage
     - Python's float has ~15-17 decimal places of precision"

You: "How precise do the results need to be?"

AI: "For a basic calculator, 6 decimal places minimum is standard:
     - Enough for most practical calculations
     - Avoids floating-point display noise
     - Matches calculator conventions"

You: "What interface makes sense—CLI, library, or web?"

AI: "For learning SDD, a Python library (importable module) is best:
     - Simple to test
     - Easy to validate specifications
     - Can add CLI/web later if needed
     - Focus on core logic first"

You: "So if I understand correctly, success looks like:
     ✅ 5 operations (add, subtract, multiply, divide, power)
     ✅ All results return float
     ✅ Minimum 6 decimal precision
     ✅ Division by zero raises clear error
     ✅ Handles negative numbers and large numbers
     ✅ Importable as Python library

     Does that cover the essentials?"

AI: "Yes! Those are your evals—the success criteria. Now let's formalize this into a specification using /sp.specify."
```

**Step 2: Formalize Into Specification**

That conversation becomes the specification's acceptance criteria. The spec says, "Here's what the calculator must do" (derived from the evals conversation you just had).

### Why Evals-First Matters

1. **Prevents Misunderstanding**: You and AI agree on success BEFORE work starts
2. **Guides Specification**: Evals inform what goes into the spec
3. **Enables Validation**: You can verify later that implementation matches evals
4. **Cascades Quality**: Clear evals → clear spec → clear plan → working code

---

## Part B: Writing SMART Acceptance Criteria (20 minutes)

Now that you've clarified success (evals), you'll formalize requirements using **SMART criteria**.

### What Makes Criteria "SMART"?

SMART stands for: **S**pecific, **M**easurable, **A**chievable, **R**elevant, **T**ime-bound

Let's see how this works for calculator operations:

### Example 1: Addition (Vague vs SMART)

**Vague Criterion**:
> "The calculator should add two numbers correctly"

**Problems**: Ambiguous ("correctly"?), untestable, no edge cases, no precision definition

**SMART Criterion**:
> "Calculator.add() accepts two int or float inputs and returns a float with sum accurate to 6+ decimal places. Rejects non-numeric inputs with TypeError. Examples: add(5, 3) = 8.0, add(-2.5, 3.7) = 1.2"

**Why SMART**:
- **Specific**: Exactly what it does (accepts numbers, returns float, rejects bad input)
- **Measurable**: You can test it (6+ decimal precision, TypeError for bad input)
- **Achievable**: Python's float supports this
- **Relevant**: Aligns with calculator evals (works with int/float, accurate results)
- **Time-bound**: Not applicable for individual operations (more relevant for project deadlines)

### Example 2: Division (Vague vs SMART)

**Vague**:
> "Division should handle edge cases"

**Problems**: What edge cases? How should it handle them? Untestable.

**SMART**:
> "Calculator.divide() accepts two numeric inputs. If divisor is zero, raises ValueError with message 'Cannot divide by zero'. Otherwise returns float result accurate to 6+ decimal places. Rejects non-numeric input with TypeError. Examples: divide(10, 2) = 5.0, divide(10, 0) raises ValueError, divide('a', 5) raises TypeError"

**Why SMART**:
- **Specific**: Three cases clearly defined (normal division, zero divisor, bad input)
- **Measurable**: Each case has verifiable behavior
- **Achievable**: Standard Python exception handling
- **Relevant**: Aligns with Constitution error-handling rules and evals
- **Time-bound**: Not applicable here

### Example 3: Power (Vague vs SMART)

**Vague**:
> "Power operation should work with positive and negative exponents"

**Problems**: What does "work" mean? What about fractional exponents? Overflow?

**SMART**:
> "Calculator.power() accepts numeric base and numeric exponent. Returns float accurate to 6+ decimal places. Handles: positive exponents (2^3 = 8.0), negative exponents (2^-2 = 0.25), fractional exponents (2^0.5 = 1.414...). Raises ValueError if base is negative and exponent is non-integer (e.g., power(-2, 0.5)). Rejects non-numeric input with TypeError. Results with exponent >= 1000 raise OverflowError."

**Why SMART**:
- **Specific**: All cases explicitly covered
- **Measurable**: Each scenario has expected behavior
- **Achievable**: Python supports all cases
- **Relevant**: Handles real-world edge cases (negative exponents, fractional exponents)
- **Time-bound**: Not applicable

---

## Part C: Specification Components (30 minutes)

A complete specification has these sections. Let's explore each:

### 1. Overview (1-2 paragraphs)

What is this feature? Why are we building it? What problem does it solve?

**Example for Calculator**:

> "Build a Python calculator library supporting 5 operations: add, subtract, multiply, divide, power. The calculator serves as a learning project demonstrating Spec-Kit Plus workflow and AI-driven development. Users import and call operations as a Python library (not a CLI)."

**Not needed**: Technical implementation details. Just "what is this" and "why build it".

### 2. Scope (What's In / What's Out)

**In Scope** (we'll build):
- Add, subtract, multiply, divide, power operations
- Integer and float inputs
- Error handling for division by zero, invalid inputs
- Type hints and docstrings

**Out of Scope** (we won't build):
- CLI or web interface (Python library only)
- Advanced operations (logarithm, trigonometry, square root—separate library)
- Performance optimization (library works correctly; speed optimization is future work)
- Unit conversion (weight, temperature—separate library)

**Why Scope Matters**: Prevents scope creep. If someone asks "Can you add square root?" you can say "No, that's out of scope for this project."

### 3. Functional Requirements (What It Does)

List the core features as user stories:

```
As a Python developer, I can import the calculator library
As a Python developer, I can call calculator.add(5, 3) to get 8.0
As a Python developer, I can call calculator.divide(10, 2) to get 5.0
As a Python developer, I get a clear error when dividing by zero
As a Python developer, I get a clear error when passing non-numeric input
```

Each user story answers: Who wants this? What do they want to do? Why?

### 4. Acceptance Criteria (How We Know It Works)

This is where your SMART criteria go. Group by operation:

```
## Acceptance Criteria

### Add Operation
- add(5, 3) returns 8.0 (float)
- add(1.5, 2.5) returns 4.0
- add(-3, 5) returns 2.0
- Rejects add("5", 3) with TypeError
- Returns float (not int) even for integer inputs

### Divide Operation
- divide(10, 2) returns 5.0
- divide(10, 3) returns 3.333333 (6+ decimals)
- divide(10, 0) raises ValueError("Cannot divide by zero")
- Rejects divide("10", 2) with TypeError

### Power Operation
- power(2, 3) returns 8.0
- power(2, -2) returns 0.25 (negative exponent)
- power(2, 0.5) returns 1.414... (fractional exponent)
- power(-2, 0.5) raises ValueError (can't take root of negative)
- power(2, 1000) might raise OverflowError (very large results)
- Rejects power("2", 3) with TypeError
```

### 5. Edge Cases & Constraints

```
## Edge Cases
- Very large numbers (e.g., 10^308 approaches float max)
- Very small numbers (e.g., 10^-308 approaches float min)
- Negative numbers in inputs
- Zero as input or output
- Floating-point precision limits

## Constraints
- Must follow Constitution standards (type hints, docstrings, 100% test coverage)
- Results accurate to 6+ decimal places
- All error messages must be clear and helpful
- No hardcoded test data in code
```

### Example: Complete Calculator Specification

Here's what your complete specification might look like:

```markdown
# Calculator Specification

## Overview

Build a Python calculator library supporting 5 basic operations: add, subtract,
multiply, divide, power. This serves as a learning project demonstrating
Spec-Kit Plus workflow and AI-driven development. Users import the library
as a Python module and call operations directly.

## Scope

### In Scope
- 5 operations: add, subtract, multiply, divide, power
- Integer and float inputs
- Clear error handling for edge cases
- Type hints and docstrings

### Out of Scope
- CLI or web interface (Python library only)
- Advanced operations (logarithm, trigonometry, square root)
- Performance optimization
- Unit conversion or other domains

## User Stories

- As a developer, I can import calculator and use it as a library
- As a developer, I can perform 5 basic operations
- As a developer, I get clear errors for division by zero
- As a developer, I get clear errors for invalid input types
- As a developer, all results follow consistent precision (6+ decimals)

## Acceptance Criteria

### Addition
- add(5, 3) returns 8.0
- add(1.5, 2.5) returns 4.0
- add(-3, 5) returns 2.0
- add("5", 3) raises TypeError

### Subtraction
- subtract(10, 3) returns 7.0
- subtract(5, 10) returns -5.0
- subtract(1.5, 0.5) returns 1.0
- subtract("10", 3) raises TypeError

### Multiplication
- multiply(4, 5) returns 20.0
- multiply(-2, 3) returns -6.0
- multiply(1.5, 2) returns 3.0
- multiply("4", 5) raises TypeError

### Division
- divide(10, 2) returns 5.0
- divide(10, 3) returns 3.333333
- divide(-10, 2) returns -5.0
- divide(10, 0) raises ValueError("Cannot divide by zero")
- divide("10", 2) raises TypeError

### Power
- power(2, 3) returns 8.0
- power(2, -2) returns 0.25
- power(2, 0.5) returns 1.414...
- power(-2, 0.5) raises ValueError (can't take root of negative)
- power("2", 3) raises TypeError

## Edge Cases
- Very large exponents (e.g., 2^1000)
- Negative exponents (division by zero risk)
- Fractional exponents with negative base
- Zero as base or exponent
- Floating-point precision limits

## Constraints
- Follow project Constitution (type hints, docstrings, 100% test coverage)
- Results accurate to 6+ decimal places
- All error messages must be descriptive
- No hardcoded test values in production code
```

---

## Part D: Write Your Calculator Specification (35 minutes)

Now it's your turn. Use the structure above to write your complete calculator specification.

### Step 1: Start the Evals-First Conversation (10 minutes)

Open your AI companion (Claude Code) in your calculator-project directory and have this conversation:

```
I'm writing a specification for a calculator Python library.
Let me clarify what success looks like with you:

1. What operations should my calculator support?
2. What edge cases should I handle?
3. What's my definition of "correct" for floating-point results?
4. How should the calculator interface work? (Library vs CLI?)
5. What should happen with invalid inputs?

[Have the conversation with your AI companion]
```

Document the outcomes of this conversation. This is your **evals** — the criteria for success.

### Step 2: Create Your Specification File

```bash
# In your calculator-project directory
touch specs/calculator/spec.md
```

### Step 3: Write Your Specification

Use the template above as a guide. Include:

- ✅ **Overview** (1-2 paragraphs explaining what you're building)
- ✅ **Scope** (In Scope / Out of Scope)
- ✅ **User Stories** (5-6 stories covering all operations)
- ✅ **Acceptance Criteria** (SMART criteria for each of 5 operations)
- ✅ **Edge Cases** (division by zero, negative exponents, overflow, etc.)
- ✅ **Constraints** (Constitution rules, precision, error messages)

### Step 4: Verify Completeness

Check that your specification:

- [ ] Has clear overview explaining the calculator
- [ ] Clearly states in-scope (5 operations, error handling) and out-of-scope
- [ ] Includes 5+ user stories
- [ ] Has SMART acceptance criteria for each operation (minimum 4 criteria per operation)
- [ ] Documents edge cases (at least 3-4 per operation)
- [ ] References Constitution constraints
- [ ] Is written clearly enough that another developer could implement from it

---

## Validation: The Cascade Effect

Now test your specification's quality by asking: **Will this spec produce a good plan?**

A good spec has:
- ✅ Crystal-clear operations (no ambiguity)
- ✅ Explicit edge cases (no surprises during planning)
- ✅ SMART criteria (AI can build acceptance tests directly from them)
- ✅ Constraint alignment (specifications respect Constitution)

A bad spec has:
- ❌ Vague operations ("should work correctly" - what's "correct"?)
- ❌ Missing edge cases (surprises emerge during implementation)
- ❌ Ambiguous criteria ("handle errors"—how?)
- ❌ Ignores Constitution (specification asks for things Constitution forbids)

**Action**: Read your specification aloud. Does it sound clear? Would a developer understand exactly what to build?

---

## Try With AI: Get Specification Feedback

Now let's use your AI companion to validate your specification and ensure it's clear enough for planning.

### Setup

**Tool**: Claude Code (or your configured AI orchestrator)

**Context**: Your calculator specification (written in `specs/calculator/spec.md`)

**Goal**: Validate that your specification is specific, measurable, and complete

### Prompt Set (Copy-Paste Ready)

**Prompt 1 — Specification Completeness**

Copy and paste this into Claude Code:

```
I've written a specification for my calculator Python library.
Please review it for completeness and clarity:

1. Is every operation fully specified? (add, subtract, multiply, divide, power)
2. Are acceptance criteria SMART (Specific, Measurable, Achievable, Relevant)?
3. Did I cover edge cases adequately?
4. Would a developer know exactly what to build from this spec?

Here's my specification:

[PASTE YOUR SPECIFICATION HERE]

Please identify any ambiguities or missing details.
```

**Prompt 2 — SMART Criteria Validation**

After completeness review, ask:

```
Looking at my acceptance criteria, are they SMART?

For example, here's one of my criteria:
"divide(10, 0) raises ValueError"

Is this SMART? What would make it SMARTer?

Please review my top 5 acceptance criteria and rate each as:
- Specific: Yes/No
- Measurable: Yes/No
- Achievable: Yes/No
- Relevant: Yes/No

And suggest improvements if any are missing elements.
```

**Prompt 3 — Ready for Planning?**

Finally, ask:

```
Based on my specification, could a planning phase happen next?
In other words, is my spec specific enough that someone could design
a plan for implementing it?

What would you need to know BEFORE planning? Any remaining ambiguities?
```

### Expected Outcomes

After these prompts, you should be able to:

✅ **Identify any missing operations or criteria**
✅ **Confirm acceptance criteria are testable**
✅ **Know whether your spec is ready for Lesson 4 (clarification)**
✅ **Understand how spec quality enables plan quality**

### Safety & Ethics Note

**On AI-Generated Criteria**:

Your AI companion might suggest additional acceptance criteria or edge cases. That's helpful! But YOU decide whether to include them. The goal is YOUR understanding—not accepting suggestions blindly. Review any suggestions and ask: "Does this align with my calculator's purpose?"

---

**You've completed Lesson 3**. You now have a complete, clear calculator specification—the foundation for all downstream work. In Lesson 4, you'll use the `/sp.clarify` command to refine this specification further, exposing ambiguities your AI companion spots.

Next: [Lesson 4: Clarify Phase — Refining Specs with /sp.clarify](./04-clarify-phase.md)
