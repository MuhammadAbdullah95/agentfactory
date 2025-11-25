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
  - name: "Multi-Source AI Synthesis"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can feed multiple structured inputs to AI and generate integrated output"

  - name: "Content Pillar Design"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can identify content themes that connect personal strengths to market demand"

  - name: "Pipeline Composition"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain how F1 + F2 outputs become F3 inputs and produce integrated strategy"

  - name: "Actionable Output Generation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can generate specific action items from analysis, not vague recommendations"

learning_objectives:
  - objective: "Combine F1 brand analysis and F2 market brief into a unified content strategy"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Content pillars explicitly connect F1 strengths to F2 trends"

  - objective: "Generate actionable content plan with specific topics and schedule"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Output includes 10+ topic ideas and weekly posting schedule"

  - objective: "Demonstrate continued acceleration from F1 baseline"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "TIME_TRACKER.md shows F3 < F2 time"

cognitive_load:
  new_concepts: 4
  reused_concepts: 6
  assessment: "4 new concepts (content pillars, topic ideation, posting schedule, format selection) + 6 reused (structured prompting, validation, quality gates, Gemini App, time tracking, pipeline flow) within B1 limit ✓"

differentiation:
  extension_for_advanced: "Add audience persona development and content distribution channel strategy"
  remedial_for_struggling: "Use provided prompt templates exactly; focus on validating pillar-to-trend connections"

generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "3.0.0"
---

# Feature 3: Content Strategy Generator

You have a brand analysis (F1) and a market intelligence brief (F2). Now you'll combine them to generate an actionable content strategy—specific themes, topics, and a posting schedule tailored to your strengths and market demand.

**This is multi-input synthesis.** You're feeding two complete outputs (F1 + F2) into Gemini App and asking it to produce an integrated strategy. This mirrors how real business intelligence systems work: data flows through a pipeline, each stage adding value.

**Start your timer.** Record in TIME_TRACKER.md:

```
F3: Content Strategy Generator | Start: [current time] | End: | Duration: |
```

## Review Your Constitution

Open your constitution and check Feature 3's quality gates:

```bash
cat .specify/memory/constitution.md | grep -A 10 "Content Strategy Generator"
```

