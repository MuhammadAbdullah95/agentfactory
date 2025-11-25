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
  - name: "Spec-Kit Plus Project Initialization"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can run specifyplus init and navigate project structure"

  - name: "Creating Project Constitutions"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can use /sp.constitution to create quality standards for a multi-feature AI system"

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
  - objective: "Initialize a Spec-Kit Plus project for personal BI system"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "specifyplus init creates correct project structure"

  - objective: "Create a project constitution using /sp.constitution"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Constitution includes vision, principles, feature specs, quality gates"

  - objective: "Prepare personal profile data for analysis"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student has LinkedIn About, GitHub bio, and portfolio text ready"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (specifyplus init, /sp.constitution, quality gates, personal BI, data preparation) within B1 limit ✓"

differentiation:
  extension_for_advanced: "Add additional quality constraints for content voice consistency"
  remedial_for_struggling: "Use provided constitution principles; focus on data gathering"

generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "4.0.0"
---

# Project Setup + Constitution

You're building a Personal AI Business Intelligence System with four features: Brand Profiler, Market Scanner, Content Strategy, and Action Dashboard. Before using any AI tools, you'll initialize your project with Spec-Kit Plus and create a constitution using `/sp.constitution`.

This constitution becomes your decision framework—the standard you reference when building each feature. If Feature 4 builds significantly faster than Feature 1, you'll know it's because you stopped re-deciding quality standards and reused your constitution.

## Gather Your Personal Data

Before anything else, collect the raw material for your brand analysis.

**Open these in browser tabs:**
1. **LinkedIn** — Your profile's "About" section
2. **GitHub** — Your profile bio and pinned repositories
3. **Portfolio** (if you have one) — Your main description/tagline

**Copy this data somewhere accessible** — You'll paste it into prompts throughout this capstone.

