---
sidebar_position: 7
title: "Ship + Retrospective"
chapter: 15
lesson: 7
duration_minutes: 30

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 4"
layer_progression: "L4 capstone - shipping and reflection"
layer_4_capstone: "Final verification, retrospective analysis, documented learnings"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "System Verification"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can verify all system outputs exist and meet quality standards"

  - name: "Acceleration Analysis"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can calculate acceleration percentages and interpret what patterns caused acceleration"

  - name: "Retrospective Documentation"
    proficiency_level: "B1"
    category: "Soft"
    bloom_level: "Evaluate"
    digcomp_area: "Communication"
    measurable_at_this_level: "Student can write honest retrospective capturing what worked, what slowed down, and learnings for future"

  - name: "Project Completion"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can finalize project with proper documentation and file organization"

learning_objectives:
  - objective: "Verify all system outputs exist and meet quality gates"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "All four feature outputs verified against constitution"

  - objective: "Calculate and interpret acceleration metrics from TIME_TRACKER.md"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student calculates F2-F4 as percentage of F1 and explains acceleration causes"

  - objective: "Write retrospective documenting what accelerated and what slowed development"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "RETROSPECTIVE.md includes specific patterns, friction points, and transferable learnings"

cognitive_load:
  new_concepts: 3
  reused_concepts: 8
  assessment: "3 new concepts (retrospective analysis, acceleration interpretation, project shipping) + 8 reused from F1-F4 (verification, quality gates, documentation, file organization) within B1 limit ✓"

differentiation:
  extension_for_advanced: "Add detailed acceleration analysis by decision type; propose Feature 5 specification"
  remedial_for_struggling: "Focus on verification checklist and basic retrospective; use provided templates"

generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "3.0.0"
---

# Ship + Retrospective

Your four features are built. Your skills are created. Now verify everything is complete, document what you learned, and ship.

## Verify Your System

Check that all outputs exist and meet quality standards.

### Output Files Verification

```bash
ls outputs/
```

**Expected files:**
- `f1-brand-analysis.md`
- `f2-market-brief.md`
- `f3-content-strategy.md`
- `f4-action-dashboard.md`

**Missing any files?** Go back and complete that feature.

### Quality Gate Verification

For each output, verify it meets the constitution's quality gates:

**F1: Brand Analysis**
```bash
cat outputs/f1-brand-analysis.md | head -40
```

Checklist:
- [ ] 3+ core strengths with evidence citations?
- [ ] 2+ brand gaps identified?
- [ ] Positioning statement (1-2 sentences)?
- [ ] Differentiation opportunities?
- [ ] Confidence score?

**F2: Market Brief**
```bash
cat outputs/f2-market-brief.md | head -40
```

Checklist:
- [ ] 3+ industry trends?
- [ ] In-demand skills list?
- [ ] Competitor/peer landscape?
- [ ] Opportunity areas matched to your profile?
- [ ] 3+ source citations?

**F3: Content Strategy**
```bash
cat outputs/f3-content-strategy.md | head -40
```

Checklist:
- [ ] 3 content pillars?
- [ ] Each pillar connects F1 strength to F2 trend?
- [ ] 10+ topic ideas?
- [ ] Weekly posting schedule?
- [ ] First week action items?

**F4: Action Dashboard**
```bash
cat outputs/f4-action-dashboard.md | head -40
```

Checklist:
- [ ] Brand summary from F1?
- [ ] Market opportunities from F2?
- [ ] Content calendar from F3?
- [ ] Top 5 priority actions?
- [ ] 30/60/90 day goals?
- [ ] No redundancy across sections?

**If any check fails:** Go back to the relevant feature and fix it before proceeding.

### Supporting Files Verification

```bash
ls -la
```

**Expected files:**
- `my-profile-data.md` — Your raw profile data
- `sources-list.md` — F2 research sources
- `TIME_TRACKER.md` — Acceleration measurement
- `.specify/memory/constitution.md` — Quality standards

### Skills Verification

```bash
ls .claude/skills/
```

**Expected files:**
- `structured-ai-prompting.md`
- `multi-source-synthesis.md`
- (optional third skill)

## Complete Your Acceleration Data

Open `TIME_TRACKER.md` and fill in any missing data:

```bash
cat TIME_TRACKER.md
```

**Required data:**

| Feature | Duration | % of F1 |
|---------|----------|---------|
| F1 | _____ min | 100% (baseline) |
| F2 | _____ min | _____% |
| F3 | _____ min | _____% |
| F4 | _____ min | _____% |

**Calculate your acceleration:**

```
F4 as % of F1 = (F4 duration / F1 duration) × 100

Example:
- F1 = 60 minutes
- F4 = 25 minutes
- F4 as % of F1 = (25 / 60) × 100 = 42%
- Result: F4 took 42% of F1 time (target was ≤ 50%)
```

**Did you achieve the target?**

| Result | Interpretation |
|--------|----------------|
| **F4 < 50% of F1** | Target achieved. Intelligence accumulation proven. |
| **F4 = 50-66% of F1** | Good acceleration. Patterns transferred well. |
| **F4 = 66-80% of F1** | Moderate acceleration. Some overhead remained. |
| **F4 > 80% of F1** | Limited acceleration. Analyze what didn't transfer. |

## Write Your Retrospective

Create the retrospective file:

```bash
touch RETROSPECTIVE.md
```

Copy this template and fill it in:

```markdown
# Personal BI System Retrospective

## Acceleration Results

- **F1 baseline:** _____ minutes
- **F4 actual:** _____ minutes
- **F4 as % of F1:** _____% (target: ≤ 50%)
- **Target achieved:** YES / NO

## What Accelerated Development?

List specific patterns that made F2-F4 faster than F1:

### Pattern 1: _______________________
- **Where used:** Features ___, ___, ___
- **Why it accelerated:** _______________________
- **Example:** _______________________

### Pattern 2: _______________________
- **Where used:** Features ___, ___, ___
- **Why it accelerated:** _______________________
- **Example:** _______________________

### Pattern 3: _______________________
- **Where used:** Features ___, ___
- **Why it accelerated:** _______________________

## What Slowed Development?

List friction points or things that didn't transfer as expected:

### Friction Point 1: _______________________
- **Which feature:** F___
- **Why it slowed down:** _______________________
- **What you'd do differently:** _______________________

### Friction Point 2: _______________________
- **Which feature:** F___
- **Why it slowed down:** _______________________
- **What you'd do differently:** _______________________

## Tool Learnings

### Gemini App (F1, F3, F4)
- **What worked well:** _______________________
- **What was frustrating:** _______________________
- **Prompting insight:** _______________________

### NotebookLM (F2)
- **What worked well:** _______________________
- **What was frustrating:** _______________________
- **Research insight:** _______________________

## Skills Created

| Skill | Purpose | When to Use Again |
|-------|---------|-------------------|
| Structured AI Prompting | _______ | _______ |
| Multi-Source Synthesis | _______ | _______ |
| [Third skill if created] | _______ | _______ |

## One-Sentence Insight

What's the single most important thing you learned from this project?

> _______________________

## What Would You Do Differently?

If starting a similar project tomorrow:

1. **Constitution:** _______________________
2. **Feature order:** _______________________
3. **Time tracking:** _______________________
4. **Tool selection:** _______________________

## Transfer to Other Projects

This approach would work for:
- [ ] Job application preparation
- [ ] Research paper writing
- [ ] Product launch planning
- [ ] Event planning
- [ ] Other: _______________________

Why? Because the pattern of [personal data] → [market research] → [strategy] → [action plan] applies broadly.
```

**Save the file.**

## Project Summary

Create a summary file that captures your complete system:

```bash
touch PROJECT_SUMMARY.md
```

```markdown
# Personal AI Business Intelligence System

## What This Is

A 4-feature personal intelligence system built entirely with AI tools (Gemini App, NotebookLM). No code written—just structured prompting, validation, and synthesis.

## Features

| Feature | Tool | Input | Output |
|---------|------|-------|--------|
| F1: Brand Profiler | Gemini App | Your profile data | Brand analysis |
| F2: Market Scanner | NotebookLM | Target company research | Market brief |
| F3: Content Strategy | Gemini App | F1 + F2 outputs | Content plan |
| F4: Action Dashboard | Gemini App | F1 + F2 + F3 outputs | Unified action plan |

## Outputs Produced

```
outputs/
├── f1-brand-analysis.md    # Your strengths, gaps, positioning
├── f2-market-brief.md      # Trends, skills, opportunities
├── f3-content-strategy.md  # Pillars, topics, schedule
└── f4-action-dashboard.md  # Unified dashboard + actions
```

## Intelligence Accumulation Proof

| Feature | Duration | % of F1 |
|---------|----------|---------|
| F1 | [your time] | 100% |
| F4 | [your time] | [your %] |

**F4 built in [X]% of F1 time.** Patterns from F1 (structured prompting, validation, quality gates) transferred directly to F2-F4.

## Skills Created

1. **Structured AI Prompting** — How to get consistent, structured outputs from AI tools
2. **Multi-Source Synthesis** — How to combine multiple inputs without redundancy

## Key Learning

[Your one-sentence insight from retrospective]

## How to Reuse This Approach

1. Start with **constitution** defining quality gates
2. Build **F1 slowly** — establish patterns
3. Build **F2-F4 faster** — reuse patterns
4. **Track time** — prove accumulation
5. **Create skills** — encode learnings
```

## Final Project Structure

Your complete project should look like this:

```
personal-bi-system/
├── my-profile-data.md           # Your raw profile data
├── sources-list.md              # F2 research sources
├── TIME_TRACKER.md              # Acceleration measurement
├── RETROSPECTIVE.md             # What you learned
├── PROJECT_SUMMARY.md           # System overview
├── .specify/
│   └── memory/
│       └── constitution.md      # Quality standards
├── .claude/
│   └── skills/
│       ├── structured-ai-prompting.md
│       └── multi-source-synthesis.md
└── outputs/
    ├── f1-brand-analysis.md
    ├── f2-market-brief.md
    ├── f3-content-strategy.md
    └── f4-action-dashboard.md
```

Verify your structure:

```bash
ls -la
ls outputs/
ls .claude/skills/
```

## Try With AI

Get final feedback on your project:

**Prompt 1: Retrospective Analysis**

In Gemini App:

```
Review my retrospective from a Personal BI System project:

[Paste your RETROSPECTIVE.md content]

Questions:
1. Based on my acceleration data, what specific patterns drove the most time savings?
2. For the friction points I identified, what would you recommend doing differently?
3. Am I missing any key insight about why F4 was [faster/slower] than expected?
4. What question should I add to my retrospective that would help me learn more?
```

**Prompt 2: Next Project Planning**

```
I just completed a Personal BI System with these results:
- F4 took [X]% of F1 time
- Created 2 skills: Structured AI Prompting, Multi-Source Synthesis
- Key learning: [your insight]

I want to build a similar system for [new domain: job applications / research papers / etc.]

Questions:
1. Which of my skills would transfer directly?
2. What new skill would I need for this domain?
3. How should I adapt my constitution for this new use case?
4. What's my target acceleration for this second project? (Should I expect even better than 50%?)
```

---

**Project complete.** You've built a real Personal AI Business Intelligence System, proven intelligence accumulation with data, and created reusable skills.

Proceed to the Chapter 15 Quiz to assess your understanding.
