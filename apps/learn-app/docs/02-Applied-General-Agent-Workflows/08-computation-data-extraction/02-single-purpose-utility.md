---
sidebar_position: 3
title: "Your First Python Utility"
chapter: 8
lesson: 2
layer: L2
duration_minutes: 25
description: "Watch Claude Code build a reusable Python script that sums decimal numbers, then learn the pattern that made it work"
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
  - name: "Directing Agent-Built Scripts"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Communication"
    measurable_at_this_level: "Student can direct Claude Code to build a script that solves their computation problem"

  - name: "Understanding stdin Patterns"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can explain how pipes connect commands to Python scripts"

  - name: "Script Reuse Pattern"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student recognizes when to ask for a script vs. a one-time calculation"

learning_objectives:
  - objective: "Direct Claude Code to build a Python script that sums numbers from stdin"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student successfully prompts Claude Code to create working sum.py"

  - objective: "Understand how pipe operator connects Bash commands to Python scripts"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can explain data flow in: cat file.txt | python sum.py"

  - objective: "Apply the computation prompt pattern to new problems"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student uses pattern to request different calculations (average, max, etc.)"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (agent-built scripts, stdin pattern, pipe data flow, reusable tools) within A2 limit"

differentiation:
  extension_for_advanced: "Ask agent to add error handling, statistics, or format options to the script"
  remedial_for_struggling: "Focus on the conversation and pattern. Run the commands, don't worry about understanding every line of code yet."
---

# Your First Python Utility

In Lesson 1, you discovered that Bash can't do decimal arithmetic and that LLMs hallucinate calculations. You know the problem. Now watch how a General Agent solves it.

Here's the scenario: You have a file of expenses. You need the total. Each line is a decimal number. What do you do?

Most people would open a spreadsheet, paste the numbers, write a SUM formula. That works for one-off tasks. But what about next month's expenses? Next year's? You'd repeat the same manual process.

You're going to do something different. You'll ask Claude Code to build a tool you can use forever.

## The Problem

You have a file called `expenses.txt`:

```
127.89
45.50
12.99
```

You need the total. Lesson 1 showed that `expr 127.89 + 45.50` fails. You could ask an LLM to calculate, but you'd get "approximately $186" or worse, a confidently wrong number.

You need code that executes.

## The Conversation

Open Claude Code and describe your problem:

```
You: I have a file with decimal numbers, one per line. I need to sum them.
Can you build me a script that reads numbers from stdin and prints the total?
```

Watch what Claude Code does:

```
Claude Code: I'll create a Python script that reads numbers from standard
input and sums them. This will work with piped data from any source.

[Creates: sum.py]

#!/usr/bin/env python3
# sum.py - Sum numbers from stdin
import sys

total = 0
for line in sys.stdin:
    line = line.strip()
    if line:  # Skip empty lines
        total += float(line)

print(f"Total: {total}")

Let me test it with your expenses:

[Runs: echo -e "127.89\n45.50\n12.99" | python sum.py]

Total: 186.38

The script works. You can now sum any file:
cat expenses.txt | python sum.py
```

That's it. In seconds, you have a reusable tool.

## What Just Happened?

You witnessed two principles in action.

**Principle 1: Bash is the Key.** The agent used `echo` and the pipe operator (`|`) to test the script. It didn't ask you to manually create test files. It used Bash to orchestrate the workflow.

**Principle 2: Code as Universal Interface.** Instead of calculating in its head (which would hallucinate), the agent wrote code that executes. The script is a contract: given numbers, return their exact sum. No approximation, no "about $186."

This is fundamentally different from asking "What's 127.89 + 45.50 + 12.99?" The agent created a tool that works on ANY list of numbers, not just these three.

### Why a Script Instead of a Direct Answer?

You might wonder: why not just calculate the answer directly?

Three reasons:

1. **Reusability.** Next month, you'll have new expenses. The script works on any file.
2. **Accuracy.** Code executes deterministically. LLM arithmetic hallucinates.
3. **Composability.** The script reads from stdin, so it connects to other tools via pipes.

The agent understood this without you explaining it. When you asked for "a script that reads from stdin," you signaled you wanted a reusable tool, not a one-time answer.

## The Agent's Toolkit: What sum.py Does

Let's decode what the agent built.

### The Shebang Line

```python
#!/usr/bin/env python3
```

This tells the operating system: "Run this file with Python 3." It's what allows you to eventually run `./sum.py` instead of `python sum.py`.

### Reading from stdin

