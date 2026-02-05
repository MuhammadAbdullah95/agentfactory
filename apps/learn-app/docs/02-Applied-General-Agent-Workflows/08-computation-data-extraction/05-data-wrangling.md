---
sidebar_position: 6
title: "Data Wrangling"
chapter: 8
lesson: 5
duration_minutes: 35
description: "Normalize merchant names and categorize transactions using regex pattern matching"
keywords:
  [
    "regex",
    "regular expressions",
    "re module",
    "find",
    "xargs",
    "data extraction",
    "pattern matching",
    "tax categorization",
  ]

skills:
  - name: "Designing Regex Patterns"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Data Processing"
    measurable_at_this_level: "Student writes regex pattern to match merchant name variations like AMZN, AMAZON.COM, AMZN MKTP"

  - name: "Batch File Processing"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Automation"
    measurable_at_this_level: "Student uses find and xargs to process multiple files through their script"

learning_objectives:
  - objective: "Design regex pattern to match merchant name variations"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Student's pattern correctly matches AMZN, AMAZON.COM, AMZN MKTP as 'Amazon'"

  - objective: "Use find and xargs to batch process files"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student executes: find . -name '*.csv' | xargs cat | python tax-categorize.py"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (regex, patterns, re module, find command, xargs, batch processing, false positive handling) AT A2 LIMIT - heavy scaffolding needed"

differentiation:
  extension_for_advanced: "Handle edge cases: partial matches, case sensitivity, regex anchors for precision"
  remedial_for_struggling: "Use pre-built keyword lists, focus only on using the script not modifying patterns"
---

# Data Wrangling

In Lesson 4, you built `sum-expenses` - a CSV parser that correctly handles quoted fields and persists as a permanent command. You can now sum any bank statement with a single command. But summing is just the beginning. Tax season arrives, and your accountant asks: "How much did you spend on medical expenses? How much on charitable donations? How much on business supplies?"

You open your bank statement. The transactions look like this:

```
CVS/PHARMACY #1234      -$45.67
WALGREENS #5678         -$23.45
AMZN MKTP US*ABC123     -$127.89
AMAZON.COM*XYZ          -$34.56
DR PEPPER SNAPPLE       -$4.99
UNITED WAY              -$100.00
```

Finding all medical expenses means recognizing that CVS, Walgreens, and pharmacy purchases all belong to the same category. Finding all Amazon purchases means recognizing that "AMZN," "AMAZON.COM," and "AMZN MKTP" are all the same merchant. And you need to avoid false positives - "Dr. Pepper" is a soda, not a medical expense.

This lesson teaches you to match patterns and categorize data using regular expressions. By the end, you will have a `tax-categorize.py` script that processes your bank statements and outputs totals by category.

## The Problem: Merchant Name Chaos

Bank statements never use clean, consistent names. Amazon alone might appear as:

| Statement Entry          | What It Is                    |
| ------------------------ | ----------------------------- |
| AMZN                     | Amazon shortened              |
| AMAZON.COM               | Amazon website                |
| AMZN MKTP US             | Amazon Marketplace            |
| AMZN DIGITAL             | Amazon digital purchases      |
| AMAZON PRIME             | Amazon subscription           |

If you search for "Amazon" exactly, you miss most of these. If you search for "AMZ" carelessly, you might match "CVSMITH" (an actual last name that contains no relation to Amazon). You need pattern matching that is both flexible enough to catch variations and precise enough to avoid false matches.

This is where regular expressions shine.

## Regular Expressions: Pattern Matching

A regular expression (regex) is a mini-language for describing text patterns. Instead of searching for exact text like "CVS," you describe the shape of what you want: "the letters CVS at the start of a word, optionally followed by other characters."

Think of regex as a template with wildcards. Just as `*.txt` matches any filename ending in `.txt`, a regex pattern matches any text fitting its description.

Here is a pattern for matching CVS pharmacy entries:

```
\bcvs\b
```

