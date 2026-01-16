---
name: assessment-architect
description: Create rigorous assessments with scope intelligence, adaptive distribution, and automatic bias prevention. Auto-discovers Chapter/Part scope, detects content type (conceptual/procedural/coding), generates questions with aligned question types, and eliminates answer patterns. Scales intelligently from 25-200 questions (typically 90-120). Triggers on "create quiz", "generate exam", "make practice questions", "assessment", or "test me on".
---

# Assessment Architect

Create intelligent, bias-free assessments from structured content with scope discovery and adaptive question distribution.

## What This Skill Does

- **Scope Intelligence**: Parse "Chapter 5" or "Part 2" → Auto-discovers all lessons
- **Content Classification**: Analyzes content type (conceptual/procedural/coding/mixed)
- **Adaptive Distribution**: Selects question type mix based on content (more Conceptual Distinction for conceptual content, more Specification Design for coding)
- **Intelligent Scaling**: Auto-recommends question count (25-200 range, typical 90-120 for full chapters)
- **Bias Prevention**: Detects and eliminates length bias, position bias, specificity bias
- **Multi-format Output**: Default DOCX (professional documents), also Markdown and PDF
- **Quality Validation**: Validates answer distribution, difficulty spread, source coverage, and answer biases

---

## Required Clarifications (AskUserQuestion)

The skill automatically asks users **two key questions**:

| # | Question | Options | Default |
|----|----------|---------|---------|
| 1 | **Question Count & Time** | Accept recommended / More challenging / Quick / Custom | Auto-recommended (90-120) |
| 2 | **Output Format** | DOCX (printable) / Markdown / PDF | DOCX (professional) |

**Note**: Scope is auto-discovered and confirmed, no user decision needed.

### Format Details

**DOCX (Recommended - Printable Format)**
- Professional exam header: Title, exam code, question count, duration
- Questions: Each on new line with all options on separate lines (A., B., C., D.)
- Answer Key: Compact quick reference (10 answers per line for fast checking)
- Explanations: Full detailed section for each question with source context
- **Best for**: Printing, formal assessment, professional distribution

**Markdown**
- Version control friendly (text-based)
- Table-based answer key (detailed with metadata)
- Full explanations with source sections
- **Best for**: Editing, version control, publishing to web

### Optional Clarifications

Ask only if relevant:
- Specific sections to emphasize or exclude?
- Target audience adjustment (undergrad vs PhD)?

### Scope Examples

- "Generate exam for Chapter 5" → Auto-discovers 12 lessons in Chapter 5
- "Generate exam for Part 2" → Auto-discovers all 8 chapters in Part 2
- "From these files: lesson1.md, lesson2.md" → Use explicit files


---

## Before Implementation

**Gather context to ensure successful autonomous question generation:**

| Source | Gather | Autonomous Reasoning |
|--------|--------|---------------------|
| **Scope Discovery** | Parse user input for chapter identifier (e.g., "Chapter 5"). Traverse hierarchy: (1) List all Part dirs (01-, 02-, 03-...) in apps/learn-app/docs/, (2) For each Part, list subdirectories to find chapters, (3) Match requested chapter number, (4) Return chapter directory path and discover lessons. Handles "Chapter X", "Part Y", "Part Y, Chapter X" formats. | Scopes auto-discovered; no manual path entry needed except for custom multi-file inputs |
| **Content Classification** | Analyze content type (conceptual/procedural/coding/mixed) to inform distribution selection. | Determines which question types to emphasize (Conceptual → +7% Conceptual Distinction; Coding → +8% Specification Design) |
| **Concept Extraction** | Extract 5-8 testable concepts per lesson. Note complexity (factual, procedural, conceptual, evaluative). | Used later to decide question type (factual → Precision Recall; conceptual → Conceptual Distinction; scenario → Decision Matrix) |
| **Reference Mapping** | For each concept, note source section and Bloom level (Remember/Understand/Apply/Analyze/Evaluate/Create). | Ensures every question has source context in explanations. |
| **Distribution Budget** | Select Bloom distribution (25% Remember/Understand, 20% Apply, 25% Analyze, 18% Evaluate, 12% Create) and question type distribution per academic-rigor-tiers.md. | Creates type budget: "of 100 questions, Precision Recall = 10, Conceptual Distinction = 15, etc." Used for batch coordination. |


