---
title: "Clarify Phase — Refining Specs with /sp.clarify"
chapter: 31
lesson: 4
duration_minutes: 90

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Using /sp.clarify Command"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can run /sp.clarify on existing specification and interpret feedback"

  - name: "Identifying Specification Gaps"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student recognizes ambiguities, missing assumptions, incomplete requirements in specifications"

  - name: "Iterative Specification Refinement"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student revises specification based on AI feedback and decides which suggestions to accept"

  - name: "Cascade Quality Improvement"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student understands how improved specifications lead to better plans"

  - name: "AI Feedback Interpretation"
    proficiency_level: "B1"
    category: "Soft"
    bloom_level: "Analyze"
    digcomp_area: "Communication & Collaboration"
    measurable_at_this_level: "Student evaluates AI suggestions critically and decides which feedback to implement"

learning_objectives:
  - objective: "Use /sp.clarify command to analyze calculator specification for gaps and ambiguities"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful execution of /sp.clarify and interpretation of feedback"

  - objective: "Identify and resolve specification ambiguities discovered by AI analysis"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Refined specification addressing all identified gaps"

  - objective: "Understand iterative refinement process: specification → AI feedback → revision → improvement"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explanation of how clarification process improved specification"

cognitive_load:
  new_concepts: 7
  assessment: "7 new concepts (Clarify command, gap identification, ambiguity resolution, AI feedback interpretation, iterative refinement, cascade improvement, human decision-making) within B1 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Run /sp.clarify multiple times; document how specification evolves with each iteration; analyze what kinds of gaps AI discovers"
  remedial_for_struggling: "Focus on top 3-4 clarifying questions from AI; resolve those before moving to planning"

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/10-chapter-31-redesign/spec.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "manual-implementation"
version: "1.0.0"
---

# Lesson 4: Clarify Phase — Refining Specs with /sp.clarify

You've written a calculator specification. It looks good. But there are always gaps you didn't catch—ambiguities that seemed clear in your head but are actually unclear on paper. Edge cases you missed. Assumptions you didn't state explicitly.

This is where the `/sp.clarify` command helps. **Clarify is NOT a formal workflow phase** like `/sp.specify` or `/sp.plan`. It's a **quick check** that your specification is complete before moving to planning.

Think of `/sp.clarify` as your AI companion putting on a "devil's advocate" hat and asking: "Wait, what about...?" It finds gaps you might have missed, then you decide whether to update your spec.

The goal: Make your specification **so clear** that the planning phase can generate a perfect plan.

---

## Part A: What Does /sp.clarify Do? (15 minutes)

### The Clarify Command

`/sp.clarify` analyzes your specification and reports:

1. **Ambiguous Terms** — Words that could mean multiple things
   - Example: "should handle errors" (what errors? how should they be handled?)

2. **Missing Assumptions** — Things you assumed but didn't state
   - Example: You assumed division by zero is an error, but didn't state what exception type
   - Example: You assumed float precision, but didn't specify the Python precision limits

3. **Incomplete Requirements** — Operations or cases you didn't cover
   - Example: You specified divide(10, 2) but didn't specify divide(10, 0.0000001)
   - Example: You specified all operations individually but didn't specify operation chaining

4. **Constraint Conflicts** — Where spec might contradict Constitution
   - Example: Spec says "results are exact integers" but Constitution says "always return float"

5. **Edge Case Gaps** — Cases that should be handled but aren't documented
   - Example: What happens with power(2, 10000)? Overflow?
   - Example: What happens with very small numbers (e.g., 0.000000001)?

### Example: What /sp.clarify Might Find

**Your Specification**:
> "divide(10, 2) returns 5.0"

**Clarify Feedback**:
> "This criterion is clear, but several related cases aren't specified:
> - What happens with divide(10, 0.00001)? Precision loss?
> - What's the maximum divisor that still produces accurate results?
> - Do you want integer division or float division?"

**Your Response**:
> "Good catch! Let me clarify:
> - Float division always (10 / 3 = 3.333..., not 3)
> - Results accurate to Python float precision (~15-17 significant digits)
> - Very small divisors are allowed (divide(10, 0.0001) = 100000.0)"

**Updated Spec**:
> "divide(x, y) performs float division and returns result accurate to Python's float precision (~15-17 significant digits). Examples: divide(10, 2) = 5.0, divide(10, 3) = 3.333..., divide(10, 0.0001) = 100000.0"

---

## Part B: The Clarify Workflow (20 minutes)

Here's how clarification works in practice.

### Step 1: Run /sp.clarify

In Claude Code, from your calculator-project directory:

```
/sp.clarify

My calculator specification is at specs/calculator/spec.md
Please analyze it for:
1. Ambiguous terms or vague language
2. Missing assumptions
3. Incomplete requirements
4. Edge cases not covered
5. Any conflicts with my Constitution

What gaps should I address before planning?
```

**What to expect**:
- AI analyzes your specification
- Lists 5-10 potential gaps or ambiguities
- Asks clarifying questions
- Organizes findings by category (ambiguous, missing, incomplete, etc.)

