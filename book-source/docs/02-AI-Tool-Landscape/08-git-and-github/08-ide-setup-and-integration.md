---
sidebar_position: 8
title: "IDE Setup and Integration"
description: "Install and configure your IDE with Git integration and AI coding extensions for professional development"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Choose and Install IDE"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Remember"
    digcomp_area: "Information & Digital Literacy"
    measurable_at_this_level: "Student can select appropriate IDE, download installer, and launch successfully on their OS"

  - name: "Configure Git in IDE"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Digital Literacy & Problem-Solving"
    measurable_at_this_level: "Student can enable Git integration in IDE and navigate Source Control panel showing repository status"

  - name: "Install AI Coding Extensions"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Literacy & Tool Usage"
    measurable_at_this_level: "Student can search, install, and activate GitHub Copilot, Cursor AI, or Continue extension and test basic functionality"

  - name: "Use IDE Git Tools"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Literacy & Problem-Solving"
    measurable_at_this_level: "Student can stage files, write commit messages, and push changes using IDE GUI without command line"

cognitive_load:
  new_concepts: 5
  assessment: "5 new concepts (IDE, Source Control panel, Diff viewer, Git extensions, AI coding assistant) within A1 limit of 5 ✓"

differentiation:
  extension_for_advanced: "Research advanced IDE features: keyboard shortcuts, custom themes, workspace configuration, extension marketplace ecosystem"
  remedial_for_struggling: "Start with VS Code only (simplest); skip optional Git Graph/GitLens extensions; focus on Source Control panel basics before AI extensions"

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/012-chapter-8-git-github-aidd/plan.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "1.0.0"
---

# IDE Setup and Integration

## The Problem

You're typing Git commands every time. It's slow and you can't see your changes visually.

**Solution**: An IDE - a code editor with Git built in, plus AI help.

**Time**: 20 minutes

---

## What Is an IDE?

**IDE** = Integrated Development Environment (a fancy code editor)

**Simple explanation**:
- Regular text editor = just typing
- IDE = typing + Git + file explorer + AI help + everything in one place

**Why this matters**:
- See Git changes with colors (green = added, red = removed)
- Click buttons instead of typing commands
- AI suggests code as you type
- Everything works together

---

## Simple Analogy

**Writing a document**:
- Notepad = basic text editor (just typing)
- Microsoft Word = IDE (spell check, formatting, tools)

**Same with code**:
- Basic editor = just typing code
- IDE = code + Git + AI help + tools

---

## Your Three Choices

Pick ONE. Don't install all three (too confusing).

| IDE | Why Choose It | Get It |
|-----|---------------|--------|
| **VS Code** | Most popular, easiest to learn | code.visualstudio.com |
| **Cursor** | Built-in AI (Claude included) | cursor.sh |
| **Zed** | Super fast, clean | zed.dev |

**Recommendation**: Start with **VS Code** (most popular) or **Cursor** (if you want built-in AI).

---

## Step 1: Install Your IDE

**Just ask your AI**:
- "Help me install VS Code"
- "Walk me through installing Cursor"
- "I need to install an IDE, which should I choose?"

### Example

**You**: "Help me install VS Code on Windows"

**AI**: "I'll guide you:

1. Go to: code.visualstudio.com
2. Click 'Download for Windows'
3. Run the downloaded file
4. Click Next through the installer
5. Make sure 'Add to PATH' is checked
6. Click Finish

Tell me when it's installed."

**You**: "Installed! Now what?"

**AI**: "Open VS Code. You should see a Welcome screen with a blue sidebar. That means it's working!"

---

## Step 2: Open Your Git Project

**What you want**: Open your existing project folder in the IDE

**Instead of**: Navigating manually

**Just ask your AI**:
- "Help me open my project folder in VS Code"
- "How do I open a folder in this IDE?"
- "I have a project at /path/to/my-project, open it"

### Example

**You**: "I have a folder called 'my-calculator' with Git already set up. Open it in VS Code."

**AI**: "I'll open it for you..."

[AI opens the folder]

**AI**: "Done! Look at the left sidebar. You should see:
- Your files listed
- A Git icon (looks like branches)

Click the Git icon to see your Git status."

---

## Step 3: Find the Git Panel

**What you'll see**: The Source Control panel

**Where is it**: Click the branch icon on the left sidebar (3rd or 4th icon from top)

**What it shows**:
- Current branch name
- Files you changed (with colors)
- Button to commit
- Button to push

### Example

**You**: "I clicked the Git icon. What am I looking at?"

**AI**: "That's your Source Control panel! Here's what each part means:

- **Top**: Your current branch (probably 'main')
- **Middle**: Files you changed (orange dot = modified)
- **Bottom**: Text box to write commit message