**State File Management** (Priority 2):
Before generation, create `questions_progress.json`:
```json
{
  "total_questions": 100,
  "batch_strategy": "parallel_5x20",
  "batches": [
    {"batch_id": 1, "range": "Q1-Q20", "status": "pending", "generated": 0},
    {"batch_id": 2, "range": "Q21-Q40", "status": "pending", "generated": 0},
    {"batch_id": 3, "range": "Q41-Q60", "status": "pending", "generated": 0},
    {"batch_id": 4, "range": "Q61-Q80", "status": "pending", "generated": 0},
    {"batch_id": 5, "range": "Q81-Q100", "status": "pending", "generated": 0}
  ],
  "global_distribution": {
    "position": {"A": 0, "B": 0, "C": 0, "D": 0},
    "question_types": {"Precision_Recall": 0, "Conceptual_Distinction": 0, ...},
    "bloom_levels": {"Remember": 0, "Understand": 0, ...},
    "option_lengths": []
  }
}
```

**Reference Usage During Generation** (Priority 4 - Mandatory Checks):

| Step | Reference File | When | What to Do | Outcome |
|------|---------|------|-----------|---------|
| **Step 4** | `academic-rigor-tiers.md` | Before distributing question types | Read tier-specific distributions (T1-T4); select default T2 or user preference | Type targets: "of 100 Q, use 10% Precision Recall, 15% Conceptual Distinction, ..." |
| **Step 5** (per Q) | `distractor-generation-strategies.md` | After deciding question type (via decision tree) | Read Section [1A/2A/3A/...] matching type; extract specific distractor procedure | 3 distractors generated per type strategy, not generic "plausible" answers |
| **Step 5** (per 10 Q) | `psychometric-standards.md` | After every 10 questions in batch | Check DIF/DIS/DF/KR-20 thresholds vs tier targets | Validate metrics; if out of range, adjust next 10 questions |
| **Step 6** | `psychometric-standards.md` | During validation | Check all red flags (DIF too high/low, DIS < min, DF < 5%) | If issues found, flag for review/remediation |

**MANDATORY VALIDATION**: Before generating ANY questions:
```
ABORT if ANY missing:
  ✓ academic-rigor-tiers.md exists? If NO → STOP with error
  ✓ distractor-generation-strategies.md exists? If NO → STOP with error
  ✓ psychometric-standards.md exists? If NO → STOP with error
  ✓ generation-procedures.md exists? If NO → STOP with error

BEFORE STEP 4: READ academic-rigor-tiers.md completely
BEFORE STEP 5: READ generation-procedures.md completely
BEFORE STEP 5: READ distractor-generation-strategies.md completely (all 9 sections)
BEFORE STEP 6: READ psychometric-standards.md completely

If you cannot read these files, ABORT and inform user that references are missing from skill directory.
```

### Explicit Reference Reading Protocol

**Step 4 (Distribution Selection)**:
```
CHECK: Is academic-rigor-tiers.md present?
READ: Section for selected tier (T1/T2/T3/T4)
EXTRACT: Question type percentages, Bloom distribution, grading scale, DIF/DIS targets
APPLY: Create type budget (e.g., "100 questions → 10 Precision Recall, 15 Conceptual Distinction...")
VALIDATE: Budget matches tier targets
```

