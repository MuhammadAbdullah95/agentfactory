---
sidebar_position: 5
title: "Feature 4: Action Dashboard"
chapter: 15
lesson: 5
duration_minutes: 30

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 4"
layer_progression: "L4 capstone - 50% target proof"
layer_4_capstone: "Four-feature aggregation proving intelligence accumulation"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Feature Specification with /sp.specify"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can use /sp.specify to create structured specification for aggregation feature"

  - name: "Implementation Planning with /sp.plan"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can generate implementation plan for multi-feature aggregation"

  - name: "Task Decomposition with /sp.tasks"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can break aggregation plan into atomic tasks with checkpoints"

  - name: "AI-Driven Implementation with /sp.implement"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can execute dashboard generation tasks with checkpoint review pattern"

learning_objectives:
  - objective: "Use /sp.specify to create dashboard specification with three-input dependencies"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Specification file references F1, F2, and F3 outputs as inputs"

  - objective: "Execute full SDD-RI workflow for Feature 4"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student runs /sp.specify → /sp.plan → /sp.tasks → /sp.implement"

  - objective: "Complete Feature 4 in less than 50% of Feature 1 time"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "TIME_TRACKER.md shows F4 time < 50% of F1 time"

cognitive_load:
  new_concepts: 3
  reused_concepts: 10
  assessment: "3 new concepts (aggregation, priority synthesis, 30/60/90 goals) + 10 reused from F1-F3 (/sp.specify, /sp.plan, /sp.tasks, /sp.implement, quality gates, checkpoint review, Gemini App, pipeline flow, validation, markdown output) within B1 limit ✓"

differentiation:
  extension_for_advanced: "Add weekly review template using /sp.clarify for specification refinement"
  remedial_for_struggling: "Use provided specification template exactly; focus on checkpoint review"

generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "4.0.0"
---

# Feature 4: Action Dashboard

You've built three features:
- **F1**: Brand analysis with strengths, gaps, and positioning
- **F2**: Market intelligence with trends, skills, and opportunities
- **F3**: Content strategy with pillars, topics, and schedule

Now you aggregate them into a single **Action Dashboard**—a unified view with priority actions and time-bound goals.

**This is the acceleration test.** Your target: complete F4 in less than 50% of your F1 time.

**START YOUR TIMER NOW.** Update TIME_TRACKER.md:

```
F4: Action Dashboard | Start: [current time] | End: | Duration: |
```

**Calculate your target:**
```
F1 Duration: _____ minutes
F4 Target (50% of F1): _____ minutes
```

## Step 1: Create Your Specification (/sp.specify)

Run the specify command to create your feature specification:

```
/sp.specify

Feature: Action Dashboard

Intent:
Aggregate all three feature outputs (F1 brand analysis + F2 market brief + F3 content strategy) into a unified action dashboard using Gemini App.
The dashboard synthesizes priority actions and time-bound goals without redundancy.

Input Data:
- F1 brand analysis (specs/brand-profiler/output/f1-brand-analysis.md)
  - Core strengths, brand gaps, positioning statement
- F2 market brief (specs/market-scanner/output/f2-market-brief.md)
  - Industry trends, in-demand skills, opportunity areas
- F3 content strategy (specs/content-strategy/output/f3-content-strategy.md)
  - Content pillars, topic ideas, posting schedule

Tool: Gemini App (gemini.google.com)

Constraints:
- Must use Gemini App (browser-based, no API)
- Dashboard must aggregate WITHOUT redundancy
- Each section must trace to source feature (F1, F2, or F3)
- Must produce structured markdown output

Success Evals:
- Output contains brand summary (from F1)
- Output contains market opportunities (from F2)
- Output contains content calendar (from F3)
- Output contains top 5 priority actions (synthesized from all)
- Output contains 30/60/90 day goals
- No redundancy—each piece of info appears once
- Each section traceable to source feature
- Output saved to specs/action-dashboard/output/f4-action-dashboard.md

Non-Goals:
- No new analysis (aggregation only)
- No interactive dashboard (markdown file)
- No automated tracking or reminders
```

**Agent does:**
- Creates `specs/action-dashboard/spec.md` with your specification
- Validates against constitution quality gates
- Confirms input dependencies (F1, F2, F3) and success evals are testable

**Verify the specification:**

```bash
cat specs/action-dashboard/spec.md
```

## Step 2: Generate Implementation Plan (/sp.plan)

Run the plan command to generate your aggregation strategy:

```
/sp.plan

Context: specs/action-dashboard/spec.md

Generate a plan for implementing the Action Dashboard using Gemini App.

The plan should cover:
1. How to gather and verify F1, F2, F3 outputs
2. What prompt to use for dashboard synthesis
3. How to validate no redundancy
4. How to validate source traceability

Tool constraints from constitution:
- Gemini App at gemini.google.com (browser-based)
- Three-input aggregation (F1 + F2 + F3)
- Structured markdown output
- No redundancy across sections
```

