---
sidebar_position: 2
title: "Feature 1: Personal Brand Profiler"
chapter: 15
lesson: 2
duration_minutes: 60

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 4"
layer_progression: "L4 capstone - baseline measurement with Gemini App"
layer_4_capstone: "Brand analysis using AI tool, establishing acceleration baseline"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "AI-Assisted Brand Analysis"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can use Gemini App to analyze personal profile data and extract structured insights"

  - name: "Prompt Engineering for Analysis"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Communication"
    measurable_at_this_level: "Student can craft prompts that produce structured, actionable AI outputs"

  - name: "Output Validation Against Specification"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can verify AI output meets quality gates from constitution"

  - name: "Baseline Time Measurement"
    proficiency_level: "A2"
    category: "Soft"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can track feature build time for acceleration comparison"

learning_objectives:
  - objective: "Use Gemini App to analyze personal profile data"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Brand analysis output contains required sections from constitution"

  - objective: "Validate AI output against constitution quality gates"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Output cites specific profile phrases as evidence"

  - objective: "Establish baseline time for intelligence accumulation measurement"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "TIME_TRACKER.md updated with F1 duration"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (Gemini App usage, structured prompting, brand analysis, output validation, quality gates, baseline measurement) within B1 limit ✓"

differentiation:
  extension_for_advanced: "Add competitive positioning section comparing to peers in industry"
  remedial_for_struggling: "Use provided prompt templates exactly; focus on output validation"

generated_by: "content-implementer v3.0.0"
source_spec: "specs/015-chapter-15-redesign/spec.md"
created: "2025-11-25"
last_modified: "2025-11-25"
git_author: "Claude Code"
workflow: "/sp.loopflow.v2"
version: "3.0.0"
---

# Feature 1: Personal Brand Profiler

**This is your baseline.** You're analyzing your professional profile using Gemini App to produce a structured brand analysis. You'll measure how long this takes—then build Features 2-4 and compare acceleration.

**START YOUR TIMER NOW.** Record in TIME_TRACKER.md:

```
F1: Personal Brand Profiler | Start: [current time] | End: | Duration: |
```

## Review Your Specification

Open your constitution and review Feature 1's quality gates:

```bash
cat .specify/memory/constitution.md | grep -A 10 "Personal Brand Profiler"
```

**Required outputs:**
- 3+ core strengths identified
- 2+ brand gaps (areas needing development)
- Positioning statement (1-2 sentences)
- Differentiation opportunities
- Confidence score (0-100)

**Quality gate:** Must cite specific phrases from your profile as evidence for each strength.

## Open Gemini App

Go to **gemini.google.com** in your browser.

If you're not logged in, sign in with your Google account.

Start a new conversation (click "+ New chat" if needed).

## Create the Analysis Prompt

You'll build a structured prompt that tells Gemini exactly what to produce.

**Copy this prompt template and fill in your data:**

```
You are a personal branding expert analyzing a professional's online presence.

## My Profile Data

### LinkedIn About Section:
[PASTE YOUR LINKEDIN ABOUT HERE]

### GitHub Bio:
[PASTE YOUR GITHUB BIO HERE]

### Portfolio Description:
[PASTE YOUR PORTFOLIO DESCRIPTION HERE - or write "No portfolio" if you don't have one]

### Target Role/Industry:
[PASTE YOUR TARGET ROLE/INDUSTRY]

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

**Before sending:** Verify you've replaced all `[PASTE...]` placeholders with YOUR actual data.

## Run the Analysis

Paste your complete prompt into Gemini App and send it.

**Wait for the full response.** Gemini will produce a structured analysis. This typically takes 15-30 seconds.

## Validate Against Quality Gates

Check your output against the constitution's quality gates:

**Checklist:**

- [ ] **3+ core strengths?** Count the strengths listed. Must be 3 or more.
- [ ] **Evidence citations?** Each strength must include a quoted phrase from your profile.
- [ ] **2+ brand gaps?** Count the gaps listed. Must be 2 or more.
- [ ] **Positioning statement?** Is there a 1-2 sentence positioning statement?
- [ ] **Differentiation opportunities?** Are there 3-5 specific suggestions?
- [ ] **Confidence score?** Is there a 0-100 score with reasoning?

**If any check fails:** Ask Gemini to fix it.

Example follow-up prompt:
```
Your analysis is missing evidence citations for the strengths.
Please revise strength #2 to include a specific quote from my profile that demonstrates it.
```

## Save Your Output

Once validated, save the analysis:

```bash
mkdir -p outputs
touch outputs/f1-brand-analysis.md
```

Copy Gemini's response into this file. Add a header:

```markdown
# Feature 1: Personal Brand Analysis
Generated: [today's date]
Tool: Gemini App (gemini.google.com)
Input: my-profile-data.md

---

[PASTE GEMINI'S COMPLETE RESPONSE HERE]
```

**Verify the file:**

```bash
cat outputs/f1-brand-analysis.md
```

## Quality Gate Verification

Run a final check against your constitution:

**Constitution says:** "Must cite specific phrases from your profile as evidence for each strength."

**Your output:** Open `f1-brand-analysis.md` and verify each strength has a quoted evidence phrase.

**If missing:** Go back to Gemini and ask for revisions until all quality gates pass.

## Stop Your Timer

Record your end time in TIME_TRACKER.md:

```
F1: Personal Brand Profiler | Start: [time] | End: [current time] | Duration: [calculate] |
```

**Example:** If you started at 2:00 PM and finished at 2:45 PM, duration = 45 minutes.

This is your **baseline**. Feature 4 should take less than 50% of this time.

## What You Built

You now have:

1. **Structured brand analysis** in `outputs/f1-brand-analysis.md`
2. **Validated output** that meets constitution quality gates
3. **Baseline time** for measuring intelligence accumulation

This output feeds Feature 2 (Market Intelligence Scanner). Your strengths and gaps inform what market opportunities to research.

## Try With AI

Before moving to Feature 2, get feedback on your analysis:

**Prompt 1: Quality Check**

In Gemini App, ask:

```
Review this brand analysis I just created:

[Paste your f1-brand-analysis.md content]

Questions:
1. Is the positioning statement specific enough to differentiate me?
2. Are the brand gaps actionable—can I actually fix them?
3. What's missing that would make this analysis more useful for content planning?
```

**Observe:** Gemini will likely suggest making the positioning statement more specific. This is common—first drafts tend toward generic.

**Prompt 2: Iteration**

If Gemini suggests improvements:

```
Based on your feedback, revise my positioning statement to be more specific.
Current: "[your current positioning statement]"
My target industry: [your target]
Make it concrete and differentiated.
```

**Update your `f1-brand-analysis.md`** with the improved positioning statement.

---

**Feature 1 complete.** Record your pattern notes in TIME_TRACKER.md:

```
## Pattern Notes - Feature 1
- Prompting pattern: Structured request with specific output format
- Validation pattern: Checklist against constitution quality gates
- Iteration pattern: Follow-up prompts to fix missing elements
```

Start Lesson 3: Feature 2 (Market Intelligence Scanner with NotebookLM). Record your F2 start time.
