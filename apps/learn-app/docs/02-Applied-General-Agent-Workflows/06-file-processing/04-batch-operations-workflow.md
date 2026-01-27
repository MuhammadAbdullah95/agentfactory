---
sidebar_position: 4
chapter: 6
lesson: 4
title: "Batch Operations Workflow"
description: "Direct Claude Code to create reusable scripts for repetitive file operations—transforming one-time commands into permanent automation"
duration_minutes: 30

skills:
  - name: "Batch Processing Direction"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can direct an agent to perform batch operations with preview-before-action safety"

  - name: "Script Generation Request"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can request reusable scripts instead of one-time commands"

  - name: "Naming Convention Design"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Create"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can specify consistent naming patterns for batch operations"

learning_objectives:
  - objective: "Direct Claude Code to batch rename files with a consistent naming convention"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student successfully renames multiple files through agent direction"

  - objective: "Request preview of batch operations before execution"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student asks agent to show proposed changes before making them"

  - objective: "Request a reusable script for future batch operations"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Agent produces a script file the student can reuse"

  - objective: "Iterate on naming conventions through conversation"
    proficiency_level: "A2"
    bloom_level: "Evaluate"
    assessment_method: "Student refines naming pattern based on preview feedback"

cognitive_load:
  new_concepts: 3
  concepts_list:
    - "Preview-before-action pattern (seeing changes before they happen)"
    - "Script generation request (asking for reusable code, not one-time execution)"
    - "Iterative refinement (adjusting the plan through conversation)"
  assessment: "3 concepts within A2 limit of 5"

differentiation:
  extension_for_advanced: "Ask Claude Code to handle edge cases: what if some files already follow the new pattern? What if there are naming conflicts?"
  remedial_for_struggling: "Focus on just the first rename operation. Watch how the agent shows the preview. Don't worry about the script—just see the pattern of 'show me first, then do it.'"
---

# Batch Operations Workflow

You've got 87 screenshots.

They're named things like `Screenshot 2024-01-15 at 10.23.45.png` and `Screenshot 2024-03-22 at 14.07.33.png`. The auto-generated names made sense to your operating system. They make no sense to you. You want something organized: `screenshot-001.png`, `screenshot-002.png`, or maybe names that include the date in a cleaner format.

You could rename them one by one. That's 87 clicks, 87 new names, 87 chances to make a typo.

Or you could tell a General Agent what you want and watch it do the work.

---

## The Conversation

Open Claude Code. Describe the problem.

```
You: I have lots of screenshots with ugly names like 'Screenshot 2024-01-15
at 10.23.45.png'. Help me rename them to something organized like
'screenshot-001.png', 'screenshot-002.png', etc.
```

Watch what Claude Code does.

```
Claude Code: I'll analyze your screenshots and prepare a rename plan.
Let me first see what we're working with.

[Runs: ls ~/Screenshots/*.png | head -10]
[Runs: ls ~/Screenshots/*.png | wc -l]

I found 87 screenshots. Before I rename anything, here's what I'll do:

| Current Name                              | New Name         |
|-------------------------------------------|------------------|
| Screenshot 2024-01-15 at 10.23.45.png     | screenshot-001.png |
| Screenshot 2024-01-15 at 14.30.22.png     | screenshot-002.png |
| Screenshot 2024-02-03 at 09.15.11.png     | screenshot-003.png |
| Screenshot 2024-02-14 at 16.42.08.png     | screenshot-004.png |
| ... (83 more files)                       | ...              |

The files will be numbered in chronological order based on
their creation date.

Should I proceed with this plan, or would you like a different
naming pattern?
```

You look at the preview. Something's missing—you want to keep the date information.

```
You: Actually, include the date. Make it 'screenshot-2024-01-15-001.png'
so I can see when each screenshot was taken.
```

```
Claude Code: Good thinking—keeping the date makes files easier to find later.
Here's the updated plan:

| Current Name                              | New Name                     |
|-------------------------------------------|------------------------------|
| Screenshot 2024-01-15 at 10.23.45.png     | screenshot-2024-01-15-001.png |
| Screenshot 2024-01-15 at 14.30.22.png     | screenshot-2024-01-15-002.png |
| Screenshot 2024-02-03 at 09.15.11.png     | screenshot-2024-02-03-001.png |
| Screenshot 2024-02-14 at 16.42.08.png     | screenshot-2024-02-14-001.png |
| ... (83 more files)                       | ...                          |

Notice that files from the same day get sequential numbers within
that day (001, 002, etc.).

I'll also create a reusable script so you can run this pattern
on new screenshots later.

Proceed?
```

You're satisfied. You give the go-ahead.

```
You: Yes, do it.
```

```
Claude Code: [Runs: mkdir -p ~/Screenshots/renamed]
[Runs: # Rename loop with logging...]

Done. Here's what happened:

SUMMARY
- Files renamed: 87
- New location: ~/Screenshots/renamed/
- Script created: rename-screenshots.sh

CHANGE LOG (first 10):
  Screenshot 2024-01-15 at 10.23.45.png → screenshot-2024-01-15-001.png
  Screenshot 2024-01-15 at 14.30.22.png → screenshot-2024-01-15-002.png
  Screenshot 2024-02-03 at 09.15.11.png → screenshot-2024-02-03-001.png
  ...

The full log is saved in rename-log.txt.

To rename future screenshots, run:
  ./rename-screenshots.sh ~/Screenshots
```

