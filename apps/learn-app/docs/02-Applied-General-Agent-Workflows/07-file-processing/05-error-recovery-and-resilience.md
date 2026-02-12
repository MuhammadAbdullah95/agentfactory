---
sidebar_position: 5
chapter: 7
lesson: 5
layer: L2
title: "Error Recovery & Resilience"
description: "Deliberately break something and practice fixing it. Build recovery muscle memory so real mistakes don't cause panic"
duration_minutes: 20

skills:
  - name: "Deliberate Error Practice"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can intentionally create and recover from file operation errors"

  - name: "Backup Recovery Execution"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can restore files from a verified backup after a failed operation"

  - name: "State Comparison"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can compare current state against backup to identify what changed"

learning_objectives:
  - objective: "Create a test environment, break it deliberately, and recover from backup"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student completes the full create-break-recover cycle on test files"

  - objective: "Compare current state against backup to diagnose what went wrong"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student directs agent to compare directories and identifies differences"

  - objective: "Apply recovery prompts to common file operation failures"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student can articulate the correct recovery prompt for different failure scenarios"

cognitive_load:
  new_concepts: 3
  concepts_list:
    - "Deliberate practice (intentionally breaking things to learn recovery)"
    - "State comparison (diff between current and backup)"
    - "Recovery workflow (restore, verify, proceed)"
  assessment: "3 concepts within A2 limit of 5"

differentiation:
  extension_for_advanced: "Create a recovery script that automates the compare-and-restore workflow"
  remedial_for_struggling: "Focus on the basic cycle: backup exists → something broke → copy backup back. Don't worry about selective recovery."
---

# Error Recovery & Resilience

Here's the lesson most tutorials skip. They show you the happy path — everything works, files move to the right place, scripts run perfectly. Then when something goes wrong in real life, you're on your own.

Not here. In this lesson, you'll deliberately break something and practice fixing it. Because the question isn't _if_ something will go wrong — it's _when_. And when it does, you need a recovery workflow, not a panic response.

This is where the backup you created in Lesson 2 proves its worth.

## Why Practice Recovery?

Think about fire drills. Nobody expects a fire during the drill. The point is building muscle memory so that when a fire _happens_, you don't freeze.

Recovery from file operations is the same. If the first time you try to restore from backup is when you've actually lost important files, you'll be stressed, rushed, and more likely to make the situation worse.

Practicing recovery when nothing is at stake builds confidence for when something is.

---

## Exercise: The Deliberate Mistake

You're going to intentionally run a bad organization command and then recover from it. This is safe because you have a verified backup from Lesson 2.

### Step 1: Create a Test Mess

First, create a small set of test files so we're not risking your real organized work:

```
You: Create a folder called file-organizer/recovery-test/ with 10 dummy
files of different types (.pdf, .txt, .csv, .png). Put some sample text
in each one so we can verify they're intact after recovery.
```

Claude Code will create something like:

```
Created: recovery-test/
  report-q1.pdf
  notes.txt
  budget.csv
  photo-001.png
  meeting-minutes.pdf
  todo-list.txt
  expenses.csv
  diagram.png
  proposal.pdf
  data-export.csv
```

### Step 2: Back Up the Test Files

```
You: Create a backup of recovery-test/ in recovery-test-backup/
and verify it's complete.
```

```
Claude Code:
[Runs: cp -r file-organizer/recovery-test/ file-organizer/recovery-test-backup/]
[Runs: diff <(ls file-organizer/recovery-test/) <(ls file-organizer/recovery-test-backup/)]

Backup complete. 10 files copied. Source and backup match exactly.
```

### Step 3: Run a Bad Organization

Now, deliberately ask for something that will cause problems:

```
You: Move all files from recovery-test/ into a subfolder called
recovery-test/documents/. Don't check extensions — just move everything.
```

```
Claude Code:
[Runs: mkdir -p file-organizer/recovery-test/documents/]
[Runs: mv file-organizer/recovery-test/*.* file-organizer/recovery-test/documents/]

Moved 10 files into recovery-test/documents/.
```

### Step 4: Discover the Problem

Now check what happened:

```
You: Show me what's in recovery-test/ now. Also check if any
files were corrupted or lost in the move.
```

```
Claude Code:
[Runs: ls -la file-organizer/recovery-test/]
[Runs: ls -la file-organizer/recovery-test/documents/]

recovery-test/ now contains:
  documents/     (directory with 10 files)

All files are in documents/. But wait — your .png files and .csv files
are now mixed in with documents. The indiscriminate move didn't respect
file types.

Also, the flat structure you had is gone. If any scripts or references
pointed to recovery-test/budget.csv, they'd break now.
```

