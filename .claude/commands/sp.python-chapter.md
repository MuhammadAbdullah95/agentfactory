---
description: Orchestrate full SpecKit Plus workflow for Python chapters (12-29). Automatically chains /sp.specify → /sp.plan → /sp.tasks with approval gates. Students learn Python through AIDD thinking (specification-first, validation-first, AI partnership).
---

# /sp.python-chapter: Orchestrated Python Chapter Workflow

**Purpose**: Design a complete Python chapter (12-29) using AIDD principles with **automatic orchestration** of the full SpecKit Plus workflow (Spec → Plan → Tasks → optional Implementation). Students learn programming by applying AIDD thinking learned in Chapters 1-11.

## User Input

```text
$ARGUMENTS
```

## VERTICAL INTELLIGENCE: AIDD-Driven Python Teaching

Before orchestration begins, understand what makes Python chapters effective in the AI-native era:

### Core Principle: Specification-First, Validation-First, AI Partnership

Students don't memorize Python syntax. Instead:

1. **Understand the concept** (plain language explanation)
2. **See minimal code** (what it does in action)
3. **Ask their AI** (explore through dialogue with Claude Code/Gemini CLI)
4. **Extract insight** (why this matters for thinking, not just coding)

### AI-Native Learning for Part 4 Students

**Traditional Programming Teaching**:
- "Memorize Python syntax"
- "Here are all 47 string methods"
- Syntax-first (memorize, then apply)

**AI-Native Learning Pattern** (Part 4: Chapters 12-29):
- **Describe Intent**: Use type hints and clear code to communicate what data means
- **Explore with AI**: Ask AI questions to understand concepts (not memorize docs)
- **Validate Together**: Use isinstance(), type(), and tests to check understanding
- **Learn from Errors**: When errors occur, ask AI "why?" and learn the pattern

**Note on AIDD**: Students in Chapters 1-11 learned AIDD principles (Specification → Generation → Execution → Reflection). Part 4 applies these principles to learning Python, using the beginner-friendly "AI-Native Learning" framing. Students don't write formal specifications yet (that's Part 5+), but they DO describe intent through type hints and clear code structure.

### Teaching Pattern (Every Concept)

```markdown
## 1. [Concept Name] — [Why it matters]

**What it is:**
Plain-language explanation (2-3 sentences).

### 💻 Code Idea

\`\`\`python
# Minimal code showing the concept
# Focus on WHAT it does
\`\`\`

### 🤖 Think With Your AI

> "What does this do?"
>
> "What changes if we...?"
>
> "How would you use this to...?"

### 🧠 The Reasoning Pattern

[Why this concept matters for thinking, not just coding]
```

**Example:**

```markdown
## 1. Variables — Storing Data

**What it is:**
A variable names a value so your program can remember it.

### 💻 Code Idea

\`\`\`python
name = "Alex"
score = 95
\`\`\`

### 🤖 Think With Your AI

> "Why do we need variables instead of just using 95?"
>
> "What breaks if we forget to name a value?"
>
> "How do AI agents use variables to track context?"

### 🧠 The Reasoning Pattern

Programs need memory. Variables let you say "remember this as X"—
exactly how reasoning chains in AI maintain state.
```

---

## Python Standards (Chapters 12-29)

