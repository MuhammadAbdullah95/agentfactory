---
description: Create complete Python chapter specification, plan, and tasks following AI-Driven Colearning methodology with automatic SpecKit Plus workflow orchestration.
---

# Python Chapter Complete Workflow (Spec → Plan → Tasks)

You are orchestrating the complete SpecKit Plus workflow for Python chapter creation (Chapters 12-29) following **AI-Driven Colearning** methodology.

---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

---

## Python Teaching Philosophy: AI-Driven Colearning

**CORE PRINCIPLE:** Students don't memorize syntax—they learn **concepts first**, then use AI co-teachers (Claude Code, Gemini CLI) to generate, explain, and refine code **with understanding**.

**The Shift:**
- Traditional: "Here's the syntax. Memorize it."
- AI-Driven: "Here's the concept. Explore it with your AI partner."

**Result:** Students think in **logic and reasoning**, not just code. They collaborate with AI as a **thinking partner**, not just a code generator.

---

## Teaching Pattern for EVERY Python Concept

```markdown
## 🔁 [Number]. [Concept Name] — [Simple Description]

**Concept:**
[Plain-language explanation in 2-3 sentences]
[Why it matters in AI-driven development]
[Real-world or AI agent analogy]

### 🧩 Python Example

\`\`\`python
# Minimal, clear code demonstrating concept
# Comments explain WHAT (not HOW - AI explains HOW)
\`\`\`

### 💬 AI Colearning Prompt

> "Ask your AI co-teacher: [Question that builds understanding]"

Then go deeper:

> "Follow up: [Question that extends concept or explores edge cases]"

Finally, connect to reasoning:

> "Real-world application: [Question linking concept to AI development]"

### 🎓 Instructor Commentary

> "[Meta-cognitive insight: why understanding beats memorization]"
> "[How this concept appears in AI agent development]"
```

**Example - Teaching Loops:**

```markdown
## 🔁 1. Loops — Repeating Until You're Done

**Concept:**
A loop repeats an action until a condition changes. Just like an AI agent iterates through tasks until a goal is achieved.

### 🧩 Python Example

\`\`\`python
# Repeat numbers 1 to 5
for i in range(1, 6):
    print(i)

# Repeat until condition becomes false
i = 1
while i <= 5:
    print(i)
    i += 1
\`\`\`

### 💬 AI Colearning Prompt

> "Ask Claude Code: Explain how the `for` loop works under the hood with `range()`.
> Then rewrite it using `while` and compare which is safer for beginners."

Then go deeper:

> "Simulate what happens if `i += 1` was forgotten. What error occurs?"

Finally, connect:

> "How do AI agents use loops? Show a real example of agent iteration."

### 🎓 Instructor Commentary

> "In AI-driven development, syntax is cheap — semantics is gold.
> Your goal isn't memorizing `for` vs `while` — it's understanding when
> repetition is the right reasoning pattern."
```

---

## Python Standards (Chapters 12-29)

### Version: Python 3.13+

**Modern features to teach:**
- f-strings (only string formatting method)
- match/case statements (Chapter 17+)
- Union types with `|` syntax: `int | str`
- Walrus operator `:=` (Chapter 17+)
- Modern type hints: `list[int]` not `List[int]`

**AVOID deprecated patterns:**
- ❌ `typing.List`, `typing.Dict` → Use `list`, `dict`
- ❌ `typing.Optional` → Use `X | None`
- ❌ `%` or `.format()` → Use f-strings only
- ❌ Old import style → Use modern syntax

### Type Hints Progression

| Chapter Range | Type Hint Policy |
|---------------|------------------|
| 13 (Intro) | NO type hints (too early) |
| 14 (Data Types) | Show in examples, don't require |
| 15-26 | Gradually increase, explain when used |
| 27+ (Pydantic) | Mandatory for all examples |

**Modern type hint syntax:**
```python
# GOOD (Python 3.10+)
def greet(name: str) -> str:
    return f"Hello, {name}"

items: list[int] = [1, 2, 3]
mapping: dict[str, int] = {"a": 1}
optional: str | None = None

# BAD (old style - don't teach)
from typing import List, Dict, Optional
items: List[int] = [1, 2, 3]
optional: Optional[str] = None
```