### Step 2: Review Feedback

Read through all gaps. For each gap, ask yourself:

- **Is this a real gap?** (Does it actually affect implementation?)
- **Is this within scope?** (Should my calculator handle this?)
- **Is this important?** (Will users/code care about this detail?)

**Example Evaluation**:

Gap: "What happens if someone tries calculator.log(2) (logarithm)?"
- Real gap? No—you explicitly said logarithm is out of scope
- Within scope? No—out of scope
- Important? No—specification clearly excludes advanced operations
**Action**: Ignore this gap; your spec is clear enough on scope

Gap: "You specify divide returns float, but what about integer division?"
- Real gap? Yes—this is ambiguous
- Within scope? Yes—division is in scope
- Important? Yes—implementers need to know which type of division
**Action**: Update spec to clarify: "Always float division, never integer division"

### Step 3: Refine Your Specification

For each real, in-scope, important gap:

1. **Update your spec.md** with clarification
2. **Add concrete examples** showing the clarified behavior
3. **Commit your changes** to git

Example update:

```markdown
## Before (Ambiguous)
### Division
- divide(10, 2) returns 5.0
- divide(10, 0) raises ValueError("Cannot divide by zero")

## After (Clarified)
### Division
- divide() always performs true float division (not integer division)
- divide(10, 2) returns 5.0
- divide(10, 3) returns 3.333... (not 3)
- divide(10, 0) raises ValueError("Cannot divide by zero")
- divide(10, 0.0001) returns 100000.0 (very small divisors allowed)
- Results accurate to Python float precision (~15-17 significant digits)
```

### Step 4: Re-Run /sp.clarify (Optional)

If you made significant changes, run `/sp.clarify` again:

```
I've updated my specification based on your feedback.
Please analyze it again for remaining gaps.
Should I proceed to planning, or are there more clarifications needed?
```

Most specifications need 1-2 clarification rounds. After that, they're ready for planning.

---

## Part C: Common Clarification Patterns (30 minutes)

Here are common gaps clarify typically finds in specifications. Learn to recognize and fix them.

### Pattern 1: Imprecise Error Handling

**Before (Unclear)**:
> "Invalid inputs raise an error"

**After (Clear)**:
> "Non-numeric inputs raise TypeError with message 'Expected numeric input, got {type}'.
> Examples: add('5', 3) raises TypeError('Expected numeric input, got <class str>')"

**Why Clearer**: Specifies which exception type, the message format, and includes examples implementers can verify against.

### Pattern 2: Missing Precision Definition

**Before (Ambiguous)**:
> "Results are accurate"

**After (Precise)**:
> "Results accurate to Python's float precision (approximately 15-17 significant digits).
> For 6+ decimal places: divide(10, 3) = 3.333333 (6 decimals shown),
> but internal precision is ~15 digits"

**Why Clearer**: Specifies what "accurate" means and clarifies float precision limits.

### Pattern 3: Incomplete Operation Specification

**Before (Incomplete)**:
> "Calculator supports add, subtract, multiply, divide, power"

**After (Complete)**:
> "Calculator supports:
> - add(x, y): x + y
> - subtract(x, y): x - y
> - multiply(x, y): x * y
> - divide(x, y): x / y (always float division)
> - power(x, y): x ^ y
>
> All operations accept int or float inputs and return float."

**Why Clearer**: Each operation documented with explicit math notation and common return behavior.

### Pattern 4: Ambiguous Edge Cases

**Before (Vague)**:
> "Power handles negative exponents and fractional exponents"

**After (Precise)**:
> "Power handles:
> - Positive exponents: power(2, 3) = 8.0
> - Negative exponents: power(2, -2) = 0.25
> - Zero exponent: power(5, 0) = 1.0
> - Fractional exponents (positive base only): power(4, 0.5) = 2.0
> - Negative base with integer exponent: power(-2, 3) = -8.0
> - Negative base with non-integer exponent: raises ValueError('Cannot take root of negative')"

**Why Clearer**: Each case is explicit with example and behavior. No ambiguity.

### Pattern 5: Scope Ambiguity

**Before (Unclear)**:
> "Calculator supports basic operations"

**After (Crystal Clear)**:
> "In Scope: add, subtract, multiply, divide, power (5 operations)
> Out of Scope: square root, logarithm, trigonometric, factorial, advanced operations
> Out of Scope: Web interface, CLI, graphical interface (Python library only)
> Out of Scope: Performance optimization, caching, parallelization"

**Why Clearer**: Explicitly lists what's in and out of scope, preventing scope creep.

---

## Part D: Clarify Your Calculator Specification (25 minutes)

Now let's clarify YOUR calculator specification.

### Step 1: Run /sp.clarify on Your Specification

In Claude Code, from your calculator-project directory, run:

```
/sp.clarify

My calculator specification is at specs/calculator/spec.md

Please analyze it for:
1. Ambiguous terms (words that could mean different things)
2. Missing assumptions (things I might have assumed but didn't state)
3. Incomplete requirements (operations or cases not fully specified)
4. Edge cases not covered
5. Conflicts with my project Constitution

List any gaps or questions. Which ones should I address before planning?
```

