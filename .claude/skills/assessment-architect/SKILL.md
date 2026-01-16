---
name: assessment-architect
description: Generate professional certification exams meeting MIT/academic standards with rigorous question design, psychometric validation, and systematic distractor generation. Auto-discovers scope, selects academic rigor tier (T1-T4), generates questions using evidence-based distractor strategies, validates against psychometric standards, and eliminates answer biases. Triggers on "create exam", "certification exam", "generate assessment", "professional exam", "test me".
---

# Assessment Architect

Create intelligent, bias-free assessments from structured content with scope discovery and adaptive question distribution.

## What This Skill Does

- **Scope Intelligence**: Parse "Chapter 5" or "Part 2" → Auto-discovers all lessons with intelligent weighting
- **Academic Rigor Tier Selection**: Choose T1 (Foundational), T2 (Intermediate), T3 (Advanced), or T4 (PhD Qualifying) with distinct question distributions
- **Content Classification**: Analyzes content type (conceptual/procedural/coding/mixed) to select appropriate question type distribution
- **Rigorous Question Design**: Generate questions using evidence-based distractor strategies per question type (not generic "plausible wrong")
- **Psychometric Validation**: Ensure difficulty index, discrimination index, and distractor functionality meet professional standards
- **Bias Prevention & Remediation**: Automatically detect and fix length bias, position bias; flag specificity bias for expert review
- **Multi-format Output**: DOCX (professional printable), Markdown (version control), PDF (distribution)
- **Professional Standards**: MIT/academic certification exam standards with grading rubrics and reliability metrics

## What This Skill Does NOT Do

- Process PDFs, images, or non-Markdown formats
- Generate answer explanations with direct quotes (exam integrity)
- Create exams from external web content
- Guarantee bias elimination without validation (detection requires human review for specificity bias)
- Create assessments from content you can't access locally

---

## Required Clarifications (AskUserQuestion)

The skill automatically asks users **three key questions**:

| # | Question | Options | Default |
|----|----------|---------|---------|
| 1 | **Academic Rigor Tier** | T1 (Foundational) / T2 (Intermediate) / T3 (Advanced) / T4 (PhD Qualifying) | T2 (Intermediate) |
| 2 | **Question Count & Time** | Accept recommended / More challenging (+15%) / Quick (-35%) / Custom | Auto-recommended per tier |
| 3 | **Output Format** | DOCX (printable) / Markdown / PDF | DOCX (professional) |

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

**PDF**
- Generated from markdown format
- Read-only for distribution
- **Best for**: Final deliverable, student distribution

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

Gather context to ensure successful exam generation:

| Source | Gather |
|--------|--------|
| **Codebase** | Read all source Markdown files completely; assess complexity |
| **User Requirements** | Academic rigor tier (T1-T4), question count preference, output format |
| **Skill References** | Domain expertise embedded in: |
| | - `academic-rigor-tiers.md` → Question distributions per tier |
| | - `distractor-generation-strategies.md` → Systematic distractor creation |
| | - `psychometric-standards.md` → Validity/reliability standards |
| | - `question-patterns.md` → Question type templates + examples |
| **Concept Extraction** | Testable facts, definitions, relationships, key distinctions |
| **Section Mapping** | Headings for source references, relative importance |

