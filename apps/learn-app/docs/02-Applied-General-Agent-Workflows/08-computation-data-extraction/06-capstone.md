---
sidebar_position: 7
title: "Capstone: The Digital Shoebox"
chapter: 7
lesson: 6
duration_minutes: 40
description: "Orchestrate a complete workflow to calculate totals from a folder of receipt files"
keywords:
  [
    "capstone",
    "workflow orchestration",
    "digital shoebox",
    "spec-driven",
    "seven principles",
  ]

skills:
  - name: "Workflow Orchestration"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student composes all chapter skills (stdin, regex, verification, alias) into complete workflow"

  - name: "Principle Mapping"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Reflective Learning"
    measurable_at_this_level: "Student maps at least 3 Seven Principles to specific actions taken in workflow"

learning_objectives:
  - objective: "Orchestrate complete workflow from file discovery to total calculation"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Student produces accurate total from receipt folder with documented steps"

  - objective: "Map chapter activities to Seven Principles"
    proficiency_level: "A2"
    bloom_level: "Evaluate"
    assessment_method: "Student correctly identifies which principles apply to each step of their workflow"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (spec-first workflow, orchestration, skill composition, reflection, principle mapping) - reduced load for synthesis"

differentiation:
  extension_for_advanced: "Add CSV output, handle receipts in subdirectories recursively, add date filtering"
  remedial_for_struggling: "Use provided spec template, follow step-by-step commands, just complete the workflow"
---

# Capstone: The Digital Shoebox

You have a shoebox. Not a literal one, but everyone has the digital equivalent: a folder where receipts accumulate. Maybe it is called "Expenses" or "Receipts 2025" or just sits in your Downloads folder. Files with names like `amazon_receipt.txt`, `lunch_march.txt`, `office_supplies.txt`. Each contains messy text with dollar amounts buried in sentences.

Tax season arrives. Your accountant asks: "What was your total business spending this quarter?"

You stare at that folder. Twenty-three files. Dollar amounts scattered through paragraphs. No way are you opening each file, hunting for numbers, and adding them manually. That is error-prone and tedious.

But you have spent the last five lessons building something better. You have tools. You have a workflow. You have a system that delivers 100% mathematical accuracy on messy, real-world data.

This capstone brings everything together. You will write a specification first, then orchestrate your accumulated skills to solve the Digital Shoebox problem.

## The Scenario

Here is your challenge:

- A folder called `receipts/` contains text files
- Each file has dollar amounts buried in sentences
- You need the total of all dollar amounts across all files
- You must verify your result is accurate

This is the kind of problem that separates people who "use AI" from people who build with AI. Someone who just uses AI might paste each file's contents and ask for a sum. They would get hallucinated results. You will build a pipeline that is mathematically certain.

## Spec First: Define Before You Build

Before touching the keyboard, write down what you intend to build. This is **spec-driven development**—a practice you will use throughout your agent-building career. The spec captures your intent clearly so you (and AI) know exactly what success looks like.

Create a file called `RECEIPT-SPEC.md`:

```markdown
# Specification: Receipt Total Calculator

## Intent

Calculate total spending from folder of receipt files.

## Input

- Folder: receipts/
- File format: .txt files with dollar amounts in sentences
- Example content: "Lunch meeting: $24.50 plus tip $5.00"

## Constraints

- Handle messy text (dollar amounts buried in sentences)
- Extract values like $10.00, $5.50, $100.00
- Skip non-monetary text
- Process ALL .txt files in receipts/ folder

## Success Criteria

- [ ] Correct total extracted (verified against manual count)
- [ ] Verification steps documented
- [ ] Workflow uses skills from Lessons 1-5:
  - [ ] Python script reads from stdin (Lesson 2)
  - [ ] Zero-trust verification with test data (Lesson 3)
  - [ ] Alias for easy invocation (Lesson 4)
  - [ ] Regex extraction of dollar amounts (Lesson 5)
```

Notice what this spec does: it defines **what** without prescribing **how**. You know the goal. The implementation follows.

## Create Test Data

Before processing real receipts, create test data with a known answer. This is Principle 3 in action: never trust output you cannot verify.

```bash
# Create receipts folder
mkdir -p receipts

# Create test receipts with known amounts
echo "Office supplies from Amazon: $15.00" > receipts/office.txt
echo "Team lunch at Bistro: $45.50 including tip" > receipts/lunch.txt
echo "Software subscription: $9.99 monthly charge" > receipts/software.txt
```

Now calculate the expected total by hand:

- office.txt: $15.00
- lunch.txt: $45.50
- software.txt: $9.99

**Expected total: $70.49**

Write this down. This is your ground truth. Any workflow that produces a different number has a bug.

## Verify Your Tool Works

Before processing real data, verify your `add-up` alias (from Lesson 4) works correctly:

```bash
# Step 1: Test with known data
echo -e "Test receipt: \$10.00\nAnother item: \$5.00" > test_receipt.txt
cat test_receipt.txt | add-up
```

**Expected output:**

```
Total: $15.00
```

If you see `Total: $15.00`, your tool works. If not, revisit Lesson 4 and fix your alias before proceeding.

This verification step takes 30 seconds. Skipping it could cost you hours debugging a workflow that fails because of a broken tool.

## The Complete Workflow