**Version:** 3.14+ (always use latest stable release from https://www.python.org/downloads/)
**Syntax:** f-strings only, match/case (17+), modern types (`list[int]`, `X | None`)
**Type hints:** Core (Ch 13) → Gradual Application (14-26) → Mandatory (27+)
**Note on Type Hints:** Modern Python treats type hints as essential for clarity and specification-first thinking, not optional features. Integrate from Chapter 13 onwards.

**Security (non-negotiable):**
- ❌ No `eval()`, `shell=True`, hardcoded secrets
- ✅ Environment variables, input validation, modern patterns

---

## CRITICAL DESIGN RULES

### Rule 1: USER INTENT IS AUTHORITY

**Never override user input:**
- User says "beginner" → Make A1-A2 (NOT A2-B1)
- User says "just variables" → Only variables (NOT + functions + loops)
- User says "absolute beginners" → 5 concepts max, simple framing

**Always ask, always honor. Do NOT assume.**

---

### Rule 2: NO FORWARD REFERENCES + PART 4 APPROPRIATE LANGUAGE

**Never mention untaught concepts:**
- ❌ NO Chapter 30+ references
- ❌ NO "Specification-Driven Development" (not yet taught - that's Part 5+)
- ❌ NO "write a specification" (use "describe your intent" instead)
- ❌ NO professional SDD terminology for Part 4 students

**DO reference AI-Native Learning (appropriate for Part 4):**
- ✅ "Describe what your code should do using type hints..."
- ✅ "Ask your AI to explain this concept..."
- ✅ "Validate your understanding by testing the code..."
- ✅ "Learn from errors by asking AI 'why did this fail?'..."

**DO reference AIDD principles from Chapters 1-11 (context only):**
- ✅ "This applies the AIDD thinking you learned in Part 1..."
- ✅ "Remember the validation-first approach from Chapter 4..."
- ✅ "You're using AI as co-reasoning partner, not coding assistant..."

**Critical Distinction**:
- Part 4 students use **AI-Native Learning** (beginner-friendly: describe intent → explore → validate → learn from errors)
- Part 5+ students learn **Specification-Driven Development** (professional: write formal specs → generate → test → iterate)
- Type hints are "describing intent" NOT "writing specifications" in Part 4

---

### Rule 3: RUTHLESS CONTEXT FILTERING

**When extracting from context materials:**

**Chapter 13 "Introduction to Python":**
- ✅ "What is Python?" → USE (intro concept)
- ✅ "Your first program" → USE (intro outcome)
- ❌ "Functions" → SKIP (Ch 20 topic)
- ❌ "Classes" → SKIP (Ch 24+ topic)
- ❌ "Async/await" → SKIP (Ch 28 topic)

**Chapter 17 "Control Flow and Loops":**
- ✅ "if/elif/else statements" → USE (chapter focus)
- ✅ "for loops" → USE (chapter focus)
- ❌ "Functions" → SKIP (Ch 20 topic)
- ❌ "List comprehensions" → SKIP (advanced)
- ❌ "Exception handling" → SKIP (Ch 21 topic)

**Decision Rule:**
- IF context concept fits THIS chapter's title → EXTRACT
- IF context concept belongs to Ch N+1 or later → SKIP
- IF context concept is advanced variation → SKIP
- IF context concept requires future prerequisites → SKIP

---

### Rule 4: MINIMAL SCOPE

**Depth > breadth.**

- Beginner (Ch 12-16): 5 concepts max, 3-4 lessons
- Intermediate (Ch 17-23): 7 concepts max, 4-5 lessons
- Advanced (Ch 24-29): 10 concepts max, 5-6 lessons

---

### Rule 5: MINIMAL FILES

**Create ONLY:**
- ✅ spec.md (what students learn)
- ✅ plan.md (how we teach it)
- ✅ tasks.md (implementation checklist)

**Never create:**
- ❌ index.md, _templates/, _assets/, _code-examples/, lesson-template.md, capstone-rubric.md

---

### Rule 6: TROUBLESHOOTING IS AI PARTNERSHIP

**Real-world context:** In an AI-native world, students will encounter errors (installation, syntax, environment issues). Rather than detailed troubleshooting in every chapter, teach students to ASK their AI assistant.

**Application in chapters:**
- **Installation/Setup chapters**: Include prompt like: `"I tried to install Python but got this error: [error]. What does this mean and how do I fix it?"`
- **Execution chapters**: Include prompt like: `"My program runs but gives this output. Is this correct? Why?"`
- **Advanced chapters**: Include prompt like: `"I'm getting a TypeError. Walk me through what went wrong."`

**Why this works:**
- ✅ Teaches resilience: Errors are information to be understood, not obstacles
- ✅ Builds partnership: AI becomes problem-solving collaborator, not just code generator
- ✅ Scales with complexity: Works for simple errors (Python not found) to complex errors (type mismatches)
- ✅ Honors reality: Professional developers ask AI for error help constantly

**Example (from Chapter 13, Lesson 2):**
```markdown
### Prompt 2: Troubleshoot Installation Errors
\`\`\`
I tried to install Python but got this error: [describe your error].
What does this mean and how do I fix it?
\`\`\`

**Expected outcome**: AI explains the error and provides step-by-step fixing instructions.
```

This single prompt replaces 10 pages of platform-specific troubleshooting guides that become outdated.

---

### Rule 7: GRADUATED TEACHING PATTERN (Constitution Principle 13)

**Apply the three-tier teaching approach from the constitution:**

**Tier 1 - Foundational Concepts** (Book Teaches Directly):
- Stable, core concepts explained directly in book
- Direct explanation with analogies and examples
- Examples: What are variables? What is a loop? What are type hints?
- NO "Ask your AI: What is X?" for foundations
- Book provides clear, authoritative explanation first

**Tier 2 - Complex Syntax** (AI Companion Handles):
- Complex syntax patterns AI handles (student directs, AI executes)
- Student specifies WHAT they want, AI handles HOW
- Examples: Decorators, context managers, complex regex, async/await patterns
- "Tell your AI: Create X with these requirements..."
- Student learns strategy and intent, not memorization of syntax

**Tier 3 - Scaling Operations** (AI Orchestration):
- Operations involving 10+ items or multi-file workflows
- Student orchestrates strategy, AI manages tactical execution
- Examples: Setting up 10 test environments, batch file conversions, project scaffolding
- "Tell your AI: Set up 10 X with Y configuration..."
- Student learns orchestration and supervision skills

**Application to Part 4 (Chapters 12-29)**:
- Primarily Tier 1 (foundations) and Tier 2 (applied syntax)
- Tier 3 introduced gradually in advanced chapters (24-29)
- Balance: Book teaches concepts, AI handles complexity, student directs strategy

---

### Rule 8: STANDARDIZED "TRY WITH AI" FORMAT

**Every lesson MUST end with "Try With AI" section** following this exact structure (verified in Chapter 1 and Chapter 13):

```markdown
## Try With AI

Use your AI companion (Claude Code or Gemini CLI). [Brief context about what you're exploring].

### Prompt 1: [Descriptive Title]
\`\`\`
[Clear, concrete prompt asking about the concept]
\`\`\`

**Expected outcome**: [What student should understand after AI response]

### Prompt 2: [Descriptive Title]
\`\`\`
[Clear, concrete prompt asking about application or edge case]
\`\`\`

**Expected outcome**: [What student learns from this]

### Prompt 3: [Descriptive Title]
\`\`\`
[Prompt encouraging deeper understanding or connection to real-world use]
\`\`\`

**Expected outcome**: [Connection to AIDD or professional practice]

### Prompt 4: [Descriptive Title]
\`\`\`
[Synthesis prompt pulling together concepts from lesson]
\`\`\`

**Expected outcome**: [Integration of understanding]
```

**Critical requirements:**
- ✅ Exactly 4 prompts per lesson (progressive complexity)
- ✅ Prompts are CONCRETE and SPECIFIC (not "ask AI about X")
- ✅ Each prompt has explicit "Expected outcome" describing what student learns
- ✅ Prompts should include rubric-style validation ("Does this answer your spec?")
- ✅ No "Key Takeaways" or "Summary" sections after "Try With AI"
- ✅ "Try With AI" is the final substantive section (closure point)

**CRITICAL LESSON CLOSURE PATTERN** (Constitutional Mandate):

Lessons MUST end with "Try With AI" section ONLY. Prompt 4 provides cognitive closure.

**NEVER ADD after "Try With AI":**
- ❌ "Key Takeaways" or "Summary"
- ❌ "What's Next"
- ❌ "Completion Checklist" (even for capstone lessons)
- ❌ "Chapter Summary"
- ❌ Any other closure content

**WHY**: Try With AI Prompt 4 already provides reflection and synthesis. Additional sections create cognitive overload and violate Constitutional Rule 13. This was identified as a critical violation in Chapter 14 technical review.

**Why this matters:**
- Consistency across entire book (students know the format)
- Progressive prompts teach exploration, not memorization
- "Expected outcome" sets clear learning targets
- Validates understanding without artificial quizzes
- Prompt 4 synthesis provides natural closure

---

## ORCHESTRATED WORKFLOW (What Actually Happens)

When you run `/sp.python-chapter [N]`:

### PHASE 0: Context Gathering (Interactive)

1. **Validate chapter**: Read `specs/book/chapter-index.md` and extract chapter title (ANCHOR)
2. **Ask 4 questions**:
   - Who are we teaching? (audience → complexity tier)
   - What's the core focus for THIS chapter? (scope → concept limit)
   - What can students BUILD? (outcome → learning objective)
   - Which context aspects fit? (materials → pedagogical patterns)
3. **Store responses** for next phases

**Apply AIDD**: Specification-first means understanding WHO and WHAT before designing HOW.

---

### PHASE 1: Specification (Automated)

```
→ Invoke: /sp.specify [chapter-context]
  ├─ Pass: chapter number, title, user answers, context materials
  ├─ Apply: AI-Native Learning principles, cognitive load limits, teaching patterns
  ├─ Create: specs/part-4-chapter-[N]/spec.md
  └─ Report: "Spec created. Review and approve."

WAIT: User reviews spec.md
→ User confirms: "✅ Spec approved" or provides feedback
  ├─ If feedback: Update spec.md iteratively
  └─ If approved: Continue to PHASE 2
```

**What /sp.specify receives:**
- Chapter title (anchor from chapter-index.md)
- User's audience answer (determines complexity tier: A1/A2/B1)
- User's scope answer (limits concepts to 5/7/10)
- User's outcome answer (real thing students will build)
- Context materials (extracted pedagogically)
- AI-Native Learning pattern (describe intent → explore → validate → learn from errors)
- Teaching pattern template (What it is → Code → Try → Why it matters)
- Cognitive load limits (max 5 for beginner, 7 for intermediate, 10 for advanced)

---

### PHASE 2: Planning (Automated)

```
→ Invoke: /sp.plan [spec-context]
  ├─ Read: specs/part-4-chapter-[N]/spec.md
  ├─ Apply: Lesson progression, CEFR proficiency levels, AI prompts, skills-proficiency-mapper
  ├─ Create: specs/part-4-chapter-[N]/plan.md
  └─ Report: "Plan created. Review and approve."

WAIT: User reviews plan.md
→ User confirms: "✅ Plan approved" or provides feedback
  ├─ If feedback: Update plan.md iteratively
  └─ If approved: Continue to PHASE 3
```

**What /sp.plan receives:**
- Approved spec.md (learning objectives, concepts, success criteria)
- Chapter scope (what fits this chapter, what doesn't)
- AI-Native Learning pattern (Describe intent → Explore → Validate → Learn from errors)
- Proficiency expectations (CEFR A1/A2/B1 levels)
- Real outcome students will build
- Skills proficiency mapper for CEFR validation and cognitive load checks

---

### PHASE 3: Tasks (Automated)

```
→ Invoke: /sp.tasks [spec+plan-context]
  ├─ Read: specs/part-4-chapter-[N]/spec.md + plan.md
  ├─ Apply: Acceptance criteria, validation steps, implementation checklist
  ├─ Create: specs/part-4-chapter-[N]/tasks.md
  └─ Report: "Tasks created. Review and approve."

WAIT: User reviews tasks.md
→ User confirms: "✅ Tasks approved" or provides feedback
  ├─ If feedback: Update tasks.md iteratively
  └─ If approved: Continue to PHASE 4
```

**What /sp.tasks receives:**
- Approved spec.md + plan.md (complete design)
- Learning objectives (what success looks like)
- Lessons (what needs to be implemented)
- Acceptance criteria (how to validate)

---

### PHASE 4: Implementation (Optional)

```
→ Ask user: "Ready to implement lesson content?"

Options:
A) Implement with lesson-writer subagent
   → Invoke: lesson-writer subagent
   → Pass: spec.md, plan.md, tasks.md
   → Apply: AI-Native Learning pattern, CEFR levels, validation-first approach
   → Create: docs/part-4/chapter-[N]/{01,02,03,04}-lesson-*.md
   → Then: Invoke technical-reviewer for validation

B) Manual implementation
   → User implements using tasks.md as checklist

C) Done for now
   → Keep design artifacts, skip implementation

→ Report final status
```

---

## KEY PRINCIPLES (Always Applied)

### ✅ AI-Native Learning First (Part 4 Appropriate)
- Apply AI-Native Learning pattern: describe intent → explore → validate → learn from errors
- Reference AIDD principles from Chapters 1-11 for context (not formal methodology)
- Validation-first practice: "How will students test understanding?"
- AI partnership: "How will they use Claude Code/Gemini CLI as co-reasoning partners?"
- NO formal "specification writing" (that's Part 5+) - use "describe intent" framing

### ✅ No Forward References
- Zero mentions of Chapters 30+ (SDD taught later)
- No "Specification-Driven Development" terminology (use "AI-Native Learning")
- No concepts from future chapters
- Chapter title from `chapter-index.md` is the absolute anchor

### ✅ Honors User Intent
- User's audience choice = final decision (never override)
- User's scope answer = limits concepts (never expand)
- User's outcome answer = determines lessons (never modify)

### ✅ Ruthless Context Filtering
- Only extract context matching THIS chapter's title
- Skip concepts from future chapters (even if in materials)
- Skip advanced variations and tangential concepts

### ✅ Cognitive Load Limits
- Max 5 concepts for beginner (Ch 12-16)
- Max 7 concepts for intermediate (Ch 17-23)
- Max 10 concepts for advanced (Ch 24-29)

### ✅ Teaching Intelligence Preserved
- Every phase applies AI-Native Learning principles
- Every phase uses teaching patterns (Book → AI Companion → AI Orchestration)
- Every phase respects chapter boundaries
- Every phase validates against acceptance criteria
- Skills proficiency mapping applied in planning phase (CEFR levels, cognitive load)

---

## EXECUTION INSTRUCTIONS (For Claude Code)

**CRITICAL**: This is an EXECUTABLE orchestration prompt, not documentation. Claude Code must:
1. Follow this flow exactly, in this order
2. Automatically invoke downstream commands WITHOUT asking for approval first
3. Pass full context (AIDD principles, teaching patterns) to each command
4. Respect approval gates ONLY between phases (not before first invocation)

### THE ORCHESTRATED WORKFLOW (EXECUTABLE)

#### PHASE 0: Validation & Context Gathering (Interactive)

1. **Read and validate chapter number**:
   - Read: `specs/book/chapter-index.md`
   - Extract chapter title for chapters 12-29 only
   - Reject if chapter < 12 or > 29
   - Store: `chapter_title`, `chapter_num`, `part_num` (derived from chapter)

   **Chapter-to-Part Mapping**:
   - Part 4 (Python Fundamentals): Chapters 12-29
     - Beginner (Ch 12-16): A1-A2 proficiency, max 5 concepts/lesson
     - Intermediate (Ch 17-23): A2-B1 proficiency, max 7 concepts/lesson
     - Advanced (Ch 24-29): B1-B2 proficiency, max 10 concepts/lesson

2. **Ask 4 clarifying questions** (Interactive user input):
   ```
   Q1: Who is the primary audience for Chapter [N]: [Title]?
   Q2: What is the core focus for THIS chapter ONLY?
   Q3: What should students be able to BUILD by the end?
   Q4: How should this chapter emphasize AIDD principles?
   ```
   - Store all 4 answers in context
   - Apply AIDD thinking: Specification-first means understanding WHO and WHAT before HOW

3. **Create feature branch** (Automatic, NO USER INTERACTION):
   ```bash
   git checkout -b [branch-name]
   ```
   Where `[branch-name]` = `[NNN]-topic-slug` (e.g., `014-data-types`)

---

#### PHASE 1: Specification (Automated + Intelligent)

**THIS PHASE INVOKES `/sp.specify` AUTOMATICALLY WITH FULL CONTEXT**

1. **Prepare context** (Ruthless filtering applied):
   - Gather user's 4 answers from PHASE 0
   - Extract materials from context directories (if available):
     - `context/13_chap12_to_29_specs/` (legacy structure)
     - `context/part-4-python/` (preferred structure)
     - Skip if no context available (spec from scratch is valid)
   - Apply ruthless filtering: Skip future chapters, skip advanced variations, skip tangential concepts
   - Embed AI-Native Learning principles in the context
   - Embed teaching patterns in the context (Book → AI Companion → AI Orchestration)
   - Embed cognitive load limits (5 for beginner, 7 for intermediate, 10 for advanced)

2. **Invoke /sp.specify with full context**:
   ```
   /sp.specify [chapter-slug]

   Write Chapter [N]: [Title] in Part [P]

   [Full AIDD context, user answers, teaching patterns, cognitive load rules, ruthlessly filtered context materials]
   ```

3. **Wait for /sp.specify completion**:
   - ✅ `specs/part-[P]-chapter-[N]/spec.md` is created
   - ✅ AIDD principles applied
   - ✅ Teaching patterns specified
   - ✅ Learning objectives aligned with evals

4. **Output approval checkpoint**:
   ```
   ✅ PHASE 1 COMPLETE: Specification Created

   📋 specs/part-[P]-chapter-[N]/spec.md

   Please review and confirm:
   - ✅ "Spec approved" to proceed to planning
   - 📝 Feedback to revise specification
   - ❓ Questions for clarification
   ```

5. **Wait for user approval**: Block here until user confirms "✅ Spec approved" OR provides feedback

---

#### PHASE 2: Planning (Automated + Intelligent) - Triggered After Spec Approval

**THIS PHASE INVOKES `/sp.plan` AUTOMATICALLY WITH FULL CONTEXT**

1. **Prepare context** (Read approved spec, add intelligence):
   - Read: `specs/part-[P]-chapter-[N]/spec.md` (the approved specification)
   - Extract: Learning objectives, key concepts, success criteria
   - Add: CEFR proficiency levels (A1/A2/B1 based on audience)
   - Add: Skills proficiency mapping (identify skills, assign CEFR levels, validate progression)
   - Add: Cognitive load validation (max concepts per lesson based on proficiency)
   - Add: Bloom's taxonomy alignment (cognitive complexity matching proficiency level)
   - Add: Lesson progression rules (foundational → applied → integration)
   - Add: AI prompts for each lesson (validation-first approach)
   - Add: Teaching pattern structure for every lesson (Book → AI Companion → AI Orchestration)

2. **Invoke /sp.plan with full context**:
   ```
   /sp.plan [chapter-slug]

   [Full context from spec, CEFR levels, lesson structure, AIDD teaching patterns]
   ```

3. **Wait for /sp.plan completion**:
   - ✅ `specs/part-[P]-chapter-[N]/plan.md` is created
   - ✅ Lessons broken down lesson-by-lesson
   - ✅ CEFR proficiency levels assigned
   - ✅ AI prompts specified

4. **Output approval checkpoint**:
   ```
   ✅ PHASE 2 COMPLETE: Plan Created

   📋 specs/part-[P]-chapter-[N]/plan.md

   Please review and confirm:
   - ✅ "Plan approved" to proceed to tasks
   - 📝 Feedback to revise plan
   - ❓ Questions for clarification
   ```

5. **Wait for user approval**: Block here until user confirms "✅ Plan approved" OR provides feedback

---

#### PHASE 3: Tasks (Automated + Intelligent) - Triggered After Plan Approval

**THIS PHASE INVOKES `/sp.tasks` AUTOMATICALLY WITH FULL CONTEXT**

1. **Prepare context** (Read approved spec + plan, add validation):
   - Read: `specs/part-[P]-chapter-[N]/spec.md` (learning objectives)
   - Read: `specs/part-[P]-chapter-[N]/plan.md` (lesson structure)
   - Add: Acceptance criteria for each lesson
   - Add: Validation steps (how to test understanding)
   - Add: Implementation checklist (content requirements)

2. **Invoke /sp.tasks with full context**:
   ```
   /sp.tasks [chapter-slug]

   [Full context from spec + plan, acceptance criteria, validation steps]
   ```

3. **Wait for /sp.tasks completion**:
   - ✅ `specs/part-[P]-chapter-[N]/tasks.md` is created
   - ✅ Implementation checklist defined
   - ✅ Validation steps specified

4. **Output completion report**:
   ```
   ✅ ALL DESIGN ARTIFACTS COMPLETE

   📋 specs/part-[P]-chapter-[N]/spec.md
   📋 specs/part-[P]-chapter-[N]/plan.md
   📋 specs/part-[P]-chapter-[N]/tasks.md
   ```

5. **Ask for next step**:
   ```
   Ready to implement?

   A) Implement with lesson-writer subagent
   B) Manual implementation (use tasks.md as checklist)
   C) Done for now (keep designs, skip implementation)
   ```

---

#### PHASE 4: Implementation (Optional) - Triggered Only If User Chooses A

**THIS PHASE INVOKES lesson-writer subagent IF AND ONLY IF USER CHOOSES OPTION A**

1. **Prepare context** (Read all 3 approved artifacts):
   - Read: `specs/part-[P]-chapter-[N]/spec.md`
   - Read: `specs/part-[P]-chapter-[N]/plan.md`
   - Read: `specs/part-[P]-chapter-[N]/tasks.md`
   - Add: AIDD teaching pattern (What it is → Code → Try → Why it matters)
   - Add: CEFR levels for validation
   - Add: Validation-first approach (test understanding before moving on)

2. **Invoke lesson-writer subagent** (Only if user chose Option A):
   ```
   Task(
       subagent_type="lesson-writer",
       prompt=prepare_lesson_writer_prompt(
           spec, plan, tasks,
           aidd_teaching_pattern=True,
           cefr_levels=True,
           validation_first=True
       )
   )
   ```

3. **Wait for lesson-writer completion**:
   - ✅ `docs/part-[P]/chapter-[N]/{01,02,03,04}-lesson-*.md` created
   - ✅ Full AI-Native Learning methodology applied
   - ✅ AI partnership approach emphasized

4. **Invoke technical-reviewer** (Automatic validation):
   ```
   Task(
       subagent_type="technical-reviewer",
       prompt=f"""
       Validate Chapter {N}: {Title} with special focus on:

       **AI-Native Learning Principles**:
       - 4-step pattern applied (describe intent → explore → validate → learn from errors)
       - AI positioned as co-reasoning partner, not coding assistant
       - Students directing AI, not passive learners

       **Part 4 Appropriate Language**:
       - NO "Specification-Driven Development" terminology (that's Part 5+)
       - Use "describe intent" not "write specifications"
       - AI-Native Learning framing, not professional SDD

       **Lesson Closure Pattern**:
       - ALL lessons end with "Try With AI" section ONLY
       - NO "Key Takeaways", "Summary", "Checklist" after Try With AI
       - Prompt 4 provides cognitive closure

       **Technical Accuracy**:
       - All code runs on Python 3.14+
       - Modern type hints throughout (list[int], dict[str, float], X | None)
       - No security issues, no hardcoded secrets

       **Constitutional Compliance**:
       - All 9 domain skills applied
       - Graduated teaching pattern followed
       - CEFR proficiency levels appropriate
       - Cognitive load within limits

       Output: Validation report with PASS/CONDITIONAL PASS/FAIL verdict
       """
   )
   ```

5. **Apply critical fixes** (if validation identifies issues):
   - Critical issues: MUST fix before proceeding
   - Major issues: SHOULD fix for quality
   - Minor issues: Optional improvements
   - Re-run technical-reviewer after fixes

6. **Final report**:
   ```
   ✅ CHAPTER [N] VALIDATED AND COMPLETE

   📚 Lessons created: docs/part-[P]/chapter-[N]/
   📋 Validation report: VALIDATION_REPORT_CHAPTER_[N].md

   Next steps:
   - Review validation report
   - Test lessons interactively
   - Prepare for publication
   - Commit to git
   ```

---

### CRITICAL EXECUTION RULES

1. **Sequential Invocation**: Phases execute in order (0 → 1 → 2 → 3 → 4), never out of order
2. **Automatic Chaining**: Each phase automatically invokes the next command (no "ask user first")
3. **Approval Gates Only Between Phases**: User approves AFTER each phase completes, BEFORE next phase starts
4. **Context Preservation**: Each phase reads prior phase outputs and passes them forward
5. **Vertical Intelligence Embedded**: EVERY command invocation includes AIDD principles, teaching patterns, cognitive load rules
6. **Ruthless Filtering**: Materials from future chapters are SKIPPED, not extracted
7. **No User Override**: User intent (audience, scope, outcome) is NEVER overridden, only honored
8. **Feature Branch Creation**: Automatic checkout of feature branch in PHASE 0, before any other work
9. **All 3 Artifacts Required**: Spec, Plan, and Tasks must exist before implementation can proceed

---

## CRITICAL VALIDATION (Before Each Phase)

**PHASE 1 Validation** (before `/sp.specify`):
- ✅ Chapter number valid (12-29, Part 4 only)
- ✅ Chapter title matches `chapter-index.md`
- ✅ User's audience answer captured
- ✅ User's scope answer captured
- ✅ User's outcome answer captured
- ✅ Context will be ruthlessly filtered (skip future chapters)
- ✅ AI-Native Learning principles will be applied (NOT formal SDD)

**PHASE 2 Validation** (before `/sp.plan`):
- ✅ spec.md was created successfully
- ✅ Concept count ≤ tier limit (5/7/10 based on chapter range)
- ✅ No forward references (Chapters 30+ or SDD terminology)
- ✅ AI-Native Learning framing used (not formal SDD)
- ✅ Only Chapters 1-N are prerequisites
- ✅ Teaching pattern respected (Book → AI Companion → AI Orchestration)
- ✅ Skills proficiency mapping will be applied

**PHASE 3 Validation** (before `/sp.tasks`):
- ✅ plan.md was created successfully
- ✅ Lessons match spec's learning objectives
- ✅ Proficiency levels assigned (CEFR A1/A2/B1)
- ✅ Cognitive load validated (concepts per lesson within limits)
- ✅ AI prompts specified for each lesson (4 prompts, progressive)
- ✅ Validation points defined
- ✅ Lesson closure pattern specified (Try With AI ONLY)

**PHASE 4 Validation** (before lesson-writer):
- ✅ All 3 design files exist and are valid
- ✅ User chose implementation option
- ✅ Context filtered ruthlessly (no future chapters)
- ✅ AI-Native Learning principles embedded
- ✅ Graduated teaching pattern clear
- ✅ Ready for lesson content creation

**PHASE 4 Post-Implementation Validation** (technical-reviewer):
- ✅ All lessons implement AI-Native Learning pattern
- ✅ No SDD terminology used inappropriately
- ✅ Lesson closure pattern followed (Try With AI ONLY)
- ✅ Code quality validated (Python 3.14+, type hints)
- ✅ CEFR proficiency levels appropriate
- ✅ Constitutional compliance verified

---

## WHAT GETS CREATED

**By End of PHASE 3** (mandatory):
```
specs/part-4-chapter-[N]/
  ├── spec.md       (What students learn + AI-Native Learning principles)
  ├── plan.md       (How we teach it, lesson-by-lesson + CEFR levels + skills mapping)
  └── tasks.md      (Implementation checklist + validation)
```

**By End of PHASE 4** (if Option A chosen):
```
book-source/docs/04-Part-4-Python-Fundamentals/[N]-[chapter-name]/
  ├── readme.md                    (Chapter overview and navigation)
  ├── 01-[lesson-name].md          (Lesson 1)
  ├── 02-[lesson-name].md          (Lesson 2)
  ├── 03-[lesson-name].md          (Lesson 3)
  ├── 04-[lesson-name].md          (Lesson 4, or more based on plan)
  └── 05-[capstone-name].md        (Optional capstone lesson)

VALIDATION_REPORT_CHAPTER_[N].md   (Technical review results)
```

---

## EXAMPLE EXECUTION (What User Sees)

```
> /sp.python-chapter 14

⏺ PHASE 0: Context Gathering

Chapter 14: "Data Types" (Part 4)
Prerequisites: Chapters 1-13 (AIDD principles + Python intro)

Q1: Who are we teaching?
[User answers: Absolute beginners AND professionals transitioning to AI-native]

Q2: Core focus for THIS chapter?
[User answers: Core data types - int, float, str, bool, None + type hints]

Q3: What will students BUILD?
[User answers: Interactive Type Explorer program demonstrating all core types]

Q4: Which context aspects from materials?
[User answers: Use existing structure but emphasize AI-Native Learning pattern]

✅ Context gathered. Moving to PHASE 1...

---

⏺ PHASE 1: Specification (Automated)

Invoking: /sp.specify with chapter context...
Applying: AI-Native Learning principles, teaching patterns, cognitive load limits

[/sp.specify generates spec.md]

📋 Spec created: specs/part-4-chapter-14/spec.md

Please review the specification:
- Does this match your vision for Chapter 14?
- Are learning objectives clear?
- Is scope appropriate (not too broad)?
- Are AI-Native Learning principles emphasized?

Reply with: "✅ Spec approved" or provide feedback

[User: ✅ Spec approved]

✅ Spec approved. Moving to PHASE 2...

---

⏺ PHASE 2: Planning (Automated)

Invoking: /sp.plan with approved spec...
Applying: Lesson progression, CEFR levels, AI prompts, skills-proficiency-mapper

[/sp.plan generates plan.md with skills metadata]

📋 Plan created: specs/part-4-chapter-14/plan.md

Please review the lesson breakdown:
- Are 5 lessons appropriate (including capstone)?
- Are AI prompts specified for each lesson (4 prompts progressive)?
- Are CEFR proficiency levels correct (A2-B1 for data types)?
- Is AI-Native Learning pattern applied throughout?
- Are cognitive load limits respected?

Reply with: "✅ Plan approved" or provide feedback

[User: ✅ Plan approved]

✅ Plan approved. Moving to PHASE 3...

---

⏺ PHASE 3: Tasks (Automated)

Invoking: /sp.tasks with spec + plan...
Applying: Validation points, acceptance criteria, lesson structure

[/sp.tasks generates tasks.md]

📋 Tasks created: specs/part-4-chapter-14/tasks.md

Please review the implementation checklist:
- Are acceptance criteria clear?
- Are validation steps included (lesson closure pattern)?
- Are all 5 lessons covered with tasks?
- Are code testing tasks included?

Reply with: "✅ Tasks approved" or provide feedback

[User: ✅ Tasks approved]

✅ Tasks approved. Moving to PHASE 4...

---

⏺ PHASE 4: Implementation (Optional)

All design artifacts complete:
  ✅ specs/part-4-chapter-14/spec.md (AI-Native Learning)
  ✅ specs/part-4-chapter-14/plan.md (CEFR-leveled, skills mapped)
  ✅ specs/part-4-chapter-14/tasks.md (validation-first)

Ready to implement lesson content?

A) Implement with lesson-writer subagent + technical-reviewer validation
   → Automatically creates lesson .md files with full AI-Native Learning methodology
   → Then validates with technical-reviewer
B) Manual implementation
   → You create lessons using tasks.md as guide
C) Done for now
   → Keep design artifacts, implement later

[User chooses A]

✅ Invoking lesson-writer subagent...
[5 lessons created in parallel/sequential approach]

✅ Invoking technical-reviewer for validation...
[Validation report generated]

⚠️ CONDITIONAL PASS: 1 critical issue found
- Lesson 5 has checklist after "Try With AI" (violates closure pattern)

✅ Applying fix...
[Removed checklist section from Lesson 5]

✅ Re-validating...
[Validation passed]

---

✅ WORKFLOW COMPLETE

Chapter 14 fully validated:
  ✅ Specification (AI-Native Learning principles)
  ✅ Lesson Plan (CEFR-leveled, skills mapped, cognitive load validated)
  ✅ Implementation Tasks (58/58 complete)
  ✅ Lesson Content (5 lessons, AI-Native Learning pattern applied)
  ✅ Technical Validation (PASS - all requirements met)

📋 Validation Report: VALIDATION_REPORT_CHAPTER_14.md

Next: Commit to git, prepare for publication
```

---

## CRITICAL SUCCESS FACTORS

1. **Automatic Invocation**: `/sp.specify`, `/sp.plan`, `/sp.tasks` must be invoked automatically via SlashCommand tool with full intelligence context

2. **Vertical Intelligence Preserved**: Every phase applies AIDD principles, teaching patterns, pedagogical design, and chapter boundary awareness

3. **Approval Gates**: User must explicitly approve each phase ("✅ Approved") before proceeding to next

4. **Context Preservation**: Each phase receives full context from all previous phases + vertical intelligence

5. **Ruthless Filtering**: Context extraction must skip any concepts from future chapters, even if present in materials

6. **User Authority**: User's answers to 4 questions are final — never override with assumptions

7. **Compliance**: Every phase validates against acceptance criteria before proceeding

8. **Teaching Quality**: Intelligence flows through all 4 phases, not just documentation

---

## REFERENCES

- **Chapter Index**: `specs/book/chapter-index.md` (Part 4 Chapters: 12-29)
- **Constitution**: `.specify/memory/constitution.md` (AI-Native Learning principles, domain skills, graduated teaching pattern)
- **Skills Library**: `.claude/skills/` (skills-proficiency-mapper, learning-objectives, concept-scaffolding, etc.)
- **Context Materials**:
  - `context/13_chap12_to_29_specs/` (legacy structure)
  - `context/part-4-python/` (preferred structure)

---

## ONE COMMAND. FULL INTELLIGENCE. COMPLETE WORKFLOW.

Run `/sp.python-chapter [N]` and the system:

✅ Gathers intelligent context (AI-Native Learning-driven questions)
✅ Automatically chains `/sp.specify` → `/sp.plan` → `/sp.tasks` → `/sp.implement` with approval gates
✅ Applies vertical intelligence (AI-Native Learning, teaching patterns, pedagogy) at every phase
✅ Respects chapter boundaries (ruthless context filtering, no forward references)
✅ Honors user intent (never overrides audience/scope/outcome decisions)
✅ Validates quality (acceptance criteria at each gate)
✅ Implements lessons with lesson-writer subagent
✅ Validates with technical-reviewer (AI-Native Learning compliance, lesson closure pattern)

**Result: AI-Native Learning-centered Python chapters ready for publication.**

---

**Note**: For PHR (Prompt History Record) creation after command completion, see constitution for instructions.
