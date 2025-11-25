---
sidebar_position: 4
title: "Feature 3: Content Strategy Generator"
chapter: 15
lesson: 4
duration_minutes: 40

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 4"
layer_progression: "L4 capstone - multi-input synthesis"
layer_4_capstone: "Combining F1 brand analysis + F2 market brief into actionable content plan"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Feature Specification with /sp.specify"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can use /sp.specify to create structured specification for multi-input synthesis feature"

  - name: "Implementation Planning with /sp.plan"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can generate implementation plan for content strategy synthesis"

  - name: "Task Decomposition with /sp.tasks"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can break synthesis plan into atomic tasks with checkpoints"

  - name: "AI-Driven Implementation with /sp.implement"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can execute content generation tasks with checkpoint review pattern"

learning_objectives:
  - objective: "Use /sp.specify to create content strategy specification with multi-input dependencies"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Specification file references F1 and F2 outputs as inputs"

  - objective: "Execute full SDD-RI workflow for Feature 3"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student runs /sp.specify → /sp.plan → /sp.tasks → /sp.implement"

  - objective: "Demonstrate continued acceleration from F1 baseline"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "TIME_TRACKER.md shows F3 < F2 time"

cognitive_load:
  new_concepts: 4
  reused_concepts: 8
  assessment: "4 new concepts (content pillars, topic ideation, posting schedule, format selection) + 8 reused from F1-F2 (/sp.specify, /sp.plan, /sp.tasks, /sp.implement, quality gates, checkpoint review, Gemini App, pipeline flow) within B1 limit ✓"

differentiation:
  extension_for_advanced: "Add audience persona development using /sp.clarify for specification refinement"
  remedial_for_struggling: "Use provided specification template exactly; focus on checkpoint review"

generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "4.0.0"
---

# Feature 3: Content Strategy Generator

You have a brand analysis (F1) and a market intelligence brief (F2). Now you'll combine them to generate an actionable content strategy—specific themes, topics, and a posting schedule tailored to your strengths and market demand.

**This is multi-input synthesis.** You're feeding two complete outputs (F1 + F2) into Gemini App and asking it to produce an integrated strategy. This mirrors how real business intelligence systems work: data flows through a pipeline, each stage adding value.

**START YOUR TIMER NOW.** Update TIME_TRACKER.md:

```
F3: Content Strategy Generator | Start: [current time] | End: | Duration: |
```

## Step 1: Create Your Specification (/sp.specify)

Run the specify command to create your feature specification:

```
/sp.specify

Feature: Content Strategy Generator

Intent:
Synthesize my brand analysis (F1) and market brief (F2) using Gemini App to produce an actionable content strategy.
The strategy connects my personal strengths to market trends through specific content pillars, topics, and a posting schedule.

Input Data:
- F1 brand analysis (specs/brand-profiler/output/f1-brand-analysis.md)
  - Core strengths (3+)
  - Brand gaps (2+)
  - Positioning statement
- F2 market brief (specs/market-scanner/output/f2-market-brief.md)
  - Industry trends (3+)
  - In-demand skills
  - Opportunity areas

Tool: Gemini App (gemini.google.com)

Constraints:
- Must use Gemini App (browser-based, no API)
- Content pillars MUST connect F1 strengths to F2 trends
- Must produce structured markdown output
- Schedule must be realistic for stated time constraints

Success Evals:
- Output contains 3 content pillars
- Each pillar explicitly connects one F1 strength to one F2 trend
- Output contains 10+ topic ideas distributed across pillars
- Output contains weekly posting schedule with time estimates
- Output contains first week action items (5+)
- Output saved to specs/content-strategy/output/f3-content-strategy.md

Non-Goals:
- No automated content publishing
- No audience research (using F2 market data instead)
- No competitor content analysis
```

**Agent does:**
- Creates `specs/content-strategy/spec.md` with your specification
- Validates against constitution quality gates
- Confirms input dependencies (F1, F2) and success evals are testable

**Verify the specification:**

```bash
cat specs/content-strategy/spec.md
```

## Step 2: Generate Implementation Plan (/sp.plan)

Run the plan command to generate your synthesis strategy:

```
/sp.plan

Context: specs/content-strategy/spec.md

Generate a plan for implementing the Content Strategy Generator using Gemini App.

The plan should cover:
1. How to gather and format F1 + F2 inputs
2. What prompts to run for pillars, topics, schedule
3. How to validate pillar-to-trend connections
4. How to validate output against quality gates

Tool constraints from constitution:
- Gemini App at gemini.google.com (browser-based)
- Multi-input synthesis (F1 + F2)
- Structured markdown output
```

