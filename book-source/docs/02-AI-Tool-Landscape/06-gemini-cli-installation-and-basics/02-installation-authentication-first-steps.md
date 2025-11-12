---
sidebar_position: 2
title: Installation, Authentication & First Steps
---

# Installation, Authentication & First Steps

> **A Word Before We Begin**
>
> Installing Gemini CLI is like meeting a new colleague—someone who's available 24/7 to collaborate on your work. In this lesson, you'll install Gemini CLI, authenticate with your Google account, and experience your first interaction with an AI partner using the Three-Role framework: AI as teacher, student, and co-worker.

---

## Learning Objectives

By the end of this lesson, you'll be able to:

- **Specify** installation and authentication requirements for Gemini CLI
- **Validate** successful installation with verification steps
- **Collaborate with AI** using the Three-Role Partnership framework (Teacher/Student/Co-Worker)
- **Use slash commands** as session specifications to control your AI session
- **Distinguish normal output** from errors using error literacy ("Red Flags to Watch")

---

## Prerequisites: What You Need

Make sure you have these before starting:

| Requirement | What It Is | How to Check |
|------------|-----------|-------------|
| **Node.js 20+** | Runtime for JavaScript applications | Open terminal, type: `node --version` |
| **npm** | Package manager (comes with Node.js) | Open terminal, type: `npm --version` |
| **Internet connection** | For installation and Google authentication | You have this already ✓ |
| **Google account** | For secure authentication | Gmail, YouTube, or any Google account |

### Don't Have Node.js 20+?

