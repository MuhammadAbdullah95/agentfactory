---
sidebar_position: 6
title: "Data Wrangling"
chapter: 7
lesson: 5
duration_minutes: 35
description: "Extract dollar amounts from messy text using regex and process multiple files with find/xargs"
keywords:
  [
    "regex",
    "regular expressions",
    "re module",
    "find",
    "xargs",
    "data extraction",
    "pattern matching",
  ]

skills:
  - name: "Designing Regex Patterns"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Data Processing"
    measurable_at_this_level: "Student writes regex pattern to extract dollar amounts like $14.50 from text"

  - name: "Batch File Processing"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Automation"
    measurable_at_this_level: "Student uses find and xargs to process multiple files through their script"

learning_objectives:
  - objective: "Design regex pattern to extract dollar amounts from text"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Student's pattern correctly extracts $14.50, $3.00 from sentences like 'Lunch cost: $14.50'"

  - objective: "Use find and xargs to batch process files"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student executes: find . -name '*.txt' | xargs cat | python calc.py"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (regex, patterns, re.findall, find command, xargs, batch processing, extraction) AT A2 LIMIT - heavy scaffolding needed"

differentiation:
  extension_for_advanced: "Handle edge cases: $10 (no cents), 10.00 (no dollar sign), 1,234.56 (commas)"
  remedial_for_struggling: "Use pre-built regex pattern, focus only on using it not understanding it"
---

# Data Wrangling

Your `calc.py` script works beautifully when data arrives as clean numbers, one per line. But real-world data rarely cooperates. You open a receipt and see "Lunch at Maria's Cafe: $14.50" or "Office supplies from Staples - $47.23 (tax included)". The numbers you need are buried in text, surrounded by words, punctuation, and context that your current script cannot handle.

This lesson teaches you to extract structured data from unstructured text. You will learn regular expressions (regex)—a pattern-matching language that finds specific text shapes within larger documents. By the end, you will process entire folders of messy receipt files and sum all dollar amounts with a single command.

This is where your toolbox becomes genuinely powerful. The pattern you learn here—extract, transform, calculate—applies to invoices, logs, reports, and any text where numbers hide among words.

## The Problem: Numbers Buried in Text

Consider these realistic receipt snippets:

```
Coffee: $4.50
Lunch with team - $47.23 (split)
Uber ride to airport $32.00
Parking fee: $15 (no receipt available)
Office supplies from Amazon, total was $127.34 including shipping
```

If you pipe this directly to your `calc.py` script, what happens?

```bash
cat messy_receipts.txt | python calc.py
# Error or Total: 0.00 (no valid numbers found)
```

The script fails because "Coffee: $4.50" is not a valid number. The text "Coffee: " and the dollar sign prevent `float()` from parsing it. You need a preprocessing step: extract dollar amounts first, then sum them.

This is the data wrangling pattern: **Extract → Transform → Calculate**.

## Regular Expressions: Pattern Matching

A regular expression (regex) is a mini-language for describing text patterns. Instead of searching for exact text like "$14.50", you describe the shape of what you want: "a dollar sign, followed by digits, followed by a decimal point, followed by two digits."

Think of regex as a template with wildcards. Just as `*.txt` matches any filename ending in `.txt`, a regex pattern matches any text fitting its description.

Here is the pattern for dollar amounts:

```
\$?\d+\.\d{2}
```

This looks cryptic at first. Let's decode it piece by piece.

## Regex Pattern Breakdown

| Pattern Part | Meaning                                            | Example Match    |
| ------------ | -------------------------------------------------- | ---------------- |
| `\$?`        | Optional dollar sign (the `?` means "zero or one") | `$` or nothing   |
| `\d+`        | One or more digits (`\d` = any digit 0-9)          | `14`, `127`, `3` |
| `\.`         | Literal decimal point (backslash escapes the dot)  | `.`              |
| `\d{2}`      | Exactly two digits (`{2}` means "exactly 2")       | `50`, `00`, `23` |

The backslashes matter. In regex:

- `$` normally means "end of line"—so `\$` means a literal dollar sign
- `.` normally means "any character"—so `\.` means a literal period
- `\d` is a shortcut for "any digit"

