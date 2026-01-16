---
name: assessment-architect
description: Generate MIT-standard assessments through plan-validate-iterate cycles. Reads source material and generates question plans validated against psychometric standards (DIF, DIS, DF, KR-20). Subagents reason autonomously about question distribution based on content type and cognitive requirements. Adaptive scoring from 25-120 questions with automatic feedback loops for quality improvement. Triggers on "create quiz", "generate exam", "make practice questions", "assessment", or "test me on".
---

# Assessment Architect (MIT Standard)

Generate rigorous, pedagogically sound assessments using Claude reasoning for each question type.

## Core Principle

**MIT-Standard = Pedagogically Sound + Psychometrically Valid + Unbiased**

Each assessment must meet these standards:
- **DIF** (Difficulty Index): 55-70% correct answers (balance between too easy/hard)
- **DIS** (Discrimination Index): > 0.30 (strong questions differentiate performers)
- **DF** (Distractor Functionality): ≥ 5% (all options are plausible)
- **KR-20** (Reliability): ≥ 0.70 (consistent across test-takers)
- **Bloom Distribution**: 25% Remember/Understand, 35% Apply, 30% Analyze, 10% Evaluate

Each question generated through Claude reasoning:
1. Testable concept extraction from source material
2. Pedagogically appropriate question type selection
3. Reference-guided distractor generation using academic strategies
4. Real-time validation against psychometric standards

---

## What This Skill Does

**Default: T2 Intermediate Certification** (adjustable via user config)

### Exam Structure
- **100-150 questions** (100 default for T2)
- **150-180 minutes** (2.5-3 hours, adjustable)
- **Pass threshold**: 75%
- **Question Type Distribution**:
  - Precision_Recall (factual): 15%
  - Conceptual_Distinction (compare/contrast): 20%
  - Critical_Evaluation (trade-offs/analysis): 20%
  - Architecture_Analysis (system integration): 20%
  - Decision_Matrix (scenario-based): 25%

### Workflow
1. **Scope Discovery**: Parse request → Auto-discover lesson structure
2. **Content Analysis**: Extract testable concepts and classify cognitive requirements
3. **Autonomous Planning**: Subagents reason about optimal distribution
4. **Validation Loop**: Check against DIF/DIS/DF/KR-20 standards
5. **Iteration**: Subagents refine until all questions pass validation
6. **Format Output**: Generate DOCX, Markdown, or PDF (uses `/docx` skill for DOCX generation)

---

## How It Works

### Phase 1: Scope Discovery & Analysis

```
INPUT: "Generate exam for Chapter 5"

STEP 1: Auto-discover scope
  └── List all Part directories (01-, 02-, 03-, ...)
  └── For Part 2, find Chapter 05 subdirectory
  └── Discover 18 lessons in 05-claude-code-features-and-workflows/

STEP 2: Content analysis
  └── Read all 18 lessons
  └── Extract testable concepts (~5-8 per lesson = 95 total concepts)
  └── Classify content type: Procedural (70%) + Conceptual (30%)
  └── Note Bloom levels for each concept
  └── Determine question count: 100 questions (standard T2 tier)
```

### Phase 2: User Configuration

Ask two questions:

| # | Question | Default |
|----|----------|---------|
| 1 | **Question Count & Time?** | 100 questions (2 hours estimated, 3 hour max) |
| 2 | **Output Format?** | DOCX (professional) |

### Phase 3: Distribution Strategy

**T2 Intermediate Certification** targets practicing professionals (default tier):

#### Question Types (why this distribution)

| Type | Count | Cognitive Focus | Purpose |
|------|-------|---|---|
| **Precision_Recall** | 15 | Remember/Understand | Ensure foundational knowledge |
| **Conceptual_Distinction** | 20 | Understand/Apply | Distinguish between similar concepts |
| **Critical_Evaluation** | 20 | Analyze/Evaluate | Identify trade-offs and limitations |
| **Architecture_Analysis** | 20 | Apply/Analyze | Understand system integration |
| **Decision_Matrix** | 25 | Apply/Analyze | Multi-criteria decision-making in context |

#### Bloom's Cognitive Distribution

| Level | % | Definition |
|-------|---|---|
| **Remember/Understand** | 25% | Recall facts and basic comprehension |
| **Apply** | 35% | Use knowledge in new situations |
| **Analyze** | 30% | Break down and understand relationships |
| **Evaluate** | 10% | Make judgments based on criteria |

### Phase 4: Generation + Validation Loop

**Reference Directory**: `references/`

Spawn parallel subagent for each question type. Each subagent:

1. **Read source material** from lesson directory
2. **Read MIT standards references**:
   - `references/distractor-generation-strategies.md`
   - `references/psychometric-standards.md`
   - `references/bloom-taxonomy.md`
   - `references/academic-rigor-tiers.md`
3. **Generate question plan** (NOT final questions yet)
   - Propose question types and distribution based on content analysis
   - Show reasoning for each choice
   - Output: JSON with proposed questions + reasoning
4. **Main session validates plan** against psychometric standards