---

## Chapter Dependencies (Quick Reference)

| Chapters | Tier | CEFR | Prerequisites | Max Concepts/Section |
|----------|------|------|---------------|---------------------|
| 12-16 | Beginner | A1-A2 | 12→13→14→15→16 | 5 |
| 17-23 | Intermediate | A2-B1 | Need 14-16 | 7 |
| 24-29 | Advanced | B1-B2 | Need 20 & 14 | 10 |

**Key dependencies:**
- **12 (Python UV):** None (first chapter)
- **13 (Intro):** Needs 12
- **17 (Control Flow):** Needs 14-16
- **20 (Functions):** Needs 17-19
- **24 (OOP I):** Needs 20 & 14
- **28 (Asyncio):** Needs 20-21

---

## Security & Quality Standards

### NEVER teach:
- ❌ `eval()` or `exec()` on user input
- ❌ `shell=True` in subprocess
- ❌ Hardcoded secrets/passwords
- ❌ SQL string concatenation
- ❌ `pickle` for untrusted data

### ALWAYS teach:
- ✅ Environment variables for secrets
- ✅ Input validation
- ✅ f-strings (only string formatting)
- ✅ REPL-first validation
- ✅ Error handling (Chapter 21+)

---

## Workflow Execution

**IMPORTANT:** This command automatically invokes `/sp.specify`, `/sp.plan`, and `/sp.tasks` using the SlashCommand tool. You do NOT ask the user to run these commands - you execute them programmatically.

**Execution pattern:**
1. Phase 0: Gather context → Ask clarifying questions
2. Phase 1: Invoke `/sp.specify` → Guide evals & spec → Get approval
3. Phase 2: Invoke `/sp.plan` → Generate lesson plan → Get approval
4. Phase 3: Invoke `/sp.tasks` → Generate task checklist → Get approval
5. Report completion with file paths

---

### Phase 0: Context Gathering

**Input from user:** Chapter number (12-29) in `$ARGUMENTS`

**Extract chapter number:**
```bash
CHAPTER_NUM=$(echo "$ARGUMENTS" | grep -oE '\b(1[2-9]|2[0-9])\b' | head -1)

if [ -z "$CHAPTER_NUM" ]; then
  echo "ERROR: No valid chapter number (12-29) found"
  echo "Usage: /sp.python-chapter [chapter-number]"
  exit 1
fi
```

**Gather chapter context:**
1. Read `specs/book/chapter-index.md` for chapter title and topic
2. Determine complexity tier (12-16: Beginner, 17-23: Intermediate, 24-29: Advanced)
3. Determine CEFR range (A1-A2, A2-B1, B1-B2)
4. Check prerequisites from dependency map
5. Set cognitive load limit (5/7/10 concepts)

**Generate feature name:**
```bash
FEATURE_NAME="part-5-chapter-${CHAPTER_NUM}"
```

**Ask user clarifying questions:**
> "**Chapter ${CHAPTER_NUM}: [Title from chapter-index]**
>
> Questions to tailor content:
>
> 1. **Existing materials?** Do you have a colab notebook, example lesson, or reference content to incorporate? If yes, provide content.
> 2. **Specific concepts?** Any Python concepts or examples to prioritize?
> 3. **Real-world scenarios?** Emphasize specific AI development use cases?
> 4. **Target audience?** Aspiring developer (beginner), professional, or founder?
> 5. **AI colearning intensity?** Default is heavy AI colearning prompts. Adjust?"

**Wait for user response.**

**If user provides existing content (colab notebook, lesson):**

1. **Analyze content:**
   - Extract core concepts taught
   - Identify examples and code patterns
   - Note pedagogical flow and structure
   - Understand user's teaching voice

