---
name: assessment-architect
description: Generate certification exams for chapters or parts. Extracts concepts first, then generates scenario-based questions. Use "ch X" for chapter, "part X" for part.
allowed-tools: Read, Grep, Glob, Bash(ls:*), Bash(wc:*), Bash(pandoc:*), Write, Edit, Task, TaskCreate, TaskUpdate, TaskList, TaskGet
---

# Assessment Architect - Concept-First Certification Exams

Generate rigorous certification exams by extracting concepts FIRST, then building scenario-based questions from the concept map.

**Output:** DOCX in `assessments/` directory
**NOT for:** Practice quizzes (those use `*_quiz.md` in chapter directories)

---

## Operating Contract (Non-Negotiable)

These rules are structural and cannot be overridden:

1. **No memorization questions.** Every question requires a novel scenario paragraph before the stem. Questions testing recall of lesson-specific facts are rejected.
2. **Grounding notes before concepts.** Read lessons → write notes file → extract concepts FROM notes. Never extract concepts from memory. The notes file is evidence of engagement.
3. **Concepts before questions.** The concept map (built from notes) is the contract for Phase 2. Never generate questions by walking through lessons sequentially.
4. **Filesystem discovery only.** No hardcoded book structure. Use `ls -d` to find paths. The filesystem is the source of truth.
5. **Structural validation.** Anti-memorization (grep patterns) and anti-gaming (distribution bias) are FAIL conditions. Readability is a principle, not a word-count gate.
6. **Dynamic question count with lesson floor.** At minimum 2 questions per lesson. 38 lessons = at least 75 questions, not 40.
7. **TaskList for coordination.** Create tasks upfront. Update status at each phase. Subagents receive the TaskList ID.
8. **2 subagents maximum.** Each receives only the concept map + `references/question-types.md`. Not the full skill file.
9. **Persisted state.** Notes, concept map, and question files saved to `assessments/`. Validation results reported at each phase.

---

## Input Parsing (via $ARGUMENTS)

```
INPUT = $ARGUMENTS (e.g., "ch 5", "part 3", "ch 2, 3, 4", "ch 2-4")

PARSE:
  IF matches "ch N, N, N" | "chapter N, N and N" (comma/and-separated list):
    SCOPE = "multi-chapter"
    NUMS = extract all numbers → zero-pad each
    FOR each NUM: PATH[] += ls -d apps/learn-app/docs/*/$(printf '%02d' NUM)-*/

  ELSE IF matches "ch N-M" | "chapter N-M" (range):
    SCOPE = "multi-chapter"
    FOR NUM in N..M: PATH[] += ls -d apps/learn-app/docs/*/$(printf '%02d' NUM)-*/

  ELSE IF matches "ch N" | "chapter N" (single):
    SCOPE = "chapter"
    NUM = zero-pad N to 2 digits
    PATH = result of: ls -d apps/learn-app/docs/*/$(printf '%02d' N)-*/

  ELSE IF matches "part N" | "p N" | "pN":
    SCOPE = "part"
    NUM = zero-pad N to 2 digits
    PATH = result of: ls -d apps/learn-app/docs/$(printf '%02d' N)-*/

  ELSE IF bare number:
    AskUserQuestion: "Did you mean Chapter {N} or Part {N}?"

  ELSE IF empty:
    AskUserQuestion: "Which chapter or part? (e.g., 'ch 5' or 'part 3')"

VALIDATE:
  FOR each path: run ls -d. If no result: FAIL "Path not found"

DISCOVER LESSONS:
  FOR each PATH (single or multi):
    LESSONS += ls {PATH}/*.md | grep -v README | grep -v summary | grep -v quiz
  LESSON_COUNT = total across all paths

CONFIRM with user (AskUserQuestion):
  "Found {SCOPE}: {chapter names and numbers}
   Path(s): {paths}
   Total lessons: {LESSON_COUNT}
   Proceed?"
```

---

## Task Coordination

After confirming scope, create a TaskList to track progress and coordinate subagents:

```
TaskCreate: "Discover scope and confirm with user" → mark in_progress immediately
TaskCreate: "Read lessons and write grounding notes" (blocked by task 1)
TaskCreate: "Extract concept map from grounding notes" (blocked by task 2)
TaskCreate: "Calculate question count and confirm with user" (blocked by task 3)
TaskCreate: "Generate questions - Subagent A (Scenario + Transfer)" (blocked by task 4)
TaskCreate: "Generate questions - Subagent B (Relationship + Evaluation)" (blocked by task 4)
TaskCreate: "Validate all questions" (blocked by tasks 5, 6)
TaskCreate: "Assemble exam and generate DOCX" (blocked by task 7)
```

