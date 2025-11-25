---
sidebar_position: 2
title: "Feature 1: Personal Brand Profiler"
chapter: 15
lesson: 2
duration_minutes: 60

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 4"
layer_progression: "L4 capstone - baseline measurement with full SDD-RI workflow"
layer_4_capstone: "Brand analysis using Gemini App, establishing acceleration baseline"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Feature Specification with /sp.specify"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can use /sp.specify to create structured specification for AI tool feature"

  - name: "Implementation Planning with /sp.plan"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can generate implementation plan from specification"

  - name: "Task Decomposition with /sp.tasks"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can break plan into atomic tasks with checkpoints"

  - name: "AI-Driven Implementation with /sp.implement"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can execute tasks with checkpoint review pattern"

learning_objectives:
  - objective: "Use /sp.specify to create brand analysis specification"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Specification file created with intent, constraints, success evals"

  - objective: "Execute full SDD-RI workflow for Feature 1"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student runs /sp.specify → /sp.plan → /sp.tasks → /sp.implement"

  - objective: "Establish baseline time for intelligence accumulation measurement"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "TIME_TRACKER.md updated with F1 duration"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (/sp.specify, /sp.plan, /sp.tasks, /sp.implement, checkpoint review, baseline measurement) within B1 limit ✓"

differentiation:
  extension_for_advanced: "Add competitive positioning section; refine spec with /sp.clarify"
  remedial_for_struggling: "Use provided specification template exactly; focus on checkpoint review"

generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "4.0.0"
---

# Feature 1: Personal Brand Profiler

**This is your baseline.** You're building Feature 1 using the full SDD-RI workflow: specification → plan → tasks → implement. You'll measure how long this takes—then build Features 2-4 and compare acceleration.

**START YOUR TIMER NOW.** Update TIME_TRACKER.md:

```
F1: Personal Brand Profiler | Start: [current time] | End: | Duration: |
```

## Step 1: Create Your Specification (/sp.specify)

Run the specify command to create your feature specification:

```
/sp.specify

Feature: Personal Brand Profiler

Intent:
Analyze my professional profile using Gemini App to produce a structured brand analysis.
The analysis identifies my core strengths, brand gaps, and positioning opportunities.

Input Data:
- LinkedIn About section (I'll paste this into Gemini)
- GitHub bio
- Portfolio description (if available)
- Target role/industry

Tool: Gemini App (gemini.google.com)

Constraints:
- Must use Gemini App (browser-based, no API)
- Must produce structured markdown output
- Must complete within 60 minutes total

Success Evals:
- Output contains 3+ core strengths
- Each strength includes quoted evidence from my profile
- Output contains 2+ brand gaps
- Output contains positioning statement (1-2 sentences)
- Output contains differentiation opportunities (3-5 items)
- Output contains confidence score (0-100) with reasoning
- Output saved to specs/brand-profiler/output/f1-brand-analysis.md

Non-Goals:
- No automated profile scraping
- No competitor analysis (that's Feature 2)
- No content recommendations (that's Feature 3)
```

**Agent does:**
- Creates `specs/brand-profiler/spec.md` with your specification
- Validates against constitution quality gates
- Confirms intent is clear and success evals are testable

**Verify the specification:**

```bash
cat specs/brand-profiler/spec.md
```

## Step 2: Generate Implementation Plan (/sp.plan)

Run the plan command to generate your implementation strategy:

```
/sp.plan

Context: specs/brand-profiler/spec.md

Generate a plan for implementing the Personal Brand Profiler using Gemini App.

The plan should cover:
1. How to structure the Gemini prompt for best results
2. What sections the output must include
3. How to validate output against quality gates
4. How to save the final output

Tool constraints from constitution:
- Gemini App at gemini.google.com (browser-based)
- No API calls
- Structured markdown output
```

**Agent does:**
- Creates `specs/brand-profiler/plan.md`
- Outlines phases: Prompt Design → Execution → Validation → Save
- References constitution quality gates

**Verify the plan:**

```bash
cat specs/brand-profiler/plan.md
```

## Step 3: Break Into Tasks (/sp.tasks)

Run the tasks command to decompose the plan into atomic work units:

```
/sp.tasks

Context:
- Specification: specs/brand-profiler/spec.md
- Plan: specs/brand-profiler/plan.md

Break down into atomic tasks with checkpoints.
```

