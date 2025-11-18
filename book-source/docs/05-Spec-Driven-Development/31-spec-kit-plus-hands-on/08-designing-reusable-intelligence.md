---
title: "Designing Reusable Intelligence from SDD Workflows"
chapter: 31
lesson: 8
duration_minutes: 150

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Pattern Recognition for Intelligence Encoding"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify which workflow patterns from Lessons 1-7 justify encoding as reusable intelligence (frequency, complexity, organizational value)"

  - name: "Skill Design Using Persona + Questions + Principles"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can design a skill with Persona (cognitive stance), Questions (reasoning prompts), and Principles (decision frameworks)"

  - name: "Subagent Persona Definition"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can define a subagent persona for specification review with 5+ decision points"

  - name: "Intelligence Component File Structure"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create intelligence component file following .claude/skills/ structure with proper metadata"

  - name: "Reuse vs Create Decision Framework"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can determine when to reuse existing intelligence vs create new component based on context specificity and decision complexity"

learning_objectives:
  - objective: "Identify recurring patterns from Lessons 1-7 that justify intelligence encoding (constitution creation, specification review, edge case analysis)"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Pattern identification exercise with frequency and complexity analysis"

  - objective: "Design a skill using Persona + Questions + Principles pattern for specification quality review"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Skill component completeness and reasoning activation quality"

  - objective: "Define a subagent persona for specification auditing with autonomous decision-making capability"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Subagent persona clarity and decision point enumeration (5+ required)"

  - objective: "Create intelligence component file with proper structure and metadata"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "File structure validation against .claude/skills/ standards"

  - objective: "Apply reuse vs create framework to determine when to build new intelligence"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Decision justification for 3 example scenarios"

cognitive_load:
  new_concepts: 5
  assessment: "5 new concepts (Pattern recognition criteria, Persona design, Question formulation, Principle articulation, Reuse judgment) within B1 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Create second skill for plan quality validation; design subagent for cross-phase consistency checking; build intelligence library with 3+ components"
  remedial_for_struggling: "Use provided skill template with examples; focus on single skill creation before subagent design; defer file structure details to later practice"

# Generation metadata
generated_by: "content-implementer v3.0.0"
source_spec: "specs/10-chapter-31-redesign/spec.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "manual-implementation"
version: "1.0.0"
---

# Designing Reusable Intelligence from SDD Workflows

You've completed the SDD workflow (Lessons 1-7): Constitution → Specify → Clarify → Plan → Tasks → Implement. You can now build projects using specification-first methodology.

But here's what separates AI-native developers from AI-assisted developers: **The ability to transform workflow patterns into reusable intelligence.**

In this lesson, you'll learn the paradigm shift from Chapter 30's whitepaper: **Reusable Intelligence** is the new unit of value, not reusable code. You'll extract patterns from Lessons 1-7 and encode them as skills and subagents—creating an intelligence library that compounds with every project.

You'll transform tacit knowledge into explicit, reusable components—the next evolution beyond workflow execution.

---

## From Workflow Execution to Intelligence Accumulation

### What You've Built So Far

**Lessons 1-7 taught you process**:
- How to create Constitutions (quality standards)
- How to write specifications (intent documentation)
- How to clarify ambiguities (specification gaps)
- How to generate plans (implementation strategy)
- How to decompose tasks (work breakdown)
- How to orchestrate implementation (AI-driven execution)

**What's missing**: Reusable components that make the next project 10x faster.

### The Paradigm Shift: Specs + Intelligence > Code

From the SDD-RI whitepaper you read in Chapter 30:

> **Traditional Development**: Code libraries are the units of reuse. Developers share functions, classes, frameworks.
>
> **AI-Native Development**: Specifications, Agent Architectures, and Skills are the units of reuse. Developers share intelligence.

**In practice**:
- **Project 1**: You write constitution, specification, run workflow (10 hours)
- **Project 2** (without intelligence): You write new constitution, new spec, run workflow (9 hours—slightly faster)
- **Project 2** (with intelligence): You invoke `spec-review` skill, reuse constitution template, orchestrate with subagent (3 hours—7x faster)

**The difference**: Accumulated intelligence compounds. Every pattern you encode accelerates future work.

---

## Identifying Patterns Worth Encoding