**Agent does:**
- Creates `specs/content-strategy/plan.md`
- Outlines phases: Input Gathering → Pillar Generation → Topic Expansion → Schedule Creation → Validation
- References constitution quality gates

**Verify the plan:**

```bash
cat specs/content-strategy/plan.md
```

## Step 3: Break Into Tasks (/sp.tasks)

Run the tasks command to decompose the plan into atomic work units:

```
/sp.tasks

Context:
- Specification: specs/content-strategy/spec.md
- Plan: specs/content-strategy/plan.md

Break down into atomic tasks with checkpoints.
```

**Agent does:**
- Creates `specs/content-strategy/tasks.md`
- Defines phases with checkpoints
- Each task is small enough to verify independently

**Expected task structure:**

```
Phase 1: Input Gathering
├─ Task 1.1: Verify F1 brand analysis exists and is complete
├─ Task 1.2: Verify F2 market brief exists and is complete
├─ Task 1.3: Extract key data (strengths, gaps, positioning, trends, skills)
└─ CHECKPOINT 1: Review inputs before synthesis

Phase 2: Pillar Generation
├─ Task 2.1: Open Gemini App and start new conversation
├─ Task 2.2: Send pillar generation prompt with F1 + F2 data
├─ Task 2.3: Verify each pillar connects F1 strength to F2 trend
├─ Task 2.4: Iterate if connections are weak
└─ CHECKPOINT 2: Review 3 pillars for F1→F2 connections

Phase 3: Topic Expansion
├─ Task 3.1: Send topic generation prompt with 3 pillars
├─ Task 3.2: Verify 10+ topics distributed across pillars
├─ Task 3.3: Verify topics are specific (not generic)
└─ CHECKPOINT 3: Review topic list for quality

Phase 4: Schedule and Actions
├─ Task 4.1: Send schedule generation prompt with time constraints
├─ Task 4.2: Verify schedule is realistic
├─ Task 4.3: Send first week action items prompt
├─ Task 4.4: Verify actions are specific and time-bounded
└─ CHECKPOINT 4: Review schedule and actions

Phase 5: Validation and Save
├─ Task 5.1: Compile all responses into structured strategy
├─ Task 5.2: Verify 3 pillars with F1→F2 connections
├─ Task 5.3: Verify 10+ topics
├─ Task 5.4: Verify realistic schedule
├─ Task 5.5: Verify 5+ first week actions
└─ CHECKPOINT 5: All quality gates pass?

Phase 6: Save Output
├─ Task 6.1: Create output directory
├─ Task 6.2: Save validated output to f3-content-strategy.md
└─ CHECKPOINT 6: Feature complete
```

**Verify the tasks:**

```bash
cat specs/content-strategy/tasks.md
```

## Step 4: Execute Implementation (/sp.implement)

Now execute the tasks with checkpoint review:

```
/sp.implement

Context:
- Specification: specs/content-strategy/spec.md
- Plan: specs/content-strategy/plan.md
- Tasks: specs/content-strategy/tasks.md

Execute Phase 1 (Input Gathering) with checkpoint.
```

### Phase 1: Input Gathering

**Agent does:**
- Task 1.1-1.2: Verifies both F1 and F2 outputs exist
- Task 1.3: Extracts key data for synthesis

**Agent reports:**

```
Input Verification:
✓ F1 brand analysis found: specs/brand-profiler/output/f1-brand-analysis.md
  - 3 core strengths identified
  - 2 brand gaps identified
  - Positioning statement present

✓ F2 market brief found: specs/market-scanner/output/f2-market-brief.md
  - 4 industry trends identified
  - In-demand skills (technical + soft) present
  - Opportunity areas matched to profile

Inputs ready for synthesis.
```

**CHECKPOINT 1:** Review inputs before synthesis.
- Are both F1 and F2 outputs complete?
- Can you identify which F1 strengths might connect to which F2 trends?

**Your decision:**
- ✅ "Inputs look good. Proceed to Phase 2."
- ❌ "F1/F2 incomplete. Need to go back and fix."

### Phase 2: Pillar Generation

```
Continue /sp.implement - Execute Phase 2 (Pillar Generation)
```

**Agent provides pillar generation prompt:**

