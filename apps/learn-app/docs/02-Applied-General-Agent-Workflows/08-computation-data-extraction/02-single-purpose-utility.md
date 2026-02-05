---
sidebar_position: 3
title: "Your First Python Utility"
chapter: 8
lesson: 2
duration_minutes: 25
description: "Build a reusable Python script that reads numbers from stdin and calculates their sum"
keywords:
  [
    "stdin",
    "stdout",
    "pipe operator",
    "python script",
    "unix philosophy",
    "single-purpose tool",
    "command line",
  ]

skills:
  - name: "Writing stdin-reading Scripts"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can write a Python script using sys.stdin to read piped input"

  - name: "Using the Pipe Operator"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can use | to connect bash commands to Python scripts for data processing"

learning_objectives:
  - objective: "Write Python script that reads numbers from stdin and calculates their sum"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student creates working sum.py that correctly sums numbers piped to it"

  - objective: "Use pipe operator to connect Bash commands to Python scripts"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student successfully executes: echo '10.5' | python sum.py"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (stdin, stdout, pipe operator, sys.stdin, line iteration) within A2 limit"

differentiation:
  extension_for_advanced: "Add error handling for non-numeric lines, explore sys.argv for command-line arguments"
  remedial_for_struggling: "Start with hardcoded list sum, then introduce stdin as 'the list coming from outside'"
---

# Your First Python Utility

In Lesson 1, you discovered that Bash fails at decimal arithmetic and that LLMs hallucinate calculations. The solution? Push math into code that executes. Now you'll build your first single-purpose utility - a Python script that does one thing well: sum numbers.

This lesson introduces a pattern you'll use throughout your agent-building career. The Unix philosophy - small tools that do one thing and connect through pipes - becomes the foundation for reliable AI workflows. When a general agent needs accurate calculations, it doesn't hope the LLM gets the math right. It calls a script.

## Why Single-Purpose Tools Matter

Consider how traditional software works. You open a spreadsheet application to sum a column. That application has menus, toolbars, formatting options, chart wizards - thousands of features you don't need when you just want to add numbers.

Now consider the Unix approach. You have a tiny script that reads numbers and outputs a sum. Nothing else. No menus, no options, no features. Just input, calculation, output.

This minimalism isn't a limitation. It's a superpower.

Single-purpose tools are:

- **Predictable**: Same input always produces same output
- **Composable**: Connect them with pipes to build complex workflows
- **Testable**: One function means one thing to verify
- **Debuggable**: When something breaks, you know exactly where to look

The General Agent orchestrates these simple tools. The agent decides _what_ to calculate and _when_. The script handles _how_ to calculate accurately. Clean separation.

## Standard Input: The Universal Receiver

Before writing code, you need to understand how programs receive data in Unix-like systems. Every program has three standard streams:

| Stream | Name            | Purpose              | Example               |
| ------ | --------------- | -------------------- | --------------------- |
| stdin  | Standard Input  | Where data comes IN  | Keyboard, piped data  |
| stdout | Standard Output | Where results go OUT | Terminal display      |
| stderr | Standard Error  | Where errors go      | Error messages        |

Think of stdin as an inbox. Your program sits waiting, and data arrives through this inbox. The program doesn't care where the data originated - it could be from a file, from another program, or from keyboard typing. All that matters is: data arrives, program processes it.

This is what makes Unix tools so powerful. A program that reads from stdin can receive data from _any_ source. Write it once, connect it to anything.

## Building sum.py

Let's build your first single-purpose utility. Create a new file called `sum.py`:

```python
#!/usr/bin/env python3
# sum.py - Sum numbers from stdin
import sys

total = 0
for line in sys.stdin:
    line = line.strip()
    if line:  # Skip empty lines
        total += float(line)

print(f"Total: {total}")
```

That's the entire script. Let's break down what each part does.

**Line 1**: The shebang `#!/usr/bin/env python3` tells Unix systems how to run this file directly.

**Line 3**: `import sys` brings in Python's system module, which gives us access to stdin.

**Line 5**: Initialize the running total at zero.

**Line 6**: `for line in sys.stdin` reads lines one at a time from standard input. This loop continues until there's no more input.

**Line 7**: `.strip()` removes whitespace and newlines from each line.

**Line 8-9**: Skip empty lines, convert to float, add to total.

**Line 11**: Print the result.

Save this file in a working directory. We'll test it next.

## New Commands: echo and File Redirection

You already know `cat` and pipes from previous chapter. This lesson introduces two new commands for creating test data.

| Command | What It Does | Memory Trick |
|---------|-------------|--------------|
| `echo` | Prints text to stdout | **echo** = repeat what I say |
| `>` | Redirects output to a file | Arrow points where data goes |

### The echo Command

`echo` prints whatever you give it:

```bash
echo "Hello"
# Output: Hello

echo "10.5"
# Output: 10.5
```

The `-e` flag enables escape sequences like `\n` for newlines:

```bash
echo -e "Line 1\nLine 2\nLine 3"
# Output:
# Line 1
# Line 2
# Line 3
```

Without `-e`, the `\n` would print literally instead of creating new lines.

### File Redirection with >

The `>` operator sends output to a file instead of the screen:

```bash
echo "Hello" > greeting.txt
# Creates greeting.txt containing "Hello"
```

**Warning**: `>` overwrites the file if it exists. Use `>>` to append instead.

## Testing Your Script

Now let's use these commands to test your script. The simplest way to send data to stdin is with `echo` and the pipe operator (`|`):

```bash
echo "10.5" | python sum.py
```

**Output:**

```
Total: 10.5
```

