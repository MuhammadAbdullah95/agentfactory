---
sidebar_position: 1
title: "Your First Agent Workflow"
chapter: 7
lesson: 1
layer: L2
duration_minutes: 25
description: "See a General Agent solve a real problem, then learn the prompt pattern that made it work"
keywords:
  [
    "agent workflow",
    "file analysis",
    "claude code",
    "general agent",
    "prompting",
    "observability",
  ]

# HIDDEN SKILLS METADATA
skills:
  - name: "Problem-to-Prompt Translation"
    proficiency_level: "A1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Communication"
    measurable_at_this_level: "Student can translate a messy real-world problem into a clear prompt for a General Agent"

  - name: "Observing Agent Behavior"
    proficiency_level: "A1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Literacy"
    measurable_at_this_level: "Student can watch what a General Agent does and identify which principles are in action"

  - name: "Prompt Pattern Recognition"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can recognize and reuse prompt patterns across different problem domains"

learning_objectives:
  - objective: "Direct a General Agent to analyze a cluttered folder"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Student successfully prompts Claude Code to produce a folder analysis report"

  - objective: "Identify the Seven Principles in agent behavior"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Student can point to specific agent actions and name the principle being demonstrated"

  - objective: "Apply the 'Help me understand' prompt pattern to new problems"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student uses the pattern to analyze a different folder or problem domain"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (problem description, agent direction, observing actions, prompt patterns) within A1-A2 limit of 5"

differentiation:
  extension_for_advanced: "Try the prompt pattern on non-file problems: 'Help me understand my calendar this week' or 'Help me understand this codebase'"
  remedial_for_struggling: "Focus on just the first conversation. Watch what the agent does. Don't worry about identifying every principle. Just notice that the agent ran commands and reported back."
---

# Your First Agent Workflow

Here's what most people get wrong about working with General Agents. They think they need to describe the solution. They type commands, specify technical details, hope the agent understands.

The experts work differently. They describe the problem. They let the General Agent figure out the solution. And they watch closely to learn patterns that work everywhere.

Your Downloads folder is chaos. You download a PDF for a meeting, then forget about it. A week later, you download a spreadsheet for taxes. Then a photo someone sent. Then another PDF. Was that the same one as before? You're not sure. Months pass. Now there are hundreds of files. You don't know what's in there. You don't know what's taking up space. You don't know if there are duplicates. You just know it's a mess.

You've been meaning to organize it. You haven't. Because organizing isn't just moving files. First you need to _understand_ what you have. And understanding requires time you don't have.

This is exactly the kind of problem where General Agents shine. But here's the key. You're not learning bash commands. You're learning how to direct an intelligent system to solve problems for you. The pattern you'll master today applies to data analysis, project management, research tasks, and any workflow where you work with General Agents.

Let's see what effective direction looks like.

## The Conversation

Open Claude Code. You're going to describe a problem in plain English and watch what happens.

```
You: I have a cluttered Downloads folder. Help me understand what's
in here. How many files, what types, what's taking up space?
```

Watch what Claude Code does.

```
Claude Code: I'll analyze your Downloads folder. Let me take a look.

[Runs: ls -la ~/Downloads | head -20]

I see a lot of files. Let me get the full picture.

[Runs: find ~/Downloads -type f | wc -l]

You have 847 files in your Downloads folder. Let me break down
what types of files you have.

[Runs: find ~/Downloads -type f -name "*.pdf" | wc -l]
[Runs: find ~/Downloads -type f -name "*.xlsx" -o -name "*.csv" | wc -l]
[Runs: find ~/Downloads -type f -name "*.jpg" -o -name "*.png" | wc -l]
[Runs: find ~/Downloads -type f -name "*.zip" | wc -l]

Here's what I found:

| File Type     | Count | Notes                         |
|---------------|-------|-------------------------------|
| PDFs          | 234   | Documents, reports, receipts  |
| Spreadsheets  | 89    | .xlsx and .csv files          |
| Images        | 156   | Screenshots, photos           |
| Archives      | 43    | .zip files (may contain more) |
| Other         | 325   | Mixed: .docx, .dmg, .exe     |

Now let me see what's taking up the most space.

[Runs: du -sh ~/Downloads]
[Runs: du -ah ~/Downloads | sort -rh | head -10]

Total folder size: 12.4 GB

Your largest files:
1. project-backup.zip (2.1 GB)
2. video-recording.mp4 (1.8 GB)
3. database-export.sql (890 MB)
4. presentation-final.pptx (456 MB)
5. dataset.csv (312 MB)

Just these 5 files account for 5.5 GB. Almost half your folder.

Would you like me to help you organize these, or should I look
for duplicates first?
```

