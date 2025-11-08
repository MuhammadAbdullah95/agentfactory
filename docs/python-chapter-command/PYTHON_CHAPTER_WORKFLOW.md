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
- Three-tier teaching structure (Concept → Code → Try With AI → Reasoning)
- Evals-first, spec-first, validation-first methodology
- Python standards (3.14.0+, type hints as core feature, f-strings, security)
- Cognitive load management (2 concepts per lesson, max 5/7/10 by tier)
- Skills proficiency metadata (CEFR A1/A2/B1, Bloom's, DigComp)
- Quality gates (technical, pedagogical, constitutional)
- Cross-chapter coherence patterns
- Assessment and validation frameworks
- Troubleshooting as AI partnership (Rule 6)
- Standardized "Try With AI" format (Rule 7: 4 prompts, Expected outcome)

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
specs/part-4-chapter-${N}/
├── spec.md      (AI-native pedagogy, Python 3.14.0, evals-first, type hints core)
├── plan.md      (4-6 lessons, CEFR A1/A2/B1, Bloom's, DigComp, "Try With AI" format)
└── tasks.md     (implementation checklist, validation tasks, acceptance criteria)
```

**Then**:
```
book-source/docs/04-Part-4-Python-Fundamentals/${N}-[chapter-name]/
├── readme.md         (chapter introduction, learning objectives, prerequisites)
├── 01-[lesson-1].md  (with skills metadata, "Try With AI" section)
├── 02-[lesson-2].md  (with skills metadata, "Try With AI" section)
├── 03-[lesson-3].md  (with skills metadata, "Try With AI" section)
└── 04-[lesson-4].md  (with skills metadata, "Try With AI" section)
```

**Finally**:
```
→ Run technical-reviewer for validation
→ PASS = publication ready
→ FAIL = fix and re-review
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

The `plan.md` file includes skills proficiency metadata (visible to institutional integrators):
```yaml
skills:
  - name: "[Skill Name]"
    proficiency_level: "A1|A2|B1"      # CEFR international standard
    category: "Technical|Conceptual|Soft"
    bloom_level: "Remember|Understand|Apply|Analyze|Evaluate|Create"
    digcomp_area: "[Digital competence framework]"
    measurable_at_this_level: "Student can... [specific, testable behavior]"
```

Each lesson in `*.md` frontmatter includes the same metadata:
```yaml
skills:
  - name: "[Skill]"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can write..."
```

This metadata:
- **Enables institutional accreditation** (CEFR/DigComp alignment)
- **Supports competency-based assessment** (not just test scores)
- **Allows curriculum differentiation** (advanced/remedial paths)
- **Feeds into learning management systems** (institutional integration)
- **Portable credentials** (A1/A2/B1 recognized internationally)

---

## Quality Assurance

### Automated Checks (via /sp.specify, /sp.plan, /sp.tasks)

- ✅ Python 3.14.0 syntax verified (latest stable from https://www.python.org/downloads/)
- ✅ Type hints present in ALL code examples (not optional)
- ✅ "Try With AI" format validated (4 prompts per lesson, Expected outcome required)
- ✅ No security vulnerabilities (input validation, no hardcoded secrets)
- ✅ Cognitive load validated (2 concepts per lesson, ≤5/7/10 by tier)
- ✅ Pedagogical structure aligned (Concept → Code → Try With AI → Reasoning)
- ✅ Learning objectives SMART + measurable (testable behaviors)
- ✅ Skills proficiency metadata complete (CEFR A1/A2/B1 progression)

### Manual Reviews (via technical-reviewer) - MANDATORY

**When**: After all lessons completed by lesson-writer

**Command**:
```bash
/invoke technical-reviewer chapter-${N}
```

**Validation Checklist**:
- ✅ Code examples tested in Python 3.14.0 (not 3.13)
- ✅ Type hints present in ALL code examples (not optional)
- ✅ "Try With AI" format: exactly 4 prompts per lesson with "Expected outcome"
- ✅ No dual-path gatekeeping comments or sections
- ✅ Reading level appropriate (Grade 7+ with explanations)
- ✅ Lesson duration realistic (20-35 minutes)
- ✅ Cross-references functional
- ✅ Chapter coherence (concept thread, scaffolding progression)
- ✅ Metadata consistency (no contradictions between sections)
- ✅ Constitutional alignment (AI-native pedagogy, specification-first, validation-first)

**Result**: PASS/FAIL verdict
- **PASS**: Publication ready
- **FAIL**: Return to implementation phase, fix issues, re-review

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

### 3. AI-Native Pedagogy (AIDD)
Students learn through:
- **Concept understanding** (not syntax memorization)
- **Specification-first thinking** (define intent before code)
- **Colearning with AI** (Claude Code/Gemini CLI as reasoning partners)
- **Type hints as specifications** (`: str` documents intent in code)
- **"Try With AI" dialogues** (exactly 4 prompts per lesson)
- **Troubleshooting as AI partnership** (ask "What does this mean?" not memorize errors)
- **Validation skills** (specification → code → validation)

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
- Each chapter created differently ❌
- No consistent pedagogical structure ❌
- REPL-first mentality ❌
- Syntax memorization focus ❌
- Institutional metadata missing ❌
- Quality inconsistent ❌
- No technical review workflow ❌
- Type hints optional/advanced ❌

### After (Systematic - v2.0)
- All chapters follow master template ✅
- Consistent "Concept → Code → Try With AI → Reasoning" structure ✅
- Specification-first mentality (not REPL-first) ✅
- Concept understanding focus ✅
- CEFR A1/A2/B1 + Bloom's + DigComp metadata built-in ✅
- Quality gates automated (spec → plan → tasks) ✅
- **Technical review MANDATORY after implementation** ✅
- **Type hints CORE (not optional)** from Chapter 13 onwards ✅
- **Python 3.14.0** as standard ✅
- **Rule 6 & 7** (AI partnership + standardized format) ✅

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

## Key Session Learnings (Nov 8, 2025)

From real-world execution of Chapter 13:

1. **Technical reviews catch contradictions early**
   - Metadata comment contradicted chapter goals
   - Found before multi-lesson implementation
   - Prevented inconsistent publication

2. **Type hints are core, not optional**
   - Modern Python treats hints as specifications
   - Essential for AIDD and AI-native thinking
   - Integrate from Chapter 13 onwards

3. **"Try With AI" format matters**
   - Consistency across book improves student experience
   - 4-prompt structure is pedagogically sound
   - Expected outcome validates understanding

4. **Python 3.14.0 is the standard**
   - Latest stable release from official source
   - Future-proofs curriculum
   - No version inconsistencies

---

**Status**: ✅ Production Ready (v2.0 - REVIEWED)
**Version**: 2.0.0
**Last Updated**: 2025-11-08
**Technical Review Integration**: Mandatory workflow added
**Alignment**: 100% with Constitution v3.0.2