**Step 5 (Per-Question Generation)**:
```
FOR EACH QUESTION:
  1. DECIDE: Use decision tree → Determine question type
  2. CHECK: Is distractor-generation-strategies.md present?
  3. READ: Section [1A/2A/3A/4A/4B/5A/5B/6A/6B/7A/8A/9A] matching type decision
  4. EXTRACT: Type-specific distractor procedure (e.g., "Precision Recall → Off-by-one, unit error, misconception")
  5. GENERATE: 3 distractors following EXACT procedure from reference
  6. VALIDATE: Check position/length/distractor_functionality immediately
```

**Step 5 (Per-10-Questions Checkpoint)**:
```
AFTER Q10, Q20, Q30, ... in each batch:
  1. CHECK: Is psychometric-standards.md present?
  2. READ: Tier-specific thresholds (Mean DIF, Min DIS, Min DF, KR-20 targets)
  3. CALCULATE: Current metrics for this batch of 10
  4. COMPARE: Current vs. tier targets
  5. ADJUST: If out of range, modify next 10 questions (easier/harder/adjust types)
  6. UPDATE: Log metrics in questions_progress.json
```

---

## Assessment Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Questions** | 90-120 (typical) | Min 25, Max 120 |
| **Estimated Time** | 1-2.5 hours | ~1 min/question (varies by content type) |
| **Maximum Duration** | 180 min (3 hours) | Hard cap on test duration |
| **Points** | 1 per question | Equal weighting |
| **Time Estimation** | Auto-calculated | Content type affects pace (conceptual slower, coding slower) |

### Grading Scale

| Grade | % | Classification |
|-------|---|----------------|
| A+ | 95-100 | Exceptional - PhD qualifying |
| A | 90-94.99 | Strong mastery |
| B+ | 85-89.99 | Good foundation |
| B | 80-84.99 | Satisfactory |
| C | 70-79.99 | Marginal pass |
| F | <70 | Fail - Retake required |

---

## Generation Workflow with Autonomous Reasoning

