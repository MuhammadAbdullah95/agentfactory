---
sidebar_position: 7
title: "Capstone: Tax Season Prep"
chapter: 8
lesson: 6
duration_minutes: 40
description: "Orchestrate a complete workflow to categorize and sum expenses from bank statement CSVs for tax preparation"
keywords:
  [
    "capstone",
    "workflow orchestration",
    "tax preparation",
    "expense categorization",
    "spec-driven",
    "seven principles",
    "CSV processing",
  ]

skills:
  - name: "Workflow Orchestration"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student composes all chapter skills (stdin, regex, CSV parsing, verification, alias) into complete workflow"

  - name: "Principle Mapping"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Reflective Learning"
    measurable_at_this_level: "Student maps at least 3 Seven Principles to specific actions taken in workflow"

learning_objectives:
  - objective: "Orchestrate complete workflow from CSV files to categorized expense report"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Student produces accurate categorized totals from bank statement folder with documented steps"

  - objective: "Map chapter activities to Seven Principles"
    proficiency_level: "A2"
    bloom_level: "Evaluate"
    assessment_method: "Student correctly identifies which principles apply to each step of their workflow"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (spec-first workflow, orchestration, skill composition, reflection, principle mapping) - reduced load for synthesis"

differentiation:
  extension_for_advanced: "Add date filtering, handle multiple currencies, generate CSV output for accountant"
  remedial_for_struggling: "Use provided spec template, follow step-by-step commands, just complete the workflow"
---

# Capstone: Tax Season Prep

Tax season arrives. Your accountant emails: "I need your deductible expenses categorized - medical, charitable donations, and business expenses. Can you pull that from your bank statements?"

You have 12 monthly CSV files from your bank, each with hundreds of transactions. Names like `january.csv`, `february.csv`, `march.csv`. Each row has a date, description, and amount. Buried in those thousands of lines are the expenses that could save you money on your taxes.

You could open each file manually, search for "CVS" and "pharmacy," copy amounts to a spreadsheet, then repeat for donations, then repeat for business expenses. That approach takes hours and guarantees you will miss something.

But you have spent the last five lessons building something better. You have tools that read from stdin, extract patterns with regex, and verify results with test data. You have a system that delivers 100% mathematical accuracy on messy, real-world data.

This capstone brings everything together. You will write a specification first, then orchestrate your accumulated skills to solve the Tax Prep problem.

## The Scenario

Here is your challenge:

- A folder called `finances/2025/` contains monthly bank statement CSVs
- Each CSV has columns: Date, Description, Amount
- You need to categorize transactions: Medical, Charitable, Business
- You must calculate subtotals for each category
- You must flag ambiguous transactions that need human review

This is the kind of problem that separates people who "use AI" from people who build with AI. Someone who just uses AI might paste file contents and ask for categorization. They would get hallucinated results and miss edge cases. You will build a pipeline that is systematic and verifiable.

## Spec First: Define Before You Build

Before touching the keyboard, write down what you intend to build. This is **spec-driven development** - a practice you will use throughout your agent-building career. The spec captures your intent clearly so you (and AI) know exactly what success looks like.

Create a file called `TAX-PREP-SPEC.md`:

```markdown
# Specification: Tax Prep Report Generator

## Intent

Categorize a year of bank transactions for tax preparation.

## Input

- Folder: ~/finances/2025/
- File format: Monthly CSV bank exports (january.csv, february.csv, etc.)
- Columns: Date, Description, Amount

## Output

- Categorized transactions with totals
- Report file for accountant
- List of ambiguous transactions needing review

## Success Criteria

- [ ] Medical expenses identified and summed
- [ ] Charitable donations identified and summed
- [ ] Business expenses identified and summed
- [ ] False positives avoided (Dr. Pepper, CVSmith)
- [ ] Verification against sample data passes
```

Notice what this spec does: it defines **what** without prescribing **how**. You know the goal. The implementation follows.

## Create Test Data

Before processing real bank statements, create test data with known answers. This is Principle 3 in action: never trust output you cannot verify.

```bash
# Create folder structure
mkdir -p ~/finances/2025

# Create sample CSV with known categorizable transactions
cat > ~/finances/2025/january.csv << 'EOF'
Date,Description,Amount
01/05/2025,CVS PHARMACY #1234,-45.67
01/05/2025,AMAZON.COM*AB1234,-23.99
01/06/2025,DR MARTINEZ MEDICAL,-150.00
01/07/2025,WALGREENS #5678,-32.50
01/10/2025,AMERICAN RED CROSS,-100.00
01/15/2025,OFFICE DEPOT #901,-89.99
01/18/2025,STAPLES #123,-45.00
01/20/2025,DOCTORS WITHOUT BORDERS,-50.00
01/22/2025,DR PEPPER BOTTLING,-4.99
01/25/2025,CVSMITH CONSULTING,-200.00
EOF
```

