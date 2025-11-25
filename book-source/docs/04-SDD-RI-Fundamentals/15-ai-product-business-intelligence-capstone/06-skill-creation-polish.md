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
- How did you structure the prompt for Gemini App?
- How did you validate the output against quality gates?
- What format did you use for the saved output?

**Feature 2: Market Intelligence Scanner**
- How did you structure research queries for NotebookLM?
- How did you ensure sources were properly cited?
- How did you connect F1 output to F2 research focus?

**Feature 3: Content Strategy Generator**
- How did you feed F1 + F2 outputs into a single prompt?
- How did you validate that pillars connected to both sources?
- How did you iterate when the output was incomplete?

**Feature 4: Action Dashboard**
- How did you aggregate three outputs into one view?
- How did you synthesize priority actions from all features?
- How did you eliminate redundancy across sections?

**List your top 2-3 patterns** (things you solved multiple times):

1. _________________ (appeared in features: _____)
2. _________________ (appeared in features: _____)
3. _________________ (appeared in features: _____)

**Common patterns to look for:**

| Pattern | Where It Appeared | Decision Points |
|---------|------------------|-----------------|
| **Structured AI Prompting** | F1, F2, F3, F4 | Format request, specify output, include examples, validate result |
| **Output Validation** | F1, F2, F3, F4 | Checklist against quality gates, iterate on failures |
| **Multi-Source Synthesis** | F3, F4 | Combine inputs, eliminate redundancy, trace to sources |
| **Research with Citations** | F2, (F3) | Upload sources, query for synthesis, verify citations |
| **Pipeline Data Flow** | F1→F2, F2→F3, F3→F4 | Output format matches next input needs |

## Create Your First Skill: Structured AI Prompting

This pattern appeared in all four features. You asked Gemini App (or NotebookLM) for structured output, validated it, and iterated when incomplete.

### Step 1: Create the File

```bash
mkdir -p .claude/skills
touch .claude/skills/structured-ai-prompting.md
```

### Step 2: Write the Skill

Open the file and add this content (customize the Example Application with YOUR actual prompts):

```markdown
# Structured AI Prompting Skill

## Persona

You are an AI prompt engineer who designs prompts that produce structured, validated outputs. You value clarity, specificity, and explicit output formats. You iterate when outputs miss requirements rather than accepting incomplete results.

## Questions (Ask Before Prompting)

1. **What is the exact output format I need?** (JSON, markdown with specific sections, table, etc.)

2. **What input data am I providing?** (What context does the AI need to produce accurate output?)

3. **What are my quality gates?** (How will I know the output is complete and correct?)

4. **What examples of good output can I show?** (Does the AI need a template to follow?)

5. **What iteration approach will I use?** (How will I ask for revisions if output is incomplete?)

## Principles (Apply During Prompting)

- **Specify Output Structure First**: Start the prompt with the exact format you want. "Output as markdown with these sections: [list sections]" or "Return JSON with these fields: [list fields]"

- **Provide Complete Context**: Include all data the AI needs. Don't assume it knows your goals, constraints, or preferences.

- **Define Quality Criteria Explicitly**: Tell the AI what "good" looks like. "Each strength must cite evidence from the profile" is better than "be specific."

- **Request Validation in Output**: Ask the AI to confirm it met requirements. "At the end, list which quality gates this output passes."

- **Plan for Iteration**: Assume the first response won't be perfect. Prepare follow-up prompts: "Revise section X to include Y."

## Example Application

When building Feature 1 (Personal Brand Profiler), I used this pattern:

**Question 1 answered**: Output format = markdown with 5 sections (strengths, gaps, positioning, differentiation, confidence score)

**Question 2 answered**: Input = LinkedIn About, GitHub bio, portfolio description, target role

**Question 3 answered**: Quality gates = 3+ strengths with evidence citations, 2+ gaps, positioning statement

**Question 4 answered**: Example = "Format: Strength: [name] — Evidence: '[exact quote from profile]'"

**Question 5 answered**: Iteration = "Your analysis is missing evidence citations. Please revise strength #2 to include a specific quote."

**Principles applied**:
- Specified output structure at prompt start (5 required sections)
- Provided complete profile data (not just summary)
- Defined quality criteria ("cite specific phrases")
- Requested validation ("include confidence score with reasoning")
- Iterated when citations were missing

**Result**: Structured brand analysis that met constitution quality gates after one iteration.
```

**Save the file.**

### Step 3: Validate Your Skill

Check your skill file:

- [ ] Persona describes WHO applies this skill and WHAT they value
- [ ] 5 Questions are specific (not generic "what do you need?")
- [ ] 5 Principles explain WHY they matter (not just WHAT to do)
- [ ] Example Application shows YOUR actual work from F1-F4
- [ ] Example answers each Question and applies each Principle

## Create Your Second Skill: Multi-Source Synthesis

This pattern appeared in Features 3 and 4. You combined multiple inputs into unified output without redundancy.

### Step 1: Create the File

```bash
touch .claude/skills/multi-source-synthesis.md
```

### Step 2: Write the Skill