Not every workflow step justifies creating reusable intelligence. Use this decision framework:

### Decision Framework: When to Encode Intelligence

Ask three questions about the workflow pattern:

**1. Frequency**: Will this pattern recur across 3+ projects?
- ✅ YES: Specification quality review (every project needs specs)
- ✅ YES: Edge case identification (every feature has edge cases)
- ❌ NO: Calculator-specific math operations (one-off for this project)

**2. Complexity**: Does this pattern involve 5+ decision points?
- ✅ YES: Specification review (scope, clarity, SMART criteria, edge cases, constraints, non-goals = 6+ decisions)
- ❌ NO: Running `/sp.specify` command (1 decision: invoke or not)

**3. Organizational Value**: Will encoding this pattern improve team capability?
- ✅ YES: Constitution templates (standardizes team quality)
- ✅ YES: Specification review skills (catches common errors)
- ❌ NO: Personal file organization preferences (individual style)

**Rule**: If 2+ answers are YES → Encode as reusable intelligence

### Pattern Analysis from Lessons 1-7

Let's analyze what you learned:

| **Pattern** | **Frequency** | **Complexity** | **Org Value** | **Encode?** |
|-------------|---------------|----------------|---------------|-------------|
| Constitution creation | ✅ Every project | ✅ 7+ decisions | ✅ Team standards | **YES** |
| Specification review | ✅ Every feature | ✅ 6+ decisions | ✅ Quality gate | **YES** |
| Edge case identification | ✅ Every feature | ✅ 5+ decisions | ✅ Bug prevention | **YES** |
| `/sp.specify` invocation | ✅ Every feature | ❌ 1 decision | ❌ Trivial | NO |
| Git branch creation | ✅ Every feature | ❌ 1-2 decisions | ❌ Standard practice | NO |
| SMART criteria validation | ✅ Every spec | ✅ 5 decisions | ✅ Clarity enforcement | **YES** |

**Candidates for intelligence encoding**:
1. **Constitution Template Skill**: Guide for creating project-specific quality standards
2. **Specification Review Skill**: Quality audit checklist for specs
3. **Edge Case Analysis Skill**: Framework for identifying edge cases
4. **SMART Criteria Validator Subagent**: Autonomous acceptance criteria review

**In this lesson, you'll build**: Specification Review Skill + SMART Validator Subagent foundation

---

## Skill Design: Persona + Questions + Principles

From Chapter 30's whitepaper and the constitution research paper, you learned that effective intelligence uses the **Persona + Questions + Principles (P+Q+P)** pattern.

This pattern **activates reasoning mode** (context-specific thinking) instead of **prediction mode** (pattern retrieval).

### The P+Q+P Pattern

**Persona**: Establishes cognitive stance (how to think about the problem)
- Not: "You are an expert" (vague, triggers generic responses)
- But: "Think like a specification reviewer who audits for SMART criteria the way a code reviewer checks for security vulnerabilities—systematically, with checklists, identifying gaps before they cause failures"

**Questions**: Forces context-specific analysis (what to analyze)
- Not: "Is this specification good?" (yes/no, no reasoning)
- But: "Are acceptance criteria Specific (exact metrics)? Measurable (objective tests)? Achievable (implementable)? Relevant (map to user needs)? For each criterion, identify vague language and suggest SMART alternatives."

**Principles**: Provides decision frameworks (how to make judgments)
- Not: "Use best practices" (meaningless without definition)
- But: "SMART Criteria Framework: Specific (no ambiguous terms like 'good', 'fast', 'secure'), Measurable (numeric thresholds or objective tests), Achievable (implementable with available resources), Relevant (directly serves user need from spec), Time-bound (if applicable)"

### Building Your First Skill: Specification Review

**Step 1: Define the Persona**

Open your AI companion and collaborate:

```
I want to create a skill for reviewing specification quality.
The skill should help me audit specs for SMART criteria, edge case coverage,
and Constitution alignment.

Let's design the persona together. I'm thinking:
"Think like a specification reviewer who audits for completeness..."

Help me finish this persona. What cognitive stance activates the right
kind of analytical thinking for specification review?
```

**What Good Looks Like**:

```markdown
## Persona

You are a specification quality auditor who thinks about requirements
the way a security engineer thinks about attack surfaces:

- Systematically checking for gaps
- Identifying what's NOT specified (implicit assumptions)
- Validating that acceptance criteria are testable
- Ensuring edge cases are documented before implementation

Your goal: Catch specification ambiguities that would cause
implementation failures or misalignment with user needs.
```

**Step 2: Formulate Analytical Questions**

```
Now let's design the questions this skill should ask when reviewing a spec.

Questions should force context-specific analysis, not yes/no answers.

Here are my ideas:
1. "Are acceptance criteria SMART or vague?"
2. "What edge cases are missing?"

Help me expand this to 5-7 questions that activate thorough analysis.
```

**What Good Looks Like**:

```markdown
## Analytical Questions

Before approving a specification, analyze:

1. **SMART Criteria Validation**:
   - Are acceptance criteria Specific (exact metrics, no vague terms)?
   - Are they Measurable (objective tests, not subjective judgment)?
   - Are they Achievable (implementable with available resources)?
   - Are they Relevant (directly serve user needs from spec overview)?

2. **Edge Case Coverage**:
   - What boundary conditions exist (min/max values, empty inputs, nulls)?
   - What error states can occur (network failures, invalid inputs, race conditions)?
   - What assumptions could be violated (type mismatches, concurrent access)?

3. **Scope Clarity**:
   - Are in-scope features clearly listed?
   - Are out-of-scope items explicitly documented?
   - Can implementer distinguish included vs excluded features?

4. **Constitution Alignment**:
   - Does spec respect project quality standards?
   - Are required constraints (type hints, testing, documentation) specified?
   - Does spec reference relevant constitution sections?

5. **Completeness Check**:
   - Does spec have Overview, Scope, Requirements, Acceptance Criteria, Constraints?
   - Can another developer implement from this spec without guessing?
   - Are success metrics defined (how to validate implementation)?
```

**Step 3: Articulate Decision Principles**

```
Finally, let's define the decision frameworks that guide the review.

These should be concrete rules, not abstract advice.

Example: "Vague Language Detection: Flag any acceptance criterion
containing 'good', 'fast', 'secure', 'clean', 'professional' without
numeric thresholds or objective tests."

Help me create 5 principle statements for specification review.
```

**What Good Looks Like**:

```markdown
## Decision Principles

Apply these frameworks when reviewing specifications:

1. **SMART Criteria Enforcement**:
   - Specific: No ambiguous language ("works well" → "returns results in <100ms")
   - Measurable: Numeric thresholds or objective tests ("fast" → "p95 latency <200ms")
   - Achievable: Implementable with stated resources/constraints
   - Relevant: Maps to user need or business goal from overview
   - Time-bound: If applicable (not always required)

2. **Edge Case Minimum Standard**:
   - Every data input: Document min/max/empty/null behavior
   - Every operation: Document error states and handling
   - Every assumption: Document what happens if assumption violated
   - Minimum 3 edge cases per feature

3. **Explicit Over Implicit**:
   - Non-goals section required (what we're NOT building)
   - Assumptions section required (what we're taking for granted)
   - If spec doesn't say it, implementation shouldn't assume it

4. **Testability Requirement**:
   - Every acceptance criterion must map to automated test
   - If criterion can't be tested objectively → it's too vague
   - Success metrics define "done" (not implementation completion)

5. **Constitution as Contract**:
   - Spec cannot contradict constitution constraints
   - If spec requires something constitution forbids → escalate conflict
   - Reference specific constitution sections for requirements
```

---

## Creating Your Skill File

Now let's turn your P+Q+P components into a reusable skill file.

### Step 1: Create the Skill Directory

```bash
# In your calculator-project directory
mkdir -p .claude/skills
```

### Step 2: Create the Skill File

```bash
# Create specification-review skill
touch .claude/skills/specification-review.md
```

### Step 3: Write the Skill Content

Open `.claude/skills/specification-review.md` and collaborate with your AI:

```
I want to create a skill file for specification review using the
P+Q+P pattern we designed.

The file should follow the standard skill structure:
- Metadata header (name, version, description, when to use)
- Persona section
- Questions section
- Principles section
- Usage examples
- Self-check validation

Here's what we designed:
[Paste your Persona + Questions + Principles from above]

Help me format this as a complete skill file.
```

**What Good Looks Like**:

```markdown
# Skill: Specification Quality Review

**Version**: 1.0.0
**Created**: 2025-01-18
**Last Updated**: 2025-01-18
**Category**: Quality Assurance
**Complexity**: Medium (5-7 decision points)

## Description

This skill provides a systematic framework for reviewing specification quality
before proceeding to planning and implementation. It validates SMART criteria,
edge case coverage, scope clarity, and Constitution alignment.

## When to Use This Skill

**Apply this skill when**:
- Reviewing specifications before `/sp.plan` invocation
- Auditing specs written by team members
- Validating that acceptance criteria are testable
- Checking Constitution alignment before implementation

**Skip this skill when**:
- Specification is still in draft phase (use informal review first)
- Prototyping without formal spec (exploratory work)
- Specifications are auto-generated by validated tools

---

## Persona

You are a specification quality auditor who thinks about requirements
the way a security engineer thinks about attack surfaces:

- Systematically checking for gaps
- Identifying what's NOT specified (implicit assumptions)
- Validating that acceptance criteria are testable
- Ensuring edge cases are documented before implementation

Your goal: Catch specification ambiguities that would cause
implementation failures or misalignment with user needs.

---

## Analytical Questions

Before approving a specification, analyze:

1. **SMART Criteria Validation**:
   - Are acceptance criteria Specific (exact metrics, no vague terms)?
   - Are they Measurable (objective tests, not subjective judgment)?
   - Are they Achievable (implementable with available resources)?
   - Are they Relevant (directly serve user needs from spec overview)?

2. **Edge Case Coverage**:
   - What boundary conditions exist (min/max values, empty inputs, nulls)?
   - What error states can occur (network failures, invalid inputs, race conditions)?
   - What assumptions could be violated (type mismatches, concurrent access)?

3. **Scope Clarity**:
   - Are in-scope features clearly listed?
   - Are out-of-scope items explicitly documented?
   - Can implementer distinguish included vs excluded features?

4. **Constitution Alignment**:
   - Does spec respect project quality standards?
   - Are required constraints (type hints, testing, documentation) specified?
   - Does spec reference relevant constitution sections?

5. **Completeness Check**:
   - Does spec have Overview, Scope, Requirements, Acceptance Criteria, Constraints?
   - Can another developer implement from this spec without guessing?
   - Are success metrics defined (how to validate implementation)?

---

## Decision Principles

Apply these frameworks when reviewing specifications:

1. **SMART Criteria Enforcement**:
   - Specific: No ambiguous language ("works well" → "returns results in <100ms")
   - Measurable: Numeric thresholds or objective tests ("fast" → "p95 latency <200ms")
   - Achievable: Implementable with stated resources/constraints
   - Relevant: Maps to user need or business goal from overview
   - Time-bound: If applicable (not always required)

2. **Edge Case Minimum Standard**:
   - Every data input: Document min/max/empty/null behavior
   - Every operation: Document error states and handling
   - Every assumption: Document what happens if assumption violated
   - Minimum 3 edge cases per feature

3. **Explicit Over Implicit**:
   - Non-goals section required (what we're NOT building)
   - Assumptions section required (what we're taking for granted)
   - If spec doesn't say it, implementation shouldn't assume it

4. **Testability Requirement**:
   - Every acceptance criterion must map to automated test
   - If criterion can't be tested objectively → it's too vague
   - Success metrics define "done" (not implementation completion)

5. **Constitution as Contract**:
   - Spec cannot contradict constitution constraints
   - If spec requires something constitution forbids → escalate conflict
   - Reference specific constitution sections for requirements

---

## Usage Example

**Scenario**: Reviewing calculator specification before planning

**Invocation**:
```
I've written a calculator specification in specs/calculator/spec.md.

Please apply the Specification Quality Review skill to audit:
1. SMART criteria compliance
2. Edge case coverage
3. Scope clarity
4. Constitution alignment
5. Overall completeness

Provide specific findings with line references and suggested improvements.
```

**Expected Output**:
```
Specification Review: specs/calculator/spec.md

✅ SMART Criteria: Mostly compliant
   - Line 45: "accurate results" → vague, suggest "accurate to 6 decimal places"
   - Line 67: "handles errors" → vague, suggest "raises ValueError with descriptive message"

