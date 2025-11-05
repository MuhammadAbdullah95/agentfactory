---
title: "Capstone Integration — Complete Workflow End-to-End"
chapter: 31
lesson: 8
duration_minutes: 210

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Complete Spec-Kit Plus Workflow (End-to-End)"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can execute complete workflow (constitution → spec → clarify → plan → tasks → implement) independently"

  - name: "Independent Specification Writing"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can write complete specification without template guidance for new project"

  - name: "Architectural Decision Making"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify and document 3-5 architecturally significant decisions"

  - name: "Vertical Intelligence Collaboration"
    proficiency_level: "B2"
    category: "Soft"
    bloom_level: "Apply"
    digcomp_area: "Communication & Collaboration"
    measurable_at_this_level: "Student collaborates with AI orchestrator and specialized subagents throughout workflow"

  - name: "Reflecting on Cascade Effect"
    proficiency_level: "B2"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student articulates how specification quality determined plan/task/code quality"

learning_objectives:
  - objective: "Complete full Spec-Kit Plus workflow independently on new project (temperature or unit converter)"
    proficiency_level: "B2"
    bloom_level: "Create"
    assessment_method: "Completed workflow artifacts (spec, plan, tasks, code, tests, ADRs, PHRs)"

  - objective: "Apply cascade principle: demonstrate how spec quality determined implementation quality"
    proficiency_level: "B2"
    bloom_level: "Evaluate"
    assessment_method: "Reflection document analyzing cascade effect"

  - objective: "Make and document architectural decisions appropriately"
    proficiency_level: "B2"
    bloom_level: "Evaluate"
    assessment_method: "3-5 ADRs documenting significant decisions"

  - objective: "Identify when Vertical Intelligence (orchestrator + subagents) helps vs when human thinking matters"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Project reflection on human vs AI roles"

cognitive_load:
  new_concepts: 0
  assessment: "Capstone applies all concepts from Lessons 1-7. No new concepts; focus on synthesis and independent application. ✓"

differentiation:
  extension_for_advanced: "Choose complex project (unit converter with multiple dimensions); document 5-8 ADRs; present reflection as formatted document"
  remedial_for_struggling: "Choose simple project (temperature converter); focus on core workflow; optional advanced features"

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/10-chapter-31-redesign/spec.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "manual-implementation"
version: "1.0.0"
---

# Lesson 8: Capstone Integration — Complete Workflow End-to-End

This is the capstone: **Apply everything you've learned in Lessons 1-7 to a new project, independently.**

You've practiced each phase separately (constitution, specification, clarification, planning, tasks, implementation). Now you'll execute the complete workflow without step-by-step guidance.

**Time**: 3-4 hours for a simple project, 5-6 hours for a complex project

**Projects**: Choose one:
- **Simple**: Temperature Converter (Celsius ↔ Fahrenheit ↔ Kelvin)
- **Complex**: Unit Converter System (length, weight, temperature with extensible architecture)

---

## Part A: Project Overview (10 minutes)

### Option 1: Temperature Converter (Simple)

**What**: Convert between Celsius, Fahrenheit, and Kelvin

**Operations**:
- celsius_to_fahrenheit(c) → f
- fahrenheit_to_celsius(f) → c
- celsius_to_kelvin(c) → k
- kelvin_to_celsius(k) → c
- fahrenheit_to_kelvin(f) → k
- kelvin_to_fahrenheit(k) → f

**Edge Cases**:
- Absolute zero (-273.15°C, 0K)
- Precision handling for scientific values
- Invalid input types and ranges

**Complexity**: ~6 hours for complete workflow

**This is Good For**: Learning without overwhelming complexity

### Option 2: Unit Converter System (Complex)

**What**: Extensible system converting length, weight, temperature

**Components**:
- Core converter engine (handles arbitrary unit conversions)
- Length conversions (mm, cm, m, km, inches, feet, miles, etc.)
- Weight conversions (g, kg, lb, oz, etc.)
- Temperature conversions (same as Option 1)
- Extensibility (easy to add new dimensions)