2. **Transform to AI-Driven pattern:**
   - Keep user's concepts and examples
   - Restructure using: Concept → Example → AI Colearning Prompt → Commentary
   - Add 💬 AI Colearning Prompts at 3 levels (understand, extend, apply)
   - Add 🎓 Instructor Commentary connecting to AI development
   - Preserve user's pedagogical intent

3. **Enhance with standards:**
   - Apply Python 3.13+ syntax to code examples
   - Add security checks (no eval, shell=True, secrets)
   - Ensure REPL-first validation
   - Apply cognitive load limits (5/7/10 concepts)

**Example transformation:**

**User provides:**
```
## Variables
A variable stores a value.
x = 5
```

**Transform to:**
```markdown
## 🧩 1. Variables — Naming Your Data

**Concept:**
A variable is a labeled container storing a value in memory.
Like AI agents store context, variables let programs remember information.

### 🧩 Python Example

\`\`\`python
x = 5
name = "Ali"
is_student = True
\`\`\`

### 💬 AI Colearning Prompt

> "Ask Claude: Explain what happens in memory when Python executes `x = 5`.
> Where is 5 stored, and what does x point to?"

Then explore:

> "What happens if I assign x = 10 after x = 5? Does 5 disappear?"

Finally, connect:

> "How do AI agents use variables? Show how an agent stores conversation history."

### 🎓 Instructor Commentary

> "Variables aren't just storage—they're how agents maintain state.
> Every chatbot, every reasoning chain uses variables to remember context."
```

---

### Phase 1: Specification (Evals → Spec)

**Objective:** Create comprehensive chapter specification with evals-first approach

**Action:** Invoke `/sp.specify ${FEATURE_NAME}` programmatically

```
Use SlashCommand tool to execute:
/sp.specify part-5-chapter-${CHAPTER_NUM}
```

**During specification, apply:**

#### Evals Definition (FIRST)

**Guide user to define business-goal-aligned success criteria:**

**Comprehension Evals:**
> "How will we know students understand this Python concept?"

Examples:
- "75%+ can explain [concept] in their own words" (quiz)
- "80%+ identify correct vs incorrect code" (multiple choice)
- "Reading level: Grade 6-8" (Flesch-Kincaid)

**Skill Acquisition Evals:**
> "What should students be able to DO after this chapter?"

Examples:
- "70%+ write working code using [concept]" (exercise)
- "65%+ debug broken code" (debugging task)
- "60%+ apply to new problem" (transfer test)

**Engagement Evals:**
> "What indicates students are engaged?"

Examples:
- "80%+ complete chapter" (completion rate)
- "70%+ submit exercises" (submission rate)

**Document in spec.md under "## Success Evals" (FIRST section after frontmatter)**

#### Specification Creation

**After evals defined**, create `specs/part-5-chapter-${CHAPTER_NUM}/spec.md`

**Apply standards:**

**Python Language Standards:**
- Python 3.13+ syntax only
- Modern type hints: `list[int]` not `List[int]`
- f-strings only (no `%` or `.format()`)
- match/case for Chapter 17+
- Union types with `|`: `int | str`
- Type hint progression (13: none, 14+: gradual, 27+: mandatory)

**AI-Driven Colearning Patterns:**
- **5-part structure for every concept:**
  1. 🧠 Concept (plain language + AI analogy)
  2. 🧩 Python Example (minimal, REPL-executable)
  3. 💬 AI Colearning Prompts (3 levels: understand, extend, apply)
  4. 🔍 Extension Prompts (build reasoning)
  5. 🎓 Instructor Commentary (connects to AI development)

- **REPL-First Learning:**
  - Every example must run in Python REPL
  - Show: Spec → AI Prompt → Generated Code → REPL Validation

- **AI as Co-Reasoning Partner:**
  - Students ask "why" and "how", not just "what"
  - Build error intuition through AI-guided exploration
  - Not just code generator—thinking partner

**Code Quality:**
- No security anti-patterns (eval, shell=True, secrets)
- Error handling (Chapter 21+)
- Testing with assertions
- Modern patterns only

**Pedagogical Principles:**
- Cognitive load limits:
  - Beginner (12-16): Max 5 concepts per section
  - Intermediate (17-23): Max 7 concepts per section
  - Advanced (24-29): Max 10 concepts per section
