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
  - name: "Multi-Feature Aggregation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can aggregate outputs from multiple upstream features into unified view"

  - name: "Markdown Dashboard Creation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can structure aggregated content into readable dashboard format"

  - name: "Priority Action Synthesis"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can synthesize priority actions from multiple feature outputs"

  - name: "Intelligence Accumulation Measurement"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can measure and analyze acceleration from F1 baseline to F4 completion"

learning_objectives:
  - objective: "Aggregate F1, F2, and F3 outputs into unified action dashboard"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Dashboard includes brand summary, market opportunities, content calendar, and actions"

  - objective: "Complete Feature 4 in less than 50% of Feature 1 time"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "TIME_TRACKER.md shows F4 time < 50% of F1 time"

  - objective: "Synthesize priority actions from all features"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Top 5 priority actions trace back to specific F1/F2/F3 outputs"

cognitive_load:
  new_concepts: 3
  reused_concepts: 8
  assessment: "3 new concepts (aggregation, priority synthesis, 30/60/90 goals) + 8 reused from F1-F3 (structured prompting, validation, quality gates, Gemini App, time tracking, markdown output, pipeline flow, checklist) within B1 limit ✓"

differentiation:
  extension_for_advanced: "Add weekly review template and progress tracking metrics"
  remedial_for_struggling: "Use provided dashboard template exactly; focus on copy-paste aggregation"

generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "3.0.0"
---

# Feature 4: Action Dashboard

You've built three features:
- **F1**: Brand analysis with strengths, gaps, and positioning
- **F2**: Market intelligence with trends, skills, and opportunities
- **F3**: Content strategy with pillars, topics, and schedule

Now you aggregate them into a single **Action Dashboard**—a unified view with priority actions and time-bound goals.

**This is the acceleration test.** Your target: complete F4 in less than 50% of your F1 time.

**Start your timer.** Record in TIME_TRACKER.md:

```
F4: Action Dashboard | Start: [current time] | End: | Duration: |
```

**Calculate your target:**
```
F1 Duration: _____ minutes
F4 Target (50% of F1): _____ minutes
```

## Review Your Constitution

Open your constitution and check Feature 4's quality gates:

```bash
cat .specify/memory/constitution.md | grep -A 10 "Action Dashboard"
```

**Required outputs:**
- Brand summary (from F1)
- Market opportunities (from F2)
- Content calendar (from F3)
- Priority action items (top 5)
- 30/60/90 day goals

**Quality gate:** Dashboard aggregates all three features without redundancy. Each section traces to source feature.

## Verify All Inputs Exist

You need all three feature outputs ready:

```bash
cat outputs/f1-brand-analysis.md | head -20
cat outputs/f2-market-brief.md | head -20
cat outputs/f3-content-strategy.md | head -20
```

**If any file is missing or incomplete:** Go back and complete that feature before proceeding.

## Open Gemini App

Go to **gemini.google.com** in your browser.

Start a new conversation for Feature 4.

## Generate the Dashboard

You'll ask Gemini to synthesize all three outputs into a unified dashboard.

**Copy this prompt and paste your actual content:**

```
You are helping me create a unified action dashboard from my personal BI system outputs.

## Feature 1: Brand Analysis

[Paste your ENTIRE f1-brand-analysis.md content here]

## Feature 2: Market Brief

[Paste your ENTIRE f2-market-brief.md content here]

## Feature 3: Content Strategy

[Paste your ENTIRE f3-content-strategy.md content here]

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

**Review the response:**
- Does each section trace to the correct feature output?
- Are priority actions specific (not vague)?
- Do 30/60/90 goals build logically on each other?

## Validate No Redundancy

The quality gate says "no redundancy." Check:

```
Ask Gemini:

Review the dashboard you just created:

[Paste the dashboard]

Redundancy check:
1. Does any information appear in multiple sections?
2. Which sections could be shorter without losing value?
3. Is there any section that doesn't trace clearly to F1, F2, or F3?