**Minimum required:**
- LinkedIn About section (1-3 paragraphs)
- GitHub bio (1-2 sentences)
- Target role/industry (what kind of roles are you targeting?)
- 3-5 target companies (companies you'd want to work for)

## Initialize Your Project

Use Spec-Kit Plus to create the project structure. In your terminal:

```bash
# Create a new Spec-Kit Plus project
specifyplus init personal-bi-system

# Navigate to the project
cd personal-bi-system
```

**Interactive Prompts:**

During initialization, you'll see:

```
? Select AI Tool:
  > Claude Code
    Gemini CLI

? Select Terminal:
  > bash
    powershell (Windows only)
```

**Recommendations:**
- **AI Tool**: Choose **Claude Code** (recommended for this book)
- **Terminal**: Choose **bash** (or powershell if on Windows without WSL)

**Verify your project structure:**

```bash
ls -la
```

**Expected:**
```
personal-bi-system/
├── .claude/
│   └── commands/           # Slash commands (/sp.specify, /sp.plan, etc.)
├── .specify/
│   ├── memory/             # Constitution lives here
│   ├── scripts/            # Automation scripts
│   └── templates/          # Templates for specs, plans, tasks
├── CLAUDE.md               # Agent instructions
├── README.md               # Project documentation
└── .gitignore
```

The `specs/` and `history/` directories will be created automatically when you start your first feature.

## Create Your Constitution

The constitution defines quality standards for all four features. Use `/sp.constitution` to create it interactively.

**In Claude Code, run:**

```
/sp.constitution

Project principles and standards:

Vision: Build an intelligent system that analyzes your professional presence, researches your target market, and generates actionable career positioning strategy—all using AI tools (Gemini App, NotebookLM) without writing code.

Core Principles:
1. Your Real Data: All analysis uses YOUR actual profiles and target companies—not hypothetical data.
2. Structured Outputs: Every feature produces structured markdown with clear sections. No freeform text.
3. Actionable Results: Every output includes specific next steps. Analysis without action items is incomplete.
4. Source Traceability: Market research cites specific sources. Brand analysis references specific profile sections.

Technical Stack:
- Gemini App (gemini.google.com) for brand analysis and content generation
- NotebookLM (notebooklm.google.com) for multi-source research synthesis
- Claude Code for SDD-RI workflow orchestration
- No student-written code (AI tools do the work)

Feature Specifications:

### Feature 1: Personal Brand Profiler
Tool: Gemini App
Input: LinkedIn About, GitHub bio, portfolio description
Output: Brand analysis with 3+ strengths (with evidence citations), 2+ gaps, positioning statement, differentiation opportunities, confidence score
Quality Gate: Must cite specific phrases from profile as evidence for each strength

### Feature 2: Market Intelligence Scanner
Tool: NotebookLM
Input: 3-5 target company pages, job postings, industry articles
Output: Market brief with 3+ trends, in-demand skills, competitor landscape, opportunity areas, source citations
Quality Gate: Must synthesize 3+ different sources with specific citations

### Feature 3: Content Strategy Generator
Tool: Gemini App
Input: F1 brand analysis + F2 market brief
Output: Content strategy with 3 pillars, weekly schedule, 10+ topics, format recommendations, first week actions
Quality Gate: Content pillars must connect F1 strengths to F2 market trends

### Feature 4: Action Dashboard
Tool: Claude Code (markdown aggregation)
Input: F1 + F2 + F3 outputs
Output: Unified dashboard with brand summary, market opportunities, content calendar, top 5 actions, 30/60/90 day goals
Quality Gate: Dashboard aggregates all three features without redundancy. Each section traces to source feature.

Non-Goals:
- Production web application
- Automated social media posting
- Database or persistent storage beyond files
- Real-time market data feeds

Constraints:
- Tools: Only Gemini App, NotebookLM, Claude Code
- Data: Only public information + your own profiles
- No code: Students don't write Python (that's Part 5)
- Time: Each feature should be < 60 minutes (F4 target: < 30 minutes)
```

**Agent does:**
- Creates `.specify/memory/constitution.md` with your project standards
- Sets up quality gates for each feature
- Defines tool constraints and non-goals

**Verify the constitution:**

```bash
cat .specify/memory/constitution.md
```

Read through it once. This is your quality gate document for all four features.

## Set Up Time Tracking

Create a time tracker to measure intelligence accumulation:

```
Ask Claude Code:

Create a TIME_TRACKER.md file in the project root with this structure:

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
- F4 actual: _____ minutes
- **F4 vs F1 ratio**: _____ % (calculate: F4_time / F1_time × 100)
- **Target: F4 ≤ 50% of F1**

## Pattern Transfer Notes

What patterns from earlier features made later features faster?
- Prompting patterns reused:
- Output validation shortcuts:
- Quality gate checks that became automatic:
```

## Verify Complete Setup

Check your project structure:

```bash
ls -la
ls .specify/memory/
```

**Expected files:**
- `.specify/memory/constitution.md` — Quality standards (created by /sp.constitution)
- `TIME_TRACKER.md` — Acceleration measurement
- `.claude/commands/` — Slash commands for SDD workflow

## Commit Your Constitution

Before starting features, commit the constitution to git:

```
/sp.git.commit_pr Commit the constitution as the foundation for the Personal BI project.
```

**Agent does:**
- Commits constitution and project structure
- Creates PR or pushes to branch

## What's Next

You now have:
1. **Spec-Kit Plus project** initialized with correct structure
2. **Constitution** defining quality gates for all four features
3. **Time tracker** ready to measure acceleration
4. **Personal data** gathered for Feature 1

In Lesson 2, you'll build Feature 1 (Personal Brand Profiler) using the full SDD-RI workflow:
- `/sp.specify` — Create specification
- `/sp.plan` — Generate implementation plan
- `/sp.tasks` — Break into atomic tasks
- `/sp.implement` — Execute with Gemini App

**Start your F1 timer when you begin Lesson 2.**