- Concept-first (not syntax-first)
- Real-world AI development connections
- Build reasoning, not memorization

**Specification structure:**
```yaml
---
chapter: [N]
title: "[Title from chapter-index]"
part: 5
complexity: [beginner|intermediate|advanced]
cefr_range: "[A1-A2|A2-B1|B1-B2]"
prerequisites:
  - chapter: [N]
    title: "[Title]"
python_version: "3.13+"
estimated_duration: "[hours]"
---

## Success Evals (Business-Goal-Aligned)

### Comprehension Evals
[Measurable understanding criteria]

### Skill Acquisition Evals
[Measurable skill criteria]

### Engagement Evals
[Completion metrics]

## Topic Summary
[1-2 paragraphs explaining chapter focus and AI-driven approach]

## Prerequisites
[Required chapters and skills]

## Learning Objectives (Aligned with Evals)
[3-5 measurable objectives]

## Content Outline

### Lesson 1: [Core Concept Title]
**Teaching Structure:** Concept-First AI Colearning
- 🧠 Concept explanations (2-3 core concepts)
- 🧩 Python examples with REPL demonstrations
- 💬 AI colearning prompts (ask, deeper, real-world)
- 🎓 Instructor commentary (connects to AI development)

### Lesson 2: [Applied Concept Title]
**Teaching Structure:** Hands-on with AI Co-Teacher
- Build on Lesson 1 concepts
- Real-world examples and use cases
- Extended AI colearning challenges
- Error exploration with AI

### Lesson 3: [Advanced/Combined Concepts]
**Teaching Structure:** Integration and Synthesis
- Combine multiple concepts
- Complex examples showing interplay
- System-thinking AI prompts
- Syntax to semantics discussions

### Lesson 4: Common Mistakes and AI-Guided Debugging
**Teaching Structure:** Error Literacy
- Typical errors students encounter
- AI-guided debugging prompts
- Build error intuition and prevention

### Lesson 5: Colearning Challenge - Build With Your AI
**Teaching Structure:** Capstone with AI Orchestration
- Real-world project using all concepts
- Student directs, AI implements, student validates
- Reflection prompts on learning

## Code Examples Specification
[3-8 examples with:
 - Pedagogical purpose
 - AI prompt template (how student asks AI)
 - Validation criteria (REPL test)
 - Connection to AI development]

## Acceptance Criteria (References Evals)
- [ ] All examples Python 3.13+ with modern syntax
- [ ] Every concept has AI colearning prompts (3 levels)
- [ ] Instructor commentary connects to AI development
- [ ] REPL-first validation demonstrated
- [ ] Cognitive load limits respected (5/7/10)
- [ ] Security standards met (no eval, shell=True, secrets)
- [ ] Type hints follow progression (13: none, 27+: mandatory)
- [ ] Learning objectives align with evals

## Dependencies
[Reads from / Writes to]

## Risks and Open Questions
```

**✋ Checkpoint:** User reviews and approves specification before proceeding.

---

### Phase 2: Planning (Lesson Structure)

**Objective:** Generate detailed lesson-by-lesson plan with skills proficiency mapping

**Action:** Invoke `/sp.plan` programmatically (after spec approved)

```
Use SlashCommand tool to execute:
/sp.plan
```

**During planning, chapter-planner subagent will:**

