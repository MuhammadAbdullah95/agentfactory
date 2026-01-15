---
name: assessment-architect
description: Create rigorous assessments with scope intelligence, adaptive distribution, and automatic bias prevention. Auto-discovers Chapter/Part scope, detects content type (conceptual/procedural/coding), generates questions with aligned question types, and eliminates answer patterns. Scales intelligently from 25-250 questions. Triggers on "create quiz", "generate exam", "make practice questions", "assessment", or "test me on".
---

# Assessment Architect

Create intelligent, bias-free assessments from structured content with scope discovery and adaptive question distribution.

## What This Skill Does

- **Scope Intelligence**: Parse "Chapter 5" or "Part 2" → Auto-discovers all lessons (vs. manual file listing)
- **Content Classification**: Analyzes content type (conceptual/procedural/coding/mixed)
- **Adaptive Distribution**: Selects question type mix based on content (more Conceptual Distinction for conceptual content, more Specification Design for coding)
- **Intelligent Scaling**: Auto-recommends question count (25-120 range, typical 90-120 for full chapters)
- **Bias Prevention**: Detects and eliminates length bias, position bias, specificity bias
- **Multi-format Output**: Default DOCX (professional documents), also Markdown and PDF
- **Quality Validation**: Validates answer distribution, difficulty spread, source coverage, and answer biases

## What This Skill Does NOT Do

- Process PDFs, images, or non-Markdown formats
- Generate answer explanations with direct quotes (exam integrity)
- Create exams from external web content
- Guarantee bias elimination without validation (detection requires human review for specificity bias)
- Create assessments from content you can't access locally

---

## Required Clarifications (AskUserQuestion)

The skill automatically asks users **two key questions**:

| # | Question | Options | Default |
|----|----------|---------|---------|
| 1 | **Question Count & Time** | Accept recommended / More challenging / Quick / Custom | Auto-recommended (90-120) |
| 2 | **Output Format** | DOCX / Markdown / PDF | DOCX (professional) |

**Note**: Scope is auto-discovered and confirmed, no user decision needed.

### Optional Clarifications

Ask only if relevant:
- Specific sections to emphasize or exclude?
- Target audience adjustment (undergrad vs PhD)?

### Scope Examples

- "Generate exam for Chapter 5" → Auto-discovers 12 lessons in Chapter 5
- "Generate exam for Part 2" → Auto-discovers all 8 chapters in Part 2
- "From these files: lesson1.md, lesson2.md" → Use explicit files

### If User Doesn't Respond

Use defaults and note assumptions in exam header:
```
**Assumptions:** Auto-discovered scope, adaptive distribution, balanced difficulty, standard timing
```

---

## Before Implementation

| Source | Gather |
|--------|--------|
| **Scope Discovery** | If Chapter/Part input: Auto-discover lesson files using scripts/scope_discovery.py |
| **Content Classification** | Analyze content type (conceptual/procedural/coding) using scripts/content_classifier.py |
| **Distribution Selection** | Choose adaptive distribution based on content type using scripts/adaptive_distribution.py |
| **Source Files** | Read all discovered/specified Markdown files completely |
| **Content Depth** | Assess complexity for difficulty calibration |
| **Key Concepts** | Extract testable facts, definitions, relationships |
| **Section Structure** | Map headings for source references |

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

## Generation Workflow

```
1. DISCOVER SCOPE
   └── Parse input: "Chapter 5", "Part 2", or explicit files
   └── Auto-discover lessons if scope-based input
   └── Confirm with user: "Found 19 lessons. Analyzing..."

2. ANALYZE CONTENT
   └── Read source files → Extract concepts → Map sections
   └── Detect content type: conceptual / procedural / coding / mixed
   └── Estimate: 95 concepts (19 lessons × 5 concepts/lesson)

3. CALIBRATE & ASK USER ⭐ (AskUserQuestion)
   ├── QUESTION 1: Question Count & Time
   │   └── Show recommendation: "95 questions (1.6 hours est. / 2.1 hours max)"
   │   └── Options: Accept / More challenging (+15%) / Quick (-35%) / Custom (25-120)
   │   └── Display estimated time + maximum time (capped at 3 hours)
   │
   └── QUESTION 2: Output Format
       └── Options: DOCX (professional) / Markdown (version control) / PDF (printable)
       └── Default: DOCX

4. DISTRIBUTE ADAPTIVELY
   └── Select distribution for detected content type (adaptive_distribution.py)
   └── Conceptual: ↑ Conceptual Distinction (+7%), ↑ Critical Evaluation (+5.5%)
   └── Coding: ↑ Specification Design (+8%), ↑ Architecture Analysis (+2.5%)
   └── Mixed: Balanced distribution

5. GENERATE
   └── Create questions following type patterns
   └── Ensure distractors are plausible (70-90% correct)
   └── Track source section for each question
   └── Include Bloom level + question type metadata

6. VALIDATE & REMEDIATE
   └── Run structure checks (questions, options, formatting)
   └── Run answer distribution checks (A/B/C/D balance)
   └── Run bias detection: length/position/specificity (NEW)
   └── Auto-fix length and position bias if detected
   └── Flag specificity bias for manual review
   └── See references/validation-rules.md and bias-detection-guide.md

7. OUTPUT (Format Selected by User)
   ├── DOCX: Professional document (via docx skill)
   │   └── Structure: Metadata → Questions → Answer Key (at END) → Explanations
   ├── Markdown: Version control friendly
   │   └── Same structure, easy to edit
   └── PDF: Printable (via markdown → docx → pdf conversion)
```

**See WORKFLOW.md for detailed step-by-step example with actual outputs.**

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

## Output Format

```markdown
# [Exam Title]

**Source:** [file(s)]
**Questions:** [N]
**Duration:** Estimated [X] min / Maximum [Y] min

---

## Questions

**Q1.** [Question stem]
A) [Option]
B) [Option]
C) [Option]
D) [Option]

[Continue all questions...]

---

## Answer Key

| Q# | Answer | Section | Difficulty | Bloom |
|----|--------|---------|------------|-------|
| 1 | C | Part A | Medium | Apply |

---

## Explanations

### Q1
**Correct: C**
[Explanation with section reference]
Section: [Heading from source]
```

**Structure**: Questions → Answer Key (at END) → Explanations

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

| File | Purpose |
|------|---------|
| `references/question-patterns.md` | Templates for each question type with distractor strategies |
| `references/bloom-taxonomy.md` | Cognitive level classification and auto-detection |
| `references/validation-rules.md` | Quality validation criteria (structure, distribution, content, bias) |
| `references/bias-detection-guide.md` | Comprehensive guide to detecting and preventing answer biases |

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