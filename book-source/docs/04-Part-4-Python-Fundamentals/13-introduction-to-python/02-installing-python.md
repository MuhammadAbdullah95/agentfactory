---
title: "Installing Python and Setting Up Your Environment"
chapter: 13
lesson: 2
duration_minutes: 30

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Understand Python Installation and Environment Setup"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain what Python installation means and where Python lives on their computer"

  - name: "Follow Platform-Specific Installation Steps and Verify Installation"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can successfully install Python 3.14.0 on their operating system and run `python --version` to confirm"

  - name: "Troubleshoot Installation Issues Using AI Partnership"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can describe installation errors using natural language and ask AI for troubleshooting guidance"

learning_objectives:
  - objective: "Understand what Python installation means and where Python lives on your system"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Explanation of Python installation location and process"

  - objective: "Install Python 3.14.0 on your operating system (Windows, macOS, or Linux)"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Successful installation of Python on target OS"

  - objective: "Verify installation by running `python --version` and confirming Python 3.14.0 is available"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Terminal output showing Python 3.14.0 version number"

cognitive_load:
  new_concepts: 2
  assessment: "2 new concepts (Installation, Verification) within A1 limit of 5. Guided procedure format provides step-by-step scaffolding ✓"

differentiation:
  extension_for_advanced: "Research: Why are virtual environments important in Python development? Search for 'Python venv' or 'conda environments' and summarize what you learn. Don't set one up yet—just understand the concept."
  remedial_for_struggling: "Installation can be frustrating if things don't work the first time. That's completely normal. If you get stuck, start by running `python --version` (without installing). If you see any error, take a screenshot and ask Claude Code: 'I see this error when I try to check my Python version: [describe the error]. What does this mean?'"

# Generation metadata
generated_by: "lesson-writer v1.0"
source_spec: "specs/part-4-chapter-13/spec.md"
source_plan: "specs/part-4-chapter-13/plan.md"
source_tasks: "specs/part-4-chapter-13/tasks.md"
created: "2025-11-08"
last_modified: "2025-11-08"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "1.0.0"
---

# Installing Python and Setting Up Your Environment

## What It Means to Install Python

Before you can write Python code, you need Python installed on your computer. Here's what that means:

**Installing Python** means downloading the Python interpreter (the software that reads and executes Python code) and placing it on your computer so your operating system knows where to find it.

Think of it this way: Python code is like instructions in a foreign language. Python (the interpreter) is like the translator who understands that language. Without the translator on your computer, your computer doesn't know what to do with Python code.

When you install Python, you're telling your computer: "Hey, I'm adding a translator. When you see Python code, use this translator to understand it."

### Where Python Lives

Depending on your operating system, Python installs in different locations:

- **Windows**: Usually in `C:\Users\YourName\AppData\Local\Programs\Python\Python313\` or similar
- **macOS**: Usually in `/usr/local/bin/python3` or `/opt/homebrew/bin/python3`
- **Linux**: Usually in `/usr/bin/python3` or `/usr/local/bin/python3`

You don't need to remember these paths. Your operating system will remember them for you once Python is installed.

## Why Python 3.14.0?

This book teaches Python 3.14.0 (the latest Python 3 release verified at https://www.python.org/downloads/). This is the modern version with the latest improvements, performance enhancements, and security updates.

## Installation Steps: Choose Your Operating System

### Windows Installation

**Step 1: Download Python**
1. Go to [python.org](https://www.python.org/downloads/)
2. Click "Download Python 3.14.0" (the yellow button at the top)
3. Click the installer file to download it

**Step 2: Run the Installer**
1. Open your Downloads folder
2. Double-click the file `python-3.14.0-amd64.exe`
3. A window appears asking you to install Python

**Step 3: Critical Step - Add Python to PATH**
1. **CHECK THE BOX** that says "Add Python 3.14 to PATH"
2. This is important! It tells Windows where to find Python when you type commands
3. Click "Install Now"
4. Wait for installation to complete

**Step 4: Verify Installation**
1. Open Command Prompt (press Windows key, type "cmd", press Enter)
2. Type this command:
   ```
   python --version
   ```
3. You should see:
   ```
   Python 3.14.0
   ```

If you see "command not found" or similar error, see the troubleshooting section below.

### macOS Installation

**Step 1: Check If Python 3 Exists**
1. Open Terminal (press Command+Space, type "terminal", press Enter)
2. Type:
   ```
   python3 --version
   ```
3. If you see Python 3.14.0, you're already set! Skip to "Verify Installation" below
4. If you see an older version, continue to Step 2

**Step 2: Install Using Homebrew (Recommended)**
If you have Homebrew installed:
1. Open Terminal
2. Type:
   ```
   brew install python@3.14
   ```
3. Wait for installation to complete
4. Verify with `python3 --version`

**Step 3: Or Download Directly**
If you don't have Homebrew:
1. Go to [python.org](https://www.python.org/downloads/)
2. Click "Download Python 3.14.0"
3. Download the macOS installer
4. Double-click the installer and follow the on-screen instructions

**Step 4: Verify Installation**
1. Open Terminal
2. Type:
   ```
   python3 --version
   ```
   (Note: On macOS, the command is `python3`, not `python`)
3. You should see: `Python 3.14.0`

### Linux Installation

Linux distributions have different package managers. Here are the most common:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3.14
python3 --version
```

