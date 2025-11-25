---
sidebar_position: 6
title: "Skill Creation + Polish"
chapter: 15
lesson: 6
duration_minutes: 45

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 3"
layer_progression: "L3 intelligence design - skill formalization from capstone patterns"
layer_3_intelligence: "P+Q+P skill creation from recurring AI tool patterns"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Pattern Recognition for Skill Creation"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify patterns that appear 2+ times with 5+ decision points across features"

  - name: "P+Q+P Skill File Design"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can write a complete skill file with Persona, Questions (5+), Principles (5+), and Example Application"

  - name: "Skill Application Testing"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can apply skill Questions and Principles to new scenario and evaluate completeness"

  - name: "AI Tool Pattern Abstraction"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can abstract AI tool usage patterns into reusable frameworks"

learning_objectives:
  - objective: "Identify recurring patterns from Features 1-4 worth formalizing as skills"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student lists 2-3 patterns with occurrence count and decision points"

  - objective: "Create complete P+Q+P skill file following the framework"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Skill file includes Persona, 5+ Questions, 5+ Principles, Example Application"

  - objective: "Apply skills to new scenario and evaluate transferability"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student answers skill Questions for new scenario and identifies any gaps"

cognitive_load:
  new_concepts: 4
  reused_concepts: 6
  assessment: "4 new concepts (P+Q+P framework, Persona definition, skill Questions, skill Principles) + 6 reused from F1-F4 (pattern recognition, structured prompting, validation, quality gates) within B1 limit ✓"

differentiation:
  extension_for_advanced: "Create third skill; analyze cross-domain applicability"
  remedial_for_struggling: "Focus on one skill; use provided Structured AI Prompting example as template"

generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "3.0.0"
---

# Skill Creation + Polish

You've built four features. Each feature built faster than the last—not because the features were simpler, but because you reused patterns. The structured prompting approach from F1 carried to F2, F3, and F4. The validation checklist you created once got used four times. The quality gate workflow became automatic.

This is intelligence accumulation. Patterns that repeat 2+ times with 5+ decision points become **skills**. Skills encode knowledge so future projects benefit immediately—no re-discovering, no re-deciding.

Now you'll formalize those patterns into actual reusable skills using the **P+Q+P Framework: Persona + Questions + Principles**.

## Identify Recurring Patterns

Review your four features. Find the patterns you used multiple times.

**Feature 1: Personal Brand Profiler**
- How did you structure the `/sp.specify` specification?
- How did the `/sp.plan` → `/sp.tasks` decomposition work?
- How did `/sp.implement` checkpoints guide the workflow?

**Feature 2: Market Intelligence Scanner**
- How did you adapt `/sp.specify` for a different tool (NotebookLM)?
- How did the checkpoint pattern transfer from F1?
- How did you connect F1 output to F2 specification inputs?

**Feature 3: Content Strategy Generator**
- How did you specify multi-input dependencies in `/sp.specify`?
- How did `/sp.implement` validate pillar-to-trend connections?
- How did you iterate when the output was incomplete?

**Feature 4: Action Dashboard**
- How did you specify three-input dependencies in `/sp.specify`?
- How did `/sp.implement` handle redundancy checking?
- How did the SDD-RI workflow accelerate compared to F1?

**List your top 2-3 patterns** (things you solved multiple times):

1. _________________ (appeared in features: _____)
2. _________________ (appeared in features: _____)
3. _________________ (appeared in features: _____)

**Common patterns to look for:**

| Pattern | Where It Appeared | Decision Points |
|---------|------------------|-----------------|
| **SDD-RI Workflow** | F1, F2, F3, F4 | /sp.specify → /sp.plan → /sp.tasks → /sp.implement |
| **Specification Structure** | F1, F2, F3, F4 | Intent, Input Data, Tool, Constraints, Success Evals, Non-Goals |
| **Checkpoint Review** | F1, F2, F3, F4 | Phase boundaries, validation, decision points |
| **Multi-Input Dependencies** | F3, F4 | Specifying upstream outputs as inputs |
| **Pipeline Data Flow** | F1→F2, F2→F3, F3→F4 | Output format matches next input needs |

## Create Your First Skill: SDD-RI Specification Design

This pattern appeared in all four features. You used `/sp.specify` to create structured specifications with Intent, Constraints, and Success Evals.

### Step 1: Create the File

```bash
mkdir -p .claude/skills
touch .claude/skills/sdd-ri-specification.md
```

### Step 2: Write the Skill

Open the file and add this content (customize the Example Application with YOUR actual prompts):

