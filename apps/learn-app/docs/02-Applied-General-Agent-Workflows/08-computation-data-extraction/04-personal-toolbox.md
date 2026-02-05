---
sidebar_position: 5
title: "From Numbers to Structured Data"
chapter: 8
lesson: 4
duration_minutes: 30
description: "Learn why simple text tools fail on real CSV data and build a robust bank statement parser with persistent aliases"
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
  - name: "Understanding CSV Parsing Challenges"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain why awk/cut fail on quoted CSV fields and recognize when Python's csv module is needed"

  - name: "Using Python's csv Module"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can write a script using csv.reader to correctly parse CSV with quoted fields"

  - name: "Creating Persistent Shell Commands"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "System Administration"
    measurable_at_this_level: "Student creates alias in shell config and verifies it persists across sessions"

learning_objectives:
  - objective: "Explain why simple delimiter-based tools fail on real-world CSV"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student identifies that quoted fields containing commas break awk/cut parsing"

  - objective: "Build CSV-reading Python script using the csv module"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student creates working sum-expenses.py that correctly handles quoted CSV fields"

  - objective: "Create persistent shell alias for the CSV script"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Student creates alias, verifies it persists after terminal restart"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (CSV format, awk/cut limitation, quoted fields, csv.reader, shebang, chmod, alias) AT A2 LIMIT - heavy but necessary scaffolding"

differentiation:
  extension_for_advanced: "Add command-line arguments to select column, explore csv.DictReader"
  remedial_for_struggling: "Focus on just using the provided script with alias - understand the WHY without modifying code"
---

# From Numbers to Structured Data

In the previous lessons, you built a script that sums simple numbers - one per line. That works for quick calculations. But real-world data is more complex.

Download your bank statement, and you get a CSV file. Open it, and you see structured rows with dates, descriptions, and amounts. The data isn't one number per line - it's organized into columns separated by commas.

This lesson takes you from simple number lists to structured data. You'll learn why "just split on commas" fails catastrophically on real CSV files, how to handle this properly with Python, and how to turn your solution into a persistent command you can use forever.

## The CSV Format: Data in Columns

CSV stands for **Comma-Separated Values**. It's the universal format for tabular data - spreadsheets, database exports, bank statements, anything with rows and columns.

A simple CSV looks like this:

```csv
Date,Description,Amount
2024-01-02,Coffee Shop,-5.50
2024-01-03,Grocery Store,-127.43
2024-01-04,Gas Station,-45.00
```

Each line is a row. Commas separate the columns. The first row is typically a header naming each column.

This seems straightforward. To extract the Amount column (column 3), you might think: "Split each line on commas and take the third piece."

That intuition will fail you spectacularly on real data.

## Meet awk: The Text Processing Tool

Before we see why simple splitting fails, let's meet a tool you'll encounter frequently: `awk`.

`awk` is a classic Unix text-processing language. It excels at extracting and manipulating columnar data. The basic syntax:

```bash
awk -F',' '{print $3}' file.csv
```

Let's decode this:

| Part | Meaning |
|------|---------|
| `awk` | The command |
| `-F','` | Field separator is comma |
| `'{print $3}'` | Print the 3rd field of each line |
| `file.csv` | Input file |

For simple data, awk works beautifully:

```bash
echo -e "a,b,c\n1,2,3\n4,5,6" | awk -F',' '{print $3}'
```

**Output:**
```
c
3
6
```

The third column, extracted perfectly. So why not use awk for bank statements?

## The CSV Parsing Trap

Real bank statements have merchant names like these:

```csv
Date,Description,Amount
01/05/2025,"CVS PHARMACY #1234",-45.67
01/05/2025,"AMAZON.COM*AB1234",-23.99
01/07/2025,"AMAZON, INC.",-89.50
```

Look at that last line carefully. The description `"AMAZON, INC."` contains a comma. The quotes tell CSV parsers "this is one field, the comma inside doesn't count as a separator."

Now try awk:

```bash
echo '01/07/2025,"AMAZON, INC.",-89.50' | awk -F',' '{print $3}'
```

**Output:**
```
 INC."
```

Wrong! awk sees three commas and splits into four fields:
1. `01/07/2025`
2. `"AMAZON`
3. ` INC."`
4. `-89.50`

Field 3 is ` INC."` - garbage. The amount we wanted is actually field 4.

**This is the CSV parsing trap**: Real-world CSV has quoted fields containing commas, and simple delimiter-based tools don't understand quoting rules.

| Tool | Handles Quoted Commas? | Result on "AMAZON, INC.",-89.50 |
|------|------------------------|----------------------------------|
| `awk -F','` | No | Breaks into wrong columns |
| `cut -d','` | No | Same problem |
| Python's `csv` module | Yes | Correctly extracts -89.50 |

## Why awk Still Matters

Don't dismiss awk entirely. It's excellent for:

- Log files with consistent delimiters
- Tab-separated data
- Quick one-liners on simple data
- Data you control (no embedded delimiters)

But for data from external sources - bank exports, downloaded datasets, API responses - assume it has edge cases. Use a proper CSV parser.

## Python's csv Module: The Right Tool

Python's built-in `csv` module understands CSV quoting rules. It correctly handles:

- Quoted fields with commas inside
- Escaped quotes within quoted fields
- Different quote characters
- Various line ending styles

Here's how to use it:

```python
import csv
import sys

reader = csv.reader(sys.stdin)
for row in reader:
    print(row)  # row is a list of fields
```

Test with the problematic data:

```bash
echo -e 'Date,Description,Amount\n01/07/2025,"AMAZON, INC.",-89.50' | python -c "
import csv, sys
for row in csv.reader(sys.stdin):
    print(row)
"
```

**Output:**
```
['Date', 'Description', 'Amount']
['01/07/2025', 'AMAZON, INC.', '-89.50']
```

The csv module correctly parsed `AMAZON, INC.` as a single field, not two.

## Building sum-expenses.py

Now let's build a proper CSV expense summer. Create `sum-expenses.py`:

```python
#!/usr/bin/env python3
# sum-expenses.py - Sum the Amount column from bank statement CSV
import sys
import csv

total = 0
reader = csv.reader(sys.stdin)
next(reader)  # Skip header row

for row in reader:
    # Amount is typically the 3rd column (index 2)
    amount_str = row[2]
    # Remove currency formatting ($, commas)
    amount = float(amount_str.replace('$', '').replace(',', ''))
    total += abs(amount)  # Use absolute value to sum all transactions

print(f"Total: ${total:.2f}")
```

Let's trace through the key parts:

**Line 7**: `csv.reader(sys.stdin)` creates a CSV reader that pulls rows from standard input.

**Line 8**: `next(reader)` skips the header row.

**Lines 11-13**: For each row:
- `row[2]` gets the Amount column (Python uses 0-based indexing)
- `.replace()` strips currency symbols
- `float()` converts to a number

**Line 14**: `abs()` takes the absolute value so both debits (-) and credits (+) are summed.

## New Commands in This Lesson

You already know `cp` from previous chapter. This lesson introduces commands for making scripts permanent:

| Command | What It Does | Memory Trick |
|---------|-------------|--------------|
| `cat > file << 'EOF'` | Creates a file with inline content (heredoc) | "Here's the document" |
| `chmod +x` | Makes a file executable | **ch**ange **mod**e + e**x**ecute |
| `source` | Reloads shell configuration | Load the **source** of settings |
| `>>` | Appends to a file (doesn't overwrite) | Two arrows = add more |

### The Heredoc: Creating Multi-line Files

The heredoc syntax (`<< 'EOF'`) lets you create files with multiple lines inline:

```bash
cat > myfile.txt << 'EOF'
Line 1
Line 2
Line 3
EOF
```

Breaking it down:
- `cat >` - output to a file
- `<< 'EOF'` - "read until you see EOF"
- Lines in between become the file contents
- `EOF` - marks the end (can be any word, EOF is convention)

The quotes around `'EOF'` prevent variable expansion - `$HOME` stays as literal text, not your home directory.

### Append vs Overwrite

```bash
echo "first" > file.txt   # Creates/overwrites file with "first"
echo "second" >> file.txt # Appends "second" to existing file
```

Result: file.txt contains both "first" and "second" on separate lines.

### The source Command

When you edit `~/.bashrc` or `~/.zshrc`, the changes don't take effect until you start a new terminal. The `source` command reloads the file immediately:

```bash
source ~/.bashrc  # Reload bash config now
```

## Testing Your CSV Parser

Create test data that exercises the tricky cases:

```bash
cat > test_bank.csv << 'EOF'
Date,Description,Amount
2024-01-02,Coffee Shop,-$5.50
2024-01-03,Grocery Store,-$127.43
2024-01-04,"AMAZON, INC.",-$89.50
2024-01-05,Gas Station,-$45.00
EOF
```

Run your script:

```bash
cat test_bank.csv | python sum-expenses.py
```

**Expected output:**
```
Total: $267.43
```

Verify by hand: 5.50 + 127.43 + 89.50 + 45.00 = 267.43. Correct!

The csv module handled `"AMAZON, INC."` correctly despite the embedded comma.

## Making Your Script Executable

Every time you run the script, you type `python sum-expenses.py`. Let's make it feel like a real command.

### Step 1: The Shebang Line

The first line of your script (`#!/usr/bin/env python3`) is called a **shebang**. It tells the operating system which interpreter to use.

When you run a file directly, the OS reads the shebang and knows to use Python. Without it, the OS wouldn't know how to execute the file.

### Step 2: Set Executable Permission

Files have permissions controlling what you can do with them. By default, scripts are readable but not executable:

```bash
ls -l sum-expenses.py
# Output: -rw-r--r-- 1 user user 342 Jan 30 10:00 sum-expenses.py
```

The `chmod` command changes permissions. `+x` adds executable permission:

```bash
chmod +x sum-expenses.py
```

Now check again:

```bash
ls -l sum-expenses.py
# Output: -rwxr-xr-x 1 user user 342 Jan 30 10:00 sum-expenses.py
```

See the `x` in `-rwxr-xr-x`? That means executable.

### Step 3: Run Directly

Now you can run without the `python` prefix:

```bash
cat test_bank.csv | ./sum-expenses.py
```

The `./` means "run the file in the current directory."

## Creating a Shell Alias

You still need `./` and the full path. Let's create an alias - a shortcut name that expands to the full command.

```bash
alias sum-expenses='python3 ~/tools/sum-expenses.py'
```

Test it:

```bash
cat test_bank.csv | sum-expenses
# Output: Total: $267.43
```

But close and reopen your terminal - the alias is gone. It only existed in that session.

## Making Aliases Persistent

Your shell reads a configuration file at startup. For Bash, it's `~/.bashrc`. For Zsh (macOS default), it's `~/.zshrc`.

### Step 1: Set Up Your Tools Directory

```bash
mkdir -p ~/tools
cp sum-expenses.py ~/tools/
chmod +x ~/tools/sum-expenses.py
```

### Step 2: Identify Your Shell

```bash
echo $SHELL
# Output: /bin/bash (or /bin/zsh on macOS)
```

### Step 3: Add the Alias

For Bash:
```bash
echo "alias sum-expenses='python3 ~/tools/sum-expenses.py'" >> ~/.bashrc
source ~/.bashrc
```

For Zsh:
```bash
echo "alias sum-expenses='python3 ~/tools/sum-expenses.py'" >> ~/.zshrc
source ~/.zshrc
```

### Step 4: Verify Persistence

```bash
cat test_bank.csv | sum-expenses
# Output: Total: $267.43
```

Now close your terminal completely. Open a new one. Run the alias:

```bash
cat test_bank.csv | sum-expenses
# Output: Total: $267.43
```

The alias persists. You've permanently extended your shell with a custom command.

## What You've Built

Look at the progression across these four lessons:

| Lesson | What You Built | Problem Solved |
|--------|---------------|----------------|
| 1. Arithmetic Gap | Recognized Bash limits | Decimals fail in Bash |
| 2. Python Utility | Created sum.py | Simple number summing |
| 3. Testing Loop | Verification workflow | Trust through testing |
| 4. Structured Data | Created sum-expenses.py | Real CSV parsing |

You went from "Bash can't add decimals" to "I have a permanent command for processing bank statements." This is the agent-building pattern: identify a need, build a solution, verify it works, make it accessible.

## Connecting to the Seven Principles

This lesson demonstrates several principles:

**Principle 1: Bash is the Key**
The shell orchestrates everything - pipes, aliases, file manipulation. But Bash delegates complex parsing to the right tool (Python).

**Principle 2: Code as Universal Interface**
Your CSV parser is code that executes. No hallucination, no approximation. Given a bank statement, it returns exact totals.

**Principle 5: Persisting State in Files**
Your script lives in `~/tools/`. Your alias lives in `~/.bashrc` or `~/.zshrc`. These persist across sessions, surviving terminal closures and reboots.

## Try With AI

### Prompt 1: Understanding the CSV Problem

```
I tried to extract the third column from a CSV using awk:
awk -F',' '{print $3}' bank_statement.csv

But some rows have merchant names like "AMAZON, INC." with commas inside quotes.
awk gives wrong results for those rows.

Why does awk fail here? What's the difference between "split on commas"
and proper CSV parsing?
```

**What you're learning:** AI explains the fundamental difference between delimiter-based splitting and proper CSV parsing. This conceptual understanding helps you choose the right tool for the job.

### Prompt 2: Extending the Parser

```
I have a CSV parser that sums the Amount column:

import sys, csv
total = 0
reader = csv.reader(sys.stdin)
next(reader)
for row in reader:
    amount = float(row[2].replace('$', '').replace(',', ''))
    total += abs(amount)
print(f"Total: ${total:.2f}")

Can you modify it to:
1. Accept a column number as a command-line argument
2. Handle empty lines gracefully
3. Show how many transactions were processed
```

**What you're learning:** Iterative improvement with AI. You have working code and clear requirements. AI helps extend functionality while preserving the core pattern.

### Prompt 3: Making Aliases Work Everywhere

```
I created an alias: alias sum-expenses='python sum-expenses.py'

It works in the directory where sum-expenses.py exists.
But when I cd to another directory, it fails with "No such file or directory."

How do I make this alias work from any directory?
What's the difference between relative and absolute paths?
```

**What you're learning:** AI teaches the concept of path resolution. Understanding why `python sum-expenses.py` fails from other directories (and why `python ~/tools/sum-expenses.py` succeeds) is fundamental to Unix tooling.