87 files renamed. A reusable script created. A log of every change. You did this by having a conversation.

---

## What Just Happened?

You witnessed three principles working together.

**Principle 2: Code as Universal Interface.** Did you notice what the agent produced? Not just renamed files—a _script_. The agent didn't just solve your problem once. It created code you can run again. Next month when you have 50 new screenshots, you run `./rename-screenshots.sh` and they're all named consistently. The agent turned a one-time task into permanent automation.

**Principle 7: Observability.** Before the agent touched a single file, it showed you exactly what it planned to do. You saw the preview table. You could check that the new names made sense. You could change your mind. The agent made its intentions visible before acting.

**Principle 3: Verification.** The workflow followed a pattern: Preview → Approve → Execute → Log. The agent verified its plan with you before executing. Then it logged every change so you could verify what happened. Nothing was a mystery.

This is different from running commands yourself. You didn't have to know bash syntax for string manipulation or date extraction. You described what you wanted, reviewed the plan, and approved it.

---

## The Pattern

Here's what made this work:

```
"Show me what you'll do before doing it."
```

This single request triggers the preview-before-action pattern. The agent will:

1. Analyze the current state
2. Generate a proposed plan
3. Show you the plan
4. Wait for approval

And the second key request:

```
"Create a script I can reuse for this."
```

This triggers script generation instead of one-time execution. The agent produces:

1. A working script file
2. Instructions for running it
3. Built-in logging

Together, these patterns transform tedious manual work into reviewed, logged, reusable automation.

---

## Why Scripts Matter

Consider the difference:

| Approach          | What You Get                            | Next Time               |
| ----------------- | --------------------------------------- | ----------------------- |
| One-time commands | Files renamed                           | Start over from scratch |
| Script generation | Files renamed + `rename-screenshots.sh` | Run one command         |

The first approach solves the problem. The second approach solves the _category_ of problems. That's Principle 2 in action: code becomes the interface between your intent and recurring tasks.

The script also serves as documentation. Six months from now, you might forget exactly how you wanted screenshots named. Open `rename-screenshots.sh` and the logic is right there, preserved in code.

---

## Try It Yourself

Pick a batch operation from your own files.

**Option 1: Date-Based Rename**

```
I have files named randomly in my Documents folder. Help me rename them
to include today's date as a prefix, like '2025-01-27-filename.pdf'.
Show me the plan before doing anything.
```

Watch how the agent handles the preview. Notice if it asks clarifying questions.

**Option 2: Prefix Addition**

```
I want to add a prefix to all .pdf files in my Downloads folder.
Add 'archive-' to the beginning of each filename.
Show me what this will look like before you do it, and create
a script I can use for other folders.
```

See how the agent produces both the preview and the reusable script.

**Option 3: Extension Cleanup**

```
Some of my image files have uppercase extensions like .PNG and .JPG.
Help me rename them all to lowercase (.png, .jpg).
Show me the files that would change before making changes.
```

This tests whether the agent identifies only the files that need changing.

---

## The Key Requests

Remember these phrases for batch operations:

| What You Want      | What to Say                               |
| ------------------ | ----------------------------------------- |
| See the plan first | "Show me what you'll do before doing it"  |
| Get reusable code  | "Create a script I can reuse for this"    |
| Keep a record      | "Log every change you make"               |
| Change the plan    | "Actually, make it [new pattern] instead" |
| Limit scope        | "Just do the first 5 files to test"       |

You're not memorizing bash syntax. You're learning how to direct an agent effectively.

---

## What You're Building

By now in this chapter, you've learned:

| Lesson                   | Pattern                              | Principle                  |
| ------------------------ | ------------------------------------ | -------------------------- |
| 1. First Workflow        | "Help me understand"                 | P7: Observability          |
| 2. Safety First          | "Back up before changing"            | P6: Constraints and Safety |
| 3. Categorize with Rules | "Write rules first"                  | P5: Persisting State       |
| **4. Batch Operations**  | **"Show me first, create a script"** | **P2: Code as Interface**  |

Each pattern builds on the last. You understand your files. You protect them with backups. You document your rules. Now you transform repetitive tasks into reusable automation.

In the next lesson, you'll run your organizer script on real files and verify the results.

---

## Try With AI: Extended Practice

**Prompt 1: Complex Naming Patterns**

```
I want to rename my screenshots but the pattern is more complex:
- Group by month into folders (2024-01/, 2024-02/, etc.)
- Within each folder, name files screenshot-001.png, screenshot-002.png
- Show me the folder structure and file mapping before doing anything

Can you handle this multi-step organization?
```

**What you're practicing**: Compound requests. You're asking the agent to both reorganize (create folders) and rename (change filenames). Watch how it breaks down the complex task.

**Prompt 2: Dry Run Mode**

```
I want to see exactly what commands you would run to rename these files,
but don't actually run them yet. Show me the bash commands you'd execute
so I can understand what's happening.
```

**What you're practicing**: Understanding the mechanics. By asking to see the commands without execution, you learn what's happening "under the hood" while staying in control.

**Prompt 3: Error Handling**

```
What happens if two files would get the same new name? For example,
if I have two screenshots from the same second on the same day?
How would your script handle that conflict?
```

**What you're practicing**: Edge case thinking. Good automation handles unusual situations gracefully. You're learning to anticipate problems before they occur.