```markdown
# SDD-RI Specification Design Skill

## Persona

You are a specification architect who designs feature specifications using the SDD-RI workflow. You value clear intent, testable success criteria, and explicit constraints. You use `/sp.specify` to create specifications that guide the entire implementation workflow.

## Questions (Ask Before Specifying)

1. **What is the intent of this feature?** (What problem does it solve? What does success look like?)

2. **What input data does this feature need?** (Raw data, upstream feature outputs, external sources?)

3. **What tool will execute this feature?** (Gemini App, NotebookLM, Claude Code, other?)

4. **What constraints must be respected?** (Tool limitations, format requirements, time bounds?)

5. **What are the testable success evals?** (How will you verify the output is correct and complete?)

## Principles (Apply During Specification)

- **Intent Before Implementation**: Start with WHY this feature exists, not HOW it will work. "/sp.specify" captures intent; "/sp.plan" captures implementation.

- **Make Success Evals Testable**: "Output contains 3+ strengths" is testable. "Output is useful" is not. Each success eval should be verifiable in "/sp.implement" validation phase.

- **Specify Input Dependencies Explicitly**: If F3 depends on F1 + F2 outputs, list them with file paths. The agent needs to verify inputs exist before proceeding.

- **Include Non-Goals**: What this feature explicitly does NOT do. Prevents scope creep during implementation.

- **Match Tool Constraints**: Specification must respect the tool's capabilities. "Browser-based, no API" for Gemini App. "Multi-source synthesis" for NotebookLM.

## Example Application

When building Feature 3 (Content Strategy Generator), I used this pattern:

**Question 1 answered**: Intent = Synthesize F1 brand + F2 market into content strategy that connects my strengths to market trends

**Question 2 answered**: Inputs = F1 brand analysis (specs/brand-profiler/output/f1-brand-analysis.md), F2 market brief (specs/market-scanner/output/f2-market-brief.md)

**Question 3 answered**: Tool = Gemini App (gemini.google.com)

**Question 4 answered**: Constraints = Browser-based, content pillars MUST connect F1 strengths to F2 trends, structured markdown output

**Question 5 answered**: Success evals = 3 pillars, each connecting F1 strength to F2 trend, 10+ topics, weekly schedule, first week actions

**Principles applied**:
- Intent captured the WHY (connect strengths to market)
- Success evals are testable ("each pillar connects F1 strength to F2 trend")
- Input dependencies explicit (file paths to F1, F2 outputs)
- Non-goals defined (no automated publishing, no audience research)
- Tool constraints respected (Gemini App, browser-based)

**Result**: Specification that guided /sp.plan → /sp.tasks → /sp.implement with clear validation criteria.
```

**Save the file.**

### Step 3: Validate Your Skill

Check your skill file:

- [ ] Persona describes WHO applies this skill and WHAT they value
- [ ] 5 Questions are specific (not generic "what do you need?")
- [ ] 5 Principles explain WHY they matter (not just WHAT to do)
- [ ] Example Application shows YOUR actual work from F1-F4
- [ ] Example answers each Question and applies each Principle

## Create Your Second Skill: Checkpoint-Driven Implementation

This pattern appeared in all four features. You used `/sp.implement` checkpoints to review progress at phase boundaries before proceeding.

### Step 1: Create the File

```bash
touch .claude/skills/checkpoint-implementation.md
```

### Step 2: Write the Skill

```markdown
# Checkpoint-Driven Implementation Skill

## Persona

You are an implementation specialist who uses checkpoints to ensure quality at every phase boundary. You value explicit review points, clear decision criteria, and systematic validation. You use `/sp.implement` to execute tasks with human-in-the-loop checkpoints.

## Questions (Ask Before Implementing)

1. **What phases does this implementation have?** (List the major phases from tasks.md)

2. **What must be true at each checkpoint?** (What validates that a phase is complete?)

3. **What decisions need human input?** (Where should the workflow pause for review?)

4. **What happens if a checkpoint fails?** (Retry? Fix? Go back to previous phase?)

5. **How do I continue after approval?** (What's the prompt to resume /sp.implement?)

## Principles (Apply During Implementation)

- **Pause at Phase Boundaries**: Every phase ends with a CHECKPOINT. Don't auto-continue; wait for explicit approval before proceeding.

- **State What Was Done**: At each checkpoint, report what tasks completed and what was produced. "Phase 1 complete: 3 sources gathered, sources-list.md created."

- **Ask for Decision**: Present clear options: "✅ Proceed to Phase 2" or "❌ Need to fix [issue]". Don't assume the answer.

- **Handle Failures Explicitly**: If validation fails, explain what failed and suggest a fix. "Quality gate FAILED: Missing evidence citation. Suggested fix: Ask AI to revise."

- **Continue Cleanly**: When resuming, state context: "Continue /sp.implement - Execute Phase 2" so the agent knows where you are in the workflow.

## Example Application

When building Feature 2 (Market Intelligence Scanner), I used checkpoints:

**Question 1 answered**: Phases = Source Gathering → NotebookLM Setup → Query Execution → Synthesis → Validation → Save

**Question 2 answered**:
- CHECKPOINT 1: 3+ sources gathered, sources-list.md created
- CHECKPOINT 2: All sources uploaded and "Ready" in NotebookLM
- CHECKPOINT 3: All 4 queries executed, responses copied
- CHECKPOINT 4: All quality gates pass
- CHECKPOINT 5: Output saved to correct location

**Question 3 answered**: Human reviews sources before upload (CHECKPOINT 1), reviews query responses before validation (CHECKPOINT 3)

**Question 4 answered**: If CHECKPOINT 3 fails (incomplete response), re-query NotebookLM with more specific prompt

**Question 5 answered**: "Continue /sp.implement - Execute Phase [N] ([Phase Name])"

**Principles applied**:
- Paused at every phase boundary (5 checkpoints total)
- Stated what was done ("4 industry trends found with citations")
- Asked for decision ("✅ All sources ready. Proceed to Phase 2?")
- Handled failure explicitly ("Trend #2 missing citation. Ask NotebookLM to revise.")
- Continued cleanly ("Continue /sp.implement - Execute Phase 3 (Query Execution)")

**Result**: Systematic implementation with human review at every critical point, no skipped validation.
```

