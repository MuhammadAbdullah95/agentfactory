---
name: image-generator
description: Automate educational infographic generation using Playwright MCP to control Gemini.google.com image generation. Use when lesson content has embedded IMAGE GENERATION PROMPT comments that need to be converted into actual images and integrated into markdown.
allowed-tools: ["Read", "Write", "Bash", "mcp__playwright"]
metadata:
  category: "content-production"
  version: "1.0.0"
  workflow-phase: "visual-assets"
---

# Image Generator

## Overview

This skill automates the complete workflow of generating professional educational infographics from embedded prompts in lesson markdown files. It uses Playwright MCP to control a browser, navigate to Gemini.google.com, generate images iteratively with quality evaluation, download them to the correct location, and update the markdown to display the final images.

## When to Use

**Triggers:**
- Lesson markdown contains `<!-- VISUAL ASSET N: ... IMAGE GENERATION PROMPT: ... -->` HTML comments
- User asks to "generate images for lesson X"
- User says "create visuals" or "produce infographics"
- After fact-checking and visual auditing phases are complete

**Prerequisites:**
- Lesson must be fact-checked (no fabricated data)
- Visual asset prompts must be embedded in markdown (via auditor → generator workflow)
- User must have Google Gemini Pro subscription
- Playwright MCP must be configured and loaded

## Workflow Pattern

This is a **sequential workflow skill** with quality gates:

```
1. Scan lesson for IMAGE GENERATION PROMPT comments
2. For each prompt:
   a. Open Gemini.google.com
   b. Generate image
   c. Evaluate quality
   d. Iterate if needed
   e. Download when satisfied
   f. Update markdown
3. Verify all images render correctly
```

## Instructions

### Step 1: Scan Lesson for Visual Asset Prompts

1. Read the lesson markdown file provided by user
2. Search for HTML comments matching pattern: `<!-- VISUAL ASSET N: ... -->`
3. Extract for each:
   - Asset number (N)
   - Asset title
   - Complete IMAGE GENERATION PROMPT block
   - Suggested filename
   - Alt text
4. Create processing queue ordered by asset number

**Validation:**
- Verify each prompt has all required elements (layout, typography, colors, dimensions)
- Check filename suggestions are unique and follow naming conventions
- Confirm alt text is descriptive

### Step 2: Initialize Browser Session (One-Time)

1. Use Playwright MCP to navigate to `https://gemini.google.com/`
2. Wait for page load
3. **Pause and ask user to log in** (one-time authentication)
4. After login confirmed, proceed to image generation

**Browser setup:**
```
- Use persistent context to maintain login across images
- Set viewport to 1920x1080 for consistent rendering
- Enable downloads to track file saves
```

### Step 3: Generate Each Image (One Session Per Image)

**⚠️ CRITICAL WORKFLOW RULE**:
- **ONE image = ONE complete session** (generate → review → iterate → download)
- **After finalizing each image**: Click "New chat" button to start fresh session for next image
- **Never mix multiple images in one session**: Prevents context contamination and makes review cleaner

**Why this matters:**
- Long sessions consume excessive tokens and become hard to manage
- Fresh session for each image provides clean context
- Easier to verify spelling/layout when not mixed with previous attempts
- Maintains focus and reduces errors

For each prompt in the queue:

**3a. Start New Gemini Conversation**
1. Click "New chat" button (pen icon in left sidebar top)
2. Ensure clean conversation context
3. Wait for new chat to load completely

**3b. Access Image Generation Tool**
1. Look for tool selector/menu (usually bottom of input area)
2. Click "Generate image" or image generation option
3. Wait for tool to activate

**3c. Submit Prompt**
1. Paste the complete IMAGE GENERATION PROMPT into input
2. Submit (Enter or Send button)
3. Wait for generation to complete (watch for loading indicators)

**3d. CRITICAL: Verify Image IMMEDIATELY (Before Download)**

**⚠️ MANDATORY STEP**: Use `browser_snapshot` or `browser_take_screenshot` to VIEW the generated image BEFORE downloading.

**Why this is critical:**
- Gemini may misspell words even when prompted correctly
- Visual proportions may be incorrect despite explicit instructions
- Issues are easier to fix BEFORE downloading and moving to next image
- Prevents wasted iterations and file management overhead

**Verification checklist:**
- ✅ **Spelling accuracy**: Check EVERY word, especially proper nouns (company names, technical terms)
- ✅ **Text accuracy**: All numbers, labels, titles match prompt exactly
- ✅ **Layout**: Grid structure, spacing, alignment correct
- ✅ **Typography**: Font sizes appear correct, text readable
- ✅ **Colors**: Visual colors match specified hex codes (approximate)
- ✅ **Visual hierarchy**: Primary elements prominent, secondary subdued
- ✅ **Overall quality**: Professional, clean, no artifacts