The "mistake" here is mild — you just lost your organization structure. But in real workflows, an indiscriminate move could overwrite files with the same name, break relative paths, or mix incompatible file types.

### Step 5: Recover from Backup

Here's the payoff. You have a backup. Recovery is straightforward:

```
You: That organization was wrong. Restore recovery-test/ from
recovery-test-backup/ to its original state.
```

```
Claude Code: Restoring from backup...

[Runs: rm -rf file-organizer/recovery-test/]
[Runs: cp -r file-organizer/recovery-test-backup/ file-organizer/recovery-test/]
[Runs: diff <(ls file-organizer/recovery-test/) <(ls file-organizer/recovery-test-backup/)]

Restored. recovery-test/ now matches the original backup exactly.
10 files, all in their original locations.
```

You're back to where you started. The bad organization is undone. No data lost.

---

## What Just Happened?

You just experienced the complete safety cycle:

```
1. Create test environment
2. Back up before changes
3. Make changes (deliberately bad ones)
4. Discover the problem
5. Restore from backup
6. Verify restoration is complete
```

This is the same cycle you'll use when real mistakes happen. The only difference is that real mistakes aren't deliberate — but the recovery process is identical.

### The Recovery Commands

The agent used these commands during recovery:

- **`rm -rf`** — **r**e**m**ove **r**ecursively, **f**orce — deletes the broken version. This is a dangerous command. It deletes without asking. That's why you need a verified backup BEFORE using it.
- **`cp -r`** — **c**o**p**y **r**ecursively — copies the backup back to the original location
- **`diff`** — **diff**erence — compares two directories to verify they match

> **Warning about `rm -rf`:** This command permanently deletes files. Never run it on a directory unless you have a verified backup you can restore from. The agent should always confirm before using it. If it doesn't, ask it to confirm first.

---

## Common Recovery Scenarios

Here are real situations where recovery saves you, and the prompt patterns to handle them:

**"I organized files with the wrong rules"**

```
The organization rules were wrong — financial files ended up in misc/
instead of spreadsheets/. Restore from backup and let's fix the rules
before re-organizing.
```

**"The rename script mangled filenames"**

```
The rename script produced garbled filenames. Show me the rename log,
then restore the original filenames from backup.
```

**"I accidentally deleted files I needed"**

```
I deleted some files from misc/ that I actually needed. Check my backup
for these files: [list filenames]. Copy them back to their original
location.
```

**"I'm not sure what went wrong"**

```
Something is off — my organized/ folder has fewer files than it should.
Compare the current state against the backup and show me what's missing
or different.
```

That last pattern — comparing current state against backup — is the most powerful recovery tool. When you're not sure what went wrong, a systematic comparison reveals exactly what changed.

---

## Building Recovery Into Your Workflow

The lesson from this exercise isn't just "backups are useful." It's that recovery should be a planned step, not an emergency response.

Here's how to build recovery thinking into every workflow:

| When                     | What to Do                                    |
| ------------------------ | --------------------------------------------- |
| Before you start         | Ask: "What's my recovery plan if this goes wrong?" |
| Before destructive ops   | Create or verify backup                       |
| After batch operations   | Compare results against expectations          |
| When something's off     | Compare current state vs backup               |
| After recovery           | Verify the restoration is complete            |

---

## ✅ Checkpoint: Do This Now

Stop reading. Open Claude Code and run the recovery exercise.

1. Create 10 test files in `file-organizer/recovery-test/`
2. Back them up to `file-organizer/recovery-test-backup/`
3. Run a bad organization (move everything into one subfolder)
4. Restore from backup
5. Verify the restoration matches the original

This should take less than 5 minutes. But the muscle memory you build will save you hours when a real mistake happens.

---

## Try With AI: Extended Practice

**Prompt 1: Selective Recovery**

```
I organized my Downloads folder but only the spreadsheet categorization
was wrong. Help me restore JUST the spreadsheet files from backup
without undoing the rest of the organization.
```

**What you're practicing:** Surgical recovery. Sometimes you don't want to undo everything — just fix the part that went wrong.

**Prompt 2: Recovery Audit**

```
Compare my organized/ folder against my backup/ folder. Show me:
- Files that exist in backup but not in organized (lost files)
- Files that exist in organized but not in backup (new files)
- Files that changed size (possible corruption)
Create an audit report.
```

**What you're practicing:** Systematic comparison. This is the detective work that tells you exactly what changed and what might be wrong.

**Prompt 3: Recovery Script**

```
Create a script called restore.sh that takes a backup folder and a
target folder as arguments and restores the target from the backup.
Include verification that the restoration was complete.
```

**What you're practicing:** Automating recovery. Just like you created scripts for organization, you can create scripts for recovery. The pattern is the same.