When you put it together, `\$?\d+\.\d{2}` matches:

- `$14.50` (with dollar sign)
- `47.23` (without dollar sign)
- `127.34` (three-digit dollars)
- `4.50` (single-digit dollars)

But it will not match:

- `$14` (no decimal portion)
- `14.5` (only one digit after decimal)
- `Year 2024` (this is why we include the decimal—otherwise `2024` would match)

## Python's re Module

Python's `re` module provides regex functionality. The function you need most is `re.findall()`—it returns all matches of a pattern in a string.

```python
import re

text = "Lunch: $14.50, Tip: $3.00"
pattern = r'\$?\d+\.\d{2}'

matches = re.findall(pattern, text)
print(matches)
# Output: ['$14.50', '$3.00']
```

The `r` before the string (`r'\$?\d+\.\d{2}'`) creates a "raw string" where backslashes are treated literally. Without the `r`, you would need to double every backslash (`'\\$?\\d+\\.\\d{2}'`).

The result is a list of strings matching your pattern. Each match is extracted from the original text, ready for processing.

## Enhanced calc.py with Regex Extraction

Now let's upgrade your `calc.py` to extract dollar amounts from messy text:

```python
#!/usr/bin/env python3
# calc.py - Enhanced with regex extraction
import sys
import re

total = 0
pattern = r'\$?\d+\.\d{2}'  # Matches: $14.50, 14.50

for line in sys.stdin:
    matches = re.findall(pattern, line)
    for amount in matches:
        # Remove $ if present and convert to float
        total += float(amount.replace('$', ''))

print(f"Total: ${total:.2f}")
```

Let's trace through what happens with input "Lunch: $14.50, Tip: $3.00":

1. `re.findall(pattern, line)` returns `['$14.50', '$3.00']`
2. First iteration: `amount = '$14.50'`
   - `amount.replace('$', '')` → `'14.50'`
   - `float('14.50')` → `14.5`
   - `total` becomes `14.5`
3. Second iteration: `amount = '$3.00'`
   - `amount.replace('$', '')` → `'3.00'`
   - `float('3.00')` → `3.0`
   - `total` becomes `17.5`
4. Output: `Total: $17.50`

Test it:

```bash
echo "Lunch: $14.50, Tip: $3.00" | python calc.py
# Output: Total: $17.50
```

The script now handles messy text. It extracts dollar amounts, strips the dollar signs, sums the values, and reports the total.

## Processing Multiple Files with find and xargs

Your script handles one file. But what about a folder full of receipts? You could list them manually:

```bash
cat receipt1.txt receipt2.txt receipt3.txt | python calc.py
```

This works but does not scale. What if you have 50 files? 500? You need automation.

The `find` command locates files matching criteria. The `xargs` command takes a list of items and runs a command on each.

Together, they process entire directories:

```bash
# Find all .txt files in the receipts folder
find receipts/ -name "*.txt"
# Output:
# receipts/january.txt
# receipts/february.txt
# receipts/march.txt

# Pipe file list to xargs, which runs cat on each file
find receipts/ -name "*.txt" | xargs cat
# Output: contents of all files concatenated

# Pipe the combined contents to calc.py
find receipts/ -name "*.txt" | xargs cat | python calc.py
# Output: Total: $847.50 (sum of all amounts in all files)
```

This is the complete data wrangling pipeline:

```
find receipts/ -name "*.txt"  →  list of file paths
        |
        v
      xargs cat               →  combined file contents
        |
        v
    python calc.py            →  extracted and summed amounts
```

One command processes an entire folder of receipts.

## Building Your Regex Skills

Regex is a skill that compounds over time. The more patterns you learn, the more data problems you can solve. Here are variations on the dollar amount pattern:

**Match with or without cents:**

```python
pattern = r'\$?\d+(?:\.\d{2})?'
# Matches: $14.50, $14, 14.50, 14
```

**Match with commas in large numbers:**

```python
pattern = r'\$?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
# Matches: $1,234.56, $12,345.00, 1,234,567.89
```

**Match currency with various symbols:**