Update each task status as work progresses. Subagents receive the TaskList ID so they can update their own task status upon completion.

---

## Grounding Notes (MANDATORY)

As you read each lesson, write observations to `assessments/{SLUG}-notes.md`. This file is your working memory and evidence of genuine engagement with the content.

**Format (append per lesson):**
```markdown
## Lesson: {filename}

**Key concepts:** {2-5 concepts worth testing}
**Relationships to other lessons:** {what connects to what}
**Testable trade-offs:** {decisions or comparisons in this lesson}
**Transfer potential:** {where else this principle applies}
**Surprise/insight:** {anything non-obvious that would make a good question}
```

**Rules:**
- Write notes DURING reading, not after all lessons are read
- This file is the RAW INPUT for concept extraction (Phase 1 reads notes, not memory)
- The concept map MUST cite specific notes entries as evidence
- If a concept in the map has no corresponding note: it's fabricated, remove it

---

## 4 Question Types

All questions require a concise scenario before the stem. No fact-recall patterns allowed.

| Type | % | Bloom Level | Key Constraint |
|------|---|-------------|----------------|
| **Scenario Analysis** | 40% | Apply/Analyze | Novel situation not appearing in lessons |
| **Concept Relationship** | 25% | Analyze/Evaluate | Tests CONNECTION between 2+ concepts |
| **Transfer Application** | 20% | Apply/Create | Apply principle to a domain NOT in the chapter |
| **Critical Evaluation** | 15% | Evaluate | Identify WHY an approach fails in context |

For detailed patterns and examples, see `references/question-types.md`.

### Readability Principle

**The difficulty is in the THINKING, not the READING.**

Write at professional-clear level. One idea per sentence. Active voice. No filler. The agent has full autonomy over word counts — the principle is clarity, not a specific number.

**WRONG (bloated — agent should never produce this):**
```
Q. A veteran meteorologist notices that her department's new AI weather
prediction system presents 48-hour forecasts with identical confidence
formatting regardless of actual prediction reliability. A tropical storm
forecast with high uncertainty appears identically to a clear-sky prediction
with strong model consensus. Junior forecasters have stopped adding uncertainty
qualifiers to public advisories, trusting the AI's confident presentation.

Applying the principle that confidence is uncorrelated with accuracy in AI
systems, which practice would most improve the department's forecast
communication reliability?

A) Requiring independent verification of AI forecasts against ensemble models
before accepting any prediction, regardless of how confidently it is presented
```

**RIGHT (clear, same concept tested):**
```
Q. A weather AI displays all forecasts with equal confidence — a risky
tropical storm prediction looks identical to a reliable clear-sky forecast.
Junior staff stopped questioning AI outputs.

How should the team handle AI outputs that show no uncertainty signal?

A) Verify all AI forecasts against independent sources before publishing
```

Same concept. Same difficulty. The right version is just clearer because it has no filler.

---

## Dynamic Question Count

The count must ensure adequate coverage. A chapter with 25 lessons getting 30 questions means barely 1 question per lesson - that's a quiz, not an exam.

```
concept_count = number of concepts extracted in Phase 1
lesson_count = total lessons in scope

concept_base = ceil(concept_count * 0.8)
lesson_floor = lesson_count * 2          # At minimum: 2 questions per lesson

base = max(concept_base, lesson_floor)   # Whichever is HIGHER

tier_multiplier:
  T1 (Introductory) = 0.7
  T2 (Intermediate) = 1.0  [default]
  T3 (Advanced)     = 1.3

raw = base * tier_multiplier
result = clamp(round_to_nearest_5(raw), min=30, max=150)
```

Examples:
- 15 lessons, 25 concepts (T2) -> max(20, 30) = 30 -> 30
- 38 lessons, 52 concepts (T2) -> max(42, 76) = 76 -> rounded to 75
- 8 lessons, 60 concepts (T2) -> max(48, 16) = 48 -> rounded to 50
- 25 lessons, 95 concepts (T2) -> max(76, 50) = 76 -> rounded to 75

The lesson_floor prevents exams that skip lessons. Present recommendation to user. User can override with any value 30-150.

---

## 4-Phase Workflow

### Phase 0.5: Read Lessons & Write Grounding Notes (this agent)

Read ALL lessons in scope. As you read each one, APPEND observations to `assessments/{SLUG}-notes.md` (see Grounding Notes section above).

This is not optional. The notes file is the evidence that you actually engaged with the content. Phase 1 builds the concept map FROM the notes file, not from memory.

Update task status: mark "Read lessons and write grounding notes" as in_progress, then completed.

---

### Phase 1: Concept Extraction (this agent)

Read `assessments/{SLUG}-notes.md` (your grounding notes). Extract concepts from the notes, not from memory.

