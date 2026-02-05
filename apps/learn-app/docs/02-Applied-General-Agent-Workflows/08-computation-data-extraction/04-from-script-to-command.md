---
sidebar_position: 5
title: "From Script to Command"
chapter: 8
lesson: 4
layer: L2
duration_minutes: 30
description: "Watch Claude Code build a CSV parser and make it a permanent command you can use forever"
keywords:
  [
    "CSV",
    "awk",
    "cut",
    "csv module",
    "structured data",
    "alias",
    "shebang",
    "chmod",
    "bank statement",
  ]

skills:
  - name: "Directing CSV Processing"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Data Processing"
    measurable_at_this_level: "Student can direct Claude Code to build a CSV parser that handles real-world edge cases"

  - name: "Understanding CSV Parsing Traps"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain why awk/cut fail on quoted CSV fields"

  - name: "Creating Permanent Commands"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "System Administration"
    measurable_at_this_level: "Student creates alias in shell config and verifies it persists"

learning_objectives:
  - objective: "Direct Claude Code to build a CSV parser for bank statements"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student prompts agent to create sum-expenses.py that handles quoted fields"

  - objective: "Explain why simple delimiter-based tools fail on real CSV"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student identifies that quoted fields with commas break awk/cut"

  - objective: "Create a persistent shell alias for the CSV script"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Student creates alias that persists after terminal restart"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (CSV complexity, awk limitation, csv module, making scripts permanent, aliases) within A2 limit"

differentiation:
  extension_for_advanced: "Add command-line column selection, explore csv.DictReader"
  remedial_for_struggling: "Focus on the conversation - watch how the agent recognizes and solves the CSV trap"
---

# From Script to Command

sum.py works on simple number lists. But real-world data is messier.

Download your bank statement, and you get a CSV file. Open it, and you see rows with dates, descriptions, and amounts. The data isn't one number per line - it's organized into columns separated by commas.

You might think: "Just split on commas and grab the amount column."

That intuition will fail you on real data. Watch Claude Code handle this complexity - and then turn the solution into a permanent command.

## The Problem

You have a bank statement CSV:

```csv
Date,Description,Amount
2024-01-02,Coffee Shop,-5.50
2024-01-03,Grocery Store,-127.43
2024-01-07,"AMAZON, INC.",-89.50
```

You need to sum the Amount column. The third column. Simple, right?

Look at line 4 carefully. The description is `"AMAZON, INC."` - it contains a comma INSIDE the quoted field. If you split on commas, you'll get the wrong column.

## The Conversation

Open Claude Code and describe your real-world problem:

```
You: I have a bank statement CSV. I need to sum the Amount column.
Be careful - some merchant names have commas inside them like "AMAZON, INC."
```

Watch what Claude Code does:

```
Claude Code: I'll create a script using Python's csv module to handle
that correctly.

[Creates: sum-expenses.py]

#!/usr/bin/env python3
# sum-expenses.py - Sum the Amount column from bank statement CSV
import sys
import csv

total = 0
reader = csv.reader(sys.stdin)
next(reader)  # Skip header row

for row in reader:
    amount_str = row[2]  # Amount is 3rd column (index 2)
    amount = float(amount_str.replace('$', '').replace(',', ''))
    total += abs(amount)

print(f"Total: ${total:.2f}")

[Creates: test_bank.csv]
Date,Description,Amount
2024-01-02,Coffee Shop,-5.50
2024-01-03,Grocery Store,-127.43
2024-01-07,"AMAZON, INC.",-89.50

[Runs: cat test_bank.csv | python sum-expenses.py]

Total: $222.43
```

The agent used Python's csv module without hesitation. But why? Why not just split on commas?

## What Just Happened?

The agent chose Python's csv module instead of simpler approaches. Here's why that matters.

**The CSV Parsing Trap.** You might think: "Just use awk to split on commas." Try it yourself:

```bash
echo '01/07/2025,"AMAZON, INC.",-89.50' | awk -F',' '{print $3}'
```

Output: ` INC."`

That's garbage. awk split on EVERY comma, including the one inside the quoted field. It saw:

1. `01/07/2025`
2. `"AMAZON`
3. ` INC."`
4. `-89.50`

Field 3 is ` INC."` - not the amount you wanted.

**Python's csv module understands quoting rules.** It knows that commas inside quotes don't count as separators. The module handles:

- Quoted fields with commas inside
- Escaped quotes within quoted fields
- Different line ending styles
- Edge cases you haven't thought of yet

When you mentioned "commas inside merchant names," you signaled the complexity. The agent chose the right tool for that complexity.

## The Agent's Toolkit: Why awk Fails

The agent demonstrated the failure first. Let's understand why.

### awk: The Text Processing Tool

`awk` is a classic Unix tool for columnar data:

```bash
awk -F',' '{print $3}' file.csv
```

| Part | Meaning |
|------|---------|
| `awk` | The command |
| `-F','` | Field separator is comma |
| `'{print $3}'` | Print the 3rd field |
| `file.csv` | Input file |

For simple data, awk works beautifully. But awk doesn't understand CSV quoting. It sees every comma as a separator, period.

### Python's csv Module: The Right Tool

```python
import csv
import sys

reader = csv.reader(sys.stdin)
for row in reader:
    print(row)  # row is a list of correctly-parsed fields
```

The csv module:
- Recognizes quoted fields
- Handles commas inside quotes
- Strips quotes from field values
- Returns clean, correctly-split rows

### When to Use Which

| Data Type | Use awk | Use csv module |
|-----------|---------|----------------|
| Log files with consistent delimiters | ✓ | |
| Tab-separated data | ✓ | |
| Data you control (no embedded delimiters) | ✓ | |
| Bank exports | | ✓ |
| Downloaded datasets | | ✓ |
| Any external CSV | | ✓ |

