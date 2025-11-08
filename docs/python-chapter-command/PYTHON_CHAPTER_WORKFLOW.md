# Python Chapter Design Workflow (Complete)

**Status**: ✅ Ready for Production

**Components**:
1. **Master Template** (`.specify/templates/book/PYTHON_CHAPTER_DESIGN_TEMPLATE.md`)
2. **Command Implementation** (`.claude/commands/sp.python-chapter.md`)
3. **This Workflow Guide**

---

## What You Have

### 1. Opinionated Master Template

**File**: `.specify/templates/book/PYTHON_CHAPTER_DESIGN_TEMPLATE.md`

**Contains**:
- Core philosophy (AI-native colearning)
- Three-tier teaching structure (Concept → Code → Think With AI → Reasoning)
- Evals-first, spec-first, validation-first methodology
- Python standards (3.13+, security, type hints progression)
- Cognitive load management (5/7/10 concepts by tier)
- Skills proficiency metadata (CEFR/Bloom's/DigComp)
- Quality gates (technical, pedagogical, constitutional)
- Cross-chapter coherence patterns
- Assessment and validation frameworks

**Why it matters**:
- No ambiguity in chapter design
- Consistent quality across all Python chapters
- Embedded institutional accreditation support
- Aligns with project constitution and book philosophy

---

### 2. Automated Command

**File**: `.claude/commands/sp.python-chapter.md`

**What it does**:
```bash
/sp.python-chapter 12
```

**Workflow**:
1. Parse chapter number (12-29)
2. Ask 3 context questions (existing materials, audience, problems)
3. Auto-run `/sp.specify` (create spec.md with evals-first)
4. User approves
5. Auto-run `/sp.plan` (create plan.md with lessons + skills metadata)
6. User approves
7. Auto-run `/sp.tasks` (create tasks.md with acceptance criteria)
8. User approves
9. Deliver complete specification package

**Output**:
```
specs/part-5-chapter-${N}/
├── spec.md      (AI-native pedagogy, Python 3.13+, evals-aligned)
├── plan.md      (5-6 lessons, CEFR/Bloom's/DigComp, "Try With AI" prompts)
└── tasks.md     (implementation checklist, validation tasks)
```

---

## How to Use

### For Designing a New Chapter

```bash
/sp.python-chapter 14
```

**Interactive flow:**
- System extracts Chapter 14 details (Data Types)
- Asks: Any existing materials?
- Asks: Target audience?
- Asks: Real problems to solve?
- Automatically runs `/sp.specify` with context
- You review and approve spec
- System automatically runs `/sp.plan`
- You review and approve plan
- System automatically runs `/sp.tasks`
- You review and approve tasks
- **Result**: Complete spec package ready for lesson-writer subagent

### For Training Other Orchestrators

**Share**: `.specify/templates/book/PYTHON_CHAPTER_DESIGN_TEMPLATE.md`

It contains everything needed to:
- Understand the philosophy
- Create new chapters consistently
- Review specifications for compliance
- Validate quality gates
- Ensure pedagogical soundness

### For Institutional Integration

The `plan.md` file includes hidden metadata:
```yaml
skills:
  - name: "[Skill Name]"
    proficiency_level: "A1|A2|B1|B2"  # CEFR
    category: "Technical|Conceptual|Soft"
    bloom_level: "Remember|Understand|Apply|Analyze|Evaluate|Create"
    digcomp_area: "[Digital competence framework areas]"
    measurable_at_this_level: "Student can... [specific behavior]"
```

This metadata:
- Enables institutional accreditation alignment
- Supports competency-based grading
- Allows curriculum differentiation
- Feeds into learning management systems

---

## Quality Assurance

### Automated Checks (via /sp.specify, /sp.plan, /sp.tasks)

- ✅ Python 3.13+ syntax verified
- ✅ Type hints correct and helpful
- ✅ No security vulnerabilities
- ✅ Cognitive load validated (≤5/7/10)
- ✅ Pedagogical structure aligned (Concept → Code → Think → Reasoning)
- ✅ Learning objectives SMART + measurable
- ✅ "Try With AI" activities specified

### Manual Reviews (via technical-reviewer)

- ✅ Code examples tested in Python 3.13
- ✅ Type hints work (no syntax errors)
- ✅ Reading level appropriate (Grade 7+ with explanations)
- ✅ Lesson duration 20-35 minutes
- ✅ Cross-references functional
- ✅ Chapter coherence (concept thread, capstone project)

### Constitutional Alignment

- ✅ Spec-first methodology (evals → spec → plan → tasks)
- ✅ Validation-first mindset (tests before code)
- ✅ AI-native philosophy (colearning, not memorization)
- ✅ Book scaffold integration (prerequisites, enables, threading)

---

## Design Principles Embedded in Template

### 1. Evals-First
Define success BEFORE writing specs:
- What can students DO? (skills)
- What will they BUILD? (application)
- How do they COLLABORATE with AI? (partnership)

### 2. Spec-First
Clear specifications enable:
- Consistent chapter quality
- Predictable learning outcomes
- Repeatable implementation
- Institutional alignment

### 3. AI-Native Pedagogy
Students learn through:
- **Concept understanding** (not syntax memorization)
- **Colearning with AI** (dialogue, not REPL)
- **Specification practice** (clarity, not copy-paste)
- **Validation skills** (testing, not hope)

### 4. Accessibility
- Grade 7+ reading level (all terms explained)
- Beginner-friendly (no prerequisites assumed)
- Scaffolded complexity (A1 → A2 → B1)
- Multiple learning modalities (text, code, dialogue)

### 5. Institutional Integration
- CEFR proficiency levels (international recognition)
- Bloom's cognitive taxonomy (learning science)
- DigComp digital competence (EU framework)
- Measurable outcomes (for assessment)

---

## Next Steps

### Immediate Actions

1. **Review the master template**:
   ```
   .specify/templates/book/PYTHON_CHAPTER_DESIGN_TEMPLATE.md
   ```

2. **Test the command**:
   ```bash
   /sp.python-chapter 13
   ```
   Should ask 3 context questions, then auto-execute the full workflow.

3. **Verify output structure**:
   ```
   specs/part-5-chapter-13/
   ├── spec.md (check evals-first structure)
   ├── plan.md (check CEFR/Bloom's metadata)
   └── tasks.md (check acceptance criteria)
   ```

### For All Future Python Chapters (12-29)

Use this workflow:
```bash
/sp.python-chapter ${N}
```

Every chapter will automatically:
- Follow the same pedagogical structure
- Enforce quality gates
- Include institutional metadata
- Align with book philosophy
- Integrate with Spec-Kit Plus workflow

### Training Other Orchestrators

Share:
1. `.specify/templates/book/PYTHON_CHAPTER_DESIGN_TEMPLATE.md` (philosophy + structure)
2. `.claude/commands/sp.python-chapter.md` (execution)
3. This file (workflow overview)

They can then independently create consistent, high-quality Python chapters.

---

## Comparison: Before vs. After

### Before (Ad-Hoc)
- Each chapter created differently
- No consistent pedagogical structure
- REPL-first mentality
- Syntax memorization focus
- Institutional metadata missing
- Quality inconsistent

### After (Systematic)
- All chapters follow master template
- Consistent "Concept → Code → Think → Reasoning" structure
- AI-CLI first (not REPL)
- Concept understanding focus
- CEFR/Bloom's/DigComp metadata built-in
- Quality gates automated

---

## What This Enables

### For Students
- Clear learning path (A1 → A2 → B1 progression)
- AI as thinking partner (not tool)
- Specification practice (fundamental AI-native skill)
- Institutional recognition (CEFR levels)

### For Educators
- Reusable, tested template
- Consistent quality
- Minimal design decisions (follow template)
- Institutional integration ready

### For Institutions
- Competency-based assessment
- International standards alignment (CEFR)
- Learner differentiation support
- Accreditation-ready metadata

### For Authors/Orchestrators
- One command to create complete chapter specs
- No ambiguity in design
- Automatic quality gates
- Scalable to all Python chapters

---

## Files Reference

```
.claude/
├── commands/
│   └── sp.python-chapter.md          ← Automated workflow command
├── templates/
│   └── PYTHON_CHAPTER_DESIGN_TEMPLATE.md  ← Master design template (source of truth)
└── PYTHON_CHAPTER_WORKFLOW.md         ← This file
```

---

## Questions?

**For usage questions**: See `.claude/commands/sp.python-chapter.md` "Usage" section

**For design questions**: See `.specify/templates/book/PYTHON_CHAPTER_DESIGN_TEMPLATE.md`

**For implementation**: Run `/sp.python-chapter ${N}` and follow interactive prompts

---

**Status**: ✅ Production Ready
**Version**: 1.0.0
**Last Updated**: 2025-11-07

