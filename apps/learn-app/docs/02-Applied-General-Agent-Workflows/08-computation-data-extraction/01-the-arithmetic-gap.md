---
sidebar_position: 2
title: "The Arithmetic Gap"
chapter: 8
lesson: 1
duration_minutes: 15
description: "Discover why Bash arithmetic fails with decimals and why LLM head-math is unreliable for real calculations"
keywords:
  [
    "bash arithmetic",
    "decimal math",
    "python calculation",
    "LLM hallucination",
    "calculation accuracy",
    "integer arithmetic",
  ]

skills:
  - name: "Recognizing Bash Arithmetic Limitations"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain why echo $((1.2 + 2.3)) fails and identify scenarios requiring Python"

  - name: "Identifying LLM Calculation Risks"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain why asking AI to do head math is unreliable for large datasets"

learning_objectives:
  - objective: "Explain why Bash arithmetic fails with decimal numbers"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student demonstrates understanding by predicting which calculations will fail"

  - objective: "Recognize when to use Python instead of Bash for calculations"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student correctly chooses appropriate tool for given calculation scenarios"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (Bash arithmetic, integer-only math, decimal failure) well within A2 limit"

differentiation:
  extension_for_advanced: "Research how bc and awk handle decimals, explore Python's decimal module for precision"
  remedial_for_struggling: "Focus on one example: Bash fails with 1.5+2.5, Python succeeds - understand just this before moving on"
---

# The Arithmetic Gap

:::info Python Required
This chapter builds Python utilities that run from your terminal. Before starting, verify Python is installed:

**macOS/Linux:**
```bash
python3 --version
```

**Windows (Command Prompt or PowerShell):**
```bash
python --version
```

If you see a version number (3.x), you're ready. If not, install Python from [python.org](https://www.python.org/downloads/) or use your system's package manager:

- **macOS**: `brew install python`
- **Ubuntu/Debian**: `sudo apt install python3`
- **Windows**: Download from python.org and check "Add to PATH" during installation
:::

You want to split a restaurant bill. Three friends, total $47.50. Simple math: $47.50 divided by 3 equals... well, let's ask the terminal.

You fire up Bash. You learned basic commands in previous chapter. Math should be straightforward.

```bash
echo $((47.50 / 3))
```

The terminal throws an error. You stare at the screen. Division is basic arithmetic. What went wrong?

## The Experiment: Watch Bash Fail

Let's recreate that moment of confusion. Open your terminal and try this exact command:

```bash
echo $((1.2 + 2.3))
```

**Expected output:**

```
bash: 1.2 + 2.3: syntax error: invalid arithmetic operator (error token is ".2 + 2.3")
```

The error message reveals the problem: Bash doesn't recognize the decimal point. It sees `1.2` and chokes on the `.2` part.

Now try this command with whole numbers:

```bash
echo $((12 + 23))
```

**Expected output:**

```
35
```

That works perfectly. The difference? No decimal points.

## Why Bash Fails: Integer-Only Arithmetic

Bash's `$((...))` syntax performs **integer-only** arithmetic. This means:

| Works in Bash                  | Fails in Bash                         |
| ------------------------------ | ------------------------------------- |
| `$((5 + 3))` = 8               | `$((5.5 + 3.5))` = Error              |
| `$((100 - 25))` = 75           | `$((100.00 - 25.00))` = Error         |
| `$((4 * 7))` = 28              | `$((4.5 * 2))` = Error                |
| `$((10 / 3))` = 3 (truncated!) | `$((10.0 / 3.0))` = Error             |

Notice that last row. Even when Bash doesn't error, it **truncates**. `10 / 3` returns `3`, not `3.333...`. For financial calculations, that silent data loss is dangerous.

Try it:

```bash
echo $((10 / 3))
```

**Output:**

```
3
```

Where did the `.333...` go? Bash threw it away. No warning. No error. Just wrong.

This is the **arithmetic gap**: the space between what you need (precise decimal math) and what Bash provides (integer-only approximations).

## Real-World Impact: Why This Matters

Consider these scenarios where the arithmetic gap bites:

**Splitting bills:**
- Dinner total: $127.89 split 4 ways
- Bash: `echo $((127 / 4))` = 31 (wrong - lost $3.89)
- Correct: $31.9725 each