Let us decode it:

| Pattern Part | Meaning                                    | Example Match      |
| ------------ | ------------------------------------------ | ------------------ |
| `\b`         | Word boundary (start or end of word)       | Prevents partial matches |
| `cvs`        | Literal letters "cvs"                      | `cvs`, `CVS`, `Cvs`    |
| `\b`         | Word boundary again                        | Ensures complete word   |

The word boundaries matter. Without them:

- `cvs` would match "CVSMITH" (a name)
- `dr` would match "ANDRE" or "DRAMATIC"

With `\b`:

- `\bcvs\b` matches "CVS" but not "CVSMITH"
- `\bdr\b` matches "DR" but not "ANDRE"

## Python's re Module

Python's `re` module provides regex functionality. The function you need most is `re.search()` - it checks if a pattern exists anywhere in a string.

```python
import re

description = "CVS/PHARMACY #1234"
pattern = r'\bcvs\b'

if re.search(pattern, description, re.IGNORECASE):
    print("Matched!")
# Output: Matched!
```

The `r` before the string (`r'\bcvs\b'`) creates a "raw string" where backslashes are treated literally. The `re.IGNORECASE` flag makes matching case-insensitive, so `cvs` matches `CVS`, `Cvs`, and `cvs`.

## Building the Tax Categorization Script

Now let us build `tax-categorize.py` that categorizes transactions by type:

```python
#!/usr/bin/env python3
import sys
import csv
import re

CATEGORIES = {
    'medical': ['cvs', 'walgreens', 'pharmacy', 'dr.', 'medical', 'health', 'dental'],
    'charitable': ['donation', 'charity', 'united way', 'red cross', 'church'],
    'business': ['office depot', 'staples', 'zoom', 'linkedin', 'adobe'],
}

# False positive guards
FALSE_POSITIVES = ['dr. pepper', 'dr pepper', 'cvsmith']

def categorize(description):
    desc_lower = description.lower()

    # Check false positives first
    if any(fp in desc_lower for fp in FALSE_POSITIVES):
        return None

    for category, keywords in CATEGORIES.items():
        if any(keyword in desc_lower for keyword in keywords):
            return category
    return None

# Process CSV from stdin
totals = {cat: 0 for cat in CATEGORIES}
reader = csv.reader(sys.stdin)
next(reader)  # Skip header

for row in reader:
    description, amount = row[1], row[2]
    amount = abs(float(amount.replace('$', '').replace(',', '')))

    category = categorize(description)
    if category:
        totals[category] += amount
        print(f"{category.upper()}: {description}: ${amount:.2f}")

print("\n--- TOTALS ---")
for cat, total in totals.items():
    if total > 0:
        print(f"{cat.title()}: ${total:.2f}")
```

Let us trace through what happens with input "CVS/PHARMACY #1234, -$45.67":

1. `description = "CVS/PHARMACY #1234"`, `amount = "$45.67"`
2. `desc_lower = "cvs/pharmacy #1234"`
3. Check false positives: "dr. pepper" not in description - continue
4. Check categories: "cvs" is in description - return "medical"
5. `totals['medical'] += 45.67`
6. Print: `MEDICAL: CVS/PHARMACY #1234: $45.67`

Test it:

```bash
cat > test_bank.csv << 'EOF'
Date,Description,Amount
2024-01-15,CVS/PHARMACY #1234,-$45.67
2024-01-16,WALGREENS #5678,-$23.45
2024-01-17,DR PEPPER SNAPPLE,-$4.99
2024-01-18,UNITED WAY,-$100.00
2024-01-19,OFFICE DEPOT,-$89.50
EOF

cat test_bank.csv | python tax-categorize.py
```

**Output:**
```
MEDICAL: CVS/PHARMACY #1234: $45.67
MEDICAL: WALGREENS #5678: $23.45
CHARITABLE: UNITED WAY: $100.00
BUSINESS: OFFICE DEPOT: $89.50

--- TOTALS ---
Medical: $69.12
Charitable: $100.00
Business: $89.50
```