**Key Point**: Question generation uses **embedded expertise from references/**, not runtime discovery. The skill contains professional exam design knowledge; you provide your domain content.

---

## Assessment Specifications by Tier

### Questions & Duration

| Tier | Questions | Est. Time | Max Duration |
|------|-----------|-----------|--------------|
| **T1 (Foundational)** | 50-100 | 1-1.5 hours | 2 hours |
| **T2 (Intermediate)** | 100-150 | 1.5-2.5 hours | 3 hours |
| **T3 (Advanced)** | 150-200 | 2.5-4 hours | 4 hours |
| **T4 (PhD Qualifying)** | 200-250 | 3-6 hours | 6 hours |

**Time Calculation:** ~1 min/question base, adjusted by content type (conceptual +20%, procedural +30%, coding +25%)

**Points:** 1 per question (equal weighting)

### Grading Scales by Tier

#### T1: Foundational Certification
| Grade | % | Pass? |
|-------|---|-------|
| Pass with Distinction | 90-100 | ✓ |
| Competent | 80-89% | ✓ |
| Minimally Competent | 70-79% | ✓ |
| Not Yet Competent | <70% | ✗ |

#### T2: Intermediate Certification
| Grade | % | Pass? |
|-------|---|-------|
| Expert | 90-100% | ✓ |
| Proficient | 80-89% | ✓ |
| Competent | 75-79% | ✓ |
| Needs Improvement | <75% | ✗ |

#### T3: Advanced Certification
| Grade | % | Pass? |
|-------|---|-------|
| Advanced Mastery | 90-100% | ✓ |
| Solid Expertise | 85-89% | ✓ |
| Competent Specialist | 80-84% | ✓ |
| Does Not Meet Standard | <80% | ✗ |

#### T4: PhD Qualifying
| Grade | % | Pass? |
|-------|---|-------|
| Exceptional - Research Ready | 95-100% | ✓ |
| Strong - Research Ready | 90-94% | ✓ |
| Acceptable - Doctoral Qualified | 85-89% | ✓ |
| Does Not Meet Doctoral Standard | <85% | ✗ |

---

## Generation Workflow

```
1. DISCOVER SCOPE
   └── Parse input: "Chapter 5", "Part 2", or explicit files
   └── Auto-discover lessons, assess content density
   └── Confirm: "Found 19 lessons across 340 pages. Proceeding..."

2. ANALYZE CONTENT (Professional Standards)
   └── Read source files → Extract testable concepts
   └── Detect content type: conceptual / procedural / coding / mixed
   └── Assess complexity: Beginner vs. Advanced concepts
   └── Count unique testable facts, relationships, definitions

3. ASK USER ⭐ (AskUserQuestion - 3 Questions)
   ├── QUESTION 1: Academic Rigor Tier
   │   ├── T1 (Foundational): Entry-level, 70% pass expected
   │   ├── T2 (Intermediate): Professional development, 65% pass expected
   │   ├── T3 (Advanced): Specialist credential, 40% pass expected
   │   └── T4 (PhD Qualifying): Doctoral preparation, 25% pass expected
   │
   ├── QUESTION 2: Question Count & Time ⭐ (Tier-Specific)
   │   ├── SHOW RECOMMENDATION: "[Tier] Recommendation: 120 questions (1.5-2.5 hours estimated / 3 hours max)"
   │   ├── OPTIONS:
   │   │   ├── Accept recommended (Default for tier)
   │   │   ├── More challenging (+15% questions)
   │   │   ├── Quick (-35% questions, shorter time)
   │   │   └── Custom count (25-250 range)
   │   └── Display time calculation based on content type
   │
   └── QUESTION 3: Output Format
       ├── Options: DOCX (professional printable) / Markdown (git-friendly) / PDF (printable)
       └── Default: DOCX

4. SELECT DISTRIBUTION (from references/academic-rigor-tiers.md)
   └── T1 Foundational: 70% recall + distinction, 30% applied
   └── T2 Intermediate: 50% foundational, 50% advanced
   └── T3 Advanced: 30% foundational, 70% advanced
   └── T4 PhD: 20% foundational, 80% research-ready
   └── Content type adjustments (conceptual/procedural/coding)

5. GENERATE RIGOROUS QUESTIONS (from references/distractor-generation-strategies.md)
   ├── For EACH question type:
   │   ├── Extract core concept from source
   │   ├── Formulate correct answer (aligns to Bloom level)
   │   ├── Identify misconceptions learners make
   │   ├── Generate 3 distractors using type-specific strategies:
   │   │   ├── Precision Recall: Off-by-one, unit errors, adjacent values
   │   │   ├── Conceptual Distinction: Surface-level confusion, partial truth
   │   │   ├── Decision Matrix: Fail on each constraint individually
   │   │   ├── Architecture Analysis: Different component roles
   │   │   ├── Economic/Quantitative: Calculation errors
   │   │   ├── Specification Design: Over/under-specification
   │   │   ├── Critical Evaluation: Primary vs. secondary trade-offs
   │   │   ├── Strategic Synthesis: Missing one integration element
   │   │   └── Research Extension: Over-generalization or missing constraints
   │   └── Validate: Length parity, specificity match, all distractors ≥5% function
   │
   └── Track metadata: Source section, Bloom level, question type, difficulty estimate

6. VALIDATE PSYCHOMETRIC QUALITY (from references/psychometric-standards.md)
   ├── Structure validation:
   │   ├── ✓ Question count matches target (±5%)
   │   ├── ✓ Each question exactly 4 options (A-D)
   │   └── ✓ Sequential numbering with no gaps
   ├── Distribution validation:
   │   ├── ✓ Answer distribution: Each letter 20-30%
   │   ├── ✓ No >3 consecutive same-letter answers
   │   └── ✓ No predictable patterns
   ├── Psychometric validation:
   │   ├── ✓ Difficulty Index (DIF) per tier (T1:65-75%, T2:60-70%, T3:50-60%, T4:45-55%)
   │   ├── ✓ Discrimination Index (DIS) > 0.30 for most questions
   │   ├── ✓ Distractor Functionality (DF) ≥5% for all options
   │   ├── ✓ Item-Total Correlation (ITC) average ≥0.25
   │   └── ✓ Kuder-Richardson KR-20 per tier (T1:≥0.75, T2:≥0.80, T3:≥0.85, T4:≥0.85)
   ├── Bias detection:
   │   ├── ✓ Length Bias: Auto-fix if detected
   │   ├── ✓ Position Bias: Auto-remediate with balanced sequences
   │   └── ✓ Specificity Bias: Flag for expert review
   └── Content validation:
       ├── ✓ All major topics represented
       ├── ✓ Bloom levels match tier distribution
       └── ✓ Question types match tier distribution

7. REMEDIATE ISSUES
   └── Length bias: Rewrite options to match word count
   └── Position bias: Apply proven answer sequences for 25% per letter
   └── Specificity bias: Enhance distractors to match detail level
   └── Low discrimination: Review question wording, verify answer key
   └── Nonfunctional distractors: Replace with realistic misconceptions

8. OUTPUT (Format Selected by User)
   ├── DOCX: Professional document
   │   ├── Header: Title, exam code, question count, duration, grading scale
   │   ├── Questions: Each on new line, all options on separate lines
   │   ├── Answer Key: Compact reference (10 per line for fast checking)
   │   └── Explanations: Full section with source context for each question
   ├── Markdown: Version control friendly
   │   ├── Same structure, easy to edit + track changes
   │   └── Table-based answer key with metadata
   └── PDF: Printable distribution format
       └── Generated via markdown → docx → PDF conversion
```

**Result**: Professional certification exam meeting MIT/academic standards with validated rigor, reliability (KR-20), and discrimination across all questions.

---

## Question Type Distribution by Academic Rigor Tier

### T1 (Foundational) - 70% Foundational, 30% Applied

| Type | % | Purpose |
|------|---|---------|
| Precision Recall | 15 | Core definitions, terminology |
| Conceptual Distinction | 20 | Paired concepts, clear differences |
| Decision Matrix | 15 | Simple two-criteria scenarios |
| Architecture Analysis | 10 | Component roles, straightforward flows |
| Economic/Quantitative | 10 | Basic calculations |
| Specification Design | 10 | Framework application, standard cases |
| Critical Evaluation | 5 | Simple trade-offs |
| Strategic Synthesis | 5 | Two-concept integration |
| Research Extension | 0 | Not applicable |

### T2 (Intermediate) - 50% Foundational, 50% Advanced

| Type | % | Purpose |
|------|---|---------|
| Precision Recall | 8 | Reduced - focus on understanding |
| Conceptual Distinction | 12 | Nuanced differences, subtle confusions |
| Decision Matrix | 15 | Multi-criteria with trade-offs |
| Architecture Analysis | 15 | System components with constraints |
| Economic/Quantitative | 10 | Complex calculations, ROI |
| Specification Design | 15 | Framework application, non-standard cases |
| Critical Evaluation | 15 | Trade-off analysis, judgment |
| Strategic Synthesis | 10 | Multi-concept integration with constraints |
| Research Extension | 0 | Not applicable |

### T3 (Advanced) - 30% Foundational, 70% Advanced

| Type | % | Purpose |
|------|---|---------|
| Precision Recall | 5 | Minimal - assumes mastery |
| Conceptual Distinction | 8 | Highly nuanced distinctions |
| Decision Matrix | 12 | Complex multi-criteria scenarios |
| Architecture Analysis | 15 | System design with competing requirements |
| Economic/Quantitative | 8 | Advanced modeling, comparative analysis |
| Specification Design | 15 | Framework application, novel cases |
| Critical Evaluation | 20 | Complex trade-offs, edge cases |
| Strategic Synthesis | 12 | Multi-level concept synthesis |
| Research Extension | 5 | Extrapolation to related domains |

### T4 (PhD Qualifying) - 20% Foundational, 80% Research-Ready

| Type | % | Purpose |
|------|---|---------|
| Precision Recall | 3 | Minimal - assumes deep mastery |
| Conceptual Distinction | 5 | Subtle theoretical distinctions |
| Decision Matrix | 8 | Complex scenarios with research findings |
| Architecture Analysis | 10 | System design from first principles |
| Economic/Quantitative | 5 | Advanced quantitative reasoning |
| Specification Design | 7 | Designing methodology for novel problems |
| Critical Evaluation | 20 | Rigorous critique of proposals |
| Strategic Synthesis | 15 | Integration across sub-domains |
| Research Extension | 27 | Novel scenarios, research design |

See `references/academic-rigor-tiers.md` for detailed question examples per tier.

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

## Output Location & Paths

### Source Content Path
```
apps/learn-app/docs/
├── 01-agent-factory-paradigm/
├── 02-AI-Tool-Landscape/
│   └── 05-claude-code-features-and-workflows/
│       ├── 04-hello-world-basics.md
│       ├── 05-tool-landscaping.md
│       └── [... other lessons ...]
└── [... other chapters ...]
```
**How to specify:** "Create exam for Chapter 5" → Auto-discovers `02-AI-Tool-Landscape/05-claude-code-features-and-workflows/*.md`

### Generated Assessment Output Path
```
assessments/
├── assessment-chapter-5-claude-code-features.docx
├── assessment-chapter-5-claude-code-features.md
├── test-part-2-ai-native-development.docx
└── quick-quiz-kubernetes-fundamentals.pdf
```

**Features**:
- ✅ `assessments/` folder auto-created if missing
- ✅ Filenames cleaned from exam title (lowercase, hyphens, no special chars)
- ✅ Format extension added automatically (.docx / .md / .pdf)
- ✅ All formats saved simultaneously (use whichever you prefer)
- ✅ Easy to organize and share with students/stakeholders

**Example filename derivation:**
```
User input: "Create exam for Chapter 5: Claude Code Features and Workflows"
Generated outputs:
  - assessment-chapter-5-claude-code-features.docx (professional printing)
  - assessment-chapter-5-claude-code-features.md (version control, editing)
  - assessment-chapter-5-claude-code-features.pdf (digital distribution)
```

---

## Output Format Examples

### DOCX Format (Printable - Recommended)

```
Agent Factory Fundamentals: Building Digital Full-Time Equivalents (FTEs)
Exam L1: P1-AGFF
90 Questions | 120 Minutes

1) The 'Agent Factory Thesis' primarily reframes the AI business opportunity as:
A. Manufacturing digital employees rather than selling traditional software
B. Shipping UI features rather than codifying organizational expertise
C. Selling token bundles rather than selling recurring subscriptions
D. Optimizing chat workflows rather than deploying autonomous systems

2) Which of the following best describes the core value proposition?
A. Reducing software licenses by 50%
B. Replacing human expertise with commodity AI
C. Codifying expert knowledge into autonomous, repeatable systems
D. Increasing chat interface sophistication

[...Questions 3-90...]

---

Answer Key
Reference this section after completing the quiz to check your answers.

1-A, 2-C, 3-B, 4-A, 5-B, 6-B, 7-B, 8-B, 9-A, 10-D
11-A, 12-A, 13-A, 14-C, 15-C, 16-A, 17-B, 18-D, 19-C, 20-C
[...more grouped by 10...]

---

Explanations

Q1 - Correct Answer: A
Source: Agent Factory Fundamentals

The Agent Factory Thesis posits that instead of selling software licenses,
companies can manufacture digital full-time equivalents (FTEs)...

------

Q2 - Correct Answer: C
Source: Agent Manufacturing Principles

Manufacturing agents transforms domain expertise into codified systems...
```

**Structure**:
- Header (title, exam code, count, duration)
- Questions (each on new line, all options on separate lines)
- Answer Key (compact, 10 per line for quick reference)
- Explanations (full details for each question)

### Markdown Format (Version Control Friendly)

```markdown
# Agent Factory Fundamentals Assessment

**Source:** P1-AGFF
**Questions:** 90
**Duration:** 120 minutes
**Content Type:** Conceptual

---

## Questions

**Q1.** The 'Agent Factory Thesis' primarily reframes...
A) Manufacturing digital employees...
B) Shipping UI features...
C) Selling token bundles...
D) Optimizing chat workflows...

[Continue all questions...]

---

## Answer Key

| Q# | Answer | Section | Difficulty | Bloom |
|----|--------|---------|------------|-------|
| 1 | A | Agent Factory Fundamentals | Medium | Understand |
| 2 | C | Agent Manufacturing Principles | Medium | Understand |

---

## Explanations

### Q1
**Correct: A**
The Agent Factory Thesis posits...
**Source Section:** Agent Factory Fundamentals
```

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
| `references/academic-rigor-tiers.md` | **NEW**: T1-T4 framework with question distributions, example questions per tier, grading scales |
| `references/distractor-generation-strategies.md` | **NEW**: Systematic procedures for generating plausible distractors per question type |
| `references/psychometric-standards.md` | **NEW**: Professional validation metrics (DIF, DIS, DF, KR-20) and quality thresholds |
| `references/question-patterns.md` | Templates for each question type with detailed examples and distractor strategies |
| `references/bloom-taxonomy.md` | Cognitive level classification and auto-detection guidance |
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