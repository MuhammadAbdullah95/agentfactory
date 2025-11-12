---
name: visual-asset-workflow
description: Analyze fact-checked lesson content to identify visual asset opportunities (statistics, timelines, comparisons), then generate complete AI image generation prompts and embed them in markdown as HTML comments. Use after fact-checking is complete and before image generation. Combines auditor and prompt generator logic into single workflow.
allowed-tools: ["Read", "Write"]
metadata:
  category: "content-production"
  version: "1.0.0"
  workflow-phase: "visual-planning"
---

# Visual Asset Workflow

## Overview

This skill automates the complete visual asset planning workflow by analyzing lesson content to identify where visuals would reduce cognitive load, then generating publication-ready AI image generation prompts for each identified opportunity. It outputs lesson markdown with embedded prompts ready for the `image-generator` skill.

## When to Use

**Triggers:**
- User says "plan visuals for lesson X"
- User asks "what images does this lesson need?"
- User requests "create image prompts for [lesson]"
- After fact-checking phase, before image generation

**Prerequisites:**
- Lesson content must be fact-checked (no fabricated data to visualize)
- Lesson is in final or near-final content state
- No existing embedded image prompts (or user wants to regenerate)

## Workflow Pattern

This is a **sequential workflow skill** combining two phases:

```
Phase 1: AUDIT
→ Scan lesson for visual opportunities
→ Identify patterns (statistics, timelines, comparisons, processes)
→ Assess cognitive load impact
→ Prioritize opportunities

Phase 2: GENERATE
→ For each opportunity, create detailed image prompt
→ Embed prompts as HTML comments in markdown
→ Create audit report
```

## Instructions

### Phase 1: Audit Lesson for Visual Opportunities

#### Step 1: Read and Analyze Lesson Content

1. Read the complete lesson markdown file
2. Identify content patterns that benefit from visualization (see **Reference: Visual Opportunity Patterns** below)
3. For each pattern found, assess:
   - **Cognitive load impact**: Does visual REDUCE or INCREASE mental effort?
   - **Information density**: Is text too dense to scan easily?
   - **Spatial relationships**: Would layout/structure clarify meaning?

#### Step 2: Categorize Identified Opportunities

For each opportunity, classify by visual type:

**High-Priority Opportunities** (always visualize):
- ✅ **Statistics Dashboard**: 3-6 discrete metrics/numbers in proximity
- ✅ **Timeline/Evolution**: Progression across stages or time periods
- ✅ **Comparison Grid**: Before/after or A vs B comparisons
- ✅ **Process Map**: Sequential steps or workflows (3+ steps)

**Medium-Priority Opportunities** (consider):
- 🟡 **Hierarchy Diagram**: Nested relationships or structures
- 🟡 **Concept Illustration**: Abstract ideas needing metaphor

**Skip** (text is better):
- ❌ Single statistics (just one number/claim)
- ❌ Narrative examples (storytelling works in text)
- ❌ Short lists (2-3 simple items)
- ❌ Code examples (code blocks are visual enough)

#### Step 3: Assess Cognitive Load Impact

For each identified opportunity, apply this test:

**Question**: "Would a reader need to re-read this section 2-3 times to understand?"
- **Yes** → Visual likely helps (REDUCE cognitive load)
- **No** → Text is already clear (skip visual)

**Additional heuristic**: If you can't scan and grasp the key point in <5 seconds, a visual would help.

#### Step 4: Prioritize and Limit Density

**Maximum visual density**: 1 visual per 2-3 pages (~600-900 words)

If more opportunities identified than this limit:
1. Rank by comprehension impact (which visual helps most?)
2. Keep only highest-priority visuals
3. Consider combining related visuals (e.g., two timelines → one comprehensive timeline)

#### Step 5: Document Audit Results

Create mental list (or written notes) with:
- Asset number (1, 2, 3...)
- Visual type (dashboard, timeline, comparison, etc.)
- Placement location (line number or section heading)
- Content to visualize (exact data/text)
- Purpose statement (what comprehension goal this achieves)
- Priority (HIGH, MEDIUM, LOW)

### Phase 2: Generate Image Prompts for Each Opportunity

For each identified opportunity from Phase 1:

#### Step 6: Choose Visual Format

Based on visual type, select appropriate format and aspect ratio:

- **Statistics Dashboard**: 2x2 or 3x2 card grid, 16:9 aspect ratio
- **Timeline/Evolution**: Horizontal progression, 16:9 or 21:9 aspect ratio
- **Comparison**: Split-screen or side-by-side, 16:9 aspect ratio
- **Process Map**: Winding path or numbered steps, 16:9 aspect ratio
- **Single Metric**: Centered composition, 1:1 aspect ratio