Notice that "DR PEPPER SNAPPLE" was correctly skipped - the false positive guard prevented it from being categorized as medical even though it contains "DR".

## Merchant Name Normalization

The categorization script uses simple keyword matching. For merchant consolidation - grouping all Amazon transactions together - you need more flexible patterns.

Here is a function that normalizes merchant names:

```python
import re

MERCHANT_PATTERNS = {
    'Amazon': r'\b(amzn|amazon)\b',
    'Walmart': r'\b(walmart|wal-mart|wm supercenter)\b',
    'Target': r'\btarget\b',
    'Starbucks': r'\b(starbucks|sbux)\b',
}

def normalize_merchant(description):
    desc_lower = description.lower()

    for merchant, pattern in MERCHANT_PATTERNS.items():
        if re.search(pattern, desc_lower):
            return merchant
    return description  # Return original if no match
```

Testing the patterns:

```python
test_descriptions = [
    "AMZN MKTP US*ABC123",
    "AMAZON.COM*XYZ",
    "AMAZON PRIME",
    "CVSMITH SERVICES",  # Should NOT match Amazon
]

for desc in test_descriptions:
    normalized = normalize_merchant(desc)
    print(f"{desc:30} -> {normalized}")
```

**Output:**
```
AMZN MKTP US*ABC123            -> Amazon
AMAZON.COM*XYZ                 -> Amazon
AMAZON PRIME                   -> Amazon
CVSMITH SERVICES               -> CVSMITH SERVICES
```

The word boundary `\b` in the pattern `\b(amzn|amazon)\b` ensures:
- "AMZN MKTP" matches (amzn is a complete word)
- "AMAZON.COM" matches (amazon is followed by punctuation)
- "CVSMITH" does NOT match (contains "v" and "smith", but no "amzn" or "amazon")

## Avoiding False Positives: The Guard Pattern

False positives are matches that look right but are wrong. The classic example: "Dr. Pepper" is not a medical expense.

The guard pattern is simple: check for false positives BEFORE checking for categories.

```python
FALSE_POSITIVES = ['dr. pepper', 'dr pepper']

def categorize(description):
    desc_lower = description.lower()

    # Guard: Check false positives first
    if any(fp in desc_lower for fp in FALSE_POSITIVES):
        return None  # Not a category match

    # Now safe to check categories
    if 'dr.' in desc_lower or 'medical' in desc_lower:
        return 'medical'

    return None
```

This pattern scales. As you discover new false positives, add them to the list:

```python
FALSE_POSITIVES = [
    'dr. pepper', 'dr pepper',      # Soda, not doctor
    'cvsmith',                       # Name, not CVS pharmacy
    'church key',                    # Tool, not religious donation
    'amazon river cruise',           # Travel, not Amazon.com
]
```

## Processing Multiple Files

Your script handles one file. But what about a folder full of bank statements? You could list them manually:

```bash
cat january.csv february.csv march.csv | python tax-categorize.py
```

This works but does not scale. What if you have 12 months of statements? 3 years?

You learned `find` and `xargs` in previous chapter. Now apply them to CSV processing:

```bash
# Find all .csv files and process them through your script
find statements/ -name "*.csv" | xargs cat | python tax-categorize.py
```

The pipeline:
1. `find` locates all CSV files
2. `xargs cat` reads them all
3. `tax-categorize.py` categorizes and sums

One command processes an entire folder of bank statements.

## Building Your Pattern Library

Regex is a skill that compounds over time. The more patterns you learn, the more data problems you can solve. Here are common patterns for financial data:

**Match word at start or end:**

```python
pattern = r'\bcvs\b'  # CVS as complete word
# Matches: "CVS PHARMACY", "CVS/STORE"
# Does NOT match: "CVSMITH", "INCVS"
```

**Match alternatives:**