Now orchestrate everything. Each step uses a skill you built in previous lessons:

```bash
# Step 1: Verify the tool works (Lesson 3 - Zero-Trust)
echo -e "Test: \$10.00\nItem: \$5.00" | add-up
# Expected: Total: $15.00

# Step 2: Process all receipts (Lesson 5 - Batch Processing)
cat receipts/*.txt | add-up
# Expected: Total: $70.49

# Step 3: Document verification
echo "Manual calculation: 15.00 + 45.50 + 9.99 = 70.49"
echo "Script output: matches"
```

Run the workflow:

```bash
cat receipts/*.txt | add-up
```

**Expected output:**

```
Total: $70.49
```

The output matches your hand-calculated total. Your workflow is verified.

## What Just Happened

Let's trace the data flow:

```
┌──────────────┐     ┌───────────────┐     ┌──────────────┐     ┌────────────┐
│ receipts/*.txt │────▶│  cat (shell)  │────▶│   add-up     │────▶│  $70.49    │
│              │     │               │     │   (regex +   │     │            │
│ office.txt   │     │  concatenates │     │    sum)      │     │            │
│ lunch.txt    │     │  all files    │     │              │     │            │
│ software.txt │     │               │     │              │     │            │
└──────────────┘     └───────────────┘     └──────────────┘     └────────────┘
```

The shell (`cat`) orchestrates file reading. Your Python tool (`add-up`) handles the computation. The regex extracts dollar amounts. The sum is calculated. The result is displayed.

Each piece does one thing. Together, they solve the Digital Shoebox problem with 100% accuracy.

## Scaling Up

Your verified workflow works on 3 files. It works identically on 300 files:

```bash
# Works the same whether 3 files or 300 files
cat receipts/*.txt | add-up
```

No changes needed. The workflow scales because each component is designed for composition.

For more complex scenarios, use `find` with `xargs`:

```bash
# Process receipts in subdirectories too
find receipts/ -name "*.txt" -exec cat {} + | add-up
```

The pattern stays the same: find files, concatenate, extract and sum.

## Reflection: The Seven Principles

You just applied the Seven Principles from Chapter 3 without thinking about them explicitly. Now make that connection conscious.

| Principle                               | How You Applied It                                             |
| --------------------------------------- | -------------------------------------------------------------- |
| **P1: Bash is the Key**                 | Used `cat`, `find`, pipes as foundation for data flow          |
| **P2: Code as Universal Interface**     | Python script (`add-up`) as reusable component                 |
| **P3: Verification as Core Step**       | Tested with known data before processing real receipts         |
| **P4: Small, Reversible Decomposition** | Each lesson built one composable skill                         |
| **P5: Persisting State in Files**       | Alias makes tool permanent across sessions                     |
| **P6: Constraints and Safety**          | Spec defined boundaries first; test data prevented blind trust |
| **P7: Observability**                   | Exit codes and test output show success or failure clearly     |

Count them: all seven principles appeared in a 40-minute exercise. This is not coincidence. The principles are how agents work effectively with computing systems. You internalized them through practice.

## The Victory

Step back and recognize what you accomplished.

**Before this chapter**: Asking AI to add up numbers in your head. Hoping the answer is right. No way to verify. Hallucination risk.

**After this chapter**: A personal toolbox that extracts dollar amounts from messy text and calculates totals with 100% mathematical accuracy. Verified against known data. Reusable across any folder, any number of files.

You built your first Digital FTE component—a tool that does tedious work accurately, every time, without complaining about the mess.

The same pattern applies to expense reports, invoice processing, time tracking, data extraction from emails, or any scenario where numbers hide in text. You have the foundation.

## Try With AI

### Prompt 1: Spec Assistance

```
Help me write a specification for a receipt total calculator.

I have a folder called "expenses/" with .txt files containing
text like "Coffee meeting: $4.50" and "Office supplies: $23.99"

I need to:
1. Extract all dollar amounts from all files
2. Calculate the total
3. Verify accuracy

What sections should my spec include? What success criteria
should I define? Help me think through edge cases.
```

**What you're learning:** AI suggests structure for specification—intent, constraints, success criteria, edge cases. You define what success looks like before implementing. This is spec-driven thinking.

### Prompt 2: Tool Composition

```
I have an alias called "add-up" that reads text from stdin,
extracts dollar amounts using regex, and prints the sum.

I have a folder called "receipts/" with .txt files.

Help me compose a single command that:
1. Finds all .txt files in receipts/
2. Pipes their contents to my add-up tool
3. Gives me the total

Show me the command and explain what each part does.
```

**What you're learning:** You teach AI about YOUR tools and ask it to compose them. The AI does not suggest generic solutions—it works with your existing toolbox. This is the collaboration pattern: your tools, AI's composition help.

### Prompt 3: Principle Mapping

```
I just completed a workflow that calculates receipt totals:
1. Created test data with known answer
2. Verified my tool works on test data
3. Ran tool on real receipts
4. Confirmed output matches manual calculation

Map each step to the Seven Principles of General Agent Problem Solving.
Which principles did I apply? Which ones might I have missed?
```

**What you're learning:** Reflective practice with AI as learning partner. The AI helps you see your actions through the lens of principles, strengthening the connection between theory and practice. This reflection cements learning.