**Architecture Decision**: How to structure for extensibility?
- All conversions to base unit then to target?
- Unit registry system?
- Conversion factor matrices?

**Complexity**: ~8 hours for complete workflow

**This is Good For**: Learning architectural thinking and complex decisions

---

## Part B: Choose Your Project (5 minutes)

**Quick Assessment**:

Choose **Simple (Temperature Converter)** if:
- ✅ This is your first time with Spec-Kit Plus
- ✅ You want to focus on workflow mastery
- ✅ You have 3-4 hours available
- ✅ You prefer confidence over complexity

Choose **Complex (Unit Converter)** if:
- ✅ You want to push yourself architecturally
- ✅ You have 5-6 hours available
- ✅ You want to practice complex design decisions
- ✅ You want extension topics (generalized architecture)

**Recommended**: Start with **Simple**. You can always build Complex afterward.

---

## Part C: The Complete Workflow (Apply all lessons)

Here's the full workflow you'll execute independently:

### Phase 1: Constitution (Lesson 2 skills) — 15 minutes

**Note**: You already have a project Constitution from Lesson 2. You can:
- **Reuse** the calculator Constitution (fine if it applies to your new project), OR
- **Create a new Constitution** for this project (better practice)

**For Temperature/Unit Converter**:

```markdown
# Temperature/Unit Converter Constitution

## Code Quality Standards
[Define standards: type hints, docstrings, PEP 8, line length, etc.]

## Error Handling
[Define: ValueError for invalid values, TypeError for invalid input, etc.]

## Type System
[Kelvin must be >= 0, negative temperatures may be invalid, precision expectations]

## Testing
[100% coverage, unit tests per conversion, edge cases, etc.]
```

**Commit**: `git add .specify/memory/constitution.md && git commit -m "Initialize converter project constitution"`

### Phase 2: Evals-First Conversation (Lesson 3 skills) — 15 minutes

Have an informal chat with your AI companion:

```
I want to build a [temperature converter / unit converter].

Before I write a formal spec, let me clarify success:
1. What conversions should I support?
2. What edge cases matter?
3. What's "correct" for precision?
4. What input/output interface?
5. What should happen with invalid input?

[Have the conversation]
```

Document key points from this evals conversation—they'll inform your spec.

### Phase 3: Specification (Lesson 3 skills) — 45 minutes

Write a complete specification (similar to calculator lesson 3):

```markdown
# Temperature Converter Specification

## Overview
[What you're building and why]

## Scope
[In Scope / Out of Scope]

## User Stories
[5-6 stories]

## Acceptance Criteria
[SMART criteria for each conversion]

## Edge Cases
[Absolute zero, negative temperatures, precision limits]

## Constraints
[Constitution requirements]
```

**Commit**: `git add specs/converter/spec.md && git commit -m "Write temperature converter specification"`

### Phase 4: Clarification (Lesson 4 skills) — 20 minutes

Run `/sp.clarify` on your specification:

```
/sp.clarify

My specification is at specs/converter/spec.md

Please analyze for:
1. Ambiguous terms
2. Missing assumptions
3. Incomplete requirements
4. Edge cases not covered
5. Conflicts with Constitution
```

Review feedback, update spec based on critical gaps, commit changes.

### Phase 5: Planning (Lesson 5 skills) — 30 minutes

Run `/sp.plan`:

```
/sp.plan

My specification is at specs/converter/spec.md

Please generate implementation plan with:
1. Architecture overview
2. Implementation phases
3. Component breakdown
4. Dependencies
5. Design decisions highlighted
```

Identify 3-5 architecturally significant decisions and create ADRs:

```bash
# Create ADRs for key decisions (error handling, architecture, precision, etc.)
touch history/adr/001-error-handling-strategy.md
touch history/adr/002-architecture-choice.md
touch history/adr/003-precision-strategy.md
```

**Commit**: `git add specs/converter/plan.md history/adr/ && git commit -m "Plan converter architecture and document decisions"`