If you find redundancy, revise the dashboard to eliminate it.
```

**If Gemini finds redundancy:** Ask it to revise and remove duplicate information.

## Create the Dashboard File

Create the output file:

```bash
touch outputs/f4-action-dashboard.md
```

Copy Gemini's response and add a header:

```markdown
# Personal BI System: Action Dashboard
Generated: [today's date]
Tool: Gemini App (gemini.google.com)
Sources: F1 brand analysis + F2 market brief + F3 content strategy

---

[PASTE GEMINI'S DASHBOARD OUTPUT HERE]

---

## Source Traceability

| Section | Source Feature | File |
|---------|---------------|------|
| Brand Summary | F1 | outputs/f1-brand-analysis.md |
| Market Opportunities | F2 | outputs/f2-market-brief.md |
| Content Calendar | F3 | outputs/f3-content-strategy.md |
| Priority Actions | F1 + F2 + F3 | Synthesized |
| 30/60/90 Goals | F1 + F2 + F3 | Synthesized |

---

## Quality Gate Verification

- [ ] Brand summary traces to F1? ✓
- [ ] Market opportunities trace to F2? ✓
- [ ] Content calendar traces to F3? ✓
- [ ] Priority actions are specific (not vague)? ✓
- [ ] 30/60/90 goals are measurable? ✓
- [ ] No redundancy across sections? ✓
```

**Verify the file:**

```bash
cat outputs/f4-action-dashboard.md
```

## Validate Against Quality Gates

Check your dashboard against the constitution:

**Checklist:**

- [ ] **Brand summary from F1?** Does it include positioning, strengths, gaps?
- [ ] **Market opportunities from F2?** Does it include trends, skills, opportunities?
- [ ] **Content calendar from F3?** Does it include pillars, schedule, first piece?
- [ ] **Top 5 priority actions?** Are they specific and actionable?
- [ ] **30/60/90 day goals?** Are they time-bound and measurable?
- [ ] **No redundancy?** Does each piece of info appear only once?
- [ ] **Source traceability?** Can you trace each section to F1/F2/F3?

**If any check fails:** Go back to Gemini and ask for revisions.

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
| **< 50%** | Intelligence accumulation proven. Patterns compounded. |
| **50-66%** | Good acceleration. Some overhead from aggregation complexity. |
| **66-80%** | Moderate acceleration. Check if scope crept or tool switching slowed you. |
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

- [ ] Reused prompting structure from F1-F3
- [ ] Validation checklist was already familiar
- [ ] Knew how to ask for revisions
- [ ] Gemini App workflow was practiced
- [ ] Quality gates were clear from constitution
- [ ] [Your observation: __________]

## What Slowed F4 (if applicable)?

- [ ] Aggregating three outputs took time
- [ ] Had to go back and fix F1/F2/F3 outputs
- [ ] Redundancy check required multiple iterations
- [ ] [Your observation: __________]
```

## What You Built

You now have a complete **Personal AI Business Intelligence System**:

```
personal-bi-system/
├── my-profile-data.md           # Your raw profile data
├── sources-list.md              # F2 research sources
├── TIME_TRACKER.md              # Acceleration measurement
├── .specify/
│   └── memory/
│       └── constitution.md      # Quality standards
└── outputs/
    ├── f1-brand-analysis.md     # Brand strengths, gaps, positioning
    ├── f2-market-brief.md       # Trends, skills, opportunities
    ├── f3-content-strategy.md   # Pillars, topics, schedule
    └── f4-action-dashboard.md   # Unified dashboard with actions
```

**The system:**
1. Analyzes YOUR professional brand (F1)
2. Researches YOUR target market (F2)
3. Generates YOUR content strategy (F3)
4. Produces YOUR action plan (F4)

All built with AI tools you already know, validated against a constitution you wrote.

## Try With AI

Get feedback on your complete system:

**Prompt 1: Dashboard Completeness**

In Gemini App:

```
Review this action dashboard for a personal BI system:

[Paste your f4-action-dashboard.md]

Questions:
1. Are the priority actions specific enough to start today?
2. Do the 30/60/90 day goals have clear success metrics?
3. What's missing that would make this dashboard more actionable?
4. If I only had 2 hours this week, which actions should I prioritize?
```

**Observe:** Gemini may suggest making goals more measurable or actions more specific.

**Prompt 2: System Integration Check**

```
I built a 4-feature personal BI system:
- F1: Brand analysis
- F2: Market intelligence
- F3: Content strategy
- F4: Action dashboard

Each feature feeds the next: F1→F2→F3→F4

Questions:
1. Are there gaps in the data flow? Does F4 miss anything from F1-F3?
2. If I updated F1 (new strengths discovered), how would that cascade through F2-F4?
3. What Feature 5 would add the most value to this system?
```

**Note insights** for the retrospective in Lesson 7.

---

**Feature 4 complete.** You've proven intelligence accumulation by building F4 faster than F1.

Your complete Personal BI System is ready. Start Lesson 6: Create reusable skills from the patterns you discovered.