⚠️ Edge Case Coverage: Incomplete
   - Missing: power(0, 0) handling (mathematically undefined)
   - Missing: Very large exponents (memory/time limits)
   - Present: Division by zero ✓

✅ Scope Clarity: Well-defined
   - In-scope: 5 operations clearly listed
   - Out-of-scope: Scientific functions, UI, history tracking

✅ Constitution Alignment: Compliant
   - References Type Hints requirement ✓
   - References Testing requirement ✓
   - References Documentation requirement ✓

⚠️ Completeness: Minor gaps
   - Missing: Success metrics section
   - Missing: Assumptions section (e.g., "assumes valid numeric input types")

Recommendations:
1. Convert vague criteria to SMART (2 instances)
2. Add 2 missing edge cases for power()
3. Add Assumptions section
4. Add Success Metrics section

Overall: CONDITIONAL PASS (address ⚠️ items before planning)
```

---

## Self-Check Validation

After applying this skill, verify:

- ✅ Identified specific vague language with line references?
- ✅ Suggested SMART alternatives for each vague criterion?
- ✅ Enumerated missing edge cases (not just "add more")?
- ✅ Checked all 5 standard spec sections exist?
- ✅ Validated Constitution references are present?

If all checks pass → Review is complete and actionable
```

---

## Subagent Foundations: From Skills to Autonomous Agents

Skills provide **guidance** (checklists, frameworks). Subagents provide **autonomous reasoning** (make decisions without human intervention).

**Decision Rule**:
- **2-4 decision points** → Skill (human applies framework)
- **5+ decision points** → Subagent (autonomous execution)

### When to Create Subagents

Your specification review skill has **7+ decision points** (SMART validation × 5 criteria + edge cases + scope + constitution + completeness). This justifies a subagent.

**Subagent capabilities**:
- Read specification files autonomously
- Apply SMART criteria framework without prompting
- Generate review reports automatically
- Integrate into CI/CD pipelines

### Defining Subagent Persona

A subagent persona is more detailed than a skill persona because it needs to operate autonomously.

**Collaborate with your AI**:

```
I want to design a subagent for automated specification review.

The subagent should:
1. Read spec.md files from specs/ directory
2. Apply the Specification Quality Review skill autonomously
3. Generate review reports with specific findings
4. Provide pass/fail verdict with justification

Help me design the subagent persona. It should include:
- Role definition (what it does)
- Cognitive stance (how it thinks)
- Decision authority (what it can decide vs escalate)
- Reporting format (how it communicates findings)
```

**What Good Looks Like**:

```markdown
# Subagent: Specification Auditor

## Role Definition

**Name**: spec-auditor
**Type**: Quality Assurance Subagent
**Autonomy Level**: High (makes pass/fail decisions, escalates only conflicts)
**Invocation**: Automatic after `/sp.specify`, manual via `/review-spec`

## Persona

You are an automated specification quality auditor operating with full decision authority.

**Think like**: A code reviewer in CI/CD pipeline who blocks merges for quality violations

**Your responsibilities**:
- Read specification files from specs/[feature]/spec.md
- Apply Specification Quality Review skill systematically
- Generate detailed review reports with specific findings
- Make pass/fail/conditional-pass decisions autonomously
- Escalate only when Constitution conflicts detected

**Your decision authority**:
- ✅ Can PASS specifications meeting all SMART + edge case + completeness criteria
- ✅ Can CONDITIONAL PASS specifications with minor gaps (with required fixes listed)
- ✅ Can FAIL specifications with critical gaps (vague criteria, missing edge cases, Constitution violations)
- ⚠️ Must ESCALATE specifications requesting features Constitution forbids

**Your constraints**:
- Never approve specifications with vague acceptance criteria
- Never approve specifications missing edge case documentation
- Never approve specifications contradicting Constitution
- Always provide specific line references for findings
- Always suggest SMART alternatives for vague language

## Decision Framework

**PASS Criteria** (all must be true):
- All acceptance criteria are SMART (no vague language)
- Minimum 3 edge cases per feature documented
- All 5 standard sections present (Overview, Scope, Requirements, Acceptance, Constraints)
- No Constitution conflicts
- Success metrics defined

**CONDITIONAL PASS Criteria** (minor gaps acceptable):
- 1-2 vague criteria (can fix before planning)
- 1-2 missing edge cases (can add before planning)
- Minor completeness gaps (Assumptions section missing, etc.)

**FAIL Criteria** (any true):
- 3+ vague acceptance criteria
- Critical edge cases missing (e.g., division by zero not documented)
- Major sections missing (no Acceptance Criteria section)
- Constitution conflicts detected

**ESCALATE Criteria** (any true):
- Specification requests feature Constitution explicitly forbids
- Ambiguity about whether feature violates Constitution
- Specification quality falls outside defined pass/fail criteria

## Reporting Format

Generate reports in this structure:

```
=== SPECIFICATION AUDIT REPORT ===
File: specs/[feature]/spec.md
Date: [timestamp]
Auditor: spec-auditor v1.0.0