```python
pattern = r'\b(amzn|amazon)\b'  # Either amzn or amazon
# Matches: "AMZN", "AMAZON", "Amazon.com"
```

**Match optional parts:**

```python
pattern = r'\bwal-?mart\b'  # Hyphen optional
# Matches: "WALMART", "WAL-MART"
```

Each pattern builds on the basics you learned. Start simple, add complexity as needed.

## The Verification Step

Remember **Principle 3: Verification as Core Step**. After building your categorization script, test it with known data:

```bash
# Create test file with known categories
cat > test_categories.csv << 'EOF'
Date,Description,Amount
2024-01-15,CVS PHARMACY,-$45.00
2024-01-16,DR PEPPER,-$3.00
2024-01-17,UNITED WAY,-$50.00
2024-01-18,OFFICE DEPOT,-$25.00
EOF

# Expected: CVS = medical, DR PEPPER = nothing, UNITED WAY = charitable, OFFICE DEPOT = business

cat test_categories.csv | python tax-categorize.py
```

**Output:**
```
MEDICAL: CVS PHARMACY: $45.00
CHARITABLE: UNITED WAY: $50.00
BUSINESS: OFFICE DEPOT: $25.00

--- TOTALS ---
Medical: $45.00
Charitable: $50.00
Business: $25.00
```

DR PEPPER correctly skipped. Only after verification should you run the script on real data.

## Connecting to the Seven Principles

This lesson demonstrates two principles in action:

**Principle 2: Code as Universal Interface**

Your category keywords and regex patterns are precise specifications of what you want to match. They remove ambiguity - "cvs" matches CVS pharmacy, not CVSMITH. The patterns are code, executable and verifiable.

**Principle 4: Small, Reversible Decomposition**

The pipeline decomposes into three steps:

1. `find` locates files
2. `xargs cat` reads them
3. `tax-categorize.py` categorizes and sums

Each step is simple and testable. If something breaks, you know exactly where to look.

This decomposition also makes the workflow reversible. Change the categories? Modify one dictionary. Change the file filter? Adjust the `find` command. Each piece is independent.

## Try With AI

### Prompt 1: Design a Merchant Pattern

```
I need to match all Amazon transactions in my bank statement.
The transactions appear as:
- AMZN MKTP US*ABC123
- AMAZON.COM*XYZ
- AMAZON PRIME*1234

Write a regex pattern that matches all these variations but does NOT match:
- AMAZONIA TRAVEL
- CAMZN AUTO PARTS

Explain why word boundaries (\b) are important for this pattern.
```

**What you are learning:** AI suggests regex syntax with word boundaries that prevent partial matches. Notice how it explains why "CAMZN" would be a false positive without proper anchoring.

### Prompt 2: Handle a False Positive

```
My tax categorization script has a problem. It marks "DR PEPPER" as medical
because the keyword list includes "dr." for doctor.

Here is my current code:
CATEGORIES = {'medical': ['cvs', 'walgreens', 'dr.', 'pharmacy']}

How do I add a false positive guard that excludes "dr. pepper" and
"dr pepper" from matching the medical category?
```

**What you are learning:** You teach AI about a limitation you discovered. Together you iterate toward a more robust solution using the guard pattern. This is the collaborative refinement loop - you provide the problem context, AI suggests solutions.

### Prompt 3: Extend the Categories

```
Help me add more categories to my tax-categorize.py script.

Current categories:
- medical: cvs, walgreens, pharmacy
- charitable: donation, charity, united way
- business: office depot, staples

I want to add:
- home_office: home depot, lowes, ikea (but NOT "IKEA RESTAURANT")
- subscriptions: netflix, spotify, hulu, apple.com

Help me design keyword lists that avoid false positives.
What patterns might I need to guard against?
```

**What you are learning:** Building a comprehensive categorization system requires thinking about edge cases. AI helps you anticipate false positives you might not have considered. The result is a more robust tool than either of you would create alone.