That took about 30 seconds. You now know:

- Total file count (847)
- Breakdown by type
- Total size (12.4 GB)
- Where the space is going

You didn't run a single command. You described a problem, and the agent solved it.

## What Just Happened?

Did you notice the agent's approach? It didn't use a fancy "folder analysis tool." It used `ls`, `find`, `wc`, and `du` — basic Unix commands that have existed for decades. These commands are fast, reliable, and do exactly what they claim. The agent combined them to extract exactly the information you needed.

Your Downloads folder was a black box. You knew it was messy, but you couldn't see inside it. The agent made chaos visible. Now you have a clear picture: file counts, types, sizes, space hogs. You went from "I should probably organize this someday" to "I know exactly what's in here and what to tackle first."

This is the power of General Agents. They don't just give you advice ("You should use the `find` command"). They do the work. They observe your system, run commands, and report back with actionable information.

### The Agent's Toolkit: What Those Commands Mean

The agent ran several commands. Let's decode them.

#### The Building Blocks

- **`ls`** — **l**i**s**t files in a folder
- **`find`** — **find** files matching a pattern
- **`wc`** — **w**ord **c**ount (counts lines, words, or characters)
- **`du`** — **d**isk **u**sage (measures sizes)
- **`sort`** — **sort** results in order

#### Anatomy of a Command

Let's break down one command the agent ran:

```
find  ~/Downloads  -type f  -name "*.pdf"  |  wc -l
  |        |          |          |         |    |
  |        |          |          |         |    +-- -l = count Lines only
  |        |          |          |         |
  |        |          |          |         +-- pipe: "then do this..."
  |        |          |          |
  |        |          |          +-- -name = match this filename pattern
  |        |          |
  |        |          +-- -type f = only Files (not folders)
  |        |
  |        +-- where to search
  |
  +-- the command
```

Read it left to right: "**Find** in **Downloads**, only **files**, named `*.pdf`, **then** count **lines**."

#### Common Flags You'll See

| Flag | Means                        | Memory Trick |
| ---- | ---------------------------- | ------------ |
| `-l` | Lines (or Long listing)      | **l**ines    |
| `-h` | Human-readable (KB, MB, GB)  | **h**uman    |
| `-r` | Reverse order                | **r**everse  |
| `-s` | Summary (totals only)        | **s**ummary  |
| `-a` | All (including hidden files)  | **a**ll      |

When the agent ran `du -sh`, that's "**d**isk **u**sage, **s**ummary, **h**uman-readable."

When it ran `sort -rh`, that's "**sort**, **r**everse order, **h**uman-readable" — biggest first.

#### The Pipe: Chaining Tools Together

The pipe (`|`) connects commands. Output from the left feeds into the right:

```bash
find ~/Downloads -name "*.pdf" | wc -l
```

"Find PDFs, **then** count them."

Small tools, chained together, solving big problems. That's what makes the shell so powerful.

You don't need to memorize these commands. But recognizing them helps you understand what the agent is doing — and verify it's doing the right thing.

## The Pattern

Here's the prompt pattern you just used:

```
"Help me understand [my problem]. Show me [what I need to know]."
```