**Quality decision tree:**
- **CRITICAL issues** (misspellings, wrong numbers, missing elements): Regenerate with refined prompt
- **MAJOR issues** (poor layout, wrong colors): Refine prompt, regenerate
- **MINOR issues** (slight spacing off): Accept if otherwise excellent
- **PERFECT**: Proceed to download

**3e. Refine if Needed**

**IMPORTANT SESSION MANAGEMENT**:
- For each image, use a SINGLE browser session from start to completion
- Once image is finalized and downloaded, START NEW SESSION for next image (click "New chat" button)
- Prevents context contamination and makes verification cleaner

If issues found:
1. **DO NOT DOWNLOAD YET** - Stay in same session
2. Analyze what went wrong (spelling? text rendering? layout? color accuracy?)
3. Adjust prompt strategy based on issue type:

   **Spelling/Text Issues** (MOST COMMON):
   - ❌ Avoid: Generic instruction like "Spell X correctly"
   - ✅ Effective: Spell word letter-by-letter: "Combinator (spelled: C-O-M-B-I-N-A-T-O-R)"
   - ✅ Effective: Break text into explicit parts: "The letter Y, then space, then word 'Combinator', then space, then 'Winter 2025'"
   - ✅ Effective: Use simpler/abbreviated forms: "YC W25" instead of full name

   **Layout/Proportion Issues**:
   - ❌ Avoid: Pixel-perfect specifications (Gemini struggles with exact measurements)
   - ✅ Effective: Use conceptual comparisons: "dramatically shorter - like comparing a full year to a single month"
   - ✅ Effective: Text-based designs instead of visual proportions: "VS" comparison instead of bars
   - ✅ Effective: Explicit ratio labels: "180x faster" instead of relying on bar length

   **Color Issues**:
   - ✅ Emphasize hex codes: "Use EXACT color #FF6B35"
   - ✅ Reference common colors: "orange (like #FF6B35) or green"

4. Ask Gemini to regenerate with refined prompt **in same conversation**
5. **Verify again immediately** with screenshot
6. Re-evaluate (max 3-4 iterations per image)
7. If still failing after 4 iterations, try **completely different visual approach**:
   - Numbers instead of grids
   - Text-based instead of visual proportions
   - "VS" comparison instead of charts

**3f. Download When Satisfied**

1. Right-click on generated image
2. Select "Save image as..."
3. Navigate to: `book-source/static/img/part-1/chapter-{N}/`
4. Use suggested filename from prompt (e.g., `yc-w25-ai-generated-code-stats.png`)
5. Verify download completes

**3g. Validate Teaching Effectiveness (Post-Generation - CRITICAL)**

After downloading image, verify it achieves **pedagogical goal** (not just technical quality):

**Self-Evaluation Questions**:

1. **< 5 Second Understanding Test**
   - Can you grasp the key concept in under 5 seconds by looking at the image?
   - ✅ PASS: Immediate comprehension of pattern/relationship
   - ❌ FAIL: Requires 10+ seconds to understand or repeated viewing

2. **Teaching vs. Showing Test**
   - Does this image TEACH a pattern/concept, or just SHOW data?
   - ✅ PASS: Reveals relationship, structure, or causality not obvious from text
   - ❌ FAIL: Restates data already clear in text (decorative, not pedagogical)

3. **Message Clarity Test**
   - Can you state in ONE sentence what this image teaches?
   - ✅ PASS: Clear teaching goal (e.g., "This teaches that value compounds at scale")
   - ❌ FAIL: Vague description (e.g., "This shows statistics")

4. **Cognitive Load Test**
   - Does this image REDUCE cognitive load, or just add visual clutter?
   - ✅ PASS: Makes dense content scannable and graspable
   - ❌ FAIL: Adds complexity without improving comprehension

**Evaluation Outcome**:
- ✅ **PASS (HIGH TEACHING VALUE)**: Proceed to markdown integration
- 🟡 **CONDITIONAL (MEDIUM VALUE)**: Consider simplification or text alternative
- ❌ **FAIL (LOW VALUE)**: Flag for redesign or removal - document why