```python
import sys

for line in sys.stdin:
    line = line.strip()
```

`sys.stdin` is Python's connection to "standard input" - data piped into the program. The `for line in sys.stdin` pattern reads one line at a time. The `.strip()` removes whitespace and newlines.

### The Calculation

```python
total = 0
for line in sys.stdin:
    line = line.strip()
    if line:  # Skip empty lines
        total += float(line)
```

- Start with `total = 0`
- For each line, convert to a decimal number (`float()`) and add to total
- Skip empty lines to handle trailing newlines in files

### The Output

```python
print(f"Total: {total}")
```

Print the result to "standard output" - the terminal, or wherever you pipe the result next.

### The Pipe Operator

When you run:

```bash
cat expenses.txt | python sum.py
```

Here's what happens:

```
┌─────────────────┐     ┌─────────────────┐
│      cat        │     │    sum.py       │
│                 │────▶│                 │
│  reads file     │  │  │  reads stdin    │
│  outputs text   │  │  │  calculates sum │
│                 │  │  │  prints total   │
└─────────────────┘  │  └─────────────────┘
                     │
        pipe (|) ────┘
   redirects stdout → stdin
```

The pipe takes whatever `cat` outputs and feeds it to your script's stdin. Your script doesn't know or care that the data came from a file. It just reads lines and sums them.

## The Pattern

Here's the prompt pattern you just used:

```
"I have [data problem]. Build me a script that [reads from stdin] and [produces output]."
```

This pattern works because:

1. **You describe the data problem**, not the implementation. The agent chooses Python, not you.
2. **You specify stdin/stdout**, which signals you want a composable Unix tool.
3. **The agent builds something reusable**, not a one-time answer.

### Pattern Variations

| Your Problem | The Prompt |
|--------------|------------|
| Sum numbers | "Build me a script that reads numbers from stdin and prints their sum" |
| Calculate average | "Build me a script that reads numbers from stdin and prints their average" |
| Find maximum | "Build me a script that reads numbers from stdin and prints the largest one" |
| Count lines | "Build me a script that reads from stdin and counts how many lines" |

The structure stays the same. The calculation changes.

## Try It Yourself

Create a test file and run the script:

```bash
# Create test data
echo -e "100.50\n25.75\n14.25" > test_numbers.txt

# Sum it
cat test_numbers.txt | python sum.py
```

**Expected output:**

```
Total: 140.5
```

Now try with different numbers:

```bash
echo -e "10\n20\n30.5" | python sum.py
```

**Expected output:**

```
Total: 60.5
```

The script handles integers and decimals. It works on any list of numbers you throw at it.

## Connecting to the Seven Principles

This lesson demonstrated two principles from Chapter 3:

**Principle 1: Bash is the Key**

You used Bash commands (`echo`, `cat`) and the pipe operator to orchestrate data flow. The shell is the conductor; your Python script is one instrument in the orchestra.

**Principle 2: Code as Universal Interface**

Instead of hoping an LLM calculates correctly, you have code that executes. The script is a contract: given numbers, return their sum. No ambiguity, no hallucination, no "approximately 186."

In the next lesson, you'll add **Principle 3: Verification as Core Step** - how do you know the script is correct? Exit code 0 means "didn't crash," not "right answer."

---

## Try With AI

### Prompt 1: Extend the Script

```
I have sum.py that reads numbers from stdin and prints the total.
Can you modify it to also print:
- The count of numbers
- The average
- The minimum and maximum values

Keep the stdin reading pattern so it still works with pipes.
```

**What you're learning:** Iterative development with AI. You have a working tool and clear requirements. The agent extends functionality while preserving the composable pattern. Notice how you specify "keep the stdin reading pattern" - you're directing the architecture.

### Prompt 2: Handle Errors

```
My sum.py crashes when the input has a header line like "Amount" before the numbers.
How do I make it skip non-numeric lines gracefully instead of crashing?
```

**What you're learning:** Collaborative debugging. You identify the limitation (crashes on headers), the agent suggests the fix (try/except). This is the refinement loop - you provide context, AI provides solution.

### Prompt 3: Understand the Pattern

```
I noticed sum.py uses "for line in sys.stdin" to read input.
Why does this work? How does the pipe operator connect cat's output to Python's stdin?
Explain the data flow step by step.
```

**What you're learning:** Conceptual understanding. The agent explains the Unix pipe mechanism. This knowledge helps you design more sophisticated workflows later. You're not just using tools - you're understanding how they connect.