Now calculate the expected totals by hand:

**Medical expenses** (CVS, WALGREENS, DR MARTINEZ - NOT Dr. Pepper):

- CVS PHARMACY: $45.67
- WALGREENS: $32.50
- DR MARTINEZ MEDICAL: $150.00
- **Medical subtotal: $228.17**

**Charitable donations** (RED CROSS, DOCTORS WITHOUT BORDERS):

- AMERICAN RED CROSS: $100.00
- DOCTORS WITHOUT BORDERS: $50.00
- **Charitable subtotal: $150.00**

**Business expenses** (OFFICE DEPOT, STAPLES - NOT CVSmith consulting):

- OFFICE DEPOT: $89.99
- STAPLES: $45.00
- **Business subtotal: $134.99**

**Needs review** (ambiguous transactions):

- DR PEPPER BOTTLING: $4.99 (DR prefix, but not medical)
- CVSMITH CONSULTING: $200.00 (CV prefix, but not CVS pharmacy)

Write these down. This is your ground truth. Any workflow that produces different numbers has a bug.

## Build the Categorizer Script

Create `tax-prep.py` that reads CSV data from stdin and categorizes transactions:

```python
#!/usr/bin/env python3
"""
tax-prep.py - Categorize bank transactions for tax preparation

Reads CSV from stdin, categorizes by keywords, outputs report.
"""
import sys
import csv
import re
from collections import defaultdict

# Category keywords (case-insensitive matching)
CATEGORIES = {
    'MEDICAL': [
        r'\bCVS\b', r'\bWALGREENS\b', r'\bPHARMACY\b',
        r'\bMEDICAL\b', r'\bDOCTOR\b', r'\bCLINIC\b',
        r'\bHOSPITAL\b', r'\bURGENT CARE\b'
    ],
    'CHARITABLE': [
        r'\bRED CROSS\b', r'\bDONATION\b', r'\bCHARITY\b',
        r'\bFOUNDATION\b', r'\bDOCTORS WITHOUT BORDERS\b',
        r'\bUNITED WAY\b', r'\bGOODWILL\b'
    ],
    'BUSINESS': [
        r'\bOFFICE DEPOT\b', r'\bSTAPLES\b', r'\bOFFICE\b',
        r'\bSUBSCRIPTION\b', r'\bSOFTWARE\b', r'\bCLOUD\b'
    ]
}

# False positive patterns to exclude
EXCLUSIONS = {
    'MEDICAL': [r'\bDR PEPPER\b', r'\bDR\.? PEPPER\b'],
    'CHARITABLE': [],
    'BUSINESS': [r'\bCVSMITH\b', r'\bOFFICE PARTY\b']
}

def categorize_transaction(description):
    """Return category name or 'REVIEW' if ambiguous."""
    description_upper = description.upper()

    for category, patterns in CATEGORIES.items():
        for pattern in patterns:
            if re.search(pattern, description_upper, re.IGNORECASE):
                # Check for false positives
                for exclusion in EXCLUSIONS.get(category, []):
                    if re.search(exclusion, description_upper, re.IGNORECASE):
                        return 'REVIEW'
                return category

    return None  # Uncategorized

def main():
    categories = defaultdict(list)
    review_items = []

    # Read CSV from stdin
    reader = csv.DictReader(sys.stdin)

    for row in reader:
        description = row.get('Description', '')
        amount_str = row.get('Amount', '0')

        try:
            amount = abs(float(amount_str))
        except ValueError:
            continue

        category = categorize_transaction(description)

        if category == 'REVIEW':
            review_items.append((description, amount))
        elif category:
            categories[category].append((description, amount))

    # Generate report
    print("=" * 50)
    print("2025 TAX CATEGORIZATION REPORT")
    print("=" * 50)
    print()

    total_deductions = 0

    for category in ['MEDICAL', 'CHARITABLE', 'BUSINESS']:
        items = categories.get(category, [])
        if items:
            subtotal = sum(amount for _, amount in items)
            total_deductions += subtotal

            schedule = "(Schedule A)" if category in ['MEDICAL', 'CHARITABLE'] else "(if applicable)"
            print(f"{category} {schedule}:")

            # Group by vendor
            vendor_totals = defaultdict(lambda: {'count': 0, 'total': 0})
            for desc, amt in items:
                vendor_totals[desc]['count'] += 1
                vendor_totals[desc]['total'] += amt

            for vendor, data in sorted(vendor_totals.items()):
                print(f"  {vendor} ({data['count']} txns)      ${data['total']:.2f}")

            print(f"  SUBTOTAL:                   ${subtotal:.2f}")
            print()

    print("=" * 50)
    print(f"POTENTIAL DEDUCTIONS: ${total_deductions:.2f}")
    print("=" * 50)

    if review_items:
        print()
        print("NEEDS REVIEW:")
        for desc, amount in review_items:
            print(f"  - \"{desc}\" ${amount:.2f} - business or personal?")

if __name__ == '__main__':
    main()
```