```markdown
# Multi-Source Synthesis Skill

## Persona

You are a synthesis specialist who combines multiple information sources into unified outputs. You value source traceability, elimination of redundancy, and clear aggregation. You ensure every piece of output traces to its source.

## Questions (Ask Before Synthesizing)

1. **What sources am I combining?** (List each input and its structure)

2. **What is the unified output structure?** (How should combined information be organized?)

3. **How do I handle overlapping information?** (What appears in multiple sources? Where does it belong in output?)

4. **What traceability do I need?** (Should output cite which source each piece came from?)

5. **What is the synthesis goal?** (Summary? Action items? Recommendations? All of these?)

## Principles (Apply During Synthesis)

- **Map Sources to Sections**: Before synthesizing, decide which source feeds which output section. "F1 → Brand Summary, F2 → Market Opportunities, F3 → Content Calendar"

- **Eliminate Redundancy Explicitly**: If information appears in multiple sources, put it in ONE place. Note in other sections: "See [Section X] for details."

- **Trace Every Claim**: Output should reference where each piece of information came from. "Based on market research (F2), top trends are..."

- **Synthesize, Don't Just Combine**: Good synthesis creates NEW value—insights that weren't in any single source. "Combining brand strengths with market trends reveals opportunity X."

- **Validate Completeness**: After synthesizing, check: "Does this output use ALL sources? Is anything missing? Is anything duplicated?"

## Example Application

When building Feature 4 (Action Dashboard), I synthesized F1, F2, and F3:

**Question 1 answered**:
- F1: Brand analysis (strengths, gaps, positioning)
- F2: Market brief (trends, skills, opportunities)
- F3: Content strategy (pillars, topics, schedule)

**Question 2 answered**: Dashboard with 5 sections: Brand Summary, Market Opportunities, Content Calendar, Priority Actions, 30/60/90 Goals

**Question 3 answered**:
- Overlapping: "Skills" appeared in both F1 (my skills) and F2 (market skills)
- Resolution: Put market skills in "Opportunities" section, my skills in "Brand Summary"

**Question 4 answered**: Each section cites source feature. Traceability table at end.

**Question 5 answered**: Goal = unified action plan with specific next steps

**Principles applied**:
- Mapped: F1→Brand Summary, F2→Market Opportunities, F3→Content Calendar
- Eliminated redundancy: Skills appear once in most relevant section
- Traced claims: "Top 3 trends relevant to my positioning (from F2)"
- Synthesized: Priority actions combine insights from all three features
- Validated: Checked that dashboard uses all outputs, no section duplicates another

**Result**: Unified dashboard that aggregates without redundancy, with source traceability.
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

### Apply Skill 1: Structured AI Prompting

Answer your skill's 5 Questions for Feature A (Job Posting Analyzer):

**Q1: What is the exact output format I need?**
Your answer: _________________________________________________

**Q2: What input data am I providing?**
Your answer: _________________________________________________

**Q3: What are my quality gates?**
Your answer: _________________________________________________

**Q4: What examples of good output can I show?**
Your answer: _________________________________________________

**Q5: What iteration approach will I use?**
Your answer: _________________________________________________

**Did your Questions cover the design decisions for Feature A?** If not, what Question is missing?

### Apply Skill 2: Multi-Source Synthesis

Answer your skill's 5 Questions for Feature D (Interview Prep Dashboard):

**Q1: What sources am I combining?**
Your answer: _________________________________________________

**Q2: What is the unified output structure?**
Your answer: _________________________________________________

**Q3: How do I handle overlapping information?**
Your answer: _________________________________________________

**Q4: What traceability do I need?**
Your answer: _________________________________________________

**Q5: What is the synthesis goal?**
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
| **Quality Gate Validation** | All features | Yes if 5+ decision points |
| **Research Query Design** | F2 (NotebookLM) | Yes if you'll use NotebookLM again |
| **Time Tracking for Acceleration** | All features | Maybe—simpler pattern |
| **Constitution-Based Decision Making** | F1 setup, all validation | Yes if you'll write more constitutions |

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
- `structured-ai-prompting.md`
- `multi-source-synthesis.md`
- (optional third skill)

These skills are now part of your project. They can be referenced in future work or copied to new projects.

## Try With AI

Get feedback on your skills:

**Prompt 1: Skill Quality Check**

In Gemini App:

```
Review this skill definition for reusability:

[Paste your structured-ai-prompting.md content]

Questions:
1. Are the 5 Questions specific enough to guide real design decisions?
2. Are the 5 Principles actionable (not vague advice)?
3. Would someone with no context be able to apply this skill?
4. What's missing that would make this skill more complete?
```

**Observe**: Gemini may identify vague questions or principles that need tightening.

**Prompt 2: Transferability Test**

```
I created these skills from a Personal BI project (brand analysis, market research, content strategy):

Skill 1: Structured AI Prompting
[Brief description]

Skill 2: Multi-Source Synthesis
[Brief description]

Now I want to use these skills for a completely different project: Planning a vacation using AI tools.

Which skill transfers directly? Which needs adaptation? What skill am I missing for vacation planning?
```

**Observe**: Skills that transfer unchanged prove high reusability. Skills that need heavy adaptation may be too project-specific.

---

**Skill creation complete.** You now have reusable skills that encode your intelligence accumulation from this capstone.

Start Lesson 7: Ship + Retrospective. You'll finalize your outputs and measure your total acceleration.