1. Read approved specification
2. Apply AI-Driven Colearning patterns
3. Invoke skills-proficiency-mapper (CEFR, Bloom's, DigComp)
4. Break spec into lesson structure with:
   - Lesson-by-lesson breakdown (4-6 lessons)
   - Skills metadata (CEFR levels, cognitive levels)
   - AI colearning prompt specifications
   - Code example details
   - Cognitive load validation
   - Progressive complexity

**Plan output includes:**
- Detailed lesson plans with AI colearning components
- Skills taught per lesson (CEFR proficiency levels)
- Learning objectives mapped to lessons
- Code example specifications with AI prompts
- Dependencies and sequencing
- Risk analysis

**Python-specific planning:**
- REPL examples in every lesson
- Type hint progression enforced
- Async only from Chapter 28+
- Security patterns for chapter level
- Modern Python 3.13+ features

**✋ Checkpoint:** User reviews plan before proceeding to tasks.

---

### Phase 3: Tasks (Work Decomposition)

**Objective:** Decompose plan into actionable, dependency-ordered task checklist

**Action:** Invoke `/sp.tasks` programmatically (after plan approved)

```
Use SlashCommand tool to execute:
/sp.tasks
```

**During task generation:**

1. Read plan and spec
2. Extract lessons and concepts
3. Generate task checklist:
   - Setup tasks (directory, frontmatter, structure)
   - Lesson implementation (one phase per lesson)
   - Code examples (with AI prompt templates)
   - AI colearning prompt validation
   - REPL validation tasks
   - Technical review and validation

**Task format (SpecKit standard):**
```
- [ ] [T001] Create chapter directory at book-source/docs/04-Python-The-Language-of-AI-Agents/${CHAPTER_NUM}-[name]/
- [ ] [T002] [US1] Implement Lesson 1: [Title] with Concept → Example → AI Prompt → Commentary structure
- [ ] [T003] [US1] Create AI colearning prompts for [concept] (3 levels: understand, extend, apply)
- [ ] [T004] [US1] Add instructor commentary connecting [concept] to AI development
- [ ] [T005] [US2] Implement Lesson 2 with hands-on AI co-teaching examples
- [ ] [T006] Validate all code examples run in Python 3.13 REPL
- [ ] [T007] Verify AI colearning prompts are effective (test with Claude/Gemini)
- [ ] [T008] Run technical-reviewer validation
```

**Tasks organized by:**
- Phase 1: Setup
- Phase 2: Foundational (README, overview)
- Phase 3+: One phase per lesson (in sequence)
- Final Phase: Validation and polish

**Each lesson task includes:**
- AI-Driven Colearning structure (5 parts)
- REPL validation requirements
- Python 3.13+ standards checklist
- Security validation
- Type hint compliance check

**✋ Checkpoint:** User reviews tasks before implementation.

---

## Workflow Summary

**User types once:**
```
/sp.python-chapter 12
```

**Command automatically executes:**
```
Phase 0: Context Gathering
→ Extract chapter number: 12
→ Read chapter-index.md (Chapter 12: Python UV)
→ Identify: Beginner tier, A1 CEFR, no prerequisites
→ Ask clarifying questions → User responds
→ Transform user content if provided

Phase 1: Specification (Automatic)
→ Invoke /sp.specify part-5-chapter-12 (SlashCommand tool)
→ Guide evals definition (comprehension, skills, engagement)
→ Create spec with AI-Driven Colearning structure
→ Apply Python 3.13+ standards, security, cognitive load limits
→ ✋ User approves spec

Phase 2: Planning (Automatic)
→ Invoke /sp.plan (SlashCommand tool)
→ chapter-planner generates lesson-by-lesson plan
→ Add skills metadata (CEFR, Bloom's, DigComp)
→ Apply AI colearning pattern specifications
→ Validate progressive complexity
→ ✋ User approves plan

Phase 3: Tasks (Automatic)
→ Invoke /sp.tasks (SlashCommand tool)
→ Decompose into atomic work units
→ Generate dependency-ordered checklist
→ Include AI colearning validation tasks
→ ✋ User approves tasks

✅ Report completion: 3 files ready
→ specs/part-5-chapter-12/spec.md
→ specs/part-5-chapter-12/plan.md
→ specs/part-5-chapter-12/tasks.md

✅ Ready for implementation (lesson-writer subagent)
```

**Key point:** All three SpecKit commands are invoked automatically. User only runs `/sp.python-chapter [N]` once.

---

## Output Files Created

```
specs/part-5-chapter-${CHAPTER_NUM}/
  spec.md    (Specification with evals, AI colearning structure)
  plan.md    (Lesson plan with skills metadata, AI prompt specs)
  tasks.md   (Task checklist with validation requirements)
```

---

## Success Criteria

Workflow complete when:

- [ ] **Specification:**
  - Evals defined first with business-goal connection
  - Every concept has 5-part AI colearning structure
  - Python 3.13+ standards applied
  - Cognitive load limits respected (5/7/10)
  - Security requirements met

- [ ] **Plan:**
  - 4-6 lessons with AI colearning components
  - Skills metadata (CEFR, Bloom's, DigComp)
  - Code examples with AI prompts specified
  - Progressive complexity validated

- [ ] **Tasks:**
  - Atomic work units (1-2 hours each)
  - Dependency-ordered
  - AI colearning validation included
  - REPL validation tasks specified

- [ ] **User approved all three phases**

---

## Next Steps After Completion

**Tell user:**

> "✅ Python Chapter ${CHAPTER_NUM} specification, plan, and tasks complete!
>
> **Files created:**
> - `specs/part-5-chapter-${CHAPTER_NUM}/spec.md` (Spec with AI colearning)
> - `specs/part-5-chapter-${CHAPTER_NUM}/plan.md` (Lesson plan with prompts)
> - `specs/part-5-chapter-${CHAPTER_NUM}/tasks.md` (Task checklist)
>
> **Next steps:**
> 1. Review all three files
> 2. Ready to implement? Invoke lesson-writer subagent with plan context
> 3. After lessons complete, run technical-reviewer for validation
>
> **Reminder:** All content follows AI-Driven Colearning pattern—students learn concepts first, explore with AI partners."

---

## Important Notes

**This command orchestrates complete workflow** (Spec → Plan → Tasks).

**CRITICAL: Automatic command execution**
- Automatically invokes `/sp.specify`, `/sp.plan`, `/sp.tasks` using SlashCommand tool
- You do NOT tell user to run these commands
- You execute them programmatically
- User types `/sp.python-chapter [N]` once—everything else automatic

**SpecKit commands executed sequentially:**
1. `/sp.specify part-5-chapter-${N}` (automatic)
2. `/sp.plan` (automatic)
3. `/sp.tasks` (automatic)

**AI-Driven Colearning enforced:**
- Every concept: Concept → Example → AI Prompt → Commentary
- Students learn reasoning, not syntax
- AI positioned as thinking partner
- Build understanding through exploration

**Human checkpoints:**
- User provides context and preferences
- User approves evals
- User approves spec
- User approves plan
- User approves tasks

**Quality gates automatic:**
- Python 3.13+ standards
- Security requirements
- Cognitive load limits
- CEFR proficiency mapping
- Type hint progression
- AI colearning structure

---

## Usage Examples

```bash
# Create Chapter 12 (Python UV) - Beginner
/sp.python-chapter 12

# Create Chapter 17 (Control Flow) - Intermediate with match/case
/sp.python-chapter 17

# Create Chapter 28 (Asyncio) - Advanced with async patterns
/sp.python-chapter 28
```

---

## Error Handling

**Invalid chapter number:**
```
ERROR: Chapter number must be 12-29 (Part 5: Python)
Usage: /sp.python-chapter [12-29]
```

**Missing prerequisites:**
```
WARNING: Chapter ${N} requires Chapter ${PREREQ} to be complete.
Check specs/book/chapter-index.md for status.
Continue anyway? (y/n)
```

---

## Design Philosophy

**Why orchestrate complete workflow?**
- Reduces cognitive load (one command vs three)
- Ensures consistency (same standards throughout)
- Enforces checkpoints (user approval at strategic points)
- Applies AI-Driven Colearning (systematic, not ad-hoc)
- Faster iteration (complete workflow in one session)

**Why human checkpoints?**
- Evals require business context (AI doesn't know goals)
- Specifications need pedagogical decisions
- Content requires human judgment (technical + pedagogical)
- Quality requires validation, not just generation

**Why AI-Driven Colearning?**
- Syntax memorization is obsolete in AI era
- Reasoning and logic are portable skills
- AI partnership is professional reality
- Understanding beats memorization for retention