The `echo` command outputs "10.5". The pipe (`|`) redirects that output to become the stdin of `python sum.py`. Your script receives "10.5" and sums it.

Now try multiple numbers. Use `echo -e` to include newlines:

```bash
echo -e "10.5\n20.3\n5.2" | python sum.py
```

**Output:**

```
Total: 36.0
```

Three numbers, correctly summed with decimals. Bash couldn't do this, but your Python utility handles it effortlessly.

## The Pipe Operator: Connecting Commands

The pipe operator (`|`) is the glue of Unix. It connects programs together, letting data flow from one to the next.

Here's what happens when you run `echo "10.5" | python sum.py`:

```
┌─────────────────┐     ┌─────────────────┐
│      echo       │     │    sum.py       │
│                 │────▶│                 │
│  outputs text   │  │  │  reads stdin    │
│  to stdout      │  │  │  calculates sum │
│                 │  │  │  prints total   │
└─────────────────┘  │  └─────────────────┘
                     │
        pipe (|) ────┘
   redirects stdout → stdin
```

The pipe takes whatever `echo` writes to stdout and feeds it directly into your script's stdin. No temporary files, no manual copying. Pure data flow.

## Reading from Files

Your script already works with files - just use `cat` to read the file and pipe it:

```bash
# Create a test file
echo -e "100.50\n25.75\n14.25" > expenses.txt

# Sum the file contents
cat expenses.txt | python sum.py
```

**Output:**

```
Total: 140.5
```

The `cat` command reads `expenses.txt` and sends it to stdout. The pipe redirects that to your script. Your script sees the same data it would see from `echo` - it doesn't know or care that it came from a file.

This is the power of stdin: your tool works with any data source without modification.

## Practice: Build and Test Your sum.py

Now it's your turn. Follow these steps:

**Step 1**: Create the sum.py script in your working directory.

```python
#!/usr/bin/env python3
# sum.py - Sum numbers from stdin
import sys

total = 0
for line in sys.stdin:
    line = line.strip()
    if line:
        total += float(line)

print(f"Total: {total}")
```

**Step 2**: Test with a single number.

```bash
echo "42.5" | python sum.py
```

**Expected output:**

```
Total: 42.5
```

**Step 3**: Test with multiple numbers.

```bash
echo -e "10\n20\n30.5" | python sum.py
```

**Expected output:**

```
Total: 60.5
```

**Step 4**: Test decimal precision.

```bash
echo -e "0.1\n0.2" | python sum.py
```

**Expected output:**

```
Total: 0.30000000000000004
```

Wait - what? `0.1 + 0.2` should equal `0.3`, not `0.30000000000000004`. This is floating-point arithmetic behavior, not a bug in your script. For most purposes, this tiny imprecision is fine. For financial applications requiring exact decimals, Python offers the `decimal` module (which you can explore as an extension).

**Step 5**: Test with a file.

```bash
# Create test data
echo -e "127.89\n45.50\n12.99" > test_numbers.txt

# Sum the file
cat test_numbers.txt | python sum.py
```

**Expected output:**

```
Total: 186.38
```

## Why This Pattern Matters for General Agents

When you use a general agent like Claude Code to process numerical data, here's what actually happens:

1. You give the agent a list of expenses
2. The agent **writes a script** just like `sum.py` to sum the amounts
3. The agent **calls the script** and reads the verified result

This is no longer a black box. You now understand exactly what the agent is doing - the same pattern you just built yourself.

This is **Principle 1 (Bash is the Key)** and **Principle 2 (Code as Universal Interface)** working together. Bash connects the tools; Python executes the logic.

## Connecting to the Seven Principles

This lesson demonstrates two principles from Chapter 3:

**Principle 1: Bash is the Key**

You used Bash commands (`echo`, `cat`) and the pipe operator to orchestrate data flow. The shell is the conductor; your script is one instrument in the orchestra.

**Principle 2: Code as Universal Interface**

Instead of hoping an LLM calculates correctly, you wrote code that executes. The script is a contract: given numbers, return their sum. No ambiguity, no hallucination, no "approximately 186."

In the next lesson, you'll add **Principle 3: Verification as Core Step** - testing your script systematically and checking exit codes to confirm success.

## Try With AI

Use these prompts with Claude Code or your preferred AI assistant to deepen your understanding.

### Prompt 1: Extend the Script

```
I have a Python script that sums numbers from stdin:

import sys
total = 0
for line in sys.stdin:
    line = line.strip()
    if line:
        total += float(line)
print(f"Total: {total}")

Can you modify it to also print:
- The count of numbers
- The average
- The minimum and maximum values
```

**What you're learning:** You're iterating with AI to extend your tool. The script stays single-purpose (process numbers) but gains useful features. Notice how the AI preserves the stdin reading pattern while adding functionality.

### Prompt 2: Handle Errors

```
My sum.py script crashes when it encounters a non-numeric line.
For example, if the input has a header like "Amount" followed by numbers.

How do I make it skip non-numeric lines gracefully instead of crashing?
Show me how to use try/except for this.
```

**What you're learning:** You're teaching AI about YOUR specific problem and asking for a solution. This is the collaborative refinement loop - you identify the limitation, AI suggests the fix.

### Prompt 3: Understand stdin Better

```
I'm trying to understand how stdin works in Python.

When I run: echo "10" | python sum.py
What exactly happens? How does the "10" get from echo to my Python script?

Also, why does sys.stdin work like a file? Can I use read() instead of iterating?
```

**What you're learning:** You're using AI as a teacher to deepen conceptual understanding. The AI explains the Unix pipe mechanism and Python's file-like interface. This knowledge helps you write more sophisticated tools later.
