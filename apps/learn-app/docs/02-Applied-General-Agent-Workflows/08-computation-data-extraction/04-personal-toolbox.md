---
sidebar_position: 5
title: "Personal Toolbox"
chapter: 7
lesson: 4
duration_minutes: 20
description: "Transform scripts into persistent personal commands using executables and aliases"
keywords:
  [
    "chmod",
    "executable",
    "shebang",
    "alias",
    "bashrc",
    "zshrc",
    "persistent tools",
  ]

skills:
  - name: "Making Scripts Executable"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "System Administration"
    measurable_at_this_level: "Student adds shebang line and uses chmod +x to make Python script directly executable"

  - name: "Creating Shell Aliases"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Automation"
    measurable_at_this_level: "Student creates alias in shell config and verifies it persists across sessions"

learning_objectives:
  - objective: "Make script executable and invoke directly"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student runs ./calc.py successfully without python prefix"

  - objective: "Create shell alias for persistent access"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Student creates alias, adds to shell config, verifies persistence after terminal restart"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (shebang line, chmod +x, executable permission, alias command, shell config files, persistence) within A2 limit"

differentiation:
  extension_for_advanced: "Add script to PATH instead of alias, create wrapper function with default arguments"
  remedial_for_struggling: "Focus on just alias creation - skip executable if overwhelmed, alias achieves same goal"
---

# Personal Toolbox

You have built `calc.py`. It works. You tested it in Lesson 3. Every time you want to use it, you type:

```bash
cat receipts.txt | python ~/calc.py
```

That command is correct but tedious. You want something simpler:

```bash
cat receipts.txt | add-up
```

One word. `add-up`. Like a real command. Like `cat` or `grep` or `ls`. Your script should feel like part of the operating system—because you are about to make it part of your operating system.

This lesson transforms your script into a persistent personal command. By the end, you will have extended your shell with a tool that exists nowhere else in the world. Every future terminal session will have access to it. You will have built the first piece of your personal toolbox.

## The Two Paths to Personal Commands

There are two ways to turn a script into a command:

| Approach              | What It Does                    | Best For                                  |
| --------------------- | ------------------------------- | ----------------------------------------- |
| **Executable Script** | Make the script itself runnable | Scripts you invoke with `./` or from PATH |
| **Shell Alias**       | Create a shortcut name          | Quick access to any command               |

We will do both. The executable approach teaches you how Unix programs work. The alias approach gives you the fastest daily workflow.

## Making Your Script Executable

Right now, `calc.py` is just a text file. Your shell does not know it can be run as a program. Try running it directly:

```bash
./calc.py
# Output: bash: ./calc.py: Permission denied
```

The shell refuses. Even though Python can interpret this file, the operating system does not know that. We need to tell it two things:

1. **What program should run this file** (the shebang line)
2. **That this file is allowed to be executed** (the permission flag)

### Step 1: Add the Shebang Line

Open `calc.py` and add this line at the very top:

```python
#!/usr/bin/env python3
# calc.py - Now with shebang line!
import sys

total = sum(float(line.strip()) for line in sys.stdin if line.strip())
print(f"Total: {total:.2f}")
```

The first line (`#!/usr/bin/env python3`) is called a **shebang**. When the operating system sees a file that starts with `#!`, it reads the rest of that line to find the interpreter.

Breaking it down:

- `#!` — The shebang marker. Tells the OS "this file specifies its own interpreter"
- `/usr/bin/env` — A program that finds other programs in your PATH
- `python3` — The interpreter to use

Why `/usr/bin/env python3` instead of just `/usr/bin/python3`? Because Python might be installed in different locations on different systems. The `env` command looks up `python3` in your PATH, making the script portable across machines.

### Step 2: Set the Executable Permission

Files have permissions that control what you can do with them. By default, text files are readable but not executable. Change that with `chmod`:

```bash
chmod +x calc.py
```

The `chmod` command changes file permissions. The `+x` flag adds executable permission. You can verify the change:

```bash
ls -l calc.py
# Output: -rwxr-xr-x 1 user user 142 Jan 30 10:00 calc.py
```

See the `x` in `-rwxr-xr-x`? That means executable. Before `chmod +x`, it would have been `-rw-r--r--` (no `x`).

### Step 3: Run Directly

Now you can run the script without the `python` prefix:

```bash
echo -e "10\n20\n30" | ./calc.py
# Output: Total: 60.00
```

The `./` tells the shell "run the file in the current directory." Without it, the shell would search your PATH and not find `calc.py`.

You have now made `calc.py` an executable program. But you still need the `./` prefix and the full path. Let us fix that with an alias.

## Creating a Shell Alias

An alias is a shortcut—a name that expands to a longer command. You define an alias like this:

```bash
alias add-up='python ~/calc.py'
```

Now test it:

```bash
echo -e "10\n20\n30" | add-up
# Output: Total: 60.00
```

The shell sees `add-up`, expands it to `python ~/calc.py`, and runs that. You have created a personal command.

But there is a problem. Close your terminal. Open a new one. Try the alias:

```bash
echo -e "10\n20" | add-up
# Output: bash: add-up: command not found
```

The alias is gone. It only existed in that terminal session. To make it permanent, you need to save it in your shell's configuration file.

## Making Aliases Persistent

Your shell reads a configuration file every time it starts. For Bash, this is `~/.bashrc`. For Zsh (default on macOS), this is `~/.zshrc`. You will add your alias to this file.

### Step 1: Identify Your Shell

First, check which shell you are using:

```bash
echo $SHELL
# Output: /bin/bash   (or /bin/zsh on macOS)
```

### Step 2: Add the Alias to Your Config

For Bash users:

```bash
echo "alias add-up='python ~/calc.py'" >> ~/.bashrc
```

For Zsh users:

```bash
echo "alias add-up='python ~/calc.py'" >> ~/.zshrc
```

The `>>` operator appends to the file without overwriting existing content.

### Step 3: Reload Your Configuration

The shell does not automatically notice changes to its config file. Tell it to reload:

For Bash:

```bash
source ~/.bashrc
```

For Zsh:

```bash
source ~/.zshrc
```

### Step 4: Verify Persistence

Test that the alias works:

```bash
echo -e "5\n5\n5" | add-up
# Output: Total: 15.00
```

Now close your terminal completely. Open a new terminal. Run the alias again:

```bash
echo -e "100\n200" | add-up
# Output: Total: 300.00
```

The alias persists. You have permanently extended your shell.

## The Complete Workflow

Let us trace what you have accomplished:

```bash
# Before: Tedious full command
cat receipts.txt | python ~/scripts/calc.py

# After: Your personal command
cat receipts.txt | add-up
```

You have:

1. Added a shebang line so the script knows its interpreter
2. Set executable permission with `chmod +x`
3. Created an alias for quick access
4. Made the alias persistent in your shell config

Your `add-up` command will now exist in every terminal session, on this machine, forever. Unless you remove it.

## What You Have Built

Step back and see what you have done across these four lessons:

| Lesson                    | What You Built                         | Principle Demonstrated            |
| ------------------------- | -------------------------------------- | --------------------------------- |
| 1. Accuracy Gap           | Recognized Bash arithmetic limits      | P3: Verification reveals failures |
| 2. Single-Purpose Utility | Created `calc.py` reading stdin        | P2: Code as Universal Interface   |
| 3. Testing Loop           | Verified with exit codes and test data | P3: Verification as Core Step     |
| 4. Personal Toolbox       | Made it a persistent command           | P5: Persisting State in Files     |

You started with a problem (inaccurate calculations) and ended with a solution (a personal tool that works every time). This is the agent-building pattern: identify a need, build a solution, verify it works, make it accessible.

The alias you created is saved in `~/.bashrc` or `~/.zshrc`—a file. The script is saved in `~/calc.py`—a file. Your tools persist because they exist in the file system, not in memory. This is **Principle 5: Persisting State in Files** in action.

And the entire workflow—from piping data to executing scripts to checking results—runs through Bash. This is **Principle 1: Bash is the Key**.

## Extending Your Toolbox

You can create more aliases for any command you use frequently:

```bash
# Count lines in a file
alias wc-lines='wc -l'

# Find all Python files
alias find-py='find . -name "*.py"'

# Quick directory navigation
alias proj='cd ~/projects'

# Git shortcuts
alias gs='git status'
alias gd='git diff'
```

Each alias is a small investment that pays off every time you use it. Your shell becomes increasingly customized to your workflow.

## Practice: Build Your Personal Command

Follow these steps to create your own `add-up` command:

**Step 1**: Ensure your `calc.py` has the shebang line:

```python
#!/usr/bin/env python3
import sys

total = sum(float(line.strip()) for line in sys.stdin if line.strip())
print(f"Total: {total:.2f}")
```

**Step 2**: Make it executable:

```bash
chmod +x ~/calc.py
```

**Step 3**: Add the alias to your shell config:

```bash
# For Bash
echo "alias add-up='python ~/calc.py'" >> ~/.bashrc && source ~/.bashrc

# For Zsh
echo "alias add-up='python ~/calc.py'" >> ~/.zshrc && source ~/.zshrc
```

**Step 4**: Test it:

```bash
echo -e "1\n2\n3\n4\n5" | add-up
# Output: Total: 15.00
```

**Step 5**: Close your terminal, open a new one, and verify persistence:

```bash
echo -e "100" | add-up
# Output: Total: 100.00
```

You now have a permanent personal command.

## Try With AI

### Prompt 1: Understanding chmod

```
Explain what chmod +x does and why it's needed to run a Python script directly.

I have a script called calc.py. When I try to run ./calc.py, I get "Permission denied."
After running chmod +x calc.py, it works.

What exactly changed? What do the letters in "-rwxr-xr-x" mean?
```

**What you are learning:** AI teaches Unix file permissions—the rwx system that controls who can read, write, and execute files. This is foundational knowledge for working with scripts and executables.

### Prompt 2: Making the Command Work from Any Directory

```
I created an alias in my .bashrc:
alias add-up='python calc.py'

It works when I'm in the directory where calc.py is located.
But when I cd to another directory, the alias fails with "No such file or directory."

How do I make this alias work from any directory?
```

**What you are learning:** You teach AI your specific problem (relative vs. absolute paths). The solution—using the full path like `~/calc.py` or `/home/user/calc.py`—emerges from the conversation. You understand why absolute paths matter.

### Prompt 3: Setting Up Persistent Aliases

```
Help me set up a persistent alias in my shell configuration.

I'm using [Bash/Zsh] on [macOS/Linux/WSL].
I want to create an alias called "add-up" that runs "python ~/calc.py".

Walk me through:
1. Which config file to edit (.bashrc or .zshrc)
2. How to add the alias
3. How to reload the config
4. How to verify it persists after closing the terminal
```

**What you are learning:** Collaborative setup where you specify your environment and AI provides the exact commands. This is the convergence pattern—you provide context, AI provides procedure, you verify results.