**Agent does:**
- Creates `specs/action-dashboard/plan.md`
- Outlines phases: Input Verification → Dashboard Generation → Redundancy Check → Validation → Save
- References constitution quality gates

**Verify the plan:**

```bash
cat specs/action-dashboard/plan.md
```

## Step 3: Break Into Tasks (/sp.tasks)

Run the tasks command to decompose the plan into atomic work units:

```
/sp.tasks

Context:
- Specification: specs/action-dashboard/spec.md
- Plan: specs/action-dashboard/plan.md

Break down into atomic tasks with checkpoints.
```

**Agent does:**
- Creates `specs/action-dashboard/tasks.md`
- Defines phases with checkpoints
- Each task is small enough to verify independently

**Expected task structure:**

```
Phase 1: Input Verification
├─ Task 1.1: Verify F1 brand analysis exists and is complete
├─ Task 1.2: Verify F2 market brief exists and is complete
├─ Task 1.3: Verify F3 content strategy exists and is complete
└─ CHECKPOINT 1: All three inputs ready for aggregation

Phase 2: Dashboard Generation
├─ Task 2.1: Open Gemini App and start new conversation
├─ Task 2.2: Send aggregation prompt with F1 + F2 + F3 content
├─ Task 2.3: Review dashboard structure for completeness
└─ CHECKPOINT 2: Dashboard contains all required sections

Phase 3: Redundancy Check
├─ Task 3.1: Send redundancy check prompt to Gemini
├─ Task 3.2: Review if any information appears multiple times
├─ Task 3.3: Ask Gemini to revise if redundancy found
└─ CHECKPOINT 3: No redundancy across sections

Phase 4: Validation
├─ Task 4.1: Verify brand summary traces to F1
├─ Task 4.2: Verify market opportunities trace to F2
├─ Task 4.3: Verify content calendar traces to F3
├─ Task 4.4: Verify priority actions are specific
├─ Task 4.5: Verify 30/60/90 goals are measurable
└─ CHECKPOINT 4: All quality gates pass?

Phase 5: Save Output
├─ Task 5.1: Create output directory
├─ Task 5.2: Save validated output to f4-action-dashboard.md
├─ Task 5.3: Add source traceability table
└─ CHECKPOINT 5: Feature complete
```

**Verify the tasks:**

```bash
cat specs/action-dashboard/tasks.md
```

## Step 4: Execute Implementation (/sp.implement)

Now execute the tasks with checkpoint review:

```
/sp.implement

Context:
- Specification: specs/action-dashboard/spec.md
- Plan: specs/action-dashboard/plan.md
- Tasks: specs/action-dashboard/tasks.md

Execute Phase 1 (Input Verification) with checkpoint.
```

### Phase 1: Input Verification

**Agent does:**
- Task 1.1-1.3: Verifies all three feature outputs exist

**Agent reports:**

```
Input Verification:
✓ F1 brand analysis found: specs/brand-profiler/output/f1-brand-analysis.md
  - 3 core strengths identified
  - 2 brand gaps identified
  - Positioning statement present

✓ F2 market brief found: specs/market-scanner/output/f2-market-brief.md
  - 4 industry trends identified
  - In-demand skills present
  - Opportunity areas present

✓ F3 content strategy found: specs/content-strategy/output/f3-content-strategy.md
  - 3 content pillars defined
  - 12 topic ideas generated
  - Weekly schedule present

All inputs ready for aggregation.
```

**CHECKPOINT 1:** All three inputs ready for aggregation.
- ✅ "All inputs verified. Proceed to Phase 2."
- ❌ "Missing [F1/F2/F3]. Need to complete that feature first."

### Phase 2: Dashboard Generation

```
Continue /sp.implement - Execute Phase 2 (Dashboard Generation)
```

**Agent provides aggregation prompt:**

```
You are helping me create a unified action dashboard from my personal BI system outputs.

## Feature 1: Brand Analysis

[Agent pastes your ENTIRE F1 output here]

## Feature 2: Market Brief

[Agent pastes your ENTIRE F2 output here]

## Feature 3: Content Strategy

[Agent pastes your ENTIRE F3 output here]

## Task: Create Action Dashboard

Synthesize these three outputs into a unified action dashboard.

The dashboard MUST include these sections:

### 1. Brand Summary (from F1)
- 1-2 sentence positioning statement
- Top 3 strengths (condensed)
- Top 2 gaps to address

### 2. Market Opportunities (from F2)
- Top 3 trends relevant to my positioning
- Key skills I should highlight
- Best opportunity area for immediate focus

### 3. Content Calendar (from F3)
- 3 content pillars (just names)
- This week's posting schedule
- First content piece to create

### 4. Priority Actions (synthesized from all)
- Top 5 specific actions I should take in the next 7 days
- Each action should trace to F1, F2, or F3 output
- Each action should be completable in 30-60 minutes

### 5. 30/60/90 Day Goals

**30 Days:**
- What should I accomplish by day 30?
- Focus: Foundation building

**60 Days:**
- What should I accomplish by day 60?
- Focus: Visibility and engagement

**90 Days:**
- What should I accomplish by day 90?
- Focus: Measurable results

Format as clean markdown. No redundancy—each piece of information appears once in its most relevant section.
```