```python
pattern = r'[$€£]\d+(?:\.\d{2})?'
# Matches: $14.50, €25.00, £100.00
```

Each pattern builds on the basics you learned. Start simple, add complexity as needed.

## The Verification Step

Remember **Principle 3: Verification as Core Step**. After building your regex-enhanced script, test it with known data:

```bash
# Create test file with known amounts
echo "Coffee: $4.50
Lunch: $12.00
Tip: $3.50" > test_messy.txt

# Expected total: $4.50 + $12.00 + $3.50 = $20.00

# Run and verify
cat test_messy.txt | python calc.py
# Output: Total: $20.00

# Check exit code
echo $?
# Output: 0
```

Only after verification should you run the script on real data.

## Practice: Build Your Data Wrangling Pipeline

Follow these steps to solidify your skills:

**Step 1**: Create the enhanced `calc.py` with regex.

```python
#!/usr/bin/env python3
# calc.py - Enhanced with regex extraction
import sys
import re

total = 0
pattern = r'\$?\d+\.\d{2}'

for line in sys.stdin:
    matches = re.findall(pattern, line)
    for amount in matches:
        total += float(amount.replace('$', ''))

print(f"Total: ${total:.2f}")
```

**Step 2**: Create a test folder with multiple receipt files.

```bash
mkdir -p receipts
echo "Coffee: $4.50" > receipts/monday.txt
echo "Lunch: $12.75, Coffee: $4.50" > receipts/tuesday.txt
echo "Team dinner: $87.00, Tip: $17.40" > receipts/wednesday.txt
```

**Step 3**: Process all files with one command.

```bash
find receipts/ -name "*.txt" | xargs cat | python calc.py
# Expected: Total: $126.15 (4.50 + 12.75 + 4.50 + 87.00 + 17.40)
```

**Step 4**: Verify your expected total matches the script output.

## Connecting to the Seven Principles

This lesson demonstrates two principles in action:

**Principle 2: Code as Universal Interface**

Your regex pattern is a precise specification of what you want to extract. It removes ambiguity—"$14.50" matches, "Year 2024" does not. The pattern is code, executable and verifiable.

**Principle 4: Small, Reversible Decomposition**

The pipeline decomposes into three steps:

1. `find` locates files
2. `xargs cat` reads them
3. `calc.py` extracts and sums

Each step is simple and testable. If something breaks, you know exactly where to look.

This decomposition also makes the workflow reversible. Change the pattern? Modify one line. Change the file filter? Adjust the `find` command. Each piece is independent.

## Try With AI

### Prompt 1: Generate a Regex Pattern

```
Write a regex pattern that extracts dollar amounts like $14.50 from text.
The pattern should match amounts with a dollar sign and exactly two decimal places.

Then show me how to use it with Python's re.findall() to extract all
amounts from this string: "Lunch: $14.50, Tip: $3.00, Tax: $1.25"
```

**What you are learning:** AI suggests regex syntax you might not know. Notice how it explains each part of the pattern. Compare its solution to the pattern you built in this lesson.

### Prompt 2: Refine the Pattern

```
My regex pattern '\$?\d+\.\d{2}' has a problem.

It matches "Year 2024" because 2024 looks like a number with decimals
to the pattern (it sees "20.24" inside "2024").

How can I modify the pattern to REQUIRE a dollar sign, so it only
matches actual currency amounts like $14.50?
```

**What you are learning:** You teach AI about a limitation you discovered. Together you iterate toward a more robust pattern. This is the collaborative refinement loop—you provide the problem context, AI suggests solutions.

### Prompt 3: Handle Edge Cases

```
I need to extract dollar amounts from real-world receipts.
My current pattern '\$?\d+\.\d{2}' works for $14.50 but fails on:
- $10 (no cents)
- 10.00 (no dollar sign)
- $1,234.56 (commas in large numbers)

Help me build a more robust pattern that handles all these cases.
Explain each modification you make.
```

**What you are learning:** Iterate toward a production-ready pattern. Real data is messy—whole dollar amounts, missing symbols, thousand separators. Working through edge cases together builds both your regex skills and your pattern for AI collaboration.
