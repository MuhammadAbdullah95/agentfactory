---
sidebar_position: 3
title: "The Single-Purpose Python Utility"
chapter: 7
lesson: 2
duration_minutes: 25
description: "Build a reusable Python script that reads from stdin and calculates sums"
keywords:
  [
    "stdin",
    "stdout",
    "pipe operator",
    "python script",
    "unix philosophy",
    "single-purpose tool",
  ]

# HIDDEN SKILLS METADATA
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
    measurable_at_this_level: "Student can use | to connect bash commands to Python scripts"

learning_objectives:
  - objective: "Write Python script that reads from stdin and sums numbers"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student creates working calc.py that correctly sums piped input"

  - objective: "Use pipe operator to connect Bash commands to Python scripts"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student successfully executes: cat numbers.txt | python calc.py"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (stdin, stdout, pipe operator, sys.stdin, float conversion, sum function) within A2 limit"

differentiation:
  extension_for_advanced: "Add error handling for non-numeric lines, explore sys.stdin.read() vs line iteration"
  remedial_for_struggling: "Start with hardcoded list sum, then introduce stdin as 'the list coming from outside'"
---

# The Single-Purpose Python Utility

In Lesson 1, you discovered that Bash fails at decimal arithmetic and that LLMs hallucinate calculations. The solution? Push math into code that executes. Now you'll build your first single-purpose utility, a Python script that does one thing well: sum numbers from any source.

This lesson introduces a pattern you'll use throughout your agent-building career. The Unix philosophy, small tools that do one thing and connect through pipes—becomes the foundation for reliable AI workflows. When an agent needs accurate calculations, it doesn't hope the LLM gets the math right. It calls a script.

## Why Single-Purpose Tools Matter

Consider how traditional software works. You open a spreadsheet application to sum numbers. That application has menus, toolbars, formatting options, chart wizards—thousands of features you don't need when you just want to add numbers.

Now consider the Unix approach. You have a tiny script that reads numbers and outputs their sum. Nothing else. No menus, no options, no features. Just input, calculation, output.

This minimalism isn't a limitation. It's a superpower.

Single-purpose tools are:

- **Predictable**: Same input always produces same output
- **Composable**: Connect them with pipes to build complex workflows
- **Testable**: One function means one thing to verify
- **Debuggable**: When something breaks, you know exactly where to look

When you build AI agents, they orchestrate these simple tools. The agent decides _what_ to calculate and _when_. The script handles _how_ to calculate accurately. Clean separation.

## Standard Input: The Universal Receiver

Before writing code, you need to understand how programs receive data in Unix-like systems. Every program has three standard streams:

| Stream | Name            | Purpose              | Example               |
| ------ | --------------- | -------------------- | --------------------- |
| stdin  | Standard Input  | Where data comes IN  | Keyboard, piped files |
| stdout | Standard Output | Where results go OUT | Terminal display      |
| stderr | Standard Error  | Where errors go      | Error messages        |

Think of stdin as an inbox. Your program sits waiting, and data arrives through this inbox. The program doesn't care where the data originated—it could be from a file, from another program, or from keyboard typing. All that matters is: data arrives, program processes it.

This is what makes Unix tools so powerful. A program that reads from stdin can receive data from _any_ source. Write it once, connect it to anything.

## Building calc.py

Let's build your first single-purpose utility. Create a new file called `calc.py`:

```python
# calc.py - A single-purpose calculation utility
import sys

total = sum(float(line.strip()) for line in sys.stdin if line.strip())
print(f"Total: {total:.2f}")
```

That's the entire script. Let's break down what each part does.

**Line 1**: `import sys` brings in Python's system module, which gives us access to stdin.

**Line 2**: This dense line does several things:

- `sys.stdin` reads from standard input
- `for line in sys.stdin` iterates through each line
- `line.strip()` removes whitespace and newlines
- `if line.strip()` skips empty lines
- `float(line.strip())` converts text to decimal numbers
- `sum(...)` adds all the numbers together

**Line 3**: Prints the result formatted to 2 decimal places.

Save this file in a working directory. We'll test it next.

## Testing with Manual Input

Before connecting pipes, verify the script works with keyboard input:

```bash
python calc.py
```

The script will wait for input. Type some numbers, one per line:

```
10.5
20.3
5.2
```

Press `Ctrl+D` (Unix) or `Ctrl+Z then Enter` (Windows) to signal end of input.

```
Total: 36.00
```

The script read your typed input through stdin, converted each line to a float, summed them, and printed the result. If you see `Total: 36.00`, your script works.

## The Pipe Operator: Connecting Commands

Now for the key insight: instead of typing numbers manually, you can send them from a file or another command. The pipe operator (`|`) connects the output of one command to the input of another.

First, create a test file:

```bash
echo -e "10.5\n20.3\n5.2" > numbers.txt
```

This creates `numbers.txt` with three numbers, one per line. Verify the file:

```bash
cat numbers.txt
```

Output:

```
10.5
20.3
5.2
```

Now pipe the file contents to your script:

```bash
cat numbers.txt | python calc.py
```

Output:

```
Total: 36.00
```

The `cat` command reads the file and sends it to stdout. The pipe (`|`) redirects that stdout to become the stdin of `python calc.py`. Your script receives the numbers exactly as if you'd typed them.

## Understanding Data Flow

Let's trace exactly what happens when you run `cat numbers.txt | python calc.py`:

```
┌─────────────────┐     ┌───────────────┐     ┌─────────────────┐
│   numbers.txt   │     │     cat       │     │    calc.py      │
│                 │────▶│               │────▶│                 │
│  10.5           │     │  reads file   │  │  │  reads stdin    │
│  20.3           │     │  writes to    │  │  │  converts to    │
│  5.2            │     │  stdout       │  │  │  floats         │
│                 │     │               │  │  │  sums them      │
└─────────────────┘     └───────────────┘  │  │  prints total   │
                                           │  └─────────────────┘
                              pipe (|) ────┘
                        redirects stdout → stdin
```

The pipe is the key connector. It takes whatever one program writes to stdout and feeds it directly into the next program's stdin. No temporary files, no manual copying. Pure data flow.

## Why This Pattern Matters for Agents

When you build AI agents later in this book, they'll need to perform calculations. Consider this workflow:

1. Agent extracts numbers from a document
2. Agent needs to sum those numbers accurately
3. Agent reports the result

Without your utility, the agent might try to calculate mentally (hallucination risk) or ask the LLM to calculate (still hallucination risk). With your utility:

```bash
# Agent generates this command
echo "extracted numbers" | python calc.py
```

The agent constructs the command, executes it, and reads the verified result. No hallucination possible—the calculation ran in real code.

This is **Principle 1 (Bash is the Key)** and **Principle 2 (Code as Universal Interface)** working together. Bash connects the tools; Python executes the logic.

## Practice: Build and Test Your calc.py

Now it's your turn. Follow these steps:

**Step 1**: Create the calc.py script in your working directory.

```python
# calc.py - A single-purpose calculation utility
import sys

total = sum(float(line.strip()) for line in sys.stdin if line.strip())
print(f"Total: {total:.2f}")
```

**Step 2**: Create test data with known values.

```bash
echo -e "100\n200\n300" > test_numbers.txt
```

Expected sum: 600.00

**Step 3**: Run the test.

```bash
cat test_numbers.txt | python calc.py
```

Expected output:

```
Total: 600.00
```

**Step 4**: Test with decimal precision.

```bash
echo -e "0.1\n0.2" > decimals.txt
cat decimals.txt | python calc.py
```

Expected output:

```
Total: 0.30
```

Remember Lesson 1: Bash would fail here. Your Python script handles decimals correctly.

**Step 5**: Test with an empty file.

```bash
echo "" > empty.txt
cat empty.txt | python calc.py
```

Expected output:

```
Total: 0.00
```

Your script gracefully handles empty input because of the `if line.strip()` filter.

## Connecting to the Seven Principles

This lesson demonstrates two principles from Chapter 3:

**Principle 1: Bash is the Key**

You used Bash commands (`cat`, `echo`) and the pipe operator to orchestrate data flow. The shell is the conductor; your script is one instrument in the orchestra.

**Principle 2: Code as Universal Interface**

Instead of hoping an LLM calculates correctly, you wrote code that executes. The script is a contract: given numbers, return their sum. No ambiguity, no hallucination, no "approximately 36."

In the next lesson, you'll add **Principle 3: Verification as Core Step**—testing your script systematically and checking exit codes to confirm success.

## Try With AI

Use these prompts with Claude Code or your preferred AI assistant to deepen your understanding.

### Prompt 1: Generate a stdin-reading script

```
Write a Python script that reads numbers from stdin (one per line) and calculates their sum.
The script should:
- Handle decimal numbers
- Skip empty lines
- Format the output to 2 decimal places
```

**What you're learning:** The AI suggests the `sys.stdin` pattern without you knowing it beforehand. Notice how it handles the conversion from text lines to numbers. Compare its solution to the calc.py you just built.

### Prompt 2: Add error handling

```
Take this calc.py script and add error handling for non-numeric lines:

import sys
total = sum(float(line.strip()) for line in sys.stdin if line.strip())
print(f"Total: {total:.2f}")

When a line isn't a valid number, skip it and optionally warn the user.
```

**What you're learning:** You're teaching the AI your robustness requirements. You know the script works for clean input—now you're specifying how it should handle messy real-world data. This is the student-teaches-AI dynamic.

### Prompt 3: Explain and optimize

```
I have this Python script that sums numbers from stdin:

import sys
total = sum(float(line.strip()) for line in sys.stdin if line.strip())
print(f"Total: {total:.2f}")

Can you explain what each part does in simple terms?
Then suggest if there's a more readable way to write the same logic.
```

**What you're learning:** You're iterating together toward clearer code. The AI might suggest breaking the one-liner into multiple lines for readability, or it might explain why the generator expression is actually clearer. Either way, you're improving your understanding through dialogue.