**Agent does:**
- Creates `specs/brand-profiler/tasks.md`
- Defines phases with checkpoints
- Each task is small enough to verify independently

**Expected task structure:**

```
Phase 1: Prompt Preparation
├─ Task 1.1: Gather profile data (LinkedIn, GitHub, portfolio)
├─ Task 1.2: Create structured prompt with output requirements
└─ CHECKPOINT 1: Review prompt before sending to Gemini

Phase 2: Gemini Execution
├─ Task 2.1: Open Gemini App and start new conversation
├─ Task 2.2: Paste prompt and submit
├─ Task 2.3: Wait for complete response
└─ CHECKPOINT 2: Review raw Gemini output

Phase 3: Validation
├─ Task 3.1: Count strengths (need 3+)
├─ Task 3.2: Verify each strength has evidence citation
├─ Task 3.3: Count gaps (need 2+)
├─ Task 3.4: Verify positioning statement exists
├─ Task 3.5: Verify differentiation opportunities (need 3-5)
├─ Task 3.6: Verify confidence score with reasoning
└─ CHECKPOINT 3: All quality gates pass?

Phase 4: Save Output
├─ Task 4.1: Create output directory
├─ Task 4.2: Save validated output to f1-brand-analysis.md
└─ CHECKPOINT 4: Feature complete
```

**Verify the tasks:**

```bash
cat specs/brand-profiler/tasks.md
```

## Step 4: Execute Implementation (/sp.implement)

Now execute the tasks with checkpoint review:

```
/sp.implement

Context:
- Specification: specs/brand-profiler/spec.md
- Plan: specs/brand-profiler/plan.md
- Tasks: specs/brand-profiler/tasks.md

Execute Phase 1 (Prompt Preparation) with checkpoint.
```

### Phase 1: Prompt Preparation

**Agent does:**
- Task 1.1: Asks you to provide your profile data
- Task 1.2: Creates structured prompt with your data

**You provide:**

```
Here's my profile data:

## LinkedIn About
[PASTE YOUR LINKEDIN ABOUT HERE]

## GitHub Bio
[PASTE YOUR GITHUB BIO HERE]

## Portfolio Description
[PASTE YOUR PORTFOLIO DESCRIPTION HERE - or "No portfolio"]

## Target Role/Industry
[PASTE YOUR TARGET ROLE/INDUSTRY]
```

**Agent creates prompt:**

The agent will generate a structured prompt like:

```
You are a personal branding expert analyzing a professional's online presence.

## My Profile Data

### LinkedIn About Section:
[Your LinkedIn content]

### GitHub Bio:
[Your GitHub bio]

### Portfolio Description:
[Your portfolio content]

### Target Role/Industry:
[Your target]

## Analysis Request

Analyze this profile data and produce a structured brand analysis. Your output MUST include:

1. **Core Strengths** (minimum 3)
   - For each strength, quote the specific phrase from my profile that demonstrates it
   - Format: "Strength: [strength name] — Evidence: '[exact quote from profile]'"

2. **Brand Gaps** (minimum 2)
   - Areas where my profile is weak or missing information
   - Be specific about what's missing and why it matters

3. **Positioning Statement**
   - One to two sentences that capture my unique professional value
   - This should differentiate me from others in my target industry

4. **Differentiation Opportunities**
   - 3-5 specific ways I could stand out in my target market
   - Based on my existing strengths + market needs

5. **Confidence Score** (0-100)
   - How confident are you in this analysis?
   - Lower if profile data was thin; higher if rich detail was available
   - Include brief reasoning for your score

Format your response as structured markdown with clear headers.
```

**CHECKPOINT 1:** Review the prompt before sending to Gemini.
- Is your profile data complete?
- Are all required output sections listed?
- Is the format clear?

**Your decision:**
- ✅ "Looks good. Proceed to Phase 2."
- ❌ "Need to add more profile data. Let me update."

### Phase 2: Gemini Execution

```
Continue /sp.implement - Execute Phase 2 (Gemini Execution)
```

**Agent instructs:**
- Task 2.1: Open gemini.google.com in your browser
- Task 2.2: Start a new conversation, paste the prompt
- Task 2.3: Wait for complete response (15-30 seconds)

**You do:**
1. Open Gemini App
2. Paste the prepared prompt
3. Send and wait for response
4. Copy Gemini's complete response

