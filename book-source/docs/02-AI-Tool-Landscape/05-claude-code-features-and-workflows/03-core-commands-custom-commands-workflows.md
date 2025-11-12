---
sidebar_position: 3
title: "Ways to Talk With Claude: Commands"
duration: "25-30 min"
---

# Ways to Talk With Claude: Commands

Imagine you have a helpful friend at your side while you work. Sometimes you ask them a quick question. Sometimes you say "let me mark where we are right now so we don't lose our place." Sometimes you point at a specific document and say "look at this file and help me understand it."

**Commands are different ways to ask Claude for help.**

Instead of remembering complicated syntax, you'll learn a few simple patterns. Each pattern tells Claude something different about what you need.

---

## What is a Command? (Start Here If New)

**A command is a way to talk to Claude Code.**

Think of it like different types of questions you can ask:
- **Simple question**: "What does this error mean?"
- **Pointing to a file**: "Look at my login code and find the bug"
- **Marking progress**: "I finished fixing that bug. Now moving to the next feature"
- **Starting fresh**: "Forget everything before. We're starting a new task"

Each of these is a **command**—a different way to communicate with Claude.

**Don't worry about memorizing them.** You'll use them naturally as you need them. We'll explain each one, and you can look them up anytime.

---

## The Most Important Commands

Here are the commands you'll use most often. We'll explain each one with examples.

### 1. `claude` - Ask Claude a Question

**What it does**: You ask Claude something, and Claude answers.

**How to use it**:
```bash
claude "What does this error mean?"
```

Or start a conversation without a question and type back and forth:
```bash
claude
(Claude starts talking with you)
```

**Real example from a beginner**:
```bash
claude "I'm confused about why my code gave me an error message. The error says: 'mkdir: test: File exists'. What does that mean?"

Claude: "Great question! This error means you tried to create a folder called 'test', but it already exists...
```

**When to use it**: Whenever you have a question or need Claude's help.

---

### 2. `#` - Mark Your Progress (Checkpoints)

**What it does**: You mark a point in your work and tell Claude "we've completed this step."

**How to use it**:
```bash
# I fixed the login bug
# Now testing the password reset feature
```

**Why this matters**: Claude remembers that you finished something, so it can help you with what comes next. Think of it like a bookmark in a book—you mark where you are so you don't get lost.

**Real example**:
```bash
claude "Review my authentication code for security issues"
# Security review complete
claude "Now help me write tests for the password reset feature"
```

Claude knows that the security review is done, so it won't repeat suggestions.

**When to use it**: When you finish one task and are moving to the next one.

---

### 3. `@filename` - Point Claude to a Specific File

**What it does**: You tell Claude "look at this file and help me with it."

**How to use it**:
```bash
@login.py "What does this function do?"
```

**Without this command**, you'd have to copy-paste the entire file into your question. With `@filename`, Claude automatically reads the file and understands the context.

**Real example**:
```bash
@models.py @views.py "How do these two files work together?"

Claude: "Looking at both files... models.py defines your data structure, and views.py uses that data to..."
```

**When to use it**: When you want Claude to look at a specific file (or multiple files) in your project.

---

### 4. `/init` - Remember My Project

**What it does**: Claude learns about your project so it can give better help.

**How to use it**:
```bash
/init
```

Claude will ask you questions like:
- "What's the name of your project?"
- "What programming language are you using?"
- "What's this project for?"

You answer the questions, and Claude remembers your answers for future conversations.

**Why this matters**: Instead of explaining "I'm working on a Python web app for managing to-do lists" every time, Claude just remembers it.

**When to use it**: When you start a new project with Claude Code.

---

### 5. `/clear` - Start Over (Forget Previous Conversations)

**What it does**: Tells Claude "forget everything we talked about. We're starting a completely new task."

**How to use it**:
```bash
/clear
```

**When to use it**:
- You've finished one project and are starting a different project
- The conversation got confusing and you want to start fresh
- You're working on something unrelated to what you just discussed

**Example**:
```bash
# Working on authentication feature
claude "Help me fix this login bug"
# ... conversation ...

/clear

# Now working on a completely different feature
claude "Help me optimize database queries"
```

Claude forgets about the login bug work and focuses only on database optimization.

---

## When to Use Which Command: A Simple Guide

Here's a quick decision guide:

| What You Want to Do | Which Command |
|-----|-----|
| Ask Claude a question | `claude "your question"` |
| Point Claude to a file | `@filename "your question"` |
| Mark that you finished something | `# Description of what you finished` |
| Tell Claude your project details once | `/init` |
| Start a completely new task | `/clear` |

---

## Pause and Reflect: Your Comfort Level

You've learned five key commands. Before moving forward, ask yourself:

**Do you feel comfortable using these commands?**
- If yes: Great! Move forward to the next section.
- If no: That's completely normal. You don't need to memorize them. Come back to this reference anytime you need it.

**What command would you use if**:
1. You wanted to ask Claude what a specific error message means? (Answer: `claude "error message here"`)
2. You wanted Claude to look at your database code? (Answer: `@database.py "question"`)
3. You finished writing a feature and were starting a new one? (Answer: `#`)
4. You were completely switching topics and wanted Claude to forget previous work? (Answer: `/clear`)

If you can answer these, you understand the basics. The rest comes with practice.

---

## Understanding Your Workspace

When you use Claude Code, you and Claude share the same **workspace**. This is important to understand:

**Your workspace includes**:
- Your files and folders (Claude can read them)
- Your current location (Claude knows where you are in your project)
- Your previous conversation (Claude remembers what you talked about)