**Required outputs:**
- 3 content pillars (themes you'll focus on)
- Weekly posting schedule
- 10+ topic ideas with brief descriptions
- Format recommendations (posts, articles, videos)
- First week action items

**Quality gate:** Content pillars must connect F1 strengths to F2 market trends.

## Gather Your Inputs

You need both F1 and F2 outputs ready:

**Verify F1 output exists:**
```bash
cat outputs/f1-brand-analysis.md
```

You should see:
- Core strengths (3+)
- Brand gaps (2+)
- Positioning statement
- Differentiation opportunities

**Verify F2 output exists:**
```bash
cat outputs/f2-market-brief.md
```

You should see:
- Industry trends (3+)
- In-demand skills
- Competitor landscape
- Opportunity areas matched to your profile

**If either file is incomplete:** Go back and complete F1 or F2 before proceeding.

## Open Gemini App

Go to **gemini.google.com** in your browser.

Start a new conversation for Feature 3.

## Generate Content Pillars

Content pillars are the 3 main themes you'll create content around. They should connect YOUR strengths (F1) to MARKET demand (F2).

**Copy this prompt and fill in your data:**

```
You are a content strategist helping me build a personal brand content strategy.

## My Brand Analysis (from Feature 1)

### Core Strengths:
[Paste your 3+ strengths from f1-brand-analysis.md]

### Brand Gaps:
[Paste your 2+ gaps from f1-brand-analysis.md]

### Positioning Statement:
[Paste your positioning statement]

## Market Intelligence (from Feature 2)

### Industry Trends:
[Paste the top 3-5 trends from f2-market-brief.md]

### In-Demand Skills:
[Paste the technical and soft skills lists]

### Opportunity Areas:
[Paste the opportunity areas that matched your profile]

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

**Review the response:**
- Does each pillar connect to at least one of your F1 strengths?
- Does each pillar address at least one F2 trend or skill demand?
- Do the example topics feel specific to YOU, not generic?

**If connections are weak:** Ask Gemini to revise:

```
Pillar 2 doesn't clearly connect to my strengths. My strength is "[your strength]".
Revise Pillar 2 to explicitly leverage that strength while still addressing the market trend.
```

## Generate Topic Ideas

Now expand each pillar into specific content topics.

**Copy this prompt:**

```
Based on the 3 content pillars we just defined:

[Paste the 3 pillars Gemini generated]

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

**Review the response:**
- Are there 10+ topics?
- Are topics distributed across all 3 pillars?
- Do titles feel specific (not generic listicles)?
- Are formats varied (not all the same type)?

## Generate Weekly Schedule

Now create a realistic posting schedule.

**Copy this prompt:**

```
I want to post content consistently but sustainably.

My constraints:
- I can spend [2-4] hours per week on content creation
- I work best in the [morning/evening] for creative work
- I prefer [LinkedIn/Twitter/Blog/YouTube] as my primary platform

Based on the topics we generated, create a realistic weekly posting schedule.

Include:
1. **Day and Time** — When to post
2. **Content Type** — Post, article, thread, video
3. **Time Investment** — How long each piece takes to create
4. **Batch Recommendations** — Which pieces can be created together

Also recommend:
- Which topic to start with (and why)
- How to repurpose one piece across multiple formats
- What to do if I miss a week

Be realistic about time. Don't suggest daily posting if I only have 2 hours per week.
```

**Review the response:**
- Is the schedule sustainable given your time constraints?
- Are batch recommendations practical?
- Does the "where to start" recommendation make sense for your brand?

## Generate First Week Action Items

Make the strategy immediately actionable.

**Copy this prompt:**

```
Let's make this actionable for this week.

From the content strategy we built:
- 3 content pillars identified
- 10+ topic ideas generated
- Weekly schedule created

Generate my FIRST WEEK action items.

For each action item:
1. **Task** — Specific action (not vague)
2. **Time Required** — How long it takes
3. **Output** — What I'll have when done
4. **Why First** — Why this task should come before others

Include both content creation AND content distribution tasks.

Give me 5-7 action items total. No more than 4 hours total time investment.
Make each task completable in a single sitting.
```

**Review the response:**
- Are action items specific (not "work on content")?
- Is total time reasonable?
- Can you actually start on item #1 today?

## Compile Your Content Strategy

Create the output file:

```bash
touch outputs/f3-content-strategy.md
```

Compile all Gemini responses into a structured strategy:

```markdown
# Feature 3: Content Strategy
Generated: [today's date]
Tool: Gemini App (gemini.google.com)
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

[Paste the schedule Gemini generated]

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

- [ ] 3 content pillars defined? ✓
- [ ] Each pillar connects F1 strength to F2 trend? ✓
- [ ] 10+ topic ideas generated? ✓
- [ ] Weekly schedule is realistic? ✓
- [ ] First week actions are specific? ✓
```

**Verify the file:**

```bash
cat outputs/f3-content-strategy.md
```

## Validate Against Quality Gates

Check your output against the constitution:

**Checklist:**

- [ ] **3 content pillars?** Count them.
- [ ] **Pillars connect F1 to F2?** Each pillar should explicitly reference a strength AND a trend.
- [ ] **10+ topic ideas?** Count them.
- [ ] **Weekly schedule?** Is it specific about days/times?
- [ ] **Format recommendations?** Are different formats suggested?
- [ ] **First week actions?** Are there 5+ specific tasks?

**If any check fails:** Go back to Gemini and ask for revisions.

Example:

```
The content pillars don't clearly connect to my F2 market trends.

My top 3 trends from market research were:
1. [Trend 1]
2. [Trend 2]
3. [Trend 3]

Revise the pillars to explicitly address at least one of these trends each.
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
- **< 66%**: Strong acceleration—patterns are compounding
- **66-80%**: Good acceleration—synthesis was efficient
- **> 80%**: Check if you over-engineered or had tool issues

**Pattern notes for TIME_TRACKER.md:**

```
## Pattern Notes - Feature 3
- Synthesis pattern: Feeding two outputs into single prompt (F1 + F2 → F3)
- Iteration pattern: Asking for revisions when connections were weak
- Validation pattern: Same checklist approach as F1 and F2
- Acceleration driver: Reusing prompting structure from F1/F2
```

## What You Built

You now have:

1. **Content strategy** in `outputs/f3-content-strategy.md`
2. **3 content pillars** connecting your strengths to market demand
3. **10+ topic ideas** distributed across pillars
4. **Weekly schedule** with realistic time estimates
5. **First week actions** to start immediately

This output feeds Feature 4 (Action Dashboard). Your content strategy becomes one section of the unified dashboard alongside brand summary and market opportunities.

## Try With AI

Get feedback on your content strategy before moving to Feature 4:

**Prompt 1: Pillar Differentiation Check**

In Gemini App:

```
Review these 3 content pillars:

[Paste your 3 pillars]

Questions:
1. Are these pillars distinct enough? Or do they overlap too much?
2. Which pillar is strongest for building authority quickly?
3. Which pillar might be hardest to maintain consistently?
4. If I could only focus on ONE pillar for the first month, which should it be?
```

**Observe:** Gemini may identify overlap or suggest consolidation.

**Prompt 2: Topic Gap Analysis**

```
I have these 10+ content topics:

[Paste your topic list]

Gap analysis:
1. What content types am I missing? (tutorials, case studies, opinions, etc.)
2. Which topics would perform well on [your platform] specifically?
3. Are there any "low-hanging fruit" topics I'm missing—easy to create but high value?
4. Which topic should be my FIRST published piece and why?
```

**Update your `f3-content-strategy.md`** with insights from these checks.

---

**Feature 3 complete.** You've synthesized F1 + F2 into an actionable content strategy.

Start Lesson 5: Feature 4 (Action Dashboard). Record your F4 start time. This is the acceleration test—F4 should take less than 50% of F1's time.