**CHECKPOINT 2:** Review Gemini's raw output.
- Did Gemini produce structured markdown?
- Are all 5 sections present?
- Does it look complete?

**Your decision:**
- ✅ "Got complete response. Proceed to Phase 3."
- ❌ "Response incomplete. Need to retry with Gemini."

### Phase 3: Validation

```
Continue /sp.implement - Execute Phase 3 (Validation)

Here's Gemini's response:
[PASTE GEMINI'S COMPLETE RESPONSE]
```

**Agent validates:**
- Task 3.1: Counts strengths (need 3+)
- Task 3.2: Checks each strength for evidence citation
- Task 3.3: Counts gaps (need 2+)
- Task 3.4: Verifies positioning statement
- Task 3.5: Counts differentiation opportunities (need 3-5)
- Task 3.6: Verifies confidence score

**Agent reports:**

```
Validation Results:
✓ 3 core strengths found
✓ All strengths have evidence citations
✓ 2 brand gaps identified
✓ Positioning statement present (2 sentences)
✓ 4 differentiation opportunities listed
✓ Confidence score: 75 with reasoning

All quality gates PASS.
```

**If validation fails:**

```
Validation Results:
✓ 4 core strengths found
✗ Strength #2 missing evidence citation
✓ 2 brand gaps identified
...

Quality gate FAILED: Missing evidence citation.

Suggested fix: Ask Gemini to revise strength #2 to include a specific quote from your profile.
```

**You fix:**

Go back to Gemini and ask:
```
Your analysis is missing evidence citations for strength #2.
Please revise to include a specific quote from my profile that demonstrates this strength.
```

**CHECKPOINT 3:** All quality gates pass?
- ✅ "All gates pass. Proceed to Phase 4."
- ❌ "Need to fix [specific issue]. Retrying validation."

### Phase 4: Save Output

```
Continue /sp.implement - Execute Phase 4 (Save Output)
```

**Agent does:**
- Task 4.1: Creates `specs/brand-profiler/output/` directory
- Task 4.2: Saves validated output to `f1-brand-analysis.md` with header

**Output file format:**

```markdown
# Feature 1: Personal Brand Analysis
Generated: [today's date]
Tool: Gemini App (gemini.google.com)
Workflow: /sp.implement

---

[GEMINI'S VALIDATED RESPONSE]

---

## Quality Gate Verification
- [x] 3+ core strengths with evidence citations
- [x] 2+ brand gaps
- [x] Positioning statement
- [x] 3-5 differentiation opportunities
- [x] Confidence score with reasoning
```

**CHECKPOINT 4:** Feature complete.

```bash
cat specs/brand-profiler/output/f1-brand-analysis.md
```

## Stop Your Timer

Record your end time in TIME_TRACKER.md:

```
F1: Personal Brand Profiler | Start: [time] | End: [current time] | Duration: [calculate] |
```

**Example:** If you started at 2:00 PM and finished at 2:45 PM, duration = 45 minutes.

This is your **baseline**. Feature 4 should take less than 50% of this time.

## Commit Feature 1

```
/sp.git.commit_pr Commit Feature 1 (Personal Brand Profiler) - specification, plan, tasks, and output.
```

## What You Built

You now have:

```
specs/brand-profiler/
├── spec.md              # Feature specification
├── plan.md              # Implementation plan
├── tasks.md             # Atomic tasks with checkpoints
└── output/
    └── f1-brand-analysis.md  # Validated output
```

**Artifacts created by SDD-RI workflow:**
1. **Specification** defining what success looks like
2. **Plan** outlining how to achieve it
3. **Tasks** breaking it into verifiable steps
4. **Output** validated against quality gates

This output feeds Feature 2 (Market Intelligence Scanner). Your strengths and gaps inform what market opportunities to research.

## Pattern Notes

Record in TIME_TRACKER.md:

```
## Pattern Notes - Feature 1
- Workflow: /sp.specify → /sp.plan → /sp.tasks → /sp.implement
- Checkpoint pattern: Review at each phase boundary
- Validation pattern: Check output against quality gates before saving
- Iteration pattern: Ask Gemini to fix specific issues when validation fails
```

**Start Lesson 3: Feature 2 (Market Intelligence Scanner).** Record your F2 start time. You'll use the same SDD-RI workflow with NotebookLM.