**You do:**
1. Open Gemini App
2. Paste the prepared prompt (agent includes all F1/F2/F3 content)
3. Review the generated dashboard

**CHECKPOINT 2:** Dashboard contains all required sections.
- Does each section trace to the correct feature output?
- Are priority actions specific (not vague)?
- Do 30/60/90 goals build logically on each other?

**Your decision:**
- ✅ "Dashboard complete. Proceed to Phase 3."
- ❌ "Missing sections. Need to re-prompt."

### Phase 3: Redundancy Check

```
Continue /sp.implement - Execute Phase 3 (Redundancy Check)
```

**Agent provides redundancy check prompt:**

```
Review the dashboard you just created:

[Agent includes dashboard content]

Redundancy check:
1. Does any information appear in multiple sections?
2. Which sections could be shorter without losing value?
3. Is there any section that doesn't trace clearly to F1, F2, or F3?

If you find redundancy, revise the dashboard to eliminate it.
```

**Agent validates:**
- Information appears only once?
- Each section traceable to source feature?

**If redundancy found:**

```
Redundancy detected:
- "Strategic thinking" mentioned in Brand Summary AND Priority Actions
- Recommend: Keep in Brand Summary, remove from Priority Actions

Ask Gemini to revise:
"Please revise the dashboard to remove the redundant mention of 'strategic thinking' in Priority Actions. It's already covered in Brand Summary."
```

**CHECKPOINT 3:** No redundancy across sections.
- ✅ "No redundancy. Proceed to Phase 4."
- ❌ "Redundancy found. Need to revise."

### Phase 4: Validation

```
Continue /sp.implement - Execute Phase 4 (Validation)

Here is Gemini's final dashboard:

[PASTE DASHBOARD CONTENT]
```

**Agent validates:**

```
Validation Results:
✓ Brand summary traces to F1 (strengths, gaps, positioning)
✓ Market opportunities trace to F2 (trends, skills, opportunities)
✓ Content calendar traces to F3 (pillars, schedule)
✓ 5 priority actions are specific and time-bounded
✓ 30/60/90 goals are measurable
✓ No redundancy detected

All quality gates PASS.
```

**CHECKPOINT 4:** All quality gates pass?
- ✅ "All gates pass. Proceed to Phase 5."
- ❌ "Need to fix [specific issue]. Retrying validation."

### Phase 5: Save Output

```
Continue /sp.implement - Execute Phase 5 (Save Output)
```

**Agent does:**
- Task 5.1: Creates `specs/action-dashboard/output/` directory
- Task 5.2: Saves validated output to `f4-action-dashboard.md` with header
- Task 5.3: Adds source traceability table

**Output file format:**

```markdown
# Personal BI System: Action Dashboard
Generated: [today's date]
Tool: Gemini App (gemini.google.com)
Workflow: /sp.implement
Sources: F1 brand analysis + F2 market brief + F3 content strategy

---

## 1. Brand Summary (from F1)

[Dashboard content from Gemini]

## 2. Market Opportunities (from F2)

[Dashboard content from Gemini]

## 3. Content Calendar (from F3)

[Dashboard content from Gemini]

## 4. Priority Actions

[Dashboard content from Gemini]

## 5. 30/60/90 Day Goals

[Dashboard content from Gemini]

---

## Source Traceability

| Section | Source Feature | File |
|---------|---------------|------|
| Brand Summary | F1 | specs/brand-profiler/output/f1-brand-analysis.md |
| Market Opportunities | F2 | specs/market-scanner/output/f2-market-brief.md |
| Content Calendar | F3 | specs/content-strategy/output/f3-content-strategy.md |
| Priority Actions | F1 + F2 + F3 | Synthesized |
| 30/60/90 Goals | F1 + F2 + F3 | Synthesized |

---

## Quality Gate Verification
- [x] Brand summary traces to F1
- [x] Market opportunities trace to F2
- [x] Content calendar traces to F3
- [x] Priority actions are specific (not vague)
- [x] 30/60/90 goals are measurable
- [x] No redundancy across sections
```

**CHECKPOINT 5:** Feature complete.