```
1. DISCOVER SCOPE
   └── Parse input: "Chapter 5", "Part 2", or explicit files
   └── Auto-discover lessons if scope-based input
   └── Confirm with user: "Found 19 lessons. Analyzing..."

2. ANALYZE CONTENT
   └── Read source files → Extract concepts → Map sections
   └── Detect content type: conceptual / procedural / coding / mixed
   └── Estimate: 95 concepts (19 lessons × 5 concepts/lesson)
   └── REASONING: Use complexity assessment to inform type distribution

3. CALIBRATE & ASK USER ⭐ (AskUserQuestion)
   ├── QUESTION 1: Question Count & Time
   │   └── Show recommendation: "95 questions (1.6 hours est. / 2.1 hours max)"
   │   └── Options: Accept / More challenging (+15%) / Quick (-35%) / Custom (25-120)
   │   └── Display estimated time + maximum time (capped at 3 hours)
   │
   └── QUESTION 2: Output Format
       └── Options: DOCX (professional) / Markdown (version control) / PDF (printable)
       └── Default: DOCX

4. DISTRIBUTE ADAPTIVELY & CREATE TYPE BUDGET
   ├── Select tier from academic-rigor-tiers.md (default: T2 Intermediate)
   ├── Read academic-rigor-tiers.md → Apply tier-specific distributions
   ├── Detect content type → Modify distributions (Conceptual: +7% Conceptual Distinction; Coding: +8% Specification Design)
   ├── Create type budget: "of 100 questions, Precision_Recall = 10, Conceptual_Distinction = 15, Decision_Matrix = 12.5, ..."
   └── REASONING: Budget ensures all batches coordinate on type distribution (Priority 2)

5. PARALLEL BATCH GENERATION (Priority 5)
   ├── Initialize questions_progress.json with batch schema
   ├── Calculate concept distribution: 20 concepts per batch
   ├── SPAWN 5 PARALLEL BACKGROUND TASKS:
   │   ├── Background Task 1 → Generate Q1-20 (reads progress file, updates atomically)
   │   ├── Background Task 2 → Generate Q21-40 (reads progress file, updates atomically)
   │   ├── Background Task 3 → Generate Q41-60 (reads progress file, updates atomically)
   │   ├── Background Task 4 → Generate Q61-80 (reads progress file, updates atomically)
   │   └── Background Task 5 → Generate Q81-100 (reads progress file, updates atomically)
   ├── Main session: Poll progress file every 30s
   ├── When all batches status="complete": Proceed to Step 6
   ├── If any batch fails: Retry that batch only (not entire generation)
   └── REASONING: Parallel batches prevent context overflow & enable quality focus per batch (Priority 5)

   **BACKGROUND TASK TEMPLATE** (see "Background Task Implementation" section below):
   For each task generating 20 questions:
   ├── Read shared questions_progress.json
   ├── Calculate available type budget for this batch (e.g., if 20% Precision Recall total = 20 questions, batch 1 already has 4, batch 2 can have max 4 more)
   ├── For EACH question Q1-Q20 in batch:
   │   ├── DECISION 1: Extract concept from lessons
   │   ├── DECISION 2: Decide question type using decision tree (below)
   │   ├── DECISION 3: Check type budget - if full, pick different type
   │   ├── ACTION: Read distractor-generation-strategies.md Section [1A/2A/3A/etc] matching question type (Priority 4)
   │   ├── ACTION: Generate correct answer + 3 distractors per strategy
   │   ├── VALIDATE: After every question, check position/length/type distribution (Priority 3)
   │   │   └── If position B > 30% of batch → Force next answer to A/C/D
   │   │   └── If avg correct answer > 16 words → Simplify next answer
   │   │   └── If type exceeds budget → Next question must be different type
   │   ├── UPDATE: Atomically update questions_progress.json
   │   └── CONTINUE: Process next question
   ├── Mark batch as "complete" in progress file
   └── Return to main session

6. CONTINUOUS VALIDATION (Priority 3) - DURING GENERATION, NOT AFTER
   ├── Per question: Check position distribution (target 25% per letter)
   ├── Per question: Check option lengths (all within ±3 words of median)
   ├── Per question: Check distractor functionality (all should be ≥5% plausible)
   ├── Per 10 questions: Validate against psychometric-standards.md thresholds
   │   └── DIF (Difficulty Index) within tier range (T2: 50-65%)
   │   └── DIS (Discrimination Index) > 0.30
   │   └── DF (Distractor Functionality) ≥ 5%
   │   └── KR-20 (Reliability) on track for tier (T2: ≥0.70)
   ├── Auto-adjust next batch based on metrics
   └── REASONING: Real-time validation prevents accumulation of bias (Priority 3)

7. ASSEMBLE & OUTPUT (Format Selected by User)
   ├── DOCX: Professional document (via docx skill)
   │   └── Structure: Metadata → Questions → Answer Key (at END) → Explanations
   ├── Markdown: Version control friendly
   │   └── Same structure, easy to edit
   └── PDF: Printable (via markdown → docx → pdf conversion)
```

**See references/generation-procedures.md for detailed decision trees and type-selection logic.**

---

## Question Type Distribution

| Type | % | Purpose |
|------|---|---------|
| Precision Recall | 10 | Exact values, definitions |
| Conceptual Distinction | 15 | Paired/contrasting concepts |
| Decision Matrix | 12.5 | Multi-criteria scenarios |
| Architecture Analysis | 12.5 | System components, flows |
| Economic/Quantitative | 10 | Calculations, comparisons |
| Specification Design | 10 | Framework application |
| Critical Evaluation | 12.5 | Trade-offs, judgments |
| Strategic Synthesis | 10 | Multi-concept integration |
| Research Extension | 7.5 | Novel scenario extrapolation |

See `references/question-patterns.md` for templates and examples.

---

## Bloom's Taxonomy Distribution

