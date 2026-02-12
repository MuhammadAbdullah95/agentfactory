---
sidebar_position: 1
title: "Chapter 8: Computation & Data Extraction Workflow"
description: "Build Unix-styled Python utilities that process bank statements and prepare tax reports with 100% accuracy"
---

# Chapter 8: Computation & Data Extraction Workflow

> "If it's math, it belongs in a script. Period."

## What You'll Build

By the end of this chapter, you'll have a personal toolbox of reusable utilities:

```bash
# Your workflow by chapter end:
cat ~/finances/2025/*.csv | tax-prep

# Output:
# MEDICAL: CVS PHARMACY: $456.70
# MEDICAL: WALGREENS: $234.50
# CHARITABLE: RED CROSS: $200.00
# BUSINESS: ZOOM SUBSCRIPTION: $179.88
#
# --- TOTALS ---
# Medical: $1,891.20
# Charitable: $1,550.00
# Business: $774.32
#
# POTENTIAL DEDUCTIONS: $4,215.52
```

You'll transform from someone who manually categorizes expenses (tedious and error-prone) to someone who builds verified automation tools that work every tax season.

## Prerequisites

**From Seven Principles Chapter**:

- You understand ALL Seven Principles conceptually
- You know why "Bash is the Key" matters (Principle 1)
- You know why "Verification as Core Step" prevents failures (Principle 3)

**From File Processing Chapter**:

- You can navigate directories (`cd`, `ls`, `pwd`)
- You've run basic Bash commands
- You understand the pipe operator (`|`) conceptually

**Technical Requirements**:

- Python 3.x installed (type `python3 --version` to check)
- Unix-like terminal (macOS, Linux, or WSL on Windows)
- Access to Claude Code or similar AI assistant
- A bank statement CSV export (most banks offer this)

## Chapter Structure

| Lesson | Title                       | Duration | Key Skill                              |
| ------ | --------------------------- | -------- | -------------------------------------- |
| 1      | The Arithmetic Gap          | 15 min   | Recognize Bash decimal limitations     |
| 2      | Your First Python Utility   | 25 min   | Build stdin-reading script             |
| 3      | The Testing Loop            | 25 min   | Verify with exit codes and test data   |
| 4      | From Script to Command      | 30 min   | Parse CSV, make permanent commands       |
| 5      | Data Wrangling              | 35 min   | Categorize with regex pattern matching |
| 6      | Capstone: Tax Season Prep        | 40 min   | Generate tax-ready report              |

**Total Duration**: 170 minutes (~3 hours)

## Seven Principles in Action

This chapter applies the principles you learned in Chapter 6:

| Principle                               | How You'll Apply It                                  |
| --------------------------------------- | ---------------------------------------------------- |
| **P1: Bash is the Key**                 | Use `cat`, `find`, `xargs`, pipes as your foundation |
| **P2: Code as Universal Interface**     | Python scripts as reusable components                |
| **P3: Verification as Core Step**       | Zero-trust debugging with exit codes                 |
| **P4: Small, Reversible Decomposition** | Each lesson builds one composable skill              |
| **P5: Persisting State in Files**       | Aliases and scripts as persistent tools              |
| **P6: Constraints and Safety**          | Test data prevents production errors                 |
| **P7: Observability**                   | Exit codes make failures visible                     |

## The Journey

**Lesson 1-2**: Foundation

- Discover why Bash arithmetic fails with decimals
- Build a Python script that reads numbers from stdin and calculates sums

**Lesson 3**: Verification

- Learn zero-trust debugging with exit codes
- Create test data with known answers to verify your scripts

**Lesson 4**: From Script to Command

- Understand why simple text tools (like awk) fail on real CSV
- Build a CSV parser with Python's csv module
- Transform scripts into permanent commands via aliases

**Lesson 5**: Tax Categorization

- Use pattern matching to categorize transactions (Medical, Charitable, Business)
- Handle false positives (Dr. Pepper is not a doctor)
- Build your `tax-categorize` script

**Lesson 6**: Capstone

- Orchestrate everything into a real-world tax preparation workflow
- Generate a report your accountant can use
- Process a full year of bank statements with one command

## Quick Start for Previous Chapter Graduates

Already comfortable with terminal basics? Here's what's new:

```bash
# Bash math FAILS with decimals (you'll discover why)
echo $((14.50 + 23.75))  # Error!

# Simple text tools FAIL on quoted CSV fields
echo '"Amazon, Inc.",-23.99' | awk -F',' '{print $2}'
# Output: Inc."  -- WRONG! Broke on comma inside quotes

# Python handles both correctly (you'll build this)
cat bank-statement.csv | python sum-expenses.py
# Output: Total: $2,456.78

# Pattern matching categorizes for taxes (you'll learn this)
cat bank-statement.csv | python tax-categorize.py
# Output: Medical: $1,891.20, Charitable: $1,550.00
```

## The Real-World Payoff

This isn't academic. By chapter end, you'll solve a real problem:

**Before this chapter**: Tax season means hours of manual work - opening each bank statement, hunting for medical expenses, trying to remember which "SQ *LOCALSTORE" was business vs personal.

**After this chapter**: Download your bank CSVs, run one command, get a categorized report. Every year. Forever.

The same pattern applies to any data extraction problem - expense reports, invoice processing, log analysis. You're learning to build tools, not just use them.


