---
sidebar_position: 3
chapter: 7
lesson: 3
layer: L2
title: "The Organization Workflow"
description: "Collaborate with Claude Code to design categorization rules, document them for reuse, and test on one file before scaling"
duration_minutes: 25

skills:
  - name: "Collaborative Rule Design"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Work with AI to design categorization rules through iterative refinement"

  - name: "State Persistence"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Document rules in rules.md for future reuse"

  - name: "Single-File Testing"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Test categorization on one file before batch processing"

  - name: "Iterative Refinement"
    proficiency_level: "A2"
    category: "Soft"
    bloom_level: "Evaluate"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Refine AI suggestions based on personal requirements"

learning_objectives:
  - objective: "Collaborate with Claude Code to analyze files and propose categorization"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student engages in multi-turn conversation refining categories"

  - objective: "Refine AI-proposed categories based on personal needs"
    proficiency_level: "A2"
    bloom_level: "Evaluate"
    assessment_method: "Student modifies initial suggestion with custom categories"

  - objective: "Create rules.md documenting categorization logic"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Document exists with complete extension-to-directory mapping"

  - objective: "Test categorization on ONE file before batch processing"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student verifies single file moved correctly"

  - objective: "Execute batch organization with verification summary"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student reviews summary and confirms results"

cognitive_load:
  new_concepts: 4
  concepts_list:
    - "Collaborative rule design (propose-refine-iterate pattern)"
    - "State persistence (rules.md for reusable logic)"
    - "Single-file testing (decomposition before scaling)"
    - "Batch execution with verification (trust but verify)"
  assessment: "4 concepts at A2 limit"
---

# The Organization Workflow

Here's what beginners miss about working with General Agents. They think the agent should just "know" what to do. Experts know better. They design rules collaboratively, document them for reuse, and test before scaling.

This workflow teaches you something that applies far beyond file organization. When you work with General Agents on data categorization, content moderation, task routing, or any system that needs consistent rules, you'll use the same collaborative design pattern.

You've surveyed 500 files. You've created a backup. Now comes the hard question: where does each file actually go?

You could spend an hour creating folders and dragging files one by one. You could make random guesses about categories. Or you could have a conversation with Claude Code that turns your messy Downloads into a categorized system in minutes.

The difference isn't just speed. It's that you'll end up with documented rules you can reuse forever. You're not just organizing files. You're learning how to design systems with General Agent assistance.

---

## Prerequisites

This lesson builds on Lessons 1-2. You should have:

- Completed the survey workflow from Lesson 1 (you understand what's in your Downloads folder)
- Created a backup from Lesson 2 (your important files are safely copied)

If you skipped ahead, that's okay - just make sure you have a backup before organizing. The safety-first pattern protects you from mistakes.

---

## The Conversation

Open Claude Code and start the collaboration:

**You:**

> Help me organize my Downloads folder. Let's create a categorization system that works for my files.

**Claude Code:**

> I can see you have 487 files in ~/Downloads. Based on the extensions, here's what I'd suggest:
>
> | Category  | File Types          | Count |
> | --------- | ------------------- | ----- |
> | Documents | pdf, doc, docx, txt | 127   |
> | Images    | jpg, png, gif       | 89    |
> | Code      | py, js, html, css   | 34    |
> | Misc      | everything else     | 237   |
>
> Does this categorization work for you, or would you like to adjust it?

**You:**

> That's good, but I also want a separate folder for spreadsheets. xlsx and csv files should go there, not with documents.

**Claude Code:**

> Got it. Updated categories:
>
> | Category     | File Types          | Count |
> | ------------ | ------------------- | ----- |
> | Documents    | pdf, doc, docx, txt | 98    |
> | Spreadsheets | xlsx, csv           | 29    |
> | Images       | jpg, png, gif       | 89    |
> | Code         | py, js, html, css   | 34    |
> | Misc         | everything else     | 237   |
>
> Should I document these rules in a rules.md file so we can reuse them later?

**You:**

> Yes, create rules.md. Then test on ONE file first before doing all of them.

**Claude Code:**

> Created rules.md with the categorization logic and edge case handling.
>
> Now testing with a single file. Moving budget-2024.pdf to documents/...
>
> ```
> Moved: budget-2024.pdf → organized/documents/
> Verified: File exists in destination
> Verified: File no longer in source
> ```
>
> Test passed. Ready to proceed with the remaining 486 files?

**You:**

> Looks good. Now do the rest and show me a summary when done.

**Claude Code:**

> Organization complete. Here's the summary:
>
> | Category      | Files Moved |
> | ------------- | ----------- |
> | documents/    | 97          |
> | spreadsheets/ | 29          |
> | images/       | 89          |
> | code/         | 34          |
> | misc/         | 237         |
>
> **Total**: 486 files organized
>
> Updated ORGANIZER-LOG.md with the full activity history.
>
> Would you like me to show you any category in detail, or are we done?

---

## What Just Happened?

Look at what emerged from that conversation:

**Rules became a file.** Claude Code didn't just remember the categories. It created `rules.md`. Next week when your Downloads folder fills up again, the logic is already documented.

**You tested before scaling.** You said "test on ONE file first." That single instruction prevented potential chaos. If the test file had landed in the wrong folder, you'd know immediately.

**Verification happened automatically.** After moving the test file, Claude Code checked both source and destination. After the batch operation, it showed you a summary.

**The collaboration refined the result.** Claude Code proposed categories. You refined them (adding spreadsheets). Claude Code adapted. Neither of you could have reached this result alone. The AI didn't know you cared about spreadsheets, and you didn't want to manually design the whole system.

### The Agent's Toolkit: Organization Commands

The agent used these commands:

- **`mkdir`** - **m**a**k**e **dir**ectory - creates category folders (documents/, images/, etc.)
- **`mv`** - **m**o**v**e - relocates files from Downloads to organized folders
- **`cat`** - con**cat**enate (display) - shows you what's in rules.md
- **`ls`** - **l**i**s**t - verifies files landed in the right place

When the agent tested on one file first:

```bash
mv budget-2024.pdf organized/documents/    # Move the file
ls organized/documents/budget-2024.pdf     # Verify it arrived
ls ~/Downloads/budget-2024.pdf             # Verify it's gone from source
```

The single-file test uses the same `mv` command as the batch operation—just on one file. If something's wrong, you catch it early.

---

## The Pattern

Notice the structure of that conversation:

```
1. "Help me [goal]. Let's [approach]."
   → AI proposes initial solution

2. "That's good, but [refinement]."
   → You adjust based on your needs

3. "Document the rules so we can reuse them."
   → Logic becomes persistent state

4. "Test on ONE file first."
   → Small verification before scale

5. "Now do the rest and show me a summary."
   → Batch execution with observability
```

This pattern works for any organization task. The specific categories change. Maybe you're organizing photos by date, or code files by project. But the workflow stays the same.

---

## Your Workspace After This Lesson

Check what Claude Code created:

```bash
ls -la
```

**Output:**

```
drwxr-xr-x  backup/
-rw-r--r--  FILE-INVENTORY.md
-rw-r--r--  ORGANIZER-LOG.md
drwxr-xr-x  organized/
-rw-r--r--  rules.md
```

Examine the organized directory:

```bash
ls organized/
```

**Output:**

```
code  documents  images  misc  spreadsheets
```

Read your rules:

```bash
cat rules.md
```

**Output:**

```markdown
# File Organization Rules

## Categories

| Extension                     | Destination   |
| ----------------------------- | ------------- |
| .pdf, .doc, .docx, .txt       | documents/    |
| .xlsx, .csv                   | spreadsheets/ |
| .jpg, .png, .gif, .svg, .webp | images/       |
| .py, .js, .sh, .html, .css    | code/         |
| everything else               | misc/         |

## Edge Cases

- Unknown extension → misc/
- No extension → misc/
- Hidden files (starting with .) → skip
- Duplicate filename → append timestamp

## History

- Created: 2025-01-27
- Based on: FILE-INVENTORY.md analysis
- Customization: Spreadsheets separated from documents
```

Your organization logic is now permanent. The next time your Downloads fills up, you have documented rules ready to apply.

---

## Why This Works Better Than Solo Organizing

| Solo Approach                  | Collaborative Approach                 |
| ------------------------------ | -------------------------------------- |
| Make up categories as you go   | AI analyzes actual file types first    |
| Forget your logic next month   | Rules persisted in rules.md            |
| Move files one by one manually | Batch execution after single-file test |
| No record of what happened     | ORGANIZER-LOG.md tracks everything     |
| Mistakes affect all files      | Test catches problems before scale     |

The collaboration doesn't replace your judgment. It amplifies it. You decided spreadsheets needed their own category. The AI executed that decision across 486 files in seconds.

---

## Try It Yourself

**Reorganize your Desktop:**

Open Claude Code and try:

```
Help me organize my Desktop folder. Analyze what's there and suggest categories based on MY actual files, not generic categories.
```

Watch how the AI proposes categories specific to your content. A designer's Desktop will get different suggestions than a developer's.

**Create project-specific categories:**

```
I have a folder with project files mixed together. Help me categorize by project name (files often start with the project name like "acme-report.pdf" or "beta-design.png").
```

This shows how the same workflow adapts to different categorization logic. By extension, by name prefix, by date, or any pattern you define.

---

## What You Built

| Item                       | Location             | Purpose                              |
| -------------------------- | -------------------- | ------------------------------------ |
| `rules.md`                 | In `file-organizer/` | Reusable categorization logic        |
| `organized/`               | In `file-organizer/` | Five category directories with files |
| Updated `ORGANIZER-LOG.md` | In `file-organizer/` | Complete activity history            |

The rules are documented. The files are organized. The log shows what happened. In the next lesson, you'll transform these rules into an executable script that automates the entire process.

---

## Try With AI

**Custom Category Design:**

```
My Downloads has a lot of archive files (.zip, .tar.gz, .7z). Should these be their own category, or go in misc? What are the trade-offs?
```

**What you're learning**: Decision frameworks. AI presents options with reasoning, you decide based on how often you need to access archives.

**Edge Case Discovery:**

```
What edge cases might break simple extension-based categorization? Show me examples of files that could cause problems.
```

**What you're learning**: Defensive design. AI reveals tricky scenarios like `file.backup.pdf` (multiple dots), `README` (no extension), or `data.CSV` (case sensitivity).

**Rule Refinement:**

```
My rules.md categorizes by extension, but I have files from specific projects that should stay together regardless of type. How can I add project-based rules that take priority over extension rules?
```

**What you're learning**: Rule precedence. AI explains how to layer rules (check project name first, then fall back to extension), preparing you for more sophisticated automation.