### Phase 4B: Validation & Iteration

Validate each question against T2 Intermediate standards:

#### Per-Question Validation

| Metric | What It Means | Target | Action If Failed |
|--------|---|---|---|
| **DIF** (Difficulty Index) | % of test-takers answering correctly | 55-70% | Too easy? Add complexity. Too hard? Clarify wording |
| **DIS** (Discrimination Index) | How well question differentiates top vs bottom performers | > 0.30 | Top performers answering incorrectly? Ambiguous wording or trick question → revise |
| **DF** (Distractor Functionality) | % selecting each distractor (should be plausible) | ≥ 5% each | No one selecting a distractor? Too obviously wrong → make more plausible |
| **Position Bias** | Answer distribution across A/B/C/D | 20-30% per letter | Skewed? Adjust answer keys to avoid patterns |

#### Per-Assessment Validation (100 questions)

| Metric | Target | What It Measures |
|--------|--------|---|
| **KR-20** | ≥ 0.70 | Overall test reliability (internal consistency) |
| **Type Distribution** | 15/20/20/20/25 | Cognitive diversity (not all recall, not all analysis) |
| **Bloom Distribution** | 25%/35%/30%/10% | Cognitive level alignment with T2 standards |
| **Position Distribution** | 20-30% per letter | No answer key patterns (no 4+ consecutive A's) |

**If validation fails:**
- Flag specific questions with feedback (e.g., "DIS = 0.15, target > 0.30")
- Subagent iterates using validation data
- Revalidate and repeat

**If validation passes:**
- Proceed to final question generation with explanations
- Include psychometric metadata in output

### Phase 5: Assembly & Output

Merge all validated questions into final assessment:

1. **Combine all question types** in optimal order (mix across cognitive levels)
2. **Final validation checks**:
   - Position distribution 20-30% per letter
   - No >3 consecutive same-letter answers
   - All Bloom levels represented
   - Calculate KR-20 (overall reliability, should be ≥ 0.70)
3. **Generate assessment**:
   - Markdown version (version control, easy to edit)
   - Include metadata: DIF, DIS, DF, Bloom level for each question
   - Include answer key with rationales
4. **Convert to DOCX** (if requested):
   - Use `/docx` skill: "Create professional exam in DOCX format from markdown assessment"
   - Formats with: header (title, instructions), questions numbered, answer key at end
   - Ready for printing/distribution

---

## Reference Materials for Autonomous Reasoning

Subagents access these materials to reason about MIT-standard assessment design:

| Reference | Path | Purpose |
|-----------|------|---------|
| **Distractor Strategies** | `references/distractor-generation-strategies.md` | Pedagogically sound distractor design for each question type |
| **Academic Rigor Tiers** | `references/academic-rigor-tiers.md` | T1-T4 frameworks for assessment difficulty and grading |
| **Psychometric Standards** | `references/psychometric-standards.md` | DIF/DIS/DF/KR-20 validation metrics and targets |
| **Bloom's Taxonomy** | `references/bloom-taxonomy.md` | Cognitive levels and question type mapping |

Subagents reason through these materials (not follow step-by-step) to generate pedagogically sound assessments that meet validation thresholds.

---

## Quality Standards

### Per-Question (Subagent Responsibility)
- [ ] Stem: Single sentence, ≤25 words, unambiguous
- [ ] Correct answer: ≤15 words, defensible from source
- [ ] Distractors: Plausible (70-90%), distinct, follow strategy
- [ ] Options: Within ±3 words of median length

### Per-10-Questions (Checkpoint)
- [ ] DIF within T2 range (50-65%)
- [ ] DIS > 0.30 (good discrimination)
- [ ] DF ≥ 5% (all distractors plausible)
- [ ] Position trending toward 25% per letter

### Final Validation (100 questions)
- [ ] Position distribution 20-30% per letter
- [ ] No >3 consecutive same-letter answers
- [ ] All types present (15, 20, 20, 20, 25)
- [ ] All Bloom levels present per distribution
- [ ] KR-20 ≥ 0.70 (reliable)
- [ ] No length, position, or specificity bias

## Failure Remediation

| Failure Type | Remediation |
|--------------|-------------|
| Answer imbalance | Swap correct answers to balance |
| Consecutive sequence | Reorder questions or swap answers |
| Missing question type | Generate additional questions of that type |
| Missing Bloom level | Adjust existing or add questions |
| Weak distractors | Rewrite with stronger alternatives |
| Quote in explanation | Paraphrase and add section reference |
| Missing section ref | Add appropriate reference |

---

## Grading Scale (T2)

| Grade | % |
|-------|---|
| A+ | 95-100 |
| A | 90-94 |
| B+ | 85-89 |
| B | 80-84 |
| C | 70-79 |
| F | <70 |

---

## Success Metrics

✅ MIT-Quality Assessment = Pedagogically sound + Technically valid + Unbiased + Well-sourced

After user request identify the correct chapters list and list all lessons in each chapter. The book content is at `apps/learn-app/docs`. THe book contains parts and chapters in each part.