**If FAIL**:
1. Document specific teaching failure (what doesn't work)
2. Flag in completion report with recommendation
3. DO NOT integrate into markdown yet
4. Suggest either:
   - Redesign prompt to better teach concept
   - Remove visual (text sufficient)
   - Replace with simpler diagram

**Example Evaluations**:

✅ **PASS**: Economic Calculation Flow Diagram
- **< 5 sec test**: ✅ Arrows show causality immediately (30M × $100K → $3T)
- **Teaching test**: ✅ Reveals multiplication structure (not just final number)
- **Message**: "Developer value compounds at scale through multiplication"
- **Cognitive load**: ✅ Makes abstract calculation concrete
- **Verdict**: HIGH VALUE - integrate

❌ **FAIL**: Generic Statistics Bar Chart
- **< 5 sec test**: ✅ Can read bars quickly
- **Teaching test**: ❌ Just displays numbers already in text
- **Message**: "Shows that X is bigger than Y" (fact, not concept)
- **Cognitive load**: ❌ Doesn't reduce (text comparison already clear)
- **Verdict**: LOW VALUE - remove, text sufficient

### Step 4: Update Markdown

For each successfully generated image:

1. Read the lesson markdown file
2. Find the corresponding `<!-- VISUAL ASSET N: ... -->` HTML comment block
3. Replace entire comment block with:
   ```markdown
   ![{alt-text}](/img/part-1/chapter-{N}/{filename})
   ```
4. Preserve surrounding text exactly (no accidental edits)
5. Save updated markdown

**Example transformation:**
```markdown
<!-- VISUAL ASSET 1: YC Winter 2025 AI-Generated Code Infographic
IMAGE GENERATION PROMPT:
... (full prompt) ...
Filename: yc-w25-ai-generated-code-stats.png
Alt Text: Infographic showing 25% of Y Combinator...
-->
```

**Becomes:**
```markdown
![Infographic showing 25% of Y Combinator Winter 2025 startups had approximately 95% AI-generated codebases](/img/part-1/chapter-1/yc-w25-ai-generated-code-stats.png)
```

### Step 5: Verify Rendering (Optional but Recommended)

After all images processed:

1. Start Docusaurus dev server: `cd book-source && npm run start`
2. Navigate to the lesson in browser
3. Verify:
   - All images load correctly
   - Images are appropriately sized (not too large/small)
   - Alt text displays on hover
   - No broken image links
4. If issues: fix paths, regenerate if image quality poor

### Step 6: Create Completion Report

Generate summary report in `history/visual-assets/lesson-{N}-visual-assets-report.md`:

```markdown
# Visual Assets - Chapter {N}, Lesson {M}

**Status**: ✅ Complete
**Date**: {today}
**Total Assets**: {count}
**Iterations**: {total refinements needed}

## Generated Images

### VISUAL ASSET 1: {title}
- **Filename**: {filename}
- **Dimensions**: {1024x1024px or 1792x1024px}
- **Iterations**: {total number including failed approaches}
- **Issues encountered**:
  - Iteration 1: {specific problem - e.g., "Spelling: 'Cymbinator' instead of 'Combinator'"}
  - Iteration 2: {what was tried and result}
  - Iteration N: {final approach that worked}
- **Final quality**: {Excellent / Good / Acceptable}
- **Prompting strategy that worked**: {e.g., "Letter-by-letter spelling", "Text-based VS comparison", "Simplified abbreviation"}
- **✨ Teaching effectiveness**: {PASS / CONDITIONAL / FAIL}
  - **< 5 sec test**: {✅ / ❌}
  - **Teaching test**: {✅ teaches [concept] / ❌ shows [data]}
  - **Message**: "{one-sentence teaching goal}"
  - **Cognitive load**: {✅ reduces / ❌ neutral or increases}
  - **Recommendation**: {integrate / simplify / remove}
- **Notes**: {Any specific observations about what approaches failed vs. succeeded}

[Repeat for each asset]

## Quality Summary

- {X} images generated on first attempt
- {Y} images required refinement (1 iteration)
- {Z} images required multiple refinements (2+ iterations)
- Overall success rate: {X / total}%

## Notes

{any observations, challenges, or recommendations for future lessons}
```

## Error Handling

**Browser issues:**
- Page not loading: Retry navigation, check network
- Login expired: Ask user to re-authenticate
- Tool not appearing: Refresh page, try different chat

**Generation issues:**
- Timeout (>2 minutes): Prompt may be too complex, simplify
- Error message: Gemini may have content restrictions, rephrase
- Poor quality: Try different aspect ratio or simpler prompt

**File issues:**
- Directory doesn't exist: Create with `mkdir -p book-source/static/img/part-1/chapter-{N}/`
- Download fails: Check permissions, try manual download
- Image won't load in markdown: Verify path is correct (absolute from /static/)

## Playwright MCP Tools Reference

**Navigation:**
- `playwright_navigate(url)` - Go to URL
- `playwright_screenshot()` - Capture current page

**Interaction:**
- `playwright_click(selector)` - Click element
- `playwright_fill(selector, text)` - Type into input
- `playwright_evaluate(script)` - Run JavaScript

**Waiting:**
- Wait for selectors to appear before interacting
- Use `waitForLoadState: 'networkidle'` after navigation

## Examples

### Example 1: Generate Single Image

**User:** "Generate the YC infographic for lesson 1"

**Claude:**
1. Reads lesson 1 markdown
2. Finds VISUAL ASSET 1 comment with prompt
3. Opens Gemini.google.com
4. Generates image with embedded prompt
5. Evaluates: Text looks good, layout correct, colors match
6. Downloads as `yc-w25-ai-generated-code-stats.png`
7. Updates markdown replacing comment with `![...](path)`
8. Confirms: "✅ Generated 1 image for Lesson 1. Image saved and markdown updated."

### Example 2: Generate All Images for Lesson

**User:** "Generate all visuals for Chapter 1, Lesson 1"

**Claude:**
1. Scans lesson, finds 3 VISUAL ASSET prompts
2. Opens Gemini, user logs in
3. **Asset 1:** Generates, evaluates, downloads
4. **Asset 2:** Generates, finds text too small, refines prompt, regenerates, downloads
5. **Asset 3:** Generates, evaluates, downloads
6. Updates markdown replacing all 3 comment blocks
7. Creates completion report in history/
8. Confirms: "✅ Generated 3 images for Lesson 1. 2 on first attempt, 1 required refinement. All images integrated into markdown."

### Example 3: Quality Iteration

**User:** "Generate the statistics dashboard"

**Claude:**
1. Generates image
2. Evaluates: Numbers correct ✅, layout good ✅, but card labels too small ❌
3. Refines prompt in same chat: "Make card labels 16pt instead of 14pt for better readability"
4. Regenerates
5. Evaluates: All criteria met ✅
6. Downloads and integrates
7. Confirms: "✅ Dashboard generated (1 refinement for text size). Image integrated."

## Quality Standards

### The 99% Quality Mindset

**CRITICAL PRINCIPLE**: Gemini CAN get it right. If an image has issues, it's the PROMPT that needs improvement, not a limitation of the tool.

**Mindset shift:**
- ❌ "Gemini can't spell 'Combinator' correctly, let's accept the typo"
- ✅ "My prompt wasn't explicit enough. Let me try letter-by-letter spelling."

- ❌ "Gemini can't do precise proportions, let's use a different tool"
- ✅ "My approach using bars didn't work. Let me try text-based 'VS' comparison."

- ❌ "After 3 tries it's still wrong, time to give up"
- ✅ "After 3 tries with same approach, time to try DIFFERENT approach."

**Quality target: 99%** - The only acceptable reason to not achieve perfect output is time constraints, never "the tool can't do it."

**Evidence from this project:**
- YC "Combinator" spelling: Failed 3 times with generic prompts, succeeded immediately with letter-by-letter spelling
- Timeline bar chart: Failed 3 times with precise measurements, succeeded immediately with "VS" text comparison
- Success rate when using RIGHT prompting strategy: ~95-100%

**Always prioritize:**
1. **Factual accuracy** - Numbers must match source data exactly
2. **Spelling perfection** - Every word must be spelled correctly (use letter-by-letter if needed)
3. **Readability** - Text must be legible at book size
4. **Professional aesthetics** - Clean, modern, publication-quality
5. **Brand consistency** - Colors, fonts match design system

**Never accept:**
- Wrong numbers or data
- Misspellings or typos
- Illegible text
- Poor layout that confuses rather than clarifies
- Low-resolution or pixelated images

**When in doubt:**
- Iterate up to 3-4 times per image WITH SAME APPROACH
- If still not acceptable after 3-4 attempts, try COMPLETELY DIFFERENT APPROACH
- Document what approaches failed and what finally worked in completion report
- Share learnings to improve future prompting strategies

## Progressive Disclosure

- **Metadata** (~100 words): Skill automates Gemini image generation via browser
- **SKILL.md** (~1.5k words): Complete workflow from prompt to integrated image
- **No bundled resources needed**: All logic in SKILL.md, uses Playwright MCP tools directly

---

**Ready to generate images.** Invoke with: "Generate images for lesson {N}" or "Create visuals for {lesson-file.md}"
