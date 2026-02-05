---
sidebar_position: 6
title: "Data Wrangling"
chapter: 8
lesson: 5
layer: L2
duration_minutes: 35
description: "Watch Claude Code categorize bank transactions with regex patterns and false-positive guards, then process multiple files"
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
  - name: "Directing Pattern-Based Categorization"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Data Processing"
    measurable_at_this_level: "Student can direct Claude Code to build a categorizer with edge case handling"

  - name: "Understanding Regex Patterns"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Pattern Recognition"
    measurable_at_this_level: "Student can explain why word boundaries prevent false matches"

  - name: "Batch File Processing"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Automation"
    measurable_at_this_level: "Student uses find and xargs to process multiple files"

learning_objectives:
  - objective: "Direct Claude Code to build a transaction categorizer with false-positive guards"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student prompts agent to create tax-categorize.py that handles edge cases"

  - objective: "Explain how regex word boundaries prevent false matches"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can explain why \\bCVS\\b matches 'CVS PHARMACY' but not 'CVSMITH'"

  - objective: "Use find and xargs to batch process multiple CSV files"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student executes: find . -name '*.csv' | xargs cat | python tax-categorize.py"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (categorization logic, regex patterns, word boundaries, false positive guards, batch processing) within A2 limit"

differentiation:
  extension_for_advanced: "Handle case sensitivity, regex anchors for precision, more complex patterns"
  remedial_for_struggling: "Focus on the conversation - use pre-built keyword lists, don't modify patterns yourself"
---

# Data Wrangling

sum-expenses gives you totals. But tax season needs CATEGORIES - medical, charitable, business. Your accountant doesn't want "Total: $4,215.52." They want:

- Medical expenses: $1,891.20
- Charitable donations: $1,550.00
- Business supplies: $774.32

The challenge: bank statements use chaotic merchant names. CVS, Walgreens, and "PHARMACY #1234" are all medical. "DR MARTINEZ MEDICAL" is a doctor visit. But "DR PEPPER SNAPPLE" is soda, not a medical expense.

Watch Claude Code build a categorizer that handles this complexity.

## The Problem

Your bank statement has transactions like:

```
CVS/PHARMACY #1234      -$45.67
WALGREENS #5678         -$23.45
DR MARTINEZ MEDICAL     -$150.00
DR PEPPER SNAPPLE       -$4.99
UNITED WAY              -$100.00
CVSMITH CONSULTING      -$200.00
OFFICE DEPOT #901       -$89.50
```

You need to categorize these for taxes. But:

- "DR" appears in both doctor visits and Dr. Pepper
- "CVS" appears in CVS Pharmacy and CVSMITH (a person's name)
- Multiple variations: CVS, WALGREENS, PHARMACY all mean medical

Simple keyword matching will produce false positives. You need pattern matching that's both flexible and precise.

## The Conversation

Open Claude Code and describe your categorization challenge:

```
You: Help me categorize my bank transactions for taxes. I need to identify:
- Medical: CVS, Walgreens, pharmacy, doctor visits
- Charitable: donations, Red Cross, United Way
- Business: Office Depot, Staples, subscriptions

Be careful: "Dr. Pepper" is NOT medical. "CVSmith" is NOT CVS pharmacy.
```

Watch what Claude Code does:

```
Claude Code: Smart to flag those false positives upfront. I'll build a
categorizer with regex patterns and false positive guards.

[Creates: tax-categorize.py]

#!/usr/bin/env python3
import sys
import csv
import re

CATEGORIES = {
    'medical': [r'\bCVS\b', r'\bWALGREENS\b', r'\bPHARMACY\b', r'\bMEDICAL\b'],
    'charitable': [r'\bDONATION\b', r'\bRED CROSS\b', r'\bUNITED WAY\b'],
    'business': [r'\bOFFICE DEPOT\b', r'\bSTAPLES\b', r'\bSUBSCRIPTION\b'],
}

# False positive guards - check BEFORE categories
FALSE_POSITIVES = [r'\bDR\.? PEPPER\b', r'\bCVSMITH\b']

def categorize(description):
    desc_upper = description.upper()

    # Check false positives first
    for fp_pattern in FALSE_POSITIVES:
        if re.search(fp_pattern, desc_upper, re.IGNORECASE):
            return None  # Not a tax category

    # Check categories
    for category, patterns in CATEGORIES.items():
        for pattern in patterns:
            if re.search(pattern, desc_upper, re.IGNORECASE):
                return category
    return None

# Process CSV...
[rest of script]

Let me test with your tricky data:

[Creates: test_bank.csv with all the example transactions]
[Runs: cat test_bank.csv | python tax-categorize.py]

MEDICAL: CVS/PHARMACY #1234: $45.67
MEDICAL: WALGREENS #5678: $23.45
MEDICAL: DR MARTINEZ MEDICAL: $150.00
CHARITABLE: UNITED WAY: $100.00
BUSINESS: OFFICE DEPOT #901: $89.50

--- TOTALS ---
Medical: $219.12
Charitable: $100.00
Business: $89.50

Notice:
✓ "DR PEPPER SNAPPLE" correctly excluded (false positive guard)
✓ "CVSMITH CONSULTING" correctly excluded (false positive guard)
✓ "DR MARTINEZ MEDICAL" correctly included (has MEDICAL keyword)
```

The agent built a categorizer that distinguishes Dr. Martinez (medical) from Dr. Pepper (soda), and CVS Pharmacy from CVSmith.

## What Just Happened?

You witnessed pattern matching with safeguards.

**The false positive guard pattern.** The agent checks false positives BEFORE checking categories. "Dr. Pepper" matches the false positive pattern first, so it never reaches the medical category check.

**Regex word boundaries.** The pattern `\bCVS\b` uses `\b` (word boundary) on both sides. This means:

- `\bCVS\b` matches "CVS PHARMACY" (CVS is a complete word)
- `\bCVS\b` does NOT match "CVSMITH" (CVS is part of a longer word)

**Order matters.** False positives are checked first. Categories are checked second. This ordering prevents "DR PEPPER" from being categorized as medical just because it contains "DR".

### Why Regex Instead of Simple Contains?

Simple keyword matching fails:

```python
# BAD: Simple contains
if 'cvs' in description.lower():
    return 'medical'
# This matches "CVSMITH" - wrong!
```

Regex with word boundaries succeeds:

```python
# GOOD: Word boundary regex
if re.search(r'\bCVS\b', description, re.IGNORECASE):
    return 'medical'
# This does NOT match "CVSMITH" - correct!
```

The `\b` ensures CVS is a complete word, not part of another word.

## The Agent's Toolkit: Regex Patterns

### Word Boundaries

`\b` marks where a word starts or ends:

```
\bCVS\b    matches: "CVS PHARMACY", "CVS", "at CVS today"
           rejects: "CVSMITH", "MCVS", "CVSX"
```

Without boundaries:

```
CVS        matches: "CVS", "CVSMITH", "MCVS" (too broad!)
```

### Alternatives with |

Match multiple options:

```python
r'\b(CVS|WALGREENS|PHARMACY)\b'
# Matches: CVS, WALGREENS, or PHARMACY as complete words
```

### Optional Characters with ?

```python
r'\bDR\.?\b'
# Matches: "DR" or "DR." (period is optional)
```

### Common Patterns for Financial Data

| Pattern | What It Matches | What It Rejects |
|---------|-----------------|-----------------|
| `\bCVS\b` | CVS, CVS PHARMACY | CVSMITH |
| `\b(AMZN\|AMAZON)\b` | AMZN, AMAZON, AMAZON.COM | CAMZN, AMAZONIA |
| `\bDR\.?\s` | "DR ", "DR. " (doctor) | DR PEPPER (no space after) |
| `\bWAL-?MART\b` | WALMART, WAL-MART | WALMARTIN |

## Processing Multiple Files

You have 12 months of bank statements. Processing them one by one would be tedious.

### The Conversation Continues

```
You: I have a folder with 12 months of bank statements (january.csv through
december.csv). Process them all at once.
```

```
Claude Code: I'll use find and xargs to batch process all CSV files.

[Runs: find statements/ -name "*.csv" | xargs cat | python tax-categorize.py]

Processing 12 files...
Total transactions: 1,247

MEDICAL (Schedule A):
  CVS PHARMACY (23 txns)      $456.70
  WALGREENS (15 txns)         $234.50
  Doctor visits (8 txns)      $1,200.00
  SUBTOTAL:                   $1,891.20

CHARITABLE (Schedule A):
  Donations (12 txns)         $1,550.00

BUSINESS:
  Office supplies (18 txns)   $539.76
  Subscriptions (9 txns)      $234.56
  SUBTOTAL:                   $774.32

All 12 months processed in one command.
```

### The Agent's Toolkit: find and xargs

**find** locates files matching a pattern:

```bash
find statements/ -name "*.csv"
# Output:
# statements/january.csv
# statements/february.csv
# ...
```

**xargs** takes that list and runs a command on it:

```bash
find statements/ -name "*.csv" | xargs cat
# Concatenates all CSV files together
```

**The full pipeline:**

```bash
find statements/ -name "*.csv" | xargs cat | python tax-categorize.py
```

1. `find` locates all CSV files
2. `xargs cat` reads them all
3. `tax-categorize.py` categorizes and sums

One command processes an entire folder.

## The Pattern

Here's the categorization prompt pattern:

```
"Categorize [data] by [criteria]. Watch out for [false positives]."
```

Mentioning false positives explicitly helps the agent build guards:

| Prompt | Result |
|--------|--------|
| "Categorize transactions as medical" | Basic keyword matching |
| "Categorize as medical. Watch out for Dr. Pepper" | Adds false positive guard |

The explicit edge case produces more robust code.

### Pattern for Batch Processing

```
"I have [multiple files matching pattern]. Process them all at once."
```

This signals you want:
- File discovery with `find`
- Batch execution with `xargs`
- Aggregated results

## Try It Yourself

Test the categorizer with edge cases:

```bash
# Create test data with tricky cases
cat > test_tricky.csv << 'EOF'
Date,Description,Amount
2024-01-01,CVS PHARMACY,-$45.00
2024-01-02,CVSMITH CONSULTING,-$200.00
2024-01-03,DR MARTINEZ CLINIC,-$150.00
2024-01-04,DR PEPPER SNAPPLE,-$4.99
2024-01-05,AMAZON PHARMACY,-$30.00
EOF

cat test_tricky.csv | python tax-categorize.py
```

**Expected:**

- CVS PHARMACY → Medical (✓)
- CVSMITH CONSULTING → Not categorized (correct - false positive guard)
- DR MARTINEZ CLINIC → Medical (has CLINIC keyword)
- DR PEPPER SNAPPLE → Not categorized (correct - false positive guard)
- AMAZON PHARMACY → Medical (has PHARMACY keyword)

If Dr. Pepper or CVSmith appear in the output, the false positive guards aren't working.

## Connecting to the Seven Principles

**Principle 2: Code as Universal Interface**

Your category keywords and regex patterns are precise specifications. They remove ambiguity - "CVS" matches CVS pharmacy, not CVSMITH. The patterns are code, executable and verifiable.

**Principle 4: Small, Reversible Decomposition**

The pipeline decomposes into three steps:
1. `find` locates files
2. `xargs cat` reads them
3. `tax-categorize.py` categorizes and sums

Each step is simple and testable. If something breaks, you know exactly where to look.

**Principle 6: Constraints and Safety**

The false positive guards are constraints that prevent incorrect categorization. You defined what should NOT match, not just what should match.

---

## Try With AI

### Prompt 1: Design a Merchant Pattern

```
I need to match all Amazon transactions in my bank statement.
They appear as: AMZN MKTP US, AMAZON.COM, AMAZON PRIME

Write a regex pattern that matches all these but does NOT match:
- AMAZONIA TRAVEL
- CAMZN AUTO PARTS

Explain why word boundaries matter here.
```

**What you're learning:** Regex design with precision. The agent shows how `\b(AMZN|AMAZON)\b` catches variations while excluding false positives. You understand the WHY, not just the pattern.

### Prompt 2: Handle a New False Positive

```
My tax-categorize.py marks "AMAZON RIVER CRUISE" as a purchase
from Amazon.com. It's actually a travel expense.

How do I add this to the false positive guards? Show me the pattern
that excludes travel-related Amazon mentions.
```

**What you're learning:** Iterative refinement. As you discover new false positives, you update the guards. The agent shows how to add patterns without breaking existing categorization.

### Prompt 3: Extend Categories

```
Help me add these categories to tax-categorize.py:
- home_office: Home Depot, Lowes, Ikea (but NOT "IKEA RESTAURANT")
- subscriptions: Netflix, Spotify, Hulu, Apple.com

What false positives might I need to guard against?
```

**What you're learning:** Proactive edge case thinking. The agent suggests guards you might not have considered - like distinguishing IKEA furniture from IKEA food court. You're learning to anticipate problems before they happen.