| Level | % | Question Characteristics |
|-------|---|--------------------------|
| Remember/Understand | 25 | Recall facts, explain concepts |
| Apply | 20 | Use in new situations |
| Analyze | 25 | Break down, compare, contrast |
| Evaluate | 18 | Judge, critique, justify |
| Create/Synthesize | 12 | Design, propose, integrate |

See `references/bloom-taxonomy.md` for level indicators.

---

## Answer Construction Rules

### Baseline Requirements

1. **Option A**: Never "All/None of the above"
2. **Correct Answer**: One clearly correct option
3. **Distractors**: Plausible but fail on critical detail (70-90% correct)
4. **Distribution**: Roughly equal A:B:C:D across exam (20-30% per letter)
5. **Sequences**: No more than 3 consecutive same-letter answers

### Bias Prevention Requirements (NEW)

6. **Length Parity**: All options within ±3 words
   - Prevents test-takers selecting longest/shortest option
   - Validated automatically; flagged for manual fix if needed

7. **Specificity Balance**: All options equally detailed
   - If correct answer includes examples ("e.g.", "such as"), distractors should too
   - Match qualifier density ("typically", "usually")
   - Avoid: "Yes" vs "Large organizations with strong metrics and documented processes..."

8. **Position Distribution**: Correct answers evenly spread across A/B/C/D
   - Target: 25% per letter
   - Acceptable range: 20-30% per letter
   - Middle (B+C) ≤55%, Outer (A+D) ≥40%
   - Auto-fixed using pre-made sequences if imbalanced

See `references/bias-detection-guide.md` for detailed examples and remediation strategies.

---

## Autonomous Decision Making: Decision Framework (Priority 1)

**See `references/generation-procedures.md` → Decision Tree for Question Type Selection**

For EACH extracted concept, use the 8-decision tree to autonomously select question type. The decision tree:
1. Evaluates concept characteristics (exact value? paired concepts? multi-criteria? etc.)
2. Maps to corresponding question type (Precision Recall, Conceptual Distinction, Decision Matrix, etc.)
3. Returns strategy section from distractor-generation-strategies.md (e.g., Section 1A, 2B, 3A)

This enables Claude to reason about WHICH question type is appropriate, not just apply templates.

---

## Parallel Batch Architecture (Priority 5)

**Why parallel batches?** Sequential generation fills context window, accumulates bias, and creates all-or-nothing failures. Parallel batches enable:
- 5 × 20 questions instead of 100 sequential
- Independent validation per batch
- Shared state prevents conflicts
- Failure isolation (retry only failed batch)

**See `references/generation-procedures.md` → Parallel Batch Coordination Logic** for budget calculation examples and main session orchestration details.

---

## Background Task Implementation (Priority 6)

**See `references/generation-procedures.md` → Background Task Template & Continuous Validation Triggers**

Each background task follows a standard template:
1. **Setup**: Read questions_progress.json, calculate available budget per type
2. **Per-Question Loop** (20 iterations):
   - Extract concept, Decide type (via decision tree), Read strategy, Generate question
   - Continuous validation: Check position/length/type distributions after EACH question
   - Auto-adjust next question if metrics drift (e.g., if B > 30%, force next answer to A/C/D)
3. **Finalization**: Validate batch against psychometric-standards.md, mark complete

**Key Autonomous Decisions**:
- **Type Selection**: Decision tree based on concept characteristics
- **Type Enforcement**: Budget check (if Precision Recall budget exhausted, pick different type)
- **Position Control**: Real-time check (if B > 30% of batch, force next answer to A/C/D)
- **Length Control**: Real-time check (if option lengths drift, rewrite to maintain ±3 word parity)

---

## Multi-Document Handling

When multiple source files provided:

```
weight[doc] = word_count[doc] / total_word_count
questions[doc] = round(total_questions * weight[doc])
```

Create distinct sections per source or merge thematically (user preference).

---

## Output Location

All generated assessments are automatically saved to:
```
assessments/
├── assessment-chapter-5-claude-code-features.md
├── test-part-2-ai-native-development.docx
└── quick-quiz-kubernetes-fundamentals.pdf
```