```
You are a content strategist helping me build a personal brand content strategy.

## My Brand Analysis (from Feature 1)

### Core Strengths:
[Agent pastes your F1 strengths here]

### Brand Gaps:
[Agent pastes your F1 gaps here]

### Positioning Statement:
[Agent pastes your positioning statement]

## Market Intelligence (from Feature 2)

### Industry Trends:
[Agent pastes your F2 trends here]

### In-Demand Skills:
[Agent pastes F2 skills lists]

### Opportunity Areas:
[Agent pastes F2 opportunity areas]

## Task: Generate Content Pillars

Based on my brand strengths and market trends, identify 3 content pillars—themes I should consistently create content around.

For each pillar:
1. **Pillar Name** (3-5 words)
2. **Connection to My Strengths** — Which of my strengths does this leverage?
3. **Connection to Market Trends** — Which trends or skills demand does this address?
4. **Why This Matters** — What value does this content provide to my target audience?
5. **Example Topics** (3 quick examples of what I'd write about)

Format as structured markdown with clear sections for each pillar.
```

**You do:**
1. Open Gemini App
2. Paste the prepared prompt
3. Review the 3 pillars generated

**Agent validates:**
- Does each pillar connect to at least one F1 strength?
- Does each pillar address at least one F2 trend?

**If validation fails:**

```
Pillar 2 doesn't clearly connect to your strengths.

Your F1 strengths are:
1. [Strength 1]
2. [Strength 2]
3. [Strength 3]

Ask Gemini to revise:
"Pillar 2 doesn't connect to my strengths. Please revise to leverage [specific strength] while still addressing the market trend."
```

**CHECKPOINT 2:** Review 3 pillars for F1→F2 connections.
- ✅ "All pillars connect strengths to trends. Proceed to Phase 3."
- ❌ "Pillar [X] weak. Need to iterate."

### Phase 3: Topic Expansion

```
Continue /sp.implement - Execute Phase 3 (Topic Expansion)
```

**Agent provides topic generation prompt:**

```
Based on the 3 content pillars we just defined:

[Agent includes the 3 pillars from Phase 2]

Generate 10-15 specific content topic ideas across these pillars.

For each topic:
1. **Title** — The actual headline/title I'd use
2. **Pillar** — Which of the 3 pillars this belongs to
3. **Format** — Post, article, video, or thread
4. **Hook** — Why would someone click on this? (1 sentence)
5. **Key Takeaway** — What will the reader learn or do? (1 sentence)

Distribute topics roughly evenly across all 3 pillars.

Avoid generic topics like "How to Get Started with X" or "Top 10 Tips for Y".
Make each topic specific to my positioning and the market trends we identified.
```

**Agent validates:**
- 10+ topics generated?
- Topics distributed across all 3 pillars?
- Titles specific (not generic listicles)?

**CHECKPOINT 3:** Review topic list for quality.
- ✅ "10+ specific topics. Proceed to Phase 4."
- ❌ "Only [X] topics / topics too generic. Need to re-prompt."

### Phase 4: Schedule and Actions

```
Continue /sp.implement - Execute Phase 4 (Schedule and Actions)
```

**Agent asks for your constraints:**

```
To generate a realistic schedule, I need your time constraints:

1. How many hours per week can you spend on content creation? [2-4 hours typical]
2. When do you work best for creative tasks? [morning/evening]
3. What's your primary platform? [LinkedIn/Twitter/Blog/YouTube]
```

**You provide:**
```
- 3 hours per week for content
- I work best in mornings
- Primary platform: LinkedIn
```

**Agent provides schedule prompt and first week actions prompt:**

(Schedule prompt with your constraints, then first week actions prompt)

**Agent validates:**
- Schedule realistic for stated hours?
- First week actions specific and time-bounded?
- Total time ≤ 4 hours?

**CHECKPOINT 4:** Review schedule and actions.
- ✅ "Schedule realistic, actions specific. Proceed to Phase 5."
- ❌ "Schedule too aggressive. Need to adjust."

### Phase 5: Validation and Save

```
Continue /sp.implement - Execute Phase 5 (Validation and Save)

Here are all Gemini responses:

## Pillars:
[PASTE PILLAR RESPONSE]

## Topics:
[PASTE TOPIC RESPONSE]

## Schedule:
[PASTE SCHEDULE RESPONSE]

## First Week Actions:
[PASTE ACTIONS RESPONSE]
```

**Agent validates:**

```
Validation Results:
✓ 3 content pillars defined
✓ Pillar 1 connects [Strength] to [Trend]
✓ Pillar 2 connects [Strength] to [Trend]
✓ Pillar 3 connects [Strength] to [Trend]
✓ 12 topic ideas generated
✓ Topics distributed across all pillars
✓ Weekly schedule within 3-hour constraint
✓ 6 first week action items (specific and time-bounded)

All quality gates PASS.
```