**Fedora/RHEL:**
```bash
sudo dnf install python3.14
python3 --version
```

**Arch:**
```bash
sudo pacman -S python
python --version
```

If your package manager doesn't have Python 3.14 yet, you can:
1. Use your current Python 3.x version (3.13, 3.12 are fine for learning)
2. Or download and install directly from [python.org](https://www.python.org/downloads/)

## Verification: You're Ready

After installation, open your terminal (Command Prompt on Windows) and run:

```
python --version
```

or on macOS/Linux:

```
python3 --version
```

You should see output like:
```
Python 3.14.0
```

**If you see this, you've succeeded. Your environment is ready.**

If you see an error or an older version, you can still proceed with an older Python 3.x version (3.13, 3.12)—the concepts are the same.

## Understanding Virtual Environments

For larger projects, Python developers use **virtual environments**—isolated spaces where each project has its own dependencies. You'll learn about this in Chapter 17+. For now, just know that virtual environments exist and why they matter: they prevent conflicts between different projects' requirements.

**Why latest Python?** Always use the latest stable Python version for new projects. It has performance improvements, better error messages, and security patches. Legacy support for older versions is for maintaining existing code, not for learning.

## Try With AI

Use your AI companion (Claude Code or Gemini CLI). You'll verify your installation and explore what's happening.

### Prompt 1: Verify Installation Success
```
I just installed Python and want to verify it works. What command should I run,
and what output should I see if installation was successful?
```

**Expected outcome**: AI tells you to run `python --version` (or `python3 --version` on macOS/Linux) and describes what successful output looks like.

### Prompt 2: Troubleshoot Installation Errors
```
I tried to install Python but got this error: [describe your error].
What does this mean and how do I fix it?
```

**Expected outcome**: AI explains the error and provides step-by-step fixing instructions.

### Prompt 3: Understand Python Versions
```
I see Python 3.13 installed on my computer, but the course says to use 3.14.0.
Do I need to upgrade, or can I use 3.13 for learning?
```

**Expected outcome**: AI explains that either version works for learning; 3.14.0 is recommended but not required.

### Prompt 4: Understand PATH
```
What does 'PATH' mean when the Windows installer asked to 'Add Python to PATH'?
Why is that important?
```

**Expected outcome**: AI explains PATH as a system variable that tells your computer where to find programs.

**Checkpoint**: Once you see `python --version` showing Python 3.14.0 (or 3.13+), you're ready for Lesson 3.

**Safety Note**: Python installation is safe. You're not changing anything dangerous—you're adding a translator to your computer. If something goes wrong, uninstall and try again. Never hesitate to ask AI for help with installation problems.

**Next**: Once your Python installation is verified, move to Lesson 3: Your First Program.
