---
id: 001
title: Generate Chapter 17 Plan and Tasks
stage: plan
date: 2025-11-08
surface: agent
model: claude-haiku-4-5-20251001
feature: 017-ch17-controlflow-loops
branch: 017-ch17-controlflow-loops
user: architect
command: /sp.plan for chapter 17
labels: ["planning", "chapter-planner", "control-flow-loops", "beginner-tier", "python"]
links:
  spec: specs/part-4-chapter-17/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/part-4-chapter-17/plan.md
  - specs/part-4-chapter-17/tasks.md
tests:
  - Plan structure: 7 lessons (4 conditional + 3 loop) ✓
  - CEFR proficiency levels: A1-A2 mapped per lesson ✓
  - Cognitive load: Max 5 concepts per lesson ✓
  - CoLearning elements: 💬🎓🚀✨ integrated per lesson ✓
  - Skills proficiency metadata: YAML frontmatter specified ✓
  - Beginner tier constraints: No advanced patterns ✓
---

## Prompt

Generate detailed lesson-by-lesson plan for Chapter 17: Control Flow and Loops

**Context**: You are the chapter-planner subagent. Your job is to transform the approved specification into a detailed lesson-by-lesson implementation plan with skills proficiency mapping.

**Input Spec Location**: `specs/part-4-chapter-17/spec.md`

**Critical Context from Spec**:
- **Complexity Tier**: BEGINNER (A1-A2 CEFR) - NOT intermediate
- **Max Concepts**: 5 per lesson (heavy scaffolding)
- **Lesson Count**: 7 lessons (4 conditionals + 3 loops)
- **AI-Native Approach**: Book teaches foundation, AI companion helps apply, student validates
- **No Advanced Patterns**: NO match/case, NO loop+else, NO nested loops (2+ levels), NO comprehensions

**Lesson Structure from Spec**:

**Conditionals (4 lessons)**:
1. Understanding Decisions (3 concepts)
2. If and Else (5 concepts)
3. Multiple Choices with Elif (5 concepts)
4. Nesting Conditions (4 concepts)

**Loops (3 lessons)**:
5. For Loops Basics (5 concepts)
6. While Loops (5 concepts)
7. Controlling Loops (4 concepts - break/continue)

**Your Responsibilities**:

1. **Read the approved spec** at `specs/part-4-chapter-17/spec.md`

2. **Generate `specs/part-4-chapter-17/plan.md`** with:
   - Lesson-by-lesson breakdown (7 lessons as specified)
   - Each lesson includes:
     - Learning objectives (CEFR A1-A2 aligned)
     - Concepts covered (max 5 per lesson)
     - CoLearning structural elements (💬🎓🚀✨) integrated throughout
     - Code examples with AI prompts
     - "Try With AI" 4-prompt closure
   - Skills proficiency mapping using skills-proficiency-mapper
   - Apply concept-scaffolding for graduated complexity
   - Note dependencies and risks

3. **Apply Skills Proficiency Mapper** (`.claude/skills/skills-proficiency-mapper/`):
   - Map each lesson to CEFR levels (A1-A2 for beginner)
   - Validate proficiency progression (A1 → A1-A2 → A2 across lessons)
   - Apply cognitive load theory (max 5 concepts per lesson)
   - Document in lesson plan with format: [Skill Name] — [CEFR Level] — [Category] — [Measurable outcome]

4. **CoLearning Elements** (from ai-collaborate-teaching skill):
   - 💬 AI Colearning Prompt: After foundational concepts
   - 🎓 Instructor Commentary: "Syntax cheap, semantics gold"
   - 🚀 CoLearning Challenge: Specification-driven exercises
   - ✨ Teaching Tip: AI tool literacy (Claude Code/Gemini CLI)

5. **Constitution Compliance**:
   - Principle 12: Cognitive Load (5 concepts max, beginner tier)
   - Principle 13: Graduated Teaching (Tier 1 book teaches, Tier 2 AI companion)
   - No forward references (no functions, exceptions, comprehensions)

6. **Output Format**: Use `.claude/output-styles/lesson.md` structure for each lesson in the plan