```bash
cat specs/action-dashboard/output/f4-action-dashboard.md
```

## Stop Your Timer

Record your end time in TIME_TRACKER.md:

```
F4: Action Dashboard | Start: [time] | End: [current time] | Duration: [calculate] |
```

## The Acceleration Test

Calculate your result:

```
F1 Duration: _____ minutes (baseline)
F4 Duration: _____ minutes
F4 as % of F1: _____ % (calculate: F4_time / F1_time × 100)

Target: < 50%
Your Result: _____ %
```

**Interpretation:**

| Result | Meaning |
|--------|---------|
| **< 50%** | Intelligence accumulation proven. SDD-RI workflow patterns compounded. |
| **50-66%** | Good acceleration. Some overhead from three-input aggregation. |
| **66-80%** | Moderate acceleration. Check if scope crept or inputs needed fixes. |
| **> 80%** | Limited acceleration. Analyze what didn't transfer from F1-F3. |

## Record Your Complete Acceleration Data

Update TIME_TRACKER.md with all four features:

```markdown
# Feature Build Times - Personal BI System

| Feature | Start Time | End Time | Duration (min) | % of F1 |
|---------|------------|----------|----------------|---------|
| F1: Personal Brand Profiler | [time] | [time] | _____ | 100% (baseline) |
| F2: Market Intelligence Scanner | [time] | [time] | _____ | _____% |
| F3: Content Strategy Generator | [time] | [time] | _____ | _____% |
| F4: Action Dashboard | [time] | [time] | _____ | _____% |

## Acceleration Analysis

- F1 baseline: _____ minutes
- F4 actual: _____ minutes
- **F4 vs F1 ratio**: _____% (Target: ≤ 50%)
- **Result**: PASS / NEEDS REVIEW

## What Accelerated F4?

- [ ] /sp.specify structure was familiar (4th time using it)
- [ ] /sp.plan → /sp.tasks decomposition automatic
- [ ] /sp.implement checkpoint pattern second nature
- [ ] Quality gate validation workflow practiced
- [ ] Gemini App prompting patterns from F1/F3
- [ ] [Your observation: __________]

## What Slowed F4 (if applicable)?

- [ ] Aggregating three outputs took time
- [ ] Had to go back and fix F1/F2/F3 outputs
- [ ] Redundancy check required multiple iterations
- [ ] [Your observation: __________]
```

## Commit Feature 4

```
/sp.git.commit_pr Commit Feature 4 (Action Dashboard) - specification, plan, tasks, and output.
```

## What You Built

You now have a complete **Personal AI Business Intelligence System**:

```
personal-bi-system/
├── .specify/memory/
│   └── constitution.md              # Quality standards
├── specs/
│   ├── brand-profiler/              # Feature 1
│   │   ├── spec.md
│   │   ├── plan.md
│   │   ├── tasks.md
│   │   └── output/f1-brand-analysis.md
│   ├── market-scanner/              # Feature 2
│   │   ├── spec.md
│   │   ├── plan.md
│   │   ├── tasks.md
│   │   └── output/f2-market-brief.md
│   ├── content-strategy/            # Feature 3
│   │   ├── spec.md
│   │   ├── plan.md
│   │   ├── tasks.md
│   │   └── output/f3-content-strategy.md
│   └── action-dashboard/            # Feature 4
│       ├── spec.md
│       ├── plan.md
│       ├── tasks.md
│       └── output/f4-action-dashboard.md
└── TIME_TRACKER.md                  # Acceleration measurement
```

**Each feature has proper SDD-RI artifacts:**
1. **Specification** (spec.md) — What success looks like
2. **Plan** (plan.md) — How to achieve it
3. **Tasks** (tasks.md) — Verifiable steps with checkpoints
4. **Output** — Validated against quality gates

**The system:**
1. Analyzes YOUR professional brand (F1)
2. Researches YOUR target market (F2)
3. Generates YOUR content strategy (F3)
4. Produces YOUR action plan (F4)

All built using the same SDD-RI workflow (`/sp.specify` → `/sp.plan` → `/sp.tasks` → `/sp.implement`) with different AI tools.

## Pattern Notes

Record in TIME_TRACKER.md:

```
## Pattern Notes - Feature 4
- Workflow: /sp.specify → /sp.plan → /sp.tasks → /sp.implement (4th time - automatic)
- Aggregation pattern: Three-input specification (F1 + F2 + F3)
- Tool pattern: Gemini App for aggregation (same as F1, F3)
- New element: Redundancy checking and source traceability
- Acceleration: SDD-RI workflow now completely familiar
```

**Feature 4 complete.** You've proven intelligence accumulation by building F4 faster than F1 using the same SDD-RI workflow.

Start Lesson 6: Create reusable skills from the patterns you discovered.