**Features**:
- ✅ `assessments/` folder auto-created if missing
- ✅ Filenames cleaned from titles (lowercase, hyphens, no special chars)
- ✅ Format extension added automatically
- ✅ Easy to organize and share

---

## Output Format Details

**DOCX** (Recommended): Professional header → Questions (4 options each) → Answer Key (10 per line) → Explanations with source context.

**Markdown**: Same structure, version-control friendly with metadata table for quick reference.

**PDF**: Generated from Markdown via docx conversion for read-only distribution.

See `references/output-format-examples.md` for detailed examples and formatting specifications.

---

## Scaling Algorithm

```python
def calculate_questions(content):
    concepts = extract_testable_concepts(content)

    if len(concepts) >= 100:
        return 200  # Full exam
    elif len(concepts) >= 50:
        return 100  # Half exam
    elif len(concepts) >= 25:
        return 50   # Quarter exam
    else:
        return max(25, len(concepts))  # Minimum viable
```

---

## Edge Case Handling

| Situation | Action |
|-----------|--------|
| **Conflicting info in source** | Flag in exam notes; create question testing the distinction |
| **Ambiguous concepts** | Skip or ask user for clarification before generating |
| **Too few testable facts** | Scale down; warn user if <25 questions possible |
| **Highly technical jargon** | Include definition in question stem if needed |
| **Multiple valid interpretations** | Avoid or phrase as "According to [source]..." |
| **Source has errors** | Do not correct; test what source states (note discrepancy) |

---

## Validation Pipeline

Run ALL checks before delivery. See `references/validation-rules.md`.

### Quick Checklist

- [ ] Question count matches calculated target
- [ ] Each question has exactly 4 options (A-D)
- [ ] Answer distribution within 20-30% per letter
- [ ] No >3 consecutive same-letter answers
- [ ] All Bloom levels represented per distribution
- [ ] All question types represented per distribution
- [ ] Every question has section reference
- [ ] No direct quotes in explanations
- [ ] Difficulty distribution matches content complexity

---

## Reference Files

**Core Domain Knowledge** (MIT Professional Standards):
| File | Purpose | When to Read |
|------|---------|-------------|
| `references/academic-rigor-tiers.md` | T1-T4 framework with tier-specific distributions, rigor levels, grading scales | Step 4: Select tier and apply distributions |
| `references/distractor-generation-strategies.md` | Type-specific distractor procedures (9 sections: 1A-9A+) with examples | Step 5: Per question, after deciding type |
| `references/psychometric-standards.md` | Professional metrics (DIF, DIS, DF, KR-20) and tier-specific thresholds | Step 5: After every 10 questions |
| `references/generation-procedures.md` | Decision tree for question type selection + background task template + budget coordination | Step 5: Background task implementation |
| `references/output-format-examples.md` | Detailed DOCX, Markdown, PDF formatting specs with examples | Step 7: Output assembly |

**Quality & Validation**:
| File | Purpose |
|------|---------|
| `references/question-patterns.md` | Templates for each question type with examples |
| `references/bloom-taxonomy.md` | Cognitive level classification |
| `references/validation-rules.md` | Quality validation criteria |
| `references/bias-detection-guide.md` | Length, position, specificity bias detection and remediation |

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/scope_discovery.py` | Parse scope input and auto-discover lesson files |
| `scripts/content_classifier.py` | Detect content type (conceptual/procedural/coding) |
| `scripts/adaptive_distribution.py` | Select distribution based on content type |
| `scripts/bias_detector.py` | Detect length, position, and specificity biases |
| `scripts/option_normalizer.py` | Analyze and normalize option word counts |
| `scripts/validate_exam.py` | Complete validation pipeline orchestration |
| `scripts/config.py` | Centralized configuration and thresholds |

## Book
Content Path: `apps/learn-app/docs`