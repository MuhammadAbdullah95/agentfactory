---
sidebar_position: 3
title: "Feature 2: Market Intelligence Scanner"
chapter: 15
lesson: 3
duration_minutes: 45

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 4"
layer_progression: "L4 capstone - first acceleration measurement with NotebookLM"
layer_4_capstone: "Multi-source research synthesis, pipeline architecture (F1→F2)"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Feature Specification with /sp.specify"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can use /sp.specify to create structured specification for NotebookLM research feature"

  - name: "Implementation Planning with /sp.plan"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can generate implementation plan for multi-source research workflow"

  - name: "Task Decomposition with /sp.tasks"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can break research plan into atomic tasks with checkpoints"

  - name: "AI-Driven Implementation with /sp.implement"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can execute NotebookLM research tasks with checkpoint review pattern"

learning_objectives:
  - objective: "Use /sp.specify to create market research specification"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Specification file created with intent, tool constraints, success evals"

  - objective: "Execute full SDD-RI workflow for Feature 2"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student runs /sp.specify → /sp.plan → /sp.tasks → /sp.implement"

  - objective: "Measure first acceleration against F1 baseline"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "TIME_TRACKER.md shows F2 vs F1 comparison"

cognitive_load:
  new_concepts: 5
  reused_concepts: 6
  assessment: "5 new concepts (NotebookLM, multi-source synthesis, citations, market brief, research queries) + 6 reused from F1 (/sp.specify, /sp.plan, /sp.tasks, /sp.implement, quality gates, checkpoint review) within B1 limit ✓"

differentiation:
  extension_for_advanced: "Add competitive analysis section comparing 3 direct competitors; use /sp.clarify for specification refinement"
  remedial_for_struggling: "Use provided specification template exactly; focus on checkpoint review"

generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "4.0.0"
---

# Feature 2: Market Intelligence Scanner

Your Feature 1 brand analysis identified strengths, gaps, and positioning opportunities. Now you'll research your target market to discover where those strengths match real demand.

**This is your first acceleration measurement.** You've already practiced the full SDD-RI workflow in F1. Those patterns transfer directly to F2—you're just using a different tool (NotebookLM instead of Gemini App).

**START YOUR TIMER NOW.** Update TIME_TRACKER.md:

```
F2: Market Intelligence Scanner | Start: [current time] | End: | Duration: |
```

## Step 1: Create Your Specification (/sp.specify)

Run the specify command to create your feature specification:

```
/sp.specify

Feature: Market Intelligence Scanner

Intent:
Research my target market using NotebookLM to produce a structured market brief.
The brief identifies industry trends, in-demand skills, competitor landscape, and opportunities matching my profile.

Input Data:
- F1 brand analysis (specs/brand-profiler/output/f1-brand-analysis.md)
- 3-5 research sources I'll upload to NotebookLM:
  - Target company pages (About, Careers)
  - Job postings for my target role
  - Industry articles on trends

Tool: NotebookLM (notebooklm.google.com)

Constraints:
- Must use NotebookLM (browser-based, no API)
- Must upload 3+ sources before querying
- Must produce structured markdown output with citations
- Must connect findings to F1 strengths/gaps

Success Evals:
- Output contains 3+ industry trends
- Each trend includes source citation
- Output contains in-demand skills list (technical + soft)
- Output contains competitor/peer landscape
- Output contains opportunity areas matched to F1 strengths
- All insights cite specific uploaded sources
- Output saved to specs/market-scanner/output/f2-market-brief.md

Non-Goals:
- No paid research databases
- No automated source scraping
- No content recommendations (that's Feature 3)
```

**Agent does:**
- Creates `specs/market-scanner/spec.md` with your specification
- Validates against constitution quality gates
- Confirms intent is clear and success evals are testable

**Verify the specification:**

```bash
cat specs/market-scanner/spec.md
```

## Step 2: Generate Implementation Plan (/sp.plan)

Run the plan command to generate your research strategy:

```
/sp.plan

Context: specs/market-scanner/spec.md

Generate a plan for implementing the Market Intelligence Scanner using NotebookLM.

The plan should cover:
1. How to gather and upload research sources
2. What queries to run against the sources
3. How to synthesize responses into market brief
4. How to validate output against quality gates

Tool constraints from constitution:
- NotebookLM at notebooklm.google.com (browser-based)
- Multi-source synthesis with citations
- Structured markdown output
```

**Agent does:**
- Creates `specs/market-scanner/plan.md`
- Outlines phases: Source Gathering → NotebookLM Setup → Query Execution → Synthesis → Validation
- References constitution quality gates

**Verify the plan:**

```bash
cat specs/market-scanner/plan.md
```

## Step 3: Break Into Tasks (/sp.tasks)

Run the tasks command to decompose the plan into atomic work units:

```
/sp.tasks

Context:
- Specification: specs/market-scanner/spec.md
- Plan: specs/market-scanner/plan.md

Break down into atomic tasks with checkpoints.
```

**Agent does:**
- Creates `specs/market-scanner/tasks.md`
- Defines phases with checkpoints
- Each task is small enough to verify independently

**Expected task structure:**

```
Phase 1: Source Gathering
├─ Task 1.1: Create sources-list.md with 3-5 target sources
├─ Task 1.2: Gather target company URLs (About, Careers pages)
├─ Task 1.3: Copy job posting text for target roles
├─ Task 1.4: Find industry trend articles
└─ CHECKPOINT 1: Review sources before uploading to NotebookLM

Phase 2: NotebookLM Setup
├─ Task 2.1: Open NotebookLM and create new notebook
├─ Task 2.2: Upload all sources (websites and text)
├─ Task 2.3: Wait for all sources to show "Ready" status
└─ CHECKPOINT 2: Confirm all sources processed successfully

Phase 3: Query Execution
├─ Task 3.1: Query for industry trends (with citation requirements)
├─ Task 3.2: Query for in-demand skills (technical + soft)
├─ Task 3.3: Query for competitor/peer landscape
├─ Task 3.4: Query for opportunity mapping (using F1 strengths/gaps)
└─ CHECKPOINT 3: Review all query responses for completeness

Phase 4: Synthesis and Validation
├─ Task 4.1: Compile responses into structured market brief
├─ Task 4.2: Verify 3+ trends with citations
├─ Task 4.3: Verify skills list is separated (technical/soft)
├─ Task 4.4: Verify opportunity areas connect to F1 strengths
├─ Task 4.5: Verify all insights cite uploaded sources
└─ CHECKPOINT 4: All quality gates pass?

Phase 5: Save Output
├─ Task 5.1: Create output directory
├─ Task 5.2: Save validated output to f2-market-brief.md
└─ CHECKPOINT 5: Feature complete
```

**Verify the tasks:**

```bash
cat specs/market-scanner/tasks.md
```

## Step 4: Execute Implementation (/sp.implement)

Now execute the tasks with checkpoint review:

```
/sp.implement

Context:
- Specification: specs/market-scanner/spec.md
- Plan: specs/market-scanner/plan.md
- Tasks: specs/market-scanner/tasks.md

Execute Phase 1 (Source Gathering) with checkpoint.
```

### Phase 1: Source Gathering

**Agent does:**
- Task 1.1: Asks you to identify 3-5 research sources
- Task 1.2-1.4: Guides you to gather URLs and text

**You provide:**

```
Here are my research sources:

## Target Companies (from my F1 data)
1. [Company Name] - [About page URL]
2. [Company Name] - [Careers page URL]
3. [Company Name] - [URL]

## Job Postings
1. [Job Title] at [Company] - [URL or paste full text]
2. [Job Title] at [Company] - [URL or paste full text]

## Industry Articles
1. "[Article Title]" - [Publication] - [URL]
2. "[Article Title]" - [Publication] - [URL]
```

**CHECKPOINT 1:** Review sources before uploading to NotebookLM.
- Do you have 3+ sources?
- Are sources relevant to your target role/industry?
- Can NotebookLM access these URLs (public pages)?

