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
  - name: "Multi-Source Research Synthesis"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can upload multiple sources to NotebookLM and generate synthesized insights with citations"

  - name: "NotebookLM Research Workflow"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can create notebook, add sources, and query for structured analysis"

  - name: "Pipeline Architecture Understanding"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain how F1 brand analysis feeds F2 market research focus"

  - name: "Source Citation and Validation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can verify NotebookLM citations trace back to uploaded sources"

learning_objectives:
  - objective: "Use NotebookLM to synthesize market intelligence from multiple sources"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Market brief includes insights from 3+ sources with citations"

  - objective: "Connect F1 brand analysis to F2 market research focus"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Research targets align with F1 strengths and gaps"

  - objective: "Measure first acceleration against F1 baseline"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "TIME_TRACKER.md shows F2 vs F1 comparison"

cognitive_load:
  new_concepts: 5
  reused_concepts: 4
  assessment: "5 new concepts (NotebookLM, multi-source synthesis, citations, market brief, research queries) + 4 reused from F1 (quality gates, time tracking, structured output, validation) within B1 limit ✓"

differentiation:
  extension_for_advanced: "Add competitive analysis section comparing 3 direct competitors"
  remedial_for_struggling: "Use provided source list; focus on query templates exactly as written"

generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "3.0.0"
---

# Feature 2: Market Intelligence Scanner

Your Feature 1 brand analysis identified strengths, gaps, and positioning opportunities. Now you'll research your target market to discover where those strengths match real demand.

**This is your first acceleration measurement.** You've already practiced structured prompting and output validation in F1. Those patterns transfer directly to F2—you're just using a different tool (NotebookLM instead of Gemini App).

**Start your timer.** Record in TIME_TRACKER.md:

```
F2: Market Intelligence Scanner | Start: [current time] | End: | Duration: |
```

## Review Your Constitution

Open your constitution and check Feature 2's quality gates:

```bash
cat .specify/memory/constitution.md | grep -A 10 "Market Intelligence Scanner"
```

**Required outputs:**
- 3+ industry trends
- In-demand skills list
- Competitor/peer landscape
- Opportunity areas matching your profile
- Source citations

**Quality gate:** Must synthesize 3+ different sources with specific citations.

## Open NotebookLM

Go to **notebooklm.google.com** in your browser.

Sign in with your Google account if not already logged in.

Click **"+ New Notebook"** to create a fresh research space.

Name it: `Personal BI - Market Research`

## Gather Your Research Sources

NotebookLM synthesizes information from sources you upload. You need 3-5 high-quality sources about your target market.

**Based on your F1 brand analysis, gather:**

1. **Target company pages** (2-3 companies from your `my-profile-data.md`)
   - Their About pages or Company pages
   - Their Careers/Jobs pages (shows what skills they hire for)

2. **Job postings** (2-3 relevant roles)
   - Search LinkedIn Jobs or Indeed for your target role
   - Copy the full job description text

3. **Industry articles** (1-2 recent pieces)
   - Search for "[your industry] trends 2024" or "[your industry] skills demand"
   - Choose articles from credible sources (not ads)

**Create a sources file for reference:**

```bash
touch sources-list.md
```

Add your sources:

```markdown
# F2 Research Sources

## Target Companies
1. [Company Name] - [URL to About or Careers page]
2. [Company Name] - [URL to About or Careers page]
3. [Company Name] - [URL to About or Careers page]

## Job Postings
1. [Job Title] at [Company] - [URL or "pasted text"]
2. [Job Title] at [Company] - [URL or "pasted text"]

## Industry Articles
1. "[Article Title]" - [Source/Publication] - [URL]
2. "[Article Title]" - [Source/Publication] - [URL]

Total sources: [count - must be 3+]
```

## Add Sources to NotebookLM

In NotebookLM, click **"+ Add source"** in the left panel.

**For web pages:**
- Click "Website"
- Paste the URL
- NotebookLM will fetch and process the content

**For job postings (if you copied text):**
- Click "Copied text"
- Paste the full job description
- Give it a title like "Senior Developer Role - TechCorp"

**For articles:**
- Click "Website" and paste the URL
- Or copy-paste the article text if behind paywall

**Add all your sources** (minimum 3, aim for 5).

NotebookLM will process each source. Wait for all sources to show "Ready" status.

## Query for Market Intelligence

Now you'll ask NotebookLM to synthesize insights across all your sources.

**Query 1: Industry Trends**

In the chat panel, ask:

```
Based on all the sources I've uploaded, what are the top 3-5 industry trends
that appear across multiple sources?

For each trend:
1. Name the trend in 3-5 words
2. Quote or cite specific evidence from the sources
3. Explain why this trend matters for someone entering this field
```