**What to extract** (see `references/concept-extraction-guide.md` for details):
- Core concepts (named ideas, patterns, principles)
- Relationships (concept A enables/conflicts/extends concept B)
- Trade-offs (choosing X means sacrificing Y)
- Transfer domains (where else could this principle apply?)

**Every concept MUST cite a grounding note entry.** If you can't point to a specific note, the concept is fabricated.

**Output:** Write to `assessments/{SLUG}-concepts.md`

Format:
```markdown
# Concept Map: {Chapter/Part Name}

## Concepts (N total)

### 1. {Concept Name}
- Definition: {1-2 sentences}
- Lessons: {which lessons cover this}
- Relationships: {connects to concepts X, Y}
- Transfer domains: {healthcare, finance, education, etc.}

### 2. {Concept Name}
...

## Relationships
- {Concept A} --enables--> {Concept B}
- {Concept C} --conflicts-with--> {Concept D}
...

## Trade-offs
- {Choosing X} vs {Choosing Y}: {what you sacrifice}
...
```

After extraction:
1. Report concept count and recommend question count (dynamic algorithm above)
2. Ask user to confirm or override question count
3. Ask user for difficulty tier (T1/T2/T3, default T2)

---

### Phase 2: Question Generation (2 parallel Task subagents)

Spawn 2 Task subagents. Each receives ONLY:
- The concept map (`assessments/{SLUG}-concepts.md`)
- Question type reference (`references/question-types.md`)
- Their assigned types and count

See `references/subagent-template.md` for prompt templates.

**Subagent A:** Scenario Analysis + Transfer Application questions
- Output: `assessments/{SLUG}-questions-A.md`
- Count: 60% of total (40% Scenario + 20% Transfer)

**Subagent B:** Concept Relationship + Critical Evaluation questions
- Output: `assessments/{SLUG}-questions-B.md`
- Count: 40% of total (25% Relationship + 15% Evaluation)

---

### Phase 3: Validation (this agent)

Read both question files. Apply ALL structural checks:

**FAIL conditions (reject question, non-negotiable):**
```
FAIL if question contains "According to"
FAIL if question contains "Lesson [0-9]" or "lesson [0-9]"
FAIL if question contains "the document states" or "as discussed in"
FAIL if question has NO scenario paragraph before the stem
FAIL if Transfer Application domain appears anywhere in chapter content
FAIL if question doesn't map to a concept in the concept map
```

**Anti-gaming checks (FAIL conditions):**
```
FAIL if correct answer is the longest option in >40% of questions
FAIL if any letter is correct >30% or <20% of total
FAIL if >3 consecutive questions have same correct letter
FAIL if correct options average >3 words longer than distractors
```

**Distribution checks:**
```
Count answer distribution across all questions:
  Each of A/B/C/D must be 20-30% of total
  No >3 consecutive same-letter answers
  Option lengths: correct answer word count within ±3 words of distractor average
```

**Coverage check:**
```
Each concept in the map should have at least 1 question
  Flag uncovered concepts (warning, not failure)
  Report: "X of Y concepts covered (Z%)"
```

If validation fails:
- Report specific failures with question numbers
- Identify pattern (e.g., "Subagent A produced 12 questions with 'According to'")
- Regenerate only the failing subagent's output (re-spawn that subagent)

See `references/validation-rules.md` for complete validation pipeline.

---

### Phase 4: Assembly & DOCX Output (this agent)