**Your decision:**
- ✅ "Sources look good. Proceed to Phase 2."
- ❌ "Need more sources. Let me add more."

### Phase 2: NotebookLM Setup

```
Continue /sp.implement - Execute Phase 2 (NotebookLM Setup)
```

**Agent instructs:**
- Task 2.1: Open notebooklm.google.com, create new notebook named "Personal BI - Market Research"
- Task 2.2: Add sources using "+ Add source" → Website or Copied text
- Task 2.3: Wait for "Ready" status on all sources

**You do:**
1. Open NotebookLM
2. Create new notebook
3. Add each source (website URL or pasted text)
4. Wait for processing to complete

**CHECKPOINT 2:** Confirm all sources processed successfully.
- Do all sources show "Ready" status?
- Did any sources fail to load?

**Your decision:**
- ✅ "All sources ready. Proceed to Phase 3."
- ❌ "Some sources failed. Need to retry or replace."

### Phase 3: Query Execution

```
Continue /sp.implement - Execute Phase 3 (Query Execution)
```

**Agent provides query templates:**

**Task 3.1: Industry Trends Query**
```
Based on all the sources I've uploaded, what are the top 3-5 industry trends
that appear across multiple sources?

For each trend:
1. Name the trend in 3-5 words
2. Quote or cite specific evidence from the sources
3. Explain why this trend matters for someone entering this field
```

**Task 3.2: In-Demand Skills Query**
```
Analyze the job postings and company pages I've uploaded.

What technical and soft skills appear most frequently?

Format as:
- **Technical Skills**: [list with frequency if possible]
- **Soft Skills**: [list with frequency if possible]
- **Emerging Skills**: [skills mentioned as "nice to have" or future-focused]

Cite which sources mention each skill.
```

**Task 3.3: Competitor/Peer Landscape Query**
```
Based on these sources, who are the key players in this space?

Identify:
1. Major companies (from the sources)
2. What differentiates them from each other
3. What skills or qualities they seem to value most

Cite specific evidence from each source.
```

**Task 3.4: Opportunity Mapping Query (uses F1 output)**
```
I have these professional strengths (from my brand analysis):
[Paste your 3+ strengths from f1-brand-analysis.md]

I have these brand gaps:
[Paste your 2+ gaps from f1-brand-analysis.md]

Based on the market intelligence from these sources:
1. Which of my strengths align with current market demand? (cite evidence)
2. Which of my gaps are most critical to address? (cite evidence)
3. What opportunities exist where my strengths meet unmet market needs?
```

**This is the pipeline connection**: F1's output (your strengths and gaps) becomes F2's input for opportunity analysis.

**You do:**
1. Run each query in NotebookLM
2. Copy responses
3. Note which sources are cited

**CHECKPOINT 3:** Review all query responses for completeness.
- Did NotebookLM cite specific sources?
- Are all required sections covered?

**Your decision:**
- ✅ "Got complete responses. Proceed to Phase 4."
- ❌ "Responses incomplete. Need to re-query."

### Phase 4: Synthesis and Validation

```
Continue /sp.implement - Execute Phase 4 (Synthesis and Validation)

Here are NotebookLM's responses:

## Industry Trends Response:
[PASTE RESPONSE]

## In-Demand Skills Response:
[PASTE RESPONSE]

## Competitor Landscape Response:
[PASTE RESPONSE]

## Opportunity Mapping Response:
[PASTE RESPONSE]
```

**Agent validates:**
- Task 4.1-4.5: Checks each quality gate

**Agent reports:**

```
Validation Results:
✓ 4 industry trends found with citations
✓ Skills separated into technical and soft categories
✓ Competitor landscape includes 3 companies
✓ Opportunity areas connected to F1 strengths
✓ All insights cite uploaded sources

All quality gates PASS.
```

**If validation fails:**

```
Validation Results:
✓ 3 industry trends found
✗ Trend #2 missing source citation
✓ Skills list complete
...

Quality gate FAILED: Missing source citation.

Suggested fix: Ask NotebookLM to revise trend #2 to include specific citation.
```