1. Visit [nodejs.org](https://nodejs.org/en/download)
2. Download the **LTS version** (Long Term Support—the stable version)
3. Follow the installer steps for your operating system
4. When asked about npm, keep the checkbox checked
5. Restart your computer

### Opening Your Terminal

**Windows:** Search "PowerShell" in your Start menu and open it

**macOS:** Press Cmd+Space, type "Terminal", press Enter

**Linux:** Press Ctrl+Alt+T (most distributions)

---

## Specification-First Installation Workflow

Before you run any commands, let's think like an AI-native developer. You'll **specify** what you want, then **execute**, then **validate**. This is the pattern you'll use throughout your career with AI tools.

### Your Installation Specification

Here's what we're trying to accomplish (the specification):

> **Goal**: Install Google Gemini CLI globally on my computer so I can access it from any directory. Then verify the installation succeeded, and authenticate using my Google account.
>
> **Success Criteria**:
> - `gemini -v` shows a version number (like 0.4.0 or higher)
> - `gemini` command launches successfully from any directory
> - Authentication completes without errors
> - I can ask questions and get responses

### Executing the Specification

**Step 1: Install Gemini CLI Globally**

Open your terminal and run this single command:

```bash
npm install -g @google/gemini-cli
```

This command downloads and installs Gemini CLI globally on your computer. You'll see text flowing by—this is normal. Wait for it to complete (usually takes 30-60 seconds).

**Step 2: Verify Installation**

After installation completes, verify it worked by checking the version:

```bash
gemini -v
```

You should see a version number like `0.4.0` or higher displayed. If you see this, the installation succeeded! ✓

---

## Validating Your Installation: Understanding Output vs. Errors

One of the most important skills in AI-native development is **error literacy**—understanding the difference between normal output and actual problems. Let's learn to validate your installation correctly.

### What Success Looks Like (Normal Output)

**Command**: `gemini -v`

**Expected Output**:
```
0.4.0
```

OR

```
Gemini CLI version 0.4.0
installed at /usr/local/bin/gemini
```

**Interpretation**: ✅ Installation successful. Version is displayed.

**Command**: `gemini`

**Expected Output**:
```
Welcome to Gemini CLI

Select theme:
  > Light
    Dark
    Solarized
```

**Interpretation**: ✅ Installation successful. Interactive prompt appears.

---

### Red Flags to Watch 🚩

These messages indicate real problems that need fixing.

**Error**: `command not found: gemini`

**What It Means**: Gemini CLI isn't installed, or npm's global directory isn't in your PATH

**How to Fix**:
1. Verify installation ran successfully: `npm list -g @google/gemini-cli`
2. If package shows, you need to fix PATH. Ask your AI: "I installed Gemini CLI but get 'command not found'. How do I fix my PATH?"
3. If package doesn't show, reinstall: `npm install -g @google/gemini-cli`

---

**Error**: `EACCES: permission denied`

**What It Means**: npm needs elevated permissions to install globally

**How to Fix** (choose ONE based on your comfort level):

*Option A (Recommended): Ask your AI*:
```
I got "EACCES permission denied" when installing Gemini CLI globally.
What's the safest way to fix this without using sudo?
```

*Option B (Manual Fix)*:
```bash
npm install -g @google/gemini-cli --no-save
```

---

**Error**: `npm: command not found`

**What It Means**: Node.js isn't installed or npm isn't in your PATH

**How to Fix**:
1. Go to [nodejs.org](https://nodejs.org/en/download) and install the LTS version
2. Restart your terminal
3. Try `npm --version` to verify

---

### Complete Verification Checklist

Run these commands to fully validate your installation:

```bash
# Check version (should show 0.4.0 or higher)
gemini -v

# Check installation location
npm list -g @google/gemini-cli

# Check command is accessible from PATH
which gemini     # macOS/Linux
where gemini     # Windows
```

**All three commands show results?** ✅ Installation is complete and correct.

**One or more show errors?** Check the "Red Flags" section above and ask your AI for guidance.

---

## Authentication & First Launch

Now comes the core experience—Gemini CLI handles authentication automatically. Simply type:

```bash
gemini
```

When you run this command for the first time, Gemini CLI launches and **automatically guides you through setup**:

### Step 1: Choose Your Theme

Gemini CLI will ask you to select a visual theme for the terminal interface:

```
Select theme:
  > Light
    Dark
    Solarized
```

Choose whichever you prefer—this is just cosmetic and can be changed later. Use arrow keys to select and press Enter.

### Step 2: Choose Authentication Method

You'll see options for authentication:

```
Choose authentication method:
  > Google login (free tier)
    Gemini API Key (requires setup)
    Vertex AI (requires Google Cloud Project)
```

**Select "Google login"** for the free tier. This is the beginner-friendly option with no setup required:
- **Free tier**: 60 requests/min, 1,000 requests/day
- **No billing required**: You can use Gemini CLI indefinitely on the free tier
- **No API key setup**: Authentication happens through your Google account

### Step 3: Browser Opens for Authentication

Your default web browser will automatically open with Google's login page. Simply:

1. Enter your Google account email
2. Enter your password
3. Click "Allow" when Google asks: "Gemini CLI wants access to your account"

### Step 4: You're In!

After you authorize, your terminal displays the Gemini CLI interface, and you're ready to start:

```
Welcome! You're authenticated as: your-email@gmail.com

Available tools:
  /help     Show all commands
  /stats    Check token usage
  /memory   Manage context files

Type your first question or use /help for commands.

gemini>
```

The prompt shows `gemini> `, indicating you're inside an interactive session. You're now ready to collaborate with your AI partner.

---

## Your First Collaboration with Gemini: The Three-Role Partnership

Instead of just asking a simple question, let's demonstrate how AI partners work with you in three distinct roles: as a teacher, as a student, and as a co-worker.

### 🎓 AI as Teacher: Learning Something New

In this role, AI teaches you concepts, explains best practices, and expands your knowledge.

**Type this into your Gemini CLI session**:

```
Explain the difference between Gemini CLI's 1M token context window and
Claude Code's 200K token context window. What does this mean for the
types of projects I should use each tool for?
```

**What Happens**: Gemini doesn't just answer—it:
- Explains token limits and what "context window" means
- Compares the two tools objectively
- Suggests when you'd want to use each tool
- Introduces concepts you may not have known (token management, context window sizing)

**What You Learn From AI**: AI taught you about context windows and tool selection criteria. This is knowledge you probably didn't have before. **This is AI as teacher.**

---

### 💙 AI as Student: Learning Your Preferences

In this role, you teach AI your coding style, preferences, and how you like to work.

**Type this into your Gemini CLI session**:

```
I prefer learning with detailed explanations and examples. When I ask you
questions, please provide:
1. A brief answer first (one paragraph)
2. Then a detailed explanation with practical examples
3. Then edge cases or gotchas to watch for
Can you adapt to this style?
```

**What Happens**: Gemini acknowledges your preference and confirms it will apply this style to all future responses in this session.

**What AI Learns**: AI learns your learning style, your communication preferences, and your quality standards. In future responses, it will remember and apply these preferences.

**This is AI as student**—it learns from you and adapts.

---

### 🤝 AI as Co-Worker: Solving Problems Together

In this role, you and AI work together as peers, with you providing direction and AI providing execution.

**Type this into your Gemini CLI session**:

```
I'm about to install Gemini CLI on my computer, but I'm not sure if my
Node.js version is compatible. Let's figure this out together:

1. Guide me through checking my current Node.js version
2. Tell me if it meets the requirements for Gemini CLI
3. If it doesn't, guide me through upgrading

Let's work step by step.
```

**What Happens**: Gemini:
1. Asks you to run: `node --version`
2. You respond with your version
3. Gemini analyzes it, tells you if it's compatible
4. If needed, it guides you through upgrading

**This is AI as co-worker**—neither commanding nor subordinate, but collaborating on equal footing to solve the problem.

---

### Key Insight: Three Modes of Collaboration

You've just experienced the three core ways you'll interact with AI throughout your development career:

| Role | What Happens | When You Use It |
|------|--------------|-----------------|
| **🎓 Teacher** | AI teaches you concepts, patterns, best practices | When you want to learn something new |
| **💙 Student** | You teach AI your preferences; AI adapts | When setting up a new project or session |
| **🤝 Co-Worker** | You direct strategy; AI executes details | When solving actual problems together |

All three roles are happening in every real project. Learning to switch between them based on your need is an essential AI-native skill.

---

## Essential Slash Commands: Session Specifications

Now that you're inside Gemini CLI, you have access to powerful slash commands. Think of these as **specifications for controlling your session**, not commands to memorize.

When you type `/` followed by a command name, you're **specifying** how you want your AI session to behave.

### Why This Matters

Traditional thinking: "I'll memorize commands and type them when I need them."

AI-native thinking: "I'll specify what I need, and the command executes that specification."

**Example**: When you're running out of context space (near the 1M token limit), instead of "remembering" there's a `/compress` command, you think: "I need to preserve key information while freeing capacity. How do I specify that?"

Answer: `/compress` is that specification.

---

### The Most Useful Commands for Right Now

Here are the slash commands you'll use most often as a beginner, organized by purpose:

#### Help & Information (When You're Stuck)

**`/help`** — Show all available commands

```
gemini> /help
```

**What it does**: Displays the complete list of all slash commands with descriptions

**When to use**: You forget what commands are available or what a command does

---

**`/stats`** — Check your session usage

```
gemini> /stats
```

**What it does**: Shows how many tokens you've used in this session and how much capacity remains

**Example output**:
```
Context Usage:
  Used: 15,234 tokens (1.5% of 1M limit)
  Remaining: 984,766 tokens (98.5%)
  Session: 5 minutes
```

**When to use**: Monitor your context budget to avoid hitting the 1M limit

---

#### Context Management (When You're Running Out of Space)

**`/compress`** — Intelligently reduce context size

```
gemini> /compress
```

**What it does**: AI analyzes your conversation, identifies the most important information, and summarizes less critical details. This frees capacity without losing key context.

**Business value**: Continue working on large projects without restarting your session

**When to use**: Your context is 70-80% full and you want to continue working

---

#### Control

**`/quit`** — Exit Gemini CLI and return to your terminal

```
gemini> /quit
```

**Alternative**: Press **Ctrl+C** twice to force quit

---

### Try It Now: Practice 3 Commands

You're inside Gemini CLI now. Let's practice using slash commands:

**1. Check your tools**:
```
gemini> /tools
```

You'll see a list of all capabilities Gemini has (file operations, web search, shell commands). This helps you understand what Gemini can do beyond answering questions.

---

**2. Monitor your context**:
```
gemini> /stats
```

You'll see how many tokens you're using. You have 1 million tokens—this is your "budget" for any single session. When you hit ~900K tokens, use `/compress` to continue.

---

**3. Get help anytime**:
```
gemini> /help
```

You'll see the complete command reference. **This is your lifeline**—when you forget a command, `/help` has the answer.

---

### Key Insight: Commands Are Specifications

You don't need to memorize these commands. Each one specifies a behavior:

- `/stats` specifies: "Show me my current resource usage"
- `/compress` specifies: "Preserve key info, reduce size"
- `/quit` specifies: "End this session"

When you're building an AI-native mindset, you're not memorizing syntax—you're thinking in specifications. The commands are just how you execute those specifications.

---

## Understanding Your Session

When you run `gemini`, you're entering an interactive session. Inside this session, you can:

1. **Ask questions** — Collaborate with AI
2. **Use slash commands** — Specify session behavior (seen above)
3. **Use @ syntax** — Reference files (covered in Lesson 3)
4. **Use ! syntax** — Execute shell commands (covered in Lesson 3)

For now, focus on asking questions and using slash commands. You have everything you need to have a productive conversation with your AI partner.

---

## Try With AI: Your First Gemini CLI Session

Now that you understand the basics, let's practice everything you've learned in an integrated workflow.

### Exercise: Meet Your AI Partner

**Time**: 15 minutes

**Part 1: Validate Installation** (3 minutes)

In your terminal:
```bash
gemini -v
```

If you see a version number, you're ready to launch.

---

**Part 2: Launch and Set Up** (3 minutes)

```bash
gemini
```

Follow the prompts to:
1. Select a theme (Light, Dark, or Solarized—your choice)
2. Select "Google login" for authentication
3. Complete authentication in your browser

You should now see the `gemini>` prompt.

---

**Part 3: Experience All Three Roles** (9 minutes)

Inside your Gemini CLI session, practice each role:

**AI as Teacher** (Ask for knowledge):
```
Explain what "context window" means and why it matters in AI tools.
Use an analogy to make it clear.
```

**AI as Student** (Teach your style):
```
I like learning through examples and real-world scenarios. When I ask
you to help with code, please:
1. Show the code first
2. Explain what it does line-by-line
3. Show how to use it
Can you remember this?
```

**AI as Co-Worker** (Work together):
```
I need to understand what Gemini CLI can do. Let's work together:
1. Tell me the 3 biggest differences between Gemini CLI and ChatGPT
2. For each difference, explain when I'd choose Gemini CLI
3. Give me one example project where Gemini CLI would be ideal

Walk me through your thinking—don't just list answers.
```

---

### Expected Outcomes

After this exercise, you'll have:

✅ Verified your installation works correctly
✅ Experienced authentication with your Google account
✅ Learned that AI works in three distinct roles
✅ Seen how `/help` and `/stats` control your session
✅ Understood that AI collaboration is bidirectional (you teach it, it teaches you)

### Safety Note: Validation and Trust

Remember: Never execute AI suggestions without understanding what they do first. In later lessons, you'll learn to:
- Read generated code before running it
- Validate that AI suggestions match your requirements
- Use `/help` to understand what commands do before executing them

This "understand before executing" mindset keeps you safe and builds expertise.

---

**Next lesson**: Lesson 3 (Core Commands & Slash Commands) will teach more advanced session management, including the `/memory` system, `/chat` save/resume, and how to use `/settings` to customize your experience.

