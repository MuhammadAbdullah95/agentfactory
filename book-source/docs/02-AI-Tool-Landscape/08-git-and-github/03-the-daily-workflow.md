---
sidebar_position: 3
title: "The Daily Workflow"
description: "Learn five essential Git tasks using simple conversation with your AI"
keywords: [git workflow, version control, AI collaboration]

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Initialize Git Repository"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can create a new Git repository using AI guidance"

  - name: "Track File Changes"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can stage files and create commits with AI help"

  - name: "Push to Remote"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can upload commits to GitHub via AI commands"

learning_objectives:
  - objective: "Initialize a Git repository by asking AI assistant"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Student creates repository with AI help"

  - objective: "Check repository status using natural language"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Student asks AI to show what changed"

  - objective: "Stage, commit, and push changes with AI guidance"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Student completes workflow with AI assistant"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (init, status, add, commit, push) at A1 limit ✓"

# Generation metadata
generated_by: "lesson-writer"
source_spec: "specs/012-chapter-8-git-github-aidd/plan.md"
created: "2025-11-05"
last_modified: "2025-11-05"
version: "2.1.0"
---

# The Daily Workflow

## What You'll Learn

You're working on a Python project. Your AI just added a new feature. You need to:
- Save your progress
- Keep a record of changes
- Back it up safely

This lesson teaches five simple tasks. You won't memorize commands. You'll just talk to your AI assistant in plain English.

**Time**: 20 minutes

---

## How This Works

Traditional way: Memorize `git init`, `git add`, `git commit`, `git push`

AIDD way: Tell your AI what you want in normal language

**You say**: "Save my work"
**AI does**: Runs the right Git command
**You understand**: What happened and why

---

## The Five Daily Tasks

```
1. Start tracking my project
2. Check what changed
3. Choose what to save
4. Save a snapshot
5. Backup to cloud
```

Let's learn each one.

---

## Task 1: Start Tracking

**What you want**: Turn on Git for your project folder

**Instead of**: Typing `git init`

**Just say to your AI**:
- "Start Git in this folder"
- "Turn on version control"
- "Initialize Git here"
- "Set up Git tracking"

### Simple Example

**You**: "Start Git in this folder"

**AI**: "I'll set up Git tracking for you. Give me a moment..."

[AI runs the command]

**AI**: "Done! Git is now tracking this folder. You'll see a hidden .git folder that stores your history."

**You**: "What if I do this twice by accident?"

**AI**: "No problem. Git will just say 'already exists' but nothing breaks."

---

## Task 2: Check What Changed

**What you want**: See which files are new or changed

**Instead of**: Typing `git status`

**Just say to your AI**:
- "What files changed?"
- "Show me the status"
- "What needs to be saved?"
- "Did I change anything?"

### Simple Example

**You**: "What files changed?"

**AI**: "Let me check... You have 2 new files:
- calculator.py
- README.md

These files need to be staged before you can commit them."

**You**: "What does staged mean?"

**AI**: "Staged means you're telling Git 'I want to save these files in my next snapshot.' Think of it like putting items in a shopping cart before checkout."

---

## Task 3: Choose What to Save

**What you want**: Pick which files to include in your save

**Instead of**: Typing `git add`

**Just say to your AI**:
- "Stage all my files"
- "Prepare everything to commit"
- "Add all changes"
- "Get ready to save"

### Simple Example

**You**: "Stage all my files"

**AI**: "Staging all your changes now..."

[AI stages the files]

**AI**: "Done! Both calculator.py and README.md are ready to commit."

**You**: "What if I only want to save calculator.py?"

**AI**: "Just say 'stage only calculator.py' and I'll do that instead."

---

## Task 4: Save a Snapshot

**What you want**: Create a permanent save point

**Instead of**: Typing `git commit -m "message"`

**Just say to your AI**:
- "Save this with a message"
- "Commit my work"
- "Create a save point"
- "Save as: Added calculator"

### Simple Example

**You**: "Save this with message 'Add calculator module'"

**AI**: "Creating your commit with that message..."

[AI makes the commit]

**AI**: "Saved! Your commit ID is abc123. This is like a save point in a game—you can always come back to this exact moment."

**You**: "What makes a good message?"

**AI**: "Keep it simple and clear:
- Good: 'Add calculator module'
- Bad: 'stuff' or 'update'

Describe what you added or fixed."

---

## Task 5: Backup to Cloud

**What you want**: Upload your saves to GitHub

**Instead of**: Typing `git push origin main`

**Just say to your AI**:
- "Push to GitHub"
- "Backup to cloud"
- "Upload my commits"
- "Send to GitHub"

### Simple Example

**You**: "Push to GitHub"

**AI**: "I'll upload your commits. First, do you have a GitHub repository created for this project?"

**You**: "Not yet"

**AI**: "Go to GitHub.com and create a new repository. Name it whatever you want. When you're done, copy the URL it gives you and tell me."

**You**: "Done. The URL is https://github.com/alice/calculator.git"

**AI**: "Perfect! Connecting and pushing now..."

[AI connects and pushes]

**AI**: "All done! Your code is now on GitHub at that URL. If your computer breaks, your work is safe."

---

## Putting It All Together

Here's how a complete session looks:

**You**: "I'm starting a new Python project. Help me set up Git."

**AI**: "I'll create a folder and set up Git."

[AI creates project folder with Git]

**AI**: "Ready! What should I create first?"

**You**: "Make a simple calculator.py file"

**AI**: "Created calculator.py with basic functions. Want to see what Git thinks?"

**You**: "Yes, check the status"

**AI**: "Git sees calculator.py as a new file. It's not tracked yet."

**You**: "Stage it and save"

**AI**: "What message for the commit?"

**You**: "Add calculator module"

**AI**: "Committed! You now have your first save point."

**You**: "Push to GitHub"

**AI**: "Creating the repository connection and pushing..."

[AI handles GitHub setup]

**AI**: "Done! Your code is live on GitHub."

---

## Remember

You don't need to memorize:
- `git init`
- `git status`
- `git add`
- `git commit`
- `git push`

You just need to know:
- What you want to do
- How to ask your AI clearly
- How to check it worked

Your AI handles the technical parts. You stay focused on your project.

---

## Try With AI

Practice the five tasks with your AI assistant.

**Tool**: Claude Code, Gemini CLI, or ChatGPT

### Exercise 1: Complete Workflow

```
Help me practice Git:
1. Create a folder called "practice-git"
2. Set up Git tracking
3. Create a file called hello.py
4. Show me what Git sees
5. Stage the file
6. Commit with message "Add hello"
7. Show me my save history

Explain each step simply.
```

### Exercise 2: Make Changes

```
I changed hello.py to print "Hello Git!".
Help me:
1. Check what changed
2. Stage it
3. Commit with a good message
```

### Exercise 3: GitHub Backup

```
I want to put this on GitHub.
Guide me through:
1. Creating a GitHub repository
2. Connecting my project
3. Uploading my commits
```

---

## What's Next

In Lesson 4, you'll learn how to undo mistakes. Sometimes you save something wrong—Git lets you go back safely.

**Key takeaway**: Git with AI is like having a safety net. You experiment freely because you can always undo or go back to any save point.