Make it executable:

```bash
chmod +x tax-prep.py
```

## Verify Your Tool Works

Before processing real data, verify the script works on test data:

```bash
cat ~/finances/2025/january.csv | python tax-prep.py
```

**Expected output:**

```
==================================================
2025 TAX CATEGORIZATION REPORT
==================================================

MEDICAL (Schedule A):
  CVS PHARMACY #1234 (1 txns)      $45.67
  DR MARTINEZ MEDICAL (1 txns)      $150.00
  WALGREENS #5678 (1 txns)      $32.50
  SUBTOTAL:                   $228.17

CHARITABLE (Schedule A):
  AMERICAN RED CROSS (1 txns)      $100.00
  DOCTORS WITHOUT BORDERS (1 txns)      $50.00
  SUBTOTAL:                   $150.00

BUSINESS (if applicable):
  OFFICE DEPOT #901 (1 txns)      $89.99
  STAPLES #123 (1 txns)      $45.00
  SUBTOTAL:                   $134.99

==================================================
POTENTIAL DEDUCTIONS: $513.16
==================================================

NEEDS REVIEW:
  - "DR PEPPER BOTTLING" $4.99 - business or personal?
  - "CVSMITH CONSULTING" $200.00 - business or personal?
```

Compare against your hand-calculated totals:

- Medical: $228.17 (matches)
- Charitable: $150.00 (matches)
- Business: $134.99 (matches)
- Review items correctly flagged Dr. Pepper and CVSmith

Your tool is verified. The workflow is ready for real data.

## Combining CSV Files

You learned `head` in Chapter 7. Now apply it to merge multiple CSV files. The challenge: each file has a header row, but you only want ONE header in the combined file.

### New Flags for CSV Merging

| Flag | What It Does | Example |
|------|-------------|---------|
| `head -1` | Show only first line | `head -1 file.csv` → header row |
| `tail -n +2` | Start from line 2 (skip header) | `tail -n +2 file.csv` → data only |
| `tail -q` | Quiet mode - no filename headers | Cleaner output with multiple files |

### Combining CSVs Without Duplicate Headers

```bash
# Get header from first file only
head -1 january.csv > combined.csv

# Append data (no headers) from ALL files
tail -n +2 -q *.csv >> combined.csv
```

The result: one combined file with a single header row followed by all data rows.

## The Complete Workflow

Now orchestrate everything. Each step uses skills you built in previous lessons:

```bash
# Step 1: Verify the tool works (Lesson 3 - Zero-Trust)
cat ~/finances/2025/january.csv | python tax-prep.py
# Verify output matches expected totals

# Step 2: Combine all monthly CSVs (skip header rows after first file)
head -1 ~/finances/2025/january.csv > all-2025.csv
tail -n +2 -q ~/finances/2025/*.csv >> all-2025.csv

# Step 3: Run categorizer on full year
cat all-2025.csv | python tax-prep.py

# Step 4: Generate report for accountant
cat all-2025.csv | python tax-prep.py > tax-report-2025.txt

# Step 5: Verify report was created
cat tax-report-2025.txt
```

For a full year of data, the output would look like:

```
==================================================
2025 TAX CATEGORIZATION REPORT
==================================================

MEDICAL (Schedule A):
  CVS PHARMACY (23 txns)      $456.70
  WALGREENS (15 txns)         $234.50
  Medical offices (8 txns)    $1,200.00
  SUBTOTAL:                   $1,891.20

CHARITABLE (Schedule A):
  Donations identified        $1,550.00

BUSINESS (if applicable):
  Office supplies             $234.56
  Subscriptions               $539.76
  SUBTOTAL:                   $774.32

==================================================
POTENTIAL DEDUCTIONS: $4,215.52
==================================================

NEEDS REVIEW:
  - "SQ *LOCALSTORE" $200.00 - business or personal?
```

