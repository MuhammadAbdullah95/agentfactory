---
sidebar_position: 2
title: "The Accuracy Gap"
chapter: 7
lesson: 1
duration_minutes: 20
description: "Discover why Bash arithmetic fails with decimals and when to use Python instead"
keywords:
  [
    "bash arithmetic",
    "decimal math",
    "python calculation",
    "LLM hallucination",
    "calculation accuracy",
  ]

skills:
  - name: "Recognizing Bash Arithmetic Limitations"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain why echo $((1.2 + 2.3)) fails and identify scenarios requiring Python"

  - name: "Identifying LLM Hallucination Risks"
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

  - objective: "Identify when to use Python instead of Bash for calculations"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student correctly chooses appropriate tool for given calculation scenarios"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (Bash arithmetic, integer-only math, decimal failure, LLM hallucination, script requirement) within A2 limit"

differentiation:
  extension_for_advanced: "Research how bc and awk handle decimals in Bash, compare with Python approach"
  remedial_for_struggling: "Focus on one example: Bash fails with 1.5+2.5, Python succeeds - understand just this before moving on"
---

# The Accuracy Gap: Bash vs. Python

Picture this: You spent the morning collecting expenses for a project budget. Coffee meeting receipts, software subscriptions, office supplies. Now you need to add them up. Simple enough, right?

You fire up your terminal. Bash can do math. You learned that in Chapter 6. So you type the first calculation: lunch was $12.50, parking was $8.75. You write `echo $((12.50 + 8.75))` and hit Enter.

The terminal throws an error. Something about "invalid arithmetic operator." You stare at the screen. This should be basic addition. What went wrong?

## The Experiment: Watch Bash Fail

Let's recreate that moment of confusion. Open your terminal and try this exact command:

```bash
echo $((1.2 + 2.3))
```

**Expected output:**

```
bash: 1.2: syntax error: invalid arithmetic operator (error token is ".2")
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

| Works in Bash                  | Fails in Bash                 |
| ------------------------------ | ----------------------------- |
| `$((5 + 3))` = 8               | `$((5.5 + 3.5))` = Error      |
| `$((100 - 25))` = 75           | `$((100.00 - 25.00))` = Error |
| `$((4 * 7))` = 28              | `$((4.5 * 2))` = Error        |
| `$((10 / 3))` = 3 (truncated!) | `$((10.0 / 3.0))` = Error     |

Notice that last row. Even when Bash doesn't error, it **truncates**. `10 / 3` returns `3`, not `3.333...`. For financial calculations, that silent data loss is dangerous.

This is the **accuracy gap**: the space between what you need (precise decimal math) and what Bash provides (integer-only approximations).

## The Head Math Trap: Why AI Gets It Wrong Too

You might think: "Okay, Bash can't do decimals. I'll just ask my AI assistant to calculate it for me."

This feels safe. After all, AI assistants are smart. They can reason. Surely they can add numbers.

Here's the trap: **LLMs don't compute, they predict**.

When you ask an AI to add `12.50 + 8.75`, it's not running arithmetic. It's predicting what text should come next based on patterns. For simple math, the prediction often matches reality. But scale changes everything.

Try this mental experiment:

**3 numbers** - AI probably gets it right:

```
Add: 12.50, 8.75, 15.25
```

**10 numbers** - AI might get it right:

```
Add: 12.50, 8.75, 15.25, 9.99, 22.00, 7.50, 18.75, 4.25, 31.00, 6.80
```

**100 numbers from a spreadsheet** - AI will almost certainly get it wrong.

The problem isn't intelligence. The problem is mechanism. Asking an LLM to sum 100 numbers is like asking a poet to recite a calculation from memory. They might get lucky, but you wouldn't bet your budget on it.

This phenomenon is called **hallucination** in the context of factual claims. For math, it's the same mechanism: the model generates plausible-looking output that happens to be wrong.

## The Principle: If It's Math, It Belongs in a Script

This brings us to a foundational rule for working with AI agents:

> **If it's math, it belongs in a script. Period.**

Don't ask AI to calculate. Ask AI to **write code that calculates**.

The difference is profound:

| Approach                            | Reliability         | Why                              |
| ----------------------------------- | ------------------- | -------------------------------- |
| "What's 12.50 + 8.75?"              | Unreliable at scale | LLM predicts, doesn't compute    |
| "Write Python to add these numbers" | Reliable            | Python executes, doesn't predict |

Here's what reliable calculation looks like:

```python
# Python - WORKS
print(1.2 + 2.3)
```

**Expected output:**

```
3.5
```

Python handles decimals natively. The result is computed, not predicted. It will be correct whether you're adding 2 numbers or 2,000.

## Connecting to the Seven Principles

This lesson demonstrates two principles from Chapter 4:

**Principle 1: Bash is the Key** - But knowing Bash's limitations is equally important. Bash is the key to _orchestration_. For computation, you route through the right tool.

**Principle 3: Verification as Core Step** - The Bash error message was verification in action. The system told us something failed. In the next lesson, you'll learn to build verification into your own scripts so failures become visible signals, not silent corruption.

## The Decision Framework

When you encounter a calculation task, use this simple test:

```
Does it involve decimals?
├── Yes → Use Python (or any language that handles floats)
└── No → Does it need more than 10 numbers?
    ├── Yes → Use Python (humans can't verify large sums easily)
    └── No → Bash might work, but Python is still safer
```

In practice, the answer is almost always: **use a script**. The cost of writing a 3-line Python script is tiny. The cost of a wrong total in your budget is not.

## Try With AI

### Prompt 1: Understanding the Limitation

```
I just tried running `echo $((1.2 + 2.3))` in Bash and got a syntax error.
Can you explain why Bash can't handle decimal numbers in arithmetic?
What's happening under the hood that causes this limitation?
```

**What you're learning:** You're experiencing AI as a teacher. The AI explains technical concepts you encountered through experimentation. Notice how the AI provides deeper context about integer arithmetic and shell design decisions. This deepens your understanding beyond "it doesn't work" to "here's why it doesn't work."

### Prompt 2: Choosing the Right Tool

```
I need to sum a list of prices from a restaurant menu:
- Appetizer: $8.95
- Entree: $24.50
- Dessert: $7.25
- Coffee: $3.50

Should I use Bash or Python for this? Why?
```

**What you're learning:** You're giving the AI a real scenario and asking it to make a tool recommendation. The AI should recognize the decimal values and recommend Python. Notice if the AI explains its reasoning or just gives an answer. A good response will connect the decimal issue to the tool choice.

### Prompt 3: Getting Reliable Output

```
Write a Python one-liner that calculates 12.50 + 8.75 + 15.25 and prints the result.
I want to paste this directly into my terminal.
```

**What you're learning:** You're treating AI as a co-worker who writes code for you. The AI produces executable code; you execute it and verify the result. This is the pattern for all calculation work going forward: AI writes the code, the computer computes the answer, you verify.