Rule of thumb: If the CSV came from outside your control, use a proper CSV parser.

## Making Your Script Permanent

The agent built sum-expenses.py. You can run it:

```bash
cat bank_statement.csv | python sum-expenses.py
```

But next month, you'll want to use it again. Let's make it a permanent command.

### The Conversation Continues

```
You: I want to use sum-expenses whenever I need it, from any folder.
Make it a permanent command I can run like: cat any_file.csv | sum-expenses
```

```
Claude Code: I'll set it up as a permanent alias. First, let me put the
script in a tools directory and make it executable.

[Runs: mkdir -p ~/tools]
[Runs: cp sum-expenses.py ~/tools/]
[Runs: chmod +x ~/tools/sum-expenses.py]

Now I'll add an alias to your shell config.

[Checks: echo $SHELL]
/bin/zsh

[Appends to ~/.zshrc:]
alias sum-expenses='python3 ~/tools/sum-expenses.py'

[Runs: source ~/.zshrc]

Done! Now you can run:
cat any_bank_file.csv | sum-expenses

This will work from any directory, and persists after you close the terminal.
```

The agent:
1. Created a `~/tools` directory for your scripts
2. Made the script executable with `chmod +x`
3. Added an alias to your shell config
4. Reloaded the config with `source`

### The Agent's Toolkit: Making Scripts Permanent

| Command | What It Does | Memory Trick |
|---------|--------------|--------------|
| `chmod +x` | Makes file executable | **ch**ange **mod**e + e**x**ecute |
| `source` | Reloads shell config | Load the **source** of settings |
| `alias` | Creates a shortcut command | Like a nickname |
| `>>` | Appends to file (doesn't overwrite) | Two arrows = add more |

**The shebang line** (`#!/usr/bin/env python3`) tells the OS which interpreter to use. Without it, `./sum-expenses.py` wouldn't know to use Python.

**chmod +x** adds executable permission. By default, text files can't be run as programs.

**Shell config files** (`~/.bashrc` for Bash, `~/.zshrc` for Zsh) run every time you open a terminal. Aliases defined there persist.

**source** reloads the config without closing the terminal.

## The Pattern

Here's the pattern for handling structured data:

```
"I have [structured data type]. Process [specific column/field].
Be careful - [edge case that could break naive parsing]."
```

Mentioning the edge case helps the agent choose robust solutions. Compare:

| Prompt | Agent's Likely Response |
|--------|------------------------|
| "Sum the third column of this CSV" | Might use awk (faster, simpler) |
| "Sum the Amount column. Some merchant names have commas" | Uses csv module (handles edge cases) |

The second prompt gives context that guides the agent to the right tool.

### Pattern for Making Tools Permanent

```
"I want to use [script] from anywhere. Make it a permanent command."
```

This signals you want:
- Script moved to a standard location
- Made executable
- Aliased in shell config
- Working across sessions

## Try It Yourself

Test that your alias works:

```bash
# Create test data
echo -e 'Date,Description,Amount\n2024-01-01,Coffee,-5.00\n2024-01-02,"SHOP, INC.",-10.00' > test.csv

# Use your new command
cat test.csv | sum-expenses
```

**Expected output:**

```
Total: $15.00
```

Now close your terminal completely. Open a new one. Run the command again:

```bash
cat test.csv | sum-expenses
```

If it still works, your alias persists. You've permanently extended your shell with a custom command.

## What You've Built

Look at the progression across these four lessons:

| Lesson | What You Built | Problem Solved |
|--------|---------------|----------------|
| 1. Arithmetic Gap | Recognized Bash limits | Decimals fail in Bash |
| 2. Python Utility | Created sum.py | Simple number summing |
| 3. Testing Loop | Verification workflow | Trust through testing |
| 4. Script to Command | Created sum-expenses as permanent command | Real CSV parsing + reusable tool |

You went from "Bash can't add decimals" to "I have a permanent command for processing bank statements."

## Connecting to the Seven Principles

**Principle 1: Bash is the Key**

The shell orchestrates everything - pipes, aliases, file manipulation. But Bash delegates complex parsing to the right tool (Python's csv module).

**Principle 2: Code as Universal Interface**

Your CSV parser is code that executes. No hallucination, no approximation. Given a bank statement, it returns exact totals.

**Principle 5: Persisting State in Files**

Your script lives in `~/tools/`. Your alias lives in `~/.zshrc`. These persist across sessions, surviving terminal closures and reboots.

---

## Try With AI

### Prompt 1: Understand the CSV Trap

```
Show me what happens when I try to parse "AMAZON, INC.",-89.50 with awk.
Why does it give the wrong result? What does Python's csv module do differently?
```

**What you're learning:** Deep understanding of the failure mode. The agent demonstrates the problem step by step, so you understand why csv modules exist - not just that you should use them.

### Prompt 2: Extend the Parser

```
My sum-expenses.py works well. Can you modify it to:
1. Accept a column number as an argument (so I can sum any column)
2. Handle empty lines gracefully
3. Show how many transactions were processed

Keep the stdin pattern so it still works with pipes.
```

**What you're learning:** Iterative improvement. You have working code and clear requirements. The agent extends functionality while preserving the composable pattern.

### Prompt 3: Fix Path Issues

```
My alias sum-expenses='python sum-expenses.py' works in the folder where
the script exists. But when I cd to another folder, it fails with
"No such file or directory."

Why? How do I make it work from any directory?
```

**What you're learning:** Path resolution. The agent explains relative vs. absolute paths - why `python sum-expenses.py` only works in one directory, but `python ~/tools/sum-expenses.py` works everywhere.
