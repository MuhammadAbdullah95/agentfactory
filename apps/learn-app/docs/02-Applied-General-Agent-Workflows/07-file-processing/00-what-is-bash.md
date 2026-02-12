---
sidebar_position: 0
title: "Getting Bash Ready"
chapter: 7
lesson: 0
duration_minutes: 10
description: "Set up your terminal environment for the workflows ahead"
keywords:
  [
    "bash",
    "terminal",
    "command line",
    "shell",
    "WSL",
    "Git Bash",
    "Unix",
  ]

skills:
  - name: "Terminal Environment Setup"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can open a Bash-compatible terminal and run basic commands"

learning_objectives:
  - objective: "Access a Bash-compatible terminal on any operating system"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Student can open a terminal and run a simple command successfully"

cognitive_load:
  new_concepts: 1
  assessment: "1 concept (terminal setup) well within A1 limit of 4"

differentiation:
  extension_for_advanced: "Explore the difference between Bash, Zsh, and PowerShell - what makes each unique?"
  remedial_for_struggling: "Focus on getting one working terminal. If Git Bash works, use that. Don't worry about understanding everything yet."
---

# Getting Bash Ready

In Chapter 6, you learned why Bash is the key to General Agent capability — how the Vercel team discovered that simple shell access outperformed elaborate custom tooling, and how the Unix philosophy of small composable tools aligns perfectly with how LLMs reason. You don't need to re-learn that here.

What you do need is a working terminal on your machine. This lesson gets you there in five minutes.

## Getting Bash on Your System

### macOS

You already have it. Open **Terminal** (in Applications > Utilities, or press `Cmd + Space` and type "Terminal").

Modern macOS uses Zsh by default, which is Bash-compatible. All commands in this book work in both.

### Linux

You already have it. Open your terminal application (usually `Ctrl + Alt + T`).

### Windows

Windows doesn't include Bash natively, but you have two excellent options:

**Option 1: Git Bash (Quick start)**

When you install Git for Windows, it includes Git Bash — a terminal that provides Bash commands on Windows.

1. Download Git from [git-scm.com](https://git-scm.com/download/win)
2. During installation, keep the default options
3. After installation, right-click on your desktop and select "Git Bash Here"

Git Bash provides all the commands you'll use in this book: `ls`, `find`, `cat`, `grep`, and more. This is the fastest way to get started.

**Windows tip:** Paste in Git Bash with `Shift+Insert` or right-click, since `Ctrl+V` often doesn't work.

**Option 2: WSL (Windows Subsystem for Linux) — Recommended for serious development**

WSL runs a full Linux environment inside Windows. It's more powerful and provides a complete Unix experience, making it the better long-term choice for development work.

**Quick install** (Windows 10 version 2004+ or Windows 11):

1. Open PowerShell as Administrator (right-click Start → "Windows Terminal (Admin)" or "PowerShell (Admin)")
2. Run this command:
   ```powershell
   wsl --install
   ```
3. Restart your computer when prompted
4. After restart, Ubuntu will open automatically
5. Create a username and password (this is your Linux user, separate from Windows)
6. You now have a full Linux terminal

**If you run into issues**, WSL setup can vary depending on your Windows version and system configuration. This is a perfect opportunity to use your General Agent:

```
I'm on Windows and trying to set up WSL (Windows Subsystem for Linux).
I ran `wsl --install` but [describe what happened].
Can you help me troubleshoot and get WSL working?
```

Your agent can check your Windows version, suggest the right commands, and walk you through any additional steps like enabling virtualization in BIOS if needed.

**Accessing WSL after installation:**
- Type "Ubuntu" in the Start menu, or
- Open Windows Terminal and select the Ubuntu tab, or
- Type `wsl` in any command prompt

For this book, either Git Bash or WSL works. Choose Git Bash for quick setup, or WSL if you want the full Linux experience.

## Verify Your Setup

Open your terminal (Terminal on macOS/Linux, Git Bash or WSL on Windows) and run:

```bash
echo "Hello from Bash!"
```

You should see:

```
Hello from Bash!
```

Now try:

```bash
ls
```

This lists files in your current directory. If you see file names, your terminal is working.

## What About PowerShell?

Windows has its own powerful shell called PowerShell. It works differently from Bash, with different command names and syntax.

Claude Code and most AI coding tools are trained primarily on Bash because of its decades of widespread use in development, servers, and automation. Commands, examples, and tutorials across the internet overwhelmingly use Bash syntax.

This is why we recommend Git Bash or WSL for Windows users. Not because PowerShell is bad, but because Bash is the common language that AI tools speak most fluently.

## Ready to Begin

You now have a working terminal with Bash-compatible commands. That's all you need. In the next lesson, you'll open Claude Code and direct it to solve a real problem. You'll describe the problem in plain English and watch the agent translate that into commands that actually work.

Let's go file hunting.

---

## Try With AI

### Prompt 1: Troubleshoot Your Setup

If you're having trouble getting your terminal working, describe the problem to your agent:

```
I'm trying to set up a Bash terminal on [Windows/macOS/Linux].
When I [describe what you tried], I get [describe the error or behavior].
Can you help me get a working terminal?
```

**What you're learning:** Your first experience using an AI agent to solve a real problem. Setup issues are perfect practice because the agent can suggest commands, explain errors, and guide you through fixes.

### Prompt 2: Explore Your Shell

Once your terminal is working:

```
I just opened my terminal for the first time. Can you show me a few
simple commands to explore? Start with something that shows me where
I am, what files are here, and how to move around.
```

**What you're learning:** You're letting the agent teach you interactively rather than memorizing from a textbook. Notice how it explains each command as it introduces them.
