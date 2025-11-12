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

### Step 3: Generate Each Image (Iterative Loop)

For each prompt in the queue:

**3a. Start New Gemini Conversation**
1. Click "New chat" button (if not first image)
2. Ensure clean conversation context

**3b. Access Image Generation Tool**
1. Look for tool selector/menu (usually bottom of input area)
2. Click "Generate image" or image generation option
3. Wait for tool to activate

**3c. Submit Prompt**
1. Paste the complete IMAGE GENERATION PROMPT into input
2. Submit (Enter or Send button)
3. Wait for generation to complete (watch for loading indicators)

**3d. Evaluate Quality**

Take screenshot and analyze against criteria:
- ✅ **Text accuracy**: All numbers, labels, titles match prompt exactly
- ✅ **Layout**: Grid structure, spacing, alignment correct
- ✅ **Typography**: Font sizes appear correct, text readable
- ✅ **Colors**: Visual colors match specified hex codes (approximate)
- ✅ **Visual hierarchy**: Primary elements prominent, secondary subdued
- ✅ **Overall quality**: Professional, clean, no artifacts

**Quality decision tree:**
- **CRITICAL issues** (wrong numbers, missing elements): Regenerate with refined prompt
- **MAJOR issues** (poor layout, wrong colors): Refine prompt, regenerate
- **MINOR issues** (slight spacing off): Accept if otherwise excellent
- **PERFECT**: Proceed to download

**3e. Refine if Needed**

If issues found:
1. Analyze what went wrong (text rendering? layout interpretation? color accuracy?)
2. Adjust prompt in same conversation:
   - Text issues: Simplify labels, reduce character count, make more explicit
   - Layout issues: Add explicit positioning, spacing values
   - Color issues: Emphasize hex codes, add "use exact colors"
3. Ask Gemini to regenerate with refinements
4. Re-evaluate (max 3 iterations per image)

**3f. Download When Satisfied**

1. Right-click on generated image
2. Select "Save image as..."
3. Navigate to: `book-source/static/img/part-1/chapter-{N}/`
4. Use suggested filename from prompt (e.g., `yc-w25-ai-generated-code-stats.png`)
5. Verify download completes

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
- **Iterations**: {1 or 2 or 3}
- **Issues encountered**: {none / text rendering / layout / colors}
- **Final quality**: {excellent / good / acceptable}

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

**Always prioritize:**
1. **Factual accuracy** - Numbers must match source data exactly
2. **Readability** - Text must be legible at book size
3. **Professional aesthetics** - Clean, modern, publication-quality
4. **Brand consistency** - Colors, fonts match design system

**Never accept:**
- Wrong numbers or data
- Illegible text
- Poor layout that confuses rather than clarifies
- Low-resolution or pixelated images

**When in doubt:**
- Iterate up to 3 times per image
- If still not acceptable after 3 attempts, flag for manual review
- Document issues in completion report

## Progressive Disclosure

- **Metadata** (~100 words): Skill automates Gemini image generation via browser
- **SKILL.md** (~1.5k words): Complete workflow from prompt to integrated image
- **No bundled resources needed**: All logic in SKILL.md, uses Playwright MCP tools directly

---

**Ready to generate images.** Invoke with: "Generate images for lesson {N}" or "Create visuals for {lesson-file.md}"