--- SMART CRITERIA VALIDATION ---
Status: [PASS | PARTIAL | FAIL]
Findings:
  - Line XX: "[vague phrase]" → Suggest: "[SMART alternative]"
  - Line YY: ✓ SMART compliant

--- EDGE CASE COVERAGE ---
Status: [PASS | PARTIAL | FAIL]
Findings:
  - Missing: [specific edge case]
  - Present: [documented edge case] ✓

--- SCOPE CLARITY ---
Status: [PASS | PARTIAL | FAIL]
Findings: [...]

--- CONSTITUTION ALIGNMENT ---
Status: [PASS | FAIL | ESCALATE]
Findings: [...]

--- COMPLETENESS ---
Status: [PASS | PARTIAL | FAIL]
Findings: [...]

=== VERDICT ===
Overall: [PASS | CONDITIONAL PASS | FAIL | ESCALATE]

Required Actions (if conditional/fail):
1. [Specific fix with line reference]
2. [Specific fix with line reference]

Recommendations (optional improvements):
- [Nice-to-have suggestion]

=== END REPORT ===
```

## Usage Integration

**Automatic Invocation** (recommended):
```bash
# In .claude/workflow-config.yml
post_specify_hooks:
  - name: spec-auditor
    trigger: after_specify
    action: audit_spec
    blocking: true  # Prevents /sp.plan until PASS or CONDITIONAL PASS
```

**Manual Invocation**:
```bash
# Review existing spec
/review-spec calculator

# AI invokes spec-auditor subagent
# Generates audit report
# Provides verdict + required actions
```

## Self-Monitoring

After each audit, validate:
- ✅ Checked all 5 audit dimensions?
- ✅ Provided specific line references for findings?
- ✅ Suggested SMART alternatives for vague language?
- ✅ Made clear pass/fail/conditional decision?
- ✅ Listed required actions for conditional/fail verdicts?

If any check fails → Audit is incomplete, regenerate with full analysis
```

---

## Building Your Intelligence Library

You've now created:
1. **Specification Review Skill** (guidance framework, 7 decision points)
2. **Spec Auditor Subagent Foundation** (autonomous reviewer, high decision authority)

### Organizing Your Intelligence

**Standard directory structure**:
```
calculator-project/
├── .claude/
│   ├── skills/
│   │   ├── specification-review.md    ← Your skill
│   │   ├── edge-case-analysis.md      ← Future skill
│   │   └── constitution-template.md   ← Future skill
│   ├── subagents/
│   │   ├── spec-auditor.md            ← Your subagent
│   │   └── plan-validator.md          ← Future subagent
│   └── workflow-config.yml            ← Automation rules
├── specs/
│   └── calculator/
│       └── spec.md
└── README.md
```

### Intelligence Reuse Strategy

**Skill reuse** (apply guidance to new contexts):
```
# Project 2: REST API
I'm reviewing an API specification.

Apply the Specification Quality Review skill from
.claude/skills/specification-review.md

Context: This is a REST API spec, not a library.
Adapt edge case analysis for HTTP contexts (404s, timeouts, malformed JSON).
```

**Subagent reuse** (autonomous application):
```
# Project 2: REST API
/review-spec user-authentication

# AI automatically applies spec-auditor subagent
# Generates audit report adapted to API context
```

**Intelligence composition** (combine multiple components):
```
# Project 3: CLI tool
Apply these skills in sequence:
1. Constitution Template → generate project quality standards
2. Specification Review → audit CLI tool spec
3. Edge Case Analysis → identify CLI-specific edge cases

Then invoke spec-auditor subagent for final validation.
```