### Step 2: Document Feedback

Create a new file `CLARIFY_NOTES.md` to track feedback:

```markdown
# Clarification Notes for Calculator Specification

## Gaps Found by /sp.clarify

1. **Ambiguity**: [Description of gap]
   - Importance: [Critical / Important / Minor]
   - Action: [Will fix / Ignore / Out of scope]

2. **Missing Assumption**: [Description]
   - Importance: [Critical / Important / Minor]
   - Action: [Will fix / Ignore / Out of scope]

[Continue for each gap]

## Changes Made to Specification

- [Change 1]
- [Change 2]
- [Change 3]

## Remaining Gaps (Won't Fix)

- [Gap 1] - Reason: Out of scope
- [Gap 2] - Reason: Explicitly addressed in Constitution
```

### Step 3: Prioritize Gaps

Not all gaps are worth fixing. Prioritize:

**Critical** (fix before planning):
- Ambiguous operations or requirements
- Conflicts with Constitution
- Safety/security gaps

**Important** (fix but not blocking):
- Missing edge cases
- Incomplete precision definitions
- Scope clarifications

**Minor** (can ignore):
- Theoretical edge cases
- Out-of-scope suggestions
- Performance concerns (spec phase doesn't address performance)

### Step 4: Update Your Specification

For each critical or important gap:

1. **Edit `specs/calculator/spec.md`**
2. **Add clarifying detail or example**
3. **Commit to git**: `git add . && git commit -m "Clarify calculator spec: [description]"`

Example updates:

```diff
## Before
divide(10, 2) returns 5.0

## After
divide(x, y) performs float division (never integer division). Returns float.
Examples: divide(10, 2) = 5.0, divide(10, 3) = 3.333..., divide(10, 0) raises ValueError
```

### Step 5: Verify Readiness

Ask your AI companion:

```
I've clarified my specification based on your feedback.
Here are the changes I made:

[List your changes]

Is my specification now ready for the planning phase?
Or are there critical gaps I should address first?
```

---

## Cascade Quality Validation

Now test the cascade effect: Does your clarified specification improve planning potential?

**Ask yourself**:
- ✅ Can a developer read your spec and understand exactly what to build?
- ✅ Are all edge cases documented?
- ✅ Are error behaviors explicit (which exception, which message)?
- ✅ Is precision defined?
- ✅ Are operation interfaces clear?

If yes to all, your spec is ready for planning.

---

## Try With AI: Validate Clarification Progress

Use your AI companion to validate that your clarification has improved the specification.

### Setup

**Tool**: Claude Code (or your configured AI orchestrator)

**Context**: Your original specification + clarification changes

**Goal**: Confirm specification is clear, complete, and ready for planning

### Prompt Set (Copy-Paste Ready)

**Prompt 1 — Clarification Impact Assessment**

Copy and paste this into Claude Code:

```
I've clarified my calculator specification based on initial feedback.

Original issues found:
[List any 3-4 key gaps that were found]

Clarifications I made:
[List the changes you made to your spec]

Looking at my updated specification, have these clarifications improved it?
Can a developer now implement this calculator from my specification alone?
Any remaining critical gaps?
```

**Prompt 2 — Readiness Confirmation**

After assessment, ask:

```
Based on my clarified specification, am I ready to move to the planning phase?

Planning will generate:
- Architecture decisions (how to structure the code)
- Implementation phases (order to build operations)
- Component breakdown (CLI, library core, tests, docs)

Should I proceed, or are there more clarifications needed?
```

**Prompt 3 — Specification Quality Self-Assessment**

Finally, ask:

```
Let me self-assess my specification quality:

My specification now:
- ✅ Clearly defines 5 operations (add, subtract, multiply, divide, power)
- ✅ Specifies error handling for each operation
- ✅ Defines precision expectations (float, 6+ decimals)
- ✅ Covers edge cases (negative numbers, zero, large numbers)
- ✅ Respects project Constitution

Is this assessment accurate? What would you add?
```

### Expected Outcomes

After clarification and these prompts, you should:

✅ **Understand how specification gaps lead to planning confusion**
✅ **Know how to identify and fix ambiguities**
✅ **Have a clear, testable specification**
✅ **Be ready for planning (Lesson 5)**

### Safety & Ethics Note

**Clarification is Iteration, Not Perfection**:

Your specification will never be 100% perfect. There will always be edge cases you don't think of until implementation. That's normal and expected. Clarification should eliminate **critical ambiguities** and **major gaps**, not every possible edge case.

Aim for "clear enough that planning can happen," not "perfect." Perfection comes through the planning and implementation phases as you discover new details.

---

**You've completed Lesson 4**. Your calculator specification is now clarified, refined, and ready for the planning phase. In Lesson 5, you'll generate an implementation plan from your specification—and you'll see how clear specs produce clear plans.

Next: [Lesson 5: Plan Phase — Architecture Decisions and ADRs](./05-plan-phase.md)