#### Step 7: Apply Design System Standards

All prompts must use the book's design system:

**Typography**:
- Font family: Roboto
- Headings: Bold or Medium
- Body: Regular
- Metrics: 72pt Bold
- Labels: 14-24pt Regular
- Captions: 10-14pt Regular or Light

**Color Palette**:
- Primary accent: Orange (#FF6B35) or Blue (#0066FF)
- Secondary accent: Teal (#00B4D8)
- Background: White (#FFFFFF) or Light Gray (#F8F9FA)
- Text primary: Dark Gray (#1A1A1A)
- Text secondary: Medium Gray (#666666)
- Text tertiary: Light Gray (#999999)

**Visual Style**:
- Modern tech publication aesthetic (TechCrunch, a16z, Stripe)
- Flat design with subtle shadows (0px 2px 8px rgba(0,0,0,0.08))
- Minimal line art icons (2-3px stroke weight)
- Generous white space
- Clean grid systems

#### Step 8: Write Structured Image Generation Prompt

For each visual asset, create a complete prompt following this template:

```
VISUAL ASSET {N}: {Descriptive Title}

IMAGE GENERATION PROMPT:

{One-sentence description of what this visual shows}

Layout: {Grid/structure with exact specifications}
- {Detailed element breakdown with positioning}
- {Spacing, margins, alignment}

Typography:
- {Primary text specs with sizes, weights, colors with hex codes}
- {Secondary text specs}
- {Label/caption specs}

Color Palette:
- Background: {Color name} ({Hex code})
- Primary accent: {Color name} ({Hex code})
- Secondary: {Color name} ({Hex code})
- Text primary: {Hex code}
- Text secondary: {Hex code}
- Text tertiary: {Hex code}

Visual Elements:
- {Icons/graphics with style, size, stroke weight, color}
- {Shadows/depth specifications}
- {Spacing/padding values}

Content:
{Exact text and data to include, broken down by element}
- Element 1: {specific content}
- Element 2: {specific content}
- ...

Style Reference: {Specific design system or publication aesthetic}

Quality: professional, high-quality, publication-ready, clean, modern, editorial

Dimensions: {Aspect ratio} ({pixel dimensions})

Filename: {descriptive-kebab-case-name.png}
Alt Text: {Descriptive alt text for accessibility, 1-2 sentences}
```

**Critical requirements**:
- ✅ All data/numbers are factually accurate to lesson content
- ✅ Layout structure is precisely defined (not vague like "arrange nicely")
- ✅ Colors include hex codes (not "blue" → "#0066FF")
- ✅ Typography includes exact sizes and weights (not "large text" → "72pt Roboto Bold")
- ✅ Visual hierarchy is explicit (primary, secondary, tertiary clearly defined)
- ✅ Filename is descriptive and follows kebab-case convention
- ✅ Alt text is complete and accessible

#### Step 9: Embed Prompts in Lesson Markdown

1. Read the lesson markdown file
2. For each visual asset, find the optimal insertion point:
   - **Statistics**: After the statistics list/paragraph
   - **Timeline**: After paragraph describing progression
   - **Comparison**: After comparison discussion
   - **Process**: Before or after process description
3. Insert the complete prompt as HTML comment:
   ```markdown
   <!-- VISUAL ASSET 1: {Title}
   IMAGE GENERATION PROMPT:

   {complete prompt from Step 8}
   -->
   ```
4. Preserve all surrounding text exactly (no accidental edits)
5. Save updated lesson markdown

#### Step 10: Create Audit Report

Generate report in `history/visual-assets/lesson-{N}-audit-report.md`:

```markdown
# Visual Asset Audit - Chapter {N}, Lesson {M}

**Date**: {today}
**Lesson**: {lesson-title}
**Total Opportunities Identified**: {count}
**Prompts Generated**: {count}
**Visual Density**: {X} visuals per ~{Y} words

---

## Identified Visual Opportunities

### VISUAL ASSET 1: {Title}
- **Type**: {Dashboard/Timeline/Comparison/Process/etc.}
- **Location**: Line {N} (after "{first few words of section...}")
- **Content**: {brief description of what's visualized}
- **Purpose**: {comprehension goal}
- **Priority**: {HIGH/MEDIUM/LOW}
- **Cognitive Load Impact**: REDUCES - {brief justification}

[Repeat for each asset]

---

## Audit Summary

**High-Priority Assets**: {count}
**Medium-Priority Assets**: {count}
**Skipped Opportunities**: {count} ({why: redundant / text clearer / low impact})

**Overall Assessment**: {1-2 sentences on lesson's visual needs}

---

## Next Steps

1. Review embedded prompts in lesson markdown
2. Adjust/refine any prompts if needed
3. Invoke `image-generator` skill to generate actual images
4. Verify images integrate correctly into lesson

---

**Prompts embedded in**: `{path/to/lesson.md}`
**Ready for image generation**: ✅ Yes
```

### Phase 3: Quality Validation

Before finalizing, verify:

- [ ] All prompts are embedded as HTML comments (not visible in rendered markdown)
- [ ] Each prompt includes all required sections (Layout, Typography, Colors, Content, etc.)
- [ ] All data/numbers match lesson content exactly (no fabrication)
- [ ] Filenames are unique and descriptive
- [ ] Alt text is complete and accessible
- [ ] Visual density is appropriate (not too many visuals)
- [ ] Audit report created in `history/visual-assets/`

## Reference: Visual Opportunity Patterns

### Pattern 1: Multiple Statistics (High Priority)

**Identify when**:
- 3+ numbers/percentages in close proximity
- Statistics presented as bullet list
- Dense numerical data in paragraph

**Example**:
```
- 84% of developers using AI tools
- $500M ARR in 2 months
- 75% daily usage
- 7.5% improvement
```

**Visual solution**: Statistics dashboard (2x2 or 3x2 card grid)

---

### Pattern 2: Temporal Progression (High Priority)

**Identify when**:
- Text describes stages, eras, or evolution
- Before/after comparison across time
- Sequential progression mentioned

**Example**:
```
Previous transitions took 10-15 years.
Current AI revolution happening in months.
```

**Visual solution**: Timeline or horizontal bar chart

---

### Pattern 3: A vs B Comparison (High Priority)

**Identify when**:
- Explicit comparison (traditional vs new, old vs modern)
- Contrasting approaches or methodologies
- Table comparing two options

**Example**:
```
Traditional: 80% coding, 20% design
AI-era: 20% specification, 80% oversight
```

**Visual solution**: Split-screen comparison or side-by-side grid

---

### Pattern 4: Sequential Process (Medium Priority)

**Identify when**:
- Numbered steps (3+ steps)
- Workflow or procedure described
- Journey or roadmap mentioned

**Example**:
```
1. Specification → 2. AI generation → 3. Validation → 4. Ship
```

**Visual solution**: Process map with arrows or journey path

---

### Pattern 5: Nested Hierarchy (Medium Priority)

**Identify when**:
- Parent-child relationships
- Organizational structure
- Category breakdowns

**Visual solution**: Tree diagram or nested boxes

## Examples

### Example 1: Statistics Dashboard

**Input**: Lesson with 4 statistics in bullet list

**Output**:
```markdown
The numbers tell the story:
- 84% of developers using AI tools
- $500M Claude Code ARR
- 75% professionals using daily
- 7.5% better documentation

<!-- VISUAL ASSET 1: AI Adoption Statistics Dashboard

IMAGE GENERATION PROMPT:

Professional statistics dashboard showing AI development tool adoption metrics.

Layout: 2x2 grid of metric cards, 1792x1024px (16:9 aspect ratio).
- Overall background: Light Gray (#F8F9FA)
- Grid: 24px gaps between cards, 48px margin from edges
- Each card: 832x448px with 32px internal padding, 8px border-radius

[... complete detailed prompt ...]

Filename: ai-adoption-statistics-2025.png
Alt Text: Dashboard showing four key AI adoption statistics...
-->
```

### Example 2: Timeline

**Input**: Lesson describing historical vs current adoption speeds

**Output**: Complete timeline prompt embedded at optimal location

### Example 3: Skip Low-Priority

**Input**: Single statistic "84% of developers"

**Action**: Skip (one number doesn't need visualization, text emphasis sufficient)

**Rationale**: Low cognitive load, text is clear, visual would be redundant

## Progressive Disclosure

- **Metadata** (~100 words): Combines auditor + generator into single workflow
- **SKILL.md** (~2k words): Complete audit → generate → embed workflow
- **No bundled resources**: All logic self-contained in SKILL.md

---

**Ready to plan visual assets.** Invoke with: "Plan visuals for lesson {N}" or "Create image prompts for {lesson-file.md}"