### Phase 6: Tasks (Lesson 6 skills) — 20 minutes

Run `/sp.tasks`:

```
/sp.tasks

My plan is at specs/converter/plan.md

Please decompose into atomic work units:
1. Size each at 1-2 hours
2. Define single acceptance criterion
3. Show dependencies
4. Create dependency graph
```

**Commit**: `git add specs/converter/tasks.md && git commit -m "Decompose plan into atomic tasks"`

### Phase 7: Implementation (Lesson 7 skills) — 90-120 minutes

Run `/sp.implement` (in phases, using checkpoint pattern):

**Phase 1** (Core Conversions - 30 minutes):

```
/sp.implement

Tasks 1-3 from specs/converter/tasks.md

Implement core temperature conversions with full type hints and docstrings.
Generate comprehensive tests.

Ready for my review.
```

Review → Test → Approve → **Commit**

**Phase 2** (Additional Conversions or Error Handling - 30 minutes):

```
/sp.implement

Tasks 4-6 (next phase from tasks.md)

Continue implementation...
Ready for my review.
```

Review → Test → Approve → **Commit**

**Phase 3** (Testing & Documentation - 30 minutes):

```
/sp.implement

Tasks 7+ (final phase: comprehensive tests, documentation, edge cases)
```

Review → Test → Approve → **Commit**

### Phase 8: Reflection & Validation (10-15 minutes)

Create a **Reflection Document**:

```markdown
# Converter Project Reflection

## Workflow Execution
- Started: [date/time]
- Completed: [date/time]
- Total time: [hours]

## Specification Quality vs Implementation Quality

### Spec Strengths (enabled good implementation)
- [What was clear in the spec?]
- [What made planning straightforward?]

### Spec Gaps (caused implementation issues)
- [What was ambiguous?]
- [What emerged during planning/implementation?]

## Cascade Effect Observed

Clear Spec → Clear Plan → Clear Tasks → Working Code
[Describe how this played out in your project]

## Architectural Decisions

I documented these key decisions:
- ADR-001: [Decision]
- ADR-002: [Decision]
- ADR-003: [Decision]

Why these decisions mattered: [Explanation]

## Vertical Intelligence Observation

Where did I control the workflow? [Specification intent, validation, approval]
Where did AI orchestrator handle complexity? [Code generation, plan decomposition]
Where did specialized subagents execute? [Spec writing, planning, implementation]

## What Would I Do Differently?

If I redid this project:
- [Learning 1]
- [Learning 2]
- [Learning 3]

## Skills Mastered

By completing this capstone, I've demonstrated:
- ✅ [Skill 1]
- ✅ [Skill 2]
- ✅ [Skill 3]

## Next Steps

For production readiness, this project would need:
- [Deployment considerations]
- [Performance optimization]
- [Additional features]

But for learning Spec-Kit Plus workflow: **COMPLETE**
```

**Commit**: `git add REFLECTION.md && git commit -m "Capstone reflection: converter workflow complete"`

---

## Part D: Validation Checklist (20 minutes)

Before declaring capstone complete, verify:

### Workflow Artifacts

**Constitution**:
- [ ] Constitution exists (reused or new)
- [ ] Constitutional standards are clear
- [ ] Committed to git

**Specification**:
- [ ] Complete spec with all sections (overview, scope, user stories, criteria, constraints)
- [ ] SMART acceptance criteria
- [ ] Edge cases documented
- [ ] Committed to git

**Clarification**:
- [ ] `/sp.clarify` run and feedback addressed
- [ ] Spec updated based on clarification
- [ ] Committed to git

**Plan**:
- [ ] Implementation plan generated
- [ ] 3-5 ADRs documenting key decisions
- [ ] Plan structure clear (phases, dependencies, milestones)
- [ ] Committed to git

**Tasks**:
- [ ] Tasks generated (6-10 atomic units)
- [ ] Dependencies clear
- [ ] Committed to git