**Calculating tips:**
- Bill: $85.50, tip 18%
- Bash can't even start - $85.50 causes an error
- Correct: $15.39

**Budget tracking:**
- Monthly expenses: $1,234.56 + $789.01 + $456.78
- Bash: Error on every number
- Correct: $2,480.35

Every financial calculation involves decimals. Bash simply cannot do them.

## The Head Math Trap: Why AI Gets It Wrong Too

You might think: "Okay, Bash can't do decimals. I'll just ask my AI assistant to calculate it for me."

This feels safe. After all, AI assistants are smart. They can reason. Surely they can add numbers.

Here's the trap: **LLMs don't compute, they predict**.

When you ask an AI to add `12.50 + 8.75`, it's not running arithmetic. It's predicting what text should come next based on patterns. For simple math, the prediction often matches reality. But scale changes everything.

Try this mental experiment:

**3 numbers** - AI probably gets it right:

```
Add: 45.67 + 23.99 + 150.00
```

**10 numbers** - AI might get it right:

```
Add: 45.67, 23.99, 150.00, 89.50, 32.00, 18.75, 225.00, 67.89, 12.50, 88.00
```

**100 numbers from your expense report** - AI will almost certainly get it wrong.

The problem isn't intelligence. The problem is mechanism. Asking an LLM to sum 100 numbers is like asking a poet to recite a calculation from memory. They might get lucky, but you wouldn't bet your finances on it.

This phenomenon is called **hallucination** in the context of factual claims. For math, it's the same mechanism: the model generates plausible-looking output that happens to be wrong.

## The Solution: Python

Python handles decimals natively:

```python
print(1.2 + 2.3)
```

**Output:**

```
3.5
```

No errors. No truncation. Just correct math.

```python
print(47.50 / 3)
```

**Output:**

```
15.833333333333334
```

Python computed the actual answer. It will be correct whether you're adding 2 numbers or 2,000.

## The Principle: If It's Math, It Belongs in a Script

This brings us to a foundational rule for working with AI agents:

> **If it's math, it belongs in a script. Period.**

Don't ask AI to calculate. Ask AI to **write code that calculates**.

The difference is profound:

| Approach                            | Reliability         | Why                              |
| ----------------------------------- | ------------------- | -------------------------------- |
| "What's the sum of these amounts?"  | Unreliable at scale | LLM predicts, doesn't compute    |
| "Write Python to sum these numbers" | Reliable            | Python executes, doesn't predict |

In the next lesson, you'll build your first Python utility that reads numbers and calculates sums with perfect accuracy.

## The Decision Framework

When you encounter a calculation task, use this quick test:

```
Does it involve decimals?
|-- Yes -> Use Python
|-- No -> Does it need more than 10 numbers?
    |-- Yes -> Use Python (humans can't verify large sums easily)
    |-- No -> Bash might work, but Python is still safer
```

In practice, the answer is almost always: **use a script**. The cost of writing a 3-line Python script is tiny. The cost of a wrong calculation in your budget, taxes, or business is not.

## Try With AI

### Prompt 1: Understanding the Limitation

```
I just tried running `echo $((1.2 + 2.3))` in Bash and got a syntax error.
Can you explain why Bash can't handle decimal numbers in arithmetic?
What's happening under the hood that causes this limitation?
```

**What you're learning:** You're experiencing AI as a teacher. The AI explains technical concepts you encountered through experimentation. Notice how the AI provides deeper context about integer arithmetic and shell design decisions.

### Prompt 2: Finding Alternatives

```
Bash can't do decimal math. What are my options for doing calculations
with decimal numbers from the command line?

I know Python works, but are there other tools built into Unix/Linux
that can handle decimals? What about bc or awk?
```

**What you're learning:** You're exploring the tool landscape. The AI introduces alternatives you might not know about. This builds your mental map of available solutions. (You'll learn more about some of these tools in later lessons.)

### Prompt 3: Writing a Quick Calculator

```
Write a simple Python one-liner I can use from the command line to
calculate decimal math. I want something I can type directly in my
terminal without creating a file.

For example, I want to calculate: 127.89 / 4
```

**What you're learning:** You're treating AI as a co-worker who provides ready-to-use solutions. The AI shows you `python -c "print(127.89 / 4)"` or similar patterns. This bridges from "Bash can't do it" to "but here's how to do it anyway."