**CHECKPOINT 4:** All quality gates pass?
- ✅ "All gates pass. Proceed to Phase 5."
- ❌ "Need to fix [specific issue]. Retrying validation."

### Phase 5: Save Output

```
Continue /sp.implement - Execute Phase 5 (Save Output)
```

**Agent does:**
- Task 5.1: Creates `specs/market-scanner/output/` directory
- Task 5.2: Saves validated output to `f2-market-brief.md` with header

**Output file format:**

```markdown
# Feature 2: Market Intelligence Brief
Generated: [today's date]
Tool: NotebookLM (notebooklm.google.com)
Workflow: /sp.implement
Sources: [count] sources analyzed

---

## Industry Trends

[Validated trend content with citations]

## In-Demand Skills

### Technical Skills
[List from query response]

### Soft Skills
[List from query response]

### Emerging Skills
[List from query response]

## Competitor/Peer Landscape

[Validated competitor content]

## Opportunity Areas (Matched to My Profile)

### Strengths That Match Market Demand
[Content connecting F1 strengths to market demand]

### Priority Gaps to Address
[Content identifying critical gaps]

### Unique Opportunity Areas
[Content on opportunity intersection]

---

## Sources Cited

1. [Source 1 name and URL]
2. [Source 2 name and URL]
3. [Source 3 name and URL]
[etc.]

---

## Quality Gate Verification
- [x] 3+ industry trends with citations
- [x] In-demand skills (technical + soft)
- [x] Competitor/peer landscape
- [x] Opportunity areas matched to F1 strengths
- [x] All insights cite specific sources
```

**CHECKPOINT 5:** Feature complete.

```bash
cat specs/market-scanner/output/f2-market-brief.md
```

## Stop Your Timer

Record your end time in TIME_TRACKER.md:

```
F2: Market Intelligence Scanner | Start: [time] | End: [current time] | Duration: [calculate] |
```

## Measure Your First Acceleration

Compare F2 to F1:

```
F1 Duration: _____ minutes
F2 Duration: _____ minutes
F2 as % of F1: _____ % (calculate: F2_time / F1_time × 100)
```

**Interpretation:**
- **< 75%**: Strong acceleration—SDD-RI workflow patterns from F1 transferred well
- **75-100%**: Moderate acceleration—some patterns transferred, new tool overhead
- **> 100%**: F2 took longer—NotebookLM learning curve offset pattern reuse

**Note what transferred from F1:**
- `/sp.specify` specification structure
- `/sp.plan` → `/sp.tasks` decomposition approach
- `/sp.implement` checkpoint review pattern
- Quality gate validation workflow

## Commit Feature 2

```
/sp.git.commit_pr Commit Feature 2 (Market Intelligence Scanner) - specification, plan, tasks, and output.
```

## What You Built

You now have:

```
specs/market-scanner/
├── spec.md              # Feature specification
├── plan.md              # Implementation plan
├── tasks.md             # Atomic tasks with checkpoints
└── output/
    └── f2-market-brief.md  # Validated output
```

**Artifacts created by SDD-RI workflow:**
1. **Specification** defining what success looks like (NotebookLM research)
2. **Plan** outlining how to achieve it (source gathering → queries → synthesis)
3. **Tasks** breaking it into verifiable steps
4. **Output** validated against quality gates

This output feeds Feature 3 (Content Strategy Generator). Your market trends and skill demands inform what content pillars to create.

## Pattern Notes

Record in TIME_TRACKER.md:

```
## Pattern Notes - Feature 2
- Workflow: /sp.specify → /sp.plan → /sp.tasks → /sp.implement (same as F1)
- Tool pattern: NotebookLM for multi-source synthesis (different from F1's Gemini App)
- Pipeline pattern: F1 output (strengths/gaps) became F2 input for opportunity mapping
- Acceleration: SDD-RI workflow familiar, only new element was NotebookLM
```

**Start Lesson 4: Feature 3 (Content Strategy Generator).** Record your F3 start time. You'll use the same SDD-RI workflow with Gemini App to synthesize F1 + F2 outputs.