**Copy NotebookLM's response.** Note which sources it cites.

**Query 2: In-Demand Skills**

```
Analyze the job postings and company pages I've uploaded.

What technical and soft skills appear most frequently?

Format as:
- **Technical Skills**: [list with frequency if possible]
- **Soft Skills**: [list with frequency if possible]
- **Emerging Skills**: [skills mentioned as "nice to have" or future-focused]

Cite which sources mention each skill.
```

**Copy the response.**

**Query 3: Competitor/Peer Landscape**

```
Based on these sources, who are the key players in this space?

Identify:
1. Major companies (from the sources)
2. What differentiates them from each other
3. What skills or qualities they seem to value most

Cite specific evidence from each source.
```

**Copy the response.**

**Query 4: Opportunity Mapping**

This query connects F1 (your brand) to F2 (market research):

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

## Compile Your Market Brief

Create the output file:

```bash
touch outputs/f2-market-brief.md
```

Compile NotebookLM's responses into a structured brief:

```markdown
# Feature 2: Market Intelligence Brief
Generated: [today's date]
Tool: NotebookLM (notebooklm.google.com)
Sources: [count] sources analyzed

---

## Industry Trends

[Paste Query 1 response - edited for clarity if needed]

## In-Demand Skills

### Technical Skills
[List from Query 2]

### Soft Skills
[List from Query 2]

### Emerging Skills
[List from Query 2]

## Competitor/Peer Landscape

[Paste Query 3 response]

## Opportunity Areas (Matched to My Profile)

### Strengths That Match Market Demand
[From Query 4 - which of your strengths are in demand]

### Priority Gaps to Address
[From Query 4 - which gaps matter most given market needs]

### Unique Opportunity Areas
[From Query 4 - where your profile meets unmet needs]

---

## Sources Cited

1. [Source 1 name and URL]
2. [Source 2 name and URL]
3. [Source 3 name and URL]
[etc.]
```

**Verify the file:**

```bash
cat outputs/f2-market-brief.md
```

## Validate Against Quality Gates

Check your output against the constitution:

**Checklist:**

- [ ] **3+ industry trends?** Count the trends listed.
- [ ] **In-demand skills list?** Are technical and soft skills separated?
- [ ] **Competitor landscape?** Are specific companies or players named?
- [ ] **Opportunity areas?** Do they connect to YOUR strengths from F1?
- [ ] **3+ source citations?** Are specific sources referenced throughout?

**If any check fails:** Go back to NotebookLM and ask follow-up questions.

Example follow-up:

```
Your response about industry trends didn't cite specific sources.
Please revise and add citations from the uploaded documents for each trend.
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
- **< 75%**: Strong acceleration—patterns from F1 transferred well
- **75-100%**: Moderate acceleration—some patterns transferred
- **> 100%**: F2 took longer—new tool learning overhead

**Note in TIME_TRACKER.md what transferred from F1:**
- Structured prompting approach
- Output validation against quality gates
- Iterative refinement when output was incomplete

## What You Built

You now have:

1. **Market intelligence brief** in `outputs/f2-market-brief.md`
2. **Source documentation** in `sources-list.md`
3. **First acceleration measurement** in TIME_TRACKER.md

This output feeds Feature 3 (Content Strategy Generator). Your market trends and skill demands inform what content topics will resonate with your target audience.

## Try With AI

Get feedback on your market research before moving to Feature 3:

**Prompt 1: Coverage Check**

In NotebookLM (or Gemini App), ask:

```
Review this market intelligence brief:

[Paste your f2-market-brief.md content]

Questions:
1. Are there obvious gaps in the market research? What topics should I research more?
2. Are the opportunity areas specific enough to act on?
3. What additional sources would strengthen this analysis?
```

**Observe:** NotebookLM may suggest gaps—like missing competitor analysis or thin skill data.

**Prompt 2: Source Quality Check**

```
I used these sources for my market research:
[Paste your sources-list.md]

Evaluate:
1. Are these sources credible and current?
2. Am I missing any category of source? (e.g., industry reports, thought leaders)
3. Which source contributed most to my insights?
```

**Update your brief** if you discover gaps worth addressing.

---

**Feature 2 complete.** Record your pattern notes in TIME_TRACKER.md:

```
## Pattern Notes - Feature 2
- Tool pattern: NotebookLM for multi-source synthesis (different from F1's Gemini App)
- Query pattern: Structured questions with citation requirements
- Validation pattern: Same checklist approach as F1
- Pipeline pattern: F1 output (strengths/gaps) became F2 input for opportunity mapping
```

Start Lesson 4: Feature 3 (Content Strategy Generator). Record your F3 start time. This feature synthesizes F1 + F2 outputs into actionable content strategy.