This pattern works because it does two things:

1. **Describes the problem, not the solution.** You said "cluttered Downloads folder," not "run `find` and `du` commands." You let the agent figure out _how_ to help.

2. **Specifies the outcome you want.** You asked for "how many files, what types, what's taking up space." The agent knew what success looked like.

This is fundamentally different from learning bash commands yourself. You're not memorizing syntax. You're describing problems and letting the agent choose the right tools.

The pattern generalizes. Try these variations:

| Your Problem                     | The Prompt                                                                                   |
| -------------------------------- | -------------------------------------------------------------------------------------------- |
| Messy Desktop                    | "Help me understand my Desktop. What's here, what's old, what's taking up space?"            |
| Mystery disk usage               | "Help me understand where my disk space is going. What folders are largest?"                  |
| Project scattered across folders | "Help me understand where files related to [project name] are scattered."                    |
| Duplicate photos                 | "Help me understand if I have duplicate photos. Show me likely duplicates."                   |

The specifics change. The pattern stays the same.

## ✅ Checkpoint: Do This Now

Stop reading. Open Claude Code and run the survey on YOUR Downloads folder.

Use this prompt (modify if needed):

```
Help me understand what's in my Downloads folder. How many files,
what types, what's taking up space? Show me the full picture.
```

After Claude Code finishes, ask it to save the results:

```
Save this analysis as FILE-INVENTORY.md in a new folder called file-organizer/
```

You should now have: A `file-organizer/FILE-INVENTORY.md` file with your actual file analysis.

**Don't move to Lesson 2 until you've created this file.** Everything that follows builds on understanding YOUR files, not the example files in this book.

> **What to do if your Downloads folder is empty or tiny:** Pick a different folder — Documents, Desktop, or any folder with at least 20 files. Adjust the prompt accordingly.

## What You're Learning

You're not learning bash commands. You're learning something more valuable: **how to work effectively with General Agents**.

The skills you're building:

- **Problem description over solution specification.** You describe outcomes, not procedures. This applies to every domain where you direct General Agents.
- **Observation over memorization.** You watch what the agent does, learning patterns without rote memorization. Experts learn by observing agent behavior.
- **Prompt patterns over command syntax.** Reusable patterns that work across different problems. The "help me understand" pattern works for files, data analysis, project planning, research, and more.

---

## Try With AI

### Prompt 1: Go Deeper

```
I tried the "help me understand" pattern on my Downloads folder.
Now I want to go deeper. Based on what you found, what should
I investigate next? Pick the most interesting finding and
help me understand that in more detail.
```

**What you're practicing:** Iterative prompting. One analysis leads to the next question. You're building a habit of drilling down, not stopping at the first answer.

### Prompt 2: Translate to a new domain

```
The "help me understand [problem], show me [what I need]" pattern
worked for files. I want to apply it to something else.

Help me understand my recent shell history. What commands have I
run most often? What patterns do you see in how I use my computer?
```

**What you're practicing:** Pattern transfer. The same prompt structure works for different problems. You're learning that General Agents respond to well-structured requests regardless of domain.

### Prompt 3: Reflect on the agent's approach

```
I watched you analyze my Downloads folder. You used commands
like find, wc, and du.

Why did you choose those specific commands? What alternatives
did you consider? What would you have done differently if I'd
asked a slightly different question?
```

**What you're practicing:** Understanding agent reasoning. By asking the agent to explain its choices, you learn how it thinks. This makes you better at directing it in the future.

### Prompt 4: The Bash Tutor

```
Break down this command for me piece by piece:

du -ah ~/Downloads | sort -rh | head -10

What does each part do? What do the flags like '-ah', '-rh',
and '-10' mean? Teach me to read this command.
```

**What you're practicing:** Just-in-time learning. Instead of memorizing a textbook, you ask the agent to teach you the specific syntax relevant to the problem you just solved. The agent becomes your tutor, explaining commands in context.
