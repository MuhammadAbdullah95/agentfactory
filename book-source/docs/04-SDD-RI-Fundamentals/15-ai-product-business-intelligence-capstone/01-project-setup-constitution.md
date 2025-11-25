---
sidebar_position: 1
title: "Project Setup + Constitution"
chapter: 15
lesson: 1
duration_minutes: 30

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 4"
layer_progression: "L4 capstone foundation"
layer_4_capstone: "Constitution as decision framework for personal BI system"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Creating Project Constitutions"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can create a constitution document that defines quality standards for a multi-feature AI system"

  - name: "Establishing Quality Gates"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can define measurable quality gates for each feature output"

  - name: "Personal Data Preparation"
    proficiency_level: "A2"
    category: "Soft"
    bloom_level: "Apply"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can gather and organize their own professional profile data"

learning_objectives:
  - objective: "Create a project constitution for a personal BI system"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Constitution includes vision, principles, feature specs, quality gates"

  - objective: "Prepare personal profile data for analysis"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student has LinkedIn About, GitHub bio, and portfolio text ready"

  - objective: "Set up time tracker for measuring intelligence accumulation"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "TIME_TRACKER.md created with correct template"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (constitution, quality gates, personal BI, time tracking, data preparation) within B1 limit ✓"

differentiation:
  extension_for_advanced: "Add additional quality constraints for content voice consistency"
  remedial_for_struggling: "Use provided constitution template; focus on data gathering"

generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "3.0.0"
---

# Project Setup + Constitution

You're building a Personal AI Business Intelligence System with four features: Brand Profiler, Market Scanner, Content Strategy, and Action Dashboard. Before using any AI tools, you'll establish a project structure and a constitution that defines quality standards.

This constitution becomes your decision framework—the standard you reference when building each feature. If Feature 4 builds significantly faster than Feature 1, you'll know it's because you stopped re-deciding quality standards and reused your constitution.

## Gather Your Personal Data

Before anything else, collect the raw material for your brand analysis.

**Open these in browser tabs:**
1. **LinkedIn** — Your profile's "About" section
2. **GitHub** — Your profile bio and pinned repositories
3. **Portfolio** (if you have one) — Your main description/tagline

**Create a working file:**

```bash
mkdir personal-bi-system
cd personal-bi-system
touch my-profile-data.md
```

**Copy your data into `my-profile-data.md`:**

```markdown
# My Profile Data (Raw Input for Feature 1)

## LinkedIn About Section
[Paste your LinkedIn About section here - usually 1-3 paragraphs]

## GitHub Bio
[Paste your GitHub profile bio here - usually 1-2 sentences]

## Portfolio/Personal Site Description
[Paste your portfolio tagline or about page content here]

## Target Role/Industry
[Write 1-2 sentences: What kind of roles are you targeting? What industry?]

## 3-5 Target Companies
[List companies you'd want to work for - you'll research these in Feature 2]
1.
2.
3.
4.
5.
```

**Verify you have real data:**

```bash
cat my-profile-data.md
```

You should see YOUR actual profile content—not placeholders. This data feeds Feature 1.

## Initialize Project Structure

Set up the SDD-RI framework (same as Chapter 14):

```bash
# If specifyplus is installed from Chapter 14:
specifyplus init --here

# Verify structure:
ls -la
```

**Expected output:** `.specify/` directory with `memory/`, `templates/`, `scripts/` subdirectories.

If `.specify/` is missing, create it manually:

```bash
mkdir -p .specify/memory .specify/templates .specify/scripts
```

## Write Your Constitution

The constitution defines quality standards for all four features. Create it:

```bash
touch .specify/memory/constitution.md
```

Open in your editor and write:

```markdown
# Personal AI Business Intelligence Constitution

## Project Vision

Build an intelligent system that analyzes your professional presence, researches your target market, and generates actionable career positioning strategy—all using AI tools (Gemini App, NotebookLM, Claude Code) without writing code.

The system processes your profile data, synthesizes market research, and produces a concrete action plan for professional growth.

## Core Principles

1. **Your Real Data**: All analysis uses YOUR actual profiles and target companies—not hypothetical data.

2. **Structured Outputs**: Every feature produces structured output (JSON or markdown with clear sections). No freeform text that requires interpretation.

3. **Actionable Results**: Every output includes specific next steps. Analysis without action items is incomplete.

4. **Source Traceability**: Market research cites specific sources. Brand analysis references specific profile sections.

## Feature Specifications

### Personal Brand Profiler (Feature 1)
**Tool**: Gemini App (gemini.google.com)
**Input**: Your LinkedIn About, GitHub bio, portfolio description
**Output**: Brand analysis with:
- 3+ core strengths identified
- 2+ brand gaps (areas needing development)
- Positioning statement (1-2 sentences)
- Differentiation opportunities
- Confidence score (0-100)

**Quality Gate**: Must cite specific phrases from your profile as evidence for each strength.

### Market Intelligence Scanner (Feature 2)
**Tool**: NotebookLM (notebooklm.google.com)
**Input**: 3-5 target company pages, job postings, industry articles
**Output**: Market brief with:
- 3+ industry trends
- In-demand skills list
- Competitor/peer landscape
- Opportunity areas matching your profile
- Source citations

**Quality Gate**: Must synthesize 3+ different sources with specific citations.

### Content Strategy Generator (Feature 3)
**Tool**: Gemini App
**Input**: F1 brand analysis + F2 market brief
**Output**: Content strategy with:
- 3 content pillars (themes you'll focus on)
- Weekly posting schedule
- 10+ topic ideas with brief descriptions
- Format recommendations (posts, articles, videos)
- First week action items

**Quality Gate**: Content pillars must connect F1 strengths to F2 market trends.

### Action Dashboard (Feature 4)
**Tool**: Claude Code (markdown aggregation)
**Input**: F1 + F2 + F3 outputs
**Output**: Unified dashboard showing:
- Brand summary (from F1)
- Market opportunities (from F2)
- Content calendar (from F3)
- Priority action items (top 5)
- 30/60/90 day goals

**Quality Gate**: Dashboard aggregates all three features without redundancy. Each section traces to source feature.

## Non-Goals

- Production web application
- Automated social media posting
- Database or persistent storage beyond files
- Real-time market data feeds
- Multi-platform publishing integration

## Quality Standards

### Output Quality
- All outputs in markdown or JSON format
- Clear section headers for navigation
- Specific citations (not vague references)
- Action items are concrete (not "consider" or "maybe")

### Process Quality
- Each feature starts with specification review
- Outputs validated against quality gates before proceeding
- Time tracked for acceleration measurement

### Tool Usage
- Gemini App: Brand analysis, content generation
- NotebookLM: Research synthesis with source citations
- Claude Code: SDD-RI workflow, dashboard aggregation

## Constraints

- Tools: Only Gemini App, NotebookLM, Claude Code
- Data: Only public information + your own profiles
- No code: You don't write Python (AI tools do the work)
- Time: Each feature should be < 60 minutes (F4 target: < 30 minutes)
```

**Save and verify:**

```bash
cat .specify/memory/constitution.md
```

Read through it once. This is your quality gate document for all four features.

## Create Time Tracker

The time tracker measures intelligence accumulation:

```bash
touch TIME_TRACKER.md
```

Add this content:

```markdown
# Feature Build Times - Personal BI System

| Feature | Start Time | End Time | Duration (min) | Notes |
|---------|------------|----------|----------------|-------|
| F1: Personal Brand Profiler | | | | |
| F2: Market Intelligence Scanner | | | | |
| F3: Content Strategy Generator | | | | |
| F4: Action Dashboard | | | | |

## Acceleration Analysis

After all four features:

- F1 baseline: _____ minutes
- F2 actual: _____ minutes
- F3 actual: _____ minutes
- F4 actual: _____ minutes
- **F4 vs F1 ratio**: _____ % (calculate: F4_time / F1_time × 100)
- **Target: F4 ≤ 50% of F1**

## Pattern Transfer Notes

What patterns from earlier features made later features faster?

- Prompting patterns reused:
- Output validation shortcuts:
- Quality gate checks that became automatic:
```

**Verify:**

```bash
cat TIME_TRACKER.md
```

## Verify Setup

Check your complete project structure:

```bash
ls -la
ls -la .specify/memory/
```

**Expected files:**
- `my-profile-data.md` — Your raw profile content
- `.specify/memory/constitution.md` — Quality standards
- `TIME_TRACKER.md` — Acceleration measurement

**Verify data is real:**

```bash
head -20 my-profile-data.md
```

You should see YOUR LinkedIn/GitHub content—not placeholder text.

## Try With AI

Before starting Feature 1, get AI feedback on your setup:

**Prompt 1: Constitution Review**

Open Gemini App (gemini.google.com) and ask:

```
Review this constitution for a personal business intelligence system:

[Paste your entire constitution.md content]

Questions:
1. Are the quality gates specific enough to validate?
2. What integration issues might arise between Feature 1 output and Feature 2 input?
3. What's missing that would prevent Feature 4 from aggregating everything properly?
```

**Observe**: Gemini will likely identify gaps in how Feature 1's brand analysis feeds Feature 3's content strategy. Fix these in your constitution before proceeding.

**Prompt 2: Profile Data Check**

```
Here's my profile data that will feed into a brand analysis:

[Paste your my-profile-data.md content]

Before I analyze this with AI:
1. Is there enough content for meaningful analysis?
2. What additional information should I add?
3. Are my target companies specific enough for market research?
```

**Observe**: Gemini will tell you if your profile data is too thin. Add more content if needed.

---

**Setup complete.** Close this lesson. Start Lesson 2: Build Feature 1 (Personal Brand Profiler). When you start, open TIME_TRACKER.md and record your start time.