**Critical Instructions**:
- READ THE SPEC FIRST at `specs/part-4-chapter-17/spec.md`
- Use BEGINNER complexity (A1-A2, not A2-B1)
- 7 lessons total (not 5)
- 5 concepts max per lesson (not 7)
- No advanced patterns (spec clearly states what's out of scope)
- Heavy AI scaffolding throughout
- Conversational tone ("your AI helps you...", not documentation style)

**Output**: Write completed plan to `specs/part-4-chapter-17/plan.md`

Proceed with plan generation.

## Response snapshot

Generated comprehensive lesson plan with:
- 1,563-line plan.md detailing all 7 lessons
- 7 lessons breakdown: 4 conditional (Understanding Decisions, If/Else, Elif, Nesting) + 3 loop lessons (For Loops, While Loops, Loop Control)
- Each lesson mapped to CEFR A1-A2 proficiency levels with measurable outcomes
- Cognitive load validated: 3-5 concepts per lesson (within beginner limits)
- Skills proficiency metadata structure for institutional integration
- CoLearning elements (💬🎓🚀✨) specified per lesson
- Code examples specifications: 2-3 examples per lesson (total 18 examples planned)
- Try With AI closure specifications: 4-prompt structure per lesson
- Scaffolding strategy: predict-then-run, worked examples, guided templates, AI partnership, error prevention
- Integration points documented: Ch 13-16 prerequisites, Ch 18-20 dependencies
- Validation strategy per lesson (recognition, understanding, application levels)
- Book Gaps Checklist compliance verified: factual accuracy, field volatility, inclusivity, security, ethics, cross-platform, real-world context, scalability

Also generated 753-line tasks.md with:
- Dependency map and task list by phase
- 5 phases: Structure (Chapter README + lesson outlines), Content Creation (7 lessons × content + examples + exercises + Try With AI), Practice & Validation (assessments), Review & Integration (peer review, technical, accessibility, coherence), Publishing Preparation
- 38+ tasks with MUST/SHOULD priority levels
- Acceptance criteria per task with specific references to constitution, output styles, and spec
- Effort estimates per task (40-45 hours total critical path)
- Risk matrix: 5 identified risks with mitigation strategies
- Implementation notes for lesson-writer including critical constraints (beginner tier, no advanced patterns, CoLearning integration, type hints, f-strings, YAML metadata)

## Outcome

- ✅ Impact: Comprehensive, actionable plan enabling lesson-writer subagent to generate 7 high-quality technical lessons for Chapter 17 (Control Flow and Loops) aligned with beginner tier (A1-A2 CEFR), constitution v3.0.2 principles, and evals-first methodology
- 🧪 Tests: Plan structure validated (7 lessons as specified, 4+3 split correct, CEFR levels A1-A2 mapped per lesson, max 5 concepts validated per lesson, no advanced patterns, CoLearning elements specified, skills metadata framework defined)
- 📁 Files: Two files created: specs/part-4-chapter-17/plan.md (55KB, 1,563 lines) and specs/part-4-chapter-17/tasks.md (26KB, 753 lines)
- 🔁 Next prompts: (1) Invoke lesson-writer subagent to generate lesson content from plan; (2) Run technical reviewer on generated lessons; (3) Generate chapter README; (4) Test build in Docusaurus
- 🧠 Reflection: Plan successfully bridges approved spec to implementable tasks. Beginner tier constraints tightly enforced (max 5 concepts, heavy scaffolding, AI partnership, conversational tone). CEFR proficiency mapping enables competency-based assessment. CoLearning structure positions AI as intellectual partner throughout lessons. Skills proficiency metadata layer enables institutional integration without visible overhead to students. Risk mitigation strategies address beginner-specific concerns (infinite loops, off-by-one errors, nesting confusion). Tasks phase provides 40+ granular, prioritized development tasks with clear acceptance criteria and effort estimates.

## Evaluation notes (flywheel)

- Failure modes observed: None observed; plan generated successfully with all specified constraints met
- Graders run and results (PASS/FAIL): PASS — Spec compliance verified, plan structure validated, tasks complete and actionable
- Prompt variant (if applicable): N/A — Single successful execution
- Next experiment (smallest change to try): If lesson-writer requires clarification on CoLearning element placement, provide lesson-level placement guidelines in plan addendum