**Step 1: Merge and STRIP internal tags**
- Interleave questions from both files (don't group by type)
- Renumber sequentially Q1 through Q{TOTAL}
- Randomize answer positions (ensure distribution holds)
- **STRIP all internal tags from student-facing questions:**
  ```
  REMOVE: [Scenario Analysis], [Concept Relationship], [Transfer Application], [Critical Evaluation]
  REMOVE: [Concept: {anything}]
  REMOVE: **Answer:** lines (answers go ONLY in answer key)
  REMOVE: **Reasoning:** sections (go ONLY in educator supplement)
  ```
- **Validation after stripping:**
  ```
  grep -E "\[(Scenario|Concept|Transfer|Critical)" assessments/{SLUG}-exam.md
  → MUST return 0 matches in the questions section
  ```

**Step 2: Build exam document (TWO separate files)**

**File 1: Student exam** (`assessments/{SLUG}-exam.md`)
```markdown
# {Chapter/Part Name} Certification Assessment

**Questions:** {TOTAL}
**Time Limit:** {ceil(TOTAL * 1.5)} minutes
**Passing Score:** 75%

**Instructions:** Select the best answer for each question.

---

Q1. {scenario paragraph}

{stem ending in ?}

A) {option}
B) {option}
C) {option}
D) {option}

---

Q2. ...
```

NO type labels. NO concept tags. NO answers. NO explanations. Just questions.

**File 2: Educator key** (`assessments/{SLUG}-answer-key.md`)
```markdown
# Answer Key: {Chapter/Part Name}

| Q | Answer | Type | Concept |
|---|--------|------|---------|
| 1 | B | Scenario Analysis | {concept name} |
| 2 | D | Concept Relationship | {concept name} |
...

## Answer Distribution
A: {count} ({%}) | B: {count} ({%}) | C: {count} ({%}) | D: {count} ({%})

## Concept Coverage
{List concepts and question count per concept}

## Type Distribution
{Scenario Analysis: X | Concept Relationship: X | Transfer Application: X | Critical Evaluation: X}
```

**Step 3: Convert to DOCX (two files)**
```bash
pandoc assessments/{SLUG}-exam.md -o assessments/{SLUG}-Assessment-Final.docx --from=markdown --to=docx
pandoc assessments/{SLUG}-answer-key.md -o assessments/{SLUG}-Answer-Key.docx --from=markdown --to=docx
```

**Step 4: Post-conversion validation**
- Verify both DOCX files exist and exam > 10KB
- **CRITICAL:** grep the exam markdown for internal tags:
  ```
  grep -cE "\[(Scenario|Concept|Transfer|Critical)" assessments/{SLUG}-exam.md
  → MUST be 0. If not: FAIL "Internal tags leaked into student exam"
  ```
- Verify NO "Answer:" or "Reasoning:" text in exam DOCX
- Report: file paths, question count, concept coverage percentage

**Step 5: Cleanup** (optional)
- Keep concept map (useful reference)
- Keep question files (for regeneration)
- Delete intermediate markdown if user prefers clean output

---

## Failure Modes (Summary)

| Failure | Prevention | Detection |
|---------|-----------|-----------|
| Memorization questions | Structural FAIL conditions | grep for "According to", "Lesson [0-9]" |
| Longest-is-correct gaming | Anti-gaming FAIL: >40% longest correct | Word count comparison |
| Answer bias (74% A) | Anti-gaming FAIL: any letter >30% | Count distribution per letter |
| Fabricated concepts | Grounding notes required | Every concept must cite a notes entry |
| Too few questions | lesson_floor = lessons * 2 | 38 lessons must produce ≥75, not 40 |
| Wrong chapter/part | `ls -d` filesystem discovery | Path validation before proceeding |
| Missing lessons | Complete lesson count + notes file | Notes file has entry per lesson |
| No coordination | TaskList created upfront | Task status visible across phases |
| Context overload | Subagents receive only concept map + types | ~300 lines context vs 937+176KB |
| Internal tags in exam | Strip [Type] and [Concept:] in Phase 4 | grep for brackets in exam.md = 0 |
| Answers in student file | Two separate files (exam + key) | No "Answer:" in exam DOCX |

For historical context on these failures, see the Jan 2026 postmortem in the skill's git history.

---

## Reference Files

| File | Purpose | Used By |
|------|---------|---------|
| `references/question-types.md` | 4 type definitions with examples | Subagents (Phase 2) |
| `references/concept-extraction-guide.md` | How to extract concepts vs facts | This agent (Phase 1) |
| `references/subagent-template.md` | Prompt templates for 2 subagents | This agent (Phase 2 spawning) |
| `references/validation-rules.md` | Complete validation pipeline | This agent (Phase 3) |
| `references/bloom-taxonomy.md` | Cognitive level reference | Subagents (question design) |
| `references/psychometric-standards.md` | DIF/DIS/DF metrics | This agent (Phase 3 validation) |
| `references/distractor-generation-strategies.md` | Distractor design patterns | Subagents (option creation) |
| `references/academic-rigor-tiers.md` | T1-T3 difficulty frameworks | This agent (Phase 1 tier selection) |

---

## Observability (Principle 7)

Report at each phase transition:

```
Phase 1 Complete:
  - Concepts extracted: {N}
  - Relationships found: {N}
  - Trade-offs identified: {N}
  - Recommended question count: {N} (T{tier})
  - Concept map: assessments/{SLUG}-concepts.md

Phase 2 Complete:
  - Subagent A: {N} questions generated ({types})
  - Subagent B: {N} questions generated ({types})
  - Total: {N} questions

Phase 3 Complete:
  - Validation: {PASS/FAIL}
  - Failed questions: {N} (reasons: ...)
  - Answer distribution: A={N} B={N} C={N} D={N}
  - Concept coverage: {X}/{Y} ({Z}%)

Phase 4 Complete:
  - DOCX: assessments/{SLUG}-Assessment-Final.docx
  - Size: {N}KB
  - Questions: {N}
  - Ready for distribution
```
