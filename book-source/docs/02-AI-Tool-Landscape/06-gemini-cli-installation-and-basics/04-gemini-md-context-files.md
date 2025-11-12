---
sidebar_position: 4
title: "GEMINI.md Files: Helping Gemini Remember Your Preferences"
duration: "15-20 min"
---

# GEMINI.md Files: Helping Gemini Remember Your Preferences

In Lesson 3, you learned about `/memory add`—a command that teaches Gemini facts about you.

But there's a problem: If you close Gemini CLI and come back tomorrow, it forgets what you taught it.

**GEMINI.md files solve this problem.** They're special files that let you write down your preferences once, and Gemini remembers them forever—across all your conversations.

---

## What is a GEMINI.md File? (Start Here If New)

**GEMINI.md is a text file that contains information about you or your projects. Gemini reads this file automatically and uses it to understand how you like to work.**

Think of it like a personal instruction manual:
- Regular instructions: "Please explain Python to me like I'm a beginner"
- GEMINI.md: You write this once in a file, and Gemini always follows it

**Why this matters:** Instead of telling Gemini your preferences every time you start a conversation, you write them once in GEMINI.md. Gemini automatically knows how you like to learn.

---

## The Simple Idea

Here's the simplest way to think about GEMINI.md:

1. **Create a file** called `GEMINI.md` (that's the filename)
2. **Write your preferences** in it (plain English, not code)
3. **Put it in your home directory** (or in a project folder)
4. **Gemini reads it automatically** when you start a conversation
5. **Your preferences are remembered forever** (until you change the file)

---

## What Goes in a GEMINI.md File?

Here's what you might write in your GEMINI.md file:

### Example 1: Your Personal Learning Preferences

```markdown
# My Learning Preferences

I'm a complete beginner learning about technology.

When you explain things:
- Use simple language, no jargon
- Give real-world examples
- Ask me clarifying questions if I'm confused
- Explain WHY something matters, not just HOW it works

I prefer learning step-by-step, not all at once.
```

**What this does:** Whenever you talk to Gemini, it remembers: "This person is a beginner, use simple language, include examples."

---

### Example 2: Your Coding Style (If You Code)

```markdown
# My Coding Preferences

I prefer Python because it's readable.

When you show code:
- Always include comments explaining what's happening
- Show me a simple example first, then a more complex one
- Explain any terms I might not know

I don't like super short code that's hard to read.
```

**What this does:** Whenever Gemini shows you code, it knows your preferences and matches them.

---

### Example 3: Your Work Style

```markdown
# How I Like to Work

I learn best through small practice exercises.
I get frustrated if explanations are too technical.
I like to understand the "why" before the "how."

Please ask me questions to check if I understand
before moving to the next topic.
```

**What this does:** Gemini adapts its teaching style to match how you learn.

---

## How to Create Your GEMINI.md File

This takes about 5 minutes. Here's the step-by-step process:

### Step 1: Open a Text Editor

On your computer, open a simple text editor:

**Windows:** Search "Notepad" in Start menu and open it

**macOS:** Open "TextEdit" (in Applications > Utilities)

**Linux:** Open "gedit" or "nano"

---

### Step 2: Write Your Preferences

Type your preferences in plain English. Here's a simple template:

```markdown
# My Gemini Preferences

I'm learning about [topic you're interested in].

When you help me:
- Use simple language
- Include examples
- Explain new terms

My learning style:
- [How you like to learn]
- [What helps you understand]
- [What frustrates you]

General preferences:
- [Anything else important]
```

**Fill in the brackets** with your actual preferences.

---

### Step 3: Save the File

**Important:** Save the file with the exact name: `GEMINI.md`

- Click "Save As"
- Name it: `GEMINI.md` (capital G, capital I, lowercase md)
- Save it in your home directory (Windows: C:\Users\YourName, Mac: /Users/YourName, Linux: ~/)

---

### Step 4: Verify Gemini Reads It

Next time you open Gemini CLI, it should automatically read your file. You can verify this by typing:

```
gemini> /memory show
```

You should see your preferences listed!

---

## Real-World Example: Your First GEMINI.md

Let me show you what a real beginner's GEMINI.md might look like:

```markdown
# My Learning Profile

## Who I Am
- Complete beginner to technology
- Learning to understand computers and basic coding
- Prefer step-by-step explanations

## How I Learn Best
- Simple explanations without jargon
- Real-world examples (not abstract theory)
- Short practice exercises after each concept
- Encouragement when things are hard

## What Frustrates Me
- Technical words without definitions
- Jumping to advanced topics too fast
- Assuming I know things I don't
- No context for WHY something matters

## My Interests
- Understanding how computers work
- Learning basic programming concepts
- Building small projects

## General Notes
- Ask me clarifying questions if I'm confused
- Celebrate small wins—I'm building confidence
- It's okay to explain the same thing multiple times
```

This is simple, personal, and helpful. Gemini reads this and knows exactly how to teach you.

---

## A Second Example: If You're Already Coding

If you already know how to code, your GEMINI.md might look different:

```markdown
# My Development Context

## Language Preferences
- Primary: Python 3.13
- Secondary: JavaScript/TypeScript
- I like readable code over clever code

## How I Like Code Examples
- Always include error handling
- Show the full working example
- Include comments for non-obvious parts
- Test examples before suggesting them

## Development Tools
- Terminal: VS Code
- Testing: pytest for Python
- Version control: git

## Preferences
- Explain your reasoning, don't just give answers
- I prefer understanding the "why" over the "what"
```

---

## Where Can You Put GEMINI.md?

You can put GEMINI.md files in different places, and Gemini will find them automatically:

### Option 1: Your Home Directory (Global)

```
/Users/YourName/GEMINI.md
```

This applies to ALL your conversations, no matter what project you're working on.

**Use this for:** Your general learning style, preferences, and how you like to work.

---

### Option 2: A Project Folder (Project-Specific)

```
/Users/YourName/my-python-project/GEMINI.md
```

This applies only when you're working in that specific folder.

**Use this for:** Information about a specific project (what you're building, what tools you use, project-specific preferences).

---

## Important: GEMINI.md vs. /memory add

You learned about `/memory add` in Lesson 3. Let's clarify the difference:

| Feature | /memory add | GEMINI.md |
|---------|-----------|-----------|
| **What is it?** | A command to teach Gemini facts | A file that teaches Gemini facts |
| **Permanence** | Lasts only this session | Permanent (until you change the file) |
| **When to use** | Quick facts you want to remember today | Preferences you want forever |
| **Example** | `/memory add I prefer Python` | Write in GEMINI.md file |

**Real scenario:**
```
Day 1:
You: /memory add Today I'm learning about loops
(Lasts only today)

Day 1 (in GEMINI.md):
"I'm a beginner learning about programming"
(Lasts forever)
```

---

## Common Beginner Questions

**Q: Do I HAVE to create a GEMINI.md file?**

A: No. Gemini CLI works fine without it. But if you want Gemini to remember your preferences automatically, GEMINI.md is the easiest way.

---

**Q: What if I don't know what to write in my GEMINI.md?**

A: Start simple. Just write:
- "I'm a complete beginner"
- "Please explain things simply"
- "Include examples in your explanations"

That's enough!

---

**Q: Can I change my GEMINI.md file after creating it?**

A: Yes! Edit it anytime. Just open it in a text editor and make changes. Gemini will read the updated version next time you start a conversation.

---

**Q: If I have both a home directory GEMINI.md and a project folder GEMINI.md, which one does Gemini use?**

A: Both! Gemini reads both files. Your home directory file applies to everything, and your project file adds project-specific information on top of that.

---

## Try With AI: Create Your First GEMINI.md

Let's create your own GEMINI.md file right now.

### Step 1: Open a Text Editor (2 minutes)

Open Notepad (Windows), TextEdit (Mac), or gedit (Linux).

---

### Step 2: Write Your Profile (5 minutes)

Copy this template and fill in your own information:

```markdown
# My Gemini Preferences

## Who I Am
- [Describe yourself briefly]
- [What are you trying to learn?]

## How I Learn Best
- [Your learning style]
- [What helps you understand]
- [What examples matter to you]

## What I Don't Like
- [Things that frustrate you]
- [Explain anything you want Gemini to avoid]

## General Notes
- [Anything else Gemini should know about you]
```

---

### Step 3: Save the File (2 minutes)

1. Click "Save As"
2. Name it: `GEMINI.md` (exactly)
3. Save in your home directory
   - **Windows:** C:\Users\YourName\
   - **Mac:** /Users/YourName/
   - **Linux:** ~/

---

### Step 4: Verify It Works (3 minutes)

1. Open Gemini CLI: `gemini`
2. Check your memory: `/memory show`
3. You should see your GEMINI.md content listed!

---

## Key Terms Review

**GEMINI.md:** A special file that contains your preferences. Gemini reads this file and remembers your preferences forever.

**Home directory:** The main folder for your user account on your computer (C:\Users\YourName on Windows, /Users/YourName on Mac).

**Project folder:** A specific folder where you're working on something (like a learning project, coding project, etc.).

**Text editor:** A simple program that lets you write plain text (like Notepad, TextEdit, or gedit).

**Global preferences:** Settings that apply to everything you do (like your learning style).

**Project-specific:** Settings that apply only to one particular project or folder.

---

**Ready for Lesson 5?** Next, you'll learn about saving your conversations and picking up where you left off—persistence across days and weeks of learning.