**Implementation**:
- [ ] Code implements all spec requirements
- [ ] All tests pass, 100% coverage
- [ ] Type hints on all functions
- [ ] Docstrings on all functions
- [ ] Checkpoint pattern used (review → approve → commit)
- [ ] Committed to git

**PHRs**:
- [ ] Auto-created PHRs in history/prompts/converter/
- [ ] At least 5 PHRs captured (spec → clarify → plan → tasks → implement)
- [ ] You understand what each PHR captures

**Reflection**:
- [ ] Reflection document written
- [ ] Cascade effect explained
- [ ] Architectural decisions documented
- [ ] Learnings captured
- [ ] Committed to git

### Code Quality

**Specification Matching**:
- [ ] All operations implemented
- [ ] All acceptance criteria pass
- [ ] All edge cases handled
- [ ] Error handling matches strategy

**Standards**:
- [ ] Type hints on all functions
- [ ] Docstrings on all functions
- [ ] PEP 8 compliance
- [ ] No hardcoded test data

**Testing**:
- [ ] 100% code coverage
- [ ] All tests passing
- [ ] Edge case tests included
- [ ] Error condition tests included

### Git History

```bash
# Your git log should show:
git log --oneline

# Something like:
abcd1234 Capstone reflection: converter workflow complete
xyz9876a Phase 3: Complete tests and documentation
...
1234567a Initialize converter project constitution
```

---

## Part E: Optional Extensions (If Time Permits)

If you want to push further:

### Extension 1: Multi-Project Comparison

Complete BOTH simple and complex projects:
- **Simple**: Temperature Converter (done)
- **Complex**: Unit Converter System

Compare:
- Spec complexity: How different are the specs?
- Plan complexity: How do architectures differ?
- Implementation difficulty: What made complex harder?

### Extension 2: Performance Optimization

Add a new phase after implementation:

```
/sp.implement

Phase: Optimization

Tasks:
- Profile current implementation (identify slow operations)
- Optimize based on profiling (not guessing)
- Verify optimizations don't break acceptance criteria

Generate performance benchmarks showing before/after.
```

### Extension 3: Architectural Refactoring

If you built Temperature Converter, refactor toward Unit Converter architecture:

- How would you generalize the code?
- What would break if you tried to add length conversions?
- Design the extensibility you wish you had

Create ADR: "ADR-004: Path to Unit Converter Extensibility"

---

## Try With AI: Capstone Validation and Celebration

Use your AI companion for final validation and reflection.

### Setup

**Tool**: Claude Code (or your configured AI orchestrator)

**Context**: Your complete project artifacts

**Goal**: Validate workflow completion and reflect on learning

### Prompt Set (Copy-Paste Ready)

**Prompt 1 — Workflow Completion Verification**

Copy and paste this into Claude Code:

```
I've completed the Spec-Kit Plus capstone project.

Here's what I built:
- Project: [Temperature Converter / Unit Converter]
- Time spent: [hours]
- Spec quality: [assessment]
- Implementation quality: [assessment]

Artifacts created:
- Specification: specs/converter/spec.md
- Plan: specs/converter/plan.md
- ADRs: [List your ADRs]
- Tasks: specs/converter/tasks.md
- Code: [Code location and stats]
- Tests: [Test location and coverage]
- Reflection: REFLECTION.md

Looking at my project, did I execute the workflow correctly?
Any phase that seems weak or incomplete?
```

**Prompt 2 — Cascade Effect Analysis**

After verification, ask:

```
Let me analyze the cascade effect in my project.

My specification was: [Quality level: very clear / fairly clear / somewhat vague]

My plan was: [Quality level: very detailed / fairly detailed / somewhat vague]

My tasks were: [Quality level: very atomic / fairly atomic / somewhat large]

My code was: [Quality level: very clean / fairly clean / somewhat messy]

Looking back, how did specification quality flow into all downstream quality?
What would have changed if my spec was vague?
```

**Prompt 3 — Capstone Celebration**

Finally, ask:

```
I've now completed:

✅ Lesson 1: Installation & Setup (configured environment)
✅ Lesson 2: Constitution Phase (project rules)
✅ Lesson 3: Specify Phase (learn evals-first thinking)
✅ Lesson 4: Clarify Phase (refine specifications)
✅ Lesson 5: Plan Phase (architecture + ADRs)
✅ Lesson 6: Tasks Phase (atomic decomposition)
✅ Lesson 7: Implement Phase (AI-driven code generation)
✅ Lesson 8: Capstone (end-to-end workflow)

What does this mean? What have I learned?
And what comes next? (Chapter 32 reference?)
```

### Expected Outcomes

✅ **Complete Spec-Kit Plus workflow mastered**
✅ **Cascade effect understood through practice**
✅ **Vertical Intelligence pattern internalized**
✅ **Ready for Chapter 32 (team parallelization patterns)**

### Safety & Ethics Note

**On Workflow Mastery**:

You've now practiced the complete Spec-Kit Plus workflow—twice. Once on calculator (guided), once on converter (independent). This is professional-level SDD practice.

The workflow doesn't change—specification, planning, tasking, implementation, validation. But your confidence and skill grow with repetition. Each project you complete teaches you more about spec quality, architectural decisions, and code validation.

The goal isn't perfection on this capstone. The goal is **understanding the workflow well enough that you could teach it to others**.

---

## Capstone Completion Celebration

**You have completed Chapter 31**.

Here's what you've accomplished:

### Skills Mastered
- ✅ **Specification-First Development** — Write clear specs that guide implementation
- ✅ **Evals-First Thinking** — Define success before building
- ✅ **SMART Criteria** — Translate vague intent into testable requirements
- ✅ **Specification Refinement** — Use `/sp.clarify` to find and fix gaps
- ✅ **Implementation Planning** — Generate architecture from specifications
- ✅ **Architectural Decision Making** — Document significant decisions in ADRs
- ✅ **Task Decomposition** — Break plans into atomic work units
- ✅ **AI-Driven Implementation** — Generate and validate code using Vertical Intelligence
- ✅ **Checkpoint Pattern** — Maintain human control throughout workflow
- ✅ **Code Validation** — Systematically verify AI-generated code
- ✅ **PHR Understanding** — Know where collaboration history is captured

### Workflow Mastery
You can now execute (and explain) the complete Spec-Kit Plus workflow:

```
Constitution (project rules)
  ↓
Evals-First Discussion (informal intent clarification)
  ↓
Specification (WHAT the system does)
  ↓
Clarification (resolve ambiguities)
  ↓
Plan (HOW to build it)
  ↓
ADRs (document significant decisions)
  ↓
Tasks (atomic work units)
  ↓
Implementation (AI-generated code + human validation)
  ↓
Validation (verify all acceptance criteria pass)
```

### What Comes Next: Chapter 32

Chapter 32 teaches **team parallelization patterns**. You now have:
- Single-project mastery (Calculator, Converter)
- Complete workflow understanding
- Ready to learn how teams parallelize multiple features

Chapter 32 will teach:
- How to run 3-5 features in parallel
- How teams coordinate specifications
- How to manage dependencies across features
- How orchestrators scale to multiple features

---

**Congratulations. You are now competent in Spec-Kit Plus and specification-first, AI-native development.**

This is just the beginning. Practice this workflow on your own projects. Each project teaches you more about writing clear specifications and working effectively with AI partners.

**Questions?** Refer back to the relevant lessons.

**Ready for more complexity?** Chapter 32 awaits.

**Want to go deeper?** Parts 6-13 build on these foundations to teach advanced topics (advanced Python, TypeScript, async patterns, databases, deployment).

Your journey in AI-native software development is well underway.

---

**End of Chapter 31: Spec-Kit Plus Hands-On**

Total chapter time: 13-15 hours (across 8 lessons)

Total projects: 2-3 (Calculator guided, Converter independent, optional extensions)

Workflow mastery: Complete ✅

Ready for Chapter 32: Yes ✅