---

## Validation: Does Your Intelligence Activate Reasoning?

Bad intelligence triggers **prediction mode** (generic responses). Good intelligence triggers **reasoning mode** (context-specific analysis).

### Test Your Specification Review Skill

**Ask your AI companion**:

```
Apply the Specification Quality Review skill to this vague acceptance criterion:

"Calculator should handle errors gracefully"

Walk me through your analysis using the Persona, Questions, and Principles
from the skill.
```

**Good response (reasoning mode)**:

```
Applying Specification Quality Review skill:

PERSONA: Thinking like a specification auditor checking for testability gaps...

QUESTIONS ANALYSIS:
1. SMART Criteria Validation:
   - Specific? NO - "gracefully" is undefined
   - Measurable? NO - "handle errors" has no objective test
   - Achievable? UNKNOWN - no error types specified
   - Relevant? UNCLEAR - which errors? all operations?

2. Edge Case Coverage:
   - What error states? (division by zero, type mismatch, overflow?)
   - What does "gracefully" mean? (raise exception, return None, log?)

PRINCIPLES APPLICATION:
- SMART Criteria Enforcement: "gracefully" is vague language (like "good", "fast")
- Testability Requirement: Cannot write automated test for "graceful"

SMART ALTERNATIVE:
"Calculator raises ValueError with descriptive message for:
 - Division by zero: 'Cannot divide by zero'
 - Invalid types: 'Inputs must be int or float'
 - Overflow: 'Result exceeds maximum float value'"

This version is:
- Specific: Exact error type (ValueError), exact messages
- Measurable: Can test with pytest.raises(ValueError, match="Cannot divide")
- Achievable: Standard Python exception handling
- Relevant: Covers error handling requirement from overview
```

**Bad response (prediction mode)**:

```
The criterion "handle errors gracefully" is too vague.
Make it more specific like "handle errors properly."
```

**If you get prediction mode responses**: Your skill's Persona/Questions/Principles need strengthening. Revise with more concrete frameworks.

---

## Common Mistakes

### Mistake 1: Creating Skills for Trivial Decisions

**The Error**: Creating a skill for "How to run /sp.specify command"

**Why It's Wrong**: 1 decision point (invoke or not) doesn't justify intelligence encoding. Skills are for 2-4+ decision workflows.

**The Fix**: Only encode patterns with frequency + complexity + organizational value.

### Mistake 2: Vague Personas

**The Error**: "You are an expert specification reviewer"

**Why It's Wrong**: "Expert" is generic, triggers prediction mode ("use best practices").

**The Fix**: Specific cognitive stance with analogy:
- ❌ "You are an expert"
- ✅ "Think like a security engineer checking attack surfaces—systematically, with checklists, identifying gaps"

### Mistake 3: Yes/No Questions

**The Error**: "Is this specification good?"

**Why It's Wrong**: Binary questions don't activate analysis. AI responds "yes" or "no" without reasoning.

**The Fix**: Open-ended analytical questions:
- ❌ "Is this specification good?"
- ✅ "Which acceptance criteria are vague vs SMART? For each vague criterion, what specific measurable alternative would make it testable?"

### Mistake 4: Over-Specific Skills

**The Error**: Creating "Calculator-Specification-Review" skill that only works for calculators

**Why It's Wrong**: Intelligence should be reusable across projects. Over-specificity reduces organizational value.

**The Fix**: Generalize patterns:
- ❌ "Calculator-Specification-Review"
- ✅ "Specification-Quality-Review" (works for APIs, CLIs, libraries, etc.)

---

## Try With AI: Create Your Intelligence Library

Now let's build your complete intelligence library for the SDD workflow.

### Setup

**Tool**: Claude Code (or your configured AI orchestrator)

**Context**: Your calculator project with completed SDD workflow (Lessons 1-7)

**Goal**: Create 2 reusable intelligence components

### Exercise 1: Create Specification Review Skill

**Prompt**:

```
I want to create a reusable skill for specification quality review.

The skill should use the Persona + Questions + Principles pattern to guide
systematic review of specifications for:
- SMART criteria compliance
- Edge case coverage
- Scope clarity
- Constitution alignment
- Completeness

Create a skill file following this structure:
1. Metadata header (name, version, when to use)
2. Persona section (cognitive stance with analogy)
3. Analytical Questions (5-7 context-specific questions)
4. Decision Principles (5 concrete frameworks)
5. Usage Example (scenario + expected output)
6. Self-Check Validation

Save to .claude/skills/specification-review.md
```

**Expected Outcome**: AI generates complete skill file with:
- Clear persona using specification auditor analogy
- 5-7 analytical questions covering SMART/edge cases/scope/constitution/completeness
- 5 decision principles with concrete criteria
- Usage example showing invocation + expected review output
- Self-check validation criteria

**Validation**: Ask AI to apply the skill to your calculator spec and verify it generates context-specific analysis (not generic "looks good").

### Exercise 2: Design Spec Auditor Subagent Foundation

**Prompt**:

```
I want to design a subagent for automated specification auditing.

The subagent should:
- Operate autonomously (no human prompting per review)
- Apply Specification Quality Review skill systematically
- Make pass/fail/conditional-pass decisions
- Generate structured audit reports
- Integrate into post-specify workflow hooks

Design the subagent persona including:
1. Role definition (autonomy level, decision authority)
2. Cognitive stance (how it thinks about auditing)
3. Decision framework (pass/conditional/fail/escalate criteria)
4. Reporting format (structured output template)
5. Self-monitoring checklist

Save to .claude/subagents/spec-auditor.md
```

**Expected Outcome**: AI generates subagent foundation with:
- Role definition specifying high autonomy + decision authority
- Persona adapted from skill but enhanced for autonomous operation
- Clear pass/conditional/fail/escalate criteria with thresholds
- Structured report template with specific sections
- Self-monitoring checklist for audit completeness

**Validation**: Ask AI to explain the difference between the skill (guidance for humans) and subagent (autonomous executor) for the same specification review task.

### Exercise 3: Test Intelligence Reuse

**Prompt**:

```
I'm starting a new project: A REST API for user authentication.

I want to reuse the intelligence I created for the calculator project.

Apply the Specification Quality Review skill to audit this acceptance criterion:

"API should return proper status codes"

Use the Persona + Questions + Principles pattern from
.claude/skills/specification-review.md

Show me how the skill adapts to API context vs library context.
```

**Expected Outcome**: AI applies skill framework to API context:
- Identifies "proper" as vague language (same as library context)
- Asks API-specific questions (which endpoints? which status codes? error cases?)
- Suggests SMART alternative: "API returns 200 OK for success, 400 Bad Request for invalid input, 401 Unauthorized for auth failures, 500 Internal Server Error for server exceptions"
- Demonstrates intelligence reuse across different project types

---

## What You've Accomplished

You've transformed workflow knowledge into reusable intelligence components:

✅ **Pattern Recognition**: Identified which workflows justify intelligence encoding (frequency + complexity + value)

✅ **Skill Design**: Created Specification Review skill using Persona + Questions + Principles pattern

✅ **Subagent Foundation**: Defined Spec Auditor subagent for autonomous specification review

✅ **Component Structure**: Built intelligence files following `.claude/skills/` and `.claude/subagents/` standards

✅ **Reuse Framework**: Applied intelligence to new contexts (API vs library)

**Most importantly**: You've learned the paradigm shift from AI-assisted (run commands) to AI-native (accumulate intelligence).

**Bridge to Chapter 32**: You now have an intelligence library. Chapter 32 teaches you to orchestrate these components into multi-agent workflows—the final piece of SDD-RI methodology.

**The compounding effect begins now**: Every future project reuses and extends your intelligence library, making you exponentially faster.

---

## Next Steps

**Immediate practice**:
1. Apply your Specification Review skill to 2 more projects (different domains)
2. Create 1 additional skill (Constitution Template or Edge Case Analysis)
3. Extend your Spec Auditor subagent with automation hooks

**Prepare for Chapter 32**:
- Review your accumulated intelligence library
- Identify which components you'll orchestrate together
- Think about multi-agent coordination patterns

**Long-term mastery**:
- Build intelligence library with 10+ skills and 5+ subagents
- Create organization-wide intelligence repository
- Contribute to open-source intelligence libraries

You've graduated from workflow executor to intelligence architect. Welcome to AI-native development. 🚀