Click any file to see what changed (green = added, red = removed)."

**You**: "Cool! So I don't need to type git status anymore?"

**AI**: "Exactly! The IDE shows you everything visually."

---

## Step 4: Make a Commit Using the IDE

**What you want**: Commit without typing commands

**Instead of**: git add + git commit

**Just use the GUI**:

1. Edit a file (make any small change)
2. Look at Source Control panel (you'll see the file listed)
3. Click the **+** icon next to filename (this stages it)
4. Type your commit message in the text box
5. Click the **✓ checkmark** above the text box (this commits)

### Example

**You**: "I changed my README. How do I commit it?"

**AI**: "Look at your Source Control panel:

1. See 'README.md' listed with orange dot? That means it changed.
2. Click the + next to it (stages the file)
3. Type your commit message: 'Update README'
4. Click the checkmark ✓ at the top

Done! No commands needed."

**You**: "That was way easier than typing!"

**AI**: "That's why developers use IDEs. Visual is faster."

---

## Step 5: Add AI Help (Optional but Amazing)

**What you want**: AI suggests code as you type

**Options** (pick ONE):
- **GitHub Copilot** ($10/month, or free for students)
- **Cursor AI** (built-in if using Cursor IDE)
- **Continue** (free, open-source)

**Just ask your AI**:
- "Help me install GitHub Copilot"
- "How do I add AI code suggestions to VS Code?"
- "I want AI to help me write code"

### Example

**You**: "I want AI to suggest code while I type. What should I use?"

**AI**: "I recommend GitHub Copilot. Here's how:

1. In VS Code, click Extensions icon (4 squares on left sidebar)
2. Search 'GitHub Copilot'
3. Click Install
4. Sign in with your GitHub account
5. Reload VS Code

Now when you start typing code, Copilot suggests completions in gray text. Press Tab to accept, Escape to dismiss."

**You**: "Does it cost money?"

**AI**: "About $10/month. But if you're a student, it's free with GitHub Student Pack."

---

## Common IDE Tasks

Here's how to do Git stuff with clicks instead of commands:

| What You Want | Instead of Command | Do This in IDE |
|---------------|-------------------|----------------|
| See what changed | `git diff` | Click filename in Source Control |
| Stage a file | `git add filename` | Click **+** icon next to file |
| Commit | `git commit -m "msg"` | Type message, click ✓ |
| Push to GitHub | `git push` | Click **...** menu → Push |
| Create branch | `git branch name` | Click branch name (bottom left) → Create new |
| Switch branches | `git checkout name` | Click branch name → Select branch |

**Key point**: Same Git operations, just with clicks instead of typing.

---

## Important: Always Review Before Committing

**Before you commit**:
1. Click the file to see the diff (what changed)
2. Read through the changes
3. Ask yourself: "Does this look right?"
4. If AI wrote it: "Do I understand what this code does?"
5. Then commit

**Why this matters**: The diff viewer shows you exactly what you're saving. Review = catch mistakes early.

---

## Key Points

**IDEs let you**:
- See Git changes with colors
- Click instead of type commands
- Get AI code suggestions
- Work faster and easier

**The workflow**:
1. Install IDE (VS Code or Cursor recommended)
2. Open your Git project folder
3. Use Source Control panel for Git operations
4. Optional: Add AI extension for code help

**Remember**: IDE = same Git commands, just prettier and easier.

---

## Try With AI

Practice using your IDE.

**Tool**: Claude Code, Gemini CLI, or ChatGPT

### Exercise 1: Install and Open

```
Help me install VS Code and open my Git project folder in it.
My project is at: /path/to/my-project
```

What to expect: AI guides you through download, install, and opening your folder.

### Exercise 2: Find Git Panel

```
I opened my project. Where's the Git panel?
What am I looking at? Explain each section.
```

What to expect: AI shows you where Source Control panel is and explains what each part means.

### Exercise 3: Make First IDE Commit

```
I edited README.md. Show me step-by-step how to commit this change
using the IDE (not command line). Use the GUI.
```

What to expect: AI walks you through: click +, type message, click ✓.

### Exercise 4: Install AI Extension

```
I want AI code suggestions. Help me install GitHub Copilot.
Walk me through every step.
```

What to expect: AI guides through Extensions, install, sign-in, testing.

### Exercise 5: Test AI Suggestions

```
I installed Copilot. How do I test it works?
Give me something simple to type and see what it suggests.
```

What to expect: AI suggests typing a comment like "# function to add two numbers" and watch Copilot suggest the code.

---

## What's Next

In Lesson 9, you'll use everything together: build a complete calculator project where AI writes all the code while you manage Git, test changes, and push to GitHub.

**Key takeaway**: IDEs make Git visual and easy. Same operations, just click instead of type.