**Save the file.**

## Test Your Skills Against a New Scenario

Test whether your skills are actually reusable. Apply them to a NEW scenario—not another feature in your Personal BI system.

**New Scenario: Job Application Intelligence System**

You're building a system to research job postings and prepare targeted applications:
- Feature A: Job Posting Analyzer (extract requirements from posting)
- Feature B: Company Researcher (gather company info from public sources)
- Feature C: Application Generator (create tailored cover letter + resume highlights)
- Feature D: Interview Prep Dashboard (combine A + B + C into prep material)

### Apply Skill 1: SDD-RI Specification Design

Answer your skill's 5 Questions for Feature A (Job Posting Analyzer):

**Q1: What is the intent of this feature?**
Your answer: _________________________________________________

**Q2: What input data does this feature need?**
Your answer: _________________________________________________

**Q3: What tool will execute this feature?**
Your answer: _________________________________________________

**Q4: What constraints must be respected?**
Your answer: _________________________________________________

**Q5: What are the testable success evals?**
Your answer: _________________________________________________

**Did your Questions cover the design decisions for Feature A?** If not, what Question is missing?

### Apply Skill 2: Checkpoint-Driven Implementation

Answer your skill's 5 Questions for Feature D (Interview Prep Dashboard):

**Q1: What phases does this implementation have?**
Your answer: _________________________________________________

**Q2: What must be true at each checkpoint?**
Your answer: _________________________________________________

**Q3: What decisions need human input?**
Your answer: _________________________________________________

**Q4: What happens if a checkpoint fails?**
Your answer: _________________________________________________

**Q5: How do I continue after approval?**
Your answer: _________________________________________________

**Did your Questions cover the design decisions for Feature D?** If not, what Question is missing?

## Identify Skill Gaps

If you found design decisions NOT answered by your skills:

**Gap in Skill 1**: _________________________________________________

**How to fix**: Add a Question or Principle to cover this case

**Gap in Skill 2**: _________________________________________________

**How to fix**: Add a Question or Principle to cover this case

**Update your skill files** if you found gaps.

## Optional: Create a Third Skill

Look back at Features 1-4. Did you solve any other patterns repeatedly?

**Candidates:**

| Pattern | Where Used | Worth Formalizing? |
|---------|------------|-------------------|
| **Multi-Input Dependencies** | F3, F4 | Yes if you build more pipeline features |
| **Quality Gate Validation** | All features | Yes if 5+ decision points |
| **Tool-Specific Prompting** | F1 (Gemini), F2 (NotebookLM) | Yes if reusing these tools |
| **Constitution-Based Decision Making** | /sp.constitution, all features | Yes if you'll write more constitutions |

**Create a third skill only if:**
- Pattern appeared in 2+ features
- Pattern has 5+ decision points
- Future projects will use this pattern

If all three are YES, create `.claude/skills/[pattern-name].md` using the same P+Q+P template.

## Save Your Skills

Verify your skills are saved:

```bash
ls .claude/skills/
```

You should see:
- `sdd-ri-specification.md`
- `checkpoint-implementation.md`
- (optional third skill)

These skills are now part of your project. They can be referenced in future work or copied to new projects.

## Try With AI

Get feedback on your skills:

**Prompt 1: Skill Quality Check**

In Gemini App:

```
Review this skill definition for reusability:

[Paste your sdd-ri-specification.md content]

Questions:
1. Are the 5 Questions specific enough to guide real design decisions?
2. Are the 5 Principles actionable (not vague advice)?
3. Would someone with no context be able to apply this skill?
4. What's missing that would make this skill more complete?
```

**Observe**: Gemini may identify vague questions or principles that need tightening.

**Prompt 2: Transferability Test**

```
I created these skills from a Personal BI project using the SDD-RI workflow:

Skill 1: SDD-RI Specification Design
- Guides how to write /sp.specify specifications with Intent, Constraints, Success Evals

Skill 2: Checkpoint-Driven Implementation
- Guides how to use /sp.implement checkpoints for systematic validation

Now I want to use these skills for a completely different project: Planning a vacation using AI tools.

Which skill transfers directly? Which needs adaptation? What skill am I missing for vacation planning?
```

**Observe**: Skills that transfer unchanged prove high reusability. Skills that need heavy adaptation may be too project-specific.

---

**Skill creation complete.** You now have reusable skills that encode your intelligence accumulation from this capstone.

Start Lesson 7: Ship + Retrospective. You'll finalize your outputs and measure your total acceleration.