**Think of it like**:
- Sitting at a desk with Claude
- You can both see the same files
- You can both see what's been written down
- Claude remembers what you've discussed

This is different from web-based AI (like ChatGPT) where you have to describe everything. Claude Code can **see** your actual files, so you can ask more specific questions like "look at my login.py file" instead of "here's some code I'm going to paste."

---

## Common Mistakes to Avoid

### Mistake 1: Typing Too Much

You don't need to explain everything. Claude can see your files.

**Bad**:
```bash
claude "I have a file called app.py with a function that handles user login. It takes a username and password, checks them against a database..."
```

**Good**:
```bash
@app.py "Is my login function secure?"
```

Claude reads the file automatically.

---

### Mistake 2: Forgetting to Use `/clear`

If you're switching to a completely different project or task, use `/clear` first. Otherwise, Claude might bring up information from the previous task.

**Example**:
```bash
# Wrong (Claude might get confused):
claude "Help me with my Python web app"
# ... lots of conversation ...
claude "Help me debug my JavaScript website"

# Right (Clean start):
claude "Help me with my Python web app"
# ... lots of conversation ...
/clear
claude "Help me debug my JavaScript website"
```

---

### Mistake 3: Not Using `#` to Mark Progress

Long conversations get confusing. Mark the progress so Claude understands what's done.

**Without checkpoints** (confusing):
```bash
claude "Help me build a login feature"
# ... conversation ...
claude "Help me add password reset"
# ... conversation ...
# But Claude doesn't know when login work ended and password reset work began
```

**With checkpoints** (clear):
```bash
claude "Help me build a login feature"
# ... conversation ...
# Login feature complete
claude "Now help me add password reset"
# ... conversation ...
```

---

## Try With AI: Practice Commands

Even though you have Claude Code installed, practice these commands using any AI tool (ChatGPT, Gemini, etc.). You're learning the *patterns*, not the specific tool.

### Activity 1: Simple Question Practice

Open ChatGPT or another AI tool and ask:

```
I'm learning Claude Code. Explain these 5 commands in simple language
(no technical jargon):
1. claude
2. #
3. @filename
4. /init
5. /clear

For each one, give me a real-world analogy (not programming-related).
```

**What you're practicing**: How to ask clear questions. The command itself is less important than being able to ask what you need.

---

### Activity 2: Pointing to Files Practice

Imagine you have three files: `login.py`, `database.py`, and `config.py`. You want to ask Claude about how they work together.

**Without the `@` command**, you'd need to describe all three files.
**With the `@` command**, you just point.

Ask your AI:
```
If I have three Python files (login.py, database.py, config.py),
what's the shortest way I could ask an AI assistant to explain
how they work together? Show me the exact command I'd use.
```

**What you're practicing**: Understanding how to point Claude to files instead of describing them.

---

### Activity 3: Starting Fresh Practice

```
Imagine I've been talking with an AI about debugging Python for 30 minutes.
Now I want to switch to asking about CSS.
What should I do to make sure the AI focuses on CSS
and doesn't keep bringing up Python from before?
```

**What you're practicing**: Understanding when to separate conversations.

---

## Key Terms Review

**Command**: A way to ask Claude for help. Different commands do different things.

**Checkpoint** (the `#` command): A marker that says "we finished this task."

**File reference** (the `@` command): Pointing Claude to a specific file you want help with.

**Workspace**: Your project folder and all its files—Claude can see everything in here.

**Clear**: Telling Claude to forget previous conversations and start fresh.

---

## What's Next?

In Lesson 4, you'll learn about **specialized helpers** (called "subagents")—Claude Code assistants that are specially trained for specific jobs, like code review or writing tests.

But first, practice these commands. The more you use them, the more natural they'll feel.

**Before moving to Lesson 4**, try using these commands with Claude Code:
1. Ask Claude a simple question with `claude "your question"`
2. Point Claude to a file with `@filename "your question"`
3. Mark progress with `# Your progress note`

You don't need to be perfect. Just get comfortable with the patterns.

---

## Try With AI: Start Your First Real Command Practice

Open ChatGPT or another AI tool and run this prompt:

### Prompt 1: Learn Commands by Example

```
I'm learning Claude Code commands. For each command below, give me:
(1) A real-world analogy (not programming)
(2) A simple example showing how I'd use it
(3) When I'd use it in my daily work

Commands:
- claude (asking questions)
- @ (pointing to files)
- # (marking progress)
- /init (remember my project)
- /clear (start over)
```

**Expected outcome**: Simple explanations with everyday analogies. You'll understand when and why to use each command.

---

### Prompt 2: Practice Your Own Use Case

```
I work on [your type of work: website building, data analysis, writing code, etc.].
Walk me through a typical workflow using Claude Code commands:
1. How would I start a session? (/init or other command)
2. How would I ask my first question? (claude command)
3. How would I point Claude to a specific file? (@filename)
4. How would I mark progress as I work? (#)
5. When would I use /clear?
```

**Expected outcome**: A personalized workflow showing how these commands fit your actual work.

---

## Safety Reminder

**Remember from Lesson 2**: You're always in control. Commands are just tools to help you communicate with Claude Code. They don't do anything dangerous on their own—they just help you ask questions and mark progress.

If a command seems confusing, you can:
- Skip it for now (you won't need all of them right away)
- Ask Claude: "What does this command do?"
- Look back at this lesson anytime

**You're learning at your pace. There's no rush.**

---

**Ready for Lesson 4?** Let's learn about specialized helpers (subagents).