**CHECKPOINT 5:** All quality gates pass?
- ✅ "All gates pass. Proceed to Phase 6."
- ❌ "Need to fix [specific issue]. Retrying validation."

### Phase 6: Save Output

```
Continue /sp.implement - Execute Phase 6 (Save Output)
```

**Agent does:**
- Task 6.1: Creates `specs/content-strategy/output/` directory
- Task 6.2: Saves validated output to `f3-content-strategy.md` with header

**Output file format:**

```markdown
# Feature 3: Content Strategy
Generated: [today's date]
Tool: Gemini App (gemini.google.com)
Workflow: /sp.implement
Inputs: F1 brand analysis + F2 market brief

---

## Content Pillars

### Pillar 1: [Name]
- **Strengths Connection**: [which F1 strength]
- **Market Connection**: [which F2 trend]
- **Value Proposition**: [why audience cares]
- **Example Topics**: [3 quick examples]

### Pillar 2: [Name]
[Same structure]

### Pillar 3: [Name]
[Same structure]

---

## Topic Ideas (10+)

| # | Title | Pillar | Format | Hook |
|---|-------|--------|--------|------|
| 1 | [Title] | [Pillar name] | [Format] | [Hook] |
| 2 | [Title] | [Pillar name] | [Format] | [Hook] |
[Continue for all topics]

---

## Weekly Schedule

[Schedule content from Gemini]

### Time Investment Summary
- Total weekly hours: [X]
- Content creation: [X hours]
- Distribution/engagement: [X hours]

---

## First Week Action Items

1. [ ] [Task 1] — [Time] — Output: [What you'll have]
2. [ ] [Task 2] — [Time] — Output: [What you'll have]
3. [ ] [Task 3] — [Time] — Output: [What you'll have]
4. [ ] [Task 4] — [Time] — Output: [What you'll have]
5. [ ] [Task 5] — [Time] — Output: [What you'll have]

---

## Quality Gate Verification
- [x] 3 content pillars defined
- [x] Each pillar connects F1 strength to F2 trend
- [x] 10+ topic ideas generated
- [x] Weekly schedule is realistic
- [x] First week actions are specific
```

**CHECKPOINT 6:** Feature complete.

```bash
cat specs/content-strategy/output/f3-content-strategy.md
```

## Stop Your Timer

Record your end time in TIME_TRACKER.md:

```
F3: Content Strategy Generator | Start: [time] | End: [current time] | Duration: [calculate] |
```

## Measure Continued Acceleration

Compare F3 to F1 and F2:

```
F1 Duration: _____ minutes (baseline)
F2 Duration: _____ minutes
F3 Duration: _____ minutes
F3 as % of F1: _____ % (calculate: F3_time / F1_time × 100)
```

**Interpretation:**
- **< 66%**: Strong acceleration—SDD-RI workflow patterns compounding
- **66-80%**: Good acceleration—synthesis was efficient
- **> 80%**: Check if you over-engineered or had tool issues

**Note what transferred from F1-F2:**
- `/sp.specify` specification structure (now with multi-input dependencies)
- `/sp.plan` → `/sp.tasks` decomposition approach
- `/sp.implement` checkpoint review pattern
- Quality gate validation workflow
- Gemini App prompting patterns (from F1)

## Commit Feature 3

```
/sp.git.commit_pr Commit Feature 3 (Content Strategy Generator) - specification, plan, tasks, and output.
```

## What You Built

You now have:

```
specs/content-strategy/
├── spec.md              # Feature specification (with F1+F2 dependencies)
├── plan.md              # Implementation plan
├── tasks.md             # Atomic tasks with checkpoints
└── output/
    └── f3-content-strategy.md  # Validated output
```

**Artifacts created by SDD-RI workflow:**
1. **Specification** defining multi-input dependencies (F1 + F2)
2. **Plan** outlining synthesis approach
3. **Tasks** breaking it into verifiable steps
4. **Output** validated against quality gates

This output feeds Feature 4 (Action Dashboard). Your content strategy becomes one section of the unified dashboard.

## Pattern Notes

Record in TIME_TRACKER.md:

```
## Pattern Notes - Feature 3
- Workflow: /sp.specify → /sp.plan → /sp.tasks → /sp.implement (same as F1, F2)
- Synthesis pattern: Multi-input specification (F1 + F2 as inputs)
- Tool pattern: Gemini App for content generation (same as F1)
- Acceleration: SDD-RI workflow now automatic, only new element was multi-input synthesis
```

**Start Lesson 5: Feature 4 (Action Dashboard).** Record your F4 start time. This is the acceleration test—F4 should take less than 50% of F1's time.