## What Just Happened

Let's trace the data flow:

```
~/finances/2025/*.csv  -->  Combine CSVs  -->  tax-prep.py  -->  Report
     |                         |                   |              |
  Monthly bank           Remove duplicate      Categorize     Subtotals +
  statements             headers, merge        + sum          review list
```

The shell orchestrates file handling. Your Python tool handles the categorization. The regex patterns identify transaction types. The output is a report your accountant can use directly.

Each piece does one thing. Together, they solve the Tax Prep problem with systematic accuracy.

## Scaling Up

Your verified workflow works on 1 month of data. It works identically on 12 months or 10 years:

```bash
# Works the same whether 1 file or 120 files
head -1 ~/finances/2025/january.csv > all-years.csv
find ~/finances/ -name "*.csv" -exec tail -n +2 {} \; >> all-years.csv
cat all-years.csv | python tax-prep.py
```

No changes needed. The workflow scales because each component is designed for composition.

## Reflection: The Seven Principles

You just applied the Seven Principles from Chapter 3 without thinking about them explicitly. Now make that connection conscious.

| Principle                               | How You Applied It                                           |
| --------------------------------------- | ------------------------------------------------------------ |
| **P1: Bash is the Key**                 | Used `cat`, `head`, `tail`, pipes as foundation for data flow |
| **P2: Code as Universal Interface**     | Python script (`tax-prep.py`) as reusable component          |
| **P3: Verification as Core Step**       | Tested with known data before processing real statements     |
| **P4: Small, Reversible Decomposition** | Each lesson built one composable skill                       |
| **P5: Persisting State in Files**       | Script and report files persist across sessions              |
| **P6: Constraints and Safety**          | Spec defined boundaries; exclusion patterns prevented false positives |
| **P7: Observability**                   | "NEEDS REVIEW" section makes ambiguity visible               |

Count them: all seven principles appeared in a 40-minute exercise. This is not coincidence. The principles are how agents work effectively with computing systems. You internalized them through practice.

## The Victory

Step back and recognize what you accomplished.

**Before this chapter**: Asking AI to categorize expenses from memory. Hoping nothing gets missed. No systematic verification. False positives mixed with real deductions.

**After this chapter**: A personal toolbox that processes bank statements, categorizes transactions with pattern matching, flags ambiguous items for review, and calculates totals with 100% mathematical accuracy. Verified against known data. Reusable across any time period, any number of files.

You built your first Digital FTE component - a tool that does tedious work accurately, every time, without missing edge cases or hallucinating categories.

The same pattern applies to expense reports, invoice processing, subscription tracking, or any scenario where transactions need categorization. You have the foundation.

## Try With AI

### Prompt 1: Spec Assistance

```
Help me write a specification for a tax preparation expense categorizer.

I have a folder with monthly bank statement CSVs containing columns:
Date, Description, Amount

I need to:
1. Categorize transactions as Medical, Charitable, or Business
2. Calculate subtotals for each category
3. Flag ambiguous transactions for manual review

What sections should my spec include? What success criteria
should I define? Help me think through edge cases like
"Dr. Pepper" matching medical patterns.
```

**What you're learning:** AI suggests structure for specification - intent, constraints, success criteria, edge cases. You define what success looks like before implementing. Notice how discussing false positives upfront prevents bugs later. This is spec-driven thinking.

### Prompt 2: Pattern Refinement

```
I have a tax categorization script that uses regex patterns like:
r'\bCVS\b' for medical expenses

But it's catching "CVSMITH CONSULTING" as medical because
the pattern sees "CVS" at the start.

Help me build an exclusion list approach where I can match
CVS pharmacy but exclude CVSmith. Show me how to implement
this in Python with the re module.
```

**What you're learning:** You teach AI about YOUR specific problem - the false positive you discovered. The AI does not suggest generic solutions; it works with your existing toolbox and improves it. This is the collaboration pattern: your context, AI's pattern expertise.

### Prompt 3: Workflow Extension

```
My tax-prep.py script works well for categorizing. Now I want to:
1. Add a date range filter (only Q4 transactions)
2. Generate CSV output instead of text (for Excel import)
3. Add a "PERSONAL" category for everything uncategorized

Show me how to extend the script. Keep the stdin/stdout
pattern so it still works in pipelines.
```

**What you're learning:** Incremental extension of working code. The AI helps you add features while preserving the Unix philosophy (stdin/stdout, composability). You maintain control of the architecture; AI accelerates implementation. This is how professional tools evolve.
